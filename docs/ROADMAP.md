# BuildNorm AI — Roadmap

## Phase 0 — Repository foundation

- [x] Initialize repository
- [x] Add product principles and initial architecture
- [x] Add FastAPI application and health endpoint
- [x] Add local PostgreSQL and Qdrant services
- [ ] Verify local setup on developer machine

## Phase 1 — Document registry and ingestion

- [ ] Define document and edition schemas
- [ ] Add database migrations
- [ ] Add document upload endpoint
- [ ] Add file checksum and metadata
- [ ] Extract PDF text with page references
- [ ] Add OCR fallback for scanned files
- [ ] Preserve headings, clauses, tables, and appendices where possible
- [ ] Track source provenance and rights basis

## Phase 2 — Retrieval

- [ ] Add embeddings adapter
- [ ] Create Qdrant collection and payload indexes
- [ ] Add lexical and dense retrieval
- [ ] Add exact matching for document numbers and clause identifiers
- [ ] Add metadata filters
- [ ] Build reviewed retrieval evaluation set

## Phase 3 — Grounded answers

- [ ] Add provider-neutral LLM interface
- [ ] Define strict answer schema
- [ ] Generate answers only from retrieved evidence
- [ ] Validate every citation against stored evidence
- [ ] Label direct requirements, analysis, recommendations, and unknowns
- [ ] Refuse when evidence is insufficient
- [ ] Evaluate answer grounding and citation correctness

## Phase 4 — Product experience

- [ ] Add React + TypeScript frontend
- [ ] Add authentication and workspaces
- [ ] Add chat history
- [ ] Add document/source viewer
- [ ] Add user document upload and access control
- [ ] Add basic usage limits

## Phase 5 — Closed beta

- [ ] Recruit pilot engineers
- [ ] Collect real questions and reviewed answers
- [ ] Measure retrieval and answer quality
- [ ] Test willingness to pay
- [ ] Fix critical security and reliability issues

## Release gates

Do not enable paid public use until source rights are reviewed, tenant isolation is tested, citations are validated, unsupported normative claims are measured, privacy terms are prepared, and backup/incident procedures exist.
