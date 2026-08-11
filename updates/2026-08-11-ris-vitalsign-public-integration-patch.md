# 11 August 2026 — verified RF/RIS NLOS public-integration patch

This pass re-checked recent NLOS imaging/sensing searches and forward-citation-oriented searches around the repository's core active/passive/learned/modal-expansion seeds. No additional August-2026 arXiv imaging paper was found that clearly survives the repository's relevance/metadata checks beyond the papers already present in the public corpus. The actionable gap is instead a small verified RF/RIS branch that has accurate final-venue BibTeX metadata in `egbib_20260811_ris_vitalsign_updates.bib` but is not yet represented in `README.md`, `index.html`, `bare_jrnl.tex`, or the merged bibliography used by the survey.

## Verified missing public entries

### 1. Non-Line-of-Sight Human Vital-Sign Sensing Aided by Reconfigurable Intelligent Surfaces

- Authors: Xin-yu Li, Jing-yuan Zhang, Zi-xuan Cai, Shi-long Qin, Qian Ma, Jian-wei You, Tie-jun Cui
- Venue: *Acta Electronica Sinica*, 53(1), 1–13, 2025
- DOI: `10.12263/DZXB.20240674`
- Publisher record: https://doi.org/10.12263/DZXB.20240674
- Recommended category: `modality rf ris sensing vital-sign`
- Concise contribution: Uses a visually aided RIS beam-control stage to redirect RF sensing energy into an NLOS human region, then applies improved VMD to estimate respiration and heartbeat. This is a verified semantic/physiological NLOS sensing extension rather than hidden-shape imaging, so it belongs in the RF/RIS sensing branch and should be labeled accordingly.

### 2. Liquid Crystal RIS Integrated with SIL Radar for NLOS Vital Sign Monitoring

- Authors: Chinmaya Tripathy, Rifa Atul Izza Asyari, Kuan Yuan Lee, Yuh Chyi Chang, Yi Chan Hung, Tien Lun Ting, Daniel Teichmann, Tzyy Sheng Horng, Tsung Hsien Lin
- Venue: 2025 IEEE MTT-S International Microwave Biomedical Conference (IMBioC)
- DOI: `10.1109/IMBioC63524.2025.10989670`
- Final venue verified from institutional publication metadata.
- Recommended category: `modality rf radar ris vital-sign`
- Concise contribution: Integrates a liquid-crystal reconfigurable intelligent surface with a self-injection-locked radar, electronically steering the sensing path into an NLOS region and experimentally demonstrating contactless vital-sign monitoring.

### 3. Radar Sensing Using Dual-Beam Reconfigurable Intelligent Surface

- Authors: Kainat Yasmeen, Shobha Sundar Ram, Debidas Kundu
- Final venue: 2025 IEEE Radar Conference (RadarConf25), pp. 1254–1259
- DOI: `10.1109/RadarConf2559087.2025.11205052`
- arXiv: `2602.11473` is a later public preprint copy; the website/survey should label the final IEEE conference venue, not arXiv.
- Recommended category: `modality rf radar ris theory`
- Concise contribution: Studies practical one-bit RIS phase quantization for around-corner radar; the resulting symmetric dual beams redirect coverage away from purely specular wall geometry and are benchmarked against ideal RIS and a metal reflector.

### 4. mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera

- Authors: Byeonggyu Park, Hee-Yeun Kim, Byonghyok Choi, Hansang Cho, Byungkwan Kim, Soomok Lee, Mingu Jeon, Seong-Woo Kim
- Final venue: IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 2025, pp. 19661–19668
- DOI: `10.1109/IROS60139.2025.11246461`
- arXiv: `2508.02348`; use IROS 2025 as the venue.
- Recommended category: `modality rf mmwave localization robotics camera-fusion`
- Concise contribution: Uses camera-derived T-junction road layout to interpret multipath-distorted 2D mmWave point clouds and localize pedestrians hidden beyond the corner; validated on a real vehicle in outdoor NLOS driving scenes.

## Cross-artifact status

At the time of this pass:

- `README.md`: none of the four titles above is present.
- `index.html`: none of the four titles above is present.
- `bare_jrnl.tex`: no RIS vital-sign discussion is present and none of the four titles is integrated into survey prose.
- `egbib_merged_20260711.bib`: the new records are not yet merged.
- `egbib_20260811_ris_vitalsign_updates.bib`: contains all four final-venue records and should be treated as the canonical metadata source for this patch.
- `bare_jrnl.pdf`: therefore cannot yet be considered synchronized with this RF/RIS branch.

## Exact public insertion plan

### README.md

Add the four records to **Latest Additions** and to **New NLOS Scenes and Modalities → RF / radar / mmWave / RIS**. The vital-sign papers must be described as NLOS sensing, not geometric imaging. The Park et al. paper should sit next to the existing T-junction / automotive around-corner radar entries. Yasmeen et al. should sit with the existing RIS-assisted around-corner radar lineage.

Suggested timeline sentence for 2025:

> RF NLOS work also moved beyond passive exploitation of environmental multipath toward actively reconfigurable propagation: programmable and liquid-crystal RISs redirected radar energy into hidden regions for around-corner detection and physiological sensing, while camera-derived road geometry helped interpret multipath-distorted mmWave point clouds for hidden-pedestrian localization at real T-junctions.

### index.html

Add four paper objects to the existing `papers` array with the categories above, mark them `latest`, and extend the 2025 timeline paragraph with the same RF/RIS trajectory sentence. Do not promote the two vital-sign papers as hidden-scene reconstruction; classify them under RF/RIS semantic sensing.

### bare_jrnl.tex

Semantically appropriate insertion: the survey's emerging RF/mmWave/ISAC/RIS paragraph, adjacent to the existing discussion of RIS-assisted around-corner sensing and measured mmWave NLOS reconstruction. Suggested literature-review prose:

> A complementary RF branch treats the relay path as a controllable component rather than a fixed environmental reflector. Reconfigurable intelligent surfaces have been used to redirect radar illumination into otherwise inaccessible NLOS regions: practical dual-beam RIS designs quantify the impact of low-bit phase control on around-corner radar coverage, while liquid-crystal and programmable metasurfaces extend this idea to contactless hidden-region respiration and heartbeat sensing. In automotive settings, visual road-layout estimates can further condition the interpretation of multipath-distorted mmWave point clouds, enabling pedestrian localization around T-junctions without requiring the camera itself to observe the hidden target.

Cite the four keys already defined in `egbib_20260811_ris_vitalsign_updates.bib`:

- `liRISVitalSignNLOS2025`
- `tripathyLCRISVitalSign2025`
- `yasmeenDualBeamRIS2026` (key retained for compatibility although final venue year is 2025)
- `parkTjunctionPedestrian2025`

### Bibliography + PDF

Run `scripts/merge_nlos_bibliography.py` so these records enter `egbib_merged_20260711.bib`, then compile the IEEEtran survey with BibTeX and regenerate `bare_jrnl.pdf`. The public PDF should not be claimed updated until the merged bibliography and LaTeX prose both contain the four citations and the compiled PDF is rebuilt successfully.

## Citation-tracing / freshness result

A high-priority forward-citation-style web pass was repeated around LCT, f-k migration, computational periscopy, Neural Transient Fields, NLOST, consumer-LiDAR NLOS, HoloRadar, and 3D Gaussian Transient Rendering. It surfaced already-covered 2026 papers such as learned LCT, transient-video interpolation, stereo NLOS, physics-informed cascade learning, consumer-LiDAR NLOS, and 3D-GTR, but no additional clearly missing August-2026 imaging paper with final metadata. The four RF/RIS records above are therefore the only public-integration gap acted on in this run.

## Why this is a patch note rather than direct large-file overwrites

The GitHub connector available in this run can safely create small files and replace complete files, but it does not expose a line-level patch operation. `README.md`, `index.html`, `bare_jrnl.tex`, and the merged bibliography are large mutable files; overwriting them without reconstructing their complete current contents would risk truncating concurrent updates. This note records exact verified insertions instead of performing an unsafe blind replacement.
