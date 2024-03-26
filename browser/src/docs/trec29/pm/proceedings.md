# Proceedings - Precision Medicine 2020 

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

- :fontawesome-solid-user-group: **Participant:** [vohcolab](./participants.md#vohcolab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/vohcolab.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/vohcolab.PM.pdf)
- :material-file-search: **Runs:** [run_bm25](./runs.md#run_bm25) | [bm25_synonyms](./runs.md#bm25_synonyms)

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

- :fontawesome-solid-user-group: **Participant:** [POZNAN](./participants.md#poznan)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/Poznan.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/Poznan.PM.pdf)
- :material-file-search: **Runs:** [pozadditional](./runs.md#pozadditional) | [pozreranked](./runs.md#pozreranked) | [pozbaseline](./runs.md#pozbaseline)

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

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/uogTr.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/uogTr.PM.pdf)
- :material-file-search: **Runs:** [uog_ufmg_DFRee](./runs.md#uog_ufmg_dfree) | [uog_ufmg_s_dfr5](./runs.md#uog_ufmg_s_dfr5) | [uog_ufmg_secL2R](./runs.md#uog_ufmg_secl2r) | [uog_ufmg_s_dfr0](./runs.md#uog_ufmg_s_dfr0) | [uog_ufmg_sb_df5](./runs.md#uog_ufmg_sb_df5)

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

- :fontawesome-solid-user-group: **Participant:** [MRG_UWaterloo](./participants.md#mrg_uwaterloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/MRG_UWaterloo.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/MRG_UWaterloo.PM.pdf)
- :material-file-search: **Runs:** [uwman](./runs.md#uwman) | [uwbm25](./runs.md#uwbm25) | [uwr](./runs.md#uwr) | [uwrn](./runs.md#uwrn) | [uwpr](./runs.md#uwpr)

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

- :fontawesome-solid-user-group: **Participant:** [ALIBABA](./participants.md#alibaba)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/ALIBABA.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/ALIBABA.PM.pdf)
- :material-file-search: **Runs:** [damoespb1](./runs.md#damoespb1) | [damoespb2](./runs.md#damoespb2) | [damoespcbh1](./runs.md#damoespcbh1) | [damoespcbh2](./runs.md#damoespcbh2) | [damoespcbh3](./runs.md#damoespcbh3)

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

- :fontawesome-solid-user-group: **Participant:** [ims_unipd](./participants.md#ims_unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/ims_unipd.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/ims_unipd.PM.pdf)
- :material-file-search: **Runs:** [bm25_p10](./runs.md#bm25_p10) | [rrf_p10](./runs.md#rrf_p10) | [rrf_prf_p10](./runs.md#rrf_prf_p10) | [rrf_prf_rprec](./runs.md#rrf_prf_rprec) | [rrf_prf_infndcg](./runs.md#rrf_prf_infndcg)

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

- :fontawesome-solid-user-group: **Participant:** [BITEM](./participants.md#bitem)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/BITEM.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/BITEM.PM.pdf)
- :material-file-search: **Runs:** [sibtm_run1](./runs.md#sibtm_run1) | [sibtm_run2](./runs.md#sibtm_run2) | [sibtm_run3](./runs.md#sibtm_run3) | [sibtm_run4](./runs.md#sibtm_run4) | [sibtm_run5](./runs.md#sibtm_run5)

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

- :fontawesome-solid-user-group: **Participant:** [h2oloo](./participants.md#h2oloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/h2oloo.DL.HM.PM.pdf)
- :material-file-search: **Runs:** [duoT5rct](./runs.md#duot5rct) | [monoT5rct](./runs.md#monot5rct) | [duoT5](./runs.md#duot5) | [monoT5](./runs.md#monot5) | [monoT5e1](./runs.md#monot5e1)

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

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/CSIROmed.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/CSIROmed.PM.pdf)
- :material-file-search: **Runs:** [CSIROmed_strDFR](./runs.md#csiromed_strdfr) | [CSIROmed_rlxRR](./runs.md#csiromed_rlxrr) | [CSIROmed_rRRa](./runs.md#csiromed_rrra) | [CSIROmed_strRR](./runs.md#csiromed_strrr) | [CSIROmed_sRRa](./runs.md#csiromed_srra)

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

- :fontawesome-solid-user-group: **Participant:** [CincyMedIR](./participants.md#cincymedir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/CincyMedIR.PM.pdf](https://trec.nist.gov/pubs/trec29/papers/CincyMedIR.PM.pdf)
- :material-file-search: **Runs:** [CincyMedIR_28](./runs.md#cincymedir_28) | [CincyMedIR28dgt](./runs.md#cincymedir28dgt) | [CincyMedIR_28_t](./runs.md#cincymedir_28_t) | [CincyMedIR_20](./runs.md#cincymedir_20) | [CincyMedIR_dgt](./runs.md#cincymedir_dgt)

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

