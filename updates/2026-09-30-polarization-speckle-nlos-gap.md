# Integration note — polarization-speckle NLOS single-pixel imaging

## Verified missing paper

Yijun Zhou, Wenwen Li, Wei Li, Xin Huang, Chen Dai, Zhong-Pei Xiao, Zheng-Ping Li, Feihu Xu, and Jian-Wei Pan, “Non-Line-of-Sight Single-Pixel Imaging Using Polarization Speckle Modulation,” *Physical Review Letters*, 136(14), 143801, 2026. DOI: 10.1103/kd8v-fykm. Published 6 April 2026.

Publisher: https://journals.aps.org/prl/abstract/10.1103/kd8v-fykm

## Why it belongs

This is direct NLOS imaging rather than a peripheral NLOS sensing citation. It introduces polarization as an illumination-encoding degree of freedom: polarization states incident on a rough relay wall generate diverse speckle patterns, and a single-pixel detector measures the returned intensity. The demonstrated system is scanning-free in the conventional spatial sense, reconstructs hidden details through a keyhole with millimeter-scale spatial resolution, and includes non-invasive calibration based on the angular memory effect of polarization speckles.

## Recommended integration

- **README / 2026 timeline:** place under active/computational optical NLOS or a single-pixel / structured-illumination subcategory. Suggested summary: “Polarization-speckle modulation enables scanning-free NLOS single-pixel imaging by using relay-wall polarization-dependent speckle diversity as structured illumination, with non-invasive memory-effect calibration.”
- **Website / Paper Explorer / Latest Additions:** add the same final PRL venue, DOI, authors, and active optical / single-pixel / polarization tags.
- **bare_jrnl.tex:** integrate near active computational/structured-illumination methods rather than learned transient reconstruction. A useful trajectory sentence is: “Beyond spatial and temporal coding, Zhou et al. exploited polarization-dependent speckle diversity on a rough relay wall as structured illumination, enabling scanning-free single-pixel NLOS imaging and introducing polarization as an additional encoding degree of freedom.”
- **Bibliography:** merge the verified entry staged in `egbib_20260930_polarization_speckle_nlos.bib` into the canonical bibliography used by `bare_jrnl.tex`.
- **PDF:** rebuild `bare_jrnl.pdf` after source and bibliography integration and verify the citation resolves.

## Deduplication status

Exact-title and DOI searches of the repository default branch returned no match before staging this update.

## Consistency requirement

Do not leave this paper only in README/website. Once the canonical large files can be safely edited from complete content, integrate it into README, index.html/Paper Explorer, bare_jrnl.tex, the canonical bibliography, and then regenerate bare_jrnl.pdf in one consistency pass.
