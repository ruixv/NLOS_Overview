# Laser–acoustic NLOS human-orientation sensing update

## Verified record

**Early fusion of laser and acoustic features for human orientation detection in non-line-of-sight environments** — Ferdi Doğan, *Scientific Reports* (2026), DOI: `10.1038/s41598-026-52682-6`, published online 21 May 2026.

The controlled NLOS experiments combine engineered features from laser and acoustic chirp measurements. Each modality contributes 21 features, producing a 42-dimensional early-fusion representation evaluated with conventional machine-learning classifiers, the proposed LAO-Net, and explainable-AI feature analysis for four hidden-person orientation classes. The work is categorized as multimodal semantic NLOS sensing rather than hidden-image, position-map, or 3D-geometry reconstruction.

## Intended integration

- Add a scope-aware row to the README Latest Additions table and a 2026 timeline sentence.
- Add a searchable website paper object tagged for laser, acoustic, fusion, learning, recognition, and orientation; recalculate the explorer count.
- Add a short literature-review paragraph after the acoustic diffraction discussion in `article/5newscenes.tex`.
- Merge the DOI-verified BibTeX entry into `egbib_merged_20260711.bib` under `doganLaserAcousticOrientationNLOS2026`.
- Add a trace marker to `bare_jrnl.tex`, compile the survey, verify that the citation resolves in `bare_jrnl.bbl`, and commit the regenerated `bare_jrnl.pdf`.

The guarded workflow commits public-source and PDF changes only after title/DOI uniqueness, website-count, bibliography-key, LaTeX, and PDF checks all pass.
