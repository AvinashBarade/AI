# Milvus

Milvus targets **large-scale** vector workloads with distributed components (query node, data node, etcd/minio dependencies in clustered mode).

## Fit

High ingest rates, billion-vector ambitions, GPU-accelerated index build options in some deployments.

## Complexity tax

More moving parts than pgvector-on-RDS. Justify with measured scale—not resume-driven architecture.

## Kubernetes

Helm charts exist; treat like any stateful distributed system: capacity tests, backup of object storage segments, upgrade drills.
