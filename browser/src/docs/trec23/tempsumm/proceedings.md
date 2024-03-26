# Proceedings - Temporal Summarization 2014 

#### TREC 2014 Temporal Summarization Track Overview

_Javed A. Aslam, Matthew Ekstrand-Abueg, Virgil Pavlu, Fernando Diaz, Richard McCreadie, Tetsuya Sakai_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/overview-tempsumm.pdf](http://trec.nist.gov/pubs/trec23/papers/overview-tempsumm.pdf)
??? abstract "Abstract"
	
	News events such as protests, accidents or natural disasters represent a unique information access problem where traditional approaches fail. For example, immediately after an event, the corpus may be sparsely populated with relevant content. Even when, after a few hours, relevant content becomes available, it is often inaccurate or highly redundant. At the same time, crisis events demonstrate a scenario where users urgently need information, especially if they are directly affected by the event. The goal of this track is to develop systems for efficiently monitoring the information associated with an event over time. Specifically, we are interested in developing systems which can broadcast short, relevant, and reliable sentence-length updates about a developing event. The track has the following four main aims: To develop algorithms which detect sub-events with low latency, To model information reliability in the presence of a dynamic corpus, To understand and address the sensitivity of text summarization algorithms in an online, sequential setting, and To understand and address the sensitivity of information extraction algorithms in dynamic settings. The remainder of this overview is structured as follows. Section 2 describes the temporal summarization task in detail. In Section 3, we discuss the corpus of documents from which the summaries are produced, while in Section 4, we discuss how temporal summarization systems are evaluated within the track. Section 5 details the process via which sentence updates were assessed. Finally, in Section 6, we summarize the performance of the participant systems to the 2014 track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AslamEPDMS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/AslamEPDMS14,
		author = {Javed A. Aslam and Matthew Ekstrand{-}Abueg and Virgil Pavlu and Fernando Diaz and Richard McCreadie and Tetsuya Sakai},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2014 Temporal Summarization Track Overview},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/overview-tempsumm.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AslamEPDMS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Temporal Summarization 2014

_Rafik Abbes, Karen Pinel-Sauvagnat, Nathalie Hernandez, Mohand Boughanem_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-IRIT_ts.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-IRIT_ts.pdf)
- :material-file-search: **Runs:** [KW30H5NW3600](./runs.md#kw30h5nw3600) | [KW30H5NW300](./runs.md#kw30h5nw300) | [KW80H5NW300](./runs.md#kw80h5nw300) | [KW80H5NW3600](./runs.md#kw80h5nw3600) | [KW80H10NW300](./runs.md#kw80h10nw300) | [KW30H10NW300](./runs.md#kw30h10nw300)

??? abstract "Abstract"
	
	This paper describes the IRIT lab participation to the 2014 TREC Temporal Summarization track. The goal of the Temporal Summarization track is to develop systems that allow users to efficiently monitor information about events over time. Our proposed method selects relevant documents that are more likely to concern the event, and extracts relevant and novel sentences based on some filters. Obtained results are presented and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbbesPHB14a.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbbesPHB14a,
		author = {Rafik Abbes and Karen Pinel{-}Sauvagnat and Nathalie Hernandez and Mohand Boughanem},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IRIT} at {TREC} Temporal Summarization 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-IRIT\_ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AbbesPHB14a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Temporal Summarization Track TREC 2014

_Lei Chen, Hainan Zhang, Siying Li, Zhiyuan Ji, Qian Liu, Yue Liu, Dayong Wu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_ts.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_ts.pdf)
- :material-file-search: **Runs:** [run1](./runs.md#run1) | [run4](./runs.md#run4) | [run3](./runs.md#run3) | [run2](./runs.md#run2)

??? abstract "Abstract"
	
	Temporal Summarization task is a standard Information Retrieval problem. The goal of the task is to generate sequential update summarization, which are useful, new and timely sentence length updates about a developing event [1]. The event refers to a temporally acute topic, and each topic contains the start time and end time. There are more event types than the last year. They are accident, bombing, hostage, impact event, protest, riot, shooting and storm. Formally, given the time ordered corpus, the query and the relevant time range, our system outputs a list of relevant sentence identifiers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenZLJLLWC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenZLJLLWC14,
		author = {Lei Chen and Hainan Zhang and Siying Li and Zhiyuan Ji and Qian Liu and Yue Liu and Dayong Wu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Temporal Summarization Track {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET\_ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenZLJLLWC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Information Extraction systems of BUPT_PRIS at TREC2014 Temporal  Summarization Track

_Yuanyuan Qi, Qinlong Wang, Chuchu Huang, Bo Tang, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [BUPT_PRIS](./participants.md#bupt_pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BUPT_PRIS_ts.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BUPT_PRIS_ts.pdf)
- :material-file-search: **Runs:** [Cluster1](./runs.md#cluster1) | [Cluster2](./runs.md#cluster2) | [Cluster3](./runs.md#cluster3) | [Cluster4](./runs.md#cluster4)

??? abstract "Abstract"
	
	This paper describes the information extraction systems of BUPT_PRIS at Temporal Summarization Track, Which includes data obtaining and preprocessing, index building and query expansion, sentences scoring module. This year only keep one task: sequential update summarization, the task: value tracking is cancelled. For the sequential update summarization we focus attention on queries expansion and sentence scoring. There are three methods of query expansion introduced in this report: WordNets, Word representation, spatial analysis method. We also show the evaluation results for our team and the comparison with the best and median evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiWHTXCG14.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiWHTXCG14,
		author = {Yuanyuan Qi and Qinlong Wang and Chuchu Huang and Bo Tang and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The Information Extraction systems of BUPT{\_}PRIS at {TREC2014} Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BUPT\_PRIS\_ts.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiWHTXCG14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2014 Temporal Summarization Track

_Yun Zhao, Fei Yao, Huayang Sun, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BJUT_ts.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BJUT_ts.pdf)
- :material-file-search: **Runs:** [Q0](./runs.md#q0) | [Q2](./runs.md#q2) | [Q1](./runs.md#q1)

??? abstract "Abstract"
	
	This paper describes the second participation of BJUT in the temporal summarization track. We performed the experiments on the TREC KBA 2014 stream corpus using the classic information retrieval models, such as BM25, vector space model. Also, we introduce the details of our system, which consists of corpus pre-processing, information retrieval module and information process module.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoYSY14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoYSY14,
		author = {Yun Zhao and Fei Yao and Huayang Sun and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2014 Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BJUT\_ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoYSY14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2014: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Web Tracks

_Richard McCreadie, Romain Deveaud, M-Dyaa Albakour, Stuart Mackie, Nut Limsopatham, Craig Macdonald, Iadh Ounis, Thibaut Thonet, Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-uogTr_cs-ts-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-uogTr_cs-ts-web.pdf)
- :material-file-search: **Runs:** [uogTr4ARas](./runs.md#uogtr4aras) | [uogTr2A](./runs.md#uogtr2a) | [uogTr4A](./runs.md#uogtr4a) | [uogTr4AC](./runs.md#uogtr4ac)

??? abstract "Abstract"
	
	In TREC 2014, we focus on tackling the challenges posed by the Contextual Suggestion and Temporal Summarisation tracks, as well as enhancing our existing technologies to tackle risk-sensitivity as part of the Web track, building upon our Terrier Information Retrieval Platform. In particular, for the Contextual Suggestion track, we propose a novel bundled venue retrieval approach and experiment with text-based summarisation for building the venue description. For our participation to the Temporal Summarisation track, we propose a general framework for performing summarisation over time and two new real-time filtering approaches that leverage the semi-structured nature of news articles to enhance summary coverage. For the TREC Web track, we investigated a novel risk-sensitive learning to rank approach that is based on hypothesis testing and examined approaches that selectively apply different retrieval techniques based upon the query, with the aim of minimising risk.
	

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

