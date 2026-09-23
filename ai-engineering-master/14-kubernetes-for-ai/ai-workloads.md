# AI Workloads on Kubernetes

Patterns: vLLM Deployment + Service, batch Jobs for embed index, Cron for eval, init containers for model artifact sync from object storage.

Liveness vs readiness: don't route until model weights loaded.
