# 2026-08-28 — Active NLOS human-detection gap

## Verified missing paper

Semra Çelebi and İbrahim Türkoğlu, “Machine Learning-Based Human Detection Using Active Non-Line-of-Sight Laser Sensing,” *Sensors*, 26(7), 2046, 2026. DOI: 10.3390/s26072046. Published 25 March 2026.

Primary metadata: MDPI Sensors and PubMed (PMID 41977832). The paper is genuinely NLOS sensing rather than generic classification: it uses a pulsed-laser / galvanometer / SPAD / TCSPC active NLOS setup, records wall-mediated time–photon histograms in rubble-like hidden-human scenes, and compares CNN, bidirectional-GRU and Random-Forest classifiers for human-presence detection. The paper reports full sensitivity for human-present samples and >97% overall accuracy for the best Random-Forest model. It explicitly situates the work relative to transient NLOS human pose estimation, NLOST, and MARMOT, making it a relevant semantic/task-oriented extension of learned transient NLOS.

## Repository audit

Searches by full title, DOI `10.3390/s26072046`, and author names returned no current repository match. Do not confuse this work with existing transient human-pose reconstruction/localization entries: this paper targets binary hidden-human presence detection from experimentally measured SPAD–TCSPC waveforms.

## Required public integration

1. **README.md / Latest Additions** — add a 2026 row under active / learned semantic sensing:
   - venue: `Sensors 26(7), 2046 (2026)`
   - contribution: real SPAD–TCSPC hidden-human dataset in rubble-like scenes; CNN/GRU/RF comparison; task-level human-presence detection instead of full scene reconstruction.
2. **README.md / 2026 timeline** — add a short milestone after transient pose / semantic sensing entries: `SPAD–TCSPC transient measurements are used directly for hidden-human presence classification, extending NLOS from reconstruction to low-cost task-level search-and-rescue sensing.`
3. **Website canonical corpus** — add one paper object to `data/papers-source.html` (and let the existing graph/explorer generation path expose it in `index.html` rather than maintaining a duplicate hard-coded list). Recommended family: `learning` or `active`, with keywords including `SPAD`, `TCSPC`, `human detection`, `semantic sensing`, `search and rescue`.
4. **Survey source** — integrate semantically in the active detection/tracking/recognition or data-driven semantic-NLOS discussion (not merely as a trailing list). Suggested sentence:
   `Task-oriented transient sensing has also moved beyond geometric reconstruction: Çelebi and Türkoğlu use experimentally measured SPAD–TCSPC time–photon waveforms from rubble-like NLOS scenes to compare convolutional, recurrent, and ensemble classifiers for hidden-human presence detection, showing that low-cost transient hardware can support semantic search-and-rescue decisions without reconstructing a full hidden volume \cite{celebiActiveNLOSHumanDetection2026}.`
5. **Bibliography** — merge the staged entry `celebiActiveNLOSHumanDetection2026` from `egbib_20260828_active_human_detection_gap.bib` into the bibliography actually used by `bare_jrnl.tex`; ensure the DOI occurs once.
6. **PDF** — clean rebuild only after source integration: `pdflatex -> bibtex -> pdflatex -> pdflatex`; verify the citation key resolves in `.aux/.bbl`, extracted PDF text contains the new semantic-sensing discussion and bibliographic entry, and render representative pages before committing `bare_jrnl.pdf`.

## Safety / current state

The connector available in this run performs whole-file replacements for large existing files, so README / canonical corpus / large LaTeX sources were not overwritten blindly. The staged BibTeX and this precise insertion note are safe to merge now. Do **not** claim `bare_jrnl.pdf` contains this paper until the guarded clean build and cross-artifact checks succeed.
