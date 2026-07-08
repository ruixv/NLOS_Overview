# 2026-07-08 homepage and survey consistency gap update

## Search outcome

This run repeated fresh keyword search plus citation-tracing style checks around the core active/transient NLOS line (Velten 2012, O'Toole 2018 LCT, Lindell 2019 f-k, Liu phasor-field / virtual-wave, NeTF / transformer / transient-rendering descendants) and the modality-expansion line (consumer LiDAR, RF/mmWave/RIS, acoustic, THz, event-camera, and differentiable transient rendering).

No new high-confidence July 2026 frontier NLOS imaging paper was found beyond the current README frontier set. Fresh searches continued to return already covered 2026 entries such as 3D Gaussian Transient Rendering, consumer-LiDAR NLOS, DENALI, and GeRaF 2.0.

## Consistency issue found

README.md is now ahead of index.html by four latest-addition objects. The homepage still says `Updated 7 July 2026` and `65 tracked latest entries`, while README.md says `Update run: 8 July 2026` and includes four latest entries not yet represented in the homepage paper explorer.

The missing homepage objects are:

1. `Automatic calibration of time of flight based non-line-of-sight reconstruction` — Sadhu et al., arXiv 2021.
2. `Differentiable Transient Rendering` — Yi et al., arXiv 2022.
3. `Self-Calibrating, Fully Differentiable NLOS Inverse Rendering` — Choi et al., arXiv 2023.
4. `Direct Object Recognition Without Line-of-Sight Using Optical Coherence` — Lei et al., arXiv 2019.

The correct homepage latest-entry count after adding these four objects is `69`.

## Exact index.html patch

Change the hero/footer date and latest-entry count:

```html
Updated 8 July 2026 · 190+ papers
```

```html
<div class="stat"><b>69</b><span>tracked latest entries</span></div>
```

```html
Last updated: 8 July 2026
```

Insert the following objects into `const papers=[ ... ]` in chronological order among the existing latest entries:

```javascript
      {cat:"latest learning active",title:"Self-Calibrating, Fully Differentiable NLOS Inverse Rendering",authors:"Choi et al.",year:2023,venue:"arXiv 2023",url:"https://arxiv.org/abs/2309.12047",key:"Self-calibrates imaging parameters by coupling diffraction-based NLOS reconstruction with differentiable transient rendering."},
      {cat:"latest dataset active",title:"Differentiable Transient Rendering",authors:"Yi et al.",year:2022,venue:"arXiv 2022",url:"https://arxiv.org/abs/2206.06193",key:"Differentiable transient path-integral framework supporting non-planar relay walls and two-corner NLOS tracking."},
      {cat:"latest active",title:"Automatic calibration of time of flight based non-line-of-sight reconstruction",authors:"Sadhu et al.",year:2021,venue:"arXiv 2021",url:"https://arxiv.org/abs/2105.10603",key:"Differentiable ToF NLOS forward model jointly optimizes hidden albedo and virtual scan positions under miscalibration."},
      {cat:"latest active learning",title:"Direct Object Recognition Without Line-of-Sight Using Optical Coherence",authors:"Lei et al.",year:2019,venue:"arXiv 2019",url:"https://arxiv.org/abs/1903.07705",key:"Coherent illumination produces diffuse-wall speckle patterns used by a neural network for direct hidden-object recognition."},
```

Suggested insertion anchors:

- Insert Choi et al. immediately before `Non-line-of-sight imaging in the presence of scattering media using phasor fields`.
- Insert Yi et al. immediately before `Occlusion Fields: An Implicit Representation for Non-Line-of-Sight Surface Reconstruction`.
- Insert Sadhu et al. immediately before `Non-line-of-sight imaging with picosecond temporal resolution`.
- Insert Lei et al. immediately before `Non-line-of-sight 3D imaging with a single-pixel camera`.

## Survey-source patch

The bibliography supplement `egbib_20260708_updates.bib` already contains:

- `sadhuAutomaticCalibrationToFNLOS2021`
- `yiDifferentiableTransientRendering2022`
- `choiSelfCalibratingDifferentiableNLOS2023`

`egbib_20260707_updates.bib` already contains:

- `leiDirectObjectRecognition2019`

However, `bare_jrnl.tex` still uses only:

```tex
\bibliography{egbib}
```

Change it to:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates,egbib_20260707_updates,egbib_20260708_updates}
```

Then integrate the three differentiable inverse-rendering/calibration papers into `article/4datadriven.tex` near the physics-constrained learning / rendering-tool discussion. A concise style-preserving paragraph is:

```tex
\vspace{0.8mm}
\noindent \textbf{Differentiable inverse rendering and self-calibration.}
A related direction is to make the NLOS forward model differentiable not only with respect to the hidden scene, but also with respect to nuisance imaging parameters. Sadhu \etal~jointly optimized hidden albedo and virtual illumination/detection positions to automatically calibrate ToF-based NLOS reconstruction under relay-wall miscalibration~\cite{sadhuAutomaticCalibrationToFNLOS2021}. Yi \etal~introduced differentiable transient rendering~\cite{yiDifferentiableTransientRendering2022}, providing a path-integral framework for gradient-based optimization in transient scenes, including non-planar relay walls and two-corner NLOS tracking. Building on this idea, Choi \etal~proposed a fully differentiable NLOS inverse-rendering pipeline that couples diffraction-based volumetric reconstruction, differentiable transient rendering, and self-calibration of imaging parameters~\cite{choiSelfCalibratingDifferentiableNLOS2023}. These works shift part of the field from fixed analytic inversion toward end-to-end optimization over both hidden geometry and capture parameters.
```

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The remaining build sequence is still:

```bash
pdflatex bare_jrnl.tex
bibtex bare_jrnl
pdflatex bare_jrnl.tex
pdflatex bare_jrnl.tex
```

Only after the bibliography line is updated and the TeX source compiles should `bare_jrnl.pdf` be replaced.

## Files intentionally not overwritten

I did not overwrite `index.html`, `bare_jrnl.tex`, or `article/4datadriven.tex` in this run because the available GitHub write action requires whole-file replacement. `index.html` is a compact hand-maintained HTML/JS file, and replacing it without a reliable patch-level operation risks truncating or damaging the paper explorer. The exact safe patch is recorded above instead.
