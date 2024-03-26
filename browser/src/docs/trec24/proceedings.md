# Proceedings 2015 

## Clinical Decision Support 

#### Overview of the TREC 2015 Clinical Decision Support Track

_Kirk Roberts, Matthew S. Simpson, Ellen M. Voorhees, William R. Hersh_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Overview-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/Overview-CL.pdf)
??? abstract "Abstract"
	
	In making clinical decisions, physicians often seek out information about how to best care for their patients. Information relevant to a physician can be related to a variety of clinical tasks such as (i) determining a patient's most likely diagnosis given a list of symptoms, (ii) determining if a particular test is indicated for a given situation, and (iii) deciding on the most effective treatment plan for a patient having a known condition. In some cases, physicians can find the information they seek in published biomedical literature. However, given the volume of the existing literature and the rapid pace at which new research is published, locating the most relevant and timely information for a particular clinical need can be a daunting and time-consuming task. In order to make biomedical information more accessible and to meet the requirements for the meaningful use of electronic health records (EHRs), a goal of modern clinical decision support systems is to anticipate the needs of physicians by linking EHRs with information relevant for patient care. The goal of the 2015 TREC Clinical Decision Support (CDS) track was to evaluate biomedical literature retrieval systems for providing answers to generic clinical questions about patient cases. Short case reports, such as those published in biomedical articles and used in medical lectures, acted as idealized representations of medical records. A case report typically describes a challenging medical case. It is organized as a well-formed narrative summarizing the pertient portions of the patient's medical record. Given a case, participants were challenged with retrieving full-text biomedical articles relevant for answering questions related to one of three generic clinical information needs. The three needs were: Diagnosis (i.e., “What is this patient's diagnosis?”), Test (“What diagnostic test is appropriate for this patient?”), and Treatment (“What treatment is appropriate for this patient?”). Retrieved articles were judged relevant if they provided information of the specified type useful for the given case. The assessment was performed by physicians with training in biomedical informatics. The evaluation of individual submissions followed standard TREC procedures. The 2015 CDS track differed from the 2014 CDS track (Simpson et al., 2014) by offering two tasks. Task A mirrored the 2014 CDS track, only with 30 new topics/cases. Task B used the same topics from Task A, but included the patient diagnosis for the Test and Treatment topics. Since the diagnosis was not guaranteed to be written in the case (consistent with how physicians often write cases in practice), we theorized that providing the diagnosis may improve retrieval systems by (a) providing additional relevant information if the diagnosis is not stated in the case, or (b) emphasizing a key piece of information in the case if the diagnosis is stated. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsSVH15.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsSVH15,
		author = {Kirk Roberts and Matthew S. Simpson and Ellen M. Voorhees and William R. Hersh},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2015 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Overview-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsSVH15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LIST at TREC 2015 Clinical Decision Support Track: Question Analysis  and Unsupervised Result Fusion

_Asma Ben Abacha, Saoussen Khelifi_

- :fontawesome-solid-user-group: **Participant:** [LIST_LUX](./clinical/participants.md#list_lux)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/LIST_LUX-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/LIST_LUX-CL.pdf)
- :material-file-search: **Runs:** [Run1DBpSimp](./clinical/runs.md#run1dbpsimp) | [Run2DBpComb](./clinical/runs.md#run2dbpcomb) | [Run4HLM](./clinical/runs.md#run4hlm) | [Run5DBpAbs](./clinical/runs.md#run5dbpabs)

??? abstract "Abstract"
	
	This paper describes our information retrieval approaches to the TREC 2015 Clinical Decision Support Track. We explore di↵erent question analysis methods in order to retrieve articles relevant to the given clinical questions. We particularly study the use of two knowledge sources: MeSH and DBpedia for question expansion and the simplification of questions by removing information about the patient and negation. We also compare single IR models with the fusion of results based on both ranks and scores. Our experiments conclude that (i) query expansion using Mesh and DBpedia improves the results and that (ii) the combination of IR results using the rank outperforms the fusion based on scores. For TREC 2015 CDS task A, our best results were obtained by using DBpedia for query expansion and by combining the 2 IR models Hiemstra LM and LGD using a rank-based method. Our best run achieved an infNDCG score of 0.2894 and was ranked second over 92 runs for task A.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbachaK15.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbachaK15,
		author = {Asma Ben Abacha and Saoussen Khelifi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{LIST} at {TREC} 2015 Clinical Decision Support Track: Question Analysis and Unsupervised Result Fusion},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/LIST\_LUX-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AbachaK15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### EMSE at TREC 2015 Clinical Decision Support Track

_Bissan Audeh, Michel Beigbeder_

- :fontawesome-solid-user-group: **Participant:** [EMSE](./clinical/participants.md#emse)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/EMSE-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/EMSE-CL.pdf)
- :material-file-search: **Runs:** [EMSEasmer](./clinical/runs.md#emseasmer) | [EMSElsi](./clinical/runs.md#emselsi) | [EMSErm3](./clinical/runs.md#emserm3)

??? abstract "Abstract"
	
	This paper describes the participation of the EMSE team at the clinical decision support track of TREC 2015 (Task A). Our team submitted three automatic runs based only on the summary field. The baseline run uses the summary field as a query and the query likelihood retrieval model to match articles. Other runs explore different approaches to expand the summary field: RM3, LSI with pseudo relevant documents, semantic ressources of UMLS, and a hybrid approach called SMERA that combines LSI and UMLS based approaches. Only three of our runs were considered for the 2015 campaign: RM3, LSI and SMERA.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AudehB15.bib) "
	```
	@inproceedings{DBLP:conf/trec/AudehB15,
		author = {Bissan Audeh and Michel Beigbeder},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{EMSE} at {TREC} 2015 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/EMSE-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AudehB15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WSU-IR at TREC 2015 Clinical Decision Support Track: Joint Weighting  of Explicit and Latent Medical Query Concepts from Diverse Sources

_Saeid Balaneshinkordan, Alexander Kotov, Railan Xisto_

- :fontawesome-solid-user-group: **Participant:** [wsu_ir](./clinical/participants.md#wsu_ir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/wsu_ir-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/wsu_ir-CL.pdf)
- :material-file-search: **Runs:** [wsuirsaa](./clinical/runs.md#wsuirsaa) | [wsuirdaa](./clinical/runs.md#wsuirdaa) | [wsuirdma](./clinical/runs.md#wsuirdma) | [wsuirsab](./clinical/runs.md#wsuirsab) | [wsuirdmb](./clinical/runs.md#wsuirdmb) | [wsuirsmb](./clinical/runs.md#wsuirsmb)

??? abstract "Abstract"
	
	This paper describes participation of WSU-IR group in TREC 2015 Clinical Decision Support (CDS) track. We present a Markov Random Fields-based retrieval model and an optimization method for jointly weighting statistical and semantic unigram, bigram and multi-phrase concepts from the query and PRF documents as well as three specific instantiations of this model that we used to obtain the runs submitted for each task in this track. These instantiations consider different types of concepts and use different parts of topics as queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Balaneshinkordan15.bib) "
	```
	@inproceedings{DBLP:conf/trec/Balaneshinkordan15,
		author = {Saeid Balaneshinkordan and Alexander Kotov and Railan Xisto},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{WSU-IR} at {TREC} 2015 Clinical Decision Support Track: Joint Weighting of Explicit and Latent Medical Query Concepts from Diverse Sources},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/wsu\_ir-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Balaneshinkordan15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LAMDA at TREC CDS track 2015 - Clinical Decision Support Track

_Moon Soo Cha, Woo-Jin Han, Garam Lee, Minsung Kim, Kyung-Ah Sohn_

- :fontawesome-solid-user-group: **Participant:** [LAMDA](./clinical/participants.md#lamda)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/LAMDA-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/LAMDA-CL.pdf)
- :material-file-search: **Runs:** [lamdarun01](./clinical/runs.md#lamdarun01) | [lamdarun02](./clinical/runs.md#lamdarun02) | [lamdarun03](./clinical/runs.md#lamdarun03) | [lamdarun04](./clinical/runs.md#lamdarun04) | [lamdarun05](./clinical/runs.md#lamdarun05) | [lamdarun06](./clinical/runs.md#lamdarun06)

??? abstract "Abstract"
	
	In TREC 2015 Clinical Decision Support Track, our goal is to retrieve the relevant medical articles for the questions about medical statement. We propose three main strategies of indexing, query expansion, and the ranking method. In the indexing stage, each medical article is indexed into 3 different fields: title, abstract, and body. Before querying, related words are appended to the query at the query expansion stage. Our system returns the score of each field corresponding to the query for all documents. The score of each field is calculated using Divergence-from-randomness (DFR) probabilistic model. With the 3 scores from each field, the total score is calculated as the weighted sum of each score. Finally, we pick up top 1000 documents and send the list of the articles for evaluation. To make it easier for building the IR system, Elasticsearch and MetaMap are adopted for general IR operations and query expansion, respectively. Elasticsearch supports the similarity module that defines how matching documents are scored. In our IR system, Divergence-from-randomness model is adopted for probabilistic term vector space model because it is figured out that DFR outperforms all the other vector space models supported by Elasticsearch. MetaMap is the online tool that maps biomedical text to the Metathesaurus, and its semantic type. Query expansion is executed by extracting the semantic type from the description of the question, and appending words in the same semantic types to the query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChaHLKS15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChaHLKS15,
		author = {Moon Soo Cha and Woo{-}Jin Han and Garam Lee and Minsung Kim and Kyung{-}Ah Sohn},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{LAMDA} at {TREC} {CDS} track 2015 - Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/LAMDA-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChaHLKS15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Clinical Decision Support with the SPUD Language Model

_Ronan Cummins_

- :fontawesome-solid-user-group: **Participant:** [CL_CAMB](./clinical/participants.md#cl_camb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/CL_CAMB-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/CL_CAMB-CL.pdf)
- :material-file-search: **Runs:** [CAMspud1](./clinical/runs.md#camspud1) | [CAMspud3](./clinical/runs.md#camspud3) | [CAMspud5](./clinical/runs.md#camspud5) | [CAMspud6](./clinical/runs.md#camspud6) | [CAMspud7](./clinical/runs.md#camspud7) | [CAMspud8](./clinical/runs.md#camspud8)

??? abstract "Abstract"
	
	In this paper we present the systems and techniques used by the University of Cambridge for the CDS (Clinical Decision Support) track of the 24th Text Retrieval Conference (TREC). The system was among the best automatic approaches for both CDS tasks and is based on a new language modelling approach implemented using Lucene.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Cummins15.bib) "
	```
	@inproceedings{DBLP:conf/trec/Cummins15,
		author = {Ronan Cummins},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Clinical Decision Support with the {SPUD} Language Model},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/CL\_CAMB-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Cummins15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LIMSI @ 2015 Clinical Decision Support Track

_Eva D'hondt, Brigitte Grau, Pierre Zweigenbaum_

- :fontawesome-solid-user-group: **Participant:** [LIMSI](./clinical/participants.md#limsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/LIMSI-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/LIMSI-CL.pdf)
- :material-file-search: **Runs:** [LIMSIrun1BoW](./clinical/runs.md#limsirun1bow) | [LIMSIrun2MSH](./clinical/runs.md#limsirun2msh) | [LIMSIrun3SmF](./clinical/runs.md#limsirun3smf) | [LIMSIrun4Syn](./clinical/runs.md#limsirun4syn) | [LIMSIrun5MPF](./clinical/runs.md#limsirun5mpf) | [LIMSIrun6Wik](./clinical/runs.md#limsirun6wik)

??? abstract "Abstract"
	
	In this paper we present our participation to the 2015 TREC Clinical Decision Support (CDS) Track. The goal of this track is to find relevant medical literature for a given medical case report which should help address a specific clinical aspect of the case (known as the Clinical Question Type). We investigated the relative merit of concept-versus word-based representations of the information contained in the case reports, and experimented with different approaches to model Clinical Question Types. We submitted six runs in total, three for subtask A (CDS search without information on the patient's diagnosis) and subtask B (CDS search with information on the patient's diagnosis for topics from the Test and Treatment Clinical Question Types). In both subtasks our best runs were MeSH-based, and they achieved a P@10 and infNDCG of 0.37 and 0.25, and 0.47 and 0.35, for subtask A and B respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DhondtGZ15.bib) "
	```
	@inproceedings{DBLP:conf/trec/DhondtGZ15,
		author = {Eva D'hondt and Brigitte Grau and Pierre Zweigenbaum},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{LIMSI} @ 2015 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/LIMSI-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DhondtGZ15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTH at TREC 2015 Clinical Decision Support Track

_George Drosatos, Stefanos Roumeliotis, Eleni Kaldoudi, Avi Arampatzis_

- :fontawesome-solid-user-group: **Participant:** [DUTH](./clinical/participants.md#duth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/DUTH-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/DUTH-CL.pdf)
- :material-file-search: **Runs:** [DuthStef](./clinical/runs.md#duthstef) | [DuthMmMt16s](./clinical/runs.md#duthmmmt16s) | [DuthMmMt16f](./clinical/runs.md#duthmmmt16f) | [DuthBaseF](./clinical/runs.md#duthbasef) | [DuthBaseS](./clinical/runs.md#duthbases) | [DuthMmMtB16f](./clinical/runs.md#duthmmmtb16f)

??? abstract "Abstract"
	
	In this report we give an overview of our participation in the TREC 2015 Clinical Decision Support Track. We present two approaches for pre-processing and indexing of the open-access PubMed articles, and four methods for query construction which are applied to the previous two approaches. Regarding pre-processing, our main assumption is that only particular medical study designs are appropriate for each type of clinical question and we filter the number of articles in each clinical question type. Regarding query construction, our main idea is to detect the medical concepts in the medical cases and to expand them with terms of semantic controlled vocabularies (such as UMLS). The track evaluation shows that our approaches provide comparable results with the other participants' approaches without to conclude on safe findings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DrosatosRKA15.bib) "
	```
	@inproceedings{DBLP:conf/trec/DrosatosRKA15,
		author = {George Drosatos and Stefanos Roumeliotis and Eleni Kaldoudi and Avi Arampatzis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DUTH} at {TREC} 2015 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/DUTH-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DrosatosRKA15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Entity-based Stochastic Analysis of Search Results for Query Expansion  and Results Re-Ranking

_Pavlos Fafalios, Yannis Tzitzikas_

- :fontawesome-solid-user-group: **Participant:** [FORTH_ICS_ISL](./clinical/participants.md#forth_ics_isl)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/FORTH_ICS_ISL-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/FORTH_ICS_ISL-CL.pdf)
- :material-file-search: **Runs:** [FORTHICSd0](./clinical/runs.md#forthicsd0) | [FORTHICSd2](./clinical/runs.md#forthicsd2) | [FORTHICSs0](./clinical/runs.md#forthicss0) | [FORTHICSd0e7](./clinical/runs.md#forthicsd0e7) | [FORTHICSdQE](./clinical/runs.md#forthicsdqe) | [FORTHICSdQER](./clinical/runs.md#forthicsdqer)

??? abstract "Abstract"
	
	In this paper we introduce a method for exploiting entities from the emerging Web of Data for enhancing various Information Retrieval (IR) services. The approach is based on named-entity recognition applied in a set of search results, and on a graph of documents and identified entities that is constructed dynamically and analyzed stochastically using a Random Walk method. The result of this analysis is exploited in two different contexts: for automatic query expansion and for re-ranking a set of retrieved results. Evaluation results in the 2015 TREC Clinical Decision Support Track illustrate that query expansion can increase recall by retrieving more relevant hits, while re-ranking can notably improve the ranked list of results by moving relevant but low-ranked hits in higher positions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FafaliosT15.bib) "
	```
	@inproceedings{DBLP:conf/trec/FafaliosT15,
		author = {Pavlos Fafalios and Yannis Tzitzikas},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Entity-based Stochastic Analysis of Search Results for Query Expansion and Results Re-Ranking},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/FORTH\_ICS\_ISL-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FafaliosT15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke: TREC 2015 Clinical Decision Support Track

_Amira Ghenai, Eldar Khalilov, Pavel Valov, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./clinical/participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-CL.pdf)
- :material-file-search: **Runs:** [UWCSolrBM25](./clinical/runs.md#uwcsolrbm25) | [UWCPL2](./clinical/runs.md#uwcpl2) | [UWCSolrTerr](./clinical/runs.md#uwcsolrterr)

??? abstract "Abstract"
	
	Clinical decision support systems help physicians with finding additional information about a particular medical case. In this paper, we develop a clinical decision support system that, based on a short medical case description, can recommend research articles to answer some common medical questions (diagnosis, test and treatment articles). The two different full-text search engines we adopted in order to search over the collection of articles are Terrier and Apache Solr. We test each search engine with different settings and retrieval algorithms. Additionally, we combine the results of the two different search engines using reciprocal rank fusion. The evaluation of the submitted runs using partially marked results of Text Retrieval Conference (TREC) from the previous year shows that the methodologies are promising.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GhenaiKVC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/GhenaiKVC15,
		author = {Amira Ghenai and Eldar Khalilov and Pavel Valov and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {WaterlooClarke: {TREC} 2015 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GhenaiKVC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting incoming and outgoing citations for improving Information  Retrieval in the TREC 2015 Clinical Decision Support Track

_Julien Gobeill, Arnaud Gaudinat, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [SIBtex](./clinical/participants.md#sibtex)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/SIBtex-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/SIBtex-CL.pdf)
- :material-file-search: **Runs:** [SIBTEX2CITIN](./clinical/runs.md#sibtex2citin) | [SIBTEX3CTOUT](./clinical/runs.md#sibtex3ctout) | [SIBTEX5COMBO](./clinical/runs.md#sibtex5combo)

??? abstract "Abstract"
	
	We investigated two strategies for improving Information Retrieval thanks to incoming and outgoing citations. We first started from settings that worked last year and established a baseline. Then, we tried to rerank this run. The incoming citations' strategy was to compute the number of incoming citations in PubMed Central, and to boost the score of the articles that were the most cited. The outgoing citations' strategy was to promote the references of the retrieved documents. Unfortunately, no significant improvement from the baseline was observed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GobeillGR15.bib) "
	```
	@inproceedings{DBLP:conf/trec/GobeillGR15,
		author = {Julien Gobeill and Arnaud Gaudinat and Patrick Ruch},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Exploiting incoming and outgoing citations for improving Information Retrieval in the {TREC} 2015 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/SIBtex-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GobeillGR15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Neural Embeddings for Diagnostic Inferencing in Clinical Question  Answering

_Sadid A. Hasan, Yuan Ling, Joey Liu, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna](./clinical/participants.md#prna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/prna-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/prna-CL.pdf)
- :material-file-search: **Runs:** [prna1](./clinical/runs.md#prna1) | [prna2](./clinical/runs.md#prna2) | [prna3](./clinical/runs.md#prna3) | [prnaB1](./clinical/runs.md#prnab1) | [prnaB2](./clinical/runs.md#prnab2) | [prnaB3](./clinical/runs.md#prnab3)

??? abstract "Abstract"
	
	In this paper, we describe our clinical question answering system implemented for the Text Retrieval Conference (TREC 2015) Clinical Decision Support (CDS) track. We submitted six runs for two related tasks using a multi-step approach that leverages Natural Language Processing (NLP) and neural embeddings to retrieve relevant biomedical articles for answering generic clinical questions. Evaluation results demonstrated that our system achieved higher scores for most clinical questions requiring answers that pertain to treatment and test/investigations, topics in which the ground-truth diagnoses were provided by the track organizers. However, our system was less accurate with questions requiring answers pertaining to diagnosis. We conclude that diagnostic inferencing may be the most important determinant of the accuracy of the clinical question answering systems, and that the use of neural embeddings and advanced deep learning techniques could help improve the quality of such systems in order to effectively support decision-making in patient care.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HasanLLF15.bib) "
	```
	@inproceedings{DBLP:conf/trec/HasanLLF15,
		author = {Sadid A. Hasan and Yuan Ling and Joey Liu and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Using Neural Embeddings for Diagnostic Inferencing in Clinical Question Answering},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/prna-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HasanLLF15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ECNU at 2015 CDS Track: Two Re-ranking Methods in Medical Information  Retrieval

_Qinmin Hu, Liang He, Yang Song, Yun He_

- :fontawesome-solid-user-group: **Participant:** [ECNU](./clinical/participants.md#ecnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/ECNU-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/ECNU-CL.pdf)
- :material-file-search: **Runs:** [ECNUPB](./clinical/runs.md#ecnupb) | [ecnu1](./clinical/runs.md#ecnu1) | [ecnu2](./clinical/runs.md#ecnu2) | [ECNUBP](./clinical/runs.md#ecnubp) | [ecnu3](./clinical/runs.md#ecnu3) | [ecnu4](./clinical/runs.md#ecnu4)

??? abstract "Abstract"
	
	This paper summarizes our work on the TREC 2015 Clinical Decision Support Track. We present a customized learning-to-rank algorithm and a query term position based re-ranking model to better satisfy the tasks. We design two learning-to-rank framework: the pointwise loss function based on random forest and the pairwise loss function based on SVM. The position based re-ranking model is composed of BM25 and a heuristic kernel function which integrates Gaussian, triangle, cosine and the circle kernel function. Furthermore, the Web-based query expansion method is utilized to improve the quality of the queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuHSH15.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuHSH15,
		author = {Qinmin Hu and Liang He and Yang Song and Yun He},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ECNU} at 2015 {CDS} Track: Two Re-ranking Methods in Medical Information Retrieval},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/ECNU-CL.pdf},
		timestamp = {Tue, 22 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuHSH15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Learning from Medical Summaries: The University of Michigan at TREC  2015 Clinical Decision Support Track

_Fengmin Hu, Danny T. Y. Wu, Qiaozhu Mei, V. G. Vinod Vydiswaran_

- :fontawesome-solid-user-group: **Participant:** [Foreseer](./clinical/participants.md#foreseer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Foreseer-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/Foreseer-CL.pdf)
- :material-file-search: **Runs:** [FusionAuto](./clinical/runs.md#fusionauto) | [FusionManual](./clinical/runs.md#fusionmanual) | [FusionMAll](./clinical/runs.md#fusionmall) | [FusionAutoB](./clinical/runs.md#fusionautob) | [FusionManB](./clinical/runs.md#fusionmanb) | [FusionAdv](./clinical/runs.md#fusionadv)

??? abstract "Abstract"
	
	The goal of TREC 2015 Clinical Decision Support Track was to retrieve biomedical articles relevant for answering three kinds of generic clinical questions, namely diagnosis, test, and treatment. In order to achieve this purpose, we investigated three approaches to improve the retrieval of relevant articles: modifying queries, improving indexes, and ranking with ensembles. Our final submissions were a combination of several different configurations of these approaches. Our system mainly focused on the summary fields of medical reports. We built two different kinds of indexes - an inverted index on the free text and a second kind of in- dexes on the Unified Medical Language System (UMLS) concepts within the entire articles that were recognized by MetaMap. We studied the variations of including UMLS concepts at paragraph and sentence level and experimented with different thresholds of MetaMap matching scores to filter UMLS concepts. The query modification process in our system involved automatic query construction, pseudo relevance feedback, and manual inputs from domain experts. Furthermore, we trained a re-ranking sub-system based on the results of TREC 2014 Clinical Decision Support track using Indri's Learning to Rank package, RankLib. Our experiments showed that the ensemble approach could improve the overall results by boosting the ranking of articles that are near the top of several single ranked lists.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuWMV15.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuWMV15,
		author = {Fengmin Hu and Danny T. Y. Wu and Qiaozhu Mei and V. G. Vinod Vydiswaran},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Learning from Medical Summaries: The University of Michigan at {TREC} 2015 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Foreseer-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HuWMV15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Siena's Clinical Decision Assistant

_Michael Ippolito, Katherine Small, Clayton Marr, Steven Gassert, Kylie Small, Sharon Gower Small_

- :fontawesome-solid-user-group: **Participant:** [SCIAITeam](./clinical/participants.md#sciaiteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Siena_SUCCESS-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/Siena_SUCCESS-CL.pdf)
- :material-file-search: **Runs:** [SCIAILuceneA](./clinical/runs.md#sciailucenea) | [RRFFused](./clinical/runs.md#rrffused) | [FrameAFinal](./clinical/runs.md#frameafinal) | [SCIAILuceneB](./clinical/runs.md#sciailuceneb) | [RRFfused](./clinical/runs.md#rrffused)

??? abstract "Abstract"
	
	This paper discusses Siena's Clinical Decision Assistant's (SCDA) system and its participation in the Text Retrieval Conference (TREC) Clinical Decision Support Track (CDST) of 2015. The overall goal of the 2015 track is to link medical cases to information that is pertinent to patient care. Participants were given a set of 30 topics in the form of medical case narratives and a snapshot of 733,138 articles from PubMed2 Central (PMC). The 30 topics were annotated into three major subsets: diagnosis, test and treatment, with ten of each type. Each topic serves as an idealized representation of actual medical records and includes both a description, which contains a complete account of the patient visit, and a summary, which is typically a one or two sentence summary of the main points in the description. SCDA used several methods to attempt improve the accuracy of medical cases retrieved. SCDA used the metathesaurus Unified Medical Language System (UMLS)3 that was implemented using MetaMap (NIH, 2013), query and document framing (Small and Stzalkowski 2004), a ranked fusion of document lists and Lucene for initial document indexing and retrieval. The track received a total of 178 runs from 36 different groups. We submitted three task A runs where our highest P(10) run was 0.3767 and two task B runs where our highest P(10) run was 0.4167. The highest P(10) from CDST TREC 20144 was 0.39. The word described here was performed by, and the entire SCDA system built by a team of undergraduate researchers working together for just ten weeks during the summer of 2015. The team was funded under the Siena College Institute for Artificial Intelligence's National Science Foundation's Research Experience for Undergraduates Grant.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/IppolitoSMGSS15.bib) "
	```
	@inproceedings{DBLP:conf/trec/IppolitoSMGSS15,
		author = {Michael Ippolito and Katherine Small and Clayton Marr and Steven Gassert and Kylie Small and Sharon Gower Small},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Siena's Clinical Decision Assistant},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Siena\_SUCCESS-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/IppolitoSMGSS15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HIT-WI at TREC 2015 Clinical Decision Support Track

_Jingchi Jiang, Yi Guan, Jia Su, Chao Zhao, Jinfeng Yang_

- :fontawesome-solid-user-group: **Participant:** [HITSJ](./clinical/participants.md#hitsj)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/HITSJ-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/HITSJ-CL.pdf)
- :material-file-search: **Runs:** [artificial](./clinical/runs.md#artificial) | [runindri](./clinical/runs.md#runindri) | [runindriML](./clinical/runs.md#runindriml) | [runindriB](./clinical/runs.md#runindrib) | [artificialB](./clinical/runs.md#artificialb) | [runnetwork](./clinical/runs.md#runnetwork)

??? abstract "Abstract"
	
	The TREC 2015 Clinical Decision Support track is composed of two subtasks, task A and task B. Similar to 2014 [1], the participants need to answer 30 clinical questions from patient cases for each task. According to the three types of clinical question: diagnosis, test and treatment, these tasks are to retrieve relevant literatures for helping clinicians to make clinical decision. This paper describes how the clinical decision support system is developed for completing the task A and B by the HIT-WI group. For the automatic runs, some classical retrieval strategies are adopted, including query extraction, query expansion and the process of retrieval. Moreover, we propose two novel re-ranking methods: the one uses SVM model with 10-dimensional feature to re-rank the retrieved list, and the other is based on word co-occurrence network. The 178 runs are submitted from 36 different groups. Our evaluation results show that 1) The Indri performs better than Lucene's for artificially-constructed queries. 2) Compare to the basic retrieval method, two re-ranking methods show the effectiveness in some topics. 3) Our results are higher than the median scores in most topics of task B. Furthermore, the system achieves the best scores for topics: #11 and #12.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangGSZY15.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangGSZY15,
		author = {Jingchi Jiang and Yi Guan and Jia Su and Chao Zhao and Jinfeng Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{HIT-WI} at {TREC} 2015 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/HITSJ-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangGSZY15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CBNU at TREC 2015 Clinical Decision Support Track

_Seung-Hyeon Jo, Kyung-Soon Lee, Jae-Wook Seol_

- :fontawesome-solid-user-group: **Participant:** [cbnu](./clinical/participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/cbnu-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/cbnu-CL.pdf)
- :material-file-search: **Runs:** [cbnu0](./clinical/runs.md#cbnu0) | [cbnu1](./clinical/runs.md#cbnu1) | [cbnu2](./clinical/runs.md#cbnu2) | [cbnu3](./clinical/runs.md#cbnu3) | [cbnu4](./clinical/runs.md#cbnu4) | [cbnu5](./clinical/runs.md#cbnu5)

??? abstract "Abstract"
	
	This paper describes the participation of the CBNU team at the TREC Clinical Decision Support track 2015. We propose a query expansion method based on a clinical semantic knowledge and a topic model. The clinical semantic knowledge is constructed by using medical terms extracted from Unified Medical Language System (UMLS) and Wikipedia articles. The word and document topics are generated by using a topic model for a document collection. The proposed methods achieved 0.2327 and 0.3033 in the inferred NDCG on Task A and Task B, respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoLS15.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoLS15,
		author = {Seung{-}Hyeon Jo and Kyung{-}Soon Lee and Jae{-}Wook Seol},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CBNU} at {TREC} 2015 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/cbnu-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoLS15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Investigation of Concept-based Proximity Matching - GRIUM@Clinical  Decision Support Track 2015 Task 1a

_Xiaojie Liu, Jian-Yun Nie_

- :fontawesome-solid-user-group: **Participant:** [GRIUM](./clinical/participants.md#grium)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/GRIUM-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/GRIUM-CL.pdf)
- :material-file-search: **Runs:** [GRIUMenRun1](./clinical/runs.md#griumenrun1) | [GRIUMenRun2](./clinical/runs.md#griumenrun2)

??? abstract "Abstract"
	
	Concepts are often used in Medical Information Retrieval. Previous studies showed that exact concept matching (using either the exact concept expression or concept IDs) is not effective, while using concept expressions for proximity matching is more effective. In our participation in Clinical Decision Support Track 2015 task 1a, we investigated the utilization of proximity matching based on concepts. Our results suggest that this matching strategy can be helpful. In this report, we describe the methods tested as well as their results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuN15.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuN15,
		author = {Xiaojie Liu and Jian{-}Yun Nie},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Investigation of Concept-based Proximity Matching - GRIUM@Clinical Decision Support Track 2015 Task 1a},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/GRIUM-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuN15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Domain Independent Approach to Clinical Decision Support

_Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [hltcoe](./clinical/participants.md#hltcoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/hltcoe-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/hltcoe-CL.pdf)
- :material-file-search: **Runs:** [hltcoe5srf](./clinical/runs.md#hltcoe5srf) | [hltcoe4srf](./clinical/runs.md#hltcoe4srf) | [hltcoewsrf](./clinical/runs.md#hltcoewsrf) | [hltcoe5sdrf](./clinical/runs.md#hltcoe5sdrf) | [hltcoe4sdrf](./clinical/runs.md#hltcoe4sdrf) | [hltcoewsdrf](./clinical/runs.md#hltcoewsdrf)

??? abstract "Abstract"
	
	Continuing our work from the inaugural running of the Clinical Decision Support track in 2014, we submitted runs to the 2015 evaluation. Our approach this year was very similar to that used in 2014 (Xu et al., 2014). Our submitted runs were created using the JHU HAIRCUT retrieval engine, and featured use of character n-gram indexing and use of pseudo-relevance feedback. The main contribution is investigating the retrieval of scientific medical documents using a domain independent approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McNamee15.bib) "
	```
	@inproceedings{DBLP:conf/trec/McNamee15,
		author = {Paul McNamee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Domain Independent Approach to Clinical Decision Support},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/hltcoe-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McNamee15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NovaSearch at TREC 2015 Clinical Decision Support Track

_André Mourão, Flávio Martins, João Magalhães_

- :fontawesome-solid-user-group: **Participant:** [NovaSearch](./clinical/participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/NovaSearch-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/NovaSearch-CL.pdf)

??? abstract "Abstract"
	
	This paper describes the participation of the NovaSearch group at TREC Clinical Decision Support 2015. For this year's task, we extended our rank fusion experiments from last year's edition using a supervised Learning to Fuse technique. Learning to Fuse is a technique that incrementally combines multiple runs that use different retrieval algorithms, relevance feedback schemes and query expansion data sources to create a better final rank. We also experimented with query expansion using MeSH, SNOMed CT and Shingles thesaurus and tested a Journal based filtering technique to remove results from irrelevant journals. For Task B runs, we added the diagnosis information to the queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MouraoMM15.bib) "
	```
	@inproceedings{DBLP:conf/trec/MouraoMM15,
		author = {Andr{\'{e}} Mour{\~{a}}o and Fl{\'{a}}vio Martins and Jo{\~{a}}o Magalh{\~{a}}es},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {NovaSearch at {TREC} 2015 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/NovaSearch-CL.pdf},
		timestamp = {Thu, 14 May 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MouraoMM15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2015 paper submission UWM-UO @ 2015 Clinical Decision Support  Track: QE by Weighted Keywords using PRF

_Xiangming Mu, Sukjin You_

- :fontawesome-solid-user-group: **Participant:** [UWM_UO](./clinical/participants.md#uwm_uo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/UWM_UO-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/UWM_UO-CL.pdf)
- :material-file-search: **Runs:** [UWMUO1](./clinical/runs.md#uwmuo1) | [UWMUO2](./clinical/runs.md#uwmuo2) | [UWMUO3](./clinical/runs.md#uwmuo3) | [UWMUO4](./clinical/runs.md#uwmuo4) | [UWMUO5](./clinical/runs.md#uwmuo5) | [UWMUO6](./clinical/runs.md#uwmuo6)

??? abstract "Abstract"
	
	In the 2015 CDS track, the queries have been expanded in four different ways which we called four different modes. The results shows statistically significantly improvement in terms of infAP, infNDCG and iP10 for some modes as compared to baseline mode which is generated using original query (summary) only without any expansion terms.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MuY15.bib) "
	```
	@inproceedings{DBLP:conf/trec/MuY15,
		author = {Xiangming Mu and Sukjin You},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2015 paper submission {UWM-UO} @ 2015 Clinical Decision Support Track: {QE} by Weighted Keywords using {PRF}},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/UWM\_UO-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MuY15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AUEB at TREC 2015: Clinical Decision Support Track

_Giannis Nikolentzos, Polykarpos Meladianos, Nektarios Liakis, Michalis Vazirgiannis_

- :fontawesome-solid-user-group: **Participant:** [DBNET_AUEB](./clinical/participants.md#dbnet_aueb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/DBNET_AUEB-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/DBNET_AUEB-CL.pdf)
- :material-file-search: **Runs:** [run1](./clinical/runs.md#run1) | [run2](./clinical/runs.md#run2) | [AUEBrun1B](./clinical/runs.md#auebrun1b) | [AUEBrun2B](./clinical/runs.md#auebrun2b)

??? abstract "Abstract"
	
	One of the goals of clinical decision support systems is to provide physicians information about how to best care for their patients. The Clinical Decision Support track organized by TREC, focuses on developing new techniques to retrieve articles from the biomedical literature relevant to the medical records of the patients. Due to the large volume of the existing literature and the diversity in the biomedical field, this is a very challenging task. This paper describes the two medical information retrieval systems designed by the Athens University of Economics and Business for participation in the 2015 Clinical Decision Support track. The two systems share many common features. Both made use of bi-grams along with unigrams for repesenting the documents. Both systems performed automatic query expansion using popular medical knowledge bases. However, the two systems employed different strategies to index the corpus which led to different retrieval methods. One utilized the vector space model with tf − idf term weighting, while the other the vector space model with tw − idf term weighting. The results showed that tf − idf outperformed tw − idf .
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NikolentzosMLV15.bib) "
	```
	@inproceedings{DBLP:conf/trec/NikolentzosMLV15,
		author = {Giannis Nikolentzos and Polykarpos Meladianos and Nektarios Liakis and Michalis Vazirgiannis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{AUEB} at {TREC} 2015: Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/DBNET\_AUEB-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NikolentzosMLV15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TUW @ TREC Clinical Decision Support Track 2015

_João R. M. Palotti, Allan Hanbury_

- :fontawesome-solid-user-group: **Participant:** [TUW](./clinical/participants.md#tuw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/TUW-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/TUW-CL.pdf)
- :material-file-search: **Runs:** [TUW1](./clinical/runs.md#tuw1) | [TUW2](./clinical/runs.md#tuw2) | [TUW3](./clinical/runs.md#tuw3) | [TUW4](./clinical/runs.md#tuw4) | [TUW5](./clinical/runs.md#tuw5) | [TUW6](./clinical/runs.md#tuw6)

??? abstract "Abstract"
	
	In this document, we describe the participation of Vienna University of Technology (TUW in German) in both tasks A and B of the TREC Clinical Decision Support (TREC-CDS) Track 2015. Based on the 2014 data, we concluded that query expansion with PRF resulted in large improvements over a BM25 baseline. Thus, we investigate a manner to add an intermediary layer based on a subset of the concepts annotated by MetaMap. This acts as a way to add weight to relevant concepts in the query and slightly expand the query with the preferred name of relevant concepts, before performing the query expansion with PRF. For TREC-CDS 2014, our method could reach a precision at 10 (P@10) of 0.40, while the best result of that year was 0.39. For 2015, we could reach a P@10 of 0.41 using the intermediary layer proposed, a small improvement over our baseline of P@10 of 0.39 when using only the original query expanded with PRF.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PalottiH15.bib) "
	```
	@inproceedings{DBLP:conf/trec/PalottiH15,
		author = {Jo{\~{a}}o R. M. Palotti and Allan Hanbury},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TUW} @ {TREC} Clinical Decision Support Track 2015},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/TUW-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PalottiH15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept based Information Retrieval for Clinical Case Summaries

_Jakob Stöber, Bret S. E. Heale, Kelley Fulghum, Guilherme Del Fiol, Heejun Kim, Kalpana Raja, Siddhartha Jonnalagadda_

- :fontawesome-solid-user-group: **Participant:** [NU_UU_UNC](./clinical/participants.md#nu_uu_unc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/NU_UU_UNC-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/NU_UU_UNC-CL.pdf)
- :material-file-search: **Runs:** [nuuuuncDFML](./clinical/runs.md#nuuuuncdfml) | [nuuuuncMDRUN](./clinical/runs.md#nuuuuncmdrun) | [nuuuuncHAKT](./clinical/runs.md#nuuuunchakt) | [nuuuuncHMKTB](./clinical/runs.md#nuuuunchmktb) | [nuuuuncMDRUB](./clinical/runs.md#nuuuuncmdrub) | [nuuuuncDFMLB](./clinical/runs.md#nuuuuncdfmlb)

??? abstract "Abstract"
	
	Objective: Query representation is a classic information retrieval (IR) problem. Forming appropriate query representations from clinical free-text adds additional complexity. We examined if external search engine mediated conceptualization based on expert knowledge, concept representation of the abstract, and application of machine learning improve the process of clinical information retrieval. Methods: Diagnosis concepts were derived through either using a Google Custom Search over a specific set of health-related websites or through manual, expert clinical diagnosis. We represented concepts both as text and UMLS concepts identified with MedTagger. Our approaches leverage Lucene indexing/searching of article full text, abstracts, titles and semantic representations. Additionally, we experimented with automatically generated diagnosis using Web search engines and the case summaries. Further, we utilized a variety of filters such as PubMed's Clinical Query filters, which retrieve articles with high scientific quality, and UMLS semantic type filters for search terms. In our final submission for the TREC 2015 CDS challenge, we focused on three approaches: 1. DFML/DFMLB: Combined ranking scores by data fusion and relevance probabilities derived by a machine learning method to offset ranking and classification errors. 2. HAKT/HMKTB: Used an iterative hierarchical search approach that progressively relaxed filters until we reached 1000 retrieved documents. 3. MDRUN/MDRUB: Manually added a diagnosis to each case and matched UMLS concepts by manual annotations with UMLS concepts in the case summaries. Results: The concepts extracted from search results are similar to the diagnosis concepts extracted from manual annotation by clinicians, and similar to the extracted concepts from the given diagnosis in task B. Two out of our three approaches performed above the median performance by all participants for both Task A and B. Overall, the run by manual diagnosis worked the best. The similarity between manual annotation by clinicians and given diagnosis in task B partially explains the performance of our algorithms. There was statistically significant difference in performance among our runs with two measures (R-prec and Prec@10) for Task A, but we could not find difference with other two measures (infNDCG and infAP) for Task A and all measures for Task B. Discussion: Our concept based approach avoids the need to remove stop words or stemming and reduces the need to look for synonyms. Conclusions: Overall, our major innovations are query transformation using diagnosis information inferred from Google searching of health resources, concept based query and document representation, and pruning of concepts based on semantic types and groups.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StoberHFFKRJ15.bib) "
	```
	@inproceedings{DBLP:conf/trec/StoberHFFKRJ15,
		author = {Jakob St{\"{o}}ber and Bret S. E. Heale and Kelley Fulghum and Guilherme Del Fiol and Heejun Kim and Kalpana Raja and Siddhartha Jonnalagadda},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Concept based Information Retrieval for Clinical Case Summaries},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/NU\_UU\_UNC-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StoberHFFKRJ15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDUMedSearch at TREC 2015 Clinical Decision Support Track

_Ronghui You, Shengwen Peng, Shanfeng Zhu, Yuanjie Zhou_

- :fontawesome-solid-user-group: **Participant:** [FDUDMIIP](./clinical/participants.md#fdudmiip)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/FDUDMIIP-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/FDUDMIIP-CL.pdf)
- :material-file-search: **Runs:** [FDUAuto1](./clinical/runs.md#fduauto1) | [FDUAuto2](./clinical/runs.md#fduauto2) | [FDUManual](./clinical/runs.md#fdumanual) | [FDUAuto](./clinical/runs.md#fduauto) | [FDUManual1](./clinical/runs.md#fdumanual1) | [FDUManual2](./clinical/runs.md#fdumanual2)

??? abstract "Abstract"
	
	This paper describes the participation of the FDUMedSearch team at TREC 2015 Clinical Decision Support track (CDS2015). Given the medical cases, the main purpose of CDS2015 is to develop effective information retrieval techniques in finding relevant documents for patient care. We used Indri as the retrieval engine, which implemented query likelihood method as the baseline. In addition, query expansion using Medical Subject Headings (MeSH), pseudo relevance feedback and classification were used to enhance the retrieval performance. We also tried to extract keywords in two different ways, automatically and manually. Experimental results show that our method achieved significant improvement over baseline methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YouPZZ15.bib) "
	```
	@inproceedings{DBLP:conf/trec/YouPZZ15,
		author = {Ronghui You and Shengwen Peng and Shanfeng Zhu and Yuanjie Zhou},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {FDUMedSearch at {TREC} 2015 Clinical Decision Support Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/FDUDMIIP-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YouPZZ15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CBIA VT at TREC 2015 Clinical Decision Support Track - Exploring  Relevance Feedback and Query Expansion in Biomedical Information Retrieval

_Sihui Zhang, Weiguo Fan, Bin He_

- :fontawesome-solid-user-group: **Participant:** [CBIA_VT](./clinical/participants.md#cbia_vt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/CBIA_VT-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/CBIA_VT-CL.pdf)
- :material-file-search: **Runs:** [QFB](./clinical/runs.md#qfb) | [UMLS](./clinical/runs.md#umls) | [PPR](./clinical/runs.md#ppr) | [QFBdiag](./clinical/runs.md#qfbdiag) | [UMLSdiag](./clinical/runs.md#umlsdiag) | [PPRdiag](./clinical/runs.md#pprdiag)

??? abstract "Abstract"
	
	We present the description and results of our participation in the Clinical Decision Support track at TREC 2015. In this task, our goal was to use clinical narratives to retrieve biomedical articles. We compared the performance of pseudo relevance feedback, query expansion based on UMLS synonyms, and query expansion with personalized PageRank. In addition, we investigated the impact of different query formulation on retrieval performance. We also give out future work in this area in the end.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangFH15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangFH15,
		author = {Sihui Zhang and Weiguo Fan and Bin He},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CBIA} {VT} at {TREC} 2015 Clinical Decision Support Track - Exploring Relevance Feedback and Query Expansion in Biomedical Information Retrieval},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/CBIA\_VT-CL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangFH15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Microblog 

#### Overview of the TREC-2015 Microblog Track

_Jimmy Lin, Miles Efron, Garrick Sherman, Yulu Wang, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec24/papers/Overview-MB.pdf](https://trec.nist.gov/pubs/trec24/papers/Overview-MB.pdf)
??? abstract "Abstract"
	
	The TREC 2015 Microblog track introduced a single real-time filtering task broken down into two scenarios. Our goal is to explore techniques for monitoring streams of social media posts with respect to users' interest profiles. An interest profile describes a topic about which the user wishes to receive information updates in real time, and is different from a typical ad hoc topic in that the profile represents a prospective (as opposed to a retrospective) information need. Thus, the nature of the desired information is qualitatively different. In real-time filtering, the goal is for a system to “push” (i.e., recommend, suggest) interesting and novel content to users in a timely fashion. We operationalized this task in terms of two scenarios: Scenario A (push notification): Content that is iden- tified as interesting and novel by a system based on the user's interest profile might be shown to the user as a notification on his or her mobile phone. The expectation is that such notifications are triggered a relatively short time after the content is generated. Scenario B (email digest): Content that is identified as interesting and novel by a system based on the user's interest profile might be aggregated into an email digest that is periodically sent to a user (e.g., nightly). It is assumed that each item of content is relatively short; one might think of these as “personalized headlines”. In both scenarios, it is assumed that the content items delivered to the users are relatively short. For expository convenience and to adopt standard information retrieval parlance, we write of users desiring relevant content, even though “relevant” in our context might be better operationalized as interesting, novel, and timely.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinESWV15.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinESWV15,
		author = {Jimmy Lin and Miles Efron and Garrick Sherman and Yulu Wang and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC-2015} Microblog Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {https://trec.nist.gov/pubs/trec24/papers/Overview-MB.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinESWV15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke: TREC 2015 Microblog Track

_Mustafa Abualsaud, Milad Ghaznavi, Daniel Recoskie, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./microblog/participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-MB.pdf)
- :material-file-search: **Runs:** [UWCMBE1](./microblog/runs.md#uwcmbe1) | [UWCMBP1](./microblog/runs.md#uwcmbp1) | [UWCMBE2](./microblog/runs.md#uwcmbe2) | [UWCMBP2](./microblog/runs.md#uwcmbp2)

??? abstract "Abstract"
	
	The goal of the TREC 2015 Microblog Track is to develop a real-time relevancy retrieval system that monitors a stream of social media posts and recommends relevant posts according to users' interests [1]. In this track, the representative social media is Twitter, and relevant posts are tweets with respect to a user's interest. A user's interest is represented by an interest profile containing a title, a description, and a narrative. Relevant tweets are recommended to the user in two tasks, push notification and periodic email digest. A. Push Notification Task:  The push notification task is meant to model a system that notifies the user in real-time on his/her mobile phone as it finds a relevant tweet. This notification, i.e. pushing a relevant tweet, is triggered in less than 100 minutes after the tweet creation time1. At most 10 tweets per day are pushed for each interest profile. B. Periodic Email Digest Task: The periodic email digest task aggregates a ranked-list of up to 100 relevant tweets for each interest profile into an email and sends it to the user at the end of every day.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbualsaudGRC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbualsaudGRC15,
		author = {Mustafa Abualsaud and Milad Ghaznavi and Daniel Recoskie and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {WaterlooClarke: {TREC} 2015 Microblog Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AbualsaudGRC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query-expansion Approaches for Microblog Retrieval

_Sandeep Avula, Jaime Arguello_

- :fontawesome-solid-user-group: **Participant:** [UNCSILS](./microblog/participants.md#uncsils)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/UNCSILS-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/UNCSILS-MB.pdf)
- :material-file-search: **Runs:** [UNCSILS_HRM](./microblog/runs.md#uncsils_hrm) | [UNCSILS_TRM](./microblog/runs.md#uncsils_trm) | [UNCSILS_WRM](./microblog/runs.md#uncsils_wrm)

??? abstract "Abstract"
	
	The School of Information and Library Science at the University of North Carolina at Chapel Hill submitted three runs to the “Scenario B” task of the TREC 2015 Microblog Track. The task simulates a scenario where a user specifies a topic of interest in the form of a keyword query and the system produces daily updates with at most 100 tweets about the topic of interest. Systems were responsible for monitoring a stream of tweets and making daily predictions for a set of 250 interest profiles. Each interest profile was in the form of a short keyword query. Systems were asked to produce a ranking of at most 100 tweets per interest profile at the end of each day (shortly after midnight). The evaluation period extended a 10-day period from July 20 to July 29, 2015. All tweets published between 00:00:00 to 23:59:59 UTC were valid candidates for each day of the evaluation period. Our team submitted three runs for “Scenario B”. All runs were automatic runs and used the interest profile title field as the input query. We explored three di↵erent ways of enriching the query representation through query expansion. In two of our runs (UNCSILS WRM and UNCSILS TRM), we scored tweets proportional to the negative KL-divergence between a relevance model generated from an external collection and the tweet language model. These two runs mainly differ by the external collection used to generate a relevance model for interest profile query. In our UNCSILS WRM run, we used an external Wikipedia corpus, and in our UNCSILS TRM run, we used a corpus of tweets collected during a three-week period prior to the evaluation period. In our third run (UNCSILS HRM), we aimed to expand the query with related hashtags.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AvulaA15.bib) "
	```
	@inproceedings{DBLP:conf/trec/AvulaA15,
		author = {Sandeep Avula and Jaime Arguello},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query-expansion Approaches for Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/UNCSILS-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AvulaA15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Burst Detection in Social Media Streams for Tracking Interest Profiles  in Real Time

_Cody Buntain, Jimmy Lin_

- :fontawesome-solid-user-group: **Participant:** [umd_hcil](./microblog/participants.md#umd_hcil)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/umd_hcil-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/umd_hcil-MB.pdf)
- :material-file-search: **Runs:** [umd_hcil_run01](./microblog/runs.md#umd_hcil_run01) | [umd_hcil_run02](./microblog/runs.md#umd_hcil_run02) | [umd_hcil_run03](./microblog/runs.md#umd_hcil_run03) | [umd_hcil_run04](./microblog/runs.md#umd_hcil_run04)

??? abstract "Abstract"
	
	This work described RTTBurst, an end-to-end system for ingesting a user's interest profiles that describe some topic of interest and identifying new tweets that might be of interest to that user using a simple model for bursts in token usage. We laid out RTTBurst's architecture, our participation in and performance at the TREC 2015 Microblog Track, and a post hoc analysis for increasing RTTBurst's performance. While not as relatively performant in the Microblog Track's real-time notification task, RTTBurst did perform well (ranking 4th overall and second in the automatic category of Scenario B) in providing daily summaries for various interest profiles. Following the official TREC evaluation period, we were also able to increase RTTBurst's performance but not by enough to significantly increase its overall ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuntainL15.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuntainL15,
		author = {Cody Buntain and Jimmy Lin},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Burst Detection in Social Media Streams for Tracking Interest Profiles in Real Time},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/umd\_hcil-MB.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BuntainL15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Microblog 2015

_Abdelhamid Chellal, Lamjed Ben Jabeur, Laure Soulier, Bilel Moulahi, Thomas Palmer, Mohand Boughanem, Karen Pinel-Sauvagnat, Lynda Tamine, Gilles Hubert_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./microblog/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/IRIT-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/IRIT-MB.pdf)
- :material-file-search: **Runs:** [IritSigSDA](./microblog/runs.md#iritsigsda) | [IritSigSDB](./microblog/runs.md#iritsigsdb) | [IRIT-KLTFIDF](./microblog/runs.md#irit-kltfidf) | [IRIT100KLTFIDF](./microblog/runs.md#irit100kltfidf) | [IRIT-RTDig.33](./microblog/runs.md#irit-rtdig.33) | [IRIT-RTNotif.33](./microblog/runs.md#irit-rtnotif.33)

??? abstract "Abstract"
	
	This paper presents the participation of the IRIT laboratory (University of Toulouse) to the Microblog Track of TREC 2015. This track consists in a real-time filtering task aiming at monitoring a stream of social media posts in accordance to a user's interest profile. In this context, our team proposes three approaches: (a) a novel selective summarization approach based on a decision of selecting/ignoring tweets without the use of external knowledge and relying on novelty and redundancy factors, (b) a processing workflow enabling to index tweets in real-time and enhanced by a notification and digests method guided by diversity and user personalization, and (c) a step by step stream selection method focusing on rapidity, and taking into account tweet similarity as well as several features including content, entities and user-related aspects. For all these approaches, we discuss the obtained results during the experimental evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChellalJSMPBPTH15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChellalJSMPBPTH15,
		author = {Abdelhamid Chellal and Lamjed Ben Jabeur and Laure Soulier and Bilel Moulahi and Thomas Palmer and Mohand Boughanem and Karen Pinel{-}Sauvagnat and Lynda Tamine and Gilles Hubert},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IRIT} at {TREC} Microblog 2015},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/IRIT-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChellalJSMPBPTH15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ECNU at TREC 2015: Microblog Track

_Qin Chen, Bo Wang, Beijing Huang, Qinmin Hu, Liang He_

- :fontawesome-solid-user-group: **Participant:** [ECNU](./microblog/participants.md#ecnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/ECNU-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/ECNU-MB.pdf)
- :material-file-search: **Runs:** [ECNURUNA1](./microblog/runs.md#ecnuruna1) | [ECNURUNA3](./microblog/runs.md#ecnuruna3) | [ECNURUNA2](./microblog/runs.md#ecnuruna2) | [ECNURUNB1](./microblog/runs.md#ecnurunb1) | [ECNURUNB2](./microblog/runs.md#ecnurunb2) | [ECNURUNB3](./microblog/runs.md#ecnurunb3)

??? abstract "Abstract"
	
	This paper describes our participation in TREC 2015 Microblog track, which includes two tasks related to Scenario A and Scenario B. For Scenario A, we build a real-time tweet push system, which is mainly composed by three parts: feature extraction, relevance prediction and redundancy detection. Only the highly relevant and nonredundant tweets are sent to users based on the interest profiles. For Scenario B, we apply three query expansion methods, namely the web search based, the TFIDF-PRF based and the Terrier embedded PRF based. In addition, three state-of-the-art information retrieval models as the language model, BM25 model and DFRee model are utilized. The retrieval results are combined for final delivery. The experimental results in both scenarios demonstrate that our system obtains convincing performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenWHHH15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenWHHH15,
		author = {Qin Chen and Bo Wang and Beijing Huang and Qinmin Hu and Liang He},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ECNU} at {TREC} 2015: Microblog Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/ECNU-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenWHHH15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Real Time Filtering of Tweets Using Wikipedia Concepts and Google  Tri-gram Semantic Relatedness

_Anh Dang, Raheleh Makki, Abidalrahman Moh'd, Aminul Islam, Vlado Keselj, Evangelos E. Milios_

- :fontawesome-solid-user-group: **Participant:** [DalTREC](./microblog/participants.md#daltrec)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/DalTREC-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/DalTREC-MB.pdf)
- :material-file-search: **Runs:** [DALTREC_B_PREP](./microblog/runs.md#daltrec_b_prep) | [DALTRECAA1](./microblog/runs.md#daltrecaa1) | [DALTRECMA1](./microblog/runs.md#daltrecma1) | [DALTRECMA2](./microblog/runs.md#daltrecma2) | [DALTRECAB1](./microblog/runs.md#daltrecab1) | [DALTRECMB1](./microblog/runs.md#daltrecmb1)

??? abstract "Abstract"
	
	This paper describes our participation in the mobile notification and email digest tasks in the TREC 2015 Mircoblog track. The tasks are about monitoring Twitter stream and retrieving relevant tweets to users' interest profiles. Interest profiles contain the description of a topic that the user is interested in receiving relevant posts in real-time. Our proposed approach extracts Wikipedia concepts for profiles and tweets and applies a corpus-based word semantic relatedness method to assign tweets to their relevant profiles. This approach is also used to determine whether two tweets are semantically similar which in turn prevents the retrieval of redundant tweets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DangMMIKM15.bib) "
	```
	@inproceedings{DBLP:conf/trec/DangMMIKM15,
		author = {Anh Dang and Raheleh Makki and Abidalrahman Moh'd and Aminul Islam and Vlado Keselj and Evangelos E. Milios},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Real Time Filtering of Tweets Using Wikipedia Concepts and Google Tri-gram Semantic Relatedness},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/DalTREC-MB.pdf},
		timestamp = {Thu, 28 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DangMMIKM15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKUICST at TREC 2015 Microblog Track: Query-biased Adaptive Filtering  in Real-time Microblog Stream

_Feifan Fan, Yue Fei, Chao Lv, Lili Yao, Jianwu Yang, Dongyan Zhao_

- :fontawesome-solid-user-group: **Participant:** [PKUICST](./microblog/participants.md#pkuicst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/PKUICST-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/PKUICST-MB.pdf)
- :material-file-search: **Runs:** [PKUICSTRunA1](./microblog/runs.md#pkuicstruna1) | [PKUICSTRunA2](./microblog/runs.md#pkuicstruna2) | [PKUICSTRunA3](./microblog/runs.md#pkuicstruna3) | [PKUICSTRunB1](./microblog/runs.md#pkuicstrunb1) | [PKUICSTRunB2](./microblog/runs.md#pkuicstrunb2) | [PKUICSTRunB3](./microblog/runs.md#pkuicstrunb3)

??? abstract "Abstract"
	
	This paper describes our approaches to real-time filtering task including push notifications on a mobile phone scenario and periodic email digest scenario in the TREC 2015 Microblog track. In the push notifications on a mobile phone scenario, we apply an adaptive timely query-biased filtering framework which utilizes two effective scores to estimate the relevance of tweets. External evidences are well incorporated in our approach with Web-based query expansion technique. In the periodic email digest scenario, we apply pseudo-relevance feedback using language model and similarly we adopt an adaptive dynamic query-biased filtering method to choose the novel representative tweets. Besides, the results of scenario periodic email digest can promote the performance of scenario push notifications since we utilize shared global relevance threshold. Experimental results show that our adaptive query-biased filtering methods achieve good performance with respect to ELG and nCG metrics for push notifications scenario. In addition, our systems for scenario periodic email digest also obtain convincing nDCG scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FanFLYYZ15.bib) "
	```
	@inproceedings{DBLP:conf/trec/FanFLYYZ15,
		author = {Feifan Fan and Yue Fei and Chao Lv and Lili Yao and Jianwu Yang and Dongyan Zhao},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{PKUICST} at {TREC} 2015 Microblog Track: Query-biased Adaptive Filtering in Real-time Microblog Stream},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/PKUICST-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FanFLYYZ15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting Neural Embeddings for Social Media Data Analysis

_Sadid A. Hasan, Yuan Ling, Joey Liu, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna](./microblog/participants.md#prna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/prna-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/prna-MB.pdf)
- :material-file-search: **Runs:** [prnaTaskA1](./microblog/runs.md#prnataska1) | [prnaTaskA2](./microblog/runs.md#prnataska2) | [prnaTaskA3](./microblog/runs.md#prnataska3) | [prnaTaskB1](./microblog/runs.md#prnataskb1) | [prnaTaskB2](./microblog/runs.md#prnataskb2) | [prnaTaskB3](./microblog/runs.md#prnataskb3)

??? abstract "Abstract"
	
	In this paper, we describe our microblog real-time filtering system developed and submitted for the Text Retrieval Conference (TREC 2015) microblog track. We submitted six runs for two tasks related to real-time filtering by using various Information Retrieval (IR), and Machine Learning (ML) techniques to analyze the Twitter sample live stream and match relevant tweets corresponding to specific user interest profiles. Evaluation results demonstrate the effectiveness of our approach as we achieved 3 of the top 7 best scores among automatic submissions across all participants and obtained the best (or close to best) scores in more than 25% of the evaluated topics for the real-time mobile push notification task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HasanLLF15a.bib) "
	```
	@inproceedings{DBLP:conf/trec/HasanLLF15a,
		author = {Sadid A. Hasan and Yuan Ling and Joey Liu and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Exploiting Neural Embeddings for Social Media Data Analysis},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/prna-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HasanLLF15a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2015 Microblog Track: Real-Time Filtering Using Knowledge  Base

_Luyang Liu, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./microblog/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/BJUT-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/BJUT-MB.pdf)
- :material-file-search: **Runs:** [BJUTllyQE](./microblog/runs.md#bjutllyqe) | [BjutNMF1](./microblog/runs.md#bjutnmf1) | [BjutNMF2](./microblog/runs.md#bjutnmf2)

??? abstract "Abstract"
	
	This paper describes our efforts for TREC 2015 Microblog track. We applied the classic retrieval model combined with the external knowledge base, i.e., Wikipedia, for query expansion. Besides, we introduced the knowledge acquisition, query expansion, and retrieval model as well. Experimental results show the proposed approach is better than classical method in microblog real-time filtering with the usage of external knowledge base.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuY15.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuY15,
		author = {Luyang Liu and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2015 Microblog Track: Real-Time Filtering Using Knowledge Base},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/BJUT-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuY15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at TREC 2015 Microblog Track

_Luchen Tan, Adam Roegiest, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./microblog/participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/UWaterlooMDS-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/UWaterlooMDS-MB.pdf)
- :material-file-search: **Runs:** [UWaterlooATEK](./microblog/runs.md#uwaterlooatek) | [UWaterlooATNDEK](./microblog/runs.md#uwaterlooatndek) | [UWaterlooATDK](./microblog/runs.md#uwaterlooatdk) | [UWaterlooBT](./microblog/runs.md#uwaterloobt) | [UWaterlooBTND](./microblog/runs.md#uwaterloobtnd)

??? abstract "Abstract"
	
	Given a topic with title, narrative and description, we start by building a language model for the topic. The top 1000 tweets were retrieved from Twitter commercial search engine by applying the title of the topic as a query. We exploit pseudo relevance feedback technologies to estimate probability distributions of each term in the topic, then comparing these probabilities with a background distribution model. We select the highest different terms as our expanded query terms. We then generate a vector for each topic, the features of the vector are non-stop word title terms, selected narrative terms and query expansion terms. Different weights are assigned to the different types of terms. Since we are allowed to deliver at most 10 tweets every day, and the latency time can not exceed 100 minutes, we solve the tweet notification scenario as a multiple-choice secretary problem. Two different solutions were tested.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TanRC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/TanRC15,
		author = {Luchen Tan and Adam Roegiest and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Waterloo at {TREC} 2015 Microblog Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/UWaterlooMDS-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TanRC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NUDTSNA at TREC 2015 Microblog Track: A Live Retrieval System  Framework for Social Network based on Semantic Expansion and Quality  Model

_Xiang Zhu, Jiuming Huang, Sheng Zhu, Ming Chen, Chenlu Zhang, Zhenzhen Li, Huang Dongchuan, Zhao Chengliang, Aiping Li, Yan Jia_

- :fontawesome-solid-user-group: **Participant:** [NUDTSNA](./microblog/participants.md#nudtsna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/NUDTSNA-MB.pdf](http://trec.nist.gov/pubs/trec24/papers/NUDTSNA-MB.pdf)
- :material-file-search: **Runs:** [SNACS](./microblog/runs.md#snacs) | [SNACSA](./microblog/runs.md#snacsa) | [SNACS_LA](./microblog/runs.md#snacs_la) | [SNACS_LB](./microblog/runs.md#snacs_lb)

??? abstract "Abstract"
	
	This paper describe our approaches to real-time filtering task in the TREC 2015 Microblog track, including push notifications on a mobile phone task and periodic email digest task. In the push notifications on a mobile phone task, we apply a recommendation framework with rank algorithm and dynamic threshold adjustment which utilizes both semantic content and quality of a tweet. External information extracted from Google search engine and word2vec model based on existing corpus are well incorporated to enhance the understanding of a tweet's or a profile's interest. In the email digest task, based on the candidate tweets retrieved from the first task, we calculate the score of a tweet considering semantic features and quality features, all the tweets classified into a topic are ranked by our key word bool logistic model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuHZCZLDCLJ15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuHZCZLDCLJ15,
		author = {Xiang Zhu and Jiuming Huang and Sheng Zhu and Ming Chen and Chenlu Zhang and Zhenzhen Li and Huang Dongchuan and Zhao Chengliang and Aiping Li and Yan Jia},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{NUDTSNA} at {TREC} 2015 Microblog Track: {A} Live Retrieval System Framework for Social Network based on Semantic Expansion and Quality Model},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/NUDTSNA-MB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuHZCZLDCLJ15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLIP at TREC 2015: Microblog and LiveQA

_Mossaab Bagdouri, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [CLIP](./microblog/participants.md#clip)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/CLIP-MBQA.pdf](http://trec.nist.gov/pubs/trec24/papers/CLIP-MBQA.pdf)
- :material-file-search: **Runs:** [CLIP-A-DYN-0.5](./microblog/runs.md#clip-a-dyn-0.5) | [CLIP-A-5.0-0.5](./microblog/runs.md#clip-a-5.0-0.5) | [CLIP-A-5.0-0.6](./microblog/runs.md#clip-a-5.0-0.6) | [CLIP-B-0.5](./microblog/runs.md#clip-b-0.5) | [CLIP-B-0.6](./microblog/runs.md#clip-b-0.6) | [CLIP-B-0.4](./microblog/runs.md#clip-b-0.4)

??? abstract "Abstract"
	
	The Computational Linguistics and Information Processing lab at the University of Maryland participated in two TREC tracks this year. The Microblog Real-Time Filtering and the LiveQA tasks both involve information processing in real time. We submitted nine runs in total, achieving relatively good results. This paper describes the architecture and configuration of the systems behind those runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BagdouriO15.bib) "
	```
	@inproceedings{DBLP:conf/trec/BagdouriO15,
		author = {Mossaab Bagdouri and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CLIP} at {TREC} 2015: Microblog and LiveQA},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/CLIP-MBQA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BagdouriO15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2015 Microblog Track: Real-Time Filtering Using Non-negative  Matrix Factorization

_Chaoyang Li, Zhen Yang, Kefeng Fan_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./microblog/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/BJUT-MB2.pdf](http://trec.nist.gov/pubs/trec24/papers/BJUT-MB2.pdf)
- :material-file-search: **Runs:** [BJUTllyQE](./microblog/runs.md#bjutllyqe) | [BjutNMF1](./microblog/runs.md#bjutnmf1) | [BjutNMF2](./microblog/runs.md#bjutnmf2)

??? abstract "Abstract"
	
	In this paper, we described our approaches to the Real-Time Filtering Task in the TREC 2015 Microblog track. We submitted the results for scenario B: periodic email digest. In this ad hoc search task, we introduced a real-time filtering framework using non-negative matrix factorization. To build this framework, we firstly considered the Real-Time Filtering Task as a short text retrieval problem, and proposed a non-negative matrix factorization based Microblog retrieval model (NMF Framework). Then after a review of the potential influencing factors in Microblog retrieval, the main influencing factor, i.e., short query expansion, was modeled as the additional regularized constraint items in NMF Framework. Experimental results show the proposed approach is better than classical method in microblog real-time filtering with the above-mentioned additional regularized constraint items.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiYF15.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiYF15,
		author = {Chaoyang Li and Zhen Yang and Kefeng Fan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2015 Microblog Track: Real-Time Filtering Using Non-negative Matrix Factorization},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/BJUT-MB2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiYF15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QU at TREC-2015: Building Real-Time Systems for Tweet Filtering  and Question Answering

_Reem Suwaileh, Maram Hasanain, Marwan Torki, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./microblog/participants.md#qu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/QU-MBQA.pdf](http://trec.nist.gov/pubs/trec24/papers/QU-MBQA.pdf)
- :material-file-search: **Runs:** [QUBaseline](./microblog/runs.md#qubaseline) | [QUDyn](./microblog/runs.md#qudyn) | [QUDynExp](./microblog/runs.md#qudynexp) | [QUBaselineB](./microblog/runs.md#qubaselineb) | [QUExpB](./microblog/runs.md#quexpb) | [QUFullExpB](./microblog/runs.md#qufullexpb)

??? abstract "Abstract"
	
	This paper presents our participation in the microblog and LiveQA tracks in TREC-2015. Both tracks required building a “real-time” system that monitors a data stream and responds to users' information needs in real-time. For the microblog track, given a set of users' interest profiles, we developed two online filtering systems that recommend “relevant” and “novel” tweets from a tweet stream for each profile. Both systems simulate real scenarios: filtered tweets are sent as push notifications on a mobile phone or as a periodic email digest. We study the e↵ect of using a static versus dynamic relevance thresholds to control the relevancy of filtered output to interest profiles. We also experiment with di↵erent profile expansion strategies that account for potential topic drift. Our results show that the baseline run of the push notifications scenario that uses a static threshold with light profile expansion achieved the best results. Similarly, in the email digest scenario, the baseline run that used a shorter representation of the interest profiles without any expansion was the best run. For the LiveQA track, the system was required to answer a stream of around 1000 real-time questions from Yahoo! Answers. We adopted a very simple approach that searched an archived Yahoo! Answers QA dataset for similar questions to the asked ones and retrieved back their answers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SuwailehHTE15.bib) "
	```
	@inproceedings{DBLP:conf/trec/SuwailehHTE15,
		author = {Reem Suwaileh and Maram Hasanain and Marwan Torki and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{QU} at {TREC-2015:} Building Real-Time Systems for Tweet Filtering and Question Answering},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/QU-MBQA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SuwailehHTE15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Contextual Suggestion 

#### Overview of the TREC 2015 Contextual Suggestion Track

_Adriel Dean-Hall, Charles L. A. Clarke, Jaap Kamps, Julia Kiseleva, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Overview-CX.pdf](http://trec.nist.gov/pubs/trec24/papers/Overview-CX.pdf)
??? abstract "Abstract"
	
	The TREC Contextual Suggestion Track evaluates point-of-interest (POI) recommendation systems, with the goal of creating open and reusable test collections for this purpose. The track imagines a traveler in a unknown city seeking sites to see and things to do that reflect his or her own personal interests, as inferred from their interests in their home city. Given a user's profile, consisting of a POI list and rating from a home city, participants make recommendations for attractions in a target city (i.e., a new context). For example, imagine a group of information retrieval researchers with a November evening to spend in beautiful Gaithersburg, Maryland. A contextual suggestion system might recommend a beer at the Dogfish Head Alehouse, dinner at the Flaming Pit, or even a trip into Washington on the metro to see the National Mall. This is the fourth year that the track has operated (since TREC 2012). If you are familiar with the track from previous years, here are the big changes this year: The track moved from the open web to a fixed set of documents. The track was split into two tasks: 1. A live task, in which participants set up a server and were sent requests over a period of about three weeks. 2. A batch task, which was similar to the task run in previous years. The live task reflects the track's long term goal of creating a “living lab” service for POI recommendation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Dean-HallCKKV15.bib) "
	```
	@inproceedings{DBLP:conf/trec/Dean-HallCKKV15,
		author = {Adriel Dean{-}Hall and Charles L. A. Clarke and Jaap Kamps and Julia Kiseleva and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2015 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Overview-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Dean-HallCKKV15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Contextual Suggestion using tag-description similarity

_Manajit Chakraborty, Hitesh Agrawal, Himanshu Shekhar, C. Ravindranath Chowdary_

- :fontawesome-solid-user-group: **Participant:** [DPLAB_IITBHU](./context/participants.md#dplab_iitbhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/DPLAB_IITBHU-CX.pdf](http://trec.nist.gov/pubs/trec24/papers/DPLAB_IITBHU-CX.pdf)
- :material-file-search: **Runs:** [IITBHU_1](./context/runs.md#iitbhu_1) | [IITBHU_2](./context/runs.md#iitbhu_2)

??? abstract "Abstract"
	
	In this paper, we present our approach for the Contextual Suggestion track of 2015 Text REtrieval Conference (TREC). The task aims at providing recommendations on points of attraction for different kind of users and a varying context. Our group DPLAB IITBHU tries to address the problem from the perspective of how relevant the attractions are based on user profiles and rank them based on two similarity measures- wup similarity and another similarity measure proposed by us.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChakrabortyASC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChakrabortyASC15,
		author = {Manajit Chakraborty and Hitesh Agrawal and Himanshu Shekhar and C. Ravindranath Chowdary},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Contextual Suggestion using tag-description similarity},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/DPLAB\_IITBHU-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChakrabortyASC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2015 Contextual Suggestion Track

_Weitong Chen, Hanchen Li, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./context/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/BJUT-CX.pdf](http://trec.nist.gov/pubs/trec24/papers/BJUT-CX.pdf)
- :material-file-search: **Runs:** [BJUTb](./context/runs.md#bjutb) | [BJUTA](./context/runs.md#bjuta)

??? abstract "Abstract"
	
	In this paper we described our efforts for TREC contextual suggestion task. Our goal of this year is to evaluate the effectiveness of: (1) predict user preferences of each scenic spot based on non-negtive matrix factorization, (2) automatic summarization method that leverages the information from multiple resources to generate the description for each candidate scenic spots; and (3) hybrid recommendation method that combing a variety of factors to construct a system of hybrid recommendation system. Finally, we conduct extensive experiments to evaluate the proposed framework on TREC 2015 Contextual Suggestion data set, and, as would be expected, the results demonstrate its generality and superior performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenLY15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenLY15,
		author = {Weitong Chen and Hanchen Li and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2015 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/BJUT-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenLY15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Parsimonious User and Group Profiling in Venue Recommendation

_Seyyed Hadi Hashemi, Mostafa Dehghani, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./context/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/UAmsterdam-CX.pdf](http://trec.nist.gov/pubs/trec24/papers/UAmsterdam-CX.pdf)
- :material-file-search: **Runs:** [PLM1](./context/runs.md#plm1) | [PLM2](./context/runs.md#plm2)

??? abstract "Abstract"
	
	This paper presents the University of Amsterdam's participation in the TREC 2015 Contextual Suggestion Track. Creating e↵ective profiles for both users and contexts is the main key to build an e↵ective contextual suggestion system. To address these issues, we investigate building users' and groups' profiles for e↵ective contextual personalization and customization. Our main aim is to answer the questions: How to build a user-specific profile that penalizes terms having high probability in negative language models? Can parsimonious language models improve user and context profile's e↵ectiveness? How to combine both models and benefit from both a contextual customization using contextual group profiles and a contextual personalization using users profiles? Our main findings are the following: First, although using parsimonious language model leads to a more compact language model as users' profiles, the personalization performance is as good as using standard language models for building users' profiles. Second, we extensively analyze e↵ectiveness of three di↵erent approaches in taking the negative profiles into account, which improves performance of contextual suggestion models that just uses positive profiles. Third, we learn an e↵ective model for contextual customization and analyze the importance of different contexts in contextual suggestion task. Finally, we propose a linear combination of contextual customization and personalization, which improves the performance of contextual suggestion using either contextual customization or personalization based on all the common used IR metrics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HashemiDK15.bib) "
	```
	@inproceedings{DBLP:conf/trec/HashemiDK15,
		author = {Seyyed Hadi Hashemi and Mostafa Dehghani and Jaap Kamps},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Parsimonious User and Group Profiling in Venue Recommendation},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/UAmsterdam-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HashemiDK15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke: TREC 2015 Contextual Suggestion Track

_Hella Hoffmann, Pragnya Addala, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./context/participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-CX.pdf](http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-CX.pdf)
- :material-file-search: **Runs:** [WaterlooRunB](./context/runs.md#waterloorunb) | [WaterlooRunA](./context/runs.md#waterlooruna)

??? abstract "Abstract"
	
	In this work we present a first attempt at developing a live system to solve the problem presented in the TREC 2015 contextual suggestion task1. The goal of this task is to tailor point-of-interest suggestions to users according to their preferences [3]. We present how we gathered data for the candidate points-of-interest, filtered some of the candidates and built a live system to return suggestions that would most likely interest the specific user. As part of TREC 2015, the contextual suggestion track is running for the fourth time [3, 4, 2] and this is the first time that the participants were required to build a live suggestion system. The general idea is to be able to make real-time suggestions for a particular person (based upon their profile) with a particular context. Unlike the previous years where the participants were asked to build their own candidate list of suggestions, this year the organizers themselves released a fixed set of candidate suggestions for 272 contexts, each context representing a city in the United States. Participants were required to set up a server that could listen to requests from users and respond with relevant suggestions. For each request, which is a profile-context pairing, a ranked list of up to 50 ranked suggestions was to be returned. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HoffmannAC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/HoffmannAC15,
		author = {Hella Hoffmann and Pragnya Addala and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {WaterlooClarke: {TREC} 2015 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HoffmannAC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Laval University and Lakehead University Experiments at TREC 2015  Contextual Suggestion Track

_Jian Mo, Luc Lamontagne, Richard Khoury_

- :fontawesome-solid-user-group: **Participant:** [LavallVA](./context/participants.md#lavallva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/LavallVA-CX.pdf](http://trec.nist.gov/pubs/trec24/papers/LavallVA-CX.pdf)

??? abstract "Abstract"
	
	In this paper we describe our effort on TREC Contextual Suggestion Track. We present a recommendation system that built upon ElasticSearch along with a machine learning re-ranking model. We utilize real world users' opinion as well as other information to build user profiles. With profile information, we then construct customized ElasticSearch queries to search on various fields. After that, a learning to rank regressor is implemented to give better ranking results. Track results of our submitted runs show the effectiveness of the system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoLK15.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoLK15,
		author = {Jian Mo and Luc Lamontagne and Richard Khoury},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Laval University and Lakehead University Experiments at {TREC} 2015 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/LavallVA-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoLK15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Siena College's Institute of Artificial Intelligence TREC 2015 Contextual  Suggestion Track

_Aidan Trees, Kevin Danaher, Zach Siatkowski, Darren Lim, Tom Heritage_

- :fontawesome-solid-user-group: **Participant:** [Siena_SUCCESS](./context/participants.md#siena_success)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Siena_SUCCESS-CX.pdf](http://trec.nist.gov/pubs/trec24/papers/Siena_SUCCESS-CX.pdf)
- :material-file-search: **Runs:** [SCIAI_runA](./context/runs.md#sciai_runa) | [SCIAI_runB](./context/runs.md#sciai_runb)

??? abstract "Abstract"
	
	An overview of Siena College's participation in the Contextual Suggestion track of the Twenty-Fourth Text Retrieval Conference (TREC) is provided in this report. Our goal was to first design a search technique for complex information on specified POI's (points of interest) from a collection set given by TREC. The second part of our task was to return a list of ranked suggestions dependent on a given context and a user's interests. Multiple API's were utilized for information retrieval on each particular POI including Google Places, Foursquare, and Yellow Pages. This process was repeated for not only the POI's being suggested to the user, but for the POI's rated by each user as well. From this information, profile preferences were created for individual users by examining the categories of the POI's that they had rated. To build these preferences, we designed a scoring algorithm to associate a value with each individual category returned by the API's. We finally created a ranking system that includes a unique penalty function to sort our suggestions of attractions specific to each of the users' interests.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TreesDSLH15.bib) "
	```
	@inproceedings{DBLP:conf/trec/TreesDSLH15,
		author = {Aidan Trees and Kevin Danaher and Zach Siatkowski and Darren Lim and Tom Heritage},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Siena College's Institute of Artificial Intelligence {TREC} 2015 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Siena\_SUCCESS-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TreesDSLH15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploration of Semantic-aware Approach for Contextual Suggestion Using  Knowledge from The Open Web

_Yuan Wang, Jie Liu, Yalou Huang, Yongfeng Zhang, Yi Zhang, Xintong Zhang_

- :fontawesome-solid-user-group: **Participant:** [ucsc](./context/participants.md#ucsc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/ucsc-CX.pdf](http://trec.nist.gov/pubs/trec24/papers/ucsc-CX.pdf)
- :material-file-search: **Runs:** [RUN1](./context/runs.md#run1) | [RUN2](./context/runs.md#run2) | [IRKM2](./context/runs.md#irkm2) | [IRKM1](./context/runs.md#irkm1)

??? abstract "Abstract"
	
	This paper describes our group's first attempt on the Contextual Suggestion Track of the Twenty-fourth Text REtrieval Conference (TREC 2015). The task aims to provide recommendations on attractions for various kinds of users under different and complex contexts. TREC provides two ways to participate in the track: one is to create a web server that can respond to contextual related queries called “Live Experiment”, the other is to submit run files that have all the responses to the released requests called “Batch Experiment”. For Live Experiment, due to lack of training data, our approach sticks closely to the defined relevance judgement criteria and context knowledge. We take linear interpolation to combine a variety of factors and contextual related knowledge. For Batch Experiment, we further consider domain preference under user attributes, and take existing Machine Learning based methods in principle. We show that feature engineering is a vital part for attraction suggestions. We find that the performance of suggestions to the provided user profiles and contexts has been improved using domain preference analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangLHZZZ15.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangLHZZZ15,
		author = {Yuan Wang and Jie Liu and Yalou Huang and Yongfeng Zhang and Yi Zhang and Xintong Zhang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Exploration of Semantic-aware Approach for Contextual Suggestion Using Knowledge from The Open Web},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/ucsc-CX.pdf},
		timestamp = {Mon, 22 Nov 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangLHZZZ15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Delaware at TREC 2015: Combining Opinion Profile Modeling  with Complex Context Filtering for Contextual Suggestion

_Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./context/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/udel_fang-CX.pdf](http://trec.nist.gov/pubs/trec24/papers/udel_fang-CX.pdf)
- :material-file-search: **Runs:** [fr](./context/runs.md#fr) | [nr](./context/runs.md#nr) | [UDInfoCS2015](./context/runs.md#udinfocs2015)

??? abstract "Abstract"
	
	In this paper we describe our effort on TREC 2015 Contextual Suggestion Track. Using opinions from online resources to model both user profile and candidate profile has been proven to be effective on previous TREC. This year we also leverage the power of building profile based on opinions. Opinions from well known commercial online resources are collected in order to build the profiles. Two kinds of opinion representations are used for the two submitted runs. Linear interpolation is leveraged to rank the candidate suggestions. Additionally, an advanced context filter which considers all possible factors such as trip type and trip duration is applied to the ranking results so that unwanted venues are removed from the final ranking list. Official results of our submitted runs show the effectiveness of the proposed method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yang015.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yang015,
		author = {Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Delaware at {TREC} 2015: Combining Opinion Profile Modeling with Complex Context Filtering for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/udel\_fang-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Yang015.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lugano at TREC 2015: Contextual Suggestion and Temporal  Summarization Tracks

_Mohammad Aliannejadi, Seyed Ali Bahrainian, Anastasia Giachanou, Fabio Crestani_

- :fontawesome-solid-user-group: **Participant:** [USI](./context/participants.md#usi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/USI-CXTS.pdf](http://trec.nist.gov/pubs/trec24/papers/USI-CXTS.pdf)
- :material-file-search: **Runs:** [11](./context/runs.md#11) | [22](./context/runs.md#22)

??? abstract "Abstract"
	
	This technical report presents the work of the University of Lugano at TREC 2015 Contextual Suggestion and Temporal Summarization tracks. The first track that we report on, is the Contextual Suggestion. The goal of the Contextual Suggestion track is to develop systems that could generate user-specific suggestions that a user might potentially like. Our proposed method attempts to model the users' behavior and interest using a classifier, and enrich the basic model using additional data sources. Our results illustrate that our proposed method performed very well in terms of all used evaluation metrics. The second track that we report on, is the Temporal Summarization that aims to develop systems that can detect useful, new, and timely updates about a certain event. Our proposed method selects sentences that are relevant and novel to a specific event with the aim to create a summary for this event. The results showed that the proposed method is very e↵ective in terms of Latency Comprehensiveness (LC). However, the approach did not manage to obtain a good performance in terms of Expected Latency Gain (ELG).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AliannejadiBGC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/AliannejadiBGC15,
		author = {Mohammad Aliannejadi and Seyed Ali Bahrainian and Anastasia Giachanou and Fabio Crestani},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Lugano at {TREC} 2015: Contextual Suggestion and Temporal Summarization Tracks},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/USI-CXTS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AliannejadiBGC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2015: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Dynamic Domain Tracks

_Richard McCreadie, Saul Vargas, Craig MacDonald, Iadh Ounis, Stuart Mackie, Jarana Manotumruksa, Graham McDonald_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./context/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf](http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf)
- :material-file-search: **Runs:** [uogTrCSFM](./context/runs.md#uogtrcsfm) | [uogTrCSLVPC](./context/runs.md#uogtrcslvpc) | [uogTrCsLtrUDepCat](./context/runs.md#uogtrcsltrudepcat) | [uogTrCsLtrUInd](./context/runs.md#uogtrcsltruind)

??? abstract "Abstract"
	
	n TREC 2015, we focus on tackling the challenges posed by the Contextual Suggestion, Temporal Summarisation and Dynamic Domain tracks. For Contextual Suggestion, we investigate the use of user-generated data in location-based social networks (LBSN) to suggest venues. For Temporal Summarisation, we examine features for event summarisation that explicitly model the entities involved in the events. Meanwhile, for the Dynamic Domain track, we explore resource selection techniques for identifying the domain of interest and diversifying sub-topic intents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieVMOMMM15.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieVMOMMM15,
		author = {Richard McCreadie and Saul Vargas and Craig MacDonald and Iadh Ounis and Stuart Mackie and Jarana Manotumruksa and Graham McDonald},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow at {TREC} 2015: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Dynamic Domain Tracks},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieVMOMMM15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Temporal Summarization 

#### TREC 2015 Temporal Summarization Track Overview

_Javed A. Aslam, Fernando Diaz, Matthew Ekstrand-Abueg, Richard McCreadie, Virgil Pavlu, Tetsuya Sakai_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Overview-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/Overview-TS.pdf)
??? abstract "Abstract"
	
	There are many summarization scenarios that require updates to be issued to users over time. For example, during unexpected news events such as natural disasters or mass protests new information rapidly emerges. The TREC Temporal Summarization track aims to investigate how to e↵ectively summarize these types of event in real-time. In particular, the goal is to develop systems which can detect useful, new, and timely sentence-length updates about a developing event to return to the user. In contrast to classical summarization challenges (such as DUC or TAC), the summaries produced by the participant systems are evaluated against a ground truth list of information nuggets representing the space of information that a user might want to know about each event. An optimal summary will cover all of the information nuggets in the minimum number of sentences. Also in contrast to classic summarization and newer timeline generation tasks, the Temporal Summarization track focuses on performing this analysis online as documents are indexed. For the third 2015 edition of the Temporal Summarization track, we had four main aims. First, to better address the issues with run incompleteness by producing larger run pools and by using pool expansion based on sentence similarity. Second, to lower the barrier to entry for new groups by providing multiple sub-tasks using corpora of varying sizes, allowing groups to pick the task(s) that their infrastructure can cope with. Third, to refine the metrics to better incorporate latency by considering timeliness against the corpus as well as against updates to the Wikipedia page. Finally, to continue to increase the number of events covered by the evaluation. This is the final year of the Temporal Summarization track. For 2016, the track will merge with the Microblog track to become the new Real-Time Summarization (RTS) Track. This new RTS track will still tackle the same challenges as the Temporal Summarization track, but will incorporate microblog streams and will include a new Living-Lab style evaluation in addition to the classical dataset-based evaluation. The remainder of this overview is structured as follows. Section 2 describes the temporal summarization task in detail. In Section 3, we discuss the corpus of documents from which the summaries are produced, while in Section 4, we discuss how temporal summarization systems are evaluated within the track. Section 5 details the process via which sentence updates were assessed. Finally, in Section 6, we summarize the performance of the participant systems to the 2014 track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AslamDEMPS15.bib) "
	```
	@inproceedings{DBLP:conf/trec/AslamDEMPS15,
		author = {Javed A. Aslam and Fernando Diaz and Matthew Ekstrand{-}Abueg and Richard McCreadie and Virgil Pavlu and Tetsuya Sakai},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2015 Temporal Summarization Track Overview},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Overview-TS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AslamDEMPS15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Temporal Summarization 2015

_Rafik Abbes, Bilel Moulahi, Abdelhamid Chellal, Karen Pinel-Sauvagnat, Nathalie Hernandez, Mohand Boughanem, Lynda Tamine, Sadok Ben Yahia_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./tempsumm/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/IRIT-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/IRIT-TS.pdf)
- :material-file-search: **Runs:** [FS1A](./tempsumm/runs.md#fs1a) | [OS1C](./tempsumm/runs.md#os1c) | [FS2A](./tempsumm/runs.md#fs2a) | [FS3A](./tempsumm/runs.md#fs3a) | [FS4A](./tempsumm/runs.md#fs4a) | [OS2C](./tempsumm/runs.md#os2c) | [FS5A](./tempsumm/runs.md#fs5a) | [OS3C](./tempsumm/runs.md#os3c) | [FS6A](./tempsumm/runs.md#fs6a) | [OS4C](./tempsumm/runs.md#os4c) | [OS1A](./tempsumm/runs.md#os1a) | [OS2A](./tempsumm/runs.md#os2a) | [OS3A](./tempsumm/runs.md#os3a) | [OS5C](./tempsumm/runs.md#os5c) | [OS6C](./tempsumm/runs.md#os6c) | [OS7C](./tempsumm/runs.md#os7c) | [OS8C](./tempsumm/runs.md#os8c) | [FS1B](./tempsumm/runs.md#fs1b) | [FS2B](./tempsumm/runs.md#fs2b) | [FS3B](./tempsumm/runs.md#fs3b) | [FS4B](./tempsumm/runs.md#fs4b)

??? abstract "Abstract"
	
	This paper describes the IRIT lab participation to the TREC 2015 Temporal Summarization track. The goal of the Temporal Summarization track is to develop systems that allow users to efficiently monitor information about events over time. To tackle this task, we proposed three different methods. Obtained results are presented and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbbesMCPHBTMY15.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbbesMCPHBTMY15,
		author = {Rafik Abbes and Bilel Moulahi and Abdelhamid Chellal and Karen Pinel{-}Sauvagnat and Nathalie Hernandez and Mohand Boughanem and Lynda Tamine and Sadok Ben Yahia},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IRIT} at {TREC} Temporal Summarization 2015},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/IRIT-TS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AbbesMCPHBTMY15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Event Oriented Query Expansion for News Event Queries

_Kuang Lu, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./tempsumm/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/udel_fang-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/udel_fang-TS.pdf)
- :material-file-search: **Runs:** [WikiProfMix1](./tempsumm/runs.md#wikiprofmix1) | [WikiProfMixFS1](./tempsumm/runs.md#wikiprofmixfs1) | [WikiOnlyFS2](./tempsumm/runs.md#wikionlyfs2) | [WikiOnly2](./tempsumm/runs.md#wikionly2) | [ProfOnlyFS3](./tempsumm/runs.md#profonlyfs3) | [ProfOnly3](./tempsumm/runs.md#profonly3)

??? abstract "Abstract"
	
	Query expansion techniques have been commonly used by participants in Temporal Summarization tack. However, many previous attempts focused on expanding queries based on their event types, which only covers partially of the information need represented by queries. The reason is that the queries in the TS track are about news events, and for an event query, the event related entities, which are the entities mentioned in the queries, are essential when defining the event. Given the query ”Vauxhall helicopter crash”, without ”Vauxhall” or ”helicopter”, the event cannot be specifically defined. Therefore, we argue that both event type and event related entities should be considered when expanding a query, and a model based query expansion framework is proposed which incorporates these two types of information. The framework is then employed by using external resources, such as external corpora and Wikipedia pages to build expansion models.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuF15.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuF15,
		author = {Kuang Lu and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Event Oriented Query Expansion for News Event Queries},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/udel\_fang-TS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuF15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke: TREC 2015 Temporal Summarization Track

_Ahsan Raza, Devin M. Rotondo, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./tempsumm/participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-TS.pdf)
- :material-file-search: **Runs:** [UWCTSRun1](./tempsumm/runs.md#uwctsrun1) | [UWCTSRun2](./tempsumm/runs.md#uwctsrun2) | [UWCTSRun3](./tempsumm/runs.md#uwctsrun3) | [UWCTSRun4](./tempsumm/runs.md#uwctsrun4) | [UWCTSRun5](./tempsumm/runs.md#uwctsrun5) | [UWCTSRun6](./tempsumm/runs.md#uwctsrun6)

??? abstract "Abstract"
	
	The Temporal Summarization Track looks at providing meaningful summaries of major events and sub-events as they occur. Difficulties arise due to the unique nature of the temporal summarization task in which the corpora is constantly changing along with the known information about the event [1]. This year, the temporal summarization track consists of three tasks, two filtering and summarization tasks and an ontopic summarization task. In the filtering and summarization tasks, relevant content must be extracted from a continuous stream of documents and gradually summarized while maintaining low redundancy, latency and verbosity. In the third task, only the summarization must take place on a corpora filled with many documents related to the event [2]. The overall goal of the track is to provide a sequence of short meaningful sentence length updates over the duration of the events taking into account sentence redundancy and latency. The summaries are scored using an expected latency gain metric (ELG) in which sentences are rewarded for containing handpicked key updates (nuggets) and are penalized for redundancy, latency and verbosity [3]. This track can help users deal with all of the vast information that comes as major events progress through the use of general impersonal updates. Our approach for this track consists of a two step process. The first stage is a data preprocessing stage which extracts the information from the supplied web documents and only retains the information considered necessary for the second stage. The second stage is the filtering and summarization stage used to find and push the relevant sentence length updates. We have applied this methodology to both the second and third task. A total of six different runs have been submitted with all of them being judged. The run scores are comparable to those in 2014, however, with a larger latency gain and lower latency comprehensiveness. The submitted task 2 runs appear to have a slightly better performance than those of task 3. However, there were no apparent differences between the task 2 or the task 3 runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RazaRC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/RazaRC15,
		author = {Ahsan Raza and Devin M. Rotondo and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {WaterlooClarke: {TREC} 2015 Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-TS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RazaRC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI and TU Delft at the TREC 2015 Temporal Summarization Track

_Jeroen B. P. Vuurens, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [CWI](./tempsumm/participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/CWI-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/CWI-TS.pdf)
- :material-file-search: **Runs:** [IGn](./tempsumm/runs.md#ign) | [IGnPrecision](./tempsumm/runs.md#ignprecision) | [docs](./tempsumm/runs.md#docs) | [titles](./tempsumm/runs.md#titles) | [IGnRecall](./tempsumm/runs.md#ignrecall) | [docsRecall](./tempsumm/runs.md#docsrecall)

??? abstract "Abstract"
	
	Internet users are turning more frequently to online news as a replacement for traditional media sources such as newspapers or television shows. Still, discovering news events online and following them as they develop can be a difficult task. In previous work, we presented a novel approach to extract sentences from an online stream of news articles that summarizes the most important news facts for a given ad-hoc information need, which compared to existing systems obtained relatively high-precision results and a comparable recall [9]. In this track, we experiment with this approach to improve the recall of retrieved results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VuurensV15.bib) "
	```
	@inproceedings{DBLP:conf/trec/VuurensV15,
		author = {Jeroen B. P. Vuurens and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CWI} and {TU} Delft at the {TREC} 2015 Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/CWI-TS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VuurensV15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ISCASIR at TREC 2015 Temporal Summarization Track

_Peixia Wang, Wenbo Li_

- :fontawesome-solid-user-group: **Participant:** [ISCASIR](./tempsumm/participants.md#iscasir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/ISCASIR-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/ISCASIR-TS.pdf)
- :material-file-search: **Runs:** [runvec1](./tempsumm/runs.md#runvec1) | [runvec2](./tempsumm/runs.md#runvec2)

??? abstract "Abstract"
	
	The goal of Temporal Summarization task is to develop systems which can detect useful, new, and timely sentence-length updates about a developing event. This paper describes our participation in Temporal Summarization track of TREC2015. Based on the word embedding technique, we submitted two runs for the summarization task. The query expanding technique is used for the first run and relevant sentences are retrieved by computing the distance between the expanded query and the sentence. The processing of second run is the same with the first run except for the query expanding stage. Using the KBA Stream Corpus 2014, the experimental results show the effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangL15.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangL15,
		author = {Peixia Wang and Wenbo Li},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ISCASIR} at {TREC} 2015 Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/ISCASIR-TS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangL15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2015 Temporal Summarization Track

_Yingzhe Yao, Zhen Yang, Kefeng Fan_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./tempsumm/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/BJUT-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/BJUT-TS.pdf)
- :material-file-search: **Runs:** [DMSL1NMF2](./tempsumm/runs.md#dmsl1nmf2) | [DMSL1AP1](./tempsumm/runs.md#dmsl1ap1) | [DMSL1VSH3](./tempsumm/runs.md#dmsl1vsh3) | [DMSL2N2](./tempsumm/runs.md#dmsl2n2) | [DMSL2A1](./tempsumm/runs.md#dmsl2a1) | [DMSL2V3](./tempsumm/runs.md#dmsl2v3)

??? abstract "Abstract"
	
	In this paper, we describe our efforts for TREC Temporal Summarization Track 2015. Since this is the third time we participate in this track,we adopt a different novel method NMFR to solve the newly emerging temporal summarization problem. Our goal of this year is to evaluate the effectiveness of: (1) Considering the semantic structure of document and the manifold structure of document could be as possible to preserve the essential characteristic of the original high-dimensional space of documents during the process of feature reduction.(2)Using the non-negative matrix factorization with our semantic and manifold regularization for summarization is effective and comparable to Affinity Propagation. Finally, we conduct experiments to verify the proposed framework NMFR on TREC Temporal Summarization Track Corpus, and, as would be expected, the results demonstrate its generality and superior performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YaoYF15.bib) "
	```
	@inproceedings{DBLP:conf/trec/YaoYF15,
		author = {Yingzhe Yao and Zhen Yang and Kefeng Fan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2015 Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/BJUT-TS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YaoYF15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SeqCluSum: Combining Sequential Clustering and Contextual Importance  Measuring to Summarize Developing Events over Time

_Markus Zopf_

- :fontawesome-solid-user-group: **Participant:** [AIPHES](./tempsumm/participants.md#aiphes)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/AIPHES-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/AIPHES-TS.pdf)
- :material-file-search: **Runs:** [Run1](./tempsumm/runs.md#run1) | [Run2](./tempsumm/runs.md#run2) | [Run4](./tempsumm/runs.md#run4) | [Run3](./tempsumm/runs.md#run3)

??? abstract "Abstract"
	
	Unexpected events such as accidents, natural disasters and terrorist attacks represent an information situation where it is essential to give users access to important and non-redundant information as fast as possible. In this paper, we introduce SeqCluSum, a temporal summarization system which combines sequential clustering to cluster sentences and a contextual importance measurement to weight the created clusters and thereby to identify important sentences. We participated with this system in the TREC Temporal Summarization track where systems have to generate extractive summaries for developing events by publishing sentence-length updates extracted from web documents. Results show that our approach is very well suited for this task by achieving best results. We furthermore point out several improvement possibilities to show how the system can further be enhanced.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Zopf15.bib) "
	```
	@inproceedings{DBLP:conf/trec/Zopf15,
		author = {Markus Zopf},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {SeqCluSum: Combining Sequential Clustering and Contextual Importance Measuring to Summarize Developing Events over Time},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/AIPHES-TS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Zopf15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lugano at TREC 2015: Contextual Suggestion and Temporal  Summarization Tracks

_Mohammad Aliannejadi, Seyed Ali Bahrainian, Anastasia Giachanou, Fabio Crestani_

- :fontawesome-solid-user-group: **Participant:** [USI](./tempsumm/participants.md#usi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/USI-CXTS.pdf](http://trec.nist.gov/pubs/trec24/papers/USI-CXTS.pdf)
- :material-file-search: **Runs:** [InL2DecrQE1ID1](./tempsumm/runs.md#inl2decrqe1id1) | [InL2DecrQE2ID2](./tempsumm/runs.md#inl2decrqe2id2) | [InL2StabQE2ID3](./tempsumm/runs.md#inl2stabqe2id3) | [InL2IncrQE2ID4](./tempsumm/runs.md#inl2incrqe2id4) | [InL2DocsQE2ID5](./tempsumm/runs.md#inl2docsqe2id5) | [InL2StabQE1ID6](./tempsumm/runs.md#inl2stabqe1id6) | [InL2IncrQE1ID7](./tempsumm/runs.md#inl2incrqe1id7)

??? abstract "Abstract"
	
	This technical report presents the work of the University of Lugano at TREC 2015 Contextual Suggestion and Temporal Summarization tracks. The first track that we report on, is the Contextual Suggestion. The goal of the Contextual Suggestion track is to develop systems that could generate user-specific suggestions that a user might potentially like. Our proposed method attempts to model the users' behavior and interest using a classifier, and enrich the basic model using additional data sources. Our results illustrate that our proposed method performed very well in terms of all used evaluation metrics. The second track that we report on, is the Temporal Summarization that aims to develop systems that can detect useful, new, and timely updates about a certain event. Our proposed method selects sentences that are relevant and novel to a specific event with the aim to create a summary for this event. The results showed that the proposed method is very e↵ective in terms of Latency Comprehensiveness (LC). However, the approach did not manage to obtain a good performance in terms of Expected Latency Gain (ELG).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AliannejadiBGC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/AliannejadiBGC15,
		author = {Mohammad Aliannejadi and Seyed Ali Bahrainian and Anastasia Giachanou and Fabio Crestani},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Lugano at {TREC} 2015: Contextual Suggestion and Temporal Summarization Tracks},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/USI-CXTS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AliannejadiBGC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam (ILPS.UvA) at TREC 2015 Temporal Summarization  Track

_Cristina Garbacea, Evangelos Kanoulas_

- :fontawesome-solid-user-group: **Participant:** [UvA.ILPS](./tempsumm/participants.md#uva.ilps)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/UvA.ILPS-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/UvA.ILPS-TS.pdf)
- :material-file-search: **Runs:** [TF](./tempsumm/runs.md#tf) | [TFISF](./tempsumm/runs.md#tfisf) | [QL](./tempsumm/runs.md#ql) | [LLR](./tempsumm/runs.md#llr) | [LDA](./tempsumm/runs.md#lda) | [LexRank](./tempsumm/runs.md#lexrank) | [LM](./tempsumm/runs.md#lm) | [TFW2V](./tempsumm/runs.md#tfw2v) | [TFISFW2V](./tempsumm/runs.md#tfisfw2v) | [LDAv2](./tempsumm/runs.md#ldav2) | [QLLP](./tempsumm/runs.md#qllp) | [TFW](./tempsumm/runs.md#tfw) | [TFISFW](./tempsumm/runs.md#tfisfw) | [QLF](./tempsumm/runs.md#qlf) | [COSSIM](./tempsumm/runs.md#cossim) | [COS](./tempsumm/runs.md#cos) | [TFFilter](./tempsumm/runs.md#tffilter)

??? abstract "Abstract"
	
	In this paper we report on our participation in the TREC 2015 Temporal Summarization track, aimed at encouraging the development of systems able to detect, emit, track, and summarize sentence length updates about a developing event. We address the task by probing the utility of a variety of information retrieval based methods in capturing useful, timely and novel updates during unexpected news events such as natural disasters or mass protests, when high volumes of information rapidly emerge. We investigate the extent to which these updates are retrievable, and explore ways to increase the coverage of the summary by taking into account the structure of documents. We find that our runs achieve high scores in terms of comprehensiveness, successfully capturing the relevant pieces of information that characterize an event. In terms of latency, our runs perform better than average. We present the specifics of our framework and discuss the results we obtained.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarbaceaK15.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarbaceaK15,
		author = {Cristina Garbacea and Evangelos Kanoulas},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Amsterdam (ILPS.UvA) at {TREC} 2015 Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/UvA.ILPS-TS.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GarbaceaK15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2015: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Dynamic Domain Tracks

_Richard McCreadie, Saul Vargas, Craig MacDonald, Iadh Ounis, Stuart Mackie, Jarana Manotumruksa, Graham McDonald_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./tempsumm/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf](http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf)
- :material-file-search: **Runs:** [uogTrT1MANU](./tempsumm/runs.md#uogtrt1manu) | [uogTrT1X2iSCP](./tempsumm/runs.md#uogtrt1x2iscp) | [uogTrT1X2iTCP](./tempsumm/runs.md#uogtrt1x2itcp) | [uogTrT1X2iNCP](./tempsumm/runs.md#uogtrt1x2incp) | [uogTrT1X2cSCP](./tempsumm/runs.md#uogtrt1x2cscp) | [uogTrT1X2iSC](./tempsumm/runs.md#uogtrt1x2isc) | [uogTrT2EimpP](./tempsumm/runs.md#uogtrt2eimpp) | [uogTrT2EintP](./tempsumm/runs.md#uogtrt2eintp) | [uogTrdEQR1](./tempsumm/runs.md#uogtrdeqr1) | [uogTrdEEQR3](./tempsumm/runs.md#uogtrdeeqr3) | [uogTrhEQR2](./tempsumm/runs.md#uogtrheqr2) | [uogTrhEEQR4](./tempsumm/runs.md#uogtrheeqr4) | [uogTrhSqCR6](./tempsumm/runs.md#uogtrhsqcr6) | [uogTrdSqCR5](./tempsumm/runs.md#uogtrdsqcr5)

??? abstract "Abstract"
	
	In TREC 2015, we focus on tackling the challenges posed by the Contextual Suggestion, Temporal Summarisation and Dynamic Domain tracks. For Contextual Suggestion, we investigate the use of user-generated data in location-based social networks (LBSN) to suggest venues. For Temporal Summarisation, we examine features for event summarisation that explicitly model the entities involved in the events. Meanwhile, for the Dynamic Domain track, we explore resource selection techniques for identifying the domain of interest and diversifying sub-topic intents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieVMOMMM15.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieVMOMMM15,
		author = {Richard McCreadie and Saul Vargas and Craig MacDonald and Iadh Ounis and Stuart Mackie and Jarana Manotumruksa and Graham McDonald},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow at {TREC} 2015: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Dynamic Domain Tracks},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieVMOMMM15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Tasks 

#### Overview of the TREC 2015 Tasks Track

_Emine Yilmaz, Manisha Verma, Rishabh Mehrotra, Evangelos Kanoulas, Ben Carterette, Nick Craswell_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Overview-T.pdf](http://trec.nist.gov/pubs/trec24/papers/Overview-T.pdf)
??? abstract "Abstract"
	
	Research in Information Retrieval has traditionally focused on serving the best results for a single query, ignoring the reasons (or the task) that might have motivated the user to submit that query. Often times search engines are used to complete complex tasks (information needs); achieving these tasks with current search engines requires users to issue multiple queries. For example, booking travel to a location such as London could require the user to submit various queries such as flights to London, hotels in London, points of interest around London, etc. Standard evaluation mechanisms focus on evaluating the quality of a retrieval system in terms of the relevance of the results retrieved, completely ignoring the fact that user satisfaction mainly depends on the usefullness of the system in helping the user complete the actual task that led the user issue the query. The TREC 2015 Tasks Track is an attempt in devising mechanisms for evaluating quality of retrieval systems in terms of (1) how well they can understand the underlying task that led the user submit a query, and (2) how useful they are for helping users complete their tasks. In this overview, we first summarise the three categories of evaluation mechanisms used in the track and briefly describe the corpus, topics, and tasks that comprise the test collections. We then give an overview of the runs submitted to the Tasks Track and present evaluation results and analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YilmazVMKCC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/YilmazVMKCC15,
		author = {Emine Yilmaz and Manisha Verma and Rishabh Mehrotra and Evangelos Kanoulas and Ben Carterette and Nick Craswell},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2015 Tasks Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Overview-T.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YilmazVMKCC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mining Tasks from the Web Anchor Text Graph: MSR Notebook Paper  for the TREC 2015 Tasks Track

_Paul N. Bennett, Ryen W. White_

- :fontawesome-solid-user-group: **Participant:** [MSRTasks](./task/participants.md#msrtasks)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/MSRTasks-T.pdf](http://trec.nist.gov/pubs/trec24/papers/MSRTasks-T.pdf)
- :material-file-search: **Runs:** [MSRTasksQUrun3](./task/runs.md#msrtasksqurun3)

??? abstract "Abstract"
	
	Users may have a variety of tasks that give rise to issuing a particular query. The goal of the Tasks Track at TREC 2015 was to identify all aspects or subtasks of a user's task as well as the documents relevant to the entire task. This was broken into two parts: (1) Task Understanding which judged relevance of key phrases or queries to the original query (relative to a likely task that would have given rise to both); (2) Task Completion which performed document retrieval and measured usefulness to any task a user with the query might be peforming through either a completion measure that uses both relevance and usefulness criteria or more simply through an ad hoc retrieval measure of relevance alone. We submitted a run in the Task Understanding track. In particular, since the anchor text graph has proven useful in the general realm of query reformulation [2], we sought to quantify the value of extracting key phrases from anchor text in the broader setting of the task understanding track. Given a query, our approach considers a simple method for identifying a relevant and diverse set of key phrases related to the possible tasks that might have given rise to the query. In particular, given the effectiveness of sessions for producing query suggestions as well as the fact that sessions tend to be both topically coherent and cohesive with respect to a task, we investigated the effectiveness of mining session co-occurrence data. For a search engine log, session boundaries can be defined in the typical way but to operate over the anchor text graph, we need some notion of a “session”. We adopt the suggestion of Dang & Croft [2] and treat different links pointing to the same document as belonging to the same “session”. The basic assumption is that the anchor text of two links pointing to the same document are related via the common reference. Note that this assumption is based on the destination URL of the link being the same. Given a query, we then find matching seed candidates (link text from the web graph or queries over search logs) and expand to related candidate key phrases via this session assumption. The final ranking is based on a combination of  session count and the similarity of a link to the query. Additionally we perform several types of filtering that prevent over-expanding the set of related queries. We refer to the method as “having coverage” if the method was able to find a matching seed - since this is a necessary step to producing any candidates based on co-occurrence. Empirical results demonstrate generally good performance for the method when it finds a matching seed. In particular, of the 34 topics judged for the Query Understanding track, our method had coverage 62% of the time (21 topics). When the method has coverage, the suggested key phrases are above the mean performance (by nearly every measure reported) 2/3 times and the best performer 1/3 times. Given it's simplicity and availability to nearly all participants as well as the fact that coverage can be detected before submission, it is a promsing candidate for future investigation in the track. We now describe the method and results more fully before summarizing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BennettW15.bib) "
	```
	@inproceedings{DBLP:conf/trec/BennettW15,
		author = {Paul N. Bennett and Ryen W. White},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Mining Tasks from the Web Anchor Text Graph: {MSR} Notebook Paper for the {TREC} 2015 Tasks Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/MSRTasks-T.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BennettW15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2015: Tasks and Total Recall Tracks

_Matthias Hagen, Steve Göring, Magdalena Keil, Olaoluwa Anifowose, Amir Othman, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./task/participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Webis-TTR.pdf](http://trec.nist.gov/pubs/trec24/papers/Webis-TTR.pdf)
- :material-file-search: **Runs:** [webis1](./task/runs.md#webis1) | [webisC1](./task/runs.md#webisc1) | [webisC2](./task/runs.md#webisc2) | [webisC3](./task/runs.md#webisc3) | [webisA1](./task/runs.md#webisa1) | [webisA2](./task/runs.md#webisa2) | [webisA3](./task/runs.md#webisa3)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2015 Tasks and Total Recall tracks. In the task understanding subtask of the Tasks track, we use dierent data sources (AOL query log, Freebase, etc.) and APIs (Google, Bing, etc.) to retrieve topics related to a given query. All sources are combined in our SQuare system. The task completion subtask is based on combining the results of our ChatNoir 2 for the dierent topics identified in the task understanding subtask. Finally, for the ad-hoc subtask (similar to the previous years' Web tracks), we use an axiomatic re-ranking approach of the search results obtained from ChatNoir 2. In the Total Recall track, we employ a simple SVM baseline with variable batch sizes equipped with a keyqueries step to identify potentially relevant documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenGKAOS15.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenGKAOS15,
		author = {Matthias Hagen and Steve G{\"{o}}ring and Magdalena Keil and Olaoluwa Anifowose and Amir Othman and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2015: Tasks and Total Recall Tracks},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Webis-TTR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenGKAOS15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Total Recall 

#### TREC 2015 Total Recall Track Overview

_Adam Roegiest, Gordon V. Cormack, Charles L. A. Clarke, Maura R. Grossman_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec24/papers/Overview-TR.pdf](https://trec.nist.gov/pubs/trec24/papers/Overview-TR.pdf)
??? abstract "Abstract"
	
	The primary purpose of the Total Recall Track is to evaluate, through controlled simulation, methods designed to achieve very high recall - as close as practicable to 100% - with a human assessor in the loop. Motivating applications include, among others, electronic discovery in legal proceedings [2], systematic review in evidence-based medicine [11], and the creation of fully labeled test collections for information retrieval (“IR”) evaluation [8]. A secondary, but no less important, purpose is to develop a sandboxed virtual test environment within which IR systems may be tested, while preventing the disclosure of sensitive test data to participants. At the same time, the test environment also operates as a “black box,” affording participants confidence that their proprietary systems cannot easily be reverse engineered
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoegiestCCG15.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoegiestCCG15,
		author = {Adam Roegiest and Gordon V. Cormack and Charles L. A. Clarke and Maura R. Grossman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2015 Total Recall Track Overview},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {https://trec.nist.gov/pubs/trec24/papers/Overview-TR.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoegiestCCG15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Waterloo (Cormack) Participation in the TREC 2015 Total Recall Track

_Gordon V. Cormack, Maura R. Grossman_

- :fontawesome-solid-user-group: **Participant:** [WaterlooCormack](./recall/participants.md#waterloocormack)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WaterlooCormack-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/WaterlooCormack-TR.pdf)
- :material-file-search: **Runs:** [UWGVCknee100](./recall/runs.md#uwgvcknee100) | [UWGVCknee1000](./recall/runs.md#uwgvcknee1000) | [stop3299](./recall/runs.md#stop3299)

??? abstract "Abstract"
	
	In the course of developing tools for the 2015 Total Recall Track, co-coordinators Cormack and Grossman created an autonomous continuous active learning (“CAL”) system, which was provided to participants as the baseline model implementation (“BMI”) [http://plg.uwaterloo.ca/⇠gvcormac/trecvm/]. BMI essentially employs the approach described by Cormack and Grossman [http://arxiv.org/abs/1504.06868]; the only difference is that BMI employs logistic regression implemented by Sofia ML [https://code.google.com/p/sofia-ml/] instead of SVMlight [http://svmlight.joachims.org/]. The Waterloo (Cormack) team submitted runs using BMI for each of the five 2015 Total Recall test collections. The only change that was made to BMI was to add a provision to “call our shot” - that is, to indicate to the assessment server when we believed the run to be reasonably complete. Although the Track provided three milestones - '70recall,' '80recall,' and 'reasonable' - we made no attempt to quantify the recall of our runs, and instead used the three milestones to indicate graduated levels of completeness, which one might interpret as “good,” “better,” and 'best.' [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackG15.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackG15,
		author = {Gordon V. Cormack and Maura R. Grossman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Waterloo (Cormack) Participation in the {TREC} 2015 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/WaterlooCormack-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackG15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Efficient semantic indexing via neural networks with dynamic supervised  feedback

_Vivek Dhand_

- :fontawesome-solid-user-group: **Participant:** [CCRi](./recall/participants.md#ccri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/CCRi-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/CCRi-TR.pdf)
- :material-file-search: **Runs:** [CCRi-athome](./recall/runs.md#ccri-athome)

??? abstract "Abstract"
	
	We describe a portable system for ecient semantic indexing of documents via neural networks with dynamic supervised feedback. We initially represent each document as a modified TF-IDF sparse vector and then apply a learned mapping to a compact embedding space. This mapping is produced by a shallow neural network which learns a latent representation for the textual graph linking words to nearby contexts. The resulting document embeddings provide significantly better semantic representation, partly because they incorporate information about synonyms. Query topics are uniformly represented in the same manner as documents. For each query, we dynamically train an additional hidden layer which modifies the embedding space in response to relevance judgements. The system was tested using the documents and topics provided in the Total Recall track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Dhand15.bib) "
	```
	@inproceedings{DBLP:conf/trec/Dhand15,
		author = {Vivek Dhand},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Efficient semantic indexing via neural networks with dynamic supervised feedback},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/CCRi-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Dhand15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### e-Discovery Team at TREC 2015 Total Recall Track

_Ralph Losey, Jim Sullivan, Tony Reichenberger_

- :fontawesome-solid-user-group: **Participant:** [eDiscoveryTeam](./recall/participants.md#ediscoveryteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/eDiscoveryTeam-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/eDiscoveryTeam-TR.pdf)
- :material-file-search: **Runs:** [Multimodal](./recall/runs.md#multimodal)

??? abstract "Abstract"
	
	The 2015 TREC Total Recall Track provided instant relevance feedback in thirty prejudged topics searching three different datasets. The e-Discovery Team of three attorneys specializing in legal search participated in all thirty topics using Kroll Ontrack's search and review software, eDiscovery.com Review (EDR). They employed a hybrid approach to continuous active learning that uses both manual and automatic searches. A variety of manual search methods were used to find training documents, including high probability ranked documents and keywords, an ad hoc process the Team calls multimodal. In the one topic (109) requiring legal analysis the Team's approach was significantly more effective than all other participants, including the fully automated approaches that otherwise attained comparable scores. In all topics the Team's hybrid multimodal method consistently attained the highest F1 values at the time of Reasonable Call, equivalent to a stop point. In all topics the Team's multimodal human machine approach also found relevant documents more quickly and with greater precision than the fully automated or other methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LoseySR15.bib) "
	```
	@inproceedings{DBLP:conf/trec/LoseySR15,
		author = {Ralph Losey and Jim Sullivan and Tony Reichenberger},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {e-Discovery Team at {TREC} 2015 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/eDiscoveryTeam-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LoseySR15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TUW at the First Total Recall Track

_Mihai Lupu_

- :fontawesome-solid-user-group: **Participant:** [TUW](./recall/participants.md#tuw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/TUW-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/TUW-TR.pdf)
- :material-file-search: **Runs:** [1NB](./recall/runs.md#1nb) | [1ST](./recall/runs.md#1st) | [1SB](./recall/runs.md#1sb) | [6SB](./recall/runs.md#6sb) | [6NB](./recall/runs.md#6nb) | [6ST](./recall/runs.md#6st) | [1NB_sandbox](./recall/runs.md#1nb_sandbox) | [1ST_sandbox](./recall/runs.md#1st_sandbox) | [1SB_sandbox](./recall/runs.md#1sb_sandbox) | [6SB_sandbox](./recall/runs.md#6sb_sandbox) | [6NB_sandbox](./recall/runs.md#6nb_sandbox) | [6ST_sandbox](./recall/runs.md#6st_sandbox)

??? abstract "Abstract"
	
	For the first participation in the TREC Total Recall track, we set out to try some basic changes to the baseline provided by the organisers. Namely, the weighting scheme, the use of stopwords, and the number of learners that contribute to the decision of which documents to ask the virtual assessor to review. We observed that the baseline was extremely strong and none of the runs significantly and consistently outperformed it.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lupu15.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lupu15,
		author = {Mihai Lupu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TUW} at the First Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/TUW-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lupu15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Constrained Approach to Manual Total Recall

_Jeremy Pickens, Tom Gricks, Bayu Hardi, Mark Noel_

- :fontawesome-solid-user-group: **Participant:** [catres](./recall/participants.md#catres)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/catres-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/catres-TR.pdf)
- :material-file-search: **Runs:** [attemptone](./recall/runs.md#attemptone)

??? abstract "Abstract"
	
	The Catalyst participation in the manual at home Total Recall Track was both limited and quick, a TREC submission of practicality over research. The group's decision to participate in TREC was made three weeks, and data was not loaded until six days, before the final submission deadline. As a result and to reasonably simulate an expedited document review process, a number of shortcuts were taken in order to accomplish the runs in limited time. Choices about implementation details were due primarily to time constraint and necessity, rather than out of designed scientific hypothesis. We detail these shortcuts, as well as provide a few additional post hoc, non-ocial runs in which we remove some of the shortcuts and constraints. We also explore the e↵ect of di↵erent manual seeding approaches on the recall outcome.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PickensGHN15.bib) "
	```
	@inproceedings{DBLP:conf/trec/PickensGHN15,
		author = {Jeremy Pickens and Tom Gricks and Bayu Hardi and Mark Noel},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Constrained Approach to Manual Total Recall},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/catres-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PickensGHN15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WHU at TREC Total Recall Track 2015

_Chuan Wu, Wei Lu, Ruixue Wang_

- :fontawesome-solid-user-group: **Participant:** [WHU_IRGroup](./recall/participants.md#whu_irgroup)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WHU_IRGroup-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/WHU_IRGroup-TR.pdf)
- :material-file-search: **Runs:** [iterative_expansion](./recall/runs.md#iterative_expansion)

??? abstract "Abstract"
	
	This paper describes the WHU IRLAB participation to the Total Recall Track in TREC 2015. We implement an end-to-end system to deal with the total recall task. We propose an iterative query expansion method, which construct queries using iteratively selected terms. We choose to participate the 'Play-at-home' evaluation. Results are presented and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuLW15.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuLW15,
		author = {Chuan Wu and Wei Lu and Ruixue Wang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{WHU} at {TREC} Total Recall Track 2015},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/WHU\_IRGroup-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuLW15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke: TREC 2015 Total Recall Track

_Haotian Zhang, Wu Lin, Yipeng Wang, Charles L. A. Clarke, Mark D. Smucker_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./recall/participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-TR.pdf)
- :material-file-search: **Runs:** [UWPAH](./recall/runs.md#uwpah) | [UWPAH_](./recall/runs.md#uwpah_)

??? abstract "Abstract"
	
	The total recall track in TREC 2015 seeks an enhanced model to accelerate the autonomous technology-assisted review process. This paper introduces several noval ideas such as clustering based seed selection method, extended n-grams features and continuous query expansion learned from the relevant documents derived from each iteration. These methods can retrieve more relevant documents from each iteration thereby achieving high recall while requiring less review effort.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangLWCS15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangLWCS15,
		author = {Haotian Zhang and Wu Lin and Yipeng Wang and Charles L. A. Clarke and Mark D. Smucker},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {WaterlooClarke: {TREC} 2015 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-TR.pdf},
		timestamp = {Sun, 09 Aug 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangLWCS15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam (ILPS) at TREC 2015 Total Recall Track

_David van Dijk, Zhaochun Ren, Evangelos Kanoulas, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UvA.ILPS](./recall/participants.md#uva.ilps)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/UvA.ILPS-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/UvA.ILPS-TR.pdf)
- :material-file-search: **Runs:** [BASELINE](./recall/runs.md#baseline) | [BASELINE2](./recall/runs.md#baseline2) | [BASELINE_SANDBOX](./recall/runs.md#baseline_sandbox) | [BASELINE2_SANDBOX](./recall/runs.md#baseline2_sandbox)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdams ILPS group in the Total Recall track at TREC 2015. Based on the provided Baseline Model Implemention (”BMI”) we set out to provide two more baselines we can compare to in future work. The two methods are bootstrapped by a synthetic document based on the query, use TF/IDF features, and sample with dynamic batch sizes which depend on the percentage of predicted relevant documents. We sample at least 1 percent of the corpus and stop sampling if a batch contains no relevant documents. The methods differ in the classifier used, i.e. Logistic Regression and Random Forest.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DijkRKR15.bib) "
	```
	@inproceedings{DBLP:conf/trec/DijkRKR15,
		author = {David van Dijk and Zhaochun Ren and Evangelos Kanoulas and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Amsterdam {(ILPS)} at {TREC} 2015 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/UvA.ILPS-TR.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DijkRKR15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2015: Tasks and Total Recall Tracks

_Matthias Hagen, Steve Göring, Magdalena Keil, Olaoluwa Anifowose, Amir Othman, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./recall/participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Webis-TTR.pdf](http://trec.nist.gov/pubs/trec24/papers/Webis-TTR.pdf)
- :material-file-search: **Runs:** [Baseline](./recall/runs.md#baseline) | [Keyphrase](./recall/runs.md#keyphrase) | [SandboxBaseline](./recall/runs.md#sandboxbaseline) | [SandboxKeyphrase](./recall/runs.md#sandboxkeyphrase)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2015 Tasks and Total Recall tracks. In the task understanding subtask of the Tasks track, we use dierent data sources (AOL query log, Freebase, etc.) and APIs (Google, Bing, etc.) to retrieve topics related to a given query. All sources are combined in our SQuare system. The task completion subtask is based on combining the results of our ChatNoir 2 for the dierent topics identified in the task understanding subtask. Finally, for the ad-hoc sub-task (similar to the previous years' Web tracks), we use an axiomatic re-ranking approach of the search results obtained from ChatNoir 2. In the Total Recall track, we employ a simple SVM baseline with variable batch sizes equipped with a keyqueries step to identify potentially relevant documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenGKAOS15.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenGKAOS15,
		author = {Matthias Hagen and Steve G{\"{o}}ring and Magdalena Keil and Olaoluwa Anifowose and Amir Othman and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2015: Tasks and Total Recall Tracks},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Webis-TTR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenGKAOS15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Dynamic Domain 

#### TREC 2015 Dynamic Domain Track Overview

_Hui Yang, John R. Frank, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec24/papers/overview-dd.pdf](https://trec.nist.gov/pubs/trec24/papers/overview-dd.pdf)
??? abstract "Abstract"
	
	Search tasks for professional searchers, such as law enforcement agencies, police officers, and patent examiners, are often more complex than open domain Web search tasks. When professional searchers look for relevant information, it is often the case that they need to go through multiple iterations of searches to interact with a system. The Dynamic Domain Track supports research in dynamic, exploratory search within complex information domains. By providing real-time fine-grained feedback with relevance judgments that was collected during assessing time to the participating systems, we create a dynamic and iterative search process that lasts until the system decides to stop. The search systems are expected to be able to adjust their retrieval algorithms based on the feedback and find quickly relevant information for a multi-faceted information need. This document reports the task, datasets, topic and assessment creation, submissions, and evaluation results for the TREC 2015 Dynamic Domain (DD) Track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001FS15.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001FS15,
		author = {Hui Yang and John R. Frank and Ian Soboroff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2015 Dynamic Domain Track Overview},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {https://trec.nist.gov/pubs/trec24/papers/overview-dd.pdf},
		timestamp = {Wed, 03 Feb 2021 08:31:23 +0100},
		biburl = {https://dblp.org/rec/conf/trec/0001FS15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Dynamic Domain: Polar Science

_Annie Bryant Burgess, Chris Mattmann, Giuseppe Totaro, Lewis John McGibbney, Paul M. Ramirez_

- :fontawesome-solid-user-group: **Participant:** [JPL_USC](./domain/participants.md#jpl_usc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/JPL_USC-DD.pdf](http://trec.nist.gov/pubs/trec24/papers/JPL_USC-DD.pdf)

??? abstract "Abstract"
	
	This paper outlines the creation of the Polar dataset within the TREC-Dynamic Domain track. The techniques used to create the Polar dataset fall into two basic categories: information extraction using Apache Tika and information retrieval using Apache Nutch. Frist, we expanded the parsing capabilities of Apache Tika, an open source framework for text and metadata extraction, to provide more searchable content within Polar data repositories. Second, we used Apache Nutch, a distributed search engine that runs on top of Apache Hadoop, to crawl three prominent Polar data repositories: the National Science Foundation Advanced Cooperative Arctic Data and Information System (ACADIS), the National Snow and Ice Data Center (NSIDC) Arctic Data Explorer (ADE), and the National Aeronautics and Space Administration Antarctic Master Directory (AMD). Because finding data is often a primary challenge in scientific discovery, the inclusion of the Polar dataset in TREC-DD helps advance science through data discovery and provides TREC-DD a new challenge in in the realm of search relevancy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BurgessMTMR15.bib) "
	```
	@inproceedings{DBLP:conf/trec/BurgessMTMR15,
		author = {Annie Bryant Burgess and Chris Mattmann and Giuseppe Totaro and Lewis John McGibbney and Paul M. Ramirez},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} Dynamic Domain: Polar Science},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/JPL\_USC-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BurgessMTMR15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Laval University and Lakehead University at TREC Dynamic Domain  2015: Combination of Techniques for Subtopics Coverage

_Robin Joganah, Luc Lamontagne, Richard Khoury_

- :fontawesome-solid-user-group: **Participant:** [LavallVA](./domain/participants.md#lavallva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/LavallVA-DD.pdf](http://trec.nist.gov/pubs/trec24/papers/LavallVA-DD.pdf)

??? abstract "Abstract"
	
	This paper describes the joint submission by Laval University and Lakehead University to the TREC 2015 Dynamic Domain track. We submitted four runs for the main track and one run for the judged-only track. In our view, the Dynamic Domain process can be separated into two phases: a traditional static information retrieval phase to generate an initial set of documents, followed by a dynamic information retrieval phase which takes user feedback into account to improve the results. We developed an algorithm that combines keyword search, Latent Dirichlet Allocation, and K-Means clustering to take advantage of each technique to generate the best subset of results for the user. Our systems performed mostly over the median of the group of participants and our system for the “judged-only” task had the best score for a wide range of queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoganahLK15.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoganahLK15,
		author = {Robin Joganah and Luc Lamontagne and Richard Khoury},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Laval University and Lakehead University at {TREC} Dynamic Domain 2015: Combination of Techniques for Subtopics Coverage},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/LavallVA-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoganahLK15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Re-ranking via User Feedback: Georgetown University at TREC 2015  DD Track

_Jiyun Luo, Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [georgetown](./domain/participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/georgetown_ir-DD.pdf](http://trec.nist.gov/pubs/trec24/papers/georgetown_ir-DD.pdf)
- :material-file-search: **Runs:** [GU_RUN3_SIMI](./domain/runs.md#gu_run3_simi) | [GU_RUN4_SIMI](./domain/runs.md#gu_run4_simi)

??? abstract "Abstract"
	
	There are two principal components involved in a search process, the user and the search engine. In TREC DD, the user is modeled by a simulator, called “jig”. The jig and the search engine exchange many messages among themselves, including the relevant passages returned by the jig, user cost spent on examining the documents, etc. In this work, we don't apply any dynamic search algorithms to model these interactions. Instead, we produce a basic re-ranking baseline. Our algorithm starts at taking in an initial query from the simulator. During the search, we collect the relevance feedback from the simulator and use them to re-rank the initial retrieval results. Our algorithm terminates itself automatically when it senses that the user has gained enough information about the search topic or that no further relevant documents can be retrieved for the user.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuoY15.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuoY15,
		author = {Jiyun Luo and Hui Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Re-ranking via User Feedback: Georgetown University at {TREC} 2015 {DD} Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/georgetown\_ir-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuoY15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2015: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Dynamic Domain Tracks

_Richard McCreadie, Saul Vargas, Craig MacDonald, Iadh Ounis, Stuart Mackie, Jarana Manotumruksa, Graham McDonald_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./domain/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf](http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf)
- :material-file-search: **Runs:** [uogTrEpsilonG](./domain/runs.md#uogtrepsilong) | [uogTrRR](./domain/runs.md#uogtrrr) | [uogTrSI](./domain/runs.md#uogtrsi) | [uogTrIL](./domain/runs.md#uogtril) | [uogTrxQuADRR](./domain/runs.md#uogtrxquadrr)

??? abstract "Abstract"
	
	In TREC 2015, we focus on tackling the challenges posed by the Contextual Suggestion, Temporal Summarisation and Dynamic Domain tracks. For Contextual Suggestion, we investigate the use of user-generated data in location-based social networks (LBSN) to suggest venues. For Temporal Summarisation, we examine features for event summarisation that explicitly model the entities involved in the events. Meanwhile, for the Dynamic Domain track, we explore resource selection techniques for identifying the domain of interest and diversifying sub-topic intents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieVMOMMM15.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieVMOMMM15,
		author = {Richard McCreadie and Saul Vargas and Craig MacDonald and Iadh Ounis and Stuart Mackie and Jarana Manotumruksa and Graham McDonald},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow at {TREC} 2015: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Dynamic Domain Tracks},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieVMOMMM15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## LiveQA 

#### Overview of the TREC 2015 LiveQA Track

_Eugene Agichtein, David Carmel, Dan Pelleg, Yuval Pinter, Donna Harman_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Overview-QA.pdf](http://trec.nist.gov/pubs/trec24/papers/Overview-QA.pdf)
??? abstract "Abstract"
	
	The automated question answering (QA) track, one of the most popular tracks in TREC for many years, has focused on the task of providing automatic answers for human questions. The track primarily dealt with factual questions, and the answers provided by participants were extracted from a corpus of News articles. While the task evolved to model increasingly realistic information needs, addressing question series, list questions, and even interactive feedback, a major limitation remained: the questions did not directly come from real users, in real time. The LiveQA track, conducted for the rst time this year, focused on real-time question answering for real-user questions. Real user questions, i.e., fresh questions submitted on the Yahoo Answers (YA) site that have not yet been answered, were sent to the participant systems, which provided an answer in real time. Returned answers were judged by TREC editors on a 4-level Likert scale.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AgichteinCPPH15.bib) "
	```
	@inproceedings{DBLP:conf/trec/AgichteinCPPH15,
		author = {Eugene Agichtein and David Carmel and Dan Pelleg and Yuval Pinter and Donna Harman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2015 LiveQA Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Overview-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AgichteinCPPH15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at the TREC 2015 LiveQA Track

_Ruey-Cheng Chen, J. Shane Culpepper, Tadele Tedla Damessie, Timothy Jones, Ahmed Mourad, Kevin Ong, Falk Scholer, Evi Yulianti_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./qa/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/RMIT-QA.pdf](http://trec.nist.gov/pubs/trec24/papers/RMIT-QA.pdf)
- :material-file-search: **Runs:** [RMIT1](./qa/runs.md#rmit1) | [RMIT3](./qa/runs.md#rmit3) | [RMIT2](./qa/runs.md#rmit2) | [system2](./qa/runs.md#system2)

??? abstract "Abstract"
	
	This paper describes the four systems RMIT fielded for the TREC 2015 LiveQA task and the associated experiments. The challenge results show that the base run RMIT-0 has achieved an above-average performance, but other attempted improvements have all resulted in decreased retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenCD0MOSY15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenCD0MOSY15,
		author = {Ruey{-}Cheng Chen and J. Shane Culpepper and Tadele Tedla Damessie and Timothy Jones and Ahmed Mourad and Kevin Ong and Falk Scholer and Evi Yulianti},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{RMIT} at the {TREC} 2015 LiveQA Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/RMIT-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenCD0MOSY15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NudtMDP at TREC 2015 LiveQA Track

_Yuanping Nie, Jiuming Huang, Zongsheng Xie, Hai Li, Pengfei Zhang, Yan Jia_

- :fontawesome-solid-user-group: **Participant:** [NUDTMDP](./qa/participants.md#nudtmdp)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/NUDTMDP-QA.pdf](http://trec.nist.gov/pubs/trec24/papers/NUDTMDP-QA.pdf)
- :material-file-search: **Runs:** [NUDTMDP1](./qa/runs.md#nudtmdp1) | [NUDTMDP2](./qa/runs.md#nudtmdp2) | [NUDTMDP3](./qa/runs.md#nudtmdp3)

??? abstract "Abstract"
	
	In this paper, we describe a web-based online question answering system which has been evaluated in TREC 2015 Live QA task. Automatic question answering is a classic widely learned technology. TREC have host 8 times QA tracks since 1999. However, the TREC results show that there is still a long way to solve the questions perfectly. LiveQA is kind of questions means asked by 'real users'. Most liveQAs are non-factoid questions and it is much more challenge to answer the liveQAs than factoid QAs. We build a question answering system to find the answers from web data. The system has two channels, one use search engine to obtain the answers and the other focus on community question answering websites. We finally submit 3 runs in the ocial test. Two of our runs can perform much better than the avarge scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NieHXLZJ15.bib) "
	```
	@inproceedings{DBLP:conf/trec/NieHXLZJ15,
		author = {Yuanping Nie and Jiuming Huang and Zongsheng Xie and Hai Li and Pengfei Zhang and Yan Jia},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {NudtMDP at {TREC} 2015 LiveQA Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/NUDTMDP-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NieHXLZJ15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ranking Answers and Web Passages for Non-factoid Question Answering:  Emory University at TREC LiveQA

_Denis Savenkov_

- :fontawesome-solid-user-group: **Participant:** [emory](./qa/participants.md#emory)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/emory-QA.pdf](http://trec.nist.gov/pubs/trec24/papers/emory-QA.pdf)
- :material-file-search: **Runs:** [Out-of-mEmory](./qa/runs.md#out-of-memory)

??? abstract "Abstract"
	
	This paper describes a question answering system built by a team from Emory University to participate in TREC LiveQA'15 shared task. The goal of this task was to automatically answer questions posted to Yahoo! Answers community question answering website in real-time. My system combines candidates extracted from answers to similar questions previously posted to Yahoo! Answers and web passages from documents retrieved using web search. The candidates are ranked by a trained linear model and the top candidate is returned as the final answer. The ranking model is trained on question and answer (QnA) pairs from Yahoo! Answers archive using pairwise ranking criterion. Candidates are represented with a set of features, which includes statistics about candidate text, question term matches and retrieval scores, associations between question and candidate text terms and the score returned by a Long Short-Term Memory (LSTM) neural network model. Our system ranked top 5 by answer precision, and took 7th place according to the average answer score. In this paper I will describe our approach in detail, present the results and analysis of the system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Savenkov15.bib) "
	```
	@inproceedings{DBLP:conf/trec/Savenkov15,
		author = {Denis Savenkov},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Ranking Answers and Web Passages for Non-factoid Question Answering: Emory University at {TREC} LiveQA},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/emory-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Savenkov15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question/Answer Matching for Yahoo! Answers Using a Corpus-Based Extracted  Ngram-based Mapping

_Stalin Varanasi, Günter Neumann_

- :fontawesome-solid-user-group: **Participant:** [dfkiqa](./qa/participants.md#dfkiqa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/dfkiqa-QA.pdf](http://trec.nist.gov/pubs/trec24/papers/dfkiqa-QA.pdf)
- :material-file-search: **Runs:** [dfkiqa](./qa/runs.md#dfkiqa)

??? abstract "Abstract"
	
	This report describes the work done by the QA group of the Multilingual Technologies Lab at DFKI for the 2015 edition of the TREC LiveQA track. We describe the system, issues faced and the approaches followed considering the time lines of the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VaranasiN15.bib) "
	```
	@inproceedings{DBLP:conf/trec/VaranasiN15,
		author = {Stalin Varanasi and G{\"{u}}nter Neumann},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Question/Answer Matching for Yahoo! Answers Using a Corpus-Based Extracted Ngram-based Mapping},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/dfkiqa-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VaranasiN15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke: TREC 2015 LiveQA Track

_Alexandra Vtyurina, Ankita Dey, Bahareh Sarrafzadeh, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./qa/participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-QA.pdf](http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-QA.pdf)
- :material-file-search: **Runs:** [system4](./qa/runs.md#system4)

??? abstract "Abstract"
	
	The goal of the LiveQA track is to automatically provide answers to questions posted by real people. Previous question answering tracks included factoid questions, list questions and complex questions[3]. Presented in 2015 for the first time the LiveQA track gave the participants an opportunity to answer questions posed by real people, as opposed to manually configured ones in the previous tasks. The questions for the task were harvested from Yahoo! Answers1 - a community question answering website. Each question was broadcasted to all registered systems. The participants had to supposed to provide an answer to every given question within a timeframe of 60 seconds. The answers were judged by human NIST assessors after the evaluation was over.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VtyurinaDSC15.bib) "
	```
	@inproceedings{DBLP:conf/trec/VtyurinaDSC15,
		author = {Alexandra Vtyurina and Ankita Dey and Bahareh Sarrafzadeh and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {WaterlooClarke: {TREC} 2015 LiveQA Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VtyurinaDSC15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CMU OAQA at TREC 2015 LiveQA: Discovering the Right Answer with  Clues

_Di Wang, Eric Nyberg_

- :fontawesome-solid-user-group: **Participant:** [CMUOAQA](./qa/participants.md#cmuoaqa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/oaqa-QA.pdf](http://trec.nist.gov/pubs/trec24/papers/oaqa-QA.pdf)
- :material-file-search: **Runs:** [CMUOAQA](./qa/runs.md#cmuoaqa)

??? abstract "Abstract"
	
	In this paper, we present CMU's automatic, web-based, real-time question answering (QA) system that was evaluated in the TREC 2015 LiveQA Challenge. This system answers real-user questions freshly submitted to the Yahoo! Answers website that have not been previously answered by humans. Given the title and body of the question, we generated multiple sets of keyword queries and retrieved a collection of web pages based on those queries. Then we extracted answer candidates from web pages in the form of answer passages and their associated clue. Finally, we combined both IR- and NLP-based relevance models to rank and select answer candidates. In the TREC 2015 LiveQA evaluations, human assessors gave our system an average score of 1.081 on a three-point scale, the highest average score achieved by a system in the competition (the second-best score was .677, and the average score was .465 for the 21 systems evaluated).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangN15.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangN15,
		author = {Di Wang and Eric Nyberg},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CMU} {OAQA} at {TREC} 2015 LiveQA: Discovering the Right Answer with Clues},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/oaqa-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangN15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Leverage Web-based Answer Retrieval and Hierarchical Answer Selection  to Improve the Performance of Live Question Answering

_GuoShun Wu, Man Lan_

- :fontawesome-solid-user-group: **Participant:** [ECNUCS](./qa/participants.md#ecnucs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/ecnucs-QA.pdf](http://trec.nist.gov/pubs/trec24/papers/ecnucs-QA.pdf)
- :material-file-search: **Runs:** [ecnucs](./qa/runs.md#ecnucs)

??? abstract "Abstract"
	
	This paper reports on East Normal China University's participation in the TREC 2015 LiveQA track. An overview is presented to introduce our community question answer system and discuss the technologies. This year, the Trec LiveQA track expands the traditional QA track, focusing on “live” question answering for the real-user questions. At this challenge, we built a real-time community question answer system. Our results are presented at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuL15.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuL15,
		author = {GuoShun Wu and Man Lan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Leverage Web-based Answer Retrieval and Hierarchical Answer Selection to Improve the Performance of Live Question Answering},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/ecnucs-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuL15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ECNU at TREC 2015: LiveQA Track

_Weiqian Zhang, Weijie An, Jinchao Ma, Yan Yang, Qinmin Hu, Liang He_

- :fontawesome-solid-user-group: **Participant:** [ECNU](./qa/participants.md#ecnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/ECNU-QA.pdf](http://trec.nist.gov/pubs/trec24/papers/ECNU-QA.pdf)
- :material-file-search: **Runs:** [ECNU_ICA_2](./qa/runs.md#ecnu_ica_2)

??? abstract "Abstract"
	
	This paper reports on East Normal China University's participation in the TREC 2015 LiveQA track. An overview is presented to introduce our community question answer system and discuss the technologies. This year, the Trec LiveQA track expands the traditional QA track, focusing on “live” question answering for the real-user questions. At this challenge, we built a real-time community question answer system. Our results are presented at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangAMYHH15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangAMYHH15,
		author = {Weiqian Zhang and Weijie An and Jinchao Ma and Yan Yang and Qinmin Hu and Liang He},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ECNU} at {TREC} 2015: LiveQA Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/ECNU-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangAMYHH15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLIP at TREC 2015: Microblog and LiveQA

_Mossaab Bagdouri, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [CLIP](./qa/participants.md#clip)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/CLIP-MBQA.pdf](http://trec.nist.gov/pubs/trec24/papers/CLIP-MBQA.pdf)
- :material-file-search: **Runs:** [CLIP3](./qa/runs.md#clip3) | [CLIP2](./qa/runs.md#clip2) | [CLIP1](./qa/runs.md#clip1)

??? abstract "Abstract"
	
	The Computational Linguistics and Information Processing lab at the University of Maryland participated in two TREC tracks this year. The Microblog Real-Time Filtering and the LiveQA tasks both involve information processing in real time. We submitted nine runs in total, achieving relatively good results. This paper describes the architecture and configuration of the systems behind those runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BagdouriO15.bib) "
	```
	@inproceedings{DBLP:conf/trec/BagdouriO15,
		author = {Mossaab Bagdouri and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CLIP} at {TREC} 2015: Microblog and LiveQA},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/CLIP-MBQA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BagdouriO15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ADAPT.DCU at TREC LiveQA: A Sentence Retrieval based Approach  to Live Question Answering

_Dasha Bogdanova, Debasis Ganguly, Jennifer Foster, Ali Hosseinzadeh Vahid_

- :fontawesome-solid-user-group: **Participant:** [ADAPT.DCU](./qa/participants.md#adapt.dcu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/ADAPT.DCU-QA.pdf](http://trec.nist.gov/pubs/trec24/papers/ADAPT.DCU-QA.pdf)
- :material-file-search: **Runs:** [system7](./qa/runs.md#system7)

??? abstract "Abstract"
	
	This paper describes the work done by ADAPT centre at Dublin City University towards automatically answering questions for the TREC LiveQA track. The system is based on a sentence retrieval approach. In particular, we first use the title of a new question as a query so as to retrieve a ranked list of conceptually similar questions from an index of previously asked on “Yahoo! Answers”. We then extract the best matching sentences from the answers of the retrieved questions. In order to construct the final answer, we combine these sentences with the best answer of the top ranked (most similar to the query) question. When no pre-existing questions with sufficient similarity with the new one can be retrieved from the index, we output an answer from a candidate set of pre-generated answers based on the domain of the question.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BogdanovaGFV15.bib) "
	```
	@inproceedings{DBLP:conf/trec/BogdanovaGFV15,
		author = {Dasha Bogdanova and Debasis Ganguly and Jennifer Foster and Ali Hosseinzadeh Vahid},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ADAPT.DCU} at {TREC} LiveQA: {A} Sentence Retrieval based Approach to Live Question Answering},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/ADAPT.DCU-QA.pdf},
		timestamp = {Thu, 21 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BogdanovaGFV15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QU at TREC-2015: Building Real-Time Systems for Tweet Filtering  and Question Answering

_Reem Suwaileh, Maram Hasanain, Marwan Torki, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./qa/participants.md#qu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/QU-MBQA.pdf](http://trec.nist.gov/pubs/trec24/papers/QU-MBQA.pdf)
- :material-file-search: **Runs:** [QU1](./qa/runs.md#qu1)

??? abstract "Abstract"
	
	This paper presents our participation in the microblog and LiveQA tracks in TREC-2015. Both tracks required building a “real-time” system that monitors a data stream and responds to users' information needs in real-time. For the microblog track, given a set of users' interest profiles, we developed two online filtering systems that recommend “relevant” and “novel” tweets from a tweet stream for each profile. Both systems simulate real scenarios: filtered tweets are sent as push notifications on a mobile phone or as a periodic email digest. We study the e↵ect of using a static versus dynamic relevance thresholds to control the relevancy of filtered output to interest profiles. We also experiment with di↵erent profile expansion strategies that account for potential topic drift. Our results show that the baseline run of the push notifications scenario that uses a static threshold with light profile expansion achieved the best results. Similarly, in the email digest scenario, the baseline run that used a shorter representation of the interest profiles without any expansion was the best run. For the LiveQA track, the system was required to answer a stream of around 1000 real-time questions from Yahoo! Answers. We adopted a very simple approach that searched an archived Yahoo! Answers QA dataset for similar questions to the asked ones and retrieved back their answers
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SuwailehHTE15.bib) "
	```
	@inproceedings{DBLP:conf/trec/SuwailehHTE15,
		author = {Reem Suwaileh and Maram Hasanain and Marwan Torki and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{QU} at {TREC-2015:} Building Real-Time Systems for Tweet Filtering and Question Answering},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/QU-MBQA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SuwailehHTE15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

