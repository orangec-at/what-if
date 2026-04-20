---
type: artifact
status: seed
created: 2026-04-20
updated: 2026-04-20
tags: [artifact, source]
aliases: [Raw source]
source_count: 1
confidence: high
---

# Source

## Summary

A source is raw evidence: a file in `raw/`, a URL, a paper, a transcript, a screenshot, a diagram, or another input curated by the human.

## Relationships

| Relation | Target | Note |
| --- | --- | --- |
| summarized-by | [[artifacts/wiki-page|Wiki page]] | Source summaries live in `wiki/sources/`. |
| consumed-by | [[practices/ingest|Ingest]] | Ingest extracts claims and relationships. |
| evidence-for | [[concepts/llm-maintained-wiki|LLM-maintained wiki]] | Sources support wiki claims. |

## Evidence

- [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]] defines raw sources as curated documents that the LLM reads but does not modify.
