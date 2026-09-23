# 07-agents

NARRATIVES = {
    "agent-fundamentals": """# Agent Fundamentals

An **agent** is a control loop: observe state → decide (often via LLM) → act (tools) → repeat until stop condition.

```text
while not done:
    msg = llm(messages, tools)
    if tool_call: execute(tool); append result
    else: return answer
```

## Not every workflow needs an agent

If steps are fixed, use a **state machine or DAG**. Agents shine when branchy exploration is required—and pay latency, cost, and safety tax.

## Bounded loops

Always cap `max_iterations`, wall-clock timeout, and tool spend per session. Unbounded loops burn budget and exfiltrate data via tool chains.

## State

Persist thread ID, tool results, and human approvals in your DB—not only in model context.
""",
    "tool-calling": """# Tool Calling

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
""",
    "planning": """# Planning in Agents

Planning decomposes a goal into steps before execution—explicit plan object, DAG, or planner node in LangGraph.

## Plan vs react

| Style | Pros | Cons |
|-------|------|------|
| Up-front plan | Auditable | Wrong plan early |
| ReAct step-by-step | Adaptive | Drift, more tokens |

For regulated workflows, require **human-approved plan** before mutating tools run.

## Replanning

When tool errors, feed structured error back and replan—don't silently retry the same bad call ten times.
""",
    "memory": """# Agent Memory

Memory spans **short** (conversation buffer), **working** (scratch in state), and **long** (vector store / DB).

## Context window is not memory

Summarize or retrieve selectively; stuffing full history causes lost-in-the-middle failures.

## Write policy

Not every turn should embed into long-term memory—PII and stale facts poison future sessions.

## Tenant isolation

Memory keys must include `tenant_id`; shared global memory is a liability.
""",
    "state-machines": """# State Machines for Agents

Model agents as **finite states**: `gathering_context`, `awaiting_approval`, `executing`, `terminal`.

Edges are events (tool success, user confirm, timeout). LLM transitions are suggestions; **code** owns legal transitions.

## Why Go engineers like this

Same discipline as payment or provisioning workflows—explicit invariants beat prompt pleading.
""",
    "agent-loops": """# Agent Loops

The loop is where cost and risk accumulate. Each iteration = another completion + possible tool fan-out.

## Parallel tools

When the API allows parallel tool calls, bound concurrency—10 simultaneous K8s API calls can trigger rate limits.

## Stop conditions

Answer quality threshold, empty tool list, user `/stop`, or budget exceeded.

## Testing

Record golden trajectories (messages + tool mocks) in CI; diff when prompt or tool schema changes.
""",
    "reflection": """# Reflection

Reflection asks the model to **critique its draft** and revise—self-consistency without extra human.

Use sparingly in prod: doubles tokens/latency. Better for offline eval or high-stakes single-shot tasks with budget.

## Guard

Reflection must not bypass safety filters or re-read secrets from context into logs.
""",
    "multi-agent-systems": """# Multi-Agent Systems

Multiple specialized agents (researcher, coder, reviewer) coordinate via messages or shared blackboard.

## Failure modes

Infinite politeness loops, duplicated work, contradictory conclusions, blameless diffusion of responsibility.

## Pattern that works

**Orchestrator + workers** with clear task IDs and a single writer to external systems.

## Cost

N agents × M turns—finance must see per-workflow attribution.
""",
    "human-in-the-loop": """# Human-in-the-Loop (HITL)

HITL pauses before irreversible or high-risk actions: deploy, refund, delete namespace, send external email.

## UX

Show proposed action, diff, and rollback plan. Timeout to deny-by-default.

## Compliance

Audit log: who approved, what model proposed, which policy version applied.
""",
    "agent-evaluation": """# Agent Evaluation

Measure **task success** end-to-end, not single-turn BLEU.

- Tool sequence correctness vs golden path
- Side effect safety (no unauthorized calls in sim)
- Steps to completion / cost
- Recovery after injected tool failures

Run in sandbox with mocked tools before touching prod APIs.
""",
    "agent-security": """# Agent Security

Agents combine **prompt injection** with **privilege escalation via tools**.

Mitigations: least-privilege credentials per tenant, schema validation, network egress allowlists, no secrets in prompts, separate read/write tool sets.

Assume compromised user message can steer tool args—validate args against server-side policy, not model intent alone.
""",
    "production-agents": """# Production Agents

Ship checklist:

- Max iterations + global timeout
- HITL for writes
- Sandboxed tool runtime
- Per-tenant rate limits
- Trace every LLM and tool span
- Kill switch feature flag

SLO: p95 latency including tools, not LLM-only TTFT.

Capstone: `22-projects/04-ai-agent`.
""",
}
