#!/usr/bin/env python3
"""Generate complete ai-engineering-master markdown curriculum."""
from __future__ import annotations

import os
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STRUCTURE: dict[str, list[str]] = {
    "00-foundations": [
        "ai-vs-ml-vs-dl-vs-genai",
        "probability-statistics-for-ai",
        "linear-algebra-for-ai",
        "optimization",
        "information-theory",
        "mental-models",
    ],
    "01-python-for-ai-engineering": [
        "python-for-go-engineers",
        "numpy",
        "pandas",
        "typing",
        "async-python",
        "pydantic",
        "packaging",
    ],
    "02-llm-fundamentals": [
        "tokens",
        "tokenization",
        "embeddings",
        "transformers",
        "attention",
        "positional-encoding",
        "pretraining",
        "instruction-tuning",
        "alignment",
        "inference",
        "context-window",
        "temperature-sampling",
        "structured-output",
        "function-calling",
        "model-selection",
    ],
    "03-llm-apis": [
        "openai-compatible-apis",
        "anthropic",
        "gemini",
        "huggingface",
        "ollama",
        "model-routing",
    ],
    "04-prompt-engineering": [
        "prompting",
        "system-prompts",
        "few-shot",
        "chain-of-thought-concepts",
        "structured-prompts",
        "prompt-versioning",
        "prompt-injection",
    ],
    "05-embeddings-and-vector-search": [
        "embedding-models",
        "similarity",
        "cosine-similarity",
        "vector-indexes",
        "pgvector",
        "qdrant",
        "milvus",
        "vector-db-comparison",
    ],
    "06-rag": [
        "rag-fundamentals",
        "ingestion",
        "document-parsing",
        "chunking",
        "embedding-pipeline",
        "retrieval",
        "hybrid-search",
        "reranking",
        "metadata-filtering",
        "query-rewriting",
        "contextual-retrieval",
        "multimodal-rag",
        "graph-rag",
        "rag-evaluation",
        "rag-failure-modes",
        "production-rag",
    ],
    "07-agents": [
        "agent-fundamentals",
        "tool-calling",
        "planning",
        "memory",
        "state-machines",
        "agent-loops",
        "reflection",
        "multi-agent-systems",
        "human-in-the-loop",
        "agent-evaluation",
        "agent-security",
        "production-agents",
    ],
    "08-mcp": [
        "mcp-fundamentals",
        "architecture",
        "tools",
        "resources",
        "prompts",
        "transport",
        "security",
        "build-mcp-server",
    ],
    "09-ai-frameworks": [
        "langchain",
        "langgraph",
        "llamaindex",
        "dspy",
        "framework-tradeoffs",
    ],
    "10-evaluation": [
        "llm-evaluation",
        "rag-evaluation",
        "agent-evaluation",
        "offline-evaluation",
        "online-evaluation",
        "benchmarks",
        "hallucination",
        "faithfulness",
        "relevance",
        "evaluation-pipelines",
    ],
    "11-fine-tuning": [
        "prompting-vs-rag-vs-finetuning",
        "supervised-finetuning",
        "lora",
        "qlora",
        "adapters",
        "datasets",
        "training-loop",
        "evaluation",
        "when-to-finetune",
    ],
    "12-model-serving": [
        "inference-fundamentals",
        "batching",
        "continuous-batching",
        "kv-cache",
        "quantization",
        "speculative-decoding",
        "streaming",
        "vllm",
        "triton",
        "kserve",
        "model-gateway",
    ],
    "13-gpu-and-accelerator-infrastructure": [
        "gpu-fundamentals",
        "cpu-vs-gpu",
        "gpu-memory",
        "cuda",
        "cuda-kernels-concepts",
        "tensor-cores",
        "gpu-utilization",
        "multi-gpu",
        "tensor-parallelism",
        "pipeline-parallelism",
        "distributed-inference",
    ],
    "14-kubernetes-for-ai": [
        "gpu-scheduling",
        "gpu-device-plugin",
        "gpu-node-pools",
        "taints-tolerations",
        "affinity",
        "autoscaling",
        "keda",
        "cluster-autoscaler",
        "kserve",
        "ray",
        "ai-workloads",
    ],
    "15-ai-platform-engineering": [
        "platform-architecture",
        "ai-gateway",
        "model-registry",
        "prompt-registry",
        "feature-management",
        "model-routing",
        "secrets",
        "tenancy",
        "quotas",
        "rate-limiting",
        "cost-management",
        "platform-api",
    ],
    "16-ai-infrastructure": [
        "reference-architecture",
        "inference-clusters",
        "model-deployment",
        "distributed-inference",
        "storage",
        "networking",
        "caching",
        "reliability",
        "disaster-recovery",
        "capacity-planning",
    ],
    "17-observability": [
        "ai-observability",
        "prometheus",
        "grafana",
        "opentelemetry",
        "tracing",
        "token-metrics",
        "latency",
        "ttft",
        "cost-observability",
        "model-observability",
        "rag-observability",
    ],
    "18-ai-security": [
        "threat-model",
        "prompt-injection",
        "jailbreaks",
        "data-leakage",
        "rag-poisoning",
        "agent-security",
        "tool-security",
        "model-security",
        "pii",
        "secrets",
        "ai-supply-chain",
    ],
    "19-production-ai": [
        "reliability",
        "scalability",
        "availability",
        "latency",
        "cost-optimization",
        "caching",
        "fallbacks",
        "retries",
        "circuit-breakers",
        "multi-model-strategy",
    ],
    "20-fde-engineering": [
        "what-is-fde",
        "customer-discovery",
        "requirement-discovery",
        "solution-design",
        "enterprise-integrations",
        "data-integration",
        "customer-deployment",
        "debugging-production",
        "technical-communication",
        "architecture-presentations",
        "stakeholder-management",
    ],
    "21-system-design": [
        "ai-chat-system",
        "chatgpt",
        "rag-platform",
        "agent-platform",
        "ai-gateway",
        "model-serving-platform",
        "inference-platform",
        "ai-observability-platform",
        "multi-tenant-ai-platform",
        "enterprise-ai-platform",
    ],
    "23-interview-preparation": [
        "ai-fundamentals",
        "llm",
        "rag",
        "agents",
        "mcp",
        "ai-infrastructure",
        "kubernetes-ai",
        "system-design",
        "python",
        "coding",
        "behavioral",
        "fde",
    ],
    "24-research": [
        "emerging-models",
        "agent-trends",
        "inference-trends",
        "ai-infrastructure-trends",
        "important-papers",
    ],
}

PROJECTS = [
    ("01-llm-chat-api", "LLM Chat API", "FastAPI streaming chat, tools, structured output, token accounting"),
    ("02-rag-system", "RAG System", "Ingestion through generation with vector DB"),
    ("03-production-rag", "Production RAG", "Hybrid search, rerank, eval, citations, ACL"),
    ("04-ai-agent", "AI Agent", "Tools, memory, HITL, bounded loops"),
    ("05-mcp-platform", "MCP Platform", "MCP servers for Git, K8s, Postgres, Prometheus"),
    ("06-kubernetes-agent", "Kubernetes AI Agent", "Incident investigation with safe approvals"),
    ("07-ai-gateway", "AI Gateway", "Go gateway: auth, routing, limits, cost, observability"),
    ("08-model-serving", "Model Serving", "vLLM on Docker/Kubernetes with autoscaling"),
    ("09-ai-observability", "AI Observability", "Prometheus/Grafana/OTel for LLM/RAG/agents"),
    ("10-multi-tenant-ai-platform", "Multi-Tenant AI Platform", "Isolation, quotas, policies"),
    ("11-capstone-ai-platform", "Enterprise AI Platform Capstone", "Full stack integration"),
]

MODULE_BLURBS: dict[str, str] = {
    "00-foundations": "Mathematical and conceptual primitives for reasoning about ML and GenAI without a university course.",
    "01-python-for-ai-engineering": "Short bridge from Go/backend to Python AI services and notebooks.",
    "02-llm-fundamentals": "How decoder LLMs work from tokens through sampling and tool interfaces.",
    "03-llm-apis": "Production integration with model providers and routing.",
    "04-prompt-engineering": "Controlling model behavior, versioning, and injection defenses.",
    "05-embeddings-and-vector-search": "Semantic search foundations and vector database trade-offs.",
    "06-rag": "Retrieval-augmented generation end-to-end including production failure modes.",
    "07-agents": "Tool-using loops, planning, and when not to use agents.",
    "08-mcp": "Model Context Protocol for portable tools and enterprise hardening.",
    "09-ai-frameworks": "LangChain/LangGraph/LlamaIndex/DSPy compared after raw implementations.",
    "10-evaluation": "Offline/online metrics and CI gates for LLM systems.",
    "11-fine-tuning": "When to adapt weights vs prompt/RAG; LoRA/QLoRA practically.",
    "12-model-serving": "Inference engineering: batching, KV cache, quantization, vLLM.",
    "13-gpu-and-accelerator-infrastructure": "GPU architecture and distributed inference for infra engineers.",
    "14-kubernetes-for-ai": "GPU scheduling and AI workloads on Kubernetes (not K8s basics).",
    "15-ai-platform-engineering": "Internal AI platform: gateway, registry, tenancy, cost.",
    "16-ai-infrastructure": "Clusters, capacity planning, DR, and reference architectures.",
    "17-observability": "Metrics/traces for LLM, RAG, agents atop Prometheus/Grafana.",
    "18-ai-security": "Threat models aligned with DevSecOps practice.",
    "19-production-ai": "Reliability patterns for stochastic APIs.",
    "20-fde-engineering": "Customer discovery through production optimization.",
    "21-system-design": "Staff-level designs with capacity and cost.",
    "23-interview-preparation": "Question banks by role and level.",
    "24-research": "Emerging trends and paper reading for engineers.",
}


def titleize(slug: str) -> str:
    return slug.replace("-", " ").title()


def topic_extra(slug: str, module: str) -> dict[str, str]:
    """Topic-specific depth blocks."""
    s = slug
    m = module
    base = {
        "problem": f"Production AI systems need a clear engineering treatment of **{titleize(s)}** so teams do not confuse demos with dependable services.",
        "mental": f"Visualize **{titleize(s)}** as a component in a pipeline with inputs, invariants, SLIs, and explicit failure boundaries—not a black-box API call.",
        "arch": textwrap.dedent(f"""
```text
  Client / Data Source
         │
         ▼
  [{titleize(s)} layer]
         │
         ├── policy / validation
         ├── observability (trace, metrics)
         └── downstream (model, index, tool runtime)
```
""").strip(),
        "flow": f"1. Validate inputs and tenant context\n2. Apply {titleize(s)} logic with timeouts\n3. Emit structured result + telemetry\n4. Record cost and quality signals",
        "prod": "Run behind feature flags; version artifacts; load-test with production-like token lengths; define SLOs before launch.",
        "fail": "Timeouts, partial outages, bad payloads, quota exhaustion, and silent quality regression without metric movement.",
        "debug": "Use correlated trace IDs across gateway → app → retrieval → model; compare offline eval slice when online metrics drift.",
        "scale": "Horizontal scale stateless tiers; partition tenant data; cache stable prefixes; queue bursty embedding work.",
        "sec": "Assume untrusted prompts and documents; least-privilege credentials; audit privileged tool calls.",
        "obs": "Log redacted prompts, token counts, latency phases (TTFT vs decode), retrieval scores, and error classes.",
        "cost": "Attribute spend per tenant via token meters; right-size models; cache; batch embedding jobs.",
        "alt": "Simpler deterministic workflow, smaller model, or rules engine when variance and risk outweigh flexibility.",
        "use": "When the problem needs adaptability and language-heavy reasoning with measurable guardrails.",
        "nouse": "When requirements are fixed, deterministic, and provable—prefer code or classical ML.",
    }
    # Enriched overrides
    overrides: dict[str, dict[str, str]] = {
        "tokens": {
            "mental": "A **token** is the model's atomic input unit—like a word fragment ID from a fixed vocabulary. You pay and bound context by tokens, not characters.",
            "internal": "Text → tokenizer → integer token IDs → embedding lookup → transformer blocks → logits.",
            "code": 'print(len(tokenizer.encode("Hello world")))  # billable units',
        },
        "attention": {
            "mental": "Each token asks: *who in the sequence should I listen to?* Answers are softmax weights over keys.",
            "internal": r"Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) V. Multi-head runs parallel subspaces.",
            "code": "# See 02-llm-fundamentals/attention.md implementation section in module",
        },
        "kv-cache": {
            "mental": "Sticky notes for past tokens' K/V tensors so decode steps do not recompute the full prefix.",
            "internal": "Memory grows ~ O(layers × batch × seq × head_dim). Dominates long-context serving.",
            "cost": "VRAM is the bill; paging (PagedAttention) reduces fragmentation.",
        },
        "rag-fundamentals": {
            "mental": "Open-book exam: retrieve evidence chunks, inject into prompt, generate with citations.",
            "nouse": "When facts change minute-by-minute without indexing pipeline—you need tools/APIs, not static RAG alone.",
        },
        "prompt-injection": {
            "sec": "Treat document text and tool output as attacker-controlled; separate instructions from data channels.",
            "fail": "Tool exfiltration, policy bypass, cross-tenant data via confused deputy retrieval.",
        },
        "ai-gateway": {
            "mental": "Air traffic control for models: auth, quotas, routing, breakers, token accounting.",
            "arch": "```text\nClients → AI Gateway → {provider A, B, local vLLM}\n```",
        },
        "capacity-planning": {
            "flow": "1. Requests/sec × tokens/request\n2. Prefill vs decode FLOPs/memory\n3. GPU count + network\n4. Cost ceiling sensitivity",
            "prod": "Model peak factor 3–5× average; include cold-start buffer for scale-from-zero.",
        },
        "chain-of-thought-concepts": {
            "mental": "Reasoning models may use internal computation; in **your product**, expose structured steps or tool plans—not hidden chain-of-thought.",
            "sec": "Do not solicit or store hidden reasoning traces; use verifiable intermediate artifacts (plans, citations).",
        },
    }
    if s in overrides:
        base.update(overrides[s])
    if m == "14-kubernetes-for-ai":
        base["prod"] = "GPU node pools, device plugin, taints/tolerations, KEDA for queue depth, KServe/Ray for serving—assumes you already know Pod/Deployment basics."
    if m == "07-agents" and "security" in s:
        base["sec"] = "Tool allowlists, argument schema validation, human approval for destructive ops, per-tenant credentials."
    return base


def render_topic(module: str, slug: str) -> str:
    t = titleize(slug)
    e = topic_extra(slug, module)
    mod_title = module.split("-", 1)[-1].replace("-", " ").title()
    py = slug in {"numpy", "pandas", "pydantic", "async-python", "packaging"} or module.startswith("01-")
    lang = "python" if py or module in ("06-rag", "07-agents", "10-evaluation", "11-fine-tuning") else "go"
    impl = (
        "```python\n# Minimal pattern — extend in project code\nasync def handle() -> None:\n    ...\n```"
        if lang == "python"
        else '```go\nfunc Handler(w http.ResponseWriter, r *http.Request) {\n    ctx := r.Context()\n    // timeout, metrics, delegate\n}\n```'
    )
    if "internal" not in e:
        e["internal"] = f"Implement {t} as a pure function/core service with explicit inputs/outputs; property-test edge cases; fuzz untrusted strings when user-facing."

    iq = f"""
### Level 1
1. Define {t} in one sentence.
2. Why is {t} needed in production AI?
3. Name one metric for {t}.
4. Name one failure mode.
5. {t} vs the naive alternative?

### Level 2
1. How does {t} interact with observability?
2. How does {t} affect cost?
3. Debug scenario: latency doubled—what checks?
4. Security concern for {t}?
5. When should you NOT use {t}?

### Senior
1. Design {t} for multi-tenant SaaS.
2. How do you version and roll back {t}?
3. Capacity impact of {t} at 10k RPS?
4. SLO proposal for {t}.
5. Trade-off vs {e['alt'].split()[0] if e['alt'] else 'workflows'}?

### Staff
1. Platform standards for {t} across 20 teams.
2. Build vs buy for {t}.
3. Executive summary of risk for {t}.
4. 3-year roadmap coupling {t} and inference cost.
5. Incident postmortem outline involving {t}.

### FDE
1. Customer asks for {t} on day 1—what do you clarify?
2. Scope a 8-week pilot involving {t}.
"""

    return f"""# {t}

> Module: `{module}` · {MODULE_BLURBS.get(module, mod_title)}

## 1. Mental Model

{e['mental']}

## 2. Why This Exists

Engineers introduced **{t}** because monolithic \"just call the model\" approaches break down under real constraints: cost, security, latency, compliance, and measurable quality.

## 3. Problem It Solves

{e['problem']}

## 4. Architecture

{e['arch']}

## 5. Internal Working

{e['internal']}

## 6. Step-by-Step Flow

{e['flow']}

## 7. Example

**Scenario:** Enterprise assistant for internal docs.

Apply **{t}** at the boundary where {mod_title} meets policy: validate tenant, execute core logic, return auditable output.

## 8. Implementation

{impl}

{e.get('code', '')}

## 9. Production Architecture

{e['prod']}

Connect to your existing stack: **Go** for gateways/workers, **Python** for model/RAG glue, **Kubernetes** for serving, **Terraform** for GPU pools, **Prometheus/Grafana** for SLIs.

## 10. Failure Modes

{e['fail']}

## 11. Debugging

{e['debug']}

## 12. Scaling

{e['scale']}

## 13. Security

{e['sec']}

## 14. Observability

{e['obs']}

## 15. Cost

{e['cost']}

## 16. Trade-offs

| Choose {t} | Avoid {t} |
|------------|-----------|
| {e['use']} | {e['nouse']} |

## 17. When To Use

{e['use']}

## 18. When NOT To Use

{e['nouse']}

## 19. Interview Questions

{iq}

## 20. Practical Exercise

Implement a minimal slice of **{t}** in isolation with unit tests and a metric (latency or quality). Document one hypothesis and measure before/after.

## 21. Project

Map **{t}** to a milestone in `22-projects/` (see repository README). Add a BUILD_LOG entry when integrated.

---

**Related:** [GLOSSARY.md](../GLOSSARY.md) · [ROADMAP.md](../ROADMAP.md) · [INTERVIEW_MASTER.md](../INTERVIEW_MASTER.md)
"""


def render_project(folder: str, name: str, desc: str) -> str:
    return f"""# Project — {name}

{desc}

## Architecture

```text
Client → API → {{core services}} → Model / Vector DB / Tools
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
"""


def write_root_files() -> None:
    readme = ROOT / "README.md"
    if readme.exists():
        pass  # will overwrite below in separate enhanced write
    # ROADMAP generated in enhanced block
    pass


def main() -> None:
    count = 0
    for module, slugs in STRUCTURE.items():
        mod_path = ROOT / module
        mod_path.mkdir(parents=True, exist_ok=True)
        for slug in slugs:
            path = mod_path / f"{slug}.md"
            content = render_topic(module, slug)
            if path.exists() and module == "00-foundations" and slug in (
                "ai-vs-ml-vs-dl-vs-genai",
                "mental-models",
            ):
                # keep richer hand-authored foundations if longer
                if path.stat().st_size > 8000:
                    continue
            path.write_text(content, encoding="utf-8")
            count += 1

    proj_root = ROOT / "22-projects"
    for folder, name, desc in PROJECTS:
        p = proj_root / folder
        p.mkdir(parents=True, exist_ok=True)
        (p / "README.md").write_text(render_project(folder, name, desc), encoding="utf-8")
        count += 1

    print(f"Generated/updated {count} topic and project files.")


if __name__ == "__main__":
    main()
