# Missing-paper integration note — acoustic NLOS material classification

## Verified missing paper

Dilan Onat Alakuş and İbrahim Türkoğlu, “Material Classification from Non-Line-of-Sight Acoustic Echoes Using Wavelet-Acoustic Hybrid Feature Fusion,” *Sensors*, 26(5), 1577, 2026. DOI: 10.3390/s26051577.

Publisher metadata reports publication on 3 March 2026. The paper introduces the ANLOS-R acoustic NLOS material-recognition dataset and combines wavelet features with acoustic descriptors and recurrent/deep models to classify nine materials from echoes measured without direct line of sight. It reports 99% balanced accuracy and macro-F1 for its Wavelet–Hybrid CNN–LSTM configuration and uses SHAP to analyze complementary MFCC and wavelet features.

## Scope assessment

This is tightly adjacent NLOS sensing rather than hidden-scene image reconstruction. It should therefore be included in the modality-expansion / acoustic NLOS sensing branch, but should not be presented as an optical-style NLOS reconstruction milestone. Its value to the survey is that it broadens acoustic NLOS from localization/geometry recovery toward inference of hidden-object/material properties from indirect echoes.

## Repository integration plan

- **README.md:** add under the 2026 acoustic / modality-expansion timeline, with a concise note that it performs hidden-material classification from NLOS echoes rather than image reconstruction.
- **index.html / Paper Explorer:** add as Acoustic; task = material recognition/classification; venue = Sensors 2026; include DOI/publisher link.
- **bare_jrnl.tex:** integrate semantically in the acoustic/RF/non-optical NLOS discussion, after acoustic localization/imaging works. Suggested trajectory sentence: “Beyond localization and geometry recovery, recent acoustic NLOS work has begun to infer latent scene properties: Alakuş and Türkoğlu classify hidden materials directly from indirect echoes by fusing wavelet and acoustic descriptors, illustrating a shift from acoustic NLOS imaging toward semantic/material sensing.”
- **Bibliography:** merge the verified entry from `egbib_20261002_acoustic_material_nlos_gap.bib` into the canonical bibliography and use the repository’s normal citation-key conventions if they differ.
- **PDF:** rebuild `bare_jrnl.pdf` only after the canonical TeX and bibliography are integrated and compile cleanly.

## Verification / consistency status

Repository-wide title search on the default branch returned no match before staging this paper. This note and the verified BibTeX staging file are intentionally small, safe updates; canonical README/index/TeX/PDF were not overwritten without a complete read-edit-build-validation cycle. Once canonical integration is performed, verify the paper appears consistently in README, website, survey source, bibliography, and rebuilt PDF.
