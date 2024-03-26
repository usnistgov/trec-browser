# Runs - Deep Learning 2021 

#### bcai_bertm1_ens 
[**`Results`**](./results.md#bcai_bertm1_ens) | [**`Participants`**](./participants.md#bcai) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.bcai_bertm1_ens.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.bcai_bertm1_ens) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/bcai_bertm1_ens.pdf) 

- :material-rename: **Run ID:** bcai_bertm1_ens 
- :fontawesome-solid-user-group: **Participant:** bcai 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/6/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `d39faeb40b6f2b37a13306e5ded2e34b` 
- :material-text: **Run description:** Candidate generation: see description of the run bl_bcai_nn_retr. Ranking: top-200 entries are re-ranked using five BERT-Model1 models that were previously used on MS MARCO V1 leaderboard. These models were fine-tuned using current MS MARCO data. 

---
#### bcai_p_mbert 
[**`Results`**](./results.md#bcai_p_mbert) | [**`Participants`**](./participants.md#bcai) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.bcai_p_mbert.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.bcai_p_mbert) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.bcai_p_mbert) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/bcai_p_mbert.pdf) 

- :material-rename: **Run ID:** bcai_p_mbert 
- :fontawesome-solid-user-group: **Participant:** bcai 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `a13b820d166178f30625dbf5a942aab4` 
- :material-text: **Run description:** 1. First stage see run bl_bcai_p_nn_rt 2. Re-ranking using an ensemble of four BERT-Model 1 models. 

---
#### bcai_p_vbert 
[**`Results`**](./results.md#bcai_p_vbert) | [**`Participants`**](./participants.md#bcai) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.bcai_p_vbert.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.bcai_p_vbert) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.bcai_p_vbert) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/bcai_p_vbert.pdf) 

- :material-rename: **Run ID:** bcai_p_vbert 
- :fontawesome-solid-user-group: **Participant:** bcai 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `fa9350484fd7d78eee81096dc0892cb8` 
- :material-text: **Run description:** 1. First stage see run bl_bcai_p_nn_rt 2. Re-ranking using an ensemble of four vanilla BERT-large models. 

---
#### bigram_qe_cedr 
[**`Results`**](./results.md#bigram_qe_cedr) | [**`Participants`**](./participants.md#certh_iti_m4d) | [**`Proceedings`**](./proceedings.md#m4d-mklab-iti-certh-participation-in-trec-deep-learning-track-2021) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.bigram_qe_cedr.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.bigram_qe_cedr) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/bigram_qe_cedr.pdf) 

- :material-rename: **Run ID:** bigram_qe_cedr 
- :fontawesome-solid-user-group: **Participant:** CERTH_ITI_M4D 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `adaf17feaccdfe9026bd2389e2b4a6e4` 
- :material-text: **Run description:** step 1: BM25 initial retrieval  step 2: query expansion with contextualized embeddings (from untrained BERT) step 3: BM25 with expanded queries step 4: re-ranking with CEDR Query expansion hyperparameters tuned with previous years' qrels on the new dataset. CEDR: trained with this year's train queries 

---
#### bigrams_cont_qe 
[**`Results`**](./results.md#bigrams_cont_qe) | [**`Participants`**](./participants.md#certh_iti_m4d) | [**`Proceedings`**](./proceedings.md#m4d-mklab-iti-certh-participation-in-trec-deep-learning-track-2021) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.bigrams_cont_qe.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.bigrams_cont_qe) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/bigrams_cont_qe.pdf) 

- :material-rename: **Run ID:** bigrams_cont_qe 
- :fontawesome-solid-user-group: **Participant:** CERTH_ITI_M4D 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `c02497567f2d0ec068deeb545b591013` 
- :material-text: **Run description:** A simple query expansion pipeline without reranking. Retrieval with BM25 and query expansion based on contextualized embeddings given from the default BERT (not fine-tuned). The query expansion technique is based on the work "CEQE: Contextualized Embeddings for Query Expansion" (Naseri et al) with some variations.  Previous years' qrels were used for hyperparameter tuning on the new dataset (v2). 

---
#### bl_bcai_nn_rtr 
[**`Results`**](./results.md#bl_bcai_nn_rtr) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.bl_bcai_nn_rtr.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.bl_bcai_nn_rtr) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/bl_bcai_nn_rtr.pdf) 

- :material-rename: **Run ID:** bl_bcai_nn_rtr 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/6/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `0e98d39fedc57b99ed753122688cacd0` 
- :material-text: **Run description:** direct retrieval using a fusion of ANCE (FirstP) and BM25 on doc2query expanded text. 

---
#### bl_bcai_p_nn_rt 
[**`Results`**](./results.md#bl_bcai_p_nn_rt) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.bl_bcai_p_nn_rt.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.bl_bcai_p_nn_rt) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.bl_bcai_p_nn_rt) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/bl_bcai_p_nn_rt.pdf) 

- :material-rename: **Run ID:** bl_bcai_p_nn_rt 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `241539b1e600312b1769668497b19664` 
- :material-text: **Run description:** 1. First stage see run bl_bcai_nn_retr 2. Re-ranking using a mix of passage BM25 and Model 1 (both neural and traditional) scores. 

---
#### bl_bcai_p_trad 
[**`Results`**](./results.md#bl_bcai_p_trad) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.bl_bcai_p_trad.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.bl_bcai_p_trad) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.bl_bcai_p_trad) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/bl_bcai_p_trad.pdf) 

- :material-rename: **Run ID:** bl_bcai_p_trad 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `b849866801e62e02938c3c79c277155c` 
- :material-text: **Run description:** First, we retrieve passages using a non-neural approach (see run bl_bcai_bm25_mdl1). Then, we re-rank passages, using a learned combination of document and passage scores, where passage scores include BM25 and Model 1 scores. 

---
#### bl_bcai_trad 
[**`Results`**](./results.md#bl_bcai_trad) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.bl_bcai_trad.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.bl_bcai_trad) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/bl_bcai_trad.pdf) 

- :material-rename: **Run ID:** bl_bcai_trad 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/6/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `b437127f4705e0664e2fe6861befe0da` 
- :material-text: **Run description:** Re-ranking of BM25 candidates using multi-field BM25 and IBM Model1 scores. 

---
#### bl_bcai_wloo_d 
[**`Results`**](./results.md#bl_bcai_wloo_d) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.bl_bcai_wloo_d.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.bl_bcai_wloo_d) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/bl_bcai_wloo_d.pdf) 

- :material-rename: **Run ID:** bl_bcai_wloo_d 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `9a3ac101acc72848446918b4b43a82e4` 
- :material-text: **Run description:** 1. First stage Jimmy Lin's document retrieval using dense vectors 2. Re-ranking using an ensemble of five Model 1 BERT models. 

---
#### bl_bcai_wloo_p 
[**`Results`**](./results.md#bl_bcai_wloo_p) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.bl_bcai_wloo_p.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.bl_bcai_wloo_p) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.bl_bcai_wloo_p) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/bl_bcai_wloo_p.pdf) 

- :material-rename: **Run ID:** bl_bcai_wloo_p 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `7f84298304a8fb077a042d779c8e5d9d` 
- :material-text: **Run description:** 1. First stage Jimmy Lin's passage retrieval using dense vectors 2. Re-ranking using an ensemble of four vanilla BERT-large models. 

---
#### CIP_run1 
[**`Results`**](./results.md#cip_run1) | [**`Participants`**](./participants.md#cip) | [**`Proceedings`**](./proceedings.md#cip-at-trec-2021-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.CIP_run1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.CIP_run1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/CIP_run1.pdf) 

- :material-rename: **Run ID:** CIP_run1 
- :fontawesome-solid-user-group: **Participant:** CIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `2dca8d728e5b4783a790e878896d7d87` 
- :material-text: **Run description:** In this run, we use the BERT model to re-rank the official candidate documents. Specifically, we utilize the BERT-large which is first trained on MS MARCO v1 passage small train triples, and then fine-tuned on MS MARCO v2 document training data. This BERT re-ranker predicts the relevance of each passage with a query independently, and the document score is given by the average score of the scores of the top-4 passages. All candidate documents are re-ranked by the document scores received.  

---
#### CIP_run2 
[**`Results`**](./results.md#cip_run2) | [**`Participants`**](./participants.md#cip) | [**`Proceedings`**](./proceedings.md#cip-at-trec-2021-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.CIP_run2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.CIP_run2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/CIP_run2.pdf) 

- :material-rename: **Run ID:** CIP_run2 
- :fontawesome-solid-user-group: **Participant:** CIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `3bb9ba53c3b3f7168f3b4811db73d08f` 
- :material-text: **Run description:** In this run, we use the BERT model to re-rank the official candidate documents. Specifically, we utilize the BERT-large which is first trained on MS MARCO v1 passage small train triples, and then fine-tuned on MS MARCO v2 passage data, and lastly fine-tuned on MS MARCO v2 document data. This BERT re-ranker predicts the relevance of each passage with a query independently, and the document score is given by the average score of the scores of the top-4 passages. All candidate documents are re-ranked by the document scores received.  

---
#### CIP_run3 
[**`Results`**](./results.md#cip_run3) | [**`Participants`**](./participants.md#cip) | [**`Proceedings`**](./proceedings.md#cip-at-trec-2021-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.CIP_run3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.CIP_run3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/CIP_run3.pdf) 

- :material-rename: **Run ID:** CIP_run3 
- :fontawesome-solid-user-group: **Participant:** CIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `5f1276704e10d7143caa8f2e48b6cbc7` 
- :material-text: **Run description:** In this run, we use the BERT model to re-rank the official candidate documents. Specifically, we utilize the BERT-large which is first trained on MS MARCO v1 passage small train triples, and then fine-tuned on MS MARCO v2 document data. This BERT re-ranker predicts the relevance of each passage with a query independently, and the document score is given by the score of the best passage (MaxP). All candidate documents are re-ranked by the document scores received.  

---
#### d_bm25 
[**`Results`**](./results.md#d_bm25) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.d_bm25.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.d_bm25) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/d_bm25.pdf) 

- :material-rename: **Run ID:** d_bm25 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `ca88e3eaf20c01fe76787035168d9eac` 
- :material-text: **Run description:** Anserini BM25, default parameters 

---
#### d_bm25rm3 
[**`Results`**](./results.md#d_bm25rm3) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.d_bm25rm3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.d_bm25rm3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/d_bm25rm3.pdf) 

- :material-rename: **Run ID:** d_bm25rm3 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `402de11d1257fe37dba3c769fba855c1` 
- :material-text: **Run description:** Anserini BM25 + RM3, default parameters 

---
#### d_f10_mdt53b 
[**`Results`**](./results.md#d_f10_mdt53b) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.d_f10_mdt53b.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.d_f10_mdt53b) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/d_f10_mdt53b.pdf) 

- :material-rename: **Run ID:** d_f10_mdt53b 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `c9f9b07f73973adc7c806b586f9729a8` 
- :material-text: **Run description:** Uses d_fusion10 as base run. Reranking using Mono-Duo-T5 3B (both trained on TCT-ColBERT HN mined from V2 Passage Collection). 

---
#### d_f10_mdt5base 
[**`Results`**](./results.md#d_f10_mdt5base) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.d_f10_mdt5base.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.d_f10_mdt5base) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/d_f10_mdt5base.pdf) 

- :material-rename: **Run ID:** d_f10_mdt5base 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `088424e31a59c77bd01290869c7d4976` 
- :material-text: **Run description:** Uses d_fusion10 as base run. Reranking using Mono-Duo-T5 base (both trained on TCT-ColBERT HN mined from V2 Passage Collection). 

---
#### d_f10_mt53b 
[**`Results`**](./results.md#d_f10_mt53b) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.d_f10_mt53b.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.d_f10_mt53b) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/d_f10_mt53b.pdf) 

- :material-rename: **Run ID:** d_f10_mt53b 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `a42e2f31a356ef65fe2ee7ddddfdd13d` 
- :material-text: **Run description:** Uses d_fusion10 as base run. Reranking using Mono-T5 3B (trained on TCT-ColBERT HN mined from V2 Passage Collection). 

---
#### d_fusion00 
[**`Results`**](./results.md#d_fusion00) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.d_fusion00.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.d_fusion00) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/d_fusion00.pdf) 

- :material-rename: **Run ID:** d_fusion00 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `9624771f293886e4bac0e2b39fd57592` 
- :material-text: **Run description:** hybrid of TCT-ColBERT HN+ dense retrieval (d_tct0) and uniCOIL (d_unicoil) 

---
#### d_fusion10 
[**`Results`**](./results.md#d_fusion10) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.d_fusion10.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.d_fusion10) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/d_fusion10.pdf) 

- :material-rename: **Run ID:** d_fusion10 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `10ec4560350c2ed87260ae6e5f379188` 
- :material-text: **Run description:** hybrid of TCT-ColBERT HN+ dense retrieval (d_tct1) and uniCOIL (d_unicoil) 

---
#### d_tct0 
[**`Results`**](./results.md#d_tct0) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.d_tct0.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.d_tct0) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/d_tct0.pdf) 

- :material-rename: **Run ID:** d_tct0 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `675b17cd121ac1b033b9e70bb246eec6` 
- :material-text: **Run description:** TCT-ColBERT HN+ dense retrieval (trained on MS MARCO v1, zero shot) 

---
#### d_tct1 
[**`Results`**](./results.md#d_tct1) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.d_tct1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.d_tct1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/d_tct1.pdf) 

- :material-rename: **Run ID:** d_tct1 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `8018f64051e8aa6254d8bb5164de7261` 
- :material-text: **Run description:** TCT-ColBERT HN+ dense retrieval (trained on MS MARCO v2) 

---
#### d_unicoil0 
[**`Results`**](./results.md#d_unicoil0) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.d_unicoil0.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.d_unicoil0) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/d_unicoil0.pdf) 

- :material-rename: **Run ID:** d_unicoil0 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `5592899e3b7a1e14c3b83ed16d3d1550` 
- :material-text: **Run description:** uniCOIL sparse retrieval (no expansion, trained on MS MARCO v1, zero shot) 

---
#### doc_full_100 
[**`Results`**](./results.md#doc_full_100) | [**`Participants`**](./participants.md#alibaba) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.doc_full_100.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.doc_full_100) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/doc_full_100.pdf) 

- :material-rename: **Run ID:** doc_full_100 
- :fontawesome-solid-user-group: **Participant:** ALIBABA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `f90df93af9798ea0fddbc1c1628789a5` 
- :material-text: **Run description:** ance + doc2query + prop top100 

---
#### doc_full_100e 
[**`Results`**](./results.md#doc_full_100e) | [**`Participants`**](./participants.md#alibaba) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.doc_full_100e.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.doc_full_100e) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/doc_full_100e.pdf) 

- :material-rename: **Run ID:** doc_full_100e 
- :fontawesome-solid-user-group: **Participant:** ALIBABA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `087856a0251de74899c636ab21124d4e` 
- :material-text: **Run description:** ance+doc2query recall prop_deepimpact 

---
#### doc_rank_100 
[**`Results`**](./results.md#doc_rank_100) | [**`Participants`**](./participants.md#alibaba) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.doc_rank_100.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.doc_rank_100) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/doc_rank_100.pdf) 

- :material-rename: **Run ID:** doc_rank_100 
- :fontawesome-solid-user-group: **Participant:** ALIBABA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `3ba5d8606b3d40bd19455a937d409718` 
- :material-text: **Run description:** prop 

---
#### dseg_bm25 
[**`Results`**](./results.md#dseg_bm25) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.dseg_bm25.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.dseg_bm25) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/dseg_bm25.pdf) 

- :material-rename: **Run ID:** dseg_bm25 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `9b0c6169928932f05d9dc320e8da4902` 
- :material-text: **Run description:** Anserini BM25, default parameters, on segmented document corpus 

---
#### dseg_bm25rm3 
[**`Results`**](./results.md#dseg_bm25rm3) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.dseg_bm25rm3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.dseg_bm25rm3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/dseg_bm25rm3.pdf) 

- :material-rename: **Run ID:** dseg_bm25rm3 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `5d1f5675ec90d68a83dcddedf44ff37b` 
- :material-text: **Run description:** Anserini BM25 + RM3, default parameters, on segmented document corpus 

---
#### Fast_Forward_2 
[**`Results`**](./results.md#fast_forward_2) | [**`Participants`**](./participants.md#l3s) | [**`Proceedings`**](./proceedings.md#l3s-at-the-trec-2021-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.Fast_Forward_2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.Fast_Forward_2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/Fast_Forward_2.pdf) 

- :material-rename: **Run ID:** Fast_Forward_2 
- :fontawesome-solid-user-group: **Participant:** L3S 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/6/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `129d34be0221b525dcbc81267d2ca88d` 
- :material-text: **Run description:** We retrieve the top 5000 documents from the sparse index for each query using BM25. After that, we retrieve the dense matching score of these 5000 query-document pairs using a pre-trained TCT-Colbert model (castorini/tct_colbert-v2-msmarco). Finally, we interpolate the scores and retrieve the top 100 documents per query.  

---
#### Fast_Forward_3 
[**`Results`**](./results.md#fast_forward_3) | [**`Participants`**](./participants.md#l3s) | [**`Proceedings`**](./proceedings.md#l3s-at-the-trec-2021-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.Fast_Forward_3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.Fast_Forward_3) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.Fast_Forward_3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/Fast_Forward_3.pdf) 

- :material-rename: **Run ID:** Fast_Forward_3 
- :fontawesome-solid-user-group: **Participant:** L3S 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/6/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `106894f297c6ceed0996240daac181f8` 
- :material-text: **Run description:** We retrieve the top 5000 passages from the sparse index for each query using BM25. After that, we retrieve the dense matching score of these 5000 query-passage pairs using a pre-trained TCT-Colbert model (castorini/tct_colbert-v2-msmarco). Finally, we interpolate the scores and retrieve the top 100 passages per query.  

---
#### Fast_Forward_5 
[**`Results`**](./results.md#fast_forward_5) | [**`Participants`**](./participants.md#l3s) | [**`Proceedings`**](./proceedings.md#l3s-at-the-trec-2021-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.Fast_Forward_5.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.Fast_Forward_5) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/Fast_Forward_5.pdf) 

- :material-rename: **Run ID:** Fast_Forward_5 
- :fontawesome-solid-user-group: **Participant:** L3S 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/6/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `d4f800b073d15fbff93992682277295a` 
- :material-text: **Run description:** We retrieve the top 5000 documents from the sparse index for each query using BM25. After that, we retrieve the dense matching score of these 5000 query-document pairs using a pre-trained TCT-Colbert model (castorini/tct_colbert-v2-msmarco). Finally, we interpolate the scores and retrieve the top 100 documents per query.  

---
#### Fast_Forward_7 
[**`Results`**](./results.md#fast_forward_7) | [**`Participants`**](./participants.md#l3s) | [**`Proceedings`**](./proceedings.md#l3s-at-the-trec-2021-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.Fast_Forward_7.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.Fast_Forward_7) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/Fast_Forward_7.pdf) 

- :material-rename: **Run ID:** Fast_Forward_7 
- :fontawesome-solid-user-group: **Participant:** L3S 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/6/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `9fd6cddc99a4efa31e8e762700c18cb8` 
- :material-text: **Run description:** We retrieve the top 5000 documents from the sparse index for each query using BM25. After that, we retrieve the dense matching score of these 5000 query-document pairs using a pre-trained TCT-Colbert model (castorini/tct_colbert-v2-msmarco). Finally, we interpolate the scores and retrieve the top 100 documents per query.  

---
#### Fast_ForwardP_2 
[**`Results`**](./results.md#fast_forwardp_2) | [**`Participants`**](./participants.md#l3s) | [**`Proceedings`**](./proceedings.md#l3s-at-the-trec-2021-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.Fast_ForwardP_2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.Fast_ForwardP_2) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.Fast_ForwardP_2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/Fast_ForwardP_2.pdf) 

- :material-rename: **Run ID:** Fast_ForwardP_2 
- :fontawesome-solid-user-group: **Participant:** L3S 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/6/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `bf2eb22d96b104d3d3834b1adec61e0b` 
- :material-text: **Run description:** We retrieve the top 5000 passages from the sparse index for each query using BM25. After that, we retrieve the dense matching score of these 5000 query-passage pairs using a pre-trained TCT-Colbert model (castorini/tct_colbert-v2-msmarco). Finally, we interpolate the scores and retrieve the top 100 passages per query.  

---
#### Fast_ForwardP_5 
[**`Results`**](./results.md#fast_forwardp_5) | [**`Participants`**](./participants.md#l3s) | [**`Proceedings`**](./proceedings.md#l3s-at-the-trec-2021-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.Fast_ForwardP_5.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.Fast_ForwardP_5) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.Fast_ForwardP_5) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/Fast_ForwardP_5.pdf) 

- :material-rename: **Run ID:** Fast_ForwardP_5 
- :fontawesome-solid-user-group: **Participant:** L3S 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/6/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `7655e3e1c0ac9a01aa2c8b73bdbf046b` 
- :material-text: **Run description:** We retrieve the top 5000 passages from the sparse index for each query using BM25. After that, we retrieve the dense matching score of these 5000 query-passage pairs using a pre-trained TCT-Colbert model (castorini/tct_colbert-v2-msmarco). Finally, we interpolate the scores and retrieve the top 100 passages per query.  

---
#### ielab-AD-uni 
[**`Results`**](./results.md#ielab-ad-uni) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ielab-AD-uni.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ielab-AD-uni) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.ielab-AD-uni) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ielab-AD-uni.pdf) 

- :material-rename: **Run ID:** ielab-AD-uni 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `ff811e2c413cd3dc42139019216f99a5` 
- :material-text: **Run description:** This is a single stage retrieval run, in which we interpolate ADORE top 1000 passage scores with uniCOIL top 1000 scores. Scores are normalised before interpolation. uniCOIL is a BERT based retrieval method. It precomputes token scores in each passage at query time, and requires a single BERT inference to get token scores in query at query time. It has been trained on MS MARCO v1 training dataset, it uses relevant judgments as positive training samples and randomly picks negatives from BM25 top1000. ADORE is a BERT based dense retriever. It has been trained on MS MARCO v1 training dataset. 

---
#### ielab-AD-uni-d 
[**`Results`**](./results.md#ielab-ad-uni-d) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ielab-AD-uni-d.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ielab-AD-uni-d) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ielab-AD-uni-d.pdf) 

- :material-rename: **Run ID:** ielab-AD-uni-d 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `2f72a4a54bce100e3c3c696311fe4c5f` 
- :material-text: **Run description:** This is a single stage retrieval run, in which we interpolate ADORE top 1000 passage scores with uniCOIL top 1000 scores. Scores are normalised before interpolation. uniCOIL is a BERT based retrieval method. It precomputes token scores in each passage at query time, and requires a single BERT inference to get token scores in query at query time. It has been trained on MS MARCO v1 training dataset, it uses relevant judgments as positive training samples and randomly picks negatives from BM25 top1000. ADORE is a BERT based dense retriever. It has been trained on MS MARCO v1 training dataset. All document runs are generated from passage ranking runs. We use passage id map to get document ids and use passage score as the document score. If there are multiple passages in a documents have been retrieved, we use the max score as the document score. 

---
#### ielab-roberta1d 
[**`Results`**](./results.md#ielab-roberta1d) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ielab-roberta1d.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ielab-roberta1d) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ielab-roberta1d.pdf) 

- :material-rename: **Run ID:** ielab-roberta1d 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `1b63f66eeaab43ad01325f32533ff3ff` 
- :material-text: **Run description:** roberta v1 is trained with v2 collection training data, we use NCE loss with 10 hard negatives sampled from top 1000 results of bm25 interpolate uniCOIL run. This model is trained with a single Tesla v100 16G GPU with batch size of 2, max length set to be 128; the training took around 15 hours to complete. We use the trained roberta model to rerank the top 100 passages retrieved by BM25 at query time. All document runs are generated from passage ranking runs. We use passage id map to get document ids and use passage score as the document score. If there are multiple passages in a documents have been retrieved, we use the max score as the document score. 

---
#### ielab-roberta2d 
[**`Results`**](./results.md#ielab-roberta2d) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ielab-roberta2d.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ielab-roberta2d) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ielab-roberta2d.pdf) 

- :material-rename: **Run ID:** ielab-roberta2d 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `1ec01715e81b72d3c089fcd1ab41b264` 
- :material-text: **Run description:** roberta v2 is trained with v2 collection training data, we use NCE loss with 10 hard negatives sampled from top 1000 results of bm25 interpolate uniCOIL run. This model is trained with a single Tesla v100 16G GPU with batch size of 2, max length set to be 128; the training took around 15 hours to complete. We use the trained roberta model to rerank the top 100 passages retrieved by BM25 at query time. All document runs are generated from passage ranking runs. We use passage id map to get document ids and use passage score as the document score. If there are multiple passages in a documents have been retrieved, we use the max score as the document score. 

---
#### ielab-robertav1 
[**`Results`**](./results.md#ielab-robertav1) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ielab-robertav1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ielab-robertav1) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.ielab-robertav1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ielab-robertav1.pdf) 

- :material-rename: **Run ID:** ielab-robertav1 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `c630f0d99df04e6e511c067a76bc792d` 
- :material-text: **Run description:** roberta v1 is trained with v1 collection training data, we use NCE loss with 10 hard negatives sampled from top 1000 results of bm25 interpolate uniCOIL run. This model is trained with a single Tesla v100 16G GPU with batch size of 2, max length set to be 128; the training took around 15 hours to complete. We use the trained roberta model to rerank the top 100 passages retrieved by BM25 at query time. 

---
#### ielab-robertav2 
[**`Results`**](./results.md#ielab-robertav2) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ielab-robertav2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ielab-robertav2) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.ielab-robertav2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ielab-robertav2.pdf) 

- :material-rename: **Run ID:** ielab-robertav2 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `fa9479541195579d548909a6f558b860` 
- :material-text: **Run description:** roberta v2 is trained with v2 collection training data, we use NCE loss with 10 hard negatives sampled from top 1000 results of bm25 interpolate uniCOIL run. This model is trained with a single Tesla v100 16G GPU with batch size of 2, max length set to be 128; the training took around 15 hours to complete. We use the trained roberta model to rerank the top 100 passages retrieved by BM25 at query time. 

---
#### ielab-TILDEv2 
[**`Results`**](./results.md#ielab-tildev2) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ielab-TILDEv2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ielab-TILDEv2) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.ielab-TILDEv2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ielab-TILDEv2.pdf) 

- :material-rename: **Run ID:** ielab-TILDEv2 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `337781dca7b8568c366d12e9bfef1080` 
- :material-text: **Run description:** This is a two stages run: BM25 retrieves the top 1000 passages, and re-rank is done with TILDEv2 model. TILDEv2 is a BERT based reranker, it uses BERT to precompute document representation at indexing time and uses tokeniser to process query at query time. It has been trained on MS MARCO v1 training dataset, it uses relevant judgments as positive training samples and randomly picks negatives from BM25 top 1000. 

---
#### ielab-TILDEv2d 
[**`Results`**](./results.md#ielab-tildev2d) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ielab-TILDEv2d.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ielab-TILDEv2d) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ielab-TILDEv2d.pdf) 

- :material-rename: **Run ID:** ielab-TILDEv2d 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `2bef8db01aa665c04ef2edfa97488d0b` 
- :material-text: **Run description:** This is a two stages run: BM25 retrieves the top 1000 passages, and re-rank is done with TILDEv2 model. TILDEv2 is a BERT based reranker, it uses BERT to precompute document representation at indexing time and uses tokeniser to process query at query time. It has been trained on MS MARCO v1 training dataset, it uses relevant judgments as positive training samples and randomly picks negatives from BM25 top1000. All document runs are generated from passage ranking runs. We use passage id map to get document ids and use passage score as the document score. If there are multiple passages in a documents have been retrieved, we use the max score as the document score.  

---
#### ielab-uniCOIL 
[**`Results`**](./results.md#ielab-unicoil) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ielab-uniCOIL.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ielab-uniCOIL) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.ielab-uniCOIL) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ielab-uniCOIL.pdf) 

- :material-rename: **Run ID:** ielab-uniCOIL 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `71ae5e66995647b1e57a3f98f07c56ff` 
- :material-text: **Run description:** This is a single stage retrieval run, in which we interpolate BM25 top 1000 passage scores with uniCOIL top 1000 scores. Scores are normalised before interpolation. uniCOIL is a BERT based retrieval method. It precomputes token scores in each passage at query time, and requires a single BERT inference to get token scores in query at query time. It has been trained on MS MARCO v1 training dataset, it uses relevant judgments as positive training samples and randomly picks negatives from BM25 top1000. 

---
#### ielab-uniCOIL-d 
[**`Results`**](./results.md#ielab-unicoil-d) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ielab-uniCOIL-d.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ielab-uniCOIL-d) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ielab-uniCOIL-d.pdf) 

- :material-rename: **Run ID:** ielab-uniCOIL-d 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `9cb982d12d737250d210af3da3d731bb` 
- :material-text: **Run description:** This is a single stage retrieval run, in which we interpolate BM25 top 1000 passage scores with uniCOIL top 1000 scores. Scores are normalised before interpolation. uniCOIL is a BERT based retrieval method. It precomputes token scores in each passage at query time, and requires a single BERT inference to get token scores in query at query time. It has been trained on MS MARCO v1 training dataset, it uses relevant judgments as positive training samples and randomly picks negatives from BM25 top1000. All document runs are generated from passage ranking runs. We use passage id map to get document ids and use passage score as the document score. If there are multiple passages in a documents have been retrieved, we use the max score as the document score.  

---
#### ihsm_bicolbert 
[**`Results`**](./results.md#ihsm_bicolbert) | [**`Participants`**](./participants.md#ihsm) | [**`Proceedings`**](./proceedings.md#quality-and-cost-trade-offs-in-passage-re-ranking-task) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ihsm_bicolbert.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ihsm_bicolbert) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.ihsm_bicolbert) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ihsm_bicolbert.pdf) 

- :material-rename: **Run ID:** ihsm_bicolbert 
- :fontawesome-solid-user-group: **Participant:** IHSM 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `14a030e67189667cad76ff02247cd204` 
- :material-text: **Run description:** Colbert model from https://arxiv.org/pdf/2004.12832 with additional hashing layer (as described in https://arxiv.org/pdf/2106.00882) after document vectorization to produce binary vectors for documents. MaxSim ranker part contains de-binarization step. The model uses cosine as a similarity metric and has output vectors dimension set to 256. Model was trained with MarginMSELoss on MSMarco dataset with logits from ensembled cross-encoder models introduced in https://arxiv.org/pdf/2010.02666. 

---
#### ihsm_colbert64 
[**`Results`**](./results.md#ihsm_colbert64) | [**`Participants`**](./participants.md#ihsm) | [**`Proceedings`**](./proceedings.md#quality-and-cost-trade-offs-in-passage-re-ranking-task) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ihsm_colbert64.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ihsm_colbert64) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.ihsm_colbert64) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ihsm_colbert64.pdf) 

- :material-rename: **Run ID:** ihsm_colbert64 
- :fontawesome-solid-user-group: **Participant:** IHSM 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `12b2ca6f7d272a029fde8d5366d42540` 
- :material-text: **Run description:** Colbert model, which was introduced in https://arxiv.org/pdf/2004.12832, with additional layer normalization after final dimensionality reduction linear layer. Output vectors dimension is set to 64, l2 distance is used as a similarity metric. Model was trained with MarginMSELoss on MSMarco dataset with logits from ensembled cross-encoder models introduced in https://arxiv.org/pdf/2010.02666. 

---
#### ihsm_poly8q 
[**`Results`**](./results.md#ihsm_poly8q) | [**`Participants`**](./participants.md#ihsm) | [**`Proceedings`**](./proceedings.md#quality-and-cost-trade-offs-in-passage-re-ranking-task) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.ihsm_poly8q.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.ihsm_poly8q) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.ihsm_poly8q) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/ihsm_poly8q.pdf) 

- :material-rename: **Run ID:** ihsm_poly8q 
- :fontawesome-solid-user-group: **Participant:** IHSM 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `aa9b66f992281640fcd803d649539506` 
- :material-text: **Run description:** Polyencoder architecture was firstly described in https://arxiv.org/abs/1905.01969, it is a split-encoder, which has three main parts: a candidate encoder, a context encoder and a ranker. Candidate encoder allows to precompute all vectors of documents to store them in a search index. This Polyencoder uses https://huggingface.co/castorini/tct_colbert-v2-hn-msmarco as encoder, and has 8 codes for query, dotprod as a score. Model was trained with MarginMSELoss on MSMarco dataset with logits from ensembled cross-encoder models introduced in https://arxiv.org/pdf/2010.02666.  

---
#### max-firstp-pass 
[**`Results`**](./results.md#max-firstp-pass) | [**`Participants`**](./participants.md#cfda_clip) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.max-firstp-pass.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.max-firstp-pass) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/max-firstp-pass.pdf) 

- :material-rename: **Run ID:** max-firstp-pass 
- :fontawesome-solid-user-group: **Participant:** CFDA_CLIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `60663082002bf456bc607205ac861cca` 
- :material-text: **Run description:** We use TCT-ColBERT trained on MsmarcoV1 Document with FirstP; and directly zero-shot transfer to msmarcoV2 Document. We first fuse the retrieval with maxP and firstP approaches (using the same model checkpoint). Then further fuse with TCT-ColBERT trained on MsmarcoV2 passage. In the second fusion, we retrieve passages from passage corpus and then map it to document ID using meta data. 

---
#### maxp 
[**`Results`**](./results.md#maxp) | [**`Participants`**](./participants.md#cfda_clip) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.maxp.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.maxp) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/maxp.pdf) 

- :material-rename: **Run ID:** maxp 
- :fontawesome-solid-user-group: **Participant:** CFDA_CLIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `40abde1f0dcb369a73ef13fe26013f6d` 
- :material-text: **Run description:** We use TCT-ColBERT trained on MsmarcoV1 Document with FirstP; and directly zero-shot transfer to msmarcoV2 Document and retrieve with MaxP. 

---
#### maxp-firstp 
[**`Results`**](./results.md#maxp-firstp) | [**`Participants`**](./participants.md#cfda_clip) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.maxp-firstp.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.maxp-firstp) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/maxp-firstp.pdf) 

- :material-rename: **Run ID:** maxp-firstp 
- :fontawesome-solid-user-group: **Participant:** CFDA_CLIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `0c80ac140f4db78da5d796020f928e35` 
- :material-text: **Run description:** We use TCT-ColBERT trained on MsmarcoV1 Document with FirstP; and directly zero-shot transfer to msmarcoV2 Document. We first fuse the retrieval with maxP and firstP approaches (using the same model checkpoint). 

---
#### maxp_h3 
[**`Results`**](./results.md#maxp_h3) | [**`Participants`**](./participants.md#mpii) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.maxp_h3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.maxp_h3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/maxp_h3.pdf) 

- :material-rename: **Run ID:** maxp_h3 
- :fontawesome-solid-user-group: **Participant:** mpii 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `b85d742c47bb2b623492e565a195eb12` 
- :material-text: **Run description:** BERT-base MaxP reranking d_fusion10 from h2oloo (fine-tuned on MS MARCO v2) 

---
#### mono_d3 
[**`Results`**](./results.md#mono_d3) | [**`Participants`**](./participants.md#mpii) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.mono_d3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.mono_d3) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.mono_d3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/mono_d3.pdf) 

- :material-rename: **Run ID:** mono_d3 
- :fontawesome-solid-user-group: **Participant:** mpii 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `066429503cee1e0e8b906717ac2d4283` 
- :material-text: **Run description:** BERT-base monoBERT reranking p_tct1 from h2oloo (fine-tuned on MS MARCO v2) 

---
#### mono_electra_h3 
[**`Results`**](./results.md#mono_electra_h3) | [**`Participants`**](./participants.md#mpii) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.mono_electra_h3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.mono_electra_h3) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.mono_electra_h3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/mono_electra_h3.pdf) 

- :material-rename: **Run ID:** mono_electra_h3 
- :fontawesome-solid-user-group: **Participant:** mpii 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `82df6aeb833161e486dd083f9a3e6687` 
- :material-text: **Run description:** ELECTRA-base monoBERT reranking p_fusion10 from h2oloo (fine-tuned on MS MARCO v2) 

---
#### mono_h3 
[**`Results`**](./results.md#mono_h3) | [**`Participants`**](./participants.md#mpii) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.mono_h3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.mono_h3) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.mono_h3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/mono_h3.pdf) 

- :material-rename: **Run ID:** mono_h3 
- :fontawesome-solid-user-group: **Participant:** mpii 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `a23ffe48ff79f21bec036f1f0a728d89` 
- :material-text: **Run description:** BERT-base monoBERT reranking p_fusion10 from h2oloo (fine-tuned on MS MARCO v2) 

---
#### NLE_D_quick 
[**`Results`**](./results.md#nle_d_quick) | [**`Participants`**](./participants.md#nle) | [**`Proceedings`**](./proceedings.md#naver-labs-europe-splade-trec-deep-learning-2021) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.NLE_D_quick.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.NLE_D_quick) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/NLE_D_quick.pdf) 

- :material-rename: **Run ID:** NLE_D_quick 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `8edba032c31ef2f18fe57297d12ac3bb` 
- :material-text: **Run description:** This run only performs one pass to rank passages. We use a splade model (https://arxiv.org/abs/2107.05720) trained on MSMARCO v1 without any query encoder (query is encoded just using the bert tokenizer) in order to make retrieval faster. Everything is performed on passages (same result as NLE_P_quick) and then ids are converted to document 

---
#### NLE_D_v1 
[**`Results`**](./results.md#nle_d_v1) | [**`Participants`**](./participants.md#nle) | [**`Proceedings`**](./proceedings.md#naver-labs-europe-splade-trec-deep-learning-2021) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.NLE_D_v1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.NLE_D_v1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/NLE_D_v1.pdf) 

- :material-rename: **Run ID:** NLE_D_v1 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `52e02d76bd8e9f889d4f4c1aa73b6c65` 
- :material-text: **Run description:** This run is divided into three steps: first stage on passages, rerank on passages, passage to document conversion. Steps 1 and 2 are the same (even the same indexes and networks) as our passage run with almost the same name (P instead of D) First stage: We use a splade model (https://arxiv.org/abs/2107.05720) trained on MSMARCO v1 using distillation following (https://arxiv.org/abs/2010.02666). Triplets for distillation come from the aforementioned paper. We retrieve top1k passages. Second stage: We use a mean score ensemble of 7 rerankers. 1 is used off-the-shelf (cross-encoder/ms-marco-MiniLM-L-12-v2 from https://www.sbert.net/docs/pretrained-models/ce-msmarco.html), 2 are trained using triplets extracted from the TOP100 of splade on the train queries and 4 are trained using triplets extracted from the TOP1k of splade on the train queries.  Third stage: We convert passage ids to document ids. Note that mean score ensembling is done after this third stage (so that the mean scores are from documents and not passages). 

---
#### NLE_D_V1andV2 
[**`Results`**](./results.md#nle_d_v1andv2) | [**`Participants`**](./participants.md#nle) | [**`Proceedings`**](./proceedings.md#naver-labs-europe-splade-trec-deep-learning-2021) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.NLE_D_V1andV2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.NLE_D_V1andV2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/NLE_D_V1andV2.pdf) 

- :material-rename: **Run ID:** NLE_D_V1andV2 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `4cc39d7183861576f4238125e441ea8a` 
- :material-text: **Run description:** This run is divided into three steps: first stage on passages, rerank on passages, passage to document conversion. Steps 1 and 2 are the same (even the same indexes and networks) as our passage run with almost the same name (P instead of D) First stage: We use an ensemble of splade models (https://arxiv.org/abs/2107.05720) trained under different settings (4 on MSMARCO v1 and 1 on MSMARCO v2). We retrieve top1k passages. Second stage: We use a mean score ensemble of 10 rerankers. 1 is used off-the-shelf (cross-encoder/ms-marco-MiniLM-L-12-v2 from https://www.sbert.net/docs/pretrained-models/ce-msmarco.html), 2 are trained using triplets extracted from the TOP100 of splade on the MSMARCOv1 train queries and 4 are trained using triplets extracted from the TOP1k of splade on the MSMARCOv1 train queries and 3 trained using triplets extracted from the TOP1k of BM25 on the MSMARCOv2 train queries.  Third stage: We convert passage ids to document ids. Note that mean score ensembling is done after this third stage (so that the mean scores are from documents and not passages). 

---
#### NLE_P_quick 
[**`Results`**](./results.md#nle_p_quick) | [**`Participants`**](./participants.md#nle) | [**`Proceedings`**](./proceedings.md#naver-labs-europe-splade-trec-deep-learning-2021) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.NLE_P_quick.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.NLE_P_quick) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.NLE_P_quick) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/NLE_P_quick.pdf) 

- :material-rename: **Run ID:** NLE_P_quick 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `53024b59932a02d222b8143978950c98` 
- :material-text: **Run description:** This run only performs one pass to rank passages. We use a splade model (https://arxiv.org/abs/2107.05720) trained on MSMARCO v1 without any query encoder (query is encoded just using the bert tokenizer) in order to make retrieval faster. 

---
#### NLE_P_v1 
[**`Results`**](./results.md#nle_p_v1) | [**`Participants`**](./participants.md#nle) | [**`Proceedings`**](./proceedings.md#naver-labs-europe-splade-trec-deep-learning-2021) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.NLE_P_v1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.NLE_P_v1) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.NLE_P_v1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/NLE_P_v1.pdf) 

- :material-rename: **Run ID:** NLE_P_v1 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/6/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `aafc82164696e3eaa6e76f338dd9562b` 
- :material-text: **Run description:** This run is divided into two steps: first stage and rerank. First stage: We use a splade model (https://arxiv.org/abs/2107.05720) trained on MSMARCO v1 using distillation following (https://arxiv.org/abs/2010.02666). Triplets for distillation come from the aforementioned paper. We retrieve top1k passages. Second stage: We use a mean score ensemble of 7 rerankers. 1 is used off-the-shelf (cross-encoder/ms-marco-MiniLM-L-12-v2 from https://www.sbert.net/docs/pretrained-models/ce-msmarco.html), 2 are trained using triplets extracted from the TOP100 of splade on the train queries and 4 are trained using triplets extracted from the TOP1k of splade on the train queries.  

---
#### NLE_P_V1andV2 
[**`Results`**](./results.md#nle_p_v1andv2) | [**`Participants`**](./participants.md#nle) | [**`Proceedings`**](./proceedings.md#naver-labs-europe-splade-trec-deep-learning-2021) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.NLE_P_V1andV2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.NLE_P_V1andV2) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.NLE_P_V1andV2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/NLE_P_V1andV2.pdf) 

- :material-rename: **Run ID:** NLE_P_V1andV2 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `e9bbe02cc8b5340a5e10c0b6b8baf42c` 
- :material-text: **Run description:** This run is divided into two steps: first stage and rerank. First stage: We use an ensemble of splade models (https://arxiv.org/abs/2107.05720) trained under different settings (4 on MSMARCO v1 and 1 on MSMARCO v2). We retrieve top1k passages. Second stage: We use a mean score ensemble of 10 rerankers. 1 is used off-the-shelf (cross-encoder/ms-marco-MiniLM-L-12-v2 from https://www.sbert.net/docs/pretrained-models/ce-msmarco.html), 2 are trained using triplets extracted from the TOP100 of splade on the MSMARCOv1 train queries and 4 are trained using triplets extracted from the TOP1k of splade on the MSMARCOv1 train queries and 3 trained using triplets extracted from the TOP1k of BM25 on the MSMARCOv2 train queries.   

---
#### p_bm25 
[**`Results`**](./results.md#p_bm25) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.p_bm25.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.p_bm25) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.p_bm25) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/p_bm25.pdf) 

- :material-rename: **Run ID:** p_bm25 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `5ef5b44895dc5e1eddd9660d9e361421` 
- :material-text: **Run description:** Anserini BM25, default parameters 

---
#### p_bm25rm3 
[**`Results`**](./results.md#p_bm25rm3) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.p_bm25rm3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.p_bm25rm3) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.p_bm25rm3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/p_bm25rm3.pdf) 

- :material-rename: **Run ID:** p_bm25rm3 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `2744e65480c2ec468c78c96e90055138` 
- :material-text: **Run description:** Anserini BM25 + RM3, default parameters 

---
#### p_f10_mdt53b 
[**`Results`**](./results.md#p_f10_mdt53b) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.p_f10_mdt53b.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.p_f10_mdt53b) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.p_f10_mdt53b) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/p_f10_mdt53b.pdf) 

- :material-rename: **Run ID:** p_f10_mdt53b 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `15942385d81560a69849f25c4d935bf3` 
- :material-text: **Run description:** Uses p_fusion10 as base run. Reranking using Mono-Duo-T5 3B (trained on TCT-ColBERT HN mined from V2 Passage Collection). 

---
#### p_f10_mdt5base 
[**`Results`**](./results.md#p_f10_mdt5base) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.p_f10_mdt5base.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.p_f10_mdt5base) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.p_f10_mdt5base) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/p_f10_mdt5base.pdf) 

- :material-rename: **Run ID:** p_f10_mdt5base 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `f0d88d8346c7c9f9bf085f39059c8e80` 
- :material-text: **Run description:** Uses p_fusion10 as base run. Reranking using Mono-Duo-T5 base (trained on TCT-ColBERT HN mined from V2 Passage Collection). 

---
#### p_f10_mt53b 
[**`Results`**](./results.md#p_f10_mt53b) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.p_f10_mt53b.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.p_f10_mt53b) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.p_f10_mt53b) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/p_f10_mt53b.pdf) 

- :material-rename: **Run ID:** p_f10_mt53b 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `b008142132fbde3854671b7ffcd7bc4e` 
- :material-text: **Run description:** Uses p_fusion10 as base run. Reranking using Mono-T5 3B (trained on TCT-ColBERT HN mined from V2 Passage Collection). 

---
#### p_fusion00 
[**`Results`**](./results.md#p_fusion00) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.p_fusion00.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.p_fusion00) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.p_fusion00) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/p_fusion00.pdf) 

- :material-rename: **Run ID:** p_fusion00 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `e9fef47413d59a468cc9fc4c57a6c760` 
- :material-text: **Run description:** hybrid of TCT-ColBERT HN+ dense retrieval (d_tct0) and uniCOIL (d_unicoil) 

---
#### p_fusion10 
[**`Results`**](./results.md#p_fusion10) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.p_fusion10.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.p_fusion10) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.p_fusion10) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/p_fusion10.pdf) 

- :material-rename: **Run ID:** p_fusion10 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `c087263907409c8541bd2ee3946da13b` 
- :material-text: **Run description:** hybrid of TCT-ColBERT HN+ dense retrieval (d_tct1) and uniCOIL (d_unicoil) 

---
#### p_tct0 
[**`Results`**](./results.md#p_tct0) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.p_tct0.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.p_tct0) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.p_tct0) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/p_tct0.pdf) 

- :material-rename: **Run ID:** p_tct0 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `b73d2317b0e51b2d29112acddb5de0ec` 
- :material-text: **Run description:** TCT-ColBERT HN+ dense retrieval (trained on MS MARCO v1, zero shot) 

---
#### p_tct1 
[**`Results`**](./results.md#p_tct1) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.p_tct1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.p_tct1) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.p_tct1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/p_tct1.pdf) 

- :material-rename: **Run ID:** p_tct1 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `1bb5692f50e1cd1e285fc97e3c8896ee` 
- :material-text: **Run description:** TCT-ColBERT HN+ dense retrieval (trained on MS MARCO v2) 

---
#### p_unicoil0 
[**`Results`**](./results.md#p_unicoil0) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.p_unicoil0.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.p_unicoil0) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.p_unicoil0) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/p_unicoil0.pdf) 

- :material-rename: **Run ID:** p_unicoil0 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `dc2d5404e86654f436c7260fd0dccb83` 
- :material-text: **Run description:** uniCOIL sparse retrieval (no expansion, trained on MS MARCO v1, zero shot) 

---
#### parade_bm25 
[**`Results`**](./results.md#parade_bm25) | [**`Participants`**](./participants.md#mpii) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.parade_bm25.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.parade_bm25) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/parade_bm25.pdf) 

- :material-rename: **Run ID:** parade_bm25 
- :fontawesome-solid-user-group: **Participant:** mpii 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `4ef93e9136dccfa8a64985e40ad8684c` 
- :material-text: **Run description:** BERT-base PARADE reranking BM25 (fine-tuned on MS MARCO v2) 

---
#### parade_h3 
[**`Results`**](./results.md#parade_h3) | [**`Participants`**](./participants.md#mpii) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.parade_h3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.parade_h3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/parade_h3.pdf) 

- :material-rename: **Run ID:** parade_h3 
- :fontawesome-solid-user-group: **Participant:** mpii 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `9d9ee392000d2125335c9e2150dd847f` 
- :material-text: **Run description:** BERT-base PARADE reranking d_fusion10 from h2oloo (fine-tuned on MS MARCO v2) 

---
#### pash_doc_f1 
[**`Results`**](./results.md#pash_doc_f1) | [**`Participants`**](./participants.md#pash) | [**`Proceedings`**](./proceedings.md#pash-at-trec-2021-deep-learning-track-generative-enhanced-model-for-multi-stagerankingtrack-dl) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pash_doc_f1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pash_doc_f1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pash_doc_f1.pdf) 

- :material-rename: **Run ID:** pash_doc_f1 
- :fontawesome-solid-user-group: **Participant:** PASH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `0ec318a9b78db35c5cb4fbeb3eaefae1` 
- :material-text: **Run description:** We adopt a multi-stage ranking framework combines DeBERTa-2.6B and T5-3b. We use a multi-way matching composed of n-grams and BM25+docT5query(neural document expansion). 

---
#### pash_doc_f4 
[**`Results`**](./results.md#pash_doc_f4) | [**`Participants`**](./participants.md#pash) | [**`Proceedings`**](./proceedings.md#pash-at-trec-2021-deep-learning-track-generative-enhanced-model-for-multi-stagerankingtrack-dl) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pash_doc_f4.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pash_doc_f4) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pash_doc_f4.pdf) 

- :material-rename: **Run ID:** pash_doc_f4 
- :fontawesome-solid-user-group: **Participant:** PASH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `cdc3ef92ceb6d706ba8a8c49eb591c53` 
- :material-text: **Run description:** We adopt a multi-stage ranking framework combines DeBERTa-2.6B and T5-3b. We use a multi-way matching composed of n-grams and BM25+docT5query(neural document expansion). 

---
#### pash_doc_f5 
[**`Results`**](./results.md#pash_doc_f5) | [**`Participants`**](./participants.md#pash) | [**`Proceedings`**](./proceedings.md#pash-at-trec-2021-deep-learning-track-generative-enhanced-model-for-multi-stagerankingtrack-dl) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pash_doc_f5.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pash_doc_f5) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pash_doc_f5.pdf) 

- :material-rename: **Run ID:** pash_doc_f5 
- :fontawesome-solid-user-group: **Participant:** PASH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `c86b1faf7ec7f76e3aec43c49cb502e3` 
- :material-text: **Run description:** We adopt a multi-stage ranking framework combines DeBERTa-2.6B and T5-3b. We use a multi-way matching composed of n-grams and BM25+docT5query(neural document expansion). 

---
#### pash_doc_r1 
[**`Results`**](./results.md#pash_doc_r1) | [**`Participants`**](./participants.md#pash) | [**`Proceedings`**](./proceedings.md#pash-at-trec-2021-deep-learning-track-generative-enhanced-model-for-multi-stagerankingtrack-dl) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pash_doc_r1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pash_doc_r1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pash_doc_r1.pdf) 

- :material-rename: **Run ID:** pash_doc_r1 
- :fontawesome-solid-user-group: **Participant:** PASH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `f6483ca40214b750335dfca7a0502b4d` 
- :material-text: **Run description:** We adopt a multi-stage ranking framework combines DeBERTa-2.6B and T5-3b. We use a multi-way matching composed of n-grams and BM25+docT5query(neural document expansion). 

---
#### pash_doc_r2 
[**`Results`**](./results.md#pash_doc_r2) | [**`Participants`**](./participants.md#pash) | [**`Proceedings`**](./proceedings.md#pash-at-trec-2021-deep-learning-track-generative-enhanced-model-for-multi-stagerankingtrack-dl) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pash_doc_r2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pash_doc_r2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pash_doc_r2.pdf) 

- :material-rename: **Run ID:** pash_doc_r2 
- :fontawesome-solid-user-group: **Participant:** PASH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `9fcbdaec0e2a6c83ffa3afe8caedba4f` 
- :material-text: **Run description:** We adopt a multi-stage ranking framework combines DeBERTa-2.6B and T5-3b. We use a multi-way matching composed of n-grams and BM25+docT5query(neural document expansion). 

---
#### pash_doc_r3 
[**`Results`**](./results.md#pash_doc_r3) | [**`Participants`**](./participants.md#pash) | [**`Proceedings`**](./proceedings.md#pash-at-trec-2021-deep-learning-track-generative-enhanced-model-for-multi-stagerankingtrack-dl) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pash_doc_r3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pash_doc_r3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pash_doc_r3.pdf) 

- :material-rename: **Run ID:** pash_doc_r3 
- :fontawesome-solid-user-group: **Participant:** PASH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `8b5786369ddacc7ad1ce8c2c70258b43` 
- :material-text: **Run description:** We adopt a multi-stage ranking framework combines DeBERTa-2.6B and T5-3b. We use a multi-way matching composed of n-grams and BM25+docT5query(neural document expansion). 

---
#### pash_f1 
[**`Results`**](./results.md#pash_f1) | [**`Participants`**](./participants.md#pash) | [**`Proceedings`**](./proceedings.md#pash-at-trec-2021-deep-learning-track-generative-enhanced-model-for-multi-stagerankingtrack-dl) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pash_f1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pash_f1) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.pash_f1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pash_f1.pdf) 

- :material-rename: **Run ID:** pash_f1 
- :fontawesome-solid-user-group: **Participant:** PASH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `001169a4810355fdcf653c451b388f1c` 
- :material-text: **Run description:** We adopt a multi-stage ranking framework combines DeBERTa-2.6B and T5-3b. We use a multi-way matching composed of n-grams and BM25+docT5query(neural document expansion). 

---
#### pash_f2 
[**`Results`**](./results.md#pash_f2) | [**`Participants`**](./participants.md#pash) | [**`Proceedings`**](./proceedings.md#pash-at-trec-2021-deep-learning-track-generative-enhanced-model-for-multi-stagerankingtrack-dl) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pash_f2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pash_f2) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.pash_f2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pash_f2.pdf) 

- :material-rename: **Run ID:** pash_f2 
- :fontawesome-solid-user-group: **Participant:** PASH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `985701c361aeb3ea1b8a3fce4204f15e` 
- :material-text: **Run description:** We adopt a multi-stage ranking framework combines DeBERTa-2.6B and T5-3b. We use a multi-way matching composed of n-grams and BM25+docT5query(neural document expansion).  

---
#### pash_f3 
[**`Results`**](./results.md#pash_f3) | [**`Participants`**](./participants.md#pash) | [**`Proceedings`**](./proceedings.md#pash-at-trec-2021-deep-learning-track-generative-enhanced-model-for-multi-stagerankingtrack-dl) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pash_f3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pash_f3) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.pash_f3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pash_f3.pdf) 

- :material-rename: **Run ID:** pash_f3 
- :fontawesome-solid-user-group: **Participant:** PASH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `86dd3f83ecfa70d573ab9e3e4cdc4578` 
- :material-text: **Run description:** We adopt a multi-stage ranking framework combines DeBERTa-2.6B and T5-3b. We use a multi-way matching composed of n-grams and BM25+docT5query(neural document expansion).  

---
#### pash_r1 
[**`Results`**](./results.md#pash_r1) | [**`Participants`**](./participants.md#pash) | [**`Proceedings`**](./proceedings.md#pash-at-trec-2021-deep-learning-track-generative-enhanced-model-for-multi-stagerankingtrack-dl) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pash_r1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pash_r1) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.pash_r1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pash_r1.pdf) 

- :material-rename: **Run ID:** pash_r1 
- :fontawesome-solid-user-group: **Participant:** PASH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `4cb96d5e0f64928398bf19c7c437c571` 
- :material-text: **Run description:** We adopt a multi-stage ranking framework combines DeBERTa-2.6B and T5-3b. 

---
#### pash_r2 
[**`Results`**](./results.md#pash_r2) | [**`Participants`**](./participants.md#pash) | [**`Proceedings`**](./proceedings.md#pash-at-trec-2021-deep-learning-track-generative-enhanced-model-for-multi-stagerankingtrack-dl) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pash_r2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pash_r2) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.pash_r2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pash_r2.pdf) 

- :material-rename: **Run ID:** pash_r2 
- :fontawesome-solid-user-group: **Participant:** PASH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `03a0cabdf85452c54c87a435fd6efd8a` 
- :material-text: **Run description:** We adopt a multi-stage ranking framework combines DeBERTa-2.6B and T5-3b. We use a multi-way matching composed of n-grams and BM25+docT5query(neural document expansion). 

---
#### pash_r3 
[**`Results`**](./results.md#pash_r3) | [**`Participants`**](./participants.md#pash) | [**`Proceedings`**](./proceedings.md#pash-at-trec-2021-deep-learning-track-generative-enhanced-model-for-multi-stagerankingtrack-dl) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pash_r3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pash_r3) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.pash_r3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pash_r3.pdf) 

- :material-rename: **Run ID:** pash_r3 
- :fontawesome-solid-user-group: **Participant:** PASH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `e616cb840af05d48154660298b44d702` 
- :material-text: **Run description:** We adopt a multi-stage ranking framework combines DeBERTa-2.6B and T5-3b. We use a multi-way matching composed of n-grams and BM25+docT5query(neural document expansion). 

---
#### pass_full_1000 
[**`Results`**](./results.md#pass_full_1000) | [**`Participants`**](./participants.md#alibaba) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pass_full_1000.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pass_full_1000) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.pass_full_1000) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pass_full_1000.pdf) 

- :material-rename: **Run ID:** pass_full_1000 
- :fontawesome-solid-user-group: **Participant:** ALIBABA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `724b8f93add87cd5b0b65bfe2af6acd3` 
- :material-text: **Run description:** passv2_full_rank ance + doc2query+prop_deepimpact 

---
#### pass_full_1000e 
[**`Results`**](./results.md#pass_full_1000e) | [**`Participants`**](./participants.md#alibaba) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pass_full_1000e.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pass_full_1000e) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.pass_full_1000e) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pass_full_1000e.pdf) 

- :material-rename: **Run ID:** pass_full_1000e 
- :fontawesome-solid-user-group: **Participant:** ALIBABA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `2a8bd727ebe7b545a45500b41a7be335` 
- :material-text: **Run description:** ance+doc2query recall prop_deepimpact 

---
#### pass_rank_100 
[**`Results`**](./results.md#pass_rank_100) | [**`Participants`**](./participants.md#alibaba) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.pass_rank_100.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.pass_rank_100) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.pass_rank_100) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/pass_rank_100.pdf) 

- :material-rename: **Run ID:** pass_rank_100 
- :fontawesome-solid-user-group: **Participant:** ALIBABA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `8a47463958dae7cc98af224f4741977a` 
- :material-text: **Run description:** prop_deepimpact 

---
#### paug_bm25 
[**`Results`**](./results.md#paug_bm25) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.paug_bm25.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.paug_bm25) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.paug_bm25) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/paug_bm25.pdf) 

- :material-rename: **Run ID:** paug_bm25 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `545cd65a2766d2c65a5e6e3fd5e7728b` 
- :material-text: **Run description:** Anserini BM25, default parameters, on augmented passage corpus 

---
#### paug_bm25rm3 
[**`Results`**](./results.md#paug_bm25rm3) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.paug_bm25rm3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.paug_bm25rm3) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.paug_bm25rm3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/paug_bm25rm3.pdf) 

- :material-rename: **Run ID:** paug_bm25rm3 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `7d625a3680f82cc58d2188c4933f3c72` 
- :material-text: **Run description:** Anserini BM25 + RM3, default parameters, on augmented passage corpus 

---
#### top1000 
[**`Results`**](./results.md#top1000) | [**`Participants`**](./participants.md#uamsterdam) | [**`Proceedings`**](./proceedings.md#recall-aspects-of-transformers-for-text-ranking) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.top1000.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.top1000) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.top1000) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/top1000.pdf) 

- :material-rename: **Run ID:** top1000 
- :fontawesome-solid-user-group: **Participant:** UAmsterdam 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `e56e4d13a14ccbf549d166df55797b03` 
- :material-text: **Run description:** BM25 top-1000, re-ranked using interaction BERT filtering out the top-100. 

---
#### TUW_DR_Base 
[**`Results`**](./results.md#tuw_dr_base) | [**`Participants`**](./participants.md#tu_vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-at-trec-dl-and-podcast-2021-simple-compression-for-dense-retrieval) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.TUW_DR_Base.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.TUW_DR_Base) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.TUW_DR_Base) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/TUW_DR_Base.pdf) 

- :material-rename: **Run ID:** TUW_DR_Base 
- :fontawesome-solid-user-group: **Participant:** TU_Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `f99c01f2cf43a827b341b41c30f5ce3e` 
- :material-text: **Run description:** This is a baseline dense retrieval model (based on DistilBERT) trained on the MSMARCO-V1 training triples (using BM25 negative samples) and a simple RankNet loss with a batch size of 32 using the binary relevance labels, without any knowledge distillation. For inference we use ONNX runtime and BERT optimizations with fp16 (resulting vectors are also fp16).  

---
#### TUW_IDCM_ALL 
[**`Results`**](./results.md#tuw_idcm_all) | [**`Participants`**](./participants.md#tu_vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-at-trec-dl-and-podcast-2021-simple-compression-for-dense-retrieval) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.TUW_IDCM_ALL.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.TUW_IDCM_ALL) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/TUW_IDCM_ALL.pdf) 

- :material-rename: **Run ID:** TUW_IDCM_ALL 
- :fontawesome-solid-user-group: **Participant:** TU_Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `d6e070bff56d5e6bf007c185f1987cb6` 
- :material-text: **Run description:** This is our IDCM (intra document cascade model) with a all passage selection (meaning DistilBERT scores all passages of the document) and a maximum document length of 2,000. The re-ranking is done on the given top100 set (Title and body of documents are concatenated and fed into the model).    

---
#### TUW_IDCM_S4 
[**`Results`**](./results.md#tuw_idcm_s4) | [**`Participants`**](./participants.md#tu_vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-at-trec-dl-and-podcast-2021-simple-compression-for-dense-retrieval) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.TUW_IDCM_S4.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.TUW_IDCM_S4) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/TUW_IDCM_S4.pdf) 

- :material-rename: **Run ID:** TUW_IDCM_S4 
- :fontawesome-solid-user-group: **Participant:** TU_Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `2d6e087979661b60ee501cd90d077443` 
- :material-text: **Run description:** This is our IDCM (intra document cascade model) with a 4 passage selection (meaning DistilBERT scores the top 4 passages of our CK selection module) and a maximum document length of 2,000. The re-ranking is done on the given top100 set (Title and body of documents are concatenated and fed into the model). 

---
#### TUW_TAS-B_768 
[**`Results`**](./results.md#tuw_tas-b_768) | [**`Participants`**](./participants.md#tu_vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-at-trec-dl-and-podcast-2021-simple-compression-for-dense-retrieval) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.TUW_TAS-B_768.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.TUW_TAS-B_768) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.TUW_TAS-B_768) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/TUW_TAS-B_768.pdf) 

- :material-rename: **Run ID:** TUW_TAS-B_768 
- :fontawesome-solid-user-group: **Participant:** TU_Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `e562417be5074cc1b7fdfa79451f4787` 
- :material-text: **Run description:** We use our publicly available checkpoint (https://huggingface.co/sebastian-hofstaetter/distilbert-dot-tas_b-b256-msmarco) of our TAS-Balanced trained DistilBERT dense retrieval model in a brute-force search configuration. For inference we use ONNX runtime and BERT optimizations with fp16 (resulting vectors are also fp16). 

---
#### TUW_TAS-B_ANN 
[**`Results`**](./results.md#tuw_tas-b_ann) | [**`Participants`**](./participants.md#tu_vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-at-trec-dl-and-podcast-2021-simple-compression-for-dense-retrieval) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.TUW_TAS-B_ANN.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.TUW_TAS-B_ANN) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.TUW_TAS-B_ANN) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/TUW_TAS-B_ANN.pdf) 

- :material-rename: **Run ID:** TUW_TAS-B_ANN 
- :fontawesome-solid-user-group: **Participant:** TU_Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `1d04515caec6c97da5e3048119fc425f` 
- :material-text: **Run description:** This TAS-Balanced trained model (based on DistilBERT) uses a compression layer at the end to produce 192 dimensional embeddings in fp16 (a 8x reduction to a default 768 dim output in fp32), we then indexed the vectors with HNSW (using 96 neighbors per vector). For inference we use ONNX runtime and BERT optimizations with fp16 (resulting vectors are also fp16).   

---
#### uogTrBaseDD 
[**`Results`**](./results.md#uogtrbasedd) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrBaseDD.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrBaseDD) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrBaseDD.pdf) 

- :material-rename: **Run ID:** uogTrBaseDD 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `b0957438d05773971b2debe0c8579226` 
- :material-text: **Run description:** PyTerrier/Terrier DPH  on the document corpus 

---
#### uogTrBaseDDpmp 
[**`Results`**](./results.md#uogtrbaseddpmp) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrBaseDDpmp.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrBaseDDpmp) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrBaseDDpmp.pdf) 

- :material-rename: **Run ID:** uogTrBaseDDpmp 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `6c4ae32d7d68b95df4599e6d65853cb7` 
- :material-text: **Run description:** PyTerrier/Terrier DPH  on the passage corpus followed by mapping to docnos, and max passage 

---
#### uogTrBaseDDQ 
[**`Results`**](./results.md#uogtrbaseddq) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrBaseDDQ.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrBaseDDQ) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrBaseDDQ.pdf) 

- :material-rename: **Run ID:** uogTrBaseDDQ 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `6faca1f643556e7e4024e6bc971eb9cb` 
- :material-text: **Run description:** PyTerrier/Terrier DPH + Bo1 QE on the document corpus 

---
#### uogTrBaseDDQC 
[**`Results`**](./results.md#uogtrbaseddqc) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrBaseDDQC.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrBaseDDQC) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrBaseDDQC.pdf) 

- :material-rename: **Run ID:** uogTrBaseDDQC 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `00fff5b8297c31c0dfb6466966b45f79` 
- :material-text: **Run description:** PyTerrier/Terrier DPH + Bo1QE ColBERT and maxpassage 

---
#### uogTrBaseDDQpmp 
[**`Results`**](./results.md#uogtrbaseddqpmp) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrBaseDDQpmp.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrBaseDDQpmp) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrBaseDDQpmp.pdf) 

- :material-rename: **Run ID:** uogTrBaseDDQpmp 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `7e97ec9d58068e164508fc8eda2b9379` 
- :material-text: **Run description:** PyTerrier/Terrier DPH + Bo1 QE on the passage corpus followed by mapping to docnos, and max passage 

---
#### uogTrBasePD 
[**`Results`**](./results.md#uogtrbasepd) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrBasePD.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrBasePD) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.uogTrBasePD) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrBasePD.pdf) 

- :material-rename: **Run ID:** uogTrBasePD 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `8406afcf86c1970df67cd8654b58fa6d` 
- :material-text: **Run description:** PyTerrier/Terrier DPH 

---
#### uogTrBasePDQ 
[**`Results`**](./results.md#uogtrbasepdq) | [**`Participants`**](./participants.md#baselines) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrBasePDQ.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrBasePDQ) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.uogTrBasePDQ) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrBasePDQ.pdf) 

- :material-rename: **Run ID:** uogTrBasePDQ 
- :fontawesome-solid-user-group: **Participant:** BASELINES 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `984975934351867b58125309b8343cd2` 
- :material-text: **Run description:** PyTerrier/Terrier DPH + Bo1 QE 

---
#### uogTrDCPpmp 
[**`Results`**](./results.md#uogtrdcppmp) | [**`Participants`**](./participants.md#uogtr) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrDCPpmp.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrDCPpmp) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrDCPpmp.pdf) 

- :material-rename: **Run ID:** uogTrDCPpmp 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `1947a4f7ccdf0ab34d1d6b4c307d75a7` 
- :material-text: **Run description:** PyTerrier/ColBERT dense retrieval plus some ColBERT PRF on the passage corpus then converted into document ranking run using max passage  

---
#### uogTrDDQt5 
[**`Results`**](./results.md#uogtrddqt5) | [**`Participants`**](./participants.md#uogtr) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrDDQt5.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrDDQt5) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrDDQt5.pdf) 

- :material-rename: **Run ID:** uogTrDDQt5 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `72d3762b12cf5e456deb896aa2ab66e2` 
- :material-text: **Run description:** PyTerrier/Terrier DPH + Bo1QE monoT5 

---
#### uogTrDot5pmp 
[**`Results`**](./results.md#uogtrdot5pmp) | [**`Participants`**](./participants.md#uogtr) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrDot5pmp.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrDot5pmp) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrDot5pmp.pdf) 

- :material-rename: **Run ID:** uogTrDot5pmp 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `d00a5728b521ff77afbadc8e220491f1` 
- :material-text: **Run description:** PyTerrier Combination of sparse (Terrier DPH + Bo1QE) and dense (ColBERT & ColBERT PRF) runs re-ranked by monoT5 converted to document run with maxpassage 

---
#### uogTrPC 
[**`Results`**](./results.md#uogtrpc) | [**`Participants`**](./participants.md#uogtr) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrPC.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrPC) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.uogTrPC) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrPC.pdf) 

- :material-rename: **Run ID:** uogTrPC 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `59f574f140161b1090579e594847b209` 
- :material-text: **Run description:** PyTerrier/ColBERT dense retrieval on the passage corpus  

---
#### uogTrPCP 
[**`Results`**](./results.md#uogtrpcp) | [**`Participants`**](./participants.md#uogtr) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrPCP.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrPCP) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.uogTrPCP) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrPCP.pdf) 

- :material-rename: **Run ID:** uogTrPCP 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `9c4b68c6d5ac2fdd5f7bf88dc72ba691` 
- :material-text: **Run description:** PyTerrier/ColBERT dense retrieval with some ColBERT PRF to re-rank on the passage corpus  

---
#### uogTrPot5 
[**`Results`**](./results.md#uogtrpot5) | [**`Participants`**](./participants.md#uogtr) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.uogTrPot5.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.uogTrPot5) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.uogTrPot5) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/uogTrPot5.pdf) 

- :material-rename: **Run ID:** uogTrPot5 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/10/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `37162adf2ca4a28b0b5d54cf435c14cb` 
- :material-text: **Run description:** PyTerrier Combination of sparse (Terrier DPH + Bo1QE) and dense (ColBERT & ColBERT PRF) runs re-ranked by monoT5 

---
#### watdfd 
[**`Results`**](./results.md#watdfd) | [**`Participants`**](./participants.md#waterloo_cormack) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.watdfd.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.watdfd) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/watdfd.pdf) 

- :material-rename: **Run ID:** watdfd 
- :fontawesome-solid-user-group: **Participant:** Waterloo_Cormack 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `a7e95247ca5c89288d8f81121f681b9c` 
- :material-text: **Run description:** Google SERP as training for logistic regression, document priority scoring. 

---
#### watdff 
[**`Results`**](./results.md#watdff) | [**`Participants`**](./participants.md#waterloo_cormack) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.watdff.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.watdff) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/watdff.pdf) 

- :material-rename: **Run ID:** watdff 
- :fontawesome-solid-user-group: **Participant:** Waterloo_Cormack 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `874740d4a33ba224a7a936d53c32b394` 
- :material-text: **Run description:** Google SERP as training for logistic regression, document/passage fusion scoring. 

---
#### watdfp 
[**`Results`**](./results.md#watdfp) | [**`Participants`**](./participants.md#waterloo_cormack) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.watdfp.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.watdfp) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/watdfp.pdf) 

- :material-rename: **Run ID:** watdfp 
- :fontawesome-solid-user-group: **Participant:** Waterloo_Cormack 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `136d5b2d6209a2433a83089945a13417` 
- :material-text: **Run description:** Google SERP as training for logistic regression, document priority scoring. 

---
#### watdrd 
[**`Results`**](./results.md#watdrd) | [**`Participants`**](./participants.md#waterloo_cormack) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.watdrd.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.watdrd) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/watdrd.pdf) 

- :material-rename: **Run ID:** watdrd 
- :fontawesome-solid-user-group: **Participant:** Waterloo_Cormack 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `cfbaca66992049638b83cc41dec49574` 
- :material-text: **Run description:** Google SERP as training for logistic regression, document-only scoring. 

---
#### watdrf 
[**`Results`**](./results.md#watdrf) | [**`Participants`**](./participants.md#waterloo_cormack) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.watdrf.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.watdrf) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/watdrf.pdf) 

- :material-rename: **Run ID:** watdrf 
- :fontawesome-solid-user-group: **Participant:** Waterloo_Cormack 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `4ccfc61de8aadad22d70dd7c4ffcd227` 
- :material-text: **Run description:** Google SERP as training for logistic regression, document/passage fusion scoring. 

---
#### watdrp 
[**`Results`**](./results.md#watdrp) | [**`Participants`**](./participants.md#waterloo_cormack) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.watdrp.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.watdrp) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/watdrp.pdf) 

- :material-rename: **Run ID:** watdrp 
- :fontawesome-solid-user-group: **Participant:** Waterloo_Cormack 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `f1a7324717fc45c16d8f4f0d84cc4140` 
- :material-text: **Run description:** Google SERP as training for logistic regression, passage-priority scoring. 

---
#### watpfd 
[**`Results`**](./results.md#watpfd) | [**`Participants`**](./participants.md#waterloo_cormack) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.watpfd.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.watpfd) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.watpfd) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/watpfd.pdf) 

- :material-rename: **Run ID:** watpfd 
- :fontawesome-solid-user-group: **Participant:** Waterloo_Cormack 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `acf88f72aea2db19df469092699e1d1d` 
- :material-text: **Run description:** Google SERP as training for logistic regression, document-priority scoring. 

---
#### watpff 
[**`Results`**](./results.md#watpff) | [**`Participants`**](./participants.md#waterloo_cormack) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.watpff.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.watpff) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.watpff) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/watpff.pdf) 

- :material-rename: **Run ID:** watpff 
- :fontawesome-solid-user-group: **Participant:** Waterloo_Cormack 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `2196763f588a5f8ebb38de8a37b4ffc3` 
- :material-text: **Run description:** Google SERP as training for logistic regression, document/passage fusion scoring. 

---
#### watpfp 
[**`Results`**](./results.md#watpfp) | [**`Participants`**](./participants.md#waterloo_cormack) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.watpfp.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.watpfp) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.watpfp) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/watpfp.pdf) 

- :material-rename: **Run ID:** watpfp 
- :fontawesome-solid-user-group: **Participant:** Waterloo_Cormack 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `def8908cececcc0632117575e303600b` 
- :material-text: **Run description:** Google SERP as training for logistic regression, passage-priority scoring. 

---
#### watprd 
[**`Results`**](./results.md#watprd) | [**`Participants`**](./participants.md#waterloo_cormack) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.watprd.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.watprd) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.watprd) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/watprd.pdf) 

- :material-rename: **Run ID:** watprd 
- :fontawesome-solid-user-group: **Participant:** Waterloo_Cormack 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `ccb5fb4a10adf5959a5901a2ed9e6be8` 
- :material-text: **Run description:** Google SERP as training for logistic regression, document-priority scoring. 

---
#### watprf 
[**`Results`**](./results.md#watprf) | [**`Participants`**](./participants.md#waterloo_cormack) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.watprf.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.watprf) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.watprf) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/watprf.pdf) 

- :material-rename: **Run ID:** watprf 
- :fontawesome-solid-user-group: **Participant:** Waterloo_Cormack 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `424b0f3ede7165d42222a224369d9ded` 
- :material-text: **Run description:** Google SERP as training for logistic regression, document/passage fusion scoring. 

---
#### watprp 
[**`Results`**](./results.md#watprp) | [**`Participants`**](./participants.md#waterloo_cormack) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.watprp.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.watprp) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.watprp) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/watprp.pdf) 

- :material-rename: **Run ID:** watprp 
- :fontawesome-solid-user-group: **Participant:** Waterloo_Cormack 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/9/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `f7e6f0c39e213ee1971accf65a289ac4` 
- :material-text: **Run description:** Google SERP as training for logistic regression, passage-only scoring. 

---
#### webis-dl-1 
[**`Results`**](./results.md#webis-dl-1) | [**`Participants`**](./participants.md#webis) | [**`Proceedings`**](./proceedings.md#webis-at-trec-2021-deep-learning-health-misinformation-and-podcasts-tracks) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.webis-dl-1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.webis-dl-1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/webis-dl-1.pdf) 

- :material-rename: **Run ID:** webis-dl-1 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `75909131f332f7034e072ecf2e00575d` 
- :material-text: **Run description:** We calculate 50 traditional features and train a LambdaMART model on those 50 features using this year's MS MARCO training data. The features include 36 query-document features (9 similarities like BM25, TF-IDF, etc. on 4 types of text: title, URL, body, and anchor text extracted from a common crawl snapshot), 8 document features (PageRank, etc), and 6 query features (number of entities in the query, etc). Here we train a model with 5000 trees. 

---
#### webis-dl-2 
[**`Results`**](./results.md#webis-dl-2) | [**`Participants`**](./participants.md#webis) | [**`Proceedings`**](./proceedings.md#webis-at-trec-2021-deep-learning-health-misinformation-and-podcasts-tracks) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.webis-dl-2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.webis-dl-2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/webis-dl-2.pdf) 

- :material-rename: **Run ID:** webis-dl-2 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `b0b229b8dd92307009ca99a5597938f4` 
- :material-text: **Run description:** We calculate 41 traditional features and train a LambdaMART model on those 50 features using this year's MS MARCO training data. The features include 27 query-document features (9 similarities like BM25, TF-IDF, etc. on 3 types of text: title, URL, body), 8 document features (PageRank, etc), and 6 query features (number of entities in the query, etc). Here we train a model with 5000 trees. 

---
#### webis-dl-3 
[**`Results`**](./results.md#webis-dl-3) | [**`Participants`**](./participants.md#webis) | [**`Proceedings`**](./proceedings.md#webis-at-trec-2021-deep-learning-health-misinformation-and-podcasts-tracks) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.webis-dl-3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.webis-dl-3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/webis-dl-3.pdf) 

- :material-rename: **Run ID:** webis-dl-3 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `8b47475818b4a49b664d5a1f44ce67bf` 
- :material-text: **Run description:** We calculate 50 traditional features and train a LambdaMART model on those 50 features using this year's MS MARCO training data. The features include 36 query-document features (9 similarities like BM25, TF-IDF, etc. on 4 types of text: title, URL, body, and anchor text extracted from a common crawl snapshot), 8 document features (PageRank, etc), and 6 query features (number of entities in the query, etc). Here we train a model with 1000 trees. 

---
#### WLUPassage 
[**`Results`**](./results.md#wlupassage) | [**`Participants`**](./participants.md#wlu) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.WLUPassage.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.WLUPassage) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.WLUPassage) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/WLUPassage.pdf) 

- :material-rename: **Run ID:** WLUPassage 
- :fontawesome-solid-user-group: **Participant:** WLU 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/7/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `cf3d9743dbe32cc720fda3e5a113644f` 
- :material-text: **Run description:** The query and passage were truncated to 10 words and 50 words respectively. BERT (base model, uncased) embeddings for both were created. These were inputs into a neural network with three sections. 1. Each input was passed to LSTM layers, convolutional and average pooling layers, and regular densely connected layers. Then, they were multiplied together and passed through more of those layers. 2. The passage embedding input was subtracted from the query embedding input. The resulting tensor was passed to LSTM layers, convolutional and average pooling layers, and regular densely connected layers. 3. A new tensor was created by averaging all BERT embeddings in the passage. The query was also split into individual words. The cosine similarity between the average tensor and each word tensor was taken and then each was passed to densely connected layers. The average of the cosine similarities was taken, and the max. similarity was calculated as well. These values were added together. The tensors at the end of these three sections were all added together into one tensor, passed through more densely connected layers, and the final output was a score between 0 and 1.  

---
#### WLUPassage1 
[**`Results`**](./results.md#wlupassage1) | [**`Participants`**](./participants.md#wlu) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.WLUPassage1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.WLUPassage1) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.WLUPassage1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/WLUPassage1.pdf) 

- :material-rename: **Run ID:** WLUPassage1 
- :fontawesome-solid-user-group: **Participant:** WLU 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/7/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `370faf3233f3ac6e3f0d66ec37b65109` 
- :material-text: **Run description:** The query and passage were truncated to 10 words and 50 words respectively. BERT (base model, uncased) embeddings for both were created. These were inputs into a neural network with two sections. 1. Each input was passed to LSTM layers, convolutional and max pooling layers, and regular densely connected layers. Then, they were multiplied together and passed through more of those layers. 2. The passage embedding input was subtracted from the query embedding input. The resulting tensor was passed to LSTM layers, convolutional and max pooling layers, and regular densely connected layers. The tensors at the end of these two sections were all added together into one tensor, passed through more densely connected layers, and the final output was a score between 0 and 1.  

---
#### yorku21_a 
[**`Results`**](./results.md#yorku21_a) | [**`Participants`**](./participants.md#yorku) | [**`Proceedings`**](./proceedings.md#york-university-at-trec-2021-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.yorku21_a.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.yorku21_a) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.yorku21_a) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/yorku21_a.pdf) 

- :material-rename: **Run ID:** yorku21_a 
- :fontawesome-solid-user-group: **Participant:** yorku 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `444c16ae80754346a1727e7370ff9243` 
- :material-text: **Run description:** First, we utilized the pre-trained model msmarco-MiniLM-L-6-v3 to calculate the sentence embeddings in each jsonl file of the passage ranking dataset. Second, we encoded each search query as a sentence embedding and utilized semantic search to calculate its relevance to the sentence embeddings of the entire dataset. This would retrieve the most relevant 100 passages from each jsonl file, instead of selecting 100 passages from the entire dataset. Finally, we utilized two pre-trained cross-coder models: ms-marco-MiniLM-L-12-v2 and ms-marco-MiniLM-L-6-v2 to re-rank the relevant passages retrieved from the second step. The results of the above three rankings were voted, and the top 100 most relevant passages for each query were selected as the final result. 

---
#### yorku21_b 
[**`Results`**](./results.md#yorku21_b) | [**`Participants`**](./participants.md#yorku) | [**`Proceedings`**](./proceedings.md#york-university-at-trec-2021-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.yorku21_b.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.yorku21_b) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.yorku21_b) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/yorku21_b.pdf) 

- :material-rename: **Run ID:** yorku21_b 
- :fontawesome-solid-user-group: **Participant:** yorku 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `44132faafb55dc01f9614155f1445647` 
- :material-text: **Run description:** First, we utilized the pre-trained model msmarco-MiniLM-L-6-v3 to calculate the sentence embeddings in each jsonl file of the passage ranking dataset. Second, we encoded each search query as a sentence embedding and utilized semantic search to calculate its relevance to the sentence embeddings of the entire dataset. This would retrieve the most relevant 100 passages from each jsonl file, instead of selecting 100 passages from the entire dataset. 

---
#### yorku21_c 
[**`Results`**](./results.md#yorku21_c) | [**`Participants`**](./participants.md#yorku) | [**`Proceedings`**](./proceedings.md#york-university-at-trec-2021-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec30/deep/input.yorku21_c.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec30/deep/summary.treceval.yorku21_c) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec30/deep/summary.passages-eval.yorku21_c) | [**`Appendix`**](https://trec.nist.gov/pubs/trec30/appendices/deep/yorku21_c.pdf) 

- :material-rename: **Run ID:** yorku21_c 
- :fontawesome-solid-user-group: **Participant:** yorku 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2021 
- :material-upload: **Submission:** 8/8/2021 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `4d459f1027098b55992e185aef81f311` 
- :material-text: **Run description:** First, we utilized the pre-trained model msmarco-MiniLM-L-6-v3 to calculate the sentence embeddings in each jsonl file of the passage ranking dataset. Second, we encoded each search query as a sentence embedding and utilized semantic search to calculate its relevance to the sentence embeddings of the entire dataset. This would retrieve the most relevant 100 passages from each jsonl file, instead of selecting 100 passages from the entire dataset. Finally, we utilized the pre-trained cross-coder models: ms-marco-MiniLM-L-6-v2 to re-rank the relevant passages retrieved from the second step. And the top 100 most relevant passages for each query were selected as the final result. 

---
