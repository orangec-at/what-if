---
type: artifact
status: seed
created: 2026-04-20
updated: 2026-04-20
tags: [artifact, navigation]
aliases: [Index]
source_count: 1
confidence: high
---

# Index

## Summary

The index is the content-oriented catalog of the wiki. Agents should read it before answering ontology questions.

## Relationships

| Relation | Target | Note |
| --- | --- | --- |
| indexes | [[artifacts/wiki-page|Wiki page]] | Lists pages by category. |
| supports | [[practices/query|Query]] | Query starts from the index. |
| updated-by | [[practices/ingest|Ingest]] | New pages must be added. |

## Evidence

- [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]] recommends `index.md` as the catalog that the LLM reads first.
