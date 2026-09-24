# Integration gap: A comprehensive study of time-of-flight non-line-of-sight imaging

Verified on 2026-09-25.

## Paper
Julio Marco, Adrian Jarabo, Ji Hyun Nam, Alberto Tosi, Diego Gutierrez, Andreas Velten, “A comprehensive study of time-of-flight non-line-of-sight imaging,” arXiv:2603.09548, 2026.

No final conference/journal venue was verifiable in this run; DBLP still indexes it as CoRR, so retain arXiv as venue until a final publication is confirmed.

## Why it belongs
This is a directly relevant ToF-NLOS comparative/methodological study from authors of core NLOS work. It places representative reconstruction families under a common forward/inverse formulation, relates Radon-transform and frequency-domain/phasor formulations, and compares methods using common hardware and similar photon counts. Its equal-hardware analysis highlights shared limits in spatial resolution, visibility, and noise sensitivity and is useful as a modern reference/benchmark paper rather than a new reconstruction algorithm.

## Repository check
Repository-wide searches for the full title and distinctive author/title terms returned no match before staging.

## Canonical integration locations
- README.md: add under 2026 active/transient NLOS, preferably a Benchmark / Comparative Study / Theory-and-Evaluation entry; mention common formulation and equal-hardware comparison.
- index.html / paper explorer: add as 2026, Active/Transient, Benchmark/Comparative Study; include arXiv link and concise contribution summary.
- development timeline: place near recent practical/theoretical ToF work as a consolidation/benchmark milestone, not as a new modality.
- bare_jrnl.tex: integrate in the active ToF reconstruction discussion or evaluation/limitations discussion. Suggested literature-review point: recent work has unified representative ToF-NLOS inversions under a common forward model and controlled hardware/photon budget, showing that apparently different methods share fundamental resolution, visibility, and noise limitations while differing in method-specific parameterization.
- bibliography: merge the staged entry in `egbib_20260925_tof_nlos_comprehensive_study.bib` into the canonical bibliography used by bare_jrnl.tex.
- bare_jrnl.pdf: rebuild only after canonical TeX/bibliography integration.

## Consistency status
This staging note and BibTeX file are committed. README.md, index.html, bare_jrnl.tex, the canonical bibliography, and bare_jrnl.pdf are NOT claimed updated by this patch. Integrate them together when complete safe file payloads are available; do not overwrite large files from truncated content.
