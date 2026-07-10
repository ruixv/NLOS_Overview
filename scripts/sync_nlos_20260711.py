#!/usr/bin/env python3
"""Idempotent 11 July 2026 NLOS literature sync.

This script applies exact, anchor-checked edits to the public README/homepage,
adds semantically placed survey prose, refreshes venue metadata, creates a
supplemental BibTeX file, and points the survey at every bibliography source.
It intentionally fails rather than truncating a file when an expected anchor
is absent.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 0:
        if new in text:
            return text
        raise RuntimeError(f"Missing anchor for {label}: {old[:100]!r}")
    if count != 1:
        raise RuntimeError(f"Expected one anchor for {label}, found {count}")
    return text.replace(old, new, 1)


# ---------------------------------------------------------------------------
# README
# ---------------------------------------------------------------------------
readme = read("README.md")
readme = readme.replace("**Update run: 10 July 2026.**", "**Update run: 11 July 2026.**")

rows = """| 2026 | [CUDA-accelerated non-line-of-sight imaging with irregular relay surfaces](https://doi.org/10.1016/j.optlaseng.2025.109591) — Sun et al. | Optics and Lasers in Engineering 2026 | GPU-accelerated filtered backprojection for measurements acquired on irregular, non-planar relay surfaces, reducing the practical cost of geometry-aware active NLOS reconstruction. |
| 2025 | [TransDiff: Unsupervised Non-Line-of-Sight Imaging with Aperture-Limited Relay Surfaces](https://doi.org/10.1109/TIP.2025.3637694) — Cui et al. | IEEE TIP 2025 | Uses latent diffusion and unsupervised measurement consistency to synthesize/recover dense transient information from aperture-limited relay measurements. |
| 2025 | [Under-scanning non-line-of-sight imaging based on convolution approximation and optimization](https://doi.org/10.1063/5.0266391) — Miao et al. | APL Photonics 2025 | DO-NLOS combines a convolution approximation with optimization to reconstruct hidden scenes from strongly under-scanned transient measurements. |
| 2025 | [Physics to the Rescue: Deep Non-line-of-sight Reconstruction for High-speed Imaging](https://doi.org/10.1109/TPAMI.2022.3203383) — Mu et al. | IEEE TPAMI 2025 | Embeds wave-propagation and volume-rendering priors in a neural model for robust high-speed NLOS reconstruction from approximate real-time capture models. |
| 2025 | [Sub-pixel resolving modulation for non-line-of-sight imaging](https://doi.org/10.1364/OE.569102) — Zhang et al. | Optics Express 2025 | Introduces sub-pixel modulation to improve spatial resolving power beyond the native relay-wall sampling grid. |
| 2024 | [Virtual Scanning: Unsupervised Non-line-of-sight Imaging from Irregularly Undersampled Transients](https://proceedings.neurips.cc/paper_files/paper/2024/file/c58437945392cec01e0c75ff6cef901a-Paper-Conference.pdf) — Cui et al. | NeurIPS 2024 | Learns from irregularly undersampled transients without paired supervision, combining virtual scanning, measurement consistency, and a physics-guided SURE denoiser. |
| 2024 | [Real-time non-line-of-sight computational imaging using spectrum filtering and motion compensation](https://doi.org/10.1038/s43588-024-00722-4) — Ye et al. | Nature Computational Science 2024 | Couples spectrum-domain filtering with motion compensation/interleaved scanning to deliver room-scale real-time NLOS video. |
| 2024 | [Plug-and-play algorithms for dynamic non-line-of-sight imaging](https://doi.org/10.1145/3665139) — Ye et al. | ACM TOG 2024 | A flexible dynamic-NLOS inverse framework that combines wave-physics filtering with learned denoiser priors for temporally consistent hidden-scene video. |
| 2024 | [Domain Reduction Strategy for Non Line of Sight Imaging](https://arxiv.org/abs/2308.10269) — Shim et al. | ECCV 2024 | Periodically prunes empty hidden-space regions during inverse rendering, accelerating geometry/albedo recovery under sparse and general acquisition setups. |
"""
header = "|------|-------|----------------|----------------|\n"
if "TransDiff: Unsupervised Non-Line-of-Sight Imaging" not in readme:
    readme = replace_once(readme, header, header + rows, "README latest rows")

venue_replacements = {
    "| arXiv 2026 | Uses 3D Gaussian primitives": "| SIGGRAPH 2026 | Uses 3D Gaussian primitives",
    "| arXiv 2025 | Transient transformer for high-speed NLOS videography": "| ICCV 2025 | Transient transformer for high-speed NLOS videography",
    "| arXiv 2023 | Extends Neural Transient Fields": "| ICCV 2023 | Extends Neural Transient Fields",
    "| arXiv 2023 | Couples diffraction-based volumetric NLOS reconstruction": "| SIGGRAPH Asia 2023 | Couples diffraction-based volumetric NLOS reconstruction",
    "| arXiv 2022 | Provides a differentiable transient path-integral framework": "| ACM TOG 2021 | Provides a differentiable transient path-integral framework",
    "| arXiv 2019 | Introduces single-optical-path active NLOS imaging/tracking": "| IEEE TCI 2021 | Introduces single-optical-path active NLOS imaging/tracking",
    "| arXiv 2017 | Introduces a factored NLOS light-transport model": "| ACM TOG 2019 | Introduces a factored NLOS light-transport model",
}
for old, new in venue_replacements.items():
    readme = readme.replace(old, new)
write("README.md", readme)


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------
index = read("index.html")
index = index.replace("Updated 9 July 2026", "Updated 11 July 2026")
index = index.replace("Last updated: 9 July 2026", "Last updated: 11 July 2026")
index = index.replace('<div class="stat"><b>71</b><span>tracked latest entries</span></div>', '<div class="stat"><b>81</b><span>tracked latest entries</span></div>')

objects = """      {cat:"latest active",title:"Non-Line-of-Sight imaging using raster scanning at NIR wavelength",authors:"Roueinfar and Salmanian",year:2026,venue:"arXiv 2026",url:"https://arxiv.org/abs/2607.04183",key:"Low-cost 808 nm raster-scanning active NLOS acquisition with pan-tilt illumination and an NIR camera."},
      {cat:"latest active",title:"CUDA-accelerated non-line-of-sight imaging with irregular relay surfaces",authors:"Sun et al.",year:2026,venue:"Optics and Lasers in Engineering 2026",url:"https://doi.org/10.1016/j.optlaseng.2025.109591",key:"GPU-accelerated geometry-aware reconstruction for irregular and non-planar relay surfaces."},
      {cat:"latest learning active",title:"TransDiff: Unsupervised Non-Line-of-Sight Imaging with Aperture-Limited Relay Surfaces",authors:"Cui et al.",year:2025,venue:"IEEE TIP 2025",url:"https://doi.org/10.1109/TIP.2025.3637694",key:"Latent diffusion and unsupervised consistency recover dense transient information from aperture-limited measurements."},
      {cat:"latest active",title:"Under-scanning non-line-of-sight imaging based on convolution approximation and optimization",authors:"Miao et al.",year:2025,venue:"APL Photonics 2025",url:"https://doi.org/10.1063/5.0266391",key:"DO-NLOS combines convolution approximation and optimization for strongly under-scanned transients."},
      {cat:"latest learning active",title:"Physics to the Rescue: Deep Non-line-of-sight Reconstruction for High-speed Imaging",authors:"Mu et al.",year:2025,venue:"IEEE TPAMI 2025",url:"https://doi.org/10.1109/TPAMI.2022.3203383",key:"Wave-propagation and volume-rendering priors enable robust high-speed learned NLOS reconstruction."},
      {cat:"latest active",title:"Sub-pixel resolving modulation for non-line-of-sight imaging",authors:"Zhang et al.",year:2025,venue:"Optics Express 2025",url:"https://doi.org/10.1364/OE.569102",key:"Sub-pixel modulation improves resolving power beyond the native relay-wall sampling grid."},
      {cat:"latest learning active",title:"Virtual Scanning: Unsupervised Non-line-of-sight Imaging from Irregularly Undersampled Transients",authors:"Cui et al.",year:2024,venue:"NeurIPS 2024",url:"https://proceedings.neurips.cc/paper_files/paper/2024/file/c58437945392cec01e0c75ff6cef901a-Paper-Conference.pdf",key:"Unsupervised virtual scanning with measurement consistency and physics-guided SURE denoising."},
      {cat:"latest active",title:"Real-time non-line-of-sight computational imaging using spectrum filtering and motion compensation",authors:"Ye et al.",year:2024,venue:"Nature Computational Science 2024",url:"https://doi.org/10.1038/s43588-024-00722-4",key:"Spectrum filtering and motion compensation enable room-scale real-time NLOS video."},
      {cat:"latest learning active",title:"Plug-and-play algorithms for dynamic non-line-of-sight imaging",authors:"Ye et al.",year:2024,venue:"ACM TOG 2024",url:"https://doi.org/10.1145/3665139",key:"Wave-physics filtering plus learned denoiser priors for temporally consistent dynamic NLOS."},
      {cat:"latest active",title:"Domain Reduction Strategy for Non Line of Sight Imaging",authors:"Shim et al.",year:2024,venue:"ECCV 2024",url:"https://arxiv.org/abs/2308.10269",key:"Coarse-to-fine pruning of empty hidden-space regions accelerates general inverse rendering."},
"""
array_anchor = "    const papers=[\n"
if "TransDiff: Unsupervised Non-Line-of-Sight Imaging" not in index:
    index = replace_once(index, array_anchor, array_anchor + objects, "homepage paper objects")

index = index.replace('title:"Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering",authors:"Yi Wang et al.",year:2026,venue:"arXiv 2026"', 'title:"Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering",authors:"Yi Wang et al.",year:2026,venue:"SIGGRAPH 2026"')
index = index.replace('title:"TransiT: Transient Transformer for Non-line-of-sight Videography",authors:"Ruiqian Li et al.",year:2025,venue:"arXiv 2025"', 'title:"TransiT: Transient Transformer for Non-line-of-sight Videography",authors:"Ruiqian Li et al.",year:2025,venue:"ICCV 2025"')
index = index.replace('title:"NLOS-NeuS: Non-line-of-sight Neural Implicit Surface",authors:"Fujimura et al.",year:2023,venue:"arXiv 2023"', 'title:"NLOS-NeuS: Non-line-of-sight Neural Implicit Surface",authors:"Fujimura et al.",year:2023,venue:"ICCV 2023"')
index = index.replace('title:"Self-Calibrating, Fully Differentiable NLOS Inverse Rendering",authors:"Choi et al.",year:2023,venue:"arXiv 2023"', 'title:"Self-Calibrating, Fully Differentiable NLOS Inverse Rendering",authors:"Choi et al.",year:2023,venue:"SIGGRAPH Asia 2023"')
index = index.replace('title:"Differentiable Transient Rendering",authors:"Yi et al.",year:2022,venue:"arXiv 2022"', 'title:"Differentiable Transient Rendering",authors:"Yi et al.",year:2021,venue:"ACM TOG 2021"')
index = index.replace('title:"Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path",authors:"Metzler et al.",year:2019,venue:"arXiv 2019"', 'title:"Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path",authors:"Metzler et al.",year:2021,venue:"IEEE TCI 2021"')
index = index.replace('title:"Non-line-of-sight Imaging with Partial Occluders and Surface Normals",authors:"Heide et al.",year:2017,venue:"arXiv 2017"', 'title:"Non-line-of-sight Imaging with Partial Occluders and Surface Normals",authors:"Heide et al.",year:2019,venue:"ACM TOG 2019"')

index = index.replace("Dynamic room-sized NLOS video, Mamba-style temporal modeling, phasor-field enhancement, passive limited-prior adaptation, ptychographic depth-resolved NLOS, single-photon-LiDAR navigation, mobile-robot passive tracking, SSD, and passive metasurface-assisted radar NLOS became central.", "Dynamic room-sized NLOS video, spectrum filtering with motion compensation, plug-and-play reconstruction, Virtual Scanning, domain reduction, Mamba-style temporal modeling, phasor-field enhancement, ptychographic depth-resolved NLOS, single-photon-LiDAR navigation, mobile-robot tracking, and passive metasurface-assisted radar NLOS became central.")
index = index.replace("TransiT, DG-NLOS, HoloRadar, NANO, MARMOT, TRT, Quasi-Fresnel transforms, MITO, N2LoS, mmMirror, See and Beam, SuperEx, mitransient, and relay-free acoustic NLOS broadened the toolbox.", "TransDiff, DO-NLOS, physics-guided high-speed reconstruction, sub-pixel modulation, TransiT, DG-NLOS, HoloRadar, NANO, MARMOT, TRT, Quasi-Fresnel transforms, MITO, N2LoS, mmMirror, and relay-free acoustic NLOS broadened the toolbox.")
index = index.replace("The frontier moves toward real-world geometry: non-planar limited relays, smartphone-grade LiDAR motion sampling, RF/radar neural reconstruction, low-cost LiDAR datasets, quantized RIS, backscatter positioning, double-bounce radio SLAM, and NLOS-aided off-grid MIMO/ISAC imaging.", "The frontier moves toward real-world geometry: arbitrary and irregular relay surfaces with CUDA acceleration and Gaussian transient rendering, low-cost NIR raster scanning, smartphone-grade LiDAR motion sampling, RF/radar neural reconstruction, quantized RIS, backscatter positioning, double-bounce radio SLAM, and NLOS-aided off-grid MIMO/ISAC imaging.")
write("index.html", index)


# ---------------------------------------------------------------------------
# Survey prose
# ---------------------------------------------------------------------------
data = read("article/4datadriven.tex")
if "cuiTransDiffTIP2025" not in data:
    anchor = "This method achieves higher fidelity and orders-of-magnitude faster inference than existing iterative solutions.\n"
    addition = anchor + "\n\\vspace{0.8mm}\n\\noindent \\textbf{Aperture-limited diffusion and physics-guided high-speed reconstruction.}\nTransDiff~\\cite{cuiTransDiffTIP2025} extends unsupervised transient completion to aperture-limited relay surfaces using a latent diffusion prior constrained by the measured transients. In parallel, Physics to the Rescue~\\cite{muPhysicsRescueTPAMI2025} embeds wave-propagation and volume-rendering priors into a neural reconstruction pipeline, improving robustness when high-speed acquisition requires approximate light-transport models. Together, these methods mark a shift from purely data-driven inversion toward learned solvers whose latent completion is explicitly checked against transient physics.\n"
    data = replace_once(data, anchor, addition, "data-driven survey paragraph")
write("article/4datadriven.tex", data)

active = read("article/2active.tex")
if "miaoUnderScanning2025" not in active:
    marker = "\\subsection{Challenges and Prospects}"
    paragraph = """\\vspace{0.8mm}
\\noindent \\textbf{Irregular, aperture-limited, and under-scanned relay measurements.}
Recent work increasingly relaxes the dense planar-wall assumption. DO-NLOS~\\cite{miaoUnderScanning2025} combines convolution approximation and optimization for strongly under-scanned measurements; sub-pixel resolving modulation~\\cite{zhangSubpixelModulation2025} extracts spatial detail beyond the native relay sampling grid; and CUDA-accelerated reconstruction on irregular relay surfaces~\\cite{sunCUDAIrregular2026} makes geometry-aware filtered backprojection practical on modern GPUs. These developments complement self-supervised Virtual Scanning and diffusion-based transient completion by improving the physical solver and acquisition model rather than relying only on learned interpolation.

"""
    if marker not in active:
        raise RuntimeError("Could not locate Active Methods challenges section")
    active = active.replace(marker, paragraph + marker, 1)
write("article/2active.tex", active)


# ---------------------------------------------------------------------------
# BibTeX additions and final-venue corrections
# ---------------------------------------------------------------------------
bib = r"""% Verified citation-tracing additions integrated on 11 July 2026.

@article{cuiTransDiffTIP2025,
  title   = {TransDiff: Unsupervised Non-Line-of-Sight Imaging with Aperture-Limited Relay Surfaces},
  author  = {Cui, Xingyu and Yue, Huanjing and Sun, Shida and Li, Yichao and Hou, Yusen and Xiong, Zhiwei and Yang, Jingyu},
  journal = {IEEE Transactions on Image Processing},
  volume  = {34},
  pages   = {8018--8031},
  year    = {2025},
  doi     = {10.1109/TIP.2025.3637694},
  url     = {https://doi.org/10.1109/TIP.2025.3637694}
}

@article{miaoUnderScanning2025,
  title   = {Under-scanning non-line-of-sight imaging based on convolution approximation and optimization},
  author  = {Miao, J. and Shi, Y. and Liu, L. and Wei, Y. and Cai, F. and Bai, L. and Guo, E. and Han, J.},
  journal = {APL Photonics},
  volume  = {10},
  number  = {6},
  pages   = {066110},
  year    = {2025},
  doi     = {10.1063/5.0266391},
  url     = {https://doi.org/10.1063/5.0266391}
}

@article{muPhysicsRescueTPAMI2025,
  title   = {Physics to the Rescue: Deep Non-line-of-sight Reconstruction for High-speed Imaging},
  author  = {Mu, Fangzhou and Mo, Sicheng and Peng, Jiayong and Liu, Xiaochun and Nam, Ji Hyun and Raghavan, Siddeshwar and Velten, Andreas and Li, Yin},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  volume  = {47},
  number  = {8},
  pages   = {6146--6158},
  year    = {2025},
  doi     = {10.1109/TPAMI.2022.3203383},
  eprint  = {2205.01679},
  archivePrefix = {arXiv},
  url     = {https://doi.org/10.1109/TPAMI.2022.3203383}
}

@article{sunCUDAIrregular2026,
  title   = {{CUDA}-accelerated non-line-of-sight imaging with irregular relay surfaces},
  author  = {Sun, Y. and Hong, Y. and Qiu, Z. and Li, W. and Li, W. and Sun, Q. and Xu, F.},
  journal = {Optics and Lasers in Engineering},
  volume  = {200},
  pages   = {109591},
  year    = {2026},
  doi     = {10.1016/j.optlaseng.2025.109591},
  url     = {https://doi.org/10.1016/j.optlaseng.2025.109591}
}

@article{zhangSubpixelModulation2025,
  title   = {Sub-pixel resolving modulation for non-line-of-sight imaging},
  author  = {Zhang, W. and Zhu, S. and Chen, L. and Liu, L. and Bai, L. and Lam, E. Y. and Guo, E. and Han, J.},
  journal = {Optics Express},
  volume  = {33},
  number  = {14},
  pages   = {30783--30798},
  year    = {2025},
  doi     = {10.1364/OE.569102},
  url     = {https://doi.org/10.1364/OE.569102}
}
"""
write("egbib_20260711_updates.bib", bib)

# Correct final venues in whichever supplement currently owns the entry.
def replace_bib_entry(title_fragment: str, replacement_factory) -> None:
    for path in sorted(ROOT.glob("egbib*.bib")):
        if path.name == "egbib_20260711_updates.bib":
            continue
        text = path.read_text(encoding="utf-8")
        pos = text.lower().find(title_fragment.lower())
        if pos < 0:
            continue
        start = text.rfind("@", 0, pos)
        if start < 0:
            continue
        brace = text.find("{", start)
        comma = text.find(",", brace)
        key = text[brace + 1:comma].strip()
        depth = 0
        end = None
        for i in range(brace, len(text)):
            if text[i] == "{": depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is None:
            raise RuntimeError(f"Malformed BibTeX entry containing {title_fragment}")
        replacement = replacement_factory(key)
        path.write_text(text[:start] + replacement + text[end:], encoding="utf-8")
        return

replace_bib_entry("TransiT: Transient Transformer", lambda k: f"""@inproceedings{{{k},
  title     = {{TransiT: Transient Transformer for Non-line-of-sight Videography}},
  author    = {{Li, Ruiqian and Shen, Siyuan and Xia, Suan and Wang, Ziheng and Peng, Xingyue and Song, Chengxuan and Zhu, Yingsheng and Wu, Tao and Li, Shiying and Yu, Jingyi}},
  booktitle = {{Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)}},
  pages     = {{27542--27551}},
  year      = {{2025}},
  eprint    = {{2503.11328}},
  archivePrefix = {{arXiv}},
  url       = {{https://arxiv.org/abs/2503.11328}}
}}""")

replace_bib_entry("Non-line-of-sight Neural Implicit Surface", lambda k: f"""@inproceedings{{{k},
  title     = {{NLOS-NeuS: Non-line-of-sight Neural Implicit Surface}},
  author    = {{Fujimura, Yuki and Kushida, Takuma and Funatomi, Takuya and Mukaigawa, Yasuhiro}},
  booktitle = {{Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)}},
  pages     = {{10532--10541}},
  year      = {{2023}},
  eprint    = {{2303.12280}},
  archivePrefix = {{arXiv}},
  url       = {{https://arxiv.org/abs/2303.12280}}
}}""")

# Include every supplemental bibliography in the survey build.
tex = read("bare_jrnl.tex")
bib_names = [p.stem for p in sorted(ROOT.glob("egbib*.bib"))]
tex = re.sub(r"\\bibliography\{[^}]+\}", "\\bibliography{" + ",".join(bib_names) + "}", tex, count=1)
write("bare_jrnl.tex", tex)


# ---------------------------------------------------------------------------
# Update note and consistency checks
# ---------------------------------------------------------------------------
note = """# 11 July 2026 citation-tracing and sparse/irregular NLOS sync

This update was driven by forward-citation tracing from the field-defining LCT, f-k migration, phasor-field, neural-transient-field, transformer, and 3D Gaussian transient-rendering lineages. Each added item is directly about NLOS imaging/reconstruction rather than a paper that merely cites NLOS work in passing.

## Public artifacts

- `README.md`: nine missing published papers added; final venue corrections applied where independently verifiable.
- `index.html`: the same papers plus the previously README-only NIR raster-scanning paper added; latest count changed from 71 to 81 and timeline summaries updated.
- `article/4datadriven.tex`: added TransDiff and physics-guided high-speed reconstruction in the physics/learning section.
- `article/2active.tex`: added a sparse/irregular-relay paragraph covering DO-NLOS, sub-pixel modulation, and CUDA acceleration.
- `egbib_20260711_updates.bib`: five new final-venue BibTeX records with DOI metadata.
- `bare_jrnl.tex`: bibliography command expanded to all `egbib*.bib` sources.

## Venue corrections

The public surfaces were corrected from arXiv-only labels to verified final venues for 3D Gaussian Transient Rendering (SIGGRAPH 2026), TransiT (ICCV 2025), NLOS-NeuS (ICCV 2023), Self-Calibrating Fully Differentiable NLOS Inverse Rendering (SIGGRAPH Asia 2023), Differentiable Transient Rendering (ACM TOG 2021), Keyhole Imaging (IEEE TCI 2021), and Partial Occluders and Surface Normals (ACM TOG 2019).

## PDF status

The accompanying GitHub Actions run attempts a clean LaTeX/BibTeX rebuild. The workflow appends the final success/failure status below before committing. If compilation fails, source changes are still committed and the old PDF is deliberately left untouched.
"""
write("updates/2026-07-11-citation-tracing-sparse-irregular-sync.md", note)

required_readme = [
    "TransDiff: Unsupervised Non-Line-of-Sight Imaging",
    "Virtual Scanning: Unsupervised Non-line-of-sight Imaging",
    "CUDA-accelerated non-line-of-sight imaging",
]
required_tex = ["cuiTransDiffTIP2025", "miaoUnderScanning2025", "sunCUDAIrregular2026"]
for token in required_readme:
    if token not in readme or token not in index:
        raise RuntimeError(f"Public-surface consistency check failed: {token}")
for token in required_tex:
    if token not in (data + active + bib):
        raise RuntimeError(f"Survey/BibTeX consistency check failed: {token}")

print("NLOS literature sync completed and consistency anchors verified.")
