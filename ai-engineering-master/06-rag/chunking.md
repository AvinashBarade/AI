# Chunking

Chunking splits documents into units that fit embedding models and retrieval granularity.

## Strategies

- **Fixed token windows** (256–1024 common) with **overlap** (10–20%) to avoid cutting sentences at boundaries.
- **Structure-aware:** split on `h1/h2`, then merge small sections.
- **Semantic chunking:** embed sentences, merge until similarity drops—higher cost offline.

Too small → missing context. Too large → dilutes relevance signal; one chunk dominates attention.

## Parent-child pattern

Retrieve small chunks for precision; pass **parent section** text to LLM for context (LangChain/LlamaIndex patterns).

## Experiment

On your corpus, sweep chunk sizes; plot retrieval MRR and answer faithfulness—there is no universal optimum.
