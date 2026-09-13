# 2026-09-13 core-forward citation gaps

This run prioritized forward-citation descendants of the repository's Core papers and verified three high-confidence NLOS works that are missing from the indexed repository content (title/DOI searches returned no existing entries). All three have final, citable venues and should be integrated into the public artifacts rather than left as arXiv-only entries.

## 1. Learned Light-Cone Transform (L2CT)

**Xinqi Gao, Yijie Yang, Lianfang Wang, Xueying Liu, Yong Wang, Yuping Duan.** “Learned Light-Cone Transform for Fast and Accurate Non-Line-of-Sight Imaging.” *Physical Review Applied* 25(4), 044024 (2026). DOI: `10.1103/jsbg-c7l5`.

Why it belongs: this is a direct methodological descendant of O'Toole et al.'s 2018 LCT and explicitly cites that Core paper. L2CT keeps the LCT/Wiener inversion structure but makes its high-frequency response learnable, then adds spatiotemporal feature extraction and volume projection. The paper reports about a 5 dB PSNR improvement over vanilla LCT on evaluated data and tests across real datasets acquired by different NLOS systems.

**Recommended survey placement:** `article/4datadriven.tex`, in the physics-guided / model-based learning discussion near learnable reconstruction operators. Suggested sentence:

> A complementary line of work learns within an established analytic inverse rather than replacing it. Gao *et al.*~\cite{gaoLearnedLCT2026} introduced a learned light-cone transform (L2CT), retaining the LCT reconstruction structure while parameterizing the high-frequency response of Wiener filtering and coupling it with spatiotemporal feature extraction and volume projection. This progression from fixed LCT inversion to learnable analytic operators illustrates how classical NLOS transforms can serve as structured neural layers rather than only preprocessing backends.

**README / website summary:** `L2CT turns the field-defining light-cone transform into a learnable high-frequency-aware reconstruction operator, combining model-based inversion with spatiotemporal learned refinement.`

Category/timeline: `Deep Learning for NLOS` → `physics-guided / learned analytic operators`; timeline node: `2018 LCT → 2026 learned LCT`.

## 2. TransDiff

**Xingyu Cui, Huanjing Yue, Shida Sun, Yue Li, Yusen Hou, Zhiwei Xiong, Jingyu Yang.** “TransDiff: Unsupervised Non-Line-of-Sight Imaging With Aperture-Limited Relay Surfaces.” *IEEE Transactions on Image Processing* 34, 8018–8031 (2025). DOI: `10.1109/TIP.2025.3637694`.

Why it belongs: TransDiff directly addresses a practical failure mode of transient NLOS reconstruction—small, discontinuous, aperture-limited relay-wall sampling. It uses an unsupervised/zero-shot latent-diffusion prior to recover missing transients under measurement consistency, progressively fills the aperture, and uses a voxel-domain backpropagation error-correction stage to reduce propagation of transient-recovery errors. It is validated on simulated and real measurements and does not require paired data or pattern-specific retraining.

**Recommended survey placement:** `article/4datadriven.tex`, close to diffusion/generative priors and sparse/limited-aperture transient recovery. Suggested sentence:

> Generative priors have also been moved upstream from image refinement to transient completion. Cui *et al.*~\cite{cuiTransDiff2025} proposed TransDiff, a zero-shot latent-diffusion framework for aperture-limited relay surfaces that progressively restores missing transient measurements under measurement consistency, followed by sparsity-aware reconstruction error correction. This shifts diffusion-based NLOS processing from purely semantic image priors toward physically constrained completion of the transient measurement domain.

**README / website summary:** `Zero-shot latent diffusion recovers missing transients from aperture-limited relay surfaces under measurement consistency, followed by reconstruction-domain error correction; published in IEEE TIP 2025.`

Category/timeline: `Deep Learning for NLOS` → `diffusion / transient completion`; cross-link from active NLOS sparse sampling.

## 3. Zero-Phase Phasor Fields

**Pablo Luesia-Lahoz, Talha Sultan, Forrest B. Peterson, Andreas Velten, Diego Gutierrez, Adolfo Muñoz.** “Zero-Phase Phasor Fields for Non-Line-of-Sight Imaging.” *IEEE International Conference on Computational Photography (ICCP)*, pp. 1–9 (2025). DOI: `10.1109/ICCP64821.2025.11143850`.

Why it belongs: this is a direct extension of the phasor-field lineage. Instead of discarding phase after transforming transient measurements into the virtual-wave domain, it identifies hidden geometry from zero crossings of the virtual phase. The authors report up to 125 μm depth precision and show robustness under reduced SNR, including captured data.

**Recommended survey placement:** `article/2active.tex`, directly after the phasor-field / virtual-wave-optics discussion. Suggested sentence:

> Later work showed that the virtual phase itself can be informative rather than disposable. Luesia-Lahoz *et al.*~\cite{luesiaZeroPhase2025} derived Zero-Phase Phasor Fields for confocal NLOS imaging, locating hidden geometry through zero crossings of the reconstructed virtual phase instead of amplitude maxima. This phase-sensitive formulation enables very fine depth localization while remaining robust to measurement noise, extending the phasor-field framework from virtual-wave amplitude imaging to phase-based geometric estimation.

**README / website summary:** `Uses zero crossings of virtual phase in the phasor-field domain to localize hidden geometry with very fine depth precision, extending virtual-wave NLOS beyond amplitude-only reconstruction.`

Category/timeline: `Active NLOS Imaging` → `Reconstruction Algorithms / phasor fields`; timeline node: `2019 phasor fields → 2025 zero-phase phasor fields`.

## Required consistency work

1. Add all three entries to `README.md` with the final venues above and concise summaries.
2. Add them to `index.html` / Paper Explorer / latest additions / timeline. Do not label any of them as arXiv-only.
3. Insert the review sentences into `article/2active.tex` and `article/4datadriven.tex` at the semantic locations described above; `bare_jrnl.tex` includes these modular article files, so do not append an isolated list to the end of the survey.
4. Merge the verified entries from `egbib_20260913_core_forward_citations.bib` into the canonical bibliography `egbib_merged_20260711.bib`, preserving citation keys unless they conflict.
5. Rebuild `bare_jrnl.pdf` after source integration and verify the three references resolve in the generated bibliography.
6. Verify README, website, survey source, canonical bibliography and PDF are mutually consistent before deleting or retiring this staging note/BibTeX.

## Reliability note

The repository's large public-facing files are not overwritten in this run because the connector returns truncated representations for those files while write operations require complete replacement content. Overwriting from a partial payload would risk destructive truncation. The verified BibTeX and precise insertion plan are therefore staged safely for a later run with complete-file access or a patch-capable workflow.
