# 20 August 2026 — passive NLOS citation-lineage integration

Two high-confidence missing passive-NLOS works were synchronized after keyword search and Core-paper / milestone citation tracing:

1. Mingyang Chen et al., **Hyper-NLOS: hyperspectral passive non-line-of-sight imaging**, *Optics Express* 32(20), 34807–34824 (2024), DOI `10.1364/OE.532699`. HFN-Net uses wavelength-resolved relay observations, a hyperspectral full-color autoencoder, and spatial–spectral attention; the work also introduces HS-NLOS.
2. Wenwen Li et al., **Turning rough surfaces into non-line-of-sight cameras**, *Optica* 12(5), 626–634 (2025), DOI `10.1364/OPTICA.544275`. A microscale rough-wall scattering model turns realistic relay roughness into an invertible passive encoding and supports ordinary-camera real-time/high-resolution, wide-FoV, full-color, keyhole, and non-invasive-calibration demonstrations.

The rough-surface paper is especially relevant to forward citation tracing because it sits directly downstream of the classical active-NLOS/light-transport literature and is itself a predecessor of later rough-wall thermal NLOS. Hyper-NLOS closes a different lineage gap between intensity/RGB passive reconstruction and the repository's later hyperspectral band-selection / multispectral-fusion works.

Guarded integration updates README, canonical V2 `data/papers-source.html`, the shell homepage date, `article/3passive.tex`, merged BibTeX, and survey provenance, then rebuilds and validates `bare_jrnl.pdf` before committing public artifacts.
