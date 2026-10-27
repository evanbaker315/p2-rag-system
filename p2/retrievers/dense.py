"""Dense retriever (stage 1): embed every chunk once, embed the query, and rank chunks by cosine similarity.

Ported from the 12 lab's retrieve.py (load_bge, cached_doc_vectors, dense_rankings), on chunks instead
of whole articles. The embedder is bge-small-en-v1.5 by default; set [dense] model = "..." in p2.toml
to use another (potion-retrieval-32M is the other one the lab measured).

Every vector from p2.embed has length 1, so the dot product of a chunk vector and the query vector is
their cosine similarity, and one matrix product scores every chunk.
"""

from __future__ import annotations

import numpy as np

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False


class Dense(ChunkScorer):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.model = cfg.table("dense").get("model", embed.BGE)
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text: str) -> np.ndarray:
        if not len(self.chunks):
            return np.zeros(0, dtype=np.float32)
        query = self.embedder.encode([text])[0]
        return self.vectors @ query


def build(corpus, cfg):
    return Dense(corpus, cfg)
