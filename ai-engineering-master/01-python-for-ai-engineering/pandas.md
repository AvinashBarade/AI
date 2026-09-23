# Pandas for Eval and Data Wrangling

Pandas is how you manipulate **tables of eval results**—not how you serve online traffic.

Typical columns: `question_id`, `prompt_version`, `model`, `answer`, `faithfulness_label`, `latency_ms`, `tenant`.

## Patterns you’ll repeat

```python
import pandas as pd

df = pd.read_csv("eval_run_2025-09-24.csv")
summary = df.groupby("model")["faithfulness_label"].mean()
by_locale = df.groupby("locale")["faithfulness_label"].agg(["mean", "count"])
```

Join runs on `question_id` to diff models on the same golden set.

## Don’t do this in production APIs

Loading a DataFrame per request is an anti-pattern. Batch offline; serve results from Postgres or object storage.

## Tie-in to platform engineering

Version datasets like code: `golden_v3.parquet` in S3, hash in CI, fail PR if eval drops >2% vs baseline on that hash.
