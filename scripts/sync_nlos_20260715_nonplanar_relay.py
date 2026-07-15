#!/usr/bin/env python3
"""Synchronize the 15 July 2026 non-planar-relay citation-tracing update.

The update is idempotent and uses narrow, validated anchors. It fails loudly if
repository layout changes instead of replacing or truncating large files.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article/2active.tex"
NOTE = ROOT / "updates/2026-07-15-nonplanar-relay-citation-tracing.md"

TITLE = "Fast Non-Line-of-Sight Imaging with Non-Planar Relay Surfaces"
URL = "https://doi.org/10.1109/ICCP56744.2023.10233262"
KEY = "guFastNLOSNonPlanar2023"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> bool:
    text = README.read_text(encoding="utf-8")
    original = text

    row = (
        f"| 2023 | [{TITLE}]({URL}) — Gu et al. | IEEE ICCP 2023 | "
        "Extends Rayleigh--Sommerfeld / phasor-field reconstruction to non-planar relay surfaces through "
        "two-stage wave propagation with a planar proxy, preserving fast wave-based inversion when the "
        "visible relay geometry is curved or irregular. |\n"
    )
    if TITLE not in text:
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + row, "README latest-table header")

    milestone = (
        "   │     Gu et al.: 3D RSD — fast two-stage wave propagation for non-planar relay surfaces [ICCP]\n"
    )
    milestone_anchor = (
        "   │     Liu et al.: SSCR — mixed-dimensional regularization from 5×5 confocal measurements [CVPR]\n"
    )
    if "Gu et al.: 3D RSD" not in text:
        text = replace_once(text, milestone_anchor, milestone_anchor + milestone, "README 2023 milestone")

    if text != original:
        README.write_text(text, encoding="utf-8")
        return True
    return False


def update_index() -> bool:
    text = INDEX.read_text(encoding="utf-8")
    original = text
    was_absent = TITLE not in text

    paper = (
        f'      {{cat:"latest active",title:"{TITLE}",authors:"Gu et al.",year:2023,'
        f'venue:"IEEE ICCP 2023",url:"{URL}",key:"3D RSD extends fast wave-based NLOS reconstruction '
        'to curved or irregular relay geometry through two-stage Rayleigh--Sommerfeld propagation via a '
        'planar proxy."},\n'
    )
    if was_absent:
        anchor = "    const papers=[\n"
        text = replace_once(text, anchor, anchor + paper, "index paper-array anchor")
        count_pattern = re.compile(
            r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>'
        )
        matches = list(count_pattern.finditer(text))
        if len(matches) != 1:
            raise RuntimeError(f"Expected one tracked-entry count, found {len(matches)}")
        old_count = int(matches[0].group(1))
        text = count_pattern.sub(
            f'<div class="stat"><b>{old_count + 1}</b><span>tracked latest entries</span></div>',
            text,
            count=1,
        )

    timeline_pattern = re.compile(
        r'^\s*<div class="tl"><div class="year">2023</div><div class="tl-body">.*?</div></div>$',
        re.MULTILINE,
    )
    if "3D RSD extended fast wave propagation" not in text:
        matches = list(timeline_pattern.finditer(text))
        if len(matches) != 1:
            raise RuntimeError(f"Expected one 2023 timeline entry, found {len(matches)}")
        old = matches[0].group(0)
        new = old.replace(
            "SSN learned a plug-and-play measurement-space superresolution operator",
            "3D RSD extended fast wave propagation from planar walls to non-planar relay surfaces through a two-stage planar-proxy construction. SSN learned a plug-and-play measurement-space superresolution operator",
            1,
        )
        if new == old:
            raise RuntimeError("Could not find the 2023 timeline narrative anchor")
        text = text[:matches[0].start()] + new + text[matches[0].end():]

    if text != original:
        INDEX.write_text(text, encoding="utf-8")
        return True
    return False


def update_active_survey() -> bool:
    text = ACTIVE.read_text(encoding="utf-8")
    original = text

    if KEY not in text:
        table_pattern = re.compile(
            r'^(\s*\\cite\{)([^\n]*)(\}\s*& Pulsed laser & SPAD & Time of fight &\s+3D reconstruction\\\\%%%% Table body)$',
            re.MULTILINE,
        )
        matches = list(table_pattern.finditer(text))
        if len(matches) != 1:
            raise RuntimeError(f"Expected one active-SPAD table row, found {len(matches)}")
        keys = matches[0].group(2)
        replacement = matches[0].group(1) + keys + "," + KEY + matches[0].group(3)
        text = text[:matches[0].start()] + replacement + text[matches[0].end():]

    heading = "\\noindent \\textbf{Wave propagation on non-planar relay surfaces.}"
    if heading not in text:
        phasor_paragraph = (
            "The phasor field methods\\cite{rezaPhasorFieldWaves2019,liuPhasorFieldDiffraction2020,liuVirtualWaveOptics2018}, "
            "which have attracted widespread attention recently, regard the NLOS imaging as a diffraction-based LOS (line-of-sight) optical imaging problem. "
            "The projector function and diffraction function are determined by selecting a suitable LOS template, thereby directly reconstructing the hidden scene. "
            "Although based on wave propagation, these methods are all suitable for ToF measurement, making it easy to collect data and apply the model to public NLOS imaging datasets."
        )
        paragraph = (
            "\n\n\\vspace{0.8mm}\n"
            f"{heading}\n"
            "The fast convolutional forms of LCT, $f$--$k$ migration, and conventional phasor-field propagation usually assume that illumination and detection samples lie on a planar relay wall. Gu~\\etal~relaxed this restriction with 3D Rayleigh--Sommerfeld diffraction (3D RSD), decomposing propagation from a measured non-planar relay surface to the hidden volume into two stages connected by a planar proxy~\\cite{guFastNLOSNonPlanar2023}. This construction retains efficient wave-based propagation while accounting for curved or irregular relay geometry, and forms an important intermediate step between planar virtual-wave solvers and later arbitrary-relay inverse-rendering and Gaussian-transient formulations.\n"
        )
        text = replace_once(text, phasor_paragraph, phasor_paragraph + paragraph, "phasor-field survey paragraph")

    if text != original:
        ACTIVE.write_text(text, encoding="utf-8")
        return True
    return False


def write_note() -> bool:
    content = f"""# 15 July 2026 non-planar-relay citation-tracing update

A fresh search across arXiv, conference and journal pages, project/lab pages, and forward citations of the repository's core active-NLOS papers did not identify a directly relevant paper newer than the 5 July 2026 NIR raster-scanning preprint already tracked by the repository.

The high-priority citation-tracing pass through the SIGGRAPH 2026 3D Gaussian Transient Rendering paper identified one genuine missing milestone:

- **{TITLE}** — Chaoying Gu, Talha Sultan, Khadijeh Masumnia-Bisheh, Laura Waller, and Andreas Velten, IEEE ICCP 2023, pp. 1--12, DOI `10.1109/ICCP56744.2023.10233262`.

The later arbitrary-relay 3D Gaussian Transient Rendering work explicitly positions this method as the prior wave-based solution for non-planar relay geometry. The method, commonly summarized as 3D RSD, uses two-stage Rayleigh--Sommerfeld propagation through a planar proxy so that fast wave-domain reconstruction is not restricted to a physically planar relay wall. It is therefore direct NLOS reconstruction work rather than a paper that cites NLOS only in passing.

## Files synchronized

- `README.md`: adds the ICCP 2023 paper and its 2023 development milestone.
- `index.html`: adds the searchable paper object, increments the tracked-entry count, and expands the 2023 timeline.
- `article/2active.tex`: adds the paper to the active-SPAD table and inserts a relay-geometry paragraph next to the phasor-field discussion.
- `egbib_20260715_nonplanar_relay_updates.bib`: adds the publisher/DOI-verified canonical BibTeX record.
- `egbib_merged_20260711.bib`: regenerated by the bibliography merger.
- `bare_jrnl.pdf`: regenerated after a clean LaTeX/BibTeX build.

The workflow validates the citation key, bibliography entry, survey text, PDF text extraction, and absence of undefined or repeated BibTeX entries.
"""
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    old = NOTE.read_text(encoding="utf-8") if NOTE.exists() else None
    if old != content:
        NOTE.write_text(content, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = {
        "README.md": update_readme(),
        "index.html": update_index(),
        "article/2active.tex": update_active_survey(),
        str(NOTE.relative_to(ROOT)): write_note(),
    }
    print("Non-planar-relay NLOS synchronization complete:")
    for path, did_change in changed.items():
        print(f"- {path}: {'updated' if did_change else 'already current'}")


if __name__ == "__main__":
    main()
