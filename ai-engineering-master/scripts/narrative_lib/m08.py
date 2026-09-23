# 08-mcp

NARRATIVES = {
    "mcp-fundamentals": """# MCP Fundamentals

**Model Context Protocol** standardizes how hosts discover and invoke **tools**, **resources**, and **prompts** exposed by servers—USB-C for agent integrations.

Host (Cursor, Claude Desktop, your platform) ↔ MCP client ↔ MCP server (Git, Postgres, K8s).

## Why platform teams care

Replace N bespoke SDK wrappers with one protocol—if you enforce auth, logging, and schema versioning on servers.
""",
    "architecture": """# MCP Architecture

```text
Host process
  └── MCP Client(s)  --stdio or HTTP+SSE--
        └── MCP Server (subprocess or remote)
              └── Your systems (DB, APIs)
```

Servers should be **stateless** where possible; session state lives in host or backing store.

## Deployment

Sidecar in K8s vs centralized gateway MCP—trade isolation vs ops count.
""",
    "tools": """# MCP Tools

Tools mirror function-calling: name, description, JSON schema. Host forwards model-selected calls to server.

## Hardening

Same as agent tools: allowlist, validation, no arbitrary SQL from model—parameterized queries only.
""",
    "resources": """# MCP Resources

Resources expose **readable context** (file URIs, metrics snapshots) without mutating side effects.

Use for grounding; still treat content as untrusted input to the model.
""",
    "prompts": """# MCP Prompts

Servers can ship **templated prompts** (slash commands) with arguments—version alongside server semver.

Centralize dangerous instructions out of user-editable chat where possible.
""",
    "transport": """# MCP Transport

Common modes: **stdio** (local subprocess) and **HTTP with SSE** (remote services).

Remote needs TLS, auth (OAuth/mTLS), and idle timeouts—stdio is not magically safer if server runs arbitrary code on laptop.
""",
    "security": """# MCP Security

Threats: malicious server, compromised host, over-privileged tools, credential theft via resource reads.

Run servers with minimal OS user, secrets from vault, audit every tool invocation, pin server versions in supply chain review.
""",
    "build-mcp-server": """# Build an MCP Server

Start from official SDK (Python/TS). Implement:

1. `list_tools` / `call_tool`
2. Health check for orchestrator
3. Structured logging with correlation ID from host

Project: `22-projects/05-mcp-platform`—Git, K8s, Postgres, Prometheus servers.
""",
}
