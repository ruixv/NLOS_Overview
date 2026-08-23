# 23 August 2026 — passive plenoptic / THz / beyond-OME gap

**Integrated on 23 August 2026.** README, canonical V2 corpus/timeline, passive-survey prose, final-venue BibTeX, and the rebuilt survey PDF were synchronized by the guarded workflow.

This run combined fresh 2026 keyword/publisher searches with forward-citation and scholarly-index checks around the repository's core active/passive NLOS milestones. Recent active-transient results found through the LCT / f-k / phasor-field citation pass (including consumer-LiDAR, TLTM iteration, arbitrary-relay transient rendering, long-range SPAD systems, and recent learned transient reconstruction) were already represented in the repository and were not duplicated.

The repository audit found a coherent missing passive light-field lineage and one missing 2026 around-corner speckle paper. All records below were verified against final publisher or scholarly-index metadata before staging:

1. **Sasaki & Leger, “Light field reconstruction from scattered light using plenoptic data,” JOSA A 37(4), 653–670 (2020), DOI 10.1364/JOSAA.378714.** A direct precursor to passive NLOS plenoptic sensing: formulates hidden-scene recovery after wall scattering with a BRDF-aware Fredholm light-field model and analyzes regularization and recoverable-information limits.
2. **Sasaki & Leger, “Non-line-of-sight object location estimation from scattered light using plenoptic data,” JOSA A 38(2), 211–228 (2021), DOI 10.1364/JOSAA.394846.** Derives depth/transverse resolution limits and a projection-slice / mixed-space-frequency localization method.
3. **Sasaki, Hashemi & Leger, “Passive 3D location estimation of non-line-of-sight objects from a scattered thermal infrared light field,” Optics Express 29(26), 43642–43661 (2021), DOI 10.1364/OE.445181.** Builds a scanned LWIR light-field cube and localizes human-temperature hidden targets in a life-size diffusive hallway.
4. **Grossman, Sasaki & Leger, “Passive Terahertz Non-Line-of-Sight Imaging,” IEEE T-THz 12(5), 489–498 (2022), DOI 10.1109/TTHZ.2022.3173168.** Demonstrates passive 336-GHz hidden-human imaging from rough-wall reflections with uncooled direct-detection hardware.
5. **Sasaki, Grossman & Leger, “Estimation of the 3D spatial location of non-line-of-sight objects using passive THz plenoptic measurements,” Optics Express 30(23), 41911–41921 (2022), DOI 10.1364/OE.472069.** Uses spatial-angular THz measurements and refocusing for 3D localization with a room-temperature sensor.
6. **Sasaki, Grossman & Leger, “Combined geometric and physical optics analysis of passive non-line-of-sight light-field measurement,” Optics Express 33(19), 39194–39217 (2025), DOI 10.1364/OE.568818.** Unifies BRDF/geometric-optics and Wigner/physical-optics regimes to predict passive NLOS information loss and optimal focusing across LWIR and THz wavelengths.
7. **Wei et al., “Single-shot imaging through scattering media and around the corner beyond the OME range via polarization-encoded spatial multiplexing,” Optics and Lasers in Engineering 200, 109602 (2026), DOI 10.1016/j.optlaseng.2026.109602.** Uses polarization-encoded speckle multiplexing and robust demultiplexing for single-shot multi-target around-corner imaging beyond the conventional optical-memory-effect range.

## Intended survey trajectory

The semantically useful trajectory is:

**wall-scattered plenoptic inverse formulation → NLOS depth/transverse localization → passive LWIR 3D localization → passive THz hidden-human imaging → passive THz plenoptic 3D localization → unified roughness/wavelength/diffraction design analysis**, alongside the speckle branch **memory-effect reconstruction → component separation beyond the OME → single-shot polarization-encoded beyond-OME multiplexing**.

## Guarded integration

`python3 scripts/integrate_plenoptic_thz_ome_20260823.py` is intentionally idempotent and fail-closed. The workflow must update `README.md`, the V2 canonical corpus/timeline in `data/papers-source.html`, `article/3passive.tex`, `egbib_merged_20260711.bib`, and `bare_jrnl.tex`; it must then clean-build `bare_jrnl.pdf`, resolve all seven citations in `.aux/.bbl`, validate PDF semantic text and render endpoints before committing public artifacts. The staging bibliography `egbib_20260823_plenoptic_thz_ome_gap.bib` is removed only after successful source integration.

If the guarded build or validation fails, no partially updated README/site/survey/PDF should be pushed. The staging files and this note then serve as the precise patch/update record required for a later safe run.
