# 21 August 2026 — passive occluder-aided learned reconstruction gap

## Status

Three high-confidence missing papers in the learned passive / occluder-aided NLOS lineage were verified against the current canonical V2 corpus and repository search. They are staged here rather than written directly into the large public artifacts because open PRs #135 and #136 currently touch the same passive-NLOS integration path. `bare_jrnl.pdf` must therefore still be treated as the last validated public build until these records are integrated and a clean PDF rebuild passes.

The verified BibTeX records are in `egbib_20260821_passive_occluder_learning_gap.bib`.

## Verified missing papers

1. **Xin He, Pengfei Wang, Hao Liu, Xinde Yu, “Passive Non-Line-of-Sight imaging reconstruction based on dual input U-Net,” 2023 3rd International Conference on Neural Networks, Information and Communication Engineering (NNICE), pp. 337–341, 2023.** DOI: `10.1109/NNICE58320.2023.10105693`.
   - Directly belongs to passive learned NLOS reconstruction rather than generic image restoration.
   - A later peer-reviewed computational-imaging review identifies it as a two-input U-Net passive-NLOS reconstruction method.
   - Keep the public contribution summary conservative unless the original IEEE full text is available during integration: “Uses a dual-input U-Net for learned reconstruction from passive NLOS observations, representing an early supervised encoder-decoder branch after computational periscopy and NLOS-Passive.”

2. **Xinde Yu, Pengfei Gao, Hao Liu, Xin He, “CAGAN: A Channel-aware Generative Adversarial Network for Passive Non-Line-of-Sight Imaging,” NNICE 2023, pp. 508–512, 2023.** DOI: `10.1109/NNICE58320.2023.10105725`.
   - Uses a GAN for passive NLOS image reconstruction and introduces a channel-aware feature-fusion mechanism to emphasize informative channels and suppress background interference.
   - Reported evaluations use the public NLOS-Passive dataset, making the paper a direct downstream learned-reconstruction work rather than a citation in passing.

3. **Yoosun Kim, Mooseok Jang, “Reliable reconstruction of passive non-line of sight imaging with occluder by deep learning,” SPIE Advanced Biophotonics Conference (SPIE ABC 2023), Proc. SPIE 13076, 1307608, 2024.** DOI: `10.1117/12.3017933`.
   - Uses a standard digital camera plus an occluder and deep learning for fast passive hidden-object reconstruction.
   - The authors explicitly target robustness to changes in both occluder position and hidden-object position, making reliability across acquisition geometry the central contribution.

## Why these papers matter to the survey trajectory

The current survey already contains the stronger milestones around them: Saunders et al. computational periscopy, NLOS-Passive / NLOS-OT, the 2022 untrained deep-decoder approach, SPIR-Net, later attention/diffusion models, and MDUNet. The three records above close a missing intermediate lineage:

**calibrated computational periscopy → supervised passive encoder-decoder reconstruction → channel-aware adversarial reconstruction → geometry-robust occluder-aided learned reconstruction → later physics-guided / multimodal / diffusion passive NLOS.**

They should be described as historical learned-passive precursors, not as 2026 frontier papers.

## Exact integration plan

### 1. `README.md`

Add these rows under **Latest Additions** (the section already includes newly completed historical gaps, not only newly published papers):

```markdown
| 2024 | [Reliable reconstruction of passive non-line of sight imaging with occluder by deep learning](https://doi.org/10.1117/12.3017933) — Kim, Jang | Proc. SPIE 13076, 1307608 (2024) | Standard-camera occluder-aided passive NLOS reconstruction with deep learning; emphasizes robustness to changes in both occluder and hidden-object position. |
| 2023 | [CAGAN: A Channel-aware Generative Adversarial Network for Passive Non-Line-of-Sight Imaging](https://doi.org/10.1109/NNICE58320.2023.10105725) — Yu et al. | IEEE NNICE 2023 | Channel-aware GAN reconstruction on passive NLOS observations, using channel-feature fusion to emphasize informative content and suppress background interference. |
| 2023 | [Passive Non-Line-of-Sight imaging reconstruction based on dual input U-Net](https://doi.org/10.1109/NNICE58320.2023.10105693) — He et al. | IEEE NNICE 2023 | Early supervised dual-input U-Net reconstruction for passive NLOS, bridging NLOS-Passive-style data-driven inversion and later attention/generative methods. |
```

Add a compact 2023–2024 timeline sentence after the existing 2022 untrained-deep-decoder / NLOS-Passive learned branch and before the later SPIR-Net / event-camera / diffusion developments:

> He et al. and Yu et al. explored supervised dual-input U-Net and channel-aware GAN reconstruction on passive observations, while Kim and Jang subsequently emphasized occluder/object-position robustness in a standard-camera passive system.

### 2. Website / Paper Explorer

The canonical paper corpus is `data/papers-source.html`; do **not** create a second paper array in `index.html`. `index.html` should only receive the synchronized shell update date when required.

Add three paper objects with categories such as:

```text
latest passive learning occluder reconstruction unet
latest passive learning occluder reconstruction gan channel-aware
latest passive learning occluder reconstruction robustness
```

Use the three DOI URLs above and concise summaries matching the README wording. Increase the tracked-entry counter by exactly three and add the same 2023–2024 lineage to the website timeline.

### 3. `article/3passive.tex`

Insert a short literature-review block in the conventional-camera / learned-passive subsection, semantically adjacent to `Untrained neural priors for occluder-aided passive NLOS` and before later attention/diffusion/deployment-oriented methods. Suggested prose:

```latex
\vspace{0.8mm}
\noindent \textbf{Supervised occluder-aided passive reconstruction.}
Alongside physics-constrained and untrained priors, early supervised networks explored direct mappings from passive relay observations to hidden images. He~\etal~used a dual-input U-Net for passive NLOS reconstruction~\cite{heDualInputUNetPNLOS2023}, while Yu~\etal~introduced CAGAN, a channel-aware adversarial model that emphasizes informative feature channels and suppresses background interference on NLOS-Passive data~\cite{yuCAGANPNLOS2023}. Kim and Jang subsequently targeted reliability across acquisition geometry with a standard digital camera and an occluder, showing learned hidden-object reconstruction that is designed to tolerate changes in both occluder and target positions~\cite{kimReliableOccluderPNLOS2024}. Together, these studies fill the transition from calibrated computational periscopy and dataset-driven passive inversion toward later attention, diffusion, multimodal, and geometry-aware passive NLOS models.
```

Do not overstate architectural details for the dual-input U-Net beyond what can be verified from the final IEEE record / peer-reviewed review.

### 4. Bibliography

Merge the three entries from `egbib_20260821_passive_occluder_learning_gap.bib` into `egbib_merged_20260711.bib` exactly once. Before insertion, check both citation key and DOI to prevent duplicate records:

- `heDualInputUNetPNLOS2023` / `10.1109/NNICE58320.2023.10105693`
- `yuCAGANPNLOS2023` / `10.1109/NNICE58320.2023.10105725`
- `kimReliableOccluderPNLOS2024` / `10.1117/12.3017933`

Remove the staging BibTeX file only after all three canonical entries have been merged successfully.

### 5. `bare_jrnl.tex` and PDF

Update the survey coverage/provenance date only when the public integration is performed. Then run a clean LaTeX/BibTeX rebuild, for example:

```text
pdflatex bare_jrnl.tex
bibtex bare_jrnl
pdflatex bare_jrnl.tex
pdflatex bare_jrnl.tex
```

or the repository's existing `latexmk` workflow.

Validation must confirm:

- all three citation keys appear in `bare_jrnl.aux`;
- all three records appear in `bare_jrnl.bbl`;
- no undefined citations remain;
- each DOI and citation key is unique in the merged bibliography;
- README and `data/papers-source.html` each contain the three papers exactly once;
- `article/3passive.tex` contains all three keys;
- PDF text contains the supervised occluder-aided passive reconstruction discussion;
- first and last PDF pages render successfully;
- only after these checks pass should the rebuilt `bare_jrnl.pdf` be committed and described as updated.

## Conflict note

PR #135 is still the guarded integration path for Hyper-NLOS 2024 and *Turning rough surfaces into non-line-of-sight cameras* (Optica 2025), and PR #136 stages DCEEM (*Optics Communications* 2026). Because those changes target the same README / V2 corpus / passive-survey / bibliography / PDF files, this gap is intentionally staged as small, non-destructive files rather than overwriting the current public artifacts.
