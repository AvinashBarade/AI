# Concept knowledge base for study material generation.
from __future__ import annotations

import re
from typing import Any

def titleize(slug: str) -> str:
    return slug.replace("-", " ").title()


MODULE_BLURB: dict[str, str] = {
    "00-foundations": "AI and ML foundations for engineering judgment",
    "01-python-for-ai-engineering": "Python as the AI ecosystem glue language",
    "02-llm-fundamentals": "decoder large language models",
    "03-llm-apis": "provider integration and routing",
    "04-prompt-engineering": "behavior control at the prompt layer",
    "05-embeddings-and-vector-search": "semantic search and vector indexes",
    "06-rag": "retrieval-augmented generation systems",
    "07-agents": "LLM-driven tool loops and orchestration",
    "08-mcp": "Model Context Protocol tool surfaces",
    "09-ai-frameworks": "orchestration frameworks atop primitives",
    "10-evaluation": "measurement and quality gates",
    "11-fine-tuning": "weight adaptation and ML lifecycle",
    "12-model-serving": "high-throughput LLM inference",
    "13-gpu-and-accelerator-infrastructure": "GPU hardware and parallelism",
    "14-kubernetes-for-ai": "Kubernetes patterns for AI workloads",
    "15-ai-platform-engineering": "internal AI platform control planes",
    "16-ai-infrastructure": "clusters, capacity, and reliability",
    "17-observability": "signals for AI systems",
    "18-ai-security": "threats and controls for GenAI",
    "19-production-ai": "SRE patterns for stochastic services",
    "20-fde-engineering": "customer-facing solution delivery",
    "21-system-design": "staff-level architecture problems",
    "23-interview-preparation": "interview mastery by domain",
    "24-research": "landscape and papers for engineers",
}


RELATED: dict[str, list[str]] = {
    "02-llm-fundamentals": [
        "tokens", "tokenization", "embeddings", "attention", "transformers", "inference",
    ],
    "06-rag": [
        "rag-fundamentals", "chunking", "hybrid-search", "reranking", "rag-evaluation",
    ],
    "12-model-serving": [
        "kv-cache", "continuous-batching", "quantization", "vllm",
    ],
}


HAND: dict[str, dict[str, Any]] = {
    "02-llm-fundamentals/tokens": {
        "concepts": [
            "A **token** is an integer ID from a fixed vocabulary produced by a tokenizer—not a word.",
            "Billing, context limits, and rate limits are enforced in **tokens**, not characters.",
            "Subword tokenization (BPE, SentencePiece) balances vocabulary size vs sequence length.",
            "Rare strings may explode into many tokens → cost and latency surprises.",
            "The model never sees raw UTF-8; it sees token IDs → embeddings.",
            "Tokenizer **must** match the model checkpoint (train/serve skew breaks generation).",
            "Prompt caching and prefix reuse are token-aligned in many providers.",
            "Token counts differ across models for the same English sentence.",
            "Special tokens mark roles (system/user/assistant) in chat templates.",
            "For platform engineers: tokenization is the metering boundary.",
        ],
        "mental": "Imagine LEGO bricks from a catalog: text is snapped into brick IDs. The transformer stacks bricks, not letters.",
        "internal": "Tokenizer.encode(text) → List[int]. Embedding matrix E[vocab, d] maps IDs to vectors. Loss is computed per token.",
        "example": "The phrase `Kubernetes` might be one token or several depending on model—always measure with the official tokenizer.",
        "impl": "Use `tiktoken` or Hugging Face `AutoTokenizer` in Python; in Go gateways, call tokenizer service or trust provider token counts from API response headers.",
    },
    "06-rag/chunking": {
        "concepts": [
            "**Chunking** splits documents into retrieval units; it is the highest-leverage RAG hyperparameter.",
            "Too small → lost context; too large → noise and wasted prompt tokens.",
            "Structure-aware chunking respects headings, tables, and code blocks.",
            "Overlap reduces boundary artifacts where answers span two chunks.",
            "Chunk metadata (title, section, page) powers filtering and citations.",
            "Chunk size interacts with embedding model max length.",
            "Parent-child chunks retrieve small pieces but inject parent context.",
            "Legal/medical domains often need sentence-bounded chunks for citations.",
            "Chunking is **not** training—it is index design.",
            "Re-chunking requires re-embedding and index rebuild or incremental pipeline.",
        ],
        "mental": "You are cutting a textbook into index cards. Search finds cards; the LLM reads only the cards you deal.",
        "internal": "Parser → segmenter → optional enricher → embedder → vector upsert with stable chunk IDs.",
        "example": "HR policy: chunk by section 4.1, 4.2 with 128-token overlap; store `section_id` for ACL.",
        "impl": "Use LlamaIndex/LangChain splitters for speed; own splitter when you need domain rules in Go/Python workers.",
    },
    "12-model-serving/kv-cache": {
        "concepts": [
            "**KV cache** stores attention keys/values for prior tokens during autoregressive decode.",
            "Without KV cache, each new token would re-attend over the full prefix at O(n²) waste.",
            "Cache memory grows with layers × batch × sequence × head dimension.",
            "Prefill phase fills cache for the prompt; decode appends one token per step.",
            "PagedAttention maps logical KV to non-contiguous GPU blocks (vLLM).",
            "Long context + large batch is the primary OOM driver in serving.",
            "GQA/MQA reduce KV footprint vs full multi-head storage.",
            "Quantized KV (where supported) trades quality for capacity.",
            "max_model_len and max_num_seqs are serving knobs tied to KV.",
            "Platform SLOs must separate prefill-bound vs decode-bound workloads.",
        ],
        "mental": "Sticky notes on every layer for each past token so decode only computes the new token's query against cached K/V.",
        "internal": "Per layer: cache tensors shaped roughly [batch, heads, seq, head_dim] for K and V.",
        "example": "8k prompt + 1k output on a 70B-class model can exceed 80GB without quant and paging.",
        "impl": "Tune vLLM `--gpu-memory-utilization`, `max_num_seqs`; monitor `nvidia-smi` reserved memory.",
    },
    "07-agents/agent-fundamentals": {
        "concepts": [
            "An **agent** is a loop: model proposes actions → runtime executes tools → results feed back.",
            "Agents trade determinism for flexibility—guardrails are mandatory.",
            "Bound steps, time, and cost budgets to prevent runaway loops.",
            "Tools are typed RPCs with schema validation and authorization.",
            "Memory spans thread state, summaries, and external stores—each with consistency trade-offs.",
            "Planning can be explicit (plan-and-execute) or implicit in model text.",
            "Evaluation must cover tool selection accuracy, not only final answer text.",
            "Prefer **workflows** when steps are fixed and compliance needs auditability.",
            "Human-in-the-loop gates irreversible or high-risk operations.",
            "Observability: log every tool call with inputs/outputs (redacted).",
        ],
        "mental": "An intern with a phone book of APIs—your code is the manager setting policy.",
        "internal": "while not done: completion with tools → parse tool_calls → execute → append tool messages → repeat.",
        "example": "Ops agent: read-only K8s + metrics first; write operations require approval ticket ID.",
        "impl": "Start with a raw loop in Python; move hot paths to Go workers for platform scale.",
    },
    "15-ai-platform-engineering/ai-gateway": {
        "concepts": [
            "An **AI gateway** centralizes auth, quotas, routing, observability, and cost for all model traffic.",
            "It is the control plane analogue of an API gateway—not the model itself.",
            "Token-aware rate limiting differs from HTTP request rate limiting.",
            "Model routing can be policy-based: cost, latency, capability, data residency.",
            "Circuit breakers isolate failing providers; retries need idempotency keys.",
            "Prompt/response logging requires PII redaction and retention policy.",
            "Streaming responses must propagate backpressure and client disconnects.",
            "Caches (semantic, exact) live behind the gateway with tenant scoping.",
            "Every team should not hold provider API keys—gateway issues scoped credentials.",
            "Go is a strong fit for connection pooling, low latency, and policy plugins.",
        ],
        "mental": "Air traffic control for models: who may fly, which runway, fuel accounting, divert storms.",
        "internal": "Client → authN/Z → quota check → route table → upstream provider → meter tokens → trace.",
        "example": "Route internal docs Q&A to cheap model; code generation to frontier model if policy allows.",
        "impl": "Go middleware chain: JWT, tenant, limiter, httputil reverse proxy to OpenAI-compatible backends.",
    },
}


def _slug_hints(slug: str) -> list[str]:
    hints: list[str] = []
    table = {
        "gpu": "GPU execution, VRAM, and kernel launch overhead dominate serving SLOs.",
        "cuda": "CUDA is NVIDIA's programming model mapping ops to thousands of parallel threads.",
        "kubernetes": "Schedulers, device plugins, and autoscaling extend your existing K8s mental model.",
        "prometheus": "Pull metrics with labels for model_id, tenant_id, and route—avoid high-cardinality prompts.",
        "rag": "Retrieval quality ceilings answer quality; measure retrieval and generation separately.",
        "embedding": "Embeddings map text to vectors; similarity is geometry, not keyword match.",
        "quant": "Quantization reduces precision of weights/activations to save memory and increase throughput.",
        "batch": "Batching improves GPU utilization by amortizing kernel launch and matrix math.",
        "security": "Assume attacker controls prompts, documents, and tool outputs unless proven otherwise.",
        "eval": "Offline eval gates releases; online eval detects drift when labels are sparse.",
        "lora": "LoRA trains low-rank adapters while freezing base weights—efficient specialization.",
        "mcp": "MCP standardizes how clients discover tools, resources, and prompts from servers.",
        "fde": "FDE work spans discovery, integration, production debugging, and stakeholder communication.",
        "tenant": "Multi-tenant AI requires isolation for data, keys, indexes, quotas, and audit logs.",
        "trace": "Distributed traces should span gateway → retrieval → model with shared trace_id.",
        "hybrid": "Hybrid retrieval combines sparse lexical (BM25) with dense vectors for robust recall.",
        "injection": "Injection attacks merge untrusted content with instructions—separate channels and validate outputs.",
    }
    s = slug.lower()
    for k, v in table.items():
        if k in s:
            hints.append(v)
    return hints


def expand(module: str, slug: str) -> dict[str, Any]:
    key = f"{module}/{slug}"
    if key in HAND:
        return HAND[key]

    title = titleize(slug)
    blurb = MODULE_BLURB.get(module, "modern AI systems")
    hints = _slug_hints(slug)

    concepts = [
        f"**{title}** is a core concept in {blurb}.",
        f"Engineering {title.lower()} means defining inputs, outputs, invariants, and failure boundaries—not only calling an API.",
        f"Connect {title.lower()} to metrics: latency, quality, cost, and security for your tenant.",
        f"In production, {title.lower()} must be versioned, observable, and testable in CI where possible.",
    ]
    concepts += hints[:6]
    while len(concepts) < 10:
        concepts.append(
            f"Staff engineers document trade-offs for {title.lower()} before choosing build vs buy."
        )
        if len(concepts) >= 10:
            break

    return {
        "concepts": concepts[:12],
        "mental": f"Visualize {title} as a box in the pipeline with clear upstream/downstream contracts inside {blurb}.",
        "internal": f"Decompose {title.lower()} into: validate → execute core logic → emit result + telemetry.",
        "example": f"Enterprise assistant: {title.lower()} fails when teams skip eval and operate only on demo prompts.",
        "impl": "Python for model/RAG paths; Go for gateways, workers, and policy-heavy services.",
    }


def get(module: str, slug: str) -> dict[str, Any]:
    base = expand(module, slug)
    title = titleize(slug)
    base.setdefault(
        "architecture",
        f"""```text
  Upstream (data / user / scheduler)
           │
           ▼
    ┌──────────────────┐
    │  {title:<18}│
    └────────┬─────────┘
             ▼
  Downstream (model / index / tool / metrics)
```""",
    )
    base.setdefault(
        "flow",
        "1. Authenticate and resolve tenant context\n"
        "2. Validate inputs against schema and policy\n"
        f"3. Apply {title.lower()} with timeouts\n"
        "4. Record tokens, latency phases, and quality signals\n"
        "5. Return response with trace correlation ID",
    )
    return base


def related_links(module: str, slug: str) -> str:
    slugs = RELATED.get(module, [])
    if not slugs:
        return f"- Other topics in `{module}/`"
    lines = []
    for s in slugs:
        if s == slug:
            continue
        lines.append(f"- [{titleize(s)}](./{s}.md)")
    return "\n".join(lines[:6]) if lines else f"- Browse `{module}/`"
