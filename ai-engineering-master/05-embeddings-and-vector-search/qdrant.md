# Qdrant

Qdrant is a **purpose-built vector database** with rich payload filtering, quantization, and horizontal scaling story.

## When teams pick it

Microservices already gRPC/HTTP-native; need strong filter + vector combo; want managed cloud or self-host on K8s.

## Payload design

Store filter fields (`tenant_id`, `doc_id`, `chunk_idx`) in payload; index them. Avoid stuffing huge text blobs in payload if object storage holds originals.

## HA

Run clustered Qdrant with replication; test failover—unlike Postgres, your team may be less practiced on its ops runbooks.
