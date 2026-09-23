# 15-ai-platform-engineering

NARRATIVES = {
    "platform-architecture": """# AI Platform Architecture

Internal platform = gateway + registries + identity + observability + self-service APIs for product teams.

```text
Teams → Platform API → {models, indexes, tools} → shared policy
```

Goal: golden paths, guardrails, not ticket-driven one-offs.
""",
    "ai-gateway": """# AI Gateway (Platform)

Central auth, model routing, quotas, logging, PII redaction—Go-friendly tier.

Every prod LLM call flows through it; no API keys in microservices.
""",
    "model-registry": """# Model Registry

Catalog approved models: license, eval scores, max context, regions, deprecation dates.

Block arbitrary HuggingFace IDs in prod namespaces.
""",
    "prompt-registry": """# Prompt Registry

Versioned templates with owners and eval suites—ties to gateway `prompt_id` header.

Rollback prompt without redeploying all consumers if gateway resolves dynamically.
""",
    "feature-management": """# Feature Management

Flags for model routes, agent tools, RAG indexes—LaunchDarkly-style with tenant overrides.

Essential for safe rollout of stochastic features.
""",
    "model-routing": """# Model Routing (Platform)

Policy engine: tenant tier → model list, fallback chain, data residency constraints.

Log decisions for cost chargeback and incident replay.
""",
    "secrets": """# Secrets in AI Platform

Provider keys in vault; short-lived tokens to workers; never in prompts or traces.

Rotate keys without downtime via gateway dual-secret window.
""",
    "tenancy": """# Tenancy

Hard isolation: separate indexes, KMS keys, rate limits, and audit partitions per tenant.

Soft isolation (metadata filter only) is insufficient for regulated competitors on same cluster.
""",
    "quotas": """# Quotas

Tokens/day, concurrent agents, embedding GB—enforce at gateway before provider 429.

Soft quota warnings; hard stops with clear UX.
""",
    "rate-limiting": """# Rate Limiting

Token bucket per tenant + global breaker on provider outages.

Different limits for batch vs interactive—protect shared GPU pool.
""",
    "cost-management": """# Cost Management

Attribute spend: tenant × model × feature. Showbacks drive model downgrades and caching adoption.

FinOps review monthly—embedding reindex jobs surprise finance if untagged.
""",
    "platform-api": """# Platform API

Self-service: create index, register prompt, run eval job—Terraform/OpenAPI backed.

Document SLOs and supported patterns; escape hatch for advanced teams with review.
""",
}
