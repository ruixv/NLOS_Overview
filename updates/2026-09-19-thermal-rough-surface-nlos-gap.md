# Integration note — Thermal NLOS through rough surfaces (TOG 2026)

Verified missing paper on 2026-09-19:

Wenwen Li, Jun Zhao, and Feihu Xu, **“Thermal Non-Line-of-Sight Imaging through Rough Surfaces,”** *ACM Transactions on Graphics*, 45(5), Article 173, pp. 1–21, 2026. DOI: 10.1145/3811030. Published online June 29, 2026. ACM records an erratum on Aug. 25 and corrected Version of Record on Aug. 27, 2026.

## Why it belongs

This is a direct thermal/passive NLOS imaging paper rather than a generic thermal-vision citation. It addresses the difficult rough-relay-wall regime, where thermal radiation is strongly spatially mixed. The paper introduces **NLOSFormer**, a physics-embedded network that models thermal transport as convolution, estimates the scene-dependent convolution kernel from measurements, and uses that physical estimate to guide end-to-end hidden-scene reconstruction. It expands the NLOS modality timeline from visible passive/active optics toward long-wave thermal sensing and, importantly, relaxes the reflective-relay-surface assumption common in earlier thermal NLOS work.

## Required canonical integration

- **README.md:** add to Latest Additions and the Passive/Thermal NLOS category. Suggested summary: “Physics-embedded NLOSFormer reconstructs thermal hidden scenes through rough relay surfaces by estimating a convolutional transport kernel and using it to guide learned reconstruction.”
- **Timeline:** place in 2026 as an emerging-modality/practical-relay milestone: thermal NLOS progresses from favorable reflective relays to rough diffuse surfaces.
- **index.html / Paper Explorer:** add venue `ACM TOG 2026`, modality `Thermal`, method tags `physics-embedded learning`, `rough relay surface`, `convolutional transport` and DOI link.
- **bare_jrnl.tex:** integrate semantically in the passive/thermal or emerging-modality discussion, adjacent to prior thermal NLOS. Suggested literature-review sentence: “Recent thermal NLOS work further relaxes relay-surface constraints: Li et al. model rough-surface thermal transport as a convolution and embed an estimated transport kernel into NLOSFormer, enabling learned reconstruction under severe spatial mixing.”
- **Canonical bibliography:** merge the verified entry staged in `egbib_20260919_thermal_nlos_rough_surfaces.bib`.
- **bare_jrnl.pdf:** rebuild only after the canonical `.tex` and bibliography are safely updated; verify the citation resolves and the final PDF reflects the new paragraph.

## Consistency / safety status

Repository-wide GitHub code search for both the exact title and DOI `10.1145/3811030` returned no match before staging, so this is a genuine repository gap. Large canonical files were not overwritten from partial connector payloads. This note and the staging BibTeX should be treated as pending integration, not as evidence that README/index/survey/PDF are already synchronized.
