from pathlib import Path
import re

RUN_DATE='15 August 2026'
RUN_DATE_SHORT='15 Aug 2026'

papers=[
    {
        'title':'Real-time two-bounce non-line-of-sight object tracking via dual-view collaborative perception network',
        'doi':'10.1364/OE.575453',
        'url':'https://doi.org/10.1364/OE.575453',
        'authors':'Jingyuan Zhang, Bochao Zhang, Taiping Lu, Lianfa Bai, Xiaoyu Chen, and Jing Han',
        'authors_short':'Zhang et al.',
        'venue':'Optics Express 33(20), 42542–42556 (2025)',
        'key':'zhangDCPNetTwoBounce2025',
        'cat':'latest learning two-bounce steady-state tracking dynamic shadow dual-view',
        'summary':'Uses time-multiplexed alternating dual illumination to acquire two shadow views and DCPNet to fuse cross-view spatial consistency with single-view temporal coherence for real-time hidden-object trajectory estimation; physics-rendered training data and real fine-tuning validate corridor/tunnel-style two-bounce tracking.'
    },
    {
        'title':'Efficient implicit reconstruction of hidden object in two-bounce non-line-of-sight imaging',
        'doi':'10.1364/OE.567764',
        'url':'https://doi.org/10.1364/OE.567764',
        'authors':'Xiaoyu Chen, Peiling Teng, Jingyuan Zhang, Lianfa Bai, and Jing Han',
        'authors_short':'Chen et al.',
        'venue':'Optics Express 33(19), 41244–41260 (2025)',
        'key':'chenImplicitTwoBounceNLOS2025',
        'cat':'latest learning two-bounce steady-state nerf implicit reconstruction shadow',
        'summary':'Replaces explicit voxel carving with hierarchical NeRF-based implicit ray carving and spatial/temporal ray selection, reducing redundant shadow rays while reconstructing static and dynamic hidden scenes; reports about 2% relative depth deviation in a 20 m × 10 m × 4 m volume.'
    }
]

# README: update freshness and add only genuinely missing final-venue records.
p=Path('README.md'); s=p.read_text(encoding='utf-8')
s=re.sub(r'\*\*Update run: \d{1,2} August 2026\.\*\*',f'**Update run: {RUN_DATE}.**',s,count=1)
anchor='|------|-------|----------------|----------------|'
if s.count(anchor)!=1: raise RuntimeError('README Latest Additions header not unique')
rows=[]
for x in papers:
    if x['doi'] not in s:
        rows.append(f"| 2025 | [{x['title']}]({x['url']}) — {x['authors_short']} | {x['venue']} | {x['summary']} |")
if rows:
    s=s.replace(anchor,anchor+'\n'+'\n'.join(rows),1)
# Add a compact timeline interpretation without duplicating entries on rerun.
marker='two-bounce NLOS matured from explicit shadow carving to implicit neural reconstruction and real-time dual-view tracking'
if marker not in s:
    tl_anchor='2025 ── Roueinfar & Salmanian:'
    if tl_anchor in s:
        s=s.replace(tl_anchor,'2025 ── Chen et al.: hierarchical-NeRF implicit ray carving makes two-bounce shadow reconstruction more efficient [Optics Express]\n   │     Zhang et al.: DCPNet advances two-bounce NLOS from reconstruction to real-time dual-view tracking [Optics Express]\n   │     '+tl_anchor,1)
    else:
        # Preserve the intended trajectory in a plain sentence if the ASCII timeline has drifted.
        insert='\nTwo-bounce NLOS matured from explicit shadow carving to implicit neural reconstruction and real-time dual-view tracking in 2025.\n'
        pos=s.find('\n## Taxonomy')
        if pos<0: raise RuntimeError('README timeline/taxonomy anchor missing')
        s=s[:pos]+insert+s[pos:]
p.write_text(s,encoding='utf-8')

# Canonical V2 page: only expose freshness; graph/explorer content comes from data/papers-source.html.
p=Path('index.html'); s=p.read_text(encoding='utf-8')
s=re.sub(r'<span class="pill">Updated \d{1,2} Aug 2026</span>',f'<span class="pill">Updated {RUN_DATE_SHORT}</span>',s,count=1)
p.write_text(s,encoding='utf-8')

# Canonical paper corpus that drives the V2 3D graph, trends and paper explorer.
p=Path('data/papers-source.html'); s=p.read_text(encoding='utf-8')
anchor_match=re.search(r'(\bconst\s+papers\s*=\s*\[\s*\n)',s)
if not anchor_match: raise RuntimeError('paper array anchor missing')
objects=[]
for x in papers:
    if x['doi'] not in s:
        obj=('      {cat:"'+x['cat']+'",title:"'+x['title'].replace('"','\\"')+'",authors:"'+x['authors_short']+'",year:2025,venue:"'+x['venue']+'",url:"'+x['url']+'",key:"'+x['summary'].replace('"','\\"')+'"},\n')
        objects.append(obj)
if objects:
    i=anchor_match.end(); s=s[:i]+''.join(objects)+s[i:]
# Add the 2025 trajectory to the legacy timeline retained in the corpus source.
if 'DCPNet advances two-bounce NLOS from reconstruction to real-time dual-view tracking' not in s:
    pat=r'(<div class="tl"><div class="year">2025</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)'
    m=re.search(pat,s,re.S)
    if m:
        extra=' Two-bounce NLOS also moved beyond explicit shadow carving: hierarchical-NeRF implicit ray carving reduced redundant multi-view rays for efficient static/dynamic reconstruction, while DCPNet combined dual-view spatial consistency and temporal coherence for real-time hidden-object tracking.'
        s=s[:m.start()]+m.group(1)+m.group(2)+extra+m.group(3)+s[m.end():]
# Keep direct inspection metadata current and recompute corpus count.
s=re.sub(r'Updated \d{1,2} August 2026',f'Updated {RUN_DATE}',s,count=1)
s=re.sub(r'Last updated: \d{1,2} August 2026',f'Last updated: {RUN_DATE}',s,count=1)
count=len(re.findall(r'\{cat:"',s))
s,n=re.subn(r'<div class="stat"><b>\d+</b><span>tracked latest entries</span></div>',f'<div class="stat"><b>{count}</b><span>tracked latest entries</span></div>',s,count=1)
if n!=1: raise RuntimeError('tracked-entry stat missing in paper source')
p.write_text(s,encoding='utf-8')

# Survey prose: place the two missing 2025 works chronologically inside the Two-Bounce NLOS section.
p=Path('article/5newscenes.tex'); s=p.read_text(encoding='utf-8')
if papers[0]['key'] not in s or papers[1]['key'] not in s:
    anchor='A complementary steady-state trajectory replaces binary shadow carving with a continuous learned scene model.'
    if s.count(anchor)!=1: raise RuntimeError('two-bounce neural-field anchor not unique')
    para=(
        '\\vspace{0.8mm}\n\\noindent \\textbf{Implicit reconstruction and real-time two-bounce tracking.}\n'
        'Between analytical two-bounce measurement design and the newer neural illumination/shadow fields, Chen~\\etal~introduced a hierarchical-NeRF formulation for implicit shadow-based reconstruction~\\cite{chenImplicitTwoBounceNLOS2025}. '
        'Instead of explicitly carving every candidate voxel from all multi-view rays, the method decomposes shadow observations spatially and temporally, selects rays that carry the strongest geometric constraints, and optimizes a cumulative-transmittance neural field. This reduces redundant ray computation while supporting both static and changing hidden scenes. '
        'Zhang~\\etal~then shifted the two-bounce branch from geometry reconstruction toward task-oriented dynamic perception with DCPNet~\\cite{zhangDCPNetTwoBounce2025}. Their time-multiplexed acquisition alternates two illumination views and fuses cross-view spatial consistency with single-view temporal coherence to recover hidden-object trajectories in corridor/tunnel-style scenes, using physics-rendered sequences for pretraining and real measurements for validation. '
        'Together these works fill the 2025 transition from explicit shadow carving toward implicit neural reconstruction and real-time two-bounce tracking, immediately preceding the NIF and D-NeSF neural-field trajectory discussed below.\n\n'
    )
    s=s.replace(anchor,para+anchor,1)
p.write_text(s,encoding='utf-8')

# Add verified final-venue BibTeX records, with strict duplicate checks.
p=Path('egbib_merged_20260711.bib'); s=p.read_text(encoding='utf-8')
entries={
'chenImplicitTwoBounceNLOS2025':'''@article{chenImplicitTwoBounceNLOS2025,
  author = {Chen, Xiaoyu and Teng, Peiling and Zhang, Jingyuan and Bai, Lianfa and Han, Jing},
  doi = {10.1364/OE.567764},
  journal = {Optics Express},
  number = {19},
  pages = {41244--41260},
  publisher = {Optica Publishing Group},
  title = {Efficient implicit reconstruction of hidden object in two-bounce non-line-of-sight imaging},
  url = {https://doi.org/10.1364/OE.567764},
  volume = {33},
  year = {2025}
}''',
'zhangDCPNetTwoBounce2025':'''@article{zhangDCPNetTwoBounce2025,
  author = {Zhang, Jingyuan and Zhang, Bochao and Lu, Taiping and Bai, Lianfa and Chen, Xiaoyu and Han, Jing},
  doi = {10.1364/OE.575453},
  journal = {Optics Express},
  number = {20},
  pages = {42542--42556},
  publisher = {Optica Publishing Group},
  title = {Real-time two-bounce non-line-of-sight object tracking via dual-view collaborative perception network},
  url = {https://doi.org/10.1364/OE.575453},
  volume = {33},
  year = {2025}
}'''
}
for key,entry in entries.items():
    if not re.search(r'@[A-Za-z]+\{'+re.escape(key)+r',',s,re.I):
        s=s.rstrip()+'\n\n'+entry+'\n'
for x in papers:
    kc=len(re.findall(r'@[A-Za-z]+\{'+re.escape(x['key'])+r',',s,re.I))
    dc=len(re.findall(r'(?im)^\s*doi\s*=\s*\{'+re.escape(x['doi'])+r'\}\s*,?\s*$',s))
    if kc!=1 or dc!=1: raise RuntimeError(f"BibTeX duplicate/absence for {x['key']}: key={kc}, doi={dc}")
p.write_text(s,encoding='utf-8')

# Living survey synchronization note/date.
p=Path('bare_jrnl.tex'); s=p.read_text(encoding='utf-8')
note='% 15 August 2026 citation trace: missing two-bounce implicit reconstruction and dual-view real-time tracking lineage synchronized.\n'
if note not in s: s=note+s
s=re.sub(r'through \d{1,2} August 2026','through 15 August 2026',s,count=1)
p.write_text(s,encoding='utf-8')

# Provenance/update note.
Path('updates/2026-08-15-two-bounce-nlos-lineage.md').write_text('''# Two-bounce NLOS lineage synchronized — 15 August 2026

A citation-tracing and publisher-index pass found two final-venue 2025 Optics Express papers missing from the public corpus and survey:

- Xiaoyu Chen et al., “Efficient implicit reconstruction of hidden object in two-bounce non-line-of-sight imaging,” Optics Express 33(19), 41244–41260 (2025), DOI 10.1364/OE.567764.
- Jingyuan Zhang et al., “Real-time two-bounce non-line-of-sight object tracking via dual-view collaborative perception network,” Optics Express 33(20), 42542–42556 (2025), DOI 10.1364/OE.575453.

The survey places them between the 2023 analysis of transient two-bounce measurements and the 2026 NIF/D-NeSF neural-field works, making the trajectory explicit: explicit shadow carving → efficient implicit neural reconstruction → real-time dual-view tracking → neural illumination/dynamic shadow fields.

README, canonical V2 corpus, survey prose, merged bibliography, and rebuilt PDF are validated together by the integration workflow.
''',encoding='utf-8')
