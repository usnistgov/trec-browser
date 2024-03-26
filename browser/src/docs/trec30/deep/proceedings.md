# Proceedings - Deep Learning 2021 

#### Overview of the TREC 2021 Deep Learning Track

_Nick Craswell, Bhaskar Mitra, Emine Yilmaz, Daniel Campos, Jimmy Lin_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Overview-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/Overview-DL.pdf)
??? abstract "Abstract"
	
	This is the third year of the TREC Deep Learning track. As in previous years, we leverage the MS MARCO datasets that made hundreds of thousands of human annotated training labels available for both passage and document ranking tasks. In addition, this year we refreshed both the document and the passage collections which also led to a nearly four times increase in the document collection size and nearly 16 times increase in the size of the passage collection. Deep neural ranking models that employ large scale pretraininig continued to outperform traditional retrieval methods this year. We also found that single stage retrieval can achieve good performance on both tasks although they still do not perform at par with multistage retrieval pipelines. Finally, the increase in the collection size and the general data refresh raised some questions about completeness of NIST judgments and the quality of the training labels that were mapped to the new collections from the old ones which we discuss in this report.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Craswell0YCL21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Craswell0YCL21,
		author = {Nick Craswell and Bhaskar Mitra and Emine Yilmaz and Daniel Campos and Jimmy Lin},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2021 Deep Learning Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Overview-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Craswell0YCL21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2021: Deep Learning, Health Misinformation, and Podcasts  Tracks

_Alexander Bondarenko, Maik Fröbe, Sebastian Günther, Matthias Hagen, Marcel Gohsen, Johannes Kiesel, Michael Völske, Benno Stein, Jakob Schwerter, Shahbaz Syed, Martin Potthast_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf)
- :material-file-search: **Runs:** [webis-dl-1](./runs.md#webis-dl-1) | [webis-dl-2](./runs.md#webis-dl-2) | [webis-dl-3](./runs.md#webis-dl-3)

??? abstract "Abstract"
	
	We describe the Webis group's participation in the TREC 2021 Deep Learning, Health Misinformation, and Podcasts tracks. Our three LambdaMART-based runs submitted to the Deep Learning track focus on the question whether anchor text is an effective retrieval feature in the MS MARCO scenario. In the Health Misinformation track, we axiomatically re-ranked the top-20 results of BM25 and MonoT5 for argumentative topics. As for the Podcasts track, our submitted six runs focus on supervised classification of podcasts as entertaining, subjective, or containing discussion by using audio and text embeddings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001F0HGKV0SSP21.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001F0HGKV0SSP21,
		author = {Alexander Bondarenko and Maik Fr{\"{o}}be and Sebastian G{\"{u}}nther and Matthias Hagen and Marcel Gohsen and Johannes Kiesel and Michael V{\"{o}}lske and Benno Stein and Jakob Schwerter and Shahbaz Syed and Martin Potthast},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Webis at {TREC} 2021: Deep Learning, Health Misinformation, and Podcasts Tracks},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 17:23:07 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001F0HGKV0SSP21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CIP at TREC 2021 Deep Learning Track

_Xuanang Chen, Ben He, Le Sun, Yingfei Sun_

- :fontawesome-solid-user-group: **Participant:** [CIP](./participants.md#cip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CIP-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/CIP-DL.pdf)
- :material-file-search: **Runs:** [CIP_run1](./runs.md#cip_run1) | [CIP_run2](./runs.md#cip_run2) | [CIP_run3](./runs.md#cip_run3)

??? abstract "Abstract"
	
	This paper describes the CIP participation in the TREC 2021 Deep Learning Track. Akin to our previous participation, we adopt the passage-level BERT re-ranker in the re-ranking subtask of the document ranking task. Besides, we utilize the MS MARCO v1 passage dataset and both the MS MARCO v2 passage and document datasets to generate hopefully sufficient training data, and BERT re-ranker is fine-tuned on these three kinds of training data one by one. Meanwhile, we adopt pairwise hinge loss rather than pointwise cross-entropy loss this year for model training, to boost the ranking effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenH0S21.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenH0S21,
		author = {Xuanang Chen and Ben He and Le Sun and Yingfei Sun},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{CIP} at {TREC} 2021 Deep Learning Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CIP-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ChenH0S21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TU Wien at TREC DL and Podcast 2021: Simple Compression for  Dense Retrieval

_Sebastian Hofstätter, Mete Sertkan, Allan Hanbury_

- :fontawesome-solid-user-group: **Participant:** [TU_Vienna](./participants.md#tu_vienna)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/TU_Vienna-DL-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/TU_Vienna-DL-Pod.pdf)
- :material-file-search: **Runs:** [TUW_DR_Base](./runs.md#tuw_dr_base) | [TUW_TAS-B_768](./runs.md#tuw_tas-b_768) | [TUW_TAS-B_ANN](./runs.md#tuw_tas-b_ann) | [TUW_IDCM_S4](./runs.md#tuw_idcm_s4) | [TUW_IDCM_ALL](./runs.md#tuw_idcm_all)

??? abstract "Abstract"
	
	The IR group of TU Wien participated in two tracks at TREC 2021: Deep Learning and Podcast segment retrieval. We continued our focus from our previous TREC participations on efficient approaches for retrieval and re-ranking. We propose a simple training process for compressing a dense retrieval model's output. First, we train it with full capacity, and then add a compression, or dimensionality reduction, layer on top and conduct a second full training pass. At TREC 2021 we test this model in a blind evaluation and zero-shot collection transfer for both Deep Learning and Podcast tracks. For our participation at the Podcast segment retrieval track, we also employ hybrid sparse-dense retrieval. Furthermore, we utilize auxiliary information to re-rank the retrieved segments by entertainment and subjectivity signals. Our results show that our simple compression procedure with approximate nearest neighbor search achieves comparable in-domain results (minus 2 points nDCG@10 difference) to a full TAS-Balanced retriever and reasonable effectiveness in a zero-shot domain transfer (Podcast track), where we outperform BM25 by 6 points nDCG@10.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HofstatterSH21.bib) "
	```
	@inproceedings{DBLP:conf/trec/HofstatterSH21,
		author = {Sebastian Hofst{\"{a}}tter and Mete Sertkan and Allan Hanbury},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TU} Wien at {TREC} {DL} and Podcast 2021: Simple Compression for Dense Retrieval},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/TU\_Vienna-DL-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HofstatterSH21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2021: Deep Learning Track

_Yizheng Huang, Jimmy X. Huang_

- :fontawesome-solid-user-group: **Participant:** [yorku](./participants.md#yorku)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/yorku-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/yorku-DL.pdf)
- :material-file-search: **Runs:** [yorku21_a](./runs.md#yorku21_a) | [yorku21_b](./runs.md#yorku21_b) | [yorku21_c](./runs.md#yorku21_c)

??? abstract "Abstract"
	
	This is our first time to participate in TREC Deep Learning track. We submitted three BERT-based runs “YorkU21a”, “YorkU21b” and “YorkU21c”, where YorkU21a has the best performance. Our main goal is to explore the possibility of combining deep learning with traditional BM25 retrieval method. In this paper, we discuss the results of using the summation method to combine the above two approaches and provide some illustrative analyses on the impact of different retrieval strategies on the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangH21.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangH21,
		author = {Yizheng Huang and Jimmy X. Huang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {York University at {TREC} 2021: Deep Learning Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/yorku-DL.pdf},
		timestamp = {Tue, 17 Oct 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangH21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### M4D-MKLab/ITI-CERTH Participation in TREC Deep Learning Track 2021

_Alexandros-Michail Koufakis, Theodora Tsikrika, Stefanos Vrochidis, Ioannis Kompatsiaris_

- :fontawesome-solid-user-group: **Participant:** [CERTH_ITI_M4D](./participants.md#certh_iti_m4d)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CERTH_ITI_M4D-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/CERTH_ITI_M4D-DL.pdf)
- :material-file-search: **Runs:** [bigrams_cont_qe](./runs.md#bigrams_cont_qe) | [bigram_qe_cedr](./runs.md#bigram_qe_cedr)

??? abstract "Abstract"
	
	Our team's (CERTH ITI M4D) goal in the TREC Deep Learning Track was to study how the Contextualized Embedding Query Expansion (CEQE) [1] method performs in such setting and how our proposed modifications affect the performance. In particular, we examine how CEQE performs with the addition of bigrams as potential expansion terms, and how an IDF weight component affects the performance. The first run we submitted is produced by a query expansion pipeline that uses BM25 for retrieval and CEQE with the IDF modification for query expansion. The second submitted run used a modification of CEQE with the addition of bigrams as candidate expansion terms and a re-ranking step using CEDR. Our runs showed promising results, especially for Average Precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoufakisTVK21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoufakisTVK21,
		author = {Alexandros{-}Michail Koufakis and Theodora Tsikrika and Stefanos Vrochidis and Ioannis Kompatsiaris},
		editor = {Ian Soboroff and Angela Ellis},
		title = {M4D-MKLab/ITI-CERTH Participation in {TREC} Deep Learning Track 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CERTH\_ITI\_M4D-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KoufakisTVK21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Naver Labs Europe (SPLADE) @ TREC Deep Learning 2021

_Carlos Lassance, Arnaud Sors, Stéphane Clinchant, Thibault Formal, Benjamin Piwowarski_

- :fontawesome-solid-user-group: **Participant:** [NLE](./participants.md#nle)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/NLE-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/NLE-DL.pdf)
- :material-file-search: **Runs:** [NLE_P_v1](./runs.md#nle_p_v1) | [NLE_P_V1andV2](./runs.md#nle_p_v1andv2) | [NLE_P_quick](./runs.md#nle_p_quick) | [NLE_D_v1](./runs.md#nle_d_v1) | [NLE_D_V1andV2](./runs.md#nle_d_v1andv2) | [NLE_D_quick](./runs.md#nle_d_quick)

??? abstract "Abstract"
	
	This paper describes our participation to the 2021 TREC Deep Learning challenge. We submitted runs to both passage and document full ranking tasks, with a focus on the passage task, where the goal is to retrieve and rank a set of 100 passages directly from the new MS MARCO v2 collection, containing around 138M entries. We rely on SPLADE for first-stage retrieval. For the second stage, we use an ensemble of BERT re-rankers, trained using hard negatives selected by SPLADE. Three runs were submitted, coming from a diverse set of experiments: i) a fast retriever without re-ranking nor query encoding (SPLADE-doc model), ii) a SPLADE model fully trained on MS MARCO v1, and re-ranked by an en- semble of models, and iii) an ensemble of SPLADE models trained on both new and old MS MARCO, re-ranked by an ensemble of models also trained on both datasets. Much to our surprise, out of the 3 runs, the one trained only on MS MARCO v1 obtained the best results on the TREC competition and is very competitive when compared to the median and best results. More surprising to us is that the results on the dev set of MS MARCO v2 did not correlate with TREC results, contrary to previous years.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LassanceSCFP21.bib) "
	```
	@inproceedings{DBLP:conf/trec/LassanceSCFP21,
		author = {Carlos Lassance and Arnaud Sors and St{\'{e}}phane Clinchant and Thibault Formal and Benjamin Piwowarski},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Naver Labs Europe {(SPLADE)} @ {TREC} Deep Learning 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/NLE-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LassanceSCFP21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### L3S at the TREC 2021 Deep Learning Track

_Jurek Leonhardt, Avishek Anand, Koustav Rudra_

- :fontawesome-solid-user-group: **Participant:** [L3S](./participants.md#l3s)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/L3S-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/L3S-DL.pdf)
- :material-file-search: **Runs:** [Fast_Forward_2](./runs.md#fast_forward_2) | [Fast_Forward_5](./runs.md#fast_forward_5) | [Fast_Forward_7](./runs.md#fast_forward_7) | [Fast_Forward_3](./runs.md#fast_forward_3) | [Fast_ForwardP_2](./runs.md#fast_forwardp_2) | [Fast_ForwardP_5](./runs.md#fast_forwardp_5)

??? abstract "Abstract"
	
	In this paper we describe the approach we used for the passage and document ranking task in the TREC 2021 deep learning track. Our approach aims for efficient retrieval and re-ranking by making use of fast look-up-based forward indexes for dense dual-encoder models. The score of a query-document pair is computed as a linear interpolation of the corresponding lexical (BM25) and semantic (re-ranking) scores. This is akin to performing the re-ranking step “implicitly” together with the retrieval step. We improve efficiency by avoiding forward passes of expensive re-ranking models without compromising performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeonhardtAR21.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeonhardtAR21,
		author = {Jurek Leonhardt and Avishek Anand and Koustav Rudra},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{L3S} at the {TREC} 2021 Deep Learning Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/L3S-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LeonhardtAR21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Quality and Cost Trade-Offs in Passage Re-Ranking Task

_Pavel Podberezko, Vsevolod Mitskevich, Raman Makouski, Pavel Goncharov, Andrei Khobnia, Nikolay Bushkov, Marina Chernyshevich_

- :fontawesome-solid-user-group: **Participant:** [IHSM](./participants.md#ihsm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IHSM-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/IHSM-DL.pdf)
- :material-file-search: **Runs:** [ihsm_colbert64](./runs.md#ihsm_colbert64) | [ihsm_bicolbert](./runs.md#ihsm_bicolbert) | [ihsm_poly8q](./runs.md#ihsm_poly8q)

??? abstract "Abstract"
	
	Deep learning models named transformers achieved state-of-the-art results in a vast majority of NLP tasks at the cost of increased computational complexity and high memory consumption. Using the transformer model in real-time inference becomes a major challenge when implemented in production, because it requires expensive computational resources. The more executions of a transformer are needed the lower the overall throughput is, and switching to the smaller encoders leads to the decrease of accuracy. Our paper is devoted to the problem of how to choose the right architecture for the ranking step of the information retrieval pipeline, so that the number of required calls of transformer encoder is minimal with the maximum achievable quality of ranking. We investigated several late-interaction models such as Colbert and Poly-encoder architectures along with their modifications. Also, we took care of the memory footprint of the search index and tried to apply the learning-to-hash method to binarize the output vectors from the transformer encoders. The results of the evaluation are provided using TREC 2019-2021 and MS Marco dev datasets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PodberezkoMMGKB21.bib) "
	```
	@inproceedings{DBLP:conf/trec/PodberezkoMMGKB21,
		author = {Pavel Podberezko and Vsevolod Mitskevich and Raman Makouski and Pavel Goncharov and Andrei Khobnia and Nikolay Bushkov and Marina Chernyshevich},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Quality and Cost Trade-Offs in Passage Re-Ranking Task},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IHSM-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PodberezkoMMGKB21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PASH at TREC 2021 Deep Learning Track: Generative Enhanced Model  for Multi-stageRankingtrack: DL

_Yixuan Qiao, Hao Chen, Tuozhen Liu, Xianbin Ye, Jun Wang, Peng Gao, Guotong Xie_

- :fontawesome-solid-user-group: **Participant:** [PASH](./participants.md#pash)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/PASH-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/PASH-DL.pdf)
- :material-file-search: **Runs:** [pash_r1](./runs.md#pash_r1) | [pash_r2](./runs.md#pash_r2) | [pash_r3](./runs.md#pash_r3) | [pash_f1](./runs.md#pash_f1) | [pash_f2](./runs.md#pash_f2) | [pash_f3](./runs.md#pash_f3) | [pash_doc_r1](./runs.md#pash_doc_r1) | [pash_doc_r2](./runs.md#pash_doc_r2) | [pash_doc_f1](./runs.md#pash_doc_f1) | [pash_doc_f4](./runs.md#pash_doc_f4) | [pash_doc_f5](./runs.md#pash_doc_f5) | [pash_doc_r3](./runs.md#pash_doc_r3)

??? abstract "Abstract"
	
	This paper describes the PASH participation in TREC 2021 Deep Learning Track. In the recall stage, we adopt a scheme combining sparse and dense retrieval method. In the multi-stage ranking phase, point-wise and pair-wise ranking strategies are used one after another based on model continual pre-trained on general knowledge and document-level data. Compared to TREC 2020 Deep Learning Track, we have additionally introduced the generative model T5 to further enhance the performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiaoC0GXLYX21.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiaoC0GXLYX21,
		author = {Yixuan Qiao and Hao Chen and Tuozhen Liu and Xianbin Ye and Jun Wang and Peng Gao and Guotong Xie},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{PASH} at {TREC} 2021 Deep Learning Track: Generative Enhanced Model for Multi-stageRankingtrack: {DL}},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/PASH-DL.pdf},
		timestamp = {Fri, 15 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/QiaoC0GXLYX21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Recall Aspects of Transformers for Text Ranking

_David Rau, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UAmsterdam-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/UAmsterdam-DL.pdf)
- :material-file-search: **Runs:** [top1000](./runs.md#top1000)

??? abstract "Abstract"
	
	This paper documents the University of Amsterdam's participation in the TREC 2021 Deep Learning Track. In addition to providing labeled training data at scale, the other major contribution of the TREC DL track is to avoid the pool-bias exhibited in all the earlier adhoc search test collections created through the pooling only runs from traditional sparse retrieval systems. However, even in the TREC deep learning track, we have shallow pools, and runs with varying but high fractions of unjudged documents. This prompts a deeper analysis of pool coverage over ranks for both a representative traditional approach (i.e., BM25) and a representative neural approach (i.e., the BERT cross-encoder for the passage retrieval task). Our main conclusions are the following. First, we submitted a neural run that specifically looks beyond those documents easily found by traditional models, highlighting the potential of neural models to address recall aspects in addition to the precision aspects prioritized in the TREC Deep Learning Track up to now. Second, we observe high fractions of unjudged documents after the initial ranks for both the 2020 and 2021 data, which may hinder the evaluation of recall-oriented aspects and reusability of the judgments for runs not contributing to the pooling. Third, we observe a gradual decline of the fraction of relevant over judged documents for 2020, which is a positive sign against pooling bias, but almost no decrease for 2021. Our general conclusion is that coverage below the guaranteed pooling horizon is far from complete and that analysis of recall aspects must be done with care, but that there is great potential to study these in future editions of the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RauK21.bib) "
	```
	@inproceedings{DBLP:conf/trec/RauK21,
		author = {David Rau and Jaap Kamps},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Recall Aspects of Transformers for Text Ranking},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UAmsterdam-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RauK21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

