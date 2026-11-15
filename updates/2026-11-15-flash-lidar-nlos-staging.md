# 2026-11-15 NLOS literature staging: low-cost flash LiDAR occlusion detection

## Verified candidate (requires integration)

Peizhao Qiu, Emmanuel A. Olowe, Zhenya Zang, Istvan Gyongy, and Danial Chitnis, **“Simulation-Driven Approach for Occlusion-Based Non-Line-Of-Sight Detection Using a Low-Cost Flash LiDAR,”** arXiv:2611.04068v1, submitted **2 November 2026**. https://arxiv.org/abs/2611.04068 . No final accepted/published venue independently verified on 15 November 2026; retain **arXiv** label pending verification. This is **hidden-target detection**, not full 3D hidden-scene reconstruction.

**Contribution and evidence:** photon-based Monte Carlo simulation trains a model to identify multibounce signatures of targets occluded by scene geometry. Uses commercial TMF8829 SPAD flash LiDAR. Reports AP 0.91 on synthetic tests and 86.67% accuracy / AP 0.95 on 180 measured samples without real-data retraining. This is a substantive low-cost NLOS sensing result, not merely a citation of prior NLOS imaging.

## Safe integration checklist (not yet applied)

- `README.md`: insert into **Latest Additions** and the **2026 development timeline**, under **active NLOS / commodity flash LiDAR / occlusion-based detection**, with explicit detection-vs-reconstruction caveat.
- `data/papers-source.html`: add a single Paper Explorer entry in the active/LiDAR category, retaining exact authors, arXiv URL, submission date, and contribution summary; ensure `index.html` latest-additions/timeline and displayed record count stay synchronized.
- `article/2active.tex`: insert a brief discussion alongside **commodity ToF/SPAD and consumer-LiDAR NLOS sensing**: unlike scanning-based 3D reconstruction, Qiu et al. learn occlusion-related multibounce signatures from photon-Monte-Carlo simulations and transfer to commercial flash LiDAR for binary hidden-target detection.
- `egbib_2026_updates.bib` and merged bibliography: add one accurate record (staged below) and ensure no duplicate key/DOI.
- Build `bare_jrnl.tex` using the repository's normal LaTeX/BibTeX workflow; verify citation key in `.aux`, no undefined citations, and regenerated `bare_jrnl.pdf` committed and deployed. Do **not** report PDF updated before a successful build and binary commit.

## BibTeX staging

```bibtex
@misc{qiuFlashLiDAROcclusionNLOS2026,
  author = {Qiu, Peizhao and Olowe, Emmanuel A. and Zang, Zhenya and Gyongy, Istvan and Chitnis, Danial},
  title = {Simulation-Driven Approach for Occlusion-Based Non-Line-Of-Sight Detection Using a Low-Cost Flash {LiDAR}},
  year = {2026},
  eprint = {2611.04068},
  archivePrefix = {arXiv},
  primaryClass = {eess.IV},
  url = {https://arxiv.org/abs/2611.04068},
  note = {Preprint submitted 2 November 2026; no final venue verified as of 15 November 2026}
}
```

## Audit limitations

Direct GitHub file reads were performed for README, website paper-source, and new-scenes survey chapter; targeted title/arXiv-ID checks found no existing catalog entry. This was a targeted discovery pass, not a complete forward-citation export for every milestone seed. No large repository files were overwritten, and the PDF was **not** rebuilt in this staging commit.
