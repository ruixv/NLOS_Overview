#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

replacements = {
    ROOT / "README.md": [
        ("https://img.shields.io/badge/Papers-190+-green", "https://img.shields.io/badge/Papers-210+-green"),
    ],
    ROOT / "index.html": [
        ("updated July 2026 with 190+ papers", "updated July 2026 with 210+ papers"),
        ("Updated 26 July 2026 · 190+ papers", "Updated 26 July 2026 · 210+ papers"),
        ('<div class="stat"><b>190+</b><span>curated papers</span></div>', '<div class="stat"><b>210+</b><span>curated papers</span></div>'),
    ],
}

for path, pairs in replacements.items():
    text = path.read_text(encoding="utf-8")
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new)
        elif new not in text:
            raise RuntimeError(f"Missing both old and new count marker in {path}: {old}")
    path.write_text(text, encoding="utf-8")

print("Synchronized NLOS public paper-count labels.")
