#!/usr/bin/env python3
"""Fail-closed integration for the 20 July 2026 core-paper citation follow-up."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUPPLEMENT = ROOT / "egbib_20260720_core_citation_followup.bib"
MASTER_BIB = ROOT / "egbib_merged_20260711.bib"


def read(path: str | Path) -> str:
    p = ROOT / path if isinstance(path, str) else path
    return p.read_text(encoding="utf-8")


def write(path: str | Path, text: str) -> None:
    p = ROOT / path if isinstance(path, str) else path
    p.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {n}")
    return text.replace(old, new, 1)


def after(text: str, anchor: str, payload: str, label: str) -> str:
    if payload.strip() in text:
        return text
    return replace_once(text, anchor, anchor + payload, label)


def before(text: str, anchor: str, payload: str, label: str) -> str:
    if payload.strip() in text:
        return text
    return replace_once(text, anchor, payload + anchor, label)


def split_bib(text: str) -> tuple[str, list[str]]:
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
    m = re.match(r"@\w+\s*\{\s*([^,]+),", entry, flags=re.I)
    return m.group(1).strip() if m else ""


def bib_doi(entry: str) -> str:
    m = re.search(r"\bdoi\s*=\s*[\{\"]([^}\"]+)", entry, flags=re.I)
    return m.group(1).strip().lower() if m else ""


def update_readme() -> None:
    text = read("README.md")
    text = text.replace("**Update run: 19 July 2026.**", "**Update run: 20 July 2026.**")

    rows = [
        ("10.1109/ICCP64821.2025.11143850", "| 2025 | [Zero-Phase Phasor Fields for Non-Line-of-Sight Imaging](https://doi.org/10.1109/ICCP64821.2025.11143850) — Luesia-Lahoz et al. | IEEE ICCP 2025 | Uses zero crossings of the virtual phasor-field phase as a geometry cue, obtaining highly precise hidden depth while retaining the noise robustness of phase-based wave propagation. |\n"),
        ("10.1364/OE.508034", "| 2024 | [Towards a More Accurate Light Transport Model for Non-Line-of-Sight Imaging](https://doi.org/10.1364/OE.508034) — Sultan, Reza, Velten | Optics Express 2024 | Derives a more complete transient transport model that unifies time-of-flight and shadow/occlusion NLOS formulations and exposes approximations made by widely used three-bounce models. |\n"),
        ("10.1364/OE.518466", "| 2024 | [Cohesive Framework for Non-Line-of-Sight Imaging Based on Dirac Notation](https://doi.org/10.1364/OE.518466) — Redo-Sanchez et al. | Optics Express 2024 | Places backprojection, f-k migration, and phasor-field propagation in one operator notation, clarifying their mathematical relationships and the role of Rayleigh–Sommerfeld propagation. |\n"),
    ]
    additions = [row for token, row in rows if token not in text]
    if additions:
        text = after(text, "|------|-------|----------------|----------------|\n", "".join(additions), "README latest table")

    old_vlt = re.compile(r"^\| 2021 \| \[Virtual Light Transport Matrices for Non-Line-Of-Sight Imaging\]\(https://arxiv\.org/abs/2103\.12622\).*?\|$", re.M)
    final_vlt = "| 2021 | [Virtual Light Transport Matrices for Non-Line-of-Sight Imaging](https://openaccess.thecvf.com/content/ICCV2021/html/Marco_Virtual_Light_Transport_Matrices_for_Non-Line-of-Sight_Imaging_ICCV_2021_paper.html) — Marco et al. | ICCV 2021 | Extends phasor-field virtual optics from hidden geometry to a virtual projector-camera transport matrix, enabling hidden-scene relighting and separation of direct and higher-order transport. |"
    if old_vlt.search(text):
        text = old_vlt.sub(final_vlt, text, count=1)
    elif final_vlt not in text:
        raise RuntimeError("README Virtual Light Transport Matrices record missing")

    text = after(
        text,
        "   │     Pueyo-Ciutad et al.: time-gated polarization — picosecond polarimetric transport reduces the missing cone and recovers directionally ambiguous hidden surfaces [SIGGRAPH Asia]\n",
        "   │     Sultan et al.: accurate transport modeling — a unified formulation connects transient ToF and occlusion/shadow NLOS [Optics Express]\n   │     Redo-Sanchez et al.: Dirac-notation framework — backprojection, f-k migration, and phasor fields become comparable operators [Optics Express]\n",
        "README 2024 core-operator timeline",
    )
    text = after(
        text,
        "   │     Garcia-Pueyo and Muñoz: inverse phasor fields — diffraction-operator conditioning and a rank-based recoverability metric [Optics Express]\n",
        "   │     Luesia-Lahoz et al.: zero-phase phasor fields — phase zero crossings provide precise and noise-robust hidden depth [ICCP]\n",
        "README 2025 zero-phase timeline",
    )
    write("README.md", text)


def update_index() -> None:
    text = read("index.html")
    text = text.replace("Updated 19 July 2026 · 190+ papers", "Updated 20 July 2026 · 190+ papers")
    text = text.replace("Last updated 19 July 2026", "Last updated 20 July 2026")

    records = [
        ("10.1109/ICCP64821.2025.11143850", '      {cat:"latest active wave phasor phase depth theory",title:"Zero-Phase Phasor Fields for Non-Line-of-Sight Imaging",authors:"Luesia-Lahoz et al.",year:2025,venue:"IEEE ICCP 2025",url:"https://doi.org/10.1109/ICCP64821.2025.11143850",key:"Zero crossings of virtual phasor-field phase provide a highly precise, noise-robust cue for hidden depth."},\n'),
        ("10.1364/OE.508034", '      {cat:"latest active theory transport model tof shadow occlusion",title:"Towards a More Accurate Light Transport Model for Non-Line-of-Sight Imaging",authors:"Sultan, Reza, Velten",year:2024,venue:"Optics Express 2024",url:"https://doi.org/10.1364/OE.508034",key:"A more complete transport formulation unifies transient time-of-flight and shadow/occlusion NLOS models and audits common approximations."},\n'),
        ("10.1364/OE.518466", '      {cat:"latest active theory operator dirac backprojection phasor fk",title:"Cohesive Framework for Non-Line-of-Sight Imaging Based on Dirac Notation",authors:"Redo-Sanchez et al.",year:2024,venue:"Optics Express 2024",url:"https://doi.org/10.1364/OE.518466",key:"A common operator notation relates backprojection, f-k migration, phasor fields, and Rayleigh-Sommerfeld propagation."},\n'),
    ]
    additions = [record for token, record in records if token not in text]

    old_vlt_pattern = re.compile(r'\s*\{cat:"[^"]*",title:"Virtual Light Transport Matrices for Non-Line-Of-Sight Imaging".*?\},\n')
    final_vlt = '      {cat:"active wave phasor transport relighting",title:"Virtual Light Transport Matrices for Non-Line-Of-Sight Imaging",authors:"Marco et al.",year:2021,venue:"ICCV 2021",url:"https://openaccess.thecvf.com/content/ICCV2021/html/Marco_Virtual_Light_Transport_Matrices_for_Non-Line-of-Sight_Imaging_ICCV_2021_paper.html",key:"Virtual projector-camera transport matrices enable hidden-scene relighting and separation of direct and higher-order light transport."},\n'
    match = old_vlt_pattern.search(text)
    if match:
        text = text[:match.start()] + "\n" + final_vlt + text[match.end():]
    elif "Marco_Virtual_Light_Transport_Matrices" not in text:
        additions.append(final_vlt)

    if additions:
        pos = text.rfind("    ];")
        if pos < 0:
            raise RuntimeError("Website paper-array terminator missing")
        text = text[:pos] + "".join(additions) + text[pos:]

    def timeline(year: int, sentence: str, token: str) -> None:
        nonlocal text
        if token in text:
            return
        p = rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)'
        m = re.search(p, text, flags=re.S)
        if not m:
            raise RuntimeError(f"Website timeline {year} missing")
        text = text[:m.start()] + m.group(1) + m.group(2).rstrip() + " " + sentence + m.group(3) + text[m.end():]

    timeline(2024, "A more accurate transport model unified transient and occlusion formulations, while a Dirac-notation framework related backprojection, f-k migration, and phasor-field operators.", "A more accurate transport model unified")
    timeline(2025, "Zero-phase phasor fields turned virtual-wave phase zero crossings into a precise and noise-robust depth observable.", "Zero-phase phasor fields turned")

    array = re.search(r"const\s+papers\s*=\s*\[(.*?)\n\s*\];", text, flags=re.S)
    if not array:
        raise RuntimeError("Website paper array missing")
    count = len(re.findall(r'\{cat:"', array.group(1)))
    text, n = re.subn(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>', f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>', text, count=1)
    if n != 1:
        raise RuntimeError("Website tracked-entry counter missing")
    write("index.html", text)


def update_active() -> None:
    text = read("article/2active.tex")
    if "luesiaZeroPhasePhasor2025" not in text:
        old = "garciaPueyoForwardInversePhasor2025,pueyoTimeGatedPolarization2024} & Pulsed laser"
        new = "garciaPueyoForwardInversePhasor2025,pueyoTimeGatedPolarization2024,sultanAccurateTransportModel2024,redoSanchezCohesiveDiracNLOS2024,luesiaZeroPhasePhasor2025,marcoVirtualLightTransport2021} & Pulsed laser"
        text = replace_once(text, old, new, "active table citation list")

    prose = r"""
\vspace{0.8mm}
\noindent \textbf{Unified transport and operator formulations.}
Sultan~\etal~revisited the transient image-formation model and derived a more complete light-transport formulation that places time-of-flight and shadow/occlusion NLOS measurements in a shared framework~\cite{sultanAccurateTransportModel2024}. Redo-Sanchez~\etal~then used Dirac notation to express backprojection, $f$--$k$ migration, and phasor-field propagation as related linear operators, clarifying when Rayleigh--Sommerfeld diffraction acts as the virtual-wave propagator and which differences arise from filtering or sampling rather than distinct physical assumptions~\cite{redoSanchezCohesiveDiracNLOS2024}. Together, these works strengthen the theoretical bridge between geometric transient inversion and wave-based reconstruction instead of treating each fast solver as an isolated algorithm.

\vspace{0.8mm}
\noindent \textbf{Zero-phase geometry and virtual transport matrices.}
Luesia-Lahoz~\etal~showed that zero crossings of virtual phasor-field phase provide a direct hidden-depth observable with high precision and substantial robustness to measurement noise~\cite{luesiaZeroPhasePhasor2025}. This phase-geometric cue complements amplitude-based virtual-wave focusing and inverse-diffraction conditioning. In a related expansion of the phasor-field camera, Marco~\etal~constructed virtual light-transport matrices between hidden projector and camera positions, enabling relighting and separation of direct, first-order indirect, and higher-order transport rather than recovering only a static hidden albedo volume~\cite{marcoVirtualLightTransport2021}. The latter work was formally published at ICCV 2021; the repository therefore uses the final conference record rather than its earlier arXiv-only label.

"""
    anchor = "\\vspace{0.8mm}\n\\noindent \\textbf{Two-dimensional Quasi-Fresnel inversion.}\n"
    if "Unified transport and operator formulations" not in text:
        text = before(text, anchor, prose, "active operator-theory insertion")
    write("article/2active.tex", text)


def update_master() -> None:
    text = read("bare_jrnl.tex")
    text = text.replace("through 18 July 2026", "through 20 July 2026")
    marker = "% 20 July 2026 core-paper citation follow-up integrates accurate transport modeling, a cohesive operator framework, zero-phase phasor fields, and the ICCV virtual-transport-matrix record.\n"
    if marker not in text:
        text = after(text, "% 19 July 2026 phasor/polarization citation trace integrates inverse-diffraction conditioning and time-gated polarimetric NLOS.\n", marker, "bare_jrnl coverage marker")
    write("bare_jrnl.tex", text)

    abstract = read("article/0abstract.tex").replace("A curated list of 150+ NLOS papers", "A curated list of 190+ NLOS papers")
    write("article/0abstract.tex", abstract)


def merge_bibliography() -> None:
    prefix, master = split_bib(read(MASTER_BIB))
    _, supplement = split_bib(read(SUPPLEMENT))
    by_key = {bib_key(e).lower(): e for e in master if bib_key(e)}
    dois = {bib_doi(e) for e in master if bib_doi(e)}
    for entry in supplement:
        key = bib_key(entry)
        doi = bib_doi(entry)
        if not key:
            raise RuntimeError("Supplement contains entry without key")
        if key.lower() in by_key:
            continue
        if doi and doi in dois:
            continue
        master.append(entry)
        by_key[key.lower()] = entry
        if doi:
            dois.add(doi)
    write(MASTER_BIB, prefix.rstrip() + "\n\n" + "\n\n".join(master) + "\n")


def validate() -> None:
    expected = {
        "README.md": ["10.1109/ICCP64821.2025.11143850", "10.1364/OE.508034", "10.1364/OE.518466", "ICCV 2021"],
        "index.html": ["10.1109/ICCP64821.2025.11143850", "10.1364/OE.508034", "10.1364/OE.518466", "Marco_Virtual_Light_Transport_Matrices"],
        "article/2active.tex": ["luesiaZeroPhasePhasor2025", "sultanAccurateTransportModel2024", "redoSanchezCohesiveDiracNLOS2024", "marcoVirtualLightTransport2021"],
        "egbib_merged_20260711.bib": ["luesiaZeroPhasePhasor2025", "sultanAccurateTransportModel2024", "redoSanchezCohesiveDiracNLOS2024", "marcoVirtualLightTransport2021"],
        "bare_jrnl.tex": ["through 20 July 2026", "core-paper citation follow-up"],
        "article/0abstract.tex": ["190+ NLOS papers"],
    }
    for path, tokens in expected.items():
        text = read(path)
        missing = [token for token in tokens if token not in text]
        if missing:
            raise RuntimeError(f"{path}: missing {missing}")

    _, entries = split_bib(read(MASTER_BIB))
    keys = [bib_key(e).lower() for e in entries if bib_key(e)]
    if len(keys) != len(set(keys)):
        raise RuntimeError("Duplicate BibTeX keys after merge")
    dois = [bib_doi(e) for e in entries if bib_doi(e)]
    if len(dois) != len(set(dois)):
        raise RuntimeError("Duplicate BibTeX DOIs after merge")


if __name__ == "__main__":
    update_readme()
    update_index()
    update_active()
    update_master()
    merge_bibliography()
    validate()
    print("Core-paper citation follow-up synchronized successfully.")
