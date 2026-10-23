# 2026-10-23 — LCT forward-citation backfill: absorption BP and ToF relay calibration

Two missing NLOS papers were identified among the works citing O'Toole, Lindell and Wetzstein's 2018 LCT paper (OpenAlex W2793604749, citing-works ranks 229 and 242). Both genuinely reconstruct hidden scenes, not merely cite NLOS in passing.

1. Hongyuan Zhou, Dejian Zhang, Tongbiao Wang, Qinghua Liao, Tianbao Yu, "Non-line-of-sight imaging with absorption backprojection," *Applied Physics Letters* **123**(5), 054001 (2023). DOI https://doi.org/10.1063/5.0156149. ABP suppresses ellipsoidal backprojection artifacts by concentrating low-confidence voxel responses into high-confidence structures. Article number corroborated in *Optics Express* 34(2), 3232–3243 (2026).
2. Yujie Fang, Xia Wang, Binghua Su, "Reconstruction of Non-Line-of-Sight Depth Data Using Genetic Algorithm-Lucy-Richardson Based on Time of Flight Camera" (Chinese title: 基于遗传-反卷积算法的飞行时间测距相机非视域成像), *Acta Optica Sinica* **43**(21), 2111002 (2023). DOI https://doi.org/10.3788/AOS230870. Genetic relay-scattering calibration and Lucy–Richardson deconvolution enable lower-cost ToF hidden-depth imaging on non-Lambertian relay materials. Verified against Beijing Institute of Technology's institutional record and the journal PDF.

Integrated in README.md Latest Additions and Milestone Timeline; index.html Core Reading Path; data/papers-source.html Latest/Paper Explorer/Timeline; article/2active.tex (modulated-ToF subsection for Fang; backprojection inverse discussion for Zhou); and egbib_merged_20260711.bib. The unchanged bare_jrnl.tex main file already includes article/2active.tex and the merged bibliography.

Screened but not added: Rethinapandian et al.'s RIS-enabled FMCW NLOS detection, which is described as an accepted WiSEE 2026 poster only on an author-hosted repository; independent publisher/proceedings verification was unavailable. It is adjacent target detection, not dense imaging.

**PDF not rebuilt:** The published bare_jrnl.pdf predates these additions. The execution container cannot access the complete repository and figure assets over the network. Recompile the existing LaTeX project with all figures, style files and BibTeX, then commit the new bare_jrnl.pdf. Do not report the PDF as synchronized until its binary blob is verified.
