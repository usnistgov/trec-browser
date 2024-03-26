# Proceedings - Filtering 2000 

#### The TREC-9 Filtering Track Final Report

_Stephen E. Robertson, David A. Hull_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/filtering_new.pdf](http://trec.nist.gov/pubs/trec9/papers/filtering_new.pdf)
??? abstract "Abstract"
	
	The TREC-9 filtering track measures the ability of systems to build persistent user profiles which successfully separate relevant and non-relevant documents. It consists of three major subtasks: adaptive filtering, batch filtering, and routing. In adaptive filtering, the system begins with only a topic statement and a small number of positive examples, and must learn a better profile from on-line feedback. Batch filtering and routing are more traditional machine learning tasks where the system begins with a large sample of evaluated training documents. This report describes the track, presents some evaluation results, and provides a general commentary on lessons learned from this year's track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonH00.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonH00,
		author = {Stephen E. Robertson and David A. Hull},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-9} Filtering Track Final Report},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/filtering\_new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonH00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### YFilter at TREC-9

_Yi Zhang, James P. Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu-lti](./participants.md#cmu-lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/cmu-dirtrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/cmu-dirtrec9.pdf)
- :material-file-search: **Runs:** [CMUDIR11](./runs.md#cmudir11) | [CMUDIR18](./runs.md#cmudir18) | [CMUDIR12](./runs.md#cmudir12) | [CMUDIR13](./runs.md#cmudir13) | [CMUDIR14](./runs.md#cmudir14) | [CMUDIR15](./runs.md#cmudir15) | [CMUDIR16](./runs.md#cmudir16) | [CMUDIR17](./runs.md#cmudir17)

??? abstract "Abstract"
	
	We built a filtering system YFILTER this year, which we used for experiments on profile updating and thresholds setting. Our focus is using incremental Rocchio for introducing new query terms and term weighting. Although 1, 0.5, 0.25 is a widely used Rocchio ratio for query expansion based on relevance feedback, we found that the optimal setting for information filtering is corpus and profile dependent. In addition to a new Rocchio ratio, we tested a modified idf measure for term weighting (ydf) that is biased towards words with middle range term frequency.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangC00.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangC00,
		author = {Yi Zhang and James P. Callan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {YFilter at {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/cmu-dirtrec9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangC00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC-9: CLIR, Filtering and QA Tasks

_Lide Wu, Xuanjing Huang, Yikun Guo, Bingwei Liu, Yuejie Zhang_

- :fontawesome-solid-user-group: **Participant:** [ICDC](./participants.md#icdc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf](http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf)
- :material-file-search: **Runs:** [S2RNsamp](./runs.md#s2rnsamp) | [S2RNr1](./runs.md#s2rnr1) | [S2RNr2](./runs.md#s2rnr2)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC-9 conference for the first time. We have participated in three tracks of CLIR, Filtering and QA. We have submitted four runs for CLIR track. Bilingual knowledge source and statistical-based search engine are integrated in our CLIR system. We varied our strategy somewhat between runs: long query (both title and description field of the queries involved) with pseudo relevance feedback (FDUT9L1), long query with no feedback (FDUT9XL2), median query (just description field of queries involved) with feedback (FDUT9XL3) and, the last, mono long query with feedback (FDUT9XL4). For filtering, we participate in the sub-task of adaptive filtering and batch filtering. Vector representation and computation are heavily applied in filtering procedure. 11 runs of various combination of topic and evaluation measure have been submitted: 4 OHSU runs, 1 MeSH run and 2 MSH-SAMPLE runs for adaptive filtering, and 2 OHSU runs, 1 MeSH run and 1 MSH-SAMPLE run for batch filtering. Our QA system consists of three components: Question Analyzer, Candidate Window Searcher and Answer Extractor. We submitted two runs in the 50-byte category and two runs in the 250-byte category. The runs of 'FDUT9QL1' and 'FDUTIQSI' are extracted from the top 100 candidate windows. The other two runs of 'FDUT9QL2' and 'FDUTIQS1' are extracted from the top 24 candidate windows.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHGLZ00.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHGLZ00,
		author = {Lide Wu and Xuanjing Huang and Yikun Guo and Bingwei Liu and Yuejie Zhang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{FDU} at {TREC-9:} CLIR, Filtering and {QA} Tasks},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHGLZ00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Training Context-Sensitive Neural Networks with Few Relevant Examples  for the TREC-9 Routing

_Mathieu Stricker, Frantz Vichot, Gérard Dreyfus, Francis Wolinski_

- :fontawesome-solid-user-group: **Participant:** [ICDC](./participants.md#icdc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/icdc_final.pdf](http://trec.nist.gov/pubs/trec9/papers/icdc_final.pdf)
- :material-file-search: **Runs:** [S2RNsamp](./runs.md#s2rnsamp) | [S2RNr1](./runs.md#s2rnr1) | [S2RNr2](./runs.md#s2rnr2)

??? abstract "Abstract"
	
	The present paper describes our second participation to the routing task; it features improvements over our previous approach [Stricker et al., 2000]. Our former model used a 'bag of words' for text representation with a feature selection, and a neural network without hidden neuron (i.e. a logistic regression), to estimate the probability of relevance of each document. This approach was close to the ones proposed by [Schütze et al., 1995] or [Wiener et al., 1995] but its original feature was the use of very few relevant features for text representation (25 features per topic on the average for the TREC-8 Routing). In this paper, two main improvements are proposed: The feature selection defines target words for which vectors of local contexts are subsequently defined. These vectors help disambiguate the target words and are defined by an analysis of both the relevant and the irrelevant documents of the training set. This new representation requires large neural networks, which are therefore prone to overfitting. A regularization technique is applied during training to favor smoother network mappings, thereby avoiding overfitting. This was achieved by adding a weight decay term to the usual cost function. This approach led to good results on the MeSH Sample topics (S2RNsamp) and on the OHSUMED topics (S2RNrl and S2RNr2).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StrickerVDW00.bib) "
	```
	@inproceedings{DBLP:conf/trec/StrickerVDW00,
		author = {Mathieu Stricker and Frantz Vichot and G{\'{e}}rard Dreyfus and Francis Wolinski},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Training Context-Sensitive Neural Networks with Few Relevant Examples for the {TREC-9} Routing},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/icdc\_final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StrickerVDW00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC-9: Filtering Track

_Stephen E. Robertson, Steve Walker_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/msrc-fq.pdf](http://trec.nist.gov/pubs/trec9/papers/msrc-fq.pdf)
- :material-file-search: **Runs:** [ok9bf2po](./runs.md#ok9bf2po) | [ok9bfr2po](./runs.md#ok9bfr2po) | [ok9rf2po](./runs.md#ok9rf2po) | [ok9rfr2po](./runs.md#ok9rfr2po) | [ok9f2pm](./runs.md#ok9f2pm) | [ok9f1us](./runs.md#ok9f1us) | [ok9f3us](./runs.md#ok9f3us) | [ok9rfr2ps](./runs.md#ok9rfr2ps) | [ok9bfr2ps](./runs.md#ok9bfr2ps) | [ok9f3uo](./runs.md#ok9f3uo) | [ok9f1uo](./runs.md#ok9f1uo) | [ok9f1po](./runs.md#ok9f1po) | [ok9f2po](./runs.md#ok9f2po)

??? abstract "Abstract"
	
	Apart from a short description of our Query Track contri-bution, this report is concerned with the Adaptive Filtering track only. There is a separate report in this volume [1] on the Microsoft Research Cambridge participation in QA track. A number of runs were submitted for the Adaptive Filtering track, on all tasks (adaptive filtering, batch filtering and routing; three separate query sets; two evaluation measures). The filtering system is somewhat more advanced than the one used for TREC-8, and includes query modification and a more highly developed scheme for threshold adaptation. A number of diagnostic runs are also reported here.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonW00.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonW00,
		author = {Stephen E. Robertson and Steve Walker},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Microsoft Cambridge at {TREC-9:} Filtering Track},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/msrc-fq.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonW00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-9 Experiments at KAIST: QA, CLIR and Batch Filtering

_Kyung-Soon Lee, Jong-Hoon Oh, Jin-Xia Huang, Jae-Ho Kim, Key-Sun Choi_

- :fontawesome-solid-user-group: **Participant:** [KAIST](./participants.md#kaist)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/kaist-trec9-qa-filtering.pdf](http://trec.nist.gov/pubs/trec9/papers/kaist-trec9-qa-filtering.pdf)
- :material-file-search: **Runs:** [KAIST9bfms](./runs.md#kaist9bfms) | [KAIST9bfo1](./runs.md#kaist9bfo1) | [KAIST9bfo2](./runs.md#kaist9bfo2)

??? abstract "Abstract"
	
	In TREC-9, we participated in three tasks: question answering task, cross-language retrieval task, and batch filtering task in the filtering task. Our question answering system consists of following basic components - query analyzer, Named entity tagger, Answer Extractor. First, question analyzer analyzes the given question. Question analyzer generates question type and keywords of the given question. Then retrieved documents are analyzed for extracting relevant answer. POS tagger and Named entity tagger are used for the purpose. Finally, Answer Extractor generates relevant answer. There are four runs in our CLIR, two runs follow the dictionary and MI information based translation approach (KAIST9xlqm, KAIST9xlqt), another one using the mixture result of two commercial Machine Translation systems (KAIST9xImt), and the final one is monolingual run (KAIST9xlch). We translated only query and description fields in all four runs. In batching filtering task, we submitted results for OHSU topics and MSH-SMP topics. For OHSU topics, we have been exploring a filtering technique which combines query zone, support vector machine, and Rocchio's algorithm. For MSH-SMP topics, we use support vector machine simply.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeOHKC00.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeOHKC00,
		author = {Kyung{-}Soon Lee and Jong{-}Hoon Oh and Jin{-}Xia Huang and Jae{-}Ho Kim and Key{-}Sun Choi},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-9} Experiments at {KAIST:} QA, {CLIR} and Batch Filtering},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/kaist-trec9-qa-filtering.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeOHKC00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on the TREC-9 Filtering Track

_Keiichiro Hoashi, Kazunori Matsumoto, Naomi Inoue, Kazuo Hashimoto, Takashi Hasegawa, Katsuhiko Shirai_

- :fontawesome-solid-user-group: **Participant:** [KDD](./participants.md#kdd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/kddtrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/kddtrec9.pdf)
- :material-file-search: **Runs:** [kddaf904](./runs.md#kddaf904) | [kddaf905](./runs.md#kddaf905) | [kddaf906](./runs.md#kddaf906) | [kddaf903](./runs.md#kddaf903)

??? abstract "Abstract"
	
	KDD R&D Laboratories has been participating in previous TREC conferences with the cooperation of students from Waseda University. This year, KDD R&D Laboratories and Waseda University are officially participating as a joint research team. We have focused our experiments for TREC-9 on the adaptive filtering experiments of the Filtering Track. Our goal was to evaluate the filtering method using a non-relevant information profile. We have also made experiments of a new feedback method to increase the accuracy of pseudo feedback. In this paper, we will describe our filtering methods, and present results of our evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HoashiMIHHS00.bib) "
	```
	@inproceedings{DBLP:conf/trec/HoashiMIHHS00,
		author = {Keiichiro Hoashi and Kazunori Matsumoto and Naomi Inoue and Kazuo Hashimoto and Takashi Hasegawa and Katsuhiko Shirai},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments on the {TREC-9} Filtering Track},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/kddtrec9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HoashiMIHHS00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filters and Answers: The University of Iowa TREC-9 Results

_Elena Catona, David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [iowa](./participants.md#iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/iowa.pdf](http://trec.nist.gov/pubs/trec9/papers/iowa.pdf)
- :material-file-search: **Runs:** [IOWAF001](./runs.md#iowaf001) | [IOWAF002](./runs.md#iowaf002) | [IOWAF003](./runs.md#iowaf003)

??? abstract "Abstract"
	
	The University of Iowa participated in the adaptive filtering and question answering tracks of TREC9. The filtering system used was an extension of the one used in TREC-7 [1] and TREC-8 [2]. Question answering was done using a rule-based system that employed a combination of public domain technologies and the SMART retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CatonaES00.bib) "
	```
	@inproceedings{DBLP:conf/trec/CatonaES00,
		author = {Elena Catona and David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Filters and Answers: The University of Iowa {TREC-9} Results},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/iowa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CatonaES00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The System RELIEFS: A New Approach for Information Filtering

_Christophe Brouard, Jian-Yun Nie_

- :fontawesome-solid-user-group: **Participant:** [UMontreal](./participants.md#umontreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/brouard.pdf](http://trec.nist.gov/pubs/trec9/papers/brouard.pdf)
- :material-file-search: **Runs:** [reliefs2](./runs.md#reliefs2) | [reliefs1](./runs.md#reliefs1)

??? abstract "Abstract"
	
	In this year's filtering track, we implemented a system called RELIEFS that tries to learn about the prediction capability of words or conjunctions of words for the relevance of documents. The novelty of the system resides in two main points. First, the features used in the prediction involve both : the implication D->Q (from document to query), and the reverse implication Q->D. This is different from usual approaches where only the first of the implication is used. Therefore, the relevance estimation of a document combines the probability that a document containing a term is relevant, and the reverse probability - the probability that a term appears in relevant documents. The second novelty is that, in addition to the use of words as prediction elements, we also consider word combinations (conjunctions). However, not all combinations are significant. Therefore, an incremental algorithm is developped to select only the meaningful conjunctions. To limit the number of conjunctions, we do not use a cut on conjunction length. Rather, we eliminate the conjunctions A&B that bear the same information as A or as B. Our first results prove the feasibility of the approach. Other experiments are ongoing in order to fully evaluate this approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrouardN00.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrouardN00,
		author = {Christophe Brouard and Jian{-}Yun Nie},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The System {RELIEFS:} {A} New Approach for Information Filtering},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/brouard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BrouardN00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Logical Analysis of Data in the TREC-9 Filtering Track

_Endre Boros, Paul B. Kantor, David J. Neu_

- :fontawesome-solid-user-group: **Participant:** [rutgers-kantor](./participants.md#rutgers-kantor)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/rutgers.pdf](http://trec.nist.gov/pubs/trec9/papers/rutgers.pdf)
- :material-file-search: **Runs:** [antadapt001](./runs.md#antadapt001) | [antadapt002](./runs.md#antadapt002) | [antrpnohsu00](./runs.md#antrpnohsu00) | [antrpohsu00](./runs.md#antrpohsu00) | [antrpnms00](./runs.md#antrpnms00) | [antrpms00](./runs.md#antrpms00)

??? abstract "Abstract"
	
	In the TREC-9 adaptive filtering and routing sub-tasks of the filtering track we continued to explore utilizing the Logical Analysis of Data (LAD) machine learning methodology to develop Boolean expressions that can be utilized as 'rules' for characterizing relevant and irrelevant documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BorosKN00.bib) "
	```
	@inproceedings{DBLP:conf/trec/BorosKN00,
		author = {Endre Boros and Paul B. Kantor and David J. Neu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Logical Analysis of Data in the {TREC-9} Filtering Track},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/rutgers.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BorosKN00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at trec9: Web and Filtering tasks

_M. Abchiche, Mohand Boughanem, Taoufiq Dkaki, Josiane Mothe, Chantal Soulé-Dupuy, Mohamed Tmar_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/irit_trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/irit_trec9.pdf)
- :material-file-search: **Runs:** [Mer9r2](./runs.md#mer9r2) | [mer9b1](./runs.md#mer9b1) | [mer9b2](./runs.md#mer9b2) | [mer9r1](./runs.md#mer9r1)

??? abstract "Abstract"
	
	The tests performed for TREC9 focus on the Web and Filtering (batch and routing) tracks. The submitted runs are based on the Mercure system. For one of the filtering routing runs, we combine Mercure with mining text functionalities from our system Tétralogie. We also performed some experiments taking hyperlinks into account to evaluate their influence on the retrieval effectiveness, but no runs were sent. Web: We submit four runs in this track. Two elements were tested: a modified Mercure term weighting scheme and the notion of the user preference on the retrieved document were tested. Filtering (batch and routing): our main investigation this year concerns the notion of non-relevant profile in a filtering system. The filtering consists on, first filtering the documents using a relevant profile learned from relevant documents, second re-filtering the selected documents using non-relevant profile learned from non-relevant documents so that non-relevant documents accepted by the relevant profile are rejected. This notion of non-relevant profile was introduced by Hoashi [6] in an adaptive system whereas we use this technique for a batch system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbchicheBDMST00.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbchicheBDMST00,
		author = {M. Abchiche and Mohand Boughanem and Taoufiq Dkaki and Josiane Mothe and Chantal Soul{\'{e}}{-}Dupuy and Mohamed Tmar},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure at trec9: Web and Filtering tasks},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/irit\_trec9.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbchicheBDMST00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### kNN at TREC-9

_Tom Ault, Yiming Yang_

- :fontawesome-solid-user-group: **Participant:** [cmu](./participants.md#cmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/cmucat.pdf](http://trec.nist.gov/pubs/trec9/papers/cmucat.pdf)
- :material-file-search: **Runs:** [CMUCAT2](./runs.md#cmucat2) | [CMUCAT3](./runs.md#cmucat3) | [CMUCAT4](./runs.md#cmucat4) | [CMUCAT1](./runs.md#cmucat1) | [CMUCAT5](./runs.md#cmucat5) | [CMUCAT6](./runs.md#cmucat6)

??? abstract "Abstract"
	
	We applied a multi-class k-nearest-neighbor based text classification algorithm to the adaptive and batch filtering problems in the TREC-9 filtering track. While our systems performed well in the batch filtering tasks, they did not perform as well in the adaptive filtering tasks, in part because we did not have an adequate mechanism for taking advantage of the relevance feedback information provided by the filtering tasks. Since TREC-9, we have made considerable improvements in our batch filtering results and discovered some serious problems with both the T9P and T9U metrics. In this paper, we discuss these issues and their impact on our filtering results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AultY00.bib) "
	```
	@inproceedings{DBLP:conf/trec/AultY00,
		author = {Tom Ault and Yiming Yang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {kNN at {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/cmucat.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AultY00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Incrementality, Half-life, and Threshold Optimization for Adaptive  Document Filtering

_Avi Arampatzis, Jean Beney, Cornelis H. A. Koster, Theo P. van der Weide_

- :fontawesome-solid-user-group: **Participant:** [nijmegen](./participants.md#nijmegen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/trec9-kun-final.pdf](http://trec.nist.gov/pubs/trec9/papers/trec9-kun-final.pdf)
- :material-file-search: **Runs:** [KUNr1](./runs.md#kunr1) | [KUNr2](./runs.md#kunr2) | [KUNb](./runs.md#kunb) | [KUNa1T9U](./runs.md#kuna1t9u) | [KUNa1T9P](./runs.md#kuna1t9p) | [KUNa2T9U](./runs.md#kuna2t9u) | [KUNa2T9P](./runs.md#kuna2t9p) | [KUNbaT9U](./runs.md#kunbat9u)

??? abstract "Abstract"
	
	This paper describes the participation by researchers from KUN (the Computing Science Department of the Katholieke Universiteit Nijmegen, The Netherlands) in the TREC-9 Filtering Track. As first-time TREC par-ticipants, our group participated in all three subtasks - adaptive, batch, and routing - while concentrating mainly on adaptive tasks. We have made use of two different systems: FILTERIT, for the adaptive and batch-adaptive' tasks: a pure adaptive filtering system developed in the context of our TREC-9 participation. It is based on the Rocchio algorithm. LOS, for the routing and batch filtering tasks: a multi-classification system based on the Winnow al-gorithm. In adaptive filtering, our contribution has been three-fold. Firstly, we have investigated the value of retrieved documents as training examples in relation to their time of retrieval. For this purpose we have introduced the notion of the half-life of a training document. Secondly, we have introduced a novel statistical threshold selection technique for optimizing linear utility functions. The method can be also applied for optimizing other effectiveness measures as well, however, the resulting equation may have to be solved numerically. Thirdly and most importantly for adaptive long-term tasks, we have developed a system that allows incremental adaptivity. We have tried to minimize the computational and memory requirements of our system without sacrificing its accuracy. In the batch and routing tasks, we have experimented with the use of the Winnow algorithm, including a couple of small improvements. From the two topic-sets given, we have experimented only with the 63 OHSUMED queries. We did not submit any runs on the 4904 MeSH topics; these were simply too many to be processed by our present systems in a reasonable time and space. All experiments were done using a keyword-based representation of documents and queries, with traditional stemming and stoplisting, although our long-term intention is to use phrase representations 2, and apply more sophisticated term selection methods [3]. Table 1 summarizes our official TREC-9 runs. Next, we will briefly describe the pre-processing applied to the data. The FILTERIT and LCS systems are described in Sections 3 and 4, respectively. In Section 5 we give an overall view to how our systems performed in relation to other participants.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ArampatzisBKW00.bib) "
	```
	@inproceedings{DBLP:conf/trec/ArampatzisBKW00,
		author = {Avi Arampatzis and Jean Beney and Cornelis H. A. Koster and Theo P. van der Weide},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Incrementality, Half-life, and Threshold Optimization for Adaptive Document Filtering},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/trec9-kun-final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ArampatzisBKW00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

