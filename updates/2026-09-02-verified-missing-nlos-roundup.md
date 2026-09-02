# Verified missing NLOS papers — 2026-09-02

This update records three high-confidence papers that were not found by exact-title or DOI search in the current repository snapshot. They should be integrated into README.md, the website/Paper Explorer/timeline, the semantically appropriate survey sections, and the canonical bibliography. A verified BibTeX staging file is available as `egbib_20260902_verified_missing_roundup.bib`.

## 1. Yu et al. — non-confocal frequency-domain phase compensation

**Jing Ping Yu, Xiao Rui Tian, Jie Yang, Zhou Yang, Ming Ze Yang, Si Qi Zhang, Meng Tang, Chen Fei Jin. “Non-confocal non-line-of-sight imaging using frequency-domain phase compensation with the reference function.” Optics Express 34(2), 3232–3243 (2026). DOI: 10.1364/OE.580027.**

Why it belongs: this is direct active/transient NLOS reconstruction, not adjacent sensing. It transfers a single-input/multiple-output frequency-domain imaging construction from millimeter-wave imaging into optical NLOS, uses a reference-function phase-compensation formulation, and accelerates reconstruction with FFTs. The work is especially relevant to the non-confocal / frequency-domain branch following f-k migration and other wave-domain inversions.

Suggested README / Paper Explorer summary: “Adapts a SIMO frequency-domain imaging model from millimeter-wave imaging to non-confocal optical NLOS; reference-function phase compensation plus FFT reconstruction reduces artifacts/shape distortion while lowering computational cost.”

Suggested timeline/category: **2026 — Active NLOS / Reconstruction Algorithms / Non-confocal & frequency-domain methods**.

Suggested survey placement: in the active-reconstruction discussion near f-k migration, non-confocal imaging, and frequency-domain methods. Suggested prose: “Recent work has also transferred frequency-domain phase-compensation ideas from millimeter-wave imaging to non-confocal optical NLOS, using reference functions and FFT-based inversion to improve reconstruction fidelity while reducing computational burden.” Cite `yuFrequencyDomainPhaseNLOS2026`.

## 2. Zhang et al. — parameter-free passive NLOS via structure-guided adaptive TV

**Qi Zhang, Shaojie Zhang, Xue Tan, Nuoxi Yu, Xiumin Gao, Bo Dai, Dawei Zhang, Songlin Zhuang, Guorong Sui. “Structure-guided adaptive total variation for parameter-free passive non-line-of-sight imaging.” Optics Express 34(3), 5210–5224 (2026). DOI: 10.1364/OE.587111.**

Why it belongs: this is genuine passive NLOS reconstruction using a conventional color camera. It introduces spatially varying TV regularization weights derived from a fast preliminary reconstruction, automatically balancing detail preservation and noise suppression and avoiding scene-by-scene manual regularization tuning. It therefore complements the repository’s learned passive-NLOS line with a modern optimization-based / interpretable prior branch.

Suggested README / Paper Explorer summary: “Structure-guided adaptive TV for conventional-camera passive NLOS; derives spatially varying regularization from a preliminary reconstruction, eliminating manual tuning while improving robustness, color fidelity, and reconstruction efficiency.”

Suggested timeline/category: **2026 — Passive NLOS / Optimization-based reconstruction / adaptive priors**.

Suggested survey placement: passive-NLOS inverse methods, immediately before/alongside the learned-attention and physics-guided passive reconstruction discussion. Suggested prose: “Alongside increasingly learned passive-NLOS pipelines, adaptive optimization remains competitive: structure-guided spatially varying TV can infer regularization weights from the measurement itself, reducing parameter sensitivity without requiring a learned reconstruction prior.” Cite `zhangStructureGuidedATV2026`.

## 3. Ling et al. — gradient coordination for physics-guided NLOS learning

**Yijun Ling, Wenjin Zhao, Mengjia Zhao, Jie Yang. “Symmetry-Aware Gradient Coordination for Physics-Guided Non-Line-of-Sight Imaging.” Symmetry 18(5), 711 (2026). DOI: 10.3390/sym18050711.**

Why it belongs: the paper explicitly targets transient NLOS reconstruction under low SNR and validates on synthetic and seven real captured scenes. Rather than introducing a new backbone, it studies how reconstruction, measurement-consistency, Poisson-statistics, and sensor-calibration objectives conflict during training, and combines PCGrad, a PhysGuard routing rule, learnable sensor calibration, and staged optimization. It is tightly adjacent to NLOST/LPP-style physics-guided learned reconstruction and represents an optimization/training-method branch rather than a new sensing modality.

Suggested README / Paper Explorer summary: “Physics-guided transient NLOS training via gradient-level coordination: PCGrad + PhysGuard routing + learnable sensor calibration + staged optimization reduce destructive conflicts between reconstruction and physical-consistency objectives under low SNR.”

Suggested timeline/category: **2026 — Deep Learning for NLOS / Physics-guided optimization and calibration**.

Suggested survey placement: learned reconstruction / physics-guided learning, after NLOST/LPP and before broader discussion of robustness/generalization. Suggested prose: “Recent physics-guided NLOS work has begun to treat training itself as a constrained inverse problem: gradient-level routing and staged sensor calibration can prevent reconstruction and measurement-consistency objectives from destructively interfering in low-SNR transient reconstruction.” Cite `lingSymmetryAwareGradientNLOS2026`.

## Verification and deduplication

- Exact-title and DOI searches against the current GitHub repository returned no matches for all three works.
- All three have final, publisher-verifiable 2026 journal venues; none should be labeled as arXiv.
- The first two are direct NLOS imaging/reconstruction papers. The third is a physics-guided learned NLOS reconstruction methodology paper with real-scene validation and is sufficiently central to the learned-reconstruction trajectory to include.
- The fresh-search pass also re-encountered already-covered or previously integrated 2026 work such as Learned LCT, 3D Gaussian Transient Rendering, Stereo NLOS, MD-NLOS, passive DAAM, thermal rough-surface NLOS, consumer-LiDAR NLOS, and recent GPU/SPAD work; those should not be duplicated.

## Integration safety / remaining work

`README.md`, `index.html`, and `egbib.bib` are large public-facing files. In the current connector environment, full reads of these files may be truncated while writes require whole-file replacement, so blind replacement would risk data loss. For that reason this run does **not** claim that the three papers have already been inserted into every artifact or that `bare_jrnl.pdf` has been regenerated. The safe next integration step is to apply the insertion text above to the complete repository checkout, merge the staging BibTeX entries into canonical `egbib.bib`, add the corresponding citations to the semantically appropriate survey sections, rebuild `bare_jrnl.pdf`, and then verify title/venue/citation parity across README, website, survey source, bibliography, and PDF.
