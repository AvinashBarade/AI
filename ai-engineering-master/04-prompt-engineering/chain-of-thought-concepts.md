# Chain-of-Thought Concepts

**Chain-of-thought (CoT)** originally meant showing intermediate reasoning steps in the prompt or output. Modern **reasoning models** may internalize multi-step computation—you do not always see or need explicit “think step by step” text.

## Product guidance

Expose **verifiable artifacts**, not hidden scratchpads:

- Tool plans with IDs
- Cited retrieval spans
- Structured `steps[]` in JSON for UI

Do not train your compliance story on storing raw model “thinking” traces unless legal and security sign off.

## Prompting vs architecture

Asking “think step by step” can help smaller models on math-like tasks; for agents, **explicit planning nodes** (LangGraph, state machine) beat prose CoT for auditability.

## Security

CoT in user-visible channels increases leakage of internal reasoning about secrets in context. Redact before logging.
