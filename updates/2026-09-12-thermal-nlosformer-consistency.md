# 2026-09-12 Thermal NLOSFormer consistency update

## Verified paper

- Ruilin Ye, Yijun Zhou, Jianwei Zeng, Chen Dai, Wenqing Hong, Wenwen Li, Jun Zhao, Feihu Xu, **Thermal Non-Line-of-Sight Imaging through Rough Surfaces**, *ACM Transactions on Graphics*, 45(5), Article 173, pp. 1–21, 2026. DOI: 10.1145/3811030.
- ACM publication history: accepted 14 Apr 2026, online 19 May 2026, published 29 Jun 2026; corrected version posted 27 Aug 2026.
- Public code/data: https://github.com/yeruilin/NLOSFormer

## Why it belongs in the survey

This is a direct passive thermal NLOS reconstruction paper, not merely adjacent thermal sensing. It introduces NLOSFormer, a physics-embedded transformer-style network that models relay-wall transport as convolution, estimates the transport kernel from the thermal measurement, and uses that kernel to constrain hidden-scene reconstruction. The paper also releases ThermalNLOS and demonstrates generalization across rough relay materials, relative-depth estimation, and dynamic reconstruction at 4 fps.

The field trajectory is:

`passive thermal localization / specular-diffuse inversion -> learned thermal reconstruction -> rough-wall physics-embedded thermal reconstruction + public dataset`

## Current repository state checked in this run

- `README.md` already contains a 2026 entry for this paper, so do **not** duplicate it there.
- `article/5newscenes.tex` currently discusses passive THz/LWIR work and many emerging modalities but does not yet contain NLOSFormer / ThermalNLOS.
- GitHub code search did not find DOI `10.1145/3811030` or `NLOSFormer` in the canonical bibliography/survey source; a verified BibTeX staging file is added in this update.
- The public website search did not surface this paper, so `index.html` / paper explorer should be checked and synchronized.

## Required integration locations

### `article/5newscenes.tex`

Insert a short paragraph in the passive thermal / emerging modality discussion (or immediately before the Terahertz subsection if no dedicated thermal subsection exists):

> **Physics-embedded thermal NLOS through rough relay surfaces.** Ye et al. extend passive thermal NLOS from localization and relatively reflective relay materials to learned reconstruction through substantially rougher walls. NLOSFormer models wall-mediated thermal transport as a convolution, predicts the corresponding transport kernel jointly with the hidden image, and uses the kernel as a physical constraint on reconstruction. Their ThermalNLOS dataset and experiments across metal, tabletop, cardboard, and foam relay surfaces show improved cross-surface generalization, relative-depth estimation from kernel scale, and dynamic hidden-target reconstruction at 4 fps. This work shifts thermal NLOS toward detector- and material-aware learned inversion under realistic rough-wall scattering rather than assuming an optically favorable relay surface. `\cite{yeThermalNLOSFormer2026}`

### Canonical bibliography

Merge `egbib_20260912_thermal_nlosformer.bib` into the bibliography actually used by `bare_jrnl.tex` (currently `egbib_merged_20260711.bib` in recent runs), preserving key `yeThermalNLOSFormer2026`.

### Website / paper explorer

Ensure the paper appears under 2026 and is tagged at least:

- Passive NLOS
- Thermal / infrared
- Learned reconstruction
- Physics-guided / physics-embedded
- Rough relay surfaces
- Dataset

Suggested one-line summary:

> Physics-embedded thermal NLOS through rough walls: NLOSFormer jointly estimates a wall-transport kernel and hidden image, releases ThermalNLOS, supports relative-depth inference, and demonstrates 4-fps dynamic reconstruction.

### PDF

After the survey source and canonical bibliography are updated, rebuild `bare_jrnl.pdf` and verify that the rendered bibliography shows *ACM Transactions on Graphics*, 45(5), Article 173, pp. 1–21 (2026), DOI 10.1145/3811030.

## Consistency check after integration

The paper should be present in all of: README, website/paper explorer, `article/5newscenes.tex` (and therefore `bare_jrnl.tex`), canonical bibliography, and rebuilt `bare_jrnl.pdf`. If the website is generated from another source file, update that source rather than editing generated HTML alone.
