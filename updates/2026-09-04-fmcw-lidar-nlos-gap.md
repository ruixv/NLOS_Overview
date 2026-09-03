# Verified NLOS gap — 4 September 2026

## New paper

**Shan Qian, Xingyu Jia, Weiwei Yang, Junzhe Qiang, Guanhao Wu. “High-speed non-line-of-sight imaging via predistorted FMCW LiDAR.” Proceedings of SPIE Photonics Europe 2026, Vol. 14083, paper 1408311. DOI: 10.1117/12.3101229.**

Official SPIE metadata confirms presentation on 14 April 2026 at Photonics Europe in Strasbourg. The work demonstrates a near-infrared FMCW-LiDAR NLOS system using a low-cost DFB laser and a predistortion procedure that corrects sweep nonlinearity. The reported single-frame NLOS acquisition time is about 0.2 s. The paper is directly relevant to practical active NLOS imaging and extends the system-design trajectory from pulsed/SPAD transient capture toward coherent FMCW ranging with eye-safe NIR hardware.

Repository exact-title and DOI searches returned no matches on 4 September 2026.

## Recommended README integration

### Latest Additions
Add a 2026 row:

| 2026 | [High-speed non-line-of-sight imaging via predistorted FMCW LiDAR](https://doi.org/10.1117/12.3101229) — Qian et al. | Proc. SPIE Photonics Europe 2026, 14083, 1408311 | Demonstrates fast near-infrared NLOS imaging with a low-cost FMCW LiDAR; predistorts the laser sweep to correct chirp nonlinearity and reports about 0.2 s single-frame acquisition, broadening practical NLOS hardware beyond pulsed-SPAD architectures. |

### Timeline / Hardware Devices
Place near other practical/real-time active NLOS hardware papers, especially scan-free SPAD, eye-safe compact NLOS, consumer-LiDAR and long-range systems.

Suggested summary sentence:

> Coherent-ranging hardware is also entering the NLOS design space: Qian et al. used predistorted near-infrared FMCW LiDAR to correct sweep nonlinearity and demonstrated roughly 0.2 s single-frame hidden-scene acquisition with a low-cost DFB laser, complementing pulsed-SPAD and consumer-LiDAR routes toward practical deployment.

## Recommended website integration

Add to the Paper Explorer with tags such as:

- year: 2026
- modality: optical / NIR / FMCW LiDAR
- task: active NLOS imaging
- theme: fast acquisition / coherent ranging / practical hardware
- venue: SPIE Photonics Europe 2026

Include in Latest Additions and the 2026 timeline alongside compact eye-safe NLOS, consumer LiDAR, scan-free transient imaging, and acquisition/reconstruction co-design.

## Recommended survey integration

Insert semantically in the active-NLOS hardware/acquisition discussion rather than appending a disconnected list. A suitable literature-review sentence is:

> Beyond pulsed time-correlated single-photon acquisition, coherent ranging is emerging as an alternative route to practical NLOS hardware. Qian et al. demonstrated near-infrared FMCW-LiDAR NLOS imaging with laser-sweep predistortion for chirp-linearity correction, reaching about 0.2 s single-frame acquisition with a low-cost DFB source \cite{qianHighSpeedNLOSFMCW2026}. This complements scan-free SPAD arrays, compact eye-safe emitters, and consumer-LiDAR systems by shifting part of the timing problem from picosecond photon counting to coherent frequency-domain ranging.

Potential placement: `article/2active.tex` hardware/acquisition subsection and corresponding material included by `bare_jrnl.tex`.

## Bibliography

Canonical entry to merge into the bibliography used by `bare_jrnl.tex`:

```bibtex
@inproceedings{qianHighSpeedNLOSFMCW2026,
  author    = {Shan Qian and Xingyu Jia and Weiwei Yang and Junzhe Qiang and Guanhao Wu},
  title     = {High-speed non-line-of-sight imaging via predistorted FMCW LiDAR},
  booktitle = {Proceedings of SPIE Photonics Europe 2026},
  volume    = {14083},
  pages     = {1408311},
  year      = {2026},
  doi       = {10.1117/12.3101229},
  note      = {Presented at SPIE Photonics Europe, Strasbourg, France, 14 April 2026},
  url       = {https://doi.org/10.1117/12.3101229}
}
```

## Consistency / build status

This run intentionally does **not** replace `README.md`, `index.html`, `bare_jrnl.tex`, or the canonical large `.bib` file through a partial read, because the available whole-file GitHub update operation requires complete replacement and large-file reads may be truncated. The verified BibTeX staging file `egbib_20260904_fmcw_lidar_gap.bib` and this insertion note are safe, non-destructive updates.

`bare_jrnl.pdf` has therefore **not** been regenerated in this run. After a safe full checkout or lossless full-file access is available, merge the staged entry, integrate the prose in the locations above, compile the survey, and verify README / website / TeX / bibliography / PDF consistency.
