#!/usr/bin/env python3
"""Create one duplicate-free, citation-key-consistent survey bibliography.

Chronological supplements intentionally supersede older metadata, while the
legacy Zotero export lower-cased many identifiers that remain mixed-case in the
LaTeX sources. Classic BibTeX treats keys case-insensitively for duplicates but
requires compatible citation spelling. This script therefore merges source
files by case-folded key, gives later supplements priority, renames each final
record to the exact spelling used by the survey when unambiguous, audits truly
missing references with source locations, and points ``bare_jrnl.tex`` to the
consolidated database.
"""
from __future__ import annotations

from collections import OrderedDict, defaultdict
from pathlib import Path
import re

import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "egbib_merged_20260711.bib"
NOTE = ROOT / "updates/2026-07-11-bibliography-deduplication.md"
CITE_RE = re.compile(r"\\cite[a-zA-Z*]*\s*(?:\[[^]]*\]\s*)?\{([^}]+)\}")


def source_files() -> list[Path]:
    all_files = [p for p in ROOT.glob("egbib*.bib") if p.name != OUTPUT.name]
    base = ROOT / "egbib.bib"
    broad = ROOT / "egbib_2026_updates.bib"
    ordered: list[Path] = []
    for preferred in (base, broad):
        if preferred in all_files:
            ordered.append(preferred)
    ordered.extend(sorted(p for p in all_files if p not in ordered))
    if not ordered:
        raise RuntimeError("No egbib*.bib sources were found")
    return ordered


def load_entries(path: Path) -> list[dict[str, str]]:
    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    with path.open("r", encoding="utf-8-sig") as handle:
        database = bibtexparser.load(handle, parser=parser)
    if not database.entries:
        raise RuntimeError(f"No BibTeX entries parsed from {path.name}")
    return database.entries


def citation_inventory() -> tuple[dict[str, set[str]], dict[str, list[str]]]:
    forms: dict[str, set[str]] = defaultdict(set)
    locations: dict[str, list[str]] = defaultdict(list)
    paths = [ROOT / "bare_jrnl.tex", *sorted((ROOT / "article").glob("*.tex"))]
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for match in CITE_RE.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            for raw in match.group(1).split(","):
                key = raw.strip()
                if not key:
                    continue
                forms[key.casefold()].add(key)
                locations[key].append(f"{path.relative_to(ROOT)}:{line}")
    return forms, locations


def main() -> None:
    sources = source_files()
    cite_forms, cite_locations = citation_inventory()
    merged: OrderedDict[str, tuple[str, str, dict[str, str]]] = OrderedDict()
    replacements: list[tuple[str, str, str, str, str]] = []
    parsed_total = 0

    for source in sources:
        entries = load_entries(source)
        parsed_total += len(entries)
        for entry in entries:
            key = entry.get("ID", "").strip()
            if not key:
                raise RuntimeError(f"Parsed entry without ID in {source.name}")
            folded = key.casefold()
            if folded in merged:
                old_source, old_key, _old_entry = merged[folded]
                replacements.append((old_key, key, old_source, source.name, folded))
                del merged[folded]
            merged[folded] = (source.name, key, entry)

    ambiguous_forms: list[tuple[str, list[str]]] = []
    normalized: list[tuple[str, str]] = []
    final_entries: OrderedDict[str, dict[str, str]] = OrderedDict()
    for folded, (_source, original_key, entry) in merged.items():
        forms = sorted(cite_forms.get(folded, set()))
        if len(forms) == 1:
            canonical = forms[0]
        elif original_key in forms:
            canonical = original_key
            ambiguous_forms.append((folded, forms))
        elif forms:
            canonical = forms[0]
            ambiguous_forms.append((folded, forms))
        else:
            canonical = original_key
        if canonical != original_key:
            normalized.append((original_key, canonical))
        entry["ID"] = canonical
        if canonical.casefold() in (k.casefold() for k in final_entries):
            raise RuntimeError(f"Case-insensitive duplicate survived merge: {canonical}")
        final_entries[canonical] = entry

    final_folded = {key.casefold() for key in final_entries}
    missing_forms = sorted(set(cite_forms).difference(final_folded))
    missing_details: list[tuple[str, list[str]]] = []
    for folded in missing_forms:
        for spelling in sorted(cite_forms[folded]):
            missing_details.append((spelling, cite_locations.get(spelling, [])))

    database = BibDatabase()
    database.entries = list(final_entries.values())
    writer = BibTexWriter()
    writer.indent = "  "
    writer.order_entries_by = None
    rendered = writer.write(database)
    header = (
        "% Auto-generated duplicate-free bibliography for bare_jrnl.tex.\n"
        "% Generated by scripts/merge_nlos_bibliography.py.\n"
        "% Keys are deduplicated case-insensitively and normalized to survey citations.\n\n"
    )
    OUTPUT.write_text(header + rendered, encoding="utf-8")

    tex_path = ROOT / "bare_jrnl.tex"
    tex = tex_path.read_text(encoding="utf-8")
    pattern = re.compile(r"(?m)^\\bibliography\{[^}]+\}\s*$")
    matches = pattern.findall(tex)
    if len(matches) != 1:
        raise RuntimeError(f"Expected exactly one active bibliography command, found {len(matches)}")
    tex = pattern.sub(lambda _m: r"\bibliography{egbib_merged_20260711}", tex, count=1)
    tex_path.write_text(tex, encoding="utf-8")

    replacement_lines = "\n".join(
        f"- `{old_key}` / `{new_key}`: `{old_source}` → `{new_source}`"
        for old_key, new_key, old_source, new_source, _folded in replacements
    ) or "- None."
    normalization_lines = "\n".join(
        f"- `{old}` → `{new}`" for old, new in normalized
    ) or "- None."
    ambiguity_lines = "\n".join(
        f"- case-folded `{folded}`: " + ", ".join(f"`{form}`" for form in forms)
        for folded, forms in ambiguous_forms
    ) or "- None."
    missing_lines = "\n".join(
        f"- `{key}` — " + ", ".join(f"`{location}`" for location in locations)
        for key, locations in missing_details
    ) or "- None."
    note = f"""# 11 July 2026 bibliography deduplication and citation-key audit

The survey previously passed chronological `egbib*.bib` supplements directly to BibTeX. Several correction files repeat keys, and the legacy Zotero export lower-cased many identifiers that remain mixed-case in the LaTeX sources. Both conditions can prevent a reproducible clean build.

This update generates `egbib_merged_20260711.bib` from {len(sources)} source files and keeps one highest-priority record for each of {len(final_entries)} case-insensitively unique keys. Priority is deterministic: `egbib.bib`, then `egbib_2026_updates.bib`, followed by dated supplements in chronological filename order, so later corrections override older records. The selected records are then renamed to the exact citation spelling used by the survey whenever the mapping is unambiguous. `bare_jrnl.tex` uses only the consolidated bibliography.

- Parsed source records: {parsed_total}
- Case-insensitive duplicate replacements: {len(replacements)}
- Citation-key case normalizations: {len(normalized)}
- Ambiguous citation spellings: {len(ambiguous_forms)}
- Truly missing citation keys: {len(missing_details)}

## Duplicate records resolved

{replacement_lines}

## Citation-key spellings normalized

{normalization_lines}

## Ambiguous citation spellings

{ambiguity_lines}

## Truly missing citation keys and source locations

{missing_lines}

The CI workflow performs a clean LaTeX/BibTeX build, rejects undefined citations or repeated entries, validates the PDF with `pdfinfo` and `pdftotext`, and verifies that the newly integrated X-band radar and Neural Illumination Fields records appear in the generated bibliography.
"""
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    NOTE.write_text(note, encoding="utf-8")

    print(
        f"Merged {parsed_total} records into {len(final_entries)} case-insensitive keys; "
        f"normalized {len(normalized)} citation spellings; "
        f"missing {len(missing_details)} cited keys."
    )


if __name__ == "__main__":
    main()
