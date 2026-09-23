# Repository Structure (v2 Manifest)

**Legend:** `[x]` substantive content · `[~]` partial · `[ ]` planned · `(opt)` optional for platform/infra fast path

**Renumbering:** v1 `02-llm-fundamentals` → **`03-llm-fundamentals`**. Folders are created when modules are authored.

---

## Root

| File | Status |
|------|--------|
| README.md | [x] v2 update |
| ROADMAP.md | [x] v2 |
| PROGRESS.md | [x] v2 |
| STRUCTURE.md | [x] |
| GLOSSARY.md | [x] |
| INTERVIEW_MASTER.md | [x] |
| BUILD_LOG.md | [x] |
| CURRICULUM_REVIEW.md | [x] |
| ai-to-existing-engineering-map.md | [x] |

---

## 00-foundations (math & vocabulary)

| File | Status | Note |
|------|--------|------|
| README.md | [x] | Skim vs deep path |
| mental-models.md | [x] | Tactical models; pair with `02` stack doc |
| ai-vs-ml-vs-dl-vs-genai.md | [x] | |
| probability-statistics-for-ai.md | [x] | (opt) skim |
| linear-algebra-for-ai.md | [x] | (opt) skim |
| optimization.md | [x] | (opt) skim |
| information-theory.md | [x] | (opt) skim |

---

## 01-python-for-ai-engineering (SHORT bridge)

| File | Status |
|------|--------|
| README.md | [x] scope |
| python-for-go-engineers.md | [~] |
| typing.md | [ ] |
| pydantic.md | [ ] |
| async-python.md | [ ] |
| fastapi-patterns.md | [ ] |
| httpx-and-apis.md | [ ] |
| numpy-basics.md | [ ] |
| pandas-basics.md | [ ] |
| venv-uv-packaging.md | [ ] |
| testing-pytest.md | [ ] |
| notebooks-jupyter.md | [ ] |
| pytorch-basics.md | [ ] |
| python-advanced-(opt).md | [ ] optional pointer only |

---

## 02-ai-engineering-core **NEW**

| File | Status |
|------|--------|
| README.md | [x] index |
| ai-system-mental-model.md | [ ] **author first** |
| application-vs-system-vs-platform.md | [ ] |
| training-inference-rag-agents-decision-tree.md | [ ] |
| components-map.md | [ ] |
| lifecycle-and-ownership.md | [ ] |

---

## 03-llm-fundamentals (expanded)

| File | Status |
|------|--------|
| tokens.md, tokenization.md, vocabulary.md | [ ] |
| embeddings.md | [ ] |
| positional-encoding.md | [ ] |
| attention.md, self-attention.md, multi-head-attention.md | [ ] |
| causal-masking.md | [ ] |
| transformer-block.md | [ ] |
| residual-connections.md, layer-normalization.md | [ ] |
| feed-forward-networks.md | [ ] |
| logits.md, softmax.md, next-token-prediction.md | [ ] |
| transformers.md | [ ] |
| pretraining.md, instruction-tuning.md | [ ] |
| alignment.md, rlhf.md, dpo.md | [ ] |
| reasoning-models.md | [ ] |
| inference.md, context-window.md, long-context-techniques.md | [ ] |
| temperature-sampling.md, top-k-top-p.md | [ ] |
| structured-output.md, function-calling.md | [ ] |
| model-selection.md | [ ] |
| training-vs-finetuning-vs-inference-vs-rag-vs-agents.md | [ ] |

---

## 04-pytorch-fundamentals **NEW**

| File | Status |
|------|--------|
| README.md | [x] index |
| tensors-shapes-dtypes.md | [ ] |
| device-cpu-gpu.md | [ ] |
| autograd-forward-backward.md | [ ] |
| optimizer-loss.md | [ ] |
| training-loop.md, inference-loop.md | [ ] |
| batching-dataloader.md | [ ] |
| gpu-memory.md | [ ] |

---

## 05-llm-apis · 06-prompt-engineering

(As v1 list: openai-compatible, anthropic, gemini, huggingface, ollama, model-routing; prompting, system-prompts, few-shot, CoT, versioning, injection.)

---

## 07-embeddings-and-vector-search

embedding-models, similarity, cosine, indexes, pgvector, qdrant, milvus, comparison.

---

## 08-rag **DEEP TRACK**

### Ingestion

pdf.md, html.md, markdown.md, docx.md, structured-data.md, ocr-concepts.md

### Processing

cleaning.md, normalization.md, chunking.md, metadata.md, deduplication.md

### Retrieval

dense-retrieval.md, sparse-retrieval.md, bm25.md, hybrid-retrieval.md, ann.md, hnsw.md, ivf.md, metadata-filters.md

### Quality

top-k.md, precision-recall.md, mrr.md, ndcg.md, reranking.md

### Advanced

query-rewriting.md, hyde.md, contextual-retrieval.md, parent-child-retrieval.md, multi-query-retrieval.md, graph-rag.md, multimodal-rag.md, agentic-rag.md

### Production

rag-fundamentals.md, freshness.md, reindexing.md, incremental-indexing.md, multi-tenancy.md, access-control.md, caching.md, observability.md, cost.md, rag-evaluation.md, rag-failure-modes.md, production-rag.md

### Clarifiers

rag-is-not-training.md, prompt-vs-rag-vs-finetune-vs-pretrain.md

---

## 09-agents **DEEP**

agent-fundamentals.md, agent-loop.md, tool-calling.md, planning.md, state.md, memory.md, reflection.md, retries.md, delegation.md, multi-agent-systems.md, workflows-vs-agents.md, deterministic-orchestration.md, bounded-execution.md, human-in-the-loop.md, permissions.md, tool-sandboxing.md, agent-evaluation.md, agent-security.md, production-agents.md, when-not-to-use-agents.md

---

## 10-mcp **EXPANDED**

mcp-fundamentals.md, architecture.md, client.md, server.md, tools.md, resources.md, prompts.md, transport.md, authentication.md, authorization.md, security.md, remote-mcp.md, enterprise-mcp.md, mcp-observability.md, build-mcp-server.md

**MCP build projects:** git, kubernetes, postgresql, prometheus, filesystem servers (under `22-projects/07-mcp-platform/`).

---

## 11-ai-frameworks

langchain.md, langgraph.md, llamaindex.md, dspy.md, framework-tradeoffs.md — **compare, don’t worship**

---

## 12-evaluation · 13-ml-lifecycle-fine-tuning

**12:** llm/rag/agent eval, offline/online, pipelines, hallucination, faithfulness.

**13:** lifecycle diagram (data → monitor), SFT, LoRA, QLoRA, adapters, datasets, data-quality, checkpoints, registry, deployment hook, overfitting, catastrophic-forgetting, small-ft-project.md

---

## 14-inference-engineering **MAJOR** (was 12-model-serving)

inference-fundamentals.md, prefill-decode.md, kv-cache.md, batching.md, continuous-batching.md, prefix-caching.md, speculative-decoding.md, quantization-fp32-int4.md, streaming.md, tensor-parallelism.md, pipeline-parallelism.md, model-parallelism.md, vllm.md, triton.md, kserve.md, model-gateway.md, capacity-math.md, why-inference-is-expensive.md

---

## 15-gpu · 16-k8s · 17-platform · 18-infra · 19-obs · 20-sec · 21-prod

**15 GPU:** architecture, CUDA runtime, kernels (concepts), VRAM, HBM, PCIe, NVLink, tensor cores, utilization, bandwidth, compute-vs-memory-bound, multi-gpu.

**16 K8s for AI:** GPU plugin, scheduling, node pools, taints, affinity, topology, KEDA, cluster autoscaler, KServe, Ray, rollout/canary, inference autoscaling, GPU observability — **no basic K8s**.

**17 Platform:** registry, catalog, routing, prompt registry, eval platform, gateway, tenancy, quotas, rate limits, cost allocation, secrets, RBAC, audit, deployment workflows.

**18 Infra:** inference clusters, GPU clusters, scheduling, capacity planning, networking, storage, model load/cache, autoscaling, HA, DR, multi-region, cost.

**19 Observability:** infra + LLM + RAG + agent metrics, dashboards.

**20 Security:** injection, jailbreak, exfiltration, RAG poisoning, tool abuse, MCP, supply chain, PII, tenant isolation, threat-model templates.

**21 Production:** reliability, fallbacks, circuit breakers, multi-model strategy.

---

## 22-fde-engineering · 23-system-design · 25-interview · 26-research

**22 FDE:** discovery → optimization loop; cases: enterprise RAG, support, coding assistant, DevOps agent, multi-tenant enterprise, AI search, document intelligence.

**23 System design:** 20+ problems (ChatGPT, RAG platform, gateway, serving, observability, multi-tenant, enterprise, …).

**25-interview-preparation/** per domain + coding (Go) + FDE.

**26-research/** emerging models, agents, inference, infra trends, papers guide.

---

## 24-projects (13)

| # | Folder | Status |
|---|--------|--------|
| 01 | llm-api | [~] README |
| 02 | streaming-chat | [ ] |
| 03 | rag-system | [ ] |
| 04 | rag-evaluation-platform | [ ] |
| 05 | production-rag | [ ] |
| 06 | ai-agent | [ ] |
| 07 | mcp-platform | [ ] |
| 08 | kubernetes-ai-agent | [ ] |
| 09 | ai-gateway | [ ] |
| 10 | model-serving | [ ] |
| 11 | ai-observability | [ ] |
| 12 | multi-tenant-ai-platform | [ ] |
| 13 | enterprise-ai-platform-capstone | [~] README |

See [22-projects/PROJECT_STANDARDS.md](./22-projects/PROJECT_STANDARDS.md).

---

## v1 → v2 module ID map

| v1 folder | v2 folder |
|-----------|-----------|
| 02-llm-fundamentals | 03-llm-fundamentals |
| 03-llm-apis | 05-llm-apis |
| 04-prompt-engineering | 06-prompt-engineering |
| 05-embeddings… | 07-embeddings… |
| 06-rag | 08-rag |
| 07-agents | 09-agents |
| 08-mcp | 10-mcp |
| 09-frameworks | 11-ai-frameworks |
| 10-evaluation | 12-evaluation |
| 11-fine-tuning | 13-ml-lifecycle-fine-tuning |
| 12-model-serving | 14-inference-engineering |
| 13-gpu | 15-gpu |
| 14-k8s | 16-k8s |
| 15-platform | 17-platform |
| 16-infra | 18-infra |
| 17-obs | 19-obs |
| 18-sec | 20-sec |
| 19-prod | 21-prod |
| 20-fde | 22-fde |
| 21-system-design | 23-system-design |
| 22-projects | 24-projects (use `22-projects` path until rename) |
| 23-interview | 25-interview |
| 24-research | 26-research |

*Physical path `22-projects/` retained for now to avoid breaking links; alias noted in README.*
