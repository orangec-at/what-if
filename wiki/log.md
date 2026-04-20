---
type: log
status: active
created: 2026-04-20
updated: 2026-04-20
tags: [log, maintenance]
aliases: [Ontology Log]
source_count: 1
confidence: high
---

# Log

Append-only timeline. Use headings that are easy to grep:

```bash
grep "^## \[" wiki/log.md | tail -5
```

## [2026-04-20] setup | Initialize software developer ontology

- Created the `raw/`, `wiki/`, `ontology/`, `templates/`, `scripts/`, and `docs/plans/` structure.
- Seeded the wiki from [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]].
- Defined initial entity and relation types for software-developer knowledge.
- Added `scripts/wiki_lint.py` for basic wikilink and index health checks.
