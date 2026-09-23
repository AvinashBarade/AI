# Agent Security

Agents combine **prompt injection** with **privilege escalation via tools**.

Mitigations: least-privilege credentials per tenant, schema validation, network egress allowlists, no secrets in prompts, separate read/write tool sets.

Assume compromised user message can steer tool args—validate args against server-side policy, not model intent alone.
