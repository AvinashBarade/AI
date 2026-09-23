# Attention

Attention answers: *for this token, which other tokens should influence its representation?*

Given queries \(Q\), keys \(K\), values \(V\):

\[
	ext{Attention}(Q,K,V)=	ext{softmax}\left(rac{QK^	op}{\sqrt{d_k}}ight)V
\]

Scale by \(\sqrt{d_k}\) so softmax doesn’t saturate when dimension grows.

## Causal masking (decoders)

Token at position \(i\) may not attend to \(j>i\). That enforces autoregressive generation: the future must not leak into the past during training/inference.

## Multi-head

Several attention operations run in parallel (different subspaces), concatenate, project. Heads let the model attend to different relationship types (syntax, coreference, etc.)—you reason at the block level, not per head in prod.

## FlashAttention (why infra cares)

Standard attention materializes large \(N	imes N\) score matrices in HBM. FlashAttention tiles computation to reduce memory traffic—enables longer context and larger batch on same GPU.

## Debug without attention maps

Ablate: shorten prompt, remove RAG chunks, swap model. Attention visualization is research tooling—not your first prod debugger.
