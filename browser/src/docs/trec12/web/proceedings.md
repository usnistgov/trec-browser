# Proceedings - Web 2003 

#### Overview of the TREC 2003 Web Track

_Nick Craswell, David Hawking, Ross Wilkinson, Mingfang Wu_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/WEB.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec12/papers/WEB.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC 2003 web track consisted of both a non-interactive stream and an interactive stream. Both streams worked with the .GOV test collection. The non-interactive stream continued an investigation into the importance of homepages in Web ranking, via both a Topic Distillation task and a Navigational task. In the topic distillation task, systems were expected to return a list of the homepages of sites relevant to each of a series of broad queries. This differs from previous homepage experiments in that queries may have multiple correct answers. The navigational task required systems to return a particular desired web page as early as possible in the ranking in response to queries. In half of the queries, the target answer was the homepage of a site and the query was derived from the name of the site (Homepage finding) while in the other half, the target answers were not homepages and the queries were derived from the name of the page (Named page finding). The two types of query were arbitrarily mixed and not identified. The interactive stream focused on human participation in a topic distillation task over the .GOV collection. Studies conducted by the two participating groups compared a search engine using au- tomatic topic distillation features with the same engine with those features disabled in order to determine whether the automatic topic distillation features assisted the users in the performance of their tasks and whether humans could achieve better results than the automatic system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellHWW03.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellHWW03,
		author = {Nick Craswell and David Hawking and Ross Wilkinson and Mingfang Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2003 Web Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {78--92},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/WEB.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellHWW03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2003 Experiments Using Web Topic-Centric Link  Analysis

_Paricha Ingongngam, Arnon Rungsawang_

- :fontawesome-solid-user-group: **Participant:** [kasetsartu](./participants.md#kasetsartu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/kasetsartu.pdf](http://trec.nist.gov/pubs/trec12/papers/kasetsartu.pdf)
- :material-file-search: **Runs:** [KUCONTENT](./runs.md#kucontent)

??? abstract "Abstract"
	
	In TREC 2003, our experiments have been concentrated only on the topic distillation task. We first simply apply the term-based technique to the .GOV web collection, and then re-rank the retrieval results using a link analysis algorithm in order to boost the retrieval precision. Our link analysis has been inspired from the original PageRank, but focused on the web topic during the iterative score propagation. We hybridize the term-based retrieval scores with our link analysis approach. From the experiments, the results show that the combination of those scores still provides inadequate precision improvement.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/IngongngamR03.bib) "
	```
	@inproceedings{DBLP:conf/trec/IngongngamR03,
		author = {Paricha Ingongngam and Arnon Rungsawang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2003 Experiments Using Web Topic-Centric Link Analysis},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {363--367},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/kasetsartu.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/IngongngamR03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fondazione Ugo Bordoni at TREC 2003: Robust and Web Track

_Giambattista Amati, Claudio Carpineto, Giovanni Romano_

- :fontawesome-solid-user-group: **Participant:** [fub.carpineto](./participants.md#fub.carpineto)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/fub.robust.web.pdf](http://trec.nist.gov/pubs/trec12/papers/fub.robust.web.pdf)
- :material-file-search: **Runs:** [fub03IneBMt](./runs.md#fub03inebmt) | [fub03IneBBt](./runs.md#fub03inebbt) | [fub03InLBt](./runs.md#fub03inlbt) | [fub03InLBo1t](./runs.md#fub03inlbo1t) | [fub03InBMt](./runs.md#fub03inbmt)

??? abstract "Abstract"
	
	Our participation in TREC 2003 aims to adapt the use of the DFR (Divergence From Randomness) models with Query Expansion (QE) to the robust track and the topic distillation task of the Web track. We focus on the robust track, where the utilization of QE improves the global performance but hurts the performance on the worst topics. In partic- ular, we study the problem of the selective application of the query expansion. We define two information theory based functions, InfoDFR and InfoQ, predicting respectively the AP (Average Precision) of queries and the AP increment of queries after the application of QE. InfoQ is used to selectively apply QE. We show that the use of InfoQ achieves the same performance comparable of the unexpanded method on the set of the worst topics, but a better performance than full QE on the entire set of topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmatiCR03.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmatiCR03,
		author = {Giambattista Amati and Claudio Carpineto and Giovanni Romano},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Fondazione Ugo Bordoni at {TREC} 2003: Robust and Web Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {234--245},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/fub.robust.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmatiCR03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Juru at TREC 2003 - Topic Distillation using Query-Sensitive Tuning  and Cohesiveness Filtering

_Einat Amitay, David Carmel, Adam Darlow, Michael Herscovici, Ronny Lempel, Aya Soffer, Reiner Kraft, Jason Y. Zien_

- :fontawesome-solid-user-group: **Participant:** [ibmhaifa.carmel](./participants.md#ibmhaifa.carmel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ibm-haifa.web.pdf](http://trec.nist.gov/pubs/trec12/papers/ibm-haifa.web.pdf)
- :material-file-search: **Runs:** [JuruFull](./runs.md#jurufull) | [JuruNoAnchor](./runs.md#jurunoanchor) | [JuruNoSS](./runs.md#jurunoss) | [JuruNoCohes](./runs.md#jurunocohes) | [JuruNoQDiff](./runs.md#jurunoqdiff)

??? abstract "Abstract"
	
	This is the third year that our group participates in TREC's Web track, the second year in the topic distillation task. Our experiments last year, as well as those of other participants, indicated that sophisticated link-based measures did not significantly improve search results in comparison to standard text-based relevance scoring. We thus focused our experiments this year on improving the ranking algorithms of our core search engine, Juru, and on developing measures that are good indicators of topical pages. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmitayCDHLSKZ03.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmitayCDHLSKZ03,
		author = {Einat Amitay and David Carmel and Adam Darlow and Michael Herscovici and Ronny Lempel and Aya Soffer and Reiner Kraft and Jason Y. Zien},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Juru at {TREC} 2003 - Topic Distillation using Query-Sensitive Tuning and Cohesiveness Filtering},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {276--282},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ibm-haifa.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmitayCDHLSKZ03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Robust and Web Retrieval with Document-Centric Integral Impacts

_Vo Ngoc Anh, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [umelbourne.moffat](./participants.md#umelbourne.moffat)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umelbourne.web.pdf](http://trec.nist.gov/pubs/trec12/papers/umelbourne.web.pdf)
- :material-file-search: **Runs:** [MU03np3](./runs.md#mu03np3) | [MU03np4](./runs.md#mu03np4) | [MU03np5](./runs.md#mu03np5) | [MU03td04](./runs.md#mu03td04) | [MU03td03](./runs.md#mu03td03) | [MU03td05](./runs.md#mu03td05) | [MU03td01](./runs.md#mu03td01) | [MU03np1](./runs.md#mu03np1)

??? abstract "Abstract"
	
	This paper reports the experiments done at The University of Melbourne for the Robust and Web tracks of TREC-2003. We explore the idea of determining the impact of a term locally within the document and in a qualitative manner instead of a quantitative one. The impact of each distinct term in a document or query text is defined to be a small integer. The scalar product of the impact vector for a document and the impact vector for a query is taken to be the similarity score between them, an arrangement that allows very fast query evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnhM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnhM03,
		author = {Vo Ngoc Anh and Alistair Moffat},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Robust and Web Retrieval with Document-Centric Integral Impacts},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {726--731},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/umelbourne.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnhM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT at TREC 2003, Task Classification and Document Structrure  for Known-Item Search

_Steven M. Beitzel, Eric C. Jensen, Rebecca Cathey, Ling Ma, David A. Grossman, Ophir Frieder, Abdur Chowdhury, Greg Pass, Herman Vandermolen_

- :fontawesome-solid-user-group: **Participant:** [iit.grossman](./participants.md#iit.grossman)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/iit.web.pdf](http://trec.nist.gov/pubs/trec12/papers/iit.web.pdf)
- :material-file-search: **Runs:** [iit03sau](./runs.md#iit03sau) | [iit03sa](./runs.md#iit03sa) | [iit03wtaez](./runs.md#iit03wtaez) | [iit03wp75](./runs.md#iit03wp75) | [iit03su](./runs.md#iit03su)

??? abstract "Abstract"
	
	This year's TREC 2003 web task incorporated two retrieval tasks into a single set of experiments for Known-Item retrieval. We hypothesized that not all retrieval tasks should use the same retrieval approach when a single search entry point is used. We applied task classifiers on top of traditional web retrieval approaches. Our traditional retrieval is based on fusion of result sets generated by query runs over independent parts of the document structure. Our task classifiers combine query term analysis with known information resources and URL depth. This approach to task classification shows promise: our classified runs improved overall MRR effectiveness over our traditional retrieval results by ~10%; provided an MRR of .665; ranked 87% of relevant results in the top 10; correctly ranked the #1result 56% of the time. 67% of the queries performed above the average, and 49% above the median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BeitzelJCMGFCPV03.bib) "
	```
	@inproceedings{DBLP:conf/trec/BeitzelJCMGFCPV03,
		author = {Steven M. Beitzel and Eric C. Jensen and Rebecca Cathey and Ling Ma and David A. Grossman and Ophir Frieder and Abdur Chowdhury and Greg Pass and Herman Vandermolen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIT} at {TREC} 2003, Task Classification and Document Structrure for Known-Item Search},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {311--320},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/iit.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BeitzelJCMGFCPV03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at TREC 2003 Web track - Topic Distillation Task

_Mohand Boughanem, Karen Sauvagnat, Cecile Laffaire_

- :fontawesome-solid-user-group: **Participant:** [irit-sig.boughanem](./participants.md#irit-sig.boughanem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/irit-sig.web.pdf](http://trec.nist.gov/pubs/trec12/papers/irit-sig.web.pdf)
- :material-file-search: **Runs:** [Merc1td](./runs.md#merc1td) | [Merc1ti](./runs.md#merc1ti) | [Merc2tp](./runs.md#merc2tp) | [Merc2tm](./runs.md#merc2tm)

??? abstract "Abstract"
	
	The tests performed for TREC'2003 web track were focused on the topic distillation part. The aim of our participation is to validate the results we obtained last year and to test the use of term proximity on Mercure model. As last year, ad-hoc methodologies were used to answer the topic distillation task. 4 runs were submitted to NIST this year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemSL03.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemSL03,
		author = {Mohand Boughanem and Karen Sauvagnat and Cecile Laffaire},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Mercure at {TREC} 2003 Web track - Topic Distillation Task},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {343--348},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/irit-sig.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemSL03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC12 Web and Interactive Tracks at CSIRO

_Nick Craswell, David Hawking, Trystan Upstill, Alistair McLean, Ross Wilkinson, Mingfang Wu_

- :fontawesome-solid-user-group: **Participant:** [CSIRO](./participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/csiro.web.pdf](http://trec.nist.gov/pubs/trec12/papers/csiro.web.pdf)
- :material-file-search: **Runs:** [csiro03td01](./runs.md#csiro03td01) | [csiro03td02](./runs.md#csiro03td02) | [csiro03td03](./runs.md#csiro03td03) | [csiro03td04](./runs.md#csiro03td04) | [csiro03td05](./runs.md#csiro03td05) | [csiro03ki01](./runs.md#csiro03ki01) | [csiro03ki02](./runs.md#csiro03ki02) | [csiro03ki03](./runs.md#csiro03ki03) | [csiro03ki04](./runs.md#csiro03ki04) | [csiro03ki05](./runs.md#csiro03ki05)

??? abstract "Abstract"
	
	This year, CSIRO teams participated in all three tasks of the web track; these being: the automatic topic distillation task, the home/named page finding task and the interactive topic distillation task. This paper describes our approaches, experiments and results. The following section describes our experiments in the two automatic tasks, and Section 3 describes our experiment in the interactive task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellHUMWW03.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellHUMWW03,
		author = {Nick Craswell and David Hawking and Trystan Upstill and Alistair McLean and Ross Wilkinson and Mingfang Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC12} Web and Interactive Tracks at {CSIRO}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {193--203},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/csiro.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellHUMWW03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Non-Functional Prototype at TREC 2003

_Brian D. Davison, Wei Zhang, Josh Miller_

- :fontawesome-solid-user-group: **Participant:** [lehighu.davison](./participants.md#lehighu.davison)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/lehighu.web.pdf](http://trec.nist.gov/pubs/trec12/papers/lehighu.web.pdf)
- :material-file-search: **Runs:** [03wume296](./runs.md#03wume296) | [03wume298](./runs.md#03wume298) | [03wume206](./runs.md#03wume206) | [03wume359](./runs.md#03wume359)

??? abstract "Abstract"
	
	As a first attempt at participation in the TREC competition, we built a system which produced some preliminary results, but was unable to generate the quality of results that we expected. While we were able to submit four base-line runs, bugs were discovered in the final hours before the deadline making it impossible to submit results using our intended implementation. We have since found additional coding errors, making our submitted results expectedly poor. The size of our index dataset was approximately 3.8GB without compression. We did not use term position information nor any kind of phrasal indexing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DavisonZM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/DavisonZM03,
		author = {Brian D. Davison and Wei Zhang and Josh Miller},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Non-Functional Prototype at {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {383--385},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/lehighu.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DavisonZM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMBC at TREC 12

_Srikanth Kallurkar, Yongmei Shi, R. Scott Cost, Charles K. Nicholas, Akshay Java, Christopher James, Sowjanya Rajavaram, Vishal Shanbhag, Sachin Bhatkar, Drew Ogle_

- :fontawesome-solid-user-group: **Participant:** [umarylandbc.kallurkar](./participants.md#umarylandbc.kallurkar)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/umbc.web.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/umbc.web.novelty.pdf)
- :material-file-search: **Runs:** [C2B](./runs.md#c2b) | [C2A](./runs.md#c2a)

??? abstract "Abstract"
	
	We present the results of UMBC's participation in the Web and Novelty tracks. We explored various heuristics-based link analysis approaches to the Topic Distillation task. For the novelty task we tried several methods for exploiting semantic information of sentences based on the SVD technique. We used SVD to expand the query and to filter redundant sentences. We also used a clustering algorithm that is also based on SVD.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KallurkarSCNJJRSBO03.bib) "
	```
	@inproceedings{DBLP:conf/trec/KallurkarSCNJJRSBO03,
		author = {Srikanth Kallurkar and Yongmei Shi and R. Scott Cost and Charles K. Nicholas and Akshay Java and Christopher James and Sowjanya Rajavaram and Vishal Shanbhag and Sachin Bhatkar and Drew Ogle},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UMBC} at {TREC} 12},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {699--706},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/umbc.web.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KallurkarSCNJJRSBO03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Approaches to Robust and Web Retrieval

_Jaap Kamps, Christof Monz, Maarten de Rijke, Börkur Sigurbjörnsson_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.derijke](./participants.md#uamsterdam.derijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uamsterdam.web.robust.pdf](http://trec.nist.gov/pubs/trec12/papers/uamsterdam.web.robust.pdf)
- :material-file-search: **Runs:** [UAmsT03WnOWS](./runs.md#uamst03wnows) | [UAmsT03WnLM](./runs.md#uamst03wnlm) | [UAmsT03WnLn3](./runs.md#uamst03wnln3) | [UAmsT03WnLM3](./runs.md#uamst03wnlm3) | [UAmsT03WnMSW](./runs.md#uamst03wnmsw) | [UAmsT03WtOk3](./runs.md#uamst03wtok3) | [UAmsT03WtLM3](./runs.md#uamst03wtlm3) | [UAmsT03WtOkI](./runs.md#uamst03wtoki) | [UAmsT03WtLMI](./runs.md#uamst03wtlmi) | [UAmsT03WtOkC](./runs.md#uamst03wtokc)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2003 Robust and Web tracks. For the Robust track, we experimented with the impact of stemming and feedback on the worst scoring topics. Our main finding is the effectiveness of stemming on poorly performing topics, which sheds new light on the role of morphological normalization in information retrieval. For both the home/named page finding and topic distillation tasks of the Web track, we experimented with different document representations and retrieval models. Our main finding is effectiveness of the anchor text index for both tasks, suggesting that compact document representations are a fruitful strategy for scaling-up retrieval systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KampsMRS03.bib) "
	```
	@inproceedings{DBLP:conf/trec/KampsMRS03,
		author = {Jaap Kamps and Christof Monz and Maarten de Rijke and B{\"{o}}rkur Sigurbj{\"{o}}rnsson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Approaches to Robust and Web Retrieval},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {594--599},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uamsterdam.web.robust.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KampsMRS03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Document Structure with IR Tools

_Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [ualaska.newby](./participants.md#ualaska.newby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/ualaska.web.pdf](http://trec.nist.gov/pubs/trec12/papers/ualaska.web.pdf)
- :material-file-search: **Runs:** [irttgrep](./runs.md#irttgrep) | [irtfgrep](./runs.md#irtfgrep)

??? abstract "Abstract"
	
	The IRTools software toolkit was modified for 2003 to utilize a MySQL database for the inverted index. Indexing was for each occurrence of each term in the collection, with HTML structure, location offset, paragraph, and subdocument weight considered. This structure enables some more sophisticated queries than a “bag of words” approach. Post hoc results from the TREC 2002 Named Page Web task are presented, in which a staged fall through approach to topic processing yielded good results, with exact precision of 0.49. The paper also provides an overview of IRTools and its interactive interface, as well as an invitation for IR researchers to get involved with the GridIR standards formation process.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Newby03.bib) "
	```
	@inproceedings{DBLP:conf/trec/Newby03,
		author = {Gregory B. Newby},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Document Structure with {IR} Tools},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {568--577},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/ualaska.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Newby03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Structural Information and the Use of Priors in Mixed Named-Page  and Homepage Finding

_Paul Ogilvie, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu.callan](./participants.md#cmu.callan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/cmu-dir.web.pdf](http://trec.nist.gov/pubs/trec12/papers/cmu-dir.web.pdf)
- :material-file-search: **Runs:** [LmrEq](./runs.md#lmreq) | [LmrEqUrl](./runs.md#lmrequrl) | [LmrEst](./runs.md#lmrest) | [LmrEstUrl](./runs.md#lmresturl)

??? abstract "Abstract"
	
	This paper presents Carnegie Mellon University's experiments on the mixed named-page and homepage finding task of the TREC 12 Web Track. Our results were strong; we achieved the success using language models estimated from combining information from document text, in-link text, and information present in the structure of the documents. We also present experiments using expectations about posterior distributions to create class-based prior probabilities. We find that priors do provide a large gain for our official runs, but we do further experiments that show the priors do not always help. Some preliminary analysis shows that the prior probabilities are not providing the desired posterior distributions. In cases where applying the priors harm performance, the observed posterior distributions in the rankings are far off of the desired posterior distributions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OgilvieC03.bib) "
	```
	@inproceedings{DBLP:conf/trec/OgilvieC03,
		author = {Paul Ogilvie and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Structural Information and the Use of Priors in Mixed Named-Page and Homepage Finding},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {177--184},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/cmu-dir.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OgilvieC03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Meiji University Web and Novelty Track Experiments at TREC 2003

_Ryosuke Ohgaya, Akiyoshi Shimmura, Tomohiro Takagi, Akiko N. Aizawa_

- :fontawesome-solid-user-group: **Participant:** [meijiu.takagi](./participants.md#meijiu.takagi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/meijiu.web.novelty.pdf](http://trec.nist.gov/pubs/trec12/papers/meijiu.web.novelty.pdf)
- :material-file-search: **Runs:** [meijihilw1](./runs.md#meijihilw1) | [meijihilw2](./runs.md#meijihilw2) | [meijihilw3](./runs.md#meijihilw3) | [meijihilw4](./runs.md#meijihilw4) | [meijihilw5](./runs.md#meijihilw5)

??? abstract "Abstract"
	
	This year we participated in TREC for the first time. We submitted runs for Novelty track and the topic distillation task of Web track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OhgayaSTA03.bib) "
	```
	@inproceedings{DBLP:conf/trec/OhgayaSTA03,
		author = {Ryosuke Ohgaya and Akiyoshi Shimmura and Tomohiro Takagi and Akiko N. Aizawa},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Meiji University Web and Novelty Track Experiments at {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {399--407},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/meijiu.web.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OhgayaSTA03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at the Web Track: Dynamic Application of Hyperlink  Analysis using the Query Scope

_Vassilis Plachouras, Iadh Ounis, Cornelis Joost van Rijsbergen, Fidel Cacheda_

- :fontawesome-solid-user-group: **Participant:** [uglasgow.ounis](./participants.md#uglasgow.ounis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uglasgow.web.pdf](http://trec.nist.gov/pubs/trec12/papers/uglasgow.web.pdf)
- :material-file-search: **Runs:** [uogki1c](./runs.md#uogki1c) | [uogki2ca](./runs.md#uogki2ca) | [uogki3cah](./runs.md#uogki3cah) | [uogki4cahs](./runs.md#uogki4cahs) | [uogtd1c](./runs.md#uogtd1c) | [uogtd2ca](./runs.md#uogtd2ca) | [uogtd3cas](./runs.md#uogtd3cas) | [uogtd4cahs](./runs.md#uogtd4cahs) | [uogtd5cass](./runs.md#uogtd5cass)

??? abstract "Abstract"
	
	This year, our participation to the Web track aims at combining dynamically evidence from both content and hyperlink analysis. To this end, we introduce a decision mechanism based on the so-called query scope concept. For the topic distillation task, we find that the use of anchor text increases precision significantly over content- only retrieval, a result that contrasts with our TREC11 findings. Using the query scope, we show that a selective application of hyperlink analysis, or URL-based scores, is effective for the more generic queries, improving the overall precision. In fact, our most effective runs use the decision mechanism and outperform significantly the content and anchor text retrieval. For the known item task, we employ the query scope in order to distinguish the named page queries from the home page queries, obtaining results close to the content and anchor text baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PlachourasORC03.bib) "
	```
	@inproceedings{DBLP:conf/trec/PlachourasORC03,
		author = {Vassilis Plachouras and Iadh Ounis and Cornelis Joost van Rijsbergen and Fidel Cacheda},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at the Web Track: Dynamic Application of Hyperlink Analysis using the Query Scope},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {646--652},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uglasgow.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PlachourasORC03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2003 Experiment: Genomic and Web Searches

_Jacques Savoy, Yves Rasolofo, Laura Perret_

- :fontawesome-solid-user-group: **Participant:** [neuchatelu.savoy](./participants.md#neuchatelu.savoy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uneuchatel.genome.web.pdf](http://trec.nist.gov/pubs/trec12/papers/uneuchatel.genome.web.pdf)
- :material-file-search: **Runs:** [UniNEtd5](./runs.md#uninetd5) | [UniNEtd1](./runs.md#uninetd1) | [UniNEtd2](./runs.md#uninetd2) | [UniNEtd3](./runs.md#uninetd3) | [UniNEtd4](./runs.md#uninetd4) | [UniNEnp1](./runs.md#uninenp1) | [UniNEnp2](./runs.md#uninenp2) | [UniNEnp3](./runs.md#uninenp3) | [UniNEnp4](./runs.md#uninenp4) | [UniNEnp5](./runs.md#uninenp5)

??? abstract "Abstract"
	
	This year we took part in the genomic information retrieval and information extraction tasks, as well as the named page and topic distillation searches. In carrying out the last two tasks, we made use of link anchor information and document content in order to construct Web page representatives. This type of document representation uses multi-vectors to highlight the importance of both hyperlink and document content.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavoyRP03.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavoyRP03,
		author = {Jacques Savoy and Yves Rasolofo and Laura Perret},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2003 Experiment: Genomic and Web Searches},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {739--750},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uneuchatel.genome.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SavoyRP03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Relevance Propagation for Topic Distillation UIUC TREC 2003 Web  Track Experiments

_Azadeh Shakery, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uillinoisuc.zhai](./participants.md#uillinoisuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.web.pdf](http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.web.pdf)
- :material-file-search: **Runs:** [UIUC03Wb](./runs.md#uiuc03wb) | [UIUC03Wp](./runs.md#uiuc03wp) | [UIUC03W2s](./runs.md#uiuc03w2s) | [UIUC03Wu1](./runs.md#uiuc03wu1) | [UIUC03Wu2](./runs.md#uiuc03wu2)

??? abstract "Abstract"
	
	In this paper, we report our experiments on the Web Track TREC-2003. We submitted five runs for the topic distillation task. Our goal was to evaluate the standard language modeling algorithms for topic distillation, as well as to explore the impact of combining link and content information. We proposed a new general relevance propagation model for combining link and content information, and explored a number of specific methods derived from the model. The experiment results show that combining link and content information generally performs better than using only content information, though the amount of improvement is sensitive to the document collection and tuning of parameters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShakeryZ03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShakeryZ03,
		author = {Azadeh Shakery and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Relevance Propagation for Topic Distillation {UIUC} {TREC} 2003 Web Track Experiments},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {673--677},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/uillinois-uc.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShakeryZ03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Towards a Sense Based Document Representation for Internet Information  Retrieval

_Christopher Stokoe, John Tait_

- :fontawesome-solid-user-group: **Participant:** [usunderland.stokoe](./participants.md#usunderland.stokoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/usunderland.web.pdf](http://trec.nist.gov/pubs/trec12/papers/usunderland.web.pdf)
- :material-file-search: **Runs:** [TBBASE](./runs.md#tbbase) | [SBBASE](./runs.md#sbbase) | [SBUNIQUE](./runs.md#sbunique) | [TBUNIQUE](./runs.md#tbunique)

??? abstract "Abstract"
	
	We describe an attempt to use word sense as an alternate text representation within an information retrieval system in order to enhance retrieval effectiveness. A performance comparison between a term and sense based system was carried out indicating increased retrieval effectiveness using a sense based representation. These increases come about by using a retrieval strategy designed to down rank documents containing query terms identified as being used in an infrequent sense.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StokoeT03.bib) "
	```
	@inproceedings{DBLP:conf/trec/StokoeT03,
		author = {Christopher Stokoe and John Tait},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Towards a Sense Based Document Representation for Internet Information Retrieval},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {791--795},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/usunderland.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StokoeT03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2003 Novelty and Web Track at ICT

_Jian Sun, Zhe Yang, Wenfeng Pan, Huaping Zhang, Bin Wang, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas-ict.bin](./participants.md#cas-ict.bin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.web.pdf](http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.web.pdf)
- :material-file-search: **Runs:** [ICTWebTD12A](./runs.md#ictwebtd12a) | [ICTWebTD12B](./runs.md#ictwebtd12b) | [ICTWebTD12C](./runs.md#ictwebtd12c) | [ICTWebKI12A](./runs.md#ictwebki12a) | [ICTWebKI12B](./runs.md#ictwebki12b) | [ICTWebKI12C](./runs.md#ictwebki12c)

??? abstract "Abstract"
	
	In this paper, we will present our approaches and experiments on the following two tracks of TREC-2003: Novelty track and Web track. The novelty track can be treated as a binary classification problem: relevant vs. irrelevant sentences, or new vs. non-new. In this way, we applied variants of techniques that have been employed for text categorization. To retrieve the relevant sentences, we compute the similarity between the topic and sentences using vector space model (VSM). In addition, we tried several techniques in an attempt to improve the performance: using narrative field and adopting dynamic threshold for different documents. We also have implemented the KNN algorithm and Winnow algorithm for classifying the sentences into relevant and irrelevant in the novelty task 3. To detect the new sentences, we used Maximum Marginal Relevance (MMR) measure, Winnow algorithm and so on. In addition, we attempted to detect novelty by computing semantic distance between sentences using WordNet. For the Web track, we improved the basic SMART system, and the Lnu-Ltu weighting method was introduced into the system. The improved system has been proved to be effective in last year's task. In addition, we implemented a simple retrieval system using the probability model that is adopted by Okapi. The structure of the paper is as follows: The section 2 reports the approaches and experiments in novelty track. The section 3 describes the experiments in web track. Finally, in section 4, we conclude by summarizing our experiments and presenting the future work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SunYPZWC03.bib) "
	```
	@inproceedings{DBLP:conf/trec/SunYPZWC03,
		author = {Jian Sun and Zhe Yang and Wenfeng Pan and Huaping Zhang and Bin Wang and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2003 Novelty and Web Track at {ICT}},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {138--146},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/chinese-acad-sci.novelty.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SunYPZWC03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Robust, Web and Genomic Retrieval with Hummingbird SearchServer at  TREC 2003

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/hummingbird.robust.web.genomic.pdf](http://trec.nist.gov/pubs/trec12/papers/hummingbird.robust.web.genomic.pdf)
- :material-file-search: **Runs:** [humNP03pl](./runs.md#humnp03pl) | [humTD03pl](./runs.md#humtd03pl) | [humTD03upl](./runs.md#humtd03upl) | [humNP03upl](./runs.md#humnp03upl) | [humTD03uhpl](./runs.md#humtd03uhpl) | [humNP03uhpl](./runs.md#humnp03uhpl) | [humNP03l](./runs.md#humnp03l) | [humNP03up](./runs.md#humnp03up) | [humTD03up](./runs.md#humtd03up) | [humTD03l](./runs.md#humtd03l)

??? abstract "Abstract"
	
	Hummingbird participated in 4 tasks of TREC 2003: the ad hoc task of the Robust Retrieval Track (find at least one relevant document in the first 10 rows from 1.9GB of news and government data), the navigational task of the Web Track (find the home or named page in 1.2 million pages (18GB) from the .GOV domain), the topic distillation task of the Web Track (find key resources for topics in the first 10 rows from home pages of .GOV), and the primary task of the Genomics Track (find all records focusing on the named gene in 1.1GB of MEDLINE data). In the ad hoc task, SearchServer found a relevant document in the first 10 rows for 48 of the 50 new short (Title-only) topics. In the navigational task, SearchServer returned the home or named page in the first 10 rows for more than 75% of the 300 queries. In the distillation task, a SearchServer run found the most key resources in the first 10 rows of the submitted runs from 23 groups.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson03.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson03,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Robust, Web and Genomic Retrieval with Hummingbird SearchServer at {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {254--267},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/hummingbird.robust.web.genomic.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Research Asia at the Web Track of TREC 2003

_Ji-Rong Wen, Ruihua Song, Deng Cai, Kaihua Zhu, Shipeng Yu, Shaozhi Ye, Wei-Ying Ma_

- :fontawesome-solid-user-group: **Participant:** [microsoftasia.wen](./participants.md#microsoftasia.wen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/microsoft-asia.web.pdf](http://trec.nist.gov/pubs/trec12/papers/microsoft-asia.web.pdf)
- :material-file-search: **Runs:** [MSRA1001](./runs.md#msra1001) | [MSRA3](./runs.md#msra3) | [MSRA4003](./runs.md#msra4003) | [MSRA4002](./runs.md#msra4002) | [MSRA1002](./runs.md#msra1002) | [MSRANP1](./runs.md#msranp1) | [MSRANP3](./runs.md#msranp3) | [MSRANP2](./runs.md#msranp2)

??? abstract "Abstract"
	
	This is the first year that our group participates in the Web track of the TREC conference. Here we report our system and methods on the topic distillation task and the home/ named page finding task. All of our experiments are conducted on a Web search platform we designed and developed from scratch. We originally want to use an existing retrieval system such as Okapi or the full text search mechanism of SQL Server. But we soon find the limitations of such a strategy - these systems cannot fully support some important Web search functions such as link analysis and anchor text, and they also lack of the flexibility to arbitrarily adjust some parameters of add new ranking functions. So we decided to design and implement a research platform to let researchers to test various algorithms or new ideas easily and, also, to conduct the TREC experiments easily. We will introduce the framework of this system in the 'Platform' section. We feel that this year's topic distillation is more close to the real Web search scenarios. The target is to find a list of key resources for a particular (broad) topic and 'key resources' are defined as the entry pages of websites. So, different from the previous years, we think that link analysis may play a positive role on identifying key resources in this year. As a consequence, we focus on using different link analysis techniques to enhance the relevance ranking. In particularly, we propose a novel block-based HITS algorithm to solve the noisy link and topic drifting problems of the classic HITS algorithm. The basic idea is to segment each Web page into multiple semantic blocks using a vision-based page segmentation algorithm we developed before. Then the main steps of the HITS algorithms, such as getting the seeds, expanding the neighbors using inlinks and outlinks, and calculating hub/authority values, can be performed at the block level instead of at the page level. Thus the noisy link and topic drifting problems can be effectively overcome. We will detail these techniques in the 'Page Layout Analysis' and 'Block-based HITS' section. To our understanding, the biggest difference of this year's topic distillation task from last year is that, in general, only one most 'suitable' page for each website should be returned as a top-ranked result. Any other page at the same website should not be included in the results or ranked highly since it is a 'part of a larger site also principally devoted to the topic', despite that the page also 'is principally devoted to the topic'. Therefore, we construct a hierarchical site map for each website by building up the parent-children relationships of Web pages in the GOV dataset. Then we apply a site compression technique to select the most suitable entry pages for websites among the retrieval results and return these entry pages as top-ranked pages. This site compression method has proved to be quite effective to increase the p@10 precision if used appropriately, and will be introduced in the 'Site Compression' section. We totally submitted 5 runs for the topic distillation task and 3 runs for the home/named page finding task. In the 'Experimental results' section, we will introduce these runs and their evaluation results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WenSCZYYM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/WenSCZYYM03,
		author = {Ji{-}Rong Wen and Ruihua Song and Deng Cai and Kaihua Zhu and Shipeng Yu and Shaozhi Ye and Wei{-}Ying Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research Asia at the Web Track of {TREC} 2003},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {408--417},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/microsoft-asia.web.pdf},
		timestamp = {Wed, 13 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WenSCZYYM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC-2003 Web Track

_Kiduk Yang, Dan E. Albertson_

- :fontawesome-solid-user-group: **Participant:** [indianau.seki](./participants.md#indianau.seki)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/indianau.web.pdf](http://trec.nist.gov/pubs/trec12/papers/indianau.web.pdf)
- :material-file-search: **Runs:** [widittdb1](./runs.md#widittdb1) | [widittdb1r1](./runs.md#widittdb1r1) | [widittdf1r1](./runs.md#widittdf1r1) | [widittdf1r2](./runs.md#widittdf1r2) | [widitpfb1](./runs.md#widitpfb1) | [widitpff1](./runs.md#widitpff1)

??? abstract "Abstract"
	
	[...] In our earlier studies (Yang, 2002a; Yang, 2002b), where we investigated various fusion approaches for ad-hoc retrieval using the WT10g collection, we found that simplistic approach that combine the results of content- and link-based retrieval results did not enhance retrieval performance in general. TREC participants in recent Web track environment, however, found that use of non-textual information such as hyperlinks, document structure, and URL could be beneficial for specific tasks such as topic distillation and named/home page finding tasks. We believe that this is not only due to the change in the retrieval environment (i.e. test collection, retrieval task) but also the result of more dynamic approach to combining multiple sources of evidence than straightforward result merging. Thus, our focus in TREC- 2003 Web track was in exploring fusion strategies that utilize various information sources in a dynamic manner to optimize retrieval for specific search environment. For our experiment, we used the experimental fusion retrieval system called WIDIT to combine content and link information, and then reranked the combined result based on heuristics arrived at from dynamic system tuning process.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangA03.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangA03,
		author = {Kiduk Yang and Dan E. Albertson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC-2003} Web Track},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {328--336},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/indianau.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangA03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### VT at TREC-2003: The Web Track Report

_Rui Yang, Li Wang, Weiguo Fan, Wensi Xi, Ming Luo, Ye Zhou, Edward A. Fox_

- :fontawesome-solid-user-group: **Participant:** [vatech.xi](./participants.md#vatech.xi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/vatech.web.pdf](http://trec.nist.gov/pubs/trec12/papers/vatech.web.pdf)
- :material-file-search: **Runs:** [VTtdgp41](./runs.md#vttdgp41) | [VTtdgp52](./runs.md#vttdgp52) | [VTtdok4](./runs.md#vttdok4) | [VTtdgp33](./runs.md#vttdgp33) | [VTtdgp5055](./runs.md#vttdgp5055) | [VTnhpok1](./runs.md#vtnhpok1) | [VTnhpgp42](./runs.md#vtnhpgp42) | [VTnhpgp33](./runs.md#vtnhpgp33) | [VTnhpgp55](./runs.md#vtnhpgp55) | [VTnhpgpd4](./runs.md#vtnhpgpd4)

??? abstract "Abstract"
	
	This year, we participated in the Web Track in addition to the Robust Track. We submitted results on both topic distillation and home page/named page finding tasks. As our time and human resources were limited for taking two tasks simultaneously, in this task we only concentrate on testing our ranking function discovery technique, ARRANGER (Automatic Rendering of RANking functions by GEnetic pRogramming) [Fan 2003a, Fan 2003b], which uses Genetic Programming (GP) to discover the “optimal” ranking functions for various information needs. From Web Track 2002, the training, testing and validation data sets are constructed in the same manner as in Robust Track. Our ARRANGER engine works on those data sets and automatically searches for the “best” ranking functions. The best runs are selected for submission according to their performance on queries in Web track 2002. Our paper is organized as follows. Section 2 states our research objectives. Section 3 describes basic data processing steps. Section 4 summarizes the GP algorithm used in our system and detailed information about how we use GP to find ranking function. Section 5 shows the official submission results in comparison with the other TREC teams.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangWFXLZF03.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangWFXLZF03,
		author = {Rui Yang and Li Wang and Weiguo Fan and Wensi Xi and Ming Luo and Ye Zhou and Edward A. Fox},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{VT} at {TREC-2003:} The Web Track Report},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {837},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/vatech.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangWFXLZF03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2003: Novelty, Robust and Web

_Min Zhang, Chuan Lin, Yiqun Liu, Leo Zhao, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [tsinghuau.ma](./participants.md#tsinghuau.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec12/papers/tsinghuau.novelty.robust.web.pdf](http://trec.nist.gov/pubs/trec12/papers/tsinghuau.novelty.robust.web.pdf)
- :material-file-search: **Runs:** [THUIRpf0301](./runs.md#thuirpf0301) | [THUIRpf0302](./runs.md#thuirpf0302) | [THUIRpf0303](./runs.md#thuirpf0303) | [THUIRpf0304](./runs.md#thuirpf0304) | [THUIRpf0305](./runs.md#thuirpf0305) | [THUIRtd0301](./runs.md#thuirtd0301) | [THUIRtd0303](./runs.md#thuirtd0303) | [THUIRtd0304](./runs.md#thuirtd0304) | [THUIRtd0305](./runs.md#thuirtd0305) | [THUIRtd0302](./runs.md#thuirtd0302)

??? abstract "Abstract"
	
	This is the second time that Tsinghua University Information Retrieval Group (THUIR) participates in TREC. In this year, we took part in four tracks: novelty, robust, web and HARD, describing in following sections, respectively. A new IR system named TMiner has been built on which all experiments have been performed. In the system, Primary Feature Model (PFM)[1] has been proposed and combined with BM2500 term weighting [2] , which led to encouraging results. Word-pair searching has also been performed and improves system precision. Both approaches are described in robust experiments (section 2), and they were also used in web track experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangLLZM03.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangLLZM03,
		author = {Min Zhang and Chuan Lin and Yiqun Liu and Leo Zhao and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2003: Novelty, Robust and Web},
		booktitle = {Proceedings of The Twelfth Text REtrieval Conference, {TREC} 2003, Gaithersburg, Maryland, USA, November 18-21, 2003},
		series = {{NIST} Special Publication},
		volume = {500-255},
		pages = {556--567},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2003},
		url = {http://trec.nist.gov/pubs/trec12/papers/tsinghuau.novelty.robust.web.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangLLZM03.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

