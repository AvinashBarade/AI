# System Design: AI Chat

Components: auth, session store, gateway, model pool, moderation, feedback loop.

Scale: WebSocket/SSE streaming, regional stickiness optional, rate limits per user.

Design interview: capacity math on tokens/sec and storage for history retention policy.
