from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
PASSIVE = ROOT / "article" / "3passive.tex"
LEARNING = ROOT / "article" / "4datadriven.tex"
MASTER = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"

PAPERS = [
    {
        "title": "Speckle-correlation-based non-line-of-sight imaging under white-light illumination",
        "authors_short": "Zhou et al.",
        "year": 2024,
        "venue": "Optics & Laser Technology 2024",
        "doi": "10.1016/j.optlastec.2023.110231",
        "cat": "latest passive steady-state white-light speckle correlation",
        "summary": "ZPF-SCI combines Zernike-polynomial envelope correction with low-pass filtering before speckle autocorrelation and phase retrieval, retaining reconstruction under ambient illumination and camera misalignment with an ordinary camera.",
        "key": "zhouWhiteLightSpeckleNLOS2024",
    },
    {
        "title": "Non-line-of-sight imaging under white-light illumination using physics-enhanced deep learning",
        "authors_short": "Fu et al.",
        "year": 2025,
        "venue": "Applied Optics 2025",
        "doi": "10.1364/AO.561658",
        "cat": "latest passive learning steady-state white-light speckle physics",
        "summary": "Embeds a speckle-correlation forward model and a denoising prior in a physics-enhanced network, enabling ordinary-camera hidden-image reconstruction under inexpensive broadband white-light illumination.",
        "key": "fuPhysicsEnhancedWhiteLightNLOS2025",
    },
    {
        "title": "Single-shot non-line-of-sight imaging based on the statistical average characteristics of a speckle pattern under ambient light",
        "authors_short": "Zhou et al.",
        "year": 2025,
        "venue": "Optics Communications 2025",
        "doi": "10.1016/j.optcom.2025.131847",
        "cat": "latest passive steady-state single-shot speckle ambient-light",
        "summary": "Extracts object-spectrum amplitude from the covariance of one random speckle pattern, removing multi-frame stitching and the conventional memory-effect field-of-view limit while reconstructing at −2.06 dB SNR.",
        "key": "zhouSingleShotSpeckleNLOS2025",
    },
    {
        "title": "Isolating Signals in Passive Non-Line-of-Sight Imaging Using Spectral Content",
        "authors_short": "Hashemi et al.",
        "year": 2025,
        "venue": "IEEE TPAMI 2025",
        "doi": "10.1109/TPAMI.2023.3301336",
        "cat": "latest passive multispectral clutter separation",
        "summary": "Uses multispectral unmixing and a convex known-spectrum formulation to separate desired wall-mediated radiance from much stronger clutter, improving passive reconstruction under realistic backgrounds.",
        "key": "hashemiSpectralContentPassiveNLOS2025",
    },
    {
        "title": "Hyperspectral passive non-line-of-sight imaging with band selection",
        "authors_short": "Chen et al.",
        "year": 2025,
        "venue": "Expert Systems with Applications 2025",
        "doi": "10.1016/j.eswa.2025.128394",
        "cat": "latest passive hyperspectral learning transformer dataset",
        "summary": "HSBS-Net selects informative spectral bands, applies a spectral-energy-guided KA-Transformer and robust sparse loss, and introduces HP-NLOS for physical full-colour passive hyperspectral reconstruction.",
        "key": "chenHyperspectralBandSelectionNLOS2025",
    },
    {
        "title": "CMFormer: Non-line-of-sight imaging with a memory-efficient MetaFormer network",
        "authors_short": "Zhang et al.",
        "year": 2025,
        "venue": "Optics and Lasers in Engineering 2025",
        "doi": "10.1016/j.optlaseng.2025.108875",
        "cat": "latest active learning metaformer memory-efficient transient",
        "summary": "A convolutional MetaFormer token mixer, aggregate feature transmission, cross-layer attention and checkpointing reduce 3D transient memory cost while reaching 8-fps reconstruction on consumer GPUs.",
        "key": "zhangCMFormerNLOS2025",
    },
]

BIB_ENTRIES = r'''
@article{zhouWhiteLightSpeckleNLOS2024,
  author = {Zhou, Meiling and Zhang, Yang and Wang, Ping and Li, Runze and Peng, Tong and Min, Junwei and Yan, Shaohui and Yao, Baoli},
  title = {Speckle-correlation-based non-line-of-sight imaging under white-light illumination},
  journal = {Optics \& Laser Technology},
  volume = {170},
  pages = {110231},
  year = {2024},
  doi = {10.1016/j.optlastec.2023.110231},
  url = {https://doi.org/10.1016/j.optlastec.2023.110231},
  publisher = {Elsevier}
}

@article{fuPhysicsEnhancedWhiteLightNLOS2025,
  author = {Fu, Zhenfeng and Wang, Fei and Zheng, Shanshan and Situ, Guohai},
  title = {Non-line-of-sight imaging under white-light illumination using physics-enhanced deep learning},
  journal = {Applied Optics},
  volume = {64},
  number = {16},
  pages = {4607--4614},
  year = {2025},
  doi = {10.1364/AO.561658},
  url = {https://doi.org/10.1364/AO.561658},
  publisher = {Optica Publishing Group}
}

@article{zhouSingleShotSpeckleNLOS2025,
  author = {Zhou, Junjie and Yin, Liang and Hu, Minglong and Ren, Shilin and Ding, Yingchun},
  title = {Single-shot non-line-of-sight imaging based on the statistical average characteristics of a speckle pattern under ambient light},
  journal = {Optics Communications},
  volume = {586},
  pages = {131847},
  year = {2025},
  doi = {10.1016/j.optcom.2025.131847},
  url = {https://doi.org/10.1016/j.optcom.2025.131847},
  publisher = {Elsevier}
}

@article{hashemiSpectralContentPassiveNLOS2025,
  author = {Hashemi, Connor and Avelar, Rafael and Leger, James},
  title = {Isolating Signals in Passive Non-Line-of-Sight Imaging Using Spectral Content},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  volume = {47},
  number = {9},
  pages = {7328--7339},
  year = {2025},
  doi = {10.1109/TPAMI.2023.3301336},
  url = {https://doi.org/10.1109/TPAMI.2023.3301336},
  publisher = {IEEE}
}

@article{chenHyperspectralBandSelectionNLOS2025,
  author = {Chen, Mingyang and Jin, Shaohui and Liu, Mengge and Xu, Ziqin and Liu, Hao and Xu, Mingliang},
  title = {Hyperspectral passive non-line-of-sight imaging with band selection},
  journal = {Expert Systems with Applications},
  volume = {290},
  pages = {128394},
  year = {2025},
  doi = {10.1016/j.eswa.2025.128394},
  url = {https://doi.org/10.1016/j.eswa.2025.128394},
  publisher = {Elsevier}
}

@article{zhangCMFormerNLOS2025,
  author = {Zhang, Shihao and Jin, Shaohui and Liu, Hao and Li, Yue and Jiang, Xiaoheng and Xu, Mingliang},
  title = {{CMFormer}: Non-line-of-sight imaging with a memory-efficient {MetaFormer} network},
  journal = {Optics and Lasers in Engineering},
  volume = {187},
  pages = {108875},
  year = {2025},
  doi = {10.1016/j.optlaseng.2025.108875},
  url = {https://doi.org/10.1016/j.optlaseng.2025.108875},
  publisher = {Elsevier}
}
'''.strip()


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Required file is missing: {path}")
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, old: str, new: str) -> None:
    if new != old:
        path.write_text(new, encoding="utf-8")
        print(f"updated {path.relative_to(ROOT)}")
    else:
        print(f"unchanged {path.relative_to(ROOT)}")


def insert_once(text: str, anchor: str, addition: str, label: str, before: bool = False) -> str:
    if addition.strip() in text:
        return text
    if anchor not in text:
        raise SystemExit(f"Fail-closed: anchor not found for {label}: {anchor!r}")
    return text.replace(anchor, addition + anchor if before else anchor + addition, 1)


def update_readme() -> None:
    old = read(README)
    text = old
    header = "|------|-------|----------------|----------------|\n"
    rows = ""
    for p in PAPERS:
        if p["title"].lower() in text.lower() or p["doi"].lower() in text.lower():
            continue
        rows += (
            f'| {p["year"]} | [{p["title"]}](https://doi.org/{p["doi"]}) — {p["authors_short"]} '
            f'| {p["venue"]} | {p["summary"]} |\n'
        )
    if rows:
        text = insert_once(text, header, rows, "README latest-additions table")

    text = text.replace("**Update run: 25 July 2026.**", "**Update run: 26 July 2026.**", 1)

    timeline_2024 = "    │     Wang et al.: event-enhanced passive NLOS — asynchronous diffusion-pattern changes and physics-embedded learning reconstruct moving hidden objects [IEEE Sensors Journal]\n"
    add_2024 = "    │     Zhou et al.: white-light ZPF speckle correlation — ambient-light and alignment-robust ordinary-camera reconstruction [Optics & Laser Technology]\n"
    if add_2024 not in text:
        text = insert_once(text, timeline_2024, add_2024, "README 2024 timeline")

    timeline_2025 = "2025 ── Shi et al.: fast configurable transient simulation and an open NLOS benchmark [arXiv]\n"
    add_2025 = (
        "2025 ── Fu et al. and Zhou et al.: physics-enhanced and single-shot speckle statistics move steady-state NLOS toward inexpensive white-light and ambient-light operation [Applied Optics / Optics Communications]\n"
        "    │     Hashemi et al. and Chen et al.: multispectral clutter separation and learned hyperspectral band selection strengthen passive NLOS under realistic backgrounds [IEEE TPAMI / Expert Systems with Applications]\n"
        "    │     Zhang et al.: CMFormer reduces transient-volume memory cost and reaches consumer-GPU real-time reconstruction [Optics and Lasers in Engineering]\n"
    )
    if "CMFormer reduces transient-volume memory cost" not in text:
        text = insert_once(text, timeline_2025, add_2025, "README 2025 timeline", before=True)

    write_if_changed(README, old, text)


def js_record(p: dict) -> str:
    def q(value: str) -> str:
        return value.replace("\\", "\\\\").replace('"', '\\"')
    return (
        f'      {{cat:"{q(p["cat"])}",title:"{q(p["title"])}",authors:"{q(p["authors_short"])}",'
        f'year:{p["year"]},venue:"{q(p["venue"])}",url:"https://doi.org/{p["doi"]}",key:"{q(p["summary"])}"}},\n'
    )


def update_index() -> None:
    old = read(INDEX)
    text = old
    marker = "const papers=["
    pos = text.find(marker)
    if pos < 0:
        raise SystemExit("Fail-closed: index paper-array anchor missing")
    array_end = text.find("];", pos)
    if array_end < 0:
        raise SystemExit("Fail-closed: index paper-array end missing")
    array_text = text[pos:array_end]
    records = ""
    added = 0
    for p in PAPERS:
        if p["title"].lower() in array_text.lower() or p["doi"].lower() in array_text.lower():
            continue
        records += js_record(p)
        added += 1
    if records:
        text = text[: pos + len(marker)] + "\n" + records + text[pos + len(marker) :]

    pos = text.find(marker)
    array_end = text.find("];", pos)
    prefix, arr, suffix = text[:pos], text[pos:array_end], text[array_end:]
    arr = re.sub(r"}(\s*\n\s*)\{cat:", r"},\1{cat:", arr)
    text = prefix + arr + suffix

    if added:
        pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span>)')
        match = pattern.search(text)
        if not match:
            raise SystemExit("Fail-closed: tracked-entry count anchor missing")
        text = pattern.sub(lambda m: f"{m.group(1)}{int(m.group(2)) + added}{m.group(3)}", text, count=1)

    text = text.replace("Updated 25 July 2026", "Updated 26 July 2026")
    text = text.replace("updated 25 July 2026", "updated 26 July 2026")

    if "ZPF-SCI made white-light speckle correlation robust" not in text:
        anchor = "</p></div></div>"
        year_start = text.find('<div class="tl"><div class="year">2024</div>')
        if year_start < 0:
            raise SystemExit("Fail-closed: 2024 website timeline missing")
        p_end = text.find(anchor, year_start)
        if p_end < 0:
            raise SystemExit("Fail-closed: 2024 website timeline paragraph end missing")
        sentence = " ZPF-SCI made white-light speckle correlation robust to ambient illumination and detector misalignment."
        text = text[:p_end] + sentence + text[p_end:]

    if "CMFormer made transient learning deployable" not in text:
        year_start = text.find('<div class="tl"><div class="year">2025</div>')
        if year_start < 0:
            raise SystemExit("Fail-closed: 2025 website timeline missing")
        p_end = text.find("</p></div></div>", year_start)
        if p_end < 0:
            raise SystemExit("Fail-closed: 2025 website timeline paragraph end missing")
        sentence = (" White-light physics-enhanced and single-shot speckle methods reduced steady-state acquisition constraints; "
                    "multispectral clutter separation and hyperspectral band selection strengthened passive reconstruction; "
                    "CMFormer made transient learning deployable on consumer GPUs.")
        text = text[:p_end] + sentence + text[p_end:]

    write_if_changed(INDEX, old, text)


def update_passive() -> None:
    old = read(PASSIVE)
    text = old
    conventional_anchor = (
        "Conventional cameras are the most inexpensive but have at least two limitations among all the cameras discussed in this article. "
        "First, the shadow is very sensitive to ambient light intensity, i.e., SNR decreases as the ambient light intensity increases. "
        "Second, for broadband illumination, the optical memory effect is no longer valid, due to which the problem is extremely ill-posed and usually requires additional constraints and priors.\n"
    )
    white_para = r'''

\vspace{0.8mm}
\noindent \textbf{White-light and single-shot speckle correlation.}
A complementary steady-state trajectory replaces ultrafast timing with statistical structure in wall speckle. Zhou~\etal~used Zernike-polynomial envelope fitting and low-pass correction before autocorrelation and phase retrieval, maintaining white-light reconstruction under ambient background and detector misalignment~\cite{zhouWhiteLightSpeckleNLOS2024}. Fu~\etal~then embedded the speckle-correlation model and an explicit denoising prior inside a physics-enhanced network, improving ordinary-camera scalability without coherent active illumination~\cite{fuPhysicsEnhancedWhiteLightNLOS2025}. A distinct single-shot formulation estimates object-spectrum amplitude from the covariance of one random speckle pattern, removing multi-frame stitching and extending the field of view beyond the conventional optical-memory-effect range while operating at negative SNR~\cite{zhouSingleShotSpeckleNLOS2025}. Together, these methods shift speckle-based NLOS from controlled darkroom demonstrations toward broadband, ambient-light, and reduced-measurement operation.
'''
    if "White-light and single-shot speckle correlation" not in text:
        text = insert_once(text, conventional_anchor, white_para, "passive white-light lineage")

    old_hyper = r'''Capturing richer spectral information beyond a single visible-light band can substantially improve passive NLOS imaging quality. Chen~\etal~proposed Hyper-NLOS, which uses a hyperspectral camera to capture NLOS measurements across many spectral bands and fuses them with a dedicated hyperspectral fusion network (HFN-Net)~\cite{chenHyperNLOS2024}. The additional spectral channels provide complementary cues that help discriminate hidden objects from background clutter. A band selection strategy can further select the most informative spectral bands to reduce measurement cost~\cite{chenHyperNLOS2024}. Building on this, Liu~\etal~proposed a multispectral passive NLOS approach via deep fusion photography that significantly improves long-distance reconstruction quality~\cite{laiHoloRadar2025}. These hyperspectral and multispectral approaches represent an important direction for improving passive NLOS imaging without increasing hardware complexity on the active illumination side.'''
    new_hyper = r'''Capturing richer spectral information beyond a single visible-light band can substantially improve passive NLOS imaging quality. Chen~\etal~proposed Hyper-NLOS, which uses a hyperspectral camera and a dedicated fusion network to combine complementary wavelength-dependent cues~\cite{chenHyperNLOS2024}. Hashemi~\etal~instead used spectral content to separate desired wall-mediated radiance from clutter: multispectral unmixing handles unknown uniformly colored sources, whereas a convex known-spectrum formulation requires fewer bands and remains effective when clutter is much stronger than the target signal~\cite{hashemiSpectralContentPassiveNLOS2025}. HSBS-Net then made band selection part of the reconstruction objective. Entropy-rich wavelengths are selected with differentiable constrained measurement learning, while a spectral-energy key-area Transformer suppresses poorly illuminated regions and a robust sparse loss preserves colour and structure~\cite{chenHyperspectralBandSelectionNLOS2025}. The accompanying HP-NLOS dataset covers physical full-colour targets, 256 spectral bands, multiple distances, and changing external conditions. This progression moves spectral passive NLOS from adding channels indiscriminately toward clutter-aware unmixing and task-driven acquisition.'''

    if "hashemiSpectralContentPassiveNLOS2025" not in text:
        if old_hyper not in text:
            raise SystemExit("Fail-closed: existing hyperspectral paragraph changed")
        text = text.replace(old_hyper, new_hyper, 1)

    table_anchor = r'''    \cite{katz2014non} & Incoherent light source (object side) & Conventional camera & Speckle coherence &  2D reconstruction\\%%%% Table body
'''
    table_rows = r'''    \cite{zhouWhiteLightSpeckleNLOS2024,fuPhysicsEnhancedWhiteLightNLOS2025,zhouSingleShotSpeckleNLOS2025} & White light / coherent speckle & Conventional camera & Speckle statistics with physics-enhanced or single-shot inversion & 2D reconstruction\\%%%% Table body
    \cite{hashemiSpectralContentPassiveNLOS2025,chenHyperspectralBandSelectionNLOS2025} & Ambient/incoherent light & Multispectral or hyperspectral camera & Spectral unmixing and learned band selection & Full-colour 2D reconstruction\\%%%% Table body
'''

    if "fuPhysicsEnhancedWhiteLightNLOS2025" not in text[text.find("\\begin{table*"):text.find("\\end{table*}")]:
        text = insert_once(text, table_anchor, table_rows, "passive table spectral rows")

    write_if_changed(PASSIVE, old, text)


def update_learning() -> None:
    old = read(LEARNING)
    text = old
    anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{KAN-enhanced transient Transformers with semantic guidance.}\n"
    para = r'''
\vspace{0.8mm}
\noindent \textbf{Memory-efficient MetaFormer reconstruction.}
Transient networks improve quality by modeling the joint spatial--temporal volume, but their memory cost can prevent training and deployment on commodity hardware. Zhang~\etal~introduced CMFormer, whose multidimensional global and dilated convolutions act as a purely convolutional MetaFormer token mixer~\cite{zhangCMFormerNLOS2025}. Aggregate feature transmission replaces width-expanding skip connections, cross-layer attention restores detail lost during downsampling, and gradient checkpointing further limits training memory. The reported 8-fps inference and synthetic-to-real evaluation make efficiency itself a learned-reconstruction objective, complementing NLOST-style global modeling rather than merely shrinking input resolution.

'''
    if "Memory-efficient MetaFormer reconstruction" not in text:
        text = insert_once(text, anchor, para, "CMFormer learned-method paragraph", before=True)

    hybrid_anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{Hybrid physics--data passive enhancement.}\n"
    hybrid_para = r'''
\vspace{0.8mm}
\noindent \textbf{Physics-enhanced white-light reconstruction.}
For inexpensive broadband acquisition, Fu~\etal~embedded a speckle-correlation image-formation model and denoising prior into a trainable reconstruction pipeline~\cite{fuPhysicsEnhancedWhiteLightNLOS2025}. Unlike a generic wall-image U-Net, the network exposes the autocorrelation-to-object relationship as an internal physical constraint. This provides a passive/steady-state counterpart to differentiable transient physics: the measurement modality changes, but the learned solver remains anchored to an explicit transport statistic.

'''
    if "Physics-enhanced white-light reconstruction" not in text:
        text = insert_once(text, hybrid_anchor, hybrid_para, "white-light hybrid paragraph", before=True)

    write_if_changed(LEARNING, old, text)


def update_master() -> None:
    old = read(MASTER)
    marker = "% 26 July 2026 citation trace: white-light speckle, spectral passive NLOS, and memory-efficient MetaFormer reconstruction synchronized.\n"
    text = old if marker in old else old.replace("%% bare_jrnl.tex\n", "%% bare_jrnl.tex\n" + marker, 1)
    write_if_changed(MASTER, old, text)


def update_bib() -> None:
    old = read(BIB)
    text = old.rstrip() + "\n"
    for p in PAPERS:
        key_token = "{" + p["key"] + ","
        doi_token = p["doi"].lower()
        if key_token.lower() in text.lower():
            continue
        if doi_token in text.lower():
            raise SystemExit(f"Fail-closed: DOI already exists under another key: {p['doi']}")
        match = re.search(r"@\w+\{" + re.escape(p["key"]) + r",.*?\n\}", BIB_ENTRIES, re.S)
        if not match:
            raise SystemExit(f"Internal error: BibTeX block missing for {p['key']}")
        text += "\n" + match.group(0).strip() + "\n"
    write_if_changed(BIB, old, text)


def validate() -> None:
    readme = read(README).lower()
    index = read(INDEX).lower()
    passive = read(PASSIVE)
    learning = read(LEARNING)
    bib = read(BIB).lower()
    for p in PAPERS:
        title = p["title"].lower()
        doi = p["doi"].lower()
        if readme.count(title) != 1:
            raise SystemExit(f"README title count is not one: {p['title']}")
        if index.count(title) != 1:
            raise SystemExit(f"index title count is not one: {p['title']}")
        if bib.count(doi) != 1:
            raise SystemExit(f"bibliography DOI count is not one: {p['doi']}")
        if ("{" + p["key"].lower() + ",") not in bib:
            raise SystemExit(f"bibliography key missing: {p['key']}")
    for key in (
        "zhouWhiteLightSpeckleNLOS2024",
        "fuPhysicsEnhancedWhiteLightNLOS2025",
        "zhouSingleShotSpeckleNLOS2025",
        "hashemiSpectralContentPassiveNLOS2025",
        "chenHyperspectralBandSelectionNLOS2025",
    ):
        if key not in passive:
            raise SystemExit(f"passive survey citation missing: {key}")
    for key in ("fuPhysicsEnhancedWhiteLightNLOS2025", "zhangCMFormerNLOS2025"):
        if key not in learning:
            raise SystemExit(f"learning survey citation missing: {key}")
    print("Cross-artifact validation passed.")


def main() -> None:
    update_readme()
    update_index()
    update_passive()
    update_learning()
    update_master()
    update_bib()
    validate()


if __name__ == "__main__":
    main()
