# RF NLOS venue and survey reconciliation — 14 October 2026

## Verified final publications
- Xin Tong, Lechen Zhang, Yu Ge, Dario Tagliaferri, Henk Wymeersch, *NLOS-Aided Joint OTA Synchronization and Off-Grid Imaging for Distributed MIMO Systems*. **IEEE Transactions on Wireless Communications**, 2026 (early access), DOI: 10.1109/TWC.2026.3732875. Verified using Chalmers University publication record (updated 22 September 2026). Previously labeled arXiv 2603.13981.
- Xi Zhang, Yu Ge, Ossi Kaltiokallio, Musa Furkan Keskin, Henk Wymeersch, Mikko Valkama, *Exploiting Double-Bounce Paths in Snapshot Radio SLAM: Bounds, Algorithms and Experiments*. **IEEE Transactions on Wireless Communications** 25 (2026), 20836–20851, DOI: 10.1109/TWC.2026.3713594. Verified using Chalmers and Tampere University publication records. Previously labeled arXiv 2603.02832.
- Jiahui Chen et al., *Joint Localization of LOS and NLOS Targets With Clutter Mitigation via Multipath Exploitation Radar*. **IEEE Transactions on Radar Systems** 3 (2025), 549–561, DOI: 10.1109/TRS.2025.3550023. Verified against IEEE Xplore. Previously present in merged bibliography but absent from the public paper list and uncited in the survey.

## Integration
- README latest additions, existing core entries and development timeline: two final-venue corrections and one missing paper.
- data/papers-source.html paper explorer: venue/DOI corrections, new IEEE TRS record, and 2025/2026 RF timeline context.
- index.html Core Reading Path: a concise RF multipath paragraph with all three publisher links.
- article/5newscenes.tex: a semantically placed paragraph in the Radar-Based NLOS Imaging section citing all three canonical BibTeX keys.
- egbib_merged_20260711.bib: update Tong and Zhang from arXiv-only to final IEEE journal records; preserve Chen's already correct journal entry.
- bare_jrnl.tex already imports article/5newscenes.tex. No duplicate citation or section is needed.

## PDF rebuild remains outstanding
**Do not claim that bare_jrnl.pdf is current.** The previously verified PDF blob SHA was `6fc5e00f2a7aee93692f6ee41a7074a4c59de9e6`. The execution container has latexmk and pdflatex, but cannot resolve github.com to retrieve the complete source tree and all required figures/assets; GitHub connector access to text files does not constitute a local full checkout. No new PDF was compiled or uploaded.

From a complete checkout, run `latexmk -pdf -interaction=nonstopmode -file-line-error bare_jrnl.tex`, check the bibliography and compilation log for undefined references or missing figures, then commit the validated bare_jrnl.pdf. Keep the old PDF until this succeeds.

## Scope
The IEEE TWC papers are tightly adjacent RF/ISAC environmental imaging and hidden-landmark mapping, **not** direct substitutes for optical transient 3D NLOS reconstruction. They are categorized as radar/RF NLOS extensions, not as core optical milestones.
