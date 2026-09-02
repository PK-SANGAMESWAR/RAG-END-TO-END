import json

from dotenv import load_dotenv

from deepeval import evaluate
from deepeval.evaluate import CacheConfig
from deepeval.test_case import LLMTestCase
from deepeval.metrics import ContextualRecallMetric, ContextualPrecisionMetric

from src.retriever import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    EMBED_MODEL,
    TOP_K,
    build_retriever,
)

load_dotenv(override=True)  # .env wins over a stale OS-level OPENAI_API_KEY

GOLDEN_PATH = "goldens/retriever_goldens.json"
JUDGE_MODEL = "gpt-4.1-mini"  
THRESHOLD = 0.7


# 1. LOAD the golden set --- the fixed, human-authored truth
with open(GOLDEN_PATH) as f:
    goldens = json.load(f)


# 2. RUN THE RETRIEVER on each question to fill retrieval_context,
#    then build one test case per golden.
retriever = build_retriever()

test_cases = []

for g in goldens:
    retrieved = retriever.invoke(g["query"])
    retrieval_context = [doc.page_content for doc in retrieved]

    test_cases.append(
        LLMTestCase(
            input=g["query"],
            expected_output=g["ideal_answer"],
            retrieval_context=retrieval_context,
            actual_output="(generator not evaluated in this run)",
        )
    )


# 3. THE METRICS --- recall (did we miss?) and precision (ranked well?)
metrics = [
    ContextualRecallMetric(threshold=THRESHOLD, model=JUDGE_MODEL, include_reason=True),
    ContextualPrecisionMetric(threshold=THRESHOLD, model=JUDGE_MODEL, include_reason=True),
]


# 4. EVALUATE --- every metric on every case, batched + parallel, with a printed report
evaluate(
    test_cases=test_cases,
    metrics=metrics,
    # write_cache=False: deepeval's on-disk test-run cache uses a non-blocking
    # file lock that's prone to contention under Windows async concurrency,
    # crashing with `'NoneType' object has no attribute 'test_cases_lookup_map'`.
    # Caching buys nothing here anyway since goldens/config differ every run.
    cache_config=CacheConfig(write_cache=False),
    hyperparameters={
        "retriever": f"base_k{TOP_K}",   # vs "reranked" -- see eval_retriever_with_reranker.py
        "embedding_model": EMBED_MODEL,
        "chunk_size": CHUNK_SIZE,
        "chunk_overlap": CHUNK_OVERLAP,
        "top_k": TOP_K,
        "judge_model": JUDGE_MODEL,
        "golden_set": GOLDEN_PATH,
    },
)