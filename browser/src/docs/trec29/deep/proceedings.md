# Proceedings - Deep Learning 2020 

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

- :fontawesome-solid-user-group: **Participant:** [BIT.UA](./participants.md#bit.ua)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/BIT.UA.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/BIT.UA.PM.pdf)
- :material-file-search: **Runs:** [BIT-run1](./runs.md#bit-run1) | [BIT-run2](./runs.md#bit-run2) | [BIT-run3](./runs.md#bit-run3)

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

- :fontawesome-solid-user-group: **Participant:** [pinganNLP](./participants.md#pingannlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/pinganNLP.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/pinganNLP.DL.pdf)
- :material-file-search: **Runs:** [pinganNLP1](./runs.md#pingannlp1) | [pinganNLP2](./runs.md#pingannlp2) | [pinganNLP3](./runs.md#pingannlp3)

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

- :fontawesome-solid-user-group: **Participant:** [ICIP](./participants.md#icip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/ICIP.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/ICIP.DL.pdf)
- :material-file-search: **Runs:** [ICIP_run1](./runs.md#icip_run1) | [ICIP_run3](./runs.md#icip_run3) | [ICIP_run2](./runs.md#icip_run2)

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

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/RMIT.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/RMIT.DL.pdf)
- :material-file-search: **Runs:** [RMIT-Bart](./runs.md#rmit-bart) | [TF_IDF_d_2_t_50](./runs.md#tf_idf_d_2_t_50) | [DLH_d_5_t_25](./runs.md#dlh_d_5_t_25) | [indri-sdmf](./runs.md#indri-sdmf) | [RMIT_DPH](./runs.md#rmit_dph) | [RMIT_DFRee](./runs.md#rmit_dfree)

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

- :fontawesome-solid-user-group: **Participant:** [NLE](./participants.md#nle)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/NLE.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/NLE.DL.pdf)
- :material-file-search: **Runs:** [NLE_pr1](./runs.md#nle_pr1) | [NLE_pr2](./runs.md#nle_pr2) | [NLE_pr3](./runs.md#nle_pr3)

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

- :fontawesome-solid-user-group: **Participant:** [USI](./participants.md#usi)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/USI.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/USI.DL.pdf)
- :material-file-search: **Runs:** [longformer_1](./runs.md#longformer_1)

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

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/uogTr.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/uogTr.DL.pdf)
- :material-file-search: **Runs:** [uogTrQCBMP](./runs.md#uogtrqcbmp) | [uogTrT20](./runs.md#uogtrt20) | [uogTr31oR](./runs.md#uogtr31or)

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

- :fontawesome-solid-user-group: **Participant:** [HSRM-LAVIS](./participants.md#hsrm-lavis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/HSRM-LAVIS.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/HSRM-LAVIS.DL.pdf)
- :material-file-search: **Runs:** [CoRT-standalone](./runs.md#cort-standalone) | [CoRT-bm25](./runs.md#cort-bm25) | [CoRT-electra](./runs.md#cort-electra)

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

- :fontawesome-solid-user-group: **Participant:** [QU](./participants.md#qu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/QU.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/QU.DL.pdf)
- :material-file-search: **Runs:** [bigIR-DCT-T5-F](./runs.md#bigir-dct-t5-f) | [bigIR-T5xp-T5-F](./runs.md#bigir-t5xp-t5-f) | [bigIR-T5-BERT-F](./runs.md#bigir-t5-bert-f) | [bigIR-BERT-R](./runs.md#bigir-bert-r) | [bigIR-T5-R](./runs.md#bigir-t5-r) | [bigIR-DH-T5-F](./runs.md#bigir-dh-t5-f) | [bigIR-DT-T5-F](./runs.md#bigir-dt-t5-f) | [bigIR-DH-T5-R](./runs.md#bigir-dh-t5-r) | [bigIR-DT-T5-R](./runs.md#bigir-dt-t5-r) | [bigIR-DTH-T5-R](./runs.md#bigir-dth-t5-r) | [bigIR-DTH-T5-F](./runs.md#bigir-dth-t5-f)

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

- :fontawesome-solid-user-group: **Participant:** [TU_Vienna](./participants.md#tu_vienna)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/TU_Vienna.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/TU_Vienna.DL.pdf)
- :material-file-search: **Runs:** [TUW-TK-2Layer](./runs.md#tuw-tk-2layer) | [TUW-TK-Sparse](./runs.md#tuw-tk-sparse) | [TUW-TKL-2k](./runs.md#tuw-tkl-2k) | [TUW-TKL-4k](./runs.md#tuw-tkl-4k)

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

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UAmsterdam.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/UAmsterdam.DL.pdf)
- :material-file-search: **Runs:** [relemb_mlm_0_2](./runs.md#relemb_mlm_0_2) | [bert_6](./runs.md#bert_6) | [bm25_bert_token](./runs.md#bm25_bert_token)

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

- :fontawesome-solid-user-group: **Participant:** [BITEM](./participants.md#bitem)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/BITEM.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/BITEM.DL.pdf)
- :material-file-search: **Runs:** [roberta-large](./runs.md#roberta-large) | [fr_doc_roberta](./runs.md#fr_doc_roberta) | [rr-pass-roberta](./runs.md#rr-pass-roberta) | [fr_pass_roberta](./runs.md#fr_pass_roberta)

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

- :fontawesome-solid-user-group: **Participant:** [mpii](./participants.md#mpii)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/mpii.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/mpii.DL.pdf)
- :material-file-search: **Runs:** [mpii_run1](./runs.md#mpii_run1) | [mpii_run2](./runs.md#mpii_run2) | [mpii_run3](./runs.md#mpii_run3)

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

- :fontawesome-solid-user-group: **Participant:** [MSAI](./participants.md#msai)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/MSAI.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/MSAI.DL.pdf)
- :material-file-search: **Runs:** [ndrm3-orc-full](./runs.md#ndrm3-orc-full) | [ndrm3-orc-re](./runs.md#ndrm3-orc-re) | [ndrm3-full](./runs.md#ndrm3-full) | [ndrm3-re](./runs.md#ndrm3-re) | [ndrm1-full](./runs.md#ndrm1-full) | [ndrm1-re](./runs.md#ndrm1-re)

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

- :fontawesome-solid-user-group: **Participant:** [NLM](./participants.md#nlm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/NLM.HM.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/NLM.HM.DL.pdf)
- :material-file-search: **Runs:** [nlm-ens-bst-3](./runs.md#nlm-ens-bst-3) | [nlm-ens-bst-2](./runs.md#nlm-ens-bst-2) | [nlm-prfun-bert](./runs.md#nlm-prfun-bert) | [nlm-bert-rr](./runs.md#nlm-bert-rr) | [nlm-bm25-prf-1](./runs.md#nlm-bm25-prf-1) | [nlm-bm25-prf-2](./runs.md#nlm-bm25-prf-2)

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

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf)
- :material-file-search: **Runs:** [d_d2q_duo](./runs.md#d_d2q_duo) | [d_d2q_rm3_duo](./runs.md#d_d2q_rm3_duo) | [d_rm3_duo](./runs.md#d_rm3_duo) | [p_d2q_bm25_duo](./runs.md#p_d2q_bm25_duo) | [p_bm25rm3_duo](./runs.md#p_bm25rm3_duo) | [p_d2q_rm3_duo](./runs.md#p_d2q_rm3_duo)

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

- :fontawesome-solid-user-group: **Participant:** [PASH](./participants.md#pash)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/PASH.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/PASH.DL.pdf)
- :material-file-search: **Runs:** [pash_r1](./runs.md#pash_r1) | [pash_r2](./runs.md#pash_r2) | [pash_r3](./runs.md#pash_r3) | [pash_f1](./runs.md#pash_f1) | [pash_f2](./runs.md#pash_f2) | [pash_f3](./runs.md#pash_f3)

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

- :fontawesome-solid-user-group: **Participant:** [UoB](./participants.md#uob)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UoB.DL.pdf](https://trec.nist.gov/pubs/trec29/papers/UoB.DL.pdf)
- :material-file-search: **Runs:** [uob_runid1](./runs.md#uob_runid1) | [uob_runid2](./runs.md#uob_runid2) | [uob_runid3](./runs.md#uob_runid3)

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

