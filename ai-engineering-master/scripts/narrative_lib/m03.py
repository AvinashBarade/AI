# 03-llm-apis

NARRATIVES = {
    "openai-compatible-apis": """# OpenAI-Compatible APIs

Most of the ecosystem converged on one HTTP shape: **chat completions** with `messages`, optional `tools`, optional `stream: true`, and a `usage` block in the response.

That lets you point the same client at OpenAI, Azure OpenAI, vLLM, LiteLLM, or local Ollama with a URL swap—if you respect subtle differences in error codes, auth headers, and tool schema support.

## Request skeleton

```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
  ],
  "stream": true,
  "tools": [...]
}
```

## What your wrapper must implement (Go or Python)

- **Timeouts** per attempt and per request
- **Retries** on 429/502 with jitter; respect `Retry-After`
- **Streaming parser** (SSE lines `data: {...}`)
- **Token accounting** from `usage` or stream chunks
- **Redacted logging**—prompts may contain secrets

## Streaming UX

Clients see tokens early (TTFT). Your gateway should not buffer the entire completion before forwarding—backpressure matters for mobile clients.

## Idempotency

For tool side effects, use idempotency keys at the **tool layer**, not assumed from the LLM API.
""",
    "anthropic": """# Anthropic APIs

Anthropic’s Messages API is a first-class alternative in many enterprises. System instructions, tool use, and document blocks have **provider-specific** details—abstract them behind your internal `CompletionRequest` type in the gateway.

Watch for: max output tokens, caching features (where offered), regional endpoints, and enterprise contract routing (Azure/GCP partnerships may change over time—verify current docs when integrating).

Your platform team should store **provider capability matrix** (tools, vision, PDF, context length) per model ID.
""",
    "gemini": """# Gemini / Vertex AI

GCP-native stacks often standardize on **Vertex AI** for Gemini with IAM service accounts, VPC-SC, and CMEK requirements.

Integration pattern: workload identity in GKE → short-lived tokens → Vertex prediction endpoint. Same gateway abstraction as OpenAI; different auth and request JSON.

Multimodal parts (image bytes inline) affect payload size and latency—treat as separate route with stricter size limits.
""",
    "huggingface": """# Hugging Face Ecosystem

HF is three things at once:

1. **Model Hub** — weights, tokenizer, model cards, licenses.
2. **Libraries** — `transformers`, `datasets`, `accelerate`.
3. **Inference** — Inference Endpoints or self-hosted.

For platform engineers, the operational path is: pin revision hash, scan license, build container with `transformers` + vLLM/TGI, deploy on GPU node pool.

Never `from_pretrained` arbitrary community models in prod without security review—pickle and supply-chain risk.
""",
    "ollama": """# Ollama (Local Development)

Ollama is excellent for **developer laptops** and demos: `ollama pull`, OpenAI-compatible local port.

It is not a multi-tenant production platform by itself—you still need auth, quotas, and HA. Use it to prototype prompts; ship through governed gateway + managed inference for prod.
""",
    "model-routing": """# Model Routing

Routing chooses **which model and provider** handle a request.

Inputs to policy:

- Task type (extract vs chat vs code)
- Tenant tier and data residency
- Latency SLO
- Cost budget
- Safety level (refusal strictness)

Implementation in Go at the gateway:

```text
classify(request) → route table → primary + fallback chain
```

Log `route_decision` on every trace for finance and debugging.

Circuit-break provider on error rate; shift traffic to secondary region/model with pre-tested eval parity.
""",
}
