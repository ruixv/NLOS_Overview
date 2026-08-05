#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOI = "10.3390/photonics13050440"
KEY = "chenDeepUnfoldingTHzNLOS2026"
TITLE = "Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one anchor, found {count}")
    return text.replace(old, new, 1)


def insert_after(text: str, anchor: str, payload: str, label: str) -> str:
    return replace_once(text, anchor, anchor + payload, label)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    if DOI in text:
        return

    text = replace_once(
        text,
        "**Update run: 3 August 2026.**",
        "**Update run: 5 August 2026.**",
        "README update date",
    )
    row = (
        "| 2026 | [Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar "
        "Non-Line-of-Sight 3D Imaging](https://doi.org/10.3390/photonics13050440) — Chen et al. | "
        "Photonics 13(5), 440 (2026) | Builds a 121 GHz measured sub-THz around-corner imaging platform "
        "and unfolds a FISTA sparse solver around a fast holographic forward/adjoint operator. The model-driven "
        "network suppresses phase-error, aperture-shadowing, and multipath artifacts while reconstructing hidden "
        "3D metal targets with substantially faster inference than iterative baselines. |\n"
    )
    header = "|------|-------|----------------|----------------|\n"
    text = insert_after(text, header, row, "README latest-additions table")

    timeline = (
        "2026 ── Chen et al.: measured 121 GHz holographic imaging and FISTA deep unfolding enable efficient "
        "around-corner THz radar 3D reconstruction [Photonics]\n"
    )
    match = re.search(r"(?m)^2026 ──", text)
    if not match:
        raise RuntimeError("README 2026 timeline anchor not found")
    text = text[: match.start()] + timeline + text[match.start() :]
    write(path, text)


def update_index() -> None:
    path = "index.html"
    text = read(path)
    if DOI in text:
        return

    text = text.replace("Updated 3 August 2026 · 210+ papers", "Updated 5 August 2026 · 210+ papers", 1)
    text = text.replace("Last updated: 3 August 2026", "Last updated: 5 August 2026", 1)
    text = replace_once(
        text,
        '<div class="stat"><b>256</b><span>tracked latest entries</span></div>',
        '<div class="stat"><b>257</b><span>tracked latest entries</span></div>',
        "website explorer count",
    )

    obj = (
        '\n      {cat:"latest modality radar rf thz active learning reconstruction deep-unfolding measured",'
        'title:"Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging",'
        'authors:"Chen et al.",year:2026,venue:"Photonics 13(5), 440",'
        'url:"https://doi.org/10.3390/photonics13050440",'
        'key:"A measured 121 GHz sub-THz platform combines a fast holographic forward/adjoint operator with FISTA-Net deep unfolding, reconstructing hidden 3D metal targets while reducing artifacts and accelerating sparse inversion by roughly two orders of magnitude."},'
    )
    text = insert_after(text, "    const papers=[", obj, "website paper explorer")

    pattern = re.compile(
        r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
        re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise RuntimeError("website 2026 timeline block not found")
    sentence = (
        " Chen et al. additionally combined a measured 121 GHz around-corner radar with a fast holographic "
        "operator and FISTA deep unfolding, extending THz NLOS from mirror-folding reconstruction toward "
        "model-driven learned 3D inversion under phase errors, aperture shadowing, and multipath."
    )
    text = text[: match.start(2)] + match.group(2) + sentence + text[match.end(2) :]
    write(path, text)


def update_survey() -> None:
    path = "article/5newscenes.tex"
    text = read(path)
    if KEY in text:
        return

    anchor = (
        "Terahertz and sub-terahertz waves provide another route to around-obstacle perception. "
        "\\href{https://arxiv.org/abs/2205.05066}{Cui and Trichopoulos} showed that building surfaces can act "
        "as lossy mirrors for sub-THz signals, enabling hidden-object reconstruction by mirror-folding the "
        "propagation geometry around the obstacle. This modality sits between optical and RF NLOS: it has shorter "
        "wavelength and potentially higher spatial resolution than many RF systems, while still interacting with "
        "common environmental surfaces in a way that can be exploited for around-corner imaging.\n"
    )
    addition = (
        "\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Model-driven learned THz reconstruction.}\n"
        "Chen~\\etal~extend this modality from geometric mirror folding to learned sparse 3D inversion with a "
        "measured 121~GHz platform~\\cite{chenDeepUnfoldingTHzNLOS2026}. Their formulation represents near-field "
        "around-corner transport with efficient holographic forward and adjoint operators, then unfolds FISTA into "
        "a fixed-depth network whose step, threshold, and momentum parameters are learned from simulated NLOS "
        "echoes. Measurements of hidden metal letters, a resolution chart, and scissors show that the physics-guided "
        "network suppresses phase-error, aperture-shadowing, and multipath artifacts while avoiding the memory cost "
        "of an explicit large sensing matrix. This work marks a transition in the THz branch from direct geometric "
        "relocation toward interpretable model-driven learning, while retaining coherent measured-data validation.\n"
    )
    text = insert_after(text, anchor, addition, "survey THz subsection")
    write(path, text)

    main = read("bare_jrnl.tex")
    comment = "% 5 August 2026 modality/citation trace: measured THz radar deep unfolding integrated across public artifacts.\n"
    if comment not in main:
        main = insert_after(main, "%% bare_jrnl.tex\n", comment, "bare_jrnl update comment")
        write("bare_jrnl.tex", main)


def bib_entry() -> str:
    return r'''@article{chenDeepUnfoldingTHzNLOS2026,
  author  = {Chen, Kun and Wei, Shunjun and Wang, Mou and Chen, Juran and Han, Bingyu and Li, Jin and Liu, Zhe and Zhang, Xiaoling and Liao, Yi and Gao, Pengcheng and Mi, Xiaolin},
  title   = {Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging},
  journal = {Photonics},
  year    = {2026},
  volume  = {13},
  number  = {5},
  pages   = {440},
  doi     = {10.3390/photonics13050440},
  url     = {https://doi.org/10.3390/photonics13050440}
}
'''


def update_bibliography() -> None:
    canonical = ROOT / "egbib_20260805_thz_deep_unfolding.bib"
    if not canonical.exists():
        canonical.write_text(bib_entry(), encoding="utf-8")

    merged_path = "egbib_merged_20260711.bib"
    merged = read(merged_path)
    if KEY not in merged:
        merged = merged.rstrip() + "\n\n" + bib_entry()
        write(merged_path, merged)

    audit_path = "updates/2026-07-11-bibliography-deduplication.md"
    audit = read(audit_path)
    if "92 source files" not in audit:
        audit = replace_once(audit, "91 source files", "92 source files", "bibliography source count")
        audit = replace_once(audit, "508 case-insensitively unique keys", "509 case-insensitively unique keys", "bibliography unique count")
        audit = replace_once(audit, "Parsed source records: 1028", "Parsed source records: 1030", "bibliography parsed count")
        audit = replace_once(audit, "Case-insensitive duplicate replacements: 520", "Case-insensitive duplicate replacements: 521", "bibliography duplicate count")
        write(audit_path, audit)


def update_note() -> None:
    path = ROOT / "updates/2026-08-05-thz-deep-unfolding-nlos.md"
    if path.exists():
        return
    path.write_text(
        """# 5 August 2026 THz deep-unfolding NLOS update

## Verified addition

- **Learning to See Around Corners: A Deep Unfolding Framework for Terahertz Radar Non-Line-of-Sight 3D Imaging** — Kun Chen, Shunjun Wei, Mou Wang, Juran Chen, Bingyu Han, Jin Li, Zhe Liu, Xiaoling Zhang, Yi Liao, Pengcheng Gao, and Xiaolin Mi; *Photonics* 13(5), 440 (2026); DOI: `10.3390/photonics13050440`.

The publisher record reports submission on 6 March 2026, acceptance on 28 April 2026, and publication on 30 April 2026. The study builds and validates a 121 GHz near-field around-corner radar platform. A fast holographic forward/adjoint operator is embedded in a FISTA-derived deep-unfolding network for sparse hidden-volume reconstruction, with measured results on metal letters, a resolution chart, and scissors.

## Scope and citation-tracing decision

The work is genuinely NLOS imaging rather than generic propagation classification: it reconstructs hidden three-dimensional scattering geometry from coherent wall-reflected radar echoes. It extends the repository's THz lineage from mirror-folding geometry to physics-guided learned inversion and is tightly connected to the radar/RF and learned-reconstruction milestones. The current README and website were searched by exact title, DOI, author/title fragments, and THz/deep-unfolding keywords before insertion; no existing record was found.

## Cross-artifact integration

The paper is placed in README Latest Additions and the 2026 timeline, the website explorer/latest feed and timeline, the Terahertz NLOS Imaging subsection of the survey, a dated canonical BibTeX supplement, the merged bibliography, and the rebuilt survey PDF. The explorer count increases from 256 to 257.
""",
        encoding="utf-8",
    )


def validate_sources() -> None:
    checks = {
        "README.md": [DOI, TITLE],
        "index.html": [DOI, TITLE, ">257<"],
        "article/5newscenes.tex": [KEY, "Model-driven learned THz reconstruction"],
        "bare_jrnl.tex": ["5 August 2026 modality/citation trace"],
        "egbib_20260805_thz_deep_unfolding.bib": [KEY, DOI],
        "egbib_merged_20260711.bib": [KEY, DOI],
    }
    for path, needles in checks.items():
        text = read(path)
        for needle in needles:
            if needle not in text:
                raise RuntimeError(f"{path}: missing {needle}")
    if read("README.md").count(DOI) != 1:
        raise RuntimeError("README DOI is not unique")
    if read("index.html").count(DOI) != 1:
        raise RuntimeError("index DOI is not unique")
    if read("article/5newscenes.tex").count(KEY) != 1:
        raise RuntimeError("survey citation is not unique")
    if read("egbib_merged_20260711.bib").count("@article{" + KEY + ",") != 1:
        raise RuntimeError("merged bibliography key is not unique")


def main() -> int:
    update_readme()
    update_index()
    update_survey()
    update_bibliography()
    update_note()
    validate_sources()
    print("THz deep-unfolding NLOS integration completed and source checks passed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
