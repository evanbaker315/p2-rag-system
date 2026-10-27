"""Hybrid retriever (stage 1): reciprocal rank fusion of bm25 and dense.

Ported from rrf() in the 13 lab's pipeline.py: each item scores the sum of 1 / (60 + rank) over the
two rankings, with ranks starting at 1. Both rankings are full (every document, or every chunk), so a
document that is 11th in both lists can still reach the fused top 10.

search fuses document rankings; search_chunks fuses chunk rankings, which `p2 answer` and the
reranker's chunk search use.
"""

from __future__ import annotations

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False

RRF_K = 60
PARTS = ("bm25", "dense")


def rrf(rankings: list[list[tuple[str, float]]], k: int = RRF_K) -> list[tuple[str, float]]:
    """Fuse full rankings of (id, score) pairs: each id scores the sum of 1 / (k + rank)."""
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, (item, _score) in enumerate(ranking, 1):
            scores[item] = scores.get(item, 0.0) + 1.0 / (k + rank)
    return order(scores.items())


class Hybrid:
    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.parts = [retrievers.build(name, corpus, cfg) for name in PARTS]
        self.n_docs = len(corpus.docs)
        self.n_chunks = len(corpus.chunks(cfg.chunk_words, cfg.chunk_overlap))

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        return rrf([p.search(text, self.n_docs) for p in self.parts])[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        return rrf([p.search_chunks(text, self.n_chunks) for p in self.parts])[:k]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
