# 06-rag — deep narrative material

NARRATIVES = {
    "rag-fundamentals": """# RAG Fundamentals

Retrieval-Augmented Generation is the pattern that makes enterprise LLM products **grounded in your data** without retraining the foundation model on every PDF update.

```text
Offline:  docs → parse → chunk → embed → index
Online:   question → embed → retrieve → prompt + LLM → answer (+ cites)
```

## The critical distinction

**RAG is not training the LLM on your documents.** You are building a **search index** and stuffing results into the prompt. The model’s weights stay the same (unless you separately fine-tune).

Compare:

| Approach | What changes | Fresh docs |
|----------|--------------|------------|
| Prompt only | Instructions | Manual paste |
| RAG | Index + prompt context | Reindex pipeline |
| Fine-tune | Weights | Retrain job |
| Continued pretrain | Weights (massive) | ML program |

## Quality ceiling

If retrieval returns irrelevant chunks, the LLM can only **sound** authoritative. Measure retrieval and generation **separately**.

## Minimum production bar

- Citations to chunk IDs
- Tenant/metadata filters
- Eval set with faithfulness labels
- Freshness SLA for index updates
""",
    "ingestion": """# RAG Ingestion

Ingestion is everything that happens **before** a user asks a question: connectors, ACL sync, parsing, chunking, embedding, upsert.

Treat it as a **data pipeline** with backpressure—not a one-off script.

## Connectors

SharePoint, S3, Confluence, tickets—each has auth, rate limits, and deletion events. You need **incremental** sync: only reprocess changed objects.

## ACL is not optional

If a user can’t read a doc in source system, they must not retrieve it in RAG. Propagate permissions to vector payload fields and filter every query.

## Poisoning awareness

Malicious or compromised documents are **untrusted input** to the model—same class as prompt injection via user chat.
""",
    "document-parsing": """# Document Parsing

Models read **text you extract**—not pretty PDF layouts. Garbage extraction → garbage chunks → confident wrong answers.

## Formats

- **HTML/Markdown:** preserve headings hierarchy for chunk boundaries.
- **PDF:** layout analysis; tables are hard—consider specialized parsers or human QA on samples.
- **DOCX:** styles map to structure.
- **Scanned PDF:** OCR adds errors—flag low-confidence regions.

## Tables and code

Tables flattened to plain text often lose semantics. Sometimes store table HTML or CSV sidecar metadata for retrieval filters.

## QA process

Sample 50 random pages per source; human rate “parse usable?” before full index.
""",
    "chunking": """# Chunking

Chunking splits documents into units that fit embedding models and retrieval granularity.

## Strategies

- **Fixed token windows** (256–1024 common) with **overlap** (10–20%) to avoid cutting sentences at boundaries.
- **Structure-aware:** split on `h1/h2`, then merge small sections.
- **Semantic chunking:** embed sentences, merge until similarity drops—higher cost offline.

Too small → missing context. Too large → dilutes relevance signal; one chunk dominates attention.

## Parent-child pattern

Retrieve small chunks for precision; pass **parent section** text to LLM for context (LangChain/LlamaIndex patterns).

## Experiment

On your corpus, sweep chunk sizes; plot retrieval MRR and answer faithfulness—there is no universal optimum.
""",
    "embedding-pipeline": """# Embedding Pipeline

Batch job: read chunks → call embedding model (API or local GPU) → upsert to vector store with metadata.

## Idempotency

Key chunks by `hash(content + doc_version)`. Re-embed only when content changes.

## Throughput

Batch size tuned to GPU/API limits. Dead-letter queue for failures; never silently drop docs.

## Version field

Store `embedding_model=v3` on every vector. Mixed versions in one index destroy recall—blue/green reindex when model changes.
""",
    "retrieval": """# Retrieval

Given query vector (and filters), return top-k chunk IDs and scores.

## Parameters

- **k:** higher improves recall, hurts precision and prompt size.
- **Score threshold:** return “I don’t know” when nothing passes.

## Diversity

MMR reduces redundant near-duplicate chunks in results.

## Observability

Log retrieved IDs and scores per request—first thing to inspect when answers go wrong.
""",
    "hybrid-search": """# Hybrid Search

Dense vectors miss **exact tokens** (SKUs, statute numbers, error codes). Sparse **BM25** keyword search catches them.

## Fusion

Run both retrievers, merge with **Reciprocal Rank Fusion (RRF)** or weighted linear combo. Tune on your eval queries—legal docs often need higher BM25 weight.

## Stack options

OpenSearch/Elasticsearch with vector field + pgvector with `tsvector` side by side—architecture varies; pattern is the same.
""",
    "reranking": """# Reranking

First stage: fast bi-encoder retrieval (top 50–100). Second stage: **cross-encoder** or LLM scores `(query, chunk)` pairs accurately—expensive.

Cascade keeps p95 latency bounded: only rerank top 20.

## When worth it

Hard paraphrase queries, dense technical docs, support tickets where lexical overlap is weak.

## Cost

Reranker API calls per query—attribute cost in gateway metrics.
""",
    "metadata-filtering": """# Metadata Filtering

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
""",
    "query-rewriting": """# Query Rewriting

Users ask vague questions; indexes were built on declarative prose. Rewriting bridges the gap.

Techniques:

- **HyDE:** LLM drafts hypothetical answer document, embed that (risk: hallucinated entities—use carefully).
- **Step-back:** ask broader question first, then narrow.
- **Multi-query:** generate paraphrases, union retrieval results.

Every rewrite step adds latency and injection surface—log and eval each variant.
""",
    "contextual-retrieval": """# Contextual Retrieval

Some chunks lack section headers (“Section 4.2” context missing). **Contextual retrieval** prepends generated situating text before embedding the chunk offline.

Trade-off: extra LLM calls during indexing, storage size, re-embed when parent doc changes.

Use when ablation shows retrieval misses on ambiguous standalone paragraphs.
""",
    "multimodal-rag": """# Multimodal RAG

Manuals with diagrams, UI screenshots, or scanned forms need **vision embeddings** or captions.

Patterns:

- Caption images with vision model → text index as today.
- CLIP-style joint embeddings for image+text search.

Higher storage/compute; define when text-only RAG failed eval.
""",
    "graph-rag": """# Graph RAG

When answers require **relationships** (org charts, dependencies, entities across docs), augment vectors with a **knowledge graph**.

Microsoft GraphRAG-style pipelines build community summaries and graph traversals—complex ops, strong on multi-hop questions.

Start with simple entity extraction + edges; only invest when vector-only eval plateaus on relational queries.
""",
    "rag-evaluation": """# RAG Evaluation

Split metrics:

**Retrieval:** recall@k, MRR, nDCG on labeled relevant chunk IDs.

**Generation:** faithfulness (answer supported by context?), answer relevance, citation correctness.

LLM-as-judge is tempting—calibrate against human labels on a slice; judges inherit model biases.

CI gate: fail if faithfulness drops >X% vs baseline on frozen golden set.
""",
    "rag-failure-modes": """# RAG Failure Modes

| Symptom | Likely cause |
|---------|----------------|
| Confident wrong fact | Bad retrieval or stale index |
| “I don’t know” always | Threshold too aggressive or empty index |
| Wrong tenant data | Missing metadata filter |
| Injection in answer | Malicious doc content |
| Slow p95 | Huge k, huge chunks, no cache |

Run a **failure taxonomy** in postmortems—stops “just tweak the prompt” loops.
""",
    "production-rag": """# Production RAG

Pilot checklist vs prod:

- Incremental indexing + deletion sync
- Blue/green index swap
- Query caching (semantic cache optional)
- Rate limits per tenant
- DR: rebuild index from source of truth
- On-call runbooks for “index lag” and “embedding provider down”

SLA example: 95% of docs reflected in index within 15 minutes of source change.

Capstone architecture belongs in `22-projects/03-production-rag`.
""",
}
