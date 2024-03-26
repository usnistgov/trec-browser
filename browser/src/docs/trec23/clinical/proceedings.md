# Proceedings - Clinical Decision Support 2014 

#### Overview of the TREC 2014 Clinical Decision Support Track

_Matthew S. Simpson, Ellen M. Voorhees, William R. Hersh_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec23/papers/overview-clinical.pdf](https://trec.nist.gov/pubs/trec23/papers/overview-clinical.pdf)
??? abstract "Abstract"
	
	In making clinical decisions, physicians often seek out information about how to best care for their patients. Information relevant to a physician can be related to a variety of clinical tasks such as determining a patient's most likely diagnosis given a list of symptoms, deciding on the most effective treatment plan for a patient having a known condition, and determining if a particular test is indicated for a given situation. In some cases, physicians can find the information they seek in published biomedical literature. However, given the volume of the existing literature and the rapid pace at which new research is published, locating the most relevant and timely information for a particular clinical need can be a daunting and time-consuming task. To make biomedical information more accessible and to meet the requirements for the meaningful use of electronic health records, a goal of modern clinical decision support systems is to anticipate the needs of physicians by linking electronic health records with information relevant for patient care. The Clinical Decision Support Track aims to simulate the requirements of such systems and to encourage the creation of tools and resources necessary for their implementation. The focus of the 2014 track was the retrieval of biomedical articles relevant for answering generic clinical questions about medical records. In the absence of a reusable, de-identified collection of medical records, we used short case reports, such as those published in biomedical articles, as idealized representations of actual medical records. A case report typically describes a challenging medical case, and it is often organized as a well-formed narrative summarizing the portions of a patient's medical record that are pertinent to the case. Participants of the track were challenged with retrieving, for a given case report, full-text biomedical articles relevant for answering questions related to several types of clinical information needs. Each topic consisted of a case report and one of three generic clinical question types, such as “What is the patient's diagnosis?” Retrieved articles were judged relevant if they provide information of the specified type useful for the given case. The evaluation of the submissions followed standard TREC evaluation procedures. In the remainder of this overview we describe the documents (Section 2) and topics (Section 3) used for the retrieval task and the evaluation (Section 4) of the retrieval results. We also include raw statistics (Section 5) summarizing the performance of the participants' submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SimpsonVH14.bib) "
	```
	@inproceedings{DBLP:conf/trec/SimpsonVH14,
		author = {Matthew S. Simpson and Ellen M. Voorhees and William R. Hersh},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2014 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {https://trec.nist.gov/pubs/trec23/papers/overview-clinical.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SimpsonVH14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SNUMedinfo at TREC CDS track 2014: Medical case-based retrieval  task

_Sungbin Choi, Jinwook Choi_

- :fontawesome-solid-user-group: **Participant:** [SNUMedinfo](./participants.md#snumedinfo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-SNUMedinfo_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-SNUMedinfo_clinical.pdf)
- :material-file-search: **Runs:** [SNUMedinfo1](./runs.md#snumedinfo1) | [SNUMedinfo2](./runs.md#snumedinfo2) | [SNUMedinfo3](./runs.md#snumedinfo3) | [SNUMedinfo4](./runs.md#snumedinfo4) | [SNUMedinfo6](./runs.md#snumedinfo6)

??? abstract "Abstract"
	
	This paper describes the participation of the SNUMedinfo team at the TREC Clinical Decision Support track 2014. This task is about medical case-based retrieval. Case description is used as query text. Per each query, one of three categories (Diagnosis, Test and Treatment) is designated as target information need. Firstly, we used external tagged knowledge-based query expansion method for the relevance ranking. Secondly, machine learning classifier based text categorization method is used for the task-specific ranking. Finally, we combined relevance ranking and task-specific ranking with Borda-fuse method. Our method showed significant performance improvements
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChoiC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChoiC14,
		author = {Sungbin Choi and Jinwook Choi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {SNUMedinfo at {TREC} {CDS} track 2014: Medical case-based retrieval task},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-SNUMedinfo\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChoiC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LIMSI @ 2014 Clinical Decision Support Track

_Eva D'hondt, Brigitte Grau, Aurélie Névéol, Pierre Zweigenbaum, Stéfan Jacques Darmoni, Matthieu Schuers_

- :fontawesome-solid-user-group: **Participant:** [LIMSI](./participants.md#limsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-LIMSI_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-LIMSI_clinical.pdf)
- :material-file-search: **Runs:** [Run1BoWC](./runs.md#run1bowc) | [Run2MeSHDi](./runs.md#run2meshdi) | [Run3MeSHDiCa](./runs.md#run3meshdica) | [Run4BoWDiCa](./runs.md#run4bowdica) | [Run5BoWDiCaS](./runs.md#run5bowdicas)

??? abstract "Abstract"
	
	In this paper we present our participation in the 2014 TREC Clinical Decision Support Track. The goal of this track is to find relevant medical literature for a case report which should help address one specific clinical aspect of the case. Since it was the first time we participated in this task, we opted for an exploratory approach to test the impact of retrieval systems based on Bag-of-Words (BoW) or Medical Subject Headings (MeSH) index terms. In all five submitted runs, we used manually constructed MeSH queries to filter a target corpus for each of the three clinical question types. Query expansion (for both MeSH and BoW runs) was based on the automatic generation of disease hypotheses for which we used data from OrphaNet [4] and the Disease Symptom Knowledge Database [3]. Our best run was a MeSH-based run in which PubMed was queried directly with the MeSH terms extracted from the case reports, combined with the MeSH terms of the top 5 disease hypotheses generated for the case reports. Compared to the other participants we achieved low scores. Preliminary analysis shows that our corpus filtering method was too strict and has a negative impact on recall.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DhondtGNZDS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/DhondtGNZDS14,
		author = {Eva D'hondt and Brigitte Grau and Aur{\'{e}}lie N{\'{e}}v{\'{e}}ol and Pierre Zweigenbaum and St{\'{e}}fan Jacques Darmoni and Matthieu Schuers},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{LIMSI} @ 2014 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-LIMSI\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DhondtGNZDS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CRP Henri Tudor at TREC 2014: Combining Search Results for Clinical  Decision Support

_Duy Dinh, Asma Ben Abacha_

- :fontawesome-solid-user-group: **Participant:** [HENRI_TUDOR_LUX](./participants.md#henri_tudor_lux)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-HENRI_TUDOR_LUX_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-HENRI_TUDOR_LUX_clinical.pdf)
- :material-file-search: **Runs:** [tudorComb1](./runs.md#tudorcomb1) | [tudorComb3](./runs.md#tudorcomb3) | [tudorComb2](./runs.md#tudorcomb2) | [tudorComb4](./runs.md#tudorcomb4) | [tudorCombm](./runs.md#tudorcombm)

??? abstract "Abstract"
	
	This paper presents the first participation of the Luxembourgish Public Research Center Henri Tudor in the TREC 2014 Clinical Decision Support (CDS) Track. At the Resource Centre for Healthcare Technologies (SANTEC) department, we focus our research activities on healthcare technologies. Our mission consists primarily in improving healthcare by developing methods, tools, services and solutions that can be applied by healthcare professionals, patients and citizens on a daily basis. In this research work, we present an approach to combining search results using data fusion techniques. The focus of the 2014 Clinical Decision Support Track was the retrieval of relevant biomedical articles for answering generic clinical questions about medical records. Each question consists of a case report and one of three generic clinical question types, such as “What is the patient's diagnosis?”. Retrieved articles are judged relevant if they provide information of the specified type that is relevant to the given case. The remainder of this report is organized as follows. Section 2 gives a brief description about he CDS Task. Section 3 describes our methodology for combining search results. Our submitted runs and the official results of TREC CDS Track are described in Section 4. Finally, Section 5 draws our conclusions and outlining directions for future work
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DinhA14.bib) "
	```
	@inproceedings{DBLP:conf/trec/DinhA14,
		author = {Duy Dinh and Asma Ben Abacha},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CRP} Henri Tudor at {TREC} 2014: Combining Search Results for Clinical Decision Support},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-HENRI\_TUDOR\_LUX\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DinhA14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCLA at TREC 2014 Clinical Decision Support Track: Exploring Language  Models, Query Expansion, and Boosting

_Jean I. Garcia-Gathright, Frank Meng, William Hsu_

- :fontawesome-solid-user-group: **Participant:** [UCLA_MII](./participants.md#ucla_mii)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UCLA_MII_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UCLA_MII_clinical.pdf)
- :material-file-search: **Runs:** [MIItfman](./runs.md#miitfman) | [MIItfauto](./runs.md#miitfauto) | [MIIjmab](./runs.md#miijmab) | [MIIjmignore](./runs.md#miijmignore) | [MIIjmboost](./runs.md#miijmboost)

??? abstract "Abstract"
	
	For the TREC 2014 Clinical Decision Support track, participants were given a set of 30 patient cases in the form of a short natural language description and a data set of over 700,000 full-text articles from PubMed Central. The task was to retrieve articles relevant to the patient cases and one of three types of clinical question: diagnosis, test, and treatment. This paper describes the retrieval system developed by the Medical Imaging Informatics group at the University of California, Los Angeles. One manual run and four automatic runs were submitted. For the automatic runs, a variety of retrieval strategies were explored. Two retrieval methods were compared: the vector space model with TF-IDF similarity, and a unigram language model with Jelinek-Mercer smoothing. The performance of retrieving on abstracts alone was compared to that of full-text. Finally, a simple set of rules for query expansion and term boosting was developed based on recommendations from domain experts. Submissions for 26 groups were pooled and evaluated by a team of medical librarians and physicians at the National Institute of Standards and Technology. The results showed that 1) the language model outperformed the vector space model for automatically-constructed queries, 2) searching full-text was more effective than searching abstracts alone, and 3) boosting improved the ranking of retrieved documents for 'test' topics, but not 'diagnosis' topics. Our best automatic run used the language model, full-text search, query expansion, and no boosting.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Garcia-Gathright14.bib) "
	```
	@inproceedings{DBLP:conf/trec/Garcia-Gathright14,
		author = {Jean I. Garcia{-}Gathright and Frank Meng and William Hsu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UCLA} at {TREC} 2014 Clinical Decision Support Track: Exploring Language Models, Query Expansion, and Boosting},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UCLA\_MII\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Garcia-Gathright14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion Using SNOMED-CT and Weighing Schemes

_Dawit Girmay, Afshin Deroie_

- :fontawesome-solid-user-group: **Participant:** [DawitAfshin](./participants.md#dawitafshin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-DawitAfshin_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-DawitAfshin_clinical.pdf)
- :material-file-search: **Runs:** [BM25](./runs.md#bm25) | [BM25EXP](./runs.md#bm25exp) | [InL2c1](./runs.md#inl2c1) | [InL2c1EXP](./runs.md#inl2c1exp)

??? abstract "Abstract"
	
	Despite all the advancements that have been made in the field of Information Retrieval, there are still so many challenges. These challenges are magnified when the information that is being retrieved is in a specialized domain such as healthcare. In order to tackle these challenges and encourage research in these domains, TREC (Text RETrival Conference) has instituted a Clinical Track in 2014. This paper is the result of participation in 2014 TREC Clinical Track. It entails the approach and the results that were obtained by utilizing Ontology to expand the original topics. Ontology was used in order to improve the quality of the terms present in the queries or topics, so that the queries are better structured, and they can better target documents of interest. The value that each term brings to the result was measured by way of weighing method algorithms in the retrieval system, BM25 and InL2c1. For this research, we have used SNOMED-CT along with UMLS Methathesaurus as our ontology in medical domain to expand the queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GirmayD14.bib) "
	```
	@inproceedings{DBLP:conf/trec/GirmayD14,
		author = {Dawit Girmay and Afshin Deroie},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query Expansion Using {SNOMED-CT} and Weighing Schemes},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-DawitAfshin\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GirmayD14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Full-texts representation with Medical Subject Headings, and co-citations  network rerank- ing strategies for TREC 2014 Clinical Decision Support  Track

_Julien Gobeill, Arnaud Gaudinat, Emilie Pasche, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BiTeM_SIBtex](./participants.md#bitem_sibtex)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BiTeM_SIBtex_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BiTeM_SIBtex_clinical.pdf)
- :material-file-search: **Runs:** [BiTeMSIBtex1](./runs.md#bitemsibtex1) | [BiTeMSIBtex2](./runs.md#bitemsibtex2) | [BiTeMSIBtex4](./runs.md#bitemsibtex4) | [BiTeMSIBtex5](./runs.md#bitemsibtex5) | [BiTeMSIBtex3](./runs.md#bitemsibtex3)

??? abstract "Abstract"
	
	In TREC 2014 Clinical Decision Support Track, the task was to retrieve full-texts relevant for answering generic clinical questions about medical records. For this purpose, we investigated a large range of strategies in the five runs we officially submitted. Concerning Information Retrieval (IR), we tested two different indexing levels: documents or sections. Section indexing was clearly below (-40% in R-Precision). In the domain of Information Extraction, we enriched documents with Medical Subject Headings concepts that were collected from MEDLINE or extracted in the text with exact match strategies. We also investigated a target-specific semantic enrichment: MeSH terms representing diagnosis, treatments or tests (relying on UMLS semantic types) were used both in collection and in queries to guide the retrieval. Unfortunately, the MeSH representation was not as complementary with the text as we expected, and the results were disappointing. Concerning post-processing strategies, we tested the boosting of specific articles types (e.g. review articles, case reports), but the IR process already tended to favour these article types. Finally, we applied a reranking strategy relying on the co-citations network, thanks to normalized references provided in the corpus. This last strategy led to a slight improvement (+5%).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GobeillGPR14.bib) "
	```
	@inproceedings{DBLP:conf/trec/GobeillGPR14,
		author = {Julien Gobeill and Arnaud Gaudinat and Emilie Pasche and Patrick Ruch},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Full-texts representation with Medical Subject Headings, and co-citations network rerank- ing strategies for {TREC} 2014 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BiTeM\_SIBtex\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GobeillGPR14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UTD at TREC 2014: Query Expansion for Clinical Decision Support

_Travis R. Goodwin, Sanda M. Harabagiu_

- :fontawesome-solid-user-group: **Participant:** [UTDHLTRI](./participants.md#utdhltri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UTDHLTRI_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UTDHLTRI_clinical.pdf)
- :material-file-search: **Runs:** [UTD0BL](./runs.md#utd0bl) | [UTD1QE](./runs.md#utd1qe) | [UTD2LDA](./runs.md#utd2lda) | [UTD3W2VE](./runs.md#utd3w2ve)

??? abstract "Abstract"
	
	This paper describes the medical information retrieval (MIR) systems designed by the University of Texas at Dallas (UTD) for clinical decision support (CDS) which were submitted to the TREC 2014. We investigated the impact of various knowledge bases for automatic query expansion in the four officially submitted runs. Each of these systems exploits both Wikipedia and PubMed corpus statistics in order to automatically extract keywords. Extracted keywords were then expanded by relying on structured medical knowledge bases, such as the Unified Medical Language System (UMLS), the Systemized Nomenclature of Medicine - Clinical Terms (SNOMED-CT), and Wikipedia as well as unsupervised distributional representations based Google's Word2Vec deep learning architecture. Our highest scoring submission achieved an inferred AP score of 0.056 and an inferred NDCG score of 0.205.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoodwinH14.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoodwinH14,
		author = {Travis R. Goodwin and Sanda M. Harabagiu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UTD} at {TREC} 2014: Query Expansion for Clinical Decision Support},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UTDHLTRI\_clinical.pdf},
		timestamp = {Mon, 19 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GoodwinH14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Hybrid Approach to Clinical Question Answering

_Sadid A. Hasan, Xianshu Zhu, Yao Dong, Joey Liu, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [Philips](./participants.md#philips)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-Philips_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-Philips_clinical.pdf)
- :material-file-search: **Runs:** [prna1](./runs.md#prna1)

??? abstract "Abstract"
	
	In this paper, we describe our clinical question answering system developed and submitted for the Text Retrieval Conference (TREC 2014) Clinical Decision Support (CDS) track. The task for this track was to retrieve relevant biomedical articles to answer generic clinical questions about medical case reports. As part of our maiden participation in TREC, we submitted a single run using a hybrid Natural Language Processing (NLP)-driven approach to accomplish the given task. Evaluation results showed that our clinical question answering system achieved the best scores in two of eight dual-judged topics: #5 and 27, and performed relatively better compared to the median scores for topics: #13, 18, 19, 22, and 23.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HasanZDLF14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HasanZDLF14,
		author = {Sadid A. Hasan and Xianshu Zhu and Yao Dong and Joey Liu and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Hybrid Approach to Clinical Question Answering},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-Philips\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HasanZDLF14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NovaSearch at TREC 2014 Clinical Decision Support Track

_André Mourão, Flávio Martins, João Magalhães_

- :fontawesome-solid-user-group: **Participant:** [NovaSearch](./participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-NovaSearch_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-NovaSearch_clinical.pdf)
- :material-file-search: **Runs:** [NOVASEARCH1](./runs.md#novasearch1) | [NOVASEARCH2](./runs.md#novasearch2) | [NOVASEARCH3](./runs.md#novasearch3) | [NOVASEARCH4](./runs.md#novasearch4) | [NOVASEARCH5](./runs.md#novasearch5)

??? abstract "Abstract"
	
	This paper describes the participation of the NovaSearch group at TREC Clinical Decision Support 2014. As this is the first edition of the track, we decided to assess the performance of multiple information retrieval techniques: retrieval functions, re-ranking, query expansion and classification of medical articles into question categories. The best performing run was based on an ensemble of state-of-the-art retrieval algorithms combined with unsupervised fusion. Our best run was based on the late fusion of runs using MeSH query expansion, pseudo-relevance feedback with terms from top retrieved results and multiple retrieval functions (BM25L, BM25+, TF-IDF and Language Models) combined with RRF fusion algorithm. We also tested an algorithm to measure article relevance to the target medical questions (diagnosis, test and treatment articles), based on the frequency of words to some categories. An additional experiment was based on pseudo relevance feedback based on each article's journal reputation. Although some techniques did not increase our baseline performance, we are satisfied with our global performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MouraoMM14.bib) "
	```
	@inproceedings{DBLP:conf/trec/MouraoMM14,
		author = {Andr{\'{e}} Mour{\~{a}}o and Fl{\'{a}}vio Martins and Jo{\~{a}}o Magalh{\~{a}}es},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {NovaSearch at {TREC} 2014 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-NovaSearch\_clinical.pdf},
		timestamp = {Thu, 14 May 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MouraoMM14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### KISTI at TREC 2014 Clinical Decision Support Track: Concept-based  Document Re-ranking to Biomedical Information Retrieval

_Heung-Seon Oh, Yuchul Jung_

- :fontawesome-solid-user-group: **Participant:** [KISTI](./participants.md#kisti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-KISTI_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-KISTI_clinical.pdf)
- :material-file-search: **Runs:** [KISTI01](./runs.md#kisti01) | [KISTI02](./runs.md#kisti02) | [KISTI03](./runs.md#kisti03) | [KISTI04](./runs.md#kisti04) | [KISTI05](./runs.md#kisti05)

??? abstract "Abstract"
	
	With fast development of medical information systems and software, clinical decision support (CDS) systems continue to develop new methods to deal with diverse information coming from heterogeneous sources such as a large volume of electronic medical records (EMRs), patient genomic data, existing genomic pharmaceutical databases, curated disease-specific databases, peer-reviewed research, etc. As an avenue towards advanced clinical decision-making, TREC CDS track focuses on developing new techniques to find medical cases that are useful for patient care from biomedical literature. Meanwhile, given the volume of the existing literature, and the diversity in biomedical field, finding & delivering relevant medical cases for a particular clinical need is a non-trivial task. Moreover, understanding three kinds of different topics (i.e. diagnosis, test, and treatment) and retrieving appropriate biomedical research articles are quite challenging. To address these problems, we propose concept-based document re-ranking approaches to clinical documents. We basically use pseudo relevance feedback for query expansion to retrieve initial relevant documents. In addition, we considered two different concept-based re-ranking approaches which utilize popular external biomedical knowledge resources (i.e. Wikipedia and UMLS) for improving biomedical information retrieval. Our concept-based re-ranking approaches are to bridge the gaps between queries and biomedical research articles in semantic level.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OhJ14.bib) "
	```
	@inproceedings{DBLP:conf/trec/OhJ14,
		author = {Heung{-}Seon Oh and Yuchul Jung},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{KISTI} at {TREC} 2014 Clinical Decision Support Track: Concept-based Document Re-ranking to Biomedical Information Retrieval},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-KISTI\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OhJ14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TUW @ TREC Clinical Decision Support Track

_João R. M. Palotti, Navid Rekabsaz, Linda Andersson, Allan Hanbury_

- :fontawesome-solid-user-group: **Participant:** [TUW](./participants.md#tuw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-TUW_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-TUW_clinical.pdf)
- :material-file-search: **Runs:** [TUW1](./runs.md#tuw1) | [TUW2](./runs.md#tuw2) | [TUW3](./runs.md#tuw3) | [TUW4](./runs.md#tuw4) | [TUW5](./runs.md#tuw5)

??? abstract "Abstract"
	
	This document describes the participation of Vienna University of Technology in the TREC Clinical Decision Support Track 2014. Four different search models are investigated, as well as different strategies to index the corpus and to extract the most relevant information from the topics. Our results conclude that BM25 and Vector Space Model had similar performance for P@10 and inferred NDCG.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PalottiRAH14.bib) "
	```
	@inproceedings{DBLP:conf/trec/PalottiRAH14,
		author = {Jo{\~{a}}o R. M. Palotti and Navid Rekabsaz and Linda Andersson and Allan Hanbury},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TUW} @ {TREC} Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-TUW\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PalottiRAH14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fusing manual and machine feedback in biomedical domain

_Jainisha Sankhavara, Fenny Thakrar, Prasenjit Majumder, Shamayeeta Sarkar_

- :fontawesome-solid-user-group: **Participant:** [DA_IICT](./participants.md#da_iict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-DA_IICT_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-DA_IICT_clinical.pdf)
- :material-file-search: **Runs:** [DAIICTzf](./runs.md#daiictzf) | [DAIICTf](./runs.md#daiictf) | [DAIICTdqer8](./runs.md#daiictdqer8) | [DAIICTdqep](./runs.md#daiictdqep) | [DAIICTsqer8](./runs.md#daiictsqer8)

??? abstract "Abstract"
	
	For our participation in CDS task of TREC, our first objective was to obtain efficient biomedical document retrieval. We focused on fusing manual and machine feedback runs. Fusion run performs better and gives consistent results for considered evaluation metrics. Also, the categories 'diagnosis' and 'treatment' are giving good results compared to 'test'.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SankhavaraTMS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/SankhavaraTMS14,
		author = {Jainisha Sankhavara and Fenny Thakrar and Prasenjit Majumder and Shamayeeta Sarkar},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Fusing manual and machine feedback in biomedical domain},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-DA\_IICT\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SankhavaraTMS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Centrality based Document Ranking

_Anil Kumar Singh, C. Ravindranath Chowdary_

- :fontawesome-solid-user-group: **Participant:** [CSEIITV](./participants.md#cseiitv)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-CSEIITV_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-CSEIITV_clinical.pdf)
- :material-file-search: **Runs:** [summary50ex](./runs.md#summary50ex) | [descript50ex](./runs.md#descript50ex)

??? abstract "Abstract"
	
	In this paper, we address the problem of ranking clinical documents using centrality based approach. We model the documents to be ranked as nodes in a graph and place edges between documents based on their similarity. Given a query, we compute similarity of the query with respect to every document in the graph. Based on these similarity values, documents are ranked for a given query. Initially, Lucene1 is used to retrieve top fifty documents that are relevant to the query and then our proposed approach is applied on these retrieved documents to re-rank them. Experimental results show that our approach did not perform well as the documents retrieved by Lucene are not among the top 50 documents in the Gold Standard.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinghC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinghC14,
		author = {Anil Kumar Singh and C. Ravindranath Chowdary},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Centrality based Document Ranking},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-CSEIITV\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SinghC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Reformulation for Clinical Decision Support Search

_Luca Soldaini, Arman Cohan, Andrew Yates, Nazli Goharian, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [georgetown_ir](./participants.md#georgetown_ir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-georgetown_ir_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-georgetown_ir_clinical.pdf)
- :material-file-search: **Runs:** [IRGURUN1](./runs.md#irgurun1) | [IRGURUN2](./runs.md#irgurun2) | [IRGURUN3](./runs.md#irgurun3) | [IRGURUN4](./runs.md#irgurun4) | [IRGURUN5](./runs.md#irgurun5)

??? abstract "Abstract"
	
	One of the tasks a Clinical Decision Support (CDS) system is designed to solve is retrieving the most relevant and actionable literature for a given medical case report. In this work, we present a query reformulation approach that addresses the unique formulation of case reports, making them suitable to be used on a general purpose search engine. Furthermore, we introduce five reranking algorithms designed to re-order a list of retrieved literature to better match the type of information needed for each case report.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SoldainiCYGF14.bib) "
	```
	@inproceedings{DBLP:conf/trec/SoldainiCYGF14,
		author = {Luca Soldaini and Arman Cohan and Andrew Yates and Nazli Goharian and Ophir Frieder},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query Reformulation for Clinical Decision Support Search},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-georgetown\_ir\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SoldainiCYGF14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Modification through External Sources to Support Clinical Decisions

_Raymond Wan, Ting-Fung Chan, Jannifer Hiu-Kwan Man_

- :fontawesome-solid-user-group: **Participant:** [cuhk_sls](./participants.md#cuhk_sls)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-cuhk_sls_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-cuhk_sls_clinical.pdf)
- :material-file-search: **Runs:** [icdqe](./runs.md#icdqe) | [mesh](./runs.md#mesh) | [icd](./runs.md#icd) | [origexp](./runs.md#origexp) | [manual](./runs.md#manual)

??? abstract "Abstract"
	
	For the Clinical Decision Support Track of TREC 2014, we looked into the effect of modifying queries by adding or removing terms. We considered both automatic and manual query modifications that use either external data sources or a domain expert. While each method gave slightly different results, we discovered that the manual method still performed slightly better among the methods we considered. This is despite the fact that the manual queries were formed through just term removal; no new terms were added.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WanCM14.bib) "
	```
	@inproceedings{DBLP:conf/trec/WanCM14,
		author = {Raymond Wan and Ting{-}Fung Chan and Jannifer Hiu{-}Kwan Man},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query Modification through External Sources to Support Clinical Decisions},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-cuhk\_sls\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WanCM14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring the Query Expansion Methods for Concept Based Representation

_Yue Wang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_clinical.pdf)
- :material-file-search: **Runs:** [UDInfoCDS1](./runs.md#udinfocds1) | [UDInfoCDS2](./runs.md#udinfocds2) | [UDInfoCDS3](./runs.md#udinfocds3) | [UDInfoCDS4](./runs.md#udinfocds4) | [UDInfoCDS5](./runs.md#udinfocds5)

??? abstract "Abstract"
	
	The CDS track investigates methods that could help physicians find relevant medical cases for patients they are dealing with. Concept based representation has been shown to be effective in biomedical domain. However, the basic concept based retrieval method may not perform well because of the additional restriction on each clinical cases. Therefore, in this paper, we explored two external resources to perform query expansion for the basic concept based representation method, and discussed the performance of them.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangF14.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangF14,
		author = {Yue Wang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Exploring the Query Expansion Methods for Concept Based Representation},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_fang\_clinical.pdf},
		timestamp = {Thu, 17 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WangF14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Atigeo at TREC 2014 Clinical Decision Support Task

_Yishul Wei, ChenChieh Hsu, Alex Thomas, Joseph F. McCarthy_

- :fontawesome-solid-user-group: **Participant:** [atigeo](./participants.md#atigeo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-atigeo_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-atigeo_clinical.pdf)
- :material-file-search: **Runs:** [atigeo3](./runs.md#atigeo3) | [atigeo4](./runs.md#atigeo4) | [atigeo1](./runs.md#atigeo1) | [atigeo2](./runs.md#atigeo2) | [atigeo5](./runs.md#atigeo5)

??? abstract "Abstract"
	
	The TREC 2014 Clinical Decision Support Track task involves retrieval and ranking of medical journal articles with respect to their relevance to prescribing tests, diagnosing or treating a patient represented in a short case report. The Atigeo xPatterns™ platform supports a variety of ensemble methods for developing and tuning information retrieval (IR) system components for a task and/or domain using labeled data. For TREC 2014, we combine results from an ensemble of search engines, each with a configurable suite of natural language processing (NLP) components, to compute a relevance score for each article and topic. We describe our ensemble approach, the strategies and tools we use to create labeled data to support this approach, the components in our IR / NLP pipeline, and our results on the TREC 2014 CDS task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WeiHTM14.bib) "
	```
	@inproceedings{DBLP:conf/trec/WeiHTM14,
		author = {Yishul Wei and ChenChieh Hsu and Alex Thomas and Joseph F. McCarthy},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Atigeo at {TREC} 2014 Clinical Decision Support Task},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-atigeo\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WeiHTM14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Refinement: Negation Detection and Proximity Learning Georgetown  at TREC 2014 Clinical Decision Support Track

_Christopher Wing, Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [Georgetown](./participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-Georgetown_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-Georgetown_clinical.pdf)
- :material-file-search: **Runs:** [GuHSINeg](./runs.md#guhsineg) | [GuHNegProxL](./runs.md#guhnegproxl) | [GuHSNegProxH](./runs.md#guhsnegproxh) | [GuHSNegProxL](./runs.md#guhsnegproxl) | [GuHSINegL](./runs.md#guhsinegl)

??? abstract "Abstract"
	
	In this paper we describe our efforts for TREC Clinical Decision Support Track 2014. Our system takes medical case narratives as input and returns relevant biomedical articles to answer clinical questions to determine the patient's diagnosis, the tests the patient should receive, and how the patient should be treated. We model each topic as highly representative keyword-based structured queries. Since both the topics and returned documents are written in highly technical language, we address the traditional vocabulary gap present within medical information retrieval, while also focusing on employing methodologies to refine our queries by detecting negation and applying query proximity learning. We hypothesized terms with high frequency among the topics, which are likely to create noise and impair the return of highly relevant documents. Our top two runs utilizing negation detection perform above the median for P@10, R-Prec, and infAP, and our other three runs that utilized proximity learning performed approximately consistent with the median. More research is required to explore the potential benefits of proximity learning over a more robust set of topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WingY14.bib) "
	```
	@inproceedings{DBLP:conf/trec/WingY14,
		author = {Christopher Wing and Hui Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query Refinement: Negation Detection and Proximity Learning Georgetown at {TREC} 2014 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-Georgetown\_clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WingY14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HLTCOE at TREC 2014: Microblog and Clinical Decision Support

_Tan Xu, Douglas W. Oard, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [hltcoe](./participants.md#hltcoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-hltcoe_microblog-clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-hltcoe_microblog-clinical.pdf)
- :material-file-search: **Runs:** [hltcoewsrf](./runs.md#hltcoewsrf) | [hltcoe5srf](./runs.md#hltcoe5srf) | [hltcoe5drf](./runs.md#hltcoe5drf) | [hltcoe5s](./runs.md#hltcoe5s)

??? abstract "Abstract"
	
	Our team submitted runs for both the Microblog and Clinical Decision Support tracks. For the Microblog track, we participated in both the temporally anchored adhoc search and the tweet timeline generation subtasks. On the Clinical Decision support task, our efforts were time limited, and our main contribution was to investigate controlling for morphological variation in this technical domain.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuOM14.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuOM14,
		author = {Tan Xu and Douglas W. Oard and Paul McNamee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{HLTCOE} at {TREC} 2014: Microblog and Clinical Decision Support},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-hltcoe\_microblog-clinical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuOM14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

