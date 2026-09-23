# Production Agents

Ship checklist:

- Max iterations + global timeout
- HITL for writes
- Sandboxed tool runtime
- Per-tenant rate limits
- Trace every LLM and tool span
- Kill switch feature flag

SLO: p95 latency including tools, not LLM-only TTFT.

Capstone: `22-projects/04-ai-agent`.
