# Context Window

The context window is the maximum **tokens** (prompt + completion) the model can attend to in one forward pass. It is not “how much text we should stuff in.”

## Failure modes

- **Truncation:** drop start or end—often silently—breaking instructions or citations.
- **Lost in the middle:** salient facts buried in middle of long contexts get ignored statistically.
- **Cost explosion:** linear token billing.

## Mitigations

Summarize older chat turns; retrieve only top chunks; use smaller models to compress; store state externally (DB) instead of infinite history in prompt.

## Architecture

Track `context_tokens` metric per request; alert when p95 approaches limit; client-side pre-count before send.
