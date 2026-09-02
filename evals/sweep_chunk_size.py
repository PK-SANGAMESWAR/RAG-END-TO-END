"""
evals/sweep_chunk_size.py — chunk_size/chunk_overlap sweep against the full
RAG-triad eval (ContextualRelevancy + Faithfulness + AnswerRelevancy).

Why this exists: eval_rag_pipeline.py at the current CHUNK_SIZE=1000/
CHUNK_OVERLAP=150 scored Contextual Relevancy 0.44 (1/15 pass) — see RAN.md
and PROGRESS.md §9. The diagnosis there: a 1000-char chunk of raw transcript
carries a lot of off-topic sentences alongside the on-topic ones, so even a
correctly-ranked chunk drags relevancy down. PROGRESS.md's suggested next
step is smaller CHUNK_SIZE.

Runs ONE (chunk_size, chunk_overlap) combo per process invocation and appends
one JSON line to evals/sweep_results.jsonl. One combo per process on purpose:
on Windows, Chroma's on-disk index (hnswlib mmap + sqlite) doesn't release
its file handles when the Python objects go out of scope, so rebuilding
chroma_store/ for a second combo in the same process hits a PermissionError.
A fresh process per combo guarantees the OS releases the handles on exit.

Run one combo:  python -m evals.sweep_chunk_size --chunk-size 500 --chunk-overlap 75
Then print the comparison table: python -m evals.sweep_chunk_size --summary

Deliberately does NOT touch fetch_k/top_k — one variable at a time.
Cost per combo: one chroma_store rebuild + one full triad eval (15 queries x
3 judge metrics x gpt-4o-mini, plus 15 real generate() calls).
"""

import argparse
import json
import os
import shutil

from dotenv import load_dotenv

from deepeval import evaluate
from deepeval.evaluate import CacheConfig
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    ContextualRelevancyMetric,
    FaithfulnessMetric,
    AnswerRelevancyMetric,
)

import src.retriever as retriever_mod
from src.rag_pipeline import RagPipeline

load_dotenv(override=True)  # .env wins over a stale OS-level OPENAI_API_KEY

GOLDEN_PATH = "goldens/faithfulness_dataset.json"
JUDGE_MODEL = "gpt-4o-mini"
THRESHOLD = 0.7
RESULTS_PATH = "evals/sweep_results.jsonl"

# Recorded baseline (RAN.md / PROGRESS.md §9) at CHUNK_SIZE=1000/OVERLAP=150 —
# not rerun by this script, just carried into the summary table for comparison.
BASELINE = {
    "chunk_size": 1000,
    "chunk_overlap": 150,
    "Contextual Relevancy": 0.44,
    "Faithfulness": 0.95,
    "Answer Relevancy": 0.86,
}


def run_combo(chunk_size, chunk_overlap):
    if os.path.exists(retriever_mod.DB_DIR):
        shutil.rmtree(retriever_mod.DB_DIR)

    # load_store() reads these as module globals at call time, so patching
    # them here is enough to rebuild with new params without editing the
    # single-source-of-truth constants in src/retriever.py.
    retriever_mod.CHUNK_SIZE = chunk_size
    retriever_mod.CHUNK_OVERLAP = chunk_overlap

    with open(GOLDEN_PATH) as f:
        goldens = json.load(f)

    rag = RagPipeline()

    test_cases = []
    for g in goldens:
        result = rag.invoke(g["query"])
        test_cases.append(
            LLMTestCase(
                input=g["query"],
                actual_output=result["answer"],
                retrieval_context=result["context"],
            )
        )

    metrics = [
        ContextualRelevancyMetric(threshold=THRESHOLD, model=JUDGE_MODEL, include_reason=True),
        FaithfulnessMetric(threshold=THRESHOLD, model=JUDGE_MODEL, include_reason=True),
        AnswerRelevancyMetric(threshold=THRESHOLD, model=JUDGE_MODEL, include_reason=True),
    ]

    eval_result = evaluate(
        test_cases=test_cases,
        metrics=metrics,
        cache_config=CacheConfig(write_cache=False),
        hyperparameters={
            "retriever": f"triad_chunk{chunk_size}_ov{chunk_overlap}",
            "embedding_model": retriever_mod.EMBED_MODEL,
            "chunk_size": chunk_size,
            "chunk_overlap": chunk_overlap,
            "top_k": rag.retriever.top_k,
            "fetch_k": rag.retriever.fetch_k,
            "reranker_model": "cross-encoder/ms-marco-MiniLM-L-6-v2",
            "judge_model": JUDGE_MODEL,
            "golden_set": GOLDEN_PATH,
        },
    )

    scores = {}
    for tc in eval_result.test_results:
        for m in tc.metrics_data:
            scores.setdefault(m.name, []).append(m.score)

    row = {"chunk_size": chunk_size, "chunk_overlap": chunk_overlap}
    for name, vals in scores.items():
        row[name] = round(sum(vals) / len(vals), 3)

    with open(RESULTS_PATH, "a") as f:
        f.write(json.dumps(row) + "\n")

    print(f"\nSWEEP RESULT: {row}")
    return row


def print_summary():
    rows = [BASELINE]
    if os.path.exists(RESULTS_PATH):
        with open(RESULTS_PATH) as f:
            rows += [json.loads(line) for line in f if line.strip()]

    print(f"\n{'chunk_size':>10} {'overlap':>8} {'Ctx.Relevancy':>14} {'Faithfulness':>13} {'Ans.Relevancy':>14}")
    for r in rows:
        print(
            f"{r['chunk_size']:>10} {r['chunk_overlap']:>8} "
            f"{r.get('Contextual Relevancy', float('nan')):>14} "
            f"{r.get('Faithfulness', float('nan')):>13} "
            f"{r.get('Answer Relevancy', float('nan')):>14}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunk-size", type=int)
    parser.add_argument("--chunk-overlap", type=int)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()

    if args.summary:
        print_summary()
    elif args.chunk_size is not None and args.chunk_overlap is not None:
        run_combo(args.chunk_size, args.chunk_overlap)
    else:
        parser.error("pass --chunk-size and --chunk-overlap, or --summary")
