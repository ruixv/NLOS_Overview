# 2026-08-28 — Compact long-range NLOS imager gap

## Verified missing paper

Jianwei Zeng, Chen Dai, Zhongpei Xiao, Yutao Chen, Wenwen Li, and Feihu Xu, **“Compact non-line-of-sight imager at long range,”** *Optics Express*, 34(9):16911–16921, 2026. DOI: `10.1364/OE.597084`.

Primary-source metadata is verified from the Optica Publishing Group issue page and Crossref/PubMed-indexed metadata. The paper is a final journal publication, not an arXiv-only record.

## Why it belongs in the survey

This is a direct active/transient NLOS imaging system paper, not merely an adjacent long-range LiDAR paper. The system targets kilometer-range outdoor NLOS under daylight, where photon loss and background noise dominate. The prototype combines optimized collection optics, adaptive temporal gating, high-transmittance optical components, and fast electronics. The paper reports approximately 27% total system efficiency, about a 7× improvement over its cited prior system, roughly three orders of magnitude SNR improvement, kilometer-scale daytime NLOS imaging, ~4 cm spatial resolution, and up to 2 fps for a simple moving target. The reconstruction explicitly uses the phasor-field algorithm, making the connection to the Liu et al. phasor-field core-paper lineage direct rather than incidental.

## Repository audit

As of this run, searches for the exact title and DOI `10.1364/OE.597084` return no existing canonical paper entry in `ruixv/NLOS_Overview`. Therefore this is a genuine corpus gap rather than a venue update or duplicate record.

## Required public-artifact integration

1. **README.md**
   - Add to Latest Additions.
   - Add a 2026 development-timeline node under long-range / deployable active transient NLOS.
   - Suggested concise contribution summary: “Compact daylight kilometer-range active NLOS prototype combining efficient photon collection, adaptive gating, fast electronics, and phasor-field reconstruction; demonstrates ~4 cm resolution and up to 2 fps for a simple moving target.”

2. **Website / V2 canonical corpus**
   - Add the paper to `data/papers-source.html` / Paper Explorer using the canonical key `zengCompactLongRangeNLOS2026`.
   - Family: active optical.
   - Venue: `Optics Express 34(9), 16911–16921 (2026)`.
   - URL: `https://doi.org/10.1364/OE.597084`.
   - Add a 2026 timeline milestone connecting earlier kilometer-scale NLOS demonstrations to compact daytime real-time-capable hardware.
   - Do not duplicate the paper object in `index.html` if the current V2 site loads the canonical corpus externally.

3. **Survey source**
   - Integrate semantically into the active optical / long-range transient NLOS discussion in `article/2active.tex` (or the corresponding included section used by `bare_jrnl.tex`).
   - Suggested literature-review sentence: “Recent work has shifted kilometer-scale NLOS from proof-of-concept demonstrations toward compact deployable prototypes: Zeng et al. combine high-efficiency collection optics, adaptive gating, and fast control electronics with phasor-field reconstruction to demonstrate daylight kilometer-range imaging at up to 2 fps.”
   - Position near long-range outdoor, all-day SPAD, scan-free/parallel acquisition, and laser-reflective-tomography developments rather than in generic learned reconstruction.

4. **Bibliography**
   - Merge `egbib_20260828_compact_long_range_nlos_gap.bib` into the canonical bibliography used by `bare_jrnl.tex`.
   - Preserve citation key `zengCompactLongRangeNLOS2026`.
   - Verify DOI uniqueness: `10.1364/OE.597084` must occur in exactly one canonical BibTeX entry.

5. **PDF rebuild and validation**
   - Clean-build using the repository's normal LaTeX/BibTeX sequence (e.g. `pdflatex -> bibtex -> pdflatex -> pdflatex`).
   - Verify `zengCompactLongRangeNLOS2026` resolves in `.aux` / `.bbl`.
   - Verify the resulting `bare_jrnl.pdf` contains the new long-range-system discussion and the Optics Express bibliography entry.
   - Render-check at least the affected survey page plus first/last pages before committing the binary PDF.

6. **Cross-artifact consistency**
   - Confirm the title/DOI appear consistently in README, V2 corpus, survey source, canonical bibliography, and rebuilt PDF.
   - Do not claim the PDF is updated until the clean build and semantic/render checks succeed.

## Relation to nearby 2026 work

This paper complements, rather than duplicates, the 3.3-km scanning-free laser reflective tomography result. The latter changes the acquisition geometry through projection/tomographic sampling, whereas Zeng et al. focus on a compact high-efficiency daylight transient-imaging prototype and retain phasor-field reconstruction. Together they define two distinct routes toward practical kilometer-scale NLOS: acquisition-paradigm redesign versus deployable photon-efficient hardware.
