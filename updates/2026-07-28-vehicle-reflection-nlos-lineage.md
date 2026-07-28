# Vehicle-reflection passive NLOS lineage — 28 July 2026

## Verified missing works

Repository-wide title, DOI, README, website, survey-source, and bibliography searches found a coherent automotive passive/specular NLOS lineage that is not yet represented in the public artifacts.

1. **NLOS Obstacle Position Estimation from Reflected Image** — Yusuke Takatori, IEEE Intelligent Vehicles Symposium 2020, pp. 1265–1270, DOI `10.1109/IV47402.2020.9304553`.
   - Uses a stereo camera to estimate the virtual image of a road obstacle reflected by a nearby vehicle or roadside glass and geometrically recover the hidden obstacle position.
   - This is passive/specular NLOS localization, not complete hidden-scene reconstruction.

2. **Estimation of NLOS Obstacle Position Using Reflected Image on Transparent Surface** — Sakuma Nakamura and Yusuke Takatori, IEEE ITSC 2022, pp. 1656–1661, IEEE Xplore document 9922107.
   - Extends the reflected-image localization formulation to transparent relay surfaces, explicitly addressing stereo parallax, incidence angle, and polarization-filter effects.
   - A final DOI was not independently exposed by the scholarly indexes available in this run, so the canonical BibTeX intentionally retains the verified IEEE Xplore URL without inventing a DOI.

3. **Object Detection Method for Non-Line-of-Sight Obstacles Reflected on Painted Surfaces** — Rei Oyama and Yusuke Takatori, IEEE ITSC 2025, pp. 783–788, DOI `10.1109/ITSC60802.2025.11423754`.
   - Moves the trajectory from geometric localization toward semantic obstacle detection in weak, color-distorted reflections on painted vehicle surfaces.
   - The paper compares training on real/pseudo reflection images with converting reflected observations toward a direct-view appearance before applying a general pretrained detector; the latter reports 85.7% overall accuracy.

4. **Feasibility study of non-line-of-sight obstacle location estimation using reflected images from in-vehicle sensors** — Baili Sheng and Yusuke Takatori, IATSS Research 50(1), 777–785, 2026, DOI `10.1016/j.iatssr.2026.02.007`.
   - Provides the most complete validation of the lineage: real-road reflection-frequency observations, microscopic traffic simulation, reflective-surface-angle modeling, and 1/6-scale localization experiments.
   - The reported mean error is 4.3 cm for targets 1.7–3.7 m from the camera; the RMS error remains approximately 45 mm under reflective-surface orientation changes.

These works are tightly adjacent NLOS sensing rather than incidental uses of the acronym: they deliberately use hidden-object virtual images formed by opportunistic specular surfaces to recover position or semantic identity beyond the ego vehicle’s direct field of view.

## Required public-artifact integration

### README.md

Insert the four records in `Latest Additions`, using the categorization **Passive / specular / automotive localization and recognition**. The concise timeline should explain the trajectory:

- 2020: stereo virtual-image geometry for reflected-obstacle localization;
- 2022: transparent-surface extension;
- 2025: detection from painted-surface reflections;
- 2026: road-availability and scale/angle robustness validation.

The 2026 IATSS record should be placed next to the existing VISAPP vehicle-body-reflection paper by Kozawa et al. to distinguish two related but different formulations: opportunistic vehicle-body mirrors for hidden-human localization versus stereo unfolding of virtual road-obstacle images.

### index.html

Add four searchable explorer objects with tags such as `passive`, `specular`, `automotive`, `reflection`, `stereo`, `localization`, and `recognition`. Recompute the displayed tracked-entry count from the actual JavaScript paper-object array rather than hard-coding an assumed value. Add short timeline sentences in 2020, 2022, 2025, and 2026.

### article/3passive.tex

Add a compact subsection immediately after the current paragraph on `Estimating the 3D Position of Hidden Humans Using Reflections on Vehicle Bodies`:

```latex
\vspace{0.8mm}
\noindent \textbf{Vehicle-body reflections as opportunistic automotive NLOS sensors.}
Takatori first used stereo observations of virtual obstacle images reflected by neighboring vehicles or roadside glass to geometrically recover hidden road-obstacle positions~\cite{takatoriReflectedImageNLOS2020}. Nakamura and Takatori extended the formulation to transparent relay surfaces, analyzing stereo parallax, incidence angle, and polarization filtering~\cite{nakamuraTransparentReflectionNLOS2022}. Oyama and Takatori subsequently moved from localization toward semantic detection on weak and color-distorted painted-surface reflections, combining pseudo-reflection augmentation with direct-view normalization and pretrained object detectors~\cite{oyamaPaintedReflectionDetection2025}. Sheng and Takatori then evaluated reflection availability in real traffic and microscopic simulation and validated stereo virtual-image unfolding across reflector orientations~\cite{shengVehicleReflectionObstacle2026}. Together, these studies establish an application-facing passive/specular NLOS branch for intelligent transportation; their outputs are obstacle position or identity rather than hidden appearance or complete geometry.
```

Where the passive-method summary table has room, add one lineage row rather than four near-duplicate rows.

### Bibliography

Merge `egbib_20260728_vehicle_reflection_lineage.bib` into the consolidated bibliography with DOI/key deduplication. Preserve the four citation keys in that file. Do not add an unverified DOI to the 2022 ITSC record.

### bare_jrnl.tex and PDF

Add a trace marker near the existing July 2026 integration comments, compile with the repository’s standard `pdflatex -> bibtex -> pdflatex -> pdflatex` sequence, and regenerate `bare_jrnl.pdf` only after all four citation keys resolve.

## Validation checklist

- Each title appears exactly once in README and website explorer.
- Each DOI appears exactly once in README, website, and consolidated BibTeX; the 2022 record is validated by title, pages, and IEEE Xplore URL.
- All four keys occur in `article/3passive.tex` and the generated `.bbl`.
- The website tracked-entry count equals the number of paper objects.
- The extracted PDF text contains the new subsection heading and all four bibliography records.
- First and last PDF pages render without clipping, missing glyphs, or unresolved citation markers.

## Current repository state

README, the website explorer and timeline, passive-survey prose, and the consolidated bibliography are now synchronized for all four records. `bare_jrnl.pdf` was rebuilt after all four automotive vehicle-reflection citation keys resolved.
