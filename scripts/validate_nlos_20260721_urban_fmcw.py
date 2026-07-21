#!/usr/bin/env python3
"""Validate cross-artifact coverage for the urban-intersection FMCW update."""
from __future__ import annotations

from pathlib import Path
import re

DOI = "10.32604/cmes.2026.078862"
KEY = "linDeepLearningFMCWRadar2026"


def text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8", errors="strict")


for path in ("README.md", "index.html"):
    value = text(path).count(DOI)
    if value != 1:
        raise SystemExit(f"{path}: expected DOI exactly once, found {value}")

article = text("article/5newscenes.tex")
if article.count(KEY) != 1:
    raise SystemExit(f"article/5newscenes.tex: expected citation key once, found {article.count(KEY)}")

index = text("index.html")
expected_stat = '<div class="stat"><b>179</b><span>tracked latest entries</span></div>'
if expected_stat not in index:
    raise SystemExit("website tracked-entry count was not updated to 179")

master = text("bare_jrnl.tex")
if "% 21 July 2026: integrated urban-intersection FMCW radar NLOS perception." not in master:
    raise SystemExit("bare_jrnl.tex integration marker is missing")

bib = text("egbib_merged_20260711.bib")
key_matches = re.findall(r"@[A-Za-z]+\s*\{\s*" + re.escape(KEY) + r"\s*,", bib)
if len(key_matches) != 1:
    raise SystemExit(f"merged bibliography: expected one {KEY} record, found {len(key_matches)}")

doi_fields = [d.strip().lower() for d in re.findall(r"\bdoi\s*=\s*\{([^}]+)\}", bib, flags=re.I)]
if doi_fields.count(DOI.lower()) != 1:
    raise SystemExit(
        f"merged bibliography: expected one DOI field for {DOI}, found {doi_fields.count(DOI.lower())}"
    )

print("Urban-intersection FMCW cross-artifact source validation passed.")
