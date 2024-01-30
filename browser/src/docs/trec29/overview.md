# Text REtrieval Conference (TREC) 2020 

## News

[`Overview`](./news/overview.md), [`Proceedings`](./news/proceedings.md), [`Data`](./news/data.md), [`Runs`](./news/runs.md), [`Participants`](./news/participants.md)

{==

The News track focuses on information retrieval in the service of helping people read the news. In 2018, in cooperation with the Washington Post, we released a new collection of nearly 600,000 news articles, and crafted two tasks related to how news is presented on the web: background linking and entity ranking. For 2020, we added more documents to the collection and retired the entity ranking task in favor of a new wikification task.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Ian Soboroff, National Institute of Standards and Technology 
- Shudong Huang, National Institute of Standards and Technology 
- Donna Harman, National Institute of Standards and Technology 


:fontawesome-solid-globe: **Track Web Page:** [`http://trec-news.org/`](http://trec-news.org/) 

---

## Deep Learning

[`Overview`](./deep/overview.md), [`Proceedings`](./deep/proceedings.md), [`Data`](./deep/data.md), [`Results`](./deep/results.md), [`Runs`](./deep/runs.md), [`Participants`](./deep/participants.md)

{==

This is the second year of the TREC Deep Learning Track, with the goal of studying ad hoc ranking in the large training data regime. We again have a document retrieval task and a passage retrieval task, each with hundreds of thousands of human-labeled training queries. We evaluate using singleshot TREC-style evaluation, to give us a picture of which ranking methods work best when large data is available, with much more comprehensive relevance labeling on the small number of test queries. This year we have further evidence that rankers with BERT-style pretraining outperform other rankers in the large data regime.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Nick Craswell, Microsoft AI & Research 
- Bhaskar Mitra, Microsoft AI & Research 
- Bhaskar Mitra, University College London 
- Emine Yilmaz, University College London 
-  Daniel Campos, University of Illinois Urbana-Champaign 


:fontawesome-solid-globe: **Track Web Page:** [`https://microsoft.github.io/msmarco/TREC-Deep-Learning`](https://microsoft.github.io/msmarco/TREC-Deep-Learning) 

---

## Incident Streams

[`Overview`](./incident/overview.md), [`Proceedings`](./incident/proceedings.md), [`Data`](./incident/data.md), [`Runs`](./incident/runs.md), [`Participants`](./incident/participants.md)

{==

Between 2018 and 2019, the Incident Streams track (TREC-IS) has developed standard approaches for classifying the types and criticality of information shared in online social spaces during crises, but the introduction of SARS-CoV-2 has shifted the landscape of online crises substantially. While prior editions of TREC-IS have lacked data on large-scale public-health emergencies as these events are exceedingly rare, COVID-19 has introduced an over-abundance of potential data, and significant open questions remain about how existing approaches to crisis informatics and datasets built on other emergencies adapt to this new context. This paper describes how the 2020 edition of TREC-IS has addressed these dual issues by introducing a new COVID-19-specific task for evaluating generalization of existing COVID-19 annotation and system performance to this new context, applied to 11 regions across the globe. TREC-IS has also continued expanding its set of target crises, adding 29 new events and expanding the collection of event types to include explosions, fires, and general storms, making for a total of 9 event types in addition to the new COVID-19 events. Across these events, TREC-IS has made available 478,110 COVID-related messages and 282,444 crisis-related messages for participant systems to analyze, of which 14,835 COVID-related and 19,784 crisis-related messages have been manually annotated. Analyses of these new datasets and participant systems demonstrate first that both the distributions of information type and priority of information vary between general crises and COVID-19-related discussion. Secondly, despite these differences, results suggest leveraging general crisis data in the COVID-19 context improves performance over baselines. Using these results, we provide guidance on which information types appear most consistent between general crises and COVID-19.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Cody Buntain, New Jersey Institute of Technology 
- Richard McCreadie, University of Glasgow 
-  Ian Soboroff, National Institute of Standards and Technology 


:fontawesome-solid-globe: **Track Web Page:** [`https://www.dcs.gla.ac.uk/~richardm/TREC_IS/`](https://www.dcs.gla.ac.uk/~richardm/TREC_IS/) 

---

## Health Misinformation

[`Overview`](./misinfo/overview.md), [`Proceedings`](./misinfo/proceedings.md), [`Data`](./misinfo/data.md), [`Results`](./misinfo/results.md), [`Runs`](./misinfo/runs.md), [`Participants`](./misinfo/participants.md)

{==

TREC 2020 was the second year for the Health Misinformation track, which was named the Decision Track in 2019. Information retrieval using document collections that contain misinformation are problematic. When a search engine returns documents that contain misinformation, users may have difficulty discerning correct from incorrect information and the incorrect information can lead to incorrect decisions. Decisions regarding health-related topics can be consequential, and as such we want search engines that enable users to make correct decisions. The track is designed to address the problem of health misinformation in three areas: 1) adhoc retrieval, 2) the total recall of misinformation in the collection, and 3) the evaluation of retrieval in the presence of misinformation. The 2020 Health Misinformation track had both a recall task and an adhoc task for participants. With the onset of the coronavirus pandemic (COVID-19), the track organizers selected a document collection of news from the Common Crawl that covered the first four months of 2020. The track’s topics were all related to COVID-19 and posed as questions such as “Can gargling salt water prevent COVID-19?” For both tasks, NIST assessors judged documents’ usefulness for answering a topic’s question, and if judged to be useful, assessors then recorded if the document contained a specific answer to the question and then judged the credibility of the document. We evaluated recall runs on their ability to find all documents containing incorrect information (misinformation). For adhoc runs, we measured their ability to return useful, correct, and credible information.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Charles L. A. Clarke, University of Waterloo 
- Saira Rizvi, University of Waterloo 
- Mark D. Smucker, University of Waterloo 
- Maria Maistro, University of Copenhagen 
- Guido Zuccon, University of Queensland 


:fontawesome-solid-globe: **Track Web Page:** [`https://trec-health-misinfo.github.io/`](https://trec-health-misinfo.github.io/) 

---

## Conversational Assistance

[`Overview`](./cast/overview.md), [`Proceedings`](./cast/proceedings.md), [`Data`](./cast/data.md), [`Results`](./cast/results.md), [`Runs`](./cast/runs.md), [`Participants`](./cast/participants.md)

{==

CAsT 2020 is the second year of the Conversational Assistance Track and builds on the lessons from the first year. Teams tried a wide range of techniques to address conversational search challenges. Some methods used proven techniques such as query difficulty prediction and query expansion. Given the text understanding challenges in the task, teams also used traditional NLP models that incorporate coreference resolution. One important development was the application of generative query models and ranking models using pre-trained neural language models. The results showed that both traditional and neural techniques provided complementary effectiveness.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Jeffrey Dalton, University of Glasgow 
- Chenyan Xiong, Microsoft Research 
- Jamie Callan, Carnegie Mellon University 


:fontawesome-solid-globe: **Track Web Page:** [`https://www.treccast.ai/`](https://www.treccast.ai/) 

---

## Precision Medicine

[`Overview`](./pm/overview.md), [`Proceedings`](./pm/proceedings.md), [`Data`](./pm/data.md), [`Results`](./pm/results.md), [`Runs`](./pm/runs.md), [`Participants`](./pm/participants.md)

{==

The precision medicine paradigm focuses on identifying treatments that are best suited to an individual patient’s unique attributes. The reasoning behind this paradigm is that diseases do not uniformly manifest in people and thus “one size fits all” treatments are often not appropriate. For many diseases, such as cancer, proper selection of a treatment strategy can drastically improve results compared to the standard, frontline treatment. Generally speaking, the issues that are taken into consideration for precision medicine are the genomic, environmental, and lifestyle contexts of the patient. While precision medicine as a paradigm can be seen to broadly apply to medicine as a whole, the area where it has seen the most attention is cancer. Many cancer treatments may be lifesaving in one patient but deadly in another, primarily based on the genetic mutations of the patient’s tumor. Different treatments for the same type of cancer often target the genetic pathways applicable to the specific tumor’s genes. As a result, there has been a significant amount of effort devoted to identifying these genetic pathways, identifying potential drugs that could target different aspects of these pathways, and assessing the clinical efficacy of these drugs in human studies. This includes the Precision Medicine Initiative (Collins and Varmus, 2015) launched by President Barack Obama in 2015, now known as the All of Us Research Program.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Kirk Roberts, The University of Texas Health Science Center 
- Dina Demner-Fushman, U.S. National Library of Medicine 
- Ellen M. Voorhees, National Institute of Standards and Technology 
- Steven Bedrick and William R. Hersh, Oregon Health & Science University 


:fontawesome-solid-globe: **Track Web Page:** [`https://www.trec-cds.org/`](https://www.trec-cds.org/) 

---

## Podcast

[`Overview`](./podcast/overview.md), [`Proceedings`](./podcast/proceedings.md), [`Data`](./podcast/data.md), [`Results`](./podcast/results.md), [`Runs`](./podcast/runs.md), [`Participants`](./podcast/participants.md)

{==

The Podcast Track is new at the Text Retrieval Conference (TREC) in 2020. The podcast track was designed to encourage research into podcasts in the information retrieval and NLP research communities. The track consisted of two shared tasks: segment retrieval and summarization, both based on a dataset of over 100,000 podcast episodes (metadata, audio, and automatic transcripts) which was released concurrently with the track. The track generated considerable interest, aracted hundreds of new registrations to TREC and fieen teams, mostly disjoint between search and summarization, made final submissions for assessment. Deep learning was the dominant experimental approach for both search experiments and summarization. This paper gives an overview of the tasks and the results of the participants’ experiments. The track will return to TREC 2021 with the same two tasks, incorporating slight modifications in response to participant feedback.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Rosie Jones, Spotify Research 
- Ben Carterette, Spotify Research 
- Ann Clifton, Spotify Research 
- Jussi Karlgren, Spotify Research 
- Aasish Pappu, Spotify Research 
-  Sravana Reddy, Spotify Research 
- Yongze Yu, Spotify Research 
- Maria Eskevich, CLARIN ERIC 
- Gareth J. F. Jones, Dublin City University 


:fontawesome-solid-globe: **Track Web Page:** [`https://trecpodcasts.github.io/`](https://trecpodcasts.github.io/) 

---

## Fair Ranking

[`Overview`](./fair/overview.md), [`Proceedings`](./fair/proceedings.md), [`Data`](./fair/data.md), [`Runs`](./fair/runs.md), [`Participants`](./fair/participants.md)

{==

For 2020, we again adopted an academic search task, where we have a corpus of academic article abstracts and queries submitted to a production academic search engine. The central goal of the Fair Ranking track is to provide fair exposure to different groups of authors (a group fairness framing). We recognize that there may be multiple group definitions (e.g. based on demographics, stature, topic) and hoped for the systems to be robust to these. We expected participants to develop systems that optimize for fairness and relevance for arbitrary group definitions, and did not reveal the exact group definitions until after the evaluation runs were submitted. The track contains two tasks, reranking and retrieval, with a shared evaluation.

==}

:fontawesome-solid-user-group: **Track coordinator(s):**

- Asia J. Biega, Microsoft Research Montreal 
- Fernando Diaz, Montreal Institute for Learning Algorithms 
- Michael D. Ekstrand, Boise State University 
- Sergey Feldman, Allen Institute for Artificial Intelligence 
- Sebastian Kohlmeier, Allen Institute for Artificial Intelligence 


:fontawesome-solid-globe: **Track Web Page:** [`https://fair-trec.github.io/`](https://fair-trec.github.io/) 

---

