# 2026-07-02 dual-beam RIS radar NLOS update

## Summary

This run added one missing RF/radar NLOS-adjacent paper:

- **Radar Sensing using Dual-Beam Reconfigurable Intelligent Surface** — Kainat Yasmeen, Shobha Sundar Ram, Debidas Kundu, **arXiv 2026**.

## Why it was added

The paper is not a conventional optical hidden-shape reconstruction method, but it is directly relevant to the repository's Radar / RF / mmWave NLOS branch. It studies around-the-corner radar sensing in NLOS settings using a reconfigurable intelligent surface (RIS), focusing on practical one-bit quantized RIS phase control that produces dual symmetric beams. It complements the already-listed paper **Around-the-corner Radar Sensing Using Reconfigurable Intelligent Surface** by studying practical hardware/beam-control constraints, dual-beam behavior, forward/reverse radar cross-section, and simulation/measurement benchmarking against a metal reflector and an ideal single-beam RIS.

## Metadata decision

- arXiv: https://arxiv.org/abs/2602.11473
- arXiv date: 2026-02-12
- No reliable final journal/conference venue was found in this run, so the paper is labeled **arXiv 2026**.

## Files updated

- `README.md`
  - Updated the Latest Additions date to 2 July 2026.
  - Added the dual-beam RIS radar entry next to the existing RIS-assisted around-corner radar entry.

- `index.html`
  - Updated homepage date to 2 July 2026.
  - Updated latest-entry count from 39 to 40.
  - Added the paper to the Latest Additions and Paper Explorer.
  - Updated the 2026 timeline sentence to mention dual-beam RIS hardware constraints.

- `article/5newscenes.tex`
  - Added the paper to the Radar-Based NLOS Imaging subsection.
  - Integrated it as a practical quantized-RIS beam-control step in the RF/mmWave NLOS sensing trajectory.

- `article/6conclusion.tex`
  - Added a short conclusion-level sentence on one-bit quantized RIS beam control and reciprocal two-way scattering.

- `egbib_20260702_updates.bib`
  - Added BibTeX key: `yasmeenDualBeamRIS2026`.

## Survey PDF status

The LaTeX source and bibliography supplement were updated, but `bare_jrnl.pdf` was **not regenerated** in this run. The remaining local build step is to make the main survey bibliography line include all supplemental BibTeX files:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates}
```

Then compile the survey locally with LaTeX/BibTeX and upload the regenerated `bare_jrnl.pdf`. The current GitHub connector path does not provide a safe LaTeX compilation environment or binary PDF upload path, so no PDF update is claimed here.
