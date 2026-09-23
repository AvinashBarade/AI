# Taints and Tolerations

GPU nodes tainted `nvidia.com/gpu=true:NoSchedule` so generic workloads don't steal expensive capacity.

Only serving pods tolerate GPU taint + matching nodeSelector/affinity.
