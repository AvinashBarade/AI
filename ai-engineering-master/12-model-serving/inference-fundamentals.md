# Inference Fundamentals

Inference = prefill (process prompt) + decode (generate tokens autoregressively).

Latency and cost split differently—long prompts hurt prefill; long answers hurt decode FLOPs and KV memory.
