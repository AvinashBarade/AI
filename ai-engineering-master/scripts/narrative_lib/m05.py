# 05-embeddings-and-vector-search

NARRATIVES = {
    "embedding-models": """# Embedding Models

An embedding model maps text (or images) to a **dense vector** such that semantic similarity ≈ geometric closeness. RAG, clustering, and dedup all depend on picking and **pinning** a model version.

## Bi-encoders vs cross-encoders

| Type | When | Cost |
|------|------|------|
| Bi-encoder | Index + query embed once | Cheap at scale |
| Cross-encoder | Rerank pairs | Expensive per pair |

Production search is almost always bi-encoder first.

## Model choice axes

- Dimension (768 vs 1536)—higher not always better if index RAM explodes.
- Multilingual vs English-only.
- Domain fit (legal, code)—generic models miss jargon; consider domain-tuned embedders or hybrid BM25.

## Operational rule

Every vector record stores `embedding_model` and `model_revision`. Reindex on change—never mix versions in one logical index.
""",
    "similarity": """# Similarity in Vector Search

“Similar” is a **design choice**, not a universal truth. You define it via embedding geometry plus optional metadata filters.

## What similarity is not

Lexical match (“error 0x803”) may be **dissimilar** in cosine space while paraphrases cluster tightly. Hybrid search exists because pure dense similarity alone fails SKU/code queries.

## Score interpretation

Distance metrics are not calibrated probabilities. A score of 0.82 today may mean nothing after re-embedding. Use **relative rank** and threshold tuning on labeled queries.

## Eval

Build a query set with expected relevant doc IDs. Plot recall@k vs threshold before shipping “I don’t know” logic.
""",
    "cosine-similarity": """# Cosine Similarity

Cosine similarity measures the angle between vectors, ignoring magnitude when vectors are L2-normalized—standard for text embeddings.

\\[
\\text{sim}(a,b) = \\frac{a \\cdot b}{\\|a\\| \\|b\\|}
\\]

Many APIs return **cosine distance** = 1 − sim; know which your DB exposes.

## Normalization

If embeddings are not normalized, dot product and cosine diverge—verify model card defaults.

## ANN indexes

Approximate nearest neighbor (HNSW, IVF) trades recall for speed. Tune `ef_search` / `nprobe` on your eval set; wrong settings look like “search broke” after scale-up.
""",
    "vector-indexes": """# Vector Indexes

Brute-force k-NN is O(n)—fine for thousands, fatal for billions. **ANN indexes** partition space for sublinear search.

## Families

- **HNSW** — graph-based, low latency, RAM-heavy.
- **IVF** — inverted lists + coarse quantizer; needs training on representative vectors.
- **PQ/OPQ** — compress vectors; faster, lower recall.

## Rebuild vs update

Some indexes tolerate incremental insert; others need periodic rebuild. Plan **blue/green** index swap for major parameter or model changes.

## Capacity planning

RAM ≈ vectors × dim × 4 bytes (float32) plus graph overhead—back-of-envelope before you promise multi-tenant SaaS on one node.
""",
    "pgvector": """# pgvector

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
""",
    "qdrant": """# Qdrant

Qdrant is a **purpose-built vector database** with rich payload filtering, quantization, and horizontal scaling story.

## When teams pick it

Microservices already gRPC/HTTP-native; need strong filter + vector combo; want managed cloud or self-host on K8s.

## Payload design

Store filter fields (`tenant_id`, `doc_id`, `chunk_idx`) in payload; index them. Avoid stuffing huge text blobs in payload if object storage holds originals.

## HA

Run clustered Qdrant with replication; test failover—unlike Postgres, your team may be less practiced on its ops runbooks.
""",
    "milvus": """# Milvus

Milvus targets **large-scale** vector workloads with distributed components (query node, data node, etcd/minio dependencies in clustered mode).

## Fit

High ingest rates, billion-vector ambitions, GPU-accelerated index build options in some deployments.

## Complexity tax

More moving parts than pgvector-on-RDS. Justify with measured scale—not resume-driven architecture.

## Kubernetes

Helm charts exist; treat like any stateful distributed system: capacity tests, backup of object storage segments, upgrade drills.
""",
    "vector-db-comparison": """# Vector DB Comparison

No universal winner—match **existing ops skills**, **query pattern**, and **scale**.

```text
        │ pgvector │ Qdrant │ Milvus │ OpenSearch k-NN
────────┼──────────┼────────┼────────┼──────────────────
ACL/SQL │   ★★★    │  ★★    │  ★★    │      ★★
Scale   │   ★★     │  ★★★   │  ★★★   │      ★★★
Ops sim │   ★★★    │  ★★    │  ★     │      ★★
Hybrid  │  tsvector│ payload│ varies │ native BM25+vec
```

## Decision workflow

1. Prove retrieval quality with **your** embedder and corpus on a sample index.
2. Measure p95 query latency at target QPS with filters.
3. Price RAM, egress, and engineer time for HA.

## Exit strategy

Abstract storage behind `VectorStore` interface—migrations hurt but are inevitable when scale crosses tiers.
""",
}
