# AI vs ML vs DL vs GenAI

You already ship backends. When someone says “we need AI,” your first job is to **name which layer of the stack they mean**—because the engineering work, cost, and risk are completely different.

## The nesting picture (keep this in your head)

**Artificial intelligence** is the umbrella: systems that do tasks we associate with human intelligence (language, vision, planning, classification).

**Machine learning** is a subset: the system **learns patterns from data** instead of you encoding every rule in `if` statements.

**Deep learning** is ML with **deep neural networks**—many layers, usually trained on GPUs, often on raw or lightly processed inputs (pixels, token IDs).

**Generative AI** is DL focused on **creating** content—most visibly large language models that continue text token by token.

```text
GenAI ⊂ DL ⊂ ML ⊂ AI
```

That nesting is not academic. It tells you whether you’re building a **classifier**, a **retrieval system**, or a **stochastic text API**.

## What each one looks like in production (your world)

### Classical ML (still everywhere)

Think fraud, churn, ranking, anomaly detection on **tabular or feature-engineered** data.

- Input: transaction features, user history aggregates.
- Output: score, label, rank.
- Serving: small CPU models, milliseconds, deterministic-ish.
- You own: feature pipelines, drift monitoring, precision/recall trade-offs.

An LLM is a poor default here if you have labeled data and need calibrated probabilities.

### Deep learning (without “chat”)

Think embeddings, speech, vision, document classifiers.

- Input: tensors (images, audio spectrograms, token sequences).
- Output: vectors, classes, segments.
- Serving: GPU sometimes; often batch jobs for embeddings.
- You own: model versioning, preprocessing parity train/serve.

### Generative AI / LLMs

Think copilots, support bots, doc Q&A, agents.

- Input: token sequences (prompt).
- Output: **sampled** text (or tools calls).
- Serving: seconds, dollars per 1M tokens, complex guardrails.
- You own: prompts, RAG, eval, gateway, security—not retraining GPT from scratch.

## The mistake senior engineers still make

Treating the LLM as a **deterministic microservice**.

Same HTTP 200 can be brilliant or wrong. Your SLIs must include **quality** (eval, human review samples), not only latency and availability.

## How this connects to architecture choices

| Business ask | Often right stack |
|--------------|-------------------|
| “Classify tickets” | ML classifier or rules + ML; maybe LLM for messy text |
| “Answer from our wiki” | RAG + LLM API; not fine-tune on day one |
| “Match our brand voice” | Prompt → maybe LoRA; still need eval |
| “Predict demand” | Time-series ML; not GenAI |
| “Automate multi-step ops” | Workflow + tools; agent only if ambiguity is real |

## Practical drill

Pick three features from your current product. For each, write:

1. Is the output **fixed schema** or open-ended language?
2. Does knowledge change **daily**?
3. What’s the cost of a wrong answer?

That table alone usually kills half the “let’s GPT it” ideas.

## Interview compression

**GenAI** generates language (or other modalities) from learned distributions; **ML** learns mappings from data; you choose LLMs when language variability and task ambiguity dominate, and classical ML when labels, structure, and calibration matter.

---

Next: [mental-models.md](./mental-models.md) for the full stack in pictures, or [probability-statistics-for-ai.md](./probability-statistics-for-ai.md) if you want the math behind eval metrics.
