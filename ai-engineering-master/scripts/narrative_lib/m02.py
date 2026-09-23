# 02-llm-fundamentals — narrative study material

NARRATIVES = {
    "tokens": """# Tokens: The Real Unit of LLM Systems

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
""",
    "tokenization": """# Tokenization

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
""",
    "embeddings": """# Embeddings

An embedding maps text (or tokens) to a dense vector \(\mathbb{R}^d\). Similar meaning → nearby vectors **if** the model was trained for that notion of similarity.

## Two different uses

1. **Input embeddings** inside the LLM (learned lookup table per token ID).
2. **Sentence/document embeddings** from encoder models (e5, BGE, etc.) for search.

Don’t confuse them in architecture diagrams.

## Similarity

Cosine on L2-normalized vectors equals dot product. Many APIs return normalized vectors—check model card.

## Production

- Embedding model version must match index version.
- Batch embed offline; cache doc vectors.
- Evaluate retrieval with **your** queries, not MTEB leaderboard alone.
""",
    "transformers": """# Transformers

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
""",
    "attention": """# Attention

Attention answers: *for this token, which other tokens should influence its representation?*

Given queries \(Q\), keys \(K\), values \(V\):

\[
\text{Attention}(Q,K,V)=\text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
\]

Scale by \(\sqrt{d_k}\) so softmax doesn’t saturate when dimension grows.

## Causal masking (decoders)

Token at position \(i\) may not attend to \(j>i\). That enforces autoregressive generation: the future must not leak into the past during training/inference.

## Multi-head

Several attention operations run in parallel (different subspaces), concatenate, project. Heads let the model attend to different relationship types (syntax, coreference, etc.)—you reason at the block level, not per head in prod.

## FlashAttention (why infra cares)

Standard attention materializes large \(N\times N\) score matrices in HBM. FlashAttention tiles computation to reduce memory traffic—enables longer context and larger batch on same GPU.

## Debug without attention maps

Ablate: shorten prompt, remove RAG chunks, swap model. Attention visualization is research tooling—not your first prod debugger.
""",
    "positional-encoding": """# Positional Encoding

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
""",
    "pretraining": """# Pretraining

Pretraining teaches general language structure by **next-token prediction** on massive corpora. The model learns grammar, facts (with cutoff), reasoning patterns—emergent capabilities scale with data and compute.

## Objective

Minimize cross-entropy on true next tokens—maximum likelihood. Not “truth” or “helpfulness”—that comes later (SFT, alignment).

## You rarely pretrain

Product teams **consume** checkpoints (OpenAI, Anthropic, Meta Llama, etc.). Your leverage is:

- data curation for RAG
- eval
- routing smaller models
- fine-tuning adapters when justified

## Risks at pretrain scale

Data contamination, PII, copyrighted text, bias. Governance matters even if you only download weights—license and acceptable use policies apply.
""",
    "instruction-tuning": """# Instruction Tuning (SFT)

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
""",
    "alignment": """# Alignment

Alignment shapes behavior toward **human preferences and policies**—refusals, tone, safety, instruction following beyond bare likelihood.

## RLHF (high level)

1. SFT model
2. Train reward model from human comparisons
3. Optimize policy (PPO) to increase reward while staying close to reference

## Alternatives you’ll hear

- **DPO / IPO:** preference learning without explicit reward model training loop in some setups.
- **Constitutional AI / rules:** layer policies in training or inference.

## Production alignment is layered

Model alignment + **gateway policies** + **tool permissions** + **content filters** + **human review** for edge cases. Don’t assume the base model is your entire safety program.
""",
    "inference": """# LLM Inference

Inference = forward passes with **frozen weights**. Training gradients are gone; now you care about milliseconds and dollars.

## Two phases

| Phase | What happens | Dominant cost |
|-------|----------------|---------------|
| **Prefill** | Process entire prompt; build KV cache | Compute (matmul) |
| **Decode** | Generate one token at a time | Memory bandwidth (KV) |

Short answers after huge prompts → optimize prefill (smaller prompt, caching). Long answers → decode dominates.

## Sampling

Logits → temperature scaling → softmax → sample or greedy. `temperature=0` often near-deterministic but provider-dependent.

## Serving interfaces

Remote APIs (OpenAI-compatible) or self-hosted **vLLM/TGI** on Kubernetes. Your Go gateway wraps either the same way.
""",
    "context-window": """# Context Window

The context window is the maximum **tokens** (prompt + completion) the model can attend to in one forward pass. It is not “how much text we should stuff in.”

## Failure modes

- **Truncation:** drop start or end—often silently—breaking instructions or citations.
- **Lost in the middle:** salient facts buried in middle of long contexts get ignored statistically.
- **Cost explosion:** linear token billing.

## Mitigations

Summarize older chat turns; retrieve only top chunks; use smaller models to compress; store state externally (DB) instead of infinite history in prompt.

## Architecture

Track `context_tokens` metric per request; alert when p95 approaches limit; client-side pre-count before send.
""",
    "temperature-sampling": """# Temperature and Sampling

After the final layer you have a vector of **logits** over the vocabulary. Temperature \(T\) divides logits before softmax:

- **Low T** → peaked distribution → deterministic, factual tasks.
- **High T** → flat distribution → creative, risky for extraction.

## top-k and top-p (nucleus)

Restrict sampling mass to likely tokens—reduces bizarre tail tokens. Production configs often combine `temperature=0.2`, `top_p=0.9` for support bots.

## Eval discipline

Regression-test prompts at **fixed** sampling settings. Changing T between runs invalidates A/B comparisons.

## Reproducibility

Seeds help on some stacks; don’t rely on cross-provider identical outputs for tests.
""",
    "structured-output": """# Structured Output

Downstream code wants **JSON**, not prose with markdown fences.

Strategies:

1. **Prompting** with schema description (weakest alone).
2. **JSON mode / response_format** from provider.
3. **Constrained decoding** (grammar, outlines) when available.
4. **Parse + validate + repair** with Pydantic (always).

```python
from pydantic import BaseModel

class Ticket(BaseModel):
    title: str
    priority: int
```

Retry loop: on `ValidationError`, send model the error message and ask for correction—cap attempts (3) and metric failures.

## Security

Structured output does not prevent **wrong** content—only well-typed wrong content.
""",
    "function-calling": """# Function Calling

The model emits a structured **tool call** (name + JSON args). Your runtime validates, authorizes, executes, appends **tool role** message with result, continues generation.

## Loop sketch

```text
user message
→ model (maybe tool_calls)
→ execute tools (parallel if allowed)
→ tool results
→ model final answer
```

## Production requirements

- Tool allowlist per tenant/role
- Timeouts and idempotency keys for side effects
- Audit log: who invoked what with hashed args
- Never execute SQL/shell from raw model strings without human approval in high-risk domains

## vs MCP

Function calling is the **pattern**; MCP standardizes discovery/transport of tools across clients.
""",
    "model-selection": """# Model Selection

Choosing a model is a **capacity, cost, compliance, and quality** decision—not a leaderboard contest.

## Dimensions

| Question | Why it matters |
|----------|----------------|
| Context length needed? | Long docs vs chat |
| Latency SLO? | Small model or regional edge |
| Data residency? | Azure OpenAI vs US-only API |
| Tool calling quality? | Agent reliability |
| Open weights required? | Self-host vLLM |

## Process

1. Build golden eval (100–500 tasks).
2. Run candidates with fixed prompts/RAG.
3. Measure quality, P95 latency, $/success.
4. Route easy traffic to cheap model; escalate hard cases.

## Gateway pattern (Go)

```text
if complexity_score < t: route small
elif needs_tools: route tool-strong
else: route large
```

Document escalation rules—interviewers love explicit economics.
""",
}
