# Runs - CrisisFACTs 2022 

#### BM25_Heuristic_ILP 
[**`Participants`**](./participants.md#ohm_kiz), [**`Proceedings`**](./proceedings.md#combining-deep-neural-reranking-and-unsupervised-extraction-for-multi-query-focused-summarization), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.BM25_Heuristic_ILP.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.BM25_Heuristic_ILP.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.BM25_Heuristic_ILP.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/BM25_Heuristic_ILP.pdf) 

- :material-rename: **Name:** BM25_Heuristic_ILP 
- :fontawesome-solid-user-group: **Participant:** ohm_kiz 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `a3507adbba6da822745b49797641f7d6` 
- :material-text: **Run description:** The system consists of three successive components: 1: Lexical retrieval with BM25 based on indicative terms + query text (top 100 per query) 2: Heuristical re-ranking with selected entity concepts based on bag-of-entities and bag-of-keywords (top 25 per query) 3: ILP-system for diversified sentence selection in terms of covered entities and queries + MMR for re-ranking (top 150 stream items)  

---
#### BM25_QAasnq_ILP 
[**`Participants`**](./participants.md#ohm_kiz), [**`Proceedings`**](./proceedings.md#combining-deep-neural-reranking-and-unsupervised-extraction-for-multi-query-focused-summarization), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.BM25_QAasnq_ILP.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.BM25_QAasnq_ILP.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.BM25_QAasnq_ILP.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/BM25_QAasnq_ILP.pdf) 

- :material-rename: **Name:** BM25_QAasnq_ILP 
- :fontawesome-solid-user-group: **Participant:** ohm_kiz 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `456ec14b698bef9b4ac71737f48ef028` 
- :material-text: **Run description:** The system consists of three successive components: 1: Lexical retrieval with BM25 based on indicative terms + query text (top 100 per query) 2: QA re-ranking with RoBERTa pretrained on ASNQ dataset (top 25 per query) 3: ILP-system for diversified sentence selection in terms of covered entities and queries + MMR for re-ranking (top 150 stream items)  

---
#### BM25_QAcrisis_ILP 
[**`Participants`**](./participants.md#ohm_kiz), [**`Proceedings`**](./proceedings.md#combining-deep-neural-reranking-and-unsupervised-extraction-for-multi-query-focused-summarization), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.BM25_QAcrisis_ILP.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.BM25_QAcrisis_ILP.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.BM25_QAcrisis_ILP.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/BM25_QAcrisis_ILP.pdf) 

- :material-rename: **Name:** BM25_QAcrisis_ILP 
- :fontawesome-solid-user-group: **Participant:** ohm_kiz 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `3ce572e66ebbcc2c1962a2927c0fcde1` 
- :material-text: **Run description:** The system consists of three successive components: 1: Lexical retrieval with BM25 based on indicative terms + query text (top 100 per query) 2: QA re-ranking with RoBERTa pretrained on ASNQ dataset and finetuned on synthesized CrisisQA DocEE-dataset (top 25 per query) 3: ILP-system for diversified sentence selection in terms of covered entities and queries + MMR for re-ranking (top 150 stream items)  

---
#### ColBERT_ILP 
[**`Participants`**](./participants.md#ohm_kiz), [**`Proceedings`**](./proceedings.md#combining-deep-neural-reranking-and-unsupervised-extraction-for-multi-query-focused-summarization), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.ColBERT_ILP.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.ColBERT_ILP.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.ColBERT_ILP.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/ColBERT_ILP.pdf) 

- :material-rename: **Name:** ColBERT_ILP 
- :fontawesome-solid-user-group: **Participant:** ohm_kiz 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `aec521ba94511d6c500110089d877930` 
- :material-text: **Run description:** The system consists of two successive components: 1: Late interaction retrieval with ColBERTv2 pretrained on MS-MARCO dataset (top 25 per query) 2: ILP-system for diversified sentence selection in terms of covered entities and queries + MMR for re-ranking (top 150 stream items)  

---
#### combsum 
[**`Participants`**](./participants.md#umcp), [**`Proceedings`**](./proceedings.md#multi-faceted-question-fusion-in-the-trec-2022-crisisfacts-track), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.combsum.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.combsum.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.combsum.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/combsum.pdf) 

- :material-rename: **Name:** combsum 
- :fontawesome-solid-user-group: **Participant:** umcp 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/27/2022 
- :material-fingerprint: **MD5:** `b8f8229fa999c59432ac206bf4650d76` 

---
#### eXSum22_submission_01 
[**`Participants`**](./participants.md#exsum22), [**`Proceedings`**](./proceedings.md#l3s-at-the-trec-2022-crisisfacts-track), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.eXSum22_submission_01.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.eXSum22_submission_01.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.eXSum22_submission_01.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/eXSum22_submission_01.pdf) 

- :material-rename: **Name:** eXSum22_submission_01 
- :fontawesome-solid-user-group: **Participant:** eXSum22 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/28/2022 
- :material-fingerprint: **MD5:** `7cd5cc3b844d4f00d5849ca1097d29b0` 

---
#### eXSum22_submission_02 
[**`Participants`**](./participants.md#exsum22), [**`Proceedings`**](./proceedings.md#l3s-at-the-trec-2022-crisisfacts-track), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.eXSum22_submission_02.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.eXSum22_submission_02.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.eXSum22_submission_02.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/eXSum22_submission_02.pdf) 

- :material-rename: **Name:** eXSum22_submission_02 
- :fontawesome-solid-user-group: **Participant:** eXSum22 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/28/2022 
- :material-fingerprint: **MD5:** `c505ef012404ccb8b76e4391e6e04e1a` 

---
#### IRIT_IRIS_mean_USE 
[**`Participants`**](./participants.md#irit_iris), [**`Proceedings`**](./proceedings.md#irit-iris-at-trec-2022-crisisfacts-track), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.IRIT_IRIS_mean_USE.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.IRIT_IRIS_mean_USE.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.IRIT_IRIS_mean_USE.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/IRIT_IRIS_mean_USE.pdf) 

- :material-rename: **Name:** IRIT_IRIS_mean_USE 
- :fontawesome-solid-user-group: **Participant:** IRIT_IRIS 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `f4632573ba9a20959d0c0a379c853c07` 
- :material-text: **Run description:** The system computes the importance as the similarity between an item and a potential Oracle summary automatically constructed. The potential Oracle summary is created using the mean of all the items of the daily stream, regarding a specific representation. 

---
#### IRIT_IRIS_mean_USE_INeeds 
[**`Participants`**](./participants.md#irit_iris), [**`Proceedings`**](./proceedings.md#irit-iris-at-trec-2022-crisisfacts-track), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.IRIT_IRIS_mean_USE_INeeds.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.IRIT_IRIS_mean_USE_INeeds.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.IRIT_IRIS_mean_USE_INeeds.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/IRIT_IRIS_mean_USE_INeeds.pdf) 

- :material-rename: **Name:** IRIT_IRIS_mean_USE_INeeds 
- :fontawesome-solid-user-group: **Participant:** IRIT_IRIS 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `cee9540e286567c7b74ef58486939477` 
- :material-text: **Run description:** The system computes the importance as the similarity between an item and a potential Oracle summary automatically constructed. The potential Oracle summary is created using the mean of all the items of the daily stream, regarding a specific representation, for a particular query.  

---
#### IRIT_IRIS_tssubert 
[**`Participants`**](./participants.md#irit_iris), [**`Proceedings`**](./proceedings.md#irit-iris-at-trec-2022-crisisfacts-track), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.IRIT_IRIS_tssubert.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.IRIT_IRIS_tssubert.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.IRIT_IRIS_tssubert.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/IRIT_IRIS_tssubert.pdf) 

- :material-rename: **Name:** IRIT_IRIS_tssubert 
- :fontawesome-solid-user-group: **Participant:** IRIT_IRIS 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `71ba6f77d21a67daac9acf850412ac76` 
- :material-text: **Run description:** The system computes the importance using a neural pre-trained language model and the frequency of the tokens of the stream. Then, the system selects items to keep in the summary using redundancy removal in the manner of MMR. 

---
#### mrr_all 
[**`Participants`**](./participants.md#umcp), [**`Proceedings`**](./proceedings.md#multi-faceted-question-fusion-in-the-trec-2022-crisisfacts-track), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.mrr_all.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.mrr_all.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.mrr_all.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/mrr_all.pdf) 

- :material-rename: **Name:** mrr_all 
- :fontawesome-solid-user-group: **Participant:** umcp 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/27/2022 
- :material-fingerprint: **MD5:** `b4a265bb9b2ce304b16260bd881cf848` 

---
#### mrr_main 
[**`Participants`**](./participants.md#umcp), [**`Proceedings`**](./proceedings.md#multi-faceted-question-fusion-in-the-trec-2022-crisisfacts-track), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.mrr_main.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.mrr_main.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.mrr_main.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/mrr_main.pdf) 

- :material-rename: **Name:** mrr_main 
- :fontawesome-solid-user-group: **Participant:** umcp 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/27/2022 
- :material-fingerprint: **MD5:** `92d1646335d699d1fb4c3356b94bcdc6` 

---
#### mrr_no_dd 
[**`Participants`**](./participants.md#umcp), [**`Proceedings`**](./proceedings.md#multi-faceted-question-fusion-in-the-trec-2022-crisisfacts-track), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.mrr_no_dd.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.mrr_no_dd.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.mrr_no_dd.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/mrr_no_dd.pdf) 

- :material-rename: **Name:** mrr_no_dd 
- :fontawesome-solid-user-group: **Participant:** umcp 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/27/2022 
- :material-fingerprint: **MD5:** `97a6fe205be3703d5db7189ec93da9f8` 

---
#### mrr_nobrf 
[**`Participants`**](./participants.md#umcp), [**`Proceedings`**](./proceedings.md#multi-faceted-question-fusion-in-the-trec-2022-crisisfacts-track), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.mrr_nobrf.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.mrr_nobrf.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.mrr_nobrf.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/mrr_nobrf.pdf) 

- :material-rename: **Name:** mrr_nobrf 
- :fontawesome-solid-user-group: **Participant:** umcp 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/27/2022 
- :material-fingerprint: **MD5:** `ef398813cc156941996634e058c6c253` 

---
#### mrr_sum 
[**`Participants`**](./participants.md#umcp), [**`Proceedings`**](./proceedings.md#multi-faceted-question-fusion-in-the-trec-2022-crisisfacts-track), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.mrr_sum.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.mrr_sum.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.mrr_sum.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/mrr_sum.pdf) 

- :material-rename: **Name:** mrr_sum 
- :fontawesome-solid-user-group: **Participant:** umcp 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/27/2022 
- :material-fingerprint: **MD5:** `7256442e1de357513b9c8863b1a9a302` 

---
#### nazmultum11 
[**`Participants`**](./participants.md#sipeo), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.nazmultum11.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.nazmultum11.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.nazmultum11.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/nazmultum11.pdf) 

- :material-rename: **Name:** nazmultum11 
- :fontawesome-solid-user-group: **Participant:** SiPEO 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-fingerprint: **MD5:** `f8852e87d24969fe1355a791b38249c4` 
- :material-text: **Run description:** for a single day run and single requestID, after downloading the dataframe it goes through text cleaning process (stop words, http links and emojis). For the queries, only stop words have removed. A SentenceTransformer model have been used to calculating the similiarity measurement ('sentence-transformers/all-mpnet-base-v2'). Then both the text and queries have sent to a function where against each query, the top 5 best maching sentecne has picked based on cosine similiarity. Then all of the sentences-->query pair has sorted based on the 'importance score' ( = cosine similiarity), then top 100 pair has been selected as a facts after removing the duplication when applied (retained the highest score pair in case of duplication). And then for the each pair of output, a output dataframe have formed with the respective information regarding text and query. The final output is the concat form of all the day-->requestID pair. And finally the dataframe transform to the submitted json format.    

---
#### NM-1 
[**`Participants`**](./participants.md#nmunicamp), [**`Proceedings`**](./proceedings.md#using-neural-reranking-and-gpt-3-for-social-media-disaster-content-summarization), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.NM-1.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.NM-1.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.NM-1.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/NM-1.pdf) 

- :material-rename: **Name:** NM-1 
- :fontawesome-solid-user-group: **Participant:** NM.unicamp 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `d460ee1cfcb5236651f809c3920ae74c` 
- :material-text: **Run description:** We follow the traditional two-step retrieve-and-aggregate approach to solve the task. In the first step, we leverage a state-of-the-art search engine to retrieve candidate passages from the event collection of streams. In the second step, we use GPT-3 in a few-shot setting to generate a verbose explanation of the passages' contents before outputting an answer. We use the generated explanation as the fact text. 

---
#### NM-2 
[**`Participants`**](./participants.md#nmunicamp), [**`Proceedings`**](./proceedings.md#using-neural-reranking-and-gpt-3-for-social-media-disaster-content-summarization), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.NM-2.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.NM-2.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.NM-2.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/NM-2.pdf) 

- :material-rename: **Name:** NM-2 
- :fontawesome-solid-user-group: **Participant:** NM.unicamp 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `b71a9d507349bdd9599484459dad770f` 
- :material-text: **Run description:** We follow the traditional two-step retrieve-and-aggregate approach to solve the task. In the first step, we leverage a state-of-the-art search engine to retrieve candidate passages from the event collection of streams. In the second step, we use GPT-3 in a few-shot setting to generate a verbose explanation of the passages' contents before outputting an answer. We use the generated explanation as the fact text. In this run, we applied a pos-processing step for removing extra white spaces 

---
#### rr_now 
[**`Participants`**](./participants.md#umcp), [**`Proceedings`**](./proceedings.md#multi-faceted-question-fusion-in-the-trec-2022-crisisfacts-track), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.rr_now.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.rr_now.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.rr_now.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/rr_now.pdf) 

- :material-rename: **Name:** rr_now 
- :fontawesome-solid-user-group: **Participant:** umcp 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/27/2022 
- :material-fingerprint: **MD5:** `ea593fc83c7f2733cf5677e427c01a92` 

---
#### submission_final.json 
[**`Participants`**](./participants.md#iiser22), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.submission_final.json.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.submission_final.json.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.submission_final.json.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/submission_final.json.pdf) 

- :material-rename: **Name:** submission_final.json 
- :fontawesome-solid-user-group: **Participant:** IISER22 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `c76c670a350e2c664b71b541e5abb3bb` 
- :material-text: **Run description:** Atfirst I used Lucene to index all the documents event-day wise.After that I used BM25 Similarity to retrieval relevant document for every query.Here system was selected first five document for each query. 

---
#### submission_final_4 
[**`Participants`**](./participants.md#iiser22), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.submission_final_4.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.submission_final_4.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.submission_final_4.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/submission_final_4.pdf) 

- :material-rename: **Name:** submission_final_4 
- :fontawesome-solid-user-group: **Participant:** IISER22 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `d068480a0681ea24b4765eca2d90c005` 
- :material-text: **Run description:** Atfirst I used Lucene to index all the documents event-day wise.After that I used LMDirichlet Similarity and BM25 similarity to retrieval relevant document for every query.Here system was selected first five document for each query. After that system found common sentences that are present in two json file.Then again calculte their importance and then normalize that. 

---
#### submission_LM_DS_3 
[**`Participants`**](./participants.md#iiser22), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.submission_LM_DS_3.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.submission_LM_DS_3.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.submission_LM_DS_3.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/submission_LM_DS_3.pdf) 

- :material-rename: **Name:** submission_LM_DS_3 
- :fontawesome-solid-user-group: **Participant:** IISER22 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `5314a08fca0717d17ef9089f9ae293bf` 
- :material-text: **Run description:** Atfirst I used Lucene to index all the documents event-day wise.After that I used LMDirichlet Similarity to retrieval relevant document for every query.Here system was selected first five document for each query. 

---
#### submission_LM_JM_2 
[**`Participants`**](./participants.md#iiser22), [**`Input`**](https://trec.nist.gov/results/trec31/crisis/input.submission_LM_JM_2.gz), [**`Summary (auto)`**](https://trec.nist.gov/results/trec31/crisis/summary.submission_LM_JM_2.auto.csv), [**`Summary (manual)`**](https://trec.nist.gov/results/trec31/crisis/summary.submission_LM_JM_2.manual.tar.gz), [**`Appendix`**](https://trec.nist.gov/pubs/trec31/appendices/crisis/submission_LM_JM_2.pdf) 

- :material-rename: **Name:** submission_LM_JM_2 
- :fontawesome-solid-user-group: **Participant:** IISER22 
- :material-format-text: **Track:** CrisisFACTs 
- :material-calendar: **Year:** 2022 
- :material-upload: **Submission:** 9/30/2022 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-fingerprint: **MD5:** `0ad4b26f3c44e9307f9eaa1ef31a5751` 
- :material-text: **Run description:** Atfirst I used Lucene to index all the documents event-day wise.After that I used LMJelinekMercer Similarity to retrieval relevant document for every query.Here system was selected first three document for each query. 

---
