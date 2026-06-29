# 2026-06-30 Survey Consistency Cleanup

This update run did not identify a new high-confidence NLOS imaging paper beyond the current README / homepage snapshot. The fresh search pass returned already-integrated items such as 3D Gaussian Transient Rendering, consumer LiDAR NLOS, GeRaF 2.0, Marco et al.'s ToF comparative study, Backscatter-assisted NLOS positioning, EMVS/RIS NLOS localization, and double-bounce radio SLAM.

## Cleanup performed

During the survey consistency pass, `article/5newscenes.tex` contained three survey subsections / citation hooks that could not be verified against reliable metadata in web/arXiv searches and did not have matching BibTeX entries:

- `xiaoHumanPose2026` / a claimed 2026 NLOS human pose paper;
- `zhouPolarizationSinglePixel2026` / a claimed polarization-based scanning-free NLOS paper;
- `liSuperFoVNLOS2026` / a claimed super-field-of-view NLOS paper.

To avoid leaving unverified or uncompilable survey content in the paper, the update:

1. Removed the unverified polarization and super-FoV subsections from `article/5newscenes.tex`.
2. Rewrote the NLOS human-pose subsection to cite the verified arXiv paper `Optical Non-Line-of-Sight Physics-based 3D Human Pose Estimation` (arXiv:2003.14414) via a direct link rather than a missing BibTeX key.
3. Updated the conclusion's semantic-NLOS future-direction sentence to use the same verified link, avoiding the missing `xiaoHumanPose2026` citation.

## Files changed

- `article/5newscenes.tex`
- `article/6conclusion.tex`

## PDF status

`bare_jrnl.pdf` was not regenerated in this run. The main unresolved build issue remains that `bare_jrnl.tex` currently calls only:

```tex
\bibliography{egbib}
```

while many newly integrated survey references live in:

```tex
egbib_2026_updates.bib
```

A safe future build should either:

```tex
\bibliography{egbib,egbib_2026_updates}
```

or append the supplement bibliography into a temporary build copy before running BibTeX. This run avoided overwriting the large `bare_jrnl.tex` file because the available connector still performs whole-file replacement rather than a patch-only edit.
