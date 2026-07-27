#!/usr/bin/env python3
from __future__ import annotations

import re

import integrate_ris_nlos_doa as ris


def patch_readme_without_duplicate_category_rows() -> None:
    text = ris.README.read_text(encoding="utf-8")
    separator = "|------|-------|----------------|----------------|\n"
    rows = ""
    if ris.GRIDLESS_DOI not in text:
        rows += (
            f"| 2025 | [{ris.GRIDLESS_TITLE}](https://doi.org/{ris.GRIDLESS_DOI}) — Yuan et al. | Signal Processing 2025 | Uses an RIS-created virtual-LOS path, covariance-domain denoising, atomic-norm minimization, and ADMM for gridless multi-target direction estimation with limited receive hardware; numerical validation only. |\n"
        )
    if ris.MONOSTATIC_DOI not in text:
        rows += (
            f"| 2026 | [{ris.MONOSTATIC_TITLE}](https://doi.org/{ris.MONOSTATIC_DOI}) — Zhang et al. | Signal Processing 2026 | Scans hidden directions with an RIS codebook, decouples the target steering-vector outer product from the composite monostatic echo, and applies Root-MUSIC for NLOS angle estimation; simulation-only, not hidden-shape reconstruction. |\n"
        )
    if rows:
        text = ris.replace_once(text, separator, separator + rows, "README latest-additions table")

    additions = {
        2025: (
            "Yuan et al.: RIS-enabled covariance-domain gridless DoA",
            "     │     Yuan et al.: RIS-enabled covariance-domain gridless DoA uses atomic-norm recovery and ADMM for simulated multi-target NLOS angular sensing [Signal Processing]",
        ),
        2026: (
            "Zhang et al.: monostatic radar--RIS steering-vector decoupling",
            "     │     Zhang et al.: monostatic radar--RIS steering-vector decoupling and Root-MUSIC enable simulated NLOS target-angle estimation [Signal Processing]",
        ),
    }
    for year, (marker, sentence) in additions.items():
        if marker in text:
            continue
        match = re.search(rf'(^\s*{year} ──.*?$)', text, re.MULTILINE)
        if not match:
            ris.die(f"README: {year} timeline anchor not found")
        text = text[: match.end()] + "\n" + sentence + text[match.end() :]

    text = text.replace("**Update run: 26 July 2026.**", "**Update run: 27 July 2026.**")
    ris.README.write_text(text, encoding="utf-8")


def main() -> None:
    patch_readme_without_duplicate_category_rows()
    ris.patch_index()
    ris.patch_modalities()
    ris.patch_bib()
    ris.patch_master()
    ris.validate()
    print("RIS-assisted NLOS DoA integration completed and validated")


if __name__ == "__main__":
    main()
