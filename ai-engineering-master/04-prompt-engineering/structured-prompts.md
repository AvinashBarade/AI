# Structured Prompts

Structured prompts force outputs into **machine-parseable shapes**: JSON Schema, XML tags, function arguments, or grammar-guided decoding.

## Why backends care

Downstream Go services should `json.Unmarshal` without regex surgery. Define schema in OpenAPI/Pydantic and mirror it in the prompt.

## Techniques

1. **Schema in prompt** + `response_format: json_schema` (where supported)
2. **Tool call only**—model never free-texts the answer
3. **Repair loop**—validate, feed errors back once (cap retries)

## Failure modes

- Partial JSON on stream—use non-streaming for transactional writes or incremental parsers with strict abort.
- Schema drift between prompt and validator—generate both from one source of truth.

```python
class InvoiceExtract(BaseModel):
    vendor: str
    total: Decimal
    line_items: list[LineItem]
```
