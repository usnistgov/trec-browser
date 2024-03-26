# Text REtrieval Conference (TREC) 2015 

## Clinical Decision Support

[`Overview`](./clinical/overview.md) | [`Proceedings`](./clinical/proceedings.md) | [`Data`](./clinical/data.md) | [`Results`](./clinical/results.md) | [`Runs`](./clinical/runs.md) | [`Participants`](./clinical/participants.md)

{==

In making clinical decisions, physicians often seek out information about how to best care for their patients. Information relevant to a physician can be related to a variety of clinical tasks such as (i) determining a patient’s most likely diagnosis given a list of symptoms, (ii) determining if a particular test is indicated for a given situation, and (iii) deciding on the most effective treatment plan for a patient having a known condition. In some cases, physicians can find the information they seek in published biomedical literature. However, given the volume of the existing literature and the rapid pace at which new research is published, locating the most relevant and timely information for a particular clinical need can be a daunting and timeconsuming task. In order to make biomedical information more accessible and to meet the requirements for the meaningful use of electronic health records (EHRs), a goal of modern clinical decision support systems is to anticipate the needs of physicians by linking EHRs with information relevant for patient care. The goal of the 2015 TREC Clinical Decision Support (CDS) track was to evaluate biomedical literature retrieval systems for providing answers to generic clinical questions about patient cases. Short case reports, such as those published in biomedical articles and used in medical lectures, acted as idealized representations of medical records. A case report typically describes a challenging medical case. It is organized as a well-formed narrative summarizing the pertient portions of the patient’s medical record. Given a case, participants were challenged with retrieving full-text biomedical articles relevant for answering questions related to one of three generic clinical information needs. The three needs were: Diagnosis (i.e., “What is this patient’s diagnosis?”), Test (“What diagnostic test is appropriate for this patient?”), and Treatment (“What treatment is appropriate for this patient?”). Retrieved articles were judged relevant if they provided information of the specified type useful for the given case. The assessment was performed by physicians with training in biomedical informatics. The evaluation of individual submissions followed standard TREC procedures. The 2015 CDS track differed from the 2014 CDS track (Simpson et al., 2014) by offering two tasks. Task A mirrored the 2014 CDS track, only with 30 new topics/cases. Task B used the same topics from Task A, but included the patient diagnosis for the Test and Treatment topics. Since the diagnosis was not guaranteed to be written in the case (consistent with how physicians often write cases in practice), we theorized that providing the diagnosis may improve retrieval systems by (a) providing additional relevant information if the diagnosis is not stated in the case, or (b) emphasizing a key piece of information in the case if the diagnosis is stated.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Kirk Roberts, U.S. National Library of Medicine (NIH) 
- Matthew S. Simpson, U.S. National Library of Medicine (NIH) 
- Ellen M. Voorhees, National Institute of Standards and Technology (NIST) 
- William R. Hersh, Oregon Health and Science University 


:fontawesome-solid-globe: **Track Web Page:** [`http://www.trec-cds.org/`](http://www.trec-cds.org/) 

---

## Microblog

[`Overview`](./microblog/overview.md) | [`Proceedings`](./microblog/proceedings.md) | [`Data`](./microblog/data.md) | [`Results`](./microblog/results.md) | [`Runs`](./microblog/runs.md) | [`Participants`](./microblog/participants.md)

{==

The TREC 2015 Microblog track introduced a single realtime filtering task broken down into two scenarios. Our goal is to explore techniques for monitoring streams of social media posts with respect to users’ interest profiles. An interest profile describes a topic about which the user wishes to receive information updates in real time, and is different from a typical ad hoc topic in that the profile represents a prospective (as opposed to a retrospective) information need. Thus, the nature of the desired information is qualitatively different. In real-time filtering, the goal is for a system to “push” (i.e., recommend, suggest) interesting and novel content to users in a timely fashion.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Jimmy Lin, University of Waterloo 
- Miles Efron, University of Illinois 
- Garrick Sherman, University of Illinois 
- Yulu Wang, University of Marland 
- Ellen M. Voorhees, National Institute of Standards and Technology (NIST) 


:fontawesome-solid-globe: **Track Web Page:** [`https://github.com/lintool/twitter-tools/wiki`](https://github.com/lintool/twitter-tools/wiki) 

---

## Contextual Suggestion

[`Overview`](./context/overview.md) | [`Proceedings`](./context/proceedings.md) | [`Data`](./context/data.md) | [`Results`](./context/results.md) | [`Runs`](./context/runs.md) | [`Participants`](./context/participants.md)

{==

The TREC Contextual Suggestion Track evaluates pointof-interest (POI) recommendation systems, with the goal of creating open and reusable test collections for this purpose. The track imagines a traveler in a unknown city seeking sites to see and things to do that reflect his or her own personal interests, as inferred from their interests in their home city. Given a user's profile, consisting of a POI list and rating from a home city, participants make recommendations for attractions in a target city (i.e., a new context).

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Adriel Dean-Hall, University of Waterloo 
- Charles L. A. Clarke, University of Waterloo 
- Jaap Kamps, University of Amsterdam 
- Julia Kiseleva Eindhoven, University of Technology 
- Ellen M. Voorhees, National Institute of Standards and Technology (NIST) 


:fontawesome-solid-globe: **Track Web Page:** [`https://sites.google.com/site/treccontext/`](https://sites.google.com/site/treccontext/) 

---

## Temporal Summarization

[`Overview`](./tempsumm/overview.md) | [`Proceedings`](./tempsumm/proceedings.md) | [`Data`](./tempsumm/data.md) | [`Runs`](./tempsumm/runs.md) | [`Participants`](./tempsumm/participants.md)

{==

There are many summarization scenarios that require updates to be issued to users over time. For example, during unexpected news events such as natural disasters or mass protests new information rapidly emerges. The TREC Temporal Summarization track aims to investigate how to effectively summarize these types of event in real-time. In particular, the goal is to develop systems which can detect useful, new, and timely sentence-length updates about a developing event to return to the user. In contrast to classical summarization challenges (such as DUC or TAC), the summaries produced by the participant systems are evaluated against a ground truth list of information nuggets representing the space of information that a user might want to know about each event. An optimal summary will cover all of the information nuggets in the minimum number of sentences. Also in contrast to classic summarization and newer timeline generation tasks, the Temporal Summarization track focuses on performing this analysis online as documents are indexed.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Javed Aslam 
- Fernando Diaz 
- Matthew Ekstrand-Abueg 
- Richard McCreadie 
- Virgil Pavlu 
- Tetsuya Sakai 


:fontawesome-solid-globe: **Track Web Page:** [`https://web.archive.org/web/20170618023232/http://www.trec-ts.org/`](https://web.archive.org/web/20170618023232/http://www.trec-ts.org/) 

---

## Tasks

[`Overview`](./task/overview.md) | [`Proceedings`](./task/proceedings.md) | [`Data`](./task/data.md) | [`Runs`](./task/runs.md) | [`Participants`](./task/participants.md)

{==

Research in Information Retrieval has traditionally focused on serving the best results for a single query, ignoring the reasons (or the task) that might have motivated the user to submit that query. Often times search engines are used to complete complex tasks (information needs); achieving these tasks with current search engines requires users to issue multiple queries. For example, booking travel to a location such as London could require the user to submit various queries such as flights to London, hotels in London, points of interest around London, etc. Standard evaluation mechanisms focus on evaluating the quality of a retrieval system in terms of the relevance of the results retrieved, completely ignoring the fact that user satisfaction mainly depends on the usefullness of the system in helping the user complete the actual task that led the user issue the query. The TREC 2015 Tasks Track is an attempt in devising mechanisms for evaluating quality of retrieval systems in terms of (1) how well they can understand the underlying task that led the user submit a query, and (2) how useful they are for helping users complete their tasks. In this overview, we first summarise the three categories of evaluation mechanisms used in the track and briefly describe the corpus, topics, and tasks that comprise the test collections. We then give an overview of the runs submitted to the Tasks Track and present evaluation results and analysis

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Emine Yilmaz, University College London 
- Manisha Verma, University College London 
- Rishabh Mehrotra, University College London 
- Evangelos Kanoulas, University of Amsterdam 
- Ben Carterette, University of Delaware 
- Nick Craswell, Microsoft 


:fontawesome-solid-globe: **Track Web Page:** [`http://www.cs.ucl.ac.uk/tasks-track-2015/`](http://www.cs.ucl.ac.uk/tasks-track-2015/) 

---

## Total Recall

[`Overview`](./recall/overview.md) | [`Proceedings`](./recall/proceedings.md) | [`Runs`](./recall/runs.md) | [`Participants`](./recall/participants.md)

{==

The primary purpose of the Total Recall Track is to evaluate, through controlled simulation, methods designed to achieve very high recall - as close as practicable to 100% - with a human assessor in the loop. Motivating applications include, among others, electronic discovery in legal proceedings, systematic review in evidencebased medicine, and the creation of fully labeled test collections for information retrieval (“IR”) evaluation. A secondary, but no less important, purpose is to develop a sandboxed virtual test environment within which IR systems may be tested, while preventing the disclosure of sensitive test data to participants. At the same time, the test environment also operates as a “black box,” affording participants confidence that their proprietary systems cannot easily be reverse engineered.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Adam Roegiest, University of Waterloo 
- Gordon V. Cormack, University of Waterloo 
- Charles L.A. Clarke, University of Waterloo 
- Maura R. Grossman, Wachtell, Lipton, Rosen & Katz 


:fontawesome-solid-globe: **Track Web Page:** [`https://plg.uwaterloo.ca/~gvcormac/trecvm/`](https://plg.uwaterloo.ca/~gvcormac/trecvm/) 

---

## Dynamic Domain

[`Overview`](./domain/overview.md) | [`Proceedings`](./domain/proceedings.md) | [`Data`](./domain/data.md) | [`Runs`](./domain/runs.md) | [`Participants`](./domain/participants.md)

{==

Search tasks for professional searchers, such as law enforcement agencies, police officers, and patent examiners, are often more complex than open domain Web search tasks. When professional searchers look for relevant information, it is often the case that they need to go through multiple iterations of searches to interact with a system. The Dynamic Domain Track supports research in dynamic, exploratory search within complex information domains. By providing real-time fine-grained feedback with relevance judgments that was collected during assessing time to the participating systems, we create a dynamic and iterative search process that lasts until the system decides to stop. The search systems are expected to be able to adjust their retrieval algorithms based on the feedback and find quickly relevant information for a multi-faceted information need. This document reports the task, datasets, topic and assessment creation, submissions, and evaluation results for the TREC 2015 Dynamic Domain (DD) Track.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Hui Yang, Georgetown University 
- John Frank, Diffeo and MIT 
- Ian Soboroff, National Institute of Standards and Technology (NIST) 


:fontawesome-solid-globe: **Track Web Page:** [`http://trec-dd.org`](http://trec-dd.org) 

---

## LiveQA

[`Overview`](./qa/overview.md) | [`Proceedings`](./qa/proceedings.md) | [`Data`](./qa/data.md) | [`Runs`](./qa/runs.md) | [`Participants`](./qa/participants.md)

{==

The automated question answering (QA) track, one of the most popular tracks in TREC for many years, has focused on the task of providing automatic answers for human questions. The track primarily dealt with factual questions, and the answers provided by participants were extracted from a corpus of News articles. While the task evolved to model increasingly realistic information needs, addressing question series, list questions, and even interactive feedback, a major limitation remained: the questions did not directly come from real users, in real time. The LiveQA track, conducted for the first time this year, focused on realtime question answering for real-user questions. Real user questions, i.e., fresh questions submitted on the Yahoo Answers (YA) site that have not yet been answered, were sent to the participant systems, which provided an answer in real time. Returned answers were judged by TREC editors on a 4-level Likert scale.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Eugene Agichtein, Emory University 
- David Carmel, Yahoo Labs 
- Dan Pelleg, Yahoo Labs 
- Yuval Pinter, Yahoo Labs 
- Donna Harman, National Institute of Standards and Technology (NIST) 


:fontawesome-solid-globe: **Track Web Page:** [`https://web.archive.org/web/20160219234556/https://sites.google.com/site/trecliveqa2015/`](https://web.archive.org/web/20160219234556/https://sites.google.com/site/trecliveqa2015/) 

---

