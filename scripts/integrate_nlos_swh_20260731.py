#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Fast non-line-of-sight imaging with high-resolution and wide field of view using synthetic wavelength holography"
KEY = "willomitzerSyntheticWavelengthNLOS2021"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def insert_after_once(text: str, anchor: str, addition: str, label: str) -> str:
    count = text.count(anchor)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(anchor, anchor + addition, 1)


# README: missing-paper table plus historical milestone placement.
readme = read("README.md")
readme_row = (
    "| 2021 | [Fast non-line-of-sight imaging with high-resolution and wide field of view using synthetic wavelength holography]"
    "(https://doi.org/10.1038/s41467-021-26776-w) — Willomitzer et al. | Nature Communications 12, 6647 (2021) | "
    "Computationally mixes complex optical fields recorded at two nearby wavelengths into a synthetic-wavelength hologram. "
    "The measured system recovers around-corner and through-scattering scenes with sub-millimeter resolution, a nearly hemispheric field of view, "
    "46 ms full-field acquisition, and only a 58×58 mm relay-wall probe. |\n"
)
if TITLE not in readme:
    readme = insert_after_once(
        readme,
        "|------|-------|----------------|----------------|\n",
        readme_row,
        "README latest-additions table",
    )

timeline_anchor = (
    "   │     Peng et al.: NLOS photography — direct high-resolution hidden-view image synthesis from transients [arXiv]\n"
)
timeline_line = (
    "   │     Willomitzer et al.: synthetic-wavelength holography combines two nearby coherent wavelengths for 46-ms, "
    "sub-millimeter NLOS imaging over a nearly hemispheric field of view from a compact relay probe [Nature Communications]\n"
)
if "synthetic-wavelength holography combines two nearby coherent wavelengths" not in readme:
    readme = insert_after_once(readme, timeline_anchor, timeline_line, "README 2021 milestone")
write("README.md", readme)


# Website: searchable paper object, 2021 timeline, and audited entry count.
index = read("index.html")
object_line = (
    '      {cat:"latest active coherent interferometry holography synthetic-wavelength scattering around-corner",'
    'title:"Fast non-line-of-sight imaging with high-resolution and wide field of view using synthetic wavelength holography",'
    'authors:"Willomitzer et al.",year:2021,venue:"Nature Communications 12, 6647",'
    'url:"https://doi.org/10.1038/s41467-021-26776-w",'
    'key:"Synthetic-wavelength holography mixes complex fields at two nearby wavelengths for 46 ms full-field NLOS capture, '
    'sub-millimeter resolution, a nearly hemispheric field of view, and a 58×58 mm relay probe."},\n'
)
if TITLE not in index:
    index = insert_after_once(index, "    const papers=[\n", object_line, "website paper explorer")

if "Synthetic-wavelength holography added a coherent full-field branch" not in index:
    pattern = re.compile(
        r'(<div class="tl"><div class="year">2021</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
        re.DOTALL,
    )
    match = pattern.search(index)
    if not match:
        raise RuntimeError("website 2021 timeline block not found")
    extra = (
        " Synthetic-wavelength holography added a coherent full-field branch: two nearby wavelengths recover a hidden hologram "
        "with sub-millimeter resolution and near-hemispheric angular coverage in 46 ms from a compact relay probe."
    )
    index = index[: match.start(2)] + match.group(2) + extra + index[match.end(2) :]

paper_count = index.count("{cat:")
index, substitutions = re.subn(
    r'<b>\d+</b><span>tracked latest entries</span>',
    f'<b>{paper_count}</b><span>tracked latest entries</span>',
    index,
    count=1,
)
if substitutions != 1:
    raise RuntimeError("website tracked-entry count anchor not found")
write("index.html", index)


# Survey: integrate the final journal milestone into the coherent/interferometric branch.
active = read("article/2active.tex")
old_table_cite = r"\cite{Willomitzer:18,xinTheoryFermatPaths2019,rezaPhasorFieldWaves2019}"
new_table_cite = r"\cite{Willomitzer:18,willomitzerSyntheticWavelengthNLOS2021,xinTheoryFermatPaths2019,rezaPhasorFieldWaves2019}"
if KEY not in active:
    if active.count(old_table_cite) != 1:
        raise RuntimeError("active-method table citation anchor not found uniquely")
    active = active.replace(old_table_cite, new_table_cite, 1)

old_sentence = (
    r"Willomiitzer \etal~utilized lasers with two wavelengths to complete high-resolution NLOS imaging based on "
    r"superheterodyne interferometry (SHI) with a resolution of about $50 \mu m$~\cite{Willomitzer:18}."
)
new_sentences = (
    r"Willomitzer \etal~utilized lasers with two wavelengths to complete high-resolution NLOS imaging based on "
    r"superheterodyne interferometry (SHI) with a resolution of about $50 \mu m$~\cite{Willomitzer:18}. "
    r"Their subsequent full-field system matured this coherent lineage into synthetic wavelength holography (SWH)~"
    r"\cite{willomitzerSyntheticWavelengthNLOS2021}. SWH combines the measured complex fields at two closely spaced "
    r"optical wavelengths into a longer synthetic-wavelength hologram, preserving phase information after diffuse scattering "
    r"without relay-wall raster scanning. The demonstrated system reconstructs around-corner and through-scattering scenes "
    r"with sub-millimeter resolution over a nearly hemispheric angular field of view, records the complete object field in "
    r"46~ms, and probes only a 58-by-58~mm relay region. This result complements transient ToF and phasor-field methods "
    r"by exchanging picosecond timing and large apertures for wavelength diversity and coherent full-field acquisition."
)
if "Their subsequent full-field system matured this coherent lineage" not in active:
    if active.count(old_sentence) != 1:
        raise RuntimeError("interferometry prose anchor not found uniquely")
    active = active.replace(old_sentence, new_sentences, 1)
# Guard against a literal Unicode multiplication sign in TeX sources.
active = active.replace("58×58", "58-by-58")
write("article/2active.tex", active)


# Root survey source records this synchronization pass; section prose is included from article/2active.tex.
main = read("bare_jrnl.tex")
marker = "% 31 July 2026 core-citation trace: synthetic-wavelength holography milestone synchronized across public artifacts.\n"
if marker not in main:
    main = insert_after_once(main, "%% bare_jrnl.tex\n", marker, "bare_jrnl update marker")
write("bare_jrnl.tex", main)


# Persistent provenance note.
note = ROOT / "updates/2026-07-31-synthetic-wavelength-holography.md"
note.write_text(
    """# Synthetic-wavelength holography NLOS milestone — 31 July 2026

A keyword and forward-citation audit of the field-defining active NLOS lineage found one journal milestone absent from README, the website explorer, the survey source, and the merged bibliography:

- **Fast non-line-of-sight imaging with high-resolution and wide field of view using synthetic wavelength holography** — Florian Willomitzer, Prasanna V. Rangarajan, Fengqiang Li, Muralidhar M. Balaji, Marc P. Christensen, and Oliver Cossairt; *Nature Communications* 12, 6647 (2021); DOI `10.1038/s41467-021-26776-w`.

The paper is directly relevant rather than a passing NLOS citation: it experimentally reconstructs around-corner and through-scattering hidden scenes. Its synthetic-wavelength holography formulation mixes complex optical fields at two nearby wavelengths, achieving sub-millimeter resolution, nearly hemispheric angular coverage, 46 ms full-field capture, and a 58×58 mm relay probe. The paper itself situates the method against Velten-style transient reconstruction, LCT, f-k migration, phasor fields, and passive computational periscopy, making it a high-priority core-lineage gap.

This integration updates the README latest-additions table and 2021 milestone, the website paper explorer and timeline, the coherent/interferometric survey discussion and active-method table, the canonical bibliography source, the merged bibliography, and the regenerated PDF. The build workflow verifies one public record per artifact, resolved citations, a matching website count, semantic presence in the PDF, and first/last-page rendering.
""",
    encoding="utf-8",
)

print(f"Integrated {TITLE}; website now contains {paper_count} paper objects.")
