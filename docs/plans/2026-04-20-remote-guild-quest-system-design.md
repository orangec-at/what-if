# Remote Guild Quest System Design

## Goal

Create a fun, lightweight what-if framework that helps the user become a strong candidate for remote-first companies as a frontend-based fullstack engineer.

The emotional goal matters as much as the career goal: the process should feel playful, experimental, and self-directed rather than heavy, anxious, or performative.

## Framing

The recommended frame is **Remote Guild Quest System**.

The user is not merely “job hunting.” They are preparing to enter a remote-first guild as a frontend/fullstack adventurer. Every week, they draw a what-if card, complete a small quest, and turn the result into reusable career loot.

This keeps the system fun while still producing serious hiring signals.

## North Star

> I am recognized as a frontend-based fullstack engineer who can own product slices end-to-end in a remote-first environment.

“Frontend-based fullstack” means the user leads from user experience and product feel, then connects whatever API, data model, auth, deployment, testing, or documentation is needed to ship the slice.

## Three capability axes

### Frontend Taste

Hiring signal: polished UI, interaction quality, React/Next.js structure, accessibility, performance awareness, product thinking.

Core what-if:

> What if one small interface could make a hiring manager feel my frontend taste in ten seconds?

### Fullstack Ownership

Hiring signal: the ability to connect UI, API, data, auth, error states, tests, and deployment into a coherent product slice.

Core what-if:

> What if a frontend engineer could prove they can own a feature end-to-end before the interview?

### Remote Trust

Hiring signal: async communication, decision logs, ambiguity reduction, clear progress updates, written tradeoffs, and low-friction collaboration across time zones.

Core what-if:

> What if I could prove remote trust before the first interview?

Remote Trust is the recommended first quest because remote-first companies often hire for collaboration confidence, not only code ability. Many candidates show code; fewer show how they think, communicate, and reduce ambiguity asynchronously.

## Core loop

1. **Draw the card** — choose one weekly what-if.
2. **Build tiny proof** — create a small artifact, not a grand project.
3. **Add remote signal** — write the async note, tradeoff log, PR summary, or demo script.
4. **Polish one visible thing** — improve only the most visible surface.
5. **Ship the loot** — convert the result into a portfolio item, GitHub link, resume bullet, interview story, or private wiki note.
6. **Log XP** — record what improved and pick the next what-if.

## What-if card shape

Each card should contain:

- Question
- Why this is fun
- Career signal
- 7-day quest
- Artifact
- XP
- Loot
- Next what-if

The system should reward evidence, not guilt. Studying is allowed, but every loop should end in an artifact.

## First quest

Recommended first quest:

> What if I could prove remote trust before the first interview?

Suggested artifact package:

- async feature proposal
- tradeoff note
- PR-style summary
- demo script
- portfolio-ready “How I work async” section

## Repository fit

This design belongs in the existing software developer ontology as a career-specific extension:

- `wiki/concepts/remote-first-frontend-fullstack-engineer.md`
- `wiki/concepts/remote-guild-quest-system.md`
- `wiki/practices/what-if-career-experiments.md`
- `wiki/syntheses/remote-first-career-quest-map.md`
- `templates/what-if-card.md`
- `wiki/decisions/2026-04-20-career-framework-direction.md`

`wiki/index.md` should gain a Career System section, and `wiki/log.md` should record the design addition.

## Constraints

- Keep the system playful and lightweight.
- Do not turn the framework into productivity theater.
- Do not require public posting by default; private artifacts are valid until the user chooses to share.
- Prefer one weekly artifact over large vague plans.
- Preserve the ontology contract: update index, update log, run lint.

## Success criteria

The initial framework succeeds if:

- The wiki has a reusable what-if career experiment practice.
- The user has a clear identity target for remote-first frontend-based fullstack roles.
- The first quest is obvious and emotionally light.
- Future work can turn each quest into resume bullets, portfolio sections, interview stories, and confidence evidence.
