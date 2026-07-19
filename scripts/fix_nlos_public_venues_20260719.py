#!/usr/bin/env python3
"""Correct final public venue metadata already integrated in the survey."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Passive acoustic non-line-of-sight localization without a relay surface"
URL = "https://doi.org/10.1103/p97k-sf71"
SUMMARY = (
    "Uses knife-edge diffraction at doorway edges and convex corners for passive 3D acoustic source localization "
    "without a conventional relay surface; the public metadata now points to the verified Physical Review Applied publication."
)


def replace_line(text: str, needle: str, replacement: str, label: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if needle in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one {label}, found {len(matches)}")
    ending = "\n" if lines[matches[0]].endswith("\n") else ""
    lines[matches[0]] = replacement.rstrip("\n") + ending
    return "".join(lines)


def main() -> None:
    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    readme_row = f"| 2026 | [{TITLE}]({URL}) — Sommer, Katz | Physical Review Applied 2026 | {SUMMARY} |"
    readme = replace_line(readme, f"[{TITLE}]", readme_row, "README passive-acoustic row")
    readme_path.write_text(readme, encoding="utf-8")

    index_path = ROOT / "index.html"
    index = index_path.read_text(encoding="utf-8")
    paper = (
        f'      {{cat:"modality acoustic passive diffraction localization",title:"{TITLE}",'
        f'authors:"Sommer, Katz",year:2026,venue:"Physical Review Applied 2026",url:"{URL}",key:"{SUMMARY}"}},'
    )
    index = replace_line(index, f'title:"{TITLE}"', paper, "homepage passive-acoustic object")
    index_path.write_text(index, encoding="utf-8")

    print("Corrected passive acoustic NLOS public metadata to Physical Review Applied 2026.")


if __name__ == "__main__":
    main()
