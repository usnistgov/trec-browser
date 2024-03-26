# Proceedings - News 2021 

#### IRCologne at TREC 2021 News Track Relation-based re-ranking for  background linking

_Björn Engelmann, Philipp Schaer_

- :fontawesome-solid-user-group: **Participant:** [IR-Cologne](./participants.md#ir-cologne)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IR-Cologne-N.pdf](https://trec.nist.gov/pubs/trec30/papers/IR-Cologne-N.pdf)
- :material-file-search: **Runs:** [base](./runs.md#base) | [rel00_ent07](./runs.md#rel00_ent07) | [rel02_ent05](./runs.md#rel02_ent05) | [rel05_ent02](./runs.md#rel05_ent02) | [rel07_ent00](./runs.md#rel07_ent00) | [bm25_sub_0.25](./runs.md#bm25_sub_0.25) | [bm25_sub_0.5](./runs.md#bm25_sub_0.5) | [bm25_sub_1.0](./runs.md#bm25_sub_1.0) | [bm25_sub_2](./runs.md#bm25_sub_2) | [bm25_sub_4](./runs.md#bm25_sub_4)

??? abstract "Abstract"
	
	This paper presents our approach to the background linking task of the TREC 2021 News Track. The background linking task is to find a set of relevant articles in the Washington Post dataset containing helpful background information for a given news article. Our approach involved a two-stage retrieval process. In the first stage, the 200 most relevant documents were extracted from the entire corpus using BM25. The second stage involved re-ranking using similarity scores based on entities and relations extracted from the query document and the associated 200 relevant documents. For this task, we submitted five runs, each giving different weights to the entities and relations. Our best run received a nDCG@5 of 0.4423, and we were thus able to show that re-ranking with the use of relations leads to a slight improvement over the baseline without re-ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0002S21.bib) "
	```
	@inproceedings{DBLP:conf/trec/0002S21,
		author = {Bj{\"{o}}rn Engelmann and Philipp Schaer},
		editor = {Ian Soboroff and Angela Ellis},
		title = {IRCologne at {TREC} 2021 News Track Relation-based re-ranking for background linking},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IR-Cologne-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0002S21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Elastic Embedded Background Linking for News Articles with Keywords,  Entities and Events

_Luis Adrián Cabrera-Diego, Emanuela Boros, Antoine Doucet_

- :fontawesome-solid-user-group: **Participant:** [L3i_Rochelle](./participants.md#l3i_rochelle)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/L3i_Rochelle-N.pdf](https://trec.nist.gov/pubs/trec30/papers/L3i_Rochelle-N.pdf)
- :material-file-search: **Runs:** [300K_ENT_PH](./runs.md#300k_ent_ph) | [300K_ENT_PH_DN](./runs.md#300k_ent_ph_dn) | [KWVec](./runs.md#kwvec) | [KWVec_sub](./runs.md#kwvec_sub) | [Lambda](./runs.md#lambda) | [Lambda_narr](./runs.md#lambda_narr) | [Lambda_sub](./runs.md#lambda_sub) | [S300K_PH_DN](./runs.md#s300k_ph_dn) | [S300K_ENT_PH_DN](./runs.md#s300k_ent_ph_dn) | [S300K_ENT_P_DN2](./runs.md#s300k_ent_p_dn2)

??? abstract "Abstract"
	
	In this paper, we present a collection of five flexible background linking models created for the News Track in TREC 2021 that generate ranked lists of articles to provide contextual information. The collection is based on the use of sentence embeddings indexes, created with Sentence BERT and Open Distro for ElasticSearch. For each model, we explore additional tools, from keywords extraction using YAKE, to entity and event detection, while passing through a linear combination. The associated code is available online as open-source software.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Cabrera-DiegoBD21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Cabrera-DiegoBD21,
		author = {Luis Adri{\'{a}}n Cabrera{-}Diego and Emanuela Boros and Antoine Doucet},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Elastic Embedded Background Linking for News Articles with Keywords, Entities and Events},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/L3i\_Rochelle-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Cabrera-DiegoBD21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### bigIR at TREC 2021: Adopting Transfer Learning for News Background  Linking

_Marwa Essam, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./participants.md#qu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/QU-N.pdf](https://trec.nist.gov/pubs/trec30/papers/QU-N.pdf)
- :material-file-search: **Runs:** [QU_SP_MBERT](./runs.md#qu_sp_mbert) | [QU_SP_MSM](./runs.md#qu_sp_msm) | [QU_SS_MSM](./runs.md#qu_ss_msm) | [QU_LeadPar](./runs.md#qu_leadpar) | [QU_YakeTruss](./runs.md#qu_yaketruss)

??? abstract "Abstract"
	
	In this paper, we present the participation of the bigIR team at Qatar University in the TREC 2021 news track. We participated in the background linking task. The task mainly aims to retrieve news articles that provide context and background knowledge to the reader of a specific query article. We submitted five runs for this task. In the first two, we adopted an ad-hoc retrieval approach, where the query articles were analyzed to generate search queries that were issued against the news articles collection to retrieve the required links. In the remaining runs, we adopted a transfer learning approach to rerank the articles retrieved given their usefulness to address specific subtopics related to the query articles. These subtopics were given by the track organizers as a new challenge this year. The results show that one of our runs outperformed TREC median submission, while others achieved comparable results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EssamE21.bib) "
	```
	@inproceedings{DBLP:conf/trec/EssamE21,
		author = {Marwa Essam and Tamer Elsayed},
		editor = {Ian Soboroff and Angela Ellis},
		title = {bigIR at {TREC} 2021: Adopting Transfer Learning for News Background Linking},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/QU-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/EssamE21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SU-NLP at TREC NEWS 2021

_Kenan Fayoumi, Reyyan Yeniterzi_

- :fontawesome-solid-user-group: **Participant:** [SU-NLP](./participants.md#su-nlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/SU-NLP-N.pdf](https://trec.nist.gov/pubs/trec30/papers/SU-NLP-N.pdf)
- :material-file-search: **Runs:** [SU_BiEnc](./runs.md#su_bienc) | [SU_BiEnc_CrsEnc](./runs.md#su_bienc_crsenc) | [SU_ES_CrsEnc](./runs.md#su_es_crsenc) | [SU_ES](./runs.md#su_es) | [SU_ES_CrsEnc_NF](./runs.md#su_es_crsenc_nf)

??? abstract "Abstract"
	
	This paper presents our work and submissions for the TREC 2021 News Track Wikification task. We approach the problem as an entity linking task initially and after identifying the mentions and their corresponding Wikipedia entities, we rank the mentions within the news article based on their usefulness. For the entity linking part, transformer-based architectures are explored for both detecting the mentions, generating the possible candidates and re-ranking them. Finally for the mention ranking, we use previous years' best performing approach which uses the position of the mention within the text
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FayoumiY21.bib) "
	```
	@inproceedings{DBLP:conf/trec/FayoumiY21,
		author = {Kenan Fayoumi and Reyyan Yeniterzi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{SU-NLP} at {TREC} {NEWS} 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/SU-NLP-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FayoumiY21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Middlebury at TREC News '21 Exploring Learning to Rank Model Variants

_Culton Koster, John Foley_

- :fontawesome-solid-user-group: **Participant:** [middlebury](./participants.md#middlebury)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/middlebury-N.pdf](https://trec.nist.gov/pubs/trec30/papers/middlebury-N.pdf)
- :material-file-search: **Runs:** [midd-rf](./runs.md#midd-rf) | [midd-direct](./runs.md#midd-direct) | [midd-twostage](./runs.md#midd-twostage) | [midd-transfer](./runs.md#midd-transfer)

??? abstract "Abstract"
	
	Middlebury College participated in the TREC News Background Linking task in 2021. We constructed a linear learning to rank model trained on the 2018-2020 data and submitted runs that included variants on the standard low resource learning-to-rank models. In this notebook paper we detail the contents of our submissions and our lessons learned from this year's participation. We explored a few variant models including a random forest ranker, linear models trained on that random forest, and two-stage linear models, but found that traditional, direct ranking still appears to be optimal.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KosterF21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KosterF21,
		author = {Culton Koster and John Foley},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Middlebury at {TREC} News '21 Exploring Learning to Rank Model Variants},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/middlebury-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KosterF21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Semantic Search for Background Linking in News Articles

_Udhav Sethi, Anup Anand Deshmukh_

- :fontawesome-solid-user-group: **Participant:** [Waterloo_Cormack](./participants.md#waterloo_cormack)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Waterloo_Cormack-N.pdf](https://trec.nist.gov/pubs/trec30/papers/Waterloo_Cormack-N.pdf)
- :material-file-search: **Runs:** [UW_UDHAVSETHI](./runs.md#uw_udhavsethi) | [UW_UDHAVSETHI_S](./runs.md#uw_udhavsethi_s) | [UW_UDHAV_S100](./runs.md#uw_udhav_s100)

??? abstract "Abstract"
	
	The task of background linking aims at recommending news articles to a reader that are most relevant for providing context and background for the query article. For this task, we propose a two-stage approach, IR-BERT, which combines the retrieval power of BM25 with the contextual understanding gained through a BERT-based model. We further propose the use of a diversity measure to evaluate the effectiveness of background linking approaches in retrieving a diverse set of documents. We provide a comparison of IR-BERT with other participating approaches at TREC 2021. We have open sourced our implementation on Github.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SethiD21.bib) "
	```
	@inproceedings{DBLP:conf/trec/SethiD21,
		author = {Udhav Sethi and Anup Anand Deshmukh},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Semantic Search for Background Linking in News Articles},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Waterloo\_Cormack-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SethiD21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Hagen @ TREC2021 News Track

_Stefan Wagenpfeil, Matthias L. Hemmje, Paul Mc Kevitt_

- :fontawesome-solid-user-group: **Participant:** [FUH](./participants.md#fuh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/FUH-N.pdf](https://trec.nist.gov/pubs/trec30/papers/FUH-N.pdf)
- :material-file-search: **Runs:** [FUH_News_BG](./runs.md#fuh_news_bg) | [FUH_News_ST](./runs.md#fuh_news_st)

??? abstract "Abstract"
	
	This paper discusses University of Hagen's approach for the TREC2021 News Track. The News Track aims at providing relevant background links to documents of the Washington Post article archive. Our submitted run is based on research and development in the field of multimedia information retrieval and employs a modified TFIDF (Text Frequency vs. Inverse Document Frequency) algorithm for topic modeling and matrix based indexing operations founded on Graph Codes for the calculation of similarity, relevance, and recommendations. This run was submitted as FUH (Fernuniversit¨at Hagen) and obtained a nDCG@5 of 0.2655.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WagenpfeilHK21.bib) "
	```
	@inproceedings{DBLP:conf/trec/WagenpfeilHK21,
		author = {Stefan Wagenpfeil and Matthias L. Hemmje and Paul Mc Kevitt},
		editor = {Ian Soboroff and Angela Ellis},
		title = {University of Hagen @ {TREC2021} News Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/FUH-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WagenpfeilHK21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TKB48 at TREC 2021 News Track

_Lirong Zhang, Hideo Joho, Sumio Fujita_

- :fontawesome-solid-user-group: **Participant:** [TKB48](./participants.md#tkb48)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/TKB48-N.pdf](https://trec.nist.gov/pubs/trec30/papers/TKB48-N.pdf)
- :material-file-search: **Runs:** [TKB48_Run1_DTQ](./runs.md#tkb48_run1_dtq) | [TKB48_Run3_skw](./runs.md#tkb48_run3_skw) | [TKB48_Run4_tlkw](./runs.md#tkb48_run4_tlkw) | [TKB48_Run2_Tep](./runs.md#tkb48_run2_tep) | [TKB48_SRun1_DS](./runs.md#tkb48_srun1_ds) | [TKB48_SRun2_Tep](./runs.md#tkb48_srun2_tep) | [TKB48_SRun3_DTQ](./runs.md#tkb48_srun3_dtq) | [TKB48_SRun4_ST](./runs.md#tkb48_srun4_st)

??? abstract "Abstract"
	
	TKB48 incorporated document expansion methods such as docT5query and keyword extraction into indexing to solve the background linking problem. Using a transformer-based model, we calculated the text similarity of queries and documents at a semantic level and combined the semantic similarity and BM25 score for re-ranking background articles. We examined different combinations of re-ranking factors such as semantic similarities between expanded documents and attributes of topics. We found that increasing index fields produced by the docT5query model and keyword extraction model was beneficial. At the same time, the re-ranking performance was influenced by the amount of semantic similarity factors and their weight in the total relevance score. To discover the effectiveness of document expansion and our method using temporal recency, we further generated several unofficial runs incorporating a temporal topic classifier and learning to rank method. However, the lack of temporal topics limits the performance of the model. Our purposed algorithm outperformed the learning to rank method. Our future work will focus on fine-tuning of the docT5query model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangJF21.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangJF21,
		author = {Lirong Zhang and Hideo Joho and Sumio Fujita},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TKB48} at {TREC} 2021 News Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/TKB48-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangJF21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

