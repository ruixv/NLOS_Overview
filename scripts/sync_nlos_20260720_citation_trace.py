#!/usr/bin/env python3
"""Guarded synchronization for the 20 July 2026 citation-tracing additions.

The script updates public artifacts only when every expected anchor is unique. It
is deliberately fail-closed: if the repository has drifted, it stops before
writing that file rather than applying an approximate replacement.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUPPLEMENT = "egbib_20260720_citation_trace_additions.bib"
MASTER_BIB = "egbib_merged_20260711.bib"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def insert_after(text: str, anchor: str, payload: str, label: str) -> str:
    if payload.strip() in text:
        return text
    return replace_once(text, anchor, anchor + payload, label)


def insert_before(text: str, anchor: str, payload: str, label: str) -> str:
    if payload.strip() in text:
        return text
    return replace_once(text, anchor, payload + anchor, label)


def split_bib(text: str) -> tuple[str, list[str]]:
    first = text.find("@")
    if first < 0:
        return text, []
    prefix = text[:first]
    entries: list[str] = []
    i = first
    while i < len(text):
        at = text.find("@", i)
        if at < 0:
            break
        brace = text.find("{", at)
        if brace < 0:
            raise RuntimeError("Malformed BibTeX entry")
        depth = 0
        for j in range(brace, len(text)):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    entries.append(text[at : j + 1].strip())
                    i = j + 1
                    break
        else:
            raise RuntimeError("Unbalanced BibTeX entry")
    return prefix, entries


def bib_key(entry: str) -> str:
    match = re.match(r"@\w+\s*\{\s*([^,]+),", entry, flags=re.I)
    return match.group(1).strip() if match else ""


def bib_doi(entry: str) -> str:
    match = re.search(r"\bdoi\s*=\s*[\{\"]([^}\"]+)", entry, flags=re.I)
    return match.group(1).strip().lower() if match else ""


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    text = text.replace("**Update run: 19 July 2026.**", "**Update run: 20 July 2026.**")

    header = "|------|-------|----------------|----------------|\n"
    rows: list[str] = []
    if "10.1145/3811281" not in text:
        rows.append(
            "| 2026 | [GenPIE: A Time-Resolved Plenoptic Imager](https://doi.org/10.1145/3811281) — Wang et al. | ACM TOG / SIGGRAPH 2026 | Reconstructs a continuous time-resolved plenoptic transport representation from sparse real transient measurements by combining a reconfigurable transient camera, generative 3D priors, differentiable transient path tracing, and a spatially varying temporal response model. This is a tightly adjacent transient-imaging and inverse-rendering milestone rather than a conventional around-corner reconstruction paper. |\n"
        )
    if "10.23919/EUSIPCO63237.2025.11226155" not in text:
        rows.append(
            "| 2025 | [Visible Occluders as Opportunistic Apertures for Wide Field of View Non-Line-of-Sight 3D Imaging](https://doi.org/10.23919/EUSIPCO63237.2025.11226155) — Czajkowski, Murray-Bruce | EUSIPCO 2025 | Extends passive edge-resolved computational periscopy from a small set of depth layers to hidden objects with substantial depth extent, using ubiquitous doorway edges as a 180-degree computational aperture for single-photograph 3D recovery. |\n"
        )
    if "10.1038/s41467-024-45397-7" not in text:
        rows.append(
            "| 2024 | [Two-edge-resolved three-dimensional non-line-of-sight imaging with an ordinary camera](https://doi.org/10.1038/s41467-024-45397-7) — Czajkowski, Murray-Bruce | Nature Communications 2024 | Introduces TERI, a calibration-free passive system that exploits two perpendicular doorway edges and a single ordinary photograph of ceiling penumbrae to recover full-colour hidden 3D scenes, with the two edges supplying azimuth and elevation resolution. |\n"
        )
    if "10.1364/COSI.2024.CTh5A.4" not in text:
        rows.append(
            "| 2024 | [Permutation Transient Attention Encoder for None-Line-of-Sight Imaging](https://doi.org/10.1364/COSI.2024.CTh5A.4) — Yue et al. | Optica Imaging Congress / COSI 2024 | Uses transient-attention blocks and Permute-MLP mixing to extract more discriminative spatio-temporal features for learned active-NLOS reconstruction; the title retains the publisher's original ‘None-Line-of-Sight’ spelling. |\n"
        )
    if rows:
        text = insert_after(text, header, "".join(rows), "README latest-additions header")

    text = insert_after(
        text,
        "   │     Pueyo-Ciutad et al.: time-gated polarization — picosecond polarimetric transport reduces the missing cone and recovers directionally ambiguous hidden surfaces [SIGGRAPH Asia]\n",
        "   │     Czajkowski and Murray-Bruce: TERI — two perpendicular doorway edges turn one ordinary photograph into full-colour passive 3D NLOS [Nature Communications]\n"
        "   │     Yue et al.: permutation transient attention — transient-attention blocks and Permute-MLP improve learned transient feature extraction [COSI]\n",
        "README 2024 timeline",
    )
    text = insert_after(
        text,
        "   │     Garcia-Pueyo and Muñoz: inverse phasor fields — diffraction-operator conditioning and a rank-based recoverability metric [Optics Express]\n",
        "   │     Czajkowski and Murray-Bruce: visible occluders as opportunistic apertures — passive doorway-edge imaging expands to wide-FoV scenes with substantial depth extent [EUSIPCO]\n",
        "README 2025 timeline",
    )
    text = insert_after(
        text,
        "   │     Wang et al.: diffuse-aware attention encoding for passive NLOS through relay-wall diffusion [Optics Express]\n",
        "   │     Wang et al.: GenPIE — sparse measured transients, generative geometry priors, and differentiable transport recover time-resolved plenoptic light transport [SIGGRAPH / ACM TOG]\n",
        "README 2026 timeline",
    )
    write(path, text)


def update_index() -> None:
    path = "index.html"
    text = read(path)
    text = text.replace("Updated 19 July 2026 · 190+ papers", "Updated 20 July 2026 · 190+ papers")
    text = text.replace("Last updated 19 July 2026", "Last updated 20 July 2026")

    additions: list[str] = []
    records = [
        (
            "10.1038/s41467-024-45397-7",
            '      {cat:"latest passive ordinary camera occluder doorway edge shadow 3d computational periscopy",title:"Two-edge-resolved three-dimensional non-line-of-sight imaging with an ordinary camera",authors:"Czajkowski, Murray-Bruce",year:2024,venue:"Nature Communications 2024",url:"https://doi.org/10.1038/s41467-024-45397-7",key:"TERI exploits two perpendicular doorway edges and one ordinary photograph of ceiling penumbrae for calibration-free, full-colour passive 3D hidden-scene reconstruction."},\n',
        ),
        (
            "10.23919/EUSIPCO63237.2025.11226155",
            '      {cat:"latest passive ordinary camera occluder doorway aperture wide field of view 3d",title:"Visible Occluders as Opportunistic Apertures for Wide Field of View Non-Line-of-Sight 3D Imaging",authors:"Czajkowski, Murray-Bruce",year:2025,venue:"EUSIPCO 2025",url:"https://doi.org/10.23919/EUSIPCO63237.2025.11226155",key:"Uses ubiquitous visible doorway edges as a 180-degree computational aperture and improves passive depth resolution for objects spanning substantial depth extents."},\n',
        ),
        (
            "10.1364/COSI.2024.CTh5A.4",
            '      {cat:"latest active transient learning attention transformer permute mlp",title:"Permutation Transient Attention Encoder for None-Line-of-Sight Imaging",authors:"Yue et al.",year:2024,venue:"COSI 2024",url:"https://doi.org/10.1364/COSI.2024.CTh5A.4",key:"Transient-attention blocks and Permute-MLP mixing provide efficient, discriminative spatio-temporal feature extraction for learned NLOS reconstruction."},\n',
        ),
        (
            "10.1145/3811281",
            '      {cat:"latest transient imaging plenoptic transport inverse rendering generative prior differentiable renderer adjacent",title:"GenPIE: A Time-Resolved Plenoptic Imager",authors:"Wang et al.",year:2026,venue:"ACM TOG / SIGGRAPH 2026",url:"https://doi.org/10.1145/3811281",key:"A tightly adjacent transient-imaging milestone that combines sparse real measurements, generative 3D priors, differentiable transient path tracing, and spatially varying sensor-response calibration to reconstruct time-resolved plenoptic transport."},\n',
        ),
    ]
    for doi, record in records:
        if doi not in text:
            additions.append(record)
    if additions:
        pos = text.rfind("    ];")
        if pos < 0:
            raise RuntimeError("Website paper-array terminator missing")
        text = text[:pos] + "".join(additions) + text[pos:]

    def timeline(year: int, sentence: str, token: str) -> None:
        nonlocal text
        if token in text:
            return
        pattern = rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)'
        match = re.search(pattern, text, flags=re.S)
        if not match:
            raise RuntimeError(f"Website {year} timeline missing")
        text = (
            text[: match.start()]
            + match.group(1)
            + match.group(2).rstrip()
            + " "
            + sentence
            + match.group(3)
            + text[match.end() :]
        )

    timeline(2024, "TERI used two perpendicular doorway edges and one ordinary photograph for passive full-colour 3D NLOS, while permutation transient attention introduced efficient attention/MLP feature mixing for active transient inversion.", "TERI used two perpendicular doorway edges")
    timeline(2025, "Visible-occluder apertures extended this passive edge-coded branch toward 180-degree field of view and targets with substantial depth extent.", "Visible-occluder apertures extended")
    timeline(2026, "GenPIE connected sparse physical transient capture to generative geometry priors and differentiable time-resolved plenoptic inverse rendering.", "GenPIE connected sparse physical transient capture")

    array = re.search(r"const\s+papers\s*=\s*\[(.*?)\n\s*\];", text, flags=re.S)
    if not array:
        raise RuntimeError("Website paper array missing")
    count = len(re.findall(r'\{cat:"', array.group(1)))
    text, n = re.subn(
        r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',
        f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',
        text,
        count=1,
    )
    if n != 1:
        raise RuntimeError("Website tracked-entry counter missing")
    write(path, text)


def update_passive() -> None:
    path = "article/3passive.tex"
    text = read(path)
    paragraph = """

\\vspace{0.8mm}
\\noindent \\textbf{Two-edge-resolved ordinary-camera 3D NLOS.}
Czajkowski and Murray-Bruce introduced two-edge-resolved imaging (TERI), which uses the vertical and horizontal edges of a doorway as complementary computational apertures~\\cite{czajkowskiTwoEdgeResolved3DNLOS2024}. From a single photograph of ceiling penumbrae, the two perpendicular edges provide azimuthal and elevation discrimination, while an information-orthogonal scene representation supplies range resolution, enabling calibration-free full-colour three-dimensional reconstruction with ordinary hardware. Their subsequent wide-field formulation treats visible doorway edges as opportunistic apertures and improves recovery for hidden objects spanning substantial depth extents over an approximately $180^\\circ$ horizontal field of view~\\cite{czajkowskiVisibleOccludersNLOS2025}. This lineage moves computational periscopy from two-dimensional light-transport inversion toward passive single-shot 3D imaging whose aperture is supplied by ubiquitous scene geometry.
"""
    anchor = "This result extends the computational-periscopy trajectory from laboratory-scale conditioning improvements toward long-range passive sensing with inexpensive hardware.\n"
    if "Two-edge-resolved ordinary-camera 3D NLOS" not in text:
        text = insert_after(text, anchor, paragraph, "passive TERI prose")

    old_row = "     \\cite{rajiMDUNet2026} & Ambient light & Conventional camera & Soft-shadow occlusion with coupled learned 2D/3D decoding & Joint 2D radiosity and 3D occluder reconstruction\\\\%%%% Table body\n"
    new_rows = (
        "     \\cite{czajkowskiTwoEdgeResolved3DNLOS2024,czajkowskiVisibleOccludersNLOS2025} & Ambient light & Conventional camera & Two perpendicular doorway edges / opportunistic aperture & Full-colour wide-FoV 3D reconstruction\\\\%%%% Table body\n"
        + old_row
    )
    if "czajkowskiTwoEdgeResolved3DNLOS2024" not in text:
        text = replace_once(text, old_row, new_rows, "passive table insertion")
    write(path, text)


def update_learning() -> None:
    path = "article/4datadriven.tex"
    text = read(path)
    ptea = """

\\vspace{0.8mm}
\\noindent \\textbf{Permutation transient attention.}
Yue~\\etal~introduced a compact transient encoder that alternates transient-attention blocks with Permute-MLP feature mixing~\\cite{yuePermutationTransientAttention2024}. The design targets discriminative spatio-temporal feature extraction before hidden-scene decoding and provides a lightweight conference-scale bridge between learnable inverse-kernel attention and later full transient Transformers. Although the paper is concise, its final Optica proceedings record makes it a verifiable part of the attention-based active-NLOS trajectory.
"""
    ptea_anchor = "In the learned-reconstruction trajectory, it provides an intermediate step between the shared, task-aware feature embeddings of Chen~\\etal~and later spatial--temporal transformers or adaptive physical-prior networks: physics determines the operator structure, whereas learned kernels and attention determine how measurement evidence is inverted and emphasized.\n"
    if "Permutation transient attention" not in text:
        text = insert_after(text, ptea_anchor, ptea, "learning PTEA prose")

    genpie = """

\\vspace{0.8mm}
\\noindent \\textbf{Generative time-resolved plenoptic inverse rendering.}
GenPIE extends the neural-transient and differentiable-rendering trajectory from recovering one hidden geometry or view toward a continuous time-resolved plenoptic transport representation~\\cite{wangGenPIE2026}. Wang~\\etal~combine a reconfigurable transient imaging system with generative three-dimensional priors, differentiable transient path tracing, material and illumination optimization, and a spatially varying temporal kernel that accounts for detector jitter and optical or calibration residuals. The recovered representation supports multi-bounce decomposition, time-resolved relighting, and time unwarping from sparse real observations. GenPIE is not a conventional around-corner reconstruction method, but it is tightly adjacent to NLOS imaging because it advances the same sparse transient inverse-rendering infrastructure and clarifies how learned geometry priors can complete under-observed higher-order light transport.
"""
    genpie_anchor = "Recent works have significantly extended this paradigm of combining physical constraints with deep learning.\n"
    if "Generative time-resolved plenoptic inverse rendering" not in text:
        text = insert_before(text, genpie_anchor, genpie, "learning GenPIE prose")
    write(path, text)


def update_root_and_abstract() -> None:
    abstract_path = "article/0abstract.tex"
    abstract = read(abstract_path)
    abstract = abstract.replace("A curated list of 150+ NLOS papers", "A curated list of 190+ NLOS papers")
    write(abstract_path, abstract)

    root_path = "bare_jrnl.tex"
    root = read(root_path)
    marker = "% 20 July 2026 citation trace integrates two-edge passive 3D NLOS, wide-field opportunistic apertures, permutation transient attention, and GenPIE transient plenoptic inverse rendering.\n"
    anchor = "% 19 July 2026 phasor/polarization citation trace integrates inverse-diffraction conditioning and time-gated polarimetric NLOS.\n"
    if marker not in root:
        root = insert_after(root, anchor, marker, "bare_jrnl integration marker")
    write(root_path, root)


def merge_bibliography() -> None:
    master = read(MASTER_BIB)
    supplement = read(SUPPLEMENT)
    prefix, master_entries = split_bib(master)
    _, new_entries = split_bib(supplement)
    keys = {bib_key(entry) for entry in master_entries}
    dois = {bib_doi(entry) for entry in master_entries if bib_doi(entry)}
    for entry in new_entries:
        key = bib_key(entry)
        doi = bib_doi(entry)
        if key in keys or (doi and doi in dois):
            continue
        master_entries.append(entry)
        keys.add(key)
        if doi:
            dois.add(doi)
    write(MASTER_BIB, prefix.rstrip() + "\n\n" + "\n\n".join(master_entries) + "\n")


def validate() -> None:
    readme = read("README.md")
    index = read("index.html")
    passive = read("article/3passive.tex")
    learning = read("article/4datadriven.tex")
    bib = read(MASTER_BIB)
    dois = [
        "10.1038/s41467-024-45397-7",
        "10.23919/EUSIPCO63237.2025.11226155",
        "10.1364/COSI.2024.CTh5A.4",
        "10.1145/3811281",
    ]
    for doi in dois:
        for label, content in (("README", readme), ("website", index), ("bibliography", bib)):
            if doi.lower() not in content.lower():
                raise RuntimeError(f"{label} is missing {doi}")
    for key in ("czajkowskiTwoEdgeResolved3DNLOS2024", "czajkowskiVisibleOccludersNLOS2025"):
        if key not in passive or key not in bib:
            raise RuntimeError(f"Passive survey integration missing {key}")
    for key in ("yuePermutationTransientAttention2024", "wangGenPIE2026"):
        if key not in learning or key not in bib:
            raise RuntimeError(f"Learning survey integration missing {key}")
    for doi in dois:
        if bib.lower().count(doi.lower()) != 1:
            raise RuntimeError(f"Bibliography DOI is missing or duplicated: {doi}")


if __name__ == "__main__":
    update_readme()
    update_index()
    update_passive()
    update_learning()
    update_root_and_abstract()
    merge_bibliography()
    validate()
    print("Citation-tracing source synchronization completed and validated.")
