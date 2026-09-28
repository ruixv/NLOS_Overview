# Integration gap: comprehensive ToF NLOS study (2026)

## Verified missing paper

Julio Marco, Adrian Jarabo, Ji Hyun Nam, Alberto Tosi, Diego Gutierrez, and Andreas Velten, **“A comprehensive study of time-of-flight non-line-of-sight imaging,”** arXiv:2603.09548, 2026.

- arXiv: https://arxiv.org/abs/2603.09548
- DBLP currently lists only CoRR/arXiv; no final conference or journal venue was verified as of 2026-09-28.
- Repository-wide exact-title search returned no result before this staging update.

## Why it belongs

This paper is directly about ToF NLOS imaging rather than a passing citation. It places representative reconstruction families under a common forward/inverse formulation, relates simplified models to Radon transforms and frequency-domain/phasor-field virtual-wave formulations, and compares methods using the same hardware setup and similar photon counts. Its central conclusion is useful for the survey: under equal hardware constraints, major reconstruction families share important limits in spatial resolution, visibility, and noise sensitivity, while method-specific parameters account for some differences.

## Required integration

1. **README.md** — add to the 2026 timeline / survey-and-benchmark or active-ToF section. Suggested summary: “Unified theoretical and experimental comparison of representative ToF NLOS methods under common forward models, hardware, and photon budgets; connects Radon/frequency-domain formulations with phasor-field virtual-wave optics.”
2. **index.html / Paper Explorer** — add with tags such as `Active NLOS`, `ToF`, `Benchmark`, `Survey/Comparison`, `Phasor Field`, `Radon Transform`, `2026`; include in latest/missing additions as appropriate.
3. **bare_jrnl.tex** — integrate semantically in the active ToF reconstruction/theory discussion, ideally after presenting LCT, f-k/Radon and phasor-field families. Use it to support a synthesis sentence that controlled same-hardware comparisons reveal shared resolution/visibility/noise limitations across reconstruction families and help separate algorithmic effects from acquisition constraints.
4. **Canonical bibliography** — merge the verified BibTeX staged in `egbib_20260928_tof_comprehensive_study.bib` without duplicating an existing key/title.
5. **bare_jrnl.pdf** — rebuild only after the canonical TeX and bibliography are integrated; verify the citation resolves and README/website/survey venue all remain `arXiv 2026` unless a final venue is later verified.

## Safety note

Do not infer a final venue from author affiliations or secondary aggregators. DBLP currently records the work as CoRR abs/2603.09548, so arXiv remains the verified venue/source.
