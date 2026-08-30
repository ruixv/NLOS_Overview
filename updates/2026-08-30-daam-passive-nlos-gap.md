# 2026-08-30 — DAAM passive NLOS gap

## Verified missing paper

Xuefeng Wang, Xingsu Chen, Miao Xu, Gulnaz Alimjan, and Li Zhao, “Passive non-line-of-sight imaging with diffuse-aware attention-enhanced encoding,” *Optics Express*, vol. 34, no. 14, pp. 26271–26289, 2026. DOI: 10.1364/OE.601398.

Publisher/PubMed metadata confirms final journal publication in July 2026. This is not an arXiv-only item.

## Why it belongs

This is a genuine passive NLOS reconstruction paper. It targets the low-SNR / weak-signal attenuation problem in passive wall-mediated imaging and introduces a diffuse-aware attention module (DAAM) that incorporates two NLOS-specific physical priors: anisotropic angular structure of diffuse reflection and channel-wise SNR disparity. The spatial branch uses deformable convolution; the channel branch combines mean and standard-deviation pooling; a learnable gate fuses them. The module is inserted into a residual-attention encoder and evaluated on NLOS-OT plus real captures.

The paper should be categorized under passive optical NLOS / learned reconstruction / physics-informed attention, not under active transient imaging.

## Repository duplicate check

Repository-wide searches for the exact title, DOI `10.1364/OE.601398`, `DAAM`, and the author/title combination returned no current match. Therefore this is a corpus gap rather than a venue correction or duplicate record.

## Recommended integration

### README.md
Add to Latest Additions and the 2026 passive/learned NLOS timeline with a concise contribution summary such as:

> **Passive NLOS with diffuse-aware attention (Optics Express 2026).** Introduces DAAM, a physics-motivated spatial-channel attention module that uses anisotropic diffuse-reflection structure and channel-wise SNR statistics to preserve weak wall-mediated signals in passive NLOS reconstruction.

Use the final Optics Express venue and DOI link.

### Website / Paper Explorer
Add a canonical paper object with year 2026, venue `Optics Express`, modality `passive optical`, task `reconstruction`, method tags including `deep learning`, `attention`, `physics prior`, and `diffuse reflection`. Include the DOI/publisher URL and the same concise contribution summary.

### Development timeline
Place it after recent passive learned reconstruction / polarization / event-camera / light-transport-modulation works. The trajectory sentence can emphasize:

> Passive NLOS learning is moving from generic encoder-decoder architectures toward modules whose inductive biases explicitly model the directional and SNR structure of diffuse wall transport.

### Survey source
Integrate into the semantically appropriate passive/data-driven section rather than appending to a standalone recent-paper list. Suggested literature-review sentence:

> Recent passive NLOS networks have begun to encode transport-specific priors directly into feature extraction. Wang *et al.* introduced diffuse-aware attention that combines deformable spatial sampling with channel-wise signal-statistics weighting, targeting the anisotropic and low-SNR structure of wall-mediated observations \cite{wangDAAMPassiveNLOS2026}.

If the survey already discusses PAC-Net/NLOS-Track, event-camera passive NLOS, polarization-guided methods, or light-transport modulation, insert this sentence nearby to show the progression toward physics-informed learned encoders.

### Bibliography
Merge the entry from `egbib_20260830_daam_passive_nlos_gap.bib` into the canonical bibliography used by `bare_jrnl.tex`, retaining citation key `wangDAAMPassiveNLOS2026` unless it conflicts with an existing key.

### PDF rebuild and consistency check
After guarded source integration:
1. rebuild `bare_jrnl.pdf` from a clean LaTeX/BibTeX state;
2. verify `wangDAAMPassiveNLOS2026` resolves in `.aux/.bbl`;
3. confirm the paper appears in README, website/Paper Explorer, survey prose, bibliography, and regenerated PDF;
4. confirm DOI `10.1364/OE.601398` appears only once in the canonical bibliography/corpus;
5. do not claim the PDF is current until the binary is successfully regenerated and committed.

## Current-run limitation

The repository’s large public-facing files should not be overwritten from partial/truncated content. This run therefore stages verified BibTeX plus exact insertion guidance rather than risking destructive whole-file replacement.
