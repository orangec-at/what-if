---
type: source
status: active
created: 2026-04-20
updated: 2026-04-20
tags: [source, llm-wiki, knowledge-management]
aliases: [LLM Wiki gist, Karpathy LLM Wiki]
source_count: 1
confidence: high
source_url: https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md
---

# Karpathy LLM Wiki

## Summary

This source describes a pattern for building personal knowledge bases with LLM agents. Instead of treating documents as a query-time retrieval corpus only, the agent incrementally maintains a persistent markdown wiki that compounds over time.

## Key takeaways

- Use three layers: immutable raw sources, an LLM-written wiki, and a schema/agent-instruction document.
- Ingest should summarize sources, update related pages, update the index, and append to the log.
- Query answers can become new durable wiki pages when they contain reusable synthesis.
- Lint should find contradictions, stale claims, orphan pages, missing cross-references, and data gaps.
- `index.md` is content-oriented; `log.md` is chronological and append-only.
- Obsidian can act as the IDE for browsing and graphing the wiki.

## Relationships

| Relation | Target | Note |
| --- | --- | --- |
| evidence-for | [[concepts/llm-maintained-wiki|LLM-maintained wiki]] | Defines the main pattern. |
| evidence-for | [[practices/ingest|Ingest]] | Describes ingest operations. |
| evidence-for | [[practices/query|Query]] | Describes query and filing answers back. |
| evidence-for | [[practices/lint|Lint]] | Describes health-checking the wiki. |
| evidence-for | [[artifacts/index-artifact|Index]] | Explains index purpose. |
| evidence-for | [[artifacts/log-artifact|Log artifact]] | Explains log purpose. |

## Evidence

- Source URL: <https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md>
- Read during initial setup on 2026-04-20.

## Open questions

- Which optional tooling should this workspace add after the markdown-only baseline: local search, MCP search, Obsidian Dataview, or RDF/JSON-LD export?
