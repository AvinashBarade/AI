# pgvector

**pgvector** keeps vectors beside relational data in PostgreSQL—ideal when you already run Postgres for tenancy, ACLs, and transactions.

## Strengths

- JOIN metadata filters with `<->` / `<=>` operators in one query.
- Familiar backup, replication, row-level security patterns.

## Limits

Massive billion-scale corpora or ultra-low latency ANN at huge QPS may outgrow Postgres—shard or move hot path to dedicated vector DB.

## Ops snippet mental model

```sql
CREATE INDEX ON chunks USING hnsw (embedding vector_cosine_ops);
-- still filter: WHERE tenant_id = $1
```

Monitor index bloat and autovacuum after heavy upserts.
