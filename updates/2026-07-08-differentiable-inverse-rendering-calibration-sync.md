# 2026-07-08 differentiable inverse-rendering / calibration NLOS sync

## Search pass summary

Fresh keyword searches and citation-tracing-style queries around LCT, f-k migration, phasor-field / virtual-wave NLOS, NeTF, differentiable transient rendering, and 3D Gaussian Transient Rendering did not reveal a newer high-confidence July 2026 frontier paper beyond the current README items: arbitrary-relay 3D Gaussian Transient Rendering, consumer-LiDAR NLOS, GeRaF 2.0 / RF NLOS reconstruction, low-cost-LiDAR datasets, RIS-assisted radar sensing, and distributed MIMO/ISAC entries.

The useful gap found in this run is a differentiable inverse-rendering / self-calibration thread that is directly relevant to recent 2026 arbitrary-relay Gaussian transient rendering but was not surfaced in the public README snapshot.

## Newly surfaced papers

1. **Automatic calibration of time of flight based non-line-of-sight reconstruction** — Sadhu et al., arXiv 2021.  
   Link: https://arxiv.org/abs/2105.10603  
   Relevance: ToF NLOS reconstruction usually assumes calibrated relay-wall scan positions; this work jointly optimizes hidden albedo and virtual illumination/detection positions using a differentiable forward model.

2. **Differentiable Transient Rendering** — Yi et al., arXiv 2022.  
   Link: https://arxiv.org/abs/2206.06193  
   Relevance: not a standalone NLOS reconstruction benchmark, but a tightly adjacent transient-rendering foundation that explicitly demonstrates NLOS tracking with non-planar relay walls and two-corner NLOS settings; it helps explain the trajectory toward later differentiable NLOS inverse rendering and Gaussian transient rendering.

3. **Self-Calibrating, Fully Differentiable NLOS Inverse Rendering** — Choi et al., arXiv 2023.  
   Link: https://arxiv.org/abs/2309.12047  
   Relevance: couples diffraction-based volumetric NLOS reconstruction with differentiable transient rendering and optimizes imaging parameters directly from measured transients.

Venue decision: no stable final conference/journal pages or DOI metadata were verified in this run, so all three are labeled by arXiv status.

## Repository changes made

- Added `egbib_20260708_updates.bib` with BibTeX keys:
  - `sadhuAutomaticCalibrationToFNLOS2021`
  - `yiDifferentiableTransientRendering2022`
  - `choiSelfCalibratingDifferentiableNLOS2023`
- Updated `README.md` to 8 July 2026 and surfaced the three papers in the timeline-ordered Latest Additions table.

## Remaining website patch

`index.html` still needs a safe patch rather than a blind whole-file rewrite. The homepage latest-entry count should be changed from `65` to `67`, and the following paper objects should be inserted into the `papers` array. The count is 67 because the homepage was also missing the previously integrated Lei et al. optical-coherence recognition entry while README already includes it.

```js
      {cat:"latest learning active",title:"Self-Calibrating, Fully Differentiable NLOS Inverse Rendering",authors:"Choi et al.",year:2023,venue:"arXiv 2023",url:"https://arxiv.org/abs/2309.12047",key:"Self-calibrating differentiable NLOS inverse rendering that optimizes hidden geometry and imaging parameters from measured transients."},
      {cat:"latest dataset active",title:"Differentiable Transient Rendering",authors:"Yi et al.",year:2022,venue:"arXiv 2022",url:"https://arxiv.org/abs/2206.06193",key:"Differentiable transient path-integral framework supporting NLOS tracking with non-planar relay walls and two-corner NLOS settings."},
      {cat:"latest active",title:"Automatic calibration of time of flight based non-line-of-sight reconstruction",authors:"Sadhu et al.",year:2021,venue:"arXiv 2021",url:"https://arxiv.org/abs/2105.10603",key:"Jointly optimizes hidden albedo and virtual scan positions to make ToF NLOS reconstruction robust to calibration error."},
      {cat:"latest learning active",title:"Direct Object Recognition Without Line-of-Sight Using Optical Coherence",authors:"Lei et al.",year:2019,venue:"arXiv 2019",url:"https://arxiv.org/abs/1903.07705",key:"Coherent illumination and diffuse-wall speckle patterns with a neural classifier for direct hidden-object recognition."},
```

Suggested placement: the Choi object before the 2023 Luesia phasor-field scattering-media entry, the Yi object before the 2022 Occlusion Fields entry, the Sadhu object before the 2021 picosecond-temporal-resolution entry, and the Lei object between Starshynov 2019 and Musarra 2019.

## Remaining survey-source patch

`article/4datadriven.tex` should receive a short paragraph in the physics-constrained / differentiable-rendering part of the deep-learning section, for example after the existing untrained-network-priors paragraph:

```tex
\vspace{0.8mm}
\noindent \textbf{Differentiable inverse rendering and self-calibration.}
A complementary direction makes the NLOS forward model differentiable not only with respect to the hidden albedo or geometry, but also with respect to nuisance imaging parameters. Sadhu~\etal~jointly optimized the hidden albedo and virtual illumination/detection positions to automatically calibrate ToF-based NLOS reconstruction under scan-position errors~\cite{sadhuAutomaticCalibrationToFNLOS2021}. Yi~\etal~introduced differentiable transient rendering for time-resolved light transport, including NLOS tracking with non-planar relay walls and two-corner settings~\cite{yiDifferentiableTransientRendering2022}. Building on this trajectory, Choi~\etal~formulated a self-calibrating NLOS inverse-rendering pipeline that couples diffraction-based volumetric reconstruction with differentiable transient rendering and optimizes imaging parameters directly from measured transients~\cite{choiSelfCalibratingDifferentiableNLOS2023}. These works help connect classic physical inversion to the recent wave of differentiable-rendering and Gaussian-based NLOS methods.
```

`bare_jrnl.tex` should also change its bibliography line to:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates,egbib_20260707_updates,egbib_20260708_updates}
```

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The current GitHub connector can safely write UTF-8 text files, but the PDF is a binary artifact and the available write path does not provide a safe binary upload/replace operation. After applying the TeX patch above, compile locally with LaTeX/BibTeX and upload the regenerated PDF.
