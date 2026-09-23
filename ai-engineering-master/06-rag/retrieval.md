# Retrieval

Given query vector (and filters), return top-k chunk IDs and scores.

## Parameters

- **k:** higher improves recall, hurts precision and prompt size.
- **Score threshold:** return “I don’t know” when nothing passes.

## Diversity

MMR reduces redundant near-duplicate chunks in results.

## Observability

Log retrieved IDs and scores per request—first thing to inspect when answers go wrong.
