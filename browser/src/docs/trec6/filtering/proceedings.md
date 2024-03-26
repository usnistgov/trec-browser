# Proceedings - Filtering 1997 

#### The TREC-6 Filtering Track: Description and Analysis

_David A. Hull_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/filter.track.ps.gz](http://trec.nist.gov/pubs/trec6/papers/filter.track.ps.gz)
??? abstract "Abstract"
	
	This article details the experiments conducted in the TREC-6 filtering track. The filtering track is an extension of the routing track which adds time sequencing of the document stream and set-based evaluation strategies which simulate immediate distribution of the retrieved doc-uments. It also introduces an adaptive filtering subtrack which is designed to simulate on-line or sequential filtering of documents. In addition to motivating the task and describing the practical details of participating in the track, this document includes a detailed graphical presentation of the experimental results and attempts to analyze and explain the observed patterns. The final section suggests some ways to extend the current research in future experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Hull97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Hull97,
		author = {David A. Hull},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-6} Filtering Track: Description and Analysis},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {45--68},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/filter.track.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Hull97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi at TREC-6 Automatic ad hoc, VLC, routing, filtering and QSDR

_Steve Walker, Stephen E. Robertson, Mohand Boughanem, Gareth J. F. Jones, Karen Sparck Jones_

- :fontawesome-solid-user-group: **Participant:** [City](./participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz](http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz)
- :material-file-search: **Runs:** [city6f21](./runs.md#city6f21) | [city6f22](./runs.md#city6f22) | [city6f23](./runs.md#city6f23) | [city6f11](./runs.md#city6f11) | [city6f12](./runs.md#city6f12) | [city6f13](./runs.md#city6f13)

??? abstract "Abstract"
	
	The filtering work was essentially only a small extension of the routing task effort. The pool of merged routing queries was used, but query selection was based on maximizing (over the training data) each of the utility functions for each topic. Two triples of runs were submitted. Both these sets compared very favourably with other participants' results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WalkerRBJJ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/WalkerRBJJ97,
		author = {Steve Walker and Stephen E. Robertson and Mohand Boughanem and Gareth J. F. Jones and Karen Sparck Jones},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Okapi at {TREC-6} Automatic ad hoc, VLC, routing, filtering and {QSDR}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {125--136},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/city\_proc\_auto.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WalkerRBJJ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Context-Based Statistical Sub-Spaces

_Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [UNC-N](./participants.md#unc-n)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/newby-t6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/newby-t6.ps.gz)
- :material-file-search: **Runs:** [isf1](./runs.md#isf1) | [isf1r](./runs.md#isf1r) | [isf2](./runs.md#isf2) | [isf2r](./runs.md#isf2r)

??? abstract "Abstract"
	
	The technique described in this paper is similar to latent semantic indexing (LSI), although with some variation. Whereas LSI operates by performing a singular value decomposition (SVD) on a large term by document matrix of co-occurrence scores, the technique here operates by identifying eigenvectors and eigenvalues of a term by term matrix of correlation scores (derived from co-occurrence scores). The technique of identifying eigenvectors and eigenvalues from a correlation matrix is known as principal components analysis (PCA). Variations from the previous year's TREC work include work using sub-documents (paragraphs), and working with small sub-matrices consisting only of terms in a query, rather than working with all terms from the collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Newby97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Newby97,
		author = {Gregory B. Newby},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Context-Based Statistical Sub-Spaces},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {735--745},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/newby-t6.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Newby97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ANU/ACSys TREC-6 Experiments

_David Hawking, Paul B. Thistlewaite, Nick Craswell_

- :fontawesome-solid-user-group: **Participant:** [ANU](./participants.md#anu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz](http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz)
- :material-file-search: **Runs:** [anu6fltU1](./runs.md#anu6fltu1) | [anu6fltU2](./runs.md#anu6fltu2)

??? abstract "Abstract"
	
	A number of experiments conducted within the framework of the TREC-6 conference and using a completely re-engineered version of the PArallel Document Retrieval Engine (PADRE97) are reported. Passage-based pseudo relevance feedback combined with a variant of City University's Okapi BM25 scoring function achieved best average precision, best recall and best precision@20 in the Long-topic Automatic Adhoc category. The same basic method was used as the basis for successful submissions in the Manual Adhoc, Filtering and VLC tasks. A new BM25-based method of scoring concept intersections was shown to produce a small but significant gain in precision on the Manual Adhoc task while the relevance feedback scheme produced a significant improvement in recall for all of the Adhoc query sets to which it was applied.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingTC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingTC97,
		author = {David Hawking and Paul B. Thistlewaite and Nick Craswell},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ANU/ACSys {TREC-6} Experiments},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {275--290},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HawkingTC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The text categorization system TEKLIS at TREC-6

_Thomas Brückner_

- :fontawesome-solid-user-group: **Participant:** [Siemens](./participants.md#siemens)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/siemens.ps.gz](http://trec.nist.gov/pubs/trec6/papers/siemens.ps.gz)
- :material-file-search: **Runs:** [teklis1000](./runs.md#teklis1000) | [teklis6](./runs.md#teklis6) | [teklis65](./runs.md#teklis65) | [teklis7](./runs.md#teklis7) | [teklis75](./runs.md#teklis75)

??? abstract "Abstract"
	
	This short paper documents our participation on the filtering and routing tasks of TREC-6 with the commercial filtering system TEKLIS. TEKLIS is a training-based statistical categorization system which incorporates shallow linguistic processing and fuzzy-set methods. In the following we will present the core technology of TEKLIS, our results on the filtering and routing tasks and a discussion of the insights we gained through our participation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bruckner97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bruckner97,
		author = {Thomas Br{\"{u}}ckner},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The text categorization system {TEKLIS} at {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {619--621},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/siemens.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Bruckner97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Daimler Benz Research: System and Experiments Routing and Filtering

_Thomas Bayer, Heike Mogg-Schneider, Ingrid Renz, Hartmut Schäfer_

- :fontawesome-solid-user-group: **Participant:** [DBenz](./participants.md#dbenz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/dbulm.ps.gz](http://trec.nist.gov/pubs/trec6/papers/dbulm.ps.gz)
- :material-file-search: **Runs:** [dbulm1fF1](./runs.md#dbulm1ff1) | [dbulm1fF2](./runs.md#dbulm1ff2) | [dbulm1Asp](./runs.md#dbulm1asp) | [dbulm1fF2R](./runs.md#dbulm1ff2r) | [dbulm1F1R](./runs.md#dbulm1f1r)

??? abstract "Abstract"
	
	The retrieval approach is based on vector representation (bag of character strings), on dimension reduction (LSI - latent semantic indexing) and on statistical machine learning techniques in all processing levels. Two phases are distinguished, the adaptation phase based on training samples (texts) and the application phase, where each text is mapped to one or more categories (classes). The adaptation process is corpus dependent and automatic and, hence, domain and language independent. The main idea of this approach is to generate different sets of simple features which represent different views to texts. For each text to be filtered/ routed, different feature vectors are generated and classified into a decision vector which contains estimates of class membership probabilities. In the following step, these decision vectors are regarded as feature vectors and fed to another classifier that combines these set of decision vectors into the final one.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BayerMRS97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BayerMRS97,
		author = {Thomas Bayer and Heike Mogg{-}Schneider and Ingrid Renz and Hartmut Sch{\"{a}}fer},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Daimler Benz Research: System and Experiments Routing and Filtering},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {329--346},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/dbulm.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BayerMRS97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY Does Battle With TREC-6

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, Donald Byrd, Russell C. Swan, Jinxi Xu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [INQ415](./runs.md#inq415) | [INQ416](./runs.md#inq416) | [INQ417](./runs.md#inq417) | [INQ418](./runs.md#inq418) | [INQ419](./runs.md#inq419) | [INQ420](./runs.md#inq420) | [INQ421](./runs.md#inq421) | [INQ422](./runs.md#inq422) | [INQ423](./runs.md#inq423) | [INQ424](./runs.md#inq424)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in eight of the ten tracks that were part of the TREC-6 workshop. We started with the two required tracks, ad-hoc and routing, but then included VLC, Filtering, Chinese, Cross-language, SDR, and Interactive. We omitted NLP and High Precision for want of time and energy. With so many tracks involved, it is nearly inevitable that something will go wrong. Despite our best efforts at verifying all aspects of each track-before, during, and after the experiments we once again made mistakes that were minor in scope, but major in consequence. Those mistakes affected our results in Ad-hoc and Routing, as well as the dependent tracks of VLC and Filtering. The details of the mistakes are presented in each track's discussion, along with information comparing the submitted runs to the corrected runs. Unfortunately, those corrected runs are not included in TREC-6 summary information. This remainder of this report covers our approach to each of the tracks as well as some experimental results and analysis. We start with an overview of the major tools that were used across all tracks. The paper is divided into the following sections. The track descriptions are generally broken into approach, results, and analysis sections, though some tracks require a different description.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCCBBSX97.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCCBBSX97,
		author = {James Allan and James P. Callan and W. Bruce Croft and Lisa Ballesteros and Donald Byrd and Russell C. Swan and Jinxi Xu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} Does Battle With {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {169--206},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AllanCCBBSX97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

