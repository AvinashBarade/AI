# Curriculum Architecture Review (v2)

**Date:** 2026-09-24  
**Audience:** Senior backend / platform / DevSecOps engineer → AI Platform / Infra / Staff / FDE  
**Action:** Architecture optimized; **no new lesson content** until approved.

---

## A. Current curriculum assessment (pre-v2)

Scores reflect **what exists today** (root docs + `00-foundations` + one Python bridge doc + project stubs)—not the full original master prompt.

| Target | Score (1–10) | Rationale |
|--------|--------------|-----------|
| **AI Engineer** | **4** | Strong mental models & math bridge; missing stack-wide `AI Engineering Core`, deep LLM/RAG/agents content, eval-first apps, PyTorch “what we serve” literacy. |
| **AI Platform** | **3** | Gateway/tenancy/registry planned late; no early platform map; projects don’t yet enforce platform primitives (quotas, routing) until project 07. |
| **AI Infra** | **3** | Inference/GPU/K8s modules exist only on paper; no capacity math, no prefix cache / parallelism depth; platform skills not wired to inference path early. |
| **FDE** | **2** | No case studies, discovery frameworks, or deliverable templates; FDE phase at end of 60-week sketch. |
| **Staff Engineer** | **3** | `INTERVIEW_MASTER` + foundations interviews help; system design & trade-off modules unwritten; cost/security not cross-cutting yet. |

**Strengths to keep**

- Production-first tone (failure modes, interview sections, BUILD_LOG).
- `00-foundations/mental-models.md` aligns with stack thinking.
- Go/Python split matches your profile.
- Incremental authoring rule (depth over file count).

**Weaknesses identified**

- **Sequencing:** LLM APIs before a unified **AI system map**; inference/platform **too late** for your primary leverage.
- **Duplication:** `mental-models.md` vs planned `ai-system-mental-model.md` (merge roles: tactical vs stack-wide).
- **Depth mismatch:** `00-foundations` math is right for AI Engineer interviews but **optional** for your infra/platform fast path; risk of weeks on theory before building.
- **Gaps:** PyTorch serving literacy, ML lifecycle registry, RAG ingestion/OCR/ACL, agent “when not to”, MCP enterprise security, capacity planning labs, FDE case library, threat models, 13-step project ladder with prod requirements.
- **Projects:** 11 projects vs required 13; project 01 bundles too much; missing dedicated **RAG eval** and **streaming** milestones; READMEs lack test/Docker/perf/security templates.
- **Time model:** Old roadmap fixed ~60 weeks; didn’t encode **20/30/30/10/10** allocation or infra-heavy parallel track.

---

## B. Missing topics (to add in STRUCTURE / authoring backlog)

### Stack & core

- `02-ai-engineering-core`: application vs system vs platform vs infra; training/fine-tune/inference/RAG/agents decision tree.
- `ai-to-existing-engineering-map.md` (added at repo root).

### LLM (expanded)

- Vocabulary, causal masking, transformer block, residuals, LayerNorm, FFN, logits/softmax, DPO, reasoning models, long-context techniques, explicit **Training vs FT vs Inference vs RAG vs Agents** doc.

### PyTorch (infra literacy)

- Tensors, device, autograd, train vs infer loop, DataLoader, GPU memory—not a DL course.

### RAG (flagship track)

- Ingestion: PDF/HTML/MD/DOCX/structured/OCR; cleaning, dedup; hybrid BM25+ANN; HNSW/IVF; MRR/nDCG; HyDE, contextual/parent-child/graph/multimodal/agentic RAG; freshness, reindex, tenancy, ACL, cache, cost.

### Agents

- Workflow vs agent vs multi-agent; bounded execution; sandboxing; when **not** to use agents.

### MCP

- AuthN/Z, remote/enterprise MCP, observability; **five** server projects (Git, K8s, Postgres, Prometheus, FS).

### ML lifecycle

- Data → dataset → train → FT → eval → registry → deploy → monitor; small LoRA project.

### Inference engineering

- Prefill/decode, KV, continuous batching, **prefix caching**, speculative decoding, quant (FP32–INT4), parallelism; **numeric** memory/throughput exercises.

### GPU infra

- HBM, PCIe/NVLink, memory bandwidth, compute vs memory bound.

### Platform & infra

- Full platform diagram (registry, gateway, eval, tenancy, audit); capacity exercise (10M req/day, 2K tokens, 4K RPS peak).

### K8s for AI

- No pod basics—GPU plugin, KEDA, canary inference, GPU observability.

### Observability

- RAG/agent-specific metrics and dashboards (not only infra CPU/GPU).

### Security

- Indirect injection, RAG poisoning, MCP/tool abuse, supply chain, threat model templates.

### FDE

- Seven case studies with discovery → rollout artifacts.

### Interview

- Per-track banks: infra capacity, platform governance, FDE scenarios (expand `23-interview-preparation`).

---

## C. Sequencing changes

| Before (v1) | After (v2) | Why |
|-------------|------------|-----|
| `00` → `01` → `02-llm` | `00` (skim math) → `01` (short) → **`02-ai-engineering-core`** → `03-llm` | Stack map before tokenizer details. |
| Platform phase ~month 10 | **Platform concepts** during Phase 2–3; **Project 09 gateway** no later than post-RAG | Your moat is control plane + K8s. |
| Inference/GPU month 7+ | **Phase 4 parallel track** for infra: `04-pytorch` + `14-inference` + capacity labs | Serve/optimize what you already run in prod. |
| Security phase 8 | **Security threads** from Phase 2 (RAG ACL) + Phase 3 (agents/MCP) | DevSecOps alignment. |
| Eval phase 4 | **Eval with Project 01–03** (chat golden set → RAG eval platform) | Quality gates early. |
| FDE end only | **FDE case studies** from Phase 5 onward; intensive Phase 8 | Solutions engineer readiness. |
| 11 projects | **13 projects** with explicit prod checklist | Portfolio matches staff loops. |

**Renumbering:** Modules use **v2 IDs** in `STRUCTURE.md`. Legacy `02-llm-fundamentals` → **`03-llm-fundamentals`** (folder created at authoring time).

---

## D. New modules (v2)

| ID | Folder | Purpose |
|----|--------|---------|
| NEW | `02-ai-engineering-core/` | Whole-stack mental model before LLM depth |
| REN | `03-llm-fundamentals/` | Expanded LLM (was `02-`) |
| NEW | `04-pytorch-fundamentals/` | Infra-level PyTorch |
| EXP | `08-rag/` | Deep RAG track (absorbs expanded 05–06 scope) |
| EXP | `09-agents/`, `10-mcp/` | Deeper agent + MCP |
| EXP | `14-inference-engineering/` | Major inference module (was `12-model-serving`) |
| EXP | `13-ml-lifecycle-fine-tuning/` | Clear lifecycle + small FT project |
| ROOT | `ai-to-existing-engineering-map.md` | Go/K8s/Terraform → AI roles |

Full file manifests: [STRUCTURE.md](./STRUCTURE.md).

---

## E. Project changes (v2)

| # | Project | Change |
|---|---------|--------|
| 01 | LLM API (non-streaming core) | Split from streaming; add tests, Docker, metrics |
| 02 | **Streaming chat** | NEW milestone |
| 03 | RAG pipeline | Was 02 |
| 04 | **RAG evaluation platform** | Was part of 03; explicit project |
| 05 | Production RAG | Hybrid, rerank, ACL, freshness |
| 06 | Agent | Bounded + HITL |
| 07 | MCP platform | **Five** servers |
| 08 | K8s AI agent | Incident investigation |
| 09 | AI Gateway (Go) | **Moved earlier** in recommended build order for platform track |
| 10 | Model serving | vLLM + K8s |
| 11 | AI observability | Full AI + RAG + agent dashboards |
| 12 | Multi-tenant platform | Isolation proofs |
| 13 | Enterprise capstone | Was 11 |

Each project: README, architecture, code, tests, Docker, deploy, observability, security, failure modes, perf test, BUILD_LOG.

---

## F. Updated 12–18 month roadmap (flexible phases)

See [ROADMAP.md](./ROADMAP.md) for detail. Summary:

```text
Phase 1 — Map & bridge        (2–3 w)   02-core, 01-python, skim 00
Phase 2 — LLM & chat          (4–6 w)   03-llm, APIs, prompts, P01–P02
Phase 3 — RAG flagship        (6–8 w)   07-embeddings, 08-rag, P03–P05
Phase 4 — Agents & MCP        (4–6 w)   09-10, P06–P07
Phase 5 — Platform & gateway    (4–6 w)   17-platform, P09, security basics
Phase 6 — Inference & GPU     (6–8 w)   04-pytorch, 14-inference, 15-gpu, P10
Phase 7 — K8s & infra         (4–6 w)   16-k8s, 18-infra, capacity labs
Phase 8 — Observability & sec (3–4 w)   19-obs, 20-sec, 21-prod, P11
Phase 9 — FDE & system design (4–6 w)   22-fde cases, 23-system-design
Phase 10 — Tenancy & capstone (8–12 w)  P12–P13
```

**Time allocation (default):** 20% theory · 30% implementation · 30% projects · 10% system design · 10% interview  

**Advanced modules (inference, platform, infra):** 20% theory · 40% projects · 20% system design · 20% interview  

No fixed week count—advance by **exit criteria** in ROADMAP.

---

## G. Recommended next step

1. **You:** Skim this review + [ROADMAP.md](./ROADMAP.md) + [ai-to-existing-engineering-map.md](./ai-to-existing-engineering-map.md). Confirm v2 numbering and whether **platform track** (gateway earlier) or **application track** (RAG-first) is primary for the next 8 weeks.
2. **Authoring (after approval):** `02-ai-engineering-core/ai-system-mental-model.md` first, then finish **short** `01-python` bundle, then `03-llm-fundamentals/tokens.md` onward.
3. **Do not** expand `00-foundations` math unless you want AI Engineer interview depth—mark complete via skim + checkpoints.

---

## Changelog (repo files updated in v2)

- `ROADMAP.md` — career ladder, phases, allocation, dual track notes
- `STRUCTURE.md` — v2 module manifest + expanded topic lists
- `PROGRESS.md` — phases, optional foundations, 13 projects, role focus
- `README.md` — progression diagram, v2 links
- `01-python-for-ai-engineering/README.md` — short bridge scope
- `22-projects/README.md` — 13-project ladder
- `02-ai-engineering-core/README.md` — module index (no lessons yet)
- `04-pytorch-fundamentals/README.md` — module index (no lessons yet)
- `00-foundations/README.md` — skim vs deep path
- **NEW** `ai-to-existing-engineering-map.md`
- **NEW** `CURRICULUM_REVIEW.md` (this file)

`00-foundations` lesson files unchanged.
