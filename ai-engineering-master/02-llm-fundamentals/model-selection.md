# Model Selection

Choosing a model is a **capacity, cost, compliance, and quality** decision—not a leaderboard contest.

## Dimensions

| Question | Why it matters |
|----------|----------------|
| Context length needed? | Long docs vs chat |
| Latency SLO? | Small model or regional edge |
| Data residency? | Azure OpenAI vs US-only API |
| Tool calling quality? | Agent reliability |
| Open weights required? | Self-host vLLM |

## Process

1. Build golden eval (100–500 tasks).
2. Run candidates with fixed prompts/RAG.
3. Measure quality, P95 latency, $/success.
4. Route easy traffic to cheap model; escalate hard cases.

## Gateway pattern (Go)

```text
if complexity_score < t: route small
elif needs_tools: route tool-strong
else: route large
```

Document escalation rules—interviewers love explicit economics.
