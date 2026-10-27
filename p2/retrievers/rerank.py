"""Reranker (stage 1): ask Claude to reorder hybrid's top 20.

Ported from rerank_one() in the 13 lab's pipeline.py: the candidates go to Claude as numbered
passages, the reply is forced into {"order": [each passage number once]}, a reply that is not a
permutation keeps the first-stage order, and the documents below the candidates keep their
first-stage order underneath.

Changes from the lab:
- the schema's items carry "minimum": 1 and "maximum": n, so Claude cannot name a passage that does not exist;
- the prompt names a document collection, not a help center, so the same reranker works on both corpora;
- passages are cut to PASSAGE_CHARS characters (the lab used 600, which cuts off most CFR sections
  before their requirement);
- every call goes through p2.claude.call, which caches replies and records tokens in the run's trace.

Scores in the run file are 1 / rank, so they fall with the rank and never tie.
A variant (stretch option 3) can subclass Rerank with a different CANDIDATES.
"""

from __future__ import annotations

from p2 import claude, retrievers

NEEDS_CLAUDE = True

FIRST_STAGE = "hybrid"
CANDIDATES = 20
PASSAGE_CHARS = 1500

PROMPT = """Below are {n} passages from a document collection, numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


def schema(n: int) -> dict:
    return {
        "type": "object",
        "properties": {
            "order": {
                "type": "array",
                "items": {"type": "integer", "minimum": 1, "maximum": n},
                "minItems": n,
                "maxItems": n,
            }
        },
        "required": ["order"],
    }


class Rerank:
    candidates = CANDIDATES

    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.cfg = cfg
        self.model = cfg.model
        self.first = retrievers.build(FIRST_STAGE, corpus, cfg)
        self.chunk_text = corpus.chunk_texts(cfg.chunk_words, cfg.chunk_overlap)

    def _rerank(self, query: str, ids: list[str], text_of) -> list[str]:
        """The candidate ids in Claude's order, or in their own order if the reply is unusable."""
        n = len(ids)
        if n < 2:
            return ids
        passages = "\n\n".join(f"[{i}] {text_of(d)[:PASSAGE_CHARS]}" for i, d in enumerate(ids, 1))
        reply = claude.call(
            PROMPT.format(n=n, query=query, passages=passages),
            schema(n),
            model=self.cfg.model,
            cache_dir=claude.cache_folder(self.cfg),
        )
        order = (reply.output or {}).get("order") if reply.error is None else None
        if not isinstance(order, list) or sorted(order) != list(range(1, n + 1)):
            return ids
        return [ids[i - 1] for i in order]

    def _ranked(self, query: str, first: list[tuple[str, float]], text_of, k: int) -> list[tuple[str, float]]:
        ids = [d for d, _ in first]
        top = self._rerank(query, ids[: self.candidates], text_of)
        ranked = top + ids[self.candidates :]
        return [(d, 1.0 / rank) for rank, d in enumerate(ranked, 1)][:k]

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        first = self.first.search(text, max(k, self.candidates))
        return self._ranked(text, first, lambda d: self.corpus.docs[d].text, k)

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        first = self.first.search_chunks(text, max(k, self.candidates))
        return self._ranked(text, first, lambda c: self.chunk_text[c], k)


def build(corpus, cfg):
    return Rerank(corpus, cfg)
