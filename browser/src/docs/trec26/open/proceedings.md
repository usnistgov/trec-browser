# Proceedings - OpenSearch 2017 

#### Overview of TREC OpenSearch 2017

_Rolf Jagerman, Krisztian Balog, Philipp Schaer, Johann Schaible, Narges Tavakolpoursaleh, Maarten de Rijke_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-O.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-O.pdf)
??? abstract "Abstract"
	
	In this paper we provide an overview of the TREC 2017 OpenSearch track. The OpenSearch track provides researchers the opportunity to have their retrieval approaches evaluated in a live setting with real users. We focus on the academic search domain with the Social Science Open Access Repository (SSOAR) search engine and report our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JagermanBSSTR17.bib) "
	```
	@inproceedings{DBLP:conf/trec/JagermanBSSTR17,
		author = {Rolf Jagerman and Krisztian Balog and Philipp Schaer and Johann Schaible and Narges Tavakolpoursaleh and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of {TREC} OpenSearch 2017},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JagermanBSSTR17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FEUP at TREC 2017 OpenSearch Track Graph-Based Models for Entity-Oriented

_José Luís Devezas, Carla Teixeira Lopes, Sérgio Nunes_

- :fontawesome-solid-user-group: **Participant:** [FEUP](./participants.md#feup)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/FEUP-O.pdf](https://trec.nist.gov/pubs/trec26/papers/FEUP-O.pdf)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2017 OpenSearch Track, where we explored graph-based approaches for document representation and retrieval. We tackled the problem as an entity-oriented search task over the SSOAR site (Social Science Open Access Repository), using the title and the abstract as a text block and the remaining metadata as a knowledge block. Our main goal for this edition was to compare the graph-of-word, a text-only representation, with the graph-of-entity, a combined data representation that we are working on. The proposal is that, by combining text and knowledge through a unified representation, we will be able to unlock novel weighting strategies capable of harnessing all available information and ultimately improving retrieval effectiveness. Unfortunately, due to a technical problem with the OpenSearch track infrastructure, we were unable to obtain feedback for the real round during August 2017. As an alternative, we were offered the opportunity to participate in a third extraordinary round, happening during October 2017, as well as available feedback from the period between the two official rounds, at the end of July 2017. We obtained an outcome of 0.375 for the graph-of-word and 0.167 for the graph-of-entity, based on only 29 impressions with clicks, out of a total of 4,683 impressions. According to this small number of clicked impressions, both models performed below the site's native search, with graph-of-entity performing below graph-of-word.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DevezasLN17.bib) "
	```
	@inproceedings{DBLP:conf/trec/DevezasLN17,
		author = {Jos{\'{e}} Lu{\'{\i}}s Devezas and Carla Teixeira Lopes and S{\'{e}}rgio Nunes},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{FEUP} at {TREC} 2017 OpenSearch Track Graph-Based Models for Entity-Oriented},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/FEUP-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DevezasLN17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IR-Cologne at TREC 2017 OpenSearch Track: Rerunning Popularity Ranking  Experiments in a Living Lab

_Narges Tavakolpoursaleh, Mandy Neumann, Philipp Schaer_

- :fontawesome-solid-user-group: **Participant:** [IR-Cologne](./participants.md#ir-cologne)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/IR-Cologne-O.pdf](https://trec.nist.gov/pubs/trec26/papers/IR-Cologne-O.pdf)
- :material-file-search: **Runs:** [Gesis](./runs.md#gesis)

??? abstract "Abstract"
	
	In this paper, we will present our work on popularity-based relevance ranking within the SSOAR open access repository system where we reused a popularity data-driven ranking approach. We applied the same normalization method as last year, namely the Characteristic Scores and Scale Method (CSS). Our main focus was to test if we could reproduce the results of last year's track. We, therefore, see this work not as a sole engineering task to produce the best possible popularity ranking method for scientific literature but as a test bed for reproducibility experiments in the domain of living labs. The TREC 2016 OpenSearch track was focused on ad-hoc search for scientific literature and three scientific search engines and document repositories were part of this living lab-centered evaluation campaign: (1) CiteSeerX, (2) Microsoft Academic Search, and (3) SSOAR - Social Science Open Access Repository. From these three only SSOAR remained in this year's OpenSearch track. The first author of this paper is responsible for the implementation of the living lab infrastructure and the LL4IR API that is necessary to include an online system into the OpenSearch evaluation campaign. This work is based on her Master's thesis at University of Bonn [8]. Details of the implementation are described in the two overview papers of the OpenSearch track [1,3].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tavakolpoursaleh17.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tavakolpoursaleh17,
		author = {Narges Tavakolpoursaleh and Mandy Neumann and Philipp Schaer},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {IR-Cologne at {TREC} 2017 OpenSearch Track: Rerunning Popularity Ranking Experiments in a Living Lab},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/IR-Cologne-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tavakolpoursaleh17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at TREC2017 OpenSearch Track

_Peng Xu, Long Bai, Suiyuan Zhang, Fang Yang, Zhibin Zhang, Xiaoming Yu, Xiaolong Jin, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ICTNET-O.pdf](https://trec.nist.gov/pubs/trec26/papers/ICTNET-O.pdf)
- :material-file-search: **Runs:** [ICTNET](./runs.md#ictnet)

??? abstract "Abstract"
	
	The OpenSearch track explores The 'Living Labs' evaluation paradigm for IR that involves real users of operational search engines. The task in the track will continue/expand upon the ad hoc Academic Search task of TREC 2016. It is difficult to define who is better in the ranking experimentation, because the real users in the natural environments search a key word with their own purpose. The best way to evaluate two ranks is let the real users make use of them. So TREC 2017 Open Search Track provides this platform which is a new form to assess the ranks good or bad. The Open Search provide the training queries, testing queries and candidates documents, but it did not tell us which document is more relevant to a specific query which is necessary to train our model. So first we need to crawl the rank of all the documents on each query from an existing web search engine. Then we try a serial of features in order to find the relevance between the queries and the documents. And we also designed scoring rules to give each document a score. Finally, we used XGBoost to train models for each training query and then found a way to predict testing data based on the models. Feedback data is the key to this track. We find a simple way to integrate the feedback into our model. Unfortunately, there is so little feedback that can hardly improve the result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuBZYZYJC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuBZYZYJC17,
		author = {Peng Xu and Long Bai and Suiyuan Zhang and Fang Yang and Zhibin Zhang and Xiaoming Yu and Xiaolong Jin and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at {TREC2017} OpenSearch Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/ICTNET-O.pdf},
		timestamp = {Thu, 13 Jan 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuBZYZYJC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2017: Open Search and Core Tracks

_Matthias Hagen, Yamen Ajjour, Johannes Kiesel, Payam Adineh, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Webis-O-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/Webis-O-CC.pdf)
- :material-file-search: **Runs:** [Webis](./runs.md#webis)

??? abstract "Abstract"
	
	We give a brief overview of the Webis group's participation in the TREC 2017 Open Search and Core tracks. Our submission to the Open Search track is similar to our last year's approach, we axiomatically re-rank a BM25-ordered result list to come up with a final ranking. The axiomatic re-ranking idea is also applied in our Core track contribution but with an emphasis on argumentativeness as a not-yet-covered aspect in retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenAKAS17.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenAKAS17,
		author = {Matthias Hagen and Yamen Ajjour and Johannes Kiesel and Payam Adineh and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2017: Open Search and Core Tracks},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Webis-O-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenAKAS17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

