# NLOS citation-trace and survey-consistency backfill — 28 October 2026

## Scope and method

Repeated the forward-citation audit from the field-defining active ToF/NLOS milestones (Velten et al. 2012, O'Toole et al. 2018/LCT, Lindell et al. 2019/f-k migration, and Liu et al.'s phasor-field work), passive computational periscopy, PAC-Net/NLOS-Track, Neural Transient Fields, NLOST/TransiT/ST-Mamba/DG-NLOS, and modality-expansion seeds including acoustic NLOS, HoloRadar, consumer-LiDAR NLOS, and 3D Gaussian Transient Rendering. Checked publisher records, scholarly indexes, arXiv, and the repository's README, homepage, paper explorer, update notes, LaTeX chapter sources, and BibTeX files. Candidates were retained only when their contribution is actual NLOS reconstruction or a clearly scoped adjacent sensing task.

## Papers newly integrated into the survey narrative

- **Non-Line-of-Sight mmW SAR Imaging With Equivariant Adaptive Threshold Learning** — Xiang Cai et al., *IEEE Transactions on Computational Imaging* 11, 1190–1205 (2025), [DOI 10.1109/TCI.2025.3597462](https://doi.org/10.1109/TCI.2025.3597462). Self-supervised equivariant imaging with TV-constrained deep unfolding and adaptive thresholding reconstructs measured 2D/3D mmWave SAR images from partial, noisy, multipath-corrupted NLOS echoes. The text notes its tested specular/isolated-target regime.

- **Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging** — Kun Chen et al., *Photonics* 13(5), 440 (2026), [DOI 10.3390/photonics13050440](https://doi.org/10.3390/photonics13050440). A measured 121-GHz platform couples a multipath echo model and fast frequency-domain imaging operator to a FISTA-derived network, addressing phase error, aperture shadowing, and clutter without storing a large sensing matrix.

- **Non-Line-of-Sight Perception Method for Autonomous Haul Trucks in Open-Pit Mines Based on 4D mmWave Radar and LiDAR Fusion** — Jianjian Yang et al., *Sensors* 26(14), 4615 (2026), [DOI 10.3390/s26144615](https://doi.org/10.3390/s26144615). Blind-Spot Complementary Fusion filters multipath-corrupted radar points and injects high-confidence cues into LiDAR blind regions in real mine data. The survey explicitly classifies this as adjacent NLOS perception, not full image or shape reconstruction.

## Newly cataloged adjacent NLOS sensing papers

- **Non-Line-of-Sight Pedestrian Recognition Approach Using Multiple Reflections for Millimeter Wave Radar Sensing Applications** — Junya Okazaki, Takeru Matsuoka, Jianghaomiao He, and Shouhei Kidera, *IEICE Transactions on Communications* E108-B(11), 1338–1348 (published 1 November 2025), [DOI 10.23919/transcom.2025EBP3011](https://doi.org/10.23919/transcom.2025EBP3011). A 24-GHz FMCW radar uses slow-time multiple-reflection signatures and SVM/LSTM classification to distinguish a pedestrian from a dummy in a real-road NLOS setting. It is cataloged as target recognition, not imaging.

- **A 1.6-to-3.8GHz Reconfigurable FMCW Radar SoC with 81.5% Relative-Bandwidth PLL for Real-Time Life Detection in Disaster Response** — Renjie Fu et al., *2026 IEEE International Solid-State Circuits Conference (ISSCC)*, pp. 582–584, [DOI 10.1109/ISSCC49663.2026.11408988](https://doi.org/10.1109/ISSCC49663.2026.11408988). The 40-nm 1.6–3.8 GHz FMCW radar SoC reports life detection behind up to six walls and vital-sign sensing behind two at 0.395 W. It is recorded as adjacent through-wall NLOS sensing hardware, not image reconstruction.

## Venue and duplicate cleanup

- **Around-the-Corner Radar Sensing Using Reconfigurable Intelligent Surface** is already cited in the survey using its final IEEE MAPCON 2024 record ([DOI 10.1109/MAPCON61407.2024.10923061](https://doi.org/10.1109/MAPCON61407.2024.10923061)). Removed an unused arXiv-only duplicate key so the final venue is not shadowed by a later arXiv upload.
- **Iterating the Transient Light Transport Matrix for Non-Line-of-Sight Imaging** is cited using its final *Nature Communications* 17, 8951 (2026) record ([DOI 10.1038/s41467-026-75177-4](https://doi.org/10.1038/s41467-026-75177-4)). Removed unused arXiv-era duplicate keys and retained the final journal record in the canonical supplement.
- Recent ToF comparison, cascaded higher-order NLOS, 3D-GTR, consumer-LiDAR, MARMOT, PICL, thermal rough-surface NLOS, passive diffuse-aware attention, and other listed recent papers were checked and were already represented in the repository or survey; no duplicate catalog rows were added for them.

## Files synchronized

The additional ISSCC record is included in the catalog, Paper Explorer, survey prose, and both bibliography sources; CI checks now require its citation key and public metadata.

- `README.md`: new catalog row, timeline milestone, and corrected audit summary.
- `index.html`: visible timeline entry describing the survey backfill.
- `data/papers-source.html`: searchable Paper Explorer record for the new IEICE paper and current PDF-date label.
- `article/5newscenes.tex`: semantically placed mmWave SAR, open-pit radar/LiDAR, hidden-pedestrian recognition, and THz deep-unfolding discussion.
- `bare_jrnl.tex`: updated source-history note.
- `egbib_2026_updates.bib`: final-venue BibTeX for TLTM iteration, the three previously cataloged missing survey papers, and the new IEICE paper; stale unused arXiv duplicates removed.
- `egbib_merged_20260711.bib`: removed stale duplicate records; the build workflow re-merges it from canonical sources.
- `.github/workflows/build-nlos-survey-20261028.yml`: added consistency checks for the new citation keys and public catalog record.

## Build verification

The source changes are staged on the guarded branch `nlos-survey-consistency-20261028`. Do not consider the PDF updated until the repository's LaTeX/BibTeX workflow succeeds and the regenerated `bare_jrnl.pdf` is committed. The successful run ID, PDF page count, byte size, and final PDF blob SHA will be recorded here after CI verification.
