# BuildNorm AI — Product Vision

## Product

BuildNorm AI is a Russian-language SaaS platform for searching, interpreting, and applying construction-related regulatory and technical documents.

## Target users

- Construction site managers and work supervisors
- Construction production/technical office engineers (ПТО)
- Construction control specialists
- Designers and chief project engineers
- Technical customers and construction managers

## Core value

Reduce time spent finding applicable requirements while making every normative claim traceable to a source, document edition, and exact clause.

## Product principles

1. Evidence before fluency: a plausible answer without a source is not a successful answer.
2. Applicability matters: distinguish document scope, dates, territory, and legal status.
3. Preserve history: never silently overwrite an earlier edition.
4. Separate fact from analysis: direct requirements, derived conclusions, recommendations, and assumptions must be labelled.
5. Respect rights: access and redistribution rights are tracked per source.
6. Isolate user data: one tenant must never access another tenant's files or conversations.

## MVP scope

- PDF ingestion for documents that may lawfully be processed
- Document metadata and edition registry
- Extraction of headings, clauses, tables, and page references where possible
- Hybrid retrieval
- Grounded answers with source citations
- Validation that cited source fragments exist in the indexed edition

Out of scope: automated legal conclusions, final design approvals, production structural calculations, DWG/BIM semantic analysis, automatic regulatory publication, and training a foundation model from scratch.

## Success measures

- Retrieval precision on a reviewed engineering test set
- Citation validity
- Edition/status correctness
- Rate of unsupported normative claims
- User-reported time saved
- Conversion from pilot to paid use
