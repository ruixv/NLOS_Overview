# 20 July 2026 — scan-free, event-camera, and polarization-speckle NLOS synchronization

## Status

**SAFE SOURCE UPDATE STAGED; PUBLIC ARTIFACT MERGE AND PDF REBUILD NOT YET CLAIMED.**

This pass verified three cross-artifact gaps and committed canonical metadata plus a guarded synchronizer. At the time of this note, `README.md`, `index.html`, the survey section files, the consolidated bibliography, and `bare_jrnl.pdf` have not yet received the generated integration commit. Do not claim that the public pages or PDF include these changes until repository history shows the synchronizer's final commit and the artifacts have been rechecked.

## Records to integrate

### Real-time scan-free non-line-of-sight imaging

- Authors: Wenjun Zhang et al.
- Venue: APL Photonics 9(12), 126101 (2024)
- DOI: `10.1063/5.0235687`
- Role in the timeline: parallel SPAD-array transient capture removes relay-wall raster scanning; reported 151-fps acquisition and 19-fps end-to-end reconstruction, with a super-resolution module reducing the nominal array requirement from 32×32 to 8×8.
- Canonical key: `zhangRealTimeScanFreeNLOS2024`

### High-resolution and real-time non-line-of-sight imaging based on spatial correlation

- Authors: Wenjun Zhang et al.
- Venue: Optics and Lasers in Engineering 193, 109100 (2025)
- DOI: `10.1016/j.optlaseng.2025.109100`
- Role in the timeline: extends scan-free acquisition with a 3D blur-kernel model and spatial-correlation resampling; reports approximately 2-cm lateral resolution and 5-fps dynamic reconstruction from a 16×16 detector.
- Canonical key: `zhangSpatialCorrelationNLOS2025`

### Event-Enhanced Passive Non-Line-of-Sight Imaging for Moving Objects With Physical Embedding

- Authors: Conghe Wang, Xia Wang, Yujie Fang, Changda Yan, Xin Zhang, Yifan Zuo
- Final venue: IEEE Sensors Journal 24(22), 37970–37985 (2024)
- DOI: `10.1109/JSEN.2024.3468909`
- Required correction: replace the repository's arXiv-only `2404.05977` record rather than creating a duplicate.
- Role in the timeline: event-camera measurements emphasize asynchronous motion-induced changes in relay-wall diffusion patterns; physics-based simulation pretraining and limited real-data fine-tuning support moving hidden-object reconstruction.
- Canonical key: `wangEventEnhancedPassiveNLOS2024`

### Non-Line-of-Sight Single-Pixel Imaging Using Polarization Speckle Modulation

- Authors: Yijun Zhou, Wenwen Li, Wei Li, Xin Huang, Chen Dai, Zhong-Pei Xiao, Zheng-Ping Li, Feihu Xu, Jian-Wei Pan
- Venue: Physical Review Letters 136(14), 143801 (2026)
- DOI: `10.1103/kd8v-fykm`
- Role in the timeline: polarization-controlled relay-wall speckles provide diverse illumination codes for scanning-free single-pixel keyhole NLOS imaging; angular-memory-effect calibration avoids direct access to the hidden scene.
- Canonical key: `zhouPolarizationSpeckleNLOS2026`
- Existing partial coverage: the active-method table and README timeline already mention this work, but the README latest-additions table, website paper explorer, dedicated survey prose, and consolidated BibTeX need explicit consistency checks.

## Intended insertion points

1. `README.md`
   - Advance the update-run date to 20 July 2026.
   - Add formal latest-additions rows for both scan-free papers and the PRL polarization-speckle paper.
   - Replace the event-camera arXiv row with the IEEE Sensors Journal final record.
   - Add 2024 scan-free/event-camera and 2025 spatial-correlation timeline milestones.

2. `index.html`
   - Replace the event-camera preprint object with the final IEEE Sensors Journal object.
   - Add searchable records for the two scan-free papers and the PRL paper.
   - Add corresponding 2024–2026 timeline sentences and recompute the tracked-entry count from the paper array.

3. `article/2active.tex`
   - Extend the pulsed-laser/SPAD-array table row with `zhangRealTimeScanFreeNLOS2024` and `zhangSpatialCorrelationNLOS2025`.
   - Add a hardware-section paragraph explaining the trajectory from parallel scan-free capture to spatial-correlation super-resolution.
   - Add a wave/transport-adjacent paragraph distinguishing polarization-speckle illumination coding from time-gated polarimetric observability.

4. `article/3passive.tex`
   - Add the final event-camera record to the passive-method table.
   - Add a semantically placed paragraph on neuromorphic passive NLOS for moving objects.

5. `bare_jrnl.tex` and bibliography
   - Advance the coverage date to 20 July 2026.
   - Merge the three existing canonical supplements and `egbib_20260720_polarization_single_pixel.bib` into `egbib_merged_20260711.bib`, replacing any duplicate/preprint event-camera entry.

6. `bare_jrnl.pdf`
   - Clean-build after source integration.
   - Reject the build if citations are undefined or rendered text omits the new scan-free, event-camera, or polarization-speckle discussion.
   - Leave the current binary unchanged when a validated replacement cannot be produced.

## Committed implementation

- `egbib_20260719_scanfree_spatial_correlation.bib`
- `egbib_20260720_event_camera_final_venue.bib`
- `egbib_20260720_polarization_single_pixel.bib`
- `scripts/sync_nlos_20260720_final.py`

The synchronizer uses unique anchors, removes the obsolete event-camera preprint metadata, deduplicates canonical BibTeX keys/DOIs, validates cross-artifact DOI coverage, and checks that the website count equals the number of paper objects.
