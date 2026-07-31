# 31 July 2026 RF inverse-scattering citation trace and consistency audit

## Status

This pass identified a directly relevant RF/radar NLOS imaging lineage that is absent from the current `README.md`, website explorer, survey prose, and merged bibliography. It also corrected an existing source record that still labeled Geometry-Constrained NLOS Imaging as an arXiv preprint even though a final IEEE TVCG version is available.

Canonical metadata has been committed in:

- `egbib_20260731_rf_inverse_scattering_trace.bib`
- `egbib_20260714_geometric_constraints_updates.bib` (corrected in place to the final TVCG record)

The repository connector available in this run can replace complete files but cannot apply bounded line patches. Because `README.md`, `index.html`, `article/5newscenes.tex`, and `egbib_merged_20260711.bib` are large and actively updated, they were not replaced from partial snapshots. The exact integration patch is recorded below. The survey PDF is therefore not claimed as rebuilt.

## Newly verified missing lineage

### Non-Line-of-Sight Imaging by Linearized Inverse Scattering Method Based on Physical Optics

Hiroshi Suenobu, Takayuki Nakanishi, Yasuhiro Nishioka, Yoshio Inasawa, and Shouhei Kidera.  
*2024 International Conference on Electromagnetics in Advanced Applications (ICEAA)*, IEEE, 2024.  
DOI: `10.1109/ICEAA61917.2024.10701790`

This conference precursor applies a physical-optics linearization of the electromagnetic inverse-scattering problem to a known T-junction geometry. A numerically computed Green tensor includes the wall-mediated multipath connecting the radar aperture and hidden imaging region, allowing two-dimensional recovery of PEC scatterer position and extent in three-dimensional electromagnetic simulations.

Canonical key: `suenobuPhysicalOpticsNLOS2024`.

### Multipath Exploitation-Based Linearized Inverse Scattering Method for Non-Line-of-Sight Indoor Imaging of PEC Objects

Hiroshi Suenobu, Shouhei Kidera, Takayuki Nakanishi, Ryosuke Kobayashi, Yasuhiro Nishioka, and Yoshio Inasawa.  
*IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, 18, 6694--6709, 2025.  
DOI: `10.1109/JSTARS.2025.3537181`

The journal extension turns multipath from an artifact into the propagation operator of a linearized inverse-scattering reconstruction. It uses a geometry-specific numerical Green tensor and physical-optics approximation to image hidden PEC plates at an indoor T-junction, and validates the method with both full-wave three-dimensional simulations and measured 2 GHz anechoic-chamber data. This is genuine hidden-object radar imaging, not generic wireless NLOS identification.

Canonical key: `suenobuMultipathInverseScatteringNLOS2025`.

## Final-venue correction

`egbib_20260714_geometric_constraints_updates.bib` previously described **Geometric Constrained Non-Line-of-Sight Imaging** as arXiv:2503.17992. It now preserves the existing citation key for compatibility while using the verified final record:

- Title: **Geometry-Constrained Non-Line-of-Sight Imaging**
- Venue: *IEEE Transactions on Visualization and Computer Graphics*
- Volume/issue/pages: 32(7), 6524--6536
- Year: 2026
- DOI: `10.1109/TVCG.2026.3684832`

The merged bibliography must be regenerated so the final venue propagates into `bare_jrnl.pdf`.

## Required public-artifact integration

### 1. `README.md`

Change the update line to 31 July 2026 and insert the following rows near the radar/RF/mmWave additions:

```markdown
| 2025 | [Multipath Exploitation-Based Linearized Inverse Scattering Method for Non-Line-of-Sight Indoor Imaging of PEC Objects](https://doi.org/10.1109/JSTARS.2025.3537181) — Suenobu et al. | IEEE JSTARS 18, 6694–6709 (2025) | Treats wall-mediated multipath as a geometry-specific numerical Green tensor inside a physical-optics linearized inverse-scattering model. Full-wave simulation and measured 2 GHz T-junction experiments recover the location and planar extent of hidden PEC objects. |
| 2024 | [Non-Line-of-Sight Imaging by Linearized Inverse Scattering Method Based on Physical Optics](https://doi.org/10.1109/ICEAA61917.2024.10701790) — Suenobu et al. | IEEE ICEAA 2024 | Establishes the simulation-only precursor: known T-junction geometry and a numerically computed multipath Green tensor make physical-optics linearized inverse scattering applicable to hidden PEC targets. |
```

Add the following timeline statements in the radar/RF branch:

```text
2024 ── Suenobu et al.: physical-optics linearized inverse scattering embeds a known T-junction's multipath Green tensor for simulated hidden-PEC imaging [IEEE ICEAA]
2025 ── Suenobu et al.: the multipath-exploitation formulation is extended to full-wave simulation and measured 2 GHz indoor T-junction imaging [IEEE JSTARS]
```

The already committed but publicly unsynchronized CA-SlotNet, LMS-NLOS, and MSPDiff entries from `updates/20260731_passive_learning_citation_trace.md` should be integrated in the same edit.

### 2. `index.html`

Add the following paper-explorer objects, adapting whitespace to the current array style:

```javascript
{cat:"latest radar rf inverse-scattering multipath physical-optics measured",title:"Multipath Exploitation-Based Linearized Inverse Scattering Method for Non-Line-of-Sight Indoor Imaging of PEC Objects",authors:"Suenobu et al.",year:2025,venue:"IEEE JSTARS 2025",url:"https://doi.org/10.1109/JSTARS.2025.3537181",key:"A geometry-specific numerical Green tensor incorporates wall-mediated multipath into a physical-optics linearized inverse-scattering operator; full-wave and measured 2 GHz T-junction experiments recover hidden PEC targets."},
{cat:"radar rf inverse-scattering multipath physical-optics simulation",title:"Non-Line-of-Sight Imaging by Linearized Inverse Scattering Method Based on Physical Optics",authors:"Suenobu et al.",year:2024,venue:"IEEE ICEAA 2024",url:"https://doi.org/10.1109/ICEAA61917.2024.10701790",key:"Simulation precursor that uses known T-junction geometry and a numerical multipath Green tensor to linearize physical-optics inversion for hidden PEC imaging."},
```

Also integrate the three paper objects specified in `updates/20260731_passive_learning_citation_trace.md`, update visible dates to 31 July 2026, and derive the displayed explorer count from the resulting array rather than assuming a fixed number.

### 3. `article/5newscenes.tex`

Insert the following paragraph in the radar/RF/mmWave subsection, near the measured multipath-reconstruction discussion:

```latex
\vspace{0.8mm}
\noindent \textbf{Multipath-exploitation inverse scattering for RF NLOS.}
Suenobu~\etal~first applied a physical-optics linearization to a known indoor T-junction, using a numerically evaluated Green tensor to encode the wall-mediated paths between the radar aperture and hidden imaging region~\cite{suenobuPhysicalOpticsNLOS2024}. Their subsequent journal study extended this formulation to multipath-exploitation imaging of PEC objects~\cite{suenobuMultipathInverseScatteringNLOS2025}. Rather than suppressing indirect returns as ghosts, the method incorporates them into the forward operator and recovers hidden target position and planar extent. Three-dimensional full-wave simulations and measured 2~GHz anechoic-chamber experiments establish a complementary RF trajectory to mirror-symmetry backprojection and learned mmWave reconstruction: environment geometry is assumed known, while target scattering is inferred through a linearized inverse problem.
```

### 4. Passive-learning survey sections

Apply the already specified prose insertions from `updates/20260731_passive_learning_citation_trace.md`:

- LMS-NLOS and MSPDiff in `article/3passive.tex` after diffuse-aware attention encoding.
- CA-SlotNet in the recognition/clustering discussion of `article/4datadriven.tex`.

### 5. Bibliography

Run:

```bash
python3 scripts/merge_nlos_bibliography.py
```

Verify exactly one case-insensitive record for each key:

```text
suenobuPhysicalOpticsNLOS2024
suenobuMultipathInverseScatteringNLOS2025
linCASlotNetNLOS2025
chenLightweightMultiScalePassiveNLOS2025
jinMSPDiffPassiveNLOS2025
liuGeometricConstrainedNLOS2025
```

Verify that the geometry-constrained record in `egbib_merged_20260711.bib` contains DOI `10.1109/TVCG.2026.3684832`, year 2026, and journal `IEEE Transactions on Visualization and Computer Graphics`, with no remaining arXiv-only duplicate.

### 6. `bare_jrnl.tex` and PDF

Add a synchronization marker after `%% bare_jrnl.tex` only after the section prose and merged bibliography have been updated:

```latex
% 31 July 2026 citation trace: RF inverse-scattering lineage, CA-SlotNet, LMS-NLOS, MSPDiff, and the final TVCG geometry-constrained record synchronized.
```

Rebuild from a clean auxiliary state:

```bash
rm -f bare_jrnl.aux bare_jrnl.bbl bare_jrnl.blg bare_jrnl.log bare_jrnl.out bare_jrnl.toc
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
bibtex bare_jrnl
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
pdflatex -interaction=nonstopmode -halt-on-error bare_jrnl.tex
```

Validate:

```bash
grep -F "Multipath Exploitation-Based Linearized Inverse Scattering" README.md index.html article/5newscenes.tex
grep -F "suenobuMultipathInverseScatteringNLOS2025" article/5newscenes.tex egbib_merged_20260711.bib
grep -F "linCASlotNetNLOS2025" article/4datadriven.tex egbib_merged_20260711.bib
grep -F "chenLightweightMultiScalePassiveNLOS2025" article/3passive.tex egbib_merged_20260711.bib
grep -F "jinMSPDiffPassiveNLOS2025" article/3passive.tex egbib_merged_20260711.bib
grep -F "10.1109/TVCG.2026.3684832" egbib_merged_20260711.bib
! grep -E "Citation .* undefined|There were undefined citations|Repeated entry" bare_jrnl.log
pdftotext -layout bare_jrnl.pdf - | grep -Ei "Multipath Exploitation-Based|Contrast Adaptive Slot|polarization-guided diffusion|Lightweight multi-scale|Geometry-Constrained"
```

Render and inspect at least the first page, the RF discussion page, the passive-learning page, and the final bibliography pages before committing the regenerated binary.

## Current consistency state

Committed and accurate:

- `egbib_20260731_rf_inverse_scattering_trace.bib`
- corrected `egbib_20260714_geometric_constraints_updates.bib`
- `egbib_20260730_ca_slotnet.bib`
- `egbib_20260731_passive_learning_trace.bib`
- this update note and the earlier passive-learning patch note

Not claimed as synchronized in this run:

- `README.md`
- `index.html`
- `article/3passive.tex`
- `article/4datadriven.tex`
- `article/5newscenes.tex`
- `bare_jrnl.tex`
- `egbib_merged_20260711.bib`
- `bare_jrnl.pdf`

## Integration completed

The pending records in this note were synchronized across README, website, semantically appropriate survey sections, the consolidated bibliography, and the rebuilt survey PDF on 31 July 2026. The final integration also includes the RF inverse-scattering lineage and the final IEEE TVCG venue for Geometry-Constrained Non-Line-of-Sight Imaging.
