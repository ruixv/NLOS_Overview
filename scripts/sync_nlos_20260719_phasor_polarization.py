#!/usr/bin/env python3
"""Synchronize citation-traced phasor-diffraction and polarized NLOS papers."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPERS = [
    {
        "title": "Forward and inverse diffraction in phasor fields",
        "authors": "Garcia-Pueyo and Muñoz",
        "year": 2025,
        "venue": "Optics Express 2025",
        "url": "https://doi.org/10.1364/OE.553755",
        "cat": "latest active wave phasor diffraction",
        "key": "garciaPueyoForwardInversePhasor2025",
        "summary": "Recasts phasor-field NLOS reconstruction as an inverse-diffraction problem, derives an explicit Inverse Phasor Fields operator, analyzes when the inverse is well posed, and proposes a diffraction-operator rank metric connected to the Rayleigh resolution criterion.",
    },
    {
        "title": "Time-Gated Polarization for Active Non-Line-of-Sight Imaging",
        "authors": "Pueyo-Ciutad et al.",
        "year": 2024,
        "venue": "SIGGRAPH Asia 2024",
        "url": "https://doi.org/10.1145/3680528.3687575",
        "cat": "latest active polarization transient missing cone",
        "key": "pueyoTimeGatedPolarization2024",
        "summary": "Combines picosecond time-of-flight capture with polarization-aware transport and inversion, using directional information induced by the relay surface to recover hidden features inside the conventional missing cone with fewer relay-wall measurements.",
    },
]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return text.replace(old, new, 1)


def insert_before_once(text: str, marker: str, addition: str, label: str) -> str:
    if addition.strip() in text:
        return text
    return replace_once(text, marker, addition.rstrip() + "\n\n" + marker, label)


def paper_object(paper: dict[str, object]) -> str:
    summary = str(paper["summary"]).replace('"', "'")
    return (
        f'      {{cat:"{paper["cat"]}",title:"{paper["title"]}",authors:"{paper["authors"]}",'
        f'year:{paper["year"]},venue:"{paper["venue"]}",url:"{paper["url"]}",key:"{summary}"}},'
    )


def append_to_timeline_year(text: str, year: int, sentence: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if f'<div class="year">{year}</div>' in line]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one homepage timeline row for {year}, found {len(matches)}")
    line = lines[matches[0]]
    if sentence.strip() not in line:
        closing = "</p></div></div>"
        if closing not in line:
            raise RuntimeError(f"Timeline closing marker missing for {year}")
        lines[matches[0]] = line.replace(closing, " " + sentence.strip() + closing, 1)
    return "".join(lines)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("**Update run: 18 July 2026.**", "**Update run: 19 July 2026.**", 1)

    rows = ""
    for p in PAPERS:
        if f"[{p['title']}]" not in text:
            rows += (
                f"| {p['year']} | [{p['title']}]({p['url']}) - {p['authors']} | "
                f"{p['venue']} | {p['summary']} |\n"
            )
    if rows:
        header = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, header, header + rows, "README latest-additions header")

    polarization_line = (
        "   │     Pueyo-Ciutad et al.: time-gated polarization — picosecond polarimetric transport reduces the missing cone and recovers directionally ambiguous hidden surfaces [SIGGRAPH Asia]\n"
    )
    if "Pueyo-Ciutad et al.: time-gated polarization" not in text:
        anchor = "2024 ── Li et al.: ST-Mamba — state-space temporal modeling and phasor-domain wave supervision for consistent dynamic NLOS video [NeurIPS]\n"
        text = replace_once(text, anchor, anchor + polarization_line, "README 2024 timeline anchor")

    diffraction_line = (
        "   │     Garcia-Pueyo and Muñoz: inverse phasor fields — diffraction-operator conditioning and a rank-based recoverability metric [Optics Express]\n"
    )
    if "Garcia-Pueyo and Muñoz: inverse phasor fields" not in text:
        anchor = "   │     Sultan et al.: optimized NUFFT/SFFT sampling — irregular relay scans and flexible hidden-volume grids at FFT-like cost [arXiv]\n"
        text = replace_once(text, anchor, anchor + diffraction_line, "README 2025 timeline anchor")

    audit = (
        "   |     19 July 2026 phasor/polarization citation trace: inverse-diffraction conditioning and time-gated polarimetric recovery integrated across public, survey, bibliography, and build artifacts\n"
    )
    if "19 July 2026 phasor/polarization citation trace" not in text:
        marker = "   |     18 July 2026 core-citation tracing: forward-citation and modality-expansion audit completed\n"
        text = replace_once(text, marker, audit + marker, "README citation-trace marker")

    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace("Updated 18 July 2026 · 190+ papers", "Updated 19 July 2026 · 190+ papers", 1)
    text = text.replace("Last updated: 18 July 2026", "Last updated: 19 July 2026", 1)

    additions = [paper_object(p) for p in PAPERS if f'title:"{p["title"]}"' not in text]
    if additions:
        text = replace_once(
            text,
            "    const papers=[\n",
            "    const papers=[\n" + "\n".join(additions) + "\n",
            "homepage paper array",
        )

    text = append_to_timeline_year(
        text,
        2024,
        "Time-gated polarization added picosecond directional cues to transient transport, recovering hidden features inside the conventional missing cone.",
    )
    text = append_to_timeline_year(
        text,
        2025,
        "Inverse Phasor Fields reframed virtual-wave reconstruction as inverse diffraction and introduced an operator-rank criterion for conditioning and recoverability.",
    )

    stat = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
    match = stat.search(text)
    if not match:
        raise RuntimeError("Homepage tracked-entry statistic not found")
    count = len(re.findall(r'^\s*\{cat:"[^"]+",title:"', text, flags=re.MULTILINE))
    if int(match.group(2)) != count:
        text = stat.sub(lambda m: m.group(1) + str(count) + m.group(3), text, count=1)

    path.write_text(text, encoding="utf-8")


def update_active() -> None:
    path = ROOT / "article/2active.tex"
    text = path.read_text(encoding="utf-8")

    keys = "garciaPueyoForwardInversePhasor2025,pueyoTimeGatedPolarization2024"
    if "garciaPueyoForwardInversePhasor2025" not in text:
        text = replace_once(
            text,
            ",sunCUDAIrregularRelayNLOS2026}",
            ",sunCUDAIrregularRelayNLOS2026," + keys + "}",
            "active-SPAD table citation tail",
        )

    polarization = r"""\vspace{0.8mm}
\noindent \textbf{Time-gated polarization beyond the missing cone.}
Feature-visibility analysis shows that time of flight alone cannot distinguish all hidden surface positions and orientations, leaving a null or ``missing-cone'' region even when photon timing is ideal. Pueyo-Ciutad~\etal~augmented picosecond transient capture with polarization-resolved measurements and formulated a polarized NLOS transport model whose relay-wall Fresnel response encodes propagation direction~\cite{pueyoTimeGatedPolarization2024}. Their inversion prunes candidate hidden points using this directional information and reconstructs surfaces that LCT, $f$--$k$ migration, and conventional phasor fields cannot observe. Simulated and measured experiments also retain fine detail from a fraction of the relay samples. This work changes polarization from a passive contrast cue or noise filter into an additional active transport dimension that directly improves geometric observability.
"""
    text = insert_before_once(
        text,
        "\\bookmark[dest=\\HyperLocalCurrentHref,level=3]{Wave-based model}",
        polarization,
        "active wave-model marker",
    )

    diffraction = r"""\vspace{0.8mm}
\noindent \textbf{Forward and inverse diffraction in phasor fields.}
Garcia-Pueyo and Mu\~noz revisited the apparent paradox that phasor-field reconstruction solves an inverse hidden-scene problem with a forward Rayleigh--Sommerfeld propagation operator~\cite{garciaPueyoForwardInversePhasor2025}. By exploiting diffraction reciprocity and the unitary structure of the propagation operator, they interpret conventional phasor fields as inverse diffraction and derive an explicit Inverse Phasor Fields formulation. The analysis identifies conditions under which diffraction inversion becomes well posed and introduces a matrix-rank quality metric linked to the Rayleigh lateral-resolution criterion. This contribution shifts the virtual-camera metaphor toward an operator-theoretic account of conditioning, explaining when phasor propagation can recover a hidden scene and how relay aperture, wavelength, and propagation distance govern information loss.
"""
    text = insert_before_once(
        text,
        "\\vspace{0.8mm}\n\\noindent \\textbf{Nonuniform and scaled Fourier sampling.}",
        diffraction,
        "active Fourier-sampling marker",
    )

    path.write_text(text, encoding="utf-8")


def update_master_tex() -> None:
    path = ROOT / "bare_jrnl.tex"
    text = path.read_text(encoding="utf-8")
    comment = "% 19 July 2026 phasor/polarization citation trace integrates inverse-diffraction conditioning and time-gated polarimetric NLOS.\n"
    if comment.strip() not in text:
        text = replace_once(
            text,
            "\\input{article/2active.tex}",
            comment + "\\input{article/2active.tex}",
            "master active-section anchor",
        )
    path.write_text(text, encoding="utf-8")


def update_note() -> None:
    path = ROOT / "updates/2026-07-19-phasor-polarization-citation-trace.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "STATUS: STAGED — source synchronization and PDF rebuild are pending.",
        "STATUS: SYNCHRONIZED — guarded source integration completed; the PDF is committed only after clean-build validation.",
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_active()
    update_master_tex()
    update_note()
    print("Synchronized two verified phasor-diffraction and polarized NLOS papers.")


if __name__ == "__main__":
    main()
