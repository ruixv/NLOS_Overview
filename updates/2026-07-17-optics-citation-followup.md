# Optica and LCT citation-tracing follow-up — 17 July 2026

## Verified additions

This follow-up identifies four direct NLOS papers absent from the public repository snapshot and one final-venue correction.

1. **Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding** — Xuefeng Wang, Xingsu Chen, Miao Xu, Gulnaz Alimjan, and Li Zhao, *Optics Express* 34(14), 26271–26289 (2026). Publisher page: `https://opg.optica.org/oe/abstract.cfm?uri=oe-34-14-26271`. The publisher page does not yet expose a stable DOI in the available metadata, so no DOI has been invented.
2. **Learned light-cone transform for fast and accurate non-line-of-sight imaging** — Xinqi Gao, Yijie Yang, Lianfang Wang, Xueying Liu, Yong Wang, and Yuping Duan, *Physical Review Applied* 25, 044024 (2026), DOI `10.1103/jsbg-c7l5`. This is a high-priority citation-traced extension of O'Toole et al.'s LCT: it introduces high-frequency-enhanced learnable Wiener filtering, spatiotemporal feature extraction, and volume projection, and reports a 5 dB PSNR improvement over LCT.
3. **Transient video interpolation for dynamic non-line-of-sight imaging** — Shida Sun, Yue Li, Jiacheng Fu, Feihu Xu, and Zhiwei Xiong, *Optics Express* 34(3), 4882–4894 (2026), DOI `10.1364/OE.580550`. TransVID uses spatial–temporal attention and latent conditional diffusion to recover 128×128 transient video at 16 fps from 16×16 measurements at 4 fps.
4. **Multi-surface sub-resolution non-line-of-sight imaging via transient waveform deposition** — Yi Wei, Jinye Miao, Yan Zhao, Taotao Qin, Lianfa Bai, Enlai Guo, and Jing Han, *Optics Express* 33(24), 51362–51382 (2025), DOI `10.1364/OE.579004`. It decomposes overlapping multi-surface returns as Gaussian mixtures before LCT reconstruction and reports centimeter-scale axial and lateral discrimination.
5. **Fast non-line-of-sight transient data simulation and an open benchmark dataset** — Yingjie Shi et al. The repository currently labels this as arXiv 2025; the verified final version is *Optics Express* 33(24), 51335–51350 (2025), DOI `10.1364/OE.575753`.

## Intended guarded integration

The committed files `egbib_20260717_optics_followup_updates.bib` and `scripts/sync_nlos_20260717_optics_followup.py` provide canonical metadata and anchor-checked edits for:

- `README.md`: four new rows, the simulation venue correction, and timeline placement;
- `index.html`: four searchable entries, final-venue correction, 2026 timeline expansion, and tracked-entry count update from 110 to 114 after the preceding frontier patch;
- `article/2active.tex`: multi-surface transient decomposition and active-SPAD table coverage;
- `article/3passive.tex`: diffuse-aware passive reconstruction and table coverage;
- `article/4datadriven.tex`: learned LCT and diffusion-based transient-video interpolation;
- `egbib_merged_20260711.bib`, `bare_jrnl.tex`, and `bare_jrnl.pdf`: bibliography merge, clean LaTeX/BibTeX build, and PDF regeneration.

The workflow `.github/workflows/sync_nlos_optics_followup_20260717.yml` runs both the previously pending frontier synchronizer and this follow-up synchronizer, performs citation and duplicate-entry audits, renders the old and new PDFs, validates PDF text, and commits the binary only after all checks pass.

## Current repository state

At the time this note was committed, no GitHub Actions source-integration or PDF-rebuild commit had appeared after the workflow-trigger commit. Therefore, **README.md, index.html, the survey sections, the consolidated bibliography, and bare_jrnl.pdf must still be treated as not yet integrated for this follow-up**. The large public files were not overwritten through a full-file replacement API because doing so without an executed/validated patch would risk truncation or data loss. No claim is made that the PDF has been regenerated.
