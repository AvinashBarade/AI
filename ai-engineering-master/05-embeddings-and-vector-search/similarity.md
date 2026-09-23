# Similarity in Vector Search

“Similar” is a **design choice**, not a universal truth. You define it via embedding geometry plus optional metadata filters.

## What similarity is not

Lexical match (“error 0x803”) may be **dissimilar** in cosine space while paraphrases cluster tightly. Hybrid search exists because pure dense similarity alone fails SKU/code queries.

## Score interpretation

Distance metrics are not calibrated probabilities. A score of 0.82 today may mean nothing after re-embedding. Use **relative rank** and threshold tuning on labeled queries.

## Eval

Build a query set with expected relevant doc IDs. Plot recall@k vs threshold before shipping “I don’t know” logic.
