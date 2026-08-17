#!/usr/bin/env python3
"""Synchronize the scan-free SPAD-array resolution lineage found by citation tracing.

This run adds the missing Optics Express 2025 sub-pixel-modulation paper and
repairs two regressions: the 2024 APL Photonics scan-free paper and the 2025
Optics and Lasers in Engineering spatial-correlation paper are already cited
in README/survey prose, but their canonical website records and merged BibTeX
entries disappeared during later homepage/bibliography migrations.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING_BIB = ROOT / "egbib_20260817_scanfree_resolution_gap.bib"
MERGED_BIB = ROOT / "egbib_merged_20260711.bib"


def read(path: str | Path) -> str:
    p = path if isinstance(path, Path) else ROOT / path
    return p.read_text(encoding="utf-8")


def write(path: str | Path, text: str) -> None:
    p = path if isinstance(path, Path) else ROOT / path
    p.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one anchor, found {n}")
    return text.replace(old, new, 1)


def split_bib_entries(text: str) -> list[str]:
    entries: list[str] = []
    i = 0
    while True:
        at = text.find("@", i)
        if at < 0:
            break
        brace = text.find("{", at)
        if brace < 0:
            raise RuntimeError("Malformed BibTeX staging file")
        depth = 0
        j = brace
        while j < len(text):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    entries.append(text[at:j + 1].strip())
                    i = j + 1
                    break
            j += 1
        else:
            raise RuntimeError("Unbalanced BibTeX staging file")
    return entries


def bib_key(entry: str) -> str:
    m = re.match(r"@\w+\s*\{\s*([^,]+),", entry, flags=re.I)
    if not m:
        raise RuntimeError("Could not parse BibTeX key")
    return m.group(1).strip()


def bib_doi(entry: str) -> str:
    m = re.search(r"\bdoi\s*=\s*\{([^}]+)\}", entry, flags=re.I)
    if not m:
        raise RuntimeError(f"Missing DOI in staged entry {bib_key(entry)}")
    return m.group(1).strip()


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    doi = "10.1364/OE.569102"
    row = (
        "| 2025 | [Sub-pixel resolving modulation for non-line-of-sight imaging]"
        "(https://doi.org/10.1364/OE.569102) — Zhang et al. | "
        "Optics Express 33(14), 30783–30798 (2025) | Uses DMD pixel-shift "
        "modulation to synthesize sub-pixel relay sampling in scan-free NLOS "
        "and explicitly models temporal/spatial broadening; reports lateral-"
        "resolution improvement from about 7 cm to 1 cm while remaining "
        "compatible with established LCT, virtual-wave, and boundary-migration "
        "reconstruction back ends. |\n"
    )
    if doi not in text:
        marker = "10.1016/j.optlaseng.2025.109100"
        idx = text.find(marker)
        if idx < 0:
            raise RuntimeError("README spatial-correlation scan-free anchor missing")
        line_end = text.find("\n", idx)
        if line_end < 0:
            raise RuntimeError("README scan-free row has no line ending")
        text = text[: line_end + 1] + row + text[line_end + 1 :]

    timeline = (
        "   │     Zhang et al.: sub-pixel resolving modulation — DMD pixel shifting "
        "densifies scan-free relay samples and recovers about 1-cm lateral detail "
        "while retaining LCT/virtual-wave/boundary-migration compatibility "
        "[Optics Express]\n"
    )
    if "Zhang et al.: sub-pixel resolving modulation" not in text:
        anchor = (
            "   │     Zhang et al.: spatial-correlation scan-free NLOS — a 3D "
            "blur-kernel model and correlation resampling recover 2-cm detail at "
            "5 fps from a 16×16 detector [Optics and Lasers in Engineering]\n"
        )
        text = replace_once(text, anchor, timeline + anchor, "README 2025 scan-free timeline")

    # The two precursor/follow-up rows must already be public; fail rather than duplicate.
    for required in ("10.1063/5.0235687", "10.1016/j.optlaseng.2025.109100"):
        if required not in text:
            raise RuntimeError(f"README unexpectedly missing existing scan-free DOI {required}")
    write(path, text)


def update_website_source() -> None:
    path = "data/papers-source.html"
    text = read(path)
    additions: list[str] = []
    if "10.1063/5.0235687" not in text:
        additions.append(
            '      {cat:"active transient hardware scan-free spad array realtime",'
            'title:"Real-time scan-free non-line-of-sight imaging",authors:"Zhang et al.",'
            'year:2024,venue:"APL Photonics 9(12), 126101 (2024)",'
            'url:"https://doi.org/10.1063/5.0235687",'
            'key:"Parallel SPAD-array non-confocal boundary migration removes relay-wall raster scanning, reaching 151-fps transient acquisition and 19-fps end-to-end reconstruction; plug-in super-resolution reduces the array requirement from 32×32 to 8×8."},\n'
        )
    if "10.1364/OE.569102" not in text:
        additions.append(
            '      {cat:"latest active transient scan-free spad array dmd subpixel modulation resolution",'
            'title:"Sub-pixel resolving modulation for non-line-of-sight imaging",authors:"Zhang et al.",'
            'year:2025,venue:"Optics Express 33(14), 30783–30798 (2025)",'
            'url:"https://doi.org/10.1364/OE.569102",'
            'key:"DMD pixel-shift modulation synthesizes sub-pixel relay sampling and models temporal/spatial broadening, improving reported lateral resolution from about 7 cm to 1 cm while remaining compatible with LCT, virtual-wave, and boundary-migration solvers."},\n'
        )
    if "10.1016/j.optlaseng.2025.109100" not in text:
        additions.append(
            '      {cat:"active transient scan-free non-confocal spatial correlation realtime",'
            'title:"High-resolution and real-time non-line-of-sight imaging based on spatial correlation",authors:"Zhang et al.",'
            'year:2025,venue:"Optics and Lasers in Engineering 193, 109100 (2025)",'
            'url:"https://doi.org/10.1016/j.optlaseng.2025.109100",'
            'key:"SCBSF-NLOS combines a 3D blur-kernel model with spatial-correlation resampling, reporting about 2-cm lateral resolution and 5-fps dynamic reconstruction from a 16×16 detector."},\n'
        )
    if additions:
        anchor = "    const papers=[\n"
        text = replace_once(text, anchor, anchor + "".join(additions), "canonical website paper array")

    if "DMD pixel-shift modulation then densified scan-free relay samples" not in text:
        old = (
            "SCBSF-NLOS coupled scan-free capture to a 3D blur-kernel model and "
            "spatial-correlation super-resolution, reaching 2-cm detail at 5 fps."
        )
        new = (
            "DMD pixel-shift modulation then densified scan-free relay samples and "
            "recovered about 1-cm lateral detail while preserving compatibility with "
            "established transient solvers. " + old
        )
        text = replace_once(text, old, new, "canonical website 2025 scan-free timeline")

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
    # The V2 explorer is generated from the canonical data source above; index.html
    # only needs its visible living-survey date synchronized with the current run.
    path = "index.html"
    text = read(path)
    text = re.sub(r"Updated \d{1,2} Aug 2026", "Updated 17 Aug 2026", text, count=1)
    write(path, text)


def update_active() -> None:
    path = "article/2active.tex"
    text = read(path)

    # Normalize the SPAD-array table row and include all three papers in the lineage.
    row_pattern = re.compile(
        r"\\cite\{nam_real-time_2020,jinScannerlessNonlineofsightThree2020,[^}]*\} & Pulsed laser & SPAD array & Time of fight &  3D reconstruction\\\\%%%% Table body"
    )
    replacement = (
        r"\cite{nam_real-time_2020,jinScannerlessNonlineofsightThree2020,"
        r"zhangRealTimeScanFreeNLOS2024,zhangSubpixelResolvingNLOS2025,"
        r"zhangSpatialCorrelationNLOS2025,albertEyeSafeNLOS2026} & Pulsed laser & "
        r"SPAD array & Time of fight &  3D reconstruction\\%%%% Table body"
    )
    text, n = row_pattern.subn(lambda _: replacement, text, count=1)
    if n != 1:
        raise RuntimeError("Active-method SPAD-array table row not found")

    heading = r"\textbf{Scan-free transient acquisition and spatial-correlation reconstruction.}"
    start = text.find(heading)
    if start < 0:
        raise RuntimeError("Existing scan-free survey paragraph missing")
    block_start = text.rfind(r"\vspace{0.8mm}", 0, start)
    block_end = text.find(r"\vspace{0.8mm}", start + len(heading))
    if block_start < 0 or block_end < 0:
        raise RuntimeError("Could not delimit scan-free survey paragraph")
    block = r"""\vspace{0.8mm}
\noindent \textbf{Scan-free SPAD-array acquisition and sub-pixel resolution recovery.}
Zhang~\etal~first removed relay-wall raster scanning by combining parallel SPAD-array acquisition with non-confocal time-to-space boundary migration~\cite{zhangRealTimeScanFreeNLOS2024}. The system reports 151-fps transient acquisition and 19-fps end-to-end hidden-scene imaging, while a plug-in super-resolution stage reduces the detector requirement from $32\times32$ to $8\times8$. Their subsequent PSM-NLOS method uses DMD pixel-shift modulation to synthesize sub-pixel relay samples and explicitly models spatial and temporal signal broadening~\cite{zhangSubpixelResolvingNLOS2025}; the reported lateral resolution improves from approximately 7\,cm to 1\,cm while the measurements remain compatible with LCT, virtual-wave, and boundary-migration reconstruction back ends. The later SCBSF-NLOS formulation models scan-free non-confocal measurements using a three-dimensional blur kernel and spatial-correlation resampling~\cite{zhangSpatialCorrelationNLOS2025}, reporting approximately 2\,cm lateral resolution and 5-fps dynamic reconstruction with a $16\times16$ detector. Together, this lineage shifts real-time transient NLOS from acquisition parallelism, through physical sub-pixel sampling densification, to model-based computational resampling.

"""
    text = text[:block_start] + block + text[block_end:]
    write(path, text)


def merge_bibliography() -> None:
    merged = read(MERGED_BIB)
    staged = read(STAGING_BIB)
    lower = merged.lower()
    appended: list[str] = []
    for entry in split_bib_entries(staged):
        key = bib_key(entry)
        doi = bib_doi(entry)
        key_token = "{" + key.lower() + ","
        if doi.lower() in lower:
            if key_token not in lower:
                raise RuntimeError(f"DOI {doi} already exists under a different BibTeX key")
            continue
        if key_token in lower:
            raise RuntimeError(f"BibTeX key {key} exists but DOI {doi} is absent")
        appended.append(entry)
        lower += "\n" + entry.lower()
    if appended:
        merged = merged.rstrip() + "\n\n" + "\n\n".join(appended) + "\n"
        write(MERGED_BIB, merged)


def update_master() -> None:
    path = "bare_jrnl.tex"
    text = read(path)
    marker = "% 17 August 2026 citation/consistency trace: scan-free SPAD-array acquisition, sub-pixel modulation, and spatial-correlation lineage synchronized.\n"
    if marker not in text:
        text = marker + text
    write(path, text)


def update_note() -> None:
    path = ROOT / "updates/2026-08-17-scanfree-spad-resolution-sync.md"
    text = read(path)
    text = text.replace(
        "Status: pending guarded integration/build.",
        "Status: integrated by the guarded workflow; public-source changes are committed only after the LaTeX/PDF and cross-artifact checks pass.",
    )
    write(path, text)


def validate_sources() -> None:
    readme = read("README.md")
    site = read("data/papers-source.html")
    active = read("article/2active.tex")
    bib = read(MERGED_BIB)
    index = read("index.html")

    dois = ["10.1063/5.0235687", "10.1364/OE.569102", "10.1016/j.optlaseng.2025.109100"]
    keys = ["zhangRealTimeScanFreeNLOS2024", "zhangSubpixelResolvingNLOS2025", "zhangSpatialCorrelationNLOS2025"]
    for doi in dois:
        if doi not in readme:
            raise RuntimeError(f"README missing {doi}")
        if doi not in site:
            raise RuntimeError(f"Canonical website source missing {doi}")
        if bib.lower().count(doi.lower()) != 2:  # doi field + DOI URL
            raise RuntimeError(f"Merged bibliography has unexpected occurrence count for {doi}")
    for key in keys:
        if key not in active:
            raise RuntimeError(f"Active survey missing citation key {key}")
        if bib.lower().count("{" + key.lower() + ",") != 1:
            raise RuntimeError(f"Merged bibliography key count is not one for {key}")
    if "Sub-pixel resolving modulation for non-line-of-sight imaging" not in readme or "Sub-pixel resolving modulation for non-line-of-sight imaging" not in site:
        raise RuntimeError("Sub-pixel paper missing from a public paper list")
    if "Updated 17 Aug 2026" not in index:
        raise RuntimeError("V2 index living-survey date was not synchronized")


def main() -> None:
    update_readme()
    update_website_source()
    update_index()
    update_active()
    merge_bibliography()
    update_master()
    update_note()
    validate_sources()
    if STAGING_BIB.exists():
        STAGING_BIB.unlink()
    print("scan-free SPAD resolution lineage synchronized")


if __name__ == "__main__":
    main()
