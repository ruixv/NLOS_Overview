from pathlib import Path

DOI = "10.1364/OL.530066"
BIBKEY = "zhuEfficientNeuromorphicNLOSTracking2024"


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    if DOI in text:
        return

    text = replace_once(
        text,
        "**Update run: 20 July 2026.**",
        "**Update run: 21 July 2026.**",
        "README update date",
    )
    header = "| Year | Paper | Venue / Status | Why it matters |\n|------|-------|----------------|----------------|\n"
    row = (
        "| 2024 | [Efficient non-line-of-sight tracking with computational neuromorphic imaging]"
        "(https://doi.org/10.1364/OL.530066) — Zhu et al. | Optics Letters 2024 | "
        "Uses an event camera to retain only motion-induced changes in dynamic NLOS speckle, suppressing static relay/background redundancy and enabling direct, efficient hidden-target motion estimation without first reconstructing a complete hidden scene. |\n"
    )
    text = replace_once(text, header, header + row, "README latest table")

    timeline_anchor = (
        "   │     Pueyo-Ciutad et al.: time-gated polarization — picosecond polarimetric transport reduces the missing cone and recovers directionally ambiguous hidden surfaces [SIGGRAPH Asia]\n"
    )
    timeline_line = (
        "   │     Zhu et al.: computational neuromorphic NLOS tracking — event streams isolate motion-induced speckle changes for direct hidden-target motion estimation [Optics Letters]\n"
    )
    text = replace_once(text, timeline_anchor, timeline_anchor + timeline_line, "README 2024 timeline")
    write(path, text)


def update_index() -> None:
    path = "index.html"
    text = read(path)
    if DOI in text:
        return

    text = text.replace("Updated 20 July 2026", "Updated 21 July 2026")
    text = text.replace("Last updated: 19 July 2026", "Last updated: 21 July 2026")
    text = replace_once(text, '<div class="stat"><b>174</b><span>tracked latest entries</span></div>', '<div class="stat"><b>175</b><span>tracked latest entries</span></div>', "website count")

    array_anchor = "    const papers=[\n"
    paper = (
        '      {cat:"latest modality tracking event-camera",title:"Efficient non-line-of-sight tracking with computational neuromorphic imaging",'
        'authors:"Zhu, Ge, Wang, Han, Lam",year:2024,venue:"Optics Letters 2024",url:"https://doi.org/10.1364/OL.530066",'
        'key:"Uses an event camera to capture non-redundant motion-induced changes in dynamic NLOS speckle, suppressing static relay/background interference and directly estimating hidden-target motion without full scene reconstruction."},\n'
    )
    text = replace_once(text, array_anchor, array_anchor + paper, "website paper array")

    old = "Parallel SPAD-array acquisition removed relay-wall raster scanning at 19 fps, while event-enhanced passive sensing exploited neuromorphic motion cues."
    new = old + " Computational neuromorphic tracking further used event streams from dynamic speckle to estimate hidden motion directly while rejecting static relay and background redundancy."
    text = replace_once(text, old, new, "website 2024 timeline")
    write(path, text)


def update_survey() -> None:
    path = "article/5newscenes.tex"
    text = read(path)
    if BIBKEY in text:
        return

    anchor = (
        "A newer line of work relaxes the need for dense multi-position illumination by turning a visible corner into a structured sensing device. "
        "\\href{https://www.nature.com/articles/s41467-023-39327-2}{Seidel~\\etal} demonstrated an active corner camera that models the complete optical response of a visible corner and reconstructs both moving foreground objects and stationary hidden background geometry from NLOS snapshots. "
        "This direction is important because it moves NLOS imaging closer to deployed corner-mounted sensing: the system no longer only recovers a single isolated object, but can also maintain a background map of the hidden space while monitoring dynamic foreground changes.\n"
    )
    addition = r'''

\bookmark[dest=\HyperLocalCurrentHref,level=2]{Neuromorphic NLOS Tracking}
\subsection{Neuromorphic NLOS Tracking}
Dynamic hidden-scene sensing does not always require reconstructing a complete albedo or geometry volume. Zhu~\etal~introduced computational neuromorphic NLOS tracking, using an event camera to respond selectively to motion-induced changes in the dynamic speckle field~\cite{zhuEfficientNeuromorphicNLOSTracking2024}. Because static relay-surface and background contributions generate few events, the event stream provides a compact, non-redundant representation for direct motion estimation. This work complements frame-based passive event-camera reconstruction and transient NLOS videography by establishing an event-driven task branch focused on efficient hidden-target tracking rather than full-scene recovery.
'''
    text = replace_once(text, anchor, anchor + addition, "survey active-corner anchor")
    write(path, text)


def update_master() -> None:
    path = "bare_jrnl.tex"
    text = read(path)
    marker = "% 21 July 2026 citation trace integrates computational neuromorphic event-camera NLOS tracking."
    if marker in text:
        return
    anchor = "% 20 July 2026 core-paper citation follow-up integrates accurate transport modeling, a cohesive operator framework, zero-phase phasor fields, and the ICCV virtual-transport-matrix record.\n"
    text = replace_once(text, anchor, anchor + marker + "\n", "master integration marker")
    write(path, text)


def update_bib() -> None:
    path = "egbib_merged_20260711.bib"
    text = read(path)
    if BIBKEY in text or DOI.lower() in text.lower():
        return
    entry = r'''

@article{zhuEfficientNeuromorphicNLOSTracking2024,
  author    = {Zhu, Shuo and Ge, Zhou and Wang, Chutian and Han, Jing and Lam, Edmund Y.},
  title     = {Efficient non-line-of-sight tracking with computational neuromorphic imaging},
  journal   = {Optics Letters},
  year      = {2024},
  volume    = {49},
  number    = {13},
  pages     = {3584--3587},
  doi       = {10.1364/OL.530066},
  url       = {https://doi.org/10.1364/OL.530066},
  publisher = {Optica Publishing Group}
}
'''
    write(path, text.rstrip() + entry + "\n")


def validate_sources() -> None:
    required = {
        "README.md": DOI,
        "index.html": DOI,
        "article/5newscenes.tex": BIBKEY,
        "bare_jrnl.tex": "21 July 2026 citation trace",
        "egbib_merged_20260711.bib": BIBKEY,
    }
    for path, token in required.items():
        text = read(path)
        if token not in text:
            raise RuntimeError(f"missing {token!r} in {path}")
    if read("egbib_merged_20260711.bib").count(BIBKEY) != 1:
        raise RuntimeError("bibliography key is missing or duplicated")
    if read("README.md").count(DOI) != 1:
        raise RuntimeError("README DOI is missing or duplicated")
    if read("index.html").count(DOI) != 1:
        raise RuntimeError("website DOI is missing or duplicated")


def main() -> None:
    update_readme()
    update_index()
    update_survey()
    update_master()
    update_bib()
    validate_sources()


if __name__ == "__main__":
    main()
