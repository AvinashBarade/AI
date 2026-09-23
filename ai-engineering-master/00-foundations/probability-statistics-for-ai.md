# Probability & Statistics for AI Engineering

You do not need to prove theorems—you need to **read metrics, design evals, and debug stochastic systems**.

## 1. Mental Model

**Probability** = language for uncertainty. **Statistics** = making decisions from finite noisy data.

**Visualize:** An LLM completion is a **sample** from a distribution shaped by weights, prompt, and sampling params—not a single “correct” return value.

---

## 2. Why It Exists

AI systems are noisy:

- Same prompt → different answers (temperature &gt; 0).
- Retrieval returns approximate neighbors.
- A/B tests on prompt changes need significance thinking.
- Classifiers have precision/recall trade-offs you must own in production.

---

## 3. Architecture

```text
  World (unknown P)          Experiment / logs           Decisions
        │                           │                        │
        ▼                           ▼                        ▼
   Data generating          Metrics & estimators      Ship / rollback
   process                  (mean, CI, tests)         thresholds
```

---

## 4. Internal Working

### Random variables

Discrete (token ID) or continuous (logit). **Expectation** \(\mathbb{E}[X]\) = long-run average.

### Key distributions

| Distribution | AI context |
|--------------|------------|
| Bernoulli / Binomial | Per-request success, click, “answer correct” in eval |
| Gaussian | Weight init, noise models; CLT for batch means |
| Categorical / Softmax | Next-token distribution |
| Poisson | Request arrivals (queueing intuition) |

### Bayes (engineering form)

\[
P(\text{hypothesis} \mid \text{data}) \propto P(\text{data} \mid \text{hypothesis}) \cdot P(\text{hypothesis})
\]

Used in: spam filters, some retrieval priors, **calibrated** confidence—not literal LLM “truth.”

### Estimators & variance

Sample mean of eval score is noisy with small \(n\). **Always report n and variance**, not just a single run.

---

## 5. Example

**RAG eval:** 200 questions, human labels “faithful” 82%.

- Point estimate: 0.82
- Wilson CI (conceptual): maybe [0.76, 0.87] at 95%
- If baseline was 0.80, don’t ship on 2% without more data or stratified slices.

---

## 6. Implementation

Bootstrap CI for a custom metric (Python):

```python
import random

def bootstrap_mean(scores: list[float], n_resamples: int = 5000) -> tuple[float, float, float]:
    means = []
    n = len(scores)
    for _ in range(n_resamples):
        sample = [scores[random.randrange(n)] for _ in range(n)]
        means.append(sum(sample) / n)
    means.sort()
    lo = means[int(0.025 * n_resamples)]
    hi = means[int(0.975 * n_resamples)]
    return sum(scores) / n, lo, hi

# faithfulness_labels: 1.0 or 0.0 per query
# mean, lo, hi = bootstrap_mean(faithfulness_labels)
```

Go engineer note: you'll implement similar in eval pipelines with fixed seeds for reproducibility.

---

## 7. Production Considerations

- **SLIs as random processes:** error rate over 5 minutes is a sample; alert on sustained shift, not one unlucky batch.
- **Imbalanced data:** fraud, rare intents—accuracy is misleading; use precision/recall/F1 or cost-weighted metrics.
- **Multiple comparisons:** testing 20 prompts → false positives; hold out sets or Bonferroni discipline.
- **Non-stationarity:** production traffic ≠ benchmark set.

---

## 8. Trade-offs

| Metric | Good for | Bad for |
|--------|----------|---------|
| Accuracy | Balanced classes | Rare events |
| Precision | When false positives costly | Ignores false negatives |
| Recall | When misses costly | Ignores false positives |
| F1 | Balance P/R | Single threshold |
| MRR / nDCG | Ranking quality | End-to-end answer quality alone |

LLM eval often needs **LLM-as-judge** + human audit—treat judge as biased instrument.

---

## 9. Debugging

- Metric jumped 10%: check **dataset version**, not just model.
- High variance across days: slice by locale, tenant, query length.
- “Eval says good, users angry”: offline set not representative—fix sampling.

---

## 10. Interview Questions

### Level 1

1. Mean vs median?
2. What is standard deviation?
3. Define precision and recall.
4. What is a confidence interval (intuition)?
5. Independent vs mutually exclusive?
6. What is conditional probability?
7. What is overfitting?
8. Train/validation/test split—why?
9. What is a histogram?
10. What does p-hacking mean?

### Level 2

1. Why accuracy fails for 1% positive class?
2. Explain ROC vs PR curve.
3. Bayesian vs frequentist—practical difference for you?
4. How many eval examples for ±3% at 95% CI (order of magnitude)?
5. Stratified sampling—when?
6. Difference between correlation and causation in A/B tests.
7. What is Simpson’s paradox?
8. How does temperature change a distribution?
9. Expected value of token cost per request?
10. MRR formula for retrieval?

### Senior

1. Design eval protocol for RAG with statistical rigor.
2. Online vs offline metrics disagreement—debug plan.
3. Multi-armed bandit for model routing—pros/cons.
4. Detect data drift without labels.
5. Sample size for comparing two prompts.
6. Bayesian optimization for hyperparameters—when worth it?
7. Calibrating classifier probabilities.
8. Causal inference for “did RAG help?”
9. Metrics for imbalanced agent success/failure.
10. Reporting metrics to executives without lying.

### Staff

1. Org-wide eval standards and CI gates.
2. Risk of LLM-as-judge bias by domain.
3. Experiment platform for AI features.
4. Ethics of synthetic eval data.
5. SLA vs SLO vs SLI for stochastic APIs.

### FDE

1. Customer demands “99% accuracy”—your response?
2. Prove pilot value with small sample.
3. Explain confidence intervals to legal/compliance.

### Explain in an interview (30s)

LLM outputs are samples from conditional distributions controlled by prompts and sampling; we use statistics to estimate quality from finite eval sets with confidence intervals, and to choose metrics aligned with business costs—precision/recall for retrieval, faithfulness rates for RAG—not a single accuracy number.

---

## 11. Practical Exercise

Take 50 prompts; run each 3 times at temperature 0.7; measure **answer exact-match rate** and **semantic similarity variance**. Write one paragraph on whether your metric is stable enough for CI gating.

---

## 12. Mini Project

**Eval stats microservice (Go):** POST `/compare` with two score arrays → returns mean delta, bootstrap CI, recommendation ship/hold. Unit test with fixed RNG seed.
