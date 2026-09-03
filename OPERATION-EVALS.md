Operation evals for RAG Application answers a different question from quality evals such as correctness, faithfulness ettc.

Even if RAG system gives good answers, can it run reliably, quickly and economiclly in production?

No golden datasets or LLM-as-judge.

There are 3 major operational evals:
- Latency
- Cost
- Reliability
- Thoroughput

Donot wait until production to check if your appl is slow 

## Latency -
1) Amount of time a system takes to respond a request

Considerations :
- Prefer latency distribution over averages. Measure P50, P95 and P95 Latency
- Measure component-level latency, not only end-to-end latency
- Measure TTFT seperately.
- Watch for cold starts
- Record context size and token counts alongside latency
- Distinguish latency from throughput
- Repeat runs because external API are noisy.
- Track failures seperately from latency.
- Set latency budgets at both system and component level
- Use representative and segmented workloads.

## How to improve latency
- Reduce generator time
1) use a faster model
2) simpler model for simple question
3) Ask generator model to give consise answers
- Reduce input size
- Analyze retriever more
- Caching
- Optimize infra distance

Embedding Cache
Retrieval cache
Reranking cache
System prompt cache


## Cost

monetory expense incurred to process a user query, driven primarily by LLM tokens consumed during generation.

Considerations : 
- Measure cost per query
- Measure input and output cost seperately
- Measure cost as a distribution
- Segment cost by query type
- Set a cost budget

How to reduce cost ?
- Reduce retrieved context size
- Use smaller chunk or contextual compression
- Reduce unnecessary prompt tokens
- Reduce o/p length
- use cheaper model
- Use caching