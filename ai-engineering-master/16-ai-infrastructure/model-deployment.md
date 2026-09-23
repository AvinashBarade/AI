# Model Deployment

Artifact pipeline: weights in object storage → signed URL → init container → readiness probe with test inference.

Canary by traffic split; rollback on error rate and quality metrics.
