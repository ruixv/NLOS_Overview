# NLOS literature gap scan — 2026-10-03

This note records four metadata-verified papers found missing from the repository default branch during the current broad/citation-oriented scan. Large canonical files were not overwritten from partial reads. The entries are staged in `egbib_20261003_multi_gap.bib` for safe later integration into `egbib.bib` and `bare_jrnl.tex`.

## 1. Stereo non-line-of-sight imaging

Pablo Luesia-Lahoz, Sergio Cartiel, Adolfo Muñoz. *The Visual Computer* 42, article 148 (2026). DOI: 10.1007/s00371-025-04340-7. Published 29 Jan 2026.

**Why it belongs:** active transient/phaser-field NLOS; two relay walls act as generalized virtual camera apertures. Cross-wall measurements reduce the missing-cone ambiguity and provide surface-orientation cues. This is a useful conceptual bridge from single-relay phasor-field imaging to multi-aperture/stereo NLOS.

**Canonical placement:** README/website 2026 active/transient timeline; Paper Explorer tags `active`, `ToF`, `phasor field`, `multi-relay`, `missing cone`; survey near the phasor-field/missing-cone discussion.

Suggested survey sentence: `Multi-relay acquisition has also been used to address visibility limitations: Stereo NLOS treats two relay walls as generalized virtual apertures and combines intra- and cross-wall transport to reduce the missing cone while exposing surface-orientation cues.`

## 2. MDUNet: Multimodal Decoding UNet for Passive Occluder-Aided Non-line-of-sight 3D Imaging

Fadlullah Raji, John Murray-Bruce. WACV 2026, pp. 461–471. DOI: 10.1109/WACV61042.2026.00053.

**Why it belongs:** directly extends passive occluder-aided NLOS reconstruction. A shared encoder with coupled 2D radiosity and 3D occluder/SDF decoding replaces much slower diffusion/iterative inference; the paper reports >100x acceleration over a diffusion baseline and >1000x over iterative optimization, with simulation-to-real transfer.

**Canonical placement:** passive NLOS / occluder-aided imaging section after recent joint hidden-scene/occluder reconstruction work; website tags `passive`, `occluder-aided`, `3D`, `learning`, `WACV 2026`.

Suggested survey sentence: `Recent passive methods increasingly learn coupled hidden-scene representations: MDUNet jointly decodes hidden radiosity and occluder geometry from a shared latent representation, substantially reducing inference cost while retaining simulation-to-real generalization.`

## 3. Non-confocal non-line-of-sight imaging using frequency-domain phase compensation with the reference function

Jing Ping Yu, Xiao Rui Tian, Jie Yang, Zhou Yang, Ming Ze Yang, Si Qi Zhang, Meng Tang, Chen Fei Jin. *Optics Express* 34(2), 3232–3243 (2026). DOI: 10.1364/OE.580027.

**Why it belongs:** a genuine non-confocal optical NLOS reconstruction paper. It transfers a SISO/SIMO-style frequency-domain phase-compensation formulation from mmWave imaging and uses a reference function plus FFT reconstruction to reduce artifacts, distortion, and computational cost.

**Canonical placement:** active NLOS section alongside non-confocal/frequency-domain reconstruction; timeline as a 2026 analytical/frequency-domain method. Note that bibliographic services disagree on online-first date (late 2025 vs issue publication in Jan 2026); use the final journal issue year 2026.

Suggested survey sentence: `For non-confocal acquisition, frequency-domain phase compensation with a reference function adapts a radar-style imaging formulation to optical NLOS, enabling FFT-based reconstruction with reduced artifacts and computational burden.`

## 4. Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging

Kun Chen, Shunjun Wei, Mou Wang, Juran Chen, Bingyu Han, Jin Li, Zhe Liu, Xiaoling Zhang, Yi Liao, Pengcheng Gao, Xiaolin Mi. *Photonics* 13(5), 440 (2026). DOI: 10.3390/photonics13050440. Published 30 Apr 2026.

**Why it belongs:** directly expands the repository's RF/mmWave modality branch toward THz radar. It uses a physics-guided deep-unfolding reconstruction for around-corner 3D THz radar imaging, making it relevant to the modality-expansion trajectory rather than generic NLOS communications.

**Canonical placement:** RF/mmWave/THz NLOS section after radar/mmWave milestones such as HoloRadar; website tags `THz`, `radar`, `around-corner`, `3D`, `deep unfolding`.

Suggested survey sentence: `The RF branch is also extending upward in carrier frequency: recent THz-radar work embeds an iterative physical reconstruction into a deep-unfolding architecture for around-corner 3D imaging, connecting model-based radar inversion with learned NLOS reconstruction.`

## Verification and exclusions

Each title was searched against the repository default branch before staging and returned no match. Final venues were preferred over preprints: The Visual Computer, WACV 2026, Optics Express, and Photonics, respectively. Broader search also surfaced RIS-assisted radar sensing, dual-spectral edge NLOS, and THz NLOS communications; these were not staged here because they are either more peripheral to imaging/reconstruction or need stronger evidence of fit before inclusion.

## Required canonical follow-up

1. Merge the four staged BibTeX entries into `egbib.bib`, checking citation-key collisions.
2. Add the papers to the appropriate README development timeline/categories with concise contribution summaries.
3. Add/update website Paper Explorer, latest additions, and timeline entries.
4. Integrate the suggested literature-review transitions into the semantically appropriate active/passive/RF sections of the modular survey source and/or `bare_jrnl.tex` without merely appending a list.
5. Compile `bare_jrnl.tex` and regenerate `bare_jrnl.pdf`; only then mark the canonical artifacts mutually consistent.

The current run intentionally does **not** claim that `README.md`, `index.html`, `bare_jrnl.tex`, `egbib.bib`, or `bare_jrnl.pdf` have already been synchronized; overwriting these large canonical files from partial connector reads would risk truncation or data loss.
