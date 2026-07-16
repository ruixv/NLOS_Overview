#!/usr/bin/env python3
"""Synchronize the SIGGRAPH Asia 2020 learned-feature NLOS milestone."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Learned Feature Embeddings for Non-Line-of-Sight Imaging and Recognition"
KEY = "chen_learned_2020"
URL = "https://doi.org/10.1145/3414685.3417825"


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
            f"| 2020 | [{TITLE}]({URL}) — Chen et al. | ACM TOG / SIGGRAPH Asia 2020 | "
            "Introduces a physics-structured learned embedding that maps transient measurements into a shared hidden-scene representation for high-resolution reconstruction, classification, and 2.5D detection; differentiable propagation, visibility, rendering, and depth modules enable synthetic-to-real generalization on measured NLOS scenes. |\n"
        )
        anchor = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, anchor, anchor + row, "README latest-table")

    milestone = (
        "   │     Chen et al.: learned NLOS feature embeddings — a shared physics-aware representation for reconstruction, detection, and recognition [SIGGRAPH Asia / TOG]\n"
    )
    if milestone not in text:
        anchor = "2020 ── Iseringhausen & Hullin: physically based transient analysis-by-synthesis — surface-, BRDF-, and visibility-aware NLOS inverse rendering [ACM TOG]\n"
        text = replace_once(text, anchor, anchor + milestone, "README 2020 milestone")

    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")

    if TITLE not in text:
        paper = (
            f'      {{cat:"latest learning active",title:"{TITLE}",authors:"Chen et al.",year:2020,'
            f'venue:"ACM TOG / SIGGRAPH Asia 2020",url:"{URL}",'
            'key:"A physics-structured learned embedding maps transient measurements to a shared hidden-scene representation for reconstruction, classification, and 2.5D detection; differentiable propagation, visibility, rendering, and depth modules generalize from synthetic training to real NLOS captures."},\n'
        )
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + paper, "homepage paper-array")
        text = replace_once(
            text,
            '<div class="stat"><b>102</b><span>tracked latest entries</span></div>',
            '<div class="stat"><b>103</b><span>tracked latest entries</span></div>',
            "homepage tracked-count",
        )

    old_heading = "Physically based inverse rendering, structured sparse scanning, and edge-resolved transients"
    new_heading = "Learned multi-task embeddings, physically based inverse rendering, structured sparse scanning, and edge-resolved transients"
    if old_heading in text:
        text = replace_once(text, old_heading, new_heading, "homepage 2020 timeline heading")

    anchor = (
        "Iseringhausen and Hullin introduced a physically based analysis-by-synthesis reconstruction that optimizes implicit hidden-surface geometry through a custom millisecond transient renderer with BRDF, shading, visibility, and self-occlusion terms;"
    )
    addition = (
        " Chen et al. learned a shared physics-aware feature space for hidden-scene reconstruction, classification, and 2.5D detection, combining differentiable propagation, visibility, rendering, and depth modules and transferring from synthetic training to real transients;"
    )
    if addition.strip() not in text:
        text = replace_once(text, anchor, anchor + addition, "homepage 2020 timeline paragraph")

    path.write_text(text, encoding="utf-8")


def update_learning_survey() -> None:
    path = ROOT / "article/4datadriven.tex"
    text = path.read_text(encoding="utf-8")
    heading = r"\noindent \textbf{Shared learned representations for reconstruction and recognition.}"
    if heading not in text:
        old = (
            "Recently, Chen \\etal~proposed an innovative NLOS imaging network structure rather than using the well-known U-Net like other works~\\cite{chen_learned_2020}. It first embedded the synthesized transient images into a feature space (feature embedding), then propagated to the hidden volume. After that, the network is divided into several parts with clear physical meaning, such as visibility network, image rendering, and depth estimation. To some extent, the physical model constrains the deep network to have good generalization ability. Although~\\cite{chen_learned_2020} contains multiple components, it can still conveniently run in an end-to-end mode during training."
        )
        new = r'''\vspace{0.8mm}
\noindent \textbf{Shared learned representations for reconstruction and recognition.}
Chen~\etal~introduced a learned feature-embedding framework that maps transient measurements into a common hidden-scene representation and then specializes it for high-resolution image reconstruction, classification, and 2.5D object detection~\cite{chen_learned_2020}. Rather than relying on a monolithic U-Net, the architecture incorporates differentiable modules with explicit physical roles, including transient propagation, visibility reasoning, image rendering, and depth estimation. Training on synthetically rendered diffuse and specular scenes while evaluating on measured transients demonstrated useful synthetic-to-real generalization. This work marks an early shift from single-output NLOS inversion toward reusable, task-aware representations, anticipating later physics-guided multi-task networks, transient pretraining, and transformer/operator models.'''
        text = replace_once(text, old, new, "learned-feature survey paragraph")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_learning_survey()
    print(f"Synchronized {TITLE} across README, homepage, timeline, survey, and bibliography citations.")


if __name__ == "__main__":
    main()
