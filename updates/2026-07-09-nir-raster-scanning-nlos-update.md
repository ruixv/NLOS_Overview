# 2026-07-09 NIR raster-scanning NLOS update

## Search result

This run repeated keyword search and forward-citation-style checks around active ToF NLOS, LCT/f-k/phasor-field, neural transient fields, passive NLOS, acoustic/RF/consumer-LiDAR NLOS, differentiable transient rendering, keyhole/single-path NLOS, and recent 2026 arXiv updates.

A new directly relevant July 2026 arXiv paper was found:

- **Non-Line-of-Sight imaging using raster scanning at NIR wavelength** — Mohammad Roueinfar, Mahdi Salmanian, arXiv 2026, `2607.04183`.
  - Link: https://arxiv.org/abs/2607.04183
  - Date on arXiv: 5 July 2026.
  - Relevance: direct active optical NLOS imaging. The paper uses an 808 nm NIR laser, a pan-tilt raster-scanning setup, a relay wall, and an NIR camera to image hidden targets through three-bounce indirect reflection.
  - Scope note: this is a simple NIR raster-scanning experimental baseline rather than a new frontier inverse model, but it is genuinely NLOS imaging and was not present in the current README/homepage/latest logs.

No final journal or conference venue was verified in the search pass, so the conservative venue label is **arXiv 2026**.

## BibTeX update

Added `egbib_20260709_updates.bib` with key:

```bibtex
roueinfarRasterScanningNIRNLOS2026
```

## README patch

Insert near the top of `README.md` Latest Additions, immediately after the table header and before the existing 3D Gaussian Transient Rendering row:

```md
| 2026 | [Non-Line-of-Sight imaging using raster scanning at NIR wavelength](https://arxiv.org/abs/2607.04183) — Roueinfar, Salmanian | arXiv 2026 | Demonstrates a low-cost 808 nm NIR raster-scanning active NLOS setup with pan-tilt illumination and NIR-camera capture over three hidden targets; useful as a simple hardware/acquisition baseline rather than a new inverse-model frontier. |
```

The README update date may remain `9 July 2026` for this run, or be changed to a more precise `Update run: 9 July 2026` if desired.

## Homepage patch

`index.html` currently shows `71 tracked latest entries`. After adding the new NIR raster-scanning object, change the count to `72 tracked latest entries` and insert this object at the top of `const papers`, immediately before the 3D Gaussian Transient Rendering object:

```js
{cat:"latest active",title:"Non-Line-of-Sight imaging using raster scanning at NIR wavelength",authors:"Roueinfar and Salmanian",year:2026,venue:"arXiv 2026",url:"https://arxiv.org/abs/2607.04183",key:"808 nm NIR laser with pan-tilt raster scanning and NIR-camera capture for direct three-bounce active NLOS imaging of hidden targets."},
```

The 2026 timeline sentence can be lightly expanded from:

```text
The frontier moves toward real-world geometry: non-planar limited relays, smartphone-grade LiDAR motion sampling, RF/radar neural reconstruction, low-cost LiDAR datasets, quantized RIS, backscatter positioning, double-bounce radio SLAM, and NLOS-aided off-grid MIMO/ISAC imaging.
```

to:

```text
The frontier moves toward real-world geometry and accessible hardware: non-planar limited relays, smartphone-grade LiDAR motion sampling, low-cost NIR raster scanning, RF/radar neural reconstruction, low-cost LiDAR datasets, quantized RIS, backscatter positioning, double-bounce radio SLAM, and NLOS-aided off-grid MIMO/ISAC imaging.
```

## Survey-source patch

Add a short sentence to the active optical acquisition / hardware discussion in `article/2active.tex` or the new-scenes/accessibility discussion in `article/5newscenes.tex`:

```tex
Recent low-cost optical variants also revisit raster-scanned active NLOS with near-infrared illumination: Roueinfar and Salmanian~\cite{roueinfarRasterScanningNIRNLOS2026} use an 808~nm laser, pan--tilt scanning, and an NIR camera to demonstrate three-bounce hidden-target imaging, providing a simple hardware/acquisition baseline complementary to SPAD- and transient-camera systems.
```

Update the `bare_jrnl.tex` bibliography line to include the new supplement file:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates,egbib_20260707_updates,egbib_20260708_updates,egbib_20260709_updates}
```

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The remaining steps are:

1. Integrate the README/homepage/LaTeX patches above.
2. Ensure `bare_jrnl.tex` loads all supplement `.bib` files including `egbib_20260709_updates`.
3. Run LaTeX/BibTeX locally and replace `bare_jrnl.pdf` after verifying citation resolution and layout.
