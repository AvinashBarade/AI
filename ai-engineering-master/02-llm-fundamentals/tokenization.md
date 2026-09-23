# Tokenization

Tokenization is the **codec** between human text and model integers. Changing tokenizer without changing model weights is like changing protobuf schema without updating servers—everything breaks subtly.

## Algorithms you’ll meet

- **BPE (Byte-Pair Encoding):** merge frequent pairs until vocab size reached—GPT family tradition.
- **SentencePiece / Unigram:** common in multilingual models; can treat whitespace explicitly.

Normalization (NFKC, lowercasing) happens **before** merges. Edge cases: emojis, rare Unicode, medical compounds.

## Round-trip invariants

`decode(encode(text))` should recover text **mostly**. PDF extraction garbage in → weird tokens out → bad retrieval.

## Engineering checklist

- Pin `tokenizer.json` / `tokenizer.model` with model version in registry.
- Test token counts on **your** domain corpus (support tickets, logs, legal).
- When comparing models, compare **cost per document**, not cost per character.
