# 29 October 2026 — NLOS survey/catalog consistency audit

## Citation-tracing and cross-artifact method

The audit revisited the repository's field-defining active-NLOS lineages (Velten 2012; O'Toole/LCT 2018; Lindell/f-k migration 2019; Liu/phasor fields), passive computational periscopy, PAC-Net/NLOS-Track, Neural Transient Fields, NLOST/TransiT/ST-Mamba/DG-NLOS, acoustic NLOS, HoloRadar, consumer-LiDAR NLOS, and 3D Gaussian Transient Rendering. Forward-citation and scholarly-index searches were followed by title/abstract and publisher/proceedings verification. Candidate papers were retained only if they contributed substantive NLOS imaging, reconstruction, or tightly adjacent NLOS sensing.

The key correction from the full cross-chapter audit is that many papers absent from the new-scenes chapter were already cited in the active, passive, or data-driven chapters. They were not duplicated. The remaining true gaps were DAAM and X-band radar NLOS imaging.

## Newly integrated survey papers

- **Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding (DAAM)** — Wang et al., *Optics Express* 34(14), 26271–26289 (2026), DOI [10.1364/OE.601398](https://doi.org/10.1364/OE.601398). Added to the passive methods discussion in article/3passive.tex. DAAM explicitly models anisotropic diffuse transport and channel-wise signal-to-noise disparities, making weak hidden-scene evidence more usable in ordinary-camera passive NLOS.
- **X-band Radar Non-Line-of-Sight Imaging** — Du et al., CVPR 2026, [official CVF paper page](https://openaccess.thecvf.com/content/CVPR2026/html/Du_X-band_Radar_Non-Line-of-Sight_Imaging_CVPR_2026_paper.html). Added to the radar NLOS discussion in article/5newscenes.tex. The 10-GHz prototype combines learned dense prediction with geometry-aware reconstruction and demonstrates hidden-object reconstruction at up to 40 m; this is a long-range imaging result, distinct from radar-only localization or tracking.

## Recent candidates confirmed already integrated

The following were checked and deliberately not duplicated because they are already cited in the appropriate survey chapters:

- Active inverse models: Cascaded NLOS (ACM TOG/SIGGRAPH Asia 2026), MD-NLOS (*iScience* 2026), learned LCT (*Physical Review Applied* 2026), Quasi-Fresnel inversion (*Optica* 2026), trapezoidal-grid reconstruction (ICCP 2026), MALCT (arXiv:2610.22847; no final venue verified), directional-confocal range characterization (arXiv:2609.26846; no final venue verified), non-confocal phase compensation, NIR raster scanning (IEEE ICEE 2025), under-scanning methods, and the comprehensive ToF comparison (arXiv:2603.09548; no final venue verified).
- Learned/transient methods: TransVID (*Optics Express* 2026), time-resolved transformer (arXiv:2510.09205; no final venue verified), noise-adapted neural operator (arXiv:2508.09655; no final venue verified), TriNLOS (ECCV 2026), NLOS-MT (ICPR 2026), ST-Mamba, DG-NLOS, NLOSdiffuser (IEEE ICME 2025), physically informed neural transient fields (ICCPA 2026), D-NeSF (SPIE/ICGIP proceedings), and the open transient simulator/benchmark (*Optics Express* 2025).
- Passive and modality expansion: MDUNet (WACV 2026), structure-guided adaptive TV (*Optics Express* 2026), HPDI (IEEE TCI 2026), thermal NLOS through rough surfaces (ACM TOG 2026), consumer-LiDAR NLOS, 3D Gaussian Transient Rendering (SIGGRAPH 2026), HoloRadar (NeurIPS 2025), RIS-assisted radar demo (MobiCom 2026 Demo), array-InSAR multipath relocation (IEEE TGRS 2024), inverse-diffraction papers (arXiv 2026), and Doppler-aware mmWave tracking.

## Bibliography consistency

The consolidated bibliography already contained verified records for both newly integrated papers. The citations use the existing keys and no duplicate BibTeX entries were added. The build workflow regenerates the merged bibliography and checks the full survey citation inventory.

## Build verification

Result: successful clean LaTeX/BibTeX rebuild and PDF-text validation.

- GitHub Actions build: https://github.com/ruixv/NLOS_Overview/actions/runs/40766638214
- GitHub Pages deployment: https://github.com/ruixv/NLOS_Overview/actions/runs/40766915826
- PDF: 72 pages; 2,383,677 bytes.
- PDF blob SHA: 707e83934476cebb747aae8d53816708cb20f12b.
- The workflow reported zero missing cited keys, no undefined citations/references, and no missing/repeated BibTeX records. The generated PDF passed the required text checks.
- The PDF, consolidated bibliography, and survey source were committed to master at build commit 756a4fbfb5afa4d486774736c9790482636aaae9.

The update is complete; the recurring literature scan remains enabled.
