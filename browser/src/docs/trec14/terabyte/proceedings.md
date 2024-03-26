# Proceedings - Terabyte 2005 

#### The TREC 2005 Terabyte Track

_Charles L. A. Clarke, Falk Scholer, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/TERABYTE.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec14/papers/TERABYTE.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Terabyte Track explores how retrieval and evaluation techniques can scale to terabyte-sized collections, examining both efficiency and effectiveness issues. TREC 2005 is the second year for the track. The track was introduced as part of TREC 2004, with a single adhoc retrieval task. That year, 17 groups submitted 70 runs in total. This year, the track consisted of three experimental tasks: an adhoc retrieval task, an efficiency task and a named page finding task. 18 groups submitted runs to the adhoc retrieval task, 13 groups submitted runs to the efficiency task, and 13 groups submitted runs to the named page finding task. This report provides an overview of each task, summarizes the results and discusses directions for the future. Further background information on the development of the track can be found in last year's track report [4].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeSS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeSS05,
		author = {Charles L. A. Clarke and Falk Scholer and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {TREC} 2005 Terabyte Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/TERABYTE.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeSS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Efficiency vs. Effectiveness in Terabyte-Scale Information Retrieval

_Stefan Büttcher, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo.clarke](./participants.md#uwaterloo.clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uwaterloo-tera.pdf](http://trec.nist.gov/pubs/trec14/papers/uwaterloo-tera.pdf)
- :material-file-search: **Runs:** [uwmtEwteD00](./runs.md#uwmtewted00) | [uwmtEwtePTP](./runs.md#uwmtewteptp) | [uwmtEwteD10](./runs.md#uwmtewted10) | [uwmtEwteD02](./runs.md#uwmtewted02) | [uwmtEwtaPt](./runs.md#uwmtewtapt) | [uwmtEwtaPtdn](./runs.md#uwmtewtaptdn) | [uwmtEwtaD00t](./runs.md#uwmtewtad00t) | [uwmtEwtaD02t](./runs.md#uwmtewtad02t) | [uwmtEwtnpDpr](./runs.md#uwmtewtnpdpr) | [uwmtEwtnpD](./runs.md#uwmtewtnpd) | [uwmtEwtnpP](./runs.md#uwmtewtnpp) | [uwmtEwtnpPpr](./runs.md#uwmtewtnpppr)

??? abstract "Abstract"
	
	We describe indexing and retrieval techniques that are suited to perform terabyte-scale information retrieval tasks on a standard desktop PC. Starting from an Okapi-BM25-based default baseline retrieval function, we explore both sides of the effectiveness spectrum. On one side, we show how term proximity can be integrated into the scoring function in order to improve the search results. On the other side, we show how index pruning can be employed to increase retrieval efficiency - at the cost of reduced retrieval effectiveness. We show that, although index pruning can harm the quality of the search results considerably, according to standard evaluation measures, the actual loss of precision, according to other measures that are more realistic for the given task, is rather small and is in most cases outweighed by the immense efficiency gains that come along with it.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ButtcherC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ButtcherC05,
		author = {Stefan B{\"{u}}ttcher and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Efficiency vs. Effectiveness in Terabyte-Scale Information Retrieval},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uwaterloo-tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ButtcherC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Indri at TREC 2005: Terabyte Track

_Donald Metzler, Trevor Strohman, Yun Zhou, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umass-tera.pdf](http://trec.nist.gov/pubs/trec14/papers/umass-tera.pdf)
- :material-file-search: **Runs:** [indri05Eql](./runs.md#indri05eql) | [indri05EqlD](./runs.md#indri05eqld) | [indri05Aql](./runs.md#indri05aql) | [indri05Adm](./runs.md#indri05adm) | [indri05AdmfS](./runs.md#indri05admfs) | [indri05AdmfL](./runs.md#indri05admfl) | [indri05Nmpsd](./runs.md#indri05nmpsd) | [indri05Nf](./runs.md#indri05nf) | [indri05Nmp](./runs.md#indri05nmp)

??? abstract "Abstract"
	
	This work details the experiments carried out using the Indri search engine during the TREC 2005 Terabyte Track. Results are presented for each of the three tasks, including efficiency, ad hoc, and named page finding. Our efficiency runs focused on query optimization techniques, our ad hoc runs look at the importance of term proximity and document quality, and our named-page finding runs investigate the use of document priors and document structure.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MetzlerSZC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MetzlerSZC05,
		author = {Donald Metzler and Trevor Strohman and Yun Zhou and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Indri at {TREC} 2005: Terabyte Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umass-tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MetzlerSZC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melbourne University 2005: Enterprise and Terabyte Tasks

_Vo Ngoc Anh, William Webber, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [umelbourne.anh](./participants.md#umelbourne.anh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umelbourne.ent.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/umelbourne.ent.tera.pdf)
- :material-file-search: **Runs:** [MU05TBy4](./runs.md#mu05tby4) | [MU05TBy2](./runs.md#mu05tby2) | [MU05TBy1](./runs.md#mu05tby1) | [MU05TBy3](./runs.md#mu05tby3) | [MU05TBa1](./runs.md#mu05tba1) | [MU05TBa2](./runs.md#mu05tba2) | [MU05TBa3](./runs.md#mu05tba3) | [MU05TBa4](./runs.md#mu05tba4)

??? abstract "Abstract"
	
	This report describes the work done at The University of Melbourne for the TREC-2005 Enterprise and Terabyte Tracks. In the Enterprise Track, we participated in the Discussion Task. We tried a number of different methods to make use of special features of mailing lists to improve retrieval effectiveness, and found the use of thread context to be promising. In the Terabyte Track, we continued our work with impact-based ranking and sought to reduce indexing as well as query time. A new retrieval system has been developed for this purpose and has shown several improvements over our system from last year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnhWM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnhWM05,
		author = {Vo Ngoc Anh and William Webber and Alistair Moffat},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Melbourne University 2005: Enterprise and Terabyte Tasks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umelbourne.ent.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnhWM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IXE at the TREC 2005 Terabyte Task

_Giuseppe Attardi_

- :fontawesome-solid-user-group: **Participant:** [upisa.attardi](./participants.md#upisa.attardi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/upisa.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/upisa.tera.pdf)
- :material-file-search: **Runs:** [pisaEff3](./runs.md#pisaeff3) | [pisaEff4](./runs.md#pisaeff4) | [pisaEff2](./runs.md#pisaeff2) | [pisaTTitProx](./runs.md#pisattitprox) | [pisaTLonProx](./runs.md#pisatlonprox) | [pisaTLonPrxA](./runs.md#pisatlonprxa) | [pisaTLonPrxC](./runs.md#pisatlonprxc) | [pisaTNp](./runs.md#pisatnp) | [pisaTNpProx](./runs.md#pisatnpprox) | [pisaTNpProxC](./runs.md#pisatnpproxc)

??? abstract "Abstract"
	
	The TREC Terabyte task provides an opportunity to analyze scalability issues in document retrieval systems. I describe how to overcome some of these issues and in particular improvements to the IXE search engine in order to achieve higher precision while maintaining good retrieval performance. A new algorithm has been introduced to handle OR queries efficiently. A proximity factor is also computed and added to the relevance score obtained by the PL2 document weighting model: several experiments have been performed to tune its parameters. By tuning also other parameters used in relevance ranking, IXE achieved second best overall P@10 score, combined with the fastest reported retrieval speed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Attardi05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Attardi05,
		author = {Giuseppe Attardi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IXE} at the {TREC} 2005 Terabyte Task},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/upisa.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Attardi05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2005: Terabyte and Robust Track

_Yaniv Bernstein, Bodo Billerbeck, Steven Garcia, Nicholas Lester, Falk Scholer, Justin Zobel, William Webber_

- :fontawesome-solid-user-group: **Participant:** [rmit.scholer](./participants.md#rmit.scholer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/rmit-falk.tera.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/rmit-falk.tera.robust.pdf)
- :material-file-search: **Runs:** [zetdir](./runs.md#zetdir) | [zetdist](./runs.md#zetdist) | [zetdirhoc](./runs.md#zetdirhoc) | [zetdirA](./runs.md#zetdira) | [zetnp](./runs.md#zetnp) | [zetnpancfuzz](./runs.md#zetnpancfuzz) | [zetnpanc](./runs.md#zetnpanc) | [zetnp50w](./runs.md#zetnp50w)

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

#### MG4J at TREC 2005

_Paolo Boldi, Sebastiano Vigna_

- :fontawesome-solid-user-group: **Participant:** [umilano.vigna](./participants.md#umilano.vigna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/unimi.vigna.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/unimi.vigna.tera.pdf)
- :material-file-search: **Runs:** [mg4jeff](./runs.md#mg4jeff) | [adhocmg4j](./runs.md#adhocmg4j)

??? abstract "Abstract"
	
	MG4J participated in two tracks of TREC 2005 — the ad hoc task and the efficiency task of the Terabyte Track (find all the relevant documents with high precision from 25.2 million pages from the .gov domain). It was the first time the MG4J group participated to TREC, and we concentrated our efforts on the ad hoc task, using a combination of techniques based on a new multi-index minimal-interval semantics and PageRank.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoldiV05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoldiV05,
		author = {Paolo Boldi and Sebastiano Vigna},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{MG4J} at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/unimi.vigna.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoldiV05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Looking at Limits and Tradeoffs: Sabir Research at TREC 2005

_Chris Buckley_

- :fontawesome-solid-user-group: **Participant:** [sabir.buckley](./participants.md#sabir.buckley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/sabir.tera.robust.qa.pdf)
- :material-file-search: **Runs:** [sabtb05ef1](./runs.md#sabtb05ef1) | [sab05tbt](./runs.md#sab05tbt) | [sab05tball](./runs.md#sab05tball) | [sab05tbas](./runs.md#sab05tbas)

??? abstract "Abstract"
	
	Sabir Research participated in TREC-2005 in the Terabyte, Robust, and document retrieval part of the Question Answering tracks. This writeup focuses on the Robust track, and in particular on a “routing” run that took advantage of relevance judgements for the topics on the old trec V45 collection to construct queries for the new Aquaint collection. The smart_retro tool is described which given a query and the set of relevant documents, constructs an optimally weighted version of the query. smart_retro is also used to examine the differences in difficulty between the V45 and Aquaint collections (the Aquaint collection is considerably easier). The final part of the paper describes the compression algorithms and tradeoffs that were used in both TREC 2004 and 2005. These were presented in the TREC 2004 speaker session, but never formally written up. The hardware used for all runs was a single commodity PC with a total cost of $1600: $540 for a Dell PC, $520 for four 250 GByte disks, and $500 to bring the memory up to 2.5 GBytes. The information retrieval software used was the research version of SMART 15.0. SMART was originally developed in the early 1960's by Gerard Salton and since then has continued to be a leading research information retrieval tool. It continues to use a statistical vector space model, with stemming, stop words, weighting, inner product similarity function, and ranked retrieval.
	

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

#### Logistic Regression Merging of Amberfish and Lucene Multisearch Results

_Christopher T. Fallen, Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [arsc.newby](./participants.md#arsc.newby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ualaska.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/ualaska.tera.pdf)
- :material-file-search: **Runs:** [ctfluc1](./runs.md#ctfluc1) | [ctfadhocaf1](./runs.md#ctfadhocaf1) | [ctfadhocluc1](./runs.md#ctfadhocluc1) | [ctfm1](./runs.md#ctfm1) | [ctfm2](./runs.md#ctfm2) | [ctflnp1](./runs.md#ctflnp1)

??? abstract "Abstract"
	
	A simple logistic-regression based isolated data fusion algorithm was used to merge results from two free open-source text retrieval tools. The algorithm is described and results from each search tool are compared against the merged results and against each other. Basic performance measures are reported and discussed, and future projects are outlined.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FallenN05.bib) "
	```
	@inproceedings{DBLP:conf/trec/FallenN05,
		author = {Christopher T. Fallen and Gregory B. Newby},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Logistic Regression Merging of Amberfish and Lucene Multisearch Results},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ualaska.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FallenN05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Dublin City University at the TREC 2005 Terabyte Track

_Paul Ferguson, Cathal Gurrin, Alan F. Smeaton, Peter Wilkins_

- :fontawesome-solid-user-group: **Participant:** [dublincityu.gurrin](./participants.md#dublincityu.gurrin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/dublincu.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/dublincu.tera.pdf)
- :material-file-search: **Runs:** [DCU05DISTWTF](./runs.md#dcu05distwtf) | [DCU05DISTDID](./runs.md#dcu05distdid) | [DCU05WTF](./runs.md#dcu05wtf) | [DCU05WTFQ](./runs.md#dcu05wtfq) | [DCU05AWTF](./runs.md#dcu05awtf) | [DCU05ADID](./runs.md#dcu05adid) | [DCU05ACOMBO](./runs.md#dcu05acombo) | [DCU05ABM25](./runs.md#dcu05abm25) | [DCU05NPWTF](./runs.md#dcu05npwtf) | [DCU05NPBM25](./runs.md#dcu05npbm25) | [DCU05NPDID](./runs.md#dcu05npdid) | [DCU05NPCOMBO](./runs.md#dcu05npcombo)

??? abstract "Abstract"
	
	For the 2005 Terabyte track in TREC Dublin City University participated in all three tasks: Adhoc, Efficiency and Named Page Finding. Our runs for TREC in all tasks were primarily focussed on the application of “Top Subset Retrieval” to the Terabyte Track. This retrieval utilises different types of sorted inverted indices so that less documents are processed in order to reduce query times, and is done so in a way that minimises loss of effectiveness in terms of query precision. We also compare a distributed version of our F´ısr´eal search system [1][2] against the same system deployed on a single machine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FergusonGSW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/FergusonGSW05,
		author = {Paul Ferguson and Cathal Gurrin and Alan F. Smeaton and Peter Wilkins},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Dublin City University at the {TREC} 2005 Terabyte Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/dublincu.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FergusonGSW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### National Taiwan University at Terabyte Track of TREC 2005

_Ming-Hung Hsu, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ntu.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/ntu.tera.pdf)
- :material-file-search: **Runs:** [NTUET1](./runs.md#ntuet1) | [NTUET2](./runs.md#ntuet2) | [NTUAH1](./runs.md#ntuah1) | [NTUAH2](./runs.md#ntuah2) | [NTUAH3](./runs.md#ntuah3) | [NTUAH4](./runs.md#ntuah4) | [NTUNF1](./runs.md#ntunf1) | [NTUNF2](./runs.md#ntunf2) | [NTUNF4](./runs.md#ntunf4) | [NTUNF3](./runs.md#ntunf3)

??? abstract "Abstract"
	
	There are three tasks in the Terabyte track of TREC 2005, i.e. Efficiency, Ad hoc and Named page finding. We participated in all the tasks and use different retrieval methods to deal with each task, aiming to vary the retrieval method according to the different characteristics of different tasks. In Ah hoc task, we adopt the technique of query-specific clustering. In Named page finding task, we cared more about the information of document title and anchor text of out-links.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HsuC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HsuC05,
		author = {Ming{-}Hung Hsu and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {National Taiwan University at Terabyte Track of {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ntu.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HsuC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Effective Smoothing for a Terabyte of Text

_Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.mueller](./participants.md#uamsterdam.mueller)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uamsterdam.tera.kamps.pdf](http://trec.nist.gov/pubs/trec14/papers/uamsterdam.tera.kamps.pdf)
- :material-file-search: **Runs:** [UAmsT05aTeLM](./runs.md#uamst05atelm) | [UAmsT05aTeVS](./runs.md#uamst05atevs) | [UAmsT05n3SUM](./runs.md#uamst05n3sum) | [UAmsT05nTeLM](./runs.md#uamst05ntelm) | [UAmsT05nTurl](./runs.md#uamst05nturl) | [UAmsT05nTind](./runs.md#uamst05ntind)

??? abstract "Abstract"
	
	As part of the TREC 2005 Terabyte track, we conducted a range of experiments investigating the effects of larger collections. Our main findings can be summarized as follows. First, we tested whether our retrieval system scales up to terabyte-scale collections. We found that our retrieval system can handle 25 million documents, although in terms of indexing time we are approaching the limits of a non-distributed retrieval system. Second, we hoped to find out whether results from earlier Web Tracks carry over to this task. For known-item search we found that, on the one hand, indegree and URL priors did not promote retrieval effectiveness, but that, on the other hand, the combination of different document representations improved retrieval effectiveness. Third, we investigated the role of smoothing for collections of this size. We found that larger collections require far less smoothing, especially for the adhoc task using very little smoothing leads to substantial gains in retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Kamps05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Kamps05,
		author = {Jaap Kamps},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Effective Smoothing for a Terabyte of Text},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uamsterdam.tera.kamps.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Kamps05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2005: Terabyte Track

_Mladen Kovacevic, Xiangji Huang_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/yorku-huang.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/yorku-huang.tera.pdf)
- :material-file-search: **Runs:** [york05tAa1](./runs.md#york05taa1) | [york05tNa1](./runs.md#york05tna1)

??? abstract "Abstract"
	
	York University participated in the terabyte track this year. Using the GOV2 collection, we used filtering techniques to shorten the amount of data to be indexed before indexing into eight partitions. As there were several different subsections of the terabyte track, we chose to participate in the ad hoc and named page retrieval runs. Our technique involved partitioned indexes across a single machine. We combined our results by first calculating the document frequency of a term across all the indexes, calculating the weight, then using the same weight in retrieving the top results from each index. This approach effectively tried to mimic the results that would be obtained if there were only one large index.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KovacevicH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/KovacevicH05,
		author = {Mladen Kovacevic and Xiangji Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2005: Terabyte Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/yorku-huang.tera.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KovacevicH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2005: Experiments in Terabyte and  Enterprise Tracks with Terrier

_Craig Macdonald, Ben He, Vassilis Plachouras, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uglasgow.ounis](./participants.md#uglasgow.ounis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uglasgow.tera.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/uglasgow.tera.ent.pdf)
- :material-file-search: **Runs:** [uogTB05SQE](./runs.md#uogtb05sqe) | [uogTB05LQEV](./runs.md#uogtb05lqev) | [uogTB05SQES](./runs.md#uogtb05sqes) | [uogTB05SQEH](./runs.md#uogtb05sqeh) | [uogNP05base](./runs.md#uognp05base) | [uogNP05bis](./runs.md#uognp05bis) | [uogNP05bisP](./runs.md#uognp05bisp) | [uogNP05baseN](./runs.md#uognp05basen)

??? abstract "Abstract"
	
	With our participation in TREC 2005, we continue experiments using Terrier, a modular and scalable Information Retrieval (IR) framework, in 4 tasks from the Terabyte and Enterprise tracks. In the Terabyte track, we investigate new Divergence From Randomness weighting models, and a novel query expansion approach that can take into account various document fields, namely content, title and anchor text. In addition, we test a new selective query expansion mechanism which determines the appropriateness of using query expansion on a per-query basis, using statistical information from a low-cost query performance predictor. In the Enterprise track, we investigate combining document fields evidence with other information occurring in an Enterprise setting. In the email known item task, we also investigate temporal and thread priors suitable for email search. In the expert search task, for each candidate, we generate profiles of expertise evidence from the W3C collection. Moreover, we propose a model for ranking these candidate profiles in response to a query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacdonaldHPO05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacdonaldHPO05,
		author = {Craig Macdonald and Ben He and Vassilis Plachouras and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2005: Experiments in Terabyte and Enterprise Tracks with Terrier},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uglasgow.tera.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacdonaldHPO05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Enterprise, QA, Robust and Terabyte Experiments with Hummingbird SearchServer  at TREC 2005

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/hummingbird.qa.robust.tera.pdf)
- :material-file-search: **Runs:** [humTE05i4](./runs.md#humte05i4) | [humTE05i4l](./runs.md#humte05i4l) | [humTE05i4ld](./runs.md#humte05i4ld) | [humTE05i5](./runs.md#humte05i5) | [humT05l](./runs.md#humt05l) | [humT05x5l](./runs.md#humt05x5l) | [humT05xl](./runs.md#humt05xl) | [humT05xle](./runs.md#humt05xle) | [humTN05dpl](./runs.md#humtn05dpl) | [humTN05pl](./runs.md#humtn05pl) | [humTN05l](./runs.md#humtn05l) | [humTN05rdpl](./runs.md#humtn05rdpl)

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

#### Queensland University of Technology at TREC 2005

_Alan Woodley, Chengye Lu, Tony Sahama, John King, Shlomo Geva_

- :fontawesome-solid-user-group: **Participant:** [queenslandu.geva](./participants.md#queenslandu.geva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/queenslandu.tera.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/queenslandu.tera.robust.pdf)
- :material-file-search: **Runs:** [QUT05TBMRel](./runs.md#qut05tbmrel) | [QUT05TBEn](./runs.md#qut05tben) | [QUT05DBEn](./runs.md#qut05dben) | [QUT05TSynEn](./runs.md#qut05tsynen)

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

#### Tianwang Search Engine at TREC 2005: Terabyte Track

_Hongfei Yan, Jingjing Li, Jiaji Zhu, Bo Peng_

- :fontawesome-solid-user-group: **Participant:** [pekingu.yan](./participants.md#pekingu.yan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/pekingu-he.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/pekingu-he.tera.pdf)
- :material-file-search: **Runs:** [TWTB05EF01](./runs.md#twtb05ef01) | [TWTB05AD01](./runs.md#twtb05ad01) | [TWTB05AD02](./runs.md#twtb05ad02) | [TWTB05NP01](./runs.md#twtb05np01) | [TWTB05NP02](./runs.md#twtb05np02) | [TWTB05NP03](./runs.md#twtb05np03)

??? abstract "Abstract"
	
	Tianwang for the first time participated in all three tasks of the Terabyte Track of TREC 2005 to explore its performance. All three tasks, including the adhoc task (find all the relevant documents with high precision ), the efficiency task (find top-20 results for each of 50k-entry queries with efficiency and scalability) and the named page finding task (sometimes search a page by name), are based on a 426GB collection of 25.2 million pages taken from the .gov Web domain (“GOV2”). In the adhoc task with 50 topics, Tianwang returned at least one relevant document in top 10 for 42 topics. In the efficiency task, Tianwang returned at least one relevant document in top 20 for 44 of the 50 quires. In the named page task with 252 topics, Tianwang returned a desired page in top 10 for 99 topics; meanwhile, it failed to find a correct one for 120 topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YanLZP05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YanLZP05,
		author = {Hongfei Yan and Jingjing Li and Jiaji Zhu and Bo Peng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Tianwang Search Engine at {TREC} 2005: Terabyte Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/pekingu-he.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YanLZP05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Juru at TREC 2005: Query Prediction in the Terabyte and the Robust  Tracks

_Elad Yom-Tov, David Carmel, Adam Darlow, Dan Pelleg, Shai Errera-Yaakov, Shai Fine_

- :fontawesome-solid-user-group: **Participant:** [ibm-haifa.carmel](./participants.md#ibm-haifa.carmel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ibm-haifa.tera.robust.pdf](http://trec.nist.gov/pubs/trec14/papers/ibm-haifa.tera.robust.pdf)
- :material-file-search: **Runs:** [JuruDF0](./runs.md#jurudf0) | [JuruDF1](./runs.md#jurudf1) | [juruFeSe](./runs.md#jurufese) | [juruFeRa](./runs.md#jurufera)

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

#### THUIR at TREC 2005 Terabyte Track

_Le Zhao, Rongwei Ceng, Min Zhang, Yijiang Jin, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [tsinghua.ma](./participants.md#tsinghua.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.tera.pdf](http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.tera.pdf)
- :material-file-search: **Runs:** [THUtb05SQWP1](./runs.md#thutb05sqwp1) | [THUtb05VQWP2](./runs.md#thutb05vqwp2) | [THUtb05LQWP1](./runs.md#thutb05lqwp1) | [THUtb05npB](./runs.md#thutb05npb) | [THUtb05npWP2](./runs.md#thutb05npwp2) | [THUtb05npW15](./runs.md#thutb05npw15)

??? abstract "Abstract"
	
	IR group of Tsinghua University this year has used its TMiner text retrieval system for indexing and retrieval of the Terabyte track ad hoc and named-page subtasks. In doing the two tasks, we used the in-link anchor texts (the anchor of the URLs that point to the current page in the collection) together with the content texts of the web pages for building the indices. When retrieving, the word-pair method [1] was used and proved effective on 2004 and 2005 Terabyte ad hoc task topics and the 2005 named-page task. We analyze the performance of word-pair method in comparison with the Markov random field term dependence model of [2] and a generative phrase model we proposed, which is natural on the language modeling framework [3].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoCZJM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoCZJM05,
		author = {Le Zhao and Rongwei Ceng and Min Zhang and Yijiang Jin and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2005 Terabyte Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoCZJM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

