# Proceedings - Conversational Assistance 2021 

#### TREC CAsT 2021: The Conversational Assistance Track Overview

_Jeffrey Dalton, Chenyan Xiong, Jamie Callan_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Overview-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/Overview-CAsT.pdf)
??? abstract "Abstract"
	
	CAsT 2021 is the third year of the Conversational Assistance Track. The techniques for conversational search continue to evolve as the task becomes more challenging. Proven neural query rewriting and ranking approaches based on pre-trained language models continue to improve with new large-scale datasets. As there is increased dependence on long result history, models that discriminatively select relevant parts of the conversation history are increasingly important. The traditional NLP approaches continue to be used, but generative approaches based on large-scale pre-trained language models are most widely used. One important development this year is the use of dense retrieval approaches. The results show that these models are complementary to traditional search approaches and appear to improve recall, but still usually require a multi-pass neural re-ranking model to be most effective. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001XC21.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001XC21,
		author = {Jeffrey Dalton and Chenyan Xiong and Jamie Callan},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC} CAsT 2021: The Conversational Assistance Track Overview},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Overview-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001XC21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MLIA-LIP6@TREC-CAST2021: Feature augmentation for query recontextualization  and passage ranking

_Nawel Astaouti, Thomas Gerald, Maya Touzari, Laure Soulier, Jian-Yun Nie_

- :fontawesome-solid-user-group: **Participant:** [MLIA-LIP6](./participants.md#mlia-lip6)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/MLIA-LIP6-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/MLIA-LIP6-CAsT.pdf)
- :material-file-search: **Runs:** [t5colbert](./runs.md#t5colbert) | [Rewritt5_monot5](./runs.md#rewritt5_monot5) | [t5_monot5](./runs.md#t5_monot5) | [t5_doc2query](./runs.md#t5_doc2query)

??? abstract "Abstract"
	
	In this work, we investigate approaches for query recontextualization in the context of conversational search. We use a pipeline setting in which we first reformulate the query and then rank passages according to a backbone model. Our main focus is put on the feature inputs of a T5 query reformulation model and we evaluate different evidence sources such as the history (previous questions and answers) as well as semantic proxy through the doc2query model. We also experiment an end-to-end version of the setting which unfortunately has not been much optimized due to time constraints.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AstaoutiGTSN21.bib) "
	```
	@inproceedings{DBLP:conf/trec/AstaoutiGTSN21,
		author = {Nawel Astaouti and Thomas Gerald and Maya Touzari and Laure Soulier and Jian{-}Yun Nie},
		editor = {Ian Soboroff and Angela Ellis},
		title = {MLIA-LIP6@TREC-CAST2021: Feature augmentation for query recontextualization and passage ranking},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/MLIA-LIP6-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AstaoutiGTSN21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IITD-DBAI: Multi-Stage Retrieval with Pseudo-Relevance Feedback  and Query Reformulation

_Shivani Choudhary_

- :fontawesome-solid-user-group: **Participant:** [IITD-DBAI](./participants.md#iitd-dbai)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IITD-DBAI-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/IITD-DBAI-CAsT.pdf)
- :material-file-search: **Runs:** [IITD-RAW_U_T5_1](./runs.md#iitd-raw_u_t5_1) | [IITD-RAW_U_T5_2](./runs.md#iitd-raw_u_t5_2)

??? abstract "Abstract"
	
	Conversational systems have acquired the center stage in NLP research. Compared to the conventional information retrieval task where we have to extract the passage or document from a vast collection of documents, the Conversational system requires extracting related information to respond to a series of questions. The turns in the conversation may follow the previous question. Complexity in this task arises due to the way we form the queries, which often have a reference to previous information using pronouns, co-reference. The presence of pronouns and unresolved co-references induces ambiguity in the query. Resolving the contextual dependency is one of the most challenging tasks in the Conversational system. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Choudhary21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Choudhary21,
		author = {Shivani Choudhary},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{IITD-DBAI:} Multi-Stage Retrieval with Pseudo-Relevance Feedback and Query Reformulation},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IITD-DBAI-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Choudhary21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TKB48 at TREC 2021 Conversational Assistance Track

_Yubo Fang, Hideo Joho, Sumio Fujita_

- :fontawesome-solid-user-group: **Participant:** [TKB48](./participants.md#tkb48)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/TKB48_CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/TKB48_CAsT.pdf)
- :material-file-search: **Runs:** [dense_manual](./runs.md#dense_manual) | [sparse_manual](./runs.md#sparse_manual) | [hybrid_manual](./runs.md#hybrid_manual) | [bm25_automatic](./runs.md#bm25_automatic)

??? abstract "Abstract"
	
	In this paper, we present TKB48's methods and submitted runs for the TREC Conversational Assistance Track of Y3. We incorporated dense retrieval methods into the conversational task. We leveraged a Dual-encoder structure[ 2] to encode the user's utterance together with the conversation context and each document of the corpus into dense vector representation. After embedding we computed their relevance score by the dot product of the dense vectors. Our four submitted runs show an competitive performance compared to a sparse retrieval model. In addition to the submitted runs, we further conducted experiments and created two unofficial runs, which followed ConvDR's [29 ] strategy and trained the conversational dense retrieval model and performed inference on CAsT21 dataset. The results of these two unofficial runs show an effective use of multiple loss functions for conversational search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FangJF21.bib) "
	```
	@inproceedings{DBLP:conf/trec/FangJF21,
		author = {Yubo Fang and Hideo Joho and Sumio Fujita},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TKB48} at {TREC} 2021 Conversational Assistance Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/TKB48\_CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FangJF21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Rewriting with Expansion and Multi-Turn Entity Graphs for Answer  Selection

_Nour Jedidi, Gustavo Gonçalves, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU-LTI](./participants.md#cmu-lti)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CMU-LTI-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/CMU-LTI-CAsT.pdf)
- :material-file-search: **Runs:** [LTI-rewriter-tc](./runs.md#lti-rewriter-tc) | [LTI-rewriter-5q](./runs.md#lti-rewriter-5q) | [LTI-entity-g](./runs.md#lti-entity-g) | [LTI-rewriter-g](./runs.md#lti-rewriter-g)

??? abstract "Abstract"
	
	Conversational search is challenging in part because often the meaning of the current question cannot be fully understood without contextual information from previous questions and/or answers. This paper describes research on using query reformulation and lightweight reranking based on a multi-turn entity graph to represent and make use of contextual information in the CAsT 2021 track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JedidiGC21.bib) "
	```
	@inproceedings{DBLP:conf/trec/JedidiGC21,
		author = {Nour Jedidi and Gustavo Gon{\c{c}}alves and Jamie Callan},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Query Rewriting with Expansion and Multi-Turn Entity Graphs for Answer Selection},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CMU-LTI-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JedidiGC21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Radboud University at TREC CAsT 2021

_Hideaki Joko, Emma J. Gerritse, Faegheh Hasibi, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [RUIR](./participants.md#ruir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/RUIR-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/RUIR-CAsT.pdf)
- :material-file-search: **Runs:** [RUIR1_TURN-FT](./runs.md#ruir1_turn-ft) | [RUIR2_TURN](./runs.md#ruir2_turn) | [RUIR4_HIST](./runs.md#ruir4_hist)

??? abstract "Abstract"
	
	This paper describes Radboud University's participation in the TREC Conversational Assistance Track (CAsT) 2021 for the manually rewritten utterances. We propose an entity-enriched BERT-based re- trieval model, where entity information is injected into the BERT model, and compare it to the regular BERT-based retrieval model. We annotate the manually resolved user utterances with named entities using an entity linker, and inject both text and entity representations into our entity-enriched BERT-based retrieval model. We present our experimental setup, results, and analysis of helped and hurt queries when using entity information.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JokoGHV21.bib) "
	```
	@inproceedings{DBLP:conf/trec/JokoGHV21,
		author = {Hideaki Joko and Emma J. Gerritse and Faegheh Hasibi and Arjen P. de Vries},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Radboud University at {TREC} CAsT 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/RUIR-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JokoGHV21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Exploration Study of Multi-stage Conversational Passage Retrieval:  Paraphrase Query Expansion and Multi-view Point-wise Ranking

_Jia-Huei Ju, Chih-Ting Yeh, Cheng-Wei Lin, Chia-Ying Tsao, Jun-En Ding, Chuan-Ju Wang, Ming-Feng Tsai_

- :fontawesome-solid-user-group: **Participant:** [CFDA_CLIP](./participants.md#cfda_clip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CFDA_CLIP-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/CFDA_CLIP-CAsT.pdf)
- :material-file-search: **Runs:** [CFDA_CLIP_MRUN1](./runs.md#cfda_clip_mrun1) | [CFDA_CLIP_MRUN2](./runs.md#cfda_clip_mrun2) | [CFDA_CLIP_ARUN1](./runs.md#cfda_clip_arun1) | [CFDA_CLIP_ARUN2](./runs.md#cfda_clip_arun2)

??? abstract "Abstract"
	
	In this paper, we report our methods and experiments for the TREC Conversational Assistance Track (CAsT) 2021. In this work, We aim to improve the conversational information seeking system by reforming the modules in the existing multi-stage conversational search pipeline. In the first-stage document retrieval, we proposed the Paraphrase Query Expansion (PQE), which is adapted to the less-training-data scenario like CAsT. As for the second-stage re-ranking, we adopt the T5 point-wise ranking model with multi-view learning framework (monoT5M) to avoid the underlying overfitting problems. To further elucidate the effectiveness of our proposed methods, we also report the ablation studies of our proposed modules.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JuYLTDWT21.bib) "
	```
	@inproceedings{DBLP:conf/trec/JuYLTDWT21,
		author = {Jia{-}Huei Ju and Chih{-}Ting Yeh and Cheng{-}Wei Lin and Chia{-}Ying Tsao and Jun{-}En Ding and Chuan{-}Ju Wang and Ming{-}Feng Tsai},
		editor = {Ian Soboroff and Angela Ellis},
		title = {An Exploration Study of Multi-stage Conversational Passage Retrieval: Paraphrase Query Expansion and Multi-view Point-wise Ranking},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CFDA\_CLIP-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JuYLTDWT21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Stavanger (IAI) at the TREC 2021 Conversational  Assistance Track

_Ivica Kostric, Krisztian Balog, Magnus Book, Trond Linjordet, Vinay Setty_

- :fontawesome-solid-user-group: **Participant:** [UiS](./participants.md#uis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UiS-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/UiS-CAsT.pdf)
- :material-file-search: **Runs:** [UiS_raft](./runs.md#uis_raft)

??? abstract "Abstract"
	
	This paper describes the participation of the IAI group at the University of Stavanger in the TREC 2021 Conversational Assistance track. The focus of our submission was to produce a strong baseline on top of which future research can be conducted. We followed the already established two-step passage ranking architecture, i.e., first-pass passage retrieval followed by re-ranking. In the first step, standard BM25 ranking is used. For the second step, we used a T5 model pre-trained on the MS MARCO QA dataset. Initial results suggest that our submission constitutes a reasonable and competitive baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KostricBBLS21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KostricBBLS21,
		author = {Ivica Kostric and Krisztian Balog and Magnus Book and Trond Linjordet and Vinay Setty},
		editor = {Ian Soboroff and Angela Ellis},
		title = {The University of Stavanger {(IAI)} at the {TREC} 2021 Conversational Assistance Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UiS-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KostricBBLS21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRLab-Amsterdam at TREC 2021 Conversational Assistant Track

_Antonios Minas Krasakis, Evangelos Kanoulas_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IRlab-Amsterdam-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/IRlab-Amsterdam-CAsT.pdf)
- :material-file-search: **Runs:** [astypalaia256](./runs.md#astypalaia256) | [historyonly](./runs.md#historyonly) | [historyonlyKILT](./runs.md#historyonlykilt)

??? abstract "Abstract"
	
	This paper describes our participation (IRLab-Amsterdam) in TREC CAsT 2021. Our approach adapts a pre-trained token-level dense retriever (ColBERT) to perform zero-shot conversational search. Specifically, our query encoder reads the entire conversation history to contextualize the embeddings of the last user utterance/query, while the token-level matching function uses the contextualized embeddings to retrieve directly from the collection. The advantages of our method are two-fold: (a) it does not need any conversational data for training (ie. query resolutions, or conversational relevance judgements) and (b) it avoids complex pipeline systems based on rewriting that can affect performance (response latency) and robustness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KrasakisK21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KrasakisK21,
		author = {Antonios Minas Krasakis and Evangelos Kanoulas},
		editor = {Ian Soboroff and Angela Ellis},
		title = {IRLab-Amsterdam at {TREC} 2021 Conversational Assistant Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IRlab-Amsterdam-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KrasakisK21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding Context through Utterance Dependencies in Search Conversations  - Participation of the CNR Team in CAsT 2021

_Ida Mele, Cristina Ioana Muntean, Franco Maria Nardini, Raffaele Perego, Nicola Tonellotto_

- :fontawesome-solid-user-group: **Participant:** [CNR](./participants.md#cnr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CNR-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/CNR-CAsT.pdf)
- :material-file-search: **Runs:** [CNR-run1](./runs.md#cnr-run1) | [CNR-run2](./runs.md#cnr-run2) | [CNR-run4](./runs.md#cnr-run4) | [CNR-run3](./runs.md#cnr-run3)

??? abstract "Abstract"
	
	To help research on Conversational Information Seeking, TREC has organized a competition on conversational assistant systems, called Conversational Assistant Track (CAsT). It provides test collections for open-domain conversational search systems. For our participation in CAsT 2021, we implemented a three-step architecture consisting of: (i) automatic utterance rewriting, (ii) first-stage retrieval of candidate passages, and (iii) neural re-ranking of candidate passages. Each run is based on a different utterance rewriting technique for enriching the raw utterance with context extracted from the previous utterances and/or replies in the conversation. Two of our approaches use only raw utterances and other two use utterances plus the canonical responses of the automatically rewritten utterances provided by CAsT 2021. Our approaches also rely on utterances manually classified by human assessors using a taxonomy defined ad hoc for this task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeleMN0T21.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeleMN0T21,
		author = {Ida Mele and Cristina Ioana Muntean and Franco Maria Nardini and Raffaele Perego and Nicola Tonellotto},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Finding Context through Utterance Dependencies in Search Conversations - Participation of the {CNR} Team in CAsT 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CNR-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MeleMN0T21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Full-Collection Search with Passage and Document Evidence: Maryland  at the TREC 2021 Conversational Assistance Track

_Xin Qian, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [UMD](./participants.md#umd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UMD-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/UMD-CAsT.pdf)
- :material-file-search: **Runs:** [umd2021_run1](./runs.md#umd2021_run1) | [umd2021_run2doc](./runs.md#umd2021_run2doc) | [umd2021_run3rrf](./runs.md#umd2021_run3rrf) | [umd2021_run4den](./runs.md#umd2021_run4den)

??? abstract "Abstract"
	
	The University of Maryland (UMD) team submitted four runs to the automatic canonical condition of the track, exploring three ideas: (1) indexing both document-scale and passage-scale features, (2) using sharding to scale dense retrieval to large collections, and (3) combining results from sparse and dense methods using re-ranking and result fusion. Compared with the three-stage baseline pipeline of query rewriting using T5-base, document retrieval using BM25, and passage re-ranking using monoT5, UMD Run #1 modifies the second stage to retrieve passages rather than documents. UMD Run #2 retrieves documents in the second stage, but augments each second-stage document with additional document-scale evidence. UMD Run #3, our best run, fuses the final output of three runs: UMD Run #1, UMD Run #2, and the organizer-provided baseline. UMD Run #4, fuses results from TCT-ColBERT (a distilled ColBERT model) passage retrieval with results from BM25 document retrieval as the second stage. The TCT-ColBERT passage retrieval uses sharding to accommodate the large collection size. In each case, the first stage is the organizer-provided baseline query rewriter, and the third stage is a re-implementation of the baseline's third stage, but using monoBERT-large.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QianO21.bib) "
	```
	@inproceedings{DBLP:conf/trec/QianO21,
		author = {Xin Qian and Douglas W. Oard},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Full-Collection Search with Passage and Document Evidence: Maryland at the {TREC} 2021 Conversational Assistance Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UMD-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/QianO21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke at the TREC 2021 Conversational Assistant Track

_Xinyi Yan, Charles L. A. Clarke, Negar Arabzadeh_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/WaterlooClarke-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/WaterlooClarke-CAsT.pdf)
- :material-file-search: **Runs:** [clarke-manual](./runs.md#clarke-manual) | [clarke-cc](./runs.md#clarke-cc) | [clarke-auto](./runs.md#clarke-auto)

??? abstract "Abstract"
	
	For TREC 2021, the WaterlooClarke group submitted three runs to TREC Conversational Assistance Track (CAsT): clarke-auto, clarke-cc, and clarke-manual. The three runs were based on raw utterances, canonical response, and manually rewritten utterances respectively. This report describes the generation and the results of each of these runs. The overall approach consists of three steps: 1) query reformulation, 2) passage retrieval, and 3) passage reranking. We did not apply the query reformulation step for the clarke-manual run as manually rewritten utterances were used. In order to improve our performance, this year we focused our effort on maximizing the total system recall at the first stage by employing both dense and sparse retrievers. Research has shown that sparse retrievers and dense retrievers can retrieve complementary information [3]. We merged the retrieved passages into a single pool, then reranked this pool using a two-stage reranking pipeline with monoT5 and duoT5 [4]. In the next section, we will explain the details of our methodology.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YanCA21.bib) "
	```
	@inproceedings{DBLP:conf/trec/YanCA21,
		author = {Xinyi Yan and Charles L. A. Clarke and Negar Arabzadeh},
		editor = {Ian Soboroff and Angela Ellis},
		title = {WaterlooClarke at the {TREC} 2021 Conversational Assistant Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/WaterlooClarke-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YanCA21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

