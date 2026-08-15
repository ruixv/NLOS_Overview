from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Noise-adapted Neural Operator for Robust Non-Line-of-Sight Imaging"
KEY = "wangNoiseAdaptedNeuralOperator2025"
ARXIV = "2508.09655"


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def require(text, needle, label):
    if needle not in text:
        raise RuntimeError(f"Missing anchor for {label}: {needle[:140]}")


# README: add the verified arXiv-only paper, advance the update stamp, and place it in the 2025 learned-method trajectory.
readme = read("README.md")
readme = readme.replace("**Update run: 15 August 2026.**", "**Update run: 16 August 2026.**", 1)
header = "|------|-------|----------------|----------------|\n"
require(readme, header, "README latest table")
if TITLE not in readme:
    row = (
        "| 2025 | [Noise-adapted Neural Operator for Robust Non-Line-of-Sight Imaging](https://arxiv.org/abs/2508.09655) — Wang et al. "
        "| arXiv:2508.09655 [cs.CV], v2 March 2026 | Introduces NANO, a noise-conditioned neural operator for confocal transient NLOS inversion. "
        "The continuous-function-space operator is unfolded from a regularized inverse formulation, adapts its reconstruction kernel to estimated measurement noise, and targets resolution/discretization invariance across sparse or irregular scan grids and photon-starved measurements. No final accepted/published venue was verified in this update. |\n"
    )
    readme = readme.replace(header, header + row, 1)

if "Wang et al.: NANO formulates transient NLOS inversion" not in readme:
    anchor = "2025 ── Shi et al.: fast configurable transient simulation and an open NLOS benchmark [arXiv]\n"
    require(readme, anchor, "README 2025 learned timeline")
    readme = readme.replace(
        anchor,
        anchor
        + "   │     Wang et al.: NANO formulates transient NLOS inversion as a noise-conditioned neural operator in continuous function spaces, targeting discretization invariance across sparse/irregular scan grids and photon-starved measurements [arXiv]\n",
        1,
    )
write("README.md", readme)


# Canonical V2 corpus: the current index.html reads paper metadata from data/papers-source.html.
data = read("data/papers-source.html")
if TITLE not in data:
    obj = (
        '      {cat:"latest learning active transient neural-operator operator-learning physics-guided noise robust sparse-scanning undersampling",'
        'title:"Noise-adapted Neural Operator for Robust Non-Line-of-Sight Imaging",authors:"Wang et al.",year:2025,'
        'venue:"arXiv 2025",url:"https://arxiv.org/abs/2508.09655",'
        'key:"NANO estimates transient noise and conditions a continuous neural operator unfolded from the NLOS inverse problem, improving zero-shot robustness across varying scan resolutions, sparse or irregular illumination grids, and photon-starved measurements on simulated and real data."},\n'
    )
    anchor = "    const papers=[\n"
    require(data, anchor, "paper corpus")
    data = data.replace(anchor, anchor + obj, 1)
    pat = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    m = pat.search(data)
    if not m:
        raise RuntimeError("Could not locate tracked latest entries counter")
    data = pat.sub(f'<b>{int(m.group(1)) + 1}</b><span>tracked latest entries</span>', data, count=1)

if "NANO casts NLOS inversion as a noise-conditioned neural operator" not in data:
    pat = re.compile(r'(<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
    m = pat.search(data)
    if not m:
        raise RuntimeError("Could not locate a 2025 website timeline block")
    sentence = (
        " Wang et al. introduced NANO, which casts NLOS inversion as a noise-conditioned neural operator in continuous function spaces and targets robustness across scan resolution, sparse sampling, and photon-starved transients."
    )
    data = data[:m.start()] + m.group(1) + m.group(2) + sentence + m.group(3) + data[m.end():]
write("data/papers-source.html", data)


# Active-method table: include the neural-operator reconstruction among active transient 3D methods.
active = read("article/2active.tex")
head = active.split("\\bookmark", 1)[0]
if KEY not in head:
    anchor = "gaoLearnedLCT2026"
    require(head, anchor, "active transient method table")
    active = active.replace(anchor, anchor + "," + KEY, 1)
write("article/2active.tex", active)


# Data-driven survey: place NANO alongside hardware/noise-aware and learnable inverse operators.
dd = read("article/4datadriven.tex")
if KEY not in dd:
    anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{SPAD-aware physics-informed cascade learning.}"
    require(dd, anchor, "data-driven physics section")
    para = r"""\vspace{0.8mm}
\noindent \textbf{Noise-conditioned neural operators for transient inversion.}
Wang~\etal~recast confocal transient NLOS reconstruction as learning an inverse operator between continuous function spaces rather than a mapping between fixed-resolution tensors~\cite{wangNoiseAdaptedNeuralOperator2025}. Their Noise-Adapted Neural Operator (NANO) first estimates the noise level of the acquired transient and uses it as a conditioning variable for an operator unfolded from a regularized gradient-flow formulation. Global--local transient lifting then couples large-scale structural information with local ballistic details before volumetric albedo projection. This operator viewpoint targets discretization invariance across different scan densities and irregular or severely down-sampled illumination patterns, while the explicit noise conditioning adapts the inverse kernel to photon-starved and non-stationary measurements. Tests on simulated and measured data therefore extend the trajectory from learnable inverse kernels and LCT-style physical priors toward mesh-independent operator learning for acquisition- and noise-robust NLOS reconstruction. At the time of this survey update, the work is available as arXiv:2508.09655 and no final accepted or published venue could be verified.

"""
    dd = dd.replace(anchor, para + anchor, 1)
write("article/4datadriven.tex", dd)


# Top-level survey synchronization marker.
tex = read("bare_jrnl.tex")
marker = "% 16 August 2026 citation trace: noise-adapted neural-operator NLOS reconstruction synchronized.\n"
if marker not in tex:
    tex = marker + tex
write("bare_jrnl.tex", tex)


# Update note: record citation-trace rationale and venue verification status.
note = ROOT / "updates/2026-08-16-noise-adapted-neural-operator.md"
note.write_text(
    """# 16 August 2026 NLOS citation-trace update: NANO

## Newly integrated paper

Lianfang Wang, Kuilin Qin, Xueying Liu, Huibin Chang, Yong Wang, and Yuping Duan, **Noise-adapted Neural Operator for Robust Non-Line-of-Sight Imaging**, arXiv:2508.09655 [cs.CV], first submitted 13 August 2025 and revised 31 March 2026.

- The paper is directly about confocal transient NLOS reconstruction rather than a passing application of NLOS terminology.
- It explicitly builds from the LCT forward/inverse formulation and compares against physical and learned NLOS reconstruction baselines.
- NANO estimates measurement noise and conditions a neural operator formulated in continuous function spaces, with deep unfolding from a regularized inverse problem.
- The operator formulation targets resolution/discretization invariance, sparse or irregular scanning, and severe photon starvation; experiments include simulated and real NLOS data.
- The arXiv record states that the manuscript has been submitted to IEEE for possible publication. No final accepted/published IEEE journal or conference venue was verified as of this update, so the public artifacts correctly retain **arXiv** as the venue rather than guessing a final publication.

## Repository synchronization

README Latest Additions and the 2025 trajectory, the canonical V2 paper corpus (`data/papers-source.html`), the active-method table, the physics/data-driven survey narrative, merged BibTeX, `bare_jrnl.tex`, and the rebuilt `bare_jrnl.pdf` are synchronized by the integration workflow. The public homepage consumes the canonical paper corpus for Paper Explorer and the 3D graph.
""",
    encoding="utf-8",
)

print("NANO neural-operator NLOS integration applied")
