# 8 August 2026 — mmWave / ISAC NLOS citation-trace integration note

## Status

This update was produced from a fresh keyword, lab-page, bibliographic-index, and forward-citation audit of the NLOS literature. Two actionable records were identified in the cellular-mmWave / ISAC branch:

1. **Final-venue correction:** the repository already contains *Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware* by Tosi et al., but README.md and index.html currently label it as `arXiv 2026`. It is a published conference paper in the **32nd International Conference on Telecommunications (ICT 2026)**, Thessaloniki, Greece, May 2026, pp. 25–30. The final venue is independently listed by DBLP and the KIT Communications Engineering Lab publication page. The arXiv page (`arXiv:2604.07032`) remains a useful public full-text link; no publisher DOI was added here because a DOI was not independently recovered during this run.
2. **Missing direct precursor:** *Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave* by Tosi, Henninger, Giroto de Oliveira, and Mandelli is not present in the current README / website explorer / survey source. It is a final **IEEE SPAWC 2024** paper, pp. 331–335, DOI `10.1109/SPAWC60668.2024.10694426`. It uses a 27.4-GHz 5G/mmWave ISAC proof-of-concept in a factory-like environment, studies TDD-induced spectral replicas and CSI-processing strategies, and experimentally establishes NLOS target-detection feasibility. The ICT 2026 paper is the follow-up that turns this feasibility study into robust intrusion detection and tracking.

**Integration completed on 8 August 2026.** The bounded changes described below were applied to README.md, index.html, article/5newscenes.tex, bare_jrnl.tex, and the bibliography, followed by a clean LaTeX/BibTeX rebuild and PDF consistency checks. The note is retained as the provenance record for the cellular-ISAC citation trace.

## 1. README.md

### A. Correct the existing ICT record

Find the existing row whose title is:

`Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware`

Keep its arXiv link if desired, but change the venue field from:

`arXiv 2026`

to:

`32nd International Conference on Telecommunications (ICT 2026), pp. 25–30`

Recommended concise contribution text:

> Uses 5G/mmWave ISAC hardware and large-surface reflections for fully occluded intrusion sensing in an industrial environment; range–Doppler processing and PHD-based tracking improve target persistence and false-alarm robustness beyond the earlier feasibility study.

### B. Add the missing SPAWC 2024 precursor

Insert in the RF/mmWave / ISAC portion of Latest Additions and in the corresponding 2024 development lineage:

```markdown
| 2024 | [Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave](https://doi.org/10.1109/SPAWC60668.2024.10694426) — Tosi et al. | IEEE SPAWC 2024, pp. 331–335 | Demonstrates NLOS target detection using a 27.4-GHz 5G/mmWave ISAC proof-of-concept in a factory-like environment. It evaluates CSI-processing strategies for suppressing TDD-induced spectral replicas and establishes the experimental precursor to the 2026 ICT intrusion-detection and tracking system. |
```

## 2. index.html

### A. Correct the existing ICT paper object

Find the object with title:

`Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware`

Change only the stale venue metadata (and, optionally, expand the key):

```javascript
{cat:"latest modality",title:"Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware",authors:"Tosi et al.",year:2026,venue:"ICT 2026, 25–30",url:"https://arxiv.org/abs/2604.07032",key:"5G/mmWave ISAC hardware uses large-surface reflections, range-Doppler processing, and PHD-based tracking for reliable fully NLOS intrusion detection in an industrial environment."},
```

### B. Add the missing SPAWC paper object

Add near the other RF/mmWave / ISAC records:

```javascript
{cat:"latest modality",title:"Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave",authors:"Tosi et al.",year:2024,venue:"IEEE SPAWC 2024, 331–335",url:"https://doi.org/10.1109/SPAWC60668.2024.10694426",key:"Commercial 27.4-GHz 5G/mmWave ISAC hardware detects NLOS targets in a factory-like environment; CSI processing mitigates TDD-induced spectral replicas and establishes the experimental precursor to the 2026 ICT tracking system."},
```

The current explorer count is 267. This correction changes no count, while the newly added SPAWC record increases the expected count to **268**.

### C. Timeline wording

In the 2024 timeline paragraph, append a short phrase such as:

> A commercial 27.4-GHz 5G/mmWave ISAC prototype also established experimentally that standard-oriented cellular hardware can detect fully NLOS targets after compensating TDD-induced sensing artifacts.

In the 2026 timeline paragraph, append:

> The ICT follow-up converted that ISAC feasibility result into reliable industrial NLOS intrusion monitoring with explicit target tracking and false-alarm stress tests.

## 3. article/5newscenes.tex and bare_jrnl.tex

The survey is modular: `bare_jrnl.tex` inputs `article/5newscenes.tex`. Insert the following paragraph in **New NLOS Scenes → Radar-Based NLOS Imaging**, preferably after the introductory HoloRadar paragraph and before the broader `Recent RF/mmWave work further expands...` paragraph. This makes the cellular-ISAC lineage part of the narrative rather than a detached list.

```latex
\vspace{0.8mm}
\noindent \textbf{Cellular ISAC hardware for NLOS sensing.}
A complementary 5G/6G ISAC trajectory asks whether communication hardware can use multipath as an around-corner sensor rather than treating it only as a channel impairment. Tosi~\etal~first demonstrated the feasibility of NLOS target detection with a 27.4~GHz commercial mmWave ISAC proof-of-concept, including channel-state-information processing that suppresses spectral replicas caused by time-division-duplex gaps~\cite{tosiFeasibilityISACNLOS2024}. The later ICT study moved from feasibility to reliable intrusion monitoring of fully occluded moving targets, adding range--Doppler detection and probability-hypothesis-density filtering for tracking and false-alarm rejection in an industrial testbed~\cite{tosiReliableISACNLOS2026}. Together, these works connect radar NLOS with standards-compatible cellular infrastructure and show a deployment path in which communication radios become opportunistic hidden-region sensors.
```

Also add a top-of-file maintenance comment to `bare_jrnl.tex`, e.g.:

```latex
% 8 August 2026 citation trace: SPAWC 2024 cellular-ISAC NLOS precursor integrated and ICT 2026 follow-up corrected to its final venue.
```

## 4. Bibliography

Add the following entries to the canonical bibliography source and regenerate `egbib_merged_20260711.bib` using the repository's normal merge script/workflow. If the merged file is edited directly, preserve duplicate-free key normalization.

```bibtex
@inproceedings{tosiFeasibilityISACNLOS2024,
  author = {Tosi, Paolo and Henninger, Marcus and Giroto de Oliveira, Lucas and Mandelli, Silvio},
  title = {Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave},
  booktitle = {2024 IEEE 25th International Workshop on Signal Processing Advances in Wireless Communications (SPAWC)},
  pages = {331--335},
  year = {2024},
  doi = {10.1109/SPAWC60668.2024.10694426},
  url = {https://doi.org/10.1109/SPAWC60668.2024.10694426}
}

@inproceedings{tosiReliableISACNLOS2026,
  author = {Tosi, Paolo and Bauhofer, Maximilian and Henninger, Marcus and Schmalen, Laurent and Mandelli, Silvio},
  title = {Reliable Non-Line-of-Sight Intrusion Detection with Integrated Sensing and Communications Hardware},
  booktitle = {32nd International Conference on Telecommunications (ICT 2026)},
  pages = {25--30},
  year = {2026},
  address = {Thessaloniki, Greece},
  month = {May},
  note = {Conference held in May 2026; also available as arXiv:2604.07032},
  url = {https://arxiv.org/abs/2604.07032}
}
```

Do not add a DOI to the ICT entry unless it is independently verified from the publisher/index record.

## 5. Rebuild and consistency checks

After applying the bounded source edits:

1. Regenerate the merged bibliography if the repository uses source `.bib` fragments.
2. Compile `bare_jrnl.tex` with the same LaTeX/BibTeX sequence used by the existing validated update workflow.
3. Commit the regenerated `bare_jrnl.pdf` only if compilation succeeds.
4. Verify that both Tosi papers resolve as citations in the PDF and that the ICT record is shown as ICT 2026 rather than arXiv 2026.
5. Verify the website explorer reports 268 records and contains exactly one entry for each Tosi paper.
6. Search README.md, index.html, article/5newscenes.tex, bare_jrnl.tex / merged bibliography, and extracted PDF text for both titles or citation keys.
7. Render at least the first page and the radar/ISAC survey page to catch LaTeX/layout regressions.

## 6. Evidence and scope notes

Verified metadata sources used in this run:

- KITopen final record for SPAWC 2024: https://publikationen.bibliothek.kit.edu/1000177265
- DOI for SPAWC 2024: https://doi.org/10.1109/SPAWC60668.2024.10694426
- DBLP SPAWC record: https://dblp.org/rec/conf/spawc/TosiHOM24
- KIT Communications Engineering Lab publication list for the ICT 2026 final venue: https://www.cel.kit.edu/english/team_schmalen.php
- DBLP ICT 2026 proceedings record: https://dblp.org/rec/conf/ict/TosiBHSM26
- Public full text for the ICT follow-up: https://arxiv.org/abs/2604.07032

The SPAWC paper is tightly relevant to the repository scope because it performs experimental fully NLOS target sensing with real mmWave/5G ISAC hardware rather than merely discussing NLOS propagation. The ICT paper is its direct application-oriented follow-up and should be kept in the semantic RF/mmWave NLOS branch, not described as hidden-shape reconstruction.

## 7. Citation-tracing result for this run

A forward-citation pass over the consumer-LiDAR / deployable active-NLOS lineage resurfaced several highly relevant 2026 works (including laser-pulse-multiplexed super-resolution NLOS and 3.3-km scanning-free laser reflective tomography), but those titles are already present in README and the active-survey citation list. The actionable gap was therefore the cellular-ISAC lineage above: one genuinely missing final paper (SPAWC 2024) and one stale arXiv-only venue label that now has a verified final ICT 2026 record.
