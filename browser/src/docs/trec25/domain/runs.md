# Runs - Dynamic Domain 2016 

#### FifthIterBaseline 
[**`Participants`**](./participants.md#georgetown) | [**`Proceedings`**](./proceedings.md#an-investigation-of-basic-retrieval-models-for-the-dynamic-domain-task) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/FifthIterBaseline.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** FifthIterBaseline 
- :fontawesome-solid-user-group: **Participant:** georgetown 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/9/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Baseline for integration of feedback information 
- :material-code-tags: **Code:** [https://github.com/NeginR/DD16](https://github.com/NeginR/DD16) 

---
#### FirstIterBaseline 
[**`Participants`**](./participants.md#georgetown) | [**`Proceedings`**](./proceedings.md#an-investigation-of-basic-retrieval-models-for-the-dynamic-domain-task) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/FirstIterBaseline.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** FirstIterBaseline 
- :fontawesome-solid-user-group: **Participant:** georgetown 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/8/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Baseline results 
- :material-code-tags: **Code:** [https://github.com/NeginR/DD16](https://github.com/NeginR/DD16) 

---
#### LDA_Indri73 
[**`Participants`**](./participants.md#iaplab) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/LDA_Indri73.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** LDA_Indri73 
- :fontawesome-solid-user-group: **Participant:** IAPLab 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/7/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** We use Indri and LDA to access the first iteration of the first query. Then we use the MDP model which we has modified and get the next iteration.During the MDP model,we use the Indri to help to search and then get the final result. 
- :material-code-tags: **Code:** [https://github.com/TrecDD2016/trec_dd/](https://github.com/TrecDD2016/trec_dd/) 

---
#### rmit_lm_nqe 
[**`Participants`**](./participants.md#rmit) | [**`Proceedings`**](./proceedings.md#rmit-trec-2016-dynamic-domain-track-exploiting-passage-representation-for-retrieval-and-relevance-feedback) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/rmit_lm_nqe.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** rmit_lm_nqe 
- :fontawesome-solid-user-group: **Participant:** RMIT 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/8/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** In this method, we used the Language modeling approach as implemented in Apache Solr using Dirichlet smoothing and default parameters. We leveraged Solr's edismax query parser that scores documents by the similarity score between the page content and the sum of bi-gram and uni-gram queries. No query expansion (nqe) was applied. 

---
#### rmit_lm_psg.max 
[**`Participants`**](./participants.md#rmit) | [**`Proceedings`**](./proceedings.md#rmit-trec-2016-dynamic-domain-track-exploiting-passage-representation-for-retrieval-and-relevance-feedback) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/rmit_lm_psg.max.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** rmit_lm_psg.max 
- :fontawesome-solid-user-group: **Participant:** RMIT 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/8/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** We split documents into half overlapped passages with a passage size of 200 words and index them as documents alongside their parent documents in Apache Solr. We then use Solr's block join query to score documents based on the maximum of their passage level relevance scores. The method scores passages using the sum of the passage language model score for a unigram query and a bigram based phrase query. 

---
#### rmit_lm_rocchio.Rp.NRd.10 
[**`Participants`**](./participants.md#rmit) | [**`Proceedings`**](./proceedings.md#rmit-trec-2016-dynamic-domain-track-exploiting-passage-representation-for-retrieval-and-relevance-feedback) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/rmit_lm_rocchio.Rp.NRd.10.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** rmit_lm_rocchio.Rp.NRd.10 
- :fontawesome-solid-user-group: **Participant:** RMIT 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/9/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** We use the content of documents to build a content language model and get the top 5 documents. We then use the Rocchio algorithm to reformulate the current iteration query using the feedback provided by JIG. To represent relevant documents, we concatenate relevant passages from relevant documents into a pseudo relevant passages (Rp) whereas we use the content of the non relevant documents as the non relevant units of Rocchio (NRd). Lastly, we use the top 10 non negative terms from the new query vector generated by Rocchio to build the new query. In addition, we set Rocchio parameters to alpha=1, beta=0.75 and gamma=0.25. 

---
#### rmit_oracle.lm.1000 
[**`Participants`**](./participants.md#rmit) | [**`Proceedings`**](./proceedings.md#rmit-trec-2016-dynamic-domain-track-exploiting-passage-representation-for-retrieval-and-relevance-feedback) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/rmit_oracle.lm.1000.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** rmit_oracle.lm.1000 
- :fontawesome-solid-user-group: **Participant:** RMIT 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/8/2016 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** We run Solr with the content language model to get the first 1000 documents, then we use the ground truth to remove non relevant documents from the initial list of documents. For each iteration, we return the next 5 relevant documents from the initial list. A document is relevant if it was found in the topic's list of judged documents. The motive is to estimate an upper bound of the task and understand if the first 1000 documents are enough to get all relevant documents. 

---
#### SecondIterationBaseline 
[**`Participants`**](./participants.md#georgetown) | [**`Proceedings`**](./proceedings.md#an-investigation-of-basic-retrieval-models-for-the-dynamic-domain-task) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/SecondIterationBaseline.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** SecondIterationBaseline 
- :fontawesome-solid-user-group: **Participant:** georgetown 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/9/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Baseline for using feedback 
- :material-code-tags: **Code:** [https://github.com/NeginR/DD16](https://github.com/NeginR/DD16) 

---
#### TenthIterBaseline 
[**`Participants`**](./participants.md#georgetown) | [**`Proceedings`**](./proceedings.md#an-investigation-of-basic-retrieval-models-for-the-dynamic-domain-task) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/TenthIterBaseline.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** TenthIterBaseline 
- :fontawesome-solid-user-group: **Participant:** georgetown 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/9/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Baseline for tenth iteration 
- :material-code-tags: **Code:** [https://github.com/NeginR/DD16](https://github.com/NeginR/DD16) 

---
#### ufmgHM2 
[**`Participants`**](./participants.md#ufmg) | [**`Proceedings`**](./proceedings.md#ufmg-at-the-trec-2016-dynamic-domain-track) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/ufmgHM2.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** ufmgHM2 
- :fontawesome-solid-user-group: **Participant:** ufmg 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/6/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Hierarchical diversification with multi-source subtopics and cumulative stopping condition. 

---
#### ufmgHM3 
[**`Participants`**](./participants.md#ufmg) | [**`Proceedings`**](./proceedings.md#ufmg-at-the-trec-2016-dynamic-domain-track) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/ufmgHM3.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** ufmgHM3 
- :fontawesome-solid-user-group: **Participant:** ufmg 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/6/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Hierarchical diversification with multi-source subtopics and window-based stopping condition. 

---
#### ufmgHS2 
[**`Participants`**](./participants.md#ufmg) | [**`Proceedings`**](./proceedings.md#ufmg-at-the-trec-2016-dynamic-domain-track) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/ufmgHS2.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** ufmgHS2 
- :fontawesome-solid-user-group: **Participant:** ufmg 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/6/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Hierarchical diversification with single-source subtopics and cumulative stopping condition. 

---
#### ufmgXM2 
[**`Participants`**](./participants.md#ufmg) | [**`Proceedings`**](./proceedings.md#ufmg-at-the-trec-2016-dynamic-domain-track) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/ufmgXM2.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** ufmgXM2 
- :fontawesome-solid-user-group: **Participant:** ufmg 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/6/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Flat diversification with multi-source subtopics and cumulative stopping condition. 

---
#### ufmgXS2 
[**`Participants`**](./participants.md#ufmg) | [**`Proceedings`**](./proceedings.md#ufmg-at-the-trec-2016-dynamic-domain-track) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/ufmgXS2.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** ufmgXS2 
- :fontawesome-solid-user-group: **Participant:** ufmg 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/6/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Flat diversification with single-source subtopics and cumulative stopping condition. 

---
#### UL_BM25 
[**`Participants`**](./participants.md#lavallakehead) | [**`Proceedings`**](./proceedings.md#laval-university-at-trec-dynamic-domain-2016-subtopic-extraction-focused-on-named-entities) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/UL_BM25.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** UL_BM25 
- :fontawesome-solid-user-group: **Participant:** LavalLakehead 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/8/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** BM25 similarity 

---
#### UL_Kmeans 
[**`Participants`**](./participants.md#lavallakehead) | [**`Proceedings`**](./proceedings.md#laval-university-at-trec-dynamic-domain-2016-subtopic-extraction-focused-on-named-entities) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/UL_Kmeans.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** UL_Kmeans 
- :fontawesome-solid-user-group: **Participant:** LavalLakehead 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/8/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Kmeans applied on a subset of documents retrieved by Solr, best document of each cluster is returned to the user. 

---
#### UL_LDA_200 
[**`Participants`**](./participants.md#lavallakehead) | [**`Proceedings`**](./proceedings.md#laval-university-at-trec-dynamic-domain-2016-subtopic-extraction-focused-on-named-entities) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/UL_LDA_200.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** UL_LDA_200 
- :fontawesome-solid-user-group: **Participant:** LavalLakehead 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/8/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** LDA is used to create 5 different topics from documents. We take 100 results from Solr, we remove documents which are too similar to others documents, then we fill the dataset with other documents to have 100 document to run LDA over the sample. 

---
#### UL_LDA_NE 
[**`Participants`**](./participants.md#lavallakehead) | [**`Proceedings`**](./proceedings.md#laval-university-at-trec-dynamic-domain-2016-subtopic-extraction-focused-on-named-entities) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/UL_LDA_NE.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** UL_LDA_NE 
- :fontawesome-solid-user-group: **Participant:** LavalLakehead 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/8/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** LDA used on a corpus of 25 documents from solr, Oriented for NE topics by reducing the text from each document to sentences which contains a part of the NE. 

---
#### UL_LDA_Psum 
[**`Participants`**](./participants.md#lavallakehead) | [**`Proceedings`**](./proceedings.md#laval-university-at-trec-dynamic-domain-2016-subtopic-extraction-focused-on-named-entities) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/UL_LDA_Psum.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** UL_LDA_Psum 
- :fontawesome-solid-user-group: **Participant:** LavalLakehead 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/8/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** Probability for each document to be assigned to each topic multiplied by the global probability of each topic to obtain the document which covers the maximum of topic information. 

---
#### UPD_IA_BiQBDiJ 
[**`Participants`**](./participants.md#upd_ia) | [**`Proceedings`**](./proceedings.md#evaluation-of-a-feedback-algorithm-inspired-by-quantum-detection-for-dynamic-search-tasks) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/UPD_IA_BiQBDiJ.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** UPD_IA_BiQBDiJ 
- :fontawesome-solid-user-group: **Participant:** UPD_IA 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/9/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** BM25 followed by max 5 iterations of feedback based on an algorithm inspired by Quantum Detection (QB) that exploits binary representation for documents. Feedback consists in re-ranking the (residual) top 1000 documents. When relevant documents are present in the feedback set explicit feedback is performed; when no relevant documents are present, residual collection is re-ranked by PRF on the top 100 documents. Description selection is based on WPQ; top 35 terms + topic terms are used. After two PRF-based re-ranking no additional iterations are performed. 

---
#### UPD_IA_BiQBFi 
[**`Participants`**](./participants.md#upd_ia) | [**`Proceedings`**](./proceedings.md#evaluation-of-a-feedback-algorithm-inspired-by-quantum-detection-for-dynamic-search-tasks) | [**`Input`**](https://trec.nist.gov/results/trec25/domain/UPD_IA_BiQBFi.gz) | [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf) 

- :material-rename: **Run ID:** UPD_IA_BiQBFi 
- :fontawesome-solid-user-group: **Participant:** UPD_IA 
- :material-format-text: **Track:** Dynamic Domain 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/7/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-text: **Run description:** BM25 followed by 5 iterations of feedback based on an algorithm inspired by Quantum Detection (QB) that exploits binary representation for documents. Feedback consists in re-ranking the (residual) top 1000 documents. When relevant documents are present in the feedback set explicit feedback is performed; when no relevant documents are present, residual collection is re-ranked by PRF on the top 100 documents. Description selection is based on WPQ; top 35 terms + topic terms are used. 

---
