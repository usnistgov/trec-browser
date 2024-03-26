# Text REtrieval Conference (TREC) 2000 

## Web

[`Overview`](./web/overview.md) | [`Proceedings`](./web/proceedings.md) | [`Data`](./web/data.md) | [`Results`](./web/results.md) | [`Runs`](./web/runs.md) | [`Participants`](./web/participants.md)

{==

TREC-9 marked a broadening of the range of of search task types represented in the Web track and a serious attempt to determine whether hyperlinks could be used to improve retrieval effectiveness on a topic-relevance ad hoc retrieval task. The Large Web Task compared the ability of systems to locate online service pages within the 18.5 million page VLC2 collection. In this case the question is not whether the page is relevant to the topic, but whether it provides direct access to the desired service. In contrast, the Main Web Task compared link-based and non-link methods on a task involving topic relevance queries and a 1.69 million page corpus (WT10g) which was carefully engineered to ensure a high density of inter-server links and (relative) ease of processing. The Main Web task topics were in TREC Ad Hoc form but were reverse engineered from query logs. Ternary relevance judgments were obtained and, in addition, assessors were asked to identify 'best' documents for each topic. As in TREC-8, no significant benefit associated with the use of link information in a topic-relevance retrieval task was demonstrated by any of the participating groups, whether or not additional weight was given to highly relevant documents.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- D. Hawking, CSIRO Mathematical and Information Sciences 


:fontawesome-solid-globe: **Track Web Page:** [`https://trec.nist.gov/data/t9.web.html`](https://trec.nist.gov/data/t9.web.html) 

---

## Spoken Document Retrieval

[`Overview`](./sdr/overview.md) | [`Proceedings`](./sdr/proceedings.md) | [`Results`](./sdr/results.md) | [`Runs`](./sdr/runs.md) | [`Participants`](./sdr/participants.md)

{==

The SDR track fosters research on retrieval methodologies for spoken documents (i.e., recordings of speech). The task in the track is an ad hoc task in which the documents are transcriptions of audio signals.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- J. Garofolo, National Institute of Standards and Technology (NIST) 
- J. Lard, National Institute of Standards and Technology (NIST) 
- E. Voorhees, National Institute of Standards and Technology (NIST) 


:fontawesome-solid-globe: **Track Web Page:** [`https://trec.nist.gov/data/sdr.html`](https://trec.nist.gov/data/sdr.html) 

---

## Question Answering

[`Overview`](./qa/overview.md) | [`Proceedings`](./qa/proceedings.md) | [`Data`](./qa/data.md) | [`Runs`](./qa/runs.md) | [`Participants`](./qa/participants.md)

{==

The TREC question answering track is an effort to bring the benefits of large-scale evaluation to bear on the question answering problem. The track has run twice so far, where the goal both times was to retrieve small snippets of text that contain the actual answer to a question rather than the document lists traditionally returned by text retrieval systems. The best performing system in TREC-9, the Falcon system from Southern Methodist University, was able to answer about 65% of the questions (compared to approximately 42% of the questions for the next best systems) by combining abductive reasoning with various natural language processing techniques. The 65% score is slightly less than the best scores for TREC-8 in absolute terms, but it represents a very significant improvement in question answering systems. The TREC-9 task was considerably harder than the TREC-8 task because the TREC-9 track used actual users' questions rather than questions constructed specifically for the track.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- E. Voorhees, National Institute of Standards and Technology (NIST) 


:fontawesome-solid-globe: **Track Web Page:** [`https://trec.nist.gov/data/qamain.html`](https://trec.nist.gov/data/qamain.html) 

---

## Cross-Language

[`Overview`](./xlingual/overview.md) | [`Proceedings`](./xlingual/proceedings.md) | [`Results`](./xlingual/results.md) | [`Runs`](./xlingual/runs.md) | [`Participants`](./xlingual/participants.md)

{==

For TREC-9 the cross-language information retrieval task was to utilize English queries against Chinese documents. This aspect of multilingual information access at TREC-9 was the seventh year in which non-English document retrieval was tested and evaluated, and the fourth year for which cross-language information retrieval has been experimented with.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- F. Gey, A. Chen, University of California, Berkeley 




---

## Filtering

[`Overview`](./filtering/overview.md) | [`Proceedings`](./filtering/proceedings.md) | [`Data`](./filtering/data.md) | [`Runs`](./filtering/runs.md) | [`Participants`](./filtering/participants.md)

{==

The TREC-9 filtering track measures the ability of systems to build persistent user profiles which successfully separate relevant and non-relevant documents. It consists of three major subtasks: adaptive filtering, batch filtering, and routing. In adaptive filtering, the system begins with only a topic statement and a small number of positive examples, and must learn a better profile from on-line feedback. Batch filtering and routing are more traditional machine learning tasks where the system begins with a large sample of evaluated training documents.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- S. Robertson, Microsoft Research 
- D.A. Hull, WhizzBang Labs 


:fontawesome-solid-globe: **Track Web Page:** [`https://trec.nist.gov/data/filtering/README.t9.filtering`](https://trec.nist.gov/data/filtering/README.t9.filtering) 

---

## Query

[`Overview`](./query/overview.md) | [`Proceedings`](./query/proceedings.md) | [`Runs`](./query/runs.md) | [`Participants`](./query/participants.md)

{==

The Query Track in TREC-9 is unlike the other tracks in TREC. The other tracks attempt to compare systems to determine the best approaches to solve the particular track problem. This comparison is normally done over a given set of topics, with a single query per topic. The Query Track, on the other hand, compares multiple queries on a single topic to determine which queries perform best with which systems. There is no emphasis on system-system comparisons: none of the participating systems were even the most advanced system from that particular participating group. Instead, the goal is to try and understand how the statement (query) of the user's information need (topic) affects retrieval.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Chris Buckley, Sabir Research, Inc. 


:fontawesome-solid-globe: **Track Web Page:** [`https://trec.nist.gov/data/t8_query.html`](https://trec.nist.gov/data/t8_query.html) 

---

## Interactive

[`Overview`](./interactive/overview.md) | [`Proceedings`](./interactive/proceedings.md) | [`Data`](./interactive/data.md) | [`Runs`](./interactive/runs.md) | [`Participants`](./interactive/participants.md)

{==

The TREC Interactive Track has the goal of investigating interactive information retrieval by examining the process as well as the results. In TREC-9 six research groups ran a total of 12 interactive information retrieval (IR) system variants on a shared problem: a fact-finding task, eight questions, and newspaper/newswire documents from the TREC collections. This report summarizes the shared experimental framework, which for TREC-9 was designed to support analysis and comparison of system performance only within sites.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- W. Hersh, Oregon Health Sciences University 
- Paul Over, National Institute of Standards and Technology (NIST) 


:fontawesome-solid-globe: **Track Web Page:** [`https://trec.nist.gov/data/t9i/t9i.html`](https://trec.nist.gov/data/t9i/t9i.html) 

---

