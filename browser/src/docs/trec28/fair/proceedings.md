# Proceedings - Fair Ranking 2019 

#### Fair ranking in academic search - Notebook for the TREC 2019 Fair  Ranking Track

_Malte Bonart_

- :fontawesome-solid-user-group: **Participant:** [IR-Cologne](./participants.md#ir-cologne)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/IR-Cologne.FR.pdf](https://trec.nist.gov/pubs/trec28/papers/IR-Cologne.FR.pdf)
- :material-file-search: **Runs:** [fair_random](./runs.md#fair_random) | [fair_LambdaMART](./runs.md#fair_lambdamart)

??? abstract "Abstract"
	
	This notebook summarizes our participation in the first Fair Ranking Track at TREC 2019 [ 2 ]. We shortly introduce the problem setting, give an overview of the software framework, and discuss the task and the results of our two submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bonart19.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bonart19,
		author = {Malte Bonart},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Fair ranking in academic search - Notebook for the {TREC} 2019 Fair Ranking Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/IR-Cologne.FR.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bonart19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team and Naver Labs Europe at TREC  2019 Fair Ranking Track

_Graham McDonald, Iadh Ounis, Craig Macdonald, Thibaut Thonet, Jean-Michel Renders_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/uogTr.FR.pdf](https://trec.nist.gov/pubs/trec28/papers/uogTr.FR.pdf)
- :material-file-search: **Runs:** [uognleMaxUtil](./runs.md#uognlemaxutil) | [uognleSgbrFair](./runs.md#uognlesgbrfair) | [uognleSgbrUtil](./runs.md#uognlesgbrutil) | [uognleDivAAsp](./runs.md#uognledivaasp) | [uognleDivAJc](./runs.md#uognledivajc)

??? abstract "Abstract"
	
	In our participation to the TREC 2019 Fair Ranking Track, the University of Glasgow Terrier Team and Naver Labs Europe joined forces to investigate (1) a novel probabilistic retrieval strategy that maximises the utility of the ranking, (2) two greedy brute-force re-ranking approaches that build on our novel probabilistic retrieval strategy and enforce individual fairness before adopting a particular trade-off between the utility and the fairness of the ranking, and (3) two approaches that deploy search results diversification as a fairness component to diversify over multiple possible dimensions of the task's unknown author groupings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McDonaldOMTR19.bib) "
	```
	@inproceedings{DBLP:conf/trec/McDonaldOMTR19,
		author = {Graham McDonald and Iadh Ounis and Craig Macdonald and Thibaut Thonet and Jean{-}Michel Renders},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow Terrier Team and Naver Labs Europe at {TREC} 2019 Fair Ranking Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/uogTr.FR.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McDonaldOMTR19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Testing Fairness Using the Log-likelihood Ratio

_Massimo Melucci_

- :fontawesome-solid-user-group: **Participant:** [QUARTZ_ITN](./participants.md#quartz_itn)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/DUTIR.FR.pdf](https://trec.nist.gov/pubs/trec28/papers/DUTIR.FR.pdf)
- :material-file-search: **Runs:** [QUARTZ-e0.00001](./runs.md#quartz-e0.00001) | [QUARTZ-e0.00010](./runs.md#quartz-e0.00010) | [QUARTZ-e0.00100](./runs.md#quartz-e0.00100) | [QUARTZ-e0.00200](./runs.md#quartz-e0.00200) | [QUARTZ-e0.00500](./runs.md#quartz-e0.00500) | [QUARTZ-e0.01000](./runs.md#quartz-e0.01000)

??? abstract "Abstract"
	
	The test collection was indexed by ElasticSearch [1]. The default indexing configuration was utilized. The JSON files were opened and each record was processed for all files by using json.loads. If a valid document identifier was found in the record, the document was added to the index by using elasticsearch. Elasticsearch.index for the document body.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Melucci19.bib) "
	```
	@inproceedings{DBLP:conf/trec/Melucci19,
		author = {Massimo Melucci},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Testing Fairness Using the Log-likelihood Ratio},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/DUTIR.FR.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Melucci19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICT at TREC 2019: Fair Ranking Track

_Meng Wang, Haopeng Zhang, Fuhuai Liang, Bin Feng, Di Zhao_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.FR.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.FR.pdf)
- :material-file-search: **Runs:** [first](./runs.md#first)

??? abstract "Abstract"
	
	In this paper, we will introduce our work in the 2019 TREC fair ranking task. In temporal academic search, more and more people choose to pay attention to the fairness constraints of ranking. The purpose of this task is to provide fairness exposure to different groups of authors, where the definition of group is diverse, such as based on demographics, height, topics, etc. For this reason, the model we design should consider the fairness of the ranking results while ensuring the relevance of the ranking results. We will show how to use our model to achieve the relevance of query results, then adjust the overall ranking results according to the fairness of documents, and finally achieve the relevance and fairness of document ordering. This paper will introduce the framework and methods of the fair ranking system, as well as the experimental results
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangZLFZ19.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangZLFZ19,
		author = {Meng Wang and Haopeng Zhang and Fuhuai Liang and Bin Feng and Di Zhao},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICT} at {TREC} 2019: Fair Ranking Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ICTNET.FR.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangZLFZ19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

