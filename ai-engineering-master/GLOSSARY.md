# Glossary

Precise definitions for design docs, interviews, and incident reviews. When two terms overlap, the **engineering usage** is noted.

---

## A

**Agent** — A control loop where an LLM plans actions, invokes **tools**, observes results, and repeats until a stop condition. Production agents add budgets, authz, logging, and human approval.

**Alignment** — Training and process steps (SFT, RLHF, constitutional rules) that shape model behavior toward human intent and policy constraints.

**Attention** — Mechanism that lets each token weigh other tokens when building representations; core of Transformers. **Self-attention** uses the same sequence as keys/values/queries.

**Autoregressive** — Model generates one token at a time, each conditioned on prior tokens. GPT-style decoders are autoregressive.

---

## B

**Batch inference** — Processing many requests together for throughput; distinct from **continuous batching** in serving systems.

**BLEU / ROUGE** — N-gram overlap metrics; weak alone for LLM quality but still used in some legacy NLP pipelines.

---

## C

**Chain-of-thought (CoT)** — Prompting or training that elicits intermediate reasoning steps before the final answer; improves some tasks at higher token cost.

**Checkpoint** — Saved model weights (and optimizer state) at a training step; used for resume, fine-tunes, and deployment artifacts.

**Chunking** — Splitting documents into segments for embedding/retrieval; trade-off between context granularity and noise.

**Context window** — Maximum tokens the model can attend to in one forward pass (prompt + completion).

**Cosine similarity** — \(\cos(\theta) = \frac{a \cdot b}{\|a\|\|b\|}\); common metric for embedding vectors when magnitude is less important than direction.

**Continuous batching** — Serving technique that adds/removes sequences from a GPU batch between decode steps (e.g. vLLM).

---

## D

**Decoder-only** — Transformer stack that predicts next token (GPT family). Contrasts with encoder-only (BERT) and encoder-decoder (T5).

**Distillation** — Training a smaller **student** model to mimic a larger **teacher**; used for cost/latency reduction.

---

## E

**Embedding** — Dense vector representation of text (or other modality) in \(\mathbb{R}^d\); similar meaning → nearby vectors (approximately).

**Encoder** — Transformer stack that builds contextual representations (BERT); often used for classification or as retriever backbone.

**Eval harness** — Automated pipeline: dataset → run system → metrics → regression gates in CI.

---

## F

**Faithfulness** — Generated answer is supported by retrieved (or cited) evidence; central RAG metric.

**Few-shot** — Including exemplar input/output pairs in the prompt to steer behavior without weight updates.

**Fine-tuning (SFT)** — Supervised update of model weights on labeled examples; distinct from prompt engineering and RAG.

**FlashAttention** — IO-aware exact attention algorithm reducing memory traffic on GPUs.

**Function calling / tool calling** — Structured API for the model to emit tool invocations (name + JSON args) parsed by the runtime.

---

## G

**Grounding** — Tying model outputs to external sources (retrieval, tools, DB) to reduce hallucination.

**GPU OOM** — Out-of-memory on device; common when batch size, sequence length, or model size exceeds VRAM.

---

## H

**Hallucination** — Confident but incorrect or unsupported content; mitigated via RAG, constraints, eval, and smaller claims.

**Hybrid search** — Combining dense (vector) and sparse (BM25/keyword) retrieval.

**HITL (human-in-the-loop)** — Approval or correction step before irreversible or high-risk actions.

---

## I

**Inference** — Forward pass(es) to produce outputs from fixed weights; contrast with **training**.

**Instruction tuning** — SFT on instruction-following datasets (Alpaca, ShareGPT-style) for chat behavior.

**IVF / HNSW** — Vector index families: inverted file with clustering vs graph-based approximate nearest neighbor.

---

## K

**KV cache** — Stored key/value tensors from prior decode steps so each new token does not recompute full history.

---

## L

**Latency (TTFT / TPOT)** — **Time to first token** (prefill-dominated) vs **time per output token** (decode-dominated).

**LoRA / QLoRA** — Low-rank adaptation of weight updates; QLoRA quantizes base weights for memory efficiency.

**LLM** — Large language model; scale + pretraining + (often) instruction tuning; deployed via API or self-hosted.

---

## M

**MCP (Model Context Protocol)** — Standard for exposing tools, resources, and prompts to AI clients over defined transports.

**Metadata filtering** — Restricting vector search by structured fields (tenant, doc type, ACL).

**Mixture of Experts (MoE)** — Subnetworks activated sparsely per token; more parameters, not always more FLOPs per token.

**Model router** — Policy layer choosing model/provider based on task, cost, latency, or compliance.

---

## P

**Prefill** — Processing the prompt in parallel (often compute-bound); fills KV cache before decode.

**Decode** — Autoregressive token generation steps (often memory-bandwidth-bound with large KV).

**Prompt injection** — Untrusted content manipulates model instructions or tool use.

**Pydantic** — Python validation layer; standard for API schemas and structured LLM outputs.

---

## Q

**Quantization** — Lower precision weights/activations (INT8, INT4, FP8) for speed and memory; quality trade-off.

**Query rewriting** — LLM or rules transform user query before retrieval (HyDE, step-back, etc.).

---

## R

**RAG** — Retrieval-augmented generation: retrieve relevant chunks → inject into prompt → generate answer.

**Reranking** — Second-stage scorer (often cross-encoder or LLM) on top-k retrieved chunks.

**RLHF** — Reinforcement learning from human feedback; aligns model with preferences using a reward model.

---

## S

**Semantic search** — Search by embedding similarity rather than exact keyword match.

**Speculative decoding** — Small draft model proposes tokens; large model verifies in parallel for speedup.

**Structured output** — JSON/schema-constrained generations (grammar, tool schema, constrained decoding).

**Streaming** — Emitting tokens (or chunks) as generated; requires HTTP/SSE or WebSocket handling.

---

## T

**Temperature** — Scales logits before softmax; higher → more random completions.

**Tensor parallelism** — Sharding weight matrices across GPUs for one forward pass.

**Token** — Atomic subword unit from a **tokenizer**; billing and context limits are token-based.

**Top-k / top-p (nucleus)** — Sampling filters restricting mass of probability distribution.

**Transformer** — Architecture using attention + FFN blocks; backbone of modern LLMs.

**TTFT** — See latency.

---

## V

**Vector database** — Storage + ANN index for embeddings (pgvector, Qdrant, Milvus, etc.).

**vLLM** — High-throughput LLM serving with PagedAttention and continuous batching.

---

## Platform & ops (your wheelhouse + AI)

**AI gateway** — Policy enforcement point: auth, rate limits, routing, caching, cost accounting, observability.

**Tenant isolation** — Separate data, keys, indexes, and quotas per customer; failure to isolate is a security incident.

**Token accounting** — Per-request input/output token counts for billing and capacity planning.

---

## Acronyms

| Acronym | Expansion |
|---------|-----------|
| ANN | Approximate nearest neighbor |
| API | Application programming interface |
| FDE | Forward deployed engineer |
| FFN | Feed-forward network (Transformer block) |
| HNSW | Hierarchical navigable small world |
| KServe | Kubernetes model serving standard |
| MRR | Mean reciprocal rank (retrieval) |
| OTel | OpenTelemetry |
| PII | Personally identifiable information |
| RAG | Retrieval-augmented generation |
| RLHF | Reinforcement learning from human feedback |
| SFT | Supervised fine-tuning |
| SLO | Service level objective |
| SSE | Server-sent events |
| STRIDE | Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation |

---

_Add terms as you encounter them in modules; link back to the defining doc when possible._
