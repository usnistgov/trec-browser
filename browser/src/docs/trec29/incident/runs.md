# Runs - Incident Streams 2020 

#### BJUT-run 
[**`Participants`**](./participants.md#bjut2020), [**`Proceedings`**](./proceedings.md#bjut-at-trec-2020-incident-streams-track) 

- :material-rename: **Name:** BJUT-run 
- :fontawesome-solid-user-group: **Participant:** BJUT2020 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/24/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task1 
- :material-fingerprint: **MD5:** `e5569c9dccc76eff1758072d9f704c56` 
- :material-text: **Run description:** Our model performs a large number of preprocessing operations on the data and then inputs it into the fast-bert model and use the user-defined importance score function to output the importance score. 

---
#### CD_CS_R1.2020A.task1 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** CD_CS_R1.2020A.task1 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-text: **Run description:** This run applies BERT_base for multi-task learning in information type categorisation and priority estimation. 

---
#### CD_CS_R2.2020A.task1 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** CD_CS_R2.2020A.task1 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-text: **Run description:** This run first applies BERT_base for multi-task learning in information type categorisation and priority estimation. Then, a fine-tuned ELECTRA is used to re-predict those that are not assigned any labels by BERT in the first stage. The fine-tuned ELECTRA is trained on the training tweets that belong to important information types (a ranking model that uses the query description and raw tweet text as inputs) 

---
#### CD_CS_R3.2020A.task1 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** CD_CS_R3.2020A.task1 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-text: **Run description:** Similar to Run2, the difference is that the training data is augmented using BART's token replace prediction technique. 

---
#### CD_CS_R4.2020A.task1 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** CD_CS_R4.2020A.task1 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-text: **Run description:** Similar to Run2, the difference is that the training data is augmented using distilGPT2 multi-task fine-tuning for generation (with control codes). 

---
#### CD_CS_T2_R1.2020A.task2 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** CD_CS_T2_R1.2020A.task2 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task2 
- :material-text: **Run description:** This run applies bert_base fine-tuned on label and text pairs for estimating which information types a test tweet matches with well. Priority is simply estimated by the numeric conversion of the predicted information types. 

---
#### elmo_all_brf 
[**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-uogtr-at-the-trec-2020-incident-streams-track) 

- :material-rename: **Name:** elmo_all_brf 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-fingerprint: **MD5:** `a6e8382c39b7390121ed172462b5f752` 
- :material-text: **Run description:** ELMo word embeddings used to represent tweet text. Other features include binary representation of the presence of location in the tweet text, numeric features of hashtag, URL, media metadata and one-hot encoding of crisis category as per the topics file (ie. earthquake, flood etc.) Model uses the binary relevance approach for multi-label classification and a Balanced Random Forest Classifier which randomly undersamples on each iteration to address class imbalance. 

---
#### elmo_all_eec 
[**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-uogtr-at-the-trec-2020-incident-streams-track) 

- :material-rename: **Name:** elmo_all_eec 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-fingerprint: **MD5:** `0072e048d1d94417993c3db31299ce6b` 
- :material-text: **Run description:** ELMo word embeddings used to represent tweet text. Other features include binary representation of the presence of location in the tweet text, numeric features of hashtag, URL, media metadata and one-hot encoding of crisis category as per the topics file (ie. earthquake, flood etc.) Model uses the binary relevance approach for multi-label classification and an 'Easy Ensemble Classifier' which uses a combination of AdaBoost learners to boost minority labels and random undersampling on the majority ones. 

---
#### elmo_all_tfidf_brf 
[**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-uogtr-at-the-trec-2020-incident-streams-track) 

- :material-rename: **Name:** elmo_all_tfidf_brf 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-fingerprint: **MD5:** `3f67dee78e7920dc5d83318065f49055` 
- :material-text: **Run description:** ELMo word embeddings used to represent tweet text with additional TF-IDF of 500 most common terms. Other features include binary representation of the presence of location in the tweet text, numeric features of hashtag, URL, media metadata and one-hot encoding of crisis category as per the topics file (ie. earthquake, flood etc.). Model uses the binary relevance approach for multi-label classification and a Balanced Random Forest Classifier which randomly undersamples the majority classes on each iteration. 

---
#### elmo_all_tfidf_eec 
[**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-uogtr-at-the-trec-2020-incident-streams-track) 

- :material-rename: **Name:** elmo_all_tfidf_eec 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-text: **Run description:** ELMo word embeddings used to represent tweet text with additional TF-IDF of 500 most common terms. Other features include binary representation of the presence of location in the tweet text, numeric features of hashtag, URL, media metadata and one-hot encoding of crisis category as per the topics file (ie. earthquake, flood etc.). Model uses the binary relevance approach for multi-label classification and an 'Easy Ensemble Classifier' which uses a combination of AdaBoost learners to boost minority labels and random undersampling on the majority ones. 

---
#### elmo_textonly_eec_covid 
[**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-terrier-team-uogtr-at-the-trec-2020-incident-streams-track) 

- :material-rename: **Name:** elmo_textonly_eec_covid 
- :fontawesome-solid-user-group: **Participant:** UoGTr 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/9/2020 
- :material-text-search: **Task:** 2020A-task3 

---
#### njit-sub01.text.2020A.task1 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit-sub01.text.2020A.task1 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-fingerprint: **MD5:** `3f67dee78e7920dc5d83318065f49055` 
- :material-text: **Run description:** This system uses transfer learning to construct embeddings of social media content, learns a mapping from these embeddings to the TREC-IS label space, and generates labels of information type and priority from these models. We use pre-trained RoBERTa models provided by the simpletransformers interface to HuggingFace's Transformers library for these models. 

---
#### njit-sub01.text.2020A.task2 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit-sub01.text.2020A.task2 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task2 
- :material-fingerprint: **MD5:** `9d4ad6b3e52c6a6eabf47282c5229b61` 
- :material-text: **Run description:** This system uses transfer learning to construct embeddings of social media content, learns a mapping from these embeddings to the TREC-IS label space, and generates labels of information type and priority from these models. We use pre-trained RoBERTa models provided by the simpletransformers interface to HuggingFace's Transformers library for these models. 

---
#### njit-sub01.text.2020A.task3 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit-sub01.text.2020A.task3 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/11/2020 
- :material-text-search: **Task:** 2020A-task3 
- :material-fingerprint: **MD5:** `bf04529c878bd4b059224d033e3ba2b7` 
- :material-text: **Run description:** This system uses transfer learning to construct embeddings of social media content, learns a mapping from these embeddings to the TREC-IS label space, and generates labels of information type and priority from these models. We use pre-trained RoBERTa models provided by the simpletransformers interface to HuggingFace's Transformers library for these models. 

---
#### njit-sub02.text+aug.2020A.task1 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit-sub02.text+aug.2020A.task1 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-fingerprint: **MD5:** `5ed150d4fc7828c9633101b58458a74c` 
- :material-text: **Run description:** This system uses transfer learning to construct embeddings of social media content, learns a mapping from these embeddings to the TREC-IS label space, and generates labels of information type and priority from these models. We use pre-trained RoBERTa models provided by the simpletransformers interface to HuggingFace's Transformers library for these models. We also employ a simple text augmentation heuristic to expand our training data by replacing words with synonyms defined in NLTK. 

---
#### njit-sub02.text+aug.2020A.task2 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit-sub02.text+aug.2020A.task2 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/2/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-fingerprint: **MD5:** `9559acd580e5bca0d7182bd0d1d21d0d` 
- :material-text: **Run description:** This system uses transfer learning to construct embeddings of social media content, learns a mapping from these embeddings to the TREC-IS label space, and generates labels of information type and priority from these models. We use pre-trained RoBERTa models provided by the simpletransformers interface to HuggingFace's Transformers library for these models. We also employ a simple text augmentation heuristic to expand our training data by replacing words with synonyms defined in NLTK. 

---
#### njit-sub02.text+aug.2020A.task3 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit-sub02.text+aug.2020A.task3 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/11/2020 
- :material-text-search: **Task:** 2020A-task3 
- :material-fingerprint: **MD5:** `95da96cd974455456c89c6ee8e6e1829` 
- :material-text: **Run description:** This system uses transfer learning to construct embeddings of social media content, learns a mapping from these embeddings to the TREC-IS label space, and generates labels of information type and priority from these models. We use pre-trained RoBERTa models provided by the simpletransformers interface to HuggingFace's Transformers library for these models. We also employ a simple text augmentation heuristic to expand our training data by replacing words with synonyms defined in NLTK. 

---
#### njit.s1.aug 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit.s1.aug 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/23/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task1 
- :material-fingerprint: **MD5:** `231d44b0f7d820594fb0c77938618871` 
- :material-text: **Run description:** This run uses RoBERTa to generate embeddings for tweets and then uses SVM and SVR on the resulting embeddings to generate information types and priorities. To deal with class imbalance, we augment the training data with weak-supervision-based training examples wherein we replace nouns and verbs with synonyms using the WordNet external resource. 

---
#### njit.s1.aug.t2 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit.s1.aug.t2 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/23/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task2 
- :material-fingerprint: **MD5:** `ec838ac374cb371b1b21ef3921ac564c` 
- :material-text: **Run description:** This run uses RoBERTa to generate embeddings for tweets and then uses SVM and SVR on the resulting embeddings to generate information types and priorities. To deal with class imbalance, we augment the training data with weak-supervision-based training examples wherein we replace nouns and verbs with synonyms using the WordNet external resource. 

---
#### njit.s1.aug.t3 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit.s1.aug.t3 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/23/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task3 
- :material-fingerprint: **MD5:** `c532926f335ff7a93bbdd42b8c822072` 
- :material-text: **Run description:** This run uses RoBERTa to generate embeddings for tweets and then uses SVM and SVR on the resulting embeddings to generate information types and priorities. To deal with class imbalance, we augment the training data with weak-supervision-based training examples wherein we replace nouns and verbs with synonyms using the WordNet external resource. 

---
#### njit.s2.cmmd.t1 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit.s2.cmmd.t1 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/23/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task1 
- :material-fingerprint: **MD5:** `d7c2d7aacdf15fe6e4c5329b3dd1d3ac` 
- :material-text: **Run description:** This run uses RoBERTa to generate embeddings for tweets and then uses SVM and SVR on the resulting embeddings to generate information types and priorities. We also augment the training data using non-humanitarian labels from CrisisMMD labeling and with our weak-supervision-based text augmentation. From CrisisMMD, we create a classifier that tags tweets with CrisisMMD labels, and we augment the text with those labels. 

---
#### njit.s2.cmmd.t2 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit.s2.cmmd.t2 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/23/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task2 
- :material-fingerprint: **MD5:** `ca30a2159967dcffc088b880a88f27f1` 
- :material-text: **Run description:** This run uses RoBERTa to generate embeddings for tweets and then uses SVM and SVR on the resulting embeddings to generate information types and priorities. We also augment the training data using non-humanitarian labels from CrisisMMD labeling and with our weak-supervision-based text augmentation. From CrisisMMD, we create a classifier that tags tweets with CrisisMMD labels, and we augment the text with those labels. 

---
#### njit.s2.cmmd.t3 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit.s2.cmmd.t3 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/23/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task3 
- :material-fingerprint: **MD5:** `26f15e55171fc2aee716462d7c5f89a2` 
- :material-text: **Run description:** This run uses RoBERTa to generate embeddings for tweets and then uses SVM and SVR on the resulting embeddings to generate information types and priorities. We also augment the training data using non-humanitarian labels from CrisisMMD labeling and with our weak-supervision-based text augmentation. From CrisisMMD, we create a classifier that tags tweets with CrisisMMD labels, and we augment the text with those labels. 

---
#### njit.s3.img.t1 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit.s3.img.t1 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/23/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task1 
- :material-fingerprint: **MD5:** `b5ca9be9041b20a49006d98d79c29bcc` 
- :material-text: **Run description:** This run uses RoBERTa to generate embeddings for tweets and then uses SVM and SVR on the resulting embeddings to generate information types and priorities. We also augment the training data using non-humanitarian labels from CrisisMMD labeling and with our weak-supervision-based text augmentation. From CrisisMMD, we create a classifier that tags tweets with CrisisMMD labels, and we augment the text with those labels. We also integrate CrisisMMD's image labels to generate priority scores for tweets with images, where we then take the max priority label between the text and image. 

---
#### njit.s3.img.t2 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit.s3.img.t2 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/23/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task2 
- :material-fingerprint: **MD5:** `1080fd47f44a50fce7f83d74d712549e` 
- :material-text: **Run description:** This run uses RoBERTa to generate embeddings for tweets and then uses SVM and SVR on the resulting embeddings to generate information types and priorities. We also augment the training data using non-humanitarian labels from CrisisMMD labeling and with our weak-supervision-based text augmentation. From CrisisMMD, we create a classifier that tags tweets with CrisisMMD labels, and we augment the text with those labels. We also integrate CrisisMMD's image labels to generate priority scores for tweets with images, where we then take the max priority label between the text and image. 

---
#### njit.s3.img.t3 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit.s3.img.t3 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/23/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task3 
- :material-fingerprint: **MD5:** `2e72ede0df0ee366228c77276acaa745` 
- :material-text: **Run description:** This run uses RoBERTa to generate embeddings for tweets and then uses SVM and SVR on the resulting embeddings to generate information types and priorities. We also augment the training data using non-humanitarian labels from CrisisMMD labeling and with our weak-supervision-based text augmentation. From CrisisMMD, we create a classifier that tags tweets with CrisisMMD labels, and we augment the text with those labels. We also integrate CrisisMMD's image labels to generate priority scores for tweets with images, where we then take the max priority label between the text and image. 

---
#### njit.s4.cml.t1 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit.s4.cml.t1 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/25/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task1 
- :material-fingerprint: **MD5:** `4d2b887dd29f293438b7fe2aa8806ba2` 
- :material-text: **Run description:** Classic ML approach that uses text and user verification to classify and prioritize content. 

---
#### njit.s4.cml.t2 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit.s4.cml.t2 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/25/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task2 
- :material-fingerprint: **MD5:** `e6b107d05f9c7ddc779ca7e312f7e4e6` 
- :material-text: **Run description:** Classic ML approach that uses text and user verification to classify and prioritize content. 

---
#### njit.s4.cml.t3 
[**`Participants`**](./participants.md#njit), [**`Proceedings`**](./proceedings.md#improving-classification-of-crisis-related-social-media-content-via-text-augmentation-and-image-analysis) 

- :material-rename: **Name:** njit.s4.cml.t3 
- :fontawesome-solid-user-group: **Participant:** njit 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/25/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task3 
- :material-fingerprint: **MD5:** `ae8f3fbfddec569d3be46ca63e6659d1` 
- :material-text: **Run description:** Classic ML approach that uses text and user verification to classify and prioritize content. 

---
#### sc-rf-021 
[**`Participants`**](./participants.md#sc) 

- :material-rename: **Name:** sc-rf-021 
- :fontawesome-solid-user-group: **Participant:** sc 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/1/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-fingerprint: **MD5:** `2e5663c8711f08db250cfd13e8c367e2` 
- :material-text: **Run description:** Random Forest estimator with tfidf vectorizer with some word cleaning and auto-correction. 

---
#### sc-rf-022 
[**`Participants`**](./participants.md#sc) 

- :material-rename: **Name:** sc-rf-022 
- :fontawesome-solid-user-group: **Participant:** sc 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/1/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-fingerprint: **MD5:** `0b44cdf66f2b844a421f7e03989e6c92` 
- :material-text: **Run description:** Random Forest estimator with tfidf vectorizer with some word cleaning and auto-correction. 

---
#### sc-rf-023 
[**`Participants`**](./participants.md#sc) 

- :material-rename: **Name:** sc-rf-023 
- :fontawesome-solid-user-group: **Participant:** sc 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/1/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-fingerprint: **MD5:** `b9af0aa57479aac8b90e0c7258257c12` 
- :material-text: **Run description:** Random Forest estimator with tfidf vectorizer with some word cleaning and auto-correction. 

---
#### sc-rf-024 
[**`Participants`**](./participants.md#sc) 

- :material-rename: **Name:** sc-rf-024 
- :fontawesome-solid-user-group: **Participant:** sc 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/1/2020 
- :material-text-search: **Task:** 2020A-task1 
- :material-fingerprint: **MD5:** `631225208c3a08b7f1d18a47037ec652` 
- :material-text: **Run description:** Random Forest estimator with tfidf vectorizer with some word cleaning and auto-correction. 

---
#### sc-rf-025 
[**`Participants`**](./participants.md#sc) 

- :material-rename: **Name:** sc-rf-025 
- :fontawesome-solid-user-group: **Participant:** sc 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/1/2020 
- :material-text-search: **Task:** 2020A-task2 
- :material-fingerprint: **MD5:** `c2153e8c4ab41e45ee50ee859404b4d6` 
- :material-text: **Run description:** Random Forest estimator with tfidf vectorizer with some word cleaning and auto-correction. 

---
#### sc-rf-026 
[**`Participants`**](./participants.md#sc) 

- :material-rename: **Name:** sc-rf-026 
- :fontawesome-solid-user-group: **Participant:** sc 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/1/2020 
- :material-text-search: **Task:** 2020A-task2 
- :material-fingerprint: **MD5:** `a957ed4c4f82c91a5c065b044361fb12` 
- :material-text: **Run description:** Random Forest estimator with tfidf vectorizer with some word cleaning and auto-correction. 

---
#### sc-rf-027 
[**`Participants`**](./participants.md#sc) 

- :material-rename: **Name:** sc-rf-027 
- :fontawesome-solid-user-group: **Participant:** sc 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/1/2020 
- :material-text-search: **Task:** 2020A-task2 
- :material-fingerprint: **MD5:** `4482caeeb2d965ca098d1e3a5e138961` 
- :material-text: **Run description:** Random Forest estimator with tfidf vectorizer with some word cleaning and auto-correction. 

---
#### sc-rf-028 
[**`Participants`**](./participants.md#sc) 

- :material-rename: **Name:** sc-rf-028 
- :fontawesome-solid-user-group: **Participant:** sc 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/1/2020 
- :material-text-search: **Task:** 2020A-task2 
- :material-fingerprint: **MD5:** `25fb01d0251f033e23909cad5fa62e69` 
- :material-text: **Run description:** Random Forest estimator with tfidf vectorizer with some word cleaning and auto-correction. 

---
#### sc-rf-029 
[**`Participants`**](./participants.md#sc) 

- :material-rename: **Name:** sc-rf-029 
- :fontawesome-solid-user-group: **Participant:** sc 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/8/2020 
- :material-text-search: **Task:** 2020A-task3 
- :material-fingerprint: **MD5:** `69ea1ce72db724e8731acddca47c4006` 
- :material-text: **Run description:** Random Forest estimator with tfidf vectorizer with some word cleaning and auto-correction. Current approach is clearly not effective as most failed to match but submitted anyway. 

---
#### sc-rf-030 
[**`Participants`**](./participants.md#sc) 

- :material-rename: **Name:** sc-rf-030 
- :fontawesome-solid-user-group: **Participant:** sc 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/8/2020 
- :material-text-search: **Task:** 2020A-task3 
- :material-fingerprint: **MD5:** `8e51f7cc583b68e1514bd8a1e37b561e` 
- :material-text: **Run description:** Random Forest estimator with tfidf vectorizer with some word cleaning and auto-correction. Current approach is clearly not effective as most failed to match but submitted anyway. 

---
#### sc-rf-031 
[**`Participants`**](./participants.md#sc) 

- :material-rename: **Name:** sc-rf-031 
- :fontawesome-solid-user-group: **Participant:** sc 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/8/2020 
- :material-text-search: **Task:** 2020A-task3 
- :material-fingerprint: **MD5:** `1b0215d9e211cb6f3ae166c52af7a333` 
- :material-text: **Run description:** Random Forest estimator with tfidf vectorizer with some word cleaning and auto-correction. Current approach is clearly not effective as most failed to match but submitted anyway. 

---
#### sc-rf-032 
[**`Participants`**](./participants.md#sc) 

- :material-rename: **Name:** sc-rf-032 
- :fontawesome-solid-user-group: **Participant:** sc 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/8/2020 
- :material-text-search: **Task:** 2020A-task3 
- :material-fingerprint: **MD5:** `2e3030213f53ced5c8b528dc5327e109` 
- :material-text: **Run description:** Random Forest estimator with tfidf vectorizer with some word cleaning and auto-correction. Current approach is clearly not effective as most failed to match but submitted anyway. 

---
#### ucd-run1 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** ucd-run1 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/24/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task1 
- :material-fingerprint: **MD5:** `a43390e188fa4bbcdc5cfe4970899d88` 
- :material-text: **Run description:** This is a baseline with techniques developed in 2019-A edition, i.e., multi-task learning transformers for crisis tweet categorisation.    

---
#### ucd-run2 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** ucd-run2 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/24/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task1 
- :material-fingerprint: **MD5:** `8587a793d4f0f2d08be773f3dea9c071` 
- :material-text: **Run description:** Similar to run1 but the predictions are combined probabilities instead of binary scores. 

---
#### ucd-run3 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** ucd-run3 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/24/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task1 
- :material-fingerprint: **MD5:** `5b979902ee29d25fecc59e67457a8af3` 
- :material-text: **Run description:** This run applies a text-to-text transformer (T5) for crisis tweet categoristion (treated as a question answering task). 

---
#### ucd-run4 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** ucd-run4 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/24/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task3 
- :material-fingerprint: **MD5:** `13a0d362133ad6d120c2580bff567c2a` 
- :material-text: **Run description:** This run applies a text-to-text transformer (T5) for COVID tweet categoristion (treated as a question answering task). 

---
#### ucd-run5 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** ucd-run5 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/25/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task1 
- :material-fingerprint: **MD5:** `8c718fe1e7b8179ea0f336b8c9d4f2e4` 
- :material-text: **Run description:** Similar to run3, the difference is that this run is trained on all previous TREC-IS dataset including 2020-A COVID data. 

---
#### UCD_CS_T3_R1 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** UCD_CS_T3_R1 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/9/2020 
- :material-text-search: **Task:** 2020A-task3 
- :material-fingerprint: **MD5:** `19fb768e2479e7b0e556330379f95245` 
- :material-text: **Run description:** This run applies BM25 for matching the similarities between a test tweet and each information type as required in this task 3. The information types used as the queries are constructed manually. Those not assigned any types are further estimated by a ELECTRA-base ranking model fine-tuned on the training set. In this run, priority is simply converted from the predicted information types based on the analysis of information types with respect to priority levels of training tweets. 

---
#### UCD_CS_T3_R2 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** UCD_CS_T3_R2 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/9/2020 
- :material-text-search: **Task:** 2020A-task3 
- :material-fingerprint: **MD5:** `e8d4fdd7b42256e0a7f62d1395de0f8f` 
- :material-text: **Run description:** This run fine-tunes a BERT-base model for multi-task learning, only on the training tweets with information type as required in this task 3. The information type categorisation is defined as a multi-label classification task and priority estimation is defined as a regression task. 

---
#### UCD_CS_T3_R3 
[**`Participants`**](./participants.md#ucd-cs), [**`Proceedings`**](./proceedings.md#multi-task-transfer-learning-for-finding-actionable-information-from-crisis-related-messages-on-social-media) 

- :material-rename: **Name:** UCD_CS_T3_R3 
- :fontawesome-solid-user-group: **Participant:** UCD-CS 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 6/9/2020 
- :material-text-search: **Task:** 2020A-task3 
- :material-fingerprint: **MD5:** `1c74034a4b341440e2eeb1ee036566a6` 
- :material-text: **Run description:** Similar to R2, the difference is that the training dataset is augmented by the GPT-2 generative model (distilled version) that is adapted to this domain by fine-tuning with control codes. 

---
#### ufmg-sars-test 
[**`Participants`**](./participants.md#ufmg) 

- :material-rename: **Name:** ufmg-sars-test 
- :fontawesome-solid-user-group: **Participant:** ufmg 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/23/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task1 
- :material-fingerprint: **MD5:** `164d3c00b3d081001870690fd15e5f5f` 
- :material-text: **Run description:** XGBoost classifiers and regressors using the same feature set. Feature set comprises basic statistics of the tweet's text, named entities features, part of speech tagging features, and sentiment analysis features.  

---
#### ufmg-sars-test-t2 
[**`Participants`**](./participants.md#ufmg) 

- :material-rename: **Name:** ufmg-sars-test-t2 
- :fontawesome-solid-user-group: **Participant:** ufmg 
- :material-format-text: **Track:** Incident Streams 
- :material-calendar: **Year:** 2020 
- :material-upload: **Submission:** 9/23/2020 
- :fontawesome-solid-user-gear: **Type:** auto 
- :material-text-search: **Task:** 2020b-task2 
- :material-fingerprint: **MD5:** `4bfb1999c4e64e49a0aa7029746b08e4` 
- :material-text: **Run description:** XGBoost classifiers and regressors using the same feature set. Feature set comprises basic statistics of the tweet's text, named entities features, part of speech tagging features, and sentiment analysis features.  

---
