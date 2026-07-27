#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article" / "2active.tex"
MASTER = ROOT / "bare_jrnl.tex"
SOURCE_BIB = ROOT / "egbib_20260727_adaptive_windowing.bib"
MERGED_BIB = ROOT / "egbib_merged_20260711.bib"
NOTE = ROOT / "updates" / "2026-07-27-adaptive-windowing-nlos.md"

TITLE = "Adaptive windowing for photon-efficient non-line-of-sight imaging under high ambient light"
DOI = "10.1364/OE.575419"
KEY = "miaoAdaptiveWindowingNLOS2025"

BIB_ENTRY = r"""@article{miaoAdaptiveWindowingNLOS2025,
  author = {Miao, Jinye and Cai, Fuyao and Qin, Taotao and Bai, Lianfa and Guo, Enlai and Shi, Yingjie and Han, Jing},
  title = {{Adaptive Windowing} for Photon-Efficient Non-Line-of-Sight Imaging under High Ambient Light},
  journal = {Optics Express},
  volume = {33},
  number = {21},
  pages = {44522--44542},
  year = {2025},
  month = {October},
  publisher = {Optica Publishing Group},
  doi = {10.1364/OE.575419},
  url = {https://doi.org/10.1364/OE.575419}
}
"""


def die(message: str) -> None:
    raise RuntimeError(message)


def patch_readme() -> None:
    text = README.read_text(encoding="utf-8")
    if TITLE not in text:
        anchor = "| 2026 | [All-day non-line-of-sight imaging based on Si-SPAD and phase-congruency-based structured ε-regularization]"
        if text.count(anchor) != 1:
            die("README all-day insertion anchor is not unique")
        row = (
            "| 2025 | [Adaptive windowing for photon-efficient non-line-of-sight imaging under high ambient light]"
            "(https://doi.org/10.1364/OE.575419) — Miao et al. | Optics Express 2025 | "
            "Models signal and background photon arrivals, clusters correlated pixels to estimate matched-filter windows, "
            "and applies per-pixel short temporal gates with total-variation reconstruction. AW-NLOS remains effective at "
            "SBR 2.12 and 0.02 detected signal photons per pixel, improving SSIM by approximately 0.5 at 42 mW laser power. |\n"
        )
        text = text.replace(anchor, row + anchor, 1)
    timeline = "Miao et al.: adaptive photon-arrival windowing suppresses overwhelming daylight background before TV-regularized transient reconstruction [Optics Express]"
    if timeline not in text:
        anchor = "2026 ── Yin et al.: Si-SPAD and phase-congruency regularization enable 200 m all-day active NLOS under 94,314 lx sunlight [Optics and Lasers in Engineering]"
        if text.count(anchor) != 1:
            die("README timeline anchor is not unique")
        text = text.replace(anchor, "   │     " + timeline + "\n" + anchor, 1)
    README.write_text(text, encoding="utf-8")


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")
    if f'title:"{TITLE}"' not in text:
        anchor = '{cat:"latest active",title:"All-day non-line-of-sight imaging based on Si-SPAD and phase-congruency-based structured ε-regularization"'
        if text.count(anchor) != 1:
            die("website all-day paper-object anchor is not unique")
        obj = (
            '      {cat:"latest active",title:"Adaptive windowing for photon-efficient non-line-of-sight imaging under high ambient light",'
            'authors:"Miao et al.",year:2025,venue:"Optics Express 2025",url:"https://doi.org/10.1364/OE.575419",'
            'key:"AW-NLOS uses probabilistic signal/background models, spatio-temporal pixel clustering, matched-filter window estimation, per-pixel short temporal gates, and TV regularization to recover hidden geometry under extreme ambient light and photon starvation."},\n'
        )
        text = text.replace(anchor, obj + "      " + anchor, 1)
    sentence = "Miao et al. added probabilistic adaptive temporal windowing that suppresses ambient detections before TV-regularized transient inversion, strengthening the photon-efficient daylight branch."
    if sentence not in text:
        pattern = re.compile(r'(<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>.*?<p>)(.*?)(</p></div></div>)', re.S)
        match = pattern.search(text)
        if not match:
            die("website 2025 timeline block is missing")
        text = text[: match.start(2)] + match.group(2) + " " + sentence + text[match.end(2) :]
    count = len(re.findall(r'\{cat:"', text))
    text, n = re.subn(
        r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',
        f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',
        text,
        count=1,
    )
    if n != 1:
        die("website tracked-entry counter is missing")
    INDEX.write_text(text, encoding="utf-8")


def patch_active() -> None:
    text = ACTIVE.read_text(encoding="utf-8")
    if KEY not in text:
        if text.count("yinAllDayNLOS2026") < 1:
            die("active-table all-day citation anchor is missing")
        text = text.replace("yinAllDayNLOS2026", KEY + ",yinAllDayNLOS2026", 1)
        heading = r"\noindent \textbf{All-day SPAD NLOS imaging.}"
        if text.count(heading) != 1:
            die("all-day survey paragraph anchor is not unique")
        paragraph = r"""\noindent \textbf{Adaptive photon-arrival windowing under high ambient light.}
Miao~\etal~address the acquisition-side failure mode in which a weak three-bounce response is overwhelmed by temporally broad background detections~\cite{miaoAdaptiveWindowingNLOS2025}. AW-NLOS first models the arrival statistics of signal and noise, then amplifies correlated weak events through spatio-temporal pixel clustering so that a matched filter can estimate a target-dependent temporal support. Per-pixel short-duration range windows reject most ambient photons before total-variation-regularized hidden-volume reconstruction. Measured experiments report recovery at an SBR of 2.12 and only 0.02 signal photons per pixel, together with an approximately 0.5 SSIM improvement over conventional processing at 42~mW illumination. This work forms an acquisition-aware bridge between photon-efficient single-photon statistics and the subsequent detector/regularizer co-design for all-day, long-range NLOS.

\vspace{0.8mm}
"""
        text = text.replace(heading, paragraph + heading, 1)
    ACTIVE.write_text(text, encoding="utf-8")


def patch_bibliography() -> None:
    if SOURCE_BIB.exists():
        source = SOURCE_BIB.read_text(encoding="utf-8")
        if KEY not in source or DOI not in source:
            die("dated bibliography supplement conflicts with the verified record")
        SOURCE_BIB.write_text(BIB_ENTRY, encoding="utf-8")
    else:
        SOURCE_BIB.write_text(BIB_ENTRY, encoding="utf-8")

    text = MERGED_BIB.read_text(encoding="utf-8")
    pattern = re.compile(rf"(?ms)^@\w+\{{{re.escape(KEY)},.*?^\}}\s*")
    matches = list(pattern.finditer(text))
    if len(matches) > 1:
        die("merged bibliography has duplicate adaptive-windowing keys")
    if matches:
        text = text[: matches[0].start()] + BIB_ENTRY.rstrip() + "\n\n" + text[matches[0].end() :].lstrip("\n")
    else:
        text = text.rstrip() + "\n\n" + BIB_ENTRY.rstrip() + "\n"
    if text.lower().count(DOI.lower()) != 2:
        die("adaptive-windowing DOI must appear once in doi and once in url")
    if text.count("{" + KEY + ",") != 1:
        die("adaptive-windowing citation key is not unique")
    MERGED_BIB.write_text(text, encoding="utf-8")


def patch_master_and_note() -> None:
    text = MASTER.read_text(encoding="utf-8")
    marker = "% 27 July 2026 citation trace: adaptive photon-arrival windowing for high-ambient-light NLOS synchronized.\n"
    if marker not in text:
        anchor = "%% bare_jrnl.tex\n"
        if text.count(anchor) != 1:
            die("master LaTeX header anchor is not unique")
        text = text.replace(anchor, anchor + marker, 1)
    MASTER.write_text(text, encoding="utf-8")
    NOTE.write_text(
        """# Adaptive-windowing NLOS citation trace — 27 July 2026

Integrated the DOI-verified Optics Express paper **Adaptive windowing for photon-efficient non-line-of-sight imaging under high ambient light** (Miao et al., 2025, DOI `10.1364/OE.575419`).

The paper is direct active transient NLOS reconstruction rather than incidental photon processing. It cites the Velten, LCT, and f-k milestones and contributes probabilistic signal/background modeling, spatio-temporal weak-event clustering, matched-filter window estimation, per-pixel temporal gating, and TV-regularized reconstruction for extreme ambient-light and photon-starved conditions.

Updated README, website explorer and timeline, active-system table and literature review, dated and consolidated BibTeX sources, survey marker, and rebuilt PDF.
""",
        encoding="utf-8",
    )


def validate() -> None:
    files = {
        "README": README.read_text(encoding="utf-8"),
        "website": INDEX.read_text(encoding="utf-8"),
        "active": ACTIVE.read_text(encoding="utf-8"),
        "source_bib": SOURCE_BIB.read_text(encoding="utf-8"),
        "merged_bib": MERGED_BIB.read_text(encoding="utf-8"),
    }
    if files["README"].count(TITLE) != 1:
        die("README adaptive-windowing record is missing or duplicated")
    if files["website"].count(f'title:"{TITLE}"') != 1:
        die("website adaptive-windowing object is missing or duplicated")
    if files["active"].count(KEY) < 2:
        die("active survey must cite adaptive windowing in the table and prose")
    for label in ("README", "website", "source_bib", "merged_bib"):
        if DOI not in files[label]:
            die(f"{label} is missing the verified DOI")
    count = len(re.findall(r'\{cat:"', files["website"]))
    expected = f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>'
    if expected not in files["website"]:
        die("website counter is inconsistent")
    print(f"Adaptive-windowing NLOS synchronization passed ({count} website entries)")


def main() -> None:
    patch_readme()
    patch_index()
    patch_active()
    patch_bibliography()
    patch_master_and_note()
    validate()


if __name__ == "__main__":
    main()
