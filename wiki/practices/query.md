---
type: practice
status: seed
created: 2026-04-20
updated: 2026-04-20
tags: [workflow, query]
aliases: [Wiki query]
source_count: 1
confidence: high
---

# Query

## Summary

Query is the process of answering a user question from the maintained wiki before falling back to raw sources or the web.

## Procedure

1. Read [[artifacts/index-artifact|Index]].
2. Search/read relevant pages.
3. Answer with links to pages and source summaries.
4. Distinguish source-backed facts from inference.
5. Save valuable durable answers under `wiki/syntheses/` or `wiki/questions/`.
6. Log multi-page or durable query work in [[artifacts/log-artifact|Log artifact]].

## Relationships

| Relation | Target | Note |
| --- | --- | --- |
| depends-on | [[artifacts/index-artifact|Index]] | Start from the catalog. |
| may-produce | [[artifacts/wiki-page|Wiki page]] | Good answers can become pages. |
| strengthens | [[concepts/knowledge-compounding|Knowledge compounding]] | Useful answers stay in the knowledge base. |

## Evidence

- [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]] says good answers should be filed back into the wiki when valuable.

## Open questions

- What threshold makes an answer worth saving as a durable synthesis?
