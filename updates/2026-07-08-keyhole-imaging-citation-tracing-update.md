# 2026-07-08 keyhole-imaging citation-tracing update

## Search / tracing result

This run did not identify a newer high-confidence July-2026 frontier NLOS-imaging paper beyond the entries already surfaced in the README, including arbitrary-relay 3D Gaussian Transient Rendering, consumer-LiDAR NLOS, GeRaF 2.0, DENALI, and recent RF/RIS/ISAC additions.

A citation-tracing / core-paper follow-up pass around the Lindell/Wetzstein active NLOS line did identify one direct missing active NLOS paper that was absent from the repository search results for `Keyhole`, `Metzler`, and `1912.06727`:

- **Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path** — Christopher A. Metzler, David B. Lindell, Gordon Wetzstein, **arXiv 2019**. This is a direct active transient NLOS imaging/tracking work. It reduces the relay-wall access requirement by using a single optical path, e.g. through a keyhole, and exploits hidden-object motion to recover shape and trajectory from time-resolved measurements.

No reliable final conference/journal venue page was verified in this run, so the conservative venue label should remain **arXiv 2019**.

## Repository update completed safely

Updated `egbib_20260708_updates.bib` with:

```bibtex
@misc{metzlerKeyholeImaging2019,
  title   = {Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path},
  author  = {Metzler, Christopher A. and Lindell, David B. and Wetzstein, Gordon},
  year    = {2019},
  eprint  = {1912.06727},
  archivePrefix = {arXiv},
  url     = {https://arxiv.org/abs/1912.06727}
}
```

Commit: `c86c29b4f39fce9ee73520d6a277685b1153e60e`.

## README patch still needed

`README.md` is currently updated to 8 July 2026 and already includes Sadhu 2021, Yi 2022, Choi 2023, and Lei 2019. It still needs the previously noted PathFinder row and the newly found Keyhole row.

Insert in the 2024 block, near the other robotic / single-photon-LiDAR entries:

```markdown
| 2024 | [PathFinder: Attention-Driven Dynamic Non-Line-of-Sight Tracking with a Mobile Robot](https://arxiv.org/abs/2404.05024) — Kannapiran et al. | arXiv 2024 | Mobile-robot / drone passive dynamic NLOS tracking: selects useful relay planes from ordinary LOS video and estimates hidden-person 2D trajectories with an attention-based temporal model. |
```

Insert in the 2019 block, near other constrained-acquisition active NLOS works:

```markdown
| 2019 | [Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path](https://arxiv.org/abs/1912.06727) — Metzler et al. | arXiv 2019 | Uses a single optical path, e.g. through a keyhole, and hidden-object motion to recover shape and trajectory from transient measurements when a large relay-wall scan area is unavailable. |
```

## Homepage / `index.html` patch still needed

`index.html` still displays `Updated 7 July 2026` and `65 tracked latest entries`. Relative to the current README + update logs, the homepage is missing six latest-entry objects:

1. Sadhu 2021 automatic ToF NLOS calibration
2. Yi 2022 differentiable transient rendering
3. Choi 2023 self-calibrating differentiable NLOS inverse rendering
4. Lei 2019 optical-coherence recognition
5. PathFinder 2024 mobile-robot passive dynamic NLOS tracking
6. Metzler/Lindell/Wetzstein 2019 Keyhole Imaging

The latest-entry count should therefore be updated from `65` to `71`, and the date should be updated from `7 July 2026` to `8 July 2026` or later.

Recommended objects:

```javascript
{cat:"latest learning active",title:"Self-Calibrating, Fully Differentiable NLOS Inverse Rendering",authors:"Choi et al.",year:2023,venue:"arXiv 2023",url:"https://arxiv.org/abs/2309.12047",key:"Differentiable transient rendering and self-calibration for NLOS inverse rendering from measured transients."},
{cat:"latest learning active",title:"Differentiable Transient Rendering",authors:"Yi et al.",year:2022,venue:"arXiv 2022",url:"https://arxiv.org/abs/2206.06193",key:"Differentiable transient path-integral framework supporting non-planar relay walls and two-corner NLOS tracking."},
{cat:"latest active",title:"Automatic calibration of time of flight based non-line-of-sight reconstruction",authors:"Sadhu et al.",year:2021,venue:"arXiv 2021",url:"https://arxiv.org/abs/2105.10603",key:"Jointly optimizes hidden albedo and virtual scan positions to make ToF NLOS robust to calibration errors."},
{cat:"latest passive learning modality",title:"PathFinder: Attention-Driven Dynamic Non-Line-of-Sight Tracking with a Mobile Robot",authors:"Kannapiran et al.",year:2024,venue:"arXiv 2024",url:"https://arxiv.org/abs/2404.05024",key:"Mobile-robot / drone passive NLOS tracking from ordinary RGB video and attention-based temporal modeling."},
{cat:"latest active",title:"Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path",authors:"Metzler et al.",year:2019,venue:"arXiv 2019",url:"https://arxiv.org/abs/1912.06727",key:"Single-optical-path active transient NLOS imaging and tracking for cases with only keyhole-like relay access."},
{cat:"latest active learning",title:"Direct Object Recognition Without Line-of-Sight Using Optical Coherence",authors:"Lei et al.",year:2019,venue:"arXiv 2019",url:"https://arxiv.org/abs/1903.07705",key:"Coherent illumination and diffuse-wall speckle patterns enable direct hidden-object recognition without full 3D reconstruction."},
```

## Survey-source patch still needed

`article/2active.tex` should include Keyhole Imaging in the active ToF detection/tracking discussion.

Suggested table change:

```latex
\cite{chanNonlineofsightTrackingPeople2017a}(long range),\cite{metzlerKeyholeImaging2019}(single optical path),\cite{caramazzaNeuralNetworkIdentification2017,musarraDetectionIdentificationTracking2019}(single point) & Pulsed laser & SPAD & Time of fight &  Detection/ Tracking/ Identification\\
```

Suggested short paragraph near the discussion of scanning limitations in active transient NLOS:

```latex
Another practical limitation of pulsed SPAD-based NLOS is the need to access and scan a sufficiently large relay-wall area. Keyhole Imaging~\cite{metzlerKeyholeImaging2019} addresses the extreme case where only a single optical path is available, for example through a keyhole. Instead of relying on spatial relay sampling, it exploits hidden-object motion to collect time-resolved projections from varying unknown viewpoints and recovers the hidden object's shape and trajectory. This line complements sparse-scanning and scannerless SPAD-array methods by showing that motion can substitute for aperture diversity when relay access is severely constrained.
```

`article/5newscenes.tex` should also include the previously noted PathFinder robotic passive NLOS paragraph when the survey source is next edited.

## Bibliography / PDF status

`egbib_20260708_updates.bib` now includes `metzlerKeyholeImaging2019` in addition to Sadhu/Yi/Choi/PathFinder. `bare_jrnl.tex` still uses only:

```latex
\bibliography{egbib}
```

For the next survey build, replace it with:

```latex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates,egbib_20260707_updates,egbib_20260708_updates}
```

`bare_jrnl.pdf` was not regenerated in this run. The current execution path can safely update small text files and add patch notes, but full-file replacement of dense hand-maintained `index.html` / LaTeX source files and binary PDF upload should be done only after local verification to avoid truncation or formatting damage.
