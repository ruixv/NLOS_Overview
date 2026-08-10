# 10 August 2026 — validated pending NLOS public-artifact integration

## Fresh-search result

A fresh keyword, venue, lab/project-page, arXiv, and core-paper citation-tracing pass did not verify a newer direct NLOS-imaging publication than the already covered *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, published 22 July 2026). The pass did, however, expose one fully metadata-verifiable paper that is genuinely missing from the repository and one very recent ICCP 2026 learned-NLOS paper that should be tracked until its canonical proceedings metadata is indexed.

### Newly verified missing paper

**A comprehensive study of time-of-flight non-line-of-sight imaging** — Julio Marco, Adrian Jarabo, Ji Hyun Nam, Alberto Tosi, Diego Gutierrez, Andreas Velten, arXiv:2603.09548 (2026).

- Final-venue audit: DBLP still lists the work as a CoRR/arXiv record, and no accepted/published journal or conference version was verified in this pass. It should therefore be labeled **arXiv 2026** for now.
- Why it belongs: the paper places representative ToF NLOS methods under one common forward model, relates simplified inverses to Radon-transform families and frequency-domain/phasor-wave formulations, and then compares methods on measurements captured with the same hardware and similar photon counts. It is a useful benchmark/theory bridge across the Velten--LCT--f-k--phasor-field lineage rather than another single reconstruction architecture.
- Repository check: exact-title searches found no current README/index/survey record, so this is a genuine omission rather than a duplicate.
- Source: https://arxiv.org/abs/2603.09548

BibTeX-ready canonical record for the current arXiv-only status:

```bibtex
@article{marcoComprehensiveToFNLOS2026,
  title   = {A comprehensive study of time-of-flight non-line-of-sight imaging},
  author  = {Marco, Julio and Jarabo, Adrian and Nam, Ji Hyun and Tosi, Alberto and Gutierrez, Diego and Velten, Andreas},
  journal = {arXiv preprint arXiv:2603.09548},
  year    = {2026},
  url     = {https://arxiv.org/abs/2603.09548}
}
```

### Newly discovered ICCP 2026 paper awaiting canonical proceedings metadata

**FermatFormer: A Fermat Optics Based Neural Architecture for Non-line-of-sight Imaging** — ICCP 2026.

- Ziheng Wang publicly identifies the work as his coauthored ICCP 2026 paper and reports a Best Paper Honorable Mention. His description states that FermatFormer represents transient measurements through stable Fermat points so that a physics-informed representation transfers more effectively from synthetic data to real measurements.
- The official ICCP 2026 site confirms the conference was held 13--15 July 2026 in Princeton and that the technical program was live. However, the currently indexed ICCP/OpenReview/proceedings pages do not yet expose a canonical FermatFormer record with a complete author list, page range, DOI, or stable paper URL.
- Repository check: the title is absent from the current README and public website.
- Relevance: the method is tightly aligned with the field-defining Fermat-path geometry lineage (Xin et al., CVPR 2019), but this note does **not** claim a forward citation until the paper itself is available for reference inspection.
- Action rule: do not invent incomplete metadata or add a guessed BibTeX entry. Integrate it into public artifacts only after the complete proceedings/arXiv/project-page record becomes independently verifiable.

## Precise insertion plan for the newly verified ToF benchmark

When the next synchronized binary-capable update is applied:

- **README.md**: add the Marco et al. paper to `Latest Additions`, categorize it under active ToF / benchmark-and-theory / surveys-and-comparisons, and summarize its common-model plus controlled-hardware comparison contribution. In the development timeline, place it in the 2026 branch alongside common-model benchmarking, phasor/f-k theory, and deployment-oriented ToF work rather than under learned reconstruction.
- **index.html**: add one searchable paper object and a short 2026 timeline sentence. The current public explorer count is 268; after the six already validated rough-relay additions plus this missing ToF benchmark are propagated, the expected count becomes **275**. FermatFormer would increase it to 276 only after its canonical metadata is verified and it is actually integrated.
- **article/2active.tex / survey prose**: insert a short literature-review paragraph in the active ToF reconstruction/model discussion, after the LCT/f-k/phasor-field relationship is introduced or near the common-model benchmarking discussion. Suggested trajectory sentence: `Marco et al. place representative ToF NLOS inverses under a common forward model and benchmark them with matched hardware and similar photon counts, showing that many apparent algorithmic differences share common limits in spatial resolution, visibility, and noise sensitivity; the study therefore provides a controlled bridge between Radon-transform, f-k, and phasor-field formulations.`
- **bare_jrnl.tex**: preserve the modular source structure; add only the maintenance/provenance comment after the section-level integration is made.
- **Bibliography**: add `marcoComprehensiveToFNLOS2026` once, with arXiv as the venue until a final venue is independently verified.
- **bare_jrnl.pdf**: rebuild only in the same synchronized change as README/index/source/bibliography, and verify that the new citation appears in both prose and references. Do not publish text-source changes with an old PDF.

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

That validated artifact predates the newly discovered Marco et al. benchmark and FermatFormer, so it is **not** the source of truth for those two newly identified records. The current repository interface can safely reuse existing Git blob objects, which allowed the ISAC bundle above to be published atomically. The later complete artifact exists only as an Actions artifact rather than committed Git blobs, and the connector does not provide a direct binary-artifact-to-Git-blob copy operation. Therefore the eight later records plus the newly verified Marco et al. benchmark remain explicitly pending instead of creating a README/source/PDF mismatch. FermatFormer remains a tracked candidate until complete publication metadata is independently verifiable.
