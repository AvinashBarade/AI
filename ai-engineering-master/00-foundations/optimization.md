# Optimization (Training vs What You Optimize in Prod)

“Optimization” means two different jobs in AI systems—don’t mix them in incident reviews.

## Training-time optimization

**Goal:** find weights \(\theta\) that minimize loss on data (e.g. cross-entropy on next token).

Mechanics you should recognize:

- **Forward pass** → loss
- **Backward pass** → gradients \(\nabla_\theta L\)
- **Optimizer step** (Adam, AdamW, SGD) updates \(\theta\)

Regularization: weight decay, dropout (training only), early stopping when validation metric stalls.

**Fine-tuning** is the same loop on smaller data—often **LoRA** updates a low-rank adapter instead of full weights:

\[
W' = W + BA
\]

Platform angle: track **GPU-hours**, checkpoint to object storage, pin dataset hash, reproduce seeds.

## Inference-time “optimization”

Weights are **frozen**. You optimize:

- latency (TTFT, tokens/sec)
- throughput (concurrent users per GPU)
- cost ($/successful task)
- memory (quantization, KV cache paging)

This is your Kubernetes + vLLM + gateway world—not learning rate schedules.

## Loss functions you’ll hear about

| Loss | Typical use |
|------|-------------|
| Cross-entropy | Classification, LM training |
| MSE | Regression |
| Contrastive | Embedding models (pull similar, push dissimilar) |

Perplexity is \(\exp(\text{cross-entropy})\)—“how surprised” the model is per token. Useful in research; product quality still needs task eval.

## Failure modes (training)

- **NaN loss:** learning rate too high, bad mixed precision, explode gradients → clip grads, lower LR.
- **Train great / val bad:** overfit—more data, regularization, stop earlier.
- **Fine-tune broke general skills:** catastrophic forgetting—mix general data, fewer steps, smaller rank.

## Failure modes (inference)

- OOM: batch × seq too large for KV cache.
- Slow: optimizing decode when prefill dominates (short outputs, huge prompts).

## Decision table

| Need | Tool |
|------|------|
| Change facts weekly | RAG + index |
| Change tone/format | Prompt → LoRA |
| New language domain at scale | Serious ML program (maybe CPT) |
| Cheaper/faster answers | Smaller model, quant, cache, route |

## Try this

Sketch a loss curve (even fictional). Mark where you’d **early stop** and what **business metric** you’d monitor instead of loss alone.
