"""Gather candidate documents for every own-corpus query, for judging by hand.

For each query in eval/own/queries.tsv, the candidates are the union of the top 10 of bm25, dense and
hybrid, plus up to 5 documents from a plain keyword search (every content word of the query in the
document), so the gold set is not built from one system's results. Candidates are listed in document
id order, not by any system's rank, with a checkbox, the title and the start of the text.

Judge by ticking a box ([x]) for each relevant document, then run with --qrels to turn the ticks into
eval/own/qrels.txt lines.

    uv run python scripts/candidates.py ../checklist/judge.md          # write the judging sheet
    uv run python scripts/candidates.py ../checklist/judge.md --qrels  # read the ticks, write qrels.txt
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from p2 import config, corpus as corpus_mod, retrievers
from p2.runfile import read_queries

STOP = set("a an and are as at be before by can do does for from get has have how if in is it may of on or the they to what when where which who with work workers".split())
BOX = re.compile(r"^- \[([ xX])\] `([^`]+)`")
QHEAD = re.compile(r"^## (\S+) ")


def keyword_hits(docs, text: str, limit: int = 5) -> list[str]:
    words = [w for w in re.findall(r"[a-z0-9.]+", text.lower()) if w not in STOP and len(w) > 2]
    if not words:
        return []
    hits = [d for d, doc in docs.items() if all(w in doc.text.lower() for w in words)]
    return sorted(hits, key=lambda d: len(docs[d].text))[:limit]


def snippet(doc, chars: int = 350) -> str:
    body = doc.text.split("\n", 1)[1] if "\n" in doc.text else doc.text
    lines = [l for l in body.splitlines() if l.strip()]
    if lines and lines[0].strip().rstrip(".") == doc.title.strip().rstrip("."):
        lines = lines[1:]
    text = " ".join(lines)
    return (text[:chars] + "...") if len(text) > chars else text


def write_sheet(out: Path) -> None:
    cfg = config.load()
    corp = corpus_mod.load(cfg.root, "own")
    systems = [retrievers.build(n, corp, cfg) for n in ("bm25", "dense", "hybrid")]
    queries, _ = read_queries(cfg.root / "eval" / "own" / "queries.tsv", require_origin=True)
    old = read_ticks(out) if out.is_file() else {}
    parts = [
        "# Own-corpus judging sheet",
        "",
        "Tick [x] every document that states the requirement the query asks about (your rule; write it in EVAL.md section 3).",
        "Candidates are in document id order, not ranked. Ticks already made are kept when the sheet is rebuilt.",
        "",
    ]
    for q in queries:
        found = set(keyword_hits(corp.docs, q.text))
        for s in systems:
            found.update(d for d, _ in s.search(q.text, 10))
        parts.append(f"## {q.qid} ({q.cls}, {q.origin}): {q.text}")
        parts.append("")
        for d in sorted(found):
            mark = "x" if d in old.get(q.qid, set()) else " "
            parts.append(f"- [{mark}] `{d}` **{corp.docs[d].title}** - {snippet(corp.docs[d])}")
        parts.append("")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {out}: {len(queries)} queries.")


def read_ticks(sheet: Path) -> dict[str, set[str]]:
    ticks: dict[str, set[str]] = {}
    qid = None
    for line in sheet.read_text(encoding="utf-8").splitlines():
        m = QHEAD.match(line)
        if m:
            qid = m.group(1)
            ticks.setdefault(qid, set())
            continue
        m = BOX.match(line)
        if m and qid and m.group(1).lower() == "x":
            ticks[qid].add(m.group(2))
    return ticks


def write_qrels(sheet: Path) -> None:
    cfg = config.load()
    ticks = read_ticks(sheet)
    lines = ["# Relevance judgments: qid 0 docid 1, separated by spaces. Every query needs at least one relevant document."]
    lines += [f"{q} 0 {d} 1" for q in ticks for d in sorted(ticks[q])]
    (cfg.root / "eval" / "own" / "qrels.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    empty = [q for q, ds in ticks.items() if not ds]
    print(f"Wrote eval/own/qrels.txt: {sum(len(v) for v in ticks.values())} judgments over {len(ticks)} queries.")
    if empty:
        print("No relevant document ticked yet for: " + ", ".join(empty))


if __name__ == "__main__":
    sheet = Path(sys.argv[1])
    write_qrels(sheet) if "--qrels" in sys.argv else write_sheet(sheet)
