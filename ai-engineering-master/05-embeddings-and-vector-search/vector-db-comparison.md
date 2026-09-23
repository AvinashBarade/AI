# Vector DB Comparison

No universal winner—match **existing ops skills**, **query pattern**, and **scale**.

```text
        │ pgvector │ Qdrant │ Milvus │ OpenSearch k-NN
────────┼──────────┼────────┼────────┼──────────────────
ACL/SQL │   ★★★    │  ★★    │  ★★    │      ★★
Scale   │   ★★     │  ★★★   │  ★★★   │      ★★★
Ops sim │   ★★★    │  ★★    │  ★     │      ★★
Hybrid  │  tsvector│ payload│ varies │ native BM25+vec
```

## Decision workflow

1. Prove retrieval quality with **your** embedder and corpus on a sample index.
2. Measure p95 query latency at target QPS with filters.
3. Price RAM, egress, and engineer time for HA.

## Exit strategy

Abstract storage behind `VectorStore` interface—migrations hurt but are inevitable when scale crosses tiers.
