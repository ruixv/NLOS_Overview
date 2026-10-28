# 28 October 2026 — diffraction and RIS NLOS citation-trace update

## Newly integrated literature

This pass adds four verified works that were not present in the README, homepage, Paper Explorer source, survey prose, or active bibliography:

1. **Gang Bao, Xi Chen, Shuai Lu, and Kuangmiao Xiong, “Inverse Scattering by Diffracted Waves,” arXiv:2607.22174 (submitted 24 July 2026).** The theory proves unique recovery of the visible portion of a 2D polygonal obstacle from a single pulse and diffracted-wave measurements on a receiver curve. No final conference/journal venue was verified on 28 October 2026. This is an inverse-scattering theory paper, not an experimental relay-wall imager.
2. **Gang Bao, Xi Chen, Shuai Lu, and Kuangmiao Xiong, “Inverse Geometric Diffraction by a Cone,” arXiv:2608.04675 (submitted 5 August 2026).** Extends inverse diffraction to strictly convex 3D conical obstacles. Arrival times/directions and diffraction coefficients measured on a small receiver patch in the reflection shadow recover the tip and visible cone shape. No final venue was verified; this is a mathematical uniqueness result, not a measured imaging system.
3. **Xi Chen, Kuangmiao Xiong, and Boxi Xu, “Numerical reconstruction of polygonal obstacles by diffracted waves,” arXiv:2610.31271 (submitted 22 October 2026).** Implements the 2D theory numerically: diffracted arrival times locate vertices, while amplitudes recover corner orientation/opening angles and permit local inference of adjacent shadowed edges. The evidence is synthetic 2D wave simulation, including a small-noise test; no final venue was verified.
4. **Jing Dai, Hua Chen, and Ming Jin, “RIS-Aided Scalable Electromagnetic Fluid Vector Antenna MIMO Radar for Target Localization,” IEEE SAM 2026, pp. 1–5, DOI [10.1109/SAM68950.2026.11687919](https://doi.org/10.1109/SAM68950.2026.11687919).** The IEEE Xplore record and SAM 2026 program verify the final venue, authors, and pages. RIS-aided bistatic MIMO radar, PARAFAC, ESPRIT, and vector-cross-product processing estimate paired 2D departure/arrival angles and polarization for multiple hidden targets. The reported evidence is simulation-based target localization, not dense 3D scene reconstruction.

## Citation tracing and scope

The high-priority seed set included the field-defining optical active-NLOS papers (Velten et al. 2012, O'Toole et al. 2018 LCT, Lindell et al. 2019 f-k migration, and Liu et al. phasor-field work), passive computational periscopy, PAC-Net/NLOS-Track, Neural Transient Fields, NLOST/TransiT/ST-Mamba/DG-NLOS, acoustic NLOS, HoloRadar, consumer-LiDAR NLOS, and 3D Gaussian Transient Rendering. Publisher and scholarly-index searches were used to check final venues and distinguish genuine hidden-scene reconstruction or tightly adjacent sensing from papers that mention NLOS only as background.

The Doppler-aided mmWave position–velocity tracking preprint found in the preceding 28 October trace already cites the optical core lineage and is already represented in the README, website, survey, and merged bibliography; it was not duplicated. Cascaded NLOS, 3D-GTR, MALCT, MARMOT, GeRaF 2.0, thermal NLOS through rough surfaces, and the other recent core successors were also found to be already covered. Following the reference trail from the newly indexed numerical polygonal-obstacle paper surfaced its two theoretical predecessors, which together form a coherent new inverse-diffraction branch across 2D and 3D. The RIS-aided SAM paper was independently verified from IEEE Xplore and the SAM program and is explicitly labeled adjacent NLOS angular localization rather than imaging.

## Cross-artifact changes

- `README.md`: added all four works to Latest Additions and the Milestone Timeline with accurate venue/status labels and scope caveats.
- `index.html`: added homepage milestone notes for the 2D and 3D inverse-diffraction theory and the RIS-aided MIMO NLOS result.
- `data/papers-source.html`: added all four searchable paper-explorer records.
- `article/5newscenes.tex`: inserted a semantically placed discussion of the 2D theory, 3D cone theory, and numerical implementation in the acoustic/wave-diffraction discussion; added the RIS MIMO work in the RIS-assisted angular-sensing discussion.
- `bare_jrnl.tex`: updated its source-history comment to record the new integration.
- `egbib_merged_20260711.bib`: added four citation records, using arXiv only for the three preprints without a verifiable final venue.
- `egbib_2026_updates.bib`: staged the same records for source-set consistency.
- `.github/workflows/rebuild_nlos_citation_gap_pdf_20260718.yml`: extended the PDF citation validation loop to require all four new keys in `bare_jrnl.aux`.

## Build status

The source changes are prepared on branch `nlos-citation-trace-2026-10-28-diffraction-ris`. The PDF workflow is configured to rebuild `bare_jrnl.pdf` after the changes reach `master`. Do not treat this note or a triggered workflow as proof of a successful build; the regenerated PDF blob, page count, clean LaTeX log, and citation-key checks must be verified after merge.
