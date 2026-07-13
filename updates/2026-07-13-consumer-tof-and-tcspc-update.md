# 13 July 2026 — commodity iToF and compact TCSPC NLOS update

## Search outcome

Fresh searches across recent arXiv submissions, conference and journal pages, project/lab pages, and scholarly indexes did not reveal a newer high-confidence direct NLOS-imaging paper than the 5 July 2026 NIR raster-scanning work already tracked by the repository. Keyword/modality searching and a forward/reference-tracing pass from the repository's active ToF milestones nevertheless identified two genuine missing 2024 works.

### NIGHT — off-the-shelf indirect ToF

**NIGHT -- Non-Line-of-Sight Imaging from Indirect Time of Flight Data** — Matteo Caligiuri, Adriano Simonetto, and Pietro Zanuttigh.

The paper tackles NLOS depth reconstruction using only an off-the-shelf indirect time-of-flight sensor, without custom direct-ToF or single-photon transient hardware. Its learned model interprets the relay/bounce surfaces as a virtual mirror and recovers hidden-scene depth from multipath measurements; the authors also introduce a purpose-built synthetic dataset. The arXiv record identifies the final status as **ECCV 2024 MELEX Workshop**, so the public artifacts use that venue rather than labeling the work only as arXiv.

Source: https://arxiv.org/abs/2403.19376

### Miniaturized TCSPC electronics for single-photon NLOS

**Miniaturized time-correlated single-photon counting module for time-of-flight non-line-of-sight imaging applications** — Jie Wu, Chao Yu, Jian-Wei Zeng, Chen Dai, Feihu Xu, and Jun Zhang, **Review of Scientific Instruments 95, 035107 (2024)**, DOI `10.1063/5.0193824`.

This is direct NLOS instrumentation rather than a generic timing-electronics paper. It presents a four-channel TCSPC module with a 10 ps bin size and 27.4 ps minimum RMS timing resolution, then validates it in a 1550 nm confocal single-photon NLOS experiment. The reported setup achieves 6.3 cm lateral and 2.3 cm depth resolution at a 5 m sensor distance and 1 ms pixel dwell time. Its experiment reconstructs the hidden target with Liu et al.'s phasor-field method and explicitly situates the hardware against Velten et al. and later single-photon ToF milestones, making it a high-confidence citation-tracing addition.

Sources: https://doi.org/10.1063/5.0193824 and https://arxiv.org/abs/2404.07218

## Repository synchronization

The marker-based script `scripts/sync_nlos_20260713_consumer_tof.py` is idempotent and aborts if an expected insertion point is absent or ambiguous. It is designed to run after the pending 6G initial-access synchronizer and performs the following changes:

1. Updates the README and homepage dates to 13 July 2026.
2. Adds both papers to `README.md` with verified venues, links, and concise contributions.
3. Adds searchable objects to `index.html`, raises the tracked-latest count to 91 after the pending 6G entry, and extends the 2024 timeline with commodity iToF and compact TCSPC instrumentation.
4. Adds both works to the active-methods hardware table in `article/2active.tex`.
5. Inserts the TCSPC work into the recent SPAD/hardware discussion and NIGHT into the modulated-light/ToF-camera discussion, preserving the survey's structure and style.
6. Merges `egbib_20260713_consumer_tof_updates.bib` into the duplicate-free bibliography and audits citation keys.
7. Clean-builds and validates `bare_jrnl.pdf`; the PDF is claimed as regenerated only if LaTeX/BibTeX, `pdfinfo`, `pdftotext`, undefined-citation, missing-key, and repeated-entry checks all pass.

## Consistency target

After a successful validated build, the following keys must each appear exactly once in the merged bibliography and be present in the survey `.aux`/`.bbl` output:

- `caligiuriNIGHT2024`
- `wuMiniaturizedTCSPC2024`
- `tornielliInitialAccessNLOS2025` (pending source-level update from the previous run)

**Build result:** successful source synchronization and clean survey rebuild. README, homepage, timelines, survey narrative, canonical BibTeX records, merged bibliography, and `bare_jrnl.pdf` now consistently include NIGHT and the compact TCSPC module.
