# 17 August 2026 passive speckle imaging/localization gap

## Newly verified missing work

Zhiyuan Wang, Huiling Huang, Haoran Li, Ziyang Chen, Jun Han, and Jixiong Pu, **Non-line-of-sight imaging and location determination using deep learning**, *Optics and Lasers in Engineering* 169, article 107701 (2023), DOI `10.1016/j.optlaseng.2023.107701`.

Elsevier's final article record describes a passive NLOS system that takes a single-shot speckle pattern and uses SPIR-Net to reconstruct hidden-object appearance while simultaneously determining object position. The method specifically removes the pulsed-laser and time-gating requirements normally used to obtain location in active transient NLOS. The reported network combines modified LeNet, U-Net, and cGAN components.

## Why it belongs in the survey

This is not a generic scattering-media paper: the experiment is explicitly framed as around-corner/passive NLOS, with light observed after reflection from a rough relay surface and the target hidden from direct view. Its contribution fills a historical gap between early steady-state passive learned reconstruction/recognition and later tracking/action-recognition systems by making spatial location a co-estimated output of the wall-mediated speckle measurement.

The paper was also cited by later learned NLOS reconstruction work, which makes it a useful citation-lineage predecessor even though it was surfaced in this run by exact passive-NLOS/learning search rather than a directly enumerable scholarly forward-citation list.

## Venue decision

Use the final Elsevier publication rather than a preprint label: *Optics and Lasers in Engineering*, volume 169, October 2023, article 107701, DOI `10.1016/j.optlaseng.2023.107701`.

## Precise integration locations

- `README.md`: add the verified paper to the Latest Additions table, and add a 2023 milestone sentence immediately after the existing Boger-Lombard acoustic-daylight entry.
- `data/papers-source.html`: add one canonical paper object to `const papers=[...]`, increment the tracked-entry counter by one, and append the contribution to the 2023 Development Timeline paragraph.
- `article/3passive.tex`: immediately after **Room-scale real-time passive reconstruction**, add a short paragraph titled **Joint passive imaging and localization from speckle** citing `wangPassiveImagingLocalization2023` and explaining SPIR-Net as the bridge from passive image recovery/recognition to simultaneous learned spatial localization.
- `bare_jrnl.tex`: add the 17 August 2026 synchronization provenance marker; the public snapshot date already reads through 17 August 2026 and should not be artificially advanced.
- `egbib_merged_20260711.bib`: merge the staged `wangPassiveImagingLocalization2023` entry and verify that both the BibTeX key and DOI are unique.
- `bare_jrnl.pdf`: rebuild only after all source changes pass validation; require successful BibTeX resolution, semantic text presence for the new paragraph/reference, and first/last-page rendering.

## Current execution status

A validated integration script and GitHub Actions workflow are committed. The first workflow attempt stopped safely before any public artifact was changed because an outdated README timeline anchor did not match the current repository text. The anchor has been corrected and a retry has been triggered. At the time this note was committed, that retry was still queued by GitHub Actions, so the public README / website / survey / merged bibliography / PDF must **not** yet be described as updated. The staged BibTeX and this patch note preserve the verified metadata and exact insertion plan without risking truncation of large public files.
