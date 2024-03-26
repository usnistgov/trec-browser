# Proceedings - Clinical Trials 2021 

#### Alibaba DAMO Academy at TREC Clinical Trials 2021: ExploringEmbedding-based  First-stage Retrieval with TrialMatcher

_Qiao Jin, Chuanqi Tan, Zhengyun Zhao, Zheng Yuan, Songfang Huang_

- :fontawesome-solid-user-group: **Participant:** [ALIBABA](./participants.md#alibaba)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/ALIBABA_CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/ALIBABA_CAsT.pdf)
- :material-file-search: **Runs:** [damohitl](./runs.md#damohitl) | [damohitls](./runs.md#damohitls) | [damoebrtog](./runs.md#damoebrtog) | [damoebrsigir](./runs.md#damoebrsigir) | [damoebr](./runs.md#damoebr)

??? abstract "Abstract"
	
	This paper describes the submissions of Ailbaba DAMO Academy to the TREC 2021 Clinical Trials Track, where the task is to match eligible clinical trials for given patient notes. Our systems follow the standard retrieval-reranking procedure. We propose a novel embedding-based retrieval model, TrialMatcher, as the retriever. TrialMatcher contains a patient note encoder and a clinical trial encoder pre-trained by 370k clinical trial documents. It retrieves relevant clinical trials based on embedding space distances. We then use different re-rankers to reorder the candidates returned by Trial-Matcher. In automatic runs, the re-rankers are trained by a relevant dataset or a synthetic patient-trial relevance dataset. In manual runs, the re-rankers are trained by annotations derived from a human-in-the-loop active learning strategy. Our automatic runs rank the second in all participants on all four metrics. Our manual runs rank the first on one metric, and the second on three other metrics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001TZ0H21.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001TZ0H21,
		author = {Qiao Jin and Chuanqi Tan and Zhengyun Zhao and Zheng Yuan and Songfang Huang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Alibaba {DAMO} Academy at {TREC} Clinical Trials 2021: ExploringEmbedding-based First-stage Retrieval with TrialMatcher},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/ALIBABA\_CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001TZ0H21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM @ TREC Clinical Trials Track 2021

_Laura Biester, Venkata Joopudi, Bharath Dandala_

- :fontawesome-solid-user-group: **Participant:** [IBMResearch](./participants.md#ibmresearch)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IBMResearch-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/IBMResearch-CT.pdf)
- :material-file-search: **Runs:** [IBMLucene](./runs.md#ibmlucene) | [IBMSTS](./runs.md#ibmsts) | [IBMSIGIR](./runs.md#ibmsigir) | [IBMAUTOGT](./runs.md#ibmautogt) | [IBMSIGIRACT](./runs.md#ibmsigiract)

??? abstract "Abstract"
	
	Although clinical trials are crucial to the advancement of medical science, many clinical trials fail because they do not meet recruitment targets. This problem engenders a need for automated systems that can match patients to ongoing trials. The potential benefits of such systems are twofold: first, they would allow for the systematic study of new treatments through completed clinical trials and second, they could improve or even save the lives of patients for whom existing treatments are ineffective. We participate in the TREC Clinical Trials (CT) Track, for which the aim is to match synthetic 5-10 sentence patient descriptions with clinical trials from ClinicalTrials.gov, a clinical trials repository that includes all clinical trials in the United States. Our system uses BM25 and semantic textual similarity (STS) models to retrieve two thousand candidates from hundreds of thousands of clinical trials. We then proceed to rerank those trials using neural reranking models with BERT-based encoders and novel attention mechanisms. In addition to training our models on an existing related corpus [Koopman and Zuccon, 2016], we leverage data from MIMIC-III to generate a larger training corpus. In the end, we found that our BM25-based ranker utilizing a Lucene index outperformed our neural models, likely due to a lack of high-quality training data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BiesterJD21.bib) "
	```
	@inproceedings{DBLP:conf/trec/BiesterJD21,
		author = {Laura Biester and Venkata Joopudi and Bharath Dandala},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{IBM} @ {TREC} Clinical Trials Track 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IBMResearch-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BiesterJD21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SIB Text Mining at TREC Clinical Trials 2021

_Déborah Caucheteur, Emilie Pasche, Luc Mottin, Anaïs Mottaz, Julien Gobeill, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BITEM](./participants.md#bitem)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/BITEM-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/BITEM-CT.pdf)
- :material-file-search: **Runs:** [SIBTMct1](./runs.md#sibtmct1) | [SIBTMct2](./runs.md#sibtmct2) | [SIBTMct3](./runs.md#sibtmct3) | [SIBTMct4](./runs.md#sibtmct4) | [SIBTMct5](./runs.md#sibtmct5)

??? abstract "Abstract"
	
	TREC 2021 Clinical Trials Track aimed to develop algorithms to improve patient recruitment in clinical trials. These recruitment problems represent a real obstacle to medical research, leading to delays in clinical trial schedules and sometimes even to the termination of the trial due to the lack of eligible patients recruited. A set of 75 topics was distributed to participants. Each topic represents a patient's medical record, in other words a patient case description in free text format. In parallel, a set of clinical trials from ClinicalTrials.gov was also provided. The challenge was then to determine for each patient, if during a recruitment phase for a clinical trial from the corpus, the patient would be assessed as eligible, excluded or irrelevant. As an output, for each topic, our system returns a list of clinical trials ranked from the highest (relevant) score to the lowest within the limit of 1,000 results per topic. In total, five strategies were tested corresponding to the five runs submitted and will be described in this paper. The publication of the results at the TREC conference in November 2021 will indicate whether one of the strategies has proved more likely to deliver good results or whether, on the contrary, the work should be redirected towards new ideas.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaucheteurPMMGR21.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaucheteurPMMGR21,
		author = {D{\'{e}}borah Caucheteur and Emilie Pasche and Luc Mottin and Ana{\"{\i}}s Mottaz and Julien Gobeill and Patrick Ruch},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{SIB} Text Mining at {TREC} Clinical Trials 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/BITEM-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CaucheteurPMMGR21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pozna'n Contribution to TREC Clinical Trials 2021⋆

_Jakub Dutkiewicz, Czeslaw Jedrzejek_

- :fontawesome-solid-user-group: **Participant:** [POZNAN](./participants.md#poznan)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/POZNAN-PM.pdf](https://trec.nist.gov/pubs/trec30/papers/POZNAN-PM.pdf)
- :material-file-search: **Runs:** [pozAbbrMesh](./runs.md#pozabbrmesh) | [pozAddTerms](./runs.md#pozaddterms) | [pozFulltext](./runs.md#pozfulltext) | [pozMeshTerms](./runs.md#pozmeshterms) | [pozTermFds](./runs.md#poztermfds)

??? abstract "Abstract"
	
	In this papaer we go over our approach to TREC Clinical Trials 2021. We discuss the architecture of our retrieval system. Specifically, we describe the used topic processing techniques. We recount the structure of a document and our methods of interpreting and extracting data from the document. This paper also covers the description of experiments we proposed for TREC Clinical Trials 2021. We conclude with a brief discussion of the obtained results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DutkiewiczJ21.bib) "
	```
	@inproceedings{DBLP:conf/trec/DutkiewiczJ21,
		author = {Jakub Dutkiewicz and Czeslaw Jedrzejek},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Pozna'n Contribution to {TREC} Clinical Trials 2021{\(\star\)}},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/POZNAN-PM.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DutkiewiczJ21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An approach to relevant clinical trials retrieving

_Mariia Fedorova_

- :fontawesome-solid-user-group: **Participant:** [clinical_trials](./participants.md#clinical_trials)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/clinical_trials-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/clinical_trials-CT.pdf)
- :material-file-search: **Runs:** [RUN0](./runs.md#run0) | [RUN1FREQS](./runs.md#run1freqs) | [RUN3SENTS](./runs.md#run3sents)

??? abstract "Abstract"
	
	In this notebook paper an approach to retrieving relevant clinical trials for patients' unstructured descriptions (electronic health records, EHTs) is described.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Fedorova21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Fedorova21,
		author = {Mariia Fedorova},
		editor = {Ian Soboroff and Angela Ellis},
		title = {An approach to relevant clinical trials retrieving},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/clinical\_trials-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Fedorova21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2021⋆ Clinical Trials Retrieval, Duisburg-Essen University  submission

_Sameh Frihat, Norbert Fuhr_

- :fontawesome-solid-user-group: **Participant:** [IRUniDUE](./participants.md#irunidue)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IRUniDUE-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/IRUniDUE-CT.pdf)
- :material-file-search: **Runs:** [first_run](./runs.md#first_run) | [second_run](./runs.md#second_run) | [third_run](./runs.md#third_run) | [fourth_run](./runs.md#fourth_run) | [fifth_run](./runs.md#fifth_run)

??? abstract "Abstract"
	
	Clinical trials are human research studies that aim to evaluate a medical, surgical, or behavioral intervention that is critical to the advancement of medical science. The majority of clinical trials fail because recruitment goals are not met. This issue necessitates the incorporation of automated systems capable of matching patients to ongoing clinical trials. This paper summarizes our participation in the TREC 2021 clinical trials track, which provided all participants with a 5-10 sentence patient description and a clinical trials database from ClinicalTrials.gov for matching. Our submission consists of a variety of retrieval techniques, including BM25, entity recognition, BERT, and others. The results show that a simple BM25 ranking algorithm could outperform neural network-based models, mainly due to the absence of quality training data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FrihatF21.bib) "
	```
	@inproceedings{DBLP:conf/trec/FrihatF21,
		author = {Sameh Frihat and Norbert Fuhr},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC} 2021{\(\star\)} Clinical Trials Retrieval, Duisburg-Essen University submission},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IRUniDUE-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FrihatF21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Clinical Trial Search Using Lucene and UMLS

_Yanqing Ji, Yun Tian, Hao Ying, John Tran_

- :fontawesome-solid-user-group: **Participant:** [GU_BioMed](./participants.md#gu_biomed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/GU_BioMed-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/GU_BioMed-CT.pdf)
- :material-file-search: **Runs:** [TxtInc](./runs.md#txtinc) | [TxtIncExc](./runs.md#txtincexc) | [CuiInc](./runs.md#cuiinc) | [TxtIncExcExp](./runs.md#txtincexcexp) | [CuiIncExc](./runs.md#cuiincexc)

??? abstract "Abstract"
	
	We approached the clinical trial search task of the 2021 TREC Clinical Trials Track as a query problem. A query (also known as a topic in 2021 TREC) is the free text description of a patient record, while the corpus is a large set of clinical trials descriptions. A commercial search engine, Lucene, was utilized for this clinical trial matching process. Namely, given a query, the system searches in the corpus and returns a subset of clinical trials with specific requirements. In this study, Unified Medical Language System (UMLS) was employed to convert the free text of both topics and clinical trials to more meaningful biomedical concepts, each of which is represented as a Concept Unique Identifier (CUI). An expansion technique based on Medical Subject Headings (MeSH) was used to expand all the condition terms for each clinical trial to their child terms. To assess whether UMLS can improve the search accuracy, we designed two groups of tests: one group uses free text, while the other uses CUIs for both queries and clinical trial corpuses. As the inclusion/exclusion criteria represent the core aspect of each trial description, we also examined whether the exclusion criteria played an important role in the process of selecting a clinical trial. We extracted the inclusion criteria and exclusion criteria for each clinical study and saved them into two separate corpuses. For each group of tests, we searched against the corpus with inclusion criteria only and also against both corpuses. When searching in both corpuses, for each query (i.e. a patient profile), the search results were sorted using the difference of the two Lucene scores that were returned when searching against the two corpuses, respectively. For the free text group, we also tested whether the expansion technique could improve the performance. Our experiment results demonstrated that the CUI-based search clearly outperformed the text-based search, which indicated the effectiveness of UMLS in text preprocessing and biomedical concept extraction. Our methods of using the exclusion criteria information and the MeSH-based term expansion technique were not as effective as we expected.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiTYT21.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiTYT21,
		author = {Yanqing Ji and Yun Tian and Hao Ying and John Tran},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Clinical Trial Search Using Lucene and {UMLS}},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/GU\_BioMed-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JiTYT21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2021 Clinical Trials Submission for Universidad del País  Vasco

_Jordan Koontz, Maite Oronoz, Alicia Pérez_

- :fontawesome-solid-user-group: **Participant:** [uni_pais_vasco](./participants.md#uni_pais_vasco)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/uni_pais_vasco-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/uni_pais_vasco-CT.pdf)
- :material-file-search: **Runs:** [LaBSE](./runs.md#labse) | [specter](./runs.md#specter) | [LaBSE_rerank](./runs.md#labse_rerank) | [spect_rerank](./runs.md#spect_rerank) | [spec_rrk_fqv](./runs.md#spec_rrk_fqv)

??? abstract "Abstract"
	
	This paper describes the University of the Basque Country's submission to the TREC 2021 Clinical Trials Track. We begin by summarizing the documents by extracting medical entities. Next, we utilize multi-lingual and scientific domain sentence embeddings to represent the summarized clinical trials descriptions and the patient topic documents. Lastly, we rank the clinical trial relevance by calculating the cosine similarities between texts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoontzOP21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoontzOP21,
		author = {Jordan Koontz and Maite Oronoz and Alicia P{\'{e}}rez},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC} 2021 Clinical Trials Submission for Universidad del Pa{\'{\i}}s Vasco},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/uni\_pais\_vasco-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KoontzOP21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DOSSIER at TREC 2021 Clinical Trials Track

_Wojciech Kusa, Yasin Ghafourian_

- :fontawesome-solid-user-group: **Participant:** [DOSSIER](./participants.md#dossier)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/DOSSIER-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/DOSSIER-CT.pdf)
- :material-file-search: **Runs:** [baseline](./runs.md#baseline) | [postproc](./runs.md#postproc) | [rerank2000](./runs.md#rerank2000)

??? abstract "Abstract"
	
	This paper describes our experimental setup and results for the Clinical Trials Track at TREC 2021. In particular, we study (i) the effectiveness of post-processing with patients' metadata and (ii) the novel re-ranking formula using eligibility criteria. We find that the post-processing improves the model over the baseline run. However, the custom re-ranking negatively impacts average results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KusaG21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KusaG21,
		author = {Wojciech Kusa and Yasin Ghafourian},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{DOSSIER} at {TREC} 2021 Clinical Trials Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/DOSSIER-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KusaG21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNTIIA Lab at TREC 2021 - Clinical Trial

_Huyen Nguyen, Haihua Chen, Bhanu Prasad, Huanhuan Zhao, Junhua Ding, Jiangping Chen, Ana D. Cleveland_

- :fontawesome-solid-user-group: **Participant:** [UNTIIA](./participants.md#untiia)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UNTIIA-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/UNTIIA-CT.pdf)
- :material-file-search: **Runs:** [UNTIIARUN1](./runs.md#untiiarun1) | [UNTIIARUN2](./runs.md#untiiarun2) | [UNTIIARUN3](./runs.md#untiiarun3) | [UNTIIARUN4](./runs.md#untiiarun4) | [UNTIIARUN5](./runs.md#untiiarun5)

??? abstract "Abstract"
	
	This paper reports our participation in 2021 TREC Clinical Trial (CT) track based on the ElasticSearch information retrieval platform. We studied different query extraction and query expansion methods with both manual and automatic strategies for query construction. Our experiments on the 2016 Clinical Decision Support collection proved the effectiveness of the knowledge base mapping method for both query extraction and expansion. We proposed a novel query construction strategy to balance precision and accuracy: we retrieve clinical trials documents with a complete list of query terms first and then decrease the number of query terms used for searching additional documents to improve recall. We also investigated two transformer-based models for reranking: unsupervised and supervised learning. Pairs of query and candidate documents were encoded with the sentence-BERT in the unsupervised reranking model, and then their semantic similarity was compared using a Cross-encoder model. We also took advantage of BERT transformers for the supervised reranking model by finetuning the model on the ground truth of the 2016 Clinical Decision Support collection and then feeding it into the TFR-BERT model for reranking. Our experiment indicates that the unsupervised transformer reranking model outperformed the supervised learning model and achieved the highest performance among teams on a number of topics
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Nguyen0PZDCC21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Nguyen0PZDCC21,
		author = {Huyen Nguyen and Haihua Chen and Bhanu Prasad and Huanhuan Zhao and Junhua Ding and Jiangping Chen and Ana D. Cleveland},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{UNTIIA} Lab at {TREC} 2021 - Clinical Trial},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UNTIIA-CT.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Nguyen0PZDCC21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filter, Transform, Expand, and Fuse The IMS Unipd at TREC 2021  Clinical Trials

_Giorgio Maria Di Nunzio, Guglielmo Faggioli, Stefano Marchesin_

- :fontawesome-solid-user-group: **Participant:** [ims_unipd](./participants.md#ims_unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/ims_unipd-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/ims_unipd-CT.pdf)
- :material-file-search: **Runs:** [RM3Filtered](./runs.md#rm3filtered) | [BARTRM3Filt](./runs.md#bartrm3filt) | [T5RM3Filt](./runs.md#t5rm3filt) | [imsFused1](./runs.md#imsfused1) | [imsFused2](./runs.md#imsfused2)

??? abstract "Abstract"
	
	We present the methodology and the experimental setting of the participation of the IMS Unipd team in TREC Clinical Trials 2021. The objective of this work is to continue the longitudinal study of the evaluation of query expansion, ranking fusion, and document filtering approach optimized in the previous participation to TREC. In particular, we added to our procedure proposed in 2020, a comparison with a pipeline that use the large transformers. The results obtained provide interesting insights in terms of the different per-topic effectiveness and will be used for further failure analyses.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NunzioF021.bib) "
	```
	@inproceedings{DBLP:conf/trec/NunzioF021,
		author = {Giorgio Maria Di Nunzio and Guglielmo Faggioli and Stefano Marchesin},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Filter, Transform, Expand, and Fuse The {IMS} Unipd at {TREC} 2021 Clinical Trials},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/ims\_unipd-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NunzioF021.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNIMIB at TREC 2021 Clinical Trials Track

_Georgios Peikos, Oscar Espitia, Gabriella Pasi_

- :fontawesome-solid-user-group: **Participant:** [UNIMIB](./participants.md#unimib)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UNIMIB-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/UNIMIB-CT.pdf)
- :material-file-search: **Runs:** [UNM_5](./runs.md#unm_5) | [UNM_4](./runs.md#unm_4) | [IKR3_BSL](./runs.md#ikr3_bsl) | [IKR3_TT_MW_k](./runs.md#ikr3_tt_mw_k) | [IKR3_TT_MW_d](./runs.md#ikr3_tt_mw_d)

??? abstract "Abstract"
	
	This contribution summarizes the participation of the UNIMIB team to the TREC 2021 Clinical Trials Track. We have investigated the effect of different query representations combined with several retrieval models on the retrieval performance. First, we have implemented a neural re-ranking approach to study the effectiveness of dense text representations. Additionally, we have investigated the effectiveness of a novel decision-theoretic model for relevance estimation. Finally, both of the above relevance models have been compared with standard retrieval approaches. In particular, we combined a keyword extraction method with a standard retrieval process based on the BM25 model and a decision-theoretic relevance model that exploits the characteristics of this particular search task. The obtained results show that the proposed keyword extraction method improves 84% of the queries over the TREC's median NDCG@10 measure when combined with either traditional or decision-theoretic relevance models. Moreover, regarding RPEC@10, the employed decision-theoretic model improves 85% of the queries over the reported TREC's median value.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PeikosEP21.bib) "
	```
	@inproceedings{DBLP:conf/trec/PeikosEP21,
		author = {Georgios Peikos and Oscar Espitia and Gabriella Pasi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{UNIMIB} at {TREC} 2021 Clinical Trials Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UNIMIB-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PeikosEP21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSIROmed Team Report of TREC 2021 Clinical Trials track: Experiments  with BERT Reranking Methods

_Maciej Rybinski, Vincent Nguyen, Sarvnaz Karimi_

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CSIROmed-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/CSIROmed-CT.pdf)
- :material-file-search: **Runs:** [CSIROmed_abs](./runs.md#csiromed_abs) | [CSIROmed_inc](./runs.md#csiromed_inc) | [CSIROmed_DCT](./runs.md#csiromed_dct) | [CSIROmedNIR](./runs.md#csiromednir) | [CSIROmed_brd](./runs.md#csiromed_brd)

??? abstract "Abstract"
	
	A large body of clinical trials fail to attract enough eligible participants. TREC 2021 Clinical Trials track set a task to use patient data in the form of clinical notes as a way to identify patients eligible for clinical trials. We explore a number of reranking methods as well as query rewighting using Bidi- rectional Encoder Representations from Transformers (BERT). Our best method used BERT reranking trained on scientific literature.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RybinskiNK21.bib) "
	```
	@inproceedings{DBLP:conf/trec/RybinskiNK21,
		author = {Maciej Rybinski and Vincent Nguyen and Sarvnaz Karimi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {CSIROmed Team Report of {TREC} 2021 Clinical Trials track: Experiments with {BERT} Reranking Methods},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CSIROmed-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RybinskiNK21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WisPerMed Text at TREC Clinical Trials Track 2021

_Henning Schäfer, Ahmad Idrissi-Yaghir, Wolfgang Galetzka, Marie Bexte, Christoph M. Friedrich_

- :fontawesome-solid-user-group: **Participant:** [wispermedtxt](./participants.md#wispermedtxt)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/wispermedtxt-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/wispermedtxt-CT.pdf)
- :material-file-search: **Runs:** [wpm_biobert](./runs.md#wpm_biobert) | [wpm_CBert](./runs.md#wpm_cbert) | [wpm_KWBM25](./runs.md#wpm_kwbm25) | [wpm_bmre](./runs.md#wpm_bmre) | [wpm_critumls](./runs.md#wpm_critumls)

??? abstract "Abstract"
	
	This paper describes the submissions of the WisPerMed Text group to the TREC Clinical Trials Track 2021. It aims to overcome the problems in patient recruitment that often lead to delays or even discontinuation of clinical trials. The focus here is finding methods to improve the process of matching patient case descriptions to eligible clinical trials. For this purpose, different systems were proposed and tested to rank the trials for each patient topic. These systems utilize methods such as transformer-based models, BM25 and keyword extraction. Additionally, Unified Medical Language System (UMLS) was used in an attempt to find relevancy between patient topics and clinical trials based on biomedical concepts. The results obtained showed that the BM25 model based on keyword extraction performed the best out of all our submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchaferIFGFB21.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchaferIFGFB21,
		author = {Henning Sch{\"{a}}fer and Ahmad Idrissi{-}Yaghir and Wolfgang Galetzka and Marie Bexte and Christoph M. Friedrich},
		editor = {Ian Soboroff and Angela Ellis},
		title = {WisPerMed Text at {TREC} Clinical Trials Track 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/wispermedtxt-CT.pdf},
		timestamp = {Fri, 15 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SchaferIFGFB21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ITTC @ TREC 2021 Clinical Trials Track

_Hung-Thinh Truong, Yulia Otmakhova, Timothy Baldwin, Jey Han Lau, Trevor Cohn, Karin Verspoor, Rahmad Mahendra, Lawrence Cavedon, Damiano Spina_

- :fontawesome-solid-user-group: **Participant:** [ITTC-AIMedTech](./participants.md#ittc-aimedtech)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/ITTC-AIMedTech-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/ITTC-AIMedTech-CT.pdf)
- :material-file-search: **Runs:** [ittc1](./runs.md#ittc1) | [ittc2](./runs.md#ittc2) | [ittc3](./runs.md#ittc3) | [ittc4](./runs.md#ittc4) | [ittc5](./runs.md#ittc5)

??? abstract "Abstract"
	
	This paper describes the submissions of the Natural Language Processing (NLP) team from the Australian Research Council Industrial Transformation Training Centre (ITTC) for Cognitive Computing in Medical Technolo- gies to the TREC 2021 Clinical Trials Track. The task focuses on the problem of matching eligible clinical trials to topics constituting a summary of a patient's admission notes. We explore different ways of representing trials and topics using NLP techniques, and then use a common retrieval model to generate the ranked list of relevant trials for each topic. The results from all our submitted runs are well above the median scores for all topics, but there is still plenty of scope for improvement.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Truong0BLCVMCS21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Truong0BLCVMCS21,
		author = {Hung{-}Thinh Truong and Yulia Otmakhova and Timothy Baldwin and Jey Han Lau and Trevor Cohn and Karin Verspoor and Rahmad Mahendra and Lawrence Cavedon and Damiano Spina},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{ITTC} @ {TREC} 2021 Clinical Trials Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/ITTC-AIMedTech-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Truong0BLCVMCS21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CincyMedIR at TREC 2021 Clinical Trial Track

_Hoang Vu, Danny T. Y. Wu_

- :fontawesome-solid-user-group: **Participant:** [CincyMedIR](./participants.md#cincymedir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CincyMedIR-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/CincyMedIR-CT.pdf)
- :material-file-search: **Runs:** [CincyMedIR_1](./runs.md#cincymedir_1) | [CincyMedIR_2](./runs.md#cincymedir_2) | [CincyMedIR_3](./runs.md#cincymedir_3) | [CincyMedIR_4](./runs.md#cincymedir_4) | [CincyMedIR_5](./runs.md#cincymedir_5)

??? abstract "Abstract"
	
	The CincyMedIR team led by Dr. Danny T.Y. Wu at the University of Cincinnati College of Medicine participated in the Text Retrieval Conference 2021 Clinical Trials Track (TREC-CT). This year, we applied our existing text-retrieval methods from our previous TREC tracks on the new Clinical Trials track while also experimenting with new techniques to process the trial exclusion criteria.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VuW21.bib) "
	```
	@inproceedings{DBLP:conf/trec/VuW21,
		author = {Hoang Vu and Danny T. Y. Wu},
		editor = {Ian Soboroff and Angela Ellis},
		title = {CincyMedIR at {TREC} 2021 Clinical Trial Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CincyMedIR-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/VuW21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Application of Traditional IE as a Non-traditional Method in  an IR Task: TDMINER at 2021 TREC Clinical Trials

_Chengyi Zheng_

- :fontawesome-solid-user-group: **Participant:** [TDMINER](./participants.md#tdminer)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/TDMINER-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/TDMINER-CT.pdf)
- :material-file-search: **Runs:** [tdminerrun1](./runs.md#tdminerrun1) | [tdminerrun2](./runs.md#tdminerrun2) | [tdminerrun3](./runs.md#tdminerrun3) | [tdminerrun4](./runs.md#tdminerrun4)

??? abstract "Abstract"
	
	The 2021 TREC Clinical Trials (CT) task focused on finding appropriate trials based on the health profiles of individual patients. This notebook details our participation in the 2021 TREC CT. In this paper, we presented the findings of our first participation in the TREC task. The TREC Clinical Trials (CT) goal for 2021 was to discover appropriate trials based on the health characteristics of individual patients. This notebook details our participation in the TREC CT in 2021 (team TDMINER). We presented the findings of our initial participation in the TREC task in this publication. Traditional information retrieval approaches, such as Elasticsearch with BM25 or DFR with query expansion, and machine learning-based rerankers, such as BERT, were used in previous efforts. Unlike these methods, we concentrated on developing an IE-based baseline that could be utilized as a starting point for future research. As part of our two-stage IR process, we implemented a basic weight-scaled reranking method. We submitted our results in the manual run category since we manually reranked the IE-identified concepts for each topic. There were 26 teams in total, with 101 automatic runs and 12 manual runs submitted. In terms of NDCG@10, PREC@10, and mean reciprocal rank (MRR), we achieved final ranking scores of 0.715, 0.576, and 0.834, respectively. In manual runs, the averaged median scores for these assessment criteria were 0.621, 0.457, and 0.721; in automatic runs, 0.304, 0.161, and 0.294. Our system ranked first on the NDCG@10 and MRR, second on the PREC@10 among all the submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Zheng21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Zheng21,
		author = {Chengyi Zheng},
		editor = {Ian Soboroff and Angela Ellis},
		title = {The Application of Traditional {IE} as a Non-traditional Method in an {IR} Task: {TDMINER} at 2021 {TREC} Clinical Trials},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/TDMINER-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Zheng21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

