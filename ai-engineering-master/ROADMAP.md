# AI Engineering Master — Roadmap (24 Phases)

Flexible pacing for **8–20 h/week**. Advance by **competence**, not calendar. Connect every phase to **projects** and **interviews**.

**Allocation (default):** 20% theory · 30% implementation · 30% projects · 10% system design · 10% interview  

**Serving / platform / infra phases:** shift toward 40% projects, 20% design, 20% interview.

---

## Phase 1 — AI foundations

**Modules:** `00-foundations/`  
**Focus:** AI vs ML vs GenAI, mental models, math for engineers (probability, linear algebra, optimization, information theory)—**skim** if platform-focused.  
**Exit:** Explain embeddings, loss, training vs inference; draw token → answer diagram.

---

## Phase 2 — Python for AI engineering

**Modules:** `01-python-for-ai-engineering/`  
**Focus:** Go→Python bridge, typing, async, Pydantic, FastAPI patterns, NumPy/Pandas basics, uv/packaging, pytest.  
**Exit:** Small FastAPI service + one eval script.

---

## Phase 3 — LLM fundamentals

**Modules:** `02-llm-fundamentals/`  
**Focus:** Tokens, transformers, attention, positional encoding, pretraining, instruction tuning, alignment, inference, context, sampling, structured output, function calling, model selection.  
**Exit:** Attention + causal mask explained; pick model for latency/cost trade-off.

---

## Phase 4 — LLM APIs and prompting

**Modules:** `03-llm-apis/`, `04-prompt-engineering/`  
**Focus:** Providers, streaming, retries, rate limits, token accounting; prompts, versioning, injection defenses; safe reasoning concepts (no hidden CoT).  
**Project:** **01-llm-chat-api**  
**Exit:** Production-grade API client wrapper with observability.

---

## Phase 5 — Embeddings and vector search

**Modules:** `05-embeddings-and-vector-search/`  
**Focus:** Models, cosine similarity, ANN, HNSW, IVF, pgvector, Qdrant, Milvus comparison.  
**Exit:** Benchmark two embedding models on your corpus.

---

## Phase 6 — RAG

**Modules:** `06-rag/`  
**Focus:** Full pipeline ingestion → production; hybrid, rerank, graph/multimodal; eval and failure modes; **RAG ≠ training**.  
**Projects:** **02-rag-system**, **03-production-rag**  
**Exit:** Citations + faithfulness metrics + ACL design.

---

## Phase 7 — Agents

**Modules:** `07-agents/`  
**Focus:** Loops, tools, planning, memory, state machines, multi-agent, HITL, security; **workflow vs agent**.  
**Project:** **04-ai-agent**  
**Exit:** Bounded agent with audit log and HITL for destructive tools.

---

## Phase 8 — MCP

**Modules:** `08-mcp/`  
**Focus:** Architecture, transport, security; build servers (Git, K8s, Postgres, Prometheus).  
**Project:** **05-mcp-platform**  
**Exit:** Client uses MCP tools with authZ.

---

## Phase 9 — AI frameworks

**Modules:** `09-ai-frameworks/`  
**Focus:** LangChain, LangGraph, LlamaIndex, DSPy—strengths, weaknesses, when to avoid.  
**Exit:** Same feature implemented raw vs one framework; written trade-off doc.

---

## Phase 10 — Evaluation

**Modules:** `10-evaluation/`  
**Focus:** LLM/RAG/agent eval, offline/online, hallucination, faithfulness, CI pipelines.  
**Exit:** Eval gate on PR for one project.

---

## Phase 11 — Fine-tuning

**Modules:** `11-fine-tuning/`  
**Focus:** Prompt vs RAG vs SFT; LoRA/QLoRA; datasets; small GPU experiment.  
**Exit:** Decision matrix for a real use case.

---

## Phase 12 — Model serving

**Modules:** `12-model-serving/`  
**Focus:** Prefill/decode, batching, KV cache, quantization, speculative decoding, vLLM, Triton, KServe, gateway.  
**Project:** **08-model-serving**  
**Exit:** Capacity math for one model; load test results table.

---

## Phase 13 — GPU infrastructure

**Modules:** `13-gpu-and-accelerator-infrastructure/`  
**Focus:** Architecture, VRAM, CUDA concepts, tensor cores, parallelism, distributed inference.  
**Exit:** Compute vs memory-bound diagnosis for a workload.

---

## Phase 14 — Kubernetes for AI

**Modules:** `14-kubernetes-for-ai/`  
**Focus:** GPU scheduling, device plugin, node pools, KEDA, KServe, Ray—**no K8s basics**.  
**Project:** **06-kubernetes-agent**  
**Exit:** GPU workload YAML + autoscaling story.

---

## Phase 15 — AI platform engineering

**Modules:** `15-ai-platform-engineering/`  
**Focus:** Gateway, registry, prompt registry, tenancy, quotas, cost, platform API.  
**Project:** **07-ai-gateway** (Go)  
**Exit:** Multi-model routing + per-tenant token accounting.

---

## Phase 16 — AI infrastructure

**Modules:** `16-ai-infrastructure/`  
**Focus:** Inference clusters, networking, storage, caching, DR, **capacity planning exercises**.  
**Exit:** Worked example (e.g. 10M req/day, 2K tokens, peak RPS).

---

## Phase 17 — Observability

**Modules:** `17-observability/`  
**Focus:** Infra + LLM + RAG + agent metrics; Prometheus, Grafana, OTel.  
**Project:** **09-ai-observability**  
**Exit:** Dashboards for TTFT, tokens/sec, retrieval quality.

---

## Phase 18 — Security

**Modules:** `18-ai-security/`  
**Focus:** Threat models, injection, RAG poisoning, tools, supply chain, PII—DevSecOps aligned.  
**Exit:** STRIDE-style doc for one system.

---

## Phase 19 — Production AI

**Modules:** `19-production-ai/`  
**Focus:** Reliability, fallbacks, circuit breakers, multi-model strategy, incident patterns.  
**Exit:** Runbook for provider outage.

---

## Phase 20 — FDE engineering

**Modules:** `20-fde-engineering/`  
**Focus:** Discovery → deployment → optimization; enterprise scenarios.  
**Exit:** One full written case (architecture + cost + rollout).

---

## Phase 21 — System design

**Modules:** `21-system-design/`  
**Focus:** Chat, ChatGPT-scale, RAG platform, agent platform, gateway, serving, observability, multi-tenant, enterprise.  
**Exit:** 3 timed designs with capacity + cost sections.

---

## Phase 22 — Projects

**Modules:** `22-projects/` (integrate all prior phases)  
**Projects:** **10-multi-tenant-ai-platform**, **11-capstone-ai-platform**  
**Exit:** Capstone meets README acceptance criteria.

---

## Phase 23 — Interview preparation

**Modules:** `23-interview-preparation/`, `INTERVIEW_MASTER.md`  
**Focus:** Drills by role; Go coding; behavioral + FDE scenarios.  
**Exit:** Mock loop with recorded system design.

---

## Phase 24 — Research

**Modules:** `24-research/`  
**Focus:** Emerging models, agents, inference, infra trends; papers for engineers.  
**Exit:** Monthly one-page “what changed / should I learn now?”

---

## Parallel tracks (your profile)

| Strength | Double down in |
|----------|----------------|
| Go / distributed systems | Phases 15–16, Project 07 |
| Kubernetes / Terraform | Phases 14, 16, capstone |
| Prometheus / Grafana | Phase 17 |
| DevSecOps | Phase 18 on every project |

---

**Next step:** [PROGRESS.md](./PROGRESS.md) → Phase 1 checklist.
