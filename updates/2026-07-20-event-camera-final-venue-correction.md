# Event-camera passive NLOS final-venue correction — 20 July 2026

**STATUS: STAGED — verified final metadata and precise insertion instructions are committed; the large public artifacts and survey PDF have not been replaced or rebuilt in this run.**

## 1. Verified correction and relevance

The repository currently lists **Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding** as an arXiv 2024 paper. The work has a verified final publication:

- **Final title:** Event-Enhanced Passive Non-Line-of-Sight Imaging for Moving Objects With Physical Embedding
- **Authors:** Conghe Wang, Xia Wang, Yujie Fang, Changda Yan, Xin Zhang, Yifan Zuo
- **Final venue:** IEEE Sensors Journal, vol. 24, no. 22, pp. 37970--37985, 2024
- **Publication date:** 15 November 2024
- **DOI:** `10.1109/JSEN.2024.3468909`
- **Publisher URL:** https://doi.org/10.1109/JSEN.2024.3468909
- **Canonical BibTeX key:** `wangEventEnhancedPassiveNLOS2024`
- **Verified BibTeX supplement:** `egbib_20260720_event_camera_final_venue.bib`

This is a direct passive NLOS reconstruction paper rather than an event-camera paper that only mentions NLOS. Its EPNP prototype uses an event camera to extract asynchronous motion features from the relay-wall diffusion pattern, pre-trains a physics-embedded model on simulated measurements, and fine-tunes it with limited real measurements for moving hidden-object reconstruction. Its literature context explicitly includes active transient NLOS foundations such as the light-cone transform and f-k migration, while its technical contribution expands passive NLOS toward neuromorphic acquisition.

## 2. README.md correction

Replace the current arXiv entry for this paper with the following final-venue row. Do not add a second entry.

```markdown
| 2024 | [Event-Enhanced Passive Non-Line-of-Sight Imaging for Moving Objects With Physical Embedding](https://doi.org/10.1109/JSEN.2024.3468909) — Wang et al. | IEEE Sensors Journal 2024 | Introduces EPNP, an event-camera-enhanced passive NLOS prototype that extracts asynchronous motion cues from relay-wall diffusion patterns and combines simulation pretraining with limited measured-data fine-tuning for moving hidden-object reconstruction. |
```

In the milestone timeline, place the following item under **2024**, near passive dynamic imaging and event-camera developments:

```text
   │     Wang et al.: event-enhanced passive NLOS — asynchronous relay-wall changes and physics-embedded learning enable reconstruction of moving hidden objects [IEEE Sensors Journal]
```

Add an audit note for 20 July 2026 stating that the arXiv record was upgraded to its final IEEE Sensors Journal publication and integrated into the passive-method survey discussion.

## 3. Website / index.html correction

Find the existing paper-explorer object whose title is `Event-enhanced Passive Non-line-of-sight imaging for moving objects with Physical embedding`. Replace it in place with one canonical final-venue object, following the local JavaScript formatting:

```javascript
{cat:"passive event camera dynamic moving object physics embedded neuromorphic",title:"Event-Enhanced Passive Non-Line-of-Sight Imaging for Moving Objects With Physical Embedding",authors:"Wang et al.",year:2024,venue:"IEEE Sensors Journal 2024",url:"https://doi.org/10.1109/JSEN.2024.3468909",key:"EPNP uses an event camera to isolate asynchronous motion-induced changes in the relay-wall diffusion pattern, then combines physics-based simulation pretraining with limited real-data fine-tuning for moving hidden-object reconstruction."},
```

Update any latest-additions or timeline copy that still labels the work as arXiv. Because this is an in-place venue correction, the homepage paper count must not increase unless the current explorer does not yet contain the paper.

## 4. Survey-source integration

### `article/3passive.tex`

Add the following row to Table `tab:passive`, near the existing conventional-camera moving-object/action entries:

```latex
\cite{wangEventEnhancedPassiveNLOS2024} & Ambient/incoherent illumination & Event camera + conventional camera & Asynchronous diffusion-pattern motion with physics-embedded learning & Dynamic 2D reconstruction\\%%%% Table body
```

Insert the following literature-review paragraph after the current paragraph on passive action recognition from relay-wall video, or at the nearest semantically equivalent location in the conventional-camera subsection:

```latex
\vspace{0.8mm}
\noindent \textbf{Event-camera passive NLOS for moving objects.}
Wang~\etal~introduced an event-enhanced passive NLOS prototype that records asynchronous changes in the relay-wall diffusion pattern and combines them with a physics-embedded reconstruction network~\cite{wangEventEnhancedPassiveNLOS2024}. Simulation-based pretraining captures dynamic light transport and sensor characteristics, while limited measured data are used for fine-tuning. This work extends ordinary-frame passive NLOS toward neuromorphic acquisition: the event stream emphasizes weak motion-induced changes that would otherwise be temporally aliased or attenuated in conventional video.
```

This paragraph should remain in the passive-sensor and dynamic-reconstruction discussion rather than being appended to a detached recent-paper list.

### `bare_jrnl.tex`

Do not append a standalone citation list. Preserve the master structure and include the paper through the semantically integrated `article/3passive.tex` discussion. Advance the survey audit/coverage comment to 20 July 2026 only after the source merge is actually applied.

## 5. Bibliography merge

Merge the single entry from `egbib_20260720_event_camera_final_venue.bib` into the bibliography source used by `bare_jrnl.tex` (currently the consolidated NLOS bibliography in the repository). Before merging:

1. Search for DOI `10.1109/JSEN.2024.3468909`, the arXiv identifier `2404.05977`, and title variants.
2. Replace any preprint-only record rather than retaining both versions.
3. Preserve one canonical key, preferably `wangEventEnhancedPassiveNLOS2024`.
4. Confirm the generated `.bbl` cites the final journal record.

## 6. Cross-artifact consistency and build work still required

Before this correction can be described as fully integrated:

1. Apply the guarded in-place edits to `README.md`, `index.html`, `article/3passive.tex`, and the consolidated bibliography.
2. Confirm the paper appears exactly once in README and the website, once in the bibliography, and is cited in the passive survey source.
3. Integrate or explicitly retain as pending the two scan-free active-NLOS papers recorded in `updates/2026-07-19-scanfree-spatial-correlation-citation-trace.md`; they remain absent from the current public README snapshot.
4. Clean-build `bare_jrnl.tex` with LaTeX/BibTeX.
5. Check for undefined citations, duplicate keys/DOIs, missing references, and critical LaTeX errors.
6. Inspect the regenerated `bare_jrnl.pdf` and verify the event-camera paragraph and final IEEE Sensors Journal bibliography entry are present.
7. Commit the PDF only after source and PDF validation pass.

The newest directly verified NLOS paper found in the associated fresh search remains **Non-line-of-sight imaging via physics-informed cascade learning**, published in JOSA A on **15 July 2026**. No later direct NLOS imaging publication with a verifiable publication date was identified in this pass.

**`README.md`, `index.html`, `article/3passive.tex`, the consolidated bibliography, and `bare_jrnl.pdf` were not overwritten or rebuilt in this run. This note is a safe patch plan, not a claim that the public artifacts are already synchronized.**
