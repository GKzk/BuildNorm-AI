# BuildNorm AI — Architecture

## Architectural style

Use a modular monolith for the MVP. Keep clear boundaries between API, document ingestion, retrieval, answer generation, and verification. Avoid microservices until measured load or team size justifies them.

## Components

- Frontend: React + TypeScript (planned)
- API: FastAPI
- Relational data: PostgreSQL
- Vector retrieval: Qdrant
- File storage: S3-compatible object storage in production; local volume in development
- Document processing: text extraction, layout-aware parsing, OCR fallback
- LLM gateway: provider-neutral adapter
- Background jobs: add a queue when ingestion workloads require it

## Request flow

1. Authenticate user and resolve tenant/workspace.
2. Classify the question and extract exact identifiers (document numbers, clauses, dates).
3. Retrieve candidates using lexical and semantic methods.
4. Apply metadata filters for document type, edition, status, jurisdiction, and effective date.
5. Rerank candidates and assemble source context.
6. Generate a structured answer from retrieved evidence only.
7. Validate citations against stored document and clause IDs.
8. Return answer, evidence, edition metadata, and limitations.

## Data model concepts

- documents: stable identity and bibliographic metadata
- document_editions: immutable edition/version records
- document_sources: source URL, access method, rights basis, retrieval timestamp, checksum
- document_sections: hierarchy of sections, clauses, tables, appendices
- chunks: retrieval units linked to exact source sections and page coordinates
- workspaces and memberships: tenant boundaries
- conversations and messages: user interaction history
- ingestion_jobs: processing state and errors
- audit_events: security and source-change history

## Retrieval strategy

Start with lexical retrieval plus dense semantic retrieval, then fuse/rerank results. Exact document identifiers, clause numbers, dates, and numeric expressions need special handling; semantic similarity alone is insufficient.

Qdrant supports hybrid and multi-stage retrieval:
- https://qdrant.tech/documentation/hybrid-queries/
- https://qdrant.tech/documentation/search/text-search/hybrid-search/

The first implementation may use Qdrant built-in text/BM25 capabilities. Add a separate search engine only if relevance tests demonstrate a need.

## Normative evidence contract

Every cited evidence item must contain a stable document ID, edition ID, clause/section ID where available, exact extracted text, page reference where available, source and rights metadata, and ingestion checksum.

The answer generator cannot invent citations. The API returns citations only from retrieved evidence records.

## Deployment and security

Local development uses Docker Compose for PostgreSQL and Qdrant. Production infrastructure must be selected after reviewing Russian data-localization, security, backup, and availability requirements.

- Keep secrets out of source control.
- Enforce tenant scoping in backend queries, not only frontend filtering.
- Authorize every file access.
- Audit uploads, downloads, deletion, and administrative source changes.
- Treat uploaded documents as untrusted input.
