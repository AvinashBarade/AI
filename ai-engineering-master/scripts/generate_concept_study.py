#!/usr/bin/env python3
"""Regenerate all study markdown as concept-based material."""
from __future__ import annotations

from pathlib import Path

from concept_knowledge import MODULE_BLURB, get, related_links, titleize
from generate_curriculum import PROJECTS, STRUCTURE

ROOT = Path(__file__).resolve().parents[1]


def interview_block(title: str, slug: str) -> str:
    t = title.lower()
    return f"""
### Level 1
1. Define **{title}** in plain language.
2. Where does {t} sit in the AI stack?
3. Name one metric that indicates {t} health.
4. Name one security concern for {t}.
5. What breaks if you ignore {t} in production?

### Level 2
1. How does {t} affect token cost?
2. How does {t} interact with multi-tenancy?
3. Design a minimal test for {t} in CI.
4. Compare two alternatives to {t}.
5. What telemetry spans should include {t}?

### Senior
1. Design {t} for 5k RPS with per-tenant quotas.
2. How do you roll back a bad change to {t}?
3. Write an SLO for {t}.
4. Incident: quality dropped but error rate is zero—debug plan.
5. Build vs buy for {t}?

### Staff
1. Standardize {t} across 15 product teams—what is platform vs product ownership?
2. Cost model including {t} at scale.
3. Regulatory constraints on {t} (PII, residency).
4. Roadmap trade-off: {t} vs faster feature shipping.
5. Postmortem template involving {t}.

### FDE
1. Customer demands {t} in week 1—how do you scope?
2. Explain {t} to a non-technical executive in 60 seconds.
"""


def render_study(module: str, slug: str) -> str:
    k = get(module, slug)
    title = titleize(slug)
    blurb = MODULE_BLURB.get(module, "AI engineering")

    concepts_md = "\n".join(f"- {c}" for c in k["concepts"])
    failures = [
        f"Silent quality regression in {title.lower()} without metric movement.",
        "Timeout cascades upstream when downstream has no bounded retries.",
        "Tenant crossover due to missing metadata filters or shared caches.",
        "Cost blowout from unbounded context or runaway agent/tool loops.",
        "Tokenizer/model/index version skew between train and serve paths.",
        "Logging raw prompts containing secrets or PII.",
    ]
    failures_md = "\n".join(f"- {f}" for f in failures)

    debug = [
        "Confirm deployment version and feature flags.",
        "Inspect trace waterfall: gateway → app → retrieval → model.",
        "Slice metrics by tenant, model_id, and prompt length bucket.",
        "Replay failing request against staging with redacted fixtures.",
        "Compare offline eval set scores before/after change.",
    ]
    debug_md = "\n".join(f"- {d}" for d in debug)

    return f"""# {title}

> **Module:** `{module}` · **Focus:** {blurb}

---

## Core concepts (study these first)

{concepts_md}

## Concept relations

{related_links(module, slug)}

---

## 1. Mental Model

{k["mental"]}

## 2. Why This Exists

Teams invented **{title.lower()}** because shipping raw model calls does not scale organizationally: you need repeatable patterns for **quality, cost, safety, and operability** in {blurb}.

## 3. Problem It Solves

Without disciplined **{title.lower()}**, you get fragile demos—unmetered spend, untestable behavior, and incidents that show up first as angry users, not red dashboards.

## 4. Architecture

{k["architecture"]}

## 5. Internal Working

{k["internal"]}

## 6. Step-by-Step Flow

{k["flow"]}

## 7. Worked Example

{k["example"]}

## 8. Implementation

**Python (AI paths):** {k.get("impl", "FastAPI services, eval scripts, PyTorch/Hugging Face pipelines.")}

```python
# Pattern: validate → call → measure
from pydantic import BaseModel

class Request(BaseModel):
    tenant_id: str
    payload: str

async def handle(req: Request) -> dict:
    # apply {title.lower()} policy here
    return {{"status": "ok", "trace_id": "..."}}
```

**Go (platform paths):** gateways, workers, high-QPS routers.

```go
func Handle(ctx context.Context, tenant string, in []byte) error {{
    ctx, cancel := context.WithTimeout(ctx, 30*time.Second)
    defer cancel()
    // policy + metrics for {title.lower()}
    return nil
}}
```

## 9. Production Engineering

- Define **SLOs** (latency, error rate, quality proxy) for `{title.lower()}`.
- Version artifacts (prompts, indexes, models) and enforce compatibility in CI.
- Use **feature flags** and canaries; avoid big-bang changes to retrieval or routing.
- Document **runbooks** for provider outages and index lag.
- Align with your existing **Kubernetes / Terraform / CI** workflows—AI is not a separate ops universe.

## 10. Failure Modes

{failures_md}

## 11. Debugging Checklist

{debug_md}

## 12. Scaling

- Horizontal scale **stateless** tiers; partition tenant data at the index and secret layers.
- Queue bursty embedding/ingestion; autoscale GPU pools on queue depth (KEDA).
- Cache stable prefixes and frequent queries with tenant-scoped keys.

## 13. Security

- Treat user prompts, uploaded docs, and tool outputs as **untrusted input**.
- Default-deny tool permissions; audit privileged actions.
- Rotate keys via vault; never commit secrets; sign model artifacts.

## 14. Observability

- **Traces:** one `trace_id` across gateway, retrieval, model, tools.
- **Metrics:** QPS, latency histograms, token counters, GPU utilization, retrieval@k.
- **Logs:** structured, redacted; link to eval run IDs for regressions.

## 15. Cost

- Attribute **tokens and GPU seconds** per tenant for chargeback.
- Right-size models; compress context; batch embeddings; route easy queries to smaller models.

## 16. Trade-offs

| Choose {title} | Avoid / defer |
|----------------|---------------|
| Measurable quality or control need | One-off scripts without tests |
| Platform standardization | Every team reimplements policy |

## 17. When To Use

When requirements need **adaptability**, language-heavy reasoning, or rapid iteration—with explicit guardrails and evaluation.

## 18. When NOT To Use

When the problem is **fully deterministic**, safety-critical without human oversight, or solvable with classical ML/rules at lower cost.

## 19. Interview Questions

{interview_block(title, slug)}

## 20. Practical Exercise

1. Implement a minimal slice of **{title.lower()}** with unit tests.  
2. Add one Prometheus metric and one trace span.  
3. Write a one-page note: hypothesis → experiment → result.

## 21. Project Application

Map this topic to `22-projects/` (see repository README). Record outcomes in **BUILD_LOG.md**.

---

**See also:** [GLOSSARY.md](../GLOSSARY.md) · [ROADMAP.md](../ROADMAP.md) · [INTERVIEW_MASTER.md](../INTERVIEW_MASTER.md)
"""


def render_project_readme(folder: str, name: str, desc: str) -> str:
    return f"""# Project — {name}

{desc}

## Concepts this project practices

- End-to-end production engineering (not a demo chatbot)
- Observability, security, cost, and failure modes as first-class requirements
- Mapping `{folder}` topics to running code

## Architecture

```text
Client → API (Python/Go) → {{core}} → Model / Vector DB / Tools
              ↘ metrics/traces ↘ auth & quotas
```

## Deliverables

- [ ] README + ARCHITECTURE.md
- [ ] Implementation + tests
- [ ] Dockerfile / Helm or compose
- [ ] Prometheus metrics + OpenTelemetry traces
- [ ] SECURITY.md + FAILURE_MODES.md
- [ ] BUILD_LOG.md

## Study order

Complete related modules in ROADMAP before starting; revisit module **Core concepts** sections while building.
"""


def main() -> None:
    n = 0
    for module, slugs in STRUCTURE.items():
        d = ROOT / module
        d.mkdir(parents=True, exist_ok=True)
        for slug in slugs:
            path = d / f"{slug}.md"
            path.write_text(render_study(module, slug), encoding="utf-8")
            n += 1

    for folder, name, desc in PROJECTS:
        p = ROOT / "22-projects" / folder
        p.mkdir(parents=True, exist_ok=True)
        (p / "README.md").write_text(render_project_readme(folder, name, desc), encoding="utf-8")
        n += 1

    print(f"Wrote concept-based study material for {n} files.")


if __name__ == "__main__":
    main()
