---
type: practice
status: seed
created: 2026-04-20
updated: 2026-04-20
tags: [workflow, maintenance]
aliases: [Wiki lint]
source_count: 1
confidence: high
---

# Lint

## Summary

Lint is the periodic health check for the ontology and wiki.

## Procedure

1. Run `python3 scripts/wiki_lint.py`.
2. Review unresolved links, index omissions, and orphan pages.
3. Look for contradictions, stale claims, missing concept pages, and weak evidence.
4. Save substantive reports under `wiki/lint/`.
5. Update [[artifacts/index-artifact|Index]] and [[artifacts/log-artifact|Log artifact]] when pages change.

## Relationships

| Relation | Target | Note |
| --- | --- | --- |
| checks | [[artifacts/wiki-page|Wiki page]] | Pages should link cleanly. |
| checks | [[artifacts/index-artifact|Index]] | Pages should be discoverable. |
| supports | [[concepts/knowledge-compounding|Knowledge compounding]] | Healthy links make accumulated knowledge reusable. |

## Evidence

- [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]] recommends checking contradictions, stale claims, orphan pages, missing cross-references, and data gaps.

## Open questions

- Which checks should remain warnings and which should become hard failures?
