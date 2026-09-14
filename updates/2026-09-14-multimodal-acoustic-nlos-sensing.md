# 2026-09-14 NLOS update: multimodal human orientation and acoustic material recognition

This update records two high-confidence NLOS sensing papers that are absent from the current repository index/search results and should be integrated into the public artifacts when the large files can be edited safely.

## 1. Early fusion of laser and acoustic features for human orientation detection in non-line-of-sight environments

- Ferdi Doğan, *Scientific Reports* 16, 25124 (2026).
- DOI: https://doi.org/10.1038/s41598-026-52682-6
- Published: 21 May 2026.
- Contribution: combines laser time-of-flight and acoustic-chirp features using early fusion for four-way hidden-human orientation classification (front/back/left/right) under NLOS conditions. The study also uses explainable-AI analysis to identify influential laser and acoustic features. This extends NLOS sensing from hidden-person detection/localization toward semantic state/orientation estimation and is a useful multimodal bridge between optical and acoustic NLOS.
- Recommended README category: Active NLOS Imaging -> Detection, Tracking and Recognition and/or New NLOS Scenes and Modalities -> Multimodal / acoustic-optical sensing.
- Recommended timeline wording: "2026 — Laser–acoustic feature fusion extends task-oriented NLOS sensing from presence/localization to hidden-human orientation estimation."
- Recommended survey placement: article/5newscenes.tex near acoustic NLOS and cross-modal sensing. Suggested sentence: "Beyond localization, recent multimodal work fuses laser time-of-flight and acoustic-chirp features to infer the orientation of an occluded person, indicating a shift from geometric NLOS recovery toward semantic hidden-state estimation."

## 2. Material Classification from Non-Line-of-Sight Acoustic Echoes Using Wavelet-Acoustic Hybrid Feature Fusion

- Dilan Onat Alakuş and İbrahim Türkoğlu, *Sensors* 26(5), 1577 (2026).
- DOI: https://doi.org/10.3390/s26051577
- Published: 3 March 2026.
- Contribution: introduces the ANLOS-R dataset and classifies nine hidden/indirectly sensed materials from NLOS acoustic echoes using wavelet + classical acoustic features and recurrent/hybrid deep models. The best CNN–LSTM reports 0.99 balanced accuracy/macro-F1, with SHAP analysis relating discriminative features to material acoustics. This extends acoustic NLOS beyond localization and liveness/person recognition toward material/scene semantics.
- Recommended README category: New NLOS Scenes and Modalities -> Acoustic / semantic NLOS sensing.
- Recommended timeline wording: "2026 — Acoustic NLOS expands from localization and human sensing to interpretable material recognition from indirect echoes."
- Recommended survey placement: article/5newscenes.tex after acoustic NLOS localization/human-sensing work. Suggested sentence: "Acoustic NLOS sensing is also broadening from localization to semantic scene inference: wavelet–acoustic hybrid features and recurrent models have been used to classify material identity directly from indirect echoes, accompanied by an NLOS acoustic recognition dataset and explainability analysis."

## Citation-tracing pass

Forward-citation searches were re-run around the repository's Core seeds, including Velten et al. (2012), O'Toole et al. LCT (2018), Lindell et al. f-k migration (2019), Liu et al. phasor-field work, and Saunders et al. computational periscopy. The strongest recent forward-citation candidates surfaced in this pass (learned LCT, zero-phase phasor fields, arbitrary-relay 3D Gaussian transient rendering, compact/long-range active NLOS systems, relay-free acoustic localization, etc.) are already represented by the repository or recent update logs. The two papers above were found through the complementary recent-keyword/modality search and passed direct NLOS relevance + final-venue verification.

## Required cross-artifact integration

When safe whole-file/patch editing is available:

1. Add both papers to README.md Latest Additions and their semantic category sections.
2. Add both to index.html / Paper Explorer and the development timeline with the labels above.
3. Integrate the survey prose into article/5newscenes.tex (and therefore bare_jrnl.tex build), not as a detached appendix/list.
4. Merge the BibTeX entries from `egbib_20260914_multimodal_acoustic_nlos_sensing.bib` into the canonical bibliography used by the survey, preserving repository citation-key conventions.
5. Rebuild bare_jrnl.pdf and verify that README, website, survey source, bibliography, and PDF expose the same two additions.

No claim is made here that the large public-facing artifacts or PDF have already been rebuilt; this note is the safe staging path to avoid truncating large files from partial connector responses.
