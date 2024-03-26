# Proceedings 2014 

## Clinical Decision Support 

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

- :fontawesome-solid-user-group: **Participant:** [SNUMedinfo](./clinical/participants.md#snumedinfo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-SNUMedinfo_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-SNUMedinfo_clinical.pdf)
- :material-file-search: **Runs:** [SNUMedinfo1](./clinical/runs.md#snumedinfo1) | [SNUMedinfo2](./clinical/runs.md#snumedinfo2) | [SNUMedinfo3](./clinical/runs.md#snumedinfo3) | [SNUMedinfo4](./clinical/runs.md#snumedinfo4) | [SNUMedinfo6](./clinical/runs.md#snumedinfo6)

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

- :fontawesome-solid-user-group: **Participant:** [LIMSI](./clinical/participants.md#limsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-LIMSI_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-LIMSI_clinical.pdf)
- :material-file-search: **Runs:** [Run1BoWC](./clinical/runs.md#run1bowc) | [Run2MeSHDi](./clinical/runs.md#run2meshdi) | [Run3MeSHDiCa](./clinical/runs.md#run3meshdica) | [Run4BoWDiCa](./clinical/runs.md#run4bowdica) | [Run5BoWDiCaS](./clinical/runs.md#run5bowdicas)

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

- :fontawesome-solid-user-group: **Participant:** [HENRI_TUDOR_LUX](./clinical/participants.md#henri_tudor_lux)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-HENRI_TUDOR_LUX_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-HENRI_TUDOR_LUX_clinical.pdf)
- :material-file-search: **Runs:** [tudorComb1](./clinical/runs.md#tudorcomb1) | [tudorComb3](./clinical/runs.md#tudorcomb3) | [tudorComb2](./clinical/runs.md#tudorcomb2) | [tudorComb4](./clinical/runs.md#tudorcomb4) | [tudorCombm](./clinical/runs.md#tudorcombm)

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

- :fontawesome-solid-user-group: **Participant:** [UCLA_MII](./clinical/participants.md#ucla_mii)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UCLA_MII_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UCLA_MII_clinical.pdf)
- :material-file-search: **Runs:** [MIItfman](./clinical/runs.md#miitfman) | [MIItfauto](./clinical/runs.md#miitfauto) | [MIIjmab](./clinical/runs.md#miijmab) | [MIIjmignore](./clinical/runs.md#miijmignore) | [MIIjmboost](./clinical/runs.md#miijmboost)

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

- :fontawesome-solid-user-group: **Participant:** [DawitAfshin](./clinical/participants.md#dawitafshin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-DawitAfshin_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-DawitAfshin_clinical.pdf)
- :material-file-search: **Runs:** [BM25](./clinical/runs.md#bm25) | [BM25EXP](./clinical/runs.md#bm25exp) | [InL2c1](./clinical/runs.md#inl2c1) | [InL2c1EXP](./clinical/runs.md#inl2c1exp)

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

- :fontawesome-solid-user-group: **Participant:** [BiTeM_SIBtex](./clinical/participants.md#bitem_sibtex)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BiTeM_SIBtex_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BiTeM_SIBtex_clinical.pdf)
- :material-file-search: **Runs:** [BiTeMSIBtex1](./clinical/runs.md#bitemsibtex1) | [BiTeMSIBtex2](./clinical/runs.md#bitemsibtex2) | [BiTeMSIBtex4](./clinical/runs.md#bitemsibtex4) | [BiTeMSIBtex5](./clinical/runs.md#bitemsibtex5) | [BiTeMSIBtex3](./clinical/runs.md#bitemsibtex3)

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

- :fontawesome-solid-user-group: **Participant:** [UTDHLTRI](./clinical/participants.md#utdhltri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UTDHLTRI_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UTDHLTRI_clinical.pdf)
- :material-file-search: **Runs:** [UTD0BL](./clinical/runs.md#utd0bl) | [UTD1QE](./clinical/runs.md#utd1qe) | [UTD2LDA](./clinical/runs.md#utd2lda) | [UTD3W2VE](./clinical/runs.md#utd3w2ve)

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

- :fontawesome-solid-user-group: **Participant:** [Philips](./clinical/participants.md#philips)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-Philips_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-Philips_clinical.pdf)
- :material-file-search: **Runs:** [prna1](./clinical/runs.md#prna1)

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

- :fontawesome-solid-user-group: **Participant:** [NovaSearch](./clinical/participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-NovaSearch_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-NovaSearch_clinical.pdf)
- :material-file-search: **Runs:** [NOVASEARCH1](./clinical/runs.md#novasearch1) | [NOVASEARCH2](./clinical/runs.md#novasearch2) | [NOVASEARCH3](./clinical/runs.md#novasearch3) | [NOVASEARCH4](./clinical/runs.md#novasearch4) | [NOVASEARCH5](./clinical/runs.md#novasearch5)

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

- :fontawesome-solid-user-group: **Participant:** [KISTI](./clinical/participants.md#kisti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-KISTI_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-KISTI_clinical.pdf)
- :material-file-search: **Runs:** [KISTI01](./clinical/runs.md#kisti01) | [KISTI02](./clinical/runs.md#kisti02) | [KISTI03](./clinical/runs.md#kisti03) | [KISTI04](./clinical/runs.md#kisti04) | [KISTI05](./clinical/runs.md#kisti05)

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

- :fontawesome-solid-user-group: **Participant:** [TUW](./clinical/participants.md#tuw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-TUW_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-TUW_clinical.pdf)
- :material-file-search: **Runs:** [TUW1](./clinical/runs.md#tuw1) | [TUW2](./clinical/runs.md#tuw2) | [TUW3](./clinical/runs.md#tuw3) | [TUW4](./clinical/runs.md#tuw4) | [TUW5](./clinical/runs.md#tuw5)

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

- :fontawesome-solid-user-group: **Participant:** [DA_IICT](./clinical/participants.md#da_iict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-DA_IICT_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-DA_IICT_clinical.pdf)
- :material-file-search: **Runs:** [DAIICTzf](./clinical/runs.md#daiictzf) | [DAIICTf](./clinical/runs.md#daiictf) | [DAIICTdqer8](./clinical/runs.md#daiictdqer8) | [DAIICTdqep](./clinical/runs.md#daiictdqep) | [DAIICTsqer8](./clinical/runs.md#daiictsqer8)

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

- :fontawesome-solid-user-group: **Participant:** [CSEIITV](./clinical/participants.md#cseiitv)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-CSEIITV_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-CSEIITV_clinical.pdf)
- :material-file-search: **Runs:** [summary50ex](./clinical/runs.md#summary50ex) | [descript50ex](./clinical/runs.md#descript50ex)

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

- :fontawesome-solid-user-group: **Participant:** [georgetown_ir](./clinical/participants.md#georgetown_ir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-georgetown_ir_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-georgetown_ir_clinical.pdf)
- :material-file-search: **Runs:** [IRGURUN1](./clinical/runs.md#irgurun1) | [IRGURUN2](./clinical/runs.md#irgurun2) | [IRGURUN3](./clinical/runs.md#irgurun3) | [IRGURUN4](./clinical/runs.md#irgurun4) | [IRGURUN5](./clinical/runs.md#irgurun5)

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

- :fontawesome-solid-user-group: **Participant:** [cuhk_sls](./clinical/participants.md#cuhk_sls)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-cuhk_sls_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-cuhk_sls_clinical.pdf)
- :material-file-search: **Runs:** [icdqe](./clinical/runs.md#icdqe) | [mesh](./clinical/runs.md#mesh) | [icd](./clinical/runs.md#icd) | [origexp](./clinical/runs.md#origexp) | [manual](./clinical/runs.md#manual)

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

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./clinical/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_clinical.pdf)
- :material-file-search: **Runs:** [UDInfoCDS1](./clinical/runs.md#udinfocds1) | [UDInfoCDS2](./clinical/runs.md#udinfocds2) | [UDInfoCDS3](./clinical/runs.md#udinfocds3) | [UDInfoCDS4](./clinical/runs.md#udinfocds4) | [UDInfoCDS5](./clinical/runs.md#udinfocds5)

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

- :fontawesome-solid-user-group: **Participant:** [atigeo](./clinical/participants.md#atigeo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-atigeo_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-atigeo_clinical.pdf)
- :material-file-search: **Runs:** [atigeo3](./clinical/runs.md#atigeo3) | [atigeo4](./clinical/runs.md#atigeo4) | [atigeo1](./clinical/runs.md#atigeo1) | [atigeo2](./clinical/runs.md#atigeo2) | [atigeo5](./clinical/runs.md#atigeo5)

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

- :fontawesome-solid-user-group: **Participant:** [Georgetown](./clinical/participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-Georgetown_clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-Georgetown_clinical.pdf)
- :material-file-search: **Runs:** [GuHSINeg](./clinical/runs.md#guhsineg) | [GuHNegProxL](./clinical/runs.md#guhnegproxl) | [GuHSNegProxH](./clinical/runs.md#guhsnegproxh) | [GuHSNegProxL](./clinical/runs.md#guhsnegproxl) | [GuHSINegL](./clinical/runs.md#guhsinegl)

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

- :fontawesome-solid-user-group: **Participant:** [hltcoe](./clinical/participants.md#hltcoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-hltcoe_microblog-clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-hltcoe_microblog-clinical.pdf)
- :material-file-search: **Runs:** [hltcoewsrf](./clinical/runs.md#hltcoewsrf) | [hltcoe5srf](./clinical/runs.md#hltcoe5srf) | [hltcoe5drf](./clinical/runs.md#hltcoe5drf) | [hltcoe5s](./clinical/runs.md#hltcoe5s)

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

## Contextual Suggestion 

#### Overview of the TREC 2014 Contextual Suggestion Track

_Adriel Dean-Hall, Charles L. A. Clarke, Jaap Kamps, Paul Thomas, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/overview-context.pdf](http://trec.nist.gov/pubs/trec23/papers/overview-context.pdf)
??? abstract "Abstract"
	
	For participants familiar with the 2013 Contextual Suggestion Track we have provided a list of the main changes to this year's track: Assessors were recruited only from a crowdsourcing service (Mechanical Turk) and not from any student bodies. Only CSV formatted files were available for profiles, contexts, and suggestions. Two seed cities were used instead of one (Chicago, IL and Santa Fe, NM) and the target cities were also changed. The number of ratings provided in profiles was changed from 50 to 70 or 100 (depending on the profile). 31 runs were submitted from 17 groups, 6 of these were ClueWeb12 runs and 25 were open web runs. If you are already familiar with this track you can skip to Section 5 which gives an overview of the approaches participants used and Section 6 which contains the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Dean-HallCKTV14.bib) "
	```
	@inproceedings{DBLP:conf/trec/Dean-HallCKTV14,
		author = {Adriel Dean{-}Hall and Charles L. A. Clarke and Jaap Kamps and Paul Thomas and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2014 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/overview-context.pdf},
		timestamp = {Fri, 24 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Dean-HallCKTV14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A New Approach to Contextual Suggestions Based on Word2Vec

_Yongqiang Chen, Zhenjun Tang, Xiaozhao Zhao, Dawei Song, Peng Zhang_

- :fontawesome-solid-user-group: **Participant:** [TJU_CS_IR](./context/participants.md#tju_cs_ir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-TJU_CS_IR _cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-TJU_CS_IR _cs.pdf)
- :material-file-search: **Runs:** [runB](./context/runs.md#runb) | [runA](./context/runs.md#runa)

??? abstract "Abstract"
	
	We report our participation in the contextual suggestion track of TREC 2014 for which we submitted two runs using a novel approach to complete the competition. The goal of the track is to generate suggestions that users might fond of given the history of users' preference where he or she used to live in when they travel to a new city. We tested our new approach in the dataset of ClueWeb12-CatB which has been pre-indexed by Luence. Our system represents all attractions and user contexts in the continuous vector space learnt by neural network language models, and then we learn the user-dependent profile model to predict the user's ratings for the attraction's websites using Softmax. Finally, we rank all the venues by using the generated model according the users' personal preference.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenTZSZ14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenTZSZ14,
		author = {Yongqiang Chen and Zhenjun Tang and Xiaozhao Zhao and Dawei Song and Peng Zhang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A New Approach to Contextual Suggestions Based on Word2Vec},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-TJU\_CS\_IR\ \_cs.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenTZSZ14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Applying Learning to Rank Techniques to Contextual Suggestions

_Julia Kiseleva, Alejandro Montes García, Yongming Luo, Mykola Pechenizkiy, Paul De Bra, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [eindhoven](./context/participants.md#eindhoven)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-eindhoven_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-eindhoven_cs.pdf)
- :material-file-search: **Runs:** [tueRforest](./context/runs.md#tuerforest) | [tueNet](./context/runs.md#tuenet)

??? abstract "Abstract"
	
	The Text Retrieval Conference's Contextual Suggestion Track investigates search techniques for complex information needs that are highly dependent on a context and user interests. The goal of the track is to evaluate systems that provide suggestions for activities to users in a specific location, taking into account their historical personal preferences. In this paper, we present our approach for the Contextual Sugges- tion Track 2014. We suggest to treat the problem of Con- textual Suggestion as a Learning to Rank problem. As a source for travel suggestions we use data from four social networks: Yelp, Facebook, Foursquare and Google Places. For our study we train two ranking algorithms: Rank Net and Random Forest. In our experiments, we seek to answer the following research questions: Does the distance between the locations of training and testing contexts impact precision? Which data sources (i.e., Facebook, Foursquare, Yelp, and Google Places) provide more effective training data?
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KiselevaGLPBK14.bib) "
	```
	@inproceedings{DBLP:conf/trec/KiselevaGLPBK14,
		author = {Julia Kiseleva and Alejandro Montes Garc{\'{\i}}a and Yongming Luo and Mykola Pechenizkiy and Paul De Bra and Jaap Kamps},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Applying Learning to Rank Techniques to Contextual Suggestions},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-eindhoven\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KiselevaGLPBK14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### User Modeling for Contextual Suggestion

_Hua Li, Rafael Alonso_

- :fontawesome-solid-user-group: **Participant:** [RAMA](./context/participants.md#rama)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-RAMA_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-RAMA_cs.pdf)
- :material-file-search: **Runs:** [RUN1](./context/runs.md#run1) | [RAMARUN2](./context/runs.md#ramarun2)

??? abstract "Abstract"
	
	This paper describes our work on the Contextual Suggestion Track of the Twenty-Third Text REtrieval Conference (TREC 2014). The key to our approach is user interest modeling. By building explicit models of user interests and information needs, we are able to make suggestions relevant to the user. We extended our Reinforcement and Aging Modeling Algorithm (RAMA) to create user interest models using the rated examples in a user profile as explicit relevance feedback. Two models, one for specific interests and the other for general interests, are built for each user profile. To ensure that the recommendations are contextually appropriate, we have also built a simple model to capture contextual relevance of a recommendation. Candidate suggestions are retrieved from the Yelp®1 website using its application programming interface. For each candidate, we calculate three component scores based on the specific interest model, the general interest model, and the context model, respectively. Final scoring and ranking are computed as a weighted linear combination of the component scores. We hypothesize that the relative weighting of the components may affect the performance of our system. To test the hypothesis, we have submitted two runs with different weighting schemes. In particular, RUN1 has a specific interest priority whereas RAMARUN2 has a general interest priority. TREC evaluation reveals that both runs performed significantly better than the median of all submitted runs (i.e., the Track Median) on three performance metrics. In addition, RAMARUN2 has a slight performance edge over RUN1. The effectiveness of our approach is evidenced by the TREC evaluation result that RAMARUN2 and RUN1 ranked #2 and #6 out of the 31 runs submitted by the 17 participating teams from around the world.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiA14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiA14,
		author = {Hua Li and Rafael Alonso},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {User Modeling for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-RAMA\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiA14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2014 Contextual Suggestion Track: Hybrid Recommendation  Based on Open-web Information

_Hanchen Li, Zhen Yang, Yingxu Lai, Lijuan Duan, Kefeng Fan_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./context/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BJUT_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BJUT_cs.pdf)
- :material-file-search: **Runs:** [BJUTa](./context/runs.md#bjuta) | [BJUTb](./context/runs.md#bjutb)

??? abstract "Abstract"
	
	In this paper we describe our efforts for TREC contextual suggestion task. Our goal of this year is to evaluate the effectiveness of: (1) Preference crawling method that as far as possible to obtain more candidate spots' information from open-web to model the users' interest profiles; (2) Automatic summarization method that leverages the information from multiple resources to generate the description for each candidate scenic spots; (3) Hybrid recommendation method that combing a variety of factors to construct a system of hybrid recommendation system. Finally, we conduct extensive experiments to evaluate the proposed framework on TREC 2014 Contextual Suggestion data set, and, as would be expected, the results demonstrate its generality and superior performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiYLDF14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiYLDF14,
		author = {Hanchen Li and Zhen Yang and Yingxu Lai and Lijuan Duan and Kefeng Fan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2014 Contextual Suggestion Track: Hybrid Recommendation Based on Open-web Information},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BJUT\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiYLDF14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Context Suggestion Track TREC 2014

_Zihao Lu, Zhijie Qiu, Liang Chang, Bingyang Liu, Dayong Wu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./context/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_cs.pdf)
- :material-file-search: **Runs:** [lda](./context/runs.md#lda) | [cat](./context/runs.md#cat)

??? abstract "Abstract"
	
	This year we did not use ClueWeb12 or ClueWeb12-B,while we solve this issue based on data we crawled from openweb.Firstly, we use external structured resource -Google Place API[1] to find all of the possible candidate places in the distance of 5 hours' drive. Secondly, we use Yandex[2] to find a description of each place because we get URL of the corresponding place. Then, we classifythe descriptions of all places. Finally, we ranked the pages based on users' preferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuQCLWLC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuQCLWLC14,
		author = {Zihao Lu and Zhijie Qiu and Liang Chang and Bingyang Liu and Dayong Wu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Context Suggestion Track {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuQCLWLC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC 2014 Contextual Suggestion Track

_Bilel Moulahi, Lynda Tamine, Sadok Ben Yahia_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./context/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-IRIT_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-IRIT_cs.pdf)
- :material-file-search: **Runs:** [choqrun](./context/runs.md#choqrun)

??? abstract "Abstract"
	
	In this work, we give an overview of our participation in the TREC 2014 Contextual Suggestion Track. To address the retrieval of attraction places, we propose a fuzzy-based document combination approach for preference learning and context processing. We use the open web in our submission and make use of both criteria users preferences and geographical location criteria.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoulahiTMY14.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoulahiTMY14,
		author = {Bilel Moulahi and Lynda Tamine and Sadok Ben Yahia},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IRIT} at {TREC} 2014 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-IRIT\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoulahiTMY14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Better Contextual Suggestions in ClueWeb12 Using Domain Knowledge  Inferred from The Open Web

_Thaer Samar, Arjen P. de Vries, Alejandro Bellogín_

- :fontawesome-solid-user-group: **Participant:** [CWI](./context/participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-CWI_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-CWI_cs.pdf)
- :material-file-search: **Runs:** [CWI_CW12_Full](./context/runs.md#cwi_cw12_full) | [CWI_CW12.MapWeb](./context/runs.md#cwi_cw12.mapweb)

??? abstract "Abstract"
	
	This paper provides an overview of our participation in the Contextual Suggestion Track. The TREC 2014 Contextual Suggestion Track allowed participants to submit personalized rankings using documents either from the Open Web or from an archived, static Web collection (ClueWeb12) collection. One of the main steps in recommending attractions for a particular user in a given context is the selection of the candidate documents. This task is more challenging when relying on ClueWeb12 collection rather than public tourist APIs for finding suggestions. In this paper, we present our approach for selecting candidate suggestions from the entire ClueWeb12 collection using the tourist domain knowledge available in the Open Web. We show that the generated recommendations to the provided user profiles and contexts improve significantly using this inferred domain knowledge.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SamarVB14.bib) "
	```
	@inproceedings{DBLP:conf/trec/SamarVB14,
		author = {Thaer Samar and Arjen P. de Vries and Alejandro Bellog{\'{\i}}n},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Better Contextual Suggestions in ClueWeb12 Using Domain Knowledge Inferred from The Open Web},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-CWI\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SamarVB14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at TREC 2014 Contextual Suggestion: Experiments  with suggestion clustering

_Luchen Tan, Adriel Dean-Hall, Pragnya Addala, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [waterloo_clarke](./context/participants.md#waterloo_clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-waterloo_clarke_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-waterloo_clarke_cs.pdf)
- :material-file-search: **Runs:** [waterlooA](./context/runs.md#waterlooa) | [waterlooB](./context/runs.md#waterloob)

??? abstract "Abstract"
	
	In this work we present our group's first attempt at developing a system to solve the problem presented in the contextual suggestion task. As part of TREC 2014 the contextual suggestion track is running for the third time. The goal of this task is to tailor point-of-interest suggestions to users according to this preferences. Here we present how we gathered candidate points-of-interest, grouped them according to similarity using clustering, and picked points-of-interest that each user would find especially appealing. The organizers of this track distributed users' personal profiles in three files: examples2014.csv, profiles2014-70.csv and profiles2014-100.csv. A list of 100 example points-of-interest, which each consist of an ID, a title, a description and a URL were included in examples2014.csv. 299 users indicated their preferences by giving a rating on a 5-point score (0, 1, 2, 3, 4) to the description and website of each example point-of-interest. 116 users, indicated preferences to all the 100 example points of interests, these profiles are distributed in profiles2014-100.csv. The other 183 users, only indicated 70% of all the example points of interest, these profiles are distributed in profiles2014-70.csv. There are 50 contexts which each represent a city in the United States which are listed in contexts2014.txt. Each group is permitted to submit up to 2 runs of suggested point of interests in the 50 contexts. Below we describe in detail our approach for building both of our runs
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TanDAC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/TanDAC14,
		author = {Luchen Tan and Adriel Dean{-}Hall and Pragnya Addala and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Waterloo at {TREC} 2014 Contextual Suggestion: Experiments with suggestion clustering},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-waterloo\_clarke\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TanDAC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploration of Opinion-aware Approach to Contextual Suggestion

_Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./context/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_cs.pdf)
- :material-file-search: **Runs:** [UDInfoCS2014_1](./context/runs.md#udinfocs2014_1) | [UDInfoCS2014_2](./context/runs.md#udinfocs2014_2)

??? abstract "Abstract"
	
	In this paper we describe our effort on TREC Contextual Suggestion Track. Using resources such as description or websites of example suggestions to build user profile has been proven to be effective on last year's TREC. This year we also leverage the power of using user profile. Real world opinions of the suggestions are used in our method to build both user profile and candidate suggestion profile. Two ranking method are investigated to rank the candidate suggestions: linear interpolation and learning to rank. For description generation, we apply the similar method as used in the last year. The structured description combines the category information of the suggestion, meta-description of the website, reviews of the suggestion and the similar example suggestions that the user liked. Official results of our submitted runs show the effectiveness of the proposed method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangF14.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangF14,
		author = {Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Exploration of Opinion-aware Approach to Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_fang\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangF14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Delaware at TREC 2014

_Ashraf Bah, Karankumar Sabhnani, Mustafa Zengin, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [udel](./context/participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf)
- :material-file-search: **Runs:** [run_DwD](./context/runs.md#run_dwd) | [run_FDwD](./context/runs.md#run_fdwd)

??? abstract "Abstract"
	
	This paper describes the work of the Information Retrieval Lab at the University of Delaware (team name “udel”) on TREC 2014 tracks. We participated in five different tracks: Contextual Suggestion, Federated Web, Microblog, Session, and Web.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BahSZC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/BahSZC14,
		author = {Ashraf Bah and Karankumar Sabhnani and Mustafa Zengin and Ben Carterette},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Delaware at {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_cs-federated-microblog-web-sesson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BahSZC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Modelling Psychological Needs for User-dependent Contextual Suggestion

_Di Xu, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [Group.Xu](./context/participants.md#group.xu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-Group.Xu_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-Group.Xu_cs.pdf)
- :material-file-search: **Runs:** [dixlticmu](./context/runs.md#dixlticmu)

??? abstract "Abstract"
	
	This paper presents our approach for the Contextual Suggestion track of 2014 Text REtrieval Conference (TREC). The task aims to provide recommendations on points of interests (POI) for various kinds of users under different contexts. This becomes challenging due to the limited amount of training data provided by TREC and the demanding constraints for a suggestion to be judged as relevant. Our approach does not deviate from existing Machine Learning based methods in principle, but sticks closely to the defined relevance judgement criteria, by focusing primarily on modelling users' preferences on POI categories, and investigating upon their psychological expectations on the textual descriptions of the POIs. The latter is considered as our novelty in this work. Support Vector Regression was used for suggestion ranking, an ad-hoc web information extractor was used to collect POI descriptions, and a description evaluation mechanism was engaged to select proper POI descriptions subject to the nature of the POIs. Our results suggest that our methods are effective in obtaining satisfying user-specific POI rankings and generating descriptions that meet users' psychological expectations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuC14,
		author = {Di Xu and Jamie Callan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Modelling Psychological Needs for User-dependent Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-Group.Xu\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2014: Web, Session, and Contextual Suggestion Tracks

_Matthias Hagen, Steve Goering, Maximilian Michel, Georg Müller, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [BUW](./context/participants.md#buw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BUW_cs-session-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BUW_cs-session-web.pdf)
- :material-file-search: **Runs:** [webis_1](./context/runs.md#webis_1) | [webis_2](./context/runs.md#webis_2)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2014 Web, Session and Contextual Suggestion tracks. All our runs for the Web and the Session track are on the full ClueWeb12 and use the online Indri retrieval system hosted at CMU. Our runs for the Contextual Suggestion track are based on the open web. As for the Web track, our runs are aimed at one research question: whether using axioms for re-ranking a baseline result list improve the retrieval performance. Therefore, we implement the axioms available in the axiomatic IR literature and combine them with new axioms aimed at term proximity. Trained on the TREC 2013 Web track data, three promising combinations of axioms are identified in a large-scale experiment and used for our three runs. As for the session track, we tackle three research questions in three different runs. First, similar to the Web track, we examine whether an axiom combination helps to improve session retrieval. Second, we examine the effect of presenting relevant documents from previous years when they seem to be related to the current queries of the 2014 data. Our third question is whether the user interactions can be used to train an activation model to predict relevant documents for new queries. As for the contextual suggestion track, our research question is whether explanations based on the user profile and explaining why specific entities are suggested by the system are perceived positively or negatively by the user. Our focus is not explicitly on finding the most relevant suggestions but rather on examining the effect of different descriptions. Thus, the system for finding the suggestions is simply based on techniques shown promising in the previous years. Our first run uses “standard” descriptions while in the second run the standard description is enriched by a profile specific sentence explaining the reasoning underlying the suggestion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenGMMS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenGMMS14,
		author = {Matthias Hagen and Steve Goering and Maximilian Michel and Georg M{\"{u}}ller and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2014: Web, Session, and Contextual Suggestion Tracks},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BUW\_cs-session-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenGMMS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Venue Recommendation and Web Search Based on Anchor Text

_Seyyed Hadi Hashemi, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./context/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UAmsterdam_cs-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UAmsterdam_cs-web.pdf)
- :material-file-search: **Runs:** [Model1](./context/runs.md#model1) | [Model0](./context/runs.md#model0)

??? abstract "Abstract"
	
	This paper presents the University of Amsterdam's participation in TREC 2014. For the Contextual Suggestion Track, we experimented with the use of anchor text representations in the language modeling framework, and base our runs either on full ClueWeb12 or the subset of touristic aggregators (e.g., tripadvisor) provided by the organizers of the track. We also look at the effectiveness of priors (in particular, PageRank) and ways of formulating the query based on the context. Our main finding is that the anchor text representation is effective for retrieving candidate attractions, and performs better than a standard document text index. A linear combination of both anchor and document text leads to further improvement. For the Web Track, we continued our experiment with the fusion of anchor text relative to the text-based baseline run. Our main finding is, again, that the combination of anchor and document text leads to improvement, and we demonstrate how the fusion weight can be used as a handle to tune the amount of risk acceptable for the risk sensitive evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HashemiK14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HashemiK14,
		author = {Seyyed Hadi Hashemi and Jaap Kamps},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Venue Recommendation and Web Search Based on Anchor Text},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UAmsterdam\_cs-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HashemiK14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2014: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Web Tracks

_Richard McCreadie, Romain Deveaud, M-Dyaa Albakour, Stuart Mackie, Nut Limsopatham, Craig Macdonald, Iadh Ounis, Thibaut Thonet, Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./context/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-uogTr_cs-ts-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-uogTr_cs-ts-web.pdf)
- :material-file-search: **Runs:** [uogTrBunSumF](./context/runs.md#uogtrbunsumf) | [uogTrCsLtrF](./context/runs.md#uogtrcsltrf)

??? abstract "Abstract"
	
	In TREC 2014, we focus on tackling the challenges posed by the Contextual Suggestion and Temporal Summarisation tracks, as well as enhancing our existing technologies to tackle risk-sensitivity as part of the Web track, building upon our Terrier Information Retrieval Platform. In particular, for the Contextual Suggestion track, we propose a novel bundled venue retrieval approach and experiment with text-based summarisation for building the venue description. For our participation to the Temporal Summarisation track, we propose a general framework for performing summarisation over time and two new real-time filtering approaches that leverage the semi-structured nature of news articles to enhance summary coverage. For the TREC Web track, we investigated a novel risk-sensitive learning to rank approach that is based on hypothesis testing and examined approaches that selectively apply different retrieval techniques based upon the query, with the aim of minimising risk.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieDAMLMO14.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieDAMLMO14,
		author = {Richard McCreadie and Romain Deveaud and M{-}Dyaa Albakour and Stuart Mackie and Nut Limsopatham and Craig Macdonald and Iadh Ounis and Thibaut Thonet and Bekir Taner Din{\c{c}}er},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow at {TREC} 2014: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Web Tracks},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-uogTr\_cs-ts-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieDAMLMO14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Microblog 

#### Overview of the TREC-2014 Microblog Track

_Jimmy Lin, Yulu Wang, Miles Efron, Garrick Sherman_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec23/papers/overview-microblog.pdf](https://trec.nist.gov/pubs/trec23/papers/overview-microblog.pdf)
??? abstract "Abstract"
	
	This year represents the fourth iteration of the TREC Microblog track, which has been running since 2011. The track continued using the “evaluation as a service” model [8, 7], in which participants had access to the document collection only through an API. In addition to the temporally-anchored ad hoc retrieval task, which has been running since the inception of the track, we introduced a new task called tweet timeline generation (TTG), where the goal is to produce concise “summaries” about a particular topic for human consumption. Although this overview covers both tasks, more emphasis is placed on the tweet timeline generation task, which necessitated the development of a new evaluation methodology. We refer the reader to previous track overview papers [8, 12, 9] for details on the setup of the ad hoc task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinWES14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinWES14,
		author = {Jimmy Lin and Yulu Wang and Miles Efron and Garrick Sherman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC-2014} Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {https://trec.nist.gov/pubs/trec23/papers/overview-microblog.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinWES14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Microblog Track in TREC 2014

_Guoxin Cui, Fabin Shi, Xiaolei Liu, Xiaobo Hao, Xueke Xu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./microblog/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_microblog.pdf)
- :material-file-search: **Runs:** [ICTNETRUN1](./microblog/runs.md#ictnetrun1) | [ICTNETRUN2](./microblog/runs.md#ictnetrun2) | [ICTNETRUN3](./microblog/runs.md#ictnetrun3) | [ICTNETRUN4](./microblog/runs.md#ictnetrun4) | [ICTNETRUNSP4](./microblog/runs.md#ictnetrunsp4) | [ICTNETRunSP3](./microblog/runs.md#ictnetrunsp3) | [ICTNETAP3](./microblog/runs.md#ictnetap3) | [ICTNETAP4](./microblog/runs.md#ictnetap4)

??? abstract "Abstract"
	
	Microblog track was first introduced in 2011 and we have participated in this task for 4 years [1,2,5]. This year's microblog track has two tasks. The first one, namely ad-hoc search task, is the same as usual. This task needs to retrieve all the tweets that are relevant to query Q before time T. Participants can access the corpus by official APIs. The second task is Tweet Timeline Generation(TTG) task. It is newly introduced this year and the main goal of it is to detect and remove the redundant tweets the first task retrieves. This report is organized as follows. Section 2 mainly focuses on the data preparation. Section 3 is our methodology and framework of the ad-hoc search task. Section 4 focuses on the methodology of TTG task. Section 5 gives the final results of the two tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CuiSLHXLC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/CuiSLHXLC14,
		author = {Guoxin Cui and Fabin Shi and Xiaolei Liu and Xiaobo Hao and Xueke Xu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Microblog Track in {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CuiSLHXLC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Pittsburgh at TREC 2014 Microblog Track

_Zheng Gao, Rui Bi_

- :fontawesome-solid-user-group: **Participant:** [zhg15](./microblog/participants.md#zhg15)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-zhg15_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-zhg15_microblog.pdf)
- :material-file-search: **Runs:** [Upitt](./microblog/runs.md#upitt) | [NewBee](./microblog/runs.md#newbee)

??? abstract "Abstract"
	
	An ad hoc retrieval task aims at return the most relevant documents based on a particular query. And high precision and recall always depends on clear query and elaborative documents. If the query is ambiguous while document is short and general, common retrieval models may not work well on the feedback. In this way, more expansive information will be needed to add in order to implement original queries and documents. That is the main purpose of microblog track of 2014 TREC Conference. The paper describes the first participation of University of Pittsburgh in 2014 TREC microblog track. The data is based on tweet collection which gathered in 2013. We got two runs for the final results which are base on BM25 feedback algorithm. The details of our retrieval model include query expansion, document expansion and retrieval model for the final rank.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaoB14.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaoB14,
		author = {Zheng Gao and Rui Bi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Pittsburgh at {TREC} 2014 Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-zhg15\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaoB14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QU at TREC-2014: Online Clustering with Temporal and Topical Expansion  for Tweet Timeline Generation

_Maram Hasanain, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./microblog/participants.md#qu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-QU_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-QU_microblog.pdf)
- :material-file-search: **Runs:** [QUQueryExp5D25T](./microblog/runs.md#ququeryexp5d25t) | [QUTmpDecay](./microblog/runs.md#qutmpdecay) | [QUTQRM](./microblog/runs.md#qutqrm) | [QUQueryExp10D15](./microblog/runs.md#ququeryexp10d15) | [QUQEd5t25TTgBL](./microblog/runs.md#quqed5t25ttgbl) | [QUTqrmTTgBL](./microblog/runs.md#qutqrmttgbl) | [QUQEd10t15TTgCL](./microblog/runs.md#quqed10t15ttgcl) | [QUTmpDecayTTgCL](./microblog/runs.md#qutmpdecayttgcl)

??? abstract "Abstract"
	
	In this work, we present our participation in the microblog track in TREC-2014, building upon our first participation last year. We present our approaches for the two tasks of this year: temporally-anchored ad-hoc search and tweet timeline generation. For the ad-hoc search task, we used topical expansion in addition to temporal models to perform retrieval. Our results show that our run based on the typical pseudo relevance feedback query expansion outperformed all of our other runs with a relatively high mean average precision (MAP). As for the timeline generation task, we approached this problem using online incremental clustering of tweets retrieved for a given query. Our approach allows the dynamic creation of “semantic” clusters while providing a framework for detecting redundant tweets and selecting representative ones to be added to the final timeline. The results demonstrate that using incremental clustering of tweets retrieved through a temporal retrieval model produced the best effectiveness among the submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HasanainE14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HasanainE14,
		author = {Maram Hasanain and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{QU} at {TREC-2014:} Online Clustering with Temporal and Topical Expansion for Tweet Timeline Generation},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-QU\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HasanainE14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HU DB at TREC 2014 Microblog Track

_Jennifer Klein, Yishai Oltchik, Nerya Or, Sara Cohen_

- :fontawesome-solid-user-group: **Participant:** [HU_DB](./microblog/participants.md#hu_db)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-HU_DB_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-HU_DB_microblog.pdf)
- :material-file-search: **Runs:** [SRTD](./microblog/runs.md#srtd) | [SR](./microblog/runs.md#sr) | [SRTL](./microblog/runs.md#srtl) | [Standard](./microblog/runs.md#standard) | [StandardAH](./microblog/runs.md#standardah) | [SRTLAH](./microblog/runs.md#srtlah) | [SRAH](./microblog/runs.md#srah) | [SRTDAH](./microblog/runs.md#srtdah)

??? abstract "Abstract"
	
	This paper describes our system for the Tweet Timeline Generation (TTG) task of the Microblog track, at the Text Retrieval Conference (TREC) 2014. Intuitively, given a collection of microblog posts (i.e., tweets), and a keyword query Q, the goal is to generate a timeline of related tweets. Such a timeline consists of representative tweets, relevant to Q. In our system we employ query expansion to identify highly relevant tweets, and then use affinity propagation to cluster the tweets, based on their word similarity, hashtag similarity and temporal similarity. We then return a representative tweet from each cluster. The result is a system with relatively good precision, but, unfortunately, poor recall. We discuss the techniques employed, as well as the insights gleaned while developing and testing our system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KleinOOC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/KleinOOC14,
		author = {Jennifer Klein and Yishai Oltchik and Nerya Or and Sara Cohen},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{HU} {DB} at {TREC} 2014 Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-HU\_DB\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KleinOOC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Siena's Twitter Information Retrieval System: The 2014 Microblog Track

_Timothy LaRock, Lauren Mathews, Matthew Roberts, Darren Lim, Sharon G. Small_

- :fontawesome-solid-user-group: **Participant:** [SCIAITeam](./microblog/participants.md#sciaiteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-SCIAITeam_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-SCIAITeam_microblog.pdf)
- :material-file-search: **Runs:** [SCIAI3am14a](./microblog/runs.md#sciai3am14a) | [SCIAI14a](./microblog/runs.md#sciai14a) | [SCIAI124a](./microblog/runs.md#sciai124a) | [SCIAI3am14aTTG](./microblog/runs.md#sciai3am14attg) | [SCIAI14aTTG](./microblog/runs.md#sciai14attg) | [SCIAI124aTTG](./microblog/runs.md#sciai124attg) | [SCIAI3cm4aTTG](./microblog/runs.md#sciai3cm4attg) | [SCIAI3cm4a](./microblog/runs.md#sciai3cm4a)

??? abstract "Abstract"
	
	As the internet dramatically changes each year, microblogs - such as Facebook and Twitter - are being used more often as a source of information exchange. Twitter users are learning about current events earlier compared to reading about it on their news feeds, as companies and celebrities continue to utilize Twitter to spread information. Information Retrieval, a topic which NIST (National Institute of Standards and Technology) holds a conference for every year, involves utilizing such online environments, like microblogs, to grab as much information from these sources to find if the information can be put towards a purpose. The Microblog Track was originally introduced to TREC2 (Text REtrieval Conference) in 2011, and selected Twitter3 as its microblog resource. Twitter allows its users to share short, 140 character length posts with their followers, and is often used to share anything from fashion trends to the latest terrorist attacks. Due to the short length of tweets, users often utilize other ways to share more information, such as including links or images with their tweets, which has an effect on the tweet containing relevant information. Participating groups for the track were given access to a Twitter API, provided by TREC, containing a corpus of 243 million tweets scrapped from February 1st to March 31st, 2013. Each group was given a set of test topics in which to test their system, which return results for the Adhoc and/or Tweet Timeline Generation Task (TTG). In this paper, we describe five Query Expansion modules and three Relevance modules designed for the microblog track, built within STIRS. Our precision results for our adhoc run shows STIRS' average to be at 61.91% precision, with our average TTG at 85.38% precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LaRockMRLS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LaRockMRLS14,
		author = {Timothy LaRock and Lauren Mathews and Matthew Roberts and Darren Lim and Sharon G. Small},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Siena's Twitter Information Retrieval System: The 2014 Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-SCIAITeam\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LaRockMRLS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept Based Tie-breaking and Maximal Marginal Relevance Retrieval  in Microblog Retrieval

_Kuang Lu, Hui Fang, Diego Roa_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./microblog/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_microblog.pdf)
- :material-file-search: **Runs:** [UDInfoTB](./microblog/runs.md#udinfotb) | [UDInfoTBRR](./microblog/runs.md#udinfotbrr) | [UDInfoQE](./microblog/runs.md#udinfoqe) | [UDInfoLTR](./microblog/runs.md#udinfoltr) | [UDInfoMMRA](./microblog/runs.md#udinfommra) | [UDInfoMMR5](./microblog/runs.md#udinfommr5) | [UDInfoMMRWCA](./microblog/runs.md#udinfommrwca) | [UDInfoMMRWC5](./microblog/runs.md#udinfommrwc5)

??? abstract "Abstract"
	
	There are enormous tweets posted on any given day, and the number keeps increasing. As a result, the needs of effectively retrieving tweets depending upon user's information need, and summarizing tweets per-taining to a given topic have become increasingly important. In this paper, Wikipedia concepts [1] was introduced in tie-breaking to perform ad-hoc microblog retrieval. The Maximal Marginal Relevance (MMR) [2] criterion is deployed to summarize relevant tweets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuFR14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuFR14,
		author = {Kuang Lu and Hui Fang and Diego Roa},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Concept Based Tie-breaking and Maximal Marginal Relevance Retrieval in Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_fang\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuFR14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKUICST at TREC 2014 Microblog Track: Feature Extraction for Effective  Microblog Search and Adaptive Clustering Algorithms for TTG

_Chao Lv, Feifan Fan, Runwei Qiang, Yue Fei, Jianwu Yang_

- :fontawesome-solid-user-group: **Participant:** [PKUICST](./microblog/participants.md#pkuicst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-PKUICST_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-PKUICST_microblog.pdf)
- :material-file-search: **Runs:** [PKUICST1](./microblog/runs.md#pkuicst1) | [PKUICST2](./microblog/runs.md#pkuicst2) | [PKUICST3](./microblog/runs.md#pkuicst3) | [PKUICST4](./microblog/runs.md#pkuicst4) | [TTGPKUICST1](./microblog/runs.md#ttgpkuicst1) | [TTGPKUICST2](./microblog/runs.md#ttgpkuicst2) | [TTGPKUICST3](./microblog/runs.md#ttgpkuicst3) | [TTGPKUICST4](./microblog/runs.md#ttgpkuicst4)

??? abstract "Abstract"
	
	This paper describes our approaches to temporally-anchored ad hoc retrieval task and tweet timeline generation (TTG) task in the TREC 2014 Microblog track. In the ad hoc search, we apply a learning to rank framework which utilizes not only the various content relevance of a tweet, but also the quality of a tweet. External evidences are well incorporated in our approach with Web-based query expansion and document expansion techniques. In the TTG task, we apply star clustering and hierarchical clustering algorithm on the retrieved tweets from ad hoc retrieval task. Experimental results show that our learning to rank methods with many state-of-the-art features achieve good retrieval performance with respect to MAP and P@30 metrics. Besides, our systems for TTG task also obtain convincing recall and precision scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LvFQFY14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LvFQFY14,
		author = {Chao Lv and Feifan Fan and Runwei Qiang and Yue Fei and Jianwu Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{PKUICST} at {TREC} 2014 Microblog Track: Feature Extraction for Effective Microblog Search and Adaptive Clustering Algorithms for {TTG}},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-PKUICST\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LvFQFY14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCAS at TREC-2014 Microblog Track

_Qingli Ma, Ben He, Dongxing Li_

- :fontawesome-solid-user-group: **Participant:** [UCAS](./microblog/participants.md#ucas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UCAS-microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UCAS-microblog.pdf)
- :material-file-search: **Runs:** [UCASRun1](./microblog/runs.md#ucasrun1) | [UCASRun3](./microblog/runs.md#ucasrun3) | [UCASRun2](./microblog/runs.md#ucasrun2) | [UCASRun4](./microblog/runs.md#ucasrun4)

??? abstract "Abstract"
	
	University of Chinese Academy of Sciences (UCAS) participated in the first task, namely temporally-anchored ad hoc retrieval in Microblog track, aiming to efficiently and effectively retrieve tweets. Based on the conventional application of learning to rank, we incorporated a machine learning approach, such as logistic regression for selecting high-quality training data for improving the effectiveness. Except for the tweets' content features, we also used the features of the web information, external evidence, which is related with the URLS to improve the effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaHL14.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaHL14,
		author = {Qingli Ma and Ben He and Dongxing Li},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UCAS} at {TREC-2014} Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UCAS-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MaHL14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QCRI at TREC 2014: Applying the KISS principle for the TTG  task in the Microblog Track

_Walid Magdy, Wei Gao, Tarek El-Ganainy, Zhongyu Wei_

- :fontawesome-solid-user-group: **Participant:** [QCRI](./microblog/participants.md#qcri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-QCRI_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-QCRI_microblog.pdf)
- :material-file-search: **Runs:** [EM50](./microblog/runs.md#em50) | [EM100](./microblog/runs.md#em100) | [SM100](./microblog/runs.md#sm100) | [SM50](./microblog/runs.md#sm50) | [HPRF1020RR](./microblog/runs.md#hprf1020rr) | [HPRF1020](./microblog/runs.md#hprf1020) | [PRF1030RR](./microblog/runs.md#prf1030rr) | [PRF1030](./microblog/runs.md#prf1030)

??? abstract "Abstract"
	
	In this paper we present our work on the ad-hoc search and the tweet timeline generation (TTG) tasks of TREC-2014 Microblog track. Regarding the ad-hoc search task, we used our best developed system over the last year, which include hyperlink-based query expansion and re-ranking models fusion. For the new tweet timeline generation task, we applied a straightforward and simple approach, which depends on clustering retrieval results based on Jaccard similarities between tweets. Our best adhoc results achieved the fifth rank and seventh rank among 21 participating groups when evaluated using P@30 and MAP respectively. However, our best TTG run achieved the second rank among participants, which shows that our simple TTG approach was more effective than most of the used TTG systems in TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MagdyGEW14.bib) "
	```
	@inproceedings{DBLP:conf/trec/MagdyGEW14,
		author = {Walid Magdy and Wei Gao and Tarek El{-}Ganainy and Zhongyu Wei},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{QCRI} at {TREC} 2014: Applying the {KISS} principle for the {TTG} task in the Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-QCRI\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MagdyGEW14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NovaSearch at TREC 2014 Microblog Track: Reranking with Wikipedia  Page Views

_Flávio Martins, João Magalhães_

- :fontawesome-solid-user-group: **Participant:** [NovaSearch](./microblog/participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-NovaSearch_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-NovaSearch_microblog.pdf)
- :material-file-search: **Runs:** [NovaRun1](./microblog/runs.md#novarun1) | [NovaRun2](./microblog/runs.md#novarun2) | [NovaRun0](./microblog/runs.md#novarun0)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2014 Microblog real-time search task. We investigate whether page views from Wikipedia can be used successfully to estimate relevant time periods for queries. To this end, we use a recently published temporal reranking method by Efron et al. [2], which uses kernel density estimation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MartinsM14.bib) "
	```
	@inproceedings{DBLP:conf/trec/MartinsM14,
		author = {Fl{\'{a}}vio Martins and Jo{\~{a}}o Magalh{\~{a}}es},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {NovaSearch at {TREC} 2014 Microblog Track: Reranking with Wikipedia Page Views},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-NovaSearch\_microblog.pdf},
		timestamp = {Thu, 14 May 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MartinsM14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UWM-HBUT at TREC 2014 Microblog Track: Using Query Expansion (QE)  and Event Identification Algorithm (EIA) to improve microblog retrieval  effectiveness

_Sukjin You, Xiangming Mu, Wei Huang_

- :fontawesome-solid-user-group: **Participant:** [UWM.HBUT](./microblog/participants.md#uwm.hbut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UWM-HBUT_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UWM-HBUT_microblog.pdf)
- :material-file-search: **Runs:** [UWMHBUT1](./microblog/runs.md#uwmhbut1) | [UWMHBUT2](./microblog/runs.md#uwmhbut2) | [UWMHBUT3](./microblog/runs.md#uwmhbut3) | [UWMHBUT4](./microblog/runs.md#uwmhbut4)

??? abstract "Abstract"
	
	This paper reports our contributions and results to TREC 2014 Microblog Track. Different from traditional web pages or database documents, microblogs have their own unique features. Considering sensitivity to time, we introduce a new factor to help to improve tweet retrieval effectiveness. The ranking score of a retrieved tweet is adjusted by considering how close the tweet time stamp is to the event using Event Identification Algorithm (EIA). In addition, we also evaluate the Query Expansion (QE) approach using Google as an external data corpus. There are 55 search topics and the data set contains a total of 243 million tweets provided by the TREC 2014 Microblog Track. Our initial results indicated that QE helped to improve the performance. We also discussed why the EIA approach failed to enhance the retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YouMH14.bib) "
	```
	@inproceedings{DBLP:conf/trec/YouMH14,
		author = {Sukjin You and Xiangming Mu and Wei Huang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UWM-HBUT} at {TREC} 2014 Microblog Track: Using Query Expansion {(QE)} and Event Identification Algorithm {(EIA)} to improve microblog retrieval effectiveness},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UWM-HBUT\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YouMH14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Estimating Semantic Similarity between Expanded Query and Tweet Content  for Microblog Retrieval

_Zhihua Zhang, Man Lan_

- :fontawesome-solid-user-group: **Participant:** [ECNUCS](./microblog/participants.md#ecnucs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ECNU_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ECNU_microblog.pdf)
- :material-file-search: **Runs:** [ECNURankLib](./microblog/runs.md#ecnuranklib) | [ECNURankLib2013](./microblog/runs.md#ecnuranklib2013) | [ECNUSVM](./microblog/runs.md#ecnusvm) | [ECNUSVM2013](./microblog/runs.md#ecnusvm2013)

??? abstract "Abstract"
	
	This paper reports the systems we submitted to the Microblog Track shared in TREC 2014 which focuses on ad hoc retrieval (i.e., retrieving top 1, 000 relevant tweet for every given topic). To address this task, we adopted a two-stage framework, i.e., firstly, we performed query expansion (i.e., expanding relevant inforamtion using pseudo-relevance feedback and Google search engine results) to retrieve more relevant tweets, then extracted several effective semantic features (e.g., Jansen-Shannon Distance, Overlap Similarity, Lucene Score, etc) from retrieved results and built ranking model using supervised machine learning algorithms with the aid of these features to perform re-ranking. Our systems ranked 3th out of 21 teams.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangL14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangL14,
		author = {Zhihua Zhang and Man Lan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Estimating Semantic Similarity between Expanded Query and Tweet Content for Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ECNU\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangL14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2014 Microblog Track

_Guangyuan Zhang, Zhen Yang, Shuyong Si_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./microblog/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BJUT_microblog.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BJUT_microblog.pdf)
- :material-file-search: **Runs:** [NCOS](./microblog/runs.md#ncos) | [NSIM](./microblog/runs.md#nsim) | [OSIM](./microblog/runs.md#osim)

??? abstract "Abstract"
	
	This paper describes the second participation of BJUT in the TREC Micro-blog Track. Two tasks are proposed in this year, including ad hoc search task and tweet timeline generation task. We attended the first task and focused on the method for re-ranking of the returned search results. Specifically, a graph-based method is proposed to re-rank the twitters returned by the official API, namely we re-rank the results by detecting whether some given characteristics are existing or not. Also, we introduce the details of our system, which consists of data preprocessing, system structure, and rank method & results analysis module.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangYS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangYS14,
		author = {Guangyuan Zhang and Zhen Yang and Shuyong Si},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2014 Microblog Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BJUT\_microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangYS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Delaware at TREC 2014

_Ashraf Bah, Karankumar Sabhnani, Mustafa Zengin, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [udel](./microblog/participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf)
- :material-file-search: **Runs:** [udelRunAH](./microblog/runs.md#udelrunah) | [udelRunTTG1](./microblog/runs.md#udelrunttg1) | [udelRunTTG2](./microblog/runs.md#udelrunttg2) | [udelRunTTG3](./microblog/runs.md#udelrunttg3) | [udelRunTTG4](./microblog/runs.md#udelrunttg4)

??? abstract "Abstract"
	
	This paper describes the work of the Information Retrieval Lab at the University of Delaware (team name “udel”) on TREC 2014 tracks. We participated in five different tracks: Contextual Suggestion, Federated Web, Microblog, Session, and Web.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BahSZC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/BahSZC14,
		author = {Ashraf Bah and Karankumar Sabhnani and Mustafa Zengin and Ben Carterette},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Delaware at {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_cs-federated-microblog-web-sesson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BahSZC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HLTCOE at TREC 2014: Microblog and Clinical Decision Support

_Tan Xu, Douglas W. Oard, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [hltcoe](./microblog/participants.md#hltcoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-hltcoe_microblog-clinical.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-hltcoe_microblog-clinical.pdf)
- :material-file-search: **Runs:** [hltcoe0](./microblog/runs.md#hltcoe0) | [hltcoe1](./microblog/runs.md#hltcoe1) | [hltcoe2](./microblog/runs.md#hltcoe2) | [hltcoe3](./microblog/runs.md#hltcoe3) | [hltcoeTTG0](./microblog/runs.md#hltcoettg0) | [hltcoeTTG1](./microblog/runs.md#hltcoettg1) | [hltcoeTTG2](./microblog/runs.md#hltcoettg2) | [hltcoeTTG3](./microblog/runs.md#hltcoettg3)

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

## Web 

#### TREC 2014 Web Track Overview

_Kevyn Collins-Thompson, Craig Macdonald, Paul N. Bennett, Fernando Diaz, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/overview-web.pdf](http://trec.nist.gov/pubs/trec23/papers/overview-web.pdf)
??? abstract "Abstract"
	
	The goal of the TREC Web track over the past few years has been to explore and evaluate innovative retrieval approaches over large-scale subsets of the Web - currently using ClueWeb12, on the order of one billion pages. For TREC 2014, the sixth year of the Web track, we implemented the following significant updates compared to 2013. First, the risk-sensitive retrieval task was modified to assess the ability of systems to adaptively perform risk-sensitive retrieval against multiple baselines, including an optional self-provided baseline. In general, the risk-sensitive task explores the tradeoffs that systems can achieve between effectiveness (overall gains across queries) and robustness (minimizing the probability of significant failure, relative to a particular provided baseline). Second, we added query performance prediction as an optional aspect of the risk-sensitive task. The Adhoc task continued as for TREC 2013, evaluated using both adhoc and diversity rel- evance criteria. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Collins-Thompson14.bib) "
	```
	@inproceedings{DBLP:conf/trec/Collins-Thompson14,
		author = {Kevyn Collins{-}Thompson and Craig Macdonald and Paul N. Bennett and Fernando Diaz and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2014 Web Track Overview},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/overview-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Collins-Thompson14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SNUMedinfo at TREC Web track 2014

_Sungbin Choi, Jinwook Choi_

- :fontawesome-solid-user-group: **Participant:** [SNUMedinfo](./web/participants.md#snumedinfo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-SNUMedinfo_web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-SNUMedinfo_web.pdf)
- :material-file-search: **Runs:** [SNUMedinfo11](./web/runs.md#snumedinfo11) | [SNUMedinfo12](./web/runs.md#snumedinfo12) | [SNUMedinfo13](./web/runs.md#snumedinfo13)

??? abstract "Abstract"
	
	This paper describes the participation of the SNUMedinfo team at the TREC Web track 2014. This is the first time we participate in the Web track. Rather than applying more sophisticated retrieval method such as learning to rank models, this year we used only baseline retrieval models with spam filtering and pagerank prior
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChoiC14a.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChoiC14a,
		author = {Sungbin Choi and Jinwook Choi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {SNUMedinfo at {TREC} Web track 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-SNUMedinfo\_web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChoiC14a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2014: Web, Session, and Contextual Suggestion Tracks

_Matthias Hagen, Steve Goering, Maximilian Michel, Georg Müller, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [BUW](./web/participants.md#buw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BUW_cs-session-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BUW_cs-session-web.pdf)
- :material-file-search: **Runs:** [webisWt14axAll](./web/runs.md#webiswt14axall) | [webisWt14axMax](./web/runs.md#webiswt14axmax) | [webisWt14axSyn](./web/runs.md#webiswt14axsyn)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2014 Web, Session and Contextual Suggestion tracks. All our runs for the Web and the Session track are on the full ClueWeb12 and use the online Indri retrieval system hosted at CMU. Our runs for the Contextual Suggestion track are based on the open web. As for the Web track, our runs are aimed at one research question: whether using axioms for re-ranking a baseline result list improve the retrieval performance. Therefore, we implement the axioms available in the axiomatic IR literature and combine them with new axioms aimed at term proximity. Trained on the TREC 2013 Web track data, three promising combinations of axioms are identified in a large-scale experiment and used for our three runs. As for the session track, we tackle three research questions in three different runs. First, similar to the Web track, we examine whether an axiom combination helps to improve session retrieval. Second, we examine the effect of presenting relevant documents from previous years when they seem to be related to the current queries of the 2014 data. Our third question is whether the user interactions can be used to train an activation model to predict relevant documents for new queries. As for the contextual suggestion track, our research question is whether explanations based on the user profile and explaining why specific entities are suggested by the system are perceived positively or negatively by the user. Our focus is not explicitly on finding the most relevant suggestions but rather on examining the effect of different descriptions. Thus, the system for finding the suggestions is simply based on techniques shown promising in the previous years. Our first run uses “standard” descriptions while in the second run the standard description is enriched by a profile specific sentence explaining the reasoning underlying the suggestion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenGMMS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenGMMS14,
		author = {Matthias Hagen and Steve Goering and Maximilian Michel and Georg M{\"{u}}ller and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2014: Web, Session, and Contextual Suggestion Tracks},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BUW\_cs-session-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenGMMS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Venue Recommendation and Web Search Based on Anchor Text

_Seyyed Hadi Hashemi, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./web/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UAmsterdam_cs-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UAmsterdam_cs-web.pdf)

??? abstract "Abstract"
	
	This paper presents the University of Amsterdam's participation in TREC 2014. For the Contextual Suggestion Track, we experimented with the use of anchor text representations in the language modeling framework, and base our runs either on full ClueWeb12 or the subset of touristic aggregators (e.g., tripadvisor) provided by the organizers of the track. We also look at the effectiveness of priors (in particular, PageRank) and ways of formulating the query based on the context. Our main finding is that the anchor text representation is effective for retrieving candidate attractions, and performs better than a standard document text index. A linear combination of both anchor and document text leads to further improvement. For the Web Track, we continued our experiment with the fusion of anchor text relative to the text-based baseline run. Our main finding is, again, that the combination of anchor and document text leads to improvement, and we demonstrate how the fusion weight can be used as a handle to tune the amount of risk acceptable for the risk sensitive evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HashemiK14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HashemiK14,
		author = {Seyyed Hadi Hashemi and Jaap Kamps},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Venue Recommendation and Web Search Based on Anchor Text},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UAmsterdam\_cs-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HashemiK14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Entity Came to Rescue - Leveraging Entities to Minimize Risks in Web  Search

_Xitong Liu, Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./web/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_web.pdf)
- :material-file-search: **Runs:** [UDInfoWebLES](./web/runs.md#udinfowebles) | [UDInfoWebENT](./web/runs.md#udinfowebent) | [UDInfoWebAX](./web/runs.md#udinfowebax) | [UDInfoWebRiskRM](./web/runs.md#udinfowebriskrm) | [UDInfoWebRiskTR](./web/runs.md#udinfowebrisktr) | [UDInfoWebRiskAX](./web/runs.md#udinfowebriskax)

??? abstract "Abstract"
	
	We present the summary of our work in the TREC 2014 Web Track. We participated both the ad hoc task and risk-sensitive task and explored two entity-based approaches to evaluate the performance of leveraging entities to improve retrieval effectiveness and robustness. Our proposed approaches are based on the integration of related entities of queries and the entity model from knowledge base to the retrieval model. The first approach is called as entity-centric query expansion, in which we integrate the related entities into the original query model to perform query expansion. Documents are then retrieved based on the expanded query model. In the second approach, we leverage the publicly available Freebase annotation on ClueWeb12 as well as Freebase API to estimate the entity model. It is called Latent Entity Space (LES), in which we model the relevance between query and document in a latent space. Each dimension of the latent space is represented by an entity and the query-document relevance is estimated based on their projections to each dimension. The evaluation results on ad hoc task show that entities can indeed bring further improvements on the performance of Web document retrieval when combined with axiomatic retrieval model with semantic expansion, one of the state-of-the-art methods. Furthermore, results on risk-sensitive task demonstrate that our proposed model also have advantage on minimizing the retrieval risk.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuYF14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuYF14,
		author = {Xitong Liu and Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Entity Came to Rescue - Leveraging Entities to Minimize Risks in Web Search},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_fang\_web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuYF14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2014: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Web Tracks

_Richard McCreadie, Romain Deveaud, M-Dyaa Albakour, Stuart Mackie, Nut Limsopatham, Craig Macdonald, Iadh Ounis, Thibaut Thonet, Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./web/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-uogTr_cs-ts-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-uogTr_cs-ts-web.pdf)
- :material-file-search: **Runs:** [uogTrDwl](./web/runs.md#uogtrdwl) | [uogTrIwa](./web/runs.md#uogtriwa) | [uogTrq1](./web/runs.md#uogtrq1) | [uogTrDwsts](./web/runs.md#uogtrdwsts) | [uogTrDuax](./web/runs.md#uogtrduax) | [uogTrBwf](./web/runs.md#uogtrbwf)

??? abstract "Abstract"
	
	In TREC 2014, we focus on tackling the challenges posed by the Contextual Suggestion and Temporal Summarisation tracks, as well as enhancing our existing technologies to tackle risk-sensitivity as part of the Web track, building upon our Terrier Information Retrieval Platform. In particular, for the Contextual Suggestion track, we propose a novel bundled venue retrieval approach and experiment with text-based summarisation for building the venue description. For our participation to the Temporal Summarisation track, we propose a general framework for performing summarisa- tion over time and two new real-time filtering approaches that leverage the semi-structured nature of news articles to enhance summary coverage. For the TREC Web track, we investigated a novel risk-sensitive learning to rank approach that is based on hypothesis testing and examined approaches that selectively apply different retrieval techniques based upon the query, with the aim of minimising risk.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieDAMLMO14.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieDAMLMO14,
		author = {Richard McCreadie and Romain Deveaud and M{-}Dyaa Albakour and Stuart Mackie and Nut Limsopatham and Craig Macdonald and Iadh Ounis and Thibaut Thonet and Bekir Taner Din{\c{c}}er},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow at {TREC} 2014: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Web Tracks},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-uogTr\_cs-ts-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieDAMLMO14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track TREC2014

_Yuanhai Xue, Xiaoming Yu, Feng Guan, Xi-Peng Li, Man Du, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./web/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_web.pdf)
- :material-file-search: **Runs:** [ICTNET14ADR3](./web/runs.md#ictnet14adr3) | [ICTNET14ADR1](./web/runs.md#ictnet14adr1) | [ICTNET14ADR2](./web/runs.md#ictnet14adr2) | [ICTNET14RSR1](./web/runs.md#ictnet14rsr1) | [ICTNET14RSR2](./web/runs.md#ictnet14rsr2) | [ICTNET14RSR3](./web/runs.md#ictnet14rsr3)

??? abstract "Abstract"
	
	An ad-hoc task in TREC investigates the performance of systems that search a static set of documents using previously-unseen topics. This year, the ClueWeb12[1] dataset are used. The overall goal of the risk-sensitive task is to explore algorithms and evaluation methods for systems that try to jointly maximize an average effectiveness measure across queries, while minimizing effectiveness losses with respect to a provided baseline. Two baselines from different IR systems are supplied this year in order to understand the nature of risk-reward tradeoffs achievable by a system that can adapt to different baselines. The rest of this paper is organized as follows. In Section 2, we discuss the processing of ClueWeb12, derived data and external resources. In Section 3, the BM25 model with term proximity, the diversification method and the results fusion strategy are introduced. We report experimental results and the corresponding re-ranking strategy in Section 4. Finally, our work is concluded in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XueYGLDLC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/XueYGLDLC14,
		author = {Yuanhai Xue and Xiaoming Yu and Feng Guan and Xi{-}Peng Li and Man Du and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Web Track {TREC2014}},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET\_web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XueYGLDLC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Delaware at TREC 2014

_Ashraf Bah, Karankumar Sabhnani, Mustafa Zengin, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [udel](./web/participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf)
- :material-file-search: **Runs:** [udel_itu](./web/runs.md#udel_itu) | [udel_itub](./web/runs.md#udel_itub) | [udelCombCAT2](./web/runs.md#udelcombcat2)

??? abstract "Abstract"
	
	This paper describes the work of the Information Retrieval Lab at the University of Delaware (team name “udel”) on TREC 2014 tracks. We participated in five different tracks: Contextual Suggestion, Federated Web, Microblog, Session, and Web.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BahSZC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/BahSZC14,
		author = {Ashraf Bah and Karankumar Sabhnani and Mustafa Zengin and Ben Carterette},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Delaware at {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_cs-federated-microblog-web-sesson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BahSZC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Towards a Simple and Efficient Web Search Framework

_Di Xu, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [Group.Xu](./web/participants.md#group.xu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-Group.Xu_web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-Group.Xu_web.pdf)
- :material-file-search: **Runs:** [Zerg](./web/runs.md#zerg) | [Terran](./web/runs.md#terran) | [Protoss](./web/runs.md#protoss)

??? abstract "Abstract"
	
	The Web Track of 2014 Text REtrieval Conference (TREC) addresses the most fundamental problem of Information Retrieval. We did not intend to craft a system that beats the state-of-the-art search engines, but to design a light weight and cost-effective system with comparable performances. We introduce a two-pass retrieval framework, with the first pass consisting of a simple and efficient retrieval model that focuses on recall, and the second pass a wave of feature extraction algorithms run on the set of top ranked documents, followed by Learning to Rank (LETOR) algorithms that provide different precision oriented rankings, and their outputs are combined using data fusion. We have focused on using statistical Language Models with novel and well-known smoothing techniques, different LETOR methods, and various data fusion techniques. In addition, we have also tried using topic modelling with Hierarchical Dirichlet Allocation for query expansion in the hope of improving diversity of our results. However, the topic modelling approach has turned out to be unsuccessful, and we have not been able to spot the problem and benefit from it in this work. In addition, we also present some further analyses demonstrating that our approach is robust against overfitting, and some general studies on overfitting in the context of LETOR.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuC14a.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuC14a,
		author = {Di Xu and Jamie Callan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Towards a Simple and Efficient Web Search Framework},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-Group.Xu\_web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuC14a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Two selfless contributions to web search evaluation

_Djoerd Hiemstra, Robin Aly_

- :fontawesome-solid-user-group: **Participant:** [ut](./web/participants.md#ut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ut_web-federated.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ut_web-federated.pdf)
- :material-file-search: **Runs:** [utexact](./web/runs.md#utexact) | [utbase](./web/runs.md#utbase)

??? abstract "Abstract"
	
	We present our results for the Web Search track and the Federated Web Search track for the 23rd Text Retrieval Conference TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HiemstraA14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HiemstraA14,
		author = {Djoerd Hiemstra and Robin Aly},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Two selfless contributions to web search evaluation},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ut\_web-federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HiemstraA14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Federated Web Search 

#### Overview of the TREC 2014 Federated Web Search Track

_Thomas Demeester, Dolf Trieschnigg, Dong Nguyen, Djoerd Hiemstra, Ke Zhou_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/overview-federated.pdf](http://trec.nist.gov/pubs/trec23/papers/overview-federated.pdf)
??? abstract "Abstract"
	
	The TREC Federated Web Search track facilitates research on federated web search, by providing a large realistic data collection sampled from a multitude of online search engines. The FedWeb 2013 Resource Selection and Results Merging tasks are again included in FedWeb 2014, and we additionally introduced the task of vertical selection. Other new aspects are the required link between the Resource Selection and Results Merging tasks, and the importance of diversity i`n the merged results. After an overview of the new data collection and relevance judgments, the individual participants' results for the tasks are introduced, analyzed, and compared.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DemeesterTNHZ14.bib) "
	```
	@inproceedings{DBLP:conf/trec/DemeesterTNHZ14,
		author = {Thomas Demeester and Dolf Trieschnigg and Dong Nguyen and Djoerd Hiemstra and Ke Zhou},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2014 Federated Web Search Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/overview-federated.pdf},
		timestamp = {Tue, 24 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DemeesterTNHZ14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Learning to Combine Collection-centric and Document-centric Models  for Resource Selection

_Krisztian Balog_

- :fontawesome-solid-user-group: **Participant:** [NTNUiS](./federated/participants.md#ntnuis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-NTNUiS_federated.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-NTNUiS_federated.pdf)
- :material-file-search: **Runs:** [NTNUiSrs1](./federated/runs.md#ntnuisrs1) | [NTNUiSrs2](./federated/runs.md#ntnuisrs2) | [NTNUiSrs3](./federated/runs.md#ntnuisrs3) | [NTNUiSvs2](./federated/runs.md#ntnuisvs2) | [NTNUiSvs3](./federated/runs.md#ntnuisvs3)

??? abstract "Abstract"
	
	This paper describes our participation in the Federated Web Search track at TREC 2014. Our main focus is on the resource selection task, where we employ a learning-to-rank approach to combine various (instantiations of) resource ranking models. Further, we show that vertical selection can be run on the output from resource selection, and that it directly benefits from the improvements of thereof.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Balog14.bib) "
	```
	@inproceedings{DBLP:conf/trec/Balog14,
		author = {Krisztian Balog},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Learning to Combine Collection-centric and Document-centric Models for Resource Selection},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-NTNUiS\_federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Balog14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Padua at TREC 2014: Federated Web Search Track

_Emanuele Di Buccio, Massimo Melucci_

- :fontawesome-solid-user-group: **Participant:** [UPD](./federated/participants.md#upd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UPD_federated.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UPD_federated.pdf)
- :material-file-search: **Runs:** [UPDFW14tinnm](./federated/runs.md#updfw14tinnm) | [UPDFW14tipnm](./federated/runs.md#updfw14tipnm) | [UPDFW14tipsm](./federated/runs.md#updfw14tipsm) | [UPDFW14tinsm](./federated/runs.md#updfw14tinsm) | [UPDFW14tiknm](./federated/runs.md#updfw14tiknm) | [UPDFW14tiksm](./federated/runs.md#updfw14tiksm) | [UPDFW14v0pnm](./federated/runs.md#updfw14v0pnm) | [UPDFW14v1knm](./federated/runs.md#updfw14v1knm) | [UPDFW14v1pnm](./federated/runs.md#updfw14v1pnm) | [UPDFW14v1nnm](./federated/runs.md#updfw14v1nnm) | [UPDFW14v0knm](./federated/runs.md#updfw14v0knm) | [UPDFW14r1ksm](./federated/runs.md#updfw14r1ksm) | [UPDFW14v0nnm](./federated/runs.md#updfw14v0nnm)

??? abstract "Abstract"
	
	This paper reports on the participation of the University of Padua to the TREC 2014 Federated Web Search track. The objective was the experimental investigation of the TWF·IRF weighting framework for resource and vertical selection in Federated Web Search settings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuccioM14.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuccioM14,
		author = {Emanuele Di Buccio and Massimo Melucci},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Padua at {TREC} 2014: Federated Web Search Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UPD\_federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuccioM14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Opinions in Federated Search: University of Lugano at TREC 2014  Federated Web Search Track

_Anastasia Giachanou, Fabio Crestani, Ilya Markov_

- :fontawesome-solid-user-group: **Participant:** [ULugano](./federated/participants.md#ulugano)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ULugano-federated.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ULugano-federated.pdf)
- :material-file-search: **Runs:** [ULuganoDFR](./federated/runs.md#uluganodfr) | [ULuganoDocL2](./federated/runs.md#uluganodocl2) | [ULuganoColL2](./federated/runs.md#uluganocoll2) | [ULuganoDFRV](./federated/runs.md#uluganodfrv) | [ULuganoDL2V](./federated/runs.md#uluganodl2v) | [ULuganoCL2V](./federated/runs.md#uluganocl2v) | [ULugFWBsNoOp](./federated/runs.md#ulugfwbsnoop) | [ULugFWBsOp](./federated/runs.md#ulugfwbsop) | [ULugDFRNoOp](./federated/runs.md#ulugdfrnoop) | [ULugDFROp](./federated/runs.md#ulugdfrop)

??? abstract "Abstract"
	
	This technical report presents the work carried out at the University of Lugano on TREC 2014 Federated Web Search track. The main motivation behind our approach is to provide better coverage of opinions that are present in federated resources. On the resource selection and vertical selection steps, we apply opinion mining to select opinionated resources/verticals given a user's query. We do this by combining relevance-based selection with lexicon-based opinion mining. On the results merging step, we diversify the final document ranking based on sentiment using the retrieval-interpolated diversification method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GiachanouCM14.bib) "
	```
	@inproceedings{DBLP:conf/trec/GiachanouCM14,
		author = {Anastasia Giachanou and Fabio Crestani and Ilya Markov},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Opinions in Federated Search: University of Lugano at {TREC} 2014 Federated Web Search Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ULugano-federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GiachanouCM14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Federated Web Search Track 2014

_Feng Guan, Shuiyuan Zhang, Chunmei Liu, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./federated/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_federated.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_federated.pdf)
- :material-file-search: **Runs:** [ICTNETVS1](./federated/runs.md#ictnetvs1) | [ICTNETVS02](./federated/runs.md#ictnetvs02) | [ICTNETVS03](./federated/runs.md#ictnetvs03) | [ICTNETVS04](./federated/runs.md#ictnetvs04) | [ICTNETVS05](./federated/runs.md#ictnetvs05) | [ICTNETVS06](./federated/runs.md#ictnetvs06) | [ICTNETVS07](./federated/runs.md#ictnetvs07) | [ICTNETRS01](./federated/runs.md#ictnetrs01) | [ICTNETRS02](./federated/runs.md#ictnetrs02) | [ICTNETRS03](./federated/runs.md#ictnetrs03) | [ICTNETRS04](./federated/runs.md#ictnetrs04) | [ICTNETRS05](./federated/runs.md#ictnetrs05) | [ICTNETRS06](./federated/runs.md#ictnetrs06) | [ICTNETRS07](./federated/runs.md#ictnetrs07) | [ICTNETRM01](./federated/runs.md#ictnetrm01) | [ICTNETRM02](./federated/runs.md#ictnetrm02) | [ICTNETRM03](./federated/runs.md#ictnetrm03) | [ICTNETRM04](./federated/runs.md#ictnetrm04) | [ICTNETRM05](./federated/runs.md#ictnetrm05) | [ICTNETRM06](./federated/runs.md#ictnetrm06) | [ICTNETRM07](./federated/runs.md#ictnetrm07)

??? abstract "Abstract"
	
	We have participated all the three tasks of FedWeb 2014 this year. Basic methods that we used for these tasks will be described in section 2. Section 3 shows combination of the basic methods for different runs and the results will also be introduced.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GuanZLYLC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/GuanZLYLC14,
		author = {Feng Guan and Shuiyuan Zhang and Chunmei Liu and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Federated Web Search Track 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET\_federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GuanZLYLC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Two selfless contributions to web search evaluation

_Djoerd Hiemstra, Robin Aly_

- :fontawesome-solid-user-group: **Participant:** [ut](./federated/participants.md#ut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ut_web-federated.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ut_web-federated.pdf)
- :material-file-search: **Runs:** [UTTailyG2000](./federated/runs.md#uttailyg2000)

??? abstract "Abstract"
	
	We present our results for the Web Search track and the Federated Web Search track for the 23rd Text Retrieval Conference TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HiemstraA14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HiemstraA14,
		author = {Djoerd Hiemstra and Robin Aly},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Two selfless contributions to web search evaluation},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ut\_web-federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HiemstraA14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Simple May Be Best - A Simple and Effective Method for Federated  Web Search via Search Engine Impact Factor Estimation

_Shan Jin, Man Lan_

- :fontawesome-solid-user-group: **Participant:** [ECNU](./federated/participants.md#ecnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ECNU_federated.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ECNU_federated.pdf)

??? abstract "Abstract"
	
	This paper reports our participation in the three tasks, i.e., vertical selection (VS), resource selection (RS) and results merging (RM) in TREC 2014 Federated Web Search track. In consideration of the connections between vertical and search engine (i.e., a vertical could contain multiple resources), we address the two tasks in an iterative way. Existing algorithms adopted relevance measures to calculate the semantic relatedness between query and resources or returned results. However they neglected the influence of search engine in itself. In this work, we propose a Search engine Impact Factor (SEIF) estimation approach to improve the performance of vertical and resource selection. The officially released results showed that our systems ranked 1st in RS task and 2nd in VS task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JinL14.bib) "
	```
	@inproceedings{DBLP:conf/trec/JinL14,
		author = {Shan Jin and Man Lan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Simple May Be Best - {A} Simple and Effective Method for Federated Web Search via Search Engine Impact Factor Estimation},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ECNU\_federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JinL14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Transformations for Result Merging

_Shriphani Palakodety, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU_LTI](./federated/participants.md#cmu_lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-CMU_LTI_federated.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-CMU_LTI_federated.pdf)
- :material-file-search: **Runs:** [plain](./federated/runs.md#plain) | [sdm5](./federated/runs.md#sdm5) | [googUniform7](./federated/runs.md#googuniform7) | [googTermWise7](./federated/runs.md#googtermwise7)

??? abstract "Abstract"
	
	This paper describes Carnegie Mellon University's entry at the TREC 2014 Federated Web Search track (FedWeb14). Federated search pipelines typically have two components: (i) resource-selection, and (ii) result-merging. This work documents experiments to modify queries to merge results in the federated-search pipeline. Approaches from previous attempts at solving this problem involved custom query-document similarity scores or rank-combination methods. In this document, we explore how term-dependence models and query expansion strategies influence result-merging.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PalakodetyC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/PalakodetyC14,
		author = {Shriphani Palakodety and Jamie Callan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query Transformations for Result Merging},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-CMU\_LTI\_federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PalakodetyC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RUC at TREC 2014: Select Resources Using Topic Models

_Qiuyue Wang, Shaochen Shi, Wei Cao_

- :fontawesome-solid-user-group: **Participant:** [info_ruc](./federated/participants.md#info_ruc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-info_ruc_federated.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-info_ruc_federated.pdf)
- :material-file-search: **Runs:** [FW14Docs100](./federated/runs.md#fw14docs100) | [FW14Docs75](./federated/runs.md#fw14docs75) | [FW14Docs50](./federated/runs.md#fw14docs50) | [FW14Search100](./federated/runs.md#fw14search100) | [FW14Search75](./federated/runs.md#fw14search75) | [FW14Search50](./federated/runs.md#fw14search50)

??? abstract "Abstract"
	
	This paper describes the work done in Renmin University of China for the Federated Web Search Track of TREC 2014. We participated in the resource selection task. We used the LDA topic modeling approach to select potentially relevant resources for a given query. The initial results are promising.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangSC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangSC14,
		author = {Qiuyue Wang and Shaochen Shi and Wei Cao},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{RUC} at {TREC} 2014: Select Resources Using Topic Models},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-info\_ruc\_federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangSC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Drexel at TREC 2014 Federated Web Search Track

_Haozhen Zhao, Xiaohua Hu_

- :fontawesome-solid-user-group: **Participant:** [dragon](./federated/participants.md#dragon)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-dragon_federated.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-dragon_federated.pdf)
- :material-file-search: **Runs:** [drexelRS1](./federated/runs.md#drexelrs1) | [drexelRS2](./federated/runs.md#drexelrs2) | [drexelRS3](./federated/runs.md#drexelrs3) | [drexelRS4](./federated/runs.md#drexelrs4) | [drexelRS5](./federated/runs.md#drexelrs5) | [drexelRS6](./federated/runs.md#drexelrs6) | [drexelRS7](./federated/runs.md#drexelrs7) | [drexelVS1](./federated/runs.md#drexelvs1) | [drexelVS2](./federated/runs.md#drexelvs2) | [drexelVS3](./federated/runs.md#drexelvs3) | [drexelVS4](./federated/runs.md#drexelvs4) | [drexelVS5](./federated/runs.md#drexelvs5) | [drexelVS6](./federated/runs.md#drexelvs6) | [drexelVS7](./federated/runs.md#drexelvs7) | [drexelRS4mW](./federated/runs.md#drexelrs4mw) | [drexelRS1mR](./federated/runs.md#drexelrs1mr) | [drexelRS7mW](./federated/runs.md#drexelrs7mw) | [drexelRS6mR](./federated/runs.md#drexelrs6mr) | [drexelRS6mW](./federated/runs.md#drexelrs6mw) | [FW14basemR](./federated/runs.md#fw14basemr) | [FW14basemW](./federated/runs.md#fw14basemw)

??? abstract "Abstract"
	
	This paper reports our participation in the Federated Web Search Track in TREC 2014. We submitted 21 runs for all the three tasks: Vertical Selection (7), Resource Selection (7) and Results Merging (7). Our main purpose is to test several established resource selection methods on the new realistic FedWeb test collections. We evaluated 7 well known resource selection methods for the vertical selection and resource selection tasks. The effectiveness of these methods in the RS tasks does not carry to the VS tasks, which implies that more sophisticated algorithms and more diverse sources of evidence are needed for solving the VS task effectively. Our Results Merging experiments reveal the correlation between the performance of RM and the performance of its input RS results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoH14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoH14,
		author = {Haozhen Zhao and Xiaohua Hu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Drexel at {TREC} 2014 Federated Web Search Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-dragon\_federated.pdf},
		timestamp = {Fri, 09 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoH14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Delaware at TREC 2014

_Ashraf Bah, Karankumar Sabhnani, Mustafa Zengin, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [udel](./federated/participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf)
- :material-file-search: **Runs:** [udelftvql](./federated/runs.md#udelftvql) | [udelftvqlR](./federated/runs.md#udelftvqlr) | [udelftrsbs](./federated/runs.md#udelftrsbs) | [udelftrssn](./federated/runs.md#udelftrssn)

??? abstract "Abstract"
	
	This paper describes the work of the Information Retrieval Lab at the University of Delaware (team name “udel”) on TREC 2014 tracks. We participated in five different tracks: Contextual Suggestion, Federated Web, Microblog, Session, and Web.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BahSZC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/BahSZC14,
		author = {Ashraf Bah and Karankumar Sabhnani and Mustafa Zengin and Ben Carterette},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Delaware at {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_cs-federated-microblog-web-sesson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BahSZC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Illinois' Graduate School of Library and Information  Science at TREC 2014

_Garrick Sherman, Miles Efron, Craig Willis_

- :fontawesome-solid-user-group: **Participant:** [uiucGSLIS](./federated/participants.md#uiucgslis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-uiucGSLIS-federated-kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-uiucGSLIS-federated-kba.pdf)
- :material-file-search: **Runs:** [uiucGSLISf2](./federated/runs.md#uiucgslisf2) | [uiucGSLISf1](./federated/runs.md#uiucgslisf1)

??? abstract "Abstract"
	
	The University of Illinois' Graduate School of Library and Information Science (uiucGSLIS) participated in TREC's Federated Web (FedWeb) and Knowledge Base Acceleration (KBA) tracks in 2014. Specifically, we submitted runs for the FedWeb resource selection and KBA cumulative citation recommendation (CCR) tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShermanEW14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShermanEW14,
		author = {Garrick Sherman and Miles Efron and Craig Willis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Illinois' Graduate School of Library and Information Science at {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-uiucGSLIS-federated-kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShermanEW14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Knowledge Base Acceleration 

#### Evaluating Stream Filtering for Entity Profile Updates in TREC 2012,  2013, and 2014

_John R. Frank, Max Kleiman-Weiner, Daniel A. Roberts, Ellen M. Voorhees, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/overview-kba.pdf](http://trec.nist.gov/pubs/trec23/papers/overview-kba.pdf)
??? abstract "Abstract"
	
	The Knowledge Base Acceleration (KBA) track ran in TREC 2012, 2013, and 2014 as an entity- centric filtering evaluation. This track evaluates systems that filter a time-ordered corpus for documents and slot fills that would change an entity profile in a predefined list of entities. Compared with the 2012 and 2013 evaluations, the 2014 evaluation introduced several refinements, including high-quality community metadata from running Raytheon/BBN's Serif named entity recognizer, sentence parser, and relation extractor on 579,838,246 English documents in the corpus. We also expanded the query entities to be primarily long-tail entities that lacked Wikipedia profiles. We simplified the SSF scoring, and also added a third task component for highlighting creative systems that used the KBA data. A successful KBA system must do more than resolve the meaning of entity mentions by linking documents to the KB: it must also distinguish novel “vitally” relevant documents and slot fills that would change a target entity's profile. This combines thinking from natural language understanding (NLU) and information retrieval (IR). Filtering tracks in TREC have typically used queries based on topics described by a set of keyword queries or short descriptions, and annotators have generated relevance judgments based on their personal interpretation of the topic. For TREC 2014, we selected a set of filter topics based on people, organizations, and facilities in the region between Seattle, Washington, and Vancouver, British Columbia: 86 people, 16 organizations, and 7 facilities. Assessors judged ~30k documents, which included most documents that mention a name from a handcrafted list of surface form names of the 109 target entities. TREC teams were provided with all of the ground truth data divided into training and evaluation data. We present peak macro-averaged F_1 scores for all run submissions. High scoring systems used a variety of approaches, including feature engineering around linguistic structures, names of related entities, and various types of classifiers. Top scoring systems achieved F_1 scores in the high-50s. We present results for a baseline system that performs in the low-40s. We discuss key lessons learned that motivate future tracks at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FrankKRVS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/FrankKRVS14,
		author = {John R. Frank and Max Kleiman{-}Weiner and Daniel A. Roberts and Ellen M. Voorhees and Ian Soboroff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Evaluating Stream Filtering for Entity Profile Updates in {TREC} 2012, 2013, and 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/overview-kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FrankKRVS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC KBA 2014

_Rafik Abbes, Karen Pinel-Sauvagnat, Nathalie Hernandez, Mohand Boughanem_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./kba/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-IRIT_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-IRIT_kba.pdf)
- :material-file-search: **Runs:** [IRIT-alpha_10_0.25](./kba/runs.md#irit-alpha_10_0.25) | [IRIT-alpha_10_0.5](./kba/runs.md#irit-alpha_10_0.5) | [IRIT-alpha_10_0.75](./kba/runs.md#irit-alpha_10_0.75) | [IRIT-alpha_50_0.25](./kba/runs.md#irit-alpha_50_0.25) | [IRIT-alpha_50_0.5](./kba/runs.md#irit-alpha_50_0.5) | [IRIT-alpha_50_0.75](./kba/runs.md#irit-alpha_50_0.75) | [IRIT-alpha_100_0.25](./kba/runs.md#irit-alpha_100_0.25) | [IRIT-alpha_100_0.5](./kba/runs.md#irit-alpha_100_0.5) | [IRIT-alpha_100_0.75](./kba/runs.md#irit-alpha_100_0.75) | [IRIT-VLM_10](./kba/runs.md#irit-vlm_10) | [IRIT-VLM_50](./kba/runs.md#irit-vlm_50) | [IRIT-VULMBuzz_10](./kba/runs.md#irit-vulmbuzz_10) | [IRIT-VULMBuzz_50](./kba/runs.md#irit-vulmbuzz_50) | [IRIT-ULM_10](./kba/runs.md#irit-ulm_10) | [IRIT-ULM_50](./kba/runs.md#irit-ulm_50) | [IRIT-alpha_50_0.75T](./kba/runs.md#irit-alpha_50_0.75t) | [IRIT-ULMBuzz_50_0.5T](./kba/runs.md#irit-ulmbuzz_50_0.5t) | [IRIT-ULMBuzz_50_0.7T](./kba/runs.md#irit-ulmbuzz_50_0.7t) | [IRIT-VULMBuz_50_0.7T](./kba/runs.md#irit-vulmbuz_50_0.7t) | [IRIT-VULMBuz_50_0.5T](./kba/runs.md#irit-vulmbuz_50_0.5t)

??? abstract "Abstract"
	
	This paper describes the IRIT lab participation to the Vital Filtering task (also known as Cumulative Citation Recommendation) of the TREC 2014 Knowledge Base Acceleration Track. This task aims at identifying vital documents containing timely new information that should help a human to update the profile of the target entity (e.g., Wikipedia page of the entity). In this work, we evaluate two factors that could detect vitality. The first one uses a Language Model to learn vitality from a sample of vital documents, and the second leverages the bursts of documents in the stream. Obtained results are presented and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbbesPHB14.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbbesPHB14,
		author = {Rafik Abbes and Karen Pinel{-}Sauvagnat and Nathalie Hernandez and Mohand Boughanem},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IRIT} at {TREC} {KBA} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-IRIT\_kba.pdf},
		timestamp = {Wed, 03 Feb 2021 08:31:24 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AbbesPHB14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Use of Time-Aware Language Model in Entity Driven Filtering System

_Vincent Bouvier, Patrice Bellot_

- :fontawesome-solid-user-group: **Participant:** [LSIS](./kba/participants.md#lsis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-LSIS_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-LSIS_kba.pdf)
- :material-file-search: **Runs:** [LSIS-AF_NU_MCE](./kba/runs.md#lsis-af_nu_mce) | [LSIS-AF_NU_SE](./kba/runs.md#lsis-af_nu_se) | [LSIS-AF_NU_TSE](./kba/runs.md#lsis-af_nu_tse) | [LSIS-AF_NU_VOE](./kba/runs.md#lsis-af_nu_voe) | [LSIS-AF_UD_MCE](./kba/runs.md#lsis-af_ud_mce) | [LSIS-AF_UD_SE](./kba/runs.md#lsis-af_ud_se) | [LSIS-AF_UD_TSE](./kba/runs.md#lsis-af_ud_tse) | [LSIS-AF_UD_VOE](./kba/runs.md#lsis-af_ud_voe) | [LSIS-AF_US_MCE](./kba/runs.md#lsis-af_us_mce) | [LSIS-AF_US_SE](./kba/runs.md#lsis-af_us_se) | [LSIS-AF_US_TSE](./kba/runs.md#lsis-af_us_tse) | [LSIS-AF_US_VOE](./kba/runs.md#lsis-af_us_voe)

??? abstract "Abstract"
	
	Tracking entities, so that new or important information about that entities are caught, is a real challenge and has many applications (e.g., information monitoring, marketing,...). We are interesting in how to represent an entity profile to fulfill two purposes: 1. entity detection and disambiguation, 2. novelty and importance quantification. We propose an entity profile, which uses two language models. First, the Reference Language Model (RLM), which is mainly used for disambiguation. Second, we propose a formalization of a Time-Aware Language Model, which is used for novelty detection. To rank documents, we propose a semi-supervised classification approach which uses meta-features computed on documents using entity profiles and time series.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BouvierB14.bib) "
	```
	@inproceedings{DBLP:conf/trec/BouvierB14,
		author = {Vincent Bouvier and Patrice Bellot},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Use of Time-Aware Language Model in Entity Driven Filtering System},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-LSIS\_kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BouvierB14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Distributed Non-Parametric Representations for Vital Filtering: UW  at TREC KBA 2014

_Ignacio Cano, Sameer Singh, Carlos Guestrin_

- :fontawesome-solid-user-group: **Participant:** [UW](./kba/participants.md#uw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UW_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UW_kba.pdf)
- :material-file-search: **Runs:** [UW-basic_single](./kba/runs.md#uw-basic_single) | [UW-basic_multitask](./kba/runs.md#uw-basic_multitask) | [UW-embedding_pos](./kba/runs.md#uw-embedding_pos) | [UW-embedding_comb](./kba/runs.md#uw-embedding_comb) | [UW-mean_stat](./kba/runs.md#uw-mean_stat) | [UW-clu_stat_a08](./kba/runs.md#uw-clu_stat_a08) | [UW-mean_dyn_g06](./kba/runs.md#uw-mean_dyn_g06) | [UW-clu_dyn_a08_g04](./kba/runs.md#uw-clu_dyn_a08_g04) | [UW-clu_dyn_nv_e](./kba/runs.md#uw-clu_dyn_nv_e) | [UW-f_basic_single](./kba/runs.md#uw-f_basic_single) | [UW-f_basic_multi](./kba/runs.md#uw-f_basic_multi) | [UW-f_emb_comb](./kba/runs.md#uw-f_emb_comb) | [UW-f_mean_stat](./kba/runs.md#uw-f_mean_stat) | [UW-f_mean_dyn](./kba/runs.md#uw-f_mean_dyn) | [UW-f_clust_stat](./kba/runs.md#uw-f_clust_stat) | [UW-f_clust_dyn](./kba/runs.md#uw-f_clust_dyn) | [UW-f_emb_pos](./kba/runs.md#uw-f_emb_pos)

??? abstract "Abstract"
	
	Identifying documents that contain timely and vi- tal information for an entity of interest, a task known as vital filtering, has become increasingly important with the availability of large document collections. To efficiently filter such large text corpora in a streaming manner, we need to compactly represent previously observed entity contexts, and quickly estimate whether a new document contains novel information. Existing approaches to modeling contexts, such as bag of words, latent semantic indexing, and topic models, are limited in several respects: they are unable to handle streaming data, do not model the underlying topic of each document, suffer from lexical sparsity, and/or do not accurately estimate temporal vitalness. In this paper, we introduce a word embedding-based non-parametric representation of entities that addresses the above limitations. The word embeddings provide accurate and compact summaries of observed entity contexts, further described by topic clusters that are estimated in a non-parametric manner. Additionally, we associate a staleness measure with each entity and topic cluster, dynamically estimating their temporal relevance. This approach of using word embeddings, non-parametric clustering, and staleness provides an efficient yet appropriate representation of entity contexts for the streaming setting, enabling accurate vital filtering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CanoSG14.bib) "
	```
	@inproceedings{DBLP:conf/trec/CanoSG14,
		author = {Ignacio Cano and Sameer Singh and Carlos Guestrin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Distributed Non-Parametric Representations for Vital Filtering: {UW} at {TREC} {KBA} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UW\_kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CanoSG14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### K2U at TREC 2014 KBA Track

_Shun Kawahara, Kuniaki Uehara, Kazuhiro Seki_

- :fontawesome-solid-user-group: **Participant:** [KobeU](./kba/participants.md#kobeu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-KobeU_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-KobeU_kba.pdf)
- :material-file-search: **Runs:** [KobeU-exact_match](./kba/runs.md#kobeu-exact_match) | [KobeU-ccr_03](./kba/runs.md#kobeu-ccr_03) | [KobeU-ccr_08](./kba/runs.md#kobeu-ccr_08)

??? abstract "Abstract"
	
	Kobe University and Konan University (K2U) collaborated on the vital filtering task of the 2014 TREC KBA track. This paper describes our proposed system developed on the distributed and fault-tolerant realtime computation system, Apache Storm, and reports the results obtained for our submitted runs. The remainder of this paper is structured as follows: Section II briefly introduces Apache Storm and its components, Section III describes our proposed system for the vital filtering task, Section IV reports and discusses the results for our submitted runs, and Section V concludes this paper with a brief summary.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KawaharaUS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/KawaharaUS14,
		author = {Shun Kawahara and Kuniaki Uehara and Kazuhiro Seki},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{K2U} at {TREC} 2014 {KBA} Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-KobeU\_kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KawaharaUS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SCU at TREC 2014 Knowledge Base Acceleration Track

_Hung Nguyen, Yi Fang_

- :fontawesome-solid-user-group: **Participant:** [SCU](./kba/participants.md#scu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-SCU_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-SCU_kba.pdf)
- :material-file-search: **Runs:** [SCU-ssf_1](./kba/runs.md#scu-ssf_1) | [SCU-ssf_2](./kba/runs.md#scu-ssf_2) | [SCU-ssf_3](./kba/runs.md#scu-ssf_3) | [SCU-ssf_4](./kba/runs.md#scu-ssf_4) | [SCU-ssf_5](./kba/runs.md#scu-ssf_5) | [SCU-ssf_6](./kba/runs.md#scu-ssf_6) | [SCU-ssf_7](./kba/runs.md#scu-ssf_7) | [SCU-ssf_8](./kba/runs.md#scu-ssf_8) | [SCU-ssf_9](./kba/runs.md#scu-ssf_9) | [SCU-ssf_10](./kba/runs.md#scu-ssf_10) | [SCU-ssf_11](./kba/runs.md#scu-ssf_11) | [SCU-ssf_12](./kba/runs.md#scu-ssf_12) | [SCU-ssf_13](./kba/runs.md#scu-ssf_13) | [SCU-ssf_14](./kba/runs.md#scu-ssf_14)

??? abstract "Abstract"
	
	In this paper, we present our system we developed at Santa Clara University to address the SSF task in TREC KBA 2014. We used the pattern matching method to extract slot values for interested entities from relevant passages. We improved the approach we used last year to enhance the performance. Our system consists of the following steps: processing filtered corpus, retrieving relevant passages, pattern matching, computing scores, and generate results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NguyenF14.bib) "
	```
	@inproceedings{DBLP:conf/trec/NguyenF14,
		author = {Hung Nguyen and Yi Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{SCU} at {TREC} 2014 Knowledge Base Acceleration Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-SCU\_kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NguyenF14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BUPT_PRIS at TREC 2014 Knowledge Base Acceleration Track

_Yuanyuan Qi, Ye Xu, Dongxu Zhang, Weiran Xu_

- :fontawesome-solid-user-group: **Participant:** [BUPT_PRIS](./kba/participants.md#bupt_pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BUPT_PRIS_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BUPT_PRIS_kba.pdf)
- :material-file-search: **Runs:** [BUPT_PRIS-pris_baseline](./kba/runs.md#bupt_pris-pris_baseline) | [BUPT_PRIS-pris_svm](./kba/runs.md#bupt_pris-pris_svm) | [BUPT_PRIS-pris_NN](./kba/runs.md#bupt_pris-pris_nn) | [BUPT_PRIS-pris_rf](./kba/runs.md#bupt_pris-pris_rf) | [BUPT_PRIS-ssf1](./kba/runs.md#bupt_pris-ssf1) | [BUPT_PRIS-ssf2](./kba/runs.md#bupt_pris-ssf2)

??? abstract "Abstract"
	
	This paper describes the system in Vital Filtering and Streaming Slot Filling task of TREC 2014 Knowledge Base Acceleration Track. In the Vital Filtering task, The PRIS system focuses attention on query expansion and similarity calculation. The system uses DBpedia as external source data to do query expansion and generates directional documents to calculate similarities with candidate worth citing documents. In the Streaming Slot Filling task, The BUPT_PRIS system utilizes a pattern learning method to do relation extraction and slot filling. Patterns of regular slots which mostly are same to TAC-KBP slots are learned from KBP Slot Filling corpus. Other slots are manually picked up some training seeds for those slot types that KBP didn't contain to use bootstrapping method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiXZX14.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiXZX14,
		author = {Yuanyuan Qi and Ye Xu and Dongxu Zhang and Weiran Xu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {BUPT{\_}PRIS at {TREC} 2014 Knowledge Base Acceleration Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BUPT\_PRIS\_kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiXZX14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Illinois' Graduate School of Library and Information  Science at TREC 2014

_Garrick Sherman, Miles Efron, Craig Willis_

- :fontawesome-solid-user-group: **Participant:** [uiucGSLIS](./kba/participants.md#uiucgslis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-uiucGSLIS-federated-kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-uiucGSLIS-federated-kba.pdf)
- :material-file-search: **Runs:** [uiucGSLIS-baseline_sf](./kba/runs.md#uiucgslis-baseline_sf) | [uiucGSLIS-baseline_rm3](./kba/runs.md#uiucgslis-baseline_rm3) | [uiucGSLIS-length_sf](./kba/runs.md#uiucgslis-length_sf) | [uiucGSLIS-length_rm3](./kba/runs.md#uiucgslis-length_rm3) | [uiucGSLIS-prevdocs_sf](./kba/runs.md#uiucgslis-prevdocs_sf) | [uiucGSLIS-prevdocs_rm3](./kba/runs.md#uiucgslis-prevdocs_rm3) | [uiucGSLIS-pdsrc_rm3](./kba/runs.md#uiucgslis-pdsrc_rm3) | [uiucGSLIS-pdsrc_sf](./kba/runs.md#uiucgslis-pdsrc_sf) | [uiucGSLIS-pdverb_sf](./kba/runs.md#uiucgslis-pdverb_sf) | [uiucGSLIS-pdverb_rm3](./kba/runs.md#uiucgslis-pdverb_rm3) | [uiucGSLIS-sourcelen_rm3](./kba/runs.md#uiucgslis-sourcelen_rm3) | [uiucGSLIS-sourcelen_sf](./kba/runs.md#uiucgslis-sourcelen_sf) | [uiucGSLIS-verbsource_rm3](./kba/runs.md#uiucgslis-verbsource_rm3) | [uiucGSLIS-verbsource_sf](./kba/runs.md#uiucgslis-verbsource_sf)

??? abstract "Abstract"
	
	The University of Illinois' Graduate School of Library and Information Science (uiucGSLIS) participated in TREC's Federated Web (FedWeb) and Knowledge Base Acceleration (KBA) tracks in 2014. Specifically, we submitted runs for the FedWeb resource selection and KBA cumulative citation recommendation (CCR) tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShermanEW14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShermanEW14,
		author = {Garrick Sherman and Miles Efron and Craig Willis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Illinois' Graduate School of Library and Information Science at {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-uiucGSLIS-federated-kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShermanEW14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BIT and Purdue at TREC-KBA-CCR Track 2014

_Jingang Wang, Ning Zhang, Zhiwei Zhang, Dandan Song, Luo Si, Lejian Liao_

- :fontawesome-solid-user-group: **Participant:** [BIT_Purdue](./kba/participants.md#bit_purdue)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BIT-Purdue_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BIT-Purdue_kba.pdf)
- :material-file-search: **Runs:** [BIT_Purdue-baseline](./kba/runs.md#bit_purdue-baseline) | [BIT_Purdue-profile](./kba/runs.md#bit_purdue-profile) | [BIT_Purdue-labeled](./kba/runs.md#bit_purdue-labeled) | [BIT_Purdue-GlobalRank](./kba/runs.md#bit_purdue-globalrank) | [BIT_Purdue-BinaryRank](./kba/runs.md#bit_purdue-binaryrank) | [BIT_Purdue-GlobalClassU](./kba/runs.md#bit_purdue-globalclassu) | [BIT_Purdue-GlobalClassV](./kba/runs.md#bit_purdue-globalclassv) | [BIT_Purdue-GlobalClassV1](./kba/runs.md#bit_purdue-globalclassv1)

??? abstract "Abstract"
	
	This report summarizes our participation at KBA-CCR track in TREC 2014. Our submissions are generated in two steps: (1) Filtering a candidate documents collection from the stream corpus for a set of target entities; and (2) Estimating the relevance levels between candidate documents and target entities. Three kinds of approaches are employed in the second step, including query expansion, classi cation and learning to rank. Query expansion is an unsupervised baseline by combining an entity and its related entities as a query to retrieve its relevant documents. Query expansion performs considerably well in vital + useful scenario. It's not difficult to lter a relevant document set from the stream corpus. However, in vital only scenario, supervised approaches are more powerful than query expansion in identifying vital documents for target entities. Our results reveal that learning to rank approaches are more suitable for CCR with current evaluation methodology.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangZZSSL14.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangZZSSL14,
		author = {Jingang Wang and Ning Zhang and Zhiwei Zhang and Dandan Song and Luo Si and Lejian Liao},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BIT} and Purdue at {TREC-KBA-CCR} Track 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BIT-Purdue\_kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangZZSSL14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WHU at TREC KBA Vital Filtering Track 2014

_Chuan Wu, Wei Lu, Pengcheng Zhou, Xiaohua Feng_

- :fontawesome-solid-user-group: **Participant:** [WHU_IRGroup](./kba/participants.md#whu_irgroup)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-WHU_IRGroup_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-WHU_IRGroup_kba.pdf)
- :material-file-search: **Runs:** [WHU_IRGroup-baseline](./kba/runs.md#whu_irgroup-baseline) | [WHU_IRGroup-BM_TF](./kba/runs.md#whu_irgroup-bm_tf) | [WHU_IRGroup-BM_TF_3](./kba/runs.md#whu_irgroup-bm_tf_3) | [WHU_IRGroup-CUSTOM_TF_FIXED](./kba/runs.md#whu_irgroup-custom_tf_fixed)

??? abstract "Abstract"
	
	This paper describes the WHU IRLAB participation to the Vital Filtering task of the TREC 2014 Knowledge Base Acceleration Track. In this task, we implemented a system to detect vital documents that could be used for a human editor to update or create the profile of an entity. Our approach is to view the problem as a classification problem and use Stanford NLP Toolkit to extract necessary information. Various kinds of features are leveraged to classify documents to three classes, i.e. vital, useful, and non-useful (garbage or neutral). We submitted four runs using different combinations of features. The results are presented and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuLZF14.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuLZF14,
		author = {Chuan Wu and Wei Lu and Pengcheng Zhou and Xiaohua Feng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{WHU} at {TREC} {KBA} Vital Filtering Track 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-WHU\_IRGroup\_kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuLZF14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Temporal Summarization 

#### TREC 2014 Temporal Summarization Track Overview

_Javed A. Aslam, Matthew Ekstrand-Abueg, Virgil Pavlu, Fernando Diaz, Richard McCreadie, Tetsuya Sakai_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/overview-tempsumm.pdf](http://trec.nist.gov/pubs/trec23/papers/overview-tempsumm.pdf)
??? abstract "Abstract"
	
	News events such as protests, accidents or natural disasters represent a unique information access problem where traditional approaches fail. For example, immediately after an event, the corpus may be sparsely populated with relevant content. Even when, after a few hours, relevant content becomes available, it is often inaccurate or highly redundant. At the same time, crisis events demonstrate a scenario where users urgently need information, especially if they are directly affected by the event. The goal of this track is to develop systems for efficiently monitoring the information associated with an event over time. Specifically, we are interested in developing systems which can broadcast short, relevant, and reliable sentence-length updates about a developing event. The track has the following four main aims: To develop algorithms which detect sub-events with low latency, To model information reliability in the presence of a dynamic corpus, To understand and address the sensitivity of text summarization algorithms in an online, sequential setting, and To understand and address the sensitivity of information extraction algorithms in dynamic settings. The remainder of this overview is structured as follows. Section 2 describes the temporal summarization task in detail. In Section 3, we discuss the corpus of documents from which the summaries are produced, while in Section 4, we discuss how temporal summarization systems are evaluated within the track. Section 5 details the process via which sentence updates were assessed. Finally, in Section 6, we summarize the performance of the participant systems to the 2014 track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AslamEPDMS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/AslamEPDMS14,
		author = {Javed A. Aslam and Matthew Ekstrand{-}Abueg and Virgil Pavlu and Fernando Diaz and Richard McCreadie and Tetsuya Sakai},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2014 Temporal Summarization Track Overview},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/overview-tempsumm.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AslamEPDMS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Temporal Summarization 2014

_Rafik Abbes, Karen Pinel-Sauvagnat, Nathalie Hernandez, Mohand Boughanem_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./tempsumm/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-IRIT_ts.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-IRIT_ts.pdf)
- :material-file-search: **Runs:** [KW30H5NW3600](./tempsumm/runs.md#kw30h5nw3600) | [KW30H5NW300](./tempsumm/runs.md#kw30h5nw300) | [KW80H5NW300](./tempsumm/runs.md#kw80h5nw300) | [KW80H5NW3600](./tempsumm/runs.md#kw80h5nw3600) | [KW80H10NW300](./tempsumm/runs.md#kw80h10nw300) | [KW30H10NW300](./tempsumm/runs.md#kw30h10nw300)

??? abstract "Abstract"
	
	This paper describes the IRIT lab participation to the 2014 TREC Temporal Summarization track. The goal of the Temporal Summarization track is to develop systems that allow users to efficiently monitor information about events over time. Our proposed method selects relevant documents that are more likely to concern the event, and extracts relevant and novel sentences based on some filters. Obtained results are presented and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbbesPHB14a.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbbesPHB14a,
		author = {Rafik Abbes and Karen Pinel{-}Sauvagnat and Nathalie Hernandez and Mohand Boughanem},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IRIT} at {TREC} Temporal Summarization 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-IRIT\_ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AbbesPHB14a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Temporal Summarization Track TREC 2014

_Lei Chen, Hainan Zhang, Siying Li, Zhiyuan Ji, Qian Liu, Yue Liu, Dayong Wu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./tempsumm/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_ts.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_ts.pdf)
- :material-file-search: **Runs:** [run1](./tempsumm/runs.md#run1) | [run4](./tempsumm/runs.md#run4) | [run3](./tempsumm/runs.md#run3) | [run2](./tempsumm/runs.md#run2)

??? abstract "Abstract"
	
	Temporal Summarization task is a standard Information Retrieval problem. The goal of the task is to generate sequential update summarization, which are useful, new and timely sentence length updates about a developing event [1]. The event refers to a temporally acute topic, and each topic contains the start time and end time. There are more event types than the last year. They are accident, bombing, hostage, impact event, protest, riot, shooting and storm. Formally, given the time ordered corpus, the query and the relevant time range, our system outputs a list of relevant sentence identifiers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenZLJLLWC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenZLJLLWC14,
		author = {Lei Chen and Hainan Zhang and Siying Li and Zhiyuan Ji and Qian Liu and Yue Liu and Dayong Wu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Temporal Summarization Track {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET\_ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenZLJLLWC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Information Extraction systems of BUPT_PRIS at TREC2014 Temporal  Summarization Track

_Yuanyuan Qi, Qinlong Wang, Chuchu Huang, Bo Tang, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [BUPT_PRIS](./tempsumm/participants.md#bupt_pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BUPT_PRIS_ts.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BUPT_PRIS_ts.pdf)
- :material-file-search: **Runs:** [Cluster1](./tempsumm/runs.md#cluster1) | [Cluster2](./tempsumm/runs.md#cluster2) | [Cluster3](./tempsumm/runs.md#cluster3) | [Cluster4](./tempsumm/runs.md#cluster4)

??? abstract "Abstract"
	
	This paper describes the information extraction systems of BUPT_PRIS at Temporal Summarization Track, Which includes data obtaining and preprocessing, index building and query expansion, sentences scoring module. This year only keep one task: sequential update summarization, the task: value tracking is cancelled. For the sequential update summarization we focus attention on queries expansion and sentence scoring. There are three methods of query expansion introduced in this report: WordNets, Word representation, spatial analysis method. We also show the evaluation results for our team and the comparison with the best and median evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiWHTXCG14.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiWHTXCG14,
		author = {Yuanyuan Qi and Qinlong Wang and Chuchu Huang and Bo Tang and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The Information Extraction systems of BUPT{\_}PRIS at {TREC2014} Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BUPT\_PRIS\_ts.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiWHTXCG14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2014 Temporal Summarization Track

_Yun Zhao, Fei Yao, Huayang Sun, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./tempsumm/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BJUT_ts.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BJUT_ts.pdf)
- :material-file-search: **Runs:** [Q0](./tempsumm/runs.md#q0) | [Q2](./tempsumm/runs.md#q2) | [Q1](./tempsumm/runs.md#q1)

??? abstract "Abstract"
	
	This paper describes the second participation of BJUT in the temporal summarization track. We performed the experiments on the TREC KBA 2014 stream corpus using the classic information retrieval models, such as BM25, vector space model. Also, we introduce the details of our system, which consists of corpus pre-processing, information retrieval module and information process module.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoYSY14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoYSY14,
		author = {Yun Zhao and Fei Yao and Huayang Sun and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2014 Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BJUT\_ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoYSY14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2014: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Web Tracks

_Richard McCreadie, Romain Deveaud, M-Dyaa Albakour, Stuart Mackie, Nut Limsopatham, Craig Macdonald, Iadh Ounis, Thibaut Thonet, Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./tempsumm/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-uogTr_cs-ts-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-uogTr_cs-ts-web.pdf)
- :material-file-search: **Runs:** [uogTr4ARas](./tempsumm/runs.md#uogtr4aras) | [uogTr2A](./tempsumm/runs.md#uogtr2a) | [uogTr4A](./tempsumm/runs.md#uogtr4a) | [uogTr4AC](./tempsumm/runs.md#uogtr4ac)

??? abstract "Abstract"
	
	In TREC 2014, we focus on tackling the challenges posed by the Contextual Suggestion and Temporal Summarisation tracks, as well as enhancing our existing technologies to tackle risk-sensitivity as part of the Web track, building upon our Terrier Information Retrieval Platform. In particular, for the Contextual Suggestion track, we propose a novel bundled venue retrieval approach and experiment with text-based summarisation for building the venue description. For our participation to the Temporal Summarisation track, we propose a general framework for performing summarisation over time and two new real-time filtering approaches that leverage the semi-structured nature of news articles to enhance summary coverage. For the TREC Web track, we investigated a novel risk-sensitive learning to rank approach that is based on hypothesis testing and examined approaches that selectively apply different retrieval techniques based upon the query, with the aim of minimising risk.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieDAMLMO14.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieDAMLMO14,
		author = {Richard McCreadie and Romain Deveaud and M{-}Dyaa Albakour and Stuart Mackie and Nut Limsopatham and Craig Macdonald and Iadh Ounis and Thibaut Thonet and Bekir Taner Din{\c{c}}er},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow at {TREC} 2014: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Web Tracks},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-uogTr\_cs-ts-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieDAMLMO14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Session 

#### Overview of the TREC 2014 Session Track

_Ben Carterette, Evangelos Kanoulas, Mark M. Hall, Paul D. Clough_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/overview-session.pdf](http://trec.nist.gov/pubs/trec23/papers/overview-session.pdf)
??? abstract "Abstract"
	
	The TREC Session track ran for the fourth time in 2014. The track has the primary goal of providing test collections and evaluation measures for studying information retrieval over user sessions rather than one-time queries. These test collections are meant to be portable, reusable, statistically powerful, and open to anyone that wishes to work on the problem of retrieval over sessions. The experimental design of the track was similar to that of the previous three years [5, 6, 1]: sessions were real user sessions with a search engine that include queries, retrieved results, clicks, and dwell times; retrieval tasks were designed to study the effect of using session data in retrieval for only the mth query in a session. For the 2014 track, sessions were obtained from workers on Amazon's Mechanical Turk. As a result, the 2014 data includes far more sessions than previous years—1,257 unique sessions as compared to around 100 for each of the previous three years. Apart from that, there is little different from the 2013 track [1]. This overview is organized as follows: in Section 2 we describe the tasks participants were to perform. In Section 3 we describe the corpus, topics, and sessions that comprise the test collection. Section 4 gives some information about submitted runs. In Section 5 we describe relevance judging and evaluation measures, and Sections 6 present evaluation results and analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarteretteKHC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarteretteKHC14,
		author = {Ben Carterette and Evangelos Kanoulas and Mark M. Hall and Paul D. Clough},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2014 Session Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/overview-session.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarteretteKHC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SIRA: TREC Session Track 2014

_Brennan Bushee, Drew Pintus, Patrick Smith, Sharon Gower Small_

- :fontawesome-solid-user-group: **Participant:** [SCIAITeam](./session/participants.md#sciaiteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-SCIAITeam_session.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-SCIAITeam_session.pdf)
- :material-file-search: **Runs:** [SCIAITeamF.RL1](./session/runs.md#sciaiteamf.rl1) | [SCIAITeamF.RL2](./session/runs.md#sciaiteamf.rl2) | [SCIAITeamC.RL1](./session/runs.md#sciaiteamc.rl1) | [SCIAITeamC.RL2](./session/runs.md#sciaiteamc.rl2) | [SCIAITeamL.RL1](./session/runs.md#sciaiteaml.rl1) | [SCIAITeamL.RL2](./session/runs.md#sciaiteaml.rl2)

??? abstract "Abstract"
	
	This paper discusses Siena's Interactive Research Assistant's (SIRA) participation in the Text Retrieval Conference (TREC) Session Track of 2014. The overall goal of this track is to improve search results during query sessions based on a user's behavior. Query sessions include many aspects of a search, including query topics, initial retrieved webpages, clicked on links, visit times, etc. SIRA has used several methods to improve search results that will be discussed in this paper. Each method of query expansion utilized clicked-on and non-clicked-on links, pages with the longest visited time, and N-Percent (N%) of each page. Two of our three submissions improved over our baseline results and both of these were equal to the median submission for all participants in the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BusheePSS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/BusheePSS14,
		author = {Brennan Bushee and Drew Pintus and Patrick Smith and Sharon Gower Small},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{SIRA:} {TREC} Session Track 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-SCIAITeam\_session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BusheePSS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC WEB 2014: Entity Query Feature Expansion using Knowledge  Base Links

_Laura Dietz, Patrick Verga_

- :fontawesome-solid-user-group: **Participant:** [UMASS_CIIR](./session/participants.md#umass_ciir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UMASS_CIIR_session.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UMASS_CIIR_session.pdf)
- :material-file-search: **Runs:** [UMASS1.RL1](./session/runs.md#umass1.rl1) | [UMASS1.RL2](./session/runs.md#umass1.rl2) | [UMASS1.RL3](./session/runs.md#umass1.rl3) | [UMASS2.RL1](./session/runs.md#umass2.rl1) | [UMASS2.RL2](./session/runs.md#umass2.rl2) | [UMASS2.RL3](./session/runs.md#umass2.rl3) | [UMASS3.RL1](./session/runs.md#umass3.rl1) | [UMASS3.RL2](./session/runs.md#umass3.rl2) | [UMASS3.RL3](./session/runs.md#umass3.rl3) | [UMASS4.RL1](./session/runs.md#umass4.rl1) | [UMASS4.RL2](./session/runs.md#umass4.rl2) | [UMASS4.RL3](./session/runs.md#umass4.rl3)

??? abstract "Abstract"
	
	Entity linking tools predict links between entity mentions in text and knowledge base entries. In this work we leverage the rich semantic knowledge available through these links to understand relevance of documents for a query. We focus on the ad hoc task on the category A subset and demonstrate the benefit of entity-centric approaches even for non-entity queries like “dark chocolate health benefits”.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DietzV14.bib) "
	```
	@inproceedings{DBLP:conf/trec/DietzV14,
		author = {Laura Dietz and Patrick Verga},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UMass at {TREC} {WEB} 2014: Entity Query Feature Expansion using Knowledge Base Links},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UMASS\_CIIR\_session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DietzV14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Endicott College at 2014 TREC Session Track

_Henry Feild_

- :fontawesome-solid-user-group: **Participant:** [Endicott](./session/participants.md#endicott)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-Endicott-session.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-Endicott-session.pdf)
- :material-file-search: **Runs:** [ECxCGxPRF.RL1](./session/runs.md#ecxcgxprf.rl1) | [ECxCGxPRF.RL2](./session/runs.md#ecxcgxprf.rl2) | [ECxCGxPRF.RL3](./session/runs.md#ecxcgxprf.rl3) | [ECxSRMxOS.RL1](./session/runs.md#ecxsrmxos.rl1) | [ECxSRMxOS.RL2](./session/runs.md#ecxsrmxos.rl2) | [ECxSRMxOS.RL3](./session/runs.md#ecxsrmxos.rl3) | [ECxSRMxPRF.RL1](./session/runs.md#ecxsrmxprf.rl1) | [ECxSRMxPRF.RL2](./session/runs.md#ecxsrmxprf.rl2) | [ECxSRMxPRF.RL3](./session/runs.md#ecxsrmxprf.rl3)

??? abstract "Abstract"
	
	Endicott College submitted three runs to Task 1 of the 2014 TREC Session Track. All runs reranked the baseline runs provided by the track organizers. One of the runs made use of a click graph to re-rank results for RL1, RL2, and RL3. The other two used relevance models computed over snippets from the session, and boosted their RL3 run using click graph recommendations. In the absence of clicks (e.g., RL1 and clickless sessions in RL2 and RL3), two of the runs used pseudo relevance feedback over the session, while the other used the unmodified baseline ranking. All runs used a similar pre-processing procedure, which we describe in Section 2. We then discuss our click graph re-ranking technique for the ECxCGxPRF run in Section 3 and the session relevance modeling technique for our ECxSRMxOS and ECxSRMxPRF runs in Section 4. We follow that with an analysis of the performance of our runs compared to each other, as well as the track minimums, medians, and maximums. Finally, we wrap up with some closing thoughts and future directions in Section 6.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Feild14.bib) "
	```
	@inproceedings{DBLP:conf/trec/Feild14,
		author = {Henry Feild},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Endicott College at 2014 {TREC} Session Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-Endicott-session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Feild14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Modeling Rich Interactions in Session Search - Georgetown University  at TREC 2014 Session Track

_Jiyun Luo, Xuchu Dong, Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [Georgetown](./session/participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-Georgetown_session.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-Georgetown_session.pdf)
- :material-file-search: **Runs:** [GUS14Run2.RL3](./session/runs.md#gus14run2.rl3) | [GUS14Run2.RL1](./session/runs.md#gus14run2.rl1) | [GUS14Run2.RL2](./session/runs.md#gus14run2.rl2) | [GUS14Run3.RL1](./session/runs.md#gus14run3.rl1) | [GUS14Run3.RL2](./session/runs.md#gus14run3.rl2) | [GUS14Run3.RL3](./session/runs.md#gus14run3.rl3) | [GUS14Run1.RL1](./session/runs.md#gus14run1.rl1) | [GUS14Run1.RL2](./session/runs.md#gus14run1.rl2) | [GUS14Run1.RL3](./session/runs.md#gus14run1.rl3)

??? abstract "Abstract"
	
	This year we participate in the TREC Session Track Task 1. We adopt the Query Change Model (QCM), weighted QCM, re-ranking, clustering, and error analysis in our approaches. The QCM retrieval model is employed to combine all queries in a session. QCM allows documents that are relevant to any query in a session to appear in the final retrieval list. Weighted QCM combines queries unevenly based on a prediction of query quality. It is based on the following intuition: if a query does not bring any document that leads to a SAT-Click from the user, it suggests that this query is poorly formed. Our re-ranking module is based on implicit feedback from the user; in this case the SAT-Clicked documents. The module boosts a document's ranking position if it has been SAT-Clicked in the session or in other sessions that share similar search topics. We apply K-means clustering algorithm to detect which sessions share similar search topics. Each unique term is one dimension of the vector and is weighted by its idf. We also apply session error analysis in RL3. From the query log, we first identify sessions with similar topics by clustering, then we use SAT-Clicks from most sessions to re-rank the documents for the sessions that the algorithm predicts as poorly issued sessions, i.e. more difficult session due to ill-form queries. Combining above approaches, we achieve a 20.9% nDCG@10 increment and a 13.0% P@10 increment from RL1 to RL2, and with utilization of the whole log data, we achieve a 4% nDCG@10 increment and a 0.5% P@10 increment from RL2 to RL3.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuoDY14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuoDY14,
		author = {Jiyun Luo and Xuchu Dong and Hui Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Modeling Rich Interactions in Session Search - Georgetown University at {TREC} 2014 Session Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-Georgetown\_session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuoDY14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Session Track TREC2014

_Yuanhai Xue, Guoxin Cui, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./session/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_session.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_session.pdf)
- :material-file-search: **Runs:** [ICTNET14SER1.RL1](./session/runs.md#ictnet14ser1.rl1) | [ICTNET14SER1.RL2](./session/runs.md#ictnet14ser1.rl2) | [ICTNET14SER1.RL3](./session/runs.md#ictnet14ser1.rl3) | [ICTNET14SER2.RL1](./session/runs.md#ictnet14ser2.rl1) | [ICTNET14SER2.RL2](./session/runs.md#ictnet14ser2.rl2) | [ICTNET14SER2.RL3](./session/runs.md#ictnet14ser2.rl3) | [ICTNET14SER3.RL1](./session/runs.md#ictnet14ser3.rl1) | [ICTNET14SER3.RL2](./session/runs.md#ictnet14ser3.rl2) | [ICTNET14SER3.RL3](./session/runs.md#ictnet14ser3.rl3)

??? abstract "Abstract"
	
	In this paper, we describe our solutions of the Session Track at TREC 2014. Our main idea is to re-rank the documents the official supplies as RL1. In order to get good results of the re-ranked documents, we implement the learning to rank model which needs to extract some features. We use the relevance judgments of Session Track TREC 2013 as training set this year and also we use it as testing set by 5-fold cross-validation. The rest of this paper is organized as follows. We detail our models in section 2. Section 3 describes our experiments, including our evaluation results. Conclusions are made in the last session.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XueCYLC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/XueCYLC14,
		author = {Yuanhai Xue and Guoxin Cui and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Session Track {TREC2014}},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET\_session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XueCYLC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Delaware at TREC 2014

_Ashraf Bah, Karankumar Sabhnani, Mustafa Zengin, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [udel](./session/participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf)
- :material-file-search: **Runs:** [udelitu.RL1](./session/runs.md#udelitu.rl1) | [udel14Run1.RL3](./session/runs.md#udel14run1.rl3) | [udel14Run1.RL1](./session/runs.md#udel14run1.rl1)

??? abstract "Abstract"
	
	This paper describes the work of the Information Retrieval Lab at the University of Delaware (team name “udel”) on TREC 2014 tracks. We participated in five different tracks: Contextual Suggestion, Federated Web, Microblog, Session, and Web.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BahSZC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/BahSZC14,
		author = {Ashraf Bah and Karankumar Sabhnani and Mustafa Zengin and Ben Carterette},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Delaware at {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_cs-federated-microblog-web-sesson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BahSZC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2014: Web, Session, and Contextual Suggestion Tracks

_Matthias Hagen, Steve Goering, Maximilian Michel, Georg Müller, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [BUW](./session/participants.md#buw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BUW_cs-session-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BUW_cs-session-web.pdf)
- :material-file-search: **Runs:** [webis2014act.RL1](./session/runs.md#webis2014act.rl1) | [webis2014act.RL2](./session/runs.md#webis2014act.rl2) | [webis2014act.RL3](./session/runs.md#webis2014act.rl3) | [webis2014db.RL2](./session/runs.md#webis2014db.rl2) | [webis2014db.RL3](./session/runs.md#webis2014db.rl3) | [webis2014db.RL1](./session/runs.md#webis2014db.rl1) | [webisSt14ax.RL3](./session/runs.md#webisst14ax.rl3) | [webisSt14ax.RL1](./session/runs.md#webisst14ax.rl1) | [webisSt14ax.RL2](./session/runs.md#webisst14ax.rl2)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2014 Web, Session and Contex tual Suggestion tracks. All our runs for the Web and the Session track are on the full ClueWeb12 and use the online Indri retrieval system hosted at CMU. Our runs for the Contextual Suggestion track are based on the open web. As for the Web track, our runs are aimed at one research question: whether using axioms for re-ranking a baseline result list improve the retrieval performance. Therefore, we implement the axioms available in the axiomatic IR literature and combine them with new axioms aimed at term proximity. Trained on the TREC 2013 Web track data, three promising combinations of axioms are identified in a large-scale experiment and used for our three runs. As for the session track, we tackle three research questions in three different runs. First, similar to the Web track, we examine whether an axiom combination helps to improve session retrieval. Second, we examine the effect of presenting relevant documents from previous years when they seem to be related to the current queries of the 2014 data. Our third question is whether the user interactions can be used to train an activation model to predict relevant documents for new queries. As for the contextual suggestion track, our research question is whether explanations based on the user profile and explaining why specific entities are suggested by the system are perceived positively or negatively by the user. Our focus is not explicitly on finding the most relevant suggestions but rather on examining the effect of different descriptions. Thus, the system for finding the suggestions is simply based on techniques shown promising in the previous years. Our first run uses “standard” descriptions while in the second run the standard description is enriched by a profile specific sentence explaining the reasoning underlying the suggestion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenGMMS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenGMMS14,
		author = {Matthias Hagen and Steve Goering and Maximilian Michel and Georg M{\"{u}}ller and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2014: Web, Session, and Contextual Suggestion Tracks},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BUW\_cs-session-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenGMMS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

