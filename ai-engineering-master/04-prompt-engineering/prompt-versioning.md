# Prompt Versioning

Treat prompts like **migrations**: named versions, diff review, rollback path, and telemetry tagged with `prompt_version`.

## Registry fields

- `id`, `semver`, `owner`, `model_constraints`, `eval_suite_id`, `deprecated_at`
- Hash of rendered template for reproducibility

## Deployment

Blue/green at the gateway: route tenant A to v2, tenant B stays v1 until eval passes.

## Observability

Dashboard: error rate and quality metrics **grouped by prompt_version**. Without this, a silent prompt edit looks like “the model got worse.”

## Anti-pattern

Editing production prompts in a vendor UI with no git history—fine for solo experiments, unacceptable for regulated workloads.
