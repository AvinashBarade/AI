# Information Theory (Engineering Intuition)

You don’t need Shannon proofs. You need to understand **why cross-entropy shows up everywhere** and how **tokenization** affects cost.

## Surprise and cross-entropy

If a model assigns probability \(p\) to the true next token, the “surprise” is \(-\log p\). Average surprise over tokens is **cross-entropy**.

Training an LLM = make the model **less surprised** by real text on the training distribution.

**Perplexity** re-expresses that as “effective number of choices” per step: lower is better on a held-out set.

Product teams still need **task metrics**—low perplexity doesn’t mean your RAG bot is faithful.

## Tokenization is a codec

Text → sequence of subword IDs. Trade-offs:

- **Larger vocab** → fewer tokens per sentence, bigger embedding table.
- **Smaller vocab** → longer sequences, more compute per document.

That’s why identical English sentences can have different **API cost** across models/tokenizers.

## KL divergence (when you’ll hear it)

Measures extra bits needed if you use distribution \(Q\) to encode data from \(P\). Shows up in distillation, some alignment objectives, VAE stories.

Engineering translation: “How wrong is our approximate model compared to the teacher?”

## Bits, billing, and context stuffing

Every token you send is a carrier of information—and **you pay for carriers** whether or not the model uses them well. Stuffing 80k tokens of mediocre RAG chunks increases cost and can **reduce** usable signal (attention dilution).

## Quantization = throwing away information

INT8/INT4 weights discard precision for speed and VRAM. Usually fine for inference; always **re-eval** on your tasks after quant.

## Logprobs in APIs

Some providers return per-token log probabilities. Uses:

- anomaly detection (very low prob on formatted outputs)
- research / calibration

Risks: logging logprobs can log **PII**—treat like prompt logging.

## Mini experiment

Take 20 prompts. Record `len(tokenizer.encode(text))` vs character count. Correlate with your verbosity preference and **invoice**.

## Sound bite

LLMs are trained to minimize next-token surprise; production is about minimizing **cost per successful task** subject to quality and safety—which is not the same objective.
