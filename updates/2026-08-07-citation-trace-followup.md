# 7 August 2026 citation-trace follow-up

## Scope and repository state

This follow-up audit was run against the current public `master` state after the 6 August synchronization. At the time of this audit, `README.md` and `index.html` still reported an update date of 6 August 2026, and the website paper explorer reported 257 tracked latest entries. The most recent verified direct NLOS-imaging publication found in the fresh search remains **Iterating the transient light transport matrix for non-line-of-sight imaging**, *Nature Communications* (published 22 July 2026; DOI `10.1038/s41467-026-75177-4`). No higher-confidence direct NLOS imaging paper published after that date was verified in this pass.

The search combined fresh keyword/modality queries with forward-citation and lineage tracing around the repository's core active, passive, learned, acoustic, RF/mmWave, and transient-imaging milestones. Candidates were retained only when the work is genuinely NLOS imaging/sensing or tightly adjacent hidden-scene reconstruction, and when bibliographic metadata could be independently verified.

## Verified missing records for integration

### Acoustic NLOS

1. **Non-line-of-sight sound source localization based on block sparse Bayesian learning and second-order edge diffraction** — Qingbo Zhai, Fangli Ning, Juan Wei, Zhaojing Su. *Applied Acoustics* 228, 110369 (2025). DOI: `10.1016/j.apacoust.2024.110369`.
   - Direct passive acoustic NLOS localization.
   - Builds the sensing matrix from the Biot–Tolstoy–Medwin second-order edge-diffraction response and solves the inverse problem with block sparse Bayesian learning.
   - This is complementary to the first-order edge-diffraction localization paper already present in the repository and should be placed next to that lineage.

### RF / mmWave NLOS

2. **Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar** — Mingu Jeon et al. *2025 IEEE Intelligent Vehicles Symposium (IV)*, 1779–1786 (2025). DOI: `10.1109/IV64158.2025.11097630`.
   - Direct outdoor mmWave NLOS localization.
   - Infers static layout from radar returns and ray-traces dynamic multipath to localize multiple hidden targets around a T-junction.

3. **BiScalar-AA: BiScalar Attentive Amplifier Network for NLOS Object Detection and Tracking Using Millimeter-Wave Radar** — Yang Yu, Shijie Hu, Junaid Abdul Wahid, Han Zhang, Qiujie Lv, Yazhou Hu. *2025 IEEE Smart World Congress (SWC)*, 886–893 (2025). DOI: `10.1109/SWC65939.2025.00144`.
   - Direct learned mmWave NLOS detection/tracking.
   - Converts sparse radar point clouds into pseudo-images and uses attention-based amplification for hidden-object perception in dynamic scenes.

4. **Two-Stage Attention Network for NLOS Object Detection and Tracking Using mmWave Radar** — Yang Yu, Shijie Hu, Kangkang Fan, Wei Guo, Yazhou Hu, Dawei Zhang. *Computer Engineering* (online first, 9 September 2025). DOI: `10.19678/j.issn.1000-3428.0252481`.
   - Direct mmWave NLOS object detection/tracking.
   - Uses a two-stage attention architecture on radar pseudo-images. The journal record is distinct from BiScalar-AA, although the two works are closely related and should be cross-referenced rather than presented as unrelated developments.

5. **CornerRadar: RF-Based Indoor Localization Around Corners** — Shichao Yue, Hao He, Peng Cao, Kaiwen Zha, Masayuki Koizumi, Dina Katabi. *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies* 6(1), Article 34 (2022). DOI: `10.1145/3517226`.
   - Historical RF NLOS localization milestone.
   - Uses learned propagation hints to localize people around corners across varied indoor layouts.

6. **Mosaic: Leveraging Diverse Reflector Geometries for Omnidirectional Around-Corner Automotive Radar** — Timothy Woodford, Xinyu Zhang, Eugene Chai, Karthikeyan Sundaresan. *ACM MobiSys 2022*, 155–167. DOI: `10.1145/3498361.3538944`.
   - Historical automotive-radar NLOS milestone.
   - Exploits diverse and curved reflector geometries to expand around-corner radar coverage beyond simple planar-wall assumptions.

7. **Around the Corner mmWave Imaging in Practical Environments** — Laura Dodds, Hailan Shanbhag, Junfeng Guan, Saurabh Gupta, Haitham Hassanieh. *ACM MobiCom 2024*, 953–967. DOI: `10.1145/3636534.3690671`.
   - Major practical mmWave NLOS imaging milestone (RFlect).
   - Uses environmental reflectors including poles and curved/composite surfaces to reconstruct hidden object shape in realistic environments.

8. **Non-Line-of-Sight 3D Object Reconstruction via mmWave Surface Normal Estimation** — Laura Dodds, Tara Boroushaki, Kaichen Zhou, Fadel Adib. *ACM MobiSys 2025*, 445–458. DOI: `10.1145/3711875.3729138`.
   - Direct hidden-object 3D reconstruction (mmNorm).
   - Estimates mmWave-derived surface-normal fields and integrates them into 3D shape recovery, extending RF NLOS from location/occupancy to object geometry.

9. **Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion** — Laura Dodds, Maisy Lam, Waleed Akbar, Yibo Cheng, Fadel Adib. *CVPR 2026*, 21713–21724.
   - Final venue verified; do not label as arXiv.
   - Physics-aware transformer-based wireless shape completion reconstructs complete 3D geometry of fully occluded objects from mmWave measurements.

10. **RISE: Single Static Radar-based Indoor Scene Understanding** — Kaichen Zhou, Laura Dodds, Sayed Saad Afzal, Fadel Adib. *CVPR 2026*, 32194–32205.
    - Final venue verified; do not label as arXiv.
    - Exploits AoA/AoD and multipath geometry from a single static radar to infer otherwise invisible indoor structures, layout, and objects.

### Adjacent theory / performance bounds

11. **A Renderer-Enabled Framework for Computing Parameter Estimation Lower Bounds in Plenoptic Imaging Systems** — Abhinav V. Sambasivan, Liam J. Coulter, Richard G. Paxman, Jarvis D. Haupt. arXiv:2602.00215 (2026); no final journal/conference venue verified.
    - Closely adjacent theory rather than a new reconstruction algorithm.
    - Particular focus is passive indirect/NLOS imaging; renderer-defined forward models are used to compute parameter-estimation lower bounds for hidden-object localization.
    - Keep this in a theory/performance-bounds subsection rather than mixing it with direct imaging methods.

## Final-venue corrections already identified but still not public on master

A separate guarded updater already records four venue corrections that should be applied at the same time as the missing-paper integration:

- **Dual-branch Graph Feature Learning for NLOS Imaging (DG-NLOS)** → *AAAI 2025*, Proceedings of the AAAI Conference on Artificial Intelligence 39(7), 7051–7059. DOI `10.1609/aaai.v39i7.32757`.
- **Enhancing Autonomous Navigation by Imaging Hidden Objects Using Single-Photon LiDAR** → *IEEE ICRA 2025*, 4907–4914. DOI `10.1109/ICRA55743.2025.11128292`.
- **TransiT: Transient Transformer for Non-line-of-sight Videography** → *ICCV 2025*, 27542–27551; use the CVF final-paper page as the primary public link, retaining arXiv:2503.11328 only as an auxiliary source if desired.
- **NLOS-NeuS: Non-line-of-sight Neural Implicit Surface** → *ICCV 2023*, 10532–10541. DOI `10.1109/ICCV51070.2023.00966`; use the CVF final-paper page as the primary link.

## Precise integration plan

### `README.md`

- Insert the new acoustic paper next to the existing first-order edge-diffraction acoustic localization record.
- Add `CornerRadar` and `Mosaic` to the historical RF/mmWave development lineage (2022).
- Add `RFlect` to the 2024 RF/mmWave milestone block.
- Add mmNorm, the IV T-junction localization paper, BiScalar-AA, and the Two-Stage Attention Network to the 2025 RF/mmWave branch.
- Add Wave-Former and RISE to the 2026 RF/learned-reconstruction branch.
- Put the renderer lower-bounds paper in a clearly labeled adjacent-theory/performance-bounds category.
- Apply the four final-venue corrections above and update the run date only after all public artifacts have passed consistency checks.

### `index.html`

- Add corresponding searchable `paperData` records with the same titles, venues, URLs, and concise descriptions used in README.
- Extend the timeline with 2022 (`CornerRadar`, `Mosaic`), 2024 (`RFlect`), 2025 (mmNorm, IV T-junction localization, BiScalar-AA / TSAN, second-order acoustic diffraction), and 2026 (Wave-Former, RISE, optional renderer lower-bounds theory).
- The current explorer reports **257** tracked latest entries. Adding the ten direct/tightly related records gives **267**. If the adjacent renderer-theory paper is also included in the explorer, the count should become **268**. Recompute from `paperData` rather than hard-coding a number if possible.

### Survey source

- `article/5newscenes.tex`: integrate the second-order acoustic paper in the Acoustic NLOS subsection; integrate `CornerRadar`, `Mosaic`, `RFlect`, mmNorm, the IV T-junction method, BiScalar-AA, TSAN, RISE, and Wave-Former into the RF/mmWave / emerging-modality discussion in chronological order.
- Passive/theory subsection (whichever existing survey section discusses passive inverse-problem limits): add the renderer-enabled lower-bound paper as an adjacent performance-bound contribution, explicitly distinguishing it from reconstruction methods.
- `article/4datadriven.tex`: apply the AAAI 2025 DG-NLOS venue correction in prose if it is still described as an arXiv work.
- `article/5newscenes.tex`: identify the single-photon-LiDAR autonomous-navigation paper as ICRA 2025 if it is still described only as a preprint.
- `bare_jrnl.tex`: update the coverage date only after the included article files and bibliography are synchronized.

### Bibliography

Add/update entries in the canonical bibliography source(s) and regenerate the merged bibliography used by `bare_jrnl.tex`. Minimal verified metadata follows.

```bibtex
@article{zhaiSecondOrderAcousticNLOS2025,
  author = {Zhai, Qingbo and Ning, Fangli and Wei, Juan and Su, Zhaojing},
  title = {Non-line-of-sight sound source localization based on block sparse Bayesian learning and second-order edge diffraction},
  journal = {Applied Acoustics},
  volume = {228},
  pages = {110369},
  year = {2025},
  doi = {10.1016/j.apacoust.2024.110369}
}

@inproceedings{jeonTJunctionMmWaveNLOS2025,
  author = {Jeon, Mingu and others},
  title = {Non-Line-of-Sight Multi-Target Localization in T-Junctions Using Ray Tracing of mmWave Radar},
  booktitle = {2025 IEEE Intelligent Vehicles Symposium (IV)},
  pages = {1779--1786},
  year = {2025},
  doi = {10.1109/IV64158.2025.11097630}
}

@inproceedings{yuBiScalarAA2025,
  author = {Yu, Yang and Hu, Shijie and Abdul Wahid, Junaid and Zhang, Han and Lv, Qiujie and Hu, Yazhou},
  title = {BiScalar-AA: BiScalar Attentive Amplifier Network for NLOS Object Detection and Tracking Using Millimeter-Wave Radar},
  booktitle = {2025 IEEE Smart World Congress (SWC)},
  pages = {886--893},
  year = {2025},
  doi = {10.1109/SWC65939.2025.00144}
}

@article{yuTSANNLOS2025,
  author = {Yu, Yang and Hu, Shijie and Fan, Kangkang and Guo, Wei and Hu, Yazhou and Zhang, Dawei},
  title = {Two-Stage Attention Network for NLOS Object Detection and Tracking Using mmWave Radar},
  journal = {Computer Engineering},
  year = {2025},
  doi = {10.19678/j.issn.1000-3428.0252481},
  note = {Online first, published 9 September 2025}
}

@article{yueCornerRadar2022,
  author = {Yue, Shichao and He, Hao and Cao, Peng and Zha, Kaiwen and Koizumi, Masayuki and Katabi, Dina},
  title = {CornerRadar: RF-Based Indoor Localization Around Corners},
  journal = {Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies},
  volume = {6},
  number = {1},
  articleno = {34},
  year = {2022},
  doi = {10.1145/3517226}
}

@inproceedings{woodfordMosaic2022,
  author = {Woodford, Timothy and Zhang, Xinyu and Chai, Eugene and Sundaresan, Karthikeyan},
  title = {Mosaic: Leveraging Diverse Reflector Geometries for Omnidirectional Around-Corner Automotive Radar},
  booktitle = {Proceedings of the 20th Annual International Conference on Mobile Systems, Applications and Services (MobiSys)},
  pages = {155--167},
  year = {2022},
  doi = {10.1145/3498361.3538944}
}

@inproceedings{doddsRFlect2024,
  author = {Dodds, Laura and Shanbhag, Hailan and Guan, Junfeng and Gupta, Saurabh and Hassanieh, Haitham},
  title = {Around the Corner mmWave Imaging in Practical Environments},
  booktitle = {Proceedings of the 30th Annual International Conference on Mobile Computing and Networking (MobiCom)},
  pages = {953--967},
  year = {2024},
  doi = {10.1145/3636534.3690671}
}

@inproceedings{doddsMmNorm2025,
  author = {Dodds, Laura and Boroushaki, Tara and Zhou, Kaichen and Adib, Fadel},
  title = {Non-Line-of-Sight 3D Object Reconstruction via mmWave Surface Normal Estimation},
  booktitle = {Proceedings of the 23rd Annual International Conference on Mobile Systems, Applications and Services (MobiSys)},
  pages = {445--458},
  year = {2025},
  doi = {10.1145/3711875.3729138}
}

@inproceedings{doddsWaveFormer2026,
  author = {Dodds, Laura and Lam, Maisy and Akbar, Waleed and Cheng, Yibo and Adib, Fadel},
  title = {Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages = {21713--21724},
  year = {2026}
}

@inproceedings{zhouRISE2026,
  author = {Zhou, Kaichen and Dodds, Laura and Afzal, Sayed Saad and Adib, Fadel},
  title = {RISE: Single Static Radar-based Indoor Scene Understanding},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages = {32194--32205},
  year = {2026}
}

@misc{sambasivanRendererBounds2026,
  author = {Sambasivan, Abhinav V. and Coulter, Liam J. and Paxman, Richard G. and Haupt, Jarvis D.},
  title = {A Renderer-Enabled Framework for Computing Parameter Estimation Lower Bounds in Plenoptic Imaging Systems},
  year = {2026},
  eprint = {2602.00215},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2602.00215}
}
```

Before finalizing the BibTeX, replace `and others` in the IV paper with the full verified author list from the IEEE/author metadata source.

## Build and validation checklist

After source integration:

1. Rebuild with `pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex`, `bibtex bare_jrnl`, then two additional `pdflatex` passes.
2. Fail on undefined citations/references.
3. Use `pdftotext -layout` to verify representative new titles/DOIs appear in the regenerated PDF.
4. Recompute and validate the website explorer count.
5. Render at least the first and last PDF pages and visually inspect them for build corruption.
6. Confirm every newly added paper is present in README, website explorer/timeline, semantically appropriate survey prose, bibliography, and regenerated PDF unless an explicit scope exception is documented.

## Limitation of this run

No blind replacement of `README.md`, `index.html`, `bare_jrnl.tex`, bibliography files, or `bare_jrnl.pdf` was performed in this run. The available repository write interface replaces complete text files, while the public artifacts are large and the current environment does not provide a safe local checkout + LaTeX build path for a transactional multi-file update. The existing guarded final-venue launcher on `master` also has not produced a generated public-artifact commit.

Accordingly, this note is the only repository change made in this follow-up pass. It records precise insertion locations, verified metadata, and the build/consistency procedure so that the next safe integration can update all public artifacts together. Open PR #115 should **not** be merged as a public synchronization in its current state because it contains integration machinery rather than the generated README/website/survey/PDF artifacts.
