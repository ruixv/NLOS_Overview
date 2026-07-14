# 14 July 2026 citation-tracing update: fast NLOS transient simulation and benchmark

## Candidate and verification

**Fast Non-Line-of-Sight Transient Data Simulation and an Open Benchmark Dataset** — Yingjie Shi, Jinye Miao, Taotao Qin, Fuyao Cai, Yi Wei, Lingfeng Liu, Tongyao Li, Chenyang Wu, Huan Liang, Yuyang Yin, Lianfa Bai, Enlai Guo, and Jing Han.

- Current verified status: **arXiv 2025**, arXiv:2506.03747.
- No final journal or conference publication was verified in the current search, so the repository must not promote the paper beyond arXiv status.
- The paper is directly relevant to active transient NLOS rather than merely adjacent sensing. It derives an FFT-accelerated simulator from the confocal light-cone-transform forward model, models configurable geometry, temporal jitter, and Poisson noise, releases data for seven ShapeNet categories, and benchmarks LCT, phasor-field, f-k migration, and backprojection.
- Citation tracing confirms a direct technical connection to the repository's core seeds: O'Toole et al. LCT is used as the simulator's core model, and LCT, Liu et al. phasor fields, Lindell et al. f-k migration, and backprojection are evaluated as benchmark reconstruction methods.
- Exact-title, arXiv-ID, and author searches found no existing entry in README.md, index.html, survey sources, bibliography supplements, or update logs before this run.

## Planned synchronized placement

1. **README.md**: add a 2025 Latest Additions row and a 2025 milestone entry describing standardized, configurable transient simulation and benchmarking.
2. **index.html**: add a searchable `dataset active` paper object, increment tracked latest entries from 95 to 96, and expand the 2025 timeline.
3. **article/4datadriven.tex**: insert the paper into the Dataset subsection after the paragraph on NLOS transient renderers and NLOS-Track. The added literature-review sentence distinguishes the fast LCT/FFT benchmark simulator from physically complete Monte Carlo transient rendering.
4. **Bibliography**: merge `egbib_20260714_simbenchmark_updates.bib` into the consolidated bibliography using `scripts/merge_nlos_bibliography.py`.
5. **PDF**: perform a clean LaTeX/BibTeX rebuild, reject undefined citations or repeated BibTeX entries, validate the PDF with `pdfinfo` and `pdftotext`, and render every page before and after the build.

**Build status:** README, homepage/timeline, survey source, merged bibliography, and regenerated PDF were synchronized; clean build and citation/PDF checks passed.
