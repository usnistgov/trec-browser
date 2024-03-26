# Proceedings 1997 

## Overview of the Sixth Text REtrieval Conference (TREC-6)

_Ellen M. Voorhees, Donna Harman_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/overview.ps.gz](http://trec.nist.gov/pubs/trec6/papers/overview.ps.gz)
??? abstract "Abstract"
	
	The sixth Text REtrieval Conference (TREC-6) was held at the National Institute of Standards and Technology (NIST) on November 19 21, 1997. The conference was co-sponsored by NIST and the Information Technology Office of the Defense Advanced Research Projects Agency (DARPA) as part of the TIPSTER Text Program. TREC-6 is the latest in a series of workshops designed to foster research in text retrieval. For analyses of the results of previous workshops, see Sparck Jones [6], Tague-Sutcliffe and Blustein [8], and Har-man [2]. In addition, the overview paper in each of the previous TREC proceedings summarizes the results of that TREC. The TREC workshop series has the following goals: • to encourage research in text retrieval based on large test collections; • to increase communication among industry, academia, and government by creating an open forum for the exchange of research ideas; • to speed the transfer of technology from research labs into commercial products by demonstrating substantial improvements in retrieval methodologies on real-world problems; and • to increase the availability of appropriate evaluation techniques for use by industry and academia, including development of new evaluation techniques more applicable to current sys-tems. Table 1 lists the groups that participated in TREC-6. Fifty-one groups including participants from 12 different countries and 21 companies were represented. The diversity of the participating groups has ensured that TREC represents many different approaches to text retrieval. The emphasis on individual experiments evaluated within a common setting has provenpto be a major strength of TREC. This paper serves as an introduction to the research described in detail in the remainder of the volume. The next section defines the common retrieval tasks performed in TREC-6. Sections 3 and 4 provide details regarding the test collections and the evaluation methodology used in TREC. Section 5 provides an overview of the retrieval results. The final section summarizes the main themes learned from the exper-iments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VoorheesH97.bib)"
	```
	@inproceedings{DBLP:conf/trec/VoorheesH97,
		author = {Ellen M. Voorhees and Donna Harman},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of the Sixth Text REtrieval Conference {(TREC-6)}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {1--24},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/overview.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/VoorheesH97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Adhoc 

#### Okapi at TREC-6 Automatic ad hoc, VLC, routing, filtering and QSDR

_Steve Walker, Stephen E. Robertson, Mohand Boughanem, Gareth J. F. Jones, Karen Sparck Jones_

- :fontawesome-solid-user-group: **Participant:** [City](./adhoc/participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz](http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz)
- :material-file-search: **Runs:** [city6al](./adhoc/runs.md#city6al) | [city6ad](./adhoc/runs.md#city6ad) | [city6at](./adhoc/runs.md#city6at)

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

- :fontawesome-solid-user-group: **Participant:** [Dublin](./adhoc/participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz](http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz)
- :material-file-search: **Runs:** [DCU97lnt](./adhoc/runs.md#dcu97lnt) | [DCU97lt](./adhoc/runs.md#dcu97lt) | [DCU97snt](./adhoc/runs.md#dcu97snt) | [DCU97vs](./adhoc/runs.md#dcu97vs)

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

- :fontawesome-solid-user-group: **Participant:** [NSA](./adhoc/participants.md#nsa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/nsa-rev.ps.gz](http://trec.nist.gov/pubs/trec6/papers/nsa-rev.ps.gz)
- :material-file-search: **Runs:** [nsasg1](./adhoc/runs.md#nsasg1) | [nsasg2](./adhoc/runs.md#nsasg2)

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

- :fontawesome-solid-user-group: **Participant:** [FS](./adhoc/participants.md#fs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/fsconsult.ps.gz](http://trec.nist.gov/pubs/trec6/papers/fsconsult.ps.gz)
- :material-file-search: **Runs:** [fsclt6](./adhoc/runs.md#fsclt6) | [fsclt6t](./adhoc/runs.md#fsclt6t) | [fsclt6r](./adhoc/runs.md#fsclt6r)

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

- :fontawesome-solid-user-group: **Participant:** [Verity](./adhoc/participants.md#verity)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/verity-trec6-corrected.ps.gz](http://trec.nist.gov/pubs/trec6/papers/verity-trec6-corrected.ps.gz)
- :material-file-search: **Runs:** [VrtyAH6a](./adhoc/runs.md#vrtyah6a) | [VrtyAH6b](./adhoc/runs.md#vrtyah6b)

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

- :fontawesome-solid-user-group: **Participant:** [UNC-N](./adhoc/participants.md#unc-n)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/newby-t6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/newby-t6.ps.gz)
- :material-file-search: **Runs:** [ispa1](./adhoc/runs.md#ispa1) | [ispa2](./adhoc/runs.md#ispa2)

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

- :fontawesome-solid-user-group: **Participant:** [GMU](./adhoc/participants.md#gmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/gmu.ps.gz](http://trec.nist.gov/pubs/trec6/papers/gmu.ps.gz)
- :material-file-search: **Runs:** [gmu97au1](./adhoc/runs.md#gmu97au1) | [gmu97au2](./adhoc/runs.md#gmu97au2) | [gmu97ma1](./adhoc/runs.md#gmu97ma1) | [gmu97ma2](./adhoc/runs.md#gmu97ma2)

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

- :fontawesome-solid-user-group: **Participant:** [CUNY](./adhoc/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/queenst6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/queenst6.ps.gz)
- :material-file-search: **Runs:** [pirc7Aa](./adhoc/runs.md#pirc7aa) | [pirc7Ad](./adhoc/runs.md#pirc7ad) | [pirc7At](./adhoc/runs.md#pirc7at)

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

- :fontawesome-solid-user-group: **Participant:** [CSIRO](./adhoc/participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/csiro.ps.gz](http://trec.nist.gov/pubs/trec6/papers/csiro.ps.gz)
- :material-file-search: **Runs:** [csiro97a1](./adhoc/runs.md#csiro97a1) | [csiro97a2](./adhoc/runs.md#csiro97a2) | [csiro97a3](./adhoc/runs.md#csiro97a3)

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

- :fontawesome-solid-user-group: **Participant:** [Harris](./adhoc/participants.md#harris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/harris.ps.gz](http://trec.nist.gov/pubs/trec6/papers/harris.ps.gz)
- :material-file-search: **Runs:** [harris1](./adhoc/runs.md#harris1)

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

- :fontawesome-solid-user-group: **Participant:** [ANU](./adhoc/participants.md#anu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz](http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz)
- :material-file-search: **Runs:** [anu6alo1](./adhoc/runs.md#anu6alo1) | [anu6ash1](./adhoc/runs.md#anu6ash1) | [anu6min1](./adhoc/runs.md#anu6min1)

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

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./adhoc/participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/brkly.ps.gz](http://trec.nist.gov/pubs/trec6/papers/brkly.ps.gz)
- :material-file-search: **Runs:** [Brkly21](./adhoc/runs.md#brkly21) | [Brkly22](./adhoc/runs.md#brkly22) | [Brkly23](./adhoc/runs.md#brkly23)

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

- :fontawesome-solid-user-group: **Participant:** [MDS](./adhoc/participants.md#mds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz](http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz)
- :material-file-search: **Runs:** [mds601](./adhoc/runs.md#mds601) | [mds602](./adhoc/runs.md#mds602) | [mds603](./adhoc/runs.md#mds603)

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

- :fontawesome-solid-user-group: **Participant:** [IBM-Roukos](./adhoc/participants.md#ibm-roukos)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ibm_ykt_t6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ibm_ykt_t6.ps.gz)
- :material-file-search: **Runs:** [ibms97a](./adhoc/runs.md#ibms97a)

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

- :fontawesome-solid-user-group: **Participant:** [Glasgow](./adhoc/participants.md#glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/glasgow.ps.gz](http://trec.nist.gov/pubs/trec6/papers/glasgow.ps.gz)
- :material-file-search: **Runs:** [glair61](./adhoc/runs.md#glair61) | [glair62](./adhoc/runs.md#glair62) | [glair64](./adhoc/runs.md#glair64)

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

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./adhoc/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz](http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz)
- :material-file-search: **Runs:** [uwmt6a0](./adhoc/runs.md#uwmt6a0) | [uwmt6a1](./adhoc/runs.md#uwmt6a1) | [uwmt6a2](./adhoc/runs.md#uwmt6a2)

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

- :fontawesome-solid-user-group: **Participant:** [Cornell](./adhoc/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/cornell.ps.gz](http://trec.nist.gov/pubs/trec6/papers/cornell.ps.gz)
- :material-file-search: **Runs:** [Cor6A3cll](./adhoc/runs.md#cor6a3cll) | [Cor6A1cls](./adhoc/runs.md#cor6a1cls) | [Cor6A2qtcs](./adhoc/runs.md#cor6a2qtcs)

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

- :fontawesome-solid-user-group: **Participant:** [IBM-Brown](./adhoc/participants.md#ibm-brown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ibm_brown.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ibm_brown.ps.gz)
- :material-file-search: **Runs:** [ibmg97a](./adhoc/runs.md#ibmg97a) | [ibmg97b](./adhoc/runs.md#ibmg97b)

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

- :fontawesome-solid-user-group: **Participant:** [IRIT](./adhoc/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/irit.ps.gz](http://trec.nist.gov/pubs/trec6/papers/irit.ps.gz)
- :material-file-search: **Runs:** [Mercure1](./adhoc/runs.md#mercure1) | [Mercure2](./adhoc/runs.md#mercure2) | [Mercure3](./adhoc/runs.md#mercure3)

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

- :fontawesome-solid-user-group: **Participant:** [UMass](./adhoc/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [INQ401](./adhoc/runs.md#inq401) | [INQ402](./adhoc/runs.md#inq402)

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

## Routing 

#### Okapi at TREC-6 Automatic ad hoc, VLC, routing, filtering and QSDR

_Steve Walker, Stephen E. Robertson, Mohand Boughanem, Gareth J. F. Jones, Karen Sparck Jones_

- :fontawesome-solid-user-group: **Participant:** [City](./routing/participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz](http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz)
- :material-file-search: **Runs:** [city6r1](./routing/runs.md#city6r1) | [city6r2](./routing/runs.md#city6r2)

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

#### Fusion Via Linear Combination for the Routing Problem

_Christopher C. Vogt, Garrison W. Cottrell_

- :fontawesome-solid-user-group: **Participant:** [UCSD](./routing/participants.md#ucsd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ucsd.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ucsd.ps.gz)
- :material-file-search: **Runs:** [UCSDrt6](./routing/runs.md#ucsdrt6)

??? abstract "Abstract"
	
	A linear combination of scores from two different IR systems is used for the routing task, with one combination model being trained for each query. Despite a poor selection of component systems, the combination model performs on par with the better of the two systems, learning to ignore the worse system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VogtC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/VogtC97,
		author = {Christopher C. Vogt and Garrison W. Cottrell},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Fusion Via Linear Combination for the Routing Problem},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {661--666},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ucsd.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/VogtC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Verity at TREC-6: Out-of-the-Box and Beyond

_Jan O. Pedersen, Craig Silverstein, Christopher C. Vogt_

- :fontawesome-solid-user-group: **Participant:** [Verity](./routing/participants.md#verity)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/verity-trec6-corrected.ps.gz](http://trec.nist.gov/pubs/trec6/papers/verity-trec6-corrected.ps.gz)
- :material-file-search: **Runs:** [VrtyRT6](./routing/runs.md#vrtyrt6)

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

- :fontawesome-solid-user-group: **Participant:** [UNC-N](./routing/participants.md#unc-n)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/newby-t6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/newby-t6.ps.gz)
- :material-file-search: **Runs:** [ispr1](./routing/runs.md#ispr1) | [ispr2](./routing/runs.md#ispr2)

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

#### ETH TREC-6: Routing, Chinese, Cross-Language and Spoken Document  Retrieval

_Bojidar Mateev, Eugen Munteanu, Paraic Sheridan, Martin Wechsler, Peter Schäuble_

- :fontawesome-solid-user-group: **Participant:** [ETH](./routing/participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ETH_notebook.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ETH_notebook.ps.gz)
- :material-file-search: **Runs:** [ETH6R1](./routing/runs.md#eth6r1) | [ETH6R2](./routing/runs.md#eth6r2)

??? abstract "Abstract"
	
	ETH Zurich's participation in TREC-6 consists of experiments in the main routing task, both manual and automatic runs in the Chinese retrieval track, cross-language retrieval in each of German, French and English as part of the new cross-language retrieval track, and experiments in speech recognition and retrieval under the new spoken document retrieval track. This year our routing experiments focused on the improvement of the feature selection strategy, on query expansion using similarity thesauri, on the grouping of features and on the combination of different retrieval methods. For Chinese retrieval we continued to rely on character bi-grams for indexing instead of attempting to segment and identify individual words, and we introduced a new manually-constructed stopword list consisting of almost 1,000 Chinese words. Experiments in cross-language retrieval focused heavily on our approach using multilingual similarity thesauri but also included several runs using machine translation technol-ogy. Finally, for the spoken document retrieval track our work included the development of a simple speaker-independent phoneme recogniser and some innovations in our probabilistic retrieval functions to compensate for speech recognition errors.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MateevMSWS97.bib) "
	```
	@inproceedings{DBLP:conf/trec/MateevMSWS97,
		author = {Bojidar Mateev and Eugen Munteanu and Paraic Sheridan and Martin Wechsler and Peter Sch{\"{a}}uble},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{ETH} {TREC-6:} Routing, Chinese, Cross-Language and Spoken Document Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {623--635},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ETH\_notebook.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MateevMSWS97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSIRO Routing and Ad-Hoc Experiments at TREC-6

_Arkadi Kosmynin_

- :fontawesome-solid-user-group: **Participant:** [CSIRO](./routing/participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/csiro.ps.gz](http://trec.nist.gov/pubs/trec6/papers/csiro.ps.gz)
- :material-file-search: **Runs:** [csiro97r1](./routing/runs.md#csiro97r1) | [csiro97r2](./routing/runs.md#csiro97r2)

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

#### Query Term Expansion based on Paragraphs of the Relevant Documents

_Kai Ishikawa, Kenji Satoh, Akitoshi Okumura_

- :fontawesome-solid-user-group: **Participant:** [NEC](./routing/participants.md#nec)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/NEC.ps.gz](http://trec.nist.gov/pubs/trec6/papers/NEC.ps.gz)
- :material-file-search: **Runs:** [virtue3](./routing/runs.md#virtue3)

??? abstract "Abstract"
	
	Recently, we studied the method of extracting terms that co-occurred with initial query terms in relevant paragraphs as query term expansion method. In our methods, paragraphs in the relevant documents are lanked by using initial query to extract terms from the upper ranked paragraphs with using term co-occurrence. Our method eases the difficulty by ranking paragraphs with the initial query. Without using term co-occurrence in paragraphs, we could achieve the highly accurate treatment of term co-occurrence by small calculation. The results of our system for TREC-6 routing test data, obtained by using the expanded queries generated by our query term generation method are compared with the results obtained by initial queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/IshikawaSO97.bib) "
	```
	@inproceedings{DBLP:conf/trec/IshikawaSO97,
		author = {Kai Ishikawa and Kenji Satoh and Akitoshi Okumura},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Query Term Expansion based on Paragraphs of the Relevant Documents},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {577--584},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/NEC.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/IshikawaSO97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Conceptual Indexing Using Thematic Representation of Texts

_Boris V. Dobrov, Natalia V. Loukachevitch, Tatyana N. Yudina_

- :fontawesome-solid-user-group: **Participant:** [CIR-Russia](./routing/participants.md#cir-russia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/CIR6ROU3.ps.gz](http://trec.nist.gov/pubs/trec6/papers/CIR6ROU3.ps.gz)
- :material-file-search: **Runs:** [cir6rou1](./routing/runs.md#cir6rou1)

??? abstract "Abstract"
	
	We present the thesaurus-based indexing technology developed by the Center for Information Research under the Information System RUSSIA project. The technology is based on using basic properties of coherent text. Initially the technology was applied for automatic processing of Russian official (government) texts. Currently the instrument is adapted to process English texts for TREC-6 routing task. 
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DobrovLY97.bib) "
	```
	@inproceedings{DBLP:conf/trec/DobrovLY97,
		author = {Boris V. Dobrov and Natalia V. Loukachevitch and Tatyana N. Yudina},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Conceptual Indexing Using Thematic Representation of Texts},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {403--413},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/CIR6ROU3.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DobrovLY97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Passage-Based Refinement (MultiText Experiements for TREC-6)

_Gordon V. Cormack, Charles L. A. Clarke, Christopher R. Palmer, Samuel S. L. To_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./routing/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz](http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz)
- :material-file-search: **Runs:** [uwmt6r1](./routing/runs.md#uwmt6r1) | [uwmt6r0](./routing/runs.md#uwmt6r0)

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

- :fontawesome-solid-user-group: **Participant:** [Cornell](./routing/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/cornell.ps.gz](http://trec.nist.gov/pubs/trec6/papers/cornell.ps.gz)
- :material-file-search: **Runs:** [Cor6R2qtc](./routing/runs.md#cor6r2qtc) | [Cor6R1cc](./routing/runs.md#cor6r1cc)

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

#### The text categorization system TEKLIS at TREC-6

_Thomas Brückner_

- :fontawesome-solid-user-group: **Participant:** [Siemens](./routing/participants.md#siemens)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/siemens.ps.gz](http://trec.nist.gov/pubs/trec6/papers/siemens.ps.gz)
- :material-file-search: **Runs:** [teklis](./routing/runs.md#teklis)

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

#### Mercure at TREC6

_Mohand Boughanem, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./routing/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/irit.ps.gz](http://trec.nist.gov/pubs/trec6/papers/irit.ps.gz)
- :material-file-search: **Runs:** [Mercure4](./routing/runs.md#mercure4)

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

#### Application of Logical Analysis of Data to the TREC-6 Routing Task

_Endre Boros, Paul B. Kantor, Jung Jin Lee, Kwong Bor Ng, Di Zhao_

- :fontawesome-solid-user-group: **Participant:** [RutgersK](./routing/participants.md#rutgersk)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/rutLAD.ps.gz](http://trec.nist.gov/pubs/trec6/papers/rutLAD.ps.gz)
- :material-file-search: **Runs:** [rutLADc1](./routing/runs.md#rutladc1) | [rutLADw1](./routing/runs.md#rutladw1)

??? abstract "Abstract"
	
	Our approach to TREC6 has explored the possibility of building complex Boolean expressions which represent the classificatory information present in the training data. The positive (i.e. judged relevant), and negative (i.e. judged not relevant) documents are studied separately, using Church's measure of 'non-Poissonicity' (Church & Gale, 1995) to identify promising terms for classification. In the official runs, statistics are produced using the MG (Witten, Moffat, Bell, 1994)) search engine, and the terms are in fact stems, rather than complete terms. The top 25 terms selected from the positive and negative examples are merged, to form a list with no more than 50 terms. The MG retrieval system is used (massively) to transform every judged document into a Boolean vector with one component for each distinct classification term. The RUTCOR LAD program (Boros, Hammer, Ibaraki, Kogan, Mayoraz, & Muchnik, 1996) is used (twice for each topic), with several modifications, to search exhaustively for Boolean prime implicants which characterize the positive and the negative examples. Due to computer speed limitations, we have limited the search in our official submissions to terms of order three (i.e terms such as ABC', where C' denotes the absence of term C). Each pattern which matches some positive (respectively, negative) examples is given a weight determined by the number of examples that it matches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BorosKLNZ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BorosKLNZ97,
		author = {Endre Boros and Paul B. Kantor and Jung Jin Lee and Kwong Bor Ng and Di Zhao},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Application of Logical Analysis of Data to the {TREC-6} Routing Task},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {611--617},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/rutLAD.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BorosKLNZ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Information Extraction to Improve Document Retrieval

_John Bear, David J. Israel, Jeff Petit, David L. Martin_

- :fontawesome-solid-user-group: **Participant:** [SRI](./routing/participants.md#sri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/sri.ps.gz](http://trec.nist.gov/pubs/trec6/papers/sri.ps.gz)
- :material-file-search: **Runs:** [srige1](./routing/runs.md#srige1)

??? abstract "Abstract"
	
	We describe an approach to applying a particular kind of Natural Language Processing (NLP) system to the TREC routing task in Information Retrieval (IR). Rather than attempting to use NLP techniques in indexing documents in a corpus, we adapted an information extraction (IE) system to act as a post-filter on the output of an IR system. The IE system was configured to score each of the top 2000 documents as determined by an IR system and on the basis of that score to rerank those 2000 documents. One aim was to improve precision on routing tasks. Another was to make it easier to write IE grammars for multiple topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BearIPM97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BearIPM97,
		author = {John Bear and David J. Israel and Jeff Petit and David L. Martin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Information Extraction to Improve Document Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {367--377},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/sri.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BearIPM97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Daimler Benz Research: System and Experiments Routing and Filtering

_Thomas Bayer, Heike Mogg-Schneider, Ingrid Renz, Hartmut Schäfer_

- :fontawesome-solid-user-group: **Participant:** [DBenz](./routing/participants.md#dbenz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/dbulm.ps.gz](http://trec.nist.gov/pubs/trec6/papers/dbulm.ps.gz)
- :material-file-search: **Runs:** [dbulm1](./routing/runs.md#dbulm1)

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

- :fontawesome-solid-user-group: **Participant:** [UMass](./routing/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [INQ403](./routing/runs.md#inq403) | [INQ404](./routing/runs.md#inq404)

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

## Chinese 

#### Chinese Document Retrieval at TREC-6

_Ross Wilkinson_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/csiro.chinese.ps.gz](http://trec.nist.gov/pubs/trec6/papers/csiro.chinese.ps.gz)
??? abstract "Abstract"
	
	In the Chinese language each character represents at least a complete syllable, rather than a letter as in other languages. Many characters are also single syllable words. The total number of characters is therefore quite large and somewhat ill-defined. A literate adult would typically recognise at least 5-6,000 characters. The various modern standards define between 10-12,000 characters, although if early and ancient literature is included the number rises to approximately 100,000. Chinese is agglutinating - there is no space between consecutive characters, except perhaps, at the end of a sentence. Thus to perform retrieval in Chinese, the basis has to be characters unless the text is pre-segmented into words. Segmentation is difficult - not even humans will always agree on correct segmentation, and there has been much research in successful segmentation of Chinese [1].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Wilkinson97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Wilkinson97,
		author = {Ross Wilkinson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Chinese Document Retrieval at {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {25--29},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/csiro.chinese.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Wilkinson97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on Proximity Based Chinese Text Retrieval in TREC 6

_K. Rajaraman, Kok F. Lai, Y. Changwen_

- :fontawesome-solid-user-group: **Participant:** [ITI-SG](./chinese/participants.md#iti-sg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/itich.ps.gz](http://trec.nist.gov/pubs/trec6/papers/itich.ps.gz)
- :material-file-search: **Runs:** [itich1](./chinese/runs.md#itich1) | [itich2](./chinese/runs.md#itich2) | [itich3](./chinese/runs.md#itich3)

??? abstract "Abstract"
	
	In TREC 6, we participate in the Chinese track and report our experiments on proximity based text retrieval. Our participation this year concentrates on automatic retrieval methods natural for the Chinese language. We index the documents by treating every Chinese character as a single term and store positional information for all terms. During retrieval we employ a proximity operator that uses the positional information in the index, to rank the documents. The operator is defined such that documents are scored in proportion to the proximity of characters as they appear in the query. Since we only use the proximity of characters to compute the score, the algorithm does not strictly require the word boundaries be known a priori. In particular, phrase detection can be derived as a special case of our algorithm by giving maximum score when the characters are immediately adjacent and 0 otherwise. This indexing and retrieval scheme is significantly different from our TREC 5 method. We submit three official runs itich1, itich2 and itich3 for TREC 6. For itich3, we use all phrases from the Description field and compute scores with our proximity operator. The runs itichi and itich2 are obtained through automatic query expansion methods. We dynamically build a 3-gram phrase dictionary from top 20 documents for each query ranked in itich3 and pick phrases to expand from this dictionary using document frequency estimates. The run itich2 is different from itich1 in that the expanded phrases are filtered to remove duplicate and common phrases.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RajaramanLC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/RajaramanLC97,
		author = {K. Rajaraman and Kok F. Lai and Y. Changwen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments on Proximity Based Chinese Text Retrieval in {TREC} 6},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {559--576},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/itich.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RajaramanLC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Between Terms and Words for European Language IR and Between Words  and Bigrams for Chinese IR

_Jian-Yun Nie, Jean-Pierre Chevallet, Marie-France Bruandet_

- :fontawesome-solid-user-group: **Participant:** [UMontreal](./chinese/participants.md#umontreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/montreal.ps.gz](http://trec.nist.gov/pubs/trec6/papers/montreal.ps.gz)
- :material-file-search: **Runs:** [UdeMbi](./chinese/runs.md#udembi) | [UdeMseg](./chinese/runs.md#udemseg)

??? abstract "Abstract"
	
	Université de Montréal, together with the MRIM research group of the CLIPS laboratory in IMAG institute, participated in the Cross-Language Retrieval track in TREC6. Université de Montréal also participated in the Chinese track. In this paper, we describe our approches used in our experiments. In the cross-language retrieval track, we compared word-based retrieval and term-based retrieval. In the Chinese track, the approaches using bigrams and words are compared.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NieCB97.bib) "
	```
	@inproceedings{DBLP:conf/trec/NieCB97,
		author = {Jian{-}Yun Nie and Jean{-}Pierre Chevallet and Marie{-}France Bruandet},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Between Terms and Words for European Language {IR} and Between Words and Bigrams for Chinese {IR}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {697--709},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/montreal.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NieCB97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ETH TREC-6: Routing, Chinese, Cross-Language and Spoken Document  Retrieval

_Bojidar Mateev, Eugen Munteanu, Paraic Sheridan, Martin Wechsler, Peter Schäuble_

- :fontawesome-solid-user-group: **Participant:** [ETH](./chinese/participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ETH_notebook.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ETH_notebook.ps.gz)
- :material-file-search: **Runs:** [ETHccM](./chinese/runs.md#ethccm) | [ETHccA](./chinese/runs.md#ethcca)

??? abstract "Abstract"
	
	ETH Zurich's participation in TREC-6 consists of experiments in the main routing task, both manual and automatic runs in the Chinese retrieval track, cross-language retrieval in each of German, French and English as part of the new cross-language retrieval track, and experiments in speech recognition and retrieval under the new spoken document retrieval track. This year our routing experiments focused on the improvement of the feature selection strategy, on query expansion using similarity thesauri, on the grouping of features and on the combination of different retrieval methods. For Chinese retrieval we continued to rely on character bi-grams for indexing instead of attempting to segment and identify individual words, and we introduced a new manually-constructed stopword list consisting of almost 1,000 Chinese words. Experiments in cross-language retrieval focused heavily on our approach using multilingual similarity thesauri but also included several runs using machine translation technol-ogy. Finally, for the spoken document retrieval track our work included the development of a simple speaker-independent phoneme recogniser and some innovations in our probabilistic retrieval functions to compensate for speech recognition errors.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MateevMSWS97.bib) "
	```
	@inproceedings{DBLP:conf/trec/MateevMSWS97,
		author = {Bojidar Mateev and Eugen Munteanu and Paraic Sheridan and Martin Wechsler and Peter Sch{\"{a}}uble},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{ETH} {TREC-6:} Routing, Chinese, Cross-Language and Spoken Document Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {623--635},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ETH\_notebook.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MateevMSWS97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Preliminary Qualitative Analysis of Segmented vs Bigram Indexing in  Chinese

_Mun-Kew Leong, Hong Zhou_

- :fontawesome-solid-user-group: **Participant:** [ISS](./chinese/participants.md#iss)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/iss.ps.gz](http://trec.nist.gov/pubs/trec6/papers/iss.ps.gz)
- :material-file-search: **Runs:** [iss97CmD](./chinese/runs.md#iss97cmd) | [iss97CbD](./chinese/runs.md#iss97cbd) | [iss97CsD](./chinese/runs.md#iss97csd)

??? abstract "Abstract"
	
	This paper investigates merging multiple methods of indexing for Chinese IR. Identical queries, differently segmented, are used to retrieve individual lists of documents which are then merged before evaluation. Two simple merge methods are discussed. Results on Chinese TREC queries 1 to 28 show improvement over either one of the indexing schemes by themselves. In addition, we examine the difference in the documents returned by each indexing method, i.e., do different indexing schemes retrieve different documents, or the same documents ranked differently, or something else. While we contrasted bigram based indexing with segmented based indexing, the same methods would apply between any two forms of indexing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeongZ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeongZ97,
		author = {Mun{-}Kew Leong and Hong Zhou},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Preliminary Qualitative Analysis of Segmented vs Bigram Indexing in Chinese},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {551--557},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/iss.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LeongZ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-6 English and Chinese Retrieval Experiments using PIRCS

_K. L. Kwok, Laszlo Grunfeld, J. H. Xu_

- :fontawesome-solid-user-group: **Participant:** [CUNY](./chinese/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/queenst6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/queenst6.ps.gz)
- :material-file-search: **Runs:** [pirc7Ca](./chinese/runs.md#pirc7ca) | [pirc7Cd](./chinese/runs.md#pirc7cd) | [pirc7Ct](./chinese/runs.md#pirc7ct)

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

#### Okapi Chinese Text Retrieval Experiments at TREC-6

_Xiangji Huang, Stephen E. Robertson_

- :fontawesome-solid-user-group: **Participant:** [City](./chinese/participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/city_proc_chinese.ps.gz](http://trec.nist.gov/pubs/trec6/papers/city_proc_chinese.ps.gz)
- :material-file-search: **Runs:** [city97c1](./chinese/runs.md#city97c1) | [city97c2](./chinese/runs.md#city97c2) | [city97c3](./chinese/runs.md#city97c3)

??? abstract "Abstract"
	
	A full description of the experimental system and conditions is given in Appendices A and B. Searchers filled in three types of questionnaires. The pre-session questionnaire established the user's experience and profile. In the post search questionnaires, searchers were asked questions regarding the topic, the search and the system used after undertaking each individual search. Finally in the post-session questionnaire, subjects were asked to provide an overview of the experiment. In addition to the questionnaires, searchers noted on a worksheet the different aspects of the topics they encountered whilst they undertook each search. A total of eight subjects completed forty eight searches, that is three searches on each of the two systems, Okapi and ZPrise. The sessions were divided into two rounds of four searchers. Of the two groups who carried out the twenty-four searches on Okapi, Group A used the same interface as in TREC-5, but with incremental query expansion modified (Appendix A.3.2), and Group B searched a slightly different version which allowed the searcher to cancel the relevance feedback process or clear the query (Appendix A.4).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangR97.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangR97,
		author = {Xiangji Huang and Stephen E. Robertson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Okapi Chinese Text Retrieval Experiments at {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {137--142},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/city\_proc\_chinese.ps.gz},
		timestamp = {Wed, 03 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangR97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MDS TREC6 Report

_Michael Fuller, Marcin Kaszkiel, Chien Leng Ng, Phil Vines, Ross Wilkinson, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [MDS](./chinese/participants.md#mds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz](http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz)
- :material-file-search: **Runs:** [mds607](./chinese/runs.md#mds607) | [mds608](./chinese/runs.md#mds608) | [mds609](./chinese/runs.md#mds609)

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

#### Passage-Based Refinement (MultiText Experiements for TREC-6)

_Gordon V. Cormack, Charles L. A. Clarke, Christopher R. Palmer, Samuel S. L. To_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./chinese/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz](http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz)
- :material-file-search: **Runs:** [uwmt6c0](./chinese/runs.md#uwmt6c0)

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

#### INQUERY Does Battle With TREC-6

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, Donald Byrd, Russell C. Swan, Jinxi Xu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./chinese/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [INQ4ch1](./chinese/runs.md#inq4ch1) | [INQ4ch2](./chinese/runs.md#inq4ch2)

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

## Cross-Language 

#### Cross-Language Information Retrieval (CLIR) Track Overview

_Peter Schäuble, Paraic Sheridan_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/clir_track_US.ps.gz](http://trec.nist.gov/pubs/trec6/papers/clir_track_US.ps.gz)
??? abstract "Abstract"
	
	Cross-Language Information Retrieval (CLIR) was a new task in the TREC-6 evaluation. In contrast to the multilingual track included in previous TREC evaluations, which was concerned with information retrieval in Spanish or Chi-nese, the cross-language retrieval track focuses on the retrieval situation where the documents are written in a language which is different than the language used to specify the queries. The TREC-6 track used documents in English, French and German and queries in English, French, German, Spanish and Dutch. There are many applications or scenarios in which a user of a retrieval system may be interested in finding information written in a language other than the user's native or preferred language. In some applications, a user may want to discover all possible relevant information in a multilingual textbase, irrespective of the language of the relevant information. This may be the case when searching certain collections of legal or patent information for example. In other cases a user may even have some language comprehension ability in the languages of the documents (passive vocabulary) but may not have a sufficiently rich active vocabulary in the document languages to confidently specify queries in those languages. In this case a cross-language search which permits the user to specify native language queries but retrieves documents in their original language is useful. Cross-language retrieval also has the added advantage of requiring only one query to a multi-lingual text collection, rather than having a user submit individual queries in each of the languages of interest. Situations where a retrieval system user is faced with the task of querying a multilingual document collection are becoming increasingly common. These range across document collections made up of documents from local offices of multinational companies, collections composed of documents from different regions of multilingual countries such as Switzerland or Canada, or the document collections of large organisations such as the United Nations or European Com-mission. It is however, the global information infrastructure of the internet that has been largely responsible for the growing awareness of a need for cross-language information retrieval systems. This has in turn led to a growing body of research into the problems of cross-language retrieval and the development of several different approaches for CLIR.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchaubleS97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchaubleS97,
		author = {Peter Sch{\"{a}}uble and Paraic Sheridan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Cross-Language Information Retrieval {(CLIR)} Track Overview},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {31--43},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/clir\_track\_US.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SchaubleS97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad hoc Retrieval Using Thresholds, WSTs for French Mono-lingual Retrieval,  Document-at-a-Glance for High Precision and Triphone Windows for Spoken  Documents

_Alan F. Smeaton, Fergus Kelledy, Gerard Quinn_

- :fontawesome-solid-user-group: **Participant:** [Dublin](./clir/participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz](http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz)
- :material-file-search: **Runs:** [DCU97Fv1](./clir/runs.md#dcu97fv1) | [DCU97Fv2](./clir/runs.md#dcu97fv2)

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

#### Automatic 3-Language Cross-Language Information Retrieval with Latent  Semantic Indexing

_Bob Rehder, Michael L. Littman, Susan T. Dumais, Thomas K. Landauer_

- :fontawesome-solid-user-group: **Participant:** [Duke](./clir/participants.md#duke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/lsi.ps.gz](http://trec.nist.gov/pubs/trec6/papers/lsi.ps.gz)
- :material-file-search: **Runs:** [97lsiSEE](./clir/runs.md#97lsisee) | [97lsiSFF](./clir/runs.md#97lsisff) | [97lsiSGG](./clir/runs.md#97lsisgg) | [97lsiLEE](./clir/runs.md#97lsilee) | [97lsiLFF](./clir/runs.md#97lsilff) | [97lsiLGG](./clir/runs.md#97lsilgg) | [97lsiSGE](./clir/runs.md#97lsisge) | [97lsiSGF](./clir/runs.md#97lsisgf) | [97lsiLGE](./clir/runs.md#97lsilge) | [97lsiLGF](./clir/runs.md#97lsilgf) | [97lsiSFE](./clir/runs.md#97lsisfe) | [97lsiSFG](./clir/runs.md#97lsisfg) | [97lsiLFE](./clir/runs.md#97lsilfe) | [97lsiLFG](./clir/runs.md#97lsilfg) | [97lsiSEG](./clir/runs.md#97lsiseg) | [97lsiSEF](./clir/runs.md#97lsisef) | [97lsiLEG](./clir/runs.md#97lsileg) | [97lsiLEF](./clir/runs.md#97lsilef)

??? abstract "Abstract"
	
	This paper describes cross-language information-retrieval experiments carried out for TREC-6. Our retrieval method, cross-language latent semantic indexing (CL-LSI), is completely automatic and we were able to use it to create a 3-way English-French-German IR system. This study extends our previous work in terms of the large size of training and testing corpora, the use of low-quality training data, the evaluation using relevance judg-ments, and the number of languages analyzed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RehderLDL97.bib) "
	```
	@inproceedings{DBLP:conf/trec/RehderLDL97,
		author = {Bob Rehder and Michael L. Littman and Susan T. Dumais and Thomas K. Landauer},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Automatic 3-Language Cross-Language Information Retrieval with Latent Semantic Indexing},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {233--239},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/lsi.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RehderLDL97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Document Translation for Cross-Language Text Retrieval at the University  of Maryland

_Douglas W. Oard, Paul G. Hackett_

- :fontawesome-solid-user-group: **Participant:** [UMd](./clir/participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umd.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umd.ps.gz)
- :material-file-search: **Runs:** [umcpxeg1](./clir/runs.md#umcpxeg1) | [umcpxeg2](./clir/runs.md#umcpxeg2) | [umcpxeg3](./clir/runs.md#umcpxeg3) | [umcpxge1](./clir/runs.md#umcpxge1) | [umcpxge2](./clir/runs.md#umcpxge2) | [umcpxge3](./clir/runs.md#umcpxge3) | [umcpxgg1](./clir/runs.md#umcpxgg1) | [umcpxgg2](./clir/runs.md#umcpxgg2) | [umcpxgg3](./clir/runs.md#umcpxgg3) | [umcpxgg4](./clir/runs.md#umcpxgg4) | [umcpxgg5](./clir/runs.md#umcpxgg5) | [umcpxgg6](./clir/runs.md#umcpxgg6)

??? abstract "Abstract"
	
	The University of Maryland participated in three TREC-6 tasks: ad hoc retrieval, cross-language retrieval, and spoken document retrieval. The principal focus of the work was evaluation of a cross-language text retrieval technique based on fully automatic machine translation. The results show that approaches based on document translation can be approximately as effective as approaches based on query translation, but that additional work will be needed to develop a solid basis for choosing between the two in specific applications. Ad hoc and spoken document retrieval results are also presented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardH97.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardH97,
		author = {Douglas W. Oard and Paul G. Hackett},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Document Translation for Cross-Language Text Retrieval at the University of Maryland},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {687--696},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/umd.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/OardH97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Between Terms and Words for European Language IR and Between Words  and Bigrams for Chinese IR

_Jian-Yun Nie, Jean-Pierre Chevallet, Marie-France Bruandet_

- :fontawesome-solid-user-group: **Participant:** [UMontreal](./clir/participants.md#umontreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/montreal.ps.gz](http://trec.nist.gov/pubs/trec6/papers/montreal.ps.gz)
- :material-file-search: **Runs:** [CLIPS1](./clir/runs.md#clips1) | [CLIPS2](./clir/runs.md#clips2) | [CLIPS3](./clir/runs.md#clips3)

??? abstract "Abstract"
	
	Université de Montréal, together with the MRIM research group of the CLIPS laboratory in IMAG institute, participated in the Cross-Language Retrieval track in TREC6. Université de Montréal also participated in the Chinese track. In this paper, we describe our approches used in our experiments. In the cross-language retrieval track, we compared word-based retrieval and term-based retrieval. In the Chinese track, the approaches using bigrams and words are compared.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NieCB97.bib) "
	```
	@inproceedings{DBLP:conf/trec/NieCB97,
		author = {Jian{-}Yun Nie and Jean{-}Pierre Chevallet and Marie{-}France Bruandet},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Between Terms and Words for European Language {IR} and Between Words and Bigrams for Chinese {IR}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {697--709},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/montreal.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NieCB97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ETH TREC-6: Routing, Chinese, Cross-Language and Spoken Document  Retrieval

_Bojidar Mateev, Eugen Munteanu, Paraic Sheridan, Martin Wechsler, Peter Schäuble_

- :fontawesome-solid-user-group: **Participant:** [ETH](./clir/participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ETH_notebook.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ETH_notebook.ps.gz)
- :material-file-search: **Runs:** [ETHdd1](./clir/runs.md#ethdd1) | [ETHde1](./clir/runs.md#ethde1) | [ETHde2](./clir/runs.md#ethde2) | [ETHde3](./clir/runs.md#ethde3) | [ETHdf1](./clir/runs.md#ethdf1) | [ETHdf2](./clir/runs.md#ethdf2) | [ETHed1](./clir/runs.md#ethed1) | [ETHed2](./clir/runs.md#ethed2) | [ETHed3](./clir/runs.md#ethed3) | [ETHed4](./clir/runs.md#ethed4) | [ETHee1](./clir/runs.md#ethee1) | [ETHfd1](./clir/runs.md#ethfd1) | [ETHfd2](./clir/runs.md#ethfd2) | [ETHff1](./clir/runs.md#ethff1)

??? abstract "Abstract"
	
	ETH Zurich's participation in TREC-6 consists of experiments in the main routing task, both manual and automatic runs in the Chinese retrieval track, cross-language retrieval in each of German, French and English as part of the new cross-language retrieval track, and experiments in speech recognition and retrieval under the new spoken document retrieval track. This year our routing experiments focused on the improvement of the feature selection strategy, on query expansion using similarity thesauri, on the grouping of features and on the combination of different retrieval methods. For Chinese retrieval we continued to rely on character bi-grams for indexing instead of attempting to segment and identify individual words, and we introduced a new manually-constructed stopword list consisting of almost 1,000 Chinese words. Experiments in cross-language retrieval focused heavily on our approach using multilingual similarity thesauri but also included several runs using machine translation technol-ogy. Finally, for the spoken document retrieval track our work included the development of a simple speaker-independent phoneme recogniser and some innovations in our probabilistic retrieval functions to compensate for speech recognition errors.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MateevMSWS97.bib) "
	```
	@inproceedings{DBLP:conf/trec/MateevMSWS97,
		author = {Bojidar Mateev and Eugen Munteanu and Paraic Sheridan and Martin Wechsler and Peter Sch{\"{a}}uble},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{ETH} {TREC-6:} Routing, Chinese, Cross-Language and Spoken Document Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {623--635},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ETH\_notebook.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MateevMSWS97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cross Language Retrieval with the Twenty-One system

_Wessel Kraaij, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [TNO](./clir/participants.md#tno)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/twentyone.ps.gz](http://trec.nist.gov/pubs/trec6/papers/twentyone.ps.gz)
- :material-file-search: **Runs:** [TNOde1](./clir/runs.md#tnode1) | [TNOde2](./clir/runs.md#tnode2) | [TNOdeMT1](./clir/runs.md#tnodemt1) | [TNOee](./clir/runs.md#tnoee) | [TNOfe1](./clir/runs.md#tnofe1) | [TNOfe2](./clir/runs.md#tnofe2) | [TNOnle1](./clir/runs.md#tnonle1) | [TNOnle2](./clir/runs.md#tnonle2) | [TNOde3](./clir/runs.md#tnode3) | [TNOde4](./clir/runs.md#tnode4) | [TNOde5](./clir/runs.md#tnode5) | [TNOde6](./clir/runs.md#tnode6) | [TNOfe3](./clir/runs.md#tnofe3) | [TNOfe4](./clir/runs.md#tnofe4) | [TNOfe5](./clir/runs.md#tnofe5) | [TNOfe6](./clir/runs.md#tnofe6) | [TNOnle3](./clir/runs.md#tnonle3) | [TNOnle4](./clir/runs.md#tnonle4) | [TNOnle5](./clir/runs.md#tnonle5) | [TNOnle6](./clir/runs.md#tnonle6)

??? abstract "Abstract"
	
	The EU project Twenty-One will support cross language queries in a multilingual document base. A prototype version of the Twenty-One system has been subjected to the Cross Language track tests in order to set baseline performances. The runs were based on query translation using dictionaries and corpus based disambiguation methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KraaijH97.bib) "
	```
	@inproceedings{DBLP:conf/trec/KraaijH97,
		author = {Wessel Kraaij and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Cross Language Retrieval with the Twenty-One system},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {753--760},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/twentyone.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KraaijH97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Phrase Discovery for English and Cross-language Retrieval at TREC  6

_Fredric C. Gey, Aitao Chen_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./clir/participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/brkly.ps.gz](http://trec.nist.gov/pubs/trec6/papers/brkly.ps.gz)
- :material-file-search: **Runs:** [BrklyG2GA](./clir/runs.md#brklyg2ga) | [BrklyE2GA](./clir/runs.md#brklye2ga) | [BrklyE2GM](./clir/runs.md#brklye2gm)

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

#### Xerox TREC-6 Site Report: Cross Language Text Retrieval

_Éric Gaussier, Gregory Grefenstette, David A. Hull, B. Maximilian Schulze_

- :fontawesome-solid-user-group: **Participant:** [Xerox](./clir/participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/xrce-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/xrce-trec6.ps.gz)
- :material-file-search: **Runs:** [XRCECLE2EA](./clir/runs.md#xrcecle2ea) | [XRCECLE2EM](./clir/runs.md#xrcecle2em) | [XRCECLF2FM](./clir/runs.md#xrceclf2fm) | [XRCECLF2FA](./clir/runs.md#xrceclf2fa) | [XRCECLF2EA](./clir/runs.md#xrceclf2ea) | [XRCECLF2EM](./clir/runs.md#xrceclf2em) | [XRCECLE2FM](./clir/runs.md#xrcecle2fm) | [XRCECLE2FA](./clir/runs.md#xrcecle2fa)

??? abstract "Abstract"
	
	Xerox participated in the Cross Language Information Retrieval (CLIR) track of TREC-6. This track examines the problem of retrieving documents written in one language using queries written in another language. Our approach is to use a bilingual dictionary at query time to construct a target language version of the original query. We concentrate our experiments this year on manual query construction based on a weighted boolean model and on an automatic method for the translation of multi-word units. We also introduce a new derivational stemming algorithm whose word classes are generated automatically from a monolingual lexicon. We present our results on the 22 TREC-6 CLIR topics which have been assessed and briefly discuss the problems inherent in the cross-language IR task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaussierGHS97.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaussierGHS97,
		author = {{\'{E}}ric Gaussier and Gregory Grefenstette and David A. Hull and B. Maximilian Schulze},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Xerox {TREC-6} Site Report: Cross Language Text Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {775--788},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/xrce-trec6.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GaussierGHS97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Free Resources And Advanced Alignment For Cross-Language Text Retrieval

_Mark W. Davis, William C. Ogden_

- :fontawesome-solid-user-group: **Participant:** [NMSU-D](./clir/participants.md#nmsu-d)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/nmsu-clir.ps.gz](http://trec.nist.gov/pubs/trec6/papers/nmsu-clir.ps.gz)
- :material-file-search: **Runs:** [clcrl1](./clir/runs.md#clcrl1) | [clcrl2](./clir/runs.md#clcrl2) | [clcrl3](./clir/runs.md#clcrl3) | [clcrl4](./clir/runs.md#clcrl4)

??? abstract "Abstract"
	
	For the Cross-Language Text Retrieval Track in TREC 6, NMSU experimented with a new approach to deriving translation equivalents from parallel text databases, and also investigated performing automatic, dictionary-based translation of query terms by using a dictionary that could be queried remotely via the World Wide Web. The new approach to building bilingual translation lexicons involved aligning parallel texts at the sentence level, and then performing further alignments at the sub-sentence level. The process initially chooses alignment anchors based on N-gram matches between cognate terms. Term and phrase matching is then performed between the anchor points by finding the most direct path from one anchor to the next, penalizing larger steps over runs of terms. The collected term translations are then used as equivalents for a query translation process and the translated query is then submitted to a monolingual retrieval engine. The results are compared against the performance of a monolingual French-French retrieval system, and against a translated query formed from a very high-quality bilingual dictionary accessed directly over the World Wide Web. A combined approach is also presented that uses terminology from both the dictionary and, where the dictionary lacks coverage, supplements the query translation using terms from a parallel text database.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DavisO97.bib) "
	```
	@inproceedings{DBLP:conf/trec/DavisO97,
		author = {Mark W. Davis and William C. Ogden},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Free Resources And Advanced Alignment For Cross-Language Text Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {385--395},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/nmsu-clir.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DavisO97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Clustering and SuperConcepts Within SMART: TREC 6

_Chris Buckley, Mandar Mitra, Janet A. Walz, Claire Cardie_

- :fontawesome-solid-user-group: **Participant:** [Cornell](./clir/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/cornell.ps.gz](http://trec.nist.gov/pubs/trec6/papers/cornell.ps.gz)
- :material-file-search: **Runs:** [Cor6FFsc](./clir/runs.md#cor6ffsc) | [Cor6EFexp](./clir/runs.md#cor6efexp) | [Cor6EFent](./clir/runs.md#cor6efent) | [Cor6ETGsc](./clir/runs.md#cor6etgsc) | [Cor6EEsc](./clir/runs.md#cor6eesc)

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

#### Mercure at TREC6

_Mohand Boughanem, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./clir/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/irit.ps.gz](http://trec.nist.gov/pubs/trec6/papers/irit.ps.gz)
- :material-file-search: **Runs:** [MercureFFs](./clir/runs.md#mercureffs) | [MercureFFl](./clir/runs.md#mercureffl)

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

- :fontawesome-solid-user-group: **Participant:** [UMass](./clir/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [INQ4xl1](./clir/runs.md#inq4xl1) | [INQ4xl2](./clir/runs.md#inq4xl2)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIR) at the University of Massachusetts participated in eight of the ten tracks that were part of the TREC-6 workshop. We started with the two required tracks, ad-hoc and routing, but then included VLC, Filtering, Chinese, Cross-language, SDR, and Interactive. We omitted NLP and High Precision for want of time and energy. With so many tracks involved, it is nearly inevitable that something will go wrong. Despite our best efforts at verifying all aspects of each track-before, during, and after the experiments we once again made mistakes that were minor in scope, but major in consequence. Those mistakes affected our results in Ad-hoc and Routing, as well as the dependent tracks of VLC and Filtering. The details of the mistakes are presented in each track's discussion, along with information comparing the submitted runs to the corrected runs. Unfortunately, those corrected runs are not included in TREC-6 summary information. This remainder of this report covers our approach to each of the tracks as well as some experimental results and analysis. We start with an overview of the major tools that were used across all tracks. The paper is divided into the following sections. The track descriptions are generally broken into approach, results, and analysis sections, though some tracks require a different description.
	

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

## Filtering 

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

- :fontawesome-solid-user-group: **Participant:** [City](./filtering/participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz](http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz)
- :material-file-search: **Runs:** [city6f21](./filtering/runs.md#city6f21) | [city6f22](./filtering/runs.md#city6f22) | [city6f23](./filtering/runs.md#city6f23) | [city6f11](./filtering/runs.md#city6f11) | [city6f12](./filtering/runs.md#city6f12) | [city6f13](./filtering/runs.md#city6f13)

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

- :fontawesome-solid-user-group: **Participant:** [UNC-N](./filtering/participants.md#unc-n)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/newby-t6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/newby-t6.ps.gz)
- :material-file-search: **Runs:** [isf1](./filtering/runs.md#isf1) | [isf1r](./filtering/runs.md#isf1r) | [isf2](./filtering/runs.md#isf2) | [isf2r](./filtering/runs.md#isf2r)

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

- :fontawesome-solid-user-group: **Participant:** [ANU](./filtering/participants.md#anu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz](http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz)
- :material-file-search: **Runs:** [anu6fltU1](./filtering/runs.md#anu6fltu1) | [anu6fltU2](./filtering/runs.md#anu6fltu2)

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

- :fontawesome-solid-user-group: **Participant:** [Siemens](./filtering/participants.md#siemens)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/siemens.ps.gz](http://trec.nist.gov/pubs/trec6/papers/siemens.ps.gz)
- :material-file-search: **Runs:** [teklis1000](./filtering/runs.md#teklis1000) | [teklis6](./filtering/runs.md#teklis6) | [teklis65](./filtering/runs.md#teklis65) | [teklis7](./filtering/runs.md#teklis7) | [teklis75](./filtering/runs.md#teklis75)

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

- :fontawesome-solid-user-group: **Participant:** [DBenz](./filtering/participants.md#dbenz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/dbulm.ps.gz](http://trec.nist.gov/pubs/trec6/papers/dbulm.ps.gz)
- :material-file-search: **Runs:** [dbulm1fF1](./filtering/runs.md#dbulm1ff1) | [dbulm1fF2](./filtering/runs.md#dbulm1ff2) | [dbulm1Asp](./filtering/runs.md#dbulm1asp) | [dbulm1fF2R](./filtering/runs.md#dbulm1ff2r) | [dbulm1F1R](./filtering/runs.md#dbulm1f1r)

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

- :fontawesome-solid-user-group: **Participant:** [UMass](./filtering/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [INQ415](./filtering/runs.md#inq415) | [INQ416](./filtering/runs.md#inq416) | [INQ417](./filtering/runs.md#inq417) | [INQ418](./filtering/runs.md#inq418) | [INQ419](./filtering/runs.md#inq419) | [INQ420](./filtering/runs.md#inq420) | [INQ421](./filtering/runs.md#inq421) | [INQ422](./filtering/runs.md#inq422) | [INQ423](./filtering/runs.md#inq423) | [INQ424](./filtering/runs.md#inq424)

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

## High-Precision 

#### TREC 6 High-Precision Track

_Chris Buckley_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/hp_track.ps.gz](http://trec.nist.gov/pubs/trec6/papers/hp_track.ps.gz)
??? abstract "Abstract"
	
	The TREC High-Precision (HP) track compares systems on the simple 'Real World' task of having users finding a few relevant documents as quickly as possible. Five groups are participating with each happening to emphasize different aspects of the retrieval process, from visualization to structured queries to relevance feedback. With so few groups participating in this inaugural run of the the track, no decisive conclusions can be reached. However, the indications are that simple approaches work very well.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Buckley97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Buckley97,
		author = {Chris Buckley},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC} 6 High-Precision Track},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {69--71},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/hp\_track.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Buckley97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad hoc Retrieval Using Thresholds, WSTs for French Mono-lingual Retrieval,  Document-at-a-Glance for High Precision and Triphone Windows for Spoken  Documents

_Alan F. Smeaton, Fergus Kelledy, Gerard Quinn_

- :fontawesome-solid-user-group: **Participant:** [Dublin](./hp/participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz](http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz)
- :material-file-search: **Runs:** [DCU97HP](./hp/runs.md#dcu97hp)

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

#### Passage-Based Refinement (MultiText Experiements for TREC-6)

_Gordon V. Cormack, Charles L. A. Clarke, Christopher R. Palmer, Samuel S. L. To_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./hp/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz](http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz)
- :material-file-search: **Runs:** [uwmt6h0](./hp/runs.md#uwmt6h0) | [uwmt6h1](./hp/runs.md#uwmt6h1) | [uwmt6h2](./hp/runs.md#uwmt6h2)

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

## Interactive 

#### TREC-6 Interactive Report

_Paul Over_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/t6irep.ps.gz](http://trec.nist.gov/pubs/trec6/papers/t6irep.ps.gz)
??? abstract "Abstract"
	
	This report is an introduction to the work of the TREC-6 Interactive Track with its goal of investigating interactive information retrieval by examining the process as well as the results. Twelve interactive information retrieval (IR) systems were run on a shared problem: a question-answering task, 6 statements of information need, and a collection of 210,158 articles from the Financial Times of London 1991-1994. The track specification called for two levels of experimentation: cross-site system comparisons in terms of simple measures of end results and local experiments with their own hypotheses and attention to the search process. This report summarizes the cross-site experiment. It refers the reader to separate discussions of the experiments performed at each participating site - their hypotheses, experimental systems, and results. The cross-site experiment can be seen as a case study in the application of experimental design principles and the use of a shared control IR system in addressing the problems of comparing experimental interactive IR systems across sites: isolating the effects of topics, human searchers, and other site-specific factors within an affordable design. The cross-site results confirm the dominance of the topic effect, show the searcher effect is almost as often absent as present, and indicate that for several sites the 2-factor interactions are negligible. An analysis of variance found the system effect to be significant, but a multiple comparisons test found no significant pairwise differences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Over97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Over97,
		author = {Paul Over},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-6} Interactive Report},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {73--81},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/t6irep.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Over97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Retrieval using IRIS: TREC-6 Experiments

_Robert G. Sumner Jr., Kiduk Yang, Roger Akers, William M. Shaw Jr._

- :fontawesome-solid-user-group: **Participant:** [UNC-S](./interactive/participants.md#unc-s)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/unc-sumner.ps.gz](http://trec.nist.gov/pubs/trec6/papers/unc-sumner.ps.gz)
- :material-file-search: **Runs:** [Iunc](./interactive/runs.md#iunc)

??? abstract "Abstract"
	
	For the TREC-5, Category B adhoc task, we examined the effectiveness of two relevance feedback models: an adaptive linear model and a probabilistic model (Sumner & Shaw, 1997). The models were shown to be effective, especially when the relevance assessments of the searchers matched those of the official TREC judges. During feedback, the query was expanded by a large number of terms from the retrieved documents. Some queries were expanded by as many as 1000 terms. Building on the basic framework of our TREC-S system, we developed an interactive, Web-based retrieval system called IRIS (Information Retrieval Interactive System ) for TREC-6. Although IRIS inherits both the adaptive linear and the probabilistic model from the TREC-5 system, we made significant modifications to the implementation of both models in order to use a three-valued scale of relevance during feedback. Furthermore, we expanded the scope of human interaction with the system. For example, throughout the search process, the searcher can add and delete query terms as well as change their weights. Moreover, statistically significant, two-word collocations have been added to the term index. IRIS uses collocations not only in formulating the feedback query, but also in presenting to the searcher 'suggested phrases' (i.e., collocations related to the initial query), prior to the first document retrieval pass. Finally, as with our TREC-5 system, during feedback the query is expanded by a large number of terms. However, for reasons of efficiency, the number of terms in the query was limited to 300 in our TREC-6 system. The primary focus of our TREC-6 experiments was on the interactive track and the manual, Category B adhoc task. People were hired to conduct searches for these runs. Here, we are interested not only in the official TREC results but also (perhaps more so) in the reactions of the searchers to the various features of IRIS.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SumnerYAJ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SumnerYAJ97,
		author = {Robert G. Sumner Jr. and Kiduk Yang and Roger Akers and William M. Shaw Jr.},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Interactive Retrieval using {IRIS:} {TREC-6} Experiments},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {711--733},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/unc-sumner.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SumnerYAJ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM Search UI Prototype Evaluation at the Interactive Track of  TREC-6

_Birgit Schmidt-Wesche, Robert Mack, Christian Lenz Cesar, David VanEsselstyn_

- :fontawesome-solid-user-group: **Participant:** [IBM-Brown](./interactive/participants.md#ibm-brown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ibm-interactive.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ibm-interactive.ps.gz)
- :material-file-search: **Runs:** [Iibm](./interactive/runs.md#iibm)

??? abstract "Abstract"
	
	Our search application used in the TREC6 Interactive Track was developed as part of a User-Centered Design (UCD) program aimed at prototyping Ul approaches for using different search technologies being investigated at IBM Research. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Schmidt-WescheMCV97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Schmidt-WescheMCV97,
		author = {Birgit Schmidt{-}Wesche and Robert Mack and Christian Lenz Cesar and David VanEsselstyn},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{IBM} Search {UI} Prototype Evaluation at the Interactive Track of {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {517--534},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ibm-interactive.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Schmidt-WescheMCV97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Information Retrieval Using Term Relationship Networks

_Jim McDonald, William C. Ogden, Peter W. Foltz_

- :fontawesome-solid-user-group: **Participant:** [NMSU-C](./interactive/participants.md#nmsu-c)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/nmsu-interactive.ps.gz](http://trec.nist.gov/pubs/trec6/papers/nmsu-interactive.ps.gz)
- :material-file-search: **Runs:** [Inmsu](./interactive/runs.md#inmsu)

??? abstract "Abstract"
	
	Users have difficulty retrieving information from ad-hoc, textual databases because, by definition, they don't know precisely what's in them. Thus, users submit queries that contain the wrong terms or which don't contain enough information to retrieve all and only those documents relevant to their information needs. Our approach to these problems is to provide users with abstract representations of database con-tent, in the form of Pathfinder networks linking related terms used in the database. This allows users to recognize and select appropriate query terms. The networks displayed to users are derived from textual analyses of documents retrieved from initial queries and, thus, the process can be thought of as a form of relevance feedback. Compared to other relevance feedback methods, however, the network displays can show important relationships between the query terms and terms suggested by the system. In the study to be reported, we compared the performance of two information retrieval systems Zprise, a control system, and InfoView, a system that uses our network displays. Participants used both systems to perform an 'aspectual retrieval' task using the six topics. Preliminary results from this study suggest that when participants used InfoView they took less time to identify topic aspects and were at least as successful as when they used Zprise.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McDonaldOF97.bib) "
	```
	@inproceedings{DBLP:conf/trec/McDonaldOF97,
		author = {Jim McDonald and William C. Ogden and Peter W. Foltz},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Interactive Information Retrieval Using Term Relationship Networks},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {379--384},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/nmsu-interactive.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/McDonaldOF97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cheshire II at TREC 6: Interactive Probabilistic Retrieval

_Ray R. Larson, Jerome McDonough_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./interactive/participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/brkly_interactive.ps.gz](http://trec.nist.gov/pubs/trec6/papers/brkly_interactive.ps.gz)
- :material-file-search: **Runs:** [Iberkeley](./interactive/runs.md#iberkeley)

??? abstract "Abstract"
	
	This paper briefly describes the features of the Cheshire II system and how it was used in the TREC 6 Interactive track. The results of the interactive track are discussed and future improvements to the Cheshire II system are considered.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LarsonM97.bib) "
	```
	@inproceedings{DBLP:conf/trec/LarsonM97,
		author = {Ray R. Larson and Jerome McDonough},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Cheshire {II} at {TREC} 6: Interactive Probabilistic Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {649--659},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/brkly\_interactive.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LarsonM97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Comparison of Boolean and Natural Language Searching for the TREC-6  Interactive Task

_William R. Hersh, Bikram Day_

- :fontawesome-solid-user-group: **Participant:** [OHSU](./interactive/participants.md#ohsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ohsu.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ohsu.ps.gz)
- :material-file-search: **Runs:** [Iohsu](./interactive/runs.md#iohsu)

??? abstract "Abstract"
	
	The TREC-6 interactive task used a multi-site experimental protocol, where each participating site compared an 'experimental' system with a common 'control' system used at all sites. For the Oregon Health Sciences University site, the 'experimental' system was a Boolean interface to the MG system, while the control system was, as for all sites, the natural language ZPRISE system. Performance was measured by aspectual recall and precision. OHSU searchers did well overall, achieving the highest overall aspectual precision. These searchers did obtain below-average aspectual recall overall, although they achieved above-average aspectual recall with the control system, indicating that for the TREC-6 interactive task, a natural language searching system was superior to a Boolean one.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershD97.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershD97,
		author = {William R. Hersh and Bikram Day},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {A Comparison of Boolean and Natural Language Searching for the {TREC-6} Interactive Task},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {585--595},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ohsu.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HershD97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MDS TREC6 Report

_Michael Fuller, Marcin Kaszkiel, Chien Leng Ng, Phil Vines, Ross Wilkinson, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [MDS](./interactive/participants.md#mds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz](http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz)
- :material-file-search: **Runs:** [Irmit](./interactive/runs.md#irmit)

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

#### The GURU System in TREC-6

_Eric W. Brown, Herb A. Chong_

- :fontawesome-solid-user-group: **Participant:** [IBM-Brown](./interactive/participants.md#ibm-brown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ibm_brown.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ibm_brown.ps.gz)
- :material-file-search: **Runs:** [Iibm](./interactive/runs.md#iibm)

??? abstract "Abstract"
	
	As the on-line world grows and increases its role in our daily lives, the problems of searching, categorizing, and understanding textual information become ever more important. While researchers and practitioners have made much progress in these areas over the last thirty years, anyone who has gone to the World Wide Web seeking information and returned with more frustration than answers can attest that much work remains. Today's important issues cover topics such as scalability, user interfaces, and techniques that exploit the unique hypermedia features of Web environments. To support our research in these areas, the Text Analysis and Advanced Search department at the IBM T. J. Watson Research Center has developed an experimental probabilistic text retrieval system called Guru[4]. Guru was originally built to explore new probabilistic ranking algorithms, and now serves as a test-bed for much of our text analysis, search, and categorization work. Guru may be run as a stand-alone system or in a client/server configuration. The Guru indexer performs minimal case and hyphen normalization, but otherwise indexes all words (including stop words) in their original form. The index includes document, paragraph, sentence, and word-in-sentence positional information for each word occurrence in the document collection. At search time, queries are input to Guru in a free-text format. Stop words are eliminated from the query and morphological variants for each query term are automatically generated and added as synonyms to the query term. Syntax is provided that allows the user to control morphological expansion and stop word elimination. Guru ranks documents using a probabilistic algorithm that considers the frequency statistics of the query terms in individual documents and the collection as a whole. Guru also considers lexical affinities (LAs), which are co-occurrences of two terms within a given distance. These automatically identified 'phrases' are ranked higher than instances of the component words occurring outside of the LA distance. Our purpose in participating in TREC-6 is four-fold. First, we continue to refine the base probabilistic ranking algorithm in Guru and wish to evaluate its performance on a large, standard test set. Second, we are developing a prototype user interface and seek initial feedback and guidance for further development. Third, we are interested in text search scalability as an issue orthogonal to the basic problems of search and categorization and seek feedback on initial attempts to address this issue. Fourth, hypermedia domains, such as the World Wide Web, are an increasingly important arena for application of text analysis and search technology. Such domains, however, pose a challenge for evaluation since both search and navigation must be considered by the evaluation metric. We hope that this issue will be addressed by the TREC community with the ultimate goal of defining appropriate evaluation metrics and building suitable test collections. Toward these ends, we are participating in the Ad-hoc Task, the Interactive Track, and the Very Large Corpus Track of TREC-6.
	

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

#### Rutgers' TREC-6 Interactive Track Experience

_Nicholas J. Belkin, Jose Perez Carballo, Colleen Cool, Shin-jeng Lin, Soyeon Park, Soo Young Rieh, Pamela A. Savage-Knepshield, C. Sikora, Hong (Iris) Xie, James Allan_

- :fontawesome-solid-user-group: **Participant:** [RutgersB](./interactive/participants.md#rutgersb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ruint-paper2.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ruint-paper2.ps.gz)
- :material-file-search: **Runs:** [Irutgers](./interactive/runs.md#irutgers)

??? abstract "Abstract"
	
	The goal of the Rutgers TREC-6 Interactive Track study was to compare the performance and usability of a system offering positive relevance feedback with one offering positive and negative relevance feedback. Our hypothesis was that the latter system would better support the aspect identification task than the former. Although aspectual recall was higher for the system supporting both kinds of relevance feedback (0.53 vs. 0.46), the difference was not significant, possibly because of the small number of subjects (four in each condition, each doing three searches). Usability results were also equivocal, perhaps due to the complexity of the system. Compared to ZPRISE, the control system without relevance feedback, both relevance feedback systems were rated more difficult to learn to use, but more effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinCCLPRSSXA97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinCCLPRSSXA97,
		author = {Nicholas J. Belkin and Jose Perez Carballo and Colleen Cool and Shin{-}jeng Lin and Soyeon Park and Soo Young Rieh and Pamela A. Savage{-}Knepshield and C. Sikora and Hong (Iris) Xie and James Allan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Rutgers' {TREC-6} Interactive Track Experience},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {597--610},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ruint-paper2.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BelkinCCLPRSSXA97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Okapi at TREC-6

_Micheline Hancock-Beaulieu, Mike Gatford_

- :fontawesome-solid-user-group: **Participant:** [City](./interactive/participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/city-interactive.ps.gz](http://trec.nist.gov/pubs/trec6/papers/city-interactive.ps.gz)
- :material-file-search: **Runs:** [Icity](./interactive/runs.md#icity)

??? abstract "Abstract"
	
	A full description of the experimental system and conditions is given in Appendices A and B. Searchers filled in three types of questionnaires. The pre-session questionnaire established the user's experience and profile. In the post search questionnaires, searchers were asked questions regarding the topic, the search and the system used after undertaking each individual search. Finally in the post-session questionnaire, subjects were asked to provide an overview of the experiment. In addition to the questionnaires, searchers noted on a worksheet the different aspects of the topics they encountered whilst they undertook each search. A total of eight subjects completed forty eight searches, that is three searches on each of the two systems, Okapi and ZPrise. The sessions were divided into two rounds of four searchers. Of the two groups who carried out the twenty-four searches on Okapi, Group A used the same interface as in TREC-5, but with incremental query expansion modified (Appendix A.3.2), and Group B searched a slightly different version which allowed the searcher to cancel the relevance feedback process or clear the query (Appendix A.4).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BeaulieuG97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BeaulieuG97,
		author = {Micheline Hancock{-}Beaulieu and Mike Gatford},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Interactive Okapi at {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {143--167},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/city-interactive.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BeaulieuG97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY Does Battle With TREC-6

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, Donald Byrd, Russell C. Swan, Jinxi Xu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./interactive/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [Iumass](./interactive/runs.md#iumass)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in eight of the ten tracks that were part of the TREC-6 workshop. We started with the two required tracks, ad-hoc and routing, but then included VLC, Filtering, Chinese, Cross-language, SDR, and Interactive. We omitted NLP and High Precision for want of time and energy. With so many tracks involved, it is nearly inevitable that something will go wrong. Despite our best efforts at verifying all aspects of each track-before, during, and after the experiments-we once again made mistakes that were minor in scope, but major in consequence. Those mistakes affected our results in Ad-hoc and Routing, as well as the dependent tracks of VLC and Filtering. The details of the mistakes are presented in each track's discussion, along with information comparing the submitted runs to the corrected runs. Unfortunately, those corrected runs are not included in TREC-6 summary information. This remainder of this report covers our approach to each of the tracks as well as some experimental results and analysis. We start with an overview of the major tools that were used across all tracks. The paper is divided into the following sections. The track descriptions are generally broken into approach, results, and analysis sections, though some tracks require a different description.
	

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

## NLP 

#### Natural Language Information Retrieval TREC-6 Report

_Tomek Strzalkowski, Fang Lin, Jose Perez Carballo_

- :fontawesome-solid-user-group: **Participant:** [GE](./nlp/participants.md#ge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ge.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ge.ps.gz)
- :material-file-search: **Runs:** [genlp1](./nlp/runs.md#genlp1) | [genlp2](./nlp/runs.md#genlp2) | [genlp3](./nlp/runs.md#genlp3)

??? abstract "Abstract"
	
	Natural language processing techniques may hold a tremendous potential for overcoming the inadequacies of purely quantitative methods of text information retrieval, but the empirical evidence to support such predictions has thus far been inadequate, and appropriate scale evaluations have been slow to emerge. In this chapter, we report on the progress of the Natural Language Information Retrieval project, a joint effort of several sites led by GE Research, and its evaluation in the 6th Text Retrieval Conferences (TREC-6).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StrzalkowskiLC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/StrzalkowskiLC97,
		author = {Tomek Strzalkowski and Fang Lin and Jose Perez Carballo},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Natural Language Information Retrieval {TREC-6} Report},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {347--366},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ge.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/StrzalkowskiLC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Short Queries, Natural Language and Spoken Document Retrieval: Experiments  at Glasgow University

_Fabio Crestani, Mark Sanderson, Marcos Theophylactou, Mounia Lalmas_

- :fontawesome-solid-user-group: **Participant:** [Glasgow](./nlp/participants.md#glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/glasgow.ps.gz](http://trec.nist.gov/pubs/trec6/papers/glasgow.ps.gz)
- :material-file-search: **Runs:** [Gla6DS1](./nlp/runs.md#gla6ds1) | [Gla6DS2](./nlp/runs.md#gla6ds2) | [Gla6DS3](./nlp/runs.md#gla6ds3)

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

## Spoken Document Retrieval 

#### TREC-6 1997 Spoken Document Retrieval Track Overview and Results

_John S. Garofolo, Ellen M. Voorhees, Vincent M. Stanford, Karen Sparck Jones_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/sdr97.ps.gz](http://trec.nist.gov/pubs/trec6/papers/sdr97.ps.gz)
??? abstract "Abstract"
	
	This paper describes the 1997 TREC-6 Spoken Document Retrieval (SDR) Track which implemented a first evaluation of retrieval of broadcast news excerpts using a combination of automatic speech recognition and information retrieval technologies. The motivations behind the SDR Track and background regarding its development and implementation are discussed. The SDR evaluation collection and topics are described and summaries and analyses of the results of the track are presented. Finally, plans for future SDR tracks are described. Since this was the first implementation of an evaluation of SDR, the evaluation itself as well as the evaluated technology should be considered experimental. The results of the first SDR Track were very encouraging and showed us that SDR could be successfully implemented and evaluated. However, the results of the SDR Track should be considered preliminary since the 50-hour spoken document collection used was very small for retrieval experiments (even though it was considered extremely large for speech recognition purposes.) Nonetheless, with thirteen groups participating in the TREC-6 SDR Track, a considerable amount of experience was gained in implementing and evaluating the SDR task. This experience will greatly benefit the next 1998 TREC-7 SDR Track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarofoloVSJ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarofoloVSJ97,
		author = {John S. Garofolo and Ellen M. Voorhees and Vincent M. Stanford and Karen Sparck Jones},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-6} 1997 Spoken Document Retrieval Track Overview and Results},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {83--91},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/sdr97.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GarofoloVSJ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad hoc Retrieval Using Thresholds, WSTs for French Mono-lingual Retrieval,  Document-at-a-Glance for High Precision and Triphone Windows for Spoken  Documents

_Alan F. Smeaton, Fergus Kelledy, Gerard Quinn_

- :fontawesome-solid-user-group: **Participant:** [Dublin](./sdr/participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz](http://trec.nist.gov/pubs/trec6/papers/DCU-TREC-6-Procs.ps.gz)
- :material-file-search: **Runs:** [DCU97QSDRB1](./sdr/runs.md#dcu97qsdrb1) | [DCU97QSDRB2](./sdr/runs.md#dcu97qsdrb2) | [DCU97QSDRR1](./sdr/runs.md#dcu97qsdrr1) | [DCU97QSDRR2](./sdr/runs.md#dcu97qsdrr2)

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

#### AT&T at TREC-6: SDR Track

_Amit Singhal, John Choi, Donald Hindle, Fernando C. N. Pereira_

- :fontawesome-solid-user-group: **Participant:** [ATT](./sdr/participants.md#att)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/att.speech.ps.gz](http://trec.nist.gov/pubs/trec6/papers/att.speech.ps.gz)
- :material-file-search: **Runs:** [att97sB1](./sdr/runs.md#att97sb1) | [att97sR1](./sdr/runs.md#att97sr1) | [att97sS1](./sdr/runs.md#att97ss1) | [att97sS2](./sdr/runs.md#att97ss2)

??? abstract "Abstract"
	
	In the spoken document retrieval track, we study how higher word-recall-recognizing many of the spoken words affects the retrieval effectiveness for speech documents, given that high word-recall comes at a cost of low word-precision-recognizing many words that were not actually spoken. We hypothesize that information retrieval algorithms would benefit from a higher word-recall and are robust against poor word-precision. Start-up difficulties with recognition for this task kept us from doing an systematic study of the effect of varying levels of word-recall and word-precision on retrieval effectiveness from speech. We simulated a high word-recall and a poor word-precision system by merging the output of several recognizers. Experiments suggest that having higher word-recall does improve the retrieval effectiveness from speech.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinghalCHP97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinghalCHP97,
		author = {Amit Singhal and John Choi and Donald Hindle and Fernando C. N. Pereira},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {AT{\&}T at {TREC-6:} {SDR} Track},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {227--232},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/att.speech.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SinghalCHP97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Spoken Document Retrieval at CMU

_Matthew Siegler, Michael J. Witbrock, Seán Slattery, Kristie Seymore, R. E. Jones, Alexander G. Hauptmann_

- :fontawesome-solid-user-group: **Participant:** [CMU](./sdr/participants.md#cmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/cmu.trecSDR97-report.ps.gz](http://trec.nist.gov/pubs/trec6/papers/cmu.trecSDR97-report.ps.gz)
- :material-file-search: **Runs:** [CMUref](./sdr/runs.md#cmuref) | [CMUibm](./sdr/runs.md#cmuibm) | [CMUcmu](./sdr/runs.md#cmucmu)

??? abstract "Abstract"
	
	We describe our submission to the TREC-6 Spoken Document Retrieval (SDR) track and the speech recognition and the information retrieval engines. We present SDR evaluation results and a brief analysis. A few developments and experiments are also described in detail including: Vocabulary size experiments, which assess the effect of words missing from the speech recognition vocabulary. For our 51,000-word vocabulary the effect was minimal. Speech recognition using a stemmed language model, where the model statistics of words containing the same root are combined. Stemmed language models did not improve speech recognition or information retrieval. Merging the IBM and CMU speech recognition data. Combining the results of two independent recognition systems slightly boosted information retrieval results. Confidence annotations that estimate of the correctness of each recognized word. Confidence annotations did not appear to improve retrieval. N-best lists where the top recognizer hypotheses are used for information retrieval. Using the top 50 hypotheses dramatically improved performance in the test set. Effects of corpus size on the SDR task. As more documents are added to the task, the gap between perfect retrieval and retrieving spoken documents gets larger. This makes it clear that the size of the current TREC SDR track corpus is too small for obtaining meaningful results. While we have done preliminary experiments with these approaches, most of them were not part of our submission, since their impact on the IR performance on the actual TREC SDR training corpus was too marginal for reliable experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SieglerWSSJH97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SieglerWSSJH97,
		author = {Matthew Siegler and Michael J. Witbrock and Se{\'{a}}n Slattery and Kristie Seymore and R. E. Jones and Alexander G. Hauptmann},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments in Spoken Document Retrieval at {CMU}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {291--302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/cmu.trecSDR97-report.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SieglerWSSJH97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Text Retrieval via Semantic Forests

_Patrick Schone, Jeffrey L. Townsend, Thomas H. Crystal, Calvin Olano_

- :fontawesome-solid-user-group: **Participant:** [NSA](./sdr/participants.md#nsa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/nsa-rev.ps.gz](http://trec.nist.gov/pubs/trec6/papers/nsa-rev.ps.gz)
- :material-file-search: **Runs:** [nsasglt1](./sdr/runs.md#nsasglt1) | [nsasgsr1](./sdr/runs.md#nsasgsr1)

??? abstract "Abstract"
	
	We approached our first participation in TREC with an interest in performing retrieval on the output of automatic speech-to-text (speech recognition) systems and a background in performing topic-labeling on such output. Our primary thrust, therefore, was to participate in the SDR track. In conformance with the rules, we also participated in the Ad Hoc text-retrieval task, to create a baseline for comparing our converted topic-labeling system with other approaches to IR and to assess the effect of speech-transcription errors. A second thrust was to explore rapid prototyping of an IR system, given the existing topic-labeling software. Our IR system makes use of software called Semantic Forests which is based on an algorithm originally developed for labeling topics in text and transcribed speech (Schone & Nelson, ICASSP 96). Topic-labelling is not an IR task, so Semantic Forests was adapted for use in TREC over an eight-week period for the Ad Hoc task, with an additional two weeks for SDR. In what follows, we describe our system as well as experiments, timings, results, and future directions with these techniques.
	

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

#### ETH TREC-6: Routing, Chinese, Cross-Language and Spoken Document  Retrieval

_Bojidar Mateev, Eugen Munteanu, Paraic Sheridan, Martin Wechsler, Peter Schäuble_

- :fontawesome-solid-user-group: **Participant:** [ETH](./sdr/participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ETH_notebook.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ETH_notebook.ps.gz)
- :material-file-search: **Runs:** [ETHS1](./sdr/runs.md#eths1) | [ETHB1](./sdr/runs.md#ethb1) | [ETHR1](./sdr/runs.md#ethr1) | [ETHS2](./sdr/runs.md#eths2) | [ETHB2](./sdr/runs.md#ethb2)

??? abstract "Abstract"
	
	ETH Zurich's participation in TREC-6 consists of experiments in the main routing task, both manual and automatic runs in the Chinese retrieval track, cross-language retrieval in each of German, French and English as part of the new cross-language retrieval track, and experiments in speech recognition and retrieval under the new spoken document retrieval track. This year our routing experiments focused on the improvement of the feature selection strategy, on query expansion using similarity thesauri, on the grouping of features and on the combination of different retrieval methods. For Chinese retrieval we continued to rely on character bi-grams for indexing instead of attempting to segment and identify individual words, and we introduced a new manually-constructed stopword list consisting of almost 1,000 Chinese words. Experiments in cross-language retrieval focused heavily on our approach using multilingual similarity thesauri but also included several runs using machine translation technol-ogy. Finally, for the spoken document retrieval track our work included the development of a simple speaker-independent phoneme recogniser and some innovations in our probabilistic retrieval functions to compensate for speech recognition errors.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MateevMSWS97.bib) "
	```
	@inproceedings{DBLP:conf/trec/MateevMSWS97,
		author = {Bojidar Mateev and Eugen Munteanu and Paraic Sheridan and Martin Wechsler and Peter Sch{\"{a}}uble},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{ETH} {TREC-6:} Routing, Chinese, Cross-Language and Spoken Document Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {623--635},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ETH\_notebook.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MateevMSWS97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MDS TREC6 Report

_Michael Fuller, Marcin Kaszkiel, Chien Leng Ng, Phil Vines, Ross Wilkinson, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [MDS](./sdr/participants.md#mds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz](http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz)
- :material-file-search: **Runs:** [mds612](./sdr/runs.md#mds612) | [mds613](./sdr/runs.md#mds613) | [mds614](./sdr/runs.md#mds614) | [mds615](./sdr/runs.md#mds615)

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

#### Short Queries, Natural Language and Spoken Document Retrieval: Experiments  at Glasgow University

_Fabio Crestani, Mark Sanderson, Marcos Theophylactou, Mounia Lalmas_

- :fontawesome-solid-user-group: **Participant:** [Glasgow](./sdr/participants.md#glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/glasgow.ps.gz](http://trec.nist.gov/pubs/trec6/papers/glasgow.ps.gz)
- :material-file-search: **Runs:** [gla6B1](./sdr/runs.md#gla6b1) | [gla6R1](./sdr/runs.md#gla6r1) | [gla6S1](./sdr/runs.md#gla6s1) | [gla6S2](./sdr/runs.md#gla6s2)

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

#### INQUERY Does Battle With TREC-6

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, Donald Byrd, Russell C. Swan, Jinxi Xu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./sdr/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [INQ4sdd](./sdr/runs.md#inq4sdd) | [INQ4sds](./sdr/runs.md#inq4sds) | [INQ4sdl](./sdr/runs.md#inq4sdl)

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

#### The THISL Spoken Document Retrieval System

_Dave Abberley, Steve Renals, Gary D. Cook, Anthony J. Robinson_

- :fontawesome-solid-user-group: **Participant:** [Sheffield](./sdr/participants.md#sheffield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/sheffield.ps.gz](http://trec.nist.gov/pubs/trec6/papers/sheffield.ps.gz)
- :material-file-search: **Runs:** [THISLB1](./sdr/runs.md#thislb1) | [THISLB2](./sdr/runs.md#thislb2) | [THISLR1](./sdr/runs.md#thislr1) | [THISLR2](./sdr/runs.md#thislr2) | [THISLS1](./sdr/runs.md#thisls1) | [THISLS2](./sdr/runs.md#thisls2)

??? abstract "Abstract"
	
	The THISL spoken document retrieval system is based on the ABBOT Large Vocabulary Continuous Speech Recognition (LVCSR) system developed by Cambridge University, Sheffield University and SoftSound, and uses PRISE (NIST) for indexing and retrieval. We participated in full SDR mode. Our approach was to transcribe the spoken documents at the word level using ABBOT, indexing the resulting text transcriptions using PRISE. The LVCSR system uses a recurrent network-based acoustic model (with no adaptation to different conditions) trained on the 50 hour Broadcast News training set, a 65,000 word vocabulary and a trigram language model derived from Broadcast News text. Words in queries which were out-of-vocabulary (OOV) were word spotted at query time (utilizing the posterior phone probabilities output by the acoustic model), added to the transcriptions of the relevant documents and the collection was then re-indexed. We generated pronunciations at run-time for OOV words using the Festival TTS system (University of Edinburgh). Our key aims in this evaluation were to produce a complete system for the SDR task, to investigate the effect of a word error rate of 30-50% on retrieval performance and to investigate the integration of LVCSR and word spotting in a retrieval task. To achieve this we performed four basic experiments indexing on: transcribed text; IBM (baseline recognizer) SRT files; ABBOT SRT files; and ABBOT SRT files combined with word spotting of OOV words in the query. This evaluation provided a stress test for our LVCSR system. In particular we developed our decoding algorithm and software to operate in a more 'online mode'. The result of this was the ability to decode arbitrarily long passages without segmentation into 'utterances'. When indexing, acoustic model computation required around 3.5 x real time on a Sun Ultra 1/170, and lexical search required around 2.5 x real time. At query time the word spotting component ran in about 0.25 × real time per document per query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbberleyRCR97.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbberleyRCR97,
		author = {Dave Abberley and Steve Renals and Gary D. Cook and Anthony J. Robinson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {THISL} Spoken Document Retrieval System},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {747--752},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/sheffield.ps.gz},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbberleyRCR97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Very Large Corpus 

#### Overview of TREC-6 Very Large Collection Track

_David Hawking, Paul B. Thistlewaite_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/vlc_track.ps.gz](http://trec.nist.gov/pubs/trec6/papers/vlc_track.ps.gz)
??? abstract "Abstract"
	
	The emergence of real world applications for text collections orders of magnitude larger than the TREC collection has motivated the introduction of a Very Large Collection track within the TREC framework. The 20 gigabyte data set developed for the track is characterised, track objectives and guidelines are summarised and the measures employed are described. The contribution of the organizations which made data available is gratefully acknowledged and an overview is given of the track participants, the methods used and the results obtained. Alternative options for the future of the track are discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingT97.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingT97,
		author = {David Hawking and Paul B. Thistlewaite},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of {TREC-6} Very Large Collection Track},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {93--105},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/vlc\_track.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HawkingT97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AT&T at TREC-6

_Amit Singhal_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/att.ps.gz](http://trec.nist.gov/pubs/trec6/papers/att.ps.gz)

??? abstract "Abstract"
	
	TREC-6 is AT&T's first independent TREC participation. We are participating in the main tasks (adhoc, routing), the filtering track, the VLC track, and the SDR track This year, in the main tasks, we experimented with multi-pass query expansion using Rocchio's formulation. We concentrated a reasonable amount of our effort on our VLC track system, which is based on locally distributed, disjoint, and smaller sub-collections of the large collection. Our filtering track runs are based on our routing runs, followed by similarity thresholding to make a binary decision of the relevance prediction for a document.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Singhal97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Singhal97,
		author = {Amit Singhal},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {AT{\&}T at {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {215--225},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/att.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Singhal97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi at TREC-6 Automatic ad hoc, VLC, routing, filtering and QSDR

_Steve Walker, Stephen E. Robertson, Mohand Boughanem, Gareth J. F. Jones, Karen Sparck Jones_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz](http://trec.nist.gov/pubs/trec6/papers/city_proc_auto.ps.gz)

??? abstract "Abstract"
	
	We were interested to find out whether the Okapi BSS (Basic Search System) could handle more than 20 gigabytes of text and 8 million documents without major modification. There was no problem with data structures, but one or two system parameters had to be altered. In the interests of speed and because of limited disk space, indexes without full positional information were used. This meant that it was not possible to use passage-searching. Apart from this, the runs were done in the same way as the ad hoc, but with parameters intended to maximize precision at 20 documents. Several pairs of runs were done, but only one based on the full topic statements was submitted.
	

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

#### ANU/ACSys TREC-6 Experiments

_David Hawking, Paul B. Thistlewaite, Nick Craswell_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz](http://trec.nist.gov/pubs/trec6/papers/anu.ps.gz)

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

#### Passage-Based Refinement (MultiText Experiements for TREC-6)

_Gordon V. Cormack, Charles L. A. Clarke, Christopher R. Palmer, Samuel S. L. To_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz](http://trec.nist.gov/pubs/trec6/papers/waterloo.ps.gz)

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

#### The GURU System in TREC-6

_Eric W. Brown, Herb A. Chong_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ibm_brown.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ibm_brown.ps.gz)

??? abstract "Abstract"
	
	As the on-line world grows and increases its role in our daily lives, the problems of searching, categorizing, and understanding textual information become ever more important. While researchers and practitioners have made much progress in these areas over the last thirty years, anyone who has gone to the World Wide Web seeking information and returned with more frustration than answers can attest that much work remains. Today's important issues cover topics such as scalability, user interfaces, and techniques that exploit the unique hypermedia features of Web environments. To support our research in these areas, the Text Analysis and Advanced Search department at the IBM T. J. Watson Research Center has developed an experimental probabilistic text retrieval system called Guru[4]. Guru was originally built to explore new probabilistic ranking algorithms, and now serves as a test-bed for much of our text analysis, search, and categorization work. Guru may be run as a stand-alone system or in a client/server configuration. The Guru indexer performs minimal case and hyphen normalization, but otherwise indexes all words (including stop words) in their original form. The index includes document, paragraph, sentence, and word-in-sentence positional information for each word occurrence in the document collection. At search time, queries are input to Guru in a free-text format. Stop words are eliminated from the query and morphological variants for each query term are automatically generated and added as synonyms to the query term. Syntax is provided that allows the user to control morphological expansion and stop word elimination. Guru ranks documents using a probabilistic algorithm that considers the frequency statistics of the query terms in individual documents and the collection as a whole. Guru also considers lexical affinities (LAs), which are co-occurrences of two terms within a given distance. These automatically identified 'phrases' are ranked higher than instances of the component words occurring outside of the LA distance. Our purpose in participating in TREC-6 is four-fold. First, we continue to refine the base probabilistic ranking algorithm in Guru and wish to evaluate its performance on a large, standard test set. Second, we are developing a prototype user interface and seek initial feedback and guidance for further development. Third, we are interested in text search scalability as an issue orthogonal to the basic problems of search and categorization and seek feedback on initial attempts to address this issue. Fourth, hypermedia domains, such as the World Wide Web, are an increasingly important arena for application of text analysis and search technology. Such domains, however, pose a challenge for evaluation since both search and navigation must be considered by the evaluation metric. We hope that this issue will be addressed by the TREC community with the ultimate goal of defining appropriate evaluation metrics and building suitable test collections. Toward these ends, we are participating in the Ad-hoc Task, the Interactive Track, and the Very Large Corpus Track of TREC-6.
	

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

#### INQUERY Does Battle With TREC-6

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, Donald Byrd, Russell C. Swan, Jinxi Xu_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in eight of the ten tracks that were part of the TREC-6 workshop. We started with the two required tracks, ad-hoc and routing, but then included VLC, Filtering, Chinese, Cross-language, SDR, and Interactive. We omitted NLP and High Precision for want of time and energy. With so many tracks involved, it is nearly inevitable that something will go wrong. Despite our best efforts at verifying all aspects of each track-before, during, and after the experiments-we once again made mistakes that were minor in scope, but major in consequence. Those mistakes affected our results in Ad-hoc and Routing, as well as the dependent tracks of VLC and Filtering. The details of the mistakes are presented in each track's discussion, along with information comparing the submitted runs to the corrected runs. Unfortunately, those corrected runs are not included in TREC-6 summary information. This remainder of this report covers our approach to each of the tracks as well as some experimental results and analysis. We start with an overview of the major tools that were used across all tracks. The paper is divided into the following sections. The track descriptions are generally broken into approach, results, and analysis sections, though some tracks require a different description.
	

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

