# Integration gap: Thermal NLOS imaging through rough surfaces (TOG 2026)

Verified on 2026-09-22.

## Paper

Ruilin Ye, Yijun Zhou, Jianwei Zeng, Chen Dai, Wenqing Hong, Wenwen Li, Jun Zhao, and Feihu Xu, “Thermal Non-Line-of-Sight Imaging through Rough Surfaces,” *ACM Transactions on Graphics*, 45(5), Article 173, pp. 1–21, 2026. DOI: 10.1145/3811030. Published 29 June 2026; corrected 27 August 2026.

## Why it belongs

This is a direct NLOS-imaging paper and a meaningful modality/practicality milestone. It addresses passive thermal NLOS through rough relay surfaces, where spatial mixing and wall self-emission make prior thermal approaches fragile. NLOSFormer embeds an explicit convolutional light-transport model into a dual-branch neural reconstruction architecture, jointly estimating a transport kernel and hidden image. The estimated kernel supplies a physical constraint and relative-depth cue. The paper also introduces the ThermalNLOS dataset and demonstrates real-time dynamic reconstruction at 4 fps across multiple relay-wall materials.

The paper explicitly situates itself against the active-NLOS core lineage (Velten 2012, LCT/O’Toole 2018, phasor-field/Liu 2019, f-k/Lindell 2019) and prior passive/thermal NLOS. It is therefore a high-confidence forward-lineage candidate rather than a tangential citation.

## Repository check

Before staging, repository-wide searches for the exact title, `NLOSFormer`, and DOI `10.1145/3811030` returned no matches. This paper is therefore missing from the current default-branch corpus rather than a duplicate.

## Required canonical integration

1. **README.md** — add to Latest Additions and to New NLOS Scenes and Modalities / thermal NLOS. Suggested concise summary: “Introduces NLOSFormer, a physics-embedded transformer that jointly estimates a rough-wall thermal transport kernel and reconstructs the hidden scene; adds the ThermalNLOS dataset, relative-depth inference, and 4-fps dynamic thermal NLOS across diverse rough relay surfaces.”
2. **Milestone timeline** — place in 2026 under thermal/passive modality expansion and physics-guided learned reconstruction. Recommended trajectory: reflective/specular thermal NLOS → learned thermal reconstruction → rough-surface physics-embedded thermal NLOS with dynamic video and depth cues.
3. **index.html / Paper Explorer / Latest Additions** — add the same final venue metadata and tags such as `thermal`, `passive`, `rough relay`, `physics-guided learning`, `dynamic`, `dataset`.
4. **bare_jrnl.tex** — integrate semantically in the thermal/passive emerging-modality discussion, not as an appended bibliography-only item. A suitable literature-review sentence is: “Recent thermal NLOS work further moves beyond reflective relay surfaces: Ye et al. embed a convolutional rough-wall transport model into a learned reconstruction architecture, jointly estimating the transport kernel and hidden scene while enabling relative-depth cues and real-time dynamic reconstruction across diverse rough materials.”
5. **Bibliography** — merge the verified entry staged in `egbib_20260922_thermal_nlosformer_tog.bib` into the canonical bibliography used by `bare_jrnl.tex`, preserving the repository citation-key convention.
6. **bare_jrnl.pdf** — rebuild only after the canonical TeX and bibliography are safely integrated; verify the new citation resolves and the PDF reflects the updated thermal-NLOS discussion.

## Safety note

The canonical README/website/TeX files are large and current connector responses can be truncated. They were not overwritten from partial payloads in this run. The staged BibTeX and this precise insertion note preserve the verified update without risking destructive truncation. Do not report the PDF as regenerated until a complete-source edit and successful LaTeX build are verified.
