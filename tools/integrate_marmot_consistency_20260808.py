from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MARMOT_TITLE = "MARMOT: Masked Autoencoder for Modeling Transient Imaging"
MARMOT_KEY = "shenMARMOT2025"
MARMOT_README_ROW = "| 2025 | [MARMOT: Masked Autoencoder for Modeling Transient Imaging](https://arxiv.org/abs/2506.08470) — Shen et al. | arXiv 2025 | Introduces self-supervised masked-autoencoder pretraining for transient/NLOS data. A scanning-pattern mask makes the retained samples equivalent to arbitrary relay sampling; pretraining on the 500K-model TransVerse synthetic transient corpus enables reusable features and measurement completion for downstream hidden-scene tasks. No final journal or conference venue could be verified as of 9 August 2026. |"
MARMOT_SURVEY = r'''\vspace{0.8mm}
\noindent \textbf{Masked transient pretraining.}
Shen~\etal~introduced MARMOT, a self-supervised masked autoencoder that treats transient measurements as a reusable pretraining modality rather than training a separate reconstruction network for every NLOS task~\cite{shenMARMOT2025}. Its scanning-pattern mask removes structured subsets of relay measurements so that the visible tokens are functionally equivalent to arbitrary sparse sampling, while a Transformer encoder--decoder predicts the missing transient measurements. Pretraining on the TransVerse corpus of 500,000 synthetic 3D models allows the learned transient representation to transfer to downstream reconstruction through direct feature reuse or decoder fine-tuning. This work marks a shift from task-specific transient inversion toward foundation-style measurement priors that can support sparse acquisition, transient completion, and multiple NLOS objectives.'''
MARMOT_ANCHOR = "Together, these works bridge classical dense ToF NLOS and the newer arbitrary-relay / mobile-capture setting: they show that practical NLOS deployment depends not only on faster solvers, but also on inverse models that remain well posed when the relay surface is incomplete, irregular, or sparsely sampled."

N2LOS_TITLE = "N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization"
N2LOS_DOI = "10.1109/TMC.2025.3634623"
N2LOS_OLD_ROW = "| 2025 | [N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization](https://arxiv.org/abs/2505.08240) — Shi et al. | arXiv 2025 | Tag-assisted mmWave NLOS localization using multipath, HFD modulation, and FS-MUSIC; relevant to RF NLOS sensing/localization rather than full imaging. |"
N2LOS_NEW_ROW = "| 2026 | [N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization](https://doi.org/10.1109/TMC.2025.3634623) — Shi et al. | IEEE Transactions on Mobile Computing 25(5), 6002–6016 (2026) | Uses a single 24 GHz radar plus one backscatter tag to disambiguate environmental and tag-mediated multipath with HFD signaling and FS-MUSIC; measured laboratory, office, and around-corner experiments report roughly 10–12 cm median coordinate error at 5 m. The repository now uses the final IEEE TMC record rather than the 2025 arXiv preprint. |"
N2LOS_OLD_INDEX = '{cat:"latest modality",title:"N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization",authors:"Shi et al.",year:2025,venue:"arXiv 2025",url:"https://arxiv.org/abs/2505.08240",key:"Tag-assisted mmWave NLOS localization with HFD modulation and FS-MUSIC multipath resolution."}'
N2LOS_NEW_INDEX = '{cat:"latest modality rf mmwave localization",title:"N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization",authors:"Shi et al.",year:2026,venue:"IEEE TMC 25(5), 6002–6016 (2026)",url:"https://doi.org/10.1109/TMC.2025.3634623",key:"Single-tag 24 GHz mmWave NLOS localization uses HFD signaling and FS-MUSIC to disambiguate multipath; the final IEEE TMC record reports measured lab, office, and around-corner validation."}'
N2LOS_SURVEY_SENTENCE = "Experiments report roughly 10--12~cm median coordinate error at 5~m, illustrating how a lightweight tag can convert uncontrolled around-corner multipath into identifiable localization paths."
N2LOS_SURVEY_REPLACEMENT = N2LOS_SURVEY_SENTENCE + " The final journal record appears in \nobreakspace IEEE Transactions on Mobile Computing, vol.~25, no.~5, pp.~6002--6016 (2026), superseding the earlier arXiv-only metadata."
N2LOS_BIB = r'''@article{shiN2LoS2025,
  author = {Shi, Zhenguo and Yan, Yihe and Wang, Yanxiang and Hu, Wen and Chou, Chun Tung and Cheng, Qingqing and Yuan, Weijie},
  doi = {10.1109/TMC.2025.3634623},
  journal = {IEEE Transactions on Mobile Computing},
  month = {May},
  number = {5},
  pages = {6002--6016},
  title = {{$N^2$LoS}: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization},
  url = {https://doi.org/10.1109/TMC.2025.3634623},
  volume = {25},
  year = {2026},
  note = {Published online 19 November 2025; final issue record May 2026; also available as arXiv:2505.08240}
}'''

UPDATE_NOTE = """# 9 August 2026 NLOS citation-trace consistency update

This bounded follow-up completes two outstanding source-consistency items discovered by the citation-tracing workflow.

1. **MARMOT: Masked Autoencoder for Modeling Transient Imaging** (Shen et al., arXiv:2506.08470, 2025) is integrated into the Latest Additions table and the survey's sparse/irregular transient-acquisition discussion. As of 9 August 2026, the arXiv/DBLP records remain preprint/CoRR metadata; no final journal or conference venue was verified.
2. **N2LoS: Single-Tag mmWave Backscatter for Robust Non-Line-of-Sight Localization** is corrected from arXiv-only metadata to its final **IEEE Transactions on Mobile Computing**, vol. 25, no. 5, pp. 6002–6016 (2026), DOI **10.1109/TMC.2025.3634623**. The final record has seven authors: Zhenguo Shi, Yihe Yan, Yanxiang Wang, Wen Hu, Chun Tung Chou, Qingqing Cheng, and Weijie Yuan. It uses a 24 GHz radar and one backscatter tag, HFD signaling, and FS-MUSIC to exploit multipath for measured NLOS localization.

The previously prepared cellular-ISAC lineage remains part of the same public-artifact branch: Tosi et al.'s IEEE SPAWC 2024 feasibility paper and the final ICT 2026 intrusion-detection follow-up. The explorer count remains 268 because this run corrects N2LoS metadata rather than adding a duplicate paper.

Validation requirements for this branch are: README/index/survey/BibTeX agreement; MARMOT and N2LoS presence in the rebuilt PDF; final IEEE TMC DOI/venue visible in the PDF bibliography; successful LaTeX/BibTeX compilation with no undefined citations; and rendered first/radar pages large enough to rule out an empty or corrupt PDF.
"""


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def patch_marmot():
    path = "README.md"
    text = read(path)
    start = text.index("## Latest Additions")
    end = text.index("\n---", start)
    if MARMOT_TITLE not in text[start:end]:
        header = "|------|-------|----------------|----------------|"
        pos = text.index(header, start, end) + len(header)
        text = text[:pos] + "\n" + MARMOT_README_ROW + text[pos:]
    write(path, text)

    path = "article/5newscenes.tex"
    text = read(path)
    if MARMOT_KEY not in text:
        if text.count(MARMOT_ANCHOR) != 1:
            raise RuntimeError(f"survey anchor count is {text.count(MARMOT_ANCHOR)}, expected 1")
        text = text.replace(MARMOT_ANCHOR, MARMOT_ANCHOR + "\n\n" + MARMOT_SURVEY, 1)
    write(path, text)


def patch_n2los():
    path = "README.md"
    text = read(path)
    if N2LOS_OLD_ROW in text:
        text = text.replace(N2LOS_OLD_ROW, N2LOS_NEW_ROW, 1)
    elif N2LOS_NEW_ROW not in text:
        raise RuntimeError("N2LoS README row not found in expected old or new form")
    text = text.replace("**Update run: 8 August 2026.**", "**Update run: 9 August 2026.**")
    write(path, text)

    path = "index.html"
    text = read(path)
    if N2LOS_OLD_INDEX in text:
        text = text.replace(N2LOS_OLD_INDEX, N2LOS_NEW_INDEX, 1)
    elif N2LOS_NEW_INDEX not in text:
        raise RuntimeError("N2LoS index object not found in expected old or new form")
    text = text.replace("Updated 8 August 2026", "Updated 9 August 2026")
    write(path, text)

    path = "article/5newscenes.tex"
    text = read(path)
    if N2LOS_SURVEY_REPLACEMENT not in text:
        if text.count(N2LOS_SURVEY_SENTENCE) != 1:
            raise RuntimeError(f"N2LoS survey sentence count is {text.count(N2LOS_SURVEY_SENTENCE)}, expected 1")
        text = text.replace(N2LOS_SURVEY_SENTENCE, N2LOS_SURVEY_REPLACEMENT, 1)
    write(path, text)

    path = "egbib_merged_20260711.bib"
    text = read(path)
    pattern = r"@article\{shiN2LoS2025,\n.*?\n\}"
    matches = re.findall(pattern, text, flags=re.S)
    if len(matches) != 1:
        raise RuntimeError(f"N2LoS merged-bib entry count is {len(matches)}, expected 1")
    text = re.sub(pattern, N2LOS_BIB, text, count=1, flags=re.S)
    write(path, text)

    path = "bare_jrnl.tex"
    text = read(path)
    marker = "% 9 August 2026 citation trace: MARMOT survey consistency and N2LoS final IEEE TMC metadata synchronized.\n"
    if not text.startswith(marker):
        text = marker + text
    text = text.replace("through 6 August 2026", "through 9 August 2026")
    write(path, text)

    write("updates/2026-08-09-marmot-n2los-final-venue.md", UPDATE_NOTE)


def validate():
    readme = read("README.md")
    survey = read("article/5newscenes.tex")
    index = read("index.html")
    bib = read("egbib_merged_20260711.bib")
    tex = read("bare_jrnl.tex")

    start = readme.index("## Latest Additions")
    end = readme.index("\n---", start)
    assert MARMOT_TITLE in readme[start:end]
    assert MARMOT_KEY in survey
    assert "Masked transient pretraining" in survey
    assert f'title:"{MARMOT_TITLE}"' in index
    assert bib.count(MARMOT_KEY) == 1
    assert "2506.08470" in bib

    assert N2LOS_TITLE in readme
    assert "IEEE Transactions on Mobile Computing 25(5), 6002–6016 (2026)" in readme
    assert N2LOS_DOI in readme
    assert N2LOS_NEW_INDEX in index
    assert "final journal record appears" in survey
    assert bib.count("shiN2LoS2025") == 1
    assert bib.count(N2LOS_DOI) >= 2
    assert "Cheng, Qingqing and Yuan, Weijie" in bib
    assert "volume = {25}" in bib and "number = {5}" in bib and "pages = {6002--6016}" in bib
    assert "through 9 August 2026" in tex
    assert "**Update run: 9 August 2026.**" in readme
    assert "Updated 9 August 2026" in index
    assert '<div class="stat"><b>268</b><span>tracked latest entries</span></div>' in index

    assert "Feasibility of Non-Line-of-Sight Integrated Sensing and Communication at mmWave" in readme
    assert "International Conference on Telecommunications (ICT 2026), 25–30" in readme
    assert "tosiFeasibilityISACNLOS2024" in survey
    assert "tosiReliableISACNLOS2026" in survey


if __name__ == "__main__":
    patch_marmot()
    patch_n2los()
    validate()
    print("MARMOT + N2LoS + cellular-ISAC cross-artifact source consistency update passed.")
