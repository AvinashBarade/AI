# Project 01 — LLM Chat API

**Unlock:** After `02-llm-fundamentals` + `03-llm-apis` (see [ROADMAP.md](../../ROADMAP.md)).

## Goal

Production-style chat API: **FastAPI**, streaming, history, structured output, tool calling, token counting, structured logging.

## Stack

Python 3.11+, FastAPI, Pydantic v2, httpx (or official SDK), optional OpenTelemetry.

## Acceptance criteria

- [ ] `POST /v1/chat` with SSE streaming
- [ ] Conversation persistence (Postgres or Redis)
- [ ] JSON schema / Pydantic structured responses
- [ ] Tool definitions + execution loop (bounded steps)
- [ ] Token usage per request in logs + metrics
- [ ] Health + readiness probes

## BUILD_LOG

Copy [BUILD_LOG.md](../../BUILD_LOG.md) template to `./BUILD_LOG.md` when you start.
