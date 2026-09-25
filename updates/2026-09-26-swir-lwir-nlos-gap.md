# Missing NLOS paper integration note — 2026-09-26

## Verified missing paper

**Mohammad Roueinfar and Mahdi Salmanian, “Non-line-of-sight (NLOS) imaging in short and long-wave infrared wavelengths,” Scientific Journal of Radar, vol. 11, no. 2, pp. 61–70, 2024.**

Persistent record identifier (DOR): `20.1001.1.23454024.1402.11.2.6.4`.

Repository-wide title/phrase search returned no existing entry before staging.

### Why it belongs

This paper is directly about NLOS imaging and expands the modality coverage beyond visible/NIR transient systems. It demonstrates two infrared regimes in one study: passive LWIR imaging of a thermally emitting hidden target using an uncooled 320×240 camera, and active SWIR NLOS imaging using external illumination and a SWIR camera. It is therefore useful as an early practical infrared/thermal modality-expansion reference rather than as a new transient inverse-model milestone.

### Recommended public-facing placement

- **README.md:** add to the 2024 development timeline / emerging modalities or thermal/infrared subsection. Suggested concise summary: “Demonstrates passive LWIR NLOS imaging of a hot hidden target and active SWIR NLOS imaging, providing an early practical bridge between thermal and actively illuminated infrared NLOS sensing.”
- **index.html / Paper Explorer:** add year 2024; tags `Thermal`, `Infrared`, `Passive NLOS`, `Active NLOS`, `LWIR`, `SWIR`; include in the modality-expansion timeline.
- **bare_jrnl.tex:** integrate semantically in the emerging-modality / passive-thermal discussion, near thermal NLOS and non-visible-spectrum sensing. Suggested survey sentence: “Infrared sensing further broadens the passive/active NLOS spectrum: Roueinfar and Salmanian demonstrated passive LWIR imaging of thermally emitting hidden targets alongside actively illuminated SWIR imaging, illustrating that NLOS acquisition can exploit both self-emission and reflected infrared radiation.”
- **Bibliography:** merge the verified entry staged in `egbib_20260926_swir_lwir_nlos.bib` into the canonical bibliography used by `bare_jrnl.tex` and cite it from the inserted survey sentence.
- **bare_jrnl.pdf:** rebuild only after the canonical TeX and bibliography integration is complete; do not treat this note as evidence that the PDF has been regenerated.

### Consistency status

This run intentionally stages the verified bibliography record and insertion plan rather than overwriting large canonical files from partial connector payloads. README/index/TeX/canonical bibliography/PDF therefore remain pending until they can be edited and validated atomically. The staged record should not be advertised as fully integrated until those checks pass.
