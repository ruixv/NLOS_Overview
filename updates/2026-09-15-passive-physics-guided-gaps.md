# 2026-09-15 NLOS update: passive optimization and physics-guided learning gaps

This run identified two high-confidence papers that were absent from repository title/DOI searches and should be integrated into the public survey artifacts.

## 1. Structure-guided adaptive total variation for parameter-free passive non-line-of-sight imaging

**Qi Zhang, Shaojie Zhang, Xue Tan, Nuoxi Yu, Xiumin Gao, Bo Dai, Dawei Zhang, Songlin Zhuang, and Guorong Sui**  
*Optics Express*, 34(3), 5210–5224 (2026). DOI: `10.1364/OE.587111`.

### Why it matters
This work extends passive NLOS reconstruction beyond fixed/manual TV regularization. SG-ATV first obtains a fast preliminary reconstruction, derives a scene-structure guidance map, and then updates spatially varying TV weights during optimization. The resulting reconstruction is parameter-free with respect to the usual manually tuned TV weight, is reported to improve robustness across scene/noise changes, and is compatible with conventional color-camera passive NLOS acquisition.

### Recommended survey placement
- **README.md**: Passive NLOS Imaging / optimization-based reconstruction; add a concise entry emphasizing adaptive scene-guided TV and elimination of manual regularization tuning.
- **Website / Paper Explorer**: category `Passive NLOS`, method tag `Optimization / Adaptive TV`, year `2026`.
- **article/3passive.tex**: place after classical inverse/regularized passive methods and before or alongside learned passive reconstruction. Suggested literature-review sentence:

  > Recent passive methods also revisit classical inverse optimization rather than relying solely on learned priors. Zhang *et al.* introduced structure-guided adaptive total variation (SG-ATV), in which a preliminary reconstruction provides a scene-dependent guidance map for spatially varying TV regularization, removing manual regularization tuning while preserving fine structure under changing noise conditions~\cite{zhang2026structureguided}.

- **Timeline**: add under 2026 as a parameter-free, adaptive-regularization milestone for passive NLOS.

## 2. Symmetry-Aware Gradient Coordination for Physics-Guided Non-Line-of-Sight Imaging

**Yijun Ling, Wenjin Zhao, Mengjia Zhao, and Jie Yang**  
*Symmetry*, 18(5), 711 (2026). DOI: `10.3390/sym18050711`.

### Why it matters
This paper is a direct Core-paper descendant: its related-work chain explicitly includes O'Toole *et al.* (LCT), Lindell *et al.* (f-k migration), Liu *et al.* (phasor-field virtual wave optics), and NLOST. Rather than adding physical consistency terms through scalar loss weighting, it treats NLOS training as a multi-objective gradient-coordination problem. The proposed pipeline combines PCGrad-style conflict projection, a hard physical routing rule (PhysGuard), learnable sensor calibration, and staged freeze/unfreeze training. The paper reports improved unseen-scene and low-SNR reconstruction within its controlled protocol and qualitative gains on seven real captured scenes.

### Recommended survey placement
- **README.md**: Deep Learning for NLOS / physics-guided reconstruction; emphasize gradient-level coordination of reconstruction, physical-consistency, and calibration objectives.
- **Website / Paper Explorer**: category `Deep Learning / Physics-Guided NLOS`, tags `gradient coordination`, `sensor calibration`, `low-SNR`, year `2026`.
- **article/4datadriven.tex**: place after NLOST/transformer and physics-guided learning paragraphs. Suggested literature-review sentence:

  > A complementary line of work moves physics integration from scalar loss design to the optimization dynamics themselves. Ling *et al.* formulate reconstruction, measurement consistency, and sensor calibration as heterogeneous gradient sources, coordinating them through conflict projection, PhysGuard routing, and staged calibration updates to improve low-SNR and unseen-scene reconstruction~\cite{ling2026symmetry}.

- **Timeline**: add under 2026 as a gradient-level physics-guided optimization milestone.

## Bibliography integration
Merge the verified entries in `egbib_20260915_passive_physics_guided_gaps.bib` into the canonical bibliography used by the survey (currently the merged bibliography file in the repository). Preserve the citation keys `zhang2026structureguided` and `ling2026symmetry` unless they conflict with existing keys.

## Public-artifact consistency checklist
1. Add both papers to `README.md` with final journal venues, DOI links, and concise summaries.
2. Add both to `index.html` / Paper Explorer / Latest Additions / development timeline.
3. Integrate SG-ATV into the passive-NLOS survey prose and the gradient-coordination paper into the data-driven/physics-guided section.
4. Merge the BibTeX entries into the canonical `.bib` source.
5. Recompile `bare_jrnl.pdf` after LaTeX integration.
6. Verify that README, website, LaTeX source, bibliography, and regenerated PDF all contain the same venue/year metadata.

## Safety note
The repository's large public-facing files are returned through truncation-prone whole-file payloads in the current connector path. This run therefore stages verified metadata and exact semantic insertion guidance instead of replacing large files from partial content. The PDF must not be reported as rebuilt until the source integration and successful LaTeX compilation are actually verified.
