# Runs - Conversational Assistance 2019 

#### bertrr_rel_1st 
[**`Results`**](./results.md#bertrr_rel_1st), [**`Participants`**](./participants.md#usi), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.bertrr_rel_1st.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.bertrr_rel_1st), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/bertrr_rel_1st.pdf) 

- :material-rename: **Name:** bertrr_rel_1st 
- :fontawesome-solid-user-group: **Participant:** USI 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `ae085804cc20b7100225212a91dabf6c` 
- :material-text: **Run description:** In this run, each question is expanded by selection of "relevant" previous questions along with the first question in the conversation. The "relevant" questions are labelled by three human assessors over training queries to train a model for predicting the relevant question(s) from the test set of questions. Passage Retrieval is performed using an open source ad-hoc search engine (Galago). Results are afterwards re-ranked using a BERT-based model. 

---
#### bertrr_rel_q 
[**`Results`**](./results.md#bertrr_rel_q), [**`Participants`**](./participants.md#usi), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.bertrr_rel_q.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.bertrr_rel_q), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/bertrr_rel_q.pdf) 

- :material-rename: **Name:** bertrr_rel_q 
- :fontawesome-solid-user-group: **Participant:** USI 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `9e4e99c55ee2c906d401423ecfcdbcd9` 
- :material-text: **Run description:** In this run, each question is expanded by selection of "relevant" previous questions. The "relevant" questions are labelled by three human assessors over training queries to train a model for predicting the relevant question(s) from the test set of questions. Passage Retrieval is performed using an open source ad-hoc search engine (Galago). Results are afterwards re-ranked using BERT. 

---
#### BM25_BERT_FC 
[**`Results`**](./results.md#bm25_bert_fc), [**`Participants`**](./participants.md#ruir), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.BM25_BERT_FC.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.BM25_BERT_FC), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/BM25_BERT_FC.pdf) 

- :material-rename: **Name:** BM25_BERT_FC 
- :fontawesome-solid-user-group: **Participant:** RUIR 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `c8e7e771142f3d7c57087972ebce4f76` 
- :material-text: **Run description:** In this run, we only used the MS MARCO collection to retrieve from. We indexed it in Anserini and retrieved 1000 articles with BM25. We did not retrieve them based on ONLY the query, but also the previous turns. We then reranked the query/passage combo's with BERT. We used a pretrained sequence classification model that was finetuned on MS MARCO.  

---
#### BM25_BERT_RANKF 
[**`Results`**](./results.md#bm25_bert_rankf), [**`Participants`**](./participants.md#ruir), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.BM25_BERT_RANKF.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.BM25_BERT_RANKF), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/BM25_BERT_RANKF.pdf) 

- :material-rename: **Name:** BM25_BERT_RANKF 
- :fontawesome-solid-user-group: **Participant:** RUIR 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `c4185e258e54ba01c5c88543ebb12c8d` 
- :material-text: **Run description:** In this run, we only used the MS MARCO collection to retrieve passages from. We indexed it in Anserini and retrieved 1000 articles with BM25. We did not retrieve them based on ONLY the query, but also the previous turns. We then reranked the query/passage combo's with BERT. We used a pretrained sequence classification model that was finetuned on MS MARCO.  We reranked three times: one time with only the query to answer as input, one time with the query to answer and the previous utterance as input and one time with the query to answer and the second to last utterance as input. We combined the scores of these runs by taking the max and ranking those max scores afterwards. 

---
#### CFDA_CLIP_RUN1 
[**`Results`**](./results.md#cfda_clip_run1), [**`Participants`**](./participants.md#cfda_clip), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.CFDA_CLIP_RUN1.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.CFDA_CLIP_RUN1), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/CFDA_CLIP_RUN1.pdf) 

- :material-rename: **Name:** CFDA_CLIP_RUN1 
- :fontawesome-solid-user-group: **Participant:** CFDA_CLIP 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `f43d37936ee49af6ee4a729e4cbe0058` 
- :material-text: **Run description:** This run uses MSMARCO as indexing corpus only. All answers are retrieved by BM25 with raw utterances and titles from MSMARCO. And the reranking model is BERT finetuned on MSMARCO dataset, the query for which is coreference resolved by CAsT provided. 

---
#### CFDA_CLIP_RUN6 
[**`Results`**](./results.md#cfda_clip_run6), [**`Participants`**](./participants.md#cfda_clip), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.CFDA_CLIP_RUN6.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.CFDA_CLIP_RUN6), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/CFDA_CLIP_RUN6.pdf) 

- :material-rename: **Name:** CFDA_CLIP_RUN6 
- :fontawesome-solid-user-group: **Participant:** CFDA_CLIP 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `e28ccf56df0e0e6209f91d40d5194be2` 
- :material-text: **Run description:** 1. use coreference resolved query + BM25 + RM3 to retrieve docs 2. use MSMARCO finetuned BERT to rerank 

---
#### CFDA_CLIP_RUN7 
[**`Results`**](./results.md#cfda_clip_run7), [**`Participants`**](./participants.md#cfda_clip), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.CFDA_CLIP_RUN7.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.CFDA_CLIP_RUN7), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/CFDA_CLIP_RUN7.pdf) 

- :material-rename: **Name:** CFDA_CLIP_RUN7 
- :fontawesome-solid-user-group: **Participant:** CFDA_CLIP 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `93ad9b409af6742bcaf56dba77b52c49` 
- :material-text: **Run description:** 1. use doc2query to expand MSMARCO corpus 2. Retrieve docs by BM25 3. Rerank by MSMARCO finetuned BERT 

---
#### CFDA_CLIP_RUN8 
[**`Results`**](./results.md#cfda_clip_run8), [**`Participants`**](./participants.md#cfda_clip), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.CFDA_CLIP_RUN8.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.CFDA_CLIP_RUN8), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/CFDA_CLIP_RUN8.pdf) 

- :material-rename: **Name:** CFDA_CLIP_RUN8 
- :fontawesome-solid-user-group: **Participant:** CFDA_CLIP 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `3a9b9c6415c44b5f5bd3dd85380f5ed8` 
- :material-text: **Run description:** 1. Doc2query model to expand MSMARCO corpus 2. Use previous turns to expand keywords for each turn's query word 3. Retrieve by BM25 4. Rerank by MSMARCO finetuned BERT 5. Use previous turn's answer to expand document candidates 6. Final rerank by MSMARCO finetuned BERT 

---
#### clacBase 
[**`Results`**](./results.md#clacbase), [**`Participants`**](./participants.md#waterlooclarke), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.clacBase.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.clacBase), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/clacBase.pdf) 

- :material-rename: **Name:** clacBase 
- :fontawesome-solid-user-group: **Participant:** WaterlooClarke 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `a285175aeb583d63e005d341ad2763f3` 
- :material-text: **Run description:** BM25 with PRF after query re-writing 

---
#### clacBaseRerank 
[**`Results`**](./results.md#clacbasererank), [**`Participants`**](./participants.md#waterlooclarke), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.clacBaseRerank.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.clacBaseRerank), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/clacBaseRerank.pdf) 

- :material-rename: **Name:** clacBaseRerank 
- :fontawesome-solid-user-group: **Participant:** WaterlooClarke 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `bdc9258e7760e9c0b68022e2f2b80292` 
- :material-text: **Run description:** BM25 with PRF after re-writing, followed by re-ranking with BERT 

---
#### clacMagic 
[**`Results`**](./results.md#clacmagic), [**`Participants`**](./participants.md#waterlooclarke), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.clacMagic.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.clacMagic), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/clacMagic.pdf) 

- :material-rename: **Name:** clacMagic 
- :fontawesome-solid-user-group: **Participant:** WaterlooClarke 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `f814088f3b9ea1b52126e409c0b101df` 
- :material-text: **Run description:** BM25 with PRF after re-writing 

---
#### clacMagicRerank 
[**`Results`**](./results.md#clacmagicrerank), [**`Participants`**](./participants.md#waterlooclarke), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.clacMagicRerank.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.clacMagicRerank), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/clacMagicRerank.pdf) 

- :material-rename: **Name:** clacMagicRerank 
- :fontawesome-solid-user-group: **Participant:** WaterlooClarke 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `e70f7c2db551fe11af5727bab95de780` 
- :material-text: **Run description:** BM25 with PRF after re-writing, followed by re-ranking with BERT 

---
#### combination 
[**`Results`**](./results.md#combination), [**`Participants`**](./participants.md#adapt-dcu), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.combination.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.combination), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/combination.pdf) 

- :material-rename: **Name:** combination 
- :fontawesome-solid-user-group: **Participant:** ADAPT-DCU 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `c9ad573fe4a942a2242dab5c7602f5b1` 
- :material-text: **Run description:** This is the baseline run, where we perform careful NLP based query extraction using spacy library to perform passage retrieval. We used the officially provided expanded questions. We had separate indexes and performed results combination across different data index. 

---
#### coref_cshift 
[**`Results`**](./results.md#coref_cshift), [**`Participants`**](./participants.md#cmu), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.coref_cshift.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.coref_cshift), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/coref_cshift.pdf) 

- :material-rename: **Name:** coref_cshift 
- :fontawesome-solid-user-group: **Participant:** CMU 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/17/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `95168668e1de3288c3bede7fdcc5ca4f` 
- :material-text: **Run description:** Uses BERT attention features for coreference resolution, and identifies context shift using KL Divergence between top retrieved documents for each turn in the conversation. No query expansion used for this run. 

---
#### coref_shift_qe 
[**`Results`**](./results.md#coref_shift_qe), [**`Participants`**](./participants.md#cmu), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.coref_shift_qe.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.coref_shift_qe), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/coref_shift_qe.pdf) 

- :material-rename: **Name:** coref_shift_qe 
- :fontawesome-solid-user-group: **Participant:** CMU 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/17/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `d47cceda0acfa47bf6b59f7aa990b3fd` 
- :material-text: **Run description:** Uses BERT attention features for coreference resolution, and identifies context shift using KL Divergence between top retrieved documents for each turn in the conversation. Retrieval is done using Indri with Query Expansion.   

---
#### datasetreorder 
[**`Results`**](./results.md#datasetreorder), [**`Participants`**](./participants.md#adapt-dcu), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.datasetreorder.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.datasetreorder), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/datasetreorder.pdf) 

- :material-rename: **Name:** datasetreorder 
- :fontawesome-solid-user-group: **Participant:** ADAPT-DCU 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/19/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `38a350ffd53a640083903f6442bb30e8` 
- :material-text: **Run description:** Re-ranking results obtained using 3 different datasets. Combining output results in a sequential fusion based approach. 

---
#### ECNUICA_BERT 
[**`Results`**](./results.md#ecnuica_bert), [**`Participants`**](./participants.md#ecnu-ica), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ECNUICA_BERT.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ECNUICA_BERT), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ECNUICA_BERT.pdf) 

- :material-rename: **Name:** ECNUICA_BERT 
- :fontawesome-solid-user-group: **Participant:** ECNU-ICA 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/17/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `fdeedd0a3474b801cb45ebd6979c6a2a` 
- :material-text: **Run description:** This run use entity linking and keywords algorithm do Neural Language Understanding. Than use BERT pretrained model(Fine-tune with MRPC corpus) compute the relevance between question and answers. 

---
#### ECNUICA_MIX 
[**`Results`**](./results.md#ecnuica_mix), [**`Participants`**](./participants.md#ecnu-ica), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ECNUICA_MIX.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ECNUICA_MIX), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ECNUICA_MIX.pdf) 

- :material-rename: **Name:** ECNUICA_MIX 
- :fontawesome-solid-user-group: **Participant:** ECNU-ICA 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/17/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `a480b3bd7aead9bbebc7d65e905bf7e2` 
- :material-text: **Run description:** This example consist entity linking, keywords extraction and BERT reranking. BERT was fine-tune on MSRP corpus. The final rank was produced by the mix of BERT score and TFIDF score. 

---
#### ECNUICA_ORI 
[**`Results`**](./results.md#ecnuica_ori), [**`Participants`**](./participants.md#ecnu-ica), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ECNUICA_ORI.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ECNUICA_ORI), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ECNUICA_ORI.pdf) 

- :material-rename: **Name:** ECNUICA_ORI 
- :fontawesome-solid-user-group: **Participant:** ECNU-ICA 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/17/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `0d7be301c7287e4487685648f7605ba5` 
- :material-text: **Run description:** A simple example use only simple entity linking and keywords extraction, passage ranking by tfidf score. AllenNLP was be used to do coreference resolve. 

---
#### ensemble 
[**`Results`**](./results.md#ensemble), [**`Participants`**](./participants.md#cmu), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ensemble.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ensemble), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ensemble.pdf) 

- :material-rename: **Name:** ensemble 
- :fontawesome-solid-user-group: **Participant:** CMU 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/17/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `ba14f473ca5855c97dfadee6d178aacb` 
- :material-text: **Run description:** Uses three different retrieval results and combines them (an ensemble system). (1) Uses BERT attention features for coreference resolution, and identifies context shift using KL Divergence between top retrieved documents for each turn in the conversation. (2) All the identified context is used for the second system. (3) Uses a heuristic based context resolution system. Retrieval is done using Indri. 

---
#### galago_rel_1st 
[**`Results`**](./results.md#galago_rel_1st), [**`Participants`**](./participants.md#usi), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.galago_rel_1st.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.galago_rel_1st), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/galago_rel_1st.pdf) 

- :material-rename: **Name:** galago_rel_1st 
- :fontawesome-solid-user-group: **Participant:** USI 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `e0716dfcd7b89da9a7148c0a8fd1d68e` 
- :material-text: **Run description:** In this run, each question is expanded by selection of "relevant" previous questions along with the first question in the conversation. The "relevant" questions are labelled by three human assessors over training queries to train a model for predicting the relevant question(s) from the test set of questions. Passage Retrieval is performed using an open source ad-hoc search engine (Galago). 

---
#### galago_rel_q 
[**`Results`**](./results.md#galago_rel_q), [**`Participants`**](./participants.md#usi), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.galago_rel_q.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.galago_rel_q), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/galago_rel_q.pdf) 

- :material-rename: **Name:** galago_rel_q 
- :fontawesome-solid-user-group: **Participant:** USI 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `5937726b677673c0ca1ff9a44c0c4e95` 
- :material-text: **Run description:** In this run, each question is expanded by selection of "relevant" previous questions. The "relevant" questions are labelled by three human assessors over training queries to train a model for predicting the relevant question(s) from the test set of questions. Passage Retrieval is performed using an open source ad-hoc search engine (Galago). 

---
#### h2oloo_RUN2 
[**`Results`**](./results.md#h2oloo_run2), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.h2oloo_RUN2.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.h2oloo_RUN2), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/h2oloo_RUN2.pdf) 

- :material-rename: **Name:** h2oloo_RUN2 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `3429c01c77295d06157a2fed609fdb68` 
- :material-text: **Run description:** 1st stage: retrieve 1000 candidate passages by query plus topic title key word matching with BM25 2nd stage: rerank the candidate passages by Bert large model trained on Ms Marco passage rerank dataset and while inference, the current query  is combined with some keywords in previous turns 

---
#### h2oloo_RUN3 
[**`Results`**](./results.md#h2oloo_run3), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.h2oloo_RUN3.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.h2oloo_RUN3), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/h2oloo_RUN3.pdf) 

- :material-rename: **Name:** h2oloo_RUN3 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `963863ba5da668aba98bf7d471a24c52` 
- :material-text: **Run description:** 1st stage: retrieve 1000 candidate passages by query plus topic title key word matching with BM25 2nd stage: rerank the candidate passages by Bert large model trained on Ms Marco passage rerank dataset and while inference, the annotated query is used. 

---
#### h2oloo_RUN4 
[**`Results`**](./results.md#h2oloo_run4), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.h2oloo_RUN4.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.h2oloo_RUN4), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/h2oloo_RUN4.pdf) 

- :material-rename: **Name:** h2oloo_RUN4 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `77e6f4cec0505d911014c3c62dad2664` 
- :material-text: **Run description:** 1st stage: retrieve 1000 candidate passages by query plus topic title key word matching with BM25 and RM3  2nd stage: rerank the candidate passages by Bert large model trained on Ms Marco passage rerank dataset and while inference, the annotated query is used. 

---
#### h2oloo_RUN5 
[**`Results`**](./results.md#h2oloo_run5), [**`Participants`**](./participants.md#h2oloo), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.h2oloo_RUN5.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.h2oloo_RUN5), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/h2oloo_RUN5.pdf) 

- :material-rename: **Name:** h2oloo_RUN5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `24465750652ba3c1d839530264b7b708` 
- :material-text: **Run description:** 1st stage: retrieve 1000 candidate passages by query plus some auto selected keywords in previous turns with BM25 2nd stage: rerank the candidate passages by Bert large model trained on Ms Marco passage rerank dataset and while inference, the annotated query is used. 

---
#### humanbert 
[**`Results`**](./results.md#humanbert), [**`Participants`**](./participants.md#ateam), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.humanbert.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.humanbert), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/humanbert.pdf) 

- :material-rename: **Name:** humanbert 
- :fontawesome-solid-user-group: **Participant:** ATeam 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/19/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `9f525b2fa36a114bbf811cd8ea6e6429` 
- :material-text: **Run description:** Using the annotations of the evaluation queries provided + Anserini + BERT 

---
#### ict_wrfml 
[**`Results`**](./results.md#ict_wrfml), [**`Participants`**](./participants.md#ictnet), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ict_wrfml.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ict_wrfml), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ict_wrfml.pdf) 

- :material-rename: **Name:** ict_wrfml 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `97fa40420de9aad6164f701f922d2367` 
- :material-text: **Run description:** We use elastic_search to rerank the baseline results provided by trec cast. 

---
#### ilps-bert-feat1 
[**`Results`**](./results.md#ilps-bert-feat1), [**`Participants`**](./participants.md#uamsterdam), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ilps-bert-feat1.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ilps-bert-feat1), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ilps-bert-feat1.pdf) 

- :material-rename: **Name:** ilps-bert-feat1 
- :fontawesome-solid-user-group: **Participant:** UAmsterdam 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/16/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `0802d3fb297a4ef64bf281e4131cb798` 
- :material-text: **Run description:** A linear combination of VanillaBERT, our unsupervised ranker (LM with Dirichlet smoothing + RM3 and query expansion to represent the conversation topic up to the current turn). VanillaBERT was fine-tuned with 100K triples from the MS MARCO passage ranking dataset. 

---
#### ilps-bert-feat2 
[**`Results`**](./results.md#ilps-bert-feat2), [**`Participants`**](./participants.md#uamsterdam), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ilps-bert-feat2.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ilps-bert-feat2), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ilps-bert-feat2.pdf) 

- :material-rename: **Name:** ilps-bert-feat2 
- :fontawesome-solid-user-group: **Participant:** UAmsterdam 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/16/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `5a3cdf08680f30b4741b4f4e6cc7768b` 
- :material-text: **Run description:** A linear combination of VanillaBERT, our unsupervised ranker (LM with Dirichlet smoothing + RM3 and query expansion to represent the conversation topic up to the current turn). VanillaBERT was fine-tuned with 100K triples from the MS MARCO passage ranking dataset. This is the same model as ilps-bert-feat1 with different hyperparameters. 

---
#### ilps-bert-featq 
[**`Results`**](./results.md#ilps-bert-featq), [**`Participants`**](./participants.md#uamsterdam), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ilps-bert-featq.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ilps-bert-featq), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ilps-bert-featq.pdf) 

- :material-rename: **Name:** ilps-bert-featq 
- :fontawesome-solid-user-group: **Participant:** UAmsterdam 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `8a5c9483cf2fbab1349b06628c1e32b5` 
- :material-text: **Run description:** A linear combination of VanillaBERT, our unsupervised ranker (LM with Dirichlet smoothing + RM3 and query expansion to represent the conversation topic up to the current turn). VanillaBERT was fine-tuned with 100K triples from the MS MARCO passage ranking dataset. The whole model was pre-trained with automatically constructed sequential queries from the QuAC (Question Answering in Context) dataset. 

---
#### ilps-lm-rm3-dt 
[**`Results`**](./results.md#ilps-lm-rm3-dt), [**`Participants`**](./participants.md#uvailps), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ilps-lm-rm3-dt.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ilps-lm-rm3-dt), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ilps-lm-rm3-dt.pdf) 

- :material-rename: **Name:** ilps-lm-rm3-dt 
- :fontawesome-solid-user-group: **Participant:** UvA.ILPS 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/16/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `ac91c5bab25f8bc46ab0892e898fa5ca` 
- :material-text: **Run description:** Unsupervised ranker using LM with Dirichlet smoothing + RM3. Queries are expanded with an automatically extracted set of words that represent the conversation topic up to the current turn. 

---
#### manual_indri 
[**`Results`**](./results.md#manual_indri), [**`Participants`**](./participants.md#cmu), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.manual_indri.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.manual_indri), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/manual_indri.pdf) 

- :material-rename: **Name:** manual_indri 
- :fontawesome-solid-user-group: **Participant:** CMU 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/17/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `154e85cbfed43665f10dbd034d9de7ae` 
- :material-text: **Run description:** Annotated (manually modified) test queries were used as input to Indri for retrieval. 

---
#### MPgate 
[**`Results`**](./results.md#mpgate), [**`Participants`**](./participants.md#rali), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.MPgate.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.MPgate), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/MPgate.pdf) 

- :material-rename: **Name:** MPgate 
- :fontawesome-solid-user-group: **Participant:** RALI 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `1eaf2c684c98fc5c1d16e8f43c56f1ae` 
- :material-text: **Run description:** This model first trains single-turn matching module by MatchPyramid using MSMARCO passage ranking dataset, afterwards the interaction patterns of each turn are aggregated through an attentive aggregation module which is trained on the CAsT Y1 training set. 

---
#### mpi-d5_cqw 
[**`Results`**](./results.md#mpi-d5_cqw), [**`Participants`**](./participants.md#mpi-inf-d5), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.mpi-d5_cqw.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.mpi-d5_cqw), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/mpi-d5_cqw.pdf) 

- :material-rename: **Name:** mpi-d5_cqw 
- :fontawesome-solid-user-group: **Participant:** mpi-inf-d5 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `09e756a99ae0f3f432a33f0206eae0d6` 
- :material-text: **Run description:** We formulated the objective of maximizing the passage score for a query as a combination of similarity and coherence. We first build a word-cooccurrence network from MS MARCO corpus, where words are nodes and there is an edge between two nodes if they co-occur in the same passage in a statistically signifcant way, within a context window. We use NPMI (normalized pointwise mutual information) as a measure of this word association significance. This information is stored as edge weight. Word Embeddings are used to model the similarity between words in the query and words in the passages. This information is stored as node weight for similarity matches above a threshold.   Edge weights between words are considered if they are similar to words in the query and co-occur in a context window. Our method uses indri to retrieve a candidate set for reranking.  The current, the previous and the first query are considered. Our final score consists of a combination of indri rank, node and edge scores.  

---
#### mpi-d5_igraph 
[**`Results`**](./results.md#mpi-d5_igraph), [**`Participants`**](./participants.md#mpi-inf-d5), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.mpi-d5_igraph.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.mpi-d5_igraph), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/mpi-d5_igraph.pdf) 

- :material-rename: **Name:** mpi-d5_igraph 
- :fontawesome-solid-user-group: **Participant:** mpi-inf-d5 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `c4deed6c792b65031b571225adbb7c92` 
- :material-text: **Run description:** We formulated the objective of maximizing the passage score for a query as a combination of similarity and coherence. We first build a word-cooccurrence network from MS MARCO corpus, where words are nodes and there is an edge between two nodes if they co-occur in the same passage in a statistically signifcant way, within a context window. We use NPMI (normalized pointwise mutual information) as a measure of this word association significance. This information is stored as edge weight. Word Embeddings are used to model the similarity between words in the query and words in the passages. This information is stored as node weight for similarity matches above a threshold.   Edge weights between words are considered if they are similar to words in the query and co-occur in a context window. Our method uses indri to retrieve a candidate set for reranking.  The current and the first query are considered. Our final score consists of a combination of indri rank, node and edge scores.  

---
#### mpi-d5_intu 
[**`Results`**](./results.md#mpi-d5_intu), [**`Participants`**](./participants.md#mpi-inf-d5), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.mpi-d5_intu.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.mpi-d5_intu), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/mpi-d5_intu.pdf) 

- :material-rename: **Name:** mpi-d5_intu 
- :fontawesome-solid-user-group: **Participant:** mpi-inf-d5 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `e1056d5f73825215a7bdf473f84784e0` 
- :material-text: **Run description:** We formulated the objective of maximizing the passage score for a query as a combination of similarity and coherence. We first build a word-cooccurrence network from MS MARCO corpus, where words are nodes and there is an edge between two nodes if they co-occur in the same passage in a statistically signifcant way, within a context window. We use NPMI (normalized pointwise mutual information) as a measure of this word association significance. This information is stored as edge weight. Word Embeddings are used to model the similarity between words in the query and words in the passages. This information is stored as node weight for similarity matches above a threshold.   Edge weights between words are considered if they are similar to words in the query and co-occur in a context window. Our method uses indri to retrieve a candidate set for reranking.  The current and the first query are considered. Our final score consists of a combination of indri rank, node and edge scores.  

---
#### mpi-d5_union 
[**`Results`**](./results.md#mpi-d5_union), [**`Participants`**](./participants.md#mpi-inf-d5), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.mpi-d5_union.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.mpi-d5_union), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/mpi-d5_union.pdf) 

- :material-rename: **Name:** mpi-d5_union 
- :fontawesome-solid-user-group: **Participant:** mpi-inf-d5 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `ab0978a9f47aa2245cdd5e77dc3121a4` 
- :material-text: **Run description:** We formulated the objective of maximizing the passage score for a query as a combination of similarity and coherence. We first build a word-cooccurrence network from MS MARCO corpus, where words are nodes and there is an edge between two nodes if they co-occur in the same passage in a statistically signifcant way, within a context window. We use NPMI (normalized pointwise mutual information) as a measure of this word association significance. This information is stored as edge weight. Word Embeddings are used to model the similarity between words in the query and words in the passages. This information is stored as node weight for similarity matches above a threshold.   Edge weights between words are considered if they are similar to words in the query and co-occur in a context window. Our method uses the union of passages, retrieved by three different indri baselines, for reranking. The current and the first query are considered. Our final score consists of a combination of node and edge scores.  

---
#### mpi_base 
[**`Results`**](./results.md#mpi_base), [**`Participants`**](./participants.md#mpii), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.mpi_base.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.mpi_base), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/mpi_base.pdf) 

- :material-rename: **Name:** mpi_base 
- :fontawesome-solid-user-group: **Participant:** mpii 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `e2dc5d1a0537bf9f70f169911fff0895` 
- :material-text: **Run description:** baseline with QE 

---
#### mpi_bert 
[**`Results`**](./results.md#mpi_bert), [**`Participants`**](./participants.md#mpii), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.mpi_bert.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.mpi_bert), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/mpi_bert.pdf) 

- :material-rename: **Name:** mpi_bert 
- :fontawesome-solid-user-group: **Participant:** mpii 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `c3d50deddb3b026c8d70908a8985257a` 
- :material-text: **Run description:** BERT re-ranking baseline with QE 

---
#### MPmlp 
[**`Results`**](./results.md#mpmlp), [**`Participants`**](./participants.md#rali), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.MPmlp.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.MPmlp), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/MPmlp.pdf) 

- :material-rename: **Name:** MPmlp 
- :fontawesome-solid-user-group: **Participant:** RALI 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `2a41ab5be894499a6083291d6099c866` 
- :material-text: **Run description:** This model first trains single-turn matching module by MatchPyramid using MSMARCO passage ranking dataset, afterwards the interaction patterns of each turn are aggregated through an aggregation module which is trained on the CAsT Y1 training set. 

---
#### pg2bert 
[**`Results`**](./results.md#pg2bert), [**`Participants`**](./participants.md#ateam), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.pg2bert.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.pg2bert), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/pg2bert.pdf) 

- :material-rename: **Name:** pg2bert 
- :fontawesome-solid-user-group: **Participant:** ATeam 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/19/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `7d6977862428e0d709ff609a2aac053a` 
- :material-text: **Run description:** Pointer-generator model for question rewriting + Anserini + BERT  

---
#### pgbert 
[**`Results`**](./results.md#pgbert), [**`Participants`**](./participants.md#ateam), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.pgbert.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.pgbert), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/pgbert.pdf) 

- :material-rename: **Name:** pgbert 
- :fontawesome-solid-user-group: **Participant:** ATeam 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/19/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `917e99a1b9f100de035d95a1086e0981` 
- :material-text: **Run description:** Generative model for question rewriting + Anserini + BERT 

---
#### rerankingorder 
[**`Results`**](./results.md#rerankingorder), [**`Participants`**](./participants.md#adapt-dcu), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.rerankingorder.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.rerankingorder), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/rerankingorder.pdf) 

- :material-rename: **Name:** rerankingorder 
- :fontawesome-solid-user-group: **Participant:** ADAPT-DCU 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/19/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `e7f4e2341bd2b54f11b0038e676b651d` 
- :material-text: **Run description:** This is the effective re-ranking run, where we perform careful NLP based query extraction using spacy library to perform passage retrieval. We used the officially provided expanded questions. We had separate indexes and performed results combination across different data index. We used the best results from different datasets and combine them sequentially based on the heuristics for modelling query effetcively using our NLP pipeline. 

---
#### RUCIR-run1 
[**`Results`**](./results.md#rucir-run1), [**`Participants`**](./participants.md#rucir), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.RUCIR-run1.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.RUCIR-run1), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/RUCIR-run1.pdf) 

- :material-rename: **Name:** RUCIR-run1 
- :fontawesome-solid-user-group: **Participant:** RUCIR 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/17/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `214a9371d343a48e91ca4d5fd3ab9b66` 
- :material-text: **Run description:** We use MS MARCO Passage Ranking dataset as training dataset and extract 10 features to train learning to rank model (LambdaMART). As for the test dataset, we use the manual resolved annotations to extract features. 

---
#### RUCIR-run2 
[**`Results`**](./results.md#rucir-run2), [**`Participants`**](./participants.md#rucir), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.RUCIR-run2.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.RUCIR-run2), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/RUCIR-run2.pdf) 

- :material-rename: **Name:** RUCIR-run2 
- :fontawesome-solid-user-group: **Participant:** RUCIR 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/17/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `90d23c0ddc2e1c07195a3ede8d15cb78` 
- :material-text: **Run description:** We use two types of query: original query and the AllenNLP query which is given to generate new query. Send the new query to indri to get the result. 

---
#### RUCIR-run3 
[**`Results`**](./results.md#rucir-run3), [**`Participants`**](./participants.md#rucir), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.RUCIR-run3.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.RUCIR-run3), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/RUCIR-run3.pdf) 

- :material-rename: **Name:** RUCIR-run3 
- :fontawesome-solid-user-group: **Participant:** RUCIR 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/17/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `989165a8a2559ad8a84c90ad8c22747f` 
- :material-text: **Run description:** There are five part of the model. 1. memory network built on previous query and positive document 2. similarity between the representation of current query and document 3. similarity between the representation of current query and the first sentence of the document 4. some statistic feature of previous query, current query and document 5. attentive KNRM model result on current query and document  

---
#### RUCIR-run4 
[**`Results`**](./results.md#rucir-run4), [**`Participants`**](./participants.md#rucir), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.RUCIR-run4.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.RUCIR-run4), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/RUCIR-run4.pdf) 

- :material-rename: **Name:** RUCIR-run4 
- :fontawesome-solid-user-group: **Participant:** RUCIR 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/17/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `cb8466d826da897b339520cab48e4253` 
- :material-text: **Run description:** We use original query and retrieved documents to generate new query. Send the new query to indri to get the result. 

---
#### SMNgate 
[**`Results`**](./results.md#smngate), [**`Participants`**](./participants.md#rali), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.SMNgate.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.SMNgate), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/SMNgate.pdf) 

- :material-rename: **Name:** SMNgate 
- :fontawesome-solid-user-group: **Participant:** RALI 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/16/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `86173a0960bc1905962ba2e16a5bed5b` 
- :material-text: **Run description:** This model first trains single-turn matching module by MatchPyramid using MSMARCO passage ranking dataset, afterwards the interaction patterns of each turn are aggregated through an aggregation module which is trained on the CAsT Y1 training set. 

---
#### SMNmlp 
[**`Results`**](./results.md#smnmlp), [**`Participants`**](./participants.md#rali), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.SMNmlp.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.SMNmlp), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/SMNmlp.pdf) 

- :material-rename: **Name:** SMNmlp 
- :fontawesome-solid-user-group: **Participant:** RALI 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `870a8d959e7b6c28aca85f6cb7aaaeb7` 
- :material-text: **Run description:** This model first trains single-turn matching module by Sequential Matching Network (SMN) using MSMARCO passage ranking dataset, afterwards the interaction patterns of each turn are aggregated through a MLP aggregation module which is trained on the CAsT Y1 training set. 

---
#### topicturnsort 
[**`Results`**](./results.md#topicturnsort), [**`Participants`**](./participants.md#adapt-dcu), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.topicturnsort.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.topicturnsort), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/topicturnsort.pdf) 

- :material-rename: **Name:** topicturnsort 
- :fontawesome-solid-user-group: **Participant:** ADAPT-DCU 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/19/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `07256b10cd4ecaef4f7c9754b9ea16d7` 
- :material-text: **Run description:** In this model, we had three separate indexes for CAR, WAPO and MARCO dataset. We searched for queries using three datasets separately. We merged the retrieval results obtained from BM25 models on three different datasets. We performed document reranking using the percentage of potentially relevant documents returned. We used the expanded queries provided by the task organizers for passage retrieval. 

---
#### UDInfoC_BL 
[**`Results`**](./results.md#udinfoc_bl), [**`Participants`**](./participants.md#udel_fang), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.UDInfoC_BL.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.UDInfoC_BL), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/UDInfoC_BL.pdf) 

- :material-rename: **Name:** UDInfoC_BL 
- :fontawesome-solid-user-group: **Participant:** udel_fang 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/16/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `8920063c8fdadb7c58c05cc55fa454c1` 
- :material-text: **Run description:** Baseline method using Indri 

---
#### UDInfoC_TS 
[**`Results`**](./results.md#udinfoc_ts), [**`Participants`**](./participants.md#udel_fang), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.UDInfoC_TS.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.UDInfoC_TS), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/UDInfoC_TS.pdf) 

- :material-rename: **Name:** UDInfoC_TS 
- :fontawesome-solid-user-group: **Participant:** udel_fang 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/17/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `3b9adaab4c41314eb5b5116a6cc026d4` 
- :material-text: **Run description:** Transfer learning on bert model 

---
#### UDInfoC_TS_2 
[**`Results`**](./results.md#udinfoc_ts_2), [**`Participants`**](./participants.md#udel_fang), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.UDInfoC_TS_2.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.UDInfoC_TS_2), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/UDInfoC_TS_2.pdf) 

- :material-rename: **Name:** UDInfoC_TS_2 
- :fontawesome-solid-user-group: **Participant:** udel_fang 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `f637c03137b4a50094558b8e7a303fb6` 
- :material-text: **Run description:** Another transfer learning based on bert model 

---
#### ug_1stprev3_sdm 
[**`Results`**](./results.md#ug_1stprev3_sdm), [**`Participants`**](./participants.md#uogtr), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ug_1stprev3_sdm.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ug_1stprev3_sdm), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ug_1stprev3_sdm.pdf) 

- :material-rename: **Name:** ug_1stprev3_sdm 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `94636ef379552e028c29f45f2f7df19a` 
- :material-text: **Run description:** This run is a probabilistic run using the Galago search engine.  The first turn and previous three turns are used as context.  For each, a sequential dependence model query is generated and combined together (manually selected weights). Stopping is performed using the Indri stopword list (modified) and stemming via the krovetz stemmer.  

---
#### ug_cedr_rerank 
[**`Results`**](./results.md#ug_cedr_rerank), [**`Participants`**](./participants.md#uogtr), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ug_cedr_rerank.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ug_cedr_rerank), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ug_cedr_rerank.pdf) 

- :material-rename: **Name:** ug_cedr_rerank 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/19/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `73ba7c873354af8d4c3835c883716134` 
- :material-text: **Run description:** This run is a reranking of a pool of results from the top 50 from ug_cont_lin, ug_1stprev3_sdm, and a RM3 feedback run on ug_1stprev3_sdm. It uses the CEDR deep learning model (BERT derived) trained on the MARCO data.   

---
#### ug_cont_lin 
[**`Results`**](./results.md#ug_cont_lin), [**`Participants`**](./participants.md#uogtr), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ug_cont_lin.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ug_cont_lin), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ug_cont_lin.pdf) 

- :material-rename: **Name:** ug_cont_lin 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `1ef6b9b5a4e20f3d46053ed340df22f7` 
- :material-text: **Run description:** The run pools together three runs (ug_1stprev3_sdm, an all context bow run, and a ug_1stprev3_sdm with RM3) and reranks them using a linear ranklib model that uses coordinate ascent. It uses six features that are variants of SDM over the context.  The model is optimized on the CAsT Y1 training data.  

---
#### ug_cur_sdm 
[**`Results`**](./results.md#ug_cur_sdm), [**`Participants`**](./participants.md#uogtr), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.ug_cur_sdm.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.ug_cur_sdm), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/ug_cur_sdm.pdf) 

- :material-rename: **Name:** ug_cur_sdm 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `7bba9a44c3be6c25e7e73ba58bd568b0` 
- :material-text: **Run description:** This run uses manually rewritten queries. It performs SDM over a Galago corpus and performs stopping (indri 418 word list) and stemming (krovetz stemmer).  

---
#### UMASS_DMN_V1 
[**`Results`**](./results.md#umass_dmn_v1), [**`Participants`**](./participants.md#umass), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.UMASS_DMN_V1.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.UMASS_DMN_V1), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/UMASS_DMN_V1.pdf) 

- :material-rename: **Name:** UMASS_DMN_V1 
- :fontawesome-solid-user-group: **Participant:** UMass 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `9f7c4bf434a15101164e5b352b727291` 
- :material-text: **Run description:** This is a deep learning model trained on MS MARCO Conversational Session dataset. The model does not use co-reference resolution. 

---
#### UMASS_DMN_V2 
[**`Results`**](./results.md#umass_dmn_v2), [**`Participants`**](./participants.md#umass), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.UMASS_DMN_V2.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.UMASS_DMN_V2), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/UMASS_DMN_V2.pdf) 

- :material-rename: **Name:** UMASS_DMN_V2 
- :fontawesome-solid-user-group: **Participant:** UMass 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/19/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `897753c060c80ea92582305785ddc390` 
- :material-text: **Run description:** This is a deep learning model trained on MS MARCO Conversational Session dataset. This model uses the provided annotated evaluation dataset with co-reference resolution. 

---
#### UNH-trema-ecn 
[**`Results`**](./results.md#unh-trema-ecn), [**`Participants`**](./participants.md#trema-unh), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.UNH-trema-ecn.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.UNH-trema-ecn), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/UNH-trema-ecn.pdf) 

- :material-rename: **Name:** UNH-trema-ecn 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `4e96c117f687af971bc80767620a8949` 
- :material-text: **Run description:** This method uses an entity and passage run as input. For every entity retrieved for a query, find all frequently co-occurring entities with this entity. For every passage mentioning the given entity, the score of the passage for the query-entity pair is equal to the sum of the frequencies of the frequently co-occurring entities in the passage. Then marginalize over the entities to obtain a passage ranking for the query.  

---
#### UNH-trema-ent 
[**`Results`**](./results.md#unh-trema-ent), [**`Participants`**](./participants.md#trema-unh), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.UNH-trema-ent.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.UNH-trema-ent), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/UNH-trema-ent.pdf) 

- :material-rename: **Name:** UNH-trema-ent 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `eba81fae00d5ebed4bf893284e8e485b` 
- :material-text: **Run description:** This method uses an entity and passage run as input. For every passage retrieved for the query, its score for a query-entity pair is equal to the the number of retrieved entities (for the query) in the passage. This passage score for a query-entity pair where the entities come from the list of entities in the passage. So for every entity in the passage, the score of the passage for the query-entity pair is the same. Then we marginalize over the entities to get a passage ranking for the query.   

---
#### unh-trema-relco 
[**`Results`**](./results.md#unh-trema-relco), [**`Participants`**](./participants.md#trema-unh), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.unh-trema-relco.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.unh-trema-relco), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/unh-trema-relco.pdf) 

- :material-rename: **Name:** unh-trema-relco 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `bedbd354887c1d13aba03f274f0dfd73` 
- :material-text: **Run description:** We first retrieve query-relevant TREC CAR feedback passages using BM25 retrieval model. We then create the candidate entity list of all the entities mentioned in the feedback passages. We create entity-pair of every entity with every other entity present in the candidate entity list. We then check the presence of every entity-pair in the feedback passage, if it is present then the rank of the passage is considered as scoring factor of the entity-pair. The score of every entity is calculated by taking average of entity-pair. Top k entities are selected and if the entity is present in the feedback passage then the score of entity is added with the score of passage, to get the final score of the passage. 

---
#### VESBERT 
[**`Results`**](./results.md#vesbert), [**`Participants`**](./participants.md#ves), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.VESBERT.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.VESBERT), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/VESBERT.pdf) 

- :material-rename: **Name:** VESBERT 
- :fontawesome-solid-user-group: **Participant:** VES 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `61b59029d64b84e79363ad1913ca782a` 
- :material-text: **Run description:** This run implemented using Lucene4ir. the questions passed from a coreference resolution module for each topic and the results passed from a bert re-ranker trained on marco dataset. 

---
#### VESBERT1000 
[**`Results`**](./results.md#vesbert1000), [**`Participants`**](./participants.md#ves), [**`Input`**](https://trec.nist.gov/results/trec28/cast/input.VESBERT1000.gz), [**`Summary`**](https://trec.nist.gov/results/trec28/cast/summary.VESBERT1000), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/cast/VESBERT1000.pdf) 

- :material-rename: **Name:** VESBERT1000 
- :fontawesome-solid-user-group: **Participant:** VES 
- :material-format-text: **Track:** Conversational Assistance 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/18/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `c91368d4e48190287b1faca404de2b69` 
- :material-text: **Run description:** This run has 1000 documents per query and uses lucene, bert and coreference resolution 

---
