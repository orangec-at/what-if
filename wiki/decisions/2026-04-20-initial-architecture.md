---
type: decision
status: active
created: 2026-04-20
updated: 2026-04-20
tags: [decision, architecture]
aliases: [Initial architecture]
source_count: 1
confidence: high
---

# Initial Architecture

## Decision

Use a markdown-first, three-layer architecture: `raw/` for immutable sources, `wiki/` for LLM-maintained knowledge pages, and `ontology/` plus `AGENTS.md` for schema and operating rules.

## Context

The workspace started empty except for local OMX runtime state. The user requested an ontology system for software developers and asked the agent to read the LLM Wiki pattern before initial setup.

## Rationale

This structure is lightweight, inspectable, Obsidian-friendly, Git-friendly, and does not require a database or embedding pipeline at small scale.

## Relationships

| Relation | Target | Note |
| --- | --- | --- |
| implements | [[concepts/llm-maintained-wiki|LLM-maintained wiki]] | Instantiates the source pattern. |
| organizes | [[concepts/software-engineering|Software engineering]] | Domain focus. |
| depends-on | [[artifacts/index-artifact|Index]] | Navigation remains explicit. |

## Consequences

- Agents must update `wiki/index.md` and `wiki/log.md` as part of maintenance.
- Raw sources stay stable, so wiki claims can be audited.
- Advanced search can be added later without changing the basic folder contract.

## Evidence

- [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]] is the seed source for this architecture.
