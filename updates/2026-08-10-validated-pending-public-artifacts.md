# 10 August 2026 — validated pending NLOS public-artifact integration

## Fresh-search result

A fresh keyword, venue, lab/project-page, and core-paper citation-tracing pass did not verify a newer direct NLOS-imaging publication than the already covered *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, published 22 July 2026). The remaining actionable gap is therefore cross-artifact propagation of already verified citation-trace records rather than another brand-new optical transient paper.

## Propagated on 10 August 2026

Commit `e4c2d54a0d33d31be6f1b40ca71929b1200b06c7` atomically synchronized the validated cellular-ISAC lineage across `README.md`, `index.html`, `article/5newscenes.tex`, `bare_jrnl.tex`, the bibliography sources, and `bare_jrnl.pdf`:

1. **Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave** — Tosi, Henninger, Giroto de Oliveira, Mandelli, IEEE SPAWC 2024, pp. 331–335, DOI `10.1109/SPAWC60668.2024.10694426`.
2. **Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware** — corrected from arXiv-only metadata to the final **32nd International Conference on Telecommunications (ICT 2026), pp. 25–30**; arXiv:2604.07032 is retained as the public full-text link.

The published PDF in that commit is the matching rebuilt PDF from the validated ISAC integration branch, so the public README / website / survey source / bibliography / PDF are mutually consistent at this integration level.

## Still pending from the later validated artifact

The later generated artifact contains the following additional verified records/corrections that are not yet propagated into the public files:

1. **MARMOT: Masked Autoencoder for Modeling Transient Imaging** — Shen et al., arXiv:2506.08470 (2025). No final journal/conference venue was verified as of this audit.
2. **N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization** — final **IEEE Transactions on Mobile Computing 25(5), 6002–6016 (2026)**, DOI `10.1109/TMC.2025.3634623`, with the complete seven-author record.
3. **Leveraging Rough-Relay-Surface Scattering for Non-Line-of-Sight mmWave Radar Sensing** — IEEE Internet of Things Journal 11(6), 10964–10978 (2024), DOI `10.1109/JIOT.2023.3328018`.
4. **Double Sparse Structure-Enhanced mmWave NLOS Imaging Under Multiangle Relay Surface** — IEEE Transactions on Signal Processing 72, 5628–5643 (2024), DOI `10.1109/TSP.2024.3505938`.
5. **Bayesian Compressive Sensing for NLOS mmWave Imaging Under Imprecisely Multiangle Surfaces** — IEEE Signal Processing Letters 32, 2075–2079 (2025), DOI `10.1109/LSP.2025.3567216`.
6. **mmWave-Based Relay Reflector Reconstruction for LiDAR-Free Around-Corner Human Sensing** — IEEE INFOCOM 2025, pp. 1–10, DOI `10.1109/INFOCOM55648.2025.11044715`.
7. **Hydra: Exploiting Multi-Bounce Scattering for Beyond-Field-of-View mmWave Radar** — ACM MobiCom 2024, pp. 1545–1559, DOI `10.1145/3636534.3690710`.
8. **MmWave NLOS Sensing under Rough Relay Surface: Challenges and Solutions** — IEEE Aerospace and Electronic Systems Magazine (2026), DOI `10.1109/MAES.2026.3701667`.

The six rough-relay records form one trajectory: non-ideal rough scattering becomes useful sensing diversity; multi-angle structure is exploited through sparse inversion; uncertain relay orientation becomes a latent inference variable; the relay reflector itself can be reconstructed without LiDAR; and uncontrolled multi-bounce scattering can be used for beyond-field-of-view localization.

## Validated complete artifact

GitHub Actions run `31333722330` successfully produced `nlos-finalized-public-artifacts-20260810` (artifact id `9043695201`, SHA-256 digest `45ba0d012254016c0a824cf32453208ec6d1c98eebc54a5f762bc849e44618a6`). It contains the fully generated README, website, survey source, merged bibliography, and a 55-page, 2,273,750-byte `bare_jrnl.pdf` incorporating MARMOT, final N2LoS metadata, and all six rough-relay citations. LaTeX/BibTeX compilation, undefined-citation checks, PDF semantic checks, and rendered-page checks passed.

The current repository interface can safely reuse existing Git blob objects, which allowed the ISAC bundle above to be published atomically. The *later* complete artifact exists only as an Actions artifact rather than committed Git blobs, and the connector does not provide a direct binary-artifact-to-Git-blob copy operation. Therefore the eight later records remain explicitly pending instead of creating a README/source/PDF mismatch. The artifact remains the source of truth for their next bounded propagation.
