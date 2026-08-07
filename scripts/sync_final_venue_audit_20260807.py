from pathlib import Path
import re

ROOT = Path('.')


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, text):
    Path(path).write_text(text, encoding='utf-8')


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f'{label}: expected exactly one match, found {n}')
    return text.replace(old, new, 1)


def replace_entry_window(text, title, replacements, label, radius=1600):
    pos = text.find(title)
    if pos < 0:
        raise RuntimeError(f'{label}: title not found: {title}')
    lo = max(0, pos - radius)
    hi = min(len(text), pos + len(title) + radius)
    win = text[lo:hi]
    for old, new in replacements:
        if old not in win:
            raise RuntimeError(f'{label}: nearby token not found for {title}: {old}')
        win = win.replace(old, new, 1)
    return text[:lo] + win + text[hi:]


def bib_entry_bounds(text, title_fragment):
    matches = [m.start() for m in re.finditer(re.escape(title_fragment), text, flags=re.I)]
    if len(matches) != 1:
        raise RuntimeError(f'Bib title fragment {title_fragment!r}: expected one match, found {len(matches)}')
    pos = matches[0]
    start = text.rfind('\n@', 0, pos)
    if start < 0:
        if text.startswith('@'):
            start = 0
        else:
            start = text.rfind('@', 0, pos)
    else:
        start += 1
    if start < 0:
        raise RuntimeError(f'Could not locate BibTeX entry start for {title_fragment}')
    end = text.find('\n}\n', pos)
    if end < 0:
        if text.rstrip().endswith('}'):
            end = len(text.rstrip()) - 1
        else:
            raise RuntimeError(f'Could not locate BibTeX entry end for {title_fragment}')
    else:
        end += 3
    entry = text[start:end]
    km = re.search(r'@\w+\s*\{\s*([^,]+),', entry)
    if not km:
        raise RuntimeError(f'Could not parse BibTeX key for {title_fragment}')
    return start, end, km.group(1).strip()


def replace_bib_entry(text, title_fragment, template):
    start, end, key = bib_entry_bounds(text, title_fragment)
    new = template.format(key=key).rstrip() + '\n'
    return text[:start] + new + text[end:]


# ---------------------------------------------------------------------------
# README: final-venue reconciliation, update date, and timeline placement.
# ---------------------------------------------------------------------------
readme_path = Path('README.md')
readme = read(readme_path)
readme = replace_once(
    readme,
    '**Update run: 6 August 2026.**',
    '**Update run: 7 August 2026.**',
    'README update date',
)
readme = replace_once(
    readme,
    '| 2025 | [Dual-branch Graph Feature Learning for NLOS Imaging](https://arxiv.org/abs/2502.19683) — Su et al. | arXiv 2025 | DG-NLOS uses graph feature learning with separate albedo and depth branches to reduce 3D-grid cost while jointly reconstructing hidden appearance and geometry. |',
    '| 2025 | [Dual-branch Graph Feature Learning for NLOS Imaging](https://doi.org/10.1609/aaai.v39i7.32757) — Su et al. | AAAI 2025, 39(7), 7051–7059 | DG-NLOS converts dense transient voxels into sparse graph features and separates albedo/depth reconstruction, reducing volumetric cost while jointly recovering hidden appearance and geometry. |',
    'README DG-NLOS row',
)
readme = replace_once(
    readme,
    '| 2024 | [Enhancing Autonomous Navigation by Imaging Hidden Objects using Single-Photon LiDAR](https://arxiv.org/abs/2410.03555) — Young et al. | arXiv 2024 | Uses SPAD / single-photon LiDAR NLOS occupancy perception to guide robot navigation around occluded corners. |',
    '| 2025 | [Enhancing Autonomous Navigation by Imaging Hidden Objects Using Single-Photon LiDAR](https://doi.org/10.1109/ICRA55743.2025.11128292) — Young et al. | IEEE ICRA 2025, 4907–4914 | Integrates SPAD-based multi-bounce sensing, learned hidden-space occupancy estimation, and robot control; real L-shaped-corridor experiments demonstrate NLOS-assisted autonomous navigation around occluded obstacles. |',
    'README autonomous-navigation row',
)
readme = replace_once(
    readme,
    '| 2025 | [TransiT: Transient Transformer for Non-line-of-sight Videography](https://arxiv.org/abs/2503.11328) — Li et al. | ICCV 2025 |',
    '| 2025 | [TransiT: Transient Transformer for Non-line-of-sight Videography](https://openaccess.thecvf.com/content/ICCV2025/html/Li_TransiT_Transient_Transformer_for_Non-line-of-sight_Videography_ICCV_2025_paper.html) — Li et al. | ICCV 2025, 27542–27551 |',
    'README TransiT final link',
)
readme = replace_once(
    readme,
    '| 2023 | [NLOS-NeuS: Non-line-of-sight Neural Implicit Surface](https://arxiv.org/abs/2303.12280) — Fujimura et al. | ICCV 2023 |',
    '| 2023 | [NLOS-NeuS: Non-line-of-sight Neural Implicit Surface](https://openaccess.thecvf.com/content/ICCV2023/html/Fujimura_NLOS-NeuS_Non-line-of-sight_Neural_Implicit_Surface_ICCV_2023_paper.html) — Fujimura et al. | ICCV 2023, 10532–10541 |',
    'README NLOS-NeuS final link',
)
# Add final-venue milestones without duplicating paper rows.
timeline_anchor = '2025 ── Shi et al.: fast configurable transient simulation and an open NLOS benchmark [arXiv]\n'
if 'Su et al.: DG-NLOS converts dense transient grids into sparse graph structure' not in readme:
    readme = replace_once(
        readme,
        timeline_anchor,
        timeline_anchor + '   │     Su et al.: DG-NLOS converts dense transient grids into sparse graph structure with separate appearance and geometry branches [AAAI]\n'
        + '   │     Young et al.: single-photon LiDAR NLOS occupancy closes the loop from around-corner sensing to autonomous robot control [IEEE ICRA]\n',
        'README timeline venue audit',
    )
write(readme_path, readme)

# ---------------------------------------------------------------------------
# Website paper explorer: normalize final records, preserve count (= no new paper).
# ---------------------------------------------------------------------------
index_path = Path('index.html')
index = read(index_path)
index = replace_once(index, 'Updated 6 August 2026 · 210+ papers', 'Updated 7 August 2026 · 210+ papers', 'website header date')
index = replace_entry_window(
    index,
    'Dual-branch Graph Feature Learning for NLOS Imaging',
    [
        ('venue:"arXiv 2025"', 'venue:"AAAI 2025, 39(7), 7051–7059"'),
        ('url:"https://arxiv.org/abs/2502.19683"', 'url:"https://doi.org/10.1609/aaai.v39i7.32757"'),
        ('key:"DG-NLOS: graph feature learning with separate albedo and depth branches for efficient joint hidden appearance/geometry recovery."', 'key:"DG-NLOS converts dense transient voxels into sparse graph features and separates albedo/depth reconstruction for efficient joint hidden appearance and geometry recovery."'),
    ],
    'website DG-NLOS',
)
index = replace_entry_window(
    index,
    'Enhancing Autonomous Navigation by Imaging Hidden Objects using Single-Photon LiDAR',
    [
        ('title:"Enhancing Autonomous Navigation by Imaging Hidden Objects using Single-Photon LiDAR"', 'title:"Enhancing Autonomous Navigation by Imaging Hidden Objects Using Single-Photon LiDAR"'),
        ('year:2024', 'year:2025'),
        ('venue:"arXiv 2024"', 'venue:"IEEE ICRA 2025, 4907–4914"'),
        ('url:"https://arxiv.org/abs/2410.03555"', 'url:"https://doi.org/10.1109/ICRA55743.2025.11128292"'),
        ('key:"SPAD / single-photon LiDAR NLOS occupancy perception connected directly to robot control in occluded corridors."', 'key:"SPAD-based multi-bounce sensing, learned hidden-space occupancy estimation, and robot control demonstrate NLOS-assisted autonomous navigation in a real L-shaped corridor."'),
    ],
    'website autonomous navigation',
)
index = replace_entry_window(
    index,
    'TransiT: Transient Transformer for Non-line-of-sight Videography',
    [
        ('venue:"ICCV 2025"', 'venue:"ICCV 2025, 27542–27551"'),
        ('url:"https://arxiv.org/abs/2503.11328"', 'url:"https://openaccess.thecvf.com/content/ICCV2025/html/Li_TransiT_Transient_Transformer_for_Non-line-of-sight_Videography_ICCV_2025_paper.html"'),
    ],
    'website TransiT',
)
index = replace_entry_window(
    index,
    'NLOS-NeuS: Non-line-of-sight Neural Implicit Surface',
    [
        ('venue:"ICCV 2023"', 'venue:"ICCV 2023, 10532–10541"'),
        ('url:"https://arxiv.org/abs/2303.12280"', 'url:"https://openaccess.thecvf.com/content/ICCV2023/html/Fujimura_NLOS-NeuS_Non-line-of-sight_Neural_Implicit_Surface_ICCV_2023_paper.html"'),
    ],
    'website NLOS-NeuS',
)
write(index_path, index)

# ---------------------------------------------------------------------------
# Survey wrapper + semantically appropriate learning discussion.
# ---------------------------------------------------------------------------
bare_path = Path('bare_jrnl.tex')
bare = read(bare_path)
bare = replace_once(bare, 'through 6 August 2026.', 'through 7 August 2026.', 'survey coverage date')
comment_anchor = '% 22 July 2026 citation trace corrects NIGHT and Soft Shadow Diffusion to final venues and integrates SNLLS and Fisher-equalized passive 3D computational periscopy.\n'
if '% 7 August 2026 final-venue audit' not in bare:
    bare = replace_once(
        bare,
        comment_anchor,
        comment_anchor + '% 7 August 2026 final-venue audit reconciles DG-NLOS to AAAI 2025, single-photon-LiDAR autonomous navigation to ICRA 2025, and normalizes final ICCV records for TransiT and NLOS-NeuS.\n',
        'survey audit comment',
    )
write(bare_path, bare)

article4_path = Path('article/4datadriven.tex')
article4 = read(article4_path)
article4 = replace_once(
    article4,
    'Su~\\etal~proposed DG-NLOS~\\cite{suDGNLOS2025},',
    'At AAAI~2025, Su~\\etal~proposed DG-NLOS~\\cite{suDGNLOS2025},',
    'DG-NLOS survey venue sentence',
)
write(article4_path, article4)

# If the navigation work is already discussed, make the final venue explicit without forcing a new paragraph.
for p in Path('article').glob('*.tex'):
    text = read(p)
    if 'Enhancing Autonomous Navigation' in text and 'ICRA~2025' not in text:
        # Title-based prose is uncommon; this clause is intentionally conservative.
        text = text.replace('Enhancing Autonomous Navigation by Imaging Hidden Objects using Single-Photon LiDAR',
                            'Enhancing Autonomous Navigation by Imaging Hidden Objects Using Single-Photon LiDAR')
        write(p, text)

# ---------------------------------------------------------------------------
# Bibliography: rewrite only entries that already exist, preserving citation keys.
# ---------------------------------------------------------------------------
DG = '''@inproceedings{{{key},
  author = {{Su, Xiongfei and Zhu, Tianyi and Liu, Lina and Chen, Zheng and Zhang, Yulun and Li, Siyuan and Ye, Juntian and Xu, Feihu and Yuan, Xin}},
  booktitle = {{Proceedings of the AAAI Conference on Artificial Intelligence}},
  doi = {{10.1609/aaai.v39i7.32757}},
  number = {{7}},
  pages = {{7051--7059}},
  title = {{Dual-branch Graph Feature Learning for NLOS Imaging}},
  url = {{https://doi.org/10.1609/aaai.v39i7.32757}},
  volume = {{39}},
  year = {{2025}}
}}'''
YOUNG = '''@inproceedings{{{key},
  archiveprefix = {{arXiv}},
  author = {{Young, Aaron and Batagoda, Nevindu M. and Zhang, Harry and Dave, Akshat and Pediredla, Adithya and Negrut, Dan and Raskar, Ramesh}},
  booktitle = {{2025 IEEE International Conference on Robotics and Automation (ICRA)}},
  doi = {{10.1109/ICRA55743.2025.11128292}},
  eprint = {{2410.03555}},
  pages = {{4907--4914}},
  publisher = {{IEEE}},
  title = {{Enhancing Autonomous Navigation by Imaging Hidden Objects Using Single-Photon LiDAR}},
  url = {{https://doi.org/10.1109/ICRA55743.2025.11128292}},
  year = {{2025}}
}}'''
TRANSIT = '''@inproceedings{{{key},
  archiveprefix = {{arXiv}},
  author = {{Li, Ruiqian and Shen, Siyuan and Xia, Suan and Wang, Ziheng and Peng, Xingyue and Song, Chengxuan and Zhu, Yingsheng and Wu, Tao and Li, Shiying and Yu, Jingyi}},
  booktitle = {{Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)}},
  eprint = {{2503.11328}},
  month = {{October}},
  pages = {{27542--27551}},
  title = {{TransiT: Transient Transformer for Non-line-of-sight Videography}},
  url = {{https://openaccess.thecvf.com/content/ICCV2025/html/Li_TransiT_Transient_Transformer_for_Non-line-of-sight_Videography_ICCV_2025_paper.html}},
  year = {{2025}}
}}'''
NEUS = '''@inproceedings{{{key},
  archiveprefix = {{arXiv}},
  author = {{Fujimura, Yuki and Kushida, Takahiro and Funatomi, Takuya and Mukaigawa, Yasuhiro}},
  booktitle = {{Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)}},
  doi = {{10.1109/ICCV51070.2023.00966}},
  eprint = {{2303.12280}},
  month = {{October}},
  title = {{NLOS-NeuS: Non-line-of-sight Neural Implicit Surface}},
  url = {{https://openaccess.thecvf.com/content/ICCV2023/html/Fujimura_NLOS-NeuS_Non-line-of-sight_Neural_Implicit_Surface_ICCV_2023_paper.html}},
  year = {{2023}}
}}'''

targets = [
    ('Dual-branch Graph Feature Learning for NLOS Imaging', DG),
    ('Enhancing Autonomous Navigation by Imaging Hidden Objects', YOUNG),
    ('TransiT: Transient Transformer for Non-line-of-sight Videography', TRANSIT),
    ('NLOS-NeuS: Non-line-of-sight Neural Implicit Surface', NEUS),
]
seen = {t[0]: [] for t in targets}
for bib in ROOT.rglob('*.bib'):
    text = read(bib)
    changed = False
    for frag, template in targets:
        if re.search(re.escape(frag), text, flags=re.I):
            text = replace_bib_entry(text, frag, template)
            seen[frag].append(str(bib))
            changed = True
    if changed:
        write(bib, text)
for frag, files in seen.items():
    if not files:
        raise RuntimeError(f'No bibliography entry found for {frag}')
    print(f'Updated {frag}: {files}')

# ---------------------------------------------------------------------------
# Public audit note: records why this run changes metadata but adds no paper.
# ---------------------------------------------------------------------------
update_path = Path('updates/2026-08-07-final-venue-audit.md')
update_path.parent.mkdir(exist_ok=True)
update_path.write_text('''# 7 August 2026 NLOS final-venue and citation-trace audit

A fresh keyword/modality search and forward-citation pass over the repository core papers did not identify a new high-confidence direct NLOS imaging publication newer than the repository's current July 2026 frontier. The run did identify four public metadata records that still pointed to preprints or omitted final proceedings metadata.

## Reconciled records

- **Dual-branch Graph Feature Learning for NLOS Imaging (DG-NLOS)** — final publication: *Proceedings of the AAAI Conference on Artificial Intelligence*, 39(7), 7051–7059 (2025), DOI `10.1609/aaai.v39i7.32757`. The repository previously labeled this paper as arXiv 2025.
- **Enhancing Autonomous Navigation by Imaging Hidden Objects Using Single-Photon LiDAR** — final publication: IEEE ICRA 2025, 4907–4914, DOI `10.1109/ICRA55743.2025.11128292`. The repository previously labeled the 2024 preprint rather than the 2025 proceedings paper.
- **TransiT: Transient Transformer for Non-line-of-sight Videography** — final ICCV 2025 open-access proceedings link and pages 27542–27551 are now used instead of the arXiv link.
- **NLOS-NeuS: Non-line-of-sight Neural Implicit Surface** — final ICCV 2023 open-access proceedings link is now used; DOI `10.1109/ICCV51070.2023.00966` is recorded in the bibliography.

## Citation-trace scope

Forward-citation searches emphasized the LCT, f-k migration, phasor-field, computational-periscopy, neural-transient-field, transformer/state-space, graph-reconstruction, acoustic, radar/mmWave, consumer-LiDAR, and differentiable-transient-rendering lineages. Candidate papers were retained only when they performed genuine hidden-scene reconstruction/sensing or were tightly adjacent NLOS perception work. The search did not uncover another missing direct NLOS paper beyond the current repository frontier in this run.

## Consistency target

README, website explorer/timeline, survey prose, bibliography, and the regenerated PDF must all carry the final-venue metadata above. The paper-explorer count is intentionally unchanged because this is a metadata/venue reconciliation, not four new papers.
''', encoding='utf-8')

# Final source checks before LaTeX compilation.
checks = {
    'README AAAI DOI': '10.1609/aaai.v39i7.32757' in read(readme_path),
    'README ICRA DOI': '10.1109/ICRA55743.2025.11128292' in read(readme_path),
    'website AAAI venue': 'AAAI 2025, 39(7), 7051–7059' in read(index_path),
    'website ICRA venue': 'IEEE ICRA 2025, 4907–4914' in read(index_path),
    'survey date': 'through 7 August 2026.' in read(bare_path),
    'survey AAAI sentence': 'At AAAI~2025, Su~\\etal~proposed DG-NLOS' in read(article4_path),
}
failed = [k for k, ok in checks.items() if not ok]
if failed:
    raise RuntimeError('Source validation failed: ' + ', '.join(failed))
print('Source audit completed successfully.')
