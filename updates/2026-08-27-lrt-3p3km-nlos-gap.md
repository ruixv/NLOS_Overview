# 2026-08-27 — 3.3-km scanning-free laser reflective tomography NLOS gap

## Verified missing paper

**Zewei Wang, Xiaoyin Li, Yinghui Guo, Hengshuo Guo, Peng Yang, Fei Zhang, Mingbo Pu, Mingfeng Xu, Xiangang Luo, “Breaking the speed-resolution trade-off in 3.3-km non-line-of-sight imaging using scanning-free laser reflective tomography,” Opto-Electronic Science 5(6), 260007 (2026), DOI: 10.29026/oes.2026.260007.**

The paper is genuinely NLOS imaging rather than merely adjacent long-range tomography. It adapts laser reflective tomography (LRT) to third-bounce NLOS capture, uses the diffuse relay surface as a natural beam expander, avoids dense relay-wall scanning, and reconstructs hidden targets from single-point detection plus multi-angle target projections. The paper reports roughly 2× better spatial resolution and 91× faster acquisition than the compared scanning-based configuration indoors, and demonstrates 3.3-km outdoor NLOS imaging with better than 3-cm spatial resolution in about 3 minutes.

Repository search on 2026-08-27 found no match for the exact title, DOI `10.29026/oes.2026.260007`, or `laser reflective tomography`, so this is a real corpus gap rather than a venue/title duplicate.

## Recommended placement

### README.md

Add to **Latest Additions**:

```markdown
| 2026 | [Breaking the speed-resolution trade-off in 3.3-km non-line-of-sight imaging using scanning-free laser reflective tomography](https://doi.org/10.29026/oes.2026.260007) — Wang et al. | Opto-Electronic Science 5(6), 260007 (2026) | Adapts laser reflective tomography to scanning-free active NLOS imaging by using the diffuse relay wall as a natural beam expander and single-point third-bounce detection; reports ~2× higher spatial resolution, ~91× faster acquisition, and a 3.3-km outdoor demonstration with <3-cm resolution in ~3 min. |
```

Add a 2026 milestone/timeline sentence placing it after scan-free SPAD-array and long-range active NLOS developments, emphasizing the shift from relay-wall raster scanning to projection/tomography-driven stand-off imaging.

### Website / V2 canonical paper corpus

The V2 site should add a paper object in `data/papers-source.html` (rather than duplicating the paper array inside `index.html`) with:

- title: `Breaking the speed-resolution trade-off in 3.3-km non-line-of-sight imaging using scanning-free laser reflective tomography`
- year: `2026`
- venue: `Opto-Electronic Science 5(6), 260007`
- family: `active`
- DOI URL: `https://doi.org/10.29026/oes.2026.260007`
- citation key: `wangLRTNLOS2026`
- contribution: scanning-free laser reflective tomography; diffuse relay wall as natural beam expander; single-point third-bounce detection; 3.3-km stand-off NLOS imaging, <3-cm resolution, ~3-min acquisition.

Add a 2026 timeline milestone such as:

> **Scanning-free laser reflective tomography reaches kilometer-scale NLOS.** LRT replaces dense relay-wall raster scanning with diffuse-wall beam expansion and projection-domain tomography, demonstrating 3.3-km stand-off reconstruction with centimeter-scale resolution.

Recompute the displayed tracked-entry count from the actual corpus rather than editing the count by hand.

### LaTeX survey

Integrate semantically in `article/2active.tex`, near the discussion of scan-free acquisition, long-range active NLOS, and practical acquisition architectures. Do not append it only as a list item.

Suggested literature-review sentence:

```latex
More recently, Wang \textit{et al.}~\cite{wangLRTNLOS2026} introduced scanning-free laser reflective tomography for active NLOS imaging, using the diffuse relay surface as a natural beam expander and recovering hidden scenes from single-point third-bounce measurements combined with projection-domain tomography. Beyond removing dense relay-wall raster scanning, the system demonstrated kilometer-scale stand-off operation, including a 3.3-km experiment with centimeter-scale spatial resolution, highlighting a distinct route toward long-range NLOS imaging that trades spatial wall scanning for tomographic angular diversity.
```

If the active-method comparison table has a suitable row for scan-free / long-range systems, add this paper there as well.

### Bibliography

Merge `egbib_20260827_lrt_3p3km_gap.bib` into the canonical bibliography used by `bare_jrnl.tex` using the key `wangLRTNLOS2026`. Ensure there is exactly one instance of the key and DOI.

### bare_jrnl.tex / PDF

After source integration, update the living-survey date only if the repository convention is to stamp each public integration run. Then rebuild cleanly:

```bash
pdflatex bare_jrnl.tex
bibtex bare_jrnl
pdflatex bare_jrnl.tex
pdflatex bare_jrnl.tex
```

Validation requirements before claiming completion:

1. `wangLRTNLOS2026` resolves in `.aux` / `.bbl` with no undefined citation.
2. DOI `10.29026/oes.2026.260007` appears exactly once in the canonical bibliography.
3. README, V2 corpus, timeline, survey prose, BibTeX, and PDF all contain the paper consistently.
4. `pdftotext bare_jrnl.pdf -` contains distinctive tokens such as `laser reflective tomography` and `3.3-km` (allowing normal PDF hyphenation differences).
5. Render at least the first page and the page containing the new citation/prose to confirm the PDF is visually valid.
6. Commit `bare_jrnl.pdf` only after the clean build and checks succeed; otherwise leave the public PDF unchanged and record the remaining blocker explicitly.

## Why this belongs in the development trajectory

This work represents a different system-level branch from conventional confocal/non-confocal ToF NLOS solvers such as LCT, f-k migration, and phasor-field propagation. Those methods generally assume transient measurements sampled over a relay region and focus on inversion efficiency/accuracy; the LRT work changes the acquisition geometry itself, replacing dense spatial scanning with a tomography-style projection acquisition and extending NLOS imaging to kilometer-scale stand-off distances. It is therefore best framed as an acquisition/long-range milestone, not as a replacement for the core transient inverse models.
