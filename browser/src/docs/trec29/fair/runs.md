# Runs - Fair Ranking 2020 

#### Deltr-gammas 
[**`Participants`**](./participants.md#mtg), [**`Proceedings`**](./proceedings.md#balancing-exposure-and-relevance-in-academic-search), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.Deltr-gammas.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.Deltr-gammas), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/Deltr-gammas.pdf) 

- :material-rename: **Run ID:** Deltr-gammas 
- :fontawesome-solid-user-group: **Participant:** MTG 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/25/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `136501c4245817369a32e8ab9e3d4ed3` 
- :material-text: **Run description:** In this solution, we train two Deltr models using gamma values of zero and one. The models are trained using 'H class' as the protected attribute. We combine the results of both models using a parameter that makes different reranks for the same query. 

---
#### LM-rel-groups 
[**`Participants`**](./participants.md#mtg), [**`Proceedings`**](./proceedings.md#balancing-exposure-and-relevance-in-academic-search), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.LM-rel-groups.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.LM-rel-groups), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/LM-rel-groups.pdf) 

- :material-rename: **Run ID:** LM-rel-groups 
- :fontawesome-solid-user-group: **Participant:** MTG 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/25/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `3064088722ff00e93209df9f1c9dd5da` 
- :material-text: **Run description:** In this solution, we use the relevance predicted with LambdaMART and rerank the results by only selecting one paper of each group until every group has a paper in the ranking.  We compute the groups by clustering the authors from the graph of collaborations. To compute the clusters, we use the Louvain algorithm. 

---
#### LM-rel-year-100 
[**`Participants`**](./participants.md#mtg), [**`Proceedings`**](./proceedings.md#balancing-exposure-and-relevance-in-academic-search), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.LM-rel-year-100.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.LM-rel-year-100), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/LM-rel-year-100.pdf) 

- :material-rename: **Run ID:** LM-rel-year-100 
- :fontawesome-solid-user-group: **Participant:** MTG 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/25/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `c82d9af3a67e66d9c398b7cf1b6e23de` 
- :material-text: **Run description:** This solution is the same as the previous "LM-relev-year" but using a smaller number of sequences for training LambdaMart (100 instead of 10000) 

---
#### LM-relev-year 
[**`Participants`**](./participants.md#mtg), [**`Proceedings`**](./proceedings.md#balancing-exposure-and-relevance-in-academic-search), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.LM-relev-year.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.LM-relev-year), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/LM-relev-year.pdf) 

- :material-rename: **Run ID:** LM-relev-year 
- :fontawesome-solid-user-group: **Participant:** MTG 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/25/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `b2b918a3d839f70870822fc915dce378` 
- :material-text: **Run description:** This solution is the same as "LM-relevance" but including the attribute "year" as a feature for LambdaMART. 

---
#### LM-relevance 
[**`Participants`**](./participants.md#mtg), [**`Proceedings`**](./proceedings.md#balancing-exposure-and-relevance-in-academic-search), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.LM-relevance.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.LM-relevance), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/LM-relevance.pdf) 

- :material-rename: **Run ID:** LM-relevance 
- :fontawesome-solid-user-group: **Participant:** MTG 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/24/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `1b1c71898ccdd2d4cc468a15077962e4` 
- :material-text: **Run description:** This submission uses the lambdamart to learn-to-rank and randomizes the results based on the predicted relevance 

---
#### MacEwan-base 
[**`Participants`**](./participants.md#macewan_biz), [**`Proceedings`**](./proceedings.md#macewan-university-at-the-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.MacEwan-base.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.MacEwan-base), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/MacEwan-base.pdf) 

- :material-rename: **Run ID:** MacEwan-base 
- :fontawesome-solid-user-group: **Participant:** MacEwan_Biz 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `13e19d7a8241840a4f04e23457afc0d8` 
- :material-text: **Run description:** Baseline run, similar to 2019 submission. Documents are ranked based on BM25 scores from query against title and abstract fields. The two rankings are merged. As the query repeats in the sequence, the weights used for merging the two lists are shifted. 

---
#### MacEwan-norm 
[**`Participants`**](./participants.md#macewan_biz), [**`Proceedings`**](./proceedings.md#macewan-university-at-the-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.MacEwan-norm.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.MacEwan-norm), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/MacEwan-norm.pdf) 

- :material-rename: **Run ID:** MacEwan-norm 
- :fontawesome-solid-user-group: **Participant:** MacEwan_Biz 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `d6407362bcdc74b1bf8864244a686295` 
- :material-text: **Run description:** The same as MacEwan-base, except normalized similarity scores are used for merging instead of ranks. 

---
#### NLE_META_99_1 
[**`Participants`**](./participants.md#nle), [**`Proceedings`**](./proceedings.md#naver-labs-europe-at-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.NLE_META_99_1.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.NLE_META_99_1), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/NLE_META_99_1.pdf) 

- :material-rename: **Run ID:** NLE_META_99_1 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/29/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `af839f3d174764ad17c4fe3b3418e587` 
- :material-text: **Run description:** Fairness is achieved by a P-controller that ensures that actual exposures for authors are as close as possible to their target exposures. This run uses the following controller gains: 0.99 for relevance and 0.01 for unfairness. The base re-ranker only use metadata (year, number of citations, ...) and content (i.e. text) information. 

---
#### NLE_META_9_1 
[**`Participants`**](./participants.md#nle), [**`Proceedings`**](./proceedings.md#naver-labs-europe-at-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.NLE_META_9_1.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.NLE_META_9_1), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/NLE_META_9_1.pdf) 

- :material-rename: **Run ID:** NLE_META_9_1 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/29/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `f4be06fddae406acdcf59b9230b3eef7` 
- :material-text: **Run description:** Fairness is achieved by a P-controller that ensures that actual exposures for authors are as close as possible to their target exposures. This run uses the following controller gains : 0.9 for relevance and 0.1 for unfairness. The base re-ranker only use metadata (year, number of citations, ...) and content (i.e. text) information. 

---
#### NLE_META_PKL 
[**`Participants`**](./participants.md#nle), [**`Proceedings`**](./proceedings.md#naver-labs-europe-at-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.NLE_META_PKL.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.NLE_META_PKL), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/NLE_META_PKL.pdf) 

- :material-rename: **Run ID:** NLE_META_PKL 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/29/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `421d0c6a2ace139fc4328da9b272b9d8` 
- :material-text: **Run description:** It is our baseline run. Fairness is achieved by drawing rankings from a PK-Luce Distribution to randomize the PRP-based re-ranker. The base re-ranker uses metadata (year, number of citations, ...) and content (i.e. text) information. 

---
#### NLE_TEXT_99_1 
[**`Participants`**](./participants.md#nle), [**`Proceedings`**](./proceedings.md#naver-labs-europe-at-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.NLE_TEXT_99_1.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.NLE_TEXT_99_1), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/NLE_TEXT_99_1.pdf) 

- :material-rename: **Run ID:** NLE_TEXT_99_1 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/29/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `67e14bbabfb52fe56dad5efa136563d3` 
- :material-text: **Run description:** Fairness is achieved by a P-controller that ensures that actual exposures for authors are as close as possible to their target exposures. This run uses the following controller gains: 0.99 for relevance and 0.01 for unfairness. The base re-ranker only use content (i.e. text) information. 

---
#### NLE_TEXT_9_1 
[**`Participants`**](./participants.md#nle), [**`Proceedings`**](./proceedings.md#naver-labs-europe-at-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.NLE_TEXT_9_1.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.NLE_TEXT_9_1), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/NLE_TEXT_9_1.pdf) 

- :material-rename: **Run ID:** NLE_TEXT_9_1 
- :fontawesome-solid-user-group: **Participant:** NLE 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/29/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `2e9a11219fff82effabd9a9ff290392b` 
- :material-text: **Run description:** Fairness is achieved by a P-controller that ensures that actual exposures for authors are as close as possible to their target exposures. This run uses the following controller gains : 0.9 for relevance and 0.1 for unfairness.. The base re-ranker only uses content (i.e. text) information. 

---
#### umd_relfair_ltr 
[**`Participants`**](./participants.md#umd_ir), [**`Proceedings`**](./proceedings.md#the-university-of-maryland-at-the-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.umd_relfair_ltr.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.umd_relfair_ltr), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/umd_relfair_ltr.pdf) 

- :material-rename: **Run ID:** umd_relfair_ltr 
- :fontawesome-solid-user-group: **Participant:** UMD_IR 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `5d2fb3c535785b80f0f8074b6512e3a0` 
- :material-text: **Run description:** Listwise learning to rank trying to optimize a custom evaluation measure that balances between relevance and fairness. The method is static and no state between rankings. 

---
#### UoGTrBComFu 
[**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-at-the-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UoGTrBComFu.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UoGTrBComFu), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UoGTrBComFu.pdf) 

- :material-rename: **Run ID:** UoGTrBComFu 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/29/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `1c54995218333d31cccd043fec53f327` 
- :material-text: **Run description:** This run builds on the Terrier.org IR platform, to rank documents by relevance before applying a fairness component that aims to be fair to a number of organically discovered communities that are generated using a graph embeddings approach. This variant of the approach deploys data fusion to promote different communities over time. 

---
#### UoGTrBComPro 
[**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-at-the-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UoGTrBComPro.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UoGTrBComPro), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UoGTrBComPro.pdf) 

- :material-rename: **Run ID:** UoGTrBComPro 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `d4a7ce8ace7ce3a98a99e1494e9121d7` 
- :material-text: **Run description:** This run builds on the Terrier.org IR platform, to rank documents by relevance before applying a fairness component that aims to be fair to a number of organically discovered communities that are generated using a graph embeddings approach. This variant of the approach ranks documents by combining the first-pass retrieval relevance score with community similarity scores to provide a fair exposure to the documents throughout the ranking. 

---
#### UoGTrBComRel 
[**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-at-the-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UoGTrBComRel.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UoGTrBComRel), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UoGTrBComRel.pdf) 

- :material-rename: **Run ID:** UoGTrBComRel 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `58252b40c94923ab82282127059406d6` 
- :material-text: **Run description:** This run builds on the Terrier.org IR platform, to rank documents by relevance before applying a fairness component that aims to be fair to a number of organically discovered communities that are generated using a graph embeddings approach. This variant of the approach ranks documents by combining the first-pass retrieval relevance score with community similarity scores to provide a fair exposure to the documents in the ranking that are predicted to be most relevant. 

---
#### UoGTrBRel 
[**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-at-the-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UoGTrBRel.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UoGTrBRel), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UoGTrBRel.pdf) 

- :material-rename: **Run ID:** UoGTrBRel 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `e1bd3a9b2fc60811dbe9f0a20bd9708d` 
- :material-text: **Run description:** This run simply consists in ranking, for each instance of a query in the sequence, the documents according to their relevance with respect to the query. No fairness component is explicitly enforced. 

---
#### UoGTrComRel 
[**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-at-the-trec-2020-fair-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UoGTrComRel.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UoGTrComRel), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UoGTrComRel.pdf) 

- :material-rename: **Run ID:** UoGTrComRel 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `11c4542c8ec1c7aa16398c8236659d11` 
- :material-text: **Run description:** This run builds on the Terrier.org IR platform, to rank documents by relevance before applying a fairness component that aims to be fair to a number of organically discovered communities that are generated using a graph embeddings approach. This variant of the approach ranks documents by combining the first-pass retrieval relevance score with community similarity scores to provide a fair exposure to the documents in the ranking that are predicted to be most relevant. This approach differs from our UoGTrBComRel run in the first-pass retrieval model. 

---
#### UW_bm25 
[**`Participants`**](./participants.md#infoseeking), [**`Proceedings`**](./proceedings.md#university-of-washington-at-trec-2020-fairness-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UW_bm25.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UW_bm25), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UW_bm25.pdf) 

- :material-rename: **Run ID:** UW_bm25 
- :fontawesome-solid-user-group: **Participant:** InfoSeeking 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/27/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `8fa716bda68877fb695c53e522d609a3` 
- :material-text: **Run description:** Used the output of OkapiBM25 directly for this run. OkapiBM25 how we judge the relevance of a document for a given query. As such, we predict this run will have the best utility. 

---
#### UW_Kr_r0g0c100 
[**`Participants`**](./participants.md#infoseeking), [**`Proceedings`**](./proceedings.md#university-of-washington-at-trec-2020-fairness-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UW_Kr_r0g0c100.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UW_Kr_r0g0c100), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UW_Kr_r0g0c100.pdf) 

- :material-rename: **Run ID:** UW_Kr_r0g0c100 
- :fontawesome-solid-user-group: **Participant:** InfoSeeking 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/27/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `e77f30749ec10035f83a642fa993597f` 
- :material-text: **Run description:** Static method. Uses KL-Divergence to optimize fairness for predicted country groups (advanced/developing economies). Reference distribution is the overall country distribution for the query. Comparison distribution is the distribution of the documents up to rank i. 

---
#### UW_Kr_r0g100c0 
[**`Participants`**](./participants.md#infoseeking), [**`Proceedings`**](./proceedings.md#university-of-washington-at-trec-2020-fairness-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UW_Kr_r0g100c0.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UW_Kr_r0g100c0), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UW_Kr_r0g100c0.pdf) 

- :material-rename: **Run ID:** UW_Kr_r0g100c0 
- :fontawesome-solid-user-group: **Participant:** InfoSeeking 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/27/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `d73f85fc4eed43d0801d42a1e0a80db2` 
- :material-text: **Run description:** Static method. Uses KL-Divergence to optimize fairness for predicted gender groups. Reference distribution is the overall gender distribution for the query. Comparison distribution is the distribution of the documents up to rank i. 

---
#### UW_Kr_r25g25c50 
[**`Participants`**](./participants.md#infoseeking), [**`Proceedings`**](./proceedings.md#university-of-washington-at-trec-2020-fairness-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UW_Kr_r25g25c50.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UW_Kr_r25g25c50), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UW_Kr_r25g25c50.pdf) 

- :material-rename: **Run ID:** UW_Kr_r25g25c50 
- :fontawesome-solid-user-group: **Participant:** InfoSeeking 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/27/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `d86c19d7da127b523dc2f7027ac23f23` 
- :material-text: **Run description:** Static method. Reranked based on 3 parameters: relevance (from OkapiBM25), gender distribution of authors, and geographic distribution of authors (2 groups--advanced/developing nations). Weighted parameters at 25%, 25%, and 50%, respectively. Used KL-Divergence to assess fairness of author group distributions up to i. The reference distributions are the overall group distributions for a query. 

---
#### UW_Kr_r60g20c20 
[**`Participants`**](./participants.md#infoseeking), [**`Proceedings`**](./proceedings.md#university-of-washington-at-trec-2020-fairness-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UW_Kr_r60g20c20.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UW_Kr_r60g20c20), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UW_Kr_r60g20c20.pdf) 

- :material-rename: **Run ID:** UW_Kr_r60g20c20 
- :fontawesome-solid-user-group: **Participant:** InfoSeeking 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/27/2020 
- :material-text-search: **Task:** rerank 
- :material-fingerprint: **MD5:** `ea5504235b903c20d3dd132df769cb52` 
- :material-text: **Run description:** Static method. Reranked based on 3 parameters: relevance (from OkapiBM25), gender distribution of authors, and geographic distribution of authors (2 groups--advanced/developing nations). Weighted parameters at 60%, 20%, and 20%, respectively. Used KL-Divergence to assess fairness of author group distributions up to i. The reference distributions are the overall group distributions for a query. 

---
#### UW_Kt_r0g0c100 
[**`Participants`**](./participants.md#infoseeking), [**`Proceedings`**](./proceedings.md#university-of-washington-at-trec-2020-fairness-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UW_Kt_r0g0c100.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UW_Kt_r0g0c100), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UW_Kt_r0g0c100.pdf) 

- :material-rename: **Run ID:** UW_Kt_r0g0c100 
- :fontawesome-solid-user-group: **Participant:** InfoSeeking 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `045981ed5b1cfb91473ebc3946b5c266` 
- :material-text: **Run description:** Static method. Retrieves top 100 results using OkapiBM25, then reranks based solely on predicted geographic groups of authors (advanced/developing nations). Document i in the reranked list results in the minimum KL-Divergence between group distribution up to i compared to the overall distribution for the query. 

---
#### UW_Kt_r25g25c50 
[**`Participants`**](./participants.md#infoseeking), [**`Proceedings`**](./proceedings.md#university-of-washington-at-trec-2020-fairness-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UW_Kt_r25g25c50.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UW_Kt_r25g25c50), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UW_Kt_r25g25c50.pdf) 

- :material-rename: **Run ID:** UW_Kt_r25g25c50 
- :fontawesome-solid-user-group: **Participant:** InfoSeeking 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `f955e1ee90e0b6d82dca0888203a1c85` 
- :material-text: **Run description:** Static method. Retrieves top 100 results using OkapiBM25, then reranks based  on relevance (OkapiBM25 score), gender distribution, and country distribution (advanced/developing). Parameters weighted at 25%, 25%, and 50%, respectively. 

---
#### UW_Kt_r60g20c20 
[**`Participants`**](./participants.md#infoseeking), [**`Proceedings`**](./proceedings.md#university-of-washington-at-trec-2020-fairness-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UW_Kt_r60g20c20.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UW_Kt_r60g20c20), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UW_Kt_r60g20c20.pdf) 

- :material-rename: **Run ID:** UW_Kt_r60g20c20 
- :fontawesome-solid-user-group: **Participant:** InfoSeeking 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `88c49ca236f445a525baea26c5c9f1d6` 
- :material-text: **Run description:** Static method. Retrieves top 100 results using OkapiBM25, then reranks based  on relevance (OkapiBM25 score), gender distribution, and country distribution (advanced/developing). Parameters weighted at 60%, 20%, and 20%, respectively. 

---
#### UW_Kt_r80g10c10 
[**`Participants`**](./participants.md#infoseeking), [**`Proceedings`**](./proceedings.md#university-of-washington-at-trec-2020-fairness-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UW_Kt_r80g10c10.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UW_Kt_r80g10c10), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UW_Kt_r80g10c10.pdf) 

- :material-rename: **Run ID:** UW_Kt_r80g10c10 
- :fontawesome-solid-user-group: **Participant:** InfoSeeking 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `1b1b6b5a26772f32ce66c2759e254de4` 
- :material-text: **Run description:** Static method. Retrieves top 100 results using OkapiBM25, then reranks based  on relevance (OkapiBM25 score), gender distribution, and country distribution (advanced/developing). Parameters weighted at 80%, 10%, and 10%, respectively. 

---
#### UW_t_bm25 
[**`Participants`**](./participants.md#infoseeking), [**`Proceedings`**](./proceedings.md#university-of-washington-at-trec-2020-fairness-ranking-track), [**`Input`**](https://trec.nist.gov/results/trec29/fair/input.UW_t_bm25.tgz), [**`Summary`**](https://trec.nist.gov/results/trec29/fair/summary.UW_t_bm25), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/fair/UW_t_bm25.pdf) 

- :material-rename: **Run ID:** UW_t_bm25 
- :fontawesome-solid-user-group: **Participant:** InfoSeeking 
- :material-format-text: **Track:** Fair Ranking 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `28ee2d36ed8e9a094b9e8c31e9dbb4ab` 
- :material-text: **Run description:** Static method. Result of running OkapiBM25 with no reranking of the top 100 results. 

---
