#!/usr/bin/env python3
"""Idempotently integrate the ECCV 2020 C2NLOS transient-sinogram paper."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Efficient Non-Line-of-Sight Imaging from Transient Sinograms"
ARXIV = "https://arxiv.org/abs/2008.02787"
PROJECT = "https://marikoisogawa.github.io/project/c2nlos"
KEY = "isogawaTransientSinograms2020"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")

    old_row = (
        f"| 2020 | [{TITLE}]({ARXIV}) — Isogawa et al. | arXiv 2020 | "
        "Introduces circular confocal NLOS (C2NLOS) scanning and transient-sinogram reconstruction, reducing relay-wall measurements while preserving hidden-position and image recovery. |"
    )
    new_row = (
        f"| 2020 | [{TITLE}]({PROJECT}) — Isogawa et al. | ECCV 2020 | "
        "Introduces circular confocal NLOS (C2NLOS) acquisition: a one-dimensional circular relay-wall scan produces transient sinograms whose sinusoid parameters encode hidden 3D positions, enabling Hough-, inverse-Radon-, and linear-inversion reconstructions with about an order of magnitude fewer measurements than dense raster scans. |"
    )
    text = replace_once(text, old_row, new_row, "README C2NLOS row")

    old_timeline = (
        "2020 ── Rapp et al.: edge-resolved transient imaging — 2.5D room-scale recovery from 45 edge-coded scans [Nature Comm.]"
    )
    new_timeline = (
        "2020 ── Isogawa et al.: C2NLOS transient sinograms — 1D circular confocal scanning with far fewer measurements [ECCV]\n"
        "   │     Rapp et al.: edge-resolved transient imaging — 2.5D room-scale recovery from 45 edge-coded scans [Nature Comm.]"
    )
    text = replace_once(text, old_timeline, new_timeline, "README 2020 timeline")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")

    old_paper = (
        '      {cat:"latest active",title:"Efficient Non-Line-of-Sight Imaging from Transient Sinograms",authors:"Isogawa et al.",year:2020,venue:"arXiv 2020",url:"https://arxiv.org/abs/2008.02787",key:"Circular confocal NLOS scanning and transient-sinogram reconstruction with fewer relay-wall measurements."},'
    )
    new_paper = (
        '      {cat:"latest active",title:"Efficient Non-Line-of-Sight Imaging from Transient Sinograms",authors:"Isogawa et al.",year:2020,venue:"ECCV 2020",url:"https://marikoisogawa.github.io/project/c2nlos",key:"C2NLOS replaces a dense 2D relay-wall raster with a 1D circular confocal scan; transient sinusoids encode hidden 3D positions and support Hough, inverse-Radon, and compact linear reconstructions from roughly an order of magnitude fewer measurements."},'
    )
    text = replace_once(text, old_paper, new_paper, "homepage C2NLOS paper")

    old_timeline = (
        '<div class="tl"><div class="year">2020</div><div class="tl-body"><strong>Edge-resolved transient imaging</strong><p>Rapp et al. combined pulsed single-photon transients with vertical-edge occlusion coding, recovering 2.5D room layouts over a 180° field of view from a 1.5 cm illumination arc and only 45 scan positions.</p></div></div>'
    )
    new_timeline = (
        '<div class="tl"><div class="year">2020</div><div class="tl-body"><strong>Structured sparse scanning and edge-resolved transients</strong><p>Isogawa et al. showed that a one-dimensional circular confocal scan forms a transient sinogram and preserves enough information for hidden localization and image reconstruction with far fewer measurements; Rapp et al. combined pulsed single-photon transients with vertical-edge occlusion coding, recovering 2.5D room layouts over a 180° field of view from a 1.5 cm illumination arc and only 45 scan positions.</p></div></div>'
    )
    text = replace_once(text, old_timeline, new_timeline, "homepage 2020 timeline")
    path.write_text(text, encoding="utf-8")


def update_survey() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")

    if KEY not in text:
        table_old = "wuNonLineofsightImaging2021,yeCompressedSensingActive2021,wuMiniaturizedTCSPC2024}"
        table_new = "wuNonLineofsightImaging2021,yeCompressedSensingActive2021,isogawaTransientSinograms2020,wuMiniaturizedTCSPC2024}"
        text = replace_once(text, table_old, table_new, "active-method table citation list")

        anchor = (
            "O'Toole \\etal~\\cite{otooleConfocalNonlineofsightImaging2018}~found that under confocal conditions, the forward imaging process can be expressed in the form of three-dimensional convolution, thus using efficient deconvolution algorithms (such as Wiener filtering) to perform the efficient reconstruction. It reduced the time complexity to $O(N^3log(N))$, which greatly improved the reconstruction speed. "
        )
        paragraph = (
            "\n\n\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Circular confocal acquisition and transient sinograms.}\n"
            "Isogawa~\\etal~asked whether confocal NLOS could reduce the relay-wall scan itself rather than only accelerate inversion~\\cite{isogawaTransientSinograms2020}. Their C$^2$NLOS acquisition samples a one-dimensional circle instead of a dense two-dimensional raster. After the light-cone-transform time reparameterization, each hidden scatterer traces a sinusoid whose amplitude, phase, and offset encode its three-dimensional location; Hough voting, inverse-Radon reconstruction, or compact linear inversion then recover hidden positions and images. This direct extension of confocal LCT and $f$--$k$ migration established structured scan-path design as a route toward rapid NLOS capture, anticipating later sparse, irregular, and learning-based sampling methods."
        )
        text = replace_once(text, anchor, anchor + paragraph, "survey LCT paragraph")

    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    print(f"Synchronized {TITLE}")


if __name__ == "__main__":
    main()
