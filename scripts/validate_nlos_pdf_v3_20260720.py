#!/usr/bin/env python3
import re
from pathlib import Path
from pypdf import PdfReader

log = Path("bare_jrnl.log").read_text(encoding="utf-8", errors="ignore")
for pattern in (
    r"Citation .* undefined",
    r"There were undefined references",
    r"undefined citations",
    r"Fatal error occurred",
):
    if re.search(pattern, log, flags=re.IGNORECASE):
        raise SystemExit(f"LaTeX validation failed: {pattern}")

pdf = Path("bare_jrnl.pdf")
if not pdf.exists() or pdf.stat().st_size < 100_000:
    raise SystemExit("bare_jrnl.pdf missing or unexpectedly small")
reader = PdfReader(str(pdf))
if len(reader.pages) < 10:
    raise SystemExit("Regenerated survey has an implausibly small page count")
compact = re.sub(
    r"[^a-z0-9]+",
    " ",
    "\n".join((page.extract_text() or "") for page in reader.pages).lower(),
)
for phrase in (
    "scan free transient acquisition",
    "spatial correlation super resolution for scan free nlos",
    "event camera passive nlos for moving objects",
    "real time scan free non line of sight imaging",
    "event enhanced passive non line of sight imaging for moving objects with physical embedding",
):
    if phrase not in compact:
        raise SystemExit(f"Expected PDF text missing: {phrase}")
print(f"Validated {len(reader.pages)} PDF pages.")
