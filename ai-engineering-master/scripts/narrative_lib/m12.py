# 12-model-serving

NARRATIVES = {
    "inference-fundamentals": """# Inference Fundamentals

Inference = prefill (process prompt) + decode (generate tokens autoregressively).

Latency and cost split differently—long prompts hurt prefill; long answers hurt decode FLOPs and KV memory.
""",
    "batching": """# Batching

Static batching waits to fill batch—good throughput, bad tail latency.

Dynamic grouping by sequence length reduces padding waste.
""",
    "continuous-batching": """# Continuous Batching

New requests join GPU work as others finish decode steps—vLLM/ORCA pattern.

Core to high GPU utilization in multi-tenant chat serving.
""",
    "kv-cache": """# KV Cache

Stores attention keys/values for prior tokens so decode avoids recomputing prefix.

Memory grows with layers × seq × batch—dominates long context. PagedAttention reduces fragmentation.
""",
    "quantization": """# Quantization

INT8/INT4 weights (and sometimes KV) cut memory and increase throughput; watch quality on your eval slice.

AWQ/GPTQ artifacts must match serving runtime support.
""",
    "speculative-decoding": """# Speculative Decoding

Small draft model proposes tokens; large model verifies in parallel—speedup when acceptance rate high.

Tune draft model pairing; measure on your traffic mix.
""",
    "streaming": """# Streaming

Token-by-token SSE to clients—improves perceived latency (TTFT).

Your API must handle client disconnect without leaking GPU work—or cancel generation promptly.
""",
    "vllm": """# vLLM

Production-oriented LLM server: continuous batching, PagedAttention, OpenAI-compatible API.

Deploy on GPU node pools; set `--max-model-len` from real context needs, not marketing max.
""",
    "triton": """# Triton Inference Server

NVIDIA Triton runs multiple model backends (TensorRT, ONNX, Python)—flexible for heterogeneous GPU fleets.

More assembly required than vLLM-for-LLM-only shops.
""",
    "kserve": """# KServe

Kubernetes-native model serving CRDs, autoscaling hooks, canary.

Pairs with Istio/Gateway for multi-model routing—see module 14 overlap.
""",
    "model-gateway": """# Model Gateway (Serving)

Edge gateway: auth, routing to vLLM/Triton pods, rate limits, token metrics—often Go.

Same pattern as LLM API gateway but backends are **your** GPUs.
""",
}
