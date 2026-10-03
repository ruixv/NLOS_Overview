# 2026-10-04 verified gap: multi-surface sub-resolution NLOS

## Paper

Yi Wei, Jinye Miao, Yan Zhao, Taotao Qin, Lianfa Bai, Enlai Guo, and Jing Han, **“Multi-surface sub-resolution non-line-of-sight imaging via transient waveform deposition,”** *Optics Express*, vol. 33, no. 24, pp. 51362–51382, 2025. DOI: 10.1364/OE.579004. PMID: 41414620.

## Why it belongs

This is directly about confocal photon-ToF NLOS reconstruction, not generic NLOS propagation. It targets the resolution loss caused by detector temporal jitter when multiple hidden surfaces are closer than the nominal axial/lateral resolution. The method models surface returns as a Gaussian mixture, uses L1–L2 hybrid-regularized deconvolution to stabilize pulse initialization under Poisson noise/jitter, then a constrained Levenberg–Marquardt decomposition to separate surface-specific histograms before LCT reconstruction. The reported experiment resolves 1 cm separations at a 3 m hidden distance versus nominal axial/lateral discrimination limits of 5.25 cm/9.74 cm, and also tests mutual/scattering occlusion.

## Citation-tracing relevance

The paper explicitly builds its active-NLOS lineage through Velten et al. (2012), O’Toole et al. / LCT (2018), Lindell et al. / f-k migration (2019), and Liu et al. / virtual-wave or phasor-field work, making it a strong forward-citation hit from the repository’s Core-paper seeds rather than a keyword-only candidate.

## Repository gap check

GitHub default-branch code search for the complete title returned no result on 2026-10-04. This paper should therefore be treated as a verified integration gap unless a later canonical edit has added it under a substantially different title.

## Recommended integration

- **README / website timeline:** 2025, Active / transient NLOS; tag as `sub-resolution`, `temporal jitter`, `waveform decomposition`, `multi-surface`, `LCT`.
- **Concise contribution summary:** “Decomposes temporally overlapping multi-surface photon returns before LCT reconstruction, using regularized deconvolution and constrained Gaussian-mixture fitting to achieve 1-cm hidden-surface discrimination despite detector-jitter-limited nominal resolution.”
- **Survey placement:** in the active ToF section near discussions of temporal resolution, detector jitter, IRF/deconvolution, and super-resolution. A useful trajectory sentence is: “Beyond improving reconstruction operators alone, recent work attacks detector-limited resolution at the transient level: Wei et al. decompose overlapping surface-specific photon waveforms before LCT inversion, demonstrating centimeter-scale discrimination below the nominal jitter-limited spatial resolution.”
- **Bibliography:** merge the staged BibTeX below into the canonical bibliography used by `bare_jrnl.tex`.
- **PDF:** rebuild `bare_jrnl.pdf` only after canonical README/website/LaTeX/bibliography integration is complete and verified.

## Reliability note

The canonical README is a large file and the available GitHub fetch returned wrapped/truncated content rather than a safe full editable buffer. Per repository reliability rules, this run did not overwrite README/index/LaTeX/PDF from partial content. This note plus the separate verified BibTeX staging file preserves a safe, precise next integration step.
