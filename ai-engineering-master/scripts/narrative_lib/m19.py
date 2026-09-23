# 19-production-ai

NARRATIVES = {
    "reliability": """# Reliability for Production AI

Design for provider outages, malformed JSON, empty retrieval, and partial streams.

User-visible errors should be honest—“try again” beats confident fiction.
""",
    "scalability": """# Scalability

Scale stateless gateway and app tiers horizontally; GPU tier on custom metrics; async embed pipelines.

Bottleneck moves to vector DB and provider rate limits—plan ahead.
""",
    "availability": """# Availability

Multi-region gateway; fallback models; read-only mode without agents when tools down.

SLO 99.9% for platform shell; maybe lower for best-effort AI add-on—set expectations.
""",
    "latency": """# Latency (Production)

Budget end-to-end; parallelize retrieval + classification where safe; stream tokens.

Set max context defaults—users paste novels otherwise.
""",
    "cost-optimization": """# Cost Optimization

Right-size model, cache prompts, batch embeds, cap agent loops, semantic cache with care.

Chargeback makes optimization sustainable—otherwise everyone picks GPT-4 class.
""",
    "caching": """# Caching (Production AI)

Exact match on prompt hash for deterministic tasks; semantic cache risks wrong answers—TTL and version keys mandatory.
""",
    "fallbacks": """# Fallbacks

Primary model timeout → smaller local model or cached response template.

Pre-test fallback quality on eval slice—bad fallback worse than error.
""",
    "retries": """# Retries

Retry idempotent LLM reads with jitter; never blind retry tool writes.

429 from provider needs respect for Retry-After and tenant fairness.
""",
    "circuit-breakers": """# Circuit Breakers

Open circuit on provider error storm; shed load; serve degraded experience.

Half-open probe with small traffic before full restore.
""",
    "multi-model-strategy": """# Multi-Model Strategy

Router sends easy queries to cheap model, hard to frontier—classifier can be small LLM or heuristics.

Monitor misroute rate—wrong tier hurts quality or cost.
""",
}
