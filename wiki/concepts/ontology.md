---
type: concept
status: seed
created: 2026-04-20
updated: 2026-04-20
tags: [ontology, schema]
aliases: [Domain model]
source_count: 1
confidence: high
---

# Ontology

## Summary

An ontology is a structured model of entity types and relationships. In this workspace, it organizes software-developer knowledge into pages such as concepts, practices, tools, artifacts, decisions, sources, and syntheses.

## Why it matters

The ontology prevents the wiki from becoming a pile of disconnected notes. It gives agents a repeatable way to file information and connect it to existing knowledge.

## Relationships

| Relation | Target | Note |
| --- | --- | --- |
| implemented-by | [[concepts/llm-maintained-wiki|LLM-maintained wiki]] | The wiki is the storage medium. |
| describes | [[concepts/software-engineering|Software engineering]] | The modeled domain. |
| uses | [[artifacts/index-artifact|Index]] | The index makes the model navigable. |

## Evidence

- [[sources/karpathy-llm-wiki|Karpathy LLM Wiki]] describes a schema document that makes an agent a disciplined wiki maintainer.

## Open questions

- Should relation statements eventually be exported to RDF/OWL, JSON-LD, or remain markdown-native?
