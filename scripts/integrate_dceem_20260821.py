from pathlib import Path
import re

DOI = "10.1016/j.optcom.2026.133626"
KEY = "wangDynamicChannelPNLOS2026"
TITLE = "Enhancing passive non-line-of-sight imaging via dynamic channel optimization"
DATE = "21 August 2026"


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


# README -----------------------------------------------------------------
p = Path("README.md")
s = read(p)
row = (
    "| 2026 | [Enhancing passive non-line-of-sight imaging via dynamic channel optimization]"
    "(https://doi.org/10.1016/j.optcom.2026.133626) — Wang et al. | "
    "Optics Communications 620, 133626 (2026) | Introduces DCEEM for low-SNR passive NLOS: "
    "Bayesian multiplicative fusion combines feature statistics with light-transport descriptors to adaptively "
    "suppress noise-dominated channels, while hierarchical denoising/refinement and vector-quantization "
    "optimization strengthen hidden-scene reconstruction. |\n"
)
added_readme = DOI.lower() not in s.lower()
if added_readme:
    anchor = "|------|-------|----------------|----------------|\n"
    if s.count(anchor) != 1:
        raise RuntimeError(f"README Latest Additions anchor count={s.count(anchor)}")
    s = s.replace(anchor, anchor + row, 1)

    timeline_anchor = (
        "2026 ── Liang et al.: HPDI — physics-informed coarse-to-fine reconstruction fused with an implicit "
        "data-driven passive pathway [IEEE TCI]\n"
    )
    if s.count(timeline_anchor) != 1:
        raise RuntimeError(f"README 2026 HPDI timeline anchor count={s.count(timeline_anchor)}")
    timeline_line = (
        "   │     Wang et al.: DCEEM makes passive feature selection explicitly light-transport-aware, using "
        "Bayesian dynamic channel weighting and hierarchical denoising/refinement to suppress low-SNR channel "
        "aliasing before vector quantization [Optics Communications]\n"
    )
    s = s.replace(timeline_anchor, timeline_anchor + timeline_line, 1)

s, n = re.subn(r"\*\*Update run: \d{1,2} August 2026\.\*\*", "**Update run: 21 August 2026.**", s, count=1)
if n != 1:
    raise RuntimeError("README update-run date anchor missing")
write(p, s)


# Canonical V2 paper corpus ------------------------------------------------
p = Path("data/papers-source.html")
s = read(p)
added_corpus = DOI.lower() not in s.lower()
if added_corpus:
    anchor = "    const papers=[\n"
    if s.count(anchor) != 1:
        raise RuntimeError(f"V2 papers array anchor count={s.count(anchor)}")
    obj = (
        '      {cat:"latest passive learning physics-guided low-snr light-transport vector-quantization '
        'channel-attention reconstruction",title:"Enhancing passive non-line-of-sight imaging via dynamic channel '
        'optimization",authors:"Wang et al.",year:2026,venue:"Optics Communications 620, 133626 (2026)",'
        'url:"https://doi.org/10.1016/j.optcom.2026.133626",key:"Introduces DCEEM for low-SNR passive NLOS: '
        'Bayesian multiplicative fusion combines feature statistics with light-transport physical descriptors to '
        'adaptively suppress noise-dominated channels, followed by hierarchical denoising/refinement and '
        'vector-quantization optimization."},\n'
    )
    s = s.replace(anchor, anchor + obj, 1)

    count_pat = re.compile(r'(<div class="stat"><b>)(\d+)(</b><span>tracked latest entries</span></div>)')
    m = count_pat.search(s)
    if not m:
        raise RuntimeError("V2 tracked-paper counter anchor missing")
    old_count = int(m.group(2))
    s = count_pat.sub(lambda x: x.group(1) + str(old_count + 1) + x.group(3), s, count=1)

    # Add one development-timeline sentence to the unique 2026 timeline block.
    tl_pat = re.compile(
        r'(<div class="tl"><div class="year">2026</div><div class="tl-body"><strong>.*?</strong><p>)(.*?)(</p></div></div>)',
        re.S,
    )
    matches = list(tl_pat.finditer(s))
    if len(matches) != 1:
        raise RuntimeError(f"V2 2026 timeline block count={len(matches)}")
    sentence = (
        " Wang et al. further made passive feature selection explicitly light-transport-aware with DCEEM, "
        "combining Bayesian dynamic channel weighting with hierarchical denoising/refinement and vector "
        "quantization for low-SNR reconstruction."
    )
    s = tl_pat.sub(lambda m: m.group(1) + m.group(2) + sentence + m.group(3), s, count=1)

s = s.replace("Updated 20 August 2026 · 210+ papers", "Updated 21 August 2026 · 210+ papers")
s = s.replace("Last updated: 20 August 2026", "Last updated: 21 August 2026")
write(p, s)


# Survey prose --------------------------------------------------------------
p = Path("article/3passive.tex")
s = read(p)
if KEY not in s:
    anchor = (
        "\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Diffuse-aware attention encoding for passive NLOS.}\n"
        "Recent ordinary-camera methods increasingly encode the relay-wall transport structure inside the network rather than relying on a generic image-to-image backbone. Wang~\\etal~introduced diffuse-aware attention-enhanced encoding for passive NLOS reconstruction~\\cite{wangDiffuseAwarePassive2026}. By explicitly emphasizing features that survive diffuse relay transport, the method represents a further step from early U-Net mappings toward attention mechanisms designed around the conditioning of the passive forward process.\n\n"
    )
    if s.count(anchor) != 1:
        raise RuntimeError(f"Passive diffuse-aware paragraph anchor count={s.count(anchor)}")
    para = (
        "\\vspace{0.8mm}\n"
        "\\noindent \\textbf{Light-transport-aware dynamic channel selection.}\n"
        "More recently, Wang~\\etal~targeted the channel-aliasing failure mode of low-SNR passive NLOS reconstruction with a dynamic channel enhancement encoding mechanism (DCEEM)~\\cite{wangDynamicChannelPNLOS2026}. Rather than deriving channel attention only from latent feature statistics, DCEEM combines those statistics with light-transport descriptors through Bayesian multiplicative fusion, then follows the signal-to-noise evolution of the encoder with low-dimensional denoising, high-dimensional refinement, and vector-quantization optimization. This direction moves learned passive inversion from increasingly expressive backbones toward explicit physics-aware selection of which latent channels should be trusted under weak indirect illumination.\n\n"
    )
    s = s.replace(anchor, anchor + para, 1)
write(p, s)


# Merge canonical bibliography ---------------------------------------------
p = Path("egbib_merged_20260711.bib")
s = read(p)
staging = read("egbib_20260820_dceem_passive_gap.bib").strip() + "\n"
key_count = len(re.findall(r"@\w+\{" + re.escape(KEY) + r"\s*,", s, flags=re.I))
doi_count = s.lower().count(DOI.lower())
if key_count == 0 and doi_count == 0:
    if not s.endswith("\n"):
        s += "\n"
    s += "\n" + staging
elif key_count != 1 or doi_count < 1:
    raise RuntimeError(f"Ambiguous DCEEM bibliography state: key_count={key_count}, doi_count={doi_count}")
write(p, s)


# Survey provenance/date ----------------------------------------------------
p = Path("bare_jrnl.tex")
s = read(p)
note = "% 21 August 2026 passive citation trace: DCEEM physics-aware dynamic channel optimization synchronized across public artifacts.\n"
if note not in s:
    s = note + s
s = s.replace("through 20 August 2026", "through 21 August 2026")
write(p, s)


# Update the old staging note so it no longer claims the previous passive PR is blocking integration.
p = Path("updates/2026-08-20-dceem-passive-gap.md")
s = read(p)
status_heading = "## Integration status"
if status_heading not in s:
    s += (
        "\n## Integration status\n\n"
        "Integrated by the guarded 21 August 2026 workflow after the Hyper-NLOS / rough-surface passive milestone update had landed on `master`. The workflow synchronizes README, the canonical V2 corpus/timeline, passive-survey prose, merged bibliography, and the rebuilt survey PDF, and validates citation resolution and rendered PDF endpoints before committing.\n"
    )
else:
    s += "\n\n21 August 2026: guarded public integration rerun requested after the earlier passive-lineage blocker was cleared.\n"
write(p, s)

print("DCEEM source integration prepared successfully")
