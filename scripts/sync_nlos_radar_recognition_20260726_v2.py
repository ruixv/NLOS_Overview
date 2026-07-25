from __future__ import annotations

import re

import sync_nlos_radar_recognition_20260726 as base


def line_insert_before(text: str, needle: str, addition: str, label: str) -> str:
    if addition.strip() in text:
        return text
    pos = text.find(needle)
    if pos < 0:
        raise SystemExit(f"Fail-closed: line anchor missing for {label}: {needle!r}")
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
        text = base.insert_once(text, header, rows, "README latest additions")

    text = re.sub(r"\*\*Update run: \d{1,2} July 2026\.\*\*", "**Update run: 26 July 2026.**", text, count=1)
    timeline = (
        "    │     Zeng et al.: measured 15 GHz multipath feature fusion recognizes four hidden target classes from path and scattering structure [Journal of Signal Processing]\n"
        "    │     Zhong et al.: physics-guided cross-path contrastive learning recognizes six hidden human activities from UWB radar with only 10% labels [Journal of Radars, Online First]\n"
    )
    if "physics-guided cross-path contrastive learning recognizes six hidden human activities" not in text:
        text = line_insert_before(
            text,
            "Chen et al.: range-migration and 121 GHz holographic operators",
            timeline,
            "README 2026 radar recognition timeline",
        )
    base.write_if_changed(base.README, old, text)


base.update_readme = update_readme_v2
base.BIB_ENTRIES = re.sub(r"\n  url = \{https://doi\.org/[^}]+\}", "", base.BIB_ENTRIES)
base.main()
