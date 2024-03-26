# Proceedings - Knowledge Base Acceleration 2013 

#### Evaluating Stream Filtering for Entity Profile Updates for TREC  2013

_John R. Frank, Steven J. Bauer, Max Kleiman-Weiner, Daniel A. Roberts, Nilesh Tripuraneni, Ce Zhang, Christopher Ré, Ellen M. Voorhees, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/KBA.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/KBA.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Knowledge Base Acceleration (KBA) track in TREC 2013 expanded the entity-centric filtering evaluation from TREC KBA 2012. This track evaluates systems that filter a time-ordered corpus for documents and slot fills that would change an entity profile in a predefined list of entities. We doubled the size of the KBA streamcorpus to twelve thousand contiguous hours and a billion documents from blogs, news, and Web content. We quadrupled the number of entities as query topics from structured knowledge bases (KB), such as Wikipedia and Twitter. We also added a second task component: identifying entity slot values that change over the course of the stream. This Streaming Slot Filling (SSF) subtask focuses on natural language understanding and is a step toward decomposing the profile update process undertaken by humans maintaining a knowledge base. A successful KBA system must do more than resolve the meaning of entity mentions by linking documents to the KB: it must also distinguish vitally relevant documents and new slot fills that would change a target entity's profile. This combines thinking from natural language processing (NLP) and information retrieval (IR). Filtering tracks in TREC have typically used queries based on topics described by a set of keyword queries or short descriptions, and annotators have generated relevance judgments based on their personal interpretation of the topic. For TREC 2013, we selected a set of filter topics based on Wikipedia and Twitter entities: 98 people, 19 organizations, and 24 facilities. Assessors judged ~50k documents, which included all documents that mention a name from a handcrafted list of surface form names of the 141 target entities. Judgments for documents from before February 2012 were provided to TREC teams as training data, and the remaining 12 months of data was used to measure the F_1 accuracy and scaled utility of these systems. We present peak macro-averaged F_1 scores for all run submissions. High scoring systems used a variety of approaches, including simple name matching, names of related entities from the knowledge base, and various types of classifiers. Top scoring systems achieved F_1 scores in the mid-30s. We present results for an oracle baseline system that scores in the low-30s. We discuss key lessons learned at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FrankBKRTZRVS13.bib) "
	```
	@inproceedings{DBLP:conf/trec/FrankBKRTZRVS13,
		author = {John R. Frank and Steven J. Bauer and Max Kleiman{-}Weiner and Daniel A. Roberts and Nilesh Tripuraneni and Ce Zhang and Christopher R{\'{e}} and Ellen M. Voorhees and Ian Soboroff},
		editor = {Ellen M. Voorhees},
		title = {Evaluating Stream Filtering for Entity Profile Updates for {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/KBA.OVERVIEW.pdf},
		timestamp = {Tue, 12 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FrankBKRTZRVS13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Knowledge Base Acceleration 2013: Cumulative Citation  Recommendation Task

_Rafik Abbes, Karen Pinel-Sauvagnat, Nathalie Hernandez, Mohand Boughanem_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/IRIT-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/IRIT-kba.pdf)
- :material-file-search: **Runs:** [IRIT-sig_irit_1](./runs.md#irit-sig_irit_1) | [IRIT-sig_irit_2](./runs.md#irit-sig_irit_2) | [IRIT-sig_irit_3](./runs.md#irit-sig_irit_3)

??? abstract "Abstract"
	
	This paper describes the IRIT lab participation to the Cumulative Citation Recommendation task of the TREC 2013 Knowledge Base Acceleration Track. In this task, we are asked to implement a system which aims to detect “Vital” documents that a human would want to cite when updating the Wikipedia article for the target entity. Our approach is built on two steps. First, for each topic (entity), we retrieve a set of potential relevant documents containing at least one entity mention. These documents are then classified using a supervised learning algorithm to identify which ones are vital. We submitted three runs using different combinations of features. Obtained results are presented and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbbesPHB13.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbbesPHB13,
		author = {Rafik Abbes and Karen Pinel{-}Sauvagnat and Nathalie Hernandez and Mohand Boughanem},
		editor = {Ellen M. Voorhees},
		title = {{IRIT} at {TREC} Knowledge Base Acceleration 2013: Cumulative Citation Recommendation Task},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/IRIT-kba.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbbesPHB13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filtering Entity Centric Documents using Numerics and Temporals features  within RF Classifier

_Vincent Bouvier, Patrice Bellot_

- :fontawesome-solid-user-group: **Participant:** [LSIS_LIA](./participants.md#lsis_lia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/LSIS_LIA-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/LSIS_LIA-kba.pdf)
- :material-file-search: **Runs:** [LSIS_LIA-no_update_S4](./runs.md#lsis_lia-no_update_s4) | [LSIS_LIA-no_update_S4_2](./runs.md#lsis_lia-no_update_s4_2) | [LSIS_LIA-no_update_S4_3](./runs.md#lsis_lia-no_update_s4_3) | [LSIS_LIA-upd_document_S4](./runs.md#lsis_lia-upd_document_s4) | [LSIS_LIA-upd_doc_S4_2](./runs.md#lsis_lia-upd_doc_s4_2) | [LSIS_LIA-upd_doc_S4_3](./runs.md#lsis_lia-upd_doc_s4_3) | [LSIS_LIA-upd_snippet_S4](./runs.md#lsis_lia-upd_snippet_s4) | [LSIS_LIA-upd_snpt_S4_2](./runs.md#lsis_lia-upd_snpt_s4_2) | [LSIS_LIA-upd_snpt_S4_3](./runs.md#lsis_lia-upd_snpt_s4_3)

??? abstract "Abstract"
	
	This article introduces the system designed to work for the Knowledge Base Acceleration (KBA) track at Text REtrieval Conference (TREC). This is the second time this track is run with yet this year there is even more challenge. KBA is focused on keeping up to date knowledge bases (KB) such as Wikipedia1 (WP) where each KB node is considered as an entity (WP page for wikipedia example). It has been shown in (Frank et al., 2012) that the time lag between the publication date of cited news articles and the date of an edit to wikipedia article creating the citation can be really big (median 356 days) for non-popular entities. KBA is to give a chance to non-popular entities information to be updated as soon as a useful information is published on the internet. The KBA organizers have built up a stream-corpus which is a huge corpus of timestamped web documents that can be processed chronologically. Hence it is possible to simulate a real time system. The documents come from newswires, blogs, forums, review, memetracker... . In addition, a set of target entities, coming from wikipedia or from twitter, has been selected for their ambiguity or unpopularity. And last but not least, more than 60,000 documents have been annotated so that systems can train on it. The train period starts on documents published from october 2011 until february 2012, and the test period starts from february 2012 to february 2013. The KBA track is divided in two tasks: CCR (Cumulative Citation Recommendation) and SSF (Streaming Slot Filling). CCR task is to filter out documents worth citing in a profile of an entity (e.g., wikipedia or freebase article). SSF task is to detect changes on given slots for each of the target entities. This article is focused only on CCR task. In CCR task, the system is to filter out documents relative to target entities out from the stream-corpus. The system must also be able to give the usefulness of a document ranked using one of those 4 relevance classes: garbage : no information about target entity; neutral : informative but not citable; useful: bio, primary or secondary source useful when creating a profile from scratch; vital : timely info about the entity's current state, actions, or situation. The remaining of this article is organized as follows. The next section give details on how we designed our system. Then the different runs we sent are analyzed to eventually conclude and give a brief outline on perspectives.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BouvierB13.bib) "
	```
	@inproceedings{DBLP:conf/trec/BouvierB13,
		author = {Vincent Bouvier and Patrice Bellot},
		editor = {Ellen M. Voorhees},
		title = {Filtering Entity Centric Documents using Numerics and Temporals features within {RF} Classifier},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/LSIS\_LIA-kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BouvierB13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2013 Knowledge Base Acceleration Track: Bi-directional  Entity Linking and Time-aware Evaluation

_Laura Dietz, Jeffrey Dalton_

- :fontawesome-solid-user-group: **Participant:** [UMass_CIIR](./participants.md#umass_ciir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/umass-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/umass-kba.pdf)
- :material-file-search: **Runs:** [UMass_CIIR-top2LinkedProb](./runs.md#umass_ciir-top2linkedprob) | [UMass_CIIR-t2LinkProb_tw](./runs.md#umass_ciir-t2linkprob_tw) | [UMass_CIIR-T2ELMaxTO_1](./runs.md#umass_ciir-t2elmaxto_1) | [UMass_CIIR-T2ELMax_1](./runs.md#umass_ciir-t2elmax_1) | [UMass_CIIR-T2ELMax_TO](./runs.md#umass_ciir-t2elmax_to) | [UMass_CIIR-T2ELMax](./runs.md#umass_ciir-t2elmax) | [UMass_CIIR-T2ELMax_TO_1_tw](./runs.md#umass_ciir-t2elmax_to_1_tw) | [UMass_CIIR-T2ELMax_1_tw](./runs.md#umass_ciir-t2elmax_1_tw) | [UMass_CIIR-T2ELMax_TO_tw](./runs.md#umass_ciir-t2elmax_to_tw) | [UMass_CIIR-T2ELMax_tw](./runs.md#umass_ciir-t2elmax_tw) | [UMass_CIIR-wrm_trm_r](./runs.md#umass_ciir-wrm_trm_r) | [UMass_CIIR-wrm_trm_s](./runs.md#umass_ciir-wrm_trm_s) | [UMass_CIIR-wrm_tsdm_r](./runs.md#umass_ciir-wrm_tsdm_r) | [UMass_CIIR-wrm_tsdm_s](./runs.md#umass_ciir-wrm_tsdm_s) | [UMass_CIIR-wrn_tsdm_r](./runs.md#umass_ciir-wrn_tsdm_r) | [UMass_CIIR-wrn_tsdm_s](./runs.md#umass_ciir-wrn_tsdm_s) | [UMass_CIIR-wrtn_tsdm_r](./runs.md#umass_ciir-wrtn_tsdm_r) | [UMass_CIIR-wrtn_tsdm_s](./runs.md#umass_ciir-wrtn_tsdm_s) | [UMass_CIIR-wrt_tsdm_r](./runs.md#umass_ciir-wrt_tsdm_r) | [UMass_CIIR-wrt_tsdm_s](./runs.md#umass_ciir-wrt_tsdm_s) | [UMass_CIIR-wsdm_tsdm_r](./runs.md#umass_ciir-wsdm_tsdm_r) | [UMass_CIIR-wrm_tskq_r](./runs.md#umass_ciir-wrm_tskq_r) | [UMass_CIIR-wrm_tskq_s](./runs.md#umass_ciir-wrm_tskq_s) | [UMass_CIIR-wsdm_tsdm_s](./runs.md#umass_ciir-wsdm_tsdm_s) | [UMass_CIIR-wskq_tskq_s](./runs.md#umass_ciir-wskq_tskq_s) | [UMass_CIIR-wskq_tsdm_r](./runs.md#umass_ciir-wskq_tsdm_r) | [UMass_CIIR-wskq_tsdm_s](./runs.md#umass_ciir-wskq_tsdm_s) | [UMass_CIIR-wrtn_tskq_r](./runs.md#umass_ciir-wrtn_tskq_r) | [UMass_CIIR-wrt_tskq_r](./runs.md#umass_ciir-wrt_tskq_r) | [UMass_CIIR-wrtn_tskq_s](./runs.md#umass_ciir-wrtn_tskq_s) | [UMass_CIIR-wrn_tskq_s](./runs.md#umass_ciir-wrn_tskq_s) | [UMass_CIIR-wrt_tskq_s](./runs.md#umass_ciir-wrt_tskq_s) | [UMass_CIIR-wskq_tskq_r](./runs.md#umass_ciir-wskq_tskq_r)

??? abstract "Abstract"
	
	This notebook details the participation of the University of Massachusetts Amherst in the Cumulative Citation Recommendation task (CCR) of the TREC 2013 Knowledge Base Acceleration Track. Our interest in TREC KBA is motived by our research on entity-based query expansion. Query expansion is a information retrieval technique for improving recall by augmenting the original query terms with other terms that are likely to indicate relevant documents. Such expansion terms can be inferred with pseudo-relevance feedback techniques (Lavrenko and Croft, 2001). The resulting retrieval model can be interpreted as a weighted mixture model including the original retrieval model and retrieval models for each expansion term. Instead of expanding the query with terms, our research is on expanding the query with relevant entities from a knowledge base. Such entities are very rich in structure, including name variants, related entities and associated text. An essential component of our entity-based query expansion is to derive a retrieval model for a given knowledge base entity, which can be incorporated into the weighted mixture model. We study the effectiveness of different entity-based retrieval models within the TREC KBA Cumulative Citation Recommendation task. However, we do not address the novelty aspects of the task, and therefore do not distinguish between 'vital' and 'useful' documents. This year we only evaluate memoryless methods, i.e., the prediction is not influenced by predictions on previous time intervals. We segment the stream into week-long intervals which are filtered independently.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DietzD13.bib) "
	```
	@inproceedings{DBLP:conf/trec/DietzD13,
		author = {Laura Dietz and Jeffrey Dalton},
		editor = {Ellen M. Voorhees},
		title = {UMass at {TREC} 2013 Knowledge Base Acceleration Track: Bi-directional Entity Linking and Time-aware Evaluation},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/umass-kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DietzD13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Illinois' Graduate School of Library and Information  Science at TREC 2013

_Miles Efron, Craig Willis, Peter Organisciak, Brian Balsamo, Ana Lucic_

- :fontawesome-solid-user-group: **Participant:** [uiuc](./participants.md#uiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/uiuc-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/uiuc-kba.pdf)

??? abstract "Abstract"
	
	The University of Illinois' Graduate School of Library and Information Science (uiucGSLIS) participated in TREC's knowledge base acceleration (KBA) track in 2013. Specifically, we submitted runs for the cumulative citation recommendation (CCR) task. CCR is a type of document filtering. The use-case is that our user U is an editor of a node T in a knowledge base such as Wikipedia (for example, the entry for blogger Jamie Parsley (http://en.wikipedia.org/wiki/Jamie Parsley). Given an incoming stream of documents D,the system must emit a binary route/not-route decision for each document Di in real time. In this case, the binary decision signals whether we should recommend Di to U as a source of information for editing the entity T's page. In other words, our goal is to monitor D, signaling to U when we find a document that contains “edit-worthy” information regarding the entity T.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EfronWOBLI13.bib) "
	```
	@inproceedings{DBLP:conf/trec/EfronWOBLI13,
		author = {Miles Efron and Craig Willis and Peter Organisciak and Brian Balsamo and Ana Lucic},
		editor = {Ellen M. Voorhees},
		title = {The University of Illinois' Graduate School of Library and Information Science at {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/uiuc-kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EfronWOBLI13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filtering Documents over Time on Evolving Topics - The University  of Amsterdam at TREC 2013 KBA CCR

_Tom Kenter_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/UAmsterdam-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/UAmsterdam-kba.pdf)
- :material-file-search: **Runs:** [UAmsterdam-bsln_5_100_100](./runs.md#uamsterdam-bsln_5_100_100) | [UAmsterdam-uva_kba_run_1](./runs.md#uamsterdam-uva_kba_run_1) | [UAmsterdam-uva_kba_run_2](./runs.md#uamsterdam-uva_kba_run_2) | [UAmsterdam-uva_kba_run_3](./runs.md#uamsterdam-uva_kba_run_3) | [UAmsterdam-uva_kba_run_4](./runs.md#uamsterdam-uva_kba_run_4) | [UAmsterdam-uva_kba_run_5](./runs.md#uamsterdam-uva_kba_run_5) | [UAmsterdam-uva_kba_run_6](./runs.md#uamsterdam-uva_kba_run_6) | [UAmsterdam-uva_kba_run_7](./runs.md#uamsterdam-uva_kba_run_7) | [UAmsterdam-uva_kba_run_8](./runs.md#uamsterdam-uva_kba_run_8) | [UAmsterdam-bl_na_wChis_c1](./runs.md#uamsterdam-bl_na_wchis_c1) | [UAmsterdam-bl_na_wChis_c3](./runs.md#uamsterdam-bl_na_wchis_c3) | [UAmsterdam-bl_na_wConcs_c1](./runs.md#uamsterdam-bl_na_wconcs_c1) | [UAmsterdam-bl_na_wConcs_c3](./runs.md#uamsterdam-bl_na_wconcs_c3) | [UAmsterdam-uva_run_wChi_c1](./runs.md#uamsterdam-uva_run_wchi_c1) | [UAmsterdam-uva_run_wChi_c3](./runs.md#uamsterdam-uva_run_wchi_c3) | [UAmsterdam-uva_run_wCon_c1](./runs.md#uamsterdam-uva_run_wcon_c1) | [UAmsterdam-uva_run_wCon_c3](./runs.md#uamsterdam-uva_run_wcon_c3) | [UAmsterdam-uva_kba_run_9](./runs.md#uamsterdam-uva_kba_run_9) | [UAmsterdam-uva_kba_run_11](./runs.md#uamsterdam-uva_kba_run_11) | [UAmsterdam-uva_kba_run_12](./runs.md#uamsterdam-uva_kba_run_12) | [UAmsterdam-uva_kba_run_14](./runs.md#uamsterdam-uva_kba_run_14) | [UAmsterdam-uva_kba_run_15](./runs.md#uamsterdam-uva_kba_run_15) | [UAmsterdam-uva_kba_run_16](./runs.md#uamsterdam-uva_kba_run_16) | [UAmsterdam-uva_kba_run_10](./runs.md#uamsterdam-uva_kba_run_10) | [UAmsterdam-uva_kba_run_13](./runs.md#uamsterdam-uva_kba_run_13) | [UAmsterdam-uva_kba_run_av](./runs.md#uamsterdam-uva_kba_run_av)

??? abstract "Abstract"
	
	In this paper we describe the University of Amsterdam's approach to the TREC 2013 Knowledge Base Acceleration (KBA) Cumulative Citation Recommendation (CCR) track. The task is to filter a stream of documents for documents relevant to a given set of entities. We model the task as a multi-class classification task. Entities may evolve over time and the classifier should be able to adapt to these changes at runtime. To achieve this, the classifier performs online self-learning, i.e., learning only from the examples it is most confident about, based on a confidence score it produces for every prediction it makes.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Kenter13.bib) "
	```
	@inproceedings{DBLP:conf/trec/Kenter13,
		author = {Tom Kenter},
		editor = {Ellen M. Voorhees},
		title = {Filtering Documents over Time on Evolving Topics - The University of Amsterdam at {TREC} 2013 {KBA} {CCR}},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/UAmsterdam-kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Kenter13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Bootstrapping Knowledge Base Acceleration

_Tushar Khot, Ce Zhang, Jude W. Shavlik, Sriraam Natarajan, Christopher Ré_

- :fontawesome-solid-user-group: **Participant:** [WiscDEFT](./participants.md#wiscdeft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/wisc-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/wisc-kba.pdf)
- :material-file-search: **Runs:** [WiscDEFT-test](./runs.md#wiscdeft-test) | [WiscDEFT-baseline](./runs.md#wiscdeft-baseline) | [WiscDEFT-baseline2](./runs.md#wiscdeft-baseline2) | [WiscDEFT-run1](./runs.md#wiscdeft-run1) | [WiscDEFT-run2](./runs.md#wiscdeft-run2)

??? abstract "Abstract"
	
	The Streaming Slot Filler (SSF) task in TREC Knowledge Base Acceleration track involves detecting changes to slot values (relations) over time. To handle this task, the system needs to extract relations to identify slot-filler values and detect novel values. Being the first attempt at KBA, the biggest challenge that we faced was the scale of the data. We present the approach used by University of Wisconsin for the SSF task and the large scale challenge. We used Elementary, a scalable statistical inference and learning system, developed in University of Wisconsin as our core system. We used Stanford NLP Toolkit to generate parse trees, dependency graphs and named-entity recognition information. These were then converted to features for the logistic regression learner of Elementary. To handle the lack of early SSF training data, we used our existing Knowledge Base Population system to bootstrap a logistic regression model and added rules to handle the new relations
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KhotZSNR13.bib) "
	```
	@inproceedings{DBLP:conf/trec/KhotZSNR13,
		author = {Tushar Khot and Ce Zhang and Jude W. Shavlik and Sriraam Natarajan and Christopher R{\'{e}}},
		editor = {Ellen M. Voorhees},
		title = {Bootstrapping Knowledge Base Acceleration},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/wisc-kba.pdf},
		timestamp = {Tue, 12 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KhotZSNR13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Related Entity based Approach for Knowledge Base Acceleration

_Xitong Liu, Jerry Darko, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/udel_fang-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/udel_fang-kba.pdf)
- :material-file-search: **Runs:** [udel_fang-UDInfoK_Ex](./runs.md#udel_fang-udinfok_ex) | [udel_fang-UDInfoK_Wiki1](./runs.md#udel_fang-udinfok_wiki1) | [udel_fang-UDInfoK_Wiki2](./runs.md#udel_fang-udinfok_wiki2) | [udel_fang-UDInfoK_Weight1](./runs.md#udel_fang-udinfok_weight1) | [udel_fang-UDInfoK_Weight2](./runs.md#udel_fang-udinfok_weight2)

??? abstract "Abstract"
	
	In this paper we present the overview of our work in the TREC 2013 KBA Track. The goal is to find documents which may contribute to the update of knowledge base entries (e.g., Wikipedia or Freebase articles). Two tasks are introduced in this year's track: (1) Cumulative Citation Recommendation (CCR), (2) Streaming Slot Filling (SSF). Particularly, we focus on the CCR task, follow our previous work on TREC 2012 KBA Track [3] and propose an improved approach by incorporating weighting to related entities. Our approach is based on the framework of leveraging related entities for document filtering. In particular, we pool related entities from the profile page (i.e., Wikipedia) of target entity, estimate the weight of each related entities based on the training data, and apply the weighted related entities to estimate the confidence scores of streaming documents. We explore three methods based on different weighting strategies: (1) all related entities get zero weight, which is equivalent to exact matching against the target entity only. (2) all related entities get same weight. (3) related entities are weighted based on training data. Experiments on the KBA Stream Corpus 2013 reveal the effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuDF13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuDF13,
		author = {Xitong Liu and Jerry Darko and Hui Fang},
		editor = {Ellen M. Voorhees},
		title = {A Related Entity based Approach for Knowledge Base Acceleration},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/udel\_fang-kba.pdf},
		timestamp = {Sun, 26 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuDF13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Pattern Matching Approach to Streaming Slot Filling

_Hung Nguyen, Yi Fang, Sandhya Gade, Vijay Mysore, Juan Hu, Sabita Pandit, Aparna Srinivasan, Miao Jiang_

- :fontawesome-solid-user-group: **Participant:** [SCU](./participants.md#scu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/SCU-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/SCU-kba.pdf)
- :material-file-search: **Runs:** [SCU-ssf_1](./runs.md#scu-ssf_1) | [SCU-ssf_2](./runs.md#scu-ssf_2) | [SCU-ssf_3](./runs.md#scu-ssf_3) | [SCU-ssf_4](./runs.md#scu-ssf_4) | [SCU-ssf_5](./runs.md#scu-ssf_5)

??? abstract "Abstract"
	
	In this paper, we described our system for Knowledge Base Acceleration (KBA) Track at TREC 2013. The KBA Track has two tasks, CCR and SSF. Our approach consists of two major steps: selecting documents and extracting slot values. Selecting documents is to look for and save the documents that mention the entities of interest. The second step involves with generating seed patterns to extract the slot values and computing confidence score.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NguyenFGMHPSJ13.bib) "
	```
	@inproceedings{DBLP:conf/trec/NguyenFGMHPSJ13,
		author = {Hung Nguyen and Yi Fang and Sandhya Gade and Vijay Mysore and Juan Hu and Sabita Pandit and Aparna Srinivasan and Miao Jiang},
		editor = {Ellen M. Voorhees},
		title = {A Pattern Matching Approach to Streaming Slot Filling},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/SCU-kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NguyenFGMHPSJ13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Florida Knowledge Base Acceleration

_Morteza Shahriari Nia, Christan Earl Grant, Yang Peng, Daisy Zhe Wang, Milenko Petrovic_

- :fontawesome-solid-user-group: **Participant:** [gatordsr](./participants.md#gatordsr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/gator-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/gator-kba.pdf)
- :material-file-search: **Runs:** [gatordsr-gatordsr_new](./runs.md#gatordsr-gatordsr_new) | [gatordsr-gatordsr_final](./runs.md#gatordsr-gatordsr_final) | [gatordsr-gatordsr_infer](./runs.md#gatordsr-gatordsr_infer)

??? abstract "Abstract"
	
	In this paper we will present the system design and algorithm adopted by the GatorDSR team, University of Florida to efficiently process TREC KBA 2013 — SSF track. Here we will describe the system as well as the details the algorithms used to extract slot values for the given slot name. Scalability, efficiency, precision and recall are the major goals of this work, given the overly limited time limitation and available computational resources.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NiaGPWP13.bib) "
	```
	@inproceedings{DBLP:conf/trec/NiaGPWP13,
		author = {Morteza Shahriari Nia and Christan Earl Grant and Yang Peng and Daisy Zhe Wang and Milenko Petrovic},
		editor = {Ellen M. Voorhees},
		title = {University of Florida Knowledge Base Acceleration},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/gator-kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NiaGPWP13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BIT and MSRA at TREC KBA CCR Track 2013

_Jingang Wang, Dandan Song, Lejian Liao, Chin-Yew Lin_

- :fontawesome-solid-user-group: **Participant:** [BIT](./participants.md#bit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/BIT-MSRA-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/BIT-MSRA-kba.pdf)
- :material-file-search: **Runs:** [BIT-ECQ](./runs.md#bit-ecq) | [BIT-RFRankUniModel](./runs.md#bit-rfrankunimodel) | [BIT-RFClassLoose](./runs.md#bit-rfclassloose) | [BIT-RFClassStrict](./runs.md#bit-rfclassstrict) | [BIT-ECQUpdate](./runs.md#bit-ecqupdate) | [BIT-RFBurst](./runs.md#bit-rfburst) | [BIT-RFMultiModel](./runs.md#bit-rfmultimodel) | [BIT-RFMultiModel_1](./runs.md#bit-rfmultimodel_1) | [BIT-RFBurst_1](./runs.md#bit-rfburst_1) | [BIT-RFDiffModel](./runs.md#bit-rfdiffmodel)

??? abstract "Abstract"
	
	Our strategy for TREC KBA CCR track is to first retrieve as many vital or documents as possible and then apply more sophisticated classification and ranking methods to differentiate vital from useful documents. We submitted 10 runs generated by 3 approaches: question expansion, classification and learning to rank. Query expansion is an unsupervised baseline, in which we combine entities' names and their related entities' names as phrase queries to retrieve relevant documents. This baseline outperforms the overall median and mean submissions. The system performance is further improved by supervised classification and learning to rank methods. We mainly exploit three kinds of external resources to construct the features in supervised learning: (i) entry pages of Wikipedia entities or profile pages of Twitter entities, (ii) existing citations in the Wikipedia page of an entity, and (iii) burst of Wikipedia page views of an entity. In vital + useful task, one of our ranking-based methods achieves the best result among all participants. In vital only task, one of our classification-based methods achieve the overall best result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangSLL13.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangSLL13,
		author = {Jingang Wang and Dandan Song and Lejian Liao and Chin{-}Yew Lin},
		editor = {Ellen M. Voorhees},
		title = {{BIT} and {MSRA} at {TREC} {KBA} {CCR} Track 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/BIT-MSRA-kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangSLL13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC2013 Knowledge Base Acceleration Track

_Chunyun Zhang, Weiran Xu, Ruifang Liu, Weitai Zhang, Dai Zhang, Janshu Ji, Jing Yang_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/PRIS-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/PRIS-kba.pdf)
- :material-file-search: **Runs:** [PRIS-pris0](./runs.md#pris-pris0) | [PRIS-pris2](./runs.md#pris-pris2) | [PRIS-pris1](./runs.md#pris-pris1) | [PRIS-pris3](./runs.md#pris-pris3) | [PRIS-pris_ssf_0](./runs.md#pris-pris_ssf_0) | [PRIS-pris_ssf_1](./runs.md#pris-pris_ssf_1) | [PRIS-pris_ssf_2](./runs.md#pris-pris_ssf_2) | [PRIS-pris_expansion](./runs.md#pris-pris_expansion) | [PRIS-pris_baseline](./runs.md#pris-pris_baseline) | [PRIS-pris_similarity](./runs.md#pris-pris_similarity) | [PRIS-pris_keywords](./runs.md#pris-pris_keywords) | [PRIS-pris_merge](./runs.md#pris-pris_merge) | [PRIS-pris_svd](./runs.md#pris-pris_svd) | [PRIS-pris_ssf_fst](./runs.md#pris-pris_ssf_fst) | [PRIS-pris_ssf_second](./runs.md#pris-pris_ssf_second)

??? abstract "Abstract"
	
	This paper details the participation of Pattern Recognition and Intelligent System lab of BUPT in CCR and SSF task of TREC 2013 Knowledge Base Acceleration track. In the CCR task, The PRIS system focuses attention on query expansion and similarity calculation. The system uses DBpedia as external source data to do query expansion and generates directional documents to calculate similarities with candidate worth citing documents. In the SSF task, The PRIS system utilizes a pattern learning method to do relation extraction and slot filling. Patterns of regular slots which are same to TAC-KBP slots are learned from KBP Slot Filling corpus. Other slots are filled by following some generalized patterns learned from external source data including homepages of some famous people and facilities. Experiments show that the CCR system gives a good performance above the median value. The pattern learning method for SSF task gives an outstanding performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangXLZZJY13.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangXLZZJY13,
		author = {Chunyun Zhang and Weiran Xu and Ruifang Liu and Weitai Zhang and Dai Zhang and Janshu Ji and Jing Yang},
		editor = {Ellen M. Voorhees},
		title = {{PRIS} at {TREC2013} Knowledge Base Acceleration Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/PRIS-kba.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangXLZZJY13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI and TU Delft Notebook TREC 2013: Contextual Suggestion,  Federated Web Search, KBA, and Web Tracks

_Alejandro Bellogín, Gebrekirstos G. Gebremeskel, Jiyin He, Alan Said, Thaer Samar, Arjen P. de Vries, Jimmy Lin, Jeroen B. P. Vuurens_

- :fontawesome-solid-user-group: **Participant:** [CWI](./participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf](http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf)
- :material-file-search: **Runs:** [CWI-J48_1213_13](./runs.md#cwi-j48_1213_13) | [CWI-RM_FPN_1213_13](./runs.md#cwi-rm_fpn_1213_13) | [CWI-RM_MB_1213_13](./runs.md#cwi-rm_mb_1213_13) | [CWI-RM_all_1213_13](./runs.md#cwi-rm_all_1213_13) | [CWI-RM_all_12_13](./runs.md#cwi-rm_all_12_13) | [CWI-J48_12_13](./runs.md#cwi-j48_12_13) | [CWI-RM_FPN_12_13](./runs.md#cwi-rm_fpn_12_13) | [CWI-RM_MB_12_13](./runs.md#cwi-rm_mb_12_13) | [CWI-J48_13_13](./runs.md#cwi-j48_13_13) | [CWI-RM_all_13_13](./runs.md#cwi-rm_all_13_13) | [CWI-RM_FPN_13_13](./runs.md#cwi-rm_fpn_13_13) | [CWI-RM_MB_13_13](./runs.md#cwi-rm_mb_13_13)

??? abstract "Abstract"
	
	This paper provides an overview of the work done at the Centrum Wiskunde & Informatica (CWI) and Delft University of Technology (TU Delft) for different tracks of TREC 2013. We participated in the Contextual Suggestion Track, the Federated Web Search Track, the Knowledge Base Acceleration (KBA) Track, and the Web Ad-hoc Track. In the Contextual Suggestion track, we focused on filtering the entire ClueWeb12 collection to generate recommendations according to the provided user profiles and contexts. For the Federated Web Search track, we exploited both categories from ODP and document relevance to merge result lists. In the KBA track, we focused on the Cumulative Citation Recommendation task where we exploited different features to two classification algorithms. For the Web track, we extended an ad-hoc baseline with a proximity model that promotes documents in which the query terms are positioned closer together.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelloginGHSSVLV13.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelloginGHSSVLV13,
		author = {Alejandro Bellog{\'{\i}}n and Gebrekirstos G. Gebremeskel and Jiyin He and Alan Said and Thaer Samar and Arjen P. de Vries and Jimmy Lin and Jeroen B. P. Vuurens},
		editor = {Ellen M. Voorhees},
		title = {{CWI} and {TU} Delft Notebook {TREC} 2013: Contextual Suggestion, Federated Web Search, KBA, and Web Tracks},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BelloginGHSSVLV13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

