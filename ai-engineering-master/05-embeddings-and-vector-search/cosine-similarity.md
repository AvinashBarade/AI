# Cosine Similarity

Cosine similarity measures the angle between vectors, ignoring magnitude when vectors are L2-normalized—standard for text embeddings.

\[
\text{sim}(a,b) = \frac{a \cdot b}{\|a\| \|b\|}
\]

Many APIs return **cosine distance** = 1 − sim; know which your DB exposes.

## Normalization

If embeddings are not normalized, dot product and cosine diverge—verify model card defaults.

## ANN indexes

Approximate nearest neighbor (HNSW, IVF) trades recall for speed. Tune `ef_search` / `nprobe` on your eval set; wrong settings look like “search broke” after scale-up.
