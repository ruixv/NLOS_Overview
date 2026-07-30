# CA-SlotNet citation-trace integration note — 30 July 2026

## Verified missing paper

**Contrast Adaptive Slot-Attention Network for NLoS Classification Under Temporal Truncation**  
Yi Lin, Cikun Liu, Daoyuan Li, and Zuyuan Yang  
*2025 International Conference on Electronic Information, Computer and Aerospace Remote Sensing (EICARS)*, pp. 140–143, IEEE, 2025.  
DOI: `10.1109/EICARS68214.2025.11320161`  
ISBN: `979-8-3315-8752-9`

This paper was identified in the forward-citation list of **Learning to Enhance Aperture Phasor Field for Non-Line-of-Sight Imaging (LEAP)** and then checked against independent scholarly metadata records. It is a genuine NLOS semantic-sensing contribution rather than a generic wireless NLoS paper: CA-SlotNet operates on temporally truncated, photon-sparse NLOS measurements, injects CLAHE/Sobel-derived local-contrast guidance into slot attention, and adds a physically guided slot regularizer to stabilize classification when only part of the transient sequence is available.

The final IEEE conference record is used as the venue. No arXiv-only label should be used.

Canonical BibTeX is stored in `egbib_20260730_ca_slotnet.bib` under the key `linCASlotNetNLOS2025`.

## Why this run uses a patch-style note

The available repository write interface replaces complete UTF-8 files rather than applying guarded line-level patches. `README.md`, `index.html`, `article/4datadriven.tex`, and `egbib_merged_20260711.bib` are large and have received frequent concurrent updates. Replacing them from a partial or stale snapshot risks truncation or loss of newer entries. The execution environment also cannot safely compile and upload the binary PDF from the current repository state. Therefore, this run commits verified metadata and the exact integration instructions below, but does **not** claim that the public artifacts or `bare_jrnl.pdf` are synchronized.

## Required integration

### 1. `README.md`

In **Latest Additions**, insert the following row immediately after the table header, or group it with the other learned recognition papers:

```markdown
| 2025 | [Contrast Adaptive Slot-Attention Network for NLoS Classification Under Temporal Truncation](https://doi.org/10.1109/EICARS68214.2025.11320161) — Lin et al. | IEEE EICARS 2025, 140–143 | Uses CLAHE/Sobel-guided contrast modulation and physically guided slot regularization to stabilize object-centric attention on temporally truncated, photon-sparse NLOS signals. It extends the learned-transient branch from reconstruction toward robust semantic classification under incomplete time-series measurements. |
```

In **Milestone Timeline**, place the following item in the 2025 learned-recognition trajectory, immediately before the existing QSS-Net item:

```text
   |     Lin et al.: CA-SlotNet uses contrast-guided slot attention and physics-aware regularization for NLOS classification from temporally truncated photon sequences [IEEE EICARS]
```

Keep the scope explicit: this is semantic classification, not hidden-image or 3D-geometry reconstruction.

### 2. `index.html`

Add this object near the existing QSS-Net/NCR-MVC recognition entries in the `papers` array:

```javascript
{cat:"latest learning recognition transient photon-sparse truncated slot-attention",title:"Contrast Adaptive Slot-Attention Network for NLoS Classification Under Temporal Truncation",authors:"Lin et al.",year:2025,venue:"IEEE EICARS 2025",url:"https://doi.org/10.1109/EICARS68214.2025.11320161",key:"CA-SlotNet injects CLAHE/Sobel-guided local-contrast modulation into slot attention and adds physically guided slot regularization, stabilizing semantic inference from incomplete photon-sparse transient sequences."},
```

Add this sentence to the 2025 timeline paragraph:

```text
CA-SlotNet further used contrast-guided slot routing and physics-aware regularization to classify hidden objects from temporally truncated photon sequences.
```

Recalculate the explorer count from the JavaScript array. The snapshot inspected in this run contains 245 entries, so adding only this record changes the displayed count from **245** to **246**. Do not hard-code 246 if other entries are merged first.

### 3. `article/4datadriven.tex`

In the subsection **End-to-End algorithms**, locate the paragraph headed:

```latex
\noindent \textbf{From reconstruction to recognition and clustering.}
```

Insert the following sentence after the NCR-MVC sentence and before the QSS-Net sentence:

```latex
Lin~\etal~also address temporally truncated photon sequences with CA-SlotNet~\cite{linCASlotNetNLOS2025}: CLAHE- and Sobel-guided local-contrast modulation adjusts slot-attention logits, while a physically guided slot regularizer stabilizes object routing when only part of the transient is observed.
```

Revise the paragraph's concluding sentence so that the trajectory explicitly includes truncation-robust semantic classification alongside recognition, action understanding, and clustering.

### 4. Bibliography used by `bare_jrnl.tex`

`bare_jrnl.tex` currently cites `egbib_merged_20260711.bib`. Merge `egbib_20260730_ca_slotnet.bib` into that generated bibliography by rerunning the repository merge script, preferably:

```bash
python scripts/merge_nlos_bibliography.py
```

If the script's source-file discovery is explicit rather than glob-based, add `egbib_20260730_ca_slotnet.bib` to its input list first. Confirm exactly one case-insensitive occurrence of `linCASlotNetNLOS2025` and DOI `10.1109/EICARS68214.2025.11320161` in the merged file.

### 5. `bare_jrnl.tex`

Add an update marker before the section inputs:

```latex
% 30 July 2026 LEAP forward-citation trace integrates CA-SlotNet for temporally truncated NLOS classification.
```

Update the title-footnote coverage date from `26 July 2026` to `30 July 2026` after all current public entries have been checked against the survey source. The literature discussion itself belongs in `article/4datadriven.tex`, not in an appended paper list.

### 6. Rebuild `bare_jrnl.pdf`

From a clean checkout with LaTeX and BibTeX installed, run either:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl.tex
```

or the repository-compatible equivalent:

```bash
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
bibtex bare_jrnl
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
```

Commit the regenerated `bare_jrnl.pdf` only after confirming that no citations are undefined and that the PDF binary actually changed.

## Consistency checks

Run these checks after integration:

```bash
grep -F "Contrast Adaptive Slot-Attention Network" README.md index.html article/4datadriven.tex egbib_merged_20260711.bib
grep -F "linCASlotNetNLOS2025" article/4datadriven.tex egbib_merged_20260711.bib
python - <<'PY'
from pathlib import Path
s = Path('index.html').read_text(encoding='utf-8')
print('paper objects:', s.count('{cat:'))
PY
pdftotext bare_jrnl.pdf - | grep -F "Contrast Adaptive Slot-Attention Network"
```

Also verify:

1. README and website use **IEEE EICARS 2025**, not arXiv, as the venue.
2. The contribution is categorized under learned NLOS recognition/semantic sensing.
3. The paper appears once in README, once in the website explorer, once in the semantic literature discussion, and once in the merged bibliography.
4. `bare_jrnl.pdf` contains both the discussion citation and the resolved bibliography entry.
5. No newer repository edits were lost while applying the patch.

## Current synchronization status

Committed in this run:

- `egbib_20260730_ca_slotnet.bib`
- this integration note

Not claimed as updated in this run:

- `README.md`
- `index.html`
- `article/4datadriven.tex`
- `bare_jrnl.tex`
- `egbib_merged_20260711.bib`
- `bare_jrnl.pdf`
