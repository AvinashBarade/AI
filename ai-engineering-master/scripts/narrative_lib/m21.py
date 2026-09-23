# 21-system-design

NARRATIVES = {
    "ai-chat-system": """# System Design: AI Chat

Components: auth, session store, gateway, model pool, moderation, feedback loop.

Scale: WebSocket/SSE streaming, regional stickiness optional, rate limits per user.

Design interview: capacity math on tokens/sec and storage for history retention policy.
""",
    "chatgpt": """# System Design: ChatGPT-Scale Product

Hypothetical staff question: multi-tenant isolation, plugin/tool sandbox, global routing, abuse detection, fine-grained cost controls.

Discuss moderation pipeline and data retention tiers—not just “call OpenAI.”
""",
    "rag-platform": """# System Design: RAG Platform

Ingestion workers, parse/chunk/embed, vector store per tenant, query API, eval service, admin console for reindex.

Failure: index lag monitor; blue/green index promotion API.
""",
    "agent-platform": """# System Design: Agent Platform

Workflow engine, tool registry, credential broker, HITL inbox, audit log, sandbox runtime.

Quota agent steps and tool classes per tenant tier.
""",
    "ai-gateway": """# System Design: AI Gateway

Go service: JWT auth, route table, Redis rate limits, OTel, provider adapters, streaming proxy.

Discuss idempotency keys for downstream side effects—not gateway responsibility alone.
""",
    "model-serving-platform": """# System Design: Model Serving Platform

Model artifact CI, GPU node pools, vLLM deployments, autoscaling metrics, multi-model routing, canary.

Cold start mitigation: keep min replicas, warm pools for flagship models.
""",
    "inference-platform": """# System Design: Inference Platform

Broader than serving: batch inference jobs, embedding fleet, scheduling, priority queues.

Fair scheduling between interactive and batch—batch must not starve chat.
""",
    "ai-observability-platform": """# System Design: AI Observability Platform

Collect traces/metrics from all teams' services; standard span names; cost attribution pipeline.

Privacy: sampling and redaction before long-term store.
""",
    "multi-tenant-ai-platform": """# System Design: Multi-Tenant AI Platform

Isolation levels (logical vs dedicated), per-tenant KMS, quotas, custom models optional, audit export.

Noisy neighbor on shared GPU—noisy neighbor on shared index—plan for both.
""",
    "enterprise-ai-platform": """# System Design: Enterprise AI Platform

Combines gateway, RAG, agents, registry, observability, SSO, data residency, admin RBAC.

Phased rollout: gateway first, then RAG, then agents—each gated by eval and security sign-off.
""",
}
