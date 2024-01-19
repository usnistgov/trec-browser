# Runs - Total Recall 2016 

#### ah4_descsubset 
[**`Participants`**](./participants.md#irsfsu2016), [**`Proceedings`**](./proceedings.md#san-francisco-state-university-sfsu-at-total-recall-track-of-trec-2016), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** ah4_descsubset 
- :fontawesome-solid-user-group: **Participant:** IR.SFSU.2016 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/31/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** limited 
- :material-text: **Run description:** This run on athome4descsubset use the same methods as ah4_run1:  1. Reducing Increasing Rate of Batch Size to L/20.  2. Using Unigram/Bigram SVM Features 3. Stopword pruning  4. Preserving words contain digits 

---
#### ah4_run1 
[**`Participants`**](./participants.md#irsfsu2016), [**`Proceedings`**](./proceedings.md#san-francisco-state-university-sfsu-at-total-recall-track-of-trec-2016), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** ah4_run1 
- :fontawesome-solid-user-group: **Participant:** IR.SFSU.2016 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/28/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** This run combines following methodologies: 1. Reducing Increasing Rate of Batch Size According to the best result among the experiment on athome1, we decide increase the batch-size by L/20.  2. Using Unigram/Bigram SVM Features Data analysis of the athome1 task reveals that the relevant documents usually contain the query phrases, while the non-relevant documents contain only single terms, and often these single terms convey slightly different meaning from the query topic. This inspires this approach of combining bigram features with original unigram features. 3. Stopword pruning The 25 pruned stop words used are :  "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "he", "in", "is", "it", "its", "of", "on", "that", "the", "to", "was", "were", "will", “with" 4. Preserving words contain digits BMI skips words contain digits[0-9] while building the inverted index of corpus. We expect preserving words contain digits or pure numbers can improve the recall of BMI.   

---
#### ah4_run2_seed_expansion 
[**`Participants`**](./participants.md#irsfsu2016), [**`Proceedings`**](./proceedings.md#san-francisco-state-university-sfsu-at-total-recall-track-of-trec-2016), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** ah4_run2_seed_expansion 
- :fontawesome-solid-user-group: **Participant:** IR.SFSU.2016 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/28/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** Run2 is run1 + following seed expansion methodologies: 1. Seed Expansion using Wikipedia In our approach, we send the original topic as the query to Wikipedia search API. If multiple pages are returned, only the top one Wikipedia page is used. The summary/content field of the Wikipedia page and original topic are combined to expanded seed.  2. Seed Expansion using Google Word2Vec In our approach, the corpus of current task was used as the training data for Word2Vec.  Therefore, the prediction of surrounding words is computed according to the behavior of the dataset.  

---
#### auto_shift_rotation 
[**`Participants`**](./participants.md#ims_unipd), [**`Proceedings`**](./proceedings.md#the-university-of-padua-ims-at-trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** auto_shift_rotation 
- :fontawesome-solid-user-group: **Participant:** ims_unipd 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/31/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** We used the two dimensional representation of probabilities to choose the documents to be assessed and to call our shot. The first round of batches was called using the same BM25 (baseline_bm25_ smoothing) approach used for the baseline. We run the BM25 until 10 relevant documents are found or at most 100 documents are judged. Then we started to use the ranking/classification line by adjusting the line parameters automatically b looking at the distribution of relevant documents. The line spanned the 2D space from minus infinity to minus 10 for the first batches, then we rotated the line until a slop of 1.5 was reached, then we shifted again until minus 3. As soon as we find a line that has all the relevant documents found at that point *and* none documents to judge below the line we call the shot. 

---
#### auto_shift_rotation_exp 
[**`Participants`**](./participants.md#ims_unipd), [**`Proceedings`**](./proceedings.md#the-university-of-padua-ims-at-trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** auto_shift_rotation_exp 
- :fontawesome-solid-user-group: **Participant:** ims_unipd 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/31/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** This is a variation of the previously submitted run (run auto_shift_rotation) that differs in the following points: 1) we automatically expanded the query using the first batch of documents in order to have 10 terms with 5 relevant documents, and 20 terms with 10 relevant documents. 2) we stopped the first round either when 20 relevant documents were found or 100 documents are judged. 3) the idea of using the ranking/classification line is the same but the adjustment of the parameters is more accurate (or we expect it to be more accurate). We first span the 2D space from minus infinity to minus  10, then we slightly rotate until the slope of the relevant documents is reached, then shift again then rotate again, etc... Calling the shot is the same as the previous run. 

---
#### baseline_bm25 
[**`Participants`**](./participants.md#ims_unipd), [**`Proceedings`**](./proceedings.md#the-university-of-padua-ims-at-trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** baseline_bm25 
- :fontawesome-solid-user-group: **Participant:** ims_unipd 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/29/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** This is a basic experiment that uses BM25 with pseudo-relevance feedback to expand the query with at most 10 terms. A standard stopword list (174 terms) and a Porter stemmer have been applied before indexing the collection. Numbers have been removed as well. Relevance judgements are called in batches of - 50 for 100 times (the first 5,000 documents) - 100 for 100 times (10,000 docs) - 500 for 70 times (35,000 docs) - 5,000 until the end At each iteration, the probability of terms (relevant and non relevant) is re-calculated and the query is expanded by choosing the top 10 terms for which the difference P(t | rel) - P(t | non_rel) is the largest. 

---
#### baseline_bm25_smoothing 
[**`Participants`**](./participants.md#ims_unipd), [**`Proceedings`**](./proceedings.md#the-university-of-padua-ims-at-trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** baseline_bm25_smoothing 
- :fontawesome-solid-user-group: **Participant:** ims_unipd 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/31/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** In this experiment, we tried the same BM25 approach with  a less a aggressive probability smoothing (compared to the baseline_bm25 run) and a slightly different automatic query expansion based on the following idea: when there are at least 5 relevant documents, we take the top 10 terms with the highest difference P(t | rel) - P(t | nonrel). 

---
#### manual_seed 
[**`Participants`**](./participants.md#catres), [**`Proceedings`**](./proceedings.md#an-exploration-of-total-recall-with-multiple-manual-seedings), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** manual_seed 
- :fontawesome-solid-user-group: **Participant:** catres 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/9/2016 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** The basic method was to let four different people search and/or search and review documents for a very short amount of time, pool all the docs that they found in that time (both positive and negative, i.e. everything that they laid eyeballs on in that time, of course) and then kick off a continuous, fully automated run from that point forward.  After manual seeding, continuous iIteration was run in a fully automated manner (no additional human intervention of any kind) until the algorithm determined it had hit its "call your shot" point, and then the shot call was done without any human intervention.  Once the shot was officially, automatically called, however, a human stepped in and did his/her own determination, i.e. ran a bunch of the topics for some more iterations and manually watched the progress.  For many of the topics, the automated shot call was correct.  For a smaller number, the shot call was not correct.  The human continued running iterations on those topics for which more relevant documents continued to be found.  Batch size was varied slightly, based on a combination of how rich the continued iterations were, plus how much time was left until the TREC deadline.  I.e. in an ideal process batch sizes would have been kept small throughout, but in the practical interest of a time deadline, a few of the batch sizes were increased.  Once time ran out, the remainder of the "unjudged" documents were submitted to the TREC server in current rank order.   There is no main hypothesis in this experiment.. the hypothesis will come once we do some post hoc runs. 

---
#### Run1 
[**`Participants`**](./participants.md#e-discoveryteam), [**`Proceedings`**](./proceedings.md#trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** Run1 
- :fontawesome-solid-user-group: **Participant:** e-discoveryteam 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/31/2016 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** All runs were manual using human input and judgment. A hybrid multimodal approach was used with a combination of keyword terms, predictive coding, and other analytics tools. 

---
#### sandbox_run 
[**`Participants`**](./participants.md#irsfsu2016), [**`Proceedings`**](./proceedings.md#san-francisco-state-university-sfsu-at-total-recall-track-of-trec-2016), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** sandbox_run 
- :fontawesome-solid-user-group: **Participant:** IR.SFSU.2016 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/5/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** sandbox 
- :material-text: **Run description:**  This run on athome4descsubset use the same methods as ah4_run1 1. Reducing Increasing Rate of Batch Size to L/20.   2. Using Unigram/Bigram SVM Features  3. Stopword pruning   4. Preserving words contain digits 

---
#### UWathome4Baseline 
[**`Participants`**](./participants.md#waterloocormack), [**`Proceedings`**](./proceedings.md#when-to-stop-waterloo-cormack-participation-in-the-trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** UWathome4Baseline 
- :fontawesome-solid-user-group: **Participant:** WaterlooCormack 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/31/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** BMI, with no changes.  Baseline run with short topic descriptions. 

---
#### UWathome4descBaseline 
[**`Participants`**](./participants.md#waterloocormack), [**`Proceedings`**](./proceedings.md#when-to-stop-waterloo-cormack-participation-in-the-trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** UWathome4descBaseline 
- :fontawesome-solid-user-group: **Participant:** WaterlooCormack 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/31/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** BMI, with no changes.  Baseline run with long topic descriptions. 

---
#### UWathome4descKnee 
[**`Participants`**](./participants.md#waterloocormack), [**`Proceedings`**](./proceedings.md#when-to-stop-waterloo-cormack-participation-in-the-trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** UWathome4descKnee 
- :fontawesome-solid-user-group: **Participant:** WaterlooCormack 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/29/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** BMI, with knee method substituted for default stopping rule.  No other changes. 

---
#### UWathome4descTarget 
[**`Participants`**](./participants.md#waterloocormack), [**`Proceedings`**](./proceedings.md#when-to-stop-waterloo-cormack-participation-in-the-trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** UWathome4descTarget 
- :fontawesome-solid-user-group: **Participant:** WaterlooCormack 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/31/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** BMI, with target method for stopping, long topic descriptions 

---
#### UWathome4Knee 
[**`Participants`**](./participants.md#waterloocormack), [**`Proceedings`**](./proceedings.md#when-to-stop-waterloo-cormack-participation-in-the-trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** UWathome4Knee 
- :fontawesome-solid-user-group: **Participant:** WaterlooCormack 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/29/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** BMI, with knee method substituted for default stopping rule.  No other changes. 

---
#### UWathome4Target 
[**`Participants`**](./participants.md#waterloocormack), [**`Proceedings`**](./proceedings.md#when-to-stop-waterloo-cormack-participation-in-the-trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** UWathome4Target 
- :fontawesome-solid-user-group: **Participant:** WaterlooCormack 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 8/31/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** full 
- :material-text: **Run description:** BMI, with target method for stopping, short topic descriptions 

---
#### uwsandboxknee 
[**`Participants`**](./participants.md#waterloocormack), [**`Proceedings`**](./proceedings.md#when-to-stop-waterloo-cormack-participation-in-the-trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** uwsandboxknee 
- :fontawesome-solid-user-group: **Participant:** WaterlooCormack 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/7/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** sandbox 
- :material-text: **Run description:** BMI with knee method stopping criterion. 

---
#### uwsandboxtarget 
[**`Participants`**](./participants.md#waterloocormack), [**`Proceedings`**](./proceedings.md#when-to-stop-waterloo-cormack-participation-in-the-trec-2016-total-recall-track), [**`Appendix`**](https://trec.nist.gov/pubs/trec25/appendices/recall/recall.pdf) 

- :material-rename: **Name:** uwsandboxtarget 
- :fontawesome-solid-user-group: **Participant:** WaterlooCormack 
- :material-format-text: **Track:** Total Recall 
- :material-calendar: **Year:** 2016 
- :material-upload: **Submission:** 9/7/2016 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** sandbox 
- :material-text: **Run description:** BMI with target method stopping criterion. 

---
