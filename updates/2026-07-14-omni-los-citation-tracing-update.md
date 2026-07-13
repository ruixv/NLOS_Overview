# 14 July 2026 Omni-LOS citation-tracing update

## Search result

A fresh search of arXiv, publisher pages, project/lab pages, and citation/reference chains did not reveal a directly relevant NLOS-imaging paper submitted later than the repository's already covered 5 July 2026 NIR raster-scanning paper. The high-priority citation-tracing pass did identify one genuine missing work in the neural-transient / implicit-surface branch:

- **Omni-Line-of-Sight Imaging for Holistic Shape Reconstruction** — Binbin Huang, Xingyue Peng, Siyuan Shen, Suan Xia, Ruiqian Li, Yanhua Yu, Yuehan Wang, Shenghua Gao, Wenzheng Chen, Shiying Li, and Jingyi Yu; arXiv:2304.10780 (2023).

The paper explicitly builds on the core transient NLOS line represented by LCT, f-k migration, phasor-field virtual wave optics, Neural Transient Fields, edge-resolved transient imaging, and neural implicit surface reconstruction. It is directly relevant rather than a passing citation: the method places an object near diffuse walls, jointly renders direct LOS rays and diffuse-wall NLOS spherical wavefronts, and optimizes a unified neural level-set representation. A SPAD/laser prototype demonstrates near-360-degree holistic shape recovery from one fixed scan position.

No final conference or journal publication could be verified from the arXiv record, publisher searches, author/project searches, or scholarly-index searches as of 14 July 2026. The repository therefore labels it conservatively as **arXiv 2023**.

## Repository integration

The marker-based synchronizer updates the following artifacts without blind whole-file replacement:

1. `README.md`
   - adds the paper to Latest Additions with an arXiv link and concise contribution summary;
   - extends the 2023 milestone path between fast differentiable transient rendering and virtual mirrors;
   - updates the run date to 14 July 2026.
2. `index.html`
   - adds a searchable `latest active learning` paper object;
   - changes the tracked-latest count from 94 to 95;
   - expands the 2023 timeline with joint LOS/NLOS holistic reconstruction;
   - updates both the homepage header and footer dates to 14 July 2026.
3. `article/2active.tex`
   - inserts a literature-review paragraph after NLOS-NeuS and before diffusion reconstruction, explaining how Omni-LOS unifies LOS and NLOS transient rendering in one neural level-set model.
4. `egbib_20260714_omnilos_updates.bib`
   - adds canonical BibTeX key `huangOmniLOS2023` using verified arXiv metadata.
5. `bare_jrnl.tex`, merged bibliography, and `bare_jrnl.pdf`
   - `scripts/merge_nlos_bibliography.py` regenerates the duplicate-free bibliography and preserves the survey's consolidated bibliography command;
   - CI performs a clean LaTeX/BibTeX build and verifies the new citation in the source, `.aux`, `.bbl`, extracted PDF text, and rendered PDF pages.

**Build result:** successful marker-based synchronization and clean LaTeX/BibTeX rebuild. README, homepage paper explorer, 2023 timeline, neural-representation survey narrative, canonical BibTeX metadata, duplicate-free merged bibliography, and `bare_jrnl.pdf` consistently include Omni-LOS. PDF metadata, text extraction, before/after page rendering, citation, missing-key, and duplicate-entry checks passed.

**Footer consistency follow-up:** staged for validation so the homepage header and footer use the same 14 July 2026 date.
