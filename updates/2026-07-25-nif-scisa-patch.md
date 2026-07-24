# NIF and SCISA-Net cross-artifact update — 25 July 2026

## Search result

No direct NLOS publication with independently verified metadata later than 22 July 2026 was found in this pass. The newest date-verified direct publication remains *Iterating the transient light transport matrix for non-line-of-sight imaging* (Nature Communications, published online 22 July 2026).

The keyword, final-venue, and core-paper citation-tracing pass identified two relevant consistency gaps.

## 1. Neural Illumination Fields

**Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce non-line-of-sight imaging**  
Jingyuan Zhang, Bochao Zhang, Zijin Wang, Chao Qu, Lianfa Bai, Xiaoyu Chen, Jing Han, Baohui Guo  
*Optics and Lasers in Engineering* 198, 109514, March 2026  
DOI: `10.1016/j.optlaseng.2025.109514`

This paper is already cited and discussed in `article/5newscenes.tex` under the two-bounce NLOS trajectory, and its stable key `zhangNeuralIlluminationFields2026` already exists in the consolidated bibliography. It is nevertheless absent from `README.md`, the website paper explorer, and the public timeline.

Contribution summary: NIF parameterizes continuous hidden density and illumination-dependent intensity with MLPs, synthesizes measured shadow images through differentiable rendering, removes error-prone binary shadow segmentation, reports 1 cm resolution within a 144 m³ hidden volume, and remains effective under low shadow contrast and ambient illumination interference.

Required insertion locations:

- `README.md`: add a Latest Additions row; add a 2026 milestone immediately before the D-NeSF milestone to make the static-to-dynamic neural-shadow progression explicit.
- `index.html`: add an explorer object categorized as active / two-bounce / neural implicit; add the corresponding historical-development sentence before D-NeSF.
- `article/5newscenes.tex`: retain the existing semantically placed paragraph and citation; do not duplicate it.
- `egbib_merged_20260711.bib`: preserve the stable key and normalize the final-venue metadata in place.

## 2. SCISA-Net

**SCISA-Net: Scene-Constrained Inverse-to-Subband Attention for Semantic Inference from Wall-Mediated Indirect Observations**  
Jihao Dai, Hongshuai Qin, Guowen Li, Jin Liu, Xiaoshuai Zhang, Huiyu Qi, Zhiwen Zheng, Xingru Huang  
*Photonics* 13(6), 575, published 11 June 2026  
DOI: `10.3390/photonics13060575`

This paper is absent from the current README, website, survey source, and consolidated bibliography. It qualifies as tightly scoped NLOS semantic sensing rather than generic image classification: the hidden display remains outside the camera field of view, while inference uses only a calibrated wall-mediated indirect observation.

Contribution summary: scene-aware regularized inverse encoding reorganizes weak indirect class evidence, and multi-stage Haar-subband attention preserves discriminative mid/high-frequency cues. Experiments use a paired 31-class benchmark and test attenuation, ambient-background interference, and matched scene-operator re-parameterization. The paper performs category-level semantic inference, not complete hidden-image, depth, or geometry reconstruction, and should be labeled accordingly.

Required insertion locations:

- `README.md`: add a Latest Additions row and a 2026 semantic-NLOS milestone immediately after QSS-Net.
- `index.html`: add an explorer object categorized as learning / recognition / semantic NLOS; link it to the recognition-and-clustering development trajectory.
- `article/4datadriven.tex`: insert a short paragraph titled **Calibrated wall-mediated semantic inference** immediately after the paragraph ending with recognition, action understanding, and clustering as a parallel trajectory to reconstruction.
- `egbib_merged_20260711.bib`: add the canonical `daiSCISANet2026` entry from `egbib_20260725_nif_scisa.bib`.

## Guarded integration assets

The repository contains:

- `scripts/sync_nlos_20260725_nif_scisa.py`, an idempotent fail-closed synchronizer accepting the known 201-entry state, a possible NIF-only 202-entry intermediate state, or the final 203-entry state;
- `.github/workflows/sync_nlos_neural_illumination_20260725.yml`, which validates titles, DOIs, stable citation keys, semantic placement, bibliography resolution, LaTeX compilation, PDF text, and every rendered PDF page;
- `egbib_20260725_nif_scisa.bib`, the DOI-verified metadata supplement.

## Status and remaining work

At the final check for this run, `README.md` still showed the 24 July 2026 snapshot and neither public paper row had been merged. Therefore the public artifacts, consolidated bibliography, and `bare_jrnl.pdf` are **not claimed as updated** in this note.

The guarded workflow is configured to perform the source integration, merge the bibliography records, run `pdflatex → bibtex → pdflatex ×2`, validate the generated bibliography and PDF, and commit the regenerated binary. Until a subsequent integration commit is visible, this file is the authoritative patch-style record of what remains to merge and compile.
