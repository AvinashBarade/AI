# OpenAI-Compatible APIs

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
