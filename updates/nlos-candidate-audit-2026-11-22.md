# NLOS candidate audit — 2026-11-22

This is a staging note, **not** a claim of integration into README, website, survey, bibliography or PDF. Master was checked by full-file reads of README.md, data/papers-source.html, and article/5newscenes.tex on 2026-11-22; neither the exact title nor DOI below was present.

## Verified missing candidate — radar NLOS recognition (adjacent sensing)

**Non-Line-of-Sight Pedestrian Recognition Approach Using Multiple Reflections for Millimeter Wave Radar Sensing Applications.** *IEICE Transactions on Communications*, E108-B(11), 1338–1348 (2025), published 2025-06-03. DOI: [10.23919/transcom.2025EBP3011](https://doi.org/10.23919/transcom.2025EBP3011). Publisher metadata mirrored in [IEEE Xplore](https://ieeexplore.ieee.org/document/11023172).

Contribution: Classifies a pedestrian versus an artificial object in road-scene NLOS using multiple reflected returns of a 24-GHz mmWave radar, with SVM and LSTM classifiers. This is **hidden-target recognition, not 3D scene reconstruction**. Recommended category: Radar/RF — NLOS target detection and recognition, as adjacent sensing, rather than optical transient reconstruction.

Suggested integration: add a concise 2025 entry in README radar/RF development timeline and website paper catalog, with final IEICE venue and DOI; insert a short sentence into article/5newscenes.tex in the mmWave radar NLOS target sensing/localization subsection; add a publisher-verified BibTeX entry to the bibliography actually included by bare_jrnl.tex. Check authors against publisher before creating BibTeX. Do not edit bare_jrnl.tex alone if the content is included from article/5newscenes.tex. Rebuild and validate bare_jrnl.pdf before reporting a PDF update.

## Other leads and exclusions

- [Single-Radar Bilateral 3D Near-Field Imaging for Mobile Robots](https://arxiv.org/abs/2611.11296), submitted 2026-11-08: not found by title/arXiv ID in README, website or article/5newscenes.tex. However its abstract describes bilateral **near-field LOS radar reconstruction**, not clearly a hidden NLOS target. **Do not add** without reading the full paper and verifying actual NLOS geometry.
- [3D transient wind camera incorporating 20 × 5 time-division multiplexing MIMO Doppler lidar](https://pubmed.ncbi.nlm.nih.gov/43024475/), *Optics Letters*, online 2026-10-09: wind-field lidar, not around-corner NLOS; exclude.
- [Vortex Coherence Filtering for Enhanced Single-Photon LiDAR Imaging Through Dense Fog](https://doi.org/10.1002/lpor.202502976), 2026: fog-penetrating LOS imaging, not NLOS; exclude.
- Qiu et al., [Simulation-Driven Approach for Occlusion-Based Non-Line-Of-Sight Detection Using a Low-Cost Flash LiDAR](https://arxiv.org/abs/2611.04068): previously staged on audit/flash-lidar-integration-20261117; do not duplicate. Its existing branch/PR requires build and cross-artifact verification.

## Publication and validation status

No large file was overwritten. This note stages a verified candidate for guarded integration. README.md, data/papers-source.html, bare_jrnl.tex, bibliography and bare_jrnl.pdf are **not** claimed to have been updated. Citation tracing across all core papers and complete PDF compilation remain pending.
