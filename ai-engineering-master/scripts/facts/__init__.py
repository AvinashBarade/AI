from __future__ import annotations

from .facts_00 import CONTENT as C00
from .facts_01 import CONTENT as C01
from .facts_02 import CONTENT as C02
from .facts_03_24 import CONTENT as C_REST  # modules 03–24
from .fallback import fallback

# module folder -> slug -> dict
HAND_AUTHORED: dict[str, dict[str, dict]] = {
    "00-foundations": C00,
    "01-python-for-ai-engineering": C01,
    "02-llm-fundamentals": C02,
}

HAND_AUTHORED.update(C_REST)


def get_fact(module: str, slug: str) -> dict:
    from .facts_interview import CONTENT as C_INT

    if module in C_INT and slug in C_INT[module]:
        return C_INT[module][slug]
    if module in HAND_AUTHORED and slug in HAND_AUTHORED[module]:
        return HAND_AUTHORED[module][slug]
    return fallback(module, slug)
