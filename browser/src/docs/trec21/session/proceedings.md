# Proceedings - Session 2012 

#### Overview of the TREC 2012 Session Track

_Evangelos Kanoulas, Ben Carterette, Mark M. Hall, Paul D. Clough, Mark Sanderson_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/SESSION.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec21/papers/SESSION.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Session track ran for the third time in 2012. The track has the primary goal of providing test collections and evaluation measures for studying information retrieval over user sessions rather than one-time queries. These test collections are meant to be portable, reusable, statistically powerful, and open to anyone that wishes to work on the problem of retrieval over sessions. The experimental design of the track was similar to that of the second year [4]: sessions were real user sessions with a search engine that include queries, retrieved results, clicks, and dwell times; retrieval tasks were designed to study the effect of using increasing amounts of user data on retrieval effectiveness for the mth query in a session. There were a few changes compared to the second year of the track, mostly regarding the topic construction and the relevance assessments: 1. topics were constructed by the track co-ordinators; past TREC topics (mainly from QA2007 and MQ2009) tracks were used as in the second year; however, for each past topic 2-4 new topics were generated with certain characteristics regarding the type of the task; 2. relevance was defined at the level of the overall topic instead of subtopics. This overview is organized as follows: in Section 2 we describe the tasks participants were to perform. In Section 3 we describe the corpus, topics, and sessions that comprise the test collection. Section 4 gives some information about submitted runs. In Section 5 we describe relevance judging and evaluation measures, and Sections 6 present evaluation results and analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KanoulasCHCS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/KanoulasCHCS12,
		author = {Evangelos Kanoulas and Ben Carterette and Mark M. Hall and Paul D. Clough and Mark Sanderson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2012 Session Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/SESSION.OVERVIEW.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KanoulasCHCS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI at TREC 2012, KBA Track and Session Track

_Samur Araújo, Gebrekirstos G. Gebremeskel, Jiyin He, Corrado Boscarino, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [CWI](./participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/CWI.kba.session.final.pdf](http://trec.nist.gov/pubs/trec21/papers/CWI.kba.session.final.pdf)
- :material-file-search: **Runs:** [CWIrun1.RL1](./runs.md#cwirun1.rl1) | [CWIrun1.RL2](./runs.md#cwirun1.rl2) | [CWIrun1.RL3](./runs.md#cwirun1.rl3) | [CWIrun1.RL4](./runs.md#cwirun1.rl4) | [TUDrun.RL1](./runs.md#tudrun.rl1) | [TUDrun.RL2](./runs.md#tudrun.rl2) | [TUDrun.RL3](./runs.md#tudrun.rl3) | [TUDrun.RL4](./runs.md#tudrun.rl4) | [CWIrun3.RL1](./runs.md#cwirun3.rl1) | [CWIrun3.RL2](./runs.md#cwirun3.rl2) | [CWIrun3.RL3](./runs.md#cwirun3.rl3) | [CWIrun3.RL4](./runs.md#cwirun3.rl4)

??? abstract "Abstract"
	
	We participated in two tracks: Knowledge Base Acceleration (KBA) Track and Session Track. In the KBA track, we focused on experimenting with different approaches as it is the first time the track is launched. We experimented with supervised and unsupervised retrieval models. Our supervised approach models include language models and a string-learning system. Our unsupervised approaches include using: 1)DBpedia labels and 2) Google-Cross-Lingual Dictionary (GCLD). While the approach that uses GCLD targets the central and relvant bins, all the rest target the central bin. The GCLD and the string-learning system have outperformed the others in their respective targeted bins. The goal of the Session track submission is to evaluate whether and how a logic framework for representing user interactions with an IR system can be used for improving the approximation of the relevant term distribution that another system that is supposed to have access to the session information will then calculate the documents in the stream corpora. Three out of the seven runs used a Hadoop cluster provide by Sara.nl to process the stream corpora. The other 4 runs used a federated access to the same corpora distributed among 7 workstations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AraujoGHBV12.bib) "
	```
	@inproceedings{DBLP:conf/trec/AraujoGHBV12,
		author = {Samur Ara{\'{u}}jo and Gebrekirstos G. Gebremeskel and Jiyin He and Corrado Boscarino and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CWI} at {TREC} 2012, {KBA} Track and Session Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/CWI.kba.session.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AraujoGHBV12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Session Track TREC 2012

_Zhenhong Chen, Mingchuan Wei, Junxiao Nan, Jun Chen, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/ICTNET.session.final.pdf](http://trec.nist.gov/pubs/trec21/papers/ICTNET.session.final.pdf)
- :material-file-search: **Runs:** [ICTNET12SER1.RL1](./runs.md#ictnet12ser1.rl1) | [ICTNET12SER1.RL2](./runs.md#ictnet12ser1.rl2) | [ICTNET12SER1.RL3](./runs.md#ictnet12ser1.rl3) | [ICTNET12SER1.RL4](./runs.md#ictnet12ser1.rl4) | [ICTNET12SER2.RL1](./runs.md#ictnet12ser2.rl1) | [ICTNET12SER2.RL2](./runs.md#ictnet12ser2.rl2) | [ICTNET12SER2.RL3](./runs.md#ictnet12ser2.rl3) | [ICTNET12SER2.RL4](./runs.md#ictnet12ser2.rl4) | [ICTNET12SER3.RL1](./runs.md#ictnet12ser3.rl1) | [ICTNET12SER3.RL2](./runs.md#ictnet12ser3.rl2) | [ICTNET12SER3.RL3](./runs.md#ictnet12ser3.rl3) | [ICTNET12SER3.RL4](./runs.md#ictnet12ser3.rl4)

??? abstract "Abstract"
	
	In this paper, we describe our solutions to the Session Track at TREC 2012. The main contribution of our work is that we implement the learning to rank model to re-rank the documents retrieved by our search engine 2]. We notice that Huurninket al. [3] have used learning to rank algorithm to model session features at last year's Session Track. Due to lacking of training data, their model did not outperform substantially than others. Intuitively, we use last year's session data for tuning the weights of ranking features. Meanwhile, we define several useful features to model session search intent. The rest of this paper is organized as follows. We detail our models in section 2. Section 3 describes our experiments,including retrieve system setup,our research structure and our evaluation results. Conclusions are made in the last section.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenWNCYLC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenWNCYLC12,
		author = {Zhenhong Chen and Mingchuan Wei and Junxiao Nan and Jun Chen and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Session Track {TREC} 2012},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/ICTNET.session.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenWNCYLC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Effective Structured Query Formulation for Session Search

_Dongyi Guan, Hui Yang, Nazli Goharian_

- :fontawesome-solid-user-group: **Participant:** [Georgetown](./participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/Georgetown.session.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/Georgetown.session.nb.pdf)
- :material-file-search: **Runs:** [guphrase1.RL1](./runs.md#guphrase1.rl1) | [guphrase1.RL2](./runs.md#guphrase1.rl2) | [guphrase1.RL3](./runs.md#guphrase1.rl3) | [guphrase1.RL4](./runs.md#guphrase1.rl4) | [guphrase2.RL1](./runs.md#guphrase2.rl1) | [guphrase2.RL2](./runs.md#guphrase2.rl2) | [guphrase2.RL3](./runs.md#guphrase2.rl3) | [guphrase2.RL4](./runs.md#guphrase2.rl4) | [gurelaxphr.RL1](./runs.md#gurelaxphr.rl1) | [gurelaxphr.RL2](./runs.md#gurelaxphr.rl2) | [gurelaxphr.RL3](./runs.md#gurelaxphr.rl3) | [gurelaxphr.RL4](./runs.md#gurelaxphr.rl4)

??? abstract "Abstract"
	
	In this work, we emphasize on formulating effective structured queries for session search. For a given query, phrase-like text nuggets are identified and formulated into Lemur queries to feed into the Lemur search engine. Nuggets are substrings in qn, similar to phrases but not necessarily as semantically coherent as phrases. We assume that a valid nugget appears frequently in top returned snippets for qn. In this work, the longest sequences of words consisting of frequent bigrams within the top returned snippets are identified as nuggets and are used to formulate a new query. By formulating structured query using the nuggets, we greatly boost the search accuracy than just using qn. We experiment both strict and relaxed forms of structured query formulation. The strict form of query formulation achieves an improvement of 13.5% and the relaxed form achieves an improvement of 17.8% on nDCG@10 on TREC 2011 query sets. We further combine the nuggets generated from all queries q1, … , qn-1, qn, to formulate one structured session query for the entire session. Nuggets from each query are weighed by various weighting schemes to indicate their relations to the current query and their potential contributions to the retrieval performance. We experiment three weighting schemes, uniform (all queries share the same weight), previous vs. current (previous queries q1, … , qn-1 share the same weight while qn uses a different and higher weight), and distance-based (the weights are distributed based on how far a query's position in the session is from the current query). We find that previous vs. current achieves the best search accuracy. For retrieval, we first retrieve a large pool of documents for qn. We then employ a re-ranking model that considers document similarity between clicked documents and documents in the pool as well as dwell time.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GuanYG12.bib) "
	```
	@inproceedings{DBLP:conf/trec/GuanYG12,
		author = {Dongyi Guan and Hui Yang and Nazli Goharian},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Effective Structured Query Formulation for Session Search},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/Georgetown.session.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GuanYG12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at the TREC 2012 Session Track

_Matthias Hagen, Martin Potthast, Matthias Busse, Jakob Gomoll, Jannis Harder, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/webis.session.final.pdf](http://trec.nist.gov/pubs/trec21/papers/webis.session.final.pdf)
- :material-file-search: **Runs:** [webis12cnqe.RL1](./runs.md#webis12cnqe.rl1) | [webis12cnqe.RL2](./runs.md#webis12cnqe.rl2) | [webis12cnqe.RL3](./runs.md#webis12cnqe.rl3) | [webis12cnqe.RL4](./runs.md#webis12cnqe.rl4) | [webis12indqe.RL1](./runs.md#webis12indqe.rl1) | [webis12indqe.RL2](./runs.md#webis12indqe.rl2) | [webis12indqe.RL3](./runs.md#webis12indqe.rl3) | [webis12indqe.RL4](./runs.md#webis12indqe.rl4) | [webis12cnse.RL1](./runs.md#webis12cnse.rl1) | [webis12cnse.RL2](./runs.md#webis12cnse.rl2) | [webis12cnse.RL3](./runs.md#webis12cnse.rl3) | [webis12cnse.RL4](./runs.md#webis12cnse.rl4)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2012 Session track. Our runs focus on three research questions: (1) distinguishing low risk sessions where we want to involve session knowledge from those where we don't, (2) examining conservative query expansion (only few expansion terms based on keywords from previous queries and seen/clicked documents/titles/snippets), and (3) incorporating knowledge from other users' similar sessions. Altogether, especially similar sessions seem to help improving retrieval performance in our experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenPBGHS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenPBGHS12,
		author = {Matthias Hagen and Martin Potthast and Matthias Busse and Jakob Gomoll and Jannis Harder and Benno Stein},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Webis at the {TREC} 2012 Session Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/webis.session.final.pdf},
		timestamp = {Tue, 23 Jun 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HagenPBGHS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### On Duplicate Results in a Search Session

_Jiepu Jiang, Daqing He, Shuguang Han_

- :fontawesome-solid-user-group: **Participant:** [PITT](./participants.md#pitt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/PITT.session.final.pdf](http://trec.nist.gov/pubs/trec21/papers/PITT.session.final.pdf)
- :material-file-search: **Runs:** [PITTSHQM.RL1](./runs.md#pittshqm.rl1) | [PITTSHQM.RL2](./runs.md#pittshqm.rl2) | [PITTSHQM.RL3](./runs.md#pittshqm.rl3) | [PITTSHQM.RL4](./runs.md#pittshqm.rl4) | [PITTSHQMnov.RL1](./runs.md#pittshqmnov.rl1) | [PITTSHQMnov.RL2](./runs.md#pittshqmnov.rl2) | [PITTSHQMnov.RL3](./runs.md#pittshqmnov.rl3) | [PITTSHQMnov.RL4](./runs.md#pittshqmnov.rl4) | [PITTSHQMsdm.RL1](./runs.md#pittshqmsdm.rl1) | [PITTSHQMsdm.RL2](./runs.md#pittshqmsdm.rl2) | [PITTSHQMsdm.RL3](./runs.md#pittshqmsdm.rl3) | [PITTSHQMsnov.RL1](./runs.md#pittshqmsnov.rl1) | [PITTSHQMsnov.RL2](./runs.md#pittshqmsnov.rl2) | [PITTSHQMsnov.RL3](./runs.md#pittshqmsnov.rl3) | [PITTSHQMsnov.RL4](./runs.md#pittshqmsnov.rl4) | [PITTSHQMsdm.RL4](./runs.md#pittshqmsdm.rl4)

??? abstract "Abstract"
	
	In this paper, we introduce the PITT group's methods and findings in TREC 2012 session track. After analyzing the search logs in session track 2011 and 2012 datasets, we find that users' reformulated queries are very different from their previous ones, probably indicating their expectations to find not only relevant but also novel results. However, as indicated from our results, a major approach adopted by the session track participants, i.e. using relevance feedback information extracted from previous queries for search, will sacrifice the novelty of results for improving ad hoc search performance (e.g. nDCG@10). Such issues were not disclosed in previous years' session tracks because TREC did not consider the effects of duplicate results in evaluation. Therefore, we proposed a method to properly penalize the duplicate results in ranking by simulating users' browsing behaviors in a search session. A duplicate result in current search will be penalized to a greater extent if it was ranked in higher positions in previous searches or it was returned by more previous queries. The method can effectively improve the novelty of search results and lead to only slight and insignificant drop in ad hoc search performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangHH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangHH12,
		author = {Jiepu Jiang and Daqing He and Shuguang Han},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {On Duplicate Results in a Search Session},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/PITT.session.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangHH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers at the TREC 2012 Session Track

_Chang Liu, Michael J. Cole, Eun Baik, Nicholas J. Belkin_

- :fontawesome-solid-user-group: **Participant:** [ruiiltrec2012](./participants.md#ruiiltrec2012)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/ruiiltrec.session.final.pdf](http://trec.nist.gov/pubs/trec21/papers/ruiiltrec.session.final.pdf)
- :material-file-search: **Runs:** [RutgersHu.RL1](./runs.md#rutgershu.rl1) | [RutgersHu.RL2](./runs.md#rutgershu.rl2) | [RutgersHu.RL3](./runs.md#rutgershu.rl3) | [RutgersHu.RL4](./runs.md#rutgershu.rl4) | [RutgersM.RL1](./runs.md#rutgersm.rl1) | [RutgersM.RL2](./runs.md#rutgersm.rl2) | [RutgersM.RL3](./runs.md#rutgersm.rl3) | [RutgersM.RL4](./runs.md#rutgersm.rl4)

??? abstract "Abstract"
	
	At Rutgers, we approached the Session Track task as an issue of personalization, based on both the behaviors exhibited by the searcher during the course of an information seeking episode, and a classification of the task that led the person to engage in information-seeking behavior. Our general approach is described in detail at the Web site of our project (http://comminfo.rutgers.edu/imls/poodle) and in the papers available there. In the TREC 2011 Session Track, we tested preliminary results of predictive models of document usefulness using recursive partitioning models learned from user studies of task session information behaviors. In this year's TREC Session Track, we tested predictive models of document usefulness based on user behaviors by using logistic regression. This was combined with predictive models of task type derived from a multinomial logistic regression model learned from the 2012 Session Track data. After an overview of our approach we provide details of how we actually did things, our results, and our conclusions about the results. The Session Track tasks were addressed by first classifying the track task sessions into four types of tasks, using the scheme and method described in section 2. This classification was based on the Session topic descriptions and narratives. Task classification was performed both manually and automatically. We distinguish the two in our results submissions as RutgersHu (human) and RutgersM (machine). The task classifications were used in our experimental runs, where the document usefulness prediction model depended on the identified search task type along with the observed search behaviors. Since the Session Track data did not allow us to incorporate evidence from behaviors on content pages, we used only data associated with SERPs and various temporal characteristics, such as dwell time on content pages, and time between queries (section 3 describes the models and data in detail). The predicted useful documents were then used to modify the last query but one in each search session using the useful documents to supply terms in a standard relevance feedback mode using the Lemur system in remote mode (section 4 describes our methods in detail). Unlike our work in the 2011 Session Track, this year we used only positive feedback in the query expansion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuCBB12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuCBB12,
		author = {Chang Liu and Michael J. Cole and Eun Baik and Nicholas J. Belkin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Rutgers at the {TREC} 2012 Session Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/ruiiltrec.session.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuCBB12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### U. Albany & USC at the TREC 2012 Session Track

_Xiaojun Yuan, Jingling Liu, Ning Sa_

- :fontawesome-solid-user-group: **Participant:** [UAlbanySession](./participants.md#ualbanysession)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UAlbany-USC.session.pdf](http://trec.nist.gov/pubs/trec21/papers/UAlbany-USC.session.pdf)
- :material-file-search: **Runs:** [UAlbany.RL1](./runs.md#ualbany.rl1) | [UAlbany.RL2](./runs.md#ualbany.rl2) | [UAlbany.RL3](./runs.md#ualbany.rl3) | [UAlbany.RL4](./runs.md#ualbany.rl4)

??? abstract "Abstract"
	
	Research in Information Retrieval has noticed that it is often the case that in a search process, users begin an interaction with a sufficiently under-specified query and they will need to reformulate their query multiple times before they find desired information. In terms of this, researchers hypothesized that a search engine may be able to better serve a user “by ranking results that help “point the way” to what the user is really looking for, or by complementing results from previous queries in the sequence with new results, or in other currently-unanticipated ways.” (Kanoulas, Carterettey, Hallz, Cloughx, & Sanderson, 2011). In 2012, the goal of session track is: (G1) to test whether system performance can be improved for a given query by using previous queries and user interactions with the system (including clicks on ranked results, dwell times, etc.), and (G2) to evaluate system performance over an entire query session instead of a single query. Our UAlbany and USC group joined the Session Track task by taking into account searcher behaviors during the course of their information seeking process. In the following, we give an overview of our approach, details of our submission runs, our results, and our conclusions about the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuanLS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuanLS12,
		author = {Xiaojun Yuan and Jingling Liu and Ning Sa},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {U. Albany {\&} {USC} at the {TREC} 2012 Session Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UAlbany-USC.session.pdf},
		timestamp = {Wed, 22 Dec 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuanLS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BUPT_PRIS at TREC 2012 Session Track

_Chuang Zhang, Xiaotian Wang, Songlin Wen, Runze Li_

- :fontawesome-solid-user-group: **Participant:** [pris411](./participants.md#pris411)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/BUPT_WILDCAT.session.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/BUPT_WILDCAT.session.nb.pdf)
- :material-file-search: **Runs:** [wildcat1.RL1](./runs.md#wildcat1.rl1) | [wildcat1.RL2](./runs.md#wildcat1.rl2) | [wildcat1.RL3](./runs.md#wildcat1.rl3) | [wildcat1.RL4](./runs.md#wildcat1.rl4) | [wildcat2.RL1](./runs.md#wildcat2.rl1) | [wildcat2.RL2](./runs.md#wildcat2.rl2) | [wildcat2.RL3](./runs.md#wildcat2.rl3) | [wildcat2.RL4](./runs.md#wildcat2.rl4) | [wildcat3.RL1](./runs.md#wildcat3.rl1) | [wildcat3.RL2](./runs.md#wildcat3.rl2) | [wildcat3.RL3](./runs.md#wildcat3.rl3) | [wildcat3.RL4](./runs.md#wildcat3.rl4)

??? abstract "Abstract"
	
	In this paper, we introduce our experiments carried out at TREC 2012 session track. Based on the work of our group in TREC 2011 session track, we propose several methods to improve the retrieval performance by considering the user behavior information over the session, which includes use query expansion based on meta data, query expansion based on click order, optimization based on history ranked lists and so on. The results show that some methods can really improve the search performance and some methods need to be optimized.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangWWL12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangWWL12,
		author = {Chuang Zhang and Xiaotian Wang and Songlin Wen and Runze Li},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BUPT{\_}PRIS at {TREC} 2012 Session Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/BUPT\_WILDCAT.session.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangWWL12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

