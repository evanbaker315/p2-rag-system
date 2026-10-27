"""A cheaper reranker (stretch option 3): the same as rerank, over hybrid's top 10 instead of its top 20.

Everything else (the prompt, the passage length, the model, the first stage) is rerank.py's, so the
difference between the two measures what the second ten candidates buy.
"""

from __future__ import annotations

from p2.retrievers.rerank import Rerank

NEEDS_CLAUDE = True
BASE = "rerank"


class RerankC10(Rerank):
    candidates = 10


def build(corpus, cfg):
    return RerankC10(corpus, cfg)
