import json

from dotenv import load_dotenv

from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import ContextualRecallMetric, ContextualPrecisionMetric

from src.reranker import CROSS_ENCODER, RerankingRetriever
from src.retriever import CHUNK_OVERLAP, CHUNK_SIZE, EMBED_MODEL

load_dotenv()

GOLDEN_PATH = "goldens/retriever_goldens.json"
JUDGE_MODEL = "gpt-4.1-mini"  
THRESHOLD = 0.7


# 1. LOAD the golden set --- the fixed, human-authored truth
with open(GOLDEN_PATH) as f:
    goldens = json.load(f)


# 2. RUN THE RETRIEVER on each question to fill retrieval_context,
#    then build one test case per golden.
retriever = RerankingRetriever()

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
    hyperparameters={
        "retriever": f"reranked_fetch{retriever.fetch_k}_top{retriever.top_k}",
        "embedding_model": EMBED_MODEL,
        "chunk_size": CHUNK_SIZE,
        "chunk_overlap": CHUNK_OVERLAP,
        "fetch_k": retriever.fetch_k,
        "top_k": retriever.top_k,
        "reranker_model": CROSS_ENCODER,
        "judge_model": JUDGE_MODEL,
        "golden_set": GOLDEN_PATH,
    },
)