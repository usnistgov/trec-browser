# Runs - Complex Answer Retrieval 2019 

#### Bert-ConvKNRM 
[**`Participants`**](./participants.md#ictnet), [**`Proceedings`**](./proceedings.md#ictnet-at-trec-2019-complex-answer-retrieval-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/Bert-ConvKNRM.pdf) 

- :material-rename: **Run ID:** Bert-ConvKNRM 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 7/29/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** Document Expansion by Query Prediction -> BM25 -> BERT -> ConvKNRM 

---
#### Bert-ConvKNRM-50 
[**`Participants`**](./participants.md#ictnet), [**`Proceedings`**](./proceedings.md#ictnet-at-trec-2019-complex-answer-retrieval-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/Bert-ConvKNRM-50.pdf) 

- :material-rename: **Run ID:** Bert-ConvKNRM-50 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 7/31/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** Document Expansion by Query Prediction -> BM25 (top 50) -> BERT -> ConvKNRM 

---
#### Bert-DRMMTKS 
[**`Participants`**](./participants.md#ictnet), [**`Proceedings`**](./proceedings.md#ictnet-at-trec-2019-complex-answer-retrieval-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/Bert-DRMMTKS.pdf) 

- :material-rename: **Run ID:** Bert-DRMMTKS 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 7/29/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** Document Expansion by Query Prediction -> BM25 -> BERT -> DRMMTKS 

---
#### bm25-populated 
[**`Participants`**](./participants.md#smith), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/bm25-populated.pdf) 

- :material-rename: **Run ID:** bm25-populated 
- :fontawesome-solid-user-group: **Participant:** Smith 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** Produced with the y3_convert_ranking_to_ordering.py provided by the organizers (removing duplicate passages).  Uses the bm25 ranking 

---
#### dangnt-nlp 
[**`Participants`**](./participants.md#dangnt-nlp), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/dangnt-nlp.pdf) 

- :material-rename: **Run ID:** dangnt-nlp 
- :fontawesome-solid-user-group: **Participant:** DANGNT-NLP 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 7/28/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** The process has two phases: 1/ Retrieval using Anserini with input benchmarkY3test.public.tar.gz, output: benchmarkY3.run 2/ Reranking using BERT large model pretrained with input benchmarkY3.run output: benchmarkY3_dangnt_nlp.run which is our run file. 

---
#### ECNU_BM25 
[**`Participants`**](./participants.md#ecnu), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/ECNU_BM25.pdf) 

- :material-rename: **Run ID:** ECNU_BM25 
- :fontawesome-solid-user-group: **Participant:** ECNU 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** single BM25 retrieval using Anserini 

---
#### ECNU_BM25_1 
[**`Participants`**](./participants.md#ecnu), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/ECNU_BM25_1.pdf) 

- :material-rename: **Run ID:** ECNU_BM25_1 
- :fontawesome-solid-user-group: **Participant:** ECNU 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** just BM25 using Anserini 

---
#### ECNU_ReRank1 
[**`Participants`**](./participants.md#ecnu), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/ECNU_ReRank1.pdf) 

- :material-rename: **Run ID:** ECNU_ReRank1 
- :fontawesome-solid-user-group: **Participant:** ECNU 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** rerank BM25 result produced by Anserini BM25: topic and paragraph -> biLSTM -> self-attention layer -> biLSTM -> a trained score function -> score 

---
#### ICT-BM25 
[**`Participants`**](./participants.md#ictnet), [**`Proceedings`**](./proceedings.md#ictnet-at-trec-2019-complex-answer-retrieval-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/ICT-BM25.pdf) 

- :material-rename: **Run ID:** ICT-BM25 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 7/28/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** D2Q + BM25 

---
#### ICT-DRMMTKS 
[**`Participants`**](./participants.md#ictnet), [**`Proceedings`**](./proceedings.md#ictnet-at-trec-2019-complex-answer-retrieval-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/ICT-DRMMTKS.pdf) 

- :material-rename: **Run ID:** ICT-DRMMTKS 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 7/29/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** Document Expansion by Query Prediction -> BM25 -> DRMMTKS 

---
#### IRIT_run1 
[**`Participants`**](./participants.md#irit), [**`Proceedings`**](./proceedings.md#irit-at-trec-2019-incident-streams-and-complex-answer-retrieval-tracks), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/IRIT_run1.pdf) 

- :material-rename: **Run ID:** IRIT_run1 
- :fontawesome-solid-user-group: **Participant:** IRIT 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 7/30/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** 1. Indexing using Terrier 2. Retrieving the relevant documents for each query (query = page title + heading) with Terrier weighting models then CombMNZ combination 3. In a round-robin fashion, the top document of each part is selected until it reaches the paragraph budget. A paragraph only appears once per outline 

---
#### IRIT_run2 
[**`Participants`**](./participants.md#irit), [**`Proceedings`**](./proceedings.md#irit-at-trec-2019-incident-streams-and-complex-answer-retrieval-tracks), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/IRIT_run2.pdf) 

- :material-rename: **Run ID:** IRIT_run2 
- :fontawesome-solid-user-group: **Participant:** IRIT 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 7/30/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** 1. Indexing using Terrier 2. Retrieving the relevant documents for each query (query = page title + heading) with Terrier weighting models then CombMNZ combination 3. Function of the score, the ranking for the heading, number of paragraphs already returned for the heading 

---
#### IRIT_run3 
[**`Participants`**](./participants.md#irit), [**`Proceedings`**](./proceedings.md#irit-at-trec-2019-incident-streams-and-complex-answer-retrieval-tracks), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/IRIT_run3.pdf) 

- :material-rename: **Run ID:** IRIT_run3 
- :fontawesome-solid-user-group: **Participant:** IRIT 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 7/30/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** 1. Indexing using Terrier 2. Retrieving the relevant documents for each query (query = page title + heading) with Terrier weighting models then CombMNZ combination 3. Function of the score, the ranking for the heading, number of paragraphs already returned for the heading 

---
#### neural 
[**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-car-2019), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/neural.pdf) 

- :material-rename: **Run ID:** neural 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** This method is a two layer neural network. The first layer takes as input passages embedded by ELMo, along with relevance scores for these passages generated by taking the inverse rank score of 28 other passage rankings given the query (ranked according to methods such as BM25 and query likelihood).  These are page-level runs (title-only, and title + all sections in page), and these runs can be found at: http://trec-car.cs.unh.edu/inputruns/. The final input for the first layer is a query vector embedded using ELMo as well. These vectors are combined using a linear layer plus an activation function. The output of this layer is fed into a second linear layer. The final output is a logit score for each retrieved passage. Softmax with binary cross entropy is used as the loss function, predicting the relevance of a passage given a query by using the page-level qrels in Y1 train and Y1 test as labels. The passages are then ordered according to their logit score and then the top 20 passages per query are obtained 

---
#### ReRnak2_BERT 
[**`Participants`**](./participants.md#ecnu), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/ReRnak2_BERT.pdf) 

- :material-rename: **Run ID:** ReRnak2_BERT 
- :fontawesome-solid-user-group: **Participant:** ECNU 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** use BERT [CLS] to score and rerank the results produced by Anserini BM25 

---
#### ReRnak3_BERT 
[**`Participants`**](./participants.md#ecnu), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/ReRnak3_BERT.pdf) 

- :material-rename: **Run ID:** ReRnak3_BERT 
- :fontawesome-solid-user-group: **Participant:** ECNU 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** use Bert [CLS] to score and re-rank results produced by Anserini Bm25 

---
#### UNH-bm25-ecmpsg 
[**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-car-2019), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UNH-bm25-ecmpsg.pdf) 

- :material-rename: **Run ID:** UNH-bm25-ecmpsg 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** Produced with the y3_convert_ranking_to_ordering.py provided by the organizers (removing duplicate passages).  Uses the bm25 with ecm-psg expansion on the paragraphs from the  paragraphCorpus. 

---
#### UNH-bm25-rm 
[**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-car-2019), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UNH-bm25-rm.pdf) 

- :material-rename: **Run ID:** UNH-bm25-rm 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** Produced with the y3_convert_ranking_to_ordering.py provided by the organizers (removing duplicate passages).  Uses the bm25 with rm expansion on the paragraphs from the  paragraphCorpus. 

---
#### UNH-bm25-stem 
[**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-car-2019), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UNH-bm25-stem.pdf) 

- :material-rename: **Run ID:** UNH-bm25-stem 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/2/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** Candidate pool of 20 passages are created for each article from the input run. Then these 20 passages are reranked based on average BM25 similarity score of each passage pair to produce the ordering. 

---
#### UNH-dl100 
[**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-car-2019), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UNH-dl100.pdf) 

- :material-rename: **Run ID:** UNH-dl100 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/2/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** The method models similarity between passages using siamese network architecture with 3 dense layers each of size 100. Pretrained ELMo embeddings are used to represent each paragraph for training. It is trained on benchmarkY1 train dataset. The trained similarity metric is used to rerank top 20 passages from input run foe each article to produce the ordering. 

---
#### UNH-dl300 
[**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-car-2019), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UNH-dl300.pdf) 

- :material-rename: **Run ID:** UNH-dl300 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/2/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** The method models similarity between passages using siamese network architecture with 3 dense layers each of size 300. Pretrained ELMo embeddings are used to represent each paragraph for training. It is trained on benchmarkY1 train dataset. The trained similarity metric is used to rerank top 20 passages from input run foe each article to produce the ordering. 

---
#### UNH-ecn 
[**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-car-2019), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UNH-ecn.pdf) 

- :material-rename: **Run ID:** UNH-ecn 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** We start with an entity ranking and passage ranking. For every query-entity pair in entity ranking, we first make a entity context document(ECD) consisting of passages (from the passage ranking) mentioning the entity. We find co-occurring entities with this entity in the ECD and rank the co-occurring entities by the frequency of their appearance. Then we score a passage in the ECD by summing over the co-occurrence score of entities in the passage.  

---
#### UNH-qee 
[**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-car-2019), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UNH-qee.pdf) 

- :material-rename: **Run ID:** UNH-qee 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** We begin with an entity and a passage run. For every query-entity pair we concatenate all passages (from the passage ranking) mentioning the entity and create an entity context document(ECD). We find the frequency of all entities in the ECD and rank the entities by this score. We take the top 20 entities from this ranking to expand the query and retrieve passages with the expanded query.  

---
#### UNH-tfidf-lem 
[**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-car-2019), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UNH-tfidf-lem.pdf) 

- :material-rename: **Run ID:** UNH-tfidf-lem 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/2/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** For each article top 20 passages are retrieved from the input run and reranked using TFIDF cosine similarity. Starting with the first passage in the original ranking we find the most similar passage from the candidate pool using TFIDF with cosine similarity. Then we find the most similar passage of second passage among rest of the passages. We repeat this until we fill up all 20 slots. We use the lemmatized version of passages. 

---
#### UNH-tfidf-ptsim 
[**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-car-2019), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UNH-tfidf-ptsim.pdf) 

- :material-rename: **Run ID:** UNH-tfidf-ptsim 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** For each article top 20 passages are retrieved from the input run and reranked using TFIDF cosine similarity. Starting with the first passage in the original ranking we find the most similar passage from the candidate pool using TFIDF with cosine similarity. Then we find the most similar passage of second passage among rest of the passages. We repeat this until we fill up all 20 slots. 

---
#### UNH-tfidf-stem 
[**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-car-2019), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UNH-tfidf-stem.pdf) 

- :material-rename: **Run ID:** UNH-tfidf-stem 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/1/2019 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** For each article we retrieve 20 passages to make candidate pool. Then we rerank them using TFIDF cosine similarity of the stemmed passages. 

---
#### UvABM25RM3 
[**`Participants`**](./participants.md#uamsterdam), [**`Proceedings`**](./proceedings.md#university-of-amsterdam-at-the-trec-2019-complex-answer-retrieval-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UvABM25RM3.pdf) 

- :material-rename: **Run ID:** UvABM25RM3 
- :fontawesome-solid-user-group: **Participant:** UAmsterdam 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/2/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** BM25+RM3 

---
#### UvABottomUp1 
[**`Participants`**](./participants.md#uamsterdam), [**`Proceedings`**](./proceedings.md#university-of-amsterdam-at-the-trec-2019-complex-answer-retrieval-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UvABottomUp1.pdf) 

- :material-rename: **Run ID:** UvABottomUp1 
- :fontawesome-solid-user-group: **Participant:** UAmsterdam 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/2/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** Use BM25+RM3 to choose paragraphs to be populated.  

---
#### UvABottomUp2 
[**`Participants`**](./participants.md#uamsterdam), [**`Proceedings`**](./proceedings.md#university-of-amsterdam-at-the-trec-2019-complex-answer-retrieval-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UvABottomUp2.pdf) 

- :material-rename: **Run ID:** UvABottomUp2 
- :fontawesome-solid-user-group: **Participant:** UAmsterdam 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/2/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** BM25+RM3/ order preserved 

---
#### UvABottomUpChangeOrder 
[**`Participants`**](./participants.md#uamsterdam), [**`Proceedings`**](./proceedings.md#university-of-amsterdam-at-the-trec-2019-complex-answer-retrieval-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec28/appendices/car/UvABottomUpChangeOrder.pdf) 

- :material-rename: **Run ID:** UvABottomUpChangeOrder 
- :fontawesome-solid-user-group: **Participant:** UAmsterdam 
- :material-format-text: **Track:** Complex Answer Retrieval 
- :material-calendar: **Year:** 2019 
- :material-upload: **Submission:** 8/2/2019 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** passages 
- :material-text: **Run description:** BM25+RM3/order changed 

---
