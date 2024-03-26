# Proceedings 2006 

## Overview of the TREC 2006

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/OVERVIEW.pdf)
??? abstract "Abstract"
	
	The fifteenth Text REtrieval Conference, TREC 2006, was held at the National Institute of Standards and Technology (NIST) 14 to 17 November 2006. The conference was co-sponsored by NIST and the Disruptive Technology Office (DTO). TREC 2006 had 107 participating groups from 17 different countries. Table 2 at the end of the paper lists the participating groups. TREC 2006 is the latest in a series of workshops designed to foster research on technologies for information retrieval. The workshop series has four goals: to encourage retrieval research based on large test collections; to increase communication among industry, academia, and government by creating an open forum for the exchange of research ideas; to speed the transfer of technology from research labs into commercial products by demonstrating substantial improvements in retrieval methodologies on real-world problems; and to increase the availability of appropriate evaluation techniques for use by industry and academia, including development of new evaluation techniques more applicable to current systems. TREC 2006 contained seven areas of focus called “tracks”. Five of the tracks ran in previous TRECs and explored tasks in question answering, detecting spam in an email stream, enterprise search, search on (almost) terabyte-scale document sets, and information access within the genomics domain. The two new tracks explored blog search and providing support for legal discovery of electronic documents. There were two main themes in TREC 2006 that were supported by these different tracks. The first theme was exploring broader information contexts than in previous TRECs. This was accomplished by exploring both different document genres and different retrieval tasks. Traditional TREC document genres of newswire (in the QA track) and web pages (in the terabyte track) were still used, but these were joined by blogs (blog track), email (enterprise and spam tracks), corporate repositories (enterprise and legal tracks), and scientific documents (genomic and legal tracks). Retrieval tasks examined included ad hoc search (terabyte, enterprise-discussion, legal, genomics), known-item search (terabyte), classification (spam), specific response (QA, genomics, enterprise-expert), and opinion finding (blog). The second theme of the conference was a focus on creating new evaluation methodologies. These efforts included examining how to make fair comparisons when using massive data sets (terabyte and legal tracks), assessing the quality of a specific response (genomics, QA), balancing realism and privacy protection in experimental design (spam, enterprise), and constructing protocols for efficiency benchmarking in a distributed setting (terabyte). This paper serves as an introduction to the research described in detail in the remainder of the proceedings. The next section provides a summary of the retrieval background knowledge that is assumed in the other papers. Section 3 presents a short description of each track—a more complete description of a track can be found in that track's overview paper in the proceedings. The final section looks toward future TREC conferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees06.bib)"
	```
	@inproceedings{DBLP:conf/trec/Voorhees06,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Terabyte 

#### The TREC 2006 Terabyte Track

_Stefan Büttcher, Charles L. A. Clarke, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/TERA06.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/TERA06.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The primary goal of the Terabyte Track is to develop an evaluation methodology for terabyte-scale document collections. In addition, we are interested in efficiency and scalability issues, which can be studied more easily in the context of a larger collection. TREC 2006 is the third year for the track. The track was introduced as part of TREC 2004, with a single adhoc retrieval task. For TREC 2005, the track was expanded with two optional tasks: a named page finding task and an efficiency task. These three tasks were continued in 2006, with 20 groups submitting runs to the adhoc retrieval task, 11 groups submitting runs to the named page finding task, and 8 groups submitting runs to the efficiency task. This report provides an overview of each task, summarizes the results, and outlines directions for the future. Further background information on the development of the track can be found in the 2004 and 2005 track reports [4, 5]. For TREC 2006, we made the following major changes to the tasks: 1. We strongly encouraged the submission of adhoc manual runs, as well as runs using pseudo- relevance feedback and other query expansion techniques. Our goal was to increase the diversity of the judging pools in order to a create a more re-usable test collection. Special recognition (and a prize) was offered to the group submitting the run contributing the most unique relevant documents to the judging pool. 2. The named page finding topics were created by task participants, with each group asked to create at least 12 topics. 3. The experimental procedure for the efficiency track was re-defined to permit more realistic intra- and inter-system comparisons, and to generate separate measurements of latency and throughput. In order to compare systems across various hardware configurations, comparative runs using publicly available search engines were encouraged.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ButtcherCS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ButtcherCS06,
		author = {Stefan B{\"{u}}ttcher and Charles L. A. Clarke and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {TREC} 2006 Terabyte Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/TERA06.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ButtcherCS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melbourne University at the 2006 Terabyte Track

_Vo Ngoc Anh, William Webber, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [umelbourne.ngoc-anh](./terabyte/participants.md#umelbourne.ngoc-anh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umelbourne.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umelbourne.tera.final.pdf)
- :material-file-search: **Runs:** [MU06TBy1](./terabyte/runs.md#mu06tby1) | [MU06TBy2](./terabyte/runs.md#mu06tby2) | [MU06TBy5](./terabyte/runs.md#mu06tby5) | [MU06TBy6](./terabyte/runs.md#mu06tby6) | [MU06TBa2](./terabyte/runs.md#mu06tba2) | [MU06TBa5](./terabyte/runs.md#mu06tba5) | [MU06TBa1](./terabyte/runs.md#mu06tba1) | [MU06TBa6](./terabyte/runs.md#mu06tba6) | [MU06TBn2](./terabyte/runs.md#mu06tbn2) | [MU06TBn5](./terabyte/runs.md#mu06tbn5) | [MU06TBn6](./terabyte/runs.md#mu06tbn6) | [MU06TBn9](./terabyte/runs.md#mu06tbn9)

??? abstract "Abstract"
	
	This report describes the work done at The University of Melbourne for the TREC-2006 Terabyte Track. For this track, we participated in all three main tasks. We continued our work with impact-based ranking and sought to reduce indexing as well as query time. However, to support the named-page task, more conventional retrieval mechanisms were also employed. The results show that, in general, the efficiency performance is slightly better than the previous year. The effectiveness level remains the same.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnhWM06.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnhWM06,
		author = {Vo Ngoc Anh and William Webber and Alistair Moffat},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Melbourne University at the 2006 Terabyte Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umelbourne.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnhWM06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Hedge Algorithm for Metasearch at TREC 2006

_Javed A. Aslam, Virgiliu Pavlu, Carlos Rei_

- :fontawesome-solid-user-group: **Participant:** [northeasternu.aslam](./terabyte/participants.md#northeasternu.aslam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/northeasternu.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/northeasternu.tera.final.pdf)
- :material-file-search: **Runs:** [hedge0](./terabyte/runs.md#hedge0) | [hedge50](./terabyte/runs.md#hedge50) | [hedge5](./terabyte/runs.md#hedge5) | [hedge10](./terabyte/runs.md#hedge10) | [hedge30](./terabyte/runs.md#hedge30)

??? abstract "Abstract"
	
	Aslam, Pavlu, and Savell [3] introduced the Hedge algorithm for metasearch which effectively combines the ranked lists of documents returned by multiple retrieval systems in response to a given query and learns which documents are likely to be relevant from a sequence of on-line relevance judgments. It has been demonstrated that the Hedge algorithm is an effective technique for metasearch, often significantly exceeding the performance of standard metasearch and IR techniques over small TREC collections. In this work, we explore the effectiveness of Hedge over the much larger Terabyte 2006 collection
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AslamPR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/AslamPR06,
		author = {Javed A. Aslam and Virgiliu Pavlu and Carlos Rei},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Hedge Algorithm for Metasearch at {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/northeasternu.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AslamPR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IO-Top-k at TREC 2006: Terabyte Track

_Hannah Bast, Debapriyo Majumdar, Ralf Schenkel, Martin Theobald, Gerhard Weikum_

- :fontawesome-solid-user-group: **Participant:** [max-planck.theobald](./terabyte/participants.md#max-planck.theobald)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/max-planck-inst.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/max-planck-inst.tera.final.pdf)
- :material-file-search: **Runs:** [mpiiotopk](./terabyte/runs.md#mpiiotopk) | [mpiiotopkpar](./terabyte/runs.md#mpiiotopkpar) | [mpiiotopk2p](./terabyte/runs.md#mpiiotopk2p) | [mpiiotopk2](./terabyte/runs.md#mpiiotopk2) | [mpiirmanual](./terabyte/runs.md#mpiirmanual) | [mpiircomb](./terabyte/runs.md#mpiircomb) | [mpiirtitle](./terabyte/runs.md#mpiirtitle) | [mpiirdesc](./terabyte/runs.md#mpiirdesc) | [wumpus](./terabyte/runs.md#wumpus)

??? abstract "Abstract"
	
	This paper describes the setup and results of our contribution to the TREC 2006 Terabyte Track. Our implementation was based on the algorithms proposed in [1] “IO-Top-k: Index-Access Optimized Top-K Query Processing, VLDB'06”, with a main focus on the efficiency track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BastMSTW06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BastMSTW06,
		author = {Hannah Bast and Debapriyo Majumdar and Ralf Schenkel and Martin Theobald and Gerhard Weikum},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {IO-Top-k at {TREC} 2006: Terabyte Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/max-planck-inst.tera.final.pdf},
		timestamp = {Thu, 14 Oct 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BastMSTW06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MG4J at TREC 2006

_Paolo Boldi, Sebastiano Vigna_

- :fontawesome-solid-user-group: **Participant:** [umilano.vigna](./terabyte/participants.md#umilano.vigna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umilano.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umilano.tera.final.pdf)
- :material-file-search: **Runs:** [mg4jAdhocBV](./terabyte/runs.md#mg4jadhocbv) | [mg4jAdhocBBV](./terabyte/runs.md#mg4jadhocbbv) | [mg4jAdhocBVV](./terabyte/runs.md#mg4jadhocbvv) | [mg4jAdhocV](./terabyte/runs.md#mg4jadhocv) | [mg4jAutoV](./terabyte/runs.md#mg4jautov) | [mg4jAutoBV](./terabyte/runs.md#mg4jautobv) | [mg4jAutoBBV](./terabyte/runs.md#mg4jautobbv) | [mg4jAutoBVV](./terabyte/runs.md#mg4jautobvv)

??? abstract "Abstract"
	
	MG4J participated in the ad hoc task of the Terabyte Track (find all the relevant documents with high precision from 25.2 million pages from the .gov domain) at TREC 2006. It was the second time the MG4J group participated to TREC. For this year, we integrated standard techniques (such as stemming and BM25 scoring) into MG4J, and submitted also automatic runs based on trivial query expansion techniques.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoldiV06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoldiV06,
		author = {Paolo Boldi and Sebastiano Vigna},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{MG4J} at {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umilano.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoldiV06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Index Pruning and Result Reranking: Effects on Ad-Hoc Retrieval and  Named Page Finding

_Stefan Büttcher, Charles L. A. Clarke, Peter C. K. Yeung_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo-clarke](./terabyte/participants.md#uwaterloo-clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uwaterloo-clarke.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uwaterloo-clarke.tera.final.pdf)
- :material-file-search: **Runs:** [uwmtFdcp12](./terabyte/runs.md#uwmtfdcp12) | [uwmtFnoprune](./terabyte/runs.md#uwmtfnoprune) | [uwmtFdcp03](./terabyte/runs.md#uwmtfdcp03) | [uwmtFdcp06](./terabyte/runs.md#uwmtfdcp06) | [uwmtFadTPRR](./terabyte/runs.md#uwmtfadtprr) | [uwmtFadTPFB](./terabyte/runs.md#uwmtfadtpfb) | [uwmtFadDS](./terabyte/runs.md#uwmtfadds) | [uwmtFmanual](./terabyte/runs.md#uwmtfmanual) | [uwmtFcompW](./terabyte/runs.md#uwmtfcompw) | [uwmtFcompW1](./terabyte/runs.md#uwmtfcompw1) | [uwmtFcompW2](./terabyte/runs.md#uwmtfcompw2) | [uwmtFcompW3](./terabyte/runs.md#uwmtfcompw3) | [uwmtFcompI0](./terabyte/runs.md#uwmtfcompi0) | [uwmtFcompI1](./terabyte/runs.md#uwmtfcompi1) | [uwmtFcompI2](./terabyte/runs.md#uwmtfcompi2) | [uwmtFcompI3](./terabyte/runs.md#uwmtfcompi3) | [uwmtFnpstr1](./terabyte/runs.md#uwmtfnpstr1) | [uwmtFnpstr2](./terabyte/runs.md#uwmtfnpstr2) | [uwmtFnpsRR1](./terabyte/runs.md#uwmtfnpsrr1) | [uwmtFcompZ0](./terabyte/runs.md#uwmtfcompz0) | [uwmtFcompZ1](./terabyte/runs.md#uwmtfcompz1) | [uwmtFcompZ2](./terabyte/runs.md#uwmtfcompz2) | [uwmtFcompZ3](./terabyte/runs.md#uwmtfcompz3)

??? abstract "Abstract"
	
	We describe experiments conducted for the TREC 2006 Terabyte track. Our experiments are centered around two concepts: Static index pruning (for increased retrieval efficiency) and result reranking (for improved precision). We investigate their effect on retrieval efficiency and effectiveness, paying special attention to the difference between ad-hoc retrieval and named page finding. We show that index pruning and reranking based on relevance models can be beneficial in an ad-hoc retrieval setting, but have a disastrous repercussion on the effectiveness of named page finding. Result reranking based on anchor text, on the other hand, is very useful for named page finding, but should not be used for ad-hoc retrieval. This dichotomy poses a problem for search engines, as there is no easy way for a search engine to decide whether a given query represents an ad-hoc retrieval task, with the purpose to satisfy an abstract information need, or a named page finding task, targeting a specific document.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ButtcherCY06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ButtcherCY06,
		author = {Stefan B{\"{u}}ttcher and Charles L. A. Clarke and Peter C. K. Yeung},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Index Pruning and Result Reranking: Effects on Ad-Hoc Retrieval and Named Page Finding},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uwaterloo-clarke.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ButtcherCY06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Juru at TREC 2006: TAAT versus DAAT in the Terabyte Track

_David Carmel, Einat Amitay_

- :fontawesome-solid-user-group: **Participant:** [ibm.carmel](./terabyte/participants.md#ibm.carmel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ibm-haifa.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ibm-haifa.tera.final.pdf)
- :material-file-search: **Runs:** [JuruT](./terabyte/runs.md#jurut) | [JuruTD](./terabyte/runs.md#jurutd) | [JuruTWE](./terabyte/runs.md#jurutwe) | [JuruMan](./terabyte/runs.md#juruman)

??? abstract "Abstract"
	
	Our experiments focused this year on the ad-hock task of the Terabyte track. We experimented with WAND, a document-at-a-time evaluation algorithm we developed recently. Our results demonstrate the superiority of WAND over traditional term-a-time strategy while searching over a large collection such as gov2. We demonstrate how Web expansion can be successfully applied to significantly improve search results. In addition, we describe several schemes for creating manual queries, following this year's goal to enrich the pool of results by manual runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarmelA06.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarmelA06,
		author = {David Carmel and Einat Amitay},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Juru at {TREC} 2006: {TAAT} versus {DAAT} in the Terabyte Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ibm-haifa.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarmelA06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Partitioning the Gov2 Corpus by Internet Domain Name: A Result-set  Merging Experiment

_Christopher T. Fallen, Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [ualaska.fairbanks.newby](./terabyte/participants.md#ualaska.fairbanks.newby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ualaska.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ualaska.tera.final.pdf)
- :material-file-search: **Runs:** [arscDomAlog](./terabyte/runs.md#arscdomalog) | [arscDomAsrt](./terabyte/runs.md#arscdomasrt) | [arscDomManL](./terabyte/runs.md#arscdommanl) | [arscDomManS](./terabyte/runs.md#arscdommans)

??? abstract "Abstract"
	
	To study the MultiSearch problem and complete the Ad Hoc Task of the 2006 TREC Terabyte Track, the Gov2 collection was divided according to web domain and for each topic, the results from each domain were merged into single ranked list. The mean average precision scores of the results from two different merge algorithms applied to the domain-divided Gov2 collection and a randomized domain-divided collection are compared with a 2-way analysis of variance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FallenN06.bib) "
	```
	@inproceedings{DBLP:conf/trec/FallenN06,
		author = {Christopher T. Fallen and Gregory B. Newby},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Partitioning the Gov2 Corpus by Internet Domain Name: {A} Result-set Merging Experiment},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ualaska.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FallenN06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Dublin City University at the TREC 2006 Terabyte Track

_Paul Ferguson, Alan F. Smeaton, Peter Wilkins_

- :fontawesome-solid-user-group: **Participant:** [dublincityu.gurrin](./terabyte/participants.md#dublincityu.gurrin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/dublin-cityu.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/dublin-cityu.tera.final.pdf)
- :material-file-search: **Runs:** [DCU05BASE](./terabyte/runs.md#dcu05base)

??? abstract "Abstract"
	
	For the 2006 Terabyte track in TREC, Dublin City University's participation was focussed on the ad hoc search task. As per the pervious two years [7, 4], our experiments on the Terabyte track have concentrated on the evaluation of a sorted inverted index, the aim of which is to sort the postings within each posting list in such a way, that allows only a limited number of postings to be processed from each list, while at the same time minimising the loss of effectiveness in terms of query precision. This is done using the Fisreal search system, developed at Dublin City University [4, 8].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FergusonSW06.bib) "
	```
	@inproceedings{DBLP:conf/trec/FergusonSW06,
		author = {Paul Ferguson and Alan F. Smeaton and Peter Wilkins},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Dublin City University at the {TREC} 2006 Terabyte Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/dublin-cityu.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FergusonSW06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2006: Terabyte Track

_Steven Garcia, Nicholas Lester, Falk Scholer, Milad Shokouhi_

- :fontawesome-solid-user-group: **Participant:** [rmit.scholer](./terabyte/participants.md#rmit.scholer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/rmit.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/rmit.tera.final.pdf)
- :material-file-search: **Runs:** [rmit06effic](./terabyte/runs.md#rmit06effic) | [zetamerg](./terabyte/runs.md#zetamerg) | [zetabm](./terabyte/runs.md#zetabm) | [zetadir](./terabyte/runs.md#zetadir) | [zetamerg2](./terabyte/runs.md#zetamerg2) | [zetaman](./terabyte/runs.md#zetaman) | [zetnpbm](./terabyte/runs.md#zetnpbm) | [zetnpft](./terabyte/runs.md#zetnpft) | [zetnpfa](./terabyte/runs.md#zetnpfa) | [zetnpfta](./terabyte/runs.md#zetnpfta) | [rmit06cmpind](./terabyte/runs.md#rmit06cmpind) | [rmit06cmpwum](./terabyte/runs.md#rmit06cmpwum) | [rmit06cmpzet](./terabyte/runs.md#rmit06cmpzet)

??? abstract "Abstract"
	
	The TREC 2006 terabyte track consisted of three tasks: informational (or ad hoc) search, named page finding, and efficient retrieval. This paper outlines RMIT University's participation in these tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarciaLSS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarciaLSS06,
		author = {Steven Garcia and Nicholas Lester and Falk Scholer and Milad Shokouhi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2006: Terabyte Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/rmit.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GarciaLSS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PSM: A New Re-Ranking Algorithm for Named-Page

_Jiafeng Guo, Lin Ding, Gang Zhang, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas-ict.wang](./terabyte/participants.md#cas-ict.wang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cas-ict.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/cas-ict.tera.final.pdf)
- :material-file-search: **Runs:** [icttb0601](./terabyte/runs.md#icttb0601) | [icttb0604](./terabyte/runs.md#icttb0604) | [icttb0603](./terabyte/runs.md#icttb0603) | [icttb0600](./terabyte/runs.md#icttb0600) | [icttb0602](./terabyte/runs.md#icttb0602)

??? abstract "Abstract"
	
	This year, the IR group of ICT participated in the terabyte track named-page Finding subtask for the first time. Since the document collection is as large as about 426G, our most important goal is to find an efficient way to catch the target web page in such a huge size data set. Meanwhile we want to make the indexing and retrieval processing at a reasonable low cost, both on hardware and time-consuming. We used our “FirteX” engine for indexing and retrieval of this task. The indexing time is within 15 hours and the retrieval time is short enough(less than 2 seconds per query). The main contribution of our work is that we design a Pattern Similarity Matching(PSM) re-ranking algorithm to reorder the results and rank the target document as top 1 as possible. We were glad to see that we've got an exciting performance on the last year's (2005) topics during our experiment. The chief procedure of our work can be divided into three parts as below, which are data preprocess, indexing and retrieval, and re-ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GuoDZLC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/GuoDZLC06,
		author = {Jiafeng Guo and Lin Ding and Gang Zhang and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PSM:} {A} New Re-Ranking Algorithm for Named-Page},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cas-ict.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GuoDZLC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MonetDB/X100 at the 2006 TREC Terabyte Track

_Sándor Héman, Marcin Zukowski, Arjen P. de Vries, Peter A. Boncz_

- :fontawesome-solid-user-group: **Participant:** [lowlands-team.deVries](./terabyte/participants.md#lowlands-team.devries)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cwi-heman.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/cwi-heman.tera.final.pdf)
- :material-file-search: **Runs:** [CWI06DIST8](./terabyte/runs.md#cwi06dist8) | [CWI06MEM4](./terabyte/runs.md#cwi06mem4) | [CWI06DISK1](./terabyte/runs.md#cwi06disk1) | [CWI06MEM1](./terabyte/runs.md#cwi06mem1) | [CWI06DIST8ah](./terabyte/runs.md#cwi06dist8ah) | [CWI06DISK1ah](./terabyte/runs.md#cwi06disk1ah) | [CWI06COMP1](./terabyte/runs.md#cwi06comp1)

??? abstract "Abstract"
	
	Requirements of database management (DB) and information retrieval (IR) systems overlap more and more. Database systems are being applied to scenarios where features such as text search and similarity scoring on multiple attributes become crucial. Many information retrieval systems are being extended beyond plain text, to rank semi-structured documents marked up in XML, or maintain ontologies or thesauri. In both areas, these new features are usually implemented using specialized solutions limited in their features and performance. Full integration of DB and IR has been considered highly desirable, see e.g. [5, 1] for some recent advocates. Yet, none of the attempts into this direction has been very successful. The explanation can be sought in what has been termed the 'structure chasm' [8]: database research builds upon the idea that all data should satisfy a pre-defined schema, and the natural language text documents of concern to information retrieval do not match this database application scenario. Still, the structure chasm does not explain why IR systems do not use database technology to alleviate their data management tasks during index construction and document ranking. In practice however, custom-built information retrieval engines have always outperformed generic database technology, especially when also taking into account the trade-off between run-time performance and resources needed. To investigate the feasibility of running terabyte scale information retrieval tasks on top of a relational engine, our team from CWI participated in the 2006 TREC Terabyte Track, using its experimental MonetDB/X100 database system [3, 11]. This system, is designed for high performance on data-intensive workloads, whereof TREC-TB is an excellent example. Furthermore, we believe that standard relational algebra provides enough flexibility to express most IR retrieval models, and show that, by employing a hardware-conscious DBMS architecture, it is possible to achieve perormance, both in terms of efficiency and effectiveness, that is competitive with leading, customized IR systems. This notebook is organized as follows. Section 2 describes the distinguishing features of MonetDB/X100 that allow it to run large-scale data processing tasks efficiently. Section 3 then explains the process of indexing the TREC-TB collection, and the resulting relational schema. This is followed by a description of the TREC-TB runs we submitted, together with the hardware platforms used to run them. Effectiveness and efficiency results for these runs are then presented in Sections 6 and Section 7, respectively, before concluding in Section 8.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HemanZVB06.bib) "
	```
	@inproceedings{DBLP:conf/trec/HemanZVB06,
		author = {S{\'{a}}ndor H{\'{e}}man and Marcin Zukowski and Arjen P. de Vries and Peter A. Boncz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {MonetDB/X100 at the 2006 {TREC} Terabyte Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cwi-heman.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HemanZVB06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Peking University at the TREC 2006 Terabyte Track

_Li Jinging, Yan Hongfei_

- :fontawesome-solid-user-group: **Participant:** [pekingu.yan](./terabyte/participants.md#pekingu.yan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/pekingu.tera.pdf](http://trec.nist.gov/pubs/trec15/papers/pekingu.tera.pdf)
- :material-file-search: **Runs:** [TWTB06AD01](./terabyte/runs.md#twtb06ad01) | [TWTB06AD02](./terabyte/runs.md#twtb06ad02) | [TWTB06AD03](./terabyte/runs.md#twtb06ad03) | [TWTB06AD04](./terabyte/runs.md#twtb06ad04) | [TWTB06AD05](./terabyte/runs.md#twtb06ad05) | [TWTB06NP01](./terabyte/runs.md#twtb06np01) | [TWTB06NP02](./terabyte/runs.md#twtb06np02) | [TWTB06NP03](./terabyte/runs.md#twtb06np03)

??? abstract "Abstract"
	
	This paper details the experiments carried out at TREC 2006 Terabyte Track using Indri Search Engine. There were three tasks in the Terabyte track of TREC 2006, i.e. efficiency task, ad hoc task and named page finding task. We participated in two tasks, and submitted 5 runs for ad hoc task and 3 runs for named page task respectively. In ad hoc task, we looked at the importance of term proximity. In named page finding task, we cared more about the information of document structure and document prior.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JingingH06.bib) "
	```
	@inproceedings{DBLP:conf/trec/JingingH06,
		author = {Li Jinging and Yan Hongfei},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Peking University at the {TREC} 2006 Terabyte Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/pekingu.tera.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JingingH06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with Document and Query Representations for a Terabyte  of Text

_Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.ilps](./terabyte/participants.md#uamsterdam.ilps)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uamsterdam-kamps.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uamsterdam-kamps.tera.final.pdf)
- :material-file-search: **Runs:** [UAmsT06aTeLM](./terabyte/runs.md#uamst06atelm) | [UAmsT06aAnLM](./terabyte/runs.md#uamst06aanlm) | [UAmsT06aTDN](./terabyte/runs.md#uamst06atdn) | [UAmsT06aTTDN](./terabyte/runs.md#uamst06attdn) | [UAmsT06a3SUM](./terabyte/runs.md#uamst06a3sum) | [UAmsT06n3SUM](./terabyte/runs.md#uamst06n3sum) | [UAmsT06nTeLM](./terabyte/runs.md#uamst06ntelm) | [UAmsT06nTurl](./terabyte/runs.md#uamst06nturl) | [UAmsT06nAnLM](./terabyte/runs.md#uamst06nanlm)

??? abstract "Abstract"
	
	As part of the TREC 2006 Terabyte track, we conducted a range of experiments investigating the effects of larger test collections for both Adhoc and known-item topics. First, we looked at the amount of smoothing required for large-scale collections, and found that the large-scale collections require little smoothing. Second, we investigated the relative effectiveness of various web-centric document representations based on document-text, incoming anchor-texts, and page titles. We found that these are of little value for the Adhoc task, but can provide crucial additional retrieval cues for the Named page finding task. Third, we studied the relative effectiveness of various query representations, both short and verbose statements of the topic of request, plus an intermediate query based on the most characteristic terms in the whole topic statement. We we found that using a more verbose query leads to an improvement of retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Kamps06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Kamps06,
		author = {Jaap Kamps},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with Document and Query Representations for a Terabyte of Text},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uamsterdam-kamps.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Kamps06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2006: Experiments in Terabyte and  Enterprise Tracks with Terrier

_Christina Lioma, Craig Macdonald, Vassilis Plachouras, Jie Peng, Ben He, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uglasgow.ounis](./terabyte/participants.md#uglasgow.ounis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uglasgow.tera.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uglasgow.tera.ent.final.pdf)
- :material-file-search: **Runs:** [uogTB06QET1](./terabyte/runs.md#uogtb06qet1) | [uogTB06QET2](./terabyte/runs.md#uogtb06qet2) | [uogTB06S50L](./terabyte/runs.md#uogtb06s50l) | [uogTB06SS10L](./terabyte/runs.md#uogtb06ss10l) | [uogTB06SSQL](./terabyte/runs.md#uogtb06ssql) | [uogTB06M](./terabyte/runs.md#uogtb06m) | [uogTB06MP](./terabyte/runs.md#uogtb06mp) | [uogTB06MPIA](./terabyte/runs.md#uogtb06mpia)

??? abstract "Abstract"
	
	In TREC 2006, we participate in three tasks of the Terabyte and Enterprise tracks. We continue experiments using Terrier1, our modular and scalable Information Retrieval (IR) platform. Furthering our research into the Divergence From Randomness (DFR) framework of weighting models, we introduce two new effective and low-cost models, which combine evidence from document structure and capture term dependence and proximity, respectively. Additionally, in the Terabyte track, we improve on our query expansion mechanism on fields, presented in TREC 2005, with a new and more refined technique, which combines evidence in a linear, rather than uniform, way. We also introduce a novel, low-cost syntactically-based noise reduction technique, which we flexibly apply to both the queries and the index. Furthermore, in the Named Page Finding task, we present a new technique for combining query-independent evidence, in the form of prior probabilities. In the Enterprise track, we test our new voting model for expert search. Our experiments focus on the need for candidate length normalisation, and on how retrieval performance can be enhanced by applying retrieval techniques to the underlying ranking of documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiomaMPPHO06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiomaMPPHO06,
		author = {Christina Lioma and Craig Macdonald and Vassilis Plachouras and Jie Peng and Ben He and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2006: Experiments in Terabyte and Enterprise Tracks with Terrier},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uglasgow.tera.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiomaMPPHO06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fuzzy Term Proximity With Boolean Queries at 2006 TREC Terabyte  Task

_Annabelle Mercier, Michel Beigbeder_

- :fontawesome-solid-user-group: **Participant:** [ecole-des-mines.beigbeder](./terabyte/participants.md#ecole-des-mines.beigbeder)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ecole.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ecole.tera.final.pdf)
- :material-file-search: **Runs:** [AMRIMtp5006](./terabyte/runs.md#amrimtp5006) | [AMRIMtp20006](./terabyte/runs.md#amrimtp20006) | [AMRIMtpm5006](./terabyte/runs.md#amrimtpm5006)

??? abstract "Abstract"
	
	We report here the results of fuzzy term proximity method applied to Terabyte Task. Fuzzy proxmity main feature is based on the idea that the closer the query terms are in a document, the more relevant this document is. With this principle, we have a high precision method so we complete by these obtained with Zettair search engine default method (dirichlet). Our model is able to deal with Boolean queries, but contrary to the traditional extensions of the basic Boolean IR model, it does not explicitly use a proximity operator because it can not be generalized to nodes. The fuzzy term proximity is controlled with an influence function. Given a query term and a document, the influence function associates to each position in the text a value dependant of the distance of the nearest occurence of this query term. To model proximity, this function is decreasing with distance. Different forms of function can be used: triangular, gaussian etc. For practical reasons only functions with finite support were used. The support of the function is limited by a constant called k. The fuzzy term proximity functions are associated to every leaves of the query tree. Then fuzzy proximities are computed for every nodes with a post-order tree traversal. Given the fuzzy proximities of the sons of a node, its fuzzy proximity is computed, like in the fuzzy IR models, with a mimimum (resp. maximum) combination for conjunctives (resp. disjunctives) nodes. Finally, a fuzzy query proximity value is obtained for each position in this document at the root of the query tree. The score of this document is the integration of the function obtained at the tree root. For the experiments, we modify Lucy (version 0.5.2) to implement our matching function. Two query sets are used for our runs. One set is manually built with the title words (and sometimes some description words). Each of these words is OR'ed with its derivatives like plurals for instance. Then the OR nodes obtained are AND'ed at the tree root. An other automatic query sets is built with an AND of automatically extracted terms from the title field. These two query sets are submitted to our system with two values of k: 50 and 200. The two corresponding query sets with flat queries are also submitted to zettair search engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MercierB06.bib) "
	```
	@inproceedings{DBLP:conf/trec/MercierB06,
		author = {Annabelle Mercier and Michel Beigbeder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Fuzzy Term Proximity With Boolean Queries at 2006 {TREC} Terabyte Task},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ecole.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MercierB06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Indri TREC Notebook 2006: Lessons Learned From Three Terabyte Tracks

_Donald Metzler, Trevor Strohman, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./terabyte/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umass.tera.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umass.tera.final.pdf)
- :material-file-search: **Runs:** [indri06Aql](./terabyte/runs.md#indri06aql) | [indri06AdmD](./terabyte/runs.md#indri06admd) | [indri06AlceD](./terabyte/runs.md#indri06alced) | [indri06AlceB](./terabyte/runs.md#indri06alceb) | [indri06AtdnD](./terabyte/runs.md#indri06atdnd) | [indri06Nfi](./terabyte/runs.md#indri06nfi) | [indri06Nfip](./terabyte/runs.md#indri06nfip) | [indri06Nsd](./terabyte/runs.md#indri06nsd) | [indri06Nsdp](./terabyte/runs.md#indri06nsdp)

??? abstract "Abstract"
	
	This report describes the lessons learned using the Indri search system during the 2004-2006 TREC Terabyte Tracks. We provide an overview of Indri, and, for the ad hoc and named page finding tasks, discuss our general approach to the problem, what worked, what did not work, and what could possibly work in the future.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MetzlerSC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/MetzlerSC06,
		author = {Donald Metzler and Trevor Strohman and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Indri {TREC} Notebook 2006: Lessons Learned From Three Terabyte Tracks},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umass.tera.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MetzlerSC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Spam 

#### TREC 2006 Spam Track Overview

_Gordon V. Cormack_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/SPAM06.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/SPAM06.OVERVIEW.pdf)
??? abstract "Abstract"
	
	TREC's Spam Track uses a standard testing framework that presents a set of chronologically ordered email messages a spam filter for classification. In the filtering task, the messages are presented one at at time to the filter, which yields a binary judgement (spam or ham [i.e. non-spam]) which is compared to a human-adjudicated gold standard. The filter also yields a spamminess score, intended to reflect the likelihood that the classified message is spam, which is the subject of post-hoc ROC (Receiver Operating Characteristic) analysis. Two forms of user feedback are modeled: with immediate feedback the gold standard for each message is communicated to the filter immediately following classification; with delayed feedback the gold standard is communicated to the filter sometime later, so as to model a user reading email from time to time in batches. A new task - active learning - presents the filter with a large collection of unadjudicated messages, and has the filter request adjudication for a subset of them before classifying a set of future messages. Four test corpora - email messages plus gold standard judgements - were used to evaluate subject filters. Two of the corpora (the public corpora, one English and one Chinese) were distributed to participants, who ran their filters on the corpora using a track-supplied toolkit implementing the framework. Two of the corpora (the private corpora) were not distributed to participants; rather, participants submitted filter implementations that were run, using the toolkit, on the private data. Nine groups participated in the track, each submitting up to four filters for evaluation in each of the three tasks (filtering with immediate feedback; filtering with delayed feedback; active learning).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Cormack06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Cormack06,
		author = {Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 Spam Track Overview},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/SPAM06.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Cormack06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### OSBF-Lua - A Text Classification Module for Lua: The Importance  of the Training Method

_Fidelis Assis_

- :fontawesome-solid-user-group: **Participant:** [fidelis.assis](./spam/participants.md#fidelis.assis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/fidelis-assis.spam.final.pdf](http://trec.nist.gov/pubs/trec15/papers/fidelis-assis.spam.final.pdf)
- :material-file-search: **Runs:** [oflS1F](./spam/runs.md#ofls1f) | [oflS2F](./spam/runs.md#ofls2f) | [oflS3F](./spam/runs.md#ofls3f) | [oflS4F](./spam/runs.md#ofls4f) | [oflA1F](./spam/runs.md#ofla1f) | [oflS1pei](./spam/runs.md#ofls1pei) | [oflS1pci](./spam/runs.md#ofls1pci) | [oflS1ped](./spam/runs.md#ofls1ped) | [oflS1pcd](./spam/runs.md#ofls1pcd) | [oflS2pei](./spam/runs.md#ofls2pei) | [oflS2pci](./spam/runs.md#ofls2pci) | [oflS2ped](./spam/runs.md#ofls2ped) | [oflS2pcd](./spam/runs.md#ofls2pcd) | [oflS3pei](./spam/runs.md#ofls3pei) | [oflS3pci](./spam/runs.md#ofls3pci) | [oflS3ped](./spam/runs.md#ofls3ped) | [oflS3pcd](./spam/runs.md#ofls3pcd) | [oflS4pei](./spam/runs.md#ofls4pei) | [oflS4pci](./spam/runs.md#ofls4pci) | [oflS4ped](./spam/runs.md#ofls4ped) | [oflS4pcd](./spam/runs.md#ofls4pcd) | [oflA1pei](./spam/runs.md#ofla1pei) | [oflA1pci](./spam/runs.md#ofla1pci) | [oflA2pei](./spam/runs.md#ofla2pei) | [oflA2pci](./spam/runs.md#ofla2pci) | [oflA3pei](./spam/runs.md#ofla3pei) | [oflA3pci](./spam/runs.md#ofla3pci) | [oflA4pei](./spam/runs.md#ofla4pei) | [oflA4pci](./spam/runs.md#ofla4pci)

??? abstract "Abstract"
	
	OSBFL ua is a C module for the Lua language which implements a Bayesian classifier enhanced with Orthogonal Sparse Bigrams OSB for feature extraction and Exponential Differential Document Count EDDC - for feature selection. These two techniques, combined with the new training method introduced for TREC 2006 produce a highly accurate filter, yet very fast and economic in resources. OSBFL ua is an Open Source Software available from http://osbf-lua.luaforge.net/. spamfilter.lua is a productionc lass antis pam filter available in the same package.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Assis06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Assis06,
		author = {Fidelis Assis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {OSBF-Lua - {A} Text Classification Module for Lua: The Importance of the Training Method},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/fidelis-assis.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Assis06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Towards Practical PPM Spam Filtering: Experiments for the TREC  2006 Spam Track

_Andrej Bratko, Bogdan Filipic, Blaz Zupan_

- :fontawesome-solid-user-group: **Participant:** [jozef-stefan-inst.bratko](./spam/participants.md#jozef-stefan-inst.bratko)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/jozef-stefan.spam.final.pdf](http://trec.nist.gov/pubs/trec15/papers/jozef-stefan.spam.final.pdf)
- :material-file-search: **Runs:** [ijsS1F](./spam/runs.md#ijss1f) | [ijsA1F](./spam/runs.md#ijsa1f) | [ijsS1pei](./spam/runs.md#ijss1pei) | [ijsS1ped](./spam/runs.md#ijss1ped) | [ijsS1pci](./spam/runs.md#ijss1pci) | [ijsS1pcd](./spam/runs.md#ijss1pcd) | [ijsA1pei](./spam/runs.md#ijsa1pei) | [ijsA1pci](./spam/runs.md#ijsa1pci) | [ijsA2pei](./spam/runs.md#ijsa2pei) | [ijsA2pci](./spam/runs.md#ijsa2pci)

??? abstract "Abstract"
	
	This paper summarizes our participation in the TREC 2006 spam track. We submitted a single filter for the evaluation, based on the Prediction by Partial Matching compression scheme, a method that performed well in the previous TREC evaluation. A major focus of our effort was to improve efficiency of the method, particularly in terms of memory consumption, in order to establish whether compression-based filters are in fact a viable solution for practical applications. Our system exhibited fair performance, despite the fact that the filtering techniques remained virtually unchanged from the previous evaluation. We did not investigate methods for tackling delayed user feedback. A very simple strategy of training on most recent examples was used for the active learning task, and found to work surprisingly well given its simplicity.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BratkoFZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BratkoFZ06,
		author = {Andrej Bratko and Bogdan Filipic and Blaz Zupan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Towards Practical {PPM} Spam Filtering: Experiments for the {TREC} 2006 Spam Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/jozef-stefan.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BratkoFZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Highly Scalable Discriminative Spam Filtering

_Michael Brückner, Peter Haider, Tobias Scheffer_

- :fontawesome-solid-user-group: **Participant:** [humboldtu.haider](./spam/participants.md#humboldtu.haider)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/humboldtu.spam.final.pdf](http://trec.nist.gov/pubs/trec15/papers/humboldtu.spam.final.pdf)
- :material-file-search: **Runs:** [hubA2F](./spam/runs.md#huba2f) | [hubA1F](./spam/runs.md#huba1f) | [hubA3F](./spam/runs.md#huba3f) | [hubA4F](./spam/runs.md#huba4f) | [hubS1F](./spam/runs.md#hubs1f) | [hubS2F](./spam/runs.md#hubs2f) | [hubS3F](./spam/runs.md#hubs3f) | [hubS4F](./spam/runs.md#hubs4f) | [hubS1pcd](./spam/runs.md#hubs1pcd) | [hubS1pci](./spam/runs.md#hubs1pci) | [hubS1ped](./spam/runs.md#hubs1ped) | [hubS1pei](./spam/runs.md#hubs1pei) | [hubS2pcd](./spam/runs.md#hubs2pcd) | [hubS2pci](./spam/runs.md#hubs2pci) | [hubS2ped](./spam/runs.md#hubs2ped) | [hubS2pei](./spam/runs.md#hubs2pei) | [hubS3pcd](./spam/runs.md#hubs3pcd) | [hubS3pci](./spam/runs.md#hubs3pci) | [hubS3ped](./spam/runs.md#hubs3ped) | [hubS3pei](./spam/runs.md#hubs3pei) | [hubS4pcd](./spam/runs.md#hubs4pcd) | [hubS4pci](./spam/runs.md#hubs4pci) | [hubS4ped](./spam/runs.md#hubs4ped) | [hubS4pei](./spam/runs.md#hubs4pei) | [hubA1pci](./spam/runs.md#huba1pci) | [hubA1pei](./spam/runs.md#huba1pei) | [hubA2pci](./spam/runs.md#huba2pci) | [hubA2pei](./spam/runs.md#huba2pei) | [hubA3pci](./spam/runs.md#huba3pci) | [hubA3pei](./spam/runs.md#huba3pei) | [hubA4pci](./spam/runs.md#huba4pci) | [hubA4pei](./spam/runs.md#huba4pei)

??? abstract "Abstract"
	
	This paper discusses several lessons learned from the SpamTREC 2006 challenge. We discuss issues related to decoding, preprocessing, and tokenization of email messages. Using the Winnow algorithm with orthogonal sparse bigram features, we construct an efficient, highly scalable incremental classifier, trained to maximize a discriminative optimization criterion. The algorithm easily scales to millions of training messages and millions of features. We address the composition of training corpora and discuss experiments that guide the construction of our SpamTREC entry. We describe our submission for the filtering tasks with periodical re-training and active learning strategies, and report on the evaluation on the publicly available corpora.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrucknerHS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrucknerHS06,
		author = {Michael Br{\"{u}}ckner and Peter Haider and Tobias Scheffer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Highly Scalable Discriminative Spam Filtering},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/humboldtu.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BrucknerHS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Spam Filtering Using Inexact String Matching in Explicit Feature Space  with On-Line Linear Classifiers

_David Sculley, Gabriel Wachman, Carla E. Brodley_

- :fontawesome-solid-user-group: **Participant:** [tufts.sculley](./spam/participants.md#tufts.sculley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/tuftsu.spam.final.pdf](http://trec.nist.gov/pubs/trec15/papers/tuftsu.spam.final.pdf)
- :material-file-search: **Runs:** [tufS1F](./spam/runs.md#tufs1f) | [tufS2F](./spam/runs.md#tufs2f) | [tufS3F](./spam/runs.md#tufs3f) | [tufS4F](./spam/runs.md#tufs4f) | [tufS1pcd](./spam/runs.md#tufs1pcd) | [tufS1pci](./spam/runs.md#tufs1pci) | [tufS1ped](./spam/runs.md#tufs1ped) | [tufS1pei](./spam/runs.md#tufs1pei) | [tufS2pcd](./spam/runs.md#tufs2pcd) | [tufS2pci](./spam/runs.md#tufs2pci) | [tufS2ped](./spam/runs.md#tufs2ped) | [tufS2pei](./spam/runs.md#tufs2pei)

??? abstract "Abstract"
	
	Contemporary spammers commonly seek to defeat statistical spam filters through the use of word obfuscation. Such methods include character level substitutions, repetitions, and insertions to reduce the effectiveness of word-based features. We present an efficient method for combating obfuscation through the use of inexact string matching kernels, which were first developed to measure similarity among mutating genes in computational biology. Our system avoids the high classification costs associated with these kernel methods by working in an explicit feature space, and employs the Perceptron Algorithm using Margins for fast on-line training. No prior domain knowledge was incorporated into this system. We report strong experimental results on the TREC 2006 spam data sets and on other publicly available spam data, including near-perfect performance on the TREC 2006 Chinese spam data set. These results invite further exploration of the use of inexact string matching for spam filtering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SculleyWB06.bib) "
	```
	@inproceedings{DBLP:conf/trec/SculleyWB06,
		author = {David Sculley and Gabriel Wachman and Carla E. Brodley},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Spam Filtering Using Inexact String Matching in Explicit Feature Space with On-Line Linear Classifiers},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/tuftsu.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SculleyWB06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SVM-Based Spam Filter with Active and Online Learning

_Qiang Wang, Yi Guan, Xiaolong Wang_

- :fontawesome-solid-user-group: **Participant:** [harbin.zhao](./spam/participants.md#harbin.zhao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/hit.spam.final.final.pdf](http://trec.nist.gov/pubs/trec15/papers/hit.spam.final.final.pdf)
- :material-file-search: **Runs:** [hitS1F](./spam/runs.md#hits1f) | [hitS2F](./spam/runs.md#hits2f) | [hitS3F](./spam/runs.md#hits3f) | [hitA1F](./spam/runs.md#hita1f) | [hitA2F](./spam/runs.md#hita2f) | [hitA1pci](./spam/runs.md#hita1pci) | [hitA1pei](./spam/runs.md#hita1pei) | [hitA2pci](./spam/runs.md#hita2pci) | [hitA2pei](./spam/runs.md#hita2pei) | [hitS1pcd](./spam/runs.md#hits1pcd) | [hitS1pci](./spam/runs.md#hits1pci) | [hitS1ped](./spam/runs.md#hits1ped) | [hitS1pei](./spam/runs.md#hits1pei) | [hitS2pcd](./spam/runs.md#hits2pcd) | [hitS2pci](./spam/runs.md#hits2pci) | [hitS2ped](./spam/runs.md#hits2ped) | [hitS2pei](./spam/runs.md#hits2pei) | [hitS3pcd](./spam/runs.md#hits3pcd) | [hitS3pci](./spam/runs.md#hits3pci) | [hitS3ped](./spam/runs.md#hits3ped) | [hitS3pei](./spam/runs.md#hits3pei)

??? abstract "Abstract"
	
	A realistic classification model for spam filtering should not only take account of the fact that spam evolves over time, but also that labeling a large number of examples for initial training can be expensive in terms of both time and money. This paper address the problem of separating legitimate emails from unsolicited ones with active and online learning algorithm, using a Support Vector Machines (SVM) as the base classifier. We evaluate its effectiveness using a set of goodness criteria on TREC2006 spam filtering benchmark datasets, and promising results are reported.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangGW06.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangGW06,
		author = {Qiang Wang and Yi Guan and Xiaolong Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {SVM-Based Spam Filter with Active and Online Learning},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/hit.spam.final.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangGW06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BUPT at TREC 2006: Spam Track

_Zhen Yang, Wei Xu, Bo Chen, Weiran Xu, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [beijingu-posts-tele.weiran](./spam/participants.md#beijingu-posts-tele.weiran)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/beijing-upt.spam.final.pdf](http://trec.nist.gov/pubs/trec15/papers/beijing-upt.spam.final.pdf)
- :material-file-search: **Runs:** [BASA2F](./spam/runs.md#basa2f) | [BASS2F](./spam/runs.md#bass2f) | [KB9A3F](./spam/runs.md#kb9a3f) | [B53S3F](./spam/runs.md#b53s3f) | [WEIA4F](./spam/runs.md#weia4f) | [KB9S4F](./spam/runs.md#kb9s4f) | [KB3S1F](./spam/runs.md#kb3s1f) | [KB3A1F](./spam/runs.md#kb3a1f) | [KB9S4pei](./spam/runs.md#kb9s4pei) | [KB9S4ped](./spam/runs.md#kb9s4ped) | [KB9S4pci](./spam/runs.md#kb9s4pci) | [KB9S4pcd](./spam/runs.md#kb9s4pcd) | [B53S3pei](./spam/runs.md#b53s3pei) | [B53S3ped](./spam/runs.md#b53s3ped) | [B53S3pci](./spam/runs.md#b53s3pci) | [B53S3pcd](./spam/runs.md#b53s3pcd) | [KB3S1pei](./spam/runs.md#kb3s1pei) | [KB3S1ped](./spam/runs.md#kb3s1ped) | [KB3S1pci](./spam/runs.md#kb3s1pci) | [KB3S1pcd](./spam/runs.md#kb3s1pcd) | [BASS2pcd](./spam/runs.md#bass2pcd) | [BASS2pci](./spam/runs.md#bass2pci) | [BASS2ped](./spam/runs.md#bass2ped) | [BASS2pei](./spam/runs.md#bass2pei) | [BASA2pci](./spam/runs.md#basa2pci) | [BASA2pei](./spam/runs.md#basa2pei) | [KB3A1pci](./spam/runs.md#kb3a1pci) | [KB3A1pei](./spam/runs.md#kb3a1pei) | [KB9A3pci](./spam/runs.md#kb9a3pci) | [KB9A3pei](./spam/runs.md#kb9a3pei) | [WEIA4pci](./spam/runs.md#weia4pci) | [WEIA4pei](./spam/runs.md#weia4pei)

??? abstract "Abstract"
	
	This report summarizes our participation in the TREC 2006 spam track, in which we consider the use of Bayesian models for the spam filtering task. Firstly, our anti-spam filter, Kidult, is briefly introduced. And then we try to use weighted adjustment of separating hyperplane and selective classifiers ensemble to improve the filtering performance. Finally, we summarize the relevant results from the official evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangXCXG06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangXCXG06,
		author = {Zhen Yang and Wei Xu and Bo Chen and Weiran Xu and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BUPT} at {TREC} 2006: Spam Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/beijing-upt.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangXCXG06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Seven Hypothesis about Spam Filtering

_William S. Yerazunis_

- :fontawesome-solid-user-group: **Participant:** [mitsubhishi.yerazunis](./spam/participants.md#mitsubhishi.yerazunis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/crm.spam.final.pdf](http://trec.nist.gov/pubs/trec15/papers/crm.spam.final.pdf)
- :material-file-search: **Runs:** [CRMS1F](./spam/runs.md#crms1f) | [CRMS2F](./spam/runs.md#crms2f) | [CRMS3F](./spam/runs.md#crms3f) | [CRMS4F](./spam/runs.md#crms4f) | [CRMS1Ffull](./spam/runs.md#crms1ffull) | [CRMS2Ffull](./spam/runs.md#crms2ffull) | [CRMS3Ffull](./spam/runs.md#crms3ffull) | [CRMS4Ffull](./spam/runs.md#crms4ffull) | [CRMS4Fdelay](./spam/runs.md#crms4fdelay) | [CRMS3Fdelay](./spam/runs.md#crms3fdelay) | [CRMS2Fdelay](./spam/runs.md#crms2fdelay) | [CRMS1Fdelay](./spam/runs.md#crms1fdelay) | [CRMS1Fchi](./spam/runs.md#crms1fchi) | [CRMS2Fchi](./spam/runs.md#crms2fchi) | [CRMS3Fchi](./spam/runs.md#crms3fchi) | [CRMS4Fchi](./spam/runs.md#crms4fchi) | [CRMS4Fchidly](./spam/runs.md#crms4fchidly) | [CRMS3Fchidly](./spam/runs.md#crms3fchidly) | [CRMS2Fchidly](./spam/runs.md#crms2fchidly) | [CRMS1Fchidly](./spam/runs.md#crms1fchidly)

??? abstract "Abstract"
	
	For TREC 2006, the CRM114 team considered several different hypothesis on the topic of spam filtering. The hypothesis were that: 1 Spammers were changing tactics to successfully evade contentba sed spam filters; 2 A pretrained database of known spam and nonspam improves overall accuracy; 3 Repeated training methods are more effective than singlepa ss Train Only Errors training 4 KNN/Hyperspace classifiers are more effective than classical Bayesian or Markovian classifiers 5 Delaying feedback learning results in degraded filter accuracy 6 Bite ntropy filters are as good or better than tokenizing filters and aftert hefa ct: 7 1R OCA% is the best figure of merit for spam filters Of these hypothesis, we found that spammers were not significantly able to evade content based spam filters, that pretraining is probably not helpful, that repeatedpa ss training is not significantly helpful, that KNNs are of roughly equal accuracy to computationally and storagee quivalent Markov classifiers, that delayed feedback is only marginal in impacting filter accuracy, and that despite their highly counterintuitive design, bite ntropic filters are capable of similar or better accuracy to tokenizing filters. We also found a fascinating counterc orrellation between 1R OCA% and the final accuracy of a filter (the accuracy of the filter for the final 10% of the corpus).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yerazunis06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yerazunis06,
		author = {William S. Yerazunis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Seven Hypothesis about Spam Filtering},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/crm.spam.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Yerazunis06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Genomics 

#### TREC 2006 Genomics Track Overview

_William R. Hersh, Aaron M. Cohen, Phoebe M. Roberts, Hari Krishna Rekapalli_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/GEO06.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/GEO06.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Genomics Track implemented a new task in 2006 that focused on passage retrieval for question answering using full-text documents from the biomedical literature. A test collection of 162,259 full-text documents and 28 topics expressed as questions was assembled. Systems were required to return passages that contained answers to the questions. Expert judges determined the relevance of passages and grouped them into aspects identified by one or more Medical Subject Headings (MeSH) terms. Document relevance was defined by the presence of one or more relevant aspects. The performance of submitted runs was scored using mean average precision (MAP) at the passage, aspect, and document level. In general, passage MAP was low, while aspect and document MAP were somewhat higher.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershCRR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershCRR06,
		author = {William R. Hersh and Aaron M. Cohen and Phoebe M. Roberts and Hari Krishna Rekapalli},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 Genomics Track Overview},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/GEO06.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershCRR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2006 Genomics Experiment

_Samir Abdou, Jacques Savoy_

- :fontawesome-solid-user-group: **Participant:** [uneuchatel.savoy](./genomics/participants.md#uneuchatel.savoy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uneuchatel.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uneuchatel.geo.final.pdf)
- :material-file-search: **Runs:** [UniNE1](./genomics/runs.md#unine1) | [UniNE2](./genomics/runs.md#unine2) | [UniNE3](./genomics/runs.md#unine3)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2006 Genomics evaluation campaign. In an effort to find text passages that will meet user requests, we propose and evaluate a new approach to the generation of orthographic variants of search terms (mainly genomic names in our case). We also evaluate the retrieval effectiveness of both the Okapi (BM25) model and the I(n)B2 probabilistic model derived from the Divergence from Randomness paradigm. In our experiments, we find that in terms of mean average precision the latter model performs clearly better than the Okapi model (with a relative difference of 50%). Moreover when comparing a 5-gram indexing approach to word-based indexing schemes, the mean average precision decreases by about 10% when using the n-gram indexing scheme. Additionally, including the article's title in all passages generated from a given article does not improve retrieval effectiveness. Finally, the generation of passages delimited by HTML tags was not a success. The performance achieved was in fact rather poor, suggesting that there were too many sentences within such text passages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbdouS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbdouS06,
		author = {Samir Abdou and Jacques Savoy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2006 Genomics Experiment},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uneuchatel.geo.final.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbdouS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BioKI, A General Literature Navigation System at TREC Genomics  2006

_Sabine Bergler, Jonathan Schuman, Julien Dubuc, Alexandr Lebedev_

- :fontawesome-solid-user-group: **Participant:** [concordiau.bergler](./genomics/participants.md#concordiau.bergler)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/concordiau.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/concordiau.geo.final.pdf)
- :material-file-search: **Runs:** [BioKI1](./genomics/runs.md#bioki1) | [BioKI2](./genomics/runs.md#bioki2) | [BioKI3](./genomics/runs.md#bioki3)

??? abstract "Abstract"
	
	We present the passage reranking component of a general literature navigation system. Based on weighted keyword scoring without automatic enhancements such as term expansion, the system performed slightly above average on all three tasks, with a strong performance on aspect retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BerglerSDL06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BerglerSDL06,
		author = {Sabine Bergler and Jonathan Schuman and Julien Dubuc and Alexandr Lebedev},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BioKI, {A} General Literature Navigation System at {TREC} Genomics 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/concordiau.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BerglerSDL06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept Recognition, Information Retrieval, and Machine Learning in  Genomics Question-Answering

_J. Gregory Caporaso, William A. Baumgartner Jr., Hyunmin Kim, Zhiyong Lu, Helen L. Johnson, Olga Medvedeva, Anna Lindemann, Lynne M. Fox, Elizabeth K. White, K. Bretonnel Cohen, Lawrence Hunter_

- :fontawesome-solid-user-group: **Participant:** [ucolorado.cohen](./genomics/participants.md#ucolorado.cohen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ucolorado.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ucolorado.geo.final.pdf)
- :material-file-search: **Runs:** [uchsc1](./genomics/runs.md#uchsc1) | [uchsc2](./genomics/runs.md#uchsc2) | [uchsc3](./genomics/runs.md#uchsc3)

??? abstract "Abstract"
	
	TREC Genomics 2006 presented a genomics question-answering challenge with questions on twenty-seven topics, and a corpus of 162,259 full-text biomedical journal articles from which to derive answers. Questions were formulated from actual information needs of biomedical researchers, and performance was based on human evaluation of the answers. The University of Colorado approach to this task involved three key components: semantic analysis, document zoning, and a promiscuous retrieval approach followed by pruning by classifiers trained to identify near-misses. We began by parsing the document HTML, splitting it into paragraph-length passages and classifying each passage with respect to a model of the sections (zones) of scientific publications. We filtered out certain sections, and built a search index for these passages using the Lemur system. Next, for each query, we semi-automatically created a set of expansions using ontological resources, including MeSH and the Gene Ontology. This expansion included not only synonyms, but terms related to concepts that were both more specific and (in some cases) more general than the query. We searched the passage collection for these expanded queries using the Indri search engine from the Lemur package, with pseudo-relevance feedback. We also tried expanding the retrieved passages by adding passages that had a small cosine distance to the initial retrievals in an LSA-defined vector space. Our final step was to filter this expanded retrieval set with document classifiers whose input features included word stems and recognized concepts. Three separate runs were constructed using varying components of the above set, allowing us to explore the utility of each. The system produced the best result for at least one query in each of the three evaluations (document, passage and aspect diversity).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaporasoBKLJMLFWCH06.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaporasoBKLJMLFWCH06,
		author = {J. Gregory Caporaso and William A. Baumgartner Jr. and Hyunmin Kim and Zhiyong Lu and Helen L. Johnson and Olga Medvedeva and Anna Lindemann and Lynne M. Fox and Elizabeth K. White and K. Bretonnel Cohen and Lawrence Hunter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concept Recognition, Information Retrieval, and Machine Learning in Genomics Question-Answering},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ucolorado.geo.final.pdf},
		timestamp = {Tue, 26 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CaporasoBKLJMLFWCH06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Lexicon Expansion, Information Retrieval, and Cluster-based  Ranking for Biomedical Question Answering

_Aaron M. Cohen, Jianji Yang, Seeger Fisher, Brian Roark, William R. Hersh_

- :fontawesome-solid-user-group: **Participant:** [ohsu.hersh](./genomics/participants.md#ohsu.hersh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ohsu.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ohsu.geo.final.pdf)
- :material-file-search: **Runs:** [OHSUNoclu](./genomics/runs.md#ohsunoclu) | [OHSUCluster](./genomics/runs.md#ohsucluster) | [OHSUBigclu](./genomics/runs.md#ohsubigclu)

??? abstract "Abstract"
	
	The Oregon Health & Science University submission to the TREC 2006 Genomics Track approached the question answer extraction task in three phases. In the first phase the biological questions were parsed into relevant entities and query expressions were generated. The second phase retrieved relevant passages from the corpus using Lucene as an information retrieval engine. The third phase performed ranking of the retrieved passages and generated the final submitted output. Through these experiments and comparison with the approaches of others we hope to learn the contribution and value of several techniques applicable to question answer extraction including: lexicon-based query term expansion, query back-off techniques for questions with few applicable passages, and passage clustering for identifying distinct aspects of question answers. Our experiments showed no improvement after cluster-based ranking. Maximal span based passage indexing proved to be too coarse, resulting in an overall average performing passage MAP of 4%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CohenYFRH06.bib) "
	```
	@inproceedings{DBLP:conf/trec/CohenYFRH06,
		author = {Aaron M. Cohen and Jianji Yang and Seeger Fisher and Brian Roark and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Lexicon Expansion, Information Retrieval, and Cluster-based Ranking for Biomedical Question Answering},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ohsu.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CohenYFRH06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding Relevant Passages in Scientific Articles: Fusion of Automatic  Approaches vs. an Interactive Team Effort

_Dina Demner-Fushman, Susanne M. Humphrey, Nicholas C. Ide, Russell F. Loane, Patrick Ruch, Miguel E. Ruiz, Lawrence H. Smith, Lorraine K. Tanabe, W. John Wilbur, Alan R. Aronson_

- :fontawesome-solid-user-group: **Participant:** [nlm.aronson](./genomics/participants.md#nlm.aronson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/nlm.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/nlm.geo.final.pdf)
- :material-file-search: **Runs:** [NLMinter](./genomics/runs.md#nlminter) | [NLMfusion](./genomics/runs.md#nlmfusion) | [NLMmanual](./genomics/runs.md#nlmmanual)

??? abstract "Abstract"
	
	This paper presents our approach to retargeting the information retrieval systems designed and/or optimized for retrieval of MEDLINE citations to the task of finding relevant passages in the text of scientific articles. To continue using our TREC 2005 fusion approach, we needed a common representation for the full text biomedical articles to be shared by the four base systems (Essie, SMART, EasyIR and Theme.) The base systems relied upon previously developed NLP, statistical and ML methods. The fusion of the automatic runs improved the results of three contributing base systems at 99.9% significance level on all metrics: document, passage, and aspect precision. The fusion run outperformed Essie, the best of the base systems, at 94% to 99% significance level, with the exception of passage precision. The novelty of the task and the lack of training data inspired our exploration of an interactive approach. The prohibitive cost (in time and domain expert effort) required for a truly interactive retrieval led to a team interaction with one of the base systems - Essie. The initial queries were developed by a computational biologist and a medical librarian. The librarian merged and then refined the queries upon inspecting the initial search results. The refined queries were submitted as a batch without further interaction with the system. The interactive results, the best we achieved, improved over the baseline automatic Essie run at the 91% significance level. The difference between the fusion and the interactive results is not statistically significant.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Demner-FushmanHILSTWADRR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Demner-FushmanHILSTWADRR06,
		author = {Dina Demner{-}Fushman and Susanne M. Humphrey and Nicholas C. Ide and Russell F. Loane and Patrick Ruch and Miguel E. Ruiz and Lawrence H. Smith and Lorraine K. Tanabe and W. John Wilbur and Alan R. Aronson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Finding Relevant Passages in Scientific Articles: Fusion of Automatic Approaches vs. an Interactive Team Effort},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/nlm.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Demner-FushmanHILSTWADRR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BioText Team Report for the TREC 2006 Genomics Track

_Anna Divoli, Marti A. Hearst, Preslav Nakov, Ariel S. Schwartz_

- :fontawesome-solid-user-group: **Participant:** [ucal-berkeley.larso](./genomics/participants.md#ucal-berkeley.larso)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ucalifornia-berkeley.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ucalifornia-berkeley.geo.final.pdf)
- :material-file-search: **Runs:** [biotext1](./genomics/runs.md#biotext1) | [biotextweb](./genomics/runs.md#biotextweb) | [biotext3](./genomics/runs.md#biotext3)

??? abstract "Abstract"
	
	The paper reports on the work conducted by the BioText team at UC Berkeley for the TREC 2006 Genomics track. Our approach had three main focal points: First, based on our successful results in the TREC 2003 Genomics track [1], we emphasized gene name recall. Second, given the structured nature of the Generic Topic Types (GTTs), we attempted to design queries that covered every part of the topics, including synonym expansion. Third, inspired by having access to the full text of documents, we experimented with identifying and weighting information depending on which section (Introduction, Results, etc.) it appeared in. Our emphasis on covering the different pieces of the query may have helped with the aspects ranking portion of the task, as we performed best on that evaluation measure. We submitted three runs: Biotext1, BiotextWeb, and Biotext3. All runs were fully automatic. The Biotext1 run performed best, achieving MAP scores of .24 on aspects, .35 on documents, and .035 on passages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DivoliHNS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/DivoliHNS06,
		author = {Anna Divoli and Marti A. Hearst and Preslav Nakov and Ariel S. Schwartz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BioText Team Report for the {TREC} 2006 Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ucalifornia-berkeley.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DivoliHNS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Twease at TREC 2006: Breaking and Fixing BM25 Scoring With Query  Expansion, A Biologically Inspired Double Mutant Recovery Experiment

_Kevin C. Dorff, Matthew J. Wood, Fabien Campagne_

- :fontawesome-solid-user-group: **Participant:** [weill-med-cornellu](./genomics/participants.md#weill-med-cornellu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/weill-cornell.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/weill-cornell.geo.final.pdf)
- :material-file-search: **Runs:** [icb1](./genomics/runs.md#icb1) | [icb2](./genomics/runs.md#icb2) | [icb3](./genomics/runs.md#icb3)

??? abstract "Abstract"
	
	This is the first year that our group has participated in the genomics track of TREC. We enter the evaluation with a new biomedical search engine, developed as an open-source project which relies heavily on MG4J, and is publicly available at http://www.twease.org. We designed our runs to test the features of Twease that most distinguish it from other biomedical search engines. Such features include: (1) a custom biomedical query expansion module (which draws on biomedical thesauri, but also includes a statistical model of morphological word variations observed in the biomedical domain); (2) the ability to search the index simultaneously at the whole document level, or at the sentence level. Our official runs evaluated the performance of minimal interval semantics when used with custom morphological word expansion on a biomedical corpus. Our best official run scored MAP=0.30 at the document level, slightly above the median of other submissions. Our non-official runs compared minimal interval semantics to BM25 on the same topics and corpus. We varied the level of query expansion for both methods, and demonstrated how easily BM25 breaks down as more related terms are added to a query, while minimal interval semantics is robust to such change. We investigated the origin of the issue with a biologically inspired experimental design (mutation recovery). Our results help understand why certain groups observe performance drops with thesaurus-based query expansion, while other groups report the opposite effect. The best of our non-official runs achieves a MAP document level of 0.32 when an intermediate level of query expansion is used. This manuscript also describes our first attempt at passage retrieval in full text articles (we achieved a MAP of 0.052, above the median of 0.028).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DorffWC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/DorffWC06,
		author = {Kevin C. Dorff and Matthew J. Wood and Fabien Campagne},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Twease at {TREC} 2006: Breaking and Fixing {BM25} Scoring With Query Expansion, {A} Biologically Inspired Double Mutant Recovery Experiment},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/weill-cornell.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DorffWC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Extraction of Document Structure for Genomics Documents

_David Eichmann_

- :fontawesome-solid-user-group: **Participant:** [uiowa.eichmann](./genomics/participants.md#uiowa.eichmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uiowa.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uiowa.geo.final.pdf)
- :material-file-search: **Runs:** [UIowa06Geno1](./genomics/runs.md#uiowa06geno1) | [UIowa06Geno2](./genomics/runs.md#uiowa06geno2) | [UIowa06Geno3](./genomics/runs.md#uiowa06geno3)

??? abstract "Abstract"
	
	The University of Iowa participated only in the genomics track in TREC-2006. Our work concentrated almost entirely on exploring how accurately we could regenerate the logical structure of each of the documents in the corpus from their HTML instantiations. This year's work is hence primarily infrastructure building, with little in the way of support for the track's specific tasks in place.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Eichmann06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Eichmann06,
		author = {David Eichmann},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Extraction of Document Structure for Genomics Documents},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uiowa.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Eichmann06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ranking Biomedical Passages for Relevance and Diversity: University  of Wisconsin, Madison at TREC Genomics 2006

_Andrew B. Goldberg, David Andrzejewski, Jurgen Van Gael, Burr Settles, Xiaojin Zhu, Mark Craven_

- :fontawesome-solid-user-group: **Participant:** [uwisconsin.craven](./genomics/participants.md#uwisconsin.craven)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uwisconsin.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uwisconsin.geo.final.pdf)
- :material-file-search: **Runs:** [WiscRun1](./genomics/runs.md#wiscrun1) | [WiscRun2](./genomics/runs.md#wiscrun2) | [WiscRun3](./genomics/runs.md#wiscrun3)

??? abstract "Abstract"
	
	We report on the University of Wisconsin, Madison's experience in the TREC Genomics 2006 track, which asks participants to retrieve passages from scientific articles that satisfy biologists' information needs. An emphasis is placed on returning relevant passages that discuss different aspects of the topic. Using an off-the-shelf information retrieval (IR) engine, we focused on query generation and reranking query results to encourage relevance and diversity. For query generation, we automatically identify noun phrases from the topic descriptions, and use online resources to gather synonyms as expansion terms. Our first submission uses the baseline IR engine results. We rerank the passages using a na¨ıve clustering-based approach in our second run, and we test GRASSHOPPER , a novel graph-theoretic algorithm based on absorbing random walks, in our third run. While our aspect-level results appear to compare favorably with other participants' on average, our query generation techniques failed to produce adequate query results for several topics, causing our passage and document-level evaluation scores to suffer. Furthermore, we surprisingly achieved higher aspect-level scores using the initial ranking than our methods aimed specifically at promoting diversity. While this sounds discouraging, we have several ideas as to why this happened and hope to produce new methods that correct these shortcomings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoldbergAGSZC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoldbergAGSZC06,
		author = {Andrew B. Goldberg and David Andrzejewski and Jurgen Van Gael and Burr Settles and Xiaojin Zhu and Mark Craven},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Ranking Biomedical Passages for Relevance and Diversity: University of Wisconsin, Madison at {TREC} Genomics 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uwisconsin.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GoldbergAGSZC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2006: Genomics Track

_Xiangji Huang, Bin Hu, Hashmat Rohian_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./genomics/participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/yorku.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/yorku.geo.final.pdf)
- :material-file-search: **Runs:** [york06ga1](./genomics/runs.md#york06ga1) | [york06ga3](./genomics/runs.md#york06ga3) | [york06ga4](./genomics/runs.md#york06ga4)

??? abstract "Abstract"
	
	Our Genomics experiments mainly focus on addressing four problems in biomedical information retrieval. The four problems are: (1) how to deal with synonyms? (2) how to deal with the frequent use of acronyms? (3) how to deal with homonyms? (4) how to deal with the document-level retrieval, passage-level retrieval and aspect-level retrieval? In particular, we use the automatic query expansion algorithm proposed at TREC 2005 to construct structured queries for document-level retrieval and we also apply several data mining techniques for passage-level retrieval and aspect-level retrieval. The mean average precisions (MAP) for our automatic run “york06ga1” are 0.3365 at the document-level retrieval, 0.0197 at the passage-level retrieval and 0.1084 at the aspect-level retrieval. The evaluation results show that the automatic query expansion algorithm is effective for improving document-level retrieval performance. However, our retrieval performance on passage-level and aspect-level is poor. One possible reason is that we did not follow the TREC 2006 Genomics track protocol regarding the calculation of passage measures correctly. Therefore, we built a completely wrong index for the passage-level retrieval. Since our aspect-level retrieval is based on the results obtained from our passage level retrieval, the results thus obtained are sub-optimal.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangHR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangHR06,
		author = {Xiangji Huang and Bin Hu and Hashmat Rohian},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2006: Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/yorku.geo.final.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangHR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Robust Pseudo Feedback Estimation and HMM Passage Extraction: UIUC  at TREC 2006 Genomics Track

_Jing Jiang, Xin He, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uillinois.chicago.zhou](./genomics/participants.md#uillinois.chicago.zhou)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uillinois-uc.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uillinois-uc.geo.final.pdf)
- :material-file-search: **Runs:** [UICGenRun1](./genomics/runs.md#uicgenrun1) | [UICGenRun2](./genomics/runs.md#uicgenrun2) | [UICGenRun3](./genomics/runs.md#uicgenrun3)

??? abstract "Abstract"
	
	The University of Illinois at Urbana-Champaign (UIUC) participated in TREC 2006 Genomics Track. Our focus this year was to apply two language modeling techniques for information retrieval that have been proposed recently by our group [4, 1]. These two techniques have been shown to be effective for general English text. It is not clear, though, how they perform on text in special domains such as the biomedical domain. We therefore tested their effectiveness for this year's genomics task. First, we tried to improve the pseudo relevance feedback mechanism in the retrieval model by applying a recently proposed regularized estimation method [4]. In the KL-divergence retrieval framework, pseudo relevance feedback documents can be used to better estimate the query model [5]. While in the original proposed method [5], this estimation involved two parameters that need to be empirically set, recent work showed that a more robust, regularized estimation method that involves less parameter tuning can be effective [4]. We therefore applied this estimation method to this year's genomics task to see whether it can improve the pseudo relevance feedback mechanism in biomedical information retrieval as well. Second, since this year's task is defined as passage retrieval rather than document retrieval, a challenge is how to extract coherent and relevant passages from whole documents. Previously, we proposed a hidden Markov model (HMM)-based passage extraction method that was shown to be effective in the general English domain [1]. We applied this method to this year's genomics task to see whether this method is also effective for biomedical text. Besides the two language modeling techniques, we also tested the use of user relevance feedback for retrieval, to see how much human interaction can help improve the performance. We obtained some manual judgments from two domain experts, and used them in the two interactive runs Our experiment results showed that the regularized estimation method for pseudo relevance feedback performed similarly to the original estimation method when both methods were under the optimal parameter setting, and outperformed the original estimation method when both methods were under the default parameter setting. Because in reality we do not know the optimal parameter setting, the regularized estimation method is thus more robust than the original estimation method. Our experiment results also showed that the HMM-based passage extraction method outperformed a baseline method that returns whole paragraphs as passages. However, our HMM-based passage extraction method tends to return relatively long and coherent passages, which may not be optimal for the genomics task this year, because in this task the information need is more specific. Finally, our experiment results showed that user relevance feedback was very effective, as we expected.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangHZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangHZ06,
		author = {Jing Jiang and Xin He and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Robust Pseudo Feedback Estimation and {HMM} Passage Extraction: {UIUC} at {TREC} 2006 Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uillinois-uc.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangHZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NTU at TREC 2006 Genomics Track

_Kevin Hsin-Yih Lin, Wen-Juan Hou, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./genomics/participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ntu.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ntu.geo.final.pdf)
- :material-file-search: **Runs:** [NTUadh1](./genomics/runs.md#ntuadh1) | [NTUadh2](./genomics/runs.md#ntuadh2) | [NTUadh3](./genomics/runs.md#ntuadh3)

??? abstract "Abstract"
	
	In this paper, we present a system for information retrieval of biomedical texts at passage level. Our system used KL-divergence as the underlying retrieval model. We further added query expansion and performed post-processing on the results. We were able to obtain a Document MAP of 0.3563, Passage MAP of 0.0464 and Aspect MAP of 0.2255 on one of the three runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinHC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinHC06,
		author = {Kevin Hsin{-}Yih Lin and Wen{-}Juan Hou and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NTU} at {TREC} 2006 Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ntu.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinHC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Expanding Queries Using Multiple Resources

_Edgar Meij, Maarten de Rijke, Machiel Jansen_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.meij](./genomics/participants.md#uamsterdam.meij)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uamsterdam-meij.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uamsterdam-meij.geo.final.pdf)
- :material-file-search: **Runs:** [UAmsBaseLine](./genomics/runs.md#uamsbaseline) | [UAmsExp](./genomics/runs.md#uamsexp) | [UAmsExpSel](./genomics/runs.md#uamsexpsel)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2006 Genomics track, in which our main focus was on query expansion. We hypothesized that applying query expansion techniques would help us both to identify and retrieve synonymous terms, and to cope with ambiguity. To this end, we developed several collection-specific as well as web-based strategies. We also performed post-submission experiments, in which we compare various retrieval engines, such as Lucene, Indri, and Lemur, using a simple baseline topic-set. When indexing entire paragraphs as pseudo-documents, we find that Lemur is able to achieve the highest document-, passage-, and aspect-level scores, using the KL-divergence method and its default settings. Additionally, we index the collection at a lower level of granularity, by creating pseudo-documents comprising of individual sentences. When we search these instead of paragraphs in Lucene, the passage-level scores improve considerably. Finally we note that stemming improves overall scores by at least 10%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeijRJ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeijRJ06,
		author = {Edgar Meij and Maarten de Rijke and Machiel Jansen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Expanding Queries Using Multiple Resources},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uamsterdam-meij.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MeijRJ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2006 Experiment: Genomics Track

_Patrick Ruch, Frédéric Ehrler, Julien Gobeill, Imad Tbahriti, Antonio Jimeno-Yepes_

- :fontawesome-solid-user-group: **Participant:** [uhosp-geneva.ruch](./genomics/participants.md#uhosp-geneva.ruch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uhosp-geneva.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uhosp-geneva.geo.final.pdf)
- :material-file-search: **Runs:** [UnigeGO](./genomics/runs.md#unigego) | [UnigeMesh](./genomics/runs.md#unigemesh) | [UniGe](./genomics/runs.md#unige)

??? abstract "Abstract"
	
	In previous TREC Genomics competition, ad hoc experiments were based on MEDLINE corpora (about 4.5 millions in 2005). This year, the collection has been replaced by a collection of about 160000 full-text articles. The proposed task is a passage retrieval task. Because document length in MEDLINE follow a binomial distribution (Figure 1), our previous investigations were focused on exploring the document length parameter, using a slightly modified pivoted normalization factor (Singhal 1999, Fujita 2004). This year, our efforts concentrated on combining knowledge-driven methods to a standard vector-space retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuchEGTY06.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuchEGTY06,
		author = {Patrick Ruch and Fr{\'{e}}d{\'{e}}ric Ehrler and Julien Gobeill and Imad Tbahriti and Antonio Jimeno{-}Yepes},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2006 Experiment: Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uhosp-geneva.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuchEGTY06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UB at TREC Genomics 2006: Using Passage Retrieval and Pre-Retrieval  Query Expansion for Genomics IR

_Miguel E. Ruiz_

- :fontawesome-solid-user-group: **Participant:** [suny-buffalo.ruiz](./genomics/participants.md#suny-buffalo.ruiz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/suny-buffalo.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/suny-buffalo.geo.final.pdf)
- :material-file-search: **Runs:** [UBexp1](./genomics/runs.md#ubexp1) | [UBexp2](./genomics/runs.md#ubexp2) | [UBexp1M](./genomics/runs.md#ubexp1m) | [UBexp2M](./genomics/runs.md#ubexp2m)

??? abstract "Abstract"
	
	This paper presents the results of the University at Buffalo (UB) in TREC genomics. For this task we used the SMART retrieval system and a pre retrieval expansion method that uses the ABGene and MetaMap tools. We tried two different weighting schemes one using pivoted length normalization (Lnu.ltu) and another using augmented tf-idf (atn.ann). The results show that performance of pivoted length normalization is very close to the median system that participated in the Genomics track. The augmented tf-idf performs significantly above the median system showing an improvement of 21%. This seems to indicate that a simpler weighting scheme could work better for retrieval of relevant passages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Ruiz06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Ruiz06,
		author = {Miguel E. Ruiz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UB} at {TREC} Genomics 2006: Using Passage Retrieval and Pre-Retrieval Query Expansion for Genomics {IR}},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/suny-buffalo.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Ruiz06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Multiple Resources, Evidences and Criteria for Genomic Information  Retrieval

_Luo Si, Jie Lu, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [purdueu.si](./genomics/participants.md#purdueu.si)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/purdue-cmu.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/purdue-cmu.geo.final.pdf)
- :material-file-search: **Runs:** [PCPsgRescore](./genomics/runs.md#pcpsgrescore) | [PCPsgClean](./genomics/runs.md#pcpsgclean) | [PCPsgAspect](./genomics/runs.md#pcpsgaspect)

??? abstract "Abstract"
	
	We participated in the passage retrieval and aspect retrieval subtasks of the TREC 2006 Genomics Track. This paper describes the methods developed for these two subtasks. For passage retrieval, our query expansion method utilizes multiple external biomedical resources to extract acronyms, aliases, and synonyms, and we propose a post-processing step which combines the evidence from multiple scoring methods to improve relevance-based passage rankings. For aspect retrieval, our method estimates the topical aspects of the retrieved passages and generates passage rankings by considering both topical relevance and topical novelty. Empirical results demonstrate the effectiveness of these methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SiLC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/SiLC06,
		author = {Luo Si and Jie Lu and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Multiple Resources, Evidences and Criteria for Genomic Information Retrieval},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/purdue-cmu.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SiLC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass Genomics 2006: Query-Biased Pseudo Relevance Feedback

_Mark D. Smucker_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./genomics/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umass.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umass.geo.final.pdf)
- :material-file-search: **Runs:** [UMassCIIR1](./genomics/runs.md#umassciir1) | [UMassCIIR2](./genomics/runs.md#umassciir2) | [UMassCIIR1L](./genomics/runs.md#umassciir1l)

??? abstract "Abstract"
	
	Query-biased pseudo relevance feedback creates document representations for document feedback that aim to be more relevant to the user than using the entire document. Our submitted runs using query-biased feedback degraded performance compared to not using feedback. The cause of this degradation was the use of too many documents for feedback. Preliminary document retrieval experiments using fewer feedback documents found that query-biasing produced gains in the geometric mean average precision that non-biased feedback did not produce.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Smucker06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Smucker06,
		author = {Mark D. Smucker},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass Genomics 2006: Query-Biased Pseudo Relevance Feedback},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umass.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Smucker06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Passage Retrieval by Shrinkage of Language Models

_Fei Song, Joe Vasak, Wei Wang_

- :fontawesome-solid-user-group: **Participant:** [uguelph.song](./genomics/participants.md#uguelph.song)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uguelph.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uguelph.geo.final.pdf)
- :material-file-search: **Runs:** [UofG2](./genomics/runs.md#uofg2) | [UofG1](./genomics/runs.md#uofg1) | [UofG0](./genomics/runs.md#uofg0)

??? abstract "Abstract"
	
	Information retrieval is the process of searching for relevant documents that satisfy a user's information need (usually in the form of queries). Some of its successful applications include library catalogue search, medical record retrieval, and Internet search engines (e.g., Google). As the exponential growth of web pages and online documents continues, there is an increasing need for retrieval systems that are capable of dealing with a large collection of documents and at the same time narrowing the scope of the search results (not only relevant documents but also relevant passages or even direct answers). A number of conceptual models have been proposed for information retrieval, including the Boolean model [Baeza-Yates and Ribeiro-Neto, 1999], the vector-space model [Salton, 1989], probabilistic models [Robertson and Sparck Jones, 1976], the inference network model [Croft and Turtle, 1992], and the language models [Ponte and Croft, 1998; Hiemstra, 1998; Miller et al., 1999]. Among these models, language models have recently received a lot of attention in the field of information retrieval, since they are based on the solid foundation of statistical natural language processing and are both intuitive and flexible for extensions with more features to handle the retrieval tasks. In language modeling, we view each document as a language sample and estimate the probabilities of producing individual terms in a document. A query is treated as a generation process. Given a sequence of terms in a query, we compute the probabilities of generating these terms according to each document model. The multiplication of these probabilities is then used to rank the retrieved documents: the higher the generation probabilities, the more relevant the corresponding documents to the given query. One big obstacle in applying language modeling to information retrieval is the sparse data problem. Unlike a collection of documents where we can control the number of documents in it, a document itself is often small in size and its content is always fixed. Even for a relatively long document, some of the words can still be rare or missing according to the Zipf's law of language usage [Manning and Schütze, 1999]. As a result, the combination of individual probabilities through multiplications will be meaningless if one of the probabilities is zero (for a missing term in a document). Thus, overcoming the sparse data problem is the key for the success of any language modeling system for information retrieval.  For TREC 2006 Genomics Track (see http://ir.ohsu.edu/genomics/ for more information), the data set presents several new challenges for language modeling in specific and information retrieval in general. First of all, the search is targeted to the relevant passages within documents (more or less corresponding to paragraphs), since users of the biomedical domain are likely interested in finding answers along with the context that provides supporting information and links to the original sources. Secondly, there is a need to balance the results across different documents and aspects. An aspect is defined as a group of passages of similar content, which will be judged by human evaluators and identified by a set of MeSH terms for the Genomics data set. By ensuring an adequate coverage of the results across documents and aspects, we can reduce the repeats (or duplicate passages) and maintain a reasonable number of novel/unique passages, which may be particularly useful for biomedical researchers. Finally, the retrieved passages may need to be trimmed further to highlight the answers, since passages are typically organized as paragraphs and may contain irrelevant wording before and after the relevant answers. In the rest of the working note, we describe our retrieval method based on the language models and their combinations in section 2. In section 3, we explain the enhancements for balancing the results for documents and aspects and narrowing the spans for the answers in the retrieved passages. In section 4, we discuss our experimental results on the Genomics data set. Finally, we conclude and point future directions of our work in section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SongVW06.bib) "
	```
	@inproceedings{DBLP:conf/trec/SongVW06,
		author = {Fei Song and Joe Vasak and Wei Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Passage Retrieval by Shrinkage of Language Models},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uguelph.geo.final.pdf},
		timestamp = {Wed, 12 Apr 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SongVW06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ASU at TREC 2006 Genomics Track

_Luis Tari, Graciela Gonzalez, Robert Leaman, Shawn Nikkila, Ryan Wendt, Chitta Baral_

- :fontawesome-solid-user-group: **Participant:** [arizona-stateu.gonzalez](./genomics/participants.md#arizona-stateu.gonzalez)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/arizona-su.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/arizona-su.geo.final.pdf)
- :material-file-search: **Runs:** [asubaral](./genomics/runs.md#asubaral) | [asubaral2](./genomics/runs.md#asubaral2) | [asubaral3](./genomics/runs.md#asubaral3)

??? abstract "Abstract"
	
	This paper describes our experiments in the TREC 2006 Genomics track submitted by the ASU BioAI group, as well as experiments based on the improvements made after our submission. Some of the major issues we tried to address in our experiments are how to (1) extract keywords from natural language questions in the biomedical domain and (2) determine the relevancy of passages
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TariGLNWB06.bib) "
	```
	@inproceedings{DBLP:conf/trec/TariGLNWB06,
		author = {Luis Tari and Graciela Gonzalez and Robert Leaman and Shawn Nikkila and Ryan Wendt and Chitta Baral},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ASU} at {TREC} 2006 Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/arizona-su.geo.final.pdf},
		timestamp = {Wed, 25 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TariGLNWB06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept Based Document Retrieval for Genomics Literature

_Dolf Trieschnigg, Wessel Kraaij, Martijn J. Schuemie_

- :fontawesome-solid-user-group: **Participant:** [erasmus.schuemie](./genomics/participants.md#erasmus.schuemie)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/erasmus-tno-utwente.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/erasmus-tno-utwente.geo.final.pdf)
- :material-file-search: **Runs:** [EMCUT1](./genomics/runs.md#emcut1) | [EMCUT2](./genomics/runs.md#emcut2)

??? abstract "Abstract"
	
	The 2006 TREC Genomics evaluation focuses on document, passage and aspect retrieval in the genomics domain. The Erasmus Medical Center, TNO and University of Twente collaborated on an approach combining concept tagging (named entity recognition) and information retrieval based on statistical language models. Experiments on the 2004 collection show that document retrieval based on concepts could not outperform the baseline based on words. However, experiments on the 2006 collection shows no significant difference between the two approaches. Further investigation has to show if and how these concept and word based language models can be effectively combined.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TrieschniggKS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/TrieschniggKS06,
		author = {Dolf Trieschnigg and Wessel Kraaij and Martijn J. Schuemie},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concept Based Document Retrieval for Genomics Literature},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/erasmus-tno-utwente.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TrieschniggKS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT TREC 2006: Genomics Track

_Jay Urbain, Nazli Goharian, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [iit.urbain](./genomics/participants.md#iit.urbain)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/iit.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/iit.geo.final.pdf)
- :material-file-search: **Runs:** [iitx1](./genomics/runs.md#iitx1) | [iitx2](./genomics/runs.md#iitx2) | [iitx3](./genomics/runs.md#iitx3)

??? abstract "Abstract"
	
	For the TREC-2006 Genomics Track, we report on the effectiveness of composite information retrieval functions based on a dimensional data model for improving document, passage, and aspect search precision of genomics literature. We designed an approach, and developed a corresponding search engine, based on a novel dimensional data model capable of document, paragraph, sentence, and passage level retrieval of genomics literature. By constructing a data warehouse style index with the flexibility of aggregating term statistics at multiple levels of document granularity, and incorporating key biological entities through shallow parsing of individual sentences, composite retrieval models combining multiple levels of contextual evidence can be efficiently developed to improve retrieval performance. The genomics track for 2006 measured document, passage, and aspect retrieval using 27 topics created by active biological researchers. Each topic fit within one of four question-oriented topic templates: the role of a gene in a disease, the effect of a gene on a biological process, how genes interact in organ function, and how mutations in genes influence biological processes. Documents for this task come from a corpus of 162,048 full-text biomedical articles. Each form of retrieval was measured with a variant of mean average precision (MAP). We submitted automatically generated results from three composite models to the TREC forum. All three models delivered results that significantly exceed the median results reported for the 2006 TREC Genomics track. The results of our best performing TREC model had MAP of 0.426 for document retrieval (53% above median), 0.055 for passage retrieval (129% above median), and 0.262 for aspect retrieval (125% above median).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UrbainGF06.bib) "
	```
	@inproceedings{DBLP:conf/trec/UrbainGF06,
		author = {Jay Urbain and Nazli Goharian and Ophir Frieder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIT} {TREC} 2006: Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/iit.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/UrbainGF06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Vector-Space and Word-Based Aspect Models for Passage Retrieval

_Raymond Wan, Ichigaku Takigawa, Hiroshi Mamitsuka, Vo Ngoc Anh_

- :fontawesome-solid-user-group: **Participant:** [kyotou.wan](./genomics/participants.md#kyotou.wan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/kyotou-umelbourne.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/kyotou-umelbourne.geo.final.pdf)
- :material-file-search: **Runs:** [kyoto2](./genomics/runs.md#kyoto2) | [kyoto20](./genomics/runs.md#kyoto20) | [kyoto1](./genomics/runs.md#kyoto1)

??? abstract "Abstract"
	
	This report summarizes the work done at Kyoto University and the University of Melbourne for the TREC 2006 Genomics Track. The single task for this year was to retrieve passages from a biomedical document collection. We devised a system made of two parts to deal with this problem. The first part was an existing IR system based on the vector-space model. The second part was a newly developed probabilistic word-based aspect model for identifying passages within relevant documents (or paragraphs).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WanTMA06.bib) "
	```
	@inproceedings{DBLP:conf/trec/WanTMA06,
		author = {Raymond Wan and Ichigaku Takigawa and Hiroshi Mamitsuka and Vo Ngoc Anh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Vector-Space and Word-Based Aspect Models for Passage Retrieval},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/kyotou-umelbourne.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WanTMA06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2006: Genomics and Enterprise Tracks

_Zhihao Yang, Hongfei Lin, Yanpeng Li, Linhong Xu, Yu Pan, Baoyan Liu_

- :fontawesome-solid-user-group: **Participant:** [dalianu.yang](./genomics/participants.md#dalianu.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/dalianu.geo.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/dalianu.geo.ent.final.pdf)
- :material-file-search: **Runs:** [DUTgen1](./genomics/runs.md#dutgen1) | [DUTgen2](./genomics/runs.md#dutgen2) | [DUTgen3](./genomics/runs.md#dutgen3)

??? abstract "Abstract"
	
	This paper describes the techniques we applied for the two TREC 2006 tracks, i.e., Genomics and Enterprise track. For the Genomics Track, we used a Rocchio relevance feedback method to expand the terms and then performed passage retrieval by building dual index and using half overlapped windows passages. Several approaches to merge the results and rerank the passages are presented. For the Enterprise track, we stripped the non-letter character from documents and query, built the index by indri or lemur and established expert document pools.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLLXPL06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangLLXPL06,
		author = {Zhihao Yang and Hongfei Lin and Yanpeng Li and Linhong Xu and Yu Pan and Baoyan Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2006: Genomics and Enterprise Tracks},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/dalianu.geo.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangLLXPL06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### I2R at TREC 2006 Genomics Track

_Nie Yu, Lingpeng Yang, Jie Zhang, Jian Su, Dong-Hong Ji_

- :fontawesome-solid-user-group: **Participant:** [inst-infocomm-res.yu](./genomics/participants.md#inst-infocomm-res.yu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/iir.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/iir.geo.final.pdf)
- :material-file-search: **Runs:** [i2rg063](./genomics/runs.md#i2rg063) | [i2rg061](./genomics/runs.md#i2rg061) | [i2rg062](./genomics/runs.md#i2rg062)

??? abstract "Abstract"
	
	This paper describes the method we used for the Genomics Track of TREC 2006. BM25 model is implemented to retrieve relevant documents. We also tried to re-ranking documents based on the initial retrieval before passage retrieval. Passages are retrieved based on the concepts defining in topics and concept coverage. Results of submitted runs are listed and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuYJSJ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuYJSJ06,
		author = {Nie Yu and Lingpeng Yang and Jie Zhang and Jian Su and Dong{-}Hong Ji},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{I2R} at {TREC} 2006 Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/iir.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuYJSJ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Profile Matching and Text Categorization for Answer Extraction  in TREC Genomics

_Haiqing Zheng, Chen Lin, Lishen Huang, Jun Xu, Jiaqian Zheng, Qi Sun, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [fudanu.niu](./genomics/participants.md#fudanu.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/fudan-zheng.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/fudan-zheng.geo.final.pdf)
- :material-file-search: **Runs:** [fdugen1](./genomics/runs.md#fdugen1) | [fdugen3](./genomics/runs.md#fdugen3) | [fdugen2](./genomics/runs.md#fdugen2)

??? abstract "Abstract"
	
	TREC'06 genomics track was focusing on text mining and passage retrieval. WIM lab participated in this year's TREC genomics track. Our system consists of five parts: preprocessing, sentence generation, document retrieval, answer extraction and answer fusion. And we developed two different method: a automated profile matching-based method and a text categorization-based method to do the text mining, we will compare the performances between those two methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengLHXZSN06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengLHXZSN06,
		author = {Haiqing Zheng and Chen Lin and Lishen Huang and Jun Xu and Jiaqian Zheng and Qi Sun and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Profile Matching and Text Categorization for Answer Extraction in {TREC} Genomics},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/fudan-zheng.geo.final.pdf},
		timestamp = {Tue, 20 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengLHXZSN06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Concept-Based Framework for Passage Retrieval at Genomics

_Wei Zhou, Clement T. Yu, Vetle I. Torvik, Neil R. Smalheiser_

- :fontawesome-solid-user-group: **Participant:** [uillinois.chicago.zhou](./genomics/participants.md#uillinois.chicago.zhou)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uillinois-chicago.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uillinois-chicago.geo.final.pdf)
- :material-file-search: **Runs:** [UICGenRun1](./genomics/runs.md#uicgenrun1) | [UICGenRun2](./genomics/runs.md#uicgenrun2) | [UICGenRun3](./genomics/runs.md#uicgenrun3)

??? abstract "Abstract"
	
	The task of TREC 2006 Genomics Track is to retrieve passages (from part to paragraph) from full-text HTML biomedical journal papers to answer the structured questions from real biologists. A system for such task needs to be able to parse the HTML free-texts (convert the HTML free-texts into plain texts) and pinpoint the most relevant passage(s) within documents for the specified question. This task is accomplished in three steps in our system. The first step is to parse the HTML articles and partition them into paragraphs. The second step is to retrieve the relevant paragraphs. The third step is to identify the most relevant passages within paragraphs and finally rank those passages. We are interested in 1. How does a concept-based IR model perform on structured queries comparing to Okapi? 2. Will the query expansion based on domain knowledge increase retrieval effectiveness? 3. Will our abbreviation database from MEDLINE help improve query expansion and will the abbreviation disambiguation help improve the ranking? The experiment results show that our concept-based IR model works better than the Okapi; query expansion based on domain knowledge is important, especially for those queries with very few relevant documents; an abbreviation database for query expansion and disambiguation is helpful for passage retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouYTS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouYTS06,
		author = {Wei Zhou and Clement T. Yu and Vetle I. Torvik and Neil R. Smalheiser},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Concept-Based Framework for Passage Retrieval at Genomics},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uillinois-chicago.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhouYTS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Enterprise 

#### Overview of the TREC 2006 Enterprise Track

_Ian Soboroff, Arjen P. de Vries, Nick Craswell_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ENT06.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/ENT06.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The goal of the enterprise track is to conduct experiments with enterprise data — intranet pages, email archives, document repositories — that reflect the experiences of users in real organizations, such that for example, an email ranking technique that is effective here would be a good choice for deployment in a real multi-user email search application. This involves both understanding user needs in enterprise search and development of appropriate IR techniques. The enterprise track began in TREC 2005 as the successor to the web track, and this is reflected in the tasks and measures. While the track takes much of its inspiration from the web track, the foci are on search at the enterprise scale, incorporating non-web data and discovering relationships between entities in the organization. As a result, we have created the first test collections for multi-user email search and expert finding. This year the track has continued using the W3C collection, a crawl of the publicly available web of the World Wide Web Consortium performed in June 2004. This collection contains not only web pages but numerous mailing lists, technical documents and other kinds of data that represent the day-to-day operation of the W3C. Details of the collection may be found in the 2005 track overview (Craswell et al., 2005). Additionally, this year we began creating a repository of information derived from the collection by participants. This data is hosted alongside the W3C collection at NIST. There were two tasks this year, email discussion search and expert search, and both represent refinements of the tasks initially done in 2005. NIST developed topics and relevance judgments for the email discussion search task this year. For expert search, rather than relying on found data as last year, the track participants created the topics and relevance judgments. Twenty-five groups took part across the two tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SoboroffVC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/SoboroffVC06,
		author = {Ian Soboroff and Arjen P. de Vries and Nick Craswell},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2006 Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ENT06.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SoboroffVC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Language Models for Enterprise Search: Query Expansion and Combination  of Evidence

_Krisztian Balog, Edgar Meij, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.ilps](./enterprise/participants.md#uamsterdam.ilps)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uamsterdam-derijke.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uamsterdam-derijke.ent.final.pdf)
- :material-file-search: **Runs:** [UvAbase](./enterprise/runs.md#uvabase) | [UAmsBase](./enterprise/runs.md#uamsbase) | [UvAprofiling](./enterprise/runs.md#uvaprofiling) | [UvAPOS](./enterprise/runs.md#uvapos) | [UvAprofPOS](./enterprise/runs.md#uvaprofpos) | [UAmsPOSBase](./enterprise/runs.md#uamsposbase) | [UAmsThreadQE](./enterprise/runs.md#uamsthreadqe) | [UAmsPOStQE](./enterprise/runs.md#uamspostqe)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2006 Enterprise track. We provide a detailed account of the ideas underlying our language modeling approaches to both the discussion search and expert search tasks. For discussion search, our focus was on query expansion techniques, using additional information from the topic statement and from message threads; while the former was generally helpful, the latter mostly hurt performance. In expert search our main experiments concerned query expansion as well as combinations of expert finding and expert profiling techniques.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalogMR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalogMR06,
		author = {Krisztian Balog and Edgar Meij and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Language Models for Enterprise Search: Query Expansion and Combination of Evidence},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uamsterdam-derijke.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalogMR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Research on Expert Search at Enterprise Track of TREC 2006

_Shenghua Bao, Huizhong Duan, Qi Zhou, Miao Xiong, Yong Yu, Yunbo Cao_

- :fontawesome-solid-user-group: **Participant:** [sjtu-apex-lab.bao](./enterprise/participants.md#sjtu-apex-lab.bao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/shanghai.final.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/shanghai.final.ent.final.pdf)
- :material-file-search: **Runs:** [SJTU01](./enterprise/runs.md#sjtu01) | [SJTU02](./enterprise/runs.md#sjtu02) | [SJTU03](./enterprise/runs.md#sjtu03) | [SJTU04](./enterprise/runs.md#sjtu04)

??? abstract "Abstract"
	
	This year, we (SJTU team) participated in the Expert Search task at the Enterprise Track. Last year, two of the members participated in the Expert Search task (MSRA team) [1]. This document reports our new experimental results on the expert search of TREC 2006. In this research, we propose a new evidence-oriented framework to expert search. Here, the evidence is defined as a quadruple, <Query, Expert, Relation, Document>. Each quadruple denotes that a 'Query' and an 'Expert', with a certain 'Relation' between them, are found in a specific 'Document'. In the proposed framework, the task of Expert Search can be accomplished in three steps, namely, 1) evidence extraction, 2) evidence quality evaluation, and 3) evidence merging. Thus, our experiments include the following items. We will explain them in detail later in the following sections. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BaoDZXYC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BaoDZXYC06,
		author = {Shenghua Bao and Huizhong Duan and Qi Zhou and Miao Xiong and Yong Yu and Yunbo Cao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Research on Expert Search at Enterprise Track of {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/shanghai.final.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BaoDZXYC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Social Network Structure Behind the Mailing Lists: ICT-IIIS at TREC  2006 Expert Finding Track

_Haiqiang Chen, Huawei Shen, Jin Xiong, Songbo Tan, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas-iiis.tan](./enterprise/participants.md#cas-iiis.tan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cas-ict.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/cas-ict.ent.final.pdf)
- :material-file-search: **Runs:** [IIISRUN](./enterprise/runs.md#iiisrun) | [ICTCSXRUN01](./enterprise/runs.md#ictcsxrun01) | [ICTCSXRUN02](./enterprise/runs.md#ictcsxrun02) | [ICTCSXRUN03](./enterprise/runs.md#ictcsxrun03) | [ICTCSXRUN04](./enterprise/runs.md#ictcsxrun04) | [ICTCSXRUN05](./enterprise/runs.md#ictcsxrun05)

??? abstract "Abstract"
	
	Expert finding system is a challenging problem in the enterprise environment. This paper introduce our research and experiments on TREC 2006's expert searching track. In our experiments, we find some interesting features of the community structures in the mailing list network. We also use some link analysis approaches to rank the candidates in the social networks. In our experiments, we choose the PageRank algorithm and a revised HITS algorithm as link analysis methods. These approaches give reasonable results in our experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenSXTC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenSXTC06,
		author = {Haiqiang Chen and Huawei Shen and Jin Xiong and Songbo Tan and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Social Network Structure Behind the Mailing Lists: {ICT-IIIS} at {TREC} 2006 Expert Finding Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cas-ict.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenSXTC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### L3S Research Center at TREC 2006 Enterprise Track

_Sergey Chernov, Gianluca Demartini, Julien Gaugaz_

- :fontawesome-solid-user-group: **Participant:** [uhannover.chernov](./enterprise/participants.md#uhannover.chernov)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/l3s.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/l3s.ent.final.pdf)
- :material-file-search: **Runs:** [l3s1](./enterprise/runs.md#l3s1) | [l3s2](./enterprise/runs.md#l3s2) | [l3s3](./enterprise/runs.md#l3s3) | [l3s4](./enterprise/runs.md#l3s4)

??? abstract "Abstract"
	
	The L3S Research Center submitted four runs at Enterprise Track for the first time in 2006, all of them are based solely on the W3C mailing lists. The first run serves as a fully automatically produced baseline. The second run uses a threshold on the document scores to limit the number of documents used for expert ranking. The third uses in addition a threshold on the experts scores in order to decide how many experts to retrieve. Our last run exploits the manually assigned topic specificity values, which predicts a number of relevant expert for each query. The results show that the simple threshold techniques outperform the baseline, while the current definition of query specificity does not improve the result quality.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChernovDG06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChernovDG06,
		author = {Sergey Chernov and Gianluca Demartini and Julien Gaugaz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{L3S} Research Center at {TREC} 2006 Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/l3s.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChernovDG06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM in TREC 2006 Enterprise Track

_Jennifer Chu-Carroll, Guillermo A. Averboch, Pablo Ariel Duboue, David Gondek, J. William Murdock, John M. Prager, Paul Hoffmann, Janyce Wiebe_

- :fontawesome-solid-user-group: **Participant:** [ibm.prager](./enterprise/participants.md#ibm.prager)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ibm-watson.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ibm-watson.ent.final.pdf)
- :material-file-search: **Runs:** [IBM06JILAQD](./enterprise/runs.md#ibm06jilaqd) | [IBM06JAQD](./enterprise/runs.md#ibm06jaqd) | [IBM06JILAPQD](./enterprise/runs.md#ibm06jilapqd) | [IBM06JAQ](./enterprise/runs.md#ibm06jaq) | [IBM06QO](./enterprise/runs.md#ibm06qo) | [IBM06PR](./enterprise/runs.md#ibm06pr) | [IBM06EXP](./enterprise/runs.md#ibm06exp) | [IBM06MA](./enterprise/runs.md#ibm06ma)

??? abstract "Abstract"
	
	In 2006, IBM participated for the first time in the Enterprise Track, submitting runs for both the discussion and expert tasks. The Enterprise Track is intended to address information seeking tasks common in corporate settings using information that is readily available on corporate intranets. Because of confidentiality issues, the corpus used for this task is a snapshot of w3c.org as of June 2004, considering the W3C as a “corporation” that conducts its day-to-day business on the web. This corpus consists of a heterogeneous set of data sources, including web pages, mailing lists, code, wiki, etc. [Craswell et al. 2006]. The discussion task seeks e-mail messages that discuss the pro or con of a given subject matter, while the expert task requires that experts for given topics be identified. The main foci of our Enterprise Track experiments this year were on 1) problem-solving through adoption of multiple discussion and expert finding strategies, 2) combination of structured, semi-structured, and unstructured information for discussion and expert finding, 3) investigation of impact of select NLP techniques, such as multi-document summarization for expert pseudo-document generation and pro/con sentiment identification and retrieval, and 4) use of external resources for discussion and expert finding. The rest of this paper discusses the systems we developed for Enterprise Track participation, focusing on the four aspects outlined above. We will also discuss specific strategies we took to configure the systems for each of the four runs in both tasks, as well as their impact on system performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Chu-CarrollADGMPHW06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Chu-CarrollADGMPHW06,
		author = {Jennifer Chu{-}Carroll and Guillermo A. Averboch and Pablo Ariel Duboue and David Gondek and J. William Murdock and John M. Prager and Paul Hoffmann and Janyce Wiebe},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IBM} in {TREC} 2006 Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ibm-watson.ent.final.pdf},
		timestamp = {Sat, 21 Jan 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Chu-CarrollADGMPHW06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SOPHIA in Enterprise Track

_Vladimir Dobrynin, Kim Son Pham, David Patterson, Niall Rooney, Mykola Galushka_

- :fontawesome-solid-user-group: **Participant:** [uulster.patterson](./enterprise/participants.md#uulster.patterson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uulster.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uulster.ent.final.pdf)
- :material-file-search: **Runs:** [sophiarun1](./enterprise/runs.md#sophiarun1) | [sophiarun2](./enterprise/runs.md#sophiarun2) | [sophiarun3](./enterprise/runs.md#sophiarun3)

??? abstract "Abstract"
	
	SOPHIA participated in TREC 2006 as part of the Enterprise track (Expert search task). Given a topic our task was to find an ordered list of up to 100 experts (from a predefined list of candidate experts) and for every expert create an ordered list of up to 20 support documents. Support document should prove that given person is indeed an expert in the domain presented by the topic. We implemented 3 algorithms to solve this task which resulted in 3 runs sophiarun1, sophiarun2 and sophiarun3. All runs are based on Contextual Document Clustering (CDC) algorithm [1,2] applied to a part of W3C document corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DobryninPPRG06.bib) "
	```
	@inproceedings{DBLP:conf/trec/DobryninPPRG06,
		author = {Vladimir Dobrynin and Kim Son Pham and David Patterson and Niall Rooney and Mykola Galushka},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{SOPHIA} in Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uulster.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DobryninPPRG06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2006: Enterprise Email Discussion Search

_Yu Fan, Xiangji Huang, Aijun An_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./enterprise/participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/yorku.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/yorku.ent.final.pdf)
- :material-file-search: **Runs:** [york06ed01](./enterprise/runs.md#york06ed01) | [york06ed02](./enterprise/runs.md#york06ed02) | [york06ed03](./enterprise/runs.md#york06ed03) | [york06ed04](./enterprise/runs.md#york06ed04)

??? abstract "Abstract"
	
	We use the Okapi retrieval system to conduct the email discussion search. The following issues are investigated. First, we make use of the thread structure in the emails to re-rank the documents retrieved by Okapi. We would like to see whether such post-processing of the retrieval result can boost the retrieval performance. Second, in terms of query formulation, we investigate whether the use of only title in a topic achieves better or worse results than the inclusion of other fields such as description and narrative. Third, we investigate whether stemming and stop word removal play an important role in the email search. Our conclusion includes that (1) re-ranking documents using a straightforward method that considers the thread structure can make a small improvement to the retrieval performance, (2) formulating the query using all the fields in a topic achieves the best result, and (3) the use of stemming and stop word removal can improve the performance, but the degree of improvement depends on the stemming method and the stop word list used.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FanHA06.bib) "
	```
	@inproceedings{DBLP:conf/trec/FanHA06,
		author = {Yu Fan and Xiangji Huang and Aijun An},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2006: Enterprise Email Discussion Search},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/yorku.ent.final.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FanHA06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Language Models for Expert Finding–UIUC TREC 2006 Enterprise Track  Experiments

_Hui Fang, Lixin Zhou, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uiuc.zhai](./enterprise/participants.md#uiuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uillinois-uc.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uillinois-uc.ent.final.pdf)
- :material-file-search: **Runs:** [UIUCe1](./enterprise/runs.md#uiuce1) | [UIUCeFB1](./enterprise/runs.md#uiucefb1) | [UIUCeFB2](./enterprise/runs.md#uiucefb2) | [UIUCe2](./enterprise/runs.md#uiuce2)

??? abstract "Abstract"
	
	In this paper, we report our experiments in the TREC 2006 Enterprise Track. Our focus is to study a language model for expert finding. We extend an existing language model for expert retrieval in three aspects. First, we model the document-expert association using a mixure model instead of name matching heuristics as in the existing work; such a mixture model allows us to put different weights on email matching and name matching. Second, we propose to model the prior of an expert based on the counts of email matches in the supporting documents instead of using uniform prior as in the previous work. Finally, we perform topic expansion and generalize the model from computing the likelihood to computing the cross entropy. Our experiments show that the first two extensions are more effective than the third extension, though when optimized, they all seem to be effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FangZZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/FangZZ06,
		author = {Hui Fang and Lixin Zhou and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Language Models for Expert Finding--UIUC {TREC} 2006 Enterprise Track Experiments},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uillinois-uc.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FangZZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Solving the Enterprise TREC Task with Probabilistic Data Models

_Jan Frederik Forst, Anastasios Tombros, Thomas Rölleke_

- :fontawesome-solid-user-group: **Participant:** [queen-mary-ulondon.forst](./enterprise/participants.md#queen-mary-ulondon.forst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/queen-mary-ulondon.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/queen-mary-ulondon.ent.final.pdf)
- :material-file-search: **Runs:** [quotes](./enterprise/runs.md#quotes) | [body](./enterprise/runs.md#body) | [listbq](./enterprise/runs.md#listbq) | [www](./enterprise/runs.md#www)

??? abstract "Abstract"
	
	Expert identification has become an important information retrieval task. We present and investigate a number of approaches for identifying an expert. Different approaches are based on exploiting the structure of documents in the knowledge base. Furthermore, our system highlights the integration of database technology with information retrieval (DB+IR).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ForstTR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ForstTR06,
		author = {Jan Frederik Forst and Anastasios Tombros and Thomas R{\"{o}}lleke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Solving the Enterprise {TREC} Task with Probabilistic Data Models},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/queen-mary-ulondon.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ForstTR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pitt at TREC 2006: Identifying Experts via Email Discussions

_Daqing He, Yefei Peng_

- :fontawesome-solid-user-group: **Participant:** [upittsburgh.he](./enterprise/participants.md#upittsburgh.he)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/upitt.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/upitt.ent.final.pdf)
- :material-file-search: **Runs:** [PITTMANUAL](./enterprise/runs.md#pittmanual) | [PITTPHFREQ](./enterprise/runs.md#pittphfreq) | [PITTNOPH](./enterprise/runs.md#pittnoph) | [PITTPHFULL](./enterprise/runs.md#pittphfull)

??? abstract "Abstract"
	
	Identifying experts in a certain domain or a subject area has always been a challenge in various settings including commercial, academia, and governmental institutions. Our interests in this year's TREC Enterprise track are to utilize the email communications as the basis for identifying experts and their expertise on certain topics. In this report, we presented a method for identifying experts based on the emails they sent around. We hypothesize that experts would be more active in relevant email threads, would send longer emails, and would participate in the discussion at the very beginning of the threads. An algorithm based on these hypotheses was developed and tested in this year TREC enterprise track experiments to find experts for 49 topics based on documents in the W3C collections. Our initial experiment results produced suboptimal performance. This motivated us to examine the hypotheses more closely in the context of provided ground truth. Interestingly, the analysis on ground truth seems to confirm that all of our hypotheses have their merits in finding experts, so one future important question is how to utilize these rules in a right way.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeP06.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeP06,
		author = {Daqing He and Yefei Peng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Pitt at {TREC} 2006: Identifying Experts via Email Discussions},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/upitt.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeP06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### In Enterprise Search: Methods to Identify Argumentative Discussions  and to Find Topical Experts

_Maheedhar Kolla, Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo-clarke](./enterprise/participants.md#uwaterloo-clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uwaterloo-kolla.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uwaterloo-kolla.ent.final.pdf)
- :material-file-search: **Runs:** [uwTbaseline](./enterprise/runs.md#uwtbaseline) | [uwTDbaseline](./enterprise/runs.md#uwtdbaseline) | [uwTsubj](./enterprise/runs.md#uwtsubj) | [uwTDsubj](./enterprise/runs.md#uwtdsubj) | [uwXSHUBS](./enterprise/runs.md#uwxshubs) | [uwXSOUT](./enterprise/runs.md#uwxsout) | [uwXSPMI](./enterprise/runs.md#uwxspmi)

??? abstract "Abstract"
	
	Our intention in taking part in this year's Enterprise Track is to experiment with various re-ranking approaches in solving two problems: email search and expert search. In email discussion search, we propose methods to retrieve email messages that contain pro/con argument about the topic in discussion. We compute the likelihood of an email having a pro/con argument about the topic and re-rank emails based on the likelihood of containing topical subjective opinion. In expert search, we explored methods to identify experts for a given topic by analyzing the mailing patterns in the email archive.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KollaV06.bib) "
	```
	@inproceedings{DBLP:conf/trec/KollaV06,
		author = {Maheedhar Kolla and Olga Vechtomova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {In Enterprise Search: Methods to Identify Argumentative Discussions and to Find Topical Experts},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uwaterloo-kolla.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KollaV06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Judging Expertise–WIM at Enterprise

_Chen Lin, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [fudanu.niu](./enterprise/participants.md#fudanu.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/fudan-niu.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/fudan-niu.ent.final.pdf)
- :material-file-search: **Runs:** [FDUSO](./enterprise/runs.md#fduso) | [FDUSN](./enterprise/runs.md#fdusn) | [FDUSF](./enterprise/runs.md#fdusf)

??? abstract "Abstract"
	
	This document reports experiment and result of Fudan WIM group in Expert Search track in TREC 2006. Our research mainly focus on the measurement of expertise. Inspired by the human procedure of expert search, we construct 2 models, a language model and a social network model are compared. The association function of expert and document is modified. And email search techniques are employed in document retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinN06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinN06,
		author = {Chen Lin and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Judging Expertise--WIM at Enterprise},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/fudan-niu.ent.final.pdf},
		timestamp = {Tue, 20 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinN06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2006: Experiments in Terabyte and  Enterprise Tracks with Terrier

_Christina Lioma, Craig Macdonald, Vassilis Plachouras, Jie Peng, Ben He, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uglasgow.ounis](./enterprise/participants.md#uglasgow.ounis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uglasgow.tera.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uglasgow.tera.ent.final.pdf)
- :material-file-search: **Runs:** [uogX06csnP](./enterprise/runs.md#uogx06csnp) | [uogX06csnQEF](./enterprise/runs.md#uogx06csnqef) | [uogX06csnQE](./enterprise/runs.md#uogx06csnqe) | [uogX06ecm](./enterprise/runs.md#uogx06ecm)

??? abstract "Abstract"
	
	In TREC 2006, we participate in three tasks of the Terabyte and Enterprise tracks. We continue experiments using Terrier1, our modular and scalable Information Retrieval (IR) platform. Furthering our research into the Divergence From Randomness (DFR) framework of weighting models, we introduce two new effective and low-cost models, which combine evidence from document structure and capture term dependence and proximity, respectively. Additionally, in the Terabyte track, we improve on our query expansion mechanism on fields, presented in TREC 2005, with a new and more refined technique, which combines evidence in a linear, rather than uniform, way. We also introduce a novel, low-cost syntactically-based noise reduction technique, which we flexibly apply to both the queries and the index. Furthermore, in the Named Page Finding task, we present a new technique for combining query-independent evidence, in the form of prior probabilities. In the Enterprise track, we test our new voting model for expert search. Our experiments focus on the need for candidate length normalisation, and on how retrieval performance can be enhanced by applying retrieval techniques to the underlying ranking of documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiomaMPPHO06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiomaMPPHO06,
		author = {Christina Lioma and Craig Macdonald and Vassilis Plachouras and Jie Peng and Ben He and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2006: Experiments in Terabyte and Enterprise Tracks with Terrier},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uglasgow.tera.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiomaMPPHO06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Window-based Enterprise Expert Search

_Wei Lu, Stephen E. Robertson, Andrew MacFarlane, Haozhen Zhao_

- :fontawesome-solid-user-group: **Participant:** [cityu.macfarlane](./enterprise/participants.md#cityu.macfarlane)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cityu-london.ent.pdf](http://trec.nist.gov/pubs/trec15/papers/cityu-london.ent.pdf)
- :material-file-search: **Runs:** [ex7512](./enterprise/runs.md#ex7512) | [ex5512](./enterprise/runs.md#ex5512) | [ex3512](./enterprise/runs.md#ex3512) | [ex5518](./enterprise/runs.md#ex5518)

??? abstract "Abstract"
	
	This is the first year for the participation of the City University Centre of Interactive System Research (CISR) in the Expert Search Task. In this paper, we describe an expert search experiment based on window-based techniques, that is, we build profile for each expert by using information around the expert's name and email address in the documents. We then use the traditional IR techniques to search and rank experts. Our experiment is done on Okapi and BM25 is used as the ranking model. Results show that parameter b does have an effect on the retrieval effectiveness and using a smaller value for b produces better results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuRMZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuRMZ06,
		author = {Wei Lu and Stephen E. Robertson and Andrew MacFarlane and Haozhen Zhao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Window-based Enterprise Expert Search},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cityu-london.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuRMZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2006 at Maryland: Blog, Enterprise, Legal and QA Tracks

_Douglas W. Oard, Tamer Elsayed, Jianqiang Wang, Yejun Wu, Pengyi Zhang, Eileen G. Abels, Jimmy Lin, Dagobert Soergel_

- :fontawesome-solid-user-group: **Participant:** [umaryland.oard](./enterprise/participants.md#umaryland.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf)
- :material-file-search: **Runs:** [UMDthrdTTL](./enterprise/runs.md#umdthrdttl) | [UMDthrdTTLDS](./enterprise/runs.md#umdthrdttlds) | [UMDthrdTTLNR](./enterprise/runs.md#umdthrdttlnr) | [UMDemailTTL](./enterprise/runs.md#umdemailttl) | [UMDemailTLNR](./enterprise/runs.md#umdemailtlnr)

??? abstract "Abstract"
	
	In TREC 2006, teams from the University of Maryland participated in the Blog track, the Expert Search task of the Enterprise track, the Complex Interactive Question Answering task of the Question Answering track, and the Legal track. This paper reports our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardEWWZALS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardEWWZALS06,
		author = {Douglas W. Oard and Tamer Elsayed and Jianqiang Wang and Yejun Wu and Pengyi Zhang and Eileen G. Abels and Jimmy Lin and Dagobert Soergel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 at Maryland: Blog, Enterprise, Legal and {QA} Tracks},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/OardEWWZALS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2006: Enterprise Track

_Desislava Petkova, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./enterprise/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umass.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umass.ent.final.pdf)
- :material-file-search: **Runs:** [UMaTiMixHdr](./enterprise/runs.md#umatimixhdr) | [UMaTiMixThr](./enterprise/runs.md#umatimixthr) | [UMaTDMixThr](./enterprise/runs.md#umatdmixthr) | [UMaTiSmoThr](./enterprise/runs.md#umatismothr) | [UMaTiDm](./enterprise/runs.md#umatidm) | [UMaTNDm](./enterprise/runs.md#umatndm) | [UMaTNFb](./enterprise/runs.md#umatnfb) | [UMaTDFb](./enterprise/runs.md#umatdfb)

??? abstract "Abstract"
	
	This paper gives an overview of the work done at the University of Massachusetts, Amherst for the TREC 2006 Enterprise track. For the discussion search task, we compare two methods for incorporating thread evidence into the language models of email messages. For the expert finding task, we create implicit expert representations as mixtures of language models from associated documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PetkovaC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/PetkovaC06,
		author = {Desislava Petkova and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2006: Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umass.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PetkovaC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BUPT at TREC 2006: Enterprise Track

_Zhao Ru, Quian Li, Weiran Xu, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [beijingu-posts-tele.weiran](./enterprise/participants.md#beijingu-posts-tele.weiran)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/beijing-upt.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/beijing-upt.ent.final.pdf)
- :material-file-search: **Runs:** [PRISEXB](./enterprise/runs.md#prisexb) | [PRISEXR](./enterprise/runs.md#prisexr) | [PRISEXRM](./enterprise/runs.md#prisexrm) | [PRISEXRMT](./enterprise/runs.md#prisexrmt)

??? abstract "Abstract"
	
	This is the second time that Pattern Recognition and Intelligent System Lab (PRIS) participate in TREC. In enterprise track, our efforts have been focused on the expert search task this year. The goal is to develop more elaborate model for expert searching and find effective support providing method for new request.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuLXG06.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuLXG06,
		author = {Zhao Ru and Quian Li and Weiran Xu and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BUPT} at {TREC} 2006: Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/beijing-upt.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuLXG06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Case Western Reserve University at the TREC 2006 Enterprise Track

_Adam D. Troy, Guo-Qiang Zhang_

- :fontawesome-solid-user-group: **Participant:** [case-western.ru.troy](./enterprise/participants.md#case-western.ru.troy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/case-western.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/case-western.ent.final.pdf)
- :material-file-search: **Runs:** [basic](./enterprise/runs.md#basic) | [allbasic](./enterprise/runs.md#allbasic) | [w1r1s1](./enterprise/runs.md#w1r1s1)

??? abstract "Abstract"
	
	For Case Western Reserve University's debut participation in TREC, we chose to participate in the Enterprise Track expert search task. Our motivation for participation stems from our work developing expert search capability for our prototype vertical digital library, MEMS World Online1. Our work incorporates two unique aspects. First, our relevance ranking mechanism relies on term position within each document rather than the number of term occurrences. This mechanism takes into account both term document rank and term co-occurrence proximity. Second, the expert score of closely related colleagues has a small effect on the score of each related expert. This follows the intuition that experts on a particular topic within a single organization tend to closely collaborate with one another. We also make some use of WordNet synonyms. We submitted a total of three runs to this years expert search task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TroyZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/TroyZ06,
		author = {Adam D. Troy and Guo{-}Qiang Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Case Western Reserve University at the {TREC} 2006 Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/case-western.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TroyZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Correlating Topic Rankings and Person Rankings to Find Experts

_Thijs Westerveld_

- :fontawesome-solid-user-group: **Participant:** [lowlands-team.deVries](./enterprise/participants.md#lowlands-team.devries)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cwi.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/cwi.ent.final.pdf)
- :material-file-search: **Runs:** [MAPTrelCret](./enterprise/runs.md#maptrelcret) | [MAPCrelTret](./enterprise/runs.md#mapcreltret) | [SPlog](./enterprise/runs.md#splog) | [SP](./enterprise/runs.md#sp)

??? abstract "Abstract"
	
	Expert search is about finding people rather than documents. The goal is to retrieve a ranked list of candidates with expertise on a given topic. The task is studied in the context of the enterprise track. We describe an approach that compares topic profiles and candidate profiles directly. These profiles are not based on unordered sets of documents, but on ranked lists. This allows us to differentiate between documents that are highly related to a topic or a candidate and documents that are only marginally related. The ranked lists for topics and candidates are obtained by simple retrieval queries. The correlation between the ranked list of documents for a topic and the ranked list for a candidate is used as an indicator of the candidate's expertise on the topic. We study different ways to rank documents for the candidate profiles as well as various ways of comparing the document and candidate based ranked lists. Experiments show that starting from the right candidate profiles, reasonable results can be obtained. Furthermore, it seems important to take a correlation measure that takes into account the orderings of documents in both the candidate profile and the documents profile.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Westerveld06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Westerveld06,
		author = {Thijs Westerveld},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Correlating Topic Rankings and Person Rankings to Find Experts},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cwi.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Westerveld06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2006: Genomics and Enterprise Tracks

_Zhihao Yang, Hongfei Lin, Yanpeng Li, Linhong Xu, Yu Pan, Baoyan Liu_

- :fontawesome-solid-user-group: **Participant:** [dalianu.yang](./enterprise/participants.md#dalianu.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/dalianu.geo.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/dalianu.geo.ent.final.pdf)
- :material-file-search: **Runs:** [DUTDS1](./enterprise/runs.md#dutds1) | [DUTDS2](./enterprise/runs.md#dutds2) | [DUTDS3](./enterprise/runs.md#dutds3) | [DUTDS4](./enterprise/runs.md#dutds4) | [DUTEX1](./enterprise/runs.md#dutex1) | [DUTEX2](./enterprise/runs.md#dutex2) | [DUTEX3](./enterprise/runs.md#dutex3) | [DUTEX4](./enterprise/runs.md#dutex4)

??? abstract "Abstract"
	
	This paper describes the techniques we applied for the two TREC 2006 tracks, i.e., Genomics and Enterprise track. For the Genomics Track, we used a Rocchio relevance feedback method to expand the terms and then performed passage retrieval by building dual index and using half overlapped windows passages. Several approaches to merge the results and rerank the passages are presented. For the Enterprise track, we stripped the non-letter character from documents and query, built the index by indri or lemur and established expert document pools.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLLXPL06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangLLXPL06,
		author = {Zhihao Yang and Hongfei Lin and Yanpeng Li and Linhong Xu and Yu Pan and Baoyan Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2006: Genomics and Enterprise Tracks},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/dalianu.geo.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangLLXPL06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ricoh Research at TREC 2006: Enterprise Track

_Ganmei You, Yaojie Lu, Gang Li, Yueyan Yin_

- :fontawesome-solid-user-group: **Participant:** [ricoh.you](./enterprise/participants.md#ricoh.you)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ricoh.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ricoh.ent.final.pdf)
- :material-file-search: **Runs:** [srcbds1](./enterprise/runs.md#srcbds1) | [srcbds2](./enterprise/runs.md#srcbds2) | [srcbds3](./enterprise/runs.md#srcbds3) | [srcbds4](./enterprise/runs.md#srcbds4) | [srcbds5](./enterprise/runs.md#srcbds5) | [SRCBEX1](./enterprise/runs.md#srcbex1) | [SRCBEX2](./enterprise/runs.md#srcbex2) | [SRCBEX5](./enterprise/runs.md#srcbex5) | [SRCBEX3](./enterprise/runs.md#srcbex3) | [SRCBEX4](./enterprise/runs.md#srcbex4)

??? abstract "Abstract"
	
	This article presents our contributions to expert search and discussion search of Enterprise Track in TREC 2006. In discussion search, we take advantage of the redundant patterns of emails, such as the subject, author, sent time, etc., which we incorporate in a field-based weighting method to mine discussion topics with more robustness. Some non-content features, such as time-line and mail thread are found to be useful as experiments showed they improve the precision of the search. In expert search, two variants of the BM25 and DFR_BM25 weighting models - namely V-BM25 and V-DFR_BM25 - are put forward. Query-based document length, not profile length, is used as document length in these weighting models to eliminate multiple topic drift. In addition, we propose a variant of an existing phrase weighting model to decrease topic confusion (V-phrase) and a two-stage field-based search method to refine the results. We demonstrate these approaches can effectively improve expert search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YouLLY06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YouLLY06,
		author = {Ganmei You and Yaojie Lu and Gang Li and Yueyan Yin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Ricoh Research at {TREC} 2006: Enterprise Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ricoh.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YouLLY06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Open University at TREC 2006 Enterprise Track Expert Search  Task

_Jianhan Zhu, Dawei Song, Stefan M. Rüger, Marc Eisenstadt, Enrico Motta_

- :fontawesome-solid-user-group: **Participant:** [openu.zhu](./enterprise/participants.md#openu.zhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/openu.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/openu.ent.final.pdf)
- :material-file-search: **Runs:** [kmiZhu2](./enterprise/runs.md#kmizhu2) | [kmiZhu4](./enterprise/runs.md#kmizhu4) | [kmiZhu1](./enterprise/runs.md#kmizhu1) | [kmiZhu5](./enterprise/runs.md#kmizhu5)

??? abstract "Abstract"
	
	The Multimedia and Information Systems group at the Knowledge Media Institute of the Open University participated in the Expert Search task of the Enterprise Track in TREC 2006. We have proposed to address three main innovative points in a two-stage language model, which consists of a document relevance model and a cooccurrence model, in order to improve the performance of expert search. The three innovative points are based on characteristics of documents. First, document authority in terms of their PageRanks is considered in the document relevance model. Second, document internal structure is taken into account in the co-occurrence model. Third, we consider multiple levels of associations between experts and query terms in the co-occurrence model. Our experiments on the TREC2006 Expert Search task show that addressing the above three points has led to improved effectiveness of expert search on the W3C dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuSREM06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuSREM06,
		author = {Jianhan Zhu and Dawei Song and Stefan M. R{\"{u}}ger and Marc Eisenstadt and Enrico Motta},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Open University at {TREC} 2006 Enterprise Track Expert Search Task},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/openu.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuSREM06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Blog 

#### Overview of the TREC 2006 Blog Track

_Iadh Ounis, Craig Macdonald, Maarten de Rijke, Gilad Mishne, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/BLOG06.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/BLOG06.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The rise on the Internet of blogging, the creation of journal-like web page logs, has created a highly dynamic subset of the World Wide Web that evolves and responds to real-world events. Indeed, blogs (or weblogs) have recently emerged as a new grassroots publishing medium. The so-called blogosphere (the collection of blogs on the Internet) opens up several new interesting research areas. Blogs have many interesting features: entries are added in chronological order, sometimes at a high volume. In addition, many blogs are created by their authors, not intended for any sizable audience, but purely as a mechanism for self-expression. Extremely accessible blog software has facilitated the act of blogging to a wide-ranging audience, their blogs reflecting their opinions, philosophies and emotions. Traditional media tends to focus on “heavy-hitting” blogs devoted to politics, punditry and technology. However, there are many different genres of blogs, some written around a specific topic, some covering several, and others talking about personal daily life [3]. The Blog track began this year, with the aim to explore the information seeking behaviour in the blogosphere. For this purpose, a new large-scale test collection, namely the TREC Blog06 collection, has been created. In the first pilot run of the track in 2006, we had two tasks, a main task (opinion retrieval) and an open task. The opinion retrieval task focuses on a specific aspect of blogs: the opinionated nature of many blogs. The second task was introduced to allow participants the opportunity to influence the determination of a suitable second task (for 2007) on other aspects of blogs, such as the temporal/event-related nature of many blogs, or the severity of spam in the blogosphere. The remainder of this paper is structured as follows. Section 2 provides a short description of the newly created Blog06 test collection. Section 3 describes the opinion task, and provides an overview of the submitted runs of the participants. Section 4 describes the open task and the submitted proposals. We provide concluding remarks in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OunisMRMS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/OunisMRMS06,
		author = {Iadh Ounis and Craig Macdonald and Maarten de Rijke and Gilad Mishne and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2006 Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/BLOG06.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OunisMRMS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Blog Mining Through Opinionated Words

_Giuseppe Attardi, Maria Simi_

- :fontawesome-solid-user-group: **Participant:** [upisa.attardi](./blog/participants.md#upisa.attardi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/upisa.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/upisa.blog.final.pdf)
- :material-file-search: **Runs:** [pisaBlDesOp6](./blog/runs.md#pisabldesop6) | [pisaBlDes](./blog/runs.md#pisabldes) | [pisaBlTit](./blog/runs.md#pisabltit) | [pisaBlTitOp6](./blog/runs.md#pisabltitop6)

??? abstract "Abstract"
	
	Intent mining is a special kind of document analysis whose goal is to assess the attitude of the document author with respect to a given subject. Opinion mining is a kind of intent mining where the attitude is a positive or negative opinion. Most systems tackle the problem with a two step approach, an information retrieval followed by a postprocess or filter phase to identify opinionated blogs. We explored a single stage approach to opinion mining, retrieving opinionated documents ranked with a special ranking function which exploits an index enriched with opinion tags. A set of subjective words are used as tags for identifying opinionated sentences. Subjective words are marked as “opinionated” and are used in the retrieval phase to boost the rank of documents containing them. In indexing the collection, we recovered the relevant content from the blog permalink pages, exploiting HTML metadata about the generator and heuristics to remove irrelevant parts from the body. The index also contains information about the occurrence of opinionated words, extracted from an analysis of WordNet glosses. The experiments compared the precision of normal queries with respect to queries which included as constraint the proximity to an opinionated word. The results show a significant improvement in precision for both topic relevance and opinion relevance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AttardiS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/AttardiS06,
		author = {Giuseppe Attardi and Maria Simi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Blog Mining Through Opinionated Words},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/upisa.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AttardiS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Robert Gordon University

_Malcolm Clark, Ulises Cerviño Beresi, Stuart N. K. Watt, David J. Harper_

- :fontawesome-solid-user-group: **Participant:** [robert-gordonu.harper](./blog/participants.md#robert-gordonu.harper)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/robert-gordonu.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/robert-gordonu.blog.final.pdf)
- :material-file-search: **Runs:** [rguBL](./blog/runs.md#rgubl) | [rguOPN](./blog/runs.md#rguopn) | [rguSBJ](./blog/runs.md#rgusbj) | [Abstract](./blog/runs.md#abstract)

??? abstract "Abstract"
	
	Blogs are highly rich in opinion making their automatic processing appealing to marketing companies, the media, costumer centres, etc. TREC ran a Blog track in 2006 with two tasks: opinion retrieval and an open task. This document reports the experiments conducted at The Robert Gordon University (RGU) where we used Statistical Language Models combined with shallow parsing techniques for the opinion retrieval problem.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkBWH06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkBWH06,
		author = {Malcolm Clark and Ulises Cervi{\~{n}}o Beresi and Stuart N. K. Watt and David J. Harper},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Robert Gordon University},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/robert-gordonu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkBWH06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Opinion Retrieval Experiments Using Generative Models: Experiments  for the TREC 2006 Blog Track

_Koji Eguchi, Chirag Shah_

- :fontawesome-solid-user-group: **Participant:** [nii-eguchi](./blog/participants.md#nii-eguchi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/nii.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/nii.blog.final.pdf)
- :material-file-search: **Runs:** [NII5](./blog/runs.md#nii5) | [NII3](./blog/runs.md#nii3) | [NII1](./blog/runs.md#nii1) | [NII7](./blog/runs.md#nii7) | [NII6](./blog/runs.md#nii6) | [NIIabstract](./blog/runs.md#niiabstract) | [NIIfinal](./blog/runs.md#niifinal)

??? abstract "Abstract"
	
	Ranking blog posts that express opinions regarding a given topic should serve a critical function in helping users. We explored three types of opinion retrieval methods in the framework of probabilistic language models. The first method combines topic-relevance model and opinion-relevance model that captures topic dependence of the opinion expressions. The second method makes use of probability that any of opinion-bearing words appear in each target document as document prior probability in query-likelihood model. The third method makes use of probability that any of adjectives or adverbs appear in each target document as document prior probability, assuming opinionated documents tend to contain more adjectives or adverbs than other documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EguchiS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/EguchiS06,
		author = {Koji Eguchi and Chirag Shah},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Opinion Retrieval Experiments Using Generative Models: Experiments for the {TREC} 2006 Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/nii.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EguchiS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The BlogVox Opinion Retrieval System

_Akshay Java, Pranam Kolari, Timothy W. Finin, Anupam Joshi, Justin Martineau_

- :fontawesome-solid-user-group: **Participant:** [umaryland-bc.finin](./blog/participants.md#umaryland-bc.finin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umbc-jhu.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umbc-jhu.blog.final.pdf)
- :material-file-search: **Runs:** [UABas11](./blog/runs.md#uabas11) | [UAEX13](./blog/runs.md#uaex13) | [UAEX21](./blog/runs.md#uaex21) | [UAEX12](./blog/runs.md#uaex12) | [UAEX11](./blog/runs.md#uaex11) | [uaplabstract](./blog/runs.md#uaplabstract) | [uaplfinal](./blog/runs.md#uaplfinal)

??? abstract "Abstract"
	
	The BlogVox system retrieves opinionated blog posts specified by ad hoc queries. BlogVox was developed for the 2006 TREC blog track by the University of Maryland, Baltimore County and the Johns Hopkins University Applied Physics Laboratory using a novel system to recognize legitimate posts and discriminate against spam blogs. It also processes posts to eliminate extraneous non-content, including blog-rolls, link-rolls, advertisements and sidebars. After retrieving posts relevant to a topic query, the system processes them to produce a set of independent features estimating the likelihood that a post expresses an opinion about the topic. These are combined using an SVM-based system and integrated with the relevancy score to rank the results. We evaluate BlogVox's performance against human assessors. We also evaluate the individual splog filtering and non-content removal components of BlogVox.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JavaKFJM06.bib) "
	```
	@inproceedings{DBLP:conf/trec/JavaKFJM06,
		author = {Akshay Java and Pranam Kolari and Timothy W. Finin and Anupam Joshi and Justin Martineau},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The BlogVox Opinion Retrieval System},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umbc-jhu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JavaKFJM06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UALR at TREC: Blog Track

_Hemant Joshi, Coskun Bayrak, Xiaowei Xu_

- :fontawesome-solid-user-group: **Participant:** [uarkansas-littlerock.joshi](./blog/participants.md#uarkansas-littlerock.joshi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uarkansas.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uarkansas.blog.final.pdf)
- :material-file-search: **Runs:** [UALR06m5Tr1](./blog/runs.md#ualr06m5tr1) | [UALR06a260r2](./blog/runs.md#ualr06a260r2) | [UALR06m260r3](./blog/runs.md#ualr06m260r3) | [UALR06a500r4](./blog/runs.md#ualr06a500r4) | [UALR06m500r5](./blog/runs.md#ualr06m500r5)

??? abstract "Abstract"
	
	We consider Opinion Blog retrieval from classification point of view. We used the active learning method with an integrated feature selection to train the Support Vector Machine algorithm. We wanted to study the effect of different types of features on the classification accuracy of the model generated by the classifier algorithm. We considered mainly three different types of features for 5 runs submitted. Feature types include bag-of-words features, seed-words as features and statistical features. Bag-of-words features are generated from the actual blog data. Seed-words were manually generated specific to the domain of interest. Statistical features studied included the ratio of linguistic features to total number of words. We built models using an iterative process and studied accuracy as well as coverage of each model. Study of different features is important in order to build a better model. Feature selection algorithms can choose the best features among the available ones but different features have costs associated with them. We need features that not only predict class labels or contribute towards prediction but the feature should also be representative of the entire dataset, especially test data. Training the classifier on such features will yield better coverage and training accuracy for the model. We compared the three different models generated by three different feature generation strategies. Our preliminary results indicate that seed-words that are specific to a particular domain or particular type of classification achieve better accuracy and coverage. In general, bag-of-words features are tightly coupled with the data they represent. On the other hand, statistical features are independent of the actual words used. Statistical features are more useful in building robust models that can be used with different languages and for different tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoshiBX06.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoshiBX06,
		author = {Hemant Joshi and Coskun Bayrak and Xiaowei Xu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UALR} at {TREC:} Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uarkansas.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoshiBX06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Language Model with Sentiment Analysis for Opinion Retrieval  of Blog-Post

_Xiangwen Liao, Donglin Cao, Songbo Tan, Yue Liu, Guodong Ding, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas-iiis.tan](./blog/participants.md#cas-iiis.tan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cas-ict.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/cas-ict.blog.final.pdf)
- :material-file-search: **Runs:** [ICT](./blog/runs.md#ict) | [IIIS](./blog/runs.md#iiis)

??? abstract "Abstract"
	
	This paper describes our participation in Blog Opinion Retrieval task this year. We conduct experiments on “FirteX” platform that is developed by our lab. Language Model is used to retrieve related blog unit. Interactive Knowledge is adopted to expand query for retrieve blog unit include opinion. Then we introduce a novel extracting technology to extract text from retrieved blog-post. Finally, Lexicon based method is used to rerank the document by opinion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiaoCTLDC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiaoCTLDC06,
		author = {Xiangwen Liao and Donglin Cao and Songbo Tan and Yue Liu and Guodong Ding and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Language Model with Sentiment Analysis for Opinion Retrieval of Blog-Post},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cas-ict.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiaoCTLDC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Splog Detection Task and A Solution Based on Temporal and Link  Properties

_Yu-Ru Lin, Wen-Yen Chen, Xiaolin Shi, Richard Sia, Xiaodan Song, Yun Chi, Koji Hino, Hari Sundaram, Jun'ichi Tatemura, Belle L. Tseng_

- :fontawesome-solid-user-group: **Participant:** [nec-labs.tseng](./blog/participants.md#nec-labs.tseng)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/nec.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/nec.blog.final.pdf)
- :material-file-search: **Runs:** [necabstract](./blog/runs.md#necabstract) | [necnistfinal](./blog/runs.md#necnistfinal)

??? abstract "Abstract"
	
	Spam blogs (splogs) have become a major problem in the increasingly popular blogosphere. Splogs are detrimental in that they corrupt the quality of information retrieved and they waste tremendous network and storage resources. We study several research issues in splog detection. First, in comparison to web spam and email spam, we identify some unique characteristics of splog. Second, we propose a new online task that captures the unique characteristics of splog, in addition to tasks based on the traditional IR evaluation framework. The new task introduces a novel time-sensitive detection evaluation to indicate how quickly a detector can identify splogs. Third, we propose a splog detection algorithm that combines traditional content features with temporal and link regularity features that are unique to blogs. Finally, we develop an annotation tool to generate ground truth on a sampled subset of the TREC-Blog dataset. We conducted experiments on both offline (traditional splog detection) and our proposed online splog detection task. Experiments based on the annotated ground truth set show excellent results on both offline and online splog detection tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinCSSSCHSTT06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinCSSSCHSTT06,
		author = {Yu{-}Ru Lin and Wen{-}Yen Chen and Xiaolin Shi and Richard Sia and Xiaodan Song and Yun Chi and Koji Hino and Hari Sundaram and Jun'ichi Tatemura and Belle L. Tseng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Splog Detection Task and {A} Solution Based on Temporal and Link Properties},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/nec.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinCSSSCHSTT06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Deep Context with a Sense-of-Self

_Robert McArthur_

- :fontawesome-solid-user-group: **Participant:** [csiro-ict.mcarthur](./blog/participants.md#csiro-ict.mcarthur)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/csiro.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/csiro.blog.final.pdf)
- :material-file-search: **Runs:** [csirabstract](./blog/runs.md#csirabstract) | [csirofull](./blog/runs.md#csirofull)

??? abstract "Abstract"
	
	There is a trend in information retrieval to an increased involvement of context. The success of recent workshops at SIGIR [8] and the subsequent 2006 IIiX Symposium 1 , the SIGIR exploratory search workshop 2 , and the outcome of the 2004 SWIRL workshop 3 [21] are indicators that elements of user context are both sort and becoming available. “The provision of tools…can yield great rewards for users, especially when contextual factors such as user emotion, task constraints, and dynamism of information needs are considered” [26]. Recent weblog workshops 4 reflect a strong interest in the discovery of context about the user in the form of the blogger's age [2, 24], gender [23, 24], opinions, sentiments and opinions expressed [9, 19, 22], mood levels [1, 20], happiness [18], residential area [28] and social network(s) [6, 7, 11-13, 25]. The research concentrated on particular forms of identifying or extracting the information, providing fertile ground for TREC-style comparisons of the approaches. Considerable interest has been shown in the analysis of sentiment in weblogs ([1, 4, 18-20, 22]). This broad umbrella encompasses notions of mood, opinion, emotion and happiness. Sentiment is only one aspect of user context. Indeed, many of the published notions of sentiment derive from reflection of authorship. That is, determination of the mood, opinion or emotion comes through analysis of the artefacts of communication, the blog entry, and is deemed a reflection of the sentiment of the author at the time. Of course, the assumption is that a person's writing reflects their inner state of being. Although it is tempting to, repeating history, ignore the author and concentrate on the blog entry itself, the focus should remain on determining more about the user. To this end, more information about the user is required apart from the emphasis on the (usually) explicit manifestations of their selves. Figure 1 presents this difference by separating what we know about the document (e.g. style), what we know about the user from the document at a particular point in time (e.g. sentiment), and the more implicit and meta-information which is derived from the sentiment and which captures deeper context about the user. An example of such information is a computational manifestation of a person's sense-of-self. This has been investigated previously using mailing list records in an online health setting ([15]) and this paper uses it as an exemplar of deeper user context, showing how to apply the ideas and techniques to blog data in a TREC setting
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McArthur06.bib) "
	```
	@inproceedings{DBLP:conf/trec/McArthur06,
		author = {Robert McArthur},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Deep Context with a Sense-of-Self},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/csiro.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McArthur06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multiple Ranking Strategies for Opinion Retrieval in Blogs - The University  of Amsterdam at the 2006 TREC Blog Track

_Gilad Mishne_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.ilps](./blog/participants.md#uamsterdam.ilps)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uamsterdam.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uamsterdam.blog.final.pdf)
- :material-file-search: **Runs:** [UAmsB06Base](./blog/runs.md#uamsb06base) | [UAmsB06L](./blog/runs.md#uamsb06l) | [UAmsB06S](./blog/runs.md#uamsb06s) | [UAmsB06O](./blog/runs.md#uamsb06o) | [UAmsB06All](./blog/runs.md#uamsb06all)

??? abstract "Abstract"
	
	We describe our participation in the Opinion Retrieval task at TREC 2006. Our approach to identifying opinions in blog post consisted of scoring the posts separately on various aspects associated with an expression of opinion about a topic, including shallow sentiment analysis, spam detection, and link-based authority estimation. The separate approaches were combined into a single ranking, yielding significant improvement over a content-only baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Mishne06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Mishne06,
		author = {Gilad Mishne},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Multiple Ranking Strategies for Opinion Retrieval in Blogs - The University of Amsterdam at the 2006 {TREC} Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uamsterdam.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Mishne06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2006 at Maryland: Blog, Enterprise, Legal and QA Tracks

_Douglas W. Oard, Tamer Elsayed, Jianqiang Wang, Yejun Wu, Pengyi Zhang, Eileen G. Abels, Jimmy Lin, Dagobert Soergel_

- :fontawesome-solid-user-group: **Participant:** [umaryland.oard](./blog/participants.md#umaryland.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf)
- :material-file-search: **Runs:** [ParTitDesDef](./blog/runs.md#partitdesdef) | [PasTitDesDef](./blog/runs.md#pastitdesdef) | [ParTiDesDmt2](./blog/runs.md#partidesdmt2) | [ParTiDesDmt3](./blog/runs.md#partidesdmt3) | [ParTitDef](./blog/runs.md#partitdef)

??? abstract "Abstract"
	
	In TREC 2006, teams from the University of Maryland participated in the Blog track, the Expert Search task of the Enterprise track, the Complex Interactive Question Answering task of the Question Answering track, and the Legal track. This paper reports our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardEWWZALS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardEWWZALS06,
		author = {Douglas W. Oard and Tamer Elsayed and Jianqiang Wang and Yejun Wu and Pengyi Zhang and Eileen G. Abels and Jimmy Lin and Dagobert Soergel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 at Maryland: Blog, Enterprise, Legal and {QA} Tracks},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/OardEWWZALS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Knowledge Transfer and Opinion Detection in the TREC 2006 Blog Track

_Hui Yang, Jamie Callan, Luo Si_

- :fontawesome-solid-user-group: **Participant:** [cmu.dir.callan](./blog/participants.md#cmu.dir.callan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cmu.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/cmu.blog.final.pdf)
- :material-file-search: **Runs:** [blog06r1](./blog/runs.md#blog06r1) | [blog06r5](./blog/runs.md#blog06r5) | [blog06r6](./blog/runs.md#blog06r6) | [blog06r2](./blog/runs.md#blog06r2) | [blog06r4](./blog/runs.md#blog06r4) | [blog06r3](./blog/runs.md#blog06r3)

??? abstract "Abstract"
	
	The paper describes the opinion detection system developed in Carnegie Mellon University for TREC 2006 Blog track. The system performed a two-stage process: passage retrieval and opinion detection. Due to lack of training data for the TREC Blog corpus, online opinion reviews provided in other domains, such as movie review and product review, were used as the training data. Knowledge transfer was performed to make the cross-domain learning possible. Logistic regression ranked the sentence-level opinions vs. objective statements. The evaluation shows that the algorithm is effective in the task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangCS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangCS06,
		author = {Hui Yang and Jamie Callan and Luo Si},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Knowledge Transfer and Opinion Detection in the {TREC} 2006 Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cmu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangCS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2006 Blog Track

_Kiduk Yang, Ning Yu, Alejandro Valerio, Hui Zhang_

- :fontawesome-solid-user-group: **Participant:** [indianau.yang](./blog/participants.md#indianau.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/indianau.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/indianau.blog.final.pdf)
- :material-file-search: **Runs:** [woqs2](./blog/runs.md#woqs2) | [wxoqs2](./blog/runs.md#wxoqs2) | [woqln2](./blog/runs.md#woqln2) | [wxoqln2](./blog/runs.md#wxoqln2) | [wxoqf2](./blog/runs.md#wxoqf2)

??? abstract "Abstract"
	
	Web Information Discovery Integrated Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science participated in the Blog track's opinion task in TREC-2006. The goal of opinion task is to 'uncover the public sentiment towards a given entity/target', which involves not only retrieving topically relevant blogs but also identifying those that contain opinions about the target. To further complicate the matter, the blog test collection contains considerable amount of noise, such as blogs with non-English content and non-blog content (e.g., advertisement, navigational text), which may misdirect retrieval systems. Based on our hypothesis that noise reduction (e.g., exclusion of non-English blogs, navigational text) will improve both on-topic and opinion retrieval performances, we explored various noise reduction approaches that can effectively eliminate the noise in blog data without inadvertently excluding valid content. After creating two separate indexes (with and without noise) to assess the noise reduction effect, we tackled the opinion blog retrieval task by breaking it down to two sequential subtasks: on-topic retrieval followed by opinion classification. Our opinion retrieval approach was to first apply traditional IR methods to retrieve on-topic blogs, and then boost the ranks of opinionated blogs based on opinion scores generated by opinion assessment methods. Our opinion module consists of Opinion Term Module, which identify opinions based on the frequency of opinion terms (i.e., terms that only occur frequently in opinion blogs), Rare Term Module, which uses uncommon/rare terms (e.g., “sooo good”) for opinion classification, IU Module, which uses IU (I and you) collocations, and Adjective-Verb Module, which uses computational linguistics' distribution similarity approach to learn the subjective language from training data
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYVZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYVZ06,
		author = {Kiduk Yang and Ning Yu and Alejandro Valerio and Hui Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2006 Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/indianau.blog.final.pdf},
		timestamp = {Wed, 29 Jun 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangYVZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC 2006 Blog Track

_Wei Zhang, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [uillinois.chicago.zhang](./blog/participants.md#uillinois.chicago.zhang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uillinois-chicago.blog.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uillinois-chicago.blog.final.pdf)
- :material-file-search: **Runs:** [uicsr](./blog/runs.md#uicsr) | [uicst](./blog/runs.md#uicst)

??? abstract "Abstract"
	
	We developed a two-step approach that finds relevant blog documents containing opinioned content for a given query topic. The first step, retrieval step, is to find documents relevant to the query. The second step, opinion identification step, is to find the documents containing opinions within the scope of the document set from the retrieval step. In the retrieval step, we try to improve the retrieval effectiveness by retrieving based on concepts, and doing query expansion using pseudo feedback, Wikipedia feedback and web feedback. In the opinion identification step, we train a sentence classifier using subjective sentences (opinioned) and objective sentences (non-opinioned), which are relevant to a query topic. This classifier labels each sentence in a given document as either subjective or objective. A document containing subjective sentences relating to the query is finally labeled as an opinioned relevant document (ORD). We tried two strategies to rank the ORDs that became two submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangY06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangY06,
		author = {Wei Zhang and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC} 2006 Blog Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uillinois-chicago.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangY06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCSC on REC 2006 Blog Opinion Mining

_Ethan Zhang, Yi Zhang_

- :fontawesome-solid-user-group: **Participant:** [ucalifornia.sc.zhang](./blog/participants.md#ucalifornia.sc.zhang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ucalifornia-sc.blog.pdf](http://trec.nist.gov/pubs/trec15/papers/ucalifornia-sc.blog.pdf)
- :material-file-search: **Runs:** [ucscauto](./blog/runs.md#ucscauto) | [ucscdesc](./blog/runs.md#ucscdesc) | [ucscrelfb](./blog/runs.md#ucscrelfb)

??? abstract "Abstract"
	
	The University of California Santa Cruz team submitted three runs for the TREC Blog Track opinion mining task. We developed a two stage retrieval system. We started with retrieving relevant documents from the corpus for each topic, and then ran each retrieved document through a classifier to estimate the probability that the document contains opinion expressions. The documents were ranked according to the product of the retrieval score and the estimated probability. The Lemur search engine, which is based on the language modeling approach, was used for retrieval. A Bayesian Logistic Regression classifier was trained using a noisy training data set from other domains, which include news articles, product reviews and movie reviews. All runs are automatic.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangZ06,
		author = {Ethan Zhang and Yi Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCSC} on {REC} 2006 Blog Opinion Mining},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ucalifornia-sc.blog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Question Answering 

#### Overview of the TREC 2006 Question Answering Track 99

_Hoa Trang Dang, Jimmy Lin, Diane Kelly_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/QA06.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/QA06.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC 2006 question answering (QA) track contained two tasks: the main task and the complex, interactive question answering (ciQA) task. As in 2005, the main task consisted of series of factoid, list, and “Other” questions organized around a set of targets; in contrast to previous years, the evaluation of factoid and list responses distinguished between answers that were globally correct (with respect to the document collection), and those that were only locally correct (with respect to the supporting document). The ciQA task provided a framework for participants to investigate interaction in the context of complex information needs, and was a blend of the TREC 2005 QA relationship task and the TREC 2005 HARD track. Multiple assessors were used to judge the importance of information nuggets used to evaluate the responses to ciQA and “Other” questions, resulting in an evaluation that is more stable and discriminative than one that uses only a single assessor to judge nugget importance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DangLK06.bib) "
	```
	@inproceedings{DBLP:conf/trec/DangLK06,
		author = {Hoa Trang Dang and Jimmy Lin and Diane Kelly},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2006 Question Answering Track 99},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/QA06.OVERVIEW.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DangLK06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Contextual Information and Assessor Characteristics in Complex Question  Answering

_Cindy Azzopardi, Leif Azzopardi, Mark Baillie, Ralf Bierig, Emma Nicol, Ian Ruthven, Scott Sweeney_

- :fontawesome-solid-user-group: **Participant:** [ustrathclyde.baillie](./qa/participants.md#ustrathclyde.baillie)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ustrathclyde.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ustrathclyde.qa.final.pdf)
- :material-file-search: **Runs:** [strath1](./qa/runs.md#strath1) | [strath3](./qa/runs.md#strath3) | [strath2](./qa/runs.md#strath2) | [strath4](./qa/runs.md#strath4)

??? abstract "Abstract"
	
	The ciqa track investigates the role of interaction in answering complex questions: questions that relate two or more entities by some specified relationship. In our submission to the first ciqa track we were interested in the interplay between groups of variables: variables describing the question creators, the questions asked and the presentation of answers to the questions. We used two interaction forms - html questionnaires completed before answer assessment - to gain contextual information from the answer assessors to better understand what factors influence assessors when judging retrieved answers to complex questions. Our results indicate the importance of understanding the assessor's personal relationship to the question - their existing topical knowledge for example - and also the presentation of the answers - contextual information about the answer to aid in the assessment of the answer.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AzzopardiABBNRS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/AzzopardiABBNRS06,
		author = {Cindy Azzopardi and Leif Azzopardi and Mark Baillie and Ralf Bierig and Emma Nicol and Ian Ruthven and Scott Sweeney},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Contextual Information and Assessor Characteristics in Complex Question Answering},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ustrathclyde.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AzzopardiABBNRS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2006 Q&A Factoid: TI Experience

_Satish Balantrapu, Monis Khan, Ayyappa Nagubandi_

- :fontawesome-solid-user-group: **Participant:** [trulyintelligent.satish](./qa/participants.md#trulyintelligent.satish)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/truly-intelligent.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/truly-intelligent.qa.final.pdf)
- :material-file-search: **Runs:** [TIQA200601](./qa/runs.md#tiqa200601)

??? abstract "Abstract"
	
	This is the first attempt of Artificial Intelligence Division of TrulyIntelligent Technologies Pvt. Ltd. at the TREC2006 Question Answering track. As any Question Answering (QA) system typically involves Question Analysis, Document Retrieval, Answer Extraction and Answer Ranking and this being our first attempt and with certain constraints of time and resources, we developed some modules of our QA system in line with already existing approaches, for example document retrieval, pattern based answer extraction and web boosting. But there are areas where we tried our ideas and got quite encouraging results particularly, Question Analysis, Constraint based Answer Extraction and Answer Ranking which are described in this paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalantrapuKN06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalantrapuKN06,
		author = {Satish Balantrapu and Monis Khan and Ayyappa Nagubandi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 Q{\&}A Factoid: {TI} Experience},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/truly-intelligent.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalantrapuKN06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The "La Sapienza" Question Answering System at TREC 2006

_Johan Bos_

- :fontawesome-solid-user-group: **Participant:** [uroma.bos](./qa/participants.md#uroma.bos)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/urome.bos.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/urome.bos.qa.final.pdf)
- :material-file-search: **Runs:** [Roma2006run1](./qa/runs.md#roma2006run1) | [Roma2006run2](./qa/runs.md#roma2006run2) | [Roma2006run3](./qa/runs.md#roma2006run3)

??? abstract "Abstract"
	
	This report describes the system developed at the University of Rome “La Sapienza” for the TREC-2006 question answering evaluation exercise. The backbone of this QA system is linguistically-principled: Combinatory Categorial Grammar is used to generate syntactic analyses of questions and potential answer snippets, and Discourse Representation Theory is employed as formalism to match the meanings of questions and answers. The key idea of the La Sapienza system is to use semantics to prune answer candidates, thereby exploiting lexical resources such as WordNet and Nom- Lex to facilitate the selection of answers. The system performed reasonably well at TREC-2006: in the per-series evaluation it performed slightly above the median accuracy score of all participating systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bos06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bos06,
		author = {Johan Bos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The "La Sapienza" Question Answering System at {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/urome.bos.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bos06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MITRE's Qanda at TREC 15

_John D. Burger_

- :fontawesome-solid-user-group: **Participant:** [mitre-corp.burger](./qa/participants.md#mitre-corp.burger)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/mitre.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/mitre.qa.final.pdf)
- :material-file-search: **Runs:** [MITRE2006C](./qa/runs.md#mitre2006c) | [MITRE2006A](./qa/runs.md#mitre2006a) | [MITRE2006D](./qa/runs.md#mitre2006d)

??? abstract "Abstract"
	
	Qanda is MITRE's TREC-style question answering system. In recent years, we have been able to apply only a small effort to the TREC QA activity, approximately six person-weeks this year. (Accordingly, much of this discussion is plagiarized from prior system descriptions.) We made a number of small improvements to the system this year, including expanding our use of Wordnet. The system's information retrieval wrapper now performs iterative query relaxation in order to improve document retrieval. We also experimented with an ad hoc means of “boosting” the maximum entropy model used to score candidate answers in order to improve its ranking ability.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Burger06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Burger06,
		author = {John D. Burger},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {MITRE's Qanda at {TREC} 15},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/mitre.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Burger06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LexiClone Lexical Cloning Systems

_Ilya S. Geller_

- :fontawesome-solid-user-group: **Participant:** [lexiclone.geller](./qa/participants.md#lexiclone.geller)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/lexiclone.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/lexiclone.qa.final.pdf)
- :material-file-search: **Runs:** [lexiclone06](./qa/runs.md#lexiclone06)

??? abstract "Abstract"
	
	In this article I substantiate my position that a human being is a point of accumulation - that is, an object. And based on this assumption I provide a foundation for my ontological justification of Differential Linguistics: I then introduce the understanding that 'becoming better and the best' is what motivates an object to movement (and change). Then I link this position with Egoism, and to achieve an understanding of what Egoism is I find it necessary to bring in the foundations I had previously elaborated for the New Mechanics and Differential Philosophy of Cynicism. Then I affirm that an object seeks information in order to 'become better and the best', and I show that information is required egoistically and that the finding of information is made possible by asking two classes of questions: factoid and definition questions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Geller06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Geller06,
		author = {Ilya S. Geller},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {LexiClone Lexical Cloning Systems},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/lexiclone.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Geller06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Sheffield's TREC 2006 Q&A Experiments

_Mark A. Greenwood, Mark Stevenson, Robert J. Gaizauskas_

- :fontawesome-solid-user-group: **Participant:** [usheffield.greenwood](./qa/participants.md#usheffield.greenwood)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/usheffield.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/usheffield.qa.final.pdf)
- :material-file-search: **Runs:** [shef06sem](./qa/runs.md#shef06sem) | [shef06ss](./qa/runs.md#shef06ss) | [shef06qal](./qa/runs.md#shef06qal)

??? abstract "Abstract"
	
	As a natural language processing group (NLP) our original approach to question answering was linguistically motivated culminating in the development of the QA-LaSIE system (Humphreys et al., 1999). In its original form QA-LaSIE would only propose answers which were linked via syntactic/semantic relations to the information missing from the question (for example “Who released the Internet worm?” is missing a person). While the answers proposed by the system were often correct, the system was frequently unable to suggest any answer. The next version of the system loosened the requirement for a link between question and answer which improved performance (Scott and Gaizauskas, 2000). There are still a number of open questions from the development of the QA-LaSIE system: does the use of parsing and discourse interpretation to determine links between questions and proposed answers result in better performance than simpler systems which adopt a shallower approach? Is it simply that the performance of our parser is below the level at which it could contribute to question answering? Are there questions which can only be answered using deep linguistic techniques? With the continued development of a second QA system at Sheffield which uses shallower techniques (Gaizauskas et al., 2005) we believe that we are now in a position to investigate these and related questions. Our entries to the 2006 TREC QA evaluation are designed to help us answer some of these questions and to investigate further the possible benefits of linguistic processing over shallower techniques. The remainder of this paper is organised as follows. Firstly the framework in which our systems are developed is described in section 2 along with the QA system components. Section 3 describes the configurations and aims of our evaluation runs. Section 4 discusses the official evaluation results of our submitted runs in relation to the research questions outlined above.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GreenwoodSG06.bib) "
	```
	@inproceedings{DBLP:conf/trec/GreenwoodSG06,
		author = {Mark A. Greenwood and Mark Stevenson and Robert J. Gaizauskas},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Sheffield's {TREC} 2006 Q{\&}A Experiments},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/usheffield.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GreenwoodSG06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Tianwang at TREC 2006 QA Track

_Jing He, Yuan Liu_

- :fontawesome-solid-user-group: **Participant:** [pekingu.yan](./qa/participants.md#pekingu.yan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/pekingu.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/pekingu.qa.final.pdf)
- :material-file-search: **Runs:** [TWQA0601](./qa/runs.md#twqa0601) | [TWQA0602](./qa/runs.md#twqa0602) | [TWQA0603](./qa/runs.md#twqa0603)

??? abstract "Abstract"
	
	This paper describes the architecture and implementation of Tianwang QA system2006, which works for the TREC QA Main task this year. The main improvement is: 1. add one well founded knowledge source from Web - Wikipedia, and employ some natural language processing technologies to extract high quality answers; 2. design and implement a new translation algorithm in query generation. The results show that fine organized knowledge source is effective in answering all three types of questions. And such query generation algorithm can be benefit from both Frequent Asked Questions on Web and past TREC QA data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeL06.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeL06,
		author = {Jing He and Yuan Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Tianwang at {TREC} 2006 {QA} Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/pekingu.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeL06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering with LCC's CHAUCER at TREC 2006

_Andrew Hickl, John Williams, Jeremy Bensley, Kirk Roberts, Ying Shi, Bryan Rink_

- :fontawesome-solid-user-group: **Participant:** [lcc.harabagiu](./qa/participants.md#lcc.harabagiu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/lcc-harabagiu.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/lcc-harabagiu.qa.final.pdf)
- :material-file-search: **Runs:** [LCCFerret](./qa/runs.md#lccferret)

??? abstract "Abstract"
	
	CHAUCER is a Q/A system developed for (a) combining several strategies for modeling the target of a series of questions and (b) optimizing the extraction of answers. Targets were modeled by (1) topic signatures; (2) semantic types; (3) lexico-semantic patterns; (4) frame dependencies; and (5) predictive questions. Several strategies for answer extraction were also tried. The best-performing strategy was based on the use of textual entailment.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HicklWBRSR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/HicklWBRSR06,
		author = {Andrew Hickl and John Williams and Jeremy Bensley and Kirk Roberts and Ying Shi and Bryan Rink},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering with LCC's {CHAUCER} at {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/lcc-harabagiu.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HicklWBRSR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Washington's UWclmaQA System

_Dan Jinguji, William D. Lewis, Efthimis N. Efthimiadis, Joshua Minor, Albert Bertram, Shauna Eggers, Joshua Johanson, Brian Nisonger, Ping Yu, Zhengbo Zhou_

- :fontawesome-solid-user-group: **Participant:** [uwash.lewis](./qa/participants.md#uwash.lewis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uwashington.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uwashington.qa.final.pdf)
- :material-file-search: **Runs:** [uwclma](./qa/runs.md#uwclma) | [uw574](./qa/runs.md#uw574)

??? abstract "Abstract"
	
	The University of Washington's U WCLM AQA is an open-architecture Question Answering system, built around open source tools unified into one system design using customized enhancements. The goal was to develop an end-to-end QA system that could be easily modified by switching out tools as needed. Central to the system is Lucene, which we use for document retrieval. Various other tools are used, such the GoogleAPI for web boosting, fnTBL Chunker for text chunking, Lingua::Stem for stemming, Lingpipe for Named Entity Recognition, etc. We also developed several in-house evaluation tools for gauging our progress at each major milestone (e.g., document classification, document retrieval, passage retrieval, etc.) and statistical classifiers were developed that we use for various classification tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JingujiLEMBEJNYZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/JingujiLEMBEJNYZ06,
		author = {Dan Jinguji and William D. Lewis and Efthimis N. Efthimiadis and Joshua Minor and Albert Bertram and Shauna Eggers and Joshua Johanson and Brian Nisonger and Ping Yu and Zhengbo Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Washington's UWclmaQA System},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uwashington.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JingujiLEMBEJNYZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments at the University of Edinburgh for the TREC 2006 QA  Track

_Michael Kaißer, Silke Scheible, Bonnie L. Webber_

- :fontawesome-solid-user-group: **Participant:** [uedinburgh.webber](./qa/participants.md#uedinburgh.webber)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uedinburgh.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uedinburgh.qa.final.pdf)
- :material-file-search: **Runs:** [ed06qar1](./qa/runs.md#ed06qar1) | [ed06qar2](./qa/runs.md#ed06qar2) | [ed06qar3](./qa/runs.md#ed06qar3)

??? abstract "Abstract"
	
	We describe experiments carried out at the University of Edinburgh for our TREC 2006 QA participation. Our main effort was to develop an approach to QA that is based on frame semantics. Two algorithms were implemented to this end, building on the lexical resources FrameNet, PropBank and VerbNet. The first algorithm uses the resources to generate potential answer templates to a given question, which are then used to pose exact, quoted queries to a web search engine and confirm which of the results contain an actual answer to the question. The second algorithm bases search queries on key words only, but it can recognize answers in a wider range of syntactic variants in its candidate sentence analysis stage. We discuss both approaches when applied to each of the resources and a combination of these. We also describe how-in a later step-the found answer candidates are mapped to the AQUAINT corpus and how we answered other questions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KaisserSW06.bib) "
	```
	@inproceedings{DBLP:conf/trec/KaisserSW06,
		author = {Michael Kai{\ss}er and Silke Scheible and Bonnie L. Webber},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments at the University of Edinburgh for the {TREC} 2006 {QA} Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uedinburgh.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KaisserSW06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering Experiments and Resources

_Boris Katz, Gregory Marton, Sue Felshin, Daniel Loreto, Ben Lu, Federico Mora, Özlem Uzuner, Michael McGraw-Herdeg, Natalie Cheung, Alexey Radul, Yuan Kui Shen, Yuan Luo, Gabriel Zaccak_

- :fontawesome-solid-user-group: **Participant:** [mit.katz](./qa/participants.md#mit.katz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/mit.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/mit.qa.final.pdf)
- :material-file-search: **Runs:** [csail1](./qa/runs.md#csail1) | [csaili1](./qa/runs.md#csaili1) | [csaili2](./qa/runs.md#csaili2) | [csail01](./qa/runs.md#csail01) | [csail03](./qa/runs.md#csail03) | [csail02](./qa/runs.md#csail02) | [csailif1](./qa/runs.md#csailif1) | [csailif2](./qa/runs.md#csailif2)

??? abstract "Abstract"
	
	MIT CSAIL's entries for the TREC Question Answering track (Voorhees, 2006) explored the effects of new document retrieval and duplicate removal strategies for 'list' and 'other' questions, established a baseline for other systems in the interactive task, and focused on question analysis and paraphrasing, rather than incorporation of external knowledge, in the factoid task. Many of the individual subsystems are largely unchanged from last year. We found that document retrieval strategy has an influence on performance in the different kinds of tasks later in the pipeline. Our other changes from last year did not immediately yield clear lessons. We present a question analysis data set and interannotator agreement indicators for the ciQA task that we hope will spur further evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KatzMFLLMUMCRSLZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/KatzMFLLMUMCRSLZ06,
		author = {Boris Katz and Gregory Marton and Sue Felshin and Daniel Loreto and Ben Lu and Federico Mora and {\"{O}}zlem Uzuner and Michael McGraw{-}Herdeg and Natalie Cheung and Alexey Radul and Yuan Kui Shen and Yuan Luo and Gabriel Zaccak},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering Experiments and Resources},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/mit.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KatzMFLLMUMCRSLZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DalTREC 2006 QA System Jellyfish: Regular Expressions Mark-and-Match  Approach to Question Answering

_Vlado Keselj, Tony Abou-Assaleh, Nick Cercone_

- :fontawesome-solid-user-group: **Participant:** [dalhousieu.keselj](./qa/participants.md#dalhousieu.keselj)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/dalhousieu.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/dalhousieu.qa.final.pdf)
- :material-file-search: **Runs:** [Dal06p](./qa/runs.md#dal06p) | [Dal06m](./qa/runs.md#dal06m) | [Dal06e](./qa/runs.md#dal06e)

??? abstract "Abstract"
	
	We present a question-answering system Jellyfish. Our approach is based on marking and matching steps that are implemented using the methodology of cascaded regular-expression rewriting. We present the system architecture and evaluate the system using the TREC 2004, 2005, and 2006 datasets. TREC 2004 was used as a training dataset, while TREC 2005 and TREC 2006 were used as testing dataset. The robustness of our approach is demonstrated in the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KeseljAC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/KeseljAC06,
		author = {Vlado Keselj and Tony Abou{-}Assaleh and Nick Cercone},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {DalTREC 2006 {QA} System Jellyfish: Regular Expressions Mark-and-Match Approach to Question Answering},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/dalhousieu.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KeseljAC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concordia University at the TREC 15 QA Track

_Leila Kosseim, Alex Beaudoin, Abolfazl Keighobadi Lamjiri, Majid Razmara_

- :fontawesome-solid-user-group: **Participant:** [concordiau.kosseim](./qa/participants.md#concordiau.kosseim)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/concordiau.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/concordiau.qa.final.pdf)
- :material-file-search: **Runs:** [QASCU1](./qa/runs.md#qascu1) | [QASCU2](./qa/runs.md#qascu2) | [QASCU3](./qa/runs.md#qascu3)

??? abstract "Abstract"
	
	In this paper, we describe the system we used for the TREC Question Answering Track. For factoid and list questions two different approaches were exploited: A redundancy-based approach using a modified version of aranea and a parse-tree based unifier. The modified version of aranea essentially uses Google snippets for extracting answers and then projects them to aquaint. The parse-tree based unifier is a linguistic-based approach that chunks candidate sentences syntactically and uses a heuristic measure to compute the similarity of each chunk in a candidate to its counterpart in the question. To answer other types of questions, our system extracts from Wikipedia articles a list of interest-marking terms related to the topic and uses them to extract and score sentences from the aquaint document collection using various interest-marking triggers. We submitted 3 runs using different variations of the system. In the factoid run, the average of our 3 runs is 0.202, for the list, we achieved an average of 0.084, and for the “Other”, we achieved an average F-score of 0.192.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KosseimBKR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/KosseimBKR06,
		author = {Leila Kosseim and Alex Beaudoin and Abolfazl Keighobadi Lamjiri and Majid Razmara},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concordia University at the {TREC} 15 {QA} Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/concordiau.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KosseimBKR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC ciQA 2006

_Giridhar Kumaran, James Allan_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./qa/participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umass.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umass.qa.final.pdf)
- :material-file-search: **Runs:** [UMASSauto1](./qa/runs.md#umassauto1) | [UMASSauto2](./qa/runs.md#umassauto2) | [UMAS1](./qa/runs.md#umas1) | [UMASSi2](./qa/runs.md#umassi2) | [UMASSi1](./qa/runs.md#umassi1)

??? abstract "Abstract"
	
	The characteristics of the ciQA Track namely the short templated queries and the scope for user interaction were the motivating factors for our interest in participating in the track. Templated queries represent a new paradigm of information-seeking more suited for specialized tasks. While work has been done in document retrieval for templated queries as part of the Global Autonomous Language Exploitation1 (GALE) program, the retrieval of snippets of information in lieu of documents was an interesting challenge. We also utilized the opportunity to try a suite of minimally interactive techniques, some of which helped and some did not. We believe we have a reasonable understanding of why some approaches worked while other failed, and contend that more experimentation and analysis is necessary to tease out various interaction effects between the suite of approaches we tried.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KumaranA06.bib) "
	```
	@inproceedings{DBLP:conf/trec/KumaranA06,
		author = {Giridhar Kumaran and James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} ciQA 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umass.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KumaranA06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Semantic Relations with World Knowledge for Question Answering

_Ka Kan Lo, Wai Lam_

- :fontawesome-solid-user-group: **Participant:** [chineseu-hongkong.kan](./qa/participants.md#chineseu-hongkong.kan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/cuhk.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/cuhk.qa.final.pdf)
- :material-file-search: **Runs:** [cuhkqaepisto](./qa/runs.md#cuhkqaepisto)

??? abstract "Abstract"
	
	Two research directions are to be explored in realizing our group's TREC QA system in 2006. The first one is to investigate the possibilities of applying linguistically sophisticated grammatical framework in tackling the real-world natural language processing task such as question answering. The other is to exploit the possible world's entities and relations as described in online encyclopedia in adding redundancy and hidden relations as those contained in the TREC corpus where the entities and relations are only implicitly mentioned and related. Our focus is on the factoid and list question as these two types of questions benefit greatly from our proposed method. We do include an experimental component in handling the ”other” question type.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LoL06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LoL06,
		author = {Ka Kan Lo and Wai Lam},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Semantic Relations with World Knowledge for Question Answering},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/cuhk.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LoL06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Temporally-Enhanced PowerAnswer in TREC 2006

_Dan I. Moldovan, Mitchell Bowden, Marta Tatu_

- :fontawesome-solid-user-group: **Participant:** [lcc.moldovan](./qa/participants.md#lcc.moldovan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/lcc-moldovan.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/lcc-moldovan.qa.final.pdf)
- :material-file-search: **Runs:** [lccPA06](./qa/runs.md#lccpa06)

??? abstract "Abstract"
	
	This paper reports on Language Computer Corporation's participation in the Question Answering track at TREC 2006. An overview of the PowerAnswer 3 question answering system and a description of new features added to meet the challenges of this year's evaluation are provided. Emphasis is given to temporal constraints in questions and how this affected the outcome of the systems in the task. LCC's results in the evaluation are presented at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoldovanBT06.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoldovanBT06,
		author = {Dan I. Moldovan and Mitchell Bowden and Marta Tatu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Temporally-Enhanced PowerAnswer in {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/lcc-moldovan.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoldovanBT06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AnswerFinder at TREC 2006

_Diego Mollá, Menno van Zaanen, Luiz Augusto Sangoi Pizzato_

- :fontawesome-solid-user-group: **Participant:** [macquarieu.molla](./qa/participants.md#macquarieu.molla)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/macquarieu.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/macquarieu.qa.final.pdf)
- :material-file-search: **Runs:** [lf10w10g5](./qa/runs.md#lf10w10g5) | [lf10w10g5l5](./qa/runs.md#lf10w10g5l5) | [lf10w20g5l5](./qa/runs.md#lf10w20g5l5)

??? abstract "Abstract"
	
	This article describes the AnswerFinder question answering system and its participation in the TREC 2006 question answering competition. This year there have been several improvements in the AnswerFinder system, although most of them in the implementation sphere. The actual functionality used this year is almost exactly the same as last year, but many bugs are fixed and the efficiency of the system has improved much. This allows for more extensive parameter tuning. Here we will also present an error analysis of the current AnswerFinder system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MollaZP06.bib) "
	```
	@inproceedings{DBLP:conf/trec/MollaZP06,
		author = {Diego Moll{\'{a}} and Menno van Zaanen and Luiz Augusto Sangoi Pizzato},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {AnswerFinder at {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/macquarieu.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MollaZP06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Reconstructing DIOGENE: ITC-irst at TREC 2006

_Matteo Negri, Milen Kouylekov, Bernardo Magnini, Bonaventura Coppola_

- :fontawesome-solid-user-group: **Participant:** [itc-irst.negri](./qa/participants.md#itc-irst.negri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/itc-irst.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/itc-irst.qa.final.pdf)
- :material-file-search: **Runs:** [irstqa06](./qa/runs.md#irstqa06)

??? abstract "Abstract"
	
	Our participation in the TREC 2006 QA task is the first step on the way of developing a new and improved DIOGENE system. The leading principles of this re-engineering activity are: i) to create a modular architecture, based on a pipeline of modules which share common I/O formats, open to the insertion/substitution of new components; ii) to allow for the capability of configuring the settings of the different modules with external configuration files; iii) to provide the capability of performing fine-grained evaluation cycles over the individual processing modules which compose a QA system. Another long-term objective of our work on QA, is to make the core components of the system freely available to the QA community for research purposes. This paper overviews the work done up to date to achieve these objectives, focusing on the description of a prototype module designed to handle the anaphoric questions often contained into TREC QA series. Preliminar evaluation results of the new module are presented, together with those achieved by DIOGENE at TREC 2006.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NegriKMC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/NegriKMC06,
		author = {Matteo Negri and Milen Kouylekov and Bernardo Magnini and Bonaventura Coppola},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Reconstructing {DIOGENE:} ITC-irst at {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/itc-irst.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NegriKMC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2006 at Maryland: Blog, Enterprise, Legal and QA Tracks

_Douglas W. Oard, Tamer Elsayed, Jianqiang Wang, Yejun Wu, Pengyi Zhang, Eileen G. Abels, Jimmy Lin, Dagobert Soergel_

- :fontawesome-solid-user-group: **Participant:** [umaryland.oard](./qa/participants.md#umaryland.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf)
- :material-file-search: **Runs:** [UMDM1pre](./qa/runs.md#umdm1pre) | [UMDM1](./qa/runs.md#umdm1) | [UMDA1pre](./qa/runs.md#umda1pre) | [UMDA1](./qa/runs.md#umda1) | [UMDA1post](./qa/runs.md#umda1post) | [UMDM1post](./qa/runs.md#umdm1post)

??? abstract "Abstract"
	
	In TREC 2006, teams from the University of Maryland participated in the Blog track, the Expert Search task of the Enterprise track, the Complex Interactive Question Answering task of the Question Answering track, and the Legal track. This paper reports our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardEWWZALS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardEWWZALS06,
		author = {Douglas W. Oard and Tamer Elsayed and Jianqiang Wang and Yejun Wu and Pengyi Zhang and Eileen G. Abels and Jimmy Lin and Dagobert Soergel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 at Maryland: Blog, Enterprise, Legal and {QA} Tracks},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/OardEWWZALS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Ephyra QA System at TREC 2006

_Nico Schlaefer, P. Gieselman, Guido Sautter_

- :fontawesome-solid-user-group: **Participant:** [ukarlsruhe-cmu.schlaefer](./qa/participants.md#ukarlsruhe-cmu.schlaefer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ukarlsruhe-cmu.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ukarlsruhe-cmu.qa.final.pdf)
- :material-file-search: **Runs:** [ISL1](./qa/runs.md#isl1) | [ISL2](./qa/runs.md#isl2) | [ISL3](./qa/runs.md#isl3)

??? abstract "Abstract"
	
	The Ephyra QA system has been developed as a flexible open-domain QA framework. This framework allows us to combine several techniques for question analysis and answer extraction and to incorporate multiple knowledge bases to best fit the requirements of the TREC QA track, in which we participated this year for the first time. The techniques used include pattern learning and matching, answer type analysis and redundancy elimination through filters. In this paper, we give an overview of the Ephyra system as used within TREC 2006 and analyze the system's performance in the QA track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchlaeferGS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchlaeferGS06,
		author = {Nico Schlaefer and P. Gieselman and Guido Sautter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Ephyra {QA} System at {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ukarlsruhe-cmu.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchlaeferGS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QACTIS Enhancements in TREC QA 2006

_Patrick Schone, Gary M. Ciany, R. Cutts, Paul McNamee, James Mayfield, Tom Smith_

- :fontawesome-solid-user-group: **Participant:** [nsa.schone](./qa/participants.md#nsa.schone)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/dod.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/dod.qa.final.pdf)
- :material-file-search: **Runs:** [QACTIS06A](./qa/runs.md#qactis06a) | [QACTIS06B](./qa/runs.md#qactis06b) | [QACTIS06C](./qa/runs.md#qactis06c)

??? abstract "Abstract"
	
	The QACTIS system has been tested in previous years at the TREC Question Answering Evaluations. This paper describes new enhancements to the system specific to TREC-2006, including basic improvements and thresholding experiments, filtered and Internet-supported pseudo-relevance feedback for information retrieval, and emerging statistics-driven question-answering. For contrast, we also compare our TREC-2006 system performance to that of our top systems from TREC-2004 and TREC-2005 applied to this year's data. Lastly, we analyze evaluator-declared unsupportedness of factoids and nugget decisions of “other” questions to understand major negative changes in performance for these categories over last year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchoneCCMMS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchoneCCMMS06,
		author = {Patrick Schone and Gary M. Ciany and R. Cutts and Paul McNamee and James Mayfield and Tom Smith},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{QACTIS} Enhancements in {TREC} {QA} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/dod.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchoneCCMMS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Alyssa System at TREC 2006: A Statistically-Inspired Question  Answering System

_Dan Shen, Jochen L. Leidner, Andreas Merkel, Dietrich Klakow_

- :fontawesome-solid-user-group: **Participant:** [saarlandu.leidner](./qa/participants.md#saarlandu.leidner)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/saarlandu.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/saarlandu.qa.final.pdf)
- :material-file-search: **Runs:** [lsv2006b](./qa/runs.md#lsv2006b) | [lsv2006c](./qa/runs.md#lsv2006c) | [lsv2006a](./qa/runs.md#lsv2006a)

??? abstract "Abstract"
	
	We present our new statistically-inspired open-domain Q&A research system that allows to carry out a wide range of experiments easily and flexibly by modifying a central file containing an experimental “recipe” that controls the activation and parameter selection of a range of widely-used and custom-built components. Based on this, we report our experiments for the TREC 2006 question answering track, where we used a cascade of LM-based document retrieval, LM-based sentence extraction, MaxEnt-based answer extraction over a dependency relation representation followed by a fusion process that uses linear interpolation to integrate evidence from various data streams to detect answers to factoid questions more accurately than the median of all participants.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShenLMK06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShenLMK06,
		author = {Dan Shen and Jochen L. Leidner and Andreas Merkel and Dietrich Klakow},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Alyssa System at {TREC} 2006: {A} Statistically-Inspired Question Answering System},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/saarlandu.qa.final.pdf},
		timestamp = {Mon, 17 Apr 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ShenLMK06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering Using the DLT System at TREC 2006

_Richard F. E. Sutcliffe, Kieran White, Igal Gabbay, Michael Mulcahy_

- :fontawesome-solid-user-group: **Participant:** [ulimerick.sutcliffe](./qa/participants.md#ulimerick.sutcliffe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ulimerick.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ulimerick.qa.final.pdf)
- :material-file-search: **Runs:** [DLT06QA01](./qa/runs.md#dlt06qa01) | [DLT06QA02](./qa/runs.md#dlt06qa02)

??? abstract "Abstract"
	
	This article summarises our participation in the Question Answering (QA) Track at TREC 2006. Section 2 outlines the architecture of our system. Section 3 describes the changes made for this year. Section 4 summarises the results of our submitted runs while Section 5 presents conclusions and proposes further steps.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SutcliffeWGM06.bib) "
	```
	@inproceedings{DBLP:conf/trec/SutcliffeWGM06,
		author = {Richard F. E. Sutcliffe and Kieran White and Igal Gabbay and Michael Mulcahy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering Using the {DLT} System at {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ulimerick.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SutcliffeWGM06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering by Diggery at TREC 2006

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [tomlinson.stan](./qa/participants.md#tomlinson.stan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/tomlinson.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/tomlinson.qa.final.pdf)
- :material-file-search: **Runs:** [TREC06ST01](./qa/runs.md#trec06st01)

??? abstract "Abstract"
	
	Diggery is a research and software project, investigating the extraction of concepts from well-written documents, with the idea of automating factoid search. The project is in its early to middle phases, and all information presented herein should be taken in light that this research is based on young software using new algorithms. In January 2006, after significant tuning, the software could answer a few simple questions from small texts. Six months later, in July 2006, the first real exercise of the software on a non-trivially sized corpora was made for the TREC QA submission, and the software answered a few questions correctly. For this submission, only factoid questions were attempted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson06a.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson06a,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Question Answering by Diggery at {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/tomlinson.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson06a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Identifying Relationships Between Entities in Text for Complex Interactive  Question Answering Task

_Olga Vechtomova, Murat Karamuftuoglu_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo-clarke](./qa/participants.md#uwaterloo-clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uwaterloo.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uwaterloo.qa.final.pdf)
- :material-file-search: **Runs:** [UWATCIQA1](./qa/runs.md#uwatciqa1) | [UWATCIQA2](./qa/runs.md#uwatciqa2) | [UWAT1](./qa/runs.md#uwat1) | [UWATCIQA3](./qa/runs.md#uwatciqa3) | [UWATCIQA4](./qa/runs.md#uwatciqa4)

??? abstract "Abstract"
	
	In this paper we describe our participation in the Complex Interactive Question Answering (ciQA) task of the QA track. We investigated the use of lexical cohesive ties (called lexical bonds) between sentences containing different question entities in finding information about relationships between these entities. We also investigated the role of clarification forms in assisting the system in finding answers to complex questions. The rest of the paper is organised as follows: in section 2 we present our approach to calculating lexical bonds between sentences containing different entities, section 3 contains the detailed description of our systems, in section 4 we present the results, and section 5 contains discussions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VechtomovaK06.bib) "
	```
	@inproceedings{DBLP:conf/trec/VechtomovaK06,
		author = {Olga Vechtomova and Murat Karamuftuoglu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Identifying Relationships Between Entities in Text for Complex Interactive Question Answering Task},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uwaterloo.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VechtomovaK06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2006 Question Answering Experiments at Tokyo Institute of Technology

_Edward W. D. Whittaker, Josef R. Novak, Pierre Chatain, Sadaoki Furui_

- :fontawesome-solid-user-group: **Participant:** [tokyo-it.whittaker](./qa/participants.md#tokyo-it.whittaker)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/tokyo-it.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/tokyo-it.qa.final.pdf)
- :material-file-search: **Runs:** [asked06a](./qa/runs.md#asked06a) | [asked06b](./qa/runs.md#asked06b) | [asked06c](./qa/runs.md#asked06c)

??? abstract "Abstract"
	
	In this paper we describe Tokyo Institute of Technology's speech group's second attempt at the TREC2006 question answering (QA) track. Keeping the same theoretical QA model as for the TREC2005 task this year we investigated combinations of variations of models focusing once again on the factoid QA task. An experimental run combining translated answers from separate English, French and Spanish systems proved inconclusive. However, our best combination of all component models gave us a factoid performance of 25.1% (placing us 9th and well above the median of the 30 participating systems of 18.6%) and an overall performance including the results from the list and other question tasks of 11.6% (which was somewhat below the median of 13.4%).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WhittakerNCF06.bib) "
	```
	@inproceedings{DBLP:conf/trec/WhittakerNCF06,
		author = {Edward W. D. Whittaker and Josef R. Novak and Pierre Chatain and Sadaoki Furui},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 Question Answering Experiments at Tokyo Institute of Technology},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/tokyo-it.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WhittakerNCF06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ILQUA at TREC 2006

_Min Wu, Tomek Strzalkowski_

- :fontawesome-solid-user-group: **Participant:** [ualbany.min](./qa/participants.md#ualbany.min)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ualbany.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ualbany.qa.final.pdf)
- :material-file-search: **Runs:** [ILQUA1](./qa/runs.md#ilqua1)

??? abstract "Abstract"
	
	This year, we made changes to the pas- sage/sentence retrieval component of ILQUA in handling factoid and list questions. All the other components remain same. ILQUA is an IE-driven QA system. To answer “Factoid” and “List” questions, we apply our answer extraction methods on NE-tagged passages or sentences. The answer extraction methods adopted here are surface text pattern matching, n-gram proximity search, and syntactic dependency matching. Although surface text pattern matching has been applied in some previous TREC QA systems, the patterns used in ILQUA are better since they are automatically generated by a supervised learning system and represented in a format of regular expressions which contain multiple question terms. In addition to surface pattern matching, we also adopt n-gram proximity search and syntactic dependency matching. N-grams of question terms are matched around every named entity in the candidate sentences or passages and a list of named entities are generated as answer candidate. These named entities then go through a multi-level syntactic dependency matching component until a final answer is generated. To answer “Other” questions, we parsed the answer sentences of “Other” questions in previous main task and built syntactic patterns combined with semantic features. These patterns are later applied to the parsed candidate sentences to extract answers of “Other” questions. Figure 1 shows the diagram of the ILQUA architecture.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuS06,
		author = {Min Wu and Tomek Strzalkowski},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ILQUA} at {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ualbany.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### InsunQA06 on QA Track of TREC 2006

_Yuming Zhao, Zhiming Xu, Peng Li, Yi Guan_

- :fontawesome-solid-user-group: **Participant:** [harbin.zhao](./qa/participants.md#harbin.zhao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/hit.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/hit.qa.final.pdf)
- :material-file-search: **Runs:** [InsunQA06](./qa/runs.md#insunqa06)

??? abstract "Abstract"
	
	This is the second time that our group takes part in the QA track of TREC. We developed a question-answering system, named InsunQA06, based on our Insun05QA system, and with InsunQA06 we participated in the Main Task, which submitted answers to three types of questions: factoid questions, list questions and others questions. The structure of InsunQA06 is similar with the structure of Insun05QA. Towards Insun05QA, the main difference of InsunQA06 is that new methods are developed and used in answer extraction module, for factoid and “others” questions. And external knowledge such as knowledge from Internet plays more important role in answer extraction. Besides that, we accomplished our documents retrieval module based on Indri, instead of SMART in InsunQA06. In Section 2, the structure of our InsunQA06 system will be describe, the details of the new methods that we adopted to process the factoid, and “others” questions will separately be described in Section 3, and our results in TREC2006 will be presented in Section 4.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoXLG06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoXLG06,
		author = {Yuming Zhao and Zhiming Xu and Peng Li and Yi Guan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {InsunQA06 on {QA} Track of {TREC} 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/hit.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoXLG06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDUQA on TREC 2006 QA Track

_Yaqian Zhou, Xiaofeng Yuan, Junkuo Cao, Xuanjing Huang, Lide Wu_

- :fontawesome-solid-user-group: **Participant:** [fudan.wu](./qa/participants.md#fudan.wu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/fudan-zhou.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/fudan-zhou.qa.final.pdf)
- :material-file-search: **Runs:** [FDUQAT15B](./qa/runs.md#fduqat15b) | [FDUQAT15A](./qa/runs.md#fduqat15a) | [FDUQAT15C](./qa/runs.md#fduqat15c)

??? abstract "Abstract"
	
	In this year's QA Track, we participant in the main task and do not take part in the ciQA task. The main task is essentially the same as the single task from 2004, in that the test set consists of a set of question series where each series asks for information regarding a particular target. In order to better answer the questions in the series, we try to improve our anaphora resolution within question series. For factoid questions, we use the system that submits the RUN-A in TREC 2005[Wu et al. 2005]. Therefore we won't describe the factoid system in this paper. For list questions, we get a lot of improvements, the most important of which are answer type classification, document searching, answer ranking and answer filtering. For definition question, we still focus on utilizing the existing definitions in the Web knowledge bases. And also applied the method of relative terms extraction to extract reliable information associated with target for getting web definition directly by question target is becoming a bottleneck. In the following, Section 2 will describe question series anaphora resolution. Section 3,and 4 will describe our algorithms for list and definition questions separately. Section 5 will present our results in TREC 2006.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouYCHW06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouYCHW06,
		author = {Yaqian Zhou and Xiaofeng Yuan and Junkuo Cao and Xuanjing Huang and Lide Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDUQA} on {TREC} 2006 {QA} Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/fudan-zhou.qa.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhouYCHW06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Legal 

#### TREC 2006 Legal Track Overview

_Jason R. Baron, David D. Lewis, Douglas W. Oard_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/LEGAL06.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/LEGAL06.OVERVIEW.pdf)
??? abstract "Abstract"
	
	This paper describes the first year of a new TREC track focused on “e-discovery” of business records and other materials. A large collection of scanned documents produced by multiple real world discovery requests was adopted as the basis for the test collection. Topic statements were developed using a process representative of current practice in e-discovery applications, with both Boolean and natural language queries being supported. Relevance judgments were performed by personnel who had received professional training, and often considerable experience, in review of similar materials for this task. Six research teams and one manual searcher submitted a total of 33 retrieved sets for each topic. These were pooled and a portion assessed to support evaluation of both the retrieved sets themselves and for future use of the collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BaronLO06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BaronLO06,
		author = {Jason R. Baron and David D. Lewis and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 Legal Track Overview},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/LEGAL06.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BaronLO06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2006 at Maryland: Blog, Enterprise, Legal and QA Tracks

_Douglas W. Oard, Tamer Elsayed, Jianqiang Wang, Yejun Wu, Pengyi Zhang, Eileen G. Abels, Jimmy Lin, Dagobert Soergel_

- :fontawesome-solid-user-group: **Participant:** [umaryland.oard](./legal/participants.md#umaryland.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf)
- :material-file-search: **Runs:** [UmdBoolAuto](./legal/runs.md#umdboolauto) | [UmdComb](./legal/runs.md#umdcomb) | [UmdBase](./legal/runs.md#umdbase) | [UmdBool](./legal/runs.md#umdbool)

??? abstract "Abstract"
	
	In TREC 2006, teams from the University of Maryland participated in the Blog track, the Expert Search task of the Enterprise track, the Complex Interactive Question Answering task of the Question Answering track, and the Legal track. This paper reports our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardEWWZALS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardEWWZALS06,
		author = {Douglas W. Oard and Tamer Elsayed and Jianqiang Wang and Yejun Wu and Pengyi Zhang and Eileen G. Abels and Jimmy Lin and Dagobert Soergel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 at Maryland: Blog, Enterprise, Legal and {QA} Tracks},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umd.blog.ent.legal.qa.final.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/OardEWWZALS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with the Negotiated Boolean Queries of the TREC 2006  Legal Discovery Track

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird.tomlinson](./legal/participants.md#hummingbird.tomlinson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/opentext.legal.final.pdf](http://trec.nist.gov/pubs/trec15/papers/opentext.legal.final.pdf)
- :material-file-search: **Runs:** [humL06tvo](./legal/runs.md#huml06tvo) | [humL06dvo](./legal/runs.md#huml06dvo) | [humL06t0](./legal/runs.md#huml06t0) | [humL06t](./legal/runs.md#huml06t) | [humL06tv](./legal/runs.md#huml06tv) | [humL06tvz](./legal/runs.md#huml06tvz) | [humL06tve](./legal/runs.md#huml06tve) | [humL06tvc](./legal/runs.md#huml06tvc)

??? abstract "Abstract"
	
	We analyze the results of several experimental runs submitted to the Legal Discovery and Terabyte Tracks of TREC 2006. In the Legal Track, the final negotiated boolean queries produced higher mean scores in average precision and Precision@10 than a corresponding vector run of the same query terms, but the vector run usually recalled more relevant items by rank 5000, and on average the boolean query matched less than half of the relevant items. We also report the impact of query negotiation, metadata and natural language vs. keywords. We find that robust metrics (which expose the downside of blind feedback techniques) are inappropriate for legal discovery because they favour duplicate filtering. We also report the results of depth probe experiments (depth 9000 in the Legal Track and depth 5000 in the Terabyte Track) which provide a lower-bound estimate for the number of unjudged relevant items in each track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson06,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with the Negotiated Boolean Queries of the {TREC} 2006 Legal Discovery Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/opentext.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2006: Legal Track

_Miao Wen, Xiangji Huang_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./legal/participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/yorku.legal.pdf](http://trec.nist.gov/pubs/trec15/papers/yorku.legal.pdf)
- :material-file-search: **Runs:** [york06la01](./legal/runs.md#york06la01) | [york06la02](./legal/runs.md#york06la02)

??? abstract "Abstract"
	
	York University participated in the legal track this year. For this track, we developed an Okapi-based Legal Search Engine (LSE) v1.0. Our experiments mainly focused on evaluating the effect of a probabilistic text retrieval model on the legal domain. In order to address the special problems in legal text retrieval, new automatic feedback methods and term weighting methods are proposed and tested.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WenH06.bib) "
	```
	@inproceedings{DBLP:conf/trec/WenH06,
		author = {Miao Wen and Xiangji Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2006: Legal Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/yorku.legal.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WenH06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with Query Expansion at TREC 2006 Legal Track

_Feng C. Zhao, Yugyung Lee, Deep Medhi_

- :fontawesome-solid-user-group: **Participant:** [umkc.zhao](./legal/participants.md#umkc.zhao)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umissouri-kc.legal.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umissouri-kc.legal.final.pdf)
- :material-file-search: **Runs:** [UMKCQE100](./legal/runs.md#umkcqe100) | [UMKCSN](./legal/runs.md#umkcsn) | [UMKCSW](./legal/runs.md#umkcsw) | [UMKCB](./legal/runs.md#umkcb) | [UMKCQE25](./legal/runs.md#umkcqe25) | [UMKCB2](./legal/runs.md#umkcb2) | [UMKCBQE10](./legal/runs.md#umkcbqe10) | [UMKCBQE5](./legal/runs.md#umkcbqe5)

??? abstract "Abstract"
	
	This paper describes the UMKC TREC 2006 Legal Track experiments. We focus on a single technique that uses cooccurrence based thesaurus to expand queries. Our results indicate this technique is effective even towards the enormous vocabulary size in the IIT CDIP collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoLM06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoLM06,
		author = {Feng C. Zhao and Yugyung Lee and Deep Medhi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with Query Expansion at {TREC} 2006 Legal Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umissouri-kc.legal.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoLM06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

