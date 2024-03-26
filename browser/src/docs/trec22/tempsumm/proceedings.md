# Proceedings - Temporal Summarization 2013 

#### TREC 2013 Temporal Summarization

_Javed A. Aslam, Matthew Ekstrand-Abueg, Virgil Pavlu, Fernando Diaz, Tetsuya Sakai_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/TS.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/TS.OVERVIEW.pdf)
??? abstract "Abstract"
	
	Unexpected news events such as earthquakes or natural disasters represent a unique information access problem where traditional approaches fail. For example, immediately after an event, the corpus may be sparsely populated with relevant content. Even when, after a few hours, relevant content is available, it is often inaccurate or highly redundant. At the same time, crisis events demonstrate a scenario where users urgently need information, especially if they are directly affected by the event. The goal of this track is to develop systems for efficiently monitoring the information associated with an event over time. Specifically, we are interested in developing systems which (1) can broadcast short, relevant, and reliable sentence-length updates about a developing event and (2) can track the value of important event-related attributes (e.g. number of fatalities). The track has the following goals, to develop algorithms which detect sub-events with low latency, to model information reliability in the presence of a dynamic corpus, to understand and address the sensitivity of text summarization algorithms in an online, sequential setting, and to understand and address the sensitivity of information extraction algorithms in dynamic settings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AslamEPDS13.bib) "
	```
	@inproceedings{DBLP:conf/trec/AslamEPDS13,
		author = {Javed A. Aslam and Matthew Ekstrand{-}Abueg and Virgil Pavlu and Fernando Diaz and Tetsuya Sakai},
		editor = {Ellen M. Voorhees},
		title = {{TREC} 2013 Temporal Summarization},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/TS.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AslamEPDS13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at the TREC 2013 Temporal Summarization Track

_Gaurav Baruah, Rakesh Guttikonda, Adam Roegiest, Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/waterloomds-ts.pdf](http://trec.nist.gov/pubs/trec22/papers/waterloomds-ts.pdf)
- :material-file-search: **Runs:** [CosineEgrep](./runs.md#cosineegrep) | [NormEgrep](./runs.md#normegrep) | [UWMDSqlec2t25](./runs.md#uwmdsqlec2t25) | [UWMDSqlec4t50](./runs.md#uwmdsqlec4t50) | [rg1](./runs.md#rg1) | [rg3](./runs.md#rg3) | [rg2](./runs.md#rg2) | [rg4](./runs.md#rg4)

??? abstract "Abstract"
	
	The University of Waterloo participated in the Temporal Summarization Track at TREC 2013 and submitted 8 runs for the Sequential Update Summarization Task. Methods like query likelihood ranking, pseudo relevance feedback, BM25 and cosine similarity, as well as, algorithms for passage retrieval and term expansion using distributional similarity to a set of seed words, were used for returning relevant sentences from a stream of time-ordered documents. Higher scores relative to the average score for all submitted runs were achieved on the Latency Comprehensiveness Metric (returning as many nuggets as possible), however, submitted runs performed poorly on the Expected Latency Gain Metric (speediness of updates).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BaruahGRV13.bib) "
	```
	@inproceedings{DBLP:conf/trec/BaruahGRV13,
		author = {Gaurav Baruah and Rakesh Guttikonda and Adam Roegiest and Olga Vechtomova},
		editor = {Ellen M. Voorhees},
		title = {University of Waterloo at the {TREC} 2013 Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/waterloomds-ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BaruahGRV13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Temporal Summarization Track TREC 2013

_Qian Liu, Yue Liu, Dayong Wu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/ICTNET-ts.pdf](http://trec.nist.gov/pubs/trec22/papers/ICTNET-ts.pdf)
- :material-file-search: **Runs:** [run1](./runs.md#run1) | [run2](./runs.md#run2) | [ValueTask](./runs.md#valuetask)

??? abstract "Abstract"
	
	This paper describes our participation in temporal summarization track of TREC2013. All runs are submitted for both two tasks, namely sequential update summarization task and value tracking task. A real-time framework was proposed based on a trigger model. This model consists of two parts. One is selecting the relevant documents by searching on the document titles. The other is obtaining import sentences to an event. Using the KBA 2013 English-and-unknown-language stream corpus, the experimental results show the effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuLWC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuLWC13,
		author = {Qian Liu and Yue Liu and Dayong Wu and Xueqi Cheng},
		editor = {Ellen M. Voorhees},
		title = {{ICTNET} at Temporal Summarization Track {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/ICTNET-ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuLWC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ZZISTI at TREC2013 Temporal Summarization Track

_Yaoyi Xi, Bicheng Li, Jie Zhou, Yongwang Tang_

- :fontawesome-solid-user-group: **Participant:** [wim_GY_2013](./participants.md#wim_gy_2013)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/wim-ts.pdf](http://trec.nist.gov/pubs/trec22/papers/wim-ts.pdf)
- :material-file-search: **Runs:** [SUS1](./runs.md#sus1) | [VT1](./runs.md#vt1) | [VT2](./runs.md#vt2)

??? abstract "Abstract"
	
	Our team submitted runs for the first running of the TREC Temporal Summarization track. TS Track at TREC2013 contains two tasks, namely Sequential update Summarization and value tracking. Our Systems to each task are described in this paper respectively. In particular, Stanford CoreNLP was applied to extract the event attributes.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XiLZT13.bib) "
	```
	@inproceedings{DBLP:conf/trec/XiLZT13,
		author = {Yaoyi Xi and Bicheng Li and Jie Zhou and Yongwang Tang},
		editor = {Ellen M. Voorhees},
		title = {{ZZISTI} at {TREC2013} Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/wim-ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XiLZT13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HLTCOE at TREC 2013: Temporal Summarization

_Tan Xu, Douglas W. Oard, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [hltcoe](./participants.md#hltcoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/hltcoe-ts.pdf](http://trec.nist.gov/pubs/trec22/papers/hltcoe-ts.pdf)
- :material-file-search: **Runs:** [Baseline](./runs.md#baseline) | [BasePred](./runs.md#basepred) | [EXTERNAL](./runs.md#external) | [TuneExternal2](./runs.md#tuneexternal2) | [TuneBasePred2](./runs.md#tunebasepred2)

??? abstract "Abstract"
	
	Our team submitted runs for the first running of the TREC Temporal Summarization track. We focused on the Sequential Update Summarization task. This task involves simulating processing a temporally ordered stream of over 1 billion documents to identify sentences that are relevant to a specific breaking news stories which contain new and important content. In this paper, we describe our approach and evaluation results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuOM13.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuOM13,
		author = {Tan Xu and Douglas W. Oard and Paul McNamee},
		editor = {Ellen M. Voorhees},
		title = {{HLTCOE} at {TREC} 2013: Temporal Summarization},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/hltcoe-ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuOM13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2013 Temporal Summarization Track

_Zhen Yang, Fei Yao, Huayang Sun, Yun Zhao, Yingxu Lai, Kefeng Fan_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/BJUT-ts.pdf](http://trec.nist.gov/pubs/trec22/papers/BJUT-ts.pdf)
- :material-file-search: **Runs:** [Q0](./runs.md#q0) | [Q1](./runs.md#q1) | [Q2](./runs.md#q2)

??? abstract "Abstract"
	
	This paper describes the first participation of BJUT in the TREC Temporal Summarization Track 2013. Since this is the first track which is held on temporal summarization, the traditional text retrieval framework is introduced to solve the newly emerging temporal summarization problem at first, and the conventional approach is found that it doesn't work without any consideration on extra expansion information to lose the retrieval limits. Therefore, the baseline is improved by considering the expansion information over the summarization, which includes the use of query expansion based on time/similarity factors, summarization based on information clusters and so on. We do not intend to identify specific methods for solutions. Rather a list of method is presented in capabilities where it is anticipated the methods are likely to adapt over time. Surprisingly, we find the traditional text retrieval methods with default parameters, such as tf-idf model, BM25 model, perform very well and can be used in many areas. Meanwhile some expansion information methods, such as k-means, show complex performance and their parameters need to be chosen carefully to achieve better performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYSZLF13.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYSZLF13,
		author = {Zhen Yang and Fei Yao and Huayang Sun and Yun Zhao and Yingxu Lai and Kefeng Fan},
		editor = {Ellen M. Voorhees},
		title = {{BJUT} at {TREC} 2013 Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/BJUT-ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangYSZLF13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Information Extraction Systems of PRIS at Temporal Summarization  Track

_Chunyun Zhang, Weiyan Xu, Fanyu Meng, Hongyan Li, Tong Wu, Lixin Xu_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/PRIS-ts.pdf](http://trec.nist.gov/pubs/trec22/papers/PRIS-ts.pdf)
- :material-file-search: **Runs:** [cluster1](./runs.md#cluster1) | [cluster2](./runs.md#cluster2) | [cluster3](./runs.md#cluster3) | [cluster4](./runs.md#cluster4) | [PRISTS1](./runs.md#prists1) | [PRISTS2](./runs.md#prists2) | [cluster5](./runs.md#cluster5) | [PRISTS3](./runs.md#prists3)

??? abstract "Abstract"
	
	This paper describes the information extraction systems of PRIS at Temporal Summarization Track. The Temporal Summarization Track includes two tasks: sequential update summarization and value tracking. For the first task, we focus attention on keywords mining and sentence scoring. The system utilizes hierarchical Latent Dirichlet Allocation (LDA) to do keywords mining and score sentences with keywords shooting method. For the second task, we define the value extracting as a sequence labeling problem and build a discriminative undirected graph model (CRF model) to extract attribute values of all topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangXMLWX13.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangXMLWX13,
		author = {Chunyun Zhang and Weiyan Xu and Fanyu Meng and Hongyan Li and Tong Wu and Lixin Xu},
		editor = {Ellen M. Voorhees},
		title = {The Information Extraction Systems of {PRIS} at Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/PRIS-ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangXMLWX13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2013: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Web Tracks

_Richard McCreadie, M-Dyaa Albakour, Stuart Mackie, Nut Limsopatham, Craig Macdonald, Iadh Ounis, Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf](http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf)
- :material-file-search: **Runs:** [uogTrNMM](./runs.md#uogtrnmm) | [uogTrNSQ1](./runs.md#uogtrnsq1) | [uogTrEMMQ2](./runs.md#uogtremmq2) | [uogTrNMTm1MM3](./runs.md#uogtrnmtm1mm3) | [uogTrNMTm3FMM4](./runs.md#uogtrnmtm3fmm4)

??? abstract "Abstract"
	
	In TREC 2013, we focus on tackling the challenges posed by the new Contextual Suggestion and Temporal summarisation tracks, as well as enhancing our existing technologies to tackle the new risk-sensitive aspect of the Web track, building upon our Terrier Information Retrieval Platform. In particular, for the Contextual Suggestion track, we investigate how to exploit location-based social networks, with the aim of better identifying venues within a city that a given user might be interested in visiting. For the Temporal Summarisation track, we propose a new summarisation framework and investigate novel techniques to adaptively alter the summarisation strategy over time. For the TREC Web track, we continue to build upon our learning-to-rank approaches and novel xQuAD / Fat frameworks within Terrier, increasing effectiveness when ranking and examining two new approaches to risk-sensitive retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieAMLMOD13.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieAMLMOD13,
		author = {Richard McCreadie and M{-}Dyaa Albakour and Stuart Mackie and Nut Limsopatham and Craig Macdonald and Iadh Ounis and Bekir Taner Din{\c{c}}er},
		editor = {Ellen M. Voorhees},
		title = {University of Glasgow at {TREC} 2013: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Web Tracks},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieAMLMOD13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

