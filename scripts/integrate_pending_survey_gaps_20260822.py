from pathlib import Path
import re

DATE = "22 August 2026"
POSE_KEY = "xiaoNLOSHumanPose2026"
POSE_DOI = "10.1016/j.optlaseng.2026.109658"
PASSIVE = [
    ("heDualInputUNetPNLOS2023", "10.1109/NNICE58320.2023.10105693"),
    ("yuCAGANPNLOS2023", "10.1109/NNICE58320.2023.10105725"),
    ("kimReliableOccluderPNLOS2024", "10.1117/12.3017933"),
]

def read(p): return Path(p).read_text(encoding="utf-8")
def write(p,s): Path(p).write_text(s, encoding="utf-8")

# README: add only the three genuinely missing public rows; Xiao already exists.
p=Path("README.md"); s=read(p)
rows=[
'| 2024 | [Reliable reconstruction of passive non-line of sight imaging with occluder by deep learning](https://doi.org/10.1117/12.3017933) — Kim, Jang | Proc. SPIE 13076, 1307608 (2024) | Standard-camera occluder-aided passive NLOS reconstruction with deep learning; emphasizes robustness to changes in both occluder and hidden-object position. |\n',
'| 2023 | [CAGAN: A Channel-aware Generative Adversarial Network for Passive Non-Line-of-Sight Imaging](https://doi.org/10.1109/NNICE58320.2023.10105725) — Yu et al. | IEEE NNICE 2023 | Channel-aware GAN reconstruction on passive NLOS observations, using channel-feature fusion to emphasize informative content and suppress background interference. |\n',
'| 2023 | [Passive Non-Line-of-Sight imaging reconstruction based on dual input U-Net](https://doi.org/10.1109/NNICE58320.2023.10105693) — He et al. | IEEE NNICE 2023 | Early supervised dual-input U-Net reconstruction for passive NLOS, bridging NLOS-Passive-style data-driven inversion and later attention/generative methods. |\n']
if all(doi.lower() not in s.lower() for _,doi in PASSIVE):
    anchor='|------|-------|----------------|----------------|\n'
    if s.count(anchor)!=1: raise RuntimeError('README Latest Additions anchor ambiguous')
    s=s.replace(anchor, anchor+''.join(rows),1)
    lines=s.splitlines(True)
    idx=next((i for i,l in enumerate(lines) if l.startswith('2024 ──')),None)
    if idx is None: raise RuntimeError('README 2024 timeline anchor missing')
    lines.insert(idx+1,'   │     He et al. and Yu et al. establish supervised dual-input U-Net and channel-aware GAN passive reconstruction, while Kim and Jang emphasize robustness to changes in occluder and hidden-object geometry [IEEE NNICE / Proc. SPIE]\n')
    s=''.join(lines)
s,n=re.subn(r'\*\*Update run: \d{1,2} August 2026\.\*\*','**Update run: 22 August 2026.**',s,count=1)
if n!=1: raise RuntimeError('README update date anchor missing')
write(p,s)

# Canonical V2 corpus: add only three missing paper objects; Xiao already exists.
p=Path('data/papers-source.html'); s=read(p)
objs=[
'      {cat:"latest passive learning occluder reconstruction robustness",title:"Reliable reconstruction of passive non-line of sight imaging with occluder by deep learning",authors:"Kim, Jang",year:2024,venue:"Proc. SPIE 13076, 1307608 (2024)",url:"https://doi.org/10.1117/12.3017933",key:"Standard-camera occluder-aided passive NLOS reconstruction with deep learning, emphasizing robustness to changes in both occluder and hidden-object position."},\n',
'      {cat:"latest passive learning occluder reconstruction gan channel-aware",title:"CAGAN: A Channel-aware Generative Adversarial Network for Passive Non-Line-of-Sight Imaging",authors:"Yu et al.",year:2023,venue:"IEEE NNICE 2023",url:"https://doi.org/10.1109/NNICE58320.2023.10105725",key:"Channel-aware GAN reconstruction on passive NLOS observations, using channel-feature fusion to emphasize informative content and suppress background interference."},\n',
'      {cat:"latest passive learning occluder reconstruction unet",title:"Passive Non-Line-of-Sight imaging reconstruction based on dual input U-Net",authors:"He et al.",year:2023,venue:"IEEE NNICE 2023",url:"https://doi.org/10.1109/NNICE58320.2023.10105693",key:"Early supervised dual-input U-Net reconstruction for passive NLOS, bridging dataset-driven passive inversion and later attention/generative methods."},\n']
if all(doi.lower() not in s.lower() for _,doi in PASSIVE):
    anchor='    const papers=[\n'
    if s.count(anchor)!=1: raise RuntimeError('V2 papers anchor ambiguous')
    s=s.replace(anchor,anchor+''.join(objs),1)
    pat=re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
    m=pat.search(s)
    if not m: raise RuntimeError('V2 tracked counter missing')
    s=pat.sub(lambda x:x.group(1)+str(int(x.group(2))+3)+x.group(3),s,count=1)
    for year,sentence in [
        ('2023',' He et al. and Yu et al. added supervised dual-input U-Net and channel-aware GAN reconstruction to the passive learned branch.'),
        ('2024',' Kim and Jang then emphasized robustness to changes in both occluder and hidden-object position in a standard-camera passive system.')]:
        tl=re.compile(r'(<div class="tl"><div class="year">'+year+r'</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',re.S)
        if len(list(tl.finditer(s)))!=1: raise RuntimeError('V2 '+year+' timeline block ambiguous')
        s=tl.sub(lambda m:m.group(1)+m.group(2)+sentence+m.group(3),s,count=1)
s=re.sub(r'Updated \d{1,2} August 2026 · 210\+ papers','Updated 22 August 2026 · 210+ papers',s,count=1)
s=re.sub(r'Last updated: \d{1,2} August 2026','Last updated: 22 August 2026',s,count=1)
write(p,s)

# Passive survey: integrate staged historical learned-passive lineage.
p=Path('article/3passive.tex'); s=read(p)
if not all(k in s for k,_ in PASSIVE):
    anchor='\\vspace{0.8mm}\n\\noindent \\textbf{From separable soft-shadow inversion to diffusion.}\n'
    if s.count(anchor)!=1: raise RuntimeError('Passive survey insertion anchor ambiguous')
    para=(
'\\vspace{0.8mm}\n\\noindent \\textbf{Supervised occluder-aided passive reconstruction.}\n'
'Alongside physics-constrained and untrained priors, early supervised networks explored direct mappings from passive relay observations to hidden images. He~\\etal~used a dual-input U-Net for passive NLOS reconstruction~\\cite{heDualInputUNetPNLOS2023}, while Yu~\\etal~introduced CAGAN, a channel-aware adversarial model that emphasizes informative feature channels and suppresses background interference on NLOS-Passive data~\\cite{yuCAGANPNLOS2023}. Kim and Jang subsequently targeted reliability across acquisition geometry with a standard digital camera and an occluder, showing learned hidden-object reconstruction designed to tolerate changes in both occluder and target positions~\\cite{kimReliableOccluderPNLOS2024}. Together, these studies fill the transition from calibrated computational periscopy and dataset-driven passive inversion toward later attention, diffusion, multimodal, and geometry-aware passive NLOS models.\n\n')
    s=s.replace(anchor,para+anchor,1)
write(p,s)

# Data-driven survey: Xiao already public in corpus, close survey/bibliography gap.
p=Path('article/4datadriven.tex'); s=read(p)
if POSE_KEY not in s:
    anchor='\\vspace{0.8mm}\n\\noindent \\textbf{From reconstruction to recognition and clustering.}\n'
    if s.count(anchor)!=1: raise RuntimeError('Pose survey insertion anchor ambiguous')
    para=(
'\\vspace{0.8mm}\n\\noindent \\textbf{Robust transient human-pose estimation.}\n'
'Xiao~\\etal~further target semantic recovery when the transient signal itself becomes severely degraded~\\cite{xiaoNLOSHumanPose2026}. Their pipeline reconstructs a hidden three-dimensional volume, derives complementary depth and intensity representations, and fuses them in a multi-stage network for three-dimensional joint estimation. A physics-based NLOS simulator converts ordinary smartphone human videos into large-scale pose training data, reducing dependence on costly transient capture. Experiments with a self-built laser/SPAD system retain useful pose estimates at relay depths up to 1.75~m and SNR as low as 0.13, shifting transient human-pose sensing from proof-of-concept inference toward robustness under weak-photon and longer-range conditions.\n\n')
    s=s.replace(anchor,para+anchor,1)
write(p,s)

# Merge staged bibliographies entry-by-entry with DOI/key guards.
p=Path('egbib_merged_20260711.bib'); s=read(p)
for staging_path in ['egbib_20260821_passive_occluder_learning_gap.bib','egbib_20260822_semantic_pose_gap.bib']:
    st=read(staging_path)
    entries=re.findall(r'@\w+\{.*?\n\}',st,flags=re.S)
    for entry in entries:
        km=re.search(r'@\w+\{([^,]+),',entry); dm=re.search(r'doi\s*=\s*\{([^}]+)\}',entry,re.I)
        if not km or not dm: raise RuntimeError('Malformed staging BibTeX entry')
        key,doi=km.group(1).strip(),dm.group(1).strip()
        kc=len(re.findall(r'@\w+\{'+re.escape(key)+r'\s*,',s,re.I)); dc=len(re.findall(r'doi\s*=\s*\{\s*'+re.escape(doi)+r'\s*\}',s,re.I))
        if kc==0 and dc==0:
            s=s.rstrip()+'\n\n'+entry.strip()+'\n'
        elif kc==1 and dc==1:
            pass
        else:
            raise RuntimeError(f'Ambiguous bibliography state for {key}: key={kc}, doi={dc}')
write(p,s)

# Survey provenance/date.
p=Path('bare_jrnl.tex'); s=read(p)
note='% 22 August 2026 citation trace: supervised occluder-aided passive reconstruction and transient human-pose survey gaps synchronized.\n'
if note not in s: s=note+s
s=re.sub(r'through \d{1,2} August 2026','through 22 August 2026',s,count=1)
write(p,s)

# Mark staging notes as integrated in this guarded run.
for f in ['updates/2026-08-21-passive-occluder-learning-gap.md','updates/2026-08-22-semantic-pose-survey-gap.md']:
    p=Path(f); s=read(p)
    marker='\n## Guarded integration status — 22 August 2026\n\nPrepared for full public synchronization in the 22 August guarded build: README/V2 de-duplication, semantically placed survey prose, merged BibTeX, clean PDF build, citation checks, PDF text checks, and endpoint rendering are all required before commit.\n'
    if '## Guarded integration status — 22 August 2026' not in s: s+=marker
    write(p,s)

print('Pending survey gaps source integration prepared successfully')
