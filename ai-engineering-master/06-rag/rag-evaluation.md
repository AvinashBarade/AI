# RAG Evaluation

Split metrics:

**Retrieval:** recall@k, MRR, nDCG on labeled relevant chunk IDs.

**Generation:** faithfulness (answer supported by context?), answer relevance, citation correctness.

LLM-as-judge is tempting—calibrate against human labels on a slice; judges inherit model biases.

CI gate: fail if faithfulness drops >X% vs baseline on frozen golden set.
