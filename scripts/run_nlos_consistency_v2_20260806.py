from pathlib import Path
import runpy

source = Path("scripts/integrate_nlos_consistency_20260806.py")
text = source.read_text(encoding="utf-8")
start_token = 'if "bogerLombardPassiveAcousticCorners2023" not in article:\n'
end_token = 'if "alburadiPolarimetricRadarNLOS2025" not in article:\n'
start = text.find(start_token)
end = text.find(end_token, start + 1)
if start < 0 or end < 0 or end <= start:
    raise RuntimeError("Could not locate the bounded acoustic insertion block")
replacement = '''if "bogerLombardPassiveAcousticCorners2023" not in article:
    sommer_key = "\\\\cite{sommerPassiveAcousticNLOS2026}"
    if sommer_key not in article:
        raise RuntimeError("Sommer survey citation anchor not found")
    citation_pos = article.index(sommer_key)
    paragraph_start = article.rfind("\\n\\n", 0, citation_pos)
    paragraph_start = 0 if paragraph_start < 0 else paragraph_start + 2
    sentence = "Boger-Lombard, Slobodkin, and Katz first showed that acoustic interferometry can retrieve effective Green functions from cross-correlations of uncontrolled broadband noise, enabling passive localization and tracking of a human hidden around a corner without controlled active probing~\\\\cite{bogerLombardPassiveAcousticCorners2023}.\\n\\n"
    article = article[:paragraph_start] + sentence + article[paragraph_start:]
'''
patched = text[:start] + replacement + text[end:]
temporary = Path("scripts/.integrate_nlos_consistency_v2_runtime.py")
temporary.write_text(patched, encoding="utf-8")
try:
    runpy.run_path(str(temporary), run_name="__main__")
finally:
    temporary.unlink(missing_ok=True)
