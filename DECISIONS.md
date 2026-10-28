# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

I chose OSHA construction safety regulations because they have a lot of specific rules and section numbers that should work well for testing retrieval. I also liked that they are public domain, so I don't have to deal with licensing issues. I expect rerank to do the best since it actually looks at the passages before putting them in order. I think dense will probably do the worst because a lot of these questions involve exact regulation numbers and specific wording. BM25 should be pretty good at finding those exact matches.

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.


One choice was how many documents the reranker should look at. I used 20 candidates, but I also tested 10. With 20, MRR@10 was 0.800. With 10, it dropped to 0.672. The smaller version saved 5,923 input tokens per question and about 0.2 seconds. I would stick with 20 because that small time savings doesn't seem worth the drop in retrieval performance. The tradeoff is spending more tokens on every question.

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.


The agent originally drafted questions about soil types and SCUBA depth like they could be answered by my corpus. But the soil definitions were in an appendix that wasn't imported, and the SCUBA section only pointed to a different regulation. Those weren't useful questions for this gold set, so I didn't accept them as they were. I had the agent replace them with questions about guardrail height and backup alarms and checked the relevant sections. There was also a misfire question where none of the candidate documents was right. I read `1926.911` and marked that as relevant instead. This showed me that the agent finding a document with a related title isn't enough.

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?


I don't fully trust the 100% verified score for the cited answers. It says 8 out of 8 in-corpus answers passed and all 14 quotes were found, but that only means the quotes exist. It doesn't prove that every sentence is supported. The interval for 8 out of 8 is also (0.676, 1.), so it's a small sample. The a06 noise answer is a good example: the checker passed it even though its gold section wasn't retrieved and the explanation of 90 dBA over eight hours didn't have its own supporting quote. I'd trust this number more after manually checking more answers against the actual regulations.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.


One thing still wrong is that the OSHA corpus repeats the title in 288 of its 310 documents. For example, `corpora/own/docs/cfr29-1926.27.md` has the section title as a heading and again as the first line of text. That could make BM25 give those words too much weight. I would remove the duplicate line, rerun the systems with the same queries and labels, and compare the scores. If rankings change, then the cleanup mattered. There are also short documents that just point to Part 1910, which still make it hard to answer some questions.