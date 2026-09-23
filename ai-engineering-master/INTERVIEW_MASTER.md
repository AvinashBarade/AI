# Interview Master Guide

Cross-cutting preparation for AI Engineer → Staff / Platform / Infra / FDE loops. Pair this with per-module **Interview Questions** sections.

---

## Interview Archetypes

| Loop | What they probe | Your angle (backend → AI) |
|------|-----------------|---------------------------|
| AI application | RAG, agents, prompts, eval | “I ship measurable quality, not demos” |
| AI platform | Gateway, tenancy, routing, cost | “I’ve run K8s + SRE; gateway is a control plane” |
| AI infrastructure | Serving, GPU, scaling, reliability | “Prefill/decode, KV cache, queueing theory” |
| System design | End-to-end architecture | Same HLD skills + data + model constraints |
| FDE | Vague ask → production design | Discovery, risk, phased delivery |
| Coding | Go/Python, concurrency, streaming | Rate limiters, caches, parsers |

---

## Answer Frameworks

### 30–60s “Explain X”

```text
1. One-sentence definition (plain English)
2. Problem it solves (why not the naive approach?)
3. One production detail (failure, cost, or metric)
4. Optional: trade-off vs alternative
```

### System design (45 min)

```text
Requirements → scale estimates → API sketch → data model
→ diagram → deep dive 2 components → failure modes → observability → cost
```

### Debugging narrative (STAR for incidents)

```text
Symptom → hypothesis → signal (metric/trace/log) → root cause
→ fix → prevention (test, guardrail, runbook)
```

---

## Staff-Level Themes (repeat until automatic)

1. **Quality is a pipeline** — data, retrieval, generation, eval, monitoring.
2. **Cost is architecture** — model choice, caching, batching, routing, context size.
3. **Security is default-deny** — tools, prompts, RAG sources, tenant boundaries.
4. **Latency is two-phase** — prefill vs decode; don’t optimize the wrong one.
5. **Fallbacks are product** — degraded model, cached answer, human handoff.

---

## “Explain This in an Interview” — Quick Scripts

### RAG (30s)

RAG grounds the LLM by retrieving relevant document chunks, embedding the user query, searching a vector index, and stuffing the top results into the prompt before generation. It reduces hallucination on factual questions but introduces failure modes: bad chunks, stale data, and injection via documents. Production RAG adds hybrid search, reranking, citations, and offline/online eval.

**Deep dive:** See `08-rag/rag-fundamentals.md` (when written) and module checkpoints.

### AI Gateway (30s)

An AI gateway sits between clients and model providers like an API management layer plus policy engine: authentication, per-tenant rate limits and quotas, model routing by cost/latency/policy, retries with idempotency keys, circuit breakers when a provider degrades, token-based cost accounting, and OpenTelemetry traces with prompt/response metadata (redacted). It’s how platform teams centralize governance without every app reimplementing limits and observability.

### KV cache (30s)

During autoregressive decode, recomputing attention over the full prefix every step would be quadratic waste. The KV cache stores key and value projections for past tokens so each new token only attends with incremental work. Memory grows with batch size × sequence length × layers × head dimension—this is why long contexts and large batches cause GPU OOM and why serving systems use paging (e.g. PagedAttention).

### Agent vs workflow (30s)

A workflow is deterministic orchestration (DAG, state machine). An agent lets the LLM choose tools and steps within guardrails. Agents flex for ambiguous tasks but risk loops, cost blowups, and tool abuse. Production agents use max steps, budgets, allowlisted tools, structured logs, and human approval for destructive actions.

---

## Question Banks by Level (samples)

Full per-topic banks live in modules. Drill these weekly.

### Level 1 — Foundations (10)

1. Difference between AI, ML, DL, and GenAI?
2. What is a token?
3. What is an embedding?
4. Supervised vs unsupervised learning—in one example each?
5. What is overfitting?
6. Precision vs recall?
7. What is gradient descent intuitively?
8. What is a loss function?
9. Why GPUs for deep learning?
10. What is inference vs training?

### Level 2 — Applied LLM (10)

1. How does temperature affect output?
2. What is the context window limit?
3. Why system prompts?
4. What is few-shot prompting?
5. How do embeddings power semantic search?
6. What is top-p sampling?
7. What is structured output?
8. What is function calling?
9. Why might a smaller model be better in production?
10. What metrics matter for a chat API?

### Senior (10)

1. Design rate limiting for LLM APIs (tokens vs requests).
2. How would you debug rising P95 latency on an LLM service?
3. Compare RAG vs fine-tuning for a support bot.
4. How do you evaluate hallucination rate?
5. Describe a safe tool-calling architecture.
6. How does hybrid search help RAG?
7. What is continuous batching?
8. How do you version prompts in production?
9. Multi-tenant vector isolation strategies?
10. Provider outage: what does the client see?

### Staff (10)

1. Cut platform LLM spend 50%—concrete levers?
2. Design model routing with compliance constraints (data residency).
3. Capacity plan GPUs for 10k concurrent chat users.
4. DR for RAG + fine-tuned models.
5. Org-wide eval registry and release gates.
6. When to build vs buy embedding/search?
7. SLOs for TTFT and tokens/sec—how to set them?
8. Threat model for enterprise agent with SQL tool.
9. Migration from single provider to multi-provider without downtime.
10. Platform team roadmap for year one—what ships first?

### FDE scenarios (10)

1. Bank wants RAG over 10M docs—first 90 days?
2. Customer says “we need 100% accuracy”—your response?
3. On-prem only, no cloud APIs—options?
4. Latency must be &lt;500ms end-to-end—architecture?
5. Legal needs citation to paragraph—design?
6. SSO + per-document ACLs in RAG?
7. Pilot succeeded; production rollout plan?
8. Debug: answers correct in dev, wrong in prod.
9. Stakeholder wants agents on day one—push back how?
10. Write a one-page architecture for executives.

---

## Coding Interview Focus (Go-primary)

| Pattern | AI engineering use |
|---------|-------------------|
| Rate limiter (token bucket) | Gateway, provider limits |
| LRU cache | Prompt/embedding cache |
| Worker pool | Batch embedding jobs |
| Heap | Top-k retrieval locally |
| Trie / string | Tokenization exercises |
| Graph BFS/DFS | Agent plan validation |
| Streaming parser | SSE/chunk handling |
| Concurrent map + lock | In-flight request registry |

Python drills: FastAPI streaming endpoint, Pydantic schema validation, async gather with semaphores.

---

## Mock Loop Schedule (12 weeks before interviews)

| Week | Activity |
|------|----------|
| 1–2 | 2× system design (RAG platform, gateway) |
| 3–4 | 2× debugging narratives (RAG + inference) |
| 5–6 | Coding 4× (Go) + 2× Python API |
| 7–8 | Staff trade-off deep dives (cost, security) |
| 9–10 | FDE role-plays (record yourself) |
| 11–12 | Full loops (design + coding + behavioral) |

---

## Behavioral (AI-specific angles)

Prepare stories for:

- Shipping something with **eval metrics** and regression gates
- A **production incident** (latency, cost spike, bad deploy)
- Saying **no** or narrowing scope with data
- **Cross-team** work (security, legal, data engineering)
- **Customer** or stakeholder communication

---

## Red Flags in Your Own Answers

- No mention of eval, security, or cost
- “We’d use RAG” without retrieval metrics
- “We’d fine-tune” without data volume and maintenance plan
- Ignoring tenant isolation on multi-tenant designs
- Treating GPU as “just bigger CPU”

---

## Module Cross-Reference

| Topic | Primary interview file |
|-------|-------------------------|
| Fundamentals | `23-interview-preparation/ai-fundamentals.md` (planned) |
| LLM | `23-interview-preparation/llm.md` |
| RAG / agents / MCP | respective files under `23-interview-preparation/` |
| This week | `00-foundations/*` interview sections |

Update `PROGRESS.md` interview column when you complete a question bank for a module.
