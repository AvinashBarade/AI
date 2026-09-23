# LangChain

LangChain is a **composition library**: chains, retrievers, tool wrappers, vector store adapters.

## Strengths

Fast prototyping; huge integration catalog.

## Weaknesses

Abstraction leakage; version churn; easy to build spaghetti without tests.

## Staff advice

Use pieces (retriever interface), not opaque “agents in a box,” until you understand raw HTTP + your eval harness.
