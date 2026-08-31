# 2026-08-31 NLOS update: memory-efficient GPU pipelines

## Verified missing paper

**Alfonso López-Ruiz and Diego Royo, “Memory-efficient GPU pipelines for real-time non-line-of-sight reconstruction,” arXiv:2608.28183 (2026).**

- Submitted: 28 Aug 2026.
- Current verified venue/status: arXiv only; no final conference/journal venue was verified in this run.
- arXiv: https://arxiv.org/abs/2608.28183
- arXiv DOI: https://doi.org/10.48550/arXiv.2608.28183
- Repository deduplication: exact-title and arXiv-ID searches returned no matches in `ruixv/NLOS_Overview`.

## Why it belongs in the survey

This is a direct active transient NLOS reconstruction/system paper rather than a peripheral citation. It explicitly rebuilds two milestone algorithms—Lindell et al. f-k migration and Liu et al. phasor-field reconstruction—for high-throughput, low-memory CUDA execution in both streaming and offline modes. The paper therefore emerged naturally from the high-priority forward-citation pass over Core papers.

Key reported contributions/results:

- GPU pipelines for both f-k migration and phasor fields.
- Fused kernels, warp-level photon binning, batched transforms, CUDA graph replay, and selective FP16 storage.
- Offline construction of ring-and-radius phasor kernels so the dense propagation kernel never exists at runtime.
- Up to 42× speed-up over the referenced streaming pipeline and up to 14× over the fastest published GPU baseline considered by the authors.
- Peak GPU memory reduced to as little as 2.5% of the compared baseline in volumetric experiments.
- Positions reconstruction throughput/memory, rather than only photon acquisition, as an emerging bottleneck as SPAD arrays scale.

Suggested short contribution summary:

> Re-engineers f-k migration and phasor-field NLOS reconstruction as memory-efficient CUDA pipelines, combining fused/streamed GPU execution with analytic ring-kernel construction to support substantially larger and faster volumetric reconstructions and future high-throughput SPAD-array capture.

## Integration locations

### README.md

1. **Latest Additions**: add a 2026 row near other active transient / hardware-acceleration / real-time papers.
2. **Milestone Timeline / 2026**: place after recent real-time/sparse/parallel-SPAD entries, emphasizing the shift from acquisition bottlenecks toward reconstruction-throughput and GPU-memory bottlenecks.
3. **Active NLOS Imaging → Reconstruction Algorithms** (or the existing acceleration/real-time subsection): group with fast back-projection, 5-FPS NLOS, FPGA acceleration, ring-and-radius phasor fields, Physics to the Rescue, and CUDA irregular-relay reconstruction.

Recommended timeline phrasing:

> **2026 — Memory-efficient GPU NLOS pipelines:** López-Ruiz and Royo rebuild f-k migration and phasor-field reconstruction around CUDA memory/throughput constraints, enabling much larger volumetric reconstructions and substantially higher streaming/offline throughput as SPAD-array data rates increase.

### Website / paper explorer

Add to the canonical paper corpus (`data/papers-source.html` if still used by the current site build) and surface it in:

- Latest additions
- 2026 timeline
- Active / transient / reconstruction
- Real-time / acceleration / GPU tags

Suggested tags: `active`, `transient`, `f-k`, `phasor-field`, `GPU`, `CUDA`, `real-time`, `SPAD`, `systems`.

### bare_jrnl.tex / article sections

Insert semantically in the active-NLOS reconstruction discussion, adjacent to the existing paragraphs covering f-k migration, phasor-field acceleration, low-latency NLOS, FPGA/GPU reconstruction, and learned high-speed reconstruction. Do not append it only as a detached list item.

Suggested literature-review sentence (adapt wording to the surrounding style):

> As parallel SPAD capture increases transient throughput, reconstruction itself becomes a systems bottleneck: López-Ruiz and Royo revisit both f-k migration and phasor-field reconstruction from a GPU-execution perspective, using fused CUDA pipelines and memory-efficient propagation-kernel construction to reduce latency and peak memory while retaining the original physical reconstruction operators.

This paper is also useful as a bridge between the historical algorithmic milestones (f-k and phasor fields) and the emerging system-level theme of scalable NLOS video processing.

### Bibliography

Canonical entry to merge into `egbib.bib`:

```bibtex
@article{lopezruizMemoryEfficientGPUNLOS2026,
  title         = {Memory-efficient GPU pipelines for real-time non-line-of-sight reconstruction},
  author        = {L{\'o}pez-Ruiz, Alfonso and Royo, Diego},
  journal       = {arXiv preprint arXiv:2608.28183},
  year          = {2026},
  eprint        = {2608.28183},
  archivePrefix = {arXiv},
  primaryClass  = {cs.DC},
  doi           = {10.48550/arXiv.2608.28183},
  url           = {https://arxiv.org/abs/2608.28183}
}
```

## PDF / consistency status

`README.md` (~179 KB) and `egbib.bib` (~276 KB) are large files, while the available GitHub write action replaces whole files. The current connector returns these large files in truncated response payloads, so reconstructing and overwriting them from partial content risks data loss. For that reason this run does **not** claim that `README.md`, website corpus, `bare_jrnl.tex`, canonical `egbib.bib`, or `bare_jrnl.pdf` were updated.

Before the next PDF build, merge this staged BibTeX entry and integrate the paper into README, website, and the active-reconstruction survey paragraph, then run the repository's normal LaTeX build and verify that the citation resolves and the rebuilt `bare_jrnl.pdf` contains the new discussion.
