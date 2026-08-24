# Joint LOS/NLOS radar clutter-mitigation gap — 24 August 2026

A radar/mmWave forward-citation and predecessor-tracing pass identified one additional direct NLOS sensing paper that is not present in the current public corpus:

- Jiahui Chen, Xiaobo Yang, Chen Qiu, Zhihao Zhu, Peilun Wu, Zihan Xu, Shisheng Guo, and Guolong Cui, “Joint Localization of LOS and NLOS Targets With Clutter Mitigation via Multipath Exploitation Radar,” *IEEE Transactions on Radar Systems*, vol. 3, pp. 549–561, 2025, DOI `10.1109/TRS.2025.3550023`.

The paper addresses a practical gap left by radar NLOS methods that assume the scene contains only hidden targets. It models a corner scene containing both LOS and NLOS targets, formulates background-clutter suppression and target localization jointly using low-rank, sparse, and group-sparse structure, and solves the resulting inverse problem with a proximal-gradient iteration. Simulations and experiments validate simultaneous clutter suppression and localization of LOS and hidden targets.

## Recommended public integration

1. **README.md / Latest Additions** — add the final IEEE TRS record, DOI link, and a concise summary emphasizing mixed LOS/NLOS localization plus clutter mitigation.
2. **README.md / 2025 timeline** — place it after the classical multipath/unknown-layout radar lineage and before later camera-conditioned / learned urban-intersection radar sensing. Suggested trajectory: `NLOS-only multipath localization → joint LOS/NLOS localization with low-rank + sparse clutter suppression → learned/reflection-aware urban-intersection perception`.
3. **data/papers-source.html** — add one canonical RF/radar paper object and update the 2025 radar timeline; recompute the displayed tracked-entry count from the array rather than editing the number manually.
4. **article/5newscenes.tex** — insert in the `Radar-Based NLOS Imaging` narrative after the multipath/unknown-layout localization lineage. Suggested literature-review sentence: “Moving beyond NLOS-only scenes, Chen et al. jointly localize visible and hidden targets while suppressing background clutter by combining low-rank, sparse, and group-sparse structure in a proximal-gradient multipath-exploitation reconstruction.” Cite `chenJointLOSNLOSClutter2025`.
5. **egbib_merged_20260711.bib** — merge the prepared `chenJointLOSNLOSClutter2025` entry exactly once; verify DOI and key uniqueness. The staging entry is in `egbib_20260824_joint_los_nlos_clutter_gap.bib`.
6. **bare_jrnl.tex / bare_jrnl.pdf** — update the survey provenance marker, run a clean `pdflatex → bibtex → pdflatex → pdflatex` (or equivalent latexmk) build, verify the citation in `.aux/.bbl`, confirm the title/contribution is present in PDF text, render at least the first/last pages, and only then commit the rebuilt PDF.

## Scope decisions

- `Deep Learning–Aided Frequency-Modulated Continuous-Wave Radar for Around-the-Corner Non-Line-of-Sight Perception at Urban Intersections` (CMES 147(1), 37, 2026; DOI `10.32604/cmes.2026.078862`) was re-verified from the publisher, but it is already present in the current public README/corpus and should **not** be duplicated.
- `LOS and NLOS Targets Localization in an L-Shaped Corner` (IGARSS 2024, DOI `10.1109/IGARSS53475.2024.10641543`) is bibliographically plausible and closely related, but this run did not obtain enough primary-source method detail to justify integrating it independently. Keep it as a citation-tracing candidate rather than adding it on title metadata alone.
- `AT-BLR: AOA- and TD-Based Multimaterial Building Layout Reconstruction` is through-wall/transmissive building-layout tomography rather than direct around-corner NLOS and is excluded from the main NLOS corpus.

This note is intentionally patch-style: the same large radar survey/public files are currently being handled by the guarded 2022–2025 unknown-layout lineage integration, so this additional paper should be merged only after that public build is stable, avoiding overlapping blind whole-file replacements.
