# 23-interview-preparation

NARRATIVES = {
    "ai-fundamentals": """# Interview: AI Fundamentals

Expect: supervised vs unsupervised, bias/variance intuition, when DL vs classical ML, eval metrics.

Answer with production framing—not textbook only.
""",
    "llm": """# Interview: LLM Topics

Tokens, context window, fine-tuning vs RAG, inference cost drivers, structured output.

Whiteboard: request path through gateway to vLLM with KV cache mention.
""",
    "rag": """# Interview: RAG

Chunking trade-offs, hybrid search, faithfulness, failure modes, ACL filtering.

Design mini RAG for internal docs with multi-tenant isolation in 25 minutes.
""",
    "agents": """# Interview: Agents

Tool calling, loops, HITL, security, when not to use agents.

Scenario: K8s debugging agent—what tools, what approvals, max steps?
""",
    "mcp": """# Interview: MCP

Explain host/server/tools/resources; compare to bespoke integrations; security concerns.

When would you build MCP vs REST microservice?
""",
    "ai-infrastructure": """# Interview: AI Infrastructure

GPU memory, batching, model deployment, capacity estimation.

Estimate GPUs for 1k RPS given avg tokens—show assumptions.
""",
    "kubernetes-ai": """# Interview: Kubernetes + AI

GPU scheduling, device plugin, KEDA, KServe basics, taints.

Not “what is a Pod”—focus AI-specific ops you've done or designed.
""",
    "system-design": """# Interview: System Design (AI)

Practice full prompts: chat at scale, RAG platform, gateway—always SLI, cost, security.

Time-box: requirements 5m, high-level 10m, deep dive 15m, trade-offs 5m.
""",
    "python": """# Interview: Python for AI

Async FastAPI, Pydantic, typing, when not to use GIL-bound threads for CPU work.

Contrast with Go responsibilities in same architecture.
""",
    "coding": """# Interview: Coding (AI Adjacent)

Implement token bucket, parse SSE stream, simple retriever interface, JSON schema validator.

Clarity and tests beat clever one-liners.
""",
    "behavioral": """# Interview: Behavioral

STAR stories: shipped RAG under deadline, handled model outage, pushed back on unsafe agent scope, taught team eval discipline.

Quantify impact (latency, cost, incident reduction).
""",
    "fde": """# Interview: FDE

Customer conflict, scoping, traveling, wearing multiple hats—show empathy + technical depth.

Example: discovered customer didn't need agents, shipped RAG MVP faster—saved quarter.
""",
}
