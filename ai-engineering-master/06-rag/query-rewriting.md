# Query Rewriting

Users ask vague questions; indexes were built on declarative prose. Rewriting bridges the gap.

Techniques:

- **HyDE:** LLM drafts hypothetical answer document, embed that (risk: hallucinated entities—use carefully).
- **Step-back:** ask broader question first, then narrow.
- **Multi-query:** generate paraphrases, union retrieval results.

Every rewrite step adds latency and injection surface—log and eval each variant.
