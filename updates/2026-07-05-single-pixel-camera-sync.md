# 2026-07-05 Single-pixel camera NLOS sync

## Search result

The latest 2026 frontier searches and citation-tracing pass did not reveal a higher-priority new July 2026 NLOS imaging paper beyond the current frontier list. However, a missing earlier active optical NLOS hardware entry was found during SPAD / single-pixel / scannerless acquisition tracing:

- **Non-line-of-sight 3D imaging with a single-pixel camera** — Musarra, Lyons, Conca, Altmann, Villa, Zappa, Padgett, Faccio, **arXiv 2019**.  
  Link: https://arxiv.org/abs/1903.04812

## Relevance decision

This is a direct NLOS 3D reconstruction paper. It uses a DMD-based time-resolved single-pixel camera with SPAD/PMT detection, couples the single-pixel transient measurements with back-projection, demonstrates full-color hidden 3D reconstruction, and reports a sub-second Hadamard acquisition regime. It is therefore relevant to the active optical / SPAD / scannerless / single-pixel acquisition branch rather than merely citing NLOS work in passing.

No reliable final journal or conference venue was verified in this run, so the repository labels the paper as **arXiv 2019**.

## Files updated

- `README.md`
  - Added the Musarra et al. single-pixel-camera NLOS paper to **Latest Additions**.
- `egbib_20260705_updates.bib`
  - Added the BibTeX entry with key `musarraNonlineofsight3DImaging2019`.

## Survey-source status

`article/2active.tex` already cites `\cite{musarraNonlineofsight3DImaging2019}` in the active NLOS hardware table, so this run primarily fixes the missing BibTeX/public README visibility gap rather than adding a new citation site.

The survey build still needs `bare_jrnl.tex` to use all supplement BibTeX files:

```tex
\bibliography{egbib,egbib_2026_updates,egbib_20260701_updates,egbib_20260702_updates,egbib_20260703_updates,egbib_20260704_updates,egbib_20260705_updates}
```

## Website patch still needed

`index.html` was not overwritten in this run because it is a dense hand-maintained HTML/JS file, and a whole-file replacement risks damaging the paper explorer. The exact object to add is:

```js
{cat:'latest active',title:'Non-line-of-sight 3D imaging with a single-pixel camera',authors:'Musarra et al.',year:2019,venue:'arXiv 2019',url:'https://arxiv.org/abs/1903.04812',key:'DMD-based time-resolved single-pixel camera with SPAD/PMT detection for scanning-free, full-color 3D NLOS reconstruction and sub-second Hadamard acquisition.'},
```

Suggested homepage text updates:

- Change `Updated 4 July 2026 · 190+ papers` to `Updated 5 July 2026 · 190+ papers`.
- Change `Last updated: 4 July 2026` to `Last updated: 5 July 2026`.
- Increase the tracked latest-entry count after reconciling all pending homepage objects.
- Insert the object above near the 2019 active optical entries in the `papers` array.

## PDF status

`bare_jrnl.pdf` was **not regenerated** in this run. The available runtime did not provide a safe LaTeX/PDF compilation path or binary GitHub PDF upload path. The remaining manual steps are:

1. Update the bibliography line in `bare_jrnl.tex` as shown above.
2. Compile with LaTeX/BibTeX locally.
3. Upload the regenerated `bare_jrnl.pdf`.
