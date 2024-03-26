# Proceedings - News 2020 

#### TREC 2020 News Track Overview

_Ian Soboroff, Shudong Huang, Donna Harman_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.N.pdf](https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.N.pdf)
??? abstract "Abstract"
	
	The News track focuses on information retrieval in the service of helping people read the news. In 2018, in cooperation with the Washington Post1, we released a new collection of nearly 600,000 news articles, and crafted two tasks related to how news is presented on the web: background linking and entity ranking. For 2020, we added more documents to the collection and retired the entity ranking task in favor of a new wikification task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SoboroffHH20.bib) "
	```
	@inproceedings{DBLP:conf/trec/SoboroffHH20,
		author = {Ian Soboroff and Shudong Huang and Donna Harman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2020 News Track Overview},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.N.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SoboroffHH20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SU-NLP at TREC NEWS 2020

_Ali Eren Ak, Çaghan Köksal, Kenan Fayoumi, Reyyan Yeniterzi_

- :fontawesome-solid-user-group: **Participant:** [SUNLP](./participants.md#sunlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/SUNLP.N.pdf](https://trec.nist.gov/pubs/trec29/papers/SUNLP.N.pdf)
- :material-file-search: **Runs:** [SUNLP_BERT_Summ](./runs.md#sunlp_bert_summ) | [SUNLP_USE](./runs.md#sunlp_use) | [SUNLP_FullText](./runs.md#sunlp_fulltext) | [SUNLP_BERT_RR](./runs.md#sunlp_bert_rr) | [SUNLP_textorder](./runs.md#sunlp_textorder) | [SUNLP_doc2vec](./runs.md#sunlp_doc2vec)

??? abstract "Abstract"
	
	This paper presents our work and submissions for the TREC 2020 News Track: background linking and wikification tasks. For the background linking task, we investigated utilization of transformer-based architectures as either to map news articles to sentence embeddings, or to extract summaries of queried news articles or to re-rank the candidate documents. Even though none of these approaches outperformed our regular full-text baseline search approach, they provided some insights and future research directions. In the wikification task, after extracting and linking the entities to their corresponding entities, we analyzed two ranking approaches; one depends on entities positions within the text and the other depends on vector similarities between the news article and entity's linked page.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AkKFY20.bib) "
	```
	@inproceedings{DBLP:conf/trec/AkKFY20,
		author = {Ali Eren Ak and {\c{C}}aghan K{\"{o}}ksal and Kenan Fayoumi and Reyyan Yeniterzi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{SU-NLP} at {TREC} {NEWS} 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/SUNLP.N.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AkKFY20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Radboud University at TREC 2020

_Pepijn Boers, Chris Kamphuis, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [RUIR](./participants.md#ruir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/RUIR.N.pdf](https://trec.nist.gov/pubs/trec29/papers/RUIR.N.pdf)
- :material-file-search: **Runs:** [ru_graph](./runs.md#ru_graph) | [ru_g_novelty](./runs.md#ru_g_novelty) | [ru_g_ne](./runs.md#ru_g_ne) | [ru_g_diversity](./runs.md#ru_g_diversity) | [ru_g_textrank](./runs.md#ru_g_textrank)

??? abstract "Abstract"
	
	The IR research group from the Radboud University (RUIR) has an interest in creating graph-based solutions for domain specific challenges. We aim to increase effectiveness by incorporating domain knowledge into graph development. This work was developed as part of a Master's thesis project about graph representations for news articles of TREC's background linking task [1]. The introduced work explores the use of named entities, novelty scores and diversification of background documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoersKV20.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoersKV20,
		author = {Pepijn Boers and Chris Kamphuis and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Radboud University at {TREC} 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/RUIR.N.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BoersKV20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### OSC at TREC 2020 - News track's Background Linking Task

_Nathan Day, Dan Worley, Tim Allison_

- :fontawesome-solid-user-group: **Participant:** [OSC](./participants.md#osc)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/OSC.N.pdf](https://trec.nist.gov/pubs/trec29/papers/OSC.N.pdf)
- :material-file-search: **Runs:** [mlt_base](./runs.md#mlt_base) | [mlt_tune](./runs.md#mlt_tune) | [mlt_tune_ners](./runs.md#mlt_tune_ners) | [tune_ners_embed](./runs.md#tune_ners_embed)

??? abstract "Abstract"
	
	This notebook details a submission by OpenSource Connections (OSC) to the TREC 2020 News track's background linking task. OSC's strategies were built around Elasticsearch's More Like This (MLT) Query so they would be accessible to industry practitioners. OSC submitted four runs: MLT with default parameters, MLT with tuned parameters, MLT with a new named entity recognition (NER) field, and MLT re-scored by document embedding similarity. MLT with parameter tuning produced the best results of any OSC runs, but was slightly worse than the task median per topic of all submitted runs. OSC's NER and document embedding runs both produced better results than MLT with default parameters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DayWA20.bib) "
	```
	@inproceedings{DBLP:conf/trec/DayWA20,
		author = {Nathan Day and Dan Worley and Tim Allison},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{OSC} at {TREC} 2020 - News track's Background Linking Task},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/OSC.N.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DayWA20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2020 NEWS Track Background Linking Task

_Rahul Gautam, Mandar Mitra, Dwaipayan Roy_

- :fontawesome-solid-user-group: **Participant:** [IRLABISI](./participants.md#irlabisi)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/IRLABISI.N.pdf](https://trec.nist.gov/pubs/trec29/papers/IRLABISI.N.pdf)
- :material-file-search: **Runs:** [IRISINews1](./runs.md#irisinews1) | [IRISINews2](./runs.md#irisinews2) | [IRISINews4](./runs.md#irisinews4) | [IRISINews3](./runs.md#irisinews3)

??? abstract "Abstract"
	
	The Background Linking task is a problem that focuses on providing users with suggestions for articles to read next, when the user is reading a news article. The suggested articles should provide adequate context and background information for the article that the user is currently reading. In this paper, we describe several methods that we explored for this task, and report their results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GautamMR20.bib) "
	```
	@inproceedings{DBLP:conf/trec/GautamMR20,
		author = {Rahul Gautam and Mandar Mitra and Dwaipayan Roy},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2020 {NEWS} Track Background Linking Task},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/IRLABISI.N.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GautamMR20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The CLaC System at the TREC 2020 News Track

_Pavel Khloponin, Leila Kosseim_

- :fontawesome-solid-user-group: **Participant:** [CLAC_NEWS_2020](./participants.md#clac_news_2020)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/CLaC.N.pdf](https://trec.nist.gov/pubs/trec29/papers/CLaC.N.pdf)
- :material-file-search: **Runs:** [clac-gpt2-norm](./runs.md#clac-gpt2-norm) | [clac-es-bm25](./runs.md#clac-es-bm25) | [clac-d2v2019](./runs.md#clac-d2v2019) | [clac-combined](./runs.md#clac-combined)

??? abstract "Abstract"
	
	This paper describes our approach to the TREC 2020 News Track. The goal of the News Track is to provide background links and entity linking to target news articles within a collection of articles. We submitted 4 runs, 2 of which achieved scores higher than the median. The first approach is based on the classic Okapi BM25 using the entire article as a query. This run obtained an nDCG@5 of 0.5924. The second approach is based on a combination of BM25 with GPT-2 embeddings which lead to an nDCG@5 of 0.5873. These top models were chosen after exploring a variety of representations of documents as embedding vectors and proximity measures. Combining document embeddings and Okapi BM25 is shown to diversify the results without much impact on quality, and can help to overcome the limitations of a single model system implementation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KhloponinK20.bib) "
	```
	@inproceedings{DBLP:conf/trec/KhloponinK20,
		author = {Pavel Khloponin and Leila Kosseim},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The CLaC System at the {TREC} 2020 News Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/CLaC.N.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KhloponinK20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Aspect Based Background Document Retrieval for News Articles

_Kuang Lu, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/udel_fang.N.pdf](https://trec.nist.gov/pubs/trec29/papers/udel_fang.N.pdf)
- :material-file-search: **Runs:** [udel_fang_AW](./runs.md#udel_fang_aw) | [udel_fang_CE](./runs.md#udel_fang_ce) | [udel_fang_CW](./runs.md#udel_fang_cw)

??? abstract "Abstract"
	
	Background information is essential for readers to understand news articles. Moreover, background information is often multi-faceted [4], which introduces extra complexity to the problem of background retrieval. In this year's News Track, we explored how to build entity graphs on news articles to identify aspects, and leverage the aspects to retrieve background information. More specifically, given a query news article, the entities in it and their relations are used to build the entity graph, and aspects are extracted using community analysis. Subsequently, the discovered aspects are individually used to retrieve background news articles, and the per-aspect results are merged to form the final background article list for the query article.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lu020.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lu020,
		author = {Kuang Lu and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Aspect Based Background Document Retrieval for News Articles},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/udel\_fang.N.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Lu020.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TUW-IFS at TREC NEWS 2020 : Wikification Task

_Annisa Maulida Ningtyas, Alaa El-Ebshihy, Florina Piroi, Allan Hanbury, Linda Andersson_

- :fontawesome-solid-user-group: **Participant:** [TUW-IFS](./participants.md#tuw-ifs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/TUW-IFS.N.pdf](https://trec.nist.gov/pubs/trec29/papers/TUW-IFS.N.pdf)
- :material-file-search: **Runs:** [tuw-ifs-1](./runs.md#tuw-ifs-1) | [tuw-ifs-2](./runs.md#tuw-ifs-2) | [tuw-ifs-3](./runs.md#tuw-ifs-3) | [tuw-ifs-4](./runs.md#tuw-ifs-4)

??? abstract "Abstract"
	
	This paper presents our work and submission to the TREC 2020 News Track on Wikification. This task aims to link word and phrases to entities in external knowledge bases, such as external news articles or Wikipedia. The idea behind this task is to increase user reading comprehension by linking entities in the text they are reading to external knowledge bases that contain information on those entities. In order to perform the Wikification task, we have built a processing pipeline consisting of three main parts: identification, candidate generation and disambiguation, and candidate pruning or nil detection. Our model is fully unsupervised, and it does not require data training. We use commonness, topic modeling distance, and embedding similarity as a disambiguation method. The evaluation of the task submissions was done using newly introduced metrics: correctness of the link, the usefulness of the target link, the usefulness of the anchor span and the sensibility of the anchor text. Our method was designed to focus on coverage to also support the readers with limited knowledge in English, and thereby requiring more explanations and the possibility to have the explanation in another language. Based on the result, we conducted a failure analysis. We infer that our low scores on both evaluation are due to the use of Wikipedia as the only knowledge base to linked to, and lack of entity ordering during our final processing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NingtyasEPHA20.bib) "
	```
	@inproceedings{DBLP:conf/trec/NingtyasEPHA20,
		author = {Annisa Maulida Ningtyas and Alaa El{-}Ebshihy and Florina Piroi and Allan Hanbury and Linda Andersson},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TUW-IFS} at {TREC} {NEWS} 2020 : Wikification Task},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/TUW-IFS.N.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NingtyasEPHA20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

