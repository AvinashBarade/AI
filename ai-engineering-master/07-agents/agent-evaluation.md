# Agent Evaluation

Measure **task success** end-to-end, not single-turn BLEU.

- Tool sequence correctness vs golden path
- Side effect safety (no unauthorized calls in sim)
- Steps to completion / cost
- Recovery after injected tool failures

Run in sandbox with mocked tools before touching prod APIs.
