# Positional Encoding

Self-attention is **permutation-invariant** without positions—you could shuffle tokens and get the same pairwise interactions. Language is order-sensitive, so models inject **position information**.

## Classic approaches

- **Sinusoidal** (original Transformer): fixed functions of position.
- **Learned** absolute embeddings: table indexed by position (limited max length).
- **RoPE (Rotary Position Embedding):** rotates Q/K by position—popular in Llama-class models; relative position bias in attention scores.
- **ALiBi:** linear biases on attention scores to extrapolate length somewhat.

## Why you should care

`max_position_embeddings` in config is a **hard cliff** unless the vendor explicitly supports extension techniques. “We’ll just stuff 200k tokens” requires verifying model + serving stack support.

## RAG interaction

Positions apply to **everything** in the window—system, retrieved junk, and user text compete for the same positional budget.
