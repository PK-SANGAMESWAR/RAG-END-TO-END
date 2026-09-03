Run everything from the repo root -- all paths (`data/`, `chroma_store/`, `goldens/`) are relative to it.

```bash
python src/retriever.py                      # build/load the store + smoke-test a query
python -m goldens.goldens_generator          # regenerate DRAFT goldens (DeepEval synthesizer)
python -m evals.eval_retriever               # baseline retriever
python -m evals.eval_retriever_with_reranker # + cross-encoder reranker
```

The first run embeds all 8 transcripts (~697 chunks) and writes `chroma_store/`.
Later runs reuse it -- delete the folder to force a rebuild after changing
chunking or the embedding model.

python src/generator.py

.\.venv\Scripts\python.exe -m evals.eval_scope_safety

.\.venv\Scripts\python.exe -m evals.eval_leakage

.\.venv\Scripts\python.exe -m evals.eval_toxicity

.\.venv\Scripts\python.exe -m evals.eval_latency

.\.venv\Scripts\python.exe -m evals.eval_cost