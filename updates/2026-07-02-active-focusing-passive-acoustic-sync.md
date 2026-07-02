# 2026-07-02 Active-Focusing and Passive-Acoustic NLOS Sync

This run found two relevant missing / partially integrated NLOS works while tracing papers that cite or are surfaced alongside core active/acoustic NLOS milestones.

## Newly verified / corrected entries

1. **High-resolution non-line-of-sight imaging employing active focusing**  
   Ruizhi Cao, Frederic de Goumoens, Baptiste Blochet, Jian Xu, Changhuei Yang.  
   **Nature Photonics 2022**, 16, 462--468. DOI: `10.1038/s41566-022-01009-8`.  
   The paper introduces UNCOVER active focusing: wavefront shaping is used to focus light through the relay/scattering wall onto the hidden target, then raster-scan the focus for high-resolution NLOS imaging. The Nature page reports publication on **30 May 2022** and a resolution of about **0.6 mm** at **0.55 m**. This work was already partially cited in `article/2active.tex` through `\cite{caohighresolutionnlos2022}`, but the BibTeX key was missing from the active survey bibliography supplements and it was not surfaced in README / homepage latest additions.

2. **Towards passive non-line-of-sight acoustic localization around corners using uncontrolled random noise sources**  
   Jeremy Boger-Lombard, Yevgeny Slobodkin, Ori Katz.  
   **Scientific Reports 2023**, 13, Article 4952. DOI: `10.1038/s41598-023-31490-2`.  
   The paper extends acoustic NLOS from controlled active chirps toward passive correlation / acoustic-daylight imaging. It retrieves Green functions from cross-correlations of uncontrolled broadband noise and localizes / tracks a hidden person around a corner. The Nature page reports publication on **27 March 2023**. This is a strong missing predecessor to the later relay-free passive acoustic NLOS line.

## Repository changes made safely

- Updated `egbib_20260702_updates.bib` with:
  - `caohighresolutionnlos2022`
  - `bogerLombardPassiveAcousticCorners2023`

Commit: `afdf2ef375a460f020abd14a909855660245a9d8`

## Recommended README patch

Insert these rows in `README.md` under **Latest Additions**, preserving chronological order:

```md
| 2023 | [Towards passive non-line-of-sight acoustic localization around corners using uncontrolled random noise sources](https://www.nature.com/articles/s41598-023-31490-2) — Boger-Lombard et al. | Scientific Reports 2023 | Uses passive correlation / acoustic-daylight imaging with uncontrolled broadband noise sources to retrieve Green functions and localize / track a hidden person around a corner. |
| 2022 | [High-resolution non-line-of-sight imaging employing active focusing](https://www.nature.com/articles/s41566-022-01009-8) — Cao et al. | Nature Photonics 2022 | UNCOVER wavefront-shaping method actively focuses light onto hidden targets through a relay/scattering wall, enabling sub-millimetre high-resolution NLOS scanning. |
```

The active-focusing paper should be placed near the 2022 THz entry; the passive-acoustic paper should be placed near the 2023 active-corner / arbitrary-pattern entries.

## Recommended `index.html` patch

- Update the latest-entry count from `40` to `42`.
- Add both papers to Latest Additions / Paper Explorer / Timeline:
  - `Nature Photonics 2022` / active focusing / UNCOVER / wavefront shaping.
  - `Scientific Reports 2023` / passive acoustic / uncontrolled noise / Green-function correlation.

## Recommended LaTeX survey patch

`article/2active.tex` already contains the active-focusing discussion and the citation key `caohighresolutionnlos2022`. With the BibTeX entry now added, this reference is ready for compilation once the main bibliography line includes `egbib_20260702_updates`.

For passive acoustic NLOS, insert the following sentence into `article/5newscenes.tex` in the **Acoustic NLOS Imaging** subsection, before the current relay-free passive acoustic paragraph:

```tex
Boger-Lombard~\etal~later extended acoustic NLOS toward passive correlation imaging~\cite{bogerLombardPassiveAcousticCorners2023}. Instead of emitting controlled chirps, their system estimates the Green functions between microphone pairs from cross-correlations of uncontrolled broadband noise, then uses the recovered pulse-echo-like timing information to localize and track a person hidden around a corner. This acoustic-daylight setting is an important bridge between active acoustic NLOS and relay-free passive acoustic localization, because it shows that ambient or uncontrolled sound fields can become useful NLOS probes when sufficient bandwidth and averaging are available.
```

## PDF / bibliography status

`bare_jrnl.pdf` was **not** regenerated in this run. The source-side bibliography supplement now contains the missing active-focusing and passive-acoustic entries, but `bare_jrnl.tex` still needs to use:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates}
```

Then run a local LaTeX/BibTeX build and upload the regenerated `bare_jrnl.pdf`. Current connector writes are whole-file replacements, so large public-facing files were not overwritten blindly.
