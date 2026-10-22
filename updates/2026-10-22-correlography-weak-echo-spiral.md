# 2026-10-22 — Forward-citation backfill: coherent correlography, weak echoes, spiral scanning

Three DOI-verified NLOS papers were found through OpenAlex forward citations of O'Toole et al. (Nature 2018 LCT), Optica/Optics Express publication records, and citations to the later 2026 adaptive-spiral method. Before this run, none was represented by its DOI and title in the README, paper explorer, or merged bibliography.

1. Muralidhar Madabhushi Balaji, Jiapeng Liu, Danyal Ahsanullah, Prasanna Rangarajan. "Imaging operator in indirect imaging correlography." *Optics Express* **31**(13), 21689–21705 (2023). DOI: https://doi.org/10.1364/OE.488520. Derives a coherent indirect NLOS imaging operator and pose-dependent resolution, with self-supervised autocorrelation inversion recovering approximately 250-µm hidden features at 1 m.
2. Tailin Li, Yihan Luo, Kaiyuan Zhao, Shiye Xia, Yaqing Liu, Haotong Ma, Ge Ren, Zongliang Xie. "Weak non-line-of-sight target echoes extraction without accumulation." *Optics Express* **31**(22), 36209–36218 (2023). DOI: https://doi.org/10.1364/OE.499869. Dual-detector temporal correlation and sequential histograms recover weak NLOS target echoes without indiscriminate noise accumulation; the task is tracking rather than dense 3D reconstruction.
3. Meiling Zhang, Yaoyao Shi, Wei Sheng, Jiaqing Liu, Jingwen Li, Yang Wei, Bin Wang, Dejin Zhang, Youwen Liu. "Non-line-of-sight imaging based on Archimedean spiral scanning." *Optics Communications* **537**, 129450 (2023). DOI: https://doi.org/10.1016/j.optcom.2023.129450. Fixed confocal spiral acquisition is a direct precursor cited by Oyama et al., *IEEE Open Journal of Signal Processing* (2026), DOI 10.1109/OJSP.2026.3688052.

## Source integration

- README.md: three Latest Additions rows and a 2023 milestone.
- index.html: new Core Reading Path paragraph.
- data/papers-source.html: three searchable Paper Explorer entries and a 2023 timeline card.
- article/2active.tex: IIC after foveated/correlation imaging; weak echo extraction before photon-arrival windowing; fixed spiral directly before adaptive spiral scanning.
- bare_jrnl.tex: unchanged, because its existing \input{article/2active.tex} and \bibliography{egbib_merged_20260711} already incorporate the three papers. The main-file comment edit was blocked, but no source content is missing.
- egbib_merged_20260711.bib: three complete DOI-verified BibTeX entries.

## Validation and PDF

All three new citation keys occur in article/2active.tex and the merged BibTeX. Website JavaScript syntax was validated. The previous PDF Git blob was `6fc5e00f2a7aee93692f6ee41a7074a4c59de9e6`.

**bare_jrnl.pdf has not been rebuilt.** This execution environment has pdflatex but cannot resolve github.com to retrieve the complete checkout and image assets. On a complete checkout, run pdflatex, bibtex, pdflatex, pdflatex, check missing assets and unresolved references, and upload the regenerated PDF binary. Do not describe PDF/source consistency as complete until the new PDF is compiled and verified.
