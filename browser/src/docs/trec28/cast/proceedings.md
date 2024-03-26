# Proceedings - Conversational Assistance 2019 

#### DCU at the TREC 2019 Conversational Assistance Track

_Piyush Arora, Abhishek Kaushik, Gareth J. F. Jones_

- :fontawesome-solid-user-group: **Participant:** [ADAPT-DCU](./participants.md#adapt-dcu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ADAPT-DCU.C.pdf](https://trec.nist.gov/pubs/trec28/papers/ADAPT-DCU.C.pdf)
- :material-file-search: **Runs:** [combination](./runs.md#combination) | [rerankingorder](./runs.md#rerankingorder) | [datasetreorder](./runs.md#datasetreorder) | [topicturnsort](./runs.md#topicturnsort)

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

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/WaterlooClarke.C.pdf](https://trec.nist.gov/pubs/trec28/papers/WaterlooClarke.C.pdf)
- :material-file-search: **Runs:** [clacBase](./runs.md#clacbase) | [clacBaseRerank](./runs.md#clacbasererank) | [clacMagic](./runs.md#clacmagic) | [clacMagicRerank](./runs.md#clacmagicrerank)

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

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.C.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.C.pdf)
- :material-file-search: **Runs:** [ict_wrfml](./runs.md#ict_wrfml)

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

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UMass.C.pdf](https://trec.nist.gov/pubs/trec28/papers/UMass.C.pdf)
- :material-file-search: **Runs:** [UMASS_DMN_V1](./runs.md#umass_dmn_v1) | [UMASS_DMN_V2](./runs.md#umass_dmn_v2)

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

- :fontawesome-solid-user-group: **Participant:** [mpi-inf-d5](./participants.md#mpi-inf-d5)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/mpi-inf-d5.C.pdf](https://trec.nist.gov/pubs/trec28/papers/mpi-inf-d5.C.pdf)
- :material-file-search: **Runs:** [mpi-d5_igraph](./runs.md#mpi-d5_igraph) | [mpi-d5_intu](./runs.md#mpi-d5_intu) | [mpi-d5_union](./runs.md#mpi-d5_union) | [mpi-d5_cqw](./runs.md#mpi-d5_cqw)

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

- :fontawesome-solid-user-group: **Participant:** [RUIR](./participants.md#ruir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/RUIR.N.C.pdf](https://trec.nist.gov/pubs/trec28/papers/RUIR.N.C.pdf)
- :material-file-search: **Runs:** [BM25_BERT_FC](./runs.md#bm25_bert_fc) | [BM25_BERT_RANKF](./runs.md#bm25_bert_rankf)

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

- :fontawesome-solid-user-group: **Participant:** [CMU](./participants.md#cmu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CMU.C.pdf](https://trec.nist.gov/pubs/trec28/papers/CMU.C.pdf)
- :material-file-search: **Runs:** [coref_shift_qe](./runs.md#coref_shift_qe) | [ensemble](./runs.md#ensemble) | [coref_cshift](./runs.md#coref_cshift) | [manual_indri](./runs.md#manual_indri)

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

- :fontawesome-solid-user-group: **Participant:** [ECNU-ICA](./participants.md#ecnu-ica)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ECNU_ICA.C.pdf](https://trec.nist.gov/pubs/trec28/papers/ECNU_ICA.C.pdf)
- :material-file-search: **Runs:** [ECNUICA_BERT](./runs.md#ecnuica_bert) | [ECNUICA_ORI](./runs.md#ecnuica_ori) | [ECNUICA_MIX](./runs.md#ecnuica_mix)

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

- :fontawesome-solid-user-group: **Participant:** [mpii](./participants.md#mpii)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/mpii.C.pdf](https://trec.nist.gov/pubs/trec28/papers/mpii.C.pdf)
- :material-file-search: **Runs:** [mpi_bert](./runs.md#mpi_bert) | [mpi_base](./runs.md#mpi_base)

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

- :fontawesome-solid-user-group: **Participant:** [USI](./participants.md#usi)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/USI.C.pdf](https://trec.nist.gov/pubs/trec28/papers/USI.C.pdf)
- :material-file-search: **Runs:** [galago_rel_q](./runs.md#galago_rel_q) | [bertrr_rel_q](./runs.md#bertrr_rel_q) | [galago_rel_1st](./runs.md#galago_rel_1st) | [bertrr_rel_1st](./runs.md#bertrr_rel_1st)

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

- :fontawesome-solid-user-group: **Participant:** [VES](./participants.md#ves)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/VES.C.pdf](https://trec.nist.gov/pubs/trec28/papers/VES.C.pdf)
- :material-file-search: **Runs:** [VESBERT](./runs.md#vesbert) | [VESBERT1000](./runs.md#vesbert1000)

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

- :fontawesome-solid-user-group: **Participant:** [UvA.ILPS](./participants.md#uva.ilps)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UvA.ILPS.C.pdf](https://trec.nist.gov/pubs/trec28/papers/UvA.ILPS.C.pdf)
- :material-file-search: **Runs:** [ilps-lm-rm3-dt](./runs.md#ilps-lm-rm3-dt)

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

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/udel_fang.C.pdf](https://trec.nist.gov/pubs/trec28/papers/udel_fang.C.pdf)
- :material-file-search: **Runs:** [UDInfoC_BL](./runs.md#udinfoc_bl) | [UDInfoC_TS](./runs.md#udinfoc_ts) | [UDInfoC_TS_2](./runs.md#udinfoc_ts_2)

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

- :fontawesome-solid-user-group: **Participant:** [CFDA_CLIP](./participants.md#cfda_clip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CFDA_CLIP.C.pdf](https://trec.nist.gov/pubs/trec28/papers/CFDA_CLIP.C.pdf)
- :material-file-search: **Runs:** [CFDA_CLIP_RUN1](./runs.md#cfda_clip_run1) | [CFDA_CLIP_RUN8](./runs.md#cfda_clip_run8) | [CFDA_CLIP_RUN6](./runs.md#cfda_clip_run6) | [CFDA_CLIP_RUN7](./runs.md#cfda_clip_run7)

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

- :fontawesome-solid-user-group: **Participant:** [RUCIR](./participants.md#rucir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/RUCIR.C.pdf](https://trec.nist.gov/pubs/trec28/papers/RUCIR.C.pdf)
- :material-file-search: **Runs:** [RUCIR-run3](./runs.md#rucir-run3) | [RUCIR-run1](./runs.md#rucir-run1) | [RUCIR-run2](./runs.md#rucir-run2) | [RUCIR-run4](./runs.md#rucir-run4)

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

- :fontawesome-solid-user-group: **Participant:** [TREMA-UNH](./participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf](https://trec.nist.gov/pubs/trec28/papers/TREMA-UNH.CAR.C.DL.N.pdf)
- :material-file-search: **Runs:** [UNH-trema-ecn](./runs.md#unh-trema-ecn) | [UNH-trema-ent](./runs.md#unh-trema-ent) | [unh-trema-relco](./runs.md#unh-trema-relco)

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

