#!/usr/bin/env python3
"""Apply the final follow-up synchronizer and reconcile the homepage counter."""
from pathlib import Path
import re
import runpy

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
FOLLOWUP = ROOT / "scripts" / "sync_nlos_20260718_visibility_detection.py"


def main() -> None:
    if not FOLLOWUP.is_file():
        raise RuntimeError(f"Missing required follow-up synchronizer: {FOLLOWUP}")
    runpy.run_path(str(FOLLOWUP), run_name="__main__")

    text = INDEX.read_text(encoding="utf-8")
    pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"Expected one homepage tracked-count stat, found {len(matches)}")

    paper_count = len(re.findall(r'^\s*\{cat:"[^"]+",title:"', text, flags=re.MULTILINE))
    if paper_count <= 0:
        raise RuntimeError("Homepage paper explorer contains no records")

    old_count = int(matches[0].group(2))
    text = pattern.sub(lambda m: f"{m.group(1)}{paper_count}{m.group(3)}", text, count=1)
    INDEX.write_text(text, encoding="utf-8")
    print(f"Reconciled homepage tracked count: {old_count} -> {paper_count}.")


if __name__ == "__main__":
    main()
