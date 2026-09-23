# Reflection

Reflection asks the model to **critique its draft** and revise—self-consistency without extra human.

Use sparingly in prod: doubles tokens/latency. Better for offline eval or high-stakes single-shot tasks with budget.

## Guard

Reflection must not bypass safety filters or re-read secrets from context into logs.
