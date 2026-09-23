# 04 — PyTorch Fundamentals (Infra Literacy)

**Not a deep learning course.** Enough PyTorch to understand what inference stacks serve, debug OOMs, and read training job logs.

**Objective:** *Understand what the infrastructure is actually serving and optimizing.*

---

## Status

Index only — lessons planned after `03-llm-fundamentals` (attention/block) or in parallel with Phase 6 inference track.

---

## Planned files

| File | Focus |
|------|--------|
| tensors-shapes-dtypes.md | Shape errors, `float16` vs `bfloat16` |
| device-cpu-gpu.md | `.to("cuda")`, synchronization |
| autograd-forward-backward.md | What training does (conceptual) |
| optimizer-loss.md | Connect to `00/optimization` |
| training-loop.md | Minimal loop |
| inference-loop.md | `torch.inference_mode()`, `no_grad` |
| batching-dataloader.md | Batching for throughput |
| gpu-memory.md | Allocated vs reserved, peak, fragmentation |

---

## Exit criteria

- Read a vLLM/PyTorch OOM stack trace and hypothesize cause
- Estimate whether a workload is **compute-bound vs memory-bound**
- Explain difference between training and inference GPU usage

---

## Skip if

You already operate GPU training clusters daily—skim `gpu-memory.md` and move to `14-inference-engineering`.
