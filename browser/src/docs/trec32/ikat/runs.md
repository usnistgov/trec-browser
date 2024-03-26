# Runs - Interactive Knowledge Assistance 2023 

#### bm25_rm3-auto-ptkb_3-k_100-num_psg-3 
[**`Participants`**](./participants.md#trackorg) 

- :material-rename: **Run ID:** bm25_rm3-auto-ptkb_3-k_100-num_psg-3 
- :fontawesome-solid-user-group: **Participant:** trackorg 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/4/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `28c07ff9a092562037c120f1834cf77c` 
- :material-text: **Run description:** BM25+RM3 (Pyserini default) as the initial retrieval (denoted by ret_bm25_rm3 in the file name) method to retrieve 100 passages per query (denoted by k_100). The query in each turn was re-written using: The context, and The top-3 relevant PTKB statements (denoted by num_ptkb_3 in the file name). Query re-writing. In all cases, the re-written query was constructed by appending the relevant PTKB statements to the (manually or automatically) resolved query. Response generation. A response was generated using the top-3 passages retrieved with the re-written query (denoted by num_psg_3 in the file name). We use the T5 model mrm8488/t5-base-finetuned-summarize-news available on HuggingFace for this purpose. The relevant PTKB statements were determined automatically by re-ranking the statements using SentenceTransformers, specifically, the model cross-encoder/ms-marco-MiniLM-L-6-v2 available on HuggingFace. The query was re-written automatically using the castorini/t5-base-canard model available on HuggingFace.  

---
#### bm25_rm3-manual-ptkb_3-k_100-num_psg-3 
[**`Participants`**](./participants.md#trackorg) 

- :material-rename: **Run ID:** bm25_rm3-manual-ptkb_3-k_100-num_psg-3 
- :fontawesome-solid-user-group: **Participant:** trackorg 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/31/2023 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `4c9944b2b9f315cd278dfca99f5a08e3` 
- :material-text: **Run description:** BM25+RM3 (Pyserini default) as the initial retrieval method to retrieve 100 passages per query.The query in each turn was re-written using: (1) the context, and (2) the top-3 relevant PTKB statements. The re-written query was construted by appending the relevant PTKB statements to the manually resolved query.A response was generated using the top-3 passages retrieved with the re-written query. We use the T5 model mrm8488/t5-base-finetuned-summarize-news available on HuggingFace for this purpose. 

---
#### cfda1 
[**`Participants`**](./participants.md#cfda_clip) 

- :material-rename: **Run ID:** cfda1 
- :fontawesome-solid-user-group: **Participant:** CFDA_CLIP 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/4/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `e76c4d3a778b410af6003f975d1bed31` 
- :material-text: **Run description:** Retrieval: Sparse retrieval with re-ranking performed by dense retrievers. Response generation: Generative QA models.   

---
#### cfda2 
[**`Participants`**](./participants.md#cfda_clip) 

- :material-rename: **Run ID:** cfda2 
- :fontawesome-solid-user-group: **Participant:** CFDA_CLIP 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/4/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `abf0f6f88b642389f0222bc8defed79f` 
- :material-text: **Run description:** Retrieval: Sparse retrieval with re-ranking performed by dense retrievers. Response generation: Generative QA models.  

---
#### cfda3 
[**`Participants`**](./participants.md#cfda_clip) 

- :material-rename: **Run ID:** cfda3 
- :fontawesome-solid-user-group: **Participant:** CFDA_CLIP 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/4/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `7bfd0063e3ebdeb3df9b664b79904600` 
- :material-text: **Run description:** Query rewriting: rewriting model conditioned on the given all ptkbs. Retrieval: Sparse retrieval with re-ranking performed by dense retrievers; the retriever was fine-tuned with synthetic statements with QReCC. Response generation: Generative QA models; the QA model was fine-tuned on augmented QReCC dataset with synthetic statements.  

---
#### cfda4 
[**`Participants`**](./participants.md#cfda_clip) 

- :material-rename: **Run ID:** cfda4 
- :fontawesome-solid-user-group: **Participant:** CFDA_CLIP 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/5/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `84e0fe10980deff4b430ce81022004bd` 
- :material-text: **Run description:** Query rewriting: statement-aware QR model Retrieval: Sparse retrieval with re-ranking performed by dense retrievers. Response generation: Generative QA models.  

---
#### ConvGQR 
[**`Participants`**](./participants.md#rali) 

- :material-rename: **Run ID:** ConvGQR 
- :fontawesome-solid-user-group: **Participant:** RALI 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/3/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `447df5f57e80871a1d7e4eb3f8b1b9cb` 
- :material-text: **Run description:** ConvGQR combines query rewriting and query expansion to conduct query reformulation training on QReCC dataset, then apply on iKAT dataset. 

---
#### georgetown_infosense_ikat_run_1 
[**`Participants`**](./participants.md#infosense) 

- :material-rename: **Run ID:** georgetown_infosense_ikat_run_1 
- :fontawesome-solid-user-group: **Participant:** InfoSense 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/1/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `c1d80d317fab7fe40ed2aa719f3df2e6` 
- :material-text: **Run description:** This is a two shot approach, meaning that I had Llama generate a response to the user utterance (combined with the PTKBs automatically determined to be relevant, in a fluent-ish manner), took that response, found passages that were classified as reliable by the TF-IDF and logarithmic regression model, used those passages with llama to generate another response, found new passages, and summarized each passage (with each sentence ranked in order of relevance to query) with FastChat T5 in a 1-2 sentences, combing each summary and using that as our result or text. 

---
#### georgetown_infosense_ikat_run_2 
[**`Participants`**](./participants.md#infosense) 

- :material-rename: **Run ID:** georgetown_infosense_ikat_run_2 
- :fontawesome-solid-user-group: **Participant:** InfoSense 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/1/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `56992f67826f9905640c0e6100fe3133` 
- :material-text: **Run description:** This is a one shot approach, meaning that I had Llama generate a response to the user utterance (combined with the PTKBs automatically determined to be relevant, in a fluent-ish manner), took that response, found passages that were classified as reliable by the TF-IDF and logarithmic regression model, then summarized each passage (with each sentence ranked in order of relevance to query) with FastChat T5 in a 1-2 sentences, combing each summary and using that as our result or text. 

---
#### georgetown_infosense_ikat_run_3 
[**`Participants`**](./participants.md#infosense) 

- :material-rename: **Run ID:** georgetown_infosense_ikat_run_3 
- :fontawesome-solid-user-group: **Participant:** InfoSense 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/1/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `834fe621c5847d66027590fa05ba4d98` 
- :material-text: **Run description:** This is a one shot approach, meaning that I had Llama generate a response to the user utterance (combined with the PTKBs automatically determined to be relevant, in a fluent-ish manner), took that response, found the top passages as scored by BM25, then summarized each passage (with each sentence ranked in order of relevance to query) with FastChat T5 in a 1-2 sentences, combing each summary and using that as our result or text.  

---
#### GRILL_BM25_T5Rewriter_T5Ranker_BARTSummariser 
[**`Participants`**](./participants.md#grill_team) 

- :material-rename: **Run ID:** GRILL_BM25_T5Rewriter_T5Ranker_BARTSummariser 
- :fontawesome-solid-user-group: **Participant:** GRILL_Team 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/1/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `b38ce956461ba62486e8a91bcc9d17ee` 
- :material-text: **Run description:** Pipeline consists of T5 for query rewriting, BM25 for initial retrieval, T5 for document/passage reranking, and a BART model for response generation. We also include a simulator in the loop based on a small LLAMA model that provides simulated user feedback and provides answers to clarification question. 

---
#### GRILL_BM25_T5Rewriter_T5Ranker_BARTSummariser_10 
[**`Participants`**](./participants.md#grill_team) 

- :material-rename: **Run ID:** GRILL_BM25_T5Rewriter_T5Ranker_BARTSummariser_10 
- :fontawesome-solid-user-group: **Participant:** GRILL_Team 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/3/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `1f2f2ee1de32902159df12c25a2af9f9` 
- :material-text: **Run description:** T5 for query rewriting, BM25 for initial retrieval then T5 for passage ranking. There is a Llama 2 based simulator in the loop that provides simulated feedback for up to 10 rounds per query 

---
#### GRILL_Colbert_BART2Summariser 
[**`Participants`**](./participants.md#grill_team) 

- :material-rename: **Run ID:** GRILL_Colbert_BART2Summariser 
- :fontawesome-solid-user-group: **Participant:** GRILL_Team 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/1/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `bf405e173bd2b19e70d2f15b4d44d02a` 
- :material-text: **Run description:** Run uses Colbert based dense retrieval for initial retrieval and generates a response from the top three ranking passages. There is also a simulator in the loop based on a small Llama 2 model that provides simulated feedback and answers to clarifying questions based on the the user's information needs and ptkbs. 

---
#### GRILL_Colbert_Llama2Summariser_manual 
[**`Participants`**](./participants.md#trackorg) 

- :material-rename: **Run ID:** GRILL_Colbert_Llama2Summariser_manual 
- :fontawesome-solid-user-group: **Participant:** trackorg 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/1/2023 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `4ff1a205bfc08ac9d2d320330209d2d9` 
- :material-text: **Run description:** Pipeline uses colbert for retrieval with the manual query and a small LLama 2 model to generate a summary of the top 3 passages. 

---
#### GRILL_LLAMA2_only_10_docs 
[**`Participants`**](./participants.md#trackorg) 

- :material-rename: **Run ID:** GRILL_LLAMA2_only_10_docs 
- :fontawesome-solid-user-group: **Participant:** trackorg 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/1/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `e55ca7c2124003e3d19589c74371be80` 
- :material-text: **Run description:** The pipeline consists of multiple calls to a (small) LLaMA 2 with different prompts and updated versions of the conversation/task state. The first call is a rewrite call where the prompt contains the conversation so far and asks the model to reformulate the latest utterance to help a search system generate retrieve better results. The second call is a reranking call where, after initial retrieval with the rewrite from the first call, the prompt contains the conversation so far and a document and asks the model to score the document based on its relevance to the conversation. The last call is a response generation call where the prompt contains the top 3 documents and the conversation so far and asks the model to generate a response that satisfies the user's information need 

---
#### LLMConvGQR 
[**`Participants`**](./participants.md#rali) 

- :material-rename: **Run ID:** LLMConvGQR 
- :fontawesome-solid-user-group: **Participant:** RALI 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/3/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `fd8ca55b406a25358a69e2204fbd6dc4` 
- :material-text: **Run description:** LLMConvGQR combines query rewriting and query expansion based on ChatGPT to conduct query reformulation directly on iKAT dataset. 

---
#### run-1-llama-zero-shot 
[**`Participants`**](./participants.md#irlab-amsterdam) 

- :material-rename: **Run ID:** run-1-llama-zero-shot 
- :fontawesome-solid-user-group: **Participant:** IRLab-Amsterdam 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/4/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `e398405a8be2611e887751a73c3728ba` 
- :material-text: **Run description:** This run is based on zero-shot prompting the Llama 7b model.  Llama (zero-shot) is used for response generation and query rewriting.  For PTKB selection the Sentence Transformers pre-trained model is used.  For reranking, the cross-encoder model from hugging face  (ms-marco-MiniLM-L-12-v2) which is trained on passage ranking task on ms Marco dataset, is used. 

---
#### run-2-llama-fine-tuned 
[**`Participants`**](./participants.md#irlab-amsterdam) 

- :material-rename: **Run ID:** run-2-llama-fine-tuned 
- :fontawesome-solid-user-group: **Participant:** IRLab-Amsterdam 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/4/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `6d14f0833bc13def50064627f7b933cc` 
- :material-text: **Run description:** The llama model is fine-tuned in this task for query rewriting and response generation. For PTKB selection (Sentence Transformers), and for Reranking cross-encoder (MiniLM12) from hugging face is used.  

---
#### run-3-llama-fine-tuned-manual 
[**`Participants`**](./participants.md#irlab-amsterdam) 

- :material-rename: **Run ID:** run-3-llama-fine-tuned-manual 
- :fontawesome-solid-user-group: **Participant:** IRLab-Amsterdam 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/4/2023 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `a8fcd8da14e80d7f6461f3d6516a310b` 
- :material-text: **Run description:** This run is a manual run based on using the llama(7b) model fine-tuned on the training dataset of ikat. The llama model is used for response generation.  For re-ranking and BM25 the manually-rewritten query and relevant ground truth ptkb statements are used.  

---
#### run-4-GPT-4 
[**`Participants`**](./participants.md#irlab-amsterdam) 

- :material-rename: **Run ID:** run-4-GPT-4 
- :fontawesome-solid-user-group: **Participant:** IRLab-Amsterdam 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/4/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `f878306191f94221d63e9bc0f7df2d0e` 
- :material-text: **Run description:** In this run an initial answer is generated for each turn using the GPT-4 model. Then, the GPT-4 is used to generate 5 queries for each answer. The generated queries are passed to a BM25 model and re-ranker (cross-encoder miniLM). The first 2 documents retrieved by each query are selected and passed to GPT-4 to generate the response text. 

---
#### run_automatic_dense_damo_canard_16000_recall 
[**`Participants`**](./participants.md#iitd) 

- :material-rename: **Run ID:** run_automatic_dense_damo_canard_16000_recall 
- :fontawesome-solid-user-group: **Participant:** IITD 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/4/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `02ba35a3916adaeffd7d6ca40299ba78` 
- :material-text: **Run description:** This method is two step pipeline. In this first step is a dense retrieval followed by reranking of passages. However the automatic queries are rewritten using query rewriting module based on T5, f. Reranking is done using T5 based model. 

---
#### run_automatic_dense_mini_LM_reranker 
[**`Participants`**](./participants.md#iitd) 

- :material-rename: **Run ID:** run_automatic_dense_mini_LM_reranker 
- :fontawesome-solid-user-group: **Participant:** IITD 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/3/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `67c8c5e6fd5ad3396f3d722581066ad2` 
- :material-text: **Run description:** This method uses two key points - 1. It uses a neural model to preserve the key elements for reformulation. So that it can keep track of conversation key items.  2. Based on conventional dense retrieval followed by neural reranking .   

---
#### run_automatic_dense_monot5 
[**`Participants`**](./participants.md#iitd) 

- :material-rename: **Run ID:** run_automatic_dense_monot5 
- :fontawesome-solid-user-group: **Participant:** IITD 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/4/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `16391510aeacffd028906faf60647d2d` 
- :material-text: **Run description:** This method is two step pipeline. In this first step is a dense retrieval followed by reranking of passages. However the automatic queries are rewritten using custom train query rewriting module based on BART, finetuned on samsum and canard dataset. Reranking is done using T5 based model 

---
#### run_automatic_llm_damo 
[**`Participants`**](./participants.md#iitd) 

- :material-rename: **Run ID:** run_automatic_llm_damo 
- :fontawesome-solid-user-group: **Participant:** IITD 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 9/4/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `0ff57448169f966dff3c35aceb7c6013` 
- :material-text: **Run description:** This method is two step pipeline. In this first step is a dense retrieval followed by reranking of passages. However the automatic queries are rewritten using custom train query rewriting module based on BART, finetuned on samsum and canard dataset. Reranking is done using COROM model 

---
#### uot-yj_run 
[**`Participants`**](./participants.md#uot-yj) 

- :material-rename: **Run ID:** uot-yj_run 
- :fontawesome-solid-user-group: **Participant:** uot-yj 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/31/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `918055d268a4da78a0939c6799da942d` 
- :material-text: **Run description:** We utilized Pyserini's LuceneSearcher tool to perform initial passage retrieval for each utterance turn. Then, multiple LLMs were employed to re-rank the top five passages retrieved in each turn by pair-wise ranking. We aggregated their results and got a final ranking. Both the passage retrieval and reranking stages consider the first two relevant PTKB statements generated by our automated runs. This is a zero-shot learning approach. 

---
#### uot-yj_run_llmnoptkb 
[**`Participants`**](./participants.md#uot-yj) 

- :material-rename: **Run ID:** uot-yj_run_llmnoptkb 
- :fontawesome-solid-user-group: **Participant:** uot-yj 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/31/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `3f89064cc43712a3680c9b9522063952` 
- :material-text: **Run description:** We utilized Pyserini's LuceneSearcher tool to perform passage retrieval for each utterance turn. Then, multiple LLMs (same with our run 1, the LLMs we used are "stabilityai/stablelm-tuned-alpha-7b," "eachadea/vicuna-13b-1.1," "jondurbin/airoboros-7b," "TheBloke/koala-13B-HF") were employed to re-rank the top five passages retrieved in each turn by pair-wise ranking. We aggregated their results and got a final ranking. Both the passage retrieval and reranking stages didn't consider relevant PTKB statements and only used our rewritten utterance in each turn. This is a zero-shot learning approach. 

---
#### uot-yj_run_monot5 
[**`Participants`**](./participants.md#uot-yj) 

- :material-rename: **Run ID:** uot-yj_run_monot5 
- :fontawesome-solid-user-group: **Participant:** uot-yj 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/31/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `0deb005e610412dbfa706db2eb8d9aa0` 
- :material-text: **Run description:** We utilized Pyserini's LuceneSearcher tool to perform passage retrieval for each utterance turn. Then, we used MonoT5 to conduct the passage reranking process. Both the passage retrieval and reranking stages consider the top-2 relevant PTKB statements in our automatic PTKB statement ranking runs in each turn. This is a zero-shot learning approach. 

---
#### uot-yj_run_rankgpt35 
[**`Participants`**](./participants.md#uot-yj) 

- :material-rename: **Run ID:** uot-yj_run_rankgpt35 
- :fontawesome-solid-user-group: **Participant:** uot-yj 
- :material-format-text: **Track:** Interactive Knowledge Assistance 
- :material-calendar: **Year:** 2023 
- :material-upload: **Submission:** 8/31/2023 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** primary 
- :material-fingerprint: **MD5:** `97fff2a4416ae42df3d22b137c512eb4` 
- :material-text: **Run description:** We utilized Pyserini's LuceneSearcher tool to perform passage retrieval for each utterance turn. Then, a combination of GPT-3.5 model with prompts and a sliding window was employed to conduct the reranking process. Both the passage retrieval and reranking stages consider the top-2 relevant PTKB statements in our automatic PTKB statement ranking runs in each turn. This is a zero-shot learning approach. 

---
