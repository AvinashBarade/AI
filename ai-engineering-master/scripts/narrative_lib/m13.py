# 13-gpu-and-accelerator-infrastructure

NARRATIVES = {
    "gpu-fundamentals": """# GPU Fundamentals

GPUs excel at **parallel matrix ops**—exactly transformer matmuls. CPU orchestrates; GPU computes.

Know SKU (A100, H100, L4), VRAM, and PCIe/NVLink topology before sizing clusters.
""",
    "cpu-vs-gpu": """# CPU vs GPU for AI

CPU: low latency small models, preprocessing, orchestration.

GPU: LLM inference/training at scale. Don't run 70B on CPU in prod unless you enjoy timeouts.
""",
    "gpu-memory": """# GPU Memory

VRAM holds weights, activations, KV cache, and temporary buffers. OOM kills the process—no swap salvation.

Right-size context length and batch; quantization frees headroom.
""",
    "cuda": """# CUDA

NVIDIA software stack for GPU programs. Drivers on nodes must match container CUDA expectations.

MIG splits A100 for smaller tenants—ops complexity vs isolation.
""",
    "cuda-kernels-concepts": """# CUDA Kernels (Concepts)

Kernels are parallel functions on GPU grids. Frameworks hide them; infra engineers care about **kernel occupancy** and **memory bandwidth** when profiling slow inference.

Use Nsight for deep dives—not required to write kernels for most LLM serving roles.
""",
    "tensor-cores": """# Tensor Cores

Hardware units accelerating mixed-precision matmuls—why FP16/BF16 inference is fast on recent NVIDIA GPUs.

Ensure serving stack uses tensor core paths where possible.
""",
    "gpu-utilization": """# GPU Utilization

Low util = wasted lease dollars. Causes: small batches, serial requests, CPU bottlenecks, bad scheduling.

Target high util with continuous batching—not 100% at expense of p99 latency SLO.
""",
    "multi-gpu": """# Multi-GPU

Single host multiple GPUs: tensor parallel for one big model, or data parallel replicas for throughput.

Network all-reduce matters across nodes—not just within box.
""",
    "tensor-parallelism": """# Tensor Parallelism

Split layers across GPUs; all-reduce per forward step. Lowers per-GPU memory, adds communication.

Common for models that don't fit one card.
""",
    "pipeline-parallelism": """# Pipeline Parallelism

Stages on different GPUs—micro-batches pipeline through. Helps very deep models; bubble overhead exists.

Less common in decoder-only LLM serving than tensor parallel + replicas.
""",
    "distributed-inference": """# Distributed Inference

Combine TP/PP with load balancers in front of replica groups. Watch **tail latency** on cross-node TP.

Health checks must validate model ready, not just pod running.
""",
}
