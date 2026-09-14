# 2026-09-14 NLOS update: non-confocal optical reconstruction and around-corner FMCW radar

This run found two high-confidence papers that are absent from the repository's indexed README/code search and are directly relevant to NLOS imaging/sensing.

## 1. Jing Ping Yu et al., Optics Express 2026

**Non-confocal non-line-of-sight imaging using frequency-domain phase compensation with the reference function**  
Jing Ping Yu, Xiao Rui Tian, Jie Yang, Zhou Yang, Ming Ze Yang, Si Qi Zhang, Meng Tang, Chen Fei Jin.  
*Optics Express* 34(2), 3232--3243 (2026). DOI: 10.1364/OE.580027.

### Contribution
Transfers a single-input-multiple-output frequency-domain imaging formulation from millimeter-wave imaging to non-confocal optical NLOS. A reference-function phase-compensation formulation enables high-resolution reconstruction with reduced artifacts/shape distortion and FFT-based computational efficiency.

### Recommended integration
- **README.md**: Active NLOS Imaging -> Reconstruction Algorithms; also list in Latest Additions.
- **Timeline**: 2026, under practical/non-confocal frequency-domain reconstruction.
- **Survey source**: `article/2active.tex`, close to non-confocal reconstruction and frequency-domain/f-k style methods. Suggested literature-review sentence: "Recent work has further transferred frequency-domain phase-compensation ideas from array imaging to non-confocal optical NLOS, using a reference function to correct path-dependent phase while retaining FFT-based efficiency \cite{yu2026nonconfocal}."
- **Website/index.html**: add to Paper Explorer as Active / Optical / Non-confocal / Frequency-domain reconstruction.
- **Canonical bibliography**: merge `yu2026nonconfocal` from `egbib_20260914_nonconfocal_radar_gaps.bib`.

## 2. Shih-Lin Lin and Yi-Hsuan Chen, CMES 2026

**Deep Learning--Aided Frequency-Modulated Continuous-Wave Radar for Around-the-Corner Non-Line-of-Sight Perception at Urban Intersections**  
Shih-Lin Lin, Yi-Hsuan Chen.  
*Computer Modeling in Engineering & Sciences* 147(1), 37 (2026). DOI: 10.32604/cmes.2026.078862. Issue published 27 April 2026.

### Contribution
Uses building specular reflections with 77-GHz FMCW automotive radar for around-corner NLOS perception at urban intersections. A compact AlexNet-derived 1-D regression model with residual learning and batch normalization restores interference-corrupted chirps before conventional range/angle estimation. Evaluation is simulation-only, so the survey should label it as a simulation study rather than implying measured-road validation.

### Recommended integration
- **README.md**: New NLOS Scenes and Modalities -> RF/mmWave/radar; concise note should explicitly say "simulation study".
- **Timeline**: 2026, after moving-target/self-supervised mmWave NLOS work, as a deep-learning interference-mitigation branch for automotive around-corner sensing.
- **Survey source**: `article/5newscenes.tex`, near radar/RF/mmWave NLOS. Suggested sentence: "A complementary automotive branch uses simulated 77-GHz FMCW specular multipath at urban intersections, with learned chirp-domain interference restoration preceding conventional range/angle estimation \cite{lin2026deeplearningradarnlos}; real-world validation remains future work."
- **Website/index.html**: add to Paper Explorer as Radar / Automotive / Around-corner / Learned signal restoration, marked simulation-only.
- **Canonical bibliography**: merge `lin2026deeplearningradarnlos` from `egbib_20260914_nonconfocal_radar_gaps.bib`.

## Consistency/build checklist

1. Merge both BibTeX entries into the canonical bibliography used by `bare_jrnl.tex`.
2. Integrate the survey sentences into the semantic sections above rather than appending a detached recent-work list.
3. Add matching README and website entries with the same venue/year/title and no arXiv-only venue labels.
4. Recompile `bare_jrnl.pdf` after source/bibliography integration.
5. Verify README, website/Paper Explorer, modular LaTeX/bare_jrnl.tex, bibliography, and regenerated PDF all contain the same two entries.

Large public-facing files were intentionally not overwritten from partial/truncated connector payloads in this run.