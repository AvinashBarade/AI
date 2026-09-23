# 10-evaluation

NARRATIVES = {
    "llm-evaluation": """# LLM Evaluation

Evaluate **behavior on tasks**, not perplexity. Golden prompts with reference outputs or rubrics; track pass rate over time.

Split: capability (can it do X?) vs regression (did we break Y?).

CI: block deploy if golden set drops beyond tolerance.
""",
    "rag-evaluation": """# RAG Evaluation (Module 10)

Measure retrieval and generation separately—recall@k on chunk IDs, faithfulness of answers to retrieved text.

Build queries from real user logs (redacted) plus synthetic edge cases.
""",
    "agent-evaluation": """# Agent Evaluation (Module 10)

Simulated environments with mocked tools. Score task completion, illegal tool usage, and step count.

Inject tool failures to test recovery—not only happy paths.
""",
    "offline-evaluation": """# Offline Evaluation

Run before release on frozen datasets—cheap, repeatable, no user impact.

Watch for **label leakage** and stale corpora that no longer match prod traffic.
""",
    "online-evaluation": """# Online Evaluation

Shadow traffic, A/B prompts, or LLM-judge on sampled prod requests.

Guard privacy; sample rate; compare variants with same tenant mix.
""",
    "benchmarks": """# Benchmarks

MMLU, HumanEval, etc. inform **model shopping**, not your product SLA.

Always add **domain benchmarks**—generic scores miss RAG and tool workflows.
""",
    "hallucination": """# Hallucination

Fabricated facts when context is insufficient or model prior dominates.

Mitigate: retrieval, abstain training in prompt, citation requirement, faithfulness metrics—not one-shot “don't hallucinate.”
""",
    "faithfulness": """# Faithfulness

Answer supported by provided context? Critical for RAG compliance.

Automated checks: NLI models, LLM judge calibrated to humans, citation overlap metrics.
""",
    "relevance": """# Relevance

Did the response address the user question—even if faithful?

Pair with user thumbs-down and task-specific rubrics.
""",
    "evaluation-pipelines": """# Evaluation Pipelines

```text
dataset git → runner (nightly/PR) → metrics store → dashboard + gates
```

Version datasets like code; attribute runs to `model`, `prompt`, `index` versions.
""",
}
