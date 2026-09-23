# 14-kubernetes-for-ai

NARRATIVES = {
    "gpu-scheduling": """# GPU Scheduling on Kubernetes

Pods request `nvidia.com/gpu` resources; scheduler places on GPU nodes.

Extended resources are **integer**—fractional GPU needs MIG or time-slicing strategies, not fake 0.5 resource without software.
""",
    "gpu-device-plugin": """# GPU Device Plugin

NVIDIA device plugin advertises GPUs to kubelet. Version skew with driver = pods stuck Pending.

Upgrade runbook: drain GPU nodes, driver, plugin, container toolkit in lockstep.
""",
    "gpu-node-pools": """# GPU Node Pools

Separate pools for inference vs training vs embedding batch—different SKUs and taints.

Autoscaler scales pool size; KEDA scales pod count from queue depth.
""",
    "taints-tolerations": """# Taints and Tolerations

GPU nodes tainted `nvidia.com/gpu=true:NoSchedule` so generic workloads don't steal expensive capacity.

Only serving pods tolerate GPU taint + matching nodeSelector/affinity.
""",
    "affinity": """# Affinity for AI Workloads

Co-locate embedding workers near vector DB region; spread inference replicas across zones for HA.

Anti-affinity prevents two vLLM shards on same host if you need blast radius control.
""",
    "autoscaling": """# Autoscaling AI on K8s

HPA on CPU fails for GPU servers—use custom metrics: queue depth, GPU util, requests/sec.

Scale-to-zero saves money; cold start (model load) must fit product tolerance.
""",
    "keda": """# KEDA

Event-driven autoscaling from Kafka, Prometheus, cloud queues.

Trigger embedding workers on backlog length; cap max replicas to control cost spikes.
""",
    "cluster-autoscaler": """# Cluster Autoscaler

Adds nodes when pending GPU pods can't schedule. Link max nodes to budget alerts.

GPU node boot + image pull + model download = minutes—plan buffer before traffic spikes.
""",
    "kserve": """# KServe on Kubernetes

ModelServer CRD, revision traffic splits, integration with GPU node pools.

Not a substitute for understanding raw Deployments + vLLM—you still own observability.
""",
    "ray": """# Ray on Kubernetes

Ray clusters for distributed training, batch inference, multi-agent runtimes.

KubeRay operator manages head/worker pods—heavier ops footprint than single vLLM Deployment.
""",
    "ai-workloads": """# AI Workloads on Kubernetes

Patterns: vLLM Deployment + Service, batch Jobs for embed index, Cron for eval, init containers for model artifact sync from object storage.

Liveness vs readiness: don't route until model weights loaded.
""",
}
