# Structured Output

Downstream code wants **JSON**, not prose with markdown fences.

Strategies:

1. **Prompting** with schema description (weakest alone).
2. **JSON mode / response_format** from provider.
3. **Constrained decoding** (grammar, outlines) when available.
4. **Parse + validate + repair** with Pydantic (always).

```python
from pydantic import BaseModel

class Ticket(BaseModel):
    title: str
    priority: int
```

Retry loop: on `ValidationError`, send model the error message and ask for correction—cap attempts (3) and metric failures.

## Security

Structured output does not prevent **wrong** content—only well-typed wrong content.
