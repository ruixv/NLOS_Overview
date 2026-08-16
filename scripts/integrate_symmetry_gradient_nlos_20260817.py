from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPER = {
    "title": "Symmetry-Aware Gradient Coordination for Physics-Guided Non-Line-of-Sight Imaging",
    "key": "lingSymmetryGradientNLOS2026",
    "year": 2026,
    "authors": "Ling et al.",
    "venue": "Symmetry 18(5), 711 (2026)",
    "url": "https://doi.org/10.3390/sym18050711",
    "cat": "latest active transient learned physics-guided low-snr gradient-coordination spad reconstruction",
    "summary": "Treats physics-guided NLOS training as a multi-objective gradient-coordination problem rather than a single weighted scalar loss, combining soft conflict projection, hard physical routing, learnable sensor calibration, and staged optimization for improved low-SNR reconstruction robustness.",
}


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def require(text, needle, label):
    if needle not in text:
        raise RuntimeError(f"Missing anchor for {label}: {needle[:180]}")


# README: add the verified final-venue record and position it in the 2026 learned-reconstruction trajectory.
readme = read("README.md")
header = "|------|-------|----------------|----------------|\n"
require(readme, header, "README latest table")
if PAPER["title"] not in readme:
    row = (
        f'| {PAPER["year"]} | [{PAPER["title"]}]({PAPER["url"]}) — {PAPER["authors"]} | '
        f'{PAPER["venue"]} | {PAPER["summary"]} |\n'
    )
    readme = readme.replace(header, header + row, 1)

if "Ling et al.: gradient-coordinated physics-guided training" not in readme:
    anchor = "   │     Sun et al.: TransVID — diffusion-based spatial-temporal interpolation for dynamic transient video [Optics Express]\n"
    require(readme, anchor, "README 2026 learned-reconstruction timeline")
    addition = (
        "   │     Ling et al.: gradient-coordinated physics-guided training routes conflicting reconstruction, physical-consistency, and sensor-calibration updates instead of collapsing them into one scalar loss [Symmetry]\n"
    )
    readme = readme.replace(anchor, anchor + addition, 1)
write("README.md", readme)


# Canonical V2 paper corpus used by Paper Explorer and the 3-D graph.
data = read("data/papers-source.html")
anchor = "    const papers=[\n"
require(data, anchor, "canonical paper corpus")
if PAPER["title"] not in data:
    def esc(value):
        return str(value).replace("\\", "\\\\").replace('"', '\\"')

    obj = (
        f'      {{cat:"{esc(PAPER["cat"])}",title:"{esc(PAPER["title"])}",'
        f'authors:"{esc(PAPER["authors"])}",year:{PAPER["year"]},venue:"{esc(PAPER["venue"])}",'
        f'url:"{esc(PAPER["url"])}",key:"{esc(PAPER["summary"])}"}},\n'
    )
    data = data.replace(anchor, anchor + obj, 1)
    pat = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    m = pat.search(data)
    if not m:
        raise RuntimeError("Could not locate tracked latest entries counter")
    data = pat.sub(f'<b>{int(m.group(1)) + 1}</b><span>tracked latest entries</span>', data, count=1)

if "gradient-coordinated physics-guided training" not in data:
    pat26 = re.compile(
        r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
        re.S,
    )
    m26 = pat26.search(data)
    if not m26:
        raise RuntimeError("Could not locate 2026 website timeline")
    sentence = (
        " Ling et al. reframed physics-guided low-SNR transient reconstruction as gradient coordination, explicitly routing reconstruction, physical-consistency, and sensor-calibration updates instead of relying only on scalar loss weighting."
    )
    data = data[:m26.start()] + m26.group(1) + m26.group(2) + sentence + m26.group(3) + data[m26.end():]
write("data/papers-source.html", data)


# Survey prose: insert next to learnable physical priors, where the contribution changes how physical constraints enter training.
survey = read("article/4datadriven.tex")
if PAPER["key"] not in survey:
    anchor = (
        "This enables significantly better generalization to diverse scene conditions and varying SNR levels, "
        "addressing the limited generalization capability that has been a persistent challenge for physics-based deep NLOS methods.\n"
    )
    require(survey, anchor, "learnable physical priors paragraph")
    paragraph = (
        "\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Gradient-coordinated physics-guided training.}\n"
        "Ling~\\etal~identify a complementary failure mode of physics-guided learning: heterogeneous reconstruction, measurement-consistency, and sensor-calibration objectives can produce conflicting gradients even when every loss term is physically meaningful~\\cite{lingSymmetryGradientNLOS2026}. Rather than tuning another scalar loss weighting, their framework coordinates the gradient families explicitly through soft conflict projection, protected physical routing, learnable instrument calibration, and staged unfreezing. Evaluated with NLOST-style transient reconstruction under multiple low-SNR conditions, the study shifts physics--data fusion from adding priors to the objective toward governing how competing physical constraints are allowed to update shared parameters; the coordination is used during training and does not require a heavier inference-time reconstruction architecture.\n"
    )
    survey = survey.replace(anchor, anchor + paragraph, 1)
write("article/4datadriven.tex", survey)


# Top-level provenance marker. The public snapshot date is already 17 August 2026.
tex = read("bare_jrnl.tex")
marker = "% 17 August 2026 citation trace: gradient-coordinated physics-guided low-SNR NLOS reconstruction synchronized.\n"
if marker not in tex:
    tex = marker + tex
write("bare_jrnl.tex", tex)


# Persistent update note for future automated audits.
note = ROOT / "updates/2026-08-17-gradient-coordination-citation-trace.md"
note.write_text(
    """# 17 August 2026 gradient-coordination citation-trace update

## Newly verified missing work

Yijun Ling, Wenjin Zhao, Mengjia Zhao, and Jie Yang, **Symmetry-Aware Gradient Coordination for Physics-Guided Non-Line-of-Sight Imaging**, *Symmetry* 18(5), article 711 (2026), DOI `10.3390/sym18050711`.

The paper is direct active transient NLOS reconstruction rather than a generic optimization paper: its experiments use the NLOST-style transient benchmark and physical laser/galvanometer/SPAD measurement setting. The paper cites the modern active NLOS lineage including wave-based f-k migration, phasor-field virtual wave optics, and NLOST, making it a valid forward-citation candidate from the repository's core/milestone seeds.

## Why it is a distinct contribution

Most physics-guided learned reconstruction combines reconstruction, measurement-consistency, noise/statistical, and calibration constraints by summing weighted losses. Ling et al. instead treat their interaction as a gradient-governance problem. The framework combines PCGrad-style soft conflict projection, PhysGuard-style protected physical routing, learnable sensor calibration, and staged unfreezing so a high-magnitude branch does not suppress other physically useful updates in low-SNR reconstruction. This is best placed immediately after the survey's learnable-physical-priors discussion: the trajectory becomes **fixed physical priors -> learnable physical priors -> explicit coordination of competing physical gradients**.

## Venue decision

This is not an arXiv-only record. The verified final publication is *Symmetry*, volume 18, issue 5, article 711 (2026), DOI `10.3390/sym18050711`, with authors Yijun Ling, Wenjin Zhao, Mengjia Zhao, and Jie Yang. Public metadata reports publication on 23 April 2026.

## Cross-artifact integration

The integration workflow adds the paper to README Latest Additions and the 2026 development timeline, the canonical V2 `data/papers-source.html` corpus/timeline, the semantically appropriate learnable-physics section in `article/4datadriven.tex`, and `egbib_merged_20260711.bib`. It then rebuilds `bare_jrnl.pdf` and checks that the title, citation key, DOI, and PDF semantic markers are mutually consistent before committing public artifacts.
""",
    encoding="utf-8",
)
