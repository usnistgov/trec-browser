# Runs - Health Misinformation 2022 

#### bm25 
[**`Results`**](./results.md#bm25), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.bm25.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.bm25), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/bm25.pdf) 

- :material-rename: **Name:** bm25 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `1fef723cf7718a7b10c0ec33a4bbcf28` 
- :material-text: **Run description:** Anserini/Pyserini BM25 

---
#### citius.base 
[**`Results`**](./results.md#citiusbase), [**`Participants`**](./participants.md#citius), [**`Proceedings`**](./proceedings.md#citius-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.citius.base.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.citius.base), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/citius.base.pdf) 

- :material-rename: **Name:** citius.base 
- :fontawesome-solid-user-group: **Participant:** CiTIUS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `7e50c9f7b28074f46cd1a8a2c99c76c3` 
- :material-text: **Run description:** First, a Bm25 search over the index is performed using the question field to obtain the top 1000 documents per topic. Afterwards, we reorder the top 100 based on MonoT5 reranker technology and the question field. 

---
#### citius.gpt-3 
[**`Results`**](./results.md#citiusgpt-3), [**`Participants`**](./participants.md#citius), [**`Proceedings`**](./proceedings.md#citius-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.citius.gpt-3.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.citius.gpt-3), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/citius.gpt-3.pdf) 

- :material-rename: **Name:** citius.gpt-3 
- :fontawesome-solid-user-group: **Participant:** CiTIUS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/31/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `fc9a964b1c3d8b8e906b56dfc2cd726e` 
- :material-text: **Run description:** To predict the answer we utilised the encoder model GPT-3. We used no fine-tuned and no prompt. The model was fed with the topic question + "Yes or No?" and the answer was automatically analyzed and categorized into "yes", "no" or "inconclusive". Finally, the "yes" topics were assigned score 1, the "no", score 0, and the "inconclusive" turned into "no" with 0.5 probability. 

---
#### citius.r1 
[**`Results`**](./results.md#citiusr1), [**`Participants`**](./participants.md#citius), [**`Proceedings`**](./proceedings.md#citius-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.citius.r1.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.citius.r1), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/citius.r1.pdf) 

- :material-rename: **Name:** citius.r1 
- :fontawesome-solid-user-group: **Participant:** CiTIUS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/31/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `74264095f914293ccaa39decf939ed12` 
- :material-text: **Run description:** First, a Bm25 search over the index is performed using the question field to obtain the top 1000 documents per topic. Afterwards, we reorder the top 100 based on the fusion of two signals: a MonoT5 reranker technology using the question field and a RF classifier that identifies credibility. Those signals were weighted.  

---
#### citius.r2 
[**`Results`**](./results.md#citiusr2), [**`Participants`**](./participants.md#citius), [**`Proceedings`**](./proceedings.md#citius-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.citius.r2.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.citius.r2), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/citius.r2.pdf) 

- :material-rename: **Name:** citius.r2 
- :fontawesome-solid-user-group: **Participant:** CiTIUS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/31/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `f7423aba3f448f9692e29d3a1eeb2452` 
- :material-text: **Run description:** First, a Bm25 search over the index is performed using the question field to obtain the top 1000 documents per topic. Afterwards, we reorder the top 100 based on the fusion of three signals: a MonoT5 reranker technology using the question field, a RF classifier that identifies credibility and a BERT model that discerns readable from non-readable excerpts. Those signals were weighted. 

---
#### citius.r3 
[**`Results`**](./results.md#citiusr3), [**`Participants`**](./participants.md#citius), [**`Proceedings`**](./proceedings.md#citius-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.citius.r3.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.citius.r3), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/citius.r3.pdf) 

- :material-rename: **Name:** citius.r3 
- :fontawesome-solid-user-group: **Participant:** CiTIUS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/31/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `729129ffd7979b3467e1370c0e86e5f6` 
- :material-text: **Run description:** First, a Bm25 search over the index is performed using the question field to obtain the top 1000 documents per topic. Afterwards, we reorder the top 100 based on MonoT5 reranker technology and the "predicted" correct sentence. To do so, we utilised a GPT-3 encoder model (see run citius.gpt-3 from Answer Prediction) to estimate the answer and for those identified as inconclusive we mantain the default Bm25 ordering.  

---
#### citius.r4 
[**`Results`**](./results.md#citiusr4), [**`Participants`**](./participants.md#citius), [**`Proceedings`**](./proceedings.md#citius-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.citius.r4.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.citius.r4), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/citius.r4.pdf) 

- :material-rename: **Name:** citius.r4 
- :fontawesome-solid-user-group: **Participant:** CiTIUS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/31/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `6ce645c221e3f6b1f980a045b6d168de` 
- :material-text: **Run description:** First, a Bm25 search over the index is performed using the question field to obtain the top 1000 documents per topic. Afterwards, we reorder the top 100 based on MonoT5 reranker technology and the "predicted" correct sentence. To do so, we utilised a GPT-3 encoder model (see run citius.gpt-3 from Answer Prediction) to estimate the answer and for those identified as inconclusive we kept the MonoT5 score based on the question field. 

---
#### citius.r5 
[**`Results`**](./results.md#citiusr5), [**`Participants`**](./participants.md#citius), [**`Proceedings`**](./proceedings.md#citius-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.citius.r5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.citius.r5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/citius.r5.pdf) 

- :material-rename: **Name:** citius.r5 
- :fontawesome-solid-user-group: **Participant:** CiTIUS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/31/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `4c5cbfc51796d9d67e4cefef5cee3377` 
- :material-text: **Run description:** First, a Bm25 search over the index is performed using the question field to obtain the top 1000 documents per topic. Afterwards, we reorder the top 100 based on MonoT5 reranker technology and the "predicted" correct sentence. To do so, we launched the query against a SE API and scraped the top 1 result. Finally, we extracted the most on topic passage and compared it with both variants (correct and incorrect) and we kept the one with highest probability. 

---
#### citius.r6 
[**`Results`**](./results.md#citiusr6), [**`Participants`**](./participants.md#citius), [**`Proceedings`**](./proceedings.md#citius-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.citius.r6.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.citius.r6), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/citius.r6.pdf) 

- :material-rename: **Name:** citius.r6 
- :fontawesome-solid-user-group: **Participant:** CiTIUS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/31/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `c3f565a34c9f13496b04663c1a7f0617` 
- :material-text: **Run description:** First, a Bm25 search over the index is performed using the question field to obtain the top 1000 documents per topic. Afterwards, we reorder the top 100 based on MonoT5 reranker technology and the "predicted" correct sentence. To do so, we combined our GPT-3 estimator and our SE one. We simply apply an "and" operation. The inconclusive ones were kept like that, and they were reordered based on the MonoT5 score of the unmodified question. 

---
#### citius.se 
[**`Results`**](./results.md#citiusse), [**`Participants`**](./participants.md#citius), [**`Proceedings`**](./proceedings.md#citius-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.citius.se.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.citius.se), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/citius.se.pdf) 

- :material-rename: **Name:** citius.se 
- :fontawesome-solid-user-group: **Participant:** CiTIUS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/31/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `e336250c9d62fdb0f3a6a94934359381` 
- :material-text: **Run description:** To predict the answer, we launched the question into a SE API and we scraped the top 1 result. Then, using passage reranking technology, the most on topic passage was selected. Finally, the positive and negative versions of the sentences were compared against the passage and the highest probability determined the answer. 

---
#### citius.se_gpt 
[**`Results`**](./results.md#citiusse_gpt), [**`Participants`**](./participants.md#citius), [**`Proceedings`**](./proceedings.md#citius-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.citius.se_gpt.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.citius.se_gpt), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/citius.se_gpt.pdf) 

- :material-rename: **Name:** citius.se_gpt 
- :fontawesome-solid-user-group: **Participant:** CiTIUS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/31/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `b4eaaef007441b25ddcc3ba3d9c98036` 
- :material-text: **Run description:** To predict the answer, we applied an "and" operation to the output of our runs with GPT-3 and SE. 

---
#### gpt3a 
[**`Results`**](./results.md#gpt3a), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.gpt3a.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.gpt3a), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/gpt3a.pdf) 

- :material-rename: **Name:** gpt3a 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `d8b5a8d34c85d994ab9b30f108c2f7e3` 
- :material-text: **Run description:** GPT3 prompted with 21 topics to generate label predictions 

---
#### gpt3a_fc 
[**`Results`**](./results.md#gpt3a_fc), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.gpt3a_fc.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.gpt3a_fc), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/gpt3a_fc.pdf) 

- :material-rename: **Name:** gpt3a_fc 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `851f0da9750f60da09b43d8c28d6846f` 
- :material-text: **Run description:** Rounds gpt3a to 1.0 or 0.0. 

---
#### gpt3a_neg 
[**`Results`**](./results.md#gpt3a_neg), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.gpt3a_neg.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.gpt3a_neg), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/gpt3a_neg.pdf) 

- :material-rename: **Name:** gpt3a_neg 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `5061028559b23d282824887135134e00` 
- :material-text: **Run description:** gpt3a but invert the predictions 

---
#### gpt3b 
[**`Results`**](./results.md#gpt3b), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.gpt3b.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.gpt3b), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/gpt3b.pdf) 

- :material-rename: **Name:** gpt3b 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `0da2ab7bf04b7b2a3baad0df578e51a9` 
- :material-text: **Run description:** gpt3a without normalized scoring scheme 

---
#### gpt3b_neg 
[**`Results`**](./results.md#gpt3b_neg), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.gpt3b_neg.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.gpt3b_neg), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/gpt3b_neg.pdf) 

- :material-rename: **Name:** gpt3b_neg 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `c88a08173273391037baa53538107bba` 
- :material-text: **Run description:** gpt3b but invert the predictions 

---
#### hm22.mdt5 
[**`Results`**](./results.md#hm22mdt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22.mdt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22.mdt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22.mdt5.pdf) 

- :material-rename: **Name:** hm22.mdt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `5ad409a1e822bb954c53cf2566348dec` 
- :material-text: **Run description:** mdt5 - mdt5 on original 

---
#### hm22.mt5 
[**`Results`**](./results.md#hm22mt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22.mt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22.mt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22.mt5.pdf) 

- :material-rename: **Name:** hm22.mt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `ba5f438e0fd0d3e6cf8413ecc1572e85` 
- :material-text: **Run description:** mt5 - mt5 on original 

---
#### hm22.vera 
[**`Results`**](./results.md#hm22vera), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22.vera.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22.vera), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22.vera.pdf) 

- :material-rename: **Name:** hm22.vera 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `bbb5d2ec47a429cd390f3579e03294a0` 
- :material-text: **Run description:** hm22 - label prediction by GPT3 (prompted with 2021 topics + stances) vera - vera without linear combinations 

---
#### hm22.vera_mdt5 
[**`Results`**](./results.md#hm22vera_mdt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22.vera_mdt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22.vera_mdt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22.vera_mdt5.pdf) 

- :material-rename: **Name:** hm22.vera_mdt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `97d93032045771d82d2d749cbf1cfc65` 
- :material-text: **Run description:** hm22 - label prediction by GPT3 (prompted with 2021 topics + stances) vera_mdt5 - mdt5 on original followed by vera(0.95, duo1) 

---
#### hm22.vera_mt5 
[**`Results`**](./results.md#hm22vera_mt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22.vera_mt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22.vera_mt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22.vera_mt5.pdf) 

- :material-rename: **Name:** hm22.vera_mt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `2697b0f7b27b8499c0fe35498d47b945` 
- :material-text: **Run description:** hm22 - label prediction by GPT3 (prompted with 2021 topics + stances) vera_mt5 - mt5 on original followed by vera(0.95, mono) 

---
#### hm22_ref.mdt5 
[**`Results`**](./results.md#hm22_refmdt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref.mdt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref.mdt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref.mdt5.pdf) 

- :material-rename: **Name:** hm22_ref.mdt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `75e283af8c8eefed518dfdb93f9a38bf` 
- :material-text: **Run description:** hm22_ref - label prediction by GPT3 (prompted with 2021 topics + stances) followed by reformulation by GPT3 mdt5 - mdt5 

---
#### hm22_ref.mt5 
[**`Results`**](./results.md#hm22_refmt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref.mt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref.mt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref.mt5.pdf) 

- :material-rename: **Name:** hm22_ref.mt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `d94474cd58112fcdcae96155e347c7fe` 
- :material-text: **Run description:** hm22_ref - label prediction by GPT3 (prompted with 2021 topics + stances) followed by reformulation by GPT3 mt5 - mt5 

---
#### hm22_ref.vera 
[**`Results`**](./results.md#hm22_refvera), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref.vera.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref.vera), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref.vera.pdf) 

- :material-rename: **Name:** hm22_ref.vera 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `aada542cf73adc2938f351d13b3eae1a` 
- :material-text: **Run description:** hm22_ref - label prediction by GPT3 (prompted with 2021 topics + stances) and reformulation by GPT3 vera - vera without linear combinations 

---
#### hm22_ref.vera_mdt5 
[**`Results`**](./results.md#hm22_refvera_mdt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref.vera_mdt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref.vera_mdt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref.vera_mdt5.pdf) 

- :material-rename: **Name:** hm22_ref.vera_mdt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `a2313f2fceb7d5c3bfb65a819365a1cf` 
- :material-text: **Run description:** hm22_ref - label prediction by GPT3 (prompted with 2021 topics + stances) followed by reformulation by GPT3 vera_mdt5 - mdt5 on ref followed by vera(0.95, duo1) 

---
#### hm22_ref.vera_mt5 
[**`Results`**](./results.md#hm22_refvera_mt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref.vera_mt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref.vera_mt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref.vera_mt5.pdf) 

- :material-rename: **Name:** hm22_ref.vera_mt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `8423f6d1dc925a34f12c93c1c76b3294` 
- :material-text: **Run description:** hm22_ref - label prediction by GPT3 (prompted with 2021 topics + stances) followed by reformulation by GPT3 vera_mdt5 - mdt5 on ref followed by vera(0.95, mono)  

---
#### hm22_ref_comb.mdt5 
[**`Results`**](./results.md#hm22_ref_combmdt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref_comb.mdt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref_comb.mdt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref_comb.mdt5.pdf) 

- :material-rename: **Name:** hm22_ref_comb.mdt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `5a33c1fc4d57d77fa0b76ce77fc4e3bc` 
- :material-text: **Run description:** hm22_ref_comb - combination of label prediction by GPT3 (prompted with 2021 topics + stances) and answer prediction run vera, followed by reformulation by GPT3 mdt5 - mdt5 

---
#### hm22_ref_comb.mt5 
[**`Results`**](./results.md#hm22_ref_combmt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref_comb.mt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref_comb.mt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref_comb.mt5.pdf) 

- :material-rename: **Name:** hm22_ref_comb.mt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `73ce4aa576bb1511f7ee87070520cb16` 
- :material-text: **Run description:** hm22_ref_comb - combination of label prediction by GPT3 (prompted with 2021 topics + stances) and answer prediction run vera, followed by reformulation by GPT3 mt5 - mt5 

---
#### hm22_ref_comb.vera_mdt5 
[**`Results`**](./results.md#hm22_ref_combvera_mdt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref_comb.vera_mdt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref_comb.vera_mdt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref_comb.vera_mdt5.pdf) 

- :material-rename: **Name:** hm22_ref_comb.vera_mdt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `1e2913d8a3af1fad8194c3bd169b2973` 
- :material-text: **Run description:** hm22_ref_comb - combination of label prediction by GPT3 (prompted with 2021 topics + stances) and answer prediction run vera, followed by reformulation by GPT3 vera_mdt5 - mdt5 on ref followed by vera(0.95, duo1) 

---
#### hm22_ref_comb.vera_mt5 
[**`Results`**](./results.md#hm22_ref_combvera_mt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref_comb.vera_mt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref_comb.vera_mt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref_comb.vera_mt5.pdf) 

- :material-rename: **Name:** hm22_ref_comb.vera_mt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `f2fd6f3bdfd63dba41326f8a5f02e203` 
- :material-text: **Run description:** hm22_ref_comb - combination of label prediction by GPT3 (prompted with 2021 topics + stances) and answer prediction run vera, followed by reformulation by GPT3 vera_mt5 - mt5 on ref followed by vera(0.95, mono) 

---
#### hm22_ref_neg.mdt5 
[**`Results`**](./results.md#hm22_ref_negmdt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref_neg.mdt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref_neg.mdt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref_neg.mdt5.pdf) 

- :material-rename: **Name:** hm22_ref_neg.mdt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `492a95aaeb770afd391d4bdce102b32c` 
- :material-text: **Run description:** hm22 - label prediction by GPT3 (prompted with 2021 topics + stances) is inverted mdt5 - mdt5 on inverted reformulations 

---
#### hm22_ref_neg.mt5 
[**`Results`**](./results.md#hm22_ref_negmt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref_neg.mt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref_neg.mt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref_neg.mt5.pdf) 

- :material-rename: **Name:** hm22_ref_neg.mt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `d34df0734db8a6ee1d7a831db5380015` 
- :material-text: **Run description:** hm22 - label prediction by GPT3 (prompted with 2021 topics + stances) is inverted mt5 - mt5 on inverted reformulations 

---
#### hm22_ref_neg.vera 
[**`Results`**](./results.md#hm22_ref_negvera), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref_neg.vera.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref_neg.vera), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref_neg.vera.pdf) 

- :material-rename: **Name:** hm22_ref_neg.vera 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `b15d84c6534fb3697b5f3d74805ad124` 
- :material-text: **Run description:** hm22 - label prediction by GPT3 (prompted with 2021 topics + stances) is inverted vera - vera without linear combinations 

---
#### hm22_ref_neg.vera_mdt5 
[**`Results`**](./results.md#hm22_ref_negvera_mdt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref_neg.vera_mdt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref_neg.vera_mdt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref_neg.vera_mdt5.pdf) 

- :material-rename: **Name:** hm22_ref_neg.vera_mdt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `bcf868497d6e9be8837ea09d0ea753d9` 
- :material-text: **Run description:** hm22 - label prediction by GPT3 (prompted with 2021 topics + stances) is inverted  vera_mdt5 - mdt5 on inverted reformulations followed by vera(0.95, duo1)  

---
#### hm22_ref_neg.vera_mt5 
[**`Results`**](./results.md#hm22_ref_negvera_mt5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.hm22_ref_neg.vera_mt5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.hm22_ref_neg.vera_mt5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/hm22_ref_neg.vera_mt5.pdf) 

- :material-rename: **Name:** hm22_ref_neg.vera_mt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `b39a09cdf20f889cf0a004c1f85a62fc` 
- :material-text: **Run description:** hm22 - label prediction by GPT3 (prompted with 2021 topics + stances) is inverted  vera_mdt5 - mt5 on inverted reformulations followed by vera(0.95, mono)  

---
#### vera 
[**`Results`**](./results.md#vera), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.vera.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.vera), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/vera.pdf) 

- :material-rename: **Name:** vera 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `4b491b70a8eaa83d5932daa38eebdb4b` 
- :material-text: **Run description:** Vera scores from top-50 Med-MonoT5 results 

---
#### vera_abs 
[**`Results`**](./results.md#vera_abs), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.vera_abs.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.vera_abs), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/vera_abs.pdf) 

- :material-rename: **Name:** vera_abs 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `6051cf5efb1533a86f14797cebccc0fa` 
- :material-text: **Run description:** Rounds vera to 1.0 or 0.0.  

---
#### vera_gpt3 
[**`Results`**](./results.md#vera_gpt3), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.vera_gpt3.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.vera_gpt3), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/vera_gpt3.pdf) 

- :material-rename: **Name:** vera_gpt3 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `7a790fe6029cd2974d5e05081b9bae0c` 
- :material-text: **Run description:** Mean of runs vera and gpt3 

---
#### vera_gpt3_abs 
[**`Results`**](./results.md#vera_gpt3_abs), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.vera_gpt3_abs.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.vera_gpt3_abs), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/vera_gpt3_abs.pdf) 

- :material-rename: **Name:** vera_gpt3_abs 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/28/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `1a12140d60057d438661fbdd7138d703` 
- :material-text: **Run description:** Rounds vera_gpt3 to 1.0 or 0.0. 

---
#### WatS-AP-Baseline 
[**`Results`**](./results.md#wats-ap-baseline), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-AP-Baseline.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-AP-Baseline), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-AP-Baseline.pdf) 

- :material-rename: **Name:** WatS-AP-Baseline 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `e7f27ae8ef2473c1766809a6f1d6f7f3` 
- :material-text: **Run description:** Logistic Regression-based Trust Model 

---
#### WatS-AP-Baseline-L1 
[**`Results`**](./results.md#wats-ap-baseline-l1), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-AP-Baseline-L1.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-AP-Baseline-L1), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-AP-Baseline-L1.pdf) 

- :material-rename: **Name:** WatS-AP-Baseline-L1 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `4449d20ab133385cf86539a94e8ebc14` 
- :material-text: **Run description:** Logistic Regression-based Trust Model with L1 regularization 

---
#### WatS-AP-Manual 
[**`Results`**](./results.md#wats-ap-manual), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-AP-Manual.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-AP-Manual), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-AP-Manual.pdf) 

- :material-rename: **Name:** WatS-AP-Manual 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/29/2022 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `4a0b1f9bbaf8983de6a2db953b09b934` 
- :material-text: **Run description:** This a manual run where the answers to topics were judged with google search results.   

---
#### WatS-AP-MT5 
[**`Results`**](./results.md#wats-ap-mt5), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-AP-MT5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-AP-MT5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-AP-MT5.pdf) 

- :material-rename: **Name:** WatS-AP-MT5 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `2c9dd2e73354b7073f3708b5774ec1d0` 
- :material-text: **Run description:** Logistic Regression-based Trust Model with mt5 for reranking 

---
#### WatS-AP-MT5-L1 
[**`Results`**](./results.md#wats-ap-mt5-l1), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-AP-MT5-L1.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-AP-MT5-L1), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-AP-MT5-L1.pdf) 

- :material-rename: **Name:** WatS-AP-MT5-L1 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `2469fd5a0c4d6a847b94e05c1de27fcb` 
- :material-text: **Run description:** Logistic Regression-based Trust Model with mt5 for reranking and L1 regularization 

---
#### WatS-BB75-MT5-TA 
[**`Results`**](./results.md#wats-bb75-mt5-ta), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-BB75-MT5-TA.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-BB75-MT5-TA), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-BB75-MT5-TA.pdf) 

- :material-rename: **Name:** WatS-BB75-MT5-TA 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `c6b6a174880f1ef1d37d611252146290` 
- :material-text: **Run description:** "Initial Retrieval: Top 1k BM25 Rerank: MT5 Passage extraction: MeshQA QA: BERT , PubMedQA (+ tuning on 2019 2021 qrels)  Answer prediction: mean_topk (bert(passage plus host plus hon))" 

---
#### WatS-Bigbird2_75-MT5 
[**`Results`**](./results.md#wats-bigbird2_75-mt5), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-Bigbird2_75-MT5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-Bigbird2_75-MT5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-Bigbird2_75-MT5.pdf) 

- :material-rename: **Name:** WatS-Bigbird2_75-MT5 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `f5ccf579ff71492183a633ae7fa32f1a` 
- :material-text: **Run description:** "Initial Retrieval: Top 1k BM25 Passage Extraction: Bigbird ss=0.75 Rerank: MT5" 

---
#### WatS-Bigbird2_75-MT5-TA1 
[**`Results`**](./results.md#wats-bigbird2_75-mt5-ta1), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-Bigbird2_75-MT5-TA1.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-Bigbird2_75-MT5-TA1), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-Bigbird2_75-MT5-TA1.pdf) 

- :material-rename: **Name:** WatS-Bigbird2_75-MT5-TA1 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `46e1b9db6370f699bc31c2afe09cd13f` 
- :material-text: **Run description:** Same as TA2 but with no fine tuning on previous years topics 

---
#### WatS-Bigbird2_75-MT5-TA2 
[**`Results`**](./results.md#wats-bigbird2_75-mt5-ta2), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-Bigbird2_75-MT5-TA2.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-Bigbird2_75-MT5-TA2), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-Bigbird2_75-MT5-TA2.pdf) 

- :material-rename: **Name:** WatS-Bigbird2_75-MT5-TA2 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `fb248f61863db9fd79333d803a88583c` 
- :material-text: **Run description:** "Initial Retrieval: Top 1k BM25 Rerank: MT5 Passage extraction: MeshQA QA: BERT , PubMedQA (+ tuning on 2019 2021 qrels)  Answer prediction: mean_topk (bert(passage plus host plus hon)) Second Rerank: MT5 * agreement alpha=.2"  

---
#### WatS-BM25-Query 
[**`Results`**](./results.md#wats-bm25-query), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-BM25-Query.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-BM25-Query), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-BM25-Query.pdf) 

- :material-rename: **Name:** WatS-BM25-Query 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `9d8709d0421e2a7b72fc63a3ccdd5b3d` 
- :material-text: **Run description:** BM25 baseline (k1=0.9, b=0.4) using the query field 

---
#### WatS-BM25-Question 
[**`Results`**](./results.md#wats-bm25-question), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-BM25-Question.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-BM25-Question), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-BM25-Question.pdf) 

- :material-rename: **Name:** WatS-BM25-Question 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `fa40dd2a07944eed25884f1248e22871` 
- :material-text: **Run description:** BM25 baseline (k1=0.9, b=0.4) using the query field 

---
#### WatS-Manual 
[**`Results`**](./results.md#wats-manual), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-Manual.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-Manual), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-Manual.pdf) 

- :material-rename: **Name:** WatS-Manual 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/29/2022 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `44e16c086d862c3316c192d976de8d1a` 
- :material-text: **Run description:** This a manual run where topics were judged by their snippets which were produced with MT5. the top 1k bm25 docs for each topic were reranked with MT5 and the first very useful correct 10 documents were found and placed first. incorrect documents were placed last. 

---
#### WatS-manual-pred 
[**`Results`**](./results.md#wats-manual-pred), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-manual-pred.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-manual-pred), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-manual-pred.pdf) 

- :material-rename: **Name:** WatS-manual-pred 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `d55cde64c2cce1cc53a1be29e7eb72f3` 
- :material-text: **Run description:** Paste question into google, mean 28s to determine answer 

---
#### WatS-MT5-MT5 
[**`Results`**](./results.md#wats-mt5-mt5), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-MT5-MT5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-MT5-MT5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-MT5-MT5.pdf) 

- :material-rename: **Name:** WatS-MT5-MT5 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `8422bbb74041fb891fdf6bd921ffce12` 
- :material-text: **Run description:** "Initial Retrieval: Top 1k BM25 Passage Extraction: MT5 Rerank: MT5" 

---
#### WatS-Trust 
[**`Results`**](./results.md#wats-trust), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-Trust.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-Trust), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-Trust.pdf) 

- :material-rename: **Name:** WatS-Trust 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `1d1b4e992658f4dd052342c5490b668b` 
- :material-text: **Run description:** Soft reranking BM25 using the predicted answers from WatS-AP-Baseline 

---
#### WatS-Trust-L1 
[**`Results`**](./results.md#wats-trust-l1), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-Trust-L1.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-Trust-L1), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-Trust-L1.pdf) 

- :material-rename: **Name:** WatS-Trust-L1 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `cb3eec9594d18527d82c513428e8b37a` 
- :material-text: **Run description:** Soft reranking BM25 using the predicted answer from WatS-AP-Baseline-L1 

---
#### WatS-Trust-MT5 
[**`Results`**](./results.md#wats-trust-mt5), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-Trust-MT5.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-Trust-MT5), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-Trust-MT5.pdf) 

- :material-rename: **Name:** WatS-Trust-MT5 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `eaa17132850030736ac19e36f75e4f58` 
- :material-text: **Run description:** Soft reranking MT5 using the predicted answer from WatS-AP-MT5 

---
#### WatS-Trust-MT5-L1 
[**`Results`**](./results.md#wats-trust-mt5-l1), [**`Participants`**](./participants.md#uwaterloomds), [**`Proceedings`**](./proceedings.md#uwaterloomds-at-the-trec-2022-health-misinformation-track), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.WatS-Trust-MT5-L1.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.WatS-Trust-MT5-L1), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/WatS-Trust-MT5-L1.pdf) 

- :material-rename: **Name:** WatS-Trust-MT5-L1 
- :fontawesome-solid-user-group: **Participant:** UWaterlooMDS 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/2/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `f26ccb8ec2b902671e09143eeede5de7` 
- :material-text: **Run description:** Soft reranking MT5 using the predicted answer from WatS-AP-MT5-L1 

---
#### webis-goo-boolq-abs 
[**`Results`**](./results.md#webis-goo-boolq-abs), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-goo-boolq-abs.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-goo-boolq-abs), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-goo-boolq-abs.pdf) 

- :material-rename: **Name:** webis-goo-boolq-abs 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `758097d69ca42b400deaf1538b3c9575` 
- :material-text: **Run description:** Retrieve up to 20 abstracts through Google Custom Search Engine using provided questions. Apply pre-trained RoBERTa-base-BoolQ model to abstracts using questions. Aggregate results. 

---
#### webis-goo-lbert-abs 
[**`Results`**](./results.md#webis-goo-lbert-abs), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-goo-lbert-abs.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-goo-lbert-abs), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-goo-lbert-abs.pdf) 

- :material-rename: **Name:** webis-goo-lbert-abs 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `651ea09b1792730297bbaa72d9b8a6d3` 
- :material-text: **Run description:** Retrieve up to 20 abstracts through Google Custom Search Engine using provided questions. Apply pre-trained BioLinkBERT-large model to abstracts using questions. Aggregate results. 

---
#### webis-goo-lbert-title-abs 
[**`Results`**](./results.md#webis-goo-lbert-title-abs), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-goo-lbert-title-abs.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-goo-lbert-title-abs), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-goo-lbert-title-abs.pdf) 

- :material-rename: **Name:** webis-goo-lbert-title-abs 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `037a9a647a99ee499ab3f0fda03e3010` 
- :material-text: **Run description:** Retrieve up to 20 abstracts along with titles through Google Custom Search Engine using provided questions. Apply pre-trained BioLinkBERT-large model to titles and abstracts using questions. Aggregate results. 

---
#### webis-longck-ax-com 
[**`Results`**](./results.md#webis-longck-ax-com), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-longck-ax-com.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-longck-ax-com), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-longck-ax-com.pdf) 

- :material-rename: **Name:** webis-longck-ax-com 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `aefaaa92b41fb358380b61e8e4904b02` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using LongChecker (fever_sci checkpoint, using abstract and title as context). Resolve answer conflicts with axiomatic re-ranking (most recently published abstract first). Aggregate abstract-wise answer score with ranking position discount. Retrieve 1000 documents from C4 using BM25 (Elasticsearch). Predict answer per document using LongChecker (fever_sci checkpoint, using abstract and title as context). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Combine retrieval score with similarity to predicted topic answer (tradeoff 0.75). 

---
#### webis-longck-ax-lin 
[**`Results`**](./results.md#webis-longck-ax-lin), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-longck-ax-lin.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-longck-ax-lin), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-longck-ax-lin.pdf) 

- :material-rename: **Name:** webis-longck-ax-lin 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `282443effae1b7623ed138a6c00786e6` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using LongChecker (fever_sci checkpoint, using abstract and title as context). Resolve answer conflicts with axiomatic re-ranking (most recently published abstract first). Aggregate abstract-wise answer score with ranking position discount. Retrieve 1000 documents from C4 using BM25 (Elasticsearch). Predict answer per document using LongChecker (fever_sci checkpoint, using abstract and title as context). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Boost retrieval score linearly based on similarity to predicted topic answer. 

---
#### webis-longck-ax-pol 
[**`Results`**](./results.md#webis-longck-ax-pol), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-longck-ax-pol.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-longck-ax-pol), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-longck-ax-pol.pdf) 

- :material-rename: **Name:** webis-longck-ax-pol 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `7781c7de503b293ebf2967e3ef947d4c` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using LongChecker (fever_sci checkpoint, using abstract and title as context). Resolve answer conflicts with axiomatic re-ranking (most recently published abstract first). Aggregate abstract-wise answer score with ranking position discount. Retrieve 1000 documents from C4 using BM25 (Elasticsearch). Predict answer per document using LongChecker (fever_sci checkpoint, using abstract and title as context). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Boost retrieval score polynomially (x^2) based on similarity to predicted topic answer. 

---
#### webis-longck-dis 
[**`Results`**](./results.md#webis-longck-dis), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-longck-dis.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-longck-dis), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-longck-dis.pdf) 

- :material-rename: **Name:** webis-longck-dis 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `f26f35390a9d9ee3ffb25e0a4299bb8b` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using LongChecker (fever_sci checkpoint, using abstract and title as context). Aggregate abstract-wise answer score with ranking position discount. 

---
#### webis-longck-uniqa-ax-com 
[**`Results`**](./results.md#webis-longck-uniqa-ax-com), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-longck-uniqa-ax-com.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-longck-uniqa-ax-com), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-longck-uniqa-ax-com.pdf) 

- :material-rename: **Name:** webis-longck-uniqa-ax-com 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `7cf56c247b69190c10388ce59f636ca8` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using LongChecker (fever_sci checkpoint, using abstract and title as context) and UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Resolve answer conflicts with axiomatic re-ranking (most recently published abstract first). Aggregate abstract-wise answer score with ranking position discount. Retrieve 1000 documents from C4 using BM25 (Elasticsearch). Predict answer per document using LongChecker (fever_sci checkpoint, using abstract and title as context) and UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Combine retrieval score with similarity to predicted topic answer (tradeoff 0.75). 

---
#### webis-longck-uniqa-ax-dis 
[**`Results`**](./results.md#webis-longck-uniqa-ax-dis), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-longck-uniqa-ax-dis.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-longck-uniqa-ax-dis), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-longck-uniqa-ax-dis.pdf) 

- :material-rename: **Name:** webis-longck-uniqa-ax-dis 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `cc701bf1f6596ae28655e2c082d145c0` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using LongChecker (fever_sci checkpoint, using abstract and title as context) and UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Resolve answer conflicts with axiomatic re-ranking (most recently published abstract first). Aggregate abstract-wise answer score with ranking position discount. 

---
#### webis-longck-uniqa-ax-lin 
[**`Results`**](./results.md#webis-longck-uniqa-ax-lin), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-longck-uniqa-ax-lin.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-longck-uniqa-ax-lin), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-longck-uniqa-ax-lin.pdf) 

- :material-rename: **Name:** webis-longck-uniqa-ax-lin 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `88ee57623c25b308a4c914905d98843c` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using LongChecker (fever_sci checkpoint, using abstract and title as context) and UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Resolve answer conflicts with axiomatic re-ranking (most recently published abstract first). Aggregate abstract-wise answer score with ranking position discount. Retrieve 1000 documents from C4 using BM25 (Elasticsearch). Predict answer per document using LongChecker (fever_sci checkpoint, using abstract and title as context) and UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Boost retrieval score linearly based on similarity to predicted topic answer. 

---
#### webis-longck-uniqa-ax-pol 
[**`Results`**](./results.md#webis-longck-uniqa-ax-pol), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-longck-uniqa-ax-pol.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-longck-uniqa-ax-pol), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-longck-uniqa-ax-pol.pdf) 

- :material-rename: **Name:** webis-longck-uniqa-ax-pol 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `1b65c66bdfd733e005e3034176185a79` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using LongChecker (fever_sci checkpoint, using abstract and title as context) and UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Resolve answer conflicts with axiomatic re-ranking (most recently published abstract first). Aggregate abstract-wise answer score with ranking position discount. Retrieve 1000 documents from C4 using BM25 (Elasticsearch). Predict answer per document using LongChecker (fever_sci checkpoint, using abstract and title as context) and UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Boost retrieval score polynomially (x^2) based on similarity to predicted topic answer. 

---
#### webis-longck-uniqa-dis 
[**`Results`**](./results.md#webis-longck-uniqa-dis), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-longck-uniqa-dis.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-longck-uniqa-dis), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-longck-uniqa-dis.pdf) 

- :material-rename: **Name:** webis-longck-uniqa-dis 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `317c29d464cbd2a6590e166bd61cd1b9` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using LongChecker (fever_sci checkpoint, using abstract and title as context) and UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Aggregate abstract-wise answer score with ranking position discount. 

---
#### webis-longck-uniqa-pol 
[**`Results`**](./results.md#webis-longck-uniqa-pol), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-longck-uniqa-pol.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-longck-uniqa-pol), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-longck-uniqa-pol.pdf) 

- :material-rename: **Name:** webis-longck-uniqa-pol 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `05e81f442166286aed6f5eea889bccc6` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using LongChecker (fever_sci checkpoint, using abstract and title as context) and UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Aggregate abstract-wise answer score with ranking position discount. Retrieve 1000 documents from C4 using BM25 (Elasticsearch). Predict answer per document using LongChecker (fever_sci checkpoint, using abstract and title as context) and UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Boost retrieval score polynomially (x^2) based on similarity to predicted topic answer. 

---
#### webis-nlm-boolq-abs 
[**`Results`**](./results.md#webis-nlm-boolq-abs), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-nlm-boolq-abs.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-nlm-boolq-abs), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-nlm-boolq-abs.pdf) 

- :material-rename: **Name:** webis-nlm-boolq-abs 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `7da710bb0b9b11d7167cf8c0e77935df` 
- :material-text: **Run description:** Retrieve up to 20 abstracts through PubMed search API using provided keyword queries. Reformulate queries for which only 0 or 1 documents are retrieved. Apply pre-trained RoBERTa-base-BoolQ model to abstracts using keyword queries. Aggregate results. 

---
#### webis-nlm-lbert-abs 
[**`Results`**](./results.md#webis-nlm-lbert-abs), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-nlm-lbert-abs.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-nlm-lbert-abs), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-nlm-lbert-abs.pdf) 

- :material-rename: **Name:** webis-nlm-lbert-abs 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `da1a5842a2ff933519664365f7c03e95` 
- :material-text: **Run description:** Retrieve up to 20 abstracts through PubMed search API using provided keyword queries. Reformulate queries for which only 0 or 1 documents are retrieved. Apply pre-trained BioLinkBERT-large model to abstracts using keyword queries. Aggregate results. 

---
#### webis-uniqa-ax-com 
[**`Results`**](./results.md#webis-uniqa-ax-com), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-uniqa-ax-com.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-uniqa-ax-com), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-uniqa-ax-com.pdf) 

- :material-rename: **Name:** webis-uniqa-ax-com 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `ff7ac49642c2c9d283f70fb3a4dbb66c` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Resolve answer conflicts with axiomatic re-ranking (most recently published abstract first). Aggregate abstract-wise answer score with ranking position discount. Retrieve 1000 documents from C4 using BM25 (Elasticsearch). Predict answer per document using UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Combine retrieval score with similarity to predicted topic answer (tradeoff 0.75). 

---
#### webis-uniqa-ax-lin 
[**`Results`**](./results.md#webis-uniqa-ax-lin), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-uniqa-ax-lin.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-uniqa-ax-lin), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-uniqa-ax-lin.pdf) 

- :material-rename: **Name:** webis-uniqa-ax-lin 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `1dac5bdfe7f88109b9999a1897081785` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Resolve answer conflicts with axiomatic re-ranking (most recently published abstract first). Aggregate abstract-wise answer score with ranking position discount. Retrieve 1000 documents from C4 using BM25 (Elasticsearch). Predict answer per document using UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Boost retrieval score linearly based on similarity to predicted topic answer. 

---
#### webis-uniqa-ax-pol 
[**`Results`**](./results.md#webis-uniqa-ax-pol), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-uniqa-ax-pol.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-uniqa-ax-pol), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-uniqa-ax-pol.pdf) 

- :material-rename: **Name:** webis-uniqa-ax-pol 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `f4a92799bab23a747e3460169e135683` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Average answer score of both predictors. Resolve answer conflicts with axiomatic re-ranking (most recently published abstract first). Aggregate abstract-wise answer score with ranking position discount. Retrieve 1000 documents from C4 using BM25 (Elasticsearch). Predict answer per document using UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Boost retrieval score polynomially (x^2) based on similarity to predicted topic answer. 

---
#### webis-uniqa-dis 
[**`Results`**](./results.md#webis-uniqa-dis), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-uniqa-dis.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-uniqa-dis), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-uniqa-dis.pdf) 

- :material-rename: **Name:** webis-uniqa-dis 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `c853271e838783c5dd6c3772998396ef` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using UnifiedQA (allenai/unifiedqa-t5-large, using abstract as context). Aggregate abstract-wise answer score with ranking position discount. 

---
#### webis-verasent-dis 
[**`Results`**](./results.md#webis-verasent-dis), [**`Participants`**](./participants.md#webis), [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation), [**`Input`**](https://trec.nist.gov/results/trec31/misinfo/input.webis-verasent-dis.gz), [**`Summary`**](https://trec.nist.gov/results/trec31/misinfo/summary.webis-verasent-dis), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/misinfo/webis-verasent-dis.pdf) 

- :material-rename: **Name:** webis-verasent-dis 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Health Misinformation 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/1/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** prediction 
- :material-fingerprint: **MD5:** `746e38981983a918271feedd5f31146f` 
- :material-text: **Run description:** Retrieve 1000 abstracts from PubMed using BM25 (Elasticsearch). Re-rank top-1000 with monoT5 (castorini/monot5-3b-med-msmarco) and top-50 with duoT5 (castorini/duot5-3b-med-msmarco). Predict answer per abstract using Vera (gs://castorini/vera/experiments/3B, using abstract as context, select most 'relevant' sentences). Aggregate abstract-wise answer score with ranking position discount. 

---
