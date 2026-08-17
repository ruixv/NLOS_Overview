# 17 August 2026 — Scan-free SPAD-array resolution citation/consistency trace

Status: integrated by the guarded workflow; public-source changes are committed only after the LaTeX/PDF and cross-artifact checks pass.

## What this run found

A forward-citation pass from the field-defining transient NLOS line (Velten 2012, LCT, f-k migration, and phasor-field reconstruction) exposed a coherent scan-free SPAD-array lineage. Two papers in that lineage had already been discussed in README/survey prose but had regressed out of the canonical V2 paper corpus and the merged bibliography during later homepage/bibliography migrations. A third paper was genuinely missing from the public paper list and survey:

1. **Real-time scan-free non-line-of-sight imaging** — Wenjun Zhang, Enlai Guo, Shuo Zhu, Chenyang Huang, Lijia Chen, Lingfeng Liu, Lianfa Bai, Edmund Y. Lam, Jing Han. *APL Photonics* 9(12), 126101 (2024). DOI: `10.1063/5.0235687`. Parallel SPAD-array capture plus non-confocal time-to-space boundary migration removes relay-wall raster scanning; the paper reports 151-fps transient capture and 19-fps end-to-end imaging, with plug-in super-resolution reducing the array requirement from 32×32 to 8×8.
2. **Sub-pixel resolving modulation for non-line-of-sight imaging** — Wenjun Zhang, Shuo Zhu, Lijia Chen, Lingfeng Liu, Lianfa Bai, Edmund Y. Lam, Enlai Guo, Jing Han. *Optics Express* 33(14), 30783–30798 (2025). DOI: `10.1364/OE.569102`. This is the genuinely missing paper in the current run. DMD pixel-shift modulation synthesizes sub-pixel relay sampling and explicitly accounts for spatial/temporal broadening; the reported lateral resolution improves from about 7 cm to 1 cm while retaining compatibility with established transient reconstruction back ends.
3. **High-resolution and real-time non-line-of-sight imaging based on spatial correlation** — Wenjun Zhang, Shuo Zhu, Lijia Chen, Lianfa Bai, Edmund Y. Lam, Enlai Guo, Jing Han. *Optics and Lasers in Engineering* 193, 109100 (2025). DOI: `10.1016/j.optlaseng.2025.109100`. SCBSF-NLOS uses a 3-D blur-kernel model and spatial-correlation resampling to recover about 2-cm lateral detail at 5 fps from a 16×16 detector.

## Intended survey trajectory

The three papers should be read as one development line:

**parallel non-confocal SPAD acquisition → physical sub-pixel sampling densification → spatial-correlation computational resampling**.

This line is tightly connected to the Core transient literature because the 2024 paper explicitly derives its non-confocal migration in the context of LCT/wave-based transient reconstruction, while the later papers target the scan-free spatial-resolution bottleneck rather than replacing the underlying transient inverse models.

## Guarded integration targets

The integration script is designed to:

- add the missing Optics Express 2025 paper to `README.md` and its 2025 development timeline;
- restore all three records to the canonical V2 corpus in `data/papers-source.html`, which feeds the 3D graph and Paper Explorer;
- synchronize the visible living-survey date in `index.html`;
- replace the existing two-paper scan-free paragraph in `article/2active.tex` with a three-stage literature-review paragraph and add the new citation to the SPAD-array method table;
- verify the three existing canonical BibTeX records in `egbib_merged_20260711.bib` and reuse `zhangSubpixelModulation2025` for the Optics Express paper, avoiding a duplicate alias;
- add a provenance marker to `bare_jrnl.tex`;
- rebuild `bare_jrnl.pdf` and require citation, public-artifact, PDF-text, and PDF-render checks before the generated sources/PDF are committed.

If any anchor or consistency check fails, the guarded workflow must not overwrite the public artifacts blindly; this note and the staged metadata remain sufficient to reproduce the intended patch safely.
