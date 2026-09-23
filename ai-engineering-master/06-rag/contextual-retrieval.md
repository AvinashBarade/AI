# Contextual Retrieval

Some chunks lack section headers (“Section 4.2” context missing). **Contextual retrieval** prepends generated situating text before embedding the chunk offline.

Trade-off: extra LLM calls during indexing, storage size, re-embed when parent doc changes.

Use when ablation shows retrieval misses on ambiguous standalone paragraphs.
