# Runs - Round 2 2020 

#### allFiltering 
[**`Results`**](./results.md#allfiltering) | [**`Participants`**](./participants.md#irlabku) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/allFiltering) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/allFiltering.pdf) 

- :material-rename: **Run ID:** allFiltering 
- :fontawesome-solid-user-group: **Participant:** IRLabKU 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `0cf1a8e9b5e0bb4cbdfb4576c38764db` 
- :material-text: **Run description:** --We create 3 indexes: 1) Based on title+abstract, 2) Based on full-text, and 3) Based on title+abstract+paragraph (a document is split into para1, para2, ..., paraK, and we create K+1 documents of the form title+abstract, title+abstract+para1, title+abstract+para2. --We create 4 different types of queries: 1) Query + named_entitities(question), 2) Query + named_entitities(question) + named_entitities(narrative), 3) Question + named_entitities(query), and 4) Question + named_entitities(query) + named_entitities(narrative) --For each query type we create 4 runs (default BM25 + default RM3): 1) We search in index of title+abstract, 2) We search in index of full-text, 3) We search in index of title+abstract+paragraph (where we only keep the first occurrence of a document and delete the following duplicates), and 4) We search in index of title+abstract+paragraph (where we don't remove the duplicates) Finally, based on these 4 runs, we use reciprocal rank fusion to get 1 run. --Now, we have 4 fusion run, which we use to create a final reciprocal rank fusion (Fusion of Fusions). We also create a fusion of the 16 runs without an intermediate fusion (Fusion of Runs).  --Finally, we use reciprocal rank fusion between the 27 automatic runs, that did not contribute to the pooling, from round 1, as well as our own 2 fusion runs.  

---
#### ASU_MDLabs_STS_qn 
[**`Results`**](./results.md#asu_mdlabs_sts_qn) | [**`Participants`**](./participants.md#asu_biomedical) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ASU_MDLabs_STS_qn) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ASU_MDLabs_STS_qn.pdf) 

- :material-rename: **Run ID:** ASU_MDLabs_STS_qn 
- :fontawesome-solid-user-group: **Participant:** ASU_biomedical 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `f3b6d657d62bfdb32187e8516de6f896` 
- :material-text: **Run description:** This submission is made by utilizing a BERT model and internet scraping. Google Scholar is scraped with the provided queries and then a score is given not each hit that matches the CORD19 dataset. Then SciBERT model is trained on sentence similarity between the documents and the query. In this run, we have used query+narrative for the similarity. 

---
#### ASU_MDLabs_STS_qq 
[**`Results`**](./results.md#asu_mdlabs_sts_qq) | [**`Participants`**](./participants.md#asu_biomedical) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ASU_MDLabs_STS_qq) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ASU_MDLabs_STS_qq.pdf) 

- :material-rename: **Run ID:** ASU_MDLabs_STS_qq 
- :fontawesome-solid-user-group: **Participant:** ASU_biomedical 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `02f9ccf2150958cbce301460f8ebe400` 
- :material-text: **Run description:** This submission is made by utilizing a BERT model and internet scraping. Google Scholar is scraped with the provided queries and then a score is given not each hit that matches the CORD19 dataset. Then SciBERT model is trained on sentence similarity between the documents and the query. In this run, we have used query+question for the similarity. 

---
#### ASU_MDLabs_STS_qqn 
[**`Results`**](./results.md#asu_mdlabs_sts_qqn) | [**`Participants`**](./participants.md#asu_biomedical) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ASU_MDLabs_STS_qqn) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ASU_MDLabs_STS_qqn.pdf) 

- :material-rename: **Run ID:** ASU_MDLabs_STS_qqn 
- :fontawesome-solid-user-group: **Participant:** ASU_biomedical 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `4f88655b49e5b47f74532d68686063a5` 
- :material-text: **Run description:** This submission is made by utilizing a BERT model and internet scraping. Google Scholar is scraped with the provided queries and then a score is given not each hit that matches the CORD19 dataset. Then SciBERT model is trained on sentence similarity between the documents and the query. In this run, we have used query+question+narrative for the similarity. 

---
#### BBGhelani1 
[**`Results`**](./results.md#bbghelani1) | [**`Participants`**](./participants.md#bbghelani) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/BBGhelani1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/BBGhelani1.pdf) 

- :material-rename: **Run ID:** BBGhelani1 
- :fontawesome-solid-user-group: **Participant:** BBGhelani 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `aed6b9beb1e0921169e9401b07a75f0c` 
- :material-text: **Run description:** The run is generated using a human in the loop active learning approach. HiCAL[2] is used for the task. It uses Continuous active learning[1] and a solr+bm25 search interface. The active learning model for each topic was seeded using judgments made by us in Round 1 and NIST qrel. For topics 1-30, at most 5 minutes were spent per topic. For topic 31-35, at most 15 minutes were spent per topic. [1] Gordon V. Cormack and Maura R. Grossman. Evaluation of machine-learning proto-cols for technology-assisted review in electronic discovery.  InProceedings of the 37thInternational ACM SIGIR Conference on Research and Development in InformationRetrieval, pages 153--162. ACM, 2014. [2] https://github.com/hical/HiCAL 

---
#### BBGhelani2 
[**`Results`**](./results.md#bbghelani2) | [**`Participants`**](./participants.md#bbghelani) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/BBGhelani2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/BBGhelani2.pdf) 

- :material-rename: **Run ID:** BBGhelani2 
- :fontawesome-solid-user-group: **Participant:** BBGhelani 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `9ce81393cd055d846151387fbe3e4bb0` 
- :material-text: **Run description:** The run is generated using a human in the loop active learning approach. HiCAL[2] is used for the task. It uses Continuous active learning[1] and a solr+bm25 search interface. The active learning model for each topic was seeded using judgments made by us in Round 1 and NIST qrel. For topics 1-30, at most 5 minutes were spent per topic. For topic 31-35, at most 15 minutes were spent per topic. [1] Gordon V. Cormack and Maura R. Grossman. Evaluation of machine-learning proto-cols for technology-assisted review in electronic discovery.  InProceedings of the 37thInternational ACM SIGIR Conference on Research and Development in InformationRetrieval, pages 153--162. ACM, 2014. [2] https://github.com/hical/HiCAL 

---
#### BBGhelani3 
[**`Results`**](./results.md#bbghelani3) | [**`Participants`**](./participants.md#bbghelani) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/BBGhelani3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/BBGhelani3.pdf) 

- :material-rename: **Run ID:** BBGhelani3 
- :fontawesome-solid-user-group: **Participant:** BBGhelani 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `37b3bab44d0b3521fea46f5a21bdc3cc` 
- :material-text: **Run description:** The run is generated using a human in the loop active learning approach. HiCAL[2] is used for the task. It uses Continuous active learning[1] and a solr+bm25 search interface. The active learning model for each topic was seeded using judgments made by us in Round 1 and NIST qrel. For topics 1-30, at most 5 minutes were spent per topic. For topic 31-35, at most 15 minutes were spent per topic. [1] Gordon V. Cormack and Maura R. Grossman. Evaluation of machine-learning proto-cols for technology-assisted review in electronic discovery.  InProceedings of the 37thInternational ACM SIGIR Conference on Research and Development in InformationRetrieval, pages 153--162. ACM, 2014. [2] https://github.com/hical/HiCAL 

---
#### Bioinfo-run1 
[**`Results`**](./results.md#bioinfo-run1) | [**`Participants`**](./participants.md#bioinformaticsua) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/Bioinfo-run1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/Bioinfo-run1.pdf) 

- :material-rename: **Run ID:** Bioinfo-run1 
- :fontawesome-solid-user-group: **Participant:** BioinformaticsUA 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `0268c8bc62d31fbb6c7bfe7d2d92a28a` 
- :material-text: **Run description:** This run corresponds to the results of a system that was tunned for the BioASQ challenge (a more broad biomedical Adhoc retrieval challenge). So this submission tries to explore the possible similarity between the data domains in order to train a neural ranking model. The system uses a standard BM25 + Neural ranking model. In the retrieval were considered only documents that have title+abstract to be more similar to the BioASQ data. The neural ranking is built upon the DeepRank model and a more complete description can be found here [1]. The word embeddings were computed on CORD+Pubmed corpus using word2vec. For each topic, the field "question" was used to express the information need. REFs: [1] T. Almeida and S. Matos, "Calling Attention to Passages for Biomedical Question Answering," in Advances in Information Retrieval, 2020, pp. 69--77. 

---
#### Bioinfo-run2 
[**`Results`**](./results.md#bioinfo-run2) | [**`Participants`**](./participants.md#bioinformaticsua) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/Bioinfo-run2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/Bioinfo-run2.pdf) 

- :material-rename: **Run ID:** Bioinfo-run2 
- :fontawesome-solid-user-group: **Participant:** BioinformaticsUA 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `08a44ab12f20161117bce12bb5f054c7` 
- :material-text: **Run description:** The system uses a standard BM25 + Neural ranking model. In the retrieval were considered only documents that have title+abstract, the model was trained on BioASQ 7b and finetunned on qrels do round1. The neural ranking is built upon the DeepRank model and a more complete description can be found here [1]. The word embeddings were computed on CORD+Pubmed corpus using word2vec. For each topic, the field "question" was used to express the information need on rerank and for the bm25 was used the "UDEL" queries [2]. REFs: [1] T. Almeida and S. Matos, "Calling Attention to Passages for Biomedical Question Answering," in Advances in Information Retrieval, 2020, pp. 69--77. [2] https://github.com/castorini/anserini/blob/master/src/main/resources/topics-and-qrels/topics.covid-round2-udel.xml 

---
#### Bioinfo-run3 
[**`Results`**](./results.md#bioinfo-run3) | [**`Participants`**](./participants.md#bioinformaticsua) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/Bioinfo-run3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/Bioinfo-run3.pdf) 

- :material-rename: **Run ID:** Bioinfo-run3 
- :fontawesome-solid-user-group: **Participant:** BioinformaticsUA 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `7834bb103e78d0808490192b7e4445cd` 
- :material-text: **Run description:** 5Fold (qrels) ensemble of the following system: The system uses a standard BM25 + Neural ranking model. In the retrieval were considered only documents that have title+abstract, the model was trained on BioASQ 7b and finetunned on qrels do round1. The neural ranking is built upon the DeepRank model and a more complete description can be found here [1]. The word embeddings were computed on CORD+Pubmed corpus using word2vec. For each topic, the field "question" was used to express the information need on rerank and for the bm25 was used the "UDEL" queries [2]. REFs: [1] T. Almeida and S. Matos, "Calling Attention to Passages for Biomedical Question Answering," in Advances in Information Retrieval, 2020, pp. 69--77. [2] https://github.com/castorini/anserini/blob/master/src/main/resources/topics-and-qrels/topics.covid-round2-udel.xml 

---
#### BITEM_BL 
[**`Results`**](./results.md#bitem_bl) | [**`Participants`**](./participants.md#bitem) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/BITEM_BL) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/BITEM_BL.pdf) 

- :material-rename: **Run ID:** BITEM_BL 
- :fontawesome-solid-user-group: **Participant:** BITEM 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `d2b10de098806c3436950c5f5cab3a0f` 
- :material-text: **Run description:** Lucene Elasticsearch engine, Okapi BM25 Topic description -> all fields used (query + question + narrative) -> token filtering based on PMC Document Frequencies in order to discard common words -> tokens boosted based on PMC Document Frequencies -> for query field, add "query" (e.g. topic 1: coronavirus origin "coronavirus origin") Normalization -> documents and queries normalized (text mining) with a dedicated COVID vocabulary (link ?) Reranking -> boost (*2) documents with pubyear = 2020 (60% of qrel while 10% of collection) 

---
#### BITEM_DC_comb 
[**`Results`**](./results.md#bitem_dc_comb) | [**`Participants`**](./participants.md#bitem) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/BITEM_DC_comb) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/BITEM_DC_comb.pdf) 

- :material-rename: **Run ID:** BITEM_DC_comb 
- :fontawesome-solid-user-group: **Participant:** BITEM 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `e90ce615d5f377b096c7506bc2d9489e` 
- :material-text: **Run description:** Automatic topics filtering to discard common words and then normalization (translation with our covid terminologies codes) ; Annotations of cord-19 corpus with our covid terminologies (COVoc) ; ElasticSearch queries with boost depending topic's field (Query: 3, Question: 2, Narrative: 1) ;  Linear combination (cord-19 documents + (0.1*metadata)). 

---
#### bm25_safir_nvsm_rrf 
[**`Results`**](./results.md#bm25_safir_nvsm_rrf) | [**`Participants`**](./participants.md#ims_unipd) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/bm25_safir_nvsm_rrf) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/bm25_safir_nvsm_rrf.pdf) 

- :material-rename: **Run ID:** bm25_safir_nvsm_rrf 
- :fontawesome-solid-user-group: **Participant:** ims_unipd 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `9ac2df7151206428e68df68dd2b0173c` 
- :material-text: **Run description:** We adopt SAFIR (three models) + RM3, NVSM + RM3, and BM25 + RM3. Then we perform RRF to combine the five runs. 

---
#### bm25_safir_rrf 
[**`Results`**](./results.md#bm25_safir_rrf) | [**`Participants`**](./participants.md#ims_unipd) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/bm25_safir_rrf) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/bm25_safir_rrf.pdf) 

- :material-rename: **Run ID:** bm25_safir_rrf 
- :fontawesome-solid-user-group: **Participant:** ims_unipd 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `4e5dd00f08ae8b8443ff7abb865bf149` 
- :material-text: **Run description:** We adopt SAFIR (three models) + RM3 and BM25 + RM3. Then we performed RRF to combine the four runs. 

---
#### bm25_safir_s01p_rrf 
[**`Results`**](./results.md#bm25_safir_s01p_rrf) | [**`Participants`**](./participants.md#ims_unipd) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/bm25_safir_s01p_rrf) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/bm25_safir_s01p_rrf.pdf) 

- :material-rename: **Run ID:** bm25_safir_s01p_rrf 
- :fontawesome-solid-user-group: **Participant:** ims_unipd 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `86ae8b191e74826cd00b014d5ed75b24` 
- :material-text: **Run description:** We adopt SAFIR + RM3 and BM25 + RM3. Then we performed RRF to combine the two runs. 

---
#### bm25_syn_0.8_2.6 
[**`Results`**](./results.md#bm25_syn_08_26) | [**`Participants`**](./participants.md#risklick) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/bm25_syn_0.8_2.6) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/bm25_syn_0.8_2.6.pdf) 

- :material-rename: **Run ID:** bm25_syn_0.8_2.6 
- :fontawesome-solid-user-group: **Participant:** risklick 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `9f39dae6ba76ea345ad1820ee0145216` 
- :material-text: **Run description:** We used the BM25 model and considered synonyms from some ontology. 

---
#### CincyMedIR-11 
[**`Results`**](./results.md#cincymedir-11) | [**`Participants`**](./participants.md#cincymedir) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/CincyMedIR-11) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/CincyMedIR-11.pdf) 

- :material-rename: **Run ID:** CincyMedIR-11 
- :fontawesome-solid-user-group: **Participant:** CincyMedIR 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `306439693a09577a72c5a21bd9c396b3` 
- :material-text: **Run description:** Query expanded using synonyms from Lexigram's API; Elasticsearch used as the search engine and re-ranking of documents post initial retrieval according to relevance from round 1. 

---
#### CincyMedIR-4 
[**`Results`**](./results.md#cincymedir-4) | [**`Participants`**](./participants.md#cincymedir) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/CincyMedIR-4) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/CincyMedIR-4.pdf) 

- :material-rename: **Run ID:** CincyMedIR-4 
- :fontawesome-solid-user-group: **Participant:** CincyMedIR 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `b5484f6080edebcb43a87c6321ca6e89` 
- :material-text: **Run description:** Query expanded using synonyms from Lexigram's API; Elasticsearch used as the search engine and re-ranking of documents post initial retrieval according to relevance from round 1. 

---
#### CincyMedIR-6 
[**`Results`**](./results.md#cincymedir-6) | [**`Participants`**](./participants.md#cincymedir) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/CincyMedIR-6) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/CincyMedIR-6.pdf) 

- :material-rename: **Run ID:** CincyMedIR-6 
- :fontawesome-solid-user-group: **Participant:** CincyMedIR 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `e190b836de5615710fa1dced74c6a94d` 
- :material-text: **Run description:** Query expanded using synonyms from Lexigram's API; Elasticsearch used as the search engine and re-ranking of documents post initial retrieval according to relevance from round 1. 

---
#### cogir-ibm-q-PolRnk 
[**`Results`**](./results.md#cogir-ibm-q-polrnk) | [**`Participants`**](./participants.md#cogir) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/cogir-ibm-q-PolRnk) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/cogir-ibm-q-PolRnk.pdf) 

- :material-rename: **Run ID:** cogir-ibm-q-PolRnk 
- :fontawesome-solid-user-group: **Participant:** CogIR 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/11/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `f72b53ecce7d27db346d1c881f02dca8` 
- :material-text: **Run description:** Indexing:  Documents were indexed using Lucene version 7.1.0 with EnglishAnalyzer and InQuery stop list.  Three fields were kept per document: title, abstract and content. Missing article title or abstract were augmented using  the article's content (when available).  * Title augmentation: first abstract's text paragraph (from json file).  * Asbtact augmentation:   + take the longer abstract among metadata and article's JSON   + for missing abstract: augmented it with either of the first 500 chars of the article's introduction/summary/conclusions section (in this preference order),   + otherwise: if content exists: take the first 500 chars of the content.  Articles with no title or abstract were discarded.  Total index size: 50309 docs (#Longer abstract taken: 9099, #Abstracts augmented: 844, #Titles augmented: 38).  Retrieval: Retrieval was performed in two main phases (baseline rankers and fusion).  The first phase was used to derive an intial pool of potential candidates.  Here, the topic's question was used as the searched query.  First baseline retrieval phase used three different rankers: 1. Lucene-based retrieval using 4 Lucene similarities:  * AxiomaticF1LOG(default) * DFRSimilarity(BasicModelIF,AfterEffectB,NormalizationH3) * LMDirichletSimilarity(mu=200) * BM25Similarity(default) For each similarity the top-1000 documents were retrieved using a multi-field document retrieval: title^0.03,abstract^0.05,content^1. Field boosts were tuned using BM25Similarity(default).  Various ranked lists were then first fused using CombSUM without score normalization.  Following [1] we applied the pseudo-relevance-feedback PoolRank method with CombSUM fusion scores as prior-scores.  For pseudo-relevance, we used RM1 [2] with PRF-size=20, Dir-smooth=200, clip size=100 and logistic interplolation (lambda=0.01) tuned  using BM25Similarity(default). Following [3] the pool was further reranked using the MaxPsg method (passages were extracted using sliding window of 200 chars with 10% overlap, BM25(K1=0.8,b=0.3) scoring),  tuned using BM25Similarity(default). The list of 1000 docs for each query (from the first ranker above), were then re-ranked using the following two fine-tuned BERT models [4]:   2. BERT-Q-a  Documents' (title, abstract) pairs were used in the collection as a weak-supervision to fine-tune SciBERT pre-trained model [5] for matching titles to abstracts.  Then at run time, given a topic with 1000 docs, document abstracts were scored by matching the topic's question to each abstract using the fine-tuned BERT-Q-a model. 3. BERT-Q-q Similarly, documents' (title, abstract) pairs were used in the collection as a weak-supervision to generate title paraphrases [4].  Those paraphrases were then used to fine-tune another SciBERT model for matching titles to their paraphrases.  Then at run time, given a topic with 1000 docs, their titles were scored by matching the topic's question to each title using the fine-tuned BERT-Q-q model. Second fusion phase was applied to combine the three baseline rankers. Following [4], we applied the pseudo-relevance feedback PoolRank method with Weighted CombSUM(weights=[3,2,1],max-min normalization)  using again RM1 model (PRF-size=3, Dir-smooth=200, clip size=100 and logistic interplolation (lambda=0.01), tuned  using BM25Similarity(default). [1] H. Roitman, Utilizing Pseudo-Relevance Feedback in Fusion-based Retrieval, Proc. of ICTIR'2018 [2] V. Lavrenko, Bruce W. Croft, Relevance-based Language Models, Proc. of SIGIR'2001 [3] H. Roitman, Y. Mass, Utilizing Passages in Fusion-based Document Retrieval, Proc. of ICTIR'2019 [4] Y. Mass, B. Carmeli, H. Roitman, D. Konopnicki, Unsupervised FAQ Retrieval with Question Generation and BERT, to appear in ACL'2020 [5] Iz Beltagy, Kyle Lo, Arman Cohan, SciBERT: A Pretrained Language Model for Scientific Text, CoRR abs/1903.10676 (2019)  

---
#### cogir-ibm-qQ-combs 
[**`Results`**](./results.md#cogir-ibm-qq-combs) | [**`Participants`**](./participants.md#cogir) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/cogir-ibm-qQ-combs) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/cogir-ibm-qQ-combs.pdf) 

- :material-rename: **Run ID:** cogir-ibm-qQ-combs 
- :fontawesome-solid-user-group: **Participant:** CogIR 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/11/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `f85c9d0918d0732f91ff227afdc92b8e` 
- :material-text: **Run description:** Indexing:  Documents were indexed using Lucene version 7.1.0 with EnglishAnalyzer and InQuery stop list.  We kept three fields per document: title, abstract and content. We performed data augmentation for missing article title or abstract using  the article's content (when exists). Title augmentation: first abstract's text paragraph (from json file).  Asbtact augmentation: If article's json file contains a longer abstract, then we index it;otherwise we used the one in metadata.  If no abstract then we augmented it with either the first 500 chars of the article's introduction/summary/conclusions section (in this preference order), otherwise, if content exists: first 500 chars of the content. Articles with no title or abstract were discarded.  Total index size: 50309 docs (#Longer abstract taken: 9099, #Abstracts augmented: 844, #Titles augmented: 38).  Retrieval: Retrieval was performed in two main phases (baseline rankers and fusion).  The first phase was used to derive an intial pool of potential candidates.  Here, the topic's query+question parts were used as the searched query.  First baseline retrieval phase used three different rankers: 1. Lucene-based retrieval using 4 Lucene similarities:  * AxiomaticF1LOG(default) * DFRSimilarity(BasicModelIF,AfterEffectB,NormalizationH3) * LMDirichletSimilarity(mu=200) * BM25Similarity(default) For each similarity the top-1000 documents were retrieved using a multi-field document retrieval: title^0.03,abstract^0.05,content^1. Field boosts were tuned using BM25Similarity(default).  Various ranked lists were then first fused using CombSUM without score normalization.  Following [1] we applied the pseudo-relevance-feedback PoolRank method with CombSUM fusion scores as prior-scores.  For pseudo-relevance, we used RM1 [2] with PRF-size=20, Dir-smooth=200, clip size=100 and logistic interplolation (lambda=0.01) tuned  using BM25Similarity(default). Following [3] the pool was further reranked using the MaxPsg method (passages were extracted using sliding window of 200 chars with 10% overlap, BM25(K1=0.8,b=0.3) scoring),  tuned using BM25Similarity(default). The list of 1000 docs for each query (from the first ranker above), were then re-ranked using the following two fine-tuned BERT models [4]:   2. BERT-Q-a  Documents' (title, abstract) pairs were used in the collection as a weak-supervision to fine-tune SciBERT pre-trained model [5] for matching titles to abstracts.  Then at run time, given a topic with 1000 docs, document abstracts were scored by matching the topic's question to each abstract using the fine-tuned BERT-Q-a model. 3. BERT-Q-q Similarly, documents' (title, abstract) pairs were used in the collection as a weak-supervision to generate title paraphrases [4].  Those paraphrases were then used to fine-tune another SciBERT model for matching titles to their paraphrases.  Then at run time, given a topic with 1000 docs, their titles were scored by matching the topic's question to each title using the fine-tuned BERT-Q-q model. Second fusion phase was applied to combine the three baseline rankers. Following [4], we applied the pseudo-relevance feedback PoolRank method with Weighted CombSUM(weights=[3,2,1],max-min normalization)  using again RM1 model (PRF-size=3, Dir-smooth=200, clip size=100 and logistic interplolation (lambda=0.01), tuned  using BM25Similarity(default). [1] H. Roitman, Utilizing Pseudo-Relevance Feedback in Fusion-based Retrieval, Proc. of ICTIR'2018 [2] V. Lavrenko, Bruce W. Croft, Relevance-based Language Models, Proc. of SIGIR'2001 [3] H. Roitman, Y. Mass, Utilizing Passages in Fusion-based Document Retrieval, Proc. of ICTIR'2019 [4] Y. Mass, B. Carmeli, H. Roitman, D. Konopnicki, Unsupervised FAQ Retrieval with Question Generation and BERT, to appear in ACL'2020 [5] Iz Beltagy, Kyle Lo, Arman Cohan, SciBERT: A Pretrained Language Model for Scientific Text, CoRR abs/1903.10676 (2019) Second fusion phase was applied to combine the three baseline rankers using Weighted CombSUM(weights=[3,2,1],max-min normalization). [1] H. Roitman, Utilizing Pseudo-Relevance Feedback in Fusion-based Retrieval, Proc. of ICTIR'2018 [2] V. Lavrenko, Bruce W. Croft, Relevance-based Language Models, Proc. of SIGIR'2001 [3] H. Roitman, Y. Mass, Utilizing Passages in Fusion-based Document Retrieval, Proc. of ICTIR'2019 [4] Y. Mass, B. Carmeli, H. Roitman, D. Konopnicki, Unsupervised FAQ Retrieval with Question Generation and BERT, to appear in ACL'2020  

---
#### cogir-ibm-qQ-PolRnk 
[**`Results`**](./results.md#cogir-ibm-qq-polrnk) | [**`Participants`**](./participants.md#cogir) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/cogir-ibm-qQ-PolRnk) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/cogir-ibm-qQ-PolRnk.pdf) 

- :material-rename: **Run ID:** cogir-ibm-qQ-PolRnk 
- :fontawesome-solid-user-group: **Participant:** CogIR 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/11/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `ae5209b8e98a80651d3eac21720cde1c` 
- :material-text: **Run description:** Indexing:  Documents were indexed using Lucene version 7.1.0 with EnglishAnalyzer and InQuery stop list.  Three fields were kept per document: title, abstract and content. Missing article title or abstract were augmented using  the article's content (when available).  * Title augmentation: first abstract's text paragraph (from json file).  * Asbtact augmentation:   + take the longer abstract among metadata and article's JSON   + for missing abstract: augmented it with either of the first 500 chars of the article's introduction/summary/conclusions section (in this preference order),   + otherwise: if content exists: take the first 500 chars of the content.  Articles with no title or abstract were discarded.  Total index size: 50309 docs (#Longer abstract taken: 9099, #Abstracts augmented: 844, #Titles augmented: 38).  Retrieval: Retrieval was performed in two main phases (baseline rankers and fusion).  The first phase was used to derive an intial pool of potential candidates.  Here, the topic's query+question parts were used as the searched query.  First baseline retrieval phase used three different rankers: 1. Lucene-based retrieval using 4 Lucene similarities:  * AxiomaticF1LOG(default) * DFRSimilarity(BasicModelIF,AfterEffectB,NormalizationH3) * LMDirichletSimilarity(mu=200) * BM25Similarity(default) For each similarity the top-1000 documents were retrieved using a multi-field document retrieval: title^0.03,abstract^0.05,content^1. Field boosts were tuned using BM25Similarity(default).  Various ranked lists were then first fused using CombSUM without score normalization.  Following [1] we applied the pseudo-relevance-feedback PoolRank method with CombSUM fusion scores as prior-scores.  For pseudo-relevance, we used RM1 [2] with PRF-size=20, Dir-smooth=200, clip size=100 and logistic interplolation (lambda=0.01) tuned  using BM25Similarity(default). Following [3] the pool was further reranked using the MaxPsg method (passages were extracted using sliding window of 200 chars with 10% overlap, BM25(K1=0.8,b=0.3) scoring),  tuned using BM25Similarity(default). The list of 1000 docs for each query (from the first ranker above), were then re-ranked using the following two fine-tuned BERT models [4]:   2. BERT-Q-a  Documents' (title, abstract) pairs were used in the collection as a weak-supervision to fine-tune SciBERT pre-trained model [5] for matching titles to abstracts.  Then at run time, given a topic with 1000 docs, document abstracts were scored by matching the topic's question to each abstract using the fine-tuned BERT-Q-a model. 3. BERT-Q-q Similarly, documents' (title, abstract) pairs were used in the collection as a weak-supervision to generate title paraphrases [4].  Those paraphrases were then used to fine-tune another SciBERT model for matching titles to their paraphrases.  Then at run time, given a topic with 1000 docs, their titles were scored by matching the topic's question to each title using the fine-tuned BERT-Q-q model. Second fusion phase was applied to combine the three baseline rankers. Following [4], we applied the pseudo-relevance feedback PoolRank method with Weighted CombSUM(weights=[3,2,1],max-min normalization)  using again RM1 model (PRF-size=3, Dir-smooth=200, clip size=100 and logistic interplolation (lambda=0.01), tuned  using BM25Similarity(default). [1] H. Roitman, Utilizing Pseudo-Relevance Feedback in Fusion-based Retrieval, Proc. of ICTIR'2018 [2] V. Lavrenko, Bruce W. Croft, Relevance-based Language Models, Proc. of SIGIR'2001 [3] H. Roitman, Y. Mass, Utilizing Passages in Fusion-based Document Retrieval, Proc. of ICTIR'2019 [4] Y. Mass, B. Carmeli, H. Roitman, D. Konopnicki, Unsupervised FAQ Retrieval with Question Generation and BERT, to appear in ACL'2020 [5] Iz Beltagy, Kyle Lo, Arman Cohan, SciBERT: A Pretrained Language Model for Scientific Text, CoRR abs/1903.10676 (2019)  

---
#### combined 
[**`Results`**](./results.md#combined) | [**`Participants`**](./participants.md#risklick) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/combined) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/combined.pdf) 

- :material-rename: **Run ID:** combined 
- :fontawesome-solid-user-group: **Participant:** risklick 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `d48ea133bf24d4943125e1790e754c2d` 
- :material-text: **Run description:** An ensemble of several learning to rank runs. 

---
#### combined_bm25_dfr 
[**`Results`**](./results.md#combined_bm25_dfr) | [**`Participants`**](./participants.md#risklick) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/combined_bm25_dfr) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/combined_bm25_dfr.pdf) 

- :material-rename: **Run ID:** combined_bm25_dfr 
- :fontawesome-solid-user-group: **Participant:** risklick 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `a93999987a3f85d3edf5657dbb84eb59` 
- :material-text: **Run description:** Linear combination of BM25 and DFR models using a COVID-19 specific ontology for query expansion. 

---
#### COMBSUM 
[**`Results`**](./results.md#combsum) | [**`Participants`**](./participants.md#ub_bw) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/COMBSUM) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/COMBSUM.pdf) 

- :material-rename: **Run ID:** COMBSUM 
- :fontawesome-solid-user-group: **Participant:** UB_BW 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `32112df4519a2aaf7fb95fc8cbf34b24` 
- :material-text: **Run description:** We indexed only the title and the abstract using Terrier-v5.2. For the final document ranking, we deployed CombSUM to combine the results from two different systems. The first system used PL2 term weighting model while the second system used TF-IDF term weighting model. During retrieval, we used both the query and the question tags, which were then expanded with terms selected using the Bo1 model for query expansion.  

---
#### ContrastNLGSciBert 
[**`Results`**](./results.md#contrastnlgscibert) | [**`Participants`**](./participants.md#cmt) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ContrastNLGSciBert) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ContrastNLGSciBert.pdf) 

- :material-rename: **Run ID:** ContrastNLGSciBert 
- :fontawesome-solid-user-group: **Participant:** CMT 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `86f7d9d4296ed810512c69abbb36bee3` 
- :material-text: **Run description:** bm25.qgenv4-600-top30.teIn: anserini TREC-COVID R2 Retrieval #8 retrieval, med-marco + Contrastive NLG COVD Query trained zero-shot SciBERT 

---
#### cord19.vespa.ai-bm25 
[**`Results`**](./results.md#cord19vespaai-bm25) | [**`Participants`**](./participants.md#cord19vespaai) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/cord19.vespa.ai-bm25) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/cord19.vespa.ai-bm25.pdf) 

- :material-rename: **Run ID:** cord19.vespa.ai-bm25 
- :fontawesome-solid-user-group: **Participant:** cord19.vespa.ai 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `b6b4510b676e2422f801a4b252c71c74` 
- :material-text: **Run description:** Query retrieval using bag of words from entity extraction using spacy en_core_sci_lg extracted from query, question and narrative. Simple bm25 ranking over title, abstract, body_text and t5 summary of the abstract.   

---
#### cord19.vespa.ai-gbdt 
[**`Results`**](./results.md#cord19vespaai-gbdt) | [**`Participants`**](./participants.md#cord19vespaai) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/cord19.vespa.ai-gbdt) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/cord19.vespa.ai-gbdt.pdf) 

- :material-rename: **Run ID:** cord19.vespa.ai-gbdt 
- :fontawesome-solid-user-group: **Participant:** cord19.vespa.ai 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `cd39a1116cb46ddc4f2c14feed66afd1` 
- :material-text: **Run description:** Query retrieval using bag of words from entity extraction using spacy en_core_sci_lg extracted from query, question and narrative. No query expansion or synonym expansion. nlp = spacy.load("en_core_sci_lg") ents = nlp(query + ' ' + question + ' ' + narrative).ents query = ' '.join([str(e) for e in ents])  BM25 retrieval and re-ranking 1K from first-phase (BM25) using a trained a GBDT model using lightGBM (https://docs.vespa.ai/documentation/lightgbm.html). The model uses 153 features from Vespa, ranging from matching features like bm25 in fields to semantic similarity (sent-scibert) over title and abstract using Vespa's nearest neighbor search operator. Parameters used with lightGBM: params = {'objective': 'lambdarank', 'metric': 'ndcg', 'ndcg_eval_at': '5,10', 'eta':0.01, 'num_leaves': 16, 'label_gain':"0,3,5"} More details on the run and how to reproduce https://github.com/vespa-engine/cord-19/trec-covid 

---
#### covidex.fuse 
[**`Results`**](./results.md#covidexfuse) | [**`Participants`**](./participants.md#covidex) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/covidex.fuse) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/covidex.fuse.pdf) 

- :material-rename: **Run ID:** covidex.fuse 
- :fontawesome-solid-user-group: **Participant:** covidex 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `3ed850f5c4c462cb2d4f4a513a331c8c` 
- :material-text: **Run description:** Reciprocal rank fusion of covidex.t5 and covidex.sim 

---
#### covidex.sim 
[**`Results`**](./results.md#covidexsim) | [**`Participants`**](./participants.md#covidex) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/covidex.sim) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/covidex.sim.pdf) 

- :material-rename: **Run ID:** covidex.sim 
- :fontawesome-solid-user-group: **Participant:** covidex 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `3d533951e9cc742125a0c2978808b31d` 
- :material-text: **Run description:** Reciprocal rank fusion of top 100 nearest neighbors of all relevant articles based on SPECTER embeddings (Cohan et al., 2020) using hnsw.  

---
#### covidex.t5 
[**`Results`**](./results.md#covidext5) | [**`Participants`**](./participants.md#covidex) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/covidex.t5) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/covidex.t5.pdf) 

- :material-rename: **Run ID:** covidex.t5 
- :fontawesome-solid-user-group: **Participant:** covidex 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `ae0be41e3a964aa6c2fafc0eb2c3e417` 
- :material-text: **Run description:** Reciprocal rank fusion of two runs: Anserini r2.fusion1, reranked with medT5-3B;  Anserini r2.fusion2, reranked with medT5-3B; Anserini fusion baselines for round 2: https://github.com/castorini/anserini/blob/master/docs/experiments-covid.md medT5-3B: a T5-3B reranker fine-tuned on MS MARCO then fine-tuned (again) on MS MARCO medical subset (from MacAvaney et al., 2020, "SLEDGE") 

---
#### CSIROmed_RF_RR 
[**`Results`**](./results.md#csiromed_rf_rr) | [**`Participants`**](./participants.md#csiromed) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/CSIROmed_RF_RR) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/CSIROmed_RF_RR.pdf) 

- :material-rename: **Run ID:** CSIROmed_RF_RR 
- :fontawesome-solid-user-group: **Participant:** CSIROmed 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `53cf3357445eb82b1964086f00482af1` 
- :material-text: **Run description:** DFR retrieval with relevance feedback query expansion (using rd1 judgements). Neural re-ranking of top 50 results done with a SciBERT variant with additional pretraining on target corpus and fine-tuning on a wide variety of biomedically themed TREC tasks. 

---
#### CSIROmedNIR 
[**`Results`**](./results.md#csiromednir) | [**`Participants`**](./participants.md#csiromed) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/CSIROmedNIR) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/CSIROmedNIR.pdf) 

- :material-rename: **Run ID:** CSIROmedNIR 
- :fontawesome-solid-user-group: **Participant:** CSIROmed 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `03f311c2384fb3ad25a378600cc46e27` 
- :material-text: **Run description:** Run CSIROMedNIR (automatic  no prior judgements): Neural Index with Cosine Similarity for retrieval over question, narrative and query and mean sentence-embeddings over abstract and title fields + BM25 score over fulltext. Same as round 1, except with better sentence segmentation using SciSpacy.  

---
#### CSIROmedNIRR 
[**`Results`**](./results.md#csiromednirr) | [**`Participants`**](./participants.md#csiromed) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/CSIROmedNIRR) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/CSIROmedNIRR.pdf) 

- :material-rename: **Run ID:** CSIROmedNIRR 
- :fontawesome-solid-user-group: **Participant:** CSIROmed 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `4096b3d305c563d5c36548f3c5f8f393` 
- :material-text: **Run description:** Neural Index with Cosine Similarity for retrieval over question, narrative and query for abstract and title fields + BM25 score over fulltext. The run is reranked using top 3 sentences scores from abstracts and full text.  

---
#### cu_dbmi_bm25 
[**`Results`**](./results.md#cu_dbmi_bm25) | [**`Participants`**](./participants.md#columbia_university_dbmi) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/cu_dbmi_bm25) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/cu_dbmi_bm25.pdf) 

- :material-rename: **Run ID:** cu_dbmi_bm25 
- :fontawesome-solid-user-group: **Participant:** columbia_university_dbmi 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `bdd3a87f34c406f8045f957f8e1d0930` 
- :material-text: **Run description:** Define COVID-19 key words To find COVID-19 related articles, we have defined a list of key words, the article is considered COVID-19 related if, any of these fields (title, abstract and full text) has any of the key word mentions. To make sure we have included all the key words for COVID-19, we trained a word2vec model on all full texts for phrase embeddings, then we tried to find all synonyms for COVID-19 from the word2vec model. We used an iterative approach, where we start looking for synonyms of one key word and add new phrases or words to the key word list, then use the newly found key word to repeat the same process until there is no new key word found anymore. Here is the list of synonyms for COVID-19. ['ncov', 'covid19', 'covid-19', 'sars cov2', 'sars cov-2', 'sars-cov-2', 'sars coronavirus 2', '2019-ncov', '2019 novel coronavirus', '2019-ncov sars', 'cov-2', 'cov2', 'novel coronvirus', 'coronavirus 2019-ncov'] Retrieve relevant articles for COVID-19 (BM25). We use a python library called whoosh as the indexing engine to enable fast search in title, abstract, and full_text across all documents. The standard tokenizer and the stemmer analyzer are applied during indexing. We retrieve relevant articles using the BM25 algorithm. https://whoosh.readthedocs.io/en/latest/index.html. We construct the search query for each topic using query, question and narrative fields provided in the topic document as the following demonstrates, 	*	lower case words, remove puncuation marks and stop words from query, question and narrative   	*	there are two parts defined in the construction of the seach query -- main query and subquery  	*	main query is constructed using the query and question fields following the pattern ((query) OR (question)),  the OR operator allows us to retrieve the maximum number of documents related to the main topic. The purpose of main query is to decide the "scope" of the search.   	*	subquery is constructed using narrative only, we run spaCy to extract the noun phrases and construct the subquery using an OR operator following the pattern (phrase_1 OR phrase_2 OR phrase_3 OR .... phrase_n), the purpose of subquery is to decide the priorities of the relevant documents. Obviously the more key words a document contains, the higher score it will receive.     *	main_query and subquery are assembled together using the AND operator ((query) OR (question)) AND ((query) OR (question) phrase_1 OR phrase_2 OR phrase_3 OR .... phrase_n). Noted that a copy of main query is also added to the subquery because we don't want to lose any relevant documents that do not contain any of the phrases extracted from the narrative. 

---
#### cu_dbmi_sent_embed 
[**`Results`**](./results.md#cu_dbmi_sent_embed) | [**`Participants`**](./participants.md#columbia_university_dbmi) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/cu_dbmi_sent_embed) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/cu_dbmi_sent_embed.pdf) 

- :material-rename: **Run ID:** cu_dbmi_sent_embed 
- :fontawesome-solid-user-group: **Participant:** columbia_university_dbmi 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `9be9b64da45f85752b0b10d26afd3743` 
- :material-text: **Run description:** Use cord 19 on tensorflow hub to calculate the similarities between the document and the query  

---
#### DD_bm25 
[**`Results`**](./results.md#dd_bm25) | [**`Participants`**](./participants.md#dy_xd) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/DD_bm25) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/DD_bm25.pdf) 

- :material-rename: **Run ID:** DD_bm25 
- :fontawesome-solid-user-group: **Participant:** DY_XD 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `7a98db35c67cbe80bd74d5cba5d7212a` 
- :material-text: **Run description:** BM25 

---
#### DD_prf 
[**`Results`**](./results.md#dd_prf) | [**`Participants`**](./participants.md#dy_xd) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/DD_prf) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/DD_prf.pdf) 

- :material-rename: **Run ID:** DD_prf 
- :fontawesome-solid-user-group: **Participant:** DY_XD 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `28feda05906a811c8c4057b65781a3e9` 
- :material-text: **Run description:** BM25 

---
#### DD_rm3 
[**`Results`**](./results.md#dd_rm3) | [**`Participants`**](./participants.md#dy_xd) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/DD_rm3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/DD_rm3.pdf) 

- :material-rename: **Run ID:** DD_rm3 
- :fontawesome-solid-user-group: **Participant:** DY_XD 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `c7e6d293db7a42e47c477653820ed95d` 
- :material-text: **Run description:** BM25, RM3 

---
#### elhuyar_rRnk_cbert1 
[**`Results`**](./results.md#elhuyar_rrnk_cbert1) | [**`Participants`**](./participants.md#elhuyar_nlp_team) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/elhuyar_rRnk_cbert1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/elhuyar_rRnk_cbert1.pdf) 

- :material-rename: **Run ID:** elhuyar_rRnk_cbert1 
- :fontawesome-solid-user-group: **Participant:** Elhuyar_NLP_team 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `2ffb0bd5a1843723da470065625aa913` 
- :material-text: **Run description:** We tackle this document retrieval task in two steps: a) a first ranking and b) re-ranking. In order to obtain the first ranking of relevant documents of the collection corresponding to the queries, we use a language modeling based information retrieval approach (Ponte & Croft, 1998) including pseudo relevance feedback. For that purpose, we used the Indri search engine (Strohman, 2005), which combines Bayesian networks with language models. Then, we make a re-ranking based on BERT following a strategy similar to the one proposed by Nogueira and Cho (2019). As we do not have a collection of query pairs and relevant abstracts for tuning BERT for this passage retrieval task, we simulate a training collection composed of titles and their corresponding abstracts from the COVID-19 Open Research dataset. Through this training collection we tuned the Clinical BERT model (Alsentzer et al., 2019) to the task of identifying relevant queries and abstracts. Indri and Tuned Clinical BERT scores are linearly combined and re-ranking is performed according to that new score. In this run we use weights of 0.9 and 0.1 for Indri and Clinical BERT scores respectively.  

---
#### elhuyar_rRnk_cbert2 
[**`Results`**](./results.md#elhuyar_rrnk_cbert2) | [**`Participants`**](./participants.md#elhuyar_nlp_team) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/elhuyar_rRnk_cbert2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/elhuyar_rRnk_cbert2.pdf) 

- :material-rename: **Run ID:** elhuyar_rRnk_cbert2 
- :fontawesome-solid-user-group: **Participant:** Elhuyar_NLP_team 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `69935e3da51154659ae59902d0955f03` 
- :material-text: **Run description:** We tackle this document retrieval task in two steps: a) a first ranking and b) re-ranking. In order to obtain the first ranking of relevant documents of the collection corresponding to the queries, we use a language modeling based information retrieval approach (Ponte & Croft, 1998) including pseudo relevance feedback. For that purpose, we used the Indri search engine (Strohman, 2005), which combines Bayesian networks with language models. Then, we make a re-ranking based on BERT following a strategy similar to the one proposed by Nogueira and Cho (2019). As we do not have a collection of query pairs and relevant abstracts for tuning BERT for this passage retrieval task, we simulate a training collection composed of titles and their corresponding abstracts from the COVID-19 Open Research dataset. Through this training collection we tuned the Clinical BERT model (Alsentzer et al., 2019) to the task of identifying relevant queries and abstracts. Indri and Tuned Clinical BERT scores are linearly combined and re-ranking is performed according to that new score. In this run we use weights of 0.8 and 0.2 for Indri and Clinical BERT scores respectively.  

---
#### elhuyar_rRnk_cbert3 
[**`Results`**](./results.md#elhuyar_rrnk_cbert3) | [**`Participants`**](./participants.md#elhuyar_nlp_team) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/elhuyar_rRnk_cbert3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/elhuyar_rRnk_cbert3.pdf) 

- :material-rename: **Run ID:** elhuyar_rRnk_cbert3 
- :fontawesome-solid-user-group: **Participant:** Elhuyar_NLP_team 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `74c510eac73bc67211cb66e30b92f0b5` 
- :material-text: **Run description:** We tackle this document retrieval task in two steps: a) a first ranking and b) re-ranking. In order to obtain the first ranking of relevant documents of the collection corresponding to the queries, we use a language modeling based information retrieval approach (Ponte & Croft, 1998) including pseudo relevance feedback. For that purpose, we used the Indri search engine (Strohman, 2005), which combines Bayesian networks with language models. Then, we make a re-ranking based on BERT following a strategy similar to the one proposed by Nogueira and Cho (2019). As we do not have a collection of query pairs and relevant abstracts for tuning BERT for this passage retrieval task, we simulate a training collection composed of titles and their corresponding abstracts from the COVID-19 Open Research dataset. Through this training collection we tuned the Clinical BERT model (Alsentzer et al., 2019) to the task of identifying relevant queries and abstracts. Indri and Tuned Clinical BERT scores are linearly combined and re-ranking is performed according to that new score. In this run we use weights of 0.85 and 0.15 for Indri and Clinical BERT scores respectively.  

---
#### Emory_IRLab_Run1 
[**`Results`**](./results.md#emory_irlab_run1) | [**`Participants`**](./participants.md#emory_irlab) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/Emory_IRLab_Run1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/Emory_IRLab_Run1.pdf) 

- :material-rename: **Run ID:** Emory_IRLab_Run1 
- :fontawesome-solid-user-group: **Participant:** Emory_IRLab 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `bc29a73a95fc8b03af0fbb924521e8a0` 
- :material-text: **Run description:** The initial results are retrieved with SLEDGE on the whole collections on history, with BM25 and query over fulltext, re-ranking using SciBERT on title and abstract with the question. Then the results are reranked with an inverse-time-decay mechanism and a time score is used as an additional term for reranking. The time score of documents published before 2010 is assigned as 0 and the subsequent published documents is assigned with a scaled score. The weight between the score from SLEDGE and time term is tuned for better performance based on the evaluation from round 1.  

---
#### Emory_IRLab_Run2 
[**`Results`**](./results.md#emory_irlab_run2) | [**`Participants`**](./participants.md#emory_irlab) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/Emory_IRLab_Run2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/Emory_IRLab_Run2.pdf) 

- :material-rename: **Run ID:** Emory_IRLab_Run2 
- :fontawesome-solid-user-group: **Participant:** Emory_IRLab 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `fced2f7a54cc84d7e29c174203d9706b` 
- :material-text: **Run description:** Simply rerank results based on Anserini and SLEDGE, used for comparing with the inverse-time-decay mechanism. 

---
#### ES_Baseline 
[**`Results`**](./results.md#es_baseline) | [**`Participants`**](./participants.md#covidsearch) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ES_Baseline) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ES_Baseline.pdf) 

- :material-rename: **Run ID:** ES_Baseline 
- :fontawesome-solid-user-group: **Participant:** CovidSearch 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `4dc2424245adbc570acb787a51269912` 
- :material-text: **Run description:** Baseline run 

---
#### ES_Covid 
[**`Results`**](./results.md#es_covid) | [**`Participants`**](./participants.md#covidsearch) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ES_Covid) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ES_Covid.pdf) 

- :material-rename: **Run ID:** ES_Covid 
- :fontawesome-solid-user-group: **Participant:** CovidSearch 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `93676bb04cae08bb66162baba6ce8d29` 
- :material-text: **Run description:** Covid Search run 

---
#### ES_Covid_ML 
[**`Results`**](./results.md#es_covid_ml) | [**`Participants`**](./participants.md#whitej_relevance) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ES_Covid_ML) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ES_Covid_ML.pdf) 

- :material-rename: **Run ID:** ES_Covid_ML 
- :fontawesome-solid-user-group: **Participant:** whitej_relevance 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `3a5ed61b2f05863e3b8c73ffb4e2bf40` 
- :material-text: **Run description:** Covid search with ML 

---
#### ES_Covid_Vector 
[**`Results`**](./results.md#es_covid_vector) | [**`Participants`**](./participants.md#whitej_relevance) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ES_Covid_Vector) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ES_Covid_Vector.pdf) 

- :material-rename: **Run ID:** ES_Covid_Vector 
- :fontawesome-solid-user-group: **Participant:** whitej_relevance 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `7cde556de90ebc962ec24ef59dcdd5dd` 
- :material-text: **Run description:** Covid vector 

---
#### ES_Defaults 
[**`Results`**](./results.md#es_defaults) | [**`Participants`**](./participants.md#covidsearch) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ES_Defaults) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ES_Defaults.pdf) 

- :material-rename: **Run ID:** ES_Defaults 
- :fontawesome-solid-user-group: **Participant:** CovidSearch 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `1cad0ec05de086208f462bc125f1fce7` 
- :material-text: **Run description:** Default run 

---
#### ES_QueryNarrative 
[**`Results`**](./results.md#es_querynarrative) | [**`Participants`**](./participants.md#whitej_relevance) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ES_QueryNarrative) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ES_QueryNarrative.pdf) 

- :material-rename: **Run ID:** ES_QueryNarrative 
- :fontawesome-solid-user-group: **Participant:** whitej_relevance 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `da1e13ab58f3652f39f7c54151b8b904` 
- :material-text: **Run description:** Covid search with narrative 

---
#### factum-dense-qa 
[**`Results`**](./results.md#factum-dense-qa) | [**`Participants`**](./participants.md#factum) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/factum-dense-qa) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/factum-dense-qa.pdf) 

- :material-rename: **Run ID:** factum-dense-qa 
- :fontawesome-solid-user-group: **Participant:** Factum 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `598383a1256c9567cc5ea64e6dba4c21` 
- :material-text: **Run description:** We used a siamese BERT encoder trained on NLI and QA data with sampled softmax loss to encode snippets of up to 5 sentences from the paragraphs of the articles. The final score is derived by a combination of cosine similarity of the dense vectors and the answer confidence (if found) by an extractive QA model (ALBERT-base trained on SQUAD 2.0). We removed articles published before December 2019. 

---
#### factum-hybrid 
[**`Results`**](./results.md#factum-hybrid) | [**`Participants`**](./participants.md#factum) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/factum-hybrid) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/factum-hybrid.pdf) 

- :material-rename: **Run ID:** factum-hybrid 
- :fontawesome-solid-user-group: **Participant:** Factum 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `20b20188cd438c51dee7db63520a7580` 
- :material-text: **Run description:** We used a siamese BERT encoder trained on NLI and QA data with sampled softmax loss to encode snippets of up to 5 sentences from the paragraphs of the articles. The final score is derived by a combination of cosine similarity of the dense vectors and BM25 score of the sparse vectors (unigrams + bigrams with lemmatisation). We removed articles published before December 2019. 

---
#### factum-hybrid-qa 
[**`Results`**](./results.md#factum-hybrid-qa) | [**`Participants`**](./participants.md#factum) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/factum-hybrid-qa) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/factum-hybrid-qa.pdf) 

- :material-rename: **Run ID:** factum-hybrid-qa 
- :fontawesome-solid-user-group: **Participant:** Factum 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `9c6de9b4878350c8d8fe5ad29c5a1f04` 
- :material-text: **Run description:** We used a siamese BERT encoder trained on NLI and QA data with sampled softmax loss to encode snippets of up to 5 sentences from the paragraphs of the articles. The final score is derived by a combination of cosine similarity of the dense vectors, BM25 score of the sparse vectors (unigrams + bigrams with lemmatisation) and the answer confidence (if found) by an extractive QA model (ALBERT-base trained on SQUAD 2.0). We removed articles published before December 2019. 

---
#### FullTxt_R2_Orig 
[**`Results`**](./results.md#fulltxt_r2_orig) | [**`Participants`**](./participants.md#ohsu) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/FullTxt_R2_Orig) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/FullTxt_R2_Orig.pdf) 

- :material-rename: **Run ID:** FullTxt_R2_Orig 
- :fontawesome-solid-user-group: **Participant:** OHSU 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `07de982ab95710b1b9584cdd7a3a61e4` 
- :material-text: **Run description:** Queries, questions, and narratives were tokenized to form a query for each topic. Additional manual review was performed for identification of relevant query terms. These queries were inputted into a Lucene full-text index was searched using Pyserini using BM25, LDA, and RM3 reranking to identify the top 1000 documents. 

---
#### FullTxt_R2_Time 
[**`Results`**](./results.md#fulltxt_r2_time) | [**`Participants`**](./participants.md#ohsu) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/FullTxt_R2_Time) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/FullTxt_R2_Time.pdf) 

- :material-rename: **Run ID:** FullTxt_R2_Time 
- :fontawesome-solid-user-group: **Participant:** OHSU 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `6fcc586df291667846a533d29e59a91c` 
- :material-text: **Run description:** Queries, questions, and narratives were tokenized and combined to form a query for each topic. Additional manual review was performed for identification of relevant query terms. These queries were inputted into a Lucene full-text index was searched using Pyserini using BM25, LDA, and RM3 reranking to identify the top 2000 documents. Results were filtered such that only documents published after 1/1/20 were considered for inclusion in the final 1000 documents per topic. 

---
#### fusionOfFusions 
[**`Results`**](./results.md#fusionoffusions) | [**`Participants`**](./participants.md#irlabku) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/fusionOfFusions) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/fusionOfFusions.pdf) 

- :material-rename: **Run ID:** fusionOfFusions 
- :fontawesome-solid-user-group: **Participant:** IRLabKU 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `5e462e86e8d2ce4076c044e127cf6414` 
- :material-text: **Run description:** --We create 3 indexes: 1) Based on title+abstract, 2) Based on full-text, and 3) Based on title+abstract+paragraph (a document is split into para1, para2, ..., paraK, and we create K+1 documents of the form title+abstract, title+abstract+para1, title+abstract+para2. --We create 4 different types of queries: 1) Query + named_entitities(question), 2) Query + named_entitities(question) + named_entitities(narrative), 3) Question + named_entitities(query), and 4) Question + named_entitities(query) + named_entitities(narrative) --For each query type we create 4 runs (default BM25 + default RM3): 1) We search in index of title+abstract, 2) We search in index of full-text, 3) We search in index of title+abstract+paragraph (where we only keep the first occurrence of a document and delete the following duplicates), and 4) We search in index of title+abstract+paragraph (where we don't remove the duplicates) Finally, based on these 4 runs, we use reciprocal rank fusion to get 1 run. --Now, we have 4 fusion run, which we use to create a final reciprocal rank fusion (Fusion of Fusions).  

---
#### GUIR_S2_run1 
[**`Results`**](./results.md#guir_s2_run1) | [**`Participants`**](./participants.md#guir_s2) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/GUIR_S2_run1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/GUIR_S2_run1.pdf) 

- :material-rename: **Run ID:** GUIR_S2_run1 
- :fontawesome-solid-user-group: **Participant:** GUIR_S2 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `602039ed5fcfb3012a87c3ad3ca90e88` 
- :material-text: **Run description:** Fusion of SciBERT over abstracts, SPECTER feedback (top 5 SciBERT documents), and BM25 (paragraph). SciBERT model trained on MS-MARCO. Tuning conducted on sample of COVID-QA queries. 

---
#### GUIR_S2_run2 
[**`Results`**](./results.md#guir_s2_run2) | [**`Participants`**](./participants.md#guir_s2) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/GUIR_S2_run2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/GUIR_S2_run2.pdf) 

- :material-rename: **Run ID:** GUIR_S2_run2 
- :fontawesome-solid-user-group: **Participant:** GUIR_S2 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `de8a958aa1a0b91c0e80350fa045b49e` 
- :material-text: **Run description:** Fusion of SciBERT over paragraphs, SPECTER feedback (top 5 SciBERT documents), and SPECTER query+document similarity. SciBERT model trained on MS-MARCO. Tuning conducted on judged documents from Round 1. 

---
#### GUIR_S2_run3 
[**`Results`**](./results.md#guir_s2_run3) | [**`Participants`**](./participants.md#guir_s2) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/GUIR_S2_run3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/GUIR_S2_run3.pdf) 

- :material-rename: **Run ID:** GUIR_S2_run3 
- :fontawesome-solid-user-group: **Participant:** GUIR_S2 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `2fb84f45a3c3ee177d90b3ce38ae2dc6` 
- :material-text: **Run description:** SciBERT over paragraphs, trained on medical subset of MS-MARCO. Tuning conducted on judged documents from Round 1. 

---
#### HKPU-Gos1-pPRF 
[**`Results`**](./results.md#hkpu-gos1-pprf) | [**`Participants`**](./participants.md#hkpu) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/HKPU-Gos1-pPRF) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/HKPU-Gos1-pPRF.pdf) 

- :material-rename: **Run ID:** HKPU-Gos1-pPRF 
- :fontawesome-solid-user-group: **Participant:** HKPU 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `a5fea0c738a1efb7af52b784c5d1a0fa` 
- :material-text: **Run description:** A ranking function of Goswami et al., IPM, 54, p454 (2017), with PRF on short queries. Passage-based retrieval. 

---
#### ielab-combmnz-meta 
[**`Results`**](./results.md#ielab-combmnz-meta) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ielab-combmnz-meta) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ielab-combmnz-meta.pdf) 

- :material-rename: **Run ID:** ielab-combmnz-meta 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `89c42cd9dd5c8df2494d2665d5b56707` 
- :material-text: **Run description:** CombMNZ rank fusion of the runs we submitted in Round 1 on a full-text index, in addition to several runs from APIs of search engines that support CORD: AEUB, Covidex, DISCOVID, Fatcat, Ludwig, and Vespa. 

---
#### ielab-rbp-baseline 
[**`Results`**](./results.md#ielab-rbp-baseline) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ielab-rbp-baseline) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ielab-rbp-baseline.pdf) 

- :material-rename: **Run ID:** ielab-rbp-baseline 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `3086fe3f465de3dfa31d89226a15fd59` 
- :material-text: **Run description:** RBP rank fusion of the runs we submitted in Round 1 on a full-text index. 

---
#### ielab-rbp-meta 
[**`Results`**](./results.md#ielab-rbp-meta) | [**`Participants`**](./participants.md#ielab) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ielab-rbp-meta) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ielab-rbp-meta.pdf) 

- :material-rename: **Run ID:** ielab-rbp-meta 
- :fontawesome-solid-user-group: **Participant:** ielab 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `9cebc208fbd04c2e665332aaac83f8a5` 
- :material-text: **Run description:** RBP rank fusion of the runs we submitted in Round 1 on a full-text index,  in addition to several runs from APIs of search engines that support CORD: AEUB, Covidex, DISCOVID, Fatcat, Ludwig, and Vespa. 

---
#### ir_covid19_cle_BM25 
[**`Results`**](./results.md#ir_covid19_cle_bm25) | [**`Participants`**](./participants.md#ir_covid19_cle) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ir_covid19_cle_BM25) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ir_covid19_cle_BM25.pdf) 

- :material-rename: **Run ID:** ir_covid19_cle_BM25 
- :fontawesome-solid-user-group: **Participant:** IR_COVID19_CLE 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `2483b93ba325121e8c17c89c77edb563` 
- :material-text: **Run description:** We have used the data set with all the documents from corpus. Using the metadata available, we added cord_id. We used around 48000 files.  We used "Paper_id",  "Title Id" and "Abstract" and "body_text" to index all the documents using Apache Lucene.  We have indexed every document for all tokens present with in the document. However, in a collection of documents these tokens can be repeating in multiple documents as well. Here, we use inverted index to store tokens repeating in multiple indexes, so that when searched for a specific token, we can narrow down the search documents specifically all documents that token is present. We have used the  query of the topic for querying the index.  We parsed the query with English Analyzer and searched on the abstract text field of the index. For each query, We have retrieved the Top 1000 documents and the relevance scores using BM25 similarity which is a ranking model used by search engines based on probabilistic weighting schemes. BM25 model approximates conditioned 2-poission model. BM25 is a TF/IDF based similarity.  Reference Paper:   Robertson, S. E., Walker, S., Hancock-Beaulieu, M., & Gatford, M. (1994). Okapi at TREC-3. In Proceedings of the Third Text REtrieval Conference (TREC 1994). Gaithersburg   

---
#### ir_covid19_cle_IB 
[**`Results`**](./results.md#ir_covid19_cle_ib) | [**`Participants`**](./participants.md#ir_covid19_cle) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ir_covid19_cle_IB) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ir_covid19_cle_IB.pdf) 

- :material-rename: **Run ID:** ir_covid19_cle_IB 
- :fontawesome-solid-user-group: **Participant:** IR_COVID19_CLE 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `8648ffd7b40bb1e5af3d64d07b90f279` 
- :material-text: **Run description:** We have used the data set with all the documents from corpus. Using the metadata available, we added cord_id. We used around 48000 files for indexing.  We used "Paper_id",  "Title Id" and "Abstract" and "body_text" to index all the documents using Apache Lucene.  We have indexed every document for all tokens present with in the document. However, in a collection of documents these tokens can be repeating in multiple documents as well. Here, we use inverted index to store tokens repeating in multiple indexes, so that when searched for a specific token, we can narrow down the search documents specifically all documents that token is present. We have used the  query of the topic for querying the index.  We parsed the query with English Analyzer and searched on the abstract text field of the index.  For each query, We have retrieved the Top 100 documents and the relevance scores using Information based (IB Similarity) which models rely on normalized values of occurrence of a word in documents. Information Models are characterized by three elements that are normalization function, probability distribution and retrieval function.  Reference Paper: Clinchant , S., & Gaussier, E. (2010). Information-based models for adhoc IR. In Proceeding of the 33rd international ACM SIGIR conference on Research and development in information retrieval (SIGIR '10). 

---
#### ir_covid19_cle_LMJ 
[**`Results`**](./results.md#ir_covid19_cle_lmj) | [**`Participants`**](./participants.md#ir_covid19_cle) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ir_covid19_cle_LMJ) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ir_covid19_cle_LMJ.pdf) 

- :material-rename: **Run ID:** ir_covid19_cle_LMJ 
- :fontawesome-solid-user-group: **Participant:** IR_COVID19_CLE 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `3d8b620ec58e2287b2c8cf390ef71a66` 
- :material-text: **Run description:** We have used the data set with all the documents from corpus. Using the metadata available, we added cord_id. We used around 48000 files for indexing.  We used "Paper_id",  "Title Id" and "Abstract" and "body_text" to index all the documents using Apache Lucene.  We have indexed every document for all tokens present with in the document. However, in a collection of documents these tokens can be repeating in multiple documents as well. Here, we use inverted index to store tokens repeating in multiple indexes, so that when searched for a specific token, we can narrow down the search documents specifically all documents that token is present. We have used the  query of the topic for querying the index.  We parsed the query with English Analyzer and searched on the abstract text field of the index.  For each query, We have retrieved the Top 100 documents and the relevance scores using LM Jelinek-Mercer similarity.  Reference Paper: Zhai , C., & Lafferty, J. (2001). A study of smoothing methods for language models applied to Ad Hoc information retrieval. In Proceedings of the 24th annual international ACM SIGIR conference on Research and development in information retrieval (SIGIR '01).  

---
#### irc_bm25_altmetric 
[**`Results`**](./results.md#irc_bm25_altmetric) | [**`Participants`**](./participants.md#irc) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/irc_bm25_altmetric) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/irc_bm25_altmetric.pdf) 

- :material-rename: **Run ID:** irc_bm25_altmetric 
- :fontawesome-solid-user-group: **Participant:** IRC 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `32079ab1827f7c65cba959e87906b526` 
- :material-text: **Run description:** This run submission combines a BM25 baseline with altmetrics. The baseline run is retrieved with the default ranker of Elasticsearch/Lucene (BM25) and queries using the contents of the <query>, <question>, and <narrative> tags. We rerank the baseline by adding the logarithmized Altmetric Attention Score. 

---
#### irc_logreg_tfidf 
[**`Results`**](./results.md#irc_logreg_tfidf) | [**`Participants`**](./participants.md#irc) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/irc_logreg_tfidf) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/irc_logreg_tfidf.pdf) 

- :material-rename: **Run ID:** irc_logreg_tfidf 
- :fontawesome-solid-user-group: **Participant:** IRC 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `1e4557f43a97964f3b266c89f0f8bf02` 
- :material-text: **Run description:** This run submission combines a BM25 baseline with a logistic regression based reranker trained on tfidf-features in combination with relevance judgments of the first round. The baseline run is retrieved with the default ranker of Elasticsearch/Lucene (BM25) and queries using the contents of the <query>, <question>, and <narrative> tags. Documents are reranked for those topics where relevance judgments are available (1-30), otherwise the baseline ranking remains unaltered (31-35). 

---
#### IRIT_markers_all 
[**`Results`**](./results.md#irit_markers_all) | [**`Participants`**](./participants.md#irit_markers) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/IRIT_markers_all) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/IRIT_markers_all.pdf) 

- :material-rename: **Run ID:** IRIT_markers_all 
- :fontawesome-solid-user-group: **Participant:** IRIT_markers 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `f394a173c100e275fcdef0832afb0332` 
- :material-text: **Run description:** We used a two-step ranker, an initial list of the top-1000 documents are retrieved using Anserini BM25, we use UDel queries and produce a run for each index: abstract, full text and paragraphs then merge the three to get a fusion run(https://github.com/castorini/anserini/blob/master/docs/experiments-covid.md). Then we use a BERT_base re-ranker finetuned on Msmarco passages. We use 3 models based on BERT, an original BERT(no modifications) and the 2 others use augmented entries with markers that highlight exact term matching. This final run is obtained by a fusion of the three re-ranking results.  

---
#### IRIT_markers_base_mu 
[**`Results`**](./results.md#irit_markers_base_mu) | [**`Participants`**](./participants.md#irit_markers) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/IRIT_markers_base_mu) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/IRIT_markers_base_mu.pdf) 

- :material-rename: **Run ID:** IRIT_markers_base_mu 
- :fontawesome-solid-user-group: **Participant:** IRIT_markers 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `5192afaf8f5a5cae8638a6b57babf592` 
- :material-text: **Run description:** We used a two-step ranker, an initial list of the top-1000 documents are retrieved using Anserini BM25, we use UDel queries and produce a run for each index: abstract, full text and paragraphs then merge the three to get a fusion run(https://github.com/castorini/anserini/blob/master/docs/experiments-covid.md). Then we use a BERT_base re-ranker finetuned on Msmarco passages . We use the question as the query and only the title and the abstract of each document. We use 2 models based on BERT, an original BERT(no modifications) and the other uses augmented entries with markers that highlight exact term matching using identifier tokens ([ei][\ei]) to surround the term i. This final run is obtained by a fusion of the two re-ranking results.  

---
#### IRIT_markers_base_un 
[**`Results`**](./results.md#irit_markers_base_un) | [**`Participants`**](./participants.md#irit_markers) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/IRIT_markers_base_un) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/IRIT_markers_base_un.pdf) 

- :material-rename: **Run ID:** IRIT_markers_base_un 
- :fontawesome-solid-user-group: **Participant:** IRIT_markers 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `d5f47ac30fd6d7514eab7f4c14cba896` 
- :material-text: **Run description:** We used a two-step ranker, an initial list of the top-1000 documents are retrieved using Anserini BM25, we use UDel queries and produce a run for each index: abstract, full text and paragraphs then merge the three to get a fusion run(https://github.com/castorini/anserini/blob/master/docs/experiments-covid.md). Then we use a BERT_base re-ranker finetuned on Msmarco passages. We use 2 models based on BERT, an original BERT(no modifications) and the other uses augmented entries with markers that highlight exact term matching with a simple character(#). This final run is obtained by a fusion of the two re-ranking results.  

---
#### MDA.QQ_RevW 
[**`Results`**](./results.md#mdaqq_revw) | [**`Participants`**](./participants.md#medduth_athenarc) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/MDA.QQ_RevW) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/MDA.QQ_RevW.pdf) 

- :material-rename: **Run ID:** MDA.QQ_RevW 
- :fontawesome-solid-user-group: **Participant:** MedDUTH_AthenaRC 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `3fa3b19918edf6d273b3d659e5403b86` 
- :material-text: **Run description:** Use Query+Question, Weighting based on reverse corpus frequencies and adjust, LDA, Cosine similarity. 

---
#### MDA.QQ_RFW 
[**`Results`**](./results.md#mdaqq_rfw) | [**`Participants`**](./participants.md#medduth_athenarc) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/MDA.QQ_RFW) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/MDA.QQ_RFW.pdf) 

- :material-rename: **Run ID:** MDA.QQ_RFW 
- :fontawesome-solid-user-group: **Participant:** MedDUTH_AthenaRC 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `18356c2a11dfcdebe0a17121aef3c0c7` 
- :material-text: **Run description:** Use Query+Question, Weighting based on reverse corpus frequencies, LDA, Cosine similarity. 

---
#### MDA.QQN_RevW 
[**`Results`**](./results.md#mdaqqn_revw) | [**`Participants`**](./participants.md#medduth_athenarc) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/MDA.QQN_RevW) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/MDA.QQN_RevW.pdf) 

- :material-rename: **Run ID:** MDA.QQN_RevW 
- :fontawesome-solid-user-group: **Participant:** MedDUTH_AthenaRC 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `3aea8d2c753a016947b9f2aca9713b5c` 
- :material-text: **Run description:** Use Query+Question+Narrative, Weighting based on reverse corpus frequencies and adjust, LDA, Cosine similarity. 

---
#### mpiid5_run1 
[**`Results`**](./results.md#mpiid5_run1) | [**`Participants`**](./participants.md#mpiid5) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/mpiid5_run1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/mpiid5_run1.pdf) 

- :material-rename: **Run ID:** mpiid5_run1 
- :fontawesome-solid-user-group: **Participant:** mpiid5 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `8ab0a5a3a0cc584fb8391fa177b944d3` 
- :material-text: **Run description:** We re-rank top-1500 documents returned by BM25 using query+question queries. For the re-ranking method, we use the ELECTRA-Base model fine-tuned on the MSMARCO passage dataset. The model is later fine-tuned on the TREC COVID round 1 full-text collection. 

---
#### mpiid5_run2 
[**`Results`**](./results.md#mpiid5_run2) | [**`Participants`**](./participants.md#mpiid5) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/mpiid5_run2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/mpiid5_run2.pdf) 

- :material-rename: **Run ID:** mpiid5_run2 
- :fontawesome-solid-user-group: **Participant:** mpiid5 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `24feda48d8ab71b85522ca35d323b5b4` 
- :material-text: **Run description:** We re-rank top-1500 documents returned by BM25 using the queries produced by Udel's method. For the re-ranking method, we use the ELECTRA-Base model fine-tuned on the MSMARCO passage dataset. The model is later fine-tuned on the TREC COVID round 1 full-text collection. 

---
#### mpiid5_run3 
[**`Results`**](./results.md#mpiid5_run3) | [**`Participants`**](./participants.md#mpiid5) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/mpiid5_run3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/mpiid5_run3.pdf) 

- :material-rename: **Run ID:** mpiid5_run3 
- :fontawesome-solid-user-group: **Participant:** mpiid5 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `cd71ce33d5ccb5a198125b23e9bd9b59` 
- :material-text: **Run description:** We re-rank top-10000 documents returned by BM25 using the queries produced by Udel's method. For the re-ranking method, we use the ELECTRA-Base model fine-tuned on the MSMARCO passage dataset. The model is later fine-tuned on the TREC COVID round 1 full-text collection. 

---
#### OHSU_BCB_round2 
[**`Results`**](./results.md#ohsu_bcb_round2) | [**`Participants`**](./participants.md#ohsu) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/OHSU_BCB_round2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/OHSU_BCB_round2.pdf) 

- :material-rename: **Run ID:** OHSU_BCB_round2 
- :fontawesome-solid-user-group: **Participant:** OHSU 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `b8de5e04213c395a2f2659783c44ed1e` 
- :material-text: **Run description:** Three Pyserini queries were created per topic using the query, question, and narrative fields on full text. After search was performed using a SimpleSearcher, scores were normalized and summed for a final score. The question query was weighted slightly higher because it appeared to retrieve better results based on review of round 1 results.  

---
#### PL2_Bo1QE 
[**`Results`**](./results.md#pl2_bo1qe) | [**`Participants`**](./participants.md#ub_bw) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/PL2_Bo1QE) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/PL2_Bo1QE.pdf) 

- :material-rename: **Run ID:** PL2_Bo1QE 
- :fontawesome-solid-user-group: **Participant:** UB_BW 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `ed16023015ecbfeee03e2206bfca5577` 
- :material-text: **Run description:** We indexed only the title and the abstract using Terrier-v5.2. For the final document ranking, we deployed PL2 term weighting model. During retrieval, we used both the query and the question tags, which were then expanded with terms selected using the Bo1 model for query expansion 

---
#### poznan_p2_2 
[**`Results`**](./results.md#poznan_p2_2) | [**`Participants`**](./participants.md#poznan) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/poznan_p2_2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/poznan_p2_2.pdf) 

- :material-rename: **Run ID:** poznan_p2_2 
- :fontawesome-solid-user-group: **Participant:** POZNAN 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `ebcb51ef694830329f56981f3df3f318` 
- :material-text: **Run description:** Automatic document score reweighting with use a word vector space done on a poznan_run_p2_3. Unsupervised method. Uses hypothesis: if there is relevant information in a document then document is relevant to a given query, regardless of the size of a document and a size of an information.  

---
#### poznan_run_p2_1 
[**`Results`**](./results.md#poznan_run_p2_1) | [**`Participants`**](./participants.md#poznan) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/poznan_run_p2_1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/poznan_run_p2_1.pdf) 

- :material-rename: **Run ID:** poznan_run_p2_1 
- :fontawesome-solid-user-group: **Participant:** POZNAN 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `e9679d19017112331c867d6fd75eab46` 
- :material-text: **Run description:** Query adjustments with use of the prior judgements. Metadata, title, abstract and body text indexed. Nested, sum based query (sum for each term in the query; sum for each document field). 

---
#### poznan_run_p2_3 
[**`Results`**](./results.md#poznan_run_p2_3) | [**`Participants`**](./participants.md#poznan) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/poznan_run_p2_3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/poznan_run_p2_3.pdf) 

- :material-rename: **Run ID:** poznan_run_p2_3 
- :fontawesome-solid-user-group: **Participant:** POZNAN 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `c6090c7fe4584c63a2fa16e0b60a8cd5` 
- :material-text: **Run description:** Added new queries. Indexing text body, metadata, title and abstract. TF-IDF weighting scheme. Sum based query. 

---
#### PS-r2-allebd 
[**`Results`**](./results.md#ps-r2-allebd) | [**`Participants`**](./participants.md#pitt) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/PS-r2-allebd) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/PS-r2-allebd.pdf) 

- :material-rename: **Run ID:** PS-r2-allebd 
- :fontawesome-solid-user-group: **Participant:** PITT 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `f3a821540596b2ade98cb4bfdcc15007` 
- :material-text: **Run description:** The query was generated manually through human by reading the topic, question and narrative section of the topics file and find keywords from it.  The query is then expand through the Metamap + Term level Word embedding + topic level embedding. The expanded query is then sent to Elastiscsearch engine which use tf-idf model to index and use "BM25" retrieval model to rank the result.  Currently, all the words weigh the same inside the query.  

---
#### PS-r2-origin 
[**`Results`**](./results.md#ps-r2-origin) | [**`Participants`**](./participants.md#pitt) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/PS-r2-origin) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/PS-r2-origin.pdf) 

- :material-rename: **Run ID:** PS-r2-origin 
- :fontawesome-solid-user-group: **Participant:** PITT 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `fbb8cee10c4f98de768aebb8f7366e2d` 
- :material-text: **Run description:** The query was generated manually through human by reading the topic, question and narrative section of the topics file and find keywords from it.  The query is then expand through the Metamap. The expanded query is then sent to Elastiscsearch engine which use tf-idf model to index and use "BM25" retrieval model to rank the result.  Currently, all the words weigh the same inside the query.  

---
#### PS-r2-termebd 
[**`Results`**](./results.md#ps-r2-termebd) | [**`Participants`**](./participants.md#pitt) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/PS-r2-termebd) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/PS-r2-termebd.pdf) 

- :material-rename: **Run ID:** PS-r2-termebd 
- :fontawesome-solid-user-group: **Participant:** PITT 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `fc012523da7cf64b057fdc88b8cad9d0` 
- :material-text: **Run description:** The query was generated manually through human by reading the topic, question and narrative section of the topics file and find keywords from it.  The query is then expand through the Metamap + Term level Word embedding. The expanded query is then sent to Elastiscsearch engine which use tf-idf model to index and use "BM25" retrieval model to rank the result.  Currently, all the words weigh the same inside the query.  

---
#### r2.fusion1 
[**`Results`**](./results.md#r2fusion1) | [**`Participants`**](./participants.md#anserini) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/r2.fusion1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/r2.fusion1.pdf) 

- :material-rename: **Run ID:** r2.fusion1 
- :fontawesome-solid-user-group: **Participant:** anserini 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `89544da0409435c74dd4f3dd5fc9dc62` 
- :material-text: **Run description:** Anserini fusion run corresponding to row 7 in "Round 2" table at https://github.com/castorini/anserini/blob/master/docs/experiments-covid.md  

---
#### r2.fusion2 
[**`Results`**](./results.md#r2fusion2) | [**`Participants`**](./participants.md#anserini) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/r2.fusion2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/r2.fusion2.pdf) 

- :material-rename: **Run ID:** r2.fusion2 
- :fontawesome-solid-user-group: **Participant:** anserini 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `774359c157c65bb7142d4f43b614e38f` 
- :material-text: **Run description:** Anserini fusion run corresponding to row 8 in "Round 2" table at https://github.com/castorini/anserini/blob/master/docs/experiments-covid.md  

---
#### random_bert_tiab 
[**`Results`**](./results.md#random_bert_tiab) | [**`Participants`**](./participants.md#random) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/random_bert_tiab) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/random_bert_tiab.pdf) 

- :material-rename: **Run ID:** random_bert_tiab 
- :fontawesome-solid-user-group: **Participant:** Random 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `1da200e16b5be130a88f24b6f49c6bf9` 
- :material-text: **Run description:** We used pre-trained BERT model and fine-tuned it with relevance judgement from round 1. We concatenated Query and Document (only title and abstract in our case, we assumed if the document is relevant to the query then the title and abstract is relevant to the query and vice-versa) for BERT input: [[CLS] Q [SEP] D [SEP]]. We used 428 tokens for BERT input, if our Query+Document Title+abstract were less than 428 tokens, we padded it with zero and if it was more than 428 tokens, we truncated it.  Next, using the CORD-19 dataset provided for round 2, we retrieved 3000 documents per topic using basic tf-idf model with cosine-similarity as ranking score. Then we used our fine-tuned BERT model to classify each query-document pair (retrieved from our tf-idf model) as relevant, partially relevant or not relevant. Finally, we retrieved 1000 documents for each topic based on the classification results from our BERT model. The ranking score for our final BERT model is the classification probability score in descending order. 

---
#### ReInfoSelect 
[**`Results`**](./results.md#reinfoselect) | [**`Participants`**](./participants.md#cmt) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ReInfoSelect) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ReInfoSelect.pdf) 

- :material-rename: **Run ID:** ReInfoSelect 
- :fontawesome-solid-user-group: **Participant:** CMT 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `c24c07ff631d7a15852f8a1e0c23156e` 
- :material-text: **Run description:** ReinfoSelect (Med Marco with nlg large): anserini TREC-COVID R2 Retrieval #8 retrieval and ReInfoSelect few-shot SciBERT with weak supervisions from med-marco and Contrastive NLG COVD Query 

---
#### req_rec_run1 
[**`Results`**](./results.md#req_rec_run1) | [**`Participants`**](./participants.md#req_rec) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/req_rec_run1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/req_rec_run1.pdf) 

- :material-rename: **Run ID:** req_rec_run1 
- :fontawesome-solid-user-group: **Participant:** req_rec 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `d34236a88f1195a6dd2196d669f9ad47` 
- :material-text: **Run description:** Based on the ReQ-ReC framework. Li, Cheng et al. "ReQ-ReC: high recall retrieval with query pooling and interactive classification." Proceedings of the 37th international ACM SIGIR conference on Research & development in information retrieval (2014): n. pag.  

---
#### req_rec_run2 
[**`Results`**](./results.md#req_rec_run2) | [**`Participants`**](./participants.md#req_rec) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/req_rec_run2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/req_rec_run2.pdf) 

- :material-rename: **Run ID:** req_rec_run2 
- :fontawesome-solid-user-group: **Participant:** req_rec 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `94789f4dece8db33a3651128e42df276` 
- :material-text: **Run description:** Use Indri to build search engine. 

---
#### req_rec_run3 
[**`Results`**](./results.md#req_rec_run3) | [**`Participants`**](./participants.md#req_rec) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/req_rec_run3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/req_rec_run3.pdf) 

- :material-rename: **Run ID:** req_rec_run3 
- :fontawesome-solid-user-group: **Participant:** req_rec 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `38fbdbe0eca44ef6a4681328f9a8dd2e` 
- :material-text: **Run description:** Based on ReQ-ReC framework. Li, Cheng et al. "ReQ-ReC: high recall retrieval with query pooling and interactive classification." Proceedings of the 37th international ACM SIGIR conference on Research & development in information retrieval (2014): n. pag. 

---
#### RMITBFuseM1 
[**`Results`**](./results.md#rmitbfusem1) | [**`Participants`**](./participants.md#rmitb) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/RMITBFuseM1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/RMITBFuseM1.pdf) 

- :material-rename: **Run ID:** RMITBFuseM1 
- :fontawesome-solid-user-group: **Participant:** RMITB 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/10/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `c3df0ea68e0d78c270d457ccf876dda7` 
- :material-text: **Run description:** Same retrieval method as RMITBFuseM2 in Round 1. However, noting that 10% of Round 1's  relevant judgments were made on documents without an associated PMC or JSON document, which we deleted from our collection, as we expected these invalid entries would not be classified as a document. 

---
#### ru-t-exp-rnd2 
[**`Results`**](./results.md#ru-t-exp-rnd2) | [**`Participants`**](./participants.md#ruir) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ru-t-exp-rnd2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ru-t-exp-rnd2.pdf) 

- :material-rename: **Run ID:** ru-t-exp-rnd2 
- :fontawesome-solid-user-group: **Participant:** RUIR 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `587a1432779b097e153d57704b5ea978` 
- :material-text: **Run description:** Anserini bm25 (title+abstract+paragraph index) using query expansion based on Kaggle task descriptions. TREC topics were manually classified into Kaggle tasks, and the top 10 keywords of the task were extracted based on TF-IDF (using paper abstracts as a corpus). Query terms were weighted as a * topic_query + (1-a) * task_terms i.e. the weights of the terms in the topic query add to 'a' a=.8 was selected by optimizing towards both high precision on known qrels and a high number of unknown qrels. 

---
#### ru-tn-exp-rnd2 
[**`Results`**](./results.md#ru-tn-exp-rnd2) | [**`Participants`**](./participants.md#ruir) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ru-tn-exp-rnd2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ru-tn-exp-rnd2.pdf) 

- :material-rename: **Run ID:** ru-tn-exp-rnd2 
- :fontawesome-solid-user-group: **Participant:** RUIR 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `3a96b281790c147cc1068b6bf5e38575` 
- :material-text: **Run description:** Anserini bm25 (title+abstract+paragraph index) using query expansion based on Kaggle task descriptions. TREC topics were manually classified into Kaggle tasks, and the top 10 keywords of the task were extracted based on TF-IDF (using paper abstracts as a corpus). Query terms were weighted as .6 * topic_query + .25 * topic_narrative + .15 task_description 

---
#### ru-tw-exp-rnd2 
[**`Results`**](./results.md#ru-tw-exp-rnd2) | [**`Participants`**](./participants.md#ruir) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ru-tw-exp-rnd2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ru-tw-exp-rnd2.pdf) 

- :material-rename: **Run ID:** ru-tw-exp-rnd2 
- :fontawesome-solid-user-group: **Participant:** RUIR 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `5982ed0f155226fb92a65cad9b66ac12` 
- :material-text: **Run description:** Anserini bm25 (title+abstract+paragraph index) using query expansion based on Kaggle task descriptions. TREC topics were manually classified into Kaggle tasks.  All relevant documents associated with a topic in a given task was associated with that task. Based on TF-IDF (with paper abstracts as corpus) we selected n=50 keywords that characterized this task. Words that occurred in more than 3 tasks were removed as stopwords, leaving a much smaller set of terms with tf-idf score. Query terms were weighted as a * topic_query + (1-a) * task_terms a=.8 was selected because we use it in our run ruir-t-exp-rnd2. The task terms were normalized to add to 1-a based on their tf-idf scores 

---
#### run1 
[**`Results`**](./results.md#run1) | [**`Participants`**](./participants.md#cuni) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/run1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/run1.pdf) 

- :material-rename: **Run ID:** run1 
- :fontawesome-solid-user-group: **Participant:** cuni 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `0ae4e54855af9faa4a7faf640b42fd52` 
- :material-text: **Run description:** Documents (abstracts and titles from metadata, full body text from json files) were indexed using Terrier. Queries were created using the query fields in the topic files.  LGD weighting model was used to retrieve 1000 documents for each query. 

---
#### run2 
[**`Results`**](./results.md#run2) | [**`Participants`**](./participants.md#cuni) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/run2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/run2.pdf) 

- :material-rename: **Run ID:** run2 
- :fontawesome-solid-user-group: **Participant:** cuni 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `d24f7eade7f704e7b483280e826fc229` 
- :material-text: **Run description:** This run is inspired by our previous work (Term Selection for Query Expansion in Medical Cross-Lingual Information Retrieval), but since we did not have enough training data, we translated the queries into French (our best performing SMT system), then we took 1-best-list from the translation, and then we translated each query back to English taking 100-best-list, and created bag-of-words from these translation hypotheses and added them to the original queries (as a query expansion method employing SMT system) then we run the same system as in Run1 using these expanded queries. 

---
#### run3 
[**`Results`**](./results.md#run3) | [**`Participants`**](./participants.md#cuni) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/run3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/run3.pdf) 

- :material-rename: **Run ID:** run3 
- :fontawesome-solid-user-group: **Participant:** cuni 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `92ba9f3ef9bdf2be524469da2a5d4f5f` 
- :material-text: **Run description:** The queries in this run were automatically expanded using Kullback-Leibler Divergence approach (top 7 documents and top 2 terms)  All other settings are similar to run1.  

---
#### sab20.2.dfo.meta 
[**`Results`**](./results.md#sab202dfometa) | [**`Participants`**](./participants.md#sabir) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/sab20.2.dfo.meta) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/sab20.2.dfo.meta.pdf) 

- :material-rename: **Run ID:** sab20.2.dfo.meta 
- :fontawesome-solid-user-group: **Participant:** sabir 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `7a7b1301273c57622b2d3868c1ee9673` 
- :material-text: **Run description:** SMART vector DFO run. Base Lnu.ltu weights. Run DFO algorithm (the runs and same parameters described in my TREC 2005 Routing track, and later, eg 2017 core track). Use relevance info on Round 1 collection to expand and optimize weights on that collection (using only metadata documents), and then run exactly that query (with same dictionary) on the Round2 collection.  This run on Round 2 used only the Lnu weighted inverted files for metadata (ignored all JSON docs). Used full narrative and ltu weights for the new topics in Round 2. 

---
#### sab20.2.dfo.metadocs 
[**`Results`**](./results.md#sab202dfometadocs) | [**`Participants`**](./participants.md#sabir) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/sab20.2.dfo.metadocs) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/sab20.2.dfo.metadocs.pdf) 

- :material-rename: **Run ID:** sab20.2.dfo.metadocs 
- :fontawesome-solid-user-group: **Participant:** sabir 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `cf89b726a391c3b686dcbbf2eed1a49d` 
- :material-text: **Run description:** SMART vector DFO run. Base Lnu.ltu weights. Run DFO algorithm (the runs and same parameters described in my TREC 2005 Routing track, and later, eg 2017 core track). Use relevance info on Round 1 collection to expand and optimize weights on that collection (using only metadata documents), and then run exactly that query (with same dictionary) on the Round2 collection.  This run on Round 2 used separate Lnu weighted inverted files for metadata and JSON docs. Score = 1.2 * metadata + JSON. Used full narrative and ltu weights for the new topics in Round 2. 

---
#### sab20.2.meta.docs 
[**`Results`**](./results.md#sab202metadocs) | [**`Participants`**](./participants.md#sabir) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/sab20.2.meta.docs) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/sab20.2.meta.docs.pdf) 

- :material-rename: **Run ID:** sab20.2.meta.docs 
- :fontawesome-solid-user-group: **Participant:** sabir 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `b557bdddae413c75d3ea1fa542a9efcd` 
- :material-text: **Run description:** SMART vector run. Lnu.ltu weights. Separate Lnu weighted inverted files for metadata and JSON docs. Score = 1.2 * metadata + JSON. Used full topics including narrative. 

---
#### savantx_nist_run_1 
[**`Results`**](./results.md#savantx_nist_run_1) | [**`Participants`**](./participants.md#savantx) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/savantx_nist_run_1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/savantx_nist_run_1.pdf) 

- :material-rename: **Run ID:** savantx_nist_run_1 
- :fontawesome-solid-user-group: **Participant:** SavantX 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `7a2267a6017134dc1ec58068eb723f30` 
- :material-text: **Run description:** An automated process was scripted to extract topics from the supplied XML. The searches were automatically issued to SavantX PRO. The system employees a patented, unsupervised machine learning hyper-dimensional relationship analysis technology. This technology coupled with PRO's full stack AI outputted ranked results without any human intervention. 

---
#### savantx_nist_run_2 
[**`Results`**](./results.md#savantx_nist_run_2) | [**`Participants`**](./participants.md#savantx) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/savantx_nist_run_2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/savantx_nist_run_2.pdf) 

- :material-rename: **Run ID:** savantx_nist_run_2 
- :fontawesome-solid-user-group: **Participant:** SavantX 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `3e8dd8aa035649a693f7b1ad6934cda0` 
- :material-text: **Run description:** An automated process was scripted to extract topics from the supplied XML. The searches were automatically issued to SavantX PRO. The system employees a patented, unsupervised machine learning hyper-dimensional relationship analysis technology. This technology coupled with PRO's full stack AI outputted ranked results without any human intervention. 

---
#### savantx_nist_run_3 
[**`Results`**](./results.md#savantx_nist_run_3) | [**`Participants`**](./participants.md#savantx) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/savantx_nist_run_3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/savantx_nist_run_3.pdf) 

- :material-rename: **Run ID:** savantx_nist_run_3 
- :fontawesome-solid-user-group: **Participant:** SavantX 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `6c67b3010e60afcc3b3e4c506207f52b` 
- :material-text: **Run description:** An automated process was scripted to extract topics from the supplied XML. The searches were automatically issued to SavantX PRO. The system employees a patented, unsupervised machine learning hyper-dimensional relationship analysis technology. This technology coupled with PRO's full stack AI outputted ranked results without any human intervention. 

---
#### SFDC-round2-baseline 
[**`Results`**](./results.md#sfdc-round2-baseline) | [**`Participants`**](./participants.md#sfdc) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/SFDC-round2-baseline) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/SFDC-round2-baseline.pdf) 

- :material-rename: **Run ID:** SFDC-round2-baseline 
- :fontawesome-solid-user-group: **Participant:** SFDC 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `b384da3885377f00ead0b61ea62f4f05` 
- :material-text: **Run description:** Semantic search retriever (no TF-IDF features) with BERT.  

---
#### SFDC-round2-qna 
[**`Results`**](./results.md#sfdc-round2-qna) | [**`Participants`**](./participants.md#sfdc) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/SFDC-round2-qna) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/SFDC-round2-qna.pdf) 

- :material-rename: **Run ID:** SFDC-round2-qna 
- :fontawesome-solid-user-group: **Participant:** SFDC 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `c96e0edd856087e87df5733479962cc6` 
- :material-text: **Run description:** Semantic Search retrieval with BERT. Uses a question-answering module to do a final ranking on the top 100 documents. 

---
#### shamra_tag 
[**`Results`**](./results.md#shamra_tag) | [**`Participants`**](./participants.md#shamra) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/shamra_tag) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/shamra_tag.pdf) 

- :material-rename: **Run ID:** shamra_tag 
- :fontawesome-solid-user-group: **Participant:** shamra 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `1a8d12c3c2fcee5468af96584b9349cc` 
- :material-text: **Run description:** Used Elasticsearch for indexing, and BM-25 as a search algorithm with parameters(k1=1.2 and b = 0.75). Removed English stopwords in indexed documents and queries. All coronavirus common names are considered the same. considered fields (in decreasing order of their score influence): abstract.text,abstract in metadata,body_text.text,metadata.title 

---
#### soboroffFiltering 
[**`Results`**](./results.md#soborofffiltering) | [**`Participants`**](./participants.md#irlabku) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/soboroffFiltering) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/soboroffFiltering.pdf) 

- :material-rename: **Run ID:** soboroffFiltering 
- :fontawesome-solid-user-group: **Participant:** IRLabKU 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `a8af948c9d4b45922855e7c4d95d737d` 
- :material-text: **Run description:** --We create 3 indexes: 1) Based on title+abstract, 2) Based on full-text, and 3) Based on title+abstract+paragraph (a document is split into para1, para2, ..., paraK, and we create K+1 documents of the form title+abstract, title+abstract+para1, title+abstract+para2. --We create 4 different types of queries: 1) Query + named_entitities(question), 2) Query + named_entitities(question) + named_entitities(narrative), 3) Question + named_entitities(query), and 4) Question + named_entitities(query) + named_entitities(narrative) --For each query type we create 4 runs (default BM25 + default RM3): 1) We search in index of title+abstract, 2) We search in index of full-text, 3) We search in index of title+abstract+paragraph (where we only keep the first occurrence of a document and delete the following duplicates), and 4) We search in index of title+abstract+paragraph (where we don't remove the duplicates) Finally, based on these 4 runs, we use reciprocal rank fusion to get 1 run. --Now, we have 4 fusion runs, which we use to create a final reciprocal rank fusion (Fusion of Fusions). We also create a fusion of the 16 runs without an intermediate fusion (Fusion of Runs).  --Finally, we use reciprocal rank fusion between the 9 automatic runs, that did not contribute to the pooling and was chosen based on the middle runs from Soboroff's Method [1] out of 27 possible runs, from round 1, as well as our own 2 fusion runs. [1] http://research.nii.ac.jp/ntcir/workshop/OnlineProceedings8/EVIA/05-EVIA2010-SakaiT.pdf 

---
#### SparseDenseSciBert 
[**`Results`**](./results.md#sparsedensescibert) | [**`Participants`**](./participants.md#cmt) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/SparseDenseSciBert) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/SparseDenseSciBert.pdf) 

- :material-rename: **Run ID:** SparseDenseSciBert 
- :fontawesome-solid-user-group: **Participant:** CMT 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `b3ae9bec83eb0d065654d6f83810329e` 
- :material-text: **Run description:** bm25+ann+scibert.0.33.teIn (ann-bm25 retrieval + scibert reranker): anserini TREC-COVID R2 Retrieval #8 + med-marco ANN + med-marco SciBERT with COVD Mask-Lm fine-tuning 

---
#### Technion-JPDs 
[**`Results`**](./results.md#technion-jpds) | [**`Participants`**](./participants.md#technion) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/Technion-JPDs) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/Technion-JPDs.pdf) 

- :material-rename: **Run ID:** Technion-JPDs 
- :fontawesome-solid-user-group: **Participant:** Technion 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `250e834adf2923895085998000c80199` 
- :material-text: **Run description:** We use the JPDs method (c.f., [Sheetrit E, Shtok A, Kurland O (2020) A Passage-Based Approach to Learning to Rank Documents. Information Retrieval Journal 23, 159--186 (2020). https://doi.org/10.1007/s10791-020- 09369-x]). We use a BERT-base (12 layers, 768 hidden size) fine-tuned on Ms Marco passage dataset to induce an effective ranking of passages from the documents that were initially retrieved in response to the query. Specifically, we use a standard unigram language model approach to retrieve an initial list of 1000 documents for a query after removing the documents that has already been judged.  

---
#### Technion-LTR 
[**`Results`**](./results.md#technion-ltr) | [**`Participants`**](./participants.md#technion) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/Technion-LTR) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/Technion-LTR.pdf) 

- :material-rename: **Run ID:** Technion-LTR 
- :fontawesome-solid-user-group: **Participant:** Technion 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `25e200edffa835864033d5ddb2e4505a` 
- :material-text: **Run description:** We use a learning-to-rank approach with 116 features. We apply the following three-step procedure. First, we use a standard unigram language model approach to retrieve an initial list of 1000 documents for a query after removing the documents that has already been judged. Second, we train a document ranking model using all documents that exist in the qrels file. Finally, we apply our trained model on the initially retrieved document list. To train and apply the document ranker, we used a linear RankSVM. The "query" and "question" fields serve for queries.  

---
#### Technion-RRF 
[**`Results`**](./results.md#technion-rrf) | [**`Participants`**](./participants.md#technion) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/Technion-RRF) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/Technion-RRF.pdf) 

- :material-rename: **Run ID:** Technion-RRF 
- :fontawesome-solid-user-group: **Participant:** Technion 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `52b8a07b527a355e044c356ceca7f1cb` 
- :material-text: **Run description:** We use the reciprocal rank fusion method to combine the rankings induced by Run2, Run3 with the ranking induced by the BERT-base (12 layers, 768 hidden size) model which was fine-tuned on the Ms Marco passage dataset. The model's free parameter was set to 60. 

---
#### TF_IDF_Bo1QE 
[**`Results`**](./results.md#tf_idf_bo1qe) | [**`Participants`**](./participants.md#ub_bw) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/TF_IDF_Bo1QE) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/TF_IDF_Bo1QE.pdf) 

- :material-rename: **Run ID:** TF_IDF_Bo1QE 
- :fontawesome-solid-user-group: **Participant:** UB_BW 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `2fbe6a2d489d1d532e7d34c8dc7e3b4d` 
- :material-text: **Run description:** We indexed only the title and the abstract using Terrier-v5.2. For the final document ranking, we deployed the TF-IDF term weighting model. During retrieval, we used both the query and the question tags, which were then expanded with terms selected using the Bo1 model for query expansion. 

---
#### TMACC_SeTA_sent2vec 
[**`Results`**](./results.md#tmacc_seta_sent2vec) | [**`Participants`**](./participants.md#tmacc_seta) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/TMACC_SeTA_sent2vec) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/TMACC_SeTA_sent2vec.pdf) 

- :material-rename: **Run ID:** TMACC_SeTA_sent2vec 
- :fontawesome-solid-user-group: **Participant:** TMACC_SeTA 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `7c7572df88206f54c2478ca586c87d98` 
- :material-text: **Run description:** The submission was fully automatic. Topic <query> and <question> elements were Stop Word and POS tag filtered (using nltk) to produce a keyword list, that was expanded by querying a Word2Vec model (gensim) of the CORD-19 dataset for 10 most related terms, filtered by tfidf scores on the same corpus. Expanded keyword list was encoded as a vector in a doc2vec model, where each sentence is treated as document, while keeping reference to the id the corpus article it belongs to. This model was trained using gensim lib after pre-processing for phrase extraction with spacy, textacy and Abner NER for multi-word named entity. The 1000 most related doc were returned by aggregating and summing up the relevance scores of the top sentences returned by sent2vec.  

---
#### TMACC_SeTA_tfidf 
[**`Results`**](./results.md#tmacc_seta_tfidf) | [**`Participants`**](./participants.md#tmacc_seta) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/TMACC_SeTA_tfidf) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/TMACC_SeTA_tfidf.pdf) 

- :material-rename: **Run ID:** TMACC_SeTA_tfidf 
- :fontawesome-solid-user-group: **Participant:** TMACC_SeTA 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `29f337b61db4c600f5f11d7f00392179` 
- :material-text: **Run description:** The submission was fully automatic. Topic <query> and <question> elements were Stop Word and POS tag filtered (using nltk) to produce a keyword list, that was expanded by querying a Word2Vec model (gensim) of the CORD-19 dataset for 10 most related terms, filtered by tfidf scores on the same corpus. Expanded keyword list was encoded as a vector in a doc2vec model. This model was trained using gensim lib after pre-processing for phrase extraction with spacy, textacy and Abner NER for multi-word named entity. The model was then filtered by using tfidf scores. The 1000 most related doc were returned. 

---
#### TMACC_SeTA_tfidf_q 
[**`Results`**](./results.md#tmacc_seta_tfidf_q) | [**`Participants`**](./participants.md#tmacc_seta) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/TMACC_SeTA_tfidf_q) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/TMACC_SeTA_tfidf_q.pdf) 

- :material-rename: **Run ID:** TMACC_SeTA_tfidf_q 
- :fontawesome-solid-user-group: **Participant:** TMACC_SeTA 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `5e34e2cc9d6f8341ea81a7f84a362c9a` 
- :material-text: **Run description:** The submission was fully automatic. Topic <query> and <question> elements were Stop Word and POS tag filtered (using nltk) to produce a keyword list, that was expanded by querying a Word2Vec model (gensim) of the CORD-19 dataset for 10 most related terms, filtered by tfidf scores on the same corpus. Expanded keyword list was encoded as a vector in a doc2vec model. This model was trained using gensim lib after pre-processing for phrase extraction with spacy, textacy and Abner NER for multi-word named entity. The 1000 most related doc were returned. 

---
#### ucd_cs_r1 
[**`Results`**](./results.md#ucd_cs_r1) | [**`Participants`**](./participants.md#ucd_cs) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ucd_cs_r1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ucd_cs_r1.pdf) 

- :material-rename: **Run ID:** ucd_cs_r1 
- :fontawesome-solid-user-group: **Participant:** UCD_CS 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `ea4acb3ad87e1632161671da174003b3` 
- :material-text: **Run description:** In the first stage, we use BM25 for retrieving 1000 documents per topic with parameters set up as reported in SLEDGE [1]. At this stage, all fields of the topic are used as the query and the document index is the fulltext version from Anserini. In the next stage, the 1000 documents are re-ranked by leveraging the off-the-shelf pre-trained SciBERT directly without fine-tuning. For re-ranking, all fields of the topic are concatenated to represent the query and only abstract is used as the document field. [1]: MacAvaney S, Cohan A, Goharian N. SLEDGE: A Simple Yet Effective Baseline for Coronavirus Scientific Knowledge Search. arXiv preprint arXiv:2005.02365. 2020 May 5. 

---
#### ucd_cs_r2 
[**`Results`**](./results.md#ucd_cs_r2) | [**`Participants`**](./participants.md#ucd_cs) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ucd_cs_r2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ucd_cs_r2.pdf) 

- :material-rename: **Run ID:** ucd_cs_r2 
- :fontawesome-solid-user-group: **Participant:** UCD_CS 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `e3e3d2c905439e87c18d3d7b9a4e2bbb` 
- :material-text: **Run description:** In the first stage, we use BM25 for retrieving 1000 documents per topic with parameters set up as reported in SLEDGE [1]. At this stage, all fields of the topic are used as the query and the document index is the fulltext version from Anserini. In the next stage, the 1000 documents are re-ranked by leveraging the the fine-tuned SciBERT on qrels-rnd1. For re-ranking, all fields of the topic are concatenated to represent the query and only abstract is used as the document field. [1]: MacAvaney S, Cohan A, Goharian N. SLEDGE: A Simple Yet Effective Baseline for Coronavirus Scientific Knowledge Search. arXiv preprint arXiv:2005.02365. 2020 May 5. 

---
#### ucd_cs_r3 
[**`Results`**](./results.md#ucd_cs_r3) | [**`Participants`**](./participants.md#ucd_cs) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/ucd_cs_r3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/ucd_cs_r3.pdf) 

- :material-rename: **Run ID:** ucd_cs_r3 
- :fontawesome-solid-user-group: **Participant:** UCD_CS 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `8d2b23ccf8baa9a2e214897989b7df28` 
- :material-text: **Run description:** This is a baseline without re-ranking, we use BM25 for retrieving 1000 documents per topic with parameters set up as reported in SLEDGE [1]. [1]: MacAvaney S, Cohan A, Goharian N. SLEDGE: A Simple Yet Effective Baseline for Coronavirus Scientific Knowledge Search. arXiv preprint arXiv:2005.02365. 2020 May 5. 

---
#### udel_fang_FB 
[**`Results`**](./results.md#udel_fang_fb) | [**`Participants`**](./participants.md#udel_fang) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/udel_fang_FB) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/udel_fang_FB.pdf) 

- :material-rename: **Run ID:** udel_fang_FB 
- :fontawesome-solid-user-group: **Participant:** udel_fang 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `176d598c2cb6ac4fb3fffd77ea2c5442` 
- :material-text: **Run description:** We build an index with title and abstract from the metadata file. The non-stopwords in query field and entities recognized by SciSpacy in question field are combined to form the queries. For the first 30 queries, we perform relevance feedback. More specifically, we use F2EXP as the retrieval function and axiomatic expansion method to select expansion terms. We pick all relevant documents with relevance grade of 2 to form the relevant document pool for each query, and if there are less than 20 documents for a query, we randomly add relevant documents with relevance grade of 1 until there are 20. For the 5 new queries, the method is similar to that of the first 30 and the only difference is that we use pseudo relevance feedback and the number of feedback documents is set to 20. For all 35 queries, we return the first 1000 documents that were not judged for the queries. 

---
#### udel_fang_L2R 
[**`Results`**](./results.md#udel_fang_l2r) | [**`Participants`**](./participants.md#udel_fang) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/udel_fang_L2R) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/udel_fang_L2R.pdf) 

- :material-rename: **Run ID:** udel_fang_L2R 
- :fontawesome-solid-user-group: **Participant:** udel_fang 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `0bbd4278d5e5c1761c267a5d09cae76f` 
- :material-text: **Run description:** We construct the keyword queries by using all non-stop words in the query field and all the entities tagged by SciSpacy in the question field. Then, we perform two baseline runs based on F2EXP, ranking title and abstract, and full text separately. After combining the features from the baseline runs, the keyword queries, and the metadata of all documents, we select the round one judgment file as the training data and use LambdaMART to re-rank the top 100 documents in the title and abstract baseline run. The best hyperparameters are chosen using cross-validation. 

---
#### udel_fang_NIR 
[**`Results`**](./results.md#udel_fang_nir) | [**`Participants`**](./participants.md#udel_fang) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/udel_fang_NIR) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/udel_fang_NIR.pdf) 

- :material-rename: **Run ID:** udel_fang_NIR 
- :fontawesome-solid-user-group: **Participant:** udel_fang 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `1869806d0810dc9fb08ed5511ed88849` 
- :material-text: **Run description:** We construct the keyword queries by using all non-stop words in the query field and all the entities tagged by SciSpacy in the question field. We use F2EXP as the retrieval function and axiomatic expansion method for pseudo relevance feedback. For all 35 queries, we return the first 1000 documents that were not judged for the queries. We remove the line breaks on the full text of documents and take the first 120 tokens from every document as its text representation. Then the queries and the text are sent to the pre-trained universal sentence encoder from TensorFlow hub separately to generate embeddings for both of the them. Dot product is performed on the embeddings and the output value is used as the score for the document. Based on this score the 1000 documents mentioned above are re-ranked for each of the 35 queries. 

---
#### UIowaS_Run1 
[**`Results`**](./results.md#uiowas_run1) | [**`Participants`**](./participants.md#uiowas) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/UIowaS_Run1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/UIowaS_Run1.pdf) 

- :material-rename: **Run ID:** UIowaS_Run1 
- :fontawesome-solid-user-group: **Participant:** UIowaS 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `17ac3dd082fd007b5a8c2e648af91b3b` 
- :material-text: **Run description:** Relevance feedback with provided relevance judgements using BM25 with 30 docs and 1000 terms for expansion (on unfiltered metadata  dataset) limited to title and abstract. For the last 5 topics retrieval feedback using TF_IDF using 10 documents and 20 terms (on filtered metadata dataset) limited to title and abstract.  

---
#### UIowaS_Run2 
[**`Results`**](./results.md#uiowas_run2) | [**`Participants`**](./participants.md#uiowas) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/UIowaS_Run2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/UIowaS_Run2.pdf) 

- :material-rename: **Run ID:** UIowaS_Run2 
- :fontawesome-solid-user-group: **Participant:** UIowaS 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `3207b50ef6119d3b172b49556730b2be` 
- :material-text: **Run description:** Relevance feedback with provided relevance judgements using BM25 with 10 docs and 300 terms for expansion (on unfiltered metadata  dataset) limited to title and abstract. For the last 5 topics retrieval feedback using TF_IDF using 10 documents and 20 terms (on filtered metadata dataset) limited to title and abstract.  

---
#### UIowaS_Run3 
[**`Results`**](./results.md#uiowas_run3) | [**`Participants`**](./participants.md#uiowas) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/UIowaS_Run3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/UIowaS_Run3.pdf) 

- :material-rename: **Run ID:** UIowaS_Run3 
- :fontawesome-solid-user-group: **Participant:** UIowaS 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `d08603c3360719b36e2cb0d4bb9400dc` 
- :material-text: **Run description:** This is a Borda merger of runs 1 and 2. Basically each document gets a score, which is a sum of its ranks in run1 and run2  

---
#### UPrrf16bert20-r2 
[**`Results`**](./results.md#uprrf16bert20-r2) | [**`Participants`**](./participants.md#unique_ptr) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/UPrrf16bert20-r2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/UPrrf16bert20-r2.pdf) 

- :material-rename: **Run ID:** UPrrf16bert20-r2 
- :fontawesome-solid-user-group: **Participant:** unique_ptr 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `4ab03aaba5b2375de7e77033d3e79f73` 
- :material-text: **Run description:** This run is produced by Reciprocal Rank Fusion (Cormack et al., 2009) of 6 Anserini runs (https://github.com/castorini/anserini/blob/master/docs/experiments-covid.md) along with 10 Terrier runs using various combinations of (query, question) and (body, abstract) fields. Top 20 RRF results are then re-ranked using a Reciprocal Rank Fusion of two TF-Ranking BERT models (https://arxiv.org/abs/2004.08476) trained on either MS-Marco or its medical queries subset (https://arxiv.org/abs/2005.02365). 

---
#### UPrrf16lgbert50-r2 
[**`Results`**](./results.md#uprrf16lgbert50-r2) | [**`Participants`**](./participants.md#unique_ptr) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/UPrrf16lgbert50-r2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/UPrrf16lgbert50-r2.pdf) 

- :material-rename: **Run ID:** UPrrf16lgbert50-r2 
- :fontawesome-solid-user-group: **Participant:** unique_ptr 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `70ee641c99e004f29f8bbd48b63cf192` 
- :material-text: **Run description:** This run is produced by Reciprocal Rank Fusion (Cormack et al., 2009) of 6 Anserini runs (https://github.com/castorini/anserini/blob/master/docs/experiments-covid.md) along with 10 Terrier runs using various combinations of (query, question) and (body, abstract) fields. Top 50 RRF results are then re-ranked using LightGBM LambdaRank that takes as features (a) RRF score (b) two best performing individual runs (Terrier using query + question with body or abstract fields) (c) two TF-Ranking BERT models (https://arxiv.org/abs/2004.08476) trained on either MS-Marco or its medical queries subset (https://arxiv.org/abs/2005.02365). 

---
#### UPrrf16lgbertd50-r2 
[**`Results`**](./results.md#uprrf16lgbertd50-r2) | [**`Participants`**](./participants.md#unique_ptr) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/UPrrf16lgbertd50-r2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/UPrrf16lgbertd50-r2.pdf) 

- :material-rename: **Run ID:** UPrrf16lgbertd50-r2 
- :fontawesome-solid-user-group: **Participant:** unique_ptr 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `a0ede515e246309e410059ce5fbecf36` 
- :material-text: **Run description:** This run is produced by Reciprocal Rank Fusion (Cormack et al., 2009) of 6 Anserini runs (https://github.com/castorini/anserini/blob/master/docs/experiments-covid.md) along with 10 Terrier runs using various combinations of (query, question) and (body, abstract) fields. Top 50 RRF results are then re-ranked using LightGBM LambdaRank that takes as features (a) RRF score (b) two best performing individual runs (Terrier using query + question with body or abstract fields) (c) two TF-Ranking BERT models (https://arxiv.org/abs/2004.08476) trained on either MS-Marco or its medical queries subset (https://arxiv.org/abs/2005.02365) (d) publish date (e) containment of any COVID-19 related keywords.  

---
#### VTechBase 
[**`Results`**](./results.md#vtechbase) | [**`Participants`**](./participants.md#virginiatechhat) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/VTechBase) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/VTechBase.pdf) 

- :material-rename: **Run ID:** VTechBase 
- :fontawesome-solid-user-group: **Participant:** VirginiaTechHAT 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `85ff56ab19f750393363a54ffe688065` 
- :material-text: **Run description:** a baseline system using QL, mu=500 (tuned using R1 data) 

---
#### VTechcrowd 
[**`Results`**](./results.md#vtechcrowd) | [**`Participants`**](./participants.md#virginiatechhat) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/VTechcrowd) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/VTechcrowd.pdf) 

- :material-rename: **Run ID:** VTechcrowd 
- :fontawesome-solid-user-group: **Participant:** VirginiaTechHAT 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `6c1a7af630645ca75dcb34407aa5c4ee` 
- :material-text: **Run description:** KLD where the query LM is from crowdsourcing alternative queries, weighted using the original query. 

---
#### VTechPRF 
[**`Results`**](./results.md#vtechprf) | [**`Participants`**](./participants.md#virginiatechhat) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/VTechPRF) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/VTechPRF.pdf) 

- :material-rename: **Run ID:** VTechPRF 
- :fontawesome-solid-user-group: **Participant:** VirginiaTechHAT 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/13/2020 
- :fontawesome-solid-user-gear: **Type:** feedback 
- :material-fingerprint: **MD5:** `097fd4667037f9be43eba15f7c5689c1` 
- :material-text: **Run description:** well-tuned RM3 based on R1 data; topfbdoc=20, fbterm=50, worg_query=0.2, mufb=0, mudoc=500 

---
#### W2VJPDRMM 
[**`Results`**](./results.md#w2vjpdrmm) | [**`Participants`**](./participants.md#aueb_nlp_group) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/W2VJPDRMM) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/W2VJPDRMM.pdf) 

- :material-rename: **Run ID:** W2VJPDRMM 
- :fontawesome-solid-user-group: **Participant:** AUEB_NLP_GROUP 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/11/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `9e43febf3a0784ace80ec62bd15cf4fa` 
- :material-text: **Run description:** We submit the results of our deep learning model named JPDRMM trained for both document retrieval and snippet extraction using data from the BioASQ contest. Our system achieved state of the art performance in document retrieval and snippet extraction tasks. you can read more here: http://nlp.cs.aueb.gr/pubs/aueb_at_bioasq7.pdf 

---
#### xj4wang_run1 
[**`Results`**](./results.md#xj4wang_run1) | [**`Participants`**](./participants.md#xj4wang) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/xj4wang_run1) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/xj4wang_run1.pdf) 

- :material-rename: **Run ID:** xj4wang_run1 
- :fontawesome-solid-user-group: **Participant:** xj4wang 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `732cb35d3460faa9a408f1957d52bc7c` 
- :material-text: **Run description:** The retrieval model used is BMI (Baseline Model Implementation), provided as a starter by Gordon Cormack for the TREC 2015/2016 Total Recall Track, with human assessors in place of the server (manual processing). [1] In more detail: It uses the CAL (Continuous Active Learning) method, starting with 1 synthetic file created using the given topics, word for word. This method is described by Grossman and Cormack in [4]. Feature vectors are created using the BMI tools. [1] SofiaML is used as the learner. The weighting scheme were chosen heavily based on the work of Cormack and Grossman in [2]. Stopping conditions for manual labeling were chosen heavily based on the work of Grossman et al. in [3]. References: [1] https://cormack.uwaterloo.ca/trecvm/ [2] file:///C:/Users/Jean/Downloads/2600428.2609601.pdf [3] https://trec.nist.gov/pubs/trec25/papers/Overview-TR.pdf [4] https://cormack.uwaterloo.ca/caldemo/AprMay16_EdiscoveryBulletin.pdf 

---
#### xj4wang_run2 
[**`Results`**](./results.md#xj4wang_run2) | [**`Participants`**](./participants.md#xj4wang) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/xj4wang_run2) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/xj4wang_run2.pdf) 

- :material-rename: **Run ID:** xj4wang_run2 
- :fontawesome-solid-user-group: **Participant:** xj4wang 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `9419de1d5f23be8caff8b3cf8f234478` 
- :material-text: **Run description:** The retrieval model used is BMI (Baseline Model Implementation), provided as a starter by Gordon Cormack for the TREC 2015/2016 Total Recall Track, with human assessors in place of the server (manual processing). [1] In more detail: It uses the CAL (Continuous Active Learning) method, starting with 1 synthetic file created using the given topics, word for word. This method is described by Grossman and Cormack in [4]. Feature vectors are created using the BMI tools. [1] SofiaML is used as the learner. The weighting scheme were chosen heavily based on the work of Cormack and Grossman in [2]. Stopping conditions for manual labeling were chosen heavily based on the work of Grossman et al. in [3]. References: [1] https://cormack.uwaterloo.ca/trecvm/ [2] file:///C:/Users/Jean/Downloads/2600428.2609601.pdf [3] https://trec.nist.gov/pubs/trec25/papers/Overview-TR.pdf [4] https://cormack.uwaterloo.ca/caldemo/AprMay16_EdiscoveryBulletin.pdf 

---
#### xj4wang_run3 
[**`Results`**](./results.md#xj4wang_run3) | [**`Participants`**](./participants.md#xj4wang) | [**`Input`**](https://ir.nist.gov/trec-covid/archive/round2/xj4wang_run3) | [**`Appendix`**](https://ir.nist.gov/trec-covid/archive/round2/xj4wang_run3.pdf) 

- :material-rename: **Run ID:** xj4wang_run3 
- :fontawesome-solid-user-group: **Participant:** xj4wang 
- :material-format-text: **Track:** Round 2 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 5/12/2020 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `f89998465ec4dd6bb6745751cae86b9c` 
- :material-text: **Run description:** The retrieval model used is BMI (Baseline Model Implementation), provided as a starter by Gordon Cormack for the TREC 2015/2016 Total Recall Track, with human assessors in place of the server (manual processing). [1] In more detail: It uses the CAL (Continuous Active Learning) method, starting with 1 synthetic file created using the given topics, word for word. This method is described by Grossman and Cormack in [4]. Feature vectors are created using the BMI tools. [1] SofiaML is used as the learner. The weighting scheme were chosen heavily based on the work of Cormack and Grossman in [2]. Stopping conditions for manual labeling were chosen heavily based on the work of Grossman et al. in [3]. References: [1] https://cormack.uwaterloo.ca/trecvm/ [2] file:///C:/Users/Jean/Downloads/2600428.2609601.pdf [3] https://trec.nist.gov/pubs/trec25/papers/Overview-TR.pdf [4] https://cormack.uwaterloo.ca/caldemo/AprMay16_EdiscoveryBulletin.pdf 

---
