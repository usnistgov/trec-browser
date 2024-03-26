# Proceedings - Adhoc 1997 

#### Okapi at TREC-6 Automatic ad hoc, VLC, routing, filtering and QSDR

_Steve Walker, Stephen E. Robertson, Mohand Boughanem, Gareth J. F. Jones, Karen Sparck Jones_

- :fontawesome-solid-user-group: **Participant:** [City](./participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz](http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz)
- :material-file-search: **Runs:** [city6al](./runs.md#city6al) | [city6ad](./runs.md#city6ad) | [city6at](./runs.md#city6at)

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

#### Ad hoc Retrieval Using Thresholds, WSTs for French Mono-lingual Retrieval,  Document-at-a-Glance for High Precision and Triphone Windows for Spoken  Documents

_Alan F. Smeaton, Fergus Kelledy, Gerard Quinn_

- :fontawesome-solid-user-group: **Participant:** [Dublin](./participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz](http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz)
- :material-file-search: **Runs:** [DCU97lnt](./runs.md#dcu97lnt) | [DCU97lt](./runs.md#dcu97lt) | [DCU97snt](./runs.md#dcu97snt) | [DCU97vs](./runs.md#dcu97vs)

??? abstract "Abstract"
	
	This paper describes work done by a team from Dublin City University as part of TREC-6. In this TREC exercise we completed series of runs in 4 categories. The first was the mainline ad hoc retrieval task in which we repeated our entry for TREC-5, without modification. This is based on applying various thresholds to processing a query including query term and posting list thresholds, in order to improve retrieval efficiency. As our previous work has shown, this can be done without any loss in retrieval effectiveness. Our second set of submitted runs were as part of the cross-lingual retrieval track where we ran French topics against French texts, effectively mono-lingual retrieval. What is novel about our approach is that it is based upon matching word shape tokens derived from character shape codes, rather than matching word stems or base forms. This technique is useful for retrieving from scanned document images rather than full texts and is something we are currently refining for English texts (and English queries). With those other experiments we have obtained surprisingly effective retrieval and this venture in TREC-6 was to see how effective WST-based retrieval could be for French. The third series of experiments we submitted were based on the high precision track in which we used a graphical representation of a ranked list of documents and the positional occurrences of search terms within those top-ranked documents, relative to each other. Our final experiments were as part of the spoken document retrieval track in which we removed the tags used for story bounds, turned transcripts and topics into a phonetic representation using a phoneme dictionary and we then retrieved story identifiers based on a triphone match between topic and fixed-width windows of triphones in the transcripts. We also applied a weighting function to triphones as they occurred in story 'windows' based on their offset within those windows.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmeatonKQ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmeatonKQ97,
		author = {Alan F. Smeaton and Fergus Kelledy and Gerard Quinn},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ad hoc Retrieval Using Thresholds, WSTs for French Mono-lingual Retrieval, Document-at-a-Glance for High Precision and Triphone Windows for Spoken Documents},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {461--475},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SmeatonKQ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Text Retrieval via Semantic Forests

_Patrick Schone, Jeffrey L. Townsend, Thomas H. Crystal, Calvin Olano_

- :fontawesome-solid-user-group: **Participant:** [NSA](./participants.md#nsa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/nsa-rev.ps.gz](http://trec.nist.gov/pubs/trec6/papers/nsa-rev.ps.gz)
- :material-file-search: **Runs:** [nsasg1](./runs.md#nsasg1) | [nsasg2](./runs.md#nsasg2)

??? abstract "Abstract"
	
	We approached our first participation in TREC with an interest in performing retrieval on the output of automatic speech-to-text (speech recognition) systems and a background in performing topic-labeling on such output. Our primary thrust, therefore, was to participate in the SDR track. In conformance with the rules, we also participated in the Ad Hoc text-retrieval task, to create a baseline for comparing our converted topic-labeling system with other approaches to IR and to assess the effect of speech-transcription errors. A second thrust was to explore rapid prototyping of an IR system, given the existing topic-labeling software. Our IR system makes use of software called Semantic Forests which is based on an algorithm originally developed for labeling topics in text and transcribed speech (Schone & Nelson, ICASSP '96). Topic-labelling is not an IR task, so Semantic Forests was adapted for use in TREC over an eight-week period for the Ad Hoc task, with an additional two weeks for SDR. In what follows, we describe our system as well as experiments, timings, results, and future directions with these techniques.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchoneTCO97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchoneTCO97,
		author = {Patrick Schone and Jeffrey L. Townsend and Thomas H. Crystal and Calvin Olano},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Text Retrieval via Semantic Forests},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {761--773},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/nsa-rev.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SchoneTCO97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Document Retrieval Using The MPS Information Server (A Report  on the TREC-6 Experiment)

_François Schiettecatte_

- :fontawesome-solid-user-group: **Participant:** [FS](./participants.md#fs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/fsconsult.ps.gz](http://trec.nist.gov/pubs/trec6/papers/fsconsult.ps.gz)
- :material-file-search: **Runs:** [fsclt6](./runs.md#fsclt6) | [fsclt6t](./runs.md#fsclt6t) | [fsclt6r](./runs.md#fsclt6r)

??? abstract "Abstract"
	
	This paper summarizes the results of the experiments conducted by FS Consulting, Inc. as part of the Six Text Retrieval Experiment Conference (TREC-6). We participated in Category C and ran the ad-hoc experiments, producingthree sets of official results (fsclt6, fscltor and fscltot), only one of which was judged (fsclt6). We also produced two sets of unofficial results as part of a database merging experiment that we ran (fscltom2 and fscltom5). Our long-term research interest is in building information retrieval systems that help users find information to solve real-world problems. Our TREC-6 participation centered on two goals: to see if automatic query reformulation' provides better results than the searcher's initial query formulation; and to continue to evaluate the effectiveness of the document scoring algorithms when searching across multiple databases located on multiple servers. Our TREC-6 ad-hoc experiments were designed around a model of an end user of information systems who is not a search professional, but one who would occasionally use a system like the MPS Information Server while seeking information in a workplace, or would be familiar with various Internet search engines such as HotBot or Alta Vista.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Schiettecatte97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Schiettecatte97,
		author = {Fran{\c{c}}ois Schiettecatte},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Document Retrieval Using The {MPS} Information Server {(A} Report on the {TREC-6} Experiment)},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {477--487},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/fsconsult.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Schiettecatte97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Verity at TREC-6: Out-of-the-Box and Beyond

_Jan O. Pedersen, Craig Silverstein, Christopher C. Vogt_

- :fontawesome-solid-user-group: **Participant:** [Verity](./participants.md#verity)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/verity-trec6-corrected.ps.gz](http://trec.nist.gov/pubs/trec6/papers/verity-trec6-corrected.ps.gz)
- :material-file-search: **Runs:** [VrtyAH6a](./runs.md#vrtyah6a) | [VrtyAH6b](./runs.md#vrtyah6b)

??? abstract "Abstract"
	
	The Verity Trec-6 entry focused on the performance of the built-in search facilities of the commercially available Verity engine and explored the impact of simple enhancements. The ad hoc results show that considerable improvements can be achieved through the application of standard and more experimental techniques. The routing results show that respectable performance can be achieved simply through careful parameter tuning.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PedersenSV97.bib) "
	```
	@inproceedings{DBLP:conf/trec/PedersenSV97,
		author = {Jan O. Pedersen and Craig Silverstein and Christopher C. Vogt},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Verity at {TREC-6:} Out-of-the-Box and Beyond},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {259--273},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/verity-trec6-corrected.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PedersenSV97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Context-Based Statistical Sub-Spaces

_Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [UNC-N](./participants.md#unc-n)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/newby-t6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/newby-t6.ps.gz)
- :material-file-search: **Runs:** [ispa1](./runs.md#ispa1) | [ispa2](./runs.md#ispa2)

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

#### Expanding Relevance Feedback in the Relational Model

_Carol Lundquist, David O. Holmes, David A. Grossman, Ophir Frieder, M. Catherine McCabe_

- :fontawesome-solid-user-group: **Participant:** [GMU](./participants.md#gmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/gmu.ps.gz](http://trec.nist.gov/pubs/trec6/papers/gmu.ps.gz)
- :material-file-search: **Runs:** [gmu97au1](./runs.md#gmu97au1) | [gmu97au2](./runs.md#gmu97au2) | [gmu97ma1](./runs.md#gmu97ma1) | [gmu97ma2](./runs.md#gmu97ma2)

??? abstract "Abstract"
	
	In TREC-6, we participated in both the automatic and manual tracks for category A. For the automatic runs, we used the short versions of the queries and enhanced our existing prototype by expanding the relevance feedback methodology to include additional term weighting methods (i.e., the typical 'ltc-lnc' or 'nidf' weights) as well as feedback term scaling. We also experimented with eliminating infrequently occurring terms to determine if the relevance ranking scores between documents and queries could be improved by eliminating certain highly weighted terms. For our manual runs, we used pre-defined concept lists with terms from the concept lists combined in different ways. We continued to use the AT&T DBC-1012 Model 4 parallel database machine as the platform for our information retrieval system which continues to be implemented in the relational database model using unchanged SQL.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LundquistHGFM97.bib) "
	```
	@inproceedings{DBLP:conf/trec/LundquistHGFM97,
		author = {Carol Lundquist and David O. Holmes and David A. Grossman and Ophir Frieder and M. Catherine McCabe},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Expanding Relevance Feedback in the Relational Model},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {489--502},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/gmu.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LundquistHGFM97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-6 English and Chinese Retrieval Experiments using PIRCS

_K. L. Kwok, Laszlo Grunfeld, J. H. Xu_

- :fontawesome-solid-user-group: **Participant:** [CUNY](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/queenst6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/queenst6.ps.gz)
- :material-file-search: **Runs:** [pirc7Aa](./runs.md#pirc7aa) | [pirc7Ad](./runs.md#pirc7ad) | [pirc7At](./runs.md#pirc7at)

??? abstract "Abstract"
	
	For Trec-6 ad-hoc experiments, we continue to use two-stage retrieval with pseudo-feedback from top-ranked un-judged documents for both Chinese and English. We perform three types of retrieval characterized by queries formed using title only, description only and all sections of the given topics. For short queries mainly derived from title or description section, query terms are weighted by average term frequency avtf introduced previously. For Chinese, we employ a combination of representation (character, bigram and short-word) strategy, returning the highest average non-interpolated precision that is even better than some manual approaches. In English ad-hoc, we try a document re-ranking strategy for the first stage retrieval based on occurrence of selected query term pairs, so as to have better result in the second stage. Performance for English ad-hoc is also highly competitive for both very short and long queries. In routing, a strategy of combining different methods of query formation and retrieval is used. These include no learning ad-hoc type queries, learning from the more current FBISS documents only, queries learnt from selecting the best set of known relevant documents based on a genetic algorithm, and queries that are trained from a back-propagation neural network with hidden nodes. Average precision results are among the best four. In addition, we also participate in high precision and the filtering track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGX97.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGX97,
		author = {K. L. Kwok and Laszlo Grunfeld and J. H. Xu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-6} English and Chinese Retrieval Experiments using {PIRCS}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {207--214},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/queenst6.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KwokGX97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSIRO Routing and Ad-Hoc Experiments at TREC-6

_Arkadi Kosmynin_

- :fontawesome-solid-user-group: **Participant:** [CSIRO](./participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/csiro.ps.gz](http://trec.nist.gov/pubs/trec6/papers/csiro.ps.gz)
- :material-file-search: **Runs:** [csiro97a1](./runs.md#csiro97a1) | [csiro97a2](./runs.md#csiro97a2) | [csiro97a3](./runs.md#csiro97a3)

??? abstract "Abstract"
	
	CSIRO stands for Commonwealth Scientific and Industrial Research Organization. It is the Australian Government's main research body. This is the first year CSIRO is taking part in TREC. We got involved in textual information retrieval research as a part of our activities in Resource Discovery Unit at the Research Data Network Co-operative Research Centre. The primary aim of our research in IR is improvement of the efficiency of resource discovery systems and networked information retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Kosmynin97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Kosmynin97,
		author = {Arkadi Kosmynin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CSIRO} Routing and Ad-Hoc Experiments at {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {455--460},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/csiro.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Kosmynin97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad Hoc Retrieval with Harris SENTINEL

_Margaret M. Knepper, Gregory J. Cusick, Kevin L. Fox, Ophir Frieder, Robert A. Killam_

- :fontawesome-solid-user-group: **Participant:** [Harris](./participants.md#harris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/harris.ps.gz](http://trec.nist.gov/pubs/trec6/papers/harris.ps.gz)
- :material-file-search: **Runs:** [harris1](./runs.md#harris1)

??? abstract "Abstract"
	
	Harris Information Systems Division (HISD) focuses on information retrieval support for various Government agencies. In our customers' applications, efficient (in terms of processing time) retrieval rates are critical, and highly accurate but relatively few documents retrieved is the norm. Our SENTINEL approach addresses our customers' needs. This is HISD first participation in the Text REtreival Conference (TREC). Our team participated in the category C (large data set) manual Ad Hoc track of the Sixth Text REtrieval Conference (TREC-6). Throughout TREC-6, we made modifications to enhance the performance of our system. We improved both the processing time and document retrieval. This paper is an overview our efforts for TREC-6.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KnepperCFFK97.bib) "
	```
	@inproceedings{DBLP:conf/trec/KnepperCFFK97,
		author = {Margaret M. Knepper and Gregory J. Cusick and Kevin L. Fox and Ophir Frieder and Robert A. Killam},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ad Hoc Retrieval with Harris {SENTINEL}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {503--509},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/harris.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KnepperCFFK97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ANU/ACSys TREC-6 Experiments

_David Hawking, Paul B. Thistlewaite, Nick Craswell_

- :fontawesome-solid-user-group: **Participant:** [ANU](./participants.md#anu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz](http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz)
- :material-file-search: **Runs:** [anu6alo1](./runs.md#anu6alo1) | [anu6ash1](./runs.md#anu6ash1) | [anu6min1](./runs.md#anu6min1)

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

#### Phrase Discovery for English and Cross-language Retrieval at TREC  6

_Fredric C. Gey, Aitao Chen_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/brkly.ps.gz](http://trec.nist.gov/pubs/trec6/papers/brkly.ps.gz)
- :material-file-search: **Runs:** [Brkly21](./runs.md#brkly21) | [Brkly22](./runs.md#brkly22) | [Brkly23](./runs.md#brkly23)

??? abstract "Abstract"
	
	Berkeley's experiments in TREC-6 center around phrase discovery in topics and documents. The technique of ranking bigram term pairs by their expected mutual information value was utilized for English phrase discovery as well as Chinese seg-mentation. This differentiates our phrase-finding method from the mechanistic one of using all bigrams which appear at least 25 times in the collection. Phrase finding presents an interesting interaction with stop words and stop word processing. English phrase discovery proved very important in a dictionary-based English to German cross language run. Our participation in the filtering track was marked with an interesting strictly Boolean retrieval as well as some experimentation with maximum utility thresholds on probabilistically ranked retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyC97,
		author = {Fredric C. Gey and Aitao Chen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Phrase Discovery for English and Cross-language Retrieval at {TREC} 6},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {637--647},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/brkly.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GeyC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MDS TREC6 Report

_Michael Fuller, Marcin Kaszkiel, Chien Leng Ng, Phil Vines, Ross Wilkinson, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [MDS](./participants.md#mds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz](http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz)
- :material-file-search: **Runs:** [mds601](./runs.md#mds601) | [mds602](./runs.md#mds602) | [mds603](./runs.md#mds603)

??? abstract "Abstract"
	
	This year the MDS group has participated in the ad hoc task, the Chinese task, the speech track, and the interactive track. It is our first year of participation in the speech and interactive tracks. We found the participation in both of these tracks of great benefit and interest.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FullerKNVWZ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/FullerKNVWZ97,
		author = {Michael Fuller and Marcin Kaszkiel and Chien Leng Ng and Phil Vines and Ross Wilkinson and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{MDS} {TREC6} Report},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {241--257},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FullerKNVWZ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-6 Ad-Hoc Retrieval

_Martin Franz, Salim Roukos_

- :fontawesome-solid-user-group: **Participant:** [IBM-Roukos](./participants.md#ibm-roukos)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ibm_ykt_t6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ibm_ykt_t6.ps.gz)
- :material-file-search: **Runs:** [ibms97a](./runs.md#ibms97a)

??? abstract "Abstract"
	
	In TREC-6 ad-hoc experiments we used multi-pass strategy, based on improving the document scores obtained from the Okapi formula [1] by combining them with scores produced by expanded queries, constructed automatically using top ranking documents from the first pass. We have examined various ways of creating expanded sets, as well as computing the scores for words and word pairs contained in them. An application of the same algorithms in the context of TREC-6 Very Large Corpus was also tested.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FranzR97.bib) "
	```
	@inproceedings{DBLP:conf/trec/FranzR97,
		author = {Martin Franz and Salim Roukos},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-6} Ad-Hoc Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {511--516},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ibm\_ykt\_t6.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FranzR97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Short Queries, Natural Language and Spoken Document Retrieval: Experiments  at Glasgow University

_Fabio Crestani, Mark Sanderson, Marcos Theophylactou, Mounia Lalmas_

- :fontawesome-solid-user-group: **Participant:** [Glasgow](./participants.md#glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/glasgow.ps.gz](http://trec.nist.gov/pubs/trec6/papers/glasgow.ps.gz)
- :material-file-search: **Runs:** [glair61](./runs.md#glair61) | [glair62](./runs.md#glair62) | [glair64](./runs.md#glair64)

??? abstract "Abstract"
	
	This paper contains a description of the methodology and results of the three TREC submissions made by the Glasgow IR group (glair). In addition to submitting to the ad hoc task, submissions were also made to NLP track and to the SDR speech 'pre-track'. Results from our submissions reveal that some of our approaches have performed poorly (i.e. ad hoc and NLP track), but we have also had success particularly in the speech track through use of transcript merging. We also highlight and discuss a seemingly unusual result where retrieval based on the very short versions of the TREC ad hoc queries produced better retrieval effectiveness than retrieval based on more 'normal' length queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CrestaniSTL97.bib) "
	```
	@inproceedings{DBLP:conf/trec/CrestaniSTL97,
		author = {Fabio Crestani and Mark Sanderson and Marcos Theophylactou and Mounia Lalmas},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Short Queries, Natural Language and Spoken Document Retrieval: Experiments at Glasgow University},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {667--686},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/glasgow.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CrestaniSTL97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Passage-Based Refinement (MultiText Experiements for TREC-6)

_Gordon V. Cormack, Charles L. A. Clarke, Christopher R. Palmer, Samuel S. L. To_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz](http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz)
- :material-file-search: **Runs:** [uwmt6a0](./runs.md#uwmt6a0) | [uwmt6a1](./runs.md#uwmt6a1) | [uwmt6a2](./runs.md#uwmt6a2)

??? abstract "Abstract"
	
	The MultiText system retrieves passages, rather than entire documents, that are likely to be relevant to a particular topic. For all runs, we used the reciprocal of the length of each passage as an estimate of its likely relevance and ranked accordingly. For the manual adhoc task we explored the limits of user interaction by judging some 13,000 documents based on retrieved passages. For the automatic adhoc task we used retrieved passages as a feedback source for new query terms. For the routing task we estimated probability of relevance from passage length and used this estimate to construct a compound (tiered) query which was used to rank the new data using passage length. For the Chinese track we indexed individual characters rather than segmented words or bigrams and used manually constructed queries and passage-length ranking. For the high precision track we performed judgements on passages using an interface similar to that used for the manual adhoc task. The Very Large Collection run was done on a network of four cheap computers using very simple manually constructed queries and passage-length ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackCPT97.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackCPT97,
		author = {Gordon V. Cormack and Charles L. A. Clarke and Christopher R. Palmer and Samuel S. L. To},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Passage-Based Refinement (MultiText Experiements for {TREC-6)}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {303--319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CormackCPT97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Clustering and SuperConcepts Within SMART: TREC 6

_Chris Buckley, Mandar Mitra, Janet A. Walz, Claire Cardie_

- :fontawesome-solid-user-group: **Participant:** [Cornell](./participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/cornell.ps.gz](http://trec.nist.gov/pubs/trec6/papers/cornell.ps.gz)
- :material-file-search: **Runs:** [Cor6A3cll](./runs.md#cor6a3cll) | [Cor6A1cls](./runs.md#cor6a1cls) | [Cor6A2qtcs](./runs.md#cor6a2qtcs)

??? abstract "Abstract"
	
	The Smart information retrieval project emphasizes completely automatic approaches to the understanding and retrieval of large quantities of text. We continue our work in TREC 6, performing runs in the routing, ad-hoc, and foreign language environments, including cross-lingual runs. The major focus this year is on trying to maintain the balance of the query - attempting to ensure the various aspects of the original query are appropriately addressed, especially while adding expansion terms. Exactly the same procedure is used for foreign language environments as for English; our tenet is that good information retrieval techniques are more powerful than linguistic knowledge. We also give an interesting cross-lingual run, assuming that French and English are closely enough related so that a query in one language can be run directly on a collection in the other language by just 'correcting' the spelling of the query words. This is quite successful for most queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleyMWC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleyMWC97,
		author = {Chris Buckley and Mandar Mitra and Janet A. Walz and Claire Cardie},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Clustering and SuperConcepts Within {SMART:} {TREC} 6},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {107--124},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/cornell.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BuckleyMWC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The GURU System in TREC-6

_Eric W. Brown, Herb A. Chong_

- :fontawesome-solid-user-group: **Participant:** [IBM-Brown](./participants.md#ibm-brown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ibm_brown.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ibm_brown.ps.gz)
- :material-file-search: **Runs:** [ibmg97a](./runs.md#ibmg97a) | [ibmg97b](./runs.md#ibmg97b)

??? abstract "Abstract"
	
	Our search application used in the TREC6 Interactive Track was developed as part of a User-Centered Design (UCD) program aimed at prototyping Ul approaches for using different search technologies being investigated at IBM Research. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrownC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrownC97,
		author = {Eric W. Brown and Herb A. Chong},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {GURU} System in {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {535--540},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ibm\_brown.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BrownC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at TREC6

_Mohand Boughanem, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/irit.ps.gz](http://trec.nist.gov/pubs/trec6/papers/irit.ps.gz)
- :material-file-search: **Runs:** [Mercure1](./runs.md#mercure1) | [Mercure2](./runs.md#mercure2) | [Mercure3](./runs.md#mercure3)

??? abstract "Abstract"
	
	We continue our work in trec performing runs in adhoc, routing and part of the cross language track. The major investigations this year are the weight schemes modification to take into account the document length. We also experiment the high precision procedure in automatic adhoc environment by tuning the term weight parameters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemS97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemS97,
		author = {Mohand Boughanem and Chantal Soul{\'{e}}{-}Dupuy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure at {TREC6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {321--328},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/irit.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemS97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY Does Battle With TREC-6

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, Donald Byrd, Russell C. Swan, Jinxi Xu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [INQ401](./runs.md#inq401) | [INQ402](./runs.md#inq402)

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

