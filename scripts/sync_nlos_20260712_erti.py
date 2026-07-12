#!/usr/bin/env python3
"""Synchronize the edge-resolved transient imaging citation-tracing update.

The edits are deliberately marker-based and idempotent so that GitHub Actions can
apply them without replacing large hand-maintained files from a stale snapshot.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Seeing Around Corners with Edge-Resolved Transient Imaging"
KEY = "rappEdgeResolvedTransient2020"
DOI_URL = "https://doi.org/10.1038/s41467-020-19727-4"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label} marker, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    text = read("README.md")
    if TITLE not in text:
        separator = "|------|-------|----------------|----------------|\n"
        row = (
            f"| 2020 | [{TITLE}]({DOI_URL}) — Rapp et al. | Nature Communications 2020 | "
            "Combines a vertical edge occluder with pulsed SPAD transients: differencing adjacent photon-arrival histograms isolates angular wedges and enables 2.5D room-scale reconstruction over a 180° field of view from only 45 illumination positions. |\n"
        )
        text = replace_once(text, separator, separator + row, "README latest-table separator")

    milestone = (
        "2020 ── Rapp et al.: edge-resolved transient imaging — 2.5D room-scale recovery from 45 edge-coded scans [Nature Comm.]\n"
        "   │\n"
    )
    if "2020 ── Rapp et al.: edge-resolved transient imaging" not in text:
        text = replace_once(
            text,
            "2021 ── Nam et al.: real-time diffuse-object NLOS video at 5 fps [Nature Comm.]",
            milestone + "2021 ── Nam et al.: real-time diffuse-object NLOS video at 5 fps [Nature Comm.]",
            "README 2021 milestone",
        )

    if text.count(TITLE) != 1:
        raise RuntimeError(f"README should contain one full-title entry, found {text.count(TITLE)}")
    write("README.md", text)


def update_homepage() -> None:
    text = read("index.html")
    if '<b>86</b><span>tracked latest entries</span>' in text:
        text = text.replace(
            '<b>86</b><span>tracked latest entries</span>',
            '<b>87</b><span>tracked latest entries</span>',
            1,
        )
    elif '<b>87</b><span>tracked latest entries</span>' not in text:
        raise RuntimeError("Homepage tracked-entry count is neither 86 nor 87")

    if TITLE not in text:
        object_line = (
            '      {cat:"latest active",title:"Seeing Around Corners with Edge-Resolved Transient Imaging",'
            'authors:"Rapp et al.",year:2020,venue:"Nature Communications 2020",'
            'url:"https://doi.org/10.1038/s41467-020-19727-4",'
            'key:"Edge-resolved transient imaging combines a vertical occluder with pulsed SPAD measurements; differencing adjacent scans isolates angular wedges and enables 2.5D room-scale reconstruction over a 180° field of view from 45 illumination positions."},\n'
        )
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + object_line, "homepage paper-array")

    timeline = (
        '      <div class="tl"><div class="year">2020</div><div class="tl-body"><strong>Edge-resolved transient imaging</strong><p>Rapp et al. combined pulsed single-photon transients with vertical-edge occlusion coding, recovering 2.5D room layouts over a 180° field of view from a 1.5 cm illumination arc and only 45 scan positions.</p></div></div>\n'
    )
    if '<div class="year">2020</div><div class="tl-body"><strong>Edge-resolved transient imaging</strong>' not in text:
        marker = '      <div class="tl"><div class="year">2021</div>'
        text = replace_once(text, marker, timeline + marker, "homepage 2021 timeline")

    if text.count(TITLE) != 1:
        raise RuntimeError(f"Homepage should contain one full-title entry, found {text.count(TITLE)}")
    if '<b>87</b><span>tracked latest entries</span>' not in text:
        raise RuntimeError("Homepage count did not update to 87")
    write("index.html", text)


def update_survey() -> None:
    text = read("article/2active.tex")
    if f"\\cite{{{KEY}}}" not in text:
        paragraph = r"""
\vspace{0.8mm}
\noindent \textbf{Edge-resolved transient imaging.}
Rapp~\etal~combined active transient sensing with a ubiquitous vertical edge occluder~\cite{rappEdgeResolvedTransient2020}. A pulsed laser scans a short semicircular arc around the edge while a gated SPAD records photon-arrival histograms; differencing adjacent histograms suppresses the approximately static visible-scene and background terms and isolates the response of successive angular wedges. The resulting edge-resolved transient measurements provide range from time of flight and azimuth from occlusion coding, enabling a 2.5D plan-view-plus-height reconstruction over a $180^\circ$ field of view from only 45 illumination positions. This hybrid of active ToF sensing and corner-camera occlusion substantially reduces the aperture and number of measurements required for room-scale hidden-scene recovery.

"""
        marker = "\\vspace{0.8mm}\n\\noindent \\textbf{Recent SPAD Advances.}"
        text = replace_once(text, marker, paragraph + marker, "survey Recent SPAD Advances")

    if text.count(f"\\cite{{{KEY}}}") != 1:
        raise RuntimeError(f"Survey should cite {KEY} exactly once")
    write("article/2active.tex", text)


def main() -> None:
    update_readme()
    update_homepage()
    update_survey()
    print("Synchronized edge-resolved transient NLOS update across README, homepage, and survey source.")


if __name__ == "__main__":
    main()
