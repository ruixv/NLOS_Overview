# Integration note — Thermal NLOS imaging through rough surfaces

## Verified missing paper

Ruilin Ye, Yijun Zhou, Jianwei Zeng, Chen Dai, Wenqing Hong, Wenwen Li, Jun Zhao, and Feihu Xu, “Thermal Non-Line-of-Sight Imaging through Rough Surfaces,” *ACM Transactions on Graphics*, 45(5), Article 173, 1–21, 2026. DOI: 10.1145/3811030. Published 29 June 2026; accepted 14 April 2026. An erratum was published 25 August 2026 and the version of record was updated 27 August 2026.

## Why it belongs

This is directly in scope, not merely adjacent sensing. It develops thermal passive NLOS reconstruction for rough relay surfaces. NLOSFormer embeds a convolutional thermal light-transport model into a neural architecture by jointly estimating the wall-dependent kernel and reconstructing the hidden image. The paper introduces the ThermalNLOS dataset, demonstrates substantially stronger cross-surface generalization than prior learning baselines, relative-depth estimation from the recovered kernel, and real-time dynamic thermal NLOS at roughly 4 fps. It also validates MWIR and lower-cost LWIR cameras.

The paper explicitly situates itself relative to the field-defining active NLOS works (Velten 2012, LCT/O’Toole 2018, phasor-field/Liu 2019, f-k/Lindell 2019) and passive computational periscopy, so it is also a high-confidence forward-citation/citation-tracing hit.

## Required canonical integration

- README.md: add under 2026 latest additions and the thermal/passive/modality-expansion timeline. Suggested summary: “Thermal NLOS through rough relay surfaces — NLOSFormer embeds a convolutional thermal transport kernel into reconstruction, introduces ThermalNLOS, supports relative depth, and demonstrates dynamic imaging at ~4 fps.”
- Website/index.html: add to Paper Explorer, Latest Additions, and the thermal/passive branch of the development timeline. Link the DOI/publisher page and, where appropriate, the public code/dataset repository reported by the paper (yeruilin/NLOSFormer).
- bare_jrnl.tex: integrate semantically in the passive/thermal NLOS discussion rather than appending a paper list. The trajectory is: early thermal NLOS under reflective/specular relay surfaces -> learning-based thermal reconstruction -> physics-embedded reconstruction robust to rough relay surfaces and dynamic targets. Mention the convolutional forward-model embedding, ThermalNLOS dataset, rough-wall generalization, relative depth, and real-time dynamic imaging.
- Bibliography: merge the staged BibTeX entry from `egbib_20261002_thermal_nlosformer_gap.bib` into the canonical bibliography used by bare_jrnl.tex, deduplicating by DOI/title.
- bare_jrnl.pdf: rebuild only after source and bibliography integration; verify the citation resolves and that README, website, survey, bibliography, and PDF agree.

## Safety/status

Repository-wide default-branch searches for the exact title and `NLOSFormer` returned no match before staging, so this was a genuine gap at discovery time. Large canonical files were not overwritten from partial/truncated content in this run. The staged BibTeX file and this note are committed so a later safe full-file integration/build can proceed without losing verified metadata.
