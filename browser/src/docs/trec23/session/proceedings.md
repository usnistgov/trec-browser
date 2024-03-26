# Proceedings - Session 2014 

#### Overview of the TREC 2014 Session Track

_Ben Carterette, Evangelos Kanoulas, Mark M. Hall, Paul D. Clough_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/overview-session.pdf](http://trec.nist.gov/pubs/trec23/papers/overview-session.pdf)
??? abstract "Abstract"
	
	The TREC Session track ran for the fourth time in 2014. The track has the primary goal of providing test collections and evaluation measures for studying information retrieval over user sessions rather than one-time queries. These test collections are meant to be portable, reusable, statistically powerful, and open to anyone that wishes to work on the problem of retrieval over sessions. The experimental design of the track was similar to that of the previous three years [5, 6, 1]: sessions were real user sessions with a search engine that include queries, retrieved results, clicks, and dwell times; retrieval tasks were designed to study the effect of using session data in retrieval for only the mth query in a session. For the 2014 track, sessions were obtained from workers on Amazon's Mechanical Turk. As a result, the 2014 data includes far more sessions than previous years—1,257 unique sessions as compared to around 100 for each of the previous three years. Apart from that, there is little different from the 2013 track [1]. This overview is organized as follows: in Section 2 we describe the tasks participants were to perform. In Section 3 we describe the corpus, topics, and sessions that comprise the test collection. Section 4 gives some information about submitted runs. In Section 5 we describe relevance judging and evaluation measures, and Sections 6 present evaluation results and analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarteretteKHC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarteretteKHC14,
		author = {Ben Carterette and Evangelos Kanoulas and Mark M. Hall and Paul D. Clough},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2014 Session Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/overview-session.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarteretteKHC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SIRA: TREC Session Track 2014

_Brennan Bushee, Drew Pintus, Patrick Smith, Sharon Gower Small_

- :fontawesome-solid-user-group: **Participant:** [SCIAITeam](./participants.md#sciaiteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-SCIAITeam_session.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-SCIAITeam_session.pdf)
- :material-file-search: **Runs:** [SCIAITeamF.RL1](./runs.md#sciaiteamf.rl1) | [SCIAITeamF.RL2](./runs.md#sciaiteamf.rl2) | [SCIAITeamC.RL1](./runs.md#sciaiteamc.rl1) | [SCIAITeamC.RL2](./runs.md#sciaiteamc.rl2) | [SCIAITeamL.RL1](./runs.md#sciaiteaml.rl1) | [SCIAITeamL.RL2](./runs.md#sciaiteaml.rl2)

??? abstract "Abstract"
	
	This paper discusses Siena's Interactive Research Assistant's (SIRA) participation in the Text Retrieval Conference (TREC) Session Track of 2014. The overall goal of this track is to improve search results during query sessions based on a user's behavior. Query sessions include many aspects of a search, including query topics, initial retrieved webpages, clicked on links, visit times, etc. SIRA has used several methods to improve search results that will be discussed in this paper. Each method of query expansion utilized clicked-on and non-clicked-on links, pages with the longest visited time, and N-Percent (N%) of each page. Two of our three submissions improved over our baseline results and both of these were equal to the median submission for all participants in the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BusheePSS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/BusheePSS14,
		author = {Brennan Bushee and Drew Pintus and Patrick Smith and Sharon Gower Small},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{SIRA:} {TREC} Session Track 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-SCIAITeam\_session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BusheePSS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC WEB 2014: Entity Query Feature Expansion using Knowledge  Base Links

_Laura Dietz, Patrick Verga_

- :fontawesome-solid-user-group: **Participant:** [UMASS_CIIR](./participants.md#umass_ciir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UMASS_CIIR_session.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UMASS_CIIR_session.pdf)
- :material-file-search: **Runs:** [UMASS1.RL1](./runs.md#umass1.rl1) | [UMASS1.RL2](./runs.md#umass1.rl2) | [UMASS1.RL3](./runs.md#umass1.rl3) | [UMASS2.RL1](./runs.md#umass2.rl1) | [UMASS2.RL2](./runs.md#umass2.rl2) | [UMASS2.RL3](./runs.md#umass2.rl3) | [UMASS3.RL1](./runs.md#umass3.rl1) | [UMASS3.RL2](./runs.md#umass3.rl2) | [UMASS3.RL3](./runs.md#umass3.rl3) | [UMASS4.RL1](./runs.md#umass4.rl1) | [UMASS4.RL2](./runs.md#umass4.rl2) | [UMASS4.RL3](./runs.md#umass4.rl3)

??? abstract "Abstract"
	
	Entity linking tools predict links between entity mentions in text and knowledge base entries. In this work we leverage the rich semantic knowledge available through these links to understand relevance of documents for a query. We focus on the ad hoc task on the category A subset and demonstrate the benefit of entity-centric approaches even for non-entity queries like “dark chocolate health benefits”.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DietzV14.bib) "
	```
	@inproceedings{DBLP:conf/trec/DietzV14,
		author = {Laura Dietz and Patrick Verga},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UMass at {TREC} {WEB} 2014: Entity Query Feature Expansion using Knowledge Base Links},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UMASS\_CIIR\_session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DietzV14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Endicott College at 2014 TREC Session Track

_Henry Feild_

- :fontawesome-solid-user-group: **Participant:** [Endicott](./participants.md#endicott)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-Endicott-session.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-Endicott-session.pdf)
- :material-file-search: **Runs:** [ECxCGxPRF.RL1](./runs.md#ecxcgxprf.rl1) | [ECxCGxPRF.RL2](./runs.md#ecxcgxprf.rl2) | [ECxCGxPRF.RL3](./runs.md#ecxcgxprf.rl3) | [ECxSRMxOS.RL1](./runs.md#ecxsrmxos.rl1) | [ECxSRMxOS.RL2](./runs.md#ecxsrmxos.rl2) | [ECxSRMxOS.RL3](./runs.md#ecxsrmxos.rl3) | [ECxSRMxPRF.RL1](./runs.md#ecxsrmxprf.rl1) | [ECxSRMxPRF.RL2](./runs.md#ecxsrmxprf.rl2) | [ECxSRMxPRF.RL3](./runs.md#ecxsrmxprf.rl3)

??? abstract "Abstract"
	
	Endicott College submitted three runs to Task 1 of the 2014 TREC Session Track. All runs reranked the baseline runs provided by the track organizers. One of the runs made use of a click graph to re-rank results for RL1, RL2, and RL3. The other two used relevance models computed over snippets from the session, and boosted their RL3 run using click graph recommendations. In the absence of clicks (e.g., RL1 and clickless sessions in RL2 and RL3), two of the runs used pseudo relevance feedback over the session, while the other used the unmodified baseline ranking. All runs used a similar pre-processing procedure, which we describe in Section 2. We then discuss our click graph re-ranking technique for the ECxCGxPRF run in Section 3 and the session relevance modeling technique for our ECxSRMxOS and ECxSRMxPRF runs in Section 4. We follow that with an analysis of the performance of our runs compared to each other, as well as the track minimums, medians, and maximums. Finally, we wrap up with some closing thoughts and future directions in Section 6.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Feild14.bib) "
	```
	@inproceedings{DBLP:conf/trec/Feild14,
		author = {Henry Feild},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Endicott College at 2014 {TREC} Session Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-Endicott-session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Feild14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Modeling Rich Interactions in Session Search - Georgetown University  at TREC 2014 Session Track

_Jiyun Luo, Xuchu Dong, Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [Georgetown](./participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-Georgetown_session.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-Georgetown_session.pdf)
- :material-file-search: **Runs:** [GUS14Run2.RL3](./runs.md#gus14run2.rl3) | [GUS14Run2.RL1](./runs.md#gus14run2.rl1) | [GUS14Run2.RL2](./runs.md#gus14run2.rl2) | [GUS14Run3.RL1](./runs.md#gus14run3.rl1) | [GUS14Run3.RL2](./runs.md#gus14run3.rl2) | [GUS14Run3.RL3](./runs.md#gus14run3.rl3) | [GUS14Run1.RL1](./runs.md#gus14run1.rl1) | [GUS14Run1.RL2](./runs.md#gus14run1.rl2) | [GUS14Run1.RL3](./runs.md#gus14run1.rl3)

??? abstract "Abstract"
	
	This year we participate in the TREC Session Track Task 1. We adopt the Query Change Model (QCM), weighted QCM, re-ranking, clustering, and error analysis in our approaches. The QCM retrieval model is employed to combine all queries in a session. QCM allows documents that are relevant to any query in a session to appear in the final retrieval list. Weighted QCM combines queries unevenly based on a prediction of query quality. It is based on the following intuition: if a query does not bring any document that leads to a SAT-Click from the user, it suggests that this query is poorly formed. Our re-ranking module is based on implicit feedback from the user; in this case the SAT-Clicked documents. The module boosts a document's ranking position if it has been SAT-Clicked in the session or in other sessions that share similar search topics. We apply K-means clustering algorithm to detect which sessions share similar search topics. Each unique term is one dimension of the vector and is weighted by its idf. We also apply session error analysis in RL3. From the query log, we first identify sessions with similar topics by clustering, then we use SAT-Clicks from most sessions to re-rank the documents for the sessions that the algorithm predicts as poorly issued sessions, i.e. more difficult session due to ill-form queries. Combining above approaches, we achieve a 20.9% nDCG@10 increment and a 13.0% P@10 increment from RL1 to RL2, and with utilization of the whole log data, we achieve a 4% nDCG@10 increment and a 0.5% P@10 increment from RL2 to RL3.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuoDY14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuoDY14,
		author = {Jiyun Luo and Xuchu Dong and Hui Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Modeling Rich Interactions in Session Search - Georgetown University at {TREC} 2014 Session Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-Georgetown\_session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuoDY14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Session Track TREC2014

_Yuanhai Xue, Guoxin Cui, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_session.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_session.pdf)
- :material-file-search: **Runs:** [ICTNET14SER1.RL1](./runs.md#ictnet14ser1.rl1) | [ICTNET14SER1.RL2](./runs.md#ictnet14ser1.rl2) | [ICTNET14SER1.RL3](./runs.md#ictnet14ser1.rl3) | [ICTNET14SER2.RL1](./runs.md#ictnet14ser2.rl1) | [ICTNET14SER2.RL2](./runs.md#ictnet14ser2.rl2) | [ICTNET14SER2.RL3](./runs.md#ictnet14ser2.rl3) | [ICTNET14SER3.RL1](./runs.md#ictnet14ser3.rl1) | [ICTNET14SER3.RL2](./runs.md#ictnet14ser3.rl2) | [ICTNET14SER3.RL3](./runs.md#ictnet14ser3.rl3)

??? abstract "Abstract"
	
	In this paper, we describe our solutions of the Session Track at TREC 2014. Our main idea is to re-rank the documents the official supplies as RL1. In order to get good results of the re-ranked documents, we implement the learning to rank model which needs to extract some features. We use the relevance judgments of Session Track TREC 2013 as training set this year and also we use it as testing set by 5-fold cross-validation. The rest of this paper is organized as follows. We detail our models in section 2. Section 3 describes our experiments, including our evaluation results. Conclusions are made in the last session.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XueCYLC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/XueCYLC14,
		author = {Yuanhai Xue and Guoxin Cui and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Session Track {TREC2014}},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET\_session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XueCYLC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Delaware at TREC 2014

_Ashraf Bah, Karankumar Sabhnani, Mustafa Zengin, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [udel](./participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf)
- :material-file-search: **Runs:** [udelitu.RL1](./runs.md#udelitu.rl1) | [udel14Run1.RL3](./runs.md#udel14run1.rl3) | [udel14Run1.RL1](./runs.md#udel14run1.rl1)

??? abstract "Abstract"
	
	This paper describes the work of the Information Retrieval Lab at the University of Delaware (team name “udel”) on TREC 2014 tracks. We participated in five different tracks: Contextual Suggestion, Federated Web, Microblog, Session, and Web.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BahSZC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/BahSZC14,
		author = {Ashraf Bah and Karankumar Sabhnani and Mustafa Zengin and Ben Carterette},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Delaware at {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_cs-federated-microblog-web-sesson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BahSZC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2014: Web, Session, and Contextual Suggestion Tracks

_Matthias Hagen, Steve Goering, Maximilian Michel, Georg Müller, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [BUW](./participants.md#buw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BUW_cs-session-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BUW_cs-session-web.pdf)
- :material-file-search: **Runs:** [webis2014act.RL1](./runs.md#webis2014act.rl1) | [webis2014act.RL2](./runs.md#webis2014act.rl2) | [webis2014act.RL3](./runs.md#webis2014act.rl3) | [webis2014db.RL2](./runs.md#webis2014db.rl2) | [webis2014db.RL3](./runs.md#webis2014db.rl3) | [webis2014db.RL1](./runs.md#webis2014db.rl1) | [webisSt14ax.RL3](./runs.md#webisst14ax.rl3) | [webisSt14ax.RL1](./runs.md#webisst14ax.rl1) | [webisSt14ax.RL2](./runs.md#webisst14ax.rl2)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2014 Web, Session and Contex tual Suggestion tracks. All our runs for the Web and the Session track are on the full ClueWeb12 and use the online Indri retrieval system hosted at CMU. Our runs for the Contextual Suggestion track are based on the open web. As for the Web track, our runs are aimed at one research question: whether using axioms for re-ranking a baseline result list improve the retrieval performance. Therefore, we implement the axioms available in the axiomatic IR literature and combine them with new axioms aimed at term proximity. Trained on the TREC 2013 Web track data, three promising combinations of axioms are identified in a large-scale experiment and used for our three runs. As for the session track, we tackle three research questions in three different runs. First, similar to the Web track, we examine whether an axiom combination helps to improve session retrieval. Second, we examine the effect of presenting relevant documents from previous years when they seem to be related to the current queries of the 2014 data. Our third question is whether the user interactions can be used to train an activation model to predict relevant documents for new queries. As for the contextual suggestion track, our research question is whether explanations based on the user profile and explaining why specific entities are suggested by the system are perceived positively or negatively by the user. Our focus is not explicitly on finding the most relevant suggestions but rather on examining the effect of different descriptions. Thus, the system for finding the suggestions is simply based on techniques shown promising in the previous years. Our first run uses “standard” descriptions while in the second run the standard description is enriched by a profile specific sentence explaining the reasoning underlying the suggestion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenGMMS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenGMMS14,
		author = {Matthias Hagen and Steve Goering and Maximilian Michel and Georg M{\"{u}}ller and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2014: Web, Session, and Contextual Suggestion Tracks},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BUW\_cs-session-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenGMMS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

