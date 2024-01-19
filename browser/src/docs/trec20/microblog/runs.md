# Runs - Microblog 2011 

#### 1 
[**`Results`**](./results.md#1), [**`Participants`**](./participants.md#knowcenter), [**`Proceedings`**](./proceedings.md#realtime-ad-hoc-search-in-twitter-know-center-at-trec-microblog-track-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/1.pdf) 

- :material-rename: **Name:** 1 
- :fontawesome-solid-user-group: **Participant:** knowcenter 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 7/29/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `8a57acc414ad236d0371f73bb4e5f0d8` 
- :material-text: **Run description:** We used Lucene for querying and ranking the Tweets. After that, we did a burst detection, identifying the time windows (interval: 3 hours) when an unusual amount of Tweets occurred. Based on our assumption that something extraordinary happened within that time, those Tweets have been ranked higher. Our final score combines both Lucene score and the Burst Detection score. If no burst was detected, than only the Lucene score was considered.  We applied simple rule-based filtering techniques. For example, Tweets which contain an @-Character are not considered. Also, we implemented a simple language guesser which removes Tweets which are not written mainly in ASCII characters.  

---
#### 2 
[**`Results`**](./results.md#2), [**`Participants`**](./participants.md#knowcenter), [**`Proceedings`**](./proceedings.md#realtime-ad-hoc-search-in-twitter-know-center-at-trec-microblog-track-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/2.pdf) 

- :material-rename: **Name:** 2 
- :fontawesome-solid-user-group: **Participant:** knowcenter 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `3f9f238b0ab1fc668091a1d4254f078c` 
- :material-text: **Run description:** We used Lucene for querying and ranking the Tweets. After that, we did a burst detection, identifying the time windows (interval: 3 hours) when an unusual amount of Tweets occurred. Based on our assumption that something extraordinary happened within that time, those Tweets have been ranked higher by a burst detection score. As second ranking factor we counted the number of retweets (retweet score) of all twitter user over the whole corpus. Note that we did not restrict this computation to retweets up the given query time. As third ranking factor, we computed the most often used hashtag per topic and ranked tweets higher that contained the most often used hashtag (hashtag score). Note that this computation has been done only on tweets posted before the query timestamp (no future evidence). Our final score combines therefore a Lucene score, the Burst Detection score, the retweet score, and the hashtag score.  If no burst was detected, only the other three score have been considered.  We applied simple rule-based filtering techniques. For example, Tweets which contain an @-Character are not considered. Also, we implemented a simple language guesser which removes Tweets which are not written mainly in ASCII characters. Besides, we computed the Levenshtein distance in order to filter out too similar tweets.  

---
#### 3 
[**`Results`**](./results.md#3), [**`Participants`**](./participants.md#knowcenter), [**`Proceedings`**](./proceedings.md#realtime-ad-hoc-search-in-twitter-know-center-at-trec-microblog-track-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/3.pdf) 

- :material-rename: **Name:** 3 
- :fontawesome-solid-user-group: **Participant:** knowcenter 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `610180ff8735df2efc62dd4bc64c4a93` 
- :material-text: **Run description:** We used Lucene for querying and ranking the Tweets. After that, we did a burst detection, identifying the time windows (interval: 3 hours) when an unusual amount of Tweets occurred. Based on our assumption that something extraordinary happened within that time, those Tweets have been ranked higher by a burst detection score. As 2nd ranking factor, we computed the most often used hashtag per topic and ranked tweets higher that contained the most often used hashtag (hashtag score). Note that this computation has been done only on tweets posted before the query timestamp (no future evidence). Our final score combines therefore a Lucene score, the Burst Detection score, and the hashtag score.  If no burst was detected, only the other two scores have been considered.  We applied simple rule-based filtering techniques. For example, Tweets which contain an @-Character are not considered. Also, we implemented a simple language guesser which removes Tweets which are not written mainly in ASCII characters. Besides, we computed the Levenshtein distance in order to filter out too similar tweets. 

---
#### 4 
[**`Results`**](./results.md#4), [**`Participants`**](./participants.md#knowcenter), [**`Proceedings`**](./proceedings.md#realtime-ad-hoc-search-in-twitter-know-center-at-trec-microblog-track-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.4.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.4), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.4), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/4.pdf) 

- :material-rename: **Name:** 4 
- :fontawesome-solid-user-group: **Participant:** knowcenter 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `902bfa494abed656cd1180796efb1612` 
- :material-text: **Run description:** We used Lucene for querying and ranking the Tweets. After that, we did a burst detection, identifying the time windows (interval: 3 hours) when an unusual amount of Tweets occurred. Based on our assumption that something extraordinary happened within that time, those Tweets have been ranked higher by a burst detection score. Our final score combines therefore a Lucene score, the Burst Detection score.  If no burst was detected, only the lucene score have been considered. We applied simple rule-based filtering techniques. For example, Tweets which contain an @-Character are not considered. Also, we implemented a simple language guesser which removes Tweets which are not written mainly in ASCII characters. Besides, we computed the Levenshtein distance in order to filter out too similar tweets. The difference to RUN IDENTIFICATION "1" is the levenshtein distance and more sophisticated stop word lists (slang, emoticons, hashtags...). 

---
#### balanceRun 
[**`Results`**](./results.md#balancerun), [**`Participants`**](./participants.md#nusis), [**`Proceedings`**](./proceedings.md#nusis-at-trec-2011-microblog-track-refining-query-results-with-hashtags), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.balanceRun.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.balanceRun), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.balanceRun), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/balanceRun.pdf) 

- :material-rename: **Name:** balanceRun 
- :fontawesome-solid-user-group: **Participant:** NUSIS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `f1100c7b9efaab524d27aaa184420646` 
- :material-text: **Run description:** we balance time and recency based on basic run results 

---
#### baseline 
[**`Results`**](./results.md#baseline), [**`Participants`**](./participants.md#ictir), [**`Proceedings`**](./proceedings.md#author-model-and-negative-feedback-methods-on-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.baseline.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.baseline), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.baseline), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/baseline.pdf) 

- :material-rename: **Name:** baseline 
- :fontawesome-solid-user-group: **Participant:** ICTIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 7/29/2011 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `4b6365c72557ec9e85c8ebabbc7b37df` 
- :material-text: **Run description:** baseline 

---
#### baseline1 
[**`Results`**](./results.md#baseline1), [**`Participants`**](./participants.md#uporto), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.baseline1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.baseline1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.baseline1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/baseline1.pdf) 

- :material-rename: **Name:** baseline1 
- :fontawesome-solid-user-group: **Participant:** UPorto 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `43872afc732b87d4e5f43e91dfba1573` 
- :material-text: **Run description:** This run is mostly a baseline of our Terrier set-up. Uses only the text of the tweets. 

---
#### baseline2 
[**`Results`**](./results.md#baseline2), [**`Participants`**](./participants.md#uporto), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.baseline2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.baseline2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.baseline2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/baseline2.pdf) 

- :material-rename: **Name:** baseline2 
- :fontawesome-solid-user-group: **Participant:** UPorto 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `6582dbdc6b1fc0cfa9cea5088ef87e52` 
- :material-text: **Run description:** Same as baseline1, but with better indexing. 

---
#### baselineBM25 
[**`Results`**](./results.md#baselinebm25), [**`Participants`**](./participants.md#ulugano), [**`Proceedings`**](./proceedings.md#university-of-lugano-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.baselineBM25.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.baselineBM25), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.baselineBM25), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/baselineBM25.pdf) 

- :material-rename: **Name:** baselineBM25 
- :fontawesome-solid-user-group: **Participant:** ULugano 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `4164b51855a8cdff45709bdc6b9081d8` 
- :material-text: **Run description:** This is a very basic run, to be used as baseline for (future) comparison with the improved ones. We used BM25 with standard settings to match the relevant tweets. The retrieved tweets were then filtered by score and time, so that the most relevant tweets for each day (from the query date) are preserved in a time-ordered way. 

---
#### Basic 
[**`Results`**](./results.md#basic), [**`Participants`**](./participants.md#elly), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.Basic.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.Basic), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.Basic), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/Basic.pdf) 

- :material-rename: **Name:** Basic 
- :fontawesome-solid-user-group: **Participant:** Elly 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `0083b6367ba46d6504d3ab146f047257` 
- :material-text: **Run description:** In response to a query, the first stage is to automatically retrieve a list of tweets and rank them based on their similarity to the query. The top 1000 tweets were submitted as the basic run results. 

---
#### basicWISTUD 
[**`Results`**](./results.md#basicwistud), [**`Participants`**](./participants.md#wis_tudelft), [**`Proceedings`**](./proceedings.md#wistud-at-trec-2011-microblog-track-exploiting-background-knowledge-from-dbpedia-and-news-articles-for-search-on-twitter), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.basicWISTUD.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.basicWISTUD), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.basicWISTUD), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/basicWISTUD.pdf) 

- :material-rename: **Name:** basicWISTUD 
- :fontawesome-solid-user-group: **Participant:** wis_tudelft 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/3/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `3c4afb51ef4cb20c4c4fc6d3a7934f91` 
- :material-text: **Run description:** Baseline run: standard retrieval with some filters (English language tweets only, no retweets, no directed tweets, no tweets with less than 100 characters, no tweets that mainly consist of a URL). 

---
#### ciirRun1 
[**`Results`**](./results.md#ciirrun1), [**`Participants`**](./participants.md#ciir), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.ciirRun1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.ciirRun1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.ciirRun1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/ciirRun1.pdf) 

- :material-rename: **Name:** ciirRun1 
- :fontawesome-solid-user-group: **Participant:** CIIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `afd692120b840b9c6fb1f6b10badb6bc` 
- :material-text: **Run description:** Temporal query expansion model and no external evidence used.  

---
#### ciirRun2 
[**`Results`**](./results.md#ciirrun2), [**`Participants`**](./participants.md#ciir), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.ciirRun2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.ciirRun2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.ciirRun2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/ciirRun2.pdf) 

- :material-rename: **Name:** ciirRun2 
- :fontawesome-solid-user-group: **Participant:** CIIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `06ec1e105218251e1049d5da5f85b002` 
- :material-text: **Run description:** Sequential dependence model, relevance feedback model adapted and quality-biased model used.  

---
#### ciirRun3 
[**`Results`**](./results.md#ciirrun3), [**`Participants`**](./participants.md#ciir), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.ciirRun3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.ciirRun3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.ciirRun3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/ciirRun3.pdf) 

- :material-rename: **Name:** ciirRun3 
- :fontawesome-solid-user-group: **Participant:** CIIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `99f10871e3b089fc4ec4f7bd31769098` 
- :material-text: **Run description:** Based on previous best model, temporal query expansion model added 

---
#### ciirRun4 
[**`Results`**](./results.md#ciirrun4), [**`Participants`**](./participants.md#ciir), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.ciirRun4.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.ciirRun4), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.ciirRun4), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/ciirRun4.pdf) 

- :material-rename: **Name:** ciirRun4 
- :fontawesome-solid-user-group: **Participant:** CIIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `b51e30495b7e491f1703c8c4f97f9481` 
- :material-text: **Run description:** Based on previous best model, query expansion model using hashtags added 

---
#### clarity1 
[**`Results`**](./results.md#clarity1), [**`Participants`**](./participants.md#clarity_dcu), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.clarity1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.clarity1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.clarity1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/clarity1.pdf) 

- :material-rename: **Name:** clarity1 
- :fontawesome-solid-user-group: **Participant:** CLARITY_DCU 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `9ebf1c09bbe4f9039248d07cd49614d1` 
- :material-text: **Run description:** BM25 ranking algorithm with parameter set to ignore Document Length and Term Frequency (i.e. K1=0). 

---
#### clarity2 
[**`Results`**](./results.md#clarity2), [**`Participants`**](./participants.md#clarity_dcu), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.clarity2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.clarity2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.clarity2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/clarity2.pdf) 

- :material-rename: **Name:** clarity2 
- :fontawesome-solid-user-group: **Participant:** CLARITY_DCU 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `f7fe9a61ccce4e4fc4209b7c1f17a08c` 
- :material-text: **Run description:** BM25 ranking algorithm with parameter set to ignore Document Length and Term Frequency (i.e. K1=0).  Query Expansion with Pseudo Relevance Feedback using the Top N results, with N determined on a per-query basis. 

---
#### clarity3 
[**`Results`**](./results.md#clarity3), [**`Participants`**](./participants.md#clarity_dcu), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.clarity3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.clarity3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.clarity3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/clarity3.pdf) 

- :material-rename: **Name:** clarity3 
- :fontawesome-solid-user-group: **Participant:** CLARITY_DCU 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `fc88733de82b8512807ae8f5d3248a30` 
- :material-text: **Run description:** BM25 ranking algorithm with parameter set to ignore Document Length and Term Frequency (i.e. K1=0).  Query Expansion with Pseudo Relevance Feedback using the Top N results, with N determined on a per-query basis. EXTERNAL RESOURCE: Language Classifier (http://code.google.com/p/language-detection/) used to detect and remove non-English tweets. This resource is *not* timely with respect to the queries. 

---
#### clarity4 
[**`Results`**](./results.md#clarity4), [**`Participants`**](./participants.md#clarity_dcu), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.clarity4.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.clarity4), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.clarity4), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/clarity4.pdf) 

- :material-rename: **Name:** clarity4 
- :fontawesome-solid-user-group: **Participant:** CLARITY_DCU 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `34320b496e0a61ea6e15b7faa729bd1b` 
- :material-text: **Run description:** BM25 ranking algorithm with parameter set to ignore Document Length and Term Frequency (i.e. K1=0).  Query Expansion with Pseudo Relevance Feedback using the Top N results, with N determined on a per-query basis. Top N results used to estimate the temporal centre of the relevant tweets, and the scores tweets far from this temporal centre are downweighted. EXTERNAL RESOURCE: Language Classifier (http://code.google.com/p/language-detection/) used to detect and remove non-English tweets. This resource is *not* timely with respect to the queries. 

---
#### COMMITbase 
[**`Results`**](./results.md#commitbase), [**`Participants`**](./participants.md#commit), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.COMMITbase.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.COMMITbase), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.COMMITbase), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/COMMITbase.pdf) 

- :material-rename: **Name:** COMMITbase 
- :fontawesome-solid-user-group: **Participant:** COMMIT 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 7/28/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `dfac0a054ffa59ef1ab961c8886e16cd` 
- :material-text: **Run description:** Removed duplicate tweets, retweets, and tweets without links. Queries were expanded using time sensitive query expansion which considers terms from documents prior to query time. Relevant tweets were retrieved using a language modeling retrieval model. The ranked list was further curated by cutting-off at threshold relative to the retrieval scores. 

---
#### COMMITexp 
[**`Results`**](./results.md#commitexp), [**`Participants`**](./participants.md#commit), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.COMMITexp.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.COMMITexp), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.COMMITexp), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/COMMITexp.pdf) 

- :material-rename: **Name:** COMMITexp 
- :fontawesome-solid-user-group: **Participant:** COMMIT 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/5/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `04944c9b60c108902ccb1d79226bd457` 
- :material-text: **Run description:**  Removed duplicate tweets and retweets. We used learning to rank to learn the weights for a linear combination of retrieval scores of different models. The ranked list was further curated by cutting-off at threshold relative to the retrieval scores. The four models were: 1. Queries were expanded using time sensitive query expansion which considers terms from documents prior to query time. Relevant tweets were retrieved using a language modeling retrieval model (retrieval model of our baseline). 2. A language modeling retrieval model 3. Boolean matching 4. We used a wikipedia-based Semantic Query Expansion (SQM). The tweets were then retrieved using a language modeling retrieval model. This model uses external data. 

---
#### COMMITfilter 
[**`Results`**](./results.md#commitfilter), [**`Participants`**](./participants.md#commit), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.COMMITfilter.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.COMMITfilter), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.COMMITfilter), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/COMMITfilter.pdf) 

- :material-rename: **Name:** COMMITfilter 
- :fontawesome-solid-user-group: **Participant:** COMMIT 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/5/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `41ffecf8e6d801b7342dc1edde0f028e` 
- :material-text: **Run description:** This approach uses pre-filtering potentially relevant tweets using a manually annotated trainingset. We trained a random forest on query-dependent (e.g.: HITS authority and hubs) and query-independent (e.g.: friends, capitalisation, number of links) features. The prediction value of the random forest served as filtering value. We then used learning to rank to learn the weights for a linear combination of retrieval scores of different models. The ranked list was further curated by cutting-off at threshold relative to the retrieval scores. The six models were: Queries were expanded using time sensitive query expansion which considers terms from documents prior to query time. Relevant tweets were retrieved using a language modeling retrieval model (retrieval model of our baseline). A language modeling retrieval model Boolean matching We used a wikipedia-based Semantic Query Expansion (SQM). The tweets were then retrieved using a language modeling retrieval model. This model uses external data. We also retrieved links. We built a corpus of web documents that were linked in tweets and used a language modeling retrieval model. We mapped the links back to the tweets. This model uses external data. We use SQM for the link retrieval setting. This model uses external data. 

---
#### COMMITlinks 
[**`Results`**](./results.md#commitlinks), [**`Participants`**](./participants.md#commit), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.COMMITlinks.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.COMMITlinks), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.COMMITlinks), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/COMMITlinks.pdf) 

- :material-rename: **Name:** COMMITlinks 
- :fontawesome-solid-user-group: **Participant:** COMMIT 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/5/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `c36d91135d325bb2f39f7dfd7bb2eadf` 
- :material-text: **Run description:** We used learning to rank to learn the weights for a linear combination of retrieval scores of different models. The ranked list was further curated by cutting-off at threshold relative to the retrieval scores. The six models were: Queries were expanded using time sensitive query expansion which considers terms from documents prior to query time. Relevant tweets were retrieved using a language modeling retrieval model (retrieval model of our baseline). A language modeling retrieval model Boolean matching We used a wikipedia-based Semantic Query Expansion (SQM). The tweets were then retrieved using a language modeling retrieval model. This model uses external data. We also retrieved links. We built a corpus of web documents that were linked in tweets and used a language modeling retrieval model. We mapped the links back to the tweets. This model uses external data. We use SQM for the link retrieval setting. This model uses external data. 

---
#### cyfrun1 
[**`Results`**](./results.md#cyfrun1), [**`Participants`**](./participants.md#ucsc), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.cyfrun1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.cyfrun1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.cyfrun1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/cyfrun1.pdf) 

- :material-rename: **Name:** cyfrun1 
- :fontawesome-solid-user-group: **Participant:** UCSC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `b0f776e40c437fff031b9c4b6fff363a` 
- :material-text: **Run description:** sum of query word IDF,  tf score of tweet,  

---
#### cyfrun2 
[**`Results`**](./results.md#cyfrun2), [**`Participants`**](./participants.md#ucsc), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.cyfrun2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.cyfrun2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.cyfrun2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/cyfrun2.pdf) 

- :material-rename: **Name:** cyfrun2 
- :fontawesome-solid-user-group: **Participant:** UCSC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `73e8485d949cfd5eaed54e6c796575c1` 
- :material-text: **Run description:** tf score of tweet,  

---
#### dbpWISTUD 
[**`Results`**](./results.md#dbpwistud), [**`Participants`**](./participants.md#wis_tudelft), [**`Proceedings`**](./proceedings.md#wistud-at-trec-2011-microblog-track-exploiting-background-knowledge-from-dbpedia-and-news-articles-for-search-on-twitter), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.dbpWISTUD.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.dbpWISTUD), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.dbpWISTUD), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/dbpWISTUD.pdf) 

- :material-rename: **Name:** dbpWISTUD 
- :fontawesome-solid-user-group: **Participant:** wis_tudelft 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `09f2aced5cd4599f891a29604bf04c39` 
- :material-text: **Run description:** 1. dbpedia 3.6 dump version 2011-01-17 

---
#### DFReeKLIM 
[**`Results`**](./results.md#dfreeklim), [**`Participants`**](./participants.md#fub), [**`Proceedings`**](./proceedings.md#fub-iasi-cnr-univaq-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.DFReeKLIM.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.DFReeKLIM), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.DFReeKLIM), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/DFReeKLIM.pdf) 

- :material-rename: **Name:** DFReeKLIM 
- :fontawesome-solid-user-group: **Participant:** FUB 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `5745b2ccc4db35d97c58511b842165b9` 
- :material-text: **Run description:** Baseline. Built using a new retrieval model and pseudo relevance feedback QE. 

---
#### DFReeKLIM30 
[**`Results`**](./results.md#dfreeklim30), [**`Participants`**](./participants.md#fub), [**`Proceedings`**](./proceedings.md#fub-iasi-cnr-univaq-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.DFReeKLIM30.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.DFReeKLIM30), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.DFReeKLIM30), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/DFReeKLIM30.pdf) 

- :material-rename: **Name:** DFReeKLIM30 
- :fontawesome-solid-user-group: **Participant:** FUB 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `94e778d61c8a29b00d5ae65aae570ee5` 
- :material-text: **Run description:** Baseline. Built using a new retrieval model and pseudo relevance feedback QE. We fix the result list size to 30. 

---
#### DFReeKLIMDC 
[**`Results`**](./results.md#dfreeklimdc), [**`Participants`**](./participants.md#fub), [**`Proceedings`**](./proceedings.md#fub-iasi-cnr-univaq-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.DFReeKLIMDC.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.DFReeKLIMDC), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.DFReeKLIMDC), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/DFReeKLIMDC.pdf) 

- :material-rename: **Name:** DFReeKLIMDC 
- :fontawesome-solid-user-group: **Participant:** FUB 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `c53f041a475ebdb1c9537b5d1c1ce03e` 
- :material-text: **Run description:** Baseline. Built using a new retrieval model and pseudo relevance feedback QE. We use a heuristic approach to determine the result list size, for each query separately. 

---
#### DFReeKLIMRA 
[**`Results`**](./results.md#dfreeklimra), [**`Participants`**](./participants.md#fub), [**`Proceedings`**](./proceedings.md#fub-iasi-cnr-univaq-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.DFReeKLIMRA.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.DFReeKLIMRA), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.DFReeKLIMRA), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/DFReeKLIMRA.pdf) 

- :material-rename: **Name:** DFReeKLIMRA 
- :fontawesome-solid-user-group: **Participant:** FUB 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `73d9f244335e2054cab1117cb637f15d` 
- :material-text: **Run description:** Built using a new retrieval model and pseudo relevance feedback QE. We also apply a re-ranking technique to deal with both, recency and relevance. We further use a heuristic approach to determine the result list size, for each query separately. 

---
#### dutirLmFb 
[**`Results`**](./results.md#dutirlmfb), [**`Participants`**](./participants.md#dutir), [**`Proceedings`**](./proceedings.md#dutir-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.dutirLmFb.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.dutirLmFb), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.dutirLmFb), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/dutirLmFb.pdf) 

- :material-rename: **Name:** dutirLmFb 
- :fontawesome-solid-user-group: **Participant:** DUTIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `87b2af7d0d3d0c19a9da1c9d5abcb282` 
- :material-text: **Run description:** language model, feedback, entropy, whether exist link 

---
#### dutirMixFb 
[**`Results`**](./results.md#dutirmixfb), [**`Participants`**](./participants.md#dutir), [**`Proceedings`**](./proceedings.md#dutir-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.dutirMixFb.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.dutirMixFb), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.dutirMixFb), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/dutirMixFb.pdf) 

- :material-rename: **Name:** dutirMixFb 
- :fontawesome-solid-user-group: **Participant:** DUTIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `43fcddf53dd458e68296bf09eb28b16d` 
- :material-text: **Run description:** max of language model and tf*idf, feedback, entropy, whether exist link 

---
#### dutirMixSp 
[**`Results`**](./results.md#dutirmixsp), [**`Participants`**](./participants.md#dutir), [**`Proceedings`**](./proceedings.md#dutir-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.dutirMixSp.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.dutirMixSp), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.dutirMixSp), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/dutirMixSp.pdf) 

- :material-rename: **Name:** dutirMixSp 
- :fontawesome-solid-user-group: **Participant:** DUTIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `edcbbeb332a4b74fc357e924d32d379a` 
- :material-text: **Run description:** mixture of language model and tf*idf,  entropy, whether exist link 

---
#### dutirTfidfFb 
[**`Results`**](./results.md#dutirtfidffb), [**`Participants`**](./participants.md#dutir), [**`Proceedings`**](./proceedings.md#dutir-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.dutirTfidfFb.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.dutirTfidfFb), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.dutirTfidfFb), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/dutirTfidfFb.pdf) 

- :material-rename: **Name:** dutirTfidfFb 
- :fontawesome-solid-user-group: **Participant:** DUTIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `141b50f5f88f32f5c55d4d0cd98f6f5b` 
- :material-text: **Run description:** tf*idf, feedback, entropy, whether exist link 

---
#### EMAX 
[**`Results`**](./results.md#emax), [**`Participants`**](./participants.md#tud_dmir), [**`Proceedings`**](./proceedings.md#dmir-on-microblog-track-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.EMAX.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.EMAX), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.EMAX), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/EMAX.pdf) 

- :material-rename: **Name:** EMAX 
- :fontawesome-solid-user-group: **Participant:** TUD_DMIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `37f657bb58239dbc35f7e8696305db38` 
- :material-text: **Run description:** The index for the query MB007 is polluted, while other queries are conducted under the strict realtime condition. The scoring method is only based on information (Entropy) provided by tweets. 

---
#### FASILKOM01 
[**`Results`**](./results.md#fasilkom01), [**`Participants`**](./participants.md#fasilkomui), [**`Proceedings`**](./proceedings.md#university-of-indonesia-at-trec-2011-microblog-task), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.FASILKOM01.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.FASILKOM01), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.FASILKOM01), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/FASILKOM01.pdf) 

- :material-rename: **Name:** FASILKOM01 
- :fontawesome-solid-user-group: **Participant:** FASILKOMUI 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `71cc79ab9ebfc080410ea7b090a56c16` 
- :material-text: **Run description:** This run does not include any future evidence and external resource. 

---
#### FASILKOM02 
[**`Results`**](./results.md#fasilkom02), [**`Participants`**](./participants.md#fasilkomui), [**`Proceedings`**](./proceedings.md#university-of-indonesia-at-trec-2011-microblog-task), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.FASILKOM02.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.FASILKOM02), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.FASILKOM02), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/FASILKOM02.pdf) 

- :material-rename: **Name:** FASILKOM02 
- :fontawesome-solid-user-group: **Participant:** FASILKOMUI 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `8f47b67721351ebfef78d4ec54fcd133` 
- :material-text: **Run description:** This run uses phrase query identification (using POS tagger), query expansion (from Google and the Twitter dataset), customized scoring function.  

---
#### FASILKOM03 
[**`Results`**](./results.md#fasilkom03), [**`Participants`**](./participants.md#fasilkomui), [**`Proceedings`**](./proceedings.md#university-of-indonesia-at-trec-2011-microblog-task), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.FASILKOM03.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.FASILKOM03), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.FASILKOM03), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/FASILKOM03.pdf) 

- :material-rename: **Name:** FASILKOM03 
- :fontawesome-solid-user-group: **Participant:** FASILKOMUI 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `2e0a7c807a0cdf99493dad950fbf8326` 
- :material-text: **Run description:** This run uses phrase query identification (using POS Tagger), query expansion which is generated from the dataset, and customized scoring function.  

---
#### FASILKOM04 
[**`Results`**](./results.md#fasilkom04), [**`Participants`**](./participants.md#fasilkomui), [**`Proceedings`**](./proceedings.md#university-of-indonesia-at-trec-2011-microblog-task), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.FASILKOM04.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.FASILKOM04), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.FASILKOM04), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/FASILKOM04.pdf) 

- :material-rename: **Name:** FASILKOM04 
- :fontawesome-solid-user-group: **Participant:** FASILKOMUI 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `e60ea9f35a435c7aa66810c78889ff3a` 
- :material-text: **Run description:** This run uses phrase query identification (using POS Tagger), query expansion which is generated from  Google search results, and customized scoring function.  

---
#### FDUNLP 
[**`Results`**](./results.md#fdunlp), [**`Participants`**](./participants.md#fdumed), [**`Proceedings`**](./proceedings.md#microblog-track-2011-of-fdu), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.FDUNLP.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.FDUNLP), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.FDUNLP), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/FDUNLP.pdf) 

- :material-rename: **Name:** FDUNLP 
- :fontawesome-solid-user-group: **Participant:** FDUMED 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `84f7f40f41e38d46e8f6ae7d1d836735` 
- :material-text: **Run description:** Strictly real time, heauristic approach to identify the language of the tweet. Each tweet is given 2 features, and finally all the tweets are clustered. 

---
#### FDUNLP2 
[**`Results`**](./results.md#fdunlp2), [**`Participants`**](./participants.md#fdumed), [**`Proceedings`**](./proceedings.md#microblog-track-2011-of-fdu), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.FDUNLP2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.FDUNLP2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.FDUNLP2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/FDUNLP2.pdf) 

- :material-rename: **Name:** FDUNLP2 
- :fontawesome-solid-user-group: **Participant:** FDUMED 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `90c4ca007596e45b949e254f6e691302` 
- :material-text: **Run description:** Strictly real time, with a fine tuned tool to identify the language of the tweet. Each tweet is given 2 features, and finally all the tweets are clustered. 

---
#### Google1GNO 
[**`Results`**](./results.md#google1gno), [**`Participants`**](./participants.md#irsi), [**`Proceedings`**](./proceedings.md#query-expansion-for-microblog-retrieval), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.Google1GNO.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.Google1GNO), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.Google1GNO), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/Google1GNO.pdf) 

- :material-rename: **Name:** Google1GNO 
- :fontawesome-solid-user-group: **Participant:** IRSI 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `cc42b20e843c53fb75f10c690c8366ba` 
- :material-text: **Run description:** The given queries were searched using Google Search API. Word wise 1-grams of the titles of all the pages returned by Google were sorted in the descending order by their frequencies. Top 5 1-grams were used as new topic (the original topics were not added)and retrieval was done using Terrier-3.5 with these new topics. 

---
#### gus 
[**`Results`**](./results.md#gus), [**`Participants`**](./participants.md#gslisuiuc), [**`Proceedings`**](./proceedings.md#the-university-of-illinois-graduate-school-of-library-and-information-science-at-trec-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.gus.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.gus), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.gus), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/gus.pdf) 

- :material-rename: **Name:** gus 
- :fontawesome-solid-user-group: **Participant:** gslisUIUC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `b322f122a6ef9a4bc12088e08e224019` 
- :material-text: **Run description:** This run uses no external or future evidence.  It is a variant of the temporal smoothing method described in Efron and Golovchinsky (2011)--a language modeling variant (with no forward-looking corpus stats). No document priors are used. 

---
#### gust 
[**`Results`**](./results.md#gust), [**`Participants`**](./participants.md#gslisuiuc), [**`Proceedings`**](./proceedings.md#the-university-of-illinois-graduate-school-of-library-and-information-science-at-trec-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.gust.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.gust), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.gust), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/gust.pdf) 

- :material-rename: **Name:** gust 
- :fontawesome-solid-user-group: **Participant:** gslisUIUC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `44fed9a322a7525f7c0207a17c1080f5` 
- :material-text: **Run description:** This run uses no external or future evidence.  It is a variant of the temporal smoothing method described in Efron and Golovchinsky (2011)--a language modeling variant (with no forward-looking corpus stats). The run uses a "temporal" document prior.  That is, the prior is estimated by judging the fit of the document's pseudo-query against an exponential distribution. 

---
#### gustc 
[**`Results`**](./results.md#gustc), [**`Participants`**](./participants.md#gslisuiuc), [**`Proceedings`**](./proceedings.md#the-university-of-illinois-graduate-school-of-library-and-information-science-at-trec-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.gustc.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.gustc), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.gustc), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/gustc.pdf) 

- :material-rename: **Name:** gustc 
- :fontawesome-solid-user-group: **Participant:** gslisUIUC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `a5bdf6b28e82395058dd5c2de6f677a3` 
- :material-text: **Run description:** This run uses no external or future evidence.  It is a variant of the temporal smoothing method described in Efron and Golovchinsky (2011)--a language modeling variant (with no forward-looking corpus stats). The run uses a "temporal" document prior.  That is, the prior is estimated by judging the fit of the document's pseudo-query against an exponential distribution. Also uses a second prior based on the clustering coefficient of the graph of words in a relevance model induced from the document's pseudo query. 

---
#### gut 
[**`Results`**](./results.md#gut), [**`Participants`**](./participants.md#gslisuiuc), [**`Proceedings`**](./proceedings.md#the-university-of-illinois-graduate-school-of-library-and-information-science-at-trec-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.gut.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.gut), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.gut), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/gut.pdf) 

- :material-rename: **Name:** gut 
- :fontawesome-solid-user-group: **Participant:** gslisUIUC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `c811a00053f4cc72dad873637782bb65` 
- :material-text: **Run description:** This run uses no external or future evidence.   It uses a query likelihood model (with no forward-looking corpus smoothing) supplemented with an independent evidence source based on the likelihood that the temporal profile of the document's pseudo-query also generated the temporal profile of the query.  

---
#### hitWId 
[**`Results`**](./results.md#hitwid), [**`Participants`**](./participants.md#hit_ltrc), [**`Proceedings`**](./proceedings.md#hit-ltrc-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.hitWId.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.hitWId), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.hitWId), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/hitWId.pdf) 

- :material-rename: **Name:** hitWId 
- :fontawesome-solid-user-group: **Participant:** HIT_LTRC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `a7e2b76aab0aec88da2fcf99400e104b` 
- :material-text: **Run description:** This run aims to test the effectiveness of score decay. 

---
#### hitWIt 
[**`Results`**](./results.md#hitwit), [**`Participants`**](./participants.md#hit_ltrc), [**`Proceedings`**](./proceedings.md#hit-ltrc-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.hitWIt.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.hitWIt), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.hitWIt), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/hitWIt.pdf) 

- :material-rename: **Name:** hitWIt 
- :fontawesome-solid-user-group: **Participant:** HIT_LTRC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `70f705b120725eb40d4f13f75bcdba57` 
- :material-text: **Run description:** This run focused on automatic threshold selection. 

---
#### ICTNET11MBR1 
[**`Results`**](./results.md#ictnet11mbr1), [**`Participants`**](./participants.md#ictnet), [**`Proceedings`**](./proceedings.md#ictnet-at-microblog-track-trec-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.ICTNET11MBR1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.ICTNET11MBR1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.ICTNET11MBR1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/ICTNET11MBR1.pdf) 

- :material-rename: **Name:** ICTNET11MBR1 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `5c0837b7adb9dfaeac20d2b7d1c5b7e6` 
- :material-text: **Run description:** we run the result with 6 features, including the enhanced BM25 weight, length, freshness,hashtag hits, user activeness. we do the query extention as well, except misspell extention.  As for this run, by developping a semi-supervising algorithm, we extend query within the content of those tweets before the query time. There is no external and future information being used. 

---
#### ICTNET11MBR2 
[**`Results`**](./results.md#ictnet11mbr2), [**`Participants`**](./participants.md#ictnet), [**`Proceedings`**](./proceedings.md#ictnet-at-microblog-track-trec-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.ICTNET11MBR2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.ICTNET11MBR2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.ICTNET11MBR2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/ICTNET11MBR2.pdf) 

- :material-rename: **Name:** ICTNET11MBR2 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `ab11a48d0a3a9fcf3cf0b0f61df16524` 
- :material-text: **Run description:** we run the result with 6 features, including the enhanced BM25 weight, length, freshness, hashtag hits, user activeness. we do the query extention as well, except misspell extention. As for this run, we used the same query extension with ICTNET11MBR1, and the different enhanced BM25 

---
#### ICTNET11MBR3 
[**`Results`**](./results.md#ictnet11mbr3), [**`Participants`**](./participants.md#ictnet), [**`Proceedings`**](./proceedings.md#ictnet-at-microblog-track-trec-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.ICTNET11MBR3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.ICTNET11MBR3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.ICTNET11MBR3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/ICTNET11MBR3.pdf) 

- :material-rename: **Name:** ICTNET11MBR3 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `98142713c2f4ca34cfe77cad7d008ff9` 
- :material-text: **Run description:** we run the result with 6 features, including the enhanced BM25 weight, length, freshness, hashtag hits, user activeness. we do the query extention as well, except misspell extention. As for this run, we extend query with the external information by google meta search technique. Meanwhile, some wiki articles are included as a complement. There is no future information being used. 

---
#### ICTNET11MBR4 
[**`Results`**](./results.md#ictnet11mbr4), [**`Participants`**](./participants.md#ictnet), [**`Proceedings`**](./proceedings.md#ictnet-at-microblog-track-trec-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.ICTNET11MBR4.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.ICTNET11MBR4), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.ICTNET11MBR4), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/ICTNET11MBR4.pdf) 

- :material-rename: **Name:** ICTNET11MBR4 
- :fontawesome-solid-user-group: **Participant:** ICTNET 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `8cd46d79e2d80acbeab42a36518a0ac7` 
- :material-text: **Run description:** we run the result with 6 features, including the enhanced BM25 weight, length, freshness, hashtag hits, user activeness. we do the query extention as well, except misspell extention. As for this run, we extend the query within all the available tweets collection. And the external extension from ICTNET11MBR3 are combined together. Thus we use both external and future informaiton in this run. 

---
#### IDEAACTQE 
[**`Results`**](./results.md#ideaactqe), [**`Participants`**](./participants.md#gucas), [**`Proceedings`**](./proceedings.md#gucas-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.IDEAACTQE.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.IDEAACTQE), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.IDEAACTQE), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/IDEAACTQE.pdf) 

- :material-rename: **Name:** IDEAACTQE 
- :fontawesome-solid-user-group: **Participant:** GUCAS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `f39fd9a63bbb96a4f6101d2f460f51c0` 
- :material-text: **Run description:** A query expand run using content,authority and time based on field-based retrieval model 

---
#### IDEABASIC 
[**`Results`**](./results.md#ideabasic), [**`Participants`**](./participants.md#gucas), [**`Proceedings`**](./proceedings.md#gucas-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.IDEABASIC.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.IDEABASIC), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.IDEABASIC), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/IDEABASIC.pdf) 

- :material-rename: **Name:** IDEABASIC 
- :fontawesome-solid-user-group: **Participant:** GUCAS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `72b2a47cec7d7bf3d87afa63d103c0d7` 
- :material-text: **Run description:** A baseline run using field-based retrieval model 

---
#### IDEABASICACT 
[**`Results`**](./results.md#ideabasicact), [**`Participants`**](./participants.md#gucas), [**`Proceedings`**](./proceedings.md#gucas-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.IDEABASICACT.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.IDEABASICACT), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.IDEABASICACT), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/IDEABASICACT.pdf) 

- :material-rename: **Name:** IDEABASICACT 
- :fontawesome-solid-user-group: **Participant:** GUCAS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `b22c690fb69ceaddf7996093a476af0e` 
- :material-text: **Run description:** A  basic run using content,authority and time based on field-based retrieval model 

---
#### IDEABASICQE 
[**`Results`**](./results.md#ideabasicqe), [**`Participants`**](./participants.md#gucas), [**`Proceedings`**](./proceedings.md#gucas-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.IDEABASICQE.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.IDEABASICQE), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.IDEABASICQE), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/IDEABASICQE.pdf) 

- :material-rename: **Name:** IDEABASICQE 
- :fontawesome-solid-user-group: **Participant:** GUCAS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `108280222fc6c04707b72857694aaeac` 
- :material-text: **Run description:** A query expand run using field-based retrieval model 

---
#### ikmRun1 
[**`Results`**](./results.md#ikmrun1), [**`Participants`**](./participants.md#ikm101), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.ikmRun1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.ikmRun1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.ikmRun1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/ikmRun1.pdf) 

- :material-rename: **Name:** ikmRun1 
- :fontawesome-solid-user-group: **Participant:** ikm101 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `6f5bf6f36b5f3dc578bd67565e90f8f8` 
- :material-text: **Run description:** We use information from link 

---
#### InL2c1 
[**`Results`**](./results.md#inl2c1), [**`Participants`**](./participants.md#irsi), [**`Proceedings`**](./proceedings.md#query-expansion-for-microblog-retrieval), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.InL2c1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.InL2c1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.InL2c1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/InL2c1.pdf) 

- :material-rename: **Name:** InL2c1 
- :fontawesome-solid-user-group: **Participant:** IRSI 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `e4d60cb5d2bac0c2d970b3f27ad424ce` 
- :material-text: **Run description:** The retrieval was done using original queries by terrier-3.5. 

---
#### iritfd1 
[**`Results`**](./results.md#iritfd1), [**`Participants`**](./participants.md#irit_sig), [**`Proceedings`**](./proceedings.md#irit-at-trec-microblog-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.iritfd1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.iritfd1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.iritfd1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/iritfd1.pdf) 

- :material-rename: **Name:** iritfd1 
- :fontawesome-solid-user-group: **Participant:** IRIT_SIG 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/9/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `586e236e16a4c2a275017f6f2564cc21` 
- :material-text: **Run description:** This run combines the score of Lucene search engine with a set of features’ scores:  Popularity of the tweet, Length of the tweet, exact term matching, Presence of a URL, Frequency of URL, Hashtag score, Number of tweet for a twitterer, Number of mentions for a twitterer. Queries were expanded with keyword from news articles published before timestamp.  

---
#### iritfd2 
[**`Results`**](./results.md#iritfd2), [**`Participants`**](./participants.md#irit_sig), [**`Proceedings`**](./proceedings.md#irit-at-trec-microblog-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.iritfd2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.iritfd2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.iritfd2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/iritfd2.pdf) 

- :material-rename: **Name:** iritfd2 
- :fontawesome-solid-user-group: **Participant:** IRIT_SIG 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/9/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `713df52d4cce2be1d2ee167538b5d819` 
- :material-text: **Run description:** This run combines the score of Lucene search engine with a set of features’ scores:  Popularity of the tweet, Length of the tweet, exact term matching, Presence of a URL, Frequency of URL, Hashtag score, Number of tweet for a twitterer, Number of mentions for a twitterer. 

---
#### IRSIGoogle1G 
[**`Results`**](./results.md#irsigoogle1g), [**`Participants`**](./participants.md#irsi), [**`Proceedings`**](./proceedings.md#query-expansion-for-microblog-retrieval), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.IRSIGoogle1G.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.IRSIGoogle1G), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.IRSIGoogle1G), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/IRSIGoogle1G.pdf) 

- :material-rename: **Name:** IRSIGoogle1G 
- :fontawesome-solid-user-group: **Participant:** IRSI 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `6a3914edd79c1533f3422c8e7b554ad7` 
- :material-text: **Run description:** The given queries were searched using Google Search API. Word wise 1-grams of the titles of all the pages returned by Google were sorted in the descending order by their frequencies. Top 5 1-grams were added to the original topics and retrieval was done using Terrier-3.5 with these new topics. 

---
#### IRSIGoogle2G 
[**`Results`**](./results.md#irsigoogle2g), [**`Participants`**](./participants.md#irsi), [**`Proceedings`**](./proceedings.md#query-expansion-for-microblog-retrieval), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.IRSIGoogle2G.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.IRSIGoogle2G), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.IRSIGoogle2G), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/IRSIGoogle2G.pdf) 

- :material-rename: **Name:** IRSIGoogle2G 
- :fontawesome-solid-user-group: **Participant:** IRSI 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `5fcdaa84a0b293215226f3f67707141c` 
- :material-text: **Run description:** The given queries were searched using Google Search API. Word wise 2-grams of the titles of all the pages returned by Google were sorted in the descending order by their frequencies. Top 5 2-grams were added to the original topics and retrieval was done using Terrier-3.5 with these new topics. 

---
#### isiFD 
[**`Results`**](./results.md#isifd), [**`Participants`**](./participants.md#isi), [**`Proceedings`**](./proceedings.md#usc-isi-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.isiFD.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.isiFD), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.isiFD), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/isiFD.pdf) 

- :material-rename: **Name:** isiFD 
- :fontawesome-solid-user-group: **Participant:** isi 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `14d026d65861123bcc77ce3598bf1e11` 
- :material-text: **Run description:** Basic keyword search using "full dependence" variant of MRF retrieval model. 

---
#### isiFDL 
[**`Results`**](./results.md#isifdl), [**`Participants`**](./participants.md#isi), [**`Proceedings`**](./proceedings.md#usc-isi-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.isiFDL.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.isiFDL), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.isiFDL), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/isiFDL.pdf) 

- :material-rename: **Name:** isiFDL 
- :fontawesome-solid-user-group: **Participant:** isi 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `01752e408ca034471f1ff97606380e83` 
- :material-text: **Run description:** Learning to rank model [base ranking function = "full dependence" variant of the MRF model]. 

---
#### isiFDRM 
[**`Results`**](./results.md#isifdrm), [**`Participants`**](./participants.md#isi), [**`Proceedings`**](./proceedings.md#usc-isi-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.isiFDRM.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.isiFDRM), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.isiFDRM), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/isiFDRM.pdf) 

- :material-rename: **Name:** isiFDRM 
- :fontawesome-solid-user-group: **Participant:** isi 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `2d923f243a6f7b7aeb620d55a3e6afe1` 
- :material-text: **Run description:** "Full dependence" variant of the MRF model + pseudo relevance feedback. 

---
#### isiFDRML 
[**`Results`**](./results.md#isifdrml), [**`Participants`**](./participants.md#isi), [**`Proceedings`**](./proceedings.md#usc-isi-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.isiFDRML.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.isiFDRML), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.isiFDRML), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/isiFDRML.pdf) 

- :material-rename: **Name:** isiFDRML 
- :fontawesome-solid-user-group: **Participant:** isi 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `3f6d5e58dbbe9eb02fc92c0ac41af198` 
- :material-text: **Run description:** Learning to rank model [base ranking function = "full dependence" variant of the MRF model + pseudo relevance feedback]. 

---
#### kanopeRun 
[**`Results`**](./results.md#kanoperun), [**`Participants`**](./participants.md#kanopereunion), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.kanopeRun.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.kanopeRun), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.kanopeRun), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/kanopeRun.pdf) 

- :material-rename: **Name:** kanopeRun 
- :fontawesome-solid-user-group: **Participant:** KanopeReunion 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `7183078cb4d6eaaa3e0f09b8f3627e12` 
- :material-text: **Run description:**  Our approach merged (i) an indicator of semantic similarity, approximated using the Reflexing Random Indexing (RRI)(Cohen, Schvaneveldt & Widdows, 2010) semantic space model, with (ii) the chronological distance separating tweets from a given query. RRI is a semantic space model that as demonstrated as good performances as LSA or LDA, but using a mathematical approach of the distributional hypothesis which is based on random projection. This point makes RRI very efficient in terms of computational resources that seems particularly attractive considering the large amount of data from social media. 

---
#### KAUSTBase 
[**`Results`**](./results.md#kaustbase), [**`Participants`**](./participants.md#kaust), [**`Proceedings`**](./proceedings.md#best-of-kaust-at-trec-2011-building-effective-search-in-twitter), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.KAUSTBase.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.KAUSTBase), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.KAUSTBase), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/KAUSTBase.pdf) 

- :material-rename: **Name:** KAUSTBase 
- :fontawesome-solid-user-group: **Participant:** KAUST 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `e71412ef748c91258605008067cacda6` 
- :material-text: **Run description:** Baseline run: - No external or future evidence is used. - Preprocessing: detecting spam users and spam-tweets and also non-English tweets. - Tweets are ranked by content similarity (using IDF) and recency. 

---
#### KAUSTExp 
[**`Results`**](./results.md#kaustexp), [**`Participants`**](./participants.md#kaust), [**`Proceedings`**](./proceedings.md#best-of-kaust-at-trec-2011-building-effective-search-in-twitter), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.KAUSTExp.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.KAUSTExp), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.KAUSTExp), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/KAUSTExp.pdf) 

- :material-rename: **Name:** KAUSTExp 
- :fontawesome-solid-user-group: **Participant:** KAUST 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `5c9d969495878a9335ce81c06cef91f3` 
- :material-text: **Run description:** Expansion without rerank run: - No external or future evidence is used. - Preprocessing: detecting spam users and spam-tweets and also non-English tweets. - Tweet expansion: expanded URLs and hashtags with most-frequent co-occurring terms. Expansion terms are added to the tweets at indexing time. - Tweets are ranked by content similarity (using IDF) and recency. 

---
#### KAUSTExpRrnk 
[**`Results`**](./results.md#kaustexprrnk), [**`Participants`**](./participants.md#kaust), [**`Proceedings`**](./proceedings.md#best-of-kaust-at-trec-2011-building-effective-search-in-twitter), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.KAUSTExpRrnk.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.KAUSTExpRrnk), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.KAUSTExpRrnk), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/KAUSTExpRrnk.pdf) 

- :material-rename: **Name:** KAUSTExpRrnk 
- :fontawesome-solid-user-group: **Participant:** KAUST 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `de700fe8b67550de607605463067f7fa` 
- :material-text: **Run description:** Expansion with rerank run: - No external or future evidence is used. - Preprocessing: detecting spam users and spam-tweets and also non-English tweets. - Tweet expansion: expanded URLs and hashtags with most-frequent co-occurring terms. Expansion terms are added to the tweets at indexing time. - Computed an estimation of user topic authority by building user's term-profile. - Computed an estimation of user popularity based on frequency of being replied-to, mentioned, and retweeted. - Tweets are ranked first by content similarity (using IDF) and recency. Then 4 other features are used to rerank: retweet frequency of a tweet, frequency of URL (if exist), estimated user popularity, and estimated user topic-authority. 

---
#### KAUSTRerank 
[**`Results`**](./results.md#kaustrerank), [**`Participants`**](./participants.md#kaust), [**`Proceedings`**](./proceedings.md#best-of-kaust-at-trec-2011-building-effective-search-in-twitter), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.KAUSTRerank.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.KAUSTRerank), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.KAUSTRerank), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/KAUSTRerank.pdf) 

- :material-rename: **Name:** KAUSTRerank 
- :fontawesome-solid-user-group: **Participant:** KAUST 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `e4e36171200802841c4ab4152de9b6e9` 
- :material-text: **Run description:** Rerank without expansion run: - No external or future evidence is used. - Preprocessing: detecting spam users and spam-tweets and also non-English tweets. - Computed an estimation of user topic authority by building user's term-profile. - Computed an estimation of user popularity based on frequency of being replied-to, mentioned, and retweeted. - Tweets are ranked first by content similarity (using IDF) and recency. Then 4 other features are used to rerank: retweet frequency of a tweet, frequency of URL (if exist), estimated user popularity, and estimated user topic-authority. 

---
#### LJQO10 
[**`Results`**](./results.md#ljqo10), [**`Participants`**](./participants.md#polyu), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.LJQO10.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.LJQO10), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.LJQO10), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/LJQO10.pdf) 

- :material-rename: **Name:** LJQO10 
- :fontawesome-solid-user-group: **Participant:** PolyU 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `99b14a6ad47ea00b77ee2d8d6c9bba26` 
- :material-text: **Run description:** Only use query without any external or future information. 

---
#### LJQO5 
[**`Results`**](./results.md#ljqo5), [**`Participants`**](./participants.md#polyu), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.LJQO5.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.LJQO5), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.LJQO5), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/LJQO5.pdf) 

- :material-rename: **Name:** LJQO5 
- :fontawesome-solid-user-group: **Participant:** PolyU 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `5d9510a4dfa98530c0f92d01c5e55f94` 
- :material-text: **Run description:** Only use query without any external or future information. 

---
#### LMOP10 
[**`Results`**](./results.md#lmop10), [**`Participants`**](./participants.md#polyu), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.LMOP10.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.LMOP10), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.LMOP10), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/LMOP10.pdf) 

- :material-rename: **Name:** LMOP10 
- :fontawesome-solid-user-group: **Participant:** PolyU 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `b6ddc9331327f12c2dbb438e1c4cd0b5` 
- :material-text: **Run description:** Only use query without any external or future information. 

---
#### LMOP5 
[**`Results`**](./results.md#lmop5), [**`Participants`**](./participants.md#polyu), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.LMOP5.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.LMOP5), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.LMOP5), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/LMOP5.pdf) 

- :material-rename: **Name:** LMOP5 
- :fontawesome-solid-user-group: **Participant:** PolyU 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `7dddb79e0139c717497bbb58107d98c4` 
- :material-text: **Run description:** Only use query without any external or future information. 

---
#### LThresh 
[**`Results`**](./results.md#lthresh), [**`Participants`**](./participants.md#syles), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.LThresh.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.LThresh), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.LThresh), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/LThresh.pdf) 

- :material-rename: **Name:** LThresh 
- :fontawesome-solid-user-group: **Participant:** syles 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `9135eceadc69c22f8987b19c1534cbbe` 
- :material-text: **Run description:** - Language identifier trained on Wikipedia 

---
#### manualWISTUD 
[**`Results`**](./results.md#manualwistud), [**`Participants`**](./participants.md#wis_tudelft), [**`Proceedings`**](./proceedings.md#wistud-at-trec-2011-microblog-track-exploiting-background-knowledge-from-dbpedia-and-news-articles-for-search-on-twitter), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.manualWISTUD.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.manualWISTUD), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.manualWISTUD), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/manualWISTUD.pdf) 

- :material-rename: **Name:** manualWISTUD 
- :fontawesome-solid-user-group: **Participant:** wis_tudelft 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 7/12/2011 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `4f2323f91c7ed055d74a589800b39413` 
- :material-text: **Run description:** An assessor manually searched through the corpus (filtered by language automatically; English only) and located interesting tweets. Allowed time per topic: 5 minutes.  To increase the number of tweets retrieved per topic, a single query was submitted at the end of the 5 minute interval and all tweets returned with a tweetid lower than the lowest manually retrieved tweet were appended to the list.  No other external sources were used: the context/circumstances topics were learnt by the assessor while assessing the tweets. 

---
#### melblt 
[**`Results`**](./results.md#melblt), [**`Participants`**](./participants.md#unimelblt), [**`Proceedings`**](./proceedings.md#melbourne-language-group-microblog-track-report), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.melblt.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.melblt), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.melblt), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/melblt.pdf) 

- :material-rename: **Name:** melblt 
- :fontawesome-solid-user-group: **Participant:** UniMelbLT 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `1228faffe792fc1c63f1587d0f14d090` 
- :material-text: **Run description:** Baseline system, using language identification and lexical normalisation and off-the-shelf IR 

---
#### MONASH1NEW 
[**`Results`**](./results.md#monash1new), [**`Participants`**](./participants.md#monash), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.MONASH1NEW.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.MONASH1NEW), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.MONASH1NEW), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/MONASH1NEW.pdf) 

- :material-rename: **Name:** MONASH1NEW 
- :fontawesome-solid-user-group: **Participant:** monash 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `e468cbdd5a3b63d7a0d5dce5c1a871da` 
- :material-text: **Run description:** MONASH1NEW run performs similar way of MONASH2NEW but in order to enhance the performance we modified the returned values of some of the characteristics of tweets which have been mentioned in MONASH2NEW run.  

---
#### MONASH2NEW 
[**`Results`**](./results.md#monash2new), [**`Participants`**](./participants.md#monash), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.MONASH2NEW.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.MONASH2NEW), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.MONASH2NEW), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/MONASH2NEW.pdf) 

- :material-rename: **Name:** MONASH2NEW 
- :fontawesome-solid-user-group: **Participant:** monash 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `26d651fd17c4ad24af190668727f19cb` 
- :material-text: **Run description:** In MONASH2run, we take into consideration some of the tweet’s features in the other words, if a tweet has hash tag, @ tag or url, then add specific values to the function to make this tweet weigh more than others which they do not have. Moreover, our system calculates the value of IDF (Inverse Document Frequency) of a content of tweet and takes this value into account.  The other thing in our system is that the number of tweets which a user writes and a length of that twee, indeed, give a good indicator of the importance and the relevance of that tweet. Accordingly, both of them are taken into account. In addition to that, this run uses a method to detect the language of tweets. Therefore, if a language of a tweet is English, then it has more weight which makes English tweets appear in the top of non-English tweets.  

---
#### MorpheusRun1 
[**`Results`**](./results.md#morpheusrun1), [**`Participants`**](./participants.md#morpheus), [**`Proceedings`**](./proceedings.md#online-topic-modeling-for-real-time-twitter-search), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.MorpheusRun1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.MorpheusRun1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.MorpheusRun1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/MorpheusRun1.pdf) 

- :material-rename: **Name:** MorpheusRun1 
- :fontawesome-solid-user-group: **Participant:** Morpheus 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `2ac13ae226dd2afad39aaa4586e78038` 
- :material-text: **Run description:** Our system use a totally non-traditional approach to real-time search.  First we have a process of combining tweets into tweet bundles (super tweets). These super tweets allow us to have a larger document size for our topic modeling runs. Document size is a main draw back to using topic models with microblogs. We do a few things, on searches past an hour in time we run a batch Latent Dirichlet Allocation on hour intervals of tweets.  To find best super tweets we use Kullback–Leibler divergence on the topic distributions. To find the best tweets we use recency and word occurrence. 

---
#### mulnewWISTUD 
[**`Results`**](./results.md#mulnewwistud), [**`Participants`**](./participants.md#wis_tudelft), [**`Proceedings`**](./proceedings.md#wistud-at-trec-2011-microblog-track-exploiting-background-knowledge-from-dbpedia-and-news-articles-for-search-on-twitter), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.mulnewWISTUD.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.mulnewWISTUD), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.mulnewWISTUD), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/mulnewWISTUD.pdf) 

- :material-rename: **Name:** mulnewWISTUD 
- :fontawesome-solid-user-group: **Participant:** wis_tudelft 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `67646c18aa6376cdd7607e88750c372f` 
- :material-text: **Run description:** 1. dbpedia 3.6 version: published at 2011-01-17 2. Short description of news articles crawled from 62 news RSS feeds.(From Jan. 21st to Feb. 10th) 

---
#### myRun 
[**`Results`**](./results.md#myrun), [**`Participants`**](./participants.md#purdue_ir), [**`Proceedings`**](./proceedings.md#query-expansion-and-message-passing-algorithms-for-trec-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.myRun.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.myRun), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.myRun), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/myRun.pdf) 

- :material-rename: **Name:** myRun 
- :fontawesome-solid-user-group: **Participant:** Purdue_IR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `4157b6e8049492def50d3c134f51c562` 
- :material-text: **Run description:** Use belief propagation to select the exemplar of each tweet. Boost score of each tweet according to its exemplar. 

---
#### myrun2 
[**`Results`**](./results.md#myrun2), [**`Participants`**](./participants.md#purdue_ir), [**`Proceedings`**](./proceedings.md#query-expansion-and-message-passing-algorithms-for-trec-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.myrun2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.myrun2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.myrun2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/myrun2.pdf) 

- :material-rename: **Name:** myrun2 
- :fontawesome-solid-user-group: **Participant:** Purdue_IR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `db42d924a19d287374fdcc7e8be88a35` 
- :material-text: **Run description:** Use query expansion to reformulate query. Use belief propagation to select the exemplar of each tweet. Boost score of each tweet according to its exemplar. Use the same similarity metrics as in run1 

---
#### myrun3 
[**`Results`**](./results.md#myrun3), [**`Participants`**](./participants.md#purdue_ir), [**`Proceedings`**](./proceedings.md#query-expansion-and-message-passing-algorithms-for-trec-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.myrun3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.myrun3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.myrun3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/myrun3.pdf) 

- :material-rename: **Name:** myrun3 
- :fontawesome-solid-user-group: **Participant:** Purdue_IR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `690b48419ae8ce109c26a8d951bd06ee` 
- :material-text: **Run description:** Use belief propagation to select the exemplar of each tweet. Boost score of each tweet according to its exemplar. Use a different similarity metrics than run1 

---
#### Nestor 
[**`Results`**](./results.md#nestor), [**`Participants`**](./participants.md#irit_sig), [**`Proceedings`**](./proceedings.md#irit-at-trec-microblog-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.Nestor.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.Nestor), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.Nestor), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/Nestor.pdf) 

- :material-rename: **Name:** Nestor 
- :fontawesome-solid-user-group: **Participant:** IRIT_SIG 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `5ad7dcf7dab4591ce895b43649de19f4` 
- :material-text: **Run description:** We use a Bayesian network retrieval model for tweet search that considers, in addition to textual similarity measures, the social influence of microbloggers, the time magnitude, the tweet length and hashtags occurrence. Results are filtered by the numbers of query terms present in the tweet. No future or external features is used in this system. 

---
#### NestorS 
[**`Results`**](./results.md#nestors), [**`Participants`**](./participants.md#irit_sig), [**`Proceedings`**](./proceedings.md#irit-at-trec-microblog-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.NestorS.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.NestorS), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.NestorS), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/NestorS.pdf) 

- :material-rename: **Name:** NestorS 
- :fontawesome-solid-user-group: **Participant:** IRIT_SIG 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `50e9d8286f7dbcfbd0f7c31de812c4cf` 
- :material-text: **Run description:** We use a Bayesian network retrieval model for tweet search that considers, in addition to textual similarity measures, the time magnitude, the tweet length and hashtag occurrence.  This system ignores the social influence of microbloggers. Results are filtered by the numbers of query terms present in the tweet. No future of external features is used in this system. 

---
#### normal 
[**`Results`**](./results.md#normal), [**`Participants`**](./participants.md#kobeu), [**`Proceedings`**](./proceedings.md#trec-2011-microblog-track-experiments-at-kobe-university), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.normal.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.normal), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.normal), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/normal.pdf) 

- :material-rename: **Name:** normal 
- :fontawesome-solid-user-group: **Participant:** KobeU 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `6673f7d5991196223871f24eacf5a775` 
- :material-text: **Run description:** We retrieve tweets from indexes corresponding to each query time. 

---
#### nQCRIwoTag 
[**`Results`**](./results.md#nqcriwotag), [**`Participants`**](./participants.md#qcri), [**`Proceedings`**](./proceedings.md#qcri-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.nQCRIwoTag.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.nQCRIwoTag), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.nQCRIwoTag), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/nQCRIwoTag.pdf) 

- :material-rename: **Name:** nQCRIwoTag 
- :fontawesome-solid-user-group: **Participant:** QCRI 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `c0ca23ea4095a12ba8a1c594d930e19b` 
- :material-text: **Run description:** without Automatically induced tags, ordered 

---
#### nQCRIwTag 
[**`Results`**](./results.md#nqcriwtag), [**`Participants`**](./participants.md#qcri), [**`Proceedings`**](./proceedings.md#qcri-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.nQCRIwTag.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.nQCRIwTag), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.nQCRIwTag), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/nQCRIwTag.pdf) 

- :material-rename: **Name:** nQCRIwTag 
- :fontawesome-solid-user-group: **Participant:** QCRI 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `bf2a0cd0029e032dcb9ccb2b362e8da7` 
- :material-text: **Run description:** with Automatically induced tags, ordered 

---
#### omarRun 
[**`Results`**](./results.md#omarrun), [**`Participants`**](./participants.md#dlde), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.omarRun.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.omarRun), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.omarRun), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/omarRun.pdf) 

- :material-rename: **Name:** omarRun 
- :fontawesome-solid-user-group: **Participant:** DLDE 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/9/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `6fba88786362d1e431415e1c1ab07be4` 
- :material-text: **Run description:** This results only use the tweets itself , and we practice a simple model and use some heuristic rules to pure the results. 

---
#### PKUICST 
[**`Results`**](./results.md#pkuicst), [**`Participants`**](./participants.md#pku_icst), [**`Proceedings`**](./proceedings.md#pku-icst-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.PKUICST.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.PKUICST), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.PKUICST), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/PKUICST.pdf) 

- :material-rename: **Name:** PKUICST 
- :fontawesome-solid-user-group: **Participant:** PKU_ICST 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `4af1811b38070cdb3f2d38bb403ac363` 
- :material-text: **Run description:** This submission run at the dynamic index with respect to different query, and the number of result is selected according to a score threshold. 

---
#### PKUICST2 
[**`Results`**](./results.md#pkuicst2), [**`Participants`**](./participants.md#pku_icst), [**`Proceedings`**](./proceedings.md#pku-icst-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.PKUICST2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.PKUICST2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.PKUICST2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/PKUICST2.pdf) 

- :material-rename: **Name:** PKUICST2 
- :fontawesome-solid-user-group: **Participant:** PKU_ICST 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `4ed23ac4a71a5267d7a4250b3c27f87d` 
- :material-text: **Run description:** This submission run at the dynamic index with respect to different query, and the number of result is 30/31 per query. 

---
#### PKUICST3 
[**`Results`**](./results.md#pkuicst3), [**`Participants`**](./participants.md#pku_icst), [**`Proceedings`**](./proceedings.md#pku-icst-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.PKUICST3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.PKUICST3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.PKUICST3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/PKUICST3.pdf) 

- :material-rename: **Name:** PKUICST3 
- :fontawesome-solid-user-group: **Participant:** PKU_ICST 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `1887446e5dca8892c15e51cae519697a` 
- :material-text: **Run description:**  This submission run at the dynamic index with respect to different query, and the number of result is 100/101 per query. 

---
#### PKUICST4 
[**`Results`**](./results.md#pkuicst4), [**`Participants`**](./participants.md#pku_icst), [**`Proceedings`**](./proceedings.md#pku-icst-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.PKUICST4.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.PKUICST4), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.PKUICST4), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/PKUICST4.pdf) 

- :material-rename: **Name:** PKUICST4 
- :fontawesome-solid-user-group: **Participant:** PKU_ICST 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `cc098105eb33e72bdc219763652bc7c8` 
- :material-text: **Run description:**  This submission run at the dynamic index with respect to different query, and the number of result is 300/301 per query. 

---
#### PL2Bo1SDExt 
[**`Results`**](./results.md#pl2bo1sdext), [**`Participants`**](./participants.md#uow), [**`Proceedings`**](./proceedings.md#university-of-wolverhampton-at-the-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.PL2Bo1SDExt.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.PL2Bo1SDExt), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.PL2Bo1SDExt), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/PL2Bo1SDExt.pdf) 

- :material-rename: **Name:** PL2Bo1SDExt 
- :fontawesome-solid-user-group: **Participant:** UoW 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/2/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `c057d38c54d1a1555b2775a08e50e711` 
- :material-text: **Run description:** PL2 DFR algorithm with Sequential Divergence from Randomness based dependence model and Bo1 query expansion using linked HTML pages as part of tweet. 

---
#### PL2NoQENoDM 
[**`Results`**](./results.md#pl2noqenodm), [**`Participants`**](./participants.md#uow), [**`Proceedings`**](./proceedings.md#university-of-wolverhampton-at-the-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.PL2NoQENoDM.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.PL2NoQENoDM), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.PL2NoQENoDM), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/PL2NoQENoDM.pdf) 

- :material-rename: **Name:** PL2NoQENoDM 
- :fontawesome-solid-user-group: **Participant:** UoW 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/2/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `bc5fe4d773b1d6664a8cdd4012d99ea2` 
- :material-text: **Run description:** PL2 DFR algorithm baseline. 

---
#### PL2NoQeSd 
[**`Results`**](./results.md#pl2noqesd), [**`Participants`**](./participants.md#uow), [**`Proceedings`**](./proceedings.md#university-of-wolverhampton-at-the-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.PL2NoQeSd.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.PL2NoQeSd), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.PL2NoQeSd), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/PL2NoQeSd.pdf) 

- :material-rename: **Name:** PL2NoQeSd 
- :fontawesome-solid-user-group: **Participant:** UoW 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/2/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `f81c980eab64f23123c111101f8437a9` 
- :material-text: **Run description:** PL2 DFR algorithm with Sequential Divergence from Randomness based dependence model. 

---
#### PL2NoQeSdExt 
[**`Results`**](./results.md#pl2noqesdext), [**`Participants`**](./participants.md#uow), [**`Proceedings`**](./proceedings.md#university-of-wolverhampton-at-the-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.PL2NoQeSdExt.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.PL2NoQeSdExt), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.PL2NoQeSdExt), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/PL2NoQeSdExt.pdf) 

- :material-rename: **Name:** PL2NoQeSdExt 
- :fontawesome-solid-user-group: **Participant:** UoW 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/2/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `94001c71957e741b5ed0ad6dc8ef88d5` 
- :material-text: **Run description:** PL2 DFR algorithm with Sequential Divergence from Randomness based dependence model where the linked HTML pages are also part of the document. 

---
#### PRISrun1 
[**`Results`**](./results.md#prisrun1), [**`Participants`**](./participants.md#pris), [**`Proceedings`**](./proceedings.md#pris-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.PRISrun1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.PRISrun1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.PRISrun1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/PRISrun1.pdf) 

- :material-rename: **Name:** PRISrun1 
- :fontawesome-solid-user-group: **Participant:** PRIS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `48cd32d42dbb1c898f8fcfb39feb7a39` 
- :material-text: **Run description:** 1.There are no future or external resources used in this run.  2.Filter out irrelevant tweets using WAF(Word Activation Force) model. 3.Some parameters and thresholds in the model are select manually.  4.Operate in a strict real-time fashion.  

---
#### PRISrun2 
[**`Results`**](./results.md#prisrun2), [**`Participants`**](./participants.md#pris), [**`Proceedings`**](./proceedings.md#pris-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.PRISrun2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.PRISrun2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.PRISrun2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/PRISrun2.pdf) 

- :material-rename: **Name:** PRISrun2 
- :fontawesome-solid-user-group: **Participant:** PRIS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `72297b2efe89dea63764c41ce4cafe2d` 
- :material-text: **Run description:** 1.Web pages linked from tweets are used in this run.  2.Some parameters and thresholds in our model are select manually.  3.Operate in a strict real-time fashion. 4.Filter out irrelevant tweets using WAF(Word Activation Force) model. 

---
#### PRISrun3 
[**`Results`**](./results.md#prisrun3), [**`Participants`**](./participants.md#pris), [**`Proceedings`**](./proceedings.md#pris-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.PRISrun3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.PRISrun3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.PRISrun3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/PRISrun3.pdf) 

- :material-rename: **Name:** PRISrun3 
- :fontawesome-solid-user-group: **Participant:** PRIS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `877300bfbfa0413876c46be42fb904e3` 
- :material-text: **Run description:** 1.Corpus after the query time is used in this run.  2.The query system filters the desirable tweets automatically. 3.Filter out irrelevant tweets using WAF(Word Activation Force) model. 

---
#### PRISrun4 
[**`Results`**](./results.md#prisrun4), [**`Participants`**](./participants.md#pris), [**`Proceedings`**](./proceedings.md#pris-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.PRISrun4.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.PRISrun4), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.PRISrun4), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/PRISrun4.pdf) 

- :material-rename: **Name:** PRISrun4 
- :fontawesome-solid-user-group: **Participant:** PRIS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `c7b591bc0313002a37e8816c50e2bce7` 
- :material-text: **Run description:** 1.Corpus after the query time is used in this run.  2.Web pages linked from tweets are used in this run. 3.The query system filters the desirable tweets automatically. 4.Filter out irrelevant tweets using WAF(Word Activation Force) model. 

---
#### QCRIwoTagOrg 
[**`Results`**](./results.md#qcriwotagorg), [**`Participants`**](./participants.md#qcri), [**`Proceedings`**](./proceedings.md#qcri-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.QCRIwoTagOrg.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.QCRIwoTagOrg), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.QCRIwoTagOrg), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/QCRIwoTagOrg.pdf) 

- :material-rename: **Name:** QCRIwoTagOrg 
- :fontawesome-solid-user-group: **Participant:** QCRI 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `e9f9bb1ea861e3eaf86c814ca7d7b816` 
- :material-text: **Run description:** NO induced hash tags, Original ranking 

---
#### QCRIwTagOrg 
[**`Results`**](./results.md#qcriwtagorg), [**`Participants`**](./participants.md#qcri), [**`Proceedings`**](./proceedings.md#qcri-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.QCRIwTagOrg.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.QCRIwTagOrg), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.QCRIwTagOrg), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/QCRIwTagOrg.pdf) 

- :material-rename: **Name:** QCRIwTagOrg 
- :fontawesome-solid-user-group: **Participant:** QCRI 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `b1784eb259eda2dd2b99af342d1f5f4c` 
- :material-text: **Run description:** using automatically induced hash tags, Original ranking 

---
#### qHtagBaseRun 
[**`Results`**](./results.md#qhtagbaserun), [**`Participants`**](./participants.md#l3s), [**`Proceedings`**](./proceedings.md#exploiting-social-tagging-behavior-in-twitter-for-information-filtering-and-recommendation), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.qHtagBaseRun.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.qHtagBaseRun), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.qHtagBaseRun), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/qHtagBaseRun.pdf) 

- :material-rename: **Name:** qHtagBaseRun 
- :fontawesome-solid-user-group: **Participant:** L3S 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `ddb5dcb3ce242408005b51b477cfc79c` 
- :material-text: **Run description:** This run represents a simple baseline that take words in the title of the topic and used them as hashtags to select and rank the tweets.  

---
#### qRefLThresh 
[**`Results`**](./results.md#qreflthresh), [**`Participants`**](./participants.md#syles), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.qRefLThresh.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.qRefLThresh), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.qRefLThresh), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/qRefLThresh.pdf) 

- :material-rename: **Name:** qRefLThresh 
- :fontawesome-solid-user-group: **Participant:** syles 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `7d7552846d2cfa4ba3bf1682f4832939` 
- :material-text: **Run description:** - MSR Web Ngrams for query segmentation / reformulation / weighting - Tf.Idf on whole corpus (Lucene) - Language detector trained on Wikipedia  

---
#### refBalRun 
[**`Results`**](./results.md#refbalrun), [**`Participants`**](./participants.md#nusis), [**`Proceedings`**](./proceedings.md#nusis-at-trec-2011-microblog-track-refining-query-results-with-hashtags), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.refBalRun.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.refBalRun), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.refBalRun), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/refBalRun.pdf) 

- :material-rename: **Name:** refBalRun 
- :fontawesome-solid-user-group: **Participant:** NUSIS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `b818d50b444a834b8c92925b417da58b` 
- :material-text: **Run description:** this is the result of query reformulation and we balance relevance and recency 

---
#### refRelRun 
[**`Results`**](./results.md#refrelrun), [**`Participants`**](./participants.md#nusis), [**`Proceedings`**](./proceedings.md#nusis-at-trec-2011-microblog-track-refining-query-results-with-hashtags), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.refRelRun.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.refRelRun), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.refRelRun), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/refRelRun.pdf) 

- :material-rename: **Name:** refRelRun 
- :fontawesome-solid-user-group: **Participant:** NUSIS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `081f58f3cf19402ff3c1a94af2d07684` 
- :material-text: **Run description:** this is the result of query reformulation 

---
#### relevanceRun 
[**`Results`**](./results.md#relevancerun), [**`Participants`**](./participants.md#nusis), [**`Proceedings`**](./proceedings.md#nusis-at-trec-2011-microblog-track-refining-query-results-with-hashtags), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.relevanceRun.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.relevanceRun), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.relevanceRun), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/relevanceRun.pdf) 

- :material-rename: **Name:** relevanceRun 
- :fontawesome-solid-user-group: **Participant:** NUSIS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `2ffd2ddd5e2fe295e994bcdf57b60750` 
- :material-text: **Run description:** This is the basic run. 

---
#### RFD 
[**`Results`**](./results.md#rfd), [**`Participants`**](./participants.md#elly), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.RFD.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.RFD), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.RFD), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/RFD.pdf) 

- :material-rename: **Name:** RFD 
- :fontawesome-solid-user-group: **Participant:** Elly 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `a2045a1e9054bd4efed68c04340b0f8c` 
- :material-text: **Run description:** The RFD mode is a pattern based model. Different from term-based models, the weight of the terms in RFD model is based on the weight of the extracted patterns. The top 10 tweets were selected as the positive feedbacks. These pseudo-relevance feedbacks were used in the RFD model to generate the feature set. Then, the feature set was used to rank all the tweets. The top 1000 ranked tweets were submitted as the final results. 

---
#### ri 
[**`Results`**](./results.md#ri), [**`Participants`**](./participants.md#kobeu), [**`Proceedings`**](./proceedings.md#trec-2011-microblog-track-experiments-at-kobe-university), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.ri.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.ri), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.ri), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/ri.pdf) 

- :material-rename: **Name:** ri 
- :fontawesome-solid-user-group: **Participant:** KobeU 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `54eb009021921ab317f3a716ac45db4e` 
- :material-text: **Run description:** We use JSON format tweets to know user information and tweet's descriptions. Our run reranks tweets by learning to rank with careful attention to their topic and interestingness. 

---
#### rit 
[**`Results`**](./results.md#rit), [**`Participants`**](./participants.md#kobeu), [**`Proceedings`**](./proceedings.md#trec-2011-microblog-track-experiments-at-kobe-university), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.rit.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.rit), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.rit), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/rit.pdf) 

- :material-rename: **Name:** rit 
- :fontawesome-solid-user-group: **Participant:** KobeU 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `3d1576d11fb36ba2fd04ecfd69405eb9` 
- :material-text: **Run description:** We use JSON format tweets to know user information and tweet's descriptions. Our run reranks tweets by learning to rank with careful attention to their topic, interestingness, and time.    

---
#### rit3 
[**`Results`**](./results.md#rit3), [**`Participants`**](./participants.md#kobeu), [**`Proceedings`**](./proceedings.md#trec-2011-microblog-track-experiments-at-kobe-university), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.rit3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.rit3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.rit3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/rit3.pdf) 

- :material-rename: **Name:** rit3 
- :fontawesome-solid-user-group: **Participant:** KobeU 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `0f501622e54ae9bf98e4d001095babb3` 
- :material-text: **Run description:**  We use JSON format tweets to know user information and tweet's descriptions. Our run reranks tweets by learning to rank with careful attention to their topic, interestingness, and time. We also use the wordnet for query expantion. 

---
#### RMITAR 
[**`Results`**](./results.md#rmitar), [**`Participants`**](./participants.md#rmit), [**`Proceedings`**](./proceedings.md#rmit-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.RMITAR.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.RMITAR), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.RMITAR), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/RMITAR.pdf) 

- :material-rename: **Name:** RMITAR 
- :fontawesome-solid-user-group: **Participant:** RMIT 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `43595f1783eb6716124606040a0f224e` 
- :material-text: **Run description:** English dictionary to filter out non-english tweets. 

---
#### RMITM 
[**`Results`**](./results.md#rmitm), [**`Participants`**](./participants.md#rmit), [**`Proceedings`**](./proceedings.md#rmit-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.RMITM.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.RMITM), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.RMITM), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/RMITM.pdf) 

- :material-rename: **Name:** RMITM 
- :fontawesome-solid-user-group: **Participant:** RMIT 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `25743aa8a5020827d1e6a454d7f95ffe` 
- :material-text: **Run description:** External sources:  - english dictionary to filter out non english tweets  

---
#### RMITMR 
[**`Results`**](./results.md#rmitmr), [**`Participants`**](./participants.md#rmit), [**`Proceedings`**](./proceedings.md#rmit-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.RMITMR.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.RMITMR), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.RMITMR), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/RMITMR.pdf) 

- :material-rename: **Name:** RMITMR 
- :fontawesome-solid-user-group: **Participant:** RMIT 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `029cb02fccff09deb252bc7595bcb68c` 
- :material-text: **Run description:** - english dictionary to filter out non english tweets. 

---
#### RMITMRR 
[**`Results`**](./results.md#rmitmrr), [**`Participants`**](./participants.md#rmit), [**`Proceedings`**](./proceedings.md#rmit-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.RMITMRR.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.RMITMRR), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.RMITMRR), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/RMITMRR.pdf) 

- :material-rename: **Name:** RMITMRR 
- :fontawesome-solid-user-group: **Participant:** RMIT 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `bd5ce14d6d4b820f984266646a647726` 
- :material-text: **Run description:** english dictionary to filter out non-english tweets. 

---
#### Rocchio 
[**`Results`**](./results.md#rocchio), [**`Participants`**](./participants.md#elly), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.Rocchio.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.Rocchio), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.Rocchio), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/Rocchio.pdf) 

- :material-rename: **Name:** Rocchio 
- :fontawesome-solid-user-group: **Participant:** Elly 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `8a50379eec1de900e8679b1136c971da` 
- :material-text: **Run description:** The Rocchio was used to build user profiles from pseudo-relevance feedbacks. Then the feedbacks were used to re-rank all tweets. The top 1000 ranked documents were submitted as the final results. 

---
#### RTB 
[**`Results`**](./results.md#rtb), [**`Participants`**](./participants.md#tud_dmir), [**`Proceedings`**](./proceedings.md#dmir-on-microblog-track-2011), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.RTB.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.RTB), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.RTB), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/RTB.pdf) 

- :material-rename: **Name:** RTB 
- :fontawesome-solid-user-group: **Participant:** TUD_DMIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `6c6ce650e0618c06c02e9a39d9518bf9` 
- :material-text: **Run description:** The index for the query MB007 is polluted, while other queries are conducted under the strict realtime condition. The scoring method balances the time dimension and information dimension. 

---
#### run1 
[**`Results`**](./results.md#run1), [**`Participants`**](./participants.md#ictir), [**`Proceedings`**](./proceedings.md#author-model-and-negative-feedback-methods-on-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.run1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.run1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.run1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/run1.pdf) 

- :material-rename: **Name:** run1 
- :fontawesome-solid-user-group: **Participant:** ICTIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/6/2011 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `d77899e073f8b0925519c3225486a591` 
- :material-text: **Run description:** p@30 

---
#### run1a 
[**`Results`**](./results.md#run1a), [**`Participants`**](./participants.md#qut1), [**`Proceedings`**](./proceedings.md#microblog-retrieval-using-topical-features-and-query-expansion), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.run1a.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.run1a), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.run1a), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/run1a.pdf) 

- :material-rename: **Name:** run1a 
- :fontawesome-solid-user-group: **Participant:** QUT1 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `c09215a22f2c284fe27ba712ca440548` 
- :material-text: **Run description:** Pseudo rf no weight 

---
#### run1fix 
[**`Results`**](./results.md#run1fix), [**`Participants`**](./participants.md#ictir), [**`Proceedings`**](./proceedings.md#author-model-and-negative-feedback-methods-on-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.run1fix.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.run1fix), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.run1fix), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/run1fix.pdf) 

- :material-rename: **Name:** run1fix 
- :fontawesome-solid-user-group: **Participant:** ICTIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `e15b8b1136c619b750234725ef978eee` 
- :material-text: **Run description:** run1fix for p@30 

---
#### run2 
[**`Results`**](./results.md#run2), [**`Participants`**](./participants.md#ictir), [**`Proceedings`**](./proceedings.md#author-model-and-negative-feedback-methods-on-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.run2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.run2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.run2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/run2.pdf) 

- :material-rename: **Name:** run2 
- :fontawesome-solid-user-group: **Participant:** ICTIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** manual 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `a121efc2d844de57d23aba709de3d2f2` 
- :material-text: **Run description:** run2 combine author and cluster 

---
#### run2a 
[**`Results`**](./results.md#run2a), [**`Participants`**](./participants.md#qut1), [**`Proceedings`**](./proceedings.md#microblog-retrieval-using-topical-features-and-query-expansion), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.run2a.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.run2a), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.run2a), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/run2a.pdf) 

- :material-rename: **Name:** run2a 
- :fontawesome-solid-user-group: **Participant:** QUT1 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `92f3b72c372adfc1324106d459a4c52e` 
- :material-text: **Run description:** pseudo rf with weight 

---
#### run3 
[**`Results`**](./results.md#run3), [**`Participants`**](./participants.md#ucsc), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.run3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.run3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.run3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/run3.pdf) 

- :material-rename: **Name:** run3 
- :fontawesome-solid-user-group: **Participant:** UCSC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `3cb8117ee7a56c197df59fd6eb0eed36` 
- :material-text: **Run description:** sum of query word idf,  if has URL,  URL MIME/text,  URL MIME/audio,  URL MIME/video,  URL MIME/image,  URL MIME/application,  if has hashtap #,  average word length of tweet,  word length variance of tweet,  if has @,  stop word percent,  bm25 score of tweet,  tf score of tweet,  tfidf score of tweet,  bm25 score of url title,  tf score of url title,  tfidf score of url title,  bm25 score of url page,  tf score of url page,  tfidf score of url page,  language model score of tweet,  doc length,  retweeted times,  tweet time, 

---
#### run3a 
[**`Results`**](./results.md#run3a), [**`Participants`**](./participants.md#qut1), [**`Proceedings`**](./proceedings.md#microblog-retrieval-using-topical-features-and-query-expansion), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.run3a.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.run3a), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.run3a), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/run3a.pdf) 

- :material-rename: **Name:** run3a 
- :fontawesome-solid-user-group: **Participant:** QUT1 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `2ad11f9c9b9ca5a79b752bf36c798532` 
- :material-text: **Run description:** This run uses pattern generated from query and reweight them based on the term frequency. 

---
#### run4 
[**`Results`**](./results.md#run4), [**`Participants`**](./participants.md#ucsc), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.run4.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.run4), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.run4), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/run4.pdf) 

- :material-rename: **Name:** run4 
- :fontawesome-solid-user-group: **Participant:** UCSC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `caf81b5b47b05c3e93d06f1efb4d6557` 
- :material-text: **Run description:** sum of query word idf,  if has URL,  if has hashtap #,  average word length of tweet,  word length variance of tweet,  if has @,  stop word percent,  bm25 score of tweet,  tf score of tweet,  tfidf score of tweet,  language model score of tweet,  doc length,  retweeted times,  tweet time, 

---
#### run4a 
[**`Results`**](./results.md#run4a), [**`Participants`**](./participants.md#qut1), [**`Proceedings`**](./proceedings.md#microblog-retrieval-using-topical-features-and-query-expansion), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.run4a.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.run4a), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.run4a), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/run4a.pdf) 

- :material-rename: **Name:** run4a 
- :fontawesome-solid-user-group: **Participant:** QUT1 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `540aec82c862294382744629e1947265` 
- :material-text: **Run description:** This run uses pattern generated from query, reweight them and combine with term weight based on the term frequency. 

---
#### RunAll 
[**`Results`**](./results.md#runall), [**`Participants`**](./participants.md#xmuprc), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.RunAll.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.RunAll), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.RunAll), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/RunAll.pdf) 

- :material-rename: **Name:** RunAll 
- :fontawesome-solid-user-group: **Participant:** xmuPRC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `c3996aef27f879bc7c9b8965ff0dafab` 
- :material-text: **Run description:** Index is built upon all tweets, expanding tweet contents by extracting contents from its linking web pages. Named Entity Extraction used. Query expansion by by extracting representative words from most relevant page on the web, pseudo relevance feedback and representative Hashtag keywords. Filter non-informative tweets by ensemble ranking author pagerank, author HITS authority and pure retweets. Filter non-english tweets. 

---
#### RunFut 
[**`Results`**](./results.md#runfut), [**`Participants`**](./participants.md#xmuprc), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.RunFut.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.RunFut), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.RunFut), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/RunFut.pdf) 

- :material-rename: **Name:** RunFut 
- :fontawesome-solid-user-group: **Participant:** xmuPRC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `adf99031ef313198daf392a9d5d936ba` 
- :material-text: **Run description:** Index is built upon all tweets, only including tweet contents. Named Entity Extraction used. Query expansion by pseudo relevance feedback and representative Hashtag keywords. Filter non-informative tweets by ensemble ranking author pagerank, author HITS authority and pure retweets. Filter non-english tweets. 

---
#### runNeMIS 
[**`Results`**](./results.md#runnemis), [**`Participants`**](./participants.md#nemis_isti_cnr), [**`Proceedings`**](./proceedings.md#isti-trec-microblog-track-2011-exploring-the-use-of-hashtag-segmentation-and-text-quality-ranking), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.runNeMIS.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.runNeMIS), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.runNeMIS), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/runNeMIS.pdf) 

- :material-rename: **Name:** runNeMIS 
- :fontawesome-solid-user-group: **Participant:** NEMIS_ISTI_CNR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `2042cf44a94b170cb51dd55ba5f8d825` 
- :material-text: **Run description:** Python retrieval system based on the whoosh library. The system uses three separate indexes: -one with the text of the tweet. -one with the distinct words composing any hash tag in the tweets (multi-word hash tag are automatically split with a Viterbi-based algorithm). -one with the title of any linked page by any tweet. The retrieval scores from the three indexes are linearly combined and a filtering threshold is used to filter out low-score tweets. 

---
#### runNeMISext 
[**`Results`**](./results.md#runnemisext), [**`Participants`**](./participants.md#nemis_isti_cnr), [**`Proceedings`**](./proceedings.md#isti-trec-microblog-track-2011-exploring-the-use-of-hashtag-segmentation-and-text-quality-ranking), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.runNeMISext.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.runNeMISext), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.runNeMISext), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/runNeMISext.pdf) 

- :material-rename: **Name:** runNeMISext 
- :fontawesome-solid-user-group: **Participant:** NEMIS_ISTI_CNR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `7ed10b983f96eb27b0f4845300e61109` 
- :material-text: **Run description:** Python retrieval system based on the whoosh library. The system uses three separate indexes: -one with the text of the tweet. -one with the distinct words composing any hash tag in the tweets (multi-word hash tag are automatically split with a Viterbi-based algorithm). -one with the title of any linked page by any tweet. This run uses a stylometric score function that compares each tweet with a word distribution model extracted from a collection of Reuters news (external resource). This function allows to filter out poorly written tweets. The retrieval scores from the three indexes and the stylometric score are linearly combined and a filtering threshold is used to filter out low-score tweets. 

---
#### RunPure 
[**`Results`**](./results.md#runpure), [**`Participants`**](./participants.md#xmuprc), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.RunPure.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.RunPure), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.RunPure), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/RunPure.pdf) 

- :material-rename: **Name:** RunPure 
- :fontawesome-solid-user-group: **Participant:** xmuPRC 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `329028ff3a7e6fbe5842ac702f527494` 
- :material-text: **Run description:** Index is built upon tweets that are before query time, only including tweet contents. Named Entity Extraction used. Query expansion by pseudo relevance feedback on Lucene search results. Filter non-informative tweets by ensemble ranking author pagerank and pure retweets. Filter non-english tweets. 

---
#### scurtuRun1 
[**`Results`**](./results.md#scurturun1), [**`Participants`**](./participants.md#vitalie_scurtu), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.scurtuRun1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.scurtuRun1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.scurtuRun1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/scurtuRun1.pdf) 

- :material-rename: **Name:** scurtuRun1 
- :fontawesome-solid-user-group: **Participant:** Vitalie_Scurtu 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `1c561553beedbd06c2fc7a296ad5954d` 
- :material-text: **Run description:** The system does some basic parsing for identification of tweets/retweets. the twitter is decomposed in a list of features that are purely extracted from text (such as mentions, links, hashtags etc.), and does language recognition. For querying it uses a simple strategy for keywords reduction, and as a scoring formula it uses lucene dismax query-document similarity. 

---
#### sielrun1 
[**`Results`**](./results.md#sielrun1), [**`Participants`**](./participants.md#siel_iiith), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.sielrun1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.sielrun1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.sielrun1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/sielrun1.pdf) 

- :material-rename: **Name:** sielrun1 
- :fontawesome-solid-user-group: **Participant:** SIEL_IIITH 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `3e71246ee2177f69105e05224e65a645` 
- :material-text: **Run description:** Uses a combination of Lucene tf-idf relevance score and a score generated by k-means clustering giving them weights in the ratio of 2:3. Does not uses any external source. 

---
#### sielrun2 
[**`Results`**](./results.md#sielrun2), [**`Participants`**](./participants.md#siel_iiith), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.sielrun2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.sielrun2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.sielrun2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/sielrun2.pdf) 

- :material-rename: **Name:** sielrun2 
- :fontawesome-solid-user-group: **Participant:** SIEL_IIITH 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `f63debe27b4cfcc68801f380e6e85e48` 
- :material-text: **Run description:** Uses a combination of Lucene tf-idf relevance score and a score generated by k-means clustering giving them weights in the ratio of 5:2. Does not uses any external source. 

---
#### sielrun3 
[**`Results`**](./results.md#sielrun3), [**`Participants`**](./participants.md#siel_iiith), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.sielrun3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.sielrun3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.sielrun3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/sielrun3.pdf) 

- :material-rename: **Name:** sielrun3 
- :fontawesome-solid-user-group: **Participant:** SIEL_IIITH 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `703ed32b19a47492e04d9a2792e1b65e` 
- :material-text: **Run description:** Uses a combination of Lucene tf-idf relevance score and a score generated by k-means clustering giving them weights in the ratio of 3:2. Does not uses any external source. 

---
#### sielrun4 
[**`Results`**](./results.md#sielrun4), [**`Participants`**](./participants.md#siel_iiith), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.sielrun4.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.sielrun4), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.sielrun4), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/sielrun4.pdf) 

- :material-rename: **Name:** sielrun4 
- :fontawesome-solid-user-group: **Participant:** SIEL_IIITH 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `31722c75077e7c0e59a18999b78a7eb2` 
- :material-text: **Run description:** Uses a combination of Lucene tf-idf relevance score and a score generated by k-means clustering giving them weights in the ratio of 7:2. Does not uses any external source. 

---
#### SienaCL1B 
[**`Results`**](./results.md#sienacl1b), [**`Participants`**](./participants.md#sienaclteam), [**`Proceedings`**](./proceedings.md#weeks-to-trec-stirs-siena-s-twitter-information-retrieval-system), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.SienaCL1B.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.SienaCL1B), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.SienaCL1B), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/SienaCL1B.pdf) 

- :material-rename: **Name:** SienaCL1B 
- :fontawesome-solid-user-group: **Participant:** SienaCLTeam 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/9/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `0ec65fa9348180621d758d32480e18ef` 
- :material-text: **Run description:** Utilized content of links in tweets 

---
#### SienaCL31 
[**`Results`**](./results.md#sienacl31), [**`Participants`**](./participants.md#sienaclteam), [**`Proceedings`**](./proceedings.md#weeks-to-trec-stirs-siena-s-twitter-information-retrieval-system), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.SienaCL31.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.SienaCL31), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.SienaCL31), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/SienaCL31.pdf) 

- :material-rename: **Name:** SienaCL31 
- :fontawesome-solid-user-group: **Participant:** SienaCLTeam 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/9/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `578a65ea6a00fbbe1c82b0d356c90947` 
- :material-text: **Run description:** Utilized Google for the query expansion module 

---
#### SienaCL342 
[**`Results`**](./results.md#sienacl342), [**`Participants`**](./participants.md#sienaclteam), [**`Proceedings`**](./proceedings.md#weeks-to-trec-stirs-siena-s-twitter-information-retrieval-system), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.SienaCL342.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.SienaCL342), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.SienaCL342), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/SienaCL342.pdf) 

- :material-rename: **Name:** SienaCL342 
- :fontawesome-solid-user-group: **Participant:** SienaCLTeam 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/9/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `563e765898ce0514ccbdffeaf86ab549` 
- :material-text: **Run description:** Content of URLs within tweets utilized WEKA machine learning used (e.g. information retrieved utilizing Twitter API) Query expansion module utilizing google  

---
#### SienaCLbase 
[**`Results`**](./results.md#sienaclbase), [**`Participants`**](./participants.md#sienaclteam), [**`Proceedings`**](./proceedings.md#weeks-to-trec-stirs-siena-s-twitter-information-retrieval-system), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.SienaCLbase.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.SienaCLbase), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.SienaCLbase), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/SienaCLbase.pdf) 

- :material-rename: **Name:** SienaCLbase 
- :fontawesome-solid-user-group: **Participant:** SienaCLTeam 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/8/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `a500d58e3ef37e960ff7bb2029cceedc` 
- :material-text: **Run description:** Simple baseline run using Lucene. Non-English tweets removed Textese expanded Strict RT's removed 

---
#### simfoll 
[**`Results`**](./results.md#simfoll), [**`Participants`**](./participants.md#ugla_d), [**`Proceedings`**](./proceedings.md#university-of-glasgow-ugla-d-at-trec-microblog-2011-temporal-pseudo-relevance-feedback-in-microblog-retrieval), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.simfoll.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.simfoll), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.simfoll), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/simfoll.pdf) 

- :material-rename: **Name:** simfoll 
- :fontawesome-solid-user-group: **Participant:** UGLA_D 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `8a92b27554c36a11348f481ad6a9e8fb` 
- :material-text: **Run description:** 1) Full text searching through mysql - this should be a flavour of bm25; results contain only tweets < tweet time given in topics 2) Removed straight retweets 3) Pushed up scores depending on the number of followers: score := score + log(#followers^(score/C) + 1); C=2 - given all users have followers in our tweet set, the use of log might not be ideal 4) Removed tweets which contain substrings identical to higher-scored ones, where the length of the substrings is > 60% of the length of the tweet (approximately) 

---
#### simfollTP01 
[**`Results`**](./results.md#simfolltp01), [**`Participants`**](./participants.md#ugla_d), [**`Proceedings`**](./proceedings.md#university-of-glasgow-ugla-d-at-trec-microblog-2011-temporal-pseudo-relevance-feedback-in-microblog-retrieval), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.simfollTP01.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.simfollTP01), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.simfollTP01), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/simfollTP01.pdf) 

- :material-rename: **Name:** simfollTP01 
- :fontawesome-solid-user-group: **Participant:** UGLA_D 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `b169bb09325e8b82cc28f7ad40d2cbef` 
- :material-text: **Run description:** Uses a novel temporal pseudo relevance feedback technique (based on the retrieval of our other run, simfoll) to attempt to expand query with terms that occur strongly in the the same time periods. Term temporality was extracted in 2 hour intervals for the duration of the collection with the algorithm attempting to identify and expand the query with other terms that had similar temporal characteristics. Lucene was used with a vector space retrieval model for the retrieval in this run. 

---
#### sylesNoRes 
[**`Results`**](./results.md#sylesnores), [**`Participants`**](./participants.md#syles), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.sylesNoRes.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.sylesNoRes), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.sylesNoRes), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/sylesNoRes.pdf) 

- :material-rename: **Name:** sylesNoRes 
- :fontawesome-solid-user-group: **Participant:** syles 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `cba58274e229a8ca581af0bb396aa0ff` 
- :material-text: **Run description:** - Cosine similarity with modified tf-idf formula for terms weight: weight(term) = 1 * log(1 / (df + 1)) / ave(tf) / (var(timef) + 1), where timef - time frequency - Filter documents not containing query terms starting with capital letter (e.g. New York) - Filter stopwords (Most frequent words. Computed from tweets until querytime) - Filter identical tweets using minhash  

---
#### tfTP01 
[**`Results`**](./results.md#tftp01), [**`Participants`**](./participants.md#ugla_d), [**`Proceedings`**](./proceedings.md#university-of-glasgow-ugla-d-at-trec-microblog-2011-temporal-pseudo-relevance-feedback-in-microblog-retrieval), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.tfTP01.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.tfTP01), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.tfTP01), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/tfTP01.pdf) 

- :material-rename: **Name:** tfTP01 
- :fontawesome-solid-user-group: **Participant:** UGLA_D 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `c30413773b6275230fb3a32fce409926` 
- :material-text: **Run description:** Uses a novel temporal pseudo-relevance feedback technique (based on a TF-only retrieval) to attempt to expand query with terms that occur strongly in the the same time periods. Term temporality was extracted in 2 hour intervals for the duration of the collection with the algorithm attempting to identify and expand the query with other terms that had similar temporal characteristics. Only the temporal information prior to the query was used by the temporal PRF algorithm (therefore this run conforms to the real-time requirements). Lucene was used with a TF-only vector space retrieval model for the initial and expanded retrieval in this run. 

---
#### udelIndri 
[**`Results`**](./results.md#udelindri), [**`Participants`**](./participants.md#udel), [**`Proceedings`**](./proceedings.md#simple-rank-based-filtering-for-microblog-retrieval-implications-for-evaluation-and-test-collections), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.udelIndri.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.udelIndri), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.udelIndri), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/udelIndri.pdf) 

- :material-rename: **Name:** udelIndri 
- :fontawesome-solid-user-group: **Participant:** udel 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `5a8ba18aefa7aeb66fe1579acbfc319a` 
- :material-text: **Run description:** basic indri run 

---
#### udelLucene 
[**`Results`**](./results.md#udellucene), [**`Participants`**](./participants.md#udel), [**`Proceedings`**](./proceedings.md#simple-rank-based-filtering-for-microblog-retrieval-implications-for-evaluation-and-test-collections), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.udelLucene.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.udelLucene), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.udelLucene), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/udelLucene.pdf) 

- :material-rename: **Name:** udelLucene 
- :fontawesome-solid-user-group: **Participant:** udel 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `edc77285fea3fb5fa418b571833774b9` 
- :material-text: **Run description:** basic lucene run 

---
#### UDMicroComb1 
[**`Results`**](./results.md#udmicrocomb1), [**`Participants`**](./participants.md#udel_fang), [**`Proceedings`**](./proceedings.md#time-sensitive-weighting-for-microblog-retrieval), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.UDMicroComb1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.UDMicroComb1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.UDMicroComb1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/UDMicroComb1.pdf) 

- :material-rename: **Name:** UDMicroComb1 
- :fontawesome-solid-user-group: **Participant:** Udel_Fang 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `879f50d5dc8bdca64b38bf750c16944d` 
- :material-text: **Run description:** Use time-sensitive weighting to favor tweets in "popular discussed" period. Use document-length-weighting to favor long and high-term-IDF tweets in order to improve "interestingness" (The only future information we used is term IDF).  Use pseudo feedback. 

---
#### UDMicroComb2 
[**`Results`**](./results.md#udmicrocomb2), [**`Participants`**](./participants.md#udel_fang), [**`Proceedings`**](./proceedings.md#time-sensitive-weighting-for-microblog-retrieval), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.UDMicroComb2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.UDMicroComb2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.UDMicroComb2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/UDMicroComb2.pdf) 

- :material-rename: **Name:** UDMicroComb2 
- :fontawesome-solid-user-group: **Participant:** Udel_Fang 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `a54a8349d750deff767d4d31331210d7` 
- :material-text: **Run description:** Use time-sensitive weighting to favor tweets in "popular discussed" period. Use document-length-weighting to favor long and high-term-IDF tweets in order to improve "interestingness" (The only future information we used is term IDF). Use yahoo's search result to do query expansion. 

---
#### UDMicroIDF 
[**`Results`**](./results.md#udmicroidf), [**`Participants`**](./participants.md#udel_fang), [**`Proceedings`**](./proceedings.md#time-sensitive-weighting-for-microblog-retrieval), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.UDMicroIDF.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.UDMicroIDF), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.UDMicroIDF), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/UDMicroIDF.pdf) 

- :material-rename: **Name:** UDMicroIDF 
- :fontawesome-solid-user-group: **Participant:** Udel_Fang 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/9/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `d3b7095102af99d3ea98abc1fcbe2f3f` 
- :material-text: **Run description:** Use time-sensitive weighting to favor tweets in "popular discussed" period. 

---
#### UDMicroIDFD 
[**`Results`**](./results.md#udmicroidfd), [**`Participants`**](./participants.md#udel_fang), [**`Proceedings`**](./proceedings.md#time-sensitive-weighting-for-microblog-retrieval), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.UDMicroIDFD.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.UDMicroIDFD), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.UDMicroIDFD), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/UDMicroIDFD.pdf) 

- :material-rename: **Name:** UDMicroIDFD 
- :fontawesome-solid-user-group: **Participant:** Udel_Fang 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `82ca89d80100ab264b00a5bf6c6a03d3` 
- :material-text: **Run description:** Use time-sensitive weighting to favor tweets in "popular discussed" period. Use document-length-weighting to favor long and high-term-IDF tweets in order to improve "interestingness" (The only future information we used is term IDF). 

---
#### uicir1 
[**`Results`**](./results.md#uicir1), [**`Participants`**](./participants.md#uicir), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.uicir1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.uicir1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.uicir1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/uicir1.pdf) 

- :material-rename: **Name:** uicir1 
- :fontawesome-solid-user-group: **Participant:** UICIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `e0dffd23595f54c73c9fefb6abe5ed47` 
- :material-text: **Run description:** We use Wikipedia and Google to conduct the query expansion. Moreover, Wikipedia is used to extracted the related concepts.  

---
#### uicir2 
[**`Results`**](./results.md#uicir2), [**`Participants`**](./participants.md#uicir), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.uicir2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.uicir2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.uicir2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/uicir2.pdf) 

- :material-rename: **Name:** uicir2 
- :fontawesome-solid-user-group: **Participant:** UICIR 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `e01d15a7c22b2c9300bddfd2be2bac89` 
- :material-text: **Run description:** We use Wikipedia and Google to conduct the query expansion. Moreover, Wikipedia is used to extracted the related concepts.  

---
#### UIowaS1 
[**`Results`**](./results.md#uiowas1), [**`Participants`**](./participants.md#uiowas), [**`Proceedings`**](./proceedings.md#the-university-of-iowa-at-trec-2011-microblogs-medical-records-and-crowdsourcing), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.UIowaS1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.UIowaS1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.UIowaS1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/UIowaS1.pdf) 

- :material-rename: **Name:** UIowaS1 
- :fontawesome-solid-user-group: **Participant:** UIowaS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `222ccd3b627801613484df2a449ec050` 
- :material-text: **Run description:** Dataset was pre-processed by extracting hashtags, mentions, and URLs, and was indexed using Indri. No external resources were used in this run, though it is not a strict real-time run, in that the queries were run against the index of the whole data set. Run consists of a merged set of results, ranging from most conservative to least. The least (OR) set of results was filtered using the presence of capitalized query words (as indicators of important entities in the query). The results were constrained temporally according to the query date, and duplicated tweets were removed. Finally top 30 results were ordered temporally. 

---
#### UIowaS2 
[**`Results`**](./results.md#uiowas2), [**`Participants`**](./participants.md#uiowas), [**`Proceedings`**](./proceedings.md#the-university-of-iowa-at-trec-2011-microblogs-medical-records-and-crowdsourcing), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.UIowaS2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.UIowaS2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.UIowaS2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/UIowaS2.pdf) 

- :material-rename: **Name:** UIowaS2 
- :fontawesome-solid-user-group: **Participant:** UIowaS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `bb2fbbad3a72d3a30877ce43dc43fa0d` 
- :material-text: **Run description:** Dataset was pre-processed by extracting hashtags, mentions, and URLs. External resources included expanded URLs (plus title, description and keywords from the pages they refer to), as well as definitions of tags using tagdef.com. It was indexed using Indri. It is not a strict real-time run, in that the queries were run against the index of the whole data set. Run consists of a merged set of results, ranging from most conservative to least. The least (OR) set of results was filtered using the presence of capitalized query words (as indicators of important entities in the query). The results were constrained temporally according to the query date, and duplicates tweets were removed. Finally top 30 results were ordered temporally.  

---
#### UIowaS3 
[**`Results`**](./results.md#uiowas3), [**`Participants`**](./participants.md#uiowas), [**`Proceedings`**](./proceedings.md#the-university-of-iowa-at-trec-2011-microblogs-medical-records-and-crowdsourcing), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.UIowaS3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.UIowaS3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.UIowaS3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/UIowaS3.pdf) 

- :material-rename: **Name:** UIowaS3 
- :fontawesome-solid-user-group: **Participant:** UIowaS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `1f092d376d8630bc90d40b19b939f8fc` 
- :material-text: **Run description:** Dataset was pre-processed by extracting hashtags, mentions, and URLs. External resources included expanded URLs (plus title, description and keywords from the pages they refer to), as well as definitions of tags using tagdef.com. It was indexed using Indri. It is not a strict real-time run, in that the queries were run against the index of the whole data set. Run consists of a merged set of results, ranging from most conservative to least. The least (OR) set of results was filtered using the presence of capitalized query words (as indicators of important entities in the query). For queries which had results from the conservative strategies, we performed query expansion by appending the most frequent capitalized word found in returned tweets which is not in the original query and is more or as frequent as one of original query terms. The results were constrained temporally according to the query date, and duplicates tweets were removed. Finally top 30 results were ordered temporally. 

---
#### UIowaS4 
[**`Results`**](./results.md#uiowas4), [**`Participants`**](./participants.md#uiowas), [**`Proceedings`**](./proceedings.md#the-university-of-iowa-at-trec-2011-microblogs-medical-records-and-crowdsourcing), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.UIowaS4.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.UIowaS4), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.UIowaS4), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/UIowaS4.pdf) 

- :material-rename: **Name:** UIowaS4 
- :fontawesome-solid-user-group: **Participant:** UIowaS 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `4c60733fb4e91670de30a6430f51ba8c` 
- :material-text: **Run description:** Dataset was pre-processed by extracting hashtags, mentions, and URLs. External resources included expanded URLs (plus title, description and keywords from the pages they refer to), as well as definitions of tags using tagdef.com. It was indexed using Indri. It is not a strict real-time run, in that the queries were run against the index of the whole data set. Run consists of a merged set of results, ranging from most conservative to least. The least (OR) set of results was filtered using the presence of capitalized query words (as indicators of important entities in the query). For queries which had results from the conservative strategies, we performed query expansion by appending the most frequent capitalized word found in returned tweets which is not in the original query and is more or as frequent as one of original query terms. The results were constrained temporally according to the query date, and duplicates tweets were removed. The results are NOT sorted temporally, but by relevance instead (which is the only difference from UIowaS3 run). 

---
#### uiucsf 
[**`Results`**](./results.md#uiucsf), [**`Participants`**](./participants.md#uiuc), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.uiucsf.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.uiucsf), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.uiucsf), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/uiucsf.pdf) 

- :material-rename: **Name:** uiucsf 
- :fontawesome-solid-user-group: **Participant:** uiuc 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `9756e1111fdd36a7ac71f9d55fedca78` 
- :material-text: **Run description:** mixture model of causal potential and standard tfidf-ness. 

---
#### uogTrLqea 
[**`Results`**](./results.md#uogtrlqea), [**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-at-trec-2011-experiments-with-terrier-in-crowdsourcing-microblog-and-web-tracks), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.uogTrLqea.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.uogTrLqea), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.uogTrLqea), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/uogTrLqea.pdf) 

- :material-rename: **Name:** uogTrLqea 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `49bf34e568dc2f3cd4abbbb7a3e51465` 
- :material-text: **Run description:** Learned run using 66 real-time non-external features 

---
#### uogTrLqeabd 
[**`Results`**](./results.md#uogtrlqeabd), [**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-at-trec-2011-experiments-with-terrier-in-crowdsourcing-microblog-and-web-tracks), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.uogTrLqeabd.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.uogTrLqeabd), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.uogTrLqeabd), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/uogTrLqeabd.pdf) 

- :material-rename: **Name:** uogTrLqeabd 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `a78d5aee1c52e88d3d22481fb856c980` 
- :material-text: **Run description:** Learned Run using 76 features including content linked from tweets.  

---
#### uogTrLqeabdd 
[**`Results`**](./results.md#uogtrlqeabdd), [**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-at-trec-2011-experiments-with-terrier-in-crowdsourcing-microblog-and-web-tracks), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.uogTrLqeabdd.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.uogTrLqeabdd), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.uogTrLqeabdd), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/uogTrLqeabdd.pdf) 

- :material-rename: **Name:** uogTrLqeabdd 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `fa0fccbf0c1901c6ce8bc438cd08555d` 
- :material-text: **Run description:** Learned run using 76 real-time non-external features where the objective function directly tries to trade off relevance and recency 

---
#### uogTrUB2 
[**`Results`**](./results.md#uogtrub2), [**`Participants`**](./participants.md#uogtr), [**`Proceedings`**](./proceedings.md#university-of-glasgow-at-trec-2011-experiments-with-terrier-in-crowdsourcing-microblog-and-web-tracks), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.uogTrUB2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.uogTrUB2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.uogTrUB2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/uogTrUB2.pdf) 

- :material-rename: **Name:** uogTrUB2 
- :fontawesome-solid-user-group: **Participant:** uogTr 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `9af36188e5379e3d0f21dfbdf978cad7` 
- :material-text: **Run description:** Filtering run 

---
#### UTBase 
[**`Results`**](./results.md#utbase), [**`Participants`**](./participants.md#utwente), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.UTBase.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.UTBase), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.UTBase), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/UTBase.pdf) 

- :material-rename: **Name:** UTBase 
- :fontawesome-solid-user-group: **Participant:** utwente 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `f68b57b10f11184032f6d3512ce16b11` 
- :material-text: **Run description:** Baseline run that performs a standard Lucene free text search over the content field of all tweets that exist up to the timestamp of each query. Performs only basic query pre-processing and matching: stopword removal+lowercasing and uses Lucene's StandardTokenizer. Uses a strict incremental index for each query. Applies (repeated) query expansion based on the tweet content if an original TREC query does not yield enough results.  

---
#### UTBaseRTF 
[**`Results`**](./results.md#utbasertf), [**`Participants`**](./participants.md#utwente), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.UTBaseRTF.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.UTBaseRTF), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.UTBaseRTF), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/UTBaseRTF.pdf) 

- :material-rename: **Name:** UTBaseRTF 
- :fontawesome-solid-user-group: **Participant:** utwente 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `801243b48a7bf536f318b4f829e77474` 
- :material-text: **Run description:** Performs a standard Lucene free text search over the content field of all tweets that exist up to the timestamp of each query, but uses a full index created for all tweets. Prefers tweets that have been retweeted one or more times, but falls back to unretweeted tweets if this yields an insufficient number of results. If this still does not yield enough results, (repeated) query expansion is applied based on the content of already obtained tweets. Basic query processing involves stopword removal+lowercasing and Lucene's StandardTokenizer.  

---
#### UTWngFuture 
[**`Results`**](./results.md#utwngfuture), [**`Participants`**](./participants.md#utwente), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.UTWngFuture.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.UTWngFuture), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.UTWngFuture), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/UTWngFuture.pdf) 

- :material-rename: **Name:** UTWngFuture 
- :fontawesome-solid-user-group: **Participant:** utwente 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `b986f08903d6d090899be016f5f2ba3d` 
- :material-text: **Run description:** Performs a Word n-gram search over the content field of all tweets that exist up to the timestamp of each query using Lucene, but uses a full index created for all tweets. The value of n used depends on the length in words of the input query and is almost always ceil(word_count(query)) unless word_count(query) is 2, in which case n is fixed to two. The word n-grams generated are posed as an “AND” query to the system and then interleaved to yield a final result list. If there are too few results, each query word is submitted as a query, and if that still does not yield enough results (repeated) query expansion is applied based on the content of already obtained tweets. Basic query processing involves stopword removal+lowercasing and Lucene's StandardTokenizer.  

---
#### UTWngFutureQ 
[**`Results`**](./results.md#utwngfutureq), [**`Participants`**](./participants.md#utwente), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.UTWngFutureQ.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.UTWngFutureQ), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.UTWngFutureQ), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/UTWngFutureQ.pdf) 

- :material-rename: **Name:** UTWngFutureQ 
- :fontawesome-solid-user-group: **Participant:** utwente 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `19e175fcd6ecacbf8d63c7778c495b43` 
- :material-text: **Run description:** Performs a Word n-gram search over the content field of all tweets that exist up to the timestamp of each query using Lucene using a full index created for all tweets. Prefers tweets that meet 4 quality criteria: contains either a hashtag or URL; is not directed at more than three people (with the “@” symbol), does not consist of more than 50 percent ALL CAPS words, and does not contain repeated exclamation marks. The value of n used for the word n-grams depends on the length in words of the input query and is almost always ceil(word_count(query)) unless word_count(query) is 2, in which case n is fixed to two. The word n-grams generated are posed as an “AND” query to the system and then interleaved to yield a final result list. If there are too few results, each query word is submitted as a query, and if that still does not yield enough results (repeated) query expansion is applied based on the content of already obtained tweets. Basic query processing involves stopword removal+lowercasing and Lucene's StandardTokenizer.  

---
#### waterlooa1 
[**`Results`**](./results.md#waterlooa1), [**`Participants`**](./participants.md#waterloo), [**`Proceedings`**](./proceedings.md#university-of-waterloo-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.waterlooa1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.waterlooa1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.waterlooa1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/waterlooa1.pdf) 

- :material-rename: **Name:** waterlooa1 
- :fontawesome-solid-user-group: **Participant:** waterloo 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `25fba9b6fdfe5c58f4d467a1fb0e7a0f` 
- :material-text: **Run description:** Uses the Wumpus Search Engine to issue multiple queries for indices respecting the time constraints. Combines results using reciprocal rank fusion. 

---
#### waterlooa2 
[**`Results`**](./results.md#waterlooa2), [**`Participants`**](./participants.md#waterloo), [**`Proceedings`**](./proceedings.md#university-of-waterloo-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.waterlooa2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.waterlooa2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.waterlooa2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/waterlooa2.pdf) 

- :material-rename: **Name:** waterlooa2 
- :fontawesome-solid-user-group: **Participant:** waterloo 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `1d83ce46435fe7be6389a0469ed5145a` 
- :material-text: **Run description:** Uses the Wumpus Search Engine to issue multiple queries for indices, where only HTTP Status 200 tweets are used, respecting the time constraints. Combines results using reciprocal rank fusion. Due to an error in how such tweets were selected, it cannot be guaranteed that all tweets used chronologically preceded the queerytweetime but all tweets returned are earlier than the time constraint. 

---
#### waterlooa3 
[**`Results`**](./results.md#waterlooa3), [**`Participants`**](./participants.md#waterloo), [**`Proceedings`**](./proceedings.md#university-of-waterloo-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.waterlooa3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.waterlooa3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.waterlooa3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/waterlooa3.pdf) 

- :material-rename: **Name:** waterlooa3 
- :fontawesome-solid-user-group: **Participant:** waterloo 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `668e0b977accf3080fcb4110cdb5247c` 
- :material-text: **Run description:** Uses the Wumpus Search Engine to issue multiple queries for indices respecting the time constraints. Queries were issued using psudeo-relevance feedback (Okapi and KLD type feedback) and the language model used was from a previous Terabyte track. Combines results using reciprocal rank fusion. 

---
#### waterlooa4 
[**`Results`**](./results.md#waterlooa4), [**`Participants`**](./participants.md#waterloo), [**`Proceedings`**](./proceedings.md#university-of-waterloo-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.waterlooa4.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.waterlooa4), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.waterlooa4), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/waterlooa4.pdf) 

- :material-rename: **Name:** waterlooa4 
- :fontawesome-solid-user-group: **Participant:** waterloo 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `a7ce41e7fdfcf31ba44e5a4b22d438e8` 
- :material-text: **Run description:** Uses the Wumpus Search Engine to issue multiple queries for indices respecting the time constraints. Combines results using reciprocal rank fusion. Following this results were reranked with respect to recency, i.e. the rrf score was multiplied by <querytweetime>/<tweetimecutoff>. 

---
#### WESTfilext 
[**`Results`**](./results.md#westfilext), [**`Participants`**](./participants.md#west), [**`Proceedings`**](./proceedings.md#livetweet-microblog-retrieval-based-on-interestingness-and-an-adaptation-of-the-vector-space-model), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.WESTfilext.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.WESTfilext), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.WESTfilext), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/WESTfilext.pdf) 

- :material-rename: **Name:** WESTfilext 
- :fontawesome-solid-user-group: **Participant:** WeST 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `6698265a2c3ef5ff77ca38ff22fe4121` 
- :material-text: **Run description:** Used ANEW sentiment vocabulary to compute the high-level feature (sentiment) of the tweet. 

---
#### WESTfilter 
[**`Results`**](./results.md#westfilter), [**`Participants`**](./participants.md#west), [**`Proceedings`**](./proceedings.md#livetweet-microblog-retrieval-based-on-interestingness-and-an-adaptation-of-the-vector-space-model), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.WESTfilter.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.WESTfilter), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.WESTfilter), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/WESTfilter.pdf) 

- :material-rename: **Name:** WESTfilter 
- :fontawesome-solid-user-group: **Participant:** WeST 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `48fee9dfc8a867da641043a80c8252be` 
- :material-text: **Run description:** This run is created purely using internal knowledge that is available at the time of query. No use of web pages linked from tweets. 

---
#### WESTrelint 
[**`Results`**](./results.md#westrelint), [**`Participants`**](./participants.md#west), [**`Proceedings`**](./proceedings.md#livetweet-microblog-retrieval-based-on-interestingness-and-an-adaptation-of-the-vector-space-model), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.WESTrelint.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.WESTrelint), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.WESTrelint), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/WESTrelint.pdf) 

- :material-rename: **Name:** WESTrelint 
- :fontawesome-solid-user-group: **Participant:** WeST 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/10/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `7842ecdefa8df62eb24e80d4e7e18d1e` 
- :material-text: **Run description:** Real time, no use of external knowledge, no use of web pages linked from tweets.  

---
#### WESTrlext 
[**`Results`**](./results.md#westrlext), [**`Participants`**](./participants.md#west), [**`Proceedings`**](./proceedings.md#livetweet-microblog-retrieval-based-on-interestingness-and-an-adaptation-of-the-vector-space-model), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.WESTrlext.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.WESTrlext), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.WESTrlext), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/WESTrlext.pdf) 

- :material-rename: **Name:** WESTrlext 
- :fontawesome-solid-user-group: **Participant:** WeST 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `14a344ab4b4970e40567b7fd597d2028` 
- :material-text: **Run description:** Used ANEW sentiment vocabulary to compute the high-level feature (sentiment) of the tweet. 

---
#### Wise2ndRun 
[**`Results`**](./results.md#wise2ndrun), [**`Participants`**](./participants.md#seem_cuhk), [**`Proceedings`**](./proceedings.md#exploring-tweets-normalization-and-query-time-sensitivity-for-twitter-search), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.Wise2ndRun.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.Wise2ndRun), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.Wise2ndRun), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/Wise2ndRun.pdf) 

- :material-rename: **Name:** Wise2ndRun 
- :fontawesome-solid-user-group: **Participant:** SEEM_CUHK 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `5034c44f8df0dbcd0db56d38434e4c6d` 
- :material-text: **Run description:** 1. Language model based retrieval 2. Query expansion 

---
#### WiseFifthRun 
[**`Results`**](./results.md#wisefifthrun), [**`Participants`**](./participants.md#seem_cuhk), [**`Proceedings`**](./proceedings.md#exploring-tweets-normalization-and-query-time-sensitivity-for-twitter-search), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.WiseFifthRun.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.WiseFifthRun), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.WiseFifthRun), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/WiseFifthRun.pdf) 

- :material-rename: **Name:** WiseFifthRun 
- :fontawesome-solid-user-group: **Participant:** SEEM_CUHK 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `6018662af8b9237cc35bcf1c8b98b7a8` 
- :material-text: **Run description:** 1. Language Model based Retrieval  2. topic classification based on the result returned  3. result re-ranking strategy for emerging topic (different with the fourth run) 

---
#### WiseFouthRun 
[**`Results`**](./results.md#wisefouthrun), [**`Participants`**](./participants.md#seem_cuhk), [**`Proceedings`**](./proceedings.md#exploring-tweets-normalization-and-query-time-sensitivity-for-twitter-search), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.WiseFouthRun.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.WiseFouthRun), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.WiseFouthRun), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/WiseFouthRun.pdf) 

- :material-rename: **Name:** WiseFouthRun 
- :fontawesome-solid-user-group: **Participant:** SEEM_CUHK 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `ecab4cad81c0fa0941772dc7642bd6b6` 
- :material-text: **Run description:** 1. Language Model based Retrieval 2. topic classification based on the result returned 3. result re-ranking for emerging topic 

---
#### WiseThirdRun 
[**`Results`**](./results.md#wisethirdrun), [**`Participants`**](./participants.md#seem_cuhk), [**`Proceedings`**](./proceedings.md#exploring-tweets-normalization-and-query-time-sensitivity-for-twitter-search), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.WiseThirdRun.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.WiseThirdRun), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.WiseThirdRun), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/WiseThirdRun.pdf) 

- :material-rename: **Name:** WiseThirdRun 
- :fontawesome-solid-user-group: **Participant:** SEEM_CUHK 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `4023e21d0665040e464e1fb572715e74` 
- :material-text: **Run description:** 1. Language model based retrieval 2. Normalize all the tweets in the corpus 

---
#### ya3 
[**`Results`**](./results.md#ya3), [**`Participants`**](./participants.md#yandex), [**`Proceedings`**](./proceedings.md#yandex-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.ya3.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.ya3), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.ya3), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/ya3.pdf) 

- :material-rename: **Name:** ya3 
- :fontawesome-solid-user-group: **Participant:** yandex 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `c5cf5b7a565c55fe385ea3d59a730c84` 
- :material-text: **Run description:** -Query extension -User social features, such as number of followers at etc. -Textual quality and diversity of the tweets (query independent) -Emotion features  of the tweets -Text features the headers of external links -Ranking scores achieved from boosting trees regression algorithm 

---
#### ya4 
[**`Results`**](./results.md#ya4), [**`Participants`**](./participants.md#yandex), [**`Proceedings`**](./proceedings.md#yandex-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.ya4.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.ya4), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.ya4), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/ya4.pdf) 

- :material-rename: **Name:** ya4 
- :fontawesome-solid-user-group: **Participant:** yandex 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/12/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `4effd0c57d54f17af70338f2e6e0e132` 
- :material-text: **Run description:** -Query extension -User social features, such as number of followers at etc. -Textual quality and diversity of the tweets (query independent) -Emotion features  of the tweets -Text features the headers of external links -Ranking scores achieved from boosting trees classification algorithm 

---
#### YNDXTPC1 
[**`Results`**](./results.md#yndxtpc1), [**`Participants`**](./participants.md#yandex), [**`Proceedings`**](./proceedings.md#yandex-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.YNDXTPC1.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.YNDXTPC1), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.YNDXTPC1), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/YNDXTPC1.pdf) 

- :material-rename: **Name:** YNDXTPC1 
- :fontawesome-solid-user-group: **Participant:** yandex 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `08246052e6bb8ebac13810d1c46eeaf6` 
- :material-text: **Run description:** just query expansion using tweets posted before the query time 

---
#### YNDXTPC2 
[**`Results`**](./results.md#yndxtpc2), [**`Participants`**](./participants.md#yandex), [**`Proceedings`**](./proceedings.md#yandex-at-trec-2011-microblog-track), [**`Input`**](https://trec.nist.gov/results/trec20/microblog/input.YNDXTPC2.gz), [**`Summary (highrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.highrel.YNDXTPC2), [**`Summary (allrel)`**](https://trec.nist.gov/results/trec20/microblog/summary.allrel.YNDXTPC2), [**`Appendix`**](https://trec.nist.gov/pubs/trec20/appendices/microblog/YNDXTPC2.pdf) 

- :material-rename: **Name:** YNDXTPC2 
- :fontawesome-solid-user-group: **Participant:** yandex 
- :material-format-text: **Track:** Microblog 
- :material-calendar: **Year:** 2011 
- :material-upload: **Submission:** 8/11/2011 
- :fontawesome-solid-user-gear: **Type:** automatic 
- :material-text-search: **Task:** main 
- :material-fingerprint: **MD5:** `ad201ddcb1e660f8f3e537e21f6bdd74` 
- :material-text: **Run description:** just query expansion using tweets posted before the query time 

---
