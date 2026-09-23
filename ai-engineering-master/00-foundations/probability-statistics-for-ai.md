# Probability & Statistics for AI Engineering

You are not training to be a statistician. You need enough fluency to **read eval dashboards**, **gate releases**, and **push back on bogus metrics** in executive meetings.

## The one idea that changes how you see LLMs

A completion is a **draw from a distribution**. Temperature &gt; 0 means the same prompt can yield different answers. Your job in production is not “find the single correct string”—it’s **estimate how often the system is good enough** on the tasks that matter, with uncertainty.

That’s statistics.

## Precision, recall, and why “accuracy” lies

For imbalanced problems (fraud, rare intents, “answer is faithful” when most answers look fine):

- **Precision:** Of what we flagged positive, how many were truly positive? (Cost of false alarms.)
- **Recall:** Of all true positives, how many did we catch? (Cost of misses.)

F1 balances them. In RAG, people often split:

- **Retrieval:** did we fetch the right chunk? (recall@k, MRR, nDCG)
- **Generation:** is the answer supported by chunks? (faithfulness)

A model can retrieve well and still hallucinate connectors—or retrieve poorly and guess.

## Confidence intervals (practical version)

You run 200 eval questions and get 82% faithfulness. Is that better than last week’s 80%?

With small **n**, noise dominates. Use:

- Wilson or bootstrap intervals
- Report **n** and slice (locale, tenant, product line)

Don’t ship on +2% without knowing if it’s within noise.

## Bayesian intuition (one paragraph)

\[
P(\text{hypothesis} \mid \text{data}) \propto P(\text{data} \mid \text{hypothesis}) \cdot P(\text{hypothesis})
\]

In engineering terms: prior belief × evidence from logs/eval → updated belief. You won’t do integrals—you **will** say “this prompt change helped on support tickets but hurt on legal—because the slice moved.”

## Train / validation / test (still matters for ML components)

Even if the LLM is frozen, your **retriever**, **router**, and **prompt** are “trained” by iteration. Treat holdout sets like ML:

- Leakage (same question paraphrased in train and test) inflates scores.
- Multiple prompt experiments without correction → false positives.

## Quick Python: bootstrap a metric

```python
import random

def bootstrap_rate(labels: list[float], n=5000):
    n0 = len(labels)
    rates = []
    for _ in range(n):
        sample = [labels[random.randrange(n0)] for _ in range(n0)]
        rates.append(sum(sample) / n0)
    rates.sort()
    return sum(labels)/n0, rates[int(0.025*n)], rates[int(0.975*n)]

# labels: 1.0 faithful, 0.0 not
```

## What to do Monday

1. Pick one AI feature. Define **one precision-like** and **one recall-like** metric for it.
2. Freeze 100–500 golden questions. Never tune on them directly.
3. Add CI that fails if faithfulness drops more than X% vs baseline on the holdout.

## Interview sound bite

LLM outputs are random variables; we use labeled eval sets and confidence intervals to decide if a change is real, and we slice metrics because aggregate averages hide regressions on important cohorts.
