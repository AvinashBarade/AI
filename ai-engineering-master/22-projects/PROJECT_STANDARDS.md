# Project Standards (All 13 Projects)

Every portfolio project must be **production-grade engineering**, not a demo chatbot.

---

## Required artifacts

| Artifact | Description |
|----------|-------------|
| README.md | Goals, architecture, how to run, env vars |
| ARCHITECTURE.md | Diagrams, components, data flow |
| BUILD_LOG.md | From [template](../BUILD_LOG.md) |
| Code | Typed where applicable (Go / Python) |
| Tests | Unit + at least one integration test |
| Dockerfile | Reproducible run |
| Deploy | docker-compose and/or K8s manifests and/or Terraform slice |
| Observability | Metrics/traces (Prometheus/OTel minimum) |
| SECURITY.md | Threat notes, secrets handling, auth model |
| FAILURE_MODES.md | Known failures + runbook hints |
| perf/ | Load test script or k6/locust notes + results table |

---

## Non-functional requirements (default)

| Area | Minimum |
|------|---------|
| Latency | Document P50/P95; streaming where applicable |
| Cost | Token or GPU $ estimate per 1k requests |
| Reliability | Timeouts, retries with bounds, idempotency where relevant |
| Security | No secrets in git; least-privilege tools |

---

## Project ladder

| # | Name | Proves |
|---|------|--------|
| 01 | llm-api | API design, validation, token accounting |
| 02 | streaming-chat | SSE, backpressure, UX latency |
| 03 | rag-system | Pipeline correctness |
| 04 | rag-evaluation-platform | Metrics, regression gates |
| 05 | production-rag | Hybrid, ACL, freshness, citations |
| 06 | ai-agent | Bounded loop, HITL |
| 07 | mcp-platform | 5 MCP servers + client |
| 08 | kubernetes-ai-agent | Safe ops assistance |
| 09 | ai-gateway | Go control plane |
| 10 | model-serving | vLLM, autoscale, health |
| 11 | ai-observability | Full dashboards |
| 12 | multi-tenant-ai-platform | Isolation tests |
| 13 | enterprise-ai-platform | Capstone integration |

---

## Review before “done”

- [ ] Another engineer could deploy from README alone
- [ ] You have one **interview story** (problem → metric → trade-off)
- [ ] FAILURE_MODES has at least 5 real scenarios
