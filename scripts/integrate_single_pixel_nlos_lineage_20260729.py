from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected anchor exactly once, found {count}: {old[:120]!r}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


def require_absent(path: str, needles: list[str]) -> None:
    text = Path(path).read_text(encoding="utf-8")
    present = [needle for needle in needles if needle in text]
    if present:
        raise SystemExit(f"{path}: entries unexpectedly already present: {present}")


readme_titles = [
    "3D RGB Non-Line-of-Sight single-pixel imaging",
    "Active mode single-pixel non-line-of-sight imaging system based on second-order correlation and diffraction",
    "Multi-wavelength single-pixel non-line-of-sight imaging with a compressive sensing measurement matrix",
]
keys = [
    "musarra3DRGBSinglePixel2019",
    "liActiveModeSinglePixelNLOS2023",
    "liMultiWavelengthSinglePixelNLOS2024",
]

for path in ["README.md", "index.html"]:
    require_absent(path, readme_titles)
require_absent("egbib_merged_20260711.bib", keys)

# README: paper table.
readme_header = (
    "| Year | Paper | Venue / Status | Why it matters |\n"
    "|------|-------|----------------|----------------|\n"
)
readme_rows = (
    "| 2024 | [Multi-wavelength single-pixel non-line-of-sight imaging with a compressive sensing measurement matrix](https://doi.org/10.1007/s00340-024-08265-2) — Li et al. | Applied Physics B 130(7), 127 (2024) | Extends patterned single-pixel NLOS from monochrome spatial recovery to RGB hidden-scene imaging. Multi-wavelength measurements and TV-regularized compressive reconstruction recover colour and spatial detail at a reported 29% compression rate. |\n"
    "| 2023 | [Active mode single-pixel non-line-of-sight imaging system based on second-order correlation and diffraction](https://doi.org/10.1088/2040-8986/ac9cec) — Li et al. | Journal of Optics 25(1), 015702 (2023) | Combines patterned active illumination and second-order correlation with Fourier-domain inverse diffraction. Hadamard coding improves measured hidden-image recovery and reaches a reported SSIM of 0.9286 at full sampling. |\n"
    "| 2019 | [3D RGB Non-Line-of-Sight single-pixel imaging](https://doi.org/10.1364/ISA.2019.IM2B.5) — Musarra et al. | Imaging Systems and Applications / OSA Technical Digest 2019, IM2B.5 | Demonstrates sub-second full-colour 3D hidden-scene acquisition with a high-efficiency time-resolved single-pixel camera, establishing an early bridge between transient depth and RGB single-pixel NLOS. |\n"
)
replace_once("README.md", readme_header, readme_header + readme_rows)

# README: historical timeline.
replace_once(
    "README.md",
    "2019 ── Tsai et al.: Beyond Volumetric Albedo — direct hidden-surface and reflectance optimization [CVPR]\n",
    "2019 ── Tsai et al.: Beyond Volumetric Albedo — direct hidden-surface and reflectance optimization [CVPR]\n"
    "   │     Musarra et al.: time-resolved single-pixel capture demonstrates sub-second full-colour 3D NLOS imaging [OSA Imaging Systems and Applications]\n",
)
replace_once(
    "README.md",
    "2023 ── Wang et al.: Signal Superresolution Network — plug-and-play 16× sparse-scan acceleration [CVPR]\n",
    "2023 ── Wang et al.: Signal Superresolution Network — plug-and-play 16× sparse-scan acceleration [CVPR]\n"
    "   │     Li et al.: patterned active single-pixel correlation plus inverse diffraction improves hidden-image recovery [Journal of Optics]\n",
)
replace_once(
    "README.md",
    "2024 ── Li et al.: ST-Mamba — state-space temporal modeling and phasor-domain wave supervision for consistent dynamic NLOS video [NeurIPS]\n",
    "2024 ── Li et al.: ST-Mamba — state-space temporal modeling and phasor-domain wave supervision for consistent dynamic NLOS video [NeurIPS]\n"
    "   │     Li et al.: multi-wavelength compressive single-pixel NLOS adds RGB colour recovery at 29% sampling [Applied Physics B]\n",
)

# Website explorer and count.
index_anchor = "    const papers=[\n"
index_entries = (
    "      {cat:\"latest active steady-state single-pixel multispectral compressive-sensing color\",title:\"Multi-wavelength single-pixel non-line-of-sight imaging with a compressive sensing measurement matrix\",authors:\"Li et al.\",year:2024,venue:\"Applied Physics B 2024\",url:\"https://doi.org/10.1007/s00340-024-08265-2\",key:\"Uses multi-wavelength patterned illumination and TV-regularized compressive sensing to recover both spatial structure and RGB colour of hidden objects, reporting a 29% compression rate and improved low-sampling performance.\"},\n"
    "      {cat:\"latest active steady-state single-pixel correlation diffraction patterned-illumination\",title:\"Active mode single-pixel non-line-of-sight imaging system based on second-order correlation and diffraction\",authors:\"Li et al.\",year:2023,venue:\"Journal of Optics 2023\",url:\"https://doi.org/10.1088/2040-8986/ac9cec\",key:\"Combines second-order correlation under patterned illumination with Fourier-domain inverse diffraction; Hadamard coding improves simulated and measured hidden-image recovery and reaches a reported SSIM of 0.9286 at full sampling.\"},\n"
    "      {cat:\"latest active transient single-pixel color 3d hardware\",title:\"3D RGB Non-Line-of-Sight single-pixel imaging\",authors:\"Musarra et al.\",year:2019,venue:\"OSA Imaging Systems and Applications 2019\",url:\"https://doi.org/10.1364/ISA.2019.IM2B.5\",key:\"Demonstrates full-colour 3D imaging of a hidden scene with sub-second acquisition using a high-efficiency time-resolved single-pixel camera, linking transient depth and RGB appearance.\"},\n"
)
replace_once("index.html", index_anchor, index_anchor + index_entries)
replace_once(
    "index.html",
    '<div class="stat"><b>239</b><span>tracked latest entries</span></div>',
    '<div class="stat"><b>242</b><span>tracked latest entries</span></div>',
)
replace_once(
    "index.html",
    "while Reza et al. experimentally demonstrated P-field interference, focusing, and imaging.</p>",
    "while Reza et al. experimentally demonstrated P-field interference, focusing, and imaging. Musarra et al. additionally demonstrated sub-second, time-resolved single-pixel 3D RGB hidden-scene acquisition.</p>",
)
replace_once(
    "index.html",
    "Virtual Mirrors turned higher-order phasor transport into secondary apertures for limited-visibility and two-corner NLOS imaging.</p>",
    "Virtual Mirrors turned higher-order phasor transport into secondary apertures for limited-visibility and two-corner NLOS imaging. Patterned active single-pixel correlation followed by inverse diffraction supplied a complementary inexpensive intensity-imaging branch.</p>",
)
replace_once(
    "index.html",
    "vector-optical-field modeling converted illumination angle plus transmit/receive polarization into complementary multi-view measurements with higher echo SNR.</p>",
    "vector-optical-field modeling converted illumination angle plus transmit/receive polarization into complementary multi-view measurements with higher echo SNR. Multi-wavelength compressive single-pixel imaging further added RGB recovery under 29% sampling.</p>",
)

# Survey active-system table.
active_table_anchor = (
    "    \\cite{chenSteadystateNonLineofSightImaging2019,vedaldi_imaging_2020,roueinfarNIRRaster2025,liuPolarizationDifferentialCorrelography2025} & Continuous laser & Conventional camera & Intensity &  3D reconstruction\\\\%%%% Table body\n"
)
active_table_row = (
    "    \\cite{musarra3DRGBSinglePixel2019,liActiveModeSinglePixelNLOS2023,liMultiWavelengthSinglePixelNLOS2024} & Pulsed / patterned multi-wavelength illumination & Single-pixel detector / time-resolved single-pixel camera & ToF, correlation, and colour channels & 2D / 3D RGB reconstruction\\\\%%%% Table body\n"
)
replace_once("article/2active.tex", active_table_anchor, active_table_anchor + active_table_row)

# Survey prose in the active steady-state/single-pixel trajectory.
prose_anchor = (
    "\\vspace{0.8mm}\n"
    "\\noindent \\textbf{Polarization-speckle single-pixel imaging.}\n"
)
prose = (
    "\\vspace{0.8mm}\n"
    "\\noindent \\textbf{From time-resolved RGB to compressive multi-wavelength single-pixel NLOS.}\n"
    "Single-pixel NLOS has developed along a complementary coding trajectory to relay-wall raster scanning. Musarra~\\etal~first combined high-efficiency time-resolved single-pixel detection with spectral channels to demonstrate sub-second three-dimensional RGB imaging of a hidden scene~\\cite{musarra3DRGBSinglePixel2019}. Li~\\etal~later considered an active patterned-illumination system in which second-order correlation supplies the initial hidden estimate and a Fourier-domain inverse-diffraction stage compensates propagation blur~\\cite{liActiveModeSinglePixelNLOS2023}. Their Hadamard-coded implementation improved simulated and measured reconstruction and reported an SSIM of 0.9286 at full sampling. The subsequent multi-wavelength formulation used TV-regularized compressive sensing in RGB space to recover spatial and colour information at a reported 29\\% compression rate~\\cite{liMultiWavelengthSinglePixelNLOS2024}. Together, these studies move single-pixel NLOS from time-resolved full-colour proof of concept toward inexpensive spatial coding and undersampled multispectral recovery; the later polarization-speckle method replaces explicit spatial masks with polarization-generated random illuminations.\n\n"
)
replace_once("article/2active.tex", prose_anchor, prose + prose_anchor)

# Main source synchronization marker.
replace_once(
    "bare_jrnl.tex",
    "%% bare_jrnl.tex\n",
    "%% bare_jrnl.tex\n% 29 July 2026 citation/lab-page trace: time-resolved RGB, correlation-diffraction, and compressive multi-wavelength single-pixel NLOS lineage synchronized.\n",
)

# Canonical BibTeX records.
bib = r'''

@inproceedings{musarra3DRGBSinglePixel2019,
  author    = {Musarra, Gabriella and Lyons, Ashley and Conca, Enrico and Villa, Federica and Zappa, Franco and Altmann, Yoann and Faccio, Daniele},
  title     = {{3D RGB} Non-Line-of-Sight Single-Pixel Imaging},
  booktitle = {Imaging Systems and Applications 2019},
  series    = {OSA Technical Digest},
  pages     = {IM2B.5},
  year      = {2019},
  month     = jun,
  publisher = {Optica Publishing Group},
  doi       = {10.1364/ISA.2019.IM2B.5},
  url       = {https://doi.org/10.1364/ISA.2019.IM2B.5}
}

@article{liActiveModeSinglePixelNLOS2023,
  author    = {Li, Mengdi and Xu, Xiping and Wang, Xiaoqian and Yao, Zhihai and Wang, Xin},
  title     = {Active Mode Single-Pixel Non-Line-of-Sight Imaging System Based on Second-Order Correlation and Diffraction},
  journal   = {Journal of Optics},
  volume    = {25},
  number    = {1},
  pages     = {015702},
  year      = {2023},
  month     = jan,
  publisher = {IOP Publishing},
  doi       = {10.1088/2040-8986/ac9cec},
  url       = {https://doi.org/10.1088/2040-8986/ac9cec}
}

@article{liMultiWavelengthSinglePixelNLOS2024,
  author    = {Li, Mengdi and Guo, Zhixing and Zhang, Chao and Jiang, Xuexing and Tai, Yonghang},
  title     = {Multi-Wavelength Single-Pixel Non-Line-of-Sight Imaging with a Compressive Sensing Measurement Matrix},
  journal   = {Applied Physics B},
  volume    = {130},
  number    = {7},
  pages     = {127},
  year      = {2024},
  month     = jul,
  publisher = {Springer Nature},
  doi       = {10.1007/s00340-024-08265-2},
  url       = {https://doi.org/10.1007/s00340-024-08265-2}
}
'''
with Path("egbib_merged_20260711.bib").open("a", encoding="utf-8") as f:
    f.write(bib)

print("Integrated three verified single-pixel NLOS papers across README, website, survey, and bibliography.")
