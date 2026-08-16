from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

TITLE = "Non-line-of-sight imaging under white-light illumination: a two-step deep learning approach"
KEY = "zhengWhiteLightTwoStepNLOS2021"
DOI = "10.1364/OE.443127"
URL = f"https://doi.org/{DOI}"
SUMMARY = (
    "Introduces an ordinary-camera white-light NLOS system that embeds a speckle-correlation model in a two-stage DNN: "
    "the first network regularizes scattered-pattern autocorrelation and the second reconstructs the hidden image, providing the direct precursor to later physics-enhanced white-light NLOS learning."
)


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def require(text, needle, label):
    if needle not in text:
        raise RuntimeError(f"Missing anchor for {label}: {needle[:160]}")


# README: add the historical gap to the newly found entries and restore its place in the 2021 trajectory.
readme = read("README.md")
header = "|------|-------|----------------|----------------|\n"
require(readme, header, "README latest table")
if TITLE not in readme:
    row = (
        f"| 2021 | [{TITLE}]({URL}) — Zheng et al. | Optics Express 29(24), 40091–40105 (2021) | {SUMMARY} |\n"
    )
    readme = readme.replace(header, header + row, 1)

if "Zheng et al.: ordinary-camera white-light speckle correlation" not in readme:
    anchor = "2021 ── Nam et al.: real-time diffuse-object NLOS video at 5 fps [Nature Comm.]\n"
    require(readme, anchor, "README 2021 timeline")
    addition = (
        "   │     Zheng et al.: ordinary-camera white-light speckle correlation plus a two-step DNN establishes a broadband learned NLOS branch without coherent illumination [Optics Express]\n"
    )
    readme = readme.replace(anchor, anchor + addition, 1)
write("README.md", readme)


# Canonical V2 corpus used by the 3D graph and paper explorer.
data = read("data/papers-source.html")
anchor = "    const papers=[\n"
require(data, anchor, "canonical paper corpus")
added = 0
if TITLE not in data:
    obj = (
        '      {cat:"latest passive learning white-light speckle correlation ordinary-camera",'
        f'title:"{TITLE}",authors:"Zheng et al.",year:2021,'
        'venue:"Optics Express 29(24), 40091–40105 (2021)",'
        f'url:"{URL}",key:"{SUMMARY}"}},\n'
    )
    data = data.replace(anchor, anchor + obj, 1)
    pat = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    m = pat.search(data)
    if not m:
        raise RuntimeError("Could not locate tracked latest entries counter")
    data = pat.sub(f'<b>{int(m.group(1)) + 1}</b><span>tracked latest entries</span>', data, count=1)
    added = 1

if "white-light speckle correlation and a two-step deep network" not in data:
    pat21 = re.compile(r'(<div class="tl"><div class="year">2021</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)', re.S)
    m21 = pat21.search(data)
    if not m21:
        raise RuntimeError("Could not locate 2021 website timeline")
    sentence = (
        " Zheng et al. combined ordinary-camera white-light speckle correlation and a two-step deep network, first regularizing scattered-pattern autocorrelation and then reconstructing the hidden image; this established the learned broadband speckle branch later revisited with stronger physics-enhanced priors."
    )
    data = data[:m21.start()] + m21.group(1) + m21.group(2) + sentence + m21.group(3) + data[m21.end():]
write("data/papers-source.html", data)


# Passive survey: make the 2021 paper the explicit origin of the white-light learned lineage.
passive = read("article/3passive.tex")
if KEY not in passive:
    anchor = "A complementary steady-state trajectory replaces ultrafast timing with statistical structure in wall speckle. "
    require(passive, anchor, "white-light speckle lineage")
    sentence = (
        "Zheng~\\etal~first demonstrated ordinary-camera NLOS under broadband white-light illumination with a two-step learning strategy: a speckle-correlation model supplies the physical representation, one DNN regularizes the scattered-pattern autocorrelation, and a second DNN maps that representation to the hidden image~\\cite{zhengWhiteLightTwoStepNLOS2021}. This result established the learned white-light speckle branch without requiring coherent illumination. "
    )
    passive = passive.replace(anchor, anchor + sentence, 1)
write("article/3passive.tex", passive)


# Top-level synchronization marker.
tex = read("bare_jrnl.tex")
marker = "% 16 August 2026 citation trace: 2021 white-light two-step deep-learning NLOS precursor synchronized.\n"
if marker not in tex:
    tex = marker + tex
write("bare_jrnl.tex", tex)


# Persistent provenance/update note.
note = ROOT / "updates/2026-08-16-white-light-nlos-precursor.md"
note.write_text(
    """# 16 August 2026 white-light NLOS citation-trace update

## Missing historical precursor integrated

Shanshan Zheng, Meihua Liao, Fei Wang, Wenqi He, Xiang Peng, and Guohai Situ, **Non-line-of-sight imaging under white-light illumination: a two-step deep learning approach**, *Optics Express* 29(24), 40091--40105 (2021), DOI 10.1364/OE.443127.

The paper uses a broadband 400--700 nm white-light source and an ordinary sCMOS camera. It embeds a speckle-correlation model in a two-stage DNN: the first network regularizes the scattered-pattern autocorrelation and the second reconstructs the hidden image. This is the direct methodological precursor to the 2025 Applied Optics physics-enhanced white-light method already represented in the repository, and it is repeatedly cited by later passive/steady-state NLOS work.

## Why it was selected

A fresh forward-citation and successor-lineage pass began from the canonical transient and passive core works (Velten 2012, LCT, f-k migration, phasor-field, computational periscopy, major learned transient methods) and cross-checked recent publisher records against README, the canonical V2 corpus, survey prose and bibliography. The recent 2025 white-light physics-enhanced method, 2025 single-shot ambient-light speckle method, and 2025 scan-free spatial-correlation transient method were already present in the survey. Their references exposed this 2021 paper as the missing origin of the white-light learned-speckle lineage rather than a merely tangential citation.

## Synchronization

The workflow inserts the paper into README, the canonical V2 paper corpus and 2021 timeline, the passive-survey white-light lineage, and the merged bibliography. It then rebuilds `bare_jrnl.pdf` and validates title/key/DOI presence, citation resolution, PDF text, and first/last-page rendering before committing the public artifacts.
""",
    encoding="utf-8",
)

print(f"White-light NLOS precursor integration applied; canonical corpus additions: {added}")
