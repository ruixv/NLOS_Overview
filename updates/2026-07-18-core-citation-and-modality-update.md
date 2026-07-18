# 18 July 2026 core-citation and modality-expansion update

## Scope

This update follows forward citations and direct methodological descendants of the repository's milestone active, passive, learned, and modality-expansion papers. Candidate records were checked against `README.md`, `index.html`, the survey sections, update logs, and the consolidated bibliography. Papers were retained only when their main contribution is NLOS imaging/reconstruction or a tightly coupled hidden-scene acquisition method.

The latest direct NLOS paper verified in this run remains **Non-line-of-sight imaging via physics-informed cascade learning**, published by JOSA A on **15 July 2026**. No later direct NLOS imaging publication or arXiv submission was verified through 18 July 2026.

## Newly integrated records

1. **Adaptive Spiral Scanning for Confocal Non-Line-of-Sight Imaging** — Tomoya Oyama, Yang Dixin, Mariko Isogawa; IEEE Open Journal of Signal Processing 7, 482–491 (2026); DOI `10.1109/OJSP.2026.3688052`.
   - Direct continuation of C2NLOS/transient-sinogram acquisition.
   - Dynamically moves the spiral center toward strong observed relay-wall returns and uses Voronoi Density Compensation for nonuniform samples.

2. **Submillimeter non-line-of-sight ranging and imaging via cost-effective FMCW interferometry** — Huan Liang et al.; Photonics Research 14(7), 3005–3018 (2026); DOI `10.1364/PRJ.595776`.
   - Adds a coherent FMCW branch to NLOS imaging with fixed-delay fiber calibration and dynamic temporal phase subdivision.
   - Reports 450 μm ranging resolution, 1 mm axial and 2.4 mm lateral imaging resolution, and operation beyond 8 klux.

3. **Breaking the speed-resolution trade-off in 3.3-km non-line-of-sight imaging using scanning-free laser reflective tomography** — Zewei Wang et al.; Opto-Electronic Science 5, 260007 (2026); DOI `10.29026/oes.2026.260007`.
   - Removes relay-wall point scanning by treating the diffuse wall as a beam expander and reconstructing from angular tomographic measurements.
   - Demonstrates approximately 91× faster acquisition and better-than-3-cm resolution at 3.3 km in about three minutes.

4. **Non-confocal non-line-of-sight imaging using frequency-domain phase compensation with the reference function** — Jing Ping Yu et al.; Optics Express 34(2), 3232–3243 (2026); DOI `10.1364/OE.580027`.
   - Transfers a single-input/multiple-output millimeter-wave frequency-domain imaging formulation to optical NLOS.
   - Uses reference-function phase compensation and FFT reconstruction to reduce artifacts, distortion, and computation.

5. **Structure-guided adaptive total variation for parameter-free passive non-line-of-sight imaging** — Qi Zhang et al.; Optics Express 34(3), 5210–5224 (2026); DOI `10.1364/OE.587111`.
   - Direct descendant of computational periscopy and TV-regularized passive inversion.
   - Uses a preliminary estimate to derive spatially varying TV weights and removes manual regularization tuning.

6. **Non-Line-of-Sight Imaging via Sparse Bayesian Learning Deconvolution** — Yuyuan Tian et al.; Photonics 13(1), 53 (2026); DOI `10.3390/photonics13010053`.
   - Adds a plug-in probabilistic transient-restoration stage before LCT or f-k migration.
   - Suppresses background and instrument-response blur while preserving sparse multipath returns.

7. **Non-Line-of-Sight Single-Pixel Imaging Using Polarization Speckle Modulation** — Yijun Zhou et al.; Physical Review Letters 136, 143801 (2026); DOI `10.1103/kd8v-fykm`.
   - Introduces polarization as an active coding dimension for scanning-free, single-pixel keyhole NLOS imaging.
   - Uses rough-wall speckle diversity and memory-effect calibration to obtain millimeter-scale reconstruction.

8. **High-resolution Fourier single-pixel non-line-of-sight imaging employing diffusion model** — Shengjie Fu et al.; Optics and Lasers in Engineering 201, 109724 (2026); DOI `10.1016/j.optlaseng.2026.109724`.
   - Enforces measured low-frequency Fourier coefficients during diffusion sampling.
   - Restores hidden-scene high-frequency content at sampling rates down to 3% under multilayer scattering.

9. **Multiple-object passive non-line-of-sight imaging** — Pengyun Chen et al.; Frontiers of Computer Science 20(5), 2005339 (2026); DOI `10.1007/s11704-025-40887-3`.
   - Extends learned passive NLOS beyond a single dominant target.
   - Uses nested U-Net decoding, channel/spatial/self attention, and multi-branch supervision for scenes with one to three hidden objects.

## Citation-tracing rationale

- Adaptive spiral sampling is a direct acquisition descendant of Efficient NLOS Imaging from Transient Sinograms/C2NLOS.
- Sparse Bayesian deconvolution and the non-confocal phase-compensation method explicitly build on or compare against LCT, f-k migration, phasor-field, and backprojection pipelines.
- Structure-guided adaptive TV continues Saunders-style computational periscopy and model-based passive inversion.
- FMCW interferometry and reference-function phase compensation provide verified optical/RF cross-modal expansions rather than merely citing radar work in passing.
- Polarization-speckle and Fourier single-pixel systems expand NLOS coding beyond conventional relay-wall temporal raster scans.

## Excluded search results

- NLOS wireless-channel classification/localization papers were excluded because they concern communication-path state rather than hidden-scene imaging.
- Papers that mentioned transient/NLOS rendering only as a possible downstream application were excluded.
- Semantic-only NLOS classification papers without image or geometry recovery were excluded from this survey update.

## Integration and verification

The guarded synchronizers run in this order:

```text
scripts/sync_nlos_20260718_passive_geometry.py
scripts/sync_nlos_20260718_core_citation.py
```

The PR validation workflow then:

1. merges all canonical bibliography fragments into `egbib_merged_20260711.bib`;
2. clean-builds `bare_jrnl.tex` with LaTeX/BibTeX;
3. regenerates and renders `bare_jrnl.pdf`;
4. checks undefined citations, missing or duplicate BibTeX records, public-entry uniqueness, dynamic website count, final venue corrections, and PDF text;
5. commits synchronized README, website, survey sections, merged bibliography, and PDF back to the PR branch.

No source or PDF should be reported as integrated until this workflow succeeds and the resulting PR is merged.
