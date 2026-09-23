# Verified gap: Compact non-line-of-sight imager at long range

## Paper
Jianwei Zeng, Chen Dai, Zhongpei Xiao, Yutao Chen, Wenwen Li, and Feihu Xu, “Compact non-line-of-sight imager at long range,” *Optics Express*, 34(9), 16911–16921, 2026. DOI: 10.1364/OE.597084. Published 4 May 2026.

## Why it belongs
This is a directly relevant active time-of-flight NLOS imaging paper focused on practical outdoor deployment rather than a merely adjacent NLOS sensing citation. It integrates optimized optics, adaptive gating, high-transmittance components, and fast control electronics into a compact prototype and demonstrates daylight kilometer-range NLOS imaging at 2 fps. The paper therefore marks the trajectory from laboratory-scale transient NLOS toward compact, real-time, long-range outdoor systems.

## Repository check
Repository-wide search for the exact title returned no match before this staging update.

## Integration locations
- README.md: add under 2026 Active / Transient / Practical Systems or Long-range NLOS; concise summary: “Compact integrated active-NLOS prototype combines efficient photon collection, adaptive gating, low-noise optics and fast electronics to demonstrate daylight kilometer-range imaging at 2 fps.”
- index.html / Paper Explorer: add as 2026, Active, ToF/SPAD, Long-range/Outdoor, Practical system.
- Development timeline: place after earlier long-range active-NLOS demonstrations and alongside 2026 deployment-oriented hardware advances; emphasize the shift from slow laboratory scanning to compact daylight kilometer-range operation.
- bare_jrnl.tex: integrate semantically in the active/transient practical-systems or long-range discussion, not as a detached list item. Suggested literature-review sentence: “Recent hardware integration has further moved transient NLOS toward outdoor deployment: Zeng et al. combine efficient photon collection, adaptive temporal gating, low-loss optics, and fast control electronics in a compact prototype, demonstrating daylight kilometer-range NLOS imaging at 2 fps.”
- Bibliography: merge the verified entry staged in `egbib_20260923_compact_long_range_nlos.bib` into the canonical bibliography using the repository’s existing key/style conventions.
- bare_jrnl.pdf: rebuild only after source/bibliography integration; verify the new citation resolves and the README, website, TeX, bibliography, and PDF agree.

## Verification / build status
Metadata was verified against the final *Optics Express* record (Vol. 34, Issue 9, pp. 16911–16921; DOI 10.1364/OE.597084). Canonical large files and PDF were not overwritten in this staging step; source integration and PDF rebuild remain required.
