# 22 July 2026 citation trace: experimental NLOS micro-Doppler drone detection

## Added record

**Detection of sUAS in Urban Environments using Multi-Antenna Micro-Doppler Radar**  
Chamindu Liyanage, Chirantha Kurukulasuriya, Chathuni Wijegunawardana, Wikum Kumara, Chamira U. S. Edussooriya, and Arjuna Madanayake  
Accepted for presentation at the **2026 IEEE 104th Vehicular Technology Conference (VTC2026-Fall)**, Boston, 6–9 September 2026.  
arXiv:2607.11868. A DOI/proceedings record was not publicly available at the time of this update, so the repository retains the arXiv link while labeling the verified accepted venue.

## Why it belongs in the overview

The paper reports a hardware-validated, fully NLOS radar experiment rather than a propagation-only simulation or a generic drone classifier. A 2.47 GHz continuous-wave MIMO prototype with one transmitter and four receivers records propeller micro-Doppler through cabinets, doors, and walls in indoor and semi-urban scenes. Spectral correlation density exposes cyclostationary rotor signatures under multipath, and a compact EfficientNet-B0 classifier reaches 86.11% overall accuracy, compared with 73.77% for a single-channel baseline.

The work expands the radar/RF branch of NLOS sensing from hidden vehicles, pedestrians, localization, and 3D geometry toward experimental low-altitude aerial-threat detection. It is deliberately categorized as **detection-only / tightly adjacent NLOS sensing**: the airframes remain stationary while the propellers rotate, and the paper does not estimate hidden-target position, track motion, or reconstruct 3D shape.

## Citation-tracing rationale

The paper connects its urban-NLOS motivation to prior around-corner Doppler radar and optical learned NLOS tracking/reconstruction, including NLOST. It was retained only after checking the experimental geometry and confirming that the direct path was physically blocked in the reported measurements; citation proximity alone was not considered sufficient.

## Guarded integration

`scripts/sync_nlos_20260722_suas_radar.py` performs fail-closed, unique-anchor edits to:

- add one README Latest Additions row and one 2026 timeline milestone;
- add one searchable website paper object, extend the 2026 timeline, and update the tracked-entry count from 182 to 183;
- insert a semantically placed radar-survey paragraph after the existing urban-intersection FMCW discussion in `article/5newscenes.tex`;
- add a master-source integration marker to `bare_jrnl.tex`.

`egbib_20260722_suas_nlos_radar.bib` supplies the canonical accepted-venue metadata. The associated workflow regenerates the consolidated bibliography, performs a clean LaTeX/BibTeX build, validates citations and PDF text, and commits the synchronized sources and rebuilt `bare_jrnl.pdf` only if all checks succeed.
