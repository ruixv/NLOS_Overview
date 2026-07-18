# Acoustic NLOS citation-tracing and consistency update — 18 July 2026

## Verified missing / incomplete records

### Ultrasound synthetic aperture non-line-of-sight imaging

- Authors: Tailin Li, Ilya Starshynov, Khaled Kassem, Zongliang Xie, Ge Ren, Yihan Luo, Daniele Faccio
- Final venue: Communications Physics 8, Article 432 (2025)
- DOI: 10.1038/s42005-025-02335-3
- Published: 17 November 2025
- Relevance: direct acoustic NLOS 3D reconstruction. The paper explicitly cites Velten 2012, LCT, f-k migration, phasor fields, Fermat paths, computational periscopy, and the NLOS Overview survey. It transfers the optical transient/f-k framework to coherent ultrasound synthetic apertures and reports approximately 1 cm lateral/depth resolution at meter-scale hidden ranges.
- Repository gap before this update: the survey text already mentioned an ultrasound system through `ultrasoundNLOS2025`, but the merged bibliography lacked that key and the paper was absent from README and the homepage paper explorer.

### Passive acoustic non-line-of-sight localization without a relay surface

- Authors: Tal I. Sommer, Ori Katz
- Final venue: Physical Review Applied 25(2), 024064 (2026)
- DOI: 10.1103/p97k-sf71
- Published: 20 February 2026
- Relevance: tightly adjacent NLOS sensing/localization. The paper cites Velten 2012, LCT, active/passive edge-resolved NLOS, and prior acoustic NLOS, then replaces relay-wall reflection with doorway/corner knife-edge diffraction for passive 3D source localization.
- Repository gap before this update: `article/5newscenes.tex` linked only the 2025 arXiv preprint; README, homepage, and bibliography did not contain the verified Physical Review Applied version.

## Guarded integration plan

The synchronizer updates:

1. `README.md` with one entry per final publication and acoustic-development timeline notes.
2. `index.html` paper explorer, 2025/2026 timeline, and the automatically derived tracked-entry count.
3. `article/5newscenes.tex` with a final-venue ultrasound discussion and a cited relay-free acoustic diffraction paragraph.
4. `egbib_merged_20260711.bib` through the repository's deterministic bibliography merger.
5. `bare_jrnl.pdf` through a clean LaTeX/BibTeX build.
6. Cross-file validation for unique public entries, survey citations, BibTeX records, bibliography output, extracted PDF text, and rendered PDF pages.

The final journal versions are used instead of the earlier conference abstract or arXiv record. The workflow must not claim the PDF is current unless the clean build and consistency checks succeed.
