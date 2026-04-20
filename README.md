# Software Developer Ontology

This folder is a markdown-first ontology/wiki system for software developers. It instantiates Andrej Karpathy's **LLM Wiki** pattern for a software-engineering domain: keep raw sources immutable, let an LLM maintain the wiki, and encode operating rules in `AGENTS.md`.

## Folder map

| Path | Purpose | Owner |
| --- | --- | --- |
| `raw/` | Immutable source material: articles, notes, transcripts, diagrams, screenshots, PDFs, or pasted markdown. | Human curates; LLM reads only. |
| `wiki/` | LLM-maintained pages: concepts, practices, tools, artifacts, source summaries, decisions, syntheses. | LLM writes and updates. |
| `ontology/` | The domain model: entity types, relation types, schema JSON, naming rules. | LLM may evolve carefully and log changes. |
| `templates/` | Copyable page templates for future ingest/query/lint work. | LLM uses and updates. |
| `scripts/` | Small local tools that help maintain the wiki. | LLM may edit with verification. |
| `docs/plans/` | Setup and implementation plans for larger changes. | LLM writes before multi-step changes. |

## Quick start

1. Put a new source in `raw/inbox/`.
2. Ask the agent: `ingest raw/inbox/<file>`.
3. The agent should:
   - create a source summary in `wiki/sources/`,
   - update affected concept/practice/tool/artifact pages,
   - update `wiki/index.md`,
   - append a parseable entry to `wiki/log.md`,
   - run `python3 scripts/wiki_lint.py`.
4. Ask questions against the wiki. Valuable answers should become durable pages under `wiki/syntheses/` or `wiki/questions/`.

## Maintenance commands

```bash
python3 scripts/wiki_lint.py
find wiki ontology templates -maxdepth 3 -type f | sort
```

## Initial source

The setup is based on Karpathy's LLM Wiki pattern: a persistent, compounding markdown wiki maintained by an LLM between raw sources and user queries.

Source URL: <https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md>
