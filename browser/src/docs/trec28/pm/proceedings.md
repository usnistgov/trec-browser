# Proceedings - Precision Medicine 2019 

#### Overview of the TREC 2019 Precision Medicine Track

_Kirk Roberts, Dina Demner-Fushman, Ellen M. Voorhees, William R. Hersh, Steven Bedrick, Alexander J. Lazar, Shubham Pant, Funda Meric-Bernstam_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/OVERVIEW.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/OVERVIEW.PM.pdf)
??? abstract "Abstract"
	
	Precision medicine is a medical paradigm in which treatments are customized entirely to the individual patient. The underlying issue that drives precision medicine is that for many complex diseases, there are no “one size fits all” solutions for patients with a particular diagnosis. The proper treatment for a patient depends upon genetic, environmental, and lifestyle choices. The ability to personalize treatment in a scientifically rigorous manner based on these factors is thus the hallmark of the emerging precision medicine paradigm. Nowhere is the potential impact of precision medicine more closely focused at the moment than in cancer, where lifesaving treatments for particular patients could prove ineffective or even deadly for other patients based entirely upon the particular genetic mutations in the patient's tumor(s). Significant effort, therefore, has been devoted to deepening the scientific research surrounding precision medicine. This includes the Precision Medicine Initiative (Collins and Varmus, 2015) launched by President Barack Obama in 2015, now known as the All of Us Research Program. A fundamental difficulty with putting the findings of precision medicine into practice is that-by its very nature-precision medicine creates a very large space of treatment options (Frey et al., 2016). These can easily overwhelm clinicians attempting to stay up-to-date with the latest findings, and can easily inhibit a clinician's attempts to determine the best possible treatment for a particular patient. However, the ability to quickly locate relevant evidence is the hallmark of information retrieval (IR). [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsDVHBLPM19.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsDVHBLPM19,
		author = {Kirk Roberts and Dina Demner{-}Fushman and Ellen M. Voorhees and William R. Hersh and Steven Bedrick and Alexander J. Lazar and Shubham Pant and Funda Meric{-}Bernstam},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/OVERVIEW.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsDVHBLPM19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Brown University at TREC Precision Medicine 2019

_Abdullah Ahmed, Gil Alon, Bashar Zaidat, Isaac Nathoo, Hwai-Liang Tung, Charles Wang, Carsten Eickhoff_

- :fontawesome-solid-user-group: **Participant:** [Brown](./participants.md#brown)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/Brown.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/Brown.PM.pdf)
- :material-file-search: **Runs:** [rrf_1](./runs.md#rrf_1) | [rrf_2](./runs.md#rrf_2) | [eged](./runs.md#eged) | [egnd](./runs.md#egnd) | [ngnd](./runs.md#ngnd)

??? abstract "Abstract"
	
	This paper describes Brown University's submission to the TREC 2019 Precision Medicine (PM) track. We expand disease and gene name related terms, prune expanded queries and boost the importance of key terms. Our retrieval model is based on BM25F and incorporates heuristic relevance eligibility filters for clinical trials as well as reciprocal rank fusion of constituent runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AhmedAZNTWE19.bib) "
	```
	@inproceedings{DBLP:conf/trec/AhmedAZNTWE19,
		author = {Abdullah Ahmed and Gil Alon and Bashar Zaidat and Isaac Nathoo and Hwai{-}Liang Tung and Charles Wang and Carsten Eickhoff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Brown University at {TREC} Precision Medicine 2019},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/Brown.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AhmedAZNTWE19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Designing retrieval models to contrast precision-driven ad hoc search  vs. recall-driven treatment extraction in Precision Medicine

_Déborah Caucheteur, Emilie Pasche, Julien Gobeill, Anaïs Mottaz, Luc Mottin, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BITEM_PM](./participants.md#bitem_pm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/BITEM_PM.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/BITEM_PM.PM.pdf)
- :material-file-search: **Runs:** [SIBTMct1](./runs.md#sibtmct1) | [SIBTMct2](./runs.md#sibtmct2) | [SIBTMct3](./runs.md#sibtmct3) | [SIBTMct4](./runs.md#sibtmct4) | [SIBTMct5](./runs.md#sibtmct5) | [SIBTMlit1](./runs.md#sibtmlit1) | [SIBTMlit3](./runs.md#sibtmlit3) | [SIBTMlit2](./runs.md#sibtmlit2) | [SIBTMlit5](./runs.md#sibtmlit5) | [SIBTMlit4](./runs.md#sibtmlit4)

??? abstract "Abstract"
	
	The TREC 2019 Precision Medicine Track repeats the general structure and evaluation of the 2018 track. Our team participated in both tasks of the track, relative to scientific abstracts and clinical trials. 40 topics where patient data are given (demographic data, disease, gene and genetic variant) were available for this competition. The aim was to retrieve scientific abstracts and clinical trials of interest regarding a topic, modelling the description of a clinical case. In the first task, we aim at retrieving scientific abstracts introducing some relevant treatments for a given case. Our system is first based on the collection of a large set of abstracts related to a particular case using various strategies such as search with keywords within abstracts, search with normalized entities within annotated abstracts and the linear combination of various queries. We then apply different strategies to re-rank the resulting scientific abstracts set. In particular, we tested two strategies to re-rank the abstracts set in order to have a large variety of treatments returned in the top articles. Almost two thirds of the top-10 returned documents are judged relevant, while nearly a quarter of the relevant treatments is returned in the top-10 abstracts. The second task aims at retrieving some clinical trials for which patients are eligible. Criteria used to determine the eligibility of patients are those found in the topics. Information such as trial location or status of clinical trials, which are important from a patient's point of view, are questionably not used in these topics. Several strategies have been tested, relaxing of constraints (data required or not), expansion of information requests thanks to synonyms or regex, and retrieval status value boosting for some criteria or fields. After judging, for almost half of the topics, a minimum of 50% of the documents retrieved are relevant, up to 90% for 10 of the 38 topics provided. Almost two thirds of the top-10 returned documents are judged relevant, while nearly a quarter of the relevant treatments is returned in the top-10 abstracts. Our best runs achieve highly competitive results depending on the measures, with on average being ranked #2 or #3 according to the official results for the literature task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaucheteurPGMMR19.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaucheteurPGMMR19,
		author = {D{\'{e}}borah Caucheteur and Emilie Pasche and Julien Gobeill and Ana{\"{\i}}s Mottaz and Luc Mottin and Patrick Ruch},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Designing retrieval models to contrast precision-driven ad hoc search vs. recall-driven treatment extraction in Precision Medicine},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/BITEM\_PM.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CaucheteurPGMMR19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Poznan Contribution to TREC-PM 2019

_Artur Cieslewicz, Jakub Dutkiewicz, Czeslaw Jedrzejek_

- :fontawesome-solid-user-group: **Participant:** [POZNAN](./participants.md#poznan)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/Poznan.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/Poznan.PM.pdf)
- :material-file-search: **Runs:** [bc](./runs.md#bc) | [w2v_noletor](./runs.md#w2v_noletor) | [w2v_letor](./runs.md#w2v_letor) | [simple_letor](./runs.md#simple_letor) | [simple](./runs.md#simple) | [SA_LGD_letor](./runs.md#sa_lgd_letor) | [SA_DPH_letor](./runs.md#sa_dph_letor) | [SAsimpleLGD](./runs.md#sasimplelgd) | [SA_bc](./runs.md#sa_bc)

??? abstract "Abstract"
	
	This paper describes Pozna´n contribution to the Precision Medicine track of the TREC 2019. In this submission we present several novelties. We cover the motivation for the hand-picked values of the weights assigned to the expanded query terms. We propose a result fusion method - slightly modified version of Borda Count algorithm. Additionally we use a learning to rank environment, we analyze the effectiveness of such an approach in combination with our other methods and analyze the achieved results. We also discuss our dedicated document processing methods. We achieve an improvement of up to 0.02 (infNDCG measure) over the baseline for Clinical Trials with our proposed methods, however the evaluation value of our baseline is much lower than the median of all contributions. The reverse effect happens in the Scientific Abstracts task, the baseline we propose is much stronger than the median, but the default setting of learning to rank proposition lowers the overall evaluation score.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CieslewiczDJ19.bib) "
	```
	@inproceedings{DBLP:conf/trec/CieslewiczDJ19,
		author = {Artur Cieslewicz and Jakub Dutkiewicz and Czeslaw Jedrzejek},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Poznan Contribution to {TREC-PM} 2019},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/Poznan.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CieslewiczDJ19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Deep Learning Approach for the Precision Medicine Track

_Juan Pablo Consuegra-Ayala, Giovanni Stilo, Alessandro Celi, Amleto Di Salle_

- :fontawesome-solid-user-group: **Participant:** [UNIVAQ](./participants.md#univaq)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UNIVAQ.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/UNIVAQ.PM.pdf)
- :material-file-search: **Runs:** [tk1allfuzzy](./runs.md#tk1allfuzzy) | [tk3allfuzzy](./runs.md#tk3allfuzzy) | [tk1allbinary](./runs.md#tk1allbinary) | [tk3nodemogr](./runs.md#tk3nodemogr) | [tk3onlygnds](./runs.md#tk3onlygnds) | [default100k](./runs.md#default100k) | [default1m](./runs.md#default1m)

??? abstract "Abstract"
	
	The paper describes the system presented by the University of L'Aquila in collaboration with the University of Havana - team named UNIVAQ - to the TREC 2019 Precision Medicine Track. The proposed solution, maps any kind of documents - Scientific Abstract, Clinical trials, and Topics - into a multi-dimensional common general representation. Each document is described by five primitive features. The values of each feature are extracted from the original documents using deep learning and machine learning text processing based techniques. To recognize Genes and Diseases, we have trained our models using the PubTator annotated corpus. Instead, to derive demographics information, we have trained the em- ployed deep learning models using the documents -obtained from the Relevance and Raw judgements of the past edition of TREC Precision Medicine / Clinical Decision Support Track 2018- considered “relevant” or “partially relevant”. The results of the Track clearly show that applying a system (as our) made solely by a tagging based approach to the Precision Medicine task, is not sufficient to achieve the performances gained by other systems presented in the TREC Precision Medicine Track 2019.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Consuegra-Ayala19.bib) "
	```
	@inproceedings{DBLP:conf/trec/Consuegra-Ayala19,
		author = {Juan Pablo Consuegra{-}Ayala and Giovanni Stilo and Alessandro Celi and Amleto Di Salle},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Deep Learning Approach for the Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UNIVAQ.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Consuegra-Ayala19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JULIE Lab & Med Uni Graz @ TREC 2019 Precision Medicine Track

_Erik Faessler, Udo Hahn, Michel Oleynik_

- :fontawesome-solid-user-group: **Participant:** [julie-mug](./participants.md#julie-mug)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/julie-mug.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/julie-mug.PM.pdf)
- :material-file-search: **Runs:** [jlctphrase](./runs.md#jlctphrase) | [jlpmtrcommon](./runs.md#jlpmtrcommon) | [jlpmletor](./runs.md#jlpmletor) | [jlpmltrin](./runs.md#jlpmltrin) | [jlctletor](./runs.md#jlctletor) | [jlctltrin](./runs.md#jlctltrin) | [jlpmtrboost](./runs.md#jlpmtrboost) | [jlctprec](./runs.md#jlctprec) | [jlctgenes](./runs.md#jlctgenes) | [jlpmcommon2](./runs.md#jlpmcommon2)

??? abstract "Abstract"
	
	The 2019 Precision Medicine Track at TREC (TREC-PM) aimed at identifying relevant documents from two collections, namely PubMed (biomedical abstracts) and ClinicalTrials.gov (clinical trials), given 40 precision medicine topics representing (virtual) patients. The organizers also proposed a new subtask on treatment retrieval from PubMed. We describe our contributions based on five runs for each task, including two runs for the treatment subtask using a naïve strategy. Our approach builds upon carefully designed weighted queries based on our experience from last year's participation and explores the usefulness of Learning to Rank (LETOR), trained on either the previous official gold standards or an internal reference standard for the topics chosen for the 2019 challenge. Our best results culminated in infNDCG = 0.5783, P@10 = 0.6525, and R-Prec = 0.3572 for the biomedical abstracts task and infNDCG = 0.6451, P@10 = 0.5474, and R-Prec = 0.4814 for the clinical trials task, obtained with a baseline retrieval strategy. LETOR worsened our results, especially when using the internal reference standard.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FaesslerHO19.bib) "
	```
	@inproceedings{DBLP:conf/trec/FaesslerHO19,
		author = {Erik Faessler and Udo Hahn and Michel Oleynik},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{JULIE} Lab {\&} Med Uni Graz @ {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/julie-mug.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FaesslerHO19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2019: Precision Medicine Track

_Jingkun Feng, Zhihao Yang, Zhiqiang Liu, Ling Luo, Hongfei Lin, Jian Wang_

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./participants.md#dutir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/DUTIR.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/DUTIR.PM.pdf)
- :material-file-search: **Runs:** [DutirRun1](./runs.md#dutirrun1) | [DutirRun2](./runs.md#dutirrun2) | [DutirRun3](./runs.md#dutirrun3) | [DutirRun4](./runs.md#dutirrun4) | [DutirRun5](./runs.md#dutirrun5) | [Dutir_Cli1](./runs.md#dutir_cli1) | [Dutir_Cli2](./runs.md#dutir_cli2)

??? abstract "Abstract"
	
	This paper describes the system developed for the TREC 2019 Precision Medicine Track by the Team DUTIR from Dalian University of Technology. In the system, we applied a hybrid method to score the related documents for each topic. First, we used Elasticsearch, an open-source Lucene-based full-text search engine, to obtain the initial retrieval results. Then we trained several deep models using TREC 2017 PM data. Finally, we applied the pre-trained models to reorder the initial search results. The performance of our system is above the median for the scientific abstracts subtask and below median for the clinical trials subtask.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FengYLLLW19.bib) "
	```
	@inproceedings{DBLP:conf/trec/FengYLLLW19,
		author = {Jingkun Feng and Zhihao Yang and Zhiqiang Liu and Ling Luo and Hongfei Lin and Jian Wang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DUTIR} at {TREC} 2019: Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/DUTIR.PM.pdf},
		timestamp = {Mon, 03 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FengYLLLW19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CBNU at TREC 2019 Precision Medicine Track

_Seung-Hyeon Jo, Kyung-Soon Lee_

- :fontawesome-solid-user-group: **Participant:** [cbnu](./participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/cbnu.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/cbnu.PM.pdf)
- :material-file-search: **Runs:** [cbnuCT1](./runs.md#cbnuct1) | [cbnuCT2](./runs.md#cbnuct2) | [cbnuCT3](./runs.md#cbnuct3) | [cbnuCT4](./runs.md#cbnuct4) | [cbnuSA1](./runs.md#cbnusa1) | [cbnuSA2](./runs.md#cbnusa2) | [cbnuSA3](./runs.md#cbnusa3) | [cbnuSA4](./runs.md#cbnusa4)

??? abstract "Abstract"
	
	This paper describes the participation of the CBNU team at the TREC Precision Medicine Track 2019. We use the cancer-centered document clusters based on graph embedding. Documents are retrieved by re-ranking documents and pseudo-relevance feedback based on cancer-centered document clusters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoL19.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoL19,
		author = {Seung{-}Hyeon Jo and Kyung{-}Soon Lee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CBNU} at {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/cbnu.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoL19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SCUT-CCNL at TREC 2019 Precision Medicine Track

_Xiaofeng Liu, Lu Li, Zuoxi Yang, Shoubin Dong_

- :fontawesome-solid-user-group: **Participant:** [CCNL](./participants.md#ccnl)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CCNL.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/CCNL.PM.pdf)
- :material-file-search: **Runs:** [ccnl_trials1](./runs.md#ccnl_trials1) | [ccnl_trials2](./runs.md#ccnl_trials2) | [ccnl_sa1](./runs.md#ccnl_sa1) | [ccnl_sa2](./runs.md#ccnl_sa2) | [ccnl_sa3](./runs.md#ccnl_sa3) | [ccnl_sa5](./runs.md#ccnl_sa5) | [ccnl_sa4](./runs.md#ccnl_sa4)

??? abstract "Abstract"
	
	This paper describes a retrieval system developed for the TREC 2019 Precision Medicine Track. For two tasks of Scientific Abstracts and Clinical Trials, we applied the same structure, including the retrieval model, the query expansion and the re-ranking model, to generate the final retrieval results. The experiment results show that the re-ranking model based on SciBERT is of great benefit for retrieval tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuLYD19.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuLYD19,
		author = {Xiaofeng Liu and Lu Li and Zuoxi Yang and Shoubin Dong},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{SCUT-CCNL} at {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CCNL.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuLYD19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2019 Precision Medicine - Medical University of Graz

_Pilar López-Úbeda, José Antonio Vera-Ramos, Pablo López-García_

- :fontawesome-solid-user-group: **Participant:** [imi_mug](./participants.md#imi_mug)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/imi_mug.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/imi_mug.PM.pdf)
- :material-file-search: **Runs:** [imi_mug1](./runs.md#imi_mug1) | [imi_mug2](./runs.md#imi_mug2) | [imi_mug3](./runs.md#imi_mug3) | [imi_mug2_t](./runs.md#imi_mug2_t) | [imi_mug3_t](./runs.md#imi_mug3_t)

??? abstract "Abstract"
	
	In this paper we report on our participation in the TREC 2019 Precision Medicine track (team name: imi_mug). We submitted 5 fully automatic runs to the biomedical articles subtask, two of them with treatments. Our system was based on Elasticsearch, templates, and parameter grid search query generation, building heavily on our previous participation and the reference standards from 2017 and 2018. Our results are close to the mean for the biomedical articles subtask.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lopez-UbedaVL19.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lopez-UbedaVL19,
		author = {Pilar L{\'{o}}pez{-}{\'{U}}beda and Jos{\'{e}} Antonio Vera{-}Ramos and Pablo L{\'{o}}pez{-}Garc{\'{\i}}a},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2019 Precision Medicine - Medical University of Graz},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/imi\_mug.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lopez-UbedaVL19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring how to Combine Query Reformulations for Precision Medicine

_Giorgio Maria Di Nunzio, Stefano Marchesin, Maristella Agosti_

- :fontawesome-solid-user-group: **Participant:** [ims_unipd](./participants.md#ims_unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ims_unipd.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/ims_unipd.PM.pdf)
- :material-file-search: **Runs:** [BM25](./runs.md#bm25) | [BM25neop01](./runs.md#bm25neop01) | [BM25neopcomd](./runs.md#bm25neopcomd) | [BM25neopgngm](./runs.md#bm25neopgngm) | [top4fusion](./runs.md#top4fusion) | [BM25ct](./runs.md#bm25ct) | [BM25neop01r](./runs.md#bm25neop01r) | [BM25solid01o](./runs.md#bm25solid01o) | [BM25solid01r](./runs.md#bm25solid01r) | [top3fusion](./runs.md#top3fusion)

??? abstract "Abstract"
	
	We report on our participation as the IMS Unipd team in both TREC PM 2019 tasks. The objective of the work is twofold: (i) we want to evaluate how different query reformulations affect the results and whether the findings obtained in previous years remain valid; (ii) we want to verify if combining different query reformulations based on expansion and reduction techniques prove effective in such a highly specific scenario. In particular, we designed a procedure to (1) filter out clinical trials based on demographic data, (2) perform query reformulations - both expansion and reduction techniques - based on knowledge bases to increase the probability of findings relevant documents, (3) apply rank fusion techniques to the rankings produced by the different query reformulations. We consider those query reformulations that have been validated on previous TREC PM experimental collections. These queries represent the most effective reformulations for our system on those topics/collections. The results obtained - especially in the clinical trials task - validate our assumptions and provide interesting insights in terms of the different per-topic effectiveness of the query reformulations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NunzioMA19.bib) "
	```
	@inproceedings{DBLP:conf/trec/NunzioMA19,
		author = {Giorgio Maria Di Nunzio and Stefano Marchesin and Maristella Agosti},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Exploring how to Combine Query Reformulations for Precision Medicine},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ims\_unipd.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NunzioMA19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNC SILS at TREC 2019 Precision Medicine Track

_Jiaming Qu, Yue Wang_

- :fontawesome-solid-user-group: **Participant:** [UNC_SILS](./participants.md#unc_sils)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UNC_SILS.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/UNC_SILS.PM.pdf)
- :material-file-search: **Runs:** [sils_run1](./runs.md#sils_run1) | [sils_run2](./runs.md#sils_run2) | [sils_run3](./runs.md#sils_run3) | [sils_run4](./runs.md#sils_run4)

??? abstract "Abstract"
	
	This paper describes our participation in the scientific abstract retrieval task of TREC 2019 Precision Medicine Track. Our approach has two major components. First, we expand the original disease and gene terms using biomedical knowledge bases to improve recall of the initial retrieval. We then improve precision by promoting treatment-related publications to the top using a machine learning reranker trained on 2017 and 2018 relevance judgments combined. Batch evaluation results show that the proposed approach effectively improves P@10 compared to the baseline model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QuW19a.bib) "
	```
	@inproceedings{DBLP:conf/trec/QuW19a,
		author = {Jiaming Qu and Yue Wang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UNC} {SILS} at {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UNC\_SILS.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QuW19a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSIRO at 2019 TREC Precision Medicine Track

_Maciej Rybinski, Sarvnaz Karimi, Cécile Paris_

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CSIROmed.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/CSIROmed.PM.pdf)
- :material-file-search: **Runs:** [bm25_6801](./runs.md#bm25_6801) | [dfr_9464](./runs.md#dfr_9464) | [et_8435](./runs.md#et_8435) | [xgb_5113](./runs.md#xgb_5113) | [bm25_ct_25](./runs.md#bm25_ct_25) | [bm25_ct_f_61](./runs.md#bm25_ct_f_61) | [DFRInL2_f](./runs.md#dfrinl2_f) | [rf1_f_100](./runs.md#rf1_f_100) | [rf2_f_50](./runs.md#rf2_f_50)

??? abstract "Abstract"
	
	TREC Precision Medicine track focuses on search tasks tailored for oncologists. Given a cancer patient, the proposed systems must find clinical trials that match the patient, as well as the relevant information from biomedical literature (PubMed abstracts 2019 baseline). In our experiments, we compare BM25 and Divergence from Randomness (DFR) baselines and report results obtained with multiple learning-to-rank models. Some of our submitted runs score in top ten runs reported by the organisers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RybinskiKP19.bib) "
	```
	@inproceedings{DBLP:conf/trec/RybinskiKP19,
		author = {Maciej Rybinski and Sarvnaz Karimi and C{\'{e}}cile Paris},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CSIRO} at 2019 {TREC} Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CSIROmed.PM.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RybinskiKP19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieving Scientific Abstracts using Venue- and Concept-based Approaches:  CincyMedIR at TREC 2019 Precision Medicine Track

_Danny T. Y. Wu, Wu-Chen Su, James J. Lee_

- :fontawesome-solid-user-group: **Participant:** [CincyMedIR](./participants.md#cincymedir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/CincyMedIR.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/CincyMedIR.PM.pdf)
- :material-file-search: **Runs:** [MedIR5](./runs.md#medir5) | [MedIR4](./runs.md#medir4) | [MedIR3](./runs.md#medir3) | [MedIR2](./runs.md#medir2) | [MedIR1](./runs.md#medir1)

??? abstract "Abstract"
	
	The CincyMedIR group led by Dr. Danny T.Y. Wu at the University of Cincinnati (UC) College of Medicine participated in the Text Retrieval Conference 2019 Precision Medicine Track (TREC-PM). Dr. Wu was part of the MedIER group in TREC 2015, 2017, and 2018, and formed his own group this year. CincyMedIR only worked on the scientific abstracts but not clinical trial documents this year.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuSL19.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuSL19,
		author = {Danny T. Y. Wu and Wu{-}Chen Su and James J. Lee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Retrieving Scientific Abstracts using Venue- and Concept-based Approaches: CincyMedIR at {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/CincyMedIR.PM.pdf},
		timestamp = {Thu, 11 Nov 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuSL19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ECNU-ICA team at TREC 2019 Precision Medicine Track

_Qi Zheng, Yong Li, Jiaying Hu, Yan Yang, Liang He, Yi Xue_

- :fontawesome-solid-user-group: **Participant:** [ECNU-ICA](./participants.md#ecnu-ica)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ECNU_ICA.PM.pdf](https://trec.nist.gov/pubs/trec28/papers/ECNU_ICA.PM.pdf)
- :material-file-search: **Runs:** [clinic_base](./runs.md#clinic_base) | [clinic_ft](./runs.md#clinic_ft) | [cl_base_rr](./runs.md#cl_base_rr) | [cl_ft_agg](./runs.md#cl_ft_agg) | [cl_ft_rr](./runs.md#cl_ft_rr) | [sa_base](./runs.md#sa_base) | [sa_base_rr](./runs.md#sa_base_rr) | [sa_ft](./runs.md#sa_ft) | [sa_ft_rr](./runs.md#sa_ft_rr)

??? abstract "Abstract"
	
	In this paper, we describe our biomedical retrieval system used in TREC 2019 precision medicine track. Based on existing querying framework, we develop a multi-pass retrieval system to adaptively refine query template based on indexing feedback. After initial retrieval process, We further re-rank the retrieved documents using language model based re-ranker to get the final results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengLHYHX19.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengLHYHX19,
		author = {Qi Zheng and Yong Li and Jiaying Hu and Yan Yang and Liang He and Yi Xue},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ECNU-ICA} team at {TREC} 2019 Precision Medicine Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ECNU\_ICA.PM.pdf},
		timestamp = {Mon, 01 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengLHYHX19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

