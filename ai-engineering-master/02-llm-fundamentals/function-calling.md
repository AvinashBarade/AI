# Function Calling

The model emits a structured **tool call** (name + JSON args). Your runtime validates, authorizes, executes, appends **tool role** message with result, continues generation.

## Loop sketch

```text
user message
→ model (maybe tool_calls)
→ execute tools (parallel if allowed)
→ tool results
→ model final answer
```

## Production requirements

- Tool allowlist per tenant/role
- Timeouts and idempotency keys for side effects
- Audit log: who invoked what with hashed args
- Never execute SQL/shell from raw model strings without human approval in high-risk domains

## vs MCP

Function calling is the **pattern**; MCP standardizes discovery/transport of tools across clients.
