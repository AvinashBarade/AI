# NumPy for AI Workloads

NumPy is **contiguous typed arrays** plus vectorized ops. Embeddings, batch similarity, and reading PyTorch tensors all pass through this mental model.

## Shapes matter more than syntax

A matrix of embeddings is `(num_vectors, dimension)`. A batch of sequences in deep learning is `(batch, seq, hidden)`—you’ll see that in error messages long before you train anything.

**Broadcasting** lets you combine arrays of different shapes without explicit loops—powerful and easy to misuse.

## The operation you’ll run constantly

Normalized rows + matrix multiply = cosine similarity search in brute-force form:

```python
import numpy as np

Q = queries / np.linalg.norm(queries, axis=1, keepdims=True)
D = docs / np.linalg.norm(docs, axis=1, keepdims=True)
scores = Q @ D.T
```

At millions of vectors you move this to Qdrant/Milvus—but you still prototype here.

## dtypes

`float32` is the default for ML storage and GPU. `float64` wastes memory. Mixed precision (FP16/BF16) is a serving topic, but NumPy is where you first see dtype mistakes.

## Exercise

Generate 1,000 random unit vectors in 384-D. For 10 queries, print top-5 indices by dot product. That is retrieval without the database.
