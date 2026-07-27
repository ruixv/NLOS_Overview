#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
MODALITIES = ROOT / "article" / "5newscenes.tex"
MASTER = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"

GRIDLESS_TITLE = "Reconfigurable intelligent surface-enabled gridless DoA estimation system for NLoS scenarios"
GRIDLESS_DOI = "10.1016/j.sigpro.2025.109934"
MONOSTATIC_TITLE = "RIS-aided monostatic radar for NLOS target DOA estimation based on steering vector decoupling"
MONOSTATIC_DOI = "10.1016/j.sigpro.2026.110685"


def die(message: str) -> None:
    raise RuntimeError(message)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        die(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def insert_timeline_sentence(text: str, year: int, marker: str, sentence: str, label: str) -> str:
    if marker in text:
        return text
    pattern = re.compile(rf'(^\s*{year} ──.*?$)', re.MULTILINE)
    match = pattern.search(text)
    if not match:
        die(f"{label}: {year} timeline anchor not found")
    return text[: match.end()] + "\n" + sentence + text[match.end() :]


def patch_readme() -> None:
    text = README.read_text(encoding="utf-8")
    separator = "|------|-------|----------------|----------------|\n"
    rows = ""
    if GRIDLESS_DOI not in text:
        rows += (
            f"| 2025 | [{GRIDLESS_TITLE}](https://doi.org/{GRIDLESS_DOI}) — Yuan et al. | Signal Processing 2025 | Uses an RIS-created virtual-LOS path, covariance-domain denoising, atomic-norm minimization, and ADMM for gridless multi-target direction estimation with limited receive hardware; numerical validation only. |\n"
        )
    if MONOSTATIC_DOI not in text:
        rows += (
            f"| 2026 | [{MONOSTATIC_TITLE}](https://doi.org/{MONOSTATIC_DOI}) — Zhang et al. | Signal Processing 2026 | Scans hidden directions with an RIS codebook, decouples the target steering-vector outer product from the composite monostatic echo, and applies Root-MUSIC for NLOS angle estimation; simulation-only, not hidden-shape reconstruction. |\n"
        )
    if rows:
        text = replace_once(text, separator, separator + rows, "README latest-additions table")

    category_anchor = "| 2026 | [Around-the-corner Radar Sensing Using Reconfigurable Intelligent Surface](https://arxiv.org/abs/2602.11471) — Yasmeen et al. | arXiv 2026 | RIS-assisted around-the-corner radar sensing; steers energy into NLOS regions and recovers human micro-Doppler signatures. |\n"
    category_rows = ""
    if text.count(GRIDLESS_DOI) < 2:
        category_rows += (
            f"| 2025 | [{GRIDLESS_TITLE}](https://doi.org/{GRIDLESS_DOI}) — Yuan et al. | Signal Processing 2025 | Establishes covariance-domain, atomic-norm gridless DoA estimation through an RIS-created virtual path. The results are simulation-only and concern angular localization rather than hidden-scene reconstruction. |\n"
        )
    if text.count(MONOSTATIC_DOI) < 2:
        category_rows += (
            f"| 2026 | [{MONOSTATIC_TITLE}](https://doi.org/{MONOSTATIC_DOI}) — Zhang et al. | Signal Processing 2026 | Uses RIS beam scanning, steering-vector decoupling, and Root-MUSIC for simulated monostatic NLOS target-angle estimation; it does not recover hidden reflectivity or geometry. |\n"
        )
    if category_rows:
        text = replace_once(text, category_anchor, category_rows + category_anchor, "README RF/RIS category")

    text = insert_timeline_sentence(
        text,
        2025,
        "Yuan et al.: RIS-enabled covariance-domain gridless DoA",
        "     │     Yuan et al.: RIS-enabled covariance-domain gridless DoA uses atomic-norm recovery and ADMM for simulated multi-target NLOS angular sensing [Signal Processing]",
        "README",
    )
    text = insert_timeline_sentence(
        text,
        2026,
        "Zhang et al.: monostatic radar--RIS steering-vector decoupling",
        "     │     Zhang et al.: monostatic radar--RIS steering-vector decoupling and Root-MUSIC enable simulated NLOS target-angle estimation [Signal Processing]",
        "README",
    )

    text = text.replace("**Update run: 26 July 2026.**", "**Update run: 27 July 2026.**")
    README.write_text(text, encoding="utf-8")


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")
    objects = ""
    if GRIDLESS_DOI not in text:
        objects += (
            f'      {{cat:"latest modality radar RF RIS NLOS localization DoA simulation",title:"{GRIDLESS_TITLE}",authors:"Yuan et al.",year:2025,venue:"Signal Processing 2025",url:"https://doi.org/{GRIDLESS_DOI}",key:"Creates a virtual-LOS path with an RIS and combines covariance-domain denoising, atomic-norm Toeplitz recovery, and ADMM for gridless multi-target DoA estimation with limited receive hardware; numerical validation only."}},\n'
        )
    if MONOSTATIC_DOI not in text:
        objects += (
            f'      {{cat:"latest modality radar RF RIS monostatic NLOS localization DoA simulation",title:"{MONOSTATIC_TITLE}",authors:"Zhang et al.",year:2026,venue:"Signal Processing 2026",url:"https://doi.org/{MONOSTATIC_DOI}",key:"Uses an RIS phase codebook to scan hidden directions, decouples the target steering-vector outer product from the composite monostatic echo, and applies Root-MUSIC; simulation-only angular sensing, not hidden-shape reconstruction."}},\n'
        )
    if objects:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + objects, "website paper array")

    additions = {
        2025: (
            "RIS-enabled covariance-domain gridless DoA used atomic-norm recovery and ADMM for simulated multi-target NLOS angular sensing.",
            " RIS-enabled covariance-domain gridless DoA used atomic-norm recovery and ADMM for simulated multi-target NLOS angular sensing.",
        ),
        2026: (
            "Monostatic radar--RIS steering-vector decoupling",
            " Monostatic radar--RIS steering-vector decoupling and Root-MUSIC enabled simulated NLOS target-angle estimation while remaining distinct from hidden-shape reconstruction.",
        ),
    }
    for year, (marker, sentence) in additions.items():
        if marker in text:
            continue
        pattern = re.compile(
            rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
            re.DOTALL,
        )
        match = pattern.search(text)
        if not match:
            die(f"website {year} timeline block not found")
        text = text[: match.start()] + match.group(1) + match.group(2) + sentence + match.group(3) + text[match.end() :]

    count = len(re.findall(r'\{cat:"', text))
    stat = re.compile(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>')
    text, n = stat.subn(f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>', text, count=1)
    if n != 1:
        die("website tracked-entry counter not found")
    text = text.replace("26 July 2026", "27 July 2026")
    INDEX.write_text(text, encoding="utf-8")


def patch_modalities() -> None:
    text = MODALITIES.read_text(encoding="utf-8")
    if "yuanRISGridlessDoA2025" not in text:
        anchor = r'''\vspace{0.8mm}
\noindent \textbf{Urban-intersection FMCW radar perception.}
'''
        prose = r'''\vspace{0.8mm}
\noindent \textbf{RIS-assisted gridless and monostatic angular sensing.}
A complementary RIS trajectory targets hidden-object direction rather than reflectivity or surface reconstruction. Yuan~\etal~formulated RIS-enabled NLOS direction finding in the covariance domain~\cite{yuanRISGridlessDoA2025}: after estimating the noise variance, atomic-norm minimization recovers a Hermitian Toeplitz representation and an ADMM solver provides gridless multi-source DoA estimates with limited receive hardware. Zhang~\etal~considered a monostatic radar--RIS--target--RIS--radar path~\cite{zhangRISMonostaticDOA2026}. A phase-codebook scans the hidden angular sector, steering-vector decoupling recovers the target outer-product matrix from the RIS-element superposition, and Root-MUSIC estimates the target angles. Both studies are numerical, so they should be read as theoretical RIS-assisted NLOS localization advances rather than measured hidden-scene imaging systems.

'''
        text = replace_once(text, anchor, prose + anchor, "radar/RIS survey insertion")
    MODALITIES.write_text(text, encoding="utf-8")


def bib_entries() -> str:
    return r'''@article{yuanRISGridlessDoA2025,
  author = {Yuan, Jiawen and Zhang, Gong and Meng, Kaitao and Leung, Henry Chi Ming},
  title = {Reconfigurable Intelligent Surface-Enabled Gridless {DoA} Estimation System for {NLoS} Scenarios},
  journal = {Signal Processing},
  volume = {233},
  pages = {109934},
  year = {2025},
  month = aug,
  publisher = {Elsevier},
  doi = {10.1016/j.sigpro.2025.109934},
  url = {https://doi.org/10.1016/j.sigpro.2025.109934}
}

@article{zhangRISMonostaticDOA2026,
  author = {Zhang, Yujia and Yang, Peng and Zhou, Yu and Liu, Lijun and Mo, Haoran and Du, Lan},
  title = {{RIS}-Aided Monostatic Radar for {NLOS} Target {DOA} Estimation Based on Steering Vector Decoupling},
  journal = {Signal Processing},
  volume = {248},
  pages = {110685},
  year = {2026},
  month = nov,
  publisher = {Elsevier},
  doi = {10.1016/j.sigpro.2026.110685},
  url = {https://doi.org/10.1016/j.sigpro.2026.110685},
  note = {Available online 6 May 2026}
}
'''


def patch_bib() -> None:
    text = BIB.read_text(encoding="utf-8")
    entries = bib_entries()
    blocks = {
        GRIDLESS_DOI: re.search(r"@article\{yuanRISGridlessDoA2025,.*?\n\}", entries, re.DOTALL).group(0),
        MONOSTATIC_DOI: re.search(r"@article\{zhangRISMonostaticDOA2026,.*?\n\}", entries, re.DOTALL).group(0),
    }
    for doi, block in blocks.items():
        if doi not in text:
            text = text.rstrip() + "\n\n" + block + "\n"
    for doi in blocks:
        if text.lower().count(doi.lower()) != 2:
            die(f"bibliography DOI {doi} should occur in doi and url exactly twice")
    BIB.write_text(text, encoding="utf-8")


def patch_master() -> None:
    text = MASTER.read_text(encoding="utf-8")
    marker = "% 27 July 2026 citation trace: RIS-assisted gridless and monostatic NLOS angular sensing synchronized.\n"
    if marker not in text:
        text = replace_once(text, "%% bare_jrnl.tex\n", "%% bare_jrnl.tex\n" + marker, "master update marker")
    MASTER.write_text(text, encoding="utf-8")


def validate() -> None:
    artifacts = {
        "README": README.read_text(encoding="utf-8"),
        "index": INDEX.read_text(encoding="utf-8"),
        "modalities": MODALITIES.read_text(encoding="utf-8"),
        "bibliography": BIB.read_text(encoding="utf-8"),
    }
    records = {
        GRIDLESS_DOI: "yuanRISGridlessDoA2025",
        MONOSTATIC_DOI: "zhangRISMonostaticDOA2026",
    }
    for doi, key in records.items():
        for name in ("README", "index", "bibliography"):
            if doi not in artifacts[name]:
                die(f"{name} is missing {doi}")
        if artifacts["modalities"].count(key) < 1:
            die(f"modalities survey is missing {key}")
        if artifacts["bibliography"].count("{" + key + ",") != 1:
            die(f"bibliography key count mismatch for {key}")
        if artifacts["bibliography"].lower().count(doi.lower()) != 2:
            die(f"bibliography DOI count mismatch for {doi}")


def main() -> None:
    patch_readme()
    patch_index()
    patch_modalities()
    patch_bib()
    patch_master()
    validate()
    print("RIS-assisted NLOS DoA integration completed and validated")


if __name__ == "__main__":
    main()
