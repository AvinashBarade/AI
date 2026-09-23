# Reranking

First stage: fast bi-encoder retrieval (top 50–100). Second stage: **cross-encoder** or LLM scores `(query, chunk)` pairs accurately—expensive.

Cascade keeps p95 latency bounded: only rerank top 20.

## When worth it

Hard paraphrase queries, dense technical docs, support tickets where lexical overlap is weak.

## Cost

Reranker API calls per query—attribute cost in gateway metrics.
