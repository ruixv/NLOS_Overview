# Practical NLOS hardware / deployment integration gap — 2026-09-27

Repository-wide exact-title and DOI searches on the default branch found no existing coverage for the two verified 2026 papers below. Both are directly relevant to active optical NLOS and should be integrated into the canonical public artifacts rather than left only in this staging note.

## 1. Eye-safe compact SPAD-array NLOS localization

**Eye-safe non-line-of-sight localization using compact nanosecond laser diodes and single-photon-avalanche-diode arrays** (2026), *Journal of the European Optical Society-Rapid Publications*, DOI: 10.1051/jeos/2026019.

Contribution: a compact, eye-safe active NLOS localization system using inexpensive 905-nm nanosecond laser diodes and a 24x32 SPAD array with on-chip timing. Parallel relay-wall detection and two off-axis illumination positions improve photon efficiency and geometrically constrain localization. Temporal matched filtering mitigates the long laser pulse. The paper explicitly points toward hybrid LiDAR-NLOS hardware and practical deployment.

Recommended integration: README 2026 timeline under practical active/ToF hardware; website Paper Explorer tags `Active`, `SPAD`, `Eye-safe`, `Compact hardware`, `Localization`, `LiDAR`; bare_jrnl.tex in the active-ToF / practical sensing hardware discussion, near consumer-LiDAR and SPAD-array work.

## 2. Compact daylight kilometer-range NLOS imager

Jianwei Zeng, Chen Dai, Zhongpei Xiao, Yutao Chen, Wenwen Li, Feihu Xu, **Compact non-line-of-sight imager at long range**, *Optics Express* 34(9), 16911–16921 (2026), DOI: 10.1364/OE.597084.

Contribution: an integrated outdoor NLOS prototype combining optimized optics, adaptive gating, high-transmittance components and fast control electronics. It demonstrates daylight kilometer-range NLOS imaging at 2 fps, addressing severe photon loss and background noise and moving optical NLOS from short-range laboratory setups toward field deployment.

Recommended integration: README 2026 timeline under long-range/practical active NLOS; website Paper Explorer tags `Active`, `Long-range`, `Outdoor`, `Daylight`, `Single-photon/ToF`, `Practical system`; bare_jrnl.tex in the deployment/long-range hardware discussion, alongside long-distance and consumer-hardware NLOS work.

## Consistency actions still required

1. Add both papers to README.md with concise contribution summaries and correct final venues.
2. Add both to index.html / Paper Explorer / latest additions / timeline.
3. Integrate both semantically into bare_jrnl.tex rather than appending a disconnected list.
4. Merge the verified entries in `egbib_20260927_practical_nlos_batch.bib` into the canonical bibliography, checking/expanding the complete author list for the JEOS paper from publisher metadata before final merge.
5. Recompile bare_jrnl.pdf and verify README/index/survey/bibliography/PDF consistency.

Large canonical files were not overwritten from partial/truncated content in this run.