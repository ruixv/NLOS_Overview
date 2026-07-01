# 2026-07-01 — Ptychographic and Navigation NLOS Sync

## Added high-confidence missing papers

1. Song et al., **Ptychographic non-line-of-sight imaging for depth-resolved visualization of hidden objects**, arXiv 2024.  
   Link: https://arxiv.org/abs/2405.11115

2. Young et al., **Enhancing Autonomous Navigation by Imaging Hidden Objects using Single-Photon LiDAR**, arXiv 2024.  
   Link: https://arxiv.org/abs/2410.03555

3. Sun et al., **Generalizable Non-Line-of-Sight Imaging with Learnable Physical Priors**, arXiv 2024.  
   Link: https://arxiv.org/abs/2409.14011

## Metadata decisions

- No final accepted/published venue was verified for the three papers above in this run; all are therefore labeled **arXiv 2024**.
- The homepage metadata for Sun et al. was corrected from the previously unverified **CVPR 2025** label to **arXiv 2024**.

## Repository updates

- `README.md`
  - Added the three papers to **Latest Additions**.
  - Moved the Last Updated badge to July 2026.

- `index.html`
  - Updated latest-entry count from 36 to 39.
  - Added the three papers to the Latest cards and searchable paper explorer.
  - Updated the 2024 timeline entry to include ptychography and single-photon-LiDAR navigation.
  - Corrected Sun et al. metadata to arXiv 2024.

- `article/5newscenes.tex`
  - Added a new **Ptychographic NLOS Imaging** subsection.
  - Added single-photon-LiDAR autonomous navigation to the robotic NLOS discussion before SuperEx.

- `article/6conclusion.tex`
  - Added ptychographic NLOS to the forward-model / reconstruction-infrastructure and geometry discussions.
  - Added single-photon-LiDAR navigation to the new-modality / robotic NLOS discussion.

- `egbib_20260701_updates.bib`
  - Added BibTeX entries for `songPtychographicNLOS2024`, `youngNavigationNLOS2024`, and `sunGeneralizable2025`.

## PDF status

`bare_jrnl.pdf` was **not regenerated** in this run.

The main LaTeX file still uses:

```tex
\bibliography{egbib}
```

To compile all newly integrated survey references, update it to:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates}
```

Then run the local LaTeX/BibTeX build and upload the regenerated `bare_jrnl.pdf`.

This was not done automatically because the current GitHub connector exposes large text files through whole-file replacement and does not provide a safe LaTeX compile plus binary PDF upload path.
