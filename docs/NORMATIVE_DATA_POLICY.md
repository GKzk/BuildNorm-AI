# Normative Data Policy

## Purpose

BuildNorm AI must not treat every publicly reachable PDF as freely reusable commercial content.

## Source record

For every imported document edition, record:
- Official title and designation
- Issuing or approving authority
- Official source URL or licensed provider
- Source retrieval date
- Edition and amendments represented by the file
- Checksum of the original file
- Legal basis or licence permitting storage, processing, display, and redistribution where applicable
- Restrictions and attribution requirements
- Review status

## Allowed ingestion states

- approved: rights basis reviewed; processing permitted within recorded limits
- metadata_only: metadata and official link may be stored; full text must not be redistributed
- internal_review: source is quarantined pending rights review
- blocked: processing or use is not permitted

Only approved sources may enter the general searchable full-text corpus. Other states must be enforced by ingestion and retrieval code.

## Edition integrity

- Never overwrite an edition file in place.
- Store a checksum for every source file.
- Link amendments to the edition they modify.
- Record effective dates separately from publication and approval dates.
- Preserve historical editions when legally permitted.
- Do not infer that a document is current merely because it is available online.

## Answer provenance

Every normative citation must resolve to a stored source record and edition. If source status or applicability is unknown, disclose that limitation.

## Operational rule

A human reviewer must approve new source classes and ingestion policies before bulk import. This document is an engineering policy, not a legal opinion; obtain qualified legal review before commercial launch.
