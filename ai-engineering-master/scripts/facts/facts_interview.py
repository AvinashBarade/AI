"""Interview preparation — concept-focused drill pages."""
from __future__ import annotations

def _p(mental, why, concepts, interview, practice):
    return {
        "mental": mental,
        "why": why,
        "concepts": concepts,
        "how": "Use spaced repetition: read concept → close notes → explain aloud → do one mock question.",
        "interview": interview,
        "practice": practice,
        "bridge": "Tie every answer to something you built in `22-projects/` or at work.",
    }

CONTENT = {
    "23-interview-preparation": {
        "ai-fundamentals": _p(
            "Map problems to **ML vs LLM vs rules** before diving into architecture.",
            "Filters noise in system design interviews.",
            ["Bias/variance", "Precision/recall", "Embeddings", "Stochastic APIs", "Eval discipline"],
            ["When not use LLM?", "Explain embedding.", "Overfitting?"],
            "5 Level-1 answers recorded on video.",
        ),
        "llm": _p(
            "LLM interview = **transformer + inference + product glue**.",
            "Core for AI engineer loops.",
            ["Attention", "KV cache", "Sampling", "Context limits", "Tool calling"],
            ["Prefill vs decode?", "Temperature?", "Function calling flow?"],
            "Draw transformer block from memory.",
        ),
        "rag": _p(
            "RAG interviews = **retrieval metrics + failure modes + ACL**.",
            "Most enterprise projects are RAG-heavy.",
            ["Hybrid search", "Rerank", "Faithfulness", "Chunking", "Freshness"],
            ["Why RAG vs FT?", "Debug empty retrieval.", "Multi-tenant index?"],
            "Design chunking eval for legal docs.",
        ),
        "agents": _p(
            "Agents = **bounded loops + tools + security**.",
            "Separate hype from production.",
            ["Workflow vs agent", "HITL", "Max steps", "Tool sandbox", "Cost per task"],
            ["When not agent?", "Infinite loop prevention?"],
            "Threat model one tool.",
        ),
        "mcp": _p(
            "MCP = **standard tool transport**, not auth boundary.",
            "Growing in IDE/enterprise integrations.",
            ["stdio/SSE", "Tools vs resources", "Remote MCP", "Audit logs"],
            ["MCP vs REST tools?", "Enterprise concerns?"],
            "Sketch MCP server for Git read-only.",
        ),
        "ai-infrastructure": _p(
            "Infra = **GPUs, serving, capacity math, networking**.",
            "Your differentiator as platform engineer.",
            ["Quantization", "Tensor parallel", "KV memory", "Cold start", "DR"],
            ["Estimate GPUs for QPS?", "Why inference expensive?"],
            "Spreadsheet capacity model.",
        ),
        "kubernetes-ai": _p(
            "K8s AI = **GPU scheduling + autoscale + KServe/Ray**.",
            "Skip pod basics; go deep on GPU ops.",
            ["Device plugin", "KEDA", "Taints", "Canary model", "GPU metrics"],
            ["Schedule GPU pod?", "Autoscale inference?"],
            "Write GPU Deployment + ServiceMonitor.",
        ),
        "system-design": _p(
            "Structured narrative beats buzzwords.",
            "Staff loops are multi-domain.",
            ["Requirements", "Capacity", "Data model", "Failure modes", "Cost"],
            ["Design RAG platform", "Design gateway", "Multi-tenant AI"],
            "One 45-min timed design per week.",
        ),
        "python": _p(
            "Python depth = **FastAPI, async, Pydantic, eval scripts**.",
            "Not language trivia.",
            ["async gather", "Pydantic validate", "pytest", "uv", "HF pipelines"],
            ["GIL?", "Structure service?"],
            "Ship typed FastAPI mini-service.",
        ),
        "coding": _p(
            "Go-heavy: **concurrency, streaming, limits, caches**.",
            "Mirrors gateway work.",
            ["Rate limiter", "Worker pool", "Heap top-k", "Trie", "Context cancel"],
            ["Token bucket", "LRU cache design"],
            "3 Go problems with tests.",
        ),
        "behavioral": _p(
            "STAR stories with **metrics and trade-offs**.",
            "Staff = influence and incidents.",
            ["Eval gates shipped", "Incident led", "Said no to scope", "Cross-team security"],
            ["Hardest production bug?", "Conflict with PM?"],
            "Write 6 STAR bullets.",
        ),
        "fde": _p(
            "Translate vague AI ask into **phased engineering plan**.",
            "Solutions/FDE screens.",
            ["Discovery questions", "Pilot scope", "Success metrics", "Rollout", "Support model"],
            ["10M doc RAG timeline?", "100% accuracy ask?"],
            "One full written case study.",
        ),
    }
}
