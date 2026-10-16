# NLOS citation-tracing findings — 2026-10-17

Verified against the existing README, website Paper Explorer, and bibliography on the staging branch.

## Missing references

- Shi, Yingjie; Liu, Lingfeng; Li, Tongyao; Qin, Taotao; Wu, Chenyang; Bai, Lianfa; Guo, Enlai; Han, Jing. "Transient non-line-of-sight temporal super-resolution based on temporal decoupling." *Optics and Lasers in Engineering* (2026), article 110054. DOI: 10.1016/j.optlaseng.2026.110054. OpenAlex W7196975428 confirms authors, title, journal, DOI. Full abstract unavailable, so no unverified performance claims.
- Murray-Bruce, John; Saunders, Charles; Goyal, Vivek K. "Occlusion-based computational periscopy with consumer cameras." *Proceedings of SPIE*, vol. 11138, article 111380X (2019). DOI: 10.1117/12.2528322. Verified with Boston University repository and later TERI citations.
- Czajkowski, Robinson; Murray-Bruce, John. "Turning Door Frames into Cameras for 3D Non-line-of-sight Imaging." *IEEE RAPID 2022*, pp. 1–2. DOI: 10.1109/RAPID54472.2022.9911582. Verified via lab publication list and conference program. Two-page precursor, not the 2024 Nature Communications article.

These works are distinct from existing catalog entries. Their BibTeX records are in `updates/2026-10-17-verified-bibtex-staging.bib`.

## Correction

Legacy bibliography key `czajkowskiTwoEdge2024` has wrong author (Robert), DOI 10.1038/s41467-024-48747-3, and article 4376. Correct: Robinson Czajkowski; DOI 10.1038/s41467-024-45397-7; *Nature Communications* 15, article 1162 (2024). Keep the alias key.

## Integration map

README Latest Additions / Milestone Timeline; `data/papers-source.html` explorer and timeline; `index.html` passive/active reading paths; `article/3passive.tex` edge/occluder periscopy (two historical papers); `article/2active.tex` temporal super-resolution alongside Tian et al.; merged BibTeX. `bare_jrnl.tex` includes these chapter sources. Verify all citation keys and DOI references. Rebuild `bare_jrnl.pdf` only with the complete LaTeX source and image assets.

OpenAlex citing-work pages 1–9 for Saunders et al. Nature 2019 (W2913322182) were reviewed, covering 215 indexed citing works. Many candidates were already covered or irrelevant. Other Core seed networks were not exhaustively reviewed.

## Release status

Changes are staged in `nlos-2026-10-17-temporal-decoupling-staging`; public master merge and survey PDF rebuild are pending. No PDF regeneration is claimed. Do not replace large source files from partial content.
