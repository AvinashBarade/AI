# RAG Fundamentals

Retrieval-Augmented Generation is the pattern that makes enterprise LLM products **grounded in your data** without retraining the foundation model on every PDF update.

```text
Offline:  docs → parse → chunk → embed → index
Online:   question → embed → retrieve → prompt + LLM → answer (+ cites)
```

## The critical distinction

**RAG is not training the LLM on your documents.** You are building a **search index** and stuffing results into the prompt. The model’s weights stay the same (unless you separately fine-tune).

Compare:

| Approach | What changes | Fresh docs |
|----------|--------------|------------|
| Prompt only | Instructions | Manual paste |
| RAG | Index + prompt context | Reindex pipeline |
| Fine-tune | Weights | Retrain job |
| Continued pretrain | Weights (massive) | ML program |

## Quality ceiling

If retrieval returns irrelevant chunks, the LLM can only **sound** authoritative. Measure retrieval and generation **separately**.

## Minimum production bar

- Citations to chunk IDs
- Tenant/metadata filters
- Eval set with faithfulness labels
- Freshness SLA for index updates
