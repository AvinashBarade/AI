# AI Engineering Master Study Repository

A **production-first** curriculum for experienced software engineers (6–7+ years) transitioning into **AI Engineering**, **AI Platform / Infrastructure**, **ML Platform**, and **Staff / FDE** roles at strong AI companies.

You already know Go, Kubernetes, Terraform, distributed systems, and observability. This repository **does not** teach programming from zero—it connects AI to that foundation.

---

## Purpose

Build the ability to take ambiguous business problems (e.g. *“enterprise assistant over millions of documents”*) and reason through:

```text
Requirements → Architecture → Data → Models → RAG → Agents
    → Inference → Infrastructure → Kubernetes → Security
    → Observability → Cost → Scaling → Production
```

**North star:** *Understand, build, deploy, evaluate, secure, observe, scale, and optimize modern AI systems.*

---

## Target roles

### Primary

- AI Engineer · AI Platform Engineer · AI Infrastructure Engineer  
- ML / AI Platform Engineer · Generative AI Engineer · AI/ML Infrastructure Engineer  

### Secondary

- Forward Deployed Engineer · AI Solutions Engineer · AI Platform Architect  
- Staff AI Engineer · Staff AI Infrastructure Engineer · Staff Platform Engineer  

---

## AI stack (mental map)

```text
                    AI APPLICATIONS
                           │
              ┌────────────┼────────────┐
              ↓            ↓            ↓
             RAG         AGENTS       TOOLS / MCP
              │            │            │
              └────────────┼────────────┘
                           ↓
                      AI PLATFORM
                     (gateway, registry,
                      tenancy, eval)
                           │
                    MODEL GATEWAY / ROUTER
                           │
                  MODEL SERVING (vLLM, Triton)
                           │
                 INFERENCE ENGINE (batch, KV)
                           │
                  GPU / ACCELERATOR (CUDA)
                           │
                    KUBERNETES (GPU, KEDA)
                           │
                CLOUD / INFRASTRUCTURE (Terraform)
```

---

## Learning philosophy

Study pages are **concept-first essays**—not a fixed template. Each topic is written in its own shape (diagrams, tables, stories, code) depending on what helps you reason about production systems.

**Hand-polished:** all of `00-foundations/`. **Narrative library:** `scripts/narrative_lib/m*.py` drives the rest.

Regenerate after editing narratives:

```powershell
Set-Location scripts
python narrative_curriculum.py
```

Do **not** use `generate_concept_material.py` (old static sections)—use `narrative_curriculum.py` only.

**Technology strategy**

| Layer | Stack |
|-------|--------|
| Platform / gateway | **Go** |
| AI apps, RAG, agents, eval | **Python** (FastAPI, PyTorch, HF) |
| Data | PostgreSQL, pgvector, Redis, Qdrant, Milvus |
| Serving | vLLM, KServe, Triton |
| Infra | Docker, Kubernetes, Helm, Terraform, GitHub Actions |
| Observability | Prometheus, Grafana, OpenTelemetry |

Teach **concepts before frameworks** (LangGraph, LlamaIndex, DSPy come after raw loops).

---

## How to navigate

| Document | Use |
|----------|-----|
| [ROADMAP.md](./ROADMAP.md) | 24 phases, recommended order |
| [PROGRESS.md](./PROGRESS.md) | Checklists per module and project |
| [GLOSSARY.md](./GLOSSARY.md) | Precise vocabulary |
| [INTERVIEW_MASTER.md](./INTERVIEW_MASTER.md) | Cross-cutting interview prep |
| [BUILD_LOG.md](./BUILD_LOG.md) | Portfolio journal template |
| `00-foundations` … `24-research` | Theory and depth |
| `22-projects` | Hands-on production projects |
| `23-interview-preparation` | Role-specific question banks |

---

## Recommended learning order

1. **Phase 1–2:** `00-foundations` (skim math if experienced) + `01-python-for-ai-engineering`  
2. **Phase 3–4:** `02-llm-fundamentals` + `03-llm-apis` + `04-prompt-engineering`  
3. **Phase 5–6:** `05-embeddings-and-vector-search` + `06-rag`  
4. **Phase 7–8:** `07-agents` + `08-mcp`  
5. **Phase 9–11:** `09-ai-frameworks` (compare) + `10-evaluation` + `11-fine-tuning`  
6. **Phase 12–14:** `12-model-serving` + `13-gpu` + `14-kubernetes-for-ai`  
7. **Phase 15–19:** Platform, infra, observability, security, production  
8. **Phase 20–24:** FDE, system design, projects, interviews, research  

Run **projects in parallel** once Phase 4 is underway (see ROADMAP).

---

## Project progression (`22-projects/`)

| # | Project |
|---|---------|
| 01 | LLM Chat API |
| 02 | RAG system |
| 03 | Production RAG |
| 04 | AI agent |
| 05 | MCP platform |
| 06 | Kubernetes AI agent |
| 07 | AI gateway (Go) |
| 08 | Model serving |
| 09 | AI observability |
| 10 | Multi-tenant AI platform |
| 11 | Enterprise capstone |

Each project README defines architecture, tests, Docker, observability, security, and BUILD_LOG expectations.

---

## Interview preparation

- Module **§19 Interview Questions** (Levels 1–2, Senior, Staff, FDE)  
- `23-interview-preparation/` by domain  
- `INTERVIEW_MASTER.md` for system design and debugging narratives  
- Portfolio **BUILD_LOG** stories for behavioral loops  

---

## Using this repository

1. Clone and work module-by-module; mark [PROGRESS.md](./PROGRESS.md).  
2. For each topic: read → implement exercise → tie to a project slice.  
3. Never skip **evaluation, security, or cost** on real features.  
4. Regenerate missing files (if any): `python scripts/generate_curriculum.py`  
5. Verify structure: `python scripts/verify_structure.py`  

---

## Status

Full markdown curriculum generated across all modules listed in the repository tree. Key topics (e.g. attention, RAG, KV cache) include extended depth; expand further via projects and your BUILD_LOG.

**Start:** [ROADMAP.md](./ROADMAP.md) Phase 1 → [00-foundations/mental-models.md](./00-foundations/mental-models.md)
