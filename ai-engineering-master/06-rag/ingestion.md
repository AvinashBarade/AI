# RAG Ingestion

Ingestion is everything that happens **before** a user asks a question: connectors, ACL sync, parsing, chunking, embedding, upsert.

Treat it as a **data pipeline** with backpressure—not a one-off script.

## Connectors

SharePoint, S3, Confluence, tickets—each has auth, rate limits, and deletion events. You need **incremental** sync: only reprocess changed objects.

## ACL is not optional

If a user can’t read a doc in source system, they must not retrieve it in RAG. Propagate permissions to vector payload fields and filter every query.

## Poisoning awareness

Malicious or compromised documents are **untrusted input** to the model—same class as prompt injection via user chat.
