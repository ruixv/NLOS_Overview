#!/usr/bin/env python3
"""Synchronize the 15 July 2026 sparse-sampling NLOS citation-tracing update.

The update is intentionally idempotent and uses exact titles/anchors so that a
future layout change fails loudly instead of truncating or silently corrupting
large public-facing files.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article/2active.tex"
NOTE = ROOT / "updates/2026-07-15-sparse-sampling-citation-tracing.md"

SSN_TITLE = "Non-Line-of-Sight Imaging With Signal Superresolution Network"
SSCR_TITLE = "Few-Shot Non-Line-of-Sight Imaging With Signal-Surface Collaborative Regularization"
SSN_URL = "https://openaccess.thecvf.com/content/CVPR2023/html/Wang_Non-Line-of-Sight_Imaging_With_Signal_Superresolution_Network_CVPR_2023_paper.html"
SSCR_URL = "https://openaccess.thecvf.com/content/CVPR2023/html/Liu_Few-Shot_Non-Line-of-Sight_Imaging_With_Signal-Surface_Collaborative_Regularization_CVPR_2023_paper.html"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label} anchor, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> bool:
    text = README.read_text(encoding="utf-8")
    original = text

    ssn_row = (
        f"| 2023 | [{SSN_TITLE}]({SSN_URL}) — Wang et al. | CVPR 2023 | "
        "Learns a plug-and-play transient superresolution operator that recovers dense measurement grids "
        "from sparse confocal or non-confocal scans, cutting acquisition time by 16× while retaining "
        "comparable reconstruction quality. |\n"
    )
    if SSN_TITLE not in text:
        header = "|------|-------|----------------|----------------|\n"
        text = replace_once(text, header, header + ssn_row, "README latest-table header")

    old_sscr = (
        "| 2022 | [Few-shot Non-line-of-sight Imaging with Signal-surface Collaborative Regularization]"
        "(https://arxiv.org/abs/2211.15367) — Liu et al. | arXiv 2022 | Extends sparse active NLOS "
        "reconstruction with mixed-dimensional priors over measured signals, virtual confocal signals, and "
        "hidden surfaces; demonstrates few-shot recovery from very coarse confocal grids. |"
    )
    new_sscr = (
        f"| 2023 | [{SSCR_TITLE}]({SSCR_URL}) — Liu et al. | CVPR 2023 | Jointly regularizes transient "
        "signals, a 3D voxel representation, and a 2D hidden-surface representation; reconstructs complex "
        "hidden geometry from only 5×5 confocal measurements and reports a 10,000× acquisition reduction. |"
    )
    if old_sscr in text:
        text = replace_once(text, old_sscr, new_sscr, "README SSCR row")
    elif new_sscr not in text:
        raise RuntimeError("Neither the old nor updated README SSCR row was found")

    ssn_milestone = (
        "2023 ── Wang et al.: Signal Superresolution Network — plug-and-play 16× sparse-scan acceleration [CVPR]\n"
        "   │     Liu et al.: SSCR — mixed-dimensional regularization from 5×5 confocal measurements [CVPR]\n"
        "   │     Plack et al.: fast differentiable transient rendering — NLOS inverse rendering in minutes [WACV]"
    )
    old_milestone = "2023 ── Plack et al.: fast differentiable transient rendering — NLOS inverse rendering in minutes [WACV]"
    if "Signal Superresolution Network — plug-and-play" not in text:
        text = replace_once(text, old_milestone, ssn_milestone, "README 2023 milestone")

    if text != original:
        README.write_text(text, encoding="utf-8")
        return True
    return False


def update_index() -> bool:
    text = INDEX.read_text(encoding="utf-8")
    original = text
    ssn_was_absent = SSN_TITLE not in text

    ssn_object = (
        f'      {{cat:"latest learning active",title:"{SSN_TITLE}",authors:"Wang et al.",year:2023,'
        f'venue:"CVPR 2023",url:"{SSN_URL}",key:"A plug-and-play learned measurement-space '
        'superresolution module recovers dense transients from sparse confocal or non-confocal scans, cutting '
        'acquisition time by 16× while preserving comparable reconstruction quality."},\n'
    )
    if ssn_was_absent:
        anchor = "    const papers=[\n"
        text = replace_once(text, anchor, anchor + ssn_object, "index paper-array anchor")
        old_count = '<div class="stat"><b>96</b><span>tracked latest entries</span></div>'
        new_count = '<div class="stat"><b>97</b><span>tracked latest entries</span></div>'
        text = replace_once(text, old_count, new_count, "index tracked-entry count")

    sscr_pattern = re.compile(
        r'^\s*\{cat:"latest active",title:"Few-shot Non-line-of-sight Imaging with Signal-surface Collaborative Regularization".*?\},$',
        re.MULTILINE,
    )
    updated_sscr = (
        f'      {{cat:"latest learning active",title:"{SSCR_TITLE}",authors:"Xintong Liu et al.",year:2023,'
        f'venue:"CVPR 2023",url:"{SSCR_URL}",key:"Mixed-dimensional regularization couples transient '
        'signals, a 3D voxel volume, and a 2D hidden surface, reconstructing complex geometry from only 5×5 '
        'confocal measurements with a reported 10,000× acquisition reduction."},'
    )
    matches = list(sscr_pattern.finditer(text))
    if matches:
        if len(matches) != 1:
            raise RuntimeError(f"Expected one old SSCR index object, found {len(matches)}")
        text = sscr_pattern.sub(updated_sscr, text, count=1)
    elif updated_sscr not in text:
        raise RuntimeError("Neither the old nor updated SSCR index object was found")

    timeline_pattern = re.compile(
        r'^\s*<div class="tl"><div class="year">2023</div><div class="tl-body">.*?</div></div>$',
        re.MULTILINE,
    )
    new_timeline = (
        '      <div class="tl"><div class="year">2023</div><div class="tl-body"><strong>Sparse transient '
        'recovery, differentiable rendering, joint LOS/NLOS shape, transformers, arbitrary patterns, virtual '
        'mirrors, neural implicit NLOS, and active corner cameras</strong><p>SSN learned a plug-and-play '
        'measurement-space superresolution operator for 16× faster sparse scanning, while SSCR combined '
        'signal, voxel, and surface priors to reconstruct from only 5×5 confocal measurements. Plack et al. '
        'reduced physically based analysis-by-synthesis NLOS reconstruction from hours to minutes on consumer '
        'hardware; Choi et al. coupled phasor-field reconstruction with differentiable transient transport to '
        'jointly self-calibrate imaging filters, sensor response, geometry, normals, and albedo; Omni-LOS '
        'unified straight-ray LOS and spherical-wavefront NLOS transients in a neural level-set model for '
        'near-360° shape recovery from one fixed scan position; NLOST, PAC-Net, NLOS-NeuS, arbitrary '
        'illumination/detection reconstruction, structure-sparsity regularization, scattering-media phasor '
        'fields, and active corner cameras broadened reconstruction settings; Virtual Mirrors turned '
        'higher-order phasor transport into secondary apertures for limited-visibility and two-corner NLOS '
        'imaging.</p></div></div>'
    )
    if "SSN learned a plug-and-play" not in text:
        matches = list(timeline_pattern.finditer(text))
        if len(matches) != 1:
            raise RuntimeError(f"Expected one 2023 index timeline line, found {len(matches)}")
        text = timeline_pattern.sub(new_timeline, text, count=1)

    if text != original:
        INDEX.write_text(text, encoding="utf-8")
        return True
    return False


def update_active_survey() -> bool:
    text = ACTIVE.read_text(encoding="utf-8")
    original = text
    old_pattern = re.compile(
        r"More recently, several works have further reduced the required scanning density\. "
        r"Wang~\\etal~proposed a signal superresolution network.*?"
        r"\\cite\{cuiVirtualScanning2024\}\."
    )
    new = (
        "More recently, CVPR 2023 established two complementary routes to extreme sparse acquisition: SSCR "
        "uses mixed-dimensional optimization priors, while Wang~\\etal~proposed a signal superresolution "
        "network that maps sparse scanning measurements to dense ones before reconstruction, achieving a "
        "$16\\times$ reduction in acquisition time while maintaining comparable quality~"
        "\\cite{liuFewShotSSCR2022,wangSignalSuperresolution2023}. Li~\\etal~then proposed the first deep "
        "learning framework specifically for NLOS reconstruction from under-scanning measurements (USM), "
        "using a transient recovery network (TRN) to recover full-density transients from sparse inputs, "
        "followed by a physical-model-based volume reconstruction network (VRN) that achieves $50\\times$ "
        "faster reconstruction than iterative methods~\\cite{liDeepUnderscanning2023}. Cui~\\etal~introduced "
        "Virtual Scanning, an unsupervised framework for NLOS reconstruction from irregularly undersampled "
        "transients without requiring paired ground truth, leveraging a physics-guided denoiser to handle the "
        "noise inherent in low-photon conditions~\\cite{cuiVirtualScanning2024}."
    )
    if "CVPR 2023 established two complementary routes" not in text:
        matches = list(old_pattern.finditer(text))
        if len(matches) != 1:
            raise RuntimeError(f"Expected one sparse-scanning survey paragraph, found {len(matches)}")
        text = old_pattern.sub(lambda _m: new, text, count=1)

    if text != original:
        ACTIVE.write_text(text, encoding="utf-8")
        return True
    return False


def write_note() -> bool:
    content = f"""# 15 July 2026 sparse-sampling NLOS citation-tracing update

A fresh search of arXiv, conference and journal pages, project/lab pages, and forward citations of the repository's core active-NLOS papers did not identify a directly relevant paper newer than the 5 July 2026 NIR raster-scanning preprint already tracked by the repository.

The high-priority citation-tracing pass through recent phasor-field and sparse-aperture work did identify a public-coverage and bibliography gap around two CVPR 2023 milestones:

- **{SSN_TITLE}** (Wang et al., CVPR 2023, pp. 17420--17429) learns a plug-and-play transient superresolution module for sparse confocal and non-confocal measurements and reports a 16x acquisition-time reduction at comparable reconstruction quality.
- **{SSCR_TITLE}** (Liu et al., CVPR 2023, pp. 13303--13312) was previously labelled only by its 2022 arXiv posting. The final CVPR venue is now used; the method jointly regularizes measured signals, a 3D voxel representation, and a 2D hidden surface, demonstrating recovery from a 5x5 confocal grid and a reported 10,000x acquisition reduction.

The survey source already discussed SSN and Deep Non-Line-of-Sight Imaging from Under-Scanning Measurements, but the consolidated bibliography did not contain their citation keys. This update therefore also adds a conservative NeurIPS 2023 record for the under-scanning paper, using only metadata verified from the LEAP reference list and leaving the proceedings URL unspecified until a stable publisher page is confirmed.

## Files synchronized

- `README.md`: adds SSN, corrects SSCR to CVPR 2023, and expands the 2023 timeline.
- `index.html`: adds the SSN explorer entry, corrects SSCR metadata, increments the tracked-entry count, and expands the 2023 development node.
- `article/2active.tex`: rewrites the sparse-acquisition paragraph to connect SSCR, SSN, USM, and Virtual Scanning.
- `egbib_20260715_sparse_sampling_updates.bib`: adds canonical records for SSN, SSCR, and USM.
- `egbib_merged_20260711.bib`: regenerated by `scripts/merge_nlos_bibliography.py`.
- `bare_jrnl.pdf`: regenerated by the update workflow after a clean LaTeX/BibTeX build.

The workflow validates all three citation keys, rejects undefined citations, checks the generated PDF is non-empty, and confirms that the SSN and SSCR titles appear in extracted PDF text.
"""
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    old = NOTE.read_text(encoding="utf-8") if NOTE.exists() else None
    if old != content:
        NOTE.write_text(content, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = {
        "README.md": update_readme(),
        "index.html": update_index(),
        "article/2active.tex": update_active_survey(),
        str(NOTE.relative_to(ROOT)): write_note(),
    }
    print("Sparse-sampling NLOS synchronization complete:")
    for path, did_change in changed.items():
        print(f"- {path}: {'updated' if did_change else 'already current'}")


if __name__ == "__main__":
    main()
