# Python for Go Engineers

## 1. Mental Model

**Go:** compile-time types, explicit errors, goroutines + channels, one way to format.  
**Python:** runtime types, exceptions, `async`/`await` + threads for CPU-bound, batteries included for data/ML.

**Visualize:** Python is your **lab + glue** for models and eval; Go remains **gateway, workers, and control plane**. Same distributed systems instincts apply—Python just hides fewer footguns behind the compiler.

---

## 2. Why It Exists

The AI ecosystem (HF, PyTorch, eval notebooks, FastAPI prototypes) is Python-first. You need to:

- Read and modify training/eval scripts
- Ship FastAPI services that wrap models/APIs
- Parse JSON/YAML datasets safely
- Not fight the GIL on embedding batch jobs (use multiprocessing or offload to Go workers)

---

## 3. Architecture

```text
  Go services (gateway, jobs)     Python services (RAG API, eval)
           │                                    │
           └────────── HTTP / gRPC / queue ─────┘
```

---

## 4. Internal Working — Concept map

| Go | Python |
|----|--------|
| `struct` | `@dataclass` / Pydantic `BaseModel` |
| `interface` | `Protocol` / duck typing |
| `error` return | `try/except` |
| `go func()` | `asyncio.create_task` / `ThreadPoolExecutor` |
| `range` | `for x in xs` |
| `map[string]T` | `dict[str, T]` |
| slice | `list` |
| `make([]T, 0, n)` | `[]` or list comprehension |
| `context.Context` | `contextvars` + cancellation in asyncio |
| modules | packages + `__init__.py` |
| `go mod` | `uv` / `poetry` + `pyproject.toml` |

---

## 5. Example

Go handler vs FastAPI (same responsibility: proxy chat):

```go
// Go — excerpt pattern
func (h *Handler) Chat(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()
    // decode, validate, call provider, stream with flusher
}
```

```python
from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest) -> dict:
    async with httpx.AsyncClient(timeout=60.0) as client:
        r = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": "Bearer ..."},
            json={"model": "gpt-4o-mini", "messages": [{"role": "user", "content": req.message}]},
        )
        r.raise_for_status()
        return r.json()
```

---

## 6. Implementation — Idioms you must internalize

### Errors

```python
# Go: if err != nil { return err }
# Python: catch specific exceptions; never bare except in production

try:
    data = load_dataset(path)
except FileNotFoundError:
    logger.exception("dataset missing", extra={"path": path})
    raise
```

### Context managers (like defer)

```python
with open(path) as f:
    content = f.read()
# file closed — similar to defer close in Go
```

### List comprehensions (not loops for maps)

```python
scores = [row["score"] for row in rows if row["valid"]]
```

### `if __name__ == "__main__"` (main package)

```python
def main() -> None:
    ...

if __name__ == "__main__":
    main()
```

### Virtual environments

Always use `uv venv` or `poetry`—never system Python for projects.

```bash
uv venv
uv pip install fastapi uvicorn pydantic httpx
```

### Type hints (non-optional for services)

```python
def top_k(ids: list[str], k: int) -> list[str]:
    return ids[:k]
```

Run `mypy` or `pyright` in CI for services you maintain.

---

## 7. Production Considerations

| Topic | Guidance |
|-------|----------|
| Concurrency | `async` for I/O-bound API fan-out; **ProcessPool** for CPU embedding |
| GIL | CPU-heavy Python loops block one core—profile before optimizing |
| Dependencies | Pin versions; SBOM; watch typosquatting on PyPI |
| Observability | `structlog` + OpenTelemetry Python SDK |
| Config | Pydantic `Settings` from env (like viper pattern) |
| Security | No `eval()` on LLM output; validate with Pydantic |

---

## 8. Trade-offs

| Stay in Go | Use Python |
|------------|------------|
| Gateway, rate limits, auth | HF, torch, notebooks |
| High-throughput parsers you own | Quick eval iteration |
| Static binaries in minimal images | CUDA stacks in GPU images |

---

## 9. Debugging

- `import pdb; pdb.set_trace()` or IDE breakpoints
- `python -m asyncio` debug patterns for hung tasks
- `httpx` logging for provider issues
- `uv run python -c "import torch; print(torch.cuda.is_available())"` on GPU nodes

---

## 10. Interview Questions

### Level 1

1. List vs tuple?
2. What is `None`?
3. `async def` vs `def`?
4. What is pip/uv?
5. Dictionary comprehension example?

### Level 2

1. GIL impact on embedding batch job?
2. How to structure FastAPI project?
3. Pydantic vs dataclass?
4. Exception handling best practice?
5. How to call Go from Python or vice versa?

### Senior

1. Deploy FastAPI with gunicorn/uvicorn workers.
2. Memory leak debugging in long-running worker.
3. Monorepo: Go + Python CI matrix.

### Staff

1. Language split standards for AI platform org.
2. Supply chain security for Python ML images.

### Explain in an interview (30s)

I use Python where the ML ecosystem and iteration speed win—FastAPI services, eval harnesses, Hugging Face—and Go for high-scale control planes and gateways; both need typed boundaries, pinned deps, and observability, with CPU-heavy work kept out of the GIL via processes or Go workers.

---

## 11. Practical Exercise

Port a small Go HTTP handler you’ve written to FastAPI with Pydantic models, request ID middleware, and structured JSON logging. Match status codes and timeout behavior.

---

## 12. Mini Project

**Polyglot repo layout:**

```text
/services/gateway-go
/services/rag-api-python
/packages/eval-python
```

Add `docker-compose.yml` wiring both; shared OpenTelemetry collector.

---

## Go → Python cheat sheet (printable)

```text
var x int          →  x: int = 0
:=                 →  x = 1  (no :=)
make(chan T)       →  asyncio.Queue()
select             →  asyncio.wait FIRST_COMPLETED
sync.Mutex         →  threading.Lock (prefer asyncio single-thread)
json.Marshal       →  json.dumps / model.model_dump_json()
testing            →  pytest
table tests        →  @pytest.mark.parametrize
```

Next: [numpy.md](./numpy.md) (when published).
