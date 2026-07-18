#!/usr/bin/env python3
"""Normalize legacy public metadata and LaTeX anchors before guarded sync."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ACTIVE = ROOT / "article/2active.tex"
OLD_TITLE = "Geometric Constrained Non-Line-of-Sight Imaging"
NEW_TITLE = "Geometry-Constrained Non-Line-of-Sight Imaging"
OLD_LINK = "https://arxiv.org/abs/2503.17992"
NEW_LINK = "https://doi.org/10.1109/TVCG.2026.3684832"
OLD_MODEL_HEADING = r"\noindent \textbf{\mbox{Model-decomposition reconstruction from sparse transients}.}"
NEW_MODEL_HEADING = r"\noindent \textbf{Model-decomposition reconstruction from sparse transients.}"


def normalize_readme() -> int:
    text = README.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    old_matches = [i for i, line in enumerate(lines) if f"[{OLD_TITLE}]" in line]

    for i in old_matches:
        line = lines[i]
        line = line.replace("| 2025 |", "| 2026 |", 1)
        line = line.replace(f"[{OLD_TITLE}]({OLD_LINK})", f"[{NEW_TITLE}]({NEW_LINK})")
        line = line.replace("| arXiv 2025 |", "| IEEE TVCG 2026 |")
        lines[i] = line

    updated = "".join(lines)
    final_lines = [line for line in updated.splitlines() if f"[{NEW_TITLE}]" in line]
    if not final_lines:
        raise RuntimeError("No geometry-constrained README records were found")
    for line in final_lines:
        if NEW_LINK not in line or "IEEE TVCG 2026" not in line or "| 2026 |" not in line:
            raise RuntimeError("A geometry-constrained README record still has preliminary metadata")
    if f"[{OLD_TITLE}]" in updated:
        raise RuntimeError("A preliminary geometry-constrained README title remains")

    README.write_text(updated, encoding="utf-8")
    return len(old_matches)


def normalize_active_heading() -> bool:
    text = ACTIVE.read_text(encoding="utf-8")
    changed = False
    if OLD_MODEL_HEADING in text:
        text = text.replace(OLD_MODEL_HEADING, NEW_MODEL_HEADING, 1)
        changed = True
    elif NEW_MODEL_HEADING not in text:
        raise RuntimeError("Model-decomposition review heading is missing")
    ACTIVE.write_text(text, encoding="utf-8")
    return changed


def main() -> None:
    records = normalize_readme()
    heading_changed = normalize_active_heading()
    print(
        f"Normalized {records} preliminary geometry-constrained README records; "
        f"model-decomposition heading changed={heading_changed}."
    )


if __name__ == "__main__":
    main()
