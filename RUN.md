python src/retriever.py
python goldens/goldens_generator.py
python -m evals.eval_retriever.py
python -m evals.eval_retriever_with_reranker.py
