# Progress so far

A record of what's been built in this repo. See [CLAUDE.md](CLAUDE.md) for
architecture/commands and [HELP.md](HELP.md) for the conceptual notes behind
these decisions.

## Goal

Evaluate the **retriever half** of a RAG pipeline in isolation — no
generator/answering LLM is in scope. Corpus is 8 WebVTT "LLM Evals" session
transcripts in [data/](data/).

## 1. Project setup

- `uv`-managed Python 3.12 project (`pyproject.toml`, `uv.lock`), unpinned
  `requirements.txt` mirror, `.venv/` local env.
- `.env` for `OPENAI_API_KEY` (empty placeholder in the committed copy).

## 2. Retriever ([src/retriever.py](src/retriever.py))

- `load_transcripts()`: reads each `.vtt`, strips `WEBVTT` header and
  `-->` timestamp lines, joins the rest into one `Document` per transcript
  with `metadata={"session": N}` parsed from the filename.
- Chunking happens after loading: `RecursiveCharacterTextSplitter`,
  `CHUNK_SIZE=1000` / `CHUNK_OVERLAP=150`.
- Embeddings: started on `text-embedding-3-small`, moved to
  `text-embedding-3-large`.
- Persisted to a local Chroma store (`chroma_store/`, gitignored); `load_store()`
  reuses the folder if it already exists rather than re-embedding every run.
- `build_retriever(k=TOP_K)` wraps it as a LangChain retriever, `TOP_K=5`.
- All four hyperparameters (`EMBED_MODEL`, `CHUNK_SIZE`, `CHUNK_OVERLAP`,
  `TOP_K`) live in this one file and are imported everywhere else so logged
  eval runs can't drift from what actually executed.

## 3. Golden dataset ([goldens/](goldens/))

- Tried the DeepEval synthesizer first (`goldens_generator.py`, seeded at 42) —
  judged the output poor quality.
- Fell back to a hand-curated set: [retriever_goldens.json](goldens/retriever_goldens.json),
  15 `{id, query, ideal_answer, source}` rows written against ideal answers
  (not chunk IDs — see HELP.md for why chunk-id-keyed goldens break the moment
  chunking params change).
- `goldens_generator.py` only ever writes the draft file
  (`retriever_deepeval_goldens.json`); the reviewed golden set is never
  overwritten automatically.

## 4. Evaluation ([evals/](evals/))

- `eval_retriever.py`: baseline — runs each golden query through
  `build_retriever()`, wraps results as DeepEval `LLMTestCase`s
  (`actual_output` is an intentional placeholder — no generator under test),
  scores with `ContextualRecallMetric` + `ContextualPrecisionMetric`
  (threshold 0.7, judge pinned to `gpt-4.1-mini`).
- `hyperparameters={...}` on `evaluate()` logs retriever config per run so
  DeepEval's dashboard can compare runs meaningfully; each variant gets a
  distinct `"retriever"` label (`base_k5` vs `reranked_...`).

## 5. Reranker ([src/reranker.py](src/reranker.py))

- `RerankingRetriever`: over-retrieves `fetch_k=10` with the bi-encoder
  (Chroma similarity search), rescores every (query, chunk) pair with a
  CPU cross-encoder (`cross-encoder/ms-marco-MiniLM-L-6-v2`), keeps the
  top `top_k=5`.
- Duck-types `.invoke(query) -> list[Document]` so it drops straight into
  `eval_retriever_with_reranker.py` in place of the plain LangChain retriever.

## 6. Bugs fixed

- **Stale API key shadowing**: a stale User-level Windows `OPENAI_API_KEY` env
  var was shadowing `.env` under dotenv's default `override=False`, causing
  silent 401s with a key that appears nowhere in the repo.
  Fix: `load_dotenv(override=True)` everywhere (`src/retriever.py`, both
  eval scripts, `goldens_generator.py`, `resources/deepeval_intro.py`).
  Documented in CLAUDE.md's Gotchas section.
- **DeepEval disk-cache crash on Windows**: `evaluate()`'s on-disk test-run
  cache uses a non-blocking file lock (`portalocker`) that isn't reliable on
  Windows without the `win32` extra. Under async concurrency the lock
  acquisition can fail entirely, leaving the in-memory cache object `None`
  and crashing with `'NoneType' object has no attribute
  'test_cases_lookup_map'` (as opposed to the merely-noisy "Lock acquisition
  failed" warning it prints the rest of the time). Caching also buys nothing
  here since goldens/config differ every run. Fix: pass
  `cache_config=CacheConfig(write_cache=False)` to `evaluate()`. Applied in
  `eval_retriever.py`, `eval_retriever_with_reranker.py`, and
  `eval_rag_pipeline.py`; `eval_generator.py` doesn't have it yet and is
  exposed to the same intermittent crash.

## 7. Tuning pass — what was tried

Four knobs were swept, in this order, against the 15-row golden set (judge
`gpt-4.1-mini`, threshold 0.7 on both metrics). Exact per-run scores were only
captured on disk for the last one (embedding model + k + chunking were eyeballed
across runs, not logged) — see the table below for the numbers that do exist.

- **Embedding model — `text-embedding-3-small` vs `text-embedding-3-large`**:
  large gave better recall/precision, so it's what the repo now runs on
  (`EMBED_MODEL` in [src/retriever.py](src/retriever.py)). Exact scores for
  the `small` run weren't saved.
- **`TOP_K` sweep**: confirmed the tradeoff HELP.md predicted — lowering k
  raised precision (fewer irrelevant chunks in the context window) but cost
  recall (more likely to miss a relevant chunk entirely). `TOP_K=5` was kept
  as the balance point; exact scores per k value weren't saved.
- **Chunk size / overlap sweep**: tried other `CHUNK_SIZE`/`CHUNK_OVERLAP`
  combinations away from 1000/150, none improved on it, so 1000/150 stayed.
  Exact scores per combination weren't saved.
- **Reranker** ([src/reranker.py](src/reranker.py)): the one run with numbers
  actually captured (from [RAN.md](RAN.md)) — see table.

Final config at time of the reranker run: `text-embedding-3-large`, chunk size
1000 / overlap 150, `TOP_K=5` (reranker: `fetch_k=10` → cross-encoder
`ms-marco-MiniLM-L-6-v2` → `top_k=5`).

| Run                    | Contextual Recall | Contextual Precision | Pass rate        |
|-------------------------|:---:|:---:|:---:|
| Baseline (`base_k5`)    | 0.99 (15/15 pass) | 0.86 (12/15 pass) | 80.0%  |
| + Reranker (`reranked_fetch10_top5`) | 0.99 (15/15 pass) | 0.87 (13/15 pass) | 86.67% |

Recall was already effectively maxed at baseline (the right chunks are in the
top-10 candidate pool almost every time), so the reranker's job was purely to
fix ordering. It moved 1 of the 3 failing precision cases over the 0.70
threshold — the remaining 2 failures (`test_case_5`/"if a model tops all the
benchmarks...", `test_case_6`/"different ways an eval can be run") still have
an irrelevant chunk ranked above the relevant one even after rescoring, so the
cross-encoder narrows the ordering problem rather than eliminating it.

**Conclusion: reranker is a net win** — same recall, +1pt precision, +6.67pt
pass rate — at the cost of a CPU cross-encoder pass per query. Adopt it as the
new baseline for further tuning. Embedding model (large), k (5), and chunk
size/overlap (1000/150) were all swept too and each confirmed the current
setting as the best of what was tried, though without saved per-run scores —
worth re-running with `hyperparameters=` logging on if precise deltas are
needed later.

## 8. Generator eval — faithfulness & answer relevancy

A generator component was added on top of the retriever work above:
[src/generator.py](src/generator.py) (`generate()` / `generate_stream()`,
`gpt-4o-mini`, temperature 0) with a faithfulness-first prompt — answer only
from the supplied context, abstain with a fixed refusal string when the
context doesn't contain the answer, plus guardrails against prompt injection
from retrieved content, toxic/abusive framing, jailbreak/roleplay overrides,
and leaking system-prompt or PII details. This is a deliberate exception to
CLAUDE.md's "no generator in scope" — the task here was explicitly about
generation quality, not retrieval.

[evals/eval_generator.py](evals/eval_generator.py) scores it in isolation:
each case is run with the **golden `ideal_context`** from
`goldens/faithfulness_dataset.json` (15 rows), not the retriever's actual
output, so a low score can only be the generator's fault, not the
retriever's. Metrics are `FaithfulnessMetric` + `AnswerRelevancyMetric`,
threshold 0.7, judge `gpt-4o-mini`.

The prompt in `src/generator.py` went through several revisions — checking
answer relevancy and faithfulness after each change — before landing on the
current wording (explicit "cover every part of the question," "don't pad
with unrelated information," and the strict context-only/abstain rule).
The run captured in [RAN.md](RAN.md) is the result after that tuning:

| Metric | Average Score | Pass rate |
|---|:---:|:---:|
| Faithfulness | 0.96 | 100.0% (15/15) |
| Answer Relevancy | 0.94 | 93.33% (14/15) |

The one remaining failure is `test_case_3` ("can you give a real-world
example of an LLM application failing badly?", the Air Canada chatbot
example): Faithfulness barely passed (0.71 — the answer stayed grounded in
the context) but Answer Relevancy failed (0.67) because the answer spent
several sentences on background detail (the legal proceedings, the exact
refund amount) that wasn't squarely aimed at "give an example of a failure,"
diluting relevancy even though nothing in it was unsupported.

## 9. Full pipeline eval — the RAG triad ([src/rag_pipeline.py](src/rag_pipeline.py), [evals/eval_rag_pipeline.py](evals/eval_rag_pipeline.py))

Everything above evaluates the retriever and generator in isolation (the
retriever evals use a placeholder `actual_output`; §8's generator eval feeds
it the golden's hand-written `ideal_context` instead of anything actually
retrieved). This step wires them together for the first time: `RagPipeline`
runs the reranked retriever, then `generate()` on whatever it comes back
with, so each test case's `retrieval_context` and `actual_output` are both
*live* — no golden context anywhere in the loop.

`eval_rag_pipeline.py` reuses the 15 queries from
`goldens/faithfulness_dataset.json` (same file as §8) and scores with the
classic RAG triad: `ContextualRelevancyMetric`, `FaithfulnessMetric`,
`AnswerRelevancyMetric` — threshold 0.7, judge `gpt-4o-mini`. Run captured in
[RAN.md](RAN.md):

| Metric | Average Score | Pass rate |
|---|:---:|:---:|
| Contextual Relevancy | 0.44 | 6.67% (1/15) |
| Faithfulness | 0.95 | 100.0% (15/15) |
| Answer Relevancy | 0.86 | 80.0% (12/15) |

Two findings this run surfaced that neither isolated eval could have:

- **Contextual Relevancy almost universally fails, despite the reranker
  looking fine in §7.** The two metrics aren't measuring the same thing:
  `ContextualPrecisionMetric` (§7) judges *chunk-level ranking* — are
  relevant chunks ordered above irrelevant ones. `ContextualRelevancyMetric`
  judges *sentence-level* — of all statements inside the retrieved chunks,
  what fraction are actually about the question. A chunk can be the single
  best-ranked, correctly-on-topic match and still score low here if it's a
  1000-character slab of conversational transcript where only 2 of 12
  sentences address the query and the rest wander. That's most chunks in
  this corpus. Precision-at-ranking and relevancy-at-content are
  independent failure modes, and only the triad eval catches the second one.
- **`test_case_3` (the Air Canada chatbot example) flips from a pass in §8
  to an abstain here.** With the golden's `ideal_context` handed to it
  directly, the generator answered fine (Faithfulness 0.71, borderline
  Answer Relevancy 0.67). With the *actual* retriever+reranker output, it
  answered "I don't have enough information in the course material to
  answer that." — the real retrieval pipeline never surfaces that content
  for this query. §8's generator eval couldn't have shown this: it never
  gave the generator a chance to fail at retrieval, only at reasoning over
  context it was handed.

No `hyperparameters=` were logged on this run (RAN.md shows the "No
hyperparameters logged" warning), so it isn't yet comparable against a
future variant the way §7's runs are.

## 10. Chunk-size sweep against Contextual Relevancy ([evals/sweep_chunk_size.py](evals/sweep_chunk_size.py))

§9's hypothesis was that a 1000-char chunk carries too much off-topic
transcript alongside the on-topic sentences, so *smaller* `CHUNK_SIZE` should
raise Contextual Relevancy. Built a sweep script that rebuilds `chroma_store/`
per combo, reruns the full triad eval (`goldens/faithfulness_dataset.json`,
15 queries, judge `gpt-4o-mini`) with `hyperparameters=` logged this time, and
tested three smaller combos against the recorded 1000/150 baseline:

| chunk_size | chunk_overlap | Contextual Relevancy | Faithfulness | Answer Relevancy |
|---:|---:|:---:|:---:|:---:|
| 300  | 50  | 0.35  | 0.97  | 0.89  |
| 500  | 75  | 0.388 | 0.955 | 0.968 |
| 750  | 100 | 0.399 | 0.974 | 0.916 |
| **1000 (baseline)** | **150** | **0.44** | **0.95** | **0.86** |

**Hypothesis rejected.** Every smaller chunk size scored *worse* on Contextual
Relevancy than baseline, and the three swept values move monotonically toward
the baseline as chunk_size increases (0.35 → 0.388 → 0.399), i.e. the trend
points up past 1000, not down. Reading the per-test-case reasons from the
sweep runs, the likely explanation: DeepEval's `ContextualRelevancyMetric`
breaks each chunk into individual statements and judges each one against the
question — a smaller chunk doesn't remove the off-topic sentences, it just
retrieves fewer chunks' worth of them relative to the doubled `k=5` retrieval
window still needed to hold the answer, so the on-topic:off-topic *ratio*
inside what gets judged doesn't clearly improve, while shrinking the chunk
also risks cutting a relevant sentence away from the surrounding context that
would have anchored it as relevant. `CHUNK_SIZE`/`CHUNK_OVERLAP` in
`src/retriever.py` were left unchanged at 1000/150 — none of the tested
alternatives are a win. `chroma_store/` was rebuilt three times during the
sweep and deleted afterward so it doesn't silently mismatch those constants.

Not yet tried: chunk sizes *larger* than 1000 (the direction the trend
actually points), and non-chunking fixes for Contextual Relevancy specifically
— e.g. a post-retrieval sentence/passage extraction step before the generator
sees the context, since the failure mode is sentence-level noise within an
already-correctly-ranked chunk, not a ranking or recall problem.

## Where things stand / not yet done

- Baseline vs. reranked comparison above is the first locked-in measurement
  (HELP.md's "we'll get a new baseline" is now done).
- Ideas noted but not implemented: tuning chunk size to see if it helps the
  2 still-failing precision cases, lowering k to trade recall for precision,
  trying a different embedding model, trying a stronger/different reranker
  (or a higher `fetch_k` before rescoring).
- Generator eval: only one prompt-revision's numbers were saved (the table
  in §8); intermediate prompt attempts and their scores weren't logged.
  `test_case_3`'s relevancy failure suggests a tighter "stay on the exact
  question asked, don't narrate surrounding detail" instruction is the next
  thing to try in the prompt.
- Full-pipeline triad (§9): Contextual Relevancy failing on 14/15 cases is
  still the biggest open problem in the repo. §10 ruled out smaller
  `CHUNK_SIZE` as the fix — it made things worse. Next to try: chunk sizes
  *larger* than 1000 (the direction §10's trend points), or a
  sentence/passage-level re-extraction step before handing context to the
  generator, since the failure is sentence-level noise inside otherwise
  correctly-ranked chunks, not a `k`/ranking problem.
  Also worth checking whether `test_case_3`'s retrieval miss (no Air Canada
  content surfaced) is a one-off or a pattern — would need looking at what
  the retriever actually returns for that query.
- `eval_generator.py` still lacks the `CacheConfig(write_cache=False)` fix
  from §6 and can hit the same intermittent crash the other three eval
  scripts were patched for.
