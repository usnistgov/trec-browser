# Proceedings 2012 

## Microblog 

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

- :fontawesome-solid-user-group: **Participant:** [unir_de](./microblog/participants.md#unir_de)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/unir_de.microblog.final2.pdf](http://trec.nist.gov/pubs/trec21/papers/unir_de.microblog.final2.pdf)
- :material-file-search: **Runs:** [okapiv1](./microblog/runs.md#okapiv1) | [okapiv2rel](./microblog/runs.md#okapiv2rel) | [vsmv2rel](./microblog/runs.md#vsmv2rel) | [vsmv1](./microblog/runs.md#vsmv1)

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

- :fontawesome-solid-user-group: **Participant:** [waterloo](./microblog/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/waterloo.microblog.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/waterloo.microblog.nb.pdf)
- :material-file-search: **Runs:** [uwcmb12CP](./microblog/runs.md#uwcmb12cp) | [uwcmb12BL](./microblog/runs.md#uwcmb12bl) | [uwcmb12CT](./microblog/runs.md#uwcmb12ct) | [uwcmb12NT](./microblog/runs.md#uwcmb12nt)

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

- :fontawesome-solid-user-group: **Participant:** [SCIAITeam](./microblog/participants.md#sciaiteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/SCIATeam.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/SCIATeam.microblog.final.pdf)
- :material-file-search: **Runs:** [baseline](./microblog/runs.md#baseline) | [aWekaModel](./microblog/runs.md#awekamodel) | [expansion](./microblog/runs.md#expansion) | [urlContent](./microblog/runs.md#urlcontent) | [basic](./microblog/runs.md#basic) | [expansion2](./microblog/runs.md#expansion2) | [weka](./microblog/runs.md#weka) | [expansionurl](./microblog/runs.md#expansionurl)

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

- :fontawesome-solid-user-group: **Participant:** [NEMIS_ISTI_CNR](./microblog/participants.md#nemis_isti_cnr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/NEMIS_ISTI_CNR.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/NEMIS_ISTI_CNR.microblog.final.pdf)
- :material-file-search: **Runs:** [nemisNotExt](./microblog/runs.md#nemisnotext) | [nemisExt](./microblog/runs.md#nemisext)

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

- :fontawesome-solid-user-group: **Participant:** [UGENT_IBCN_SIS](./microblog/participants.md#ugent_ibcn_sis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UGENT_IBCN_SIS.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/UGENT_IBCN_SIS.microblog.final.pdf)
- :material-file-search: **Runs:** [IBCN1](./microblog/runs.md#ibcn1) | [IBCN2](./microblog/runs.md#ibcn2) | [IBCN3](./microblog/runs.md#ibcn3) | [IBCN4](./microblog/runs.md#ibcn4)

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

- :fontawesome-solid-user-group: **Participant:** [qcri_twitsear](./microblog/participants.md#qcri_twitsear)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/qcri_twitsear.micro.final.pdf](http://trec.nist.gov/pubs/trec21/papers/qcri_twitsear.micro.final.pdf)
- :material-file-search: **Runs:** [BM25](./microblog/runs.md#bm25) | [BM25PRF](./microblog/runs.md#bm25prf) | [BM25TRF](./microblog/runs.md#bm25trf) | [mergedRun](./microblog/runs.md#mergedrun) | [QFilRun1](./microblog/runs.md#qfilrun1) | [QFilRun2](./microblog/runs.md#qfilrun2) | [QFilRun3](./microblog/runs.md#qfilrun3)

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

- :fontawesome-solid-user-group: **Participant:** [AI_ROMA3](./microblog/participants.md#ai_roma3)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/AI_ROMA3.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/AI_ROMA3.microblog.final.pdf)
- :material-file-search: **Runs:** [AIrun1](./microblog/runs.md#airun1)

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

- :fontawesome-solid-user-group: **Participant:** [HIT_MTLAB](./microblog/participants.md#hit_mtlab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/HIT_MTLAB.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/HIT_MTLAB.microblog.final.pdf)
- :material-file-search: **Runs:** [hitLRrun1](./microblog/runs.md#hitlrrun1) | [hitDELMrun2](./microblog/runs.md#hitdelmrun2) | [hitURLrun3](./microblog/runs.md#hiturlrun3) | [hitQryFBrun4](./microblog/runs.md#hitqryfbrun4) | [window2run](./microblog/runs.md#window2run) | [hitRSW](./microblog/runs.md#hitrsw) | [hitUWT](./microblog/runs.md#hituwt) | [urlAllFB](./microblog/runs.md#urlallfb)

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

- :fontawesome-solid-user-group: **Participant:** [IRIT](./microblog/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/IRIT.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/IRIT.microblog.final.pdf)
- :material-file-search: **Runs:** [IRITfdvsm](./microblog/runs.md#iritfdvsm) | [IRITfdvsmurl](./microblog/runs.md#iritfdvsmurl) | [IRITbnetKSO](./microblog/runs.md#iritbnetkso) | [IRITbnetK](./microblog/runs.md#iritbnetk)

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

- :fontawesome-solid-user-group: **Participant:** [csiro](./microblog/participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/csiro.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/csiro.microblog.final.pdf)
- :material-file-search: **Runs:** [csiroNE112](./microblog/runs.md#csirone112) | [csiroQEll112](./microblog/runs.md#csiroqell112) | [csiroQEt112](./microblog/runs.md#csiroqet112) | [csiroR112](./microblog/runs.md#csiror112) | [csirolrhuq111](./microblog/runs.md#csirolrhuq111) | [csiroQERF111](./microblog/runs.md#csiroqerf111) | [csiroSVMqe111](./microblog/runs.md#csirosvmqe111) | [csiroshuq111](./microblog/runs.md#csiroshuq111)

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

- :fontawesome-solid-user-group: **Participant:** [CMU_Callan](./microblog/participants.md#cmu_callan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/CMU_Callan.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/CMU_Callan.microblog.final.pdf)
- :material-file-search: **Runs:** [cmuPhrE](./microblog/runs.md#cmuphre) | [cmuPrfPhr](./microblog/runs.md#cmuprfphr) | [cmuPrfPhrENo](./microblog/runs.md#cmuprfphreno) | [cmuPrfPhrE](./microblog/runs.md#cmuprfphre)

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

- :fontawesome-solid-user-group: **Participant:** [PKUICST](./microblog/participants.md#pkuicst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/PKUICST.microblog.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/PKUICST.microblog.nb.pdf)
- :material-file-search: **Runs:** [PKUICST1](./microblog/runs.md#pkuicst1) | [PKUICST2](./microblog/runs.md#pkuicst2) | [PKUICST3](./microblog/runs.md#pkuicst3) | [PKUICST4](./microblog/runs.md#pkuicst4) | [PKUICSTF2](./microblog/runs.md#pkuicstf2) | [PKUICSTF3](./microblog/runs.md#pkuicstf3) | [PKUICSTF4](./microblog/runs.md#pkuicstf4) | [PKUICSTF1](./microblog/runs.md#pkuicstf1)

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

- :fontawesome-solid-user-group: **Participant:** [KobeU](./microblog/participants.md#kobeu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/KobeU.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/KobeU.microblog.final.pdf)
- :material-file-search: **Runs:** [tsqe](./microblog/runs.md#tsqe) | [kobeL2R](./microblog/runs.md#kobel2r) | [kobeMHC](./microblog/runs.md#kobemhc) | [kobeMHC2](./microblog/runs.md#kobemhc2)

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

- :fontawesome-solid-user-group: **Participant:** [york](./microblog/participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/york.microblog.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/york.microblog.nb.pdf)
- :material-file-search: **Runs:** [YORK1](./microblog/runs.md#york1) | [YORK2](./microblog/runs.md#york2) | [york12mb3](./microblog/runs.md#york12mb3) | [york12mb4](./microblog/runs.md#york12mb4) | [york12bd1i](./microblog/runs.md#york12bd1i)

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

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./microblog/participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UWaterlooMDS.microblog.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/UWaterlooMDS.microblog.nb.pdf)
- :material-file-search: **Runs:** [uwatrrfall](./microblog/runs.md#uwatrrfall) | [uwatrrflm](./microblog/runs.md#uwatrrflm) | [uwatgclrbase](./microblog/runs.md#uwatgclrbase) | [uwatgclrman](./microblog/runs.md#uwatgclrman) | [uwn](./microblog/runs.md#uwn) | [uw](./microblog/runs.md#uw)

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

- :fontawesome-solid-user-group: **Participant:** [QCRI](./microblog/participants.md#qcri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/QCRI.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/QCRI.microblog.final.pdf)
- :material-file-search: **Runs:** [BL](./microblog/runs.md#bl) | [BLFB](./microblog/runs.md#blfb) | [QEWeb](./microblog/runs.md#qeweb) | [QEWebFB](./microblog/runs.md#qewebfb) | [UnifiedThr](./microblog/runs.md#unifiedthr) | [RetrievalThr](./microblog/runs.md#retrievalthr)

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

- :fontawesome-solid-user-group: **Participant:** [ot](./microblog/participants.md#ot)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/OpenText.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/OpenText.microblog.final.pdf)
- :material-file-search: **Runs:** [otM12i](./microblog/runs.md#otm12i) | [otM12ih](./microblog/runs.md#otm12ih) | [otM12h](./microblog/runs.md#otm12h) | [otM12ihe](./microblog/runs.md#otm12ihe)

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

- :fontawesome-solid-user-group: **Participant:** [IIEIR](./microblog/participants.md#iieir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/IIEIR.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/IIEIR.microblog.final.pdf)
- :material-file-search: **Runs:** [IIEIR01](./microblog/runs.md#iieir01) | [IIEIR02](./microblog/runs.md#iieir02) | [IIEIR03](./microblog/runs.md#iieir03) | [IIEIR04](./microblog/runs.md#iieir04)

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

- :fontawesome-solid-user-group: **Participant:** [UNC_SILS](./microblog/participants.md#unc_sils)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UNC_SILS.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/UNC_SILS.microblog.final.pdf)
- :material-file-search: **Runs:** [UNCQE](./microblog/runs.md#uncqe) | [UNCTP](./microblog/runs.md#unctp) | [UNCRQE](./microblog/runs.md#uncrqe) | [UNCTQE](./microblog/runs.md#unctqe)

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

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./microblog/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/udel_fang.microblog.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/udel_fang.microblog.nb.pdf)
- :material-file-search: **Runs:** [UDInfoMBIDF](./microblog/runs.md#udinfombidf) | [UDInfoMBEx](./microblog/runs.md#udinfombex) | [UDInfoMBCW](./microblog/runs.md#udinfombcw) | [UDInfoMBTp](./microblog/runs.md#udinfombtp)

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

- :fontawesome-solid-user-group: **Participant:** [PRIS](./microblog/participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/PRIS.microblog.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/PRIS.microblog.nb.pdf)
- :material-file-search: **Runs:** [PRISrun1](./microblog/runs.md#prisrun1) | [PRISrun2](./microblog/runs.md#prisrun2) | [PRISrun3](./microblog/runs.md#prisrun3) | [PRISrun4](./microblog/runs.md#prisrun4)

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

- :fontawesome-solid-user-group: **Participant:** [GUCAS](./microblog/participants.md#gucas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/GUCAS.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/GUCAS.microblog.final.pdf)
- :material-file-search: **Runs:** [gucasBasic](./microblog/runs.md#gucasbasic) | [gucasGen](./microblog/runs.md#gucasgen) | [gucasQuery](./microblog/runs.md#gucasquery) | [gucasGenReg](./microblog/runs.md#gucasgenreg) | [gucasB](./microblog/runs.md#gucasb) | [gucasL1](./microblog/runs.md#gucasl1) | [gucasL2](./microblog/runs.md#gucasl2)

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

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./microblog/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/ICTNET.microblog.final.pdf](http://trec.nist.gov/pubs/trec21/papers/ICTNET.microblog.final.pdf)
- :material-file-search: **Runs:** [ICTWDSERUN1](./microblog/runs.md#ictwdserun1) | [ICTWDSERUN2](./microblog/runs.md#ictwdserun2) | [ICTWDSERUN3](./microblog/runs.md#ictwdserun3) | [ICTWDSERUN4](./microblog/runs.md#ictwdserun4) | [ICTNETFTRUN1](./microblog/runs.md#ictnetftrun1) | [ICTNETFTRUN2](./microblog/runs.md#ictnetftrun2) | [ICTNETFTRUN3](./microblog/runs.md#ictnetftrun3) | [ICTNETFTRUN4](./microblog/runs.md#ictnetftrun4)

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

- :fontawesome-solid-user-group: **Participant:** [uiucGSLIS](./microblog/participants.md#uiucgslis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/uiucGSLIS.microblog.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/uiucGSLIS.microblog.kba.final.pdf)
- :material-file-search: **Runs:** [uiucGSLIS01](./microblog/runs.md#uiucgslis01) | [uiucGSLIS02](./microblog/runs.md#uiucgslis02) | [uiucGSLIS03](./microblog/runs.md#uiucgslis03) | [uiucGSLIS04](./microblog/runs.md#uiucgslis04)

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

- :fontawesome-solid-user-group: **Participant:** [uogTr](./microblog/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/uogTr.medical.microblog.web.final.pdf](http://trec.nist.gov/pubs/trec21/papers/uogTr.medical.microblog.web.final.pdf)
- :material-file-search: **Runs:** [uogTrBsE](./microblog/runs.md#uogtrbse) | [uogTrLsE](./microblog/runs.md#uogtrlse) | [uogTrCIDE](./microblog/runs.md#uogtrcide) | [uogTrFFeDm](./microblog/runs.md#uogtrffedm) | [uogTrFFDmN](./microblog/runs.md#uogtrffdmn) | [uogTrFADmI](./microblog/runs.md#uogtrfadmi) | [uogTrFADmN](./microblog/runs.md#uogtrfadmn)

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

- :fontawesome-solid-user-group: **Participant:** [UvA](./microblog/participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UvA.microblog.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/UvA.microblog.kba.final.pdf)
- :material-file-search: **Runs:** [UvAfilter](./microblog/runs.md#uvafilter)

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

## Web 

#### Overview of the TREC 2012 Web Track

_Charles L. A. Clarke, Nick Craswell, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/WEB12.overview.pdf](http://trec.nist.gov/pubs/trec21/papers/WEB12.overview.pdf)
??? abstract "Abstract"
	
	If you are an experienced participant, you may not need to read the full report. Apart from the results themselves (see tables 1, 2, and 3) little has changed from TREC 2011 [6]. A six-point scale was used for relevance assessment (see section 4.1). Limitations on available assessor time meant that some topics were judged to depth 30 and others to depth 20, as well as causing other minor problems (see section 4.3). However, our plans for next year, as outlined in the concluding section, are quite different from this year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCV12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCV12,
		author = {Charles L. A. Clarke and Nick Craswell and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2012 Web Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/WEB12.overview.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCV12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query-Structure Based Web Page Indexing

_Falah Hassan Al-akashi, Diana Inkpen_

- :fontawesome-solid-user-group: **Participant:** [uottawa](./web/participants.md#uottawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/uottawa.web.final.pdf](http://trec.nist.gov/pubs/trec21/papers/uottawa.web.final.pdf)
- :material-file-search: **Runs:** [DFalah121A](./web/runs.md#dfalah121a) | [DFalah121D](./web/runs.md#dfalah121d) | [DFalah120A](./web/runs.md#dfalah120a) | [DFalah120D](./web/runs.md#dfalah120d)

??? abstract "Abstract"
	
	Indexing is a crucial technique for dealing with the massive amount of data present on the web. In our third participation in the web track at TREC 2012, we explore the idea of building an efficient query-based indexing system over Web page collection. Our prototype explores the trends in user queries and consequently indexes texts using particular attributes available in the documents. This paper provides an in-depth description of our approach for indexing web documents efficiently; that is, topics available in the web documents are discovered with the assistance of knowledge available in Wikipedia. The well- defined articles in Wikipedia are shown to be valuable as a training set when indexing Webpages. Our complex index structure also records information from titles and urls, and pays attention to web domains. Our approach is designed to close the gaps in our approaches from the previous two years, for some queries. Our framework is able to efficiently index the 50 million pages available in the subset B of the ClueWeb09 collection. Our preliminary experiments on the TREC 2012 testing queries showed that our indexing scheme is robust and efficient for both indexing and retrieving relevant web pages, for both the ad-hoc and diversity task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Al-akashiI12.bib) "
	```
	@inproceedings{DBLP:conf/trec/Al-akashiI12,
		author = {Falah Hassan Al{-}akashi and Diana Inkpen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Query-Structure Based Web Page Indexing},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/uottawa.web.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Al-akashiI12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Does Category A Anchor Text Improve Category B Results?

_Leonid Boytsov_

- :fontawesome-solid-user-group: **Participant:** [srchvrs](./web/participants.md#srchvrs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/srchvrs.web.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/srchvrs.web.nb.pdf)
- :material-file-search: **Runs:** [srchvrs12c10](./web/runs.md#srchvrs12c10) | [srchvrs12c09](./web/runs.md#srchvrs12c09) | [srchvrs12c00](./web/runs.md#srchvrs12c00)

??? abstract "Abstract"
	
	We merged results obtained from the Category B index with results obtained from the index built over complete (Category A) anchor text. However, we were unable to improve over Category B results in either the ad hoc or the diversity task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Boytsov12.bib) "
	```
	@inproceedings{DBLP:conf/trec/Boytsov12,
		author = {Leonid Boytsov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Does Category {A} Anchor Text Improve Category {B} Results?},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/srchvrs.web.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Boytsov12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LIA at TREC 2012 Web Track: Unsupervised Search Concepts Identification  from General Sources of Information

_Romain Deveaud, Eric SanJuan, Patrice Bellot_

- :fontawesome-solid-user-group: **Participant:** [LIA](./web/participants.md#lia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/LIA.web.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/LIA.web.nb.pdf)
- :material-file-search: **Runs:** [lcmweb](./web/runs.md#lcmweb) | [lcmweb10p](./web/runs.md#lcmweb10p) | [lcmwebnoW](./web/runs.md#lcmwebnow) | [lcm4res](./web/runs.md#lcm4res)

??? abstract "Abstract"
	
	In this paper, we report the experiments we conducted for our participation to the TREC 2012 Web Track. We experimented a brand new system that models the latent concepts underlying a query. We use Latent Dirichlet Allocation (LDA), a generative probabilistic topic model, to exhibit highly-specific query-related topics from pseudo-relevant feedback documents. We define these topics as the latent concepts of the user query. Our approach automatically estimates the number of latent concepts as well as the needed amount of feedback documents, without any prior training step. These concepts are incorporated into the ranking function with the aim of promoting documents that refer to many different query-related thematics. We also explored the use of different types of sources of information for modeling the latent concepts. For this purpose, we use four general sources of information of various nature (web, news, encyclopedic) from which the feedback documents are extracted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DeveaudSB12.bib) "
	```
	@inproceedings{DBLP:conf/trec/DeveaudSB12,
		author = {Romain Deveaud and Eric SanJuan and Patrice Bellot},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{LIA} at {TREC} 2012 Web Track: Unsupervised Search Concepts Identification from General Sources of Information},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/LIA.web.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DeveaudSB12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRRA at TREC 2012: Divergence From Independence (DFI)

_Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [irra](./web/participants.md#irra)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/irra.web.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/irra.web.nb.pdf)

??? abstract "Abstract"
	
	IRRA (IR-Ra) group participated in the 2012 Web track, with a system implementing a non-parametric term weighting method based on measuring the divergence from independence (DFI). This is the third year of participation for IRRA group, following the participations in TREC 2009 and 2010 Web tracks. In this year, the aim is to evaluate a new DFI-based term weighting model developed on the basis of Shannon's information theory (Shannon, 1949), along with the evaluation of a heuristic approach that is expected to provide early precision when used together with DFI term weighting. The TERRIER retrieval platform version 3.0 (Ounis et al., 2007) is used to index and search the ClueWeb09-T09B1 data set (“Category B” data set), a subset of about 50 million Web pages in English. During indexing and searching, terms are stemmed (Porter's stemmer as implemented in TERRIER) but not stopped. The result sets are filtered using the fusion of two spam-page lists provided by Cormack et al. (2010) for ClueWeb09 document collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Dincer12.bib) "
	```
	@inproceedings{DBLP:conf/trec/Dincer12,
		author = {Bekir Taner Din{\c{c}}er},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRRA} at {TREC} 2012: Divergence From Independence {(DFI)}},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/irra.web.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Dincer12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2012: Experiments with Terrier in  Medical Records, Microblog, and Web Tracks

_Nut Limsopatham, Richard McCreadie, M-Dyaa Albakour, Craig Macdonald, Rodrygo L. T. Santos, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./web/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/uogTr.medical.microblog.web.final.pdf](http://trec.nist.gov/pubs/trec21/papers/uogTr.medical.microblog.web.final.pdf)
- :material-file-search: **Runs:** [uogTrA44s9](./web/runs.md#uogtra44s9) | [uogTrA44xi](./web/runs.md#uogtra44xi) | [uogTrA44xu](./web/runs.md#uogtra44xu) | [uogTrA44xl](./web/runs.md#uogtra44xl) | [uogTrB44xu](./web/runs.md#uogtrb44xu) | [uogTrB45aIs](./web/runs.md#uogtrb45ais)

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

#### Ensemble Clustering for Result Diversification

_Dong Nguyen, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [utwente](./web/participants.md#utwente)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/utwente.web.final.pdf](http://trec.nist.gov/pubs/trec21/papers/utwente.web.final.pdf)
- :material-file-search: **Runs:** [utw2012lm09](./web/runs.md#utw2012lm09) | [utw2012lda](./web/runs.md#utw2012lda) | [utw2012c1](./web/runs.md#utw2012c1) | [utw2012sc1](./web/runs.md#utw2012sc1) | [utw2012c2](./web/runs.md#utw2012c2) | [utw2012fc1](./web/runs.md#utw2012fc1)

??? abstract "Abstract"
	
	This paper describes the participation of the University of Twente in the Web track of TREC 2012. Our baseline approach uses the Mirex toolkit, an open source tool that sequantially scans all the documents. For result diversification, we experimented with improving the quality of clusters through ensemble clustering. We combined clusters obtained by different clustering methods (such as LDA and K-means) and clusters obtained by using different types of data (such as document text and anchor text). Our two-layer ensemble run performed better than the LDA based diversification and also better than a non-diversification run.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NguyenH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/NguyenH12,
		author = {Dong Nguyen and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Ensemble Clustering for Result Diversification},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/utwente.web.final.pdf},
		timestamp = {Tue, 24 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NguyenH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QUT_Para at TREC 2012 Web Track: Word Associations for Retrieving  Web Documents

_Mike Symonds, Guido Zuccon, Bevan Koopman, Peter Bruza_

- :fontawesome-solid-user-group: **Participant:** [QUT_Para](./web/participants.md#qut_para)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/QUT_Para.web.final.pdf](http://trec.nist.gov/pubs/trec21/papers/QUT_Para.web.final.pdf)
- :material-file-search: **Runs:** [QUTparaTQEg1](./web/runs.md#qutparatqeg1) | [QUTparaBline](./web/runs.md#qutparabline)

??? abstract "Abstract"
	
	Many existing information retrieval models do not explicitly take into account information about word associations. Our approach makes use of first and second order relationships found in natural language, known as syntagmatic and paradigmatic associations, respectively. This is achieved by using a formal model of word meaning within the query expansion process. On ad hoc retrieval, our approach achieves statistically significant improvements in MAP (0.158) and P@20 (0.396) over our baseline model. The ERR@20 and nDCG@20 of our system was 0.249 and 0.192 respectively. Our results and discussion suggest that information about both syntagamtic and paradigmatic associations can assist with improving retrieval effectiveness on ad hoc retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SymondsZKBZK12.bib) "
	```
	@inproceedings{DBLP:conf/trec/SymondsZKBZK12,
		author = {Mike Symonds and Guido Zuccon and Bevan Koopman and Peter Bruza},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {QUT{\_}Para at {TREC} 2012 Web Track: Word Associations for Retrieving Web Documents},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/QUT\_Para.web.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SymondsZKBZK12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting Ontologies for Search Result Diversification

_Wei Zheng, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./web/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/udel_fang.web.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/udel_fang.web.nb.pdf)
- :material-file-search: **Runs:** [UDInfoDivSt](./web/runs.md#udinfodivst) | [UDInfoDivC1](./web/runs.md#udinfodivc1) | [UDInfoDivC2](./web/runs.md#udinfodivc2)

??? abstract "Abstract"
	
	We report our systems and experimental results in the diversity task of web track 2012. Our goal is to exploit the structured data, i.e., the ontologies, as well as unstructured data for search result diversification. We use two strategies in the diversification systems. The first strategy combines the ontology and unstructured data to extract integrated subtopics. It then uses the coverage based diversification function to diversify documents based on the integrated subtopics. The second strategy exploits the structure information in the ontology for diversification. We use a structural diversification to diversify documents based on the structural relationships of their subtopics in the ontology.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengF12,
		author = {Wei Zheng and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploiting Ontologies for Search Result Diversification},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/udel\_fang.web.nb.pdf},
		timestamp = {Tue, 20 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2012 Diversity Task

_Zilong Feng, Yuanhai Xue, Xiaoming Yu, Hongbo Xu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./web/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/ICTNET.web-diversity.final.pdf](http://trec.nist.gov/pubs/trec21/papers/ICTNET.web-diversity.final.pdf)
- :material-file-search: **Runs:** [ICTNET12ADR1](./web/runs.md#ictnet12adr1) | [ICTNET12DVR1](./web/runs.md#ictnet12dvr1) | [ICTNET12DVR2](./web/runs.md#ictnet12dvr2) | [ICTNET12ADR2](./web/runs.md#ictnet12adr2) | [ICTNET12DVR3](./web/runs.md#ictnet12dvr3) | [ICTNET12ADR3](./web/runs.md#ictnet12adr3)

??? abstract "Abstract"
	
	In this paper, we report our experiments at Diversity task, Web Track 2012. In this year, we attempt to use query expansion and topic model such as LDA[5] to get subtopics. And an model based on xQuAD[10] was used to re-rank the ad-hoc search results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FengXYXLC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/FengXYXLC12,
		author = {Zilong Feng and Yuanhai Xue and Xiaoming Yu and Hongbo Xu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2012 Diversity Task},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/ICTNET.web-diversity.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FengXYXLC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2012 adhoc Task

_Heyuan Li, Yuanhai Xue, Shaohua Guo, Feng Guan, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./web/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/ICTNET.web-adhoc.final.pdf](http://trec.nist.gov/pubs/trec21/papers/ICTNET.web-adhoc.final.pdf)
- :material-file-search: **Runs:** [ICTNET12ADR1](./web/runs.md#ictnet12adr1) | [ICTNET12DVR1](./web/runs.md#ictnet12dvr1) | [ICTNET12DVR2](./web/runs.md#ictnet12dvr2) | [ICTNET12ADR2](./web/runs.md#ictnet12adr2) | [ICTNET12DVR3](./web/runs.md#ictnet12dvr3) | [ICTNET12ADR3](./web/runs.md#ictnet12adr3)

??? abstract "Abstract"
	
	In this paper, we report our experiments at Ad-hoc task, Web Track 2012. In this year, we attempt to use new web parser with noise elimination. The Conditional Boolean BM25 was used as major ranking function. We also introduce Learning-To-Rank to combine multiple features together for ranking, but the performance was poor due to the low quality of training data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiXGGYLC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiXGGYLC12,
		author = {Heyuan Li and Yuanhai Xue and Shaohua Guo and Feng Guan and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2012 adhoc Task},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/ICTNET.web-adhoc.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiXGGYLC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Contextual Suggestion 

#### Overview of the TREC 2012 Contextual Suggestion Track

_Adriel Dean-Hall, Charles L. A. Clarke, Jaap Kamps, Paul Thomas, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/CONTEXTUAL12.overview.pdf](http://trec.nist.gov/pubs/trec21/papers/CONTEXTUAL12.overview.pdf)
??? abstract "Abstract"
	
	The contextual suggestion track investigates search techniques for complex information needs that are highly dependent on context and user interests. According to a report from the Second Strategic Workshop on Information Retrieval in Lorne [1]: “Future information retrieval systems must anticipate user needs and respond with information appropriate to the current context without the user having to enter an explicit query. . . In a mobile context such a system might take the form of an app that recommends interesting places and activities based on the user's location, personal preferences, past history, and environmental factors such as weather and time. . . In contrast to many traditional recommender systems, these systems must be open domain, ideally able to make suggestion and synthesize information from multiple sources. . . ” For example, imagine a group of information retrieval researchers with a November evening to spend in beautiful Gaithersburg, Maryland. A contextual suggestion system might recommend a beer at the Dogfish Head Alehouse (www.dogfishalehouse.com), dinner at the Flaming Pit (www.flamingpitrestaurant.com), or even a trip into Washington on the metro to see the National Mall (www.nps.gov/nacc). As its primary goal, the contextual suggestion track seeks to develop evaluation methodologies for such systems. TREC 2012 is the first year for the track. For this first year, we introduced a single task to evaluate contextual suggestion from the open Web. As input to the task participants were given a set of example suggestions, a set of user preference profiles, and a set of geotemporal contexts. The task was to take the profiles and contexts and to produce up to 50 ranked suggestions for each combination of profile and context. Participants gathered suggestions from the open Web. Each profile corresponds to a single user, and indicates that user's preference with respect to each sample suggestion. For example, one suggestion might be to have a beer at the Dogfish Head Alehouse, and the profile might include a negative preference with respect to this suggestion. Each suggestion includes a title, description, and an associated URL. Each context corresponds to a particular geotemporal location, including city, day of the week, time of day, and season. For example, the context might be Gaithersburg, Maryland, on a weekday evening in the fall. The geographical contexts are very coarse-grained (i.e., an entire city) to help simplify the task. A total of 14 groups submitting 27 runs participated in this first year of the track, this includes the 2 baseline submissions from CSIRO and 2 baseline submissions from the University of Waterloo. These baselines will be discussed later in this report. Given the newness of the track, participants were given the option of basing their suggestions solely on the user profiles (returning suggstions appropriate to any place and time) or solely on geotemporal context (returning suggestions appropriate to a generic user). Only one group, from the University of Delaware, took advantage of this option, submitting runs based solely on user profile.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Dean-HallCKTV12.bib) "
	```
	@inproceedings{DBLP:conf/trec/Dean-HallCKTV12,
		author = {Adriel Dean{-}Hall and Charles L. A. Clarke and Jaap Kamps and Paul Thomas and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2012 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/CONTEXTUAL12.overview.pdf},
		timestamp = {Fri, 24 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Dean-HallCKTV12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC 2012 Contextual Suggestion Track

_Gilles Hubert, Guillaume Cabanac_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./context/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/IRIT.context.final.pdf](http://trec.nist.gov/pubs/trec21/papers/IRIT.context.final.pdf)
- :material-file-search: **Runs:** [iritSplit3CPv1](./context/runs.md#iritsplit3cpv1) | [iritSplit3CPv2](./context/runs.md#iritsplit3cpv2)

??? abstract "Abstract"
	
	In this paper we give an overview of the participation of the IRIT lab, University of Toulouse, France, in the TREC 2012 Contextual Suggestion Track. We present our personalized contextual retrieval framework, an approach for context processing, and two approaches for user preference processing. The official evaluations of our two submitted runs are reported and compared to the four baselines defined for the track. Evaluation results show that one of our submitted run was ranked 1st among the 27 runs of the 14 participants for the two official evaluation measures of the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HubertC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/HubertC12,
		author = {Gilles Hubert and Guillaume Cabanac},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRIT} at {TREC} 2012 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/IRIT.context.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HubertC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Contextual Suggestion from Wikitravel: Exploiting Community-Based  Suggestions

_Marijn Koolen, Jaap Kamps, Hugo C. Huurdeman_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./context/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UAmsterdam.contextual.final.pdf](http://trec.nist.gov/pubs/trec21/papers/UAmsterdam.contextual.final.pdf)
- :material-file-search: **Runs:** [UAmsCS12wtSUM](./context/runs.md#uamscs12wtsum) | [UAmsCS12wtSUMb](./context/runs.md#uamscs12wtsumb)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2012 Contextual Suggestion Track. The goal of the track is to evaluate systems that provide suggestions for activities to users in a specific location, at a specific time, taking into account their personal preferences. As a source for travel suggestions we use Wikitravel, which is a community-based travel guide for destinations all over the world. From pages dedicated to cities in the US we extract suggestions for sightseeing, shopping, eating and drinking. Descriptions from positive examples in the user profiles are used as queries to rank all suggestions in the US. Our baseline approach merges the per-query rankings of all positive examples of all users. Our user-dependent approach merges the per-query rankings of the positive examples of a single user. The rankings suggestions are then filtered based on the location of the user. We ignore the temporal aspects of the context. The user-dependent rankings are more effective for contextual suggestion than user-independent rankings. The two systems show similar perform on the geographical dimension, but the user-dependent system provides more interesting suggestions. Our results show that information on user preferences is valuable for providing appropriate suggestions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoolenKH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoolenKH12,
		author = {Marijn Koolen and Jaap Kamps and Hugo C. Huurdeman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Contextual Suggestion from Wikitravel: Exploiting Community-Based Suggestions},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UAmsterdam.contextual.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KoolenKH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Context Suggestion Track TREC 2012

_Bingyang Liu, Tong Wu, Xianghui Lin, Yanqin Zhong, Qian Liu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./context/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/ICTNET.contextual.final.pdf](http://trec.nist.gov/pubs/trec21/papers/ICTNET.contextual.final.pdf)
- :material-file-search: **Runs:** [ICTCONTEXTRUN1](./context/runs.md#ictcontextrun1) | [ICTCONTEXTRUN2](./context/runs.md#ictcontextrun2)

??? abstract "Abstract"
	
	Yelp'is used to collect the initial candidate web site list for every context. Then we use a spider to fetch contents of each candidate site. We also classify the candidates and examples into 6 classes and calculate preference of each profile to each class. The classes and preference are used for the ranking of the results. Finally we use several methods to filter and generate descriptions for every web site that is returned in the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuWLZLLC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuWLZLLC12,
		author = {Bingyang Liu and Tong Wu and Xianghui Lin and Yanqin Zhong and Qian Liu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Context Suggestion Track {TREC} 2012},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/ICTNET.contextual.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuWLZLLC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Contextual Suggestion

_Abhishek Mallik, Mandar Mitra, Kripabandhu Ghosh_

- :fontawesome-solid-user-group: **Participant:** [isi_paik](./context/participants.md#isi_paik)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/isi_paik.contextual.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/isi_paik.contextual.nb.pdf)
- :material-file-search: **Runs:** [watcs12a](./context/runs.md#watcs12a) | [watcs12b](./context/runs.md#watcs12b)

??? abstract "Abstract"
	
	The goal of this project is to build a Contextual Suggestion system that will recommend the usel a lanked list of suggestions depending on user's context as well as her preferences. In this context we pr€6ent an algorithm based on the regular expression for extra.ting time and address information from different websites for the places. Then we have suggested a ranking function that can utilize these timing and address information of those places as well as the users' context and preferences to rank the places. Here the page6 are unstructured but the address is structured i.e. template based as we have worked with only the plaaes located at Toronto, Canada.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MallikMG12.bib) "
	```
	@inproceedings{DBLP:conf/trec/MallikMG12,
		author = {Abhishek Mallik and Mandar Mitra and Kripabandhu Ghosh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/isi\_paik.contextual.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MallikMG12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding, Weighting and Describing Venues: CSIRO at the 2012 TREC  Contextual Suggestion Track

_David N. Milne, Paul Thomas, Cécile Paris_

- :fontawesome-solid-user-group: **Participant:** [csiro](./context/participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/csiro.contextual.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/csiro.contextual.nb.pdf)
- :material-file-search: **Runs:** [baselineB](./context/runs.md#baselineb) | [baselineA](./context/runs.md#baselinea) | [csiroth](./context/runs.md#csiroth) | [csiroht](./context/runs.md#csiroht)

??? abstract "Abstract"
	
	We report on the participation of CSIRO1 in the TREC 2012 contextual suggestion track, for which we submitted four runs. Two submissions were baselines that investigate the performance of a commercial system (namely the Google Places API), and whether the current experimental setup encourages diversity. The remaining two submissions were more complex approaches that explore the importance of time and personal preference. For the former, check-in statistics provided by Foursquare were used to identify which times of day and which days of week venues are more likely or less likely to be frequented. For the latter, textual similarity was used to weight venues with respect to positive and negative examples provided for each profile. Our submissions all fall either slightly above or slightly below the mean, depending on how they are judged. Interestingly, our baselines consistently outperform our more complex submissions, which suggests that a) venue quality (as given by Google review score) is a more important signal than either time or personal preference, at least in the context of this evaluation, and b) that the evaluation is biased to a specific type of venue, namely pubs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MilneTP12.bib) "
	```
	@inproceedings{DBLP:conf/trec/MilneTP12,
		author = {David N. Milne and Paul Thomas and C{\'{e}}cile Paris},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Finding, Weighting and Describing Venues: {CSIRO} at the 2012 {TREC} Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/csiro.contextual.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MilneTP12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2012 Contextual Suggestion Track

_Lin Qiu, JunRui Peng, Qianqian Wang, Yue Liu, Zhihua Zhou, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./context/participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/PRIS.context.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/PRIS.context.nb.pdf)
- :material-file-search: **Runs:** [PRISabc](./context/runs.md#prisabc)

??? abstract "Abstract"
	
	The system to Contextual Suggestion Track at TREC2012 includes information crawling and preprocessing, context filtering, user modeling, similarity computing and ranking, description generating. Some third party tool kits are used, such as URLPARSE. TF-IDF (term frequency-inverse document frequency) and cosine similarity is also used for building user models and computed similarities between users and candidate items.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiuPWLZXCG12.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiuPWLZXCG12,
		author = {Lin Qiu and JunRui Peng and Qianqian Wang and Yue Liu and Zhihua Zhou and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2012 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/PRIS.context.nb.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiuPWLZXCG12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TNO and RUN at the TREC 2012 Contextual Suggestion Track: Recommending  Personalized Touristic Sights Using Google Places

_Maya Sappelli, Wessel Kraaij, Suzan Verberne_

- :fontawesome-solid-user-group: **Participant:** [TNO_RadboudUniv](./context/participants.md#tno_radbouduniv)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/TNO_RadboudUniv.contextual.final.pdf](http://trec.nist.gov/pubs/trec21/papers/TNO_RadboudUniv.contextual.final.pdf)
- :material-file-search: **Runs:** [run01TI](./context/runs.md#run01ti) | [run02K](./context/runs.md#run02k)

??? abstract "Abstract"
	
	The purpose of the Contextual Suggestion track is to suggest personalized touristic activities to an individual, given a certain location and time. In our approach, we collected initial recommendations by using the location context as search query in Google Places. We first ranked the recommendations based on their textual similarity to the user profiles. In order to improve the ranking of popular sights, we combined the resulted ranking with a number of other rankings based on Google Search, popularity and categories. Finally, we performed filtering based on the temporal context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SappelliKV12.bib) "
	```
	@inproceedings{DBLP:conf/trec/SappelliKV12,
		author = {Maya Sappelli and Wessel Kraaij and Suzan Verberne},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TNO} and {RUN} at the {TREC} 2012 Contextual Suggestion Track: Recommending Personalized Touristic Sights Using Google Places},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/TNO\_RadboudUniv.contextual.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SappelliKV12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Exploraton of Ranking-Based Strategy for Contextual Suggestion

_Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./context/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/udel_fang.contextual.final.pdf](http://trec.nist.gov/pubs/trec21/papers/udel_fang.contextual.final.pdf)
- :material-file-search: **Runs:** [UDInfoCSTc](./context/runs.md#udinfocstc) | [UDInfoCSTdc](./context/runs.md#udinfocstdc)

??? abstract "Abstract"
	
	The purpose of the Contextual Suggestion track is to suggest personalized touristic activities to an individual, given a certain location and time. In our approach, we collected initial recommendations by using the location context as search query in Google Places. We first ranked the recommendations based on their textual similarity to the user profiles. In order to improve the ranking of popular sights, we combined the resulted ranking with a number of other rankings based on Google Search, popularity and categories. Finally, we performed filtering based on the temporal context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangF12,
		author = {Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {An Exploraton of Ranking-Based Strategy for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/udel\_fang.contextual.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### (Not Too) Personalized Learning to Rank for Contextual Suggestion

_Andrew Yates, Dave DeBoer, Hui Yang, Nazli Goharian, Steve Kunath, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [Georgetown](./context/participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/Georgetown.contextual.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/Georgetown.contextual.nb.pdf)
- :material-file-search: **Runs:** [gufinal](./context/runs.md#gufinal) | [guinit](./context/runs.md#guinit)

??? abstract "Abstract"
	
	In this work, we emphasize how to merge and re-rank contextual suggestions from the open Web based on a user‟s personal interests. We retrieve relevant results from the open Web by identifying context-independent queries, combining them with location information, and issuing the combined queries to multiple Web search engines. Our learning to rank model utilizes three types of profiles (a general profile, a city profile, and a personal profile) to re-rank and merge the results retrieved from the Web. We find that the learning model generates better results when the user profiles‟ weights are biased heavily towards major personal interests. The detections of major, minor and negative personal interests are done by statistical analysis across users, examples, and context-independent query types. For user interests detected by query types, we call the interests “macro-level interests”, while for user interest detected by examples, we call them “micro-level interests”. In our experiments, we find that “micro-level interests” effectively avoid favoring too much towards rare query types such as spa and game, and thus yields more balanced rankings. Finally, for the top ranked suggestions for each user and context, we generate result descriptions by learning to rank favorable Yelp comments and using a natural language generation algorithm to generate positive comments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YatesDYGKF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/YatesDYGKF12,
		author = {Andrew Yates and Dave DeBoer and Hui Yang and Nazli Goharian and Steve Kunath and Ophir Frieder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {(Not Too) Personalized Learning to Rank for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/Georgetown.contextual.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YatesDYGKF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Medical 

#### Overview of the TREC 2012 Medical Records Track

_Ellen M. Voorhees, William R. Hersh_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/MED12OVERVIEW.pdf](http://trec.nist.gov/pubs/trec21/papers/MED12OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Medical Records track fosters research that allows electronic health records to be retrieved based on the semantic content of free-text fields. The ability to find records by matching semantic content will enhance clinical care and support the secondary use of medical records in clinical trials and epidemiological studies. TREC 2012 is the sophomore year of the track, which attracted 24 participating research groups. The track repeated the cohort-finding task from its initial year. This task is an ad hoc search task in which systems search a set of de-identified clinical reports to identify cohorts for (possible) clinical studies. A topic statement for the task describes the criteria for inclusion in a study, and a system returns a list of “visits” ordered by the likelihood that the inclusion criteria are satisfied. Physicians created fifty topics and performed relevance judgments for the track. Top-performing groups each used some sort of vocabulary normalization device specific to the medical domain, supporting the hypothesis that language use within electronic health records is sufficiently different from general use to warrant domain-specific processing. Such devices must be used carefully, however, as multiple groups also demonstrated that aggressive use harms baseline performance. Exploiting human expertise through manual query construction proved most effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VoorheesH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/VoorheesH12,
		author = {Ellen M. Voorhees and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2012 Medical Records Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/MED12OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VoorheesH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Meda-data to Search for Clinical Records: RMIT at TREC 2012  Medical Track

_Iman Amini, Mark Sanderson, Xiaodong Li, David Martínez_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./medical/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/RMIT.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/RMIT.medical.nb.pdf)
- :material-file-search: **Runs:** [APRel1](./medical/runs.md#aprel1) | [GE4](./medical/runs.md#ge4) | [APRel2](./medical/runs.md#aprel2) | [RAPRel2](./medical/runs.md#raprel2)

??? abstract "Abstract"
	
	Clinical records contain International Classification of Diseases (ICD) codes summarizing the primary and/or secondary diseases of patients; these codes can be used as evidence to find relevant documents. In this paper we propose a novel approach to locally build a knowledge source from the existing data set to be used for query expansion, exploiting the ICD codes. While this approach does not rely on any external knowledge sources, it proves to be significantly superior to our global expansion and baseline systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AminiSLM12.bib) "
	```
	@inproceedings{DBLP:conf/trec/AminiSLM12,
		author = {Iman Amini and Mark Sanderson and Xiaodong Li and David Mart{\'{\i}}nez},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Meda-data to Search for Clinical Records: {RMIT} at {TREC} 2012 Medical Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/RMIT.medical.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AminiSLM12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Identifying Patients for Clinical Studies from Electronic Health Records:  TREC 2012 Medical Records Track at OHSU

_Steven Bedrick, Tracy Edinger, Aaron M. Cohen, William R. Hersh_

- :fontawesome-solid-user-group: **Participant:** [OHSU](./medical/participants.md#ohsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/OHSU.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/OHSU.medical.final.pdf)
- :material-file-search: **Runs:** [ohsuManBool](./medical/runs.md#ohsumanbool) | [OHSUCombICD](./medical/runs.md#ohsucombicd) | [OHSUCombET](./medical/runs.md#ohsucombet) | [OHSUCEtICD](./medical/runs.md#ohsuceticd)

??? abstract "Abstract"
	
	The goal of the TREC 2012 Medical Records Track was to search medical record documents to identify patients as possible candidates for clinical studies based on diagnosis, age, and other attributes. For TREC 2012, the Oregon Health & Science University (OHSU) group experimented with both manual and automated techniques. We used a derivative of Lucene to build an interactive retrieval system that can process queries in one of two ways. Users can manually specify Boolean queries whose terms may include words as well as ICD-9 codes. Alternatively, the system features an automated query parser that transforms free-text queries into structured Boolean queries. The query parser is built on top of MetaMap and the UMLS Metathesaurus. We submitted both automatic runs (which relied solely on the automated query parser) as well as manual runs consisting of queries built by an expert clinician. Overall, our automated query parser performed below the mean of other groups, although there were individual topics for which it performed very well. This irregular performance was in part due to our parser's tendency to over-specify queries, leading to reduced recall. There were, however, several topics for which our parser performed very well, suggesting that our fundamental approach has merit. In contrast, our manual runs performed very well, scoring second-best among official manual runs. With further modification of the manual queries, we were able to achieve even better performance. Query of electronic health records for the use case of identifying patients as candidates for clinical studies still requires manual query development, at least until better automated methods can be developed that outperform them.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BedrickECH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/BedrickECH12,
		author = {Steven Bedrick and Tracy Edinger and Aaron M. Cohen and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Identifying Patients for Clinical Studies from Electronic Health Records: {TREC} 2012 Medical Records Track at {OHSU}},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/OHSU.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BedrickECH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCD IIRG at TREC 2012 Medical Track

_James Cogley, Nicola Stokes, John Dunnion, Joe Carthy_

- :fontawesome-solid-user-group: **Participant:** [UCD_CSI](./medical/participants.md#ucd_csi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UCD_CSI.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/UCD_CSI.medical.nb.pdf)
- :material-file-search: **Runs:** [UCDCSI1](./medical/runs.md#ucdcsi1) | [UCDCSI2](./medical/runs.md#ucdcsi2) | [UCDCSI3](./medical/runs.md#ucdcsi3) | [UCDCSI4](./medical/runs.md#ucdcsi4)

??? abstract "Abstract"
	
	This paper describes the participation of UCD IIRG in the TREC 2012 Medical Records track, which fosters research in the retrieval of electronic health records using free text fields. Our contributions to this track investigate several problem areas in the retrieval of medical documents. Multiple knowledge sources are investigated to alleviate the issue of vocabulary mismatch. Medical records are verbose documents that give a full picture of a patient's medical status including their family health information and their own medical history. A Condition Attribution and Temporal Grounding system is implemented to address such occurrences. A rule-based system is employed in order to extract the patient's demographic information from their medical record. All extracted information is then leveraged using Indri's structured query language. These methods are combined to identify patients who fit the exact criteria as described in natural language queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CogleySDC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/CogleySDC12,
		author = {James Cogley and Nicola Stokes and John Dunnion and Joe Carthy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCD} {IIRG} at {TREC} 2012 Medical Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UCD\_CSI.medical.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CogleySDC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLM at TREC 2012 Medical Records Track

_Dina Demner-Fushman, Swapna Abhyankar, Antonio Jimeno-Yepes, Russell F. Loane, François-Michel Lang, James G. Mork, Nicolas Ide, Alan R. Aronson_

- :fontawesome-solid-user-group: **Participant:** [NLM](./medical/participants.md#nlm)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/NLM.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/NLM.medical.final.pdf)
- :material-file-search: **Runs:** [NLMManual](./medical/runs.md#nlmmanual) | [NLMLuceneExp](./medical/runs.md#nlmluceneexp) | [EssieAuto](./medical/runs.md#essieauto) | [NLMLuceneSec](./medical/runs.md#nlmlucenesec)

??? abstract "Abstract"
	
	The NLM team used the relevance judgments for the 2011 Medical Records track (that focused on finding patients eligible for clinical studies) to analyze the components of our 2011 systems. The analysis showed that the components provided moderate improvements over the baseline (established submitting 2011 topics 'as is' to Lucene) for some topics and did not harm the results for any other topics. Our experiments confirmed that implementing methods (such as negation detection and section splitting) motivated by clinical text processing experience could improve identifying patients that meet complex criteria for inclusion in cohort studies. We therefore largely used the 2011 system with minor modifications for document processing. We submitted three automatic runs: an Essie baseline run, and two Lucene runs that used the 2011 system with minor modifications. We also submitted an interactive run for which the queries were interactively modified using Essie until either the top ten retrieved documents appeared mostly relevant or no relevant documents could be found. Our interactive queries submitted to Essie significantly outperformed all our other runs and were significantly above the medians for all submission types (achieving 0.37 infAP; 0.68 infNDCG; 0.75 P@10; and 0.48 R-prec). Interestingly, the values of the two metrics common for the two years of this track are very close to the values achieved in 2011. The hypothetical overall-best and best-manual performances are significantly better than our interactive run. Our Lucene run that used the topic frames and web-based expansion is significantly better than the Lucene baseline run and the medians (on all metrics but P@10 for the medians), but it is not significantly better than our other automatic runs. Our other automatic runs are not significantly above the medians. As in 2011, we conclude that the existing search engines are mature enough to support cohort selection tasks, and the quality of the queries could be significantly improved with a modest interactive effort.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Demner-FushmanA12.bib) "
	```
	@inproceedings{DBLP:conf/trec/Demner-FushmanA12,
		author = {Dina Demner{-}Fushman and Swapna Abhyankar and Antonio Jimeno{-}Yepes and Russell F. Loane and Fran{\c{c}}ois{-}Michel Lang and James G. Mork and Nicolas Ide and Alan R. Aronson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NLM} at {TREC} 2012 Medical Records Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/NLM.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Demner-FushmanA12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCM at TREC 2012: Does Negation Influence The Retrieval of Medical  Reports?

_Alberto Díaz, Miguel Ballesteros, Jorge Carrillo de Albornoz, Laura Plaza_

- :fontawesome-solid-user-group: **Participant:** [NIL_UCM](./medical/participants.md#nil_ucm)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/NIL_UCM.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/NIL_UCM.medical.final.pdf)
- :material-file-search: **Runs:** [ucm4](./medical/runs.md#ucm4) | [ucm5](./medical/runs.md#ucm5) | [ucm3](./medical/runs.md#ucm3) | [ucm1](./medical/runs.md#ucm1)

??? abstract "Abstract"
	
	This paper details the UCM participation in the TREC 2012 Medical Records Track. We present several experiments directed to evaluate the effect of detecting negation in the task of retrieving medical reports. In particular, two different algorithms based on syntactic analysis have been applied to detect negations and to infer their scope. These algorithms are then combined with a simple term-frequency approach using Lucene to retrieve the reports that are relevant to a given query. We evaluate whether ignoring the information that is within the scope of negation may result in a higher retrieving performance. However, our experiments reveal that the effect of negation in this task is not significant.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DiazBAP12.bib) "
	```
	@inproceedings{DBLP:conf/trec/DiazBAP12,
		author = {Alberto D{\'{\i}}az and Miguel Ballesteros and Jorge Carrillo de Albornoz and Laura Plaza},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCM} at {TREC} 2012: Does Negation Influence The Retrieval of Medical Reports?},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/NIL\_UCM.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DiazBAP12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cohort Sherpherd II: Verifying Cohort Constraints from Hospital  Visits

_Travis R. Goodwin, Kirk Roberts, Bryan Rink, Sanda M. Harabagiu_

- :fontawesome-solid-user-group: **Participant:** [UTDHLT](./medical/participants.md#utdhlt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UTDHLT.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/UTDHLT.medical.nb.pdf)
- :material-file-search: **Runs:** [UTDHLTNASK](./medical/runs.md#utdhltnask) | [UTDHLTASK](./medical/runs.md#utdhltask) | [UTDHLTNA](./medical/runs.md#utdhltna) | [UTDHLTA](./medical/runs.md#utdhlta)

??? abstract "Abstract"
	
	This paper describes the updated system created by the University of Texas at Dallas for content-based medical record retrieval submitted to the TREC 2012 Medical Records Track. Our system updates our work from the previous year by building a structured query for each cohort that captures the patient's age, gender, hospital status, and medical assertion information. Further, all keywords that encode any medical phenomena from the query are recursively decomposed before being expanded using knowledge from UMLS, SNOMED, Wikipedia, and PubMed co-occurrences. An initial ranking of hospital visits is then obtained using BM25 relevance on an interpolation of these decomposed keywords. Finally, hospital visits are re-ranked according to the constraints extracted in the structured query. Four runs were submitted, comparing pair-wise combinations of complete vs. shallow keyword decomposition and full vs. negation-only assertion processing. Our highest scoring submission achieved an infNDCG score of 0.426.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoodwinRRH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoodwinRRH12,
		author = {Travis R. Goodwin and Kirk Roberts and Bryan Rink and Sanda M. Harabagiu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Cohort Sherpherd {II:} Verifying Cohort Constraints from Hospital Visits},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UTDHLT.medical.nb.pdf},
		timestamp = {Mon, 19 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GoodwinRRH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LSIS at TREC 2012 Medical Track - Experiments With Conceptualization,  a DFR Model and a Semantic Measure

_Hussam Hamdan, Shereen Albitar, Patrice Bellot, Bernard Espinasse, Sébastien Fournier_

- :fontawesome-solid-user-group: **Participant:** [LSIS](./medical/participants.md#lsis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/LSIS.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/LSIS.medical.final.pdf)
- :material-file-search: **Runs:** [LSIS1](./medical/runs.md#lsis1) | [LSIS2](./medical/runs.md#lsis2) | [LSIS3](./medical/runs.md#lsis3)

??? abstract "Abstract"
	
	In this paper, we present our participation in the Medical Records Track of TREC2012. We focus on the impact of combining the word space and the concept space in the information retrieval process. For this track, we submitted a baseline run by employing the In_expC2 weighting model implemented in the Terrier platform, which achieved fair results (0.304 MAP, 0.51P@10). Then, we expanded the documents by performing automatic text conceptualization using UMLS® and the MetaMap software on medical records. These textual and conceptual representations, still using the DFR model, led to precision (0.29 MAP, 0.47 P@10). We also automatically extended the topics with UMLS® concepts. This led to a lower precision (0.27 MAP, 0.46 P@10) Lastly, we experimented the usage of semantic IR measures only (0.21 MAP, 0.41 P@10)..
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HamdanABEF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/HamdanABEF12,
		author = {Hussam Hamdan and Shereen Albitar and Patrice Bellot and Bernard Espinasse and S{\'{e}}bastien Fournier},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{LSIS} at {TREC} 2012 Medical Track - Experiments With Conceptualization, a {DFR} Model and a Semantic Measure},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/LSIS.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HamdanABEF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Exploration and Learning for Medical Records Search: An Experiment  in Identifying Cohorts for Comparative Effectiveness Research

_Harvey S. Hyman, Warren Fridy III_

- :fontawesome-solid-user-group: **Participant:** [USF_ISDS](./medical/participants.md#usf_isds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/USF_ISDS.medical.pdf](http://trec.nist.gov/pubs/trec21/papers/USF_ISDS.medical.pdf)
- :material-file-search: **Runs:** [USFISDS1](./medical/runs.md#usfisds1) | [USFISDS2](./medical/runs.md#usfisds2)

??? abstract "Abstract"
	
	This paper describes an experiment performed on a medical record data set, using an information retrieval (IR) tool that applies the techniques of exploration and learning, to assist a researcher in identifying the most relevant cohorts. The paper presents some brief background on exploration and learning, how they are incorporated in the IR tool, and an instantiation of exploration and learning used for selecting cohorts for a research population. The research problem addressed in this paper is the TREC 2012 Medical Track task: How to provide content-based access to free-text fields of electronic medical records? The stated goal of the task is to 'find a population over which comparative effectiveness studies can be done.'
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HymanF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/HymanF12,
		author = {Harvey S. Hyman and Warren Fridy III},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Exploration and Learning for Medical Records Search: An Experiment in Identifying Cohorts for Comparative Effectiveness Research},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/USF\_ISDS.medical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HymanF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting SNOMED CT Concepts & Relationships for Clinical  Information Retrieval: Australian e-Health Research Centre and Queensland  University of Technology at the TREC 2012 Medical Track

_Bevan Koopman, Guido Zuccon, Anthony N. Nguyen, Deanne Vickers, Luke Butt, Peter Bruza_

- :fontawesome-solid-user-group: **Participant:** [AEHRC](./medical/participants.md#aehrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/AEHRC.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/AEHRC.medical.nb.pdf)
- :material-file-search: **Runs:** [AEHRClvl0](./medical/runs.md#aehrclvl0) | [AEHRClvl1](./medical/runs.md#aehrclvl1) | [AEHRClvl2](./medical/runs.md#aehrclvl2) | [AEHRCsub](./medical/runs.md#aehrcsub)

??? abstract "Abstract"
	
	The Australian e-Health Research Centre and Queensland University of Technology recently participated in the TREC 2012 Medical Records Track. This paper reports on our methods, results and experience using an approach that exploits the concept and inter-concept relationships defined in the SNOMED CT medical ontology. Our concept-based approach is intended to overcome specific challenges in searching medical records, namely vocabulary mismatch and granularity mismatch. Queries and documents are transformed from their term-based originals into medical concepts as defined by the SNOMED CT ontology, this is done to tackle vocabulary mismatch. In addition, we make use of the SNOMED CT parent-child 'is-a' relationships between concepts to weight documents that contained concept subsumed by the query concepts; this is done to tackle the problem of granularity mismatch. Finally, we experiment with other SNOMED CT relationships besides the is-a relationship to weight concepts related to query concepts. Results show our concept-based approach performed significantly above the median in all four performance metrics. Further improvements are achieved by the incorporation of weighting subsumed concepts, overall leading to improvement above the median of 28% infAP, 10% infNDCG, 12% R-prec and 7% Prec@10. The incorporation of other relations besides is-a demonstrated mixed results, more research is required to determined which SNOMED CT relationships are best employed when weighting related concepts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoopmanZNVBB12.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoopmanZNVBB12,
		author = {Bevan Koopman and Guido Zuccon and Anthony N. Nguyen and Deanne Vickers and Luke Butt and Peter Bruza},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploiting {SNOMED} {CT} Concepts {\&} Relationships for Clinical Information Retrieval: Australian e-Health Research Centre and Queensland University of Technology at the {TREC} 2012 Medical Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/AEHRC.medical.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KoopmanZNVBB12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DCU@TRECMed 2012: Using adhoc Baselines for Domain-Specific Retrieval

_Johannes Leveling, Lorraine Goeuriot, Liadh Kelly, Gareth J. F. Jones_

- :fontawesome-solid-user-group: **Participant:** [DCU](./medical/participants.md#dcu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/DCU.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/DCU.medical.final.pdf)
- :material-file-search: **Runs:** [DCU21](./medical/runs.md#dcu21) | [DCU22](./medical/runs.md#dcu22) | [DCU23b](./medical/runs.md#dcu23b) | [DCU24b](./medical/runs.md#dcu24b)

??? abstract "Abstract"
	
	This paper describes the first participation of DCU in the TREC Medical Records Track (TRECMed) 2012. We performed initial experiments on the the 2011 TRECMed data based on the BM25 retrieval model. Surprisingly, we found that the standard BM25 model with default parameters performs comparable to the best automatic runs submitted to TRECMed 2011 and our experiments would have ranked among the top four out of 29 participating groups. We expected that some form of domain adaptation would increase performance. However, results on the 2011 data proved otherwise: query expansion decreased performance, and filtering and reranking by term proximity also de- creased performance slightly. We submitted four runs based on the BM25 retrieval model to TRECMed 2012 using standard BM25, standard query expansion, result filtering, and concept-based query expansion. Official results for 2012 confirm that domain-specific knowledge, as applied by us, does not increase performance compared to the BM25 baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LevelingGKJ12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LevelingGKJ12,
		author = {Johannes Leveling and Lorraine Goeuriot and Liadh Kelly and Gareth J. F. Jones},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {DCU@TRECMed 2012: Using adhoc Baselines for Domain-Specific Retrieval},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/DCU.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LevelingGKJ12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NICTA and UBC at the TREC 2012 Medical Track

_David Martínez, Arantxa Otegi, Eneko Agirre_

- :fontawesome-solid-user-group: **Participant:** [NICTA](./medical/participants.md#nicta)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/NICTA.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/NICTA.medical.final.pdf)
- :material-file-search: **Runs:** [NICTAUBC1](./medical/runs.md#nictaubc1) | [NICTAUBC2](./medical/runs.md#nictaubc2) | [NICTAUBC4](./medical/runs.md#nictaubc4) | [NICTAUBC6](./medical/runs.md#nictaubc6)

??? abstract "Abstract"
	
	We introduce two heterogeneous query expansion techniques, and a combined system to the TREC 2012 Medical Track. Our methods are based on external resources that provide expansion concepts related to the query terms, by means of the PageRank algorithm, and simple rules based on UMLS Semantic Types. In this paper we show that our systems are able to reach competitive performances at both the TREC-2011 and TREC-2012 tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MartinezOA12.bib) "
	```
	@inproceedings{DBLP:conf/trec/MartinezOA12,
		author = {David Mart{\'{\i}}nez and Arantxa Otegi and Eneko Agirre},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NICTA} and {UBC} at the {TREC} 2012 Medical Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/NICTA.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MartinezOA12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Siena College Medical Information Retrieval System (MIRS)

_Larry R. Medsker, Sharon G. Small_

- :fontawesome-solid-user-group: **Participant:** [SCIAITeam](./medical/participants.md#sciaiteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/SCIAITeam.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/SCIAITeam.medical.nb.pdf)
- :material-file-search: **Runs:** [Siena1](./medical/runs.md#siena1) | [Siena2](./medical/runs.md#siena2) | [Siena3](./medical/runs.md#siena3)

??? abstract "Abstract"
	
	The work done by our MIRS team of three students and two faculty mentors resulted in a baseline system for content-based medical record retrieval. We also made significant progress on an alternative system based on neural computing concepts. The task for the Medical Records TREC in 2012 was to process a list of thirty-four randomly selected queries against a large medical records database to simulate searches for patients who meet the criteria for participating in various clinical trials. The task was to analyze a data set of over 100,000 reports associated with hospital visits and identify patients whose situations were relevant to the queries. Our text retrieval process was done in two separate ways: one used an index created from standard Information Retrieval (IR) software called Lucene and an alternate method based on principles of neural computing. We submitted three runs to the TREC competition, two using our standard Lucene-based approach and one that used elements of neural network analysis. The MIRS team was provided the code necessary to download the Medical Records corpus, consisting of an average of 15 reports from each of approximately 100K patient visits to a hospital. Teams were also provided a training set of 34 sample topic statements from TREC 2011. The records, which comprised one month of reports from multiple hospitals, came from the University of Pittsburgh NLP Repository and were de-identified in regard to specific patient names. The Medical Record track organizers from TREC also provided year 2011 judgment sets, produced by medical professionals at the Oregon Health Science University, that we then used in testing our MIRS software at different states of development. For each topic the system was required to search the medical records data corpus and return a ranked list of the top 10 relevant hospital visits, which were proxies for specific patients whose personal identification was made anonymous by the TREC organizers. It is not yet clear how traditional IR should perform on the identification of patients suitable for the clinical trials. Our first logical step was to run an experiment using traditional simple keyword informational retrieval. We used the open source IR system Lucene to index the NIST-supplied Medical Records corpus and to run our baseline experiments. This Lucene version became the first version of our MIRS system and these results were used as our baseline. Modules were proposed and implemented to improve the keyword identification. Then, the first round of experimentation was run with full error analysis. Modules were modified based on this error analysis, run again on the training collection and finally run on the test collection. Results were submitted to NIST before the deadline of August 11, 2012.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MedskerS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/MedskerS12,
		author = {Larry R. Medsker and Sharon G. Small},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Siena College Medical Information Retrieval System {(MIRS)}},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/SCIAITeam.medical.nb.pdf},
		timestamp = {Thu, 09 Sep 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MedskerS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2012: Medical Records Track

_Jun Miao, Zheng Ye, Jimmy X. Huang_

- :fontawesome-solid-user-group: **Participant:** [york](./medical/participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/york.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/york.medical.nb.pdf)
- :material-file-search: **Runs:** [YorkUMB1](./medical/runs.md#yorkumb1) | [YorkUMC2](./medical/runs.md#yorkumc2) | [YorkUMQ3](./medical/runs.md#yorkumq3) | [YorkUMP4](./medical/runs.md#yorkump4)

??? abstract "Abstract"
	
	In this paper, we present our participation in the Medical Records Track of TREC 2012. This is the second time we take part in this track. 50 new topics have been published in this year. The goal of this track is still to find relevant patients that have particular diseases and/or treatments. To achieve this goal, we try four methods which include popular techniques like query expansion, concept recognition and so on. Four runs have been submitted and they are based on our previous work. Detailed discussion has been made to show the effectiveness of different techniques on the Medical Records dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MiaoYH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/MiaoYH12,
		author = {Jun Miao and Zheng Ye and Jimmy X. Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2012: Medical Records Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/york.medical.nb.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MiaoYH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting Domain Thesaurus for Medical Record Retrieval

_Miguel A. Callejas P., Yue Wang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./medical/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/udel_fang.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/udel_fang.medical.nb.pdf)
- :material-file-search: **Runs:** [UDInfoMed123](./medical/runs.md#udinfomed123) | [UDInfoMed12](./medical/runs.md#udinfomed12) | [UDInfoMed1](./medical/runs.md#udinfomed1)

??? abstract "Abstract"
	
	InfoLab at the University of Delaware participated in the TREC 2012 Medical Records Track. This paper explains our method and describes experiment results. One limitation of existing keyword matching based retrieval functions is the problem of vocabulary mismatch. To overcome this limitation, we propose to first map topics and visits to bags of concepts using domain thesaurus, and then model the relevance based on the similarities between those concepts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PWF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/PWF12,
		author = {Miguel A. Callejas P. and Yue Wang and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploiting Domain Thesaurus for Medical Record Retrieval},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/udel\_fang.medical.nb.pdf},
		timestamp = {Thu, 17 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PWF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieving Medical Records with "sennamed": NEC Labs America at  TREC 2012 Medical Record Track

_Yanjun Qi, Pierre-François Laquerre_

- :fontawesome-solid-user-group: **Participant:** [sennamed](./medical/participants.md#sennamed)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/sennamed.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/sennamed.medical.final.pdf)
- :material-file-search: **Runs:** [sennamedlsi](./medical/runs.md#sennamedlsi) | [sennamed1](./medical/runs.md#sennamed1) | [sennamed2](./medical/runs.md#sennamed2) | [sennamed3](./medical/runs.md#sennamed3)

??? abstract "Abstract"
	
	In this notebook, we describe the automatic retrieval runs from NEC Laboratories America (NECLA) for the Text REtrieval Conference (TREC) 2012 Medical Records track. Our approach is based on a combination of UMLS medical concept detection and a set of simple retrieval models. Our best run, sennamed2, has achieved the best inferred average precision (infAP) score on 5 of the 47 test topics, and obtained a higher score than the median of all submission runs on 27 other topics. Overall, sennamed2 ranks at the second place amongst all the 82 automatic runs submitted for this track, and obtains the third place amongst both automatic and manual submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiL12.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiL12,
		author = {Yanjun Qi and Pierre{-}Fran{\c{c}}ois Laquerre},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Retrieving Medical Records with "sennamed": {NEC} Labs America at {TREC} 2012 Medical Record Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/sennamed.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiL12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Ensemble Approach for Expanding Queries

_Duy Duc An Bui, Doug Redd, Thomas C. Rindflesch, Qing Zeng-Treitler_

- :fontawesome-solid-user-group: **Participant:** [BMIUOU](./medical/participants.md#bmiuou)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/BMIUOU.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/BMIUOU.medical.final.pdf)
- :material-file-search: **Runs:** [BMIUOUsyn](./medical/runs.md#bmiuousyn) | [BMIUOUbase](./medical/runs.md#bmiuoubase) | [BMIUOUens](./medical/runs.md#bmiuouens) | [BMIUOUensneg](./medical/runs.md#bmiuouensneg)

??? abstract "Abstract"
	
	In our TREC participation, we used an ensemble approach in query expansion. Query expansion, such as synonym expansion, had shown promising results in medical literature search. On the other hand, some of the 2011 papers reported worse results from expansion. Since there are multiple knowledge sources available and each resource has clear strengths and weaknesses, we tested the combination of three expansion methods versus each individual method. We found that the ensemble approach performed better (in terms of average infAP, infNDCG, R-prec, and P10) than the individual methods and better than the Lucene baseline. The individual expansion methods, however, did not improve the baseline Lucene performance. We also performed an unofficial run using a concept index to boost the query performance, which led to small improvements in infAP, infNDCG, and R-prec.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ReddZBRR12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ReddZBRR12,
		author = {Duy Duc An Bui and Doug Redd and Thomas C. Rindflesch and Qing Zeng{-}Treitler},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {An Ensemble Approach for Expanding Queries},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/BMIUOU.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ReddZBRR12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Atigeo at TREC 2012 Medical Records Track: ICD-9 Code Description  Injection to Enhance Electronic Medical Record Search Accuracy

_Bryan Tinsley, Alex Thomas, Joseph F. McCarthy, Mike Lazarus_

- :fontawesome-solid-user-group: **Participant:** [xMusketeers](./medical/participants.md#xmusketeers)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/atigeo.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/atigeo.medical.final.pdf)
- :material-file-search: **Runs:** [atigeo0](./medical/runs.md#atigeo0) | [atigeo1](./medical/runs.md#atigeo1) | [atigeo2](./medical/runs.md#atigeo2) | [atigeo3](./medical/runs.md#atigeo3)

??? abstract "Abstract"
	
	The TREC 2012 Medical Records Track task involves the identification of electronic medical records (EMRs) that are relevant to a set of search topics. Atigeo has a Computer-Aided Coding (CAC) product that analyzes electronic medical records (EMRs) and recommends ICD-9 codes that represent the diagnoses and procedures described in those medical records. We have developed a suite of natural language processing (NLP) components that are useful for both tasks. Our TREC 2012 experiments focused on the ICD-9 admission and diagnosis codes included in more than 90% of the TREC EMRs: we used our comprehensive ICD-9 database to insert one of three variants of the text descriptions associated with each code found in each EMR. We describe the variations of ICD-9 code descriptions we inserted, the NLP components used for processing all the reports and topics, and report on the results of our experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TinsleyTML12.bib) "
	```
	@inproceedings{DBLP:conf/trec/TinsleyTML12,
		author = {Bryan Tinsley and Alex Thomas and Joseph F. McCarthy and Mike Lazarus},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Atigeo at {TREC} 2012 Medical Records Track: {ICD-9} Code Description Injection to Enhance Electronic Medical Record Search Accuracy},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/atigeo.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TinsleyTML12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Three Questions About Clinical Information Retrieval

_Stephen T. Wu, James J. Masanz, K. E. Ravikumar, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [MayoClinicNLP](./medical/participants.md#mayoclinicnlp)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/MayoClinicNLP.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/MayoClinicNLP.medical.final.pdf)
- :material-file-search: **Runs:** [MayoLucene](./medical/runs.md#mayolucene) | [MayoMetaData](./medical/runs.md#mayometadata) | [MayoPayload](./medical/runs.md#mayopayload) | [MayoExpanded](./medical/runs.md#mayoexpanded)

??? abstract "Abstract"
	
	Electronic Medical Records (EMRs) have greatly expanded the potential for the evidence-based improvement of clinical practice by providing a data source for computable medical information. The Text REtrieval Conference 2012 Medical Records Track (TREC-med) explored how information retrieval may support clinical research by providing an efficient means to identify cohorts for clinical studies. A shared task called participants to find cohorts of relevant patients for 50 different topic queries. The users in TREC-med information retrieval systems would be medical experts who are searching for cohorts. In our previous work, we have collaborated with such experts on specific queries; the assortment of 50 queries makes this competition a standardized benchmark task. Thus, techniques that have shown case-by-case improvement can be tested against a much larger number of queries. We have taken this opportunity to investigate three core questions around which many of our algorithms are designed: 1. What is the relative value of structured data (e.g., fields in EMRs, or document metadata) compared to clinical text? 2. Are extensive information extraction (IE) efforts any benefit when we consider the applied question of information retrieval (IR)? 3. Can distributional semantics help supply missing information in a query? For each of these three questions, we have extended Apache Lucene1 with pre-existing techniques and tested on the TREC-med cohort identification task. In testing these independently, we aim to find generalizable principles for cohort identification in other documents collections and queries. The rest of this paper describes the TREC 2012 Medical Records task, describes Mayo Clinic's run submissions in detail, and reports evaluation results with subsequent discussion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuMRL12.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuMRL12,
		author = {Stephen T. Wu and James J. Masanz and K. E. Ravikumar and Hongfang Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Three Questions About Clinical Information Retrieval},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/MayoClinicNLP.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuMRL12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at 2012 TREC Medical Track: Query Expansion, Retrieval and  Ranking

_Jiayue Zhang, Lin Lin, Shudang Diao, Yukun Li, Runnan Liu, Weiran Xu, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./medical/participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/PRIS.medical.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/PRIS.medical.nb.pdf)
- :material-file-search: **Runs:** [buptprisBase](./medical/runs.md#buptprisbase) | [buptprisInt](./medical/runs.md#buptprisint) | [buptprisCscr](./medical/runs.md#buptpriscscr) | [buptprisLrnk](./medical/runs.md#buptprislrnk)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangLDLLXG12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangLDLLXG12,
		author = {Jiayue Zhang and Lin Lin and Shudang Diao and Yukun Li and Runnan Liu and Weiran Xu and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at 2012 {TREC} Medical Track: Query Expansion, Retrieval and Ranking},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/PRIS.medical.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangLDLLXG12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring Evidence Aggregation Methods and External Expansion Sources  for Medical Record Search

_Dongqing Zhu, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [udel](./medical/participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/udel.medical.final.pdf](http://trec.nist.gov/pubs/trec21/papers/udel.medical.final.pdf)
- :material-file-search: **Runs:** [udelMNZ](./medical/runs.md#udelmnz) | [udelSUM](./medical/runs.md#udelsum) | [udelMRF](./medical/runs.md#udelmrf) | [udelMED](./medical/runs.md#udelmed)

??? abstract "Abstract"
	
	This paper describes and analyzes experiments we performed for the Medical Records track in the 2012 Text REtrieval Conference (TREC). We mainly investigated three research problems: 1. Evidence Aggregation: In last year's track there were two different methods in general for obtaining a visit ranking out of reports (smaller document units), i.e., (A) using reports as indexing and retrieval units and then converting a report ranking into a visit ranking, and (B) using visits as indexing and retrieval units by concatenating reports at the very first stage and then obtain a visit ranking directly. Method A avoids the potential problem of varying visit document length, while Method B naturally aggregates evidence scatter over multiple reports and easily obtains a visit ranking. It is unclear which method is better based on all reported results. Thus, we compared the two approaches, tried various score aggregation methods for (A), and combined both approaches in a way that further improved the system performance. 2. Expansion Sources: We tested a variety of external collections (ranging from general web datasets to domain-specific thesauri, and from Megabyte datasets to Terabyte datasets) for query expansion, compared their effectiveness, and obtained useful insights into the data. 3. Retrieval Models: We tested several statistical IR models (proven to be effective on news and web collections) on this medical collection, and explored ways to combine these models to address different aspects of task. For instance, we used MRF model to model term proximity since most medical concepts are phrases. We also used a mixture of relevance models to obtain various relevant expansion terms covered by different expansion collections respectively, which is expect to significantly alleviate the vocabulary mismatch between medical terminologies. For TREC submissions, we tested systems that combined multiple IR models, leveraged diverse expansion sources, and used various evidence aggregation methods. We implemented all the retrieval models in the Indri1 retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuC12,
		author = {Dongqing Zhu and Ben Carterette},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploring Evidence Aggregation Methods and External Expansion Sources for Medical Record Search},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/udel.medical.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2012: Experiments with Terrier in  Medical Records, Microblog, and Web Tracks

_Nut Limsopatham, Richard McCreadie, M-Dyaa Albakour, Craig Macdonald, Rodrygo L. T. Santos, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./medical/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/uogTr.medical.microblog.web.final.pdf](http://trec.nist.gov/pubs/trec21/papers/uogTr.medical.microblog.web.final.pdf)
- :material-file-search: **Runs:** [uogTrMConQ](./medical/runs.md#uogtrmconq) | [uogTrMConQRa](./medical/runs.md#uogtrmconqra) | [uogTrMConQRd](./medical/runs.md#uogtrmconqrd) | [uogTrMConQT](./medical/runs.md#uogtrmconqt)

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

## Session 

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

- :fontawesome-solid-user-group: **Participant:** [CWI](./session/participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/CWI.kba.session.final.pdf](http://trec.nist.gov/pubs/trec21/papers/CWI.kba.session.final.pdf)
- :material-file-search: **Runs:** [CWIrun1.RL1](./session/runs.md#cwirun1.rl1) | [CWIrun1.RL2](./session/runs.md#cwirun1.rl2) | [CWIrun1.RL3](./session/runs.md#cwirun1.rl3) | [CWIrun1.RL4](./session/runs.md#cwirun1.rl4) | [TUDrun.RL1](./session/runs.md#tudrun.rl1) | [TUDrun.RL2](./session/runs.md#tudrun.rl2) | [TUDrun.RL3](./session/runs.md#tudrun.rl3) | [TUDrun.RL4](./session/runs.md#tudrun.rl4) | [CWIrun3.RL1](./session/runs.md#cwirun3.rl1) | [CWIrun3.RL2](./session/runs.md#cwirun3.rl2) | [CWIrun3.RL3](./session/runs.md#cwirun3.rl3) | [CWIrun3.RL4](./session/runs.md#cwirun3.rl4)

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

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./session/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/ICTNET.session.final.pdf](http://trec.nist.gov/pubs/trec21/papers/ICTNET.session.final.pdf)
- :material-file-search: **Runs:** [ICTNET12SER1.RL1](./session/runs.md#ictnet12ser1.rl1) | [ICTNET12SER1.RL2](./session/runs.md#ictnet12ser1.rl2) | [ICTNET12SER1.RL3](./session/runs.md#ictnet12ser1.rl3) | [ICTNET12SER1.RL4](./session/runs.md#ictnet12ser1.rl4) | [ICTNET12SER2.RL1](./session/runs.md#ictnet12ser2.rl1) | [ICTNET12SER2.RL2](./session/runs.md#ictnet12ser2.rl2) | [ICTNET12SER2.RL3](./session/runs.md#ictnet12ser2.rl3) | [ICTNET12SER2.RL4](./session/runs.md#ictnet12ser2.rl4) | [ICTNET12SER3.RL1](./session/runs.md#ictnet12ser3.rl1) | [ICTNET12SER3.RL2](./session/runs.md#ictnet12ser3.rl2) | [ICTNET12SER3.RL3](./session/runs.md#ictnet12ser3.rl3) | [ICTNET12SER3.RL4](./session/runs.md#ictnet12ser3.rl4)

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

- :fontawesome-solid-user-group: **Participant:** [Georgetown](./session/participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/Georgetown.session.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/Georgetown.session.nb.pdf)
- :material-file-search: **Runs:** [guphrase1.RL1](./session/runs.md#guphrase1.rl1) | [guphrase1.RL2](./session/runs.md#guphrase1.rl2) | [guphrase1.RL3](./session/runs.md#guphrase1.rl3) | [guphrase1.RL4](./session/runs.md#guphrase1.rl4) | [guphrase2.RL1](./session/runs.md#guphrase2.rl1) | [guphrase2.RL2](./session/runs.md#guphrase2.rl2) | [guphrase2.RL3](./session/runs.md#guphrase2.rl3) | [guphrase2.RL4](./session/runs.md#guphrase2.rl4) | [gurelaxphr.RL1](./session/runs.md#gurelaxphr.rl1) | [gurelaxphr.RL2](./session/runs.md#gurelaxphr.rl2) | [gurelaxphr.RL3](./session/runs.md#gurelaxphr.rl3) | [gurelaxphr.RL4](./session/runs.md#gurelaxphr.rl4)

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

- :fontawesome-solid-user-group: **Participant:** [webis](./session/participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/webis.session.final.pdf](http://trec.nist.gov/pubs/trec21/papers/webis.session.final.pdf)
- :material-file-search: **Runs:** [webis12cnqe.RL1](./session/runs.md#webis12cnqe.rl1) | [webis12cnqe.RL2](./session/runs.md#webis12cnqe.rl2) | [webis12cnqe.RL3](./session/runs.md#webis12cnqe.rl3) | [webis12cnqe.RL4](./session/runs.md#webis12cnqe.rl4) | [webis12indqe.RL1](./session/runs.md#webis12indqe.rl1) | [webis12indqe.RL2](./session/runs.md#webis12indqe.rl2) | [webis12indqe.RL3](./session/runs.md#webis12indqe.rl3) | [webis12indqe.RL4](./session/runs.md#webis12indqe.rl4) | [webis12cnse.RL1](./session/runs.md#webis12cnse.rl1) | [webis12cnse.RL2](./session/runs.md#webis12cnse.rl2) | [webis12cnse.RL3](./session/runs.md#webis12cnse.rl3) | [webis12cnse.RL4](./session/runs.md#webis12cnse.rl4)

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

- :fontawesome-solid-user-group: **Participant:** [PITT](./session/participants.md#pitt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/PITT.session.final.pdf](http://trec.nist.gov/pubs/trec21/papers/PITT.session.final.pdf)
- :material-file-search: **Runs:** [PITTSHQM.RL1](./session/runs.md#pittshqm.rl1) | [PITTSHQM.RL2](./session/runs.md#pittshqm.rl2) | [PITTSHQM.RL3](./session/runs.md#pittshqm.rl3) | [PITTSHQM.RL4](./session/runs.md#pittshqm.rl4) | [PITTSHQMnov.RL1](./session/runs.md#pittshqmnov.rl1) | [PITTSHQMnov.RL2](./session/runs.md#pittshqmnov.rl2) | [PITTSHQMnov.RL3](./session/runs.md#pittshqmnov.rl3) | [PITTSHQMnov.RL4](./session/runs.md#pittshqmnov.rl4) | [PITTSHQMsdm.RL1](./session/runs.md#pittshqmsdm.rl1) | [PITTSHQMsdm.RL2](./session/runs.md#pittshqmsdm.rl2) | [PITTSHQMsdm.RL3](./session/runs.md#pittshqmsdm.rl3) | [PITTSHQMsnov.RL1](./session/runs.md#pittshqmsnov.rl1) | [PITTSHQMsnov.RL2](./session/runs.md#pittshqmsnov.rl2) | [PITTSHQMsnov.RL3](./session/runs.md#pittshqmsnov.rl3) | [PITTSHQMsnov.RL4](./session/runs.md#pittshqmsnov.rl4) | [PITTSHQMsdm.RL4](./session/runs.md#pittshqmsdm.rl4)

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

- :fontawesome-solid-user-group: **Participant:** [ruiiltrec2012](./session/participants.md#ruiiltrec2012)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/ruiiltrec.session.final.pdf](http://trec.nist.gov/pubs/trec21/papers/ruiiltrec.session.final.pdf)
- :material-file-search: **Runs:** [RutgersHu.RL1](./session/runs.md#rutgershu.rl1) | [RutgersHu.RL2](./session/runs.md#rutgershu.rl2) | [RutgersHu.RL3](./session/runs.md#rutgershu.rl3) | [RutgersHu.RL4](./session/runs.md#rutgershu.rl4) | [RutgersM.RL1](./session/runs.md#rutgersm.rl1) | [RutgersM.RL2](./session/runs.md#rutgersm.rl2) | [RutgersM.RL3](./session/runs.md#rutgersm.rl3) | [RutgersM.RL4](./session/runs.md#rutgersm.rl4)

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

- :fontawesome-solid-user-group: **Participant:** [UAlbanySession](./session/participants.md#ualbanysession)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UAlbany-USC.session.pdf](http://trec.nist.gov/pubs/trec21/papers/UAlbany-USC.session.pdf)
- :material-file-search: **Runs:** [UAlbany.RL1](./session/runs.md#ualbany.rl1) | [UAlbany.RL2](./session/runs.md#ualbany.rl2) | [UAlbany.RL3](./session/runs.md#ualbany.rl3) | [UAlbany.RL4](./session/runs.md#ualbany.rl4)

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

- :fontawesome-solid-user-group: **Participant:** [pris411](./session/participants.md#pris411)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/BUPT_WILDCAT.session.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/BUPT_WILDCAT.session.nb.pdf)
- :material-file-search: **Runs:** [wildcat1.RL1](./session/runs.md#wildcat1.rl1) | [wildcat1.RL2](./session/runs.md#wildcat1.rl2) | [wildcat1.RL3](./session/runs.md#wildcat1.rl3) | [wildcat1.RL4](./session/runs.md#wildcat1.rl4) | [wildcat2.RL1](./session/runs.md#wildcat2.rl1) | [wildcat2.RL2](./session/runs.md#wildcat2.rl2) | [wildcat2.RL3](./session/runs.md#wildcat2.rl3) | [wildcat2.RL4](./session/runs.md#wildcat2.rl4) | [wildcat3.RL1](./session/runs.md#wildcat3.rl1) | [wildcat3.RL2](./session/runs.md#wildcat3.rl2) | [wildcat3.RL3](./session/runs.md#wildcat3.rl3) | [wildcat3.RL4](./session/runs.md#wildcat3.rl4)

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

## Crowdsourcing 

#### Overview of the TREC 2012 Crowdsourcing Track

_Mark D. Smucker, Gabriella Kazai, Matthew Lease_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/CROWD12.overview.pdf](http://trec.nist.gov/pubs/trec21/papers/CROWD12.overview.pdf)
??? abstract "Abstract"
	
	In 2012, the Crowdsourcing track had two separate tasks: a text relevance assessing task (TRAT) and an image relevance assessing task (IRAT). This track overview describes the track and provides analysis of the track's results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmuckerKL12.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmuckerKL12,
		author = {Mark D. Smucker and Gabriella Kazai and Matthew Lease},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2012 Crowdsourcing Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/CROWD12.overview.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmuckerKL12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Hybrid Methods for Relevance Assessment in TREC Crowd '12

_Christopher G. Harris, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [UIowaS](./crowd/participants.md#uiowas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UIowaS.crowd.final.pdf](http://trec.nist.gov/pubs/trec21/papers/UIowaS.crowd.final.pdf)
- :material-file-search: **Runs:** [UIowaS01r](./crowd/runs.md#uiowas01r) | [UIowaS02r](./crowd/runs.md#uiowas02r) | [UIowaS03r](./crowd/runs.md#uiowas03r)

??? abstract "Abstract"
	
	The University of Iowa (UIowaS) submitted three runs to the TRAT subtask of the 2012 TREC Crowdsourcing track. The task objective was to evaluate approaches to crowdsourcing high quality relevance judgments for a text document collection. We used this as an opportunity to examine three hybrid (combination of human-based and machine-based) approaches while simultaneously limiting time and cost. We create a training set from topics, which were previously assessed for relevance on the same document set, and use this training set to build strategies. We apply machine approaches, including clustering, to order documents for each topic, and then ask crowdworkers to provide relevance judgments for a subset of documents. One of our runs provides the best logistic average misclassification (LAM) rates of all submitted TRAT runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001S12.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001S12,
		author = {Christopher G. Harris and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Hybrid Methods for Relevance Assessment in {TREC} Crowd '12},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UIowaS.crowd.final.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001S12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Northeastern University Runs at the TREC12 Crowdsourcing Track

_Maryam Bashir, Jesse Anderton, Jie Wu, Matthew Ekstrand-Abueg, Peter B. Golbus, Virgil Pavlu, Javed A. Aslam_

- :fontawesome-solid-user-group: **Participant:** [NEU](./crowd/participants.md#neu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/NEU.crowd.final.pdf](http://trec.nist.gov/pubs/trec21/papers/NEU.crowd.final.pdf)
- :material-file-search: **Runs:** [NEUElo2](./crowd/runs.md#neuelo2) | [NEUElo3](./crowd/runs.md#neuelo3) | [NEUElo4](./crowd/runs.md#neuelo4) | [NEUElo5](./crowd/runs.md#neuelo5) | [NEUEM1](./crowd/runs.md#neuem1) | [NEUNugget12](./crowd/runs.md#neunugget12)

??? abstract "Abstract"
	
	The goal of the TREC 2012 Crowdsourcing Track was to evaluate approaches to crowdsourcing high quality relevance judgments for images and text documents. This paper describes our submission to the Text Relevance Assessing Task. We explored three different approaches for obtaining relevance judgments. Our first two approaches are based on collecting a limited number of preference judgments from Amazon Mechanical Turk workers. These preferences are then extended to relevance judgments through the use of expectation maximization and the Elo rating system. Our third approach is based on our Nugget-based evaluation paradigm.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BashirAWEGPA12.bib) "
	```
	@inproceedings{DBLP:conf/trec/BashirAWEGPA12,
		author = {Maryam Bashir and Jesse Anderton and Jie Wu and Matthew Ekstrand{-}Abueg and Peter B. Golbus and Virgil Pavlu and Javed A. Aslam},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Northeastern University Runs at the {TREC12} Crowdsourcing Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/NEU.crowd.final.pdf},
		timestamp = {Sat, 14 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BashirAWEGPA12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2012: CrowdSourcing Track

_Qinmin Hu, Zhi Xu, Xanghi Huang, Zheng Ye_

- :fontawesome-solid-user-group: **Participant:** [york](./crowd/participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/york.crowd.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/york.crowd.nb.pdf)
- :material-file-search: **Runs:** [yorku12cs01](./crowd/runs.md#yorku12cs01) | [yorku12cs02](./crowd/runs.md#yorku12cs02) | [yorku12cs03](./crowd/runs.md#yorku12cs03) | [yorku12cs04](./crowd/runs.md#yorku12cs04)

??? abstract "Abstract"
	
	The objective of this work is to address the challenges in managing and analyzing crowdsourcing in the information retrieval field. In particular, we would like to answer the following questions: (1) how to control the quality of the workers when crowdsourcing? (2) How to design the interface such that the workers are willing to participate in and are driven to give useful feedback information? (3) How to make use the crowdsourcing information in the IR systems? The crowdsourcing system called CrowdFlower is employed and four classic information retrieval models are applied in our proposed approaches. Our experimental results show that the IR systems refine the results crowdsourcing by minimizing the manual work and the cost is much less
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuXHY12.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuXHY12,
		author = {Qinmin Hu and Zhi Xu and Xanghi Huang and Zheng Ye},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2012: CrowdSourcing Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/york.crowd.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HuXHY12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Skierarchy: Extending the Power of Crowdsourcing Using a Hierarchy  of Domain Experts, Crowd and Machine Learning

_Ramesh Nellapati, Sanga Peerreddy, Prateek Singhal_

- :fontawesome-solid-user-group: **Participant:** [SetuServ](./crowd/participants.md#setuserv)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/SetuServ.crowd.final.pdf](http://trec.nist.gov/pubs/trec21/papers/SetuServ.crowd.final.pdf)
- :material-file-search: **Runs:** [SetuServtest](./crowd/runs.md#setuservtest) | [SSML2pct](./crowd/runs.md#ssml2pct) | [SSNoEC](./crowd/runs.md#ssnoec) | [SSEC3incl](./crowd/runs.md#ssec3incl) | [SSEC3excl](./crowd/runs.md#ssec3excl) | [SSEC3inclML](./crowd/runs.md#ssec3inclml) | [SSECML75pct](./crowd/runs.md#ssecml75pct) | [SSECML50pct](./crowd/runs.md#ssecml50pct) | [SSECML2to99](./crowd/runs.md#ssecml2to99) | [testrun](./crowd/runs.md#testrun) | [SSPreEC](./crowd/runs.md#sspreec) | [SSPostEC](./crowd/runs.md#sspostec) | [SSPostECv2](./crowd/runs.md#sspostecv2)

??? abstract "Abstract"
	
	In the last few years, crowdsourcing has emerged as an effective solution for large-scale 'micro-tasks'. Usually, the micro-tasks that are accomplished using crowdsourcing tend to be those that computers cannot solve very effectively, but are fairly trivial for humans with no specialized training. In this work, we aim to extend the capability of crowdsourcing to tasks that are complex even from a human perspective. Towards this objective, we present a novel hierarchical approach involving a small number of domain experts at the top of the hierarchy, a large crowd with generic skills at the intermediate level, and a Machine Learning system serving as a personal assistant to the crowd, at the bottom level. We call this approach Skierarchy, short for Hierarchy of Skills. To test the efficacy of the Skierarchy approach, we deployed the model on the TREC 2012 TRAT task, a task we believe is fairly complex compared to typical micro-tasks. In this paper, we present illustrative experiments to demonstrate the utility of each of the layers of our hierarchy. Our experiments on TRAT as well as IRAT show that using an interactive process between the experts and the crowd could significantly reduce the need for redundancy among the crowd, while also enabling a crowd with generic skills to perform tasks that are reserved for specialists. Further, we found from our TRAT experience that both the crowd and the Machine Learning system improve their performance over time as they gain experience on specialized tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NellapatiPS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/NellapatiPS12,
		author = {Ramesh Nellapati and Sanga Peerreddy and Prateek Singhal},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Skierarchy: Extending the Power of Crowdsourcing Using a Hierarchy of Domain Experts, Crowd and Machine Learning},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/SetuServ.crowd.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NellapatiPS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using a Bayesian Model to Combine LDA Features with Crowdsourced  Responses

_Edwin Simpson, Steven Reece, Antonio Penta, Sarvapali D. Ramchurn_

- :fontawesome-solid-user-group: **Participant:** [HAC](./crowd/participants.md#hac)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/HAC.crowd.final.pdf](http://trec.nist.gov/pubs/trec21/papers/HAC.crowd.final.pdf)
- :material-file-search: **Runs:** [OrcVB1](./crowd/runs.md#orcvb1) | [OrcVB1Conf](./crowd/runs.md#orcvb1conf) | [OrcVBW80Conf](./crowd/runs.md#orcvbw80conf) | [OrcVBW80](./crowd/runs.md#orcvbw80) | [OrcVBW9Conf](./crowd/runs.md#orcvbw9conf) | [Orc2Stage](./crowd/runs.md#orc2stage) | [Orc2G](./crowd/runs.md#orc2g) | [Orc2GUL](./crowd/runs.md#orc2gul) | [Orc2GULConf](./crowd/runs.md#orc2gulconf) | [OrcVBW16Conf](./crowd/runs.md#orcvbw16conf)

??? abstract "Abstract"
	
	This paper describes a crowdsourcing system that integrates machine learning techniques with human classifiers, showing how to apply a Bayesian approach to classifier combination to the challenge of crowdsourcing document topic labels. First, we use a number of NLP techniques to extract informative document features. We then screen and select workers using Amazon Mechanical Turk to label selected documents. We then apply Independent Bayesian Classifier Combination (IBCC) to classify the complete set of documents in a semi-supervised manner, taking into account the unreliability of crowd-sourced labels. More documents are then selected intelligently for labeling by the crowd. We demonstrate superior results using IBCC compared to a two-stage classifier and strong performance with only 16% documents labelled by the crowd.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SimpsonRPR12.bib) "
	```
	@inproceedings{DBLP:conf/trec/SimpsonRPR12,
		author = {Edwin Simpson and Steven Reece and Antonio Penta and Sarvapali D. Ramchurn},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using a Bayesian Model to Combine {LDA} Features with Crowdsourced Responses},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/HAC.crowd.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SimpsonRPR12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BUPT_PRIS at TREC 2012 Crowdsourcing Track 1

_Chuang Zhang, Minjie Zeng, Xiaokang Sang, Kailai Zhang, Houfu Kang_

- :fontawesome-solid-user-group: **Participant:** [pris411](./crowd/participants.md#pris411)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/BUPT_WILDCAT.crowd.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/BUPT_WILDCAT.crowd.nb.pdf)
- :material-file-search: **Runs:** [BUPTPRISZHS](./crowd/runs.md#buptpriszhs)

??? abstract "Abstract"
	
	In this paper, the strategies and methods used by the team BUPT-WILDCAT in the TREC 2012 Crowdsourcing Track1 will be mainly introduced. The Crowdsourcing solution is designed and carried out on the CrowdFlower Platform. Corwdsourcing tasks are released on the AMT. The relevance labels are gathered from workers of AMT and optimized by the inner algorithms of Crowdflower Platform.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangZSZK12.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangZSZK12,
		author = {Chuang Zhang and Minjie Zeng and Xiaokang Sang and Kailai Zhang and Houfu Kang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BUPT{\_}PRIS at {TREC} 2012 Crowdsourcing Track 1},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/BUPT\_WILDCAT.crowd.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangZSZK12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Knowledge Base Acceleration 

#### Building an Entity-Centric Stream Filtering Test Collection for TREC  2012

_John R. Frank, Max Kleiman-Weiner, Daniel A. Roberts, Feng Niu, Ce Zhang, Christopher Ré, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/KBA.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec21/papers/KBA.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Knowledge Base Acceleration track in TREC 2012 focused on a single task: filter a time-ordered corpus for documents that are highly relevant to a predefined list of entities. KBA differs from previous filtering evaluations in two primary ways: the stream corpus is >100x larger than previous filtering collections, and the use of entities as topics enables systems to incorporate structured knowledge bases (KB), such as Wikipedia, as external data sources. A successful KBA system must do more than resolve the meaning of entity mentions by linking documents to the KB: it must also distinguish centrally relevant documents that are worth citing in the entity's WP article. This combines thinking from natural language processing (NLP) and information retrieval (IR). Filtering tracks in TREC have typically used queries based on topics described by a set of keyword queries or short descriptions, and annotators have generated relevance judgments based on their personal interpretation of the topic. For TREC 2012, we selected a set of filter topics based on Wikipedia entities: 27 people and 2 organizations. Such named entities are more familiar in NLP than IR. We also constructed an entirely new stream corpus spanning 4,973 consecutive hours from October 2011 through April 2012. It contains over 400M documents, which we augmented with named entity classification tagging for the ~40% of the documents identified as English. Each document has a timestamp that places it in the stream. The 29 target entities were mentioned infrequently enough in the corpus that NIST assessors could judge the relevance of most of the mentioning documents (~91%). Judgments for documents from before January 2012 were provided to TREC teams as training data for filtering documents from the remaining hours. Run submissions were evaluated against the assessor-generated list of citation-worthy documents. We present peak F_1 scores averaged across the entities for all run submissions. High scoring systems used a variety of approaches, including simple name matching, names of related entities from the knowledge base, and support vector machines. Top scoring systems achieved F_1 scores in the high 30s or low 40s depending on score averaging techniques. We discuss key lessons learned at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FrankKRNZRS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/FrankKRNZRS12,
		author = {John R. Frank and Max Kleiman{-}Weiner and Daniel A. Roberts and Feng Niu and Ce Zhang and Christopher R{\'{e}} and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Building an Entity-Centric Stream Filtering Test Collection for {TREC} 2012},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/KBA.OVERVIEW.pdf},
		timestamp = {Tue, 12 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FrankKRNZRS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at TREC 2012

_Richard Berendsen, Edgar Meij, Daan Odijk, Maarten de Rijke, Wouter Weerkamp_

- :fontawesome-solid-user-group: **Participant:** [UvA](./kba/participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UvA.microblog.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/UvA.microblog.kba.final.pdf)
- :material-file-search: **Runs:** [UvA-UvAbaseline](./kba/runs.md#uva-uvabaseline) | [UvA-UvALearning](./kba/runs.md#uva-uvalearning) | [UvA-UvAIncLearnHigh](./kba/runs.md#uva-uvainclearnhigh) | [UvA-UvAIncLearnLow](./kba/runs.md#uva-uvainclearnlow) | [UvA-UvAIncLearnT25](./kba/runs.md#uva-uvainclearnt25) | [UvA-UvAIncLearnT50](./kba/runs.md#uva-uvainclearnt50)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's ILPS group in the Knowledge Base Acceleration and Microblog tracks at TREC 2012.
	

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

#### LSIS/LIA at TREC 2012 Knowledge Base Acceleration

_Ludovic Bonnefoy, Vincent Bouvier, Patrice Bellot_

- :fontawesome-solid-user-group: **Participant:** [LSIS](./kba/participants.md#lsis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/LSIS.LIA.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/LSIS.LIA.kba.final.pdf)
- :material-file-search: **Runs:** [LSIS-lsisSys1](./kba/runs.md#lsis-lsissys1) | [LSIS-lsisSys2](./kba/runs.md#lsis-lsissys2) | [LSIS-lsisRFAll](./kba/runs.md#lsis-lsisrfall) | [LSIS-lsisRFYes](./kba/runs.md#lsis-lsisrfyes) | [LSIS-lsisSRFYes](./kba/runs.md#lsis-lsissrfyes) | [LSIS-lsisSRFAll](./kba/runs.md#lsis-lsissrfall)

??? abstract "Abstract"
	
	This paper describes our joint participation in the TREC 2012 KBA task. The system is broken down as follows : first name variations of the entity topics are searched then documents containing at least one of them are retrieved. Finally documents go through two classifiers to categorize them as garbage, neutrals, relevant or centrals. This system got good results (3rd of 11) however first analyses tends to show that ranking is just a little bit better than random.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BonnefoyBB12.bib) "
	```
	@inproceedings{DBLP:conf/trec/BonnefoyBB12,
		author = {Ludovic Bonnefoy and Vincent Bouvier and Patrice Bellot},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{LSIS/LIA} at {TREC} 2012 Knowledge Base Acceleration},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/LSIS.LIA.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BonnefoyBB12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Bi-directional Linkability From Wikipedia to Documents and Back Again:  UMass at TREC 2012 Knowledge Base Acceleration Track

_Jeffrey Dalton, Laura Dietz_

- :fontawesome-solid-user-group: **Participant:** [UMass_CIRR](./kba/participants.md#umass_cirr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/umass_CIRR.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/umass_CIRR.kba.final.pdf)

??? abstract "Abstract"
	
	This notebook details the participation of the University of Massachusetts Amherst in the Cumulative Citation Recommendation task (CCR) of the TREC 2012 Knowledge Base Acceleration Track. UMass' objective is to introduce a single model for Knowledge Base Entity Linking and Knowledge Base Acceleration stream filtering using bi-directional linkability between knowledge base (KB) entries and mentions of the entities in documents. Our system focuses on estimating linkability between documents and Knowledge Base entities which measures compatibility in two directions: (1) from a KB entity to documents and (2) from mentions of entities in documents to their KB entries. The entity to document direction, is modeled as a retrieval task where the goal is to identify the most relevant documents for an entity in the evaluation time range. However, if the entity is ambiguous, the retrieved documents may contain documents that are relevant to other entities with the same or similar name. To address this, we want to leverage information from the document to disambiguate the entity. We observe that this problem, from mention to KB entity, is very similar to the TAC Knowledge Base Population Entity Linking Task (Ji et al., 2011). The major goal of our participation is to explore how these two directions, from KB to documents and back can be combined. For KBA, the goal is to identify documents from a stream that are central for a given entity in Wikipedia. Some participants viewed this as a classification problem and trained supervised classifiers for each entity. Instead, our approach to the problem is based upon document ranking. We combine probabilistic information retrieval and then combine the results with TAC entity linking for re-ranking and filtering. Our ranking approach has three stages: First, documents are retrieved from the stream corpus using an entity query model. Second, potential mentions of the target entity are identified in the retrieved documents. Third, links between the document mentions and the target entity are established or dismissed, giving rise to a filtered (or reranked) list of results that mention the target entity. Our initial system leverages the bi-directional relevance as a simple form of re-ranking of retrieved documents, but we envision tighter integration in the future. The baseline retrieval run generates a query from the Wikipedia KB entry, including the name, name variants, and linked entities. We also incorporate contextual evidence from the document stream by using the documents in the training time period as relevance feedback documents. We use Latent Concept Expansion (Metzler and Croft, 2007) to estimate important contextual words and NER concepts. Our experiments show that incorporating entity context from query expansion methods provides significant gains both in precision and recall over the baseline, with all of our experimental runs outperforming the median. Our best performing run incorporates linkability evidence from the TAC Entity Linking model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DaltonD12.bib) "
	```
	@inproceedings{DBLP:conf/trec/DaltonD12,
		author = {Jeffrey Dalton and Laura Dietz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Bi-directional Linkability From Wikipedia to Documents and Back Again: UMass at {TREC} 2012 Knowledge Base Acceleration Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/umass\_CIRR.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DaltonD12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Illinois' Graduate School of Library and Information  Science at TREC 2012

_Miles Efron, Jana Deisner, Peter Organisciak, Garrick Sherman, Ana Lucic_

- :fontawesome-solid-user-group: **Participant:** [uiucGSLIS](./kba/participants.md#uiucgslis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/uiucGSLIS.microblog.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/uiucGSLIS.microblog.kba.final.pdf)
- :material-file-search: **Runs:** [uiucGSLIS-gslis_adaptive](./kba/runs.md#uiucgslis-gslis_adaptive) | [uiucGSLIS-gslis_mult](./kba/runs.md#uiucgslis-gslis_mult)

??? abstract "Abstract"
	
	The University of Illinois' Graduate School of Library and Information Science (uiucGSLIS) participated in TREC's microblog and knowledge base acceleration (KBA) tracks in 2012. Our high-level goals were two-fold: Microblog: Test a novel method for document ranking during real-time search. KBA: Compare methods of topic representation-particularly longitudinal adaptation of topic representation-for the KBA task. Our document ranking in the microblog track is based on a behavioral metaphor. Given a query Q, we decompose Q into a set of imaginary saved searches S. Given an incoming document stream D = D1, D2, . . . , DN , we ask: what is the probability that a document D is read, given the user's query and a rational allocation of attention over his saved searches? [...]
	

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

#### Team Association Analysis for Named Entity Filtering

_Oskar Gross, Hannu Toivonen, Antoine Doucet_

- :fontawesome-solid-user-group: **Participant:** [helsinki](./kba/participants.md#helsinki)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/helsinki.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/helsinki.kba.final.pdf)
- :material-file-search: **Runs:** [helsinki-disgraph](./kba/runs.md#helsinki-disgraph) | [helsinki-disgraph2](./kba/runs.md#helsinki-disgraph2)

??? abstract "Abstract"
	
	This paper describes the participation of the Universities of Helsinki and Caen in the first round of the TREC Knowledge Base Acceleration track3. The task focused on filtering a stream of documents relevant to a set of entities. Our approach uses word co-occurrence graphs for modelling the named entities. We submitted two runs that achieved an average F-measure superior to the mean of all submitted runs. The best of those runs ranked in the top 5 runs for both the central and relevant F-measures, out of a total of 43 runs submitted by 11 institutions. As our runs were the produce of a first implementation of our approach, these preliminary results are very supportive of our idea to use concept graphs for modelling named entity relations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossTD12.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossTD12,
		author = {Oskar Gross and Hannu Toivonen and Antoine Doucet},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Team Association Analysis for Named Entity Filtering},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/helsinki.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossTD12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The HLTCOE Approach to the TREC 2012 KBA Track

_Brian Kjersten, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [hltcoe](./kba/participants.md#hltcoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/hltcoe.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/hltcoe.kba.final.pdf)
- :material-file-search: **Runs:** [hltcoe-wordNER500](./kba/runs.md#hltcoe-wordner500) | [hltcoe-wordNER](./kba/runs.md#hltcoe-wordner)

??? abstract "Abstract"
	
	Our team submitted runs for the TREC KBA Cumulative Citation Recommendation task. This task involves labeling over 300 million documents for whether they are relevant and/or central to particular entities already in a database. For this task, we used an SVM classifier that uses unigrams and named entities as binary features. In this paper, we describe our work for the 2012 evaluation and the results we obtained.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KjerstenM12.bib) "
	```
	@inproceedings{DBLP:conf/trec/KjerstenM12,
		author = {Brian Kjersten and Paul McNamee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {HLTCOE} Approach to the {TREC} 2012 {KBA} Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/hltcoe.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KjerstenM12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2012 KBA Track

_Yan Li, Zhaozhao Wang, Baojin Yu, Yong Zhang, Ruiyang Luo, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./kba/participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/PRIS.kba.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/PRIS.kba.nb.pdf)
- :material-file-search: **Runs:** [PRIS-PRIS_Run_1](./kba/runs.md#pris-pris_run_1) | [PRIS-PRIS_Run_900](./kba/runs.md#pris-pris_run_900) | [PRIS-PRIS_Run_800](./kba/runs.md#pris-pris_run_800) | [PRIS-PRIS_Run_700](./kba/runs.md#pris-pris_run_700) | [PRIS-PRIS_Run_600](./kba/runs.md#pris-pris_run_600) | [PRIS-PRIS_Run_500](./kba/runs.md#pris-pris_run_500) | [PRIS-PRIS_Run_400](./kba/runs.md#pris-pris_run_400)

??? abstract "Abstract"
	
	Our system to KBA Track at TREC2012 is described in this paper, which includes preprocessing, index building, relevance feedback and similarity calculation. In particular, the Jaccard coefficient was applied to calculate the similarities between documents. We also show the evaluation results for our team and the comparison with the best and median evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiWYZLXCG12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiWYZLXCG12,
		author = {Yan Li and Zhaozhao Wang and Baojin Yu and Yong Zhang and Ruiyang Luo and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2012 {KBA} Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/PRIS.kba.nb.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiWYZLXCG12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Entity Profile Based Approach in Automatic Knowledge Finding

_Xitong Liu, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./kba/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/udel_fang.kba.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/udel_fang.kba.nb.pdf)
- :material-file-search: **Runs:** [udel_fang-UDInfoKBA_EX](./kba/runs.md#udel_fang-udinfokba_ex) | [udel_fang-UDInfoKBA_WIKI1](./kba/runs.md#udel_fang-udinfokba_wiki1) | [udel_fang-UDInfoKBA_WIKI2](./kba/runs.md#udel_fang-udinfokba_wiki2) | [udel_fang-UDInfoKBA_WIKI3](./kba/runs.md#udel_fang-udinfokba_wiki3)

??? abstract "Abstract"
	
	We focus on the problem of profile building in this year's KBA track and proposed two methods. The first method is a baseline, which selects the stream items that has exact string match with the query entity. All the matched documents are assigned with the same relevance score. In the second method, we propose to use the related entities to help us identify the information related to the query entity. In particular, we retrieve the wikipedia pages for the query entities and extract the anchor text in all the internal links within the wikipedia page. These anchor text are treated as the related entities of the query entity and they are used to build the profile of the query entity. Given a stream item (i.e., a document), the relevance score is estimated by integrating the match with the query entity and the match with the related entities. Results on the training data show that the second method is more effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuF12,
		author = {Xitong Liu and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Entity Profile Based Approach in Automatic Knowledge Finding},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/udel\_fang.kba.nb.pdf},
		timestamp = {Sun, 26 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SAWUS Siena's Automatic Wikipedia Update System

_Carl Tompkins, Zachary Witter, Sharon G. Small_

- :fontawesome-solid-user-group: **Participant:** [SCIATeam](./kba/participants.md#sciateam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/SCIATeam.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/SCIATeam.kba.final.pdf)

??? abstract "Abstract"
	
	The National Institute of Standards and Technology (NIST) has been running an annual Text Retrieval Competition and Conference (TREC) since 1992. This is a premier conference that offers researchers in the field of Computational Linguistics the opportunity to showcase their work and compare their results against other leading researchers. Our Siena research team participated in the TREC Knowledge Based Acquisition (KBA) Track, which was offered for the first time in 2012. The objective of this track is to drive research into automatic acquisition of knowledge, such as automatically updating Wikipedia by utilizing online news. Specifically our team of researchers developed a system that filters a stream of content for information that should be included on a given Wikipedia page. It was not yet clear how traditional Information Retrieval (IR) techniques perform for this task; therefore we began with a baseline test using current state of the art IR techniques. We then went on to experiment with query expansion, building a module that utilized Wikipedia Infoboxes to add terms to our query. This module was incorporated with our IR component to create SAWUS. Four submissions were sent to NIST to undergo a formal evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TompkinsWS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/TompkinsWS12,
		author = {Carl Tompkins and Zachary Witter and Sharon G. Small},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{SAWUS} Siena's Automatic Wikipedia Update System},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/SCIATeam.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TompkinsWS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI at TREC 2012, KBA Track and Session Track

_Samur Araújo, Gebrekirstos G. Gebremeskel, Jiyin He, Corrado Boscarino, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [CWI](./kba/participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/CWI.kba.session.final.pdf](http://trec.nist.gov/pubs/trec21/papers/CWI.kba.session.final.pdf)
- :material-file-search: **Runs:** [CWI-LEARNING16000](./kba/runs.md#cwi-learning16000) | [CWI-DISAMBIGUATOR](./kba/runs.md#cwi-disambiguator) | [CWI-LANGUAGEMODEL](./kba/runs.md#cwi-languagemodel) | [CWI-google_dic_1](./kba/runs.md#cwi-google_dic_1) | [CWI-google_dic_2](./kba/runs.md#cwi-google_dic_2) | [CWI-google_dic_3](./kba/runs.md#cwi-google_dic_3) | [CWI-google_strip_1](./kba/runs.md#cwi-google_strip_1) | [CWI-google_strip_2](./kba/runs.md#cwi-google_strip_2)

??? abstract "Abstract"
	
	We participated in two tracks: Knowledge Base Acceleration (KBA) Track and Session Track. In the KBA track, we focused on experimenting with different approaches as it is the first time the track is launched. We experimented with supervised and unsupervised retrieval models. Our supervised approach models include language models and a string-learning system. Our unsupervised approaches include using: 1)DBpedia labels and 2) Google-Cross-Lingual Dictionary (GCLD). While the approach that uses GCLD targets the central and relvant bins, all the rest target the central bin. The GCLD and the string-learning system have outperformed the others in their respective targeted bins. The goal of the Session track submission is to evaluate whether and how a logic framework for representing user interactions with an IR system can be used for improving the approximation of the relevant term distribution that another system that is supposed to have access to the session information will then calculate.
	

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

