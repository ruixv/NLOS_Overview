# 2026-10-24 — PathFinder final-venue correction and GeRaF lineage integration

## High-confidence bibliography and citation audit

This pass rechecked previously catalogued papers against publisher/academic-institution records rather than assuming that their original arXiv links were still the final venues. It also inspected **all LaTeX chapter citation keys** for already catalogued but uncited 2024–2026 works.

1. **PathFinder: Attention-Driven Dynamic Non-Line-of-Sight Tracking with a Mobile Robot**, Shenbagaraj Kannapiran, Sreenithy Chandran, Suren Jayasuriya and Spring Berman. **IEEE/RSJ IROS 2024, pp. 12880–12887**, [DOI 10.1109/IROS58592.2024.10801990](https://doi.org/10.1109/IROS58592.2024.10801990). Its repository catalog record previously labeled the paper **arXiv 2024**, although a final IEEE conference publication is verifiable from the [Arizona State University institutional record](https://asu.elsevierpure.com/en/publications/pathfinder-attention-driven-dynamic-non-line-of-sight-tracking-wi/). The website, README, and BibTeX now use the final venue. `article/3passive.tex` now explains its moving-camera RGB-based hidden-person tracking and differentiates it from fixed-view PAC-Net.
2. **GeRaF: Neural Geometry Reconstruction from Radio Frequency Signals**, Jiachen Lu, Hailan Shanbhag and Haitham Al Hassanieh. **NeurIPS 2025, Vol. 38**, [DOI 10.52202/085713-3151](https://doi.org/10.52202/085713-3151), publisher page [NeurIPS Proceedings](https://papers.nips.cc/paper_files/paper/2025/hash/8766fbc68e1ed1cdef712ce273e0a363-Abstract-Conference.html). This original RF-only implicit reconstruction work was already in the merged bibliography, but missing from README, the paper explorer, and LaTeX survey. The README, `data/papers-source.html`, `index.html` and `article/5newscenes.tex` now explain its use of physically based differentiable RF rendering and its relationship to **GeRaF 2.0**, *Seeing through boxes* (CVPR 2026), which adds visible exterior geometry as an additional physical anchor.

## Files and consistency

- `README.md`: correct PathFinder final venue and add GeRaF NeurIPS 2025 to the historical radar timeline.
- `index.html`: update the Core Reading Path with the verified IROS/NeurIPS trajectory.
- `data/papers-source.html`: update PathFinder metadata; add GeRaF; adjust manually displayed tracked-entry count **401 to 402**.
- `article/3passive.tex`: add PathFinder mobile passive-tracking literature review.
- `article/5newscenes.tex`: add GeRaF RF neural inverse-rendering lineage.
- `egbib_merged_20260711.bib`: replace obsolete PathFinder arXiv-only entry with final IROS metadata (same citation key); add NeurIPS proceedings DOI to existing GeRaF BibTeX entry (same citation key).

The root `bare_jrnl.tex` already imports both updated chapters; modifying that root file is unnecessary. Existing paper keys are reused, not duplicated.

**PDF verification:** after the source changes reach `master`, `.github/workflows/rebuild_nlos_citation_gap_pdf_20260718.yml` is expected to rebuild `bare_jrnl.pdf`. An actual successful workflow and changed PDF binary blob SHA must be verified before claiming that the public PDF includes this backfill.

**Scope note:** This update concerns publication corrections and previously omitted survey/web coverage; it is not a claim that the entire forward-citation graph of Velten, LCT, f--k, phasor-field, or other core papers was exhausted.
