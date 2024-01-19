# Text REtrieval Conference (TREC) 2016 

## Clinical Decision Support

[`Overview`](./clinical/overview.md), [`Proceedings`](./clinical/proceedings.md), [`Data`](./clinical/data.md), [`Results`](./clinical/results.md), [`Runs`](./clinical/runs.md), [`Participants`](./clinical/participants.md)

{==

In handling challenging cases, clinicians often seek out information to make better decisions in patient care. Typically, these information sources combine clinical experience with scientific medical research in a process known as evidence-based medicine (EBM). Information relevant to a physician can be related to a variety of clinical tasks, such as (i) determining a patient's most likely diagnosis given a list of symptoms, (ii) determining if a particular test is indicated for a given situation, and (iii) deciding on the most effective treatment plan for a patient having a known condition. Finding the most relevant and recent research, however, can be quite challenging due to the volume of scientific literature and the pace at which new research is published. As such, the time-consuming nature of information seeking means that most clinician questions go unanswered (Ely et al., 2005). In order to better enable access to the scientific literature in the clinical setting, research is necessary to evaluate information retrieval methods that connect clinical notes with the published literature. The TREC Clinical Decision Support (CDS) track simulates the information retrieval requirements of such systems to encourage the creation of tools and resources necessary for their implementation. In 2014 and 2015, the CDS tracks used simulated patient cases presented as if they were typical case reports used in medical education. However, in an actual electronic health record (EHR), patient notes are written in a much different manner, notably with terse language and heavy use of abbreviations and clinical jargon. To address the challenge specific to EHR notes, the 2016 CDS track used de-identified notes for actual patients. This enabled participants to experiment with a realistic topic/query and develop methods to handle the challenging nature of clinical text. For a given EHR note, participants were challenged with retrieving full-text biomedical articles relevant for answering questions related to one of three generic clinical information needs: Diagnosis (i.e., “What is this patient's diagnosis?”), Test (“What diagnostic test is appropriate for this patient?”), and Treatment (“What treatment is appropriate for this patient?”). Retrieved articles were judged relevant if they provided information of the specified type useful for the given case. The assessment was performed by physicians with training in biomedical informatics using a 3-point scale: relevant, partially relevant, not relevant.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Kirk Roberts, The University of Texas Health Science Center 
- Dina Demner-Fushman, U.S. National Library of Medicine 
- Ellen M. Voorhees, National Institute of Standards and Technology (NIST) 
- William R. Hersh, Oregon Health and Science University 


:fontawesome-solid-globe: **Track Web Page:** [`https://www.trec-cds.org/`](https://www.trec-cds.org/) 

---

## LiveQA

[`Overview`](./qa/overview.md), [`Proceedings`](./qa/proceedings.md), [`Data`](./qa/data.md), [`Runs`](./qa/runs.md), [`Participants`](./qa/participants.md)

{==

The LiveQA track, now in its second year, is focused on real-time question answering for real-user questions. During the test period, real user questions are drawn from those newly submitted on a popular community question answering site, Yahoo Answers (YA), that have not yet been answered. These questions are sent to the participating systems, who provide an answer in real time. Returned answers are judged by the NIST assessors on a 4-level Likert scale. The most challenging aspects of this task are that the questions can be on any one of many popular topics, are informally stated, and are often complex and at least partly subjective. Furthermore, the participant systems must return an answer in under 60 seconds, which places additional, and realistic, constraints on the kind of processing that a system can do. In addition to the main real-time question answering task, this year we introduced a pilot task aimed at identifying the question intent. As human questions submitted on forums and CQA sites are verbose in nature and contain many redundant or unnecessary terms, participants were challenged to identify the significant parts of the question. The main theme of the question is marked by the systems by specifying a list of spans that capture its main intent. This automatic “summary” of the question was evaluated by measuring its ROUGEand METEOR-based similarity to a succinct rephrase of the question, manually provided by NIST assessors.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Eugene Agichtein, Emory University 
- David Carmel, Yahoo Research 
- Dan Pelleg, Yahoo Research 
- Yuval Pinter, Yahoo Research 
- Donna Harman - National Institute of Standards and Technology (NIST) 


:fontawesome-solid-globe: **Track Web Page:** [`https://web.archive.org/web/20160220151945/https://sites.google.com/site/trecliveqa2016/`](https://web.archive.org/web/20160220151945/https://sites.google.com/site/trecliveqa2016/) 

---

## Contextual Suggestion

[`Overview`](./context/overview.md), [`Proceedings`](./context/proceedings.md), [`Data`](./context/data.md), [`Results`](./context/results.md), [`Runs`](./context/runs.md), [`Participants`](./context/participants.md)

{==

The TREC Contextual Suggestion Track offers a personalized point of interest (POI) recommendation task, in which participants develop systems to give a ranked list of suggestions related to a profile and a context pair available in the tasks' requests provided by the track organizers. Previously, reusability of the contextual suggestion track suffered from using dynamic collections and a shallow pool depth. The main innovations at TREC 2016 are the following. First, the TREC CS web corpus, consisting of a web crawl of the TREC contextual suggestion collection, was made available. The rich textual descriptions of the web pages makes far more information available for each candidate POI in the collection. Second, we released endorsements (end user tags) of the attractions as given by NIST assessors, potentially matching the endorsements of POIs in another city as given by the person issuing the request as part of her profile. Third, a multi-depth pooling approach extending beyond the shallow top 5 pool was used. The multi-depth pooling approach has created a test collection that provides more reliable evaluation results in ranks deeper than the traditional pool cut-off.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Seyyed Hadi Hashemi,University of Amsterdam 
- Jaap KampsUniversity of Amsterdam 
- Julia Kiseleva, University of Amsterdam 
- Charles L.A. Clarke, University of Waterloo 
- Ellen M. Voorhees, National Institute of Standards and Technology (NIST) 


:fontawesome-solid-globe: **Track Web Page:** [`https://sites.google.com/site/treccontext/`](https://sites.google.com/site/treccontext/) 

---

## Real-time Summarization

[`Overview`](./realtime/overview.md), [`Proceedings`](./realtime/proceedings.md), [`Data`](./realtime/data.md), [`Runs`](./realtime/runs.md), [`Participants`](./realtime/participants.md)

{==

The TREC 2016 Real-Time Summarization (RTS) Track aims to explore techniques and systems that automatically monitor streams of social media posts such as Twitter to keep users up to date on topics of interest. We might think of these topics as “interest profiles”, specifying the user's prospective information needs. In real-time summarization, the goal is for a system to “push” (i.e., recommend or suggest) interesting and novel content to users in a timely fashion. For example, the user might be interested in poll results for the 2016 U.S. presidential elections and wishes to be notified whenever new results are published. 

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Jimmy Lin, University of Waterloo 
- Adam Roegiest, University of Waterloo 
- Luchen Tan, University of Waterloo 
- Richard McCreadie, University of Glasgow 
- Ellen Voorhees, National Institute of Standards and Technology (NIST) 
- Fernando Diaz, Microsoft Research 


:fontawesome-solid-globe: **Track Web Page:** [`https://trecrts.github.io/`](https://trecrts.github.io/) 

---

## Total Recall

[`Overview`](./recall/overview.md), [`Proceedings`](./recall/proceedings.md), [`Runs`](./recall/runs.md), [`Participants`](./recall/participants.md)

{==

The primary purpose of the Total Recall Track is to evaluate, through controlled simulation, methods designed to achieve very high recall - as close as practicable to 100% - with a human assessor in the loop. Motivating applications include, among others, electronic discovery in legal proceedings, systematic review in evidencebased medicine, and the creation of fully labeled test collections for information retrieval (“IR”) evaluation. A secondary, but no less important, purpose is to develop a sandboxed virtual test environment within which IR systems may be tested, while preventing the disclosure of sensitive test data to participants. At the same time, the test environment also operates as a “black box,” affording participants confidence that their proprietary systems cannot easily be reverse engineered.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Maura R. Grossman, University of Waterloo 
- Gordon V. Cormack, University of Waterloo 
- Adam Roegiest, University of Waterloo 


:fontawesome-solid-globe: **Track Web Page:** [`https://plg.uwaterloo.ca/~gvcormac/total-recall/`](https://plg.uwaterloo.ca/~gvcormac/total-recall/) 

---

## Tasks

[`Overview`](./task/overview.md), [`Proceedings`](./task/proceedings.md), [`Data`](./task/data.md), [`Results`](./task/results.md), [`Runs`](./task/runs.md), [`Participants`](./task/participants.md)

{==

Standard evaluation mechanisms focus on evaluating the quality of a retrieval system in terms of the relevance of the results retrieved, completely ignoring the fact that user satisfaction mainly depends on the usefulness of the system in helping the user complete the actual task that led the user issue the query. Similar to Tasks Track 2015 [1], Tasks Track 2016 is an attempt investigate quality of retrieval systems in terms of (1) how well they can understand the underlying task that led the user submit a query, and (2) how useful they are for helping users complete their tasks.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Manisha Verma, University College London 
- Emine Yilmaz, University College London 
- Rishabh Mehrotra, University College London 
- Evangelos Kanoulas, University of Amsterdam 
- Ben Carterette, University of Delaware 
- Nick Craswell, Microsoft 
- Peter Bailey, Microsoft 


:fontawesome-solid-globe: **Track Web Page:** [`http://www.cs.ucl.ac.uk/tasks-track-2016/`](http://www.cs.ucl.ac.uk/tasks-track-2016/) 

---

## Dynamic Domain

[`Overview`](./domain/overview.md), [`Proceedings`](./domain/proceedings.md), [`Data`](./domain/data.md), [`Runs`](./domain/runs.md), [`Participants`](./domain/participants.md)

{==

The main goal of TREC dynamic domain track is to explore and evaluate systems for interactive information retrieval, which reflects real-world search scenarios. Due to the importance of learning from user interactions, this track has been held for the second year. The name of the track contains two parts. “Dynamic” means that the search system dynamically adapts the provided ranking to the user through interactions. “Domain” stems from the fact that the search task in the track is on the domains of special interests, which tend to bring information needs that would not be met within a single interaction. The task is inspired by interested groups in government, including the DARPA Memex program.3 Each search task in the DD track involves some interactions between a user and a search system. In the first iteration, the user submits a query and the target domain of interest to the search system. The system provides the user with an initial ranking of documents, and receives feedback from the user on the provided ranking. This interaction, providing the user with a ranking and receiving the user’s feedback, continues until the search system stops the search task. The DD track introduces a new challenging search problem with the following important assumptions.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Grace Hui Yang, Georgetown University 
- Ian Soboroff, National Institute of Standards and Technology (NIST) 


:fontawesome-solid-globe: **Track Web Page:** [`https://infosense.cs.georgetown.edu/trec_dd/index.html`](https://infosense.cs.georgetown.edu/trec_dd/index.html) 

---

## OpenSearch

[`Overview`](./open/overview.md), [`Proceedings`](./open/proceedings.md), [`Runs`](./open/runs.md), [`Participants`](./open/participants.md)

{==

We present the TREC Open Search track, which represents a new evaluation paradigm for information retrieval. It offers the possibility for researchers to evaluate their approaches in a live setting, with real, unsuspecting users of an existing search engine. The first edition of the track focuses on the academic search domain and features the ad-hoc scientific literature search task. We report on experiments with three different academic search engines: CiteSeerX, SSOAR, and Microsoft Academic Search.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Krisztian Balog, University of Stavanger 
- Anne Schuth, Blendle 
- Peter Dekker, University of Amsterdam 
- Narges Tavakolpoursaleh, GESIS – Leibniz Institute for the Social Sciences 
- Philipp Schaer, TH Köln (University of Applied Sciences) 
- Po-Yu Chuang, Pennsylvania State University 


:fontawesome-solid-globe: **Track Web Page:** [`https://web.archive.org/web/20170617095056/http://trec-open-search.org/`](https://web.archive.org/web/20170617095056/http://trec-open-search.org/) 

---

