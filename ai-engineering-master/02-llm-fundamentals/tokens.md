# Tokens: The Real Unit of LLM Systems

Providers bill you in **tokens**. Context windows are measured in **tokens**. Rate limits are often **tokens per minute**. If you still think in words, you will mis-size prompts and budgets.

A **token** is an integer ID from a fixed vocabulary produced by a **tokenizer**. The model never sees Unicode strings in the transformer—only IDs, then learned embedding vectors.

## Why subwords exist

English “unhappiness” might be multiple tokens; rare words split into pieces so the vocab stays finite (~32k–200k). Code and JSON are token-inefficient: braces and indentation become many tokens.

**Practical rule:** measure with the **same tokenizer as the model** before shipping a feature.

```python
# Hugging Face pattern
ids = tokenizer.encode("def hello(): pass")
print(len(ids))
```

## Operations impact

- Longer prompts → higher **prefill** cost and latency.
- Longer completions → linear growth in decode cost.
- Same semantic content, different formatting → different token count.

## Platform takeaway

Your gateway should log `prompt_tokens`, `completion_tokens`, and attribute them to `tenant_id` and `route`. Finance will ask; be ready.
