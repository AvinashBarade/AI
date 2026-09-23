"""Render concept-based study markdown from structured topic dicts."""
from __future__ import annotations


def titleize(slug: str) -> str:
    return slug.replace("-", " ").title()


def render(title: str, module: str, d: dict) -> str:
    concepts = d.get("concepts", [])
    prod = d.get("production", [])
    pitfalls = d.get("pitfalls", [])
    interview = d.get("interview", [])
    concepts_md = "\n".join(f"- {c}" for c in concepts)
    prod_md = "\n".join(f"- {p}" for p in prod)
    pit_md = "\n".join(f"- {p}" for p in pitfalls)
    int_md = "\n".join(f"- {q}" for q in interview)
    extra = d.get("extra", "")
    bridge = d.get("bridge", "")
    code = d.get("code", "")

    return f"""# {title}

> **Module:** `{module}`

## Mental model

{d.get("mental", "")}

## Why we use this

{d.get("why", "")}

## Core concepts

{concepts_md}

## How it works

{d.get("how", "")}

## Example

{d.get("example", "")}

{code}

## If you come from Go / Kubernetes / platform engineering

{bridge}

## Production notes

{prod_md}

## Mistakes to avoid

{pit_md}

{extra}

## Interview quick hits

{int_md}

## Practice

{d.get("practice", "")}

---
**See also:** [ROADMAP.md](../ROADMAP.md) · [GLOSSARY.md](../GLOSSARY.md)
"""
