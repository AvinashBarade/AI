# 17-observability

NARRATIVES = {
    "ai-observability": """# AI Observability

Beyond RED metrics: **quality**, **cost**, and **context** signals per request.

Trace spans: gateway → retrieval → prefill → decode → tools.
""",
    "prometheus": """# Prometheus for AI

Counters: tokens in/out, requests by model. Histograms: latency phases. Gauges: queue depth, GPU util from DCGM.

Avoid high-cardinality labels (full prompt text)—use hashed prompt_id.
""",
    "grafana": """# Grafana Dashboards

Panels: p50/p95 TTFT, cost per tenant, retrieval recall proxy, tool error rate.

Link traces from exemplars for debugging slow requests.
""",
    "opentelemetry": """# OpenTelemetry

Standardize trace propagation across Go gateway and Python workers.

Baggage for tenant_id—careful with PII in attributes.
""",
    "tracing": """# Tracing LLM Apps

One trace_id per user request; child spans for each LLM call and tool.

Compare traces when users report “slow Tuesday”—often retrieval or rerank regression.
""",
    "token-metrics": """# Token Metrics

Input/output tokens drive cost and latency—meter at gateway from provider `usage`.

Alert on anomaly spikes (looping agent, prompt leak).
""",
    "latency": """# Latency Breakdown

Split: queue wait, prefill, time-to-first-token, inter-token latency, tool RTT.

Optimizing wrong phase wastes engineering—profile first.
""",
    "ttft": """# TTFT (Time to First Token)

User-perceived speed for streaming—prefill bound.

Long system prompts and RAG context inflate TTFT; cache and trim context.
""",
    "cost-observability": """# Cost Observability

$/1k requests by tenant, model, feature flag.

Export to billing warehouse nightly—real-time approximations OK for ops, finance wants reconciliation.
""",
    "model-observability": """# Model Observability

Track model version, temperature, finish reason distribution, refusal rate.

Sudden `length` finish reason spike → users hitting max_tokens cap.
""",
    "rag-observability": """# RAG Observability

Log retrieved chunk IDs, scores, index version, embed model.

Dashboard: empty retrieval rate, average k, hybrid branch usage.
""",
}
