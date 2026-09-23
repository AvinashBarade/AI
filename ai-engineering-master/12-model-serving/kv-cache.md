# KV Cache

Stores attention keys/values for prior tokens so decode avoids recomputing prefix.

Memory grows with layers × seq × batch—dominates long context. PagedAttention reduces fragmentation.
