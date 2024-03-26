# Proceedings - Web 2014 

#### TREC 2014 Web Track Overview

_Kevyn Collins-Thompson, Craig Macdonald, Paul N. Bennett, Fernando Diaz, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/overview-web.pdf](http://trec.nist.gov/pubs/trec23/papers/overview-web.pdf)
??? abstract "Abstract"
	
	The goal of the TREC Web track over the past few years has been to explore and evaluate innovative retrieval approaches over large-scale subsets of the Web - currently using ClueWeb12, on the order of one billion pages. For TREC 2014, the sixth year of the Web track, we implemented the following significant updates compared to 2013. First, the risk-sensitive retrieval task was modified to assess the ability of systems to adaptively perform risk-sensitive retrieval against multiple baselines, including an optional self-provided baseline. In general, the risk-sensitive task explores the tradeoffs that systems can achieve between effectiveness (overall gains across queries) and robustness (minimizing the probability of significant failure, relative to a particular provided baseline). Second, we added query performance prediction as an optional aspect of the risk-sensitive task. The Adhoc task continued as for TREC 2013, evaluated using both adhoc and diversity rel- evance criteria. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Collins-Thompson14.bib) "
	```
	@inproceedings{DBLP:conf/trec/Collins-Thompson14,
		author = {Kevyn Collins{-}Thompson and Craig Macdonald and Paul N. Bennett and Fernando Diaz and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2014 Web Track Overview},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/overview-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Collins-Thompson14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SNUMedinfo at TREC Web track 2014

_Sungbin Choi, Jinwook Choi_

- :fontawesome-solid-user-group: **Participant:** [SNUMedinfo](./participants.md#snumedinfo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-SNUMedinfo_web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-SNUMedinfo_web.pdf)
- :material-file-search: **Runs:** [SNUMedinfo11](./runs.md#snumedinfo11) | [SNUMedinfo12](./runs.md#snumedinfo12) | [SNUMedinfo13](./runs.md#snumedinfo13)

??? abstract "Abstract"
	
	This paper describes the participation of the SNUMedinfo team at the TREC Web track 2014. This is the first time we participate in the Web track. Rather than applying more sophisticated retrieval method such as learning to rank models, this year we used only baseline retrieval models with spam filtering and pagerank prior
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChoiC14a.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChoiC14a,
		author = {Sungbin Choi and Jinwook Choi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {SNUMedinfo at {TREC} Web track 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-SNUMedinfo\_web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChoiC14a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2014: Web, Session, and Contextual Suggestion Tracks

_Matthias Hagen, Steve Goering, Maximilian Michel, Georg Müller, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [BUW](./participants.md#buw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BUW_cs-session-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BUW_cs-session-web.pdf)
- :material-file-search: **Runs:** [webisWt14axAll](./runs.md#webiswt14axall) | [webisWt14axMax](./runs.md#webiswt14axmax) | [webisWt14axSyn](./runs.md#webiswt14axsyn)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2014 Web, Session and Contextual Suggestion tracks. All our runs for the Web and the Session track are on the full ClueWeb12 and use the online Indri retrieval system hosted at CMU. Our runs for the Contextual Suggestion track are based on the open web. As for the Web track, our runs are aimed at one research question: whether using axioms for re-ranking a baseline result list improve the retrieval performance. Therefore, we implement the axioms available in the axiomatic IR literature and combine them with new axioms aimed at term proximity. Trained on the TREC 2013 Web track data, three promising combinations of axioms are identified in a large-scale experiment and used for our three runs. As for the session track, we tackle three research questions in three different runs. First, similar to the Web track, we examine whether an axiom combination helps to improve session retrieval. Second, we examine the effect of presenting relevant documents from previous years when they seem to be related to the current queries of the 2014 data. Our third question is whether the user interactions can be used to train an activation model to predict relevant documents for new queries. As for the contextual suggestion track, our research question is whether explanations based on the user profile and explaining why specific entities are suggested by the system are perceived positively or negatively by the user. Our focus is not explicitly on finding the most relevant suggestions but rather on examining the effect of different descriptions. Thus, the system for finding the suggestions is simply based on techniques shown promising in the previous years. Our first run uses “standard” descriptions while in the second run the standard description is enriched by a profile specific sentence explaining the reasoning underlying the suggestion.
	

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

#### Venue Recommendation and Web Search Based on Anchor Text

_Seyyed Hadi Hashemi, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UAmsterdam_cs-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UAmsterdam_cs-web.pdf)

??? abstract "Abstract"
	
	This paper presents the University of Amsterdam's participation in TREC 2014. For the Contextual Suggestion Track, we experimented with the use of anchor text representations in the language modeling framework, and base our runs either on full ClueWeb12 or the subset of touristic aggregators (e.g., tripadvisor) provided by the organizers of the track. We also look at the effectiveness of priors (in particular, PageRank) and ways of formulating the query based on the context. Our main finding is that the anchor text representation is effective for retrieving candidate attractions, and performs better than a standard document text index. A linear combination of both anchor and document text leads to further improvement. For the Web Track, we continued our experiment with the fusion of anchor text relative to the text-based baseline run. Our main finding is, again, that the combination of anchor and document text leads to improvement, and we demonstrate how the fusion weight can be used as a handle to tune the amount of risk acceptable for the risk sensitive evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HashemiK14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HashemiK14,
		author = {Seyyed Hadi Hashemi and Jaap Kamps},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Venue Recommendation and Web Search Based on Anchor Text},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UAmsterdam\_cs-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HashemiK14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Entity Came to Rescue - Leveraging Entities to Minimize Risks in Web  Search

_Xitong Liu, Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_web.pdf)
- :material-file-search: **Runs:** [UDInfoWebLES](./runs.md#udinfowebles) | [UDInfoWebENT](./runs.md#udinfowebent) | [UDInfoWebAX](./runs.md#udinfowebax) | [UDInfoWebRiskRM](./runs.md#udinfowebriskrm) | [UDInfoWebRiskTR](./runs.md#udinfowebrisktr) | [UDInfoWebRiskAX](./runs.md#udinfowebriskax)

??? abstract "Abstract"
	
	We present the summary of our work in the TREC 2014 Web Track. We participated both the ad hoc task and risk-sensitive task and explored two entity-based approaches to evaluate the performance of leveraging entities to improve retrieval effectiveness and robustness. Our proposed approaches are based on the integration of related entities of queries and the entity model from knowledge base to the retrieval model. The first approach is called as entity-centric query expansion, in which we integrate the related entities into the original query model to perform query expansion. Documents are then retrieved based on the expanded query model. In the second approach, we leverage the publicly available Freebase annotation on ClueWeb12 as well as Freebase API to estimate the entity model. It is called Latent Entity Space (LES), in which we model the relevance between query and document in a latent space. Each dimension of the latent space is represented by an entity and the query-document relevance is estimated based on their projections to each dimension. The evaluation results on ad hoc task show that entities can indeed bring further improvements on the performance of Web document retrieval when combined with axiomatic retrieval model with semantic expansion, one of the state-of-the-art methods. Furthermore, results on risk-sensitive task demonstrate that our proposed model also have advantage on minimizing the retrieval risk.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuYF14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuYF14,
		author = {Xitong Liu and Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Entity Came to Rescue - Leveraging Entities to Minimize Risks in Web Search},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_fang\_web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuYF14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2014: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Web Tracks

_Richard McCreadie, Romain Deveaud, M-Dyaa Albakour, Stuart Mackie, Nut Limsopatham, Craig Macdonald, Iadh Ounis, Thibaut Thonet, Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-uogTr_cs-ts-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-uogTr_cs-ts-web.pdf)
- :material-file-search: **Runs:** [uogTrDwl](./runs.md#uogtrdwl) | [uogTrIwa](./runs.md#uogtriwa) | [uogTrq1](./runs.md#uogtrq1) | [uogTrDwsts](./runs.md#uogtrdwsts) | [uogTrDuax](./runs.md#uogtrduax) | [uogTrBwf](./runs.md#uogtrbwf)

??? abstract "Abstract"
	
	In TREC 2014, we focus on tackling the challenges posed by the Contextual Suggestion and Temporal Summarisation tracks, as well as enhancing our existing technologies to tackle risk-sensitivity as part of the Web track, building upon our Terrier Information Retrieval Platform. In particular, for the Contextual Suggestion track, we propose a novel bundled venue retrieval approach and experiment with text-based summarisation for building the venue description. For our participation to the Temporal Summarisation track, we propose a general framework for performing summarisa- tion over time and two new real-time filtering approaches that leverage the semi-structured nature of news articles to enhance summary coverage. For the TREC Web track, we investigated a novel risk-sensitive learning to rank approach that is based on hypothesis testing and examined approaches that selectively apply different retrieval techniques based upon the query, with the aim of minimising risk.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieDAMLMO14.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieDAMLMO14,
		author = {Richard McCreadie and Romain Deveaud and M{-}Dyaa Albakour and Stuart Mackie and Nut Limsopatham and Craig Macdonald and Iadh Ounis and Thibaut Thonet and Bekir Taner Din{\c{c}}er},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow at {TREC} 2014: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Web Tracks},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-uogTr\_cs-ts-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieDAMLMO14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track TREC2014

_Yuanhai Xue, Xiaoming Yu, Feng Guan, Xi-Peng Li, Man Du, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_web.pdf)
- :material-file-search: **Runs:** [ICTNET14ADR3](./runs.md#ictnet14adr3) | [ICTNET14ADR1](./runs.md#ictnet14adr1) | [ICTNET14ADR2](./runs.md#ictnet14adr2) | [ICTNET14RSR1](./runs.md#ictnet14rsr1) | [ICTNET14RSR2](./runs.md#ictnet14rsr2) | [ICTNET14RSR3](./runs.md#ictnet14rsr3)

??? abstract "Abstract"
	
	An ad-hoc task in TREC investigates the performance of systems that search a static set of documents using previously-unseen topics. This year, the ClueWeb12[1] dataset are used. The overall goal of the risk-sensitive task is to explore algorithms and evaluation methods for systems that try to jointly maximize an average effectiveness measure across queries, while minimizing effectiveness losses with respect to a provided baseline. Two baselines from different IR systems are supplied this year in order to understand the nature of risk-reward tradeoffs achievable by a system that can adapt to different baselines. The rest of this paper is organized as follows. In Section 2, we discuss the processing of ClueWeb12, derived data and external resources. In Section 3, the BM25 model with term proximity, the diversification method and the results fusion strategy are introduced. We report experimental results and the corresponding re-ranking strategy in Section 4. Finally, our work is concluded in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XueYGLDLC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/XueYGLDLC14,
		author = {Yuanhai Xue and Xiaoming Yu and Feng Guan and Xi{-}Peng Li and Man Du and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Web Track {TREC2014}},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET\_web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XueYGLDLC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Delaware at TREC 2014

_Ashraf Bah, Karankumar Sabhnani, Mustafa Zengin, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [udel](./participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf)
- :material-file-search: **Runs:** [udel_itu](./runs.md#udel_itu) | [udel_itub](./runs.md#udel_itub) | [udelCombCAT2](./runs.md#udelcombcat2)

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

#### Towards a Simple and Efficient Web Search Framework

_Di Xu, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [Group.Xu](./participants.md#group.xu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-Group.Xu_web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-Group.Xu_web.pdf)
- :material-file-search: **Runs:** [Zerg](./runs.md#zerg) | [Terran](./runs.md#terran) | [Protoss](./runs.md#protoss)

??? abstract "Abstract"
	
	The Web Track of 2014 Text REtrieval Conference (TREC) addresses the most fundamental problem of Information Retrieval. We did not intend to craft a system that beats the state-of-the-art search engines, but to design a light weight and cost-effective system with comparable performances. We introduce a two-pass retrieval framework, with the first pass consisting of a simple and efficient retrieval model that focuses on recall, and the second pass a wave of feature extraction algorithms run on the set of top ranked documents, followed by Learning to Rank (LETOR) algorithms that provide different precision oriented rankings, and their outputs are combined using data fusion. We have focused on using statistical Language Models with novel and well-known smoothing techniques, different LETOR methods, and various data fusion techniques. In addition, we have also tried using topic modelling with Hierarchical Dirichlet Allocation for query expansion in the hope of improving diversity of our results. However, the topic modelling approach has turned out to be unsuccessful, and we have not been able to spot the problem and benefit from it in this work. In addition, we also present some further analyses demonstrating that our approach is robust against overfitting, and some general studies on overfitting in the context of LETOR.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuC14a.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuC14a,
		author = {Di Xu and Jamie Callan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Towards a Simple and Efficient Web Search Framework},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-Group.Xu\_web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuC14a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Two selfless contributions to web search evaluation

_Djoerd Hiemstra, Robin Aly_

- :fontawesome-solid-user-group: **Participant:** [ut](./participants.md#ut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ut_web-federated.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ut_web-federated.pdf)
- :material-file-search: **Runs:** [utexact](./runs.md#utexact) | [utbase](./runs.md#utbase)

??? abstract "Abstract"
	
	We present our results for the Web Search track and the Federated Web Search track for the 23rd Text Retrieval Conference TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HiemstraA14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HiemstraA14,
		author = {Djoerd Hiemstra and Robin Aly},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Two selfless contributions to web search evaluation},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ut\_web-federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HiemstraA14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

