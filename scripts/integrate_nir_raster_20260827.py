from pathlib import Path
import re

TITLE = "Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength"
DOI = "10.1109/ICEE67339.2025.11213924"
KEY = "roueinfarNIRRaster2025"
STAGING_KEY = "roueinfarNIRRasterNLOS2025"


def read(path): return Path(path).read_text(encoding="utf-8")
def write(path,text): Path(path).write_text(text,encoding="utf-8")
def replace_once(text,old,new,label):
    n=text.count(old)
    if n!=1: raise RuntimeError(f"{label}: expected one anchor, found {n}")
    return text.replace(old,new,1)
def doi_field_count(text): return len(re.findall(r"(?mi)^\s*doi\s*=\s*\{"+re.escape(DOI)+r"\}\s*,?\s*$",text))

def bib_entries(text):
    out=[]; i=0
    while True:
        m=re.search(r"(?m)^@[A-Za-z]+\{",text[i:])
        if not m: break
        start=i+m.start(); brace=text.find('{',start); depth=0; j=brace
        while j<len(text):
            if text[j]=='{': depth+=1
            elif text[j]=='}':
                depth-=1
                if depth==0:
                    out.append((start,j+1,text[start:j+1])); i=j+1; break
            j+=1
        else: raise RuntimeError('unterminated BibTeX entry')
    return out

def dedupe_doi_keep_key(text):
    matches=[]
    for start,end,entry in bib_entries(text):
        if re.search(r"(?mi)^\s*doi\s*=\s*\{"+re.escape(DOI)+r"\}\s*,?\s*$",entry):
            km=re.match(r"@[A-Za-z]+\{\s*([^,]+),",entry,re.I|re.S)
            matches.append((start,end,entry,km.group(1).strip() if km else ''))
    if len(matches)<=1: return text
    canonical=[x for x in matches if x[3]==KEY]
    if len(canonical)!=1: raise RuntimeError(f"cannot safely deduplicate DOI: {len(matches)} entries, canonical={len(canonical)}")
    for start,end,entry,k in sorted([x for x in matches if x[3]!=KEY],key=lambda x:x[0],reverse=True):
        left=start
        while left>0 and text[left-1]=='\n': left-=1
        text=text[:left]+'\n\n'+text[end:].lstrip('\n')
        print(f"Removed duplicate DOI entry with key {k}")
    return text

# README: check the Latest Additions section itself, not global timeline mentions.
readme=read("README.md")
latest_start=readme.find("## Latest Additions")
if latest_start<0: raise RuntimeError("Latest Additions heading missing")
next_heading=readme.find("\n## ",latest_start+4)
latest_end=next_heading if next_heading>=0 else len(readme)
latest=readme[latest_start:latest_end]
if TITLE not in latest:
    row=("| 2025 | [Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength]"
         "(https://doi.org/10.1109/ICEE67339.2025.11213924) — Roueinfar and Salmanian | "
         "IEEE ICEE 2025, 1175–1179 | "
         "Demonstrates a low-complexity active NIR NLOS system using an 808-nm, 500-mW laser raster-scanned over a relay wall by a pan–tilt unit; "
         "an NIR camera records three-bounce returns for three simple hidden targets, with reconstruction error evaluated by MSE/RMSE. "
         "The final IEEE venue supersedes the later arXiv:2607.04183 upload. |\n")
    table_anchor="|------|-------|----------------|----------------|\n"
    pos=readme.find(table_anchor,latest_start,latest_end)
    if pos<0: raise RuntimeError("Latest Additions table header missing")
    pos+=len(table_anchor); readme=readme[:pos]+row+readme[pos:]
readme=re.sub(r"\*\*Update run: \d{1,2} August 2026\.\*\*","**Update run: 27 August 2026.**",readme,count=1)
write("README.md",readme)

# Public V2 wrapper date.
index=read("index.html")
index=re.sub(r"Updated \d{1,2} Aug 2026","Updated 27 Aug 2026",index,count=1)
write("index.html",index)

# Canonical paper corpus: check only the paper array, not timeline prose.
corpus=read("data/papers-source.html")
arr_start=corpus.find("    const papers=["); arr_end=corpus.find("\n    ];",arr_start)
if arr_start<0 or arr_end<0: raise RuntimeError("canonical paper array boundaries not found")
array_text=corpus[arr_start:arr_end]
if TITLE not in array_text:
    obj=('      {cat:"latest active optical steady-state nir raster-scan conventional-camera hardware",'
         'title:"Non-Line-of-Sight Imaging Using Raster Scanning at NIR Wavelength",'
         'authors:"Roueinfar and Salmanian",year:2025,venue:"IEEE ICEE 2025, 1175–1179",'
         'url:"https://doi.org/10.1109/ICEE67339.2025.11213924",'
         'key:"Uses an 808-nm, 500-mW NIR laser on a pan–tilt raster scan and an NIR camera to recover simple hidden targets from three-bounce relay-wall returns; the final IEEE ICEE 2025 publication supersedes the later arXiv upload."},\n')
    insert=corpus.find("\n",arr_start)+1
    corpus=corpus[:insert]+obj+corpus[insert:]
arr_start=corpus.find("    const papers=["); arr_end=corpus.find("\n    ];",arr_start); array_text=corpus[arr_start:arr_end]
tracked=array_text.count("{cat:")
corpus,n=re.subn(r'(<div class="stat"><b>)\d+(</b><span>tracked latest entries</span>)',rf'\g<1>{tracked}\g<2>',corpus,count=1)
if n!=1: raise RuntimeError("tracked-entry counter not found")
corpus=re.sub(r"Updated \d{1,2} August 2026","Updated 27 August 2026",corpus,count=1)
corpus=re.sub(r"Last updated: \d{1,2} August 2026","Last updated: 27 August 2026",corpus,count=1)
write("data/papers-source.html",corpus)

# Survey body already uses this canonical key.
active=read("article/2active.tex")
if KEY not in active or "raster" not in active.lower(): raise RuntimeError("existing NIR survey integration/canonical citation key is missing")

# Canonical bibliography: preserve canonical survey key and remove same-DOI legacy duplicates.
bib=read("egbib_merged_20260711.bib")
if STAGING_KEY in bib and KEY not in bib: bib=bib.replace(STAGING_KEY,KEY)
key_n=len(re.findall(r"@[A-Za-z]+\{"+re.escape(KEY)+r",",bib,flags=re.I)); doi_n=doi_field_count(bib)
if key_n==0 and doi_n==0:
    stage=read("egbib_20260827_nir_raster_scan_gap.bib").replace(STAGING_KEY,KEY)
    bib=bib.rstrip()+"\n\n"+stage.strip()+"\n"
else: bib=dedupe_doi_keep_key(bib)
key_n=len(re.findall(r"@[A-Za-z]+\{"+re.escape(KEY)+r",",bib,flags=re.I)); doi_n=doi_field_count(bib)
if key_n!=1 or doi_n!=1: raise RuntimeError(f"bibliography normalization failed: key={key_n}, doi_field={doi_n}")
write("egbib_merged_20260711.bib",bib)

# Survey provenance/date marker; no duplicate literature prose is added.
tex=read("bare_jrnl.tex")
note="% 27 August 2026 consistency pass: finalized IEEE ICEE venue and synchronized the NIR raster-scan NLOS record across public artifacts.\n"
if note not in tex: tex=note+tex
tex=re.sub(r"through \d{1,2} August 2026","through 27 August 2026",tex,count=1)
write("bare_jrnl.tex",tex)

# Scoped final assertions.
readme=read("README.md"); latest_start=readme.find("## Latest Additions"); latest_end=readme.find("\n## ",latest_start+4); latest=readme[latest_start:latest_end if latest_end>=0 else len(readme)]
corpus=read("data/papers-source.html"); arr_start=corpus.find("    const papers=["); arr_end=corpus.find("\n    ];",arr_start); array_text=corpus[arr_start:arr_end]
if TITLE not in latest or DOI not in latest: raise RuntimeError("NIR record missing from README Latest Additions")
if TITLE not in array_text or DOI not in array_text: raise RuntimeError("NIR record missing from V2 Paper Explorer array")
if KEY not in read("article/2active.tex"): raise RuntimeError("canonical survey citation missing")
if KEY not in read("egbib_merged_20260711.bib") or doi_field_count(read("egbib_merged_20260711.bib"))!=1: raise RuntimeError("canonical bibliography missing or duplicated")
if "27 August 2026 consistency pass" not in read("bare_jrnl.tex"): raise RuntimeError("survey provenance missing")
print(f"Integrated {TITLE}; canonical key={KEY}; tracked={tracked}")
