#!/usr/bin/env python3
"""Synchronize the already-cited GeRaF 2.0 paper with public artifacts.

The survey prose and canonical bibliography already contain this CVPR 2026 work.
This bounded, idempotent script closes the README/website visibility gap without
rewriting large files wholesale.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals"
KEY = "luSeeingThroughBoxes2026"
URL = (
    "https://openaccess.thecvf.com/content/CVPR2026/html/"
    "Lu_Seeing_through_boxes_Non-Line-of-Sight_3D_Reconstruction_from_"
    "Radar_Signals_CVPR_2026_paper.html"
)


def require_once(text: str, needle: str, label: str) -> None:
    count = text.count(needle)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label}, found {count}")


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    if TITLE not in text:
        separator = "|------|-------|----------------|----------------|\n"
        require_once(text, separator, "Latest Additions table separator")
        row = (
            f"| 2026 | [Seeing through boxes: Non-Line-of-Sight 3D Reconstruction "
            f"from Radar Signals]({URL}) — Lu, Shanbhag, Al Hassanieh | CVPR 2026, "
            "1221–1230 | Introduces GeRaF 2.0, a unified LOS/NLOS neural geometry "
            "framework that uses visible exterior geometry to guide RF propagation "
            "into an occluded enclosure. The added LOS constraints stabilize signed-"
            "distance-field optimization and improve the physical consistency and "
            "surface accuracy of hidden 3D reconstruction. |\n"
        )
        text = text.replace(separator, separator + row, 1)

    timeline_line = (
        "   │     Lu et al.: GeRaF 2.0 uses visible exterior geometry to constrain "
        "RF propagation and stabilize hidden signed-distance reconstruction "
        "[CVPR]\n"
    )
    if timeline_line not in text:
        lines = text.splitlines(keepends=True)
        matches = [i for i, line in enumerate(lines) if line.startswith("2026 ──")]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one 2026 timeline line, found {len(matches)}")
        lines.insert(matches[0] + 1, timeline_line)
        text = "".join(lines)
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    if f'title:"{TITLE}"' not in text:
        anchor = "    const papers=[\n"
        require_once(text, anchor, "paper explorer array")
        record = (
            '      {cat:"latest radar rf mmwave learned reconstruction neural-field '
            'sdf los-guided geometry cvpr",title:"Seeing through boxes: Non-Line-of-'
            'Sight 3D Reconstruction from Radar Signals",authors:"Lu, Shanbhag & Al '
            'Hassanieh",year:2026,venue:"CVPR 2026",url:"' + URL + '",key:"GeRaF '
            '2.0 jointly models visible exterior and hidden interior geometry, using '
            'LOS structure to guide RF propagation and stabilize physically consistent '
            'signed-distance reconstruction behind occlusions."},\n'
        )
        text = text.replace(anchor, anchor + record, 1)

    marker = "GeRaF 2.0 jointly models visible exterior and hidden interior geometry"
    if marker not in text:
        pattern = re.compile(
            r'(<div class="tl"><div class="year">2026</div><div class="tl-body">'
            r'<strong>.*?</strong><p>)(.*?)(</p>)',
            flags=re.DOTALL,
        )
        match = pattern.search(text)
        if not match:
            raise RuntimeError("Could not locate the 2026 website timeline entry")
        sentence = (
            " GeRaF 2.0 jointly models visible exterior and hidden interior geometry, "
            "using LOS structure to guide RF propagation and stabilize neural SDF "
            "reconstruction inside occluded enclosures."
        )
        text = text[: match.start(2)] + match.group(2) + sentence + text[match.end(2) :]

    actual = text.count("{cat:")
    text, count = re.subn(
        r'<b>\d+</b><span>tracked latest entries</span>',
        f'<b>{actual}</b><span>tracked latest entries</span>',
        text,
        count=1,
    )
    if count != 1:
        raise RuntimeError("Website tracked-entry count anchor not found")
    path.write_text(text, encoding="utf-8")


def validate_existing_survey_sources() -> None:
    survey = (ROOT / "article/5newscenes.tex").read_text(encoding="utf-8")
    bib = (ROOT / "egbib_merged_20260711.bib").read_text(encoding="utf-8")
    if KEY not in survey:
        raise RuntimeError("GeRaF 2.0 survey citation is missing from article/5newscenes.tex")
    if not re.search(rf"@\w+\s*\{{\s*{re.escape(KEY)}\s*,", bib, flags=re.I):
        raise RuntimeError("GeRaF 2.0 canonical bibliography entry is missing")


def update_note() -> None:
    note = ROOT / "updates/2026-08-02-geraf2-public-sync.md"
    note.write_text(
        """# GeRaF 2.0 public-artifact synchronization — 2 August 2026

A fresh RF/radar NLOS audit found that **Seeing through boxes: Non-Line-of-Sight
3D Reconstruction from Radar Signals** (Lu, Shanbhag, and Al Hassanieh, CVPR
2026, pp. 1221--1230) was already discussed in the survey and present in the
canonical bibliography under `luSeeingThroughBoxes2026`, but was absent from
the README Latest Additions table and website paper explorer.

GeRaF 2.0 uses visible line-of-sight geometry outside an enclosure to guide RF
propagation and regularize neural signed-distance reconstruction of hidden
interior surfaces. This update adds the final CVPR record, concise contribution
summary, radar/RF categorization, and 2026 timeline placement to both public
artifacts. The guarded build subsequently verifies the existing survey citation,
unique bibliography entry, regenerated PDF text, and website entry count.
""",
        encoding="utf-8",
    )


def main() -> None:
    validate_existing_survey_sources()
    update_readme()
    update_index()
    update_note()
    print("Synchronized GeRaF 2.0 across README and website public artifacts.")


if __name__ == "__main__":
    main()
