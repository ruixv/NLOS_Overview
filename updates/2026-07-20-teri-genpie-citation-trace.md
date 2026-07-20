# 20 July 2026 — two-edge passive NLOS and transient-plenoptic citation trace

## Status

**VERIFIED METADATA AND FAIL-CLOSED SYNCHRONIZER COMMITTED; PUBLIC ARTIFACT MERGE AND PDF REBUILD ARE NOT YET CLAIMED.**

The current public `README.md` still reports an update run of 19 July 2026, `index.html` still reports 165 tracked latest entries, the event-camera paper remains represented by its arXiv record, and `article/0abstract.tex` still says 150+ papers. The repository also contains earlier staged scan-free/event-camera updates that have not yet produced a source-integration or validated PDF-rebuild commit. This pass therefore does not claim that the README, website, survey sections, consolidated bibliography, or `bare_jrnl.pdf` are mutually synchronized.

## Search and citation-tracing result

The pass combined recent publisher/project/lab-page searches with forward-lineage tracing from computational periscopy, edge-resolved transient imaging, Neural Transient Fields, learnable transient inversion, and differentiable transient rendering. Repository-wide title and DOI searches found no existing coverage for the four records below.

### 1. Two-edge-resolved three-dimensional non-line-of-sight imaging with an ordinary camera

- Authors: Robinson Czajkowski and John Murray-Bruce
- Final venue: **Nature Communications 15, Article 1162 (2024)**
- DOI: `10.1038/s41467-024-45397-7`
- Published: 7 February 2024
- Canonical key: `czajkowskiTwoEdgeResolved3DNLOS2024`
- Relevance: direct passive NLOS imaging. TERI exploits the vertical and horizontal edges of a doorway as complementary computational apertures and reconstructs a full-colour hidden 3D scene from one ordinary photograph of ceiling penumbrae. This is a major missing milestone in the computational-periscopy / corner-camera trajectory, not merely a paper that mentions NLOS.

### 2. Visible Occluders as Opportunistic Apertures for Wide Field of View Non-Line-of-Sight 3D Imaging

- Authors: Robinson Czajkowski and John Murray-Bruce
- Final venue: **2025 33rd European Signal Processing Conference (EUSIPCO), pp. 701–705**
- DOI: `10.23919/EUSIPCO63237.2025.11226155`
- Canonical key: `czajkowskiVisibleOccludersNLOS2025`
- Relevance: direct forward extension of the two-edge passive lineage. It treats ubiquitous doorway edges as a computational aperture for approximately 180-degree horizontal field of view and improves range recovery for hidden objects with substantial depth extent.

### 3. Permutation Transient Attention Encoder for None-Line-of-Sight Imaging

- Authors: Wenjie Yue, Xiaxu Chen, Gangping Liu, Chutian Wang, Edmund Y. Lam, and Jun Ke
- Final venue: **Optica Imaging Congress 2024 / Computational Optical Sensing and Imaging, paper CTh5A.4**
- DOI: `10.1364/COSI.2024.CTh5A.4`
- Canonical key: `yuePermutationTransientAttention2024`
- Relevance: direct learned active-NLOS reconstruction. Transient-attention blocks and Permute-MLP mixing are used to extract more discriminative spatio-temporal features. The publisher's title uses the spelling “None-Line-of-Sight”; the repository should preserve that title while categorizing the paper as NLOS imaging.

### 4. GenPIE: A Time-Resolved Plenoptic Imager

- Authors: Ziheng Wang, Siyuan Shen, Huanyu Xu, Kaichun Qiao, Longwen Zhang, Qixuan Zhang, Qilin Sun, Shiying Li, and Jingyi Yu
- Final venue: **ACM Transactions on Graphics 45(4), pp. 1–18 / SIGGRAPH 2026**
- DOI: `10.1145/3811281`
- Online publication: 3 July 2026
- Canonical key: `wangGenPIE2026`
- Relevance: tightly adjacent transient imaging and inverse rendering, not a conventional around-corner reconstruction paper. GenPIE combines sparse real transient capture, generative 3D priors, differentiable transient path tracing, material/illumination optimization, and a spatially varying temporal response model to recover time-resolved plenoptic transport. It supports multi-bounce decomposition, time-resolved relighting, and time unwarping, and belongs in the survey's emerging neural-transient / differentiable-rendering trajectory.

## Candidate deliberately excluded

`Transient Polarimetry`, a three-page SIGGRAPH 2026 poster published online on 19 July 2026, is a verified forward citation of *Time-Gated Polarization for Active NLOS Imaging*. It was not added because the available publisher, schedule, author, and lab-page metadata establishes a transient-polarimetry framework but does not establish that the poster performs hidden-scene NLOS reconstruction. Citation alone is insufficient under the repository's relevance rule.

## Latest-publication check

No direct NLOS imaging paper with a verified publication date later than **15 July 2026** was identified. *Non-line-of-sight imaging via physics-informed cascade learning* (JOSA A, DOI `10.1364/JOSAA.593401`) therefore remains the newest date-verifiable direct NLOS publication in this pass. GenPIE was published online on 3 July 2026, and the excluded Transient Polarimetry poster is later but was not verified as NLOS imaging.

## Committed implementation

- `egbib_20260720_citation_trace_additions.bib`
  - Contains canonical, DOI-verified BibTeX for all four records.
- `scripts/sync_nlos_20260720_citation_trace.py`
  - Uses exact unique anchors and fails closed if the repository has drifted.
  - Adds all four papers to `README.md` and the website paper explorer/timeline.
  - Adds TERI and its EUSIPCO extension to the passive-method table and ordinary-camera narrative in `article/3passive.tex`.
  - Adds permutation transient attention and GenPIE to semantically appropriate parts of `article/4datadriven.tex`.
  - Advances public update dates, corrects the abstract's 150+ count to 190+, merges canonical BibTeX without duplicate keys/DOIs, recomputes the website entry count, and validates DOI/key coverage.

## Required completion procedure

1. Run from the repository root:

   ```bash
   python scripts/sync_nlos_20260720_final.py
   python scripts/sync_nlos_20260720_citation_trace.py
   ```

   The first command applies the previously staged scan-free, event-camera final-venue, and polarization-speckle consistency update. The second applies this citation-tracing pass.

2. Inspect the resulting diff. Do not continue if either synchronizer reports a missing/non-unique anchor.

3. Clean-build the survey using the repository's IEEEtran/BibTeX toolchain, for example:

   ```bash
   rm -f bare_jrnl.aux bare_jrnl.bbl bare_jrnl.blg bare_jrnl.log bare_jrnl.out
   pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
   bibtex bare_jrnl
   pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
   pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
   ```

4. Reject the build if the log contains undefined citations/references or duplicate BibTeX keys.

5. Render the regenerated `bare_jrnl.pdf` and verify that the TERI, opportunistic-aperture, transient-attention, and GenPIE paragraphs are present and visually sound.

6. Commit `README.md`, `index.html`, `article/0abstract.tex`, `article/3passive.tex`, `article/4datadriven.tex`, `bare_jrnl.tex`, `egbib_merged_20260711.bib`, and the validated `bare_jrnl.pdf` together. Only then mark the public artifacts mutually consistent.

## Current limitation

The available GitHub write path can safely create metadata, scripts, and precise update notes, but applying and validating multi-file generated edits plus a binary PDF requires an executable repository checkout or a functioning GitHub Actions runner. No successful Actions status or follow-up integration/PDF commit was present at the end of this pass. Large public files were therefore not replaced blindly, and the current PDF is explicitly not claimed as rebuilt.
