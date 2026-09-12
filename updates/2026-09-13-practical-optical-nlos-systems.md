# 2026-09-13 practical optical NLOS systems update

This update records two verified 2026 optical NLOS papers that are absent from the current repository index/search results and should be integrated across README, website, survey source, canonical bibliography, and rebuilt PDF.

## 1. Compact non-line-of-sight imager at long range

- **Paper:** Jianwei Zeng, Chen Dai, Zhongpei Xiao, Yutao Chen, Wenwen Li, Feihu Xu, “Compact non-line-of-sight imager at long range.”
- **Final venue:** *Optics Express* 34(9), 16911–16921 (2026).
- **DOI:** 10.1364/OE.597084.
- **Published:** 2026 (Optica/PubMed/OpenAlex metadata verified; PubMed issue date 4 May 2026).
- **Why it belongs:** this is a direct active optical NLOS imaging system paper, not a generic LiDAR paper. It presents a compact integrated prototype for outdoor daylight NLOS and reports kilometer-range imaging at 2 fps by combining optimized collection optics, adaptive gating, high-transmittance optics, and fast control electronics.
- **Citation-tracing relevance:** OpenAlex record W7155210986 lists the 2018 LCT paper (W2793604749) and the 2019 computational-periscopy paper (W2913322182) among its references, making this a high-priority forward-citation hit from repository Core papers.

### Suggested README entry

| 2026 | [Compact non-line-of-sight imager at long range](https://doi.org/10.1364/OE.597084) — Zeng et al. | Optics Express 34(9), 16911–16921 (2026) | Pushes active optical NLOS toward deployable outdoor sensing with a compact integrated prototype; adaptive gating and high-efficiency photon collection enable daylight kilometer-range hidden-target imaging at 2 fps, emphasizing system-level practicality rather than reconstruction-only gains. |

### Suggested survey placement

Place in `article/2active.tex` in the hardware / practical-system / long-range active-NLOS discussion, near outdoor and long-range SPAD systems and before or alongside the 3.3-km laser-reflective-tomography discussion.

Suggested literature-review sentence:

> Moving beyond laboratory-scale transient setups, Zeng et al. developed a compact integrated NLOS prototype for outdoor daylight operation, combining optimized photon collection, adaptive gating, high-transmittance optics, and fast control electronics to demonstrate kilometer-range hidden-target imaging at 2 fps \cite{zengCompactLongRangeNLOS2026}. Together with later long-range tomography systems, this work marks a shift from reconstruction-centric demonstrations toward deployable high-throughput NLOS instrumentation.

### Suggested website categorization

- Year: 2026
- Primary category: Active NLOS / Hardware systems
- Secondary tags: long-range, outdoor, SPAD/single-photon, practical system, daylight
- Timeline message: compact integrated optical NLOS reaches kilometer-scale outdoor operation at video-rate acquisition.

## 2. Eye-safe non-line-of-sight localization using compact nanosecond laser diodes and single-photon-avalanche-diode arrays

- **Paper:** Konstantin Albert, Julian Klein, Manuel Ligges, Anton Grabmaier, “Eye-safe non-line-of-sight localization using compact nanosecond laser diodes and single-photon-avalanche-diode arrays.”
- **Final venue:** *Journal of the European Optical Society-Rapid Publications* 22(1), Article 40 (2026).
- **DOI:** 10.1051/jeos/2026019.
- **Published online:** 19 May 2026.
- **Why it belongs:** this is directly about active optical NLOS localization. It replaces bulky picosecond/femtosecond laser hardware with compact 905-nm nanosecond laser diodes and a 24×32 SPAD array with on-chip timing, while explicitly designing for eye-safe operation. Dual off-axis illumination and matched temporal filtering compensate pulse-width and first-photon saturation constraints.

### Suggested README entry

| 2026 | [Eye-safe non-line-of-sight localization using compact nanosecond laser diodes and single-photon-avalanche-diode arrays](https://doi.org/10.1051/jeos/2026019) — Albert et al. | Journal of the European Optical Society-Rapid Publications 22(1), Article 40 (2026) | Demonstrates a compact eye-safe active-NLOS localization platform using 905-nm nanosecond laser diodes and a time-resolved SPAD array; dual off-axis illumination and matched temporal filtering reduce pulse-width-induced localization uncertainty and move NLOS sensing toward LiDAR-like solid-state hardware. |

### Suggested survey placement

Place in `article/2active.tex` in the active-NLOS hardware / SPAD-array / practical-system subsection, near scan-free SPAD-array systems and detector calibration work.

Suggested literature-review sentence:

> A complementary route toward practical hardware is to relax ultrafast-source requirements. Albert et al. demonstrated eye-safe NLOS localization with compact 905-nm nanosecond laser diodes and a time-resolved SPAD array, using dual off-axis illumination and matched temporal filtering to mitigate first-photon saturation and pulse-width-induced uncertainty \cite{albertEyeSafeNLOS2026}. This points toward hybrid LiDAR–NLOS architectures built from compact solid-state components rather than laboratory ultrafast sources.

### Suggested website categorization

- Year: 2026
- Primary category: Active NLOS / Hardware systems
- Secondary tags: eye-safe, SPAD array, nanosecond laser, localization, compact hardware
- Timeline message: compact eye-safe solid-state NLOS localization using LiDAR-like components.

## Cross-artifact integration checklist

1. Add both entries to `README.md` Latest Additions and the relevant Active NLOS / hardware list/timeline.
2. Add both papers to `index.html` / Paper Explorer / latest additions / timeline with the categories above.
3. Integrate the two review sentences (or style-matched equivalents) into the semantically appropriate hardware/practical-system discussion in `article/2active.tex` or whichever file `bare_jrnl.tex` inputs for that section. Do not append an isolated paper list.
4. Merge `egbib_20260913_practical_optical_nlos_systems.bib` into the canonical bibliography used by `bare_jrnl.tex` (currently `egbib_merged_20260711.bib`, unless that wiring has changed), preserving unique keys `zengCompactLongRangeNLOS2026` and `albertEyeSafeNLOS2026`.
5. Recompile `bare_jrnl.tex` and replace `bare_jrnl.pdf` only after source/bibliography integration succeeds.
6. Verify README, website, survey source, bibliography, and PDF all contain both papers and use the final published venues rather than arXiv/preprint labels.

## Safety note for the repository update

The current connector can safely create small staging files, but large public-facing files are returned in truncated JSON payloads and the write API performs whole-file replacement. Do not overwrite README, `index.html`, large survey modules, or the merged bibliography from partial content. If a later run can obtain complete source safely (e.g. complete ranged reads stitched without gaps, or a checkout/worktree), perform the full integration and rebuild then delete/retire this staging note as appropriate.
