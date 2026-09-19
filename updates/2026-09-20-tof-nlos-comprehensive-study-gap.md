# 2026-09-20 gap: comprehensive ToF NLOS study

## Verified missing work

Julio Marco, Adrian Jarabo, Ji Hyun Nam, Alberto Tosi, Diego Gutierrez, and Andreas Velten, **“A comprehensive study of time-of-flight non-line-of-sight imaging,”** arXiv:2603.09548 (2026).

As of 2026-09-20, arXiv and DBLP/CoRR are the verifiable publication records; no final conference/journal venue was verified, so the venue should remain **arXiv 2026** until a final publication is confirmed.

## Why it belongs

This is not a generic survey. It places representative ToF NLOS reconstruction families under a common forward/inverse formulation and, importantly, evaluates them on hidden scenes acquired with the same hardware setup and similar photon counts. It connects Radon-transform/light-cone formulations, frequency-domain migration, and phasor-field virtual-wave models, and reports shared limitations in spatial resolution, visibility, and noise sensitivity under controlled hardware constraints. Because the author team includes major contributors to phasor-field and transient NLOS, it is also directly connected to the repository’s Core-paper lineage.

## Integration locations

- **README.md:** add to 2026/latest additions and to Active / Transient / Benchmark & Analysis (or closest existing category). Contribution summary: “Controlled same-hardware comparison and common formulation of representative ToF NLOS reconstruction families; relates Radon/LCT, frequency-domain, and phasor-field models and exposes shared resolution/visibility/noise limits.”
- **index.html / paper explorer:** add as a 2026 Active + Transient + Benchmark/Analysis item; timeline wording should emphasize standardized comparison rather than a new reconstruction algorithm.
- **bare_jrnl.tex:** integrate in the active ToF reconstruction overview / comparative discussion, ideally after the exposition of LCT, f-k migration, and phasor-field families. Suggested literature-review sentence: “A recent controlled study unified representative ToF NLOS methods under a common forward model and evaluated them using the same acquisition hardware and comparable photon budgets, showing that several apparently different inversion families share fundamental limits in resolution, visibility, and noise sensitivity.”
- **Bibliography:** merge `egbib_20260920_tof_nlos_comprehensive_study.bib` into the canonical bibliography, preserving arXiv as venue until a final publication is verified.
- **bare_jrnl.pdf:** rebuild only after the canonical TeX/Bib changes are safely integrated.

## Consistency note

This staging note exists because the large canonical README/index/TeX/Bib artifacts should not be overwritten from truncated connector payloads. The paper is not considered fully integrated until README.md, index.html, bare_jrnl.tex, canonical bibliography, and rebuilt bare_jrnl.pdf are mutually consistent.
