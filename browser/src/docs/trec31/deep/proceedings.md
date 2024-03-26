# Proceedings - Deep Learning 2022 

#### Overview of the TREC 2022 Deep Learning Track

_Nick Craswell, Bhaskar Mitra, Emine Yilmaz, Daniel Campos, Jimmy Lin, Ellen M. Voorhees, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Overview_deep.pdf](https://trec.nist.gov/pubs/trec31/papers/Overview_deep.pdf)
??? abstract "Abstract"
	
	This is the fourth year of the TREC Deep Learning track. As in previous years, we leverage the MS MARCO datasets that made hundreds of thousands of human annotated training labels available for both passage and document ranking tasks. In addition, this year we also leverage both the refreshed passage and document collections that were released last year leading to a nearly 16 times increase in the size of the passage collection and nearly four times increase in the document collection size. Unlike previous years, in 2022 we mainly focused on constructing a more complete test collection for the passage retrieval task, which has been the primary focus of the track. The document ranking task was kept as a secondary task, where document-level labels were inferred from the passage-level labels. Our analysis shows that similar to previous years, deep neural ranking models that employ large scale pretraining continued to outperform traditional retrieval methods. Due to the focusing our judging resources on passage judging, we are more confident in the quality of this year's queries and judgments, with respect to our ability to distinguish between runs and reuse the dataset in future. We also see some surprises in overall outcomes. Some top-performing runs did not do dense retrieval. Runs that did single-stage dense retrieval were not as competitive this year as they were last year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Craswell0YCLVS22.bib) "
	```
	@inproceedings{DBLP:conf/trec/Craswell0YCLVS22,
		author = {Nick Craswell and Bhaskar Mitra and Emine Yilmaz and Daniel Campos and Jimmy Lin and Ellen M. Voorhees and Ian Soboroff},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2022 Deep Learning Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Overview\_deep.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Craswell0YCLVS22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Hybrid Retrieval and Multi-stage Ranking at TREC 2022 Deep Learning  Track

_Guangwei Xu, Yanzhao Zhang, Longhui Zhang, Dingkun Long, Pengjun Xie, Ruijie Guo_

- :fontawesome-solid-user-group: **Participant:** [Ali](./participants.md#ali)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Ali.D.pdf](https://trec.nist.gov/pubs/trec31/papers/Ali.D.pdf)
- :material-file-search: **Runs:** [pass1](./runs.md#pass1) | [doc1](./runs.md#doc1) | [pass2](./runs.md#pass2) | [pass3](./runs.md#pass3) | [doc3](./runs.md#doc3) | [doc2](./runs.md#doc2)

??? abstract "Abstract"
	
	Large-scale text retrieval technology has been widely used in various practical business scenarios. This paper presents our systems for the TREC 2022 Deep Learning Track. We explain the hybrid text retrieval and multi-stage text ranking method adopted in our solution. The retrieval stage combined the two structures of traditional sparse retrieval and neural dense retrieval. In the ranking stage, in addition to the full interaction-based ranking model built on large pre-trained language model, we also proposes a lightweight sub-ranking module to further enhance the final text ranking performance. Evaluation results demonstrate the effectiveness of our proposed approach. Our models achieve the 1st and 4th rank on the test set of passage ranking and document ranking respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuZZLXG22.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuZZLXG22,
		author = {Guangwei Xu and Yanzhao Zhang and Longhui Zhang and Dingkun Long and Pengjun Xie and Ruijie Guo},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Hybrid Retrieval and Multi-stage Ranking at {TREC} 2022 Deep Learning Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Ali.D.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/XuZZLXG22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### M4D-MKLab/ITI-CERTH Participation in TREC Deep Learning Track 2022

_Alexandros-Michail Koufakis, Theodora Tsikrika, Stefanos Vrochidis, Ioannis Kompatsiaris_

- :fontawesome-solid-user-group: **Participant:** [CERTH_ITI_M4D](./participants.md#certh_iti_m4d)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CERTH_ITI_M4D.D.pdf](https://trec.nist.gov/pubs/trec31/papers/CERTH_ITI_M4D.D.pdf)
- :material-file-search: **Runs:** [rm3_term_filter_rerank](./runs.md#rm3_term_filter_rerank) | [ceqe_custom_rerank](./runs.md#ceqe_custom_rerank)

??? abstract "Abstract"
	
	Our team's (CERTH ITI M4D) participation in TREC Deep Learning Track this year focused on the use of the pretrained BERT model in Query Expansion. We submitted two runs in the document retrieval subtask; both include a final reranking step. The first run incorporates a novel pooling approach for the Contextualized Embedding Query Expansion (CEQE) methodology. The second run introduces a novel term selection mechanism that complements the RM3 query expansion method by filtering disadvantageous expansion terms. The term selection mechanism capitalizes on the BERT model by fine tuning it to predict the quality of terms as expansion terms and can be used on any query expansion technique.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoufakisTVK22.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoufakisTVK22,
		author = {Alexandros{-}Michail Koufakis and Theodora Tsikrika and Stefanos Vrochidis and Ioannis Kompatsiaris},
		editor = {Ian Soboroff and Angela Ellis},
		title = {M4D-MKLab/ITI-CERTH Participation in {TREC} Deep Learning Track 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CERTH\_ITI\_M4D.D.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KoufakisTVK22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CIP at TREC 2022 Deep Learning Track

_Jian Luo, Xinlin Peng, Xuanang Chen, Ben He, Le Sun, Yingfei Sun_

- :fontawesome-solid-user-group: **Participant:** [CIP](./participants.md#cip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CIP.D.pdf](https://trec.nist.gov/pubs/trec31/papers/CIP.D.pdf)
- :material-file-search: **Runs:** [cip_f1](./runs.md#cip_f1) | [cip_f2](./runs.md#cip_f2) | [cip_f3](./runs.md#cip_f3) | [cip_r1](./runs.md#cip_r1) | [cip_r2](./runs.md#cip_r2) | [cip_r3](./runs.md#cip_r3) | [cip_f1_r](./runs.md#cip_f1_r) | [cip_f2_r](./runs.md#cip_f2_r) | [cip_f3_r](./runs.md#cip_f3_r)

??? abstract "Abstract"
	
	This paper describes the CIP participation in the TREC 2022 Deep Learning Track. We submitted runs to both full ranking and re-ranking subtasks of the passage ranking task. In the full ranking sub-task, we adopt a query noise resistant dense retrieval model RoDR. In the re-ranking subtask, we adopt localized contrastive estimation loss and hinge loss rather than pointwise cross-entropy loss for training rerankers. Besides, We utilize both the MS MARCO v1 and v2 passage datasets to generate hopefully sufficient training data, and our models are fine-tuned on these two kinds of training data one by one selectively. Additionally, we introduce docT5query to further enhance the performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuoPCH0S22.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuoPCH0S22,
		author = {Jian Luo and Xinlin Peng and Xuanang Chen and Ben He and Le Sun and Yingfei Sun},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{CIP} at {TREC} 2022 Deep Learning Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CIP.D.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LuoPCH0S22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Efficient Document Representations for Neural Text Ranking

_David Rau, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UAmsterdam.D.pdf](https://trec.nist.gov/pubs/trec31/papers/UAmsterdam.D.pdf)
- :material-file-search: **Runs:** [plm_512](./runs.md#plm_512) | [plm_128](./runs.md#plm_128) | [plm_64](./runs.md#plm_64)

??? abstract "Abstract"
	
	This paper documents the University of Amsterdam's participation in the TREC 2022 Deep Learning Track. We investigate novel document representation approaches capturing long documents within the input token length of neural rankers, and even in a fraction of the maximum input token length. Reducing input length of the document representation leads to dramatic gains in efficiency, as the self-attention over token length is the main culprit of the high gpu memory footprint, low query latency, and small batch sizes. Our experiments result in a number of findings. First, we observe dramatic gains in efficiency of the document representation approaches mindful of what tokens matter most for the neural rankers. Second, we observe the expected trade-off between effectiveness and efficiency, but also observe that document native approaches retrieve numerous documents missed by passage based approaches. This leads to a significant underestimation of their effectiveness, but also highlights their potential to retrieve documents not considered by traditional rankers or passage based neural rankers. There is great potential to study these in future editions of the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RauK22.bib) "
	```
	@inproceedings{DBLP:conf/trec/RauK22,
		author = {David Rau and Jaap Kamps},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Efficient Document Representations for Neural Text Ranking},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UAmsterdam.D.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RauK22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Université Grenoble Alpes / LIG at TREC Deep Learning Track  2022

_Petra Galuscáková, Lucas Alberede, Gabriela Nicole González Sáez, Aidan Mannion, Philippe Mulhem, Georges Quénot_

- :fontawesome-solid-user-group: **Participant:** [UGA](./participants.md#uga)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UGA.D.pdf](https://trec.nist.gov/pubs/trec31/papers/UGA.D.pdf)
- :material-file-search: **Runs:** [fused_3runs](./runs.md#fused_3runs) | [fused_2runs](./runs.md#fused_2runs) | [hierarchical_2runs](./runs.md#hierarchical_2runs) | [graph_colbert](./runs.md#graph_colbert) | [hierarchcal_combination](./runs.md#hierarchcal_combination) | [6systems](./runs.md#6systems) | [2systems](./runs.md#2systems) | [unicoil_reranked](./runs.md#unicoil_reranked) | [4systems](./runs.md#4systems) | [c47](./runs.md#c47)

??? abstract "Abstract"
	
	This paper describes the submissions of the MRIM research Group/Laboratoire d'Informatique de Grenoble from the Universite Grenoble Alpes at the TREC Deep Learning Track 2022. We participated in both fullranking and reranking sub-tasks in the passages ranking task. We proposed several ways to combine neural and non-neural runs using reciprocal-rank based fusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaluscakovaASMM22.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaluscakovaASMM22,
		author = {Petra Galusc{\'{a}}kov{\'{a}} and Lucas Alberede and Gabriela Nicole Gonz{\'{a}}lez S{\'{a}}ez and Aidan Mannion and Philippe Mulhem and Georges Qu{\'{e}}not},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Universit{\'{e}} Grenoble Alpes / {LIG} at {TREC} Deep Learning Track 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UGA.D.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GaluscakovaASMM22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with Adaptive ReRanking and ColBERT-PRF: University of  Glasgow Terrier Team at TREC DL 2022

_Xiao Wang, Sean MacAvaney, Craig Macdonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UoGTr.D.pdf](https://trec.nist.gov/pubs/trec31/papers/UoGTr.D.pdf)
- :material-file-search: **Runs:** [uogtr_dph](./runs.md#uogtr_dph) | [uogtr_dph_bo1](./runs.md#uogtr_dph_bo1) | [uogtr_s](./runs.md#uogtr_s) | [uogtr_se](./runs.md#uogtr_se) | [uogtr_be](./runs.md#uogtr_be) | [uogtr_c](./runs.md#uogtr_c) | [uogtr_be_gb](./runs.md#uogtr_be_gb) | [uogtr_se_gb](./runs.md#uogtr_se_gb) | [uogtr_e_gb](./runs.md#uogtr_e_gb) | [uogtr_se_gt](./runs.md#uogtr_se_gt) | [uogtr_t_cprf](./runs.md#uogtr_t_cprf) | [uogtr_s_cprf](./runs.md#uogtr_s_cprf) | [uogtr_c_cprf](./runs.md#uogtr_c_cprf) | [uogtr_e_cprf_t5](./runs.md#uogtr_e_cprf_t5) | [uogtr_doc_dph_bo1](./runs.md#uogtr_doc_dph_bo1) | [uogtr_doc_dph](./runs.md#uogtr_doc_dph)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2022 Deep Learning Track. In our participation, we applied the Adaptive ReRanking technique on the constructed corpus graph from various first-stage retrieval models, namely the BM25 and SPLADE retrieval models, before applying the reranker, namely the ELECTRA reranking model. In addition, we employed the ColBERT-PRF technique on various first stage retrieval models. Finally, we experimented with ensemble retrieval for implementing both the Adaptive ReRanking and the ColBERT-PRF techniques. We submitted 14 passage ranking runs (including six baseline runs). Among the submitted runs, the run where the Adaptive ReRanking technique is applied on the ensemble of BM25 and SPLADE retrieval, namely uogtr_e_gb, is the most effective in terms of nDCG@10.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangMMO22.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangMMO22,
		author = {Xiao Wang and Sean MacAvaney and Craig Macdonald and Iadh Ounis},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Experiments with Adaptive ReRanking and ColBERT-PRF: University of Glasgow Terrier Team at {TREC} {DL} 2022},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UoGTr.D.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WangMMO22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2022: Deep Learning and Health Misinformation

_Alexander Bondarenko, Maik Fröbe, Lukas Gienapp, Alexander Pugachev, Jan Heinrich Reimer, Ferdinand Schlatt, Ekaterina Artemova, Martin Potthast, Benno Stein, Pavel Braslavski, Matthias Hagen_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Webis.DH.pdf](https://trec.nist.gov/pubs/trec31/papers/Webis.DH.pdf)
- :material-file-search: **Runs:** [webis-dl-duot5](./runs.md#webis-dl-duot5) | [webis-dl-duot5-g](./runs.md#webis-dl-duot5-g) | [webis-dl-duot5-aug-1](./runs.md#webis-dl-duot5-aug-1) | [webis-dl-duot5-aug-2](./runs.md#webis-dl-duot5-aug-2)

??? abstract "Abstract"
	
	We describe the Webis group's participation in the TREC 2022 Deep Learning and Health Misinformation tracks. Our runs submitted to the Deep Learning track focus on improving the pairwise retrieval model duoT5 by combining a greedy aggregation algorithm with document augmentation. In the Health Misinformation track, our submissions to the Answer Prediction task exploit pre-trained question answering and claim verification models, whose input is extended by evidence information from PubMed abstracts. For the Web Retrieval task, we explore re-ranking based on the closeness of the predicted answers for each web document in the initial ranking to the predicted “true” answer of a topic's question.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001FGPRSAP0BH22.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001FGPRSAP0BH22,
		author = {Alexander Bondarenko and Maik Fr{\"{o}}be and Lukas Gienapp and Alexander Pugachev and Jan Heinrich Reimer and Ferdinand Schlatt and Ekaterina Artemova and Martin Potthast and Benno Stein and Pavel Braslavski and Matthias Hagen},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Webis at {TREC} 2022: Deep Learning and Health Misinformation},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Webis.DH.pdf},
		timestamp = {Tue, 29 Aug 2023 17:20:28 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001FGPRSAP0BH22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2022: Deep Learning Track

_Yizheng Huang, Jimmy X. Huang_

- :fontawesome-solid-user-group: **Participant:** [yorku22](./participants.md#yorku22)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/yorku22.D.pdf](https://trec.nist.gov/pubs/trec31/papers/yorku22.D.pdf)
- :material-file-search: **Runs:** [yorku22b](./runs.md#yorku22b) | [yorku22a](./runs.md#yorku22a)

??? abstract "Abstract"
	
	The present study outlines the involvement of the YorkU group in the TREC 2022 Deep Learning Track. This year, the investigation into the fusion of BM25 and the deep learning model, which was initiated in the previous year, is pursued further. The findings from last year's experiments indicate that while the deep learning model was superior for most queries, BM25 demonstrated better performance for particular queries. In our contribution, the queries were classified: BM25 was utilized directly as the final ranking result for queries suited to it, whereas the results of the deep learning model were employed for queries incompatible with BM25. The experimental results indicate that this integrated approach yields improved results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangH22.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangH22,
		author = {Yizheng Huang and Jimmy X. Huang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {York University at {TREC} 2022: Deep Learning Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/yorku22.D.pdf},
		timestamp = {Tue, 17 Oct 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangH22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

