# Passive NLOS citation-lineage gaps — 19 August 2026

## Scope

This note records verified papers that remain absent from the current public README / canonical V2 paper corpus and should be integrated only through a guarded source-edit + clean LaTeX/BibTeX + PDF-validation workflow. It complements the already staged `updates/2026-08-19-hyperspectral-passive-gap.md` / `egbib_20260819_hyperspectral_passive_gap.bib` for **Hyper-NLOS**.

## Newly verified missing papers

### 1. Turning rough surfaces into non-line-of-sight cameras

- Wenwen Li, Yijun Zhou, Wei Li, Yutao Chen, Xin Huang, Chen Dai, Jianwei Zeng, Vivek K. Goyal, Feihu Xu, Jian-Wei Pan.
- **Optica 12(5), 626–634 (2025)**.
- DOI: `10.1364/OPTICA.544275`.
- Final venue is verified; do not label as arXiv.
- Contribution: derives a microscale rough-surface scattering model whose resulting passive light-transport inversion is well-conditioned; with an ordinary monochrome camera the paper demonstrates sub-mm spatial resolution, 25 fps, near-90° FOV, full-color recovery, mm-scale keyhole NLOS imaging, and non-invasive relay-wall calibration. The work is also a direct forward-citation descendant of the O'Toole/Liu active virtual-imaging lineage and is cited by later thermal rough-surface NLOS work, making it a high-priority milestone rather than a peripheral passive-imaging paper.

### 2. Passive Non-Line-of-Sight Imaging via Hyperspectral Autoencoder Net

- F. Li, F. Miao, Y. Zhang, M. Chen, P. Gao, P. Chen, S. Jin, M. Xu, H. Liu.
- **Proc. SPIE 13542, 135421R (2025)**, Fourth International Conference on Computational Imaging (CITA 2024).
- DOI: `10.1117/12.3055610`.
- Contribution: HAENet exploits hyperspectral information with spatial–spectral separation reconstruction (SS-SR) and spatial–spectral residual attention (SS-RA), providing a learned hyperspectral follow-up to Hyper-NLOS rather than another RGB-only passive reconstruction network.

### 3. Enhanced reflection U-Net reconstruction for passive Non-Line-of-Sight imaging

- Xiangzhi Yu, Weiqi Jin, Su Qiu, Li Li.
- **Optics and Precision Engineering 34(9), 1496–1506 (2026)**.
- DOI: `10.37188/OPE.20263409.1496`.
- Official journal metadata, publication date, authors, volume/issue/pages, and DOI are verified. The currently accessible publisher HTML does not expose a reliable full method abstract, so the public README/survey summary should remain conservative unless the article PDF or publisher abstract is available during integration. Do not invent architecture details beyond the verified U-Net/passive-NLOS scope implied by the title and journal record.

## Existing staged gap to integrate in the same pass

**Hyper-NLOS: hyperspectral passive non-line-of-sight imaging**, Optics Express 32(20), 34807–34824 (2024), DOI `10.1364/OE.532699`, key `chenHyperNLOS2024`, is already staged in `egbib_20260819_hyperspectral_passive_gap.bib` with a dedicated update note. It should be integrated together with the 2025 HAENet follow-up so the survey presents a coherent spectral trajectory rather than isolated entries.

## Required public-artifact edits

1. `README.md`
   - Add all verified records to Latest Additions only if absent by DOI/title.
   - Add the rough-surface paper to the 2025 passive-NLOS trajectory as a practical-conditioning/keyhole milestone.
   - Add Hyper-NLOS (2024) and HAENet (2025) as a hyperspectral passive-NLOS lineage.
   - Add the 2026 enhanced-reflection U-Net paper conservatively, without unsupported method claims.

2. `data/papers-source.html`
   - This is the canonical V2 paper corpus used by Paper Explorer / graph / timeline. Do not create a duplicate paper array in `index.html`.
   - Insert one canonical object per DOI and refresh the tracked-entry count automatically from the array.
   - Add concise 2024/2025/2026 timeline sentences matching the README categorization.

3. `article/3passive.tex`
   - Insert **Turning rough surfaces into non-line-of-sight cameras** near the practical/ordinary-camera passive-NLOS discussion. Suggested trajectory: calibrated/occluder-based steady-state inversion → physically modeled rough-relay encoding with well-conditioned inversion → long-range low-SBR passive imaging.
   - Create/extend a short paragraph headed along the lines of `Hyperspectral fusion for passive NLOS`: Hyper-NLOS 2024 establishes wavelength-resolved spatial–spectral conditioning and HS-NLOS; HAENet 2025 extends this through spatial–spectral separation and residual attention.
   - Place the 2026 enhanced-reflection U-Net entry with learned passive reconstruction only after a primary-source abstract/PDF confirms the detailed contribution; until then, a bibliographic/timeline mention is safer than an invented method description.

4. `egbib_merged_20260711.bib`
   - Merge `chenHyperNLOS2024` from `egbib_20260819_hyperspectral_passive_gap.bib`.
   - Merge the three entries from `egbib_20260819_passive_nlos_lineage_gap.bib`.
   - Enforce unique BibTeX keys and unique DOI identity before deleting staging files.

5. `bare_jrnl.tex`
   - Update the living-survey snapshot date only after the source files above are synchronized.
   - Preserve existing style/structure; do not append a disconnected paper dump.

6. `bare_jrnl.pdf`
   - Rebuild only after a clean LaTeX/BibTeX pass.
   - Require: no undefined citations/references; new citation keys in `.aux/.bbl`; DOI/key uniqueness; `pdftotext` semantic checks using whitespace/hyphenation-normalized tokens; first/last-page render checks.
   - Commit the binary PDF only if all checks pass. Otherwise leave the last known-good PDF unchanged and keep this note as the explicit blocker record.

## Suggested narrative after integration

A useful passive-NLOS trajectory is:

**ordinary-camera/occluder-based inversion → rough-relay physical encoding and well-conditioned keyhole imaging (Optica 2025) → long-range low-SBR passive imaging (Optics Letters 2025)**,

while the spectral branch becomes:

**RGB/intensity passive reconstruction → Hyper-NLOS hyperspectral conditioning + HS-NLOS (Optics Express 2024) → HAENet spatial–spectral autoencoding (Proc. SPIE 2025) → later multispectral/polarization/thermal spectral fusion**.

## Safety/status

No large public artifact was overwritten in creating this note. The public PDF must not be described as containing these records until a guarded build and consistency check succeeds.
