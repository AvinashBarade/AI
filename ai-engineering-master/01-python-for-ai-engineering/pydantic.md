# Pydantic for APIs and Structured LLM Output

Models emit text; your system needs **objects**.

```python
from pydantic import BaseModel, Field

class Citation(BaseModel):
    doc_id: str
    snippet: str

class Answer(BaseModel):
    text: str
    citations: list[Citation] = Field(default_factory=list)
```

Flow: ask model for JSON matching schema → `Answer.model_validate_json(raw)` → on failure, retry with error hint (max N times) → alert if failure rate spikes.

## Settings from environment

Use `pydantic-settings` for `Settings(BaseSettings)`—same idea as envconfig in Go.

## Security

Validation is not sanitization. Tool args still need **authorization** before touching production databases.
