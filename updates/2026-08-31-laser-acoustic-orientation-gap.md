# 2026-08-31 — Laser–acoustic NLOS human-orientation gap

## Verified missing paper

Ferdi Doğan, **“Early fusion of laser and acoustic features for human orientation detection in non-line-of-sight environments,”** *Scientific Reports*, vol. 16, Article 25124, 2026. DOI: 10.1038/s41598-026-52682-6. Published 21 May 2026.

## Why this belongs

This is a task-oriented multimodal NLOS sensing paper rather than a generic classification paper. The controlled NLOS experiment acquires wall-mediated laser returns with a SPAD+TCSPC chain together with acoustic chirp measurements, extracts 21 features from each modality, and performs four-way hidden-human orientation classification (back/front/left/right). The work therefore extends the development line from full hidden-scene reconstruction toward semantic NLOS inference and multimodal optical–acoustic sensing. The authors also explicitly caution that the very high reported accuracy was obtained in a controlled setup with eight subjects and without matched laser-only/acoustic-only ablations, so the survey summary should avoid implying broad real-world generalization.

## Guarded integration locations

1. **README.md — Latest Additions**: add a 2026 row near other semantic / human-detection / acoustic NLOS entries. Suggested concise summary: “Fuses SPAD–TCSPC laser-return statistics with acoustic-chirp features for four-class hidden-human orientation recognition, extending task-oriented NLOS sensing from presence/localization toward multimodal semantic inference; validation remains controlled and small-scale.”
2. **README.md — 2026 development timeline**: place under task-oriented / multimodal NLOS sensing, after active hidden-human detection and near acoustic NLOS localization.
3. **Website / Paper Explorer (`index.html` and canonical paper data source)**: add category tags such as `multimodal`, `active`, `acoustic`, `semantic sensing`, `human orientation`, venue `Scientific Reports 2026`, DOI link above.
4. **Survey source (`bare_jrnl.tex` or the included section file covering new scenes / detection-recognition)**: integrate semantically rather than appending a bare list. Suggested literature-review sentence: “Recent task-oriented systems also combine modalities: Doğan fused SPAD–TCSPC laser-return statistics with acoustic-chirp descriptors to classify the orientation of hidden people, illustrating a shift from geometric recovery toward multimodal semantic NLOS sensing, although evaluation remains limited to a controlled laboratory setting.” Cite `doganLaserAcousticNLOSOrientation2026`.
5. **Canonical bibliography**: merge the staged entry from `egbib_20260831_laser_acoustic_orientation_gap.bib` into the bibliography actually used by the survey; remove the staging file afterwards if that is the repository convention.
6. **PDF**: clean-rebuild `bare_jrnl.pdf` after source/bibliography integration; confirm the citation resolves and the DOI appears once in the bibliography.

## Cross-artifact verification

After integration, search the repository for both the exact title and DOI `10.1038/s41598-026-52682-6`. Confirm the paper is present in README, Paper Explorer / website data, survey prose, canonical BibTeX, and rebuilt PDF. Do not leave it only in an update note or staging `.bib` file.

## Search notes

A fresh-search pass also surfaced MD-NLOS (*iScience* 2026), learned LCT (*Physical Review Applied* 2026), compact long-range NLOS, DAAM passive NLOS, SPAD-array timing correction, eye-safe SPAD localization, 3D Gaussian Transient Rendering, and several acoustic/RF NLOS papers. MD-NLOS is already explicitly present in the repository timeline, while the other major items are already present in the corpus or prior update lineage, so they were not duplicated in this run.
