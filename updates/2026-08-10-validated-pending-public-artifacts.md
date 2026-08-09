# 10 August 2026 — validated pending NLOS public-artifact integration

## Fresh-search result

A fresh keyword, venue, lab/project-page, and core-paper citation-tracing pass did not verify a newer direct NLOS-imaging publication than the already covered *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, published 22 July 2026). The current actionable gap is therefore not another brand-new optical transient paper, but the outstanding cross-artifact integration from the RF/mmWave citation trace and metadata audit below.

## Records that still need to propagate into the public artifacts

The generated and validated update contains the following genuinely missing or corrected records:

1. **MARMOT: Masked Autoencoder for Modeling Transient Imaging** — Shen et al., arXiv:2506.08470 (2025). No final journal/conference venue was verified as of this audit. It belongs in the sparse/irregular acquisition and reusable transient-pretraining discussion rather than as a detached bibliography-only record.
2. **Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave** — Tosi, Henninger, Giroto de Oliveira, Mandelli, IEEE SPAWC 2024, pp. 331–335, DOI `10.1109/SPAWC60668.2024.10694426`. This is the missing experimental cellular-ISAC precursor.
3. **Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware** — correct the existing arXiv-only label to the final **32nd International Conference on Telecommunications (ICT 2026), pp. 25–30**. Keep arXiv:2604.07032 as the public full-text link when useful.
4. **N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization** — correct the existing arXiv-only label to **IEEE Transactions on Mobile Computing 25(5), 6002–6016 (2026)**, DOI `10.1109/TMC.2025.3634623`, with the complete seven-author record.
5. **Leveraging Rough-Relay-Surface Scattering for Non-Line-of-Sight mmWave Radar Sensing** — IEEE Internet of Things Journal 11(6), 10964–10978 (2024), DOI `10.1109/JIOT.2023.3328018`.
6. **Double Sparse Structure-Enhanced mmWave NLOS Imaging Under Multiangle Relay Surface** — IEEE Transactions on Signal Processing 72, 5628–5643 (2024), DOI `10.1109/TSP.2024.3505938`.
7. **Bayesian Compressive Sensing for NLOS mmWave Imaging Under Imprecisely Multiangle Surfaces** — IEEE Signal Processing Letters 32, 2075–2079 (2025), DOI `10.1109/LSP.2025.3567216`.
8. **mmWave-Based Relay Reflector Reconstruction for LiDAR-Free Around-Corner Human Sensing** — IEEE INFOCOM 2025, pp. 1–10, DOI `10.1109/INFOCOM55648.2025.11044715`.
9. **Hydra: Exploiting Multi-Bounce Scattering for Beyond-Field-of-View mmWave Radar** — ACM MobiCom 2024, pp. 1545–1559, DOI `10.1145/3636534.3690710`.
10. **MmWave NLOS Sensing under Rough Relay Surface: Challenges and Solutions** — IEEE Aerospace and Electronic Systems Magazine (2026), DOI `10.1109/MAES.2026.3701667`.

The six rough-relay records should be treated as one development trajectory: non-ideal rough scattering becomes useful sensing diversity; multi-angle structure is exploited through sparse inversion; uncertain relay orientation becomes a latent inference variable; the relay reflector itself can be reconstructed without LiDAR; and uncontrolled multi-bounce scattering can be used for beyond-field-of-view localization. This complements, rather than duplicates, CornerRadar, Mosaic, RFlect, mmNorm, HoloRadar, Wave-Former, and RISE.

## Precise bounded insertion locations

- **README.md**: insert the missing records in `## Latest Additions`; place the rough-relay/multi-angle/Hydra records in the RF/mmWave branch of the milestone timeline. Correct the ICT 2026 and N2LoS venue strings in place. The generated update changes the website-style tracked-entry count from **267 to 274** after the SPAWC precursor plus six rough-relay records are added; venue corrections do not change the count.
- **index.html**: add the corresponding paper objects to the `papers` array near the existing RF/mmWave/ISAC records, correct the ICT 2026 and N2LoS objects in place, set the hero/update metadata to the 9 August integration snapshot, and change the tracked-latest statistic to **274**.
- **article/5newscenes.tex**: in `New NLOS Scenes -> Radar-Based NLOS Imaging`, insert the cellular-ISAC paragraph after the introductory HoloRadar/RF trajectory and insert the subsection-style paragraph **“Rough, uncertain, and unknown relay geometry in mmWave NLOS”** before the measured/model-unfolded radar reconstruction discussion. Add the MARMOT literature-review sentence in the sparse/irregular transient-acquisition / learning discussion.
- **bare_jrnl.tex**: preserve the modular `article/5newscenes.tex` structure; update only the maintenance/provenance comment so the master source records that the survey includes the 9 August citation-trace integration.
- **egbib_merged_20260711.bib** (and canonical bibliography source if split): add one duplicate-free entry for each new citation key and replace the stale N2LoS metadata with the final TMC record. Required keys in the validated build include `tosiFeasibilityISACNLOS2024`, `tosiReliableISACNLOS2026`, `shenMARMOT2025`, `shiN2LoS2025`, `xuRoughRelayMmWave2024`, `xuDoubleSparseMmWave2024`, `xuBayesianMmWave2025`, `lvRelayReflector2025`, `mehrotraHydra2024`, and `liuRoughRelaySurvey2026`.

## Build and validation completed

A guarded updater was executed on GitHub Actions, followed by a clean LaTeX/BibTeX rebuild. The generated `bare_jrnl.pdf` is **55 pages** and **2,273,750 bytes**. Source/PDF consistency checks passed for MARMOT, both cellular-ISAC papers, the final N2LoS TMC record, and all six rough-relay citations. The PDF was additionally rendered and visually inspected on the first page, the radar rough-relay discussion page, and the corresponding reference page; no clipping, overlap, broken glyphs, or empty/corrupt-page failure was observed.

The successful artifact-export workflow run is GitHub Actions run `31333722330`. Its artifact is `nlos-finalized-public-artifacts-20260810` (artifact id `9043695201`, SHA-256 digest `45ba0d012254016c0a824cf32453208ec6d1c98eebc54a5f762bc849e44618a6`) and contains the validated README, website, survey source, merged bibliography, regenerated PDF, and provenance notes.

## Why the large public files were not overwritten in this commit

The repository's GitHub Actions token can build and validate the complete update but cannot push the generated commit: the final `git push` is rejected with HTTP 403 for `github-actions[bot]`. The available safe repository-write interface in this run supports bounded UTF-8 file replacement, but does not expose a safe binary-file upload path that can atomically carry the regenerated ~2.3 MB PDF together with the large text artifacts. Replacing README/index/survey files one-by-one while leaving an old PDF would create the exact cross-artifact inconsistency this repository is trying to avoid.

Therefore this commit follows the repository's requested fallback rule: **do not overwrite large files blindly; record a precise patch/update note instead**. The validated artifact above is the source of truth for the pending synchronized update. Once binary write/push permission is available, apply those generated files together and verify README, index, survey source, bibliography, and PDF in one final consistency pass.
