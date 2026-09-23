# Prompting

Prompting is how you **program behavior without recompiling weights**. For a backend engineer, think of it as configuration that is interpreted by a stochastic runtime—except the interpreter hallucinates if your spec is ambiguous.

## A useful decomposition

| Layer | Who owns it | Change frequency |
|-------|-------------|------------------|
| System | Platform / security | Weekly–monthly |
| Developer | Feature team | Per release |
| User | End user | Every message |

Your service should never concatenate these blindly. Build an explicit **message assembly** function with tests.

## Precision beats poetry

Weak: “Be helpful and accurate.”

Strong: “Answer in JSON matching schema X. If context lacks support, return `{"status":"insufficient_evidence"}`. Never invent ticket IDs.”

## Token economics

Long system prompts tax **every** request. Cache stable prefixes where the provider allows; otherwise hoist repeated rules into retrieval or tools.

## Eval loop

Prompt changes are code changes. Run a golden set before merge; track regression on faithfulness and refusal rate—not just “looks fine in Playground.”
