# Embeddings

An embedding maps text (or tokens) to a dense vector \(\mathbb{R}^d\). Similar meaning → nearby vectors **if** the model was trained for that notion of similarity.

## Two different uses

1. **Input embeddings** inside the LLM (learned lookup table per token ID).
2. **Sentence/document embeddings** from encoder models (e5, BGE, etc.) for search.

Don’t confuse them in architecture diagrams.

## Similarity

Cosine on L2-normalized vectors equals dot product. Many APIs return normalized vectors—check model card.

## Production

- Embedding model version must match index version.
- Batch embed offline; cache doc vectors.
- Evaluate retrieval with **your** queries, not MTEB leaderboard alone.
