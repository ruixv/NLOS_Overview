# 2026-08-29 acoustic NLOS localization review gap

## Verified missing work

**Shuo Wang, Zhe Chen, Fuliang Yin, “Overview of Non-line-of-sight Sound Source Localization Techniques,” Journal of Data Acquisition and Processing, 2026(4):1026–1040. DOI: 10.16337/j.1004-9037.2026.04.008.**

The journal’s current-issue page lists the paper in issue 4, pages 1026–1040. The article page describes a systematic review of NLOS sound-source localization organized around three modeling families: multi-sensor localization, geometrical-acoustics models, and statistical-acoustics models. The article was accepted on 9 June 2026 and appears in the August 2026 issue/current-issue listing.

This work is directly relevant to the repository’s acoustic NLOS branch, but it is a **survey/review rather than a new imaging algorithm**. It should therefore be integrated conservatively as field context rather than promoted as a core technical milestone.

## Repository audit

No current repository hit was found for the exact title or DOI `10.16337/j.1004-9037.2026.04.008`.

The current README already contains substantial 2026 coverage of optical active/passive NLOS, consumer LiDAR, RF/mmWave, thermal NLOS, learned reconstruction, semantic sensing, and several acoustic NLOS works. The current survey source `article/5newscenes.tex` also explicitly treats acoustic and ultrasound sensing as an emerging modality branch. This review is therefore a genuine bibliographic/context gap, not evidence that the main acoustic trajectory is absent.

## Recommended guarded integration

1. **README.md**
   - Add the paper under **Related Surveys and Benchmarks** (preferred), not in the main milestone list.
   - Suggested concise summary: “A 2026 review of NLOS sound-source localization that organizes the field into multi-sensor, geometrical-acoustics, and statistical-acoustics approaches, providing context for the repository’s growing acoustic NLOS branch.”
   - Optionally add a lightweight 2026 timeline/context entry only if other modality-specific reviews are already represented there.

2. **Website / canonical paper corpus**
   - Add a paper record to the canonical paper source used by the Paper Explorer, categorized as `resource` / survey (or the closest existing survey category).
   - Do not classify it as an original acoustic-imaging method.
   - Ensure the website displays the final journal metadata and DOI, not a generic web-search source.

3. **LaTeX survey**
   - Integrate one short contextual sentence in the acoustic/ultrasound subsection of `article/5newscenes.tex`, near the existing discussion of acoustic NLOS localization and imaging.
   - Suggested prose in the existing survey style:

     `A recent review by Wang \etal~\cite{wangAcousticNLOSLocalizationReview2026} systematizes NLOS sound-source localization into multi-sensor, geometrical-acoustics, and statistical-acoustics families, highlighting how the acoustic branch has matured from isolated around-corner demonstrations toward a more structured sensing literature.`

   - Avoid presenting the review as a new reconstruction method.

4. **Bibliography**
   - Merge the staged entry from `egbib_20260829_acoustic_nlos_localization_review_gap.bib` into the canonical bibliography used by `bare_jrnl.tex`.
   - Preserve citation key `wangAcousticNLOSLocalizationReview2026`.

5. **PDF rebuild / consistency**
   - After guarded source integration, run a clean LaTeX/BibTeX build and regenerate `bare_jrnl.pdf`.
   - Verify the title/DOI occur exactly once in the public corpus, the survey citation resolves, and the paper is categorized as a review/resource rather than an original milestone.

## Why no large-file overwrite in this run

The available GitHub write path replaces complete files. Because README, the canonical website corpus, and the survey sources are large and have accumulated many recent edits, blindly reconstructing and overwriting them from truncated retrievals risks data loss. This note therefore records exact insertion intent while the verified BibTeX is staged separately.
