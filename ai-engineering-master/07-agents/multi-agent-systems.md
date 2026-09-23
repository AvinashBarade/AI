# Multi-Agent Systems

Multiple specialized agents (researcher, coder, reviewer) coordinate via messages or shared blackboard.

## Failure modes

Infinite politeness loops, duplicated work, contradictory conclusions, blameless diffusion of responsibility.

## Pattern that works

**Orchestrator + workers** with clear task IDs and a single writer to external systems.

## Cost

N agents × M turns—finance must see per-workflow attribution.
