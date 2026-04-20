# Software Developer Ontology Initial Setup Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Turn this empty folder into a markdown-first, LLM-maintained ontology/wiki system for software developers.

**Architecture:** Follow the LLM Wiki pattern from Karpathy's gist: immutable `raw/` sources, generated `wiki/` pages, and a durable agent schema in `AGENTS.md`. Add an `ontology/` layer for software-developer entity types and relationship semantics, plus lightweight scripts for local health checks.

**Tech Stack:** Markdown, YAML frontmatter conventions, Obsidian-style wikilinks, Python standard library only, Git.

---

### Task 1: Create directory skeleton

**Files:**
- Create directories: `raw/inbox`, `raw/processed`, `raw/assets`, `wiki/{concepts,practices,tools,artifacts,decisions,sources,syntheses,questions,lint}`, `ontology`, `templates`, `scripts`, `docs/plans`
- Create placeholder files where directories should be tracked by Git.

**Steps:**
1. Create the directory tree.
2. Add short README files for `raw/`, `wiki/`, and `ontology/`.
3. Add `.gitkeep` placeholders in empty raw subdirectories.

### Task 2: Write the agent operating contract

**Files:**
- Create: `AGENTS.md`

**Steps:**
1. Capture the three-layer architecture: raw sources, wiki, schema/ontology.
2. Define source ingest, query, lint, and maintenance workflows.
3. Define page metadata, wikilink, citation, contradiction, and logging conventions.
4. Define software-developer ontology entity and relation types.

### Task 3: Seed the wiki and ontology

**Files:**
- Create: `README.md`
- Create: `wiki/index.md`, `wiki/log.md`, `wiki/syntheses/software-developer-ontology-overview.md`
- Create seed concept/practice pages under `wiki/concepts/` and `wiki/practices/`
- Create: `ontology/schema.md`, `ontology/entity-types.md`, `ontology/relation-types.md`, `ontology/schema.json`

**Steps:**
1. Write a user-facing quick start.
2. Seed index and log files.
3. Add concise initial pages for LLM-maintained wiki, ontology, software engineering, ingest, query, and lint.
4. Add machine-readable schema JSON for future automation.

### Task 4: Add reusable templates

**Files:**
- Create: `templates/source-summary.md`, `templates/concept.md`, `templates/practice.md`, `templates/decision.md`, `templates/query-synthesis.md`, `templates/lint-report.md`

**Steps:**
1. Use consistent YAML frontmatter.
2. Include relationship and evidence sections.
3. Keep templates short enough to copy during maintenance.

### Task 5: Add lightweight verification tooling

**Files:**
- Create: `scripts/wiki_lint.py`

**Steps:**
1. Implement a dependency-free Python script that checks markdown files under `wiki/`.
2. Report unresolved wikilinks, index omissions, and orphan pages.
3. Exit non-zero only for unresolved links so early ontology growth is not blocked by orphans.

### Task 6: Verify and snapshot

**Commands:**
- `python3 scripts/wiki_lint.py`
- `find . -maxdepth 3 -type f | sort`
- `git init` if this is not already a Git repo
- `git status --short`
- Commit with Lore-style message if Git identity is available.

**Expected:**
- Lint completes with no unresolved wikilinks.
- Initial files are visible and `.omx/` is ignored.
- Git repository exists with an initial commit or a clear note if commit is blocked by local Git identity.
