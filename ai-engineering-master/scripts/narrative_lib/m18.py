# 18-ai-security

NARRATIVES = {
    "threat-model": """# AI Threat Model

STRIDE on LLM systems: prompt injection, tool abuse, data exfil via retrieval, model supply chain, denial of wallet.

Document trust boundaries: user, docs, tools, model provider.
""",
    "prompt-injection": """# Prompt Injection (Security Module)

Same class as module 04—here emphasize **enterprise controls**: DLP on outputs, segregated agents, monitoring for exfil patterns.

Red team quarterly; log policy violations.
""",
    "jailbreaks": """# Jailbreaks

User attempts to bypass safety—multi-turn, encoding tricks, roleplay.

Defense in depth: input filters (weak alone), output filters, tool restrictions, human review for sensitive actions—not one magic system prompt.
""",
    "data-leakage": """# Data Leakage

Training data memorization, cross-tenant retrieval, logs storing PII prompts.

Minimize retention; encrypt; access controls on trace stores.
""",
    "rag-poisoning": """# RAG Poisoning

Attacker uploads docs instructing model to leak secrets or mislead.

Scan ingestion; provenance; admin-only write paths; anomaly detection on new docs.
""",
    "agent-security": """# Agent Security (Module 18)

Tool graphs are attack surface—same as module 07 with audit/compliance framing.

SOC2: prove who can invoke which tool under which policy version.
""",
    "tool-security": """# Tool Security

Validate args; no shell; parameterized SQL; scoped OAuth tokens per tenant.

Network policies from tool runner to only required endpoints.
""",
    "model-security": """# Model Security

Pick vetted weights; scan containers; air-gap option for classified workloads.

Monitor for adversarial inputs causing misclassification in safety classifiers.
""",
    "pii": """# PII in AI Systems

Detect/redact before model call where required; regional processing; DSR deletion includes vector indexes and logs.

Models may still infer—don't treat LLM as anonymizer.
""",
    "secrets": """# Secrets (AI Security)

Secrets in RAG docs are a data problem; secrets in prompts are an ops problem.

Automated secret scanning on ingestion and on outbound tool payloads.
""",
    "ai-supply-chain": """# AI Supply Chain

HF models, Python deps, MCP servers, LoRA adapters—SBOM and signature verification.

Pin hashes; block `pip install` at runtime in prod images.
""",
}
