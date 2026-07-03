# 2026-07-04 DG-NLOS and homepage consistency sync

## Summary

This update pass did not identify a newer high-confidence NLOS imaging paper beyond the current July 2026 frontier list. The search and verification pass mainly returned papers already represented in the repository, including 3D Gaussian Transient Rendering, consumer-LiDAR NLOS, GeRaF 2.0, RIS radar sensing, LEAP, and other recent entries.

The useful missing item found in this pass was a consistency gap around DG-NLOS:

- `article/4datadriven.tex` already discussed and cited `suDGNLOS2025` in the graph-neural-network paragraph.
- `README.md` did not list DG-NLOS in Latest Additions.
- `egbib_20260703_updates.bib` did not contain the `suDGNLOS2025` BibTeX entry.
- `index.html` contained a stale non-latest DG-NLOS object with an unverified venue label (`AAAI`) and no URL.

## Verified paper

### Dual-branch Graph Feature Learning for NLOS Imaging

- Authors: Xiongfei Su, Tianyi Zhu, Lina Liu, Zheng Chen, Yulun Zhang, Siyuan Li, Juntian Ye, Feihu Xu, Xin Yuan
- Status: arXiv 2025
- arXiv: https://arxiv.org/abs/2502.19683
- Reason for inclusion: direct learned NLOS imaging paper. It introduces DG-NLOS, a graph-feature-learning architecture that transforms dense NLOS grid data into sparse structural features and uses dual branches for albedo and depth/geometric recovery.
- Metadata decision: no reliable final conference/journal venue was verified in this pass, so the repository labels it as `arXiv 2025` rather than the previously stale `AAAI` label that appeared in the website object.

## Repository changes

### README.md

- Updated the run label to `4 July 2026`.
- Added the following Latest Additions row:

```markdown
| 2025 | [Dual-branch Graph Feature Learning for NLOS Imaging](https://arxiv.org/abs/2502.19683) — Su et al. | arXiv 2025 | DG-NLOS uses graph feature learning with separate albedo and depth branches to reduce 3D-grid cost while jointly reconstructing hidden appearance and geometry. |
```

### egbib_20260703_updates.bib

Added:

```bibtex
@misc{suDGNLOS2025,
  title   = {Dual-branch Graph Feature Learning for NLOS Imaging},
  author  = {Su, Xiongfei and Zhu, Tianyi and Liu, Lina and Chen, Zheng and Zhang, Yulun and Li, Siyuan and Ye, Juntian and Xu, Feihu and Yuan, Xin},
  year    = {2025},
  eprint  = {2502.19683},
  archivePrefix = {arXiv},
  url     = {https://arxiv.org/abs/2502.19683}
}
```

### index.html

The homepage was substantially resynced with README instead of only patching one stale object:

- Updated the page date to `4 July 2026`.
- Updated the tracked latest-entry count to `53`.
- Added DG-NLOS to Latest Additions and the searchable paper explorer.
- Corrected DG-NLOS venue/status from unverified `AAAI` to `arXiv 2025`.
- Corrected NLOS-NeuS from stale `ICCV`/blank URL to `arXiv 2023` with its arXiv URL.
- Added the previously README-visible but homepage-missing recent entries, including LEAP, HDPS, scattering-media phasor fields, passive acoustic corners, Occlusion Fields, active focusing, RF/RIS/ISAC items, and commercial-LiDAR deep remapping.
- Updated the timeline text to mention graph models, LEAP, HDPS, scattering-media phasor fields, passive acoustic corners, and commercial-LiDAR deep remapping.

## Candidates not added

Several names appearing in recent related-work lists, including `TransDiff`, `DO-NLOS`, and some `Virtual Scanning`/domain-reduction references, were not added as new public-facing entries in this pass because independent, metadata-verifiable paper records could not be reliably confirmed during this run. They should be rechecked in a future pass before inclusion.

## Survey/PDF status

No PDF was regenerated in this run. The survey source already contains the DG-NLOS paragraph in `article/4datadriven.tex`, and this update adds the missing BibTeX key. However, the top-level `bare_jrnl.tex` still uses only:

```tex
\bibliography{egbib}
```

To compile the current extended survey, it should be changed to:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates}
```

After that, the survey should be compiled locally with LaTeX/BibTeX and `bare_jrnl.pdf` should be uploaded. The current environment did not provide a safe LaTeX compilation and binary PDF upload path, so the PDF was not silently claimed as updated.
