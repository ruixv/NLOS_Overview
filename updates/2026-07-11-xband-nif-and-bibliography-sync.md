# 11 July 2026 X-band radar, neural two-bounce, and bibliography sync

Fresh keyword search and forward-citation tracing from core optical NLOS, phasor-field, and two-bounce papers identified two verified missing works that are directly about NLOS imaging rather than incidental citations:

- **X-band Radar Non-Line-of-Sight Imaging** — Du et al., CVPR 2026. A neural, geometry-aware X-band radar pipeline for long-range hidden-scene reconstruction, experimentally demonstrated up to 40 m.
- **Neural illumination fields: High-fidelity and ambient-robust stereo reconstruction for two-bounce non-line-of-sight imaging** — Zhang et al., Optics and Lasers in Engineering 198:109514 (2026), DOI 10.1016/j.optlaseng.2025.109514. A self-supervised continuous neural field and differentiable-rendering method for robust two-bounce shadow inversion without binary segmentation.

## Synchronized artifacts

- `README.md`: both papers added with final verified venues and concise contribution summaries.
- `index.html`: both paper objects added; latest-entry count increased from 81 to 83; the 2026 timeline now includes long-range X-band radar and neural two-bounce fields.
- `article/5newscenes.tex`: NIF integrated in the two-bounce section and X-band radar integrated in the radar-NLOS section.
- `egbib_20260711_run15_updates.bib`: final-venue BibTeX records added.
- `bare_jrnl.tex`: the active bibliography command was corrected to include every supplemental `egbib*.bib` source, including this run. The previous active command still pointed only to `egbib`, despite a commented all-supplements example.

## PDF status

The GitHub Actions workflow performs a clean LaTeX/BibTeX rebuild, checks for undefined citations/references, validates the resulting PDF with `pdfinfo` and `pdftotext`, and confirms that both newly integrated paper titles appear in the generated survey text. The workflow records the final result below.

**Build result:** source synchronization and bibliography consolidation succeeded, but no strictly validated replacement PDF was committed. The prior PDF was preserved. Reason: PDF/reference validation failed (undefined=true, integrated=false, pdfinfo=0, pdftotext=0) (latexmk exit code 0). See `updates/2026-07-11-xband-nif-build-diagnostic.md`.
