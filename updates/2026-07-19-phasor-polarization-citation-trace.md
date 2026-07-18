# 19 July 2026 — phasor-field and polarized-transient citation trace

STATUS: SYNCHRONIZED — guarded source integration completed; the PDF is committed only after clean-build validation.

## Verified additions

### Forward and inverse diffraction in phasor fields

- **Authors:** Jorge Garcia-Pueyo; Adolfo Muñoz
- **Final venue:** *Optics Express* 33(5), 11420–11441, 2025
- **DOI:** `10.1364/OE.553755`
- **Why it belongs:** This is a direct theoretical and algorithmic extension of the Liu et al. phasor-field line. It explains conventional forward-propagation reconstruction through diffraction reciprocity, introduces an explicit Inverse Phasor Fields operator, studies well-posedness, and proposes a rank-based quality metric linked to Rayleigh resolution.
- **Intended survey placement:** `article/2active.tex`, wave-based model discussion, immediately before nonuniform/scaled Fourier sampling.

### Time-Gated Polarization for Active Non-Line-of-Sight Imaging

- **Authors:** Oscar Pueyo-Ciutad; Julio Marco; Stephane Schertzer; Frank Christnacher; Martin Laurenzis; Diego Gutierrez; Albert Redo-Sanchez
- **Final venue:** *SIGGRAPH Asia 2024 Conference Papers*, Article 49, 1–11
- **DOI:** `10.1145/3680528.3687575`
- **Why it belongs:** This is a direct active transient NLOS method citing Velten, LCT, f-k migration, phasor fields, and feature-visibility analysis. It combines picosecond ToF and polarization-resolved transport to recover directional information and reduce the missing-cone/null-space ambiguity.
- **Intended survey placement:** `article/2active.tex`, after the feature-visibility/three-bounce discussion and before the wave-based forward-model subsection.

## Citation-tracing decision

The ACM forward-citation list for the 2024 polarization paper also exposed **Transient Polarimetry**, a SIGGRAPH 2026 poster published online on 19 July 2026. It was not added in this run because the available metadata did not verify that the poster itself performs NLOS imaging or tightly adjacent hidden-scene reconstruction; citation alone is insufficient under the repository's relevance standard.

## Cross-artifact synchronization plan

The guarded synchronizer updates:

1. `README.md`: two Latest Additions records, chronological milestones, update date, and audit marker.
2. `index.html`: searchable paper objects, 2024/2025 timeline text, current date, and computed entry count.
3. `article/2active.tex`: active-SPAD table citations and two semantically placed literature-review paragraphs.
4. `bare_jrnl.tex`: integration marker while preserving the existing section structure.
5. `egbib_merged_20260711.bib`: regenerated from the verified canonical BibTeX source.
6. `bare_jrnl.pdf`: clean LaTeX/BibTeX rebuild only after source, bibliography, citation, text-extraction, page-rendering, and entry-count checks pass.

No large source file is to be replaced blindly. If a unique anchor is absent or duplicated, the synchronizer fails before writing changes.
