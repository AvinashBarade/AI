# Tensor Parallelism

Split layers across GPUs; all-reduce per forward step. Lowers per-GPU memory, adds communication.

Common for models that don't fit one card.
