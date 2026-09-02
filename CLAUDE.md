# CLAUDE.md

## What this project is

A teaching/experimentation repo for **evaluating the retrieval half of a RAG
pipeline**. The corpus is 8 WebVTT transcripts of "LLM Evals" sessions in
[data/](data/). There is deliberately **no generator/answering LLM** — the
whole project measures the *retriever*, not end-to-end answers.

The workflow it exists to support: build a retriever → measure contextual
recall & precision against a golden set → change one thing (chunking, embedding
model, k, reranker) → re-measure → compare.

[HELP.md](HELP.md) is the author's running conceptual notes (why recall/precision,
why golden datasets keyed on chunk-ids are a bad idea, what to try next). Read it
for intent before changing evaluation logic.

## Commands

Run everything **from the repo root** — every path is CWD-relative.

```bash
python src/retriever.py                      # build/load store + smoke-test one query
python -m goldens.goldens_generator          # regenerate DRAFT goldens (needs human review)
python -m evals.eval_retriever               # baseline
python -m evals.eval_retriever_with_reranker # + cross-encoder reranker
```

Package manager is **uv** (`uv.lock`, `.python-version` = 3.12); `requirements.txt`
is an unpinned mirror of `pyproject.toml`. Local venv is `.venv/`.

Needs a real `OPENAI_API_KEY` in `.env` — the committed `.env` holds an empty
placeholder, so a fresh clone will fail at embedding time until it's filled in.

## Architecture

```
data/*.vtt ──> load_transcripts() ──> chunk ──> OpenAI embeddings ──> chroma_store/
                                                                          │
                            goldens/retriever_goldens.json                │
                                     │                                    ▼
                                     └──────> evals/ ──> DeepEval ──> recall/precision
```

- [src/retriever.py](src/retriever.py) — VTT cleaning (drop `WEBVTT` + `-->`
  timestamp lines, join the rest), chunking, Chroma store, `build_retriever()`.
  Each transcript becomes **one `Document`** with `metadata={"session": N}`
  parsed out of the filename; chunking happens after.
- [src/reranker.py](src/reranker.py) — `RerankingRetriever`: over-retrieve
  `fetch_k=10` with the bi-encoder, rescore with a CPU cross-encoder, keep
  `top_k=5`. Duck-types `.invoke(query) -> list[Document]` so it drops into the
  eval scripts in place of the LangChain retriever.
- [evals/](evals/) — two near-identical scripts, one per retrieval config. They
  run at **import time** (no `main()`), which is why they must be launched with
  `python -m`.
- [goldens/retriever_goldens.json](goldens/retriever_goldens.json) — the 15-row
  golden set actually used: `{id, query, ideal_answer, source}`.

### Two things that are load-bearing

**1. The store is cached by directory existence.** `load_store()` returns the
existing `chroma_store/` if the folder is present and *never checks whether it
matches the current settings*. After changing `CHUNK_SIZE`, `CHUNK_OVERLAP`, or
`EMBED_MODEL` you **must** delete `chroma_store/` or you will silently evaluate
the old index. (A half-finished build also leaves a poisoned directory behind.)

**2. Retrieval hyperparameters live in one place.** `EMBED_MODEL`, `CHUNK_SIZE`,
`CHUNK_OVERLAP`, `TOP_K` are defined in `src/retriever.py` and imported by the
eval scripts for their `hyperparameters={...}` block. Keep it that way — these
were previously hardcoded per-file and had drifted from what the code ran, which
mislabels every result in the DeepEval dashboard. Never retype a value there.

## Evaluation conventions

- Metrics are `ContextualRecallMetric` and `ContextualPrecisionMetric`
  (reference-based, LLM-judged), `THRESHOLD = 0.7`.
- Judge model is pinned to `gpt-4.1-mini` for reproducibility. Changing the
  judge invalidates comparison against earlier runs — treat it as a new baseline.
- `actual_output` is a placeholder string in every test case. That is intentional:
  DeepEval requires the field, but no generator is under test. Don't "fix" it by
  wiring in an LLM unless the task is explicitly about generation.
- `hyperparameters=` on `evaluate()` is what makes runs comparable. Any new
  retrieval variant needs a distinct `"retriever"` label.
- **Goldens are reviewed artifacts, not build output.** `goldens_generator.py`
  writes to `retriever_deepeval_goldens.json` (a draft, seeded at 42) — it does
  *not* overwrite `retriever_goldens.json`. The author tried the DeepEval
  synthesizer, judged the output poor, and hand-curated the set in use.
  Never regenerate the live golden set as a side effect of another change.

## Gotchas

- **`load_dotenv(override=True)` everywhere — keep the flag.** This machine has a
  stale User-level `OPENAI_API_KEY` that shadows `.env` under dotenv's default
  `override=False`. Dropping the flag makes every script authenticate with the
  wrong key and 401 with a key that appears nowhere in the repo.
- A `401` means the key is wrong (likely shadowing, above); a `429
  insufficient_quota` means the key is fine and the account is out of credits.

- Running these scripts **costs money and time** (OpenAI embeddings + judge
  calls). Don't run a full eval to check a syntax change.
- The first reranker run downloads ~80MB of model weights.
- `chroma_store/` is gitignored and rebuildable; `data/` and `goldens/` are not
  reproducible — never delete them.
- `main.py` is unused `uv init` boilerplate.
  [resources/deepeval_intro.py](resources/deepeval_intro.py) is a standalone
  teaching demo, not part of the pipeline.
- VTT parsing assumes cue-payload-only files with no cue IDs, `NOTE` blocks, or
  speaker labels — true for the current data, worth re-checking if transcripts
  are added. Filenames must contain `Session <n>` or loading raises.
