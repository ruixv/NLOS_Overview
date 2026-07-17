#!/usr/bin/env python3
"""Synchronize three citation-traced 2026 NLOS papers across public and survey artifacts."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

STEREO = "Stereo non-line-of-sight imaging"
COMPACT = "Compact non-line-of-sight imager at long range"
MDNLOS = "A model decomposition method for the real-time non-line-of-sight imaging"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def paper_object(title: str, authors: str, venue: str, url: str, cat: str, key: str) -> str:
    return f'      {{cat:"{cat}",title:"{title}",authors:"{authors}",year:2026,venue:"{venue}",url:"{url}",key:"{key}"}},'


def append_active_table_keys(text: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if "Pulsed laser & SPAD & Time of fight &  3D reconstruction" in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one active SPAD reconstruction row, found {len(matches)}")
    line = lines[matches[0]]
    match = re.search(r"\\cite\{([^}]*)\}", line)
    if not match:
        raise RuntimeError("Active SPAD row has no citation list")
    keys = [k.strip() for k in match.group(1).split(",") if k.strip()]
    for key in ("luesiaStereoNLOS2026", "zengCompactLongRangeNLOS2026", "yangModelDecompositionNLOS2026"):
        if key not in keys:
            keys.append(key)
    lines[matches[0]] = line[:match.start(1)] + ",".join(keys) + line[match.end(1):]
    return "".join(lines)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    rows = [
        (STEREO, f"| 2026 | [{STEREO}](https://doi.org/10.1007/s00371-025-04340-7) — Luesia-Lahoz, Cartiel, Muñoz | The Visual Computer 2026 | Introduces a two-relay-wall stereo configuration in which phasor fields treat both walls as generalized virtual apertures. Combining same-wall and cross-wall illumination/detection paths reduces missing-cone ambiguity and provides surface-orientation cues that are unavailable from a single relay wall. |"),
        (COMPACT, f"| 2026 | [{COMPACT}](https://doi.org/10.1364/OE.597084) — Zeng et al. | Optics Express 2026 | Integrates optimized collection optics, adaptive scan-synchronized gating, a gated InGaAs/InP SPAD, and fast electronics into a compact outdoor prototype. It demonstrates daylight kilometer-scale NLOS, approximately 4 cm spatial resolution, and 2 fps imaging of simple moving targets. |"),
        (MDNLOS, f"| 2026 | [{MDNLOS}](https://doi.org/10.1016/j.isci.2026.115828) — Yang et al. | iScience 2026 | Reformulates sparse transient NLOS reconstruction as a spectrally filtered non-negative LASSO problem and decomposes the optimization into GPU-parallelizable subproblems. The reported system reconstructs 128×128 hidden images from 64 measurements in 4.6 s. |"),
    ]
    header = "|------|-------|----------------|----------------|\n"
    insertion = "".join(row + "\n" for title, row in rows if f"[{title}]" not in text)
    if insertion:
        text = replace_once(text, header, header + insertion, "README latest-table")

    if "Luesia-Lahoz et al.: stereo relay walls" not in text:
        anchor = "   │     Wang et al.: diffuse-aware attention encoding for passive NLOS through relay-wall diffusion [Optics Express]\n"
        addition = (
            "   │     Luesia-Lahoz et al.: stereo relay walls — dual virtual apertures reduce the missing cone and recover orientation cues [The Visual Computer]\n"
            "   │     Zeng et al.: compact kilometer-range NLOS — adaptive gating and efficient optics enable daylight 2 fps operation [Optics Express]\n"
            "   │     Yang et al.: MD-NLOS — spectrally filtered model decomposition for sparse real-time reconstruction [iScience]\n"
        )
        text = replace_once(text, anchor, anchor + addition, "README 2026 citation-tracing timeline")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    objects = [
        (STEREO, paper_object(STEREO, "Luesia-Lahoz, Cartiel, Muñoz", "The Visual Computer 2026", "https://doi.org/10.1007/s00371-025-04340-7", "latest active wave", "Two relay walls act as generalized phasor-field virtual apertures; same-wall and cross-wall paths reduce missing-cone ambiguity and expose hidden-surface orientation cues.")),
        (COMPACT, paper_object(COMPACT, "Zeng et al.", "Optics Express 2026", "https://doi.org/10.1364/OE.597084", "latest active hardware long-range", "A compact gated-SPAD prototype combines optimized optics, adaptive gating, and fast electronics for daylight kilometer-scale NLOS, 4 cm resolution, and 2 fps imaging.")),
        (MDNLOS, paper_object(MDNLOS, "Yang et al.", "iScience 2026", "https://doi.org/10.1016/j.isci.2026.115828", "latest active optimization sparse", "MD-NLOS uses spectral filtering and non-negative-LASSO model decomposition to reconstruct 128×128 hidden images from 64 transient samples in 4.6 seconds.")),
    ]
    new_lines = ""
    inserted = 0
    for title, obj in objects:
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
        text = pattern.sub(lambda m: f"{m.group(1)}{int(m.group(2)) + inserted}{m.group(3)}", text, count=1)

    pattern_2026 = re.compile(r'^\s*<div class="tl"><div class="year">2026</div>.*$', re.MULTILINE)
    new_2026 = '      <div class="tl"><div class="year">2026</div><div class="tl-body"><strong>Deployable sensing, stereo relay geometry, learned physical operators, sparse real-time optimization, dynamic transient completion, thermal/passive reconstruction, consumer LiDAR, and RF geometry</strong><p>PICL and learned LCT embed detector and inverse physics in trainable models; TransVID densifies dynamic transient video; NLOSFormer, MDUNet, and diffuse-aware attention broaden passive sensing; stereo phasor-field acquisition uses two relay walls to reduce the missing cone; MD-NLOS decomposes sparse non-negative inversion for rapid reconstruction; compact gated-SPAD hardware reaches kilometer-scale daylight operation; consumer LiDAR and radar/LiDAR benchmarks broaden deployable modalities; and Gaussian transient rendering supports arbitrary relay geometry.</p></div></div>'
    if len(pattern_2026.findall(text)) != 1:
        raise RuntimeError("Expected exactly one 2026 homepage timeline row")
    text = pattern_2026.sub(new_2026, text, count=1)
    path.write_text(text, encoding="utf-8")


def update_active() -> None:
    path = ROOT / "article/2active.tex"
    text = append_active_table_keys(path.read_text(encoding="utf-8"))

    if "zengCompactLongRangeNLOS2026" not in text[text.index(r"\end{table*}") + len(r"\end{table*}"):]:
        anchor = "\n\vspace{0.8mm}\n\noindent \\textbf{Active Focusing for High Resolution.}"
        paragraph = (
            "\n\vspace{0.8mm}\n"
            "\\noindent \\textbf{Compact kilometer-range NLOS imaging.}\n"
            "Long-range outdoor NLOS is limited jointly by the cubic-bounce photon budget, daylight background, detector dead time, and the bulk of laboratory timing hardware. Zeng~\\etal~co-designed optimized transmit/receive optics, scan-synchronized adaptive gating, a gated InGaAs/InP SPAD, and fast control electronics in a compact prototype~\\cite{zengCompactLongRangeNLOS2026}. The system reports daylight imaging at a relay-wall distance of approximately one kilometer, roughly 4~cm spatial resolution, and 2~fps reconstruction of simple moving targets. This result advances the earlier kilometer-range demonstration from proof of range toward a portable, high-efficiency instrument and shows that practical progress can come from hardware-level photon collection and gating as much as from a new inverse algorithm.\n"
        )
        text = replace_once(text, anchor, paragraph + anchor, "active focusing heading")

    if "yangModelDecompositionNLOS2026" not in text[text.index(r"\end{table*}") + len(r"\end{table*}"):]:
        anchor = "\n\vspace{0.8mm}\n\noindent \\textbf{Inverse Rendering.}"
        paragraph = (
            "\n\vspace{0.8mm}\n"
            "\\noindent \\textbf{Model-decomposition reconstruction from sparse transients.}\n"
            "Sparse transient acquisition reduces scan time but usually shifts the computational burden to large regularized inverse problems. Yang~\\etal~formulated MD-NLOS as a spectrally filtered non-negative LASSO problem and decomposed it into smaller updates suited to parallel GPU execution~\\cite{yangModelDecompositionNLOS2026}. Their experiments reconstruct $128\\times128$ hidden images from only 64 relay measurements in 4.6~s. In the development from analytic LCT and structured scan paths toward learned completion, this work occupies a complementary optimization route: it preserves an explicit linear transport model and sparsity prior while restructuring the solver for practical low-sample latency.\n"
        )
        text = replace_once(text, anchor, paragraph + anchor, "inverse-rendering heading")

    if "luesiaStereoNLOS2026" not in text[text.index(r"\end{table*}") + len(r"\end{table*}"):]:
        anchor = "\nThe wave-based approaches have two attractive advantages:"
        paragraph = (
            "\n\vspace{0.8mm}\n"
            "\\noindent \\textbf{Stereo relay-wall acquisition.}\n"
            "The missing cone is not only an algorithmic artifact: with one finite relay aperture, surfaces whose orientations direct little transport toward that aperture remain intrinsically weak. Luesia-Lahoz~\\etal~introduced a stereo NLOS configuration with two distinct relay walls and used phasor fields to treat both as generalized virtual camera apertures~\\cite{luesiaStereoNLOS2026}. The reconstruction combines measurements that illuminate and detect on the same wall with cross-wall paths that illuminate one wall and observe the other. These complementary angular views improve conditioning, diminish missing-cone artifacts, and provide surface-orientation cues from the relative wall contributions, extending phasor-field imaging from a single virtual aperture to coordinated multi-aperture capture.\n"
        )
        text = replace_once(text, anchor, paragraph + anchor, "wave-method advantages paragraph")

    path.write_text(text, encoding="utf-8")


def update_note() -> None:
    path = ROOT / "updates/2026-07-17-stereo-longrange-citation-tracing.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "# Stereo, long-range, and sparse-model NLOS citation-tracing update — 17 July 2026\n\n"
        "This update adds three direct NLOS papers absent from the public repository snapshot.\n\n"
        "- Luesia-Lahoz, Cartiel, and Muñoz, *Stereo non-line-of-sight imaging*, The Visual Computer 42, article 148 (2026), DOI `10.1007/s00371-025-04340-7`.\n"
        "- Zeng et al., *Compact non-line-of-sight imager at long range*, Optics Express 34(9), 16911–16921 (2026), DOI `10.1364/OE.597084`.\n"
        "- Yang et al., *A model decomposition method for the real-time non-line-of-sight imaging*, iScience 29(6), 115828 (2026), DOI `10.1016/j.isci.2026.115828`.\n\n"
        "The first is a forward-citation descendant of phasor-field virtual wave optics and directly addresses missing-cone visibility with two relay apertures. The second extends the Velten/LCT/phasor-field active hardware trajectory to compact daylight kilometer-range operation. The third retains an explicit transient forward model while decomposing sparse non-negative LASSO inversion for GPU-parallel low-latency reconstruction. The PR workflow applies all pending 17 July synchronizers, merges canonical bibliography records, clean-builds the LaTeX survey, renders both PDFs, and rejects undefined or duplicate citations before committing the regenerated binary.\n",
        encoding="utf-8",
    )


def main() -> None:
    update_readme()
    update_index()
    update_active()
    update_note()
    print("Synchronized stereo, compact long-range, and model-decomposition NLOS papers.")


if __name__ == "__main__":
    main()
