#!/usr/bin/env python3
"""Synchronize the missing passive-polarization NLOS milestone.

Edits are marker-based and idempotent. The script aborts rather than blindly
rewriting a large hand-maintained artifact when an expected marker is absent or
ambiguous.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Enhancing Passive Non-Line-of-Sight Imaging Using Polarization Cues"
KEY = "tanakaPolarizedNonLineofSightImaging2020"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label} marker, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    text = read("README.md")
    text = text.replace("**Update run: 12 July 2026.**", "**Update run: 13 July 2026.**", 1)

    marker = (
        "| 2020 | [Seeing Around Corners with Edge-Resolved Transient Imaging]"
        "(https://doi.org/10.1038/s41467-020-19727-4) — Rapp et al. | Nature Communications 2020 | "
        "Combines a vertical edge occluder with pulsed SPAD transients: differencing adjacent photon-arrival "
        "histograms isolates angular wedges and enables 2.5D room-scale reconstruction over a 180° field of view "
        "from only 45 illumination positions. |\n"
    )
    if TITLE not in text:
        row = (
            f"| 2019 | [{TITLE}](https://arxiv.org/abs/1911.12906) — Tanaka, Mukaigawa, Kadambi | "
            "arXiv 2019 | Adds a camera-mounted polarizer to passive NLOS capture: polarization-axis rotation "
            "makes oblique indirect paths more discriminative, improves the conditioning of the light-transport "
            "inverse problem, and enhances hidden-image recovery both with and without occluders. |\n"
        )
        text = replace_once(text, marker, row + marker, "README edge-resolved row")

    if text.count(TITLE) != 1:
        raise RuntimeError(f"README should contain one {TITLE!r} entry, found {text.count(TITLE)}")
    if "**Update run: 13 July 2026.**" not in text:
        raise RuntimeError("README update date did not advance to 13 July 2026")
    write("README.md", text)


def update_homepage() -> None:
    text = read("index.html")
    text = text.replace("Updated 12 July 2026", "Updated 13 July 2026", 1)
    text = text.replace("Last updated: 12 July 2026", "Last updated: 13 July 2026", 1)

    marker = (
        '      {cat:"latest active",title:"Seeing Around Corners with Edge-Resolved Transient Imaging",'
        'authors:"Rapp et al.",year:2020,'
    )
    if TITLE not in text:
        obj = (
            '      {cat:"latest passive hardware",title:"Enhancing Passive Non-Line-of-Sight Imaging Using '
            'Polarization Cues",authors:"Tanaka, Mukaigawa, Kadambi",year:2019,venue:"arXiv 2019",'
            'url:"https://arxiv.org/abs/1911.12906",key:"A camera-mounted polarizer exploits polarization-axis '
            'rotation along oblique indirect paths to improve light-transport conditioning and passive hidden-image '
            'recovery, with or without occluders."},\n'
        )
        text = replace_once(text, marker, obj + marker, "homepage edge-resolved paper object")

    count_re = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    matches = count_re.findall(text)
    if len(matches) != 1:
        raise RuntimeError(f"Expected one homepage tracked-entry count, found {len(matches)}")
    current = int(matches[0])
    if current not in (88, 89, 90, 91, 92):
        raise RuntimeError(f"Unexpected homepage count {current}")
    text = count_re.sub('<b>92</b><span>tracked latest entries</span>', text, count=1)

    old_timeline = (
        '      <div class="tl"><div class="year">2019</div><div class="tl-body"><strong>f-k migration, '
        'feature-visibility limits, passive periscopy, coherent control, and single-path/scannerless NLOS</strong>'
        '<p>The field split into wave-based active NLOS, principled analysis of which hidden orientations and spatial '
        'features are recoverable, ordinary-camera passive NLOS, keyhole imaging, coherent recognition, scannerless '
        'single-pixel acquisition, and wavefront-shaping active focusing.</p></div></div>'
    )
    new_timeline = (
        '      <div class="tl"><div class="year">2019</div><div class="tl-body"><strong>f-k migration, '
        'feature visibility, passive periscopy and polarization, coherent control, and single-path/scannerless '
        'NLOS</strong><p>The field split into wave-based active NLOS, principled recoverability analysis, '
        'ordinary-camera computational periscopy, polarization-conditioned passive light transport, keyhole '
        'imaging, coherent recognition, scannerless single-pixel acquisition, and wavefront-shaping active '
        'focusing.</p></div></div>'
    )
    if "polarization-conditioned passive light transport" not in text:
        text = replace_once(text, old_timeline, new_timeline, "homepage 2019 timeline")

    if text.count(TITLE) != 1:
        raise RuntimeError(f"Homepage should contain one {TITLE!r} object, found {text.count(TITLE)}")
    if '<b>92</b><span>tracked latest entries</span>' not in text:
        raise RuntimeError("Homepage tracked-entry count did not update to 92")
    if "Updated 13 July 2026" not in text or "Last updated: 13 July 2026" not in text:
        raise RuntimeError("Homepage dates did not update to 13 July 2026")
    write("index.html", text)


def update_survey() -> None:
    text = read("article/3passive.tex")
    paragraph = r'''\vspace{0.8mm}
\noindent \textbf{Polarization-conditioned passive transport.}
Tanaka~\etal~showed that a camera-mounted polarizer can improve passive NLOS reconstruction by exploiting polarization-axis rotation along oblique indirect paths~\cite{tanakaPolarizedNonLineofSightImaging2020}. The added directional cue lowers the effective conditioning of the wall-to-hidden-scene transport matrix and improves recovery both with and without a known occluder, complementing computational periscopy without requiring a controllable active source.

'''
    if "Polarization-conditioned passive transport." not in text:
        marker = r'''\bookmark[dest=\HyperLocalCurrentHref,level=3]{Coherence}
'''
        text = replace_once(text, marker, paragraph + marker, "passive-survey coherence marker")

    if text.count(f"\\cite{{{KEY}}}") < 1:
        raise RuntimeError(f"Survey did not cite {KEY}")
    if "Polarization-conditioned passive transport." not in text:
        raise RuntimeError("Survey polarization discussion was not inserted")
    write("article/3passive.tex", text)


def main() -> None:
    source = read("egbib_20260713_polarization_updates.bib")
    if KEY not in source or "1911.12906" not in source:
        raise RuntimeError("Canonical passive-polarization BibTeX record is missing")
    update_readme()
    update_homepage()
    update_survey()
    print("Synchronized passive polarization NLOS across README, homepage, timeline, survey, and bibliography metadata.")


if __name__ == "__main__":
    main()
