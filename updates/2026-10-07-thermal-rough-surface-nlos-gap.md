# 2026-10-07 verified gap: Thermal NLOS through rough surfaces

## Canonical paper
Ruilin Ye, Yijun Zhou, Jianwei Zeng, Chen Dai, Wenqing Hong, Wenwen Li, Jun Zhao, Feihu Xu, "Thermal Non-Line-of-Sight Imaging through Rough Surfaces," ACM Transactions on Graphics, 45(5), Article 173, 1–21, 2026. DOI: 10.1145/3811030.

Published online 29 June 2026; accepted 14 April 2026. ACM issued an erratum on 25 August 2026 and updated the version of record on 27 August 2026; use the corrected record.

## Why it belongs
NLOSFormer embeds a convolutional thermal light-transport model into a dual-branch neural reconstruction network, explicitly estimates the transport kernel, introduces the ThermalNLOS dataset, generalizes across rough relay walls, supports relative depth estimation, and demonstrates dynamic thermal NLOS at about 4 fps. This is a major bridge between passive thermal NLOS, physics-embedded learning, rough-surface generalization, and real-time reconstruction.

## Canonical integration
- README.md: add to Latest Additions and the thermal/passive or new-modalities timeline.
- index.html / paper explorer: add venue, DOI, thermal/passive tags, rough-surface and physics-embedded-learning tags.
- bare_jrnl.tex: integrate semantically in the passive/thermal NLOS discussion, contrasting earlier reflective-wall thermal/light-field methods with rough-wall physics-embedded reconstruction.
- bibliography: add the BibTeX below.
- Rebuild bare_jrnl.pdf after source integration and verify all public artifacts agree.

## BibTeX staging
@article{ye2026thermalrough,
  title={Thermal Non-Line-of-Sight Imaging through Rough Surfaces},
  author={Ye, Ruilin and Zhou, Yijun and Zeng, Jianwei and Dai, Chen and Hong, Wenqing and Li, Wenwen and Zhao, Jun and Xu, Feihu},
  journal={ACM Transactions on Graphics},
  volume={45},
  number={5},
  pages={1--21},
  articleno={173},
  year={2026},
  doi={10.1145/3811030}
}

## Other verified missing candidates from this pass
The default branch also returned no exact-title hit for "Stereo Non-Line-of-Sight Imaging" (The Visual Computer 42, 148, 2026; DOI 10.1007/s00371-025-04340-7) and "Forward and inverse diffraction in phasor fields" (Optics Express 33(5), 11420–11441, 2025; DOI 10.1364/OE.553755). These are relevant follow-up candidates for canonical integration after duplicate/section-level review. A lower-priority arXiv-only candidate is "Non-Line-of-Sight imaging using raster scanning at NIR wavelength" (arXiv:2607.04183).
