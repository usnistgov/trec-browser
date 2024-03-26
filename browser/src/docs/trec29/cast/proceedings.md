# Proceedings - Conversational Assistance 2020 

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

- :fontawesome-solid-user-group: **Participant:** [HBKU](./participants.md#hbku)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/HBKU.C.pdf](https://trec.nist.gov/pubs/trec29/papers/HBKU.C.pdf)
- :material-file-search: **Runs:** [HBKU_t5_1v2](./runs.md#hbku_t5_1v2) | [HBKU_t5_1v1](./runs.md#hbku_t5_1v1) | [HBKU_t2_1v2](./runs.md#hbku_t2_1v2) | [HBKU_t2_1v1](./runs.md#hbku_t2_1v1) | [HBKU_t2_1v2_mnl](./runs.md#hbku_t2_1v2_mnl) | [HBKU_t5_1v2_mnl](./runs.md#hbku_t5_1v2_mnl) | [HBKU_t5_1v1_mnl](./runs.md#hbku_t5_1v1_mnl) | [HBKU_t2_1v1_mnl](./runs.md#hbku_t2_1v1_mnl)

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

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/WaterlooClarke.C.pdf](https://trec.nist.gov/pubs/trec29/papers/WaterlooClarke.C.pdf)
- :material-file-search: **Runs:** [WatACBase](./runs.md#watacbase) | [WatACBaseRe](./runs.md#watacbasere) | [WatACGPT2Re](./runs.md#watacgpt2re) | [WatACReAll](./runs.md#watacreall)

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

- :fontawesome-solid-user-group: **Participant:** [ASCFDA](./participants.md#ascfda)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/ASCFDA.C.pdf](https://trec.nist.gov/pubs/trec29/papers/ASCFDA.C.pdf)
- :material-file-search: **Runs:** [ASCFDA_baseline](./runs.md#ascfda_baseline) | [ASCFDA_d2q_emb](./runs.md#ascfda_d2q_emb) | [ASCFDA_qa](./runs.md#ascfda_qa) | [ASCFDA_rm3](./runs.md#ascfda_rm3)

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

- :fontawesome-solid-user-group: **Participant:** [ielab](./participants.md#ielab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/ielab.C.pdf](https://trec.nist.gov/pubs/trec29/papers/ielab.C.pdf)
- :material-file-search: **Runs:** [ielab-bertAQ](./runs.md#ielab-bertaq) | [ielab-bm25T5QLM](./runs.md#ielab-bm25t5qlm) | [ielab-bertPRFAQ](./runs.md#ielab-bertprfaq) | [ielab-bm25AQ](./runs.md#ielab-bm25aq)

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

- :fontawesome-solid-user-group: **Participant:** [nova-search](./participants.md#nova-search)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/nova_search.C.pdf](https://trec.nist.gov/pubs/trec29/papers/nova_search.C.pdf)
- :material-file-search: **Runs:** [T5_BERT100](./runs.md#t5_bert100) | [AUTO_BERT100](./runs.md#auto_bert100) | [AUTO_T5_RRF](./runs.md#auto_t5_rrf)

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

- :fontawesome-solid-user-group: **Participant:** [DUTH](./participants.md#duth)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/DUTH.C.pdf](https://trec.nist.gov/pubs/trec29/papers/DUTH.C.pdf)
- :material-file-search: **Runs:** [duth](./runs.md#duth) | [duth_arq](./runs.md#duth_arq) | [duth_manual](./runs.md#duth_manual)

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

- :fontawesome-solid-user-group: **Participant:** [grill](./participants.md#grill)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/grill.C.pdf](https://trec.nist.gov/pubs/trec29/papers/grill.C.pdf)
- :material-file-search: **Runs:** [grill_ctxDuo](./runs.md#grill_ctxduo) | [grill_bmDuo](./runs.md#grill_bmduo) | [grill_duoBART](./runs.md#grill_duobart) | [grill_fuseDuo](./runs.md#grill_fuseduo)

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

- :fontawesome-solid-user-group: **Participant:** [USI](./participants.md#usi)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/USI.C.pdf](https://trec.nist.gov/pubs/trec29/papers/USI.C.pdf)
- :material-file-search: **Runs:** [castur_albert](./runs.md#castur_albert) | [rewrite_albert](./runs.md#rewrite_albert) | [hist_attention](./runs.md#hist_attention) | [hist_concat](./runs.md#hist_concat)

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

- :fontawesome-solid-user-group: **Participant:** [UvA.ILPS](./participants.md#uva.ilps)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UvA.ILPS.C.pdf](https://trec.nist.gov/pubs/trec29/papers/UvA.ILPS.C.pdf)
- :material-file-search: **Runs:** [quretecQR](./runs.md#quretecqr) | [baselineQR](./runs.md#baselineqr) | [humanQR](./runs.md#humanqr) | [quretecNoRerank](./runs.md#quretecnorerank)

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

- :fontawesome-solid-user-group: **Participant:** [POLYU_SOME](./participants.md#polyu_some)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/POLYU_SOME.C.pdf](https://trec.nist.gov/pubs/trec29/papers/POLYU_SOME.C.pdf)
- :material-file-search: **Runs:** [raw_polyu1](./runs.md#raw_polyu1) | [man_polyu1](./runs.md#man_polyu1)

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

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/h2oloo.C.pdf](https://trec.nist.gov/pubs/trec29/papers/h2oloo.C.pdf)
- :material-file-search: **Runs:** [h2oloo_RUN1](./runs.md#h2oloo_run1) | [h2oloo_RUN2](./runs.md#h2oloo_run2) | [h2oloo_RUN3](./runs.md#h2oloo_run3) | [h2oloo_RUN4](./runs.md#h2oloo_run4)

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

- :fontawesome-solid-user-group: **Participant:** [HPCLab-CNR](./participants.md#hpclab-cnr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/HPCLab-CNR.C.pdf](https://trec.nist.gov/pubs/trec29/papers/HPCLab-CNR.C.pdf)
- :material-file-search: **Runs:** [HPCLab-CNR-run1](./runs.md#hpclab-cnr-run1) | [HPCLab-CNR-run3](./runs.md#hpclab-cnr-run3) | [HPCLab-CNR-run2](./runs.md#hpclab-cnr-run2) | [HPCLab-CNR-run4](./runs.md#hpclab-cnr-run4)

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

- :fontawesome-solid-user-group: **Participant:** [WLU](./participants.md#wlu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/WLU.C.pdf](https://trec.nist.gov/pubs/trec29/papers/WLU.C.pdf)
- :material-file-search: **Runs:** [WLU_ManUttOnly](./runs.md#wlu_manuttonly) | [WLU_RawUttOnly](./runs.md#wlu_rawuttonly)

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

