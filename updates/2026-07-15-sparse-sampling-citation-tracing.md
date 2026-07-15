# 15 July 2026 sparse-sampling NLOS citation-tracing update

A fresh search of arXiv, conference and journal pages, project/lab pages, and forward citations of the repository's core active-NLOS papers did not identify a directly relevant paper newer than the 5 July 2026 NIR raster-scanning preprint already tracked by the repository.

The high-priority citation-tracing pass through recent phasor-field and sparse-aperture work identified a public-coverage and bibliography gap around two CVPR 2023 milestones:

- **Non-Line-of-Sight Imaging With Signal Superresolution Network** — Jianyu Wang, Xintong Liu, Leping Xiao, Zuoqiang Shi, Lingyun Qiu, and Xing Fu; CVPR 2023, pp. 17420–17429. The method learns a plug-and-play transient superresolution module for sparse confocal and non-confocal measurements and reports a 16× acquisition-time reduction at comparable reconstruction quality.
- **Few-Shot Non-Line-of-Sight Imaging With Signal-Surface Collaborative Regularization** — Xintong Liu, Jianyu Wang, Leping Xiao, Xing Fu, Lingyun Qiu, and Zuoqiang Shi; CVPR 2023, pp. 13303–13312. The repository currently labels this only by its 2022 arXiv posting. The final CVPR venue should be used. The method jointly regularizes measured signals, a 3D voxel representation, and a 2D hidden surface, demonstrating recovery from a 5×5 confocal grid and a reported 10,000× acquisition reduction.

The survey source already discusses SSN and **Deep Non-Line-of-Sight Imaging from Under-Scanning Measurements**, but the consolidated bibliography currently lacks the corresponding `wangSignalSuperresolution2023` and `liDeepUnderscanning2023` records. It also lacks the `liuFewShotSSCR2022` key already used by the survey. The new supplement `egbib_20260715_sparse_sampling_updates.bib` repairs all three keys; the USM entry is deliberately conservative and uses only metadata verified from the LEAP reference list.

## Exact synchronization changes

1. **README.md**
   - Insert the SSN CVPR 2023 row immediately after the Latest Additions table header.
   - Replace the existing 2022/arXiv SSCR row with the final CVPR 2023 record and official CVF link.
   - Add SSN and SSCR to the 2023 milestone node before the differentiable-rendering milestones.

2. **index.html**
   - Insert an SSN `papers` object immediately after `const papers=[`.
   - Replace the existing SSCR object with the final CVPR metadata and official CVF link.
   - Increment tracked latest entries from 96 to 97 only when SSN is newly inserted.
   - Expand the 2023 timeline to connect SSN/SSCR sparse acquisition with differentiable transient rendering, transformers, neural surfaces, and Virtual Mirrors.

3. **article/2active.tex**
   - Replace the paragraph beginning `More recently, several works have further reduced the required scanning density.` in the `Reducing scanning points` discussion.
   - The replacement should explicitly connect SSCR, SSN, USM, and Virtual Scanning and cite `liuFewShotSSCR2022`, `wangSignalSuperresolution2023`, `liDeepUnderscanning2023`, and `cuiVirtualScanning2024`.

4. **Bibliography and PDF**
   - Run `python scripts/merge_nlos_bibliography.py` so the new supplement is merged into `egbib_merged_20260711.bib` and all cited keys are audited.
   - Perform a clean LaTeX/BibTeX build of `bare_jrnl.tex`.
   - Verify that the generated PDF contains the SSN and SSCR titles and that the LaTeX log contains no undefined citations or references.

## Automation status

The repository now contains:

- `egbib_20260715_sparse_sampling_updates.bib`
- `scripts/sync_nlos_20260715_sparse_sampling.py`
- `.github/workflows/sync_sparse_sampling_nlos_20260715.yml`

The workflow is designed to apply the marker-based edits, regenerate the consolidated bibliography, clean-build `bare_jrnl.pdf`, validate the citations/PDF, and commit the generated artifacts. At the time this note was committed, no workflow-generated synchronization commit had appeared. Therefore this note does **not** claim that `README.md`, `index.html`, `article/2active.tex`, `egbib_merged_20260711.bib`, or `bare_jrnl.pdf` have already changed. The source supplement and exact safe patch are committed; the public artifacts and binary PDF remain pending until the workflow executes successfully.
