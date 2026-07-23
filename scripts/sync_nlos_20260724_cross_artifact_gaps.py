#!/usr/bin/env python3
"""Synchronize three already-surveyed NLOS papers across public artifacts.

This script is intentionally fail-closed: every structural edit uses a unique anchor,
and bibliography records are normalized by citation key without tolerating duplicate
DOIs. It is safe to re-run.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
SURVEY = ROOT / "bare_jrnl.tex"
ACTIVE = ROOT / "article/2active.tex"
PASSIVE = ROOT / "article/3passive.tex"
LEARNING = ROOT / "article/4datadriven.tex"
BIB = ROOT / "egbib_merged_20260711.bib"

PAPERS = [
    {
        "key": "wangDiffuseAwarePassive2026",
        "doi": "10.1364/OE.601398",
        "readme": "| 2026 | [Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding](https://doi.org/10.1364/OE.601398) — Wang et al. | Optics Express 2026 | Designs diffuse-aware attention-enhanced encoding for ordinary-camera passive NLOS, emphasizing weak relay-wall features that survive diffuse transport rather than relying on a generic image-to-image backbone. The final paper appears in Optics Express 34(14), 26271–26289. |",
        "index": '{cat:"latest passive learning ordinary-camera attention",title:"Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding",authors:"Wang et al.",year:2026,venue:"Optics Express 2026",url:"https://doi.org/10.1364/OE.601398",key:"Diffuse-aware attention-enhanced encoding emphasizes weak ordinary-camera relay-wall features that survive diffuse transport, extending passive NLOS from generic image translation toward architecture choices matched to the conditioning of the physical forward process."},',
        "bib": """@article{wangDiffuseAwarePassive2026,
  author = {Wang, Xuefeng and Chen, Xingsu and Xu, Miao and Alimjan, Gulnaz and Zhao, Li},
  doi = {10.1364/OE.601398},
  journal = {Optics Express},
  month = {July},
  number = {14},
  pages = {26271--26289},
  publisher = {Optica Publishing Group},
  title = {Passive Non-Line-of-Sight Imaging with Diffuse-Aware Attention-Enhanced Encoding},
  url = {https://doi.org/10.1364/OE.601398},
  volume = {34},
  year = {2026}
}""",
        "article": PASSIVE,
    },
    {
        "key": "liangFMCWNLOS2026",
        "doi": "10.1364/PRJ.595776",
        "readme": "| 2026 | [Submillimeter non-line-of-sight ranging and imaging via cost-effective FMCW interferometry](https://doi.org/10.1364/PRJ.595776) — Liang et al. | Photonics Research 2026 | Uses dual-path fixed-delay-fiber calibration and dynamic temporal phase subdivision to compensate nonlinear frequency sweeps in a lower-cost coherent FMCW system, retaining submillimeter ranging and millimeter-scale hidden imaging without optical-frequency-comb calibration. |",
        "index": '{cat:"latest active coherent fmcw interferometry ranging",title:"Submillimeter non-line-of-sight ranging and imaging via cost-effective FMCW interferometry",authors:"Liang et al.",year:2026,venue:"Photonics Research 2026",url:"https://doi.org/10.1364/PRJ.595776",key:"Dual-path fixed-delay-fiber calibration and dynamic temporal phase subdivision compensate nonlinear FMCW sweeps in a lower-cost coherent architecture, achieving submillimeter ranging and millimeter-scale NLOS imaging."},',
        "bib": """@article{liangFMCWNLOS2026,
  author = {Liang, Huan and Wei, Lingchuan and Qin, Taotao and Bai, Lianfa and Shi, Yingjie and Guo, Enlai and Han, Jing},
  doi = {10.1364/PRJ.595776},
  journal = {Photonics Research},
  month = {June},
  number = {7},
  pages = {3005--3018},
  publisher = {Optica Publishing Group},
  title = {Submillimeter Non-Line-of-Sight Ranging and Imaging via Cost-Effective {FMCW} Interferometry},
  url = {https://doi.org/10.1364/PRJ.595776},
  volume = {14},
  year = {2026}
}""",
        "article": ACTIVE,
    },
    {
        "key": "fuFourierSinglePixelDiffusion2026",
        "doi": "10.1016/j.optlaseng.2026.109724",
        "readme": "| 2026 | [High-resolution Fourier single-pixel non-line-of-sight imaging employing diffusion model](https://doi.org/10.1016/j.optlaseng.2026.109724) — Fu et al. | Optics and Lasers in Engineering 2026 | Combines compressed Fourier single-pixel measurements with diffusion-prior reconstruction and Fourier data consistency, recovering high-frequency detail at sampling rates down to 3% through multiple paper layers. It is categorized as tightly adjacent transmissive/scattering NLOS rather than classical relay-wall around-corner imaging. |",
        "index": '{cat:"latest learning modality single-pixel diffusion scattering adjacent",title:"High-resolution Fourier single-pixel non-line-of-sight imaging employing diffusion model",authors:"Fu et al.",year:2026,venue:"Optics and Lasers in Engineering 2026",url:"https://doi.org/10.1016/j.optlaseng.2026.109724",key:"A diffusion prior reconstructs missing high-frequency Fourier coefficients while measured low-frequency single-pixel spectra enforce data consistency, supporting 3% sampling through multiple paper layers; this is tightly adjacent transmissive/scattering NLOS rather than classical around-corner relay imaging."},',
        "bib": """@article{fuFourierSinglePixelDiffusion2026,
  author = {Fu, Shengjie and Fang, Haoran and Yu, Yuheng and Shen, Nuo and Yuan, Yuqing and Liu, Hao and Liu, Guolin and Peng, Ziqi and Xia, Zizhun and Liu, Xuan and Liu, Qiegen and Song, Xianlin},
  doi = {10.1016/j.optlaseng.2026.109724},
  journal = {Optics and Lasers in Engineering},
  note = {Available online 12 March 2026},
  pages = {109724},
  publisher = {Elsevier},
  title = {High-Resolution Fourier Single-Pixel Non-Line-of-Sight Imaging Employing Diffusion Model},
  url = {https://doi.org/10.1016/j.optlaseng.2026.109724},
  volume = {201},
  year = {2026}
}""",
        "article": LEARNING,
    },
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def normalize_bib_entry(text: str, key: str, doi: str, canonical: str) -> str:
    pattern = re.compile(rf"(?ms)^@\w+\{{{re.escape(key)},\n.*?^\}}\s*\n?")
    matches = list(pattern.finditer(text))
    if len(matches) > 1:
        raise SystemExit(f"bibliography: duplicate key {key}")
    if matches:
        text = text[: matches[0].start()] + canonical.rstrip() + "\n\n" + text[matches[0].end() :]
    else:
        if doi.lower() in text.lower():
            raise SystemExit(f"bibliography: DOI {doi} exists under a different key")
        text = text.rstrip() + "\n\n" + canonical.rstrip() + "\n"
    if text.lower().count(doi.lower()) != 2:  # DOI field plus URL field
        raise SystemExit(f"bibliography: canonical DOI/URL count failed for {doi}")
    return text


# Validate that the detailed survey prose is already semantically integrated.
for paper in PAPERS:
    article_text = read(paper["article"])
    if article_text.count(paper["key"]) < 1:
        raise SystemExit(f"survey section missing expected citation {paper['key']}")

# README: preserve the newest 22 July Nature Communications item at the top,
# then expose the three records that were previously present only in the timeline/survey.
readme = read(README)
readme = readme.replace("**Update run: 23 July 2026.**", "**Update run: 24 July 2026.**")
missing_rows = [p["readme"] for p in PAPERS if p["doi"].lower() not in readme.lower()]
if missing_rows:
    sultan_line = next((line for line in readme.splitlines() if "10.1038/s41467-026-75177-4" in line), None)
    if not sultan_line:
        raise SystemExit("README: Sultan TLTM anchor not found")
    readme = replace_once(readme, sultan_line + "\n", sultan_line + "\n" + "\n".join(missing_rows) + "\n", "README insertion")
write(README, readme)

# Website: add searchable objects, update date, and increment the tracked count only
# for records that were absent before this run.
index = read(INDEX)
missing_objects = [p for p in PAPERS if p["doi"].lower() not in index.lower()]
if missing_objects:
    anchor = "    const papers=[\n"
    block = "\n".join("      " + p["index"] for p in missing_objects) + "\n"
    index = replace_once(index, anchor, anchor + block, "index paper-array insertion")
    count_pattern = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    match = count_pattern.search(index)
    if not match:
        raise SystemExit("index: tracked-entry counter not found")
    old_count = int(match.group(1))
    new_count = old_count + len(missing_objects)
    index = index[: match.start(1)] + str(new_count) + index[match.end(1) :]
index = index.replace("Updated 23 July 2026", "Updated 24 July 2026")
index = index.replace("Last updated: 23 July 2026", "Last updated: 24 July 2026")
write(INDEX, index)

# Master survey wrapper: update coverage date and leave a traceable audit marker.
survey = read(SURVEY)
marker = "% 24 July 2026 consistency audit: diffuse-aware passive, cost-effective FMCW, and diffusion-prior Fourier single-pixel records synchronized across public artifacts.\n"
if marker not in survey:
    survey = replace_once(survey, "%% bare_jrnl.tex\n", "%% bare_jrnl.tex\n" + marker, "survey audit marker")
survey = survey.replace("through 23 July 2026", "through 24 July 2026")
write(SURVEY, survey)

# Normalize final-venue bibliography metadata without changing stable citation keys.
bib = read(BIB)
for paper in PAPERS:
    bib = normalize_bib_entry(bib, paper["key"], paper["doi"], paper["bib"])
write(BIB, bib)

# Final cross-artifact assertions.
readme = read(README)
index = read(INDEX)
survey = read(SURVEY)
bib = read(BIB)
for paper in PAPERS:
    doi = paper["doi"].lower()
    if readme.lower().count(doi) != 1:
        raise SystemExit(f"README DOI count failed: {doi}")
    if index.lower().count(doi) != 1:
        raise SystemExit(f"index DOI count failed: {doi}")
    if bib.lower().count(doi) != 2:
        raise SystemExit(f"bibliography DOI/URL count failed: {doi}")
    if read(paper["article"]).count(paper["key"]) < 1:
        raise SystemExit(f"survey citation missing after synchronization: {paper['key']}")
if "through 24 July 2026" not in survey:
    raise SystemExit("survey coverage date was not updated")

print("Synchronized three NLOS cross-artifact gaps.")
