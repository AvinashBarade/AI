# Gemini / Vertex AI

GCP-native stacks often standardize on **Vertex AI** for Gemini with IAM service accounts, VPC-SC, and CMEK requirements.

Integration pattern: workload identity in GKE → short-lived tokens → Vertex prediction endpoint. Same gateway abstraction as OpenAI; different auth and request JSON.

Multimodal parts (image bytes inline) affect payload size and latency—treat as separate route with stricter size limits.
