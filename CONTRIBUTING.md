# Contributing to Awesome NLOS Imaging

Thank you for contributing to this NLOS Imaging survey repository!

## How to Add a Paper

1. Fork this repository and create a branch: `git checkout -b add-paper-yourname`
2. Add the paper to the appropriate section in `README_GITHUB.md`
3. Use the following format in the table:

```
| [Paper Title](URL) — First Author et al. | Venue Year | One-sentence key contribution | [Code](URL) |
```

4. Submit a Pull Request with the title: `Add: [Short Paper Title] ([Venue Year])`

## Paper Eligibility

- Peer-reviewed papers in top venues (Nature, Science, IEEE, ACM SIGGRAPH, CVPR, NeurIPS, ICCV, ECCV, AAAI, etc.)
- High-impact arXiv preprints from well-known groups
- Papers with significant methodological contribution to NLOS imaging

## Section Placement

Place papers in the most relevant section:

| If the paper is about... | Place in section |
|--------------------------|-----------------|
| SPAD, streak camera, new hardware | Active NLOS → Hardware |
| ToF / wave-based forward models | Active NLOS → Forward Models |
| Reconstruction algorithms (FBP, LCT, f-k, phasor) | Active NLOS → Reconstruction |
| Passive imaging without controllable source | Passive NLOS |
| End-to-end neural network for NLOS | Deep Learning → End-to-End |
| Physics + deep learning hybrid | Deep Learning → Physics-Guided |
| Transformer / attention for NLOS | Deep Learning → Transformers |
| Mamba / SSM for NLOS | Deep Learning → State-Space Models |
| GNN for NLOS | Deep Learning → Graph Neural Networks |
| Diffusion model for NLOS | Deep Learning → Diffusion Models |
| Neural implicit surface / NeRF for NLOS | Deep Learning → Neural Implicit |
| Real-time / video NLOS reconstruction | Deep Learning → Dynamic NLOS |
| Radar, acoustic, multi-modal | New NLOS Scenes |
| Dataset or rendering tool | Datasets |

## Milestone Papers

For truly landmark papers (Nature/Science tier, or field-defining algorithmic contributions), also add an entry to the **Milestone Timeline** section.

## Code Repositories

When adding code links:
- Prefer official author repositories over third-party reimplementations
- Mark unofficial reimplementations with `[Code (unofficial)]`
- If code is not yet released but announced, use `[Code (coming soon)]`

## Questions

Open an Issue if you are unsure where to place a paper or have other questions.
