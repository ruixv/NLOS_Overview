#!/usr/bin/env python3
"""Synchronize citation-traced irregular-relay, undersampling, and 2D NLOS papers."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPERS = [
    {
        "title": "CUDA-accelerated Non-line-of-sight imaging with irregular relay surfaces",
        "authors": "Sun et al.",
        "year": 2026,
        "venue": "Optics and Lasers in Engineering 2026",
        "url": "https://doi.org/10.1016/j.optlaseng.2025.109591",
        "cat": "latest active irregular relay gpu backprojection",
        "key": "sunCUDAIrregularRelayNLOS2026",
        "summary": "Runs filtered back projection directly on non-planar relay geometry and arbitrary nonuniform source-detector samples, avoiding planarization or resampling; a CUDA implementation provides at least two orders of magnitude acceleration while retaining competitive measured-data reconstruction quality.",
    },
    {
        "title": "Reprojection-Guided Non-Line-of-Sight Imaging Under Irregular Undersampling",
        "authors": "Cui, Yue, Yang",
        "year": 2025,
        "venue": "IEEE JSTSP 2025",
        "url": "https://doi.org/10.1109/JSTSP.2025.3620710",
        "cat": "latest active learning irregular undersampling reprojection",
        "key": "cuiReprojectionGuidedNLOS2025",
        "summary": "Recovers dense denoised transients from sparse, irregular, or fragmented relay measurements; range-space reprojection supplies physics-grounded guidance that spatio-temporal modulation blocks inject adaptively, improving simulated-to-real and cross-relay generalization.",
    },
    {
        "title": "Looking Around Flatland: End-to-End 2D Real-Time NLOS Imaging",
        "authors": "Peña, Gutierrez, Marco",
        "year": 2025,
        "venue": "IEEE TCI 2025",
        "url": "https://doi.org/10.1109/TCI.2025.3536092",
        "cat": "latest active transient simulation phasor field realtime",
        "key": "penaFlatlandNLOS2025",
        "summary": "Reformulates transient light transport in self-contained 2D worlds and couples it to phasor-field camera models, enabling end-to-end real-time simulation, progressive reconstruction, and controlled analysis of filtering, reflectance, and geometry at up to five orders of magnitude lower cost than equivalent 3D experiments.",
    },
]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return text.replace(old, new, 1)


def insert_before_once(text: str, marker: str, addition: str, label: str) -> str:
    if addition.strip() in text:
        return text
    return replace_once(text, marker, addition.rstrip() + "\n\n" + marker, label)


def paper_object(paper: dict[str, object]) -> str:
    summary = str(paper["summary"]).replace('"', "'")
    return (
        f'      {{cat:"{paper["cat"]}",title:"{paper["title"]}",authors:"{paper["authors"]}",'
        f'year:{paper["year"]},venue:"{paper["venue"]}",url:"{paper["url"]}",key:"{summary}"}},'
    )


def append_to_timeline_year(text: str, year: int, sentence: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if f'<div class="year">{year}</div>' in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one homepage timeline row for {year}, found {len(matches)}")
    line = lines[matches[0]]
    if sentence.strip() not in line:
        closing = "</p></div></div>"
        if closing not in line:
            raise RuntimeError(f"Timeline closing marker missing for {year}")
        lines[matches[0]] = line.replace(closing, " " + sentence.strip() + closing, 1)
    return "".join(lines)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    rows = ""
    for p in PAPERS:
        if f"[{p['title']}]" not in text:
            rows += f"| {p['year']} | [{p['title']}]({p['url']}) - {p['authors']} | {p['venue']} | {p['summary']} |\n"
    if rows:
        header = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, header, header + rows, "README latest-additions header")

    anchor = "   |     18 July 2026 core-citation tracing: forward-citation and modality-expansion audit completed\n"
    lines = (
        "   |     Direct CUDA back projection extends active transient reconstruction to arbitrary irregular relay geometry and nonuniform scans [Optics and Lasers in Engineering]\n"
        "   |     Reprojection-guided transient recovery advances learned NLOS from fixed sparse grids to fragmented and irregular relay sampling [IEEE JSTSP]\n"
        "   |     Flatland provides a real-time 2D transient-and-phasor testbed for controlled end-to-end NLOS analysis [IEEE TCI]\n"
        "   |     18 July 2026 irregular-relay citation trace: three final-venue records integrated across public, survey, bibliography, and build artifacts\n"
    )
    if "18 July 2026 irregular-relay citation trace" not in text:
        text = replace_once(text, anchor, lines + anchor, "README core-citation marker")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    additions = [paper_object(p) for p in PAPERS if f'title:"{p["title"]}"' not in text]
    if additions:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + "\n".join(additions) + "\n", "homepage paper array")

    stat = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
    match = stat.search(text)
    if not match:
        raise RuntimeError("Homepage tracked-entry statistic not found")
    count = len(re.findall(r'^\s*\{cat:"[^"]+",title:"', text, flags=re.MULTILINE))
    if int(match.group(2)) != count:
        text = stat.sub(lambda m: m.group(1) + str(count) + m.group(3), text, count=1)

    text = append_to_timeline_year(
        text,
        2025,
        "Reprojection-guided recovery generalized learned transient completion to irregular and fragmented relay samples, while Flatland enabled real-time end-to-end 2D transient and phasor-field experimentation.",
    )
    text = append_to_timeline_year(
        text,
        2026,
        "CUDA-filtered back projection operated directly on non-planar relay geometry and arbitrary nonuniform scans, removing the planarization and resampling requirement.",
    )
    path.write_text(text, encoding="utf-8")


def update_active() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")

    if "sunCUDAIrregularRelayNLOS2026" not in text:
        text = replace_once(
            text,
            ",shiSpecularFlightPathNLOS2026}",
            ",shiSpecularFlightPathNLOS2026,sunCUDAIrregularRelayNLOS2026,penaFlatlandNLOS2025}",
            "active-SPAD table citation tail",
        )

    block = r"""\vspace{0.8mm}
\noindent \textbf{Direct arbitrary-relay back projection on GPUs.}
Sun~\etal~returned to the geometry-general back-projection model and made it practical for irregular relay surfaces and arbitrary nonuniform source--detector samples~\cite{sunCUDAIrregularRelayNLOS2026}. Rather than flattening or resampling the measurements onto a planar grid, the method accumulates each measured ellipsoidal constraint in its native geometry, applies a frequency-domain bandpass filter to reduce noise and multipath artifacts, and parallelizes the full reconstruction with CUDA. Measured non-planar-wall experiments report at least two orders of magnitude acceleration over CPU execution while remaining competitive with CC-SOCR, Virtual Scanning, and 3D RSD. This complements proxy-plane wave propagation: geometric generality can also be obtained by retaining the original back-projection operator and removing its computational bottleneck.

\vspace{0.8mm}
\noindent \textbf{Real-time two-dimensional transient testbeds.}
Pe\~na~\etal~reformulated the transient path integral for self-contained two-dimensional worlds and coupled it to phasor-field NLOS camera models~\cite{penaFlatlandNLOS2025}. The resulting end-to-end pipeline performs progressive transient simulation and hidden-scene reconstruction in real time while exposing controlled variations in filtering, reflectance, geometry, and acquisition parameters. Reported computational savings reach five orders of magnitude relative to equivalent three-dimensional experiments, with substantial memory reduction. Flatland is therefore not a replacement for measured 3D benchmarks, but a complementary instrument for rapidly testing assumptions and failure modes along the Velten--LCT--phasor-field trajectory before committing to expensive capture or rendering.
"""
    marker = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Reconstruction topology}"
    text = insert_before_once(text, marker, block, "active reconstruction-topology marker")
    path.write_text(text, encoding="utf-8")


def update_data_driven() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    block = r"""\vspace{0.8mm}
\noindent \textbf{Reprojection-guided recovery from irregular relay samples.}
Cui~\etal~extended transient completion beyond fixed sparse grids to noisy, irregularly undersampled, and spatially fragmented relay measurements~\cite{cuiReprojectionGuidedNLOS2025}. Their transient-recovery network is guided by a range-space reprojection module that extracts measurement-intrinsic structure; spatio-temporal modulation blocks then control where and how strongly this physical guidance affects denoising and interpolation. Evaluation on simulated and measured data shows improved transfer across relay layouts. In the development from under-scanning recovery and Virtual Scanning to TransDiff, this work makes reprojection consistency an explicit conditioning signal rather than relying only on an implicit learned prior.
"""
    marker = "\\bookmark[dest=\\HyperLocalCurrentHref,level=2]{Challenges and Prospects}"
    text = insert_before_once(text, marker, block, "deep-learning challenges marker")
    path.write_text(text, encoding="utf-8")


def update_master_tex() -> None:
    path = ROOT / "bare_jrnl.tex"
    text = path.read_text(encoding="utf-8")
    marker = "\\input{article/2active.tex}"
    comment = "% 18 July 2026 irregular-relay citation trace integrates CUDA arbitrary-relay BP, reprojection-guided undersampling, and the Flatland 2D transient testbed.\n"
    if comment.strip() not in text:
        text = replace_once(text, marker, comment + marker, "master survey section anchor")
    path.write_text(text, encoding="utf-8")


def update_note() -> None:
    path = ROOT / "updates/2026-07-18-irregular-relay-flatland-citation-trace.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "STATUS: STAGED — public sources and PDF have not yet been rebuilt.",
        "STATUS: SYNCHRONIZED — source artifacts were updated by the guarded workflow; PDF validity is checked before its separate commit.",
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_active()
    update_data_driven()
    update_master_tex()
    update_note()
    print("Synchronized three verified irregular-relay and Flatland NLOS papers.")


if __name__ == "__main__":
    main()
