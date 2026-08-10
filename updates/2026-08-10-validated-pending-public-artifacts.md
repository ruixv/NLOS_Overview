# 10 August 2026 — validated pending NLOS public-artifact integration

## Fresh-search result

A fresh keyword, venue, lab/project-page, arXiv, and core-paper forward-citation pass did not verify a newer direct NLOS-imaging publication than *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, published 22 July 2026). The citation-tracing pass did, however, expose one additional fully metadata-verifiable omission that is directly relevant to the active-transient / learned-reconstruction trajectory:

### Newly verified missing paper

**Non-line-of-sight multi-person pose sensing** — Yusen Hou, Xingyu Cui, Shida Sun, Yue Li, Jing Huang, Zhi Lu, Kun Li, Zhiwei Xiong, Jingyu Yang, *Optics Express* **33**(20), 41937–41950 (2025), DOI `10.1364/OE.570120`.

- Final-venue audit: this is a final *Optics Express* paper, not an arXiv-only record.
- Why it belongs: the method (AMPE-NLOS) extends active transient NLOS from scene reconstruction / single-person sensing to unified **multi-person 3D pose and mesh sensing**. A confocal pulsed-laser + single-pixel SPAD + TCSPC system provides transients; LCT first reconstructs coarse physics-aware 3D features, a 3D U-Net refines them, and body-center heatmaps guide sampling of SMPL parameter maps so multiple hidden people can be separated and reconstructed.
- Citation-tracing relevance: the paper explicitly situates itself in the LCT, f-k, and phasor-field lineages rather than merely citing NLOS work in passing, making it a strong forward-lineage candidate from the repository's Core papers.
- Repository check on 10 August 2026: exact-title / DOI searches found no current `README.md`, `index.html`, or repository-wide canonical record. It is therefore a genuine omission.
- Canonical source: https://doi.org/10.1364/OE.570120

BibTeX-ready record:

```bibtex
@article{hou2025multipersonNLOS,
  author  = {Hou, Yusen and Cui, Xingyu and Sun, Shida and Li, Yue and Huang, Jing and Lu, Zhi and Li, Kun and Xiong, Zhiwei and Yang, Jingyu},
  title   = {Non-line-of-sight multi-person pose sensing},
  journal = {Optics Express},
  volume  = {33},
  number  = {20},
  pages   = {41937--41950},
  year    = {2025},
  doi     = {10.1364/OE.570120},
  url     = {https://doi.org/10.1364/OE.570120}
}
```

## Precise insertion plan for the newly verified paper

When the next synchronized binary-capable update is applied:

- **README.md**: add the paper to the 2025 active-transient / learned-reconstruction portion of `Latest Additions`; categorize it under active ToF, learned reconstruction, human sensing / downstream perception. Suggested concise summary: `AMPE-NLOS combines LCT-derived coarse 3D features, a 3D U-Net, body-center heatmaps and SMPL-parameter sampling to recover multiple hidden human meshes from confocal SPAD transients; it also introduces a multi-person transient dataset and validates on a self-built system.`
- **index.html / paper explorer**: add one searchable paper object with final *Optics Express* metadata, DOI link, modality `Optical / active transient`, method tags `LCT`, `3D U-Net`, `SMPL`, `human pose`, and year 2025. Add a short 2025 timeline note that active NLOS reconstruction is increasingly being used as a front-end for structured downstream perception rather than only geometry recovery.
- **survey source**: insert a short literature-review sentence in the learned active-NLOS / hidden-human-sensing discussion, near works on learned transient reconstruction and NLOS pose estimation rather than in the RF/mmWave section. Suggested trajectory sentence: `Beyond recovering hidden geometry, Hou et al. couple an LCT-based volumetric front end with learned refinement, body-center localization and SMPL regression to extend active transient NLOS to multi-person 3D pose and mesh sensing, illustrating a shift from reconstruction toward structured downstream perception.`
- **bibliography**: add `hou2025multipersonNLOS` exactly once with the final *Optics Express* metadata above.
- **bare_jrnl.pdf**: rebuild in the same synchronized change as README/index/survey/BibTeX, then verify the citation in both prose and references. Do not publish source-only changes with an old PDF.

## Previously discovered ToF benchmark — current status correction

**A comprehensive study of time-of-flight non-line-of-sight imaging** — Julio Marco, Adrian Jarabo, Ji Hyun Nam, Alberto Tosi, Diego Gutierrez, Andreas Velten, arXiv:2603.09548 (2026).

The earlier version of this note described this paper as absent from all public/source artifacts. That statement is now stale: the current repository already contains the paper in `README.md`, `article/2active.tex`, and `egbib_merged_20260711.bib`. The public `index.html` still lacks the record, so it remains a **cross-artifact consistency item**, not a completely missing-paper item. No final conference/journal venue has been independently verified; retain **arXiv 2026** until that changes.

The paper remains important as a controlled theory/benchmark bridge across Velten 2012, LCT, f-k migration and phasor-field formulations: it places representative ToF methods under a common model and compares them using common hardware and comparable photon counts.

## FermatFormer metadata hold

**FermatFormer: A Fermat Optics Based Neural Architecture for Non-line-of-sight Imaging** — ICCP 2026 — remains a tracked candidate. Public author/lab information identifies it as an ICCP 2026 paper and reports a Best Paper Honorable Mention, but a canonical proceedings record with complete author list, page range, DOI and stable paper URL has not yet been independently indexed. Do **not** invent a BibTeX record; integrate only after complete metadata is verifiable.

## Already propagated cellular-ISAC lineage

Commit `e4c2d54a0d33d31be6f1b40ca71929b1200b06c7` synchronized the validated cellular-ISAC lineage across README, website, survey source, bibliography and rebuilt PDF:

1. **Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave** — Tosi, Henninger, Giroto de Oliveira, Mandelli, IEEE SPAWC 2024, pp. 331–335, DOI `10.1109/SPAWC60668.2024.10694426`.
2. **Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware** — final **32nd International Conference on Telecommunications (ICT 2026), pp. 25–30**; arXiv:2604.07032 retained as a public full-text link.

## Still pending from the validated later artifact

The later generated artifact contains these additional verified records/corrections that are not yet atomically propagated into all public files:

1. **MARMOT: Masked Autoencoder for Modeling Transient Imaging** — Shen et al., arXiv:2506.08470 (2025). No final journal/conference venue verified as of this audit.
2. **N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization** — final **IEEE Transactions on Mobile Computing 25(5), 6002–6016 (2026)**, DOI `10.1109/TMC.2025.3634623`, with the complete seven-author record.
3. **Leveraging Rough-Relay-Surface Scattering for Non-Line-of-Sight mmWave Radar Sensing** — *IEEE Internet of Things Journal* 11(6), 10964–10978 (2024), DOI `10.1109/JIOT.2023.3328018`.
4. **Double Sparse Structure-Enhanced mmWave NLOS Imaging Under Multiangle Relay Surface** — *IEEE Transactions on Signal Processing* 72, 5628–5643 (2024), DOI `10.1109/TSP.2024.3505938`.
5. **Bayesian Compressive Sensing for NLOS mmWave Imaging Under Imprecisely Multiangle Surfaces** — *IEEE Signal Processing Letters* 32, 2075–2079 (2025), DOI `10.1109/LSP.2025.3567216`.
6. **mmWave-Based Relay Reflector Reconstruction for LiDAR-Free Around-Corner Human Sensing** — IEEE INFOCOM 2025, pp. 1–10, DOI `10.1109/INFOCOM55648.2025.11044715`.
7. **Hydra: Exploiting Multi-Bounce Scattering for Beyond-Field-of-View mmWave Radar** — ACM MobiCom 2024, pp. 1545–1559, DOI `10.1145/3636534.3690710`.
8. **MmWave NLOS Sensing under Rough Relay Surface: Challenges and Solutions** — *IEEE Aerospace and Electronic Systems Magazine* (2026), DOI `10.1109/MAES.2026.3701667`.

The six rough-relay records form a coherent trajectory: non-ideal rough scattering becomes useful sensing diversity; multi-angle structure is exploited through sparse inversion; uncertain relay orientation becomes a latent inference variable; the relay reflector itself can be reconstructed without LiDAR; and uncontrolled multi-bounce scattering can be used for beyond-field-of-view localization.

## Validated complete artifact and propagation limitation

GitHub Actions run `31333722330` produced `nlos-finalized-public-artifacts-20260810` (artifact id `9043695201`, SHA-256 digest `45ba0d012254016c0a824cf32453208ec6d1c98eebc54a5f762bc849e44618a6`). It contains generated README, website, survey source, merged bibliography and a 55-page, 2,273,750-byte `bare_jrnl.pdf` incorporating MARMOT, final N2LoS metadata, the rough-relay cluster, and the Marco ToF benchmark. LaTeX/BibTeX compilation, undefined-citation checks, PDF semantic checks and rendered-page checks passed.

That artifact **predates the newly verified multi-person pose paper**. It therefore must not be treated as the final source of truth for this run. The current connector does not expose a safe atomic binary-artifact-to-Git-blob publication path, and a temporary one-shot Actions publisher created during this audit did not trigger from connector-authored pushes; it was removed immediately so no dead workflow remains on `master`. To avoid a README/source/PDF mismatch, the large public artifacts were not overwritten piecemeal.

The current public website count is **268**. Because the validated artifact and current public branch have diverged in which records/corrections they contain, do not hard-code a future explorer count from the older staging note; recompute it from the merged canonical paper objects when the next synchronized build is applied.
