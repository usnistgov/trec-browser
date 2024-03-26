# Proceedings - Microblog 2014 

#### Overview of the TREC-2014 Microblog Track

_Jimmy Lin, Yulu Wang, Miles Efron, Garrick Sherman_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec23/papers/overview-microblog.pdf](https://trec.nist.gov/pubs/trec23/papers/overview-microblog.pdf)
??? abstract "Abstract"
	
	This year represents the fourth iteration of the TREC Microblog track, which has been running since 2011. The track continued using the “evaluation as a service” model [8, 7], in which participants had access to the document collection only through an API. In addition to the temporally-anchored ad hoc retrieval task, which has been running since the inception of the track, we introduced a new task called tweet timeline generation (TTG), where the goal is to produce concise “summaries” about a particular topic for human consumption. Although this overview covers both tasks, more emphasis is placed on the tweet timeline generation task, which necessitated the development of a new evaluation methodology. We refer the reader to previous track overview papers [8, 12, 9] for details on the setup of the ad hoc task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinWES14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinWES14,
		author = {Jimmy Lin and Yulu Wang and Miles Efron and Garrick Sherman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC-2014} Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {https://trec.nist.gov/pubs/trec23/papers/overview-microblog.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinWES14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Microblog Track in TREC 2014

_Guoxin Cui, Fabin Shi, Xiaolei Liu, Xiaobo Hao, Xueke Xu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_microblog.pdf)
- :material-file-search: **Runs:** [ICTNETRUN1](./runs.md#ictnetrun1) | [ICTNETRUN2](./runs.md#ictnetrun2) | [ICTNETRUN3](./runs.md#ictnetrun3) | [ICTNETRUN4](./runs.md#ictnetrun4) | [ICTNETRUNSP4](./runs.md#ictnetrunsp4) | [ICTNETRunSP3](./runs.md#ictnetrunsp3) | [ICTNETAP3](./runs.md#ictnetap3) | [ICTNETAP4](./runs.md#ictnetap4)

??? abstract "Abstract"
	
	Microblog track was first introduced in 2011 and we have participated in this task for 4 years [1,2,5]. This year's microblog track has two tasks. The first one, namely ad-hoc search task, is the same as usual. This task needs to retrieve all the tweets that are relevant to query Q before time T. Participants can access the corpus by official APIs. The second task is Tweet Timeline Generation(TTG) task. It is newly introduced this year and the main goal of it is to detect and remove the redundant tweets the first task retrieves. This report is organized as follows. Section 2 mainly focuses on the data preparation. Section 3 is our methodology and framework of the ad-hoc search task. Section 4 focuses on the methodology of TTG task. Section 5 gives the final results of the two tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CuiSLHXLC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/CuiSLHXLC14,
		author = {Guoxin Cui and Fabin Shi and Xiaolei Liu and Xiaobo Hao and Xueke Xu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Microblog Track in {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CuiSLHXLC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Pittsburgh at TREC 2014 Microblog Track

_Zheng Gao, Rui Bi_

- :fontawesome-solid-user-group: **Participant:** [zhg15](./participants.md#zhg15)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-zhg15_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-zhg15_microblog.pdf)
- :material-file-search: **Runs:** [Upitt](./runs.md#upitt) | [NewBee](./runs.md#newbee)

??? abstract "Abstract"
	
	An ad hoc retrieval task aims at return the most relevant documents based on a particular query. And high precision and recall always depends on clear query and elaborative documents. If the query is ambiguous while document is short and general, common retrieval models may not work well on the feedback. In this way, more expansive information will be needed to add in order to implement original queries and documents. That is the main purpose of microblog track of 2014 TREC Conference. The paper describes the first participation of University of Pittsburgh in 2014 TREC microblog track. The data is based on tweet collection which gathered in 2013. We got two runs for the final results which are base on BM25 feedback algorithm. The details of our retrieval model include query expansion, document expansion and retrieval model for the final rank.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaoB14.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaoB14,
		author = {Zheng Gao and Rui Bi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Pittsburgh at {TREC} 2014 Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-zhg15\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaoB14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QU at TREC-2014: Online Clustering with Temporal and Topical Expansion  for Tweet Timeline Generation

_Maram Hasanain, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./participants.md#qu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-QU_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-QU_microblog.pdf)
- :material-file-search: **Runs:** [QUQueryExp5D25T](./runs.md#ququeryexp5d25t) | [QUTmpDecay](./runs.md#qutmpdecay) | [QUTQRM](./runs.md#qutqrm) | [QUQueryExp10D15](./runs.md#ququeryexp10d15) | [QUQEd5t25TTgBL](./runs.md#quqed5t25ttgbl) | [QUTqrmTTgBL](./runs.md#qutqrmttgbl) | [QUQEd10t15TTgCL](./runs.md#quqed10t15ttgcl) | [QUTmpDecayTTgCL](./runs.md#qutmpdecayttgcl)

??? abstract "Abstract"
	
	In this work, we present our participation in the microblog track in TREC-2014, building upon our first participation last year. We present our approaches for the two tasks of this year: temporally-anchored ad-hoc search and tweet timeline generation. For the ad-hoc search task, we used topical expansion in addition to temporal models to perform retrieval. Our results show that our run based on the typical pseudo relevance feedback query expansion outperformed all of our other runs with a relatively high mean average precision (MAP). As for the timeline generation task, we approached this problem using online incremental clustering of tweets retrieved for a given query. Our approach allows the dynamic creation of “semantic” clusters while providing a framework for detecting redundant tweets and selecting representative ones to be added to the final timeline. The results demonstrate that using incremental clustering of tweets retrieved through a temporal retrieval model produced the best effectiveness among the submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HasanainE14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HasanainE14,
		author = {Maram Hasanain and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{QU} at {TREC-2014:} Online Clustering with Temporal and Topical Expansion for Tweet Timeline Generation},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-QU\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HasanainE14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HU DB at TREC 2014 Microblog Track

_Jennifer Klein, Yishai Oltchik, Nerya Or, Sara Cohen_

- :fontawesome-solid-user-group: **Participant:** [HU_DB](./participants.md#hu_db)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-HU_DB_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-HU_DB_microblog.pdf)
- :material-file-search: **Runs:** [SRTD](./runs.md#srtd) | [SR](./runs.md#sr) | [SRTL](./runs.md#srtl) | [Standard](./runs.md#standard) | [StandardAH](./runs.md#standardah) | [SRTLAH](./runs.md#srtlah) | [SRAH](./runs.md#srah) | [SRTDAH](./runs.md#srtdah)

??? abstract "Abstract"
	
	This paper describes our system for the Tweet Timeline Generation (TTG) task of the Microblog track, at the Text Retrieval Conference (TREC) 2014. Intuitively, given a collection of microblog posts (i.e., tweets), and a keyword query Q, the goal is to generate a timeline of related tweets. Such a timeline consists of representative tweets, relevant to Q. In our system we employ query expansion to identify highly relevant tweets, and then use affinity propagation to cluster the tweets, based on their word similarity, hashtag similarity and temporal similarity. We then return a representative tweet from each cluster. The result is a system with relatively good precision, but, unfortunately, poor recall. We discuss the techniques employed, as well as the insights gleaned while developing and testing our system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KleinOOC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/KleinOOC14,
		author = {Jennifer Klein and Yishai Oltchik and Nerya Or and Sara Cohen},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{HU} {DB} at {TREC} 2014 Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-HU\_DB\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KleinOOC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Siena's Twitter Information Retrieval System: The 2014 Microblog Track

_Timothy LaRock, Lauren Mathews, Matthew Roberts, Darren Lim, Sharon G. Small_

- :fontawesome-solid-user-group: **Participant:** [SCIAITeam](./participants.md#sciaiteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-SCIAITeam_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-SCIAITeam_microblog.pdf)
- :material-file-search: **Runs:** [SCIAI3am14a](./runs.md#sciai3am14a) | [SCIAI14a](./runs.md#sciai14a) | [SCIAI124a](./runs.md#sciai124a) | [SCIAI3am14aTTG](./runs.md#sciai3am14attg) | [SCIAI14aTTG](./runs.md#sciai14attg) | [SCIAI124aTTG](./runs.md#sciai124attg) | [SCIAI3cm4aTTG](./runs.md#sciai3cm4attg) | [SCIAI3cm4a](./runs.md#sciai3cm4a)

??? abstract "Abstract"
	
	As the internet dramatically changes each year, microblogs - such as Facebook and Twitter - are being used more often as a source of information exchange. Twitter users are learning about current events earlier compared to reading about it on their news feeds, as companies and celebrities continue to utilize Twitter to spread information. Information Retrieval, a topic which NIST (National Institute of Standards and Technology) holds a conference for every year, involves utilizing such online environments, like microblogs, to grab as much information from these sources to find if the information can be put towards a purpose. The Microblog Track was originally introduced to TREC2 (Text REtrieval Conference) in 2011, and selected Twitter3 as its microblog resource. Twitter allows its users to share short, 140 character length posts with their followers, and is often used to share anything from fashion trends to the latest terrorist attacks. Due to the short length of tweets, users often utilize other ways to share more information, such as including links or images with their tweets, which has an effect on the tweet containing relevant information. Participating groups for the track were given access to a Twitter API, provided by TREC, containing a corpus of 243 million tweets scrapped from February 1st to March 31st, 2013. Each group was given a set of test topics in which to test their system, which return results for the Adhoc and/or Tweet Timeline Generation Task (TTG). In this paper, we describe five Query Expansion modules and three Relevance modules designed for the microblog track, built within STIRS. Our precision results for our adhoc run shows STIRS' average to be at 61.91% precision, with our average TTG at 85.38% precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LaRockMRLS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LaRockMRLS14,
		author = {Timothy LaRock and Lauren Mathews and Matthew Roberts and Darren Lim and Sharon G. Small},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Siena's Twitter Information Retrieval System: The 2014 Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-SCIAITeam\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LaRockMRLS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept Based Tie-breaking and Maximal Marginal Relevance Retrieval  in Microblog Retrieval

_Kuang Lu, Hui Fang, Diego Roa_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_microblog.pdf)
- :material-file-search: **Runs:** [UDInfoTB](./runs.md#udinfotb) | [UDInfoTBRR](./runs.md#udinfotbrr) | [UDInfoQE](./runs.md#udinfoqe) | [UDInfoLTR](./runs.md#udinfoltr) | [UDInfoMMRA](./runs.md#udinfommra) | [UDInfoMMR5](./runs.md#udinfommr5) | [UDInfoMMRWCA](./runs.md#udinfommrwca) | [UDInfoMMRWC5](./runs.md#udinfommrwc5)

??? abstract "Abstract"
	
	There are enormous tweets posted on any given day, and the number keeps increasing. As a result, the needs of effectively retrieving tweets depending upon user's information need, and summarizing tweets per-taining to a given topic have become increasingly important. In this paper, Wikipedia concepts [1] was introduced in tie-breaking to perform ad-hoc microblog retrieval. The Maximal Marginal Relevance (MMR) [2] criterion is deployed to summarize relevant tweets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuFR14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuFR14,
		author = {Kuang Lu and Hui Fang and Diego Roa},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Concept Based Tie-breaking and Maximal Marginal Relevance Retrieval in Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_fang\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuFR14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKUICST at TREC 2014 Microblog Track: Feature Extraction for Effective  Microblog Search and Adaptive Clustering Algorithms for TTG

_Chao Lv, Feifan Fan, Runwei Qiang, Yue Fei, Jianwu Yang_

- :fontawesome-solid-user-group: **Participant:** [PKUICST](./participants.md#pkuicst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-PKUICST_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-PKUICST_microblog.pdf)
- :material-file-search: **Runs:** [PKUICST1](./runs.md#pkuicst1) | [PKUICST2](./runs.md#pkuicst2) | [PKUICST3](./runs.md#pkuicst3) | [PKUICST4](./runs.md#pkuicst4) | [TTGPKUICST1](./runs.md#ttgpkuicst1) | [TTGPKUICST2](./runs.md#ttgpkuicst2) | [TTGPKUICST3](./runs.md#ttgpkuicst3) | [TTGPKUICST4](./runs.md#ttgpkuicst4)

??? abstract "Abstract"
	
	This paper describes our approaches to temporally-anchored ad hoc retrieval task and tweet timeline generation (TTG) task in the TREC 2014 Microblog track. In the ad hoc search, we apply a learning to rank framework which utilizes not only the various content relevance of a tweet, but also the quality of a tweet. External evidences are well incorporated in our approach with Web-based query expansion and document expansion techniques. In the TTG task, we apply star clustering and hierarchical clustering algorithm on the retrieved tweets from ad hoc retrieval task. Experimental results show that our learning to rank methods with many state-of-the-art features achieve good retrieval performance with respect to MAP and P@30 metrics. Besides, our systems for TTG task also obtain convincing recall and precision scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LvFQFY14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LvFQFY14,
		author = {Chao Lv and Feifan Fan and Runwei Qiang and Yue Fei and Jianwu Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{PKUICST} at {TREC} 2014 Microblog Track: Feature Extraction for Effective Microblog Search and Adaptive Clustering Algorithms for {TTG}},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-PKUICST\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LvFQFY14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCAS at TREC-2014 Microblog Track

_Qingli Ma, Ben He, Dongxing Li_

- :fontawesome-solid-user-group: **Participant:** [UCAS](./participants.md#ucas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UCAS-microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UCAS-microblog.pdf)
- :material-file-search: **Runs:** [UCASRun1](./runs.md#ucasrun1) | [UCASRun3](./runs.md#ucasrun3) | [UCASRun2](./runs.md#ucasrun2) | [UCASRun4](./runs.md#ucasrun4)

??? abstract "Abstract"
	
	University of Chinese Academy of Sciences (UCAS) participated in the first task, namely temporally-anchored ad hoc retrieval in Microblog track, aiming to efficiently and effectively retrieve tweets. Based on the conventional application of learning to rank, we incorporated a machine learning approach, such as logistic regression for selecting high-quality training data for improving the effectiveness. Except for the tweets' content features, we also used the features of the web information, external evidence, which is related with the URLS to improve the effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaHL14.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaHL14,
		author = {Qingli Ma and Ben He and Dongxing Li},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UCAS} at {TREC-2014} Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UCAS-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MaHL14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QCRI at TREC 2014: Applying the KISS principle for the TTG  task in the Microblog Track

_Walid Magdy, Wei Gao, Tarek El-Ganainy, Zhongyu Wei_

- :fontawesome-solid-user-group: **Participant:** [QCRI](./participants.md#qcri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-QCRI_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-QCRI_microblog.pdf)
- :material-file-search: **Runs:** [EM50](./runs.md#em50) | [EM100](./runs.md#em100) | [SM100](./runs.md#sm100) | [SM50](./runs.md#sm50) | [HPRF1020RR](./runs.md#hprf1020rr) | [HPRF1020](./runs.md#hprf1020) | [PRF1030RR](./runs.md#prf1030rr) | [PRF1030](./runs.md#prf1030)

??? abstract "Abstract"
	
	In this paper we present our work on the ad-hoc search and the tweet timeline generation (TTG) tasks of TREC-2014 Microblog track. Regarding the ad-hoc search task, we used our best developed system over the last year, which include hyperlink-based query expansion and re-ranking models fusion. For the new tweet timeline generation task, we applied a straightforward and simple approach, which depends on clustering retrieval results based on Jaccard similarities between tweets. Our best adhoc results achieved the fifth rank and seventh rank among 21 participating groups when evaluated using P@30 and MAP respectively. However, our best TTG run achieved the second rank among participants, which shows that our simple TTG approach was more effective than most of the used TTG systems in TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MagdyGEW14.bib) "
	```
	@inproceedings{DBLP:conf/trec/MagdyGEW14,
		author = {Walid Magdy and Wei Gao and Tarek El{-}Ganainy and Zhongyu Wei},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{QCRI} at {TREC} 2014: Applying the {KISS} principle for the {TTG} task in the Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-QCRI\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MagdyGEW14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NovaSearch at TREC 2014 Microblog Track: Reranking with Wikipedia  Page Views

_Flávio Martins, João Magalhães_

- :fontawesome-solid-user-group: **Participant:** [NovaSearch](./participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-NovaSearch_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-NovaSearch_microblog.pdf)
- :material-file-search: **Runs:** [NovaRun1](./runs.md#novarun1) | [NovaRun2](./runs.md#novarun2) | [NovaRun0](./runs.md#novarun0)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2014 Microblog real-time search task. We investigate whether page views from Wikipedia can be used successfully to estimate relevant time periods for queries. To this end, we use a recently published temporal reranking method by Efron et al. [2], which uses kernel density estimation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MartinsM14.bib) "
	```
	@inproceedings{DBLP:conf/trec/MartinsM14,
		author = {Fl{\'{a}}vio Martins and Jo{\~{a}}o Magalh{\~{a}}es},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {NovaSearch at {TREC} 2014 Microblog Track: Reranking with Wikipedia Page Views},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-NovaSearch\_microblog.pdf},
		timestamp = {Thu, 14 May 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MartinsM14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UWM-HBUT at TREC 2014 Microblog Track: Using Query Expansion (QE)  and Event Identification Algorithm (EIA) to improve microblog retrieval  effectiveness

_Sukjin You, Xiangming Mu, Wei Huang_

- :fontawesome-solid-user-group: **Participant:** [UWM.HBUT](./participants.md#uwm.hbut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UWM-HBUT_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UWM-HBUT_microblog.pdf)
- :material-file-search: **Runs:** [UWMHBUT1](./runs.md#uwmhbut1) | [UWMHBUT2](./runs.md#uwmhbut2) | [UWMHBUT3](./runs.md#uwmhbut3) | [UWMHBUT4](./runs.md#uwmhbut4)

??? abstract "Abstract"
	
	This paper reports our contributions and results to TREC 2014 Microblog Track. Different from traditional web pages or database documents, microblogs have their own unique features. Considering sensitivity to time, we introduce a new factor to help to improve tweet retrieval effectiveness. The ranking score of a retrieved tweet is adjusted by considering how close the tweet time stamp is to the event using Event Identification Algorithm (EIA). In addition, we also evaluate the Query Expansion (QE) approach using Google as an external data corpus. There are 55 search topics and the data set contains a total of 243 million tweets provided by the TREC 2014 Microblog Track. Our initial results indicated that QE helped to improve the performance. We also discussed why the EIA approach failed to enhance the retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YouMH14.bib) "
	```
	@inproceedings{DBLP:conf/trec/YouMH14,
		author = {Sukjin You and Xiangming Mu and Wei Huang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UWM-HBUT} at {TREC} 2014 Microblog Track: Using Query Expansion {(QE)} and Event Identification Algorithm {(EIA)} to improve microblog retrieval effectiveness},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UWM-HBUT\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YouMH14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Estimating Semantic Similarity between Expanded Query and Tweet Content  for Microblog Retrieval

_Zhihua Zhang, Man Lan_

- :fontawesome-solid-user-group: **Participant:** [ECNUCS](./participants.md#ecnucs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ECNU_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ECNU_microblog.pdf)
- :material-file-search: **Runs:** [ECNURankLib](./runs.md#ecnuranklib) | [ECNURankLib2013](./runs.md#ecnuranklib2013) | [ECNUSVM](./runs.md#ecnusvm) | [ECNUSVM2013](./runs.md#ecnusvm2013)

??? abstract "Abstract"
	
	This paper reports the systems we submitted to the Microblog Track shared in TREC 2014 which focuses on ad hoc retrieval (i.e., retrieving top 1, 000 relevant tweet for every given topic). To address this task, we adopted a two-stage framework, i.e., firstly, we performed query expansion (i.e., expanding relevant inforamtion using pseudo-relevance feedback and Google search engine results) to retrieve more relevant tweets, then extracted several effective semantic features (e.g., Jansen-Shannon Distance, Overlap Similarity, Lucene Score, etc) from retrieved results and built ranking model using supervised machine learning algorithms with the aid of these features to perform re-ranking. Our systems ranked 3th out of 21 teams.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangL14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangL14,
		author = {Zhihua Zhang and Man Lan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Estimating Semantic Similarity between Expanded Query and Tweet Content for Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ECNU\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangL14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2014 Microblog Track

_Guangyuan Zhang, Zhen Yang, Shuyong Si_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BJUT_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BJUT_microblog.pdf)
- :material-file-search: **Runs:** [NCOS](./runs.md#ncos) | [NSIM](./runs.md#nsim) | [OSIM](./runs.md#osim)

??? abstract "Abstract"
	
	This paper describes the second participation of BJUT in the TREC Micro-blog Track. Two tasks are proposed in this year, including ad hoc search task and tweet timeline generation task. We attended the first task and focused on the method for re-ranking of the returned search results. Specifically, a graph-based method is proposed to re-rank the twitters returned by the official API, namely we re-rank the results by detecting whether some given characteristics are existing or not. Also, we introduce the details of our system, which consists of data preprocessing, system structure, and rank method & results analysis module.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangYS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangYS14,
		author = {Guangyuan Zhang and Zhen Yang and Shuyong Si},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2014 Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BJUT\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangYS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Delaware at TREC 2014

_Ashraf Bah, Karankumar Sabhnani, Mustafa Zengin, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [udel](./participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf)
- :material-file-search: **Runs:** [udelRunAH](./runs.md#udelrunah) | [udelRunTTG1](./runs.md#udelrunttg1) | [udelRunTTG2](./runs.md#udelrunttg2) | [udelRunTTG3](./runs.md#udelrunttg3) | [udelRunTTG4](./runs.md#udelrunttg4)

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

#### HLTCOE at TREC 2014: Microblog and Clinical Decision Support

_Tan Xu, Douglas W. Oard, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [hltcoe](./participants.md#hltcoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-hltcoe_microblog-clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-hltcoe_microblog-clinical.pdf)
- :material-file-search: **Runs:** [hltcoe0](./runs.md#hltcoe0) | [hltcoe1](./runs.md#hltcoe1) | [hltcoe2](./runs.md#hltcoe2) | [hltcoe3](./runs.md#hltcoe3) | [hltcoeTTG0](./runs.md#hltcoettg0) | [hltcoeTTG1](./runs.md#hltcoettg1) | [hltcoeTTG2](./runs.md#hltcoettg2) | [hltcoeTTG3](./runs.md#hltcoettg3)

??? abstract "Abstract"
	
	Our team submitted runs for both the Microblog and Clinical Decision Support tracks. For the Microblog track, we participated in both the temporally anchored adhoc search and the tweet timeline generation subtasks. On the Clinical Decision support task, our efforts were time limited, and our main contribution was to investigate controlling for morphological variation in this technical domain.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuOM14.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuOM14,
		author = {Tan Xu and Douglas W. Oard and Paul McNamee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{HLTCOE} at {TREC} 2014: Microblog and Clinical Decision Support},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-hltcoe\_microblog-clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuOM14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

