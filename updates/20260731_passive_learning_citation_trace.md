# 31 July 2026 passive-learning and semantic NLOS citation trace

## Status

This citation-tracing pass verified three directly relevant missing works. Canonical BibTeX metadata has been committed for all three papers: CA-SlotNet is stored in `egbib_20260730_ca_slotnet.bib`, while LMS-NLOS and MSPDiff are stored in `egbib_20260731_passive_learning_trace.bib`.

The guarded GitHub Actions integration was attempted through both a push trigger and pull request #97, but no workflow run was created. Therefore this update does **not** claim that `README.md`, `index.html`, `article/3passive.tex`, `article/4datadriven.tex`, `bare_jrnl.tex`, `egbib_merged_20260711.bib`, or `bare_jrnl.pdf` have been synchronized. The exact safe integration patch is recorded below so the large public files are not replaced from a partial or stale snapshot.

## Verified missing papers

### Contrast Adaptive Slot-Attention Network for NLoS Classification Under Temporal Truncation

Yi Lin, Cikun Liu, Daoyuan Li, and Zuyuan Yang.  
*2025 International Conference on Electronic Information, Computer and Aerospace Remote Sensing (EICARS)*, pp. 140--143, IEEE, 2025.  
DOI: `10.1109/EICARS68214.2025.11320161`

CA-SlotNet was identified through a forward-citation trace from LEAP. It injects CLAHE/Sobel-derived local-contrast guidance into slot attention and adds a physically guided slot regularizer for semantic classification from temporally truncated, photon-sparse NLOS transients. It is a recognition result rather than hidden-image or 3D reconstruction.

Canonical key: `linCASlotNetNLOS2025`.

### Lightweight multi-scale feature fusion with attention guidance for passive non-line-of-sight imaging

Pengyun Chen, Shuang Cui, Ning Cao, Wenhao Zhang, Pengfei Wang, Shaohui Jin, and Mingliang Xu.  
*The Visual Computer*, 41(10), 7767--7780, 2025.  
DOI: `10.1007/s00371-025-03837-5`

LMS-NLOS combines multi-scale encoder--decoder features, detail-enhanced Transformer processing, asymmetric shallow/deep fusion, contour-aware supervision, and spatial-shift feed-forward units. Its compact configuration makes efficiency an explicit passive-NLOS design objective while retaining competitive reconstruction quality.

Canonical key: `chenLightweightMultiScalePassiveNLOS2025`.

### Enhanced passive non-line-of-sight imaging via multi-scale polarization-guided diffusion model

Shaohui Jin, Peng Zheng, Guangpeng Li, Huimin Wang, Manman Zhang, Wenhao Zhang, and Hao Liu.  
*The Visual Computer*, 41(13), 10789--10804, 2025.  
DOI: `10.1007/s00371-025-04069-3`

MSPDiff was found in the forward-citation chain of LMS-NLOS. It progressively reconstructs polarized long-wave-infrared relay observations from coarse to fine resolution and uses polarization as a physical guide inside diffusion sampling. The reported results reach 25.78 dB PSNR and 0.92 SSIM.

Canonical key: `jinMSPDiffPassiveNLOS2025`.

## Required integration

### 1. `README.md`

Change the update line to:

```markdown
**Update run: 31 July 2026.** This section tracks newly found or newly completed entries that were not explicitly covered in the previous README / homepage snapshot.
```

Immediately after the **Latest Additions** table divider, insert:

```markdown
| 2025 | [Contrast Adaptive Slot-Attention Network for NLoS Classification Under Temporal Truncation](https://doi.org/10.1109/EICARS68214.2025.11320161) — Lin et al. | IEEE EICARS 2025, 140–143 | Uses CLAHE/Sobel-guided contrast modulation and physically guided slot regularization to stabilize object-centric attention on temporally truncated, photon-sparse NLOS signals. It extends the learned-transient branch from reconstruction toward robust semantic classification under incomplete time-series measurements. |
| 2025 | [Enhanced passive non-line-of-sight imaging via multi-scale polarization-guided diffusion model](https://doi.org/10.1007/s00371-025-04069-3) — Jin et al. | The Visual Computer 41(13), 10789–10804 (2025) | MSPDiff progressively reconstructs polarized long-wave-infrared relay observations from coarse to fine resolution, using polarization as a physical cue inside diffusion sampling; the reported passive dataset results reach 25.78 dB PSNR and 0.92 SSIM. |
| 2025 | [Lightweight multi-scale feature fusion with attention guidance for passive non-line-of-sight imaging](https://doi.org/10.1007/s00371-025-03837-5) — Chen et al. | The Visual Computer 41(10), 7767–7780 (2025) | LMS-NLOS combines multi-scale encoding, detail-enhanced Transformer blocks, asymmetric shallow/deep fusion, contour-aware loss, and spatial-shift feed-forward units; its lightweight variant nearly halves model size while retaining strong passive reconstruction quality. |
```

In the 2025 milestone timeline, immediately before the current `Fu et al. and Zhou et al.` white-light entry, insert:

```text
2025 ── Chen et al.: LMS-NLOS couples lightweight multi-scale fusion and attention-guided detail recovery for deployable passive reconstruction [The Visual Computer]
   │     Jin et al.: MSPDiff introduces polarization-guided coarse-to-fine diffusion for passive LWIR NLOS reconstruction [The Visual Computer]
   │     Lin et al.: CA-SlotNet uses contrast-guided slot routing and physics-aware regularization for classification from temporally truncated photon sequences [IEEE EICARS]
```

### 2. `index.html`

Change the visible update dates from 30 July 2026 to 31 July 2026.

Immediately after `const papers=[`, insert:

```javascript
{cat:"latest learning recognition transient photon-sparse truncated slot-attention",title:"Contrast Adaptive Slot-Attention Network for NLoS Classification Under Temporal Truncation",authors:"Lin et al.",year:2025,venue:"IEEE EICARS 2025",url:"https://doi.org/10.1109/EICARS68214.2025.11320161",key:"CA-SlotNet injects CLAHE/Sobel-guided local-contrast modulation into slot attention and adds physically guided slot regularization, stabilizing semantic inference from incomplete photon-sparse transient sequences."},
{cat:"latest passive learning diffusion polarization thermal lwir",title:"Enhanced passive non-line-of-sight imaging via multi-scale polarization-guided diffusion model",authors:"Jin et al.",year:2025,venue:"The Visual Computer 2025",url:"https://doi.org/10.1007/s00371-025-04069-3",key:"MSPDiff uses polarized LWIR relay observations and progressive coarse-to-fine diffusion training, injecting polarization-derived physical cues into passive reconstruction and reporting 25.78 dB PSNR and 0.92 SSIM."},
{cat:"latest passive learning lightweight transformer attention multi-scale",title:"Lightweight multi-scale feature fusion with attention guidance for passive non-line-of-sight imaging",authors:"Chen et al.",year:2025,venue:"The Visual Computer 2025",url:"https://doi.org/10.1007/s00371-025-03837-5",key:"LMS-NLOS combines multi-scale encoder-decoder features, detail-enhanced Transformer processing, asymmetric fusion, contour-aware loss, and spatial-shift feed-forward units; the compact variant nearly halves model size."},
```

Prepend the 2025 timeline paragraph with:

```text
LMS-NLOS established a lightweight attention-guided passive reconstruction route, MSPDiff moved polarization cues into coarse-to-fine LWIR diffusion, and CA-SlotNet extended photon-transient learning toward classification under temporal truncation.
```

Recalculate the explorer count from the paper array. The audited snapshot contains 245 objects, so adding only these three records should produce 248; do not hard-code 248 if another update lands first.

### 3. `article/3passive.tex`

Immediately after the paragraph headed **Diffuse-aware attention encoding for passive NLOS**, insert:

```latex
\vspace{0.8mm}
\noindent \textbf{Lightweight fusion and polarization-guided diffusion.}
Chen~\etal~introduced LMS-NLOS~\cite{chenLightweightMultiScalePassiveNLOS2025}, combining multi-scale encoder--decoder features with a detail-enhanced Transformer, asymmetric shallow/deep fusion, contour-aware supervision, and spatial-shift feed-forward units. Its compact variant reduces model size by nearly one half while retaining competitive passive reconstruction, making efficiency an explicit design objective rather than a post-hoc compression step. Jin~\etal~subsequently proposed MSPDiff~\cite{jinMSPDiffPassiveNLOS2025}, which uses polarized long-wave-infrared relay observations and a coarse-to-fine diffusion schedule. Polarization supplies a physically meaningful guide to source and surface structure, while progressive diffusion restores increasingly fine hidden detail. Together, these works trace a transition from generic attention to deployable multi-scale networks and then to physics-guided generative priors for passive NLOS.
```

### 4. `article/4datadriven.tex`

In **From reconstruction to recognition and clustering**, immediately after the NCR-MVC sentence and before QSS-Net, insert:

```latex
The same group addressed temporally truncated photon sequences with CA-SlotNet~\cite{linCASlotNetNLOS2025}: CLAHE- and Sobel-guided local-contrast modulation adjusts slot-attention logits, while a physically guided slot regularizer stabilizes object routing when only part of the transient is observed.
```

Revise the paragraph's final sentence so the trajectory explicitly includes truncation-robust classification alongside recognition, action understanding, and clustering.

### 5. `bare_jrnl.tex`

Add this marker immediately after `%% bare_jrnl.tex`:

```latex
% 31 July 2026 forward-citation trace: CA-SlotNet, LMS-NLOS, and polarization-guided MSPDiff synchronized.
```

The literature discussion belongs in `article/3passive.tex` and `article/4datadriven.tex`, not in an appended paper list.

### 6. Consolidated bibliography

Run:

```bash
python3 scripts/merge_nlos_bibliography.py
```

Confirm one case-insensitive record for each key:

```text
linCASlotNetNLOS2025
chenLightweightMultiScalePassiveNLOS2025
jinMSPDiffPassiveNLOS2025
```

Also confirm the DOI records occur once in `egbib_merged_20260711.bib`.

### 7. Rebuild and validate `bare_jrnl.pdf`

From a clean checkout with LaTeX, BibTeX, Poppler, and the repository dependencies installed:

```bash
rm -f bare_jrnl.aux bare_jrnl.bbl bare_jrnl.blg bare_jrnl.log bare_jrnl.out bare_jrnl.toc
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
bibtex bare_jrnl
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
```

Then validate:

```bash
grep -F "Contrast Adaptive Slot-Attention Network" README.md index.html
grep -F "Enhanced passive non-line-of-sight imaging via multi-scale polarization-guided diffusion model" README.md index.html
grep -F "Lightweight multi-scale feature fusion with attention guidance for passive non-line-of-sight imaging" README.md index.html
grep -F "linCASlotNetNLOS2025" article/4datadriven.tex egbib_merged_20260711.bib
grep -F "chenLightweightMultiScalePassiveNLOS2025" article/3passive.tex egbib_merged_20260711.bib
grep -F "jinMSPDiffPassiveNLOS2025" article/3passive.tex egbib_merged_20260711.bib
! grep -E "Citation .* undefined|There were undefined citations|Repeated entry" bare_jrnl.log
pdfinfo bare_jrnl.pdf
pdftotext -layout bare_jrnl.pdf - | grep -Ei "Contrast Adaptive Slot|polarization-guided diffusion|Lightweight multi-scale feature fusion"
```

Render at least the first and final PDF pages before committing the binary, and verify that the PDF blob changes from the current version.

## Screened but not integrated

**Passive NLOS Imaging Based on Multi-Dimension Collaborative Attention Module** was verified as an SSRN preprint (DOI `10.2139/ssrn.5169297`). It is directly relevant, but no final peer-reviewed venue was found in this pass. It is therefore retained as a future candidate rather than being added beside the stronger published LMS-NLOS/MSPDiff lineage.

## Current consistency state

Committed metadata:

- `egbib_20260730_ca_slotnet.bib`
- `egbib_20260731_passive_learning_trace.bib`
- this patch/update note

Not claimed as updated:

- `README.md`
- `index.html`
- `article/3passive.tex`
- `article/4datadriven.tex`
- `bare_jrnl.tex`
- `egbib_merged_20260711.bib`
- `bare_jrnl.pdf`
