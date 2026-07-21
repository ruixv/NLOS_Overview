#!/usr/bin/env python3
"""Validate cross-artifact coverage for the urban-intersection FMCW update."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re

DOI = "10.32604/cmes.2026.078862"
KEY = "linDeepLearningFMCWRadar2026"
TITLE_FRAGMENT = "Deep Learning"


def text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8", errors="strict")


for path in ("README.md", "index.html", "egbib_merged_20260711.bib"):
    value = text(path).count(DOI)
    if value != 1:
        raise SystemExit(f"{path}: expected DOI exactly once, found {value}")

for path in ("article/5newscenes.tex", "egbib_merged_20260711.bib"):
    if KEY not in text(path):
        raise SystemExit(f"{path}: missing citation key {KEY}")

index = text("index.html")
expected_stat = '<div class="stat"><b>179</b><span>tracked latest entries</span></div>'
if expected_stat not in index:
    raise SystemExit("website tracked-entry count was not updated to 179")

master = text("bare_jrnl.tex")
if "% 21 July 2026: integrated urban-intersection FMCW radar NLOS perception." not in master:
    raise SystemExit("bare_jrnl.tex integration marker is missing")

bib = text("egbib_merged_20260711.bib")
keys = re.findall(r"@[A-Za-z]+\s*\{\s*([^,\s]+)", bib)
key_dupes = [key for key, count in Counter(keys).items() if count > 1]
if key_dupes:
    raise SystemExit(f"duplicate BibTeX keys: {key_dupes[:10]}")

dois = [d.lower() for d in re.findall(r"\bdoi\s*=\s*\{([^}]+)\}", bib, flags=re.I)]
doi_dupes = [doi for doi, count in Counter(dois).items() if count > 1]
if doi_dupes:
    raise SystemExit(f"duplicate BibTeX DOIs: {doi_dupes[:10]}")

print("Urban-intersection FMCW cross-artifact source validation passed.")
