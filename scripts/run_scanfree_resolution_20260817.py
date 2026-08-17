#!/usr/bin/env python3
"""Compatibility and diagnostic wrapper for the guarded scan-free integration."""
from __future__ import annotations

import traceback
from pathlib import Path
import integrate_scanfree_resolution_20260817 as sync

# The merged bibliography already contains the Optics Express paper under this
# canonical key. Preserve that key rather than introducing a duplicate alias.
CANONICAL_SUBPIXEL_KEY = "zhangSubpixelModulation2025"
LEGACY_STAGED_KEY = "zhangSubpixelResolvingNLOS2025"

_original_update_active = sync.update_active


def update_active_with_canonical_key() -> None:
    _original_update_active()
    path = sync.ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    text = text.replace(LEGACY_STAGED_KEY, CANONICAL_SUBPIXEL_KEY)
    path.write_text(text, encoding="utf-8")


def validate_sources_with_canonical_key() -> None:
    readme = sync.read("README.md")
    site = sync.read("data/papers-source.html")
    active = sync.read("article/2active.tex")
    bib = sync.read(sync.MERGED_BIB)
    index = sync.read("index.html")
    for doi in ("10.1063/5.0235687", "10.1364/OE.569102", "10.1016/j.optlaseng.2025.109100"):
        if doi not in readme:
            raise RuntimeError(f"README missing {doi}")
        if doi not in site:
            raise RuntimeError(f"Canonical website source missing {doi}")
        if bib.lower().count(doi.lower()) < 1:
            raise RuntimeError(f"Merged bibliography missing {doi}")
    for key in ("zhangRealTimeScanFreeNLOS2024", CANONICAL_SUBPIXEL_KEY, "zhangSpatialCorrelationNLOS2025"):
        if key not in active:
            raise RuntimeError(f"Active survey missing citation key {key}")
        if bib.lower().count("{" + key.lower() + ",") != 1:
            raise RuntimeError(f"Merged bibliography key count is not one for {key}")
    if "Sub-pixel resolving modulation for non-line-of-sight imaging" not in readme:
        raise RuntimeError("README missing sub-pixel paper")
    if "Sub-pixel resolving modulation for non-line-of-sight imaging" not in site:
        raise RuntimeError("Canonical website source missing sub-pixel paper")
    if "Updated 17 Aug 2026" not in index:
        raise RuntimeError("V2 index living-survey date was not synchronized")


sync.update_active = update_active_with_canonical_key
sync.validate_sources = validate_sources_with_canonical_key

try:
    sync.main()
    note = sync.ROOT / "updates/2026-08-17-scanfree-spad-resolution-sync.md"
    if note.exists():
        text = note.read_text(encoding="utf-8")
        text = text.replace(
            "restore the two lost BibTeX records and add the new Optics Express BibTeX record in `egbib_merged_20260711.bib`;",
            "verify the three existing canonical BibTeX records in `egbib_merged_20260711.bib` and reuse `zhangSubpixelModulation2025` for the Optics Express paper, avoiding a duplicate alias;",
        )
        note.write_text(text, encoding="utf-8")
except Exception as exc:
    msg = f"{type(exc).__name__}: {exc}".replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')
    print(f"::error file=scripts/integrate_scanfree_resolution_20260817.py::{msg}")
    traceback.print_exc()
    raise
