# Proceedings - Microblog 2012 

#### Overview of the TREC-2012 Microblog Track

_Ian Soboroff, Iadh Ounis, Craig Macdonald, Jimmy Lin_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/MICROBLOG12OVERVIEW.pdf](http://trec.nist.gov/pubs/trec21/papers/MICROBLOG12OVERVIEW.pdf)
??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SoboroffOML12.bib) "
	```
	@inproceedings{DBLP:conf/trec/SoboroffOML12,
		author = {Ian Soboroff and Iadh Ounis and Craig Macdonald and Jimmy Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC-2012} Microblog Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/MICROBLOG12OVERVIEW.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SoboroffOML12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Stream Features for Instant Document Filtering

_Andreas Bauer, Christian Wolff_

- :fontawesome-solid-user-group: **Participant:** [unir_de](./participants.md#unir_de)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/unir_de.microblog.final2.pdf](http://trec.nist.gov/pubs/trec21/papers/unir_de.microblog.final2.pdf)
- :material-file-search: **Runs:** [okapiv1](./runs.md#okapiv1) | [okapiv2rel](./runs.md#okapiv2rel) | [vsmv2rel](./runs.md#vsmv2rel) | [vsmv1](./runs.md#vsmv1)

??? abstract "Abstract"
	
	In this paper, we discuss how event processing technologies can be employed for real-time text stream processing and information filtering in the context of the TREC 2012 microblog task. After introducing basic characteristics of stream and event processing, the technical architecture of our text stream analysis engine is presented. Employing well-known term weighting schemes from document-centric text retrieval for temporally dynamic text streams is discussed next, giving details of the ESPER Event Processing Agents (EPAs) we have implemented for this task. Finally, we describe our experimental setup, give details on the TREC microblog runs as well as the result thereafter with our system including some extensions and give a short interpretation of the evaluation results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001W12.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001W12,
		author = {Andreas Bauer and Christian Wolff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Stream Features for Instant Document Filtering},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/unir\_de.microblog.final2.pdf},
		timestamp = {Mon, 19 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001W12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Frequent Itemset Mining for Query Expansion in Microblog adhoc Search

_Younos Aboulnaga, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/waterloo.microblog.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/waterloo.microblog.nb.pdf)
- :material-file-search: **Runs:** [uwcmb12CP](./runs.md#uwcmb12cp) | [uwcmb12BL](./runs.md#uwcmb12bl) | [uwcmb12CT](./runs.md#uwcmb12ct) | [uwcmb12NT](./runs.md#uwcmb12nt)

??? abstract "Abstract"
	
	The high volume of Tweets arriving every second and the requirement to index them in real time emphasize the importance of the computational complexity of algorithms used to process them. In this paper, we investigate the use of Frequent Itemsets Mining to quickly discover patterns that can later be used for query expansion. Frequent Itemsets Mining (FIM) has been highly adopted to mine data streams because of its computational simplicity and the possibility to parallelize some of its steps. Initial experiments using the TREC 2011 Microblogs track queries showed that it is possible to improve the performance of BM25, however this was not the case with the 2012 queries. Our analysis of the difference in performance provides insight about how to make best use of FIM for microblog search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AboulnagaC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/AboulnagaC12,
		author = {Younos Aboulnaga and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Frequent Itemset Mining for Query Expansion in Microblog adhoc Search},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/waterloo.microblog.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AboulnagaC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Siena's Twitter Information Retrieval System: The 2012 Microblog Track

_Karl Appel, Lauren Mathews, Darren Lim, Sharon G. Small_

- :fontawesome-solid-user-group: **Participant:** [SCIAITeam](./participants.md#sciaiteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/SCIATeam.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/SCIATeam.microblog.final.pdf)
- :material-file-search: **Runs:** [baseline](./runs.md#baseline) | [aWekaModel](./runs.md#awekamodel) | [expansion](./runs.md#expansion) | [urlContent](./runs.md#urlcontent) | [basic](./runs.md#basic) | [expansion2](./runs.md#expansion2) | [weka](./runs.md#weka) | [expansionurl](./runs.md#expansionurl)

??? abstract "Abstract"
	
	Since 1992, the National Institute of Standards and Technology (NIST) has been annually hosting the Text Retrieval Conference (TREC). One of the newest tracks, which started in 2011, is the Microblog Track, which uses a well-known social network site, Twitter[10], as its source of microblog data. Twitter allows its users to post 140 character length tweets to share messages with their followers, posting personal updates, and share major media stories from around the world. In order to evaluate information retrieval on microblog data, groups were provided with a file of about 16 million tweet IDs from January 24th to February 8th, 2011. This allowed us to download the tweet content of each ID for a total of 16,141,812 tweets. Participating teams were given a set of topics to test their retrieval process, and their program would return relevant tweets about that topic. The Siena College Institute of Artificial Intelligence expanded on STIRS, Siena's Twitter Information Retrieval System. The results for our adhoc run showed STIRS' best run to be at 18.08% precision, while the average of the median from all participating teams was 14.86%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AppelMLS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/AppelMLS12,
		author = {Karl Appel and Lauren Mathews and Darren Lim and Sharon G. Small},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Siena's Twitter Information Retrieval System: The 2012 Microblog Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/SCIATeam.microblog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AppelMLS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ISTI@TREC Microblog Track 2012: Real-Time Filtering Through Supervised  Learning

_Giacomo Berardi, Andrea Esuli, Diego Marcheggiani_

- :fontawesome-solid-user-group: **Participant:** [NEMIS_ISTI_CNR](./participants.md#nemis_isti_cnr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/NEMIS_ISTI_CNR.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/NEMIS_ISTI_CNR.microblog.final.pdf)
- :material-file-search: **Runs:** [nemisNotExt](./runs.md#nemisnotext) | [nemisExt](./runs.md#nemisext)

??? abstract "Abstract"
	
	Our approach to the microblog filtering task is based on learning a relevance classifier from an initial training set of relevant and non relevant tweets, generated by using a simple retrieval method. The classifier is then retrained using the (simulated) user feedback collected during the training process, in order to improve its accuracy as the filtering process goes on. In the official runs the system scored low effectiveness values, suffering a strong imbalance toward recall.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BerardiEM12.bib) "
	```
	@inproceedings{DBLP:conf/trec/BerardiEM12,
		author = {Giacomo Berardi and Andrea Esuli and Diego Marcheggiani},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {ISTI@TREC Microblog Track 2012: Real-Time Filtering Through Supervised Learning},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/NEMIS\_ISTI\_CNR.microblog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BerardiEM12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UGent Participation in the Microblog Track 2012

_Thong Hoang Van Duc, Thomas Demeester, Johannes Deleu, Piet Demeester, Chris Develder_

- :fontawesome-solid-user-group: **Participant:** [UGENT_IBCN_SIS](./participants.md#ugent_ibcn_sis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UGENT_IBCN_SIS.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/UGENT_IBCN_SIS.microblog.final.pdf)
- :material-file-search: **Runs:** [IBCN1](./runs.md#ibcn1) | [IBCN2](./runs.md#ibcn2) | [IBCN3](./runs.md#ibcn3) | [IBCN4](./runs.md#ibcn4)

??? abstract "Abstract"
	
	In this paper, we describe the search system, developed at Ghent University for the TREC 2012 Microblog Track in order to rank Twitter messages or 'tweets' from a fixed corpus in response to a number of search requests. Our system ranks the tweets based on a Logistic Regression classifier trained with data from the Microblog Track 2011. The features used for training the classifier include local tweets features, but also, query expansion and tweet expansion features, based on external Web data, which appear to significantly improve results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DucDDDD12.bib) "
	```
	@inproceedings{DBLP:conf/trec/DucDDDD12,
		author = {Thong Hoang Van Duc and Thomas Demeester and Johannes Deleu and Piet Demeester and Chris Develder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UGent Participation in the Microblog Track 2012},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UGENT\_IBCN\_SIS.microblog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DucDDDD12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microblog Search and Filtering with Time Sensitive Feedback and Thresholding  bsed on BM25

_Wei Gao, Zhongyu Wei, Kam-Fai Wong_

- :fontawesome-solid-user-group: **Participant:** [qcri_twitsear](./participants.md#qcri_twitsear)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/qcri_twitsear.micro.final.pdf](http://trec.nist.gov/pubs/trec21/papers/qcri_twitsear.micro.final.pdf)
- :material-file-search: **Runs:** [BM25](./runs.md#bm25) | [BM25PRF](./runs.md#bm25prf) | [BM25TRF](./runs.md#bm25trf) | [mergedRun](./runs.md#mergedrun) | [QFilRun1](./runs.md#qfilrun1) | [QFilRun2](./runs.md#qfilrun2) | [QFilRun3](./runs.md#qfilrun3)

??? abstract "Abstract"
	
	Microblogs such as Twitter are considered faster first-hand sources of information with many real-time fashions. We report our work in the real-time adhoc search and filtering tasks of TREC 2012 microblog track. Our system is built based on the traditional BM25 relevance model, in which specific techniques are tried out to respond to the need of finding relevant tweets, in the real-time adhoc task, we applied a peak detection algorithm for the process of blind feedback, We also tried to automatically combine the search results of multiple retrieval techniques. In the real-time filtering pilot task, we examine the effectiveness of some typical filtering methods previously used in TREC filtering track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaoWW12.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaoWW12,
		author = {Wei Gao and Zhongyu Wei and Kam{-}Fai Wong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microblog Search and Filtering with Time Sensitive Feedback and Thresholding bsed on {BM25}},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/qcri\_twitsear.micro.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaoWW12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Microblog 2012 Track: Real-Time Ranking Algorithm for Microblog  Ranking Systems

_Davide Feltoni Gurini, Fabio Gasparetti_

- :fontawesome-solid-user-group: **Participant:** [AI_ROMA3](./participants.md#ai_roma3)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/AI_ROMA3.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/AI_ROMA3.microblog.final.pdf)
- :material-file-search: **Runs:** [AIrun1](./runs.md#airun1)

??? abstract "Abstract"
	
	As a matter of fact Twitter is becoming the new big data container, due to the deep increase of amount of users and its growing popularity. Moreover the huge amount of user profiles and rough text data, are providing continuosly new research challenges. This paper reports our contribution and results to the Trec 2012 Microblog Track. In this particular, challenge each participant is required to conduct a ”real-time” retrieval task, which given a query topic seeks for the most recent and relevant tweets. We devised an effective real time ranking algorithm, avoiding heavy computational requirements. Our contribution is multifold: (1) adapting an existing ranking method BM25 to the microblogging purpose (2) enhancing traditional content-based features with knowledge extracted from Wikipedia, (3) employing Pseudo Relevance Feedback techniques for query expansion (4) performing text analysis such as ad-hoc text normalization and POS Tagging to limit noise data and better represent useful information.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GuriniG12.bib) "
	```
	@inproceedings{DBLP:conf/trec/GuriniG12,
		author = {Davide Feltoni Gurini and Fabio Gasparetti},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Microblog 2012 Track: Real-Time Ranking Algorithm for Microblog Ranking Systems},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/AI\_ROMA3.microblog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GuriniG12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HIT at TREC 2012 Microblog Track

_Zhongyuan Han, Xuwei Li, Muyun Yang, Haoliang Qi, Sheng Li, Tiejun Zhao_

- :fontawesome-solid-user-group: **Participant:** [HIT_MTLAB](./participants.md#hit_mtlab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/HIT_MTLAB.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/HIT_MTLAB.microblog.final.pdf)
- :material-file-search: **Runs:** [hitLRrun1](./runs.md#hitlrrun1) | [hitDELMrun2](./runs.md#hitdelmrun2) | [hitURLrun3](./runs.md#hiturlrun3) | [hitQryFBrun4](./runs.md#hitqryfbrun4) | [window2run](./runs.md#window2run) | [hitRSW](./runs.md#hitrsw) | [hitUWT](./runs.md#hituwt) | [urlAllFB](./runs.md#urlallfb)

??? abstract "Abstract"
	
	This paper describes our approaches to the TREC 2012 Microblog Track. We explore the query expansion and document expansion techniques to address the retrieval of short tweet texts. Further, we examine the webpages linked by the URL in a tweet as an external source to improve the performance. Then learning to rank technique is adopted to combine all features for better performance. Finally, we accomplish the microblog filtering via comparing the new tweet against top m relevant tweet retrieved in the history.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HanLYQLZHQ12.bib) "
	```
	@inproceedings{DBLP:conf/trec/HanLYQLZHQ12,
		author = {Zhongyuan Han and Xuwei Li and Muyun Yang and Haoliang Qi and Sheng Li and Tiejun Zhao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{HIT} at {TREC} 2012 Microblog Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/HIT\_MTLAB.microblog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HanLYQLZHQ12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Microblog 2012: adhoc Task

_Lamjed Ben Jabeur, Firas Damak, Lynda Tamine, Karen Pinel-Sauvagnat, Guillaume Cabanac, Mohand Boughanem_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/IRIT.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/IRIT.microblog.final.pdf)
- :material-file-search: **Runs:** [IRITfdvsm](./runs.md#iritfdvsm) | [IRITfdvsmurl](./runs.md#iritfdvsmurl) | [IRITbnetKSO](./runs.md#iritbnetkso) | [IRITbnetK](./runs.md#iritbnetk)

??? abstract "Abstract"
	
	This paper describes the participation of the IRIT lab, university of Toulouse, France, to the Microblog Track of TREC 2012. Two different models are experimented by our team for the adhoc task: (i) a Bayesian network retrieval model for tweet search and (ii) a feature learning model for relevance classification. Experimental results show that Bayesian network retrieval model improves the performances comparing to the track median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JabeurDTPCB12.bib) "
	```
	@inproceedings{DBLP:conf/trec/JabeurDTPCB12,
		author = {Lamjed Ben Jabeur and Firas Damak and Lynda Tamine and Karen Pinel{-}Sauvagnat and Guillaume Cabanac and Mohand Boughanem},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRIT} at {TREC} Microblog 2012: adhoc Task},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/IRIT.microblog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JabeurDTPCB12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Searching and Filtering Tweets: CSIRO at the TREC 2012 Microblog  Track

_Sarvnaz Karimi, Jie Yin, Paul Thomas_

- :fontawesome-solid-user-group: **Participant:** [csiro](./participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/csiro.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/csiro.microblog.final.pdf)
- :material-file-search: **Runs:** [csiroNE112](./runs.md#csirone112) | [csiroQEll112](./runs.md#csiroqell112) | [csiroQEt112](./runs.md#csiroqet112) | [csiroR112](./runs.md#csiror112) | [csirolrhuq111](./runs.md#csirolrhuq111) | [csiroQERF111](./runs.md#csiroqerf111) | [csiroSVMqe111](./runs.md#csirosvmqe111) | [csiroshuq111](./runs.md#csiroshuq111)

??? abstract "Abstract"
	
	We report on the participation of the CSIRO1 team in the TREC 2012 Microblog Track. We participated with four automatic runs for the adhoc search task and four automatic runs for the filtering task. In the adhoc search task, we experiment with different pre-processing and query expansion techniques. Our most important finding is highlighting the value of systematic pre-processing of tweets and its impact on improving the effectiveness of search. In the filtering task, we apply different feature extraction and classification techniques. We demonstrate the potential of using SVM classifiers for filtering tweets for a given topic.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KarimiYT12.bib) "
	```
	@inproceedings{DBLP:conf/trec/KarimiYT12,
		author = {Sarvnaz Karimi and Jie Yin and Paul Thomas},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Searching and Filtering Tweets: {CSIRO} at the {TREC} 2012 Microblog Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/csiro.microblog.final.pdf},
		timestamp = {Thu, 21 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KarimiYT12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Overcoming Vocabulary Limitations in Twitter Microblogs

_Yubin Kim, Reyyan Yeniterzi, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU_Callan](./participants.md#cmu_callan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/CMU_Callan.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/CMU_Callan.microblog.final.pdf)
- :material-file-search: **Runs:** [cmuPhrE](./runs.md#cmuphre) | [cmuPrfPhr](./runs.md#cmuprfphr) | [cmuPrfPhrENo](./runs.md#cmuprfphreno) | [cmuPrfPhrE](./runs.md#cmuprfphre)

??? abstract "Abstract"
	
	One major difficulty in performing ad-hoc search on microblogs such as Twitter is the limited vocabulary of each document due their short length. In this paper, two approaches to addressing this issue are presented. The first is query expansion through pseudo-relevance feedback and the other is document expansion of tweets using web documents linked from the body of the tweet. Tweets are expanded by concatenating the contents of the title tag and the meta descriptor tags of the document to the tweet itself. These two approaches gave additive gains in MAP and Precision at 30.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KimYC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/KimYC12,
		author = {Yubin Kim and Reyyan Yeniterzi and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overcoming Vocabulary Limitations in Twitter Microblogs},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/CMU\_Callan.microblog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KimYC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKUICST at TREC 2012 Microblog Track

_Feng Liang, Runwei Qiang, Yihong Hong, Yue Fei, Jianwu Yang_

- :fontawesome-solid-user-group: **Participant:** [PKUICST](./participants.md#pkuicst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/PKUICST.microblog.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/PKUICST.microblog.nb.pdf)
- :material-file-search: **Runs:** [PKUICST1](./runs.md#pkuicst1) | [PKUICST2](./runs.md#pkuicst2) | [PKUICST3](./runs.md#pkuicst3) | [PKUICST4](./runs.md#pkuicst4) | [PKUICSTF2](./runs.md#pkuicstf2) | [PKUICSTF3](./runs.md#pkuicstf3) | [PKUICSTF4](./runs.md#pkuicstf4) | [PKUICSTF1](./runs.md#pkuicstf1)

??? abstract "Abstract"
	
	This paper describes the PKUICST's entry into the TREC 2012 Microblog track. In this year of microblog track, we participate in both the Real-time Adhoc Task and Real-time Filtering Task. In the Real-time Adhoc Task, we designed and conducted a series of experiments based on different retrieval models, namely Real-time Tweet Ranking (RTR) model and learning to rank framework. In the Real-time Filtering Task, we adopted various strategies to determine the filtering threshold. Official results demonstrate that our approach obtains convincing performances and more unofficial runs lead to some further conclusions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiangQHFY12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiangQHFY12,
		author = {Feng Liang and Runwei Qiang and Yihong Hong and Yue Fei and Jianwu Yang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PKUICST} at {TREC} 2012 Microblog Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/PKUICST.microblog.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiangQHFY12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2012 Microblog Track Experiments at Kobe University

_Taiki Miyanishi, Kazuhiro Seki, Kuniaki Uehara_

- :fontawesome-solid-user-group: **Participant:** [KobeU](./participants.md#kobeu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/KobeU.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/KobeU.microblog.final.pdf)
- :material-file-search: **Runs:** [tsqe](./runs.md#tsqe) | [kobeL2R](./runs.md#kobel2r) | [kobeMHC](./runs.md#kobemhc) | [kobeMHC2](./runs.md#kobemhc2)

??? abstract "Abstract"
	
	This paper describes our approach to real-time ad hoc task processing in the TREC 2012 Microblog track. The approach uses two-stage relevance feedback to model search interests and temporal dynamics on a microblog. The rst relevance feedback uses a single user-selected tweet as feedback. The second approach uses time-based query expansion method leveraging the temporal property derived from the real-time feature on microblogging services. The experimentally obtained results demonstrate that our two-stage relevance feedback approaches improve search result relevance considerably.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MiyanishiSU12.bib) "
	```
	@inproceedings{DBLP:conf/trec/MiyanishiSU12,
		author = {Taiki Miyanishi and Kazuhiro Seki and Kuniaki Uehara},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2012 Microblog Track Experiments at Kobe University},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/KobeU.microblog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MiyanishiSU12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2012: Microblog Track

_Zahra Amin Nayeri, Zheng Ye, Jimmy Xiangji Huang_

- :fontawesome-solid-user-group: **Participant:** [york](./participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/york.microblog.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/york.microblog.nb.pdf)
- :material-file-search: **Runs:** [YORK1](./runs.md#york1) | [YORK2](./runs.md#york2) | [york12mb3](./runs.md#york12mb3) | [york12mb4](./runs.md#york12mb4) | [york12bd1i](./runs.md#york12bd1i)

??? abstract "Abstract"
	
	Abstract. In this paper, we describe our participation of the ad-hoc task of TREC 2012 Microblog Track. In particular, we evaluate a hybrid retrieval system, which extends the Rocchio's feedback method by incorporating three kinds of IR component techniques. We adapt to the specifics of the microblog search task, giving rise to a highly effective end-to-end search system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NayeriYH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/NayeriYH12,
		author = {Zahra Amin Nayeri and Zheng Ye and Jimmy Xiangji Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2012: Microblog Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/york.microblog.nb.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NayeriYH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo: Logistic Regression and Reciprocal Rank Fusion  at the Microblog Track

_Adam Roegiest, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UWaterlooMDS.microblog.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/UWaterlooMDS.microblog.nb.pdf)
- :material-file-search: **Runs:** [uwatrrfall](./runs.md#uwatrrfall) | [uwatrrflm](./runs.md#uwatrrflm) | [uwatgclrbase](./runs.md#uwatgclrbase) | [uwatgclrman](./runs.md#uwatgclrman) | [uwn](./runs.md#uwn) | [uw](./runs.md#uw)

??? abstract "Abstract"
	
	For the second iteration of the Microblog Track, two tasks were given to participants to complete. The first was to perform the same ad hoc search task as the 2011 iteration. The goal of the task was to expand on last year's methods with 60 new topics and to explore different measures of evaluation. The second task was to filter the corpus with respect to the 2011 topics in an attempt to simulate a streaming environment and how simulating user feedback can effect retrieval results. For the ad hoc search task, we decided to expand on last year's approach by continuing to use the Wumpus Search Engine1 and adding in a logistic regression classifier (denoted GCLR in this article), first used in the TREC 2007 Spam Track [5]. In addition, pseudo-relevance feedback was conducted this year by taking a swapdocs approach[3], which will be expanded upon later. As well, a semi-automatic logistic regression run was conducted using seed documents provided by a user. For the filtering task, only different methods of training GCLR were examined. No manual feedback was conducted for the filtering task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoegiestC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoegiestC12,
		author = {Adam Roegiest and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Waterloo: Logistic Regression and Reciprocal Rank Fusion at the Microblog Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UWaterlooMDS.microblog.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoegiestC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Web-Based Pseudo Relevance Feedback for Microblog Retrieval

_Ahmed Saad El Din, Walid Magdy_

- :fontawesome-solid-user-group: **Participant:** [QCRI](./participants.md#qcri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/QCRI.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/QCRI.microblog.final.pdf)
- :material-file-search: **Runs:** [BL](./runs.md#bl) | [BLFB](./runs.md#blfb) | [QEWeb](./runs.md#qeweb) | [QEWebFB](./runs.md#qewebfb) | [UnifiedThr](./runs.md#unifiedthr) | [RetrievalThr](./runs.md#retrievalthr)

??? abstract "Abstract"
	
	This paper presents the experiments and results for the QCRI participation in the TREC Microblog track 2012. In this year, we apply a query expansion approach for improving the retrieval results in microblog search. Our approach performs web-search with the original query to get web results appeared at the same period of the query; then it extracts the webpage title of the first web result and uses it as an expansion to the original query before applying microblog search. Our results show a significant improvement to the baseline and significantly better results than the median result achieved in the track. We also report one run in the filtering task that applies straightforward technique for retrieval score threshold selection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SaadDM12.bib) "
	```
	@inproceedings{DBLP:conf/trec/SaadDM12,
		author = {Ahmed Saad El Din and Walid Magdy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Web-Based Pseudo Relevance Feedback for Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/QCRI.microblog.final.pdf},
		timestamp = {Mon, 13 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SaadDM12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Measuring Robustness with First Relevant Score in the TREC 2012  Microblog Track

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [ot](./participants.md#ot)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/OpenText.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/OpenText.microblog.final.pdf)
- :material-file-search: **Runs:** [otM12i](./runs.md#otm12i) | [otM12ih](./runs.md#otm12ih) | [otM12h](./runs.md#otm12h) | [otM12ihe](./runs.md#otm12ihe)

??? abstract "Abstract"
	
	In this paper, we measure the effectiveness of various experimental search techniques not just with traditional TREC ad hoc search measures such as Average Precision, R-precision and Precision@30, but also with robust measures based on just the rank of the first relevant item retrieved such as First Relevant Score and Generalized Success@30. We report the results of our experiments conducted in the context of the Real-Time Adhoc Search Task of the TREC 2012 Microblog Track which investigated the effectiveness of ad hoc search of a collection of more than 10 million tweets. For the experimental technique of favoring tweets with urls, we found that both the traditional and robust measures indicated statistically significant increases in the mean score. However, for an experimental blind feedback technique, a technique known to be non-robust as it typically makes poor results even worse, the traditional Average Precision measure indicated a statistically significant increase in the mean score, but some of the measures just based on the rank of the first relevant item successfully discerned a statistically significant decrease in the mean score from the non-robust technique.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson12.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson12,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Measuring Robustness with First Relevant Score in the {TREC} 2012 Microblog Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/OpenText.microblog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Time-Aware Language Model for Microblog Retrieval

_Bingjie Wei, Shuai Zhang, Rui Li, Bin Wang_

- :fontawesome-solid-user-group: **Participant:** [IIEIR](./participants.md#iieir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/IIEIR.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/IIEIR.microblog.final.pdf)
- :material-file-search: **Runs:** [IIEIR01](./runs.md#iieir01) | [IIEIR02](./runs.md#iieir02) | [IIEIR03](./runs.md#iieir03) | [IIEIR04](./runs.md#iieir04)

??? abstract "Abstract"
	
	This paper describes our work (the IIEIR participation) in the TREC 2012 Microblog Adhoc Track. We proposed a ranking algorithm with temporal information based query. More and more research work proved that time is an important factor for improving the search result, especially for Microblog search. Based on Language Model, the representative work used time information as the document's prior information. Intuitively, there were two ways for making use of this feature. One way was query relevant while the other was query irrelevant. The hypothesis of the two models is “the newer of the document, the more important”. However, different query had different hot time points (the top time of relevance documents' time distribution). Take this into consideration; we supposed four models based on hot time points (HTLM). On this basis, we considered the model which is not relevant with query as document's background information and the model which is relevant with query as document's independent information. We used smoothing operation and supposed a mix timed language model. The results suggested that, HTLM models are more effective for Microblog search and mix model further improved compared with the single model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WeiZLW12.bib) "
	```
	@inproceedings{DBLP:conf/trec/WeiZLW12,
		author = {Bingjie Wei and Shuai Zhang and Rui Li and Bin Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Time-Aware Language Model for Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/IIEIR.microblog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WeiZLW12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Incorporating Temporal Information in Microblog Retrieval

_Craig Willis, Richard Medlin, Jaime Arguello_

- :fontawesome-solid-user-group: **Participant:** [UNC_SILS](./participants.md#unc_sils)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UNC_SILS.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/UNC_SILS.microblog.final.pdf)
- :material-file-search: **Runs:** [UNCQE](./runs.md#uncqe) | [UNCTP](./runs.md#unctp) | [UNCRQE](./runs.md#uncrqe) | [UNCTQE](./runs.md#unctqe)

??? abstract "Abstract"
	
	Microblog retrieval is the task of retrieving relevant tweets in response a query. This paper presents our methods and results for the Real-time Ad-hoc Task in the TREC Microblog Track 2012. Our experiments focused on different ways of using temporal information to improve retrieval. Our four runs include three methods that use temporal information and a baseline method that does not. One of our temporal methods favors recent tweets and the other two favor tweets from time periods associated with a high concentration of tweets predicted relevant (potentially, but not necessarily the recent past).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WillisMA12.bib) "
	```
	@inproceedings{DBLP:conf/trec/WillisMA12,
		author = {Craig Willis and Richard Medlin and Jaime Arguello},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Incorporating Temporal Information in Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UNC\_SILS.microblog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WillisMA12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept Detection and Using Concept in adhoc of Microblog Search

_Hao Wu, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/udel_fang.microblog.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/udel_fang.microblog.nb.pdf)
- :material-file-search: **Runs:** [UDInfoMBIDF](./runs.md#udinfombidf) | [UDInfoMBEx](./runs.md#udinfombex) | [UDInfoMBCW](./runs.md#udinfombcw) | [UDInfoMBTp](./runs.md#udinfombtp)

??? abstract "Abstract"
	
	We report our system and experiments in TREC 2012 microblog Ad-hoc task. Our goal is to return most relevant tweets to satisfy user's information needs which are represented by short keyword queries. In additional to the last year's temporal approach, we used Wikipedia pages to detect concepts of each query. And based on the concepts we detected, we did query expansion and concepts weighting separately. Both methods showed improvements comparing to baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuF12,
		author = {Hao Wu and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concept Detection and Using Concept in adhoc of Microblog Search},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/udel\_fang.microblog.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at 2012 Microblog Track

_Jiayue Zhang, Sijia Chen, Yue Liu, Jie Yin, Qianqian Wang, Weiran Xu, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/PRIS.microblog.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/PRIS.microblog.nb.pdf)
- :material-file-search: **Runs:** [PRISrun1](./runs.md#prisrun1) | [PRISrun2](./runs.md#prisrun2) | [PRISrun3](./runs.md#prisrun3) | [PRISrun4](./runs.md#prisrun4)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangCLYWXG12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangCLYWXG12,
		author = {Jiayue Zhang and Sijia Chen and Yue Liu and Jie Yin and Qianqian Wang and Weiran Xu and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at 2012 Microblog Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/PRIS.microblog.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangCLYWXG12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCAS at TREC 2012 Microblog Track

_Xin Zhang, Sha Lu, Ben He, Jungang Xu, Tiejian Luo_

- :fontawesome-solid-user-group: **Participant:** [GUCAS](./participants.md#gucas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/GUCAS.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/GUCAS.microblog.final.pdf)
- :material-file-search: **Runs:** [gucasBasic](./runs.md#gucasbasic) | [gucasGen](./runs.md#gucasgen) | [gucasQuery](./runs.md#gucasquery) | [gucasGenReg](./runs.md#gucasgenreg) | [gucasB](./runs.md#gucasb) | [gucasL1](./runs.md#gucasl1) | [gucasL2](./runs.md#gucasl2)

??? abstract "Abstract"
	
	Two search tasks, i.e. real-time adhoc and real-time filtering are addressed in this year's Microblog track. The participation of (Graduate) University of Chinese Academy of Sciences (UCAS) in this track aims to evaluate the effectiveness of the query-biased learning to rank model, which was proposed in our previous work. To futher improve the retrieval effectiveness of learning to rank, we construct the query-biased learning to rank framework by taking the difference between queries into consideration. In particular, we learn a query-biased ranking model with a semi-supervised transductive learning algorithm so that the query-specific features, e.g. the unique expansion terms, are utilized to capture the characteristics of the target query. This query-biased ranking mode is combined with the general ranking model to produce the final ranked list of tweets in response to the given target query. Experiments on the standard TREC Tweets11 collection show that the query-biased learning to rank approach outperforms strong baselines when evaluated under MAP, namely the conventional application of the state-of-the-art learning to rank algorithm.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangLHXL12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangLHXL12,
		author = {Xin Zhang and Sha Lu and Ben He and Jungang Xu and Tiejian Luo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCAS} at {TREC} 2012 Microblog Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/GUCAS.microblog.final.pdf},
		timestamp = {Fri, 27 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangLHXL12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Microblog Track TREC 2012

_Bolong Zhu, Jinghua Gao, Xiao Han, Cunhui Shi, Shenghua Liu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/ICTNET.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/ICTNET.microblog.final.pdf)
- :material-file-search: **Runs:** [ICTWDSERUN1](./runs.md#ictwdserun1) | [ICTWDSERUN2](./runs.md#ictwdserun2) | [ICTWDSERUN3](./runs.md#ictwdserun3) | [ICTWDSERUN4](./runs.md#ictwdserun4) | [ICTNETFTRUN1](./runs.md#ictnetftrun1) | [ICTNETFTRUN2](./runs.md#ictnetftrun2) | [ICTNETFTRUN3](./runs.md#ictnetftrun3) | [ICTNETFTRUN4](./runs.md#ictnetftrun4)

??? abstract "Abstract"
	
	There are two search tasksin TREC2012 Microblog Track[1], namely: Real-time Adhoc and Real-time Filtering.The Tweets2011 corpus is used again and last year's results can be used as first officiallylabeled data for any participants to traintheir models.In this year's track, the former task has60 new queriesgiven and the latter is first proposed. In the Real-time Adhoc task, we use indri retrieval toolkit[2] to construct our retrieval system and propose a strategy of pseudo relevance feedback to expand original query,then we retrieved original tweets and their indri's scores as an important feature.Besides, we calculate lots of other features of these tweets, such abouturl, hash_tag, entropy, tfidf, bm25, language model[3] and proximity[4].At last, we use two learning-to-rank methods, specifically RankSVM[5] and ListNet[6], to combine all those featuresto sort them, returning the final ranked tweets to a specified query. In the Real-time Filtering task, we assuming this task is similar with the topic tracking in Twitter Stream[7], we build up two filtering modelsbased on language modeland Vector Space Modelrespectively. Each model is initialized by the start query and its relevant tweets. For each new coming tweet, the model will decide whether it is under thetopic. If it is, we update the model to keep up with the development of the topic. The rest of this paper is organized as follows. In Section 2, we discuss the preprocessing of Tweets2011 corpus. In Section 3, the main method to rank the search results in Real-time Adhoc task is discussed. In Real-time Filtering task, we describe two filtering models in Section 4. Experiment resultsare reported in Section 5. And in the last section, we draw conclusions about our work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuGHSLLC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuGHSLLC12,
		author = {Bolong Zhu and Jinghua Gao and Xiao Han and Cunhui Shi and Shenghua Liu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Microblog Track {TREC} 2012},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/ICTNET.microblog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuGHSLLC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Illinois' Graduate School of Library and Information  Science at TREC 2012

_Miles Efron, Jana Deisner, Peter Organisciak, Garrick Sherman, Ana Lucic_

- :fontawesome-solid-user-group: **Participant:** [uiucGSLIS](./participants.md#uiucgslis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/uiucGSLIS.microblog.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/uiucGSLIS.microblog.kba.final.pdf)
- :material-file-search: **Runs:** [uiucGSLIS01](./runs.md#uiucgslis01) | [uiucGSLIS02](./runs.md#uiucgslis02) | [uiucGSLIS03](./runs.md#uiucgslis03) | [uiucGSLIS04](./runs.md#uiucgslis04)

??? abstract "Abstract"
	
	The University of Illinois' Graduate School of Library and Information Science (uiucGSLIS) participated in TREC's microblog and knowledge base acceleration (KBA) tracks in 2012. Our high-level goals were two-fold: Microblog: Test a novel method for document ranking during real-time search. KBA: Compare methods of topic representation-particularly longitudinal adaptation of topic representation-for the KBA task. Our document ranking in the microblog track is based on a behavioral metaphor. Given a query Q, we decompose Q into a set of imaginary saved searches S. Given an incoming document stream D = D1, D2, . . . , DN , we ask: what is the probability that a document D is read, given the user's query and a rational allocation of attention over his saved searches? Our KBA runs relied on the track's inherent temporality to induce and maintain expressive entity profiles during the Cumulative Citation Recommendation (CCR) task. Time influenced our approach in two ways. First, an initial entity model was built by analyzing that entity's Wikipedia edit history prior to the corpus start date. Each feature's initial probability was a function of its persistence over the edit history. Second, as our system iterated over the stream's nine-month window, an entity's model adapted in light of recently seen documents. Entities were represented as weighted feature sets using the Indri query language. Our main result hinged on the method for model adaptation over time. In adapting for temporal change, we used a monthly “memoryless” updating procedure, balancing a conservative approach to updating with more aggressive adaptation. Thus, at the end of each month of filtering, an entity's features were updated based on the month's stream. This update mixed the previous month's model with the current model; but all previous months were ignored. No new features were added; rather, we only re-estimated each feature's probability within the model. This approach allowed a helpful degree of adaptability, while hedging against model drift. Of particular interest was the effect of model updating mechanisms. We used two very different approaches to adaptation. On the supplied training data, a Markov model-based technique strongly outperformed a sim- ple linear interpolation. However, initial results suggest that in the long run, the formalism behind updating was less important than the more basic matter of assuring adequate flex- ibility by some means while retaining the model's pertinence to the entity it described. Our system used the Indri search engine and API1 for core indexing and data manip- ulation. Our retrieval models varied from task to task, as described below. Very little pre-processing was used in our experiments. We did not stem documents. We did no stopping at index time, though stoplists (described below) were used during construction of some baseline pseudo-relevance feedback models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EfronDOSL12.bib) "
	```
	@inproceedings{DBLP:conf/trec/EfronDOSL12,
		author = {Miles Efron and Jana Deisner and Peter Organisciak and Garrick Sherman and Ana Lucic},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Illinois' Graduate School of Library and Information Science at {TREC} 2012},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/uiucGSLIS.microblog.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EfronDOSL12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2012: Experiments with Terrier in  Medical Records, Microblog, and Web Tracks

_Nut Limsopatham, Richard McCreadie, M-Dyaa Albakour, Craig Macdonald, Rodrygo L. T. Santos, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/uogTr.medical.microblog.web.final.pdf](http://trec.nist.gov/pubs/trec21/papers/uogTr.medical.microblog.web.final.pdf)
- :material-file-search: **Runs:** [uogTrBsE](./runs.md#uogtrbse) | [uogTrLsE](./runs.md#uogtrlse) | [uogTrCIDE](./runs.md#uogtrcide) | [uogTrFFeDm](./runs.md#uogtrffedm) | [uogTrFFDmN](./runs.md#uogtrffdmn) | [uogTrFADmI](./runs.md#uogtrfadmi) | [uogTrFADmN](./runs.md#uogtrfadmn)

??? abstract "Abstract"
	
	In TREC 2012, we focus on tackling the new challenges posed by the Medical, Microblog and Web tracks, using our Terrier Information Retrieval Platform. In particular, for the Medical track, we investigate how to exploit implicit knowledge within medical records, with the aim of better identifying those records from patients with specific medical conditions. For the Microblog track adhoc task, we investigate novel techniques to leverage documents hyperlinked from tweets to better estimate relevance of those tweets and increase recall. Meanwhile, for the Microblog track filtering task, we developed a new stream processing infrastructure for real-time adaptive filtering on top of the Storm framework. For the TREC Web track, we continue to build upon our learning-to-rank approaches and novel xQuAD framework within Terrier, increasing both effectiveness and efficiency when ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LimsopathamMAMS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LimsopathamMAMS12,
		author = {Nut Limsopatham and Richard McCreadie and M{-}Dyaa Albakour and Craig Macdonald and Rodrygo L. T. Santos and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2012: Experiments with Terrier in Medical Records, Microblog, and Web Tracks},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/uogTr.medical.microblog.web.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LimsopathamMAMS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at TREC 2012

_Richard Berendsen, Edgar Meij, Daan Odijk, Maarten de Rijke, Wouter Weerkamp_

- :fontawesome-solid-user-group: **Participant:** [UvA](./participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UvA.microblog.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/UvA.microblog.kba.final.pdf)
- :material-file-search: **Runs:** [UvAfilter](./runs.md#uvafilter)

??? abstract "Abstract"
	
	This year the Information and Language Processing Systems (ILPS) group of the University of Amsterdam participated in the Microblog and the Knowledge Base Acceleration (KBA) tracks. In this paper, we describe our participation for each of these tracks, in two largely independent sections: Section 2 on our KBA track participation and Section 3 on our work in the Microblog track. We detail the runs we submitted, present the results of the submitted runs, and, where possible, provide an initial analysis of these results. We conclude in Section 4.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BerendsenMORW12.bib) "
	```
	@inproceedings{DBLP:conf/trec/BerendsenMORW12,
		author = {Richard Berendsen and Edgar Meij and Daan Odijk and Maarten de Rijke and Wouter Weerkamp},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at {TREC} 2012},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UvA.microblog.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BerendsenMORW12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

