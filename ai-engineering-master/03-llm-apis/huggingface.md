# Hugging Face Ecosystem

HF is three things at once:

1. **Model Hub** — weights, tokenizer, model cards, licenses.
2. **Libraries** — `transformers`, `datasets`, `accelerate`.
3. **Inference** — Inference Endpoints or self-hosted.

For platform engineers, the operational path is: pin revision hash, scan license, build container with `transformers` + vLLM/TGI, deploy on GPU node pool.

Never `from_pretrained` arbitrary community models in prod without security review—pickle and supply-chain risk.
