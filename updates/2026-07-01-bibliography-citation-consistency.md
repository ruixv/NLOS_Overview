# 2026-07-01 Bibliography and Citation Consistency Update

This run did not identify a fresh, high-confidence NLOS paper beyond the current README/homepage latest-entry set. Fresh keyword and citation-tracing checks mainly returned papers that are already tracked in the repository, including 3D Gaussian Transient Rendering, consumer-LiDAR NLOS, DENALI, MITO, TransiT, Time-Resolved Transformer, Backscatter-assisted NLOS positioning, RIS/EMVS NLOS localization, and double-bounce radio SLAM.

## What changed

The main update is a bibliography consistency fix for the LaTeX survey source. Several papers that had already been integrated into `article/5newscenes.tex`, `article/6conclusion.tex`, README, or the homepage did not yet have corresponding BibTeX entries in `egbib_2026_updates.bib`. This would leave unresolved citations once the supplemental bibliography files are enabled in `bare_jrnl.tex`.

Updated `egbib_2026_updates.bib` by adding or completing BibTeX entries for:

- `somasundaramRoleTransients2023`
- `sultanOptimizedSamplingNLOS2025`
- `marcoComprehensiveToFNLOS2026`
- `doddsMITO2025`
- `parkTjunctionPedestrian2025`
- `yanMmMirror2025`
- `bandariSeeBeam2025`
- `tongNLOSAidedMIMO2026`
- `zhangDoubleBounceRadioSLAM2026`
- `yasmeenRISRadar2026`
- `chenBeyondLambdaEMVS2026`
- `ruttikBackscatterNLOS2026`
- `somasundaramConsumerLiDARNLOS2026`
- `behariDENALI2026`

Also corrected the passive-acoustic BibTeX author metadata from the previous placeholder to `Sommer, Tal I. and Katz, Ori`.

## Metadata policy

All newly completed entries in this bibliography supplement are kept as arXiv entries unless a final venue was verified during the run. This follows the repository update rule that arXiv should remain the venue/status when no reliable accepted/published venue can be confirmed.

One venue item remains worth future review: the current README/homepage label for `Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals` is `CVPR 2026`, but this run only verified an arXiv/project-page record and did not find a final CVPR/OpenAccess page. I did not modify README or `index.html` in this run because the priority was citation consistency and because large-file whole replacement still risks unrelated edits.

## Remaining LaTeX / PDF work

`bare_jrnl.tex` still contains:

```tex
\bibliography{egbib}
```

For the updated survey build, this should become:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates}
```

I did not directly update `bare_jrnl.tex` in this run because the available GitHub update path performs whole-file replacement, and the fetched text rendering can corrupt LaTeX backslashes in some contexts. The safer next step is a local or patch-only edit of that single bibliography line, followed by a normal LaTeX/BibTeX compile and upload of the regenerated `bare_jrnl.pdf`.

No `bare_jrnl.pdf` update was performed in this run.