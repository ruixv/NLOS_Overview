# 2026-07-09 Pathfinder + Keyhole NLOS README Sync

## Search result

Fresh keyword search and citation-tracing-style checks did not surface a new high-confidence July 2026 frontier NLOS imaging paper beyond the already tracked 2026 items such as 3D Gaussian Transient Rendering, consumer-LiDAR NLOS, DENALI, and GeRaF 2.0.

This run instead completed a public README sync for two previously identified but not yet surfaced missing entries:

1. **PathFinder: Attention-Driven Dynamic Non-Line-of-Sight Tracking with a Mobile Robot** — Kannapiran, Chandran, Jayasuriya, Berman, **arXiv 2024**.
   - Relevance: passive/ordinary-RGB dynamic NLOS tracking from a mobile robot or drone.
   - Metadata status: arXiv verified; no final venue page verified in this run.

2. **Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path** — Metzler, Lindell, Wetzstein, **arXiv 2019**.
   - Relevance: active transient NLOS imaging/tracking from a single optical path, using hidden-object motion and EM/unknown-view tomography to recover shape and trajectory.
   - Metadata status: arXiv verified; no final venue page verified in this run.

## Repository updates made

### README.md

Updated directly in this run.

- Changed the latest-additions date to **9 July 2026**.
- Added PathFinder to the 2024 block.
- Added Keyhole Imaging to the 2019 block.

Commit:

- `0e478b2ca98aeadffd37fefba0ff9ccad0dc8356`

## Remaining public-surface consistency work

### index.html

`index.html` was not whole-file overwritten because it is a compact hand-maintained HTML/JS file with long single-line objects; accidental truncation or escaping damage would break the paper explorer. The exact patch is:

1. Replace:

```html
Updated 7 July 2026 · 190+ papers
```

with:

```html
Updated 9 July 2026 · 190+ papers
```

2. Replace:

```html
<b>65</b><span>tracked latest entries</span>
```

with:

```html
<b>71</b><span>tracked latest entries</span>
```

3. Replace footer text:

```html
Last updated: 7 July 2026
```

with:

```html
Last updated: 9 July 2026
```

4. Insert the following paper objects into the `const papers=[...]` list:

```js
{cat:"latest learning active",title:"Self-Calibrating, Fully Differentiable NLOS Inverse Rendering",authors:"Choi et al.",year:2023,venue:"arXiv 2023",url:"https://arxiv.org/abs/2309.12047",key:"Differentiable transient rendering with imaging-parameter self-calibration for NLOS inverse rendering."},
{cat:"latest dataset active",title:"Differentiable Transient Rendering",authors:"Yi et al.",year:2022,venue:"arXiv 2022",url:"https://arxiv.org/abs/2206.06193",key:"Differentiable transient path-integral framework supporting NLOS tracking with non-planar relay walls and two-corner settings."},
{cat:"latest active",title:"Automatic calibration of time of flight based non-line-of-sight reconstruction",authors:"Sadhu et al.",year:2021,venue:"arXiv 2021",url:"https://arxiv.org/abs/2105.10603",key:"Jointly optimizes hidden albedo and virtual scan positions to make ToF NLOS reconstruction robust to calibration error."},
{cat:"latest passive modality learning",title:"PathFinder: Attention-Driven Dynamic Non-Line-of-Sight Tracking with a Mobile Robot",authors:"Kannapiran et al.",year:2024,venue:"arXiv 2024",url:"https://arxiv.org/abs/2404.05024",key:"Moving RGB camera on a small robot/drone plus attention-based temporal inference for hidden-person trajectory tracking."},
{cat:"latest active",title:"Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path",authors:"Metzler et al.",year:2019,venue:"arXiv 2019",url:"https://arxiv.org/abs/1912.06727",key:"Single-optical-path transient NLOS imaging/tracking using hidden-object motion and EM/unknown-view tomography."},
{cat:"latest active learning",title:"Direct Object Recognition Without Line-of-Sight Using Optical Coherence",authors:"Lei et al.",year:2019,venue:"arXiv 2019",url:"https://arxiv.org/abs/1903.07705",key:"Coherent illumination and diffuse-wall speckle patterns with a neural recognizer for direct hidden-object recognition."},
```

### bare_jrnl.tex

`bare_jrnl.tex` still uses only:

```tex
\bibliography{egbib}
```

It should be changed to:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates,egbib_20260707_updates,egbib_20260708_updates}
```

Suggested narrative integration:

- `article/2active.tex`: add `\cite{metzlerKeyholeImaging2019}` to the pulsed-laser/SPAD detection-tracking row, or add a short sentence near the sparse/acquisition discussion: Keyhole imaging showed that active NLOS can be posed with only a single optical path when hidden-object motion provides the missing angular diversity.
- `article/5newscenes.tex`: add `\cite{kannapiranPathFinder2024}` to the robotic / mobile-camera NLOS paragraph, noting that PathFinder uses ordinary RGB video from a moving robot or drone to choose useful relay planes and track hidden people in the wild.

### Bibliography

`egbib_20260708_updates.bib` already contains:

- `kannapiranPathFinder2024`
- `metzlerKeyholeImaging2019`

### PDF

`bare_jrnl.pdf` was not regenerated in this run. Remaining steps:

```bash
pdflatex bare_jrnl.tex
bibtex bare_jrnl
pdflatex bare_jrnl.tex
pdflatex bare_jrnl.tex
```

Then upload/commit the regenerated `bare_jrnl.pdf`.
