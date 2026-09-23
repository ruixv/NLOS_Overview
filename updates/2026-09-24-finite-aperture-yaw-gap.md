# 2026-09-24 integration gap: finite-aperture yaw limits

Verified missing paper:

Riccardo Romanelli, Lorenzo Francesco Livi, Francesco V. Pepe, Giacomo Sorelli, Enea Mauri, Milena D'Angelo, and Massimiliano Proietti, “Finite-Aperture Limits for Yaw Estimation in Confocal Non-Line-of-Sight Imaging,” *Journal of Imaging*, 12(6), 248, 2026. DOI: 10.3390/jimaging12060248.

## Why it belongs

This is a tightly relevant active/transient NLOS analysis paper rather than a passing citation. It studies a measurement-level limitation of confocal ToF NLOS: how a finite relay-wall aperture constrains planar-target yaw observability. It derives a switch-line geometric visibility criterion and complements it with Fisher-information analysis, showing that loss of unique planar reconstruction and loss of useful angular information occur at different yaw angles. Experiments/simulations with f-k migration and backprojection connect the analysis directly to established NLOS reconstruction methods and the missing-cone/visibility literature.

## Integration locations

- **README.md**: add under Active / Transient / Theory & Visibility (or the nearest finite-aperture/missing-cone subsection). Concise summary: “Characterizes yaw observability under finite relay-wall apertures using a switch-line visibility criterion and Fisher information, separating the loss of unique planar reconstruction from the gradual loss of angular sensitivity.”
- **Development timeline (2026)**: place near Stereo NLOS / arbitrary-relay / visibility-limit works as a theory-and-system-design milestone on finite-aperture observability.
- **index.html / Paper Explorer**: category `Active NLOS`, tags such as `transient`, `confocal`, `finite aperture`, `visibility`, `Fisher information`, `f-k`, `backprojection`.
- **bare_jrnl.tex**: integrate semantically in the active-ToF limitations / visibility / missing-cone discussion. A useful literature-review transition is that recent work moves beyond reconstruction algorithms to quantify which target orientations are identifiable from a finite relay aperture; the switch-line criterion gives a geometric uniqueness transition while Fisher information shows that orientation sensitivity degrades continuously and can remain nonzero beyond that transition.
- **Canonical bibliography**: merge the verified BibTeX staged in `egbib_20260924_finite_aperture_yaw_jimaging.bib`.
- **bare_jrnl.pdf**: rebuild only after the canonical TeX and bibliography have been safely integrated.

## Verification

Publisher metadata: *Journal of Imaging* 12(6), 248 (2026), DOI 10.3390/jimaging12060248. Publisher page reports publication on 2 June 2026. Repository-wide exact-title search returned no match before staging.

## Consistency status

This note and the staging BibTeX are committed because the large canonical public-facing files should not be overwritten from partial content. README.md, index.html, bare_jrnl.tex, the canonical bibliography, and bare_jrnl.pdf still require safe integration/rebuild; do not report them as synchronized until verified.
