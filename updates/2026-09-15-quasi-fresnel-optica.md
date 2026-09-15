# 2026-09-15 update — Quasi-Fresnel NLOS imaging

## Newly verified missing paper

Yijun Wei, Jianyu Wang, Leping Xiao, Zuoqiang Shi, Xing Fu, and Lingyun Qiu, **“Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform,” Optica 13, 1785 (2026)**, DOI: 10.1364/OPTICA.604217. Earlier version: arXiv:2508.02003 (2025).

This paper was absent from repository code search at this run. The final Optica venue is verified by Xing Fu’s Tsinghua publication page, which lists the paper as Optica 13, 1785 (2026) with DOI 10.1364/OPTICA.604217. Therefore the repository should label the final venue as Optica rather than arXiv.

## Contribution / timeline placement

The method observes that many hidden targets of interest can be represented as 2-D surfaces rather than full 3-D volumes. It derives a Quasi-Fresnel transform that directly maps aggregated transient measurements to a 2-D hidden-scene representation. This reduces the reported computational complexity to O(N^2 log N) and memory complexity to O(N^2), enabling orders-of-magnitude reductions in runtime and memory compared with volumetric NLOS reconstruction while retaining reconstruction quality.

Recommended development-line description:

**volumetric analytic inversion (LCT / f-k / phasor fields) → learned/optimized transient inversion → dimension-reduced direct inversion (Quasi-Fresnel) → lightweight / embedded real-time NLOS reconstruction.**

## Required integration when full-file-safe editing is available

1. **README.md** — add under 2026 Latest Additions and Active NLOS / Reconstruction Algorithms. Suggested concise summary: “Represents thin hidden scenes with 2-D functions and derives a direct Quasi-Fresnel inversion from aggregated transient measurements, reducing compute and memory by orders of magnitude and targeting real-time high-resolution reconstruction on lightweight devices.”
2. **index.html / Paper Explorer / timeline** — add as Active / analytic inverse / efficient reconstruction; mark venue Optica 2026, not arXiv.
3. **Survey LaTeX** — integrate semantically in the active reconstruction/fast analytic inversion discussion near LCT, f-k migration, phasor fields, and recent GPU/efficient reconstruction methods. Suggested literature-review sentence: “More recently, Wei et al. exploit the effectively two-dimensional structure of thin hidden scenes and derive a Quasi-Fresnel direct inversion, replacing volumetric processing with two-dimensional aggregation and transforms to reduce both runtime and memory by orders of magnitude, thereby shifting analytic NLOS reconstruction toward embedded and lightweight platforms.” Cite `wei2026quasifresnel`.
4. **Canonical bibliography** — merge `egbib_20260915_quasi_fresnel_optica.bib` into the bibliography actually used by the survey.
5. **bare_jrnl.pdf** — rebuild only after the source and canonical bibliography are synchronized; verify the new citation resolves and the PDF contains the new discussion.
6. **Consistency check** — ensure README, website, LaTeX source, canonical bibliography, and rebuilt PDF all use the final Optica 2026 venue and DOI.

Large public-facing files were not overwritten in this run because the connector returned README content through a truncated payload and whole-file replacement from partial content would risk destructive truncation. This staging note and verified BibTeX are intentionally committed as the safe recovery path.
