#!/usr/bin/env python3
"""Fail-closed source synchronizer for the 20 July 2026 citation trace."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUPPLEMENT = ROOT / "egbib_20260720_citation_trace_additions.bib"
MASTER_BIB = ROOT / "egbib_merged_20260711.bib"


def read(path: str | Path) -> str:
    return (ROOT / path if isinstance(path, str) else path).read_text(encoding="utf-8")


def write(path: str | Path, text: str) -> None:
    (ROOT / path if isinstance(path, str) else path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def after(text: str, anchor: str, payload: str, label: str) -> str:
    if payload.strip() in text:
        return text
    return replace_once(text, anchor, anchor + payload, label)


def before(text: str, anchor: str, payload: str, label: str) -> str:
    if payload.strip() in text:
        return text
    return replace_once(text, anchor, payload + anchor, label)


def bib_entries(text: str) -> tuple[str, list[str]]:
    first = text.find("@")
    if first < 0:
        return text, []
    prefix, entries, i = text[:first], [], first
    while True:
        at = text.find("@", i)
        if at < 0:
            return prefix, entries
        brace = text.find("{", at)
        if brace < 0:
            raise RuntimeError("Malformed BibTeX")
        depth = 0
        for j in range(brace, len(text)):
            depth += text[j] == "{"
            depth -= text[j] == "}"
            if depth == 0:
                entries.append(text[at : j + 1].strip())
                i = j + 1
                break
        else:
            raise RuntimeError("Unbalanced BibTeX")


def bib_key(entry: str) -> str:
    match = re.match(r"@\w+\s*\{\s*([^,]+),", entry, flags=re.I)
    return match.group(1).strip() if match else ""


def bib_doi(entry: str) -> str:
    match = re.search(r"\bdoi\s*=\s*[\{\"]([^}\"]+)", entry, flags=re.I)
    return match.group(1).strip().lower() if match else ""


def update_readme() -> None:
    text = read("README.md")
    text = text.replace("**Update run: 19 July 2026.**", "**Update run: 20 July 2026.**")
    rows = []
    candidates = [
        ("10.1145/3811281", "| 2026 | [GenPIE: A Time-Resolved Plenoptic Imager](https://doi.org/10.1145/3811281) — Wang et al. | ACM TOG / SIGGRAPH 2026 | Reconstructs time-resolved plenoptic transport from sparse real transient measurements using generative 3D priors, differentiable transient path tracing, and spatially varying sensor-response calibration. It is tightly adjacent transient inverse rendering rather than a conventional around-corner method. |\n"),
        ("10.23919/EUSIPCO63237.2025.11226155", "| 2025 | [Visible Occluders as Opportunistic Apertures for Wide Field of View Non-Line-of-Sight 3D Imaging](https://doi.org/10.23919/EUSIPCO63237.2025.11226155) — Czajkowski, Murray-Bruce | EUSIPCO 2025 | Uses ubiquitous doorway edges as a 180-degree computational aperture and improves passive depth recovery for hidden objects spanning substantial depth extents. |\n"),
        ("10.1038/s41467-024-45397-7", "| 2024 | [Two-edge-resolved three-dimensional non-line-of-sight imaging with an ordinary camera](https://doi.org/10.1038/s41467-024-45397-7) — Czajkowski, Murray-Bruce | Nature Communications 2024 | TERI exploits two perpendicular doorway edges and one ordinary photograph of ceiling penumbrae for calibration-free, full-colour passive 3D reconstruction. |\n"),
        ("10.1364/COSI.2024.CTh5A.4", "| 2024 | [Permutation Transient Attention Encoder for None-Line-of-Sight Imaging](https://doi.org/10.1364/COSI.2024.CTh5A.4) — Yue et al. | Optica Imaging Congress / COSI 2024 | Combines transient-attention blocks and Permute-MLP mixing for efficient, discriminative spatio-temporal feature extraction in learned active-NLOS reconstruction. |\n"),
    ]
    for doi, row in candidates:
        if doi not in text:
            rows.append(row)
    if rows:
        text = after(text, "|------|-------|----------------|----------------|\n", "".join(rows), "README table")
    text = after(text, "   │     Pueyo-Ciutad et al.: time-gated polarization — picosecond polarimetric transport reduces the missing cone and recovers directionally ambiguous hidden surfaces [SIGGRAPH Asia]\n", "   │     Czajkowski and Murray-Bruce: TERI — two doorway edges and one ordinary image enable passive full-colour 3D NLOS [Nature Communications]\n   │     Yue et al.: permutation transient attention — attention and Permute-MLP blocks improve learned transient features [COSI]\n", "README 2024 timeline")
    text = after(text, "   │     Garcia-Pueyo and Muñoz: inverse phasor fields — diffraction-operator conditioning and a rank-based recoverability metric [Optics Express]\n", "   │     Czajkowski and Murray-Bruce: visible occluders as opportunistic apertures — passive wide-FoV 3D recovery for extended-depth scenes [EUSIPCO]\n", "README 2025 timeline")
    text = after(text, "   │     Wang et al.: diffuse-aware attention encoding for passive NLOS through relay-wall diffusion [Optics Express]\n", "   │     Wang et al.: GenPIE — generative geometry priors and differentiable transient transport recover a time-resolved plenoptic representation [SIGGRAPH / ACM TOG]\n", "README 2026 timeline")
    write("README.md", text)


def update_index() -> None:
    text = read("index.html")
    text = text.replace("Updated 19 July 2026 · 190+ papers", "Updated 20 July 2026 · 190+ papers")
    text = text.replace("Last updated 19 July 2026", "Last updated 20 July 2026")
    records = [
        ("10.1038/s41467-024-45397-7", '      {cat:"latest passive ordinary camera doorway edge occluder 3d computational periscopy",title:"Two-edge-resolved three-dimensional non-line-of-sight imaging with an ordinary camera",authors:"Czajkowski, Murray-Bruce",year:2024,venue:"Nature Communications 2024",url:"https://doi.org/10.1038/s41467-024-45397-7",key:"TERI uses two perpendicular doorway edges and one photograph of ceiling penumbrae for calibration-free, full-colour passive 3D NLOS."},\n'),
        ("10.23919/EUSIPCO63237.2025.11226155", '      {cat:"latest passive ordinary camera doorway aperture wide field 3d",title:"Visible Occluders as Opportunistic Apertures for Wide Field of View Non-Line-of-Sight 3D Imaging",authors:"Czajkowski, Murray-Bruce",year:2025,venue:"EUSIPCO 2025",url:"https://doi.org/10.23919/EUSIPCO63237.2025.11226155",key:"Doorway edges act as a 180-degree computational aperture and improve passive depth recovery for extended hidden objects."},\n'),
        ("10.1364/COSI.2024.CTh5A.4", '      {cat:"latest active transient learning attention permute mlp",title:"Permutation Transient Attention Encoder for None-Line-of-Sight Imaging",authors:"Yue et al.",year:2024,venue:"COSI 2024",url:"https://doi.org/10.1364/COSI.2024.CTh5A.4",key:"Transient-attention blocks and Permute-MLP mixing extract discriminative spatio-temporal features for learned NLOS reconstruction."},\n'),
        ("10.1145/3811281", '      {cat:"latest transient plenoptic transport inverse rendering generative prior differentiable adjacent",title:"GenPIE: A Time-Resolved Plenoptic Imager",authors:"Wang et al.",year:2026,venue:"ACM TOG / SIGGRAPH 2026",url:"https://doi.org/10.1145/3811281",key:"Tightly adjacent transient inverse rendering from sparse physical captures, generative 3D priors, differentiable path tracing, and spatially varying response calibration."},\n'),
    ]
    additions = [record for doi, record in records if doi not in text]
    if additions:
        pos = text.rfind("    ];")
        if pos < 0:
            raise RuntimeError("Website paper array terminator missing")
        text = text[:pos] + "".join(additions) + text[pos:]

    def add_timeline(year: int, sentence: str, token: str) -> None:
        nonlocal text
        if token in text:
            return
        pattern = rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)'
        match = re.search(pattern, text, flags=re.S)
        if not match:
            raise RuntimeError(f"Website timeline year {year} missing")
        text = text[:match.start()] + match.group(1) + match.group(2).rstrip() + " " + sentence + match.group(3) + text[match.end():]

    add_timeline(2024, "TERI added ordinary-camera passive 3D recovery from two doorway edges, and permutation transient attention added efficient learned spatio-temporal feature mixing.", "TERI added ordinary-camera")
    add_timeline(2025, "Visible-occluder apertures expanded passive edge-coded imaging toward 180-degree field of view and extended-depth objects.", "Visible-occluder apertures expanded")
    add_timeline(2026, "GenPIE linked sparse transient capture, generative geometry priors, and differentiable plenoptic inverse rendering.", "GenPIE linked sparse transient capture")
    array = re.search(r"const\s+papers\s*=\s*\[(.*?)\n\s*\];", text, flags=re.S)
    if not array:
        raise RuntimeError("Website paper array missing")
    count = len(re.findall(r'\{cat:"', array.group(1)))
    text, n = re.subn(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>', f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>', text, count=1)
    if n != 1:
        raise RuntimeError("Website tracked count missing")
    write("index.html", text)


def update_passive() -> None:
    text = read("article/3passive.tex")
    paragraph = """

\\vspace{0.8mm}
\\noindent \\textbf{Two-edge-resolved ordinary-camera 3D NLOS.}
Czajkowski and Murray-Bruce introduced TERI, which uses the vertical and horizontal edges of a doorway as complementary computational apertures~\\cite{czajkowskiTwoEdgeResolved3DNLOS2024}. A single photograph of ceiling penumbrae supplies azimuth, elevation, and range information for calibration-free full-colour three-dimensional reconstruction. Their later wide-field method treats visible doorway edges as opportunistic apertures and improves passive depth recovery for hidden objects spanning substantial depth extents over an approximately $180^\\circ$ horizontal field of view~\\cite{czajkowskiVisibleOccludersNLOS2025}. This branch moves computational periscopy from two-dimensional transport inversion toward single-shot passive 3D imaging whose aperture is provided by ubiquitous scene geometry.
"""
    if "Two-edge-resolved ordinary-camera 3D NLOS" not in text:
        text = after(text, "This result extends the computational-periscopy trajectory from laboratory-scale conditioning improvements toward long-range passive sensing with inexpensive hardware.\n", paragraph, "passive TERI prose")
    row = "     \\cite{czajkowskiTwoEdgeResolved3DNLOS2024,czajkowskiVisibleOccludersNLOS2025} & Ambient light & Conventional camera & Two perpendicular doorway edges / opportunistic aperture & Full-colour wide-FoV 3D reconstruction\\\\%%%% Table body\n"
    if "Full-colour wide-FoV 3D reconstruction" not in text:
        text = before(text, "     \\cite{rajiMDUNet2026} & Ambient light & Conventional camera & Soft-shadow occlusion with coupled learned 2D/3D decoding & Joint 2D radiosity and 3D occluder reconstruction\\\\%%%% Table body\n", row, "passive table")
    write("article/3passive.tex", text)


def update_learning() -> None:
    text = read("article/4datadriven.tex")
    ptea = """

\\vspace{0.8mm}
\\noindent \\textbf{Permutation transient attention.}
Yue~\\etal~combined transient-attention blocks with Permute-MLP feature mixing to construct an efficient encoder for active NLOS reconstruction~\\cite{yuePermutationTransientAttention2024}. The concise proceedings paper provides a verifiable intermediate step between learnable inverse-kernel attention and later full transient Transformers by focusing specifically on discriminative spatio-temporal measurement features.
"""
    if "Permutation transient attention" not in text:
        text = after(text, "In the learned-reconstruction trajectory, it provides an intermediate step between the shared, task-aware feature embeddings of Chen~\\etal~and later spatial--temporal transformers or adaptive physical-prior networks: physics determines the operator structure, whereas learned kernels and attention determine how measurement evidence is inverted and emphasized.\n", ptea, "learning attention prose")
    genpie = """

\\vspace{0.8mm}
\\noindent \\textbf{Generative time-resolved plenoptic inverse rendering.}
GenPIE extends neural-transient and differentiable-rendering research from recovering one hidden geometry or view toward a continuous time-resolved plenoptic transport representation~\\cite{wangGenPIE2026}. Wang~\\etal~combine sparse measurements from a reconfigurable transient imager with generative three-dimensional priors, differentiable transient path tracing, material and illumination optimization, and a spatially varying temporal kernel for detector and calibration residuals. The recovered transport supports multi-bounce decomposition, time-resolved relighting, and time unwarping. Although not a conventional around-corner method, GenPIE is tightly adjacent to NLOS imaging because it advances the same sparse transient inverse-rendering infrastructure and completes under-observed higher-order transport with learned geometry priors.
"""
    if "Generative time-resolved plenoptic inverse rendering" not in text:
        text = before(text, "Recent works have significantly extended this paradigm of combining physical constraints with deep learning.\n", genpie, "learning GenPIE prose")
    write("article/4datadriven.tex", text)


def merge_bib() -> None:
    prefix, master = bib_entries(read(MASTER_BIB))
    _, extra = bib_entries(read(SUPPLEMENT))
    keys = {bib_key(entry) for entry in master}
    dois = {bib_doi(entry) for entry in master if bib_doi(entry)}
    for entry in extra:
        key, doi = bib_key(entry), bib_doi(entry)
        if key in keys or (doi and doi in dois):
            continue
        master.append(entry)
        keys.add(key)
        if doi:
            dois.add(doi)
    write(MASTER_BIB, prefix.rstrip() + "\n\n" + "\n\n".join(master) + "\n")


def update_wrapper() -> None:
    abstract = read("article/0abstract.tex").replace("A curated list of 150+ NLOS papers", "A curated list of 190+ NLOS papers")
    write("article/0abstract.tex", abstract)
    root = read("bare_jrnl.tex")
    marker = "% 20 July 2026 citation trace integrates two-edge passive 3D NLOS, wide-field opportunistic apertures, permutation transient attention, and GenPIE transient plenoptic inverse rendering.\n"
    if marker not in root:
        root = after(root, "% 19 July 2026 phasor/polarization citation trace integrates inverse-diffraction conditioning and time-gated polarimetric NLOS.\n", marker, "survey marker")
    write("bare_jrnl.tex", root)


def validate() -> None:
    public = {"README": read("README.md"), "website": read("index.html"), "bibliography": read(MASTER_BIB)}
    dois = ["10.1038/s41467-024-45397-7", "10.23919/EUSIPCO63237.2025.11226155", "10.1364/COSI.2024.CTh5A.4", "10.1145/3811281"]
    for doi in dois:
        for label, text in public.items():
            if doi.lower() not in text.lower():
                raise RuntimeError(f"{label} missing {doi}")
        if public["bibliography"].lower().count(doi.lower()) != 1:
            raise RuntimeError(f"bibliography DOI missing or duplicated: {doi}")
    passive, learning = read("article/3passive.tex"), read("article/4datadriven.tex")
    for key in ("czajkowskiTwoEdgeResolved3DNLOS2024", "czajkowskiVisibleOccludersNLOS2025"):
        if key not in passive or key not in public["bibliography"]:
            raise RuntimeError(f"passive survey missing {key}")
    for key in ("yuePermutationTransientAttention2024", "wangGenPIE2026"):
        if key not in learning or key not in public["bibliography"]:
            raise RuntimeError(f"learning survey missing {key}")


if __name__ == "__main__":
    update_readme()
    update_index()
    update_passive()
    update_learning()
    update_wrapper()
    merge_bib()
    validate()
    print("Citation-tracing source synchronization completed and validated.")
