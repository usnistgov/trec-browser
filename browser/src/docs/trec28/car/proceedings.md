# Proceedings - Complex Answer Retrieval 2019 

#### TREC CAR Y3: Complex Answer Retrieval Overview

_Laura Dietz, John Foley_

- :material-file-pdf-box: **Paper:** [https://trec-car.cs.unh.edu/results-Y3/trec-car-overview-2019.pdf](https://trec-car.cs.unh.edu/results-Y3/trec-car-overview-2019.pdf)
??? abstract "Abstract"
	
	The vision of TREC Complex Answer Retrieval is to create complex long-form answers in response to a wide-variety information needs. In general, we aspire to create answers that are reminiscent to Wikipedia articles or school text books (e.g. TQA). However, while the vast majority of Wikipedia articles are about people, in TREC CAR we aim at information needs that are off the beaten path, covering topics in popular science, technology, and illnesses. The first two years of TREC CAR, we aimed to reproduce Wikipedia articles. This provided a very large-scale automated benchmark, which had significant impact on neural ranking research [7, 6], as well as feature-based ranking models [1, 4]. The downside was that we had to prohibit access to Wikipedia, collections that could include Wikipedia (e.g. ClueWeb), and knowledge bases derived from Wikipedia (we provided the part of Wikipedia from which a knowledge graph can be built that excludes the benchmark topics, called “allButBenchmark”). Technically this would even affect resources that are trained on Wikipedia, such as most word embeddings and BERT [3]. To avoid this difficulty, in this year, our test topics come exclusively from an collection of school text book chapters, which are provided along with the TQA dataset [5]. These chapters have a similar length as Wikipedia articles, but are written for a younger audience. We derive outlines from TQA chapters, and ask participants to populate these outlines with paragraphs from Wikipedia, using the paragraphCorpus from previous years. We manually cleaned and rewrote the outlines so that they are suitable to be treated like search queries. This test collection is called benchmarkY3test. A downside of this decision is that no automatic evaluation can be conducted. We recommend to train data-hungry methods on the “train” collection provided in the first year (Y1). Since previous year's test data (benchmarkY2test ) contained both contained Wikipedia topics and TQA topics, we re-released manually assessed TQA topics as training data for this year, released as benchmarkY3train.
	

??? quote "Bibtex [:material-link-variant:]() "
	```
	@inproceedings{dietz2019trec,
		title = {{TREC} {CAR} {Y3}: Complex Answer Retrieval Overview},
		author = {Laura Dietz and John Foley},
		booktitle = {Proceedings of Text REtrieval Conference (TREC)},
		url = {https://trec-car.cs.unh.edu/results-Y3/trec-car-overview-2019.pdf},
		biburl = {},
		year = {2019}
	}
	```

#### IRIT at TREC 2019: Incident Streams and Complex Answer Retrieval  Tracks

_Alexis Dusart, Gilles Hubert, Karen Pinel-Sauvagnat_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/IRIT.IS.CAR.pdf](https://trec.nist.gov/pubs/trec28/papers/IRIT.IS.CAR.pdf)
- :material-file-search: **Runs:** [IRIT_run1](./runs.md#irit_run1) | [IRIT_run2](./runs.md#irit_run2) | [IRIT_run3](./runs.md#irit_run3)

??? abstract "Abstract"
	
	This paper presents the approaches proposed by the IRIS team of the IRIT laboratory for the TREC Incident Streams and Complex Answer Retrieval tracks. The Incident Streams (IS) track aims to categorize and prioritize tweets in disaster situation to assist emergency service operators. In our participation, we applied supervised learning techniques based on features extracted from tweets. Then, the 2019 edition of the Complex Answer Retrieval (CAR) track aims to answer complex questions expressed as outlines using paragraphs from Wikipedia. In our participation, we used the Terrier retrieval system to rank paragraphs for each section of the outline and keep the most relevant according to three different strategies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DusartHP19.bib) "
	```
	@inproceedings{DBLP:conf/trec/DusartHP19,
		author = {Alexis Dusart and Gilles Hubert and Karen Pinel{-}Sauvagnat},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IRIT} at {TREC} 2019: Incident Streams and Complex Answer Retrieval Tracks},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/IRIT.IS.CAR.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DusartHP19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at TREC 2019 Complex Answer Retrieval Track

_Hongfei Ren, Ruibin Xiong, Yutao Zeng, Jiangui Chen, Yinqiong Cai, Haoquan Jiang_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.CAR.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.CAR.pdf)
- :material-file-search: **Runs:** [ICT-BM25](./runs.md#ict-bm25) | [Bert-DRMMTKS](./runs.md#bert-drmmtks) | [Bert-ConvKNRM](./runs.md#bert-convknrm) | [ICT-DRMMTKS](./runs.md#ict-drmmtks) | [Bert-ConvKNRM-50](./runs.md#bert-convknrm-50)

??? abstract "Abstract"
	
	We participate in the Complex Answer Retrieval(CAR) track at TREC 2019. We applied several useful models in this work. In the rough ranking, we applied doc2query model to predict queries and retrieve using BM25. In the re-ranking, we submitted 5 different runs which use 5 different models, include BM25, DRMMTKS, Bert-DRMMTKS, Bert-ConvKNRM and Bert-ConvKNRM-50, to try to get the best result
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RenXZCCJ19.bib) "
	```
	@inproceedings{DBLP:conf/trec/RenXZCCJ19,
		author = {Hongfei Ren and Ruibin Xiong and Yutao Zeng and Jiangui Chen and Yinqiong Cai and Haoquan Jiang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at {TREC} 2019 Complex Answer Retrieval Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ICTNET.CAR.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RenXZCCJ19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Amsterdam at the TREC 2019 Complex Answer Retrieval  Track

_Mahsa S. Shahshahani, Jaap Kamps, Maarten Marx_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UAmsterdam.CAR.pdf](https://trec.nist.gov/pubs/trec28/papers/UAmsterdam.CAR.pdf)
- :material-file-search: **Runs:** [UvABottomUp1](./runs.md#uvabottomup1) | [UvABottomUp2](./runs.md#uvabottomup2) | [UvABM25RM3](./runs.md#uvabm25rm3) | [UvABottomUpChangeOrder](./runs.md#uvabottomupchangeorder)

??? abstract "Abstract"
	
	This paper documents the University of Amsterdam's participation in the TREC 2019 Complex Answer Retrieval Track. This is the first year we actively participate in TREC CAR, attracted by the introduction to the limited “budget” of 20 passages per heading in the outline. We conducted initial exploratory experiments on making each heading contain a unique set of passages within the outline, and even do this hierarchical for each subtree and main title/article level, hence remove any redundancy between passages for different “queries” within the same title. We experimented with top-down and bottom-up filtering approaches. At the time of writing we are still in the process of analyzing the results. Some initial observations are the following. First, the restriction makes the task very challenging, as assigning any passage to the right heading in the outline is highly non-trivial. Qualitative analysis shows that our simple heuristics often make a different decision than the editorial judges on the heading under which a passage relevant to the title's topic is assigned. Second, the fraction of judged and relevant passages per individual query or leave node is very small, making it hard to draw any definite conclusions on our experiments, and also resulting in a too small recall base to evaluate our non-pooled runs in a meaningful way. Third, when aggregating all qrels and runs to the title level, there is reasonable effectiveness of the underlying BM25 rankings, showing that the underlying passage ranking is not unreasonable, and that the hard and interesting problem is in the exact assignment of passages to the “right” headings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShahshahaniKM19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShahshahaniKM19,
		author = {Mahsa S. Shahshahani and Jaap Kamps and Maarten Marx},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Amsterdam at the {TREC} 2019 Complex Answer Retrieval Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UAmsterdam.CAR.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShahshahaniKM19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREMA-UNH at CAR 2019

_Jordan Ramsdell, Sumanta Kashyapi, Shubham Chatterjee, Pooja Oza, Laura Dietz_

- :fontawesome-solid-user-group: **Participant:** [TREMA-UNH](./participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf](https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf)
- :material-file-search: **Runs:** [neural](./runs.md#neural) | [UNH-bm25-rm](./runs.md#unh-bm25-rm) | [UNH-bm25-ecmpsg](./runs.md#unh-bm25-ecmpsg) | [UNH-tfidf-ptsim](./runs.md#unh-tfidf-ptsim) | [UNH-ecn](./runs.md#unh-ecn) | [UNH-qee](./runs.md#unh-qee) | [UNH-tfidf-stem](./runs.md#unh-tfidf-stem) | [UNH-dl300](./runs.md#unh-dl300) | [UNH-dl100](./runs.md#unh-dl100) | [UNH-bm25-stem](./runs.md#unh-bm25-stem) | [UNH-tfidf-lem](./runs.md#unh-tfidf-lem)

??? abstract "Abstract"
	
	This notebook describes the submissions of team TREMA-UNH to the TREC Complex Answer Retrieval, TREC News, TREC Conversational Assistance, and TREC Deep Learning tracks in 2019. We explore passage retrieval systems, passage similarity metrics, and neural network methods that address the task statements of these tracks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RamsdellKCOD19.bib) "
	```
	@inproceedings{DBLP:conf/trec/RamsdellKCOD19,
		author = {Jordan Ramsdell and Sumanta Kashyapi and Shubham Chatterjee and Pooja Oza and Laura Dietz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREMA-UNH} at {CAR} 2019},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf},
		timestamp = {Tue, 21 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RamsdellKCOD19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

