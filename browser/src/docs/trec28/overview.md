# Text REtrieval Conference (TREC) 2019 

## Complex Answer Retrieval

[`Overview`](./car/overview.md), [`Proceedings`](./car/proceedings.md), [`Data`](./car/data.md), [`Runs`](./car/runs.md), [`Participants`](./car/participants.md)

{==

The vision of TREC Complex Answer Retrieval is to create complex long-form answers in response to a wide-variety information needs. In general, we aspire to create answers that are reminiscent to Wikipedia articles or school text books (e.g. TQA). However, while the vast majority of Wikipedia articles are about people, in TREC CAR we aim at information needs that are off the beaten path, covering topics in popular science, technology, and illnesses.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Laura Dietz, University of New Hampshire 
- John Foley, Smith College 


:fontawesome-solid-globe: **Track Web Page:** [`https://trec-car.cs.unh.edu/`](https://trec-car.cs.unh.edu/) 

---

## Deep Learning

[`Overview`](./deep/overview.md), [`Proceedings`](./deep/proceedings.md), [`Data`](./deep/data.md), [`Results`](./deep/results.md), [`Runs`](./deep/runs.md), [`Participants`](./deep/participants.md)

{==

The Deep Learning Track is a new track for TREC 2019, with the goal of studying ad hoc ranking in a large data regime. It is the first track with large human-labeled training sets, introducing two sets corresponding to two tasks, each with rigorous TREC-style blind evaluation and reusable test sets. The document retrieval task has a corpus of 3.2 million documents with 367 thousand training queries, for which we generate a reusable test set of 43 queries. The passage retrieval task has a corpus of 8.8 million passages with 503 thousand training queries, for which we generate a reusable test set of 43 queries. This year 15 groups submitted a total of 75 runs, using various combinations of deep learning, transfer learning and traditional IR ranking methods. Deep learning runs significantly outperformed traditional IR runs. Possible explanations for this result are that we introduced large training data and we included deep models trained on such data in our judging pools, whereas some past studies did not have such training data or pooling.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Nick Craswell,  Microsoft AI and Research 
- Bhaskar Mitra, Microsoft AI and Research 
- Daniel Campos,  Microsoft AI and Research 
- Emine Yilmaz, University College London 
- Ellen M. Voorhees, NIST 


:fontawesome-solid-globe: **Track Web Page:** [`https://microsoft.github.io/msmarco/TREC-Deep-Learning`](https://microsoft.github.io/msmarco/TREC-Deep-Learning) 

---

## Precision Medicine

[`Overview`](./pm/overview.md), [`Proceedings`](./pm/proceedings.md), [`Data`](./pm/data.md), [`Results`](./pm/results.md), [`Runs`](./pm/runs.md), [`Participants`](./pm/participants.md)

{==

Precision medicine is a medical paradigm in which treatments are customized entirely to the individual patient. The underlying issue that drives precision medicine is that for many complex diseases, there are no “one size fits all” solutions for patients with a particular diagnosis. The proper treatment for a patient depends upon genetic, environmental, and lifestyle choices. The ability to personalize treatment in a scientifically rigorous manner based on these factors is thus the hallmark of the emerging precision medicine paradigm. Nowhere is the potential impact of precision medicine more closely focused at the moment than in cancer, where lifesaving treatments for particular patients could prove ineffective or even deadly for other patients based entirely upon the particular genetic mutations in the patient’s tumor(s). Significant effort, therefore, has been devoted to deepening the scientific research surrounding precision medicine. This includes the Precision Medicine Initiative (Collins and Varmus, 2015) launched by President Barack Obama in 2015, now known as the All of Us Research Program.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Kirk Roberts, The University of Texas Health Science Center 
- Dina Demner-Fushman, U.S. National Library of Medicine 
- Ellen M. Voorhees, National Institute of Standards and Technology 
- William R. Hersh, Oregon Health & Science University 
- Steven Bedrick, Oregon Health & Science University 
- Alexander J. Lazar, The University of Texas MD Anderson Cancer Center 
- Shubham Pant, The University of Texas MD Anderson Cancer Center 
- Funda Meric-Bernstam, The University of Texas MD Anderson Cancer Center 


:fontawesome-solid-globe: **Track Web Page:** [`https://www.trec-cds.org/`](https://www.trec-cds.org/) 

---

## Conversational Assistance

[`Overview`](./cast/overview.md), [`Proceedings`](./cast/proceedings.md), [`Data`](./cast/data.md), [`Results`](./cast/results.md), [`Runs`](./cast/runs.md), [`Participants`](./cast/participants.md)

{==

The importance of conversation and conversational models for complex information seeking tasks is well-established within information retrieval, initially to understand user behavior during interactive search [4, 8] and later to improve search accuracy during search sessions [1]. The rapid adoption of a new generation of conversational assistants such as Alexa, Siri, Cortana, Bixby, and Google Assistant increase the scope and importance of conversational approaches to information seeking and also introduce a broad range of new research problems [2]. The TREC Conversational Assistance Track (CAsT) is a new initiative to facilitate Conversational Information Seeking (CIS) research and to create a large-scale reusable test collection for conversational search systems. We define it as a task in which effective response selection requires understanding a question’s context (the dialogue history). It focuses attention on user modeling, analysis of prior retrieval results, transformation of questions into effective queries, and other topics that have been difficult to study with previous datasets. To make this tractable and reusable for the first year of CAsT, we begin with pre-determined conversation trajectories and passage responses. Our target conversations include several rounds of utterances that are coherent in topic and explore relevant information. The primary initial focus is on system understanding of information needs in a conversational format and finding relevant passages leveraging conversational context. The long-term vision of CAsT is to allow natural conversions with mixed-initiative, where the system performs a variety of information actions [7], e.g., providing information (INFORM), asking clarifying questions (CLARIFY), leading conversations with more interactions (SUGGEST), and others. For the first year we focus on context understanding and use simple INFORM actions, where systems return text passages to the user. In the future, we plan to explore richer sets of information actions, richer response formats, and more interactions between users and conversational agents.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Jeffrey Dalton, University of Glasgow 
- Chenyan Xiong, Microsoft Research 
- Jamie Callan, Carnegie Mellon University 


:fontawesome-solid-globe: **Track Web Page:** [`https://www.treccast.ai/`](https://www.treccast.ai/) 

---

## News

[`Overview`](./news/overview.md), [`Proceedings`](./news/proceedings.md), [`Data`](./news/data.md), [`Results`](./news/results.md), [`Runs`](./news/runs.md), [`Participants`](./news/participants.md)

{==

The News track focuses on information retrieval in the service of helping people read the news. In 2018, in cooperation with the Washington Post1 , we released a new collection of nearly 600,000 news articles, and crafted two tasks related to how news is presented on the web: background linking and entity ranking. This second iteration of the track continues these two tasks with minor updates.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Ian Soboroff, NIST 
- Shudong Huang, NIST 
- Donna Harman, NIST 


:fontawesome-solid-globe: **Track Web Page:** [`http://trec-news.org/`](http://trec-news.org/) 

---

## Decision

[`Overview`](./decisions/overview.md), [`Proceedings`](./decisions/proceedings.md), [`Data`](./decisions/data.md), [`Results`](./decisions/results.md), [`Runs`](./decisions/runs.md), [`Participants`](./decisions/participants.md)

{==

Search engine results underpin many consequential decision making tasks. Examples include people using search technologies to seek health advice online [10, 18], or time-pressured clinicians relying on search results to decide upon the best treatment/diagnosis/test for a patient [22, 20]. A key problem when using search engines in order to complete such decision making tasks, is whether users are able to discern authoritative from unreliable information and correct from incorrect information. This problem is further exacerbated when the search occurs within uncontrolled data collections, such as the web, where information can be unreliable, generally misleading, too technical, and can lead to unfounded escalations [24]. Information from search engine results can significantly influence decisions, and research shows that increasing the amount of incorrect information about a topic presented in a Search Engine Result Page (SERP) can impel users to take incorrect decisions [16]. As noted in the SWIRL III report [7], decision making with search engines is poorly understood, and likewise, evaluation measures for these search tasks need to be developed and improved. In this context, the TREC 2019 Decision track aims to (1) foster research on retrieval methods that promote better decision making with search engines, and (2) develop new online and offline evaluation methods to predict the decision making quality induced by search results. This overview paper is organized as follows: Section 2 describes the track setup, the collection and the official evaluation measures, Section 3 reports and discusses the evaluation results for the submitted runs, and finally Section 4 outlines future directions for the next edition of the track.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Mustafa Abualsaud, University of Waterloo 
- Mark D. Smucker, University of Waterloo 
- Christina Lioma, University of Copenhagen 
- Maria Maistro, University of Copenhagen 
- Guido Zuccon, University of Queensland  


:fontawesome-solid-globe: **Track Web Page:** [`https://trec-health-misinfo.github.io/2019.html`](https://trec-health-misinfo.github.io/2019.html) 

---

## Fair Ranking

[`Overview`](./fair/overview.md), [`Proceedings`](./fair/proceedings.md), [`Data`](./fair/data.md), [`Runs`](./fair/runs.md), [`Participants`](./fair/participants.md)

{==

The goal of the TREC Fair Ranking track was to develop a benchmark for evaluating retrieval systems in terms of fairness to different content providers in addition to classic notions of relevance. As part of the benchmark, we defined standardized fairness metrics with evaluation protocols and released a dataset for the fair ranking problem. The 2019 task focused on reranking academic paper abstracts given a query. The objective was to fairly represent relevant authors from several groups that were unknown at the system submission time. Thus, the track emphasized the development of systems which have robust performance across a variety of group definitions. Participants were provided with querylog data (queries, documents, and relevance) from Semantic Scholar. This paper presents an overview of the track, including the task definition, descriptions of the data and the annotation process, as well as a comparison of the performance of submitted systems.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Asia J. Biega, Microsoft Research Montréal 
- Fernando Diaz, Microsoft Research Montréal 
- Michael D. Ekstrand, Boise State University 
- Sebastian Kohlmeier, Allen Institute for Artificial Intelligence 


:fontawesome-solid-globe: **Track Web Page:** [`https://fair-trec.github.io/`](https://fair-trec.github.io/) 

---

## Incident Streams

[`Overview`](./incident/overview.md), [`Proceedings`](./incident/proceedings.md), [`Data`](./incident/data.md), [`Runs`](./incident/runs.md), [`Participants`](./incident/participants.md)

{==

The ubiquity of mobile internet-enabled devices combined with wide-spread social media use during emergencies is posing new challenges for response personnel. In particular, service operators are now expected to monitor these online channels to extract actionable insights and answer questions from the public. A lack of adequate tools makes this monitoring impractical at the scale of many emergencies. The TREC Incident Streams (TREC-IS) track drives research into solving this technology gap by bringing together academia and industry to develop techniques for extracting actionable insights from social media streams during emergencies. This paper covers the second year of TREC-IS, hosted in 2019 with two editions, 2019-A and 2019-B, contributing 12 new events and approximately 20,000 new tweets across 25 information categories, with 15 research groups participating across the world. This paper provides an overview of these new editions, actionable insights from data labelling, and the automated techniques employed by participant systems that appear most effective.

==}

:fontawesome-solid-user-group: **Track coordinators:**

- Richard McCreadie, University of Glasgow 
- Cody Buntain, InfEco Lab, New Jersey Institute of Technology (NJIT) 
- Ian Soboroff, National Institute of Standards and Technology (NIST) 


:fontawesome-solid-globe: **Track Web Page:** [`https://www.dcs.gla.ac.uk/~richardm/TREC_IS/`](https://www.dcs.gla.ac.uk/~richardm/TREC_IS/) 

---

