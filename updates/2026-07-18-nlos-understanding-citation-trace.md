# 18 July 2026 NLOS recognition and clustering citation-tracing update

This pass compared fresh scholarly-index, publisher, and citation-chain results against the current README, homepage paper explorer, timeline, modular LaTeX survey, and merged bibliography. It identified three direct or tightly adjacent NLOS understanding papers that were absent from the public repository snapshot.

## Verified additions

### Adaptive motion enhancement for passive non-line-of-sight action recognition

- Authors: Zhongqi Sun, Yuan Zhou, Shuwei Huo, Sun-Yuan Kung
- Final venue: *Neurocomputing*, volume 655, article 131372, 2025
- DOI: <https://doi.org/10.1016/j.neucom.2025.131372>
- Relevance: AME-Net recognizes hidden human actions from standard RGB video of a visible relay wall and introduces NLOS-Action, the first passive NLOS action-recognition benchmark, with 2,000 synthetic and more than 500 real videos.
- Survey placement: conventional-camera passive sensing and the learned recognition trajectory.

### Multi-view clustering for non-line-of-sight imaging with neighborhood consistency reweighting

- Authors: Yi Lin, Zuyuan Yang, Cikun Liu, Daoyuan Li
- Final venue: *Neurocomputing*, volume 683, article 133462, 2026
- DOI: <https://doi.org/10.1016/j.neucom.2026.133462>
- Relevance: NCR-MVC is explicitly designed for photon-corrupted NLOS reconstructions. It refines view-specific neighborhood graphs, suppresses perturbation-induced edges through a Huber-smoothed dual-consistency objective, adaptively reweights views, and provides closed-form alternating updates with convergence analysis.
- Citation tracing: its references directly include O'Toole et al.'s LCT, Velten et al. 2012, phasor-field virtual wave optics, NLOST, arbitrary illumination/detection NLOS, and the AME-Net paper above.
- Survey placement: learned NLOS understanding after reconstruction/recognition multi-task models.

### QSS-Net: A Quanta-State-Slot Network for Non-line-of-Sight Classification

- Authors: Yi Lin, Daoyuan Li, Zhengdong Zhu, Zuyuan Yang
- Final venue: *Machine Learning and Knowledge Engineering for Decision Making*, Springer Lecture Notes in Computer Science, FLINS-ISKE 2026, pages 27--40
- DOI: <https://doi.org/10.1007/978-981-92-2487-6_3>
- Relevance: the paper explicitly frames the continuing shift from complete 3D geometric recovery toward efficient semantic NLOS classification for time-sensitive applications. The repository summary remains deliberately conservative because only publisher metadata and the beginning of the abstract were publicly verifiable in this run.
- Survey placement: learned semantic classification, adjacent to shared NLOS feature embeddings and joint reconstruction/recognition.

## Freshness result

No verified direct NLOS imaging paper published after 15 July 2026 was found in this pass. The latest verified formal publication remains Rui Zhao et al., “Non-line-of-sight imaging via physics-informed cascade learning,” *JOSA A* 43(9), E9--E18, published 15 July 2026, DOI 10.1364/JOSAA.593401.

## Synchronization plan

The guarded synchronizer updates:

1. `README.md` latest additions and the milestone audit.
2. `index.html` paper explorer, tracked-entry count, and 2025/2026 timeline.
3. `article/3passive.tex` with a passive action-recognition table row and literature-review paragraph.
4. `article/4datadriven.tex` with a semantically placed recognition-and-clustering trajectory paragraph.
5. `egbib_merged_20260711.bib` through the existing deterministic bibliography merge script.
6. `bare_jrnl.pdf` through a clean LaTeX/BibTeX build and PDF text/render validation.

The workflow rejects missing or duplicated public entries, undefined citations, repeated or absent BibTeX records, stale homepage counts, and PDFs that do not contain the newly integrated review text.

A pull-request event is used for the final guarded execution so that workflow status and failure diagnostics remain inspectable before the trigger-only branch is closed.
