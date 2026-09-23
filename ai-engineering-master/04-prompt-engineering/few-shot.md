# Few-Shot Prompting

Few-shot means embedding **input→output exemplars** in the prompt so the model imitates the pattern.

## When it works

Classification with fuzzy boundaries, extraction to a fixed schema, tone matching for support macros.

## When it fails

Long examples blow the context window; contradictory examples teach the wrong policy; stale examples encode deprecated business rules.

## Engineering tips

- Keep examples **diverse** but **consistent** in label semantics.
- Put the hardest edge case in the set—models often interpolate naively.
- For production, consider **fine-tuning or constrained decoding** once the example set stabilizes—few-shot does not scale linearly with cost.

## Test

Swap example order (position bias is real). Remove one example at a time to see which actually carries signal.
