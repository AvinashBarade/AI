# Transformers

The transformer is the architectural bet that made modern LLMs possible: **parallel attention** over sequences instead of sequential RNN steps.

## Decoder-only stack (GPT-class)

```text
tokens → embed + position
       → repeat L times:
            self-attention (causal mask)
            feed-forward MLP
            residuals + norm
       → logits → softmax → next token
```

**Encoder-only** (BERT): bidirectional context; great for classification/embeddings, not open-ended chat generation.

**Encoder-decoder** (T5): seq2seq; translation/summarization patterns.

## Parameters live where

Most weights are in attention projections and FFN matrices. Model cards list `hidden_size`, `num_layers`, `num_heads`—use them in capacity planning conversations.

## What you won’t do

Rewrite a transformer in production. You **will** choose max context, quantization, and serving runtime based on this structure.
