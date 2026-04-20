#!/usr/bin/env python3
"""Lightweight health check for the markdown wiki.

Checks:
- unresolved Obsidian-style wikilinks: [[target]] or [[target|alias]]
- wiki pages missing from wiki/index.md
- orphan pages with no inbound wikilinks

Only unresolved links are hard failures. Index omissions and orphans are warnings
because young ontologies often have useful seed pages before the graph matures.
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
INDEX = WIKI / "index.md"
WIKILINK_RE = re.compile(r"(?<!!)(?:\[\[)([^\]]+)(?:\]\])")


def normalize_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    if target.startswith("wiki/"):
        target = target[len("wiki/") :]
    target = target.removeprefix("/")
    if target.endswith(".md"):
        target = target[:-3]
    return target


def wiki_pages() -> list[Path]:
    if not WIKI.exists():
        return []
    return sorted(p for p in WIKI.rglob("*.md") if p.is_file())


def build_key_map(pages: list[Path]) -> tuple[dict[str, Path], set[str]]:
    full_keys: dict[str, Path] = {}
    basename_counts: Counter[str] = Counter()
    for page in pages:
        rel = page.relative_to(WIKI).with_suffix("").as_posix()
        full_keys[rel] = page
        basename_counts[page.stem] += 1

    ambiguous = {name for name, count in basename_counts.items() if count > 1}
    for page in pages:
        if page.stem not in ambiguous:
            full_keys[page.stem] = page
    return full_keys, ambiguous


def extract_links(page: Path) -> list[str]:
    text = page.read_text(encoding="utf-8")
    return [normalize_target(match.group(1)) for match in WIKILINK_RE.finditer(text)]


def main() -> int:
    pages = wiki_pages()
    if not pages:
        print("wiki_lint: no markdown pages under wiki/", file=sys.stderr)
        return 1

    key_map, ambiguous = build_key_map(pages)
    unresolved: list[tuple[Path, str]] = []
    inbound: defaultdict[Path, int] = defaultdict(int)

    for page in pages:
        for target in extract_links(page):
            if not target or target.startswith("#"):
                continue
            resolved = key_map.get(target)
            if resolved is None:
                unresolved.append((page, target))
            else:
                inbound[resolved] += 1

    index_text = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    index_omissions = []
    for page in pages:
        rel = page.relative_to(WIKI).with_suffix("").as_posix()
        if rel in {"index", "log", "README"}:
            continue
        if rel not in index_text and page.stem not in index_text:
            index_omissions.append(rel)

    orphan_pages = []
    for page in pages:
        rel = page.relative_to(WIKI).with_suffix("").as_posix()
        if rel in {"index", "log", "README"}:
            continue
        if inbound[page] == 0:
            orphan_pages.append(rel)

    print("wiki_lint: scanned", len(pages), "markdown pages")

    if ambiguous:
        print("\nAmbiguous basename links; prefer full paths:")
        for name in sorted(ambiguous):
            print(f"  - {name}")

    if unresolved:
        print("\nUnresolved wikilinks:")
        for page, target in unresolved:
            rel = page.relative_to(ROOT).as_posix()
            print(f"  - {rel}: [[{target}]]")
    else:
        print("Unresolved wikilinks: 0")

    if index_omissions:
        print("\nIndex omissions (warnings):")
        for rel in index_omissions:
            print(f"  - {rel}")
    else:
        print("Index omissions: 0")

    if orphan_pages:
        print("\nOrphan pages (warnings):")
        for rel in orphan_pages:
            print(f"  - {rel}")
    else:
        print("Orphan pages: 0")

    return 1 if unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
