# Packaging and Environments (uv, Docker)

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
