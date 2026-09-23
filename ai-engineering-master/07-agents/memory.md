# Agent Memory

Memory spans **short** (conversation buffer), **working** (scratch in state), and **long** (vector store / DB).

## Context window is not memory

Summarize or retrieve selectively; stuffing full history causes lost-in-the-middle failures.

## Write policy

Not every turn should embed into long-term memory—PII and stale facts poison future sessions.

## Tenant isolation

Memory keys must include `tenant_id`; shared global memory is a liability.
