#!/usr/bin/env python3
"""Fail-closed PDC-NLOS synchronization across public and survey artifacts."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOI = "10.3788/COL202523.081104"
KEY = "liuPolarizationDifferentialCorrelography2025"
MARKER = "% 23 July 2026 citation trace: polarization differential correlography NLOS integrated."


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return text.replace(old, new, 1)


def regex_once(text, pattern, repl, label, flags=0):
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return out


def integrated():
    if DOI not in read("README.md"):
        return False
    expected = {
        "README.md": DOI,
        "index.html": DOI,
        "article/2active.tex": KEY,
        "bare_jrnl.tex": MARKER,
    }
    missing = [p for p, s in expected.items() if s not in read(p)]
    if missing:
        raise RuntimeError("Partial PDC-NLOS integration: " + ", ".join(missing))
    return True


def update_readme():
    text = read("README.md")
    text = replace_once(text, "**Update run: 22 July 2026.**", "**Update run: 23 July 2026.**", "README date")
    row = (
        "| 2025 | [High-resolution non-line-of-sight imaging via polarization differential "
        "correlography](https://doi.org/10.3788/COL202523.081104) — Liu et al. | "
        "Chinese Optics Letters 2025 | Introduces PDC-NLOS, a single-shot steady-state system "
        "that encodes hidden objects with independently polarized laser speckles and uses "
        "polarization differencing before correlographic phase retrieval. It removes mechanical "
        "relay scanning, improves perturbation robustness, and demonstrates millimeter-level "
        "resolution with an average reported SSIM of about 0.76. |"
    )
    text = regex_once(
        text,
        r"(?m)^(\|------\|-------\|----------------\|----------------\|\s*)$",
        lambda m: m.group(1) + "\n" + row,
        "README table header",
    )
    anchor = (
        "   │     Zhang et al.: spatial-correlation scan-free NLOS — a 3D blur-kernel model "
        "and correlation resampling recover 2-cm detail at 5 fps from a 16×16 detector "
        "[Optics and Lasers in Engineering]"
    )
    milestone = (
        "   │     Liu et al.: polarization differential correlography — single-shot polarized "
        "speckle encoding removes mechanical scanning and achieves millimeter-scale steady-state "
        "NLOS reconstruction [Chinese Optics Letters]"
    )
    text = replace_once(text, anchor, anchor + "\n" + milestone, "README milestone")
    write("README.md", text)


def update_index():
    text = read("index.html")
    text = replace_once(text, '<b>184</b><span>tracked latest entries</span>', '<b>185</b><span>tracked latest entries</span>', "homepage count")
    text = replace_once(text, "Updated 22 July 2026 · 190+ papers", "Updated 23 July 2026 · 190+ papers", "homepage hero date")
    text = replace_once(text, "Last updated: 22 July 2026", "Last updated: 23 July 2026", "homepage footer date")
    paper = (
        '      {cat:"latest active steady-state polarization speckle correlography single-shot",'
        'title:"High-resolution non-line-of-sight imaging via polarization differential correlography",'
        'authors:"Liu et al.",year:2025,venue:"Chinese Optics Letters 2025",'
        'url:"https://doi.org/10.3788/COL202523.081104",'
        'key:"PDC-NLOS uses independently polarized speckle illumination and polarization differencing '
        'for single-shot steady-state correlographic reconstruction, avoiding mechanical scanning '
        'and demonstrating millimeter-level resolution with an average reported SSIM near 0.76."},'
    )
    text = regex_once(
        text,
        r"(?m)^(\s*const papers=\[\s*)$",
        lambda m: m.group(1) + "\n" + paper,
        "homepage paper array",
    )
    pattern = r'(<div class="tl"><div class="year">2025</div>.*?<p>)(.*?)(</p></div></div>)'
    match = re.search(pattern, text, flags=re.S)
    if not match:
        raise RuntimeError("Missing homepage 2025 timeline")
    if "Polarization differential correlography additionally" in match.group(2):
        raise RuntimeError("PDC-NLOS timeline already exists")
    addition = (
        " Polarization differential correlography additionally replaced mechanical relay scanning "
        "with single-shot polarized-speckle encoding, adding a millimeter-resolution steady-state branch."
    )
    text = text[:match.start()] + match.group(1) + match.group(2).rstrip() + addition + match.group(3) + text[match.end():]
    write("index.html", text)


def update_active():
    text = read("article/2active.tex")
    old = r"\cite{chenSteadystateNonLineofSightImaging2019,vedaldi_imaging_2020,roueinfarNIRRaster2025}"
    new = r"\cite{chenSteadystateNonLineofSightImaging2019,vedaldi_imaging_2020,roueinfarNIRRaster2025,liuPolarizationDifferentialCorrelography2025}"
    text = replace_once(text, old, new, "steady-state table citation")
    anchor = (
        "\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Low-cost NIR steady-state raster scanning.}\n"
        "Roueinfar and Salmanian demonstrated a deliberately simple active NLOS acquisition baseline using a 500~mW, 808~nm laser mounted on a pan--tilt unit to raster scan the relay wall and a conventional NIR camera to record the three-bounce steady-state response~\\cite{roueinfarNIRRaster2025}. Experiments on three hidden targets quantify image error with MSE and RMSE. The method does not recover transient depth or introduce a new inverse operator, but it shows how near-infrared illumination and commodity spatial capture can lower hardware complexity. Although uploaded to arXiv in July 2026, the work had already appeared in the 2025 IEEE International Conference on Electrical Engineering; the survey therefore cites the final conference version."
    )
    paragraph = (
        "\n\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Single-shot polarization differential correlography.}\n"
        "Liu~\\etal~introduced PDC-NLOS, a steady-state active system that illuminates the relay wall with independently polarized laser speckles and forms a polarization-difference correlogram before phase retrieval~\\cite{liuPolarizationDifferentialCorrelography2025}. Polarization modulation replaces repeated mechanical scanning, while differential speckle statistics add redundancy against vibration and coloured perturbations. Experiments on horizontal and vertical stripe targets demonstrate millimeter-level resolution, and the reported average SSIM of about 0.76 improves on the authors' earlier chromato-axial single-shot correlography baseline. This work connects steady-state NLOS, speckle correlation, and polarization coding, providing a low-complexity high-resolution alternative to transient time-of-flight inversion."
    )
    text = replace_once(text, anchor, anchor + paragraph, "steady-state survey paragraph")
    write("article/2active.tex", text)


def update_master():
    text = read("bare_jrnl.tex")
    text = regex_once(text, r"(?m)^%% bare_jrnl\.tex\s*$", "%% bare_jrnl.tex\n" + MARKER, "master header")
    text = replace_once(
        text,
        "extends coverage to include significant advances from 2022 through 22 July 2026",
        "extends coverage to include significant advances from 2022 through 23 July 2026",
        "survey coverage date",
    )
    write("bare_jrnl.tex", text)


def validate():
    expected = {
        "README.md": (DOI, 1),
        "index.html": (DOI, 1),
        "article/2active.tex": (KEY, 2),
        "bare_jrnl.tex": (MARKER, 1),
    }
    for path, (needle, count) in expected.items():
        actual = read(path).count(needle)
        if actual != count:
            raise RuntimeError(f"{path}: expected {count} occurrences of {needle}, found {actual}")
    assert '<b>185</b><span>tracked latest entries</span>' in read("index.html")
    assert "through 23 July 2026" in read("bare_jrnl.tex")
    assert "**Update run: 23 July 2026.**" in read("README.md")


def main():
    if integrated():
        print("PDC-NLOS already fully integrated")
        return
    update_readme()
    update_index()
    update_active()
    update_master()
    validate()
    print("PDC-NLOS synchronized across all source artifacts")


if __name__ == "__main__":
    main()
