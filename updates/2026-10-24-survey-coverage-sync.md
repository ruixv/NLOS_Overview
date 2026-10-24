# 2026-10-24 — Survey coverage sync for catalogued NLOS research

## Scope and outcome

A fresh literature and core-paper forward-citation screening did not independently verify a new paper missing from the README, paper explorer, and merged bibliography. A cross-artifact audit nonetheless found **two already catalogued 2026 papers** that were not cited anywhere in the LaTeX survey. Both have now been integrated into semantically appropriate article sections, without adding duplicate discovery entries or duplicate BibTeX records.

| Paper | Final verified venue | Existing bibliography key now used | Survey location |
| --- | --- | --- | --- |
| Y. Ling et al., *Symmetry-Aware Gradient Coordination for Physics-Guided Non-Line-of-Sight Imaging* | *Symmetry* 18(5), 711 (2026), DOI [10.3390/sym18050711](https://doi.org/10.3390/sym18050711) | `lingSymmetryAwareGradientNLOS2026` | `article/4datadriven.tex`, network combined with physical models; distinguishes gradient coordination from scalar regularization and learned inverse filters |
| F. Doğan, *Early fusion of laser and acoustic features for human orientation detection in non-line-of-sight environments* | *Scientific Reports* 16, 25124 (2026), DOI [10.1038/s41598-026-52682-6](https://doi.org/10.1038/s41598-026-52682-6) | `doganLaserAcousticNLOSOrientation2026` | `article/5newscenes.tex`, acoustic NLOS imaging; explicitly labels orientation classification as semantic sensing rather than hidden-image reconstruction |

Publisher metadata was checked on the [Symmetry article page](https://www.mdpi.com/2073-8994/18/5/711) and [Scientific Reports article page](https://www.nature.com/articles/s41598-026-52682-6). The latter explicitly notes that matched laser-only and acoustic-only baselines were not evaluated; the survey text does not claim a demonstrated fusion advantage.

## Existing-coverage and alias audit

The current README and `data/papers-source.html` already list both works with final venues, contribution descriptions, and DOI links. Their BibTeX records also already exist in `egbib_merged_20260711.bib`. **No new paper entry or duplicate BibTeX record is warranted.**

A check of the seven LaTeX chapters and `bare_jrnl.tex` revealed other unused 2026 bibliography keys that refer to works *already cited under different keys*: thermal NLOS, open-pit radar/LiDAR, diffuse-aware passive NLOS, acoustic CorridorLocNet, and active human detection. There are also two separate BibTeX records for the same Symmetry paper. The 2026 arXiv variant `yasmeenRISRadar2026` corresponds to a paper whose final venue is already correctly catalogued as IEEE MAPCON 2024; no 2026 duplicate entry was added. These are duplicate bibliographic aliases rather than evidence of missing survey coverage. Bibliography de-duplication is a separate maintenance task and is not performed in this patch.

## Build and verification

The master LaTeX entry point already includes both edited files through `\\input{article/4datadriven.tex}` and `\\input{article/5newscenes.tex}`. The repository PDF workflow (`.github/workflows/rebuild_nlos_citation_gap_pdf_20260718.yml`) runs on pushes to `master` that touch `article/*.tex`, recompiles `bare_jrnl.pdf`, checks for undefined citations, and commits the regenerated binary.

**Status at source commit:** the two chapter files are updated; `bare_jrnl.pdf` must be rebuilt and verified after merge before binary/public-facing PDF consistency can be declared. Check the Actions build conclusion and confirm that `bare_jrnl.pdf` has a new Git blob SHA. Do not treat this note or a triggered build as proof of successful compilation.

The forward-citation screening in this run was targeted rather than an exhaustive harvest of every core paper's citations; further OpenAlex/Semantic Scholar citing-paper pagination remains a useful follow-up.
