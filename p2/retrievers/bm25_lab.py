"""Ablation: bm25 with the 12 lab's plain [a-z0-9]+ tokenizer instead of the "codes" tokenizer.

The one change is the tokenizer: "codes" keeps section numbers such as 1926.501 whole and also
indexes their parts, while "lab" splits them into 1926 and 501. Everything else (k1, b, chunking)
is p2.toml's, through a changed copy of the settings.
"""

from __future__ import annotations

from p2.retrievers.bm25 import BM25

NEEDS_CLAUDE = False
BASE = "bm25"


def build(corpus, cfg):
    return BM25(corpus, cfg.replace(tokenizer="lab"))
