#!/usr/bin/env python3
"""Remove an accidentally repeated 2025 timeline sentence from the homepage."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
SENTENCE = (
    " Zhou et al. extended ordinary-camera computational periscopy to 10 m through pattern calibration "
    "and low-rank separation of weak indirect signals from ambient background."
)


def main() -> None:
    text = INDEX.read_text(encoding="utf-8")
    count = text.count(SENTENCE)
    if count < 1:
        raise RuntimeError("Expected the 2025 passive 10 m timeline sentence")
    while text.count(SENTENCE) > 1:
        text = text.replace(SENTENCE + SENTENCE, SENTENCE, 1)
    if text.count(SENTENCE) != 1:
        raise RuntimeError("Could not reconcile the duplicated timeline sentence")
    INDEX.write_text(text, encoding="utf-8")
    print(f"Reconciled repeated 2025 timeline sentence: {count} -> 1.")


if __name__ == "__main__":
    main()
