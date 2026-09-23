# Narrative study material — 01-python-for-ai-engineering

NARRATIVES = {
    "python-for-go-engineers": """# Python for Go Engineers

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
""",
    "numpy": """# NumPy for AI Workloads

NumPy is **contiguous typed arrays** plus vectorized ops. Embeddings, batch similarity, and reading PyTorch tensors all pass through this mental model.

## Shapes matter more than syntax

A matrix of embeddings is `(num_vectors, dimension)`. A batch of sequences in deep learning is `(batch, seq, hidden)`—you’ll see that in error messages long before you train anything.

**Broadcasting** lets you combine arrays of different shapes without explicit loops—powerful and easy to misuse.

## The operation you’ll run constantly

Normalized rows + matrix multiply = cosine similarity search in brute-force form:

```python
import numpy as np

Q = queries / np.linalg.norm(queries, axis=1, keepdims=True)
D = docs / np.linalg.norm(docs, axis=1, keepdims=True)
scores = Q @ D.T
```

At millions of vectors you move this to Qdrant/Milvus—but you still prototype here.

## dtypes

`float32` is the default for ML storage and GPU. `float64` wastes memory. Mixed precision (FP16/BF16) is a serving topic, but NumPy is where you first see dtype mistakes.

## Exercise

Generate 1,000 random unit vectors in 384-D. For 10 queries, print top-5 indices by dot product. That is retrieval without the database.
""",
    "pandas": """# Pandas for Eval and Data Wrangling

Pandas is how you manipulate **tables of eval results**—not how you serve online traffic.

Typical columns: `question_id`, `prompt_version`, `model`, `answer`, `faithfulness_label`, `latency_ms`, `tenant`.

## Patterns you’ll repeat

```python
import pandas as pd

df = pd.read_csv("eval_run_2025-09-24.csv")
summary = df.groupby("model")["faithfulness_label"].mean()
by_locale = df.groupby("locale")["faithfulness_label"].agg(["mean", "count"])
```

Join runs on `question_id` to diff models on the same golden set.

## Don’t do this in production APIs

Loading a DataFrame per request is an anti-pattern. Batch offline; serve results from Postgres or object storage.

## Tie-in to platform engineering

Version datasets like code: `golden_v3.parquet` in S3, hash in CI, fail PR if eval drops >2% vs baseline on that hash.
""",
    "typing": """# Typing in Python AI Services

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
""",
    "async-python": """# Async Python for LLM Apps

`async` helps when your service **waits on networks**—provider APIs, vector DB, rerankers—not when it crunches numbers.

## The pattern

```python
import asyncio
import httpx

sem = asyncio.Semaphore(5)

async def call_provider(client: httpx.AsyncClient, payload: dict) -> dict:
    async with sem:
        r = await client.post("/v1/chat/completions", json=payload, timeout=60.0)
        r.raise_for_status()
        return r.json()

async def run_many(payloads: list[dict]) -> list[dict]:
    async with httpx.AsyncClient() as client:
        return await asyncio.gather(*[call_provider(client, p) for p in payloads])
```

Semaphore = backpressure so you don’t trigger 429s across the whole fleet.

## When async is wrong

Embedding 50k documents with CPU numpy/torch in the event loop blocks everything. Use **batch jobs**, **Ray**, or **Go workers**.

## Link to Go

Your gateway can stay sync/threads; internal Python can be async. Boundaries matter more than dogma.
""",
    "pydantic": """# Pydantic for APIs and Structured LLM Output

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
""",
    "packaging": """# Packaging and Environments (uv, Docker)

Reproducible Python is non-negotiable for compliance and incident replay.

## Minimal layout

```text
services/rag-api/
  pyproject.toml
  src/rag_api/
  tests/
```

Lock dependencies. In Docker, multi-stage build: compile/install in builder, copy venv/site-packages to slim runtime.

## ML images

CUDA base images are huge. Split **training** images from **API** images that only call remote models.

## Monorepo with Go

```text
/gateway-go
/services/rag-python
/infra/terraform
```

CI matrix: `go test ./...` and `pytest` with shared lint rules.
""",
}
