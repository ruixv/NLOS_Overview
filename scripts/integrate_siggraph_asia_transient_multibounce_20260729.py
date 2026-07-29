from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


title_sb3d = "Shoot-Bounce-3D: Single-Shot Occlusion-Aware 3D from Lidar by Decomposing Two-Bounce Light"
title_lasso = "Transient LASSO: Transient Large-Scale Scene Reconstruction"

# Guard against duplicate or partially completed integration.
for path in ["README.md", "index.html", "article/4datadriven.tex", "egbib_merged_20260711.bib"]:
    text = read(path)
    for title in [title_sb3d, title_lasso]:
        if title in text:
            raise RuntimeError(f"{path}: {title!r} already present; refusing a partial duplicate update")

# README: add verified final-venue records at the top of Latest Additions.
readme = read("README.md")
readme_anchor = "|------|-------|----------------|----------------|\n"
readme_rows = (
    "| 2025 | [Shoot-Bounce-3D: Single-Shot Occlusion-Aware 3D from Lidar by Decomposing Two-Bounce Light](https://doi.org/10.1145/3757377.3763945) — Klinghoffer et al. | SIGGRAPH Asia 2025 | Uses multiplexed single-shot single-photon LiDAR and a learned decomposition of two-bounce transport, trained on roughly 100,000 simulated transients, to recover dense depth plus occluded and mirror-mediated geometry from one view. Real captures validate the demultiplexing; this is tightly adjacent multi-bounce NLOS reconstruction rather than the conventional relay-wall configuration. |\n"
    "| 2025 | [Transient LASSO: Transient Large-Scale Scene Reconstruction](https://doi.org/10.1145/3757377.3763911) — Scheuble et al. | SIGGRAPH Asia 2025 | Fits a neural scene representation directly to posed raw outdoor transient-LiDAR measurements while explicitly modeling back-reflected light, ambient illumination, and high-flux sensor behavior. It disentangles dense geometry and normals from reflectivity, retroreflectivity, and ambient light, extending transient inverse rendering to in-the-wild urban scenes. |\n"
)
readme = replace_once(readme, readme_anchor, readme_anchor + readme_rows, "README latest table")

readme_timeline_anchor = (
    "   │     Shen et al.: HOLI-1-to-3 combines LOS radiance and NLOS transient fields to complete invisible 3D geometry from one viewpoint [IEEE TPAMI]\n"
)
readme_timeline_add = (
    "   │     Klinghoffer et al.: Shoot-Bounce-3D learns to demultiplex single-shot two-bounce single-photon LiDAR for occlusion- and mirror-aware geometry [SIGGRAPH Asia]\n"
    "   │     Scheuble et al.: Transient LASSO fits raw outdoor transient LiDAR with an ambient- and sensor-aware neural scene field [SIGGRAPH Asia]\n"
)
readme = replace_once(
    readme,
    readme_timeline_anchor,
    readme_timeline_anchor + readme_timeline_add,
    "README 2025 timeline",
)
write("README.md", readme)

# Website: add searchable/latest records, extend the 2025 development trajectory,
# and recalculate the explorer count from the actual data objects.
index = read("index.html")
index_anchor = "    const papers=[\n"
index_objects = (
    "      {cat:\"latest learning active lidar transient multi-bounce occlusion single-shot dataset\",title:\"Shoot-Bounce-3D: Single-Shot Occlusion-Aware 3D from Lidar by Decomposing Two-Bounce Light\",authors:\"Klinghoffer et al.\",year:2025,venue:\"SIGGRAPH Asia 2025\",url:\"https://doi.org/10.1145/3757377.3763945\",key:\"Learns to demultiplex multiplexed two-bounce single-photon LiDAR using roughly 100,000 simulated transients, then recovers dense depth and occluded or mirror-mediated geometry from one real single-shot view; adjacent multi-bounce NLOS rather than a conventional relay-wall setup.\"},\n"
    "      {cat:\"latest learning transient lidar neural-field outdoor inverse-rendering\",title:\"Transient LASSO: Transient Large-Scale Scene Reconstruction\",authors:\"Scheuble et al.\",year:2025,venue:\"SIGGRAPH Asia 2025\",url:\"https://doi.org/10.1145/3757377.3763911\",key:\"Fits a neural scene field to posed raw outdoor transient-LiDAR captures with explicit back-reflection, ambient-light, and high-flux sensor modeling, disentangling geometry, normals, reflectivity, retroreflectivity, and illumination in urban scenes.\"},\n"
)
index = replace_once(index, index_anchor, index_anchor + index_objects, "website paper array")

index_timeline_anchor = (
    "MARMOT made masked transient pretraining and arbitrary-scan completion reusable across downstream NLOS tasks, while HOLI-1-to-3 combined radiance and transient fields so hidden three-bounce evidence could constrain geometry invisible to a single LOS view.</p></div></div>"
)
index_timeline_replacement = (
    "MARMOT made masked transient pretraining and arbitrary-scan completion reusable across downstream NLOS tasks, while HOLI-1-to-3 combined radiance and transient fields so hidden three-bounce evidence could constrain geometry invisible to a single LOS view. Shoot-Bounce-3D then learned to separate multiplexed two-bounce single-photon returns for single-shot occlusion- and mirror-aware geometry, while Transient LASSO extended raw-transient neural reconstruction to outdoor urban trajectories with explicit ambient-light and high-flux sensor modeling.</p></div></div>"
)
index = replace_once(index, index_timeline_anchor, index_timeline_replacement, "website 2025 timeline")

actual_count = index.count('{cat:')
index, count_replacements = re.subn(
    r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',
    f'<div class="stat"><b>{actual_count}</b><span>tracked latest entries</span></div>',
    index,
    count=1,
)
if count_replacements != 1:
    raise RuntimeError("website explorer count anchor not found exactly once")
write("index.html", index)

# Survey prose: place both papers beside neural transient fields and holistic
# LOS/NLOS completion, while explicitly delimiting their relation to classic NLOS.
article = read("article/4datadriven.tex")
article_anchor = (
    "HOLI-1-to-3 uses NLOS transients not only to reconstruct an isolated hidden scene, but to resolve the invisible side of an object observed from one conventional viewpoint~\\cite{shenHOLI1to3TPAMI2025}. Its neural plenoptic representation unifies an LOS radiance field with an NLOS transient field, and a two-stage optimization combines diffusion and transient priors to recover continuous visible and occluded geometry. Relative to NeTF, the trajectory expands from representing spherical hidden transport to fusing straight-ray and multi-bounce evidence for holistic generation; relative to purely RGB diffusion, measured transients provide physical constraints on otherwise ambiguous unseen shape.\n"
)
article_add = (
    "\n\\vspace{0.8mm}\n"
    "\\noindent \\textbf{Multi-bounce and outdoor transient scene reconstruction.}\n"
    "Shoot-Bounce-3D treats normally discarded higher-order single-photon LiDAR returns as recoverable geometric evidence~\\cite{klinghofferShootBounce3D2025}. A multiplexed source illuminates several visible points simultaneously, and a learned transport prior trained on roughly 100,000 simulated transients separates the measured two-bounce contribution of each source point. The demultiplexed transport supports dense metric depth together with geometry hidden by occlusion or mirrors from one view and one capture. Although this is not the canonical relay-wall NLOS geometry, it directly extends the field's multi-bounce inverse problem from sequential scanning to practical single-shot acquisition. Transient LASSO broadens the same transient-learning trajectory from controlled indoor transport to outdoor, in-the-wild reconstruction~\\cite{scheubleTransientLASSO2025}. Its neural scene representation operates on posed raw transient LiDAR, explicitly accounts for back-reflected and ambient components and high-photon-flux sensor behavior, and disentangles geometry and normals from reflectivity, retroreflectivity, and ambient illumination. Together, these studies move transient inverse rendering beyond isolated calibrated hidden volumes toward occlusion-aware single-shot capture and large-scale scene-and-sensor modeling.\n"
)
article = replace_once(article, article_anchor, article_anchor + article_add, "data-driven survey placement")
write("article/4datadriven.tex", article)

# Master survey trace marker.
master = read("bare_jrnl.tex")
master_anchor = "%% bare_jrnl.tex\n"
master_comment = "% 29 July 2026 citation trace: Shoot-Bounce-3D multi-bounce LiDAR and Transient LASSO outdoor transient neural reconstruction synchronized.\n"
master = replace_once(master, master_anchor, master_anchor + master_comment, "bare_jrnl trace marker")
write("bare_jrnl.tex", master)

# Canonical final-venue BibTeX records.
bib = read("egbib_merged_20260711.bib")
bib_add = r'''

@inproceedings{klinghofferShootBounce3D2025,
  author = {Klinghoffer, Tzofi and Somasundaram, Siddharth and Xiang, Xiaoyu and Fan, Yuchen and Richardt, Christian and Dave, Akshat and Raskar, Ramesh and Ranjan, Rakesh},
  title = {{Shoot-Bounce-3D}: Single-Shot Occlusion-Aware 3D from {LiDAR} by Decomposing Two-Bounce Light},
  booktitle = {SIGGRAPH Asia 2025 Conference Papers},
  articleno = {146},
  pages = {146:1--146:12},
  year = {2025},
  month = dec,
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  doi = {10.1145/3757377.3763945},
  url = {https://doi.org/10.1145/3757377.3763945}
}

@inproceedings{scheubleTransientLASSO2025,
  author = {Scheuble, Dominik and Ramazzina, Andrea and Holzh{\"u}ter, Hanno and Gasperini, Stefano and Peters, Steven and Tombari, Federico and Bijelic, Mario and Heide, Felix},
  title = {Transient {LASSO}: Transient Large-Scale Scene Reconstruction},
  booktitle = {SIGGRAPH Asia 2025 Conference Papers},
  articleno = {148},
  pages = {148:1--148:12},
  year = {2025},
  month = dec,
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  doi = {10.1145/3757377.3763911},
  url = {https://doi.org/10.1145/3757377.3763911}
}
'''
if not bib.endswith("\n"):
    bib += "\n"
bib += bib_add.lstrip("\n")
write("egbib_merged_20260711.bib", bib)

# Source-level consistency checks before handing off to LaTeX.
checks = {
    "README.md": [title_sb3d, title_lasso],
    "index.html": [title_sb3d, title_lasso],
    "article/4datadriven.tex": ["klinghofferShootBounce3D2025", "scheubleTransientLASSO2025"],
    "bare_jrnl.tex": ["Shoot-Bounce-3D multi-bounce LiDAR"],
    "egbib_merged_20260711.bib": ["10.1145/3757377.3763945", "10.1145/3757377.3763911"],
}
for path, needles in checks.items():
    text = read(path)
    for needle in needles:
        if text.count(needle) != 1:
            raise RuntimeError(f"{path}: expected exactly one occurrence of {needle!r}, found {text.count(needle)}")

print(f"Integrated two SIGGRAPH Asia transient papers; explorer count is {actual_count}.")
