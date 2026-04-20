# Remote Guild Quest System Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a playful what-if career framework to the software developer ontology so the user can pursue remote-first frontend-based fullstack roles through weekly artifact-producing quests.

**Architecture:** Extend the existing markdown ontology with two career concepts, one repeatable practice, one synthesis map, one decision record, and one reusable card template. Update `wiki/index.md` and `wiki/log.md`, then verify with `scripts/wiki_lint.py`.

**Tech Stack:** Markdown, YAML frontmatter, Obsidian-style wikilinks, Python standard-library lint script, Git.

---

### Task 1: Add career identity concept

**Files:**
- Create: `wiki/concepts/remote-first-frontend-fullstack-engineer.md`

**Step 1: Create the page**

Add a concept page defining the target identity: a remote-first frontend-based fullstack engineer who leads from UX/product and can own product slices end-to-end.

**Step 2: Include relationships**

Link to:
- `[[concepts/software-developer|Software developer]]`
- `[[concepts/software-engineering|Software engineering]]`
- `[[concepts/remote-guild-quest-system|Remote Guild Quest System]]`
- `[[practices/what-if-career-experiments|What-if career experiments]]`

**Step 3: Verify links later**

Run `python3 scripts/wiki_lint.py` after all pages are created.

### Task 2: Add framework concept

**Files:**
- Create: `wiki/concepts/remote-guild-quest-system.md`

**Step 1: Create the page**

Describe the Remote Guild Quest System: career preparation as weekly what-if quests that produce loot/artifacts.

**Step 2: Define game vocabulary**

Include definitions for:
- Quest
- XP
- Loot
- Boss fight
- Telemetry

**Step 3: Link to practice and synthesis**

Link to `what-if career experiments` and the quest map.

### Task 3: Add repeatable practice

**Files:**
- Create: `wiki/practices/what-if-career-experiments.md`

**Step 1: Create the procedure**

Document the weekly loop:
1. Draw the card
2. Build tiny proof
3. Add remote signal
4. Polish one visible thing
5. Ship the loot
6. Log XP

**Step 2: Include the first quest**

First quest: “What if I could prove remote trust before the first interview?”

**Step 3: Link to template**

Reference `templates/what-if-card.md` as the reusable card format.

### Task 4: Add synthesis map

**Files:**
- Create: `wiki/syntheses/remote-first-career-quest-map.md`

**Step 1: Create the map**

Map three capability axes:
- Frontend Taste
- Fullstack Ownership
- Remote Trust

**Step 2: Add initial quests**

Add at least five what-if quest seeds:
- Remote Trust
- Frontend Taste
- Fullstack Ownership
- Interview Boss Fight
- Rejection Alchemy

**Step 3: Distinguish source-backed vs inference**

State that the LLM Wiki structure is source-backed while career quest content is user-specific design inference.

### Task 5: Add card template

**Files:**
- Create: `templates/what-if-card.md`

**Step 1: Create reusable card sections**

Sections:
- Question
- Why this is fun
- Career signal
- 7-day quest
- Artifact
- XP
- Loot
- Next what-if

**Step 2: Keep it copyable**

Do not overbuild metadata; this should be easy to use weekly.

### Task 6: Add decision record

**Files:**
- Create: `wiki/decisions/2026-04-20-career-framework-direction.md`

**Step 1: Record decision**

Decision: use Remote Guild Quest System as the career framework.

**Step 2: Record rejected alternatives**

Rejected:
- pure productivity tracker
- pure game skin
- pure public creator mode

### Task 7: Update index and log

**Files:**
- Modify: `wiki/index.md`
- Modify: `wiki/log.md`

**Step 1: Add Career System section to index**

Include links to the new concept, practice, synthesis, and decision pages.

**Step 2: Append setup entry to log**

Use heading:

```markdown
## [2026-04-20] setup | Add Remote Guild Quest System
```

### Task 8: Verify and commit

**Files:**
- All changed files

**Step 1: Run lint**

Run:

```bash
python3 scripts/wiki_lint.py
```

Expected:

```text
Unresolved wikilinks: 0
Index omissions: 0
Orphan pages: 0
```

**Step 2: Review git status**

Run:

```bash
git status --short
```

Expected: only planned files changed.

**Step 3: Commit**

Use a Lore-style commit message explaining why the framework exists and what verification was run.
