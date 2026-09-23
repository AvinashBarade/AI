#!/usr/bin/env python3
"""Regenerate all topic markdown with concept-based study material."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_curriculum import STRUCTURE  # noqa: E402
from concept_render import render, titleize  # noqa: E402
from facts import get_fact  # noqa: E402


def main() -> None:
    n = 0
    for module, slugs in STRUCTURE.items():
        mod_path = ROOT / module
        mod_path.mkdir(parents=True, exist_ok=True)
        for slug in slugs:
            d = get_fact(module, slug)
            body = render(titleize(slug), module, d)
            (mod_path / f"{slug}.md").write_text(body, encoding="utf-8")
            n += 1
    print(f"Wrote {n} concept-based topic files.")


if __name__ == "__main__":
    main()
