# Pretraining

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
