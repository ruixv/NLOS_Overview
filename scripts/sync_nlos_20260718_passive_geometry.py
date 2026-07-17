#!/usr/bin/env python3
"""Synchronize the 18 July 2026 passive-NLOS and geometry update."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATE_OLD = "17 July 2026"
DATE_NEW = "18 July 2026"

PASSIVE_10M = "Passive non-line-of-sight imaging at 10 meters"
HPDI = "Neural Networks Meet Light Transport Physics for Passive Non-Line-of-Sight Imaging Enhancement"
GEOMETRY_OLD = "Geometric Constrained Non-Line-of-Sight Imaging"
GEOMETRY = "Geometry-Constrained Non-Line-of-Sight Imaging"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def replace_line_containing(text: str, needle: str, replacement: str, label: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if needle in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one {label} line containing {needle!r}, found {len(matches)}")
    ending = "\n" if lines[matches[0]].endswith("\n") else ""
    lines[matches[0]] = replacement.rstrip("\n") + ending
    return "".join(lines)


def insert_line_before(text: str, needle: str, new_line: str, label: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if needle in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one {label} line containing {needle!r}, found {len(matches)}")
    lines.insert(matches[0], new_line.rstrip("\n") + "\n")
    return "".join(lines)


def insert_after_heading_block(text: str, heading: str, block: str, label: str) -> str:
    marker = f"\\noindent \\textbf{{{heading}}}"
    starts = [m.start() for m in re.finditer(re.escape(marker), text)]
    if len(starts) != 1:
        raise RuntimeError(f"Expected one {label} heading, found {len(starts)}")
    end = text.find("\n\n", starts[0])
    if end < 0:
        raise RuntimeError(f"Could not locate paragraph end after {label}")
    return text[: end + 2] + block.strip("\n") + "\n\n" + text[end + 2 :]


def append_timeline_sentence(text: str, year: int, marker: str, sentence: str) -> str:
    if marker in text:
        return text
    lines = text.splitlines(keepends=True)
    needle = f'<div class="year">{year}</div>'
    matches = [i for i, line in enumerate(lines) if needle in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one homepage timeline row for {year}, found {len(matches)}")
    line = lines[matches[0]]
    closing = "</p></div></div>"
    if closing not in line:
        raise RuntimeError(f"Homepage timeline row for {year} has an unexpected structure")
    ending = "\n" if line.endswith("\n") else ""
    core = line[:-1] if ending else line
    core = core.replace(closing, " " + sentence + closing, 1)
    lines[matches[0]] = core + ending
    return "".join(lines)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(DATE_OLD, DATE_NEW)

    old_geometry_needle = f"[{GEOMETRY_OLD}]"
    final_geometry_row = (
        f"| 2026 | [{GEOMETRY}](https://doi.org/10.1109/TVCG.2026.3684832) — Liu et al. | "
        "IEEE TVCG 2026 | Jointly reconstructs hidden albedo and surface normals while regularizing normal-field variation with a shape operator. The geometry-aware formulation improves fine surface recovery on synthetic and measured transients and reports approximately 30× faster optimization than an earlier surface-reconstruction baseline. |"
    )
    if old_geometry_needle in text:
        text = replace_line_containing(text, old_geometry_needle, final_geometry_row, "README geometry venue correction")
    elif f"[{GEOMETRY}]" not in text:
        raise RuntimeError("Existing geometry-constrained README record is missing")

    new_rows = [
        (
            PASSIVE_10M,
            f"| 2025 | [{PASSIVE_10M}](https://doi.org/10.1364/OL.573268) — Zhou et al. | Optics Letters 2025 | Combines pattern-based calibration with low-rank matrix decomposition to enhance weak wall-encoded signals and separate ambient background. The ordinary-camera system demonstrates passive NLOS at a 10 m wall-to-camera distance and 4.5 m wall-to-object distance, with centimeter-scale resolution at an SBR as low as −13 dB. |",
        ),
        (
            HPDI,
            f"| 2026 | [{HPDI}](https://doi.org/10.1109/TCI.2026.3653304) — Liang et al. | IEEE TCI 2026 | Introduces HPDI, a dual-path hybrid of a physics-informed coarse-to-fine pathway and a data-driven implicit reconstruction pathway, followed by adaptive fusion. It improves fidelity, generalization, and data efficiency across passive scenes with and without occluders while retaining an interpretable light-transport branch. |",
        ),
    ]
    insertion = ""
    for title, row in new_rows:
        if f"[{title}]" not in text:
            insertion += row + "\n"
    if insertion:
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + insertion, "README latest-additions table")

    if "Zhou et al.: 10 m passive NLOS" not in text:
        marker = "\n```\n\n---\n\n## Taxonomy"
        timeline = (
            "2025 ── Zhou et al.: 10 m passive NLOS — pattern calibration and low-rank background separation move ordinary-camera computational periscopy to long range [Optics Letters]\n"
            "2026 ── Liang et al.: HPDI — physics-informed coarse-to-fine reconstruction fused with an implicit data-driven passive pathway [IEEE TCI]\n"
            "   │     Liu et al.: geometry-constrained NLOS — shape-operator regularization jointly recovers albedo and hidden surface normals [IEEE TVCG]\n"
        )
        text = replace_once(text, marker, "\n" + timeline + "```\n\n---\n\n## Taxonomy", "README timeline ending")

    path.write_text(text, encoding="utf-8")


def paper_object(title: str, authors: str, year: int, venue: str, url: str, cat: str, key: str) -> str:
    return f'      {{cat:"{cat}",title:"{title}",authors:"{authors}",year:{year},venue:"{venue}",url:"{url}",key:"{key}"}},'


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace(DATE_OLD, DATE_NEW)

    geometry_obj = paper_object(
        GEOMETRY,
        "Liu et al.",
        2026,
        "IEEE TVCG 2026",
        "https://doi.org/10.1109/TVCG.2026.3684832",
        "latest active reconstruction",
        "Shape-operator regularization controls hidden surface-normal variation during joint albedo and normal recovery, improving geometric detail while substantially reducing optimization cost.",
    )
    if f'title:"{GEOMETRY_OLD}"' in text:
        text = replace_line_containing(text, f'title:"{GEOMETRY_OLD}"', geometry_obj, "homepage geometry venue correction")
    elif f'title:"{GEOMETRY}"' not in text:
        raise RuntimeError("Existing geometry-constrained homepage record is missing")

    objects = [
        paper_object(
            PASSIVE_10M,
            "Zhou et al.",
            2025,
            "Optics Letters 2025",
            "https://doi.org/10.1364/OL.573268",
            "latest passive",
            "Pattern-based calibration and low-rank matrix decomposition separate weak wall-encoded passive signals from ambient background, enabling centimeter-scale recovery at 10 m and −13 dB SBR.",
        ),
        paper_object(
            HPDI,
            "Liang et al.",
            2026,
            "IEEE TCI 2026",
            "https://doi.org/10.1109/TCI.2026.3653304",
            "latest passive learning",
            "HPDI adaptively fuses an interpretable physics-informed coarse-to-fine pathway with a data-driven implicit reconstruction pathway for higher-fidelity and more generalizable passive NLOS imaging.",
        ),
    ]
    inserted = 0
    new_lines = ""
    for obj, title in zip(objects, (PASSIVE_10M, HPDI)):
        if f'title:"{title}"' not in text:
            new_lines += obj + "\n"
            inserted += 1
    if new_lines:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + new_lines, "homepage paper array")

    if inserted:
        pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
        match = pattern.search(text)
        if not match:
            raise RuntimeError("Homepage tracked-count anchor is missing")
        new_count = int(match.group(2)) + inserted
        text = pattern.sub(lambda m: f"{m.group(1)}{new_count}{m.group(3)}", text, count=1)

    text = append_timeline_sentence(
        text,
        2025,
        "10 m passive NLOS",
        "Zhou et al. extended ordinary-camera computational periscopy to 10 m through pattern calibration and low-rank separation of weak indirect signals from ambient background.",
    )
    text = append_timeline_sentence(
        text,
        2026,
        "HPDI adaptively fuses",
        "HPDI adaptively fuses physics-informed and implicit data-driven passive reconstruction, while geometry-constrained inversion regularizes hidden surface normals with a shape operator.",
    )
    path.write_text(text, encoding="utf-8")


def update_passive() -> None:
    path = ROOT / "article/3passive.tex"
    text = path.read_text(encoding="utf-8")

    if "zhouPassiveNLOS10m2025" not in text:
        paragraph = r"""
\vspace{0.8mm}
\noindent \textbf{Long-range passive NLOS under severe background.}
The practical range of ordinary-camera passive NLOS is commonly limited by geometric attenuation and ambient illumination. Zhou~\etal~combined pattern-based calibration with low-rank matrix decomposition to enhance the wall-encoded indirect component and separate slowly varying background contributions~\cite{zhouPassiveNLOS10m2025}. Their experiment placed the camera 10~m from the relay wall and the hidden object 4.5~m from the wall, retaining centimeter-scale resolution at an SBR as low as $-13$~dB. This result extends the computational-periscopy trajectory from laboratory-scale conditioning improvements toward long-range passive sensing with inexpensive hardware.
"""
        text = insert_after_heading_block(
            text,
            "Diffuse-aware attention encoding for passive NLOS.",
            paragraph,
            "diffuse-aware passive paragraph",
        )
        row = r"    \cite{zhouPassiveNLOS10m2025} & Ambient light & Conventional camera & Pattern calibration and low-rank background separation & Long-range 2D reconstruction\\%%%% Table body"
        text = insert_line_before(text, "\\cite{rajiMDUNet2026} &", row, "passive technology table")

    if "liangHPDIPassiveNLOS2026" not in text:
        row = r"    \cite{liangHPDIPassiveNLOS2026} & Hybrid physics--data dual path & Scattering image & 2D image & Ambient-light passive NLOS with or without an occluder & Synthetic and experimental data\\%%%%"
        text = insert_line_before(text, "\\cite{du2025passive} &", row, "passive deep-learning table")

    path.write_text(text, encoding="utf-8")


def update_learning() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    if "liangHPDIPassiveNLOS2026" not in text:
        paragraph = r"""
\vspace{0.8mm}
\noindent \textbf{Hybrid physics--data passive enhancement.}
Purely data-driven passive reconstruction can be difficult to interpret and generalize, whereas a fixed light-transport inverse may preserve physics but lose perceptual detail. Liang~\etal~proposed HPDI, a dual-path architecture that combines a physics-informed coarse-to-fine pathway with a data-driven implicit reconstruction pathway and learns an adaptive fusion of their outputs~\cite{liangHPDIPassiveNLOS2026}. Evaluation across passive datasets with and without explicit occluders shows how a recognizable transport model and scene-specific statistical priors can be complementary rather than competing constraints. This hybrid design extends computational periscopy and blind transport factorization toward trainable passive solvers with improved fidelity, generalization, and data efficiency.
"""
        text = insert_after_heading_block(
            text,
            "SPAD-aware physics-informed cascade learning.",
            paragraph,
            "PICL paragraph",
        )
    path.write_text(text, encoding="utf-8")


def update_active() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    if "Geometry-constrained joint normal and albedo reconstruction." not in text:
        paragraph = r"""
\vspace{0.8mm}
\noindent \textbf{Geometry-constrained joint normal and albedo reconstruction.}
Surface orientation supplies geometric and illumination cues that are discarded by a scalar albedo volume, but jointly estimating albedo and normals substantially enlarges the inverse problem. Liu~\etal~regularized hidden normal-field variation through the shape operator and jointly reconstructed surface normals and albedo from transient measurements~\cite{liuGeometricConstrainedNLOS2025}. The method improves geometric detail and robustness on synthetic and measured data while reporting approximately $30\times$ faster optimization than an earlier surface-reconstruction baseline. Its final IEEE TVCG publication formalizes a trajectory from direct surface optimization toward explicit differential-geometric priors for hidden-scene recovery.
"""
        text = insert_after_heading_block(
            text,
            "Beyond volumetric albedo: direct surface optimization.",
            paragraph,
            "direct surface-optimization paragraph",
        )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_passive()
    update_learning()
    update_active()
    print("Synchronized passive long-range, HPDI, and geometry-constrained NLOS updates.")


if __name__ == "__main__":
    main()
