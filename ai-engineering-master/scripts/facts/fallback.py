"""Rich concept fallback when no hand-authored fact exists."""
from __future__ import annotations


def titleize(slug: str) -> str:
    return slug.replace("-", " ").title()


MODULE_CONTEXT: dict[str, str] = {
    "03-llm-apis": "Integrating production apps with model providers—streaming, limits, and routing.",
    "04-prompt-engineering": "Controlling LLM behavior through instructions, examples, and safe reasoning patterns.",
    "05-embeddings-and-vector-search": "Semantic search layer under RAG and recommendations.",
    "06-rag": "Retrieval-augmented generation: index, retrieve, ground, generate.",
    "07-agents": "LLM-driven control loops with tools, state, and guardrails.",
    "08-mcp": "Model Context Protocol for portable tools and resources.",
    "09-ai-frameworks": "Orchestration libraries—use after you understand raw loops.",
    "10-evaluation": "Measuring quality and preventing regressions in stochastic systems.",
    "11-fine-tuning": "Adapting weights when prompts and RAG are insufficient.",
    "12-model-serving": "High-throughput inference: batching, KV cache, runtimes.",
    "13-gpu-and-accelerator-infrastructure": "Hardware and parallelism for AI workloads.",
    "14-kubernetes-for-ai": "Running GPU inference and training on Kubernetes.",
    "15-ai-platform-engineering": "Internal platform: gateway, registry, tenancy, cost.",
    "16-ai-infrastructure": "Clusters, networking, capacity, and DR for AI.",
    "17-observability": "Metrics and traces for LLM, RAG, and agents.",
    "18-ai-security": "Threats unique to LLM systems and supply chain.",
    "19-production-ai": "Reliability patterns for AI in production.",
    "20-fde-engineering": "Customer-facing delivery from discovery to production.",
    "21-system-design": "End-to-end architectures at scale.",
    "23-interview-preparation": "Consolidated interview drills by topic.",
    "24-research": "Staying current without hype.",
}


SLUG_HINTS: dict[str, list[str]] = {
    "openai-compatible-apis": [
        "Chat Completions schema (messages, roles)",
        "SSE streaming chunks",
        "API keys and org/project scoping",
        "Retries on 429/5xx with exponential backoff",
        "Usage object: prompt_tokens, completion_tokens",
    ],
    "hybrid-search": [
        "Combine BM25 sparse + dense vectors",
        "Reciprocal rank fusion (RRF)",
        "Handles exact SKU/legal citations + semantic paraphrase",
        "Tune weights per corpus",
        "Often beats pure vector on enterprise docs",
    ],
    "kv-cache": [
        "Stores K/V per layer for past tokens",
        "Decode step only computes new token query",
        "Memory ∝ layers × batch × seq × head_dim",
        "PagedAttention reduces fragmentation",
        "Drives max concurrent users per GPU",
    ],
    "gpu-scheduling": [
        "Extended resources: nvidia.com/gpu",
        "Fractional GPUs (where supported)",
        "Queueing when GPUs saturated",
        "Pod priority and preemption policies",
        "Separate pools for train vs infer",
    ],
    "prompt-injection": [
        "Untrusted text overrides system intent",
        "Direct vs indirect (via RAG/tool output)",
        "Defenses: separation, filtering, privilege boundaries",
        "Never trust model to self-police",
        "Red-team eval sets",
    ],
}


def fallback(module: str, slug: str) -> dict:
    title = titleize(slug)
    ctx = MODULE_CONTEXT.get(module, "AI engineering practice.")
    hints = SLUG_HINTS.get(slug, [
        f"Define clear inputs/outputs for {title}.",
        f"Measure quality and latency for {title} in your stack.",
        f"Document failure modes specific to {title}.",
        f"Connect {title} to observability and cost.",
        f"Know when to simplify away {title} for a workflow.",
    ])
    return {
        "mental": f"**{title}** is a named piece of the AI stack. {ctx} Visualize data flowing *into* it, *through* it, and what can break at the boundary.",
        "why": f"Without a clear model of **{title}**, teams over-trust demos, mis-size infrastructure, or ship security holes. It exists to make the system **testable, operable, and cost-aware**.",
        "concepts": hints,
        "how": f"At runtime, **{title}** participates in the request path: validate context → apply domain logic → emit results and telemetry. Internals vary by vendor, but the **contract** (inputs, outputs, SLIs) is what you own in production.",
        "example": f"Enterprise assistant: when **{title}** misconfigured, users see wrong answers or slow responses even if the base model is strong—debug the layer, not only the model.",
        "bridge": "Same engineering habits as backend services: timeouts, idempotency where relevant, least privilege, structured logs, and load tests before peak traffic.",
        "production": [
            "Define SLIs (latency, error rate, quality metric) for this layer.",
            "Feature-flag changes; roll back independently of model version.",
            "Run game days for provider outage or index corruption.",
        ],
        "pitfalls": [
            "Skipping eval because 'the model is smart'.",
            "No tenant isolation at this layer.",
            "Unbounded retries blowing cost and rate limits.",
        ],
        "interview": [
            f"Explain **{title}** in 30 seconds.",
            f"One failure mode of **{title}** in production?",
            f"How does **{title}** affect cost or latency?",
        ],
        "practice": f"Draw a sequence diagram for one user request highlighting where **{title}** sits; list three metrics you would alert on.",
    }
