# Mental Models for the AI Stack

These are **pictures to think with** when you read a diagram or debug a bad answer. You don’t need to memorize vendors—slot unknown boxes into one of these patterns.

---

## Token

**Picture:** Text shredded into LEGO IDs from a catalog (~32k–200k pieces). The model never sees “hello” as letters—only ID `15496`. Your bill and context limit count **pieces**, not words.

**When it bites you:** English prose vs JSON vs code changes token count 2×; legal clauses split into many subwords; you truncate the wrong end of the prompt.

---

## Embedding

**Picture:** A GPS coordinate in 768–4096 dimensions. “Refund policy” and “return item” sit close; “weather” is far away. You can’t read the numbers as English—they’re for **similarity math**.

**When it bites you:** Wrong embedding model for the domain; forgot to normalize; changed model without reindexing.

---

## Attention

**Picture:** Each token holds a flashlight over the sequence, deciding who to listen to. Stack many layers and you get deep context—but attention budget is finite and expensive at long distance.

**When it bites you:** “Lost in the middle” on stuffed prompts; debugging by staring at weights (you won’t in prod—ablate context instead).

---

## Transformer

**Picture:** A conveyor of identical blocks: **mix tokens (attention)** → **per-token MLP** → repeat. Decoder-only stacks predict the next token; that’s ChatGPT-class behavior.

---

## Context window

**Picture:** A whiteboard with fixed area. System prompt, RAG chunks, history, tool output—all compete for the same space. Overflow = truncate, summarize, or fail.

---

## Inference (prefill + decode)

**Picture:** A two-phase factory:

1. **Prefill** — read the whole prompt in parallel (compute-heavy).
2. **Decode** — stamp one token at a time using KV cache (memory-bandwidth-heavy).

Latency complaints are often “we optimized the wrong phase.”

---

## RAG

**Picture:** Open-book exam. A **librarian** (retriever) picks pages; the **student** (LLM) writes the answer. If the librarian brings the wrong chapter, the student can still sound confident.

RAG is usually **not** training the model on your docs—it’s **index + search + prompt stuffing**.

---

## Vector search

**Picture:** Nearest neighbors in a huge map. Indexes (HNSW, IVF) are tricks to avoid scanning every point—trade recall for speed.

---

## Reranking

**Picture:** Net fishing → chef inspects the catch. Cheap retrieval gets 50 candidates; expensive cross-encoder or LLM scores the top 10 properly.

---

## Agent

**Picture:** An intern with a phone (tools) and a manager (your code). The intern improvises; the manager sets **max calls, budget, and approval for dangerous actions**.

---

## Tool

**Picture:** A typed RPC the model may invoke. Your runtime validates JSON, checks authz, executes, returns a string. Over-privileged tools = remote code execution via prompt.

---

## MCP

**Picture:** USB-C for AI tools—one plug shape so clients discover servers (Git, K8s, DB) without custom glue per IDE.

Not a security boundary by itself—still need network policy and secrets hygiene.

---

## Model serving

**Picture:** A kitchen built for one heavy dish. Queue out front, batch on the grill (GPU), plates stream out (tokens). Cold start = loading tens of GB of weights.

---

## GPU / VRAM

**Picture:** Thousands of tiny workers great at matmul; **VRAM** is a small shelf. Model + KV cache + batch must fit or the job dies with OOM.

---

## KV cache

**Picture:** Sticky notes per layer for past tokens’ keys/values so decode doesn’t reread the whole book. Notes grow with **batch × sequence length**.

---

## AI gateway

**Picture:** Air traffic control—auth, quotas, route to runway (model/provider), divert on storms (circuit breaker), log fuel (tokens/$).

---

## AI platform

**Picture:** Internal cloud for models, prompts, evals, tenancy—so product teams don’t each hold raw provider keys and reimplement limits.

---

## AI observability

**Picture:** Flight recorder for stochastic APIs: TTFT, tokens/sec, retrieval scores, tool failures—not just CPU graphs.

---

## One diagram to rule them all

```text
User → Gateway → App (RAG/Agent) → Retrieval/Tools → Model API or vLLM
         │              │                                    │
         └──────────────┴──────── Prometheus / OTel / eval ───┘
```

When something fails, ask: **which box**—data, retrieval, policy, model, or infra?

---

Use this page before deep dives in `02-llm-fundamentals` and `06-rag`.
