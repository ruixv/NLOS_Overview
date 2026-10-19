# NLOS citation-tracing update — 20 October 2026

## Newly integrated, verified works

1. **Woodford, Qian, Zhang, Metasight: High-Resolution NLoS Radar with Efficient Metasurface Encoding.** ACM SenSys 2023, pp. 308–321. DOI: 10.1145/3625687.3625803. Publisher and DBLP confirm the final conference record. A passive compact metasurface and angular encoding enable around-corner automotive radar sensing, not dense 3D imaging.
2. **Angjo, Zubow, Laskos, Dressler, Demo: Now You See It! RIS-Assisted mmWave Radar for NLOS Sensing.** Accepted ACM MobiCom 2026 demo, three pages, conference 26–30 October 2026. Accepted-demos listing: https://www.sigmobile.org/mobicom/2026/accepted_demos.html ; author PDF: https://www.tkn.tu-berlin.de/bib/angjo2026now/angjo2026now.pdf . DOI 10.1145/3795866.3848436 appears in the author PDF; ACM publisher landing record not independently verified yet. Uses a 28-GHz monostatic FMCW radar, programmable RIS, reference/target difference maps and a single static passive hidden target; controlled detection/rough localization rather than volumetric reconstruction.

## Citation-tracing chain and inclusion policy

The accepted 2026 MobiCom demonstration directly cites **Metasight** as reference [5], as well as the 2024 RIS around-corner sensing work by Yasmeen et al. and 2024 MobiCom RFlect. Its related-work section distinguishes passive fixed-angle metasurfaces from programmable RIS beam steering. Metasight is a missing full SenSys paper, while the 2026 work is a new verified accepted demonstration. Both were absent from README, Paper Explorer, bibliography and the radar/RF survey section before this update. The survey already cited the CVPR 2026 RISE work under key zhouRISE2026; it was not duplicated. Other citation leads (e.g., Horus) were not added solely for being cited because their sensing geometry/task is more peripheral.

## Cross-artifact changes

README: Latest Additions, radar/RF table, milestone timeline. index.html: Core Reading Path RF relay context. data/papers-source.html: Paper Explorer records and development timeline. article/5newscenes.tex: semantically placed literature-review paragraph in Radar-Based NLOS Imaging. bare_jrnl.tex: dated integration comment; chapter remains included by existing \\input. egbib_merged_20260711.bib: keys woodfordMetasight2023 and angjoRISDemo2026.

## PDF status / remaining steps

**PDF NOT REBUILT in this run.** Source consistency does not imply binary PDF consistency. Rebuild in a complete repository checkout with all figures and installed TeX packages:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex
pdftotext bare_jrnl.pdf - | grep -Ei 'Metasight|Now You See It'
```

Then verify zero undefined citations and no duplicate bibliography keys, inspect output and commit bare_jrnl.pdf. If CI/build fails, retain the source commit and this explicit pending record. Do not claim PDF updated until its blob SHA changes and a successful build is verified.
