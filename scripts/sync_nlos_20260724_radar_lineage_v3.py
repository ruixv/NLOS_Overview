#!/usr/bin/env python3
"""Execute the bibliography-aware radar-lineage synchronizer with the exact website anchor."""

from pathlib import Path

source_path = Path(__file__).with_name("sync_nlos_20260724_radar_lineage_v2.py")
source = source_path.read_text(encoding="utf-8")
old = 'papers_anchor = "    const papers = [\\n"'
new = 'papers_anchor = "    const papers=[\\n"'
if source.count(old) != 1:
    raise SystemExit(f"Expected exactly one legacy website-array anchor, found {source.count(old)}")
source = source.replace(old, new, 1)
exec(compile(source, str(source_path), "exec"), {"__name__": "__main__", "__file__": str(source_path)})
