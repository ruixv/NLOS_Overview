from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPER = {
    "title": "Non-line-of-sight imaging and location determination using deep learning",
    "key": "wangPassiveImagingLocalization2023",
    "year": 2023,
    "authors": "Wang et al.",
    "venue": "Optics and Lasers in Engineering 169, 107701 (2023)",
    "url": "https://doi.org/10.1016/j.optlaseng.2023.107701",
    "doi": "10.1016/j.optlaseng.2023.107701",
    "cat": "passive speckle learned localization reconstruction steady-state semantic",
    "summary": "Uses a single-shot wall-mediated speckle pattern with SPIR-Net to jointly reconstruct hidden-object appearance and estimate object location, adding spatial localization to passive steady-state NLOS without pulsed ToF or time-gated hardware.",
}


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def require(text, needle, label):
    if needle not in text:
        raise RuntimeError(f"Missing anchor for {label}: {needle[:180]}")


# README Latest Additions.
readme = read("README.md")
header = "|------|-------|----------------|----------------|\n"
require(readme, header, "README latest-additions table")
if PAPER["title"] not in readme:
    row = (
        f'| {PAPER["year"]} | [{PAPER["title"]}]({PAPER["url"]}) — {PAPER["authors"]} | '
        f'{PAPER["venue"]} | {PAPER["summary"]} |\n'
    )
    readme = readme.replace(header, header + row, 1)

# README 2023 trajectory.
timeline_sentence = (
    "   │     Wang et al.: SPIR-Net jointly reconstructs hidden appearance and estimates object position "
    "from a single-shot passive speckle pattern, adding learned spatial localization without transient timing [Optics and Lasers in Engineering]\n"
)
if "Wang et al.: SPIR-Net jointly reconstructs hidden appearance" not in readme:
    anchor = (
        "   │     Boger-Lombard, Slobodkin, and Katz established passive acoustic daylight localization "
        "from uncontrolled-noise cross-correlations.\n"
    )
    require(readme, anchor, "README 2023 trajectory")
    readme = readme.replace(anchor, anchor + timeline_sentence, 1)
write("README.md", readme)

# Canonical V2 corpus / Paper Explorer.
data = read("data/papers-source.html")
papers_anchor = "    const papers=[\n"
require(data, papers_anchor, "canonical V2 paper array")
if PAPER["title"] not in data:
    def esc(value):
        return str(value).replace("\\", "\\\\").replace('"', '\\"')
    obj = (
        f'      {{cat:"{esc(PAPER["cat"])}",title:"{esc(PAPER["title"])}",'
        f'authors:"{esc(PAPER["authors"])}",year:{PAPER["year"]},venue:"{esc(PAPER["venue"])}",'
        f'url:"{esc(PAPER["url"])}",key:"{esc(PAPER["summary"])}"}},\n'
    )
    data = data.replace(papers_anchor, papers_anchor + obj, 1)
    count_pat = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    m = count_pat.search(data)
    if not m:
        raise RuntimeError("Could not locate V2 tracked-entry counter")
    data = count_pat.sub(
        f'<b>{int(m.group(1)) + 1}</b><span>tracked latest entries</span>',
        data,
        count=1,
    )

if "SPIR-Net jointly reconstructs passive speckle appearance" not in data:
    year_pat = re.compile(
        r'(<div class="tl"><div class="year">2023</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
        re.S,
    )
    m = year_pat.search(data)
    if not m:
        raise RuntimeError("Could not locate V2 2023 timeline")
    sentence = (
        " Wang et al. added SPIR-Net, which jointly reconstructs passive speckle appearance and estimates "
        "hidden-object position from a single-shot steady-state measurement, extending passive learned NLOS "
        "from recognition/reconstruction toward spatial localization without transient timing."
    )
    data = data[:m.start()] + m.group(1) + m.group(2) + sentence + m.group(3) + data[m.end():]
write("data/papers-source.html", data)

# Passive-method survey prose, placed after room-scale real-time reconstruction.
survey = read("article/3passive.tex")
if PAPER["key"] not in survey:
    anchor = (
        "This work therefore supplies an intermediate step from ordinary-camera passive inversion toward "
        "practical real-time indoor sensing.\n"
    )
    require(survey, anchor, "passive room-scale paragraph")
    paragraph = (
        "\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Joint passive imaging and localization from speckle.}\n"
        "Wang~\\etal~showed that steady-state wall-mediated speckle can encode not only hidden appearance but "
        "also object position~\\cite{wangPassiveImagingLocalization2023}. Their speckle-based position and image "
        "recognition network (SPIR-Net) combines modified LeNet, U-Net, and conditional-GAN components to recover "
        "a hidden image and classify its spatial location from a single-shot CCD speckle measurement. Because the "
        "system does not require a controllable pulsed source or time-gated detector, it introduces a complementary "
        "localization route to transient ToF: position becomes a learned output of the passive scattering pattern. "
        "This work therefore bridges early passive deep reconstruction/recognition and later passive tracking and "
        "semantic sensing by explicitly coupling image recovery with spatial localization.\n"
    )
    survey = survey.replace(anchor, anchor + paragraph, 1)

# Add the work to the passive deep-learning comparison table if the table anchor is present.
if "SPIR-Net" not in survey.split("\\begin{table}", 1)[-1]:
    row_anchor = "\\cite{zhouNonlineofsightImagingPhong2020}"
    idx = survey.find(row_anchor)
    if idx != -1:
        line_end = survey.find("\n", idx)
        if line_end == -1:
            raise RuntimeError("Malformed passive deep-learning table row")
        row = (
            "\\cite{wangPassiveImagingLocalization2023} & SPIR-Net (modified LeNet + U-Net + cGAN) "
            "& Single-shot speckle image & Hidden image + spatial location & Passive steady-state speckle / CCD "
            "& Experimental data\\\\\n"
        )
        survey = survey[:line_end+1] + row + survey[line_end+1:]
write("article/3passive.tex", survey)

# Provenance marker; public snapshot date is already 17 August 2026.
tex = read("bare_jrnl.tex")
marker = "% 17 August 2026 citation/keyword trace: passive speckle joint imaging-and-localization precursor synchronized.\n"
if marker not in tex:
    tex = marker + tex
write("bare_jrnl.tex", tex)

# Persistent audit note.
note = ROOT / "updates/2026-08-17-passive-speckle-localization-gap.md"
note.write_text(
    """# 17 August 2026 passive speckle imaging/localization gap

## Newly verified missing work

Zhiyuan Wang, Huiling Huang, Haoran Li, Ziyang Chen, Jun Han, and Jixiong Pu, **Non-line-of-sight imaging and location determination using deep learning**, *Optics and Lasers in Engineering* 169, article 107701 (2023), DOI `10.1016/j.optlaseng.2023.107701`.

Elsevier's final article record describes a passive NLOS system that takes a single-shot speckle pattern and uses SPIR-Net to reconstruct hidden-object appearance while simultaneously determining object position. The method specifically removes the pulsed-laser and time-gating requirements normally used to obtain location in active transient NLOS. The reported network combines modified LeNet, U-Net, and cGAN components.

## Why it belongs in the survey

This is not a generic scattering-media paper: the experiment is explicitly framed as around-corner/passive NLOS, with light observed after reflection from a rough relay surface and the target hidden from direct view. Its contribution fills a historical gap between early steady-state passive learned reconstruction/recognition and later tracking/action-recognition systems by making spatial location a co-estimated output of the wall-mediated speckle measurement.

The paper was also cited by later learned NLOS reconstruction work, which makes it a useful citation-lineage predecessor even though it was surfaced in this run by exact passive-NLOS/learning search rather than a directly enumerable scholarly forward-citation list.

## Venue decision

Use the final Elsevier publication rather than a preprint label: *Optics and Lasers in Engineering*, volume 169, October 2023, article 107701, DOI `10.1016/j.optlaseng.2023.107701`.

## Cross-artifact integration

The integration workflow adds the work to README Latest Additions and the 2023 trajectory, the canonical V2 `data/papers-source.html` corpus/timeline, and the semantically appropriate passive/deep-learning discussion in `article/3passive.tex`. The verified BibTeX record is merged into `egbib_merged_20260711.bib`, then `bare_jrnl.pdf` is rebuilt and checked for citation resolution, semantic presence, and renderability before the synchronized public artifacts are committed.
""",
    encoding="utf-8",
)
