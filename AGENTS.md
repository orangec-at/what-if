# Software Developer Ontology Agent Contract

This file is the schema layer for this workspace. It governs how agents maintain a software-developer ontology using the LLM Wiki pattern: immutable raw sources, an LLM-maintained wiki, and an explicit schema/workflow contract.

System, developer, and direct user instructions outrank this file. If those instructions conflict with this contract, follow the higher-priority instruction and record the deviation in `wiki/log.md` when relevant.

## Mission

Maintain a persistent, compounding ontology for software developers. The ontology should help answer questions such as:

- What concepts, practices, tools, artifacts, and risks matter in software engineering?
- How do practices trade off against each other?
- Which sources support or challenge a claim?
- What should a developer learn, decide, test, or revisit next?

The human curates sources and asks questions. The agent performs the bookkeeping: summarizing, cross-linking, updating pages, flagging contradictions, and keeping the index/log current.

## Architecture

### 1. Raw sources: `raw/`

- Raw sources are the source of truth.
- Treat files under `raw/` as immutable unless the user explicitly asks for cleanup or relocation.
- Preferred flow:
  - `raw/inbox/` for unprocessed sources.
  - `raw/processed/` for sources that have been summarized into the wiki.
  - `raw/assets/` for local images or attachments referenced by sources.
- Never overwrite source evidence to fit the wiki. If the wiki disagrees with a source, update the wiki and log the contradiction.

### 2. Wiki: `wiki/`

- The wiki is LLM-maintained markdown.
- Use Obsidian-style links: `[[concepts/software-engineering|Software engineering]]`.
- Every durable page should include YAML frontmatter unless it is a lightweight placeholder.
- Read `wiki/index.md` first when answering wiki questions.
- Append every ingest/query/lint/architecture-changing action to `wiki/log.md`.

### 3. Ontology schema: `ontology/`

- `ontology/schema.md` explains the model.
- `ontology/entity-types.md` lists allowed page/entity types.
- `ontology/relation-types.md` lists relationship verbs.
- `ontology/schema.json` is the machine-readable seed schema.
- Evolve the schema conservatively. Prefer adding a relation note before inventing a new relation type.

## Page conventions

Use this frontmatter pattern when applicable:

```yaml
type: concept | practice | tool | artifact | source | decision | synthesis | question | lint-report
status: seed | draft | active | superseded
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [software-engineering]
aliases: []
source_count: 0
confidence: low | medium | high
```

Content sections should usually include:

1. `## Summary`
2. `## Why it matters`
3. `## Relationships`
4. `## Evidence`
5. `## Open questions`

Use `Evidence` to distinguish sourced claims from agent inference.

## Entity types

Primary wiki entity types:

- `concept`: idea or mental model, e.g. `technical debt`.
- `practice`: repeatable activity, e.g. `code review`.
- `tool`: product, library, language, framework, runtime, CLI, or service.
- `artifact`: produced object, e.g. `test suite`, `ADR`, `API contract`.
- `principle`: normative guidance, e.g. `prefer deletion over addition`.
- `quality-attribute`: system property, e.g. `reliability`, `maintainability`.
- `risk`: failure mode, hazard, or tradeoff.
- `decision`: recorded choice and rationale.
- `source`: source summary page connected back to `raw/` or a URL.
- `synthesis`: cross-page answer, map, comparison, or thesis.
- `question`: durable user question and answer when worth preserving.

## Relationship verbs

Use these verbs in `Relationships` sections and tables:

- `is-a`
- `part-of`
- `depends-on`
- `enables`
- `constrains`
- `implements`
- `tested-by`
- `mitigates`
- `trades-off-with`
- `supersedes`
- `contradicts`
- `evidence-for`
- `observed-in`
- `asked-by`
- `answered-by`

If a relation does not fit, describe it in prose and consider updating `ontology/relation-types.md` after a lint pass.

## Ingest workflow

When the user asks to ingest a source:

1. Read the source from `raw/` or the provided URL/path.
2. Create or update a source summary in `wiki/sources/<slug>.md`.
3. Extract software-developer entities and relationships.
4. Update affected concept/practice/tool/artifact pages.
5. Mark contradictions explicitly instead of smoothing them away.
6. Update `wiki/index.md` with new/changed pages.
7. Append `## [YYYY-MM-DD] ingest | <title>` to `wiki/log.md`.
8. Run `python3 scripts/wiki_lint.py` and record notable results.

## Query workflow

When answering a question against the ontology:

1. Read `wiki/index.md`.
2. Search/read relevant pages.
3. Answer with links to wiki pages and source pages.
4. Clearly label source-backed facts vs. inference.
5. If the answer is durable, save it as `wiki/syntheses/<slug>.md` or `wiki/questions/<slug>.md`.
6. Append `## [YYYY-MM-DD] query | <question>` to `wiki/log.md` when a durable page is created or multiple pages are updated.

## Lint workflow

Periodically run:

```bash
python3 scripts/wiki_lint.py
```

Then inspect for:

- unresolved wikilinks,
- orphan pages with no inbound links,
- pages missing from `wiki/index.md`,
- stale or superseded claims,
- contradictions between pages,
- important terms without pages,
- source summaries that do not point back to raw evidence or URLs.

Save substantive lint reports under `wiki/lint/YYYY-MM-DD-<topic>.md` and log them.

## Index and log rules

- `wiki/index.md` is content-oriented. Keep it organized by category with one-line summaries.
- `wiki/log.md` is chronological and append-only.
- Use parseable log headings:

```markdown
## [YYYY-MM-DD] ingest | Source title
## [YYYY-MM-DD] query | Question summary
## [YYYY-MM-DD] lint | Scope
## [YYYY-MM-DD] setup | Change summary
```

## Git and verification

- Keep `.omx/` out of Git; it is runtime state, not ontology content.
- Run `python3 scripts/wiki_lint.py` before claiming wiki maintenance is complete.
- Use Lore-style commit messages for commits: intent line first, then useful trailers such as `Tested:` and `Not-tested:`.
