# Runs - Clinical Trials 2023 

#### bm25_bsln 
[**`Participants`**](./participants.md#csiromed) 

- :material-rename: **Run ID:** bm25_bsln 
- :fontawesome-solid-user-group: **Participant:** CSIROmed 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/31/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `70d83c97e0afb29f3ae43199fa6da090` 
- :material-text: **Run description:** Solr BM25 baseline. 

---
#### BM25_two_stage 
[**`Participants`**](./participants.md#unimib_ikr3) 

- :material-rename: **Run ID:** BM25_two_stage 
- :fontawesome-solid-user-group: **Participant:** UNIMIB_IKR3 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/2/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `42f19ab6dc4df8f41ad4f43960975b51` 
- :material-text: **Run description:** BM25+RM3 and then a re-ranking based on BM25+RM3 on the eligibility+title 

---
#### BM25RM3_gpt35_run 
[**`Participants`**](./participants.md#unimib_ikr3) 

- :material-rename: **Run ID:** BM25RM3_gpt35_run 
- :fontawesome-solid-user-group: **Participant:** UNIMIB_IKR3 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/2/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `d5a491dd5dab78471f35dd4498bc285f` 
- :material-text: **Run description:** Single retrieval with BM25 and eligibility estimation based on a prompt introduced to ChatGPT 

---
#### BM25RM3_gpt35_strict_run 
[**`Participants`**](./participants.md#unimib_ikr3) 

- :material-rename: **Run ID:** BM25RM3_gpt35_strict_run 
- :fontawesome-solid-user-group: **Participant:** UNIMIB_IKR3 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/2/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `7faec543bd5a973d1d2bab63ef4b5b68` 
- :material-text: **Run description:** BM25 + RM3 + LLM to determine eligibility 

---
#### BM25RM3_single_run 
[**`Participants`**](./participants.md#unimib_ikr3) 

- :material-rename: **Run ID:** BM25RM3_single_run 
- :fontawesome-solid-user-group: **Participant:** UNIMIB_IKR3 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/2/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `11a5f7caa3e48437a86981a23a446ff8` 
- :material-text: **Run description:** BM25 with RM3 for pseudo relevance estimation. The queries have been processed so that onlyy the positive information has been kept. 

---
#### brsema3 
[**`Participants`**](./participants.md#ema3) 

- :material-rename: **Run ID:** brsema3 
- :fontawesome-solid-user-group: **Participant:** EMA3 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/2/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `f268005b0d6d49f191d2c48a9be42ead` 
- :material-text: **Run description:** This run uses a sentence encoder to encode the itemized inclusion and exclusion criteria. The scoring function weighs the inclusion and exclusion criteria equally.  

---
#### CE_weighted 
[**`Participants`**](./participants.md#csiro-uq-ielab) 

- :material-rename: **Run ID:** CE_weighted 
- :fontawesome-solid-user-group: **Participant:** CSIRO-UQ-ielab 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/30/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `48af05cd2016132bdc32d2b00f70a451` 
- :material-text: **Run description:** a 2-stage cascade ranking pipeline. The first stage retriever is a dense-sparse hybrid retriever model, the second stage reranker is a BERT cross-encoder reranker which rerankers top1000 docs from the first stage. The final doc scores are weighted between the scores of the retriever and reranker. 

---
#### DoSSIER_1 
[**`Participants`**](./participants.md#dossier) 

- :material-rename: **Run ID:** DoSSIER_1 
- :fontawesome-solid-user-group: **Participant:** DoSSIER 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/1/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `7422fe91d5977d707acf84879a82a930` 
- :material-text: **Run description:** Transformer models fine-tuned on clinical data used to standardize Clinical Trials and topics. Topic were enhanced with understanding through Synonym Enrichment using Language Models (LLMs). To retrieve relevant results, they utilized ElasticSearch and devised a custom query, incorporating specialized analyzers within the ElasticSearch mappings, to match the normalized data effectively. Finally, the lexically retrieved results were re-ranked by a neural model, which was pretrained on TREC CT data from previous years. 

---
#### DoSSIER_2 
[**`Participants`**](./participants.md#dossier) 

- :material-rename: **Run ID:** DoSSIER_2 
- :fontawesome-solid-user-group: **Participant:** DoSSIER 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/1/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `e755a3e9fc6c109396dfedbd1f0b997a` 
- :material-text: **Run description:** DFR retrieval model from PyTerrier, queries reformulated with GPT-3.5. Both documents and queries were expanded using the Kusa et al. 2023 approach for past, current and family medical history. 

---
#### DoSSIER_3 
[**`Participants`**](./participants.md#dossier) 

- :material-rename: **Run ID:** DoSSIER_3 
- :fontawesome-solid-user-group: **Participant:** DoSSIER 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/1/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `acd7c88b26ecb223f86dda10c013ede3` 
- :material-text: **Run description:** DoSSIER_1 run after neural reranking with the TCRR_BlueBERT model (top 100). 

---
#### DoSSIER_4 
[**`Participants`**](./participants.md#dossier) 

- :material-rename: **Run ID:** DoSSIER_4 
- :fontawesome-solid-user-group: **Participant:** DoSSIER 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/1/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `fbdab29ed64431b91876912a7156fc9a` 
- :material-text: **Run description:** DoSSIER_2 run after neural reranking with the TCRR_BlueBERT model (top 200) 

---
#### DoSSIER_5 
[**`Participants`**](./participants.md#dossier) 

- :material-rename: **Run ID:** DoSSIER_5 
- :fontawesome-solid-user-group: **Participant:** DoSSIER 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/6/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `a0e584cec82c4c3d2c95ff1a3440d2df` 
- :material-text: **Run description:** This run takes DoSSIER_4 run and post-processes it with the GPT-3.5 model using QA based on the eligibility criteria section. Runs are filtered until top 10 of them are included or # of excluded is equal to 50. 

---
#### DR 
[**`Participants`**](./participants.md#csiro-uq-ielab) 

- :material-rename: **Run ID:** DR 
- :fontawesome-solid-user-group: **Participant:** CSIRO-UQ-ielab 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/30/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `89467a156d119391af5294979bc35e3d` 
- :material-text: **Run description:** A BERT-based dense retriever model train with multistage hard negative mining and synthetic data generated by gpt-3.5-turbo. 

---
#### fbkida 
[**`Participants`**](./participants.md#fbk-ida) 

- :material-rename: **Run ID:** fbkida 
- :fontawesome-solid-user-group: **Participant:** FBK-IDA 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/1/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `e1074344349e783e2dfd5b2ecb2e9f81` 
- :material-text: **Run description:** We developed a proprietary retrieval model implemented through a pipeline starting with a retrieval method based on cosine similarity and with subsequent refinements adopting different type of language models. 

---
#### GPT4 
[**`Participants`**](./participants.md#csiro-uq-ielab) 

- :material-rename: **Run ID:** GPT4 
- :fontawesome-solid-user-group: **Participant:** CSIRO-UQ-ielab 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/30/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `30251e9567c34719ceff57a801373d59` 
- :material-text: **Run description:** a 3-stage cascade ranking pipeline. The first stage retriever is a dense-sparse hybrid retriever model, the second stage reranker is a BERT cross-encoder reranker which rerankers top1000 docs from the first stage. The thrid stage is prompting GPT4 to rerank top20 docs from the sencond stage. 

---
#### gpt_unweighted 
[**`Participants`**](./participants.md#patient2trial) 

- :material-rename: **Run ID:** gpt_unweighted 
- :fontawesome-solid-user-group: **Participant:** patient2trial 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/30/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `a85bc12191c4f5d95e2f9caaa8ff7544` 
- :material-text: **Run description:** Our retrieval system is based on BM25 and GPT. 

---
#### gpt_weighted 
[**`Participants`**](./participants.md#patient2trial) 

- :material-rename: **Run ID:** gpt_weighted 
- :fontawesome-solid-user-group: **Participant:** patient2trial 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/30/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `914448d014e521cd5f1b60de7cfee7b5` 
- :material-text: **Run description:** Our retrieval system is based on BM25 and GPT. 

---
#### Hybrid 
[**`Participants`**](./participants.md#csiro-uq-ielab) 

- :material-rename: **Run ID:** Hybrid 
- :fontawesome-solid-user-group: **Participant:** CSIRO-UQ-ielab 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/30/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `3b61deec89ae775475c0700268bef235` 
- :material-text: **Run description:** A BERT-based dense retriever and BERT-based SPLADE sparse retriever hybrid retrieval model. 

---
#### nrema3 
[**`Participants`**](./participants.md#ema3) 

- :material-rename: **Run ID:** nrema3 
- :fontawesome-solid-user-group: **Participant:** EMA3 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/2/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `7265ab8980a1d32cd880d593cf43a45f` 
- :material-text: **Run description:** This run uses a sentence encoder to encode the itemized inclusion and exclusion criteria. The scoring function prefers high precision and performs strict checks for exclusion criteria,  

---
#### qe 
[**`Participants`**](./participants.md#csiromed) 

- :material-rename: **Run ID:** qe 
- :fontawesome-solid-user-group: **Participant:** CSIROmed 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/31/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `b004cc30b31b636b6bb22f26fab3ff2f` 
- :material-text: **Run description:** Solr BM25 with query expansion with GPT-3.5. 

---
#### qe_err 
[**`Participants`**](./participants.md#csiromed) 

- :material-rename: **Run ID:** qe_err 
- :fontawesome-solid-user-group: **Participant:** CSIROmed 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/31/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `6520faa19a36c70b8a7d83909b2cf814` 
- :material-text: **Run description:** Solr BM25 with query expansion with GPT-3.5, followed by reranking with GPT embeddings (zero-shot bi-encoder setup). 

---
#### qe_prr_ft_rf 
[**`Participants`**](./participants.md#csiromed) 

- :material-rename: **Run ID:** qe_prr_ft_rf 
- :fontawesome-solid-user-group: **Participant:** CSIROmed 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/31/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `21446c899c6661ef7d9561f54a532655` 
- :material-text: **Run description:** Solr BM25 with query expansion with GPT-3.5, followed by prompt-based reranking with GPT-3.5 (fine-tuned on a subset of 2021 TREC CT dataset). Rank fusion between BM25 and reranker. 

---
#### qe_prr_zs 
[**`Participants`**](./participants.md#csiromed) 

- :material-rename: **Run ID:** qe_prr_zs 
- :fontawesome-solid-user-group: **Participant:** CSIROmed 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/31/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `e2d2dd42c39384ca0a31b7a438a5fc5f` 
- :material-text: **Run description:** Solr BM25 with query expansion with GPT-3.5, followed by prompt-based reranking with GPT-3.5 (zero-shot). 

---
#### run1 
[**`Participants`**](./participants.md#mu_cs) 

- :material-rename: **Run ID:** run1 
- :fontawesome-solid-user-group: **Participant:** MU_CS 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/7/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `490710ba1d074884a44fc0f43f2780f1` 
- :material-text: **Run description:** This run essentially uses the OpenAI ada model to retrieve recommendations between the given topics and trials. 

---
#### SPLADEv2 
[**`Participants`**](./participants.md#csiro-uq-ielab) 

- :material-rename: **Run ID:** SPLADEv2 
- :fontawesome-solid-user-group: **Participant:** CSIRO-UQ-ielab 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/30/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `ce3467c44819183c0de8ac1010eaca88` 
- :material-text: **Run description:** A BERT-based SPLADE sparse retriever model train with multistage hard negative mining and synthetic data generated by gpt-3.5-turbo. 

---
#### stage1ema 
[**`Participants`**](./participants.md#ema3) 

- :material-rename: **Run ID:** stage1ema 
- :fontawesome-solid-user-group: **Participant:** EMA3 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/2/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `82c5bd148a13c86374ff8cf7ddaa7b81` 
- :material-text: **Run description:** This run uses scispacy to idenitify medical terms. It uses the UMLS API provided by the National Library of Medicine.  

---
#### tugas_nlp_2 
[**`Participants`**](./participants.md#tugas_nlp) 

- :material-rename: **Run ID:** tugas_nlp_2 
- :fontawesome-solid-user-group: **Participant:** tugas_nlp 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/31/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `17bb7cea157709f5404a2c5874e32de8` 
- :material-text: **Run description:** In this run, we used BM25 with RM3 and RRF (with sintetic queries generated by doc2query-t5-large-msmarco) to generate a list of top 10000 documents for each topic, and then used Llama-2-13b-chat-hf with 4-bit quantization to generate relevance judgements to re-rank the top10000, adapting prior work done by TrialGPT. The LLaMa-2 model was not trained due to hardware limitations, so the settings were the base settings and weights meta-llama offers in huggingface.    

---
#### v1tmurun 
[**`Participants`**](./participants.md#v-torontomu) 

- :material-rename: **Run ID:** v1tmurun 
- :fontawesome-solid-user-group: **Participant:** V-TorontoMU 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/2/2023 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `ccdbf8fd2fb3ef231c1e7c1a5b8f3595` 
- :material-text: **Run description:** Doc2Vec 

---
#### v2tmurun 
[**`Participants`**](./participants.md#v-torontomu) 

- :material-rename: **Run ID:** v2tmurun 
- :fontawesome-solid-user-group: **Participant:** V-TorontoMU 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/2/2023 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `6b5dda53bb35b476772e32ffb8fe4bde` 
- :material-text: **Run description:** Sentence Transformer - RoBERTa Large 

---
#### v3tmurun 
[**`Participants`**](./participants.md#v-torontomu) 

- :material-rename: **Run ID:** v3tmurun 
- :fontawesome-solid-user-group: **Participant:** V-TorontoMU 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/2/2023 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `2d5a421c3f0a3ae54f741f96f333b267` 
- :material-text: **Run description:** Sentence Transformer - RoBERTa Large 

---
#### v4tmurun 
[**`Participants`**](./participants.md#v-torontomu) 

- :material-rename: **Run ID:** v4tmurun 
- :fontawesome-solid-user-group: **Participant:** V-TorontoMU 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/2/2023 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `8751e2ef93db51ebb3335273176f7e34` 
- :material-text: **Run description:** Doc2Vec 

---
#### wrsema3 
[**`Participants`**](./participants.md#ema3) 

- :material-rename: **Run ID:** wrsema3 
- :fontawesome-solid-user-group: **Participant:** EMA3 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/2/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `b34ecf9b7e63fc4e4881b9c408545e79` 
- :material-text: **Run description:** This run uses a sentence encoder to encode the itemized inclusion and exclusion criteria. The scoring function weighs the exclusion criteria more than the inclusion criteria for computing relevance scores.  

---
#### yorku23a 
[**`Participants`**](./participants.md#yorku23) 

- :material-rename: **Run ID:** yorku23a 
- :fontawesome-solid-user-group: **Participant:** yorku23 
- :material-format-text: **Track:** Clinical Trials 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/30/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `3c3125ab91b07d7e52439ca91af7ad84` 
- :material-text: **Run description:** Dense 

---
