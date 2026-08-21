# 22 August 2026 — transient human-pose survey consistency gap

## Verified paper

**Zhongpei Xiao, Chen Dai, Ruilin Ye, Jianwei Zeng, Wenwen Li, and Feihu Xu, “Non-line-of-sight human pose estimation,” Optics and Lasers in Engineering 201, 109658 (2026), DOI 10.1016/j.optlaseng.2026.109658.**

The final Elsevier record verifies the journal, volume, article number, DOI, and six-author list. The paper is directly active transient NLOS rather than a generic pose-estimation citation: a pulsed-laser / SPAD ToF system reconstructs a hidden 3-D volume, derives intensity and depth representations, and fuses those cues in a multi-stage semantic network. A physics-based NLOS simulator synthesizes training examples from smartphone human videos; measured experiments report pose recovery at relay depth up to 1.75 m and SNR down to 0.13.

The paper also lies on the survey's Core-paper citation lineage: its NLOS background explicitly starts from Velten et al.'s ultrafast ToF work and uses the standard three-bounce transient forward model, while positioning itself against prior transient human-pose methods such as HiddenPose.

## Current repository state

The public README / V2 history already mention this work (including the compact 2026 timeline statement that Xiao et al. extend active transients to semantic human-pose recovery), but the current LaTeX survey prose inspected in `article/4datadriven.tex` stops its pose-sensing discussion at Chandran et al. and Hou et al. The merged bibliography / survey citation path does not currently expose DOI `10.1016/j.optlaseng.2026.109658`. Therefore this run treats the paper as a **survey/bibliography/PDF consistency gap**, not as a newly discovered README paper.

## Exact integration plan

1. **README / V2 corpus:** do not duplicate the existing paper row/object. Preserve the final Optics and Lasers in Engineering venue and existing contribution summary. Only synchronize the public update date if the integration run advances the survey date.
2. **`article/4datadriven.tex`:** extend the existing `Learned illumination control and multi-person pose sensing` paragraph after the Hou et al. discussion with a concise deployment-oriented continuation, for example:

```latex
Xiao~\etal~further target semantic recovery when the transient signal itself becomes severely degraded~\cite{xiaoNLOSHumanPose2026}. Their pipeline reconstructs a hidden three-dimensional volume, derives complementary depth and intensity representations, and fuses them in a multi-stage network for three-dimensional joint estimation. A physics-based NLOS simulator converts ordinary smartphone human videos into large-scale pose training data, reducing dependence on costly transient capture. Experiments with a self-built laser/SPAD system retain useful pose estimates at relay depths up to 1.75~m and SNR as low as 0.13, shifting transient human-pose sensing from proof-of-concept inference toward robustness under weak-photon and longer-range conditions.
```

3. **Bibliography:** merge `egbib_20260822_semantic_pose_gap.bib` into `egbib_merged_20260711.bib` exactly once using key `xiaoNLOSHumanPose2026` and DOI `10.1016/j.optlaseng.2026.109658` as duplicate guards.
4. **`bare_jrnl.tex`:** advance the public coverage/provenance date only in the same guarded run that rebuilds the PDF.
5. **PDF validation:** clean-build `bare_jrnl.pdf`; verify `xiaoNLOSHumanPose2026` in `.aux`, the normalized title in `.bbl`, the pose-sensing prose in extracted PDF text, and successful first/last-page rendering before committing the binary.
6. Remove the staging BibTeX only after the canonical merged bibliography and PDF have passed the checks above.

## Related audit result

The same fresh publisher/citation-tracing pass rechecked PICL (`10.1364/JOSAA.593401`), learned LCT, consumer-LiDAR NLOS, arbitrary-relay 3D Gaussian Transient Rendering, MD-NLOS, Stereo NLOS, and relay-free acoustic NLOS. Those works are already represented in the current public corpus, so they should not be duplicated.
