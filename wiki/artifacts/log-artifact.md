---
type: artifact
status: seed
created: 2026-04-20
updated: 2026-04-20
tags: [artifact, history]
aliases: [Log artifact]
source_count: 1
confidence: high
---

# Log Artifact

## Summary

The log is the chronological, append-only record of wiki activity: ingests, queries, lint passes, setup changes, and schema changes.

## Relationships

| Relation | Target | Note |
| --- | --- | --- |
| records | [[practices/ingest|Ingest]] | Ingest events should be logged. |
| records | [[practices/query|Query]] | Durable query work should be logged. |
| records | [[practices/lint|Lint]] | Lint findings should be logged when substantive. |

## Evidence

- [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]] recommends a parseable `log.md` with chronological headings.
