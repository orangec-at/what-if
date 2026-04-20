---
type: concept
status: seed
created: 2026-04-20
updated: 2026-04-20
tags: [llm-wiki, knowledge-management]
aliases: [LLM Wiki]
source_count: 1
confidence: high
---

# LLM-Maintained Wiki

## Summary

An LLM-maintained wiki is a persistent markdown knowledge base that an agent updates as new sources and questions arrive. It sits between immutable raw sources and one-off answers.

## Why it matters

The wiki compounds. Cross-references, contradictions, and syntheses are maintained once, then reused instead of rediscovered from raw documents for every query.

## Relationships

| Relation | Target | Note |
| --- | --- | --- |
| depends-on | [[artifacts/source|Source]] | Raw evidence remains the source of truth. |
| produces | [[artifacts/wiki-page|Wiki page]] | The agent writes maintained pages. |
| maintained-by | [[tools/codex|Codex]] | This workspace is maintained by a coding agent. |
| enables | [[concepts/knowledge-compounding|Knowledge compounding]] | Durable synthesis accumulates. |

## Evidence

- [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]] is the seed source for this page.

## Open questions

- At what size should this workspace add search tooling beyond `wiki/index.md` and shell search?
