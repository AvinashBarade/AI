# Project — AI Observability

Prometheus/Grafana/OTel for LLM/RAG/agents

## Architecture

```text
Client → API → {core services} → Model / Vector DB / Tools
              ↘ observability (OTel) ↘ policy (auth, quotas)
```

## Requirements

- [ ] README (this file) + ARCHITECTURE.md
- [ ] Code (Python and/or Go per ROADMAP)
- [ ] Tests (unit + integration)
- [ ] Dockerfile + compose or Helm
- [ ] Observability: metrics + traces
- [ ] SECURITY.md + FAILURE_MODES.md
- [ ] BUILD_LOG.md (see root template)

## Build phases

1. MVP correctness
2. Hardening (timeouts, retries, limits)
3. Observability and cost accounting
4. Load test + document results

## Failure modes

Document at least five production failures and mitigations before marking complete.

## Interview story

Prepare a 2-minute STAR narrative: constraint → decision → metric → outcome.
