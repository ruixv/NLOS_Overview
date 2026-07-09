# 2026-07-09 Phasor-field venue and survey consistency audit

This update run did not identify a new high-confidence July 2026 NLOS imaging paper beyond the current README/homepage frontier entries, including 3D Gaussian Transient Rendering, consumer-LiDAR NLOS, DENALI, GeRaF 2.0, RIS-assisted radar, and the 2026 ToF NLOS comparative study.

## Citation-tracing result

A citation-tracing pass around the phasor-field / virtual-wave branch did surface a metadata consistency issue rather than a new missing paper. The README and homepage already include the following phasor-field follow-up papers, so they should not be added as new papers again:

- Dove and Shapiro, **Paraxial Theory of Phasor-Field Imaging**, currently labelled `arXiv 2019` in README/homepage.
- Dove and Shapiro, **Paraxial phasor-field physical optics**, currently labelled `arXiv 2020` in README/homepage.
- Dove and Shapiro, **Nonparaxial phasor-field propagation**, currently labelled `arXiv 2020` in README/homepage.
- Reza et al., **Wave-like Properties of Phasor Fields: Experimental Demonstrations**, still only verified as arXiv 2019 in this run.
- Reza et al., **Phasor field waves: A statistical treatment for the case of a partially coherent optical carrier**, the arXiv page is marked withdrawn, so it should remain treated cautiously.

## Verified venue/status corrections

The following corrections should be made when public surfaces are next edited safely:

1. **Paraxial Theory of Phasor-Field Imaging**
   - Current README/homepage label: `arXiv 2019`
   - Verified related DOI on arXiv: `10.1364/OE.27.018016`
   - Recommended label: **Optics Express 2019**

2. **Paraxial phasor-field physical optics**
   - Current README/homepage label: `arXiv 2020`
   - Verified related DOI on arXiv: `10.1364/OE.396577`
   - Recommended label: **Optics Express 2020**

3. **Nonparaxial phasor-field propagation**
   - Current README/homepage label: `arXiv 2020`
   - Verified related DOI on arXiv: `10.1364/OE.401203`
   - Recommended label: **Optics Express 2020**

4. **Phasor field waves: A statistical treatment for the case of a partially coherent optical carrier**
   - Current README/homepage label: `arXiv 2020`
   - The arXiv page is marked withdrawn.
   - Recommended action: keep it visible only if the goal is to document phasor-field theory discussion, but add a caution note or remove it from `latest` if strict paper status is desired.

## README patch

Replace the venue/status labels in the existing rows:

```diff
-| 2020 | [Nonparaxial phasor-field propagation](https://arxiv.org/abs/2006.13775) — Dove, Shapiro | arXiv 2020 | Extends phasor-field propagation beyond the Fresnel/paraxial assumption using Rayleigh--Sommerfeld theory, closer to wide-angle reflective NLOS geometries. |
+| 2020 | [Nonparaxial phasor-field propagation](https://arxiv.org/abs/2006.13775) — Dove, Shapiro | Optics Express 2020 | Extends phasor-field propagation beyond the Fresnel/paraxial assumption using Rayleigh--Sommerfeld theory, closer to wide-angle reflective NLOS geometries. |

-| 2020 | [Paraxial phasor-field physical optics](https://arxiv.org/abs/2004.14239) — Dove, Shapiro | arXiv 2020 | Shows that ordinary lenses can focus or project phasor fields through diffusers, bridging computational virtual-wave NLOS and physical P-field optics. |
+| 2020 | [Paraxial phasor-field physical optics](https://arxiv.org/abs/2004.14239) — Dove, Shapiro | Optics Express 2020 | Shows that ordinary lenses can focus or project phasor fields through diffusers, bridging computational virtual-wave NLOS and physical P-field optics. |

-| 2019 | [Paraxial Theory of Phasor-Field Imaging](https://arxiv.org/abs/1903.02365) — Dove, Shapiro | arXiv 2019 | Provides a paraxial wave-optics and Wigner-distribution analysis of phasor-field imaging, clarifying which occluded and unoccluded geometries are supported by virtual-wave NLOS models. |
+| 2019 | [Paraxial Theory of Phasor-Field Imaging](https://arxiv.org/abs/1903.02365) — Dove, Shapiro | Optics Express 2019 | Provides a paraxial wave-optics and Wigner-distribution analysis of phasor-field imaging, clarifying which occluded and unoccluded geometries are supported by virtual-wave NLOS models. |
```

## Homepage patch

Replace the corresponding `venue` strings in `index.html`:

```diff
-venue:"arXiv 2020",url:"https://arxiv.org/abs/2006.13775"
+venue:"Optics Express 2020",url:"https://arxiv.org/abs/2006.13775"

-venue:"arXiv 2020",url:"https://arxiv.org/abs/2004.14239"
+venue:"Optics Express 2020",url:"https://arxiv.org/abs/2004.14239"

-venue:"arXiv 2019",url:"https://arxiv.org/abs/1903.02365"
+venue:"Optics Express 2019",url:"https://arxiv.org/abs/1903.02365"
```

## BibTeX patch

`egbib_20260704_updates.bib` currently stores these as `@misc` arXiv entries. When editing the bibliography directly, update at least these three entries:

```bibtex
@article{doveParaxialTheoryPhasor2019,
  title   = {Paraxial Theory of Phasor-Field Imaging},
  author  = {Dove, Justin and Shapiro, Jeffrey H.},
  journal = {Optics Express},
  year    = {2019},
  doi     = {10.1364/OE.27.018016},
  eprint  = {1903.02365},
  archivePrefix = {arXiv},
  url     = {https://arxiv.org/abs/1903.02365}
}

@article{doveParaxialPhysicalOptics2020,
  title   = {Paraxial phasor-field physical optics},
  author  = {Dove, Justin and Shapiro, Jeffrey H.},
  journal = {Optics Express},
  year    = {2020},
  doi     = {10.1364/OE.396577},
  eprint  = {2004.14239},
  archivePrefix = {arXiv},
  url     = {https://arxiv.org/abs/2004.14239}
}

@article{doveNonparaxialPhasor2020,
  title   = {Nonparaxial phasor-field propagation},
  author  = {Dove, Justin and Shapiro, Jeffrey H.},
  journal = {Optics Express},
  year    = {2020},
  doi     = {10.1364/OE.401203},
  eprint  = {2006.13775},
  archivePrefix = {arXiv},
  url     = {https://arxiv.org/abs/2006.13775}
}
```

## Survey-source patch

`article/2active.tex` already discusses the phasor-field branch, but the phasor-theory follow-up papers are not yet integrated narratively. Insert after the paragraph ending with Faccio et al.'s review in the wave-based methods subsection:

```tex
Several theory-oriented follow-ups further clarified the optical foundations of phasor-field NLOS. Dove and Shapiro developed a paraxial theory of phasor-field imaging and analyzed it with Wigner-distribution tools~\cite{doveParaxialTheoryPhasor2019}; they later showed that ordinary physical optics such as lenses can focus or project phasor fields through diffusers~\cite{doveParaxialPhysicalOptics2020}, and extended the propagation model beyond the paraxial regime using nonparaxial Rayleigh--Sommerfeld theory~\cite{doveNonparaxialPhasor2020}. Reza~\etal experimentally demonstrated wave-like phasor-field behavior~\cite{rezaWaveLikePhasorFields2019}. These works do not constitute a separate reconstruction pipeline, but they strengthen the link between virtual-wave NLOS computation and physical optical imaging systems.
```

## Remaining PDF / source consistency work

`bare_jrnl.tex` still uses only:

```tex
\bibliography{egbib}
```

The intended replacement remains:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates,egbib_20260706_updates,egbib_20260707_updates,egbib_20260708_updates}
```

The PDF was **not** regenerated in this run. The execution environment could not clone the GitHub repository through the local shell because DNS resolution for `github.com` failed, and the GitHub connector only provides safe text-file replacement / creation rather than a verified LaTeX build workspace. Do not claim `bare_jrnl.pdf` is updated until the full LaTeX tree is compiled and the binary PDF is uploaded.
