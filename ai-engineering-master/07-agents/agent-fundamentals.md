# Agent Fundamentals

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
