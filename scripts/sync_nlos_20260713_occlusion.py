#!/usr/bin/env python3
"""Synchronize two missing occlusion-coded active NLOS milestones.

The edits are marker-based and idempotent. The script aborts instead of
blindly rewriting large hand-maintained files when an expected marker is
missing or ambiguous.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
THEORY_TITLE = "Exploiting Occlusion in Non-Line-of-Sight Active Imaging"
EXPERIMENT_TITLE = "Revealing hidden scenes by photon-efficient occlusion-based opportunistic active imaging"
THEORY_KEY = "thrampoulidisExploitingOcclusionNonLineofSight2018"
EXPERIMENT_KEY = "xuPhotonEfficientOcclusion2018"


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
    marker = (
        "| 2019 | [Enhancing Passive Non-Line-of-Sight Imaging Using Polarization Cues]"
        "(https://arxiv.org/abs/1911.12906) — Tanaka, Mukaigawa, Kadambi | arXiv 2019 | "
        "Adds a camera-mounted polarizer to passive NLOS capture: polarization-axis rotation makes oblique indirect "
        "paths more discriminative, improves the conditioning of the light-transport inverse problem, and enhances "
        "hidden-image recovery both with and without occluders. |\n"
    )
    additions = ""
    if THEORY_TITLE not in text:
        additions += (
            f"| 2017 | [{THEORY_TITLE}](https://arxiv.org/abs/1711.06297) — Thrampoulidis et al. | "
            "arXiv 2017 | Formalizes natural hidden-scene occluders as an active NLOS coding mechanism: the induced "
            "visibility masks improve transport-matrix conditioning and can replace picosecond time resolution for "
            "recovering static hidden reflectivity. |\n"
        )
    if EXPERIMENT_TITLE not in text:
        additions += (
            f"| 2018 | [{EXPERIMENT_TITLE}](https://doi.org/10.1364/OE.26.009945) — Xu et al. | "
            "Optics Express 2018 | Converts the occlusion-coding theory into a photon-efficient room-scale system: "
            "a binomial single-photon forward model reconstructs hidden reflectivity from non-time-resolved "
            "three-bounce counts and needs about 16× fewer detected photons than the earlier Gaussian model. |\n"
        )
    if additions:
        text = replace_once(text, marker, additions + marker, "README passive-polarization row")

    for title in (THEORY_TITLE, EXPERIMENT_TITLE):
        if text.count(title) != 1:
            raise RuntimeError(f"README should contain one {title!r} entry, found {text.count(title)}")
    write("README.md", text)


def update_homepage() -> None:
    text = read("index.html")
    marker = (
        '      {cat:"latest active",title:"Seeing Around Corners with Edge-Resolved Transient Imaging",'
        'authors:"Rapp et al.",year:2020,'
    )
    objects = ""
    if THEORY_TITLE not in text:
        objects += (
            '      {cat:"latest active occlusion",title:"Exploiting Occlusion in Non-Line-of-Sight Active Imaging",'
            'authors:"Thrampoulidis et al.",year:2017,venue:"arXiv 2017",url:"https://arxiv.org/abs/1711.06297",'
            'key:"Natural hidden-scene occluders act as spatial codes that improve the conditioning of active NLOS '
            'light transport and can remove the need for ultrafast time-resolved measurements."},\n'
        )
    if EXPERIMENT_TITLE not in text:
        objects += (
            '      {cat:"latest active occlusion hardware",title:"Revealing hidden scenes by photon-efficient '
            'occlusion-based opportunistic active imaging",authors:"Xu et al.",year:2018,venue:"Optics Express 2018",'
            'url:"https://doi.org/10.1364/OE.26.009945",key:"A binomial single-photon model and natural occluder '
            'recover meter-scale hidden reflectivity from non-time-resolved three-bounce counts with roughly 16× '
            'fewer detected photons than the prior Gaussian treatment."},\n'
        )
    if objects:
        text = replace_once(text, marker, objects + marker, "homepage edge-resolved paper object")

    count_re = re.compile(r'<b>(\d+)</b><span>tracked latest entries</span>')
    matches = count_re.findall(text)
    if len(matches) != 1:
        raise RuntimeError(f"Expected one homepage tracked-entry count, found {len(matches)}")
    current = int(matches[0])
    if current not in (92, 93, 94):
        raise RuntimeError(f"Unexpected homepage count {current}")
    text = count_re.sub('<b>94</b><span>tracked latest entries</span>', text, count=1)

    old_2017 = (
        '      <div class="tl"><div class="year">2017</div><div class="tl-body"><strong>Occlusion-aware active '
        'NLOS models</strong><p>Partial occluders, surface normals, and natural hidden-scene occluders became useful '
        'constraints rather than nuisances.</p></div></div>'
    )
    new_2017 = (
        '      <div class="tl"><div class="year">2017</div><div class="tl-body"><strong>Natural-occluder coding '
        'and occlusion-aware active NLOS</strong><p>Partial occluders, surface normals, and a formal visibility-mask '
        'model showed that hidden-scene occlusion can improve transport conditioning and enable static reconstruction '
        'without picosecond time resolution.</p></div></div>'
    )
    if "Natural-occluder coding and occlusion-aware active NLOS" not in text:
        text = replace_once(text, old_2017, new_2017, "homepage 2017 timeline")

    old_2018 = (
        '      <div class="tl"><div class="year">2018</div><div class="tl-body"><strong>Confocal LCT and '
        'virtual-wave thinking</strong><p>Light-cone transform and phasor-field formulations made NLOS reconstruction '
        'faster and more wave-optics aware.</p></div></div>'
    )
    new_2018 = (
        '      <div class="tl"><div class="year">2018</div><div class="tl-body"><strong>Confocal LCT, virtual '
        'waves, and photon-efficient occlusion imaging</strong><p>Light-cone transform and phasor-field formulations '
        'accelerated transient inversion, while room-scale experiments showed that natural occluders and a '
        'single-photon likelihood can recover hidden reflectivity from integrated, non-time-resolved returns.</p></div></div>'
    )
    if "photon-efficient occlusion imaging" not in text:
        text = replace_once(text, old_2018, new_2018, "homepage 2018 timeline")

    for title in (THEORY_TITLE, EXPERIMENT_TITLE):
        if text.count(title) != 1:
            raise RuntimeError(f"Homepage should contain one {title!r} object, found {text.count(title)}")
    if '<b>94</b><span>tracked latest entries</span>' not in text:
        raise RuntimeError("Homepage tracked-entry count did not update to 94")
    write("index.html", text)


def update_survey() -> None:
    text = read("article/2active.tex")

    legacy_table_key = ",thrampoulidisExploitingOcclusionNonLineofSight2018"
    if legacy_table_key in text:
        text = text.replace(legacy_table_key, "", 1)

    table_marker = r'''    \cite{chanNonlineofsightTrackingPeople2017a}(long range),\cite{caramazzaNeuralNetworkIdentification2017,musarraDetectionIdentificationTracking2019}(single point) & Pulsed laser & SPAD & Time of fight &  Detection/ Tracking/ Identification\\%%%% Table body
'''
    table_row = r'''    \cite{thrampoulidisExploitingOcclusionNonLineofSight2018,xuPhotonEfficientOcclusion2018} & Pulsed laser & SPAD & Integrated photon counts and occlusion & 2D reflectivity reconstruction\\%%%% Table body
'''
    if table_row not in text:
        text = replace_once(text, table_marker, table_row + table_marker, "active-system tracking row")

    old_paragraph = r'''\vspace{0.8mm}
\noindent \textbf{Occlusion-based active NLOS imaging model}
For the occlusion-based imaging model, all that needs to be done is to add the visible item $V(\mu,\mu',s)$ to the imaging model, which means the occlusion relationship between $(\mu,s)$ and $(\mu',s)$. Generally, $V(\mu,\mu',s)$ is a boolean variable, i.e., $V(\mu,\mu',s)=0$ if and only if there is no occlusion, otherwise $V(\mu,\mu',s)=1$~\cite{thrampoulidisExploitingOcclusionNonLineofSight2018}. In the study with partial occlusion, the value of $V(\mu,\mu',s)$ is allowed to be continuous~\cite{heideNonlineofsightImagingPartial2017}. An interesting but predictable fact in NLOS imaging is that the occlusion term $V(\mu,\mu',s)$ can be unified into the optical transport matrix $\mathbf{A}$ and reduce the condition number, which is helpful for reconstruction.
'''
    new_paragraph = r'''\vspace{0.8mm}
\noindent \textbf{Occlusion-based active NLOS imaging model}
For the occlusion-based imaging model, a visibility term $V(\mu,\mu',s)$ describes whether the illumination and observation paths connecting relay-wall points to a hidden point remain unblocked. Thrampoulidis~\etal~showed that the binary masks cast by natural hidden-scene occluders make the rows of the optical transport matrix substantially more diverse, improve its conditioning, and can therefore replace fine time-of-flight resolution when recovering a static hidden reflectivity map~\cite{thrampoulidisExploitingOcclusionNonLineofSight2018}. Partial-occlusion formulations further allow $V(\mu,\mu',s)$ to vary continuously while jointly estimating surface geometry and normals~\cite{heideNonlineofsightImagingPartial2017}.

Xu~\etal~translated this principle into a photon-efficient room-scale experiment~\cite{xuPhotonEfficientOcclusion2018}. Their forward model accounts for three-bounce attenuation, known occluder geometry, background light, and the binomial statistics of a non-photon-number-resolving SPAD. By integrating the third-bounce detections rather than using their arrival-time structure, the system reconstructs two-dimensional hidden-wall reflectivity with roughly sixteen times fewer detected photons than the preceding Gaussian-noise treatment. This branch of active NLOS thus established environmental occlusion as a computational aperture rather than merely a nuisance and anticipated later edge-resolved and passive computational-periscopy methods.
'''
    if "translated this principle into a photon-efficient room-scale experiment" not in text:
        text = replace_once(text, old_paragraph, new_paragraph, "occlusion-model paragraph")

    for key in (THEORY_KEY, EXPERIMENT_KEY):
        if text.count(f"\\cite{{{key}}}") < 1 and key not in table_row:
            raise RuntimeError(f"Survey did not cite {key}")
    if EXPERIMENT_KEY not in text or THEORY_KEY not in text:
        raise RuntimeError("Survey occlusion citations are incomplete")
    write("article/2active.tex", text)


def main() -> None:
    bib = read("egbib_20260713_occlusion_updates.bib")
    required = (THEORY_KEY, EXPERIMENT_KEY, "10.1364/OE.26.009945", "1711.06297")
    for token in required:
        if token not in bib:
            raise RuntimeError(f"Canonical occlusion bibliography is missing {token}")
    update_readme()
    update_homepage()
    update_survey()
    print("Synchronized occlusion-coded active NLOS milestones across public artifacts and survey sources.")


if __name__ == "__main__":
    main()
