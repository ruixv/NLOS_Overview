# 2026-07-10 README NIR sync and consistency note

## Search result

This run repeated fresh keyword search and citation-tracing-style checks around active ToF NLOS, LCT/f-k/phasor-field, passive NLOS, Neural Transient Fields, differentiable transient rendering, consumer LiDAR, acoustic/RF/mmWave/THz, RIS/ISAC, keyhole/single-path NLOS, and recent 2026 arXiv updates.

No additional high-confidence July 2026 frontier NLOS imaging paper was found beyond the already verified July arXiv paper:

- **Non-Line-of-Sight imaging using raster scanning at NIR wavelength** — Mohammad Roueinfar, Mahdi Salmanian, arXiv 2026, `2607.04183`.
  - Link: https://arxiv.org/abs/2607.04183
  - Date on arXiv: 5 July 2026.
  - Relevance: direct active optical NLOS imaging using an 808 nm NIR laser, pan-tilt raster scanning, a relay wall, and an NIR camera for three-bounce hidden-target imaging.
  - Venue check: no final conference/journal venue was verified, so the conservative venue remains **arXiv 2026**.

## Repository changes in this run

`README.md` was updated directly:

- Update date changed to `10 July 2026`.
- Added the Roueinfar/Salmanian NIR raster-scanning paper at the top of Latest Additions.
- The entry is categorized as a direct active optical NLOS acquisition/hardware baseline, not a new inverse-model frontier.

Commit:

```text
ce69615bc84b756883f700ad5373e93c0bf06dc7
```

`egbib_20260709_updates.bib` already contains the BibTeX key:

```bibtex
roueinfarRasterScanningNIRNLOS2026
```

## Remaining homepage patch

`index.html` still needs to be updated from `71` to `72` tracked latest entries and should insert this object at the top of `const papers`, immediately before the 3D Gaussian Transient Rendering object:

```js
{cat:"latest active",title:"Non-Line-of-Sight imaging using raster scanning at NIR wavelength",authors:"Roueinfar and Salmanian",year:2026,venue:"arXiv 2026",url:"https://arxiv.org/abs/2607.04183",key:"808 nm NIR laser with pan-tilt raster scanning and NIR-camera capture for direct three-bounce active NLOS imaging of hidden targets."},
```

Also change the hero/stat count:

```html
<div class="stat"><b>72</b><span>tracked latest entries</span></div>
```

The 2026 timeline sentence can be expanded to:

```text
The frontier moves toward real-world geometry and accessible hardware: non-planar limited relays, smartphone-grade LiDAR motion sampling, low-cost NIR raster scanning, RF/radar neural reconstruction, low-cost LiDAR datasets, quantized RIS, backscatter positioning, double-bounce radio SLAM, and NLOS-aided off-grid MIMO/ISAC imaging.
```

I did not whole-file overwrite `index.html` in this run because the file is a compact hand-maintained HTML/JS artifact and a line-level patch API was not available.

## Remaining survey-source patch

Add a short sentence to the active optical acquisition / hardware discussion in `article/2active.tex` or the new-scenes/accessibility discussion in `article/5newscenes.tex`:

```tex
Recent low-cost optical variants also revisit raster-scanned active NLOS with near-infrared illumination: Roueinfar and Salmanian~\cite{roueinfarRasterScanningNIRNLOS2026} use an 808~nm laser, pan--tilt scanning, and an NIR camera to demonstrate three-bounce hidden-target imaging, providing a simple hardware/acquisition baseline complementary to SPAD- and transient-camera systems.
```

Update `bare_jrnl.tex` from:

```tex
\bibliography{egbib}
```

to:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates,egbib_20260707_updates,egbib_20260708_updates,egbib_20260709_updates}
```

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. Remaining steps:

1. Apply the homepage and survey-source patches above.
2. Ensure `bare_jrnl.tex` loads all supplement `.bib` files through `egbib_20260709_updates`.
3. Run LaTeX/BibTeX locally and replace `bare_jrnl.pdf` after verifying citation resolution and layout.
