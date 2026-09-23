#!/usr/bin/env python3
"""Verify all required curriculum paths exist."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

# Mirror generate_curriculum.STRUCTURE + projects + root
from generate_curriculum import STRUCTURE, PROJECTS  # noqa: E402

REQUIRED_ROOT = [
    "README.md",
    "ROADMAP.md",
    "PROGRESS.md",
    "GLOSSARY.md",
    "INTERVIEW_MASTER.md",
]

missing: list[str] = []
for f in REQUIRED_ROOT:
    if not (ROOT / f).exists():
        missing.append(f)

for module, slugs in STRUCTURE.items():
    for slug in slugs:
        p = ROOT / module / f"{slug}.md"
        if not p.exists():
            missing.append(str(p.relative_to(ROOT)))

for folder, _, _ in PROJECTS:
    p = ROOT / "22-projects" / folder / "README.md"
    if not p.exists():
        missing.append(str(p.relative_to(ROOT)))

if missing:
    print("MISSING:", len(missing))
    for m in missing[:50]:
        print(" ", m)
    if len(missing) > 50:
        print(" ...")
    sys.exit(1)

total = sum(len(s) for s in STRUCTURE.values()) + len(PROJECTS)
print(f"OK: {total} module topics + {len(PROJECTS)} projects + root docs present.")
