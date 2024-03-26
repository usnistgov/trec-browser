# Proceedings 2019 

## Complex Answer Retrieval 

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

- :fontawesome-solid-user-group: **Participant:** [IRIT](./car/participants.md#irit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/IRIT.IS.CAR.pdf](https://trec.nist.gov/pubs/trec28/papers/IRIT.IS.CAR.pdf)
- :material-file-search: **Runs:** [IRIT_run1](./car/runs.md#irit_run1) | [IRIT_run2](./car/runs.md#irit_run2) | [IRIT_run3](./car/runs.md#irit_run3)

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

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./car/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.CAR.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.CAR.pdf)
- :material-file-search: **Runs:** [ICT-BM25](./car/runs.md#ict-bm25) | [Bert-DRMMTKS](./car/runs.md#bert-drmmtks) | [Bert-ConvKNRM](./car/runs.md#bert-convknrm) | [ICT-DRMMTKS](./car/runs.md#ict-drmmtks) | [Bert-ConvKNRM-50](./car/runs.md#bert-convknrm-50)

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

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./car/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UAmsterdam.CAR.pdf](https://trec.nist.gov/pubs/trec28/papers/UAmsterdam.CAR.pdf)
- :material-file-search: **Runs:** [UvABottomUp1](./car/runs.md#uvabottomup1) | [UvABottomUp2](./car/runs.md#uvabottomup2) | [UvABM25RM3](./car/runs.md#uvabm25rm3) | [UvABottomUpChangeOrder](./car/runs.md#uvabottomupchangeorder)

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

- :fontawesome-solid-user-group: **Participant:** [TREMA-UNH](./car/participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf](https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf)
- :material-file-search: **Runs:** [neural](./car/runs.md#neural) | [UNH-bm25-rm](./car/runs.md#unh-bm25-rm) | [UNH-bm25-ecmpsg](./car/runs.md#unh-bm25-ecmpsg) | [UNH-tfidf-ptsim](./car/runs.md#unh-tfidf-ptsim) | [UNH-ecn](./car/runs.md#unh-ecn) | [UNH-qee](./car/runs.md#unh-qee) | [UNH-tfidf-stem](./car/runs.md#unh-tfidf-stem) | [UNH-dl300](./car/runs.md#unh-dl300) | [UNH-dl100](./car/runs.md#unh-dl100) | [UNH-bm25-stem](./car/runs.md#unh-bm25-stem) | [UNH-tfidf-lem](./car/runs.md#unh-tfidf-lem)

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

## Deep Learning 

#### ICTNET at TREC 2019 Deep Learning Track

_Jiangui Chen, Yinqiong Cai, Haoquan Jiang_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./deep/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.DL.pdf)
- :material-file-search: **Runs:** [ICT-CKNRM_B](./deep/runs.md#ict-cknrm_b) | [ICT-CKNRM_B50](./deep/runs.md#ict-cknrm_b50) | [ICT-BERT2](./deep/runs.md#ict-bert2)

??? abstract "Abstract"
	
	We participated in the Deep Learning Track at TREC 2019. We built a ranking system which combines a search component based on BM25 and a semantic matching component using pretraining knowledge. Our best run achieves NDCG@10 of 0.6650, MAP of 0.2035.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenCJ19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenCJ19,
		author = {Jiangui Chen and Yinqiong Cai and Haoquan Jiang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at {TREC} 2019 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ICTNET.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenCJ19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCAS at TREC-2019 Deep Learning Track

_Xuanang Chen, Canjia Li, Ben He, Yingfei Sun_

- :fontawesome-solid-user-group: **Participant:** [UCAS](./deep/participants.md#ucas)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UCAS.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/UCAS.DL.pdf)
- :material-file-search: **Runs:** [ucas_runid1](./deep/runs.md#ucas_runid1) | [ucas_runid2](./deep/runs.md#ucas_runid2) | [ucas_runid3](./deep/runs.md#ucas_runid3)

??? abstract "Abstract"
	
	This paper describes the experiment conducted for our participation in the TREC-2019 Deep Learning track [1]. We test the effectiveness of two pre-trained language models, BERT [2] and XLNet [3], for the re-ranking subtask of the document ranking task, with an adoption of the passage-level document ranking approach as proposed in [4]. Our preliminary results indicate that the uses of BERT and XLNet lead to comparable performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenLHS19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenLHS19,
		author = {Xuanang Chen and Canjia Li and Ben He and Yingfei Sun},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UCAS} at {TREC-2019} Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UCAS.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenLHS19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Evaluation of Weakly-Supervised DeepCT in the TREC 2019 Deep  Learning Track

_Zhuyun Dai, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU](./deep/participants.md#cmu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CMU.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/CMU.DL.pdf)
- :material-file-search: **Runs:** [dct_qp_bm25e](./deep/runs.md#dct_qp_bm25e) | [dct_tp_bm25e2](./deep/runs.md#dct_tp_bm25e2) | [dct_tp_bm25e](./deep/runs.md#dct_tp_bm25e)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2019 Deep Learning Track document ranking task. We developed a deep learning based document term weighting approach based on our previous work of DeepCT. It used the contextualized token embeddings generated by BERT to estimate a term's importance in passages, and combines passage term weights into document-level term weights. The weighted document is stored in an ordinary inverted index and searched using a multi-field BM25, which is efficient. We tested two ways of training DeepCT: a query-based method using sparse relevant query-document pairs, and a weakly-supervised method using document title-body pairs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DaiC19.bib) "
	```
	@inproceedings{DBLP:conf/trec/DaiC19,
		author = {Zhuyun Dai and Jamie Callan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {An Evaluation of Weakly-Supervised DeepCT in the {TREC} 2019 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CMU.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DaiC19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TUA1 at the TREC 2019: Deep Learning Track

_Yun Gao, Xin Kang, Fuji Ren, Haitao Yu_

- :fontawesome-solid-user-group: **Participant:** [TUA1](./deep/participants.md#tua1)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/TUA1.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/TUA1.DL.pdf)
- :material-file-search: **Runs:** [TUA1-1](./deep/runs.md#tua1-1)

??? abstract "Abstract"
	
	This paper details our participation in the TREC 2019 Deep Learning Track task including Passage Ranking task. In the Top-1000 Re-ranking subtask of Passage Ranking task, we performed passage ranking based on the technique of Conv-KNRM and BERT. In order to get a better ranking result, we divided the task into two stages. In the first stage we use Conv-KNRM model for initial ranking, then in the second stage we combine the results with a state-of-the-art BERT re-ranker.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaoKRY19.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaoKRY19,
		author = {Yun Gao and Xin Kang and Fuji Ren and Haitao Yu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TUA1} at the {TREC} 2019: Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/TUA1.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaoKRY19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TU Wien @ TREC Deep Learning '19 - Simple Contextualization for  Re-ranking

_Sebastian Hofstätter, Markus Zlabinger, Allan Hanbury_

- :fontawesome-solid-user-group: **Participant:** [TU-Vienna](./deep/participants.md#tu-vienna)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/TU-Vienna.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/TU-Vienna.DL.pdf)
- :material-file-search: **Runs:** [TUW19-p2-f](./deep/runs.md#tuw19-p2-f) | [TUW19-p2-re](./deep/runs.md#tuw19-p2-re) | [TUW19-d1-f](./deep/runs.md#tuw19-d1-f) | [TUW19-d1-re](./deep/runs.md#tuw19-d1-re) | [TUW19-p1-f](./deep/runs.md#tuw19-p1-f) | [TUW19-p1-re](./deep/runs.md#tuw19-p1-re) | [TUW19-p3-f](./deep/runs.md#tuw19-p3-f) | [TUW19-p3-re](./deep/runs.md#tuw19-p3-re) | [TUW19-d2-f](./deep/runs.md#tuw19-d2-f) | [TUW19-d2-re](./deep/runs.md#tuw19-d2-re) | [TUW19-d3-f](./deep/runs.md#tuw19-d3-f) | [TUW19-d3-re](./deep/runs.md#tuw19-d3-re)

??? abstract "Abstract"
	
	The usage of neural network models puts multiple objectives in conflict with each other: Ideally we would like to create a neural model that is effective, efficient, and interpretable at the same time. However, in most instances we have to choose which property is most important to us. We used the opportunity of the TREC 2019 Deep Learning track to evaluate the effectiveness of a balanced neural re-ranking approach. We submitted results of the TK (Transformer-Kernel) model: a neural re-ranking model for ad-hoc search using an efficient contextualization mechanism. TK employs a very small number of lightweight Transformer layers to contextualize query and document word embeddings. To score individual term interactions, we use a document-length enhanced kernel-pooling, which enables users to gain insight into the model. Our best result for the passage ranking task is: 0.420 MAP, 0.671 nDCG, 0.598 P@10 (TUW19-p3 full). Our best result for the document ranking task is: 0.271 MAP, 0.465 nDCG, 0.730 P@10 (TUW19-d3 re-ranking).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HofstatterZH19.bib) "
	```
	@inproceedings{DBLP:conf/trec/HofstatterZH19,
		author = {Sebastian Hofst{\"{a}}tter and Markus Zlabinger and Allan Hanbury},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TU} Wien @ {TREC} Deep Learning '19 - Simple Contextualization for Re-ranking},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/TU-Vienna.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HofstatterZH19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CCNU_IRGroup @ TREC 2019 Deep Learning Track

_Hao Hu, Junmei Wang, Xinhui Tu, Tingting He_

- :fontawesome-solid-user-group: **Participant:** [CCNU_IRGroup](./deep/participants.md#ccnu_irgroup)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CCNU_IRGroup.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/CCNU_IRGroup.DL.pdf)
- :material-file-search: **Runs:** [runid1](./deep/runs.md#runid1) | [runid2](./deep/runs.md#runid2) | [runid5](./deep/runs.md#runid5)

??? abstract "Abstract"
	
	The deep learning track consists of two tasks: passage ranking and document ranking. The former focuses on long text retrieval, while the latter focuses on short text retrieval. Both tasks use a large human-labeled set, which is from the MS-MARCO dataset. For different emphases of the two tasks, we adopt two different BERT-based retrieval models. In Section 2 and 3, we will introduce our methods in details. In Section 4 and 5, we will discuss the experiments setting and results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuWTH19.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuWTH19,
		author = {Hao Hu and Junmei Wang and Xinhui Tu and Tingting He},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {CCNU{\_}IRGroup @ {TREC} 2019 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CCNU\_IRGroup.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HuWTH19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SIB Text Mining at TREC 2019 Deep Learning Track: Working Note

_Julien Knafou, Matt Jeffryes, Luc Mottin, Douglas Teodoro, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BITEM_DL](./deep/participants.md#bitem_dl)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/BITEM_DL.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/BITEM_DL.DL.pdf)
- :material-file-search: **Runs:** [baseline](./deep/runs.md#baseline) | [query2doc_RNN](./deep/runs.md#query2doc_rnn)

??? abstract "Abstract"
	
	The TREC 2019 Deep Learning task aims at studying information retrieval in a large training data regime. It includes two tasks: the document ranking task (1) and the passage ranking task (2). Both of these tasks had a full ranking (a) and reranking (b) subtasks. The SIB Text Mining group participated at the full document ranking subtask (1a). In order to retrieve pertinent documents in the 3.2 million documents corpus, our strategy was two-fold. At first, we used a BM25 model to retrieve a subset of documents relevant to a query. We also tried to improve recall by using query expansion. The second step consisted in reranking the retrieved subset using an original model, so-called query2doc. This model, which has been designed to predict if a query-document pair was a good candidate to be ranked in position #1, was trained using the training dataset provided for the task. Our baseline, which is basically a BM25 ranking performed the best and achieve a MAP of 0.2892. Results of the query2doc run clearly indicates that the query2doc model could not learn any meaningful relationship. More precisely, to explain such a failure, we hypothesize that using documents returned by our baseline model as negative items confused our model. As future steps, it will be interesting to take into account features such as the document's BM25 score as well as the number of times a document's URL is mentioned in the corpus and use them along with learning to rank algorithms.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KnafouJMTR19.bib) "
	```
	@inproceedings{DBLP:conf/trec/KnafouJMTR19,
		author = {Julien Knafou and Matt Jeffryes and Luc Mottin and Douglas Teodoro and Patrick Ruch},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{SIB} Text Mining at {TREC} 2019 Deep Learning Track: Working Note},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/BITEM\_DL.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KnafouJMTR19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUET AT TREC 2019 DEEP LEARNING TRACK

_Bhaskar Mitra, Nick Craswell_

- :fontawesome-solid-user-group: **Participant:** [Microsoft](./deep/participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/Microsoft.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/Microsoft.DL.pdf)
- :material-file-search: **Runs:** [ms_duet](./deep/runs.md#ms_duet) | [ms_ensemble](./deep/runs.md#ms_ensemble) | [ms_duet_passage](./deep/runs.md#ms_duet_passage)

??? abstract "Abstract"
	
	This report discusses three submissions based on the Duet architecture to the Deep Learning track at TREC 2019. For the document retrieval task, we adapt the Duet model to ingest a “multiple field” view of documents—we refer to the new architecture as Duet with Multiple Fields (DuetMF). A second submission combines the DuetMF model with other neural and traditional relevance estimators in a learning-to-rank framework and achieves improved performance over the DuetMF baseline. For the passage retrieval task, we submit a single run based on an ensemble of eight Duet models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MitraC19.bib) "
	```
	@inproceedings{DBLP:conf/trec/MitraC19,
		author = {Bhaskar Mitra and Nick Craswell},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DUET} {AT} {TREC} 2019 {DEEP} {LEARNING} {TRACK}},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/Microsoft.DL.pdf},
		timestamp = {Wed, 27 Apr 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MitraC19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team at the TREC 2019 Deep Learning  Track

_Ting Su, Xi Wang, Craig Macdonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./deep/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/uogTr.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/uogTr.DL.pdf)
- :material-file-search: **Runs:** [uogTrDNN6LM](./deep/runs.md#uogtrdnn6lm) | [uogTrDSSQE5LM](./deep/runs.md#uogtrdssqe5lm) | [uogTrDSS6pLM](./deep/runs.md#uogtrdss6plm)

??? abstract "Abstract"
	
	For TREC 2019, we focus on combining deep learning methods with traditional information retrieval methods, by using deep learning scores as an extra feature in the re-ranking process. In particular, we explore the effectiveness of using deep learning techniques based on the state-of-the-art BERT contextual language models, as well as tak- ing into account alternative query reformulations in the re-ranking process. We submitted three official runs to the document ranking task: uogTrDNN6LM, uogTrDSS6pLM, and uogTrDSSQE5LM, where all three runs deploy a deep learning method and the LambdaMART learning-to-rank method. Our results show that uogTrDNN6LM is competitive, performing above the TREC median in terms of MAP and NDCG, yet a simple untrained DFR query expansion run was more effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SuWMO19.bib) "
	```
	@inproceedings{DBLP:conf/trec/SuWMO19,
		author = {Ting Su and Xi Wang and Craig Macdonald and Iadh Ounis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow Terrier Team at the {TREC} 2019 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/uogTr.DL.pdf},
		timestamp = {Tue, 04 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SuWMO19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IDST at TREC 2019 Deep Learning Track: Deep Cascade Ranking with  Generation-based Document Expansion and Pre-trained Language Modeling

_Ming Yan, Chenliang Li, Chen Wu, Bin Bi, Wei Wang, Jiangnan Xia, Luo Si_

- :fontawesome-solid-user-group: **Participant:** [IDST](./deep/participants.md#idst)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/IDST.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/IDST.DL.pdf)
- :material-file-search: **Runs:** [idst_bert_v1](./deep/runs.md#idst_bert_v1) | [idst_bert_v2](./deep/runs.md#idst_bert_v2) | [idst_bert_r1](./deep/runs.md#idst_bert_r1) | [idst_bert_r2](./deep/runs.md#idst_bert_r2) | [idst_bert_v3](./deep/runs.md#idst_bert_v3) | [idst_bert_p1](./deep/runs.md#idst_bert_p1) | [idst_bert_p2](./deep/runs.md#idst_bert_p2) | [idst_bert_p3](./deep/runs.md#idst_bert_p3) | [idst_bert_pr1](./deep/runs.md#idst_bert_pr1) | [idst_bert_pr2](./deep/runs.md#idst_bert_pr2)

??? abstract "Abstract"
	
	This paper describes our participation in the passage and document ranking tasks of TREC 2019 Deep Learning Track. We propose a two-stage cascade ranking pipeline by taking the advantages of sequence-to-sequence generation and pre-trained language modeling. Firstly, we use a simple and effective index-based method to retrieve a collection of candidate passages. To overcome the vocabulary mismatch problem, we propose a query generation method for document expansion based on the pointer-generator model, where each passage is expanded with a set of generated queries for higher recall in the retrieval of candidate passages. Then we pre-train a BERT language model with a new sentence prediction objective, and adopt a pointwise ranking strategy for re-ranking the remained candidate passages. Our cascade ranking method achieves the best results among all participants on both the passage ranking and document ranking tasks, according to the official evaluation metric NDCG@10.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YanLWBWXS19.bib) "
	```
	@inproceedings{DBLP:conf/trec/YanLWBWXS19,
		author = {Ming Yan and Chenliang Li and Chen Wu and Bin Bi and Wei Wang and Jiangnan Xia and Luo Si},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IDST} at {TREC} 2019 Deep Learning Track: Deep Cascade Ranking with Generation-based Document Expansion and Pre-trained Language Modeling},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/IDST.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YanLWBWXS19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Brown University at TREC Deep Learning 2019

_George Zerveas, Ruochen Zhang, Leila Kim, Carsten Eickhoff_

- :fontawesome-solid-user-group: **Participant:** [Brown](./deep/participants.md#brown)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/Brown.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/Brown.DL.pdf)
- :material-file-search: **Runs:** [test1](./deep/runs.md#test1)

??? abstract "Abstract"
	
	This paper describes Brown University's submission to the TREC 2019 Deep Learning track. We followed a 2-phase method for producing a ranking of passages for a given input query: In the the first phase, the user's query is expanded by appending 3 queries generated by a transformer model which was trained to rephrase an input query into semantically similar queries. The expanded query can exhibit greater similarity in surface form and vocabulary overlap with the passages of interest and can therefore serve as enriched input to any downstream information retrieval method. In the second phase, we use a BERT-based model pre-trained for language modeling but fine-tuned for query - document relevance prediction to compute relevance scores for a set of 1000 candidate passages per query and subsequently obtain a ranking of passages by sorting them based on the predicted relevance scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZerveasZKE19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZerveasZKE19,
		author = {George Zerveas and Ruochen Zhang and Leila Kim and Carsten Eickhoff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Brown University at {TREC} Deep Learning 2019},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/Brown.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZerveasZKE19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Higway BERT for Passage Ranking

_Di Zhao, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./deep/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/udel_fang.DL.pdf](https://trec.nist.gov/pubs/trec28/papers/udel_fang.DL.pdf)
- :material-file-search: **Runs:** [runid3](./deep/runs.md#runid3) | [runid4](./deep/runs.md#runid4)

??? abstract "Abstract"
	
	This is the first year of TREC for deep learning and there are two tasks which are document ranking and passage ranking. Our task is passage ranking which can be described as given a query q and the 1000 most relevant passages p1, p2, ..., p1000 retrieved by BM25, passage ranking task expects to come up with a successful system to rank the most relevant passage as high as possible. In this work, we build a neural network based IR model for the passage rank- ing tasks. Basically we are trying to combine BERT [2] and highway network [6] to get a good performance on the task. Since BERT is the current SOTA model on several nlp related tasks and highway network [6] is kind of neural network with gate structure, since gate structure has already shown its success on some neural network models like lstm [3] and gru [1] on sequence modeling tasks. So we assume combining multi-head attention based transformer with gate based network structure to improve the model performance can be achieved. Meanwhile we also try different loss functions and different training strategies also with axiomatic thinking [5] approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoF19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoF19,
		author = {Di Zhao and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Higway {BERT} for Passage Ranking},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/udel\_fang.DL.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoF19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Precision Medicine 

#### Overview of the TREC 2019 Precision Medicine Track

_Kirk Roberts, Dina Demner-Fushman, Ellen M. Voorhees, William R. Hersh, Steven Bedrick, Alexander J. Lazar, Shubham Pant, Funda Meric-Bernstam_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/OVERVIEW.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/OVERVIEW.PM.pdf)
??? abstract "Abstract"
	
	Precision medicine is a medical paradigm in which treatments are customized entirely to the individual patient. The underlying issue that drives precision medicine is that for many complex diseases, there are no “one size fits all” solutions for patients with a particular diagnosis. The proper treatment for a patient depends upon genetic, environmental, and lifestyle choices. The ability to personalize treatment in a scientifically rigorous manner based on these factors is thus the hallmark of the emerging precision medicine paradigm. Nowhere is the potential impact of precision medicine more closely focused at the moment than in cancer, where lifesaving treatments for particular patients could prove ineffective or even deadly for other patients based entirely upon the particular genetic mutations in the patient's tumor(s). Significant effort, therefore, has been devoted to deepening the scientific research surrounding precision medicine. This includes the Precision Medicine Initiative (Collins and Varmus, 2015) launched by President Barack Obama in 2015, now known as the All of Us Research Program. A fundamental difficulty with putting the findings of precision medicine into practice is that-by its very nature-precision medicine creates a very large space of treatment options (Frey et al., 2016). These can easily overwhelm clinicians attempting to stay up-to-date with the latest findings, and can easily inhibit a clinician's attempts to determine the best possible treatment for a particular patient. However, the ability to quickly locate relevant evidence is the hallmark of information retrieval (IR). [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsDVHBLPM19.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsDVHBLPM19,
		author = {Kirk Roberts and Dina Demner{-}Fushman and Ellen M. Voorhees and William R. Hersh and Steven Bedrick and Alexander J. Lazar and Shubham Pant and Funda Meric{-}Bernstam},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/OVERVIEW.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsDVHBLPM19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Brown University at TREC Precision Medicine 2019

_Abdullah Ahmed, Gil Alon, Bashar Zaidat, Isaac Nathoo, Hwai-Liang Tung, Charles Wang, Carsten Eickhoff_

- :fontawesome-solid-user-group: **Participant:** [Brown](./pm/participants.md#brown)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/Brown.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/Brown.PM.pdf)
- :material-file-search: **Runs:** [rrf_1](./pm/runs.md#rrf_1) | [rrf_2](./pm/runs.md#rrf_2) | [eged](./pm/runs.md#eged) | [egnd](./pm/runs.md#egnd) | [ngnd](./pm/runs.md#ngnd)

??? abstract "Abstract"
	
	This paper describes Brown University's submission to the TREC 2019 Precision Medicine (PM) track. We expand disease and gene name related terms, prune expanded queries and boost the importance of key terms. Our retrieval model is based on BM25F and incorporates heuristic relevance eligibility filters for clinical trials as well as reciprocal rank fusion of constituent runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AhmedAZNTWE19.bib) "
	```
	@inproceedings{DBLP:conf/trec/AhmedAZNTWE19,
		author = {Abdullah Ahmed and Gil Alon and Bashar Zaidat and Isaac Nathoo and Hwai{-}Liang Tung and Charles Wang and Carsten Eickhoff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Brown University at {TREC} Precision Medicine 2019},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/Brown.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AhmedAZNTWE19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Designing retrieval models to contrast precision-driven ad hoc search  vs. recall-driven treatment extraction in Precision Medicine

_Déborah Caucheteur, Emilie Pasche, Julien Gobeill, Anaïs Mottaz, Luc Mottin, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BITEM_PM](./pm/participants.md#bitem_pm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/BITEM_PM.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/BITEM_PM.PM.pdf)
- :material-file-search: **Runs:** [SIBTMct1](./pm/runs.md#sibtmct1) | [SIBTMct2](./pm/runs.md#sibtmct2) | [SIBTMct3](./pm/runs.md#sibtmct3) | [SIBTMct4](./pm/runs.md#sibtmct4) | [SIBTMct5](./pm/runs.md#sibtmct5) | [SIBTMlit1](./pm/runs.md#sibtmlit1) | [SIBTMlit3](./pm/runs.md#sibtmlit3) | [SIBTMlit2](./pm/runs.md#sibtmlit2) | [SIBTMlit5](./pm/runs.md#sibtmlit5) | [SIBTMlit4](./pm/runs.md#sibtmlit4)

??? abstract "Abstract"
	
	The TREC 2019 Precision Medicine Track repeats the general structure and evaluation of the 2018 track. Our team participated in both tasks of the track, relative to scientific abstracts and clinical trials. 40 topics where patient data are given (demographic data, disease, gene and genetic variant) were available for this competition. The aim was to retrieve scientific abstracts and clinical trials of interest regarding a topic, modelling the description of a clinical case. In the first task, we aim at retrieving scientific abstracts introducing some relevant treatments for a given case. Our system is first based on the collection of a large set of abstracts related to a particular case using various strategies such as search with keywords within abstracts, search with normalized entities within annotated abstracts and the linear combination of various queries. We then apply different strategies to re-rank the resulting scientific abstracts set. In particular, we tested two strategies to re-rank the abstracts set in order to have a large variety of treatments returned in the top articles. Almost two thirds of the top-10 returned documents are judged relevant, while nearly a quarter of the relevant treatments is returned in the top-10 abstracts. The second task aims at retrieving some clinical trials for which patients are eligible. Criteria used to determine the eligibility of patients are those found in the topics. Information such as trial location or status of clinical trials, which are important from a patient's point of view, are questionably not used in these topics. Several strategies have been tested, relaxing of constraints (data required or not), expansion of information requests thanks to synonyms or regex, and retrieval status value boosting for some criteria or fields. After judging, for almost half of the topics, a minimum of 50% of the documents retrieved are relevant, up to 90% for 10 of the 38 topics provided. Almost two thirds of the top-10 returned documents are judged relevant, while nearly a quarter of the relevant treatments is returned in the top-10 abstracts. Our best runs achieve highly competitive results depending on the measures, with on average being ranked #2 or #3 according to the official results for the literature task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaucheteurPGMMR19.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaucheteurPGMMR19,
		author = {D{\'{e}}borah Caucheteur and Emilie Pasche and Julien Gobeill and Ana{\"{\i}}s Mottaz and Luc Mottin and Patrick Ruch},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Designing retrieval models to contrast precision-driven ad hoc search vs. recall-driven treatment extraction in Precision Medicine},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/BITEM\_PM.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CaucheteurPGMMR19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Poznan Contribution to TREC-PM 2019

_Artur Cieslewicz, Jakub Dutkiewicz, Czeslaw Jedrzejek_

- :fontawesome-solid-user-group: **Participant:** [POZNAN](./pm/participants.md#poznan)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/Poznan.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/Poznan.PM.pdf)
- :material-file-search: **Runs:** [bc](./pm/runs.md#bc) | [w2v_noletor](./pm/runs.md#w2v_noletor) | [w2v_letor](./pm/runs.md#w2v_letor) | [simple_letor](./pm/runs.md#simple_letor) | [simple](./pm/runs.md#simple) | [SA_LGD_letor](./pm/runs.md#sa_lgd_letor) | [SA_DPH_letor](./pm/runs.md#sa_dph_letor) | [SAsimpleLGD](./pm/runs.md#sasimplelgd) | [SA_bc](./pm/runs.md#sa_bc)

??? abstract "Abstract"
	
	This paper describes Pozna´n contribution to the Precision Medicine track of the TREC 2019. In this submission we present several novelties. We cover the motivation for the hand-picked values of the weights assigned to the expanded query terms. We propose a result fusion method - slightly modified version of Borda Count algorithm. Additionally we use a learning to rank environment, we analyze the effectiveness of such an approach in combination with our other methods and analyze the achieved results. We also discuss our dedicated document processing methods. We achieve an improvement of up to 0.02 (infNDCG measure) over the baseline for Clinical Trials with our proposed methods, however the evaluation value of our baseline is much lower than the median of all contributions. The reverse effect happens in the Scientific Abstracts task, the baseline we propose is much stronger than the median, but the default setting of learning to rank proposition lowers the overall evaluation score.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CieslewiczDJ19.bib) "
	```
	@inproceedings{DBLP:conf/trec/CieslewiczDJ19,
		author = {Artur Cieslewicz and Jakub Dutkiewicz and Czeslaw Jedrzejek},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Poznan Contribution to {TREC-PM} 2019},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/Poznan.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CieslewiczDJ19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Deep Learning Approach for the Precision Medicine Track

_Juan Pablo Consuegra-Ayala, Giovanni Stilo, Alessandro Celi, Amleto Di Salle_

- :fontawesome-solid-user-group: **Participant:** [UNIVAQ](./pm/participants.md#univaq)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UNIVAQ.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/UNIVAQ.PM.pdf)
- :material-file-search: **Runs:** [tk1allfuzzy](./pm/runs.md#tk1allfuzzy) | [tk3allfuzzy](./pm/runs.md#tk3allfuzzy) | [tk1allbinary](./pm/runs.md#tk1allbinary) | [tk3nodemogr](./pm/runs.md#tk3nodemogr) | [tk3onlygnds](./pm/runs.md#tk3onlygnds) | [default100k](./pm/runs.md#default100k) | [default1m](./pm/runs.md#default1m)

??? abstract "Abstract"
	
	The paper describes the system presented by the University of L'Aquila in collaboration with the University of Havana - team named UNIVAQ - to the TREC 2019 Precision Medicine Track. The proposed solution, maps any kind of documents - Scientific Abstract, Clinical trials, and Topics - into a multi-dimensional common general representation. Each document is described by five primitive features. The values of each feature are extracted from the original documents using deep learning and machine learning text processing based techniques. To recognize Genes and Diseases, we have trained our models using the PubTator annotated corpus. Instead, to derive demographics information, we have trained the em- ployed deep learning models using the documents -obtained from the Relevance and Raw judgements of the past edition of TREC Precision Medicine / Clinical Decision Support Track 2018- considered “relevant” or “partially relevant”. The results of the Track clearly show that applying a system (as our) made solely by a tagging based approach to the Precision Medicine task, is not sufficient to achieve the performances gained by other systems presented in the TREC Precision Medicine Track 2019.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Consuegra-Ayala19.bib) "
	```
	@inproceedings{DBLP:conf/trec/Consuegra-Ayala19,
		author = {Juan Pablo Consuegra{-}Ayala and Giovanni Stilo and Alessandro Celi and Amleto Di Salle},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Deep Learning Approach for the Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UNIVAQ.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Consuegra-Ayala19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JULIE Lab & Med Uni Graz @ TREC 2019 Precision Medicine Track

_Erik Faessler, Udo Hahn, Michel Oleynik_

- :fontawesome-solid-user-group: **Participant:** [julie-mug](./pm/participants.md#julie-mug)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/julie-mug.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/julie-mug.PM.pdf)
- :material-file-search: **Runs:** [jlctphrase](./pm/runs.md#jlctphrase) | [jlpmtrcommon](./pm/runs.md#jlpmtrcommon) | [jlpmletor](./pm/runs.md#jlpmletor) | [jlpmltrin](./pm/runs.md#jlpmltrin) | [jlctletor](./pm/runs.md#jlctletor) | [jlctltrin](./pm/runs.md#jlctltrin) | [jlpmtrboost](./pm/runs.md#jlpmtrboost) | [jlctprec](./pm/runs.md#jlctprec) | [jlctgenes](./pm/runs.md#jlctgenes) | [jlpmcommon2](./pm/runs.md#jlpmcommon2)

??? abstract "Abstract"
	
	The 2019 Precision Medicine Track at TREC (TREC-PM) aimed at identifying relevant documents from two collections, namely PubMed (biomedical abstracts) and ClinicalTrials.gov (clinical trials), given 40 precision medicine topics representing (virtual) patients. The organizers also proposed a new subtask on treatment retrieval from PubMed. We describe our contributions based on five runs for each task, including two runs for the treatment subtask using a naïve strategy. Our approach builds upon carefully designed weighted queries based on our experience from last year's participation and explores the usefulness of Learning to Rank (LETOR), trained on either the previous official gold standards or an internal reference standard for the topics chosen for the 2019 challenge. Our best results culminated in infNDCG = 0.5783, P@10 = 0.6525, and R-Prec = 0.3572 for the biomedical abstracts task and infNDCG = 0.6451, P@10 = 0.5474, and R-Prec = 0.4814 for the clinical trials task, obtained with a baseline retrieval strategy. LETOR worsened our results, especially when using the internal reference standard.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FaesslerHO19.bib) "
	```
	@inproceedings{DBLP:conf/trec/FaesslerHO19,
		author = {Erik Faessler and Udo Hahn and Michel Oleynik},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{JULIE} Lab {\&} Med Uni Graz @ {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/julie-mug.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FaesslerHO19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2019: Precision Medicine Track

_Jingkun Feng, Zhihao Yang, Zhiqiang Liu, Ling Luo, Hongfei Lin, Jian Wang_

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./pm/participants.md#dutir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/DUTIR.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/DUTIR.PM.pdf)
- :material-file-search: **Runs:** [DutirRun1](./pm/runs.md#dutirrun1) | [DutirRun2](./pm/runs.md#dutirrun2) | [DutirRun3](./pm/runs.md#dutirrun3) | [DutirRun4](./pm/runs.md#dutirrun4) | [DutirRun5](./pm/runs.md#dutirrun5) | [Dutir_Cli1](./pm/runs.md#dutir_cli1) | [Dutir_Cli2](./pm/runs.md#dutir_cli2)

??? abstract "Abstract"
	
	This paper describes the system developed for the TREC 2019 Precision Medicine Track by the Team DUTIR from Dalian University of Technology. In the system, we applied a hybrid method to score the related documents for each topic. First, we used Elasticsearch, an open-source Lucene-based full-text search engine, to obtain the initial retrieval results. Then we trained several deep models using TREC 2017 PM data. Finally, we applied the pre-trained models to reorder the initial search results. The performance of our system is above the median for the scientific abstracts subtask and below median for the clinical trials subtask.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FengYLLLW19.bib) "
	```
	@inproceedings{DBLP:conf/trec/FengYLLLW19,
		author = {Jingkun Feng and Zhihao Yang and Zhiqiang Liu and Ling Luo and Hongfei Lin and Jian Wang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DUTIR} at {TREC} 2019: Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/DUTIR.PM.pdf},
		timestamp = {Mon, 03 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FengYLLLW19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CBNU at TREC 2019 Precision Medicine Track

_Seung-Hyeon Jo, Kyung-Soon Lee_

- :fontawesome-solid-user-group: **Participant:** [cbnu](./pm/participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/cbnu.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/cbnu.PM.pdf)
- :material-file-search: **Runs:** [cbnuCT1](./pm/runs.md#cbnuct1) | [cbnuCT2](./pm/runs.md#cbnuct2) | [cbnuCT3](./pm/runs.md#cbnuct3) | [cbnuCT4](./pm/runs.md#cbnuct4) | [cbnuSA1](./pm/runs.md#cbnusa1) | [cbnuSA2](./pm/runs.md#cbnusa2) | [cbnuSA3](./pm/runs.md#cbnusa3) | [cbnuSA4](./pm/runs.md#cbnusa4)

??? abstract "Abstract"
	
	This paper describes the participation of the CBNU team at the TREC Precision Medicine Track 2019. We use the cancer-centered document clusters based on graph embedding. Documents are retrieved by re-ranking documents and pseudo-relevance feedback based on cancer-centered document clusters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoL19.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoL19,
		author = {Seung{-}Hyeon Jo and Kyung{-}Soon Lee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CBNU} at {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/cbnu.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoL19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SCUT-CCNL at TREC 2019 Precision Medicine Track

_Xiaofeng Liu, Lu Li, Zuoxi Yang, Shoubin Dong_

- :fontawesome-solid-user-group: **Participant:** [CCNL](./pm/participants.md#ccnl)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CCNL.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/CCNL.PM.pdf)
- :material-file-search: **Runs:** [ccnl_trials1](./pm/runs.md#ccnl_trials1) | [ccnl_trials2](./pm/runs.md#ccnl_trials2) | [ccnl_sa1](./pm/runs.md#ccnl_sa1) | [ccnl_sa2](./pm/runs.md#ccnl_sa2) | [ccnl_sa3](./pm/runs.md#ccnl_sa3) | [ccnl_sa5](./pm/runs.md#ccnl_sa5) | [ccnl_sa4](./pm/runs.md#ccnl_sa4)

??? abstract "Abstract"
	
	This paper describes a retrieval system developed for the TREC 2019 Precision Medicine Track. For two tasks of Scientific Abstracts and Clinical Trials, we applied the same structure, including the retrieval model, the query expansion and the re-ranking model, to generate the final retrieval results. The experiment results show that the re-ranking model based on SciBERT is of great benefit for retrieval tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuLYD19.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuLYD19,
		author = {Xiaofeng Liu and Lu Li and Zuoxi Yang and Shoubin Dong},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{SCUT-CCNL} at {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CCNL.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuLYD19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2019 Precision Medicine - Medical University of Graz

_Pilar López-Úbeda, José Antonio Vera-Ramos, Pablo López-García_

- :fontawesome-solid-user-group: **Participant:** [imi_mug](./pm/participants.md#imi_mug)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/imi_mug.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/imi_mug.PM.pdf)
- :material-file-search: **Runs:** [imi_mug1](./pm/runs.md#imi_mug1) | [imi_mug2](./pm/runs.md#imi_mug2) | [imi_mug3](./pm/runs.md#imi_mug3) | [imi_mug2_t](./pm/runs.md#imi_mug2_t) | [imi_mug3_t](./pm/runs.md#imi_mug3_t)

??? abstract "Abstract"
	
	In this paper we report on our participation in the TREC 2019 Precision Medicine track (team name: imi_mug). We submitted 5 fully automatic runs to the biomedical articles subtask, two of them with treatments. Our system was based on Elasticsearch, templates, and parameter grid search query generation, building heavily on our previous participation and the reference standards from 2017 and 2018. Our results are close to the mean for the biomedical articles subtask.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lopez-UbedaVL19.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lopez-UbedaVL19,
		author = {Pilar L{\'{o}}pez{-}{\'{U}}beda and Jos{\'{e}} Antonio Vera{-}Ramos and Pablo L{\'{o}}pez{-}Garc{\'{\i}}a},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2019 Precision Medicine - Medical University of Graz},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/imi\_mug.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lopez-UbedaVL19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring how to Combine Query Reformulations for Precision Medicine

_Giorgio Maria Di Nunzio, Stefano Marchesin, Maristella Agosti_

- :fontawesome-solid-user-group: **Participant:** [ims_unipd](./pm/participants.md#ims_unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ims_unipd.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/ims_unipd.PM.pdf)
- :material-file-search: **Runs:** [BM25](./pm/runs.md#bm25) | [BM25neop01](./pm/runs.md#bm25neop01) | [BM25neopcomd](./pm/runs.md#bm25neopcomd) | [BM25neopgngm](./pm/runs.md#bm25neopgngm) | [top4fusion](./pm/runs.md#top4fusion) | [BM25ct](./pm/runs.md#bm25ct) | [BM25neop01r](./pm/runs.md#bm25neop01r) | [BM25solid01o](./pm/runs.md#bm25solid01o) | [BM25solid01r](./pm/runs.md#bm25solid01r) | [top3fusion](./pm/runs.md#top3fusion)

??? abstract "Abstract"
	
	We report on our participation as the IMS Unipd team in both TREC PM 2019 tasks. The objective of the work is twofold: (i) we want to evaluate how different query reformulations affect the results and whether the findings obtained in previous years remain valid; (ii) we want to verify if combining different query reformulations based on expansion and reduction techniques prove effective in such a highly specific scenario. In particular, we designed a procedure to (1) filter out clinical trials based on demographic data, (2) perform query reformulations - both expansion and reduction techniques - based on knowledge bases to increase the probability of findings relevant documents, (3) apply rank fusion techniques to the rankings produced by the different query reformulations. We consider those query reformulations that have been validated on previous TREC PM experimental collections. These queries represent the most effective reformulations for our system on those topics/collections. The results obtained - especially in the clinical trials task - validate our assumptions and provide interesting insights in terms of the different per-topic effectiveness of the query reformulations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NunzioMA19.bib) "
	```
	@inproceedings{DBLP:conf/trec/NunzioMA19,
		author = {Giorgio Maria Di Nunzio and Stefano Marchesin and Maristella Agosti},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Exploring how to Combine Query Reformulations for Precision Medicine},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ims\_unipd.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NunzioMA19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNC SILS at TREC 2019 Precision Medicine Track

_Jiaming Qu, Yue Wang_

- :fontawesome-solid-user-group: **Participant:** [UNC_SILS](./pm/participants.md#unc_sils)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UNC_SILS.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/UNC_SILS.PM.pdf)
- :material-file-search: **Runs:** [sils_run1](./pm/runs.md#sils_run1) | [sils_run2](./pm/runs.md#sils_run2) | [sils_run3](./pm/runs.md#sils_run3) | [sils_run4](./pm/runs.md#sils_run4)

??? abstract "Abstract"
	
	This paper describes our participation in the scientific abstract retrieval task of TREC 2019 Precision Medicine Track. Our approach has two major components. First, we expand the original disease and gene terms using biomedical knowledge bases to improve recall of the initial retrieval. We then improve precision by promoting treatment-related publications to the top using a machine learning reranker trained on 2017 and 2018 relevance judgments combined. Batch evaluation results show that the proposed approach effectively improves P@10 compared to the baseline model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QuW19a.bib) "
	```
	@inproceedings{DBLP:conf/trec/QuW19a,
		author = {Jiaming Qu and Yue Wang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UNC} {SILS} at {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UNC\_SILS.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QuW19a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSIRO at 2019 TREC Precision Medicine Track

_Maciej Rybinski, Sarvnaz Karimi, Cécile Paris_

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./pm/participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CSIROmed.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/CSIROmed.PM.pdf)
- :material-file-search: **Runs:** [bm25_6801](./pm/runs.md#bm25_6801) | [dfr_9464](./pm/runs.md#dfr_9464) | [et_8435](./pm/runs.md#et_8435) | [xgb_5113](./pm/runs.md#xgb_5113) | [bm25_ct_25](./pm/runs.md#bm25_ct_25) | [bm25_ct_f_61](./pm/runs.md#bm25_ct_f_61) | [DFRInL2_f](./pm/runs.md#dfrinl2_f) | [rf1_f_100](./pm/runs.md#rf1_f_100) | [rf2_f_50](./pm/runs.md#rf2_f_50)

??? abstract "Abstract"
	
	TREC Precision Medicine track focuses on search tasks tailored for oncologists. Given a cancer patient, the proposed systems must find clinical trials that match the patient, as well as the relevant information from biomedical literature (PubMed abstracts 2019 baseline). In our experiments, we compare BM25 and Divergence from Randomness (DFR) baselines and report results obtained with multiple learning-to-rank models. Some of our submitted runs score in top ten runs reported by the organisers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RybinskiKP19.bib) "
	```
	@inproceedings{DBLP:conf/trec/RybinskiKP19,
		author = {Maciej Rybinski and Sarvnaz Karimi and C{\'{e}}cile Paris},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CSIRO} at 2019 {TREC} Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CSIROmed.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RybinskiKP19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieving Scientific Abstracts using Venue- and Concept-based Approaches:  CincyMedIR at TREC 2019 Precision Medicine Track

_Danny T. Y. Wu, Wu-Chen Su, James J. Lee_

- :fontawesome-solid-user-group: **Participant:** [CincyMedIR](./pm/participants.md#cincymedir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CincyMedIR.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/CincyMedIR.PM.pdf)
- :material-file-search: **Runs:** [MedIR5](./pm/runs.md#medir5) | [MedIR4](./pm/runs.md#medir4) | [MedIR3](./pm/runs.md#medir3) | [MedIR2](./pm/runs.md#medir2) | [MedIR1](./pm/runs.md#medir1)

??? abstract "Abstract"
	
	The CincyMedIR group led by Dr. Danny T.Y. Wu at the University of Cincinnati (UC) College of Medicine participated in the Text Retrieval Conference 2019 Precision Medicine Track (TREC-PM). Dr. Wu was part of the MedIER group in TREC 2015, 2017, and 2018, and formed his own group this year. CincyMedIR only worked on the scientific abstracts but not clinical trial documents this year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuSL19.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuSL19,
		author = {Danny T. Y. Wu and Wu{-}Chen Su and James J. Lee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Retrieving Scientific Abstracts using Venue- and Concept-based Approaches: CincyMedIR at {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CincyMedIR.PM.pdf},
		timestamp = {Thu, 11 Nov 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuSL19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ECNU-ICA team at TREC 2019 Precision Medicine Track

_Qi Zheng, Yong Li, Jiaying Hu, Yan Yang, Liang He, Yi Xue_

- :fontawesome-solid-user-group: **Participant:** [ECNU-ICA](./pm/participants.md#ecnu-ica)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ECNU_ICA.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/ECNU_ICA.PM.pdf)
- :material-file-search: **Runs:** [clinic_base](./pm/runs.md#clinic_base) | [clinic_ft](./pm/runs.md#clinic_ft) | [cl_base_rr](./pm/runs.md#cl_base_rr) | [cl_ft_agg](./pm/runs.md#cl_ft_agg) | [cl_ft_rr](./pm/runs.md#cl_ft_rr) | [sa_base](./pm/runs.md#sa_base) | [sa_base_rr](./pm/runs.md#sa_base_rr) | [sa_ft](./pm/runs.md#sa_ft) | [sa_ft_rr](./pm/runs.md#sa_ft_rr)

??? abstract "Abstract"
	
	In this paper, we describe our biomedical retrieval system used in TREC 2019 precision medicine track. Based on existing querying framework, we develop a multi-pass retrieval system to adaptively refine query template based on indexing feedback. After initial retrieval process, We further re-rank the retrieved documents using language model based re-ranker to get the final results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengLHYHX19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengLHYHX19,
		author = {Qi Zheng and Yong Li and Jiaying Hu and Yan Yang and Liang He and Yi Xue},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ECNU-ICA} team at {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ECNU\_ICA.PM.pdf},
		timestamp = {Mon, 01 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengLHYHX19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Conversational Assistance 

#### DCU at the TREC 2019 Conversational Assistance Track

_Piyush Arora, Abhishek Kaushik, Gareth J. F. Jones_

- :fontawesome-solid-user-group: **Participant:** [ADAPT-DCU](./cast/participants.md#adapt-dcu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ADAPT-DCU.C.pdf](https://trec.nist.gov/pubs/trec28/papers/ADAPT-DCU.C.pdf)
- :material-file-search: **Runs:** [combination](./cast/runs.md#combination) | [rerankingorder](./cast/runs.md#rerankingorder) | [datasetreorder](./cast/runs.md#datasetreorder) | [topicturnsort](./cast/runs.md#topicturnsort)

??? abstract "Abstract"
	
	We describe the DCU-ADAPT team's participation in the TREC 2019 Conversational Assistance Track (CAsT) track. The CAsT track focuses on two main aspects: i) system understanding of information needs in a conversational format, and ii) finding relevant responses using contextual information. In our participation in the CAST track, we focused on the second aspect of finding relevant information using contextual information from the queries for a conversational search system. We carried out two main investigations: i) Query formulation using syntactic analysis, and ii) Data Fusion of results for re-ranking top candidates retrieved from three different data sources used in the CAsT track. We find that using only query formulation and data fusions techniques attains average results in comparison to other submissions, which are not sufficient to answer questions in a conversational setting reliably.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AroraKJ19.bib) "
	```
	@inproceedings{DBLP:conf/trec/AroraKJ19,
		author = {Piyush Arora and Abhishek Kaushik and Gareth J. F. Jones},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DCU} at the {TREC} 2019 Conversational Assistance Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ADAPT-DCU.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AroraKJ19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke at the TREC 2019 Conversational Assistant Track

_Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./cast/participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/WaterlooClarke.C.pdf](https://trec.nist.gov/pubs/trec28/papers/WaterlooClarke.C.pdf)
- :material-file-search: **Runs:** [clacBase](./cast/runs.md#clacbase) | [clacBaseRerank](./cast/runs.md#clacbasererank) | [clacMagic](./cast/runs.md#clacmagic) | [clacMagicRerank](./cast/runs.md#clacmagicrerank)

??? abstract "Abstract"
	
	For TREC 2019, I, the WaterlooClarke group, submitted four runs to the Conversational Assistant Track (CAsT), which in combination represent three experiments:, clacBase vs. clacBaseRerank, clacBase vs. clacMagic, clacMagic vs clacMagicRerank. This report details the generation of each of these runs and the outcome of these experiments. My overall approach can be explained as three steps: 1) query construction, 2) passage retrieval and ranking, and 3) passage re-ranking. The third step is optional and applies only to the clac*Rerank runs. Like everyone else participating this first year, my ability to explore alternatives for these steps was hampered by the lack of training data specific to this track, and so ultimately I adopted relatively simple methods for all steps. During an exploratory phrase, while these methods were being selected and developed, I did a fair amount of seat-of-the-pants judging and side-by-side comparison of results on selected training topics. I never want to read about physician assistants, Plessy v. Ferguson, or water molecules ever again. On the other hand, I have lots of ideas for improving these methods, and I'm looking for to the continuation of the track in TREC 2020.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Clarke19.bib) "
	```
	@inproceedings{DBLP:conf/trec/Clarke19,
		author = {Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {WaterlooClarke at the {TREC} 2019 Conversational Assistant Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/WaterlooClarke.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Clarke19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Trec 2019 Conversational Assistance Track

_Changying Hao, Yuanyuan Zhang, Weifeng Yang, Heng Zhao_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./cast/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.C.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.C.pdf)
- :material-file-search: **Runs:** [ict_wrfml](./cast/runs.md#ict_wrfml)

??? abstract "Abstract"
	
	In this paper we report on our participation in the TREC 2019 Conversational Assistance Track which focuses on Conversational Information Seeking CIS namely understand the dialogue context and retrieve candidate response information from collections provided. We convert the CIS task into a standard information retrieval task and use both traditional IR model and neural IR model to rerank the baseline official evaluation results. We compare the results of models in two categories(four models in total), and give a summary for the solution of our work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HaoZYZ19.bib) "
	```
	@inproceedings{DBLP:conf/trec/HaoZYZ19,
		author = {Changying Hao and Yuanyuan Zhang and Weifeng Yang and Heng Zhao},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Trec 2019 Conversational Assistance Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ICTNET.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HaoZYZ19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2019 Conversational Assistance Track

_Helia Hashemi, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [UMass](./cast/participants.md#umass)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UMass.C.pdf](https://trec.nist.gov/pubs/trec28/papers/UMass.C.pdf)
- :material-file-search: **Runs:** [UMASS_DMN_V1](./cast/runs.md#umass_dmn_v1) | [UMASS_DMN_V2](./cast/runs.md#umass_dmn_v2)

??? abstract "Abstract"
	
	This is an overview of University of Massachusetts efforts in providing passage retrieval run submissions for the TREC 2019 Conversational Assistance Track (CAsT). We adopted recent neural approaches for the task. The goal is to retrieve passages that are different from what traditional methods retrieve, in order to enrich the candidates pool.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HashemiC19.bib) "
	```
	@inproceedings{DBLP:conf/trec/HashemiC19,
		author = {Helia Hashemi and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UMass at {TREC} 2019 Conversational Assistance Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UMass.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HashemiC19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CROWN: Conversational Passage Ranking by Reasoning over Word Networks

_Magdalena Kaiser, Rishiraj Saha Roy, Gerhard Weikum_

- :fontawesome-solid-user-group: **Participant:** [mpi-inf-d5](./cast/participants.md#mpi-inf-d5)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/mpi-inf-d5.C.pdf](https://trec.nist.gov/pubs/trec28/papers/mpi-inf-d5.C.pdf)
- :material-file-search: **Runs:** [mpi-d5_igraph](./cast/runs.md#mpi-d5_igraph) | [mpi-d5_intu](./cast/runs.md#mpi-d5_intu) | [mpi-d5_union](./cast/runs.md#mpi-d5_union) | [mpi-d5_cqw](./cast/runs.md#mpi-d5_cqw)

??? abstract "Abstract"
	
	Information needs around a topic often cannot be satisfied in a single turn; users typically ask follow-up questions referring to the same theme. A system must be capable of understanding the conversational context of a request to retrieve correct answers. In this paper, we present our submission to the TREC Conversational Assistance Track (CAsT) 2019, in which such a conversational setting is explored. We propose an unsupervised method for conversational passage ranking by formulating the passage score for a query as a combination of similarity and coherence. To be specific, passages are preferred that contain words semantically similar to the words used in the question, and where such words appear close by. We built a word proximity network (WPN) from a large corpus, where words are nodes and there is an edge between two nodes if they co-occur in the same passages in a statistically significant way, within a context window. Our approach, named CROWN, achieved above-average performance on the TREC CAsT data with respect to AP@5 and nDCG@1000.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KaiserRW19.bib) "
	```
	@inproceedings{DBLP:conf/trec/KaiserRW19,
		author = {Magdalena Kaiser and Rishiraj Saha Roy and Gerhard Weikum},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CROWN:} Conversational Passage Ranking by Reasoning over Word Networks},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/mpi-inf-d5.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KaiserRW19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Radboud University at TREC 2019

_Chris Kamphuis, Faegheh Hasibi, Arjen P. de Vries, Tanja Crijns_

- :fontawesome-solid-user-group: **Participant:** [RUIR](./cast/participants.md#ruir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/RUIR.N.C.pdf](https://trec.nist.gov/pubs/trec28/papers/RUIR.N.C.pdf)
- :material-file-search: **Runs:** [BM25_BERT_FC](./cast/runs.md#bm25_bert_fc) | [BM25_BERT_RANKF](./cast/runs.md#bm25_bert_rankf)

??? abstract "Abstract"
	
	The Radboud University Information Retrieval (RU/IR) research group has a research interest in graph based approaches to IR, where we aim to exploit the flexibility of a graph representation of documents and other types of information (such as entities) to achieve increased retrieval effectiveness, e.g. by integrating extra knowledge about a domain. The main focus of our participation in TREC 2019 has been the News Track, where we see a large potential to improve search using graph based representations. We have also participated in the new Conversational Assistance Track, where we have explored how to make use of the conversational context to improve ranking answer passages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KamphuisHVC19.bib) "
	```
	@inproceedings{DBLP:conf/trec/KamphuisHVC19,
		author = {Chris Kamphuis and Faegheh Hasibi and Arjen P. de Vries and Tanja Crijns},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Radboud University at {TREC} 2019},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/RUIR.N.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KamphuisHVC19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Step towards Context Identification for Conversational Search

_Vaibhav Kumar, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU](./cast/participants.md#cmu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CMU.C.pdf](https://trec.nist.gov/pubs/trec28/papers/CMU.C.pdf)
- :material-file-search: **Runs:** [coref_shift_qe](./cast/runs.md#coref_shift_qe) | [ensemble](./cast/runs.md#ensemble) | [coref_cshift](./cast/runs.md#coref_cshift) | [manual_indri](./cast/runs.md#manual_indri)

??? abstract "Abstract"
	
	The system comprises of three different components. The first component makes a decision whether to incorporate contextual information for the current query in ongoing conversation. The decision is based on the KL-divergence between the retrieved documents for the original query and whether the query consists of pronouns. The second component identifies the contextual information (if required) for the answering the current query. This identification is performed using an SVM classifier which uses BERT aention weights along with other linguistic features. Finally, the third component utilises Indri for document retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KumarC19.bib) "
	```
	@inproceedings{DBLP:conf/trec/KumarC19,
		author = {Vaibhav Kumar and Jamie Callan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Step towards Context Identification for Conversational Search},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CMU.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KumarC19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LINBER: A Retrieval-based Conversational Assistant using Entity  Linking and BERT

_Yucheng Li, Yuxiang Sun, Jun Zhang, Pei Huo, Yan Yang, Liang He_

- :fontawesome-solid-user-group: **Participant:** [ECNU-ICA](./cast/participants.md#ecnu-ica)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ECNU_ICA.C.pdf](https://trec.nist.gov/pubs/trec28/papers/ECNU_ICA.C.pdf)
- :material-file-search: **Runs:** [ECNUICA_BERT](./cast/runs.md#ecnuica_bert) | [ECNUICA_ORI](./cast/runs.md#ecnuica_ori) | [ECNUICA_MIX](./cast/runs.md#ecnuica_mix)

??? abstract "Abstract"
	
	We developed a retrieval-based conversational assistant named linber. linber was featured by entity linking module and Bert re-ranking process. linber perform Conversational Assistance Track (CAsT) by the fellowing five modules: (1) Coreference resolution module (2) Keywords extraction module (3) Entity linking module (4) Retrieval module (5) BERT re-ranking module.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiSZHYH19.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiSZHYH19,
		author = {Yucheng Li and Yuxiang Sun and Jun Zhang and Pei Huo and Yan Yang and Liang He},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{LINBER:} {A} Retrieval-based Conversational Assistant using Entity Linking and {BERT}},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ECNU\_ICA.C.pdf},
		timestamp = {Tue, 14 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiSZHYH19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MPII at TREC CAsT 2019: Incoporating Query Context into a BERT  Re-ranker

_Samarth Mehrotra, Andrew Yates_

- :fontawesome-solid-user-group: **Participant:** [mpii](./cast/participants.md#mpii)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/mpii.C.pdf](https://trec.nist.gov/pubs/trec28/papers/mpii.C.pdf)
- :material-file-search: **Runs:** [mpi_bert](./cast/runs.md#mpi_bert) | [mpi_base](./cast/runs.md#mpi_base)

??? abstract "Abstract"
	
	MPII participated in the Conversational Assistance Track (CAsT) at TREC 2019. Our approach consists of an initial stage ranker followed by a BERT-based [3] neural document re-ranking model. BM25 with query expansion based on external knowledge (i.e., Wikipedia and ConceptNet) serves as the first stage ranking method, while the neural model uses BERT embeddings and a kernel-based ranking module (KNRM) to predict a document-query relevance score. We repurpose and modify subtopics from the TREC Web Track's diversity task to train the neural module. We find that the neural re-ranking module substantially improves upon the initial ranking approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MehrotraY19.bib) "
	```
	@inproceedings{DBLP:conf/trec/MehrotraY19,
		author = {Samarth Mehrotra and Andrew Yates},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{MPII} at {TREC} CAsT 2019: Incoporating Query Context into a {BERT} Re-ranker},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/mpii.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MehrotraY19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Predicting Relevant Conversation Turns for Improved Retrieval in Multi-Turn  Conversational Search

_Esteban A. Ríssola, Manajit Chakraborty, Fabio Crestani, Mohammad Aliannejadi_

- :fontawesome-solid-user-group: **Participant:** [USI](./cast/participants.md#usi)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/USI.C.pdf](https://trec.nist.gov/pubs/trec28/papers/USI.C.pdf)
- :material-file-search: **Runs:** [galago_rel_q](./cast/runs.md#galago_rel_q) | [bertrr_rel_q](./cast/runs.md#bertrr_rel_q) | [galago_rel_1st](./cast/runs.md#galago_rel_1st) | [bertrr_rel_1st](./cast/runs.md#bertrr_rel_1st)

??? abstract "Abstract"
	
	This technical report presents the work of Universit`a della Svizzera italiana in TREC CAsT 2019. TREC CAsT was set up to advance research on conversational search systems. The goal of the track is to create a reusable benchmark for open-domain information-centric conversational dialogues and to establish a concrete and standard collection of data with information needs to make systems directly comparable. Given the complexity of natural language and the evolution of user's information need in a conversation with multiple turns, finding relevant context is not always straightforward. We developed a neural model for identifying relevant turn(s) corresponding to the given turn. Our model reformulates the information need of the user to take into account the conversational context to enhance the ad-hoc passage retrieval performance. Two of our runs also employ neural re-ranking of the passages post-retrieval. One of our runs was able to achieve above-median performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RissolaCCA19.bib) "
	```
	@inproceedings{DBLP:conf/trec/RissolaCCA19,
		author = {Esteban A. R{\'{\i}}ssola and Manajit Chakraborty and Fabio Crestani and Mohammad Aliannejadi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Predicting Relevant Conversation Turns for Improved Retrieval in Multi-Turn Conversational Search},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/USI.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RissolaCCA19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### VES Team at TREC Conversational Assistance Track (CAsT) 2019

_Vasileios Stamatis, Leif Azzopardi, Alan Wilson_

- :fontawesome-solid-user-group: **Participant:** [VES](./cast/participants.md#ves)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/VES.C.pdf](https://trec.nist.gov/pubs/trec28/papers/VES.C.pdf)
- :material-file-search: **Runs:** [VESBERT](./cast/runs.md#vesbert) | [VESBERT1000](./cast/runs.md#vesbert1000)

??? abstract "Abstract"
	
	In this work we present our submission at the TREC Conversational Assistance Track 2019. For this year's track, we have focused on developing a baseline system from which we can build upon in the future. Our system is built upon a Lucene index which serves up results (using BM25), these are then re-ranked by BERT given the conversational context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StamatisAW19.bib) "
	```
	@inproceedings{DBLP:conf/trec/StamatisAW19,
		author = {Vasileios Stamatis and Leif Azzopardi and Alan Wilson},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{VES} Team at {TREC} Conversational Assistance Track (CAsT) 2019},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/VES.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StamatisAW19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ILPS at TREC 2019 Conversational Assistant Track

_Nikos Voskarides, Dan Li, Andreas Panteli, Pengjie Ren_

- :fontawesome-solid-user-group: **Participant:** [UvA.ILPS](./cast/participants.md#uva.ilps)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UvA.ILPS.C.pdf](https://trec.nist.gov/pubs/trec28/papers/UvA.ILPS.C.pdf)
- :material-file-search: **Runs:** [ilps-lm-rm3-dt](./cast/runs.md#ilps-lm-rm3-dt)

??? abstract "Abstract"
	
	This paper describes the participation of the UvA.ILPS group at the TREC CAsT 2019 track. We propose a cascade architecture that consists of (i) a unsupervised initial retrieval step that uses on a query expansion model that extracts words from the previous turns that are relevant to the current turn, and (ii) a supervised neural ranker that is based on BERT. We use transfer learning to pretrain our neural ranker with a single-turn passage ranking dataset (MS MARCO) and a multi-turn passage ranking dataset that we induced from a dataset originally proposed for a different task (QuAC). Official results show that our best run outperforms the median run by 25.6% in terms of NDCG@5 and 26.4% in terms of NDCG@1000.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VoskaridesLPR19.bib) "
	```
	@inproceedings{DBLP:conf/trec/VoskaridesLPR19,
		author = {Nikos Voskarides and Dan Li and Andreas Panteli and Pengjie Ren},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ILPS} at {TREC} 2019 Conversational Assistant Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UvA.ILPS.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VoskaridesLPR19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring Query Reformulation for Conversational Information Seeking

_Disen Wang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./cast/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/udel_fang.C.pdf](https://trec.nist.gov/pubs/trec28/papers/udel_fang.C.pdf)
- :material-file-search: **Runs:** [UDInfoC_BL](./cast/runs.md#udinfoc_bl) | [UDInfoC_TS](./cast/runs.md#udinfoc_ts) | [UDInfoC_TS_2](./cast/runs.md#udinfoc_ts_2)

??? abstract "Abstract"
	
	Few tasks have been designed for conversational information seeking. To fill this gap, this year's TREC Conversation Assistance Track (CAsT) is proposed to advance research on conversational search systems. We built a model that first read the dialogue context, then retrieved candidate response information from a large collection of paragraphs. In order to perform passage retrieval task, we first applied the coreference resolution method to format questions into queries, and we use Indri to retrieve top 100 relevant passages. During the second phrase, we applied fine-tuned BERT model to re-rank retrieved passage.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangF19.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangF19,
		author = {Disen Wang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Exploring Query Reformulation for Conversational Information Seeking},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/udel\_fang.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangF19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query and Answer Expansion from Conversation History

_Jheng-Hong Yang, Sheng-Chieh Lin, Chuan-Ju Wang, Jimmy Lin, Ming-Feng Tsai_

- :fontawesome-solid-user-group: **Participant:** [CFDA_CLIP](./cast/participants.md#cfda_clip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CFDA_CLIP.C.pdf](https://trec.nist.gov/pubs/trec28/papers/CFDA_CLIP.C.pdf)
- :material-file-search: **Runs:** [CFDA_CLIP_RUN1](./cast/runs.md#cfda_clip_run1) | [CFDA_CLIP_RUN8](./cast/runs.md#cfda_clip_run8) | [CFDA_CLIP_RUN6](./cast/runs.md#cfda_clip_run6) | [CFDA_CLIP_RUN7](./cast/runs.md#cfda_clip_run7)

??? abstract "Abstract"
	
	In this paper, we present our methods, experimental analysis, and final submissions for the Conversational Assistance Track (CAsT) at TREC 2019. In addition to language understanding, extracting knowledge from historical dialogues (e.g., previous queries, searching results) is a key to the conversational IR task. However, limited annotated data in the CAsT task makes machine learning or other data-driven approaches infeasible. Along this line, we propose two ad hoc and intuitive approaches: Historical Query Expansion and Historical Answer Expansion, to improve the performance of the conversational IR system with limited training data. Our empirical result on the CAsT training set shows that the proposed methods significantly improve the quality of conversational search in terms of retrieval (recall@1000: 0.774 → 0.844) and ranking (mAP: 0.187 → 0.197) compared to our strong baseline. As a result, our submitted entries outperform the median performance of all the 21 teams.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLWLT19.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangLWLT19,
		author = {Jheng{-}Hong Yang and Sheng{-}Chieh Lin and Chuan{-}Ju Wang and Jimmy Lin and Ming{-}Feng Tsai},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query and Answer Expansion from Conversation History},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CFDA\_CLIP.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangLWLT19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RUCIR at TREC 2019: Conversational Assistance Track

_Xiaochen Zuo, Xue Yang, Zhicheng Dou, Ji-Rong Wen_

- :fontawesome-solid-user-group: **Participant:** [RUCIR](./cast/participants.md#rucir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/RUCIR.C.pdf](https://trec.nist.gov/pubs/trec28/papers/RUCIR.C.pdf)
- :material-file-search: **Runs:** [RUCIR-run3](./cast/runs.md#rucir-run3) | [RUCIR-run1](./cast/runs.md#rucir-run1) | [RUCIR-run2](./cast/runs.md#rucir-run2) | [RUCIR-run4](./cast/runs.md#rucir-run4)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the RUCIR group's participation in the TREC 2019 Conversational Assistance Track. All our runs for the Conversational Assistance Track are on the full MS MARCO Conversational Search Sessions dataset and use the online Indri retrieval system hosted at CMU. For the Conversational Assistance Track, our runs try to solve conversational retrieval problems from two directions: One is to improve the search results by modifying the user's current query, including query reference resolution and incorporate the information from user's history queries in the same session. Run 1, Run 2 and Run 4 use this method. The other direction is to design a neural network to model user's global search intent and current search intent to get the retrieval results and run3 uses this method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZuoYDW19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZuoYDW19,
		author = {Xiaochen Zuo and Xue Yang and Zhicheng Dou and Ji{-}Rong Wen},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{RUCIR} at {TREC} 2019: Conversational Assistance Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/RUCIR.C.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZuoYDW19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREMA-UNH at CAR 2019

_Jordan Ramsdell, Sumanta Kashyapi, Shubham Chatterjee, Pooja Oza, Laura Dietz_

- :fontawesome-solid-user-group: **Participant:** [TREMA-UNH](./cast/participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf](https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf)
- :material-file-search: **Runs:** [UNH-trema-ecn](./cast/runs.md#unh-trema-ecn) | [UNH-trema-ent](./cast/runs.md#unh-trema-ent) | [unh-trema-relco](./cast/runs.md#unh-trema-relco)

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

## News 

#### ICTNET at TREC 2019 News Track

_Yuyang Ding, Xiaoying Lian, Houquan Zhou, Zhaoge Liu, Hanxing Ding, Zhongni Hou_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./news/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.N.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.N.pdf)
- :material-file-search: **Runs:** [ICTNET_stem](./news/runs.md#ictnet_stem) | [ql](./news/runs.md#ql) | [rm3](./news/runs.md#rm3) | [rocchio](./news/runs.md#rocchio) | [ICTNET_estem](./news/runs.md#ictnet_estem)

??? abstract "Abstract"
	
	This paper describes our work in the background linking task and entity ranking task in TREC 2018 News Track. We explore four methods in background linking task and two methods in entity ranking task. All of our methods largely rely on off-the-shell open-source components(e.g., Solr for indexing the documents), and follow the basic thoughts — BM25 and relevance feedback. These methods differ in how they analyze the given input to obtain a query and to what extent the returned results are re-ranked taking meta data of the document (e.g., publish dates) into account.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DingLZLDH19.bib) "
	```
	@inproceedings{DBLP:conf/trec/DingLZLDH19,
		author = {Yuyang Ding and Xiaoying Lian and Houquan Zhou and Zhaoge Liu and Hanxing Ding and Zhongni Hou},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at {TREC} 2019 News Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ICTNET.N.pdf},
		timestamp = {Tue, 27 Jun 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DingLZLDH19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### bigIR at TREC 2019: Graph-based Analysis for News Background Linking

_Marwa Essam, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./news/participants.md#qu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/QU.N.pdf](https://trec.nist.gov/pubs/trec28/papers/QU.N.pdf)
- :material-file-search: **Runs:** [QU_KCore](./news/runs.md#qu_kcore) | [QU_KTruss](./news/runs.md#qu_ktruss) | [QU_KCore_F](./news/runs.md#qu_kcore_f) | [QU_KTruss_F](./news/runs.md#qu_ktruss_f)

??? abstract "Abstract"
	
	Nowadays, it is very rare to find an online news article that is self-contained with everything a reader would want to know about the article's story. Therefore, it became vital for any article to contain links to other articles or resources that provide the background and contextual knowledge required to conceptualize the article's story. However, finding useful background and contextual links can be a challenging problem. In this paper, we address this problem in the context of the participation of the bigIR team at Qatar University in the news background linking task of the TREC 2019 news track. Our methods mainly relied on a graph-based analysis of the query-article's text to extract its most representative and influential keywords, and then use these keywords as a search query to retrieve the article's background links from a collection of news articles. All of our submitted runs outperformed the TREC hypothetical run that achieved a median effectiveness over all queries. Moreover, our best submitted run was ranked second among 28 runs submitted to the task, indicating the potential effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EssamE19.bib) "
	```
	@inproceedings{DBLP:conf/trec/EssamE19,
		author = {Marwa Essam and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {bigIR at {TREC} 2019: Graph-based Analysis for News Background Linking},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/QU.N.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EssamE19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Smith at TREC2019: Learning to Rank Background Articles with Poetry  Categories and Keyphrase Extraction

_John Foley, Ananda Montoly, Mayeline Pena_

- :fontawesome-solid-user-group: **Participant:** [Smith](./news/participants.md#smith)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/Smith.N.pdf](https://trec.nist.gov/pubs/trec28/papers/Smith.N.pdf)
- :material-file-search: **Runs:** [smith_base](./news/runs.md#smith_base) | [smith_poetry](./news/runs.md#smith_poetry) | [smith_keyword](./news/runs.md#smith_keyword) | [smith_full](./news/runs.md#smith_full)

??? abstract "Abstract"
	
	Smith College participated in the TREC News Background Linking task in 2019. We constructed a linear learning to rank model trained on the 2018 data and submitted runs that included features derived from ongoing research into automatic poetry understanding. In this notebook paper we detail the contents of our submissions and our lessons learned from this year's participation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FoleyMP19.bib) "
	```
	@inproceedings{DBLP:conf/trec/FoleyMP19,
		author = {John Foley and Ananda Montoly and Mayeline Pena},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Smith at {TREC2019:} Learning to Rank Background Articles with Poetry Categories and Keyphrase Extraction},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/Smith.N.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FoleyMP19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Proximity-Based Entity Ranking

_Gustavo Gonçalves, João Magalhães, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU](./news/participants.md#cmu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CMU.N.pdf](https://trec.nist.gov/pubs/trec28/papers/CMU.N.pdf)
- :material-file-search: **Runs:** [CMU_NS-1-tpb](./news/runs.md#cmu_ns-1-tpb) | [CMU_NS-2-tp](./news/runs.md#cmu_ns-2-tp) | [CMU_NS-3-t](./news/runs.md#cmu_ns-3-t)

??? abstract "Abstract"
	
	This work explores the value of a combination of features, including entity proximity, for improving a learning-to-rank entity ranking system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoncalvesMC19.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoncalvesMC19,
		author = {Gustavo Gon{\c{c}}alves and Jo{\~{a}}o Magalh{\~{a}}es and Jamie Callan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Proximity-Based Entity Ranking},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CMU.N.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GoncalvesMC19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UQ at the TREC 2019 News Track

_Vu Anh Le, Gianluca Demartini_

- :fontawesome-solid-user-group: **Participant:** [UQ](./news/participants.md#uq)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UQ.N.pdf](https://trec.nist.gov/pubs/trec28/papers/UQ.N.pdf)
- :material-file-search: **Runs:** [UQ_count_sent](./news/runs.md#uq_count_sent) | [UQ_count](./news/runs.md#uq_count) | [UQ_wiki](./news/runs.md#uq_wiki) | [UQ_sent](./news/runs.md#uq_sent) | [UQ_wiki_count](./news/runs.md#uq_wiki_count)

??? abstract "Abstract"
	
	The Data Science research group at the University of Queensland participated to the TREC 2019 News Track by submitting 5 runs for the Entity Ranking task. Our approach is based on entity frequency, sentence similarity scoring functions, and the use of external sources of evidence like Wikipedia. The results we obtained show that 1) the most effective of our methods makes use of Wikipedia as an external collection to rank entities and that 2) this method can deal well with difficult topics but it should be combined with alternative approaches on a topic-by-topic basis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeD19.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeD19,
		author = {Vu Anh Le and Gianluca Demartini},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UQ} at the {TREC} 2019 News Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UQ.N.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeD19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Leveraging Entities in Background Document Retrieval for News Articles

_Kuang Lu, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./news/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/udel_fang.N.pdf](https://trec.nist.gov/pubs/trec28/papers/udel_fang.N.pdf)
- :material-file-search: **Runs:** [UDInfolab_all](./news/runs.md#udinfolab_all) | [UDInfolab_ent](./news/runs.md#udinfolab_ent)

??? abstract "Abstract"
	
	In this year's News Track, we focus on effectively estimating entity weights by using the words surrounding the entities for background linking task. Analyses on the results reveal the inconsistency of our methods as well as the temporal characteristics of the queries. These observations lead to several interesting research questions about the background document retrieval task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuF19.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuF19,
		author = {Kuang Lu and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Leveraging Entities in Background Document Retrieval for News Articles},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/udel\_fang.N.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuF19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNC SILS at TREC 2019 News Track

_Jiaming Qu, Yue Wang_

- :fontawesome-solid-user-group: **Participant:** [UNC_SILS](./news/participants.md#unc_sils)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UNC_SILS.N.pdf](https://trec.nist.gov/pubs/trec28/papers/UNC_SILS.N.pdf)
- :material-file-search: **Runs:** [sils_news_run1](./news/runs.md#sils_news_run1) | [sils_news_run2](./news/runs.md#sils_news_run2) | [sils_news_run3](./news/runs.md#sils_news_run3) | [sils_news_run4](./news/runs.md#sils_news_run4)

??? abstract "Abstract"
	
	This paper describes our participation in the Background Linking task of TREC 2019 News Track. Our approach has two directions. After processing the corpus, we use Lucene to index and run the initial retrieval. Then we leverage the learning-to-rank idea to train a re-ranker using the 2018 relevance judgement files as ground truth, and the re-ranker is applied to the initial retrieval results to generate a new ranked list. Experiment results prove that the re-ranker significantly improves the retrieval performance (NDCG@5) compared to the initial retrieval results without the re-ranking step.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QuW19.bib) "
	```
	@inproceedings{DBLP:conf/trec/QuW19,
		author = {Jiaming Qu and Yue Wang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UNC} {SILS} at {TREC} 2019 News Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UNC\_SILS.N.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QuW19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREMA-UNH at CAR 2019

_Jordan Ramsdell, Sumanta Kashyapi, Shubham Chatterjee, Pooja Oza, Laura Dietz_

- :fontawesome-solid-user-group: **Participant:** [TREMA-UNH](./news/participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf](https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf)
- :material-file-search: **Runs:** [unh-trema-news](./news/runs.md#unh-trema-news)

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

#### OzU-NLP at TREC NEWS 2019: Entity Ranking

_Kenan Fayoumi, Reyyan Yeniterzi_

- :fontawesome-solid-user-group: **Participant:** [OzUNLP](./news/participants.md#ozunlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/OzUNLP.News.pdf](https://trec.nist.gov/pubs/trec28/papers/OzUNLP.News.pdf)
- :material-file-search: **Runs:** [OzU_wiki](./news/runs.md#ozu_wiki) | [OzU_wiki_1_ws](./news/runs.md#ozu_wiki_1_ws) | [OzU_wiki_5_ws](./news/runs.md#ozu_wiki_5_ws) | [OzU_wiki_top1](./news/runs.md#ozu_wiki_top1) | [OzU_wiki_top5](./news/runs.md#ozu_wiki_top5)

??? abstract "Abstract"
	
	This paper presents our work and submission for TREC 2019 News Track: Entity Ranking Task. Our approach utilizes Doc2Vec's ability to represent documents as fixed sized numerical vectors. Applied on news articles and wiki-pages of the entities, Doc2Vec provides us with vector representations for these two that we can utilize to perform ranking on entities. We also investigate whether background linked articles can be useful for entity ranking task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FayoumiY19.bib) "
	```
	@inproceedings{DBLP:conf/trec/FayoumiY19,
		author = {Kenan Fayoumi and Reyyan Yeniterzi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {OzU-NLP at {TREC} {NEWS} 2019: Entity Ranking},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/OzUNLP.News.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FayoumiY19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DMINR at TREC News Track

_Sondess Missaoui, Andrew MacFarlane, Stephann Makri, Marisela Gutierrez-Lopez_

- :fontawesome-solid-user-group: **Participant:** [cityuni](./news/participants.md#cityuni)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/cityuni.News.pdf](https://trec.nist.gov/pubs/trec28/papers/cityuni.News.pdf)
- :material-file-search: **Runs:** [cityuni_1](./news/runs.md#cityuni_1) | [cityuni_ER1](./news/runs.md#cityuni_er1) | [cityuni_ER2](./news/runs.md#cityuni_er2)

??? abstract "Abstract"
	
	This paper describes the use of the DMINR Named entity extraction and linking system in TREC 2019. The track entered for are: News track, involves both Background Linking and Entity Ranking. Our approach to each of these tasks draws on prior work done by City, University of London at the TREC conference. In the background linking task, we treated the problems as an adhoc search task, using Named Entities (NEs) from a set of documents identified in pseudo relevance feedback, and optimizing these using a Hill-Climbing algorithm to provide a set of related articles. In the Entity Ranking task, we compared an approach using the BM25 ranking method with a probabilistic model that uses Wikipedia data as a resource to rank entities. The probabilistic model utilises an entity modeling approach to disambiguate NEs. Then , it utilises a scoring model which uses the given entities to provide a score for them based on evidence from the news articles.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MissaouiMMG19.bib) "
	```
	@inproceedings{DBLP:conf/trec/MissaouiMMG19,
		author = {Sondess Missaoui and Andrew MacFarlane and Stephann Makri and Marisela Gutierrez{-}Lopez},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DMINR} at {TREC} News Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/cityuni.News.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MissaouiMMG19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Decision 

#### UWaterlooMDS at the TREC 2019 Decision Track

_Mustafa Abualsaud, Fuat Can Beylunioglu, Mark D. Smucker, P. Robert Duimering_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./decisions/participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UWaterlooMDS.D.pdf](https://trec.nist.gov/pubs/trec28/papers/UWaterlooMDS.D.pdf)
- :material-file-search: **Runs:** [UWaterMDS_BM25](./decisions/runs.md#uwatermds_bm25) | [UWatMDSBM25_HC1](./decisions/runs.md#uwatmdsbm25_hc1) | [UWatMDSBM25_HC2](./decisions/runs.md#uwatmdsbm25_hc2) | [UWatMDSBM25_HC3](./decisions/runs.md#uwatmdsbm25_hc3) | [UWatMDS_BM25_ZS](./decisions/runs.md#uwatmds_bm25_zs) | [UWatMDS_BM25_Z](./decisions/runs.md#uwatmds_bm25_z) | [UWatMDS_BMZBS10](./decisions/runs.md#uwatmds_bmzbs10) | [UWatMDS_BMF_C90](./decisions/runs.md#uwatmds_bmf_c90) | [UWatMDS_BMF_C95](./decisions/runs.md#uwatmds_bmf_c95) | [UWatMDS_BMF_S30](./decisions/runs.md#uwatmds_bmf_s30)

??? abstract "Abstract"
	
	In this report, we discuss the experiments we conducted for the TREC 2019 Decision Track. This year, our goal was to investigate the effect of document credibility on the quality of automatic runs. To address credibility, we combined scores from a spam classifier and a credibility classifier trained to detect non-trustworthy websites. The results from both classifiers were then used to modify a baseline BM25 ranking. In addition to the automatic runs, we also submitted manual runs using the HiCAL [2] system. Our manual runs modify a baseline BM25 ranking using manually judged documents found using the system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbualsaudBSD19.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbualsaudBSD19,
		author = {Mustafa Abualsaud and Fuat Can Beylunioglu and Mark D. Smucker and P. Robert Duimering},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UWaterlooMDS at the {TREC} 2019 Decision Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UWaterlooMDS.D.pdf},
		timestamp = {Mon, 31 Jul 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbualsaudBSD19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2019: Decision Track

_Alexander Bondarenko, Maik Fröbe, Vaibhav Kasturia, Matthias Hagen, Michael Völske, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./decisions/participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/Webis.D.pdf](https://trec.nist.gov/pubs/trec28/papers/Webis.D.pdf)
- :material-file-search: **Runs:** [webisMSame1](./decisions/runs.md#webismsame1) | [webisMSame2](./decisions/runs.md#webismsame2) | [webisMSame3](./decisions/runs.md#webismsame3) | [webisMSame4](./decisions/runs.md#webismsame4) | [webisMSame5](./decisions/runs.md#webismsame5) | [webisTSame1](./decisions/runs.md#webistsame1) | [webisMMajority1](./decisions/runs.md#webismmajority1) | [webisTMajority1](./decisions/runs.md#webistmajority1) | [webisMAll1](./decisions/runs.md#webismall1) | [webisTAll1](./decisions/runs.md#webistall1)

??? abstract "Abstract"
	
	This paper gives an overview of the Webis group's participation in the TREC 2019 Decision Track. Our idea is to axiomatically re-rank the top-k results of BM25F for those topics that seem to be argumentative. For the re-ranking, we use five axioms that capture signals of argumentativeness and information credibility.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BondarenkoFKHVS19.bib) "
	```
	@inproceedings{DBLP:conf/trec/BondarenkoFKHVS19,
		author = {Alexander Bondarenko and Maik Fr{\"{o}}be and Vaibhav Kasturia and Matthias Hagen and Michael V{\"{o}}lske and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2019: Decision Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/Webis.D.pdf},
		timestamp = {Fri, 19 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BondarenkoFKHVS19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Trec 2019 Decision Track

_Wanqing Cui, Yan Jiang, Shuchang Tao, Hanzhang Guo_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./decisions/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.D.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.D.pdf)
- :material-file-search: **Runs:** [ICTNETv1BM25](./decisions/runs.md#ictnetv1bm25) | [ICTNETv2BM25](./decisions/runs.md#ictnetv2bm25)

??? abstract "Abstract"
	
	In this paper we report on our participation in the Trec 2019 Decision Track[1] which aims to provide a venue for research on retrieval methods that promote better decision making with search engines and develop new online and offline evaluation methods to predict the decision making quality induced by search results. We convert this task into a standard information retrieval task and use traditional IR model. Finally we give a summary for the solution of our work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CuiJTG19.bib) "
	```
	@inproceedings{DBLP:conf/trec/CuiJTG19,
		author = {Wanqing Cui and Yan Jiang and Shuchang Tao and Hanzhang Guo},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Trec 2019 Decision Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ICTNET.D.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CuiJTG19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UQ IElab at TREC 2019 Decision Track

_Jimmy, Guido Zuccon_

- :fontawesome-solid-user-group: **Participant:** [UQ](./decisions/participants.md#uq)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UQ.D.pdf](https://trec.nist.gov/pubs/trec28/papers/UQ.D.pdf)
- :material-file-search: **Runs:** [IELAB01_ori_q](./decisions/runs.md#ielab01_ori_q) | [IELAB02_ori_d](./decisions/runs.md#ielab02_ori_d) | [IELAB03_umls_d](./decisions/runs.md#ielab03_umls_d) | [IELAB04_umls_n](./decisions/runs.md#ielab04_umls_n) | [IELAB05_xChv_q](./decisions/runs.md#ielab05_xchv_q) | [IELAB06_xChv_d](./decisions/runs.md#ielab06_xchv_d) | [IELAB07_xWiki_q](./decisions/runs.md#ielab07_xwiki_q) | [IELAB08_xWiki_d](./decisions/runs.md#ielab08_xwiki_d) | [IELAB09_xCW_q](./decisions/runs.md#ielab09_xcw_q) | [IELAB10_xCW_d](./decisions/runs.md#ielab10_xcw_d)

??? abstract "Abstract"
	
	We describe our participation to the TREC 2019 Decision Track. The first year of this track challenges participants to devise search technologies that retrieve correct health advice from web resources, with the intent to better support people's health decision making. Our solution addressed this challenge by extending the Entity Query Feature Expansion model (EQFE), a knowledge base (KB) query expansion method. In previous work we showed that Wikipedia and the Consumer Health Vocabulary resource can be effective as basis for consumer health search query expansion, within the EQFE method. To obtain query expansion terms, first, we mapped entity mentions to KB entities by performing exact matching. After mapping, we used the Title of the mapped KB entities as the source for expansion terms. Despite previous evaluation demonstrating the effectiveness of this method, EQFE did not provide the expected gains over not using query expansion, on both relevant-based and credibility-based evaluation measures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JimmyZ19.bib) "
	```
	@inproceedings{DBLP:conf/trec/JimmyZ19,
		author = {Jimmy and Guido Zuccon},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UQ} IElab at {TREC} 2019 Decision Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UQ.D.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JimmyZ19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Fair Ranking 

#### Fair ranking in academic search - Notebook for the TREC 2019 Fair  Ranking Track

_Malte Bonart_

- :fontawesome-solid-user-group: **Participant:** [IR-Cologne](./fair/participants.md#ir-cologne)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/IR-Cologne.FR.pdf](https://trec.nist.gov/pubs/trec28/papers/IR-Cologne.FR.pdf)
- :material-file-search: **Runs:** [fair_random](./fair/runs.md#fair_random) | [fair_LambdaMART](./fair/runs.md#fair_lambdamart)

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

- :fontawesome-solid-user-group: **Participant:** [uogTr](./fair/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/uogTr.FR.pdf](https://trec.nist.gov/pubs/trec28/papers/uogTr.FR.pdf)
- :material-file-search: **Runs:** [uognleMaxUtil](./fair/runs.md#uognlemaxutil) | [uognleSgbrFair](./fair/runs.md#uognlesgbrfair) | [uognleSgbrUtil](./fair/runs.md#uognlesgbrutil) | [uognleDivAAsp](./fair/runs.md#uognledivaasp) | [uognleDivAJc](./fair/runs.md#uognledivajc)

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

- :fontawesome-solid-user-group: **Participant:** [QUARTZ_ITN](./fair/participants.md#quartz_itn)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/DUTIR.FR.pdf](https://trec.nist.gov/pubs/trec28/papers/DUTIR.FR.pdf)
- :material-file-search: **Runs:** [QUARTZ-e0.00001](./fair/runs.md#quartz-e0.00001) | [QUARTZ-e0.00010](./fair/runs.md#quartz-e0.00010) | [QUARTZ-e0.00100](./fair/runs.md#quartz-e0.00100) | [QUARTZ-e0.00200](./fair/runs.md#quartz-e0.00200) | [QUARTZ-e0.00500](./fair/runs.md#quartz-e0.00500) | [QUARTZ-e0.01000](./fair/runs.md#quartz-e0.01000)

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

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./fair/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.FR.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.FR.pdf)
- :material-file-search: **Runs:** [first](./fair/runs.md#first)

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

## Incident Streams 

#### CBNU at TREC 2019 Incident Streams Track

_Won-Gyu Choi, Kyung-Soon Lee_

- :fontawesome-solid-user-group: **Participant:** [cbnu](./incident/participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/cbnu.IS.pdf](https://trec.nist.gov/pubs/trec28/papers/cbnu.IS.pdf)
- :material-file-search: **Runs:** [cbnuC1](./incident/runs.md#cbnuc1) | [cbnuS1](./incident/runs.md#cbnus1)

??? abstract "Abstract"
	
	This paper describes the participation of the CBNU team at the TREC Incident Streams Track 2019 [1]. Our approach is the same with CBNU at TREC-IS 2018 [2]. In our participation to TREC-IS Track 2018 and 2019, we focus on the conceptual representation for crisis-related terms. In order to classify a stream of tweets related to the incident, the terms in each tweet are represented as conceptual entities such as event entities, category indicator entities, information type entities, URL entities, and user entities. For tweet classification, we have compared support vector machines (SVM) and convolutional neural networks (CNNs).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChoiL19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChoiL19,
		author = {Won{-}Gyu Choi and Kyung{-}Soon Lee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CBNU} at {TREC} 2019 Incident Streams Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/cbnu.IS.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChoiL19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Trec 2019 Incident Streams Track

_Guangsheng Kuang, Kun Zhang, Jiabao Zhang, Xin Zheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./incident/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.IS.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.IS.pdf)
- :material-file-search: **Runs:** [ict_dl](./incident/runs.md#ict_dl)

??? abstract "Abstract"
	
	Social medial become our public ways to share our information in our lives. Crisis management via social medial is becoming indispensable for its tremendous information. While deep learning shows surprising outcome in many tasks. So in this paper, we cope this learning task with neural network in the view of classification problem.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GuangshengKJX19.bib) "
	```
	@inproceedings{DBLP:conf/trec/GuangshengKJX19,
		author = {Guangsheng Kuang and Kun Zhang and Jiabao Zhang and Xin Zheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Trec 2019 Incident Streams Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ICTNET.IS.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GuangshengKJX19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Classification of Incident-related Tweets: Exploiting Word and Sentence  Embeddings

_Anna M. Kruspe, Jens Kersten, Friederike Klan_

- :fontawesome-solid-user-group: **Participant:** [DLR_DW](./incident/participants.md#dlr_dw)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/DLR_DW.IS.pdf](https://trec.nist.gov/pubs/trec28/papers/DLR_DW.IS.pdf)
- :material-file-search: **Runs:** [DLR_BERT_R](./incident/runs.md#dlr_bert_r) | [DLR_USE_R](./incident/runs.md#dlr_use_r) | [DLR_SIF_R](./incident/runs.md#dlr_sif_r) | [DLR_Fusion](./incident/runs.md#dlr_fusion) | [DLR_MeanMaxAAE_Regression](./incident/runs.md#dlr_meanmaxaae_regression)

??? abstract "Abstract"
	
	In this paper, we present our five approaches submitted to the Text REtrieval Conference (TREC) Incident Streams (IS) 2019B edition. The goal is to classify crisis-related tweets into a variable set of information classes and to provide an importance score. This multi-class, multi-label and multi-task problem turns out to be even more challenging because of extremely unbalanced training data available. We use recently proposed, publicy available word and sentence embeddings and deep neural network models for this task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KruspeKK19.bib) "
	```
	@inproceedings{DBLP:conf/trec/KruspeKK19,
		author = {Anna M. Kruspe and Jens Kersten and Friederike Klan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Classification of Incident-related Tweets: Exploiting Word and Sentence Embeddings},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/DLR\_DW.IS.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KruspeKK19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT BHU at TREC 2019 Incident Streams Track

_Akanksha Mishra, Sukomal Pal_

- :fontawesome-solid-user-group: **Participant:** [IIT_BHU](./incident/participants.md#iit_bhu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/IIT_BHU.IS.pdf](https://trec.nist.gov/pubs/trec28/papers/IIT_BHU.IS.pdf)
- :material-file-search: **Runs:** [IITBHU_run1](./incident/runs.md#iitbhu_run1) | [IITBHU_run2](./incident/runs.md#iitbhu_run2)

??? abstract "Abstract"
	
	The paper describes the participation of the IIT BHU at the TREC 2019B Incident Streams track. We submitted two fully automatic runs for categorizing information within tweet into multiple high-level information types and determining the criticality score for each tweet given in the test set.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MishraP19.bib) "
	```
	@inproceedings{DBLP:conf/trec/MishraP19,
		author = {Akanksha Mishra and Sukomal Pal},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IIT} {BHU} at {TREC} 2019 Incident Streams Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/IIT\_BHU.IS.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MishraP19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Classification for Crisis-Related Tweets Leveraging Word Embeddings  and Data Augmentation

_Congcong Wang, David Lillis_

- :fontawesome-solid-user-group: **Participant:** [CS-UCD](./incident/participants.md#cs-ucd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CS-UCD.IS.pdf](https://trec.nist.gov/pubs/trec28/papers/CS-UCD.IS.pdf)
- :material-file-search: **Runs:** [UCDbcnelmo](./incident/runs.md#ucdbcnelmo) | [UCDbaseline](./incident/runs.md#ucdbaseline) | [UCDbilstmalpha](./incident/runs.md#ucdbilstmalpha) | [UCDbilstmbeta](./incident/runs.md#ucdbilstmbeta)

??? abstract "Abstract"
	
	This paper presents University College Dublin's (UCD) work at TREC 2019-B Incident Streams (IS) track. The purpose of the IS track is to find actionable messages and estimate their priority among a stream of crisis-related tweets. Based on the track's requirements, we break down the task into two sub-tasks. One is defined as a multi-label classification task that categorises upcoming tweets into different aid requests. The other is defined as a single-label classification task that estimates these tweets with four different levels of priority. For the track, we submitted four runs, each of which uses a different model for the tasks. Our baseline run trains classification models with hand-crafted features through machine learning methods, namely Logistic Regression and Naïve Bayes. Our other three runs train classification models with different deep learning methods. The deep methods include a vanilla bidirectional long short-term memory recurrent neural network (biLSTM), an adapted biLSTM, and a bi-attentive classification network (BCN) with pre-trained contextualised ELMo embedding. For all the runs, we apply different word embeddings (in-domain pre-trained, word-level pre-trained GloVe, character-level, or ELMo embeddings) and data augmentation strategies (SMOTE, loss weights, or GPT-2) to explore the influence they have on performance. Evaluation results show that our models perform better than the median for most situations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangL19.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangL19,
		author = {Congcong Wang and David Lillis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Classification for Crisis-Related Tweets Leveraging Word Embeddings and Data Augmentation},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CS-UCD.IS.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangL19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fine-tuned BERT Model for Multi-Label Tweets Classification

_Hamada M. Zahera, Ibrahim A. Elgendy, Rricha Jalota, Mohamed Ahmed Sherif_

- :fontawesome-solid-user-group: **Participant:** [DICE_UPB](./incident/participants.md#dice_upb)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/DICE_UPB.IS.pdf](https://trec.nist.gov/pubs/trec28/papers/DICE_UPB.IS.pdf)
- :material-file-search: **Runs:** [UPB-BERT](./incident/runs.md#upb-bert) | [UPB-FOCAL](./incident/runs.md#upb-focal)

??? abstract "Abstract"
	
	In this paper, we describe our approach to classify disaster-related tweets into multi-label information types (i.e, labels). We aim to filter first relevant tweets during disasters. Then, we assign tweets relevant information types. Information types can be SearchAndRescue, MovePeople and Volunteer. We employ a fine-tuned BERT model with 10 BERT layers. Further, we submitted our approach to the TREC-IS 2019 challenge, the evaluation results showed that our approach outperforms the F1-score of median score in identifying actionable information.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZaheraEJS19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZaheraEJS19,
		author = {Hamada M. Zahera and Ibrahim A. Elgendy and Rricha Jalota and Mohamed Ahmed Sherif},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Fine-tuned {BERT} Model for Multi-Label Tweets Classification},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/DICE\_UPB.IS.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZaheraEJS19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CMU-Informedia at TREC 2019 Incident Streams Track

_Junpei Zhou, Xinyu Wang, Po-Yao Huang, Alexander G. Hauptmann_

- :fontawesome-solid-user-group: **Participant:** [CMUInformedia](./incident/participants.md#cmuinformedia)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CMUInformedia.IS.pdf](https://trec.nist.gov/pubs/trec28/papers/CMUInformedia.IS.pdf)
- :material-file-search: **Runs:** [Informedia-rf1](./incident/runs.md#informedia-rf1) | [Informedia-rf2](./incident/runs.md#informedia-rf2) | [Informedia-rf3](./incident/runs.md#informedia-rf3) | [Informedia-nb](./incident/runs.md#informedia-nb)

??? abstract "Abstract"
	
	We describe CMU-Informedia's models for the TREC 2019 Incident Streams track. The goal of this track is classifying event/incident related tweets by High-level Information Types such as 'SearchAndRescue', 'InformationWanted' and so on. Each tweet should be assigned as many categories as are appropriate. What's more, this track requires predicting the Importance Scores, which is converted from the Importance Labels including 'Critical', 'High', 'Medium', 'Low' and 'Irrelevant'. For predicting the information types, we use feature extractors to extract features including meta-information, user entity, and textual embeddings, and then we build an information type predictor on those features. For predicting the importance scores, we build an importance score predictor which combines the scores derived from the predicted information types and the scores produced by a regression model. Evaluation results show that our models perform well on all metrics, and different models perform particularly well on different aspects.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouWHH19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouWHH19,
		author = {Junpei Zhou and Xinyu Wang and Po{-}Yao Huang and Alexander G. Hauptmann},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {CMU-Informedia at {TREC} 2019 Incident Streams Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CMUInformedia.IS.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhouWHH19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

