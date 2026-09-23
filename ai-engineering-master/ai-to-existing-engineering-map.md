# AI ↔ Your Existing Engineering Map

Use this when learning or interviewing: **you are not starting over**—you are adding an AI layer to patterns you already run in production.

---

## Career ladder (how skills compound)

```text
Senior Backend / Platform Engineer  ← YOU ARE HERE
              ↓
         AI Engineer               (apps: RAG, agents, eval, APIs)
              ↓
      AI Platform Engineer         (gateway, registry, tenancy, cost)
              ↓
   AI Infrastructure / Inference   (serving, GPU, capacity, SLOs)
              ↓
        Staff AI / Infra             (HLD, economics, org standards)
              ↓
     FDE / AI Solutions              (discovery → deployed value)
```

---

## Skill transfer table

| Your skill | AI engineering role | What you build / own |
|------------|---------------------|----------------------|
| **Go** | AI gateway, routers, admission control, high-QPS glue | Token-aware rate limits, model routing, streaming proxies, workers |
| **Backend / APIs** | LLM application layer | FastAPI/Go services, idempotency, conversation state, tool runtimes |
| **Distributed systems** | Multi-tenant AI, distributed inference | Sharded vector indexes, queue-backed embedding, fan-out/agents |
| **HLD / LLD** | Platform & FDE architecture | RAG pipelines, agent boundaries, data planes vs control planes |
| **Kubernetes** | Model serving & GPU workloads | Device plugins, queues, KServe/Ray, rollouts, HPA/KEDA |
| **Docker** | Model images, reproducible eval | CUDA base images, slim inference images, CI-built artifacts |
| **Terraform** | AI infra as code | GPU node pools, networking, managed OpenAI alternatives, observability stack |
| **Azure / AWS** | Managed + self-hosted mix | OpenAI/Foundry, Bedrock, AKS/EKS GPU pools, private endpoints |
| **CI/CD** | Eval gates, model promotion | Prompt/version CI, offline eval on PR, canary inference |
| **DevSecOps** | AI security & supply chain | Prompt injection controls, secret scoping, SBOM for ML images, agent RBAC |
| **Prometheus / Grafana** | AI observability | TTFT, tokens/sec, GPU, retrieval precision, tool failure rates |
| **Linux** | GPU nodes, serving debug | `nvidia-smi`, cgroup memory, NUMA awareness (conceptual) |
| **SQL / MongoDB** | Metadata, chat history, eval sets | Postgres + pgvector; tenant-scoped document metadata |
| **Cloud-native** | Platform primitives | Gateway + service mesh patterns, external secrets, policy-as-code |

---

## Layer map (where your head should be)

```text
┌─────────────────────────────────────────────────────────────┐
│  APPLICATION (AI Engineer)                                   │
│  RAG · Agents · Prompts · Eval · Product APIs                │
├─────────────────────────────────────────────────────────────┤
│  PLATFORM (AI Platform Engineer)  ← strong fit               │
│  Gateway · Registry · Tenancy · Quotas · Cost · Audit        │
├─────────────────────────────────────────────────────────────┤
│  SERVING / INFERENCE (AI Infra)  ← strong fit               │
│  vLLM/Triton · Batching · KV cache · Quant · Autoscale       │
├─────────────────────────────────────────────────────────────┤
│  CLUSTER / HARDWARE (AI Infra)  ← strong fit               │
│  GPU scheduling · Network · Storage · Capacity planning      │
└─────────────────────────────────────────────────────────────┘
```

You can **shorten** time-to-impact by spending more hours in PLATFORM + SERVING + CLUSTER while still building **one** flagship RAG and **one** agent for interview stories.

---

## Pattern analogies (interview-friendly)

| You know | AI equivalent |
|----------|----------------|
| API gateway + rate limit | AI gateway + **token** budget |
| Circuit breaker | Provider failover / degraded model |
| Cache (Redis) | Semantic cache / prompt cache / prefix cache |
| Feature flags | Prompt version, model route, kill switch |
| Blue/green deploy | Canary inference, shadow traffic |
| Multi-tenant SaaS | Vector + secret + quota isolation |
| SLO / error budget | TTFT P95, faithfulness regression budget |
| STRIDE threat model | Prompt injection, tool abuse, RAG poisoning |
| Job queue + workers | Embedding/indexing pipelines |
| Connection pool | GPU batch scheduler / max concurrent sequences |

---

## Recommended emphasis (for your targets)

| Priority | Modules | Projects |
|----------|---------|----------|
| **P0** | `02-ai-engineering-core`, `08-rag`, `14-inference`, `17-platform`, `18-infra`, `19-obs`, `20-sec` | P04–P05, P09–P11 |
| **P1** | `03-llm`, `09-agents`, `10-mcp`, `16-k8s` | P06–P08, P12–P13 |
| **P2** | `00` math (skim), `04-pytorch`, `13-ml-lifecycle` | P01–P03 |
| **P3** | `11-frameworks` (compare only) | — |

---

## Anti-patterns for your profile

- Re-learning Kubernetes pod basics instead of GPU scheduling.
- Deep Python language trivia without shipping FastAPI + eval scripts.
- Building a chatbot demo without eval, cost, or security.
- Fine-tuning before RAG + eval prove the bottleneck.
- Agents where a **workflow** (Temporal/Go state machine) is safer.

---

## Next document

After this map: [02-ai-engineering-core/README.md](./02-ai-engineering-core/README.md) → `ai-system-mental-model.md` (when authored).
