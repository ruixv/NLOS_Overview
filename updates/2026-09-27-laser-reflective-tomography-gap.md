# Integration note — scanning-free laser reflective tomography NLOS (2026-09-27)

## Verified missing paper

Zewei Wang, Xiaoyin Li, Yinghui Guo, Hengshuo Guo, Peng Yang, Fei Zhang, Mingbo Pu, Mingfeng Xu, and Xiangang Luo, “Breaking the speed-resolution trade-off in 3.3-km non-line-of-sight imaging using scanning-free laser reflective tomography,” *Opto-Electronic Science* (2026), DOI: 10.29026/oes.2026.260007.

Verified against the publisher-linked record/news release. The article was available online in May 2026. Repository-wide exact-title and distinctive-phrase searches returned no hit on the default branch before staging.

## Why it belongs

This is a direct optical NLOS imaging paper, not merely adjacent long-range LiDAR. It adapts laser reflective tomography (LRT) to third-bounce NLOS transport. Instead of densely scanning the relay wall, it uses the diffuse relay surface as a natural beam expander, performs single-point detection, and reconstructs the hidden target from multi-angle projection/range data with tomography. Reported experiments include roughly 2× spatial-resolution improvement and 91× imaging-speed improvement over the compared scanning approach, plus 3.3-km NLOS imaging with about 3-cm resolution in roughly 3 minutes.

The trajectory is useful for the survey: dense relay-wall scanning / LCT–f-k–phasor reconstruction -> sparse and scanning-efficient acquisition -> scanning-free tomographic NLOS -> kilometer-scale practical deployment.

## Canonical integration plan

- **README.md — Latest Additions / 2026 timeline:** add under active optical NLOS / practical hardware and acquisition. Suggested one-line summary: “Adapts laser reflective tomography to scanning-free third-bounce NLOS, using a diffuse relay wall as a natural beam expander and single-point detection; demonstrates 3.3-km reconstruction at ~3-cm resolution in ~3 min.”
- **README taxonomy:** cross-tag Active NLOS, Hardware/Acquisition, Reconstruction Algorithms, Long-range / practical NLOS.
- **index.html / Paper Explorer:** add searchable tags `Active`, `Optical`, `ToF`, `Laser Reflective Tomography`, `Scanning-free`, `Long-range`, `3.3 km`, `2026`; include in Latest Additions and 2026 timeline.
- **bare_jrnl.tex:** integrate semantically in the active ToF/practical-system discussion near sparse scanning, acquisition-efficiency, long-range and real-world deployment papers. A useful literature-review sentence is: “Beyond accelerating inversion after dense transient acquisition, scanning-free laser reflective tomography repurposes the diffuse relay surface as a natural beam expander and recovers hidden targets from single-point third-bounce detection and multi-angle projections, extending active NLOS demonstrations to kilometer-scale stand-off distances.”
- **Bibliography:** merge the verified entry staged in `egbib_20260927_laser_reflective_tomography.bib` into the bibliography actually used by `bare_jrnl.tex`, preserving the repository's citation-key convention.
- **PDF:** after canonical source integration, compile `bare_jrnl.tex`, inspect warnings/references, regenerate `bare_jrnl.pdf`, and verify README/index/TeX/bibliography/PDF consistency before claiming completion.

## Reliability note

The current README is a very large single JSON content field through the connector and was truncated during retrieval. To avoid replacing a canonical file from partial content, this run intentionally staged verified metadata plus precise insertion instructions rather than performing an unsafe whole-file overwrite. Canonical integration and PDF rebuild remain outstanding until the complete files can be fetched/edited safely.
