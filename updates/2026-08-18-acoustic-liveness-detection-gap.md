# 18 August 2026 — citation-traced acoustic NLOS liveness gap

## Verified missing work

**Yunus Emre Cetin, Mehmet Ercan Nergiz, Nevzat Olgun, Mucahit Calisan, Ferdi Dogan, Gürkan Gürgöze, and Ibrahim Turkoglu, “Comparative Analysis of Deep Latent Representation and Statistical Fusion Strategies Under Model Inductive Bias in Multichannel Acoustic Live Subject Detection,” IEEE Access, vol. 14, pp. 73343–73356, 2026. DOI: 10.1109/ACCESS.2026.3692353.**

Metadata verification:
- DBLP final record: `journals/access/CetinNOCDGT26`, IEEE Access 14: 73343–73356 (2026).
- DOI: https://doi.org/10.1109/ACCESS.2026.3692353
- ORCID/Crossref-backed author record confirms the final IEEE Access journal article and DOI.

This is genuinely NLOS sensing rather than a generic acoustic-classification paper. The measurement diagram uses a blocked direct path and a speaker → relay wall → hidden subject/object → relay wall → microphone return. The paper directly cites Lindell et al., *Acoustic Non-Line-of-Sight Imaging* (CVPR 2019), and explicitly positions itself after the ANLOS-R IEEE Access 2026 material-classification benchmark. Its contribution is a semantic extension from hidden geometry/material sensing to **live-human versus inanimate-object discrimination in cluttered acoustic NLOS scenes**. It compares raw eight-channel measurements, arithmetic-mean fusion, and a convolutional-transformer autoencoder (CT-AE) latent fusion across CNN/LSTM/Random-Forest classifiers, and highlights that fusion can help or destroy discriminative structure depending on model inductive bias.

The title, DOI, and citation key were absent from the current README / canonical V2 corpus / merged bibliography snapshot checked in this run.

A ready-to-merge BibTeX entry is staged in `egbib_20260818_acoustic_liveness_gap.bib` under key `cetinAcousticLivenessNLOS2026`.

## Required public-artifact patch

### 1. `README.md`

Insert near the top of **Latest Additions**:

```markdown
| 2026 | [Comparative Analysis of Deep Latent Representation and Statistical Fusion Strategies Under Model Inductive Bias in Multichannel Acoustic Live Subject Detection](https://doi.org/10.1109/ACCESS.2026.3692353) — Cetin et al. | IEEE Access 14, 73343–73356 (2026) | Extends acoustic NLOS semantic sensing from hidden material recognition to live-human versus inanimate-object discrimination in cluttered scenes; compares raw 8-channel measurements, arithmetic averaging, and convolutional-transformer latent fusion across deep and classical classifiers, showing that the best fusion strategy depends strongly on model inductive bias. |
```

In the 2026 milestone/timeline text, add a compact acoustic-semantic progression after ANLOS-R / acoustic-material sensing, e.g.:

> Acoustic NLOS also expands from hidden-source localization and material recognition to search-and-rescue semantics: Cetin et al. use multichannel wall-mediated echoes to distinguish live humans from clutter/debris and analyze how representation/fusion choices interact with classifier inductive bias.

Update the README run date to 18 August 2026 only when the public integration is actually committed.

### 2. Canonical V2 website corpus: `data/papers-source.html`

Add the following paper object in the 2026 acoustic / modality / learning / semantic-sensing neighborhood:

```js
{cat:"latest modality acoustic learning semantic detection search-rescue",title:"Comparative Analysis of Deep Latent Representation and Statistical Fusion Strategies Under Model Inductive Bias in Multichannel Acoustic Live Subject Detection",authors:"Cetin et al.",year:2026,venue:"IEEE Access 2026",url:"https://doi.org/10.1109/ACCESS.2026.3692353",key:"Uses wall-mediated multichannel acoustic echoes for live-human versus inanimate-object discrimination in cluttered NLOS scenes, and compares raw, arithmetic-mean, and convolutional-transformer latent fusion to expose strong interactions between representation choice and classifier inductive bias."},
```

Add the same development to the 2026 website timeline. `index.html` is the V2 shell; update only its displayed last-updated date/count if the current architecture requires it. Do not reintroduce a duplicate hard-coded paper array into `index.html`.

### 3. Survey prose: `article/5newscenes.tex`

Insert immediately **after** the paragraph headed `Material recognition from wall-mediated acoustic echoes.` and before `Robotic Exploration with NLOS Perception`:

```tex
\vspace{0.8mm}
\noindent \textbf{Acoustic liveness detection in cluttered NLOS scenes.}
Cetin~\etal~extend acoustic NLOS semantic sensing from hidden-source localization and material recognition to live-human versus inanimate-object discrimination for search-and-rescue settings~\cite{cetinAcousticLivenessNLOS2026}. Their blocked-path multichannel setup measures wall-mediated echoes from hidden people and clutter, and compares raw eight-channel signals, arithmetic channel averaging, and a convolutional--transformer autoencoder latent representation across convolutional, recurrent, and classical ensemble classifiers. The results expose a representation--model interaction: fusion that suppresses apparently redundant signal structure can improve one classifier while removing local phase/temporal cues needed by another. In the acoustic NLOS trajectory, this work therefore follows relay-free/source-localization and ANLOS-R material recognition with a task-oriented liveness branch, shifting evaluation from recovering hidden geometry or material labels toward deciding whether an occluded return corresponds to a living person or debris.
```

This paragraph should cite the final IEEE Access record, not a preprint.

### 4. Bibliography

Merge the single entry from `egbib_20260818_acoustic_liveness_gap.bib` into `egbib_merged_20260711.bib`. Before merging, assert that both the key and DOI occur zero times; after merging, assert exactly one occurrence of each. Remove the staging `.bib` after successful public integration.

### 5. `bare_jrnl.tex`

Add a provenance comment near the existing 18-August synchronization comments, for example:

```tex
% 18 August 2026 acoustic citation trace: multichannel acoustic NLOS liveness detection synchronized after ANLOS-R material sensing.
```

Keep the survey snapshot date at **through 18 August 2026** once this and the already-staged Ambient-IoT backscatter paper are actually integrated.

### 6. Rebuild and validate `bare_jrnl.pdf`

Do not claim the PDF is current until the sources above have been merged and a clean build succeeds:

```bash
rm -f bare_jrnl.aux bare_jrnl.bbl bare_jrnl.blg bare_jrnl.log bare_jrnl.out bare_jrnl.toc
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
bibtex bare_jrnl
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
```

Then verify:
- no undefined/multiply-defined citations in `bare_jrnl.log`;
- `cetinAcousticLivenessNLOS2026` appears in `bare_jrnl.aux` and the generated bibliography;
- extracted PDF text contains `Comparative Analysis of Deep Latent Representation` and the acoustic-liveness paragraph;
- first and last PDF pages render successfully;
- README, V2 paper corpus, timeline, survey prose, merged bibliography, and PDF all contain the same final IEEE Access venue/DOI.

## Interaction with the pending Ambient-IoT backscatter update

The previous 18-August candidate `Ambient IoT Backscatter Devices as Passive Anchors for NLOS Cellular Positioning: Fundamental Limits` (`arXiv:2607.03459`) is still absent from the currently fetched README / V2 corpus. The safest next full checkout should integrate **both** pending records in one guarded source update and one clean PDF rebuild, rather than rebuilding twice.

## Why this run uses a patch note

The connected GitHub interface can safely create small files but returns large public files in truncated form for whole-file writes. Overwriting `README.md`, `data/papers-source.html`, `article/5newscenes.tex`, the merged bibliography, or the binary PDF from truncated content would risk data loss. The repository’s Actions workflow also did not start from connector-authored trigger commits/PR events in this run. Following the repository-safety rule, no large public file or PDF was blindly overwritten, and this note records exact insertion locations and validated metadata for the next full-checkout integration.

## Integration status

Source integration is complete once this script's guarded build passes; the public PDF must only be committed after the clean LaTeX/BibTeX, citation, semantic-text, and render checks succeed.
