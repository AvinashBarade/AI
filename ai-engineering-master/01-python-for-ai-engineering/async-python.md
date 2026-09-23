# Async Python for LLM Apps

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
