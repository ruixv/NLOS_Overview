# 2026-07-09 homepage latest-count sync

## Search result

This run repeated keyword search and forward-citation-style checks around active ToF NLOS, phasor-field/f-k/LCT, neural transient fields, passive NLOS, acoustic/RF/consumer-LiDAR NLOS, differentiable transient rendering, keyhole/single-path NLOS, and mobile-robot NLOS tracking.

No additional high-confidence July 2026 frontier NLOS imaging paper was found beyond the current README/update-log set. Fresh search continued to surface already-covered items such as 3D Gaussian Transient Rendering, consumer-LiDAR NLOS, DENALI, GeRaF 2.0, and the recent ToF NLOS study/review.

## Actual repository update

The main public-facing inconsistency was the homepage. `README.md` was already updated to 9 July 2026 and included the recently completed additions, but `index.html` still showed:

- `Updated 7 July 2026`
- `65 tracked latest entries`
- missing homepage objects for Sadhu 2021, Yi 2022, Choi 2023, Lei 2019, PathFinder 2024, and Keyhole Imaging 2019.

This run updated `index.html` to:

- show `Updated 9 July 2026`
- show `71 tracked latest entries`
- add the six missing latest-entry objects:
  - `Automatic calibration of time of flight based non-line-of-sight reconstruction` — Sadhu et al., arXiv 2021
  - `Differentiable Transient Rendering` — Yi et al., arXiv 2022
  - `Self-Calibrating, Fully Differentiable NLOS Inverse Rendering` — Choi et al., arXiv 2023
  - `Direct Object Recognition Without Line-of-Sight Using Optical Coherence` — Lei et al., arXiv 2019
  - `PathFinder: Attention-Driven Dynamic Non-Line-of-Sight Tracking with a Mobile Robot` — Kannapiran et al., arXiv 2024
  - `Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path` — Metzler et al., arXiv 2019
- update the timeline narrative to mention keyhole/single-path NLOS, coherent recognition, self-calibration, differentiable transient rendering, self-calibrating inverse rendering, and mobile-robot passive tracking.

## Remaining survey/PDF consistency work

`bare_jrnl.tex` still uses only:

```tex
\bibliography{egbib}
```

The survey source should be updated to include the supplement BibTeX files before regenerating the PDF:

```tex
\bibliography{egbib,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates,egbib_20260707_updates,egbib_20260708_updates}
```

The narrative still needs a careful source-level pass before PDF regeneration, especially for:

- differentiable transient rendering and self-calibrating inverse rendering in `article/4datadriven.tex`
- PathFinder / mobile passive NLOS tracking in `article/5newscenes.tex`
- Keyhole Imaging and single-path transient NLOS in `article/2active.tex` or the dynamic/new-scenes discussion

`bare_jrnl.pdf` was not regenerated in this run because the available safe GitHub operation is text-file replacement and there is no verified local LaTeX build/binary-PDF upload path in this automation environment.
