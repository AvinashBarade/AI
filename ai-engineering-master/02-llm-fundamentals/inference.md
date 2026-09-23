# LLM Inference

Inference = forward passes with **frozen weights**. Training gradients are gone; now you care about milliseconds and dollars.

## Two phases

| Phase | What happens | Dominant cost |
|-------|----------------|---------------|
| **Prefill** | Process entire prompt; build KV cache | Compute (matmul) |
| **Decode** | Generate one token at a time | Memory bandwidth (KV) |

Short answers after huge prompts → optimize prefill (smaller prompt, caching). Long answers → decode dominates.

## Sampling

Logits → temperature scaling → softmax → sample or greedy. `temperature=0` often near-deterministic but provider-dependent.

## Serving interfaces

Remote APIs (OpenAI-compatible) or self-hosted **vLLM/TGI** on Kubernetes. Your Go gateway wraps either the same way.
