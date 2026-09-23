# Planning in Agents

Planning decomposes a goal into steps before execution—explicit plan object, DAG, or planner node in LangGraph.

## Plan vs react

| Style | Pros | Cons |
|-------|------|------|
| Up-front plan | Auditable | Wrong plan early |
| ReAct step-by-step | Adaptive | Drift, more tokens |

For regulated workflows, require **human-approved plan** before mutating tools run.

## Replanning

When tool errors, feed structured error back and replan—don't silently retry the same bad call ten times.
