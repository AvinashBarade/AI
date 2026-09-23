# Temperature and Sampling

After the final layer you have a vector of **logits** over the vocabulary. Temperature \(T\) divides logits before softmax:

- **Low T** → peaked distribution → deterministic, factual tasks.
- **High T** → flat distribution → creative, risky for extraction.

## top-k and top-p (nucleus)

Restrict sampling mass to likely tokens—reduces bizarre tail tokens. Production configs often combine `temperature=0.2`, `top_p=0.9` for support bots.

## Eval discipline

Regression-test prompts at **fixed** sampling settings. Changing T between runs invalidates A/B comparisons.

## Reproducibility

Seeds help on some stacks; don’t rely on cross-provider identical outputs for tests.
