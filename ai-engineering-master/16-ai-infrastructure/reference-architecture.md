# Reference Architecture

Typical enterprise stack:

```text
Edge WAF → AI Gateway → App services → {vLLM pool, vector DB, object storage}
                    ↘ OTel → Prometheus/Grafana
```

Adapt regions, CMEK, and air-gapped object stores per compliance—not copy-paste cloud blog posts.
