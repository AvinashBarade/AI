# noqa: D100
"""Concept facts for modules 03–24. Each entry is concept-focused study material."""

from __future__ import annotations


def titleize(slug: str) -> str:
    return slug.replace("-", " ").title()


def _t(
    mental: str,
    why: str,
    concepts: list[str],
    how: str = "",
    example: str = "",
    bridge: str = "Apply the same reliability patterns you use for backend microservices: timeouts, budgets, and traces.",
    production: list[str] | None = None,
    pitfalls: list[str] | None = None,
    interview: list[str] | None = None,
    practice: str = "",
    code: str = "",
    extra: str = "",
) -> dict:
    return {
        "mental": mental,
        "why": why,
        "concepts": concepts,
        "how": how
        or "Validate inputs → execute core logic with bounded time/resources → return structured output and emit metrics.",
        "example": example or "See your `22-projects/` milestone for hands-on integration.",
        "bridge": bridge,
        "production": production
        or [
            "Define SLIs and alert on regressions.",
            "Version artifacts and roll back independently.",
            "Load-test with production-like token lengths.",
        ],
        "pitfalls": pitfalls
        or [
            "Treating provider demos as your SLA.",
            "Missing tenant isolation.",
            "No eval gate in CI.",
        ],
        "interview": interview
        or ["30-second explanation?", "Top failure mode?", "Cost or latency driver?"],
        "practice": practice or "Add one metric and one integration test for this topic in a project.",
        "code": code,
        "extra": extra,
    }


CONTENT: dict[str, dict[str, dict]] = {}

# --- 03 LLM APIs ---
CONTENT["03-llm-apis"] = {
    "openai-compatible-apis": _t(
        "Many providers expose the **same JSON shape** (messages, model, stream) so one client can switch endpoints.",
        "Avoid N custom SDK integrations; standardize retries, streaming parsers, and token accounting once.",
        [
            "POST /v1/chat/completions",
            "Roles: system, user, assistant, tool",
            "stream: true → SSE deltas",
            "usage.prompt_tokens / completion_tokens",
            "tool_calls in assistant message",
        ],
        how="Wrap httpx/Go client with middleware: auth, retry, metrics, redacted logging.",
        example="Azure OpenAI and local vLLM both behind one gateway route.",
        bridge="Implement the client in Go at the gateway; Python services call gateway not raw keys.",
        code="```python\nasync with httpx.AsyncClient() as c:\n    r = await c.post(url, json={\"model\": \"...\", \"messages\": [...]})\n```",
    ),
    "anthropic": _t(
        "Anthropic APIs emphasize **long context** and **messages API** with system as separate parameter on some versions.",
        "Enterprise buyers often require Anthropic; your platform must abstract provider differences.",
        ["Messages API", "System prompt handling", "Tool use blocks", "PDF/document inputs (product-dependent)", "Rate limit headers"],
        bridge="Map Anthropic response blocks to your internal ChatCompletion type in gateway.",
    ),
    "gemini": _t(
        "Google Gemini integrates with **Vertex AI** and Google Cloud IAM—common in GCP-first enterprises.",
        "Multi-cloud platforms need a Gemini adapter with GCP auth and regional endpoints.",
        ["Vertex vs AI Studio", "Service account auth", "Safety settings", "Multimodal parts", "Quota projects"],
    ),
    "huggingface": _t(
        "Hugging Face is **model hub + libraries**—download weights, tokenizers, run Inference API or self-host.",
        "Self-hosting open weights is the path to private inference clusters.",
        ["Model cards", "transformers AutoModel", "Inference Endpoints", "GGUF/local runtimes", "License per model"],
    ),
    "ollama": _t(
        "Ollama runs **local models** on laptop or server—great for dev, not a full prod story alone.",
        "Developers iterate without cloud spend; platform teams still need governed prod routing.",
        ["pull/run CLI", "OpenAI-compatible local port", "Quantized models", "Single-node limits", "No multi-tenant isolation by default"],
    ),
    "model-routing": _t(
        "A **router** picks model/provider per request based on policy, cost, latency, or task type.",
        "Central place for compliance (data residency) and economizing small vs large models.",
        ["Rule-based vs learned routing", "Fallback chains", "Shadow traffic", "A/B prompt+model experiments", "Circuit breaker per provider"],
        bridge="This is core **AI gateway** logic—ideal Go service.",
    ),
}

# --- 04 Prompt engineering ---
CONTENT["04-prompt-engineering"] = {
    "prompting": _t(
        "A **prompt** is the programmable interface to a frozen model—instructions + context + examples.",
        "Most product iteration happens here before fine-tuning.",
        ["Zero-shot vs few-shot", "Instruction clarity", "Output format spec", "Delimiters for data", "Negative instructions (what not to do)"],
    ),
    "system-prompts": _t(
        "The **system** message sets persistent behavior, tone, and policy for the session.",
        "Separates operator intent from untrusted user content.",
        ["Policy and persona", "Tool usage rules", "Citation requirements", "Refusal guidelines", "Keep stable across turns"],
    ),
    "few-shot": _t(
        "Include **example input/output pairs** in the prompt to steer format and task.",
        "Cheap way to adapt without weight updates—costs tokens.",
        ["Example ordering bias", "Diverse examples", "Label leakage in examples", "Dynamic example selection", "Eval per example set"],
    ),
    "chain-of-thought-concepts": _t(
        "**Reasoning** can mean explicit plans, tool steps, or verifier checks—not hidden private chain-of-thought.",
        "Regulations and safety discourage exposing/raw-storing hidden reasoning; products use structured plans.",
        [
            "Reasoning models (o-series class) use more inference compute",
            "Expose **verifiable** steps: citations, tool traces",
            "Do not ask models to print secret scratchpad in prod",
            "Test-time compute vs single-shot",
            "Eval reasoning with outcome metrics",
        ],
        pitfalls=["Storing raw CoT with PII", "Trusting unverified long reasoning"],
    ),
    "structured-prompts": _t(
        "Templates with **variables** (Jinja-style) versioned like code.",
        "Scale prompts across tenants and locales safely.",
        ["Partial templates", "Injection via variables", "Schema for variables", "Preview/render in CI", "Diff on PR"],
    ),
    "prompt-versioning": _t(
        "Prompts are **code**—git tags, registry, and eval gates per version.",
        "Rollback prompts faster than rollback models.",
        ["prompt_id + version in traces", "Link to eval scores", "Canary rollout", "Immutable production versions"],
        bridge="Prompt registry is a platform feature alongside model registry.",
    ),
    "prompt-injection": _t(
        "Attacker-controlled text tries to **override system instructions** or exfiltrate secrets.",
        "RAG and tools multiply attack surface—core DevSecOps concern.",
        [
            "Direct injection in user chat",
            "Indirect via retrieved doc or tool JSON",
            "Delimiter fencing and instruction hierarchy",
            "Output filtering and DLP",
            "Least-privilege tools",
        ],
        pitfalls=["Trusting system prompt alone", "Concatenating untrusted HTML into instructions"],
    ),
}

# --- 05 Embeddings ---
CONTENT["05-embeddings-and-vector-search"] = {
    "embedding-models": _t(
        "Models map text → **vectors**; choice affects recall in RAG.",
        "Wrong model = semantic near-misses in production.",
        ["bi-encoders vs cross-encoders", "e5/bge/gecko-class families", "Multilingual models", "Matryoshka dims", "API vs self-host"],
    ),
    "similarity": _t(
        "Similarity scores rank candidates—usually cosine or dot on normalized vectors.",
        "Foundation of retrieval ranking before rerank.",
        ["Dot vs cosine vs L2", "Score calibration", "Threshold for 'no answer'", "Hybrid with sparse scores"],
    ),
    "cosine-similarity": _t(
        "Cosine measures **angle** between vectors—magnitude-invariant when normalized.",
        "Standard in text embeddings when vectors are L2-normalized.",
        ["cos = dot / (|a||b|)", "Range [-1,1]", "ANN indexes assume metric", "Batch via matrix multiply"],
        code="```python\nimport numpy as np\na,b = ...\ncos = np.dot(a,b) / (np.linalg.norm(a)*np.linalg.norm(b))\n```",
    ),
    "vector-indexes": _t(
        "**ANN indexes** avoid brute-force scan over millions of vectors.",
        "Latency and recall trade-off for RAG at scale.",
        ["HNSW graph", "IVF clusters", "Product quantization", "Exact brute force for small N", "Rebuild vs incremental"],
    ),
    "pgvector": _t(
        "**Postgres + pgvector** keeps vectors with relational metadata and ACID.",
        "Great when you already run Postgres and need joins + ACL columns.",
        ["vector column type", "IVFFlat/HNSW indexes", "SQL filters + ORDER BY distance", "Connection pooling", "Vacuum/index rebuild"],
        bridge="Familiar SQL ops + Terraform for RDS/Aurora.",
    ),
    "qdrant": _t(
        "Qdrant is a **purpose-built vector DB** with filtering and HNSW.",
        "Microservice-friendly for RAG scale-out.",
        ["Collections", "Payload filters", "Quantization", "Replication", "gRPC/REST"],
    ),
    "milvus": _t(
        "Milvus targets **large-scale** vector workloads with distributed components.",
        "When billion-vector scale and dedicated vector ops team.",
        ["Segments", "MinIO/etcd dependencies", "GPU index build options", "Cloud managed offerings"],
    ),
    "vector-db-comparison": _t(
        "Pick store based on **scale, ops, metadata, and team skills**—not benchmarks alone.",
        "Architecture decision for multi-year RAG platform.",
        ["pgvector vs dedicated", "Managed vs self-host", "Multi-tenancy patterns", "Cost at 100M vectors", "Migration path"],
    ),
}

# --- 06 RAG (deep) ---
_rag = lambda slug, mental, why, concepts, **kw: (slug, _t(mental, why, concepts, **kw))
_rag_entries = [
    _rag(
        "rag-fundamentals",
        "RAG = **retrieve evidence, then generate** with citations. It does not automatically retrain the model.",
        "Ground answers in private/current docs; reduce hallucination on facts.",
        [
            "Index pipeline (offline) vs query path (online)",
            "Retrieval ceiling on answer quality",
            "Citations for audit",
            "Not a substitute for access control",
            "Prompt + RAG + FT are complementary",
        ],
        example="HR bot retrieves policy PDF chunks before answering leave questions.",
    ),
    _rag("ingestion", "Continuous **document intake** from drives, tickets, wikis.", "Knowledge changes; index must refresh.", ["Connectors", "ACL at source", "Change detection", "Backpressure queues", "Poison document handling"]),
    _rag("document-parsing", "Turn PDF/HTML into **clean text** preserving structure.", "Garbage parse → garbage chunks.", ["PDF layout", "Tables", "Headers hierarchy", "OCR when scanned", "Encoding issues"]),
    _rag(
        "chunking",
        "Split docs into **segments** that fit embedding context.",
        "Too small loses context; too large dilutes retrieval.",
        ["Fixed token windows", "Overlap", "Semantic chunking", "Parent-child chunks", "Markdown-aware splits"],
        how="Parse document tree → choose strategy (headers/tokens) → emit chunks with stable IDs and source offsets → store metadata for citations.",
    ),
    _rag("embedding-pipeline", "Batch **embed chunks** and upsert to index.", "Usually async, idempotent jobs.", ["Batch size", "Retry dead letter", "Embedding model version field", "Deduplication hashes"]),
    _rag("retrieval", "Fetch top-k by similarity (+ filters).", "First stage recall matters.", ["top_k tuning", "Score thresholds", "MMR diversity", "Per-tenant namespaces"]),
    _rag("hybrid-search", "Blend **keyword + vector** scores.", "Enterprise docs need exact tokens (SKUs, clauses).", ["BM25", "RRF fusion", "Weight tuning", "Elasticsearch/OpenSearch + vector"]),
    _rag("reranking", "Second-stage **cross-encoder** or LLM scores pairs.", "Improves precision@5 for hard queries.", ["Latency cost", "Cascade: cheap retrieve → expensive rerank", "Batch rerank"]),
    _rag("metadata-filtering", "Restrict search by **tenant, product, date, ACL**.", "Prevent cross-customer leakage.", ["Payload indexes", "SQL WHERE + vector", "Sync ACL from source"]),
    _rag("query-rewriting", "Transform user query before search.", "Users ask vaguely; indexes need better queries.", ["HyDE hypothetical doc", "Step-back", "Multi-query", "LLM rewrite risks injection"]),
    _rag("contextual-retrieval", "Prepend **chunk-specific context** before embedding (Anthropic-style idea).", "Disambiguate chunks that lack section headers.", ["Offline context generation", "Storage cost", "Re-embed on change"]),
    _rag("multimodal-rag", "Retrieve **images/audio** with text.", "Manuals with diagrams need vision embeddings.", ["CLIP-class models", "Captioning pipeline", "Higher storage/compute"]),
    _rag("graph-rag", "Use **knowledge graph** for multi-hop reasoning.", "When entities and relations matter.", ["Community summaries", "Graph traversal + text", "Sync graph with docs"]),
    _rag("rag-evaluation", "Measure **retrieval and generation** separately.", "Know which stage regressed.", ["MRR, nDCG", "Faithfulness", "Answer relevance", "LLM-as-judge risks"]),
    _rag("rag-failure-modes", "Catalog **what breaks RAG** in prod.", "Ops runbooks need named failures.", ["Stale index", "Bad chunk", "Wrong tenant filter", "Empty retrieval hallucination", "Injection in doc"]),
    _rag(
        "production-rag",
        "RAG as a **managed service**: SLAs, reindex, monitoring.",
        "Pilot ≠ production without freshness and ACL.",
        ["Incremental index", "Blue/green index swap", "Cache hot queries", "Cost caps", "Human feedback loop"],
    ),
]
CONTENT["06-rag"] = {k: v for k, v in _rag_entries}

# --- 07 Agents ---
_agent_slugs = [
    ("agent-fundamentals", "An **agent** loops: model → optional tool → observation until stop.", "Automate multi-step tasks with guardrails."),
    ("tool-calling", "Tools are **typed functions** the runtime executes.", "Connect LLM to real systems safely."),
    ("planning", "Decide **sequence of steps** before or during execution.", "Reduce random tool thrashing."),
    ("memory", "Persist **facts across turns** (summary, vector, SQL).", "Long conversations exceed context."),
    ("state-machines", "Explicit **states and transitions** beat free-form loops for risk.", "Regulated workflows want determinism."),
    ("agent-loops", "while not done: model step → tools → check budget.", "Core control flow you implement."),
    ("reflection", "Model **critiques** draft before final answer.", "Quality up, cost up."),
    ("multi-agent-systems", "Multiple roles (planner, worker, critic).", "Complex tasks; orchestration overhead."),
    ("human-in-the-loop", "Human **approves** high-risk actions.", "Required for prod ops agents."),
    ("agent-evaluation", "Task success rate, steps, cost per task.", "Agents regress silently."),
    ("agent-security", "Tool abuse and injection via observations.", "Agents are privileged code paths."),
    ("production-agents", "Budgets, audit logs, idempotency, sandboxes.", "Demo agent ≠ SRE-approved."),
]
CONTENT["07-agents"] = {
    slug: _t(
        mental,
        f"Production AI needs **{titleize(slug)}** with clear contracts.",
        [
            f"Design {titleize(slug)} with max steps and timeouts",
            "Log every tool call with args hash",
            "Separate planning from execution for critical domains",
            "Compare workflow engine vs LLM agent",
            "Eval on scenario suites",
        ],
        example="Ops agent: read-only K8s tools by default; write needs approval.",
    )
    for slug, mental, why in _agent_slugs
}

# --- 08 MCP ---
CONTENT["08-mcp"] = {
    slug: _t(
        f"MCP **{titleize(slug)}** standardizes how clients discover capabilities.",
        "Portable tools across IDEs and agents—like USB-C for AI integrations.",
        [
            "JSON-RPC messages",
            "Capability negotiation",
            "stdio vs SSE transport",
            "Auth for remote servers",
            "Audit tool invocations",
        ],
    )
    for slug in [
        "mcp-fundamentals",
        "architecture",
        "tools",
        "resources",
        "prompts",
        "transport",
        "security",
        "build-mcp-server",
    ]
}

# --- 09 Frameworks ---
CONTENT["09-ai-frameworks"] = {
    name: _t(
        f"**{titleize(name)}** orchestrates LLM apps with abstractions.",
        "Speed development after you understand raw HTTP + loops.",
        [
            "Chain/graph abstractions",
            "Callback hooks for tracing",
            "Vendor lock-in risk",
            "Debug complexity",
            "When to drop to minimal code",
        ],
        pitfalls=["Hiding retries and token usage", "Framework upgrade breaks prod"],
    )
    for name in ["langchain", "langgraph", "llamaindex", "dspy", "framework-tradeoffs"]
}

# --- 10 Evaluation ---
CONTENT["10-evaluation"] = {
    slug: _t(
        "Evaluation is how you **trust** changes to prompts, models, and retrieval.",
        "Without eval, AI prod is guesswork.",
        [
            "Golden datasets versioned in git",
            "Offline CI gates",
            "Online A/B with guardrails",
            "Slice metrics (locale, tenant)",
            "Human review sampling",
        ],
    )
    for slug in [
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
    ]
}

# --- 11 Fine-tuning ---
CONTENT["11-fine-tuning"] = {
    "prompting-vs-rag-vs-finetuning": _t(
        "Three levers: **context**, **index**, **weights**—different cost and freshness profiles.",
        "Prevents wrong 'just fine-tune the PDFs' projects.",
        ["Prompt = instant", "RAG = fresh docs", "FT = behavior/format", "Continued pretrain = rare", "Combine often"],
    ),
    "supervised-finetuning": _t("SFT on **input→output** pairs.", "Teach format and task.", ["Mask labels", "Data quality > quantity", "Holdout eval"]),
    "lora": _t("Low-rank adapters **ΔW=BA**.", "Cheap FT.", ["Rank r", "Target modules", "Merge weights optional"]),
    "qlora": _t("LoRA + **quantized base**.", "FT on single GPU.", ["4-bit base", "NF4", "VRAM savings"]),
    "adapters": _t("Small modules inserted in layers.", "Swap adapters per tenant.", ["Adapter hub", "Serving complexity"]),
    "datasets": _t("JSONL chat or instruction rows.", "Garbage data → garbage model.", ["PII scrubbing", "Dedup", "License"]),
    "training-loop": _t("Standard PyTorch/HF Trainer.", "You monitor loss + val.", ["Checkpointing", "Gradient accumulation"]),
    "evaluation": _t("Same metrics as product.", "FT is not done at low loss.", ["Regression on general tasks"]),
    "when-to-finetune": _t("When prompts+RAG plateau on **style/reliability**.", "Not for weekly doc updates.", ["Maintenance cost", "Catastrophic forgetting"]),
}

# --- 12 Model serving ---
CONTENT["12-model-serving"] = {
    "inference-fundamentals": _t(
        "Inference serves **frozen graphs** under latency and throughput SLOs.",
        "Product UX and COGS depend on this layer.",
        ["Prefill vs decode", "Batching", "Quantization", "Streaming", "SLA tiers"],
    ),
    "batching": _t("Group requests for **GPU utilization**.", "Static batch waits; dynamic batching helps.", ["Max batch size", "Padding waste", "Latency tail"]),
    "continuous-batching": _t("Add/remove sequences **between decode steps**.", "vLLM core idea.", ["Iteration-level scheduling", "Fairness"]),
    "kv-cache": _t("Cache K/V for prior tokens.", "Decode memory dominant.", ["PagedAttention", "Max seq × batch"]),
    "quantization": _t("Lower precision weights.", "INT8/INT4/FP8 trade quality.", ["GPTQ/AWQ", "Per-model eval"]),
    "speculative-decoding": _t("Draft model proposes; target verifies.", "Latency win on some hardware.", ["Draft size", "Acceptance rate"]),
    "streaming": _t("Emit tokens as generated.", "SSE/WebSocket UX.", ["Time to first token", "Backpressure"]),
    "vllm": _t("Popular **OSS serving** with PagedAttention.", "Self-host LLMs on K8s.", ["OpenAI compatible server", "tensor parallel"]),
    "triton": _t("NVIDIA **multi-framework** server.", "Custom models + ensembles.", ["Model repository", "Dynamic batching"]),
    "kserve": _t("K8s **CRDs** for model serving.", "Standard for K8s ML platforms.", ["Serverless vs raw Deployment", "Rollouts"]),
    "model-gateway": _t("Policy in front of runtimes.", "Auth, route, meter.", ["Same as AI gateway pattern"]),
}

# --- 13 GPU ---
CONTENT["13-gpu-and-accelerator-infrastructure"] = {
    slug: _t(
        f"**{titleize(slug)}** for inference clusters.",
        "Infra engineers must speak GPU, not only pods.",
        [
            "VRAM capacity planning",
            "Memory bandwidth vs FLOPs",
            "nvidia-smi diagnostics",
            "Multi-GPU topology",
            "CUDA driver + container toolkit",
        ],
    )
    for slug in [
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
    ]
}

# --- 14 K8s ---
CONTENT["14-kubernetes-for-ai"] = {
    slug: _t(
        f"Kubernetes **{titleize(slug)}** for AI workloads (not pod basics).",
        "You already know K8s—extend to GPUs and autoscaling inference.",
        [
            "Device plugin exposes GPUs",
            "Resource requests limits scheduling",
            "Taints for GPU-only nodes",
            "HPA/KEDA signals",
            "KServe/Ray patterns",
        ],
        bridge="Helm + Terraform for node pools; Prometheus for GPU metrics.",
    )
    for slug in [
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
    ]
}

# --- 15 Platform ---
CONTENT["15-ai-platform-engineering"] = {
    slug: _t(
        f"Platform component: **{titleize(slug)}**.",
        "Internal AI platform teams ship self-service primitives.",
        [
            "Developer portal / API",
            "Governance and audit",
            "Cost chargeback",
            "Safe defaults",
            "Golden paths not wild west keys",
        ],
        bridge="Your Go/K8s background is the core skill here.",
    )
    for slug in [
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
    ]
}

# --- 16 Infra ---
CONTENT["16-ai-infrastructure"] = {
    "capacity-planning": _t(
        "Translate **QPS × tokens × model size** into GPU count and spend.",
        "Staff infra interviews live here.",
        [
            "Peak factor over average",
            "Prefill vs decode duty cycle",
            "KV memory per session",
            "Network for tensor parallel",
            "Cold start buffer",
        ],
        example="10M req/day × 2k tokens → rough GPU-hours; compare API $ vs self-host.",
    ),
}
for slug in [
    "reference-architecture",
    "inference-clusters",
    "model-deployment",
    "distributed-inference",
    "storage",
    "networking",
    "caching",
    "reliability",
    "disaster-recovery",
]:
    if slug not in CONTENT["16-ai-infrastructure"]:
        CONTENT["16-ai-infrastructure"][slug] = _t(
            f"Infrastructure topic **{titleize(slug)}** for AI at scale.",
            "Connect models to reliable cloud/K8s footprint.",
            ["HA patterns", "Multi-AZ", "Object storage for weights", "CDN not for LLM", "Runbooks"],
        )

# --- 17–24 (compact module-level richness; per-slug via loop) ---
for module, slugs in {
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
}.items():
    CONTENT[module] = {
        slug: _t(
            f"Study focus: **{titleize(slug)}** ({module}).",
            "Interview and production readiness for senior/staff loops.",
            [
                "Know trade-offs, not buzzwords",
                "Tie to metrics and cost",
                "Reference one personal project story",
                "Compare build vs buy",
                "Security and tenancy always",
            ],
            practice=f"Write 10 bullet answers for {titleize(slug)}; do one timed 35-min system design if in module 21.",
        )
        for slug in slugs
    }
