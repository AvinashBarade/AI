# 16-ai-infrastructure

NARRATIVES = {
    "reference-architecture": """# Reference Architecture

Typical enterprise stack:

```text
Edge WAF → AI Gateway → App services → {vLLM pool, vector DB, object storage}
                    ↘ OTel → Prometheus/Grafana
```

Adapt regions, CMEK, and air-gapped object stores per compliance—not copy-paste cloud blog posts.
""",
    "inference-clusters": """# Inference Clusters

Dedicated GPU clusters with fast network, model cache on local NVMe, horizontal vLLM replicas behind L4/L7 load balancers.

Separate from CPU microservices cluster to simplify blast radius and scaling signals.
""",
    "model-deployment": """# Model Deployment

Artifact pipeline: weights in object storage → signed URL → init container → readiness probe with test inference.

Canary by traffic split; rollback on error rate and quality metrics.
""",
    "distributed-inference": """# Distributed Inference (Infrastructure)

Multi-node TP groups behind single logical endpoint—coordination and failure domains are hard.

Prefer smaller models + routing before jumping to mega-model TP unless eval proves need.
""",
    "storage": """# Storage for AI

Object store for corpora and checkpoints; block storage for GPU node model cache; vector DB for embeddings.

Lifecycle policies—stale indexes cost money and confuse retrieval.
""",
    "networking": """# Networking

East-west bandwidth for TP; egress costs to cloud LLM APIs; private endpoints for Vertex/Azure OpenAI.

Latency between app and vector DB dominates RAG p95 in multi-region setups.
""",
    "caching": """# Caching (Infrastructure)

Semantic cache at gateway (optional), CDN for static assets, Redis for session state.

Invalidate on prompt/index version change—stale cache = wrong answers with low latency.
""",
    "reliability": """# Reliability

Multi-AZ replicas, provider fallback chains, graceful degradation (shorter context, smaller model).

Define error budget for AI features separately from core API—stochastic failures differ.
""",
    "disaster-recovery": """# Disaster Recovery

Rebuild indexes from source docs; restore model artifacts from replicated buckets; RTO/RPO for gateway config and registries.

Test DR yearly—embedding reindex duration is often the long pole.
""",
    "capacity-planning": """# Capacity Planning

Model requests/sec × tokens × GPU TFLOPs/memory → node count + headroom for spikes.

Include reindex and batch embed peaks—not just chat steady state.
""",
}
