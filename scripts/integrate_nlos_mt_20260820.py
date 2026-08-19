from pathlib import Path
import re

TITLE = "NLOS-MT: A Hybrid Mamba and Windowed Attention Transformer for Non-Line-of-Sight Imaging"
DOI = "10.1007/978-3-032-31666-0_20"
KEY = "jinNLOSMT2026"
DATE_LONG = "20 August 2026"
DATE_SHORT = "20 Aug 2026"


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


path = Path("README.md")
text = read(path)
text = re.sub(r"\*\*Update run: \d{1,2} August 2026\.\*\*", f"**Update run: {DATE_LONG}.**", text, count=1)
row = (
    "| 2026 | [NLOS-MT: A Hybrid Mamba and Windowed Attention Transformer for Non-Line-of-Sight Imaging]"
    "(https://doi.org/10.1007/978-3-032-31666-0_20) — Jin et al. | ICPR 2026, LNCS 16816, 297–311 "
    "(Springer chapter; first online 3 Aug 2026) | Combines a DeformMamba block for linear-complexity long-range/global "
    "transient modeling and robust denoising with a window-attention U-Net for local contextual refinement, extending learned "
    "active NLOS reconstruction from pure Transformer or pure Mamba designs to a hybrid state-space/attention architecture. |\n"
)
if DOI not in text:
    marker = "|------|-------|----------------|----------------|\n"
    if marker not in text:
        raise RuntimeError("README Latest Additions table marker not found")
    text = text.replace(marker, marker + row, 1)

timeline_line = (
    "   │     Jin et al.: NLOS-MT combines DeformMamba long-range state-space modeling with windowed-attention U-Net local "
    "refinement for active transient reconstruction [ICPR 2026]\n"
)
if "Jin et al.: NLOS-MT combines DeformMamba" not in text:
    marker = (
        "   │     Ling et al.: gradient-coordinated physics-guided training routes conflicting reconstruction, physical-consistency, "
        "and sensor-calibration updates instead of collapsing them into one scalar loss [Symmetry]\n"
    )
    if marker not in text:
        raise RuntimeError("README 2026 learned-method timeline anchor not found")
    text = text.replace(marker, marker + timeline_line, 1)
write(path, text)

path = Path("data/papers-source.html")
text = read(path)
added_paper = TITLE not in text
text = re.sub(r"Updated \d{1,2} August 2026", f"Updated {DATE_LONG}", text)
text = re.sub(r"Last updated: \d{1,2} August 2026", f"Last updated: {DATE_LONG}", text)
if added_paper:
    m = re.search(r'<div class="stat"><b>(\d+)</b><span>tracked latest entries</span></div>', text)
    if not m:
        raise RuntimeError("Website tracked-entry counter not found")
    old = int(m.group(1))
    text = text[:m.start()] + m.group(0).replace(f">{old}<", f">{old + 1}<") + text[m.end():]
    obj = (
        '      {cat:"latest learning active transient mamba transformer state-space reconstruction",'
        'title:"NLOS-MT: A Hybrid Mamba and Windowed Attention Transformer for Non-Line-of-Sight Imaging",'
        'authors:"Jin et al.",year:2026,venue:"ICPR 2026 · LNCS 16816 · 297–311",'
        'url:"https://doi.org/10.1007/978-3-032-31666-0_20",'
        'key:"Hybrid active-transient reconstruction couples a DeformMamba block for efficient long-range dependencies, adaptive shape modeling and denoising with a window-attention U-Net for local context; validated on synthetic and public real NLOS datasets."},\n'
    )
    marker = "    const papers=[\n"
    if marker not in text:
        raise RuntimeError("Canonical V2 papers-array marker not found")
    text = text.replace(marker, marker + obj, 1)
if "NLOS-MT couples linear-complexity Mamba" not in text:
    block_re = re.compile(r'(<div class="tl"><div class="year">2026</div><div class="tl-body">.*?<p>)(.*?)(</p></div></div>)', re.S)
    m = block_re.search(text)
    if not m:
        raise RuntimeError("Website 2026 timeline block not found")
    sentence = (
        " NLOS-MT couples linear-complexity Mamba state-space modeling with windowed Transformer attention, adding a hybrid "
        "global--local learned inverse to the NLOST/TransiT/ST-Mamba trajectory."
    )
    text = text[:m.start(2)] + m.group(2) + sentence + text[m.end(2):]
write(path, text)

path = Path("index.html")
text = read(path)
text = re.sub(r"Updated \d{1,2} Aug 2026", f"Updated {DATE_SHORT}", text)
write(path, text)

path = Path("article/4datadriven.tex")
text = read(path)
if KEY not in text:
    para = r"""
\vspace{0.8mm}
\noindent \textbf{Hybrid state-space and windowed-attention reconstruction.}
Building on the Transformer and state-space branches, Jin~\etal~introduced NLOS-MT at ICPR~2026~\cite{jinNLOSMT2026}. The network first forms an initial hidden intensity representation and then applies a DeformMamba block, where deformable convolution adapts to object shape while Mamba's selective state-space mechanism captures long-range dependencies with linear-complexity sequence modeling. A U-Net equipped with windowed attention subsequently restores local contextual detail. This global--local division complements NLOST's spatio-temporal self-attention, TransiT's transient Transformer, and ST-Mamba's temporal state-space modeling: rather than choosing attention or state-space layers as the dominant backbone, NLOS-MT explicitly combines both for denoising and structural reconstruction, with experiments on synthetic and publicly available real NLOS datasets.

"""
    marker = "\\noindent \\textbf{Graph neural networks.}"
    if marker not in text:
        raise RuntimeError("Survey graph-NLOS anchor not found")
    text = text.replace(marker, para + marker, 1)
write(path, text)

path = Path("egbib_merged_20260711.bib")
text = read(path)
if DOI.casefold() not in text.casefold() and KEY not in text:
    entry = r"""

@inproceedings{jinNLOSMT2026,
  author    = {Jin, Shaohui and Ye, Xiu and Liu, Mengge and Wang, Huimin and Lu, Yang and Liu, Hao and Xu, Mingliang},
  title     = {{NLOS-MT}: A Hybrid Mamba and Windowed Attention Transformer for Non-Line-of-Sight Imaging},
  booktitle = {Pattern Recognition. ICPR 2026},
  series    = {Lecture Notes in Computer Science},
  volume    = {16816},
  pages     = {297--311},
  publisher = {Springer Nature Switzerland},
  address   = {Cham},
  year      = {2027},
  doi       = {10.1007/978-3-032-31666-0_20},
  url       = {https://doi.org/10.1007/978-3-032-31666-0_20},
  note      = {ICPR 2026; first online 3 August 2026}
}
"""
    text = text.rstrip() + entry + "\n"
write(path, text)

path = Path("bare_jrnl.tex")
text = read(path)
text = re.sub(r"through \d{1,2} August 2026\.", f"through {DATE_LONG}.", text, count=1)
write(path, text)

updates = Path("updates")
updates.mkdir(exist_ok=True)
note = updates / "2026-08-20-nlos-mt-icpr.md"
note.write_text(
    "# 20 August 2026 — ICPR NLOS-MT citation-trace update\n\n"
    "Verified missing work: Shaohui Jin, Xiu Ye, Mengge Liu, Huimin Wang, Yang Lu, Hao Liu, and Mingliang Xu, "
    "**NLOS-MT: A Hybrid Mamba and Windowed Attention Transformer for Non-Line-of-Sight Imaging**, ICPR 2026, "
    "LNCS 16816, pp. 297–311, DOI 10.1007/978-3-032-31666-0_20. Springer lists first online as 3 August 2026 "
    "and gives a 2027 citation/copyright year for the LNCS chapter; the repository categorizes it on the 2026 conference timeline.\n\n"
    "The paper is a direct Core-paper citation-trace hit: its references include Velten 2012, O'Toole 2018 LCT, "
    "Lindell 2019 f-k migration, Liu phasor-field work, Neural Transient Fields, NLOST, and ST-Mamba. It combines "
    "DeformMamba long-range/global modeling with windowed-attention U-Net local refinement for active transient NLOS reconstruction.\n\n"
    "Public artifacts updated by the guarded integration: README, canonical V2 paper corpus/timeline, data-driven survey prose, "
    "merged bibliography, survey date, and rebuilt bare_jrnl.pdf.\n",
    encoding="utf-8",
)

assert DOI in read("README.md")
assert DOI in read("data/papers-source.html")
assert KEY in read("article/4datadriven.tex")
assert KEY in read("egbib_merged_20260711.bib")
assert f"through {DATE_LONG}." in read("bare_jrnl.tex")
print("NLOS-MT source integration complete")
