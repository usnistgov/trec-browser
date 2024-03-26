# Proceedings - Session 2013 

#### Overview of the TREC 2013 Session Track

_Ben Carterette, Ashraf Bah, Evangelos Kanoulas, Mark M. Hall, Paul D. Clough_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/SESSION.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/SESSION.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Session track ran for the fourth time in 2013. The track has the primary goal of providing test collections and evaluation measures for studying information retrieval over user sessions rather than one-time queries. These test collections are meant to be portable, reusable, statistically powerful, and open to anyone that wishes to work on the problem of retrieval over sessions. The experimental design of the track was similar to that of the previous two years [4, 5]: sessions were real user sessions with a search engine that include queries, retrieved results, clicks, and dwell times; retrieval tasks were designed to study the effect of using session data in retrieval for only the mth query in a session. Changes from last year's track include: 1. a new set of topics; 2. a new corpus (ClueWeb12); 3. a new search system for collecting session data; 4. a small change in the retrieval tasks. This overview is organized as follows: in Section 2 we describe the tasks participants were to perform. In Section 3 we describe the corpus, topics, and sessions that comprise the test collection. Section 4 gives some information about submitted runs. In Section 5 we describe relevance judging and evaluation measures, and Sections 6 present evaluation results and analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarteretteBKHC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarteretteBKHC13,
		author = {Ben Carterette and Ashraf Bah and Evangelos Kanoulas and Mark M. Hall and Paul D. Clough},
		editor = {Ellen M. Voorhees},
		title = {Overview of the {TREC} 2013 Session Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/SESSION.OVERVIEW.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarteretteBKHC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Session Track TREC 2013

_Zhenhong Chen, Long Xia, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/ICTNET-session.pdf](http://trec.nist.gov/pubs/trec22/papers/ICTNET-session.pdf)
- :material-file-search: **Runs:** [ICTNET13SER1.RL1](./runs.md#ictnet13ser1.rl1) | [ICTNET13SER1.RL2](./runs.md#ictnet13ser1.rl2) | [ICTNET13SER1.RL3](./runs.md#ictnet13ser1.rl3) | [ICTNET13SER2.RL1](./runs.md#ictnet13ser2.rl1) | [ICTNET13SER2.RL2](./runs.md#ictnet13ser2.rl2) | [ICTNET13SER2.RL3](./runs.md#ictnet13ser2.rl3) | [ICTNET13SER3.RL1](./runs.md#ictnet13ser3.rl1) | [ICTNET13SER3.RL2](./runs.md#ictnet13ser3.rl2) | [ICTNET13SER3.RL3](./runs.md#ictnet13ser3.rl3)

??? abstract "Abstract"
	
	In this paper, we describe our solutions to the Session Track at TREC 2013. There are three main differences compared to our last year's submission[2]. Firstly, we use Indri[3] to build our retrieval system. Due to computing resource limited, we only index the Category B collection. Secondly, we try to take advantage of FreeBase[4] to recognize the entities in the given query and then weight each term or phrase accordingly. Lastly, we discard the Google virtual document and page rank features from our last year's learning to rank model. The rest of this paper is organized as follows.We detail our research structure in section 2. Section 3 describes our experiments and evaluation results. Conclusions are made in the last section.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenXYLC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenXYLC13,
		author = {Zhenhong Chen and Long Xia and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees},
		title = {{ICTNET} at Session Track {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/ICTNET-session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenXYLC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pitt at TREC 2013: Different Effects of Click-through and Past Queries  on Whole-session Search Performance

_Jiepu Jiang, Daqing He_

- :fontawesome-solid-user-group: **Participant:** [PITT](./participants.md#pitt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/pitt-session.pdf](http://trec.nist.gov/pubs/trec22/papers/pitt-session.pdf)
- :material-file-search: **Runs:** [FixInt28.RL1](./runs.md#fixint28.rl1) | [FixInt28.RL2](./runs.md#fixint28.rl2) | [FixInt28.RL3](./runs.md#fixint28.rl3) | [FixInt28N.RL1](./runs.md#fixint28n.rl1) | [FixInt28N.RL2](./runs.md#fixint28n.rl2) | [FixInt28N.RL3](./runs.md#fixint28n.rl3) | [FixInt58.RL1](./runs.md#fixint58.rl1) | [FixInt58.RL2](./runs.md#fixint58.rl2) | [FixInt58.RL3](./runs.md#fixint58.rl3) | [FixInt58N.RL1](./runs.md#fixint58n.rl1) | [FixInt58N.RL2](./runs.md#fixint58n.rl2) | [FixInt58N.RL3](./runs.md#fixint58n.rl3) | [KM1.RL1](./runs.md#km1.rl1) | [KM1.RL2](./runs.md#km1.rl2) | [KM1.RL3](./runs.md#km1.rl3) | [KM1N.RL1](./runs.md#km1n.rl1) | [KM1N.RL2](./runs.md#km1n.rl2) | [KM1N.RL3](./runs.md#km1n.rl3)

??? abstract "Abstract"
	
	Past search queries and click-through information within a search session have been heavily exploited to improve search performance. However, it remains unclear how do these two data source contribute to whole-session search performance due to the lack of reliable evaluation approaches. For example, as pointed out in our last year's report [2], using past search queries as positive relevance feedback information can make search results of the current query similar to previous queries' results. Such issues cannot be disclosed by evaluation metrics such as nDCG@10. Therefore, in this paper, we focus on analyzing the effects of past queries and click-through information on whole-session search performance. We adopted alternative evaluation approaches other than the TREC official ones. We found that past queries may seemingly enhance nDCG@10 by retrieving previously returned results, which is difficult to result in real improvements of whole-session search performance; in comparison, click-through can enhance search performance without sacrificing search novelty, consequently leading to improved search performance across the whole session. However, after appropriate demotion of repeated results, both past queries and click-through can improve search performance while balancing novelty of results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangH13a.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangH13a,
		author = {Jiepu Jiang and Daqing He},
		editor = {Ellen M. Voorhees},
		title = {Pitt at {TREC} 2013: Different Effects of Click-through and Past Queries on Whole-session Search Performance},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/pitt-session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangH13a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Applying the Query Change Retrieval Model on Session Search-Georgetown  at TREC 2013 Session Track

_Sicong Zhang, Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [GeorgetownYang](./participants.md#georgetownyang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/georgetown-session.pdf](http://trec.nist.gov/pubs/trec22/papers/georgetown-session.pdf)
- :material-file-search: **Runs:** [GUrun1.RL1](./runs.md#gurun1.rl1) | [GUrun1.RL2](./runs.md#gurun1.rl2) | [GUrun1.RL3](./runs.md#gurun1.rl3) | [GUrun3.RL1](./runs.md#gurun3.rl1) | [GUrun3.RL2](./runs.md#gurun3.rl2) | [GUrun3.RL3](./runs.md#gurun3.rl3) | [GUrun2.RL1](./runs.md#gurun2.rl1) | [GUrun2.RL2](./runs.md#gurun2.rl2) | [GUrun2.RL3](./runs.md#gurun2.rl3)

??? abstract "Abstract"
	
	In TREC 2013 Session Track, we experiment the Query Change Model (QCM) for session search on the new document collection ClueWeb12 CatB. We use structured query formulation and pseudo-relevance feedback for RL1. The QCM approach is used in RL2 and it studies query change between adjacent queries and models session search as a Markov Decision Process. We further add information from other sessions by a majority vote of cross-session clicked data to the model in RL3. Comparing the retrieval accuracy in RL1 with that in RL2 and RL3, we obtain 46.1% and 46.6% improvements, respectively. We present an analysis and discussion on the dataset difference between ClueWeb12 Cat A and Cat B, the difference between TREC2012 and TREC2013 session, and their impact on the retrieval accuracy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangY13.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangY13,
		author = {Sicong Zhang and Hui Yang},
		editor = {Ellen M. Voorhees},
		title = {Applying the Query Change Retrieval Model on Session Search-Georgetown at {TREC} 2013 Session Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/georgetown-session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangY13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2013-Session and Web Track

_Matthias Hagen, Michael Völske, Jakob Gomoll, Marie Bornemann, Lene Ganschow, Florian Kneist, Abdul Hamid Sabri, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/webis-session-web.pdf](http://trec.nist.gov/pubs/trec22/papers/webis-session-web.pdf)
- :material-file-search: **Runs:** [webisS1.RL1](./runs.md#webiss1.rl1) | [webisS1.RL2](./runs.md#webiss1.rl2) | [webisS1.RL3](./runs.md#webiss1.rl3) | [webisS2.RL1](./runs.md#webiss2.rl1) | [webisS2.RL2](./runs.md#webiss2.rl2) | [webisS2.RL3](./runs.md#webiss2.rl3) | [webisS3.RL1](./runs.md#webiss3.rl1) | [webisS3.RL2](./runs.md#webiss3.rl2) | [webisS3.RL3](./runs.md#webiss3.rl3)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2013 Session and Web tracks. All our runs are on the full ClueWeb12 and use the online Indri retrieval system hosted at CMU. As for the session track, our runs implement three main ideas that were slightly improved compared to our participation in 2012: (1) distinguishing low risk sessions where we want to involve session knowledge in the form of a conservative query expansion strategy (only few expansion terms based on keywords from previous queries and seen/clicked documents/titles/snippets) from those where we don't, (2) conservative query expansion based on similar sessions from other users, (3) result list postprocessing to boost clicked documents of other users in similar sessions. As these techniques leave a lot of queries unchanged when not enough session knowledge is available, we do not expect large gains over all the sessions. As for the Web track, our runs exploit different strategies of segmenting the queries (i.e., identifying and highlighting concepts within the query as phrases to be contained in the results). Additionally to algorithmic segmentations based on our WWW 2011 and CIKM 2012 ideas, we had one run where we chose the segmentation according to a majority vote amongst five humans. In a last run, the results are constructed so as to be disjunct from the track's baseline's and our other runs' results. Instead, we populate the result list with documents that different segmentations of the query would return top-ranked or that are deeper in the ranking for segmentations already chosen in previous runs. The underlying idea was to obtain at least some judgments for the top documents that other segmentations would bring up in their rankings. As most of the queries are rather short, we expect only slight improvements or no effect at all from the different segmentation strategies that are tailored to longer and more verbose queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenVGBGKSS13.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenVGBGKSS13,
		author = {Matthias Hagen and Michael V{\"{o}}lske and Jakob Gomoll and Marie Bornemann and Lene Ganschow and Florian Kneist and Abdul Hamid Sabri and Benno Stein},
		editor = {Ellen M. Voorhees},
		title = {Webis at {TREC} 2013-Session and Web Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/webis-session-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenVGBGKSS13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

