#!/usr/bin/env python3
"""Synchronize the CVPR 2019 NLOS feature-visibility milestone.

The script is idempotent and checks stable anchors before modifying the manually
maintained README, homepage, and survey source.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TITLE = "Analysis of Feature Visibility in Non-Line-of-Sight Measurements"
CITE_KEY = "liuFeatureVisibility2019"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, description: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {description} anchor, found {count}")
    return text.replace(old, new, 1)


def patch_readme() -> None:
    path = "README.md"
    text = read(path)
    text = text.replace("**Update run: 11 July 2026.**", "**Update run: 12 July 2026.**", 1)
    if TITLE in text:
        write(path, text)
        return
    anchor = (
        "| 2019 | [Keyhole Imaging: Non-Line-of-Sight Imaging and Tracking of Moving Objects Along a Single Optical Path]"
        "(https://arxiv.org/abs/1912.06727) — Metzler et al. | IEEE TCI 2021 | Introduces single-optical-path active NLOS imaging/tracking; uses hidden-object motion and EM/unknown-view tomography to recover shape and trajectory when only keyhole-like access is available. |"
    )
    row = (
        "| 2019 | [Analysis of Feature Visibility in Non-Line-of-Sight Measurements]"
        "(https://openaccess.thecvf.com/content_CVPR_2019/html/Liu_Analysis_of_Feature_Visibility_in_Non-Line-of-Sight_Measurements_CVPR_2019_paper.html) — Liu, Bauer, Velten | CVPR 2019 | Systematically analyzes which hidden-scene features are recoverable from transient NLOS measurements, clarifying orientation-, aperture-, and capture-geometry-dependent visibility limits that later reconstruction methods must respect. |"
    )
    text = replace_once(text, anchor, row + "\n" + anchor, "README 2019 insertion")
    write(path, text)


def patch_index() -> None:
    path = "index.html"
    text = read(path)
    text = text.replace("Updated 11 July 2026", "Updated 12 July 2026", 1)
    if TITLE in text:
        write(path, text)
        return
    text = replace_once(
        text,
        '<div class="stat"><b>84</b><span>tracked latest entries</span></div>',
        '<div class="stat"><b>85</b><span>tracked latest entries</span></div>',
        "homepage latest-count",
    )
    timeline_old = (
        '<div class="tl"><div class="year">2019</div><div class="tl-body"><strong>f-k migration, passive periscopy, coherent control, and single-path/scannerless NLOS</strong><p>The field split into wave-based active NLOS, ordinary-camera passive NLOS, keyhole imaging, coherent recognition, scannerless single-pixel acquisition, and wavefront-shaping active focusing.</p></div></div>'
    )
    timeline_new = (
        '<div class="tl"><div class="year">2019</div><div class="tl-body"><strong>f-k migration, feature-visibility limits, passive periscopy, coherent control, and single-path/scannerless NLOS</strong><p>The field split into wave-based active NLOS, principled analysis of which hidden orientations and spatial features are recoverable, ordinary-camera passive NLOS, keyhole imaging, coherent recognition, scannerless single-pixel acquisition, and wavefront-shaping active focusing.</p></div></div>'
    )
    text = replace_once(text, timeline_old, timeline_new, "2019 timeline")
    object_text = (
        '      {cat:"latest active",title:"Analysis of Feature Visibility in Non-Line-of-Sight Measurements",authors:"Liu, Bauer, Velten",year:2019,venue:"CVPR 2019",url:"https://openaccess.thecvf.com/content_CVPR_2019/html/Liu_Analysis_of_Feature_Visibility_in_Non-Line-of-Sight_Measurements_CVPR_2019_paper.html",key:"A foundational recoverability analysis explaining how surface orientation, finite relay aperture, and capture geometry determine which hidden features can appear in transient NLOS reconstructions."},\n'
    )
    match = re.search(r"(?m)^(\s*const papers\s*=\s*\[\s*)$", text)
    if not match:
        raise RuntimeError("Could not find homepage papers-array anchor")
    text = text[: match.end()] + "\n" + object_text + text[match.end() :]
    write(path, text)


def patch_survey() -> None:
    path = "article/2active.tex"
    text = read(path)
    if CITE_KEY in text:
        return
    anchor = (
        "support light-transport analysis as well as geometric imaging.\n\n"
    )
    paragraph = (
        "\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Visibility limits and recoverability.}\n"
        "Beyond developing faster inverses, Liu~\\etal~analyzed which hidden-scene features are physically visible in transient NLOS measurements~\\cite{liuFeatureVisibility2019}. Their study connects recoverability to surface orientation, finite relay-wall aperture, and acquisition geometry, explaining why some surfaces remain weak or absent even under accurate reconstruction. This visibility perspective established an important limit-aware complement to LCT, $f$--$k$ migration, and phasor-field propagation, and motivates later methods that explicitly model normals, occlusion, and adaptive capture.\n\n"
    )
    text = replace_once(text, anchor, anchor + paragraph, "survey visibility insertion")
    write(path, text)


def verify() -> None:
    checks = {
        "README.md": TITLE,
        "index.html": TITLE,
        "article/2active.tex": CITE_KEY,
        "egbib_20260712_feature_visibility_updates.bib": CITE_KEY,
    }
    for path, token in checks.items():
        if token not in read(path):
            raise RuntimeError(f"Verification failed: {token!r} absent from {path}")
    index = read("index.html")
    if '<div class="stat"><b>85</b><span>tracked latest entries</span></div>' not in index:
        raise RuntimeError("Homepage latest count was not updated to 85")


if __name__ == "__main__":
    patch_readme()
    patch_index()
    patch_survey()
    verify()
    print("Feature-visibility synchronization applied and verified.")
