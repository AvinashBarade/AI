#!/usr/bin/env python3
"""
Write concept-focused narrative study material (no fixed section template).
Hand-authored modules are imported; others use rich per-slug prose.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_curriculum import STRUCTURE  # noqa: E402

NARRATIVE_DIR = Path(__file__).resolve().parent / "narrative_lib"


def load_module_narratives(name: str) -> dict[str, str]:
    path = NARRATIVE_DIR / f"{name}.py"
    if not path.exists():
        return {}
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, "NARRATIVES", {})


def prose_fallback(module: str, slug: str) -> str:
    title = slug.replace("-", " ").title()
    return f"""# {title}

This topic sits in **`{module}`**—part of the path from backend engineer to someone who can ship and operate AI systems in production.

## What to understand

**{title}** is not an isolated buzzword. In real architectures it shows up with explicit inputs and outputs, failure modes, and metrics. Before you adopt a vendor feature, you should be able to explain what would break if this component were misconfigured, undersized, or bypassed.

## How practitioners use it

Teams that succeed treat **{title}** like any other critical dependency: version it, test it, observe it, and limit blast radius (feature flags, rollbacks, tenant isolation). The model may be stochastic; your *platform* around it should not be accidental.

## Practical checklist

- Define one SLI (latency, quality, or error rate) for this layer.
- Document owner and on-call expectations.
- Add an integration test or eval case that fails when behavior regresses.
- Review security: what untrusted data touches this path?

## Go deeper

Pair this page with the matching project under `22-projects/` and your own BUILD_LOG notes when you implement something real.

---
Module: `{module}` · See [ROADMAP.md](../ROADMAP.md)
"""


def main() -> None:
    # Map folder prefix to narrative_lib file
    lib_map = {
        "00-foundations": "m00",
        "01-python-for-ai-engineering": "m01",
        "02-llm-fundamentals": "m02",
        "03-llm-apis": "m03",
        "04-prompt-engineering": "m04",
        "05-embeddings-and-vector-search": "m05",
        "06-rag": "m06",
        "07-agents": "m07",
        "08-mcp": "m08",
        "09-ai-frameworks": "m09",
        "10-evaluation": "m10",
        "11-fine-tuning": "m11",
        "12-model-serving": "m12",
        "13-gpu-and-accelerator-infrastructure": "m13",
        "14-kubernetes-for-ai": "m14",
        "15-ai-platform-engineering": "m15",
        "16-ai-infrastructure": "m16",
        "17-observability": "m17",
        "18-ai-security": "m18",
        "19-production-ai": "m19",
        "20-fde-engineering": "m20",
        "21-system-design": "m21",
        "23-interview-preparation": "m23",
        "24-research": "m24",
    }

    skip_write = {
        # hand-maintained on disk (this session)
        ("00-foundations", "ai-vs-ml-vs-dl-vs-genai"),
        ("00-foundations", "mental-models"),
        ("00-foundations", "probability-statistics-for-ai"),
        ("00-foundations", "linear-algebra-for-ai"),
        ("00-foundations", "optimization"),
        ("00-foundations", "information-theory"),
    }

    written = 0
    for module, slugs in STRUCTURE.items():
        lib = load_module_narratives(lib_map.get(module, ""))
        for slug in slugs:
            if (module, slug) in skip_write:
                continue
            path = ROOT / module / f"{slug}.md"
            if slug in lib:
                body = lib[slug]
            else:
                body = prose_fallback(module, slug)
            path.write_text(body, encoding="utf-8")
            written += 1
    print(f"Narrative pass wrote {written} files (00 foundations partially hand-authored).")


if __name__ == "__main__":
    main()
