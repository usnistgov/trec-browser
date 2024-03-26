# Proceedings - Common Core 2018 

#### UWaterlooMDS at the TREC 2018 Common Core Track

_Mustafa Abualsaud, Gordon V. Cormack, Nimesh Ghelani, Amira Ghenai, Maura R. Grossman, Shahin Rahbariasl, Haotian Zhang, Mark D. Smucker_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UWaterlooMDS-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/UWaterlooMDS-CC.pdf)
- :material-file-search: **Runs:** [UWaterMDS_DS_A](./runs.md#uwatermds_ds_a) | [UWaterMDS_DS_B](./runs.md#uwatermds_ds_b) | [UWaterMDS_Rank](./runs.md#uwatermds_rank) | [UWaterMDS_SEQ](./runs.md#uwatermds_seq)

??? abstract "Abstract"
	
	This year we applied dynamic sampling (DS) [ 4] to create a sampled set of relevance judgments. One goal was to test the effectiveness and efficiency of this technique with a set of non-expert, secondary relevance assessors. We consider NIST assessors to be the experts and the primary assessors. Another goal was to make available to other researchers a sampled set of relevance judgments (prels) and thus allow the estimation of retrieval metrics that have the potential to be more robust than the standard NIST provided relevance judgments (qrels). In addition to creating the prels, we also submied several runs based on our manual judging and the models produced by our HiCAL system [1, 6].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbualsaudCGGGRZ18.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbualsaudCGGGRZ18,
		author = {Mustafa Abualsaud and Gordon V. Cormack and Nimesh Ghelani and Amira Ghenai and Maura R. Grossman and Shahin Rahbariasl and Haotian Zhang and Mark D. Smucker},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UWaterlooMDS at the {TREC} 2018 Common Core Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UWaterlooMDS-CC.pdf},
		timestamp = {Wed, 03 Feb 2021 08:31:25 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AbualsaudCGGGRZ18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion Based on NLP and Word Embeddings

_Billel Aklouche, Ibrahim Bounhas, Yahya Slimani_

- :fontawesome-solid-user-group: **Participant:** [JARIR](./participants.md#jarir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/JARIR-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/JARIR-CC.pdf)
- :material-file-search: **Runs:** [jarir_cb_re](./runs.md#jarir_cb_re) | [jarir_cbow](./runs.md#jarir_cbow) | [jarir_sg_re](./runs.md#jarir_sg_re) | [jarir_skipgram](./runs.md#jarir_skipgram) | [jarir_cb_ind](./runs.md#jarir_cb_ind) | [jarir_sg_ind](./runs.md#jarir_sg_ind)

??? abstract "Abstract"
	
	Query Expansion is an important process in information retrieval, which consists in adding new related terms to the original query in order to better identify relevant documents. In this paper, we discuss the participation of the JARIR research group to the TREC 2018 Common Core Track. We present different Query Expansion methods, which are based on Natural Language Pre-processing (NLP) tools and Word2Vec embedding models. Using the title of TREC topics, we select semantically related terms to the query. Our approach is composed of four steps: (1) Data Pre-processing, (2) Model Training, (3) Query Expansion and (4) Documents Ranking. For our best runs, results show that most of our topics scores are above the published median scores with some topics having the best scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AkloucheBSABSAB18.bib) "
	```
	@inproceedings{DBLP:conf/trec/AkloucheBSABSAB18,
		author = {Billel Aklouche and Ibrahim Bounhas and Yahya Slimani},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query Expansion Based on {NLP} and Word Embeddings},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/JARIR-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AkloucheBSABSAB18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at the 2018 TREC CORE Track

_Rodger Benham, Luke Gallagher, Joel M. Mackenzie, Binsheng Liu, Xiaolu Lu, Falk Scholer, J. Shane Culpepper, Alistair Moffat_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/RMIT-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/RMIT-CC.pdf)
- :material-file-search: **Runs:** [RMITUQVDBFDM3](./runs.md#rmituqvdbfdm3) | [RMITUQVDBFNZDM1](./runs.md#rmituqvdbfnzdm1) | [RMITUQVBestDM2](./runs.md#rmituqvbestdm2) | [RMITFDA4](./runs.md#rmitfda4) | [RMITEXTGIGADA5](./runs.md#rmitextgigada5)

??? abstract "Abstract"
	
	Ad-hoc retrieval is an important problem with many practical applications. It forms the basis of web search, question-answering, and a new generation of virtual assistants being developed by several of the largest software companies in the world. In this report, we continue our exploration of the importance of multiple expressions of information needs. Our thesis is that over-reliance on a single query can lead to suboptimal performance, and that by creating multiple query representations for an information need and combining the relevance signals through fusion and relevance modeling, highly effective systems can be produced. This approach may form the basis for more complex multi-stage retrieval systems in a variety of applications.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BenhamGML0SCM18.bib) "
	```
	@inproceedings{DBLP:conf/trec/BenhamGML0SCM18,
		author = {Rodger Benham and Luke Gallagher and Joel M. Mackenzie and Binsheng Liu and Xiaolu Lu and Falk Scholer and J. Shane Culpepper and Alistair Moffat},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{RMIT} at the 2018 {TREC} {CORE} Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/RMIT-CC.pdf},
		timestamp = {Mon, 26 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BenhamGML0SCM18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2018: Common Core Track

_Alexander Bondarenko, Matthias Hagen, Michael Völske, Benno Stein, Alexander Panchenko, Chris Biemann_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Webis-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/Webis-CC.pdf)
- :material-file-search: **Runs:** [webis-argument](./runs.md#webis-argument) | [webis-bm25f](./runs.md#webis-bm25f) | [webis-baseline](./runs.md#webis-baseline)

??? abstract "Abstract"
	
	This paper gives a brief overview of the Webis network's participation in the TREC 2018 Common Core track. The basic idea applied in our approach is to axiomatically re-rank the top-50 results of BM25F for those topics that seem to be argumentative. To this end, we use three axioms with the goal of covering some aspects of argumentativeness in text documents. If all three argumentative axioms favor a re-ordering of two documents, they “overrule” the initial ranking and the documents change their ranks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BondarenkoHVSPB18.bib) "
	```
	@inproceedings{DBLP:conf/trec/BondarenkoHVSPB18,
		author = {Alexander Bondarenko and Matthias Hagen and Michael V{\"{o}}lske and Benno Stein and Alexander Panchenko and Chris Biemann},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2018: Common Core Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/Webis-CC.pdf},
		timestamp = {Fri, 19 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BondarenkoHVSPB18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FEUP at TREC 2018 Common Core Track - Reranking for Diversity  using Hypergraph-of-Entity and Document Profiling

_José Luís Devezas, Sérgio Nunes, Antonio Guillén, Yoan Gutiérrez, Rafael Muñoz_

- :fontawesome-solid-user-group: **Participant:** [FEUP](./participants.md#feup)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/FEUP-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/FEUP-CC.pdf)
- :material-file-search: **Runs:** [feup-run1](./runs.md#feup-run1) | [feup-run2](./runs.md#feup-run2) | [feup-run3](./runs.md#feup-run3) | [feup-run5](./runs.md#feup-run5) | [feup-run7](./runs.md#feup-run7) | [feup-run8](./runs.md#feup-run8) | [feup-run4](./runs.md#feup-run4) | [feup-run6](./runs.md#feup-run6)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2018 Common Core track, where we experimented with hyperedge-based document ranking, over the hypergraph-of-entity. We compared a text-only implementation (feup-run1) with a different implementation that also included entities and triples from DBpedia (feup-run2). We also experimented with reranking for diversity, based on the maximal marginal relevance and document profiling, in order to find a balance between relevance and the dissimilarity of neighboring documents. This resulted in six additional runs (3 to 8), using feup-run1 and feup-run2 as the base runs for reranking. We then assessed the impact in effectiveness, along with the changes in diversity, particularly over the top-ranked documents. We evaluated retrieval effectiveness based on the mean average precision, over the relevance judgments provided by TREC. We also proposed a weighted diversity metric, based on the cosine distance between each document and all others, within results for the same topic. Documents with a lower rank were assigned a higher weight, more strongly contributing to the weighted diversity. Our best results were for feup-run1 and feup-run7, both with a MAP score of 0.0070 and a P@10 of 0.0680, as well as a weighted diversity of 0.1197 and 0.1218, respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DevezasNGGM18.bib) "
	```
	@inproceedings{DBLP:conf/trec/DevezasNGGM18,
		author = {Jos{\'{e}} Lu{\'{\i}}s Devezas and S{\'{e}}rgio Nunes and Antonio Guill{\'{e}}n and Yoan Guti{\'{e}}rrez and Rafael Mu{\~{n}}oz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{FEUP} at {TREC} 2018 Common Core Track - Reranking for Diversity using Hypergraph-of-Entity and Document Profiling},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/FEUP-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DevezasNGGM18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improving Ad Hoc Retrieval With Bag Of Entities

_Gustavo Gonçalves, João Magalhães, Chenyan Xiong, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [NOVASearch](./participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/NOVASearch-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/NOVASearch-CC.pdf)
- :material-file-search: **Runs:** [bt-BoWBoE](./runs.md#bt-bowboe) | [bt-BoW](./runs.md#bt-bow) | [bt-BoE](./runs.md#bt-boe) | [b-BoE](./runs.md#b-boe) | [t-BoE](./runs.md#t-boe) | [eb-boost](./runs.md#eb-boost) | [b-BoW](./runs.md#b-bow) | [b-BoWBoE-t-BoE](./runs.md#b-bowboe-t-boe) | [b-BoW-t-BoWBoE](./runs.md#b-bow-t-bowboe) | [BM25-b-BoW](./runs.md#bm25-b-bow)

??? abstract "Abstract"
	
	This work explores the value of entity information for improving a feature-based learning-to-rank search engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoncalvesMXC18.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoncalvesMXC18,
		author = {Gustavo Gon{\c{c}}alves and Jo{\~{a}}o Magalh{\~{a}}es and Chenyan Xiong and Jamie Callan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Improving Ad Hoc Retrieval With Bag Of Entities},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/NOVASearch-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GoncalvesMXC18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MRG_UWaterloo Participation in the TREC 2018 Common Core Track

_Maura R. Grossman, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [MRG_UWaterloo](./participants.md#mrg_uwaterloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/MRG_UWaterloo-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/MRG_UWaterloo-CC.pdf)
- :material-file-search: **Runs:** [uwmrg](./runs.md#uwmrg) | [uwmrgx](./runs.md#uwmrgx)

??? abstract "Abstract"
	
	The MRG_UWaterloo team from the University of Waterloo participated in the TREC 2018 Common Core Track. We used logistic regression to score and rank all documents from the Washington Post dataset, using pseudo-relevant and pseudo-nonrelevant training documents fetched from the Web using Google search. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanC18.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanC18,
		author = {Maura R. Grossman and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {MRG{\_}UWaterloo Participation in the {TREC} 2018 Common Core Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/MRG\_UWaterloo-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanC18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### H2oloo at TREC 2018: Cross-Collection Relevance Transfer for the  Common Core Track

_Ruifan Yu, Yuhao Xie, Jimmy Lin_

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/h2oloo-CC.pdf](https://trec.nist.gov/pubs/trec27/papers/h2oloo-CC.pdf)
- :material-file-search: **Runs:** [h2oloo_LR2AX0.6](./runs.md#h2oloo_lr2ax0.6) | [h2oloo_enax0.6](./runs.md#h2oloo_enax0.6) | [h2oloo_enax0.7](./runs.md#h2oloo_enax0.7) | [h2oloo_LR2_rm3](./runs.md#h2oloo_lr2_rm3) | [h2oloo_LRax0.6](./runs.md#h2oloo_lrax0.6) | [h2oloo_enrm30.6](./runs.md#h2oloo_enrm30.6) | [h2oloo_e7ax0.6](./runs.md#h2oloo_e7ax0.6) | [h2oloo_e7ax0.7](./runs.md#h2oloo_e7ax0.7) | [h2oloo_e7rm30.6](./runs.md#h2oloo_e7rm30.6) | [h2oloo_e7rm30.7](./runs.md#h2oloo_e7rm30.7)

??? abstract "Abstract"
	
	The h2oloo team at the University of Waterloo participated in the Common Core Track in TREC 2018. Our main effort involved reproducing the cross-collection relevance transfer technique of Grossman and Cormack [ 8 ] from the TREC 2017 Common Core Track, as captured in their WCrobust0405 run. Their idea was relatively simple: for information needs (topics) that are shared across more than one test collection, it is possible to train (per topic) relevance classifiers using one or more test collections (in their case, from the TREC 2004 and 2005 Robust Tracks) and apply the classifiers to a new document collection (in their case, the New York Times collection used in the TREC 2017 Common Core Track) to improve ranking effectiveness. Each classifier, in essence, learns a relevance model for a specific information need, and the experiments of Grossman and Cormack demonstrate that such models can generalize across document collections. According to the TREC 2017 Common Core Track overview paper [ 2 ], WCrobust0405 ranked third in terms of average precision of runs that contributed to the judgment pools. The two runs that were more effective than WCrobust0405 involved humans who interactively searched the target collection to find relevant documents. In other words, the relevance transfer technique yielded effectiveness levels that approach human searchers. Not only is the technique of Grossman and Cormack effective, it is also simple: According to their paper, a logistic regression classifier for each topic was trained on the union of relevance judgments from the TREC 2004 and 2005 Robust Tracks. Documents were represented using word-level tf-idf features and each logistic regression classifier was learned using Sofia-ML1 and then applied to the entire Common Core collection. The top 10000 scoring documents (per topic), in decreasing order of classifier score, was submitted as the final run. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuXL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuXL18,
		author = {Ruifan Yu and Yuhao Xie and Jimmy Lin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {H2oloo at {TREC} 2018: Cross-Collection Relevance Transfer for the Common Core Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/h2oloo-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuXL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Anserini at trec 2018: Centre, Common Core, and News Tracks

_Yang, Peilin, Lin, Jimmy_

- :fontawesome-solid-user-group: **Participant:** [Anserini](./participants.md#anserini)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf](https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf)
- :material-file-search: **Runs:** [anserini_ax](./runs.md#anserini_ax) | [anserini_ax17](./runs.md#anserini_ax17) | [anserini_sdm](./runs.md#anserini_sdm) | [anserini_rm3](./runs.md#anserini_rm3) | [anserini_bm25](./runs.md#anserini_bm25) | [anserini_qlax](./runs.md#anserini_qlax) | [anserini_qlax17](./runs.md#anserini_qlax17) | [anserini_qlsdm](./runs.md#anserini_qlsdm) | [anserini_qlrm3](./runs.md#anserini_qlrm3) | [anserini_ql](./runs.md#anserini_ql)

??? abstract "Abstract"
	
	Anserini is an open-source information retrieval toolkit built on Lucene [3, 4]. The goal of our effort is to support information retrieval research using the popular open-source Lucene search library by allowing researchers to easily replicate results with modern ranking models on diverse test collections. Although there are many open-source search engines developed and maintained by academic research groups, most of them are designed primarily to facilitate the publication of research papers, and as such, they often suffer from poor usability, incomplete documentation, and a host of other issues. The growing complexity of modern software ecosystems and the diverse capabilities that are required to build useful end-to-end search applications places academic research groups at a huge disadvantage relative to Lucene. Except for a handful of commercial web search engines that deploy custom infrastructure, Lucene has become the de facto platform in industry for building production search applications—used by organizations as diverse as Twitter, Reddit, Bloomberg, and Target. It has an active developer base, diverse features and capabilities, and lies at the center of a vibrant ecosystem. However, Lucene lacks systematic support for information retrieval research—in particu- lar, ad hoc experimentation using standard test collections. This is where Anserini comes in: we enable cutting-edge information retrieval research using Lucene. At TREC 2018, we participated in the CENTRE, Common Core, and News Tracks. Each is described in its own section below. Our development efforts centered around the v0.1.0 release of Anserini, which is based on Lucene 6.3.0 (not the latest release).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/) "
	```
	@inproceedings{yang2018anserini,
		title = {Anserini at trec 2018: Centre, Common Core, and News Tracks},
		author = {Yang, Peilin and Lin, Jimmy},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference (TREC 2018), Gaithersburg, MD},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/anserini-CTR-CC-N.pdf},
		biburl = {https://dblp.org/}
	}
	```

#### UMass at TREC 2018: CAR, Common Core and News Tracks

_Shahrzad Naseri, John Foley, James Allan_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf](https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf)
- :material-file-search: **Runs:** [umass_cbsdm](./runs.md#umass_cbsdm) | [umass_bsdm](./runs.md#umass_bsdm) | [umass_sdm](./runs.md#umass_sdm) | [umass_ql](./runs.md#umass_ql)

??? abstract "Abstract"
	
	UMass participated in three TREC tasks in 2018: the TREC CAR, TREC Core tasks and TREC News (Background Linking). In this paper we detail the contents of our submissions and our lessons learned from this year's participation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NaseriFA18.bib) "
	```
	@inproceedings{DBLP:conf/trec/NaseriFA18,
		author = {Shahrzad Naseri and John Foley and James Allan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UMass at {TREC} 2018: CAR, Common Core and News Tracks},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NaseriFA18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

