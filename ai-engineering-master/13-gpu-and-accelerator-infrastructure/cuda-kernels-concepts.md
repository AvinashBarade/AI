# CUDA Kernels (Concepts)

Kernels are parallel functions on GPU grids. Frameworks hide them; infra engineers care about **kernel occupancy** and **memory bandwidth** when profiling slow inference.

Use Nsight for deep dives—not required to write kernels for most LLM serving roles.
