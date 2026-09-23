# Retries

Retry idempotent LLM reads with jitter; never blind retry tool writes.

429 from provider needs respect for Retry-After and tenant fairness.
