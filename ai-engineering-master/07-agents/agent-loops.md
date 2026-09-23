# Agent Loops

The loop is where cost and risk accumulate. Each iteration = another completion + possible tool fan-out.

## Parallel tools

When the API allows parallel tool calls, bound concurrency—10 simultaneous K8s API calls can trigger rate limits.

## Stop conditions

Answer quality threshold, empty tool list, user `/stop`, or budget exceeded.

## Testing

Record golden trajectories (messages + tool mocks) in CI; diff when prompt or tool schema changes.
