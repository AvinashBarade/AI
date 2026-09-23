# Embedding Models

An embedding model maps text (or images) to a **dense vector** such that semantic similarity ≈ geometric closeness. RAG, clustering, and dedup all depend on picking and **pinning** a model version.

## Bi-encoders vs cross-encoders

| Type | When | Cost |
|------|------|------|
| Bi-encoder | Index + query embed once | Cheap at scale |
| Cross-encoder | Rerank pairs | Expensive per pair |

Production search is almost always bi-encoder first.

## Model choice axes

- Dimension (768 vs 1536)—higher not always better if index RAM explodes.
- Multilingual vs English-only.
- Domain fit (legal, code)—generic models miss jargon; consider domain-tuned embedders or hybrid BM25.

## Operational rule

Every vector record stores `embedding_model` and `model_revision`. Reindex on change—never mix versions in one logical index.
