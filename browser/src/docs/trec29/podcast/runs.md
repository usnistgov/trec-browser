# Runs - Podcast 2020 

#### 2306987O_abs_run1 
[**`Results`**](./results.md#2306987o_abs_run1), [**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#glasgow-representation-and-information-learning-lab-grill-at-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.2306987O_abs_run1.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.2306987O_abs_run1), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.2306987O_abs_run1.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/2306987O_abs_run1.pdf) 

- :material-rename: **Run ID:** 2306987O_abs_run1 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/24/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** For this run, a pre-trained T5 model that was fine-tuned on the provided episode descriptions was used to generate the summaries. As part of the summary generation pipeline, some post-processing was done on the model's outputs to remove as much promotional material (links, hashtags etc) as possible.  

---
#### 2306987O_extabs_run2 
[**`Results`**](./results.md#2306987o_extabs_run2), [**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#glasgow-representation-and-information-learning-lab-grill-at-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.2306987O_extabs_run2.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.2306987O_extabs_run2), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.2306987O_extabs_run2.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/2306987O_extabs_run2.pdf) 

- :material-rename: **Run ID:** 2306987O_extabs_run2 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/1/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** For this run, the first 15 sentences were extracted from the podcast transcript and fed as input to a T5 model that was fine-tuned/trained using the podcast transcripts and episode descriptions. 

---
#### 2306987O_extabs_run3 
[**`Results`**](./results.md#2306987o_extabs_run3), [**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#glasgow-representation-and-information-learning-lab-grill-at-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.2306987O_extabs_run3.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.2306987O_extabs_run3), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.2306987O_extabs_run3.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/2306987O_extabs_run3.pdf) 

- :material-rename: **Run ID:** 2306987O_extabs_run3 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** For this run, the podcast transcripts were first fed through an extractive pipeline to pick out the top 15 most representative sentences. This extractive pipeline used SpanBert to generate the embeddings of the text, and a K-means classifier to cluster those embeddings into 15 (number of desired sentences) clusters. The 15 sentences that constitute the output from this pipeline are those that are closest to the K-means cluster centroids. The output of the extractive pipeline is then given to a T5 model that was fine-tuned on podcast transcripts and their respective episode descriptions. 

---
#### bartcnn 
[**`Results`**](./results.md#bartcnn), [**`Participants`**](./participants.md#podcast_baselines), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.bartcnn.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.bartcnn), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.bartcnn.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/bartcnn.pdf) 

- :material-rename: **Run ID:** bartcnn 
- :fontawesome-solid-user-group: **Participant:** podcast_baselines 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** The model inference code was used out of the box from huggingface/transformers. 

---
#### bartpodcasts 
[**`Results`**](./results.md#bartpodcasts), [**`Participants`**](./participants.md#podcast_baselines), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.bartpodcasts.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.bartpodcasts), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.bartpodcasts.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/bartpodcasts.pdf) 

- :material-rename: **Run ID:** bartpodcasts 
- :fontawesome-solid-user-group: **Participant:** podcast_baselines 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** We fine-tuned the pretrained BART summarization model from huggingface/transformers using the first 1024 tokens of the transcripts as inputs and the descriptions as outputs. 

---
#### BERT-DESC-Q 
[**`Results`**](./results.md#bert-desc-q), [**`Participants`**](./participants.md#spotify), [**`Proceedings`**](./proceedings.md#spotify-at-the-trec-2020-podcasts-track-segment-retrieval), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.BERT-DESC-Q.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.BERT-DESC-Q), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/BERT-DESC-Q.pdf) 

- :material-rename: **Run ID:** BERT-DESC-Q 
- :fontawesome-solid-user-group: **Participant:** spotify 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `f10d10202c6189f6ec9a2b8d5b192c20` 
- :material-text: **Run description:** (1) Generate a pool of top 50 candidates with BM25 using the queries, (2) rerank topic description-segments pairs using BERT reranking model; The model pre-trained on MS MARCO passage reranking data (Nogueira et al) and fine-tuned on automatically generated questions - segments pairs.  

---
#### BERT-DESC-S 
[**`Results`**](./results.md#bert-desc-s), [**`Participants`**](./participants.md#spotify), [**`Proceedings`**](./proceedings.md#spotify-at-the-trec-2020-podcasts-track-segment-retrieval), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.BERT-DESC-S.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.BERT-DESC-S), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/BERT-DESC-S.pdf) 

- :material-rename: **Run ID:** BERT-DESC-S 
- :fontawesome-solid-user-group: **Participant:** spotify 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `e30b716ce266292d377aae5752e0c35c` 
- :material-text: **Run description:** (1) Generate a pool of top 50 candidates with BM25 using the queries, (2) rerank topic description-segments pairs using BERT reranking model; The model pre-trained on MS MARCO passage reranking data (Nogueira et al) and fine-tuned on extra topics and relevance judgments from crowdsourcing.  

---
#### BERT-DESC-TD 
[**`Results`**](./results.md#bert-desc-td), [**`Participants`**](./participants.md#spotify), [**`Proceedings`**](./proceedings.md#spotify-at-the-trec-2020-podcasts-track-segment-retrieval), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.BERT-DESC-TD.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.BERT-DESC-TD), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/BERT-DESC-TD.pdf) 

- :material-rename: **Run ID:** BERT-DESC-TD 
- :fontawesome-solid-user-group: **Participant:** spotify 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `ce584a7f5c82374a7edfb52ce3dc5771` 
- :material-text: **Run description:** (1) Generate a pool of top 50 candidates with BM25 using the queries, (2) rerank topic description-segments pairs using BERT reranking model; The model pre-trained on MS MARCO passage reranking data (Nogueira et al) and fine-tuned on synthetic data from the podcast dataset. The top relevant segments within the episode were retrieved using the episode title as the query and the episode description-segments were used as reranking pairs. 

---
#### BM25 
[**`Results`**](./results.md#bm25), [**`Participants`**](./participants.md#podcast_baselines), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.BM25.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.BM25), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/BM25.pdf) 

- :material-rename: **Run ID:** BM25 
- :fontawesome-solid-user-group: **Participant:** podcast_baselines 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `8f43c4bb18e80cc8ef24794d3961678e` 
- :material-text: **Run description:** Traditional IR model, BM25; implemented with Anserini toolkit and default parameters (b=0.9 and k=0.4) 

---
#### categoryaware1 
[**`Results`**](./results.md#categoryaware1), [**`Participants`**](./participants.md#spotify), [**`Proceedings`**](./proceedings.md#spotify-at-the-trec-2020-podcasts-track-segment-retrieval), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.categoryaware1.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.categoryaware1), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.categoryaware1.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/categoryaware1.pdf) 

- :material-rename: **Run ID:** categoryaware1 
- :fontawesome-solid-user-group: **Participant:** spotify 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** This run is after one epoch of fine-tuning. 

---
#### categoryaware2 
[**`Results`**](./results.md#categoryaware2), [**`Participants`**](./participants.md#spotify), [**`Proceedings`**](./proceedings.md#spotify-at-the-trec-2020-podcasts-track-segment-retrieval), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.categoryaware2.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.categoryaware2), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.categoryaware2.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/categoryaware2.pdf) 

- :material-rename: **Run ID:** categoryaware2 
- :fontawesome-solid-user-group: **Participant:** spotify 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** This run is after two epochs of fine-tuning. 

---
#### coarse2fine 
[**`Results`**](./results.md#coarse2fine), [**`Participants`**](./participants.md#spotify), [**`Proceedings`**](./proceedings.md#spotify-at-the-trec-2020-podcasts-track-segment-retrieval), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.coarse2fine.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.coarse2fine), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.coarse2fine.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/coarse2fine.pdf) 

- :material-rename: **Run ID:** coarse2fine 
- :fontawesome-solid-user-group: **Participant:** spotify 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** We used TextRank to extract central regions (chunks of sentences) of the transcript. The most central regions (up to about 1000 tokens) were concatenated in order of appearance and used as input for fine-tuning the Bart CNN/Daily Mail summarization model from huggingface/transformers, with episode descriptions as output. Output summaries were constrained to a maximum of 250 tokens. 

---
#### cued_speechUniv1 
[**`Results`**](./results.md#cued_speechuniv1), [**`Participants`**](./participants.md#cued_speechuniv), [**`Proceedings`**](./proceedings.md#cued-speech-at-trec-2020-podcast-summarisation-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.cued_speechUniv1.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.cued_speechUniv1), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.cued_speechUniv1.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/cued_speechUniv1.pdf) 

- :material-rename: **Run ID:** cued_speechUniv1 
- :fontawesome-solid-user-group: **Participant:** cued_speechUniv 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** Two-step approach: (1) sentence filtering based on sentence-level attention scores of the hierarchical model, (2) BART summarisation using the filtered sentence as the input at both training & inference time. We optimised BART on maximum likelihood criterion and subsequently on reinforcement learning (sequence-level optimisation) criterion. Finally, we perform an ensemble of BART models from different checkpoints and different data shuffles. 

---
#### cued_speechUniv2 
[**`Results`**](./results.md#cued_speechuniv2), [**`Participants`**](./participants.md#cued_speechuniv), [**`Proceedings`**](./proceedings.md#cued-speech-at-trec-2020-podcast-summarisation-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.cued_speechUniv2.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.cued_speechUniv2), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.cued_speechUniv2.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/cued_speechUniv2.pdf) 

- :material-rename: **Run ID:** cued_speechUniv2 
- :fontawesome-solid-user-group: **Participant:** cued_speechUniv 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** same as Run1 (cued_speechUniv2) - difference being the ensemble consists of 3 models 

---
#### cued_speechUniv3 
[**`Results`**](./results.md#cued_speechuniv3), [**`Participants`**](./participants.md#cued_speechuniv), [**`Proceedings`**](./proceedings.md#cued-speech-at-trec-2020-podcast-summarisation-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.cued_speechUniv3.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.cued_speechUniv3), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.cued_speechUniv3.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/cued_speechUniv3.pdf) 

- :material-rename: **Run ID:** cued_speechUniv3 
- :fontawesome-solid-user-group: **Participant:** cued_speechUniv 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** - This is meant to be the most standard approach (i.e. our baseline) - Fine-tuning CNN/Daily trained BART model on the podcast data - If the transcription at training and inference time exceeds 1,024 tokens, it gets truncated.  

---
#### cued_speechUniv4 
[**`Results`**](./results.md#cued_speechuniv4), [**`Participants`**](./participants.md#cued_speechuniv), [**`Proceedings`**](./proceedings.md#cued-speech-at-trec-2020-podcast-summarisation-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.cued_speechUniv4.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.cued_speechUniv4), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.cued_speechUniv4.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/cued_speechUniv4.pdf) 

- :material-rename: **Run ID:** cued_speechUniv4 
- :fontawesome-solid-user-group: **Participant:** cued_speechUniv 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** - same as RUN1 "cued_speechUniv1", with the difference being that this system is not optimised on the RL criterion and it is a single-model system rather than an ensemble  

---
#### hk_uu_podcast1 
[**`Results`**](./results.md#hk_uu_podcast1), [**`Participants`**](./participants.md#hk_uu_podcast), [**`Proceedings`**](./proceedings.md#abstract-podcast-summarization-using-bart-with-longformer-attention), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.hk_uu_podcast1.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.hk_uu_podcast1), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.hk_uu_podcast1.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/hk_uu_podcast1.pdf) 

- :material-rename: **Run ID:** hk_uu_podcast1 
- :fontawesome-solid-user-group: **Participant:** hk_uu_podcast 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** The model was trained for 3 epochs and the best rogue2 checkpoint on a created validation split was chosen. The model was trained using and input sequence length of 4096 and a target max length of 200. 

---
#### hltcoe1 
[**`Results`**](./results.md#hltcoe1), [**`Participants`**](./participants.md#hltcoe), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.hltcoe1.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.hltcoe1), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/hltcoe1.pdf) 

- :material-rename: **Run ID:** hltcoe1 
- :fontawesome-solid-user-group: **Participant:** hltcoe 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/4/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `d2ee581babda85ed80422c954a8df344` 
- :material-text: **Run description:** Statistical language model with linear interpolation.  Rocchio-style relevance feedback and term reweighting.  Overlapping, word-spanning, character 5-gram tokenization. 

---
#### hltcoe2 
[**`Results`**](./results.md#hltcoe2), [**`Participants`**](./participants.md#hltcoe), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.hltcoe2.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.hltcoe2), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/hltcoe2.pdf) 

- :material-rename: **Run ID:** hltcoe2 
- :fontawesome-solid-user-group: **Participant:** hltcoe 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/4/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `9c86dc3b9eb1d0f49512f8d11ca9603c` 
- :material-text: **Run description:** Statistical language model with linear interpolation.  Rocchio-style relevance feedback and term reweighting.  Unstemmed words used for tokenization. 

---
#### hltcoe3 
[**`Results`**](./results.md#hltcoe3), [**`Participants`**](./participants.md#hltcoe), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.hltcoe3.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.hltcoe3), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/hltcoe3.pdf) 

- :material-rename: **Run ID:** hltcoe3 
- :fontawesome-solid-user-group: **Participant:** hltcoe 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/4/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `51b7a815b8a665f7e8dddc71327939d8` 
- :material-text: **Run description:** Statistical language model with linear interpolation.  No query modification or relevance feedback was employed.  Unstemmed words used for tokenization. 

---
#### hltcoe4 
[**`Results`**](./results.md#hltcoe4), [**`Participants`**](./participants.md#hltcoe), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.hltcoe4.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.hltcoe4), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/hltcoe4.pdf) 

- :material-rename: **Run ID:** hltcoe4 
- :fontawesome-solid-user-group: **Participant:** hltcoe 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/4/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `5b505126e2ac891314aa11124e7afacc` 
- :material-text: **Run description:** Statistical language model with linear interpolation.  Rocchio-style relevance feedback and term reweighting.  Unstemmed words used for tokenization. 

---
#### hltcoe5 
[**`Results`**](./results.md#hltcoe5), [**`Participants`**](./participants.md#hltcoe), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.hltcoe5.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.hltcoe5), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/hltcoe5.pdf) 

- :material-rename: **Run ID:** hltcoe5 
- :fontawesome-solid-user-group: **Participant:** hltcoe 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/4/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `b94954bf6db0fd88d8bf3f4df4f26b77` 
- :material-text: **Run description:** Independently decoded audio data (baseline transcript was not used). Statistical language model with linear interpolation.  Rocchio-style relevance feedback and term reweighting.  Overlapping, word-spanning character 4-gram tokenization. 

---
#### LRGREtvrs-r_1 
[**`Results`**](./results.md#lrgretvrs-r_1), [**`Participants`**](./participants.md#lrg_retrievers), [**`Proceedings`**](./proceedings.md#lrg-at-trec-2020-document-ranking-with-xlnet-based-models), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.LRGREtvrs-r_1.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.LRGREtvrs-r_1), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/LRGREtvrs-r_1.pdf) 

- :material-rename: **Run ID:** LRGREtvrs-r_1 
- :fontawesome-solid-user-group: **Participant:** LRG_REtrievers 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/31/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `f8902c4b7a18df3a165e5d2f7fa0e8a9` 
- :material-text: **Run description:** We ranked the user's query with BM25 scores for every podcast episode in the dataset and filtered the top 200 podcasts. We then divided the filtered podcasts into 2 minute segments and re-ranked them with a regressive XLNet model and returned the top 1000 results. 

---
#### LRGREtvrs-r_2 
[**`Results`**](./results.md#lrgretvrs-r_2), [**`Participants`**](./participants.md#lrg_retrievers), [**`Proceedings`**](./proceedings.md#lrg-at-trec-2020-document-ranking-with-xlnet-based-models), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.LRGREtvrs-r_2.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.LRGREtvrs-r_2), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/LRGREtvrs-r_2.pdf) 

- :material-rename: **Run ID:** LRGREtvrs-r_2 
- :fontawesome-solid-user-group: **Participant:** LRG_REtrievers 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/1/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `a7c7e79b62c6c05f13afa50370b7f40e` 
- :material-text: **Run description:** To tackle the problem statement, we adopt a neural re-ranking approach, using BM25 to filter episodes and RM3 for query expansion. We then split the episodes into two minute segments. For each query-segment pair in the training set, we use a transformers-based model. We then find the contextual embeddings using XLNet (keeping two layers unfrozen) and compute the similarity matrix between the query and the document, followed by kernel pooling techniques and linear layers to finally arrive at a relevance score for the document. 

---
#### LRGREtvrs-r_3 
[**`Results`**](./results.md#lrgretvrs-r_3), [**`Participants`**](./participants.md#lrg_retrievers), [**`Proceedings`**](./proceedings.md#lrg-at-trec-2020-document-ranking-with-xlnet-based-models), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.LRGREtvrs-r_3.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.LRGREtvrs-r_3), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/LRGREtvrs-r_3.pdf) 

- :material-rename: **Run ID:** LRGREtvrs-r_3 
- :fontawesome-solid-user-group: **Participant:** LRG_REtrievers 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/1/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `25e2a11f66071c0d2e208529867ea3dc` 
- :material-text: **Run description:** To tackle the problem statement, we adopt a neural re-ranking approach, we first split each episode into 2 minute segments. Then using BM25 to filter episodes and RM3 for query expansion we create a curated list of 5000 segments. For each query-segment pair in the training set, we use a regression based transformer model, after which we re-rank the documents according to the regression scores. 

---
#### LRGREtvrs-r_4 
[**`Results`**](./results.md#lrgretvrs-r_4), [**`Participants`**](./participants.md#lrg_retrievers), [**`Proceedings`**](./proceedings.md#lrg-at-trec-2020-document-ranking-with-xlnet-based-models), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.LRGREtvrs-r_4.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.LRGREtvrs-r_4), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/LRGREtvrs-r_4.pdf) 

- :material-rename: **Run ID:** LRGREtvrs-r_4 
- :fontawesome-solid-user-group: **Participant:** LRG_REtrievers 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `3490b3763a141e7a47637f941e7a38bc` 
- :material-text: **Run description:** We ranked the user's query with BM25 scores for every podcast episode in the dataset and filtered the top 400 podcasts. We then divided the filtered podcasts into 2 minute segments and re-ranked them with a regressive XLNet model and returned the top 1000 results. 

---
#### onemin 
[**`Results`**](./results.md#onemin), [**`Participants`**](./participants.md#podcast_baselines), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.onemin.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.onemin), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.onemin.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/onemin.pdf) 

- :material-rename: **Run ID:** onemin 
- :fontawesome-solid-user-group: **Participant:** podcast_baselines 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** The first minute of the transcript is extracted and used as the summary. 

---
#### oudalab1 
[**`Results`**](./results.md#oudalab1), [**`Participants`**](./participants.md#oudalab), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.oudalab1.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.oudalab1), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/oudalab1.pdf) 

- :material-rename: **Run ID:** oudalab1 
- :fontawesome-solid-user-group: **Participant:** oudalab 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/4/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `8ff5420f22d01244c61c617e8baf8347` 
- :material-text: **Run description:** Using the above-mentioned method, this run was a trial run with a few data points. We used the top 10 closest segments based on distance to find the episodes to use for our BERT QA task. We then chose the top 3 answers with the lowest similarity scores according to BERT, removing duplicates. 

---
#### QL 
[**`Results`**](./results.md#ql), [**`Participants`**](./participants.md#podcast_baselines), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.QL.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.QL), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/QL.pdf) 

- :material-rename: **Run ID:** QL 
- :fontawesome-solid-user-group: **Participant:** podcast_baselines 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `29f529f98bbbb230c34347f19fc61217` 
- :material-text: **Run description:** Traditional IR model, query likelihood; implemented with Anserini toolkit, and default hyperparameters (for Dirichlet smoothing &#956; = 1000). 

---
#### RERANK-DESC 
[**`Results`**](./results.md#rerank-desc), [**`Participants`**](./participants.md#podcast_baselines), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.RERANK-DESC.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.RERANK-DESC), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/RERANK-DESC.pdf) 

- :material-rename: **Run ID:** RERANK-DESC 
- :fontawesome-solid-user-group: **Participant:** podcast_baselines 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `178140590bd272270d8e1a52e9c04c5d` 
- :material-text: **Run description:** (1) Generate a pool of top 50 candidates with BM25 using the queries, (2) rerank topic description-segments pairs using BERT reranking model pre-trained on MS MARCO passage reranking data (Nogueira et al). The model was used without any further fine-tuning. 

---
#### RERANK-QUERY 
[**`Results`**](./results.md#rerank-query), [**`Participants`**](./participants.md#podcast_baselines), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.RERANK-QUERY.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.RERANK-QUERY), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/RERANK-QUERY.pdf) 

- :material-rename: **Run ID:** RERANK-QUERY 
- :fontawesome-solid-user-group: **Participant:** podcast_baselines 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `75e41ba41563c7448b30378fb13f2386` 
- :material-text: **Run description:** (1) Generate a pool of top 50 candidates with BM25 using the queries, (2) rerank topic query-segments pairs using BERT reranking model pre-trained on MS MARCO passage reranking data (Nogueira et al). The model was used without any further fine-tuning. 

---
#### run_dcu1 
[**`Results`**](./results.md#run_dcu1), [**`Participants`**](./participants.md#dcu-adapt), [**`Proceedings`**](./proceedings.md#dcu-adapt-at-the-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.run_dcu1.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.run_dcu1), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/run_dcu1.pdf) 

- :material-rename: **Run ID:** run_dcu1 
- :fontawesome-solid-user-group: **Participant:** DCU-ADAPT 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/1/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `e5eb3bb396ee53bb8894a10f77414a9b` 
- :material-text: **Run description:** Nouns and proper nouns are identified automatically using Spacy natural language processing toolkit, and those words are added to queries. From the documents of 1st pass retrieval, words relevant to query nouns are identified using wordnet, and these words are added after being ranked using Robertson offer weight. The queries are processed by the DPH model, and further Bo1 query expansion model was applied. 

---
#### run_dcu2 
[**`Results`**](./results.md#run_dcu2), [**`Participants`**](./participants.md#dcu-adapt), [**`Proceedings`**](./proceedings.md#dcu-adapt-at-the-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.run_dcu2.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.run_dcu2), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/run_dcu2.pdf) 

- :material-rename: **Run ID:** run_dcu2 
- :fontawesome-solid-user-group: **Participant:** DCU-ADAPT 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/1/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `df6299db1ef8194672883331ae579edc` 
- :material-text: **Run description:** Nouns and named entities are identified automatically using Spacy natural language processing toolkit, and those words are added to queries. The queries are processed by the DPH model, and further Bo1 query expansion model was applied. 

---
#### run_dcu3 
[**`Results`**](./results.md#run_dcu3), [**`Participants`**](./participants.md#dcu-adapt), [**`Proceedings`**](./proceedings.md#dcu-adapt-at-the-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.run_dcu3.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.run_dcu3), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/run_dcu3.pdf) 

- :material-rename: **Run ID:** run_dcu3 
- :fontawesome-solid-user-group: **Participant:** DCU-ADAPT 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/1/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `0be485c98b8ce2978fbee980e261519a` 
- :material-text: **Run description:** Nouns and named entities are identified automatically using Spacy natural language processing toolkit, and those words are added to queries. From the documents of 1st pass retrieval, words relevant to query nouns are identified using wordnet, and these words are added after being ranked using Robertson offer weight. The queries are processed by the DPH model, and further Bo1 query expansion model was applied. 

---
#### run_dcu4 
[**`Results`**](./results.md#run_dcu4), [**`Participants`**](./participants.md#dcu-adapt), [**`Proceedings`**](./proceedings.md#dcu-adapt-at-the-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.run_dcu4.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.run_dcu4), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/run_dcu4.pdf) 

- :material-rename: **Run ID:** run_dcu4 
- :fontawesome-solid-user-group: **Participant:** DCU-ADAPT 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/1/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `6245881af107cb477116c70a8faa531e` 
- :material-text: **Run description:** A collection of webtext was compiled using Google search engine. From the collection, terms relevant to queries were found using Robertson offer weight and added to the queries. Nouns and named entities from query description were also added to the queries. 

---
#### run_dcu5 
[**`Results`**](./results.md#run_dcu5), [**`Participants`**](./participants.md#dcu-adapt), [**`Proceedings`**](./proceedings.md#dcu-adapt-at-the-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.run_dcu5.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.run_dcu5), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/run_dcu5.pdf) 

- :material-rename: **Run ID:** run_dcu5 
- :fontawesome-solid-user-group: **Participant:** DCU-ADAPT 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/1/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `b439b372162c454e6abc26926983bdc0` 
- :material-text: **Run description:** This is a combination of all of the query extension approaches from the previous submissions. 

---
#### textranksegments 
[**`Results`**](./results.md#textranksegments), [**`Participants`**](./participants.md#podcast_baselines), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.textranksegments.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.textranksegments), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.textranksegments.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/textranksegments.pdf) 

- :material-rename: **Run ID:** textranksegments 
- :fontawesome-solid-user-group: **Participant:** podcast_baselines 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** We chunked the transcript into ~50 word segments (respecting sentence boundaries), and ran TextRank, using TF-IDF cosine similarity as the edge weights, with aggregate vertex degree as the centrality measure (not PageRank). Up to ~150 words from the top segments were selected for the summary, with segments kept in order. We specified a set of stopwords, consisting of the most common terms in the whole corpus, to be ignored. 

---
#### textranksentences 
[**`Results`**](./results.md#textranksentences), [**`Participants`**](./participants.md#podcast_baselines), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.textranksentences.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.textranksentences), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.textranksentences.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/textranksentences.pdf) 

- :material-rename: **Run ID:** textranksentences 
- :fontawesome-solid-user-group: **Participant:** podcast_baselines 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** We split the transcript into sentences using spaCy, and ran TextRank, using TF-IDF cosine similarity as the edge weights, with aggregate vertex degree as the centrality measure (not PageRank). The top sentences, up to about 150 words in total, were selected for the summary, with sentences kept in the order they appear. We specified a set of stopwords, consisting of the most common terms in the whole corpus, to be ignored. 

---
#### UCF_NLP1 
[**`Results`**](./results.md#ucf_nlp1), [**`Participants`**](./participants.md#ucf_nlp), [**`Proceedings`**](./proceedings.md#automatic-summarization-of-open-domain-podcast-episodes), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.UCF_NLP1.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.UCF_NLP1), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.UCF_NLP1.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/UCF_NLP1.pdf) 

- :material-rename: **Run ID:** UCF_NLP1 
- :fontawesome-solid-user-group: **Participant:** UCF_NLP 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** Our summarization system (UCF_NLP1) focuses on generating abstractive summaries from podcast transcripts. It employs an encoder-decoder model to condense the first few segments of the transcript into an abstractive summary. 

---
#### UCF_NLP2 
[**`Results`**](./results.md#ucf_nlp2), [**`Participants`**](./participants.md#ucf_nlp), [**`Proceedings`**](./proceedings.md#automatic-summarization-of-open-domain-podcast-episodes), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.UCF_NLP2.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.UCF_NLP2), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.UCF_NLP2.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/UCF_NLP2.pdf) 

- :material-rename: **Run ID:** UCF_NLP2 
- :fontawesome-solid-user-group: **Participant:** UCF_NLP 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** Our summarization system (UCF_NLP2) focuses on generating abstractive summaries from podcast transcripts. It consists of an abstractor that employs an encoder-decoder model to compose summaries and an extractor that enhances content selection by identifying summary-worthy segments from lengthy transcripts and provide them as input to the abstractor.  

---
#### udel_wang_zheng1 
[**`Results`**](./results.md#udel_wang_zheng1), [**`Participants`**](./participants.md#udel_wang_zheng), [**`Proceedings`**](./proceedings.md#a-two-phase-approach-for-abstractive-podcast-summarization), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.udel_wang_zheng1.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.udel_wang_zheng1), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.udel_wang_zheng1.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/udel_wang_zheng1.pdf) 

- :material-rename: **Run ID:** udel_wang_zheng1 
- :fontawesome-solid-user-group: **Participant:** udel_wang_zheng 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 8/28/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** We build a model using the first 1024 tokens from the transcript and fine-tune it on distilBART-cnndm. 

---
#### udel_wang_zheng2 
[**`Results`**](./results.md#udel_wang_zheng2), [**`Participants`**](./participants.md#udel_wang_zheng), [**`Proceedings`**](./proceedings.md#a-two-phase-approach-for-abstractive-podcast-summarization), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.udel_wang_zheng2.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.udel_wang_zheng2), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.udel_wang_zheng2.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/udel_wang_zheng2.pdf) 

- :material-rename: **Run ID:** udel_wang_zheng2 
- :fontawesome-solid-user-group: **Participant:** udel_wang_zheng 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/1/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** We perform LDA on transcript to extract the topics covered in the episode, and then select top-scoring sentences for fine-tuning. 

---
#### udel_wang_zheng3 
[**`Results`**](./results.md#udel_wang_zheng3), [**`Participants`**](./participants.md#udel_wang_zheng), [**`Proceedings`**](./proceedings.md#a-two-phase-approach-for-abstractive-podcast-summarization), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.udel_wang_zheng3.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.udel_wang_zheng3), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.udel_wang_zheng3.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/udel_wang_zheng3.pdf) 

- :material-rename: **Run ID:** udel_wang_zheng3 
- :fontawesome-solid-user-group: **Participant:** udel_wang_zheng 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/1/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** Select sentences for fine-tuning. 

---
#### udel_wang_zheng4 
[**`Results`**](./results.md#udel_wang_zheng4), [**`Participants`**](./participants.md#udel_wang_zheng), [**`Proceedings`**](./proceedings.md#a-two-phase-approach-for-abstractive-podcast-summarization), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.udel_wang_zheng4.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.udel_wang_zheng4), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.udel_wang_zheng4.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/udel_wang_zheng4.pdf) 

- :material-rename: **Run ID:** udel_wang_zheng4 
- :fontawesome-solid-user-group: **Participant:** udel_wang_zheng 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/1/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** Combine our output from previous three submission and generate summary again. 

---
#### UMD_ID_run4 
[**`Results`**](./results.md#umd_id_run4), [**`Participants`**](./participants.md#umd_ir), [**`Proceedings`**](./proceedings.md#combine-and-re-rank-the-university-of-maryland-at-the-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.UMD_ID_run4.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.UMD_ID_run4), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/UMD_ID_run4.pdf) 

- :material-rename: **Run ID:** UMD_ID_run4 
- :fontawesome-solid-user-group: **Participant:** UMD_IR 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `eb8c143b43c146995afb00785cfbdf47` 
- :material-text: **Run description:** 7 systems (unstemmed LM, unstemmed LM+word2vec query expansion, stemmed weighted LM with stopwords, unstemmed TFIDF, stemmed LM+sdm, unstemmed 5min long segments LM, stemmed LM with documents expanded with metadata), each system re-reranked using either T5 or BERT and then combined into a single system. 

---
#### UMD_IR_run1 
[**`Results`**](./results.md#umd_ir_run1), [**`Participants`**](./participants.md#umd_ir), [**`Proceedings`**](./proceedings.md#combine-and-re-rank-the-university-of-maryland-at-the-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.UMD_IR_run1.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.UMD_IR_run1), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/UMD_IR_run1.pdf) 

- :material-rename: **Run ID:** UMD_IR_run1 
- :fontawesome-solid-user-group: **Participant:** UMD_IR 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `b4a90a6bed2ffc141f49cb4962c7240d` 
- :material-text: **Run description:** Baseline model prepared from Indri LM with sequential dependency model applied, the results are re-ranked using T5 BERT model trained using MS MARCO dataset. 

---
#### UMD_IR_run2 
[**`Results`**](./results.md#umd_ir_run2), [**`Participants`**](./participants.md#umd_ir), [**`Proceedings`**](./proceedings.md#combine-and-re-rank-the-university-of-maryland-at-the-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.UMD_IR_run2.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.UMD_IR_run2), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/UMD_IR_run2.pdf) 

- :material-rename: **Run ID:** UMD_IR_run2 
- :fontawesome-solid-user-group: **Participant:** UMD_IR 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `da9e8e1e56a3b84dcaae8da759b1df2d` 
- :material-text: **Run description:** Indri LM with sequential dependency model. 

---
#### UMD_IR_run3 
[**`Results`**](./results.md#umd_ir_run3), [**`Participants`**](./participants.md#umd_ir), [**`Proceedings`**](./proceedings.md#combine-and-re-rank-the-university-of-maryland-at-the-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.UMD_IR_run3.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.UMD_IR_run3), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/UMD_IR_run3.pdf) 

- :material-rename: **Run ID:** UMD_IR_run3 
- :fontawesome-solid-user-group: **Participant:** UMD_IR 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `75f5f2cf929466b63a7856511bf308ed` 
- :material-text: **Run description:** 7 systems (unstemmed LM, unstemmed LM+word2vec query expansion, stemmed weighted LM with stopwords, unstemmed TFIDF, stemmed LM+sdm, unstemmed 5min long segments LM, stemmed LM with documents expanded with metadata ) combined into a single run, which is reranked using 3 MS MARCO trained models (T5 and BERT) and combined with the baseline run. 

---
#### UMD_IR_run5 
[**`Results`**](./results.md#umd_ir_run5), [**`Participants`**](./participants.md#umd_ir), [**`Proceedings`**](./proceedings.md#combine-and-re-rank-the-university-of-maryland-at-the-trec-2020-podcasts-track), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.UMD_IR_run5.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.UMD_IR_run5), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/UMD_IR_run5.pdf) 

- :material-rename: **Run ID:** UMD_IR_run5 
- :fontawesome-solid-user-group: **Participant:** UMD_IR 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `23429c601ffc40adce398db7c3450e29` 
- :material-text: **Run description:** CombMNZ Combination of the run1 - run4 

---
#### unhtrema1 
[**`Results`**](./results.md#unhtrema1), [**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-trec-2020), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.unhtrema1.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.unhtrema1), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.unhtrema1.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/unhtrema1.pdf) 

- :material-rename: **Run ID:** unhtrema1 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** A GAN model is used to generate abstractive summary of chunks of input texts. Sentence-transformer method is used to embed each of these summary lines as fixed length vectors. Another LSTM network is trained to output a summary embedding vector given input summary embedding vectors. Then the generated summary lines are sorted based on the cosine similarity of their embedding vector to this synthetic summary vector. Top k summary lines are chosen from these sorted lines as the overall summary. For this run, k=3 with max output sequence length of 15 for the GAN model. Input text is split into 10 parts each input chunk of 1000 words. 

---
#### unhtrema2 
[**`Results`**](./results.md#unhtrema2), [**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-trec-2020), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.unhtrema2.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.unhtrema2), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.unhtrema2.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/unhtrema2.pdf) 

- :material-rename: **Run ID:** unhtrema2 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** A GAN model is used to generate abstractive summary of chunks of input texts. Sentence-transformer method is used to embed each of these summary lines as fixed length vectors. Another LSTM network is trained to output a summary embedding vector given input summary embedding vectors. Then the generated summary lines are sorted based on the cosine similarity of their embedding vector to this synthetic summary vector. Top k summary lines are chosen from these sorted lines as the overall summary. For this run, k=10 with max output sequence length of 15 for the GAN model. Input text is split into 10 parts each input chunk of 1000 words. 

---
#### unhtrema3 
[**`Results`**](./results.md#unhtrema3), [**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-trec-2020), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.unhtrema3.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.unhtrema3), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.unhtrema3.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/unhtrema3.pdf) 

- :material-rename: **Run ID:** unhtrema3 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** A GAN model is used to generate abstractive summary of chunks of input texts. Sentence-transformer method is used to embed each of these summary lines as fixed length vectors. Another LSTM network is trained to output a summary embedding vector given input summary embedding vectors. Then the generated summary lines are sorted based on the cosine similarity of their embedding vector to this synthetic summary vector. Top k summary lines are chosen from these sorted lines as the overall summary. For this run, k=10 with max output sequence length of 20 for the GAN model. Input text is split into 100 parts each input chunk of 100 words. 

---
#### unhtrema4 
[**`Results`**](./results.md#unhtrema4), [**`Participants`**](./participants.md#trema-unh), [**`Proceedings`**](./proceedings.md#trema-unh-at-trec-2020), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.unhtrema4.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.unhtrema4), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.unhtrema4.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/unhtrema4.pdf) 

- :material-rename: **Run ID:** unhtrema4 
- :fontawesome-solid-user-group: **Participant:** TREMA-UNH 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/3/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** A GAN model is used to generate abstractive summary of chunks of input texts. Sentence-transformer method is used to embed each of these summary lines as fixed length vectors. Another LSTM network is trained to output a summary embedding vector given input summary embedding vectors. Then the generated summary lines are sorted based on the cosine similarity of their embedding vector to this synthetic summary vector. Top k summary lines are chosen from these sorted lines as the overall summary. For this run, k=20 with max output sequence length of 20 for the GAN model. Input text is split into 100 parts each input chunk of 100 words. 

---
#### UTDThesis1 
[**`Results`**](./results.md#utdthesis1), [**`Participants`**](./participants.md#utdthesis), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.UTDThesis1.tgz), [**`Summary (manual)`**](https://trec.nist.gov/results/trec29/podcast/summary.manual.UTDThesis1), [**`Summary (rouge)`**](https://trec.nist.gov/results/trec29/podcast/summary.rouge.UTDThesis1.tgz), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/UTDThesis1.pdf) 

- :material-rename: **Run ID:** UTDThesis1 
- :fontawesome-solid-user-group: **Participant:** UTDThesis 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** summarization 
- :material-text: **Run description:** These are the abstractive summaries generated by the Dialogue Action Tokenized T5-Transformer described above. 

---
#### UTDThesis_Run1 
[**`Results`**](./results.md#utdthesis_run1), [**`Participants`**](./participants.md#utdthesis), [**`Input`**](https://trec.nist.gov/results/trec29/podcast/input.UTDThesis_Run1.gz), [**`Summary`**](https://trec.nist.gov/results/trec29/podcast/summary.treceval.UTDThesis_Run1), [**`Appendix`**](https://trec.nist.gov/pubs/trec29/appendices/podcast/UTDThesis_Run1.pdf) 

- :material-rename: **Run ID:** UTDThesis_Run1 
- :fontawesome-solid-user-group: **Participant:** UTDThesis 
- :material-format-text: **Track:** Podcast 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/2/2020 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** retrieval 
- :material-fingerprint: **MD5:** `bf94389052d00735052d02c0c8324a8d` 
- :material-text: **Run description:** This run collects 100 ranked documents for each query, using the previously described ranking method. 

---
