# Linear Algebra for AI Engineering

Skip the proof course. Learn the **shapes, operations, and intuitions** that show up in embeddings, attention, and GPU OOM errors.

## Vectors and dot products

An embedding is a vector \(\mathbf{v} \in \mathbb{R}^d\). The **dot product** \(\mathbf{a}\cdot\mathbf{b} = \sum_i a_i b_i\) measures alignment.

If vectors are **unit length** (many APIs L2-normalize), dot product equals **cosine similarity**. That’s why retrieval code often does `query @ docs.T` after normalization.

## Matrices are batch operations

A layer in a transformer is mostly **matrix multiply**: \(\mathbf{Y} = \mathbf{X}\mathbf{W}\). GPU kernels love large, regular matmuls—that’s why batching matters.

Shape discipline:

```text
batch × sequence × hidden
batch × heads × seq × head_dim
```

When you see `matmul` errors in PyTorch, it’s almost always a **shape** bug.

## Attention in one picture

For each token you form query \(\mathbf{q}\), compare to all keys \(\mathbf{k}_j\), softmax into weights, sum value vectors \(\mathbf{v}_j\):

\[
\text{Attention}(Q,K,V)=\text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
\]

**Multi-head** = run several attention “subspaces” in parallel, concatenate, project.

You won’t implement this in your API service—but you **will** explain why long context costs more (bigger \(QK^\top\)).

## Why \(\sqrt{d_k}\) scaling

Dot products grow in magnitude with dimension; softmax saturates (one weight → 1, rest → 0). Scaling keeps gradients healthier. Interviewers ask this because it signals you read past the API docs.

## Worked retrieval toy example

Three doc embeddings (4D, pretend):

| Doc | Vector (simplified) |
|-----|---------------------|
| refund policy | [0.8, 0.1, 0.0, 0.2] |
| return item | [0.7, 0.2, 0.0, 0.1] |
| weather | [0.0, 0.1, 0.9, 0.0] |

Query “how do I return something?” should land nearest **return/refund** rows. If it doesn’t, check embedding model, normalization, or whether you need **hybrid** keyword search.

## NumPy you’ll actually use

```python
import numpy as np

def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))
```

## Production connections

| Topic | Where it shows up |
|-------|-------------------|
| Cosine vs L2 | Vector DB metric choice |
| Normalization | Score calibration across indexes |
| Dtype FP16/BF16 | Serving memory halved, rare numerical issues |
| Batch matmul | Embedding jobs, GPU utilization |

## Exercise

Implement cosine in **Go** on `[]float32`. Benchmark 10k comparisons—feel why ANN indexes exist.
