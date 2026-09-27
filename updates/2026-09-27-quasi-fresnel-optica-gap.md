# Integration gap: Quasi-Fresnel NLOS (Optica 2026)

Verified missing paper on 2026-09-27:

Yijun Wei, Jianyu Wang, Leping Xiao, Zuoqiang Shi, Xing Fu, and Lingyun Qiu, **Fast and Memory-efficient Non-line-of-sight Imaging with Quasi-Fresnel Transform**, *Optica*, vol. 13, p. 1785, 2026. DOI: 10.1364/OPTICA.604217. Earlier preprint: arXiv:2508.02003.

## Why it belongs

This is a direct analytic-inversion descendant of the active transient NLOS line (including LCT/f-k style volumetric inversion), but explicitly exploits the approximately 2D nature of hidden surfaces. The Quasi-Fresnel transform maps aggregated transient measurements directly to a 2D hidden-scene representation, reducing the stated computational complexity to O(N^2 log N) and memory to O(N^2). The published/author metadata reports sub-second high-resolution reconstruction and <50 MB memory in representative experiments, making it an important efficiency/deployment milestone rather than another generic learned reconstruction method.

## Verified metadata

- Final venue: Optica 13, 1785 (2026), not arXiv.
- DOI: 10.1364/OPTICA.604217.
- Authors: Yijun Wei; Jianyu Wang; Leping Xiao; Zuoqiang Shi; Xing Fu; Lingyun Qiu.
- Author/lab publication page confirms the Optica venue, volume, page and DOI.

## Required canonical integration

1. **README.md**: add to the 2026 active/transient reconstruction timeline. Suggested summary: “Introduces a Quasi-Fresnel transform that exploits 2D hidden-surface structure to replace volumetric inversion with a direct 2D formulation, substantially reducing runtime and memory for high-resolution NLOS reconstruction.”
2. **index.html / Paper Explorer / Latest additions**: add under Active / Transient / Analytic reconstruction / Efficient reconstruction; expose DOI and final Optica venue.
3. **bare_jrnl.tex**: integrate semantically in the analytic reconstruction / computational-efficiency discussion after LCT/f-k/related fast-transform methods. Useful trajectory sentence: recent work revisits analytic inversion itself rather than only accelerating 3D operators, with the Quasi-Fresnel formulation exploiting surface dimensionality to reduce the transient inverse problem to a 2D transform suitable for lightweight deployment.
4. **Canonical bibliography**: merge the verified entry staged in `egbib_20260927_quasi_fresnel_optica.bib`, avoiding duplicate keys/entries.
5. **bare_jrnl.pdf**: rebuild only after the canonical TeX and bibliography are safely updated; verify the new citation resolves and PDF is consistent with README/site.

Large canonical files were not overwritten from partial/truncated payloads in this run.
