# 2026-09-21 gap: laser–acoustic NLOS human-orientation sensing

## Verified missing paper

Ferdi Doğan, “Early fusion of laser and acoustic features for human orientation detection in non-line-of-sight environments,” *Scientific Reports*, vol. 16, Article 25124, 2026. Published 21 May 2026. DOI: 10.1038/s41598-026-52682-6.

Repository-wide title search before staging returned no match.

## Why it belongs

This is a genuine NLOS sensing paper rather than a generic multimodal-classification citation. The experiment places a human target in an occluded stage and collects indirect laser photon-count and acoustic-chirp measurements. It studies a semantic NLOS objective—four-way human orientation (front/back/left/right)—rather than reconstructing a full hidden image. Twenty-one features from each modality are fused into a 42-dimensional representation and evaluated with conventional classifiers and the proposed LAO-Net. The paper should be presented cautiously: the reported very high accuracy is obtained in a controlled laboratory setting with eight subjects, and the paper itself notes the lack of matched laser-only/acoustic-only ablations and subject-independent validation.

## Suggested integration

- **README.md / Latest Additions:** add under 2026 as multimodal NLOS sensing. Suggested summary: “Fuses indirect SPAD/TCSPC laser photon-count features with acoustic-chirp features for four-way hidden-human orientation classification, extending NLOS sensing from presence/localization toward semantic pose/orientation; results are demonstrated in a controlled eight-subject laboratory setup.”
- **README taxonomy:** place in **New NLOS Scenes and Modalities** or the detection/tracking/recognition subsection, near acoustic/RF semantic sensing rather than active optical 3-D reconstruction.
- **Website / Paper Explorer:** tags: `2026`, `multimodal`, `laser`, `acoustic`, `human sensing`, `orientation`, `NLOS recognition`; add a 2026 timeline item only as a modality/semantic-sensing expansion, not a core reconstruction milestone.
- **bare_jrnl.tex:** integrate into the emerging-modality / semantic-NLOS discussion. A suitable literature-review sentence is: “Beyond geometry and localization, recent multimodal systems combine indirect optical photon-count and acoustic-echo features to infer semantic attributes such as hidden-human orientation, illustrating a shift from NLOS image formation toward task-oriented multimodal perception.” Follow with a caveat that current evidence is from controlled small-cohort experiments.
- **Bibliography:** merge the verified entry staged in `egbib_20260921_laser_acoustic_orientation.bib` into the canonical bibliography used by `bare_jrnl.tex`.
- **PDF:** rebuild `bare_jrnl.pdf` only after the canonical TeX and bibliography are updated and compiled successfully.

## Consistency status

This file is a staging/integration note because the large canonical public-facing files could not be safely rewritten from a partial payload in this run. Do not claim README/index/TeX/PDF consistency until the staged entry is merged and the PDF is rebuilt.
