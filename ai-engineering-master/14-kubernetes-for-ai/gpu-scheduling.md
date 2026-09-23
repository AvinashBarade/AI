# GPU Scheduling on Kubernetes

Pods request `nvidia.com/gpu` resources; scheduler places on GPU nodes.

Extended resources are **integer**—fractional GPU needs MIG or time-slicing strategies, not fake 0.5 resource without software.
