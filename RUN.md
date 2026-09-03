# Running the RAG evaluation suite

Run every command from the repository root. The commands below use the project's
virtual environment and assume `.env` contains a valid `OPENAI_API_KEY`.

## 1. Prepare the retrieval store

Run this once after a fresh checkout, or after changing source documents,
chunking, or the embedding model:

```powershell
.\.venv\Scripts\python.exe src/retriever.py
```

The first run creates `chroma_store/`. Later runs reuse it.

## 2. Run individual evaluations

Use these while developing or investigating one area of the pipeline:

```powershell
.\.venv\Scripts\python.exe -m evals.eval_retriever
.\.venv\Scripts\python.exe -m evals.eval_retriever_with_reranker
.\.venv\Scripts\python.exe -m evals.eval_generator
.\.venv\Scripts\python.exe -m evals.eval_rag_pipeline
.\.venv\Scripts\python.exe -m evals.eval_application
.\.venv\Scripts\python.exe -m evals.eval_scope_safety
.\.venv\Scripts\python.exe -m evals.eval_leakage
.\.venv\Scripts\python.exe -m evals.eval_toxicity
.\.venv\Scripts\python.exe -m evals.eval_latency
.\.venv\Scripts\python.exe -m evals.eval_cost
.\.venv\Scripts\python.exe -m evals.eval_reliability
```

## 3. Measure normal evaluation noise (five unchanged runs)

Before setting regression tolerances, run the complete suite five times with no
pipeline changes. Keep each snapshot; do not overwrite the baseline.

```powershell
1..5 | ForEach-Object {
  .\.venv\Scripts\python.exe -m evals.run_suite `
    --out "baselines\noise_run_$_.json" `
    --label "unchanged pipeline run $_" `
    --quiet --full
}
```

This creates `baselines/noise_run_1.json` through `baselines/noise_run_5.json`.

## 4. Create an approved baseline

After confirming the pipeline is in an acceptable state, save the baseline that
future changes will be compared against:

```powershell
.\.venv\Scripts\python.exe -m evals.run_suite `
  --baseline `
  --label "approved baseline" `
  --full
```

This writes `baselines/baseline.json`.

## 5. Evaluate a candidate change

Make one scoped pipeline change, then generate a candidate snapshot:

```powershell
.\.venv\Scripts\python.exe -m evals.run_suite `
  --label "describe the pipeline change" `
  --full
```

This writes `baselines/candidate.json`.

## 6. Compare baseline and candidate

```powershell
.\.venv\Scripts\python.exe -m evals.compare --all
```

Exit codes are suitable for CI: `0` = PASS, `1` = FAIL, `2` = REVIEW.

To compare custom snapshot paths:

```powershell
.\.venv\Scripts\python.exe -m evals.compare `
  --baseline baselines\baseline.json `
  --candidate baselines\candidate.json `
  --all
```
