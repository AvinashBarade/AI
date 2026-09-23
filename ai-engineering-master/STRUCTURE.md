# Repository Structure — Complete Manifest

**Status:** All paths below exist with Markdown content (generated + selected deep overrides).

**Verify:** `python scripts/verify_structure.py` from `scripts/` directory.

---

## Root (6)

- README.md · ROADMAP.md · PROGRESS.md · GLOSSARY.md · INTERVIEW_MASTER.md · BUILD_LOG.md

## Modules (234 topic files)

| Module | Files |
|--------|-------|
| 00-foundations | 6 |
| 01-python-for-ai-engineering | 7 |
| 02-llm-fundamentals | 15 |
| 03-llm-apis | 6 |
| 04-prompt-engineering | 7 |
| 05-embeddings-and-vector-search | 8 |
| 06-rag | 16 |
| 07-agents | 12 |
| 08-mcp | 8 |
| 09-ai-frameworks | 5 |
| 10-evaluation | 10 |
| 11-fine-tuning | 9 |
| 12-model-serving | 11 |
| 13-gpu-and-accelerator-infrastructure | 11 |
| 14-kubernetes-for-ai | 11 |
| 15-ai-platform-engineering | 12 |
| 16-ai-infrastructure | 10 |
| 17-observability | 11 |
| 18-ai-security | 11 |
| 19-production-ai | 10 |
| 20-fde-engineering | 11 |
| 21-system-design | 10 |
| 23-interview-preparation | 12 |
| 24-research | 5 |

## Projects (11)

`22-projects/01-llm-chat-api` … `11-capstone-ai-platform` — each has README.md.

## Tooling

- `scripts/generate_curriculum.py` — regenerate topic/project bodies  
- `scripts/enhance_deep_topics.py` — overwrite flagship topics with extra depth  
- `scripts/verify_structure.py` — completeness check  

## Deep overrides (hand-enhanced)

- `02-llm-fundamentals/attention.md`
- `02-llm-fundamentals/transformers.md`
- `06-rag/rag-fundamentals.md`
- `12-model-serving/kv-cache.md`

Additional hand-authored richness may remain in select `00-foundations` files if longer than generated threshold.
