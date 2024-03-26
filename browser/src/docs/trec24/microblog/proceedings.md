# Proceedings - Microblog 2015 

#### Overview of the TREC-2015 Microblog Track

_Jimmy Lin, Miles Efron, Garrick Sherman, Yulu Wang, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec24/papers/Overview-MB.pdf](https://trec.nist.gov/pubs/trec24/papers/Overview-MB.pdf)
??? abstract "Abstract"
	
	The TREC 2015 Microblog track introduced a single real-time filtering task broken down into two scenarios. Our goal is to explore techniques for monitoring streams of social media posts with respect to users' interest profiles. An interest profile describes a topic about which the user wishes to receive information updates in real time, and is different from a typical ad hoc topic in that the profile represents a prospective (as opposed to a retrospective) information need. Thus, the nature of the desired information is qualitatively different. In real-time filtering, the goal is for a system to “push” (i.e., recommend, suggest) interesting and novel content to users in a timely fashion. We operationalized this task in terms of two scenarios: Scenario A (push notification): Content that is iden- tified as interesting and novel by a system based on the user's interest profile might be shown to the user as a notification on his or her mobile phone. The expectation is that such notifications are triggered a relatively short time after the content is generated. Scenario B (email digest): Content that is identified as interesting and novel by a system based on the user's interest profile might be aggregated into an email digest that is periodically sent to a user (e.g., nightly). It is assumed that each item of content is relatively short; one might think of these as “personalized headlines”. In both scenarios, it is assumed that the content items delivered to the users are relatively short. For expository convenience and to adopt standard information retrieval parlance, we write of users desiring relevant content, even though “relevant” in our context might be better operationalized as interesting, novel, and timely.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinESWV15.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinESWV15,
		author = {Jimmy Lin and Miles Efron and Garrick Sherman and Yulu Wang and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC-2015} Microblog Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {https://trec.nist.gov/pubs/trec24/papers/Overview-MB.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinESWV15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke: TREC 2015 Microblog Track

_Mustafa Abualsaud, Milad Ghaznavi, Daniel Recoskie, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-MB.pdf)
- :material-file-search: **Runs:** [UWCMBE1](./runs.md#uwcmbe1) | [UWCMBP1](./runs.md#uwcmbp1) | [UWCMBE2](./runs.md#uwcmbe2) | [UWCMBP2](./runs.md#uwcmbp2)

??? abstract "Abstract"
	
	The goal of the TREC 2015 Microblog Track is to develop a real-time relevancy retrieval system that monitors a stream of social media posts and recommends relevant posts according to users' interests [1]. In this track, the representative social media is Twitter, and relevant posts are tweets with respect to a user's interest. A user's interest is represented by an interest profile containing a title, a description, and a narrative. Relevant tweets are recommended to the user in two tasks, push notification and periodic email digest. A. Push Notification Task:  The push notification task is meant to model a system that notifies the user in real-time on his/her mobile phone as it finds a relevant tweet. This notification, i.e. pushing a relevant tweet, is triggered in less than 100 minutes after the tweet creation time1. At most 10 tweets per day are pushed for each interest profile. B. Periodic Email Digest Task: The periodic email digest task aggregates a ranked-list of up to 100 relevant tweets for each interest profile into an email and sends it to the user at the end of every day.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbualsaudGRC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbualsaudGRC15,
		author = {Mustafa Abualsaud and Milad Ghaznavi and Daniel Recoskie and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {WaterlooClarke: {TREC} 2015 Microblog Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AbualsaudGRC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query-expansion Approaches for Microblog Retrieval

_Sandeep Avula, Jaime Arguello_

- :fontawesome-solid-user-group: **Participant:** [UNCSILS](./participants.md#uncsils)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/UNCSILS-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/UNCSILS-MB.pdf)
- :material-file-search: **Runs:** [UNCSILS_HRM](./runs.md#uncsils_hrm) | [UNCSILS_TRM](./runs.md#uncsils_trm) | [UNCSILS_WRM](./runs.md#uncsils_wrm)

??? abstract "Abstract"
	
	The School of Information and Library Science at the University of North Carolina at Chapel Hill submitted three runs to the “Scenario B” task of the TREC 2015 Microblog Track. The task simulates a scenario where a user specifies a topic of interest in the form of a keyword query and the system produces daily updates with at most 100 tweets about the topic of interest. Systems were responsible for monitoring a stream of tweets and making daily predictions for a set of 250 interest profiles. Each interest profile was in the form of a short keyword query. Systems were asked to produce a ranking of at most 100 tweets per interest profile at the end of each day (shortly after midnight). The evaluation period extended a 10-day period from July 20 to July 29, 2015. All tweets published between 00:00:00 to 23:59:59 UTC were valid candidates for each day of the evaluation period. Our team submitted three runs for “Scenario B”. All runs were automatic runs and used the interest profile title field as the input query. We explored three di↵erent ways of enriching the query representation through query expansion. In two of our runs (UNCSILS WRM and UNCSILS TRM), we scored tweets proportional to the negative KL-divergence between a relevance model generated from an external collection and the tweet language model. These two runs mainly differ by the external collection used to generate a relevance model for interest profile query. In our UNCSILS WRM run, we used an external Wikipedia corpus, and in our UNCSILS TRM run, we used a corpus of tweets collected during a three-week period prior to the evaluation period. In our third run (UNCSILS HRM), we aimed to expand the query with related hashtags.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AvulaA15.bib) "
	```
	@inproceedings{DBLP:conf/trec/AvulaA15,
		author = {Sandeep Avula and Jaime Arguello},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query-expansion Approaches for Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/UNCSILS-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AvulaA15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Burst Detection in Social Media Streams for Tracking Interest Profiles  in Real Time

_Cody Buntain, Jimmy Lin_

- :fontawesome-solid-user-group: **Participant:** [umd_hcil](./participants.md#umd_hcil)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/umd_hcil-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/umd_hcil-MB.pdf)
- :material-file-search: **Runs:** [umd_hcil_run01](./runs.md#umd_hcil_run01) | [umd_hcil_run02](./runs.md#umd_hcil_run02) | [umd_hcil_run03](./runs.md#umd_hcil_run03) | [umd_hcil_run04](./runs.md#umd_hcil_run04)

??? abstract "Abstract"
	
	This work described RTTBurst, an end-to-end system for ingesting a user's interest profiles that describe some topic of interest and identifying new tweets that might be of interest to that user using a simple model for bursts in token usage. We laid out RTTBurst's architecture, our participation in and performance at the TREC 2015 Microblog Track, and a post hoc analysis for increasing RTTBurst's performance. While not as relatively performant in the Microblog Track's real-time notification task, RTTBurst did perform well (ranking 4th overall and second in the automatic category of Scenario B) in providing daily summaries for various interest profiles. Following the official TREC evaluation period, we were also able to increase RTTBurst's performance but not by enough to significantly increase its overall ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuntainL15.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuntainL15,
		author = {Cody Buntain and Jimmy Lin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Burst Detection in Social Media Streams for Tracking Interest Profiles in Real Time},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/umd\_hcil-MB.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BuntainL15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Microblog 2015

_Abdelhamid Chellal, Lamjed Ben Jabeur, Laure Soulier, Bilel Moulahi, Thomas Palmer, Mohand Boughanem, Karen Pinel-Sauvagnat, Lynda Tamine, Gilles Hubert_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/IRIT-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/IRIT-MB.pdf)
- :material-file-search: **Runs:** [IritSigSDA](./runs.md#iritsigsda) | [IritSigSDB](./runs.md#iritsigsdb) | [IRIT-KLTFIDF](./runs.md#irit-kltfidf) | [IRIT100KLTFIDF](./runs.md#irit100kltfidf) | [IRIT-RTDig.33](./runs.md#irit-rtdig.33) | [IRIT-RTNotif.33](./runs.md#irit-rtnotif.33)

??? abstract "Abstract"
	
	This paper presents the participation of the IRIT laboratory (University of Toulouse) to the Microblog Track of TREC 2015. This track consists in a real-time filtering task aiming at monitoring a stream of social media posts in accordance to a user's interest profile. In this context, our team proposes three approaches: (a) a novel selective summarization approach based on a decision of selecting/ignoring tweets without the use of external knowledge and relying on novelty and redundancy factors, (b) a processing workflow enabling to index tweets in real-time and enhanced by a notification and digests method guided by diversity and user personalization, and (c) a step by step stream selection method focusing on rapidity, and taking into account tweet similarity as well as several features including content, entities and user-related aspects. For all these approaches, we discuss the obtained results during the experimental evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChellalJSMPBPTH15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChellalJSMPBPTH15,
		author = {Abdelhamid Chellal and Lamjed Ben Jabeur and Laure Soulier and Bilel Moulahi and Thomas Palmer and Mohand Boughanem and Karen Pinel{-}Sauvagnat and Lynda Tamine and Gilles Hubert},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IRIT} at {TREC} Microblog 2015},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/IRIT-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChellalJSMPBPTH15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ECNU at TREC 2015: Microblog Track

_Qin Chen, Bo Wang, Beijing Huang, Qinmin Hu, Liang He_

- :fontawesome-solid-user-group: **Participant:** [ECNU](./participants.md#ecnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/ECNU-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/ECNU-MB.pdf)
- :material-file-search: **Runs:** [ECNURUNA1](./runs.md#ecnuruna1) | [ECNURUNA3](./runs.md#ecnuruna3) | [ECNURUNA2](./runs.md#ecnuruna2) | [ECNURUNB1](./runs.md#ecnurunb1) | [ECNURUNB2](./runs.md#ecnurunb2) | [ECNURUNB3](./runs.md#ecnurunb3)

??? abstract "Abstract"
	
	This paper describes our participation in TREC 2015 Microblog track, which includes two tasks related to Scenario A and Scenario B. For Scenario A, we build a real-time tweet push system, which is mainly composed by three parts: feature extraction, relevance prediction and redundancy detection. Only the highly relevant and nonredundant tweets are sent to users based on the interest profiles. For Scenario B, we apply three query expansion methods, namely the web search based, the TFIDF-PRF based and the Terrier embedded PRF based. In addition, three state-of-the-art information retrieval models as the language model, BM25 model and DFRee model are utilized. The retrieval results are combined for final delivery. The experimental results in both scenarios demonstrate that our system obtains convincing performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenWHHH15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenWHHH15,
		author = {Qin Chen and Bo Wang and Beijing Huang and Qinmin Hu and Liang He},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ECNU} at {TREC} 2015: Microblog Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/ECNU-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenWHHH15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Real Time Filtering of Tweets Using Wikipedia Concepts and Google  Tri-gram Semantic Relatedness

_Anh Dang, Raheleh Makki, Abidalrahman Moh'd, Aminul Islam, Vlado Keselj, Evangelos E. Milios_

- :fontawesome-solid-user-group: **Participant:** [DalTREC](./participants.md#daltrec)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/DalTREC-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/DalTREC-MB.pdf)
- :material-file-search: **Runs:** [DALTREC_B_PREP](./runs.md#daltrec_b_prep) | [DALTRECAA1](./runs.md#daltrecaa1) | [DALTRECMA1](./runs.md#daltrecma1) | [DALTRECMA2](./runs.md#daltrecma2) | [DALTRECAB1](./runs.md#daltrecab1) | [DALTRECMB1](./runs.md#daltrecmb1)

??? abstract "Abstract"
	
	This paper describes our participation in the mobile notification and email digest tasks in the TREC 2015 Mircoblog track. The tasks are about monitoring Twitter stream and retrieving relevant tweets to users' interest profiles. Interest profiles contain the description of a topic that the user is interested in receiving relevant posts in real-time. Our proposed approach extracts Wikipedia concepts for profiles and tweets and applies a corpus-based word semantic relatedness method to assign tweets to their relevant profiles. This approach is also used to determine whether two tweets are semantically similar which in turn prevents the retrieval of redundant tweets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DangMMIKM15.bib) "
	```
	@inproceedings{DBLP:conf/trec/DangMMIKM15,
		author = {Anh Dang and Raheleh Makki and Abidalrahman Moh'd and Aminul Islam and Vlado Keselj and Evangelos E. Milios},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Real Time Filtering of Tweets Using Wikipedia Concepts and Google Tri-gram Semantic Relatedness},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/DalTREC-MB.pdf},
		timestamp = {Thu, 28 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DangMMIKM15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKUICST at TREC 2015 Microblog Track: Query-biased Adaptive Filtering  in Real-time Microblog Stream

_Feifan Fan, Yue Fei, Chao Lv, Lili Yao, Jianwu Yang, Dongyan Zhao_

- :fontawesome-solid-user-group: **Participant:** [PKUICST](./participants.md#pkuicst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/PKUICST-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/PKUICST-MB.pdf)
- :material-file-search: **Runs:** [PKUICSTRunA1](./runs.md#pkuicstruna1) | [PKUICSTRunA2](./runs.md#pkuicstruna2) | [PKUICSTRunA3](./runs.md#pkuicstruna3) | [PKUICSTRunB1](./runs.md#pkuicstrunb1) | [PKUICSTRunB2](./runs.md#pkuicstrunb2) | [PKUICSTRunB3](./runs.md#pkuicstrunb3)

??? abstract "Abstract"
	
	This paper describes our approaches to real-time filtering task including push notifications on a mobile phone scenario and periodic email digest scenario in the TREC 2015 Microblog track. In the push notifications on a mobile phone scenario, we apply an adaptive timely query-biased filtering framework which utilizes two effective scores to estimate the relevance of tweets. External evidences are well incorporated in our approach with Web-based query expansion technique. In the periodic email digest scenario, we apply pseudo-relevance feedback using language model and similarly we adopt an adaptive dynamic query-biased filtering method to choose the novel representative tweets. Besides, the results of scenario periodic email digest can promote the performance of scenario push notifications since we utilize shared global relevance threshold. Experimental results show that our adaptive query-biased filtering methods achieve good performance with respect to ELG and nCG metrics for push notifications scenario. In addition, our systems for scenario periodic email digest also obtain convincing nDCG scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FanFLYYZ15.bib) "
	```
	@inproceedings{DBLP:conf/trec/FanFLYYZ15,
		author = {Feifan Fan and Yue Fei and Chao Lv and Lili Yao and Jianwu Yang and Dongyan Zhao},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{PKUICST} at {TREC} 2015 Microblog Track: Query-biased Adaptive Filtering in Real-time Microblog Stream},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/PKUICST-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FanFLYYZ15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting Neural Embeddings for Social Media Data Analysis

_Sadid A. Hasan, Yuan Ling, Joey Liu, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna](./participants.md#prna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/prna-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/prna-MB.pdf)
- :material-file-search: **Runs:** [prnaTaskA1](./runs.md#prnataska1) | [prnaTaskA2](./runs.md#prnataska2) | [prnaTaskA3](./runs.md#prnataska3) | [prnaTaskB1](./runs.md#prnataskb1) | [prnaTaskB2](./runs.md#prnataskb2) | [prnaTaskB3](./runs.md#prnataskb3)

??? abstract "Abstract"
	
	In this paper, we describe our microblog real-time filtering system developed and submitted for the Text Retrieval Conference (TREC 2015) microblog track. We submitted six runs for two tasks related to real-time filtering by using various Information Retrieval (IR), and Machine Learning (ML) techniques to analyze the Twitter sample live stream and match relevant tweets corresponding to specific user interest profiles. Evaluation results demonstrate the effectiveness of our approach as we achieved 3 of the top 7 best scores among automatic submissions across all participants and obtained the best (or close to best) scores in more than 25% of the evaluated topics for the real-time mobile push notification task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HasanLLF15a.bib) "
	```
	@inproceedings{DBLP:conf/trec/HasanLLF15a,
		author = {Sadid A. Hasan and Yuan Ling and Joey Liu and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Exploiting Neural Embeddings for Social Media Data Analysis},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/prna-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HasanLLF15a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2015 Microblog Track: Real-Time Filtering Using Knowledge  Base

_Luyang Liu, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/BJUT-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/BJUT-MB.pdf)
- :material-file-search: **Runs:** [BJUTllyQE](./runs.md#bjutllyqe) | [BjutNMF1](./runs.md#bjutnmf1) | [BjutNMF2](./runs.md#bjutnmf2)

??? abstract "Abstract"
	
	This paper describes our efforts for TREC 2015 Microblog track. We applied the classic retrieval model combined with the external knowledge base, i.e., Wikipedia, for query expansion. Besides, we introduced the knowledge acquisition, query expansion, and retrieval model as well. Experimental results show the proposed approach is better than classical method in microblog real-time filtering with the usage of external knowledge base.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuY15.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuY15,
		author = {Luyang Liu and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2015 Microblog Track: Real-Time Filtering Using Knowledge Base},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/BJUT-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuY15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at TREC 2015 Microblog Track

_Luchen Tan, Adam Roegiest, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/UWaterlooMDS-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/UWaterlooMDS-MB.pdf)
- :material-file-search: **Runs:** [UWaterlooATEK](./runs.md#uwaterlooatek) | [UWaterlooATNDEK](./runs.md#uwaterlooatndek) | [UWaterlooATDK](./runs.md#uwaterlooatdk) | [UWaterlooBT](./runs.md#uwaterloobt) | [UWaterlooBTND](./runs.md#uwaterloobtnd)

??? abstract "Abstract"
	
	Given a topic with title, narrative and description, we start by building a language model for the topic. The top 1000 tweets were retrieved from Twitter commercial search engine by applying the title of the topic as a query. We exploit pseudo relevance feedback technologies to estimate probability distributions of each term in the topic, then comparing these probabilities with a background distribution model. We select the highest different terms as our expanded query terms. We then generate a vector for each topic, the features of the vector are non-stop word title terms, selected narrative terms and query expansion terms. Different weights are assigned to the different types of terms. Since we are allowed to deliver at most 10 tweets every day, and the latency time can not exceed 100 minutes, we solve the tweet notification scenario as a multiple-choice secretary problem. Two different solutions were tested.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TanRC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/TanRC15,
		author = {Luchen Tan and Adam Roegiest and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Waterloo at {TREC} 2015 Microblog Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/UWaterlooMDS-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TanRC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NUDTSNA at TREC 2015 Microblog Track: A Live Retrieval System  Framework for Social Network based on Semantic Expansion and Quality  Model

_Xiang Zhu, Jiuming Huang, Sheng Zhu, Ming Chen, Chenlu Zhang, Zhenzhen Li, Huang Dongchuan, Zhao Chengliang, Aiping Li, Yan Jia_

- :fontawesome-solid-user-group: **Participant:** [NUDTSNA](./participants.md#nudtsna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/NUDTSNA-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/NUDTSNA-MB.pdf)
- :material-file-search: **Runs:** [SNACS](./runs.md#snacs) | [SNACSA](./runs.md#snacsa) | [SNACS_LA](./runs.md#snacs_la) | [SNACS_LB](./runs.md#snacs_lb)

??? abstract "Abstract"
	
	This paper describe our approaches to real-time filtering task in the TREC 2015 Microblog track, including push notifications on a mobile phone task and periodic email digest task. In the push notifications on a mobile phone task, we apply a recommendation framework with rank algorithm and dynamic threshold adjustment which utilizes both semantic content and quality of a tweet. External information extracted from Google search engine and word2vec model based on existing corpus are well incorporated to enhance the understanding of a tweet's or a profile's interest. In the email digest task, based on the candidate tweets retrieved from the first task, we calculate the score of a tweet considering semantic features and quality features, all the tweets classified into a topic are ranked by our key word bool logistic model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuHZCZLDCLJ15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuHZCZLDCLJ15,
		author = {Xiang Zhu and Jiuming Huang and Sheng Zhu and Ming Chen and Chenlu Zhang and Zhenzhen Li and Huang Dongchuan and Zhao Chengliang and Aiping Li and Yan Jia},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{NUDTSNA} at {TREC} 2015 Microblog Track: {A} Live Retrieval System Framework for Social Network based on Semantic Expansion and Quality Model},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/NUDTSNA-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuHZCZLDCLJ15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLIP at TREC 2015: Microblog and LiveQA

_Mossaab Bagdouri, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [CLIP](./participants.md#clip)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/CLIP-MBQA.pdf](http://trec.nist.gov/pubs/trec24/papers/CLIP-MBQA.pdf)
- :material-file-search: **Runs:** [CLIP-A-DYN-0.5](./runs.md#clip-a-dyn-0.5) | [CLIP-A-5.0-0.5](./runs.md#clip-a-5.0-0.5) | [CLIP-A-5.0-0.6](./runs.md#clip-a-5.0-0.6) | [CLIP-B-0.5](./runs.md#clip-b-0.5) | [CLIP-B-0.6](./runs.md#clip-b-0.6) | [CLIP-B-0.4](./runs.md#clip-b-0.4)

??? abstract "Abstract"
	
	The Computational Linguistics and Information Processing lab at the University of Maryland participated in two TREC tracks this year. The Microblog Real-Time Filtering and the LiveQA tasks both involve information processing in real time. We submitted nine runs in total, achieving relatively good results. This paper describes the architecture and configuration of the systems behind those runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BagdouriO15.bib) "
	```
	@inproceedings{DBLP:conf/trec/BagdouriO15,
		author = {Mossaab Bagdouri and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CLIP} at {TREC} 2015: Microblog and LiveQA},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/CLIP-MBQA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BagdouriO15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2015 Microblog Track: Real-Time Filtering Using Non-negative  Matrix Factorization

_Chaoyang Li, Zhen Yang, Kefeng Fan_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/BJUT-MB2.pdf](http://trec.nist.gov/pubs/trec24/papers/BJUT-MB2.pdf)
- :material-file-search: **Runs:** [BJUTllyQE](./runs.md#bjutllyqe) | [BjutNMF1](./runs.md#bjutnmf1) | [BjutNMF2](./runs.md#bjutnmf2)

??? abstract "Abstract"
	
	In this paper, we described our approaches to the Real-Time Filtering Task in the TREC 2015 Microblog track. We submitted the results for scenario B: periodic email digest. In this ad hoc search task, we introduced a real-time filtering framework using non-negative matrix factorization. To build this framework, we firstly considered the Real-Time Filtering Task as a short text retrieval problem, and proposed a non-negative matrix factorization based Microblog retrieval model (NMF Framework). Then after a review of the potential influencing factors in Microblog retrieval, the main influencing factor, i.e., short query expansion, was modeled as the additional regularized constraint items in NMF Framework. Experimental results show the proposed approach is better than classical method in microblog real-time filtering with the above-mentioned additional regularized constraint items.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiYF15.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiYF15,
		author = {Chaoyang Li and Zhen Yang and Kefeng Fan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2015 Microblog Track: Real-Time Filtering Using Non-negative Matrix Factorization},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/BJUT-MB2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiYF15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QU at TREC-2015: Building Real-Time Systems for Tweet Filtering  and Question Answering

_Reem Suwaileh, Maram Hasanain, Marwan Torki, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./participants.md#qu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/QU-MBQA.pdf](http://trec.nist.gov/pubs/trec24/papers/QU-MBQA.pdf)
- :material-file-search: **Runs:** [QUBaseline](./runs.md#qubaseline) | [QUDyn](./runs.md#qudyn) | [QUDynExp](./runs.md#qudynexp) | [QUBaselineB](./runs.md#qubaselineb) | [QUExpB](./runs.md#quexpb) | [QUFullExpB](./runs.md#qufullexpb)

??? abstract "Abstract"
	
	This paper presents our participation in the microblog and LiveQA tracks in TREC-2015. Both tracks required building a “real-time” system that monitors a data stream and responds to users' information needs in real-time. For the microblog track, given a set of users' interest profiles, we developed two online filtering systems that recommend “relevant” and “novel” tweets from a tweet stream for each profile. Both systems simulate real scenarios: filtered tweets are sent as push notifications on a mobile phone or as a periodic email digest. We study the e↵ect of using a static versus dynamic relevance thresholds to control the relevancy of filtered output to interest profiles. We also experiment with di↵erent profile expansion strategies that account for potential topic drift. Our results show that the baseline run of the push notifications scenario that uses a static threshold with light profile expansion achieved the best results. Similarly, in the email digest scenario, the baseline run that used a shorter representation of the interest profiles without any expansion was the best run. For the LiveQA track, the system was required to answer a stream of around 1000 real-time questions from Yahoo! Answers. We adopted a very simple approach that searched an archived Yahoo! Answers QA dataset for similar questions to the asked ones and retrieved back their answers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SuwailehHTE15.bib) "
	```
	@inproceedings{DBLP:conf/trec/SuwailehHTE15,
		author = {Reem Suwaileh and Maram Hasanain and Marwan Torki and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{QU} at {TREC-2015:} Building Real-Time Systems for Tweet Filtering and Question Answering},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/QU-MBQA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SuwailehHTE15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

