# Stereo, long-range, and sparse-model NLOS citation-tracing update — 17 July 2026

This update adds three direct NLOS papers absent from the public repository snapshot.

- Luesia-Lahoz, Cartiel, and Muñoz, *Stereo non-line-of-sight imaging*, The Visual Computer 42, article 148 (2026), DOI `10.1007/s00371-025-04340-7`.
- Zeng et al., *Compact non-line-of-sight imager at long range*, Optics Express 34(9), 16911–16921 (2026), DOI `10.1364/OE.597084`.
- Yang et al., *A model decomposition method for the real-time non-line-of-sight imaging*, iScience 29(6), 115828 (2026), DOI `10.1016/j.isci.2026.115828`.

The first is a forward-citation descendant of phasor-field virtual wave optics and directly addresses missing-cone visibility with two relay apertures. The second extends the Velten/LCT/phasor-field active hardware trajectory to compact daylight kilometer-range operation. The third retains an explicit transient forward model while decomposing sparse non-negative LASSO inversion for GPU-parallel low-latency reconstruction. The PR workflow applies all pending 17 July synchronizers, merges canonical bibliography records, clean-builds the LaTeX survey, renders both PDFs, and rejects undefined or duplicate citations before committing the regenerated binary.
