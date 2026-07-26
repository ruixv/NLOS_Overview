#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article" / "2active.tex"
ABSTRACT = ROOT / "article" / "0abstract.tex"
MASTER = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"

DOIS = {
    "poisson": "10.1117/12.3091668",
    "semantic": "10.1117/12.3094245",
    "spaett": "10.1364/OE.584776",
}

EXPECTED_TITLES = {
    "poisson": "Fast NLOS imaging at low sampling rates based on Poisson modeling",
    "semantic": "Semantic-guided under sampling scanning for improving real-time performance of NLOS imaging",
    "spaett": "Fast SPAD-array timing-error correction with time-referencing for non-line-of-sight imaging",
}


def die(msg: str) -> None:
    raise RuntimeError(msg)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        die(f"{label}: expected exactly one anchor, found {n}")
    return text.replace(old, new, 1)


def crossref(doi: str) -> dict:
    encoded = urllib.parse.quote(doi, safe="")
    req = urllib.request.Request(
        f"https://api.crossref.org/works/{encoded}",
        headers={"User-Agent": "NLOS-Overview-updater/1.0 (mailto:raygeng@hku.hk)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if payload.get("status") != "ok":
        die(f"Crossref lookup failed for {doi}")
    return payload["message"]


def norm_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def validate_metadata() -> dict[str, dict]:
    meta: dict[str, dict] = {}
    for key, doi in DOIS.items():
        record = crossref(doi)
        title = (record.get("title") or [""])[0]
        if norm_title(title) != norm_title(EXPECTED_TITLES[key]):
            die(f"Crossref title mismatch for {doi}: {title!r}")
        if record.get("DOI", "").lower() != doi.lower():
            die(f"Crossref DOI mismatch for {doi}")
        meta[key] = record
    return meta


def authors_from_crossref(record: dict) -> str:
    names: list[str] = []
    for author in record.get("author", []):
        family = (author.get("family") or "").strip()
        given = (author.get("given") or "").strip()
        if family and given:
            names.append(f"{family}, {given}")
        elif family:
            names.append(family)
        elif given:
            names.append(given)
    if not names:
        die(f"No authors in Crossref record for {record.get('DOI')}")
    return " and ".join(names)


def bib_escape(value: str) -> str:
    replacements = {
        "&": r"\&",
        "é": r"{\'e}",
        "É": r"{\'E}",
        "á": r"{\'a}",
        "Á": r"{\'A}",
        "ö": r'{\"o}',
        "Ö": r'{\"O}',
        "ü": r'{\"u}',
        "Ü": r'{\"U}',
        "ß": r"{\ss}",
    }
    for source, target in replacements.items():
        value = value.replace(source, target)
    return value


def build_bib(meta: dict[str, dict]) -> str:
    poisson_authors = bib_escape(authors_from_crossref(meta["poisson"]))
    semantic_authors = bib_escape(authors_from_crossref(meta["semantic"]))

    return rf"""
@article{{spaettSPADTimingNLOS2026,
  author = {{Spaett, Alexander and Schertzer, St{{\'e}}phane and Nguyen, Thai-An and Laurenzis, Martin}},
  title = {{Fast {{SPAD}}-Array Timing-Error Correction with Time-Referencing for Non-Line-of-Sight Imaging}},
  journal = {{Optics Express}},
  volume = {{34}},
  number = {{12}},
  pages = {{22596--22613}},
  year = {{2026}},
  publisher = {{Optica Publishing Group}},
  doi = {{10.1364/OE.584776}},
  url = {{https://doi.org/10.1364/OE.584776}}
}}

@inproceedings{{yangPoissonLowSamplingNLOS2026,
  author = {{{poisson_authors}}},
  title = {{Fast {{NLOS}} Imaging at Low Sampling Rates Based on Poisson Modeling}},
  booktitle = {{11th International Symposium on Advanced Optical Manufacturing and Testing Technologies ({{AOMATT}} 2025)}},
  series = {{Proceedings of SPIE}},
  volume = {{13992}},
  pages = {{1399223}},
  year = {{2026}},
  publisher = {{SPIE}},
  doi = {{10.1117/12.3091668}},
  url = {{https://doi.org/10.1117/12.3091668}}
}}

@inproceedings{{wangSemanticUndersamplingNLOS2026,
  author = {{{semantic_authors}}},
  title = {{Semantic-Guided Under Sampling Scanning for Improving Real-Time Performance of {{NLOS}} Imaging}},
  booktitle = {{Fifth International Computational Imaging Conference ({{CITA}} 2025)}},
  series = {{Proceedings of SPIE}},
  volume = {{14000}},
  pages = {{140004W}},
  year = {{2026}},
  publisher = {{SPIE}},
  doi = {{10.1117/12.3094245}},
  url = {{https://doi.org/10.1117/12.3094245}}
}}
""".strip() + "\n"


def patch_readme() -> None:
    text = README.read_text(encoding="utf-8")

    if EXPECTED_TITLES["spaett"] not in text:
        separator = "|------|-------|----------------|----------------|\n"
        rows = (
            "| 2026 | **Fast SPAD-array timing-error correction with time-referencing for non-line-of-sight imaging** | "
            "[Optics Express](https://doi.org/10.1364/OE.584776) | Corrects approximately 6% pixel-to-pixel mean-bin-width variation and 0.6% bin-level fluctuation in SPAD-array TCSPC data with a precomputed lookup table, then derives an absolute NLOS time reference from intrinsic diffraction-wave and lens-flare peaks; the calibration sharpens measured non-confocal and simulated confocal reconstructions without an external timing target. |\n"
            "| 2026 | **Fast NLOS imaging at low sampling rates based on Poisson modeling** | "
            "[Proc. SPIE / AOMATT 2025](https://doi.org/10.1117/12.3091668) | Formulates photon-limited transient inversion with a Poisson likelihood and a GPU-parallel Nesterov proximal-gradient solver; measured 64×64×4096 transients retain strong reconstruction quality at 1.56% sampling with roughly one-second processing per frame. |\n"
            "| 2026 | **Semantic-guided under sampling scanning for improving real-time performance of NLOS imaging** | "
            "[Proc. SPIE / CITA 2025](https://doi.org/10.1117/12.3094245) | Uses a semantic target contour to restrict the relay-wall scan to one quarter of the original area and then applies neighborhood sparse sampling, reducing density to one fifth while limiting the reported PSNR and SSIM degradation. |\n"
        )
        text = replace_once(text, separator, separator + rows, "README latest-additions table")

    timeline_anchor = (
        "2026 ── Yin et al.: Si-SPAD and phase-congruency regularization enable 200 m all-day active NLOS "
        "under 94,314 lx sunlight [Optics and Lasers in Engineering]\n"
    )
    if "Spaett et al.: per-pixel SPAD-array timing correction" not in text:
        addition = (
            "   │     Spaett et al.: per-pixel SPAD-array timing correction and intrinsic LOS-peak time referencing prevent TCSPC aggregation blur in measured NLOS reconstruction [Optics Express]\n"
            "   │     Yang et al.: Poisson-likelihood Nesterov optimization approaches direct-method speed at 1.56% measured transient sampling [Proc. SPIE / AOMATT]\n"
            "   │     Wang et al.: semantic contours guide relay-wall scan-area and sampling-density reduction for faster active NLOS acquisition [Proc. SPIE / CITA]\n"
        )
        text = replace_once(text, timeline_anchor, timeline_anchor + addition, "README 2026 timeline")

    text = text.replace("190%2B_curated_papers", "210%2B_curated_papers")
    README.write_text(text, encoding="utf-8")


def remove_stale_index_record(text: str, title: str, year: int, venue: str) -> str:
    pattern = (
        r'^[ \t]*\{cat:[^\n]*title:"'
        + re.escape(title)
        + r'"[^\n]*year:'
        + str(year)
        + r',venue:"'
        + re.escape(venue)
        + r'"[^\n]*\},\n'
    )
    updated, n = re.subn(pattern, "", text, count=1, flags=re.MULTILINE)
    if n not in (0, 1):
        die(f"Unexpected duplicate stale index record: {title}")
    return updated


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")

    text = remove_stale_index_record(
        text,
        "Iterating the Transient Light Transport Matrix for Non-Line-of-Sight Imaging",
        2024,
        "arXiv 2024",
    )
    text = remove_stale_index_record(
        text,
        "Non-line-of-sight imaging in the presence of scattering media using phasor fields",
        2023,
        "arXiv 2023",
    )

    if EXPECTED_TITLES["spaett"] not in text:
        objects = (
            '      {cat:"latest active hardware calibration spad array transient",title:"Fast SPAD-array timing-error correction with time-referencing for non-line-of-sight imaging",authors:"Spaett et al.",year:2026,venue:"Optics Express 2026",url:"https://doi.org/10.1364/OE.584776",key:"Equalizes pixel-dependent TCSPC bin widths with a precomputed lookup table and derives an absolute NLOS time reference from intrinsic diffraction-wave and lens-flare peaks, sharpening measured non-confocal and simulated confocal phasor-field reconstructions without external timing calibration."},\n'
            '      {cat:"latest active reconstruction optimization sparse poisson",title:"Fast NLOS imaging at low sampling rates based on Poisson modeling",authors:"Yang et al.",year:2026,venue:"Proc. SPIE / AOMATT 2025",url:"https://doi.org/10.1117/12.3091668",key:"Combines a Poisson transient likelihood with GPU-parallel Nesterov proximal-gradient iterations, reporting strong measured-data reconstruction at 1.56% sampling and approximately one second per frame."},\n'
            '      {cat:"latest active acquisition semantic undersampling",title:"Semantic-guided under sampling scanning for improving real-time performance of NLOS imaging",authors:"Wang et al.",year:2026,venue:"Proc. SPIE / CITA 2025",url:"https://doi.org/10.1117/12.3094245",key:"Projects a hidden-target semantic contour to the relay wall to reduce scan area to one quarter, then applies neighborhood sparse sampling at one-fifth density with limited reported PSNR and SSIM loss."},\n'
        )
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + objects, "website paper array")

    timeline_marker = "SPAD-array timing calibration"
    if timeline_marker not in text:
        pattern = re.compile(
            r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
            re.DOTALL,
        )
        match = pattern.search(text)
        if not match:
            die("website 2026 timeline block not found")
        sentence = (
            " SPAD-array timing calibration and intrinsic LOS-peak referencing corrected detector-dependent temporal grids before inversion. "
            "Poisson-likelihood accelerated optimization and semantic-guided relay-wall scan allocation added complementary low-sampling routes: one improves the inverse solver at 1.56% measured sampling, while the other reduces both scanned area and point density using task-level priors."
        )
        text = text[: match.start()] + match.group(1) + match.group(2) + sentence + match.group(3) + text[match.end() :]

    count = len(re.findall(r'\{cat:"', text))
    stat_pattern = re.compile(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>')
    text, n = stat_pattern.subn(
        f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',
        text,
        count=1,
    )
    if n != 1:
        die("website tracked-entry counter not found")

    INDEX.write_text(text, encoding="utf-8")


def patch_active() -> None:
    text = ACTIVE.read_text(encoding="utf-8")

    if "spaettSPADTimingNLOS2026" not in text:
        table_anchor = "liTimeMultiplexingNLOS2025}"
        table_replacement = (
            "liTimeMultiplexingNLOS2025,spaettSPADTimingNLOS2026,"
            "yangPoissonLowSamplingNLOS2026,wangSemanticUndersamplingNLOS2026}"
        )
        text = replace_once(text, table_anchor, table_replacement, "active-system table citation")

        prose_anchor = (
            "while showing that acquisition complexity can be reduced by optical temporal coding rather than only by "
            "learned transient completion or detector arrays.\n"
        )
        paragraphs = r"""

\vspace{0.8mm}
\noindent \textbf{SPAD-array timing calibration and intrinsic time referencing.}
Parallel SPAD arrays avoid relay-wall raster detection but introduce detector-dependent temporal grids: manufacturing tolerances change the mean time-bin width across pixels and produce differential nonlinearity within each pixel. Spaett~\etal~measured approximately six-percent pixel-to-pixel mean-bin-width variation and 0.6-percent bin-level fluctuation, then corrected the resulting aggregation blur with a precomputed lookup table~\cite{spaettSPADTimingNLOS2026}. For NLOS reconstruction, they additionally infer a scan-specific absolute reference from the midpoint of intrinsic diffraction-wave and lens-flare peaks, removing unknown LOS path delays without an external calibration target. Experiments with two non-confocal SPAD-array systems and simulated confocal data show sharper phasor-field reconstructions, placing sensor calibration and temporal alignment upstream of the conventional inverse operator.

\vspace{0.8mm}
\noindent \textbf{Poisson optimization and semantic scan allocation at low sampling rates.}
Two proceedings studies further reduce acquisition and reconstruction cost from complementary directions. Yang~\etal~formulate low-count transient inversion with a Poisson likelihood and solve it using GPU-parallel Nesterov-accelerated proximal gradients~\cite{yangPoissonLowSamplingNLOS2026}; on measured $64\times64\times4096$ transients, the method retains favorable reconstruction quality at 1.56\% sampling and reports approximately one second per frame, narrowing the speed gap between iterative reconstruction and direct LCT-like operators. Wang~\etal~instead use a target semantic contour to restrict the relay-wall scan area to one quarter and then apply neighborhood sparse sampling at one-fifth spatial density~\cite{wangSemanticUndersamplingNLOS2026}. The latter is explicitly task-prior dependent, but it demonstrates that under-scanning can be optimized jointly in spatial support and density rather than treated only as uniform grid decimation.
"""
        text = replace_once(text, prose_anchor, prose_anchor + paragraphs, "active-method prose insertion")

    ACTIVE.write_text(text, encoding="utf-8")


def patch_master_and_abstract() -> None:
    text = MASTER.read_text(encoding="utf-8")
    marker = "% 26 July 2026 citation trace: SPAD-array timing calibration, Poisson low-sampling inversion, and semantic-guided under-scanning synchronized.\n"
    if marker not in text:
        text = replace_once(text, "%% bare_jrnl.tex\n", "%% bare_jrnl.tex\n" + marker, "master trace marker")
    text = text.replace("through 24 July 2026", "through 26 July 2026")
    text = text.replace("A curated list of 190+ NLOS papers", "A curated list of 210+ NLOS papers")
    MASTER.write_text(text, encoding="utf-8")

    abstract = ABSTRACT.read_text(encoding="utf-8")
    abstract = abstract.replace("A curated list of 190+ NLOS papers", "A curated list of 210+ NLOS papers")
    ABSTRACT.write_text(abstract, encoding="utf-8")


def patch_bibliography(meta: dict[str, dict]) -> None:
    text = BIB.read_text(encoding="utf-8")
    entries = build_bib(meta)
    keys = [
        "spaettSPADTimingNLOS2026",
        "yangPoissonLowSamplingNLOS2026",
        "wangSemanticUndersamplingNLOS2026",
    ]
    existing = [key for key in keys if f"{{{key}," in text]
    if existing and len(existing) != len(keys):
        die(f"partial bibliography integration detected: {existing}")
    if not existing:
        if not text.endswith("\n"):
            text += "\n"
        text += "\n" + entries
        BIB.write_text(text, encoding="utf-8")


def validate_sources() -> None:
    checks = {
        README: [
            EXPECTED_TITLES["spaett"],
            EXPECTED_TITLES["poisson"],
            EXPECTED_TITLES["semantic"],
        ],
        INDEX: [
            EXPECTED_TITLES["spaett"],
            EXPECTED_TITLES["poisson"],
            EXPECTED_TITLES["semantic"],
        ],
        ACTIVE: [
            "spaettSPADTimingNLOS2026",
            "yangPoissonLowSamplingNLOS2026",
            "wangSemanticUndersamplingNLOS2026",
        ],
        BIB: [
            "10.1364/OE.584776",
            "10.1117/12.3091668",
            "10.1117/12.3094245",
        ],
    }
    for path, needles in checks.items():
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                die(f"{path}: missing {needle}")
    bib = BIB.read_text(encoding="utf-8").lower()
    for doi in DOIS.values():
        if bib.count(doi.lower()) != 2:
            die(f"bibliography DOI occurrence count is not exactly two for {doi}")


def main() -> int:
    meta = validate_metadata()
    patch_readme()
    patch_index()
    patch_active()
    patch_master_and_abstract()
    patch_bibliography(meta)
    validate_sources()
    print("NLOS SPAD/sampling citation-trace integration completed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
