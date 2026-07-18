# 18 July 2026 visibility-limit and hidden-human NLOS follow-up

## Scope

This follow-up extends the core-paper citation-tracing pass from reconstruction methods to two tightly coupled branches that remained absent from the public repository: quantitative finite-aperture limits for hidden-object orientation estimation, and real-measurement active NLOS human detection. Both records were verified from final publisher metadata and checked against `README.md`, `index.html`, the survey sections, update logs, and bibliography fragments.

The latest direct NLOS imaging publication verified in the complete 18 July search remains **Non-line-of-sight imaging via physics-informed cascade learning**, published in *JOSA A* on **15 July 2026**. No later direct NLOS imaging paper or arXiv submission was independently verified.

## Newly integrated records

### Finite-Aperture Limits for Yaw Estimation in Confocal Non-Line-of-Sight Imaging

- Authors: Riccardo Romanelli, Lorenzo Francesco Livi, Francesco V. Pepe, Giacomo Sorelli, Enea Mauri, Milena D'Angelo, Massimiliano Proietti
- Venue: *Journal of Imaging* 12(6), 248 (2026)
- Published: 2 June 2026
- DOI: `10.3390/jimaging12060248`
- Contribution: derives a geometric switch-line criterion and Fisher-information limits for yaw observability with a finite confocal relay-wall aperture. Simulated and measured f-k/backprojection results show how angular information degrades as informative transient features leave the observed wall, converting qualitative missing-cone and visibility limitations into quantitative acquisition-design guidance.
- Citation-tracing rationale: this is a direct theoretical and experimental continuation of finite-aperture feature visibility, f-k migration, and transient backprojection rather than a paper that merely cites NLOS imaging in passing.

### Machine Learning-Based Human Detection Using Active Non-Line-of-Sight Laser Sensing

- Authors: Semra Çelebi, İbrahim Türkoğlu
- Venue: *Sensors* 26(7), 2046 (2026)
- Published: 25 March 2026
- DOI: `10.3390/s26072046`
- Contribution: builds a real SPAD–TCSPC active NLOS acquisition system for controlled rubble-like scenes and compares CNN, GRU, and random-forest classifiers on hidden-human presence across poses, orientations, and object configurations. All tested models achieve full sensitivity; random forest obtains the strongest specificity and weighted F1 under the measured limited-photon conditions.
- Inclusion rationale: the repository explicitly covers active NLOS detection, tracking, and identification. This work directly senses a hidden person from time-resolved multi-bounce measurements and is therefore a tightly adjacent NLOS sensing contribution even though it does not reconstruct a full image.

## Excluded candidate

**Non-line-of-sight imaging based on adaptive neural grid resampling** was found as an SSRN preprint dated 29 June 2026. It was not added because no independent final venue, institutional project page, or second authoritative metadata source was verified in this run. It can be reconsidered after publication or stronger metadata confirmation.

## Repository integration

- `scripts/sync_nlos_20260718_visibility_detection.py` performs guarded, idempotent edits to `README.md`, `index.html`, and `article/2active.tex`.
- `egbib_20260718_visibility_detection_updates.bib` contains the two canonical final-venue BibTeX records.
- The synchronizer adds the finite-aperture paper to the active pose-estimation line and literature narrative, and the hidden-human paper to the active detection/identification line and discussion.
- `scripts/finalize_nlos_20260718_public_counts.py` invokes the follow-up synchronizer before reconciling the website paper count, so the existing PR workflow merges the new bibliography, clean-builds the survey, regenerates `bare_jrnl.pdf`, and checks citation integrity.

No public source or PDF should be reported as integrated until the PR workflow succeeds and the resulting branch is merged.
