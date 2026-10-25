# 25 October 2026: FDDA single-pixel NLOS literature integration

## Verified missing research paper

- Wendi Yang, Mingnan Le, Fang Ren, and Bo Jiang, “Frequency-domain dynamic awareness for non-line-of-sight single-pixel imaging: a frequency-aware optical-computational co-design framework,” *Journal of Electronic Imaging*, vol. 35, no. 5, article 053013, 2026 (published online 6 October 2026). DOI: https://doi.org/10.1117/1.JEI.35.5.053013.
- FDDA jointly optimizes binary illumination modulation and frequency-aware learned reconstruction for **intensity-only hidden-target NLOS single-pixel imaging**. Authors report measured PSNR of 25.1 dB, SSIM of 0.81 at 6.25% sampling, and recognizable structures at 1.56% sampling. These are reported experimental results, not new independent replications.
- Relevance: direct active NLOS hidden-scene reconstruction, bridging fixed-coded or multiband single-pixel relay acquisition with optical–computational co-design and learned inverse regularization. Categorized under active optical and learning.

## Integration locations

- `README.md`: Latest Additions, active coded single-pixel category and development timeline.
- `index.html`: Core Reading Path, latest historical trajectory.
- `data/papers-source.html`: searchable paper-explorer record, 2026 technology timeline and latest counts.
- `article/2active.tex`: subsection adjacent to compressive multi-wavelength and polarization-speckle single-pixel NLOS.
- `article/4datadriven.tex`: co-optimization comparison adjacent to diffusion-prior single-pixel work.
- `bare_jrnl.tex`: main-source integration log; included chapters provide both literature-review passages.
- `egbib_merged_20260711.bib`: publisher DOI-based `yangFDDASinglePixelNLOS2026` entry.

## Provenance, citation tracing, and build status

Publisher record: https://www.spiedigitallibrary.org/journals/journal-of-electronic-imaging/volume-35/issue-05/053013/Frequency-domain-dynamic-awareness-for-non-line-of-sight-single/10.1117/1.JEI.35.5.053013.short . Independent indexed abstract: https://www.researchgate.net/publication/415272213_Frequency-domain_dynamic_awareness_for_non-line-of-sight_single-pixel_imaging_a_frequency-aware_optical-computational_co-design_framework .

The paper was identified by fresh journal search and mapped into the core single-pixel/compressive optical lineage. Its direct forward-citation relationship to Velten/LCT/f-k/phasor-field seeds has **not** been independently verified. It was absent by normalized full title and DOI from README, Paper Explorer and merged bibliography at start of this run.

The public `bare_jrnl.pdf` file should **not be called current** until a successful source rebuild and binary GitHub SHA change are verified. Previous PDF blob SHA: `2e42376753c7097c180eecd23b52d694af5ac591` (24 October 2026 build). If Actions compilation fails, diagnose logs and retain the source changes and this build note.
