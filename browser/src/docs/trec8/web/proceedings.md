# Proceedings - Large Web 1999 

#### Overview of the TREC-8 Web Track

_David Hawking, Ellen M. Voorhees, Nick Craswell, Peter Bailey_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/web_overview.pdf](http://trec.nist.gov/pubs/trec8/papers/web_overview.pdf)
??? abstract "Abstract"
	
	The TREC-8 Web Track defined ad hoc retrieval tasks over the 100 gigabyte VLC2 collection (Large Web Task) and a selected 2 gigabyte subset known as WT2g (Small Web Task). Here, the guidelines and resources for both tasks are described and results presented and analysed Performance on the Small Web was strongly correlated with performance on the regular TREC Ad Hoc task. Little benefit was derived from the use of link-based methods, for standard TREC measures on the WT2g collection. The number of inter-server links within WT2g may have been too small or it may be that link-based methods would have worked better with different types of query and/or with different types of relevance judgment. In fact, a small number of link-based runs proved to be much more effective than their content-only baseline at finding documents which linked to documents judged relevant. A variety of issues were investigated by participants in the Large Web Task. One group investigated the use of PageRank scores and found no benefit on standard TREC measures. Engineering improvements by several groups led to either considerable reduction in query processing time or reduction in the amount of hardware necessary to maintain comparable performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingVCB99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingVCB99,
		author = {David Hawking and Ellen M. Voorhees and Nick Craswell and Peter Bailey},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of the {TREC-8} Web Track},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/web\_overview.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HawkingVCB99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AT&T at TREC-8

_Amit Singhal, Steven P. Abney, Michiel Bacchiani, Michael Collins, Donald Hindle, Fernando C. N. Pereira_

- :fontawesome-solid-user-group: **Participant:** [ATT](./participants.md#att)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf](http://trec.nist.gov/pubs/trec8/papers/att-trec8.pdf)
- :material-file-search: **Runs:** [att99wtdc](./runs.md#att99wtdc) | [att99wtde](./runs.md#att99wtde)

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

#### SCAI TREC-8 Experiments

_Dong-Ho Shin, Yu-Hwan Kim, Sun Kim, Jae-Hong Eom, Hyung-Joo Shin, Byoung-Tak Zhang_

- :fontawesome-solid-user-group: **Participant:** [seoul](./participants.md#seoul)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps](http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps)
- :material-file-search: **Runs:** [Scai8Web1](./runs.md#scai8web1) | [Scai8Web2](./runs.md#scai8web2)

??? abstract "Abstract"
	
	This working note reports our experiences with TREC-8 on four tracks: Ad Hoc, Filtering, Web, and QA. The Ad Hoc retrieval engine, SCAIR, has been used for the Web and QA experiments, and the filtering experiments were based on it's own engine. As a second entry to TREC, we focused this year on exploring possibilities of applying machine learning techniques to TREC tasks. The Ad Hoc track employed a cluster-based retrieval method where the scoring function used cluster information extracted from a collection of precompiled documents. Filtering was based on naive Bayes learning supported by an EM algorithm. In the Web track, we compared the performance of using link information to that of not using the information. In the QA track, some passage extraction techniques have been tested using the baseline SCAIR retrieval engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShinKKESZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShinKKESZ99,
		author = {Dong{-}Ho Shin and Yu{-}Hwan Kim and Sun Kim and Jae{-}Hong Eom and Hyung{-}Joo Shin and Byoung{-}Tak Zhang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SCAI} {TREC-8} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShinKKESZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC-8 Experiment: Searching on the Web and in Distributed  Collections

_Jacques Savoy, Justin Picard_

- :fontawesome-solid-user-group: **Participant:** [savoy](./participants.md#savoy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/neuchatel2.pdf](http://trec.nist.gov/pubs/trec8/papers/neuchatel2.pdf)
- :material-file-search: **Runs:** [UniNEWCt](./runs.md#uninewct) | [UniNEW2Ct](./runs.md#uninew2ct) | [UniNEWLink](./runs.md#uninewlink) | [UniNEW2Link](./runs.md#uninew2link)

??? abstract "Abstract"
	
	The Internet paradigm permits information searches to be made across wide-area networks where information is contained in web pages and/or whole document collections such as digital libraries. These new distributed information environments reveal new and challenging problems for the IR community. Consequently, in this TREC experiment we investigated two questions related to information searches on the web or in digital libraries: (1) an analysis of the impact of hyperlinks in improving retrieval performance, and (2) a study of techniques useful in selecting more appropriate text databases (database selection problem encountered when faced with multiple collections), including an evaluation of certain merging strategies effective in producing, single, ranked lists to be presented to the user (database merging problem).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavoyP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavoyP99,
		author = {Jacques Savoy and Justin Picard},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Report on the {TREC-8} Experiment: Searching on the Web and in Distributed Collections},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/neuchatel2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SavoyP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi/Keenbow at TREC-8

_Stephen E. Robertson, Steve Walker_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/okapi.pdf](http://trec.nist.gov/pubs/trec8/papers/okapi.pdf)
- :material-file-search: **Runs:** [ok8wmx](./runs.md#ok8wmx)

??? abstract "Abstract"
	
	Automatic ad hoc and web track: Three ad hoc runs were submitted: long (title, description and narrative), medium (title and description) and short (title only). 'Blind' expansion was used for all runs. The queries from the medium ad hoc run were reused for the small web track submission. Most of the negative expressions were removed from the narrative field of the topic statements, and a new expansion term selection procedure was tried. Adaptive filtering: Methods were similar to those we used in TREC-7. Six runs were submitted. VLC track: Two unexpanded ad hoc runs were submitted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonW99,
		author = {Stephen E. Robertson and Steve Walker},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Okapi/Keenbow at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/okapi.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Moving More Quickly toward Full Term Relations in Information Space

_Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [Newby](./participants.md#newby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/newby-trec99-proceedings.pdf](http://trec.nist.gov/pubs/trec8/papers/newby-trec99-proceedings.pdf)
- :material-file-search: **Runs:** [isw25](./runs.md#isw25) | [isw50](./runs.md#isw50) | [isw25t](./runs.md#isw25t) | [isw50t](./runs.md#isw50t)

??? abstract "Abstract"
	
	This paper describes the ISpace retrieval system's involvement in TREC8. The main goal for this year's work was to speed up document indexing and query processing compared to previous years. This goal was achieved, but retrieval performance was not as good as for TREC7. System details for the AdHoc task, small Web task, and large Web (VLC) task are presented. The AdHoc task emphasized query expansion, while the large Web track emphasized rapid indexing and retrieval. The paper describes an implementation of a multidimensional tree structure for retrieval from information space based on the kd-tree. The larger setting for ISpace, the TeraScale Retrieval project, is summarized. A concluding section describes plans for ISpace.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Newby99.bib) "
	```
	@inproceedings{DBLP:conf/trec/Newby99,
		author = {Gregory B. Newby},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Moving More Quickly toward Full Term Relations in Information Space},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/newby-trec99-proceedings.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Newby99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fujitsu Laboratories TREC8 Report - Ad hoc, Small Web, and Large  Web Track

_Isao Namba, Nobuyuki Igata_

- :fontawesome-solid-user-group: **Participant:** [fujitsu](./participants.md#fujitsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/flab8_proceedings_letter.pdf](http://trec.nist.gov/pubs/trec8/papers/flab8_proceedings_letter.pdf)
- :material-file-search: **Runs:** [Flab8wtdN](./runs.md#flab8wtdn) | [Flab8wtdnN](./runs.md#flab8wtdnn)

??? abstract "Abstract"
	
	This year a Fujitsu Laboratory team participated in three tracks that is ad hoc, small web track, and large web track. As basic techiniques, we compared four popular stemmers, and we made simple removing stop pattern techniques for TREC queries. For the ad hoc task, and small web track, we used the same techniques. We experimented with area weighting, co-occurence boosting, bi-gram utliza-tion, and reranking by bi-gram extraction from pilot search. The effect of blind application with those te-chiniques is rather limited, or even uncertain in the TREC8 experiment. What we can say from TREC8 result is that blind application of co-occurence boosting and area weighting may be effective for the small web track. They requerie query dependent application. In the large web track, our main interest is ef-ficiency, that is how much resources are required to process 100GB of web text and 10000 real web queries in practical time. Using a statistical based language type checker, we can eliminate 23% of non-English text. This leads to speeding up a indexing and reducing the index size. The search speed for an inverted file is CPU intensive if the target machine has main memory in excess of 10-25% of the index size. So with simple, but effective index compression methods, the throughput of query processing is about 0.54-1.1 query/second even by a single 300MHz Ultra-sparc processor.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NambaI99.bib) "
	```
	@inproceedings{DBLP:conf/trec/NambaI99,
		author = {Isao Namba and Nobuyuki Igata},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Fujitsu Laboratories {TREC8} Report - Ad hoc, Small Web, and Large Web Track},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/flab8\_proceedings\_letter.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NambaI99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT at TREC-8: Improving Baseline Precision

_M. Catherine McCabe, David O. Holmes, Kenneth L. Alford, Abdur Chowdhury, David A. Grossman, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [iit](./participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/iit99pr.pdf](http://trec.nist.gov/pubs/trec8/papers/iit99pr.pdf)
- :material-file-search: **Runs:** [iit99wt1](./runs.md#iit99wt1) | [iit99wt2](./runs.md#iit99wt2) | [iit99wt3](./runs.md#iit99wt3)

??? abstract "Abstract"
	
	In TREC-8, we participated in the automatic and manual tracks for category A as well as the small web track. This year, we focussed on improving our baseline and then introduced some experimental improvements. Our automatic runs used relevance feedback with a high-precision first pass to select terms and then a high-recall final pass. For manual runs, we used predefined concept lists focussing on phrases and proper nouns in the query. In the small web-track, we submitted one content-only run and two link-plus-content runs. We continued to use the relational model with unchanged SQL for retrieval. Our results show some promise for the use of automatic concepts, expansion within concepts and a high-precision first pass for relevance feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCabeHACGF99.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCabeHACGF99,
		author = {M. Catherine McCabe and David O. Holmes and Kenneth L. Alford and Abdur Chowdhury and David A. Grossman and Ophir Frieder},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{IIT} at {TREC-8:} Improving Baseline Precision},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/iit99pr.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCabeHACGF99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ACSys TREC-8 Experiments

_David Hawking, Peter Bailey, Nick Craswell_

- :fontawesome-solid-user-group: **Participant:** [ACSys](./participants.md#acsys)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/acsys.pdf](http://trec.nist.gov/pubs/trec8/papers/acsys.pdf)
- :material-file-search: **Runs:** [acsys8wm](./runs.md#acsys8wm) | [acsys8wmp](./runs.md#acsys8wmp) | [acsys8wmq](./runs.md#acsys8wmq) | [acsys8wmr](./runs.md#acsys8wmr)

??? abstract "Abstract"
	
	Experiments relating to TREC-8 Ad Hoc, Web Track (Large and Small) and Query Track tasks are described and results reported. Due to time constraints, only minimal effort was put into Ad Hoc and Query Track participation. In the Web Track, Google-style PageRanks were calculated for all 18.5 million pages in the VLC2 collection and for the 0.25 million pages in the WT2g collection. Various combinations of content score and PageRank produced no benefit for TREC style ad hoc retrieval. A major goal in the Web Track was to make engineering improvements to permit indexing of the 100 gigabyte collection and subsequent query processing using a single PC. A secondary goal was to achieve last year's performance (obtained with eight DEC Alphas) with less recourse to effectiveness-harming optimisations. The main goal was achieved and indexing times are comparable to last year's. However, effectiveness results were worse relative to last year and query processing times were approximately double.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingBC99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingBC99,
		author = {David Hawking and Peter Bailey and Nick Craswell},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ACSys {TREC-8} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/acsys.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HawkingBC99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Connectivity Analysis Approach to Increasing Precision in Retrieval  From Hyperlinked Documents

_Cathal Gurrin, Alan F. Smeaton_

- :fontawesome-solid-user-group: **Participant:** [dublin](./participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/dcuTREC8paper.pdf](http://trec.nist.gov/pubs/trec8/papers/dcuTREC8paper.pdf)
- :material-file-search: **Runs:** [DCU99C01](./runs.md#dcu99c01) | [DCU99L02](./runs.md#dcu99l02) | [DCU99L01](./runs.md#dcu99l01)

??? abstract "Abstract"
	
	Within the last few years very little as been made of the usefulness of Connectivity Analysis to Information Retrieval on the WWW. This document discusses hyperlinks on the WWW and our experiments on the exploitation of the immediate neighbourhood of a web page in an effort to improve search results. In order to test the hypothesis that Connectivity Analysis can increase precision in the top ranked documents from a set of relevant documents, we developed a software application to generate and re-rank a query relevant subset of the WT2g Dataset. We discuss our software in depth and the problems that we encountered during development. Our experiments are based on implementing a number of re-ranking formulae, each of which tests the usefulness of different approaches to re-ranking a set of relevant pages, ranging from basic context analysis (inLink ranking) to combined content and context analysis approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GurrinS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/GurrinS99,
		author = {Cathal Gurrin and Alan F. Smeaton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {A Connectivity Analysis Approach to Increasing Precision in Retrieval From Hyperlinked Documents},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/dcuTREC8paper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GurrinS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The RMIT/CSIRO Ad Hoc, Q&A, Web, Interactive, and Speech Experiments  at TREC 8

_Michael Fuller, Marcin Kaszkiel, Sam Kimberley, Corinna Ng, Ross Wilkinson, Mingfang Wu, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [rmit](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf](http://trec.nist.gov/pubs/trec8/papers/RMIT-CSIRO.pdf)
- :material-file-search: **Runs:** [mds08w1](./runs.md#mds08w1) | [mds08w2](./runs.md#mds08w2) | [mds08w3](./runs.md#mds08w3)

??? abstract "Abstract"
	
	The MDS group participated in the small web track, submitting three runs; a content-only run, mds08w1, and two content-and-link runs, mds08w2 and mds08w3. Our objective in participating in this track was twofold. Firstly, to determine whether simple manipulation of linking information would enable effective re-ranking of documents within a result set. Secondly, to examine the effectiveness of content-only retrieval on web data.
	

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

#### Filters, Webs and Answers: The University of Iowa TREC-8 Results

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [iowa](./participants.md#iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf](http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf)
- :material-file-search: **Runs:** [uiowaweb1](./runs.md#uiowaweb1) | [uiowaweb2](./runs.md#uiowaweb2)

??? abstract "Abstract"
	
	The University of Iowa attempted three tracks this year: filtering, question answering, and Web, the latter two new for us this year. All work was based upon that done for TREC-7 [21, with our system adapted for the specifics of the QA and Web tracks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS99,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Filters, Webs and Answers: The University of Iowa {TREC-8} Results},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Early DiscoWeb Prototype at TREC8

_Brian D. Davison, Apostolos Gerasoulis, Konstantinos Kleisouris, Yingfang Lu, Hyun-ju Seo, Junyu Tian, Song Wang, Wei Wang, Baohua Wu_

- :fontawesome-solid-user-group: **Participant:** [rutgers-davison](./participants.md#rutgers-davison)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/discoweb.pdf](http://trec.nist.gov/pubs/trec8/papers/discoweb.pdf)
- :material-file-search: **Runs:** [disco2](./runs.md#disco2) | [disco3](./runs.md#disco3)

??? abstract "Abstract"
	
	Recently the notion of popularity and its generalizations have been investigated as a possible alternative approach to text only analysis to rank web pages in search engines (e.g. Kle98, BP98, CDR+98, CDDG+98, BH98, HHMN99] among others). We have built a research prototype that incorporates many link analysis algorithms from the literature and also new algorithms to investigate the impact of the popularity on the ranking of the search engines (DGK+ 99]. Our goal in the TREC& competition was to investigate the quality of the results using the TREC data and in particular the large web track. Unfortunately we did not have the needed hardware in time to generate results for the large web track. We only participated in the Small Web Track (Text Only and Text and Link Analysis). However, our system was designed for large datasets and the quality of the TREC8 results are not representative of the system. More recently we have experimented with larger datasets and we have come to the conclusion that link analysis can significantly increase the quality of the ranking of search engines, a conclusion that is shared by many others in the literature (BP98, PBMW98, Kle98, CDR+98, CDDG+98, CDG+ 99]. We will report these new results in a future publication.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DavisonGKLSTWWW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/DavisonGKLSTWWW99,
		author = {Brian D. Davison and Apostolos Gerasoulis and Konstantinos Kleisouris and Yingfang Lu and Hyun{-}ju Seo and Junyu Tian and Song Wang and Wei Wang and Baohua Wu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {An Early DiscoWeb Prototype at {TREC8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/discoweb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DavisonGKLSTWWW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fast Automatic Passage Ranking (MultiText Experiments for TREC-8)

_Gordon V. Cormack, Charles L. A. Clarke, D. I. E. Kisman, Christopher R. Palmer_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf](http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf)
- :material-file-search: **Runs:** [uwmt8w0](./runs.md#uwmt8w0)

??? abstract "Abstract"
	
	TREC-8 represents the fifth year that the MultiText project has participated in TREC [2, 1, 4, 5]. The MultiText project develops and prototypes scalable technologies for parallel information retrieval systems implemented on networks of workstations. Research issues are addressed in the context of this parallel architecture. Issues of concern to the MultiText Project include data distribution, load balancing, fast update, fault tolerance, document structure, relevance ranking, and user interaction. The MultiText system incorporates a unique technique for arbitrary passage retrieval. Since our initial participation in TREC-4 our TREC work has explored variants of this technique. For TREC-8 we focused our efforts on the Web track. In addition, we submitted runs for the Adhoc task (title and title +description) and a run for the Question Answering task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackCKP99.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackCKP99,
		author = {Gordon V. Cormack and Charles L. A. Clarke and D. I. E. Kisman and Christopher R. Palmer},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Fast Automatic Passage Ranking (MultiText Experiments for {TREC-8)}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/waterloo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackCKP99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at trec8: Adhoc, Web, CLIR and Filtering tasks

_Mohand Boughanem, Christine Julien, Josiane Mothe, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [irit](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/irit.pdf](http://trec.nist.gov/pubs/trec8/papers/irit.pdf)
- :material-file-search: **Runs:** [Mer8Wctd](./runs.md#mer8wctd) | [Mer8Wci1](./runs.md#mer8wci1) | [Mer8Wci2](./runs.md#mer8wci2) | [Mer8Wci3](./runs.md#mer8wci3)

??? abstract "Abstract"
	
	The tests performed for TREC8 were focused on automatic Adhoc, Web, Clir and Filtering (batch and routing) tasks. All the submitted runs were based on the Mercure system. Automatic adhoc : Four runs were submitted. All these runs were based on automatic relevance back-propagation used in the previous TREC, with a slight change for one of these runs (Mer8Adtd3). A strategy based on predicting the relevance of documents using the past relevant documents was tested for this run. More precisely, instead of using the same relevance value for all top retrieved documents, some of them are selected and have their relevance value boosted. Web : Four runs were submitted in this track: 1. content based only using Mercure simple search 2. content tilink, according to Mercure architecture, we consider that document nodes are linked each other by weighted links. The top selected documents resulting from the initial search spread their signals towards the other document nodes. The documents were then sorted according to their activations, the top 1000 documents were submitted. 3. (2) + pseudo-relevance back-propagation method. 4. reranking of the 40 top documents using their links between each others. Cross-language : Three runs were submitted for our first participation in this track. All these runs were based on query translation using an online machine translation . Two of these runs are a comparison between query translation from English to other languages and from French to other languages. Filtering - batch and routing: The profiles were learned using three different strategies : Relevance Back-propagation (RB) and Gradient Back-propagation (GB) used in the previous TREC and a new strategy based on Genetic Algorithm (GA). Four runs were submitted, two batch runs based on RB+GB and two routing runs, one based on RB+GB and the other one based on GA.
	

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

#### CLARIT TREC-8 Experiments in Searching Web Data

_Jeffrey Bennett, Xiang Tong, David A. Evans_

- :fontawesome-solid-user-group: **Participant:** [claritech](./participants.md#claritech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/CLARIT_Web.pdf](http://trec.nist.gov/pubs/trec8/papers/CLARIT_Web.pdf)
- :material-file-search: **Runs:** [CL99WebH](./runs.md#cl99webh) | [CL99WebM](./runs.md#cl99webm)

??? abstract "Abstract"
	
	CLARITECH submitted two baseline content-only runs and completed two additional content+link runs in the TREC-8 Web Track. These represent our first serious attempt to deal with Web data, and our first automatic runs in several years. The first question was whether CLARIT would perform as well on Web data as on more traditional text. We found that, with extensive pre-processing of the raw data prior to indexing, the automatic retrieval system actually performed better on Web data than on Ad Hoc data. For the link runs, we implemented a version of the HITS algorithm [Kleinberg 1997], originally developed at IBM. Our version optimized HITS for the CLARIT environment, but also reflected some constraints imposed by limited resources. Unable to develop and sufficiently test our own matrix-processing library in time, we used a commercial product for the number crunching. Performance on the link runs was poor, but failure analysis suggests many ways to improve it.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BennettTE99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BennettTE99,
		author = {Jeffrey Bennett and Xiang Tong and David A. Evans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CLARIT} {TREC-8} Experiments in Searching Web Data},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/CLARIT\_Web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BennettTE99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-8

_James Allan, James P. Callan, Fangfang Feng, Daniella Malin_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf)
- :material-file-search: **Runs:** [INQ620](./runs.md#inq620)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in seven of the tracks: ad-hoc, filtering, spoken document retrieval, small web, large web, question and answer, and the query tracks. We spent signicant time working on the filtering track, resulting in substantial performance improvement over TREC-7. For all of the other tracks, we used essentially the same system as used in previous years. In the next section, we describe some of the basic processing that was applied across most of the tracks. We then describe the details for each of the tracks and in some cases present some modest analysis of the effectiveness of our results.
	

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

