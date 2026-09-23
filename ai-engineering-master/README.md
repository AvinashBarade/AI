# AI Engineering Master Study Repository

A **production-oriented** curriculum for experienced software engineers transitioning into AI Engineering, AI Platform Engineering, AI Infrastructure, and Forward Deployed / Staff roles.

You are not learning to code—you are learning to **design, build, deploy, secure, observe, scale, and optimize AI systems** in production.

---

## Who This Is For

| You already have | This curriculum adds |
|------------------|----------------------|
| 6–7+ years backend / platform / DevSecOps | LLMs, RAG, agents, evaluation, model serving |
| Go, K8s, Terraform, Azure/AWS, observability | GPU inference, AI gateways, multi-tenant AI platforms |
| Distributed systems & system design | AI-specific failure modes, cost, security, FDE delivery |

**Prerequisite bar:** Strong in APIs, concurrency, Kubernetes, SQL, CI/CD, and system design. **Not** aimed at first-time programmers.

---

## North Star Question

> Given a business problem, how would you design, build, deploy, secure, observe, scale, and optimize an AI solution in production?

Every module is written to strengthen that capability—not to collect certificates.

---

## Career progression (v2)

```text
Senior Backend / Platform Engineer
              ↓
         AI Engineer
              ↓
     AI Platform Engineer
              ↓
 AI Infrastructure / Inference
              ↓
 Staff AI / AI Infrastructure
              ↓
      FDE / AI Solutions
```

Map your existing skills: [ai-to-existing-engineering-map.md](./ai-to-existing-engineering-map.md)  
Curriculum review & changelog: [CURRICULUM_REVIEW.md](./CURRICULUM_REVIEW.md)

---

## How to Use This Repo

```text
1. Read ROADMAP.md (v2)     → phases by exit criteria, not fixed weeks
2. Track PROGRESS.md        → theory / impl / projects / design / interview
3. Study path               → 00 (skim) → 01 (short) → 02-ai-engineering-core → 03-llm …
4. Build in 22-projects/    → 13 projects + PROJECT_STANDARDS.md
5. INTERVIEW_MASTER.md      → cross-cutting drills
6. GLOSSARY.md              → design-review vocabulary
```

### Capability Levels (target: Level 6)

| Level | Meaning |
|-------|---------|
| 1 — Understand | Explain the concept clearly |
| 2 — Implement | Build a working version |
| 3 — Debug | Troubleshoot real failures |
| 4 — Design | Production architecture & APIs |
| 5 — Optimize | Latency, cost, reliability |
| 6 — Lead | Trade-offs, roadmap, org alignment |

---

## Repository Map

```text
ai-engineering-master/
├── README.md                 ← you are here
├── ROADMAP.md                ← 12–24 month plan
├── PROGRESS.md               ← checklist
├── GLOSSARY.md               ← terms
├── INTERVIEW_MASTER.md       ← cross-cutting interview prep
├── BUILD_LOG.md              ← project journal template
│
├── 00-foundations … 26-research/     ← theory (see STRUCTURE.md v2 IDs)
├── 02-ai-engineering-core/           ← stack map (before LLM depth)
├── 22-projects/                      ← 13 production-grade projects
└── 25-interview-preparation/         ← planned (see STRUCTURE.md)
```

**Technology bias (when we build):**

| Layer | Stack |
|-------|--------|
| Platform / gateway | **Go** |
| AI apps / eval / training glue | **Python** (FastAPI, async, Pydantic) |
| Data | PostgreSQL, Redis, pgvector, Qdrant |
| Serving | vLLM, KServe, Triton |
| Infra | Docker, Kubernetes, Helm, Terraform, GitHub Actions |
| Observability | Prometheus, Grafana, OpenTelemetry |
| Cloud | Azure-first, AWS where relevant |

Frameworks (LangGraph, LlamaIndex, DSPy) are taught **after** you can implement the core ideas without them.

---

## Learning Loop (every topic)

```text
Concept → Mental model → Internals → Experiment → Failure modes
    → Production → Security & cost → Interview → Project hook
```

Each major document follows a consistent section pattern (see any file in `00-foundations/`).

---

## Projects (portfolio spine — 13 steps)

See [22-projects/README.md](./22-projects/README.md) and [PROJECT_STANDARDS.md](./22-projects/PROJECT_STANDARDS.md).

Highlights: LLM API → streaming → RAG → **RAG eval platform** → production RAG → agent → **5-server MCP** → K8s agent → **Go AI gateway** → model serving → observability → multi-tenant → **enterprise capstone**.

---

## Curriculum Status (v2 architecture)

| Area | Status |
|------|--------|
| v2 review, roadmap, structure | **Done** — [CURRICULUM_REVIEW.md](./CURRICULUM_REVIEW.md) |
| `00-foundations` | Content written; use **skim path** if platform-focused |
| `01-python` | Short bridge scoped; only `python-for-go-engineers.md` drafted |
| `02-ai-engineering-core` | Index only — **next authored module after approval** |
| Remaining modules | Per [STRUCTURE.md](./STRUCTURE.md); depth over breadth |

**Hold:** No new lesson files until you approve v2 sequencing.

---

## Study rhythm (v2 allocation)

| Bucket | Share | Examples |
|--------|-------|----------|
| Theory | 20% | Core + LLM/RAG reading |
| Implementation | 30% | Exercises, gateway slices |
| Projects | 30% | `22-projects` ladder |
| System design | 10% | `23-system-design` |
| Interview | 10% | `INTERVIEW_MASTER` |

**Inference/platform modules:** shift toward 40% projects, 20% design, 20% interview (see ROADMAP).

---

## Final Capability Checklist

Use `PROGRESS.md` for the full checklist. At graduation you should confidently own:

- LLM inference, RAG, agents, MCP, evaluation
- Model serving, GPU/K8s scheduling, distributed inference
- AI gateway, tenancy, cost, observability, security
- FDE-style discovery → deployed solution → production debug

---

## License & Notes

Personal study repository. Keep secrets out of git; use `.env` and cloud secret managers for API keys in projects.

**Start here:** [ai-to-existing-engineering-map.md](./ai-to-existing-engineering-map.md) → [ROADMAP.md](./ROADMAP.md) Phase 1 → [00-foundations/README.md](./00-foundations/README.md)
