#!/usr/bin/env python3
"""Integrate a missing Ambient-IoT/backscatter NLOS positioning paper.

The paper was found while tracing the RF/backscatter branch around existing
N2LoS and passive-backscatter NLOS localization works. It is kept as arXiv
because no final accepted/published venue could be verified as of 18 Aug 2026.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARXIV_ID = "2607.03459"
ARXIV_URL = f"https://arxiv.org/abs/{ARXIV_ID}"
KEY = "yigitlerAmbientIoTBackscatter2026"
TITLE = "Ambient IoT Backscatter Devices as Passive Anchors for NLOS Cellular Positioning: Fundamental Limits"


def read(path: str | Path) -> str:
    p = path if isinstance(path, Path) else ROOT / path
    return p.read_text(encoding="utf-8")


def write(path: str | Path, text: str) -> None:
    p = path if isinstance(path, Path) else ROOT / path
    p.write_text(text, encoding="utf-8")


def insert_after_line(text: str, needle: str, addition: str, label: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if needle in line]
    if not matches:
        raise RuntimeError(f"{label}: anchor not found: {needle}")
    i = matches[-1]
    lines.insert(i + 1, addition if addition.endswith("\n") else addition + "\n")
    return "".join(lines)


def update_readme() -> None:
    path = "README.md"
    text = read(path)

    row = (
        f"| 2026 | [{TITLE}]({ARXIV_URL}) — Yiğitler et al. | arXiv:2607.03459 (2026) | "
        "Derives closed-form equivalent Fisher information matrices for calibrated, partially calibrated, and fully uncalibrated Ambient-IoT backscatter anchors in uplink NLOS positioning. It quantifies which carrier-phase and delay information survives unknown device phases/gains and shows that joint single-snapshot UE–scatterer identifiability requires at least two passive anchors in 2D or three in 3D with sufficient angular diversity. |\n"
    )
    if ARXIV_ID not in text:
        text = insert_after_line(text, "Backscatter Assisted Indoor NLOS Positioning", row, "README backscatter paper row")

    timeline_line = (
        "   │     Yiğitler et al.: Ambient-IoT backscatter fundamental limits — calibration-aware EFIM/CRB analysis identifies which NLOS positioning information survives unreferenced passive anchors and the minimum 2D/3D anchor geometry for joint UE–scatterer identifiability [arXiv]\n"
    )
    if "Ambient-IoT backscatter fundamental limits" not in text:
        anchor = "Yasmeen et al.: one-bit RIS quantization"
        if anchor in text:
            text = insert_after_line(text, anchor, timeline_line, "README 2026 RF timeline")
        else:
            text = insert_after_line(text, "Goïcoechea et al.: a single antenna plus programmable RIS", timeline_line, "README 2026 RF timeline fallback")

    text = text.replace("**Update run: 17 August 2026.**", "**Update run: 18 August 2026.**", 1)
    text = re.sub(r"This update run \(17 August 2026\)", "This update run (18 August 2026)", text, count=1)
    write(path, text)


def update_website_source() -> None:
    path = "data/papers-source.html"
    text = read(path)

    paper_obj = (
        '      {cat:"latest modality rf backscatter positioning theory fundamental-limits",'
        f'title:"{TITLE}",authors:"Yiğitler et al.",year:2026,venue:"arXiv:2607.03459 (2026)",'
        f'url:"{ARXIV_URL}",'
        'key:"Calibration-aware EFIM/CRB analysis for Ambient-IoT passive anchors in uplink NLOS positioning; quantifies information loss from unknown device phases/gains and shows that joint UE–scatterer identifiability needs at least two anchors in 2D or three in 3D with sufficient angular diversity."},\n'
    )
    if ARXIV_ID not in text:
        anchor = (
            '      {cat:"latest modality",title:"Backscatter Assisted Indoor NLOS Positioning",authors:"Ruttik et al.",year:2026,venue:"arXiv 2026",url:"https://arxiv.org/abs/2606.17325",key:"Passive backscatter devices act as virtual anchors for corridor NLOS indoor positioning."},\n'
        )
        if anchor not in text:
            raise RuntimeError("Canonical website backscatter anchor missing")
        text = text.replace(anchor, anchor + paper_obj, 1)

    if "Ambient-IoT backscatter fundamental-limit analysis" not in text:
        pattern = re.compile(
            r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
            flags=re.S,
        )
        m = pattern.search(text)
        if not m:
            raise RuntimeError("Canonical website 2026 timeline block missing")
        sentence = (
            " Yiğitler et al. added an Ambient-IoT backscatter fundamental-limit analysis: "
            "closed-form EFIM/CRB results quantify calibration losses for passive NLOS anchors and show that joint UE–scatterer identification needs at least two anchors in 2D or three in 3D with sufficient angular diversity."
        )
        text = text[:m.start(2)] + m.group(2) + sentence + text[m.end(2):]

    text = text.replace("Updated 17 August 2026", "Updated 18 August 2026", 1)
    text = text.replace("Last updated: 17 August 2026", "Last updated: 18 August 2026", 1)

    array = re.search(r"const\s+papers\s*=\s*\[(.*?)\n\s*\];", text, flags=re.S)
    if not array:
        raise RuntimeError("Canonical website paper array missing")
    count = len(re.findall(r'\{cat:"', array.group(1)))
    text, n = re.subn(
        r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',
        f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',
        text,
        count=1,
    )
    if n != 1:
        raise RuntimeError("Canonical website tracked-count badge missing")
    write(path, text)


def update_index() -> None:
    path = "index.html"
    text = read(path)
    text = re.sub(r"Updated 17 Aug 2026", "Updated 18 Aug 2026", text, count=1)
    text = re.sub(r"Updated 17 August 2026", "Updated 18 August 2026", text, count=1)
    text = re.sub(r"Last updated: 17 August 2026", "Last updated: 18 August 2026", text, count=1)
    write(path, text)


def update_rf_survey() -> None:
    path = "article/5newscenes.tex"
    text = read(path)
    if KEY not in text:
        anchor = (
            "Backscatter-assisted indoor NLOS positioning~\\cite{ruttikBackscatterNLOS2026} extends this branch from dedicated tag modulation toward passive asynchronous backscatter devices that act as virtual anchors for corridor-constrained user tracking, showing that low-power environmental tags can turn otherwise difficult multipath into useful NLOS localization evidence."
        )
        if anchor not in text:
            raise RuntimeError("RF survey backscatter sentence anchor missing")
        addition = (
            " Yi\\u{g}itler~\\etal~then moved this passive-anchor branch from measured tracking to calibration-aware fundamental limits~\\cite{" + KEY + "}. "
            "For an uplink NLOS model in which the direct and backscatter-assisted paths share an unknown scatterer, they treat the common gain, relative backscatter response, and residual device phases as nuisance variables and derive closed-form equivalent Fisher information matrices. The analysis isolates which carrier-phase and bandwidth-dependent delay information survives partial or absent calibration and shows that joint single-snapshot UE--scatterer identification requires at least two backscatter devices in two dimensions or three in three dimensions, together with sufficient angular diversity. This provides a theoretical deployment counterpart to measured backscatter-assisted NLOS localization rather than another hidden-shape reconstruction method."
        )
        text = text.replace(anchor, anchor + addition, 1)
    write(path, text)


def merge_bibliography() -> None:
    path = "egbib_merged_20260711.bib"
    text = read(path)
    lower = text.lower()
    doi = "10.48550/arXiv.2607.03459"
    if KEY.lower() in lower:
        if ARXIV_ID not in text:
            raise RuntimeError("BibTeX key exists without expected arXiv id")
        return
    if ARXIV_ID in text or doi.lower() in lower:
        raise RuntimeError("arXiv record already exists under a different BibTeX key")
    entry = r'''
@misc{yigitlerAmbientIoTBackscatter2026,
  author        = {H{\"u}seyin Yi{\u{g}}itler and Musa Furkan Keskin and Ossi Kaltiokallio and Riku J{\"a}ntti},
  title         = {Ambient {IoT} Backscatter Devices as Passive Anchors for {NLOS} Cellular Positioning: Fundamental Limits},
  year          = {2026},
  eprint        = {2607.03459},
  archivePrefix = {arXiv},
  primaryClass  = {eess.SP},
  doi           = {10.48550/arXiv.2607.03459},
  url           = {https://arxiv.org/abs/2607.03459},
  note          = {arXiv preprint, version 2, 7 July 2026}
}
'''.strip()
    text = text.rstrip() + "\n\n" + entry + "\n"
    write(path, text)


def update_master() -> None:
    path = "bare_jrnl.tex"
    text = read(path)
    text = text.replace("extends coverage to include significant advances from 2022 through 17 August 2026.", "extends coverage to include significant advances from 2022 through 18 August 2026.", 1)
    marker = "% 18 August 2026 RF/backscatter trace: Ambient-IoT passive-anchor NLOS positioning fundamental limits integrated.\n"
    if marker not in text:
        text = marker + text
    write(path, text)


def update_note() -> None:
    path = ROOT / "updates/2026-08-18-backscatter-nlos-fundamental-limits.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "Status: pending guarded integration/build.",
        "Status: integrated by the guarded workflow; public artifacts and the rebuilt PDF are committed only after source, citation, semantic-PDF, and render checks pass.",
    )
    path.write_text(text, encoding="utf-8")


def validate() -> None:
    readme = read("README.md")
    website = read("data/papers-source.html")
    survey = read("article/5newscenes.tex")
    bib = read("egbib_merged_20260711.bib")
    master = read("bare_jrnl.tex")
    for name, text in (("README", readme), ("website", website), ("bib", bib)):
        if ARXIV_ID not in text:
            raise RuntimeError(f"{name} missing {ARXIV_ID}")
    if survey.count(KEY) != 1:
        raise RuntimeError(f"survey citation count for {KEY}: {survey.count(KEY)}")
    if bib.lower().count("{" + KEY.lower() + ",") != 1:
        raise RuntimeError("BibTeX key is not unique")
    if bib.count(ARXIV_ID) < 1:
        raise RuntimeError("BibTeX arXiv id missing")
    if "**Update run: 18 August 2026.**" not in readme:
        raise RuntimeError("README update date not synchronized")
    if "18 August 2026" not in website:
        raise RuntimeError("website date not synchronized")
    if "through 18 August 2026." not in master:
        raise RuntimeError("survey snapshot date not synchronized")
    if not master.startswith("% 18 August 2026 RF/backscatter trace"):
        raise RuntimeError("master provenance marker missing")


def main() -> None:
    update_readme()
    update_website_source()
    update_index()
    update_rf_survey()
    merge_bibliography()
    update_master()
    update_note()
    validate()
    print("Integrated Ambient-IoT/backscatter NLOS fundamental-limits paper.")


if __name__ == "__main__":
    main()
