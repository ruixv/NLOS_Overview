# 6 July 2026 — Quantized RIS radar-sensing consistency update

## Search / citation-tracing result

A fresh keyword search and forward-citation-style pass over active optical NLOS, phasor-field / virtual-wave NLOS, RF/mmWave around-corner sensing, RIS-aided radar, consumer-LiDAR NLOS, acoustic NLOS, passive NLOS, neural transient fields, and 3D Gaussian transient rendering did not reveal a newer high-confidence 2026 optical NLOS imaging frontier paper beyond the currently tracked entries such as 3D Gaussian Transient Rendering, Consumer-LiDAR NLOS, GeRaF 2.0, DENALI, and the ToF NLOS benchmark.

The main genuinely missing adjacent item found in this run is:

- **Radar Cross Section Characterization of Quantized Reconfigurable Intelligent Surfaces** — Kainat Yasmeen, Shobha Sundar Ram, Debidas Kundu, **arXiv 2026**, <https://arxiv.org/abs/2603.27961>.

## Why this is relevant

This paper is not a full hidden-scene reconstruction method, but it is tightly adjacent to the existing RIS / around-corner radar entries already tracked in the README. It provides the aperture-field and radar-cross-section characterization for low-complexity quantized RIS hardware, and the arXiv abstract reports experiments where a fabricated 1-bit RIS redirects radar energy into non-specular / shadowed regions and recovers micro-Doppler signatures that remain undetectable under conventional radar deployment. This makes it relevant to the repository's RF/mmWave / RIS-assisted NLOS sensing thread.

No final conference or journal venue was verified during this run, so the entry should be labeled **arXiv 2026** until publisher metadata appears.

## Files updated safely

- `egbib_20260706_updates.bib`
  - Added BibTeX key: `yasmeenRCSQuantizedRIS2026`.
  - Commit: `de96e61e06f7587ecc4ae313fe8f5fb20f8b6e13`.

## Recommended README patch

Insert this row near the other 2026 RIS/radar entries, preferably after `Radar Sensing using Dual-Beam Reconfigurable Intelligent Surface`:

```markdown
| 2026 | [Radar Cross Section Characterization of Quantized Reconfigurable Intelligent Surfaces](https://arxiv.org/abs/2603.27961) — Yasmeen et al. | arXiv 2026 | Characterizes one-bit / quantized RIS radar cross section and experimentally shows RIS redirection can recover micro-Doppler signatures in non-specular or shadowed regions. |
```

## Recommended homepage patch

In `index.html`, update the visible update metadata from `4 July 2026` to `6 July 2026`, increment the latest-entry count accordingly, and insert this object after the existing dual-beam RIS paper object:

```javascript
{cat:'latest modality',title:'Radar Cross Section Characterization of Quantized Reconfigurable Intelligent Surfaces',authors:'Yasmeen et al.',year:2026,venue:'arXiv 2026',url:'https://arxiv.org/abs/2603.27961',key:'Aperture-field/RCS characterization of quantized RIS radar hardware; experiments show non-specular beam redirection and recovery of micro-Doppler signatures in shadowed regions.'},
```

Also apply the previously noted homepage consistency fixes that are still outstanding: the top 2026 entries should remain `arXiv 2026` unless final venue pages are verified, and the homepage should surface all README-listed latest additions rather than keeping the latest counter stale.

## Recommended survey-source patch

In the RF / RIS / EM-skin part of the survey source, add a short sentence such as:

```tex
Complementary RIS hardware studies further characterize practical quantized apertures: Yasmeen et al. analyze the radar cross section of one-bit RIS panels and experimentally show that quantized beam redirection can recover micro-Doppler signatures in non-specular or shadowed regions~\cite{yasmeenRCSQuantizedRIS2026}.
```

This belongs semantically near the existing around-corner RIS radar entries, not in the optical active NLOS section.

## Bibliography / PDF status

`egbib_20260706_updates.bib` now contains the new BibTeX entry. The survey PDF was **not** regenerated in this run. To include all update supplements, `bare_jrnl.tex` still needs to use:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates}
```

Then rebuild locally with LaTeX/BibTeX and upload the regenerated `bare_jrnl.pdf`. This run did not silently claim a PDF update.

## Excluded candidates

- **Near-lossless method for generating thermal photon-bunched light** — adjacent to future timing-correlation NLOS ideas, but it is a thermal-light-source paper rather than NLOS imaging or hidden-scene reconstruction.
- Generic Wi-Fi / communications / missile-search results that use “NLOS” in a propagation or weapons sense were excluded because they are not NLOS imaging / sensing papers.
