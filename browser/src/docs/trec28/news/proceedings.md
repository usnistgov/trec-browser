# Proceedings - News 2019 

#### ICTNET at TREC 2019 News Track

_Yuyang Ding, Xiaoying Lian, Houquan Zhou, Zhaoge Liu, Hanxing Ding, Zhongni Hou_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.N.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.N.pdf)
- :material-file-search: **Runs:** [ICTNET_stem](./runs.md#ictnet_stem) | [ql](./runs.md#ql) | [rm3](./runs.md#rm3) | [rocchio](./runs.md#rocchio) | [ICTNET_estem](./runs.md#ictnet_estem)

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

- :fontawesome-solid-user-group: **Participant:** [QU](./participants.md#qu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/QU.N.pdf](https://trec.nist.gov/pubs/trec28/papers/QU.N.pdf)
- :material-file-search: **Runs:** [QU_KCore](./runs.md#qu_kcore) | [QU_KTruss](./runs.md#qu_ktruss) | [QU_KCore_F](./runs.md#qu_kcore_f) | [QU_KTruss_F](./runs.md#qu_ktruss_f)

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

- :fontawesome-solid-user-group: **Participant:** [Smith](./participants.md#smith)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/Smith.N.pdf](https://trec.nist.gov/pubs/trec28/papers/Smith.N.pdf)
- :material-file-search: **Runs:** [smith_base](./runs.md#smith_base) | [smith_poetry](./runs.md#smith_poetry) | [smith_keyword](./runs.md#smith_keyword) | [smith_full](./runs.md#smith_full)

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

- :fontawesome-solid-user-group: **Participant:** [CMU](./participants.md#cmu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CMU.N.pdf](https://trec.nist.gov/pubs/trec28/papers/CMU.N.pdf)
- :material-file-search: **Runs:** [CMU_NS-1-tpb](./runs.md#cmu_ns-1-tpb) | [CMU_NS-2-tp](./runs.md#cmu_ns-2-tp) | [CMU_NS-3-t](./runs.md#cmu_ns-3-t)

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

- :fontawesome-solid-user-group: **Participant:** [UQ](./participants.md#uq)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UQ.N.pdf](https://trec.nist.gov/pubs/trec28/papers/UQ.N.pdf)
- :material-file-search: **Runs:** [UQ_count_sent](./runs.md#uq_count_sent) | [UQ_count](./runs.md#uq_count) | [UQ_wiki](./runs.md#uq_wiki) | [UQ_sent](./runs.md#uq_sent) | [UQ_wiki_count](./runs.md#uq_wiki_count)

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

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/udel_fang.N.pdf](https://trec.nist.gov/pubs/trec28/papers/udel_fang.N.pdf)
- :material-file-search: **Runs:** [UDInfolab_all](./runs.md#udinfolab_all) | [UDInfolab_ent](./runs.md#udinfolab_ent)

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

- :fontawesome-solid-user-group: **Participant:** [UNC_SILS](./participants.md#unc_sils)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UNC_SILS.N.pdf](https://trec.nist.gov/pubs/trec28/papers/UNC_SILS.N.pdf)
- :material-file-search: **Runs:** [sils_news_run1](./runs.md#sils_news_run1) | [sils_news_run2](./runs.md#sils_news_run2) | [sils_news_run3](./runs.md#sils_news_run3) | [sils_news_run4](./runs.md#sils_news_run4)

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

- :fontawesome-solid-user-group: **Participant:** [TREMA-UNH](./participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf](https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf)
- :material-file-search: **Runs:** [unh-trema-news](./runs.md#unh-trema-news)

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

- :fontawesome-solid-user-group: **Participant:** [OzUNLP](./participants.md#ozunlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/OzUNLP.News.pdf](https://trec.nist.gov/pubs/trec28/papers/OzUNLP.News.pdf)
- :material-file-search: **Runs:** [OzU_wiki](./runs.md#ozu_wiki) | [OzU_wiki_1_ws](./runs.md#ozu_wiki_1_ws) | [OzU_wiki_5_ws](./runs.md#ozu_wiki_5_ws) | [OzU_wiki_top1](./runs.md#ozu_wiki_top1) | [OzU_wiki_top5](./runs.md#ozu_wiki_top5)

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

- :fontawesome-solid-user-group: **Participant:** [cityuni](./participants.md#cityuni)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/cityuni.News.pdf](https://trec.nist.gov/pubs/trec28/papers/cityuni.News.pdf)
- :material-file-search: **Runs:** [cityuni_1](./runs.md#cityuni_1) | [cityuni_ER1](./runs.md#cityuni_er1) | [cityuni_ER2](./runs.md#cityuni_er2)

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

