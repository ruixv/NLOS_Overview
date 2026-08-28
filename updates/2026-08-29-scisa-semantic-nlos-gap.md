# 2026-08-29 — SCISA-Net semantic NLOS gap

## Verified paper

- Jihao Dai, Hongshuai Qin, Guowen Li, Jin Liu, Xiaoshuai Zhang, **“SCISA-Net: Scene-Constrained Inverse-to-Subband Attention for Semantic Inference from Wall-Mediated Indirect Observations,”** *Photonics* 13(6), 575 (2026).
- DOI: `10.3390/photonics13060575`
- Final venue verified from the publisher page; published 11 June 2026.
- Canonical BibTeX key: `daiSCISANet2026`.

## Why this is a genuine NLOS paper

The work studies category-level semantic inference from a hidden display terminal using only a calibrated wall-mediated indirect intensity observation. The camera never directly sees the display. Its front end performs scene-constrained inverse reorganization of the indirect wall measurement, followed by multi-stage Haar-subband attention for semantic discrimination. The paper explicitly positions LCT, f-k migration, phasor-field NLOS, arbitrary illumination/detection NLOS, and other NLOS reconstruction/recognition works as direct predecessors, so this is not a passing-citation case.

## Contribution summary for public artifacts

**SCISA-Net** couples a scene-constrained inverse module with multi-stage Haar-subband attention to recover weak class-discriminative evidence from a single wall-mediated indirect image. On a calibrated 31-class hidden-display benchmark, it reports macro-F1 0.7170 and AUC 0.9759, and studies robustness to illumination attenuation, ambient background, Poisson/Gaussian/scatter corruption, and scene re-parameterization. It extends NLOS research from reconstruction/localization toward calibrated semantic inference and optical side-channel sensing.

## Required integration locations

1. **README.md — Latest Additions**
   Add a 2026 row under learned/passive/semantic NLOS:
   - Paper: `SCISA-Net: Scene-Constrained Inverse-to-Subband Attention for Semantic Inference from Wall-Mediated Indirect Observations`
   - Venue: `Photonics 13(6), 575 (2026)`
   - DOI: `https://doi.org/10.3390/photonics13060575`
   - Summary: use the concise contribution summary above.

2. **README.md — 2026 development timeline**
   Add a semantic-sensing milestone after learned passive recognition / task-oriented NLOS entries:
   - `2026 — Scene-constrained inversion + subband attention enables category-level semantic inference directly from calibrated wall-mediated indirect observations, extending NLOS from image recovery toward hidden-content recognition and optical semantic leakage analysis.`

3. **Website canonical corpus (`data/papers-source.html`)**
   Add exactly one paper object with:
   - title as above
   - authors: `Jihao Dai; Hongshuai Qin; Guowen Li; Jin Liu; Xiaoshuai Zhang`
   - year: `2026`
   - venue: `Photonics 13(6), 575 (2026)`
   - DOI URL: `https://doi.org/10.3390/photonics13060575`
   - key: `daiSCISANet2026`
   - family: `learning` or the repository’s nearest semantic/passive-learning category
   - contribution: concise summary above.
   Recompute tracked-entry counts rather than hand-editing them.

4. **Website development timeline / latest additions**
   Add the same 2026 semantic-inference milestone. Do not duplicate the paper object in `index.html` if `data/papers-source.html` remains the canonical corpus source.

5. **Survey source**
   Insert semantically in the learned NLOS recognition / passive semantic inference discussion, not as an isolated appendix list. Suggested prose:

   `Beyond reconstructing hidden appearance or geometry, Dai et al. introduced SCISA-Net for category-level semantic inference directly from calibrated wall-mediated indirect observations \cite{daiSCISANet2026}. Their scene-constrained inverse module first reorganizes the occlusion-dominated wall measurement into a representation aligned with the hidden source domain, after which multi-stage Haar-subband attention aggregates weak frequency-dependent discriminative cues. This direction extends learned NLOS sensing from reconstruction and localization toward direct semantic inference and raises a complementary security perspective in which indirect optical transport itself may leak hidden visual content.`

   The most appropriate file is likely `article/4datadriven.tex` if semantic learned inference is grouped with data-driven methods; if the repository currently places passive recognition in `article/3passive.tex`, use that section instead. Preserve existing citation style and paragraph formatting.

6. **Canonical bibliography**
   Merge `egbib_20260829_scisa_semantic_nlos_gap.bib` into the bibliography actually used by `bare_jrnl.tex`. Ensure exactly one DOI `10.3390/photonics13060575` and exactly one citation key `daiSCISANet2026`.

7. **bare_jrnl.tex / PDF**
   Ensure the included section file containing the new prose is referenced by `bare_jrnl.tex`, then run a clean build (`pdflatex -> bibtex -> pdflatex -> pdflatex`, or the repository's established equivalent). Verify `daiSCISANet2026` resolves in `.aux/.bbl`, the DOI appears once in the bibliography, the semantic-inference paragraph appears in extracted PDF text, and representative pages render correctly before committing `bare_jrnl.pdf`.

## Current-run safety status

The repository’s public README, website corpus, survey source, bibliography and binary PDF are large and have accumulated several recent staged integrations. To avoid truncation or a partial cross-artifact update through whole-file replacement, this run records the verified BibTeX and exact insertion plan rather than overwriting those artifacts blindly. The paper should be folded into the next guarded full-checkout integration together with other pending verified records, followed by a clean survey rebuild and consistency audit.
