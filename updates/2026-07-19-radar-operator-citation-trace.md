# 19 July 2026 radar/THz NLOS citation trace

STATUS: STAGED — source synchronization and PDF rebuild are pending.

## Search and verification scope

This run repeated the recent-paper sweep across arXiv, publisher pages, conference/journal indexes, project/lab pages, and core-paper citation paths. The optical forward-citation pass around Velten 2012, LCT, f-k migration, and the Liu phasor-field lineage surfaced no additional high-confidence work newer than the records already integrated on 19 July. In particular, *Stereo non-line-of-sight imaging* and *Compact non-line-of-sight imager at long range* were re-verified but are already present in the README/homepage/survey/bibliography and were not duplicated.

The modality-expansion pass around HoloRadar, RF/mmWave NLOS reconstruction, and terahertz around-corner imaging identified two genuine omissions. Both papers reconstruct hidden 3D targets from measured NLOS radar returns, preserve explicit propagation operators, and are substantially closer to the repository's imaging/reconstruction scope than adjacent detection-only or communication-only NLOS papers.

## Newly integrated papers

### RM Operator Learning-driven Non-line-of-sight 3D Imaging Method for Millimeter Wave Radar

- Authors: Kun Chen, Shunjun Wei, Xiang Cai, Mou Wang, Hao Zhang, Guolong Cui, Xiaoling Zhang, Siyuan Chen
- Venue: *Journal of Radars*, 15(1), 42–63, 2026
- DOI: `10.12000/JR25132`
- Publication date: 5 January 2026; issue date February 2026
- Contribution: introduces a fast range-migration kernel and unfolds FISTA into an NLOS-specific 3D reconstruction network. The measured near-field platform evaluates ideal and non-ideal reflectors, reduced sampling ratios, and multiple metallic targets, reporting approximately two orders of magnitude faster reconstruction than conventional sparse imaging.

### Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging

- Authors: Kun Chen, Shunjun Wei, Mou Wang, Juran Chen, Bingyu Han, Jin Li, Zhe Liu, Xiaoling Zhang, Yi Liao, Pengcheng Gao, Xiaolin Mi
- Venue: *Photonics*, 13(5), Article 440, 2026
- DOI: `10.3390/photonics13050440`
- Published: 30 April 2026
- Contribution: embeds a fast holographic imaging operator in FISTA-Net for a measured 121 GHz sub-THz around-corner setup. It addresses phase errors, aperture shadowing, multipath mismatch, memory growth, and slow iterative inversion while reconstructing hidden metal targets.

## Intended synchronization

The guarded synchronizer updates:

1. `README.md` latest additions and the 2026 development timeline.
2. `index.html` paper explorer, 2026 timeline, and tracked-entry statistic.
3. `article/5newscenes.tex`, adding semantically placed operator-learning paragraphs to the radar/RF/mmWave and terahertz subsections.
4. `bare_jrnl.tex`, advancing the update coverage date to 19 July 2026 and recording the integration marker.
5. `egbib_merged_20260711.bib` through the repository's deterministic bibliography merger.
6. `bare_jrnl.pdf` only after a clean LaTeX/BibTeX build, undefined-citation audit, bibliography deduplication check, PDF text verification, and page rendering.

## Latest-paper check

No directly relevant NLOS imaging paper later than *Non-line-of-sight imaging via physics-informed cascade learning*, published 15 July 2026, was verified during this run. A SIGGRAPH 2026 item published online on 19 July was not added because the available public metadata did not establish direct hidden-scene imaging or reconstruction relevance.

<!-- workflow trigger: radar-operator synchronization -->
