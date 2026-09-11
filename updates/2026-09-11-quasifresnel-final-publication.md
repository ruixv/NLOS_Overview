# Quasi-Fresnel NLOS final-publication metadata sync — 11 September 2026

## Verified publication

Yijun Wei, Jianyu Wang, Leping Xiao, Zuoqiang Shi, Xing Fu, and Lingyun Qiu, **“Fast and Memory-Efficient Non-Line-of-Sight Imaging with Quasi-Fresnel Transform,”** *Optica* **13**(9), 1785–1795 (2026), DOI: 10.1364/OPTICA.604217.

Optica’s September 2026 issue page now lists the paper as the final published article. The repository currently still labels the README entry as “Optica 2026 (accepted)” and the canonical bibliography entry `weiQuasiFresnel2026` still contains the note “Accepted for publication; also available as arXiv:2508.02003”.

## Required consistency edits

1. **README.md**
   - Locate the entry `Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform`.
   - Replace venue/status `Optica 2026 (accepted)` with `Optica 13(9), 1785–1795 (2026)`.
   - Keep DOI `10.1364/OPTICA.604217`; arXiv:2508.02003 may remain only as an auxiliary preprint link/source.

2. **Website / paper explorer / timeline**
   - Replace any `accepted` / arXiv-first venue label for this paper with the final Optica citation above.
   - Preserve the contribution summary: the method collapses common hidden surfaces and aggregated measurements to 2D functions and derives a direct Quasi-Fresnel inverse with substantially reduced runtime and memory.

3. **Canonical bibliography: `egbib_merged_20260711.bib`**
   - Replace the current `weiQuasiFresnel2026` record with the verified final metadata below (also staged in `egbib_20260911_quasifresnel_final.bib`):

```bibtex
@article{weiQuasiFresnel2026,
  author = {Wei, Yijun and Wang, Jianyu and Xiao, Leping and Shi, Zuoqiang and Fu, Xing and Qiu, Lingyun},
  title = {Fast and Memory-Efficient Non-Line-of-Sight Imaging with Quasi-Fresnel Transform},
  journal = {Optica},
  volume = {13},
  number = {9},
  pages = {1785--1795},
  year = {2026},
  doi = {10.1364/OPTICA.604217},
  url = {https://doi.org/10.1364/OPTICA.604217},
  note = {Final published version; September 2026. Preprint also available as arXiv:2508.02003}
}
```

4. **Survey prose / LaTeX**
   - No new literature-review paragraph is required if the paper is already discussed and cited as `weiQuasiFresnel2026`; the existing citation key can be retained.
   - Remove wording that calls the work only accepted or arXiv-only if such wording occurs in survey prose.

5. **PDF**
   - After canonical bibliography and any stale prose/venue labels are synchronized, rebuild `bare_jrnl.pdf` and verify the bibliography renders `Optica 13(9), 1785–1795 (2026)`.

## Why this note exists

The current GitHub connector can safely create small verified files, but the large README, website, and merged bibliography require whole-file replacement while the connector read response is truncated. Per repository-update safety rules, do not overwrite those large files from incomplete content. This note records exact insertion/replacement targets until a full-file-safe update path is available.
