#!/usr/bin/env python3
"""Synchronize the ICCV 2023 learnable inverse-kernel NLOS milestone."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Enhancing Non-Line-of-Sight Imaging via Learnable Inverse Kernel and Attention Mechanisms"
KEY = "yuLearnableInverseKernel2023"
URL = "https://openaccess.thecvf.com/content/ICCV2023/papers/Yu_Enhancing_Non-line-of-sight_Imaging_via_Learnable_Inverse_Kernel_and_Attention_Mechanisms_ICCV_2023_paper.pdf"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")

    if TITLE not in text:
        row = (
            f"| 2023 | [{TITLE}]({URL}) — Yu et al. | ICCV 2023 | "
            "Introduces a system-aware learned inverse kernel tailored to transient NLOS point-spread functions, together with attention mechanisms that refine hidden intensity and depth reconstruction; it forms a direct learned-physics bridge between shared feature embeddings and later transformer/generalizable-prior models. |\n"
        )
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + row, "README latest-table")

    milestone = (
        "   │     Yu et al.: learnable inverse kernel and attention — system-aware transient inversion for hidden intensity and depth [ICCV]\n"
    )
    if milestone not in text:
        anchor = (
            "   │     Li et al.: deep under-scanning reconstruction — learned transient recovery plus physics-aware volumetric inversion from grids as sparse as 8×8 [NeurIPS]\n"
        )
        text = replace_once(text, anchor, anchor + milestone, "README 2023 milestone")

    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")

    if TITLE not in text:
        paper = (
            f'      {{cat:"latest learning active",title:"{TITLE}",authors:"Yu et al.",year:2023,'
            f'venue:"ICCV 2023",url:"{URL}",'
            'key:"A system-aware learned inverse kernel is tailored to the transient NLOS point-spread function, while attention modules refine hidden intensity and depth; the method bridges physics-structured feature embeddings and later transformer or adaptive-prior reconstruction."},\n'
        )
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + paper, "homepage paper-array")
        text = replace_once(
            text,
            '<div class="stat"><b>103</b><span>tracked latest entries</span></div>',
            '<div class="stat"><b>104</b><span>tracked latest entries</span></div>',
            "homepage tracked-count",
        )

    old_heading = "Sparse and deep under-scanned transient recovery, differentiable rendering, joint LOS/NLOS shape, transformers, arbitrary patterns, virtual mirrors, neural implicit NLOS, and active corner cameras"
    new_heading = "Sparse and deep under-scanned transient recovery, learnable inverse kernels, differentiable rendering, joint LOS/NLOS shape, transformers, arbitrary patterns, virtual mirrors, neural implicit NLOS, and active corner cameras"
    if old_heading in text:
        text = replace_once(text, old_heading, new_heading, "homepage 2023 timeline heading")

    anchor = (
        "Li et al. paired learned transient densification with a physics-aware volume reconstruction network, retaining robustness at 8×8 scans and delivering 50× faster inference than an iterative under-scanning solver."
    )
    addition = (
        " Yu et al. learned a system-specific inverse kernel from the transient point-spread function and coupled it with attention mechanisms for hidden intensity and depth recovery, providing a CNN-based learned-physics step between LFE and later NLOST/generalizable-prior models."
    )
    if addition.strip() not in text:
        text = replace_once(text, anchor, anchor + addition, "homepage 2023 timeline paragraph")

    path.write_text(text, encoding="utf-8")


def update_active_table() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")
    if KEY not in text:
        anchor = "chen_learned_2020,wuNonLineofsightImaging2021"
        text = replace_once(
            text,
            anchor,
            f"chen_learned_2020,{KEY},wuNonLineofsightImaging2021",
            "active-SPAD citation list",
        )
    path.write_text(text, encoding="utf-8")


def update_learning_survey() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    heading = r"\noindent \textbf{Learnable inverse kernels and attention.}"
    if heading not in text:
        anchor = (
            "This work marks an early shift from single-output NLOS inversion toward reusable, task-aware representations, anticipating later physics-guided multi-task networks, transient pretraining, and transformer/operator models."
        )
        addition = r'''

\vspace{0.8mm}
\noindent \textbf{Learnable inverse kernels and attention.}
Yu~\etal~subsequently made the inverse operator itself trainable by introducing a learnable inverse kernel tailored to the transient NLOS point-spread function, together with attention mechanisms for recovering hidden intensity and depth~\cite{yuLearnableInverseKernel2023}. The method remains explicitly tied to the active transient forward model while allowing data-driven adaptation beyond a fixed analytic inverse. In the learned-reconstruction trajectory, it provides an intermediate step between the shared, task-aware feature embeddings of Chen~\etal~and later spatial--temporal transformers or adaptive physical-prior networks: physics determines the operator structure, whereas learned kernels and attention determine how measurement evidence is inverted and emphasized.'''
        text = replace_once(text, anchor, anchor + addition, "inverse-kernel survey paragraph")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_active_table()
    update_learning_survey()
    print(f"Synchronized {TITLE} across README, homepage, timeline, survey, and bibliography citations.")


if __name__ == "__main__":
    main()
