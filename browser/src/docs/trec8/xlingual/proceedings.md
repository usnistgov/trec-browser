# Proceedings - Cross-Language 1999 

#### Cross-Language Information Retrieval (CLIR) Track Overview

_Martin Braschler, Peter Schäuble, Carol Peters_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8ov.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8ov.pdf)
??? abstract "Abstract"
	
	A cross-language retrieval track was offered for the third time at TREC-8. The main task was the same as that of the previous year: the goal was for groups to use queries written in a single language in order to retrieve documents from a multilingual pool of documents written in many different languages. Compared to the usual definition of cross-language information retrieval, where systems work with a single language pair, retrieving documents in a language L1 using queries in language L2, this is a slightly more comprehensive task, and we feel one that more closely meets the demands of real world applications. The document languages used were the same as for TREC-7: English, German, French and Italian. The queries were available in all of these languages. Monolingual non-English retrieval was offered to new participants who preferred to begin with an easier task. However, all the groups which did not tackle the full task opted for limited cross-language rather than monolingual runs. These experiments were evaluated by NIST and are published as unofficial ('alternate') runs. We also offered a subtask, working with documents from the field of social sciences. This collection (known as 'GIRT') has some very interesting features, such as controlled vocabulary terms, title translations, and an associated multilingual thesaurus. The track was coordinated at Eurospider Information Technology AG in Zurich. Due to its multilingual nature, the topic creation and relevance assessment tasks were distributed over four sites in different countries: NIST (English), IZ Bonn (German), IEI-CNR (Italian) and University of Zurich (French). The University of Hildesheim invested considerable effort into rendering the topics homogeneous and consistent over languages. The participating groups experimented with a wide variety of strategies, ranging machine translation, corpus-, and dictionary-based approaches. Some results are given in Section 4. There were, however, also some striking similarities between many of the runs, such as the choice of English as topic language the majority, and the use of Systran by a lot of groups. Some implications of these findings are discussed in Section 5. The main goal of the TREC CLIR activities has been the creation of a multilingual test collection that is re-usable for a wide range of evaluation experiments. This means that the quality of the relevance assessments is very important. The Twenty-One group conducted an interesting analysis with respect to the completeness of the assessments and the impact of this on the pool. We address some of their findings in Section 5. The paper concludes with an indication of our plans for the future of the cross-language track, which will bring substantial changes to the format and coordination of the activities.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BraschlerSP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BraschlerSP99,
		author = {Martin Braschler and Peter Sch{\"{a}}uble and Carol Peters},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Cross-Language Information Retrieval {(CLIR)} Track Overview},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8ov.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BraschlerSP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CINDOR Conceptual Interlingua Document Retrieval: TREC-8 Evaluation

_Miguel E. Ruiz, Anne Diekema, Paraic Sheridan_

- :fontawesome-solid-user-group: **Participant:** [textwise](./participants.md#textwise)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/TextWise.pdf](http://trec.nist.gov/pubs/trec8/papers/TextWise.pdf)
- :material-file-search: **Runs:** [TW8F2E](./runs.md#tw8f2e) | [TW8E2F](./runs.md#tw8e2f)

??? abstract "Abstract"
	
	The TREC-8 evaluation of the CINDOR system was based on English and French data from the cross-language retrieval track. Our objective was to continue our investigation of our conceptual interlingua approach to cross-language retrieval, specifically by measuring the contribution of conceptual retrieval over and above a baseline cross-language retrieval approach based on machine translation of queries. In both of the cross-language runs that were submitted for evaluation, corresponding to English-French and French-English retrieval, performance was measured at 75% of the equivalent monolingual searches. We noted however that absolute average precision values achieved were somewhat lower than many other systems in the cross-language track. Our hypothesis, that the underlying retrieval engine used in CINDOR was employing a simple retrieval function that was impacting performance, was confirmed through experiments with the SMART system configured with several different retrieval settings. Taken together, our TREC-8 experiments point to the value of our conceptual interlingua approach to retrieval, but indicate that our retrieval algorithm must be brought up to date so that valid comparisons may be made to other approaches used in other cross-language systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuizDS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuizDS99,
		author = {Miguel E. Ruiz and Anne Diekema and Paraic Sheridan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CINDOR} Conceptual Interlingua Document Retrieval: {TREC-8} Evaluation},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/TextWise.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuizDS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLARIT TREC-8 CLIR Experiments

_Yan Qu, Hongming Jin, Alla N. Eilerman, Emilia Stoica, David A. Evans_

- :fontawesome-solid-user-group: **Participant:** [claritech](./participants.md#claritech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/CLARIT_CLIR.pdf](http://trec.nist.gov/pubs/trec8/papers/CLARIT_CLIR.pdf)
- :material-file-search: **Runs:** [CLARITrmwf1](./runs.md#claritrmwf1) | [CLARITrmwf2](./runs.md#claritrmwf2) | [CLARITrmwf3](./runs.md#claritrmwf3) | [CLARITdmwf](./runs.md#claritdmwf)

??? abstract "Abstract"
	
	In the TREC-8 cross-language information retrieval (CLIR) track, we adopted the approach of using machine translation to prepare a source-language query for use in a target-language retrieval task. We empirically evaluated (1) the effect of pseudo relevance feedback on retrieval performance with two feedback vector length control methods in CLIR and (2) the effect of multilingual data merging either before or after retrieval. Our experiments show that, in general, pseudo relevance feedback significantly improves cross-language retrieval performance, and that post-retrieval merging of retrieval results can outperform pre-retrieval merging of multilingual data collections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QuJESE99.bib) "
	```
	@inproceedings{DBLP:conf/trec/QuJESE99,
		author = {Yan Qu and Hongming Jin and Alla N. Eilerman and Emilia Stoica and David A. Evans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CLARIT} {TREC-8} {CLIR} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/CLARIT\_CLIR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QuJESE99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CRL's TREC-8 Systems Cross-Lingual IR, and Q&A

_William C. Ogden, James R. Cowie, Yevgeny Ludovik, Hugo Molina-Salgado, Sergei Nirenburg, Nigel Sharples, Svetlana O. Sheremetyeva_

- :fontawesome-solid-user-group: **Participant:** [nmsu](./participants.md#nmsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/crl_proceedings.pdf](http://trec.nist.gov/pubs/trec8/papers/crl_proceedings.pdf)
- :material-file-search: **Runs:** [nmsui1](./runs.md#nmsui1)

??? abstract "Abstract"
	
	This paper describes the systems used by CRL in the Cross-lingual IR and Q&A tracks. The cross-language experiment was unique in that it was run interactively with a mono-lingual user simulating how a true cross-language system might be used. The methods used in the Q&A system are based on language processing technology developed at CRL for machine translation and information extraction.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OgdenCLMNSS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/OgdenCLMNSS99,
		author = {William C. Ogden and James R. Cowie and Yevgeny Ludovik and Hugo Molina{-}Salgado and Sergei Nirenburg and Nigel Sharples and Svetlana O. Sheremetyeva},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {CRL's {TREC-8} Systems Cross-Lingual IR, and Q{\&}A},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/crl\_proceedings.pdf},
		timestamp = {Thu, 17 Nov 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OgdenCLMNSS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Experiments at Maryland: CLIR, QA and Routing

_Douglas W. Oard, Jianqiang Wang, Dekang Lin, Ian Soboroff_

- :fontawesome-solid-user-group: **Participant:** [umd](./participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf](http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf)
- :material-file-search: **Runs:** [umd99b1](./runs.md#umd99b1) | [umd99b2](./runs.md#umd99b2) | [umd99b3](./runs.md#umd99b3) | [umd99c1](./runs.md#umd99c1) | [umd99c2](./runs.md#umd99c2)

??? abstract "Abstract"
	
	The University of Maryland team participated in four aspects of TREC-8: the ad hoc retrieval task, the main task in the cross-language retrieval (CLIR) track, the question answering track, and the routing task in the filtering track. The CLIR method was based on Pirkola's method for Dictionary-based Query Translation, using freely available dictionaries. Broad-coverage parsing and rule-based matching was used for question answering. Routing was performed using Latent Semantic Indexing in profile space.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardWLS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardWLS99,
		author = {Douglas W. Oard and Jianqiang Wang and Dekang Lin and Ian Soboroff},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Experiments at Maryland: CLIR, {QA} and Routing},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OardWLS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLIR using a Probabilistic Translation Model based on Web Documents

_Jian-Yun Nie_

- :fontawesome-solid-user-group: **Participant:** [montreal](./participants.md#montreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/TREC8-Nie.pdf](http://trec.nist.gov/pubs/trec8/papers/TREC8-Nie.pdf)
- :material-file-search: **Runs:** [RaliWebE2EF](./runs.md#raliwebe2ef) | [RaliWebF2EF](./runs.md#raliwebf2ef) | [RaliHanE2EF](./runs.md#ralihane2ef) | [RaliHanF2EF](./runs.md#ralihanf2ef)

??? abstract "Abstract"
	
	In this report, we describe the approach we used in TREC-8 Cross-Language IR (CLIR) track. The approach is based on probabilistic translation models estimated from two parallel training corpora: one established manually, and the other built automatically with the documents mined from the Web. We describe the principle of model building, the mining of parallel texts, as well as some preliminary evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Nie99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Nie99,
		author = {Jian{-}Yun Nie},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CLIR} using a Probabilistic Translation Model based on Web Documents},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/TREC8-Nie.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Nie99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Twenty-One at TREC-8: using Language Technology for Information  Retrieval

_Wessel Kraaij, Renée Pohlmann, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [twentyone](./participants.md#twentyone)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf](http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf)
- :material-file-search: **Runs:** [tno8dis](./runs.md#tno8dis) | [tno8gr](./runs.md#tno8gr) | [tno8mx](./runs.md#tno8mx) | [tno8dpx](./runs.md#tno8dpx)

??? abstract "Abstract"
	
	This paper describes the official runs of the Twenty-One group for TREC-8. The Twenty-One group participated in the Ad-hoc, CLIR, Adaptive Filtering and SDR tracks. The main focus of our experiments is the development and evaluation of retrieval methods that are motivated by natural language processing techniques. The following new techniques are introduced in this paper. In the Ad-Hoc and CLIR tasks we experimented with automatic sense disambiguation followed by query expansion or translation. We used a combination of thesaurial and corpus information for the disambiguation process. We continued research on CLIR techniques which exploit the target corpus for an implicit disambiguation, by importing the translation probabilities into the probabilistic term-weighting framework. In filtering we extended the the use of language models for document ranking with a relevance feedback algorithm for query term reweighting.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KraaijPH99.bib) "
	```
	@inproceedings{DBLP:conf/trec/KraaijPH99,
		author = {Wessel Kraaij and Ren{\'{e}}e Pohlmann and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Twenty-One at {TREC-8:} using Language Technology for Information Retrieval},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KraaijPH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad hoc, Cross-language and Spoken Document Information Retrieval at  IBM

_Martin Franz, J. Scott McCarley, Todd Ward_

- :fontawesome-solid-user-group: **Participant:** [ibm-franz](./participants.md#ibm-franz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/t8_ibm_hlt.pdf](http://trec.nist.gov/pubs/trec8/papers/t8_ibm_hlt.pdf)
- :material-file-search: **Runs:** [ibmcl8ea](./runs.md#ibmcl8ea) | [ibmcl8fa](./runs.md#ibmcl8fa) | [ibmcl8fc](./runs.md#ibmcl8fc) | [ibmcl8ec](./runs.md#ibmcl8ec)

??? abstract "Abstract"
	
	The Natural Language Systems group at IBM participated in three tracks at TREC-8: ad hoc, SDR and cross-language. Our SDR and ad hoc participation included experiments involving query expansion and clustering-induced document reranking. Our CLIR participation involved both the French and English queries and included experiments with the merging strategy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FranzMW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FranzMW99,
		author = {Martin Franz and J. Scott McCarley and Todd Ward},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ad hoc, Cross-language and Spoken Document Information Retrieval at {IBM}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/t8\_ibm\_hlt.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FranzMW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Eurospider Retrieval System and the TREC-8 Cross-Language Track

_Martin Braschler, Min-Yen Kan, Peter Schäuble, Judith Klavans_

- :fontawesome-solid-user-group: **Participant:** [eurospider](./participants.md#eurospider)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/eit_t8f.pdf](http://trec.nist.gov/pubs/trec8/papers/eit_t8f.pdf)
- :material-file-search: **Runs:** [EIT99mta](./runs.md#eit99mta) | [EIT99sta](./runs.md#eit99sta) | [EIT99sal](./runs.md#eit99sal)

??? abstract "Abstract"
	
	This year the Eurospider team, with help from Columbia, focused on trying different combinations of translation approaches. We investigated the use and integration of pseudo-relevance feedback, multilingual similarity thesauri and machine translation. We also looked at different ways of merging individual cross-language retrieval runs to produce multilingual result lists. We participated in both the CLIR main task and the GIRT sub task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BraschlerKSK99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BraschlerKSK99,
		author = {Martin Braschler and Min{-}Yen Kan and Peter Sch{\"{a}}uble and Judith Klavans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The Eurospider Retrieval System and the {TREC-8} Cross-Language Track},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/eit\_t8f.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BraschlerKSK99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at trec8: Adhoc, Web, CLIR and Filtering tasks

_Mohand Boughanem, Christine Julien, Josiane Mothe, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [irit](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/irit.pdf](http://trec.nist.gov/pubs/trec8/papers/irit.pdf)
- :material-file-search: **Runs:** [Mer8Can2x](./runs.md#mer8can2x) | [Mer8Cfr2x](./runs.md#mer8cfr2x) | [Mer8Can2x0](./runs.md#mer8can2x0)

??? abstract "Abstract"
	
	Three runs were submitted for our first participation in this track. All these runs were based on query translation using an online machine translation . Two of these runs are a comparison between query translation from English to other languages and from French to other languages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemJMS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemJMS99,
		author = {Mohand Boughanem and Christine Julien and Josiane Mothe and Chantal Soul{\'{e}}{-}Dupuy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure at trec8: Adhoc, Web, {CLIR} and Filtering tasks},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/irit.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemJMS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

