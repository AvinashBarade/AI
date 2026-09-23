# GPU Device Plugin

NVIDIA device plugin advertises GPUs to kubelet. Version skew with driver = pods stuck Pending.

Upgrade runbook: drain GPU nodes, driver, plugin, container toolkit in lockstep.
