# NLOS literature integration: 14 October 2026

## Verified publication
Zhou, Jie; Zheng, Zhiwen; Tang, Wenwen; Huang, Xingru; Zhou, Huiyu. "Bounded Hidden-Screen Reconstruction from Diffuse Wall Reflections via Survivability-Guided Representation Learning." Photonics 13(9), 895 (2026). DOI: 10.3390/photonics13090895. Published 21 September 2026.

This work studies passive reconstruction from a single ordinary RGB photograph of a diffuse wall. It combines learned complementary feature paths with observation-conditioned fusion. Its conclusions are limited to coarse structure under controlled indoor conditions; generalization and small-detail reconstruction are not established.

## Integration
README.md: latest additions and 2026 timeline.
data/papers-source.html: Paper Explorer and timeline.
index.html: Core Reading Path.
article/4datadriven.tex: End-to-End algorithms section, using citation key zhouSurvivabilityHiddenScreen2026.
egbib_merged_20260711.bib: publisher metadata.
The main bare_jrnl.tex imports article/4datadriven.tex.

## PDF pending
bare_jrnl.pdf has not been rebuilt. Previous verified blob: 6fc5e00f2a7aee93692f6ee41a7074a4c59de9e6. The current environment cannot clone the complete repository with figures. From a complete checkout, run latexmk -pdf -interaction=nonstopmode -file-line-error bare_jrnl.tex, check logs and references, then commit the regenerated PDF. Do not describe the existing PDF as up-to-date.
