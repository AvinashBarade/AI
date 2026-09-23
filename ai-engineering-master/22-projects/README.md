# Projects Portfolio (v2 — 13 projects)

Build order is **flexible** by track—see [ROADMAP.md](../ROADMAP.md).

**Platform/infra track:** prioritize P09 gateway + P10 serving + P11 observability once P01–P02 exist.  
**Application track:** prioritize P03–P05 before P09.

All projects: [PROJECT_STANDARDS.md](./PROJECT_STANDARDS.md).

| # | Folder | Summary | Status |
|---|--------|---------|--------|
| 01 | [01-llm-api](./01-llm-chat-api/) | Core chat API (non-streaming first) | README [~] |
| 02 | 02-streaming-chat | SSE streaming, history | planned |
| 03 | 03-rag-system | Ingest → retrieve → generate | planned |
| 04 | 04-rag-evaluation-platform | Experiments + metrics + CI | planned |
| 05 | 05-production-rag | Hybrid, rerank, ACL, freshness | planned |
| 06 | 06-ai-agent | Tools, memory, HITL | planned |
| 07 | 07-mcp-platform | Git, K8s, Postgres, Prometheus, FS | planned |
| 08 | 08-kubernetes-ai-agent | Incident investigation | planned |
| 09 | 09-ai-gateway | Go: auth, routing, cost, breakers | planned |
| 10 | 10-model-serving | vLLM on K8s | planned |
| 11 | 11-ai-observability | LLM + RAG + agent dashboards | planned |
| 12 | 12-multi-tenant-ai-platform | Quotas, isolation | planned |
| 13 | [13-enterprise-ai-platform](./11-capstone-ai-platform/) | Capstone | README [~] |

_Note: folders `01-llm-chat-api` and `11-capstone-ai-platform` are legacy names; align to P01/P13 when renaming._
