# NLOS literature gap update — 2026-09-30

This run found three relevant works that were absent from the repository default branch by exact-title, DOI/arXiv-ID searches. Metadata was verified against publisher/arXiv records before staging. Because the canonical README, website and survey are large and were not safely reconstructed as complete editable payloads in this run, they were not overwritten from partial content.

## 1. Passive acoustic non-line-of-sight localization without a relay surface

- Tal I. Sommer and Ori Katz
- Physical Review Applied 25(2), 024064 (2026)
- DOI: 10.1103/p97k-sf71
- Final venue verified; supersedes arXiv:2506.08471 for venue labeling.
- Contribution: passive acoustic 3D NLOS source localization from knife-edge diffraction, eliminating the usual visible relay-surface requirement. Doorway edges act as virtual detector arrays; a convex-corner case exploits the frequency signature of knife-edge diffraction.
- Relevance: strong modality-expansion milestone for acoustic NLOS and a useful conceptual contrast to relay-wall optical/acoustic reconstruction.
- Suggested README/website placement: 2026 acoustic / multimodal NLOS timeline and Paper Explorer.
- Suggested survey placement: acoustic NLOS section, after relay-surface acoustic approaches, emphasizing the shift from reflected relay signals to edge-diffracted cues.

## 2. CUDA-accelerated Non-line-of-sight imaging with irregular relay surfaces

- Y. Sun, Y. Hong, W. Li, W. Li, Q. Sun, F. Xu
- Optics and Lasers in Engineering 200, 109591 (2026)
- DOI: 10.1016/j.optlaseng.2025.109591
- Contribution: back-projection directly on irregular relay geometries and arbitrary non-uniform scan patterns, with frequency-domain bandpass filtering and a CUDA implementation reporting at least two orders of magnitude speedup over CPU baselines.
- Relevance: connects arbitrary-relay geometry with practical GPU acceleration, complementing recent differentiable/3D-Gaussian arbitrary-relay work.
- Suggested README/website placement: 2026 active ToF / practical reconstruction / arbitrary-relay timeline.
- Suggested survey placement: analytic/back-projection discussion and practical-efficiency paragraph; explicitly connect planar-grid assumptions to irregular relay geometry and GPU deployment.

## 3. Memory-efficient GPU pipelines for real-time non-line-of-sight reconstruction

- Alfonso López-Ruiz and Diego Royo
- arXiv:2608.28183 (2026); no final venue verified as of this run.
- Contribution: GPU execution redesign for f-k migration and phasor fields using fused kernels, warp-level photon binning, batched transforms, CUDA graph replay and selective FP16 storage; reports up to 42x speedup over the reference streaming pipeline, up to 14x over the fastest published GPU baseline, and memory use as low as 2.5% of the reference.
- Relevance: directly follows two Core analytic/wave-based families (f-k and phasor fields), and marks the transition from reconstruction theory toward real-time, memory-bounded NLOS video processing.
- Suggested README/website placement: 2026 real-time / computational-efficiency timeline.
- Suggested survey placement: after f-k and phasor-field algorithm descriptions or in an efficiency/deployment subsection, distinguishing algorithmic inversion from systems-level GPU execution optimization.

## Citation-tracing note

The acoustic paper explicitly cites the field-defining Velten 2012, O'Toole 2018 LCT and Lindell 2019 f-k papers, and is genuinely NLOS sensing rather than a passing citation. The GPU-pipeline paper directly implements f-k migration and phasor-field reconstruction, making it a particularly direct forward branch from Core methods. The irregular-relay CUDA paper is also directly NLOS reconstruction and addresses assumptions shared by classic planar-wall methods.

## Integration status

Verified BibTeX staging is in `egbib_20260930_missing_nlos_batch.bib`. Remaining work: merge entries into the canonical bibliography; integrate concise literature-review text into `bare_jrnl.tex`; update README Latest Additions/timeline and website Paper Explorer/timeline; compile and verify `bare_jrnl.pdf`; then check all public artifacts for mutual consistency. Do not claim those canonical artifacts are updated until those edits/builds are verified.
