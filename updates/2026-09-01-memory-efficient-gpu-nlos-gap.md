# 2026-09-01 — Memory-efficient GPU NLOS reconstruction gap

## Verified missing paper

**Alfonso López-Ruiz and Diego Royo, “Memory-efficient GPU pipelines for real-time non-line-of-sight reconstruction,” arXiv:2608.28183 (2026).**

- arXiv: https://arxiv.org/abs/2608.28183
- First submitted: 28 August 2026
- Venue status checked on 1 September 2026: no final conference or journal venue could be verified; keep **arXiv** as the venue/status.
- Repository deduplication: exact-title and arXiv-ID searches returned no hit in the current default branch.

## Why this paper belongs in the survey

This is a direct active/transient NLOS reconstruction paper, not a citation-in-passing result. It rebuilds the GPU execution of two milestone wave-based NLOS algorithms—**f-k migration** and **phasor fields**—for both streaming and offline processing. It therefore sits directly on the forward-citation/successor line of the Lindell et al. f-k and Liu et al. phasor-field core papers.

The contribution is systems-oriented: fused CUDA kernels, warp-level photon binning, batched transforms, CUDA graph replay, selective FP16 storage, and an offline ring/radius construction that avoids materializing a dense phasor-field propagation kernel at runtime. The authors report up to **42×** speedup over their reference streaming pipeline, up to **14×** over the fastest published GPU baseline used in their comparison, and memory usage as low as **2.5%** of that baseline in some settings. The paper also proposes denoising strategies enabled by the resulting frame budget.

This paper makes explicit an emerging practical transition in NLOS imaging:

> fast analytical inversion → GPU/FPGA acceleration → high-throughput SPAD arrays → reconstruction throughput and GPU-memory becoming the system bottleneck.

## Required public-artifact integration

Because the available GitHub write interface requires whole-file replacement for existing large text files, while direct full-file retrieval is truncated in this environment, **README.md, index.html, bare_jrnl.tex, and the canonical bibliography were not overwritten in this run**. Doing so from partial content would risk data loss. This note gives precise insertion targets for a safe later integration.

### README.md

1. **Latest Additions**: insert near the top of the 2026 active/transient entries:

```markdown
| 2026 | [Memory-efficient GPU pipelines for real-time non-line-of-sight reconstruction](https://arxiv.org/abs/2608.28183) — López-Ruiz and Royo | arXiv 2026 | Re-engineers f-k migration and phasor-field reconstruction for streaming/offline GPU execution using fused kernels, warp-level photon binning, batched transforms, CUDA graphs, selective FP16 storage, and memory-efficient phasor kernels; reports up to 42× streaming speedup and major memory reductions, highlighting reconstruction throughput as the next bottleneck for high-rate SPAD-array NLOS. |
```

2. **Milestone Timeline / 2026**: place after recent real-time / acceleration papers such as MD-NLOS, GPU/FPGA phasor-field acceleration, or high-throughput SPAD-array entries.

3. **Active NLOS → Reconstruction Algorithms / Hardware & Systems**: cross-list under real-time/acceleration if the README uses such a subsection.

### Website (index.html / paper explorer / latest additions / timeline)

Add a 2026 entry categorized as:

- Active NLOS
- Transient / ToF
- Reconstruction acceleration
- GPU / real-time systems
- f-k migration / phasor field

Suggested short summary:

> GPU execution pipeline for f-k migration and phasor fields that reduces runtime memory traffic and kernel storage, shifting real-time NLOS toward high-throughput SPAD-array operation.

### bare_jrnl.tex

Integrate semantically in the discussion of **fast reconstruction / real-time NLOS / wave-based methods**, immediately after passages covering f-k migration, phasor fields, real-time spectral filtering, FPGA/GPU acceleration, or high-throughput SPAD arrays.

Suggested survey prose (adapt style to surrounding text):

```tex
As parallel SPAD arrays increase transient-acquisition throughput, reconstruction itself is becoming a systems bottleneck. López-Ruiz and Royo~\cite{lopezruizMemoryEfficientGPUNLOS2026} re-engineer the GPU execution of both $f$-$k$ migration and phasor-field reconstruction using fused CUDA kernels, warp-level photon binning, batched transforms, CUDA graph replay, selective half-precision storage, and an offline construction of the phasor propagation kernels. Their results show that algorithmic equivalence alone does not determine real-time performance: memory movement, kernel materialization, and execution scheduling can dominate the end-to-end NLOS pipeline. This systems-level trend complements recent work on sparse acquisition and parallel SPAD sensing, and suggests that future real-time NLOS cameras must co-design acquisition throughput with reconstruction memory bandwidth and latency.
```

### Canonical bibliography

Merge the following entry into the .bib source used by `bare_jrnl.tex`:

```bibtex
@misc{lopezruizMemoryEfficientGPUNLOS2026,
  title         = {Memory-efficient GPU pipelines for real-time non-line-of-sight reconstruction},
  author        = {L{\'o}pez-Ruiz, Alfonso and Royo, Diego},
  year          = {2026},
  eprint        = {2608.28183},
  archivePrefix = {arXiv},
  primaryClass  = {cs.DC},
  url           = {https://arxiv.org/abs/2608.28183}
}
```

A staging copy is committed as `egbib_20260901_gpu_pipeline_gap.bib`.

## PDF rebuild / consistency checklist

After integrating the source safely:

1. Run the repository's normal LaTeX build for `bare_jrnl.tex`.
2. Regenerate `bare_jrnl.pdf` rather than editing the binary directly.
3. Confirm `lopezruizMemoryEfficientGPUNLOS2026` resolves without an undefined citation.
4. Confirm title/year/status match in README, website, TeX, and BibTeX.
5. Keep the venue as **arXiv 2026** until a final accepted/published venue is independently verified.
6. Confirm the regenerated PDF contains the new literature-review sentence, not merely the bibliography entry.

## Search/citation-tracing notes

The run prioritized forward-successor searches around the LCT, f-k migration, phasor-field, computational-periscopy, Neural Transient Fields, NLOST, recent learned transient models, consumer LiDAR, acoustic and RF/mmWave branches. The GPU-pipeline paper was the only newly surfaced, high-confidence paper from the immediate Aug. 28–Sep. 1 window that was both directly NLOS-reconstruction-relevant and absent from the current repository search. Other prominent 2026 results returned by the search (e.g. MARMOT, MD-NLOS, stereo NLOS, recent thermal/passive/acoustic/SPAD works) are already represented in the repository or its current update lineage and were therefore not duplicated.
