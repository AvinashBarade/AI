# Hybrid Search

Dense vectors miss **exact tokens** (SKUs, statute numbers, error codes). Sparse **BM25** keyword search catches them.

## Fusion

Run both retrievers, merge with **Reciprocal Rank Fusion (RRF)** or weighted linear combo. Tune on your eval queries—legal docs often need higher BM25 weight.

## Stack options

OpenSearch/Elasticsearch with vector field + pgvector with `tsvector` side by side—architecture varies; pattern is the same.
