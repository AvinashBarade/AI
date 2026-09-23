# Optimization for AI Engineering

## 1. Mental Model

Training finds parameters \(\theta\) that **minimize loss** \(\mathcal{L}(\theta)\) on data. Inference **freezes** \(\theta\) and only runs forward passes.

**Visualize:** Loss landscape = hilly terrain; gradient descent walks downhill. SGD adds noise (mini-batches) that can help escape shallow local minima. In huge LLMs, you rarely “solve” loss—you stop when validation metrics plateau.

---

## 2. Why It Exists

Without optimization, neural nets are random functions. **Backpropagation** computes \(\nabla_\theta \mathcal{L}\) efficiently; **optimizers** (Adam, AdamW) choose step sizes and momentum.

As a platform engineer you care about:

- Training jobs (GPU hours, checkpointing)
- Fine-tuning cost (LoRA reduces trainable params)
- Inference “optimization” = different problem (latency, throughput)

---

## 3. Architecture

```text
  Forward pass  →  loss L
        │
        ▼
  Backward pass →  gradients ∂L/∂θ
        │
        ▼
  Optimizer step →  θ ← θ − η · update(∇)
        │
        └── repeat until budget / convergence
```

**Inference path (no optimizer):**

```text
  prompt → forward only → logits → sample token → repeat
```

---

## 4. Internal Working

### Loss functions (examples)

| Loss | Use |
|------|-----|
| Cross-entropy | Classification, next-token prediction |
| MSE | Regression |
| Contrastive | Embeddings (pull similar, push dissimilar) |

LLM pretraining: minimize **average cross-entropy** over tokens (maximum likelihood).

### Gradient descent variants

- **SGD:** batch gradient noisy; cheap per step.
- **Adam/AdamW:** adaptive per-parameter learning rates; default for many fine-tunes.
- **Learning rate schedule:** warmup + cosine decay common in LLM training.

### Regularization

- **Weight decay (L2):** smaller weights, less overfit.
- **Dropout:** random zero neurons (training); usually off in inference.
- **Early stopping:** stop when val loss worsens.

### Fine-tuning connection

Full fine-tune updates all \(\theta\). **LoRA** updates low-rank adapters \(BA\) added to weights—optimization in a smaller subspace.

---

## 5. Example

Support classifier fine-tune:

- Base: 7B LLM (frozen except LoRA)
- Loss: cross-entropy on intent labels
- Metric: F1 on holdout
- Stop when val F1 flat for 3 epochs

Platform concern: track **GPU-hours per experiment** in metadata registry.

---

## 6. Implementation

Toy training loop (PyTorch-style pseudocode):

```python
# model, train_loader, optimizer = ...
for epoch in range(num_epochs):
    for batch in train_loader:
        optimizer.zero_grad()
        logits = model(batch.input_ids)
        loss = cross_entropy(logits.view(-1, vocab), batch.labels.view(-1))
        loss.backward()
        optimizer.step()
```

Inference-only (what your API wraps):

```python
with torch.inference_mode():
    out = model.generate(input_ids, max_new_tokens=128)
```

---

## 7. Production Considerations

| Training | Inference |
|----------|-----------|
| Needs reproducibility (seed, data version) | Needs SLOs (TTFT, throughput) |
| Checkpoint to object storage | Model load time = cold start |
| Distributed data parallel | Tensor parallel for big models |
| Gradient explosion → NaN | OOM from batch × seq |

**You** often won’t own full pretraining—but you **will** own fine-tune pipelines and serving optimizations (quantization, batching).

---

## 8. Trade-offs

| Approach | When |
|----------|------|
| Prompt engineering | Fast iteration, no GPU train |
| RAG | Knowledge changes often |
| Fine-tune | Style/format/domain stable, data available |
| Full train | Rare outside labs |

Optimizer choice matters less to infra than **batch size, sequence length, and precision**.

---

## 9. Debugging

- Loss NaN: lower LR, check mixed precision, gradient clipping.
- Train great / val bad: overfit—more data, regularization, early stop.
- Fine-tune degraded general capability: **catastrophic forgetting**—mix general data, lower rank, fewer steps.

---

## 10. Interview Questions

### Level 1

1. What is a loss function?
2. What is a gradient?
3. Training vs inference?
4. What is learning rate?
5. What is overfitting?
6. What is backprop (one sentence)?
7. What is SGD?
8. What is epoch vs batch?
9. What is cross-entropy intuitively?
10. Why freeze layers in fine-tuning?

### Level 2

1. Adam vs SGD?
2. What is weight decay?
3. What is gradient clipping?
4. Learning rate warmup—why?
5. What is LoRA optimizing?
6. Mixed precision training?
7. Data parallel vs model parallel?
8. Checkpoint frequency trade-offs?
9. How does batch size affect memory?
10. Validation loss up, train loss down?

### Senior

1. Design fine-tune job on Kubernetes (fault tolerance).
2. Estimate GPU time for 1M examples × 512 tokens.
3. When does QLoRA make sense?
4. Optimizer state in checkpoints—size impact?
5. CI for training pipelines?

### Staff

1. Build vs buy fine-tuning platform.
2. Experiment tracking and reproducibility standards.
3. Cost allocation for research vs product fine-tunes.

### Explain in an interview (30s)

We train neural nets by minimizing a loss with gradient-based optimizers; at serving time we freeze weights and optimize a different objective—latency and throughput—via batching, caching, quantization, and hardware utilization.

---

## 11. Practical Exercise

Plot loss curve from a public tiny training run (or simulate convex + noise). Identify where you’d early-stop and how that choice affects downstream eval.

---

## 12. Mini Project

**Experiment tracker schema (Go + Postgres):** tables for `run`, `hyperparams`, `metrics`, `artifact_uri`; CLI to register a fine-tune job outcome—foundation for your eval platform (Project 03).
