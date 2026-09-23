# Anthropic APIs

Anthropic’s Messages API is a first-class alternative in many enterprises. System instructions, tool use, and document blocks have **provider-specific** details—abstract them behind your internal `CompletionRequest` type in the gateway.

Watch for: max output tokens, caching features (where offered), regional endpoints, and enterprise contract routing (Azure/GCP partnerships may change over time—verify current docs when integrating).

Your platform team should store **provider capability matrix** (tools, vision, PDF, context length) per model ID.
