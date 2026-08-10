from pathlib import Path

TITLE = "Non-line-of-sight multi-person pose sensing"
DOI = "10.1364/OE.570120"
KEY = "houMultiPersonPose2025"
DATE = "11 August 2026"


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def insert_after_once(text, anchor, addition, label):
    if anchor not in text:
        raise RuntimeError(f"missing {label} anchor")
    return text.replace(anchor, anchor + addition, 1)


def patch_readme():
    path = "README.md"
    text = read(path)
    text = text.replace("**Update run: 9 August 2026.**", f"**Update run: {DATE}.**", 1)
    if TITLE not in text:
        latest_row = (
            "\n| 2025 | [Non-line-of-sight multi-person pose sensing](https://doi.org/10.1364/OE.570120) — Hou et al. | "
            "Optics Express 33(20), 41937–41950 (2025) | Introduces AMPE-NLOS, the first adaptive multi-person 3D pose/mesh sensing framework for active transient NLOS: LCT supplies coarse volumetric features, a 3D U-Net refines them, and body-center-guided SMPL parameter sampling separates a variable number of hidden people. The paper validates on simulation and a self-built confocal laser/SPAD system. |"
        )
        latest_start = text.index("## Latest Additions")
        latest_end = text.index("\n---", latest_start)
        sep = "|------|-------|----------------|----------------|"
        pos = text.index(sep, latest_start, latest_end) + len(sep)
        text = text[:pos] + latest_row + text[pos:]

        main_row = (
            "| 2025 | [Non-line-of-sight multi-person pose sensing](https://doi.org/10.1364/OE.570120) - Hou et al. | "
            "Optics Express 33(20), 41937–41950 (2025) | Extends transient NLOS semantics from single-person pose to adaptive multi-person 3D mesh recovery. AMPE-NLOS combines LCT-propagated coarse features, 3D U-Net refinement, body-center heatmaps, and SMPL parameter maps; simulated and measured confocal SPAD experiments cover varying hidden-person counts. |\n"
        )
        anchor = "| 2026 | [Non-line-of-sight human pose estimation](https://doi.org/10.1016/j.optlaseng.2026.109658) - Xiao et al."
        idx = text.find(anchor)
        if idx < 0:
            raise RuntimeError("README human-pose catalog anchor not found")
        text = text[:idx] + main_row + text[idx:]

        timeline_anchor = "   |     Xiao et al.: semantic human-pose recovery extends active transients beyond shape reconstruction [Optics and Lasers in Engineering]"
        timeline_line = "   |     Hou et al.: AMPE-NLOS extends active transient semantics to adaptive multi-person 3D body-center and SMPL mesh recovery [Optics Express]\n"
        idx = text.find(timeline_anchor)
        if idx < 0:
            raise RuntimeError("README human-pose timeline anchor not found")
        text = text[:idx] + timeline_line + text[idx:]
    write(path, text)


def patch_index():
    path = "index.html"
    text = read(path)
    text = text.replace("Updated 9 August 2026 · 210+ papers", f"Updated {DATE} · 210+ papers", 1)
    text = text.replace("Last updated: 8 August 2026", f"Last updated: {DATE}", 1)
    if TITLE not in text:
        text = text.replace('<div class="stat"><b>274</b><span>tracked latest entries</span></div>', '<div class="stat"><b>275</b><span>tracked latest entries</span></div>', 1)
        line_anchor = '{cat:"latest active semantics",title:"Non-line-of-sight human pose estimation",authors:"Xiao et al.",year:2026'
        idx = text.find(line_anchor)
        if idx < 0:
            raise RuntimeError("index paper-object anchor not found")
        line_start = text.rfind("\n", 0, idx) + 1
        hou_obj = (
            '      {cat:"latest active learning semantics human pose",title:"Non-line-of-sight multi-person pose sensing",authors:"Hou et al.",year:2025,'
            'venue:"Optics Express 33(20), 41937–41950 (2025)",url:"https://doi.org/10.1364/OE.570120",'
            'key:"AMPE-NLOS is the first adaptive multi-person 3D pose/mesh sensing framework for active transient NLOS, coupling LCT coarse features with 3D U-Net refinement, body-center heatmaps, and SMPL parameter maps; simulation and a self-built confocal laser/SPAD system validate variable-person hidden scenes."},\n'
        )
        text = text[:line_start] + hou_obj + text[line_start:]

        timeline_anchor = "AME-Net and NLOS-Action moved ordinary-camera passive sensing from hidden-image recovery toward robust hidden-action recognition from subtle relay-wall motion."
        addition = " Hou et al. extended active transient semantics from single-person pose to adaptive multi-person 3D mesh sensing with LCT-guided AMPE-NLOS and measured confocal laser/SPAD data."
        if timeline_anchor not in text:
            raise RuntimeError("index 2025 timeline anchor not found")
        text = text.replace(timeline_anchor, timeline_anchor + addition, 1)
    write(path, text)


def patch_article():
    path = "article/5newscenes.tex"
    text = read(path)
    if KEY not in text:
        anchor = r" \href{https://arxiv.org/abs/2003.14414}{Isogawa~\etal} introduced an optical NLOS physics-based 3D human-pose-estimation pipeline"
        idx = text.find(anchor)
        if idx < 0:
            raise RuntimeError("survey human-pose insertion anchor not found")
        paragraph = (
            "\n\n\\vspace{0.8mm}\n"
            "\\noindent \\textbf{Adaptive multi-person pose and mesh sensing.}\n"
            "Hou~\\etal~extend active transient semantics from single-person pose recovery to scenes containing an unknown number of hidden people~\\cite{houMultiPersonPose2025}. Their AMPE-NLOS pipeline propagates transient features with LCT to obtain a coarse physical 3D representation, refines it with a 3D U-Net, and predicts both a body-center heatmap and an SMPL parameter map. Body-center-guided sampling then associates mesh parameters with individual people, enabling adaptive multi-person 3D mesh regression. Simulated training data and measurements from a self-built confocal pulsed-laser/SPAD system demonstrate a trajectory in which NLOS reconstruction becomes a front end for structured, multi-instance human understanding rather than only hidden geometry or single-person joints.\n"
        )
        text = text[:idx] + paragraph + text[idx:]
    write(path, text)


def patch_bib():
    path = "egbib_merged_20260711.bib"
    text = read(path)
    if f"@article{{{KEY}," not in text:
        entry = r'''

@article{houMultiPersonPose2025,
  author = {Hou, Yusen and Cui, Xingyu and Sun, Shida and Li, Yue and Huang, Jing and Lu, Zhi and Li, Kun and Xiong, Zhiwei and Yang, Jingyu},
  title = {Non-line-of-sight multi-person pose sensing},
  journal = {Optics Express},
  volume = {33},
  number = {20},
  pages = {41937--41950},
  year = {2025},
  publisher = {Optica Publishing Group},
  doi = {10.1364/OE.570120},
  url = {https://doi.org/10.1364/OE.570120}
}
'''
        text = text.rstrip() + entry + "\n"
    write(path, text)


def patch_master_tex():
    path = "bare_jrnl.tex"
    text = read(path)
    comment = "% 11 August 2026 citation trace: adaptive multi-person transient NLOS pose/mesh sensing integrated with final Optics Express metadata.\n"
    if not text.startswith(comment):
        text = comment + text
    text = text.replace("through 9 August 2026", "through 11 August 2026", 1)
    write(path, text)


def patch_note():
    path = Path("updates/2026-08-11-hou-multiperson-pose.md")
    if path.exists():
        return
    path.write_text(
        "# 11 August 2026 citation-trace update: adaptive multi-person transient NLOS pose sensing\n\n"
        "Integrated Yusen Hou, Xingyu Cui, Shida Sun, Yue Li, Jing Huang, Zhi Lu, Kun Li, Zhiwei Xiong, and Jingyu Yang, "
        "*Non-line-of-sight multi-person pose sensing*, Optics Express 33(20), 41937–41950 (2025), DOI `10.1364/OE.570120`. "
        "This is a high-confidence forward-citation hit because the paper explicitly builds its physical feature stage on LCT, phasor-field, and f-k NLOS reconstruction lineages. "
        "AMPE-NLOS extends transient semantic sensing from single-person pose to adaptive multi-person 3D mesh recovery using LCT coarse features, 3D U-Net refinement, body-center heatmaps, and SMPL parameter maps, with both simulated and measured confocal laser/SPAD validation.\n\n"
        "The update is synchronized across README, website explorer/timeline, survey prose, merged BibTeX, and the rebuilt survey PDF.\n",
        encoding="utf-8",
    )


def validate():
    readme = read("README.md")
    index = read("index.html")
    article = read("article/5newscenes.tex")
    bib = read("egbib_merged_20260711.bib")
    master = read("bare_jrnl.tex")
    assert readme.count(TITLE) >= 2
    assert DOI in readme
    assert f"**Update run: {DATE}.**" in readme
    assert index.count(TITLE) == 1
    assert '<div class="stat"><b>275</b><span>tracked latest entries</span></div>' in index
    assert f"Updated {DATE}" in index
    assert KEY in article and "Adaptive multi-person pose and mesh sensing" in article
    assert bib.count(f"@article{{{KEY},") == 1 and DOI in bib
    assert "through 11 August 2026" in master
    assert Path("updates/2026-08-11-hou-multiperson-pose.md").is_file()


if __name__ == "__main__":
    patch_readme()
    patch_index()
    patch_article()
    patch_bib()
    patch_master_tex()
    patch_note()
    validate()
    print("Hou et al. multi-person NLOS pose integration passed source validation.")
