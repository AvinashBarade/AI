# Linear Algebra for AI Engineering

Focus: **embeddings, attention, and tensor shapes**—not abstract proofs.

## 1. Mental Model

Linear algebra is the **coordinate system** of deep learning. Vectors are points; matrices are transformations; dot products measure alignment.

**Visualize:** An embedding is a point in high-dimensional space. Similar texts → nearby points. A weight matrix **rotates/stretches** space so that “king − man + woman ≈ queen” (classic word2vec intuition).

---

## 2. Why It Exists

Neural networks are chained **matrix multiplications** + nonlinearities. GPUs are fast at GEMM (general matrix multiply). You reason about:

- Shape errors (`matmul` incompatible dims)
- Memory (`batch × seq × hidden`)
- Attention as weighted sums of vectors

---

## 3. Architecture

```text
  tokens (ids)  →  Embedding matrix E  →  vectors x ∈ R^d
                           │
                           ▼
              Layers: x' = σ(W x + b)   (W ∈ R^{d×d'})
                           │
                           ▼
              Attention: softmax(QK^T / √d) V
```

---

## 4. Internal Working

### Vectors and dot product

\(a \cdot b = \sum_i a_i b_i\). For unit vectors, dot product = cosine similarity.

### Matrices

\(y = Ax\): linear map. Stacking layers = composing maps (with ReLU etc. breaking strict linearity).

### Attention (engineering view)

For each query token, scores against all keys → softmax weights → sum values.

\[
\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right) V
\]

**Multi-head:** parallel attention subspaces, concatenated.

### Shapes (decoder LLM)

Roughly: `batch`, `seq_len`, `hidden_dim`, `num_heads`, `head_dim` where `hidden = heads * head_dim`.

---

## 5. Example

Three sentence embeddings (toy 4D):

```text
"refund policy"  → [0.8, 0.1, 0.0, 0.2]
"return item"    → [0.7, 0.2, 0.0, 0.1]
"weather today"  → [0.0, 0.1, 0.9, 0.0]
```

Query “how do I return?” embeds near refund/return; cosine similarity ranks retrieval.

---

## 6. Implementation

NumPy: embedding table + cosine similarity.

```python
import numpy as np

def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))

E = np.array([
    [0.8, 0.1, 0.0, 0.2],
    [0.7, 0.2, 0.0, 0.1],
    [0.0, 0.1, 0.9, 0.0],
])
query = np.array([0.75, 0.15, 0.0, 0.15])
sims = [cosine_sim(query, E[i]) for i in range(len(E))]
best = int(np.argmax(sims))
```

Toy attention scores (single head):

```python
Q = K = V = np.random.randn(4, 8)  # seq=4, d=8
scores = Q @ K.T / np.sqrt(8)
weights = np.exp(scores - scores.max(axis=-1, keepdims=True))
weights /= weights.sum(axis=-1, keepdims=True)
out = weights @ V
```

---

## 7. Production Considerations

- **Dimension `d`:** higher → better quality often, more storage in vector DB (4 bytes × d per float32 vector).
- **Normalization:** many embedding APIs return unit vectors → dot product = cosine.
- **Batching:** matmul efficiency depends on consistent shapes; padding wastes compute.
- **Mixed precision:** FP16/BF16 halves memory; risk numerical edge cases in training; inference often OK.

---

## 8. Trade-offs

| Representation | Pros | Cons |
|----------------|------|------|
| Sparse one-hot | Exact token ID | Huge dims, no similarity |
| Dense embedding | Semantic similarity | Approximate, model-dependent |
| Higher dimension | Finer discrimination | Cost storage/latency |

---

## 9. Debugging

- `CUDA error: misaligned address` / shape errors → print tensor shapes on each layer.
- Retrieval always wrong → check **normalization**, wrong embedding model, or metric (L2 vs cosine).
- Attention maps (viz tools) for debugging long-context misses.

---

## 10. Interview Questions

### Level 1

1. What is a vector?
2. Dot product geometric meaning?
3. What is a matrix?
4. Why cosine similarity for embeddings?
5. What is rank (intuition)?
6. Identity matrix?
7. What does transpose do?
8. Sparse vs dense?
9. What is embedding dimension?
10. GEMM?

### Level 2

1. Write attention formula.
2. Why scale by √d_k?
3. Parameters in embedding layer (vocab × d)?
4. Batch matrix multiply benefit on GPU?
5. L2 distance vs cosine when vectors normalized?
6. What is orthogonality?
7. Eigenvalues intuition (PCA)?
8. Why nonlinearity if stacks of linear layers collapse to one linear map?
9. Head dimension vs num heads trade-off?
10. How does positional info enter if attention is permutation-invariant?

### Senior

1. Memory estimate for KV cache (symbols).
2. Tensor parallelism splits which matrices?
3. Why FlashAttention helps (IO not math)?
4. Quantization impact on vector search?
5. Mixed precision failure modes?

### Staff

1. Choose embedding dim for 1B vectors—storage math.
2. ANN recall vs exact cosine at scale.

### Explain in an interview (30s)

Embeddings map discrete tokens or text into dense vectors where direction encodes meaning; transformers apply learned linear projections and attention—which is softmax-weighted mixing of vectors—so each token contextually updates before the next-token prediction.

---

## 11. Practical Exercise

Implement cosine similarity in **Go** for `[]float32` with SIMD-friendly loop; benchmark 1M comparisons vs naive Python for intuition (not to beat BLAS).

---

## 12. Mini Project

Visualize 2D PCA projection of 100 sentence embeddings (sklearn) colored by document category; note overlap regions where RAG will confuse.
