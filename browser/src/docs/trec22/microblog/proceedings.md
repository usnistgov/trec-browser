# Proceedings - Microblog 2013 

#### Overview of the TREC-2013 Microblog Track

_Jimmy Lin, Miles Efron_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/MB.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/MB.OVERVIEW.pdf)
??? abstract "Abstract"
	
	This year represents the third iteration of the TREC Microblog track, which began in 2011. There was no substantive change in the task definition, which remains nominally real-time search, best summarized as “At time T , give me the most relevant tweets about topic X.” However, we introduced a radically different evaluation methodology, dubbed “evaluation as a service”, which attempted to address deficiencies in how the document collection was distributed in previous years. This is the first time such an approach has been deployed at TREC. Overall, we believe that the evaluation methodology was successful, drawing participation from twenty groups around the world.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinE13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinE13,
		author = {Jimmy Lin and Miles Efron},
		editor = {Ellen M. Voorhees},
		title = {Overview of the {TREC-2013} Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/MB.OVERVIEW.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinE13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion for Microblog Retrieval: 2013

_Ayan Bandyopadhyay_

- :fontawesome-solid-user-group: **Participant:** [ISIKol](./participants.md#isikol)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/isikol-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/isikol-microblog.pdf)
- :material-file-search: **Runs:** [GSAT](./runs.md#gsat) | [GSAS](./runs.md#gsas) | [GSAA](./runs.md#gsaa)

??? abstract "Abstract"
	
	Microblogging sites like http://twitter.com have emerged as a popular platform for expressing opinions. Given the increasing amount of information available through such microblogging sites, it would be nice to be able to retrieve useful tweets in response to a given information need. Finding relevant tweets that match a user query is challenging for the following reasons. Tweets are short. They contain a maximum of 140 characters. Tweets are not always written maintaining formal grammar and proper spelling. Spelling variations increase the likelihood of vocabulary mismatch. In this preliminary study, we explore standard query expansion approaches as a way to address this problem.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bandyopadhyay13.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bandyopadhyay13,
		author = {Ayan Bandyopadhyay},
		editor = {Ellen M. Voorhees},
		title = {Query Expansion for Microblog Retrieval: 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/isikol-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bandyopadhyay13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QCRI at TREC 2013 Microblog Track

_Tarek El-Ganainy, Walid Magdy, Wei Gao, Zhongyu Wei_

- :fontawesome-solid-user-group: **Participant:** [QCRI](./participants.md#qcri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/QCRI-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/QCRI-microblog.pdf)
- :material-file-search: **Runs:** [QCRI2](./runs.md#qcri2) | [QCRI1](./runs.md#qcri1) | [QCRI3](./runs.md#qcri3) | [QCRI4](./runs.md#qcri4)

??? abstract "Abstract"
	
	We report our work in the real-time ad hoc search task of TREC-2013 Microblog track. Our system focuses on improving retrieval effectiveness of Microblog search through query expansion and reranking of search results. We apply web-based query expansion algorithm for enriching the microblog queries with additional terms from concurrent webpages related to the search topic. Later we apply results reranking through utilizing state-of-the-art learning to rank algorithms to train 12 different ranking models using relevance judgment of Tweets2011-12 queries, for which we conduct feature engineering, validation dataset selection, and the ensemble of these models. Our approach differs from salient approaches in the previous Microblog tracks that are based on document expansion utilizing embedded URLs and that leverage some single ranking model for tweets re-ranking. Our pipeline constructed using the hybrid of these two components showed promising retrieval results on Tweets2013 benchmark dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/El-GanainyMGW13.bib) "
	```
	@inproceedings{DBLP:conf/trec/El-GanainyMGW13,
		author = {Tarek El{-}Ganainy and Walid Magdy and Wei Gao and Zhongyu Wei},
		editor = {Ellen M. Voorhees},
		title = {{QCRI} at {TREC} 2013 Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/QCRI-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/El-GanainyMGW13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Microblog Track in TREC 2013

_Jinhua Gao, Guoxin Cui, Shenghua Liu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/ICTNET-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/ICTNET-microblog.pdf)
- :material-file-search: **Runs:** [ICTNETBASE](./runs.md#ictnetbase) | [ICTNETBO1EXP](./runs.md#ictnetbo1exp) | [ICTNETCOCCUR](./runs.md#ictnetcoccur)

??? abstract "Abstract"
	
	Microblogging services, in which users can publish and share personal status, are now very popular, and attracting more and more industrial and scientific interests. Twitter is one of the most famous microblogging services. On twitter, Users can post personal updates, which are called tweets and limited to 140 characters long. In tweets, users can share interesting messages to their friends by retweeting(RT), push some tweets to specific users using @ mention, and indicate the topics of their tweets using # hashtags. The short-text characteristic and social attributes such as RT, @ mention and # hashtags, make traditional problems, like search, rank, and recommendation etc, quite different in microblogging settings. Microblog track was first introduced in 2011, and ICTNET group have participated in this track three times[2, 7]. In this year's track, only the realtime ad-hoc search task, which was also proposed in 2011 and 2012, was open for submission. This task requires to retrieve all the tweets that are relevant to query Q and before time T. Unlike the past two years, in which participants had to collect the corpus themselves, microblog track was first provided as a service this year, and participants could access the corpus through official APIs, which made it possible for the organizers to increase the size of corpus from 16M tweets to 260M tweets, which were collected via the Twitter streaming API over a two-month period. This report is organized as follows. Section 2 mainly focuses on the data preparation step, which contains the data collecting step and preprocessing step. The methodology and framework are illustrated in section 3, and some experiments and results are presented in section 4
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaoCLLC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaoCLLC13,
		author = {Jinhua Gao and Guoxin Cui and Shenghua Liu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees},
		title = {{ICTNET} at Microblog Track in {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/ICTNET-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaoCLLC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QU at TREC-2013: Expansion Experiments for Microblog Ad hoc Search

_Maram Hasanain, Latifa Al-Marri, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./participants.md#qu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/qu-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/qu-microblog.pdf)
- :material-file-search: **Runs:** [QUQueryExp](./runs.md#ququeryexp) | [QUBaseline](./runs.md#qubaseline) | [QUTemporal](./runs.md#qutemporal) | [QUDocExp](./runs.md#qudocexp)

??? abstract "Abstract"
	
	In the first appearance of Qatar University (QU) at Text REtrieval Conference (TREC), our submitted microblog runs explored different ways of expanding the context of both queries and tweets to overcome the sparsity and lack of context problems. Since the task is real-time, we have also considered the temporal aspect, once combined with tweet expansion technique, and another separately as a scoring factor. Our explored ideas were all unsupervised and only used internal resources (i.e., the provided API service with only access to the tweets). For query expansion, we have used pseudo relevance feedback to include terms from the top-ranked retrieved tweets. Based on experiments on previous TREC collections, an aggressive expansion with 30 terms or more provided the best improvement. For tweet expansion, a 2-step relevance modeling approach was leveraged to temporally and lexically expand a tweet. To further explore the effect of considering the time dimension in scoring tweets, we also developed a temporal re-scoring function used to favor tweets that are closer in time to the query over tweets that might be more lexically relevant but are posted further apart in time from the query. We also conducted post-TREC experiments in which we worked on enhancing the query expansion and temporal re-scoring approaches. Resuls released by TREC have shown that the temporal re-scoring run was the most effective run among all of our submitted ones. As for the post-TREC experiments, our results have shown that the enhanced query expansion and temporal re-scoring approaches had notable improvements on retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HasanainAE13.bib) "
	```
	@inproceedings{DBLP:conf/trec/HasanainAE13,
		author = {Maram Hasanain and Latifa Al{-}Marri and Tamer Elsayed},
		editor = {Ellen M. Voorhees},
		title = {{QU} at {TREC-2013:} Expansion Experiments for Microblog Ad hoc Search},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/qu-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HasanainAE13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Microblog Track 2013

_Lamjed Ben Jabeur, Firas Damak, Lynda Tamine, Guillaume Cabanac, Karen Pinel-Sauvagnat, Mohand Boughanem_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/IRIT-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/IRIT-microblog.pdf)
- :material-file-search: **Runs:** [iritfdUrlRoc](./runs.md#iritfdurlroc) | [iritfdUrl](./runs.md#iritfdurl) | [BNTSrK](./runs.md#bntsrk) | [BNTSrKSO](./runs.md#bntsrkso)

??? abstract "Abstract"
	
	This paper describes the participation of the IRIT lab, University of Toulouse, France, to the Microblog Track of TREC 2013. Two different approaches are experimented by our team for the real-time ad-hoc search task: (i) a Bayesian network retrieval model for tweet search and (ii) a document and query expansion model for microblog search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JabeurDTCPB13.bib) "
	```
	@inproceedings{DBLP:conf/trec/JabeurDTCPB13,
		author = {Lamjed Ben Jabeur and Firas Damak and Lynda Tamine and Guillaume Cabanac and Karen Pinel{-}Sauvagnat and Mohand Boughanem},
		editor = {Ellen M. Voorhees},
		title = {{IRIT} at {TREC} Microblog Track 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/IRIT-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JabeurDTCPB13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCAS at TREC-2013 Microblog Track

_Dongxing Li, Ben He, Xin Zhang, Tiejian Luo_

- :fontawesome-solid-user-group: **Participant:** [UCAS](./participants.md#ucas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/UCAS-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/UCAS-microblog.pdf)
- :material-file-search: **Runs:** [UCASgem](./runs.md#ucasgem) | [UCASqe](./runs.md#ucasqe)

??? abstract "Abstract"
	
	The participation of University of Chinese Academy of Sciences (UCAS) in the real-time adhoc task in Microblog track aims to evaluate the effectiveness of the query-biased learning to rank model, which was proposed in our previous work. To further improve the retrieval effectiveness of learning to rank, we construct the query-biased learning to rank framework by taking the difference between queries into consideration. In particular, a query-biased ranking model is learned by a cluster classification learning algorithm in order to better capture the characteristics of the given queries. This query-biased ranking mode is combined with the general ranking model (BM25 etc.) to produce the final ranked list of tweets in response to the given target query. We were also planning to incorporate a machine learning approach for selecting high-quality training data for improving the effectiveness of learning to rank. However, due to interruption caused by lab move, we only managed to experiment with the query-biased approach using partial features.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiHZL13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiHZL13,
		author = {Dongxing Li and Ben He and Xin Zhang and Tiejian Luo},
		editor = {Ellen M. Voorhees},
		title = {{UCAS} at {TREC-2013} Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/UCAS-microblog.pdf},
		timestamp = {Fri, 27 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiHZL13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A User-in-the-Loop Process for Investigational Search: Foreseer in  TREC 2013 Microblog Track

_Cheng Li, Yue Wang, Qiaozhu Mei_

- :fontawesome-solid-user-group: **Participant:** [Foreseer](./participants.md#foreseer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/foreseer-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/foreseer-microblog.pdf)
- :material-file-search: **Runs:** [FSsvm](./runs.md#fssvm) | [Direrank](./runs.md#direrank) | [Avgrank](./runs.md#avgrank) | [RvsDir](./runs.md#rvsdir)

??? abstract "Abstract"
	
	Traditionally, ad hoc retrieval aims at satisfying an information need with a few highly relevant documents. This high-precision approach works well for simple and clear queries. When the information need becomes complex, a few top-ranked documents may not provide satisfactory answer. As a result, the user adapts to reformulate the query to explore more relevant information; the search engine evolves to diversify results to cover the user's real information need. In cases where the user puts emphasis on high recall of the results, the search process becomes increasingly laborious. We propose a retrieval system that interacts with the user to obtain high precision and high recall search results, while minimizing the user effort. It iteratively explores the collection by a series of queries to optimize the recall, and refines an active learning classifier to maintain the precision. We built a prototype of the system for TREC 2013 Microblog Track. Depending on the actual query, the system converges to a stable decision on relevant/non-relevant tweets after asking for a few hundred labels, which was used to retrieve and rank 10,000 tweets (maximum allowance of the TREC API).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiWM13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiWM13,
		author = {Cheng Li and Yue Wang and Qiaozhu Mei},
		editor = {Ellen M. Voorhees},
		title = {A User-in-the-Loop Process for Investigational Search: Foreseer in {TREC} 2013 Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/foreseer-microblog.pdf},
		timestamp = {Thu, 03 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiWM13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NovaSearch at TREC 2013 Microblog Track: Experiments with reranking  using Wikipedia

_Flávio Martins, André Mourão, João Magalhães_

- :fontawesome-solid-user-group: **Participant:** [NOVASEARCH](./participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/novasearch-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/novasearch-microblog.pdf)
- :material-file-search: **Runs:** [NOVAsearch01](./runs.md#novasearch01) | [NOVAsearch02](./runs.md#novasearch02) | [NOVAsearch03](./runs.md#novasearch03) | [NOVAsearch00](./runs.md#novasearch00)

??? abstract "Abstract"
	
	Users engaged in microblogging services and social-media apps contribute to multiple real-time text streams which amass large volumes of messages often sparked by events reported in newswire and in other media. We explore the use of external sources to detect topic popularity surges and improve microblog search performance using time- based language models [3]. The major novelty concerns the analysis that explores Wikipedia page view streams to find topic interest spikes. We obtained promising initial results when using evidence from Wikipedia for temporal reranking with the Tweets2013 dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MartinsMM13.bib) "
	```
	@inproceedings{DBLP:conf/trec/MartinsMM13,
		author = {Fl{\'{a}}vio Martins and Andr{\'{e}} Mour{\~{a}}o and Jo{\~{a}}o Magalh{\~{a}}es},
		editor = {Ellen M. Voorhees},
		title = {NovaSearch at {TREC} 2013 Microblog Track: Experiments with reranking using Wikipedia},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/novasearch-microblog.pdf},
		timestamp = {Thu, 14 May 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MartinsMM13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2013 Microblog Track Experiments at Kobe University

_Taiki Miyanishi, Sayaka Kitaguchi, Kazuhiro Seki, Kuniaki Uehara_

- :fontawesome-solid-user-group: **Participant:** [KobeU](./participants.md#kobeu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/kobe-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/kobe-microblog.pdf)
- :material-file-search: **Runs:** [kobeU](./runs.md#kobeu) | [kobeRMU](./runs.md#kobermu) | [kobeTSFRM](./runs.md#kobetsfrm) | [kobeTSFRMU](./runs.md#kobetsfrmu)

??? abstract "Abstract"
	
	This paper describes our approach to real-time ad hoc task processing in the TREC 2013 microblog track. The approach uses a concept-based query expansion method based on a temporal relevance model that uses the temporal variation of concepts (e.g. terms or phrases) on microblogs. Our model extends an effective existing word and concept-based relevance models by tracking the concept frequency over time in microblogging services. The experimentally obtained results demonstrate that our concept-based query expansion method improve search performance, especially when using tweet selection feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MiyanishiKSU13.bib) "
	```
	@inproceedings{DBLP:conf/trec/MiyanishiKSU13,
		author = {Taiki Miyanishi and Sayaka Kitaguchi and Kazuhiro Seki and Kuniaki Uehara},
		editor = {Ellen M. Voorhees},
		title = {{TREC} 2013 Microblog Track Experiments at Kobe University},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/kobe-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MiyanishiKSU13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow (UoG_TwTeam) at TREC Microblog 2013

_Jesus A. Rodriguez Perez, Andrew James McMinn, Joemon M. Jose_

- :fontawesome-solid-user-group: **Participant:** [UoG_TwTeam](./participants.md#uog_twteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/TwTeam-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/TwTeam-microblog.pdf)
- :material-file-search: **Runs:** [ModelSEL922](./runs.md#modelsel922) | [QEDiscIDF25Good](./runs.md#qediscidf25good) | [DFRBase](./runs.md#dfrbase) | [QEClustIDF](./runs.md#qeclustidf)

??? abstract "Abstract"
	
	TREC 2013, we participated in the ad-hoc search task of the Microblog Track. The Microblog track, which is in its third consecutive year, has remained very similar to the last two. This paper describes the approaches we have implemented for Tweet retrieval, which comprehend query expansion, and baseline model selection. The results for all the runs submitted are well above the median achieved for all the automatic runs submitted to TREC. Furthermore, statistically significant improvements in terms of precision at 30, are reported for our automatic query expansion approach with respect to the baseline we chose. The methods here proposed show great potential for enhancing tweet retrieval performance and should therefore be further studied.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PerezMJ13.bib) "
	```
	@inproceedings{DBLP:conf/trec/PerezMJ13,
		author = {Jesus A. Rodriguez Perez and Andrew James McMinn and Joemon M. Jose},
		editor = {Ellen M. Voorhees},
		title = {University of Glasgow (UoG{\_}TwTeam) at {TREC} Microblog 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/TwTeam-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PerezMJ13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKUICST at TREC 2013 Microblog Track

_Runwei Qiang, Yue Fei, Yihong Hong, Jianwu Yang_

- :fontawesome-solid-user-group: **Participant:** [PKUICST](./participants.md#pkuicst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/PKUICST-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/PKUICST-microblog.pdf)
- :material-file-search: **Runs:** [PKUICST1](./runs.md#pkuicst1) | [PKUICST2](./runs.md#pkuicst2) | [PKUICST3](./runs.md#pkuicst3) | [PKUICST4](./runs.md#pkuicst4)

??? abstract "Abstract"
	
	This paper describes PKUICST's entry into the TREC 2013 Microblog track. In this year of microblog track, we designed and conducted a series of experiments based on both our local crawled collection and the official track API. For runs with local crawled dataset, we exploited different retrieval models, such as TFIDF, Okapi BM25 and statistic language model and tuned optimal parameters for all these models with the dataset in TREC 2012. Furthermore, we attempted to combine these models to gain a better performance with the help of learning to rank framework. For runs with the official track API, we employed language model with two-stage pseudo feedback query expansion. In addition, a filtering component was adopted to refine the results retrieved by the expanded query. Experimental results demonstrate that our approach obtains convincing performances.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiangFHY13.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiangFHY13,
		author = {Runwei Qiang and Yue Fei and Yihong Hong and Jianwu Yang},
		editor = {Ellen M. Voorhees},
		title = {{PKUICST} at {TREC} 2013 Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/PKUICST-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiangFHY13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CIRGIRDISCO at TREC 2013 Microblog Track

_Muhammad Atif Qureshi, Colm O'Riordan, Gabriella Pasi_

- :fontawesome-solid-user-group: **Participant:** [CIRG_IRDISCO](./participants.md#cirg_irdisco)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/NUIG-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/NUIG-microblog.pdf)
- :material-file-search: **Runs:** [CIRGIRDISCO2](./runs.md#cirgirdisco2) | [CIRGIRDISCO3](./runs.md#cirgirdisco3) | [CIRGIRDISCO4](./runs.md#cirgirdisco4)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2013 Microblog real-time search task. We utilized a query expansion approach and submitted three runs: one without using any form of external evidence and the remaining two runs utilize extended abstracts of Wikipedia articles.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QureshiOP13.bib) "
	```
	@inproceedings{DBLP:conf/trec/QureshiOP13,
		author = {Muhammad Atif Qureshi and Colm O'Riordan and Gabriella Pasi},
		editor = {Ellen M. Voorhees},
		title = {{CIRGIRDISCO} at {TREC} 2013 Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/NUIG-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QureshiOP13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Tie-breaker: A New Perspective of Ranking and Evaluation for Microblog  Retrieval

_Yue Wang, Jerry Darko, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/udel_fang-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/udel_fang-microblog.pdf)
- :material-file-search: **Runs:** [UDInfoMB](./runs.md#udinfomb) | [UDInfoMTB1](./runs.md#udinfomtb1) | [UDInfoMTB2](./runs.md#udinfomtb2) | [UDInfoMINT](./runs.md#udinfomint)

??? abstract "Abstract"
	
	Microblog retrieval is the key tool that enables users to access the relevant information from the enormous tweets posted on social media. Due to the differences of the tweets and traditional documents, existing IR models might not be the optimal choice for this problem. In this paper, we aim to introduce a new idea, i.e., tie-breaking, and discuss its implication in ranking methods and evaluation measures for microblog retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangDF13.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangDF13,
		author = {Yue Wang and Jerry Darko and Hui Fang},
		editor = {Ellen M. Voorhees},
		title = {Tie-breaker: {A} New Perspective of Ranking and Evaluation for Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/udel\_fang-microblog.pdf},
		timestamp = {Thu, 17 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WangDF13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2013 Microblog Track

_Zhen Yang, Guangyuan Zhang, Shuyong Si, Yingxu Lai, Kefeng Fan_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/BJUT-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/BJUT-microblog.pdf)
- :material-file-search: **Runs:** [BJUTFreq](./runs.md#bjutfreq) | [BJUTEntr](./runs.md#bjutentr) | [BJUTCnor](./runs.md#bjutcnor)

??? abstract "Abstract"
	
	This paper describes the first participation of BJUT in the TREC Micro-blog Track 2013. We perform the experiments on the 2013 TREC Microblog data using the standard retrieval model with several different query expansion methods including frequency method, C measure and Entropy differences. Also we introduce the details of our system, which consists of data preprocessing, retrieval structure, and query expansion & results analysis module.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangZSLF13.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangZSLF13,
		author = {Zhen Yang and Guangyuan Zhang and Shuyong Si and Yingxu Lai and Kefeng Fan},
		editor = {Ellen M. Voorhees},
		title = {{BJUT} at {TREC} 2013 Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/BJUT-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangZSLF13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2013 Microblog Track

_Siming Zhu, Zhe Gao, Yajing Yuan, Hui Wang, Guang Chen_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/PRIS-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/PRIS-microblog.pdf)
- :material-file-search: **Runs:** [PrisRun1](./runs.md#prisrun1) | [PrisRun2](./runs.md#prisrun2) | [PrisRun4](./runs.md#prisrun4) | [PrisRun3](./runs.md#prisrun3)

??? abstract "Abstract"
	
	This paper described the real-time search system we built for TREC 2013 microblog track. We focused on query expansion and ranking algorithm and employed different strategies. For query expansion, we implied pseudo-relevance feedback using WAF algorithms and a refined tf*idf formula. For re-ranking part, our system makes use of various tweets' features, such as expansion terms, URL information, and incorporate them in a learning-to-rank framework to improve the final ranking results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuGYWC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuGYWC13,
		author = {Siming Zhu and Zhe Gao and Yajing Yuan and Hui Wang and Guang Chen},
		editor = {Ellen M. Voorhees},
		title = {{PRIS} at {TREC} 2013 Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/PRIS-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuGYWC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

