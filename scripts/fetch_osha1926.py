"""Fetch 29 CFR part 1926 (OSHA, Safety and Health Regulations for Construction) from the eCFR
versioner API and write one Markdown file per section into ../p2-raw/osha1926/, the input to
`uv run p2 ingest`.

The format follows corpora/shared/NOTICE.md, so the two corpora are built the same way:
- file name and document id `cfr29-` plus the section number, for example `cfr29-1926.501`;
- first line `# ` plus the section number and heading without the section sign, a blank line, the body;
- each paragraph one line, a blank line between paragraphs; each table row one line, cells joined by ` | `;
- history citations, authority and source lines, editorial notes and images are left out;
- sections marked [Reserved] are left out.

Run from the repo root: uv run python scripts/fetch_osha1926.py
"""

from __future__ import annotations

import gzip
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

DATE = "2026-10-14"
URL = f"https://www.ecfr.gov/api/versioner/v1/full/{DATE}/title-29.xml?part=1926"
OUT = Path(__file__).resolve().parents[2] / "p2-raw" / "osha1926"
SKIP = {"CITA", "AUTH", "SOURCE", "EDNOTE", "img", "SECAUTH", "FTREF"}
BLOCKS = {"P", "FP", "FP-1", "FP-2", "FP1-2", "HD1", "HD2", "HD3", "NOTE", "EXTRACT", "PSPACE", "FTNT", "CAPTION"}


def fetch() -> bytes:
    request = urllib.request.Request(URL, headers={"Accept-Encoding": "gzip"})
    with urllib.request.urlopen(request, timeout=300) as reply:
        data = reply.read()
        return gzip.decompress(data) if reply.headers.get("Content-Encoding") == "gzip" else data


def text_of(el: ET.Element) -> str:
    """The text of an element with inline markup flattened: sup and sub inline, img dropped."""
    parts = [el.text or ""]
    for child in el:
        if child.tag == "img":
            pass
        elif child.tag == "sup":
            parts.append("^" + text_of(child) if (child.text or "").strip().isdigit() else "")
        elif child.tag == "br":
            parts.append(" ")
        else:
            parts.append(text_of(child))
        parts.append(child.tail or "")
    return re.sub(r"\s+", " ", "".join(parts)).strip()


def lines_of(el: ET.Element) -> list[str]:
    out: list[str] = []
    for child in el:
        tag = child.tag
        if tag in SKIP or tag == "HEAD":
            continue
        if tag == "TABLE" or tag == "GPOTABLE":
            for row in child.iter("TR"):
                cells = [text_of(c) for c in row if c.tag in ("TD", "TH")]
                if any(cells):
                    out.append(" | ".join(cells))
            continue
        if tag in BLOCKS and not any(g.tag in BLOCKS or g.tag in ("TABLE", "GPOTABLE") for g in child):
            line = text_of(child)
            if line:
                out.append(line)
            continue
        out.extend(lines_of(child))  # a container (DIV, NOTE with paragraphs, EXTRACT): go inside
    return out


def main() -> int:
    root = ET.fromstring(fetch())
    OUT.mkdir(parents=True, exist_ok=True)
    written = skipped = 0
    for sec in root.iter("DIV8"):
        number = sec.get("N", "").strip()
        head = text_of(sec.find("HEAD")) if sec.find("HEAD") is not None else number
        head = re.sub(r"^§+\s*", "", head)
        body = lines_of(sec)
        if "[Reserved]" in head or not body:
            skipped += 1
            continue
        docid = "cfr29-" + number.lower()
        (OUT / f"{docid}.md").write_text(f"# {head}\n\n" + "\n\n".join(body) + "\n", encoding="utf-8", newline="\n")
        written += 1
    print(f"Wrote {written} sections to {OUT} ({skipped} reserved or empty left out).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
