# 2026-09-21 NLOS literature integration patch: LRT, laser-pulse multiplexing, and PICL

This patch records three verified papers absent from the repository default branch at discovery time. They should be integrated into the canonical README, website/paper explorer/timeline, `bare_jrnl.tex`, and canonical bibliography before rebuilding `bare_jrnl.pdf`. Verified BibTeX is staged in `egbib_20260921_lrt_lpm_picl.bib`.

## 1. Scanning-free laser reflective tomography at 3.3 km

**Zewei Wang, Xiaoyin Li, Yinghui Guo, Hengshuo Guo, Peng Yang, Fei Zhang, Mingbo Pu, Mingfeng Xu, Xiangang Luo. “Breaking the speed-resolution trade-off in 3.3-km non-line-of-sight imaging using scanning-free laser reflective tomography.” Opto-Electronic Science 5(6), 260007 (2026). DOI: 10.29026/oes.2026.260007.**

Contribution: adapts laser reflective tomography (LRT) to NLOS by using the diffuse relay wall as a natural beam expander and single-point third-bounce detection, avoiding conventional large-area relay-wall scanning. The reported experiments show roughly 2x spatial-resolution improvement and 91x acquisition-speed improvement in short-range comparisons, and demonstrate 3.3-km NLOS reconstruction with ~3-cm resolution in ~3 minutes. This is a strong practical long-range / scanning-free active-NLOS milestone.

Suggested integration: README active optical / long-range / practical acquisition; 2026 timeline; website paper explorer. In `bare_jrnl.tex`, place near discussions of scan-free, long-range, photon-efficient, and practical active ToF acquisition, emphasizing the shift from dense relay-wall scanning toward tomography-based stand-off NLOS.

## 2. Laser-pulse multiplexing for temporal super-resolution

**Jinye Miao, Yingjie Shi, Fuyao Cai, Yi Wei, Lingfeng Liu, Lianfa Bai, Enlai Guo, Jing Han. “Super-resolution non-line-of-sight imaging with laser pulses multiplexing.” Optics and Lasers in Engineering 199, 109558 (2026). DOI: 10.1016/j.optlaseng.2025.109558.**

Contribution: uses laser-pulse multiplexing / temporal coding to recover higher-resolution transient information than the detector's native single-photon timing resolution, targeting the hardware timing-resolution bottleneck without requiring a higher-end detector. It extends the temporal-super-resolution line represented by earlier temporal-encoding and oversampled-transient approaches.

Suggested integration: README active/transient hardware-computation co-design; 2026 timeline; website paper explorer. In `bare_jrnl.tex`, place in the transient acquisition / SPAD timing / temporal-super-resolution discussion, alongside consumer/low-cost SPAD and timing-calibration work rather than generic learned reconstruction.

## 3. Physics-informed cascade learning (PICL)

**Rui Zhao, Yifan He, Yi-Ming Lin, Rui Chen. “Non-line-of-sight imaging via physics-informed cascade learning.” Journal of the Optical Society of America A 43(9), E9–E18 (2026). DOI: 10.1364/JOSAA.593401. Published 15 July 2026.**

Contribution: a two-stage physics-informed learning framework for low-SNR SPAD-based NLOS. Net1 performs SPAD-specific mixed-noise separation; Net2 embeds a differentiable forward model for self-supervised reconstruction. The design explicitly couples detector-noise modeling with physics-consistent inversion and avoids requiring large paired NLOS training sets.

Suggested integration: README learned / physics-guided reconstruction; 2026 timeline; website paper explorer. In `bare_jrnl.tex`, place with physics-guided/unrolled/self-supervised NLOS methods, highlighting the trajectory from black-box reconstruction toward detector-aware and differentiable-forward-model supervision.

## Consistency / build status

These entries are staged only because the canonical README, website, survey source, and bibliography are large and should not be overwritten from partial payloads. Do not claim `bare_jrnl.pdf` is updated until the entries are merged into the canonical sources, LaTeX compilation succeeds, and the resulting PDF is committed and checked. After canonical integration, verify title/venue/category consistency across README, `index.html`, `bare_jrnl.tex`, bibliography, and PDF, then remove or retain this patch as an update log according to repository convention.
