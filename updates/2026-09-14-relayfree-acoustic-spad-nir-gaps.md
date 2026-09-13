# NLOS gap update — 14 September 2026

This run combined fresh keyword search with a Core-paper forward-citation pass and repository-wide title/DOI checks. Three genuinely missing works survived relevance and duplication filtering. A fourth strong hit, Marco et al., *A comprehensive study of time-of-flight non-line-of-sight imaging* (arXiv:2603.09548), was **not** re-added because it is already documented in `updates/2026-06-28-tof-study-optimized-sampling-survey-sync.md` and was previously integrated into the survey workflow.

## 1. Passive acoustic NLOS without a relay surface

**Tal I. Sommer and Ori Katz, “Passive acoustic non-line-of-sight localization without a relay surface,” Physical Review Applied 25(2), 024064 (2026). DOI: 10.1103/p97k-sf71.**

Why it matters: most acoustic/optical NLOS methods depend on a visible relay wall or floor. Sommer and Katz instead localize a hidden acoustic point source from **edge diffraction**. For a doorway, the two door edges act as virtual detector arrays; for a convex corner, the method exploits the frequency-dependent knife-edge diffraction signature. This creates a distinct trajectory from relay-surface NLOS toward **relay-free diffraction-based NLOS localization**.

Recommended integration:
- README: add under **New NLOS Scenes and Modalities → Acoustic NLOS** and optionally Latest Additions.
- Website/Paper Explorer: category `Acoustic NLOS / localization`; timeline node `2026 — relay-free diffraction-based acoustic NLOS`.
- Survey: integrate into the acoustic-NLOS paragraph in `article/5newscenes.tex`, after prior relay-wall acoustic localization/imaging methods. Suggested synthesis sentence: “Recent acoustic work further relaxes the relay-surface assumption: Sommer and Katz exploit doorway and corner-edge diffraction to localize hidden sources directly from knife-edge signatures, extending acoustic NLOS from relay-mediated echoes toward relay-free diffractive sensing.”
- Bibliography: merge `sommerRelayFreeAcousticNLOS2026` from `egbib_20260914_missing_sensing_systems.bib` into the canonical bibliography.

This paper is also a high-value forward-citation hit: its reference list explicitly includes Velten et al. (2012), O’Toole et al. LCT (2018), Lindell et al. f-k (2019), and Liu et al. phasor-field work, but the paper itself is genuinely NLOS sensing rather than a passing citation.

## 2. Active SPAD/TCSPC hidden-human detection

**Semra Çelebi and İbrahim Türkoğlu, “Machine Learning-Based Human Detection Using Active Non-Line-of-Sight Laser Sensing,” Sensors 26(7), 2046 (2026). DOI: 10.3390/s26072046.**

Why it matters: this work shifts active transient NLOS from full scene reconstruction toward **task-oriented hidden-human detection** using real SPAD/TCSPC measurements. A 640-nm pulsed-laser / SPAD / TCSPC setup collects 50×50 relay-wall scans across multiple debris-like configurations and human subjects; CNN, GRU and Random Forest classifiers are compared on the measured time–photon histograms. The paper reports full sensitivity for human-present samples, with Random Forest giving the strongest overall accuracy/specificity under the tested conditions.

Recommended integration:
- README: place under **Active NLOS Imaging → Detection, Tracking and Recognition** and optionally Latest Additions.
- Website/Paper Explorer: tags `active optical`, `SPAD/TCSPC`, `human detection`, `task-oriented NLOS`.
- Survey: integrate in the active detection/tracking discussion rather than learned reconstruction. Suggested sentence: “Beyond reconstructing hidden geometry, recent SPAD–TCSPC systems increasingly target semantic decisions directly; Çelebi and Türkoğlu classify hidden-human presence from measured time–photon histograms, comparing convolutional, recurrent and ensemble models under debris-like NLOS configurations.”
- Bibliography: merge `celebiActiveNLOSHumanDetection2026` into the canonical bibliography.

## 3. Near-infrared raster-scanning NLOS system

**Mohammad Roueinfar and Mahdi Salmanian, “Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength,” 2025 33rd International Conference on Electrical Engineering (ICEE), pp. 1175–1179 (2025). DOI: 10.1109/ICEE67339.2025.11213924.**

The work only became easy to discover in this corpus after its July 2026 arXiv posting, but the final venue predates the preprint and should therefore be cited as **IEEE ICEE 2025**, not arXiv. It demonstrates a straightforward three-bounce NIR imaging system using an 808-nm, 500-mW laser and pan–tilt raster scanning over the relay wall, reconstructing three hidden targets and reporting MSE/RMSE against ground truth.

Recommended integration:
- README: add under active optical hardware/system demonstrations; do **not** label the venue as arXiv.
- Website/Paper Explorer: tags `active optical`, `NIR`, `raster scanning`, `three-bounce imaging`.
- Survey: this is a lower-impact but relevant system demonstration; one concise sentence in the active-hardware/practical-system subsection is sufficient rather than promoting it to a major milestone.
- Bibliography: merge `roueinfarNIRRasterNLOS2025` into the canonical bibliography.

## Consistency / build actions still required

The three papers were absent from repository code search by title/DOI at the start of this run. To avoid destructive whole-file replacement from truncated large-file payloads, this run stages verified BibTeX plus exact semantic insertion instructions instead of blindly overwriting `README.md`, `index.html`, modular LaTeX files, or the merged bibliography.

On the next safe full-file/patch-capable pass:
1. Merge the three BibTeX records into the bibliography actually referenced by `bare_jrnl.tex`.
2. Apply the README and website placements above.
3. Integrate the acoustic and task-oriented SPAD papers into the appropriate survey paragraphs; mention the NIR paper briefly in practical active-system coverage.
4. Rebuild `bare_jrnl.pdf` and check that README, website, survey source, bibliography and PDF all expose consistent venue/title metadata.
