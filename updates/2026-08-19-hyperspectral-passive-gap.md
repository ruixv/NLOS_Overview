# 19 Aug 2026 — hyperspectral passive NLOS gap

## Status

**Integrated on 20 August 2026.** The verified paper is now synchronized across README, the canonical V2 corpus/timeline, passive survey prose, merged bibliography, and rebuilt survey PDF. The remainder of this note is retained as provenance for the earlier gap analysis.

A fresh recent-paper search plus Core-paper / milestone forward-citation tracing identified one high-confidence paper that is still missing from the public survey artifacts:

- Mingyang Chen, Hao Liu, Shaohui Jin, Mengge Liu, Ziqin Xu, Xiaoheng Jiang, Ming Liang Xu, **“Hyper-NLOS: hyperspectral passive non-line-of-sight imaging,”** *Optics Express*, 32(20):34807–34824, 2024. DOI: `10.1364/OE.532699`.

Exact-title / DOI checks against the current public `README.md`, canonical V2 corpus `data/papers-source.html`, survey sources, and merged bibliography found no existing canonical entry for `Hyper-NLOS` / `10.1364/OE.532699`. A verified staging BibTeX record is stored in `egbib_20260819_hyperspectral_passive_gap.bib` under key `chenHyperNLOS2024`.

The final Optica metadata are **Volume 32, Issue 20, pages 34807–34824 (2024)**. Do not use the earlier incorrect issue/page metadata that appeared in preliminary notes.

## Why it belongs

Hyper-NLOS is directly about **passive non-line-of-sight imaging**, not generic hyperspectral reconstruction. It introduces HFN-Net, which exploits wavelength-resolved relay-wall measurements through a hyperspectral full-color autoencoder and spatial–spectral attention. The paper also introduces the HS-NLOS dataset. The key trajectory is therefore:

`RGB / intensity-only passive NLOS → wavelength-resolved hyperspectral conditioning → spatial–spectral learned reconstruction`

This is a useful missing precursor for the repository’s later multispectral / spectral-fusion passive-NLOS branch.

## Required public integration

### 1. `README.md`

Add a concise Latest Additions row using the **final Optics Express venue**, e.g.:

> **Hyper-NLOS: hyperspectral passive non-line-of-sight imaging** — *Optics Express*, 2024 — HFN-Net uses hyperspectral relay-wall measurements, a hyperspectral full-color autoencoder, and spatial–spectral attention to improve passive-NLOS color fidelity and structural recovery; introduces the HS-NLOS dataset.

Also add a 2024 development-timeline milestone near the passive learned / multispectral branch. Suggested wording:

> **Hyperspectral passive NLOS:** Hyper-NLOS moves passive reconstruction beyond RGB/intensity-only relay measurements by using spectral diversity as an additional conditioning signal.

Do not create a duplicate if the DOI or title has entered `README.md` by the time this patch is applied.

### 2. Canonical website corpus

The current V2 site reads its paper corpus / timeline from `data/papers-source.html`; do **not** insert a duplicate paper array into `index.html`.

Add a canonical paper record for:

- title: `Hyper-NLOS: hyperspectral passive non-line-of-sight imaging`
- authors: `Mingyang Chen; Hao Liu; Shaohui Jin; Mengge Liu; Ziqin Xu; Xiaoheng Jiang; Ming Liang Xu`
- year: `2024`
- venue: `Optics Express`
- DOI/link: `10.1364/OE.532699`
- category: passive / learned reconstruction / spectral or hyperspectral, following the existing taxonomy
- key: `chenHyperNLOS2024`

Add the same 2024 hyperspectral-passive milestone to the website timeline. Recompute any tracked-entry count only from the canonical corpus rather than hard-coding an assumed value.

### 3. `article/3passive.tex`

Insert a short literature-review paragraph in the passive learned-reconstruction sequence, before the later 2025–2026 multispectral / dual-spectral deployment papers. A suitable semantic insertion is after the ordinary-camera learned passive discussion and before later lightweight/polarization/thermal spectral-fusion work.

Suggested prose (adapt to the surrounding style rather than pasting blindly):

> `\noindent \textbf{Hyperspectral fusion for passive NLOS.}` Chen~\etal~move passive reconstruction beyond RGB or intensity-only relay measurements by explicitly exploiting wavelength-resolved observations~\cite{chenHyperNLOS2024}. Their HFN-Net combines a hyperspectral full-color autoencoder with spatial--spectral attention so that complementary bands provide additional conditioning for an otherwise ill-posed steady-state inverse problem. The accompanying HS-NLOS dataset supplies wavelength-resolved training and evaluation data. This work establishes spectral diversity as an additional sensing dimension for passive NLOS and provides a precursor to later multispectral, polarization-assisted, and dual-spectral reconstruction systems.

Keep the prose concise and avoid claiming that spectral diversity alone resolves the inverse problem.

### 4. Bibliography

Merge `egbib_20260819_hyperspectral_passive_gap.bib` into `egbib_merged_20260711.bib` exactly once. Before merging, check both:

- citation key `chenHyperNLOS2024`
- DOI `10.1364/OE.532699`

Delete the staging BibTeX only after the canonical merged bibliography contains the verified entry and a clean build succeeds.

### 5. `bare_jrnl.tex` / survey date

The survey body is modular, so the substantive citation belongs in `article/3passive.tex`; do not append a detached paper list to `bare_jrnl.tex`. Once all public artifacts are integrated, update the survey provenance / coverage date to **through 19 August 2026** if that is still the current integration date.

### 6. PDF rebuild and validation

After the public source patch is applied, clean-build the survey:

```text
pdflatex bare_jrnl.tex
bibtex bare_jrnl
pdflatex bare_jrnl.tex
pdflatex bare_jrnl.tex
```

Then verify:

- `chenHyperNLOS2024` appears in `bare_jrnl.aux` / bibliography output;
- no duplicate key or DOI exists;
- `pdftotext bare_jrnl.pdf` contains the hyperspectral-passive survey prose and the correct survey date;
- first and last pages render successfully;
- `README.md`, `data/papers-source.html`, `article/3passive.tex`, `egbib_merged_20260711.bib`, `bare_jrnl.tex`, and `bare_jrnl.pdf` are mutually consistent.

Only after all checks pass should the rebuilt `bare_jrnl.pdf` be committed.

## Additional missing candidates verified but not yet integrated

### Hyperspectral Autoencoder Net — SPIE 2025

`Passive Non-Line-of-Sight Imaging via Hyperspectral Autoencoder Net`, Proc. SPIE Vol. 13542, article 135421R (2025), DOI `10.1117/12.3055610`, is a likely direct follow-up in the same spectral branch. The DOI / proceedings identity is verifiable, and available indexing describes spatial–spectral reconstruction / attention. However, the currently accessible publisher metadata are insufficient here to guarantee the complete author metadata at the same standard as the main survey bibliography. **Do not add a guessed BibTeX record.** Recover complete publisher-author metadata first, then integrate if confirmed absent.

### Enhanced reflection U-Net — OPE 2026

`Enhanced reflection U-Net reconstruction for passive Non-Line-of-Sight imaging`, *Optics and Precision Engineering* 34(9):1496–1506 (2026), DOI `10.37188/OPE.20263409.1496`, is also absent by exact-title / DOI checks and has verifiable final journal metadata. The accessible official page currently exposes publication metadata but not enough method detail to support a reliable survey-quality contribution summary. Keep it as a high-confidence candidate and add it only after the method / abstract can be verified from the paper itself or another authoritative source.

## Interaction with the existing 18-Aug pending integration

There is already an open guarded integration path for the separately verified 18-Aug RF-backscatter and acoustic-liveness records. Its source-level integration has run, but the public commit is intentionally blocked until the PDF semantic/render validation succeeds. Do not bypass that safeguard by replacing large public files from truncated connector output.

For the same reason, this 19-Aug Hyper-NLOS discovery is staged as a small verified BibTeX record plus this precise patch note rather than a risky partial overwrite. The public PDF must continue to be treated as the last successfully validated build until a clean cross-artifact integration passes.
