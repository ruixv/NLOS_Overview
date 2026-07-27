#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article" / "2active.tex"
DATA = ROOT / "article" / "4datadriven.tex"
MASTER = ROOT / "bare_jrnl.tex"
SOURCE_BIB = ROOT / "egbib_20260728_physics_rescue.bib"
MERGED_BIB = ROOT / "egbib_merged_20260711.bib"
NOTE = ROOT / "updates" / "2026-07-28-physics-rescue-tpami.md"

TITLE = "Physics to the Rescue: Deep Non-Line-of-Sight Reconstruction for High-Speed Imaging"
DOI = "10.1109/TPAMI.2022.3203383"
KEY = "muPhysicsRescueTPAMI2025"

BIB_ENTRY = r"""@article{muPhysicsRescueTPAMI2025,
  author = {Mu, Fangzhou and Mo, Sicheng and Peng, Jiayong and Liu, Xiaochun and Nam, Ji Hyun and Raghavan, Siddeshwar and Velten, Andreas and Li, Yin},
  title = {Physics to the Rescue: Deep Non-Line-of-Sight Reconstruction for High-Speed Imaging},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  volume = {47},
  number = {8},
  pages = {6146--6158},
  year = {2025},
  month = {August},
  publisher = {IEEE},
  doi = {10.1109/TPAMI.2022.3203383},
  url = {https://doi.org/10.1109/TPAMI.2022.3203383}
}
"""


def die(message: str) -> None:
    raise RuntimeError(message)


def patch_readme() -> None:
    text = README.read_text(encoding="utf-8")
    if TITLE not in text:
        anchor = "| 2025 | [Reconfigurable intelligent surface-enabled gridless DoA estimation system for NLoS scenarios]"
        if text.count(anchor) != 1:
            die("README latest-addition anchor is not unique")
        row = (
            "| 2025 | [Physics to the Rescue: Deep Non-Line-of-Sight Reconstruction for High-Speed Imaging]"
            "(https://doi.org/10.1109/TPAMI.2022.3203383) — Mu et al. | IEEE TPAMI 2025 | "
            "Embeds complementary wave-propagation and volume-rendering priors in a feed-forward model for high-speed non-confocal transient NLOS. "
            "The model is trained on synthetic data with intensity or raw-transient supervision, generalizes to measured captures, and reconstructs intensity and depth at more than 5 captures per second. |\n"
        )
        text = text.replace(anchor, row + anchor, 1)

    text, n = re.subn(
        r"\*\*Update run: \d{1,2} [A-Za-z]+ 2026\.\*\*",
        "**Update run: 28 July 2026.**",
        text,
        count=1,
    )
    if n != 1:
        die("README update-run line is missing")

    timeline = "Mu et al.: wave-propagation and volume-rendering priors enable feed-forward high-speed non-confocal NLOS reconstruction [IEEE TPAMI]"
    if timeline not in text:
        anchor = "Miao et al.: adaptive photon-arrival windowing suppresses overwhelming daylight background before TV-regularized transient reconstruction [Optics Express]"
        if text.count(anchor) != 1:
            die("README 2025 timeline anchor is not unique")
        text = text.replace(anchor, anchor + "\n   │     " + timeline, 1)
    README.write_text(text, encoding="utf-8")


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")
    if f'title:"{TITLE}"' not in text:
        anchor = '{cat:"latest active",title:"Adaptive windowing for photon-efficient non-line-of-sight imaging under high ambient light"'
        if text.count(anchor) != 1:
            die("website adaptive-windowing object anchor is not unique")
        obj = (
            '      {cat:"latest learning",title:"Physics to the Rescue: Deep Non-Line-of-Sight Reconstruction for High-Speed Imaging",'
            'authors:"Mu et al.",year:2025,venue:"IEEE TPAMI 2025",url:"https://doi.org/10.1109/TPAMI.2022.3203383",'
            'key:"A physics-guided feed-forward model combines wave propagation with volume rendering to tolerate the approximate transport of a 5 Hz non-confocal capture system, generalizing from synthetic training to measured intensity and depth reconstruction."},\n'
        )
        text = text.replace(anchor, obj + "      " + anchor, 1)

    sentence = "Mu et al. combined wave-propagation and volume-rendering priors in a feed-forward network for high-speed non-confocal reconstruction, linking the 5 Hz capture system to synthetic-to-real intensity and depth inference."
    if sentence not in text:
        pattern = re.compile(r'(<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>.*?<p>)(.*?)(</p></div></div>)', re.S)
        match = pattern.search(text)
        if not match:
            die("website 2025 timeline block is missing")
        text = text[: match.start(2)] + match.group(2) + " " + sentence + text[match.end(2) :]

    text, n = re.subn(
        r'(<div class="eyebrow">Updated )\d{1,2} [A-Za-z]+ 2026',
        r'\g<1>28 July 2026',
        text,
        count=1,
    )
    if n != 1:
        die("website hero update date is missing")
    text = re.sub(r'(Last updated:?\s*)\d{1,2} [A-Za-z]+ 2026', r'\g<1>28 July 2026', text, flags=re.I)

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
        anchor = "miaoAdaptiveWindowingNLOS2025"
        if text.count(anchor) != 1:
            die("active SPAD-table anchor is not unique")
        text = text.replace(anchor, KEY + "," + anchor, 1)
    ACTIVE.write_text(text, encoding="utf-8")


def patch_data_driven() -> None:
    text = DATA.read_text(encoding="utf-8")
    if KEY not in text:
        heading = r"\noindent \textbf{Memory-efficient MetaFormer reconstruction.}"
        if text.count(heading) != 1:
            die("data-driven insertion anchor is not unique")
        paragraph = r"""\noindent \textbf{Physics-guided reconstruction for high-speed non-confocal capture.}
Mu~\etal~address the model mismatch introduced by a 5~Hz non-confocal acquisition system, whose speed depends on approximations that invalidate idealized transport inverses~\cite{muPhysicsRescueTPAMI2025}. Their network embeds complementary wave-propagation and volume-rendering modules and supports supervision from target intensity images or raw transients. Although trained exclusively on synthetic data, it generalizes to measured captures and renders hidden intensity and depth in one feed-forward pass at more than five captures per second. This result connects real-time diffuse acquisition to later physics-constrained neural fields, transient completion, and differentiable rendering.

\vspace{0.8mm}
"""
        text = text.replace(heading, paragraph + heading, 1)
    else:
        old = (
            "TransDiff~\\cite{cuiTransDiffTIP2025} extends unsupervised transient completion to aperture-limited relay surfaces using a latent diffusion prior constrained by the measured transients. "
            "In parallel, Physics to the Rescue~\\cite{muPhysicsRescueTPAMI2025} embeds wave-propagation and volume-rendering priors into a neural reconstruction pipeline, improving robustness when high-speed acquisition requires approximate light-transport models. "
            "Together, these methods mark a shift from purely data-driven inversion toward learned solvers whose latent completion is explicitly checked against transient physics."
        )
        new = (
            "TransDiff~\\cite{cuiTransDiffTIP2025} extends unsupervised transient completion to aperture-limited relay surfaces using a latent diffusion prior constrained by the measured transients. "
            "In parallel, Physics to the Rescue~\\cite{muPhysicsRescueTPAMI2025} embeds complementary wave-propagation and volume-rendering priors into a feed-forward reconstruction model, improving robustness when a 5~Hz non-confocal acquisition system requires approximate light transport. "
            "Its flexible intensity- or raw-transient supervision and synthetic-to-real intensity/depth inference connect high-speed capture to later physics-constrained neural fields and differentiable transient rendering."
        )
        if old in text:
            text = text.replace(old, new, 1)
    DATA.write_text(text, encoding="utf-8")


def patch_bibliography() -> None:
    SOURCE_BIB.write_text(BIB_ENTRY, encoding="utf-8")
    text = MERGED_BIB.read_text(encoding="utf-8")
    pattern = re.compile(rf"(?ms)^@\w+\{{{re.escape(KEY)},.*?^\}}\s*")
    matches = list(pattern.finditer(text))
    if len(matches) > 1:
        die("merged bibliography has duplicate Physics-to-the-Rescue keys")
    if matches:
        text = text[: matches[0].start()] + BIB_ENTRY.rstrip() + "\n\n" + text[matches[0].end() :].lstrip("\n")
    else:
        text = text.rstrip() + "\n\n" + BIB_ENTRY.rstrip() + "\n"
    if text.lower().count(DOI.lower()) != 2:
        die("Physics-to-the-Rescue DOI must appear once in doi and once in url")
    if text.count("{" + KEY + ",") != 1:
        die("Physics-to-the-Rescue citation key is not unique")
    MERGED_BIB.write_text(text, encoding="utf-8")


def patch_master_and_note() -> None:
    text = MASTER.read_text(encoding="utf-8")
    marker = "% 28 July 2026 citation trace: Physics to the Rescue finalized as IEEE TPAMI 2025 and synchronized across public artifacts.\n"
    if marker not in text:
        anchor = "%% bare_jrnl.tex\n"
        if text.count(anchor) != 1:
            die("master LaTeX header anchor is not unique")
        text = text.replace(anchor, anchor + marker, 1)
    MASTER.write_text(text, encoding="utf-8")
    NOTE.write_text(
        """# Physics to the Rescue cross-artifact integration — 28 July 2026

Integrated the final journal record for **Physics to the Rescue: Deep Non-Line-of-Sight Reconstruction for High-Speed Imaging** by Mu et al., IEEE Transactions on Pattern Analysis and Machine Intelligence 47(8), 6146–6158, 2025, DOI `10.1109/TPAMI.2022.3203383`.

The work was already mentioned in the data-driven survey prose but lacked a resolvable bibliography entry and was absent from the README, website explorer, public timeline, and active-system table. The synchronized record uses the final TPAMI volume/issue/pages rather than arXiv or the ICCP 2022 precursor status.

The method is direct active transient NLOS reconstruction: it combines wave-propagation and volume-rendering priors to tolerate the approximate transport of a 5 Hz non-confocal capture system, supports intensity or raw-transient supervision, generalizes from synthetic training to real measurements, and produces intensity and depth in a feed-forward pass.
""",
        encoding="utf-8",
    )


def validate() -> None:
    files = {
        "README": README.read_text(encoding="utf-8"),
        "website": INDEX.read_text(encoding="utf-8"),
        "active": ACTIVE.read_text(encoding="utf-8"),
        "data": DATA.read_text(encoding="utf-8"),
        "source_bib": SOURCE_BIB.read_text(encoding="utf-8"),
        "merged_bib": MERGED_BIB.read_text(encoding="utf-8"),
    }
    if files["README"].count(TITLE) != 1:
        die("README Physics-to-the-Rescue record is missing or duplicated")
    if files["website"].count(f'title:"{TITLE}"') != 1:
        die("website Physics-to-the-Rescue object is missing or duplicated")
    if files["active"].count(KEY) != 1:
        die("active survey table must cite Physics to the Rescue exactly once")
    if files["data"].count(KEY) != 1:
        die("data-driven survey must cite Physics to the Rescue exactly once")
    for label in ("README", "website", "source_bib", "merged_bib"):
        if DOI not in files[label]:
            die(f"{label} is missing the verified DOI")
    count = len(re.findall(r'\{cat:"', files["website"]))
    expected = f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>'
    if expected not in files["website"]:
        die("website counter is inconsistent")
    print(f"Physics-to-the-Rescue synchronization passed ({count} website entries)")


def main() -> None:
    patch_readme()
    patch_index()
    patch_active()
    patch_data_driven()
    patch_bibliography()
    patch_master_and_note()
    validate()


if __name__ == "__main__":
    main()
