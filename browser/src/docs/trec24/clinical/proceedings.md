# Proceedings - Clinical Decision Support 2015 

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

- :fontawesome-solid-user-group: **Participant:** [LIST_LUX](./participants.md#list_lux)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/LIST_LUX-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/LIST_LUX-CL.pdf)
- :material-file-search: **Runs:** [Run1DBpSimp](./runs.md#run1dbpsimp) | [Run2DBpComb](./runs.md#run2dbpcomb) | [Run4HLM](./runs.md#run4hlm) | [Run5DBpAbs](./runs.md#run5dbpabs)

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

- :fontawesome-solid-user-group: **Participant:** [EMSE](./participants.md#emse)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/EMSE-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/EMSE-CL.pdf)
- :material-file-search: **Runs:** [EMSEasmer](./runs.md#emseasmer) | [EMSElsi](./runs.md#emselsi) | [EMSErm3](./runs.md#emserm3)

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

- :fontawesome-solid-user-group: **Participant:** [wsu_ir](./participants.md#wsu_ir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/wsu_ir-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/wsu_ir-CL.pdf)
- :material-file-search: **Runs:** [wsuirsaa](./runs.md#wsuirsaa) | [wsuirdaa](./runs.md#wsuirdaa) | [wsuirdma](./runs.md#wsuirdma) | [wsuirsab](./runs.md#wsuirsab) | [wsuirdmb](./runs.md#wsuirdmb) | [wsuirsmb](./runs.md#wsuirsmb)

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

- :fontawesome-solid-user-group: **Participant:** [LAMDA](./participants.md#lamda)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/LAMDA-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/LAMDA-CL.pdf)
- :material-file-search: **Runs:** [lamdarun01](./runs.md#lamdarun01) | [lamdarun02](./runs.md#lamdarun02) | [lamdarun03](./runs.md#lamdarun03) | [lamdarun04](./runs.md#lamdarun04) | [lamdarun05](./runs.md#lamdarun05) | [lamdarun06](./runs.md#lamdarun06)

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

- :fontawesome-solid-user-group: **Participant:** [CL_CAMB](./participants.md#cl_camb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/CL_CAMB-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/CL_CAMB-CL.pdf)
- :material-file-search: **Runs:** [CAMspud1](./runs.md#camspud1) | [CAMspud3](./runs.md#camspud3) | [CAMspud5](./runs.md#camspud5) | [CAMspud6](./runs.md#camspud6) | [CAMspud7](./runs.md#camspud7) | [CAMspud8](./runs.md#camspud8)

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

- :fontawesome-solid-user-group: **Participant:** [LIMSI](./participants.md#limsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/LIMSI-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/LIMSI-CL.pdf)
- :material-file-search: **Runs:** [LIMSIrun1BoW](./runs.md#limsirun1bow) | [LIMSIrun2MSH](./runs.md#limsirun2msh) | [LIMSIrun3SmF](./runs.md#limsirun3smf) | [LIMSIrun4Syn](./runs.md#limsirun4syn) | [LIMSIrun5MPF](./runs.md#limsirun5mpf) | [LIMSIrun6Wik](./runs.md#limsirun6wik)

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

- :fontawesome-solid-user-group: **Participant:** [DUTH](./participants.md#duth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/DUTH-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/DUTH-CL.pdf)
- :material-file-search: **Runs:** [DuthStef](./runs.md#duthstef) | [DuthMmMt16s](./runs.md#duthmmmt16s) | [DuthMmMt16f](./runs.md#duthmmmt16f) | [DuthBaseF](./runs.md#duthbasef) | [DuthBaseS](./runs.md#duthbases) | [DuthMmMtB16f](./runs.md#duthmmmtb16f)

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

- :fontawesome-solid-user-group: **Participant:** [FORTH_ICS_ISL](./participants.md#forth_ics_isl)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/FORTH_ICS_ISL-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/FORTH_ICS_ISL-CL.pdf)
- :material-file-search: **Runs:** [FORTHICSd0](./runs.md#forthicsd0) | [FORTHICSd2](./runs.md#forthicsd2) | [FORTHICSs0](./runs.md#forthicss0) | [FORTHICSd0e7](./runs.md#forthicsd0e7) | [FORTHICSdQE](./runs.md#forthicsdqe) | [FORTHICSdQER](./runs.md#forthicsdqer)

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

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-CL.pdf)
- :material-file-search: **Runs:** [UWCSolrBM25](./runs.md#uwcsolrbm25) | [UWCPL2](./runs.md#uwcpl2) | [UWCSolrTerr](./runs.md#uwcsolrterr)

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

- :fontawesome-solid-user-group: **Participant:** [SIBtex](./participants.md#sibtex)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/SIBtex-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/SIBtex-CL.pdf)
- :material-file-search: **Runs:** [SIBTEX2CITIN](./runs.md#sibtex2citin) | [SIBTEX3CTOUT](./runs.md#sibtex3ctout) | [SIBTEX5COMBO](./runs.md#sibtex5combo)

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

- :fontawesome-solid-user-group: **Participant:** [prna](./participants.md#prna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/prna-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/prna-CL.pdf)
- :material-file-search: **Runs:** [prna1](./runs.md#prna1) | [prna2](./runs.md#prna2) | [prna3](./runs.md#prna3) | [prnaB1](./runs.md#prnab1) | [prnaB2](./runs.md#prnab2) | [prnaB3](./runs.md#prnab3)

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

- :fontawesome-solid-user-group: **Participant:** [ECNU](./participants.md#ecnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/ECNU-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/ECNU-CL.pdf)
- :material-file-search: **Runs:** [ECNUPB](./runs.md#ecnupb) | [ecnu1](./runs.md#ecnu1) | [ecnu2](./runs.md#ecnu2) | [ECNUBP](./runs.md#ecnubp) | [ecnu3](./runs.md#ecnu3) | [ecnu4](./runs.md#ecnu4)

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

- :fontawesome-solid-user-group: **Participant:** [Foreseer](./participants.md#foreseer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Foreseer-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/Foreseer-CL.pdf)
- :material-file-search: **Runs:** [FusionAuto](./runs.md#fusionauto) | [FusionManual](./runs.md#fusionmanual) | [FusionMAll](./runs.md#fusionmall) | [FusionAutoB](./runs.md#fusionautob) | [FusionManB](./runs.md#fusionmanb) | [FusionAdv](./runs.md#fusionadv)

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

- :fontawesome-solid-user-group: **Participant:** [SCIAITeam](./participants.md#sciaiteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Siena_SUCCESS-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/Siena_SUCCESS-CL.pdf)
- :material-file-search: **Runs:** [SCIAILuceneA](./runs.md#sciailucenea) | [RRFFused](./runs.md#rrffused) | [FrameAFinal](./runs.md#frameafinal) | [SCIAILuceneB](./runs.md#sciailuceneb) | [RRFfused](./runs.md#rrffused)

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

- :fontawesome-solid-user-group: **Participant:** [HITSJ](./participants.md#hitsj)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/HITSJ-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/HITSJ-CL.pdf)
- :material-file-search: **Runs:** [artificial](./runs.md#artificial) | [runindri](./runs.md#runindri) | [runindriML](./runs.md#runindriml) | [runindriB](./runs.md#runindrib) | [artificialB](./runs.md#artificialb) | [runnetwork](./runs.md#runnetwork)

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

- :fontawesome-solid-user-group: **Participant:** [cbnu](./participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/cbnu-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/cbnu-CL.pdf)
- :material-file-search: **Runs:** [cbnu0](./runs.md#cbnu0) | [cbnu1](./runs.md#cbnu1) | [cbnu2](./runs.md#cbnu2) | [cbnu3](./runs.md#cbnu3) | [cbnu4](./runs.md#cbnu4) | [cbnu5](./runs.md#cbnu5)

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

- :fontawesome-solid-user-group: **Participant:** [GRIUM](./participants.md#grium)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/GRIUM-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/GRIUM-CL.pdf)
- :material-file-search: **Runs:** [GRIUMenRun1](./runs.md#griumenrun1) | [GRIUMenRun2](./runs.md#griumenrun2)

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

- :fontawesome-solid-user-group: **Participant:** [hltcoe](./participants.md#hltcoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/hltcoe-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/hltcoe-CL.pdf)
- :material-file-search: **Runs:** [hltcoe5srf](./runs.md#hltcoe5srf) | [hltcoe4srf](./runs.md#hltcoe4srf) | [hltcoewsrf](./runs.md#hltcoewsrf) | [hltcoe5sdrf](./runs.md#hltcoe5sdrf) | [hltcoe4sdrf](./runs.md#hltcoe4sdrf) | [hltcoewsdrf](./runs.md#hltcoewsdrf)

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

- :fontawesome-solid-user-group: **Participant:** [NovaSearch](./participants.md#novasearch)
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

- :fontawesome-solid-user-group: **Participant:** [UWM_UO](./participants.md#uwm_uo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/UWM_UO-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/UWM_UO-CL.pdf)
- :material-file-search: **Runs:** [UWMUO1](./runs.md#uwmuo1) | [UWMUO2](./runs.md#uwmuo2) | [UWMUO3](./runs.md#uwmuo3) | [UWMUO4](./runs.md#uwmuo4) | [UWMUO5](./runs.md#uwmuo5) | [UWMUO6](./runs.md#uwmuo6)

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

- :fontawesome-solid-user-group: **Participant:** [DBNET_AUEB](./participants.md#dbnet_aueb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/DBNET_AUEB-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/DBNET_AUEB-CL.pdf)
- :material-file-search: **Runs:** [run1](./runs.md#run1) | [run2](./runs.md#run2) | [AUEBrun1B](./runs.md#auebrun1b) | [AUEBrun2B](./runs.md#auebrun2b)

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

- :fontawesome-solid-user-group: **Participant:** [TUW](./participants.md#tuw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/TUW-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/TUW-CL.pdf)
- :material-file-search: **Runs:** [TUW1](./runs.md#tuw1) | [TUW2](./runs.md#tuw2) | [TUW3](./runs.md#tuw3) | [TUW4](./runs.md#tuw4) | [TUW5](./runs.md#tuw5) | [TUW6](./runs.md#tuw6)

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

- :fontawesome-solid-user-group: **Participant:** [NU_UU_UNC](./participants.md#nu_uu_unc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/NU_UU_UNC-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/NU_UU_UNC-CL.pdf)
- :material-file-search: **Runs:** [nuuuuncDFML](./runs.md#nuuuuncdfml) | [nuuuuncMDRUN](./runs.md#nuuuuncmdrun) | [nuuuuncHAKT](./runs.md#nuuuunchakt) | [nuuuuncHMKTB](./runs.md#nuuuunchmktb) | [nuuuuncMDRUB](./runs.md#nuuuuncmdrub) | [nuuuuncDFMLB](./runs.md#nuuuuncdfmlb)

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

- :fontawesome-solid-user-group: **Participant:** [FDUDMIIP](./participants.md#fdudmiip)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/FDUDMIIP-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/FDUDMIIP-CL.pdf)
- :material-file-search: **Runs:** [FDUAuto1](./runs.md#fduauto1) | [FDUAuto2](./runs.md#fduauto2) | [FDUManual](./runs.md#fdumanual) | [FDUAuto](./runs.md#fduauto) | [FDUManual1](./runs.md#fdumanual1) | [FDUManual2](./runs.md#fdumanual2)

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

- :fontawesome-solid-user-group: **Participant:** [CBIA_VT](./participants.md#cbia_vt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/CBIA_VT-CL.pdf](http://trec.nist.gov/pubs/trec24/papers/CBIA_VT-CL.pdf)
- :material-file-search: **Runs:** [QFB](./runs.md#qfb) | [UMLS](./runs.md#umls) | [PPR](./runs.md#ppr) | [QFBdiag](./runs.md#qfbdiag) | [UMLSdiag](./runs.md#umlsdiag) | [PPRdiag](./runs.md#pprdiag)

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

