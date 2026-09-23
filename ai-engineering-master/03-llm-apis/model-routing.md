# Model Routing

Routing chooses **which model and provider** handle a request.

Inputs to policy:

- Task type (extract vs chat vs code)
- Tenant tier and data residency
- Latency SLO
- Cost budget
- Safety level (refusal strictness)

Implementation in Go at the gateway:

```text
classify(request) → route table → primary + fallback chain
```

Log `route_decision` on every trace for finance and debugging.

Circuit-break provider on error rate; shift traffic to secondary region/model with pre-tested eval parity.
