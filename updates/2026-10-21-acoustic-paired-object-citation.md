# 2026-10-21 — Acoustic paired-object NLOS citation update

## Verified paper
Mücahit Çalışan, "Classification of Paired-Object Combinations in Non-Line-of-Sight Environments from Secondary Acoustic Reflections: Multi-Seed Evaluation of Spectral Representations and Multi-Channel Strategies," *Applied Sciences* **16**(20), 10293, published 17 October 2026. DOI: https://doi.org/10.3390/app162010293.

The study uses wall-reflected 2–20 kHz chirps and an eight-speaker/eight-microphone array to classify four hidden paired-object combinations (120 recordings). STFT features and a random forest yield 0.9850 ± 0.0207 mean accuracy over repeated recording-level cross-validation. This is **semantic acoustic NLOS sensing**, not geometric NLOS imaging. Results are from a single room; recordings from the same acquisition group may cross folds. No unseen-session/room generalization is demonstrated.

## Citation relevance
The publisher article directly references Lindell et al.'s CVPR 2019 acoustic NLOS imaging and O'Toole et al.'s Nature 2018 LCT, and discusses recent wall-mediated acoustic material recognition. This is a verified, tightly adjacent forward-citation successor, not an incidental NLOS keyword hit.

## Integration
README: latest additions, acoustic modality category, and milestone timeline.
Website: index.html recent update and data/papers-source.html timeline, narrative, and paper explorer.
Survey: article/5newscenes.tex acoustic material-recognition paragraph cites `calisan2026pairedacoustic`; bare_jrnl.tex already includes this chapter via `\\input{article/5newscenes.tex}`. A comment-only edit to bare_jrnl.tex was blocked by the connector and is not required for inclusion.
Bibliography: egbib_merged_20260711.bib includes publisher-verified article metadata and DOI.

## PDF publication status
**bare_jrnl.pdf has NOT been rebuilt or uploaded**. The previously observed blob SHA is `6fc5e00f2a7aee93692f6ee41a7074a4c59de9e6`. A complete LaTeX checkout with images and styles is required. Build with pdflatex/bibtex/pdflatex/pdflatex (or the repository's existing build instructions), inspect unresolved citations and warnings, then commit the generated PDF. Do not claim the binary survey is synchronized before checking its changed SHA and successful build log.
