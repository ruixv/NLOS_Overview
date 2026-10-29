#!/usr/bin/env python3
"""Apply final follow-up synchronizers and reconcile public paper counts."""
from pathlib import Path
import re
import runpy

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
PAPER_SOURCE = ROOT / "data/papers-source.html"
FOLLOWUPS = [
    ROOT / "scripts" / "sync_nlos_20260718_visibility_detection.py",
    ROOT / "scripts" / "sync_nlos_20260718_reconstruction_pose_consistency.py",
    ROOT / "scripts" / "cleanup_nlos_20260718_timeline_duplicates.py",
    ROOT / "scripts" / "sync_nlos_20260718_understanding.py",
]


def reconcile_count(path: Path, expected: int) -> None:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"Expected one tracked-count stat in {path.relative_to(ROOT)}, found {len(matches)}")
    old_count = int(matches[0].group(2))
    text = pattern.sub(lambda m: f"{m.group(1)}{expected}{m.group(3)}", text, count=1)
    path.write_text(text, encoding="utf-8")
    print(f"Reconciled {path.relative_to(ROOT)} tracked count: {old_count} -> {expected}.")


def main() -> None:
    for followup in FOLLOWUPS:
        if not followup.is_file():
            raise RuntimeError(f"Missing required follow-up synchronizer: {followup}")
        runpy.run_path(str(followup), run_name="__main__")

    source_text = PAPER_SOURCE.read_text(encoding="utf-8")
    paper_count = len(re.findall(r'^\s*\{cat:"[^"]+",title:"', source_text, flags=re.MULTILINE))
    if paper_count <= 0:
        raise RuntimeError("Paper source contains no records")
    reconcile_count(PAPER_SOURCE, paper_count)


if __name__ == "__main__":
    main()
