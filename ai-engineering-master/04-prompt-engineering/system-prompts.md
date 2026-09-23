# System Prompts

The system prompt is your **policy envelope**: persona boundaries, output format, safety posture, and what the model should do when uncertain.

## Separation of concerns

Do not bury dynamic facts (user name, tenant config) in the static system block—those belong in structured user/context messages so you can audit and redact per tenant.

## Versioning

Store system prompts in git (or prompt registry) with semver. Roll out via feature flag: 5% traffic on `system_v3`, compare metrics, then promote.

## Over-constraint risk

Stacking fifty rules causes **rule collision**—the model satisfies the loudest instruction. Prefer a short hierarchy: safety > format > style.

## Go gateway pattern

```go
type PromptBundle struct {
    SystemID string // registry key
    Tools    []ToolDef
}
// Resolve SystemID → text at request time; never trust client-supplied system text in prod
```
