from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "MARMOT: Masked Autoencoder for Modeling Transient Imaging"
KEY = "shenMARMOT2025"
README_ROW = "| 2025 | [MARMOT: Masked Autoencoder for Modeling Transient Imaging](https://arxiv.org/abs/2506.08470) — Shen et al. | arXiv 2025 | Introduces self-supervised masked-autoencoder pretraining for transient/NLOS data. A scanning-pattern mask makes the retained samples equivalent to arbitrary relay sampling; pretraining on the 500K-model TransVerse synthetic transient corpus enables reusable features and measurement completion for downstream hidden-scene tasks. No final journal or conference venue could be verified as of 8 August 2026. |"
SURVEY = r'''\vspace{0.8mm}
\noindent \textbf{Masked transient pretraining.}
Shen~\etal~introduced MARMOT, a self-supervised masked autoencoder that treats transient measurements as a reusable pretraining modality rather than training a separate reconstruction network for every NLOS task~\cite{shenMARMOT2025}. Its scanning-pattern mask removes structured subsets of relay measurements so that the visible tokens are functionally equivalent to arbitrary sparse sampling, while a Transformer encoder--decoder predicts the missing transient measurements. Pretraining on the TransVerse corpus of 500,000 synthetic 3D models allows the learned transient representation to transfer to downstream reconstruction through direct feature reuse or decoder fine-tuning. This work marks a shift from task-specific transient inversion toward foundation-style measurement priors that can support sparse acquisition, transient completion, and multiple NLOS objectives.'''
ANCHOR = "Together, these works bridge classical dense ToF NLOS and the newer arbitrary-relay / mobile-capture setting: they show that practical NLOS deployment depends not only on faster solvers, but also on inverse models that remain well posed when the relay surface is incomplete, irregular, or sparsely sampled."


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def patch_readme():
    path = "README.md"
    text = read(path)
    if TITLE not in text:
        start = text.index("## Latest Additions")
        end = text.index("\n---", start)
        header = "|------|-------|----------------|----------------|"
        pos = text.index(header, start, end) + len(header)
        text = text[:pos] + "\n" + README_ROW + text[pos:]
    else:
        # MARMOT may already occur in the timeline; ensure a paper row exists in Latest Additions.
        start = text.index("## Latest Additions")
        end = text.index("\n---", start)
        if TITLE not in text[start:end]:
            header = "|------|-------|----------------|----------------|"
            pos = text.index(header, start, end) + len(header)
            text = text[:pos] + "\n" + README_ROW + text[pos:]
    write(path, text)


def patch_survey():
    path = "article/5newscenes.tex"
    text = read(path)
    if KEY not in text:
        if text.count(ANCHOR) != 1:
            raise RuntimeError(f"survey anchor count is {text.count(ANCHOR)}, expected 1")
        text = text.replace(ANCHOR, ANCHOR + "\n\n" + SURVEY, 1)
    write(path, text)


def validate():
    readme = read("README.md")
    survey = read("article/5newscenes.tex")
    index = read("index.html")
    bib = read("egbib_merged_20260711.bib")
    start = readme.index("## Latest Additions")
    end = readme.index("\n---", start)
    assert TITLE in readme[start:end]
    assert KEY in survey
    assert "Masked transient pretraining" in survey
    assert f'title:"{TITLE}"' in index
    assert bib.count(KEY) == 1
    assert "2506.08470" in bib


if __name__ == "__main__":
    patch_readme()
    patch_survey()
    validate()
    print("MARMOT cross-artifact source consistency update passed.")
