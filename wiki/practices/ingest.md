---
type: practice
status: seed
created: 2026-04-20
updated: 2026-04-20
tags: [workflow, ingest]
aliases: [Source ingest]
source_count: 1
confidence: high
---

# Ingest

## Summary

Ingest is the process of turning a raw source into maintained wiki knowledge.

## Procedure

1. Read the source from `raw/` or a URL.
2. Create or update a source summary under `wiki/sources/`.
3. Extract entities, claims, examples, and relationships.
4. Update relevant concept/practice/tool/artifact pages.
5. Update [[artifacts/index-artifact|Index]].
6. Append to [[artifacts/log-artifact|Log artifact]].
7. Run `python3 scripts/wiki_lint.py`.

## Relationships

| Relation | Target | Note |
| --- | --- | --- |
| consumes | [[artifacts/source|Source]] | Sources are immutable evidence. |
| produces | [[artifacts/wiki-page|Wiki page]] | The wiki is updated after reading. |
| updates | [[artifacts/index-artifact|Index]] | New pages must be discoverable. |

## Evidence

- [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]] describes ingest as reading a source, summarizing it, updating pages, updating the index, and logging the operation.

## Open questions

- Should processed sources be physically moved from `raw/inbox/` to `raw/processed/`, or only tagged in source summary pages?
