# Proceedings - Web 2002 

#### Overview of the TREC-2002 Web Track

_Nick Craswell, David Hawking_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/WEB.OVER.pdf](http://trec.nist.gov/pubs/trec11/papers/WEB.OVER.pdf)
??? abstract "Abstract"
	
	The TREC-2002 Web Track moved away from non-Web relevance ranking and towards Web-specific tasks on a 1.25 million page crawl “.GOV”. The topic distillation task involved finding pages which were relevant, but also had characteristics which would make them desirable inclusions in a distilled list of key pages. The named page task is a variant of last year's homepage finding task. The task is to find a particular page, but in this year's task the page need not be a home page.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellH02.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellH02,
		author = {Nick Craswell and David Hawking},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC-2002} Web Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/WEB.OVER.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellH02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Hierarchical Clustering and Summarisation Approaches for Web  Retrieval: Glasgow at the TREC 2002 Interactive Track

_Richard Osdin, Iadh Ounis, Ryen W. White_

- :fontawesome-solid-user-group: **Participant:** [glasgow](./participants.md#glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/glasgow.int.pdf](http://trec.nist.gov/pubs/trec11/papers/glasgow.int.pdf)
- :material-file-search: **Runs:** [uog01ctaialh](./runs.md#uog01ctaialh) | [uog02ctadh](./runs.md#uog02ctadh) | [uog03ctadqh](./runs.md#uog03ctadqh) | [uog04cta2dqh](./runs.md#uog04cta2dqh) | [uog05tad](./runs.md#uog05tad) | [uog06c](./runs.md#uog06c) | [uog07cta](./runs.md#uog07cta) | [uog08ctap](./runs.md#uog08ctap) | [uog09cta2](./runs.md#uog09cta2) | [uog10ctad](./runs.md#uog10ctad)

??? abstract "Abstract"
	
	Current search engines are typified as having a lack of precision, coupled with an elongated ranked list style of result presentation. When combined, these factors make relevant data extraction increasingly complex. The main investigation of our participation in the Interactive Track of TREC 2002 is to assess the effectiveness of new visualisation techniques for displaying the results of search engines. Our current system, provisionally named HuddleSearch, uses a newly developed clustering algorithm, which dynamically organises the relevant documents into a traversable hierarchy of general to more-specific cluster categories. We have extended our TREC-10 summarisation tool to also allow the summarisation of multiple documents; whereby a summary paints a caricature of the contents of a cluster, rather than an individual document, thus allowing the user to provisionally judge a cluster's relevance prior to viewing its contents. The interaction between the user and the system is further developed by the aid of an information visualisation tool. Our primary assumption is that the combination of both hierarchical clustering and summarisation tools will aid users in their interaction with the system in the Web context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OsdinOW02.bib) "
	```
	@inproceedings{DBLP:conf/trec/OsdinOW02,
		author = {Richard Osdin and Iadh Ounis and Ryen W. White},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Hierarchical Clustering and Summarisation Approaches for Web Retrieval: Glasgow at the {TREC} 2002 Interactive Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/glasgow.int.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OsdinOW02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC 2002: Web Track

_Shuang Liu, Clement T. Yu, Wensheng Wu_

- :fontawesome-solid-user-group: **Participant:** [illinois_chicago](./participants.md#illinois_chicago)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uillinois.li.pdf](http://trec.nist.gov/pubs/trec11/papers/uillinois.li.pdf)
- :material-file-search: **Runs:** [uic0101](./runs.md#uic0101) | [uic0102](./runs.md#uic0102) | [uic0103](./runs.md#uic0103) | [uicnp01](./runs.md#uicnp01) | [uicnp02](./runs.md#uicnp02) | [uicnp03](./runs.md#uicnp03) | [uic0104](./runs.md#uic0104)

??? abstract "Abstract"
	
	This is the first year that members of the Database and Information System Lab (DBIS) at University of Illinois at Chicago (UIC) participate in TREC. We participate in two tasks for the Web track: topic distillation and named page finding. Linkage information among documents as well as content information about documents is used in some of our submitted runs. We utilize the Okapi weighting scheme with some modification for documents and passages retrieval; the proximity of query terms in documents is also utilized for document ranking. The PageRank of a document is combined with the similarity of the document with the query to obtain an overall ranking of documents. A local linkage and URL analysis algorithm is employed for topic distillation. In the named page finding task, we combine the surrogate similarity with the document similarity in one run.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuYW02.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuYW02,
		author = {Shuang Liu and Clement T. Yu and Wensheng Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC} 2002: Web Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uillinois.li.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuYW02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2002 Web, Novelty and Filtering Track Experiments using PIRCS

_Kui-Lam Kwok, Peter Deng, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf](http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf)
- :material-file-search: **Runs:** [pirc2Wd1](./runs.md#pirc2wd1) | [pirc2Wd2](./runs.md#pirc2wd2) | [pirc2Wnp1](./runs.md#pirc2wnp1) | [pirc2Wnp2](./runs.md#pirc2wnp2)

??? abstract "Abstract"
	
	In TREC2002, we participated in three tracks: web, novelty and adaptive filtering. The Web track has two tasks: distillation and named-page retrieval. Distillation is a new utility concept for ranking documents, and needs new design on the output document ranked list after an ad-hoc retrieval from the web (.gov) collection. Novelty track is a new task that involves identifying relevant sentences to a question, and to remove duplicate or non-novel entries in the answer list. The third track is adaptive filtering. We revived a filtering program that was functional at TREC-9 with some added capability. Sections 2, 3, 4 describe our participation in these tracks respectively. Section 5 has our conclusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokDDC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokDDC02,
		author = {Kui{-}Lam Kwok and Peter Deng and Norbert Dinstl and M. Chan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2002 Web, Novelty and Filtering Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokDDC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CARROTT 11 and the TREC 11 Web Track

_R. Scott Cost, Srikanth Kallurkar, Hemali Majithia, Charles K. Nicholas, Yongmei Shi_

- :fontawesome-solid-user-group: **Participant:** [umbc-cost](./participants.md#umbc-cost)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umbc.kallurkar.pdf](http://trec.nist.gov/pubs/trec11/papers/umbc.kallurkar.pdf)
- :material-file-search: **Runs:** [CARROT2A](./runs.md#carrot2a) | [CARROT2B](./runs.md#carrot2b) | [CARROT2D](./runs.md#carrot2d) | [CARROT2C](./runs.md#carrot2c) | [CARROT2E](./runs.md#carrot2e)

??? abstract "Abstract"
	
	We describe CARROT II, an agent-based architecture for distributed information retrieval and document collection management. CARROT II consists of an arbitrary number of agents, distributed across a variety of platforms and locations. CARROT II agents provide search services over local document collections or information sources. They advertise content-derived metadata that describes their local document store. This metadata is sent to other CARROT II agents which agree to act as brokers for that collection, and every agent in the system has the ability to serve as such a broker. A query can be sent to any CARROT II agent, which can decide to answer the query itself from its local collection, or to send the query on to other agents whose metadata indicate that they would be able to answer the query, or send the query on further. Search results from multiple agents are merged and returned to the user. CARROT II differs from similar systems in that metadata takes the form of an automatically generated, unstructured feature vector, and that any agent in the system can act as a broker, so there is no centralized control. We present experimental results of retrieval performance and effectiveness in a distributed environment. We have evaluated CARROT II in the context of the Web Track of NIST's annual Text Retrieval Conference. Our methodology is described, and results are presented. 
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CostKMNS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/CostKMNS02,
		author = {R. Scott Cost and Srikanth Kallurkar and Hemali Majithia and Charles K. Nicholas and Yongmei Shi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CARROTT} 11 and the {TREC} 11 Web Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umbc.kallurkar.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CostKMNS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Filtering, Novelty Detection, and Named-Page Finding

_Kevyn Collins-Thompson, Paul Ogilvie, Yi Zhang, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu_lti](./participants.md#cmu_lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf](http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf)
- :material-file-search: **Runs:** [LmrAllEq](./runs.md#lmralleq) | [LmrAllEst](./runs.md#lmrallest) | [LmrNoStruct](./runs.md#lmrnostruct) | [LmrDocStruct](./runs.md#lmrdocstruct) | [LmrSmall](./runs.md#lmrsmall)

??? abstract "Abstract"
	
	In TREC 11, our group participated in the Novelty track, Filtering track, and the Named-Page Finding task of the Web track. This paper describes our approaches, experiments, and results. As the approach for each task is quite different, the paper contains a section for each of the tasks. The following section describes our experiments in adaptive filtering, Section 3 describes named-page finding, and section 4 discusses the Novelty track
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Collins-ThompsonOZC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Collins-ThompsonOZC02,
		author = {Kevyn Collins{-}Thompson and Paul Ogilvie and Yi Zhang and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Information Filtering, Novelty Detection, and Named-Page Finding},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Collins-ThompsonOZC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT at TREC 2002 Linear Combinations Based on Document Structure  and Varied Stemming for Arabic Retrieval

_Abdur Chowdhury, Mohammed Aljlayl, Eric C. Jensen, Steven M. Beitzel, David A. Grossman, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [IIT](./participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/iit.grossman.pdf](http://trec.nist.gov/pubs/trec11/papers/iit.grossman.pdf)
- :material-file-search: **Runs:** [iit02b](./runs.md#iit02b) | [iit02tf](./runs.md#iit02tf) | [iit02tfa](./runs.md#iit02tfa)

??? abstract "Abstract"
	
	For TREC 10 we participated in the Named Page Finding Task and the Cross-Lingual Task. In the web track, we explored the use of linear combinations of term collections based on document structure. Our goal was to examine the effects of different term collection statistics based on document structure in respect to known item retrieval. We parsed documents into structural components and built specific term indexes based on that document structure. Each of those indices have their own collection statistics for term weighting based on the type of language used for that structure in the collection. For producing a single ranked list, we examined a weighted linear combination approach to merging results. Our approach to known item retrieval was equal or above the median 58% of the time and 71% above the mean score of submitted runs. In the Arabic track we participated in Arabic Cross-language Information Retrieval (CLIR) and in Arabic monolingual information retrieval. For the monolingual retrieval, we examined the use of two stemming algorithms. The first is a deeper approach, and the second is a pattern-based approach. For the Arabic CLIR, we explored the retrieval effectiveness by using a machine translation (MT) system and translation probabilities obtained from parallel documents collection provided by the United Nations (UN).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChowdhuryAJBGF02.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChowdhuryAJBGF02,
		author = {Abdur Chowdhury and Mohammed Aljlayl and Eric C. Jensen and Steven M. Beitzel and David A. Grossman and Ophir Frieder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIT} at {TREC} 2002 Linear Combinations Based on Document Structure and Varied Stemming for Arabic Retrieval},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/iit.grossman.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChowdhuryAJBGF02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Homepage Finding and Topic Distillation Using a Common Retrieval Strategy

_Vo Ngoc Anh, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [UMelbourne](./participants.md#umelbourne)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umelbourne.moffat.pdf](http://trec.nist.gov/pubs/trec11/papers/umelbourne.moffat.pdf)
- :material-file-search: **Runs:** [MU106](./runs.md#mu106) | [MU307](./runs.md#mu307) | [MU208](./runs.md#mu208) | [MU609](./runs.md#mu609) | [MU80A](./runs.md#mu80a) | [MU111](./runs.md#mu111) | [MU212](./runs.md#mu212) | [MU313](./runs.md#mu313) | [MU525](./runs.md#mu525) | [MU624](./runs.md#mu624)

??? abstract "Abstract"
	
	For the TREC-2002 web track the University of Melbourne experimented with a system designed primarily for topic relevance tasks, and applied it directly to the homepage finding and topic distillation tasks. Our intention was to process queries regardless of their classification, as discriminating information may be unavailable in practice. An integer-valued weighting scheme reported in earlier work was employed, modified to take into account anchor text and many of the metadata fields, but not the URL text, and not the link structure information. Our experiments were carried out using a distributed retrieval system, with data spread across a sixteen node cluster. Indexing and query processing is fast, and the total index size is small.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnhM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnhM02,
		author = {Vo Ngoc Anh and Alistair Moffat},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Homepage Finding and Topic Distillation Using a Common Retrieval Strategy},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umelbourne.moffat.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnhM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC 2002: Web Track

_Anis Benammar, Mohand Boughanem, Gilles Hubert, Cecile Laffaire, Josiane Mothe_

- :fontawesome-solid-user-group: **Participant:** [irit](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/irit.web.pdf](http://trec.nist.gov/pubs/trec11/papers/irit.web.pdf)
- :material-file-search: **Runs:** [MercureLynx](./runs.md#mercurelynx) | [Mercah](./runs.md#mercah) | [Mercure](./runs.md#mercure)

??? abstract "Abstract"
	
	The tests we performed for TREC'2002 web track focus on the web distillation part. The aim of our participation is to experiment our method for topic distillation combined with a new version of our system Mercure and to validate our system on a large collection of web pages: 18 Go of data. This year, three runs were submitted to NIST.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BenammarBHLM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/BenammarBHLM02,
		author = {Anis Benammar and Mohand Boughanem and Gilles Hubert and Cecile Laffaire and Josiane Mothe},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRIT} at {TREC} 2002: Web Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/irit.web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BenammarBHLM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LIT at TREC 2002: Web Track

_Nie Yu, Dong-Hong Ji, Lingpeng Yang_

- :fontawesome-solid-user-group: **Participant:** [lit](./participants.md#lit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/lit.donghong.pdf](http://trec.nist.gov/pubs/trec11/papers/lit.donghong.pdf)
- :material-file-search: **Runs:** [litlink](./runs.md#litlink) | [littext](./runs.md#littext)

??? abstract "Abstract"
	
	In Trec-2002, we participated in the Web Trec (named page finding task). There are two kinds of information that can be used while finding the expected page, content information and link information. We exploited both of them. That is to say, our system is content-based and link-based. As to link information, we only used anchor text and connections, and topology between pages is ignored. We submitted two runs. One is based on traditional contented-based retrieval, the other try to combine content-based retrieval and link-based retrieval to get better result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuDL02.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuDL02,
		author = {Nie Yu and Dong{-}Hong Ji and Lingpeng Yang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{LIT} at {TREC} 2002: Web Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/lit.donghong.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuDL02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 11 Experiments at CAS-ICT: Filtering and Web

_Hongbo Xu, Zhifeng Yang, Bin Wang, Bin Liu, Jun Cheng, Yue Liu, Zhe Yang, Xueqi Cheng, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [chinese_academy](./participants.md#chinese_academy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cas_final.hongbo.pdf](http://trec.nist.gov/pubs/trec11/papers/cas_final.hongbo.pdf)
- :material-file-search: **Runs:** [ictnp4](./runs.md#ictnp4) | [ictnp3](./runs.md#ictnp3) | [ictnp2](./runs.md#ictnp2) | [icttd2](./runs.md#icttd2) | [icttd1](./runs.md#icttd1) | [icttd3](./runs.md#icttd3) | [ictnp7](./runs.md#ictnp7) | [ictnp6](./runs.md#ictnp6)

??? abstract "Abstract"
	
	CAS-ICT took part in the TREC conference for the second time this year and we undertook two tracks of TREC-11. For filtering track, we have submitted results of all three subtasks. In adaptive filtering, we paid more attention to undetermined documents processing, profile building and adaptation. In batch filtering and routing, a centroid-based classifier is used with preprocessed samples. For Web track, we have submitted results of both two subtasks. Different factors are considered to improve the overall performance of our Web systems. This paper describes our methods in detail.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuYWLCLYCB02.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuYWLCLYCB02,
		author = {Hongbo Xu and Zhifeng Yang and Bin Wang and Bin Liu and Jun Cheng and Yue Liu and Zhe Yang and Xueqi Cheng and Shuo Bai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 11 Experiments at {CAS-ICT:} Filtering and Web},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cas\_final.hongbo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuYWLCLYCB02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC 2002: Filtering, Q&A, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yingju Xia, Zhe Feng, Yaqian Zhou_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf](http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf)
- :material-file-search: **Runs:** [fduwt11o1](./runs.md#fduwt11o1) | [fduwt11o2](./runs.md#fduwt11o2) | [fduwt11t2](./runs.md#fduwt11t2) | [fduwt11t1](./runs.md#fduwt11t1) | [fduwt11b0](./runs.md#fduwt11b0)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC conference for the third time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we only participate in the sub-task of adaptive filtering. A novel method is presented, in which a winnow classifier from the description and narrative fields is constructed, and then utilized to assist our previous adaptive filtering system. A novel approach to confidence sorting, which is based on Maximum Entropy, is proposed in our Question Answering system. The rank of individual answer is determined by several weighted factors, and the confidence score is the product of the exponent of the weights of every factors. The weight of every factor is assigned during the training of previous questions. To return highly relevant key resources for web retrieval, we modified our original search system to make it return higher precision result than before. First, we proposed a novel search algorithm to get a base set of highly relevant documents. Then special post-processing modules are used to expand and re-sort the base set. This year we tried a fast manifold-based approach to face recognition in the Video Search Task. It can be used when there are only few different images of a specific person and runs fast. Experiment shows that applying this step will make the face recognition 5-fold faster and with almost no decreasing of performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHNXFZ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHNXFZ02,
		author = {Lide Wu and Xuanjing Huang and Junyu Niu and Yingju Xia and Zhe Feng and Yaqian Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDU} at {TREC} 2002: Filtering, Q{\&}A, Web and Video Tasks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHNXFZ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Named Page Finding and Arabic Retrieval with Hummingbird  SearchServerTM at TREC 2002

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/hummingbird.tomlinson.pdf](http://trec.nist.gov/pubs/trec11/papers/hummingbird.tomlinson.pdf)
- :material-file-search: **Runs:** [hum02upd](./runs.md#hum02upd) | [hum02pd](./runs.md#hum02pd) | [hum02ud](./runs.md#hum02ud) | [hum02up](./runs.md#hum02up) | [hum02uhp](./runs.md#hum02uhp)

??? abstract "Abstract"
	
	Hummingbird participated in the named page finding task of the TREC 2002 Web Track (find the named page in 18GB from the .GOV domain) and the monolingual Arabic topic relevance task of the TREC 2002 Cross-Language Track (find all relevant documents in 869MB of Arabic news data). In the named page finding task, SearchServer returned the named page in the first 10 rows for more than 80% of the 150 queries. Searching the full document content produced mean reciprocal rank (MRR) scores more than 20 points higher than just searching particular HTML properties (such as the Title), but enhancing a content search with a little extra weight for HTML properties further increased MRR by 6 points (with standard error of just 2 points). Treating queries as phrases was not found to help significantly (on average), but document length normalization increased MRR by more than 20 points. For Arabic topic relevance, light algorithmic stemming increased mean average precision (MAP) by 5 points, use of Arabic stop words increased MAP by 1 point, and query expansion from blind feedback increased MAP by 3 points.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson02,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Named Page Finding and Arabic Retrieval with Hummingbird SearchServerTM at {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/hummingbird.tomlinson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2002 Web Track "Automated Word Sense Disambiguation for Internet  Information Retrieval"

_Christopher Stokoe, John Tait_

- :fontawesome-solid-user-group: **Participant:** [dgic_stokoe](./participants.md#dgic_stokoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/usunderland.stokoe.pdf](http://trec.nist.gov/pubs/trec11/papers/usunderland.stokoe.pdf)
- :material-file-search: **Runs:** [TDtfidf](./runs.md#tdtfidf) | [TDwsdtfidf](./runs.md#tdwsdtfidf)

??? abstract "Abstract"
	
	We describe an attempt to use automated word sense disambiguation to improve the performance of an internet information retrieval system. A performance comparison of term frequency verses word sense frequency was carried out, the results of which indicated no significant performance gains from using a sense based retrieval model instead of the traditional TF*IDF.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StokoeT02.bib) "
	```
	@inproceedings{DBLP:conf/trec/StokoeT02,
		author = {Christopher Stokoe and John Tait},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2002 Web Track "Automated Word Sense Disambiguation for Internet Information Retrieval"},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/usunderland.stokoe.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StokoeT02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Web Document Retrieval Using Sentence-Query Similarity

_Eui-Kyu Park, Seong-In Moon, Dong-Yul Ra, Myung-Gil Jang_

- :fontawesome-solid-user-group: **Participant:** [yonsei](./participants.md#yonsei)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/yonsei.ra.pdf](http://trec.nist.gov/pubs/trec11/papers/yonsei.ra.pdf)
- :material-file-search: **Runs:** [yenp01](./runs.md#yenp01) | [yedi01](./runs.md#yedi01) | [yedi01no](./runs.md#yedi01no)

??? abstract "Abstract"
	
	For the web document retrieval experiments in our TREC '2002 participation, we used two new methods. One is the use of anchor texts, which has been advocated by many researchers. But the methods used by them is different from our method. The second is the use of sentence-query similarity. It has been known that the use of links for web retrieval did not show impressive improvement in performance [5,6,8,9]. But Bailey, etc. [1] reported that using anchor texts can improve retrieval performance. However, our home page finding experiment done for TREC '2001 showed that it is not the case. The use of anchor texts did not allow any improvement in performance. Our method to use the anchor texts this year is changed a lot from last year and found that it is pretty effective. The major focus of our experiment this year is in the use of sentential information in information retrieval. We obtain similarity values between sentences of a document and the query and use them for computing the retrieval score of the document. The main idea is the following: a sentence in a document that is much relevant to the query can support relevance of the document to the query. We compute the similarity between each sentence in the document and the query. The degree of this similarity is incorporated in calculating the document's score (in addition to the similarity between the document as a whole and the query). It has been found that it does not take too much time for this extra processing. Our experiment showed that including the sentential information in the proposed way can significantly improve retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ParkMRJ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/ParkMRJ02,
		author = {Eui{-}Kyu Park and Seong{-}In Moon and Dong{-}Yul Ra and Myung{-}Gil Jang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Web Document Retrieval Using Sentence-Query Similarity},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/yonsei.ra.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ParkMRJ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at TREC 2002

_Christof Monz, Jaap Kamps, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uva](./participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf](http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf)
- :material-file-search: **Runs:** [UAmsT02WnA](./runs.md#uamst02wna) | [UAmsT02WnTl](./runs.md#uamst02wntl) | [UAmsT02WnTlA](./runs.md#uamst02wntla) | [UAmsT02WnTm](./runs.md#uamst02wntm) | [UAmsT02WnTmA](./runs.md#uamst02wntma) | [UAmsT02WtA](./runs.md#uamst02wta) | [UAmsT02WtAcs](./runs.md#uamst02wtacs) | [UAmsT02WtAri](./runs.md#uamst02wtari) | [UAmsT02WtT](./runs.md#uamst02wtt) | [UAmsT02WtTri](./runs.md#uamst02wttri)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2002 Novelty, Question answering, and Web tracks. We provide a detailed account of the ideas underlying our approaches to these tasks. All our runs used the FlexIR information retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MonzKR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MonzKR02,
		author = {Christof Monz and Jaap Kamps and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MonzKR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding Named Pages via Frequent Anchor Descriptions

_J. Malawong, Arnon Rungsawang_

- :fontawesome-solid-user-group: **Participant:** [kasetsart](./participants.md#kasetsart)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/kasetsart.malawong.pdf](http://trec.nist.gov/pubs/trec11/papers/kasetsart.malawong.pdf)
- :material-file-search: **Runs:** [KUHPF0201](./runs.md#kuhpf0201)

??? abstract "Abstract"
	
	This article describes about finding documents of interest via frequent anchor descriptions that being derived from the 'gov' web collection. The main idea of our approach is that we consider frequent anchor descriptions as documents. To find out the frequent item sets, we apply the Apri-ori algorithm with a new scoring criterion, called the maximum correspondence. We likewise integrate both retrieval scores calculated from anchor descriptions and title texts of the web pages to identify the resulting named pages, and foundthat these combination scores can boost the precision performance. Concluded from our preliminary experiments, this approach yields a considerable efficiency of named page finding in the aspect that it also highly reduces the document search space.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MalawongR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MalawongR02,
		author = {J. Malawong and Arnon Rungsawang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Finding Named Pages via Frequent Anchor Descriptions},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/kasetsart.malawong.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MalawongR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pliers at Trec 2002

_Andy MacFarlane_

- :fontawesome-solid-user-group: **Participant:** [city-pliers](./participants.md#city-pliers)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cityu.pliers.pdf](http://trec.nist.gov/pubs/trec11/papers/cityu.pliers.pdf)
- :material-file-search: **Runs:** [pltr02wt1](./runs.md#pltr02wt1) | [pltr02wt2](./runs.md#pltr02wt2) | [pltr02wt3](./runs.md#pltr02wt3) | [pltr02wt4](./runs.md#pltr02wt4) | [pltr02wt5](./runs.md#pltr02wt5) | [pltr02wt6](./runs.md#pltr02wt6) | [pltr02wt7](./runs.md#pltr02wt7) | [pltr02wt8](./runs.md#pltr02wt8) | [pltr02wt9](./runs.md#pltr02wt9)

??? abstract "Abstract"
	
	We report on our experiments for the TREC 2002 web track for both the topic distillation and named page tasks. We use a very simple method for both tasks which takes the first hit page in the top 10 for a give web site and discards any further pages from that web site (section 2 describes our research aims and objectives in more detail). We also describe indexing results (section 3), give a description of the runs and settings used (section 4), briefly describe our retrieval efficiency results in section 5, and outline our retrieval efficiency results in sections 6 and 7. A conclusion is given in section 8.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacFarlane02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacFarlane02,
		author = {Andy MacFarlane},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Pliers at Trec 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cityu.pliers.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacFarlane02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 11 Experiment: Arabic, Named Page and Topic Distillation  Searches

_Jacques Savoy, Yves Rasolofo_

- :fontawesome-solid-user-group: **Participant:** [Neuchatel](./participants.md#neuchatel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uneuchatel.pdf](http://trec.nist.gov/pubs/trec11/papers/uneuchatel.pdf)
- :material-file-search: **Runs:** [UniNEnp1](./runs.md#uninenp1) | [UniNEnp2](./runs.md#uninenp2) | [UniNEnp4](./runs.md#uninenp4) | [UniNEnp3](./runs.md#uninenp3) | [UniNEdi5](./runs.md#uninedi5) | [UniNEdi1](./runs.md#uninedi1) | [UniNEdi4](./runs.md#uninedi4) | [UniNEdi2](./runs.md#uninedi2) | [UniNEdi3](./runs.md#uninedi3)

??? abstract "Abstract"
	
	This year we took part in the Arabic cross-language information retrieval track (for us limited to monolingual Arabic retrieval) and also in both named page and topic distillation searches. In the last two tasks, we made use of link anchor information and document content in order to construct Web page representatives. This document representation uses multi-vectors in order to highlight the importance of both link anchor information and document content.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavoyR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavoyR02,
		author = {Jacques Savoy and Yves Rasolofo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 11 Experiment: Arabic, Named Page and Topic Distillation Searches},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uneuchatel.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SavoyR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Topic Distillation with Knowledge Agents

_Einat Amitay, David Carmel, Adam Darlow, Ronny Lempel, Aya Soffer_

- :fontawesome-solid-user-group: **Participant:** [IBM-Haifa](./participants.md#ibm-haifa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ibm-haifa.pdf](http://trec.nist.gov/pubs/trec11/papers/ibm-haifa.pdf)
- :material-file-search: **Runs:** [ibmHaifaBase](./runs.md#ibmhaifabase) | [ibmHaifaAP](./runs.md#ibmhaifaap) | [ibmHaifaT10](./runs.md#ibmhaifat10) | [ibmHaifaPR](./runs.md#ibmhaifapr) | [ibmHaifaT10D](./runs.md#ibmhaifat10d)

??? abstract "Abstract"
	
	This is the second year that our group participates in TREC's Web track. Our experiments focused on the Topic distillation task. Our main goal was to experiment with the Knowledge Agent (KA) technology [1], previously developed at our Lab, for this particular task. The knowledge agent approach was designed to enhance Web search results by utilizing domain knowledge. We first describe the generic KA approach and then articulate on the use of this technology in the context of the topic distillation task. We focus mainly on the Knowledge Agent features that were used in this task. The rest of this paper is organized as follows: Section 2 describes KA in general. In Section 3 we describe how KA was used for the topic distillation experiment. Section 4 describes the obtained results. Section 5 concludes.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmitayCDLS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmitayCDLS02,
		author = {Einat Amitay and David Carmel and Adam Darlow and Ronny Lempel and Aya Soffer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Topic Distillation with Knowledge Agents},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ibm-haifa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmitayCDLS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

