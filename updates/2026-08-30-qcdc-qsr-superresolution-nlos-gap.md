# 2026-08-30 — QCDC–QSR temporal super-resolution NLOS gap

## Verified paper

Xiaorui Tian, Kai Qiao, Xiaojie Shi, Meng Tang, Siqi Zhang, and Chenfei Jin, **“Non-line-of-sight super-resolution imaging with quasi-constant-delay circular pattern,”** *APL Photonics*, 11(7), 076122 (2026). DOI: `10.1063/5.0331605`. Published online 28 July 2026.

## Why it belongs

This is a direct active transient NLOS reconstruction/acquisition paper. It jointly designs a quasi-constant-delay circular (QCDC) relay-wall sampling pattern and a quasi-constant-delay super-resolution (QSR) algorithm so that multiple sub-bin delayed measurements are collected within one acquisition. The reported system computationally improves effective transient resolution from 200 ps to 20 ps and reconstructs 256×256 hidden images from a 15×64 QCDC pattern. The authors explicitly validate the processed transients with standard NLOS reconstruction families including f-k migration and phasor-field reconstruction, and motivate the method as a route to consumer SPAD hardware with limited timing resolution.

This therefore extends the development line:

`transient NLOS reconstruction → sparse/efficient relay-wall sampling → computational temporal super-resolution → consumer-SPAD-oriented high-resolution NLOS`.

## Repository audit

Searches for the exact title, DOI `10.1063/5.0331605`, and the token `QCDC` returned no match in the current repository corpus at the time of this run. The paper should therefore be treated as a genuine missing item rather than a venue/title duplicate.

## Guarded integration instructions

Do **not** replace large public files from partial/truncated content. Integrate only after fetching the complete current versions.

### README.md

Add to **Latest Additions** near the other 2026 active transient acquisition/reconstruction papers:

```markdown
| 2026 | [Non-line-of-sight super-resolution imaging with quasi-constant-delay circular pattern](https://doi.org/10.1063/5.0331605) — Tian et al. | APL Photonics 11(7), 076122 (2026) | Jointly designs quasi-constant-delay circular relay-wall sampling and a QSR temporal super-resolution algorithm, computationally lifting 200 ps measurements to 20 ps effective timing resolution and enabling 256×256 reconstruction from a 15×64 acquisition pattern; the processed transients remain compatible with f-k, phasor-field, and other standard NLOS reconstruction backends. |
```

Also add a concise 2026 timeline node under active transient acquisition / hardware-algorithm co-design, preferably adjacent to adaptive spiral scanning, pulse multiplexing, sub-pixel/sparse acquisition, or consumer-SPAD entries.

### Website / paper explorer

Add one canonical paper object to the source that feeds `index.html` / Paper Explorer (currently `data/papers-source.html` in this repository lineage), with:

- title: `Non-line-of-sight super-resolution imaging with quasi-constant-delay circular pattern`
- authors: `Xiaorui Tian; Kai Qiao; Xiaojie Shi; Meng Tang; Siqi Zhang; Chenfei Jin`
- year: `2026`
- venue: `APL Photonics 11(7), 076122`
- DOI / primary link: `https://doi.org/10.1063/5.0331605`
- category: active NLOS / transient imaging / acquisition / super-resolution
- short summary: QCDC sampling + QSR temporal super-resolution; 200 ps → 20 ps effective timing; 15×64 sampling for 256×256 reconstruction; compatible with f-k / phasor-field reconstruction.

Expose it in Latest Additions and in the 2026 timeline without duplicating the same canonical record.

### Survey source

Integrate into the active-NLOS section that discusses acquisition efficiency, timing resolution, sparse scanning, scan-free systems, pulse multiplexing, or consumer SPADs (in the current modular source this is expected to be under `article/2active.tex`; verify the exact current structure before editing).

Suggested literature-review sentence, adapted to local style:

```latex
Tian \textit{et al.} further co-designed relay-wall sampling and temporal recovery through a quasi-constant-delay circular acquisition pattern and a quasi-constant-delay super-resolution algorithm, using deliberately shifted transient measurements to computationally improve the effective timing resolution from 200~ps to 20~ps while retaining compatibility with standard f--k and phasor-field reconstruction backends~\cite{tianQCDCQSRNLOS2026}. This direction shifts part of the temporal-resolution burden from specialized detector hardware to acquisition geometry and inverse processing, which is particularly relevant to consumer-grade SPAD deployment.
```

Place this semantically near discussion of under-scanning, sparse/adaptive trajectories, temporal super-resolution / pulse multiplexing, real-time scan-free acquisition, and consumer LiDAR/SPAD hardware; do not append it as an isolated list item at the end of the survey.

### Bibliography

Merge the staged entry from `egbib_20260830_qcdc_qsr_nlos_gap.bib` into the bibliography actually used by the survey build, preserving the canonical key:

`tianQCDCQSRNLOS2026`

Deduplicate by DOI `10.1063/5.0331605` before merging.

### PDF rebuild / consistency checks

After source integration, run a clean LaTeX build using the repository’s actual bibliography workflow (typically `pdflatex → bibtex → pdflatex → pdflatex`, unless the current project specifies otherwise) and regenerate `bare_jrnl.pdf`.

Verify all of the following before committing the PDF:

1. `README.md` contains exactly one public paper entry for DOI `10.1063/5.0331605`.
2. The website/Paper Explorer contains exactly one canonical paper object for the DOI.
3. Survey prose contains `\cite{tianQCDCQSRNLOS2026}` in the semantically appropriate active-acquisition section.
4. The active bibliography contains exactly one BibTeX record for the DOI and citation key.
5. The `.aux/.bbl` resolves the citation with no undefined-reference warning.
6. `bare_jrnl.pdf` visibly contains both the new discussion and bibliography entry.
7. No existing recent additions are lost while updating the large files.

Until these checks pass, do not claim that `bare_jrnl.pdf` has been updated.
