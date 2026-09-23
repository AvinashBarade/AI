# MCP Architecture

```text
Host process
  └── MCP Client(s)  --stdio or HTTP+SSE--
        └── MCP Server (subprocess or remote)
              └── Your systems (DB, APIs)
```

Servers should be **stateless** where possible; session state lives in host or backing store.

## Deployment

Sidecar in K8s vs centralized gateway MCP—trade isolation vs ops count.
