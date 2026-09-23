# Project 11 — Enterprise AI Platform (Capstone)

**Unlock:** After Phases 7–9 (platform, infra, security, observability).

## Reference architecture

```text
                         Users
                           │
                           ↓
                     API Gateway
                           │
                           ↓
                      AI Gateway
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
            RAG          Agents       Models
             │             │             │
             ↓             ↓             ↓
        Vector DB        MCP         Model Router
                           │             │
                           └──────┬──────┘
                                  ↓
                           Model Serving
                                  │
                             Kubernetes
```

## Must include

Multi-tenancy, authZ, RAG, agents, MCP, routing, serving, observability, security, cost, eval, CI/CD, Terraform, Helm, DR, autoscaling.

## BUILD_LOG

Maintain a release-style BUILD_LOG per milestone (MVP → beta → prod).
