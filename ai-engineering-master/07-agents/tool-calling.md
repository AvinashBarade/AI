# Tool Calling

Tools are **typed RPCs** the model may invoke. Your runtime validates names and JSON args against schemas before execution.

## Contract

```json
{"name": "get_pod_logs", "arguments": {"namespace": "prod", "pod": "api-7f8"}}
```

Implement in Go with strict allowlists; never `exec` arbitrary shell from model text.

## Idempotency & side effects

Reads: retry freely. Writes: idempotency keys + human gate for destructive ops.

## Observability

Log `tool_name`, latency, success, and redacted args on every call—first pivot in agent incident response.
