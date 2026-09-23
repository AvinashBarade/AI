# Embedding Pipeline

Batch job: read chunks → call embedding model (API or local GPU) → upsert to vector store with metadata.

## Idempotency

Key chunks by `hash(content + doc_version)`. Re-embed only when content changes.

## Throughput

Batch size tuned to GPU/API limits. Dead-letter queue for failures; never silently drop docs.

## Version field

Store `embedding_model=v3` on every vector. Mixed versions in one index destroy recall—blue/green reindex when model changes.
