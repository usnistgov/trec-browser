# Proceedings - Clinical Trials 2022 

#### Overview of the TREC 2022 Clinical Trials Track

_Kirk Roberts, Dina Demner-Fushman, Ellen M. Voorhees, Steven Bedrick, William R. Hersh_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Overview_trials.pdf](https://trec.nist.gov/pubs/trec31/papers/Overview_trials.pdf)
??? abstract "Abstract"
	
	Clinical trials are the primary means for new medical treatments-such as drugs, surgical procedures, and behavior interventions-to demonstrate their effectiveness in an evidence-based manner. However, clinical trials have high costs, can take years to complete, and oftentimes fail to identify a sufficient number of patients to establish clinical significance. Automated methods for improving the patient recruitment process can aid in all three areas: reducing manual and expensive chart review, more quickly identifying eligible patients, and expanding the pool of candidate patients that may be eligible. The primary means of automating clinical trial recruitment is through the use of electronic health record (EHR) data. EHRs are responsible for documenting routine medical care, as well as being the legal and billing record. However, the re-use of EHR data for research is well-established (Hersh, 2007), commonly for observational studies but also as the source data for informatics-driven models, including machine learning (ML) and information retrieval (IR). This was the inspiration behind the TREC Medical Records track (2011-2012) (Voorhees and Tong, 2011; Voorhees and Hersh, 2012), which used short cohort descriptions as queries (e.g., “Patients treated for vascular claudication surgically”) and used EHR visit records as the document collection. Unfortunately, this track was discontinued due to the the lack of an EHR dataset of sufficient size to merit a proper IR evaluation. The TREC Clinical Trials track, instead, flips the trial-to-patients paradigm to a patient-to-trials paradigm. This has enabled the building of a large test collection for clinical trial search. In this paradigm, the topic is a (synthetic) patient description and the document collection is a large set of clinical trial descriptions (which are, notably, publicly and freely available). There are several challenges involved with task, however. The first set of challenges revolve around using clinical trial descriptions as the document collection. Clinical trial descriptions are often very long (see link to trial in Table 2). The core part of the description with regards to trial matching is the eligibility criteria, a (often long) list of inclusion criteria (the patient must meet all these requirements) and exclusion criteria (if the patient meets any of these criteria, they are ineligible and would be excluded from the trial). These criteria not only use complex medical terminology, but they are often written in a way that does not correspond directly to how patient cases are described in the EHR, making direct term mapping problematic. The second set of challenges revolves around the patient cases. In addition to the linguistic issues of how identical clinical concepts in EHR text versus trial descriptions, patient cases contain significant amounts of extraneous information with respect to the clinical trial. That is, not all of the information in a patient case need be covered in the trial. Rather, a sufficient amount of information must be present to suggest the patient may be eligible, while also not containing information showing the patient to be excluded. This means that many of the conditions in the patient description are irrelevant for a single clinical trial, whereas matching to a different clinical trial may involve a different subset of conditions in the patient case. As in 2021 Roberts et al. (2021b), to ensure this task focuses on information retrieval and not supervised information extraction, we present a lengthy (5-10 sentence) patient case description as the topic that simulates an admission statement in an EHR. The evaluation is further be broken down into Eligible, Excludes, and Not Relevant to allow retrieval methods to distinguish between patients that do not have sufficient information to qualify for the trial (Not Relevant) and those that are explicitly Excluded. This latter category can be difficult for retrieval systems without strong semantic understanding.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsDVBH22.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsDVBH22,
		author = {Kirk Roberts and Dina Demner{-}Fushman and Ellen M. Voorhees and Steven Bedrick and William R. Hersh},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2022 Clinical Trials Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Overview\_trials.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RobertsDVBH22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Matching a Patient from An Admission Note to Clinical Trials: Experiments  with Query Generation and Neural-Ranking

_Vincent Nguyen, Maciej Rybinski, Sarvnaz Karimi_

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CSIROmed.T.pdf](https://trec.nist.gov/pubs/trec31/papers/CSIROmed.T.pdf)
- :material-file-search: **Runs:** [doct5query](./runs.md#doct5query) | [CSIROmedANIR](./runs.md#csiromedanir) | [ANIR_demo](./runs.md#anir_demo) | [zs_bert_500](./runs.md#zs_bert_500) | [monobert500](./runs.md#monobert500)

??? abstract "Abstract"
	
	Many clinical trials fail to attract enough eligible participants. The TREC 2022 Clinical Trials track set a task where patient data, in the form of clinical notes, can be used to match eligible patients to a relevant clinical trial. We explore a number of dense retrieval methods using Bidirectional Encoder Representations from Transformers (BERT). Our best method used BERT reranking using models based on monoBERT architecture. Our self-supervised monoBERT run achieved effectiveness competitive to that of a fully-tuned monoBERT run.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NguyenRK22.bib) "
	```
	@inproceedings{DBLP:conf/trec/NguyenRK22,
		author = {Vincent Nguyen and Maciej Rybinski and Sarvnaz Karimi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Matching a Patient from An Admission Note to Clinical Trials: Experiments with Query Generation and Neural-Ranking},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CSIROmed.T.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NguyenRK22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNIMIB at TREC 2022 Clinical Trials Track

_Georgios Peikos, Gabriella Pasi_

- :fontawesome-solid-user-group: **Participant:** [UNIMIB](./participants.md#unimib)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UNIMIB.T.pdf](https://trec.nist.gov/pubs/trec31/papers/UNIMIB.T.pdf)
- :material-file-search: **Runs:** [IKR3_BSL](./runs.md#ikr3_bsl) | [IKR3_TT_MW](./runs.md#ikr3_tt_mw) | [IKR3_TT_BW](./runs.md#ikr3_tt_bw) | [IKR3_BSL_TT_HW](./runs.md#ikr3_bsl_tt_hw) | [IKR3_BSL_TT_MW](./runs.md#ikr3_bsl_tt_mw)

??? abstract "Abstract"
	
	This notebook summarizes our participation as the UNIMIB team in the TREC 2022 Clinical Trials Track. In this work, we extend our last year's participation by further investigating the retrieval performance achieved by our decision-theoretic model for relevance estimation. Specifically, our objective was to investigate the effectiveness of our decision-theoretic model by heavily penalizing those clinical trials for which the patient has high topical similarity to the exclusion criteria. The model has been employed to estimate relevance in two retrieval settings, ranking and re-ranking. The obtained results showed that the proposed model performs equally well in both of them, while the best results in terms of precision were achieved in the re-ranking setting.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PeikosP22.bib) "
	```
	@inproceedings{DBLP:conf/trec/PeikosP22,
		author = {Georgios Peikos and Gabriella Pasi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{UNIMIB} at {TREC} 2022 Clinical Trials Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UNIMIB.T.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PeikosP22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Elsevier Data Science Health Sciences at TREC 2022 Clinical Trials:  Exploring Transformer Embeddings for Clinical Trial Retrieval

_Drahomira Herrmannova, Sharvari Jadhav, Harsh Sindhwa, Hina Nazir, Elia Lima-Walton_

- :fontawesome-solid-user-group: **Participant:** [els_dshs](./participants.md#els_dshs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/els_dshs.T.pdf](https://trec.nist.gov/pubs/trec31/papers/els_dshs.T.pdf)
- :material-file-search: **Runs:** [senttr](./runs.md#senttr) | [bm25_bi_filtered](./runs.md#bm25_bi_filtered) | [bm25_st_bienc](./runs.md#bm25_st_bienc) | [st_distilbert](./runs.md#st_distilbert)

??? abstract "Abstract"
	
	In this paper, we describe the submissions of Elsevier Data Science Health Sciences to the TREC 2022 Clinical Trials Track. Our submissions explored the applicability of transformer embeddings to the task and demonstrated a straightforward retriever using the MiniLM model can achieve competitive performance. Additionally, we share observations from a manual evaluation we performed to better understand the performance of our embedding-based retrievers
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HerrmannovaJSNL22.bib) "
	```
	@inproceedings{DBLP:conf/trec/HerrmannovaJSNL22,
		author = {Drahomira Herrmannova and Sharvari Jadhav and Harsh Sindhwa and Hina Nazir and Elia Lima{-}Walton},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Elsevier Data Science Health Sciences at {TREC} 2022 Clinical Trials: Exploring Transformer Embeddings for Clinical Trial Retrieval},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/els\_dshs.T.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HerrmannovaJSNL22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Summarize and Expand Queries in Clinical Trials Retrieval. The IIIA  Unipd at TREC 2022 Clinical Trials

_Giorgio Maria Di Nunzio, Guglielmo Faggioli, Stefano Marchesin_

- :fontawesome-solid-user-group: **Participant:** [iiia-unipd](./participants.md#iiia-unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/iiia-unipd.T.pdf](https://trec.nist.gov/pubs/trec31/papers/iiia-unipd.T.pdf)
- :material-file-search: **Runs:** [ims_BM25Filtered_s](./runs.md#ims_bm25filtered_s) | [ims_BM25Filtered_kw](./runs.md#ims_bm25filtered_kw) | [ims_RM3Filtered_kw](./runs.md#ims_rm3filtered_kw) | [ims_RM3Filtered_s](./runs.md#ims_rm3filtered_s) | [ims_T5summarizer](./runs.md#ims_t5summarizer)

??? abstract "Abstract"
	
	We present the methodology and the experimental setting we, the Intelligent Interactive Information Access (IIIA)1 UNIPD team, used in the TREC Clinical Trials 2022. This work continues the long streak of studies we carried out at TREC Precision Medicine to evaluate the effectiveness of query reformulation, pseudo-relevance feedback, and document filtering. Compared to the procedure proposed in 2021, we introduced the use of manual summarization and removed rank fusion. The obtained results provide interesting insights on the different per-topic effectiveness and will be used for further analyses.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NunzioF022.bib) "
	```
	@inproceedings{DBLP:conf/trec/NunzioF022,
		author = {Giorgio Maria Di Nunzio and Guglielmo Faggioli and Stefano Marchesin},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Summarize and Expand Queries in Clinical Trials Retrieval. The {IIIA} Unipd at {TREC} 2022 Clinical Trials},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/iiia-unipd.T.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NunzioF022.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JBNU at TREC 2022 Clinical Trials Track

_Dalya Sin, Woo-Kyoung Lee, Seung-Hyeon Jo, Kyung-Soon Lee_

- :fontawesome-solid-user-group: **Participant:** [jbnu](./participants.md#jbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/jbnu.T.pdf](https://trec.nist.gov/pubs/trec31/papers/jbnu.T.pdf)
- :material-file-search: **Runs:** [jbnu1](./runs.md#jbnu1) | [jbnu2](./runs.md#jbnu2)

??? abstract "Abstract"
	
	This paper describes the participation of the JBNU team at the TREC 2022 Clinical Trials Track. Our approach is to focus on clinical terms detected from the ClinicalBERT and BioBERT. In order to expand clinical terms, the synonym terms are extracted by BERT embedding model. Our experimental results showed 0.4527, 0.3220 and 0.5543 by NDCG@10, P@10 and MRR, respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinLJL22.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinLJL22,
		author = {Dalya Sin and Woo{-}Kyoung Lee and Seung{-}Hyeon Jo and Kyung{-}Soon Lee},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{JBNU} at {TREC} 2022 Clinical Trials Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/jbnu.T.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SinLJL22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CogStack Cohort at TREC 2022 Clinical Trials Track

_Jack Wu, Zeljko Kraljevic, Thomas Searle, Daniel Bean, Richard J. B. Dobson_

- :fontawesome-solid-user-group: **Participant:** [phi_lab](./participants.md#phi_lab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/phi_lab.T.pdf](https://trec.nist.gov/pubs/trec31/papers/phi_lab.T.pdf)
- :material-file-search: **Runs:** [phir1m1](./runs.md#phir1m1) | [phir2m2](./runs.md#phir2m2) | [phir3m1prf](./runs.md#phir3m1prf) | [phir4m1prf2](./runs.md#phir4m1prf2) | [phir5m2prf](./runs.md#phir5m2prf)

??? abstract "Abstract"
	
	This notebook paper describes the methodology used to produce the retrieval results we submitted for TREC 2022 Clinical Trials Track. The method is based on named entity recognition and linking (NER+L). Medical Concept Annotation Tool (MedCAT) is used to perform NER+L on the topics and documents to produce entities in the SNOMED Clinical Terms ontology. The clinical terms extracted by the annotation process are used for indexing and retrieval purposes. The retrieval model used is a passage-based retrieval model that gives different weights to different document portions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuKSBD22.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuKSBD22,
		author = {Jack Wu and Zeljko Kraljevic and Thomas Searle and Daniel Bean and Richard J. B. Dobson},
		editor = {Ian Soboroff and Angela Ellis},
		title = {CogStack Cohort at {TREC} 2022 Clinical Trials Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/phi\_lab.T.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WuKSBD22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Hybrid Re-ranking for Biomedical Information Retrieval at the TREC  2021 Clinical Trials Track

_Ming-Xuan Shi, Tsung-Hsuan Pan, Hsin-Hsi Chen, Hen-Hsen Huang_

- :fontawesome-solid-user-group: **Participant:** [NTU_NLP](./participants.md#ntu_nlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/NTU_NLP-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/NTU_NLP-CT.pdf)

??? abstract "Abstract"
	
	This paper presents our methodology for the task of TREC 2021 Clinical Trials Track, which requires a system to retrieve and return the most relevant biomedical articles after giving queries. We propose a novel approach to biomedical information retrieval by leveraging the term-based and the embedding-based retrieval models with a re-ranking strategy. In our hybrid framework, all the documents will be indexed by using a term-based, efficient search engine. For the given query, a smaller set of candidate results are retrieved from the search engine. The ranking is determined not only by the term-based ranking score but also by the term relationships labeled by the Amazon Comprehend service1 for refinement. Then, the candidate results are further scored by using the embedding-based model. We represent the document and the query with bioBERT and compute the cosine similarity between a pair of the document embedding and the query embedding as their relevance score. The final score is a linear combination of the term-based and the embedding-based scores. Experimental results show that our hybrid re-ranking method improves both Precision@k and R-precision scores on the 2016 Clinical Decision Support Track and 2021 Clinical Trials Track dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShiPCH21.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShiPCH21,
		author = {Ming{-}Xuan Shi and Tsung{-}Hsuan Pan and Hsin{-}Hsi Chen and Hen{-}Hsen Huang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Hybrid Re-ranking for Biomedical Information Retrieval at the {TREC} 2021 Clinical Trials Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/NTU\_NLP-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ShiPCH21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

