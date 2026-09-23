# 11-fine-tuning

NARRATIVES = {
    "prompting-vs-rag-vs-finetuning": """# Prompting vs RAG vs Fine-Tuning

| Method | Changes | Best for |
|--------|---------|----------|
| Prompt | Instructions | Policy, format |
| RAG | External facts | Fresh docs |
| Fine-tune | Weights | Stable style/task |

Most enterprise wins: prompt + RAG before GPU training programs.
""",
    "supervised-finetuning": """# Supervised Fine-Tuning (SFT)

Train on input→output pairs to mimic behavior—format, tone, domain phrasing.

Needs curated dataset, eval split, and guard against memorizing PII from training rows.
""",
    "lora": """# LoRA

Low-rank adapters train small matrices attached to frozen base weights—efficient GPU use.

Ship adapter weights per tenant or task; load in vLLM/serving stack that supports LoRA hot-swap.
""",
    "qlora": """# QLoRA

LoRA + quantized base (4-bit)—fits larger models on single consumer GPU for experimentation.

Prod serving may still want full-precision base + merged adapters—validate latency/quality.
""",
    "adapters": """# Adapters

Beyond LoRA: adapter layers, prefix tuning. Pick one strategy per platform—operational complexity multiplies with mixing.

Registry should record base model + adapter artifact hash.
""",
    "datasets": """# Fine-Tuning Datasets

Quality > quantity. Dedup near-duplicates; strip secrets; balance classes.

Provenance and license for every row—training on scraped customer data without consent is a legal incident.
""",
    "training-loop": """# Training Loop

Standard DL: forward, loss, backward, checkpoint, early stop on val loss.

Use experiment tracking (W&B, MLflow); reproducible seeds; spot-check generations each epoch—not loss alone.
""",
    "evaluation": """# Fine-Tune Evaluation

Compare base vs tuned on **held-out** tasks and **safety** refusals.

Regression on general capability (catastrophic forgetting) matters for small models.
""",
    "when-to-finetune": """# When to Fine-Tune

Consider when: stable task, large labeled set, prompt/RAG ceiling proven, cost of long prompts exceeds training.

Skip when: facts change daily (RAG), few examples (few-shot), or compliance needs citeable retrieval.
""",
}
