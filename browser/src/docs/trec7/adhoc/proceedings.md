# Proceedings - Adhoc 1998 

#### Readware Text Analysis and Retrieval in TREC 7

_Tom Adi, O. K. Ewell, Patricia Adi_

- :fontawesome-solid-user-group: **Participant:** [miti](./participants.md#miti)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/t7miti2.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/t7miti2.pdf.gz)
- :material-file-search: **Runs:** [t7miti1](./runs.md#t7miti1)

??? abstract "Abstract"
	
	This paper describes Management Information Technologies, Inc.'s (MITi) first involvement in the TREC program. We limited our participation to manual adhoc although our multilingual algorithms can be used for automatic query generation and refinement and are suited for most TREC tasks. We used our commercially available text analysis and retrieval Readware technology to perform the manual adhoc task of finding the documents relevant to fifty specified topics in a pool of more than half a million documents. Readware uses concepts (groups of related words), superconcepts (groups of concepts), Readware query elements (query building blocks) and document subjects to form queries. This is complemented by word search, phrase search and Boolean logic. One MITi analyst performed the task. She formulated an average of 18 queries per topic. The queries were derived intuitively from topic specifications (title, description and narrative). First, a baseline pool of documents was identified for every topic using a few simple queries. Then the analyst queried the baselines using as often as possible Readware query elements related to elements of the topic specification. On average, few hits were returned per query. The analyst also had the advantage of seeing the exact responsive text spots highlighted in every hit document. Queries were adjusted and expanded using information from the neighborhood of the highlighted hit spots. There was no intrinsic ranking of hits. All hits were full semantic matches. The hits were ranked higher after the fact if the queries contained more items. In the 'Best Manual Adhoc' figure of the TREC 7 evaluation results, MITi's graph is above all other participants' graphs at most points.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AdiEA98.bib) "
	```
	@inproceedings{DBLP:conf/trec/AdiEA98,
		author = {Tom Adi and O. K. Ewell and Patricia Adi},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Readware Text Analysis and Retrieval in {TREC} 7},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {400--403},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/t7miti2.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AdiEA98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-7

_James Allan, James P. Callan, Mark Sanderson, Jinxi Xu, Steven Wegmann_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/umass-trec7.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/umass-trec7.pdf.gz)
- :material-file-search: **Runs:** [INQ501](./runs.md#inq501) | [INQ502](./runs.md#inq502) | [INQ503](./runs.md#inq503)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in only four of the tracks that were part of the TREC-T workshop. We worked on ad-hoc retrieval, filtering, VLC, and the SDR track. This report covers the work done on each track successively. We start with a discussion of IR tools that were broadly applied in our work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCSXW98.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCSXW98,
		author = {James Allan and James P. Callan and Mark Sanderson and Jinxi Xu and Steven Wegmann},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} and {TREC-7}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {148--163},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/umass-trec7.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AllanCSXW98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at TREC7

_Mohand Boughanem, Taoufiq Dkaki, Josiane Mothe, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/IRITtrec7.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/IRITtrec7.pdf.gz)
- :material-file-search: **Runs:** [MerAdRbtnd](./runs.md#meradrbtnd) | [MerTetAdtnd](./runs.md#mertetadtnd) | [MerAdRbtd](./runs.md#meradrbtd)

??? abstract "Abstract"
	
	The tests we performed for TREC-7 were focused on automatic ad hoc and filtering tasks. With regard to the automatic ad hoc task we assessed two query modification strategies. Both were based on blind relevance feedback processes. The first one carried on with the TREC6 tests: new parameter values of the relevance backpropagation formulas have been tuned. On the other hand, we proposed a new query modification strategy that uses a text mining approach. Three runs were sent. We sent two runs for the relevance backpropagation strategy: one used long topics (titles, descriptions and narratives) and the other one used titles and descriptions. We sent one run for the text mining strategy using long topics. With regard to the filtering task, we sent runs in batch filtering and routing using both relevance backpropagation and gradient neural backpropagation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemDMS98.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemDMS98,
		author = {Mohand Boughanem and Taoufiq Dkaki and Josiane Mothe and Chantal Soul{\'{e}}{-}Dupuy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure at {TREC7}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {355--360},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/IRITtrec7.pdf.gz},
		timestamp = {Mon, 07 Oct 2019 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemDMS98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SPIDER Retrieval System at TREC7

_Martin Braschler, Bojidar Mateev, Elke Mittendorf, Peter Schäuble, Martin Wechsler_

- :fontawesome-solid-user-group: **Participant:** [ETH](./participants.md#eth)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/ETHTREC7.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/ETHTREC7.pdf.gz)
- :material-file-search: **Runs:** [ETHAC0](./runs.md#ethac0) | [ETHAR0](./runs.md#ethar0) | [ETHAB0](./runs.md#ethab0)

??? abstract "Abstract"
	
	This year the Zurich team participated in two tracks: the automatic-adhoc track and the crosslingual track. For the adhoc task we focused on improving retrieval for short queries. We pursued two aims. First, we investigated weighting functions for short queries explicitely without any kind of automatic query expansion. Second we developed rules that automatically decide for which queries automatic expansion works fine and for which it does not. For the cross-language track, we approached the problem of retrieving documents from a multilingual document pool containing documents in all TREC CLIR languages. Our method uses individual runs for different language combinations, followed by merging their results into one final ranked list. We obtained good results without sophisticated machine translation or costly linguistic resources.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BraschlerMMSW98.bib) "
	```
	@inproceedings{DBLP:conf/trec/BraschlerMMSW98,
		author = {Martin Braschler and Bojidar Mateev and Elke Mittendorf and Peter Sch{\"{a}}uble and Martin Wechsler},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SPIDER} Retrieval System at {TREC7}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {446--454},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/ETHTREC7.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BraschlerMMSW98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SMART High Precision: TREC 7

_Chris Buckley, Mandar Mitra, Janet A. Walz, Claire Cardie_

- :fontawesome-solid-user-group: **Participant:** [Cornell/Sabir](./participants.md#cornell/sabir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/cornell.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/cornell.pdf.gz)
- :material-file-search: **Runs:** [Cor7A1clt](./runs.md#cor7a1clt) | [Cor7A2rrd](./runs.md#cor7a2rrd) | [Cor7A3rrf](./runs.md#cor7a3rrf)

??? abstract "Abstract"
	
	The Smart information retrieval project emphasizes completely automatic approaches to the understanding and retrieval of large quantities of text. We continue our work in TREC 7, concentrating on high precision retrieval. In particular, we present an in-depth analysis of our High-Precision Track results, including offering evaluation approaches and measures for time dependent evaluation. We participated in the Query Track, making initial efforts at analyzing query variability, one of the major obstacles for improving retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleyMWC98.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleyMWC98,
		author = {Chris Buckley and Mandar Mitra and Janet A. Walz and Claire Cardie},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SMART} High Precision: {TREC} 7},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {230--243},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/cornell.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BuckleyMWC98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Term Selection for Automatic Query Expansion

_Claudio Carpineto, Renato de Mori, Giovanni Romano_

- :fontawesome-solid-user-group: **Participant:** [bordoni](./participants.md#bordoni)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/fub98.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/fub98.pdf.gz)
- :material-file-search: **Runs:** [fub98a](./runs.md#fub98a) | [fub98b](./runs.md#fub98b)

??? abstract "Abstract"
	
	Techniques for query expansion from top retrieved documents have been recently used by many groups at TREC, often on a purely empirical ground. In this paper we present a novel method for ranking and weighting expansion terms. The method is based on the concept of relative entropy, or Kullback-Lieber distance, developed in Information Theory, from which we derive a computationally simple and theoretically justified formula to assign scores to candidate expansion terms. This method has been incorporated into a comprehensive prototype ranking system, tested in the ad hoc track of TREC-7. The system's overall performance was comparable to median performance of TREC-7 participants, wich is quite good considering that we are new to TREC and that we used unsophisticated indexing and weighting techniques. More focused experiments showed that the use of an information-theoretic component for query expansion significantly improved mean retrieval effectiveness over unexpanded query, yielding performance gains as high as 14% (for non interpolated average precision), while a per-query analysis suggested that queries that are neither too difficult nor too easy can be more easily improved upon.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarpinetoMR98.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarpinetoMR98,
		author = {Claudio Carpineto and Renato de Mori and Giovanni Romano},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Information Term Selection for Automatic Query Expansion},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {308--314},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/fub98.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CarpinetoMR98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Deriving Very Short Queries for High Precision and Recall (MultiText  Experiments for TREC-7)

_Gordon V. Cormack, Christopher R. Palmer, Michael Van Biesbrouck, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/mt7.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/mt7.pdf.gz)
- :material-file-search: **Runs:** [uwmt7a2](./runs.md#uwmt7a2) | [uwmt7a1](./runs.md#uwmt7a1) | [uwmt7a0](./runs.md#uwmt7a0)

??? abstract "Abstract"
	
	The main aim of the MultiText experiments for TREC-T was to derive very short queries that would yield high precision and recall, using a hybrid of manual and automatic processes. Identical queries were formulated for adhoc and VLC runs. A query set derived automatically from the topic title words, with an average of 2.84 terms per query, achieved a reasonable but unexceptional average precision for the adhoc task and a median precision @20 for the 100 GB VLC task. However, these short queries achieved very fast retrieval times - less than 1 second per query over 100 GB using four inexpensive PCs. Two further query sets were derived using post-processing of the results of interactive searching on the adhoc corpus. Queries comprising a single conjunction, averaging 1.86 terms, achieved high precision on both adhoc and VLC tasks, and achieved faster retrieval times than the title-word queries. Compound queries averaging 6.42 terms achieved precision values competitive with the best runs, and retrieval times of 1.51 seconds per query on the 100 GB VLC corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackPBC98.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackPBC98,
		author = {Gordon V. Cormack and Christopher R. Palmer and Michael Van Biesbrouck and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Deriving Very Short Queries for High Precision and Recall (MultiText Experiments for {TREC-7)}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {68--79},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/mt7.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CormackPBC98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Audio-Indexing For Broadcast News

_Satya Dharanipragada, Martin Franz, Salim Roukos_

- :fontawesome-solid-user-group: **Participant:** [ibm-franz](./participants.md#ibm-franz)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/ibmy_t7_1.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/ibmy_t7_1.pdf.gz)
- :material-file-search: **Runs:** [ibms98a](./runs.md#ibms98a) | [ibms98b](./runs.md#ibms98b) | [ibms98c](./runs.md#ibms98c)

??? abstract "Abstract"
	
	In this paper we describe the IBM Audio-Indexing System which is a combination of a large vocabulary speech recognizer and a text-based information retrieval system. Our speech recognizer was used to produce the baseline transcripts for the NIST SDR97 evaluation. We report the performance of the system on the SDR-97 'known item retrieval' task and on a more pertinent TREC-style Audio-Indexing task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DharanipragadaFR98.bib) "
	```
	@inproceedings{DBLP:conf/trec/DharanipragadaFR98,
		author = {Satya Dharanipragada and Martin Franz and Salim Roukos},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Audio-Indexing For Broadcast News},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {63--67},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/ibmy_t7_1.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DharanipragadaFR98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cluster-Based Adaptive and Batch Filtering

_David Eichmann, Miguel E. Ruiz, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [iowa](./participants.md#iowa)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/Iowa.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/Iowa.pdf.gz)
- :material-file-search: **Runs:** [iowacuhk1](./runs.md#iowacuhk1) | [iowacuhk2](./runs.md#iowacuhk2)

??? abstract "Abstract"
	
	Information filtering is increasingly critical to knowledge workers drowning in a growing flood of byte streams [6, 8, 9]. Our interest in the filtering track for TREC-7 grew out of work originally designed for information retrieval on the Web, using both 'traditional' search engine [5] and agent-based techniques [6, 7]. In particular, the work by Cutter, et. al. in clustering [3, 4] has great appeal in the potential for synergistic interaction between user and retrieval system. Our efforts for TREC-7 included two distinct filtering architectures, as well as a more traditional approach to the adhoc track (which used SMART 113). The filtering work was done using TRECcer - our Java-based clustering environment - alone for adaptive filtering and a combination of TRECcer and SMART for batch filtering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannRS98.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannRS98,
		author = {David Eichmann and Miguel E. Ruiz and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Cluster-Based Adaptive and Batch Filtering},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {211--220},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/Iowa.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/EichmannRS98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Effectiveness of Clustering in Ad-Hoc Retrieval

_David A. Evans, Alison Huettner, Xiang Tong, Peter Jansen, Jeffrey Bennett_

- :fontawesome-solid-user-group: **Participant:** [clarit](./participants.md#clarit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/CLARIT_ad_hoc.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/CLARIT_ad_hoc.pdf.gz)
- :material-file-search: **Runs:** [CLARIT98COMB](./runs.md#clarit98comb) | [CLARIT98CLUS](./runs.md#clarit98clus) | [CLARIT98RANK](./runs.md#clarit98rank)

??? abstract "Abstract"
	
	In this paper, we describe the experiment underlying the CLARITECH entries in the TREC-7 Ad Hoc Retrieval Track. Based on past results, we have come to regard accurate, selective relevance feedback as the dominant factor in effective retrieval. We hypothesized that a clustered rather than a ranked presentation of documents would facilitate judgments of document relevance, allowing a user to judge more documents accurately in a given period of time. This in turn should yield better feedback performance and ultimately better retrieval results. We found that users were indeed able to find more relevant documents in the same time period when results were clustered rather than ranked. Retrieval results from the cluster run were better than results from the ranked run, and those from a combined run were better still. The difference between the ranked and combined runs was statistically significant for both recall and average precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EvansHTJB98.bib) "
	```
	@inproceedings{DBLP:conf/trec/EvansHTJB98,
		author = {David A. Evans and Alison Huettner and Xiang Tong and Peter Jansen and Jeffrey Bennett},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Effectiveness of Clustering in Ad-Hoc Retrieval},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {90--95},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/CLARIT_ad_hoc.pdf.gz},
		timestamp = {Thu, 05 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/EvansHTJB98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIS at TREC-7

_Kiduk Yang, Kelly Maglaughlin, Lokman I. Meho, Robert G. Sumner Jr._

- :fontawesome-solid-user-group: **Participant:** [UNC-N](./participants.md#unc-n)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/tr7unc1.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/tr7unc1.pdf.gz)
- :material-file-search: **Runs:** [unc7aal1](./runs.md#unc7aal1) | [unc7aal2](./runs.md#unc7aal2)

??? abstract "Abstract"
	
	In our TREC-5 ad-hoc experiment, we tested two relevance feedback models, an adaptive linear model and a probabilistic model, using massive feedback query expansion (Sumner & Shaw, 1997). For our TREC-6 interactive experiment, we developed an interactive retrieval system called IRIS (Information Retrieval Interactive System'), which implemented modified versions of the feedback models with a three-valued scale of relevance and reduced feedback query expansion (Sumner, Yang, Akers & Shaw, 1998). The goal of the IRIS design was to provide users with ample opportunities to interact with the system throughout the search process. For example, users could supplement the initial query by choosing from a list of statistically significant, two-word collocations, or add and delete query terms as well as change their weights at each search iteration. Unfortunately, it was difficult to tell how much effect each IRIS feature had on the retrieval outcome due to such factors as strong searcher effect and major differences between the experimental and control systems. In our TREC-7 interactive experiment, we attempted to isolate the effect of a given system feature by making the experimental and control systems identical, save for the feature we were studying. In one interactive experiment, the difference between the experimental and control systems was the display and modification capability of term weights. In another experiment, the difference was relevance feedback by passage versus document. For the TREC-7 ad-hoc task, we wanted to examine the effectiveness of relevance feedback using a subcollection in order to lay the groundwork for future participation in the Very Large Corpus experiment. Though the pre-test results showed the retrieval effectiveness of a subcollection approach to be competitive with a whole collection approach, we were not able to execute the subcollection retrieval in the actual ad-hoc experiment due to hardware problems. Instead, our ad-hoc experiment consisted of a simple initial retrieval run and a pseudo-relevance feedback run using the top 5 documents as relevant and the 100* document as non-relevant. Though the precision was high in the top few documents, the ad-hoc results were below average by TREC measures as expected. In the interactive experiment, the passage feedback results were better than the document feedback results, and the results of the simple interface system that did not display query term weights were better than that of the more complex interface system that displayed query term weights and allowed users to change these weights. Overall interactive results were about average among participants.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangMMS98.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangMMS98,
		author = {Kiduk Yang and Kelly Maglaughlin and Lokman I. Meho and Robert G. Sumner Jr.},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{IRIS} at {TREC-7}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {489--500},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/tr7unc1.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangMMS98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Natural Language Information Retrieval: TREC-7 Report

_Tomek Strzalkowski, Gees C. Stein, G. Bowden Wise, Jose Perez Carballo, Pasi Tapanainen, Timo Järvinen, Atro Voutilainen, Jussi Karlgren_

- :fontawesome-solid-user-group: **Participant:** [GE](./participants.md#ge)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/ge.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/ge.pdf.gz)
- :material-file-search: **Runs:** [gersh1](./runs.md#gersh1) | [gersh2](./runs.md#gersh2) | [gersh3](./runs.md#gersh3)

??? abstract "Abstract"
	
	The GE/Rutgers/SICS/Helsinki team has performed runs in the main ad-hoc task. All submissions are NLP-assisted retrieval. We used two retrieval engines: SMART and InQuery built into the stream model architecture where each stream represents an alternative text indexing method. The processing of TREC data was performed at Helsinki using the commercial Functional Dependency Grammar (FDG) text processing toolkit. Six linguistic streams have been produced, described below. Processed text streams were sent via ftp to Rutgers for indexing. Indexing was done using Inquery system. Additionally, 4 steams produced by GE NLToolset for TREC-6 were reused in SMART indexing. Adhoc topics were processed at GE using both automatic and manual topic expansion. We used the interactive Query Expansion Tool to expand topics with automatically generated summaries of top 30 documents retrieved by the original topic. Manual intervention was restricted to accept/reject decisions on summaries. We observed time limit of 10 minutes per topic. Automatic topics expansion was done by replacing human summary selection by an automatic procedure, which accepted only the summaries that obtained sufficiently high scores. Two sets of expanded topics (automatic and manual) were sent to Helsinki for NL processing, and then on to Rutgers for retrieval. Rankings were obtained from each stream index and then merged using a combined strategy developed at GE and SICS.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StrzalkowskiSWCTJVK98.bib) "
	```
	@inproceedings{DBLP:conf/trec/StrzalkowskiSWCTJVK98,
		author = {Tomek Strzalkowski and Gees C. Stein and G. Bowden Wise and Jose Perez Carballo and Pasi Tapanainen and Timo J{\"{a}}rvinen and Atro Voutilainen and Jussi Karlgren},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Natural Language Information Retrieval: {TREC-7} Report},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {164--173},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/ge.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/StrzalkowskiSWCTJVK98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AT&T at TREC-7

_Amit Singhal, John Choi, Donald Hindle, David D. Lewis, Fernando C. N. Pereira_

- :fontawesome-solid-user-group: **Participant:** [ATT](./participants.md#att)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/att.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/att.pdf.gz)
- :material-file-search: **Runs:** [att98atc](./runs.md#att98atc) | [att98atdc](./runs.md#att98atdc) | [att98atde](./runs.md#att98atde)

??? abstract "Abstract"
	
	This year AT&T participated in the ad-hoc task and the Filtering, SDR, and VLC tracks. Most of our effort for TREC-T was concentrated on SDR and VLC tracks. On the filtering track, we tested a preliminary version of a text classification toolkit that we have been developing over the last year. In the ad-hoc task, we introduce a new tf-factor in our term weighting scheme and use a simplified retrieval algorithm. The same weighting scheme and algorithm are used in the SDR and the VLC tracks. The results from the SDR track show that retrieval from automatic transcriptions of speech is quite competitive with doing retrieval from human transcriptions. Our experiments indicate that document expansion can be used to further improve retrieval from automatic transcripts. Results of filtering track are in line with our expectations given the early developmental stage of our classification software. The results of VLC track do not support our hypothesis that retrieval lists from a distributed search can be effectively merged using only the initial part of the documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinghalCHLP98.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinghalCHLP98,
		author = {Amit Singhal and John Choi and Donald Hindle and David D. Lewis and Fernando C. N. Pereira},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {AT{\&}T at {TREC-7}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {186--198},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/att.pdf.gz},
		timestamp = {Fri, 30 Aug 2019 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SinghalCHLP98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Two-Stage Retrieval Model for the TREC-7 Ad Hoc Task

_Dong-Ho Shin, Byoung-Tak Zhang_

- :fontawesome-solid-user-group: **Participant:** [Seoul](./participants.md#seoul)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/ScaiTrec7.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/ScaiTrec7.pdf.gz)
- :material-file-search: **Runs:** [ScaiTrec7](./runs.md#scaitrec7)

??? abstract "Abstract"
	
	A two-stage model for ad hoc text retrieval is proposed in which recall and precision are maximized sequentially. The first stage employs query expansion methods using WordNet and on a modified stemming algorithm. The second stage incorporates a term proximity-based scoring function and a prototype-based reranking method. The effectiveness of the two-stage retrieval model is tested on the TREC-7 ad hoc text data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShinZ98.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShinZ98,
		author = {Dong{-}Ho Shin and Byoung{-}Tak Zhang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {A Two-Stage Retrieval Model for the {TREC-7} Ad Hoc Task},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {439--445},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/ScaiTrec7.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ShinZ98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Document Retrieval Using The MPS Information Server (A Report  on the TREC-7 Experiment)

_François Schiettecatte_

- :fontawesome-solid-user-group: **Participant:** [FS](./participants.md#fs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/fsconsult7.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/fsconsult7.pdf.gz)
- :material-file-search: **Runs:** [fsclt7m](./runs.md#fsclt7m) | [fsclt7a](./runs.md#fsclt7a)

??? abstract "Abstract"
	
	This paper summarizes the results of the work conducted by FS Consulting, Inc. as part of the Seventh Text Retrieval Experiment Conference (TREC-7). We participated in two components of TREC: (1) Category C, running the Ad Hoc experiments, producing two sets of official results (fsclt7m and fsclt7a) and (2) the Very Large Collection (VLC) track, running the entire experiment, producing the required official results as well as a set of unofficial results. Our long-term research interest is in building information retrieval systems that help users find information to solve real-world problems. Our TREC runs employ two models: for the manual experiments, we have developed a model information systems end-user described more fully in section 5. For the automatic experiments, we use a title-word retrieval model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Schiettecatte98.bib) "
	```
	@inproceedings{DBLP:conf/trec/Schiettecatte98,
		author = {Fran{\c{c}}ois Schiettecatte},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Document Retrieval Using The {MPS} Information Server {(A} Report on the {TREC-7} Experiment)},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {315--326},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/fsconsult7.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Schiettecatte98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DSIR: the First TREC-7 Attempt

_Arnon Rungsawang_

- :fontawesome-solid-user-group: **Participant:** [Kasetsart](./participants.md#kasetsart)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/kasetsart.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/kasetsart.pdf.gz)
- :material-file-search: **Runs:** [dsir07a01](./runs.md#dsir07a01) | [dsir07a02](./runs.md#dsir07a02)

??? abstract "Abstract"
	
	This paper describes our first large-scale retrieval attempt in TREC-7 using DSIR. DSIR is a vector space based retrieval system in which semantic similarity between words, documents and queries, is interpreted in terms of geometric proximity of vectors in a multi-dimensional space. A co-occurrence matrix computed directly from the collection is used to build the underlying semantic space. We have implemented DSIR on a cluster of low-cost PC Pentium-class machines, and chosen the PVM message-passing library to manage our distributed DSIR version. Although our first adhoc retrieval results are quite poor in terms of recall-precision measure, we believe that more work and experiments have to be explored in order to obtain more promising retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Rungsawang98.bib) "
	```
	@inproceedings{DBLP:conf/trec/Rungsawang98,
		author = {Arnon Rungsawang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{DSIR:} the First {TREC-7} Attempt},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {366--372},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/kasetsart.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Rungsawang98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Feature Reduction for Information Retrieval

_Stefan M. Rüger_

- :fontawesome-solid-user-group: **Participant:** [imperial](./participants.md#imperial)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/ic98san3.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/ic98san3.pdf.gz)
- :material-file-search: **Runs:** [ic98san4](./runs.md#ic98san4) | [ic98san3](./runs.md#ic98san3)

??? abstract "Abstract"
	
	Our experiments for the ad hoc task were centred around the question how to create a document surrogate that still contains enough information to be used for a high-quality, efficient retrieval. In the first step we drop all the function words and all the auxiliary words that although having a proper meaning merely help to communicate about the topic without being relevant to the topic. We apply part-of-speech analysis in order to retain the nouns and adjectives of a document. Standard term and document frequency analysis is used to compute a weight factor for each of the remaining words. In a second step, we plan to set the relevant words into a relation that conveys a part of the meaning. Like in vector space models, both topic and document would be represented in this keyword-relation form and a suitable metric would quantify the relevance of a document to a topic. At this stage of our research, no relations are stored in document surrogates. The automatic processed topic descriptions, however, include some very crude relation analysis that, eg, transfers 'relevant documents describe cases of drink-driving outside France' to 'drink driving outside France' and hence, knowing about the connotation of '... outside...' a negative weight factor for the occurrence of drink-driving and France. It is planned for future work to analyse relations more and more with statistical models and with trained probabilistic models and less with linguistic analysis. For now, the purpose of our experiments is assessing the performance of the above very simple model of pure feature reduction without relations, without training/learning weights without sophisticated recall procedures, without inverted document files and without a proper document retrieval system. It might be interesting to see which effect feature reduction algorithms have in other, sophisticatedly tuned systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Ruger98.bib) "
	```
	@inproceedings{DBLP:conf/trec/Ruger98,
		author = {Stefan M. R{\"{u}}ger},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Feature Reduction for Information Retrieval},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {351--354},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/ic98san3.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Ruger98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi at TREC-7: Automatic Ad Hoc, Filtering, VLC and Interactive

_Stephen E. Robertson, Steve Walker, Micheline Hancock-Beaulieu_

- :fontawesome-solid-user-group: **Participant:** [okapi](./participants.md#okapi)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/okapi_proc.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/okapi_proc.pdf.gz)
- :material-file-search: **Runs:** [ok7ax](./runs.md#ok7ax) | [ok7am](./runs.md#ok7am) | [ok7as](./runs.md#ok7as)

??? abstract "Abstract"
	
	Three runs were submitted: medium (title and description), short (title only) and a run which was a combination of a long run (title, description and narrative) with the medium and short runs. The average precision of the last mentioned run was higher by several percent than any other submitted run, but another participant' recently noticed an impossibly high score for one topic in the short run. This led to the discovery that due to a mistake in the indexing procedures part of the SUBJECT field of the LA Times documents had been indexed. Use of this field was explicitly forbidden in the guidelines [1] for the ad hoc track. The official runs were repeated against a corrected index, and the corrected results are reported below, average precisions being reduced by about 2-4%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonWB98.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonWB98,
		author = {Stephen E. Robertson and Steve Walker and Micheline Hancock{-}Beaulieu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Okapi at {TREC-7:} Automatic Ad Hoc, Filtering, {VLC} and Interactive},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {199--210},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/okapi_proc.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonWB98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Query Processing at LEXIS-NEXIS for TREC-7

_Ashwin G. Rao, Timothy Humphrey, Afsar Parhizgar, Christi Wilson, Daniel Pliske_

- :fontawesome-solid-user-group: **Participant:** [LN](./participants.md#ln)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/lntrec7.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/lntrec7.pdf.gz)
- :material-file-search: **Runs:** [LNaTit7](./runs.md#lnatit7) | [LNaTitDesc7](./runs.md#lnatitdesc7) | [LNmanual7](./runs.md#lnmanual7)

??? abstract "Abstract"
	
	The purpose of this report is to provide an overview of LEXIS-NEXIS' entries to the TREC-7 competition. The report will describe the experiments we conducted, the results we obtained, and our future research directions. The report is divided into three sections. The first section describes the experimental setup and gives a brief account of some of the research activities that led to the TREC-7 entries. The second section explains how the techniques developed during our research culminated into the three entries that were submitted. Our experiences with these new techniques gave us insight into new research directions for improving query processing. In the third section, we conclude by sharing these ideas with the reader.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RaoHPWP98.bib) "
	```
	@inproceedings{DBLP:conf/trec/RaoHPWP98,
		author = {Ashwin G. Rao and Timothy Humphrey and Afsar Parhizgar and Christi Wilson and Daniel Pliske},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments in Query Processing at {LEXIS-NEXIS} for {TREC-7}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {390--399},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/lntrec7.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RaoHPWP98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-7 Experiments at the University of Maryland

_Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [UMD](./participants.md#umd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/umdfinal.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/umdfinal.pdf.gz)
- :material-file-search: **Runs:** [umd98a1](./runs.md#umd98a1) | [umd98a2](./runs.md#umd98a2)

??? abstract "Abstract"
	
	The University of Maryland participated in three TREC-7 tasks: ad hoc retrieval, cross-language retrieval, and spoken document retrieval. The principal focus of the work was evaluation of merging techniques for cross-language text retrieval from mixed language collections. The results show that biasing the merging strategy in favor of documents in the query language can be helpful. Ad hoc and spoken document retrieval results are also presented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Oard98.bib) "
	```
	@inproceedings{DBLP:conf/trec/Oard98,
		author = {Douglas W. Oard},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-7} Experiments at the University of Maryland},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {477--481},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/umdfinal.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Oard98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 7 Ad Hoc, Speech, and Interactive tracks at MDS/CSIRO

_Michael Fuller, Marcin Kaszkiel, Dongki Kim, Corinna Ng, John Robertson, Ross Wilkinson, Mingfang Wu, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/mds.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/mds.pdf.gz)
- :material-file-search: **Runs:** [mds98td](./runs.md#mds98td) | [mds98t](./runs.md#mds98t) | [mds98t2](./runs.md#mds98t2)

??? abstract "Abstract"
	
	For the 1998 round of TREC, the MDS group, long-term participants at the conference, jointly participated with newcomers CSIRO. Together we completed runs in three tracks: ad-hoc, interactive, and speech.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FullerKKNRWWZ98.bib) "
	```
	@inproceedings{DBLP:conf/trec/FullerKKNRWWZ98,
		author = {Michael Fuller and Marcin Kaszkiel and Dongki Kim and Corinna Ng and John Robertson and Ross Wilkinson and Mingfang Wu and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC} 7 Ad Hoc, Speech, and Interactive tracks at {MDS/CSIRO}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {404--413},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/mds.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FullerKKNRWWZ98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad hoc and Multilingual Information Retrieval at IBM

_Martin Franz, J. Scott McCarley, Salim Roukos_

- :fontawesome-solid-user-group: **Participant:** [ibm-franz](./participants.md#ibm-franz)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/ibmy_t7_2.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/ibmy_t7_2.pdf.gz)
- :material-file-search: **Runs:** [ibms98a](./runs.md#ibms98a) | [ibms98b](./runs.md#ibms98b) | [ibms98c](./runs.md#ibms98c)

??? abstract "Abstract"
	
	IBM participated in two tracks at TREC-7: ad hoc and cross-language. In the adhoc task we contrasted the performance of two different query expansion techniques: local context analysis and probabilistic model. Two themes characterize IBM's participation in the CLIR track at TREC-7. The first is the use of statistical methods. In order to use the document translation approach, we built a fast (translation time within an order of magnitude of the indexing time) French= English translation model trained from parallel corpora. We also trained German→French and Italian→French translation models entirely from comparable corpora. The unique characteristic of the work described here is that all bilingual resources and translation models were learned automatically from corpora (parallel and comparable.) The other theme is that the widely varying quality and availability of bilingual resources means that language pairs must be treated separately. We will describe methods for using one language as a pivot language in order to decrease the number pairs, as well as methods for merging the results from several retrievals.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FranzMR98.bib) "
	```
	@inproceedings{DBLP:conf/trec/FranzMR98,
		author = {Martin Franz and J. Scott McCarley and Salim Roukos},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ad hoc and Multilingual Information Retrieval at {IBM}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {104--115},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/ibmy_t7_2.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FranzMR98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Text Retrieval via Semantic Forests: TREC7

_Gregory D. Henderson, Patrick Schone, Thomas H. Crystal_

- :fontawesome-solid-user-group: **Participant:** [nsa](./participants.md#nsa)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/nsa-rev.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/nsa-rev.pdf.gz)
- :material-file-search: **Runs:** [nsasgrp3](./runs.md#nsasgrp3) | [nsasgrp4](./runs.md#nsasgrp4)

??? abstract "Abstract"
	
	In the second year of the use of Semantic Forests in TREC, we have raised our 30-document average precision in the automatic Ad Hoc task to 27% from 19% last year. We also contributed a significant number of unique relevant documents to the judgement pool [3]. Our mean average precisions on the SDR task are roughly the median performance for that task [4]. The Semantic Forests algorithm was originally developed by Schone and Nelson [1] for labeling topics in text and transcribed speech. Semantic Forests uses an electronic dictionary to make a tree for each word in a text document. The root of the tree is the word from the document, the first branches are the words in the definition of the root word, the next branches are the words in the definitions of the words in the first branches, and so on. The words in the trees are tagged by part of speech and given weights based on statistics gathered during training. Finally, the trees are merged into a scored list of words. The premise is that words in common between trees will be reinforced and represent 'topics' present in the document. With minor modifications, queries are treated as documents. Seven major changes were made in developing this year's system from last year's. (1) A number of pre-processing steps which were performed last year (such as identifying multi-word units) were incorporated into Semantic Forests. (2) A part of speech tagger was added, allowing Semantic Forests to use this additional information. (3) Semantic Forests distinguishes between queries and documents this year, since our experiments indicated they needed to be treated differently. (4) Only the first three letters of words which do not occur in the dictionary are retained, instead of the entire word. (5) A parameter directs Semantic Forests to break each document into segments containing at most a set number of words, typically 500. 6) The algorithms used by Semantic Forests to assign and combine word weights have been improved. (7) Quasi-relevance feedback was implemented and evaluated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HendersonSC98.bib) "
	```
	@inproceedings{DBLP:conf/trec/HendersonSC98,
		author = {Gregory D. Henderson and Patrick Schone and Thomas H. Crystal},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Text Retrieval via Semantic Forests: {TREC7}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {516--527},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/nsa-rev.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HendersonSC98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Twenty-One at TREC7: Ad-hoc and Cross-Language Track

_Djoerd Hiemstra, Wessel Kraaij_

- :fontawesome-solid-user-group: **Participant:** [TwentyOne](./participants.md#twentyone)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/twentyone.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/twentyone.pdf.gz)
- :material-file-search: **Runs:** [tno7cbm25](./runs.md#tno7cbm25) | [tno7tw4](./runs.md#tno7tw4) | [tno7exp1](./runs.md#tno7exp1)

??? abstract "Abstract"
	
	This paper describes the official runs of the Twenty-One group for TREC-7. The Twenty-One group participated in the ad-hoc and the cross-language track and made the following accom-plishments: We developed a new weighting algorithm, which outperforms the popular Cornell version of BM25 on the ad-hoc collection. For the CLIR task we developed a fuzzy matching algorithm to recover from missing translations and spelling variants of proper names. Also for CLIR we investigated translation strategies that make extensive use of information from our dictionaries by identifying preferred translations, main translations and synonym translations, by defining weights of possible translations and by experimenting with probabilistic boolean matching strategies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HiemstraK98.bib) "
	```
	@inproceedings{DBLP:conf/trec/HiemstraK98,
		author = {Djoerd Hiemstra and Wessel Kraaij},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Twenty-One at {TREC7:} Ad-hoc and Cross-Language Track},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {174--185},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/twentyone.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HiemstraK98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-7 Experiments: Query Expansion Method Based on Word Contribution

_Keiichiro Hoashi, Kazunori Matsumoto, Naomi Inoue, Kazuo Hashimoto_

- :fontawesome-solid-user-group: **Participant:** [KDD](./participants.md#kdd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/kddproc3.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/kddproc3.pdf.gz)
- :material-file-search: **Runs:** [KD71010s](./runs.md#kd71010s) | [KD70000](./runs.md#kd70000) | [KD71010q](./runs.md#kd71010q)

??? abstract "Abstract"
	
	This is KDD R&D Laboratories' first participation in TREC. In this participation, we focused on experiments on a novel method of query expansion. The query expansion method described in this paper is based on a measure we call 'word contribution'. Word contribution is a measure which expresses the influence of a word to the similarity between the query and a document. From our data, we figured that words which have highly negative contribution can be considered as to being expressive of the characteristics of the data (query or document) in which they exist. We proposed extracting such words from documents highly similar to a query, and adding them to the original query to generate an expanded query. We made experiments to evaluate this method, and reported the results in this paper. We submitted 3 official ad hoc runs (KD70000, KD71010q, KD71010s) to TREC-7. However, the data we used for these runs were generated by a buggy morphological analysis program, which we consider a serious cause for our bad results. Since the official submission, we have fixed these bugs, and reconstructured our data. The results described in this paper are based on these new data, and some experiments made after the TREC-T con-terence.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HoashiMIH98.bib) "
	```
	@inproceedings{DBLP:conf/trec/HoashiMIH98,
		author = {Keiichiro Hoashi and Kazunori Matsumoto and Naomi Inoue and Kazuo Hashimoto},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-7} Experiments: Query Expansion Method Based on Word Contribution},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {373--381},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/kddproc3.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HoashiMIH98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-7 Ad-Hoc, High Precision and Filtering Experiments using PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, M. Chan, Norbert Dinstl, Colleen Cool_

- :fontawesome-solid-user-group: **Participant:** [CUNY](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/queens.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/queens.pdf.gz)
- :material-file-search: **Runs:** [pirc8At](./runs.md#pirc8at) | [pirc8Ad](./runs.md#pirc8ad) | [pirc8Aa2](./runs.md#pirc8aa2)

??? abstract "Abstract"
	
	In TREC-7, we participated in the main task of automatic ad-hoc retrieval as well as the high precision and filtering tracks. For ad-hoc, three experiments were done with query types of short (title section of a topic), medium (description section) and long (all sections) lengths. We used a sequence of five methods to handle the short and medium length queries. For long queries we employed a re-ranking method based on evidence from matching query phrases in document windows in both stages of a 2-stage retrieval. Results are well above median. For high precision track, we employed our interactive PIRCS system for the first time. In adaptive filtering, we concentrate on dynamically varying the retrieval status value threshold for deciding selection and during the course of filtering. Query weights were trained but expansion was not done. We also submitted results for batch filtering and standard routing based on methods evolved from previous TREC experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGCDC98.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGCDC98,
		author = {Kui{-}Lam Kwok and Laszlo Grunfeld and M. Chan and Norbert Dinstl and Colleen Cool},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-7} Ad-Hoc, High Precision and Filtering Experiments using {PIRCS}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {287--297},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/queens.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KwokGCDC98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ACSys TREC-7 Experiments

_David Hawking, Nick Craswell, Paul B. Thistlewaite_

- :fontawesome-solid-user-group: **Participant:** [ANU](./participants.md#anu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/acsys.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/acsys.pdf.gz)
- :material-file-search: **Runs:** [acsys7mi](./runs.md#acsys7mi) | [acsys7al](./runs.md#acsys7al) | [acsys7as](./runs.md#acsys7as)

??? abstract "Abstract"
	
	Experiments relating to TREC-7 Ad Hoc, HP and VLC tasks are described and results reported. Minor refinements of last year's Ad Hoc methods do not appear to have resulted in worthwile improvements in performance. However, larger benefits were gained from automatic feedback than last year and concept scoring was very beneficial in the Manual Ad Hoc category. In the Automatic Ad Hoc category title-only performance seems to have suffered more severely than long-topic from a number of lexical scanning shortcomings and from an excessive stopword list. The HP track was used to validate the usibility of the combination of PADRE and the Quokka GUI. In the VLC track, the 100 gigabyte collection was indexed in under eight hours and moderately effective queries were processed in less than two seconds.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingCT98a.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingCT98a,
		author = {David Hawking and Nick Craswell and Paul B. Thistlewaite},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ACSys {TREC-7} Experiments},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {244--257},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/acsys.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HawkingCT98a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fujitsu Laboratories TREC7 Report

_Isao Namba, Nobuyuki Igata, Hisayuki Horai, Kiyoshi Nitta, Kunio Matsui_

- :fontawesome-solid-user-group: **Participant:** [Fujitsu](./participants.md#fujitsu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/flab_trec7_report012299.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/flab_trec7_report012299.pdf.gz)
- :material-file-search: **Runs:** [FLab7at](./runs.md#flab7at) | [FLab7ad](./runs.md#flab7ad) | [FLab7atE](./runs.md#flab7ate)

??? abstract "Abstract"
	
	In our first participation in TREC, our focus was on improving the basic ranking systems and applying text clustering techniques for query ex-pansion. We tested a variety of techiniques including reference measures, passage retrieval, and data fusion for the basic ranking systems. Some te-chiniques were used in the official run, others were not used because of time limitations. We applied the text clustering techiniques for query expansion with a text clustering engine. Clustering base query expansion uses the top N best text clusters from the top 1000 documents instead of just using the top N documents. Clustering base query expansion produces better results than simple query expansion based on passage retrieval. We submitted three runs, Flab7at, Flab7ad, and Flab7atE. Flabat is combination of ranking and query expansion by clustering the top 1000 documents on the title field, Flabad is combination of ranking and query expansion by clustering on the description field, and Flab7atE is combination of ranking with Boolean (exis-tence) operators and query expansion by passage retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NambaIHNM98.bib) "
	```
	@inproceedings{DBLP:conf/trec/NambaIHNM98,
		author = {Isao Namba and Nobuyuki Igata and Hisayuki Horai and Kiyoshi Nitta and Kunio Matsui},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Fujitsu Laboratories {TREC7} Report},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {327--335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/flab_trec7_report012299.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NambaIHNM98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NTT DATA at TREC-7: System Approach for Ad-Hoc and Filtering

_Hiroyuke Nakajima, Toru Takaki, Tsutomu Hirao, Akira Kitauchi_

- :fontawesome-solid-user-group: **Participant:** [NTT](./participants.md#ntt)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/nttdata_at_TREC_7.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/nttdata_at_TREC_7.pdf.gz)
- :material-file-search: **Runs:** [nttdata7Al0](./runs.md#nttdata7al0) | [nttdata7Al2](./runs.md#nttdata7al2) | [nttdata7At1](./runs.md#nttdata7at1)

??? abstract "Abstract"
	
	In TREC-7, we participated in the ad-hoc task (main task) and the filtering track (sub task). In the ad-hoc task, we adopted a scoring method that used co-occurrence term relations in a document and specific processing in order to determine which conceptual parts of the documents should be targeted for query expansion. In filtering, we adopted a machine-readable dictionary for detecting idioms and an inductive learning algorithm for detecting important co-occurrences of terms. In this paper, we describe the system approach and discuss the evaluation results in brief for our ad-hoc and filtering in TREC-7.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NakajimaTHK98.bib) "
	```
	@inproceedings{DBLP:conf/trec/NakajimaTHK98,
		author = {Hiroyuke Nakajima and Toru Takaki and Tsutomu Hirao and Akira Kitauchi},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{NTT} {DATA} at {TREC-7:} System Approach for Ad-Hoc and Filtering},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {420--428},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/nttdata_at_TREC_7.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NakajimaTHK98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BBN at TREC7: Using Hidden Markov Models for Information Retrieval

_David R. H. Miller, Tim Leek, Richard M. Schwartz_

- :fontawesome-solid-user-group: **Participant:** [BBN](./participants.md#bbn)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/trec7bbn.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/trec7bbn.pdf.gz)
- :material-file-search: **Runs:** [bbn1](./runs.md#bbn1)

??? abstract "Abstract"
	
	We present a new method for information retrieval using hidden Markov models (HMMs) and relate our experience with this system on the TREC-7 ad hoc task. We develop a general framework for incorporating multiple word generation mechanisms within the same model. We then demonstrate that an extremely simple realization of this model substantially outperforms tf.idf ranking on both the TREC-6 and TREC-7 ad hoc retrieval tasks. We go on to present several algorithmic refinements, including a novel method for performing blind feedback in the HMM framework. Together, these methods form a state-of-the-art retrieval system that ranked among the best on the TREC-7 ad hoc retrieval task, and showed extraordinary performance in development experiments on TREC-6.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MillerLS98.bib) "
	```
	@inproceedings{DBLP:conf/trec/MillerLS98,
		author = {David R. H. Miller and Tim Leek and Richard M. Schwartz},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{BBN} at {TREC7:} Using Hidden Markov Models for Information Retrieval},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {80--89},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/trec7bbn.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MillerLS98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Retrieval and Visualization using SENTINEL

_Margaret M. Knepper, Robert A. Killam, Kevin L. Fox, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [Harris](./participants.md#harris)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/harris.PDF](https://trec.nist.gov/pubs/trec7/papers/harris.PDF)
- :material-file-search: **Runs:** [harris1](./runs.md#harris1)

??? abstract "Abstract"
	
	Harris Corporation focuses on information retrieval support for various Government agencies. Time constraints and interest-level limit our user to reviewing the top documents before determining if the results of a query are accurate and satisfactory. In such cases, retrieval times and precision accuracy are at a premium, with recall potentially being compromised. To meet user demands our system, called SENTINEL, was designed to yield efficient, high precision retrieval. This is the second time Harris has participated in the Text Retrieval Conference (TREC). We learned a lot from our first TREC [Knepper-97]. This year, we enhanced several aspects of our retrieval system and improved our performance over last year's results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KnepperKFF98.bib) "
	```
	@inproceedings{DBLP:conf/trec/KnepperKFF98,
		author = {Margaret M. Knepper and Robert A. Killam and Kevin L. Fox and Ophir Frieder},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Information Retrieval and Visualization using {SENTINEL}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {336--340},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/harris.PDF},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KnepperKFF98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Indexing Using Both N-Grams and Words

_James Mayfield, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [JHU](./participants.md#jhu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/JHUAPL.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/JHUAPL.pdf.gz)
- :material-file-search: **Runs:** [APL985L](./runs.md#apl985l) | [APL985LC](./runs.md#apl985lc) | [APL985SC](./runs.md#apl985sc)

??? abstract "Abstract"
	
	The Johns Hopkins University Applied Physics Laboratory (JHU/APL) is a first-time entrant in the TREC Category A evaluation. The focus of our information retrieval research is on the relative value of and interaction among multiple term types. In particular, we are interested in examining both words and n-grams as indexing terms. The relative values of words and n-grams have been disputed; to our knowledge though, no one has previously studied their relative merits while holding all other aspects of the system constant.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MayfieldM98.bib) "
	```
	@inproceedings{DBLP:conf/trec/MayfieldM98,
		author = {James Mayfield and Paul McNamee},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Indexing Using Both N-Grams and Words},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {361--365},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/JHUAPL.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MayfieldM98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad Hoc Retrieval Experiments Using WordNet and Automatically Constructed  Thesauri

_Rila Mandala, Takenobu Tokunaga, Hozumi Tanaka, Akitoshi Okumura, Kenji Satoh_

- :fontawesome-solid-user-group: **Participant:** [NEC/TITECH](./participants.md#nec/titech)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/nectitech-proc.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/nectitech-proc.pdf.gz)
- :material-file-search: **Runs:** [nectitech](./runs.md#nectitech) | [nectitechdes](./runs.md#nectitechdes) | [nectitechall](./runs.md#nectitechall)

??? abstract "Abstract"
	
	This paper describe our method in automatic-adhoc task of TREC-7. We propose a method to improve the performance of information retrieval system by expanded the query using 3 diffferent types of thesaurus. The expansion terms are taken from handcrafted thesaurus (WordNet), co-occurrence-based automatically constructed thesaurus, and syntactically predicate-argument based automatically constructed thesaurus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MandalaTTOS98.bib) "
	```
	@inproceedings{DBLP:conf/trec/MandalaTTOS98,
		author = {Rila Mandala and Takenobu Tokunaga and Hozumi Tanaka and Akitoshi Okumura and Kenji Satoh},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ad Hoc Retrieval Experiments Using WordNet and Automatically Constructed Thesauri},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {414--419},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/nectitech-proc.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MandalaTTOS98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion and Classification of Retrieved Documents

_Claude de Loupy, Patrice Bellot, Marc El-Bèze, Pierre-Francois Marteau_

- :fontawesome-solid-user-group: **Participant:** [bertin-cie](./participants.md#bertin-cie)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/LIA.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/LIA.pdf.gz)
- :material-file-search: **Runs:** [LIAClass](./runs.md#liaclass) | [LIArel2](./runs.md#liarel2) | [LIAshort2](./runs.md#liashort2)

??? abstract "Abstract"
	
	This paper presents different methods tested by the University of Avignon and Bertin at the TREC-7 evaluation. A first section describes several methodologies used for query expansion: synonymy and stemming. Relevance feedback is applied both to the TIPSTER corpora and Internet documents. In a second section, we describe a classification algorithm based on hierarchical and clustering methods. This algorithm improves results given by any Information Retrieval system (that retrieves a list of documents from a query) and helps the users by automatically providing a structured document map from the set of retrieved documents. Lastly, we present the first results obtained with TREC-6 and TREC-7 corpora and queries by using this algorithm.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LoupyBEM98.bib) "
	```
	@inproceedings{DBLP:conf/trec/LoupyBEM98,
		author = {Claude de Loupy and Patrice Bellot and Marc El{-}B{\`{e}}ze and Pierre{-}Francois Marteau},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Query Expansion and Classification of Retrieved Documents},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {382--389},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/LIA.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LoupyBEM98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Manual Queries and Machine Translation in Cross-Language Retrieval  and Interactive Retrieval with Cheshire II at TREC-7

_Fredric C. Gey, Hailing Jiang, Aitao Chen, Ray R. Larson_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/berkeley.trec7.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/berkeley.trec7.pdf.gz)
- :material-file-search: **Runs:** [Brkly24](./runs.md#brkly24) | [Brkly25](./runs.md#brkly25) | [Brkly26](./runs.md#brkly26)

??? abstract "Abstract"
	
	For TREC-7, the Berkeley ad-hoc experiments explored more phrase discovery in topics and documents. We utilized Boolean retrieval combined with probabilistic ranking for 17 topics in ad-hoc manual entry. Our cross-language experiments tested 3 different widely available machine translation software packages. For language pairs (e.g. German to French) for which no direct machine translation was available we made use of English as a universal intermediate language. For CLIR we also manually reformulated the English topics before doing machine translation, and this elicited a significant performance increase for both quad language retrieval and for English against English and French documents. In our Interactive Track entry eight searchers conducted eight searches each, half on the Cheshire II system and the other half on the Zprise system, for a total of 64 searches. Questionnaires were administered to gather information about basic demographic and searching experience, about each search, about each of the systems, and finally, about the user's perceptions of the systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyJCL98.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyJCL98,
		author = {Fredric C. Gey and Hailing Jiang and Aitao Chen and Ray R. Larson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Manual Queries and Machine Translation in Cross-Language Retrieval and Interactive Retrieval with Cheshire {II} at {TREC-7}},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {463--476},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/berkeley.trec7.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GeyJCL98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Use of Query Concepts and Information Extraction to Improve Information  Retrieval Effectiveness

_David O. Holmes, David A. Grossman, Ophir Frieder, M. Catherine McCabe, Abdur Chowdhury_

- :fontawesome-solid-user-group: **Participant:** [gmu](./participants.md#gmu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec7/papers/iitfinal.pdf.gz](https://trec.nist.gov/pubs/trec7/papers/iitfinal.pdf.gz)
- :material-file-search: **Runs:** [iit98ma1](./runs.md#iit98ma1) | [iit98au2](./runs.md#iit98au2) | [iit98au1](./runs.md#iit98au1)

??? abstract "Abstract"
	
	In TREC-7, we participated in both the automatic and manual tracks for category A. For the automatic runs, we included a baseline run and an experimental run that filtered relevance feedback using proper nouns. The baseline run used the short query versions and term thresholding to focus on the most meaningful terms. The experimental run used the long queries (title, description and narrative) with relevance feedback that filtered for proper nouns. Information extraction tools were used to identify proper nouns. For manual runs, we used predefined concept lists with terms from the concept lists combined in different ways. The manual run focused on using phrases and proper nouns in the query. We continued to use the NCR/Teradata DBC-1012 Model 4 parallel database machine as the primary platform and added an implementation on Sybase IQ. We again used the relational database model implemented with unchanged SQL. In addition, we enhanced our system by implementing new stop word lists for terms and selecting phrases based on association scores. Our results, while not dramatic, indicate that further work in merging information extraction and information retrieval is warranted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HolmesGFMC98.bib) "
	```
	@inproceedings{DBLP:conf/trec/HolmesGFMC98,
		author = {David O. Holmes and David A. Grossman and Ophir Frieder and M. Catherine McCabe and Abdur Chowdhury},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Use of Query Concepts and Information Extraction to Improve Information Retrieval Effectiveness},
		booktitle = {Proceedings of The Seventh Text REtrieval Conference, {TREC} 1998, Gaithersburg, Maryland, USA, November 9-11, 1998},
		series = {{NIST} Special Publication},
		volume = {500-242},
		pages = {341--350},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1998},
		url = {https://trec.nist.gov/pubs/trec7/papers/iitfinal.pdf.gz},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HolmesGFMC98.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

