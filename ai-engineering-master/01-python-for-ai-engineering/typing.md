# Typing in Python AI Services

Types are how you survive **LLM JSON** and large teams. Use them at service boundaries.

```python
from typing import Protocol

class Retriever(Protocol):
    def search(self, query: str, tenant_id: str, k: int) -> list[str]: ...
```

Run `pyright` or `mypy` on `services/` in CI—same discipline as Go compile errors.

## Pydantic overlaps typing

For HTTP and model outputs, Pydantic gives runtime validation + JSON schema. Dataclasses alone won’t save you from malformed tool arguments.

## Interview angle

“How do you validate structured LLM output?” → schema + parse + bounded retries + metric on validation failures.
