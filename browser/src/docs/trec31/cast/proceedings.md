# Proceedings - Conversational Assistance 2022 

#### TREC CAsT 2022: Going Beyond User Ask and System Retrieve with Initiative  and Response Generation

_Paul Owoicho, Jeff Dalton, Mohammad Aliannejadi, Leif Azzopardi, Johanne R. Trippas, Svitlana Vakulenko_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Overview_cast.pdf](https://trec.nist.gov/pubs/trec31/papers/Overview_cast.pdf)
??? abstract "Abstract"
	
	The fourth year of the TREC Conversational Assistance Track (CAsT) continues to focus on evaluating Conversational Passage Ranking (ConvPR) for information seeking but with several new additions to improve the realism of the task and to improve our understanding of conversational search. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Owoicho0AATV22.bib) "
	```
	@inproceedings{DBLP:conf/trec/Owoicho0AATV22,
		author = {Paul Owoicho and Jeff Dalton and Mohammad Aliannejadi and Leif Azzopardi and Johanne R. Trippas and Svitlana Vakulenko},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC} CAsT 2022: Going Beyond User Ask and System Retrieve with Initiative and Response Generation},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Overview\_cast.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Owoicho0AATV22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CFDA & CLIP at TREC 2022 Conversational Assistance Track  (CAsT)

_Jia-Huei Ju, Sheng-Chieh Lin, Li-Young Chang, Ming-Feng Tsai, Chuan-Ju Wang_

- :fontawesome-solid-user-group: **Participant:** [CFDA_CLIP](./participants.md#cfda_clip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CFDA_CLIP.C.pdf](https://trec.nist.gov/pubs/trec31/papers/CFDA_CLIP.C.pdf)
- :material-file-search: **Runs:** [CNC_kwqlm2_cqg](./runs.md#cnc_kwqlm2_cqg) | [CNC_kwqlm_cqg](./runs.md#cnc_kwqlm_cqg) | [CNC_cqg](./runs.md#cnc_cqg) | [CNC_AS-C](./runs.md#cnc_as-c) | [CNC_AD-C](./runs.md#cnc_ad-c) | [CNC_MS-C](./runs.md#cnc_ms-c) | [CNC_MD-C](./runs.md#cnc_md-c) | [CNC_AD](./runs.md#cnc_ad) | [CNC_AS](./runs.md#cnc_as)

??? abstract "Abstract"
	
	In this notebook, we introduce a new pipeline for TREC CAsT 2022. Comparing to the common multistage pipeline for conversational search, we experimented an alternative that does not require conversational query reformulation (CQR). Specifically, our pipeline equipped with conversational dense retriever and conversational passage re-ranker. Our empirical evaluation result on TREC CAsT dataset is also reported in this paper
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JuLCTW22.bib) "
	```
	@inproceedings{DBLP:conf/trec/JuLCTW22,
		author = {Jia{-}Huei Ju and Sheng{-}Chieh Lin and Li{-}Young Chang and Ming{-}Feng Tsai and Chuan{-}Ju Wang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{CFDA} {\&} {CLIP} at {TREC} 2022 Conversational Assistance Track (CAsT)},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CFDA\_CLIP.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JuLCTW22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Context Propagation in Conversational Search Utterances Participation  of the CNR Team in CAsT 2022

_Ida Mele, Cristina Ioana Muntean, Franco Maria Nardini, Raffaele Perego, Nicola Tonellotto_

- :fontawesome-solid-user-group: **Participant:** [CNR](./participants.md#cnr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CNR.C.pdf](https://trec.nist.gov/pubs/trec31/papers/CNR.C.pdf)
- :material-file-search: **Runs:** [CNR_run1](./runs.md#cnr_run1) | [CNR_run2](./runs.md#cnr_run2) | [CNR_run3](./runs.md#cnr_run3) | [CNR_run4](./runs.md#cnr_run4)

??? abstract "Abstract"
	
	Every year, NIST organizes the Text REtrieval Conference (TREC) which gathers competitions for forecasting research on text retrieval. Since 2019, it has included a contest on conversational assistant systems, called Conversational Assistant Track (CAsT) with the purpose of helping research on conversational information systems. CAsT provides test collections for open-domain conversational seeking where the users can ask multiple questions to the system and get answers like in a multi-turn conversation. For our participation in CAsT 2022, we implemented an architecture consisting of two steps: utterance rewriting and passage retrieval. Each run is based on a different utterance rewriting technique for enriching the raw utterance with context extracted from the previous utterances and/or from the replies in the conversation. Three of our approaches are completely automatic, while another one uses the manually rewritten utterances provided by the organizers of TREC CAsT 2022.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeleMN0T22.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeleMN0T22,
		author = {Ida Mele and Cristina Ioana Muntean and Franco Maria Nardini and Raffaele Perego and Nicola Tonellotto},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Context Propagation in Conversational Search Utterances Participation of the {CNR} Team in CAsT 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CNR.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MeleMN0T22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Cambridge at TREC Cast 2022

_Adian Liusie, Mengjie Qian, Xiang Li, Mark J. F. Gales_

- :fontawesome-solid-user-group: **Participant:** [HEATWAVE](./participants.md#heatwave)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/HEATWAVE.C.pdf](https://trec.nist.gov/pubs/trec31/papers/HEATWAVE.C.pdf)
- :material-file-search: **Runs:** [monot5](./runs.md#monot5) | [duo_reranker](./runs.md#duo_reranker) | [gold](./runs.md#gold) | [combine0.5](./runs.md#combine0.5)

??? abstract "Abstract"
	
	Team heatwave (of the University of Cambridge) submitted 3 automatic runs to the TREC 2022 Conversational Assistance Track. This paper discusses our approach to the challenge of conversational informational retrieval. We first describe our four stage approach of query reformulation, BM25 retrieval, passage reranking, and response extraction. Our experiments then show that our multi-query approach, which uses the raw concatenated conversational context for BM25 and the rewritten query for reranking, shows considerable performance improvement over a single-query approach, where our best performing system achieves a NDCG@3 of 0.440 in the 2022 CAsT challenge.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiusieQLG22.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiusieQLG22,
		author = {Adian Liusie and Mengjie Qian and Xiang Li and Mark J. F. Gales},
		editor = {Ian Soboroff and Angela Ellis},
		title = {University of Cambridge at {TREC} Cast 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/HEATWAVE.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiusieQLG22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MLIA-DAC@TREC CAsT 2022: Sparse Contextualized Query Embedding

_Nam Le Hai, Thomas Gerald, Thibault Formal, Jian-Yun Nie, Benjamin Piwowarski, Laure Soulier_

- :fontawesome-solid-user-group: **Participant:** [MLIA-DAC](./participants.md#mlia-dac)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/MLIA-DAC.C.pdf](https://trec.nist.gov/pubs/trec31/papers/MLIA-DAC.C.pdf)
- :material-file-search: **Runs:** [MLIA_DAC_splade](./runs.md#mlia_dac_splade) | [splade_t5mse](./runs.md#splade_t5mse) | [splade_t5mm_ens](./runs.md#splade_t5mm_ens) | [splade_t5mm](./runs.md#splade_t5mm)

??? abstract "Abstract"
	
	We extend SPLADE, a sparse information retrieval model, as our first stage ranker for the conversational task. This end-to-end approach achieves a high recall (as measure on TREC CAsT 2021). To further increase the effectiveness of our approach, we train a T5-based re-ranker. This working note fully describes our model and the four runs submitted to TREC CAsT 2022.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HaiGFNPS22.bib) "
	```
	@inproceedings{DBLP:conf/trec/HaiGFNPS22,
		author = {Nam Le Hai and Thomas Gerald and Thibault Formal and Jian{-}Yun Nie and Benjamin Piwowarski and Laure Soulier},
		editor = {Ian Soboroff and Angela Ellis},
		title = {MLIA-DAC@TREC CAsT 2022: Sparse Contextualized Query Embedding},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/MLIA-DAC.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HaiGFNPS22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Stavanger (IAI) at the TREC 2022 Conversational  Assistance Track

_Weronika Lajewska, Nolwenn Bernard, Ivica Kostric, Ivan Sekulic, Krisztian Balog_

- :fontawesome-solid-user-group: **Participant:** [UiS](./participants.md#uis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UiS.C.pdf](https://trec.nist.gov/pubs/trec31/papers/UiS.C.pdf)
- :material-file-search: **Runs:** [uis_clearboat](./runs.md#uis_clearboat) | [uis_vagueboat](./runs.md#uis_vagueboat) | [uis_duoboat](./runs.md#uis_duoboat) | [uis_cargoboat](./runs.md#uis_cargoboat) | [uis_sparseboat](./runs.md#uis_sparseboat) | [uis_mixedboat](./runs.md#uis_mixedboat)

??? abstract "Abstract"
	
	This paper describes the participation of the IAI group at the University of Stavanger in the TREC 2022 Conversational Assistance track. We employ an established two-stage passage ranking architecture, i.e., first-pass passage retrieval (with standard BM25 ranking and pseudo-relevance feedback) followed by re-ranking (with mono and duo T5) using a rewritten query (with a T5 model fine-tuned on the CANARD dataset). In our runs, we experiment with intent classification based on MSDialog-Intent and term expansion using beam search scores for query rewriting as well as with clarifying questions for the mixed-initiative subtask.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LajewskaBKSB22.bib) "
	```
	@inproceedings{DBLP:conf/trec/LajewskaBKSB22,
		author = {Weronika Lajewska and Nolwenn Bernard and Ivica Kostric and Ivan Sekulic and Krisztian Balog},
		editor = {Ian Soboroff and Angela Ellis},
		title = {The University of Stavanger {(IAI)} at the {TREC} 2022 Conversational Assistance Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UiS.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LajewskaBKSB22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team at the TREC 2022 Conversational  Assistance Track

_Sarawoot Kongyoung, Craig Macdonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UoGTr.C.pdf](https://trec.nist.gov/pubs/trec31/papers/UoGTr.C.pdf)
- :material-file-search: **Runs:** [uogTr-MI](./runs.md#uogtr-mi) | [uogTr-MI-HB](./runs.md#uogtr-mi-hb) | [uogTr-AT](./runs.md#uogtr-at) | [uogTr-MT](./runs.md#uogtr-mt)

??? abstract "Abstract"
	
	In this paper, we describe our methods and submitted runs for the TREC 2022 Conversational Assistance Track. In our participation, we leverage Multi-Task Learning (MTL) methods to enhance the performance of the conversational search system. For the main task, we use our recently proposed monoQA model, which applies Multi-Task Learning (MTL) on reranking and answer extraction by sharing a single text generation model, predicts both the answer and the reranking score simultaneously. For the mixed-initiative sub-task, we propose T5MI, which is trained on the ClariQ dataset, to determine whether a user utterance needs to ask clarifying questions, as well as to generate useful clarifying questions. This year, we submitted three runs based on the data used in the testing step consisting of 1) uogTr-MT: using the provided manually rewritten utterances as the queries; 2) uogTr-AT: using the raw utterances and the provided provenances as the context for rewriting the queries; 3) uogTr-MI-HB: using the raw utterances and the output from the mixed-initiative sub-task as the context for rewriting the queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KongyoungMO22.bib) "
	```
	@inproceedings{DBLP:conf/trec/KongyoungMO22,
		author = {Sarawoot Kongyoung and Craig Macdonald and Iadh Ounis},
		editor = {Ian Soboroff and Angela Ellis},
		title = {University of Glasgow Terrier Team at the {TREC} 2022 Conversational Assistance Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UoGTr.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KongyoungMO22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke at the TREC 2022 Conversational Assistant Track

_Siqing Huo, Xinyi Yan, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/WaterlooClarke.C.pdf](https://trec.nist.gov/pubs/trec31/papers/WaterlooClarke.C.pdf)
- :material-file-search: **Runs:** [UWCmanual22](./runs.md#uwcmanual22) | [UWCcano22](./runs.md#uwccano22) | [UWCauto22](./runs.md#uwcauto22)

??? abstract "Abstract"
	
	The WaterlooClarke group submitted three runs to TREC Conversational Assistant Track (CAsT) 2022: UWCmanual22, UWCauto22, and UWCcano22. This report describes the techniques used and the results of these three runs. The pipeline to generate each run contains three main steps: 1) query reformulation, 2) passage retrieval and reranking, 3) passage summarization and reranking. For the UWCmanual22 run, we used the manual rewritten utterances provided as reformulated queries. For the UWCauto22 run, we used the automatic rewritten utterances provided as reformulated queries. For the UWCcano22 run, we augmented the automatic rewritten utterances provided with keywords extracted from the previous responses' titles, and used them as reformulated queries. We continued last year's strategy [6] of performing passage reranking with both MonoT5 and DuoT5 [2] on the pooled retrieved passages from both sparse and dense retrievers [1]. This year we focused on experimenting with the following changes: 1) Incorporating generative summarization techniques to make the produced answers more conversational. 2) Incorporating pseudo-relevance feedback into the passage retrieval stage to improve performance. In the next section, we will present the details of our pipeline
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuoYC22.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuoYC22,
		author = {Siqing Huo and Xinyi Yan and Charles L. A. Clarke},
		editor = {Ian Soboroff and Angela Ellis},
		title = {WaterlooClarke at the {TREC} 2022 Conversational Assistant Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/WaterlooClarke.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuoYC22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering-Based Query Expansion for Conversational Search:  IIIA@UNIPD at TREC CAsT 2022

_Guglielmo Faggioli, Nicola Ferro, Mattia Romanello_

- :fontawesome-solid-user-group: **Participant:** [iiia-unipd](./participants.md#iiia-unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/iiia-unipd.C.pdf](https://trec.nist.gov/pubs/trec31/papers/iiia-unipd.C.pdf)
- :material-file-search: **Runs:** [DEI-run1](./runs.md#dei-run1) | [DEI-run2](./runs.md#dei-run2) | [DEI-run4](./runs.md#dei-run4) | [DEI-run5.json](./runs.md#dei-run5.json)

??? abstract "Abstract"
	
	Conversational Search task is becoming ubiquitous in our daily interaction with information systems. Nevertheless, it remains an extremely complex task due to its profoundly different nature from ad-hoc retrieval, and the challenges presented by the way a user interacts with the system. CAsT TREC Track explicitly aims at fostering the development of conversational systems and the discussion of the linked challenges within the research community. In this work, we describe the approach that we propose to CAsT 2022 to tackle the conversational task. In particular, our approach is based on expanding and rewriting the utterance at hand with the response to the previous utterance, using a QA model to extract it from the first passage retrieved in response to the previous query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Faggioli0R22.bib) "
	```
	@inproceedings{DBLP:conf/trec/Faggioli0R22,
		author = {Guglielmo Faggioli and Nicola Ferro and Mattia Romanello},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Question Answering-Based Query Expansion for Conversational Search: IIIA@UNIPD at {TREC} CAsT 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/iiia-unipd.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Faggioli0R22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Exploration Study of Mixed-initiative Query Reformulation in Conversational  Passage Retrieval

_Dayu Yang, Yue Zhang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/udel_fang.C.pdf](https://trec.nist.gov/pubs/trec31/papers/udel_fang.C.pdf)
- :material-file-search: **Runs:** [mi_task_0822_1](./runs.md#mi_task_0822_1) | [udinfo_best2021](./runs.md#udinfo_best2021) | [udinfo_mi_b2021](./runs.md#udinfo_mi_b2021) | [udinfo_onlyd](./runs.md#udinfo_onlyd) | [udinfo_onlyd_mi](./runs.md#udinfo_onlyd_mi)

??? abstract "Abstract"
	
	In this paper, we report our methods and experiments for the TREC Conversational Assistance Track (CAsT) 2022. In this work, we aim to reproduce multi-stage retrieval pipelines and explore one of the potential benefits of involving mixed-initiative interaction in conversational passage retrieval scenarios: reformulating raw queries. Before the first ranking stage of a multi-stage retrieval pipeline, we propose a mixed-initiative query reformulation module, which achieves query reformulation based on the mixed-initiative interaction between the users and the system, as the replacement for the neural reformulation method. Specifically, we design an algorithm to generate appropriate questions related to the ambiguities in raw queries, and another algorithm to reformulate raw queries by parsing users' feedback and incorporating it into the raw query. For the first ranking stage of our multi-stage pipelines, we adopt a sparse ranking function: BM25, and a dense retrieval method: TCT-ColBERT. For the second-ranking step, we adopt a pointwise reranker: MonoT5, and a pairwise reranker: DuoT5. Experiments on both TREC CAsT 2021 and TREC CAsT 2022 datasets show the effectiveness of our mixed-initiative-based query reformulation method on improving retrieval performance compared with two popular reformulators: a neural reformulator: CANARD-T5 and a rule-based reformulator: historical query reformulator(HQE)
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangZF22.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangZF22,
		author = {Dayu Yang and Yue Zhang and Hui Fang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {An Exploration Study of Mixed-initiative Query Reformulation in Conversational Passage Retrieval},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/udel\_fang.C.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangZF22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

