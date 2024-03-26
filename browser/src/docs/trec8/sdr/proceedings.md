# Proceedings - Spoken Document Retrieval 1999 

#### The TREC Spoken Document Retrieval Track: A Success Story

_John S. Garofolo, Cedric G. P. Auzanne, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-sdr-overview.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-sdr-overview.pdf)
??? abstract "Abstract"
	
	This paper describes work within the NIST Text REtrieval Conference (TREC) over the last three years in designing and implementing evaluations of Spoken Document Retrieval (SDR) technology within a broadcast news domain. SDR involves the search and retrieval of excerpts from spoken audio recordings using a combination of automatic speech recognition and information retrieval technologies. The TREC SDR Track has provided an infrastructure for the development and evaluation of SDR technology and a common forum for the exchange of knowledge between the speech recognition and information retrieval research communities. The SDR Track can be declared a success in that it has provided objective, demonstrable proof that this technology can be successfully applied to realistic audio collections using a combination of existing technologies and that it can be objectively evaluated. The design and implementation of each of the SDR evaluations are presented and the results are summarized. Plans for the 2000 TREC SDR Track are presented and thoughts about how the track might evolve are discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarofoloAV99.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarofoloAV99,
		author = {John S. Garofolo and Cedric G. P. Auzanne and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC} Spoken Document Retrieval Track: {A} Success Story},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-sdr-overview.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GarofoloAV99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AT&T at TREC-8

_Amit Singhal, Steven P. Abney, Michiel Bacchiani, Michael Collins, Donald Hindle, Fernando C. N. Pereira_

- :fontawesome-solid-user-group: **Participant:** [ATT](./participants.md#att)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf](http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf)
- :material-file-search: **Runs:** [att-r1](./runs.md#att-r1) | [att-b1](./runs.md#att-b1) | [att-s1](./runs.md#att-s1) | [att-s2](./runs.md#att-s2) | [att-cr-cmus1](./runs.md#att-cr-cmus1) | [att-cr-cuhtks1](./runs.md#att-cr-cuhtks1) | [att-cr-cuhtks1p1](./runs.md#att-cr-cuhtks1p1) | [att-cr-limsis1](./runs.md#att-cr-limsis1) | [att-cr-shefs1](./runs.md#att-cr-shefs1)

??? abstract "Abstract"
	
	In 1999, AT&T participated in the ad-hoc task and the Question Answering (QA), Spoken Document Retrieval (SDR), and Web tracks. Most of our effort for TREC-8 focused on the QA and SDR tracks. Results from SDR track show that our document expansion techniques, presented in [8, 9], are very effective for speech retrieval. The results for question answering are also encouraging. Our system designed in a relatively short period for this task can find the correct answer for about 45% of the user questions. This is specially good given the fact that our system extracts only a short phrase as an answer.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinghalABCHP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinghalABCHP99,
		author = {Amit Singhal and Steven P. Abney and Michiel Bacchiani and Michael Collins and Donald Hindle and Fernando C. N. Pereira},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {AT{\&}T at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SinghalABCHP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CMU Spoken Document Retrieval in Trec-8: Analysis of the role of  Term Frequency TF

_Matthew Siegler, Rong Jin, Alexander G. Hauptmann_

- :fontawesome-solid-user-group: **Participant:** [cmu](./participants.md#cmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-cmusdr.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-cmusdr.pdf)
- :material-file-search: **Runs:** [cmu-s1](./runs.md#cmu-s1) | [cmu-b1](./runs.md#cmu-b1) | [cmu-r1](./runs.md#cmu-r1) | [cmu-s2](./runs.md#cmu-s2)

??? abstract "Abstract"
	
	The participation of Carnegie Mellon University in the TREC-8 Spoken Document Retrieval Track used the basic same Sphinx speech recognition system as in TREC-7. Due to some unfortunate defaults in the parameter setup files, the speech recognizer did not perform in a reasonable manner. We will not analyze the results of the speech recognizer runs, as we believe the results contained abnormal types of errors, and insights or improvements on these errors would not generalize. A thorough examination of the speech recognition condition is given in [3]. However, we did evaluate a slightly modified weighting scheme in the reference (R1) and baseline (B1) conditions, which is described below.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SieglerJH99.bib) "
	```
	@inproceedings{DBLP:conf/trec/SieglerJH99,
		author = {Matthew Siegler and Rong Jin and Alexander G. Hauptmann},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CMU} Spoken Document Retrieval in Trec-8: Analysis of the role of Term Frequency {TF}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-cmusdr.pdf},
		timestamp = {Thu, 16 Dec 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SieglerJH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Twenty-One at TREC-8: using Language Technology for Information  Retrieval

_Wessel Kraaij, Renée Pohlmann, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [twentyone](./participants.md#twentyone)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf](http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf)
- :material-file-search: **Runs:** [tno8b-b1-limsi](./runs.md#tno8b-b1-limsi) | [tno8b-r1-limsi](./runs.md#tno8b-r1-limsi) | [tno8b-s1-limsi](./runs.md#tno8b-s1-limsi) | [tno8b-b1u-limsi](./runs.md#tno8b-b1u-limsi) | [tno8b-s1u-limsi](./runs.md#tno8b-s1u-limsi)

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

#### Spoken Document Retrieval for TREC-8 at Cambridge University

_Sue E. Johnson, Philip C. Woodland, Karen Sparck Jones, Pierre Jourlin_

- :fontawesome-solid-user-group: **Participant:** [cambridge](./participants.md#cambridge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/cuhtk-sdr-paper.pdf](http://trec.nist.gov/pubs/trec8/papers/cuhtk-sdr-paper.pdf)
- :material-file-search: **Runs:** [cuhtk-r1](./runs.md#cuhtk-r1) | [cuhtk-b1](./runs.md#cuhtk-b1) | [cuhtk-s1](./runs.md#cuhtk-s1) | [cuhtk-b1u](./runs.md#cuhtk-b1u) | [cuhtk-s1u](./runs.md#cuhtk-s1u) | [cuhtk-s1p1u](./runs.md#cuhtk-s1p1u) | [cuhtk-s1p1](./runs.md#cuhtk-s1p1) | [cuhtk-cru-nist-b2](./runs.md#cuhtk-cru-nist-b2) | [cuhtk-cru-limsi-s1](./runs.md#cuhtk-cru-limsi-s1) | [cuhtk-cru-shef-s1](./runs.md#cuhtk-cru-shef-s1) | [cuhtk-cr-att-s1](./runs.md#cuhtk-cr-att-s1) | [cuhtk-cr-cmu-s1](./runs.md#cuhtk-cr-cmu-s1) | [cuhtk-cr-shef-s1](./runs.md#cuhtk-cr-shef-s1) | [cuhtk-cr-b2](./runs.md#cuhtk-cr-b2) | [cuhtk-cr-limsi-s1](./runs.md#cuhtk-cr-limsi-s1)

??? abstract "Abstract"
	
	This paper presents work done at Cambridge University on the TREC-8 Spoken Document Retrieval (SDR) Track. The 500 hours of broadcast news audio was filtered using an automatic scheme for detecting commercials, and then transcribed using a 2-pass HTK speech recogniser which ran at 13 times real time. The system gave an overall word error rate of 20.5% on the 10 hour scored subset of the corpus, the lowest in the track. Our retrieval engine used an Okapi scheme with traditional stopping and Porter stemming, enhanced with part-of-speech weighting on query terms, a stemmer exceptions list, semantic 'poset' in-dexing, parallel collection frequency weighting, both parallel and traditional blind relevance feedback and document expansion using parallel blind relevance feedback. The final system gave an Average Precision of 55.29% on our transcriptions. For the case where story boundaries are unknown, a similar retrieval system, without the document expansion, was run on a set of 'stories' derived from windowing the transcriptions after removal of commercials. Boundaries were forced at 'commercial' or 'music' changes and some recombination of temporally close stories was allowed after retrieval. When scoring duplicate story hits and commercials as irrelevant, this system gave an Average Precision of 41.47% on our transcriptions. The paper also presents results for cross-recogniser experiments using our retrieval strategies on transcriptions from our own first pass output, AT&T, CMU, 2 NIST-run BBN baselines, LIMSI and Sheffield University, and the relationship between performance and transcription error rate is shown.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JohnsonWJJ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/JohnsonWJJ99,
		author = {Sue E. Johnson and Philip C. Woodland and Karen Sparck Jones and Pierre Jourlin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Spoken Document Retrieval for {TREC-8} at Cambridge University},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/cuhtk-sdr-paper.pdf},
		timestamp = {Wed, 05 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JohnsonWJJ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Experiments at SUNY Buffalo

_Benjamin Han, Ramya Nagarajan, Rohini K. Srihari, Srikanth Munirathnam_

- :fontawesome-solid-user-group: **Participant:** [buffalo](./participants.md#buffalo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ub-nbpaper.pdf](http://trec.nist.gov/pubs/trec8/papers/ub-nbpaper.pdf)
- :material-file-search: **Runs:** [cedar-r1](./runs.md#cedar-r1) | [cedar-b1](./runs.md#cedar-b1)

??? abstract "Abstract"
	
	For TREC-8, State University of New York at Buffalo(UB) participated in the ad-hoe task and the spoken document retrieval(SDR) track. This is our first year of participation at TREC. We submitted two runs for the Ad-hoc task. The first run was term vector-based using SMART[10]. The second run used the TROVE - Text Retrieval using Object VEctors - system. For the SDR Track, we participated in the IR component of the Quasi-SDR task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HanNSM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HanNSM99,
		author = {Benjamin Han and Ramya Nagarajan and Rohini K. Srihari and Srikanth Munirathnam},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Experiments at {SUNY} Buffalo},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ub-nbpaper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HanNSM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The LIMSI SDR System for TREC-8

_Jean-Luc Gauvain, Yannick de Kercadio, Lori Lamel, Gilles Adda_

- :fontawesome-solid-user-group: **Participant:** [limsi-tlp](./participants.md#limsi-tlp)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/limsi-tlp.pdf](http://trec.nist.gov/pubs/trec8/papers/limsi-tlp.pdf)
- :material-file-search: **Runs:** [limsi-b1](./runs.md#limsi-b1) | [limsi-r1](./runs.md#limsi-r1) | [limsi-s1](./runs.md#limsi-s1) | [limsi-b2](./runs.md#limsi-b2) | [limsi-cr-att1](./runs.md#limsi-cr-att1) | [limsi-cr-cmu1](./runs.md#limsi-cr-cmu1) | [limsi-cr-cuhtk1](./runs.md#limsi-cr-cuhtk1) | [limsi-cr-shef1](./runs.md#limsi-cr-shef1)

??? abstract "Abstract"
	
	In this paper we report on our TREC-8 SDR system, which combines an adapted version of the LIMSI 1998 Hub-4E transcription system for speech recognition with an IR system based on the Okapi term weighting function. Experimental results are given in terms of word error rate and average precision for both the SDR’98 and SDR’99 data sets. In addition to the Okapi approach, we also investiged a Markovian approach, which although not used in the TREC-8 evaluation, yields comparable results. The evaluation system obtained an average precision of 0.5411 on the reference transcriptions and of 0.5072 on the automatic transcriptions. The word error rate measured on a 10 hour subset is of 21.5%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GauvainKLA99.bib) "
	```
	@inproceedings{DBLP:conf/trec/GauvainKLA99,
		author = {Jean{-}Luc Gauvain and Yannick de Kercadio and Lori Lamel and Gilles Adda},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {LIMSI} {SDR} System for {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/limsi-tlp.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GauvainKLA99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The RMIT/CSIRO Ad Hoc, Q&A, Web, Interactive, and Speech Experiments  at TREC 8

_Michael Fuller, Marcin Kaszkiel, Sam Kimberley, Corinna Ng, Ross Wilkinson, Mingfang Wu, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [rmit](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf](http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf)
- :material-file-search: **Runs:** [mds08-b1](./runs.md#mds08-b1) | [mds08-r1](./runs.md#mds08-r1)

??? abstract "Abstract"
	
	Two runs were submitted for this year's Quasi-SDR runs. The word-based documents were first translated to phonemes using a text-to-phoneme algorithm. We assumed that there is a certain level of word recognition error for each type of tran-scription. Given this, we utilised a passage retrieval technique to perform the retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/FullerKKNWWZ99,
		author = {Michael Fuller and Marcin Kaszkiel and Sam Kimberley and Corinna Ng and Ross Wilkinson and Mingfang Wu and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {RMIT/CSIRO} Ad Hoc, Q{\&}A, Web, Interactive, and Speech Experiments at {TREC} 8},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FullerKKNWWZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad hoc, Cross-language and Spoken Document Information Retrieval at  IBM

_Martin Franz, J. Scott McCarley, Todd Ward_

- :fontawesome-solid-user-group: **Participant:** [ibm-franz](./participants.md#ibm-franz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/t8_ibm_hlt.pdf](http://trec.nist.gov/pubs/trec8/papers/t8_ibm_hlt.pdf)
- :material-file-search: **Runs:** [ibms-r1](./runs.md#ibms-r1) | [ibms-b1](./runs.md#ibms-b1)

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

#### INQUERY and TREC-8

_James Allan, James P. Callan, Fangfang Feng, Daniella Malin_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf)
- :material-file-search: **Runs:** [umass-r1](./runs.md#umass-r1) | [umass-b1](./runs.md#umass-b1)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CI IR) at the University of Massachusetts participated in seven of the tracks: ad-ho c, ltering, sp oken do cument retrieval, small web, large web, question and answer, and the query tracks. We sp ent signi cant time working on the ltering track, resulting in substantial p erformance improvement over TREC-7. For all of the other tracks, we used essentially the same system as used in previous years. In the next section, we describ e some of the basic pro cessing that was applied across most of the tracks. We then describe the details for each of the tracks and in some cases present some mo dest analysis of the e ectiveness of our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCFM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCFM99,
		author = {James Allan and James P. Callan and Fangfang Feng and Daniella Malin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} and {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanCFM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The THISL SDR System At TREC-8

_Dave Abberley, Steve Renals, Dan Ellis, Anthony J. Robinson_

- :fontawesome-solid-user-group: **Participant:** [thisl](./participants.md#thisl)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/shef-proc-trec8.pdf](http://trec.nist.gov/pubs/trec8/papers/shef-proc-trec8.pdf)
- :material-file-search: **Runs:** [shef-r1](./runs.md#shef-r1) | [shef-b1](./runs.md#shef-b1) | [shef-b1u](./runs.md#shef-b1u) | [shef-s1](./runs.md#shef-s1) | [shef-s1u](./runs.md#shef-s1u) | [shef-cr-att-s1](./runs.md#shef-cr-att-s1) | [shef-cr-cmu-s1](./runs.md#shef-cr-cmu-s1) | [shef-cr-cuhtk-s1](./runs.md#shef-cr-cuhtk-s1) | [shef-cr-cuhtk-s1p1](./runs.md#shef-cr-cuhtk-s1p1) | [shef-cr-limsi-s1](./runs.md#shef-cr-limsi-s1) | [shef-cr-nist-b2](./runs.md#shef-cr-nist-b2) | [shef-cru-cuhtk-s1p1u](./runs.md#shef-cru-cuhtk-s1p1u) | [shef-cru-limsi-s1u](./runs.md#shef-cru-limsi-s1u) | [shef-cru-cuhtk-s1u](./runs.md#shef-cru-cuhtk-s1u) | [shef-cru-nist-b2u](./runs.md#shef-cru-nist-b2u)

??? abstract "Abstract"
	
	This paper describes the participation of the THISL group at the TREC-8 Spoken Document Retrieval (SDR) track. The THISL SDR system consists of the realtime version of the A BBOT large vocabulary speech recognition system and the THISL IR text retrieval system. The TREC-8 evaluation assessed SDR performance on a corpus of 500 hours of broadcast news material collected over a five month period. The main test condition involved retrieval of stories defined by manual segmentation of the corpus in which non-news material, such as commercials, were excluded. An optional test condition required required retrieval of the same stories from the unsegmented audio stream. The THISL SDR system participated at both test conditions. The results show that a system such as THISL can produce respectable information retrieval performance on a realistically-sized corpus of unsegmented audio material.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbberleyRER99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbberleyRER99,
		author = {Dave Abberley and Steve Renals and Dan Ellis and Anthony J. Robinson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {THISL} {SDR} System At {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/shef-proc-trec8.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbberleyRER99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

