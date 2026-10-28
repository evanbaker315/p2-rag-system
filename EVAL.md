# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.


Dense uses bge-small-en-v1.5 embeddings to find documents with similar meaning. I split documents into 300-word chunks with 50 words of overlap. Hybrid combines BM25 and dense with reciprocal rank fusion (k=60), so it can use both exact words and semantic matches. Rerank takes the top 20 hybrid results and has Claude Sonnet reorder them. I changed the lab reranker to send up to 1,500 characters per passage instead of 600 because some regulations are too long to fit in 600 characters.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.592 | 0.471 | 0.443 |
| rerank | 0.733 | 0.800 | 0.746 |
| rerank_c10 | 0.592 | 0.672 | 0.590 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.500 | 0.405 | 0.917 |
| hybrid | MRR@10 | 0.514 | 0.152 | 0.792 |
| hybrid | nDCG@10 | 0.397 | 0.202 | 0.779 |
| rerank | Recall@10 | 0.643 | 0.595 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.714 | 1.000 |
| rerank | nDCG@10 | 0.648 | 0.626 | 1.000 |
| rerank_c10 | Recall@10 | 0.500 | 0.405 | 0.917 |
| rerank_c10 | MRR@10 | 0.492 | 0.571 | 1.000 |
| rerank_c10 | nDCG@10 | 0.443 | 0.440 | 0.936 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.033 | [-0.250, +0.192] | 0.324 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.037 | [-0.178, +0.083] | 0.192 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.075 | [-0.238, +0.075] | 0.228 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.033 | [-0.125, +0.192] | 0.231 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.092 | [-0.306, +0.109] | 0.301 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.036 | [-0.200, +0.113] | 0.227 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.108 | [-0.133, +0.350] | 0.351 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.293 | [+0.043, +0.533] | 0.353 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.227 | [-0.009, +0.452] | 0.335 | not distinguishable |
| rerank minus dense | Recall@10 | +0.175 | [+0.033, +0.333] | 0.221 | rerank higher |
| rerank minus dense | MRR@10 | +0.237 | [+0.083, +0.408] | 0.239 | rerank higher |
| rerank minus dense | nDCG@10 | +0.266 | [+0.128, +0.417] | 0.212 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.142 | [+0.050, +0.258] | 0.160 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | 0.247 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.302 | [+0.177, +0.432] | 0.187 | rerank higher |
| rerank_c10 minus bm25 | Recall@10 | -0.033 | [-0.250, +0.192] | 0.324 | not distinguishable |
| rerank_c10 minus bm25 | MRR@10 | +0.165 | [-0.117, +0.432] | 0.392 | not distinguishable |
| rerank_c10 minus bm25 | nDCG@10 | +0.072 | [-0.176, +0.311] | 0.352 | not distinguishable |
| rerank_c10 minus dense | Recall@10 | +0.033 | [-0.125, +0.192] | 0.231 | not distinguishable |
| rerank_c10 minus dense | MRR@10 | +0.110 | [-0.106, +0.312] | 0.307 | not distinguishable |
| rerank_c10 minus dense | nDCG@10 | +0.110 | [-0.068, +0.280] | 0.254 | not distinguishable |
| rerank_c10 minus hybrid | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| rerank_c10 minus hybrid | MRR@10 | +0.202 | [+0.003, +0.396] | 0.283 | rerank_c10 higher |
| rerank_c10 minus hybrid | nDCG@10 | +0.147 | [+0.027, +0.269] | 0.175 | rerank_c10 higher |
| rerank_c10 minus rerank | Recall@10 | -0.142 | [-0.258, -0.050] | 0.160 | rerank higher |
| rerank_c10 minus rerank | MRR@10 | -0.128 | [-0.278, +0.000] | 0.199 | not distinguishable |
| rerank_c10 minus rerank | nDCG@10 | -0.156 | [-0.275, -0.052] | 0.160 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time. Two systems that score the same on every query have no interval to speak of, so their MDD is shown as -.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?


On the 20 practice questions, rerank had the best MRR@10 at 0.800. Dense got 0.562, BM25 got 0.507, and hybrid got 0.471. Rerank was higher than all three on MRR, and those confidence intervals did not include zero. But the differences between BM25, dense, and hybrid all included zero, so I can't say one of those three was clearly better. For example, dense beat BM25 by only 0.055, while that comparison had an MDD of 0.412. With just 20 questions, smaller differences are hard to detect. The results support the idea that reranking can improve the order of retrieved documents. They don't show that combining BM25 and dense always improves retrieval. BM25 was better at identifier questions, while dense handled paraphrases much better.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hybrid | hybrid | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 14 of 14 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.


I used hybrid for the 12 cited answers because it combines keyword and semantic search without paying for an extra reranker call. I didn't change `prompts/answer.txt`, so there isn't a before-and-after prompt result to compare. All 8 in-corpus answers passed verification, all 4 out-of-corpus questions were declined, and all 14 quoted passages were found. That sounds good, but passing the checker isn't the same as being correct.

For a03, the quote from `cfr30-75.1714` directly says the self-rescue device must protect a miner for at least one hour, so it supports the answer. For a07, the quotes from `cfr30-56.9300` and `cfr30-57.9300` support the mid-axle-height rule for berms and guardrails. For a06, the quotes support the 90-dB criterion, the 5-dB exchange rate, full-shift monitoring, and the 115-dBA maximum. But the sentence saying the permissible exposure level equals 90 dBA over eight hours wasn't directly backed by one of its quoted claims, and the gold section `cfr30-62.101` wasn't retrieved. So I wouldn't call that answer fully supported just because it passed verification.

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.


My corpus is OSHA construction safety rules from 29 CFR Part 1926, pulled from the eCFR API. It is a federal government regulations source, which was one of the allowed source types. I ended up with 310 documents, about 365,000 words, and 2.41 MB of files. I used the US government public-domain license basis, and `p2 license` reported 310 OK, 0 flagged, and 0 failing.

I was less sure about the short documents that only point to another rule, like `cfr29-1926.1102`, because they don't actually give the requirement. I kept them as part of the real corpus but didn't count a pointer alone as relevant. Some long regulations were also split into multiple documents. The corpus fits the size limits, although those short references are still a weakness.


### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.


---

My gold set has 30 questions, 20 from `claude` and 10 from `hand`. There are 10 identifier questions, 11 paraphrase questions, and 9 mixed questions. I used all three types so I could test exact section numbers, regular everyday wording, and questions that combine both.

My rule was simple, a document is relevant if it actually states the rule needed to answer the question. Just mentioning the topic or pointing to another section does not count. I used binary labels, so relevant is 1 and everything else is 0. Candidates came from the top 10 results of BM25, dense, and hybrid, plus a keyword search. The judging was done against those candidate documents and their text, not by reading all 310 documents from start to finish. The final set has 39 relevant-document judgments across the 30 questions.

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.767 | 0.635 | 0.652 |
| dense | 0.933 | 0.693 | 0.744 |
| hybrid | 0.850 | 0.769 | 0.765 |
| rerank | 0.942 | 0.933 | 0.920 |
| ablation/bm25_lab | 0.767 | 0.618 | 0.639 |

30 judged queries; nDCG uses binary labels; a random ranking of the 310 documents would get recall@10 near 0.032.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | identifier (n=10) | paraphrase (n=11) | mixed (n=9) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.500 | 0.833 |
| bm25 | MRR@10 | 0.950 | 0.299 | 0.694 |
| bm25 | nDCG@10 | 0.969 | 0.310 | 0.716 |
| dense | Recall@10 | 0.900 | 0.909 | 1.000 |
| dense | MRR@10 | 0.733 | 0.586 | 0.778 |
| dense | nDCG@10 | 0.774 | 0.644 | 0.832 |
| hybrid | Recall@10 | 1.000 | 0.636 | 0.944 |
| hybrid | MRR@10 | 0.883 | 0.591 | 0.861 |
| hybrid | nDCG@10 | 0.915 | 0.540 | 0.873 |
| rerank | Recall@10 | 1.000 | 0.864 | 0.972 |
| rerank | MRR@10 | 0.900 | 0.909 | 1.000 |
| rerank | nDCG@10 | 0.928 | 0.863 | 0.981 |
| ablation/bm25_lab | Recall@10 | 1.000 | 0.500 | 0.833 |
| ablation/bm25_lab | MRR@10 | 0.900 | 0.299 | 0.694 |
| ablation/bm25_lab | nDCG@10 | 0.932 | 0.310 | 0.716 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=10) | claude (n=20) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.650 | 0.825 | -0.175 | [-0.500, +0.125] | not distinguishable |
| bm25 | MRR@10 | 0.463 | 0.721 | -0.258 | [-0.562, +0.062] | not distinguishable |
| bm25 | nDCG@10 | 0.505 | 0.725 | -0.219 | [-0.519, +0.090] | not distinguishable |
| dense | Recall@10 | 1.000 | 0.900 | +0.100 | [+0.000, +0.250] | not distinguishable |
| dense | MRR@10 | 0.775 | 0.651 | +0.124 | [-0.150, +0.386] | not distinguishable |
| dense | nDCG@10 | 0.828 | 0.701 | +0.127 | [-0.083, +0.331] | not distinguishable |
| hybrid | Recall@10 | 0.800 | 0.875 | -0.075 | [-0.325, +0.150] | not distinguishable |
| hybrid | MRR@10 | 0.825 | 0.742 | +0.083 | [-0.200, +0.333] | not distinguishable |
| hybrid | nDCG@10 | 0.778 | 0.758 | +0.019 | [-0.245, +0.261] | not distinguishable |
| rerank | Recall@10 | 0.975 | 0.925 | +0.050 | [-0.050, +0.175] | not distinguishable |
| rerank | MRR@10 | 1.000 | 0.900 | +0.100 | [+0.000, +0.225] | not distinguishable |
| rerank | nDCG@10 | 0.983 | 0.889 | +0.095 | [+0.001, +0.217] | hand higher |
| ablation/bm25_lab | Recall@10 | 0.650 | 0.825 | -0.175 | [-0.500, +0.125] | not distinguishable |
| ablation/bm25_lab | MRR@10 | 0.412 | 0.721 | -0.308 | [-0.592, +0.000] | not distinguishable |
| ablation/bm25_lab | nDCG@10 | 0.469 | 0.725 | -0.256 | [-0.536, +0.039] | not distinguishable |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | -0.075 | -0.350 | +0.275 | [-0.050, +0.600] | not distinguishable |
| MRR@10 | +0.069 | -0.312 | +0.382 | [+0.114, +0.671] | bm25 gains more on claude queries |
| nDCG@10 | +0.024 | -0.323 | +0.346 | [+0.093, +0.612] | bm25 gains more on claude queries |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.58 (10 queries), claude 0.76 (20 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 10 hand and 20 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | +0.167 | [+0.017, +0.317] | 0.216 | dense higher |
| dense minus bm25 | MRR@10 | +0.058 | [-0.089, +0.202] | 0.211 | not distinguishable |
| dense minus bm25 | nDCG@10 | +0.092 | [-0.047, +0.227] | 0.197 | not distinguishable |
| hybrid minus bm25 | Recall@10 | +0.083 | [+0.017, +0.150] | 0.097 | hybrid higher |
| hybrid minus bm25 | MRR@10 | +0.135 | [+0.022, +0.258] | 0.172 | hybrid higher |
| hybrid minus bm25 | nDCG@10 | +0.113 | [+0.030, +0.202] | 0.126 | hybrid higher |
| hybrid minus dense | Recall@10 | -0.083 | [-0.217, +0.033] | 0.179 | not distinguishable |
| hybrid minus dense | MRR@10 | +0.077 | [-0.024, +0.183] | 0.149 | not distinguishable |
| hybrid minus dense | nDCG@10 | +0.021 | [-0.072, +0.117] | 0.137 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.175 | [+0.067, +0.300] | 0.175 | rerank higher |
| rerank minus bm25 | MRR@10 | +0.299 | [+0.150, +0.454] | 0.222 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.268 | [+0.135, +0.410] | 0.201 | rerank higher |
| rerank minus dense | Recall@10 | +0.008 | [-0.058, +0.092] | 0.109 | not distinguishable |
| rerank minus dense | MRR@10 | +0.241 | [+0.128, +0.363] | 0.170 | rerank higher |
| rerank minus dense | nDCG@10 | +0.176 | [+0.082, +0.274] | 0.138 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.092 | [+0.008, +0.200] | 0.136 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.164 | [+0.064, +0.283] | 0.158 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.155 | [+0.067, +0.263] | 0.144 | rerank higher |
| ablation/bm25_lab minus bm25 | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| ablation/bm25_lab minus bm25 | MRR@10 | -0.017 | [-0.050, +0.000] | 0.047 | not distinguishable |
| ablation/bm25_lab minus bm25 | nDCG@10 | -0.012 | [-0.037, +0.000] | 0.034 | not distinguishable |
| ablation/bm25_lab minus dense | Recall@10 | -0.167 | [-0.317, -0.017] | 0.216 | dense higher |
| ablation/bm25_lab minus dense | MRR@10 | -0.075 | [-0.219, +0.073] | 0.215 | not distinguishable |
| ablation/bm25_lab minus dense | nDCG@10 | -0.104 | [-0.240, +0.035] | 0.199 | not distinguishable |
| ablation/bm25_lab minus hybrid | Recall@10 | -0.083 | [-0.150, -0.017] | 0.097 | hybrid higher |
| ablation/bm25_lab minus hybrid | MRR@10 | -0.151 | [-0.276, -0.036] | 0.175 | hybrid higher |
| ablation/bm25_lab minus hybrid | nDCG@10 | -0.125 | [-0.216, -0.041] | 0.128 | hybrid higher |
| ablation/bm25_lab minus rerank | Recall@10 | -0.175 | [-0.300, -0.067] | 0.175 | rerank higher |
| ablation/bm25_lab minus rerank | MRR@10 | -0.315 | [-0.468, -0.167] | 0.221 | rerank higher |
| ablation/bm25_lab minus rerank | nDCG@10 | -0.281 | [-0.420, -0.150] | 0.199 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time. Two systems that score the same on every query have no interval to speak of, so their MDD is shown as -.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?


On my OSHA corpus rerank did the best again with MRR@10 of 0.933. Hybrid got 0.769, dense got 0.693, and BM25 0.635. Rerank was higher than each other system, and all three MRR difference intervals excluded zero. Hybrid was also higher than BM25 by 0.135, with an interval of (0.022, 0.258). Dense versus BM25 and hybrid versus dense were not distinguishable. So my prediction that rerank would win was right, but my prediction that dense would be worst was wrong. BM25 was the lowest overall.

The hand and Claude question groups weren't exactly the same. BM25 got 0.463 MRR on hand queries and 0.721 on Claude queries, but that direct interval includes zero. A clearer difference is BM25's advantage over dense: it was 0.382 higher on the Claude group relative to the hand group, with interval (0.114, 0.671). The Claude queries shared more words with the correct documents too (0.76 versus 0.58). That shows how the questions are written matters a lot. There are only 10 hand queries so I wouldn't generalize too much from them.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/bm25_lab minus bm25 | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| ablation/bm25_lab minus bm25 | MRR@10 | -0.017 | [-0.050, +0.000] | 0.047 | not distinguishable |
| ablation/bm25_lab minus bm25 | nDCG@10 | -0.012 | [-0.037, +0.000] | 0.034 | not distinguishable |
| ablation/bm25_lab minus dense | Recall@10 | -0.167 | [-0.317, -0.017] | 0.216 | dense higher |
| ablation/bm25_lab minus dense | MRR@10 | -0.075 | [-0.219, +0.073] | 0.215 | not distinguishable |
| ablation/bm25_lab minus dense | nDCG@10 | -0.104 | [-0.240, +0.035] | 0.199 | not distinguishable |
| ablation/bm25_lab minus hybrid | Recall@10 | -0.083 | [-0.150, -0.017] | 0.097 | hybrid higher |
| ablation/bm25_lab minus hybrid | MRR@10 | -0.151 | [-0.276, -0.036] | 0.175 | hybrid higher |
| ablation/bm25_lab minus hybrid | nDCG@10 | -0.125 | [-0.216, -0.041] | 0.128 | hybrid higher |
| ablation/bm25_lab minus rerank | Recall@10 | -0.175 | [-0.300, -0.067] | 0.175 | rerank higher |
| ablation/bm25_lab minus rerank | MRR@10 | -0.315 | [-0.468, -0.167] | 0.221 | rerank higher |
| ablation/bm25_lab minus rerank | nDCG@10 | -0.281 | [-0.420, -0.150] | 0.199 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time. Two systems that score the same on every query have no interval to speak of, so their MDD is shown as -.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/bm25_lab against bm25 (BASE = "bm25" in p2/retrievers/bm25_lab.py): it helped 0 queries, hurt 1 and left 29 unchanged.

| Query | Class | Origin | bm25 RR | ablation/bm25_lab RR | Change | Effect |
| --- | --- | --- | ---: | ---: | ---: | --- |
| h03 | identifier | hand | 1.000 | 0.500 | -0.500 | hurt |

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.


I expect the lab tokenizer to perform worse on identifier questions because it splits regulation numbers apart instead of keeping them together. Since a lot of OSHA questions involve specific section numbers, I think this will make it harder to find the right documents.

I only changed the BM25 tokenizer from `codes` to `lab`. The lab version splits numbers like 1926.451 into separate pieces, while codes keeps the full section number too. My hypothesis was that this would hurt identifier questions. Overall MRR@10 went from 0.635 to 0.618, a drop of 0.017, with interval (-0.050, 0). That includes zero, and the MDD was 0.047, so the overall change wasn't distinguishable. Recall@10 stayed exactly the same.

Identifier MRR dropped from 0.950 to 0.900, while the other two classes didn't change. The new tokenizer helped zero queries, hurt one, and left 29 unchanged. For h03, the correct scaffolding section `1926.451` fell from rank 1 to rank 2 behind `1926.452`. That fits my prediction, but one changed question isn't enough to claim the tokenizer is generally worse.
---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|
| c06 | Put 1926.1409 (over 350 kV) at rank 1 | 1926.1407 at rank 2 and 1926.1408 at rank 4 | Similar section names, but the wrong voltage range | Pay more attention to the voltage range |
| c07 | Put 1926.601 (motor vehicles) at rank 1 | 1926.602 (earthmoving equipment) at rank 2 | Both mention reverse alarms, but only one covers earthmoving equipment | Match the specific equipment type better |
| c09 | Returned unrelated sections, with helicopters at rank 1 | 1926.911 (misfires), missing from the top 10 | The question said "charge fails to go off" instead of "misfire" | Add similar terms to the search and retrieve more documents |
| c11 | Found 1926.101 (hearing protection) at rank 1 but missed the noise limits | Also needed 1926.52, which was outside the top 10 | Found part of the answer but missed the actual noise limits | Retrieve more documents and include exposure limits |
| h10 | Found three relevant crane sections in ranks 1–3 but missed another | Also needed 1926.1424 (work area control) | The question was broad, and the missing section was ranked too low | Break broad questions into smaller ones or retrieve more candidates |

The biggest problem I noticed is that rerank can't fix documents it never gets to see. For c09, c11, and h10, the missing documents weren't even in hybrid's top 20, so rerank couldn't move them up. The other problems mostly came from regulations that were very similar or questions that weren't specific enough. I think improving the initial search would help more than just changing the reranker.


---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.


Rerank won on both corpora. It got MRR@10 of 0.800 on the shared mining regulations and 0.933 on my OSHA construction regulations, with intervals showing it was higher than each of the other systems in both sets. What changed was hybrid versus BM25. On the shared corpus, their difference was -0.037 and the interval included zero. On OSHA, hybrid was higher by 0.135 with interval (0.022, 0.258).

The collections are pretty different. The shared corpus has 2,484 documents with a median of 68 words each, while OSHA has 310 documents with a median of 381.5 words. The OSHA questions also share more words with their relevant documents overall, 0.70 compared with 0.53. For paraphrase questions it was 0.41 versus 0.11. That overlap is measured, and it might help explain why keyword based retrieval did better on OSHA. But I didn't run an experiment that proves overlap or document length caused the difference. With only 20 shared questions and 30 OSHA questions, I can't claim the same results would hold for every regulation or every question.
---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.


For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.


### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-hybrid.jsonl | hybrid | 12 | 12 | 2 | 63,842 | 5,391 | 75.0 | 5,320 | 449 | 6.3 |
| traces/own-own-rerank.jsonl | rerank | 30 | 30 | 0 | 622,710 | 7,197 | 136.0 | 20,757 | 240 | 4.5 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 2 | 441,831 | 5,777 | 104.0 | 22,092 | 289 | 5.2 |
| traces/shared-practice-rerank_c10.jsonl | rerank_c10 | 20 | 20 | 0 | 323,377 | 5,505 | 101.0 | 16,169 | 275 | 5.0 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 0 | 793,945 | 14,077 | 228.4 | 19,849 | 352 | 5.7 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.293 | [-0.533, -0.043] | 22,092 | 5.2 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.237 | [-0.408, -0.083] | 22,092 | 5.2 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.329 | [-0.504, -0.164] | 22,092 | 5.2 | rerank higher |
| shared practice: bm25 minus rerank_c10 | 20 | -0.165 | [-0.432, +0.117] | 16,169 | 5.0 | not distinguishable |
| shared practice: dense minus rerank_c10 | 20 | -0.110 | [-0.312, +0.106] | 16,169 | 5.0 | not distinguishable |
| shared practice: hybrid minus rerank_c10 | 20 | -0.202 | [-0.396, -0.003] | 16,169 | 5.0 | rerank_c10 higher |
| shared practice: rerank_c10 minus rerank | 20 | -0.128 | [-0.278, +0.000] | 5,923 | 0.2 | not distinguishable |
| own: bm25 minus rerank | 30 | -0.299 | [-0.454, -0.150] | 20,757 | 4.5 | rerank higher |
| own: dense minus rerank | 30 | -0.241 | [-0.363, -0.128] | 20,757 | 4.5 | rerank higher |
| own: hybrid minus rerank | 30 | -0.164 | [-0.283, -0.064] | 20,757 | 4.5 | rerank higher |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-bm25_lab.jsonl | bm25_lab | 30 | 0.02 | 0.5 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 30 | 0.02 | 0.6 |
| traces/retrieval/own-own-dense.jsonl | dense | 30 | 0.14 | 4.5 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 30 | 0.14 | 4.7 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.03 | 1.5 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.16 | 8.2 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.16 | 8.2 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.06 | 1.6 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.23 | 5.7 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 0.37 | 9.2 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Write the five things here.

I chose stretch option 3, cost and latency. I tested reranking 10 candidates instead of 20 using `rerank_c10.py`. The results are in the `stretch-cost` table. The 10-candidate version saved 26.8% of input tokens (5,923 per query), but only 0.2 seconds. MRR@10 dropped from 0.800 to 0.672, with a difference of -0.128 and interval (-0.278, 0), so it wasn't statistically distinguishable. Recall@10 also dropped from 0.733 to 0.592, and that difference was distinguishable. I'd keep 20 candidates because the accuracy loss isn't worth the small time savings. Next I'd test 15 candidates to see if I can save tokens without losing as much performance.
---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
_No repeated runs or answers files yet (598E: `p2 run ... --repeat 3` and `p2 answer ... --repeat 3`)._
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
