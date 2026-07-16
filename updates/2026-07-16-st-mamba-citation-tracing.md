# 16 July 2026 ST-Mamba citation-tracing and consistency update

## Verified missing public entry

**Toward Dynamic Non-Line-of-Sight Imaging with Mamba Enforced Temporal Consistency** — Yue Li, Yi Sun, Shida Sun, Juntian Ye, Yueyi Zhang, Feihu Xu, and Zhiwei Xiong; *Advances in Neural Information Processing Systems*, vol. 37, pp. 126452–126473, 2024; DOI: `10.52202/079017-4016`.

The paper is a direct active transient NLOS reconstruction contribution rather than a passing NLOS citation. It introduces ST-Mamba, a spatial--temporal state-space model for dynamic NLOS video, and couples interleaved Mamba processing with a phasor-field wave-domain loss to improve temporal consistency under noisy measurements. A forward-reference trace from the SIGGRAPH 2026 3D Gaussian Transient Rendering paper independently verifies the title, complete author list, NeurIPS 2024 venue, volume, pages, and DOI, and places the method in the dynamic-NLOS reconstruction trajectory.

## Repository gap found

The LaTeX survey already contained a semantically placed ST-Mamba literature-review paragraph and cited `liMambaTemporalConsistency2024`, but the citation key was absent from the consolidated bibliography and the paper was absent from `README.md` and `index.html`. This created a survey/bibliography/public-artifact consistency gap.

## Synchronized changes

- Add a canonical final-venue BibTeX record in `egbib_20260716_st_mamba_updates.bib`.
- Add the paper to the README latest-additions table and the 2024 milestone timeline.
- Add a searchable homepage paper object, increment the tracked-entry count from 104 to 105, and make the 2024 timeline explicitly identify ST-Mamba and its phasor-domain physics supervision.
- Add the citation to the active pulsed-laser/SPAD reconstruction summary table.
- Preserve the existing semantically placed survey paragraph in `article/4datadriven.tex` rather than duplicating it.
- Regenerate the duplicate-free merged bibliography and clean-build `bare_jrnl.pdf`.
- Validate unique cross-file presence, final-venue metadata, citation resolution, PDF text extraction, and page rendering.

No paper newer than the 5 July 2026 NIR raster-scanning preprint was added in this run; the substantive update is the verified NeurIPS 2024 citation-tracing and consistency repair above.
