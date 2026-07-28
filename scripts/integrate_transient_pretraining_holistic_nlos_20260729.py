#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "index.html"
ACTIVE = ROOT / "article/2active.tex"
DATA = ROOT / "article/4datadriven.tex"
BARE = ROOT / "bare_jrnl.tex"
BIB = ROOT / "egbib_merged_20260711.bib"
CANONICAL = ROOT / "egbib_20260729_transient_pretraining_holistic_nlos.bib"
NOTE = ROOT / "updates/2026-07-29-transient-pretraining-holistic-nlos-integration.md"

A_TITLE = "Real-Time and High-Fidelity Non-Line-of-Sight Imaging"
M_TITLE = "MARMOT: Masked Autoencoder for Modeling Transient Imaging"
H_TITLE = "HOLI-1-to-3: Transient-Enhanced Holistic Image-to-3D Generation"
A_DOI = "10.21203/rs.3.rs-8336286/v1"
M_DOI = "10.48550/arXiv.2506.08470"
H_DOI = "10.1109/TPAMI.2024.3463875"
A_KEY = "jiUnifiedRealTimeNLOS2026"
M_KEY = "shenMARMOT2025"
H_KEY = "shenHOLI1to3TPAMI2025"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def require_count(text: str, needle: str, expected: int, label: str) -> None:
    count = text.count(needle)
    if count != expected:
        raise RuntimeError(f"Expected {expected} occurrence(s) of {label}; found {count}: {needle!r}")


def insert_after(text: str, anchor: str, addition: str, label: str) -> str:
    require_count(text, anchor, 1, label)
    return text.replace(anchor, anchor + addition, 1)


def extract_bib_entry(text: str, key: str) -> str:
    pattern = rf"(?ms)^@\w+\{{{re.escape(key)},.*?^\}}\s*"
    matches = list(re.finditer(pattern, text))
    if len(matches) != 1:
        raise RuntimeError(f"Expected one canonical BibTeX record for {key}; found {len(matches)}")
    return matches[0].group(0).strip() + "\n"


# Establish the expected cross-artifact state and fail closed on duplicates.
readme0 = read(README)
index0 = read(INDEX)
active0 = read(ACTIVE)
data0 = read(DATA)
bare0 = read(BARE)
bib0 = read(BIB)

for title in (A_TITLE, H_TITLE):
    for path, content in ((README, readme0), (INDEX, index0), (ACTIVE, active0), (DATA, data0), (BARE, bare0), (BIB, bib0)):
        if title in content:
            raise RuntimeError(f"Refusing duplicate/partial integration: {title!r} already appears in {path}")
for doi in (A_DOI, H_DOI):
    if doi in bib0 or doi in readme0 or doi in index0:
        raise RuntimeError(f"Refusing duplicate/partial integration: {doi} already appears in a target artifact")
for key in (A_KEY, H_KEY):
    if key in active0 or key in data0 or key in bare0 or key in bib0:
        raise RuntimeError(f"Refusing duplicate/partial integration: {key} already appears in a target artifact")

# MARMOT is intentionally a cross-artifact repair: one website object and one incomplete BibTeX record exist.
require_count(index0, M_TITLE, 1, "existing MARMOT website object")
require_count(bib0, f"@misc{{{M_KEY},", 1, "existing MARMOT bibliography key")
require_count(readme0, M_TITLE, 0, "missing MARMOT README record")
require_count(data0, M_KEY, 0, "missing MARMOT survey citation")

# README: latest-additions rows and semantically placed timeline milestones.
readme = readme0
readme = readme.replace("**Update run: 28 July 2026.**", "**Update run: 29 July 2026.**", 1)
header = "| Year | Paper | Venue / Status | Why it matters |\n|------|-------|----------------|----------------|\n"
rows = (
    "| 2026 | [Real-Time and High-Fidelity Non-Line-of-Sight Imaging](https://doi.org/10.21203/rs.3.rs-8336286/v1) — Ji et al. | Research Square preprint 2026 | Introduces a unified inverse framework for both see-through-scattering-media and see-around-corner NLOS. Scale modulation and joint regularization recover hidden albedo and depth across diverse measurement settings; no final journal or conference venue was verified. |\n"
    "| 2025 | [MARMOT: Masked Autoencoder for Modeling Transient Imaging](https://arxiv.org/abs/2506.08470) — Shen et al. | arXiv 2025 | Uses a scanning-pattern mask for self-supervised pretraining on the 500,000-model TransVerse dataset, learning to complete arbitrarily sampled transients and transfer reusable features to downstream NLOS imaging tasks. |\n"
    "| 2025 | [HOLI-1-to-3: Transient-Enhanced Holistic Image-to-3D Generation](https://doi.org/10.1109/TPAMI.2024.3463875) — Shen et al. | IEEE TPAMI 47(9), 7206–7217 (2025) | Unifies LOS radiance fields and NLOS transient fields in a neural plenoptic representation; diffusion and transient priors recover both visible and invisible object geometry from a single viewpoint. |\n"
)
readme = insert_after(readme, header, rows, "README latest-additions header")
anchor_2025 = "2025 ── Shi et al.: fast configurable transient simulation and an open NLOS benchmark [arXiv]\n"
readme = insert_after(
    readme,
    anchor_2025,
    "   │     Shen et al.: MARMOT shifts transient learning toward reusable masked pretraining on TransVerse, with the retained scan subset acting as arbitrary sampling [arXiv]\n"
    "   │     Shen et al.: HOLI-1-to-3 combines LOS radiance and NLOS transient fields to complete invisible 3D geometry from one viewpoint [IEEE TPAMI]\n",
    "README 2025 transient-learning milestone",
)
anchor_2026 = "2026 ── Zhao et al.: PICL — SPAD-aware denoising cascaded with self-supervised differentiable-physics reconstruction [JOSA A]\n"
readme = insert_after(
    readme,
    anchor_2026,
    "   │     Ji et al.: a unified scale-modulated, jointly regularized inverse spans through-medium and around-corner NLOS while recovering albedo and depth [Research Square preprint]\n",
    "README 2026 unified-reconstruction milestone",
)
write(README, readme)

# Website: retain the existing MARMOT object, add the two absent records, update dates and count dynamically.
index = index0
index = index.replace("Updated 28 July 2026", "Updated 29 July 2026", 1)
index = index.replace("Last updated: 28 July 2026", "Last updated: 29 July 2026", 1)
objects_anchor = "    const papers=[\n"
objects = (
    '      {cat:"latest active reconstruction unified-inverse regularization scattering corner preprint",title:"Real-Time and High-Fidelity Non-Line-of-Sight Imaging",authors:"Ji et al.",year:2026,venue:"Research Square preprint 2026",url:"https://doi.org/10.21203/rs.3.rs-8336286/v1",key:"A unified scale-modulated and jointly regularized inverse recovers albedo and depth across both through-scattering-medium and around-corner NLOS settings; no final venue has been verified."},\n'
    '      {cat:"latest learning transient-fields holistic-3d los-nlos diffusion",title:"HOLI-1-to-3: Transient-Enhanced Holistic Image-to-3D Generation",authors:"Shen et al.",year:2025,venue:"IEEE TPAMI 2025",url:"https://doi.org/10.1109/TPAMI.2024.3463875",key:"A neural plenoptic representation unifies LOS radiance fields and NLOS transient fields; diffusion and transient priors complete both visible and invisible geometry from one viewpoint."},\n'
)
index = insert_after(index, objects_anchor, objects, "website papers-array anchor")


def append_timeline_sentence(html: str, year: str, sentence: str) -> str:
    pattern = rf'(<div class="tl"><div class="year">{year}</div><div class="tl-body">.*?<p>)(.*?)(</p></div></div>)'
    matches = list(re.finditer(pattern, html, flags=re.S))
    if len(matches) != 1:
        raise RuntimeError(f"Expected one website timeline block for {year}; found {len(matches)}")
    m = matches[0]
    replacement = m.group(1) + m.group(2) + " " + sentence + m.group(3)
    return html[:m.start()] + replacement + html[m.end():]


index = append_timeline_sentence(
    index,
    "2025",
    "MARMOT made masked transient pretraining and arbitrary-scan completion reusable across downstream NLOS tasks, while HOLI-1-to-3 combined radiance and transient fields so hidden three-bounce evidence could constrain geometry invisible to a single LOS view.",
)
index = append_timeline_sentence(
    index,
    "2026",
    "A unified scale-modulated, jointly regularized inverse was proposed for both through-scattering-medium and around-corner measurements, recovering albedo and depth across scenario classes while remaining a Research Square preprint.",
)
actual_count = index.count("{cat:")
count_pattern = r"<b>\d+</b><span>tracked latest entries</span>"
if len(re.findall(count_pattern, index)) != 1:
    raise RuntimeError("Could not uniquely identify the website tracked-entry counter")
index = re.sub(count_pattern, f"<b>{actual_count}</b><span>tracked latest entries</span>", index, count=1)
write(INDEX, index)

# Active-method survey: unified cross-scenario inverse after the dimension-reduced QFT discussion.
active = active0
qft_anchor = (
    "Most fast transient inverses still allocate a three-dimensional hidden volume even when the target is effectively a surface. "
    "Wei~\\etal~represent both aggregated measurements and the hidden scene as two-dimensional functions and derive a direct Quasi-Fresnel transform between them~\\cite{weiQuasiFresnelNLOS2025}. "
    "The reduction in representation dimension lowers runtime and memory by orders of magnitude while preserving reconstruction quality, creating a route toward high-resolution active NLOS on mobile or embedded hardware.\n"
)
unified_paragraph = (
    "\n\\vspace{0.8mm}\n"
    "\\noindent \\textbf{Unified reconstruction across NLOS scenario classes.}\n"
    "Most active inverses are specialized either to time-resolved around-corner transport or to transmission through a scattering medium. Ji~\\etal~propose a single scale-modulated and jointly regularized formulation for both categories~\\cite{jiUnifiedRealTimeNLOS2026}. The method recovers hidden albedo and depth under diverse measurement patterns and is accompanied by a dataset spanning the two scenario families. This cross-scenario formulation complements operator-specific acceleration such as LCT, $f$--$k$ migration, phasor fields, and the Quasi-Fresnel transform: rather than deriving another fixed inverse for one geometry, it regularizes a broader family of forward models. The work is currently a Research Square preprint, because no final journal or conference publication could be verified.\n"
)
active = insert_after(active, qft_anchor, unified_paragraph, "Quasi-Fresnel survey paragraph")
write(ACTIVE, active)

# Data-driven survey: masked transient pretraining and NLOS-enhanced holistic shape completion.
data = data0
shared_anchor = (
    "Chen~\\etal~introduced a learned feature-embedding framework that maps transient measurements into a common hidden-scene representation and then specializes it for high-resolution image reconstruction, classification, and 2.5D object detection~\\cite{chen_learned_2020}. "
    "Rather than relying on a monolithic U-Net, the architecture incorporates differentiable modules with explicit physical roles, including transient propagation, visibility reasoning, image rendering, and depth estimation. "
    "Training on synthetically rendered diffuse and specular scenes while evaluating on measured transients demonstrated useful synthetic-to-real generalization. "
    "This work marks an early shift from single-output NLOS inversion toward reusable, task-aware representations, anticipating later physics-guided multi-task networks, transient pretraining, and transformer/operator models.\n"
)
marmot_paragraph = (
    "\n\\vspace{0.8mm}\n"
    "\\noindent \\textbf{Masked transient pretraining.}\n"
    "MARMOT moves reusable representation learning from multi-task supervision to self-supervised transient completion~\\cite{shenMARMOT2025}. A Transformer encoder--decoder receives measurements hidden by a scanning-pattern mask; the retained subset is functionally equivalent to an arbitrary relay sampling pattern, and the network predicts the complete transient volume. Pretraining on TransVerse, a synthetic collection built from 500,000 three-dimensional models, supports direct feature transfer or decoder fine-tuning for downstream NLOS tasks. This development changes the role of a large transient dataset: instead of training one reconstruction mapping, it supplies a modality-level prior that can be adapted across sampling regimes and task heads.\n"
)
data = insert_after(data, shared_anchor, marmot_paragraph, "shared-representation survey paragraph")
netf_anchor = (
    "Technically, such unsupervised learning methods~\\cite{aittalaComputationalMirrorsBlind2019,shenNonlineofsightImagingNeural2021} are not data-driven methods, but the idea of using deep neural networks to simulate matrix factorization is instructive.\n"
)
holi_paragraph = (
    "\n\\vspace{0.8mm}\n"
    "\\noindent \\textbf{From hidden reconstruction to holistic 3D completion.}\n"
    "HOLI-1-to-3 uses NLOS transients not only to reconstruct an isolated hidden scene, but to resolve the invisible side of an object observed from one conventional viewpoint~\\cite{shenHOLI1to3TPAMI2025}. Its neural plenoptic representation unifies an LOS radiance field with an NLOS transient field, and a two-stage optimization combines diffusion and transient priors to recover continuous visible and occluded geometry. Relative to NeTF, the trajectory expands from representing spherical hidden transport to fusing straight-ray and multi-bounce evidence for holistic generation; relative to purely RGB diffusion, measured transients provide physical constraints on otherwise ambiguous unseen shape.\n"
)
data = insert_after(data, netf_anchor, holi_paragraph, "NeTF survey paragraph")
write(DATA, data)

# Main-source audit marker.
bare = bare0
marker_anchor = "%% bare_jrnl.tex\n"
marker = "% 29 July 2026 citation trace: unified cross-scenario inversion, MARMOT masked transient pretraining, and HOLI-1-to-3 transient-enhanced holistic 3D integrated.\n"
bare = insert_after(bare, marker_anchor, marker, "bare_jrnl header")
write(BARE, bare)

# Consolidated bibliography: repair MARMOT and add the two absent records from canonical metadata.
canonical = read(CANONICAL)
entries = {key: extract_bib_entry(canonical, key) for key in (A_KEY, M_KEY, H_KEY)}
bib = bib0
marmot_pattern = rf"(?ms)^@\w+\{{{re.escape(M_KEY)},.*?^\}}\s*"
matches = list(re.finditer(marmot_pattern, bib))
if len(matches) != 1:
    raise RuntimeError(f"Expected one existing MARMOT BibTeX record; found {len(matches)}")
m = matches[0]
bib = bib[:m.start()] + entries[M_KEY] + "\n" + bib[m.end():]
bib = bib.rstrip() + "\n\n" + entries[A_KEY] + "\n" + entries[H_KEY]
write(BIB, bib)

write(NOTE, f"""# Transient pretraining and holistic NLOS integration — 29 July 2026

This guarded update synchronized three records across public and survey artifacts:

- Ji et al., Research Square 2026: unified reconstruction across through-medium and around-corner NLOS.
- Shen et al., arXiv 2025: MARMOT masked transient pretraining on TransVerse; the incomplete existing BibTeX record was repaired.
- Shen et al., IEEE TPAMI 2025: HOLI-1-to-3 combines LOS radiance and NLOS transient fields for holistic visible/invisible 3D completion.

The website retained its existing single MARMOT object, added exactly two new objects, and was recalculated to {actual_count} tracked entries. The accompanying workflow compiles the LaTeX survey, validates resolved citations and DOI uniqueness, extracts PDF text, and renders the first and last PDF pages before committing.
""")

print(f"Prepared synchronized transient-pretraining/holistic integration with {actual_count} website entries")
