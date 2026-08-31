# 2026-08-31 NLOS update: missing RF/mmWave and acoustic papers

## Verified missing papers

### 1. GeRaF: Neural Geometry Reconstruction from Radio Frequency Signals

**Jiachen Lu, Hailan Shanbhag, Haitham Al Hassanieh, “GeRaF: Neural Geometry Reconstruction from Radio Frequency Signals,” NeurIPS 2025 (Spotlight).**

- Final venue verified from the official NeurIPS proceedings and NeurIPS virtual site.
- Official paper: https://papers.nips.cc/paper_files/paper/2025/hash/8766fbc68e1ed1cdef712ce273e0a363-Abstract-Conference.html
- NeurIPS virtual page: https://nips.cc/virtual/2025/poster/115084
- Repository deduplication: exact-title and `GeRaF` searches returned no matches in `ruixv/NLOS_Overview`.

Why it belongs:

GeRaF is a direct RF/mmWave geometry-reconstruction paper. It introduces a neural implicit, physics-based RF volumetric renderer for near-range 3D geometry reconstruction, with filter-based rendering, lensless sampling, and lensless alpha blending to handle the full-space propagation and specular interactions of RF signals. It is an important bridge between conventional RF/SAR imaging and neural implicit reconstruction.

Suggested short summary:

> Introduces neural implicit 3D geometry reconstruction from RF measurements using a physics-based lensless volumetric rendering model, establishing a learned RF reconstruction baseline for occluded/penetrating sensing.

### 2. Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals

**Jiachen Lu, Hailan Shanbhag, Haitham Al Hassanieh, “Seeing through boxes: Non-Line-of-Sight 3D Reconstruction from Radar Signals,” CVPR 2026, pp. 1221–1230.**

- Final venue verified from the official CVPR 2026 Open Access proceedings.
- Official paper page: https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Seeing_through_boxes_Non-Line-of-Sight_3D_Reconstruction_from_Radar_Signals_CVPR_2026_paper.html
- arXiv: https://arxiv.org/abs/2605.29098
- The arXiv record explicitly lists CVPR 2026; use CVPR 2026 as the venue.
- Repository deduplication: exact-title, arXiv-ID, and `GeRaF` searches returned no matches.

Why it belongs:

This is a direct NLOS 3D reconstruction paper, not generic radar sensing. The paper extends GeRaF to a unified LoS/NLoS neural SDF framework (GeRaF 2.0) for reconstructing both an enclosing opaque box and objects hidden inside it from RF measurements. Visual LoS geometry provides a physical prior that stabilizes RF propagation modeling and resolves SDF surface ambiguity in the hidden region.

Suggested short summary:

> GeRaF 2.0 reconstructs hidden 3D geometry from radar by jointly modeling visible and NLOS regions, using visual LoS SDF priors to stabilize physically grounded RF neural rendering inside opaque enclosures.

Suggested trajectory sentence:

> RF-based NLOS has progressed from radar/SAR localization and coarse imaging toward learned implicit geometry: GeRaF introduced physics-based neural RF rendering, while GeRaF 2.0 demonstrated CVPR-level 3D reconstruction of objects hidden inside opaque containers by coupling visible-scene geometry with NLOS RF propagation.

### 3. Passive acoustic non-line-of-sight localization without a relay surface

**Tal I. Sommer and Ori Katz, “Passive acoustic non-line-of-sight localization without a relay surface,” Physical Review Applied 25(2), 024064 (2026), DOI 10.1103/p97k-sf71.**

- Published 20 February 2026.
- Final venue verified from APS / Physical Review Applied.
- DOI: https://doi.org/10.1103/p97k-sf71
- arXiv: https://arxiv.org/abs/2506.08471
- Repository deduplication: exact-title and DOI searches returned no matches.

Why it belongs:

This is a tightly adjacent NLOS sensing/localization paper with an unusual propagation model: it does not require a diffuse relay wall. Instead, it exploits knife-edge acoustic diffraction for 3D localization of a hidden passive point source. In a doorway setting, the two door edges act as virtual detector arrays; around a convex corner, the method uses the frequency-dependent knife-edge diffraction signature. This extends NLOS sensing beyond reflection-based relay-surface paradigms.

Suggested short summary:

> Demonstrates passive 3D NLOS acoustic source localization without a relay surface by exploiting knife-edge diffraction at doorway/corner boundaries, broadening NLOS sensing beyond reflection-mediated architectures.

## Citation-tracing / Core-paper pass

The high-priority search pass included the repository’s active-NLOS milestones (LCT, f-k migration, phasor fields), passive computational periscopy, learned transient reconstruction families, and modality-expansion work. Searches around recent forward citations and citation neighborhoods primarily returned papers already present in the repository/update lineage, including Learned LCT, TLTM iteration, consumer-LiDAR NLOS, 3D Gaussian Transient Rendering, thermal rough-surface NLOS, MARMOT, and recent GPU/SPAD work. No additional high-confidence missing optical transient paper was added in this run.

The three papers above were retained because they are genuine NLOS imaging/sensing contributions rather than papers that merely cite NLOS work in passing. The two GeRaF papers are especially important omissions because they form a coherent RF/mmWave neural-reconstruction lineage and the 2026 paper has a verified CVPR final venue.

## Integration locations

### README.md

1. **Latest Additions**
   - Add GeRaF 2.0 / CVPR 2026 under RF/mmWave / learned reconstruction.
   - Add Sommer & Katz / PRApplied 2026 under acoustic NLOS.
   - Add GeRaF / NeurIPS 2025 in the historical RF/mmWave learned-reconstruction section; it need not dominate the latest-additions block if that block is intentionally recent-only.

2. **Development timeline**
   - 2025: GeRaF — neural implicit RF geometry reconstruction (NeurIPS Spotlight).
   - 2026: GeRaF 2.0 — LoS-guided NLOS 3D reconstruction from radar through opaque enclosures (CVPR).
   - 2026: Sommer & Katz — relay-free passive acoustic NLOS localization from knife-edge diffraction (Physical Review Applied).

3. **Modality sections**
   - Place both GeRaF papers under RF / radar / mmWave NLOS, near HoloRadar and other RF imaging works.
   - Place Sommer & Katz under acoustic/ultrasound NLOS, distinguishing reflection-mediated methods from diffraction-mediated localization.

### Website / Paper Explorer

Add the three papers to the canonical paper corpus used by the site (e.g. `data/papers-source.html`, if still canonical), with tags such as:

- GeRaF: `RF`, `mmWave`, `radar`, `neural implicit`, `3D reconstruction`, `physics-based rendering`, `NeurIPS 2025`, `Spotlight`.
- GeRaF 2.0: `RF`, `mmWave`, `radar`, `NLOS`, `3D reconstruction`, `neural SDF`, `CVPR 2026`, `LoS prior`.
- Sommer & Katz: `acoustic`, `passive NLOS`, `localization`, `diffraction`, `knife-edge`, `relay-free`, `Physical Review Applied 2026`.

### bare_jrnl.tex / article sections

Insert semantically rather than appending a detached list:

- In the emerging RF/mmWave NLOS section, add a paragraph explaining the shift from classical radar/SAR imaging toward neural implicit RF rendering. Cite GeRaF first, then GeRaF 2.0 as the explicit NLOS extension using visible-geometry priors.
- In the acoustic/ultrasound section, add Sommer & Katz after reflection-based around-corner localization/imaging, emphasizing that diffraction at obstacle edges can replace a conventional diffuse relay surface.

Suggested survey prose:

> Beyond optical transport, RF-based NLOS reconstruction is beginning to adopt implicit-scene representations. GeRaF formulates near-range RF geometry recovery as physics-based neural volumetric rendering with lensless sampling, while its successor GeRaF 2.0 couples visible-region geometry with radar measurements to stabilize reconstruction of surfaces hidden inside opaque enclosures. These works move RF NLOS from coarse occupancy/localization toward continuous learned 3D geometry.

> Acoustic NLOS need not rely exclusively on wall reflections. Sommer and Katz exploit the frequency-dependent diffraction of sound around doorway and corner edges to localize passive hidden sources in 3D, demonstrating a relay-free NLOS sensing regime based on knife-edge propagation rather than diffuse reflection.

### Bibliography

Merge the verified entries staged in `egbib_20260831_rf_acoustic_missing_gap.bib` into the canonical bibliography (`egbib.bib` or whichever file is actually cited by `bare_jrnl.tex`).

## PDF / consistency status

The current repository contains a large `README.md` (~179 KB), `egbib.bib` (~276 KB), and a binary `bare_jrnl.pdf`. The available GitHub write action replaces whole text files, while large fetches are returned in truncated payloads. Reconstructing and overwriting README/website/bibliography from partial content would risk truncation or data loss. Therefore this run intentionally does **not** claim that README, website, `bare_jrnl.tex`, canonical `egbib.bib`, or `bare_jrnl.pdf` have been fully synchronized.

Before rebuilding the PDF, integrate these staged entries into README, website corpus, the RF/acoustic survey paragraphs, and canonical bibliography, then run the normal LaTeX build and verify that all three papers resolve in the rebuilt `bare_jrnl.pdf`. The staged BibTeX and this note provide exact metadata and insertion guidance without risking destructive whole-file replacement.
