# AI vs ML vs DL vs GenAI

## 1. Mental Model

Think of **nested toolboxes**:

```text
AI        = machines that perform tasks requiring human-like intelligence (broad)
  ML      = systems that improve from data without explicit rule programming
    DL    = ML using deep neural networks (many layers)
      GenAI = DL models that generate content (text, images, code, …)
```

As a backend engineer: **GenAI is what you ship in 2024–2026 product stacks**; **ML** is the discipline behind ranking, fraud, and forecasting; **DL** is the implementation stack for embeddings and LLMs; **AI** is the umbrella term executives use.

**Visualize:** A product feature “Ask our docs” is **GenAI application** → often **RAG** → **embeddings (DL)** → **vector search (ML/IR)** → **API (your job)**.

---

## 2. Why It Exists

| Era | Problem | Approach |
|-----|---------|----------|
| Pre-ML | Hand-coded rules don’t scale (vision, language) | Expert systems, brittle |
| ML | Patterns in data too complex to code | Learn function \(f(x)\) from examples |
| DL | Raw pixels/tokens need hierarchical features | Neural nets + GPUs |
| GenAI | Users want open-ended generation, not just labels | Large autoregressive / diffusion models |

---

## 3. Architecture

```text
                    ┌─────────────────────────────────────┐
                    │           Application               │
                    │  (API, agent, RAG, UI, workflows)   │
                    └─────────────────┬───────────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              ▼                       ▼                       ▼
        ┌───────────┐           ┌───────────┐           ┌───────────┐
        │  GenAI    │           │ Classical │           │  Rules /  │
        │  (LLM)    │           │    ML     │           │  heuristics│
        └─────┬─────┘           └─────┬─────┘           └───────────┘
              │                       │
              ▼                       ▼
        ┌───────────┐           ┌───────────┐
        │ Deep      │           │ Features  │
        │ Learning  │           │ + models  │
        └───────────┘           └───────────┘
```

---

## 4. Internal Working (what each actually does)

### Machine learning

- **Input:** labeled or unlabeled dataset.
- **Process:** pick model family, loss, optimizer; train until validation metric stabilizes.
- **Output:** parameters \(\theta\) that map features → prediction.
- **Production:** batch or online inference; **data drift** breaks models silently.

### Deep learning

- **Input:** raw or lightly processed tensors (images, token IDs).
- **Process:** stacked layers learn representations; backprop computes gradients.
- **Output:** same as ML but features are learned, not hand-engineered.

### Generative AI (LLM focus)

- **Input:** token sequence (prompt).
- **Process:** autoregressive next-token prediction with billions of parameters.
- **Output:** continuation distribution; sampling yields text.
- **Production:** stochastic, expensive, needs guardrails—not a deterministic microservice.

---

## 5. Example

**Fraud detection (classical ML):** Features = transaction amount, velocity, merchant category → XGBoost → block/score. Eval = precision/recall on labeled fraud.

**Support bot (GenAI + RAG):** User question → embed → retrieve KB chunks → LLM generates answer with citations → log faithfulness eval. Eval = retrieval MRR + LLM-judge faithfulness.

Same company, different stacks; platform team may host **both**.

---

## 6. Implementation

Minimal contrast: sklearn-style classifier vs OpenAI-style completion (patterns only).

```python
# Classical ML (conceptual)
from sklearn.linear_model import LogisticRegression
# X_train, y_train = ...
clf = LogisticRegression().fit(X_train, y_train)
score = clf.predict_proba(X_test)

# GenAI (conceptual — API boundary you'll own in production)
import httpx

async def complete(prompt: str) -> str:
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://api.example.com/v1/chat/completions",
            json={"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}]},
            timeout=60.0,
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
```

Your Go gateway would wrap the HTTP call with auth, limits, and metrics—not reimplement the model.

---

## 7. Production Considerations

| Concern | Classical ML | GenAI |
|---------|--------------|-------|
| Latency | Often ms | Often seconds; streaming helps UX |
| Cost | CPU inference | Per-token $ + GPU if self-hosted |
| Correctness | Bounded output space | Open-ended; hallucination |
| Versioning | Model registry + features | Model + prompt + retrieval index |
| Security | Data poisoning | Prompt injection, tool abuse |
| Observability | Prediction distribution drift | Tokens, TTFT, eval scores |

---

## 8. Trade-offs

| Use ML/DL (non-LLM) when | Use GenAI when |
|----------------------------|----------------|
| Fixed labels, abundant labeled data | Language-heavy, varied phrasing |
| Strict latency/cost budgets on CPU | Quality worth token cost |
| Explainability via features | Flexibility beats perfect explainability |
| Determinism required | Probabilistic output acceptable with guardrails |

**Don’t** replace a calibrated fraud model with an LLM because “AI is newer.”

---

## 9. Debugging

- **Wrong problem class:** LLM used for numeric forecasting → use time-series ML.
- **GenAI “randomly wrong”:** often retrieval or prompt, not “model broken.”
- **ML degradation:** check data pipeline, feature null rate, label definition changes.

---

## 10. Interview Questions

### Level 1

1. Define AI, ML, DL, GenAI in one line each.
2. Is ChatGPT “AI” or “ML”?
3. What is supervised learning?
4. Name a non-LLM ML use case in backend systems.
5. What is a label?
6. What is training vs inference?
7. Why do LLMs need GPUs?
8. What is a foundation model?
9. What is fine-tuning vs pretraining?
10. What is a hallucination?

### Level 2

1. When would you not use an LLM for a classification task?
2. How does RAG relate to ML/DL/GenAI?
3. What is data drift?
4. Compare batch ML inference to LLM streaming APIs.
5. What is transfer learning?
6. Encoder vs decoder models?
7. What is self-supervised learning?
8. Why are embeddings considered ML?
9. What is a discriminative vs generative model?
10. How do you version a GenAI app vs a sklearn model?

### Senior

1. Design observability for mixed ML + LLM platform.
2. How do you gate releases for RAG vs traditional models?
3. Cost model for 1M daily LLM requests vs 1M XGBoost scores.
4. Compliance: when must data not leave region?
5. Build vs buy embedding model.
6. Multi-tenant isolation across model types.
7. Fallback when LLM provider is down.
8. How to A/B test prompts safely.
9. Explain catastrophic forgetting in fine-tuning.
10. When is rules engine still correct answer?

### Staff

1. Enterprise AI strategy: three workloads, three stacks—justify.
2. Org structure: platform vs product ML vs infra.
3. Technical debt of “LLM for everything” pilot.
4. Migration from keyword search to hybrid RAG at scale.
5. Risk framework for agents in regulated industry.
6. Build internal model vs API-only for 5-year horizon.
7. KPIs for AI platform team.
8. Standardize eval across business units.
9. Capacity planning GPUs vs API spend crossover.
10. How you’d audit vendor claims on “AI features.”

### FDE

1. Customer says “we want ChatGPT internally”—first three questions?
2. Map “automate invoices” to ML vs OCR vs LLM.
3. Pilot scope for 8-week FDE engagement.
4. Explain GenAI limits to a CFO without jargon.
5. Document classification: classical vs LLM—proposal?

### Explain in an interview (30s)

**GenAI** is a subset of deep learning focused on *creating* content by learning data distributions—LLMs predict next tokens at scale. It’s powerful for language tasks but needs retrieval, eval, and security layers in production, unlike most classical ML services that map fixed inputs to fixed output types.

**Deep dive:** Generative models model \(P(x)\) or conditional \(P(x|y)\); LLMs factorize text as token sequences; scale + data + compute yielded emergent instruction-following; production is mostly integration, not training from scratch.

---

## 11. Practical Exercise

Write a one-page **decision matrix** for your current employer: list 5 real features; for each, mark **Rules / ML / LLM / Hybrid** and justify with latency, cost, and risk.

---

## 12. Mini Project

**“Stack picker” CLI (Go):** Read YAML feature specs; output recommended stack + risks + observability checklist. No model calls—pure engineering judgment encoded as rules you can later replace with learned ranker.

---

## Knowledge Checkpoint

Without notes:

1. Why is GenAI not a replacement for all ML?
2. What changes in monitoring when you add an LLM?
3. Name three production components that are *not* the neural net but are required for GenAI apps.
