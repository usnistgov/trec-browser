# Runs - Deep Learning 2019 

#### baseline 
[**`Results`**](./results.md#baseline) | [**`Participants`**](./participants.md#bitem_dl) | [**`Proceedings`**](./proceedings.md#sib-text-mining-at-trec-2019-deep-learning-track-working-note) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.baseline.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.baseline) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/baseline.pdf) 

- :material-rename: **Run ID:** baseline 
- :fontawesome-solid-user-group: **Participant:** BITEM_DL 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `857d64201de964f2d9a1f47481e0aac6` 
- :material-text: **Run description:** This is our baseline run, we use document representations and look for the 1000 nearest documents wrt the query. 

---
#### bm25_marcomb 
[**`Results`**](./results.md#bm25_marcomb) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25_marcomb.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25_marcomb) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25_marcomb.pdf) 

- :material-rename: **Run ID:** bm25_marcomb 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/8/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `705962a69ff0163985d5c76e65ac253a` 
- :material-text: **Run description:** BERT Large was pretrained on MS MARCO passages and TREC Microblog data (best model chosen) to learn a sentence relevance model. Top 1000 MS MARCO documents for each query were retrieved with tuned BM25+RM3. MS MARCO documents were then split into sentences and fed into the BERT model to predict a relevance score for each sentence. Top 3 most relevant sentence scores and document scores were combined to rerank the documents. 

---
#### bm25base 
[**`Results`**](./results.md#bm25base) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25base.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25base) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25base.pdf) 

- :material-rename: **Run ID:** bm25base 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `1920f64b68ff7077641e0c83f087c8c0` 
- :material-text: **Run description:** Top 1000 documents with BM25 with default parameters 

---
#### bm25base_ax 
[**`Results`**](./results.md#bm25base_ax) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25base_ax.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25base_ax) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25base_ax.pdf) 

- :material-rename: **Run ID:** bm25base_ax 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `e3b1dcc5acf0ba9752bbca82d9d59b3c` 
- :material-text: **Run description:** Top 1000 documents with BM25+AX with default parameters 

---
#### bm25base_ax_p 
[**`Results`**](./results.md#bm25base_ax_p) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25base_ax_p.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25base_ax_p) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.bm25base_ax_p) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25base_ax_p.pdf) 

- :material-rename: **Run ID:** bm25base_ax_p 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `59d6b6f67217a4b99f4dd5b434040c6d` 
- :material-text: **Run description:** Top 1000 passages with BM25+Ax with default parameters 

---
#### bm25base_p 
[**`Results`**](./results.md#bm25base_p) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25base_p.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25base_p) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.bm25base_p) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25base_p.pdf) 

- :material-rename: **Run ID:** bm25base_p 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `5aac87b215c8de3fbc735b4912d60950` 
- :material-text: **Run description:** Top 1000 passages with BM25 with default parameters 

---
#### bm25base_prf 
[**`Results`**](./results.md#bm25base_prf) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25base_prf.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25base_prf) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25base_prf.pdf) 

- :material-rename: **Run ID:** bm25base_prf 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `1c0316ecfce3f20d399570dfbb261c4a` 
- :material-text: **Run description:** Top 1000 documents with BM25+PRF with default parameters 

---
#### bm25base_prf_p 
[**`Results`**](./results.md#bm25base_prf_p) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25base_prf_p.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25base_prf_p) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.bm25base_prf_p) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25base_prf_p.pdf) 

- :material-rename: **Run ID:** bm25base_prf_p 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `c52d47b73259ee80049717611bdb61f2` 
- :material-text: **Run description:** Top 1000 passages with BM25+PRF with default parameters 

---
#### bm25base_rm3 
[**`Results`**](./results.md#bm25base_rm3) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25base_rm3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25base_rm3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25base_rm3.pdf) 

- :material-rename: **Run ID:** bm25base_rm3 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `f20421717658a585c2d8affb5f36d979` 
- :material-text: **Run description:** Top 1000 documents with BM25+RM3 with default parameters 

---
#### bm25base_rm3_p 
[**`Results`**](./results.md#bm25base_rm3_p) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25base_rm3_p.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25base_rm3_p) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.bm25base_rm3_p) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25base_rm3_p.pdf) 

- :material-rename: **Run ID:** bm25base_rm3_p 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `ef08f82918ca1c85a0bfb456dae078ae` 
- :material-text: **Run description:** Top 1000 passages with BM25+RM3 with default parameters 

---
#### bm25exp_marco 
[**`Results`**](./results.md#bm25exp_marco) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25exp_marco.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25exp_marco) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25exp_marco.pdf) 

- :material-rename: **Run ID:** bm25exp_marco 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/8/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `f678bf0b376b0fcd88e61cf0bea2c21f` 
- :material-text: **Run description:** BERT Large was pretrained on MS MARCO passages (best model chosen) to learn a sentence relevance model. MS MARCO documents were expanded with doc2query model (https://github.com/nyu-dl/dl4ir-doc2query) and indexed. Top 1000 documents for each query were retrieved with tuned BM25+RM3. MS MARCO documents were then split into sentences and fed into the BERT model to predict a relevance score for each sentence. Top 3 most relevant sentence scores and document scores were combined to rerank the documents. 

---
#### bm25exp_marcomb 
[**`Results`**](./results.md#bm25exp_marcomb) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25exp_marcomb.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25exp_marcomb) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25exp_marcomb.pdf) 

- :material-rename: **Run ID:** bm25exp_marcomb 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/8/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `fa49e8581ca4424f44aa9d61788ddec5` 
- :material-text: **Run description:** BERT Large was pretrained on MS MARCO passages and TREC Microblog data (best model chosen) to learn a sentence relevance model. MS MARCO documents were expanded with doc2query model (https://github.com/nyu-dl/dl4ir-doc2query) and indexed. Top 1000 documents for each query were retrieved with tuned BM25+RM3. MS MARCO documents were then split into sentences and fed into the BERT model to predict a relevance score for each sentence. Top 3 most relevant sentence scores and document scores were combined to rerank the documents. 

---
#### bm25tuned 
[**`Results`**](./results.md#bm25tuned) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25tuned.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25tuned) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25tuned.pdf) 

- :material-rename: **Run ID:** bm25tuned 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `d827b52134f84e9230b1a19e4c7db6e4` 
- :material-text: **Run description:** Top 1000 documents with BM25 with tuned parameters 

---
#### bm25tuned_ax 
[**`Results`**](./results.md#bm25tuned_ax) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25tuned_ax.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25tuned_ax) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25tuned_ax.pdf) 

- :material-rename: **Run ID:** bm25tuned_ax 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `c0d005a5edd5296d3b8100ef33600e93` 
- :material-text: **Run description:** Top 1000 documents with BM25+AX with tuned parameters 

---
#### bm25tuned_ax_p 
[**`Results`**](./results.md#bm25tuned_ax_p) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25tuned_ax_p.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25tuned_ax_p) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.bm25tuned_ax_p) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25tuned_ax_p.pdf) 

- :material-rename: **Run ID:** bm25tuned_ax_p 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `25f66f5b4feeb4d6ef23caf8b481f78b` 
- :material-text: **Run description:** Top 1000 passages with BM25+Ax with tuned parameters 

---
#### bm25tuned_p 
[**`Results`**](./results.md#bm25tuned_p) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25tuned_p.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25tuned_p) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.bm25tuned_p) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25tuned_p.pdf) 

- :material-rename: **Run ID:** bm25tuned_p 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `3e84dd3903e79cb61efcb9859ed84505` 
- :material-text: **Run description:** Top 1000 passages with BM25 with tuned parameters 

---
#### bm25tuned_prf 
[**`Results`**](./results.md#bm25tuned_prf) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25tuned_prf.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25tuned_prf) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25tuned_prf.pdf) 

- :material-rename: **Run ID:** bm25tuned_prf 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `9750d48d3bb75e238b20ba5516e7b1f7` 
- :material-text: **Run description:** Top 1000 documents with BM25+PRF with tuned parameters 

---
#### bm25tuned_prf_p 
[**`Results`**](./results.md#bm25tuned_prf_p) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25tuned_prf_p.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25tuned_prf_p) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.bm25tuned_prf_p) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25tuned_prf_p.pdf) 

- :material-rename: **Run ID:** bm25tuned_prf_p 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `c7ad436bab74c41b0678b4766021c8ec` 
- :material-text: **Run description:** Top 1000 passages with BM25+PRF with tuned parameters 

---
#### bm25tuned_rm3 
[**`Results`**](./results.md#bm25tuned_rm3) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25tuned_rm3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25tuned_rm3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25tuned_rm3.pdf) 

- :material-rename: **Run ID:** bm25tuned_rm3 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `14b4c312e0aae7b5c6b49677727f409a` 
- :material-text: **Run description:** Top 1000 documents with BM25+RM3 with tuned parameters 

---
#### bm25tuned_rm3_p 
[**`Results`**](./results.md#bm25tuned_rm3_p) | [**`Participants`**](./participants.md#baseline) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.bm25tuned_rm3_p.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.bm25tuned_rm3_p) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.bm25tuned_rm3_p) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/bm25tuned_rm3_p.pdf) 

- :material-rename: **Run ID:** bm25tuned_rm3_p 
- :fontawesome-solid-user-group: **Participant:** BASELINE 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `4ec6d4b34f715d7099a12928401d47bd` 
- :material-text: **Run description:** Top 1000 passages with BM25+RM3 with tuned parameters 

---
#### dct_qp_bm25e 
[**`Results`**](./results.md#dct_qp_bm25e) | [**`Participants`**](./participants.md#cmu) | [**`Proceedings`**](./proceedings.md#an-evaluation-of-weakly-supervised-deepct-in-the-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.dct_qp_bm25e.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.dct_qp_bm25e) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/dct_qp_bm25e.pdf) 

- :material-rename: **Run ID:** dct_qp_bm25e 
- :fontawesome-solid-user-group: **Participant:** CMU 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `1342681203a58e35832de6158af33391` 
- :material-text: **Run description:** The run uses a deep model, called DeepCT, to generate term weights for the body field of the documents. DeepCT model is trained with document task training labels. Documents are indexed with the term weights and retrieved with BM25. BM25 scores on titles, URLs, and the reweighted bodies are combined linearly. 

---
#### dct_tp_bm25e 
[**`Results`**](./results.md#dct_tp_bm25e) | [**`Participants`**](./participants.md#cmu) | [**`Proceedings`**](./proceedings.md#an-evaluation-of-weakly-supervised-deepct-in-the-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.dct_tp_bm25e.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.dct_tp_bm25e) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/dct_tp_bm25e.pdf) 

- :material-rename: **Run ID:** dct_tp_bm25e 
- :fontawesome-solid-user-group: **Participant:** CMU 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `b5a726b15c4dc5c8a3cf2ebebf0d084d` 
- :material-text: **Run description:** The run uses a deep model, called DeepCT, to generate term weights for the body field of the documents. DeepCT model is trained in a unsupervised manner using document titles as pseudo-queries. Documents are indexed with the term weights and retrieved with BM25. BM25 scores on titles, URLs, and the reweighted bodies are combined linearly. 

---
#### dct_tp_bm25e2 
[**`Results`**](./results.md#dct_tp_bm25e2) | [**`Participants`**](./participants.md#cmu) | [**`Proceedings`**](./proceedings.md#an-evaluation-of-weakly-supervised-deepct-in-the-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.dct_tp_bm25e2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.dct_tp_bm25e2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/dct_tp_bm25e2.pdf) 

- :material-rename: **Run ID:** dct_tp_bm25e2 
- :fontawesome-solid-user-group: **Participant:** CMU 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `e56b1607247755d264ff64a4403cea83` 
- :material-text: **Run description:** The run uses a deep model, called DeepCT, to generate term weights for the body field of the documents. DeepCT model is trained in a unspuervised manner using the doucment titles as pseudo-queries. Documents are indexed with the term weights and retrieved with BM25. BM25 scores on titles, URLs, the original body, and the reweighted bodies are combined linearly. 

---
#### ICT-BERT2 
[**`Results`**](./results.md#ict-bert2) | [**`Participants`**](./participants.md#ictnet) | [**`Proceedings`**](./proceedings.md#ictnet-at-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.ICT-BERT2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.ICT-BERT2) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.ICT-BERT2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/ICT-BERT2.pdf) 

- :material-rename: **Run ID:** ICT-BERT2 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `4391b8ffe5d2f2b0b8b53a32dc375ca9` 
- :material-text: **Run description:** Document Expansion by Query Prediction -> BM25 (top20) -> BERT 

---
#### ICT-CKNRM_B 
[**`Results`**](./results.md#ict-cknrm_b) | [**`Participants`**](./participants.md#ictnet) | [**`Proceedings`**](./proceedings.md#ictnet-at-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.ICT-CKNRM_B.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.ICT-CKNRM_B) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.ICT-CKNRM_B) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/ICT-CKNRM_B.pdf) 

- :material-rename: **Run ID:** ICT-CKNRM_B 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/13/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `727181ecee66f28bc671d6bed70db281` 
- :material-text: **Run description:** Document Expansion by Query Prediction -> BM25 (top20) -> BERT + ConvKNRM 

---
#### ICT-CKNRM_B50 
[**`Results`**](./results.md#ict-cknrm_b50) | [**`Participants`**](./participants.md#ictnet) | [**`Proceedings`**](./proceedings.md#ictnet-at-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.ICT-CKNRM_B50.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.ICT-CKNRM_B50) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.ICT-CKNRM_B50) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/ICT-CKNRM_B50.pdf) 

- :material-rename: **Run ID:** ICT-CKNRM_B50 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/13/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `49f3c8d3bf1d9ef607c7ee0169581ac2` 
- :material-text: **Run description:** Document Expansion by Query Prediction -> BM25 (top50) -> BERT + ConvKNRM 

---
#### idst_bert_p1 
[**`Results`**](./results.md#idst_bert_p1) | [**`Participants`**](./participants.md#idst) | [**`Proceedings`**](./proceedings.md#idst-at-trec-2019-deep-learning-track-deep-cascade-ranking-with-generation-based-document-expansion-and-pre-trained-language-modeling) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.idst_bert_p1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.idst_bert_p1) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.idst_bert_p1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/idst_bert_p1.pdf) 

- :material-rename: **Run ID:** idst_bert_p1 
- :fontawesome-solid-user-group: **Participant:** IDST 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `0951a1154ddfd0530a27e9b1fbbb797e` 
- :material-text: **Run description:** enriched bert base model + index 

---
#### idst_bert_p2 
[**`Results`**](./results.md#idst_bert_p2) | [**`Participants`**](./participants.md#idst) | [**`Proceedings`**](./proceedings.md#idst-at-trec-2019-deep-learning-track-deep-cascade-ranking-with-generation-based-document-expansion-and-pre-trained-language-modeling) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.idst_bert_p2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.idst_bert_p2) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.idst_bert_p2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/idst_bert_p2.pdf) 

- :material-rename: **Run ID:** idst_bert_p2 
- :fontawesome-solid-user-group: **Participant:** IDST 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `2090a13b1bbe6c55f8f9e7f22f8784c8` 
- :material-text: **Run description:** enriched bert base + index p2 

---
#### idst_bert_p3 
[**`Results`**](./results.md#idst_bert_p3) | [**`Participants`**](./participants.md#idst) | [**`Proceedings`**](./proceedings.md#idst-at-trec-2019-deep-learning-track-deep-cascade-ranking-with-generation-based-document-expansion-and-pre-trained-language-modeling) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.idst_bert_p3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.idst_bert_p3) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.idst_bert_p3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/idst_bert_p3.pdf) 

- :material-rename: **Run ID:** idst_bert_p3 
- :fontawesome-solid-user-group: **Participant:** IDST 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `7b228eda6897505d5e0c7f3c2ae80341` 
- :material-text: **Run description:** enriched bert base + index p3 

---
#### idst_bert_pr1 
[**`Results`**](./results.md#idst_bert_pr1) | [**`Participants`**](./participants.md#idst) | [**`Proceedings`**](./proceedings.md#idst-at-trec-2019-deep-learning-track-deep-cascade-ranking-with-generation-based-document-expansion-and-pre-trained-language-modeling) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.idst_bert_pr1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.idst_bert_pr1) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.idst_bert_pr1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/idst_bert_pr1.pdf) 

- :material-rename: **Run ID:** idst_bert_pr1 
- :fontawesome-solid-user-group: **Participant:** IDST 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `cfa078c5b80a9c3d91c1ac41cf62065a` 
- :material-text: **Run description:** directly enriched bert base version 1 

---
#### idst_bert_pr2 
[**`Results`**](./results.md#idst_bert_pr2) | [**`Participants`**](./participants.md#idst) | [**`Proceedings`**](./proceedings.md#idst-at-trec-2019-deep-learning-track-deep-cascade-ranking-with-generation-based-document-expansion-and-pre-trained-language-modeling) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.idst_bert_pr2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.idst_bert_pr2) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.idst_bert_pr2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/idst_bert_pr2.pdf) 

- :material-rename: **Run ID:** idst_bert_pr2 
- :fontawesome-solid-user-group: **Participant:** IDST 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `c99c376be5a0e203ed3b8c3014881812` 
- :material-text: **Run description:** direct enriched bert base version 2 

---
#### idst_bert_r1 
[**`Results`**](./results.md#idst_bert_r1) | [**`Participants`**](./participants.md#idst) | [**`Proceedings`**](./proceedings.md#idst-at-trec-2019-deep-learning-track-deep-cascade-ranking-with-generation-based-document-expansion-and-pre-trained-language-modeling) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.idst_bert_r1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.idst_bert_r1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/idst_bert_r1.pdf) 

- :material-rename: **Run ID:** idst_bert_r1 
- :fontawesome-solid-user-group: **Participant:** IDST 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/5/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `e0b57cc3e55714b2776db280c2c24b75` 
- :material-text: **Run description:** directly enriched bert base trained on msmarco data version 1 

---
#### idst_bert_r2 
[**`Results`**](./results.md#idst_bert_r2) | [**`Participants`**](./participants.md#idst) | [**`Proceedings`**](./proceedings.md#idst-at-trec-2019-deep-learning-track-deep-cascade-ranking-with-generation-based-document-expansion-and-pre-trained-language-modeling) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.idst_bert_r2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.idst_bert_r2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/idst_bert_r2.pdf) 

- :material-rename: **Run ID:** idst_bert_r2 
- :fontawesome-solid-user-group: **Participant:** IDST 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/5/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `df6baf60a3b4f10d94ecb74602460fe1` 
- :material-text: **Run description:** directly enriched bert base trained on msmarco data version 2 

---
#### idst_bert_v1 
[**`Results`**](./results.md#idst_bert_v1) | [**`Participants`**](./participants.md#idst) | [**`Proceedings`**](./proceedings.md#idst-at-trec-2019-deep-learning-track-deep-cascade-ranking-with-generation-based-document-expansion-and-pre-trained-language-modeling) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.idst_bert_v1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.idst_bert_v1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/idst_bert_v1.pdf) 

- :material-rename: **Run ID:** idst_bert_v1 
- :fontawesome-solid-user-group: **Participant:** IDST 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/4/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `415a9521852c4e5edaa9e4dddb2105b6` 
- :material-text: **Run description:** direct enriched bert base v1 

---
#### idst_bert_v2 
[**`Results`**](./results.md#idst_bert_v2) | [**`Participants`**](./participants.md#idst) | [**`Proceedings`**](./proceedings.md#idst-at-trec-2019-deep-learning-track-deep-cascade-ranking-with-generation-based-document-expansion-and-pre-trained-language-modeling) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.idst_bert_v2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.idst_bert_v2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/idst_bert_v2.pdf) 

- :material-rename: **Run ID:** idst_bert_v2 
- :fontawesome-solid-user-group: **Participant:** IDST 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/4/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `7ed3ff0445703ba45fa2c776e59d8609` 
- :material-text: **Run description:** direct enriched bert base v2 

---
#### idst_bert_v3 
[**`Results`**](./results.md#idst_bert_v3) | [**`Participants`**](./participants.md#idst) | [**`Proceedings`**](./proceedings.md#idst-at-trec-2019-deep-learning-track-deep-cascade-ranking-with-generation-based-document-expansion-and-pre-trained-language-modeling) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.idst_bert_v3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.idst_bert_v3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/idst_bert_v3.pdf) 

- :material-rename: **Run ID:** idst_bert_v3 
- :fontawesome-solid-user-group: **Participant:** IDST 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/5/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `4bf3f4294d8e9946020ec0eea92e8578` 
- :material-text: **Run description:** enriched bert base model trained on msmarco data version 3 

---
#### ms_duet 
[**`Results`**](./results.md#ms_duet) | [**`Participants`**](./participants.md#microsoft) | [**`Proceedings`**](./proceedings.md#duet-at-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.ms_duet.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.ms_duet) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/ms_duet.pdf) 

- :material-rename: **Run ID:** ms_duet 
- :fontawesome-solid-user-group: **Participant:** Microsoft 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `203ab15c3c98acf29c21b36fd53f510e` 
- :material-text: **Run description:** This submission is combines the Duet model (Mitra et al.) with the NRMF model (Zamani et al.). We first train the model using a distant supervision strategy (treating document URL and title as pseudo-queries) on the document collection provided by the track. Then we train the model using the labeled training data provided by the track. Word embeddings were trained on the corpus provided. No external data is used for this run. 

---
#### ms_duet_passage 
[**`Results`**](./results.md#ms_duet_passage) | [**`Participants`**](./participants.md#microsoft) | [**`Proceedings`**](./proceedings.md#duet-at-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.ms_duet_passage.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.ms_duet_passage) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.ms_duet_passage) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/ms_duet_passage.pdf) 

- :material-rename: **Run ID:** ms_duet_passage 
- :fontawesome-solid-user-group: **Participant:** Microsoft 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/12/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `e1ff08a4b94f1811ed20709b5e870d7b` 
- :material-text: **Run description:** This submission consists of an ensemble (via bagging) of 8 Duet models. The word embedding input to the model was trained using FastText on the document collection. 

---
#### ms_ensemble 
[**`Results`**](./results.md#ms_ensemble) | [**`Participants`**](./participants.md#microsoft) | [**`Proceedings`**](./proceedings.md#duet-at-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.ms_ensemble.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.ms_ensemble) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/ms_ensemble.pdf) 

- :material-rename: **Run ID:** ms_ensemble 
- :fontawesome-solid-user-group: **Participant:** Microsoft 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `9910772fad6e3ec5f5b264ad19436d79` 
- :material-text: **Run description:** First retrieved 100 candidates using Sequential Dependence Model (SDM) and then re-ranked the candidates using a neural Learning to Rank (LTR) model that combined Duet, SDM, PRF, BM25, DESM, and other features. 

---
#### p_bert 
[**`Results`**](./results.md#p_bert) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.p_bert.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.p_bert) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.p_bert) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/p_bert.pdf) 

- :material-rename: **Run ID:** p_bert 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `9b0c168666dc4d0b004ab781890650c1` 
- :material-text: **Run description:** Top 1000 passages for each query were retrieved with tuned BM25. The candidate passages were reranked with BERT. 

---
#### p_exp_bert 
[**`Results`**](./results.md#p_exp_bert) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.p_exp_bert.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.p_exp_bert) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.p_exp_bert) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/p_exp_bert.pdf) 

- :material-rename: **Run ID:** p_exp_bert 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `3e0ee3361ee04f3341c2d621f353d5f5` 
- :material-text: **Run description:** A transformer model was trained on MS MARCO passage and queries to learn how to predict potential queries given a passage. (https://github.com/nyu-dl/dl4ir-doc2query) The passages in the corpus were expanded with 10 samples for each passage based on top k sampling and indexed. Top 1000 passages for each query were retrieved with tuned BM25. The candidate passages were reranked with BERT. 

---
#### p_exp_rm3_bert 
[**`Results`**](./results.md#p_exp_rm3_bert) | [**`Participants`**](./participants.md#h2oloo) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.p_exp_rm3_bert.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.p_exp_rm3_bert) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.p_exp_rm3_bert) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/p_exp_rm3_bert.pdf) 

- :material-rename: **Run ID:** p_exp_rm3_bert 
- :fontawesome-solid-user-group: **Participant:** h2oloo 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `832915218da143bbc9fe35d419598a83` 
- :material-text: **Run description:** A transformer model was trained on MS MARCO passage and queries to learn how to predict potential queries given a passage. (https://github.com/nyu-dl/dl4ir-doc2query) The passages in the corpus were expanded with 10 samples for each passage based on top k sampling and indexed. Top 1000 passages for each query were retrieved with tuned BM25+RM3. The candidate passages were reranked with BERT. 

---
#### query2doc_RNN 
[**`Results`**](./results.md#query2doc_rnn) | [**`Participants`**](./participants.md#bitem_dl) | [**`Proceedings`**](./proceedings.md#sib-text-mining-at-trec-2019-deep-learning-track-working-note) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.query2doc_RNN.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.query2doc_RNN) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/query2doc_RNN.pdf) 

- :material-rename: **Run ID:** query2doc_RNN 
- :fontawesome-solid-user-group: **Participant:** BITEM_DL 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/8/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `6daaf7e8620ad1c83149f983c8582a49` 
- :material-text: **Run description:** We first used our baseline approach (with a high recall) to retrieve a manageable amount of documents that will later be used for training (negative + positive documents that are near). Using a RNN framework we computed the score of each document wrt a query that were returned by our baseline approach. 

---
#### runid1 
[**`Results`**](./results.md#runid1) | [**`Participants`**](./participants.md#ccnu_irgroup) | [**`Proceedings`**](./proceedings.md#ccnu-irgroup-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.runid1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.runid1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/runid1.pdf) 

- :material-rename: **Run ID:** runid1 
- :fontawesome-solid-user-group: **Participant:** CCNU_IRGroup 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/6/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `5aad612a84d156887a7467e2a719b6e9` 
- :material-text: **Run description:** 1)Use the Bert model(Jacob Devlin et al., 2018) pre-trained on wikipedia. 2)Fine-tune the Bert on MNLI dataset In our experiment, we use the fine-tuned BERT model to calculate the similarity score between the query and each sentence of a document. Then we use the weighted sum of the scores of the top three sentences as the relevance score for the document and the query and rerank the documents by it. 

---
#### runid2 
[**`Results`**](./results.md#runid2) | [**`Participants`**](./participants.md#ccnu_irgroup) | [**`Proceedings`**](./proceedings.md#ccnu-irgroup-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.runid2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.runid2) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.runid2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/runid2.pdf) 

- :material-rename: **Run ID:** runid2 
- :fontawesome-solid-user-group: **Participant:** CCNU_IRGroup 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/13/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `33d761a7cc7cc54cc14249bdbf54fc88` 
- :material-text: **Run description:** 1)Use the Bert model(Jacob Devlin et al., 2018) pre-trained on wikipedia. 2)Use the GloVe embedding(glove.840B.300d.txt). In this task, we use BERT as a feature-based Approach. we use the features extracted by BERT as the input of a neural model consisted of the bidirectional LSTM and the attention mechanism,and then use this model to calculate the similarity score between the query and the passage. Finally,we calculate the weighted sum of the neural model calculated score and the BM25 calculated score as the final relevance score for the passage and the query. 

---
#### runid3 
[**`Results`**](./results.md#runid3) | [**`Participants`**](./participants.md#udel_fang) | [**`Proceedings`**](./proceedings.md#higway-bert-for-passage-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.runid3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.runid3) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.runid3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/runid3.pdf) 

- :material-rename: **Run ID:** runid3 
- :fontawesome-solid-user-group: **Participant:** udel_fang 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/11/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `08834d448962007184bd80424bd1c1f1` 
- :material-text: **Run description:** Training data: msmarco training data set. Unsupervised model: BERT. Supervised model: BERT Encodre+ Highway Network + Multilayer Perceptron + Axioms. Loss function: Cross Entropy Loss. 

---
#### runid4 
[**`Results`**](./results.md#runid4) | [**`Participants`**](./participants.md#udel_fang) | [**`Proceedings`**](./proceedings.md#higway-bert-for-passage-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.runid4.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.runid4) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.runid4) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/runid4.pdf) 

- :material-rename: **Run ID:** runid4 
- :fontawesome-solid-user-group: **Participant:** udel_fang 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/13/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `46feb649f2ac9808162ad59ec2c21a8c` 
- :material-text: **Run description:** unsupervised model: BERT-base supervised model: BERT-base + Highway network + Cross entropy 

---
#### runid5 
[**`Results`**](./results.md#runid5) | [**`Participants`**](./participants.md#ccnu_irgroup) | [**`Proceedings`**](./proceedings.md#ccnu-irgroup-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.runid5.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.runid5) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.runid5) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/runid5.pdf) 

- :material-rename: **Run ID:** runid5 
- :fontawesome-solid-user-group: **Participant:** CCNU_IRGroup 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `70b49829ec0572b6cba58b3b0767483e` 
- :material-text: **Run description:** 1)Use the Bert model(Jacob Devlin et al., 2018) pre-trained on wikipedia. 2)Use the GloVe embedding(glove.840B.300d.txt).  In this task, we use BERT as a feature-based Approach. we use the features extracted by BERT as the input of a neural model consisted of the bidirectional LSTM and the attention mechanism,and then use this model to calculate the similarity score between the query and the passage. Finally,we calculate the weighted sum of the neural model calculated score and the BM25 calculated score as the final relevance score for the passage and the query.  

---
#### srchvrs_ps_run1 
[**`Results`**](./results.md#srchvrs_ps_run1) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.srchvrs_ps_run1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.srchvrs_ps_run1) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.srchvrs_ps_run1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/srchvrs_ps_run1.pdf) 

- :material-rename: **Run ID:** srchvrs_ps_run1 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `92e0e52421042a968074747eab7d7945` 
- :material-text: **Run description:** classic IR 

---
#### srchvrs_ps_run2 
[**`Results`**](./results.md#srchvrs_ps_run2) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.srchvrs_ps_run2.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.srchvrs_ps_run2) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.srchvrs_ps_run2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/srchvrs_ps_run2.pdf) 

- :material-rename: **Run ID:** srchvrs_ps_run2 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `421c11b068185293d30d230f6773f66f` 
- :material-text: **Run description:** classic IR + BERT finetuned 

---
#### srchvrs_ps_run3 
[**`Results`**](./results.md#srchvrs_ps_run3) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.srchvrs_ps_run3.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.srchvrs_ps_run3) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.srchvrs_ps_run3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/srchvrs_ps_run3.pdf) 

- :material-rename: **Run ID:** srchvrs_ps_run3 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/15/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `d45d59ff2731c5b2104ffee8ab17769c` 
- :material-text: **Run description:** classic IR  

---
#### srchvrs_run1 
[**`Results`**](./results.md#srchvrs_run1) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.srchvrs_run1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.srchvrs_run1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/srchvrs_run1.pdf) 

- :material-rename: **Run ID:** srchvrs_run1 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `b0bd10c1f59319dd4eede2ba8bf6823c` 
- :material-text: **Run description:** classic IR 

---
#### srchvrs_run2 
[**`Results`**](./results.md#srchvrs_run2) | [**`Participants`**](./participants.md#srchvrs) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.srchvrs_run2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.srchvrs_run2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/srchvrs_run2.pdf) 

- :material-rename: **Run ID:** srchvrs_run2 
- :fontawesome-solid-user-group: **Participant:** srchvrs 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/8/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `528fceb23e6be219f581820510db0ea9` 
- :material-text: **Run description:** classic IR 

---
#### test1 
[**`Results`**](./results.md#test1) | [**`Participants`**](./participants.md#brown) | [**`Proceedings`**](./proceedings.md#brown-university-at-trec-deep-learning-2019) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.test1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.test1) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.test1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/test1.pdf) 

- :material-rename: **Run ID:** test1 
- :fontawesome-solid-user-group: **Participant:** Brown 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/14/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `92cefe4c093da8b7e065785c9960361b` 
- :material-text: **Run description:** A transformer sequence to sequence model was used to predict related queries from the original query. To train the "query-to-query" model, the qrels file was used to find pairs of related queries (i.e. queries corresponding to the same passage). The original query was subsequently expanded by the predicted related queries. A BERT-based reranking model was used to rerank candidate passages, based on the expanded query. 

---
#### TUA1-1 
[**`Results`**](./results.md#tua1-1) | [**`Participants`**](./participants.md#tua1) | [**`Proceedings`**](./proceedings.md#tua1-at-the-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUA1-1.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUA1-1) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.TUA1-1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUA1-1.pdf) 

- :material-rename: **Run ID:** TUA1-1 
- :fontawesome-solid-user-group: **Participant:** TUA1 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 7/29/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `72046970d4103b6a7763a094758ff4f3` 
- :material-text: **Run description:** We used conv-knrm model to rank at first stage.And,then use bert to re-rank the results.Training data set is MS MARCO Train Triples Small.Bert is pre-trained model on MS MARCO.  

---
#### TUW19-d1-f 
[**`Results`**](./results.md#tuw19-d1-f) | [**`Participants`**](./participants.md#tu-vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-trec-deep-learning-19-simple-contextualization-for-re-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUW19-d1-f.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUW19-d1-f) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUW19-d1-f.pdf) 

- :material-rename: **Run ID:** TUW19-d1-f 
- :fontawesome-solid-user-group: **Participant:** TU-Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/5/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `612ae81f87e59c9529204336035bfeee` 
- :material-text: **Run description:** Model: unpublished fast contextualized re-ranking model (capping documents at 200 words) on top of tuned bm25 initial ranking, tuned re-ranking depth to 29 Data: glove-commoncrawl word embeddings (fine-tuned), msmarco documents training data (more samples than from the official script) 

---
#### TUW19-d1-re 
[**`Results`**](./results.md#tuw19-d1-re) | [**`Participants`**](./participants.md#tu-vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-trec-deep-learning-19-simple-contextualization-for-re-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUW19-d1-re.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUW19-d1-re) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUW19-d1-re.pdf) 

- :material-rename: **Run ID:** TUW19-d1-re 
- :fontawesome-solid-user-group: **Participant:** TU-Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/5/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `3850129f84348dd64ce760dc54ad5f1b` 
- :material-text: **Run description:** Model: unpublished fast contextualized re-ranking model (with glove embeddings) Data: glove-commoncrawl embeddings + msmarco document training data (more samples than generated from the official script) 

---
#### TUW19-d2-f 
[**`Results`**](./results.md#tuw19-d2-f) | [**`Participants`**](./participants.md#tu-vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-trec-deep-learning-19-simple-contextualization-for-re-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUW19-d2-f.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUW19-d2-f) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUW19-d2-f.pdf) 

- :material-rename: **Run ID:** TUW19-d2-f 
- :fontawesome-solid-user-group: **Participant:** TU-Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `5d27f867b86db1f1808e1e806c4ccba5` 
- :material-text: **Run description:** Model: unpublished fast contextualized re-ranking model (with glove embeddings) on top of tuned bm25 initial ranking, tuned re-ranking depth to 60 Data: glove-commoncrawl embeddings + msmarco passage (!) training data  

---
#### TUW19-d2-re 
[**`Results`**](./results.md#tuw19-d2-re) | [**`Participants`**](./participants.md#tu-vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-trec-deep-learning-19-simple-contextualization-for-re-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUW19-d2-re.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUW19-d2-re) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUW19-d2-re.pdf) 

- :material-rename: **Run ID:** TUW19-d2-re 
- :fontawesome-solid-user-group: **Participant:** TU-Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `0ba93f6b1c14f0f69e60bbae109104ea` 
- :material-text: **Run description:** Model: unpublished fast contextualized re-ranking model (with glove embeddings) Data: glove-commoncrawl embeddings + msmarco passage (!) training data  

---
#### TUW19-d3-f 
[**`Results`**](./results.md#tuw19-d3-f) | [**`Participants`**](./participants.md#tu-vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-trec-deep-learning-19-simple-contextualization-for-re-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUW19-d3-f.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUW19-d3-f) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUW19-d3-f.pdf) 

- :material-rename: **Run ID:** TUW19-d3-f 
- :fontawesome-solid-user-group: **Participant:** TU-Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `adbadc501e0576cd635ce631036d1ee0` 
- :material-text: **Run description:** Model: unpublished fast contextualized re-ranking model including a document-length specific part-scoring (with fasttext embeddings) on top of tuned bm25 initial ranking, tuned re-ranking depth to 31 Data: fasttext pre-trained on Wikipedia text + msmarco document training data (more samples than the original generator file produced)  

---
#### TUW19-d3-re 
[**`Results`**](./results.md#tuw19-d3-re) | [**`Participants`**](./participants.md#tu-vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-trec-deep-learning-19-simple-contextualization-for-re-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUW19-d3-re.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUW19-d3-re) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUW19-d3-re.pdf) 

- :material-rename: **Run ID:** TUW19-d3-re 
- :fontawesome-solid-user-group: **Participant:** TU-Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `49f6e1ab4ba28326be5fa7e2994af866` 
- :material-text: **Run description:** Model: unpublished fast contextualized re-ranking model including a document-length specific part-scoring (with fasttext embeddings) Data: fasttext pre-trained on Wikipedia text + msmarco document training data (more samples than the original generator file produced)  

---
#### TUW19-p1-f 
[**`Results`**](./results.md#tuw19-p1-f) | [**`Participants`**](./participants.md#tu-vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-trec-deep-learning-19-simple-contextualization-for-re-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUW19-p1-f.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUW19-p1-f) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.TUW19-p1-f) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUW19-p1-f.pdf) 

- :material-rename: **Run ID:** TUW19-p1-f 
- :fontawesome-solid-user-group: **Participant:** TU-Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/5/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `77ff18573996eb97238f4e39cb5da7f7` 
- :material-text: **Run description:** Model: unpublished fast contextualized re-ranking model (with glove embeddings) on top of tuned bm25 initial ranking Data: glove based on commoncrawl + msmarco passage training data  

---
#### TUW19-p1-re 
[**`Results`**](./results.md#tuw19-p1-re) | [**`Participants`**](./participants.md#tu-vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-trec-deep-learning-19-simple-contextualization-for-re-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUW19-p1-re.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUW19-p1-re) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.TUW19-p1-re) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUW19-p1-re.pdf) 

- :material-rename: **Run ID:** TUW19-p1-re 
- :fontawesome-solid-user-group: **Participant:** TU-Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/5/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `c9aae6a6f0657ee0ccbbd8a2a7356bef` 
- :material-text: **Run description:** Model: unpublished fast contextualized re-ranking model (with glove embeddings) Data: glove-commoncrawl embeddings + msmarco passage training data  

---
#### TUW19-p2-f 
[**`Results`**](./results.md#tuw19-p2-f) | [**`Participants`**](./participants.md#tu-vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-trec-deep-learning-19-simple-contextualization-for-re-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUW19-p2-f.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUW19-p2-f) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.TUW19-p2-f) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUW19-p2-f.pdf) 

- :material-rename: **Run ID:** TUW19-p2-f 
- :fontawesome-solid-user-group: **Participant:** TU-Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/5/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `6301aed7af96bb1939d795bb78f7200f` 
- :material-text: **Run description:** Model: unpublished fast contextualized re-ranking model (with fasttext embeddings) on top of tuned bm25 initial ranking, tuned re-ranking depth to 997  Data: fasttext pre-trained on Wikipedia text + msmarco passage training data  

---
#### TUW19-p2-re 
[**`Results`**](./results.md#tuw19-p2-re) | [**`Participants`**](./participants.md#tu-vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-trec-deep-learning-19-simple-contextualization-for-re-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUW19-p2-re.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUW19-p2-re) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.TUW19-p2-re) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUW19-p2-re.pdf) 

- :material-rename: **Run ID:** TUW19-p2-re 
- :fontawesome-solid-user-group: **Participant:** TU-Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/5/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `33e330bb48cb1504c5172034a7e16ecc` 
- :material-text: **Run description:** Model: unpublished fast contextualized re-ranking model (with fasttext embeddings) Data: fasttext pre-trained on Wikipedia text + msmarco passage training data 

---
#### TUW19-p3-f 
[**`Results`**](./results.md#tuw19-p3-f) | [**`Participants`**](./participants.md#tu-vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-trec-deep-learning-19-simple-contextualization-for-re-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUW19-p3-f.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUW19-p3-f) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.TUW19-p3-f) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUW19-p3-f.pdf) 

- :material-rename: **Run ID:** TUW19-p3-f 
- :fontawesome-solid-user-group: **Participant:** TU-Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/5/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `96cbcdd51f75461e58badf030aacecc1` 
- :material-text: **Run description:** Model: ensemble of multiple instances of: unpublished fast contextualized re-ranking model (with glove embeddings) Data: glove-commoncrawl embeddings + msmarco passage training data 

---
#### TUW19-p3-re 
[**`Results`**](./results.md#tuw19-p3-re) | [**`Participants`**](./participants.md#tu-vienna) | [**`Proceedings`**](./proceedings.md#tu-wien-trec-deep-learning-19-simple-contextualization-for-re-ranking) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.TUW19-p3-re.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.TUW19-p3-re) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.TUW19-p3-re) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/TUW19-p3-re.pdf) 

- :material-rename: **Run ID:** TUW19-p3-re 
- :fontawesome-solid-user-group: **Participant:** TU-Vienna 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/5/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `ab55438010d9a6a8df48e68e59aa50b3` 
- :material-text: **Run description:** Model: ensemble of multiple instances of: unpublished fast contextualized re-ranking model (with glove embeddings) Data: glove-commoncrawl embeddings + msmarco passage training data 

---
#### ucas_runid1 
[**`Results`**](./results.md#ucas_runid1) | [**`Participants`**](./participants.md#ucas) | [**`Proceedings`**](./proceedings.md#ucas-at-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.ucas_runid1.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.ucas_runid1) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/ucas_runid1.pdf) 

- :material-rename: **Run ID:** ucas_runid1 
- :fontawesome-solid-user-group: **Participant:** UCAS 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/6/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `920e5871baf5ed2d4881c68a6f38ffc2` 
- :material-text: **Run description:** In this run, we use the neural language model BERT to re-rank the candidate documents. First, documents are split into overlapping passages, and the title is added if it is available. Second, we truncate the query and passage with the maximum length of 256 tokens. Last, we use the [CLS] vector to obtain the score of the passage being relevant, and the score of a document is the score of its best passage. All candidate documents are re-ranked by the document scores received. 

---
#### ucas_runid2 
[**`Results`**](./results.md#ucas_runid2) | [**`Participants`**](./participants.md#ucas) | [**`Proceedings`**](./proceedings.md#ucas-at-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.ucas_runid2.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.ucas_runid2) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/ucas_runid2.pdf) 

- :material-rename: **Run ID:** ucas_runid2 
- :fontawesome-solid-user-group: **Participant:** UCAS 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/6/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `933390b7ecce720aca26d593b952dbe7` 
- :material-text: **Run description:** In this run, we use the neural language model XLNet to re-rank the candidate documents. First, documents are split into overlapping passages, and the title is added if it is available. Second, we truncate the passage with the maximum length of 256 tokens. Last, we use the [CLS] vector to obtain the score of the passage being relevant, and the score of a document is the score of its best passage. All candidate documents are re-ranked by the document scores received. 

---
#### ucas_runid3 
[**`Results`**](./results.md#ucas_runid3) | [**`Participants`**](./participants.md#ucas) | [**`Proceedings`**](./proceedings.md#ucas-at-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.ucas_runid3.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.ucas_runid3) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/ucas_runid3.pdf) 

- :material-rename: **Run ID:** ucas_runid3 
- :fontawesome-solid-user-group: **Participant:** UCAS 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `8a1bf83be17ac19f32e542de8302f45c` 
- :material-text: **Run description:** In this run, we use the neural language model BERT to re-rank the candidate documents. First, documents are split into overlapping passages, and the title is added if it is available. Second, we truncate the query and passage with the maximum length of 256 tokens. Last, we use the [CLS] vector to obtain the score of the passage being relevant, and the score of a document is the score of its best passage. All candidate documents are re-ranked by the document scores received. The train step of this run is different from the run ucas_runid1. 

---
#### UNH_bm25 
[**`Results`**](./results.md#unh_bm25) | [**`Participants`**](./participants.md#trema-unh) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.UNH_bm25.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.UNH_bm25) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.UNH_bm25) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/UNH_bm25.pdf) 

- :material-rename: **Run ID:** UNH_bm25 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/13/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `548bab1b3b1e6c5e3a620dd0b9d35132` 
- :material-text: **Run description:** Run is created using BM25 retrieval method from a lucene index created from collection.tsv and questions as query preprocesses with Lucene Standard analyzer. 

---
#### UNH_exDL_bm25 
[**`Results`**](./results.md#unh_exdl_bm25) | [**`Participants`**](./participants.md#trema-unh) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.UNH_exDL_bm25.gz) | [**`Summary (trec_eval)`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.UNH_exDL_bm25) | [**`Summary (passages-eval)`**](https://trec.nist.gov/results/trec28/deep/summary.passages-eval.UNH_exDL_bm25) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/UNH_exDL_bm25.pdf) 

- :material-rename: **Run ID:** UNH_exDL_bm25 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/13/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** passages 
- :material-fingerprint: **MD5:** `f3d6c5587e3688de7d7a4ec6701d5d25` 
- :material-text: **Run description:** A siamese neural model is trained on preprocessed benchmark Y1 train dataset (http://trec-car.cs.unh.edu/) that models similarity between two pieces of texts embedded using ELMo vectors. This model is used to get a paragraph from benchmark Y1 train dataset which is the most similar to the query and used to expand it. Then BM25 retrieval method is used to rank passages using this expanded query. 

---
#### uogTrDNN6LM 
[**`Results`**](./results.md#uogtrdnn6lm) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-at-the-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.uogTrDNN6LM.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.uogTrDNN6LM) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/uogTrDNN6LM.pdf) 

- :material-rename: **Run ID:** uogTrDNN6LM 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `200a5df592fdde37396c2adc0ecfd7de` 
- :material-text: **Run description:** Build upon the Terrier.org IR platform, a Divergence from Randomness weighting model is used to identify a set of candidate documents, which are further rescored by 6 query-dependent features, including a BERT-based deep learning model. These are combined using a learning-to-rank technique. 

---
#### uogTrDSS6pLM 
[**`Results`**](./results.md#uogtrdss6plm) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-at-the-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.uogTrDSS6pLM.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.uogTrDSS6pLM) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/uogTrDSS6pLM.pdf) 

- :material-rename: **Run ID:** uogTrDSS6pLM 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/8/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `a66a951a7aae0be20619aad9313d497e` 
- :material-text: **Run description:** A Divergence from Randomness weighting model, used to identify a set of candidate documents, which are further rescored by 6 query-dependent features, including BERT-based deep learning models at document and passage levels. These are combined using a learning-to-rank technique. 

---
#### uogTrDSSQE5LM 
[**`Results`**](./results.md#uogtrdssqe5lm) | [**`Participants`**](./participants.md#uogtr) | [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-at-the-trec-2019-deep-learning-track) | [**`Input`**](https://trec.nist.gov/results/trec28/deep/input.uogTrDSSQE5LM.gz) | [**`Summary`**](https://trec.nist.gov/results/trec28/deep/summary.treceval.uogTrDSSQE5LM) | [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/deep/uogTrDSSQE5LM.pdf) 

- :material-rename: **Run ID:** uogTrDSSQE5LM 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Deep Learning 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/7/2019 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** docs 
- :material-fingerprint: **MD5:** `723e70600c416771063eb4b7ae631714` 
- :material-text: **Run description:** Build upon the Terrier.org IR platform, a Divergence from Randomness weighting model with pseudo-relevance feedback is used to identify a set of candidate documents, which are further rescored by 5 query-dependent features, including a BERT-based deep learning model. These are combined using a learning-to-rank technique. 

---
