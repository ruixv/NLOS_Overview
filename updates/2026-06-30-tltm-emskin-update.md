# 2026-06-30 TLTM + EM-skin NLOS update

## Added / integrated entries

This update integrates two verified missing NLOS-relevant papers and one metadata correction.

### 1. Iterating the Transient Light Transport Matrix for Non-Line-of-Sight Imaging
- **Authors:** Talha Sultan, Eric Brandt, Khadijeh Masumnia-Bisheh, Simone Riccardo, Pavel Polynkin, Alberto Tosi, Andreas Velten
- **Status:** arXiv 2024
- **Link:** https://arxiv.org/abs/2412.10300
- **Why included:** It is directly about time-resolved NLOS imaging. It extends the relay-surface transient light transport matrix (TLTM) from a passive measurement object into an iterated computational sensing system, enabling hidden-scene relighting, direct/indirect transport separation, and dual-photography-style operations.

### 2. Multi-View Near-field Imaging in NLOS with Non-Reconfigurable EM Skins
- **Authors:** Davide Tornielli Bellini, Dario Tagliaferri, Marouan Mizmizi, Stefano Tebaldini, Umberto Spagnolini
- **Status:** arXiv 2024
- **Link:** https://arxiv.org/abs/2401.06891
- **Why included:** It is a radar/NLOS imaging work using static passive electromagnetic skins. It complements RIS-assisted, IRS-assisted, and naturally specular reflector-aware RF NLOS works already tracked in the repository.

### 3. Soft Shadow Diffusion metadata correction
- **Corrected status:** arXiv 2026
- **Link:** https://arxiv.org/abs/2601.12257
- **Reason:** No reliable venue evidence was found for the previous ECCV 2024 label. The arXiv metadata lists the paper as a 2026 arXiv preprint, so the repository now uses arXiv 2026 unless a final venue is later verified.

## Repository changes made

- `README.md`
  - Updated latest-run date to 30 June 2026.
  - Added TLTM iteration and EM-skin radar NLOS entries.
  - Corrected Soft Shadow Diffusion from ECCV 2024 to arXiv 2026.

- `article/5newscenes.tex`
  - Added a new subsection: `Transient Light-Transport-Matrix Iteration`.
  - Integrated non-reconfigurable electromagnetic skins into the RF/mmWave radar NLOS paragraph.

- `article/6conclusion.tex`
  - Added TLTM iteration to the forward-model / reconstruction-infrastructure discussion.
  - Added passive electromagnetic skins to the new-modality and relay-geometry discussion.

- `egbib_2026_updates.bib`
  - Added BibTeX entries:
    - `sultanIteratingTLTM2024`
    - `tornielliEMSkinsNLOS2024`
  - Corrected SSD metadata with key:
    - `rajiSoftShadowDiffusion2026`

## Candidate papers checked but not added

- `Lightweight Non-Line-of-Sight Channel Detection for ML-assisted Bluetooth Direction Finding` — rejected for now because it is mainly BLE LOS/NLOS channel classification, not NLOS imaging, hidden-scene reconstruction, hidden localization, or tightly adjacent computational sensing.
- `Near-lossless method for generating thermal photon-bunched light` — not added because it is a source-engineering / photon-statistics paper that mentions NLOS imaging as a possible application, but is not itself a NLOS imaging or reconstruction paper.
- `MIMO Capacity Enhancement by Grating Walls` — not added because it focuses on communication capacity and channel engineering rather than hidden-scene sensing or NLOS imaging.

## Website/index.html patch still needed

`index.html` is a compact but large whole-file GitHub contents update. To avoid accidental truncation, this run did not overwrite it directly. Recommended changes:

1. Change the latest-entry count from `31` to `33`.
2. Change the footer date from `29 June 2026` to `30 June 2026`.
3. In the `papers` array, add:

```js
{cat:'latest active', title:'Iterating the Transient Light Transport Matrix for Non-Line-of-Sight Imaging', authors:'Sultan et al.', year:2024, venue:'arXiv 2024', url:'https://arxiv.org/abs/2412.10300', key:'Computationally focuses a relay-surface TLTM into the hidden scene to obtain second-order transport, relighting, and dual-photography-style operations.'},
{cat:'latest modality active', title:'Multi-View Near-field Imaging in NLOS with Non-Reconfigurable EM Skins', authors:'Tornielli Bellini et al.', year:2024, venue:'arXiv 2024', url:'https://arxiv.org/abs/2401.06891', key:'Static passive electromagnetic-skin modules focus radar energy into NLOS regions and support multi-view near-field radar imaging.'},
```

4. Correct the SSD entry to:

```js
{cat:'latest passive learning', title:'Soft Shadow Diffusion (SSD): Physics-inspired Learning for 3D Computational Periscopy', authors:'Raji and Murray-Bruce', year:2026, venue:'arXiv 2026', url:'https://arxiv.org/abs/2601.12257', key:'Single ordinary NLOS photograph to 3D hidden scene via soft-shadow physics and a neural solver.'},
```

## PDF compilation status

`bare_jrnl.pdf` was not regenerated in this run. The source files and BibTeX supplement were updated, but the available GitHub connector only supports UTF-8 text file replacement, not a safe LaTeX build plus binary PDF upload. The remaining steps are:

1. Change the bibliography line in `bare_jrnl.tex` from:

```tex
\bibliography{egbib}
```

to:

```tex
\bibliography{egbib,egbib_2026_updates}
```

2. Compile locally, e.g.:

```bash
pdflatex bare_jrnl.tex
bibtex bare_jrnl
pdflatex bare_jrnl.tex
pdflatex bare_jrnl.tex
```

3. Upload the regenerated `bare_jrnl.pdf`.
