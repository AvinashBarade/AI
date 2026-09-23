# Information Theory for AI Engineering

## 1. Mental Model

Information theory quantifies **uncertainty** and **how much encoding/compression** a distribution allows.

**Visualize:** A confident next-token distribution (one token at 99%) needs few bits to transmit; a flat distribution over 50k tokens is **high entropy**—the model is “surprised” often.

---

## 2. Why It Exists

- **Cross-entropy loss** in LLMs is information-theoretic: expected bits to encode true token under model distribution.
- **Tokenization** balances vocabulary size vs sequence length (compression of text).
- **Rate–distortion:** quantization throws away information for smaller models/faster inference.
- **RAG:** reduces uncertainty about facts by injecting evidence.

---

## 3. Architecture

```text
  Source (text)  →  Tokenizer (codec)  →  Token sequence
                            │
                            ▼
                    Model predicts P(token | context)
                            │
                            ▼
              Loss ≈ cross-entropy H(data; model)
```

---

## 4. Internal Working

### Entropy

For discrete \(X\): \(H(X) = -\sum_x P(x)\log_2 P(x)\) bits.

High entropy = unpredictable. English text has redundancy → models exploit structure.

### Cross-entropy

\(H(P, Q) = -\sum_x P(x)\log Q(x)\). Training minimizes \(H(P_{\text{data}}, Q_{\theta})\).

**Perplexity** (common LLM metric): \(2^{H}\) or \(\exp(H_{\text{nats}})\)—“effective branching factor.”

### KL divergence

\(D_{KL}(P \| Q)\) measures extra bits if you use \(Q\) to encode \(P\). Appears in VAEs, some alignment objectives, distillation.

### Mutual information (intuition)

How much knowing \(X\) reduces uncertainty about \(Y\). Retrieval increases mutual information between answer and documents **if** retrieval is good.

---

## 5. Example

Two next-token distributions after prompt “Paris is the capital of”:

| Token | P (model A) | P (model B) |
|-------|-------------|-------------|
| France | 0.92 | 0.60 |
| Texas | 0.01 | 0.05 |
| … | … | … |

Model A lower cross-entropy on true token “France” → better calibration for that step. Production still needs end-task eval—not single-token loss.

---

## 6. Implementation

Compute perplexity from token log-probs (conceptual):

```python
import math

def perplexity(log_probs: list[float]) -> float:
    # log_probs: log P(token_i | context_i) for each token in sequence
    n = len(log_probs)
    return math.exp(-sum(log_probs) / n)

# Lower perplexity = model assigns higher probability to actual tokens
```

Tokenizer “compression” experiment:

```python
def chars_per_token(text: str, encode_fn) -> float:
    tokens = encode_fn(text)
    return len(text) / max(len(tokens), 1)
```

Compare BPE vs SentencePiece on your domain corpus.

---

## 7. Production Considerations

- **Logprobs in API:** some providers return token logprobs for monitoring calibration and detection; PII risk in logs.
- **Context length vs information:** stuffing 100k tokens doesn’t mean model **uses** all bits—attention budget and “lost in the middle.”
- **Compression + encryption:** embeddings are lossy summaries—not reversible; don’t treat as secure redaction.

---

## 8. Trade-offs

| More tokens (finer BPE) | Fewer tokens (larger vocab) |
|-------------------------|-----------------------------|
| Longer sequences, more compute | Shorter seq, larger embedding table |
| Better rare words | More OOV issues if vocab too small |

Quantization: fewer bits per weight → less information capacity → possible quality loss.

---

## 9. Debugging

- Sudden perplexity spike on holdout: data contamination or train/eval leak.
- RAG doesn’t help: retrieved chunks may add **noise** not information—measure retrieval precision.
- High entropy completions at low temperature: bug in sampling or broken logits.

---

## 10. Interview Questions

### Level 1

1. What is entropy (intuition)?
2. What is cross-entropy?
3. What is perplexity?
4. Why do LLMs predict tokens?
5. What is compression relation to tokens?
6. Bits vs nats?
7. What is redundancy in language?
8. Loss going down means what?
9. What is vocabulary size trade-off?
10. Random baseline perplexity ≈ ?

### Level 2

1. KL divergence intuition?
2. Mutual information and RAG?
3. Why log base 2 in bits?
4. Perplexity vs BLEU?
5. Label smoothing effect on loss?
6. How does temperature affect entropy of output?
7. Minimum description length intuition?
8. Information bottleneck (VAE)?
9. Rate-distortion in quantization?
10. Why eval perplexity on public sets can mislead?

### Senior

1. Use logprobs for anomaly detection on API.
2. Design metric combining retrieval MI proxy + answer quality.
3. Token accounting vs information content for billing fairness.

### Staff

1. Enterprise: storing logprobs and compliance.
2. Model distillation information argument.

### Explain in an interview (30s)

LLMs are trained to minimize cross-entropy, which is how many bits the model needs on average to predict the next token; perplexity is the exponential of that uncertainty. Tokenizers are codecs trading vocabulary size for sequence length, and production quality still needs task metrics beyond perplexity.

---

## 11. Practical Exercise

For 20 prompts, record average output length in tokens vs character count; correlate with user-rated verbosity. Discuss whether tokenizer choice affects **cost** more than **quality**.

---

## 12. Mini Project

Add **per-request perplexity proxy** to Project 01 chat API when logprobs available; dashboard P95 and alert on drift vs baseline week.
