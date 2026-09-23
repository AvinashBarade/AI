# Python for Go Engineers

You are not learning Python to become a Python developer. You are learning enough to **read Hugging Face examples**, **ship a FastAPI RAG service**, and **own eval scripts**—while your Go code still carries auth, routing, and high-QPS paths.

## How to map what you already know

| Go | Python |
|----|--------|
| `struct` | `@dataclass` or Pydantic `BaseModel` |
| `if err != nil` | `try/except` (catch specific exceptions) |
| `context.Context` | `asyncio` cancellation + timeouts on `httpx` |
| `go mod` | `uv` / `poetry` + lockfile |
| goroutines | `asyncio.create_task` (I/O bound only) |

Indentation defines blocks—there are no braces. That annoys everyone once, then you stop fighting it.

## What to actually install

```bash
uv venv
uv pip install fastapi uvicorn pydantic httpx pytest
```

Never use system Python for projects. Treat `pyproject.toml` like `go.mod`.

## A minimal service pattern

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Ask(BaseModel):
    question: str

@app.post("/ask")
async def ask(body: Ask) -> dict:
    # call retrieval + LLM client here
    return {"answer": "..."}
```

Run: `uvicorn main:app --reload`

## Where Python lives in your AI architecture

```text
Go gateway (auth, limits, routing)
        ↓
Python RAG / eval / batch embedding workers
        ↓
Postgres / Qdrant / provider APIs
```

CPU-heavy embedding loops do **not** belong on the asyncio event loop—use a process pool or push work to Go/a job queue.

## Common footguns

- **GIL:** pure Python loops don’t parallelize across cores.
- **`eval()` on LLM JSON:** never.
- **Unpinned deps:** reproduce prod bugs impossible.

## What “done” looks like

You can open a vendor notebook, trace the data flow, add a typed FastAPI endpoint, and run `pytest` in CI—then go back to writing the gateway in Go.
