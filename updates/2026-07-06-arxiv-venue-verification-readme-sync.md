# 2026-07-06 arXiv-only venue verification and README sync

## Search result

A fresh keyword and forward-citation-style web pass did not surface a new high-confidence NLOS imaging paper beyond the current July 2026 frontier list. The most recent directly relevant hits remain:

- Wang et al., *Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering*, arXiv:2606.21270.
- Somasundaram et al., *Imaging Hidden Objects with Consumer LiDAR via Motion Induced Sampling*, arXiv:2605.17865.
- Lu et al., *Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals*, arXiv:2605.29098.

For these three entries, the fresh search found only arXiv/source metadata and did not verify stable final venue pages for the previously displayed `SIGGRAPH 2026`, `Nature 2026`, or `CVPR 2026` labels. Under the repository rule that arXiv-first papers should be labeled by the final venue only when the final venue is verified, the README now labels all three as `arXiv 2026`.

## Committed change

- `README.md` updated to `Update run: 6 July 2026`.
- Venue/status changed:
  - `SIGGRAPH 2026` -> `arXiv 2026` for 3D Gaussian Transient Rendering.
  - `Nature 2026` -> `arXiv 2026` for consumer-LiDAR NLOS.
  - `CVPR 2026` -> `arXiv 2026` for GeRaF 2.0 / seeing through boxes.

## Remaining consistency work

`index.html` still mirrors the old venue labels and should be updated when safe:

```diff
- Updated 4 July 2026 · 190+ papers
+ Updated 6 July 2026 · 190+ papers

- <p style="margin-top:1rem;">Last updated: 4 July 2026</p>
+ <p style="margin-top:1rem;">Last updated: 6 July 2026</p>

- venue:'SIGGRAPH 2026'
+ venue:'arXiv 2026'

- venue:'Nature 2026'
+ venue:'arXiv 2026'

- venue:'CVPR 2026'
+ venue:'arXiv 2026'
```

`bare_jrnl.tex` still needs its bibliography line changed before PDF compilation:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates}
```

The updated PDF was not regenerated in this run because no safe LaTeX/PDF build-and-upload path was available through the current connector set.
