# Vector Indexes

Brute-force k-NN is O(n)—fine for thousands, fatal for billions. **ANN indexes** partition space for sublinear search.

## Families

- **HNSW** — graph-based, low latency, RAM-heavy.
- **IVF** — inverted lists + coarse quantizer; needs training on representative vectors.
- **PQ/OPQ** — compress vectors; faster, lower recall.

## Rebuild vs update

Some indexes tolerate incremental insert; others need periodic rebuild. Plan **blue/green** index swap for major parameter or model changes.

## Capacity planning

RAM ≈ vectors × dim × 4 bytes (float32) plus graph overhead—back-of-envelope before you promise multi-tenant SaaS on one node.
