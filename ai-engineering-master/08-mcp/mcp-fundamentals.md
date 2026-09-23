# MCP Fundamentals

**Model Context Protocol** standardizes how hosts discover and invoke **tools**, **resources**, and **prompts** exposed by servers—USB-C for agent integrations.

Host (Cursor, Claude Desktop, your platform) ↔ MCP client ↔ MCP server (Git, Postgres, K8s).

## Why platform teams care

Replace N bespoke SDK wrappers with one protocol—if you enforce auth, logging, and schema versioning on servers.
