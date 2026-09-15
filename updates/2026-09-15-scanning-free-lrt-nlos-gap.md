# NLOS literature update: scanning-free laser reflective tomography

## Verified missing paper

Zewei Wang, Xiaoyin Li, Yinghui Guo, Hengshuo Guo, Peng Yang, Fei Zhang, Mingbo Pu, Mingfeng Xu, and Xiangang Luo, “Breaking the speed-resolution trade-off in 3.3-km non-line-of-sight imaging using scanning-free laser reflective tomography,” *Opto-Electronic Science*, vol. 5, no. 6, 260007, 2026. DOI: 10.29026/oes.2026.260007.

The paper adapts laser reflective tomography (LRT) to active NLOS imaging. Instead of densely scanning the relay wall, the diffuse wall acts as a natural beam expander and a single-point detector records third-bounce photons while target rotation supplies multi-angle projections for tomographic reconstruction. The reported experiments show about 2× higher spatial resolution and 91× faster imaging than the compared scanning approach in short-range tests, and demonstrate 3.3-km NLOS imaging with approximately 3-cm resolution in about 3 minutes.

## Recommended integration

- **README / development timeline:** place under 2026 active optical NLOS / practical long-range systems. Suggested summary: “Introduces scanning-free laser reflective tomography for NLOS imaging, using the relay wall as a natural beam expander and target-motion-derived angular projections; demonstrates 3.3-km hidden-scene reconstruction at ~3-cm resolution in ~3 min.”
- **Website / Paper Explorer / latest additions:** categorize as Active / Optical / Long-range / Tomographic reconstruction / Scanning-free acquisition.
- **Survey source:** integrate in the active-NLOS acquisition / practical-system discussion, near long-range and scanning-efficiency work. Suggested literature-review sentence: “A complementary route to practical long-range acquisition replaces dense relay-wall scanning with laser reflective tomography: Wang et al. exploit the diffuse wall as a natural beam expander and use target-induced angular projections for tomographic inversion, demonstrating kilometer-scale NLOS imaging while decoupling spatial resolution from relay-surface sampling density.”
- **Trajectory:** dense relay-wall scanning → sparse/structured sampling → scanning-free tomographic acquisition → kilometer-scale practical NLOS.
- **Bibliography:** merge `egbib_20260915_laser_reflective_tomography.bib` into the canonical bibliography and use the repository’s normal citation-key convention if renaming is required.
- **PDF:** rebuild `bare_jrnl.pdf` only after the canonical LaTeX and bibliography are safely synchronized.

## Consistency status

Repository title/DOI searches on 2026-09-15 returned no indexed occurrence of this paper before staging. Large public-facing files were not overwritten from partial/truncated content. This note is intentionally a safe staging patch until README, website, canonical survey source, bibliography, and PDF can be updated together and validated.
