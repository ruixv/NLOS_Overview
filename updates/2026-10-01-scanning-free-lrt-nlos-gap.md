# 2026-10-01 gap: scanning-free laser reflective tomography for 3.3-km NLOS imaging

## Verified missing paper

Zewei Wang, Xiaoyin Li, Yinghui Guo, Hengshuo Guo, Peng Yang, Fei Zhang, Mingbo Pu, Mingfeng Xu, and Xiangang Luo, “Breaking the speed-resolution trade-off in 3.3-km non-line-of-sight imaging using scanning-free laser reflective tomography,” *Opto-Electronic Science*, vol. 5, no. 6, 260007, 2026. DOI: 10.29026/oes.2026.260007.

Final venue is verified as Opto-Electronic Science (2026); do not label this as arXiv.

## Why it belongs

The work adapts laser reflective tomography (LRT) to NLOS imaging. Instead of densely scanning a relay wall, it uses the diffuse relay surface as a natural beam expander, records third-bounce light with single-point detection, and uses multi-angle projections plus tomographic reconstruction. Reported experiments show about 2x spatial-resolution improvement and 91x imaging-speed improvement relative to the paper's scanning baseline, and demonstrate 3.3-km NLOS imaging with ~3-cm resolution in ~3 minutes. It is therefore a useful milestone in the trajectory from scanning ToF NLOS toward scanning-free, kilometer-scale practical systems.

## Repository check

Before staging, repository-wide default-branch searches for the exact DOI and distinctive phrase “laser reflective tomography” returned no matches.

## Integration plan

- README.md: add under 2026 active/long-range/practical NLOS and the development timeline; concise summary should emphasize scanning-free LRT, single-point detection, and the 3.3-km demonstration.
- index.html / Paper Explorer / Latest Additions: add a 2026 active optical NLOS entry and timeline milestone.
- bare_jrnl.tex: integrate semantically in the active-ToF / practical long-range systems discussion, preferably near kilometer-scale, scan-free, and acquisition-efficiency work. Explain that LRT replaces dense relay-wall spatial scanning with tomographic angular diversity and thus changes the acquisition trade-off rather than merely changing the reconstruction network.
- Bibliography: merge the verified entry staged in `egbib_20261001_lrt_nlos_gap.bib` into the canonical bibliography used by bare_jrnl.tex.
- bare_jrnl.pdf: rebuild only after the source and canonical bibliography are safely integrated; do not claim the PDF is current until compilation succeeds.

## Consistency status

This run intentionally did not overwrite large canonical files without a complete safe read/edit/validation cycle. Until integration and compilation are completed, this note and the staged BibTeX entry explicitly document the remaining consistency gap.
