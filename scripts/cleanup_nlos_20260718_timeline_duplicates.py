#!/usr/bin/env python3
"""Remove repeated 2025 timeline sentence from both public pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = [ROOT / "index.html", ROOT / "data" / "papers-source.html"]
SENTENCE = (
    " Zhou et al. extended ordinary-camera computational periscopy to 10 m through pattern calibration "
    "and low-rank separation of weak indirect signals from ambient background."
)


def main() -> None:
    for path in PAGES:
        text = path.read_text(encoding="utf-8")
        count = text.count(SENTENCE)
        if count == 0:
            continue
        first = text.find(SENTENCE)
        keep = text[:first + len(SENTENCE)]
        rest = text[first + len(SENTENCE):].replace(SENTENCE, "")
        text = keep + rest
        path.write_text(text, encoding="utf-8")
        print(f"Reconciled {path.relative_to(ROOT)} repeated timeline sentence: {count} -> 1.")


if __name__ == "__main__":
    main()
