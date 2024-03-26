# Proceedings - Robust 2005 

#### Overview of the TREC 2005 Robust Retrieval Track

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ROBUST.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec14/papers/ROBUST.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The robust retrieval track explores methods for improving the consistency of retrieval technology by focusing on poorly performing topics. The retrieval task in the track is a traditional ad hoc retrieval task where the evaluation methodology emphasizes a system's least effective topics. The 2005 edition of the track used 50 topics that had been demonstrated to be difficult on one document collection, and ran those topics on a different document collection. Relevance information from the first collection could be exploited in producing a query for the second collection, if desired. The main measure for evaluating system effectiveness is “gmap”, a variant of the traditional MAP measure that uses a geometric mean rather than an arithmetic mean to average individual topic results. As in previous years, the most effective retrieval strategy was to expand queries using terms derived from additional corpora. The relative difficulty of topics differed across the two document sets. Systems were also required to rank the topics by predicted difficulty. This task is motivated by the hope that systems will eventually be able to use such predictions to do topic-specific processing. This remains a challenging task. Since difficulty depends on more then the topic set alone, prediction methods that train on data from other test collections do not generalize well.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees05a.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees05a,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2005 Robust Retrieval Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ROBUST.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees05a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fuzzy Proximity Ranking with Boolean Queries

_Michel Beigbeder, Annabelle Mercier_

- :fontawesome-solid-user-group: **Participant:** [emse.mercier](./participants.md#emse.mercier)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ecole-des-mines.pdf](http://trec.nist.gov/pubs/trec14/papers/ecole-des-mines.pdf)
- :material-file-search: **Runs:** [RIMam05t050](./runs.md#rimam05t050) | [RIMam05t200](./runs.md#rimam05t200) | [RIMam05l050](./runs.md#rimam05l050) | [RIMam05l200](./runs.md#rimam05l200) | [RIMam05d200](./runs.md#rimam05d200)

??? abstract "Abstract"
	
	Based on the idea that the closer the query terms are in a document, the more relevant this document is, we experiment an IR method based on a fuzzy proximity degree of the query term occurences in a document to compute its relevance to the query. Our model is able to deal with Boolean queries, but contrary to the traditional extensions of the basic Boolean IR model, it does not explicitly use a proximity operator. The fuzzy term proximity is controlled with an influence function. Given a query term and a document, the influence function associates to each position in the text a value dependant on the distance of the nearest occurence of this query term. To model proximity, this function is decreasing with distance. Different forms of function can be used: triangular, gaussian etc. For practical reasons only functions with finite support were used. The support of the function is limited by a constant called k. The fuzzy term proximity functions are associated to every leaves of the query tree. Then fuzzy proximities are computed for every nodes with a post-order tree traversal. Given the fuzzy proximities of the sons of a node, its fuzzy proximity is computed, like in the fuzzy IR models, with a mimimum (resp. maximum) combination for conjunctives (resp. disjunctives) nodes. Finally, a fuzzy query proximity value is obtained for each position in this document at the root of the query tree. The score of this document is the integration of the function obtained at the tree root. For the experiments, we modified Lucy (version 0.5.2) to implement our IR model. Three query sets are used for our eight runs. One set is manually built with the title words and some description words. Each of these words is OR'ed with its derivatives like plurals for instance. Then the OR nodes obtained are AND'ed at the tree root. The two automatic query sets are built with an AND of automatically extracted terms from either the title field or the description field. These three query sets are submitted to our system with two values of k: 50 and 200. As our method is aimed at high precision, it sometimes give less than one thousand answers. In such cases, the documents retrieved by the BM-25 method implemented in Lucy was concatenated after our result list.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BeigbederM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BeigbederM05,
		author = {Michel Beigbeder and Annabelle Mercier},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Fuzzy Proximity Ranking with Boolean Queries},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ecole-des-mines.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BeigbederM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass Robust 2005: Using Mixtures of Relevance Models for Query Expansion

_Donald Metzler, Fernando Diaz, Trevor Strohman, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umass-robust.pdf](http://trec.nist.gov/pubs/trec14/papers/umass-robust.pdf)
- :material-file-search: **Runs:** [indri05RdmT](./runs.md#indri05rdmt) | [indri05RdmD](./runs.md#indri05rdmd) | [indri05RdmeD](./runs.md#indri05rdmed) | [indri05RdmeT](./runs.md#indri05rdmet) | [indri05RdmmT](./runs.md#indri05rdmmt)

??? abstract "Abstract"
	
	This paper describes the UMass TREC 2005 Robust Track experiments. We focus on approaches that use term proximity and pseudo-relevance feedback using external collections. Our results indicate both approaches are highly effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MetzlerDSC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MetzlerDSC05,
		author = {Donald Metzler and Fernando Diaz and Trevor Strohman and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass Robust 2005: Using Mixtures of Relevance Models for Query Expansion},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umass-robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MetzlerDSC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Conceptual Indexing Approach for the TREC Robust Task

_Mustapha Baziz, Mohand Boughanem, Nathalie Aussenac-Gilles_

- :fontawesome-solid-user-group: **Participant:** [irit-sig.boughanem](./participants.md#irit-sig.boughanem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/irit.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/irit.robust.pdf)
- :material-file-search: **Runs:** [CKonT](./runs.md#ckont) | [CKonD](./runs.md#ckond) | [CKonTSE](./runs.md#ckontse) | [CKSEonD](./runs.md#ckseond) | [CKSEonTSE](./runs.md#ckseontse)

??? abstract "Abstract"
	
	This paper describes our participation to the TREC 2005 Robust Task. A method of conceptual indexing based on WordNet is used. Both documents and queries are mapped onto WordNet. Thus concepts belonging to WordNet synsets are identified and extracted whereas those having a single sense are expanded.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BazizBA05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BazizBA05,
		author = {Mustapha Baziz and Mohand Boughanem and Nathalie Aussenac{-}Gilles},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Conceptual Indexing Approach for the {TREC} Robust Task},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/irit.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BazizBA05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2005: Terabyte and Robust Track

_Yaniv Bernstein, Bodo Billerbeck, Steven Garcia, Nicholas Lester, Falk Scholer, Justin Zobel, William Webber_

- :fontawesome-solid-user-group: **Participant:** [rmit.scholer](./participants.md#rmit.scholer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/rmit-falk.tera.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/rmit-falk.tera.robust.pdf)
- :material-file-search: **Runs:** [rmit5t1025](./runs.md#rmit5t1025) | [rmit5t0530N](./runs.md#rmit5t0530n) | [rmit5t1545Td](./runs.md#rmit5t1545td) | [rmit5t0000](./runs.md#rmit5t0000) | [rmit5d1025](./runs.md#rmit5d1025)

??? abstract "Abstract"
	
	RMIT University participated in the terabyte and robust tracks in TREC 2005. The terabyte track consists of the three tasks: adhoc retrieval, efficient retrieval, and named page finding. For the adhoc retrieval task we used a language modelling approach based on query likelihood, as well as a new technique aimed at reducing the amount of memory used for ranking documents. For the efficiency task, we submitted results from both a single-machine system and one that was distrubuted among a number of machines, with promising results. The named page task was organised by RMIT University and as a result we repeated last year's experiments, slightly modified, with this year's data. The robust track has two subtasks: adhoc retrieval, and query difficulty prediction. For adhoc retrieval, we employed a standard local analysis query expansion method, sourcing expansion terms for different runs from the collection supplied, from a side corpus, or a combination of both. In one run, we also tested removing duplicate documents from the list of results; in order to predict topic difficulty, we evaluated different document priors of the documents in the result set, in the hope of supplying a more robust set of answers at the cost of returning a potentially smaller number of relevant documents. The second task was to predict query difficulty. To this end, we compared the order of the documents in the result sets to the ordering as determined by document priors. A high similarity in orderings indicated that the query was poor. Two different priors were used. The first was based on document access counts, where each document is given a score that is derived from how likely it is to be ranked by a randomly generated query. The second was directly related to the document size. In this paper we outline our approaches and experiments in both tracks, and discuss our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BernsteinBGLSZW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BernsteinBGLSZW05,
		author = {Yaniv Bernstein and Bodo Billerbeck and Steven Garcia and Nicholas Lester and Falk Scholer and Justin Zobel and William Webber},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2005: Terabyte and Robust Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/rmit-falk.tera.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BernsteinBGLSZW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Looking at Limits and Tradeoffs: Sabir Research at TREC 2005

_Chris Buckley_

- :fontawesome-solid-user-group: **Participant:** [sabir.buckley](./participants.md#sabir.buckley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf)
- :material-file-search: **Runs:** [sab05rot2](./runs.md#sab05rot2) | [sab05rod1](./runs.md#sab05rod1) | [sab05rod2](./runs.md#sab05rod2) | [sab05roa2](./runs.md#sab05roa2) | [sab05ror1](./runs.md#sab05ror1)

??? abstract "Abstract"
	
	Sabir Research participated in TREC-2005 in the Terabyte, Robust, and document retrieval part of the Question Answering tracks. This writeup focuses on the Robust track, and in particular on a “routing” run that took advantage of relevance judgements for the topics on the old trec V45 collection to construct queries for the new Aquaint collection. The s ¯mart retro tool is described which given a query and the set of relevant documents, constructs an optimally weighted version of the query. s ¯mart retro is also used to examine the differences in difficulty between the V45 and Aquaint collections (the Aquaint collection is considerably easier). The final part of the paper describes the compression algorithms and tradeoffs that were used in both TREC 2004 and 2005. These were presented in the TREC 2004 speaker session, but never formally written up. The hardware used for all runs was a single commodity PC with a total cost of $1600: $540 for a Dell PC, $520 for four 250 GByte disks, and $500 to bring the memory up to 2.5 GBytes. The information retrieval software used was the research version of SMART 15.0. SMART was originally developed in the early 1960's by Gerard Salton and since then has continued to be a leading research information retrieval tool. It continues to use a statistical vector space model, with stemming, stop words, weighting, inner product similarity function, and ranked retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Buckley05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Buckley05,
		author = {Chris Buckley},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Looking at Limits and Tradeoffs: Sabir Research at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Buckley05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CAS-ICT at TREC 2005 Robust Track: Using Query Expansion and RankFusion  to Improve Effectiveness and Robustness of Ad Hoc Information Retrieval

_Guodong Ding, Bin Wang, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [cas-ict.wang](./participants.md#cas-ict.wang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-bin.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-bin.robust.pdf)
- :material-file-search: **Runs:** [ICT05qerfTg](./runs.md#ict05qerftg) | [ICT05qerfT](./runs.md#ict05qerft) | [ICT05qerfD](./runs.md#ict05qerfd) | [ICT05qerfDg](./runs.md#ict05qerfdg)

??? abstract "Abstract"
	
	Our participation in this year's robust track aims to: (1) test how to improve the effectiveness of IR (according to MAP) using different retrieval methods with different local analysis-based query expansion methods; (2) test how to improve the retrieval robustness (according to gMAP) using RankFusion, a novel fusion technique proposed in our experiments. Our results show that although query expansion can improve the effectiveness of IR significantly, it hurts the robustness of IR seriously. However, with appropriate parameters setting, using RankFusion for merging multiple retrieval results can improve the robustness significantly while not harming the average precision too much or even increasing it in some cases.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DingWB05.bib) "
	```
	@inproceedings{DBLP:conf/trec/DingWB05,
		author = {Guodong Ding and Bin Wang and Shuo Bai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CAS-ICT} at {TREC} 2005 Robust Track: Using Query Expansion and RankFusion to Improve Effectiveness and Robustness of Ad Hoc Information Retrieval},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/chinese-acad-sci-bin.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DingWB05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Axiomatic Approach to IR–UIUC TREC 2005 Robust Track Experiments

_Hui Fang, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uiuc.zhai](./participants.md#uiuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.robust.pdf)
- :material-file-search: **Runs:** [UIUCrAXd0](./runs.md#uiucraxd0) | [UIUCrAXt1](./runs.md#uiucraxt1) | [UIUCrAXt0](./runs.md#uiucraxt0) | [UIUCrAXt2](./runs.md#uiucraxt2) | [UIUCrAXt3](./runs.md#uiucraxt3)

??? abstract "Abstract"
	
	In this paper, we report our experiments in the TREC 2005 Robust Track. Our focus is to explore the use of a new axiomatic approach to information retrieval. Most existing retrieval models make the assumption that terms are independent of each other. Although such simplifying assumption has facilitated the construction of successful retrieval systems, the assumption is not true; words are related by use, and their similarity of occurrence in documents can reflect underlying semantic relations between terms. Our new method aims at incorporating term dependency relations into the axiomatic retrieval model in a natural way. In this paper, we describe the method and present analysis of our Robust-2005 evaluation results. The results show that the proposed method works equally well as the KL-divergence retrieval model with a mixture model feedback method. The performance can be further improved by using the external resources such as Google.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FangZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/FangZ05,
		author = {Hui Fang and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {An Axiomatic Approach to {IR--UIUC} {TREC} 2005 Robust Track Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FangZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Meiji University HARD and Robust Track Experiments

_Kazuya Kudo, Kenji Imai, Makoto Hashimoto, Tomohiro Takagi_

- :fontawesome-solid-user-group: **Participant:** [meijiu.kakuta](./participants.md#meijiu.kakuta)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/meijiu.hard.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/meijiu.hard.robust.pdf)
- :material-file-search: **Runs:** [MEIJIr2](./runs.md#meijir2)

??? abstract "Abstract"
	
	We participated in HARD Track and Robust Track at TREC2005. Our main challenge is to deal with expansion of a word by recognition of context. In HARD Track, we handled semantic expansion of a word. In Robust Track, we tried a challenge to new approach of “Document expansion” by context recognition. In this paper, the next section presents HARD Track. Section 3 describes Robust Track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KudoIHT05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KudoIHT05,
		author = {Kazuya Kudo and Kenji Imai and Makoto Hashimoto and Tomohiro Takagi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Meiji University {HARD} and Robust Track Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/meijiu.hard.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KudoIHT05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Robust Track Experiments Using PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, Norbert Dinstl, Peter Deng_

- :fontawesome-solid-user-group: **Participant:** [queenscollege.kwok](./participants.md#queenscollege.kwok)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/queensc-kwok.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/queensc-kwok.robust.pdf)
- :material-file-search: **Runs:** [pircRB05t3](./runs.md#pircrb05t3) | [pircRB05d1](./runs.md#pircrb05d1) | [pircRB05d3](./runs.md#pircrb05d3) | [pircRB05td3](./runs.md#pircrb05td3) | [pircRB05t2](./runs.md#pircrb05t2)

??? abstract "Abstract"
	
	The two tasks in the TREC2005 Robust track were as follows: given a set of topics, A) predict their ranking according to average precision; and B) improve the effectiveness of their ad hoc retrieval, in particular the weakest topics and if possible with the help of what has been found in task A. The difference from last year is that the test collection (ACQUAINT) is different from the training collection (from TREC2004). The evaluation measures for these tasks have also changed from TREC2004. For task A, it is the difference in area (diff-area) between the observed and the predicted MAP plots when the worst performing topic is successively removed from the set. For task B, it is the GMAP, which is roughly the geometric mean of the average precision of all topics (Voorhees 2005). We do not believe our techniques for predicting topic average precision is sufficiently accurate to be applied to task B, and treat the two tasks independently. For task A, two methods of predicting topic behavior were tried: i) predicting the weakest and strongest n topics by SVM regression; and ii) ranking topics by retrieved document similarity. For task B, we followed the strategy introduced by us before to improve ad-hoc retrieval via the web as an external thesaurus to supplement a given topic's representation, followed with data fusion. A new method of salient term selection from longer description queries based on SVM classification was employed to define web probes for these queries. Five runs were submitted: two for title (pircRB05t2 and -t3), two for description queries (pircRB05d1 and -d3), and one for the combination of the two (pircRB05td3). Section 2 describes our experiments for topic prediction; section 3 describes our weak query effectiveness improvements; and section 4 has our conclusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGDD05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGDD05,
		author = {Kui{-}Lam Kwok and Laszlo Grunfeld and Norbert Dinstl and Peter Deng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Robust Track Experiments Using {PIRCS}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/queensc-kwok.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGDD05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC 2005: Robust Track

_Shuang Liu, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [uillinois-chicago.liu](./participants.md#uillinois-chicago.liu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uillinois-chicago.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/uillinois-chicago.robust.pdf)
- :material-file-search: **Runs:** [uic0501](./runs.md#uic0501)

??? abstract "Abstract"
	
	This paper presents a new approach to improve retrieval effectiveness by using concepts, examples, and word sense disambiguation. We also employ pseudo-feedback and web-assisted feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuY05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuY05,
		author = {Shuang Liu and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC} 2005: Robust Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uillinois-chicago.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuY05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2005: QA Retrieval and Robust Tracks

_James Mayfield, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [jhu.mayfield](./participants.md#jhu.mayfield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/jhu-apl.mayfield.qa.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/jhu-apl.mayfield.qa.robust.pdf)
- :material-file-search: **Runs:** [apl05pd](./runs.md#apl05pd) | [apl05cmb](./runs.md#apl05cmb) | [apl05prf](./runs.md#apl05prf) | [apl05pt](./runs.md#apl05pt) | [apl05p50](./runs.md#apl05p50)

??? abstract "Abstract"
	
	The Johns Hopkins University Applied Physics Laboratory (JHU/APL) focused on the Robust and Question Answering Information Retrieval (QAIR) Tracks at the 2005 TREC conference. For the Robust Track, we attempted to use the difference in retrieval scores between the top retrieved and the 100th document to predict performance; the result was not competitive. For QAIR, we augmented each query with terms that appeared frequently in documents that contained answers to questions from previous question sets; the results showed modest gains from the technique.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MayfieldM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MayfieldM05,
		author = {James Mayfield and Paul McNamee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{JHU/APL} at {TREC} 2005: {QA} Retrieval and Robust Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/jhu-apl.mayfield.qa.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MayfieldM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Building on Redundancy: Factoid Question Answering, Robust Retrieval  and the "Other"

_Dmitri Roussinov, Elena Filatova, Michael Chau, Jose Antonio Robles-Flores_

- :fontawesome-solid-user-group: **Participant:** [arizonau.roussinov](./participants.md#arizonau.roussinov)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/arizonasu.qa.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/arizonasu.qa.robust.pdf)
- :material-file-search: **Runs:** [ASUDIV](./runs.md#asudiv) | [ASUBE](./runs.md#asube) | [ASUDE](./runs.md#asude) | [ASUTI](./runs.md#asuti) | [ASUBE3](./runs.md#asube3)

??? abstract "Abstract"
	
	We have explored how redundancy based techniques can be used in improving factoid question answering, definitional questions (“other”), and robust retrieval. For the factoids, we explored the meta approach: we submit the questions to the several open domain question answering systems available on the Web and applied our redundancy-based triangulation algorithm to analyze their outputs in order to identify the most promising answers. Our results support the added value of the meta approach: the performance of the combined system surpassed the underlying performances of its components. To answer definitional (“other”) questions, we were looking for the sentences containing re-occurring pairs of noun entities containing the elements of the target. For robust retrieval, we applied our redundancy based Internet mining technique to identify the concepts (single word terms or phrases) that were highly related to the topic (query) and expanded the queries with them. All our results are above the mean performance in the categories in which we have participated, with one of our robust runs being the best in its category among all 24 participants. Overall, our findings support the hypothesis that using as much as possible textual data, specifically such as mined from the World Wide Web, is extre mely promising.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoussinovFCR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoussinovFCR05,
		author = {Dmitri Roussinov and Elena Filatova and Michael Chau and Jose Antonio Robles{-}Flores},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Building on Redundancy: Factoid Question Answering, Robust Retrieval and the "Other"},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/arizonasu.qa.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoussinovFCR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Enterprise, QA, Robust and Terabyte Experiments with Hummingbird SearchServer  at TREC 2005

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf)
- :material-file-search: **Runs:** [humR05tl](./runs.md#humr05tl) | [humR05txl](./runs.md#humr05txl) | [humR05txle](./runs.md#humr05txle) | [humR05dl](./runs.md#humr05dl) | [humR05dle](./runs.md#humr05dle)

??? abstract "Abstract"
	
	Hummingbird participated in 6 tasks of TREC 2005: the email known-item search task of the Enterprise Track, the document ranking task of the Question Answering Track, the ad hoc topic relevance task of the Robust Retrieval Track, and the adhoc, efficiency and named page finding tasks of the Terabyte Track. In the email known-item task, SearchServer found the desired message in the first 10 rows for more than 80% of the 125 queries. In the document ranking task, SearchServer returned an answering document in the first 10 rows for more than 90% of the 50 questions. In the robustness task, SearchServer found a relevant document in the first 10 rows for 88% of the 50 short (title) topics. In the terabyte adhoc and efficiency tasks, SearchServer found a relevant document in the first 10 rows for more than 90% of the 50 title topics. A new retrieval measure, First Relevant Score, is investigated; it is found to more accurately reflect known-item differences than reciprocal rank and to better reflect robustness across topics than the primary measure of the Robust track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson05,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Enterprise, QA, Robust and Terabyte Experiments with Hummingbird SearchServer at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MATRIX at the TREC 2005 Robust Track

_W. S. Wong, Ho Chung Wu, Robert Wing Pong Luk, Hong Va Leong, Kam-Fai Wong, Kui-Lam Kwok_

- :fontawesome-solid-user-group: **Participant:** [hkpu.luk](./participants.md#hkpu.luk)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/hkpu.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/hkpu.robust.pdf)
- :material-file-search: **Runs:** [HKPU2CT](./runs.md#hkpu2ct) | [HKPU2CTDN](./runs.md#hkpu2ctdn) | [HKPUVCTDN](./runs.md#hkpuvctdn) | [HKPUCD](./runs.md#hkpucd) | [HKPUVCT](./runs.md#hkpuvct)

??? abstract "Abstract"
	
	In the TREC 2005 robust retrieval track, we tested our adaptive retrieval model that automatically switches between the 2-Poisson model/adaptive vector space model and our initial predictive probabilistic context-based model depending on some query characteristics. Our 2-Poisson model uses the BM11 term weighting scheme with passage retrieval and pseudo-relevance feedback. The context-based model incorporates the term locations in a document for calculating the term weights. By doing this, different term weights are assigned to the same query term depending on its context and location in the document. We also use WordNet in the term selection process when doing pseudo-relevance feedback. The performance of our model is comparable to the median among all participants in the robust track on the whole query set including the title, descriptive and long queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WongWLLWK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WongWLLWK05,
		author = {W. S. Wong and Ho Chung Wu and Robert Wing Pong Luk and Hong Va Leong and Kam{-}Fai Wong and Kui{-}Lam Kwok},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{MATRIX} at the {TREC} 2005 Robust Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/hkpu.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WongWLLWK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Queensland University of Technology at TREC 2005

_Alan Woodley, Chengye Lu, Tony Sahama, John King, Shlomo Geva_

- :fontawesome-solid-user-group: **Participant:** [queenslandu.geva](./participants.md#queenslandu.geva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/queenslandu.tera.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/queenslandu.tera.robust.pdf)
- :material-file-search: **Runs:** [pstitle01](./runs.md#pstitle01) | [pstopic01](./runs.md#pstopic01) | [topic01](./runs.md#topic01) | [title01](./runs.md#title01)

??? abstract "Abstract"
	
	The Information Retrieval and Web Intelligence (IR-WI) research group is a research team at the Faculty of Information Technology, QUT, Brisbane, Australia. The IR-WI group participated in the Terabyte and Robust track at TREC 2005, both for the first time. For the Robust track we applied our existing information retrieval system that was originally designed for use with structured (XML) retrieval to the domain of document retrieval. For the Terabyte track we experimented with an open source IR system, Zettair and performed two types of experiments. First, we compared Zettair's performance on both a high-powered supercomputer and a distributed system across seven midrange personal computers. Second, we compared Zettair's performance when a standard TREC title is used, compared with a natural language query, and a query expanded with synonyms. We compare the systems both in terms of efficiency and retrieval performance. Our results indicate that the distributed system is faster than the supercomputer, while slightly decreasing retrieval performance, and that natural language queries also slightly decrease retrieval performance, while our query expansion technique significantly decreased performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WoodleyLSKG05.bib) "
	```
	@inproceedings{DBLP:conf/trec/WoodleyLSKG05,
		author = {Alan Woodley and Chengye Lu and Tony Sahama and John King and Shlomo Geva},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Queensland University of Technology at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/queenslandu.tera.robust.pdf},
		timestamp = {Wed, 14 Jun 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WoodleyLSKG05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2005 HARD, Robust, and SPAM Tracks

_Kiduk Yang, Ning Yu, Nicholas George, Aaron Loehrlein, David McCaulay, Hui Zhang, Shahrier Akram, Jue Mei, Ivan Record_

- :fontawesome-solid-user-group: **Participant:** [indianau.yang](./participants.md#indianau.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf](http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf)
- :material-file-search: **Runs:** [wdf1tbqf](./runs.md#wdf1tbqf) | [wdf1t10q](./runs.md#wdf1t10q) | [wdf1t3qs0](./runs.md#wdf1t3qs0) | [wdf1t3qd](./runs.md#wdf1t3qd) | [wdf1s1wp1sm](./runs.md#wdf1s1wp1sm)

??? abstract "Abstract"
	
	Web Information Discovery Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science participated in the HARD, Robust, and SPAM tracks in TREC-2005. The basic approach of WIDIT is to combine multiple methods as well as to leverage multiple sources of evidence. Our main strategies for the tracks were: query expansion and fusion optimization for the HARD and Robust tracks; and combination of probabilistic, rule-based, pattern-based, and blacklist email filters for the SPAM track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYGLMZAMR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYGLMZAMR05,
		author = {Kiduk Yang and Ning Yu and Nicholas George and Aaron Loehrlein and David McCaulay and Hui Zhang and Shahrier Akram and Jue Mei and Ivan Record},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2005 HARD, Robust, and {SPAM} Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/indianau-bloom.hard.robust.spam.pdf},
		timestamp = {Wed, 29 Jun 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangYGLMZAMR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Juru at TREC 2005: Query Prediction in the Terabyte and the Robust  Tracks

_Elad Yom-Tov, David Carmel, Adam Darlow, Dan Pelleg, Shai Errera-Yaakov, Shai Fine_

- :fontawesome-solid-user-group: **Participant:** [ibm-haifa.carmel](./participants.md#ibm-haifa.carmel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ibm-haifa.tera.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/ibm-haifa.tera.robust.pdf)
- :material-file-search: **Runs:** [juruManTit](./runs.md#jurumantit) | [JuruTDWE](./runs.md#jurutdwe) | [JuruDWE](./runs.md#jurudwe) | [JuruTiWE](./runs.md#jurutiwe)

??? abstract "Abstract"
	
	Our experiments focus this year on the ad-hock tasks of the Terabyte and the Robust tracks. In both tracks we experimented with the query prediction technology we developed recently. In the Terabyte track, we investigated how query prediction can be used to improve federation of search results extracted from several indices. We show that federated search based on query prediction can achieve comparable results to single-index search. In the Robust track we trained a predictor over one collection (TREC-8) for predicting query difficulty over another collection (AQUAINT). The experimental results show that difficult topics on the TREC-8 collection were not found to be consistently difficult on the AQUAINT collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yom-TovCDPEF05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yom-TovCDPEF05,
		author = {Elad Yom{-}Tov and David Carmel and Adam Darlow and Dan Pelleg and Shai Errera{-}Yaakov and Shai Fine},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Juru at {TREC} 2005: Query Prediction in the Terabyte and the Robust Tracks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ibm-haifa.tera.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Yom-TovCDPEF05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

