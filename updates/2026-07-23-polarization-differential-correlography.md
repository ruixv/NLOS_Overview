# 23 July 2026 — Polarization differential correlography citation trace

## Verified missing paper

**High-resolution non-line-of-sight imaging via polarization differential correlography**  
Lingfeng Liu, Shuo Zhu, Yi Wei, Jingye Miao, Wenjun Zhang, Lianfa Bai, Enlai Guo, and Jing Han  
*Chinese Optics Letters*, 23(8), 081104, 2025  
DOI: `10.3788/COL202523.081104`  
Published online: 31 July 2025

The paper is a direct steady-state active-NLOS reconstruction method, not an incidental NLOS citation. PDC-NLOS uses independently polarized laser speckles and polarization differencing to form a correlographic estimate of the hidden object before phase retrieval. The single-shot encoding avoids mechanical relay scanning, improves stability against vibration and coloured perturbations, and demonstrates millimeter-level resolution. The paper reports an average SSIM near 0.76, compared with about 0.6 for the authors' earlier chromato-axial differential-correlography system.

Its literature lineage connects steady-state NLOS, computational periscopy, active focusing, polarized infrared NLOS, deep inverse correlography, and event-driven NLOS tracking. It is therefore placed in the active laser-plus-conventional-camera discussion rather than appended as an unclassified recent work.

## Intended synchronized artifacts

The guarded synchronizer `scripts/sync_nlos_20260723_pdc_nlos.py` performs the following fail-closed edits:

1. `README.md`
   - adds the final journal record and contribution summary to Latest Additions;
   - adds a 2025 steady-state polarization/correlography milestone;
   - updates the run date to 23 July 2026.
2. `index.html`
   - adds a searchable active/steady-state/polarization paper object;
   - updates tracked latest entries from 184 to 185;
   - extends the 2025 timeline and synchronizes header/footer dates.
3. `article/2active.tex`
   - adds the citation to the continuous-laser/conventional-camera system table;
   - adds a literature-review paragraph after the low-cost NIR steady-state discussion.
4. `bare_jrnl.tex`
   - adds an integration marker and advances survey coverage through 23 July 2026.
5. Bibliography
   - merges `egbib_20260723_pdc_nlos.bib` into the consolidated bibliography with one DOI/key occurrence.
6. `bare_jrnl.pdf`
   - is rebuilt only after source, bibliography, citation, page, and extracted-text validation succeeds.

## Exclusions in this pass

Fresh arXiv, Optica, ACM, recent-conference, and core-paper forward-citation searches did not reveal a direct NLOS imaging paper with a verified publication date later than the already integrated PICL record of 15 July 2026. Generic NLOS communications, hidden-message recognition, and transient/LiDAR papers without hidden-scene reconstruction were excluded.
