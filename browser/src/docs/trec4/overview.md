# Text REtrieval Conference (TREC) 1995 

## Adhoc

[`Overview`](./adhoc/overview.md), [`Proceedings`](./adhoc/proceedings.md), [`Data`](./adhoc/data.md), [`Results`](./adhoc/results.md), [`Runs`](./adhoc/runs.md), [`Participants`](./adhoc/participants.md)

{==

The adhoc task is represented by new topics for known documents. 50 new test topics are used to create the adhoc queries for searching against the known documents. Fifty new topics (numbers 201-250) were generated for TREC-4. The known documents used in TREC-4 were on disks 2 and 3.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Donna Harman, National Institute of Standards and Technology (NIST) 




---

## Database Merging

[`Overview`](./dbmerge/overview.md), [`Proceedings`](./dbmerge/proceedings.md), [`Data`](./dbmerge/data.md), [`Results`](./dbmerge/results.md), [`Runs`](./dbmerge/runs.md), [`Participants`](./dbmerge/participants.md)

{==

The database merging task also represents a focussing of the adhoc task. In this case the goal was to investigate techniques for merging results from the various TREC subcollections as opposed to treating the collections as a single entity). There were 10 subcollections defined corresponding to the various dates of the data, i.e., the three different years of the Wall Street Journal, the two different years of the AP newswire, the two sets of Ziff documents (one on each disk), and the three single subcollections (the Federal Register, the San Jose Mercury News, and the U.S. Patents). The 3 participating groups ran the adhoc topics separately on each of the 10 subcollections, merged the results, and submitted these results, along with a baseline run treating the subcollections as a single collection.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Donna Harman, National Institute of Standards and Technology (NIST) 




---

## Routing

[`Overview`](./routing/overview.md), [`Proceedings`](./routing/proceedings.md), [`Data`](./routing/data.md), [`Results`](./routing/results.md), [`Runs`](./routing/runs.md), [`Participants`](./routing/participants.md)

{==

In TREC the routing task is represented by using known topics and known relevant documents for those topics, but new data for testing. The participants are given a set of known (or training) topics, along with a set of documents, including known relevant documents for those topics. The topics consist of natural language text describing a user's information need. The topics are used to create a set of queries (the actual input to the retrieval system) which are then used against the training documents.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Donna Harman, National Institute of Standards and Technology (NIST) 




---

## Spanish

[`Overview`](./spanish/overview.md), [`Proceedings`](./spanish/proceedings.md), [`Data`](./spanish/data.md), [`Results`](./spanish/results.md), [`Runs`](./spanish/runs.md), [`Participants`](./spanish/participants.md)

{==

The multilingual track represents an extension of the adhoc task to a second language (Spanish). An informal Spanish test was run in TREC-3, but the data arrived late and few groups were able to take part. In TREC-4 the track was made official and 10 groups took part. There were about 200 megabytes of Spanish data (the El Norte newspaper from Monterey, Mexico), and 25 topics. Groups used the adhoc task guidelines, and submitted the top 1000 documents retrieved for each of the 25 Spanish topics.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Donna Harman, National Institute of Standards and Technology (NIST) 




---

## Filtering

[`Overview`](./filtering/overview.md), [`Data`](./filtering/data.md)

{==

The filtering track represents a variation of the routing task, and was designed to investigate concerns about the current definition of this task. It used the same topics, training documents, and test documents as the routing task. The difference was that the results submitted for the filtering runs were unranked sets of documents satisfying three 'utility function' criteria. These criteria were designed to approximate a high precision run, a high recall run, and a balanced run.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- D. Lewis, AT&T Research 




---

## Confusion

[`Overview`](./confusion/overview.md), [`Proceedings`](./confusion/proceedings.md), [`Data`](./confusion/data.md), [`Results`](./confusion/results.md), [`Runs`](./confusion/runs.md), [`Participants`](./confusion/participants.md)

{==

The confusion track represents an extension of the current tasks to deal with corrupted data such as would come from OCR or speech input. The track followed the adhoc task, but using only the category B data. This data was randomly corrupted at NIST using character dele-tions, substitutions, and additions to create data with a 10% and 20% error rate (i.e., 10% or 20% of the characters were affected). Note that this process is neutral in that it does not model OCR or speech input. Four groups used the baseline and 10% corruption level; only two groups tried the 20% level.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Donna Harman, National Institute of Standards and Technology (NIST) 




---

## Interactive

[`Overview`](./interactive/overview.md), [`Proceedings`](./interactive/proceedings.md), [`Data`](./interactive/data.md), [`Results`](./interactive/results.md), [`Runs`](./interactive/runs.md), [`Participants`](./interactive/participants.md)

{==

The interactive track focusses the adhoc task on the process of doing searches interactively. It was felt by many groups that TREC uses evaluation for a batch retrieval environment rather than the more common interactive environments seen today. However there are few tools for evaluating interactive systems, and none that seem appropriate to TREC. The interactive track has a double goal of developing better methodologies for interactive evaluation and investigating in depth how users search the TREC topics. Eleven groups took part in this track in TREC-4. A subset of the adhoc topics was used, and many different types of experiments were run. The common thread was that all groups used the same topics, performed the same task(s), and recorded the same information about how the searches were done. Task 1 was to retrieve as many relevant documents as possible within a certain timeframe. Task 2 was to construct the best query possible.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Donna Harman, National Institute of Standards and Technology (NIST) 




---

