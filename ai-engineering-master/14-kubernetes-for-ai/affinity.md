# Affinity for AI Workloads

Co-locate embedding workers near vector DB region; spread inference replicas across zones for HA.

Anti-affinity prevents two vLLM shards on same host if you need blast radius control.
