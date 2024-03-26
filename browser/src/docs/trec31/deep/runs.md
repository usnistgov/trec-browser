# Runs - Deep Learning 2022 

#### 2systems 
[**`Results`**](./results.md#2systems) | [**`Participants`**](./participants.md#uga) | [**`Proceedings`**](./proceedings.md#universite-grenoble-alpes-lig-at-trec-deep-learning-track-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.2systems.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.2systems.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.2systems.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/2systems.pdf) 

- :material-rename: **Run ID:** 2systems 
- :fontawesome-solid-user-group: **Participant:** UGA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/6/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `980c4233cc8ce21beb24720eaf13ec79` 
- :material-text: **Run description:** Combination of 2 systems (combined by RR-based fusion): - BM25 expanded by DocT5query and RM3, reranked by T5 (top 100 documents) - Unicol reranked first by MiniLM-L12 (top 100 documents), then by T5 (top 10 documents) 

---
#### 4systems 
[**`Results`**](./results.md#4systems) | [**`Participants`**](./participants.md#uga) | [**`Proceedings`**](./proceedings.md#universite-grenoble-alpes-lig-at-trec-deep-learning-track-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.4systems.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.4systems.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.4systems.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/4systems.pdf) 

- :material-rename: **Run ID:** 4systems 
- :fontawesome-solid-user-group: **Participant:** UGA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/6/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `09ea1800c8c5d9acc31945f0d272275b` 
- :material-text: **Run description:** Combination of 4 systems using RR-based fusion: - Unicoil - Unicoil reranked by MiniLM-L12 [top 100 documents] - (BM25 with docT5query and RM3 expansion) reranked by T5 [top 100 documents]  + BM25 with GAT and Colbert reranking 

---
#### 6systems 
[**`Results`**](./results.md#6systems) | [**`Participants`**](./participants.md#uga) | [**`Proceedings`**](./proceedings.md#universite-grenoble-alpes-lig-at-trec-deep-learning-track-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.6systems.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.6systems.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.6systems.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/6systems.pdf) 

- :material-rename: **Run ID:** 6systems 
- :fontawesome-solid-user-group: **Participant:** UGA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/6/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `bdaf925b3cd6fcb13ca90a0b709bc26f` 
- :material-text: **Run description:** Combination of 6 sytems, combined using RR-based fusion: - Unicoil (pre-trained model) - (BM25 with docT5query and RM3 expansions) reranked by T5 (top 100 document were reranked) - Unicoil pre-trained model reranked by MiniLM-L12 model (top 100 documents were reranked)  - BM25 with GAT and Colbert reranking (top 100 documents were reranked) - Colbert pre-trained model reranked by T5 (top 100 document were reranked) - (DPH stemmed + BM25) models combined by RR-based fusion and reranked by T5 (top 100 documents were reranked) 

---
#### c47 
[**`Results`**](./results.md#c47) | [**`Participants`**](./participants.md#uga) | [**`Proceedings`**](./proceedings.md#universite-grenoble-alpes-lig-at-trec-deep-learning-track-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.c47.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.c47.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.c47.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/c47.pdf) 

- :material-rename: **Run ID:** c47 
- :fontawesome-solid-user-group: **Participant:** UGA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/6/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `bda42c82fd6eb9ace935ca734d6952d5` 
- :material-text: **Run description:** Combination of 4 systems using RR-based fusion: - Unicoil  - Unicoil reranked by MiniLM-L12 [top 100 documents] and then by T5 [top 10 documents] - (DPH stemmed + BM25) combined by RR-based fusion and reranked by T5 [top 100 documents reranked]  - (BM25 with docT5query and BM3 expansion) reranked by T5 [top 100 documents]  

---
#### ceqe_custom_rerank 
[**`Results`**](./results.md#ceqe_custom_rerank) | [**`Participants`**](./participants.md#certh_iti_m4d) | [**`Proceedings`**](./proceedings.md#m4d-mklab-iti-certh-participation-in-trec-deep-learning-track-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.ceqe_custom_rerank.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.ceqe_custom_rerank) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/ceqe_custom_rerank.pdf) 

- :material-rename: **Run ID:** ceqe_custom_rerank 
- :fontawesome-solid-user-group: **Participant:** CERTH_ITI_M4D 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/7/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `c513c0efd44300ce247cb298cc810539` 
- :material-text: **Run description:** A query expansion pipeline with a reranking step. The query expansion is expanding on the approach of the paper "CEQE: Contextualized Embeddings for Query Expansion" by Naseri et al. CEQE preforms query expansion based contextualized embeddings (BERT). Our approach examines some minor modifications on the original approach. The reranking step was performed using a pretrained ColBERT model.  pipeline: 1. first stage retrieval (bm25) 2. query expansion (CEQE) 3. second stage retrieval on expanded queries (bm25) 4. rerank (colbert) 

---
#### cip_f1 
[**`Results`**](./results.md#cip_f1) | [**`Participants`**](./participants.md#cip) | [**`Proceedings`**](./proceedings.md#cip-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.cip_f1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_f1.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_f1.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/cip_f1.pdf) 

- :material-rename: **Run ID:** cip_f1 
- :fontawesome-solid-user-group: **Participant:** CIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `a7cf2dfee12a284948a10b8ee3d988a4` 
- :material-text: **Run description:** To produce this run, a standard dense retrieval model (based on bert-uncased-base) was fine-tuned on MS MARCO_v1 and MS MARCO_v2 in turn with a local ranking alignment mechanism. For training data, the negative examples were sample from the top retrieval result of model before fine-tuning and a noise queries (such as injected misspellings, swapped synonyms) set was generated. The training loss consists of two parts, cross-entropy loss for queries and passages and Kullback-Leibler divergence loss for queries retrieval list and noise queries retrieval list. After training on MS MARCO_v1, RoDR_v1 was obtained. And the docT5query was used to match with dense model results. 

---
#### cip_f1_r 
[**`Results`**](./results.md#cip_f1_r) | [**`Participants`**](./participants.md#cip) | [**`Proceedings`**](./proceedings.md#cip-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.cip_f1_r.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_f1_r.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_f1_r.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/cip_f1_r.pdf) 

- :material-rename: **Run ID:** cip_f1_r 
- :fontawesome-solid-user-group: **Participant:** CIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `9fb69bc35f3aa17711703c14b80fa73b` 
- :material-text: **Run description:** To produce this run, the dense retrieval model TAS-B BERT_Dot was fine-tuned on MS MARCO_v1 and MS MARCO_v2 in turn with a local ranking alignment mechanism. For training data, the negative examples were sample from the top retrieval result of model before fine-tuning and a noise queries (such as injected misspellings, swapped synonyms) set was generated. The training loss consists of two parts, cross-entropy loss for queries and passages and Kullback-Leibler divergence loss for queries retrieval list and noise queries retrieval list. And the docT5query was used to match with dense model results. The model we used to get the run cip_r3 of re-rank subtask was used. 

---
#### cip_f2 
[**`Results`**](./results.md#cip_f2) | [**`Participants`**](./participants.md#cip) | [**`Proceedings`**](./proceedings.md#cip-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.cip_f2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_f2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_f2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/cip_f2.pdf) 

- :material-rename: **Run ID:** cip_f2 
- :fontawesome-solid-user-group: **Participant:** CIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `a72f1417c57508d682b0f7e89a578fc8` 
- :material-text: **Run description:** To produce this run, the dense retrieval model TAS-B BERT_Dot was fine-tuned on MS MARCO_v1 and MS MARCO_v2 in turn with a local ranking alignment mechanism. For training data, the negative examples were sample from the top retrieval result of model before fine-tuning and a noise queries (such as injected misspellings, swapped synonyms) set was generated. The training loss consists of two parts, cross-entropy loss for queries and passages and Kullback-Leibler divergence loss for queries retrieval list and noise queries retrieval list. And the docT5query was used to match with dense model results. 

---
#### cip_f2_r 
[**`Results`**](./results.md#cip_f2_r) | [**`Participants`**](./participants.md#cip) | [**`Proceedings`**](./proceedings.md#cip-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.cip_f2_r.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_f2_r.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_f2_r.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/cip_f2_r.pdf) 

- :material-rename: **Run ID:** cip_f2_r 
- :fontawesome-solid-user-group: **Participant:** CIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `ffd84420f4cd4d0dea98435a4fb0d3bb` 
- :material-text: **Run description:** To produce this run, a standard dense retrieval model (based on bert-uncased-base) was fine-tuned on MS MARCO_v1 and MS MARCO_v2 in turn with a local ranking alignment mechanism. For training data, the negative examples were sample from the top retrieval result of model before fine-tuning and a noise queries (such as injected misspellings, swapped synonyms) set was generated. The training loss consists of two parts, cross-entropy loss for queries and passages and Kullback-Leibler divergence loss for queries retrieval list and noise queries retrieval list. After training on MS MARCO_v1, RoDR_v1 was obtained. And the docT5query was used to match with dense model results. The model we used to get the run cip_r1 of re-rank subtask was used. 

---
#### cip_f3 
[**`Results`**](./results.md#cip_f3) | [**`Participants`**](./participants.md#cip) | [**`Proceedings`**](./proceedings.md#cip-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.cip_f3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_f3.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_f3.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/cip_f3.pdf) 

- :material-rename: **Run ID:** cip_f3 
- :fontawesome-solid-user-group: **Participant:** CIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `52a7c24cb9bf687a57601db4f0def564` 
- :material-text: **Run description:** To produce this run, the dense retrieval model PAIR was fine-tuned on MS MARCO_v2 with a local ranking alignment mechanism. For training data, the negative examples were sample from the top retrieval result of RoDR_v1 and a noise queries (such as injected misspellings, swapped synonyms) set was generated. The training loss consists of two parts, cross-entropy loss for queries and passages and Kullback-Leibler divergence loss for queries retrieval list and noise queries retrieval list. And the docT5query was used to match with dense model results. 

---
#### cip_f3_r 
[**`Results`**](./results.md#cip_f3_r) | [**`Participants`**](./participants.md#cip) | [**`Proceedings`**](./proceedings.md#cip-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.cip_f3_r.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_f3_r.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_f3_r.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/cip_f3_r.pdf) 

- :material-rename: **Run ID:** cip_f3_r 
- :fontawesome-solid-user-group: **Participant:** CIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `a52021a0ce28199f9b58dfcd96214f1b` 
- :material-text: **Run description:** To produce this run, the dense retrieval model PAIR was fine-tuned on MS MARCO_v2 with a local ranking alignment mechanism. For training data, the negative examples were sample from the top retrieval result of RoDR_v1 and a noise queries (such as injected misspellings, swapped synonyms) set was generated. The training loss consists of two parts, cross-entropy loss for queries and passages and Kullback-Leibler divergence loss for queries retrieval list and noise queries retrieval list. And the docT5query was used to match with dense model results. The model we used to get the run cip_r2 of re-rank subtask was used. 

---
#### cip_r1 
[**`Results`**](./results.md#cip_r1) | [**`Participants`**](./participants.md#cip) | [**`Proceedings`**](./proceedings.md#cip-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.cip_r1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_r1.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_r1.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/cip_r1.pdf) 

- :material-rename: **Run ID:** cip_r1 
- :fontawesome-solid-user-group: **Participant:** CIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `0ca5e6ff9fbbfa3593b0fbdd2367e2c2` 
- :material-text: **Run description:** To produce this run, a model (based on bert-uncased-large) was fine-tuned on MS MARCO_v2 in turn with the initial top100 ranking files. For training data, the negative examples were sample from the top retrieval result of model before fine-tuning. The training loss is Localized Contrastive Estimation (LCE). And the docT5query was used to match with model results. 

---
#### cip_r2 
[**`Results`**](./results.md#cip_r2) | [**`Participants`**](./participants.md#cip) | [**`Proceedings`**](./proceedings.md#cip-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.cip_r2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_r2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_r2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/cip_r2.pdf) 

- :material-rename: **Run ID:** cip_r2 
- :fontawesome-solid-user-group: **Participant:** CIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `d496c58af4af05ea5a9fd6aa1f2cade7` 
- :material-text: **Run description:** To produce this run, a model (based on bert-uncased-large) was fine-tuned on MS MARCO_v1 in turn with the initial top1000 ranking files. For training data, the negative examples were sample from the top retrieval result of model before fine-tuning. The training loss is hinge loss. After training on MS MARCO_v1, HingeReranker was obtained.  

---
#### cip_r3 
[**`Results`**](./results.md#cip_r3) | [**`Participants`**](./participants.md#cip) | [**`Proceedings`**](./proceedings.md#cip-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.cip_r3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_r3.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.cip_r3.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/cip_r3.pdf) 

- :material-rename: **Run ID:** cip_r3 
- :fontawesome-solid-user-group: **Participant:** CIP 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `7c3d885a290d918ed0f30eea0f7493ee` 
- :material-text: **Run description:** To produce this run, a model (based on HingeReranker) was fine-tuned on MS MARCO_v2 in turn with the initial top100 ranking files. For training data, the negative examples were sample from the top retrieval result of model before fine-tuning. The training loss consists of two parts, hinge loss for queries and passages of MS MARCO_v1 and Localized Contrastive Estimation loss for queries and passages of MS MARCO_v2. And the docT5query was used to match with model results. 

---
#### doc1 
[**`Results`**](./results.md#doc1) | [**`Participants`**](./participants.md#ali) | [**`Proceedings`**](./proceedings.md#hybrid-retrieval-and-multi-stage-ranking-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.doc1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.doc1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/doc1.pdf) 

- :material-rename: **Run ID:** doc1 
- :fontawesome-solid-user-group: **Participant:** Ali 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `eec8e094e65ecd910ead7d6b75d5deb7` 
- :material-text: **Run description:** rom + splade + reranker 

---
#### doc2 
[**`Results`**](./results.md#doc2) | [**`Participants`**](./participants.md#ali) | [**`Proceedings`**](./proceedings.md#hybrid-retrieval-and-multi-stage-ranking-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.doc2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.doc2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/doc2.pdf) 

- :material-rename: **Run ID:** doc2 
- :fontawesome-solid-user-group: **Participant:** Ali 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `cfacee0200e9a6ff5d7e991eec90e028` 
- :material-text: **Run description:** rom + splade + reranker 

---
#### doc3 
[**`Results`**](./results.md#doc3) | [**`Participants`**](./participants.md#ali) | [**`Proceedings`**](./proceedings.md#hybrid-retrieval-and-multi-stage-ranking-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.doc3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.doc3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/doc3.pdf) 

- :material-rename: **Run ID:** doc3 
- :fontawesome-solid-user-group: **Participant:** Ali 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `fbcfcec20ad5dfa88cdfb1e0fb4a116f` 
- :material-text: **Run description:** rom + splade + reranker 

---
#### f_sum_mdt5 
[**`Results`**](./results.md#f_sum_mdt5) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.f_sum_mdt5.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.f_sum_mdt5.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.f_sum_mdt5.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/f_sum_mdt5.pdf) 

- :material-rename: **Run ID:** f_sum_mdt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/11/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `8c5a3aba78ff38e612361e24b5a4cd63` 
- :material-text: **Run description:** f_sum reranked by MSv1 monoT5-3B-10K then MSv1 duoT5-3B-10K  

---
#### fused_2runs 
[**`Results`**](./results.md#fused_2runs) | [**`Participants`**](./participants.md#uga) | [**`Proceedings`**](./proceedings.md#universite-grenoble-alpes-lig-at-trec-deep-learning-track-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.fused_2runs.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.fused_2runs.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.fused_2runs.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/fused_2runs.pdf) 

- :material-rename: **Run ID:** fused_2runs 
- :fontawesome-solid-user-group: **Participant:** UGA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/5/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `5b3756bdde237f836981dc08e1788b09` 
- :material-text: **Run description:** A reciprocal rank fusion of the run reranked by 3 systems (dense retrieval with ms-marco-MiniLM, T5 models. 

---
#### fused_3runs 
[**`Results`**](./results.md#fused_3runs) | [**`Participants`**](./participants.md#uga) | [**`Proceedings`**](./proceedings.md#universite-grenoble-alpes-lig-at-trec-deep-learning-track-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.fused_3runs.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.fused_3runs.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.fused_3runs.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/fused_3runs.pdf) 

- :material-rename: **Run ID:** fused_3runs 
- :fontawesome-solid-user-group: **Participant:** UGA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/5/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `b0591e56ff093714b38e1c6547cd1508` 
- :material-text: **Run description:** A reciprocal rank fusion of the run reranked by 3 systems (dense retrieval with ms-marco-MiniLM, T5 and BERT models. 

---
#### graph_colbert 
[**`Results`**](./results.md#graph_colbert) | [**`Participants`**](./participants.md#uga) | [**`Proceedings`**](./proceedings.md#universite-grenoble-alpes-lig-at-trec-deep-learning-track-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.graph_colbert.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.graph_colbert.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.graph_colbert.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/graph_colbert.pdf) 

- :material-rename: **Run ID:** graph_colbert 
- :fontawesome-solid-user-group: **Participant:** UGA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/6/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `75cb8459910fba7a1c3e2c3ab82d22c1` 
- :material-text: **Run description:** BM25 baseline with reranking applied. Reranking is done using a combination of Graph Attention Network which uses information about full document and Colbert.  

---
#### hierarchcal_combination 
[**`Results`**](./results.md#hierarchcal_combination) | [**`Participants`**](./participants.md#uga) | [**`Proceedings`**](./proceedings.md#universite-grenoble-alpes-lig-at-trec-deep-learning-track-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.hierarchcal_combination.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.hierarchcal_combination.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.hierarchcal_combination.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/hierarchcal_combination.pdf) 

- :material-rename: **Run ID:** hierarchcal_combination 
- :fontawesome-solid-user-group: **Participant:** UGA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/6/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `e80ca582976a82964a014f3fc4bd862b` 
- :material-text: **Run description:** Hierarchical combination of 3 models (combined using RR-based fusion): [Colbert + Unicoil + BM25 with docT5query and RM3 expansions] combined using RR-based fusion, reranked by BERT with top 10 documents reranked,  Unicoil reranked by MiniLM-L12 model with top 100 documents reranked, and BM25 with reranking using GAT and Colbert with top 100 documents reranked 

---
#### hierarchical_2runs 
[**`Results`**](./results.md#hierarchical_2runs) | [**`Participants`**](./participants.md#uga) | [**`Proceedings`**](./proceedings.md#universite-grenoble-alpes-lig-at-trec-deep-learning-track-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.hierarchical_2runs.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.hierarchical_2runs.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.hierarchical_2runs.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/hierarchical_2runs.pdf) 

- :material-rename: **Run ID:** hierarchical_2runs 
- :fontawesome-solid-user-group: **Participant:** UGA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/5/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `e782e0a1023ecc90bc071a1e67a6f647` 
- :material-text: **Run description:** Two stage reranking. First all documents were reranked by a dense retrieval   ms-marco-MiniLM model, then top 10 documents were reranked by T5 model. 

---
#### IELab-3MP-DI 
[**`Results`**](./results.md#ielab-3mp-di) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.IELab-3MP-DI.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.IELab-3MP-DI.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.IELab-3MP-DI.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/IELab-3MP-DI.pdf) 

- :material-rename: **Run ID:** IELab-3MP-DI 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `deb4447c2ba09627d8a61a1cc70145ff` 
- :material-text: **Run description:** This is a DeepImpact run, with the model trained on Marco V1 passages. 

---
#### IELab-3MP-DT5 
[**`Results`**](./results.md#ielab-3mp-dt5) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.IELab-3MP-DT5.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.IELab-3MP-DT5.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.IELab-3MP-DT5.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/IELab-3MP-DT5.pdf) 

- :material-rename: **Run ID:** IELab-3MP-DT5 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `a1ec3c9e9cc04d9aab477fb477e84d14` 
- :material-text: **Run description:** This is a DocT5Query expanded corpus with BM25 ranking baseline using PISA from an Anserini index. 

---
#### IELab-3MP-RBC 
[**`Results`**](./results.md#ielab-3mp-rbc) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.IELab-3MP-RBC.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.IELab-3MP-RBC.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.IELab-3MP-RBC.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/IELab-3MP-RBC.pdf) 

- :material-rename: **Run ID:** IELab-3MP-RBC 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `ba8eb0fd46c3b49e4dcdebb81a7dfb2a` 
- :material-text: **Run description:** This is an RBC fusion of (1) BM25 run on the augmented passage collection; (2) a DocT5Query expanded augmented passage collection; (3) a v1-trained DeepImpact run; and (4) a v2-trained uniCOIL-TILDE run. 

---
#### IELab-3MP-UT 
[**`Results`**](./results.md#ielab-3mp-ut) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.IELab-3MP-UT.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.IELab-3MP-UT.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.IELab-3MP-UT.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/IELab-3MP-UT.pdf) 

- :material-rename: **Run ID:** IELab-3MP-UT 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `9dc15dc14eb135842bc32d9342834eb9` 
- :material-text: **Run description:** This is a uniCOIL-TILDE run trained on V1 passages 

---
#### Infosense-1 
[**`Results`**](./results.md#infosense-1) | [**`Participants`**](./participants.md#infosense) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.Infosense-1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.Infosense-1.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.Infosense-1.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/Infosense-1.pdf) 

- :material-rename: **Run ID:** Infosense-1 
- :fontawesome-solid-user-group: **Participant:** InfoSense 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `391c6014e2e48da6d3513e17b056ae62` 
- :material-text: **Run description:** We classify the queries into different types (what, number, how, when, where, etc). Based on different query type, we fine-tuned the monoBERT with the corresponding training queries, and then do the reranking using the corresponding rankers. 

---
#### Infosense-2 
[**`Results`**](./results.md#infosense-2) | [**`Participants`**](./participants.md#infosense) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.Infosense-2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.Infosense-2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.Infosense-2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/Infosense-2.pdf) 

- :material-rename: **Run ID:** Infosense-2 
- :fontawesome-solid-user-group: **Participant:** InfoSense 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `b5e5e7afb09f95a161c53a04960b482c` 
- :material-text: **Run description:** We classify the queries into different types (what, number, how, when, where, etc). Based on different query type, we fine-tuned the monoBERT with the corresponding training queries, and then do the reranking using the corresponding rankers. 

---
#### NLE_ENSEMBLE_CONDORCE_doc 
[**`Results`**](./results.md#nle_ensemble_condorce_doc) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.NLE_ENSEMBLE_CONDORCE_doc.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_ENSEMBLE_CONDORCE_doc) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/NLE_ENSEMBLE_CONDORCE_doc.pdf) 

- :material-rename: **Run ID:** NLE_ENSEMBLE_CONDORCE_doc 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `083b9b668b65822cf597e43c67cd6008` 
- :material-text: **Run description:** An ensemble of 6 rerankers using condorcet (using ranx which normalizes the scores) 

---
#### NLE_ENSEMBLE_CONDORCET 
[**`Results`**](./results.md#nle_ensemble_condorcet) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.NLE_ENSEMBLE_CONDORCET.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_ENSEMBLE_CONDORCET.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_ENSEMBLE_CONDORCET.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/NLE_ENSEMBLE_CONDORCET.pdf) 

- :material-rename: **Run ID:** NLE_ENSEMBLE_CONDORCET 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `fd091e6448149d2d24eeaef5a3984a01` 
- :material-text: **Run description:** An ensemble of 6 rerankers using condorcet (using ranx which normalizes the scores) 

---
#### NLE_ENSEMBLE_SUM 
[**`Results`**](./results.md#nle_ensemble_sum) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.NLE_ENSEMBLE_SUM.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_ENSEMBLE_SUM.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_ENSEMBLE_SUM.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/NLE_ENSEMBLE_SUM.pdf) 

- :material-rename: **Run ID:** NLE_ENSEMBLE_SUM 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `83c74e19227c4563183e03133097598a` 
- :material-text: **Run description:** An ensemble of 6 rerankers using condorcet (using ranx which normalizes the scores) 

---
#### NLE_ENSEMBLE_SUM_doc 
[**`Results`**](./results.md#nle_ensemble_sum_doc) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.NLE_ENSEMBLE_SUM_doc.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_ENSEMBLE_SUM_doc) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/NLE_ENSEMBLE_SUM_doc.pdf) 

- :material-rename: **Run ID:** NLE_ENSEMBLE_SUM_doc 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `daa4395b8ef6dc45ce34d0547b70006d` 
- :material-text: **Run description:** An ensemble of 6 rerankers using sum (using ranx which normalizes the scores) 

---
#### NLE_SPLADE_CBERT_DT5_RR 
[**`Results`**](./results.md#nle_splade_cbert_dt5_rr) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.NLE_SPLADE_CBERT_DT5_RR.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_SPLADE_CBERT_DT5_RR.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_SPLADE_CBERT_DT5_RR.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/NLE_SPLADE_CBERT_DT5_RR.pdf) 

- :material-rename: **Run ID:** NLE_SPLADE_CBERT_DT5_RR 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `c8133224e6e2485673b6a2dcab394b54` 
- :material-text: **Run description:** Uses an ensemble of SPLADE models and ColBERTv2 and DocT5 as first stage ranker. Then reranked by 6 different rerankers based on different pretrained language models (Deberta Deberta v2 xxlarge, Deberta-v3 large, Electra-large, T0pp, Albert-v2-xxlarge,Roberta-Large). Finally the rerankers and the first stage ranker are ensembled using a simple sum on normalized scores (max-min normalization). 

---
#### NLE_SPLADE_CBERT_DT5_RR_D 
[**`Results`**](./results.md#nle_splade_cbert_dt5_rr_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.NLE_SPLADE_CBERT_DT5_RR_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_SPLADE_CBERT_DT5_RR_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/NLE_SPLADE_CBERT_DT5_RR_D.pdf) 

- :material-rename: **Run ID:** NLE_SPLADE_CBERT_DT5_RR_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `48a3ac924d50441a2be306dd72dfea63` 
- :material-text: **Run description:** Uses an ensemble of SPLADE models and ColBERTv2 and DocT5 as first stage ranker. Then reranked by 6 different rerankers based on different pretrained language models (Deberta Deberta v2 xxlarge, Deberta-v3 large, Electra-large, T0pp, Albert-v2-xxlarge,Roberta-Large). Finally the rerankers and the first stage ranker are ensembled using a simple sum on normalized scores (max-min normalization). Converted to doc with max_p 

---
#### NLE_SPLADE_CBERT_RR 
[**`Results`**](./results.md#nle_splade_cbert_rr) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.NLE_SPLADE_CBERT_RR.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_SPLADE_CBERT_RR.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_SPLADE_CBERT_RR.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/NLE_SPLADE_CBERT_RR.pdf) 

- :material-rename: **Run ID:** NLE_SPLADE_CBERT_RR 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `8585a9dbf2934f43d837f4065565b3c4` 
- :material-text: **Run description:** Uses an ensemble of SPLADE models adn ColBERTv2 as first stage ranker. Then reranked by 6 different rerankers based on different pretrained language models (Deberta Deberta v2 xxlarge, Deberta-v3 large, Electra-large, T0pp, Albert-v2-xxlarge,Roberta-Large). Finally the rerankers and the first stage ranker are ensembled using a simple sum on normalized scores (max-min normalization). 

---
#### NLE_SPLADE_CBERT_RR_D 
[**`Results`**](./results.md#nle_splade_cbert_rr_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.NLE_SPLADE_CBERT_RR_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_SPLADE_CBERT_RR_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/NLE_SPLADE_CBERT_RR_D.pdf) 

- :material-rename: **Run ID:** NLE_SPLADE_CBERT_RR_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `ead8dbd0f376bae6131d26c60c33500f` 
- :material-text: **Run description:** Uses an ensemble of SPLADE models adn ColBERTv2 as first stage ranker. Then reranked by 6 different rerankers based on different pretrained language models (Deberta Deberta v2 xxlarge, Deberta-v3 large, Electra-large, T0pp, Albert-v2-xxlarge,Roberta-Large). Finally the rerankers and the first stage ranker are ensembled using a simple sum on normalized scores (max-min normalization). Converted to document via max_p 

---
#### NLE_SPLADE_RR 
[**`Results`**](./results.md#nle_splade_rr) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.NLE_SPLADE_RR.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_SPLADE_RR.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_SPLADE_RR.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/NLE_SPLADE_RR.pdf) 

- :material-rename: **Run ID:** NLE_SPLADE_RR 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `fc0b2ef50de5955cca0643bd67f92515` 
- :material-text: **Run description:** Uses an ensemble of SPLADE models as first stage ranker. Then reranked by 6 different rerankers based on different pretrained language models (Deberta Deberta v2 xxlarge, Deberta-v3 large, Electra-large, T0pp, Albert-v2-xxlarge,Roberta-Large). Finally the rerankers and the first stage ranker are ensembled using a simple sum on normalized scores (max-min normalization). 

---
#### NLE_SPLADE_RR_D 
[**`Results`**](./results.md#nle_splade_rr_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.NLE_SPLADE_RR_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_SPLADE_RR_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/NLE_SPLADE_RR_D.pdf) 

- :material-rename: **Run ID:** NLE_SPLADE_RR_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `61c8697c0f27be9a0943f1c579b3607a` 
- :material-text: **Run description:** Uses an ensemble of SPLADE models as first stage ranker. Then reranked by 6 different rerankers based on different pretrained language models (Deberta Deberta v2 xxlarge, Deberta-v3 large, Electra-large, T0pp, Albert-v2-xxlarge,Roberta-Large). Finally the rerankers and the first stage ranker are ensembled using a simple sum on normalized scores (max-min normalization). Converted to document via max_p 

---
#### NLE_T0pp 
[**`Results`**](./results.md#nle_t0pp) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.NLE_T0pp.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_T0pp.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_T0pp.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/NLE_T0pp.pdf) 

- :material-rename: **Run ID:** NLE_T0pp 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `c0bdff0e5c226f148da2d8abc927114b` 
- :material-text: **Run description:** Train a T0pp reranker and rerank the TOP100 

---
#### NLE_T0pp_doc 
[**`Results`**](./results.md#nle_t0pp_doc) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.NLE_T0pp_doc.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.NLE_T0pp_doc) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/NLE_T0pp_doc.pdf) 

- :material-rename: **Run ID:** NLE_T0pp_doc 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `b59f40cdd4d81daba6e76dff3bbf22a5` 
- :material-text: **Run description:** Train a T0pp reranker and rerank the TOP100 of passages then convert to docs 

---
#### p_agg 
[**`Results`**](./results.md#p_agg) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_agg.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_agg.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_agg.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_agg.pdf) 

- :material-rename: **Run ID:** p_agg 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `02edbbe3ca97226d0b2f571593ed817c` 
- :material-text: **Run description:** We train DistilBERT on MSMARCO training queries for 3 epochs and self-mined hard negatives for 2 epochs. 

---
#### p_bm25 
[**`Results`**](./results.md#p_bm25) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_bm25.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_bm25.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_bm25.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_bm25.pdf) 

- :material-rename: **Run ID:** p_bm25 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `b74617018c997060768f12e3886ea4ee` 
- :material-text: **Run description:** original passages, BM25 

---
#### p_bm25rm3 
[**`Results`**](./results.md#p_bm25rm3) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_bm25rm3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_bm25rm3.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_bm25rm3.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_bm25rm3.pdf) 

- :material-rename: **Run ID:** p_bm25rm3 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `b01bd7a5284568598f4c000b2aadd275` 
- :material-text: **Run description:** original passages, BM25 + RM3 

---
#### p_bm25rocchio 
[**`Results`**](./results.md#p_bm25rocchio) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_bm25rocchio.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_bm25rocchio.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_bm25rocchio.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_bm25rocchio.pdf) 

- :material-rename: **Run ID:** p_bm25rocchio 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `7d1e87e767f0873cc7368a5794aea147` 
- :material-text: **Run description:** original passages, BM25 + Rocchio 

---
#### p_d2q_bm25 
[**`Results`**](./results.md#p_d2q_bm25) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_d2q_bm25.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_d2q_bm25.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_d2q_bm25.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_d2q_bm25.pdf) 

- :material-rename: **Run ID:** p_d2q_bm25 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `1cfae30eca47301f32dfa0fec702fed4` 
- :material-text: **Run description:** original passages + doc2query-T5 expansions, BM25 

---
#### p_d2q_bm25rm3 
[**`Results`**](./results.md#p_d2q_bm25rm3) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_d2q_bm25rm3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_d2q_bm25rm3.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_d2q_bm25rm3.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_d2q_bm25rm3.pdf) 

- :material-rename: **Run ID:** p_d2q_bm25rm3 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `735596ada3499cccf5938c7da92fb7f8` 
- :material-text: **Run description:** original passages + doc2query-T5 expansions, BM25 + RM3  

---
#### p_d2q_bm25rocchio 
[**`Results`**](./results.md#p_d2q_bm25rocchio) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_d2q_bm25rocchio.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_d2q_bm25rocchio.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_d2q_bm25rocchio.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_d2q_bm25rocchio.pdf) 

- :material-rename: **Run ID:** p_d2q_bm25rocchio 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `03b13b64ee51382b2dd03fd1840d5aeb` 
- :material-text: **Run description:** original passages + doc2query-T5 expansions, BM25 + Rocchio 

---
#### p_d2q_bm25rocchio_mdt5 
[**`Results`**](./results.md#p_d2q_bm25rocchio_mdt5) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_d2q_bm25rocchio_mdt5.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_d2q_bm25rocchio_mdt5.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_d2q_bm25rocchio_mdt5.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_d2q_bm25rocchio_mdt5.pdf) 

- :material-rename: **Run ID:** p_d2q_bm25rocchio_mdt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/11/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `e8b9d80c74244fc5658d4adf8fbf3275` 
- :material-text: **Run description:** p_d2q_bm25rocchio reranked by MSv1 monoT5-3B-10K then MSv1 duoT5-3B-10K 

---
#### p_d2q_bm25rocchio_mt5 
[**`Results`**](./results.md#p_d2q_bm25rocchio_mt5) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_d2q_bm25rocchio_mt5.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_d2q_bm25rocchio_mt5.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_d2q_bm25rocchio_mt5.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_d2q_bm25rocchio_mt5.pdf) 

- :material-rename: **Run ID:** p_d2q_bm25rocchio_mt5 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/11/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `10985d50ecb6960623d8ed4537505d4b` 
- :material-text: **Run description:** p_d2q_bm25rocchio reranked by MSv1 monoT5-3B-10K 

---
#### p_dhr 
[**`Results`**](./results.md#p_dhr) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_dhr.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_dhr.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_dhr.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_dhr.pdf) 

- :material-rename: **Run ID:** p_dhr 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `e011c11c680700bd3a97708c451a365d` 
- :material-text: **Run description:** We train distilBERT model with 6 epochs on msmarco training queries with BM25 mined negatives and used ColBERT as teacher to further train the model on self-mined negatives. 

---
#### p_tct 
[**`Results`**](./results.md#p_tct) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_tct.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_tct.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_tct.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_tct.pdf) 

- :material-rename: **Run ID:** p_tct 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `546b2ee9a480684deaa300428bbe11fb` 
- :material-text: **Run description:** We use BERT-base as a bi-encoder DPR model and use ColBERT as a teacher model to train it with BM25 and self mined hard negatives. (TCT-ColBERT-HNP) 

---
#### p_unicoil_exp 
[**`Results`**](./results.md#p_unicoil_exp) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_unicoil_exp.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_unicoil_exp.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_unicoil_exp.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_unicoil_exp.pdf) 

- :material-rename: **Run ID:** p_unicoil_exp 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `033f94adb10a5607f24a4376deb669a6` 
- :material-text: **Run description:** uniCOIL w/ d2q-T5 expansions 

---
#### p_unicoil_exp_rocchio 
[**`Results`**](./results.md#p_unicoil_exp_rocchio) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_unicoil_exp_rocchio.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_unicoil_exp_rocchio.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_unicoil_exp_rocchio.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_unicoil_exp_rocchio.pdf) 

- :material-rename: **Run ID:** p_unicoil_exp_rocchio 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `ea9db4e3e6f67f82a3b87ec7f02cff35` 
- :material-text: **Run description:** uniCOIL w/ d2q-T5 expansions + Rocchio 

---
#### p_unicoil_noexp 
[**`Results`**](./results.md#p_unicoil_noexp) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_unicoil_noexp.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_unicoil_noexp.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_unicoil_noexp.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_unicoil_noexp.pdf) 

- :material-rename: **Run ID:** p_unicoil_noexp 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `25326e1d45f5f41aadb8952d499a5a4e` 
- :material-text: **Run description:** uniCOIL no expansion 

---
#### p_unicoil_noexp_rocchio 
[**`Results`**](./results.md#p_unicoil_noexp_rocchio) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.p_unicoil_noexp_rocchio.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.p_unicoil_noexp_rocchio.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.p_unicoil_noexp_rocchio.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/p_unicoil_noexp_rocchio.pdf) 

- :material-rename: **Run ID:** p_unicoil_noexp_rocchio 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `10b385413708511c98f5fe1a8486391c` 
- :material-text: **Run description:** uniCOIL no expansion + Rocchio 

---
#### pass1 
[**`Results`**](./results.md#pass1) | [**`Participants`**](./participants.md#ali) | [**`Proceedings`**](./proceedings.md#hybrid-retrieval-and-multi-stage-ranking-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.pass1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.pass1.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.pass1.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/pass1.pdf) 

- :material-rename: **Run ID:** pass1 
- :fontawesome-solid-user-group: **Participant:** Ali 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `f3a7756b95867d08a52ebb4ae58fa914` 
- :material-text: **Run description:** rom + splade + reranker 

---
#### pass2 
[**`Results`**](./results.md#pass2) | [**`Participants`**](./participants.md#ali) | [**`Proceedings`**](./proceedings.md#hybrid-retrieval-and-multi-stage-ranking-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.pass2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.pass2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.pass2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/pass2.pdf) 

- :material-rename: **Run ID:** pass2 
- :fontawesome-solid-user-group: **Participant:** Ali 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `bc9f0718c62da5d16ac50a5095929bf7` 
- :material-text: **Run description:** rom + splade + reranker 

---
#### pass3 
[**`Results`**](./results.md#pass3) | [**`Participants`**](./participants.md#ali) | [**`Proceedings`**](./proceedings.md#hybrid-retrieval-and-multi-stage-ranking-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.pass3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.pass3.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.pass3.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/pass3.pdf) 

- :material-rename: **Run ID:** pass3 
- :fontawesome-solid-user-group: **Participant:** Ali 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `3b78254fc6ea3351ace3eba105ac87f3` 
- :material-text: **Run description:** rom + splade + reranker 

---
#### paug_bm25 
[**`Results`**](./results.md#paug_bm25) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.paug_bm25.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.paug_bm25.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.paug_bm25.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/paug_bm25.pdf) 

- :material-rename: **Run ID:** paug_bm25 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `79037b8c82f26484722f9161194355f5` 
- :material-text: **Run description:** augmented passages, BM25 

---
#### paug_bm25rm3 
[**`Results`**](./results.md#paug_bm25rm3) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.paug_bm25rm3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.paug_bm25rm3.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.paug_bm25rm3.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/paug_bm25rm3.pdf) 

- :material-rename: **Run ID:** paug_bm25rm3 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `8c786f46e5658fd4763a3dca37bf652e` 
- :material-text: **Run description:** augmented passages, BM25 + RM3 

---
#### paug_bm25rocchio 
[**`Results`**](./results.md#paug_bm25rocchio) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.paug_bm25rocchio.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.paug_bm25rocchio.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.paug_bm25rocchio.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/paug_bm25rocchio.pdf) 

- :material-rename: **Run ID:** paug_bm25rocchio 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `12d32634f6a0746b5de7401ab98c2d67` 
- :material-text: **Run description:** augmented passages, BM25 + Rocchio 

---
#### paug_d2q_bm25 
[**`Results`**](./results.md#paug_d2q_bm25) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.paug_d2q_bm25.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.paug_d2q_bm25.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.paug_d2q_bm25.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/paug_d2q_bm25.pdf) 

- :material-rename: **Run ID:** paug_d2q_bm25 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `4921fc20f7ea1606941aeba4bb693bd8` 
- :material-text: **Run description:** augmented passages + doc2query-T5 expansions, BM25 

---
#### paug_d2q_bm25rm3 
[**`Results`**](./results.md#paug_d2q_bm25rm3) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.paug_d2q_bm25rm3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.paug_d2q_bm25rm3.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.paug_d2q_bm25rm3.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/paug_d2q_bm25rm3.pdf) 

- :material-rename: **Run ID:** paug_d2q_bm25rm3 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `68c255005d07096a748eaaa2ced27153` 
- :material-text: **Run description:** augmented passages + doc2query-T5 expansions, BM25 + RM3 

---
#### paug_d2q_bm25rocchio 
[**`Results`**](./results.md#paug_d2q_bm25rocchio) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.paug_d2q_bm25rocchio.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.paug_d2q_bm25rocchio.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.paug_d2q_bm25rocchio.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/paug_d2q_bm25rocchio.pdf) 

- :material-rename: **Run ID:** paug_d2q_bm25rocchio 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `2b9a722b365a84f60582da9fb0047f06` 
- :material-text: **Run description:** augmented passages + doc2query-T5 expansions, BM25 + Rocchio 

---
#### plm_128 
[**`Results`**](./results.md#plm_128) | [**`Participants`**](./participants.md#uamsterdam) | [**`Proceedings`**](./proceedings.md#efficient-document-representations-for-neural-text-ranking) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.plm_128.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.plm_128) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/plm_128.pdf) 

- :material-rename: **Run ID:** plm_128 
- :fontawesome-solid-user-group: **Participant:** UAmsterdam 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/11/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `418364d1712d35cd3ad371f0893784b1` 
- :material-text: **Run description:** BERT PLM inp. 512 

---
#### plm_512 
[**`Results`**](./results.md#plm_512) | [**`Participants`**](./participants.md#uamsterdam) | [**`Proceedings`**](./proceedings.md#efficient-document-representations-for-neural-text-ranking) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.plm_512.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.plm_512) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/plm_512.pdf) 

- :material-rename: **Run ID:** plm_512 
- :fontawesome-solid-user-group: **Participant:** UAmsterdam 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/11/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `a7501f5b619d82a70f43d9dc8f5b79c0` 
- :material-text: **Run description:** BERT PLM inp. 512 

---
#### plm_64 
[**`Results`**](./results.md#plm_64) | [**`Participants`**](./participants.md#uamsterdam) | [**`Proceedings`**](./proceedings.md#efficient-document-representations-for-neural-text-ranking) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.plm_64.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.plm_64) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/plm_64.pdf) 

- :material-rename: **Run ID:** plm_64 
- :fontawesome-solid-user-group: **Participant:** UAmsterdam 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/11/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `64768c24ffb666a18636be4ca818162d` 
- :material-text: **Run description:** BERT PLM inp. 64 

---
#### rm3_term_filter_rerank 
[**`Results`**](./results.md#rm3_term_filter_rerank) | [**`Participants`**](./participants.md#certh_iti_m4d) | [**`Proceedings`**](./proceedings.md#m4d-mklab-iti-certh-participation-in-trec-deep-learning-track-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.rm3_term_filter_rerank.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.rm3_term_filter_rerank) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/rm3_term_filter_rerank.pdf) 

- :material-rename: **Run ID:** rm3_term_filter_rerank 
- :fontawesome-solid-user-group: **Participant:** CERTH_ITI_M4D 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/5/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `dfa2e83b7878a665bbc7e1c84f74450b` 
- :material-text: **Run description:** A query expansion with an additional term filtering step pipeline with a final reranking step.  Query expansion performed with a tuned RM3 model.  An additional term filtering step was added that removes the expansion terms that are found to be not beneficial. The filtering was performed using the BERT (bert-base-uncased) model trained for predicting the likely benefit of the expansion terms.  The final reranking step was performed using the ColBERT model.  Pipeline: 1. first stage retrieval (bm25) 2. query expansion (tuned rm3) 3. filter the expansion terms (remove the expansion terms that are regarded as bad) + renormalize the term weights 4. second stage retrieval on expanded queries (bm25) 5. rerank (colbert)  

---
#### SPLADE_EFF_V 
[**`Results`**](./results.md#splade_eff_v) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_EFF_V.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_EFF_V.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_EFF_V.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_EFF_V.pdf) 

- :material-rename: **Run ID:** SPLADE_EFF_V 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `f1d8f4f5a95cd77070df3d7f37192c23` 
- :material-text: **Run description:** Baseline run using efficient SPLADE "level V" introduced in https://arxiv.org/pdf/2207.03834.pdf and available at huggingface(https://huggingface.co/naver/efficient-splade-V-large-doc). 

---
#### SPLADE_EFF_V_D 
[**`Results`**](./results.md#splade_eff_v_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_EFF_V_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_EFF_V_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_EFF_V_D.pdf) 

- :material-rename: **Run ID:** SPLADE_EFF_V_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `40326063e0ea4323e355b56765c1b864` 
- :material-text: **Run description:** Baseline run using efficient SPLADE "level V" introduced in https://arxiv.org/pdf/2207.03834.pdf and available at huggingface(https://huggingface.co/naver/efficient-splade-V-large-doc). Converted to doc with max_p 

---
#### SPLADE_EFF_V_RCIO 
[**`Results`**](./results.md#splade_eff_v_rcio) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_EFF_V_RCIO.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_EFF_V_RCIO.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_EFF_V_RCIO.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_EFF_V_RCIO.pdf) 

- :material-rename: **Run ID:** SPLADE_EFF_V_RCIO 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `c56849d439b14fbdfcacebd3258ee40e` 
- :material-text: **Run description:** Baseline run using efficient SPLADE "level V" introduced in https://arxiv.org/pdf/2207.03834.pdf and available at huggingface(https://huggingface.co/naver/efficient-splade-V-large-doc). With Rocchio. 

---
#### SPLADE_EFF_V_RCIO_D 
[**`Results`**](./results.md#splade_eff_v_rcio_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_EFF_V_RCIO_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_EFF_V_RCIO_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_EFF_V_RCIO_D.pdf) 

- :material-rename: **Run ID:** SPLADE_EFF_V_RCIO_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `f3570fbf90a22c3861e0061a25c3daa1` 
- :material-text: **Run description:** Baseline run using efficient SPLADE "level V" introduced in https://arxiv.org/pdf/2207.03834.pdf and available at huggingface(https://huggingface.co/naver/efficient-splade-V-large-doc). With Rocchio. Converted to doc with max_p 

---
#### SPLADE_EFF_VI-BT 
[**`Results`**](./results.md#splade_eff_vi-bt) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_EFF_VI-BT.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_EFF_VI-BT.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_EFF_VI-BT.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_EFF_VI-BT.pdf) 

- :material-rename: **Run ID:** SPLADE_EFF_VI-BT 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `2abde03aede395c79619c0202fb38a86` 
- :material-text: **Run description:** Baseline run using efficient SPLADE "level VI" using BertTiny introduced in https://arxiv.org/pdf/2207.03834.pdf and available at huggingface(https://huggingface.co/naver/efficient-splade-VI-BT-large-doc). 

---
#### SPLADE_EFF_VI-BT_D 
[**`Results`**](./results.md#splade_eff_vi-bt_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_EFF_VI-BT_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_EFF_VI-BT_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_EFF_VI-BT_D.pdf) 

- :material-rename: **Run ID:** SPLADE_EFF_VI-BT_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `cedab6c15e3e723044aad5a27173d34b` 
- :material-text: **Run description:** Baseline run using efficient SPLADE "level VI" using BertTiny introduced in https://arxiv.org/pdf/2207.03834.pdf and available at huggingface(https://huggingface.co/naver/efficient-splade-VI-BT-large-doc). Converted to doc using max_p 

---
#### SPLADE_EFF_VI-BT_RCIO 
[**`Results`**](./results.md#splade_eff_vi-bt_rcio) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_EFF_VI-BT_RCIO.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_EFF_VI-BT_RCIO.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_EFF_VI-BT_RCIO.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_EFF_VI-BT_RCIO.pdf) 

- :material-rename: **Run ID:** SPLADE_EFF_VI-BT_RCIO 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `343eb4fc92ee8618cfd8f163e2f8a799` 
- :material-text: **Run description:** Baseline run using efficient SPLADE "level VI" using BertTiny introduced in https://arxiv.org/pdf/2207.03834.pdf and available at huggingface(https://huggingface.co/naver/efficient-splade-VI-BT-large-doc). With Rocchio 

---
#### SPLADE_EFF_VI-BT_RCIO_D 
[**`Results`**](./results.md#splade_eff_vi-bt_rcio_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_EFF_VI-BT_RCIO_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_EFF_VI-BT_RCIO_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_EFF_VI-BT_RCIO_D.pdf) 

- :material-rename: **Run ID:** SPLADE_EFF_VI-BT_RCIO_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `9fe3ada4e5412c55a817b2a20d45517c` 
- :material-text: **Run description:** Baseline run using efficient SPLADE "level VI" using BertTiny introduced in https://arxiv.org/pdf/2207.03834.pdf and available at huggingface(https://huggingface.co/naver/efficient-splade-VI-BT-large-doc). With Rocchio. Converted to doc using max_p 

---
#### SPLADE_ENSEMBLE_PP 
[**`Results`**](./results.md#splade_ensemble_pp) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_ENSEMBLE_PP.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_ENSEMBLE_PP.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_ENSEMBLE_PP.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_ENSEMBLE_PP.pdf) 

- :material-rename: **Run ID:** SPLADE_ENSEMBLE_PP 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `9b4eed622ee9403f707b55fe77549c60` 
- :material-text: **Run description:** Baseline run using a ensemble of SPLADE models available on huggingface (naver/splade-cocondenser-selfdistil and naver/splade-cocondenser-ensembledistil) and presented at SIGIR (https://arxiv.org/pdf/2205.04733.pdf). 

---
#### SPLADE_ENSEMBLE_PP_D 
[**`Results`**](./results.md#splade_ensemble_pp_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_ENSEMBLE_PP_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_ENSEMBLE_PP_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_ENSEMBLE_PP_D.pdf) 

- :material-rename: **Run ID:** SPLADE_ENSEMBLE_PP_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `d6d14f76b5753a1d1b0fbfad961f54ef` 
- :material-text: **Run description:** Baseline run using a ensemble of SPLADE models available on huggingface (naver/splade-cocondenser-selfdistil and naver/splade-cocondenser-ensembledistil) and presented at SIGIR (https://arxiv.org/pdf/2205.04733.pdf). Converted to document with max_p 

---
#### SPLADE_ENSEMBLE_PP_RCIO 
[**`Results`**](./results.md#splade_ensemble_pp_rcio) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_ENSEMBLE_PP_RCIO.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_ENSEMBLE_PP_RCIO.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_ENSEMBLE_PP_RCIO.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_ENSEMBLE_PP_RCIO.pdf) 

- :material-rename: **Run ID:** SPLADE_ENSEMBLE_PP_RCIO 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `ab343755599a0e50de9dc9ba6e36a52b` 
- :material-text: **Run description:** Baseline run using a ensemble of SPLADE models available on huggingface (naver/splade-cocondenser-selfdistil and naver/splade-cocondenser-ensembledistil) and presented at SIGIR (https://arxiv.org/pdf/2205.04733.pdf). With Rocchio 

---
#### SPLADE_ENSEMBLE_PP_RCIO_D 
[**`Results`**](./results.md#splade_ensemble_pp_rcio_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_ENSEMBLE_PP_RCIO_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_ENSEMBLE_PP_RCIO_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_ENSEMBLE_PP_RCIO_D.pdf) 

- :material-rename: **Run ID:** SPLADE_ENSEMBLE_PP_RCIO_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `f001a6c1ff2186906cbaeee177072b50` 
- :material-text: **Run description:** Baseline run using a ensemble of SPLADE models available on huggingface (naver/splade-cocondenser-selfdistil and naver/splade-cocondenser-ensembledistil) and presented at SIGIR (https://arxiv.org/pdf/2205.04733.pdf). With Rocchio. Converted to document with max_p 

---
#### SPLADE_PP_ED 
[**`Results`**](./results.md#splade_pp_ed) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_PP_ED.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_PP_ED.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_PP_ED.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_PP_ED.pdf) 

- :material-rename: **Run ID:** SPLADE_PP_ED 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `33420ecb41ef88e309d6b06b86119151` 
- :material-text: **Run description:** Baseline run using the SPLADE model available on huggingface (naver/splade-cocondenser-ensembledistil) and presented at SIGIR (https://arxiv.org/pdf/2205.04733.pdf) 

---
#### SPLADE_PP_ED_D 
[**`Results`**](./results.md#splade_pp_ed_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_PP_ED_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_PP_ED_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_PP_ED_D.pdf) 

- :material-rename: **Run ID:** SPLADE_PP_ED_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `527d8f2bd8bbf551442e4f0182bb18d0` 
- :material-text: **Run description:** Baseline run using the SPLADE model available on huggingface (naver/splade-cocondenser-ensembledistil) and presented at SIGIR (https://arxiv.org/pdf/2205.04733.pdf). Converted to document with max passage 

---
#### SPLADE_PP_ED_RCIO 
[**`Results`**](./results.md#splade_pp_ed_rcio) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_PP_ED_RCIO.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_PP_ED_RCIO.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_PP_ED_RCIO.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_PP_ED_RCIO.pdf) 

- :material-rename: **Run ID:** SPLADE_PP_ED_RCIO 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `d30d804ccb5a9fd102073b22c499cae1` 
- :material-text: **Run description:** Baseline run using the SPLADE model available on huggingface (naver/splade-cocondenser-ensembledistil) and presented at SIGIR (https://arxiv.org/pdf/2205.04733.pdf). We add Rocchio to the retrieval. Converted to document with max passage 

---
#### SPLADE_PP_ED_RCIO_D 
[**`Results`**](./results.md#splade_pp_ed_rcio_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_PP_ED_RCIO_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_PP_ED_RCIO_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_PP_ED_RCIO_D.pdf) 

- :material-rename: **Run ID:** SPLADE_PP_ED_RCIO_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `80fa814a8c71508d77419390ab7dc32a` 
- :material-text: **Run description:** Baseline run using the SPLADE model available on huggingface (naver/splade-cocondenser-ensembledistil) and presented at SIGIR (https://arxiv.org/pdf/2205.04733.pdf). We add Rocchio to the retrieval. Converted to document with max passage 

---
#### SPLADE_PP_SD 
[**`Results`**](./results.md#splade_pp_sd) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_PP_SD.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_PP_SD.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_PP_SD.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_PP_SD.pdf) 

- :material-rename: **Run ID:** SPLADE_PP_SD 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `379a55cf59fe24a44d5de18b3e133f60` 
- :material-text: **Run description:** Baseline run using the SPLADE model available on huggingface (naver/splade-cocondenser-selfdistil) and presented at SIGIR (https://arxiv.org/pdf/2205.04733.pdf). 

---
#### SPLADE_PP_SD_D 
[**`Results`**](./results.md#splade_pp_sd_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_PP_SD_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_PP_SD_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_PP_SD_D.pdf) 

- :material-rename: **Run ID:** SPLADE_PP_SD_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `e26542dcbca39ed8392854ceff777471` 
- :material-text: **Run description:** Baseline run using the SPLADE model available on huggingface (naver/splade-cocondenser-selfdistil) and presented at SIGIR (https://arxiv.org/pdf/2205.04733.pdf). We add Rocchio to the retrieval. Converted to document with max_p 

---
#### SPLADE_PP_SD_RCIO 
[**`Results`**](./results.md#splade_pp_sd_rcio) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_PP_SD_RCIO.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_PP_SD_RCIO.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_PP_SD_RCIO.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_PP_SD_RCIO.pdf) 

- :material-rename: **Run ID:** SPLADE_PP_SD_RCIO 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `30a4052d1bac59f7a6fbe3d80b18d714` 
- :material-text: **Run description:** Baseline run using the SPLADE model available on huggingface (naver/splade-cocondenser-selfdistil) and presented at SIGIR (https://arxiv.org/pdf/2205.04733.pdf). We add Rocchio to the retrieval. 

---
#### SPLADE_PP_SD_RCIO_D 
[**`Results`**](./results.md#splade_pp_sd_rcio_d) | [**`Participants`**](./participants.md#nle) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.SPLADE_PP_SD_RCIO_D.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.SPLADE_PP_SD_RCIO_D) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/SPLADE_PP_SD_RCIO_D.pdf) 

- :material-rename: **Run ID:** SPLADE_PP_SD_RCIO_D 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `a8400b313725f60af1044f546afb9914` 
- :material-text: **Run description:** Baseline run using the SPLADE model available on huggingface (naver/splade-cocondenser-selfdistil) and presented at SIGIR (https://arxiv.org/pdf/2205.04733.pdf). We add Rocchio to the retrieval. Converted to document with max_p 

---
#### srchvrs_d_bm25 
[**`Results`**](./results.md#srchvrs_d_bm25) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_d_bm25.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_d_bm25) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_d_bm25.pdf) 

- :material-rename: **Run ID:** srchvrs_d_bm25 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/29/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `e431df71faa03f95d511feb94ab28223` 
- :material-text: **Run description:** BM25 on doc text 

---
#### srchvrs_d_bm25_mdl1 
[**`Results`**](./results.md#srchvrs_d_bm25_mdl1) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_d_bm25_mdl1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_d_bm25_mdl1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_d_bm25_mdl1.pdf) 

- :material-rename: **Run ID:** srchvrs_d_bm25_mdl1 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/29/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `7829de00f230b1ed0a41e66c6da07e2b` 
- :material-text: **Run description:** BM25 + Model 1 trained on metadata (with re-ranking srchvrs_d_bm25) 

---
#### srchvrs_d_bm25_mf 
[**`Results`**](./results.md#srchvrs_d_bm25_mf) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_d_bm25_mf.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_d_bm25_mf) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_d_bm25_mf.pdf) 

- :material-rename: **Run ID:** srchvrs_d_bm25_mf 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/29/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `6b9e36a346072c595e9738dfdcbef32d` 
- :material-text: **Run description:** BM25 multi-field (with re-ranking srchvrs_d_bm25) 

---
#### srchvrs_d_bm25_mf_mdl1 
[**`Results`**](./results.md#srchvrs_d_bm25_mf_mdl1) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_d_bm25_mf_mdl1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_d_bm25_mf_mdl1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_d_bm25_mf_mdl1.pdf) 

- :material-rename: **Run ID:** srchvrs_d_bm25_mf_mdl1 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `cd2dfdaf3dcbee4fa8c4f21010d00bef` 
- :material-text: **Run description:** BM25 multi-field + Model 1 (with re-ranking srchvrs_d_bm25) 

---
#### srchvrs_d_bm25_p_mf_mdl1 
[**`Results`**](./results.md#srchvrs_d_bm25_p_mf_mdl1) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_d_bm25_p_mf_mdl1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_d_bm25_p_mf_mdl1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_d_bm25_p_mf_mdl1.pdf) 

- :material-rename: **Run ID:** srchvrs_d_bm25_p_mf_mdl1 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `4eeb5de0de62945f09661596e9abc22a` 
- :material-text: **Run description:** BM25 multi-field + Model 1 trained on meta-data (reranking a passage BM25 run, i.e., retrieval via passages) 

---
#### srchvrs_d_bm25_pass_mdl1 
[**`Results`**](./results.md#srchvrs_d_bm25_pass_mdl1) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_d_bm25_pass_mdl1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_d_bm25_pass_mdl1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_d_bm25_pass_mdl1.pdf) 

- :material-rename: **Run ID:** srchvrs_d_bm25_pass_mdl1 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `faa35351c2d652642ad1477dd7ae17c4` 
- :material-text: **Run description:** BM25 (passage score + single document field score) + Model 1 trained on meta-data (reranking a passage BM25 run, i.e., retrieval via passages) 

---
#### srchvrs_d_bm25_pass_mf 
[**`Results`**](./results.md#srchvrs_d_bm25_pass_mf) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_d_bm25_pass_mf.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_d_bm25_pass_mf) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_d_bm25_pass_mf.pdf) 

- :material-rename: **Run ID:** srchvrs_d_bm25_pass_mf 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `8d1719c712bb5b6b2aa53eb77de050f7` 
- :material-text: **Run description:** BM25 multi-field (reranking a passage BM25 run, i.e., retrieval via passages) 

---
#### srchvrs_d_lb1 
[**`Results`**](./results.md#srchvrs_d_lb1) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_d_lb1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_d_lb1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_d_lb1.pdf) 

- :material-rename: **Run ID:** srchvrs_d_lb1 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `066e9395da08f77ce3f9b0103e2edd3c` 
- :material-text: **Run description:** neural retriever + neural re-ranker. trained using MS MARCO v1. 

---
#### srchvrs_d_lb2 
[**`Results`**](./results.md#srchvrs_d_lb2) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_d_lb2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_d_lb2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_d_lb2.pdf) 

- :material-rename: **Run ID:** srchvrs_d_lb2 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `b25af4aa067fb1bf047560e0132301df` 
- :material-text: **Run description:** neural retriever + neural re-ranker. trained using MS MARCO v1. 

---
#### srchvrs_d_lb3 
[**`Results`**](./results.md#srchvrs_d_lb3) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_d_lb3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_d_lb3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_d_lb3.pdf) 

- :material-rename: **Run ID:** srchvrs_d_lb3 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `b8af91ff95fe8c99488de6bb85b1d490` 
- :material-text: **Run description:** neural retriever + neural re-ranker. trained using MS MARCO v1. 

---
#### srchvrs_d_prd1 
[**`Results`**](./results.md#srchvrs_d_prd1) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_d_prd1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_d_prd1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_d_prd1.pdf) 

- :material-rename: **Run ID:** srchvrs_d_prd1 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `c6a60ec6c3491cce2ec9b241f32b96f1` 
- :material-text: **Run description:** neural retriever + neural re-ranker. trained using MS MARCO v1. 

---
#### srchvrs_d_prd3 
[**`Results`**](./results.md#srchvrs_d_prd3) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_d_prd3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_d_prd3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_d_prd3.pdf) 

- :material-rename: **Run ID:** srchvrs_d_prd3 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `1203e1fa37afe5b9f3936e3e51eef91d` 
- :material-text: **Run description:** neural retriever + neural re-ranker. trained using MS MARCO v1. 

---
#### srchvrs_dtn1 
[**`Results`**](./results.md#srchvrs_dtn1) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_dtn1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_dtn1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_dtn1.pdf) 

- :material-rename: **Run ID:** srchvrs_dtn1 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/4/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `ee6b2561a6816fce9dd527367b23eee7` 
- :material-text: **Run description:** neural retriever + neural reranker 

---
#### srchvrs_dtn2 
[**`Results`**](./results.md#srchvrs_dtn2) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_dtn2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_dtn2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_dtn2.pdf) 

- :material-rename: **Run ID:** srchvrs_dtn2 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/4/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `554e482eee7353c424b240b49b46b091` 
- :material-text: **Run description:** neural retriever + neural reranker 

---
#### srchvrs_p1_colb2 
[**`Results`**](./results.md#srchvrs_p1_colb2) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_p1_colb2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_p1_colb2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_p1_colb2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_p1_colb2.pdf) 

- :material-rename: **Run ID:** srchvrs_p1_colb2 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/7/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `3521045205b31ce4bdc4d651370ce17b` 
- :material-text: **Run description:** lucene + neural reranker (using MS MARCO v1 models) 

---
#### srchvrs_p2_colb2 
[**`Results`**](./results.md#srchvrs_p2_colb2) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_p2_colb2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_p2_colb2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_p2_colb2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_p2_colb2.pdf) 

- :material-rename: **Run ID:** srchvrs_p2_colb2 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/7/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `bc0c03dd185c822d22dabde7240eb492` 
- :material-text: **Run description:** neural retriever + neural reranker (using MS MARCO v1 models) 

---
#### srchvrs_p_bm25 
[**`Results`**](./results.md#srchvrs_p_bm25) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_p_bm25.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_p_bm25.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_p_bm25.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_p_bm25.pdf) 

- :material-rename: **Run ID:** srchvrs_p_bm25 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `db8a1cc181166b8d9142b018571cfad4` 
- :material-text: **Run description:** BM25 (only passage text) 

---
#### srchvrs_p_bm25_mdl1 
[**`Results`**](./results.md#srchvrs_p_bm25_mdl1) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_p_bm25_mdl1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_p_bm25_mdl1.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_p_bm25_mdl1.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_p_bm25_mdl1.pdf) 

- :material-rename: **Run ID:** srchvrs_p_bm25_mdl1 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `767e7bfe94709c284e8ad68db7029a00` 
- :material-text: **Run description:** BM25 + Model 1 score (passage and document fields, reranking srchvrs_p_bm25) 

---
#### srchvrs_p_bm25f 
[**`Results`**](./results.md#srchvrs_p_bm25f) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_p_bm25f.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_p_bm25f.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_p_bm25f.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_p_bm25f.pdf) 

- :material-rename: **Run ID:** srchvrs_p_bm25f 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `62ef7ec89a2d7471235e0170e9c44975` 
- :material-text: **Run description:** BM25 multi-field (passage and document field, reranking srchvrs_p_bm25) 

---
#### srchvrs_p_bm25f_mdl1 
[**`Results`**](./results.md#srchvrs_p_bm25f_mdl1) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_p_bm25f_mdl1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_p_bm25f_mdl1.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_p_bm25f_mdl1.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_p_bm25f_mdl1.pdf) 

- :material-rename: **Run ID:** srchvrs_p_bm25f_mdl1 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 7/30/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `4a05b15dbe9cf248734db2051eac87a9` 
- :material-text: **Run description:** BM25 multi-field + Model 1 score (passage and document fields, reranking srchvrs_p_bm25) 

---
#### srchvrs_ptn1_colb2 
[**`Results`**](./results.md#srchvrs_ptn1_colb2) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_ptn1_colb2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_ptn1_colb2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_ptn1_colb2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_ptn1_colb2.pdf) 

- :material-rename: **Run ID:** srchvrs_ptn1_colb2 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/7/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `fc1ab3ae85aa7669cbf9d3a9df2841e7` 
- :material-text: **Run description:** neural retriever + neural reranker (using MS MARCO v1 models) 

---
#### srchvrs_ptn1_lcn_colb2 
[**`Results`**](./results.md#srchvrs_ptn1_lcn_colb2) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_ptn1_lcn_colb2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_ptn1_lcn_colb2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_ptn1_lcn_colb2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_ptn1_lcn_colb2.pdf) 

- :material-rename: **Run ID:** srchvrs_ptn1_lcn_colb2 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/7/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `042538ffc00e94b8430f0a4b297b62c5` 
- :material-text: **Run description:** lucene + neural reranker (using MS MARCO v1 models) 

---
#### srchvrs_ptn2_colb2 
[**`Results`**](./results.md#srchvrs_ptn2_colb2) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_ptn2_colb2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_ptn2_colb2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_ptn2_colb2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_ptn2_colb2.pdf) 

- :material-rename: **Run ID:** srchvrs_ptn2_colb2 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/7/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `da09c6ec52e1adbf997e41374bc073b7` 
- :material-text: **Run description:** neural retriever + neural reranker (using MS MARCO v1 models) 

---
#### srchvrs_ptn3_colb2 
[**`Results`**](./results.md#srchvrs_ptn3_colb2) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_ptn3_colb2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_ptn3_colb2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_ptn3_colb2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_ptn3_colb2.pdf) 

- :material-rename: **Run ID:** srchvrs_ptn3_colb2 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/7/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `deb29684ce48c6fff949b5769c835d3c` 
- :material-text: **Run description:** neural retriever + neural reranker (using MS MARCO v1 models) 

---
#### srchvrs_pz1_colb2 
[**`Results`**](./results.md#srchvrs_pz1_colb2) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_pz1_colb2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_pz1_colb2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_pz1_colb2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_pz1_colb2.pdf) 

- :material-rename: **Run ID:** srchvrs_pz1_colb2 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/7/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `733e4c7fae28a9ed581021f781d973c4` 
- :material-text: **Run description:** lucene + neural reranker (using MS MARCO v1 models) 

---
#### srchvrs_pz2_colb2 
[**`Results`**](./results.md#srchvrs_pz2_colb2) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.srchvrs_pz2_colb2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_pz2_colb2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.srchvrs_pz2_colb2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/srchvrs_pz2_colb2.pdf) 

- :material-rename: **Run ID:** srchvrs_pz2_colb2 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/7/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `22785eed7e62b4b815ff11c7b8ca8743` 
- :material-text: **Run description:** neural retriever + neural reranker (using MS MARCO v1 models) 

---
#### tuvienna 
[**`Results`**](./results.md#tuvienna) | [**`Participants`**](./participants.md#dossier) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.tuvienna.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.tuvienna) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/tuvienna.pdf) 

- :material-rename: **Run ID:** tuvienna 
- :fontawesome-solid-user-group: **Participant:** DOSSIER 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/8/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `c67cbff8d29b0233281a84a5c0a264f8` 
- :material-text: **Run description:** We employ the ColBERTer model, which reduces the storage space for retrieval while maintaining retrieval effectiveness. We use the ColBERTer model which compresses the representation to a 32-dimensional embedding. The model is based on ColBERT and combines dense retrieval with ColBERT-style token-based refinement. The model is trained with knowledge distillation training for dense retrieval and token-refinement on MS Marco v1. The model starts from the pretrained language model DistilBERT.  

---
#### tuvienna-pas-col 
[**`Results`**](./results.md#tuvienna-pas-col) | [**`Participants`**](./participants.md#dossier) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.tuvienna-pas-col.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.tuvienna-pas-col.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.tuvienna-pas-col.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/tuvienna-pas-col.pdf) 

- :material-rename: **Run ID:** tuvienna-pas-col 
- :fontawesome-solid-user-group: **Participant:** DOSSIER 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/8/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `b64d7b8ebcdb7363a6ea1959f71d3d7c` 
- :material-text: **Run description:** We employ the ColBERTer model, which reduces the storage space for retrieval while maintaining retrieval effectiveness. We use the ColBERTer model which compresses the representation to a 32-dimensional embedding. The model is based on ColBERT and combines dense retrieval with ColBERT-style token-based refinement. The model is trained with knowledge distillation training for dense retrieval and token-refinement on MS Marco v1. The model starts from the pretrained language model DistilBERT.  

---
#### tuvienna-pas-unicol 
[**`Results`**](./results.md#tuvienna-pas-unicol) | [**`Participants`**](./participants.md#dossier) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.tuvienna-pas-unicol.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.tuvienna-pas-unicol.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.tuvienna-pas-unicol.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/tuvienna-pas-unicol.pdf) 

- :material-rename: **Run ID:** tuvienna-pas-unicol 
- :fontawesome-solid-user-group: **Participant:** DOSSIER 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/8/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `96bd79db9279676a96a3b313a75e6c95` 
- :material-text: **Run description:** We employ the ColBERTer model, which reduces the storage space for retrieval while maintaining retrieval effectiveness. We employ Uni-ColBERTer with exact matching and a 1-dimensional score. The model is based on ColBERT and combines dense retrieval with ColBERT-style token-based refinement. The model is trained with knowledge distillation training for dense retrieval and token-refinement on MS Marco v1. The model starts from the pretrained language model DistilBERT.  

---
#### tuvienna-unicol 
[**`Results`**](./results.md#tuvienna-unicol) | [**`Participants`**](./participants.md#dossier) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.tuvienna-unicol.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.tuvienna-unicol) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/tuvienna-unicol.pdf) 

- :material-rename: **Run ID:** tuvienna-unicol 
- :fontawesome-solid-user-group: **Participant:** DOSSIER 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/8/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `d9117ba87d8c16e1d9248e0572255efe` 
- :material-text: **Run description:** We employ the ColBERTer model, which reduces the storage space for retrieval while maintaining retrieval effectiveness. We employ Uni-ColBERTer with exact matching and a 1-dimensional score. The model is based on ColBERT and combines dense retrieval with ColBERT-style token-based refinement. The model is trained with knowledge distillation training for dense retrieval and token-refinement on MS Marco v1. The model starts from the pretrained language model DistilBERT.  

---
#### unicoil_reranked 
[**`Results`**](./results.md#unicoil_reranked) | [**`Participants`**](./participants.md#uga) | [**`Proceedings`**](./proceedings.md#universite-grenoble-alpes-lig-at-trec-deep-learning-track-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.unicoil_reranked.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.unicoil_reranked.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.unicoil_reranked.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/unicoil_reranked.pdf) 

- :material-rename: **Run ID:** unicoil_reranked 
- :fontawesome-solid-user-group: **Participant:** UGA 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/6/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `36d2e276f37a8516cafe38895647b9d0` 
- :material-text: **Run description:** Pre-trained Unicoil model with 2 stage reranking. MiniLM-L12 is applied in the first stage at top 100 results and T5 is applied in the second stage at top 10 results. 

---
#### uogtr_be 
[**`Results`**](./results.md#uogtr_be) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_be.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_be.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_be.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_be.pdf) 

- :material-rename: **Run ID:** uogtr_be 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `c12f5801937b4b37d7decdd0063ff5c7` 
- :material-text: **Run description:** BM25 retrieval, re-ranked using crystina-z/monoELECTRA_LCE_nneg31 

---
#### uogtr_be_gb 
[**`Results`**](./results.md#uogtr_be_gb) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_be_gb.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_be_gb.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_be_gb.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_be_gb.pdf) 

- :material-rename: **Run ID:** uogtr_be_gb 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `37890ba8c4c8ced4bcddf5ff3b3894f8` 
- :material-text: **Run description:** BM25 retrieval, adaptively re-ranked using crystina-z/monoELECTRA_LCE_nneg31 and a BM25 graph 

---
#### uogtr_c 
[**`Results`**](./results.md#uogtr_c) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_c.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_c.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_c.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_c.pdf) 

- :material-rename: **Run ID:** uogtr_c 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `81cea1df84e8f8713c5d58ace4b94320` 
- :material-text: **Run description:** Performs ColBERT E2E on msmarco-passage-v2 colbert dense index 

---
#### uogtr_c_cprf 
[**`Results`**](./results.md#uogtr_c_cprf) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_c_cprf.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_c_cprf.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_c_cprf.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_c_cprf.pdf) 

- :material-rename: **Run ID:** uogtr_c_cprf 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `f3d04212ff78f15a27f34354832f4628` 
- :material-text: **Run description:** Performs ColBERT-PRF reranker on top of ColBERT E2E , then reranks using ColBERT. 

---
#### uogtr_doc_dph 
[**`Results`**](./results.md#uogtr_doc_dph) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_doc_dph.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_doc_dph) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_doc_dph.pdf) 

- :material-rename: **Run ID:** uogtr_doc_dph 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `5c9d3539b88ccc7cb1caa03b4d43f0e4` 
- :material-text: **Run description:** Performing dph on the entire msmarco-document-v2 inverted index. 

---
#### uogtr_doc_dph_bo1 
[**`Results`**](./results.md#uogtr_doc_dph_bo1) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_doc_dph_bo1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_doc_dph_bo1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_doc_dph_bo1.pdf) 

- :material-rename: **Run ID:** uogtr_doc_dph_bo1 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `a9d73cf9c52e3feeb9ff3fd6232941d3` 
- :material-text: **Run description:** Performing dph with bo1 query expansion on the entire msmarco-document-v2 inverted index. 

---
#### uogtr_dph 
[**`Results`**](./results.md#uogtr_dph) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_dph.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_dph.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_dph.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_dph.pdf) 

- :material-rename: **Run ID:** uogtr_dph 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `05fd745a86f74b8b4261d60aee65dc72` 
- :material-text: **Run description:** Performs DPH on the entire msmarco-passage-v2 inverted index. 

---
#### uogtr_dph_bo1 
[**`Results`**](./results.md#uogtr_dph_bo1) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_dph_bo1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_dph_bo1.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_dph_bo1.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_dph_bo1.pdf) 

- :material-rename: **Run ID:** uogtr_dph_bo1 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `6aee49a2c0a7e9da18f51e9c3597e8fc` 
- :material-text: **Run description:** Performs DPH with Bo1 query expansion on the entire msmarco-passage-v2 inverted index. 

---
#### uogtr_e_cprf_t5 
[**`Results`**](./results.md#uogtr_e_cprf_t5) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_e_cprf_t5.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_e_cprf_t5.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_e_cprf_t5.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_e_cprf_t5.pdf) 

- :material-rename: **Run ID:** uogtr_e_cprf_t5 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `d517cad714d058428345fd7a2e973f91` 
- :material-text: **Run description:** Make the hybrid of the retrieved documents of  TCT_ColBERT reranking using ColBERT-PRF and  ColBERT E2E reranking using ColBERT-PRF, then  reranking the hybrid documents using monoT5 reranker. 

---
#### uogtr_e_gb 
[**`Results`**](./results.md#uogtr_e_gb) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_e_gb.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_e_gb.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_e_gb.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_e_gb.pdf) 

- :material-rename: **Run ID:** uogtr_e_gb 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `f8285aa263549b805be4895223c99f86` 
- :material-text: **Run description:** Ensemble of BM25 and SPLADE retrieval using naver/splade-cocondenser-ensembledistil, adaptively re-ranked using crystina-z/monoELECTRA_LCE_nneg31 using a BM25 graph 

---
#### uogtr_s 
[**`Results`**](./results.md#uogtr_s) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_s.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_s.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_s.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_s.pdf) 

- :material-rename: **Run ID:** uogtr_s 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `3d8da1806d759fa20d631cba359f8c5f` 
- :material-text: **Run description:** SPLADE retrieval using naver/splade-cocondenser-ensembledistil 

---
#### uogtr_s_cprf 
[**`Results`**](./results.md#uogtr_s_cprf) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_s_cprf.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_s_cprf.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_s_cprf.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_s_cprf.pdf) 

- :material-rename: **Run ID:** uogtr_s_cprf 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `93d8d14a8e570bc519f700d3bda26e4a` 
- :material-text: **Run description:** Performs ColBERT-PRF on top of SPLADE retrieval,  then reranks using ColBERT. 

---
#### uogtr_se 
[**`Results`**](./results.md#uogtr_se) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_se.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_se.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_se.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_se.pdf) 

- :material-rename: **Run ID:** uogtr_se 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `98fd3cd8ddb56db111f203b83e073f3d` 
- :material-text: **Run description:** SPLADE retrieval using naver/splade-cocondenser-ensembledistil, re-ranked using crystina-z/monoELECTRA_LCE_nneg31 

---
#### uogtr_se_gb 
[**`Results`**](./results.md#uogtr_se_gb) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_se_gb.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_se_gb.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_se_gb.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_se_gb.pdf) 

- :material-rename: **Run ID:** uogtr_se_gb 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `b50d1650d17faced73645b40eab55299` 
- :material-text: **Run description:** SPLADE retrieval using naver/splade-cocondenser-ensembledistil, adaptively re-ranked using crystina-z/monoELECTRA_LCE_nneg31 using a BM25 graph 

---
#### uogtr_se_gt 
[**`Results`**](./results.md#uogtr_se_gt) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_se_gt.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_se_gt.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_se_gt.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_se_gt.pdf) 

- :material-rename: **Run ID:** uogtr_se_gt 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `5761a1446349042df5443806f4da45c2` 
- :material-text: **Run description:** SPLADE retrieval using naver/splade-cocondenser-ensembledistil, adaptively re-ranked using crystina-z/monoELECTRA_LCE_nneg31 using a TCT-ColBERT graph constructed using HNSW data 

---
#### uogtr_t_cprf 
[**`Results`**](./results.md#uogtr_t_cprf) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#experiments-with-adaptive-reranking-and-colbert-prf-university-of-glasgow-terrier-team-at-trec-dl-2022) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.uogtr_t_cprf.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_t_cprf.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.uogtr_t_cprf.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/uogtr_t_cprf.pdf) 

- :material-rename: **Run ID:** uogtr_t_cprf 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `2f97d07293d6e9b265f591897187cf75` 
- :material-text: **Run description:** Performs ColBERT-PRF on top of TCT-ColBERT retrieval, then reranks using ColBERT. 

---
#### webis-dl-duot5 
[**`Results`**](./results.md#webis-dl-duot5) | [**`Participants`**](./participants.md#webis) | [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.webis-dl-duot5.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.webis-dl-duot5.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.webis-dl-duot5.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/webis-dl-duot5.pdf) 

- :material-rename: **Run ID:** webis-dl-duot5 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `63a7df70aeed27f69f4c8a9b22fc9cf3` 
- :material-text: **Run description:** We rerank the top-100 candidates of the official baseline with monoT5 and rerank the top-50 of the monoT5 ranking with duoT5. We use the implementation of monoT5 and duoT5 in Pyterrier with models trained on Version~1 of MS~MARCO available at Hugging Face: https://huggingface.co/castorini/monot5-3b-msmarco for monoT5 and https://huggingface.co/castorini/duot5-3b-msmarco for duoT5. 

---
#### webis-dl-duot5-aug-1 
[**`Results`**](./results.md#webis-dl-duot5-aug-1) | [**`Participants`**](./participants.md#webis) | [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.webis-dl-duot5-aug-1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.webis-dl-duot5-aug-1.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.webis-dl-duot5-aug-1.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/webis-dl-duot5-aug-1.pdf) 

- :material-rename: **Run ID:** webis-dl-duot5-aug-1 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `db70f0756b8c2dd894c88785f2b32613` 
- :material-text: **Run description:** We rerank the top-25 results of our webis-dl-duot5-g run by aggregating multiple pairwise preferences obtained via duoT5 on augmented document pairs. Out of 9 augmentation patterns ((1) no augmentation, (2, 3, 4) using only the first one, two, or three sentence(s) of the passages, and (5, 6, 7, 8, 9) expand the passages with a query obtained via doct5query.), two methods to aggregate pairwise scores (greedy and sym-sum), and five methods to aggregate augmented scores (min, max, mean, median, sum), we selected the combination with the highest nDCG@10 on the 2020 TREC DL data. This hyperparameter optimization yielded an approach that used five augmentations ((1) no augmentation, (2) both passages in a comparison shortened to the first two sentences, (3-5) variants of passage expansions) that are aggregated into a single pairwise score using min aggregation and the pairwise scores are aggregated to the retrieval scores using greedy aggregation. 

---
#### webis-dl-duot5-aug-2 
[**`Results`**](./results.md#webis-dl-duot5-aug-2) | [**`Participants`**](./participants.md#webis) | [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.webis-dl-duot5-aug-2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.webis-dl-duot5-aug-2.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.webis-dl-duot5-aug-2.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/webis-dl-duot5-aug-2.pdf) 

- :material-rename: **Run ID:** webis-dl-duot5-aug-2 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `e6b0f49547cd9da8865e531cbc240293` 
- :material-text: **Run description:** We rerank the top-25 results of our webis-dl-duot5-g run by aggregating multiple pairwise preferences obtained via duoT5 on augmented document pairs. Out of 9 augmentation patterns ((1) no augmentation, (2, 3, 4) using only the first one, two, or three sentence(s) of the passages, and (5, 6, 7, 8, 9) expand the passages with a query obtained via doct5query.), two methods to aggregate pairwise scores (greedy and sym-sum), and five methods to aggregate augmented scores (min, max, mean, median, sum), we selected the combination with the highest MRR on the 2020 TREC DL data. This hyperparameter optimization yielded an approach that used six augmentations ((1) no augmentation, (2,3) both passages in a comparison shortened to the first one and first three sentences, (4-6) variants of passage expansions) that are aggregated into a single pairwise score using sum aggregation and the pairwise scores are aggregated to the retrieval scores using greedy aggregation. 

---
#### webis-dl-duot5-g 
[**`Results`**](./results.md#webis-dl-duot5-g) | [**`Participants`**](./participants.md#webis) | [**`Proceedings`**](./proceedings.md#webis-at-trec-2022-deep-learning-and-health-misinformation) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.webis-dl-duot5-g.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.webis-dl-duot5-g.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.webis-dl-duot5-g.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/webis-dl-duot5-g.pdf) 

- :material-rename: **Run ID:** webis-dl-duot5-g 
- :fontawesome-solid-user-group: **Participant:** Webis 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/10/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `dedfef8a8cb0b60c79fc3a36f00249dd` 
- :material-text: **Run description:** We rerank the top-100 candidates of the official baseline with monoT5 and rerank the top-50 of the monoT5 ranking with duoT5 with greedy aggregation. We use the implementation of monoT5 and duoT5 in Pyterrier with models trained on Version~1 of MS~MARCO available at Hugging Face: https://huggingface.co/castorini/monot5-3b-msmarco for monoT5 and https://huggingface.co/castorini/duot5-3b-msmarco for duoT5. To aggregate the pairwise preferences into retrieval scores, we use a greedy approach instead of the default sym-sum aggregation. 

---
#### yorku22a 
[**`Results`**](./results.md#yorku22a) | [**`Participants`**](./participants.md#yorku22) | [**`Proceedings`**](./proceedings.md#york-university-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.yorku22a.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.yorku22a.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.yorku22a.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/yorku22a.pdf) 

- :material-rename: **Run ID:** yorku22a 
- :fontawesome-solid-user-group: **Participant:** yorku22 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `629961bd776b0e0310e58b7a77368c22` 
- :material-text: **Run description:** Base on Transformer 

---
#### yorku22b 
[**`Results`**](./results.md#yorku22b) | [**`Participants`**](./participants.md#yorku22) | [**`Proceedings`**](./proceedings.md#york-university-at-trec-2022-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec31/deep/input.yorku22b.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec31/deep/summary.yorku22b.trec_eval) | [**`Summary (ndcg)`**](https://trec.nist.gov/results/trec31/deep/summary.yorku22b.ndcg) | [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/deep/yorku22b.pdf) 

- :material-rename: **Run ID:** yorku22b 
- :fontawesome-solid-user-group: **Participant:** yorku22 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 8/9/2022 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `66f775641e0539555ef250b2d50f2cff` 
- :material-text: **Run description:** Based on BERT 

---
