from pathlib import Path
import re


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one anchor in {path}, found {count}: {old[:100]!r}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


def insert_before(path: str, anchor: str, block: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if block.strip() in text:
        raise RuntimeError(f"Block already present in {path}")
    count = text.count(anchor)
    if count != 1:
        raise RuntimeError(f"Expected exactly one anchor in {path}, found {count}")
    p.write_text(text.replace(anchor, block + anchor, 1), encoding="utf-8")


def append_bib(entries: str) -> None:
    p = Path("egbib_merged_20260711.bib")
    text = p.read_text(encoding="utf-8")
    for key in (
        "wuUntrainedDeepDecoderNLOS2022",
        "zhuCompressiveNLOSDeepLearning2023",
        "wangIRFDeconvolutionNLOS2024",
    ):
        if re.search(rf"^@(article|inproceedings)\{{{re.escape(key)},", text, re.M):
            raise RuntimeError(f"Bibliography key already present: {key}")
    p.write_text(text.rstrip() + "\n\n" + entries.strip() + "\n", encoding="utf-8")


# README: new verified rows, concrete update date, and historical placement.
replace_once(
    "README.md",
    "**Update run: 29 July 2026.**",
    "**Update run: 30 July 2026.**",
)
readme_anchor = "| Year | Paper | Venue / Status | Why it matters |\n|------|-------|----------------|----------------|\n"
readme_rows = (
    "| 2024 | [Enhancing the spatial resolution of time-of-flight based non-line-of-sight imaging via instrument response function deconvolution](https://doi.org/10.1364/OE.518767) — Wang et al. | Optics Express 32(7), 12303–12317 (2024) | Models measured transients as a Poisson convolution with the calibrated instrument response and deconvolves timing blur before LCT or f-k migration. Simulations and experiments show that reconstruction remains viable with total timing jitter up to 1200 ps, linking detector calibration directly to recoverable spatial resolution. |\n"
    "| 2023 | [Compressive Non-Line-of-Sight Imaging with Deep Learning](https://doi.org/10.1103/PhysRevApplied.19.034090) — Zhu et al. | Physical Review Applied 19(3), 034090 (2023) | Reconstructs 32×32 hidden images from only 8×8 transient scan points using a CNN trained entirely on simulation and transferred to measured data. The 6.25% spatial sampling regime is an early direct precursor to later learned under-scanning and transient-completion methods. |\n"
    "| 2022 | [Non-line-of-sight imaging based on an untrained deep decoder network](https://doi.org/10.1364/OL.471319) — Wu et al. | Optics Letters 47(19), 5056–5059 (2022) | Couples an untrained deep decoder with the passive occluder-aided forward model, optimizing network weights per measurement without paired training data. It improves hidden-image detail and robustness under strong ambient light, bridging computational periscopy and zero-shot physics-guided neural priors. |\n"
)
replace_once("README.md", readme_anchor, readme_anchor + readme_rows)
replace_once(
    "README.md",
    "2022 ── Grau et al.: Occlusion Fields — implicit recoverability and self-occlusion-aware hidden meshes [arXiv]\n",
    "2022 ── Grau et al.: Occlusion Fields — implicit recoverability and self-occlusion-aware hidden meshes [arXiv]\n"
    "   │     Wu et al.: an untrained deep decoder is optimized through the passive occluder-aided forward model, avoiding paired training data under strong ambient light [Optics Letters]\n",
)
replace_once(
    "README.md",
    "2023 ── Wang et al.: Signal Superresolution Network — plug-and-play 16× sparse-scan acceleration [CVPR]\n",
    "2023 ── Wang et al.: Signal Superresolution Network — plug-and-play 16× sparse-scan acceleration [CVPR]\n"
    "   │     Zhu et al.: simulation-trained compressive learning reconstructs 32×32 hidden images from 8×8 transient scans [Physical Review Applied]\n",
)
replace_once(
    "README.md",
    "2024 ── Li et al.: ST-Mamba — state-space temporal modeling and phasor-domain wave supervision for consistent dynamic NLOS video [NeurIPS]\n",
    "2024 ── Li et al.: ST-Mamba — state-space temporal modeling and phasor-domain wave supervision for consistent dynamic NLOS video [NeurIPS]\n"
    "   │     Wang et al.: instrument-response deconvolution removes TCSPC timing blur before LCT or f-k reconstruction, converting hardware jitter into an explicit inverse problem [Optics Express]\n",
)

# Website explorer and timeline.
replace_once("index.html", "Updated 29 July 2026 · 210+ papers", "Updated 30 July 2026 · 210+ papers")
replace_once("index.html", "Last updated: 29 July 2026", "Last updated: 30 July 2026")
index_anchor = "    const papers=[\n"
index_rows = (
    "      {cat:\"latest active transient tof spad calibration deconvolution lct fk resolution\",title:\"Enhancing the spatial resolution of time-of-flight based non-line-of-sight imaging via instrument response function deconvolution\",authors:\"Wang et al.\",year:2024,venue:\"Optics Express 2024\",url:\"https://doi.org/10.1364/OE.518767\",key:\"Treats TCSPC timing blur as a Poisson convolution with the measured instrument response and deconvolves it before LCT or f-k migration, retaining useful reconstruction with total timing jitter up to 1200 ps.\"},\n"
    "      {cat:\"latest learning active transient compressive underscanning cnn simulation-to-real\",title:\"Compressive Non-Line-of-Sight Imaging with Deep Learning\",authors:\"Zhu et al.\",year:2023,venue:\"Physical Review Applied 2023\",url:\"https://doi.org/10.1103/PhysRevApplied.19.034090\",key:\"Uses a simulation-trained CNN to reconstruct 32×32 hidden images from 8×8 measured transient scans, an early 6.25%-sampling bridge toward learned under-scanning and scan-free NLOS.\"},\n"
    "      {cat:\"latest passive occluder computational-periscopy zero-shot untrained-network physics-guided\",title:\"Non-line-of-sight imaging based on an untrained deep decoder network\",authors:\"Wu et al.\",year:2022,venue:\"Optics Letters 2022\",url:\"https://doi.org/10.1364/OL.471319\",key:\"Optimizes an untrained deep decoder through the passive occluder-aided forward model for each wall photograph, avoiding paired data while improving detail and robustness under strong ambient light.\"},\n"
)
replace_once("index.html", index_anchor, index_anchor + index_rows)

p = Path("index.html")
html = p.read_text(encoding="utf-8")n

def augment_year(year: int, sentence: str) -> None:
    global html
    pattern = re.compile(
        rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
        re.S,
    )
    match = pattern.search(html)
    if not match:
        raise RuntimeError(f"Timeline year not found: {year}")
    if sentence in match.group(2):
        raise RuntimeError(f"Timeline sentence already present for {year}")
    replacement = match.group(1) + match.group(2).rstrip() + " " + sentence + match.group(3)
    html = html[: match.start()] + replacement + html[match.end() :]


augment_year(2022, "Wu et al. also coupled an untrained deep decoder to the passive occluder-aided transport model, establishing a measurement-specific neural prior that requires no paired training set.")
augment_year(2023, "Zhu et al. demonstrated simulation-to-real compressive learning from only 8×8 transient scan points, anticipating later learned measurement completion and under-scanning pipelines.")
augment_year(2024, "Wang et al. explicitly inverted the measured TCSPC instrument response before LCT or f-k migration, showing that detector timing jitter can be computationally traded for spatial resolution.")
actual = html.count('{cat:')
html, n = re.subn(r'(<div class="stat"><b>)\d+(</b><span>tracked latest entries</span>)', rf'\g<1>{actual}\2', html, count=1)
if n != 1:
    raise RuntimeError("Could not update website tracked-entry count")
p.write_text(html, encoding="utf-8")

# Active survey: detector-response inversion and compressive transient learning.
replace_once(
    "article/2active.tex",
    "spaettSPADTimingNLOS2026,yangPoissonLowSamplingNLOS2026,wangSemanticUndersamplingNLOS2026}",
    "spaettSPADTimingNLOS2026,yangPoissonLowSamplingNLOS2026,wangSemanticUndersamplingNLOS2026,zhuCompressiveNLOSDeepLearning2023,wangIRFDeconvolutionNLOS2024}",
)
active_anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{From few-channel inference to time-multiplexed imaging.}\n"
active_block = (
    "\\vspace{0.8mm}\n"
    "\\noindent \\textbf{Detector-response inversion and compressive transient sampling.}\n"
    "Two complementary studies made the acquisition bottleneck itself part of the reconstruction pipeline. Zhu~\\etal~trained a convolutional network entirely on simulated transients and reconstructed $32\\times32$ hidden images from only $8\\times8$ scan points on measured data, corresponding to 6.25\\% of the dense spatial samples~\\cite{zhuCompressiveNLOSDeepLearning2023}. This result is an early precursor to later transient-completion and under-scanning networks, although its output is two-dimensional and its learned prior remains category-dependent. Wang~\\etal~instead addressed the temporal response of the hardware: they modeled the measured histogram as a Poisson convolution with the calibrated instrument response function and applied iterative deconvolution before LCT or $f$--$k$ migration~\\cite{wangIRFDeconvolutionNLOS2024}. Simulations and experiments showed successful recovery even when total timing jitter reached 1200~ps, a regime previously associated with roughly 200~ps timing. Together, these works clarify that faster NLOS need not rely only on a new back end: spatial scan density and detector timing blur can be reduced or inverted upstream while retaining established physical solvers.\n\n"
)
insert_before("article/2active.tex", active_anchor, active_block)

# Passive survey: zero-shot physics-guided neural prior.
passive_anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{From separable soft-shadow inversion to diffusion.}\n"
passive_block = (
    "\\vspace{0.8mm}\n"
    "\\noindent \\textbf{Untrained neural priors for occluder-aided passive NLOS.}\n"
    "Wu~\\etal~combined the calibrated occluder-aided forward model with an untrained deep decoder whose weights are optimized separately for each observed wall image~\\cite{wuUntrainedDeepDecoderNLOS2022}. The network therefore acts as an implicit image prior rather than a supervised mapping and requires neither paired hidden scenes nor a pre-collected training corpus. Simulated and measured results under strong ambient illumination improve detail and robustness over conventional inversion. This work supplies an early zero-shot bridge between ordinary-camera computational periscopy and later physics-guided passive networks: the light-transport operator enforces measurement consistency, while network architecture regularizes the hidden image.\n\n"
)
insert_before("article/3passive.tex", passive_anchor, passive_block)

# Data-driven survey: place compressive learning in the end-to-end trajectory.
data_anchor = "In addition to reconstruction tasks, recognition is also an important goal in NLOS scenes."
data_block = (
    "\\vspace{0.8mm}\n"
    "\\noindent \\textbf{Compressive simulation-to-real transient learning.}\n"
    "Zhu~\\etal~directly targeted acquisition reduction with a convolutional network that maps sparse photon time-of-flight histograms to hidden two-dimensional images~\\cite{zhuCompressiveNLOSDeepLearning2023}. Training uses only simulated data, whereas evaluation includes physical captures; $8\\times8$ relay samples reconstruct a $32\\times32$ output. Relative to earlier dense end-to-end mappings, this study makes scan compression the central learning objective and foreshadows later signal-superresolution, under-scanning, virtual-scanning, and masked-transient-pretraining methods.\n\n"
)
insert_before("article/4datadriven.tex", data_anchor, data_block)

# Top-level synchronization note.
replace_once(
    "bare_jrnl.tex",
    "%% bare_jrnl.tex\n",
    "%% bare_jrnl.tex\n% 30 July 2026 core-citation trace: passive untrained decoding, compressive transient learning, and instrument-response deconvolution synchronized.\n",
)

append_bib(r"""
@article{wuUntrainedDeepDecoderNLOS2022,
  author    = {Wu, Huazheng and Liu, Shoupei and Meng, Xiangfeng and Yang, Xiulun and Yin, Yongkai},
  title     = {Non-line-of-sight imaging based on an untrained deep decoder network},
  journal   = {Optics Letters},
  volume    = {47},
  number    = {19},
  pages     = {5056--5059},
  year      = {2022},
  publisher = {Optica Publishing Group},
  doi       = {10.1364/OL.471319},
  url       = {https://doi.org/10.1364/OL.471319}
}

@article{zhuCompressiveNLOSDeepLearning2023,
  author    = {Zhu, Shenyu and Sua, Yong Meng and Bu, Ting and Huang, Yu-Ping},
  title     = {Compressive Non-Line-of-Sight Imaging with Deep Learning},
  journal   = {Physical Review Applied},
  volume    = {19},
  number    = {3},
  pages     = {034090},
  year      = {2023},
  publisher = {American Physical Society},
  doi       = {10.1103/PhysRevApplied.19.034090},
  url       = {https://doi.org/10.1103/PhysRevApplied.19.034090}
}

@article{wangIRFDeconvolutionNLOS2024,
  author    = {Wang, Dingjie and Hao, Wei and Tian, Yuyuan and Xu, Weihao and Tian, Yuan and Cheng, Haihao and Chen, Songmao and Zhang, Ning and Zhu, Wenhua and Su, Xiuqin},
  title     = {Enhancing the spatial resolution of time-of-flight based non-line-of-sight imaging via instrument response function deconvolution},
  journal   = {Optics Express},
  volume    = {32},
  number    = {7},
  pages     = {12303--12317},
  year      = {2024},
  publisher = {Optica Publishing Group},
  doi       = {10.1364/OE.518767},
  url       = {https://doi.org/10.1364/OE.518767}
}
""")

print("Synchronized three citation-traced NLOS papers across README, website, survey prose, and bibliography.")
