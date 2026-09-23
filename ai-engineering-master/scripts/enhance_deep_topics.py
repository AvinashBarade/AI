#!/usr/bin/env python3
"""Overwrite selected topics with deeper hand-authored content."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DEEP: dict[str, str] = {}

def set_path(rel: str, content: str) -> None:
    DEEP[rel] = content

set_path(
    "02-llm-fundamentals/attention.md",
    r"""# Attention

> Module: `02-llm-fundamentals`

## 1. Mental Model

Each token projects a **query** vector and compares it to **keys** of all tokens (including itself). High dot-product → high weight. Output is a weighted blend of **value** vectors. Stacking layers lets representations become contextual.

## 2. Why This Exists

Fixed-length context needs **dynamic routing** of information. CNNs/RNNs struggled with long-range dependencies; attention learns which positions matter per token.

## 3. Problem It Solves

Without attention, each position has limited receptive field. Attention provides **all-pairs** interaction (within sequence) in one parallelizable op—ideal for GPUs.

## 4. Architecture

```text
  X (embeddings)
    │
    ├─ Linear → Q
    ├─ Linear → K
    └─ Linear → V
         │
         ▼
  Scores = QK^T / sqrt(d_k)
  Weights = softmax(Scores)   [causal mask in decoder]
  Out = Weights @ V
```

## 5. Internal Working

Scaled dot-product attention (Vaswani et al.):

\[
\text{Attention}(Q,K,V)=\text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
\]

**Multi-head:** \(h\) parallel heads with separate \(W^Q_i, W^K_i, W^V_i\); outputs concatenated and projected.

**Causal mask (decoder):** positions may not attend to future tokens—ensures autoregressive factorization.

## 6. Step-by-Step Flow

1. Input hidden states \(X \in \mathbb{R}^{n \times d}\)
2. Project to \(Q,K,V\)
3. Compute scores, apply mask, softmax per row
4. Multiply by \(V\) → contextualized vectors
5. Feed-forward sublayer + residual + LayerNorm

## 7. Example

Prompt: "The capital of France is" — the token "France" should attend strongly to "capital" and weakly to unrelated tokens when predicting "Paris".

## 8. Implementation

```python
import math
import torch
import torch.nn.functional as F

def attention(q, k, v, mask=None):
    d_k = q.size(-1)
    scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(d_k)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float("-inf"))
    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, v)
```

## 9. Production Architecture

You rarely implement attention in app code—it lives inside the model runtime (vLLM, TensorRT-LLM). Your job: **context length**, batching, and KV cache sizing drive memory and latency.

## 10. Failure Modes

- **Lost in the middle:** salient info buried in long prompts gets low weight.
- **Attention sink artifacts** in some models.
- OOM from materializing full \(n \times n\) scores at huge \(n\) (mitigated by FlashAttention).

## 11. Debugging

Compare retrieval+short prompt vs long stuffed prompt; ablate chunks; use attention visualization tools in research settings.

## 12. Scaling

FlashAttention reduces HBM traffic; sparse/sliding windows trade quality for cost; multi-query attention in serving reuses KV.

## 13. Security

Attention does not sanitize content—poisoned long contexts shift weights; enforce ACL at retrieval.

## 14. Observability

Log `prompt_tokens`, `completion_tokens`; cannot easily log per-head weights in prod—use eval sets.

## 15. Cost

Attention cost scales with sequence length; prefill is attention-heavy.

## 16. Trade-offs

| More heads / larger d | Better expressivity | More memory/compute |

## 17. When To Use

Built into transformers—you choose **model family** and **context budget**.

## 18. When NOT To Use

Tasks solvable with embeddings + classifier without generation.

## 19. Interview Questions

### Level 1
1. What are Q, K, V?
2. Why divide by sqrt(d_k)?
3. What is causal masking?

### Senior
1. How does KV cache change attention during decode?
2. FlashAttention value proposition?

### Staff
1. Pick context window for enterprise RAG—attention implications?

## 20. Practical Exercise

Implement masked attention on a 8-token toy sequence; verify future positions receive -inf before softmax.

## 21. Project

Relate attention to TTFT in Project 01/08 serving benchmarks.

---
**Related:** [transformers.md](./transformers.md) · [kv-cache](../12-model-serving/kv-cache.md)
""",
)

set_path(
    "02-llm-fundamentals/transformers.md",
    r"""# Transformers

## 1. Mental Model

A **stack of identical blocks**: each block = multi-head self-attention + position-wise FFN, with residuals and normalization. Decoder-only stacks (GPT) predict next token; encoder-only (BERT) builds representations.

## 2. Why This Exists

Parallelizable training over sequences replaced sequential RNN bottlenecks and unlocked scale.

## 3. Problem It Solves

Language modeling at scale with stable optimization and GPU-friendly matmuls.

## 4. Architecture

```text
Token IDs → Embedding + Positional
    → [Block × L]
         Block = Attention → Add&Norm → FFN → Add&Norm
    → LM head → logits → softmax → sample
```

## 5. Internal Working

**FFN:** typically expands dimension (e.g. 4×) with GELU/SwiGLU, then projects back.

**Residual connections:** ease optimization in deep stacks.

**LayerNorm/RMSNorm:** stabilizes activations.

Parameter count dominated by weight matrices in attention and FFN.

## 6. Step-by-Step Flow

Prefill: process prompt tokens in parallel. Decode: one new token per step, append to sequence, update KV cache.

## 7. Example

GPT-style chat model: system + user tokens prefill; assistant tokens generated autoregressively until stop token or max tokens.

## 8. Implementation

Use Hugging Face `AutoModelForCausalLM` for experiments; production via vLLM/OpenAI API—not custom PyTorch stacks unless you are a model team.

## 9. Production Architecture

Model weights in GPU memory; scheduler batches requests; gateway handles auth and token accounting.

## 10. Failure Modes

Hallucination, context overflow, degraded quality on long outputs, version skew between tokenizer and weights.

## 11. Debugging

Verify tokenizer matches model card; check `max_model_len`; compare logits on golden prompt across versions.

## 12. Scaling

Tensor/pipeline/expert parallelism for huge models; multi-node inference for 70B+.

## 13. Security

Model weights are secrets; supply-chain verify checksums; prevent arbitrary pickle loads.

## 14. Observability

Per-model version label on every trace span.

## 15. Cost

Parameters × precision × replicas = CapEx; tokens/sec = OpEx driver.

## 16–18. Trade-offs / When / When not

Choose decoder LLM for open-ended generation; use smaller encoders for classification/embedding-only workloads.

## 19. Interview Questions

Explain transformer block; difference encoder vs decoder; why residuals.

## 20. Practical Exercise

Load a tiny model; print number of layers, hidden size, heads from config.

## 21. Project

Document model card metadata in Project 08 serving deployment.

---
**Related:** [attention.md](./attention.md)
""",
)

set_path(
    "06-rag/rag-fundamentals.md",
    r"""# RAG Fundamentals

## 1. Mental Model

**Retrieval-Augmented Generation** = open-book exam. The LLM answers using retrieved passages plus its parametric knowledge. RAG is **not** training the LLM on your docs by default—it is **index + retrieve + prompt**.

## 2. Why This Exists

LLMs hallucinate and have stale knowledge. Enterprises need grounded, updatable answers with citations.

## 3. Problem It Solves

Knowledge cutoff, proprietary data, auditability (cite sources), and controlled update cycles without full fine-tunes.

## 4. Architecture

```text
Documents → parse → chunk → embed → vector index
User query → embed → retrieve top-k → (optional rerank)
→ build prompt with chunks → LLM → answer + citations
```

## 5. Internal Working

Retrieval quality ceiling bounds answer quality. Generation can only be faithful to **provided** context (mostly)—faithfulness metrics measure this gap.

## 6. Step-by-Step Flow

Ingestion pipeline (async) separate from online query path (sync, low latency).

## 7. Example

HR policy bot: query "parental leave" retrieves policy section 4.2; answer quotes chunk; user clicks source link.

## 8. Implementation

```python
# Conceptual retrieve
hits = index.query(vector=embed(query), top_k=20, filters={"tenant_id": tid})
context = "\n\n".join(h.text for h in hits[:5])
prompt = f"Use only context.\n{context}\n\nQ: {query}"
```

## 9. Production Architecture

Hybrid search (BM25 + vector), reranker, metadata ACL per chunk, freshness jobs, eval harness in CI.

## 10. Failure Modes

Bad chunking, wrong embedding model, stale index, injection in documents, cross-tenant leakage, empty retrieval → confident hallucination.

## 11. Debugging

Log retrieval IDs/scores; run query in isolation; A/B chunk sizes; human eval slice.

## 12. Scaling

Shard indexes by tenant; async embedding workers; cache frequent queries.

## 13. Security

Treat corpus as untrusted input; sanitize HTML; enforce document ACL at index time.

## 14. Observability

Retrieval precision@k, nDCG, faithfulness, answer relevance, latency breakdown.

## 15. Cost

Embedding $ + storage + LLM tokens (context inflation).

## 16. Trade-offs

| RAG | Fine-tune |
|-----|-----------|
| Fresh docs | Style/format lock-in |
| Cheaper iteration | Needs GPU training pipeline |

## 17–18. When / When not

Use RAG for dynamic knowledge bases. Avoid RAG alone when you need guaranteed tool side-effects—use agents/APIs.

## 19. Interview Questions

Difference prompt vs RAG vs FT vs continued pretrain; how evaluate retrieval vs generation.

## 20. Practical Exercise

Build 50-question set; measure MRR when changing chunk size 256 vs 1024.

## 21. Project

Projects 02–03 in `22-projects/`.

---
See also: [prompting-vs-rag-vs-finetuning](../11-fine-tuning/prompting-vs-rag-vs-finetuning.md)
""",
)

set_path(
    "12-model-serving/kv-cache.md",
    r"""# KV Cache

## 1. Mental Model

During decode, store **keys and values** for prior tokens so each new step only computes Q for the latest token against cached K/V.

## 2. Why This Exists

Recomputing full-sequence attention every token is wasteful—\(O(n^2)\) per step without cache.

## 3. Problem It Solves

Decode throughput and latency for autoregressive models.

## 4. Architecture

Paged KV blocks (vLLM) map logical sequences to non-contiguous GPU blocks to reduce fragmentation.

## 5. Internal Working

Memory scales roughly with:

\[
\text{KV bytes} \approx 2 \times L \times B \times T \times H \times D_{head} \times \text{bytes\_per\_elem}
\]

\(L\)=layers, \(B\)=batch, \(T\)=seq len, \(H\)=heads (or grouped in GQA).

## 6. Step-by-Step Flow

Prefill fills cache for prompt; each decode step appends one position.

## 7. Example

8k context + 512 output on 70B class model can OOM smaller GPUs—why serving picks quantization and max seq limits.

## 8. Implementation

Handled inside vLLM/TGI; tune `max_num_seqs`, `gpu_memory_utilization`.

## 9–15. Production / failures / debug / scale / sec / obs / cost

Monitor GPU memory; alert on eviction; cap `max_model_len` per tier.

## 16–18. Trade-offs

Longer context vs fewer concurrent users on same GPU.

## 19. Interview Questions

Derive KV memory for given config; PagedAttention purpose.

## 20. Exercise

Spreadsheet calculator for KV GB vs batch size.

## 21. Project

Project 08 load test varying context length.

---
""",
)

for rel, body in DEEP.items():
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")

print(f"Enhanced {len(DEEP)} deep topic files.")
