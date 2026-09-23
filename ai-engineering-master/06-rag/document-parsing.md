# Document Parsing

Models read **text you extract**—not pretty PDF layouts. Garbage extraction → garbage chunks → confident wrong answers.

## Formats

- **HTML/Markdown:** preserve headings hierarchy for chunk boundaries.
- **PDF:** layout analysis; tables are hard—consider specialized parsers or human QA on samples.
- **DOCX:** styles map to structure.
- **Scanned PDF:** OCR adds errors—flag low-confidence regions.

## Tables and code

Tables flattened to plain text often lose semantics. Sometimes store table HTML or CSV sidecar metadata for retrieval filters.

## QA process

Sample 50 random pages per source; human rate “parse usable?” before full index.
