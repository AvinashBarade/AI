# State Machines for Agents

Model agents as **finite states**: `gathering_context`, `awaiting_approval`, `executing`, `terminal`.

Edges are events (tool success, user confirm, timeout). LLM transitions are suggestions; **code** owns legal transitions.

## Why Go engineers like this

Same discipline as payment or provisioning workflows—explicit invariants beat prompt pleading.
