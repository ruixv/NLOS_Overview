# 2026-09-19 NLOS update: NIR raster-scanning conference paper

## Verified missing paper

Mohammad Roueinfar and Mahdi Salmanian, **“Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength,”** *2025 33rd International Conference on Electrical Engineering (ICEE)*, pp. 1175–1179, 2025. DOI: `10.1109/ICEE67339.2025.11213924`. A later author preprint is available as arXiv:2607.04183 (posted July 2026), but the repository should label the work by its verified final IEEE conference venue/year rather than as arXiv 2026.

### Why it belongs

The paper is a direct active optical NLOS imaging experiment rather than a passing NLOS citation. It uses an 808-nm, 500-mW NIR laser, pan–tilt raster scanning of a relay wall, a three-bounce wall–target–wall transport path, and an NIR camera to recover hidden targets. Its contribution is modest compared with the major transient/phasor-field milestones, but it is useful coverage of a practical NIR intensity-imaging branch and should be categorized accordingly rather than presented as a core milestone.

## Integration locations

- **README.md / paper explorer:** add under active optical / practical acquisition, venue `IEEE ICEE 2025`; mention 808-nm illumination, pan–tilt relay-wall raster scanning, and three-bounce NIR-camera recovery.
- **Timeline:** include as a secondary 2025 practical-hardware entry, not a field-defining milestone.
- **index.html:** mirror the README metadata/category and use the DOI as the canonical publication link; arXiv may be kept as a secondary preprint link.
- **bare_jrnl.tex:** integrate briefly in the active-NLOS acquisition/hardware discussion, near practical scanning and wavelength/hardware variants. Suggested sentence: `Recent practical variants have also explored conventional near-infrared acquisition, including an 808-nm pan--tilt raster-scanning system that recovers hidden targets from three-bounce intensity measurements with an NIR camera~\cite{roueinfar2025nirnlos}.`
- **Canonical bibliography:** merge the verified entry staged in `egbib_20260919_nir_raster_icee.bib`.
- **bare_jrnl.pdf:** rebuild only after the canonical source and bibliography have been safely merged.

## Verification / safety note

Repository searches for the exact title and DOI returned no match before staging. External metadata confirms DOI, IEEE conference publication, 2025 venue year, and pages 1175–1179. Because the repository’s large public-facing files cannot be safely replaced from partial/truncated payloads in this run, they were not blindly overwritten. This note and the verified BibTeX staging file record the exact remaining integration work; no claim is made that the PDF was rebuilt in this run.
