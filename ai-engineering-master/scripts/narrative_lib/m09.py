# 09-ai-frameworks

NARRATIVES = {
    "langchain": """# LangChain

LangChain is a **composition library**: chains, retrievers, tool wrappers, vector store adapters.

## Strengths

Fast prototyping; huge integration catalog.

## Weaknesses

Abstraction leakage; version churn; easy to build spaghetti without tests.

## Staff advice

Use pieces (retriever interface), not opaque “agents in a box,” until you understand raw HTTP + your eval harness.
""",
    "langgraph": """# LangGraph

LangGraph models workflows as **graphs** with state—good fit for explicit agent control flow and checkpoints.

## When to adopt

You outgrew while-loops and need persistence, human interrupts, and replay.

## Ops

Compile graph once; test nodes in isolation; store state schema in git.
""",
    "llamaindex": """# LlamaIndex

LlamaIndex skews **data-centric RAG**: ingestion pipelines, indices, query engines.

Strong for document-heavy products; pair with your own gateway and eval—not a full platform alone.
""",
    "dspy": """# DSPy

DSPy treats prompts as **optimizable programs**—compile examples into prompts or small modules via search.

Interesting for teams with labeled data who want systematic prompt improvement beyond manual tinkering.

## Caveat

Optimization overfits small dev sets—hold out production-like eval before deploy.
""",
    "framework-tradeoffs": """# Framework Tradeoffs

| Need | Lean toward |
|------|-------------|
| RAG ingestion | LlamaIndex |
| Agent state machine | LangGraph |
| Glue + tools | LangChain pieces |
| Prompt optimization | DSPy |

**Default:** raw SDK + your Go gateway until pain is measured—frameworks don't replace observability or security.
""",
}
