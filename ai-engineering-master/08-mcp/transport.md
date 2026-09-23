# MCP Transport

Common modes: **stdio** (local subprocess) and **HTTP with SSE** (remote services).

Remote needs TLS, auth (OAuth/mTLS), and idle timeouts—stdio is not magically safer if server runs arbitrary code on laptop.
