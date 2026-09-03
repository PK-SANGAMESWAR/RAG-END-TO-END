# EvalLens

EvalLens is an end-to-end Retrieval-Augmented Generation (RAG) assistant for an LLM-evaluations course, built as a practical evaluation project. It answers questions from course-transcript material while keeping responses grounded in retrieved context, then evaluates the system across retrieval quality, generation quality, safety, operational behaviour, and regressions.

> **Project status:** Offline evaluation is implemented. Production **online evaluations** are the next planned phase.

## What it does

1. Loads WebVTT course transcripts from `data/`.
2. Chunks them, embeds the chunks with OpenAI embeddings, and persists them in Chroma.
3. Retrieves a broad candidate set, then reranks it with a cross-encoder.
4. Generates a context-grounded teaching answer with `gpt-4o-mini`.
5. Measures the pipeline with curated golden datasets, DeepEval metrics, safety checks, operational measurements, and baseline-vs-candidate regression checks.

## Architecture

```text
Course transcripts (.vtt)
        |
        v
Chunking + text-embedding-3-large
        |
        v
Chroma vector store
        |
        v
Retrieve 10 candidates -> cross-encoder rerank -> retain top 5
        |
        v
Grounded generator (gpt-4o-mini, temperature=0)
        |
        v
Answer + evaluation suite
```

The generator is instructed to use only retrieved context and to abstain when the course material does not contain enough information. Its prompt also includes safeguards for prompt injection, unsafe language, private data, and protected course-content extraction.

## Evaluation coverage

The evaluation suite constructs one pipeline instance and injects it into each relevant evaluation, so a saved snapshot represents one consistent system configuration.

| Area | What is evaluated |
| --- | --- |
| Retriever | Contextual recall and precision, including reranker performance |
| Generator | Faithfulness and answer relevancy using ideal contexts |
| RAG pipeline | Contextual relevancy, faithfulness, and answer relevancy on live retrieval |
| Application | Correctness, completeness, and teaching style |
| Safety | Scope adherence, prompt-leakage resistance, and toxicity behaviour |
| Operations | Latency (including TTFT), estimated token cost, and reliability |
| Regression | Baseline/candidate snapshot comparison with pass, fail, and review outcomes |

### Current offline findings

The currently adopted retrieval configuration uses `text-embedding-3-large`, 500-character chunks with 100-character overlap, and retrieves 10 candidates before reranking down to 5. In the recorded reranker comparison, contextual recall remained **0.99**, contextual precision increased from **0.86 to 0.87**, and pass rate increased from **80.0% to 86.67%**.

The generator evaluation recorded **0.96 faithfulness** (15/15 passing) and **0.94 answer relevancy** (14/15 passing). See [RAN.md](RAN.md) and [PROGRESS.md](PROGRESS.md) for the detailed observations and experiment history.

## Getting started

### Prerequisites

- Python 3.12+
- An OpenAI API key

### Install

Using `uv`:

```powershell
uv sync
```

Or using pip:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a `.env` file in the repository root:

```env
OPENAI_API_KEY=your_key_here
```

### Build the local vector store

Run this after a fresh clone, after changing the transcript corpus, or after changing chunking/embedding configuration:

```powershell
.\.venv\Scripts\python.exe src\retriever.py
```

This creates `chroma_store/`, which is intentionally ignored by Git because it can always be rebuilt from `data/`.

### Run a smoke test

```powershell
.\.venv\Scripts\python.exe -m src.rag_pipeline
```

## Running evaluations

Run the full offline suite and save a candidate snapshot:

```powershell
.\.venv\Scripts\python.exe -m evals.run_suite --label "current pipeline" --full
```

Create an approved regression baseline:

```powershell
.\.venv\Scripts\python.exe -m evals.run_suite --baseline --label "approved baseline" --full
```

Compare the current candidate with the baseline:

```powershell
.\.venv\Scripts\python.exe -m evals.compare --all
```

Run one focused evaluation while iterating:

```powershell
.\.venv\Scripts\python.exe -m evals.eval_retriever
.\.venv\Scripts\python.exe -m evals.eval_retriever_with_reranker
.\.venv\Scripts\python.exe -m evals.eval_generator
.\.venv\Scripts\python.exe -m evals.eval_rag_pipeline
.\.venv\Scripts\python.exe -m evals.eval_application
.\.venv\Scripts\python.exe -m evals.eval_safety
.\.venv\Scripts\python.exe -m evals.eval_ops
```

More detailed run and regression instructions are in [RUN.md](RUN.md) and [REGRESSION-TESTING.md](REGRESSION-TESTING.md).

## Repository layout

```text
src/          RAG components: retrieval, reranking, generation, pipeline
data/         WebVTT course transcripts used as the knowledge base
goldens/      Curated evaluation datasets
evals/        Quality, safety, operations, and regression evaluation code
baselines/    Saved baseline and candidate metric snapshots
resources/    Supporting evaluation examples and notes
```

## Next: online evaluations

The current suite evaluates the system offline, using fixed datasets and controlled requests. The remaining work is to add online evaluation for live traffic after deployment, such as production tracing, sampled answer-quality review, user feedback signals, drift detection, alerting, and segmented latency/cost/reliability monitoring.

## Notes

- Evaluation calls and embeddings use paid external API services.
- First-time reranker use downloads `cross-encoder/ms-marco-MiniLM-L-6-v2` locally.
- The project is intended as an educational evaluation workflow, not a production deployment by itself.

## License

See [LICENSE](LICENSE).
