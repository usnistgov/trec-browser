# Proceedings - Microblog 2011 

#### Overview of the TREC 2011 Microblog Track

_Iadh Ounis, Craig Macdonald, Jimmy Lin, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec20/papers/MICROBLOG.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec20/papers/MICROBLOG.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Microblog track examines search tasks and evaluation methodologies for information seeking behaviours in microblogging environments such as Twitter. It was first introduced in 2011, addressing a real-time adhoc search task, whereby the user wishes to see the most recent but relevant information to the query. In particular, systems should respond to a query by providing a list of relevant tweets ordered from newest to oldest, starting from the time the query was issued. For TREC 2011, we used the newly-created Tweets2011 corpus. The corpus is comprised of 16M tweets over approximately two weeks, sampled courtesy of Twitter. The corpus is designed to be a reusable, representative sample of the twittersphere. As the reusability of a test collection is paramount in a TREC track, these sampled tweets can be obtained at any point in time (subjected to some caveats, discussed below). To accomplish this, the TREC Microblog track introduced a novel methodology whereby participants sign an agreement for the ids of the tweets in the corpus. Tools are then provided that permit the downloading of the corpus from the Twitter website. The first Microblog track in TREC 2011 has been a remarkable success. A total of 59 groups participated in the track from across the world, with 184 submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OunisMLS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/OunisMLS11,
		author = {Iadh Ounis and Craig Macdonald and Jimmy Lin and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {https://trec.nist.gov/pubs/trec20/papers/MICROBLOG.OVERVIEW.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OunisMLS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LiveTweet: Microblog Retrieval Based on Interestingness and an Adaptation  of the Vector Space Model

_Arifah Che Alhadi, Thomas Gottron, Jérôme Kunegis, Nasir Naveed_

- :fontawesome-solid-user-group: **Participant:** [WeST](./participants.md#west)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/WeST.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/WeST.microblog.update.pdf)
- :material-file-search: **Runs:** [WESTfilter](./runs.md#westfilter) | [WESTrelint](./runs.md#westrelint) | [WESTfilext](./runs.md#westfilext) | [WESTrlext](./runs.md#westrlext)

??? abstract "Abstract"
	
	This paper presents the Institute for Web Science and Technology's contribution to the TREC2011 Microblog Track. The goal of the Microblog Track is to address the user's information need in which a user wishes to see not only the most recent but also the most interesting and relevant information to a query in Twitter. In this paper we present the LiveTweet system, submitted by the Institute for Web Science and Technologies (WeST) from the University of Koblenz-Landau. The system addresses two issues of microblog media: sparsity and its effect on document length normalization, as well as the problem of assessing content quality. We provide the following approaches to overcome these issues: ignoring length normalization and using interestingness as a static quality measure to find the most recent and interesting tweets related to a given query topic. The results in similar settings have shown that deliberately ignoring length normalization yields better retrieval results in general and that interestingness improves retrieval for underspecified queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlhadiGKN11.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlhadiGKN11,
		author = {Arifah Che Alhadi and Thomas Gottron and J{\'{e}}r{\^{o}}me Kunegis and Nasir Naveed},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {LiveTweet: Microblog Retrieval Based on Interestingness and an Adaptation of the Vector Space Model},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/WeST.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlhadiGKN11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FUB, IASI-CNR, UNIVAQ at TREC 2011 Microblog Track

_Gianni Amati, Giuseppe Amodeo, Marco Bianchi, Giuseppe Marcone, Fondazione Ugo Bordoni, Carlo Gaibisso, Giorgio Gambosi, Alessandro Celi, Cesidio Di Nicola, Michele Flammini_

- :fontawesome-solid-user-group: **Participant:** [FUB](./participants.md#fub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/FUB.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/FUB.microblog.update.pdf)
- :material-file-search: **Runs:** [DFReeKLIM](./runs.md#dfreeklim) | [DFReeKLIM30](./runs.md#dfreeklim30) | [DFReeKLIMDC](./runs.md#dfreeklimdc) | [DFReeKLIMRA](./runs.md#dfreeklimra)

??? abstract "Abstract"
	
	The ad-hoc task of the microblogging track has an important theoretical impact for Information Retrieval. A key problem in Information Retrieval is, in fact, how to compare term frequencies among documents of different length. Apparently, term frequency normalization for microblogging can be simplified because of the short length constraint for the composition of admissible messages. The shortness of messages reduces the number of admissible values for the document length, and thus the length of a message can be regarded as if it were almost small and constant. On the other hand, short messages can carry a small amount of information, so that they are hardly distinguishable from each other for content. To overcome both problems, we propose to use a precise mathematical definition of information as the one given by Shannon [10] to provide an ad hoc IR model for Microblogging search. We show how to use Shannon's information theory and coding theory to weight the query content in Twitter messages and retrieve relevant messages. A second major problem of the microblogging track, as well as of any new collection of TREC, is the unavailability of a set of queries to derive and tune model parameters. Moreover, this is the first evaluation campaign on a new released corpus ever made for the microblogging search task, and in absence of any relevance data, it seems very interesting to define a retrieval methodology which is independent from relevance data, but still highly effective for the ranking of very short messages. Indeed, the proposed information theoretic methodology leads to the construction of a microblogging retrieval model that does not contain parameters to learn, and evaluation has shown the effectiveness of such parameter-free approach. In addition to these two major problems (i.e. how short length affects relevance and how to learn param- eters in absence of any relevance data), message recency is the only criterion applied to re-rank the retrieved messages. Thus, we regard the microblogging task more as a filtering decision task than as a ranking task. The new microblogging search task shares several similarities with some of the previous TREC evaluation campaigns, in particular with the past legal and blog TREC tracks. The legal track is basically a filtering task, that provides a large boolean retrieved set. In the legal track of TREC 2008 [8], for example, participants were asked to improve the quality of a given boolean baseline. This baseline was hard to improve according to the official evaluation measure. The task was to perform a dynamic cut-off value K in the ranking, being all evaluation measures estimated at the depth of this variable value for K, e.g. the precision and recall at depth K, P @K or R@K or other similar official measures used to assess the quality of the retrieved set. Similarly to the recency re-ordering of retrieved messages, in the TREC 2008 blog track [6] participants had to re-rank the documents by relevance according also to an opinion content dimension. An evaluation study however showed that filtering relevant documents by a second dimension or criterion, such as the opinionated content of documents, is often more harmful than performing a mild re-ranking strategy for the official MAP or P@10 measures [3] or even no re-ordering at all. As a consequence of these general remarks we made the following hypotheses and submissions: a) We have submitted a standard TREC baseline (the run named DFReeKLIM with 1000 messages retrieved per query) ordered by relevance only, that is without any time analysis, in order to assess how time re-ranking affects the precision at different depths of the retrieved set. b) Relevance by score distribution follows a mixture of two distributions (e.g. one exponential for the non-relevant documents, and the normal for the relevant ones [7,11]). Therefore, relevant documents have to be found on top of the ranking, and indeed P @K is a decreasing function with respect to K. It has been also observed that the precision at depth K, P @K, increases with collection size [5]. We assumed that relevance is dependent of recency of the messages. However, a pure re-ranking by time of the first K topmost messages, retrieved by relevance, hardly improve the official measure P @30 when K 6 = 30 since relevance scores and relevance ranks do not distribute uniformly but follow a power law. Therefore we submitted an official run retrieving exactly 30 messages per query (the run named DFReeKLIM30). c) We made a preliminary recency analysis. A dynamical cut to the retrieved set was introduced. The aim was to predict the best K documents for each query for which time reordering would have been successful. The mean threshold value for K was 73. The effectiveness of the methodology (run DFReeKLIMDC) must be assessed by the evaluation measures on time re-ranking. d) We explicitly assumed dependence of relevance with respect to time and used the time ranking as recency score to reorder by relevance the first pass retrieval. The effectiveness of the methodology can be thus assessed by the evaluation measures on relevance and not by time re-ranking, as performed by the official TREC measures (run DFReeKLIMRA).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmatiA0MBGGCNF11.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmatiA0MBGGCNF11,
		author = {Gianni Amati and Giuseppe Amodeo and Marco Bianchi and Giuseppe Marcone and Fondazione Ugo Bordoni and Carlo Gaibisso and Giorgio Gambosi and Alessandro Celi and Cesidio Di Nicola and Michele Flammini},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {FUB, IASI-CNR, {UNIVAQ} at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/FUB.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmatiA0MBGGCNF11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NUSIS at TREC 2011 Microblog Track: Refining Query Results with  Hashtags

_Hadi Amiri, Yang Bao, Anindya Datta, Xiaoying Xu, Anqi Cui_

- :fontawesome-solid-user-group: **Participant:** [NUSIS](./participants.md#nusis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/NUSIS.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/NUSIS.microblog.pdf)
- :material-file-search: **Runs:** [relevanceRun](./runs.md#relevancerun) | [balanceRun](./runs.md#balancerun) | [refRelRun](./runs.md#refrelrun) | [refBalRun](./runs.md#refbalrun)

??? abstract "Abstract"
	
	In this paper, we describe our submission to the TREC 2011 Microblog track. We first use URLs as a clue to discover and remove the spam tweets. Then we use both Lucene and Indri to generate a ranked list of results for each query, together with their relevance scores. After that, we use the scores to find out useful hashtags relevant to the query, therefore some previously lower-ranked tweets can be discovered and are re-ranked higher. Query reformulation is considered in two of the four runs in our submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmiriBDXC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmiriBDXC11,
		author = {Hadi Amiri and Yang Bao and Anindya Datta and Xiaoying Xu and Anqi Cui},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NUSIS} at {TREC} 2011 Microblog Track: Refining Query Results with Hashtags},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/NUSIS.microblog.pdf},
		timestamp = {Mon, 03 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AmiriBDXC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion for Microblog Retrieval

_Ayan Bandyopadhyay, Mandar Mitra, Prasenjit Majumder_

- :fontawesome-solid-user-group: **Participant:** [IRSI](./participants.md#irsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/IRSI.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/IRSI.microblog.update.pdf)
- :material-file-search: **Runs:** [IRSIGoogle1G](./runs.md#irsigoogle1g) | [IRSIGoogle2G](./runs.md#irsigoogle2g) | [Google1GNO](./runs.md#google1gno) | [InL2c1](./runs.md#inl2c1)

??? abstract "Abstract"
	
	Entries in microblogging sites such as Twitter are very short: a “tweet ”can contain at most 140 characters. Given a user query, retrieving relevant tweets is particularly challenging since their extreme brevity exacerbates the well-known vocabulary mismatch problem. In this preliminary study, we explore standard query expansion approaches as a way to address this problem. Since the tweets are short, we use external corpora as a source for query expansion terms. Specifically, we used the Google Search API (GSA) to retrieve pages from the Web, and used the titles to expand queries. Initial results on the TREC 2011 Microblog test data are very promising. Since many of the TREC topics were oriented towards the news genre, we also tried restricting the GSA to a news site (BBC) in the hope that it would be a cleaner, less noisy source for expansion terms. This turned out to be counter-productive. Some analysis of these results is also included.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BandyopadhyayMM11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BandyopadhyayMM11,
		author = {Ayan Bandyopadhyay and Mandar Mitra and Prasenjit Majumder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Query Expansion for Microblog Retrieval},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/IRSI.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BandyopadhyayMM11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ISTI@TREC Microblog Track 2011: Exploring the Use of Hashtag Segmentation  and Text Quality Ranking

_Giacomo Berardi, Andrea Esuli, Diego Marcheggiani, Fabrizio Sebastiani_

- :fontawesome-solid-user-group: **Participant:** [NEMIS_ISTI_CNR](./participants.md#nemis_isti_cnr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/NEMIS_ISTI_CNR.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/NEMIS_ISTI_CNR.microblog.update.pdf)
- :material-file-search: **Runs:** [runNeMIS](./runs.md#runnemis) | [runNeMISext](./runs.md#runnemisext)

??? abstract "Abstract"
	
	In the first year of the TREC Micro Blog track, our participation has focused on building from scratch an IR system based on the Whoosh IR library. Though the design of our system (CipCipPy) is pretty standard it includes three ad-hoc solutions for the track: (i) a dedicated indexing function for hashtags that automatically recognizes the distinct words composing an hashtag, (ii) expansion of tweets based on the title of any referred Web page, and (iii) a tweet ranking function that ranks tweets in results by their content quality, which is compared against a reference corpus of Reuters news. In this preliminary paper we describe all the components of our system, and the efficacy scored by our runs. The CipCipPy system is available under a GPL license.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BerardiEMS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BerardiEMS11,
		author = {Giacomo Berardi and Andrea Esuli and Diego Marcheggiani and Fabrizio Sebastiani},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {ISTI@TREC Microblog Track 2011: Exploring the Use of Hashtag Segmentation and Text Quality Ranking},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/NEMIS\_ISTI\_CNR.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BerardiEMS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Microblog Track TREC 2011

_Peng Cao, Jinhua Gao, Yubao Yu, Shenghua Liu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ICTNET.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/ICTNET.microblog.pdf)
- :material-file-search: **Runs:** [ICTNET11MBR1](./runs.md#ictnet11mbr1) | [ICTNET11MBR2](./runs.md#ictnet11mbr2) | [ICTNET11MBR3](./runs.md#ictnet11mbr3) | [ICTNET11MBR4](./runs.md#ictnet11mbr4)

??? abstract "Abstract"
	
	The ICTNET group has participated in the Microblog track of TREC 2011. The main task is to search the messy tweets for those about a topic that is represented by a query. There are 50 queries, i.e. topics given for the track totally. Besides the topic description, a query time is also given for each query, indicating the exact time of the query issuance. The search is supposed to be conducted onsite, and those tweets later than the query time should not be returned. Furthermore, the issuers wishes to see the most recent but relevant information to the query. Hence, our system should answer a query by providing a list of relevant tweets ordered from newest to oldest, starting from the time the query was issued. The existing related work about microblog is mainly focused on users [1-2], information flow [3-4], and tweets' content [5-6]. Our work is to query the tweets' content to find relevant, interesting, and fresh tweets. With exploring the features of tweets' content, hashtags, urls, post time etc., we employ SVM ranking model to rank our query results. The model is trained on pair-wise labeled data. Query extension both within tweets and external Wikipedia articles and Google search results are conducted by pseudo relevance feedback method and keywords extracting. In our experiment, 4 running results of 50 queries are collected on more than 5.6 million English tweets. There are 64.6% relevant tweets retrieved in less than 1000 returned results, and 449 relevant tweets are retrieved in top 30 according our ranking scores. The rest of the report is organized as follows. Section 2 introduces the data preprocessing. Section 3 describes our main method to rank the search results namely the learning to rank. Section 4 shows the experiment results, and section 5 concludes the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaoGYLLC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaoGYLLC11,
		author = {Peng Cao and Jinhua Gao and Yubao Yu and Shenghua Liu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Microblog Track {TREC} 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ICTNET.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CaoGYLLC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Simple Rank-Based Filtering for Microblog Retrieval: Implications  for Evaluation and Test Collections

_Ben Carterette, Naveen Kumar, Ashwani Rao, Dongqing Zhu_

- :fontawesome-solid-user-group: **Participant:** [udel](./participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/udel.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/udel.microblog.pdf)
- :material-file-search: **Runs:** [udelIndri](./runs.md#udelindri) | [udelLucene](./runs.md#udellucene)

??? abstract "Abstract"
	
	The IR Lab at the University of Delaware participated in the first year of the TREC Microblog track. We submitted two runs using two different indexers and ranking functions, one of which filtered results by a score threshold. The results inspired some post hoc analysis of the test collection, which is the main focus of this paper. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarteretteKRZ11.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarteretteKRZ11,
		author = {Ben Carterette and Naveen Kumar and Ashwani Rao and Dongqing Zhu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Simple Rank-Based Filtering for Microblog Retrieval: Implications for Evaluation and Test Collections},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/udel.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarteretteKRZ11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Microblog 2011

_Firas Damak, Lamjed Ben Jabeur, Guillaume Cabanac, Karen Pinel-Sauvagnat, Lynda Tamine, Mohand Boughanem_

- :fontawesome-solid-user-group: **Participant:** [IRIT_SIG](./participants.md#irit_sig)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/IRIT_SIG.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/IRIT_SIG.microblog.update.pdf)
- :material-file-search: **Runs:** [iritfd1](./runs.md#iritfd1) | [iritfd2](./runs.md#iritfd2) | [Nestor](./runs.md#nestor) | [NestorS](./runs.md#nestors)

??? abstract "Abstract"
	
	This paper describes the participation of the IRIT lab, university of Toulouse, France, to the Microblog Track of TREC 2011. Two different approaches were experimented by our team, which are described in the two main parts of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DamakJCPTB11.bib) "
	```
	@inproceedings{DBLP:conf/trec/DamakJCPTB11,
		author = {Firas Damak and Lamjed Ben Jabeur and Guillaume Cabanac and Karen Pinel{-}Sauvagnat and Lynda Tamine and Mohand Boughanem},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRIT} at {TREC} Microblog 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/IRIT\_SIG.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DamakJCPTB11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting Social #-Tagging Behavior in Twitter for Information  Filtering and Recommendation

_Ernesto Diaz-Aviles, Patrick Siehndel, Kaweh Djafari Naini_

- :fontawesome-solid-user-group: **Participant:** [L3S](./participants.md#l3s)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/L3S.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/L3S.microblog.update.pdf)
- :material-file-search: **Runs:** [qHtagBaseRun](./runs.md#qhtagbaserun)

??? abstract "Abstract"
	
	We present a ranking approach for Twitter documents that exploits social hashtagging behavior. We first map topics of user interest, represented by keywords, to a set of twitter hashtags that we use as query terms to retrieve twitter documents (tweets) based on tf-idf scores, with the additional restrictions that the documents retrieved should occur before the query timestamp. We show that this simple method performs significantly better than a disjunctive baseline based on the topic description.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Diaz-AvilesSN11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Diaz-AvilesSN11,
		author = {Ernesto Diaz{-}Aviles and Patrick Siehndel and Kaweh Djafari Naini},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploiting Social {\#}-Tagging Behavior in Twitter for Information Filtering and Recommendation},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/L3S.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Diaz-AvilesSN11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Illinois' Graduate School of Library and Information  Science at TREC 2011

_Miles Efron_

- :fontawesome-solid-user-group: **Participant:** [gslisUIUC](./participants.md#gslisuiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/gslisUIUC.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/gslisUIUC.microblog.update.pdf)
- :material-file-search: **Runs:** [gus](./runs.md#gus) | [gust](./runs.md#gust) | [gustc](./runs.md#gustc) | [gut](./runs.md#gut)

??? abstract "Abstract"
	
	The University of Illinois' Graduate School of Library and Information Science (GSLIS) participated in TREC's microblog track this year-the track's first iteration. In keeping with the foundational status of the track, our goals were chosen to emphasize the role of a single factor in microblog IR: time. As such, we adhered to the strictest guidelines of the task description, using only real-time information available in the microblog corpus to inform retrieval. Our innovation involved assessing the extent to which (and the way in which) temporal factors can improve microblog search effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Efron11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Efron11,
		author = {Miles Efron},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Illinois' Graduate School of Library and Information Science at {TREC} 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/gslisUIUC.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Efron11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Online Topic Modeling for Real-Time Twitter Search

_Christan Earl Grant, Clint P. George, Chris Jenneisch, Joseph N. Wilson_

- :fontawesome-solid-user-group: **Participant:** [Morpheus](./participants.md#morpheus)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Morpheus.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Morpheus.microblog.update.pdf)
- :material-file-search: **Runs:** [MorpheusRun1](./runs.md#morpheusrun1)

??? abstract "Abstract"
	
	This paper discusses the work done by a team at the University of Florida for the TREC 2011 Microblog Track. To build a real-time microblog search engine we rely on topic modeling for our search. To facilitate our algorithms we bundle similar tweets together in what we call supertweet generation. We perform online inference and offline inference depending on the time frame of the topical query. In this paper we discuss our techniques, challenges, future work, but not the evaluation of our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrantGJW11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrantGJW11,
		author = {Christan Earl Grant and Clint P. George and Chris Jenneisch and Joseph N. Wilson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Online Topic Modeling for Real-Time Twitter Search},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Morpheus.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrantGJW11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melbourne Language Group Microblog Track Report

_Bo Han, Marco Lui, Timothy Baldwin_

- :fontawesome-solid-user-group: **Participant:** [UniMelbLT](./participants.md#unimelblt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UniMelbLT.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UniMelbLT.microblog.update.pdf)
- :material-file-search: **Runs:** [melblt](./runs.md#melblt)

??? abstract "Abstract"
	
	This report outlines the TREC 2011 microblog track submission of the Language Technology Group at The University of Melbourne. The microblog track is an ad-hoc retrieval task over Twitter data with temporally-specified queries, and the requirement that all results must predate the query. Our objective is to establish baseline results for the task and study the relative impact of various factors on microblog retrieval. Twitter messages are authored in many different languages (Hong et al., 2011), but the queries were all monolingual English and assessors where instructed to base their judgements on only the English content of tweets. As such, we first conduct language identification to filter out non-English tweets (Baldwin and Lui, 2010). Next, we lexically-normalise tweets, to remove typos and phonetic substitutions, and deabbreviate common abbreviations (Han and Baldwin, 2011). Finally, we index the language-filtered, normalised documents using Indri,1 apply dynamic lexical normalisation to the queries, and temporally filter the results relative to the query timestamp. Descriptions of each module in our system are presented in the following sections. As we use language processing tools and a dictionary as part of the lexical normalisation, our submission is classified as making use of external evidence.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HanLB11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HanLB11,
		author = {Bo Han and Marco Lui and Timothy Baldwin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Melbourne Language Group Microblog Track Report},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UniMelbLT.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HanLB11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion and Message-Passing Algorithms for TREC Microblog  Track

_Dzung Hong, Qifan Wang, Dan Zhang, Luo Si_

- :fontawesome-solid-user-group: **Participant:** [Purdue_IR](./participants.md#purdue_ir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Purdue_IR.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Purdue_IR.microblog.update.pdf)
- :material-file-search: **Runs:** [myRun](./runs.md#myrun) | [myrun3](./runs.md#myrun3) | [myrun2](./runs.md#myrun2)

??? abstract "Abstract"
	
	This report describes the methods that our Information Retrieval Group at Purdue University used for the TREC Microblog 2011 track. The first method is the pseudo-relevance feedback, a traditional algorithm to reformulate the query by adding expanded terms to the query. The second method is the affinity propagation, a non parametric clustering algorithm that can group the top tweets according to their similarities. The final score of a tweet is based on its relevance score and the relevance score of its representative in the group. We found that query expansion is a very useful technique for microblog retrieval, while affinity propagation could achieve a comparable performance when combining with other techniques.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HongWZS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HongWZS11,
		author = {Dzung Hong and Qifan Wang and Dan Zhang and Luo Si},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Query Expansion and Message-Passing Algorithms for {TREC} Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Purdue\_IR.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HongWZS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Realtime Ad Hoc Search in Twitter: Know-Center at TREC Microblog  Track 2011

_Christopher Horn, Oliver Pimas, Michael Granitzer, Elisabeth Lex_

- :fontawesome-solid-user-group: **Participant:** [knowcenter](./participants.md#knowcenter)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/knowcenter.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/knowcenter.microblog.update.pdf)
- :material-file-search: **Runs:** [1](./runs.md#1) | [2](./runs.md#2) | [3](./runs.md#3) | [4](./runs.md#4)

??? abstract "Abstract"
	
	In this paper, we outline our experiments carried out at the TREC Microblog Track 2011. Our system is based on a plain text index extracted from Tweets crawled from twitter.com. This index has been used to retrieve candidate Tweets for the given topics. The resulting Tweets were post-processed and then analyzed using three different approaches: (i) a burst detection approach, (ii) a hashtag analysis, and (iii) a Retweet analysis. Our experiments consisted of four runs: Firstly, a combination of the Lucene ranking with the burst detection, and secondly, a combination of the Lucene ranking, the burst detection, and the hashtag analysis. Thirdly, a combination of the Lucene ranking, the burst detection, the hashtag analysis, and the Retweet analysis, and fourthly, again a combination of the Lucene ranking with the burst detection but in this case with more sophisticated query language and post-processing. We achieved the best MAP values overall in the fourth run.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HornPGL11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HornPGL11,
		author = {Christopher Horn and Oliver Pimas and Michael Granitzer and Elisabeth Lex},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Realtime Ad Hoc Search in Twitter: Know-Center at {TREC} Microblog Track 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/knowcenter.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HornPGL11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lugano at TREC 2011 Microblog Track

_Giacomo Inches_

- :fontawesome-solid-user-group: **Participant:** [ULugano](./participants.md#ulugano)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ULugano.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/ULugano.microblog.update.pdf)
- :material-file-search: **Runs:** [baselineBM25](./runs.md#baselinebm25)

??? abstract "Abstract"
	
	In this document we present the participation of University of Lugano in the Microblog track of TREC 2011. We describe our approach based on a time-based filtering algorithm of retrieved documents. We highlight the results and the possible improvement of the described technique.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Inches11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Inches11,
		author = {Giacomo Inches},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Lugano at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ULugano.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Inches11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BEST of KAUST at TREC 2011: Building Effective Search in Twitter

_Jinling Jiang, Lailatul Hidayah, Hany E. Ramadan, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [KAUST](./participants.md#kaust)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/kaust.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/kaust.microblog.update.pdf)
- :material-file-search: **Runs:** [KAUSTExpRrnk](./runs.md#kaustexprrnk) | [KAUSTExp](./runs.md#kaustexp) | [KAUSTRerank](./runs.md#kaustrerank) | [KAUSTBase](./runs.md#kaustbase)

??? abstract "Abstract"
	
	In our first-ever appearance at TREC, we explore initial ideas on building an effective search tool over tweet stream as a participation in this year's microblog track. Among those ideas are tweet expansion with short representation of terms that frequently co-occur with hashtags and URLs, and re-ranking based on statistics that estimate user popularity (using replies and mentions), tweet popularity, URL popularity and user topic authority (using simple user profiles). Initial results show that re-ranking improves the effectiveness while expansion sometimes harms it. Overall, the system built for the task is indeed a great resource for further extensions and experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangHREL11.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangHREL11,
		author = {Jinling Jiang and Lailatul Hidayah and Hany E. Ramadan and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BEST} of {KAUST} at {TREC} 2011: Building Effective Search in Twitter},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/kaust.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangHREL11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QCRI @ TREC 2011: Microblog Track

_Ali El Kahki, Kareem Darwish_

- :fontawesome-solid-user-group: **Participant:** [QCRI](./participants.md#qcri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/QCRI.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/QCRI.microblog.pdf)
- :material-file-search: **Runs:** [QCRIwTagOrg](./runs.md#qcriwtagorg) | [QCRIwoTagOrg](./runs.md#qcriwotagorg) | [nQCRIwTag](./runs.md#nqcriwtag) | [nQCRIwoTag](./runs.md#nqcriwotag)

??? abstract "Abstract"
	
	This paper briefly describes the Qatar Computing Research Institute (QCRI) participation in the TREC 2011 Microblog track. The focus of our TREC submissions was on using a generative graphic model to perform query expansion. We trained a model that attempted to predict appropriate hashtags to expand tweets as well as queries. In essence, we used hashtags to represent latent topics in tweets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KahkiD11.bib) "
	```
	@inproceedings{DBLP:conf/trec/KahkiD11,
		author = {Ali El Kahki and Kareem Darwish},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{QCRI} @ {TREC} 2011: Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/QCRI.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KahkiD11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microblog Retrieval Using Topical Features and Query Expansion

_Cher Han Lau, Yuefeng Li, Dian Tjondronegoro_

- :fontawesome-solid-user-group: **Participant:** [QUT1](./participants.md#qut1)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/QUT1.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/QUT1.microblog.pdf)
- :material-file-search: **Runs:** [run3a](./runs.md#run3a) | [run4a](./runs.md#run4a) | [run1a](./runs.md#run1a) | [run2a](./runs.md#run2a)

??? abstract "Abstract"
	
	Retrieving information from Twitter is always challenging given its volume, inconsistent writing and noise. Existing systems focus on term-based approach, but important topical features such as person, proper noun and events are often neglected, leading to less satisfactory results while searching information from tweets. This paper propose a novelty feature extraction algorithm which targets the above problems, and present the experiment results using TREC11 dataset. The proposed approach considers both term-based and pattern-based features and distribute weights accordingly. We experiment four different setting to evaluate different combinations and results show that our approach outperformed traditional method of using term-based or pattern only methods and signify the importance of topical features in microblog retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LauLT11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LauLT11,
		author = {Cher Han Lau and Yuefeng Li and Dian Tjondronegoro},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microblog Retrieval Using Topical Features and Query Expansion},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/QUT1.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LauLT11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HIT_LTRC at TREC 2011 Microblog Track

_Yun Li, Xishuang Dong, Yi Guan_

- :fontawesome-solid-user-group: **Participant:** [HIT_LTRC](./participants.md#hit_ltrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/HIT_LTRC.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/HIT_LTRC.microblog.pdf)
- :material-file-search: **Runs:** [hitWIt](./runs.md#hitwit) | [hitWId](./runs.md#hitwid)

??? abstract "Abstract"
	
	This paper describes our entry into the TREC 2011 Microblog track. We submitted two runs in this year's track, both in real-time fashion and without any external resources. The runs were generated through a three-step procedure, including scoring, threshold selection and re-ranking. The evaluation results of our submitted runs significantly outperform the disjunctive baseline run. We conducted additional runs to show our score decay and threshold selection strategies to be exceptionally effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiDG11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiDG11,
		author = {Yun Li and Xishuang Dong and Yi Guan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {HIT{\_}LTRC at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/HIT\_LTRC.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiDG11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DMIR on Microblog Track 2011

_Wen Li, Carsten Eickhoff, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [TUD_DMIR](./participants.md#tud_dmir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/TUD-DMIR.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/TUD-DMIR.microblog.pdf)
- :material-file-search: **Runs:** [EMAX](./runs.md#emax) | [RTB](./runs.md#rtb)

??? abstract "Abstract"
	
	In this paper we present our work on the Microblog Track of TREC 2011. We tried two methods to tackle the problem of tweet retrieval, namely EMAX and RTB. The first method EMAX is mainly based on the intuition that not only should retrieved tweets related to the keywords in given queries but also provide more information. This results in a ranking method based on self-information. Our second method RTB tries to incorporate the importance of recency along with relevance in microblog retrieval tasks. Therefore, we adapt portfolio theory to balance the relevance dimension and recency dimension. However, the evaluation results suggest no significant improvement from both two methods because of the short lengths of documents, the noisy and spam tweets and the re-ordering in recency. Meanwhile, we also present some ideas during the course of participation. By closely examining the judgments, we find that most of relevant documents are those containing a link to external resource and have a length of around 17 words, which is different from the statistics observed in the collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiEV11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiEV11,
		author = {Wen Li and Carsten Eickhoff and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DMIR} on Microblog Track 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/TUD-DMIR.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiEV11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Author Model and Negative Feedback Methods on TREC 2011 Microblog  Track

_Rui Li, Binjie Wei, Kai Lu, Bin Wang_

- :fontawesome-solid-user-group: **Participant:** [ICTIR](./participants.md#ictir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ICTIR.microblog.new.pdf](http://trec.nist.gov/pubs/trec20/papers/ICTIR.microblog.new.pdf)
- :material-file-search: **Runs:** [baseline](./runs.md#baseline) | [run1](./runs.md#run1) | [run1fix](./runs.md#run1fix) | [run2](./runs.md#run2)

??? abstract "Abstract"
	
	This paper gives an overview of our work (the ICTIR group) in microblog track of TREC 2011 for tweets retrieval. The basic query likelihood model with smoothing is the fundamental method in our approaches, we also consider other factors: the author information and the negative feedback. Firstly, we classify all queries into three categories, construct refined feedback in different ways to reform them; Secondly, extremely short tweets lead to poor clustering performance, the author topic models are trained for tweets expansion and smoothing. Finally, we train negative feedback model to reduce noise impacts in our microblog search task. Experimental results show that our methods could improve the retrieval performance greatly.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiWLW11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiWLW11,
		author = {Rui Li and Binjie Wei and Kai Lu and Bin Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Author Model and Negative Feedback Methods on {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ICTIR.microblog.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiWLW11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2011 Microblog Track

_Yan Li, Zhenhua Zhang, Wenlong Lv, Qianlong Xie, Yuhang Lin, Rao Xu, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/PRIS.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/PRIS.microblog.pdf)
- :material-file-search: **Runs:** [PRISrun1](./runs.md#prisrun1) | [PRISrun2](./runs.md#prisrun2) | [PRISrun3](./runs.md#prisrun3) | [PRISrun4](./runs.md#prisrun4)

??? abstract "Abstract"
	
	Our system to Micro-blog Track at TREC2011 is described in this paper, which includes data obtaining and preprocessing, index building and query expansion. There‟re two methods of query expansion introduced in this report: Word Activation Force algorithm (WAF) and Electric Resistance Network. We also show the evaluation results for our team and the comparison with the best and median evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiZLXLXXCG11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiZLXLXXCG11,
		author = {Yan Li and Zhenhua Zhang and Wenlong Lv and Qianlong Xie and Yuhang Lin and Rao Xu and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/PRIS.microblog.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiZLXLXXCG11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKU_ICST at TREC 2011 Microblog Track

_Feng Liang, Runwei Qiang, Jianwu Yang_

- :fontawesome-solid-user-group: **Participant:** [PKU_ICST](./participants.md#pku_icst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/PKU_ICST.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/PKU_ICST.microblog.update.pdf)
- :material-file-search: **Runs:** [PKUICST](./runs.md#pkuicst) | [PKUICST2](./runs.md#pkuicst2) | [PKUICST3](./runs.md#pkuicst3) | [PKUICST4](./runs.md#pkuicst4)

??? abstract "Abstract"
	
	This paper describes the PKU_ICST participation in the TREC 2011 Microblog track. In the first year of Microblog track, we designed a group of experiments to verify whether external resources and future resources would improve the performance of our system. Moreover, given that microblog track is a real-­-‑time adhoc task, we explored an approach making use of the temporal evidence. To obtain a better performance, we employed different strategies to generate final results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiangQY11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiangQY11,
		author = {Feng Liang and Runwei Qiang and Jianwu Yang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {PKU{\_}ICST at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/PKU\_ICST.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiangQY11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Indonesia at TREC 2011 Microblog Task

_Samuel Louvan, Mochamad Ibrahim, Mirna Adriani, Clara Vania, Bayu Distiawan, Metti Zakaria Wanagiri_

- :fontawesome-solid-user-group: **Participant:** [FASILKOMUI](./participants.md#fasilkomui)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/FASILKOM.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/FASILKOM.microblog.update.pdf)
- :material-file-search: **Runs:** [FASILKOM01](./runs.md#fasilkom01) | [FASILKOM03](./runs.md#fasilkom03) | [FASILKOM04](./runs.md#fasilkom04) | [FASILKOM02](./runs.md#fasilkom02)

??? abstract "Abstract"
	
	In this paper we describe our submission to the TREC2011 MicroblogTrack. Our run combines different methods namely customized scoring function, query reformulation, and query expansion. We apply query expansion from dataset with different weighting scheme. Furthermore, we do an initial experiment to incorporate timestamp of the tweet document in order to improve search performance. We found the query expansion utilizing external search result combined with re-tweet value in the customized scoring function was the most effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LouvanIAVDW11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LouvanIAVDW11,
		author = {Samuel Louvan and Mochamad Ibrahim and Mirna Adriani and Clara Vania and Bayu Distiawan and Metti Zakaria Wanagiri},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Indonesia at {TREC} 2011 Microblog Task},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/FASILKOM.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LouvanIAVDW11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### USC/ISI at TREC 2011: Microblog Track

_Donald Metzler, Congxing Cai_

- :fontawesome-solid-user-group: **Participant:** [isi](./participants.md#isi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/isi.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/isi.microblog.update.pdf)
- :material-file-search: **Runs:** [isiFD](./runs.md#isifd) | [isiFDL](./runs.md#isifdl) | [isiFDRML](./runs.md#isifdrml) | [isiFDRM](./runs.md#isifdrm)

??? abstract "Abstract"
	
	This paper describes the search system we developed for the inaugural TREC 2011 Microblog Track. Our system makes use of best-practice ranking techniques, including term, phrase, and proximity-based text matching via the Markov random field model, pseudo-relevance feedback using Latent Concept Expansion, and a feature-based ranking model that uses a simple, but effective learning-to-rank model. We adapted each of these approaches to the specifics of the microblog search task, giving rise to a highly effective end-to-end search system. The official results from the TREC evaluation suggest that pseudo-relevance feedback and learning-to-rank yield significant improvements in precision at early rank under different evaluation scenarios.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MetzlerC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/MetzlerC11,
		author = {Donald Metzler and Congxing Cai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{USC/ISI} at {TREC} 2011: Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/isi.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MetzlerC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2011 Microblog Track Experiments at Kobe University

_Taiki Miyanishi, Naoto Okamura, Xiaoxi Liu, Kazuhiro Seki, Kuniaki Uehara_

- :fontawesome-solid-user-group: **Participant:** [KobeU](./participants.md#kobeu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/KobeU.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/KobeU.microblog.update.pdf)
- :material-file-search: **Runs:** [rit](./runs.md#rit) | [ri](./runs.md#ri) | [normal](./runs.md#normal) | [rit3](./runs.md#rit3)

??? abstract "Abstract"
	
	This paper describes our approach to real-time microblog search that returns tweets for a given query in reverse chronological order. The approach utilizes a learning-to-rank (L2R) algorithm that has been increasingly used for information retrieval (IR). Generally, L2R algorithms require features which represent the associations between a user query and a document (tweet in this case). However, it is more difficult for microblog search to obtain rich features than traditional document search because the contents of microblog are too short: limited to only 140 characters. In addition, there is no standard, publicly available training data for learning to rank microblogs. To solve these problems, we generate new features by clustering large microblog data (the Tweets2011 corpus). The features are de ned for triplets ⟨user query, tweet, cluster⟩ and represent the relevance of the tweet with respect to both the query and its topic (cluster). An L2R model is learned using the generated features as well as other features on labeled training data manually created by our research group. The effectiveness of the proposed approach is demonstrated by comparative experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MiyanishiOLSU11.bib) "
	```
	@inproceedings{DBLP:conf/trec/MiyanishiOLSU11,
		author = {Taiki Miyanishi and Naoto Okamura and Xiaoxi Liu and Kazuhiro Seki and Kuniaki Uehara},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2011 Microblog Track Experiments at Kobe University},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/KobeU.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MiyanishiOLSU11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Yandex at TREC 2011 Microblog Track

_Zlata Obukhovskaya, Konstantin Pervyshev, Andrey Styskin, Pavel Serdyukov_

- :fontawesome-solid-user-group: **Participant:** [yandex](./participants.md#yandex)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/yandex.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/yandex.microblog.update.pdf)
- :material-file-search: **Runs:** [YNDXTPC2](./runs.md#yndxtpc2) | [YNDXTPC1](./runs.md#yndxtpc1) | [ya3](./runs.md#ya3) | [ya4](./runs.md#ya4)

??? abstract "Abstract"
	
	Building microblog search is a challenging task in many ways. One of its most exciting aspects is the creation of reliable search engine architecture. However in our work we focused on tweet retrieval, utilizing relevance signals coming from various sources related to a tweet and learning to rank. For ranking-related tasks we decided to rely on the following data sources: Text sources: tweet itself and the title of the linked URL: Crowd activity (retweets) We assumed that the number of retweets should be a good indicator of social interest to the particular document and the retweet prediction would be a useful feature for ranking. Also we encountered a problem with low recall of TF-based retrieval on small-sized twitter documents. This prompted us to use flexible term weighting models and query expansion to avoid missing relevant results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ObukhovskayaPSS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ObukhovskayaPSS11,
		author = {Zlata Obukhovskaya and Konstantin Pervyshev and Andrey Styskin and Pavel Serdyukov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Yandex at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/yandex.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ObukhovskayaPSS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Wolverhampton at the TREC 2011 Microblog Track

_Georgios Paltoglou, Mike Thelwall_

- :fontawesome-solid-user-group: **Participant:** [UoW](./participants.md#uow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UoW.microblog.new.pdf](http://trec.nist.gov/pubs/trec20/papers/UoW.microblog.new.pdf)
- :material-file-search: **Runs:** [PL2NoQeSd](./runs.md#pl2noqesd) | [PL2NoQeSdExt](./runs.md#pl2noqesdext) | [PL2NoQENoDM](./runs.md#pl2noqenodm) | [PL2Bo1SDExt](./runs.md#pl2bo1sdext)

??? abstract "Abstract"
	
	In this report we discuss the experiments we conducted at the University of Wolverhampton for the Microblog Track at TREC-2011. As this was the first time we participated in TREC and the particular task presents some unique challenges we initially focused on properly analyzing and indexing the new Tweets2011 Corpus. We experimented with the effects that some standard IR techniques, such as query expansion and proximity models have in this setting. Initial results indicated that both techniques provide small increases in precision, but more experiments are needed for final conclusions to be reached. Lastly, we experimented with using the page that a tweet links to as part of the tweet. The results were particularly low, indicating a potential error in the indexing process or a natural outcome, due to the increased length of the combined documents. More research into answering the issue is underway.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PaltoglouT11.bib) "
	```
	@inproceedings{DBLP:conf/trec/PaltoglouT11,
		author = {Georgios Paltoglou and Mike Thelwall},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Wolverhampton at the {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UoW.microblog.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PaltoglouT11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at TREC 2011 Microblog Track

_Matthias Petri, J. Shane Culpepper, Falk Scholer_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/RMIT.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/RMIT.microblog.pdf)
- :material-file-search: **Runs:** [RMITM](./runs.md#rmitm) | [RMITMR](./runs.md#rmitmr) | [RMITAR](./runs.md#rmitar) | [RMITMRR](./runs.md#rmitmrr)

??? abstract "Abstract"
	
	This paper describes our submission to the TREC 2011 microblog task. For the experiments, we use our new self-index search engine, NeWT, to support ranked search in the Twitter document corpus. We use a combination of phrase queries and degrading conjunctive Boolean intersection to improve retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PetriCS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/PetriCS11,
		author = {Matthias Petri and J. Shane Culpepper and Falk Scholer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/RMIT.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PetriCS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at TREC 2011 Microblog Track

_Adam Roegiest, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/waterloo.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/waterloo.microblog.update.pdf)
- :material-file-search: **Runs:** [waterlooa1](./runs.md#waterlooa1) | [waterlooa2](./runs.md#waterlooa2) | [waterlooa3](./runs.md#waterlooa3) | [waterlooa4](./runs.md#waterlooa4)

??? abstract "Abstract"
	
	For the first year of the Microblog Track, a real time ad hoc search task was determined to be a suitable first task. The goal of the track is to return the most recent but also relevant tweets for a user's query. Participating runs will be officially scored using precision at 30. Other experimental scoring measures will be evaluated in parallel to the official measure. As this was the first year for the Microblog Track, our primary goal was to create a baseline method and then attempt to improve upon the baseline. Since the only task was to perform a real time ad hoc search for the track, we decided that the task would be best suited by using a traditional search methodology. In doing so we used the Wumpus Search Engine1, which was developed by Stefan B¨uttcher while at the University of Waterloo.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoegiestC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoegiestC11,
		author = {Adam Roegiest and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Waterloo at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/waterloo.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoegiestC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2011 Microblog Track

_Cunhui Shi, Kejiang Ren, Hongfei Lin, Shaowu Zhang_

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./participants.md#dutir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/DUTIR.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/DUTIR.microblog.pdf)
- :material-file-search: **Runs:** [dutirLmFb](./runs.md#dutirlmfb) | [dutirMixFb](./runs.md#dutirmixfb) | [dutirTfidfFb](./runs.md#dutirtfidffb) | [dutirMixSp](./runs.md#dutirmixsp)

??? abstract "Abstract"
	
	In TREC 2011 Microblog Track, we explore the use of pseudo relevance feedback to expand original query terms in topics. Hyperlink is used to enhance the performance of the retrieval results. And we set a threshold of entropy to filter retrieval results. Microblog is a Realtime Adhoc Task, so we make use of average querytweettime that comes from pseudo relevance feedback to change retrieval score. We combine two models to improve retrieval results. The results show that our model is effective at realtime relevance retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShiRLZ11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShiRLZ11,
		author = {Cunhui Shi and Kejiang Ren and Hongfei Lin and Shaowu Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/DUTIR.microblog.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ShiRLZ11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### 10 Weeks to TREC: STIRS Siena's Twitter Information Retrieval  System

_Sharon Gower Small, Darren Lim, Karl Appel, Denis Kalic, Matthew Kemmer, David Purcell, Carl Tompkins, Chan Tran_

- :fontawesome-solid-user-group: **Participant:** [SienaCLTeam](./participants.md#sienaclteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/SienaCLTeam.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/SienaCLTeam.microblog.pdf)
- :material-file-search: **Runs:** [SienaCLbase](./runs.md#sienaclbase) | [SienaCL342](./runs.md#sienacl342) | [SienaCL31](./runs.md#sienacl31) | [SienaCL1B](./runs.md#sienacl1b)

??? abstract "Abstract"
	
	There has been an increasing interest, both of the research community and federal funding agencies in microblogs as a source of viable information for a variety of tasks. NIST (National Institute of Standards and Technology) has added a microblog retrieval track to TREC (Text REtrieval Conference) for the first time in 2011. NIST has selected Twitter as the source of microblog data. Twitter is a dynamic social website that allows users to post tweets which are short posts to share news with friends and followers across the world. While some tweets provide useful information, this information is very limited by the restriction on length to 140 characters or less. Participating teams were provided with the code necessary to download the Twitter Corpus, consisting of 16,141,812 tweets from a 2-week time period, January 24, 2011 to February 8, 2011, inclusive. Teams were also provided with a training set of 12 example topics, and later the test set of 50 topics. In this paper, we describe three modules designed for this track, built within a system called STIRS, Siena's Twitter Information Retrieval System. After submitting three user-defined runs and a Lucene baseline run, the NIST judging showed our best run to be at 30.83% precision. The reported median from all runs of all 58 participating teams was 25.9%. We also describe our process of developing a new and complete end-to-end system in just 10 weeks time with six undergraduate researchers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmallLAKKPTT11.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmallLAKKPTT11,
		author = {Sharon Gower Small and Darren Lim and Karl Appel and Denis Kalic and Matthew Kemmer and David Purcell and Carl Tompkins and Chan Tran},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {10 Weeks to {TREC:} {STIRS} Siena's Twitter Information Retrieval System},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/SienaCLTeam.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmallLAKKPTT11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WISTUD at TREC 2011: Microblog Track: Exploiting Background Knowledge  from DBpedia and News Articles for Search on Twitter

_Ke Tao, Fabian Abel, Claudia Hauff_

- :fontawesome-solid-user-group: **Participant:** [wis_tudelft](./participants.md#wis_tudelft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/wis.tudelft.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/wis.tudelft.microblog.update.pdf)
- :material-file-search: **Runs:** [manualWISTUD](./runs.md#manualwistud) | [basicWISTUD](./runs.md#basicwistud) | [dbpWISTUD](./runs.md#dbpwistud) | [mulnewWISTUD](./runs.md#mulnewwistud)

??? abstract "Abstract"
	
	These working notes describe the system developed by the WISTUD team for the Microblog track. We evaluated the suitability of semantic technologies for the search task, in particular, query expansion with named entities that are deduced by means of a topic-based profiling process. The results indicate the feasibility of the approach: for half of the topics, at P@30, our top performing automatic method based on semantic profiling yields better results than the median over all submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TaoAH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/TaoAH11,
		author = {Ke Tao and Fabian Abel and Claudia Hauff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WISTUD} at {TREC} 2011: Microblog Track: Exploiting Background Knowledge from DBpedia and News Articles for Search on Twitter},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/wis.tudelft.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TaoAH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microblog Track 2011 of FDU

_Bingqing Wang, Xuanjing Huang_

- :fontawesome-solid-user-group: **Participant:** [FDUMED](./participants.md#fdumed)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/FDUMED.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/FDUMED.microblog.pdf)
- :material-file-search: **Runs:** [FDUNLP](./runs.md#fdunlp) | [FDUNLP2](./runs.md#fdunlp2)

??? abstract "Abstract"
	
	Twitter provides huge amount of short mes-sages, raises challenge problems to the research community. The Microblog Track of TREC detects the special behavior of the twitter dataset in the 'real-time' retrieval task. This paper reports our participation in the Microblog Track task. Given the query topic-s, each participants are required to conduct a 'real-time' retrieval task, which seeks for the most recent and interesting tweets for each query topic. Our focus in this task includes t-wo aspects: (1)data preprocessing to remove non-English tweets, and (2)feature extraction for clustering the tweets into two categories. Given the huge interest in the microblog, there is lot of work to apply different linguist analysis techniques and data analysis methods to explore the behavior and special features in the Microblog sphere.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangH11,
		author = {Bingqing Wang and Xuanjing Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microblog Track 2011 of {FDU}},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/FDUMED.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring Tweets Normalization and Query Time Sensitivity for Twitter  Search

_Zhongyu Wei, Wei Gao, Lanjun Zhou, Binyang Li, Kam-Fai Wong_

- :fontawesome-solid-user-group: **Participant:** [SEEM_CUHK](./participants.md#seem_cuhk)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/SEEM_CUHK.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/SEEM_CUHK.microblog.update.pdf)
- :material-file-search: **Runs:** [WiseFouthRun](./runs.md#wisefouthrun) | [WiseThirdRun](./runs.md#wisethirdrun) | [Wise2ndRun](./runs.md#wise2ndrun) | [WiseFifthRun](./runs.md#wisefifthrun)

??? abstract "Abstract"
	
	This paper presents our work for the Realtime Adhoc Task of TREC 2011 Microblog Track. Microblog texts like tweets are generally characterized by the inclusion of a large proportion of irregular expressions, such as ill-formed words, which can lead to significant mismatch between query terms and tweets. In addition, Twitter queries are distinguished from Web queries with many unique characteristics, one of which reflects the clearly distinct temporal aspects of Twitter search behavior. In this study, we deal with the first problem by normalizing tweet texts and the second by capturing the temporal characteristics of a topic. We divided topics into two categories: time-sensitive and time-insensitive. For the time-sensitive ones, we introduce a decay factor to adjust the relevance score of results according to the expected date of the topical event to happen, and then re-rank the search results. Experiments demonstrate that our methods are significantly better than baseline and outperform the medium of all runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WeiZLWGWE11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WeiZLWGWE11,
		author = {Zhongyu Wei and Wei Gao and Lanjun Zhou and Binyang Li and Kam{-}Fai Wong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploring Tweets Normalization and Query Time Sensitivity for Twitter Search},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/SEEM\_CUHK.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WeiZLWGWE11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow (UGLA-D) at TREC Microblog 2011: Temporal  Pseudo-Relevance Feedback in Microblog Retrieval

_Stewart Whiting, Iraklis A. Klampanos, Joemon M. Jose_

- :fontawesome-solid-user-group: **Participant:** [UGLA_D](./participants.md#ugla_d)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UGLA-D.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UGLA-D.microblog.update.pdf)
- :material-file-search: **Runs:** [simfoll](./runs.md#simfoll) | [simfollTP01](./runs.md#simfolltp01) | [tfTP01](./runs.md#tftp01)

??? abstract "Abstract"
	
	This submission represents a first attempt to apply temporal pseudo-relevance feedback for the microblog context. For our submission to the TREC Microblogging 2011 track we perform two approaches, which serve as our initial bases for retrieval. Our first approach uses the retrieval facilities of a standard MySQL server on a heuristically altered tweet collection. Our second approach intends to improve on this initial retrieval through pseudo-relevance feedback, based upon the temporal profiles of n-grams extracted from the top N relevance feedback tweets. A weighted graph is used to model temporal correlation between n-grams, with a PageRank variant employed to combine both pseudo-relevant document term distribution and temporal collection evidence. Preliminary experiments with the TREC Microblogging 2011 Twitter corpus indicate that through parameter optimisation, retrieval effectiveness can be improved.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WhitingKJ11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WhitingKJ11,
		author = {Stewart Whiting and Iraklis A. Klampanos and Joemon M. Jose},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow {(UGLA-D)} at {TREC} Microblog 2011: Temporal Pseudo-Relevance Feedback in Microblog Retrieval},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UGLA-D.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WhitingKJ11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Time-Sensitive Weighting for Microblog Retrieval

_Hao Wu, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [Udel_Fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Udel_Fang.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Udel_Fang.microblog.update.pdf)
- :material-file-search: **Runs:** [UDMicroIDF](./runs.md#udmicroidf) | [UDMicroIDFD](./runs.md#udmicroidfd) | [UDMicroComb1](./runs.md#udmicrocomb1) | [UDMicroComb2](./runs.md#udmicrocomb2)

??? abstract "Abstract"
	
	We report our system and experiments for the realtime Adhoc task in the 2011 MicroBlog track. Our goal is to develop effective technique to retrieve relevant tweets that have been posted recently. In particular, we propose a time sensitive term weighting strategy that can favor tweets in hot discussed time and a document length related weighting method that can favor long tweets which are more likely to be interesting. Query expansion technique is also used to further improve the retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuF11a.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuF11a,
		author = {Hao Wu and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Time-Sensitive Weighting for Microblog Retrieval},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Udel\_Fang.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuF11a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### GUCAS at TREC 2011 Microblog Track

_Xin Zhang, Kai Hui, Ben He, Tiejian Luo_

- :fontawesome-solid-user-group: **Participant:** [GUCAS](./participants.md#gucas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/GUCAS.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/GUCAS.microblog.update.pdf)
- :material-file-search: **Runs:** [IDEABASIC](./runs.md#ideabasic) | [IDEABASICQE](./runs.md#ideabasicqe) | [IDEAACTQE](./runs.md#ideaactqe) | [IDEABASICACT](./runs.md#ideabasicact)

??? abstract "Abstract"
	
	The aim of GUCAS's participation in the Microblog track this year is to evaluate the effectiveness of probabilistic retrieval models in combination with various sources of evidence for relevance in the context of the Twitter corpus. In our official runs, we use the PL2F field-based model as the baseline, on top of which query expansion is also applied. In addition, a supplement model combining recency, authority and URL length is developed to retrieve authoritative and timely tweets. Finally, a language filter is used to remove non-English tweets. Our experimental results show that the language filter and URL length filter can benefit the most the retrieval effectiveness. In the following-up experiments, it demonstrates that the results applying the basic models improve siginificantly after removing the retweets in the preliminary results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangHHL11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangHHL11,
		author = {Xin Zhang and Kai Hui and Ben He and Tiejian Luo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{GUCAS} at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/GUCAS.microblog.update.pdf},
		timestamp = {Fri, 27 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangHHL11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2011: Experiments with Terrier in  Crowdsourcing, Microblog, and Web Tracks

_Richard McCreadie, Craig Macdonald, Rodrygo L. T. Santos, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf](http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf)
- :material-file-search: **Runs:** [uogTrUB2](./runs.md#uogtrub2) | [uogTrLqea](./runs.md#uogtrlqea) | [uogTrLqeabdd](./runs.md#uogtrlqeabdd) | [uogTrLqeabd](./runs.md#uogtrlqeabd)

??? abstract "Abstract"
	
	In TREC 2011, we focus on tackling the new challenges proposed by the pilot Crowdsourcing and Microblog tracks, using our Terrier Information Retrieval Platform. Meanwhile, we continue to build upon our novel xQuAD framework and data-driven ranking approaches within Terrier to achieve effective and efficient ranking for the TREC Web track. In particular, the aim of our Microblog track participation is the development of a learning to rank approach for filtering within a tweet ranking environment, where tweets are ranked in reverse chronological order. In the Crowdsourcing track, we work to achieve a closer integration between the crowdsourcing marketplaces that are used for relevance assessment, and Terrier, which produces the document rankings to be assessed. Moreover, we focus on generating relevance assessments quickly and at a minimal cost. For the Web track, we enhance the data-driven learning support within Terrier by proposing a novel framework for the fast computation of document features for learning to rank.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMSO11.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMSO11,
		author = {Richard McCreadie and Craig Macdonald and Rodrygo L. T. Santos and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2011: Experiments with Terrier in Crowdsourcing, Microblog, and Web Tracks},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMSO11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Iowa at TREC 2011: Microblogs, Medical Records  and Crowdsourcing

_Sanmitra Bhattacharya, Christopher G. Harris, Yelena Mejova, Chao Yang, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [UIowaS](./participants.md#uiowas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf)
- :material-file-search: **Runs:** [UIowaS1](./runs.md#uiowas1) | [UIowaS2](./runs.md#uiowas2) | [UIowaS3](./runs.md#uiowas3) | [UIowaS4](./runs.md#uiowas4)

??? abstract "Abstract"
	
	The Text Retrieval and Text Mining group at the University of Iowa participated in three tracks, all new tracks introduced this year: Microblog, Medical Records (Med) and Crowdsourcing. Details of our strategies are provided in this paper. Overall our effort has been fruitful in that we have been able to understand more about the nature of medical records and Twitter messages, and also the merits and challenges of working with games as a framework for gathering relevance judgments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bhattacharya0MYS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bhattacharya0MYS11,
		author = {Sanmitra Bhattacharya and Christopher G. Harris and Yelena Mejova and Chao Yang and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Iowa at {TREC} 2011: Microblogs, Medical Records and Crowdsourcing},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bhattacharya0MYS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

