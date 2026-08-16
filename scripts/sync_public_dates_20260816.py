from pathlib import Path

corpus_path = Path('data/papers-source.html')
tex_path = Path('bare_jrnl.tex')
note_path = Path('updates/2026-08-16-cross-artifact-date-sync.md')

corpus = corpus_path.read_text(encoding='utf-8')
old_footer = 'Last updated: 15 August 2026'
new_footer = 'Last updated: 16 August 2026'
if old_footer in corpus:
    corpus = corpus.replace(old_footer, new_footer, 1)
elif new_footer not in corpus:
    raise SystemExit('Refusing unsafe edit: canonical V2 footer date anchor not found')
if 'Updated 16 August 2026 · 210+ papers' not in corpus:
    raise SystemExit('Refusing unsafe edit: V2 header is not already at 16 August 2026')
corpus_path.write_text(corpus, encoding='utf-8')

tex = tex_path.read_text(encoding='utf-8')
old_tex = 'through 15 August 2026.'
new_tex = 'through 16 August 2026.'
if old_tex in tex:
    tex = tex.replace(old_tex, new_tex, 1)
elif new_tex not in tex:
    raise SystemExit('Refusing unsafe edit: survey coverage-date anchor not found')
comment = '% 16 August 2026 consistency audit: synchronized the V2 footer and survey snapshot date after the latest literature integrations.\n'
if comment.strip() not in tex:
    tex = comment + tex
tex_path.write_text(tex, encoding='utf-8')

note = '''# 16 August 2026 cross-artifact date synchronization

No additional high-confidence missing NLOS paper was added in this audit. Fresh recent-paper searches and core-paper citation tracing were checked against the current README, canonical V2 paper corpus, survey prose, and merged bibliography. The paper content was already synchronized.

This maintenance update closes two date-only inconsistencies left after the 16 August literature integrations: the canonical V2 homepage header already reported 16 August 2026 while its footer still reported 15 August 2026, and the survey source title note still stated that coverage extended through 15 August 2026 even though 16 August additions were already integrated. The footer and survey snapshot date are therefore synchronized to 16 August 2026, and `bare_jrnl.pdf` is rebuilt and validated from the corrected source by the accompanying CI workflow.
'''
note_path.write_text(note, encoding='utf-8')

print('Synchronized V2 footer and survey coverage date to 16 August 2026.')
