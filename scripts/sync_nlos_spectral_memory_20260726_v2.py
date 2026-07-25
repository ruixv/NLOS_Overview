from __future__ import annotations

import re

import sync_nlos_spectral_memory_20260726 as base


def line_insert_after(text: str, needle: str, addition: str, label: str) -> str:
    if addition.strip() in text:
        return text
    pos = text.find(needle)
    if pos < 0:
        raise SystemExit(f"Fail-closed: line needle not found for {label}: {needle!r}")
    end = text.find("\n", pos)
    if end < 0:
        end = len(text)
        suffix = "\n"
    else:
        end += 1
        suffix = ""
    return text[:end] + addition + suffix + text[end:]


def line_insert_before(text: str, needle: str, addition: str, label: str) -> str:
    if addition.strip() in text:
        return text
    pos = text.find(needle)
    if pos < 0:
        raise SystemExit(f"Fail-closed: line needle not found for {label}: {needle!r}")
    start = text.rfind("\n", 0, pos) + 1
    return text[:start] + addition + text[start:]


def update_readme_v2() -> None:
    old = base.read(base.README)
    text = old
    header = "|------|-------|----------------|----------------|\n"
    rows = ""
    for p in base.PAPERS:
        if p["title"].lower() in text.lower() or p["doi"].lower() in text.lower():
            continue
        rows += (
            f'| {p["year"]} | [{p["title"]}](https://doi.org/{p["doi"]}) — {p["authors_short"]} '
            f'| {p["venue"]} | {p["summary"]} |\n'
        )
    if rows:
        text = base.insert_once(text, header, rows, "README latest-additions table")

    text = re.sub(r"\*\*Update run: \d{1,2} July 2026\.\*\*", "**Update run: 26 July 2026.**", text, count=1)

    add_2024 = "    │     Zhou et al.: white-light ZPF speckle correlation — ambient-light and alignment-robust ordinary-camera reconstruction [Optics & Laser Technology]\n"
    text = line_insert_after(
        text,
        "Wang et al.: event-enhanced passive NLOS",
        add_2024,
        "README 2024 timeline",
    )

    add_2025 = (
        "2025 ── Fu et al. and Zhou et al.: physics-enhanced and single-shot speckle statistics move steady-state NLOS toward inexpensive white-light and ambient-light operation [Applied Optics / Optics Communications]\n"
        "    │     Hashemi et al. and Chen et al.: multispectral clutter separation and learned hyperspectral band selection strengthen passive NLOS under realistic backgrounds [IEEE TPAMI / Expert Systems with Applications]\n"
        "    │     Zhang et al.: CMFormer reduces transient-volume memory cost and reaches consumer-GPU real-time reconstruction [Optics and Lasers in Engineering]\n"
    )
    text = line_insert_before(
        text,
        "Shi et al.: fast configurable transient simulation and an open NLOS benchmark",
        add_2025,
        "README 2025 timeline",
    )

    base.write_if_changed(base.README, old, text)


_original_update_passive = base.update_passive


def update_passive_v2() -> None:
    old = base.read(base.PASSIVE)
    text = old
    table_start = text.find("\\begin{table*")
    table_end = text.find("\\end{table*", table_start)
    if table_start < 0 or table_end < 0:
        raise SystemExit("Fail-closed: passive table bounds missing")
    table = text[table_start:table_end]
    if "fuPhysicsEnhancedWhiteLightNLOS2025" not in table:
        rows = (
            "    \\cite{zhouWhiteLightSpeckleNLOS2024,fuPhysicsEnhancedWhiteLightNLOS2025,zhouSingleShotSpeckleNLOS2025} & White light / coherent speckle & Conventional camera & Speckle statistics with physics-enhanced or single-shot inversion & 2D reconstruction\\\\%%%% Table body\n"
            "    \\cite{hashemiSpectralContentPassiveNLOS2025,chenHyperspectralBandSelectionNLOS2025} & Ambient/incoherent light & Multispectral or hyperspectral camera & Spectral unmixing and learned band selection & Full-colour 2D reconstruction\\\\%%%% Table body\n"
        )
        needle = "\\cite{katz2014non}"
        pos = table.find(needle)
        if pos < 0:
            raise SystemExit("Fail-closed: passive speckle table row missing")
        line_end = table.find("\n", pos)
        if line_end < 0:
            raise SystemExit("Fail-closed: passive speckle row line ending missing")
        line_end += 1
        table = table[:line_end] + rows + table[line_end:]
        text = text[:table_start] + table + text[table_end:]
        base.PASSIVE.write_text(text, encoding="utf-8")
    _original_update_passive()


def validate_v2() -> None:
    readme = base.read(base.README).lower()
    index = base.read(base.INDEX).lower()
    passive = base.read(base.PASSIVE)
    learning = base.read(base.LEARNING)
    bib = base.read(base.BIB).lower()
    for p in base.PAPERS:
        title = p["title"].lower()
        doi = p["doi"].lower()
        if readme.count(title) != 1:
            raise SystemExit(f"README title count is not one: {p['title']}")
        if index.count(title) != 1:
            raise SystemExit(f"index title count is not one: {p['title']}")
        # Each canonical record intentionally contains the DOI once in `doi` and once in its DOI URL.
        if bib.count(doi) != 2:
            raise SystemExit(f"bibliography DOI occurrence count is not two: {p['doi']}")
        if ("{" + p["key"].lower() + ",") not in bib:
            raise SystemExit(f"bibliography key missing: {p['key']}")
    for key in (
        "zhouWhiteLightSpeckleNLOS2024",
        "fuPhysicsEnhancedWhiteLightNLOS2025",
        "zhouSingleShotSpeckleNLOS2025",
        "hashemiSpectralContentPassiveNLOS2025",
        "chenHyperspectralBandSelectionNLOS2025",
    ):
        if key not in passive:
            raise SystemExit(f"passive survey citation missing: {key}")
    for key in ("fuPhysicsEnhancedWhiteLightNLOS2025", "zhangCMFormerNLOS2025"):
        if key not in learning:
            raise SystemExit(f"learning survey citation missing: {key}")
    print("Cross-artifact validation passed.")


base.update_readme = update_readme_v2
base.update_passive = update_passive_v2
base.validate = validate_v2
base.main()
