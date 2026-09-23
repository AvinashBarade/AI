# Prometheus for AI

Counters: tokens in/out, requests by model. Histograms: latency phases. Gauges: queue depth, GPU util from DCGM.

Avoid high-cardinality labels (full prompt text)—use hashed prompt_id.
