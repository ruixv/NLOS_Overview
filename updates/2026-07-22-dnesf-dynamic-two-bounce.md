# D-NeSF dynamic two-bounce NLOS citation trace — 22 July 2026

## Verified missing paper

**D-NeSF: Dynamic Neural Shadow Fields for Two-bounce Non-line-of-sight Stereo Reconstruction**  
Jingyuan Zhang, Zijin Wang, Lianfa Bai, Jing Han, Xiaoyu Chen  
17th International Conference on Graphics and Image Processing (ICGIP 2025), Proceedings of SPIE, vol. 14124, article 1412415, 2026.  
DOI: `10.1117/12.3095236`

The paper is directly about two-bounce NLOS 3D reconstruction, not an incidental citation. It extends the static Neural Illumination Fields / shadow-carving trajectory to moving hidden targets. Its spatiotemporally disentangled representation decomposes the dynamic hidden volume into six feature planes; an MLP predicts time-varying density, and cyclic multi-position illumination plus a cumulative-transmittance constraint permits self-supervised fitting to shadow-image sequences.

## Repository comparison

Repository-wide title, DOI, and `D-NeSF` searches found no prior record in `README.md`, `index.html`, the survey sections, or the consolidated bibliography. The closely related static Neural Illumination Fields paper was already integrated in the README and `article/5newscenes.tex`, making the two-bounce subsection the appropriate semantic insertion point.

## Intended synchronized changes

- Add one formal latest-additions row and one 2026 timeline milestone to `README.md`.
- Add one searchable paper-explorer object, expand the 2026 timeline, and increment the tracked-entry count from 183 to 184 in `index.html`.
- Add a literature-review paragraph immediately after Neural Illumination Fields in `article/5newscenes.tex`, explaining the shift from static continuous fields to dynamic spatiotemporal shadow fields.
- Add citation key `zhangDynamicNeuralShadowFields2026` to the consolidated bibliography through `egbib_20260722_dnesf.bib`.
- Add a dated integration marker and synchronize the survey coverage date to 22 July 2026 in `bare_jrnl.tex`.
- Clean-build `bare_jrnl.pdf`, check citation resolution and duplicate bibliography entries, extract PDF text, and verify the new paragraph appears in the regenerated binary.

The guarded synchronizer refuses partial or duplicate integration and edits only unique structural anchors.
