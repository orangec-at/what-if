# Ontology Schema

This ontology is markdown-native. It can later be exported to JSON-LD, RDF, or a graph database, but the initial source of truth is the wiki itself.

## Core model

A page represents an entity. A link represents a connection. A relationship table gives that connection semantic meaning.

```text
Page(entity) --relation verb--> Page(entity)
Claim --evidence-for--> Source summary --observed-in--> Raw source or URL
```

## Required maintenance behavior

- Add new entity pages only when the concept is durable enough to reuse.
- Prefer updating an existing page over creating near-duplicates.
- Record ambiguous or contested claims in `Open questions` or `Contradictions` sections.
- Use relation verbs from `relation-types.md` when possible.
- Keep `wiki/index.md` current.

## Naming

- Use lowercase kebab-case file names.
- Prefer singular nouns for concepts and artifacts: `technical-debt.md`, not `technical-debts.md`.
- Prefix dated decisions and lint reports with `YYYY-MM-DD-`.
- Use aliases in frontmatter for common synonyms.

## Evidence levels

- `high`: directly backed by one or more sources in `wiki/sources/`.
- `medium`: supported by established project context or common usage, but not yet source-rich.
- `low`: hypothesis, draft synthesis, or needs more evidence.

## See also

- `entity-types.md`
- `relation-types.md`
- `schema.json`
