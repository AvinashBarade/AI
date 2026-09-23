# RAG Failure Modes

| Symptom | Likely cause |
|---------|----------------|
| Confident wrong fact | Bad retrieval or stale index |
| “I don’t know” always | Threshold too aggressive or empty index |
| Wrong tenant data | Missing metadata filter |
| Injection in answer | Malicious doc content |
| Slow p95 | Huge k, huge chunks, no cache |

Run a **failure taxonomy** in postmortems—stops “just tweak the prompt” loops.
