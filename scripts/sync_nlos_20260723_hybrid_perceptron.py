#!/usr/bin/env python3
"""Fail-closed synchronization for the HP-CDT active steady-state NLOS paper."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOI = "10.1016/j.sigpro.2025.110072"
KEY = "liangHybridPerceptronSteadyState2025"
MARKER = "% 23 July 2026 citation trace: HP-CDT active steady-state cross-domain learning integrated."
NOTE = "updates/2026-07-23-hybrid-perceptron-steady-state-audit.md"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return text.replace(old, new, 1)


def integrated() -> bool:
    expected = {
        "README.md": DOI,
        "index.html": DOI,
        "article/4datadriven.tex": KEY,
        "bare_jrnl.tex": MARKER,
    }
    found = {path: needle in read(path) for path, needle in expected.items()}
    if all(found.values()):
        return True
    if any(found.values()):
        missing = [path for path, present in found.items() if not present]
        raise RuntimeError("Partial HP-CDT integration; missing: " + ", ".join(missing))
    return False


def update_readme() -> None:
    text = read("README.md")
    pdc_row = "| 2025 | [High-resolution non-line-of-sight imaging via polarization differential correlography](https://doi.org/10.3788/COL202523.081104) — Liu et al. | Chinese Optics Letters 2025 | Introduces PDC-NLOS, a single-shot steady-state system that encodes hidden objects with independently polarized laser speckles and uses polarization differencing before correlographic phase retrieval. It removes mechanical relay scanning, improves perturbation robustness, and demonstrates millimeter-level resolution with an average reported SSIM of about 0.76. |"
    row = "| 2025 | [A hybrid perceptron with cross-domain transferability towards active steady-state non-line-of-sight imaging](https://doi.org/10.1016/j.sigpro.2025.110072) — Liang et al. | Signal Processing 2025 | Introduces HP-CDT for active steady-state NLOS. Hierarchical pooling and feature fusion combine local CNN and global Transformer perception, while LOS-domain latent representations guide NLOS feature learning; synthetic and measured experiments demonstrate lightweight, high-fidelity 2D hidden-scene reconstruction. |"
    text = replace_once(text, pdc_row, pdc_row + "\n" + row, "README HP-CDT row anchor")

    milestone = "   │     Liu et al.: polarization differential correlography — single-shot polarized speckle encoding removes mechanical scanning and achieves millimeter-scale steady-state NLOS reconstruction [Chinese Optics Letters]"
    addition = "   │     Liang et al.: HP-CDT — LOS latent representations guide a lightweight hybrid CNN--Transformer for active steady-state hidden-image reconstruction [Signal Processing]"
    text = replace_once(text, milestone, milestone + "\n" + addition, "README 2025 HP-CDT milestone")
    write("README.md", text)


def update_index() -> None:
    text = read("index.html")
    text = replace_once(
        text,
        '<b>191</b><span>tracked latest entries</span>',
        '<b>192</b><span>tracked latest entries</span>',
        "homepage tracked-paper count",
    )
    paper = '      {cat:"latest active learning steady-state",title:"A hybrid perceptron with cross-domain transferability towards active steady-state non-line-of-sight imaging",authors:"Liang et al.",year:2025,venue:"Signal Processing 2025",url:"https://doi.org/10.1016/j.sigpro.2025.110072",key:"HP-CDT combines hierarchical pooling and feature fusion with local CNN and global Transformer perception, then transfers LOS-domain latent representations as priors for lightweight, high-fidelity active steady-state hidden-image reconstruction."},'
    text = replace_once(text, "      const papers=[", "      const papers=[\n" + paper, "homepage paper-array anchor")

    pattern = r'(<div class="tl"><div class="year">2025</div>.*?<p>)(.*?)(</p></div></div>)'
    match = re.search(pattern, text, flags=re.S)
    if not match:
        raise RuntimeError("Missing homepage 2025 timeline")
    addition = " Liang et al. transferred LOS latent structure into active steady-state NLOS with HP-CDT, a lightweight hybrid CNN--Transformer that improves hidden-image feature extraction and cross-domain generalization."
    if addition.strip() in match.group(2):
        raise RuntimeError("Homepage HP-CDT timeline text already exists without full integration")
    text = text[:match.start()] + match.group(1) + match.group(2).rstrip() + addition + match.group(3) + text[match.end():]
    write("index.html", text)


def update_survey() -> None:
    text = read("article/4datadriven.tex")
    anchor = "Most of the existed NLOS imaging works based on deep learning used the end-to-end network structure, as reviewed in Tab.~\\ref{tab:deeplearning}. Chen \\etal~used conventional cameras and continuous laser illumination to collect steady-state NLOS imaging data and corresponding hidden scenes~\\cite{chenSteadystateNonLineofSightImaging2019}. After that, a U-Net~\\cite{ronnebergerUnetConvolutionalNetworks2015a}~based network was trained to complete the mapping from the measurement to the corresponding hidden scenes. In \\cite{chenSteadystateNonLineofSightImaging2019}, the loss function was a multi-scale (for different resolutions) $L_2$ loss function."
    paragraph = (
        "\n\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Cross-domain transfer for active steady-state NLOS.}\n"
        "Liang~\\etal~extended learned steady-state reconstruction beyond a direct wall-image-to-hidden-image mapping with HP-CDT~\\cite{liangHybridPerceptronSteadyState2025}. Its hybrid perceptron uses hierarchical pooling and feature fusion to preserve primitive cues, combines convolutional local perception with Transformer-style global correlation modeling, and promotes interactions across feature levels. The cross-domain transfer stage then treats line-of-sight latent representations as structural priors that steer the optimization of NLOS features. Validation on rendered data and a measured active steady-state setup shows that priors learned from the easier LOS domain can reduce the ill-posedness of continuous multi-bounce inversion without requiring a heavy deployment model. This result connects the original U-Net steady-state baseline to later physics--data hybrids by making representation transfer, rather than only network depth, the source of additional hidden-scene information."
    )
    text = replace_once(text, anchor, anchor + paragraph, "HP-CDT survey insertion")
    write("article/4datadriven.tex", text)


def update_master() -> None:
    text = read("bare_jrnl.tex")
    text = replace_once(text, "%% bare_jrnl.tex", "%% bare_jrnl.tex\n" + MARKER, "master survey header")
    if "through 23 July 2026" not in text:
        raise RuntimeError("Unexpected survey coverage date")
    write("bare_jrnl.tex", text)


def update_note() -> None:
    text = read(NOTE)
    text = replace_once(
        text,
        "**Status before automation:** staged; public artifacts and PDF not yet updated.",
        "**Status after source synchronization:** README, website, survey source, and bibliography integrated; PDF rebuild pending validation.",
        "update-note status",
    )
    write(NOTE, text)


def main() -> None:
    if integrated():
        print("HP-CDT is already fully integrated; no source edits required.")
        return
    update_readme()
    update_index()
    update_survey()
    update_master()
    update_note()
    if not integrated():
        raise RuntimeError("HP-CDT integration validation failed")
    print("Synchronized HP-CDT across README, homepage, survey source, and update note.")


if __name__ == "__main__":
    main()
