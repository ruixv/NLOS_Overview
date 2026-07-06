# 2026-07-07 public-surface consistency sync

## Search and citation-tracing result

Fresh keyword/web search and a citation-tracing-style pass around active ToF, phasor-field, occlusion-aware active NLOS, RIS/radar NLOS, and recent arXiv 2026 entries did not reveal a newer high-confidence July 2026 optical/transient NLOS imaging frontier paper beyond the current 2026 list.

The actionable gap was public-surface consistency: several papers that had already been verified or placed in update notes / BibTeX supplements were still absent from the README and homepage paper explorer.

## Papers surfaced in README and homepage

- **Radar Cross Section Characterization of Quantized Reconfigurable Intelligent Surfaces** — Yasmeen, Ram, Kundu, arXiv 2026.  This complements RIS around-corner radar sensing by characterizing one-bit/quantized RIS RCS and demonstrating recovery of micro-Doppler signatures in non-specular or shadowed regions.
- **Coherent control of light for non-line-of-sight imaging** — Starshynov, Ghafur, Fitches, Faccio, arXiv 2019.  This uses coherent phase control / wavefront shaping and the speckle memory effect to refocus light behind an obstacle, enabling sub-millimeter active NLOS imaging.
- **Non-line-of-sight Imaging with Partial Occluders and Surface Normals** — Heide, O'Toole, Zang, Lindell, Diamond, Wetzstein, arXiv 2017.  This adds partial occlusions and surface normals to the NLOS light-transport model.
- **Exploiting Occlusion in Non-Line-of-Sight Active Imaging** — Thrampoulidis et al., arXiv 2017.  This treats natural hidden-scene occluders as useful coding structure and suggests reduced reliance on expensive time-resolved hardware.

## Repository updates in this run

- `README.md`
  - Updated the run marker to **7 July 2026**.
  - Added the four entries above to the Latest Additions table.
  - Kept the 2026 frontier venue labels conservative as **arXiv 2026** where no final venue page was verified.

- `index.html`
  - Updated the hero/footer date to **7 July 2026**.
  - Updated the tracked latest-entry count to **65**.
  - Synced the paper explorer with README-visible recent entries, including previously missing single-photon, phasor-field, coherent-control, single-pixel-camera, transient-sinogram, occlusion-aware, and quantized-RIS entries.
  - Fixed the three 2026 frontier venue labels to arXiv status where final venues were not verified.
  - Added a 2017 timeline note for occlusion-aware active NLOS models and expanded the 2019 timeline note to include coherent control and single-pixel NLOS.

## Survey / PDF status

The main LaTeX survey source still needs a careful source-level pass before claiming full PDF consistency. The current bibliography line in `bare_jrnl.tex` is still:

```tex
\bibliography{egbib}
```

It should be changed to:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates}
```

The existing `article/2active.tex` already discusses the occlusion-aware active NLOS line through `heideNonlineofsightImagingPartial2017` and `thrampoulidisExploitingOcclusionNonLineofSight2018`, and also includes single-pixel / transient-sinogram / active-focusing / sparse-sampling material. A future safe TeX patch should additionally add one short sentence in the active-focusing or wavefront-shaping paragraph noting Starshynov et al.'s coherent phase control / speckle-memory-effect active NLOS result, and a short note in the RF/RIS section for quantized-RIS RCS.

`bare_jrnl.pdf` was not regenerated in this run. The available GitHub write path is safe for UTF-8 text files, but not for binary PDF replacement, so no claim is made that the PDF was updated.
