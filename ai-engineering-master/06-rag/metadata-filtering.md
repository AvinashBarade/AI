# Metadata Filtering

Vectors without filters are a **data leak** waiting to happen in multi-tenant systems.

Filter on: `tenant_id`, `product`, `doc_class`, `effective_date`, `clearance_level`.

SQL + pgvector example mental model:

```sql
SELECT id, embedding <-> query_vec AS dist
FROM chunks
WHERE tenant_id = $1 AND effective_date <= now()
ORDER BY dist LIMIT 20;
```

Index payload fields in Qdrant/Milvus similarly.
