# 2026-09-12 — SCCLM deformable-object NLOS tracking integration

## Verified missing paper

Aiping Zhai, Wenjing Ji, Yan Wang, Xiyuan Luo, Wenjing Zhao, Dong Wang, and Fei Liu, **“Non-Invasively Tracking an Arbitrary Deformable Object Through Scattering Media and Around Corners via Speckle Correlations,”** *Advanced Science*, vol. 13, no. 34, e75072, 2026. DOI: 10.1002/advs.75072.

The publisher record and PubMed metadata confirm the final venue, volume/issue, article number, DOI, and author list. The paper explicitly includes an around-corner NLOS experiment, not only through-scattering-media experiments. Its SCCLM method estimates hidden-target displacement by the centroids of speckle autocorrelation and cross-correlation rather than correlation peaks, allowing tracking when the hidden object translates while rotating, scaling, stretching, or changing shape. In the around-corner experiment, wall-mediated speckle observations recover the trajectory of the hidden moving deformable object; the paper reports repeated experiments with error bars below 2.5 pixels across tested scenarios.

## Why it belongs in this repository

This is a genuine passive NLOS tracking contribution. It extends the speckle-correlation branch from static image reconstruction and rigid-object tracking to **prior-free tracking of deformable hidden objects**, including an explicit around-corner geometry. It is therefore tightly connected to the repository’s passive-speckle, tracking, and semantic-sensing lineages.

Suggested development trajectory:

> passive speckle reconstruction → passive joint imaging/localization → hidden-object tracking → deformation-robust / prior-free NLOS tracking

## Required cross-artifact integration

### README.md

Add to **Latest Additions** (2026):

> [Non-Invasively Tracking an Arbitrary Deformable Object Through Scattering Media and Around Corners via Speckle Correlations](https://doi.org/10.1002/advs.75072) — Zhai et al. | *Advanced Science* 13(34), e75072 (2026) | Introduces speckle-correlation centroid localization (SCCLM) for prior-free tracking of hidden deformable objects. By using centroids of speckle auto/cross-correlations rather than correlation peaks, it remains valid under translation with rotation, scaling, stretching, or shape changes, and is experimentally demonstrated in an around-corner NLOS setup.

Also place the paper in the passive NLOS / detection-tracking timeline near existing passive speckle localization/tracking works.

### article/3passive.tex

Insert after the existing **Joint passive imaging and localization from speckle** discussion (or the nearest passive tracking paragraph):

```tex
\vspace{0.8mm}
\noindent \textbf{Deformation-robust passive speckle tracking.}
Speckle-correlation NLOS tracking often assumes that the hidden target preserves its appearance so that the peak of the cross-correlation remains a stable displacement cue. Zhai~\etal~instead localize the centroid of the speckle auto- and cross-correlation functions and show that this centroid displacement tracks the hidden object's motion even when its projected shape changes through rotation, scaling, stretching, or more general deformation~\cite{zhaiSCCLMAroundCorner2026}. Their speckle-correlation centroid localization method requires no target template or calibrated point-spread function and is experimentally validated not only through static and dynamic scattering media but also in an explicit around-corner configuration. This extends passive speckle sensing from static reconstruction and rigid-object localization toward prior-free tracking of deformable hidden targets.
```

If the passive summary table has a detection/tracking row, add `zhaiSCCLMAroundCorner2026` there as an ordinary-camera / speckle-correlation / tracking entry.

### Canonical bibliography

Merge the verified entry from `egbib_20260912_scc_speckle_tracking.bib` into the bibliography actually used by `bare_jrnl.tex` (`egbib_merged_20260711.bib` at the time of this audit). Avoid duplicate DOI/key entries.

### Website / Paper Explorer

Add the paper to the passive-NLOS tracking/speckle category in `index.html` and/or the repository’s generated paper-source data. Use the final *Advanced Science* venue rather than a preprint label.

### PDF

After the canonical bibliography and LaTeX prose are integrated, rebuild `bare_jrnl.pdf` and verify that `zhaiSCCLMAroundCorner2026` resolves without an undefined citation.

## Safety / consistency note

The large public artifacts were not overwritten from truncated connector responses. This patch note and the verified standalone BibTeX are the safe staging artifacts for a later complete-file integration when the full file content can be read without truncation.
