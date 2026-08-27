# 28 August 2026 — Acoustic material NLOS bibliography consistency repair

## Finding

A fresh recent-paper and citation-lineage audit did not identify a new high-confidence NLOS paper that is absent from the public corpus. However, it found a concrete cross-artifact consistency gap in the acoustic NLOS branch.

The following two peer-reviewed 2026 papers are already present in the public README, the canonical V2 paper corpus (`data/papers-source.html`), and the survey narrative (`article/5newscenes.tex`), but their canonical citation keys are absent from `egbib_merged_20260711.bib`:

1. Dilan Onat Alakuş and İbrahim Türkoğlu, “Material Classification in Acoustic NLOS Environments Using an Attention-Based U-Net and Multimodal Fusion With the ANLOS-R Dataset,” *IEEE Access*, vol. 14, pp. 26983–27004, 2026. DOI: `10.1109/ACCESS.2026.3664294`. Canonical key: `alakusANLOSR2026`.
2. Dilan Onat Alakuş and İbrahim Türkoğlu, “Material Classification from Non-Line-of-Sight Acoustic Echoes Using Wavelet-Acoustic Hybrid Feature Fusion,” *Sensors*, vol. 26, no. 5, article 1577, 2026. DOI: `10.3390/s26051577`. Canonical key: `alakusAcousticMaterialNLOS2026`.

The survey already cites both keys in the **Acoustic NLOS Imaging** subsection, under **Material recognition from wall-mediated acoustic echoes**. The README and V2 corpus already describe the IEEE Access paper as the ANLOS-R dataset / attention-U-Net precursor and the Sensors paper as the wavelet–acoustic / SHAP follow-up. Therefore, do **not** add duplicate README rows, V2 paper objects, timeline items, or survey prose.

## Required integration

1. Merge the two entries from `egbib_20260828_acoustic_material_consistency.bib` into `egbib_merged_20260711.bib` using the existing duplicate-free bibliography workflow.
2. Preserve the exact citation keys `alakusANLOSR2026` and `alakusAcousticMaterialNLOS2026`, because `article/5newscenes.tex` already references those keys.
3. Verify that each DOI appears exactly once in the merged bibliography:
   - `10.1109/ACCESS.2026.3664294`
   - `10.3390/s26051577`
4. Do not change README.md or `data/papers-source.html` unless a later audit finds a factual metadata mismatch; both public artifacts already contain the papers.
5. Do not duplicate the existing survey paragraph in `article/5newscenes.tex`.

## PDF rebuild and validation

After merging the bibliography, rebuild the survey cleanly with the repository’s normal sequence, e.g. `pdflatex -> bibtex -> pdflatex -> pdflatex` (or the equivalent repository workflow). Then confirm:

- both citation keys resolve in the `.aux` / `.bbl`;
- no undefined citations remain;
- `bare_jrnl.pdf` contains both acoustic-material references and the existing “Material recognition from wall-mediated acoustic echoes” discussion;
- README, V2 paper corpus, survey source, merged bibliography, and PDF are mutually consistent.

Only commit a rebuilt `bare_jrnl.pdf` after those checks pass. Until then, the existing public PDF should not be described as repaired by this update.

## Research-screening note

The 28 August 2026 search also re-checked recent optical transient NLOS, passive NLOS, consumer-LiDAR, RF/mmWave, acoustic, learned reconstruction, and forward-citation hits from LCT, f-k migration, phasor-field, computational periscopy, and learned transient milestones. The strongest recent hits were already represented in the repository; this run therefore records a bibliography consistency repair rather than adding another paper to the corpus.
