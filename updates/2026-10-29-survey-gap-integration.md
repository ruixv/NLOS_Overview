# 29 October 2026 — NLOS survey/catalog consistency audit

## Scope and citation tracing

This pass revisited the repository's core/milestone lineages: Velten et al. (2012), O'Toole et al. and the light-cone transform (2018), Lindell et al. and frequency--wavenumber migration (2019), phasor-field methods, computational periscopy and PAC-Net/NLOS-Track, Neural Transient Fields, NLOST/TransiT/ST-Mamba/DG-NLOS, acoustic NLOS, HoloRadar, consumer-LiDAR NLOS, and 3D Gaussian Transient Rendering. Forward-citation and scholarly-index searches were followed by title/abstract and final-venue checks; citations were retained only when the work made a substantive contribution to NLOS imaging, reconstruction, or tightly adjacent NLOS sensing.

The catalog and Paper Explorer already contained the principal recent candidates below, so this is a survey-body integration pass rather than duplicate catalog insertion. It also repairs a cross-artifact gap: the README and Paper Explorer listed several 2025–2026 methods that were absent from the article/5newscenes.tex citations.

## Survey additions

- **Cascaded Non-Line-of-Sight Imaging** — Royo et al., *ACM Transactions on Graphics* 45(6), Article 205 (SIGGRAPH Asia 2026), DOI [10.1145/3842503](https://doi.org/10.1145/3842503). Integrates fourth-/fifth-bounce transport and virtual secondary relay surfaces for difficult orientations and multi-corner scenes.
- **A model decomposition method for the real-time non-line-of-sight imaging** — Yang et al., *iScience* 29(6), 115828 (2026), DOI [10.1016/j.isci.2026.115828](https://doi.org/10.1016/j.isci.2026.115828). Adds non-negative LASSO model decomposition and spectral filtering for sparse transient inversion.
- **Learned light-cone transform for fast and accurate non-line-of-sight imaging** — Gao et al., *Physical Review Applied* 25, 044024 (2026), DOI [10.1103/jsbg-c7l5](https://doi.org/10.1103/jsbg-c7l5). Adds a learned high-frequency-enhanced Wiener response and end-to-end spatiotemporal reconstruction.
- **Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform** — Wei et al., *Optica* 13(9), 1785–1795 (2026), DOI [10.1364/OPTICA.604217](https://doi.org/10.1364/OPTICA.604217); **Trapezoidal Grid Reconstruction for Efficient Non-Line-of-Sight Imaging** — Sultan et al., IEEE ICCP 2026, DOI [10.1109/ICCP69532.2026.11668867](https://doi.org/10.1109/ICCP69532.2026.11668867). Both reduce computation through more suitable surface representations or depth-adaptive grids.
- **Measurement-Adaptive Light-Cone Transform for Robust Non-Line-of-Sight Imaging** — Wang et al., arXiv:2610.22847, submitted 16 October 2026. The preprint retains Fourier-domain LCT inversion while conditioning learned response weighting and regularization on the measurements; no final venue was verified as of 29 October 2026.
- **Transient video interpolation for dynamic non-line-of-sight imaging** — Sun et al., *Optics Express* 34(3), 4882–4894 (2026), DOI [10.1364/OE.580550](https://doi.org/10.1364/OE.580550); and **Fast Non-Line-of-Sight Transient Data Simulation and an Open Benchmark Dataset** — Shi et al., *Optics Express* 2025, DOI [10.1364/OE.575753](https://doi.org/10.1364/OE.575753). These extend dynamic reconstruction and reproducible comparison of transient methods.
- **MDUNet** — Raji and Murray-Bruce, WACV 2026, pp. 461–471; **Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding** — Wang et al., *Optics Express* 34(14), 26271–26289 (2026), DOI [10.1364/OE.601398](https://doi.org/10.1364/OE.601398); **Structure-guided adaptive total variation** — Zhang et al., *Optics Express* 34(3), 5210–5224 (2026); and **Neural Networks Meet Light Transport Physics for Passive Non-Line-of-Sight Imaging Enhancement** — Liang et al., IEEE Transactions on Computational Imaging 12, 282–296 (2026), DOI [10.1109/TCI.2026.3653304](https://doi.org/10.1109/TCI.2026.3653304). These broaden passive NLOS from generic enhancement toward shared geometry/radiosity decoding, diffuse-aware attention, parameter-free regularization, and physics/data fusion.
- **Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength** — Roueinfar and Salmanian, IEEE ICEE 2025, DOI [10.1109/ICEE67339.2025.11213924](https://doi.org/10.1109/ICEE67339.2025.11213924). The survey uses the final IEEE conference record rather than the later arXiv upload.
- **X-band Radar Non-Line-of-Sight Imaging** — Du et al., CVPR 2026, [CVF paper page](https://openaccess.thecvf.com/content/CVPR2026/html/Du_X-band_Radar_Non-Line-of-Sight_Imaging_CVPR_2026_paper.html). Adds a long-range radar-imaging branch complementary to optical and 77-GHz/mmWave methods.
- **A Comprehensive Study of Time-of-Flight Non-Line-of-Sight Imaging** — Marco et al., arXiv:2603.09548. The comparative ToF study is cited as arXiv because no final publication venue was verified.

## Metadata and scope decisions

- The DOI/publisher or official proceedings record is used for works with a verified final venue.
- MALCT and the comparative ToF study remain arXiv preprints because no final venue was verified in this pass.
- NIR raster scanning is retained as a practical low-cost acquisition baseline, not described as a new inverse-model breakthrough.
- X-band radar is described as long-range hidden-scene reconstruction, distinct from radar-only localization/tracking.
- Existing survey sections for thermal NLOS, consumer LiDAR, MARMOT, 3D Gaussian Transient Rendering, array-InSAR, inverse diffraction, and Doppler-aware mmWave tracking were checked and retained without duplicating their existing prose.

## Build status

The source changes are committed to a guarded branch for validation. The PDF is **not claimed updated yet**; the repository's LaTeX/BibTeX workflow must pass before the update is considered complete. The merged bibliography already contains the cited records; the build workflow will regenerate and audit the consolidated bibliography against the new citations.
