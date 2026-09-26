# Integration gap: laser–acoustic NLOS human orientation (2026-09-26)

## Verified missing paper

Ferdi Doğan, **“Early fusion of laser and acoustic features for human orientation detection in non-line-of-sight environments,”** *Scientific Reports*, vol. 16, Article 25124, 2026. Published 21 May 2026. DOI: https://doi.org/10.1038/s41598-026-52682-6

Repository-wide title/DOI searches returned no hit before staging this update.

## Why it belongs

This is a genuine NLOS sensing paper rather than generic multimodal recognition. The controlled setup measures a hidden person using both laser time-of-flight data (SPAD + TCSPC) and acoustic chirps reflected through the NLOS environment. Twenty-one laser and twenty-one acoustic features are fused for four-way human-orientation classification (front/back/left/right), independent of standing/sitting/crouching posture. The proposed LAO-Net reports 99.98% accuracy under the paper's controlled protocol. The paper explicitly cautions that it uses eight subjects, a controlled single-reflector setting, window-derived samples that are not fully independent, and lacks matched laser-only/acoustic-only ablations, so the result should not be presented as proof of broad real-world generalization or of a quantified fusion gain.

## Recommended canonical integration

- **README.md — Latest Additions / New NLOS Scenes and Modalities:** add under multimodal/acoustic sensing. Suggested concise summary: “Fuses SPAD/TCSPC laser-ToF and acoustic-chirp features for four-class hidden-human orientation recognition, extending NLOS sensing beyond presence/localization toward semantic pose/orientation cues; strong controlled-set performance, with limited-subject and no single-modality-ablation caveats.”
- **Milestone timeline (2026):** place near recent acoustic identity/localization and RF/mmWave semantic NLOS entries as a modality-fusion milestone rather than an optical 3D-reconstruction milestone.
- **index.html / Paper Explorer:** tags: `Multimodal`, `Acoustic`, `Laser/ToF`, `SPAD`, `Recognition`, `Human sensing`, `NLOS orientation`, `2026`.
- **bare_jrnl.tex:** integrate semantically in the emerging modalities / task-oriented NLOS sensing discussion. A suitable literature-review point is that recent NLOS work increasingly combines complementary propagation channels and targets semantic attributes (identity/orientation) rather than reconstructing complete hidden geometry. Keep the limitations above explicit if quantitative accuracy is mentioned.
- **Bibliography:** merge `egbib_20260926_laser_acoustic_orientation.bib` into the canonical bibliography used by `bare_jrnl.tex` and cite it from the new sentence.
- **bare_jrnl.pdf:** rebuild only after the source and canonical bibliography are integrated and compile cleanly.

## Consistency status

This run intentionally does **not** claim README/index/LaTeX/PDF integration. Large canonical artifacts were not overwritten from partial/truncated connector payloads. The verified BibTeX staging file and this insertion plan are safe follow-up inputs for a guarded full-source integration/build.
