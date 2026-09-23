# Instruction Tuning (SFT)

Raw pretrained models complete text; they don’t naturally act like assistants. **Supervised fine-tuning (SFT)** on (instruction, response) pairs teaches chat formatting and helpful behavior.

## Chat templates

Models expect a specific string format (`<|user|>`, `[INST]`, etc.). Serving **must** apply the same template as training or quality collapses.

```python
# HF pattern
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

## Data quality beats size

Thousands of excellent examples can beat millions of noisy ones. Filter toxicity, PII, and incorrect answers **before** SFT.

## Relation to your stack

SFT is not your first lever—**prompt + RAG** usually are. SFT shines for stable output schemas and domain phrasing when retrieval alone can’t fix format reliability.
