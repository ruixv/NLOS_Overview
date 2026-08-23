from pathlib import Path
import re

TITLE = "Influence of some acquisition parameters in non-line-of-sight imaging"
DOI = "10.1117/12.3069294"
KEY = "christnacherAcquisitionParametersNLOS2025"


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one anchor, found {n}")
    return text.replace(old, new, 1)


# README: add the verified final proceedings record and a 2025 timeline node.
readme = read("README.md")
if DOI not in readme:
    row = (
        "| 2025 | [Influence of some acquisition parameters in non-line-of-sight imaging]"
        "(https://doi.org/10.1117/12.3069294) — Christnacher et al. | "
        "Proc. SPIE 13678, Emerging Technologies and Materials for Security and Defence 2025, 136780E | "
        "Systematically studies practical SPAD/transient acquisition choices—including pixel calibration, "
        "exposure time, frame count, camera FOV, and focus—to map the speed–transient-quality trade-off "
        "before f-k, back-projection, or phasor-field reconstruction, complementing algorithm-side acceleration "
        "with acquisition-side optimization. |\n"
    )
    anchor = "|------|-------|----------------|----------------|\n"
    readme = replace_once(readme, anchor, anchor + row, "README latest-additions table")

timeline_line = (
    "   │     Christnacher et al.: acquisition-parameter sensitivity moves real-time NLOS optimization upstream, "
    "quantifying SPAD pixel calibration, exposure, frame count, field of view, and focus before downstream "
    "f-k/back-projection/phasor-field inversion [Proc. SPIE]\n"
)
if "Christnacher et al.: acquisition-parameter sensitivity" not in readme:
    anchor = (
        "2025 ── Chen et al.: hierarchical-NeRF implicit ray carving makes two-bounce shadow reconstruction "
        "more efficient [Optics Express]\n"
    )
    readme = replace_once(readme, anchor, anchor + timeline_line, "README 2025 milestone")
write("README.md", readme)


# V2 homepage wrapper: its public date must agree with the 23-August corpus/survey snapshot.
index = read("index.html")
index = index.replace("Updated 22 Aug 2026", "Updated 23 Aug 2026")
write("index.html", index)


# Canonical V2 paper corpus / explorer / timeline.
corpus = read("data/papers-source.html")
if DOI not in corpus:
    obj = (
        '      {cat:"latest active hardware acquisition spad transient calibration real-time",'
        'title:"Influence of some acquisition parameters in non-line-of-sight imaging",'
        'authors:"Christnacher et al.",year:2025,'
        'venue:"Proc. SPIE 13678, 136780E (2025)",'
        'url:"https://doi.org/10.1117/12.3069294",'
        'key:"Systematically analyzes SPAD/transient acquisition parameters—including pixel calibration, exposure, '
        'frame count, field of view, and focus—to quantify the speed–transient-quality trade-off before downstream '
        'f-k, back-projection, or phasor-field reconstruction."},\n'
    )
    anchor = "    const papers=[\n"
    corpus = replace_once(corpus, anchor, anchor + obj, "canonical paper array")

    tail = (
        "A combined BRDF/Wigner analysis unified scattering- and diffraction-limited passive light-field design "
        "across LWIR and THz wavelengths.</p></div></div>"
    )
    tail2 = (
        "A combined BRDF/Wigner analysis unified scattering- and diffraction-limited passive light-field design "
        "across LWIR and THz wavelengths. Christnacher et al. also shifted real-time optimization upstream into "
        "acquisition design, systematically quantifying how SPAD pixel calibration, exposure, frame count, field "
        "of view, and focus trade transient quality against capture time before f-k, back-projection, or phasor-field "
        "inversion.</p></div></div>"
    )
    corpus = replace_once(corpus, tail, tail2, "V2 2025 timeline")

# Recompute the displayed paper count from the actual canonical array, rather than hard-coding it.
arr_start = corpus.find("    const papers=[")
arr_end = corpus.find("\n    ];", arr_start)
if arr_start < 0 or arr_end < 0:
    raise RuntimeError("could not locate canonical paper array boundaries")
tracked = corpus[arr_start:arr_end].count("{cat:")
corpus, n = re.subn(
    r'(<div class="stat"><b>)\d+(</b><span>tracked latest entries</span>)',
    rf'\g<1>{tracked}\g<2>',
    corpus,
    count=1,
)
if n != 1:
    raise RuntimeError("could not update tracked-entry count")
corpus = corpus.replace("Last updated: 22 August 2026", "Last updated: 23 August 2026")
write("data/papers-source.html", corpus)


# Active survey: make acquisition design part of the SPAD hardware trajectory and method table.
active = read("article/2active.tex")
if KEY not in active:
    cite_anchor = "liTimeMultiplexingNLOS2025,spaettSPADTimingNLOS2026,yangPoissonLowSamplingNLOS2026"
    cite_new = (
        "liTimeMultiplexingNLOS2025,spaettSPADTimingNLOS2026,"
        "christnacherAcquisitionParametersNLOS2025,yangPoissonLowSamplingNLOS2026"
    )
    active = replace_once(active, cite_anchor, cite_new, "active table SPAD citation list")

    paragraph_anchor = (
        "Moreover, SPAD has been widely used in commercial LiDAR systems, and the SPAD array, which can avoid "
        "the mechanical raster scan process, has the potential to save scanning time and realize real-time data "
        "collection for active NLOS imaging.\n"
    )
    insertion = r'''
\vspace{0.8mm}
\noindent \textbf{Acquisition-parameter sensitivity for practical SPAD NLOS.}
Beyond accelerating only the inverse solver, Christnacher \etal~\cite{christnacherAcquisitionParametersNLOS2025} systematically examined the measurement parameters that determine how quickly a usable transient data cube can be collected. Their study considers SPAD-pixel calibration, exposure time, the number of images accumulated per frame, camera field of view, and focus adjustment, and evaluates how these choices trade acquisition time against transient quality and ultimately reconstruction fidelity. Because the downstream examples are framed around established back-projection, $f$-$k$ migration, and phasor-field reconstruction, this work complements later detector-timing calibration~\cite{spaettSPADTimingNLOS2026}: the former asks which acquisition settings should be spent in the first place, while the latter corrects timing-grid errors once SPAD-array data have been captured.

'''
    active = replace_once(active, paragraph_anchor, paragraph_anchor + insertion, "SPAD hardware prose")
write("article/2active.tex", active)


# Canonical merged bibliography; fail closed on partial/duplicate records.
bib = read("egbib_merged_20260711.bib")
key_n = len(re.findall(r"@[A-Za-z]+\{" + re.escape(KEY) + r",", bib, flags=re.I))
doi_n = bib.lower().count(DOI.lower())
if key_n == 0 and doi_n == 0:
    entry = r'''

@inproceedings{christnacherAcquisitionParametersNLOS2025,
  author = {Christnacher, Frank and Laurenzis, Martin and Schertzer, St{\'e}phane and Spaett, Alexander and Redo-Sanchez, Albert and Gutierrez, Diego},
  booktitle = {Emerging Technologies and Materials for Security and Defence 2025},
  doi = {10.1117/12.3069294},
  pages = {136780E},
  publisher = {SPIE},
  series = {Proceedings of SPIE},
  title = {Influence of Some Acquisition Parameters in Non-Line-of-Sight Imaging},
  url = {https://doi.org/10.1117/12.3069294},
  volume = {13678},
  year = {2025}
}
'''
    bib = bib.rstrip() + entry + "\n"
elif key_n != 1 or doi_n != 1:
    raise RuntimeError(f"bibliography has inconsistent existing record: key={key_n}, doi={doi_n}")
write("egbib_merged_20260711.bib", bib)


# Survey provenance.  The public snapshot is already 23 August; this records this citation/acquisition pass.
tex = read("bare_jrnl.tex")
note = (
    "% 23 August 2026 acquisition/citation trace: practical SPAD/transient acquisition-parameter optimization "
    "and V2 public-date consistency synchronized.\n"
)
if note not in tex:
    tex = note + tex
write("bare_jrnl.tex", tex)


# Final source-level assertions.
for path, needle in [
    ("README.md", DOI),
    ("data/papers-source.html", DOI),
    ("article/2active.tex", KEY),
    ("egbib_merged_20260711.bib", DOI),
]:
    if needle not in read(path):
        raise RuntimeError(f"missing {needle} from {path}")
