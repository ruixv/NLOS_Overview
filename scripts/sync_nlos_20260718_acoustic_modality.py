#!/usr/bin/env python3
"""Synchronize verified ultrasound and relay-free acoustic NLOS papers."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAPERS = [
    {
        "title": "Ultrasound synthetic aperture non-line-of-sight imaging",
        "authors": "Li et al.",
        "year": 2025,
        "venue": "Communications Physics 2025",
        "url": "https://doi.org/10.1038/s42005-025-02335-3",
        "cat": "latest modality acoustic reconstruction",
        "key": "ultrasoundNLOS2025",
        "summary": "Transfers the core optical ToF/f-k reconstruction trajectory to coherent ultrasound: a phase-sensitive scanning emitter-receiver synthetic aperture reconstructs complex hidden 3D scenes at meter-scale range with approximately 1 cm lateral and depth resolution, using low-power eye-safe hardware.",
    },
    {
        "title": "Passive acoustic non-line-of-sight localization without a relay surface",
        "authors": "Sommer, Katz",
        "year": 2026,
        "venue": "Physical Review Applied 2026",
        "url": "https://doi.org/10.1103/p97k-sf71",
        "cat": "latest modality acoustic localization",
        "key": "sommerPassiveAcousticNLOS2026",
        "summary": "Replaces relay-wall reflection with obstacle-edge diffraction for passive 3D localization of hidden sound sources. Door edges act as virtual detector arrays, while corner localization exploits the frequency-dependent knife-edge diffraction signature.",
    },
]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return text.replace(old, new, 1)


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
    if sentence.strip() not in lines[matches[0]]:
        closing = "</p></div></div>"
        if closing not in lines[matches[0]]:
            raise RuntimeError(f"Timeline closing marker missing for {year}")
        lines[matches[0]] = lines[matches[0]].replace(closing, " " + sentence.strip() + closing, 1)
    return "".join(lines)


def update_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    rows = ""
    for paper in PAPERS:
        if f"[{paper['title']}]" not in text:
            rows += (
                f"| {paper['year']} | [{paper['title']}]({paper['url']}) - {paper['authors']} | "
                f"{paper['venue']} | {paper['summary']} |\n"
            )
    if rows:
        header = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, header, header + rows, "README latest-additions header")

    audit_anchor = "   |     18 July 2026 core-citation tracing: forward-citation and modality-expansion audit completed\n"
    audit_lines = (
        "   |     Li et al.: coherent ultrasound synthetic apertures reach centimeter-scale hidden 3D reconstruction at meter-scale range [Communications Physics]\n"
        "   |     Sommer and Katz: knife-edge diffraction enables relay-free passive acoustic NLOS localization [Physical Review Applied]\n"
        "   |     18 July 2026 acoustic citation trace: final-venue ultrasound and edge-diffraction records synchronized across public and survey artifacts\n"
    )
    if "18 July 2026 acoustic citation trace" not in text:
        text = replace_once(text, audit_anchor, audit_lines + audit_anchor, "README core-citation audit marker")
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    additions = [paper_object(p) for p in PAPERS if f'title:"{p["title"]}"' not in text]
    if additions:
        text = replace_once(text, "    const papers=[\n", "    const papers=[\n" + "\n".join(additions) + "\n", "homepage paper array")

    stat_pattern = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
    match = stat_pattern.search(text)
    if not match:
        raise RuntimeError("Homepage tracked-entry statistic not found")
    expected = len(re.findall(r'^\s*\{cat:"[^"]+",title:"', text, flags=re.MULTILINE))
    if int(match.group(2)) != expected:
        text = stat_pattern.sub(lambda m: m.group(1) + str(expected) + m.group(3), text, count=1)

    text = append_to_timeline_year(
        text,
        2025,
        "Li et al. translated the optical LCT/f-k lineage into coherent ultrasound synthetic-aperture imaging, achieving centimeter-scale 3D resolution at meter-scale hidden ranges.",
    )
    text = append_to_timeline_year(
        text,
        2026,
        "Sommer and Katz removed the relay-surface requirement for passive acoustic sensing by localizing hidden sources from doorway and corner knife-edge diffraction.",
    )
    path.write_text(text, encoding="utf-8")


def update_new_scenes() -> None:
    path = ROOT / "article/5newscenes.tex"
    text = path.read_text(encoding="utf-8")

    old_ultrasound = (
        "More recently, a synthetic aperture ultrasound NLOS imaging system has been demonstrated~\\cite{ultrasoundNLOS2025}, "
        "operating in a frequency range similar to bat echolocation and achieving centimeter-scale depth resolution at distances up to 2\\,m from the scattering surface. "
        "By using a scanning ultrasound emitter and receiver, this system demonstrates high-resolution 3D reconstruction of multiple hidden targets and complex scenes. "
        "The spatial resolution of the acoustic system scales with the opening angle of the scattering surface rather than the sound wavelength, enabling sub-wavelength effective resolution."
    )
    new_ultrasound = (
        "Li~\\etal~translated the optical ToF and $f$--$k$ migration lineage into a coherent synthetic-aperture ultrasound system~\\cite{ultrasoundNLOS2025}. "
        "A scanning emitter--receiver pair preserves acoustic phase and reconstructs multiple hidden targets and complex 3D scenes at distances up to 2\\,m from the scattering surface, with measured lateral and depth resolution of approximately 1\\,cm. "
        "The study also reports the NLOS modulation-transfer function and releases data and code, establishing ultrasound as a quantitatively comparable, low-power and eye-safe alternative to optical transient NLOS."
    )
    if "releases data and code, establishing ultrasound" not in text:
        text = replace_once(text, old_ultrasound, new_ultrasound, "ultrasound survey paragraph")

    old_passive = (
        "The scope of acoustic NLOS has also moved beyond relay-surface reflection. "
        "\\href{https://arxiv.org/abs/2506.08471}{Passive acoustic NLOS localization without a relay surface} exploits knife-edge diffraction at doorways and corners to localize hidden sound sources. "
        "This relay-free setting is conceptually different from wall-reflection NLOS imaging and suggests that edge diffraction, rather than diffuse reflection alone, can be treated as an exploitable physical transport path for hidden-scene sensing."
    )
    new_passive = (
        "The scope of acoustic NLOS has also moved beyond relay-surface reflection. Sommer and Katz exploit knife-edge diffraction at doorways and convex corners to passively localize a hidden acoustic point source in three dimensions~\\cite{sommerPassiveAcousticNLOS2026}. "
        "For a doorway, its two edges act as virtual detector arrays; for a corner, the method uses the frequency-dependent diffraction-loss signature in a manner analogous to head-related transfer functions. "
        "This relay-free setting shows that edge diffraction, rather than diffuse reflection alone, can be treated as an exploitable physical transport path for hidden-scene sensing."
    )
    if "sommerPassiveAcousticNLOS2026" not in text:
        text = replace_once(text, old_passive, new_passive, "relay-free acoustic survey paragraph")

    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_readme()
    update_index()
    update_new_scenes()
    print("Synchronized two verified acoustic NLOS papers and final venues.")


if __name__ == "__main__":
    main()
