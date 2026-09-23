# Production RAG

Pilot checklist vs prod:

- Incremental indexing + deletion sync
- Blue/green index swap
- Query caching (semantic cache optional)
- Rate limits per tenant
- DR: rebuild index from source of truth
- On-call runbooks for “index lag” and “embedding provider down”

SLA example: 95% of docs reflected in index within 15 minutes of source change.

Capstone architecture belongs in `22-projects/03-production-rag`.
