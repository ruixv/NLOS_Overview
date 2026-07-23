#!/usr/bin/env python3
"""Fail-closed synchronization of the phasor-field theory lineage and venue audit."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MARKER = "% 23 July 2026 citation trace: phasor-field theory lineage and scattering-media final venues integrated."
DOIS = (
    "10.1364/OE.27.018016",
    "10.1364/OE.27.032587",
    "10.1364/OE.396577",
    "10.1364/OE.401203",
    "10.1364/OL.463296",
)
KEYS = (
    "doveParaxialTheoryPhasor2019",
    "rezaPhasorFieldExperimental2019",
    "doveParaxialPhysicalOptics2020",
    "doveNonparaxialPhasor2020",
)
SCATTERING_KEY = "luesiaScatteringPhasor2023"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return text.replace(old, new, 1)


def regex_once(text: str, pattern: str, repl, label: str, flags: int = 0) -> str:
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}")
    return out


def integrated() -> bool:
    if MARKER not in read("bare_jrnl.tex"):
        return False
    expected = {
        "README.md": DOIS,
        "index.html": DOIS,
        "article/2active.tex": KEYS,
        "article/5newscenes.tex": (SCATTERING_KEY,),
    }
    missing: list[str] = []
    for path, needles in expected.items():
        text = read(path)
        if any(needle not in text for needle in needles):
            missing.append(path)
    if missing:
        raise RuntimeError("Partial phasor-lineage integration: " + ", ".join(missing))
    return True


def update_readme() -> None:
    text = read("README.md")
    replacements = {
        "| 2020 | [Nonparaxial phasor-field propagation](https://arxiv.org/abs/2006.13775) — Dove, Shapiro | arXiv 2020 | Extends phasor-field propagation beyond the Fresnel/paraxial assumption using Rayleigh--Sommerfeld theory, closer to wide-angle reflective NLOS geometries. |":
        "| 2020 | [Nonparaxial phasor-field propagation](https://doi.org/10.1364/OE.401203) — Dove, Shapiro | Optics Express 2020 | Replaces the paraxial Fresnel assumption with Rayleigh--Sommerfeld propagation for both the phasor field and the two-frequency spatial Wigner distribution, extending virtual-wave analysis toward wide-angle reflective NLOS geometries. |",
        "| 2020 | [Paraxial phasor-field physical optics](https://arxiv.org/abs/2004.14239) — Dove, Shapiro | arXiv 2020 | Shows that ordinary lenses can focus or project phasor fields through diffusers, bridging computational virtual-wave NLOS and physical P-field optics. |":
        "| 2020 | [Paraxial phasor-field physical optics](https://doi.org/10.1364/OE.396577) — Dove, Shapiro | Optics Express 2020 | Proves that ordinary lenses can physically focus and project phasor fields through intervening diffusers, linking computational virtual-wave NLOS to physical P-field optical systems. |",
        "| 2019 | [Wave-like Properties of Phasor Fields: Experimental Demonstrations](https://arxiv.org/abs/1904.01565) — Reza et al. | arXiv 2019 | Experimentally validates wave-like phasor-field behavior and introduces P-field optical elements for practical virtual-wave NLOS systems. |":
        "| 2019 | [Phasor field waves: experimental demonstrations of wave-like properties](https://doi.org/10.1364/OE.27.032587) — Reza et al. | Optics Express 2019 | Demonstrates P-field interference, independent focusing, and imaging with a modulated source and detector, validating the virtual-wave model and motivating computation-light NLOS optical systems. |",
        "| 2019 | [Paraxial Theory of Phasor-Field Imaging](https://arxiv.org/abs/1903.02365) — Dove, Shapiro | arXiv 2019 | Provides a paraxial wave-optics and Wigner-distribution analysis of phasor-field imaging, clarifying which occluded and unoccluded geometries are supported by virtual-wave NLOS models. |":
        "| 2019 | [Paraxial theory of phasor-field imaging](https://doi.org/10.1364/OE.27.018016) — Dove, Shapiro | Optics Express 2019 | Formalizes paraxial phasor-field imaging and introduces two-frequency spatial-Wigner propagation primitives that retain occlusion and specular information not represented by the P-field alone. |",
        "| 2023 | [Non-line-of-sight imaging in the presence of scattering media using phasor fields](https://arxiv.org/abs/2311.09223) — Luesia et al. | arXiv 2023 | Extends phasor-field NLOS analysis to hidden scenes submerged in scattering media, empirically testing robustness under fog/smoke-like volumetric scattering. |":
        "| 2022 | [Non-line-of-sight imaging in the presence of scattering media using phasor fields](https://doi.org/10.1364/OL.463296) — Luesia et al. | Optics Letters 2022 | Tests phasor-field reconstruction for synthetic and measured hidden scenes submerged in volumetric scattering, extending surface-only NLOS toward fog-, smoke-, and diffuse-optical-tomography-like regimes. |",
    }
    for old, new in replacements.items():
        text = replace_once(text, old, new, f"README venue correction for {old.split(']')[0]}")

    anchor_2019 = "2019 ── Tsai et al.: Beyond Volumetric Albedo — direct hidden-surface and reflectance optimization [CVPR]"
    addition_2019 = (
        "\n   │     Dove and Shapiro: paraxial phasor-field theory — TFSWD propagation formalizes occlusions and specular transport beyond the P-field alone [Optics Express]"
        "\n   │     Reza et al.: experimental phasor-field waves — interference and independent optical/P-field focusing validate the virtual-wave picture [Optics Express]"
    )
    text = replace_once(text, anchor_2019, anchor_2019 + addition_2019, "README 2019 phasor milestones")

    anchor_2020 = "2020 ── Iseringhausen & Hullin: physically based transient analysis-by-synthesis — surface-, BRDF-, and visibility-aware NLOS inverse rendering [ACM TOG]"
    addition_2020 = (
        "\n   │     Dove and Shapiro: physical and nonparaxial phasor optics — ordinary lenses manipulate P-fields and Rayleigh--Sommerfeld theory extends them beyond Fresnel geometry [Optics Express]"
    )
    text = replace_once(text, anchor_2020, anchor_2020 + addition_2020, "README 2020 phasor milestone")

    anchor_2022 = "   │     Li et al.: time-sequential first-photon stamping — detection-aware acquisition reduces photon collection time for active transient NLOS [Optics Letters]"
    scattering_milestone = "   │     Luesia et al.: scattering-media phasor fields — virtual-wave reconstruction remains effective for hidden scenes immersed in thick volumetric scattering [Optics Letters]"
    text = replace_once(text, anchor_2022, anchor_2022 + "\n" + scattering_milestone, "README 2022 scattering milestone")
    write("README.md", text)


def update_index() -> None:
    text = read("index.html")
    text = replace_once(
        text,
        '<b>186</b><span>tracked latest entries</span>',
        '<b>191</b><span>tracked latest entries</span>',
        "homepage tracked-paper count",
    )
    papers = """      {cat:"latest active theory phasor wave optics",title:"Paraxial theory of phasor-field imaging",authors:"Dove and Shapiro",year:2019,venue:"Optics Express 2019",url:"https://doi.org/10.1364/OE.27.018016",key:"Formalizes paraxial P-field propagation and introduces two-frequency spatial-Wigner primitives for hidden-space occlusions and specularities that the P-field alone cannot represent."},
      {cat:"latest active theory experimental phasor",title:"Phasor field waves: experimental demonstrations of wave-like properties",authors:"Reza et al.",year:2019,venue:"Optics Express 2019",url:"https://doi.org/10.1364/OE.27.032587",key:"Experimentally demonstrates P-field interference, focusing, and imaging, connecting computational virtual waves to direct modulated-source and detector implementations."},
      {cat:"latest active theory hardware phasor",title:"Paraxial phasor-field physical optics",authors:"Dove and Shapiro",year:2020,venue:"Optics Express 2020",url:"https://doi.org/10.1364/OE.396577",key:"Proves that ordinary lenses can focus and project P-fields through diffusers, suggesting physical-optics NLOS systems with reduced computational burden."},
      {cat:"latest active theory phasor nonparaxial",title:"Nonparaxial phasor-field propagation",authors:"Dove and Shapiro",year:2020,venue:"Optics Express 2020",url:"https://doi.org/10.1364/OE.401203",key:"Derives Rayleigh--Sommerfeld propagation for P-fields and TFSWDs, relaxing the Fresnel approximation for wide-angle reflective NLOS geometries."},
      {cat:"latest active modality phasor scattering",title:"Non-line-of-sight imaging in the presence of scattering media using phasor fields",authors:"Luesia et al.",year:2022,venue:"Optics Letters 2022",url:"https://doi.org/10.1364/OL.463296",key:"Evaluates phasor-field reconstruction for synthetic and measured hidden scenes immersed in volumetric scattering, connecting surface NLOS with diffuse optical tomography."},"""
    text = regex_once(
        text,
        r"(?m)^(\s*const papers=\[\s*)$",
        lambda m: m.group(1) + "\n" + papers,
        "homepage paper array",
    )

    def append_timeline(year: int, addition: str) -> None:
        nonlocal text
        pattern = rf'(<div class="tl"><div class="year">{year}</div>.*?<p>)(.*?)(</p></div></div>)'
        match = re.search(pattern, text, flags=re.S)
        if not match:
            raise RuntimeError(f"Missing homepage {year} timeline")
        if addition.strip() in match.group(2):
            raise RuntimeError(f"Homepage {year} addition already exists")
        text = text[:match.start()] + match.group(1) + match.group(2).rstrip() + addition + match.group(3) + text[match.end():]

    append_timeline(2019, " Dove and Shapiro supplied the paraxial TFSWD theory needed to retain occlusion and specular transport, while Reza et al. experimentally demonstrated P-field interference, focusing, and imaging.")
    append_timeline(2020, " Physical-optics and nonparaxial extensions then showed that ordinary lenses can manipulate P-fields and that Rayleigh--Sommerfeld propagation is needed outside the Fresnel regime.")
    append_timeline(2022, " Luesia et al. further tested phasor-field reconstruction when the hidden scene is immersed in volumetric scattering, connecting around-corner imaging with diffuse optical tomography.")
    write("index.html", text)


def update_active() -> None:
    text = read("article/2active.tex")
    anchor = (
        "The phasor field methods\\cite{rezaPhasorFieldWaves2019,liuPhasorFieldDiffraction2020,liuVirtualWaveOptics2018}, which have attracted widespread attention recently, regard the NLOS imaging as a diffraction-based LOS (line-of-sight) optical imaging problem. The projector function and diffraction function are determined by selecting a suitable LOS template, thereby directly reconstructing the hidden scene. Although based on wave propagation, these methods are all suitable for ToF measurement, making it easy to collect data and apply the model to public NLOS imaging datasets."
    )
    paragraph = (
        "\n\n\\vspace{0.8mm}\n"
        "\\noindent \\textbf{From paraxial theory to physical and nonparaxial phasor optics.}\n"
        "Dove and Shapiro formalized phasor-field imaging under paraxial wave optics and introduced two-frequency spatial-Wigner-distribution (TFSWD) propagation primitives to carry directional information associated with occlusion and specular transport that is not represented by the P-field alone~\\cite{doveParaxialTheoryPhasor2019}. Reza~\\etal~then experimentally demonstrated P-field interference, focusing, and imaging with modulated optical sources and detectors, validating that the virtual-wave analogy is observable rather than only a post-processing construction~\\cite{rezaPhasorFieldExperimental2019}. Two subsequent results extended this foundation in complementary directions: ordinary lenses were shown to physically focus and project P-fields through intervening diffusers~\\cite{doveParaxialPhysicalOptics2020}, while Rayleigh--Sommerfeld formulas for both P-fields and TFSWDs relaxed the Fresnel approximation for wide-angle reflective NLOS geometries~\\cite{doveNonparaxialPhasor2020}. Together, this lineage connects Liu's computational phasor-field camera to a broader physical-optics and phase-space account of what virtual waves preserve, how they propagate, and where paraxial reconstruction ceases to be valid."
    )
    text = replace_once(text, anchor, anchor + paragraph, "phasor-field theory lineage paragraph")
    write("article/2active.tex", text)


def update_new_scenes() -> None:
    text = read("article/5newscenes.tex")
    old = "Most active optical NLOS models assume that light propagates through free space and scatters only at surfaces. Luesia~\\etal~study a harder regime"
    new = "Most active optical NLOS models assume that light propagates through free space and scatters only at surfaces. In their final Optics Letters study, Luesia~\\etal~consider a harder regime"
    text = replace_once(text, old, new, "scattering-media final-venue wording")
    write("article/5newscenes.tex", text)


def update_master() -> None:
    text = read("bare_jrnl.tex")
    text = regex_once(
        text,
        r"(?m)^%% bare_jrnl\.tex\s*$",
        "%% bare_jrnl.tex\n" + MARKER,
        "master survey header",
    )
    if "through 23 July 2026" not in text:
        raise RuntimeError("Unexpected survey coverage date")
    write("bare_jrnl.tex", text)


def validate() -> None:
    readme = read("README.md")
    index = read("index.html")
    active = read("article/2active.tex")
    new_scenes = read("article/5newscenes.tex")
    for doi in DOIS:
        if readme.count(doi) != 1:
            raise RuntimeError(f"README expected one occurrence of {doi}")
        if index.count(doi) != 1:
            raise RuntimeError(f"index expected one occurrence of {doi}")
    for key in KEYS:
        if active.count(key) != 1:
            raise RuntimeError(f"active survey expected one occurrence of {key}")
    if new_scenes.count(SCATTERING_KEY) != 1:
        raise RuntimeError("scattering-media citation key count changed")
    if '<b>191</b><span>tracked latest entries</span>' not in index:
        raise RuntimeError("Homepage count was not updated")
    if MARKER not in read("bare_jrnl.tex"):
        raise RuntimeError("Master marker missing")
    stale = (
        "https://arxiv.org/abs/1903.02365",
        "https://arxiv.org/abs/1904.01565",
        "https://arxiv.org/abs/2004.14239",
        "https://arxiv.org/abs/2006.13775",
        "https://arxiv.org/abs/2311.09223",
    )
    if any(url in readme for url in stale):
        raise RuntimeError("README still contains a corrected preprint link")


def main() -> None:
    if integrated():
        print("Phasor-field lineage and final venues already fully integrated")
        return
    update_readme()
    update_index()
    update_active()
    update_new_scenes()
    update_master()
    validate()
    print("Phasor-field theory lineage synchronized across source artifacts")


if __name__ == "__main__":
    main()
