# Proceedings 2020 

## News 

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

- :fontawesome-solid-user-group: **Participant:** [SUNLP](./news/participants.md#sunlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/SUNLP.N.pdf](https://trec.nist.gov/pubs/trec29/papers/SUNLP.N.pdf)
- :material-file-search: **Runs:** [SUNLP_BERT_Summ](./news/runs.md#sunlp_bert_summ) | [SUNLP_USE](./news/runs.md#sunlp_use) | [SUNLP_FullText](./news/runs.md#sunlp_fulltext) | [SUNLP_BERT_RR](./news/runs.md#sunlp_bert_rr) | [SUNLP_textorder](./news/runs.md#sunlp_textorder) | [SUNLP_doc2vec](./news/runs.md#sunlp_doc2vec)

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

- :fontawesome-solid-user-group: **Participant:** [RUIR](./news/participants.md#ruir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/RUIR.N.pdf](https://trec.nist.gov/pubs/trec29/papers/RUIR.N.pdf)
- :material-file-search: **Runs:** [ru_graph](./news/runs.md#ru_graph) | [ru_g_novelty](./news/runs.md#ru_g_novelty) | [ru_g_ne](./news/runs.md#ru_g_ne) | [ru_g_diversity](./news/runs.md#ru_g_diversity) | [ru_g_textrank](./news/runs.md#ru_g_textrank)

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

- :fontawesome-solid-user-group: **Participant:** [OSC](./news/participants.md#osc)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/OSC.N.pdf](https://trec.nist.gov/pubs/trec29/papers/OSC.N.pdf)
- :material-file-search: **Runs:** [mlt_base](./news/runs.md#mlt_base) | [mlt_tune](./news/runs.md#mlt_tune) | [mlt_tune_ners](./news/runs.md#mlt_tune_ners) | [tune_ners_embed](./news/runs.md#tune_ners_embed)

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

- :fontawesome-solid-user-group: **Participant:** [IRLABISI](./news/participants.md#irlabisi)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/IRLABISI.N.pdf](https://trec.nist.gov/pubs/trec29/papers/IRLABISI.N.pdf)
- :material-file-search: **Runs:** [IRISINews1](./news/runs.md#irisinews1) | [IRISINews2](./news/runs.md#irisinews2) | [IRISINews4](./news/runs.md#irisinews4) | [IRISINews3](./news/runs.md#irisinews3)

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

- :fontawesome-solid-user-group: **Participant:** [CLAC_NEWS_2020](./news/participants.md#clac_news_2020)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/CLaC.N.pdf](https://trec.nist.gov/pubs/trec29/papers/CLaC.N.pdf)
- :material-file-search: **Runs:** [clac-gpt2-norm](./news/runs.md#clac-gpt2-norm) | [clac-es-bm25](./news/runs.md#clac-es-bm25) | [clac-d2v2019](./news/runs.md#clac-d2v2019) | [clac-combined](./news/runs.md#clac-combined)

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

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./news/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/udel_fang.N.pdf](https://trec.nist.gov/pubs/trec29/papers/udel_fang.N.pdf)
- :material-file-search: **Runs:** [udel_fang_AW](./news/runs.md#udel_fang_aw) | [udel_fang_CE](./news/runs.md#udel_fang_ce) | [udel_fang_CW](./news/runs.md#udel_fang_cw)

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

- :fontawesome-solid-user-group: **Participant:** [TUW-IFS](./news/participants.md#tuw-ifs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/TUW-IFS.N.pdf](https://trec.nist.gov/pubs/trec29/papers/TUW-IFS.N.pdf)
- :material-file-search: **Runs:** [tuw-ifs-1](./news/runs.md#tuw-ifs-1) | [tuw-ifs-2](./news/runs.md#tuw-ifs-2) | [tuw-ifs-3](./news/runs.md#tuw-ifs-3) | [tuw-ifs-4](./news/runs.md#tuw-ifs-4)

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

## Deep Learning 

#### Overview of the TREC 2020 Deep Learning Track

_Nick Craswell, Bhaskar Mitra, Emine Yilmaz, Daniel Campos_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.DL.pdf)
??? abstract "Abstract"
	
	This is the second year of the TREC Deep Learning Track, with the goal of studying ad hoc ranking in the large training data regime. We again have a document retrieval task and a passage retrieval task, each with hundreds of thousands of human-labeled training queries. We evaluate using single-shot TREC-style evaluation, to give us a picture of which ranking methods work best when large data is available, with much more comprehensive relevance labeling on the small number of test queries. This year we have further evidence that rankers with BERT-style pretraining outperform other rankers in the large data regime.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellMMYC20.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellMMYC20,
		author = {Nick Craswell and Bhaskar Mitra and Emine Yilmaz and Daniel Campos},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2020 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.DL.pdf},
		timestamp = {Wed, 27 Apr 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CraswellMMYC20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BIT.UA@TREC 2020 Precision Medicine Track

_Tiago Almeida, Sérgio Matos_

- :fontawesome-solid-user-group: **Participant:** [BIT.UA](./deep/participants.md#bit.ua)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/BIT.UA.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/BIT.UA.PM.pdf)
- :material-file-search: **Runs:** [BIT-run1](./deep/runs.md#bit-run1) | [BIT-run2](./deep/runs.md#bit-run2) | [BIT-run3](./deep/runs.md#bit-run3)

??? abstract "Abstract"
	
	The TREC Precision Medicine and the previous CDS track have produced a variety of approaches on document retrieval to support clinical decisions. To the best of our knowledge, the top-performing approaches always relied on traditional information retrieval solutions, such as BM25 with query expansion, to find the biomedical articles relevant to the given topics. Although deep learning solutions have been tried, these struggle to reach the top scores on this particular task. To further explore and assess the effectiveness of deep learning methods in the PM retrieval task, we reformulate this relevance problem of evidence finding as a question-answering problem, where a query is formulated with the topic information and a neural information retrieval model generates a ranked list of documents. More precisely, we adopted a two-stage retrieval pipeline, where we first reduce the searching space using BM25 with gene name expansion and then apply a lightweight neural IR model, with only 620 trainable parameters, that was previously trained and tested on the BioASQ challenge. In terms of overall performance, in phase 1 we achieved the overall best score of 0.5325 nDCG, ten percentage points above the reported median. In phase 2 we achieved a best score of 0.3289 nDCG@30, four percentage points above the reported median. Our source code is available from https://github.com/T-Almeida/TREC-PM-2020.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlmeidaM20a.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlmeidaM20a,
		author = {Tiago Almeida and S{\'{e}}rgio Matos},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {BIT.UA@TREC 2020 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/BIT.UA.PM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AlmeidaM20a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Multiple Models Ensembling Method in TREC Deep Learning

_Liyu Cao, Yixuan Qiao, Hao Chen, Peng Gao, Yuan Ni, Guo Tong Xie_

- :fontawesome-solid-user-group: **Participant:** [pinganNLP](./deep/participants.md#pingannlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/pinganNLP.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/pinganNLP.DL.pdf)
- :material-file-search: **Runs:** [pinganNLP1](./deep/runs.md#pingannlp1) | [pinganNLP2](./deep/runs.md#pingannlp2) | [pinganNLP3](./deep/runs.md#pingannlp3)

??? abstract "Abstract"
	
	This paper is to describe our participation in the passage ranking tasks of TREC 2020 Depp Learning Track. We take leverage of several pre-trained models, such as BERT, ELECTRA and XLNET, to re-rank passages. Firstly, we use corpus in this track and enhanced next sentence prediction task to pre-treain a new BERT large model. Secondly, we fine-tune the new BERT model as well as ELECTRA, XL-NET and ALBERT with selected triplet data. Then, we ensemble several different kind of models to score and rank top-1000 passage. Finally, we select and re-rank top-10 passages in the former step according to the similarity to the top-1 passage to reduce noise.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaoQCGNX20.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaoQCGNX20,
		author = {Liyu Cao and Yixuan Qiao and Hao Chen and Peng Gao and Yuan Ni and Guo Tong Xie},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Multiple Models Ensembling Method in {TREC} Deep Learning},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/pinganNLP.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CaoQCGNX20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICIP at TREC-2020 Deep Learning Track

_Xuanang Chen, Ben He, Le Sun, Yingfei Sun_

- :fontawesome-solid-user-group: **Participant:** [ICIP](./deep/participants.md#icip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/ICIP.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/ICIP.DL.pdf)
- :material-file-search: **Runs:** [ICIP_run1](./deep/runs.md#icip_run1) | [ICIP_run3](./deep/runs.md#icip_run3) | [ICIP_run2](./deep/runs.md#icip_run2)

??? abstract "Abstract"
	
	This paper describes the ICIP participation in TREC 2020 Deep Learning Track. We apply BERT [1] to the re-ranking subtask of the document ranking task, with an adoption of the passage-level BERT re-ranker [2]. We utilize both the passage and document ranking dataset for model training, and the noisy training samples in generated document training set will be filtered, to guarantee and boost the ranking effectiveness. Additionally, we also distill smaller BERT models, on top of the recent knowledge distillation (KD) method on BERT, called Simplified TinyBERT [3], to investigate the influence of KD on the document ranking task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenHSCH020.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenHSCH020,
		author = {Xuanang Chen and Ben He and Le Sun and Yingfei Sun},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICIP} at {TREC-2020} Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/ICIP.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ChenHSCH020.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at TREC Deep Learning Track 2020

_J. Shane Culpepper, Binsheng Liu_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./deep/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/RMIT.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/RMIT.DL.pdf)
- :material-file-search: **Runs:** [RMIT-Bart](./deep/runs.md#rmit-bart) | [TF_IDF_d_2_t_50](./deep/runs.md#tf_idf_d_2_t_50) | [DLH_d_5_t_25](./deep/runs.md#dlh_d_5_t_25) | [indri-sdmf](./deep/runs.md#indri-sdmf) | [RMIT_DPH](./deep/runs.md#rmit_dph) | [RMIT_DFRee](./deep/runs.md#rmit_dfree)

??? abstract "Abstract"
	
	RMIT University submitted multiple baseline runs to improve the diversity of system types in the judgment pool for the TREC Deep Learning Track in 2020. All of these runs used the publicly available Terrier and Indri search engines and no machine learning. In addition, we submitted a single non-baseline run which applied a custom pairwise ranker to a Bart transformer to rerank passages for the passage ranking task. The RMIT Bart run as well as several of the more basic baseline runs performed well overall in the document and passage ranking tasks based on the preliminary assessment provided by NIST.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CulpepperL20.bib) "
	```
	@inproceedings{DBLP:conf/trec/CulpepperL20,
		author = {J. Shane Culpepper and Binsheng Liu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{RMIT} at {TREC} Deep Learning Track 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/RMIT.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CulpepperL20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Naver Labs Europe @ TREC Deep Learning 2020

_Thibault Formal, Benjamin Piwowarski, Stéphane Clinchant_

- :fontawesome-solid-user-group: **Participant:** [NLE](./deep/participants.md#nle)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/NLE.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/NLE.DL.pdf)
- :material-file-search: **Runs:** [NLE_pr1](./deep/runs.md#nle_pr1) | [NLE_pr2](./deep/runs.md#nle_pr2) | [NLE_pr3](./deep/runs.md#nle_pr3)

??? abstract "Abstract"
	
	This paper describes our participation to the 2020 TREC Deep Learning challenge. While the track comprises 4 tasks in total (document and passage (re-)ranking), we only focused on the passage full ranking task, for which the goal is to retrieve and rank a set of 1000 passages directly from the collection of 8.8M entries. We submitted three runs, coming from a diverse set of experiments we conducted throughout the year regarding the use of BERT in ranking models. We explored simple dense embedding-based first stage retrieval, the impact of training transformer models from scratch with Masked Language Modeling (MLM) on the target collection, as well as diverse training settings and hyperparameter configurations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FormalPFC20.bib) "
	```
	@inproceedings{DBLP:conf/trec/FormalPFC20,
		author = {Thibault Formal and Benjamin Piwowarski and St{\'{e}}phane Clinchant},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Naver Labs Europe @ {TREC} Deep Learning 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/NLE.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FormalPFC20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Longformer for MS MARCO Document Re-ranking Task

_Ivan Sekulic, Fabio Crestani, Amir Soleimani, Mohammad Aliannejadi_

- :fontawesome-solid-user-group: **Participant:** [USI](./deep/participants.md#usi)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/USI.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/USI.DL.pdf)
- :material-file-search: **Runs:** [longformer_1](./deep/runs.md#longformer_1)

??? abstract "Abstract"
	
	This technical report describes the approach of the Università della Svizzera italiana and the University of Amsterdam for MS MARCO document ranking task and TREC Deep Learning track 2020. Two step document ranking, where the initial retrieval is done by a classical information retrieval method, followed by neural re-ranking model, is the new standard. The best performance is achieved by using transformer-based models as re-rankers, e.g., BERT. We employ Longformer, a BERT-like model for long documents, on the MS MARCO document re-ranking task. The complete code used for training the model can be found on: https://github.com/isekulic/longformer-marco.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SekulicCSA20.bib) "
	```
	@inproceedings{DBLP:conf/trec/SekulicCSA20,
		author = {Ivan Sekulic and Fabio Crestani and Amir Soleimani and Mohammad Aliannejadi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Longformer for {MS} {MARCO} Document Re-ranking Task},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/USI.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SekulicCSA20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team at the TREC 2020 Deep Learning  Track

_Xiao Wang, Yaxiong Wu, Xi Wang, Craig Macdonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./deep/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/uogTr.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/uogTr.DL.pdf)
- :material-file-search: **Runs:** [uogTrQCBMP](./deep/runs.md#uogtrqcbmp) | [uogTrT20](./deep/runs.md#uogtrt20) | [uogTr31oR](./deep/runs.md#uogtr31or)

??? abstract "Abstract"
	
	This paper describes our submission to the document ranking task of the TREC 2020 Deep Learning Track. We followed a three-stage architecture: candidate set retrieval, feature calculation and re-ranking using a learning-to-rank technique. In particular, in the feature calculation stage, we leverage the traditional information retrieval document weighting models and the deep contextualised language models to provide the features for the learning-to-rank technique in the final stage. We submitted three runs for the document ranking task: uogTr31oR, uogTrQCBMP and uogTrT20 and six baseline runs with no neural re-ranking techniques applied. Among our submitted runs, run uogTrQCBMP, which combines query expansion, ColBERT neural ranking and MaxPassage, was the most effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangWWMO20.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangWWMO20,
		author = {Xiao Wang and Yaxiong Wu and Xi Wang and Craig Macdonald and Iadh Ounis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow Terrier Team at the {TREC} 2020 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/uogTr.DL.pdf},
		timestamp = {Tue, 30 Nov 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangWWMO20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HSRM-LAVIS at TREC 2020 Deep Learning Track: Neural First-stage  Ranking Complementing Term-based Retrieval

_Marco Wrzalik, Dirk Krechel_

- :fontawesome-solid-user-group: **Participant:** [HSRM-LAVIS](./deep/participants.md#hsrm-lavis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/HSRM-LAVIS.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/HSRM-LAVIS.DL.pdf)
- :material-file-search: **Runs:** [CoRT-standalone](./deep/runs.md#cort-standalone) | [CoRT-bm25](./deep/runs.md#cort-bm25) | [CoRT-electra](./deep/runs.md#cort-electra)

??? abstract "Abstract"
	
	This paper describes our submission to the passage ranking task of the TREC 2020 Deep Learning Track. With our work we focus on improving first-stage ranking and investigate its effect on endto-end retrieval. Our approach aims to complement term-based retrieval methods with rankings from a representation-focused neural ranking model for first-stage ranking. Thus, we compile reranking candidates by mixing rankings from our complementary model with BM25 rankings. Our model incorporates ALBERT to exploit local term interactions and language modeling pretraining. For efficient retrieval, our passage representations are pre-computed and can be indexed in an Approximate Nearest Neighbor index. We investigate the characteristics of our approach based on the following three submitted runs: First, isolated rankings from our complementing first-stage ranking model for to reveal its standalone effectiveness. Second, mixed candidates from both BM25 and our model to inspect its complementary behavior. Third, rankings from an ELECTRA-based re-ranker using the candidates from the second run as an example of end-to-end results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WrzalikK20.bib) "
	```
	@inproceedings{DBLP:conf/trec/WrzalikK20,
		author = {Marco Wrzalik and Dirk Krechel},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{HSRM-LAVIS} at {TREC} 2020 Deep Learning Track: Neural First-stage Ranking Complementing Term-based Retrieval},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/HSRM-LAVIS.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WrzalikK20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### bigIR at TREC 2020: Simple but Deep Retrieval of Passages and Documents

_Fatima Haouari, Marwa Essam, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./deep/participants.md#qu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/QU.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/QU.DL.pdf)
- :material-file-search: **Runs:** [bigIR-DCT-T5-F](./deep/runs.md#bigir-dct-t5-f) | [bigIR-T5xp-T5-F](./deep/runs.md#bigir-t5xp-t5-f) | [bigIR-T5-BERT-F](./deep/runs.md#bigir-t5-bert-f) | [bigIR-BERT-R](./deep/runs.md#bigir-bert-r) | [bigIR-T5-R](./deep/runs.md#bigir-t5-r) | [bigIR-DH-T5-F](./deep/runs.md#bigir-dh-t5-f) | [bigIR-DT-T5-F](./deep/runs.md#bigir-dt-t5-f) | [bigIR-DH-T5-R](./deep/runs.md#bigir-dh-t5-r) | [bigIR-DT-T5-R](./deep/runs.md#bigir-dt-t5-r) | [bigIR-DTH-T5-R](./deep/runs.md#bigir-dth-t5-r) | [bigIR-DTH-T5-F](./deep/runs.md#bigir-dth-t5-f)

??? abstract "Abstract"
	
	In this paper, we present the participation of the bigIR team at Qatar University in the TREC Deep Learning 2020 track. We participated in both document and passage retrieval tasks, and each of its subtasks, full ranking and reranking. As it is our first participation in the track, our primary goal is to experiment with the latest approaches and pre-trained models for both tasks. We used Anserini IR toolkit for indexing and retrieval, and experimented with different techniques for passage expansion and reranking, which are either BERT-based or sequence-to-sequence based. All our submitted runs for the passage retrieval task, and most of our submitted runs for the document retrieval task outperformed TREC median submission. We observed that BERT reranker performed slightly better than T5 reranker when expanding passages with sequence-to-sequence based models. However, T5 achieved better results than BERT when passages were expanded with DeepCT, a BERT-based model. Moreover, the results showed that combining the title and the head segment as document representation for reranking yielded significant improvement over each separately.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HaouariEE20.bib) "
	```
	@inproceedings{DBLP:conf/trec/HaouariEE20,
		author = {Fatima Haouari and Marwa Essam and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {bigIR at {TREC} 2020: Simple but Deep Retrieval of Passages and Documents},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/QU.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HaouariEE20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluating Transformer-Kernel Models at TREC Deep Learning 2020

_Sebastian Hofstätter, Allan Hanbury_

- :fontawesome-solid-user-group: **Participant:** [TU_Vienna](./deep/participants.md#tu_vienna)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/TU_Vienna.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/TU_Vienna.DL.pdf)
- :material-file-search: **Runs:** [TUW-TK-2Layer](./deep/runs.md#tuw-tk-2layer) | [TUW-TK-Sparse](./deep/runs.md#tuw-tk-sparse) | [TUW-TKL-2k](./deep/runs.md#tuw-tkl-2k) | [TUW-TKL-4k](./deep/runs.md#tuw-tkl-4k)

??? abstract "Abstract"
	
	We tested multiple hypotheses using the Transformer-Kernel neural ranking pattern. The TK model family sits between BERT and previous ranking model in terms of the efficiency-effectiveness trade-off, faster than BERT albeit less effective. In the passage re-ranking task we tested the effectiveness of contextualized stopwords, introduced with TK-Sparse and find that removing 19% of terms after contextualization even slightly increases the model's effectiveness. In the document re-ranking task we tested if a long-text TKL model is better with 2,000 or 4,000 document tokens and find that our 2,000 token instance outperforms the other. Our results confirm the path for new storage saving methods for interpretable ranking models, and give an interesting insight into the questions of how many tokens of a document we need to read for a relevance assessment.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HofstatterH20.bib) "
	```
	@inproceedings{DBLP:conf/trec/HofstatterH20,
		author = {Sebastian Hofst{\"{a}}tter and Allan Hanbury},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Evaluating Transformer-Kernel Models at {TREC} Deep Learning 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/TU\_Vienna.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HofstatterH20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Impact of Tokenization, Pretraining Task, and Transformer Depth on  Text Ranking

_Jaap Kamps, Nikolaos Kondylidis, David Rau_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./deep/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UAmsterdam.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/UAmsterdam.DL.pdf)
- :material-file-search: **Runs:** [relemb_mlm_0_2](./deep/runs.md#relemb_mlm_0_2) | [bert_6](./deep/runs.md#bert_6) | [bm25_bert_token](./deep/runs.md#bm25_bert_token)

??? abstract "Abstract"
	
	This paper documents the University of Amsterdam's participation in the TREC 2020 Deep Learning Track. Rather than motivated by engineering the best scoring system, our work is motivated by our interest in analysis, informing our understanding of the opportunities and challenges of transformers for text ranking. Specifically, we focus on the passage retrieval task where we try to answer three of sets of questions. First, transformers use different tokenization than traditional IR approaches such as stemming and lemmatizing, leading to different document representations. What is the effect of modern preprocessing techniques on traditional retrieval algorithms? Our main observation is that the limited vocabulary of the BERT tokenizer is affecting many long-tail tokens, which leads to large gains in efficiency at the cost of a small decrease in effectiveness. Second, the effectiveness of transformers is a result of the self-supervised pre-training task promoting general language understanding, ignorant of the specific demands of ranking tasks. Can we make further correlate queries and relevant passages in the pre-training task? Our main observation is that there is a whole continuum between the original self-supervised training task of BERT and the final interaction ranker, and isolating ranking-aware pre-training tasks may leads to gains in efficiency (as these pretrained models can be reused for many tasks) as well as to gains in effectiveness (in particular when limited data on the target task is available). Third, transformers combine large sequence length with many layers, with unclear what this deep semantics adds in the context of ranking. How complex do the models need to be in order to perform well on this task? Our main observation is that the deep layers of BERT lead to some, but relatively modest, gains in performance, but that the exact role of the presumed superior language understanding for search is far from clear.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KampsKR20.bib) "
	```
	@inproceedings{DBLP:conf/trec/KampsKR20,
		author = {Jaap Kamps and Nikolaos Kondylidis and David Rau},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Impact of Tokenization, Pretraining Task, and Transformer Depth on Text Ranking},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/UAmsterdam.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KampsKR20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SIB Text Mining at TREC 2020 Deep Learning Track

_Julien Knafou, Matthew Jeffryes, Sohrab Ferdowsi, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BITEM](./deep/participants.md#bitem)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/BITEM.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/BITEM.DL.pdf)
- :material-file-search: **Runs:** [roberta-large](./deep/runs.md#roberta-large) | [fr_doc_roberta](./deep/runs.md#fr_doc_roberta) | [rr-pass-roberta](./deep/runs.md#rr-pass-roberta) | [fr_pass_roberta](./deep/runs.md#fr_pass_roberta)

??? abstract "Abstract"
	
	This second campaign of the TREC Deep Learning Track was an opportunity for us to experiment with deep neural language models reranking techniques in a realistic use case. This year's tasks were the same as the previous edition: (1) building a reranking system and (2) building an end-to-end retrieval system. Both tasks could be completed on both a document and a passage collection. In this paper, we describe how we coupled Anserini's information retrieval toolkit with a BERT-based classifier to build a state-of-the-art end-to-end retrieval system. Our only submission which is based on a RoBERTalarge pretrained model achieves for (1) a ncdg@10 of .6558 and .6295 for passages and documents respectively and for (2) a ndcg@10 of .6614 and .6404 for passages and documents respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KnafouJFRKJRK20.bib) "
	```
	@inproceedings{DBLP:conf/trec/KnafouJFRKJRK20,
		author = {Julien Knafou and Matthew Jeffryes and Sohrab Ferdowsi and Patrick Ruch},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{SIB} Text Mining at {TREC} 2020 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/BITEM.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KnafouJFRKJRK20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MPII at the TREC 2020 Deep Learning Track

_Canjia Li, Andrew Yates_

- :fontawesome-solid-user-group: **Participant:** [mpii](./deep/participants.md#mpii)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/mpii.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/mpii.DL.pdf)
- :material-file-search: **Runs:** [mpii_run1](./deep/runs.md#mpii_run1) | [mpii_run2](./deep/runs.md#mpii_run2) | [mpii_run3](./deep/runs.md#mpii_run3)

??? abstract "Abstract"
	
	MPII participated in the TREC 2020 Deep Learning track's document ranking task with several variants of our recent PARADE model. PARADE is based on the idea that aggregating passage-level relevance representations is preferable to aggregating relevance scores. We submitted runs using three different PARADE variants that performed well in previous evaluations. The results differ from both those in the PARADE paper and those from the NTCIR-15 WWW-3 track: on this document ranking task, the least complex representation aggregation technique performs best.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiY20.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiY20,
		author = {Canjia Li and Andrew Yates},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{MPII} at the {TREC} 2020 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/mpii.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiY20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Conformer-Kernel with Query Term Independence at TREC 2020 Deep  Learning Track

_Bhaskar Mitra, Sebastian Hofstätter, Hamed Zamani, Nick Craswell_

- :fontawesome-solid-user-group: **Participant:** [MSAI](./deep/participants.md#msai)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/MSAI.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/MSAI.DL.pdf)
- :material-file-search: **Runs:** [ndrm3-orc-full](./deep/runs.md#ndrm3-orc-full) | [ndrm3-orc-re](./deep/runs.md#ndrm3-orc-re) | [ndrm3-full](./deep/runs.md#ndrm3-full) | [ndrm3-re](./deep/runs.md#ndrm3-re) | [ndrm1-full](./deep/runs.md#ndrm1-full) | [ndrm1-re](./deep/runs.md#ndrm1-re)

??? abstract "Abstract"
	
	We benchmark Conformer-Kernel models under the strict blind evaluation setting of the TREC 2020 Deep Learning track. In particular, we study the impact of incorporating: (i) Explicit term matching to complement matching based on learned representations (i.e., the “Duet principle”), (ii) query term independence (i.e., the “QTI assumption”) to scale the model to the full retrieval setting, and (iii) the ORCAS click data as an additional document description field. We find evidence which supports that all three aforementioned strategies can lead to improved retrieval quality.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MitraHZC20.bib) "
	```
	@inproceedings{DBLP:conf/trec/MitraHZC20,
		author = {Bhaskar Mitra and Sebastian Hofst{\"{a}}tter and Hamed Zamani and Nick Craswell},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Conformer-Kernel with Query Term Independence at {TREC} 2020 Deep Learning Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/MSAI.DL.pdf},
		timestamp = {Wed, 27 Apr 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MitraHZC20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLM at TREC 2020 Health Misinformation and Deep Learning Tracks

_Yassine Mrabet, Mourad Sarrouti, Asma Ben Abacha, Soumya Gayen, Travis R. Goodwin, Alastair R. Rae, Willie Rogers, Dina Demner-Fushman_

- :fontawesome-solid-user-group: **Participant:** [NLM](./deep/participants.md#nlm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/NLM.HM.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/NLM.HM.DL.pdf)
- :material-file-search: **Runs:** [nlm-ens-bst-3](./deep/runs.md#nlm-ens-bst-3) | [nlm-ens-bst-2](./deep/runs.md#nlm-ens-bst-2) | [nlm-prfun-bert](./deep/runs.md#nlm-prfun-bert) | [nlm-bert-rr](./deep/runs.md#nlm-bert-rr) | [nlm-bm25-prf-1](./deep/runs.md#nlm-bm25-prf-1) | [nlm-bm25-prf-2](./deep/runs.md#nlm-bm25-prf-2)

??? abstract "Abstract"
	
	This paper describes the participation of the National Library of Medicine to TREC 2020. Our main focus was the health misinformation track. We also participated to the Deep Learning track to both evaluate and enhance our deep re-ranking baselines for information retrieval. Our methods include a wide variety of approaches, ranging from conventional Information Retrieval (IR) models, neural re-ranking models, Natural Language Inference (NLI) models, Claim-Truth models, hyperlinks-based scores such as Page Rank and HITS, and ensemble methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MrabetSAGGRRD20.bib) "
	```
	@inproceedings{DBLP:conf/trec/MrabetSAGGRRD20,
		author = {Yassine Mrabet and Mourad Sarrouti and Asma Ben Abacha and Soumya Gayen and Travis R. Goodwin and Alastair R. Rae and Willie Rogers and Dina Demner{-}Fushman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{NLM} at {TREC} 2020 Health Misinformation and Deep Learning Tracks},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/NLM.HM.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MrabetSAGGRRD20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### H2oloo at TREC 2020: When all you got is a hammer... Deep Learning,  Health Misinformation, and Precision Medicine

_Ronak Pradeep, Xueguang Ma, Xinyu Zhang, Hang Cui, Ruizhou Xu, Rodrigo Frassetto Nogueira, Jimmy Lin_

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./deep/participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf)
- :material-file-search: **Runs:** [d_d2q_duo](./deep/runs.md#d_d2q_duo) | [d_d2q_rm3_duo](./deep/runs.md#d_d2q_rm3_duo) | [d_rm3_duo](./deep/runs.md#d_rm3_duo) | [p_d2q_bm25_duo](./deep/runs.md#p_d2q_bm25_duo) | [p_bm25rm3_duo](./deep/runs.md#p_bm25rm3_duo) | [p_d2q_rm3_duo](./deep/runs.md#p_d2q_rm3_duo)

??? abstract "Abstract"
	
	The h2oloo team from the University of Waterloo participated in the TREC 2020 Deep Learning, Health Misinformation, and Precision Medicine Tracks. Our primary goal was to validate sequence-to-sequence based retrieval techniques that we have been working on in the context of multi-stage retrieval dubbed “Expando-Mono-Duo” [6, 10] comprising a candidate document generation stage (driven by “bag of words” techniques) followed by a pointwise and then a pairwise reranking stage built around T5 [ 11 ], a powerful sequence-to-sequence transformer language model. For the Health Misinformation task, we also employ learnings from our fact verification system, VerT5erini [9]. All of our experiments employed the open-source Anserini IR toolkit [14 , 16], which is based on the popular open-source Lucene search library, for initial retrieval that feeds the T5-based rerankers. Besides being the state of the art in various other collections (e.g., Robust04 and TREC-COVID), we found our models achieved much better effectiveness compared to the BM25 baselines as well as the median scores in all three tracks, demonstrating the versatility and the zero-shot transfer capabilities of our multi-stage ranking system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PradeepMZCXNL20.bib) "
	```
	@inproceedings{DBLP:conf/trec/PradeepMZCXNL20,
		author = {Ronak Pradeep and Xueguang Ma and Xinyu Zhang and Hang Cui and Ruizhou Xu and Rodrigo Frassetto Nogueira and Jimmy Lin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {H2oloo at {TREC} 2020: When all you got is a hammer... Deep Learning, Health Misinformation, and Precision Medicine},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf},
		timestamp = {Mon, 20 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PradeepMZCXNL20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PASH at TREC 2020 Deep Learning Track: Dense Matching for Nested  Ranking

_Yixuan Qiao, Hao Chen, Liyu Cao, Liping Chen, Pengyong Li, Jun Wang, Peng Gao, Yuan Ni, Guotong Xie_

- :fontawesome-solid-user-group: **Participant:** [PASH](./deep/participants.md#pash)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/PASH.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/PASH.DL.pdf)
- :material-file-search: **Runs:** [pash_r1](./deep/runs.md#pash_r1) | [pash_r2](./deep/runs.md#pash_r2) | [pash_r3](./deep/runs.md#pash_r3) | [pash_f1](./deep/runs.md#pash_f1) | [pash_f2](./deep/runs.md#pash_f2) | [pash_f3](./deep/runs.md#pash_f3)

??? abstract "Abstract"
	
	This paper describes our participation in the passage ranking task of TREC 2020 Deep Learning Track. We propose a Dense retriever by a BERT-based dual-encoder framework utilizing in-batch negatives corresponding to a list-wise ranking loss. To add an extra degree of difficulty, we redesign the pre-training tasks of BERT to absorb additional information rendered by Dense Retriever. After pre-trained with general knowledge and document-level data, we firstly fine-tune it with a strictly balanced binary data using a point-wise ranking strategy. Then we re-rank the top k passages using a fine-grained data by gradual unfreezing skill which form a Nested Ranking framework. In addition, further combined with traditional retrieval methods and ensemble learning, we obtain the competitive ranking results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiaoCCCLWGNXCLX20.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiaoCCCLWGNXCLX20,
		author = {Yixuan Qiao and Hao Chen and Liyu Cao and Liping Chen and Pengyong Li and Jun Wang and Peng Gao and Yuan Ni and Guotong Xie},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{PASH} at {TREC} 2020 Deep Learning Track: Dense Matching for Nested Ranking},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/PASH.DL.pdf},
		timestamp = {Tue, 22 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/QiaoCCCLWGNXCLX20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Faster BERT-based Re-ranking through Candidate Passage Extraction

_Kyle Reed, Harish Tayyar Madabushi_

- :fontawesome-solid-user-group: **Participant:** [UoB](./deep/participants.md#uob)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UoB.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/UoB.DL.pdf)
- :material-file-search: **Runs:** [uob_runid1](./deep/runs.md#uob_runid1) | [uob_runid2](./deep/runs.md#uob_runid2) | [uob_runid3](./deep/runs.md#uob_runid3)

??? abstract "Abstract"
	
	Most modern information retrieval systems employ a multi-step approach to retrieving documents relevant to a query, first retrieving a set of candidate documents before re-ranking the candidates. The most effective methods of re-ranking use a transformer-based classifier to score documents. Since many documents exceed the input length of transformers, they are split into passages and each passage is classified independently, aggregating the scores for an overall document score. As transformers are slow due to their quadratic attention mechanism, we investigate whether extracting only the most promising passages from documents as input for the classifier can alleviate slow performance on longer documents at inference time while maintaining comparable performance. We explore three methods of passage extraction and find these approaches prove effective, performing comparably to the state-of-the-art while significantly reducing the run-time, with the best results coming from a graph-based passage-ranking algorithm.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ReedM20.bib) "
	```
	@inproceedings{DBLP:conf/trec/ReedM20,
		author = {Kyle Reed and Harish Tayyar Madabushi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Faster BERT-based Re-ranking through Candidate Passage Extraction},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/UoB.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ReedM20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Incident Streams 

#### Incident Streams 2020: TRECIS in the Time of COVID-19

_Cody Buntain, Richard McCreadie, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.IS.pdf](https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.IS.pdf)
??? abstract "Abstract"
	
	Between 2018 and 2019, the Incident Streams track (TREC-IS) has developed standard approaches for classifying the types and criticality of information shared in online social spaces during crises, but the introduction of SARS-CoV-2 has shifted the landscape of online crises substantially. While prior editions of TREC-IS have lacked data on large-scale public-health emergencies as these events are exceedingly rare, COVID-19 has introduced an over-abundance of potential data, and significant open questions remain about how existing approaches to crisis informatics and datasets built on other emergencies adapt to this new context. This paper describes how the 2020 edition of TREC-IS has addressed these dual issues by introducing a new COVID-19-specific task for evaluating generalization of existing COVID-19 annotation and system performance to this new context, applied to 11 regions across the globe. TREC-IS has also continued expanding its set of target crises, adding 29 new events and expanding the collection of event types to include explosions, fires, and general storms, making for a total of 9 event types in addition to the new COVID-19 events. Across these events, TREC-IS has made available 478,110 COVID-related messages and 282,444 crisis-related messages for participant systems to analyze, of which 14,835 COVID-related and 19,784 crisis-related messages have been manually annotated. Analyses of these new datasets and participant systems demonstrate first that both the distributions of information type and priority of information vary between general crises and COVID-19-related discussion. Secondly, despite these differences, results suggest leveraging general crisis data in the COVID-19 context improves performance over baselines. Using these results, we provide guidance on which information types appear most consistent between general crises and COVID-19.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuntainMS20.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuntainMS20,
		author = {Cody Buntain and Richard McCreadie and Ian Soboroff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Incident Streams 2020: {TRECIS} in the Time of {COVID-19}},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.IS.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BuntainMS20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improving Classification of Crisis-Related Social Media Content via  Text Augmentation and Image Analysis

_Shivam Sharma, Cody Buntain_

- :fontawesome-solid-user-group: **Participant:** [njit](./incident/participants.md#njit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/NJIT.IS.pdf](https://trec.nist.gov/pubs/trec29/papers/NJIT.IS.pdf)
- :material-file-search: **Runs:** [njit-sub01.text.2020A.task1](./incident/runs.md#njit-sub01.text.2020a.task1) | [njit-sub01.text.2020A.task2](./incident/runs.md#njit-sub01.text.2020a.task2) | [njit-sub02.text+aug.2020A.task1](./incident/runs.md#njit-sub02.text+aug.2020a.task1) | [njit-sub02.text+aug.2020A.task2](./incident/runs.md#njit-sub02.text+aug.2020a.task2) | [njit-sub01.text.2020A.task3](./incident/runs.md#njit-sub01.text.2020a.task3) | [njit-sub02.text+aug.2020A.task3](./incident/runs.md#njit-sub02.text+aug.2020a.task3) | [njit.s1.aug](./incident/runs.md#njit.s1.aug) | [njit.s1.aug.t2](./incident/runs.md#njit.s1.aug.t2) | [njit.s1.aug.t3](./incident/runs.md#njit.s1.aug.t3) | [njit.s2.cmmd.t1](./incident/runs.md#njit.s2.cmmd.t1) | [njit.s2.cmmd.t2](./incident/runs.md#njit.s2.cmmd.t2) | [njit.s2.cmmd.t3](./incident/runs.md#njit.s2.cmmd.t3) | [njit.s3.img.t1](./incident/runs.md#njit.s3.img.t1) | [njit.s3.img.t2](./incident/runs.md#njit.s3.img.t2) | [njit.s3.img.t3](./incident/runs.md#njit.s3.img.t3) | [njit.s4.cml.t1](./incident/runs.md#njit.s4.cml.t1) | [njit.s4.cml.t2](./incident/runs.md#njit.s4.cml.t2) | [njit.s4.cml.t3](./incident/runs.md#njit.s4.cml.t3)

??? abstract "Abstract"
	
	Identifying, classifying, and prioritizing crisis-related content in social media is an increasingly important task, as users of online platforms continue to expect emergency-response officials to monitor these channels. Much of the current work in this area, however, focuses on applications of neural language models (NLMs) to the text of these social media messages, leaving many meta-content and multi-modal signals unaddressed. This work challenges this text- and NLM-centric view as it applies to crisis informatics and the Incident Streams track at the annual Text Retrieval Conference (TREC-IS) by first measuring the performance enhancements NLMs provide over classical text-classification pipelines and then by integrating external data sources and non-textual image analysis. Results suggest classical machine learning (ML) models are still competitive to NLMs, especially in identifying high-priority content, but adding a simple text augmentation strategy results in significant gains in NLM performance. Preliminary results are consistent with the community's focus on NLMs as our work suggests augmented NLMs perform best in classification, while integrating image analysis has marginal effects on performance. Augmenting samples with inferences from CrisisMMD, however, also significantly increases prioritization performance, suggesting strategies for integrating other data and signals remain valuable. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SharmaB20.bib) "
	```
	@inproceedings{DBLP:conf/trec/SharmaB20,
		author = {Shivam Sharma and Cody Buntain},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Improving Classification of Crisis-Related Social Media Content via Text Augmentation and Image Analysis},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/NJIT.IS.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SharmaB20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2020 Incident Streams Track

_Hesong Wang, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT2020](./incident/participants.md#bjut2020)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/BJUT.IS.pdf](https://trec.nist.gov/pubs/trec29/papers/BJUT.IS.pdf)
- :material-file-search: **Runs:** [BJUT-run](./incident/runs.md#bjut-run)

??? abstract "Abstract"
	
	In this paper, we will continue to use the new method in the 2019 version to continue the work of the 2020 TREC Incident Streams System task[1]. Social media has become an indispensable part of human life, such as Twitter, Weibo and so on. When natural disasters occur, such as fires, earthquakes, flash floods, tsunamis, mudslides and other natural disasters or shootings, robberies and other emergencies, if only through media reports, the time of the event will be very slow, leading to some preventable loss. People like to post disaster situations or events on social media. The purpose of the task is to filter such natural disasters or emergencies by classifying the text on twitter. Similarly, each tweet is prioritized and the tagged information is reported to the relevant personnel according to different priorities. Let the staff know about the progress of the incident to help. This article will introduce the framework and methods of the classification system, as well as the experimental results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Wang020.bib) "
	```
	@inproceedings{DBLP:conf/trec/Wang020,
		author = {Hesong Wang and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2020 Incident Streams Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/BJUT.IS.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Wang020.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multi-task Transfer Learning for Finding Actionable Information from  Crisis-related Messages on Social Media

_Congcong Wang, David Lillis_

- :fontawesome-solid-user-group: **Participant:** [UCD-CS](./incident/participants.md#ucd-cs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UCD-CS.IS.pdf](https://trec.nist.gov/pubs/trec29/papers/UCD-CS.IS.pdf)
- :material-file-search: **Runs:** [CD_CS_R1.2020A.task1](./incident/runs.md#cd_cs_r1.2020a.task1) | [CD_CS_R2.2020A.task1](./incident/runs.md#cd_cs_r2.2020a.task1) | [CD_CS_R3.2020A.task1](./incident/runs.md#cd_cs_r3.2020a.task1) | [CD_CS_R4.2020A.task1](./incident/runs.md#cd_cs_r4.2020a.task1) | [CD_CS_T2_R1.2020A.task2](./incident/runs.md#cd_cs_t2_r1.2020a.task2) | [UCD_CS_T3_R1](./incident/runs.md#ucd_cs_t3_r1) | [UCD_CS_T3_R2](./incident/runs.md#ucd_cs_t3_r2) | [UCD_CS_T3_R3](./incident/runs.md#ucd_cs_t3_r3) | [ucd-run1](./incident/runs.md#ucd-run1) | [ucd-run2](./incident/runs.md#ucd-run2) | [ucd-run3](./incident/runs.md#ucd-run3) | [ucd-run4](./incident/runs.md#ucd-run4) | [ucd-run5](./incident/runs.md#ucd-run5)

??? abstract "Abstract"
	
	The Incident streams (IS) track is a research challenge aimed at finding important information from social media during crises for emergency response purposes. More specifically, given a stream of crisis-related tweets, the IS challenge asks a participating system to 1) classify what the types of users' concerns or needs are expressed in each tweet, known as the information type (IT) classification task and 2) estimate how critical each tweet is with regard to emergency response, known as the priority level prediction task. In this paper, we describe our multi-task transfer learning approach for this challenge. Our approach leverages state-of-the-art transformer models including both encoder-based models such as BERT and a sequence-to-sequence based T5 for joint transfer learning on the two tasks. Based on this approach, we submitted several runs to the track. The returned evaluation results show that our runs substantially outperform other participating runs in both IT classification and priority level prediction.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangL20.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangL20,
		author = {Congcong Wang and David Lillis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Multi-task Transfer Learning for Finding Actionable Information from Crisis-related Messages on Social Media},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/UCD-CS.IS.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WangL20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team (uogTr) at the TREC 2020 Incident  Streams Track

_Alexander J. Hepburn, Richard McCreadie_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./incident/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/uogTr.IS.pdf](https://trec.nist.gov/pubs/trec29/papers/uogTr.IS.pdf)
- :material-file-search: **Runs:** [elmo_all_brf](./incident/runs.md#elmo_all_brf) | [elmo_all_eec](./incident/runs.md#elmo_all_eec) | [elmo_all_tfidf_brf](./incident/runs.md#elmo_all_tfidf_brf) | [elmo_all_tfidf_eec](./incident/runs.md#elmo_all_tfidf_eec) | [elmo_textonly_eec_covid](./incident/runs.md#elmo_textonly_eec_covid)

??? abstract "Abstract"
	
	In this paper, we describe runs submitted on behalf of the University of Glasgow Terrier Team (uogTr) for the TREC 2020 Incident Streams track. We detail our approach to addressing the challenges present in the classification of crisis and disaster management data in unstructured text. In particular, we explore the usage of pre-trained ELMo embeddings alongside descriptive metadata-level and event-level features for classification. We also utilise algorithms incorporating undersampling techniques in order to mitigate the significant class imbalance in the dataset. We submitted a total of three official runs to the 2020A track: ELMO_ALL_BRF, ELMO_ALL_EEC, and ELMO_ALL_TFIDF_BRF with varying features and classifiers used. Our results show that our run, ELMO_ALL_BRF shows competitive performance, performing above the median across a number of track-specific metrics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HepburnM20.bib) "
	```
	@inproceedings{DBLP:conf/trec/HepburnM20,
		author = {Alexander J. Hepburn and Richard McCreadie},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow Terrier Team (uogTr) at the {TREC} 2020 Incident Streams Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/uogTr.IS.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HepburnM20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Health Misinformation 

#### Overview of the TREC 2020 Health Misinformation Track

_Charles L. A. Clarke, Saira Rizvi, Mark D. Smucker, Maria Maistro, Guido Zuccon_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.HM.pdf](https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.HM.pdf)
??? abstract "Abstract"
	
	TREC 2020 was the second year for the Health Misinformation track, which was named the Decision Track in 2019 [1]. Information retrieval using document collections that contain misinformation are problematic. When a search engine returns documents that contain misinformation, users may have difficulty discerning correct from incorrect information and the incorrect information can lead to incorrect decisions [5]. Decisions regarding health-related topics can be consequential, and as such we want search engines that enable users to make correct decisions. The track is designed to address the problem of health misinformation in three areas: 1) adhoc retrieval, 2) the total recall of misinformation in the collection, and 3) the evaluation of retrieval in the presence of misinformation. The 2020 Health Misinformation track had both a recall task and an adhoc task for participants. With the onset of the coronavirus pandemic (COVID-19), the track organizers selected a document collection of news from the Common Crawl1 that covered the first four months of 2020. The track's topics were all related to COVID-19 and posed as questions such as “Can gargling salt water prevent COVID-19?” For both tasks, NIST assessors judged documents' usefulness for answering a topic's question, and if judged to be useful, assessors then recorded if the document contained a specific answer to the question and then judged the credibility of the document. We evaluated recall runs on their ability to find all documents containing incorrect information (misinformation). For adhoc runs, we measured their ability to return useful, correct, and credible information.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeRSMZ20.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeRSMZ20,
		author = {Charles L. A. Clarke and Saira Rizvi and Mark D. Smucker and Maria Maistro and Guido Zuccon},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2020 Health Misinformation Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.HM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeRSMZ20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2020: Health Misinformation Track Extended Abstract

_Janek Bevendorff, Michael Völske, Benno Stein, Alexander Bondarenko, Maik Fröbe, Sebastian Günther, Matthias Hagen_

- :fontawesome-solid-user-group: **Participant:** [Webis](./misinfo/participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/webis.HM.pdf](https://trec.nist.gov/pubs/trec29/papers/webis.HM.pdf)
- :material-file-search: **Runs:** [cn-m-title](./misinfo/runs.md#cn-m-title) | [cn-title-2](./misinfo/runs.md#cn-title-2) | [cn-descr-2](./misinfo/runs.md#cn-descr-2) | [cn-ax-rer](./misinfo/runs.md#cn-ax-rer) | [cn-kq](./misinfo/runs.md#cn-kq) | [cn-kq-t-td](./misinfo/runs.md#cn-kq-t-td) | [cn-kq-td](./misinfo/runs.md#cn-kq-td)

??? abstract "Abstract"
	
	We give a brief overview of the Webis group's participation in the TREC 2020 Health Misinformation track. e baseline retrieval results of our search engine ChatNoir (BM25F-based) are re-ranked in two dierent approaches: (1) axiomatically re-ranking the top-20 initial results for argumentative topics / queries, and (2) formulating keyqueries to retrieve relevant documents at the top ranks. Our axiomatic re-ranking uses three axioms that capture argumentativeness, while for the keyqueries approach, we use low-eort manual pilot judgments to identify several relevant documents per topic.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BevendorffV0BFG20.bib) "
	```
	@inproceedings{DBLP:conf/trec/BevendorffV0BFG20,
		author = {Janek Bevendorff and Michael V{\"{o}}lske and Benno Stein and Alexander Bondarenko and Maik Fr{\"{o}}be and Sebastian G{\"{u}}nther and Matthias Hagen},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2020: Health Misinformation Track Extended Abstract},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/webis.HM.pdf},
		timestamp = {Fri, 19 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BevendorffV0BFG20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CiTIUS at the TREC 2020 Health Misinformation Track

_Marcos Fernández-Pichel, David E. Losada, Juan Carlos Pichel, David Elsweiler_

- :fontawesome-solid-user-group: **Participant:** [CiTIUS](./misinfo/participants.md#citius)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/CiTIUS.HM.pdf](https://trec.nist.gov/pubs/trec29/papers/CiTIUS.HM.pdf)
- :material-file-search: **Runs:** [CiTIUSCrdAdh](./misinfo/runs.md#citiuscrdadh) | [CiTIUSCrdRelAdh](./misinfo/runs.md#citiuscrdreladh) | [CiTIUSCrdTot](./misinfo/runs.md#citiuscrdtot) | [CiTIUSCrdRelTot](./misinfo/runs.md#citiuscrdreltot) | [CiTIUSSimTot](./misinfo/runs.md#citiussimtot) | [CiTIUSSimAdh](./misinfo/runs.md#citiussimadh) | [CiTIUSSimRelAdh](./misinfo/runs.md#citiussimreladh)

??? abstract "Abstract"
	
	The TREC Health Misinformation track focuses on discerning reliable from unreliable information and correct from incorrect information. This problem is very common in Web Search results and it is especially critical when it is related to health content [1]. This year's task focuses on COVID-19 and SARS-CoV-2 misinformation. In our experiments, we applied a BM25 retrieval baseline as a first step. Afterwards, we used a document-level reliability classifier recently developed by our team [2]. Finally, we also experimented with BERT-based variants that attempt to estimate similarity between sentences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Fernandez-Pichel20.bib) "
	```
	@inproceedings{DBLP:conf/trec/Fernandez-Pichel20,
		author = {Marcos Fern{\'{a}}ndez{-}Pichel and David E. Losada and Juan Carlos Pichel and David Elsweiler},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {CiTIUS at the {TREC} 2020 Health Misinformation Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/CiTIUS.HM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Fernandez-Pichel20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RealSakaiLab at the TREC 2020 Health Misinformation Track

_Sijie Tao, Tetsuya Sakai_

- :fontawesome-solid-user-group: **Participant:** [RealSakaiLab](./misinfo/participants.md#realsakailab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/RealSakaiLab.HM.pdf](https://trec.nist.gov/pubs/trec29/papers/RealSakaiLab.HM.pdf)
- :material-file-search: **Runs:** [RSL_BM25](./misinfo/runs.md#rsl_bm25) | [RSL_BM25LC](./misinfo/runs.md#rsl_bm25lc) | [RSL_BM25LM](./misinfo/runs.md#rsl_bm25lm) | [RSL_BM25LMC](./misinfo/runs.md#rsl_bm25lmc)

??? abstract "Abstract"
	
	In this paper, we describe our experiments conducted for the AdHoc Retrieval task of the TREC 2020 Health Misinformation Track. This task offers a challenges to participants to design a ranking model that promotes retrieval of both credible and correct health information. To address both relevance and credibility, we combined several techniques to re-rank a BM25 baseline ranking. The results from a language identi cation model, a news category classi er and a majority score calculation were used to modify the BM25 scores of the baseline ranking
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TaoS20.bib) "
	```
	@inproceedings{DBLP:conf/trec/TaoS20,
		author = {Sijie Tao and Tetsuya Sakai},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {RealSakaiLab at the {TREC} 2020 Health Misinformation Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/RealSakaiLab.HM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/TaoS20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### VOH.CoLAB at TREC 2020 Health Misinformation Track

_Simao N. Goncalves, Flávio Martins_

- :fontawesome-solid-user-group: **Participant:** [vohcolab](./misinfo/participants.md#vohcolab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/vohcolab.HM.pdf](https://trec.nist.gov/pubs/trec29/papers/vohcolab.HM.pdf)
- :material-file-search: **Runs:** [vohcolabEvSim](./misinfo/runs.md#vohcolabevsim) | [vohEvDivTfidf](./misinfo/runs.md#vohevdivtfidf) | [vohEvDiv_colm](./misinfo/runs.md#vohevdiv_colm) | [vohbm25rm3](./misinfo/runs.md#vohbm25rm3) | [vohbm25](./misinfo/runs.md#vohbm25)

??? abstract "Abstract"
	
	In this paper, we describe the participation of VOH.CoLAB in the TREC 2020 Health Misinformation Track (HMT). This year's edition of the track focused on two main Consumer Health Search tasks regarding COVID-19 questions: 1) to find misinformation; 2) to find relevant, credible, and correct information. In our participation in the HMT track, we submitted runs to both tasks, performing experiments to explore two main research hypothesis: 1) Does misinformation avoid mentioning the evidence text? 2) Does correct and credible information look similar to the evidence text? To explore these two complementary ideas we represent both the documents and the evidence as vectors and compute scores using a formula based on Kullback-Leibler divergence.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoncalvesM20.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoncalvesM20,
		author = {Simao N. Goncalves and Fl{\'{a}}vio Martins},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {VOH.CoLAB at {TREC} 2020 Health Misinformation Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/vohcolab.HM.pdf},
		timestamp = {Thu, 18 Nov 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GoncalvesM20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Copenhagen Participation in TREC Health Misinformation  Track 2020

_Lucas Chaves Lima, Dustin Brandon Wright, Isabelle Augenstein, Maria Maistro_

- :fontawesome-solid-user-group: **Participant:** [KU](./misinfo/participants.md#ku)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/KU.HM.pdf](https://trec.nist.gov/pubs/trec29/papers/KU.HM.pdf)
- :material-file-search: **Runs:** [run1](./misinfo/runs.md#run1) | [run2](./misinfo/runs.md#run2) | [run3](./misinfo/runs.md#run3) | [run4](./misinfo/runs.md#run4) | [run5](./misinfo/runs.md#run5) | [run6](./misinfo/runs.md#run6) | [run7](./misinfo/runs.md#run7) | [run8](./misinfo/runs.md#run8) | [run9](./misinfo/runs.md#run9) | [run10](./misinfo/runs.md#run10) | [run11](./misinfo/runs.md#run11) | [adhoc_run1](./misinfo/runs.md#adhoc_run1) | [adhoc_run2](./misinfo/runs.md#adhoc_run2) | [adhoc_run3](./misinfo/runs.md#adhoc_run3) | [adhoc_run4](./misinfo/runs.md#adhoc_run4) | [adhoc_run5](./misinfo/runs.md#adhoc_run5) | [adhoc_run6](./misinfo/runs.md#adhoc_run6) | [adhoc_run7](./misinfo/runs.md#adhoc_run7) | [adhoc_run8](./misinfo/runs.md#adhoc_run8) | [adhoc_run9](./misinfo/runs.md#adhoc_run9) | [adhoc_run10](./misinfo/runs.md#adhoc_run10) | [adhoc_run11](./misinfo/runs.md#adhoc_run11) | [adhoc_run12](./misinfo/runs.md#adhoc_run12) | [adhoc_run13](./misinfo/runs.md#adhoc_run13)

??? abstract "Abstract"
	
	In this paper, we describe our participation in the TREC Health Misinformation Track 2020. We submitted 11 runs to the Total Recall Task and 13 runs to the Ad Hoc task. Our approach consists of 3 steps: (1) we create an initial run with BM25 and RM3; (2) we estimate credibility and misinformation scores for the documents in the initial run; (3) we merge the relevance, credibility and misinformation scores to re-rank documents in the initial run. To estimate credibility scores, we implement a classifier which exploits features based on the content and the popularity of a document. To compute the misinformation score, we apply a stance detection approach with a pretrained Transformer language model. Finally, we use different approaches to merge scores: weighted average, the distance among score vectors and rank fusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LimaWAM20.bib) "
	```
	@inproceedings{DBLP:conf/trec/LimaWAM20,
		author = {Lucas Chaves Lima and Dustin Brandon Wright and Isabelle Augenstein and Maria Maistro},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Copenhagen Participation in {TREC} Health Misinformation Track 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/KU.HM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LimaWAM20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLM at TREC 2020 Health Misinformation and Deep Learning Tracks

_Yassine Mrabet, Mourad Sarrouti, Asma Ben Abacha, Soumya Gayen, Travis R. Goodwin, Alastair R. Rae, Willie Rogers, Dina Demner-Fushman_

- :fontawesome-solid-user-group: **Participant:** [NLM](./misinfo/participants.md#nlm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/NLM.HM.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/NLM.HM.DL.pdf)
- :material-file-search: **Runs:** [NLM_CTM_R1](./misinfo/runs.md#nlm_ctm_r1) | [NLM_CTM_R2](./misinfo/runs.md#nlm_ctm_r2) | [NLM_BNU_T5_CTM](./misinfo/runs.md#nlm_bnu_t5_ctm) | [NLM_BNU_ENS_NLI](./misinfo/runs.md#nlm_bnu_ens_nli) | [NLM_BNU_E_NLI_C](./misinfo/runs.md#nlm_bnu_e_nli_c) | [NLM_CTM_R1_C](./misinfo/runs.md#nlm_ctm_r1_c) | [NLM_TME_NLIR](./misinfo/runs.md#nlm_tme_nlir) | [NLM_TME_NLIR_C](./misinfo/runs.md#nlm_tme_nlir_c) | [NLM_E3](./misinfo/runs.md#nlm_e3) | [NLM_TME](./misinfo/runs.md#nlm_tme) | [NLM_BNU_E_GH](./misinfo/runs.md#nlm_bnu_e_gh) | [NLM_TME_GH](./misinfo/runs.md#nlm_tme_gh) | [NLM_E4](./misinfo/runs.md#nlm_e4)

??? abstract "Abstract"
	
	This paper describes the participation of the National Library of Medicine to TREC 2020. Our main focus was the health misinformation track. We also participated to the Deep Learning track to both evaluate and enhance our deep re-ranking baselines for information retrieval. Our methods include a wide variety of approaches, ranging from conventional Information Retrieval (IR) models, neural re-ranking models, Natural Language Inference (NLI) models, Claim-Truth models, hyperlinks-based scores such as Page Rank and HITS, and ensemble methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MrabetSAGGRRD20.bib) "
	```
	@inproceedings{DBLP:conf/trec/MrabetSAGGRRD20,
		author = {Yassine Mrabet and Mourad Sarrouti and Asma Ben Abacha and Soumya Gayen and Travis R. Goodwin and Alastair R. Rae and Willie Rogers and Dina Demner{-}Fushman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{NLM} at {TREC} 2020 Health Misinformation and Deep Learning Tracks},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/NLM.HM.DL.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MrabetSAGGRRD20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### H2oloo at TREC 2020: When all you got is a hammer... Deep Learning,  Health Misinformation, and Precision Medicine

_Ronak Pradeep, Xueguang Ma, Xinyu Zhang, Hang Cui, Ruizhou Xu, Rodrigo Frassetto Nogueira, Jimmy Lin_

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./misinfo/participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf)
- :material-file-search: **Runs:** [h2oloo.m1](./misinfo/runs.md#h2oloo.m1) | [h2oloo.m2](./misinfo/runs.md#h2oloo.m2) | [h2oloo.m3](./misinfo/runs.md#h2oloo.m3) | [h2oloo.m4](./misinfo/runs.md#h2oloo.m4) | [h2oloo.m5](./misinfo/runs.md#h2oloo.m5) | [h2oloo.m9](./misinfo/runs.md#h2oloo.m9) | [h2oloo.m10](./misinfo/runs.md#h2oloo.m10) | [h2oloo.m7](./misinfo/runs.md#h2oloo.m7) | [h2oloo.m8](./misinfo/runs.md#h2oloo.m8)

??? abstract "Abstract"
	
	The h2oloo team from the University of Waterloo participated in the TREC 2020 Deep Learning, Health Misinformation, and Precision Medicine Tracks. Our primary goal was to validate sequence-to-sequence based retrieval techniques that we have been working on in the context of multi-stage retrieval dubbed “Expando-Mono-Duo” [6, 10] comprising a candidate document generation stage (driven by “bag of words” techniques) followed by a pointwise and then a pairwise reranking stage built around T5 [ 11 ], a powerful sequence-to-sequence transformer language model. For the Health Misinformation task, we also employ learnings from our fact verification system, VerT5erini [9]. All of our experiments employed the open-source Anserini IR toolkit [14 , 16], which is based on the popular open-source Lucene search library, for initial retrieval that feeds the T5-based rerankers. Besides being the state of the art in various other collections (e.g., Robust04 and TREC-COVID), we found our models achieved much better effectiveness compared to the BM25 baselines as well as the median scores in all three tracks, demonstrating the versatility and the zero-shot transfer capabilities of our multi-stage ranking system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PradeepMZCXNL20.bib) "
	```
	@inproceedings{DBLP:conf/trec/PradeepMZCXNL20,
		author = {Ronak Pradeep and Xueguang Ma and Xinyu Zhang and Hang Cui and Ruizhou Xu and Rodrigo Frassetto Nogueira and Jimmy Lin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {H2oloo at {TREC} 2020: When all you got is a hammer... Deep Learning, Health Misinformation, and Precision Medicine},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf},
		timestamp = {Mon, 20 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PradeepMZCXNL20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Conversational Assistance 

#### CAsT 2020: The Conversational Assistance Track Overview

_Jeffrey Dalton, Chenyan Xiong, Jamie Callan_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.C.pdf](https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.C.pdf)
??? abstract "Abstract"
	
	CAsT 2020 is the second year of the Conversational Assistance Track and builds on the lessons from the first year. Teams tried a wide range of techniques to address conversational search challenges. Some methods used proven techniques such as query difficulty prediction and query expansion. Given the text understanding challenges in the task, teams also used traditional NLP models that incorporate coreference resolution. One important development was the application of generative query models and ranking models using pre-trained neural language models. The results showed that both traditional and neural techniques provided complementary effectiveness. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001XC20.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001XC20,
		author = {Jeffrey Dalton and Chenyan Xiong and Jamie Callan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {CAsT 2020: The Conversational Assistance Track Overview},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.C.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001XC20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HBKU at TREC 2020: Conversational Multi-Stage Retrieval with Pseudo-Relevance  Feedback

_Haya Al-Thani, Bernard J. Jansen, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [HBKU](./cast/participants.md#hbku)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/HBKU.C.pdf](https://trec.nist.gov/pubs/trec29/papers/HBKU.C.pdf)
- :material-file-search: **Runs:** [HBKU_t5_1v2](./cast/runs.md#hbku_t5_1v2) | [HBKU_t5_1v1](./cast/runs.md#hbku_t5_1v1) | [HBKU_t2_1v2](./cast/runs.md#hbku_t2_1v2) | [HBKU_t2_1v1](./cast/runs.md#hbku_t2_1v1) | [HBKU_t2_1v2_mnl](./cast/runs.md#hbku_t2_1v2_mnl) | [HBKU_t5_1v2_mnl](./cast/runs.md#hbku_t5_1v2_mnl) | [HBKU_t5_1v1_mnl](./cast/runs.md#hbku_t5_1v1_mnl) | [HBKU_t2_1v1_mnl](./cast/runs.md#hbku_t2_1v1_mnl)

??? abstract "Abstract"
	
	Passage retrieval in a conversational context is extremely challenging due to limited data resources. Information seeking in a conversational setting may contain omissions, implied context, and topic shifts. TREC CAsT promotes research in this field by aiming to create a reusable dataset for open-domain conversational information seeking (CIS). The track achieves this goal by defining a passage retrieval task in a multi-turn conversation setting. Understanding conversation context and history is a key factor in this challenge. This solution addresses this challenge by implementing a multi-stage retrieval pipeline inspired by last year's winning algorithm. The first stage in this retrieval process is a historical query expansion step from last year's winning algorithm where context is extracted from historical queries in the conversation. The second stage is the addition of a pseudo-relevance feedback step where the query is expanded using top-k retrieved passages. Finally, a pre-trained BERT passage re-ranker is used. The solution performed better than the median results of other submitted runs with an NDCG@3 of 0.3127 for the best performing run.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Al-ThaniJE20.bib) "
	```
	@inproceedings{DBLP:conf/trec/Al-ThaniJE20,
		author = {Haya Al{-}Thani and Bernard J. Jansen and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{HBKU} at {TREC} 2020: Conversational Multi-Stage Retrieval with Pseudo-Relevance Feedback},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/HBKU.C.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Al-ThaniJE20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke at the Trec 2020 Conversational Assistant Track

_Negar Arabzadeh, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./cast/participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/WaterlooClarke.C.pdf](https://trec.nist.gov/pubs/trec29/papers/WaterlooClarke.C.pdf)
- :material-file-search: **Runs:** [WatACBase](./cast/runs.md#watacbase) | [WatACBaseRe](./cast/runs.md#watacbasere) | [WatACGPT2Re](./cast/runs.md#watacgpt2re) | [WatACReAll](./cast/runs.md#watacreall)

??? abstract "Abstract"
	
	This report describes the methodology and results of the runs submitted by the WaterlooClarke group to TREC Conversational Assistant Track (CAsT) 2020. Our runs this year were based solely on the raw utterances. We did not submit any runs using the manually rewritten utterances or canonical response. All in all, our team submitted the four following runs: 1. WatACBase, 2. WatACBaseRe, 3. WatACGPT2Re, 4. WatACReAll. The overall approach is based on last year's approach [1]: 1) Refining the query, 2) retrieving the passages and 3) reranking the passages. We did not apply the reranking step for the WatACBase run. Compared to last year, we tried to improve our performance by: 1) expanding the pool of the retrieved documents by merging the retrieved documents from two query variations and 2) re-ranking the passages with Bert [2]. Based on preliminary experiments on the TREC CAsT 2019 data set, employing these two approaches showed statistically significant improvement in performance. In the following, we will explain the details of our methodology and discuss the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ArabzadehC20.bib) "
	```
	@inproceedings{DBLP:conf/trec/ArabzadehC20,
		author = {Negar Arabzadeh and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {WaterlooClarke at the Trec 2020 Conversational Assistant Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/WaterlooClarke.C.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ArabzadehC20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion with Semantic-Based Ellipsis Reduction for Conversational  IR

_Chia-Yuan Chang, Ning Chen, Wei-Ting Chiang, Chih-Hen Lee, Yu-Hsuan Tseng, Chuan-Ju Wang, Hsien-Hao Chen, Ming-Feng Tsai_

- :fontawesome-solid-user-group: **Participant:** [ASCFDA](./cast/participants.md#ascfda)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/ASCFDA.C.pdf](https://trec.nist.gov/pubs/trec29/papers/ASCFDA.C.pdf)
- :material-file-search: **Runs:** [ASCFDA_baseline](./cast/runs.md#ascfda_baseline) | [ASCFDA_d2q_emb](./cast/runs.md#ascfda_d2q_emb) | [ASCFDA_qa](./cast/runs.md#ascfda_qa) | [ASCFDA_rm3](./cast/runs.md#ascfda_rm3)

??? abstract "Abstract"
	
	Word choice mismatch between query and documents is a common problem in QA/dialogue subjects such as the TREC Conversational Assistance Track (CAsT) 2020. We account for this kind of mismatch by expanding queries using semantic-based ellipsis reduction (SER), which involves gathering supplemental information from historical queries and potentially relevant documents. We formulate information retrieval as (1) retrieving potential information and (2) reranking its priority. To explain the importance of query expansion and verify our method's effectiveness, we conduct experiments with diverse settings in the retrieval part, followed by a Transformer model for reranking. We also resolve coreferences by replacing pronouns with their coreferential antecedents using a Transformer-based model. This work shows the importance of accounting for differences in wording and the potential of semantic-based approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChangCCLTWCT20.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChangCCLTWCT20,
		author = {Chia{-}Yuan Chang and Ning Chen and Wei{-}Ting Chiang and Chih{-}Hen Lee and Yu{-}Hsuan Tseng and Chuan{-}Ju Wang and Hsien{-}Hao Chen and Ming{-}Feng Tsai},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query Expansion with Semantic-Based Ellipsis Reduction for Conversational {IR}},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/ASCFDA.C.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ChangCCLTWCT20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IELAB for TREC Conversational Assistance Track (CAsT) 2020

_Sebastian Cross, Hang Li, Arvin Zhuang, Ahmed Mourad, Guido Zuccon, Bevan Koopman_

- :fontawesome-solid-user-group: **Participant:** [ielab](./cast/participants.md#ielab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/ielab.C.pdf](https://trec.nist.gov/pubs/trec29/papers/ielab.C.pdf)
- :material-file-search: **Runs:** [ielab-bertAQ](./cast/runs.md#ielab-bertaq) | [ielab-bm25T5QLM](./cast/runs.md#ielab-bm25t5qlm) | [ielab-bertPRFAQ](./cast/runs.md#ielab-bertprfaq) | [ielab-bm25AQ](./cast/runs.md#ielab-bm25aq)

??? abstract "Abstract"
	
	This paper describes the work done by the IELAB for the TREC Conversational Assistance Track (CAsT) 2020. IELAB investigated two methods to improve both the retrieval and re-ranking stages of a conversational IR system. The first method used an Adapted Query (AQ), which extracted context from the first utterance only to expand all subsequent queries for a conversational session. The second method utilized a query likelihood model (QLM) which used a pre-trained deep language model to estimate the likelihood that a query could be generated by a document. Specifically, we used the text-to-text transfer transformer (T5) as a scoring functions for re-ranking passages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CrossLZMZK20.bib) "
	```
	@inproceedings{DBLP:conf/trec/CrossLZMZK20,
		author = {Sebastian Cross and Hang Li and Arvin Zhuang and Ahmed Mourad and Guido Zuccon and Bevan Koopman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IELAB} for {TREC} Conversational Assistance Track (CAsT) 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/ielab.C.pdf},
		timestamp = {Wed, 18 Jan 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CrossLZMZK20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NOVA at TREC 2020 Conversational Assistance Track

_Rafael Ferreira, David Semedo, João Magalhães_

- :fontawesome-solid-user-group: **Participant:** [nova-search](./cast/participants.md#nova-search)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/nova_search.C.pdf](https://trec.nist.gov/pubs/trec29/papers/nova_search.C.pdf)
- :material-file-search: **Runs:** [T5_BERT100](./cast/runs.md#t5_bert100) | [AUTO_BERT100](./cast/runs.md#auto_bert100) | [AUTO_T5_RRF](./cast/runs.md#auto_t5_rrf)

??? abstract "Abstract"
	
	The use of conversational assistants to search for information is becoming more popular among the general public. In particular, in the last few years, the interest in conversational search is increasing, being this a step forward in allowing a more natural interaction with search systems. In this paper, we describe our work and submitted runs to TREC Conversational Assistance Track (CAsT) 2020 [4]. This track is mainly focused on Passage Conversational Information Seeking, being the context of the conversation key to retrieve relevant information. Our approach leverages a three-stage architecture composed of: (a) context tracking via query rewriting, (b) retrieval, and (c) re-ranking using a transformer model. The results obtained with this architecture achieved state-of-the-art results when compared to TREC CAsT 2019 baselines [5].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FerreiraSM20.bib) "
	```
	@inproceedings{DBLP:conf/trec/FerreiraSM20,
		author = {Rafael Ferreira and David Semedo and Jo{\~{a}}o Magalh{\~{a}}es},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{NOVA} at {TREC} 2020 Conversational Assistance Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/nova\_search.C.pdf},
		timestamp = {Sat, 26 Feb 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FerreiraSM20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTh at TREC 2020 Conversational Assistance Track

_Michalis Fotiadis, Georgios Peikos, Symeon Symeonidis, Avi Arampatzis_

- :fontawesome-solid-user-group: **Participant:** [DUTH](./cast/participants.md#duth)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/DUTH.C.pdf](https://trec.nist.gov/pubs/trec29/papers/DUTH.C.pdf)
- :material-file-search: **Runs:** [duth](./cast/runs.md#duth) | [duth_arq](./cast/runs.md#duth_arq) | [duth_manual](./cast/runs.md#duth_manual)

??? abstract "Abstract"
	
	This paper describes the DUTh's participation in the TREC 2020 Conversational Assistance Track (CAsT) track. Our approach incorporates linguistic analysis of the available queries along with query reformulation. The linguistic perspective of our approach implements the AllenNLP co-reference resolution model to every query of each conversational session. In addition, the SpaCy model was used for part-of-speech tagging and keyword extraction from the current and the previous turns. We reformulate the initial query into a weighted new query by keeping the keywords from the current turn and adding conversational context from previous turns. We argue that the conversational context of previous turns to have less impact than the keywords from the current turn while still adding some informational value. Finally, the new query was used for retrieval using Indri.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FotiadisPSA20.bib) "
	```
	@inproceedings{DBLP:conf/trec/FotiadisPSA20,
		author = {Michalis Fotiadis and Georgios Peikos and Symeon Symeonidis and Avi Arampatzis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {DUTh at {TREC} 2020 Conversational Assistance Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/DUTH.C.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FotiadisPSA20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Glasgow Representation and Information Learning Lab (GRILL) at the  Conversational Assistance Track 2020

_Carlos Gemmell, Jeffrey Dalton_

- :fontawesome-solid-user-group: **Participant:** [grill](./cast/participants.md#grill)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/grill.C.pdf](https://trec.nist.gov/pubs/trec29/papers/grill.C.pdf)
- :material-file-search: **Runs:** [grill_ctxDuo](./cast/runs.md#grill_ctxduo) | [grill_bmDuo](./cast/runs.md#grill_bmduo) | [grill_duoBART](./cast/runs.md#grill_duobart) | [grill_fuseDuo](./cast/runs.md#grill_fuseduo)

??? abstract "Abstract"
	
	In this paper we present our methods, experimental setup and results for the Conversational Assistance Track (CAsT) at TREC 2020. We present a novel neural query re-writing objective for conversational disambiguation that maximises semantic and grammatical knowledge transfer by aligning pre-training and fine tuning objectives. When resolving queries, our model regenerates previous context staying true to original infilling objective. Our re-writer assimilates query and context to auto-regressively resolve queries from previous utterances resulting performance approaching that of manual results. When used as part of a multi-stage retrieval pipeline leveraging point-wise and pair-wise scores, our system allows for robust conversational information seeking. We demonstrate our system by significantly outperforming median results in both manual and automatic runs from the track and show generalisation of our system with qualitative examples.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Gemmell020.bib) "
	```
	@inproceedings{DBLP:conf/trec/Gemmell020,
		author = {Carlos Gemmell and Jeffrey Dalton},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Glasgow Representation and Information Learning Lab {(GRILL)} at the Conversational Assistance Track 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/grill.C.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Gemmell020.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Extending the Use of Previous Relevant Utterances for Response Ranking  in Conversational Search

_Ivan Sekulic, Fabio Crestani, Mohammad Aliannejadi_

- :fontawesome-solid-user-group: **Participant:** [USI](./cast/participants.md#usi)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/USI.C.pdf](https://trec.nist.gov/pubs/trec29/papers/USI.C.pdf)
- :material-file-search: **Runs:** [castur_albert](./cast/runs.md#castur_albert) | [rewrite_albert](./cast/runs.md#rewrite_albert) | [hist_attention](./cast/runs.md#hist_attention) | [hist_concat](./cast/runs.md#hist_concat)

??? abstract "Abstract"
	
	This technical report describes the approach of the Universit`a della Svizzera italiana and the University of Amsterdam to TREC CAsT 2020. TREC CAsT provides a reusable benchmark for open-domain conversational information-seeking dialogues. Our system first performs query expansion by concatenating raw, relevant previous utterances, as predicted by an independent model trained on CAsTUR, with the current utterance. Initial ranking is performed by BM25, followed by ALBERT re-ranker trained on MS MARCO passage ranking task. Modifications of the approach include two different methods for utilising context: i) feeding the previous utterance and its top response to the model alongside the current one; ii) feeding up to 3 relevant utterances to the model and performing an attentive-sum to aggregate context information. Our last run uses automatically rewritten queries without context utilisation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SekulicCA20.bib) "
	```
	@inproceedings{DBLP:conf/trec/SekulicCA20,
		author = {Ivan Sekulic and Fabio Crestani and Mohammad Aliannejadi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Extending the Use of Previous Relevant Utterances for Response Ranking in Conversational Search},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/USI.C.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SekulicCA20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Leveraging Query Resolution and Reading Comprehension for Conversational  Passage Retrieval

_Svitlana Vakulenko, Nikos Voskarides, Zhucheng Tu, Shayne Longpre_

- :fontawesome-solid-user-group: **Participant:** [UvA.ILPS](./cast/participants.md#uva.ilps)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UvA.ILPS.C.pdf](https://trec.nist.gov/pubs/trec29/papers/UvA.ILPS.C.pdf)
- :material-file-search: **Runs:** [quretecQR](./cast/runs.md#quretecqr) | [baselineQR](./cast/runs.md#baselineqr) | [humanQR](./cast/runs.md#humanqr) | [quretecNoRerank](./cast/runs.md#quretecnorerank)

??? abstract "Abstract"
	
	This paper describes the participation of UvA.ILPS group at the TREC CAsT 2020 track. Our passage retrieval pipeline consists of (i) an initial retrieval module that uses BM25, and (ii) a re-ranking module that combines the score of a BERT ranking model with the score of a machine comprehension model adjusted for passage retrieval. An important challenge in conversational passage retrieval is that queries are often under-specified. Thus, we perform query resolution, that is, add missing context from the conversation history to the current turn query using QuReTeC, a term classification query resolution model. We show that our best automatic and manual runs outperform the corresponding median runs by a large margin.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VakulenkoVTL20.bib) "
	```
	@inproceedings{DBLP:conf/trec/VakulenkoVTL20,
		author = {Svitlana Vakulenko and Nikos Voskarides and Zhucheng Tu and Shayne Longpre},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Leveraging Query Resolution and Reading Comprehension for Conversational Passage Retrieval},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/UvA.ILPS.C.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/VakulenkoVTL20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### POLYU at TREC 2020 Conversational Assistant Track: Query Reformulation  with Heuristic Topic Phrases Discovery

_Kaishuai Xu, Wenjie Li, Yongli Li_

- :fontawesome-solid-user-group: **Participant:** [POLYU_SOME](./cast/participants.md#polyu_some)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/POLYU_SOME.C.pdf](https://trec.nist.gov/pubs/trec29/papers/POLYU_SOME.C.pdf)
- :material-file-search: **Runs:** [raw_polyu1](./cast/runs.md#raw_polyu1) | [man_polyu1](./cast/runs.md#man_polyu1)

??? abstract "Abstract"
	
	This paper demonstrates a 2-stage conversational search architecture for the Conversational Assistant Track in TREC 2020, including the initial rule-based retrieval and BERT-based re-ranking. We propose a straightforward query reformulation method with topic phrases discovery and inheritance. The method can efficiently extract the key phrase as a topic and inherit phrases based on specific rules. Experimental results show that our method performs as well as top-2 teams in CAsT 2019 evaluation datasets (NDCG@3: 0.433) with a simpler query expansion and smaller BERT model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuLL20.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuLL20,
		author = {Kaishuai Xu and Wenjie Li and Yongli Li},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{POLYU} at {TREC} 2020 Conversational Assistant Track: Query Reformulation with Heuristic Topic Phrases Discovery},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/POLYU\_SOME.C.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/XuLL20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2020 Notebook: CAsT Track

_Sheng-Chieh Lin, Jheng-Hong Yang, Jimmy Lin_

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./cast/participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/h2oloo.C.pdf](https://trec.nist.gov/pubs/trec29/papers/h2oloo.C.pdf)
- :material-file-search: **Runs:** [h2oloo_RUN1](./cast/runs.md#h2oloo_run1) | [h2oloo_RUN2](./cast/runs.md#h2oloo_run2) | [h2oloo_RUN3](./cast/runs.md#h2oloo_run3) | [h2oloo_RUN4](./cast/runs.md#h2oloo_run4)

??? abstract "Abstract"
	
	This notebook describes our participation (h2oloo) in TREC CAsT 2020. We first illustrate our multi-stage pipeline for conversational search: sequence-to-sequence query reformulation followed by an ad hoc text ranking pipeline; then, detail our proposed method for canonical response entry. Empirically, we show that our method effectively reformulates conversational queries considering both historical user utterances and system responses, yielding final ranking result 0.363 and 0.494 in terms of MAP and NDCG@3 respectively, which is our best submission to CAsT 2020.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinYL20.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinYL20,
		author = {Sheng{-}Chieh Lin and Jheng{-}Hong Yang and Jimmy Lin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2020 Notebook: CAsT Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/h2oloo.C.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinYL20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Topical Enrichment of Conversational Search Utterances: Participation  of the HPCLab-CNR Team in CAsT 2020

_Ida Mele, Cristina Ioana Muntean, Franco Maria Nardini, Raffaele Perego, Nicola Tonellotto_

- :fontawesome-solid-user-group: **Participant:** [HPCLab-CNR](./cast/participants.md#hpclab-cnr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/HPCLab-CNR.C.pdf](https://trec.nist.gov/pubs/trec29/papers/HPCLab-CNR.C.pdf)
- :material-file-search: **Runs:** [HPCLab-CNR-run1](./cast/runs.md#hpclab-cnr-run1) | [HPCLab-CNR-run3](./cast/runs.md#hpclab-cnr-run3) | [HPCLab-CNR-run2](./cast/runs.md#hpclab-cnr-run2) | [HPCLab-CNR-run4](./cast/runs.md#hpclab-cnr-run4)

??? abstract "Abstract"
	
	The TREC Conversational Assistant Track (CAsT) provides test collections for open-domain conversational search systems with the purpose of pursuing research on Conversational Information Seeking (CIS). For our participation in CAsT 2020, we implemented a modular architecture consisting of three steps: (i) automatic utterance rewriting, (ii) first-stage retrieval of candidate passages, and (iii) neural re-ranking of candidate passages. Each run is based on a different utterance rewriting technique for enriching the raw utterance with context extracted from the previous utterances in the conversation. Two of our approaches are completely unsupervised, while the other two rely on utterances manually classified by human assessors. These approaches also employ the canonical responses for the automatically rewritten utterances provided by CAsT 2020.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeleMN0T20.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeleMN0T20,
		author = {Ida Mele and Cristina Ioana Muntean and Franco Maria Nardini and Raffaele Perego and Nicola Tonellotto},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Topical Enrichment of Conversational Search Utterances: Participation of the HPCLab-CNR Team in CAsT 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/HPCLab-CNR.C.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MeleMN0T20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Wilfrid Laurier University at the NIST TREC 2020: Conversational  Assistance Track

_Max Niebergall, Jiashu Zhao_

- :fontawesome-solid-user-group: **Participant:** [WLU](./cast/participants.md#wlu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/WLU.C.pdf](https://trec.nist.gov/pubs/trec29/papers/WLU.C.pdf)
- :material-file-search: **Runs:** [WLU_ManUttOnly](./cast/runs.md#wlu_manuttonly) | [WLU_RawUttOnly](./cast/runs.md#wlu_rawuttonly)

??? abstract "Abstract"
	
	For TREC 2020, we submitted two runs to the Conversational Assistance Track (CAsT): WLU_ManUttOnly, for this run we used indri search to retrieve 1000 candidate results for each query, followed by reranking with a hierarchical session-based learning model with BERT encoding, and evaluated on the manually rewritten conversational query set. WLU_RawUttOnly, this run is the same as above except we evaluated on the raw conversational query set without any rewriting. This report details the system we designed to generate these runs, as well as an evaluation of each run.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NiebergallZ20.bib) "
	```
	@inproceedings{DBLP:conf/trec/NiebergallZ20,
		author = {Max Niebergall and Jiashu Zhao},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Wilfrid Laurier University at the {NIST} {TREC} 2020: Conversational Assistance Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/WLU.C.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NiebergallZ20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Precision Medicine 

#### Overview of the TREC 2020 Precision Medicine Track

_Kirk Roberts, Dina Demner-Fushman, Ellen M. Voorhees, Steven Bedrick, William R. Hersh_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.PM.pdf)
??? abstract "Abstract"
	
	The precision medicine paradigm focuses on identifying treatments that are best suited to an individual patient's unique attributes. The reasoning behind this paradigm is that diseases do not uniformly manifest in people and thus “one size fits all” treatments are often not appropriate. For many diseases, such as cancer, proper selection of a treatment strategy can drastically improve results compared to the standard, frontline treatment. Generally speaking, the issues that are taken into consideration for precision medicine are the genomic, environmental, and lifestyle contexts of the patient. While precision medicine as a paradigm can be seen to broadly apply to medicine as a whole, the area where it has seen the most attention is cancer. Many cancer treatments may be lifesaving in one patient but deadly in another, primarily based on the genetic mutations of the patient's tumor. Different treatments for the same type of cancer often target the genetic pathways applicable to the specific tumor's genes. As a result, there has been a significant amount of effort devoted to identifying these genetic pathways, identifying potential drugs that could target different aspects of these pathways, and assessing the clinical efficacy of these drugs in human studies. This includes the Precision Medicine Initiative (Collins and Varmus, 2015) launched by President Barack Obama in 2015, now known as the All of Us Research Program. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsDVBH20.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsDVBH20,
		author = {Kirk Roberts and Dina Demner{-}Fushman and Ellen M. Voorhees and Steven Bedrick and William R. Hersh},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2020 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.PM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RobertsDVBH20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### VOH.CoLAB at TREC 2020 Precision Medicine Track

_Miguel D. Cardoso, Flávio Martins_

- :fontawesome-solid-user-group: **Participant:** [vohcolab](./pm/participants.md#vohcolab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/vohcolab.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/vohcolab.PM.pdf)
- :material-file-search: **Runs:** [run_bm25](./pm/runs.md#run_bm25) | [bm25_synonyms](./pm/runs.md#bm25_synonyms)

??? abstract "Abstract"
	
	This paper describes our participation in the Scientific Abstracts task of the TREC 2020 Precision Medicine Track. We present our approach and the methods implemented, including both submitted runs and several post-mortem experiments using different methods. We performed experiments with Drugbank-based synonym expansion, Rocchio-based pseudo-relevance feedback, and neural re-ranking using the BioBERT biomedical pre-trained language models. In our evaluation, the Rocchio-based pseudo-relevance feedback method was the best performing method. Finally, we found that metadata and other textual fields in the document (e.g., journal name), are useful for retrieval and, when indexed, can improve recall-oriented metrics considerably leading to improvements in retrieval performance across the board.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CardosoM20.bib) "
	```
	@inproceedings{DBLP:conf/trec/CardosoM20,
		author = {Miguel D. Cardoso and Fl{\'{a}}vio Martins},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {VOH.CoLAB at {TREC} 2020 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/vohcolab.PM.pdf},
		timestamp = {Thu, 18 Nov 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CardosoM20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Poznań Contribution to TREC-PM 2020

_Jakub Dutkiewicz, Czeslaw Jedrzejek_

- :fontawesome-solid-user-group: **Participant:** [POZNAN](./pm/participants.md#poznan)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/Poznan.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/Poznan.PM.pdf)
- :material-file-search: **Runs:** [pozadditional](./pm/runs.md#pozadditional) | [pozreranked](./pm/runs.md#pozreranked) | [pozbaseline](./pm/runs.md#pozbaseline)

??? abstract "Abstract"
	
	This paper describes our contribution to TREC PM 2020. We discuss the retrieval architecture used for our contribution. We split our system into four layers - preprocessing, representation, baseline and neural layer. We go over goals and specification of each layer. We conclude the section with description of our hardware setup. Then, we describe experiments conducted within this contribution - we discuss used data and retrieval models.The reranking gives little but noticeable improvement. Our results are significantly better than the median. Paper is concluded with a discussion over weaknesses and strengths of our approach, we briefly formulate what has to be done in the future.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DutkiewiczJ20.bib) "
	```
	@inproceedings{DBLP:conf/trec/DutkiewiczJ20,
		author = {Jakub Dutkiewicz and Czeslaw Jedrzejek},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Pozna{\'{n}} Contribution to {TREC-PM} 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/Poznan.PM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DutkiewiczJ20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team and UFMG at the TREC 2020 Precision  Medicine Track

_Alberto Ueda, Rodrygo L. T. Santos, Craig Macdonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./pm/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/uogTr.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/uogTr.PM.pdf)
- :material-file-search: **Runs:** [uog_ufmg_DFRee](./pm/runs.md#uog_ufmg_dfree) | [uog_ufmg_s_dfr5](./pm/runs.md#uog_ufmg_s_dfr5) | [uog_ufmg_secL2R](./pm/runs.md#uog_ufmg_secl2r) | [uog_ufmg_s_dfr0](./pm/runs.md#uog_ufmg_s_dfr0) | [uog_ufmg_sb_df5](./pm/runs.md#uog_ufmg_sb_df5)

??? abstract "Abstract"
	
	For TREC 2020, we explore different re-ranking strategies by integrating PyTerrier — a framework which allows us to build advanced retrieval pipelines — with state-of-the-art BERT-based contextual language models. To produce the initial ranking, we use traditional retrieval models, such as Divergence From Randomness (DFR) weighting models. Then, we assign new scores for each document with BERT-based models, such as SciBERT and ColBERT. Finally, we re-rank the documents using combinations of those scores, via linear combination or learning-to-rank. We also conduct experiments with models able to leverage the structure information of the documents, i.e., by assigning different scores for their individual sections (e.g., Background, Results, Conclusions). We submitted five official runs, uog_ufmg_DFRee, uog_ufmg_s_dfr0, uog_ufmg_s_dfr5, uog_ufmg_sb_df5, uog_ufmg_secL2R. Our results in TREC 2020 confirm our main observations in our tests using the TREC 2019 test collection, showing that re-ranking strategies such as simple linear combinations of DFR and SciBERT scores (uog_ufmg_sb_df5) are competitive and outperform the TREC median performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UedaSMO20.bib) "
	```
	@inproceedings{DBLP:conf/trec/UedaSMO20,
		author = {Alberto Ueda and Rodrygo L. T. Santos and Craig Macdonald and Iadh Ounis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow Terrier Team and {UFMG} at the {TREC} 2020 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/uogTr.PM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/UedaSMO20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MRG_UWaterloo Participation in the TREC 2020 Precision Medicine  Track

_Maura R. Grossman, Gordon V. Cormack, Ba' Pham_

- :fontawesome-solid-user-group: **Participant:** [MRG_UWaterloo](./pm/participants.md#mrg_uwaterloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/MRG_UWaterloo.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/MRG_UWaterloo.PM.pdf)
- :material-file-search: **Runs:** [uwman](./pm/runs.md#uwman) | [uwbm25](./pm/runs.md#uwbm25) | [uwr](./pm/runs.md#uwr) | [uwrn](./pm/runs.md#uwrn) | [uwpr](./pm/runs.md#uwpr)

??? abstract "Abstract"
	
	The MRG_UWaterloo group from the University of Waterloo, in collaboration with Ba' Pham of the University of Toronto Health Economics and Assessment Collaborative, participated for the first time in the TREC 2020 Precision Medicine Track. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanCP20.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanCP20,
		author = {Maura R. Grossman and Gordon V. Cormack and Ba' Pham},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {MRG{\_}UWaterloo Participation in the {TREC} 2020 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/MRG\_UWaterloo.PM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanCP20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Aliababa DAMO Academy at TREC Precision Medicine 2020: State-of-the-art  Evidence Retriever for Precision Medicine with Expert-in-the-loop  Active Learning

_Qiao Jin, Chuanqi Tan, Mosha Chen, Ming Yan, Songfang Huang, Ningyu Zhang, Xiaozhong Liu_

- :fontawesome-solid-user-group: **Participant:** [ALIBABA](./pm/participants.md#alibaba)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/ALIBABA.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/ALIBABA.PM.pdf)
- :material-file-search: **Runs:** [damoespb1](./pm/runs.md#damoespb1) | [damoespb2](./pm/runs.md#damoespb2) | [damoespcbh1](./pm/runs.md#damoespcbh1) | [damoespcbh2](./pm/runs.md#damoespcbh2) | [damoespcbh3](./pm/runs.md#damoespcbh3)

??? abstract "Abstract"
	
	This paper describes the submissions of Alibaba DAMO Academy to the TREC Precision Medicine (PM) Track in 2020, which achieve state-of-the-art performance in the evidence quality assessment. The focus of the TREC PM Track is to retrieve academic papers that report critical clinical evidence for or against a given treatment in a population specified by its disease and gene mutation. We use a two-step approach that includes: 1) a baseline retriever using query expansion with Elasticsearch (ES) and 2) an automatic or expert-in-the-loop reranker: the automatic re-ranker uses features of the ES scores, pre-trained BioBERT scores, publication type scores and citation count scores; the expert-in-the-loop re-ranker uses expert annotations, fine-tuned BioBERT as well as features used in the automatic re-ranker. For the expert-in-the-loop re-ranker, we use a novel active learning annotation strategy that is sample-efficient: at each iteration of the annotation, 1) we fine-tune the BioBERT using all expert annotations of query-document relevance; 2) we let human experts annotate the actual relevance of the most relevant unannotated query-document pairs predicted by the fine-tuned BioBERT. Our submissions outperform the median topic-wise scores in the phase 1 assessment for general relevance and achieve state-of-the-art performance in the phase 2 assessment for evidence quality. Our analyses show that evidence quality is a distinct aspect than the general relevance, and thus additional modeling of it is necessary to assist IR for Evidence-based Precision Medicine
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JinJTCYHZL20.bib) "
	```
	@inproceedings{DBLP:conf/trec/JinJTCYHZL20,
		author = {Qiao Jin and Chuanqi Tan and Mosha Chen and Ming Yan and Songfang Huang and Ningyu Zhang and Xiaozhong Liu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Aliababa {DAMO} Academy at {TREC} Precision Medicine 2020: State-of-the-art Evidence Retriever for Precision Medicine with Expert-in-the-loop Active Learning},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/ALIBABA.PM.pdf},
		timestamp = {Tue, 27 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JinJTCYHZL20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Study on Query Expansion and Rank Fusion for Precision Medicine:  The IMS Unipd at TREC 2020 Precision Medicine

_Giorgio Maria Di Nunzio, Stefano Marchesin_

- :fontawesome-solid-user-group: **Participant:** [ims_unipd](./pm/participants.md#ims_unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/ims_unipd.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/ims_unipd.PM.pdf)
- :material-file-search: **Runs:** [bm25_p10](./pm/runs.md#bm25_p10) | [rrf_p10](./pm/runs.md#rrf_p10) | [rrf_prf_p10](./pm/runs.md#rrf_prf_p10) | [rrf_prf_rprec](./pm/runs.md#rrf_prf_rprec) | [rrf_prf_infndcg](./pm/runs.md#rrf_prf_infndcg)

??? abstract "Abstract"
	
	In this report, we describe the methodology and the experimental setting of our participation as the IMS Unipd team in TREC PM 2020. The objective of this work is to evaluate a query expansion and ranking fusion approach optimized on the previous years of TREC PM. In particular, we designed a procedure to (1) perform query expansion using a pseudo relevance feedback model on the first k retrieved documents, and (2) apply rank fusion techniques to the rankings produced by the different experimental settings. The results obtained provide interesting insights in terms of the different per-topic effectiveness and will be used for further failure analyses.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Nunzio020.bib) "
	```
	@inproceedings{DBLP:conf/trec/Nunzio020,
		author = {Giorgio Maria Di Nunzio and Stefano Marchesin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Study on Query Expansion and Rank Fusion for Precision Medicine: The {IMS} Unipd at {TREC} 2020 Precision Medicine},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/ims\_unipd.PM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Nunzio020.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SIB Text Mining at TREC Precision Medicine 2020

_Emilie Pasche, Déborah Caucheteur, Luc Mottin, Anaïs Mottaz, Julien Gobeill, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BITEM](./pm/participants.md#bitem)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/BITEM.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/BITEM.PM.pdf)
- :material-file-search: **Runs:** [sibtm_run1](./pm/runs.md#sibtm_run1) | [sibtm_run2](./pm/runs.md#sibtm_run2) | [sibtm_run3](./pm/runs.md#sibtm_run3) | [sibtm_run4](./pm/runs.md#sibtm_run4) | [sibtm_run5](./pm/runs.md#sibtm_run5)

??? abstract "Abstract"
	
	TREC 2020 Precision Medicine Track aimed at developing specialized algorithms able to retrieve the best available evidence for a specific cancer treatment. A set of 40 topics representing cases (i.e. a disease, caused by a gene and treated by a drug) were provided. Two assessments were performed: an assessment of the relevance of the documents and an assessment of the ranking of documents regarding the strength of the evidence. Our system collected a set of up to 1000 documents per topic and re-ranked the documents based on several strategies: classification of documents as precision medicine-related, classification of documents as focused on the topic and attribution of a set of evidence-related scores to documents. Our baseline run achieved competitive results (rank #3 for infNDCG according to the official results): more than half of the documents retrieved in the top-10 were judged as relevant regarding the topic. All the tested strategies decreased the performances in the phase-1 assessment, while the evidence-related re-ranking improved performance in the phase-2 assessment.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PascheCMMGR20.bib) "
	```
	@inproceedings{DBLP:conf/trec/PascheCMMGR20,
		author = {Emilie Pasche and D{\'{e}}borah Caucheteur and Luc Mottin and Ana{\"{\i}}s Mottaz and Julien Gobeill and Patrick Ruch},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{SIB} Text Mining at {TREC} Precision Medicine 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/BITEM.PM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PascheCMMGR20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### H2oloo at TREC 2020: When all you got is a hammer... Deep Learning,  Health Misinformation, and Precision Medicine

_Ronak Pradeep, Xueguang Ma, Xinyu Zhang, Hang Cui, Ruizhou Xu, Rodrigo Frassetto Nogueira, Jimmy Lin_

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./pm/participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf)
- :material-file-search: **Runs:** [duoT5rct](./pm/runs.md#duot5rct) | [monoT5rct](./pm/runs.md#monot5rct) | [duoT5](./pm/runs.md#duot5) | [monoT5](./pm/runs.md#monot5) | [monoT5e1](./pm/runs.md#monot5e1)

??? abstract "Abstract"
	
	The h2oloo team from the University of Waterloo participated in the TREC 2020 Deep Learning, Health Misinformation, and Precision Medicine Tracks. Our primary goal was to validate sequence-to-sequence based retrieval techniques that we have been working on in the context of multi-stage retrieval dubbed “Expando- Mono-Duo” [6, 10] comprising a candidate document generation stage (driven by “bag of words” techniques) followed by a pointwise and then a pairwise reranking stage built around T5 [11], a powerful sequence-to-sequence transformer language model. For the Health Misinformation task, we also employ learnings from our fact verification system, VerT5erini [9]. All of our experiments employed the open-source Anserini IR toolkit [14 , 16], which is based on the popular open-source Lucene search library, for initial retrieval that feeds the T5-based rerankers. Besides being the state of the art in various other collections (e.g., Robust04 and TREC-COVID), we found our models achieved much better effectiveness compared to the BM25 baselines as well as the median scores in all three tracks, demonstrating the versatility and the zero-shot transfer capabilities of our multi-stage ranking system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PradeepMZCXNL20.bib) "
	```
	@inproceedings{DBLP:conf/trec/PradeepMZCXNL20,
		author = {Ronak Pradeep and Xueguang Ma and Xinyu Zhang and Hang Cui and Ruizhou Xu and Rodrigo Frassetto Nogueira and Jimmy Lin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {H2oloo at {TREC} 2020: When all you got is a hammer... Deep Learning, Health Misinformation, and Precision Medicine},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf},
		timestamp = {Mon, 20 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PradeepMZCXNL20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSIROmed at TREC Precision Medicine 2020

_Maciej Rybinski, Sarvnaz Karimi_

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./pm/participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/CSIROmed.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/CSIROmed.PM.pdf)
- :material-file-search: **Runs:** [CSIROmed_strDFR](./pm/runs.md#csiromed_strdfr) | [CSIROmed_rlxRR](./pm/runs.md#csiromed_rlxrr) | [CSIROmed_rRRa](./pm/runs.md#csiromed_rrra) | [CSIROmed_strRR](./pm/runs.md#csiromed_strrr) | [CSIROmed_sRRa](./pm/runs.md#csiromed_srra)

??? abstract "Abstract"
	
	TREC Precision Medicine (PM) focuses on providing high-quality evidence from the biomedical literature for clinicians treating cancer patients. Our experiments focus on incorporating treatment into search. We established a promising baseline using PM 2017-2018 datasets for training and 2019 for validation. Our baseline consisted of a base-ranking step using Divergence From Randomness (DFR) scoring that used disease and gene as queries and an aggregated text field to represent documents, followed by a BERT-based neural re-ranker. We examined two mechanisms for incorporating the treatment within the query formulation strategy for DFR: (1) a concatenation of disease, gene and treatment fields; and (2) a concatenation of disease and gene fields, but filtering out the documents where treatment terms were absent. We experimented with both strategies in combination with re-rankers trained either directly on TREC PM 2017-2019 retrieval task, or trained on a treatment-augmented version of these tasks. We obtained the best results using boolean retrieval for treatment terms with a re-ranker trained on non-augmented TREC PM datasets. Our top-ranking run achieved 0.530, 0.565, 0.436 for infNDCG, P@10, RPrec, respectively. TREC median for these metrics were 0.432, 0.465, and 0.326.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RybinskiK20.bib) "
	```
	@inproceedings{DBLP:conf/trec/RybinskiK20,
		author = {Maciej Rybinski and Sarvnaz Karimi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {CSIROmed at {TREC} Precision Medicine 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/CSIROmed.PM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RybinskiK20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieving Scientific Abstracts using Medical Concepts and Learning  to Rank: CincyMedIR at TREC 2020 Precision Medicine Track

_Piyush Sahu, Hoang Vu, Danny T. Y. Wu_

- :fontawesome-solid-user-group: **Participant:** [CincyMedIR](./pm/participants.md#cincymedir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/CincyMedIR.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/CincyMedIR.PM.pdf)
- :material-file-search: **Runs:** [CincyMedIR_28](./pm/runs.md#cincymedir_28) | [CincyMedIR28dgt](./pm/runs.md#cincymedir28dgt) | [CincyMedIR_28_t](./pm/runs.md#cincymedir_28_t) | [CincyMedIR_20](./pm/runs.md#cincymedir_20) | [CincyMedIR_dgt](./pm/runs.md#cincymedir_dgt)

??? abstract "Abstract"
	
	The CincyMedIR team led by Dr. Danny T.Y. Wu at the University of Cincinnati College of Medicine (UC CoM) participated in the Text Retrieval Conference 2020 Precision Medicine Track (TREC-PM). CincyMedIR only worked on the scientific abstracts this year with two main objectives: 1) to experiment learning to rank (LTR) models, a supervised machine-learning approach to adjust ranking based on the text features in the relevant documents, and 2) to develop a configurable pipeline for TREC-like tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SahuVW20.bib) "
	```
	@inproceedings{DBLP:conf/trec/SahuVW20,
		author = {Piyush Sahu and Hoang Vu and Danny T. Y. Wu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Retrieving Scientific Abstracts using Medical Concepts and Learning to Rank: CincyMedIR at {TREC} 2020 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/CincyMedIR.PM.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SahuVW20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Podcast 

#### TREC 2020 Podcasts Track Overview

_Rosie Jones, Ben Carterette, Ann Clifton, Jussi Karlgren, Aasish Pappu, Sravana Reddy, Yongze Yu, Maria Eskevich, Gareth J. F. Jones_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.P.pdf](https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.P.pdf)
??? abstract "Abstract"
	
	The Podcast Track is new at the Text Retrieval Conference (TREC) in 2020. The podcast track was designed to encourage research into podcasts in the information retrieval and NLP research communities. The track consisted of two shared tasks: segment retrieval and summarization, both based on a dataset of over 100,000 podcast episodes (metadata, audio, and automatic transcripts) which was released concurrently with the track. The track generated considerable interest, aracted hundreds of new registrations to TREC and fifteen teams, mostly disjoint between search and summarization, made final submissions for assessment. Deep learning was the dominant experimental approach for both search experiments and summarization. This paper gives an overview of the tasks and the results of the participants' experiments. The track will return to TREC 2021 with the same two tasks, incorporating slight modifications in response to participant feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JonesCCKPRYEJ20.bib) "
	```
	@inproceedings{DBLP:conf/trec/JonesCCKPRYEJ20,
		author = {Rosie Jones and Ben Carterette and Ann Clifton and Jussi Karlgren and Aasish Pappu and Sravana Reddy and Yongze Yu and Maria Eskevich and Gareth J. F. Jones},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2020 Podcasts Track Overview},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JonesCCKPRYEJ20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combine and Re-Rank: The University of Maryland at the TREC 2020  Podcasts Track

_Petra Galuscáková, Suraj Nair, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [UMD_IR](./podcast/participants.md#umd_ir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UMD_IR.P.pdf](https://trec.nist.gov/pubs/trec29/papers/UMD_IR.P.pdf)
- :material-file-search: **Runs:** [UMD_IR_run1](./podcast/runs.md#umd_ir_run1) | [UMD_IR_run2](./podcast/runs.md#umd_ir_run2) | [UMD_IR_run3](./podcast/runs.md#umd_ir_run3) | [UMD_ID_run4](./podcast/runs.md#umd_id_run4) | [UMD_IR_run5](./podcast/runs.md#umd_ir_run5)

??? abstract "Abstract"
	
	The University of Maryland submitted five runs to Task 1 of the TREC 2020 podcasts track. The best results, achieved by combining seven system variants and then re-ranking with using combinations of two neural models, achieved a 27% improvement in NDCG over a simple Indri baseline in the official evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaluscakovaNONO20.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaluscakovaNONO20,
		author = {Petra Galusc{\'{a}}kov{\'{a}} and Suraj Nair and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Combine and Re-Rank: The University of Maryland at the {TREC} 2020 Podcasts Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/UMD\_IR.P.pdf},
		timestamp = {Wed, 06 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GaluscakovaNONO20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LRG at TREC 2020: Document Ranking with XLNet-Based Models

_Abheesht Sharma, Harshit Pandey_

- :fontawesome-solid-user-group: **Participant:** [LRG_REtrievers](./podcast/participants.md#lrg_retrievers)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/LRG_REtrievers.P.pdf](https://trec.nist.gov/pubs/trec29/papers/LRG_REtrievers.P.pdf)
- :material-file-search: **Runs:** [LRGREtvrs-r_1](./podcast/runs.md#lrgretvrs-r_1) | [LRGREtvrs-r_2](./podcast/runs.md#lrgretvrs-r_2) | [LRGREtvrs-r_3](./podcast/runs.md#lrgretvrs-r_3) | [LRGREtvrs-r_4](./podcast/runs.md#lrgretvrs-r_4)

??? abstract "Abstract"
	
	Establishing a good information retrieval system in popular mediums of entertainment is a quickly growing area of investigation for companies and researchers alike. We delve into the domain of information retrieval for podcasts. In Spotify's Podcast Challenge, we are given a user's query with a description to find the most relevant short segment from the given dataset having all the podcasts. Previous techniques that include solely classical Information Retrieval (IR) techniques, perform poorly when descriptive queries are presented. On the other hand, models which exclusively rely on large neural networks tend to perform better. The downside to this technique is that a considerable amount of time and computing power are required to infer the result. We experiment with two hybrid models which first filter out the best podcasts based on user's query with a classical IR technique, and then perform re-ranking on the shortlisted documents based on the detailed description using a transformer-based model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SharmaP20.bib) "
	```
	@inproceedings{DBLP:conf/trec/SharmaP20,
		author = {Abheesht Sharma and Harshit Pandey},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{LRG} at {TREC} 2020: Document Ranking with XLNet-Based Models},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/LRG\_REtrievers.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SharmaP20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Automatic Summarization of Open-Domain Podcast Episodes

_Kaiqiang Song, Fei Liu, Chen Li, Xiaoyang Wang, Dong Yu_

- :fontawesome-solid-user-group: **Participant:** [UCF_NLP](./podcast/participants.md#ucf_nlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UCF_NLP.P.pdf](https://trec.nist.gov/pubs/trec29/papers/UCF_NLP.P.pdf)
- :material-file-search: **Runs:** [UCF_NLP1](./podcast/runs.md#ucf_nlp1) | [UCF_NLP2](./podcast/runs.md#ucf_nlp2)

??? abstract "Abstract"
	
	We present implementation details of our abstractive summarizers that achieve competitive results on the Podcast Summarization task of TREC 2020. A concise textual summary that captures important information is crucial for users to decide whether to listen to the podcast. Prior work focuses primarily on learning contextualized representations. Instead, we investigate several less-studied aspects of neural abstractive summarization, including (i) the importance of selecting important segments from transcripts to serve as input to the summarizer; (ii) striking a balance between the amount and quality of training instances; (iii) the appropriate summary length and start/end points. We highlight the design considerations behind our system and offer key insights into the strengths and weaknesses of neural abstractive systems. Our results suggest that identifying important segments from transcripts to use as input to an abstractive summarizer is advantageous for summarizing long documents. Our best system achieves a quality rating of 1.559 judged by NIST evaluators—an absolute increase of 0.268 (+21%) over the creator descriptions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SongLLWY20.bib) "
	```
	@inproceedings{DBLP:conf/trec/SongLLWY20,
		author = {Kaiqiang Song and Fei Liu and Chen Li and Xiaoyang Wang and Dong Yu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Automatic Summarization of Open-Domain Podcast Episodes},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/UCF\_NLP.P.pdf},
		timestamp = {Fri, 14 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SongLLWY20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Spotify at the TREC 2020 Podcasts Track: Segment Retrieval

_Yongze Yu, Jussi Karlgren, Ann Clifton, Md. Iftekhar Tanveer, Rosie Jones, Hamed R. Bonab_

- :fontawesome-solid-user-group: **Participant:** [spotify](./podcast/participants.md#spotify)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/Spotify.P.pdf](https://trec.nist.gov/pubs/trec29/papers/Spotify.P.pdf)
- :material-file-search: **Runs:** [BERT-DESC-S](./podcast/runs.md#bert-desc-s) | [BERT-DESC-Q](./podcast/runs.md#bert-desc-q) | [BERT-DESC-TD](./podcast/runs.md#bert-desc-td) | [coarse2fine](./podcast/runs.md#coarse2fine) | [categoryaware1](./podcast/runs.md#categoryaware1) | [categoryaware2](./podcast/runs.md#categoryaware2)

??? abstract "Abstract"
	
	In this notebook paper, we present the details of baselines and experimental runs of the segment retrieval task in TREC 2020 Podcasts Track. As baselines, we implemented traditional IR methods,i.e. BM25 and QL, and the neural re-ranking BERT model pre-trained on MS MARCO passage re-ranking task. We also detail experimental runs of the re-ranking model fine-tuned on additional external data sets from (1) crowd- sourcing, (2) automatically generated questions, and (3) episode title-description pairs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuKCTJB20.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuKCTJB20,
		author = {Yongze Yu and Jussi Karlgren and Ann Clifton and Md. Iftekhar Tanveer and Rosie Jones and Hamed R. Bonab},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Spotify at the {TREC} 2020 Podcasts Track: Segment Retrieval},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/Spotify.P.pdf},
		timestamp = {Sat, 11 Dec 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuKCTJB20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Two-Phase Approach for Abstractive Podcast Summarization

_Chujie Zheng, Harry Jiannan Wang, Kunpeng Zhang, Ling Fan_

- :fontawesome-solid-user-group: **Participant:** [udel_wang_zheng](./podcast/participants.md#udel_wang_zheng)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/udel_wang_zheng.P.pdf](https://trec.nist.gov/pubs/trec29/papers/udel_wang_zheng.P.pdf)
- :material-file-search: **Runs:** [udel_wang_zheng1](./podcast/runs.md#udel_wang_zheng1) | [udel_wang_zheng2](./podcast/runs.md#udel_wang_zheng2) | [udel_wang_zheng3](./podcast/runs.md#udel_wang_zheng3) | [udel_wang_zheng4](./podcast/runs.md#udel_wang_zheng4)

??? abstract "Abstract"
	
	Podcast summarization is different from summarization of other data formats, such as news, patents, and scientific papers in that podcasts are often longer, conversational, colloquial, and full of sponsorship and advertising information, which imposes great challenges for existing models. In this paper, we focus on abstractive podcast summarization and propose a two-phase approach: sentence selection and seq2seq learning. Specifically, we first select important sentences from the noisy long podcast transcripts. The selection is based on sentence similarity to the reference to reduce the redundancy and the associated latent topics to preserve semantics. Then the selected sentences are fed into a pre-trained encoder-decoder framework for the summary generation. Our approach achieves promising results regarding both ROUGE-based measures and human evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengWZF20.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengWZF20,
		author = {Chujie Zheng and Harry Jiannan Wang and Kunpeng Zhang and Ling Fan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Two-Phase Approach for Abstractive Podcast Summarization},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/udel\_wang\_zheng.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengWZF20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Abstract Podcast Summarization using BART with Longformer Attention

_Hannes Karlbom, Ann Clifton_

- :fontawesome-solid-user-group: **Participant:** [hk_uu_podcast](./podcast/participants.md#hk_uu_podcast)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/hk_uu_podcast.P.pdf](https://trec.nist.gov/pubs/trec29/papers/hk_uu_podcast.P.pdf)
- :material-file-search: **Runs:** [hk_uu_podcast1](./podcast/runs.md#hk_uu_podcast1)

??? abstract "Abstract"
	
	In this paper, we present our model submitted to the TREC (Text REtrieval Conference) summarization part of the Podcasts track 2020 edition. The goal of this task is to summarize podcast episodes using 100k open-domain podcast transcripts. The challenge lies in the long length of the transcript documents, diverse structures of the podcast format and that neither the creator descriptions nor the transcripts are a perfect gold truth of an episode. We propose a combined model that tackles the length challenge, by using a drop in replacement of the Longformer attention mechanism in a pre-trained BART model and fine-tuning the model on the podcasts dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KarlbomC20.bib) "
	```
	@inproceedings{DBLP:conf/trec/KarlbomC20,
		author = {Hannes Karlbom and Ann Clifton},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Abstract Podcast Summarization using {BART} with Longformer Attention},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/hk\_uu\_podcast.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KarlbomC20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREMA-UNH at TREC 2020

_Sumanta Kashyapi, Laura Dietz_

- :fontawesome-solid-user-group: **Participant:** [TREMA-UNH](./podcast/participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/TREMA_UNH.P.pdf](https://trec.nist.gov/pubs/trec29/papers/TREMA_UNH.P.pdf)
- :material-file-search: **Runs:** [unhtrema1](./podcast/runs.md#unhtrema1) | [unhtrema3](./podcast/runs.md#unhtrema3) | [unhtrema2](./podcast/runs.md#unhtrema2) | [unhtrema4](./podcast/runs.md#unhtrema4)

??? abstract "Abstract"
	
	This notebook describes the submissions of team TREMA-UNH to the TREC Podcasts track. We participate in the summarization task of the track. We focus on combining extractive and generative summarization technique. The extractive model is used to detect salient parts of the input text and the generative model is used to generate summaries of only the selected segments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KashyapiD20.bib) "
	```
	@inproceedings{DBLP:conf/trec/KashyapiD20,
		author = {Sumanta Kashyapi and Laura Dietz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREMA-UNH} at {TREC} 2020},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/TREMA\_UNH.P.pdf},
		timestamp = {Tue, 21 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KashyapiD20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CUED_SPEECH at TREC 2020 Podcast Summarisation Track

_Potsawee Manakul, Mark J. F. Gales_

- :fontawesome-solid-user-group: **Participant:** [cued_speechUniv](./podcast/participants.md#cued_speechuniv)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/cued_speech.P.pdf](https://trec.nist.gov/pubs/trec29/papers/cued_speech.P.pdf)
- :material-file-search: **Runs:** [cued_speechUniv1](./podcast/runs.md#cued_speechuniv1) | [cued_speechUniv2](./podcast/runs.md#cued_speechuniv2) | [cued_speechUniv3](./podcast/runs.md#cued_speechuniv3) | [cued_speechUniv4](./podcast/runs.md#cued_speechuniv4)

??? abstract "Abstract"
	
	In this paper, we describe our approach for the Podcast Summarisation challenge in TREC 2020. Given a podcast episode with its transcription, the goal is to generate a summary that captures the most important information in the content. Our approach consists of two steps: (1) Filtering redundant or less informative sentences in the transcription using the attention of a hierarchical model; (2) Applying a state-of-the-art text summarisation system (BART) fine-tuned on the Podcast data using a sequence-level reward function. Furthermore, we perform ensembles of three and nine models for our submission runs. We also fine-tune the BART model on the Podcast data as our baseline. The human evaluation by NIST shows that our best submission achieves 1.777 in the EGFB scale, while the score of creator-provided description is 1.291. Our system won the Spotify Podcast Summarisation Challenge in the TREC2020 Podcast Track in both human and automatic evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ManakulG20.bib) "
	```
	@inproceedings{DBLP:conf/trec/ManakulG20,
		author = {Potsawee Manakul and Mark J. F. Gales},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {CUED{\_}SPEECH at {TREC} 2020 Podcast Summarisation Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/cued\_speech.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ManakulG20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DCU-ADAPT at the TREC 2020 Podcasts Track

_Yasufumi Moriya, Gareth J. F. Jones_

- :fontawesome-solid-user-group: **Participant:** [DCU-ADAPT](./podcast/participants.md#dcu-adapt)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/DCU-ADAPT.P.pdf](https://trec.nist.gov/pubs/trec29/papers/DCU-ADAPT.P.pdf)
- :material-file-search: **Runs:** [run_dcu1](./podcast/runs.md#run_dcu1) | [run_dcu2](./podcast/runs.md#run_dcu2) | [run_dcu3](./podcast/runs.md#run_dcu3) | [run_dcu4](./podcast/runs.md#run_dcu4) | [run_dcu5](./podcast/runs.md#run_dcu5)

??? abstract "Abstract"
	
	We describe DCU-ADAPT's participation in the TREC 2020 Podcasts Track. We participated in the ad-hoc segment retrieval task. The goal of the task was to search for fixed-length segments from a large archive of podcasts which contain good jump-in points to relevant content for a given query topic. The challenge of retrieving relevant segments with good jump-in points at high rank is made more difficult by the presence of transcription errors in transcripts created using automatic speech recognition. We investigated three query expan- sion techniques designed overcome this issue. Our first approach was to extract nouns and named entities from the query description provided with each query and to add them to the corresponding query. Our second approach was to retrieve documents for the query using a commercial online web search en- gine and add selected words from the web documents to the query. Our final approach was to select words to expand the query using a pseudo-relevance feedback method and WordNet. Combining the above approaches for query expansion, we achieved a normalised discounted cumulative gain (nDCG) value of 0.586.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoriyaJ20.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoriyaJ20,
		author = {Yasufumi Moriya and Gareth J. F. Jones},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DCU-ADAPT} at the {TREC} 2020 Podcasts Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/DCU-ADAPT.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MoriyaJ20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Glasgow Representation and Information Learning Lab (GRILL) at TREC  2020 Podcasts Track

_Paul Owoicho, Jeff Dalton_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./podcast/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/uog_msc.P.pdf](https://trec.nist.gov/pubs/trec29/papers/uog_msc.P.pdf)
- :material-file-search: **Runs:** [2306987O_abs_run1](./podcast/runs.md#2306987o_abs_run1) | [2306987O_extabs_run2](./podcast/runs.md#2306987o_extabs_run2) | [2306987O_extabs_run3](./podcast/runs.md#2306987o_extabs_run3)

??? abstract "Abstract"
	
	In this paper, we discuss our participation in the Summarization Task of the TREC 2020 Podcasts Track. Our submission consists of summaries generated by (i) an abstractive model based on fine-tuning T5 on the Spotify Podcasts Dataset, (ii) an ensemble model where the first 15 sentences from the podcast transcript are extracted and passed as input to a fine-tuned T5 model, and (iii) another ensemble model where we use a SpanBERT and K-Means pipeline to extract the 15 most important sentences from the podcast transcript and pass them as input to a fine-tuned T5 model. Official results demonstrate that out of 179 evaluated summaries, our best performing model (ii) generated 42 good-quality summaries - on par with the average across all other submissions. This provides evidence that focusing on the first part of the podcast episode is a strong baseline for podcast summarization.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Owoicho020.bib) "
	```
	@inproceedings{DBLP:conf/trec/Owoicho020,
		author = {Paul Owoicho and Jeff Dalton},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Glasgow Representation and Information Learning Lab {(GRILL)} at {TREC} 2020 Podcasts Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/uog\_msc.P.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Owoicho020.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Spotify at TREC 2020: Genre-Aware Abstractive Podcast Summarization

_Rezvaneh Rezapour, Sravana Reddy, Ann Clifton, Rosie Jones_

- :fontawesome-solid-user-group: **Participant:** [spotify](./podcast/participants.md#spotify)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/Spotify.P2.pdf](https://trec.nist.gov/pubs/trec29/papers/Spotify.P2.pdf)
- :material-file-search: **Runs:** [BERT-DESC-S](./podcast/runs.md#bert-desc-s) | [BERT-DESC-Q](./podcast/runs.md#bert-desc-q) | [BERT-DESC-TD](./podcast/runs.md#bert-desc-td) | [coarse2fine](./podcast/runs.md#coarse2fine) | [categoryaware1](./podcast/runs.md#categoryaware1) | [categoryaware2](./podcast/runs.md#categoryaware2)

??? abstract "Abstract"
	
	This paper contains the description of our submissions to the summarization task of the Pod- cast Track in TREC (the Text REtrieval Conference) 2020. The goal of this challenge was to generate short, informative summaries that contain the key information present in a podcast episode using automatically generated transcripts of the podcast audio. Since podcasts vary with respect to their genre, topic, and granularity of information, we propose two summarization models that explicitly take genre and named entities into consideration in order to generate summaries appropriate to the style of the podcasts. Our models are abstractive, and supervised using creator-provided de- scriptions as ground truth summaries. The results of the submitted summaries show that our best model achieves an aggregate quality score of 1.58 in comparison to the creator descriptions and a baseline abstractive system which both score 1.49 (an improvement of 9%) as assessed by human evaluators
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RezapourRCJ20.bib) "
	```
	@inproceedings{DBLP:conf/trec/RezapourRCJ20,
		author = {Rezvaneh Rezapour and Sravana Reddy and Ann Clifton and Rosie Jones},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Spotify at {TREC} 2020: Genre-Aware Abstractive Podcast Summarization},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/Spotify.P2.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RezapourRCJ20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Fair Ranking 

#### MacEwan University at the TREC 2020 Fair Ranking Track

_Brian Almquist_

- :fontawesome-solid-user-group: **Participant:** [MacEwan_Biz](./fair/participants.md#macewan_biz)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/MacEwan_BIZ.FR.pdf](https://trec.nist.gov/pubs/trec29/papers/MacEwan_BIZ.FR.pdf)
- :material-file-search: **Runs:** [MacEwan-base](./fair/runs.md#macewan-base) | [MacEwan-norm](./fair/runs.md#macewan-norm)

??? abstract "Abstract"
	
	The MacEwan University School of Business submitted two runs for the TREC 2020 Fair Ranking Track. For this task, we indexed the document abstracts and the associated metadata from the provided Semantic Scholar dataset into a single Solr1 node using a standard Tokenizer chain. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Almquist20.bib) "
	```
	@inproceedings{DBLP:conf/trec/Almquist20,
		author = {Brian Almquist},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {MacEwan University at the {TREC} 2020 Fair Ranking Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/MacEwan\_BIZ.FR.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Almquist20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Washington at TREC 2020 Fairness Ranking Track

_Yunhe Feng, Daniel Saelid, Ke Li, Chirag Shah, Ruoyuan Gao_

- :fontawesome-solid-user-group: **Participant:** [InfoSeeking](./fair/participants.md#infoseeking)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/InfoSeeking.FR.pdf](https://trec.nist.gov/pubs/trec29/papers/InfoSeeking.FR.pdf)
- :material-file-search: **Runs:** [UW_bm25](./fair/runs.md#uw_bm25) | [UW_Kr_r60g20c20](./fair/runs.md#uw_kr_r60g20c20) | [UW_Kr_r25g25c50](./fair/runs.md#uw_kr_r25g25c50) | [UW_Kr_r0g100c0](./fair/runs.md#uw_kr_r0g100c0) | [UW_Kr_r0g0c100](./fair/runs.md#uw_kr_r0g0c100) | [UW_t_bm25](./fair/runs.md#uw_t_bm25) | [UW_Kt_r0g0c100](./fair/runs.md#uw_kt_r0g0c100) | [UW_Kt_r25g25c50](./fair/runs.md#uw_kt_r25g25c50) | [UW_Kt_r60g20c20](./fair/runs.md#uw_kt_r60g20c20) | [UW_Kt_r80g10c10](./fair/runs.md#uw_kt_r80g10c10)

??? abstract "Abstract"
	
	InfoSeeking Lab's FATE (Fairness Accountability Transparency Ethics) group at University of Washington participated in 2020 TREC Fairness Ranking Track. This report describes that track, assigned data and tasks, our group definitions, and our results. Our approach to bringing fairness in retrieval and re-ranking tasks with Semantic Scholar data was to extract various dimensions of author identity. These dimensions included gender and location. We developed modules for these extractions in a way that allowed us to plug them in for either of the tasks as needed. After trying different combinations of relative weights assigned to relevance, gender, and location information, we chose five runs for retrieval and five runs for re-ranking tasks. The results showed that our runs performed below par for re-ranking task, but above average for retrieval
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FengSLSG20.bib) "
	```
	@inproceedings{DBLP:conf/trec/FengSLSG20,
		author = {Yunhe Feng and Daniel Saelid and Ke Li and Chirag Shah and Ruoyuan Gao},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Washington at {TREC} 2020 Fairness Ranking Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/InfoSeeking.FR.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FengSLSG20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Balancing Exposure and Relevance in Academic Search

_Andres Ferraro, Lorenzo Porcaro, Xavier Serra_

- :fontawesome-solid-user-group: **Participant:** [MTG](./fair/participants.md#mtg)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/MTG.FR.pdf](https://trec.nist.gov/pubs/trec29/papers/MTG.FR.pdf)
- :material-file-search: **Runs:** [LM-relevance](./fair/runs.md#lm-relevance) | [Deltr-gammas](./fair/runs.md#deltr-gammas) | [LM-relev-year](./fair/runs.md#lm-relev-year) | [LM-rel-year-100](./fair/runs.md#lm-rel-year-100) | [LM-rel-groups](./fair/runs.md#lm-rel-groups)

??? abstract "Abstract"
	
	The TREC 2020 Fair Ranking Track focuses on the evaluation of retrieval systems according to how well they fairly rank academic papers. The evaluation metric considered estimates how much the ranked papers are relevant and fairly represent different groups of authors, groups unknown to the track's participants. In this paper, we present the three different solutions proposed by our team to the given problem. The first solution is built on a learning-to-rank model to predict how much the documents are relevant for a given query and modify the ranking based on this relevance and a randomization strategy. The second approach is also based on the relevance predicted by a learning-to-rank model, but it additionally selects the authors using categories defined by analyzing collaborations between authors. The third approach uses the DELTR framework, and it considers different categories of authors based on the corresponding H-class. The results show that the first approach gives the best performance, with the additional advantage that it does not require extra information about the authors.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FerraroPS20.bib) "
	```
	@inproceedings{DBLP:conf/trec/FerraroPS20,
		author = {Andres Ferraro and Lorenzo Porcaro and Xavier Serra},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Balancing Exposure and Relevance in Academic Search},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/MTG.FR.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FerraroPS20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Naver Labs Europe at TREC 2020 Fair Ranking Track

_Till Kletti_

- :fontawesome-solid-user-group: **Participant:** [NLE](./fair/participants.md#nle)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/NLE.FR.pdf](https://trec.nist.gov/pubs/trec29/papers/NLE.FR.pdf)
- :material-file-search: **Runs:** [NLE_TEXT_99_1](./fair/runs.md#nle_text_99_1) | [NLE_META_99_1](./fair/runs.md#nle_meta_99_1) | [NLE_META_9_1](./fair/runs.md#nle_meta_9_1) | [NLE_META_PKL](./fair/runs.md#nle_meta_pkl) | [NLE_TEXT_9_1](./fair/runs.md#nle_text_9_1)

??? abstract "Abstract"
	
	In our participation to the TREC 2020 Fair Ranking Track, as Naver Labs Europe, we focused on the re-ranking task and we investigated the performance of a controller as a way to minimize unfairness over time, with minimal loss of utility. We used a two-step approach, based on (1) a relevance probability estimator, and (2) a controller that aims to bring the actual exposure close to the target exposure. This paper describes the components we designed in more detail. It contains a comparison of the performance of the controller to a baseline, which consists of a Plackett-Luce sampler. It also analyses the effect of the quality of the estimated relevance probabilities (closeness to the true binary relevance values) on the controller performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Kletti20.bib) "
	```
	@inproceedings{DBLP:conf/trec/Kletti20,
		author = {Till Kletti},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Naver Labs Europe at {TREC} 2020 Fair Ranking Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/NLE.FR.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Kletti20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team at the TREC 2020 Fair Ranking  Track

_Graham McDonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./fair/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/uogTr.FR.pdf](https://trec.nist.gov/pubs/trec29/papers/uogTr.FR.pdf)
- :material-file-search: **Runs:** [UoGTrBComRel](./fair/runs.md#uogtrbcomrel) | [UoGTrBComPro](./fair/runs.md#uogtrbcompro) | [UoGTrBRel](./fair/runs.md#uogtrbrel) | [UoGTrComRel](./fair/runs.md#uogtrcomrel) | [UoGTrBComFu](./fair/runs.md#uogtrbcomfu)

??? abstract "Abstract"
	
	In our participation to the TREC 2020 Fair Ranking Track, the University of Glasgow Terrier Team investigated a new approach for organically uncovering latent communities of authors that we wish to be fair to. Our deployed approach leverages a co-embedding model to jointly model a document's attributes, such as the document's authors, and the citation link graph of the documents in a collection, within a single embedding space. This network co-embedding is then used as input to a community detection approach that automatically updates the identified communities for each instance of a repeated query. Moreover, we experiment with two different ranking strategies to provide a fair exposure to different communities, and the authors within the communities, over time. Our first ranking strategy is inspired by the concepts of coverage and novelty from search results diversification, while our second ranking strategy leverages a data fusion approach for prioritising different communities over time.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McDonaldO20.bib) "
	```
	@inproceedings{DBLP:conf/trec/McDonaldO20,
		author = {Graham McDonald and Iadh Ounis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow Terrier Team at the {TREC} 2020 Fair Ranking Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/uogTr.FR.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/McDonaldO20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Maryland at the TREC 2020 Fair Ranking Track

_Mahmoud F. Sayed, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [UMD_IR](./fair/participants.md#umd_ir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UMD_IR.FR.pdf](https://trec.nist.gov/pubs/trec29/papers/UMD_IR.FR.pdf)
- :material-file-search: **Runs:** [umd_relfair_ltr](./fair/runs.md#umd_relfair_ltr)

??? abstract "Abstract"
	
	In this paper, we describe our submission to the second Fair Ranking Track at TREC 2020. We leverage the flexibility of listwise Learning to Rank (LtR) techniques which directly optimize towards a custom evaluation measure. To do this, we developed an objective function that balances between relevance and fairness
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SayedO20.bib) "
	```
	@inproceedings{DBLP:conf/trec/SayedO20,
		author = {Mahmoud F. Sayed and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Maryland at the {TREC} 2020 Fair Ranking Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/UMD\_IR.FR.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SayedO20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

