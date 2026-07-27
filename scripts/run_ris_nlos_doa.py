#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
MODALITIES = ROOT / "article" / "5newscenes.tex"
MASTER = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"

AROUND_TITLE = "Around-the-corner Radar Sensing Using Reconfigurable Intelligent Surface"
AROUND_OLD = "https://arxiv.org/abs/2602.11471"
AROUND_DOI = "10.1109/MAPCON61407.2024.10923061"
AROUND_KEY = "yasmeenAroundCornerRIS2024"
DUAL_TITLE = "Radar Sensing using Dual-Beam Reconfigurable Intelligent Surface"
DUAL_OLD = "https://arxiv.org/abs/2602.11473"
DUAL_DOI = "10.1109/RadarConf2559087.2025.11205052"
DUAL_KEY = "yasmeenDualBeamRIS2026"  # Preserve the established citation key.
GEOMETRY_TITLE = "Geometry-Constrained Non-Line-of-Sight Imaging"
GEOMETRY_DOI = "10.1109/TVCG.2026.3684832"


def die(message: str) -> None:
    raise RuntimeError(message)


def patch_readme() -> None:
    lines = README.read_text(encoding="utf-8").splitlines(keepends=True)
    seen_geometry = False
    output: list[str] = []
    around_hits = dual_hits = 0
    for line in lines:
        if GEOMETRY_TITLE in line and GEOMETRY_DOI in line:
            if seen_geometry:
                continue
            seen_geometry = True
        if AROUND_TITLE in line:
            around_hits += 1
            line = line.replace(AROUND_OLD, f"https://doi.org/{AROUND_DOI}")
            line = re.sub(r"^\|\s*2026\s*\|", "| 2024 |", line)
            line = line.replace("| arXiv 2026 |", "| IEEE MAPCON 2024 |")
            line = line.replace(
                "RIS-assisted around-the-corner radar sensing; steers energy into NLOS regions and recovers human micro-Doppler signatures.",
                "Uses a custom 1-bit RIS with a measured 5.5 GHz monostatic radar to steer illumination around a corridor corner and recover human walking micro-Doppler signatures; this is experimental NLOS sensing rather than hidden-shape reconstruction.",
            )
        if DUAL_TITLE in line:
            dual_hits += 1
            line = line.replace(DUAL_OLD, f"https://doi.org/{DUAL_DOI}")
            line = re.sub(r"^\|\s*2026\s*\|", "| 2025 |", line)
            line = line.replace("| arXiv 2026 |", "| IEEE RadarConf25 2025 |")
            line = line.replace(
                "Extends RIS-assisted around-corner radar toward practical one-bit dual-beam RIS configurations, benchmarking beam steering and radar cross-section against metal and ideal single-beam RIS baselines.",
                "Benchmarks a practical 1-bit dual-beam RIS against a metal plate and an ideal single-beam RIS in simulations and measurements, widening NLOS radar coverage and supporting simultaneous multi-direction sensing.",
            )
        output.append(line)
    if around_hits != 1 or dual_hits != 1:
        die(f"README expected one row per RIS paper; found around={around_hits}, dual={dual_hits}")
    if not seen_geometry:
        die("README geometry-constrained record was not found")
    README.write_text("".join(output), encoding="utf-8")


def update_paper_object(text: str, title: str, year: int, venue: str, url: str, summary: str) -> str:
    lines = text.splitlines(keepends=True)
    hits = 0
    output: list[str] = []
    for line in lines:
        if f'title:"{title}"' in line:
            hits += 1
            line = re.sub(r"year:\d{4}", f"year:{year}", line)
            line = re.sub(r'venue:"[^"]*"', f'venue:"{venue}"', line)
            line = re.sub(r'url:"[^"]*"', f'url:"{url}"', line)
            line = re.sub(r'key:"[^"]*"', f'key:"{summary}"', line)
        output.append(line)
    if hits != 1:
        die(f"website expected one object for {title!r}; found {hits}")
    return "".join(output)


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")
    text = update_paper_object(
        text,
        AROUND_TITLE,
        2024,
        "IEEE MAPCON 2024",
        f"https://doi.org/{AROUND_DOI}",
        "Experimental 5.5 GHz monostatic radar and a custom 1-bit RIS steer illumination around a corridor corner and recover human walking micro-Doppler; NLOS sensing rather than hidden-shape reconstruction.",
    )
    text = update_paper_object(
        text,
        DUAL_TITLE,
        2025,
        "IEEE RadarConf25 2025",
        f"https://doi.org/{DUAL_DOI}",
        "A practical 1-bit dual-beam RIS is compared with metal and ideal single-beam reflectors in simulations and measurements, widening hidden-region radar coverage and enabling simultaneous multi-direction sensing.",
    )

    lines = text.splitlines(keepends=True)
    geometry_seen = False
    output: list[str] = []
    for line in lines:
        if f'title:"{GEOMETRY_TITLE}"' in line:
            if geometry_seen:
                continue
            geometry_seen = True
        output.append(line)
    if not geometry_seen:
        die("website geometry-constrained object was not found")
    text = "".join(output)
    count = len(re.findall(r'\{cat:"', text))
    text, n = re.subn(
        r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',
        f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',
        text,
        count=1,
    )
    if n != 1:
        die("website tracked-entry counter not found")
    INDEX.write_text(text, encoding="utf-8")


def patch_modalities() -> None:
    text = MODALITIES.read_text(encoding="utf-8")
    old = r"\href{https://arxiv.org/abs/2602.11471}{RIS-assisted around-corner radar} uses a reconfigurable intelligent surface to steer RF energy into otherwise difficult NLOS regions and recover micro-Doppler signatures."
    new = (
        r"Yasmeen~\etal~experimentally used a custom one-bit RIS with a 5.5~GHz monostatic radar to steer illumination around a corridor corner and recover human walking micro-Doppler signatures~\cite{yasmeenAroundCornerRIS2024}."
    )
    if old in text:
        text = text.replace(old, new, 1)
    elif AROUND_KEY not in text:
        die("survey around-corner RIS anchor was not found")
    if DUAL_KEY not in text:
        die("survey is missing the established dual-beam RIS citation")
    MODALITIES.write_text(text, encoding="utf-8")


def replace_bib_entry(text: str, key: str, entry: str) -> str:
    pattern = re.compile(rf"(?ms)^@\w+\{{{re.escape(key)},.*?^\}}\s*")
    matches = list(pattern.finditer(text))
    if len(matches) > 1:
        die(f"bibliography has duplicate key {key}")
    if matches:
        return text[: matches[0].start()] + entry.rstrip() + "\n\n" + text[matches[0].end() :].lstrip("\n")
    return text.rstrip() + "\n\n" + entry.rstrip() + "\n"


def patch_bib() -> None:
    text = BIB.read_text(encoding="utf-8")
    around_entry = r"""@inproceedings{yasmeenAroundCornerRIS2024,
  author = {Yasmeen, Kainat and Kundu, Debidas and Ram, Shobha Sundar},
  title = {Around-the-Corner Radar Sensing Using Reconfigurable Intelligent Surface},
  booktitle = {2024 IEEE Microwaves, Antennas, and Propagation Conference (MAPCON)},
  year = {2024},
  publisher = {IEEE},
  doi = {10.1109/MAPCON61407.2024.10923061},
  url = {https://doi.org/10.1109/MAPCON61407.2024.10923061}
}"""
    dual_entry = r"""@inproceedings{yasmeenDualBeamRIS2026,
  author = {Yasmeen, Kainat and Ram, Shobha Sundar and Kundu, Debidas},
  title = {Radar Sensing Using Dual-Beam Reconfigurable Intelligent Surface},
  booktitle = {2025 IEEE Radar Conference (RadarConf25)},
  pages = {1--6},
  year = {2025},
  publisher = {IEEE},
  doi = {10.1109/RadarConf2559087.2025.11205052},
  url = {https://doi.org/10.1109/RadarConf2559087.2025.11205052}
}"""
    text = replace_bib_entry(text, AROUND_KEY, around_entry)
    text = replace_bib_entry(text, DUAL_KEY, dual_entry)
    for doi, key in ((AROUND_DOI, AROUND_KEY), (DUAL_DOI, DUAL_KEY)):
        if text.lower().count(doi.lower()) != 2:
            die(f"bibliography DOI {doi} should appear exactly in doi and url")
        if text.count("{" + key + ",") != 1:
            die(f"bibliography key mismatch for {key}")
    BIB.write_text(text, encoding="utf-8")


def patch_master() -> None:
    text = MASTER.read_text(encoding="utf-8")
    marker = "% 27 July 2026 venue audit: RIS around-corner and dual-beam radar records corrected to MAPCON 2024 and IEEE RadarConf 2025.\n"
    if marker not in text:
        anchor = "%% bare_jrnl.tex\n"
        if text.count(anchor) != 1:
            die("master LaTeX header anchor is not unique")
        text = text.replace(anchor, anchor + marker, 1)
    MASTER.write_text(text, encoding="utf-8")


def validate() -> None:
    files = {
        "README": README.read_text(encoding="utf-8"),
        "website": INDEX.read_text(encoding="utf-8"),
        "modalities": MODALITIES.read_text(encoding="utf-8"),
        "bib": BIB.read_text(encoding="utf-8"),
    }
    for doi, key in ((AROUND_DOI, AROUND_KEY), (DUAL_DOI, DUAL_KEY)):
        for label in ("README", "website", "bib"):
            if doi not in files[label]:
                die(f"{label} missing {doi}")
        if key not in files["modalities"]:
            die(f"survey missing {key}")
    for stale in (AROUND_OLD, DUAL_OLD):
        if stale in files["README"] + files["website"] + files["modalities"]:
            die(f"stale public arXiv URL remains: {stale}")
    if files["README"].count(GEOMETRY_TITLE) != 1:
        die("README geometry-constrained duplicate cleanup failed")
    if files["website"].count(f'title:"{GEOMETRY_TITLE}"') != 1:
        die("website geometry-constrained duplicate cleanup failed")
    count = len(re.findall(r'\{cat:"', files["website"]))
    expected = f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>'
    if expected not in files["website"]:
        die("website entry counter is inconsistent")
    print(f"RIS final venues corrected and cross-artifact validation passed ({count} website entries)")


def main() -> None:
    patch_readme()
    patch_index()
    patch_modalities()
    patch_bib()
    patch_master()
    validate()


if __name__ == "__main__":
    main()
