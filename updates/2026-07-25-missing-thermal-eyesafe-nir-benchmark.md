# NLOS missing-modality and benchmark follow-up — 25 July 2026

## Search result

No direct NLOS publication with independently verified publication metadata later than **22 July 2026** was found. The newest date-verified direct paper remains Talha Sultan et al., **Iterating the transient light transport matrix for non-line-of-sight imaging**, *Nature Communications* (published 22 July 2026), DOI `10.1038/s41467-026-75177-4`.

A fresh keyword, venue/lab-page, and core-paper citation/reference-tracing pass found four records that are absent from the current README, website snapshot, survey source, and/or consolidated bibliography. Each candidate was checked for direct NLOS relevance rather than inclusion based only on a passing citation.

## Records to integrate

### 1. Thermal Non-Line-of-Sight Imaging through Rough Surfaces

Ruilin Ye, Yijun Zhou, Jianwei Zeng, Chen Dai, Wenqing Hong, Wenwen Li, Jun Zhao, Feihu Xu  
*ACM Transactions on Graphics* 45(5), Article 41, pp. 1–21 (2026)  
DOI: `10.1145/3811030`  
Published online: 29 June 2026

This is direct passive thermal NLOS imaging through rough relay materials. NLOSFormer embeds a thermal transport model into a learned reconstruction pipeline, estimates a scene-dependent convolution kernel, and jointly recovers hidden appearance and relative depth. The work contributes the ThermalNLOS dataset and reports dynamic real-time reconstruction at approximately 4 fps with about 5% relative-depth error. It extends the thermal-NLOS trajectory from smooth or conveniently modeled relay surfaces toward practical rough surfaces.

### 2. Eye-Safe Non-Line-of-Sight Localization Using Compact Nanosecond Laser Diodes and Single-Photon-Avalanche-Diode Arrays

Konstantin Albert, Julian Klein, Manuel Ligges, Anton Grabmaier  
*Journal of the European Optical Society–Rapid Publications* 22, Article 40 (2026)  
DOI: `10.1051/jeos/2026019`

This is direct active optical NLOS localization using compact and comparatively inexpensive hardware. The system combines nanosecond pulsed laser diodes with a SPAD array that performs parallel time-resolved wall observation, uses dual off-axis illumination to mitigate first-photon saturation, and reconstructs target position using matched temporal filtering and ellipsoidal filtered backprojection. It belongs in the practical eye-safe/compact ToF hardware lineage rather than only in a generic detector list.

### 3. Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength

Mohammad Roueinfar, Mahdi Salmanian  
*2025 33rd International Conference on Electrical Engineering (ICEE)*, IEEE (2025)  
DOI: `10.1109/ICEE67339.2025.11213924`  
Auxiliary source: arXiv:2607.04183

The July 2026 arXiv upload is not the venue: an IEEE ICEE 2025 proceedings record is already verifiable and should be used as the final venue. The paper demonstrates a low-cost 808-nm, 500-mW laser, pan–tilt relay-wall raster scan, NIR-camera three-bounce system on three hidden targets. It is a direct NLOS experiment and useful as a hardware/deployment entry, although it is not a new core inverse operator and should not be presented as a major algorithmic milestone.

### 4. A Comprehensive Study of Time-of-Flight Non-Line-of-Sight Imaging

Julio Marco, Adrián Jarabo, Ji Hyun Nam, Alberto Tosi, Diego Gutiérrez, Andreas Velten  
arXiv:2603.09548 (2026); no final venue verified

This survey/benchmark paper places common time-of-flight NLOS methods under a shared forward model, relates simplified inverses to Radon-, frequency-domain-, and phasor-field formulations, and compares reconstruction behavior under controlled hardware and photon-count assumptions. It is relevant to the repository's **Related Surveys and Benchmarks** section and to the survey's methodological comparison narrative. Use arXiv as the venue until a final accepted or published record is independently verified.

## Repository comparison

Repository-wide title and DOI checks against the current `README.md`, `bare_jrnl.tex`, and `egbib_merged_20260711.bib` did not find these four exact records. The repository is also still awaiting application of the preceding `2026-07-25-frontier-followup-staged.md` items; the latest public README snapshot remains dated 24 July 2026. These two pending batches should be integrated together to avoid repeated paper-count changes and duplicate PDF rebuilds.

Canonical metadata for the four records is staged in:

- `egbib_20260725_missing_modalities_and_benchmark.bib`

## Precise integration plan

### `README.md`

1. Add the following rows to **Latest Additions**, preserving their scope labels in the contribution summaries:
   - Thermal rough-surface NLOS — passive / thermal / learned reconstruction / depth.
   - Eye-safe compact laser-diode and SPAD-array localization — active ToF hardware / localization.
   - NIR raster scanning — active steady-state/NIR hardware; label it as a measured proof of concept rather than a core inverse-method milestone.
   - Comprehensive ToF study — survey/benchmark rather than a new reconstruction system.
2. Add timeline sentences:
   - **2025:** accessible NIR raster-scanning hardware broadens low-cost active NLOS experimentation.
   - **2026:** compact eye-safe SPAD localization and rough-wall thermal reconstruction expand deployment conditions; common-model ToF benchmarking improves method comparability.
3. Keep the publication venue for the NIR paper as ICEE 2025, with arXiv only as an auxiliary source.

### `index.html`

1. Add one paper-explorer object for each record with categories that distinguish direct reconstruction, localization, hardware, thermal modality, and survey/benchmark status.
2. Extend the 2025 and 2026 development timeline using the same scope distinctions as the README.
3. Recalculate the tracked-entry count from the actual number of previously absent objects after both pending 25 July update batches are applied; do not hard-code an assumed count.

### `article/2active.tex`

1. Insert the eye-safe laser-diode/SPAD-array paper in the active acquisition/hardware discussion near compact, eye-safe, scan-free, and parallel-SPAD systems. Add a short sentence explaining the trade-off between inexpensive nanosecond hardware and picosecond-resolution custom systems.
2. Insert the NIR raster-scanning paper in the continuous-wave/NIR or low-cost active-hardware discussion. Describe it as a measured three-bounce proof of concept and avoid overstating algorithmic novelty.
3. In the methods-comparison discussion, cite the comprehensive ToF study when explaining that LCT, f-k migration, phasor-field, and related inverses can be compared under a shared forward model and controlled photon/hardware assumptions.

### `article/5newscenes.tex`

Add a subsection or semantically placed paragraph titled **Thermal NLOS through rough relay surfaces**. Connect the paper to prior thermal NLOS and long-wave-infrared work, then explain that learned, physics-embedded kernel estimation relaxes idealized relay-surface assumptions and enables simultaneous appearance/depth inference for dynamic scenes.

### `article/4datadriven.tex`

Where the survey discusses physics-embedded learned reconstruction, add a cross-reference to NLOSFormer as an example in which a network estimates the effective thermal transport kernel rather than treating the wall observation as an unconstrained image-to-image mapping. Avoid duplicating the primary thermal-modality discussion in `article/5newscenes.tex`.

### Related surveys / benchmarks

Place **A Comprehensive Study of Time-of-Flight Non-Line-of-Sight Imaging** in the README's **Related Surveys and Benchmarks** list and add a brief survey sentence explaining its common-model and controlled-comparison role. Do not describe it as a final journal or conference paper unless a final venue becomes verifiable.

### Bibliography

Merge the four canonical entries from `egbib_20260725_missing_modalities_and_benchmark.bib` into `egbib_merged_20260711.bib` while preserving any pre-existing stable key if an equivalent DOI record is discovered during the merge. Reject duplicate DOI/title records.

### `bare_jrnl.tex` and `bare_jrnl.pdf`

1. Add a 25 July 2026 trace marker after both pending update batches are applied.
2. Run a clean `pdflatex → bibtex → pdflatex ×2` build.
3. Reject undefined or multiply defined citations and duplicate bibliography entries.
4. Verify PDF text contains the new thermal, eye-safe, NIR, and ToF-comparison discussion.
5. Render all pages to images and confirm the rendered-page count matches `pdfinfo` before committing `bare_jrnl.pdf`.

## Current status

Only the verified metadata supplement and this precise patch-style integration note were committed in this pass. The large public files and `bare_jrnl.pdf` were not overwritten because the preceding guarded workflow has not yet produced its source-integration commit and applying a second blind whole-file replacement would risk conflicts or truncation. Therefore README, website, survey source, consolidated bibliography, and PDF are **not claimed as synchronized for these four records yet**.
