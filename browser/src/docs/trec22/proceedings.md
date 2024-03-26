# Proceedings 2013 

## Knowledge Base Acceleration 

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

- :fontawesome-solid-user-group: **Participant:** [IRIT](./kba/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/IRIT-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/IRIT-kba.pdf)
- :material-file-search: **Runs:** [IRIT-sig_irit_1](./kba/runs.md#irit-sig_irit_1) | [IRIT-sig_irit_2](./kba/runs.md#irit-sig_irit_2) | [IRIT-sig_irit_3](./kba/runs.md#irit-sig_irit_3)

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

- :fontawesome-solid-user-group: **Participant:** [LSIS_LIA](./kba/participants.md#lsis_lia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/LSIS_LIA-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/LSIS_LIA-kba.pdf)
- :material-file-search: **Runs:** [LSIS_LIA-no_update_S4](./kba/runs.md#lsis_lia-no_update_s4) | [LSIS_LIA-no_update_S4_2](./kba/runs.md#lsis_lia-no_update_s4_2) | [LSIS_LIA-no_update_S4_3](./kba/runs.md#lsis_lia-no_update_s4_3) | [LSIS_LIA-upd_document_S4](./kba/runs.md#lsis_lia-upd_document_s4) | [LSIS_LIA-upd_doc_S4_2](./kba/runs.md#lsis_lia-upd_doc_s4_2) | [LSIS_LIA-upd_doc_S4_3](./kba/runs.md#lsis_lia-upd_doc_s4_3) | [LSIS_LIA-upd_snippet_S4](./kba/runs.md#lsis_lia-upd_snippet_s4) | [LSIS_LIA-upd_snpt_S4_2](./kba/runs.md#lsis_lia-upd_snpt_s4_2) | [LSIS_LIA-upd_snpt_S4_3](./kba/runs.md#lsis_lia-upd_snpt_s4_3)

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

- :fontawesome-solid-user-group: **Participant:** [UMass_CIIR](./kba/participants.md#umass_ciir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/umass-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/umass-kba.pdf)
- :material-file-search: **Runs:** [UMass_CIIR-top2LinkedProb](./kba/runs.md#umass_ciir-top2linkedprob) | [UMass_CIIR-t2LinkProb_tw](./kba/runs.md#umass_ciir-t2linkprob_tw) | [UMass_CIIR-T2ELMaxTO_1](./kba/runs.md#umass_ciir-t2elmaxto_1) | [UMass_CIIR-T2ELMax_1](./kba/runs.md#umass_ciir-t2elmax_1) | [UMass_CIIR-T2ELMax_TO](./kba/runs.md#umass_ciir-t2elmax_to) | [UMass_CIIR-T2ELMax](./kba/runs.md#umass_ciir-t2elmax) | [UMass_CIIR-T2ELMax_TO_1_tw](./kba/runs.md#umass_ciir-t2elmax_to_1_tw) | [UMass_CIIR-T2ELMax_1_tw](./kba/runs.md#umass_ciir-t2elmax_1_tw) | [UMass_CIIR-T2ELMax_TO_tw](./kba/runs.md#umass_ciir-t2elmax_to_tw) | [UMass_CIIR-T2ELMax_tw](./kba/runs.md#umass_ciir-t2elmax_tw) | [UMass_CIIR-wrm_trm_r](./kba/runs.md#umass_ciir-wrm_trm_r) | [UMass_CIIR-wrm_trm_s](./kba/runs.md#umass_ciir-wrm_trm_s) | [UMass_CIIR-wrm_tsdm_r](./kba/runs.md#umass_ciir-wrm_tsdm_r) | [UMass_CIIR-wrm_tsdm_s](./kba/runs.md#umass_ciir-wrm_tsdm_s) | [UMass_CIIR-wrn_tsdm_r](./kba/runs.md#umass_ciir-wrn_tsdm_r) | [UMass_CIIR-wrn_tsdm_s](./kba/runs.md#umass_ciir-wrn_tsdm_s) | [UMass_CIIR-wrtn_tsdm_r](./kba/runs.md#umass_ciir-wrtn_tsdm_r) | [UMass_CIIR-wrtn_tsdm_s](./kba/runs.md#umass_ciir-wrtn_tsdm_s) | [UMass_CIIR-wrt_tsdm_r](./kba/runs.md#umass_ciir-wrt_tsdm_r) | [UMass_CIIR-wrt_tsdm_s](./kba/runs.md#umass_ciir-wrt_tsdm_s) | [UMass_CIIR-wsdm_tsdm_r](./kba/runs.md#umass_ciir-wsdm_tsdm_r) | [UMass_CIIR-wrm_tskq_r](./kba/runs.md#umass_ciir-wrm_tskq_r) | [UMass_CIIR-wrm_tskq_s](./kba/runs.md#umass_ciir-wrm_tskq_s) | [UMass_CIIR-wsdm_tsdm_s](./kba/runs.md#umass_ciir-wsdm_tsdm_s) | [UMass_CIIR-wskq_tskq_s](./kba/runs.md#umass_ciir-wskq_tskq_s) | [UMass_CIIR-wskq_tsdm_r](./kba/runs.md#umass_ciir-wskq_tsdm_r) | [UMass_CIIR-wskq_tsdm_s](./kba/runs.md#umass_ciir-wskq_tsdm_s) | [UMass_CIIR-wrtn_tskq_r](./kba/runs.md#umass_ciir-wrtn_tskq_r) | [UMass_CIIR-wrt_tskq_r](./kba/runs.md#umass_ciir-wrt_tskq_r) | [UMass_CIIR-wrtn_tskq_s](./kba/runs.md#umass_ciir-wrtn_tskq_s) | [UMass_CIIR-wrn_tskq_s](./kba/runs.md#umass_ciir-wrn_tskq_s) | [UMass_CIIR-wrt_tskq_s](./kba/runs.md#umass_ciir-wrt_tskq_s) | [UMass_CIIR-wskq_tskq_r](./kba/runs.md#umass_ciir-wskq_tskq_r)

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

- :fontawesome-solid-user-group: **Participant:** [uiuc](./kba/participants.md#uiuc)
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

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./kba/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/UAmsterdam-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/UAmsterdam-kba.pdf)
- :material-file-search: **Runs:** [UAmsterdam-bsln_5_100_100](./kba/runs.md#uamsterdam-bsln_5_100_100) | [UAmsterdam-uva_kba_run_1](./kba/runs.md#uamsterdam-uva_kba_run_1) | [UAmsterdam-uva_kba_run_2](./kba/runs.md#uamsterdam-uva_kba_run_2) | [UAmsterdam-uva_kba_run_3](./kba/runs.md#uamsterdam-uva_kba_run_3) | [UAmsterdam-uva_kba_run_4](./kba/runs.md#uamsterdam-uva_kba_run_4) | [UAmsterdam-uva_kba_run_5](./kba/runs.md#uamsterdam-uva_kba_run_5) | [UAmsterdam-uva_kba_run_6](./kba/runs.md#uamsterdam-uva_kba_run_6) | [UAmsterdam-uva_kba_run_7](./kba/runs.md#uamsterdam-uva_kba_run_7) | [UAmsterdam-uva_kba_run_8](./kba/runs.md#uamsterdam-uva_kba_run_8) | [UAmsterdam-bl_na_wChis_c1](./kba/runs.md#uamsterdam-bl_na_wchis_c1) | [UAmsterdam-bl_na_wChis_c3](./kba/runs.md#uamsterdam-bl_na_wchis_c3) | [UAmsterdam-bl_na_wConcs_c1](./kba/runs.md#uamsterdam-bl_na_wconcs_c1) | [UAmsterdam-bl_na_wConcs_c3](./kba/runs.md#uamsterdam-bl_na_wconcs_c3) | [UAmsterdam-uva_run_wChi_c1](./kba/runs.md#uamsterdam-uva_run_wchi_c1) | [UAmsterdam-uva_run_wChi_c3](./kba/runs.md#uamsterdam-uva_run_wchi_c3) | [UAmsterdam-uva_run_wCon_c1](./kba/runs.md#uamsterdam-uva_run_wcon_c1) | [UAmsterdam-uva_run_wCon_c3](./kba/runs.md#uamsterdam-uva_run_wcon_c3) | [UAmsterdam-uva_kba_run_9](./kba/runs.md#uamsterdam-uva_kba_run_9) | [UAmsterdam-uva_kba_run_11](./kba/runs.md#uamsterdam-uva_kba_run_11) | [UAmsterdam-uva_kba_run_12](./kba/runs.md#uamsterdam-uva_kba_run_12) | [UAmsterdam-uva_kba_run_14](./kba/runs.md#uamsterdam-uva_kba_run_14) | [UAmsterdam-uva_kba_run_15](./kba/runs.md#uamsterdam-uva_kba_run_15) | [UAmsterdam-uva_kba_run_16](./kba/runs.md#uamsterdam-uva_kba_run_16) | [UAmsterdam-uva_kba_run_10](./kba/runs.md#uamsterdam-uva_kba_run_10) | [UAmsterdam-uva_kba_run_13](./kba/runs.md#uamsterdam-uva_kba_run_13) | [UAmsterdam-uva_kba_run_av](./kba/runs.md#uamsterdam-uva_kba_run_av)

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

- :fontawesome-solid-user-group: **Participant:** [WiscDEFT](./kba/participants.md#wiscdeft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/wisc-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/wisc-kba.pdf)
- :material-file-search: **Runs:** [WiscDEFT-test](./kba/runs.md#wiscdeft-test) | [WiscDEFT-baseline](./kba/runs.md#wiscdeft-baseline) | [WiscDEFT-baseline2](./kba/runs.md#wiscdeft-baseline2) | [WiscDEFT-run1](./kba/runs.md#wiscdeft-run1) | [WiscDEFT-run2](./kba/runs.md#wiscdeft-run2)

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

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./kba/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/udel_fang-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/udel_fang-kba.pdf)
- :material-file-search: **Runs:** [udel_fang-UDInfoK_Ex](./kba/runs.md#udel_fang-udinfok_ex) | [udel_fang-UDInfoK_Wiki1](./kba/runs.md#udel_fang-udinfok_wiki1) | [udel_fang-UDInfoK_Wiki2](./kba/runs.md#udel_fang-udinfok_wiki2) | [udel_fang-UDInfoK_Weight1](./kba/runs.md#udel_fang-udinfok_weight1) | [udel_fang-UDInfoK_Weight2](./kba/runs.md#udel_fang-udinfok_weight2)

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

- :fontawesome-solid-user-group: **Participant:** [SCU](./kba/participants.md#scu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/SCU-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/SCU-kba.pdf)
- :material-file-search: **Runs:** [SCU-ssf_1](./kba/runs.md#scu-ssf_1) | [SCU-ssf_2](./kba/runs.md#scu-ssf_2) | [SCU-ssf_3](./kba/runs.md#scu-ssf_3) | [SCU-ssf_4](./kba/runs.md#scu-ssf_4) | [SCU-ssf_5](./kba/runs.md#scu-ssf_5)

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

- :fontawesome-solid-user-group: **Participant:** [gatordsr](./kba/participants.md#gatordsr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/gator-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/gator-kba.pdf)
- :material-file-search: **Runs:** [gatordsr-gatordsr_new](./kba/runs.md#gatordsr-gatordsr_new) | [gatordsr-gatordsr_final](./kba/runs.md#gatordsr-gatordsr_final) | [gatordsr-gatordsr_infer](./kba/runs.md#gatordsr-gatordsr_infer)

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

- :fontawesome-solid-user-group: **Participant:** [BIT](./kba/participants.md#bit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/BIT-MSRA-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/BIT-MSRA-kba.pdf)
- :material-file-search: **Runs:** [BIT-ECQ](./kba/runs.md#bit-ecq) | [BIT-RFRankUniModel](./kba/runs.md#bit-rfrankunimodel) | [BIT-RFClassLoose](./kba/runs.md#bit-rfclassloose) | [BIT-RFClassStrict](./kba/runs.md#bit-rfclassstrict) | [BIT-ECQUpdate](./kba/runs.md#bit-ecqupdate) | [BIT-RFBurst](./kba/runs.md#bit-rfburst) | [BIT-RFMultiModel](./kba/runs.md#bit-rfmultimodel) | [BIT-RFMultiModel_1](./kba/runs.md#bit-rfmultimodel_1) | [BIT-RFBurst_1](./kba/runs.md#bit-rfburst_1) | [BIT-RFDiffModel](./kba/runs.md#bit-rfdiffmodel)

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

- :fontawesome-solid-user-group: **Participant:** [PRIS](./kba/participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/PRIS-kba.pdf](http://trec.nist.gov/pubs/trec22/papers/PRIS-kba.pdf)
- :material-file-search: **Runs:** [PRIS-pris0](./kba/runs.md#pris-pris0) | [PRIS-pris2](./kba/runs.md#pris-pris2) | [PRIS-pris1](./kba/runs.md#pris-pris1) | [PRIS-pris3](./kba/runs.md#pris-pris3) | [PRIS-pris_ssf_0](./kba/runs.md#pris-pris_ssf_0) | [PRIS-pris_ssf_1](./kba/runs.md#pris-pris_ssf_1) | [PRIS-pris_ssf_2](./kba/runs.md#pris-pris_ssf_2) | [PRIS-pris_expansion](./kba/runs.md#pris-pris_expansion) | [PRIS-pris_baseline](./kba/runs.md#pris-pris_baseline) | [PRIS-pris_similarity](./kba/runs.md#pris-pris_similarity) | [PRIS-pris_keywords](./kba/runs.md#pris-pris_keywords) | [PRIS-pris_merge](./kba/runs.md#pris-pris_merge) | [PRIS-pris_svd](./kba/runs.md#pris-pris_svd) | [PRIS-pris_ssf_fst](./kba/runs.md#pris-pris_ssf_fst) | [PRIS-pris_ssf_second](./kba/runs.md#pris-pris_ssf_second)

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

- :fontawesome-solid-user-group: **Participant:** [CWI](./kba/participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf](http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf)
- :material-file-search: **Runs:** [CWI-J48_1213_13](./kba/runs.md#cwi-j48_1213_13) | [CWI-RM_FPN_1213_13](./kba/runs.md#cwi-rm_fpn_1213_13) | [CWI-RM_MB_1213_13](./kba/runs.md#cwi-rm_mb_1213_13) | [CWI-RM_all_1213_13](./kba/runs.md#cwi-rm_all_1213_13) | [CWI-RM_all_12_13](./kba/runs.md#cwi-rm_all_12_13) | [CWI-J48_12_13](./kba/runs.md#cwi-j48_12_13) | [CWI-RM_FPN_12_13](./kba/runs.md#cwi-rm_fpn_12_13) | [CWI-RM_MB_12_13](./kba/runs.md#cwi-rm_mb_12_13) | [CWI-J48_13_13](./kba/runs.md#cwi-j48_13_13) | [CWI-RM_all_13_13](./kba/runs.md#cwi-rm_all_13_13) | [CWI-RM_FPN_13_13](./kba/runs.md#cwi-rm_fpn_13_13) | [CWI-RM_MB_13_13](./kba/runs.md#cwi-rm_mb_13_13)

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

## Contextual Suggestion 

#### Overview of the TREC 2013 Contextual Suggestion Track

_Adriel Dean-Hall, Charles L. A. Clarke, Nicole Simone, Jaap Kamps, Paul Thomas, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/CONTEXT.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/CONTEXT.OVERVIEW.pdf)
??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Dean-HallCSKTV13.bib) "
	```
	@inproceedings{DBLP:conf/trec/Dean-HallCSKTV13,
		author = {Adriel Dean{-}Hall and Charles L. A. Clarke and Nicole Simone and Jaap Kamps and Paul Thomas and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees},
		title = {Overview of the {TREC} 2013 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/CONTEXT.OVERVIEW.pdf},
		timestamp = {Fri, 24 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Dean-HallCSKTV13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Nearest Neighbor Approach to Contextual Suggestion

_Sandeep Avula, John O'Connor, Jaime Arguello_

- :fontawesome-solid-user-group: **Participant:** [UNC_SILS](./context/participants.md#unc_sils)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/unc-context.pdf](http://trec.nist.gov/pubs/trec22/papers/unc-context.pdf)
- :material-file-search: **Runs:** [uncsils_base](./context/runs.md#uncsils_base) | [uncsils_param](./context/runs.md#uncsils_param)

??? abstract "Abstract"
	
	The School of Information and Library Science at the University of North Carolina at Chapel Hill (UNCSILS) submit ted two runs to the Contextual Suggestion Track. Given a geographical context, both our runs (UNCSILS BASE and UNCSILS PARAM) scored venues from the same candidate set gathered using the Yelp API. Our baseline run (UNCSILS BASE) followed a nearest neighbor approach. For a given profile/context pair, the candidate venues were scored using the weighted average rating associated with the venues in the profile. The weighting was implemented based on the cosine similarity between the candidate venue and the profile venue using TF.IDF term weighting. The goal of this approach was to score each candidate venue based on the rating associated with the most similar venues in the profile. Our experimental run (UNCSILS PARAM) boosted the contribution from the profile venue with the greatest similarity with the candidate venue and rating. The experimental run (UNCSILS PARAM) outperformed the baseline run (UNCSILS BASE) by a small, but statistically significant margin.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AvulaOA13.bib) "
	```
	@inproceedings{DBLP:conf/trec/AvulaOA13,
		author = {Sandeep Avula and John O'Connor and Jaime Arguello},
		editor = {Ellen M. Voorhees},
		title = {A Nearest Neighbor Approach to Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/unc-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AvulaOA13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTH at TREC 2013 Contextual Suggestion Track

_George Drosatos, Giorgos Stamatelatos, Avi Arampatzis, Pavlos S. Efraimidis_

- :fontawesome-solid-user-group: **Participant:** [DuTH](./context/participants.md#duth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/DUTH-context.pdf](http://trec.nist.gov/pubs/trec22/papers/DUTH-context.pdf)
- :material-file-search: **Runs:** [DuTH_A](./context/runs.md#duth_a) | [DuTH_B](./context/runs.md#duth_b)

??? abstract "Abstract"
	
	In this report we give an overview of our participation in the TREC 2013 Contextual Suggestion Track. We present an approach for context processing that comprises a newly designed and fine-tuned POI (Point Of Interest) data collection technique, a crowdsourcing approach to speed up data collection and two radically different approaches for suggestion processing (a k-NN based and a Rocchio-like). In the context processing, we collect POIs from three popular place search engines, Google Places, Foursquare and Yelp. The collected POIs are enriched by adding snippets from the Google and Bing search engines using crowdsourcing techniques. In the suggestion processing, we propose two methods. The first submits each candidate place as a query to an index of a user's rated examples and scores it based on the top-k results. The second method is based on Rocchio's algorithm and uses the rated examples per user profile to generate a personal query which is then submitted to an index of all candidate places. The track evaluation shows that both approaches are working well; especially the Rocchio-like approach is the most promising since it scores almost firmly above the median system and achieves the best system result in almost half of the judged context-profile pairs. In the final TREC system rankings, we are the 2nd best group in MRR and TBG, and 3rd best group in P@5, out of 15 groups in the category we participated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DrosatosSAE13.bib) "
	```
	@inproceedings{DBLP:conf/trec/DrosatosSAE13,
		author = {George Drosatos and Giorgos Stamatelatos and Avi Arampatzis and Pavlos S. Efraimidis},
		editor = {Ellen M. Voorhees},
		title = {{DUTH} at {TREC} 2013 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/DUTH-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DrosatosSAE13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT, GeoComp, and LIUPPA at the TREC 2013 Contextual Suggestion  Track

_Gilles Hubert, Guillaume Cabanac, Karen Pinel-Sauvagnat, Damien Palacio, Christian Sallaberry_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./context/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/IRIT-context.pdf](http://trec.nist.gov/pubs/trec22/papers/IRIT-context.pdf)
- :material-file-search: **Runs:** [IRIT.OpenWeb](./context/runs.md#irit.openweb) | [IRIT.ClueWeb](./context/runs.md#irit.clueweb)

??? abstract "Abstract"
	
	In this paper we give an overview of the participation of the IRIT, GeoComp, and LIUPPA labs in the TREC 2013 Contextual Suggestion Track. Our framework combines existing geo-tools or services (e.g., Google Places, Yahoo! BOSS Geo Services, PostGIS, Gisgraphy, GeoNames) and ranks results according to features such as context-place distance, place popularity, and user preferences. We participated in the Open Web and ClueWeb12 sub-tracks with runs IRIT.OpenWeb and IRIT.ClueWeb.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HubertCPTPS13.bib) "
	```
	@inproceedings{DBLP:conf/trec/HubertCPTPS13,
		author = {Gilles Hubert and Guillaume Cabanac and Karen Pinel{-}Sauvagnat and Damien Palacio and Christian Sallaberry},
		editor = {Ellen M. Voorhees},
		title = {IRIT, GeoComp, and {LIUPPA} at the {TREC} 2013 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/IRIT-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HubertCPTPS13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PITT at TREC 2013 Contextual Suggestion Track

_Ming Jiang, Daqing He_

- :fontawesome-solid-user-group: **Participant:** [PITT](./context/participants.md#pitt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/pitt-context.pdf](http://trec.nist.gov/pubs/trec22/papers/pitt-context.pdf)
- :material-file-search: **Runs:** [ming_1](./context/runs.md#ming_1) | [ming_2](./context/runs.md#ming_2)

??? abstract "Abstract"
	
	This paper reports the IRIS Lab@Pitt's participation to 2013 TREC Contextual Suggestion track, which focuses on technology and issues related to location-based recommender systems (LBRSs). Besides the data provided by the track, our recommendation algorithms also retrieve information from Yelp for creating candidate, example and user profiles. Our algorithms uses linear regression model to combine multiple attributes of candidate profiles into the calculation, and performed 5-fold cross validation for training and testing on 2012 track data. The two runs we submitted this year both obtained reasonable good performance comparing with the median results of all runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangH13.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangH13,
		author = {Ming Jiang and Daqing He},
		editor = {Ellen M. Voorhees},
		title = {{PITT} at {TREC} 2013 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/pitt-context.pdf},
		timestamp = {Mon, 05 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangH13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Amsterdam at the TREC 2013 Contextual Suggestion Track:  Learning User Preferences from Wikitravel Categories

_Marijn Koolen, Hugo C. Huurdeman, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./context/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/uvaKamps-context.pdf](http://trec.nist.gov/pubs/trec22/papers/uvaKamps-context.pdf)
- :material-file-search: **Runs:** [UAmsTF30WU](./context/runs.md#uamstf30wu)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2013 Contextual Suggestion Track. The goal of the track is to evaluate systems that provide suggestions for activities to users in a specific location, taking into account their personal preferences. As a source for travel suggestions we use Wikitravel, which is a community-based travel guide for destinations all over the world. From pages dedicated to cities in the US we extract suggestions for sightseeing, shopping, eating and drinking. Descriptions from positive examples in the user profiles are used as queries to rank all suggestions in the US. Our user-dependent approach merges the per-query rankings of the positive examples of a single user. We automatically classified the rated examples according to the Wikitravel categories—Buy, Do, Drink, Eat and See - and derived a user-specific prior probability per category. With these we re-rank Wikitravel suggestions. The ranked suggestions are then filtered based on the location of the user.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoolenHK13.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoolenHK13,
		author = {Marijn Koolen and Hugo C. Huurdeman and Jaap Kamps},
		editor = {Ellen M. Voorhees},
		title = {University of Amsterdam at the {TREC} 2013 Contextual Suggestion Track: Learning User Preferences from Wikitravel Categories},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/uvaKamps-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KoolenHK13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Context Suggestion Track TREC 2013

_Bingyang Liu, Yanqin Zhong, Yue Liu, Dayong Wu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./context/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/ICTNET-context.pdf](http://trec.nist.gov/pubs/trec22/papers/ICTNET-context.pdf)
- :material-file-search: **Runs:** [RUN1](./context/runs.md#run1) | [RUN2](./context/runs.md#run2)

??? abstract "Abstract"
	
	This year we did not use any external structured resources like 'Yelp'. An 'Information Retrieval' scheme is implemented. We built index of the ClueWeb12-B-13 using Lucene and use manually and automatically constructed queries to fetch pages from the data subset. Finally we ranked the pages based on user preferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuZLWC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuZLWC13,
		author = {Bingyang Liu and Yanqin Zhong and Yue Liu and Dayong Wu and Xueqi Cheng},
		editor = {Ellen M. Voorhees},
		title = {{ICTNET} at Context Suggestion Track {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/ICTNET-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuZLWC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Boosting Venue Page Rankings for Contextual Retrieval-Georgetown at  TREC 2013 Contextual Suggestion Track

_Jiyun Luo, Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [GeorgetownYang](./context/participants.md#georgetownyang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/georgetown-context.pdf](http://trec.nist.gov/pubs/trec22/papers/georgetown-context.pdf)
- :material-file-search: **Runs:** [BOW_V18](./context/runs.md#bow_v18) | [BOW_V17](./context/runs.md#bow_v17)

??? abstract "Abstract"
	
	We participate in the closed collection sub-track of the TREC 2013 Contextual Suggestion. The dataset that we use is an integrated collection of ClueWeb12 Category B, Wikitravel, and the city-specific sub-collection; all are from ClueWeb12. Since the Open Web is not used in our submissions, the task is essentially a retrieval task instead of a result merging task. Our system takes users' ratings of venues in a training city as inputs, and generates titles, document identification numbers, and descriptions for venues that fit users' interests in a new city. Ideal relevant documents for this task should be a list of Web pages each of which is a venue's homepage, which we call a “venue page”. However, off-the-shelf search tools, such as Lemur, fail to retrieve such venue homepages from the collection. They either retrieve non-relevant documents or “yellow-page”-like pages that link to a long list of venue pages where the links are often broken and the destination pages are out of the collection. Therefore, large portions of the retrieved documents are not suitable as answers for contextual suggestion. To address this challenge, we experiment two different approaches, a precision-oriented approach and a recall-oriented approach, to boost the relevant venue pages' ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuoY13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuoY13,
		author = {Jiyun Luo and Hui Yang},
		editor = {Ellen M. Voorhees},
		title = {Boosting Venue Page Rankings for Contextual Retrieval-Georgetown at {TREC} 2013 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/georgetown-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuoY13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CIRGIRDISCO at TREC 2013 Contextual Suggestion Track: Using the  Wikipedia Graph Structure for Item-to-Item Recommendation

_Muhammad Atif Qureshi, Arjumand Younus, Colm O'Riordan, Gabriella Pasi_

- :fontawesome-solid-user-group: **Participant:** [CIRG_IRDISCO](./context/participants.md#cirg_irdisco)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/NUIG-context.pdf](http://trec.nist.gov/pubs/trec22/papers/NUIG-context.pdf)
- :material-file-search: **Runs:** [CIRG_IRDISCOA](./context/runs.md#cirg_irdiscoa) | [CIRG_IRDISCOB](./context/runs.md#cirg_irdiscob)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2013 contextual suggestion task. We fetch possible locations based on given contexts using Google Places API and WikiTravel. This is followed by a Wikipedia-based item-to-item similarity computation framework which uses the Wikipedia category-article structure to compute similarity between example locations rated by users and the suggested locations. This is then used in an item-based nearest neighbor recommendation framework to recommend the locations based on given user profile ratings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QureshiYOP13.bib) "
	```
	@inproceedings{DBLP:conf/trec/QureshiYOP13,
		author = {Muhammad Atif Qureshi and Arjumand Younus and Colm O'Riordan and Gabriella Pasi},
		editor = {Ellen M. Voorhees},
		title = {{CIRGIRDISCO} at {TREC} 2013 Contextual Suggestion Track: Using the Wikipedia Graph Structure for Item-to-Item Recommendation},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/NUIG-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QureshiYOP13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lugano at the TREC 2013 Contextual Suggestion Track

_Andrei Rikitianskii, Morgan Harvey, Fabio Crestani_

- :fontawesome-solid-user-group: **Participant:** [ULugano](./context/participants.md#ulugano)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/lugano-context.pdf](http://trec.nist.gov/pubs/trec22/papers/lugano-context.pdf)
- :material-file-search: **Runs:** [simpleScore](./context/runs.md#simplescore) | [complexScore](./context/runs.md#complexscore)

??? abstract "Abstract"
	
	We report on the University of Lugano's participation in the Contextual Suggestion track of TREC 2013 for which we submitted two runs. In particular we present our approach for contextual suggestion which very carefully constructs user profiles in order to provide more accurate and relevant recommendations. The evaluations of our two runs are reported and compared to each other. Based on the track evaluations we demonstrate that our system performs very well in comparison to other runs submitted to the track, managing to achieve the best results in nearly half of all runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RikitianskiiHC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/RikitianskiiHC13,
		author = {Andrei Rikitianskii and Morgan Harvey and Fabio Crestani},
		editor = {Ellen M. Voorhees},
		title = {University of Lugano at the {TREC} 2013 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/lugano-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RikitianskiiHC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Simple Context Dependent Suggestion System

_Dwaipayan Roy, Ayan Bandyopadhyay, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [ISIatTREC](./context/participants.md#isiattrec)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/isi-context.pdf](http://trec.nist.gov/pubs/trec22/papers/isi-context.pdf)
- :material-file-search: **Runs:** [isirun](./context/runs.md#isirun)

??? abstract "Abstract"
	
	The Contextual Suggestion Problem focuses on search techniques for complex information needs that are highly dependent on context and user interest. In this paper, we present our approach to providing user and context dependent suggestions. The official evaluation scores for our submitted run are reported and compared to the overall median scores (across all 34 runs).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoyBM13.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoyBM13,
		author = {Dwaipayan Roy and Ayan Bandyopadhyay and Mandar Mitra},
		editor = {Ellen M. Voorhees},
		title = {A Simple Context Dependent Suggestion System},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/isi-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoyBM13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2013: Contextual Suggestion Track

_Sushma Yalamarti, Mariam Daoud, Jimmy X. Huang_

- :fontawesome-solid-user-group: **Participant:** [YORK](./context/participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/york-context.pdf](http://trec.nist.gov/pubs/trec22/papers/york-context.pdf)
- :material-file-search: **Runs:** [york13cr1](./context/runs.md#york13cr1) | [york13cr2](./context/runs.md#york13cr2)

??? abstract "Abstract"
	
	This paper presents our participation in the Contextual Suggestion Track of TREC 2013. The goal of this track is to investigate search techniques for complex information needs that are highly dependent on context and user interests. To achieve this goal, we propose a semantic user profile modeling for personalized place recommendation. For the semantic user profile model construction, we construct a place ontology based on the Open Directory Project (ODP), a hierarchical ontology scheme for organizing websites. Previously rated attractions by the user are mapped to the place ontology where we represent positive and negative preferences under each place type. For a new user context represented by geographic coordinates, we rerank the top 50 suggestions returned by Google places API using the user profile.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YalamartiDH13.bib) "
	```
	@inproceedings{DBLP:conf/trec/YalamartiDH13,
		author = {Sushma Yalamarti and Mariam Daoud and Jimmy X. Huang},
		editor = {Ellen M. Voorhees},
		title = {York University at {TREC} 2013: Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/york-context.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YalamartiDH13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Opinion-aware Approach to Contextual Suggestion

_Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./context/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/udel_fang-context.pdf](http://trec.nist.gov/pubs/trec22/papers/udel_fang-context.pdf)
- :material-file-search: **Runs:** [UDInfoCS1](./context/runs.md#udinfocs1) | [UDInfoCS2](./context/runs.md#udinfocs2)

??? abstract "Abstract"
	
	In this paper we describe our efforts for TREC Contextual Suggestion task. Our goal of this year is to evaluate the effectiveness of (1) an opinion-based method to model user profiles and rank candidate suggestions; and (2) a template-based summarization method that leverages the information from multiple resources to generate the description of a candidate suggestion. Existing approaches often uses the description or category information of the suggestions to estimate the user profile. However, one limitation of such approaches is that it may not be generalized well to other suggestions. To overcome this limitation, we propose to estimate the user profile based on the reviews of the candidate suggestions. Our preliminary results show that the proposed new method can improve the performance. Moreover, we explore a new way of generating summaries for the candidate suggestions. The main idea is that we want to leverage the information from multiple sources to generate a more comprehensive summary for a candidate suggestion. In particular, the summary includes the category information of the suggestion, meta-description of the website, reviews of the suggestion and the similar example suggestions that the user liked.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangF13.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangF13,
		author = {Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees},
		title = {An Opinion-aware Approach to Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/udel\_fang-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangF13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI and TU Delft Notebook TREC 2013: Contextual Suggestion,  Federated Web Search, KBA, and Web Tracks

_Alejandro Bellogín, Gebrekirstos G. Gebremeskel, Jiyin He, Alan Said, Thaer Samar, Arjen P. de Vries, Jimmy Lin, Jeroen B. P. Vuurens_

- :fontawesome-solid-user-group: **Participant:** [CWI](./context/participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf](http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf)
- :material-file-search: **Runs:** [IBCosTop1](./context/runs.md#ibcostop1)

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

#### University of Glasgow at TREC 2013: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Web Tracks

_Richard McCreadie, M-Dyaa Albakour, Stuart Mackie, Nut Limsopatham, Craig Macdonald, Iadh Ounis, Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./context/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf](http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf)
- :material-file-search: **Runs:** [uogTrCFP](./context/runs.md#uogtrcfp) | [uogTrCFX](./context/runs.md#uogtrcfx)

??? abstract "Abstract"
	
	In TREC 2013, we focus on tackling the challenges posed by the new Contextual Suggestion and Temporal summarisation tracks, as well as enhancing our existing technologies to tackle the new risk-sensitive aspect of the Web track, building upon our Terrier Information Retrieval Platform. In particular, for the Contextual Suggestion track, we investigate how to exploit location-based social networks, with the aim of better identifying venues within a city that a given user might be interested in visiting. For the Temporal Summarisation track, we propose a new summarisation framework and investigate novel techniques to adaptively alter the summarisation strategy over time. For the TREC Web track, we continue to build upon our learning-to-rank approaches and novel xQuAD / Fat frameworks within Terrier, increasing effectiveness when ranking and examining two new approaches to risk-sensitive retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieAMLMOD13.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieAMLMOD13,
		author = {Richard McCreadie and M{-}Dyaa Albakour and Stuart Mackie and Nut Limsopatham and Craig Macdonald and Iadh Ounis and Bekir Taner Din{\c{c}}er},
		editor = {Ellen M. Voorhees},
		title = {University of Glasgow at {TREC} 2013: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Web Tracks},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieAMLMOD13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Web 

#### TREC 2013 Web Track Overview

_Kevyn Collins-Thompson, Paul N. Bennett, Fernando Diaz, Charlie Clarke, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/WEB.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/WEB.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The goal of the TREC Web track is to explore and evaluate retrieval approaches over large-scale subsets of the Web - currently on the order of one billion pages. For TREC 2013, the fifth year of the Web track, we implemented the following significant updates compared to 2012. First, the Diversity task was replaced with a new Risk-sensitive retrieval task that explores the tradeoffs systems can achieve between effectiveness (overall gains across queries) and robustness (minimizing the probability of significant failure, relative to a provided baseline). Second, we based the 2013 Web track experiments on the new ClueWeb12 collection created by the Language Technologies Institute at Carnegie Mellon University. ClueWeb12 is a successor to the ClueWeb09 dataset, comprising about one billion Web pages crawled between Feb-May 2012.1 The crawling and collection process for ClueWeb12 included a rich set of seed URLs based on commercial search traffic, Twitter and other sources, and multiple measures for flagging undesirable content such as spam, pornography, and malware. The Adhoc task continued as in previous years. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Collins-Thompson13.bib) "
	```
	@inproceedings{DBLP:conf/trec/Collins-Thompson13,
		author = {Kevyn Collins{-}Thompson and Paul N. Bennett and Fernando Diaz and Charlie Clarke and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees},
		title = {{TREC} 2013 Web Track Overview},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/WEB.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Collins-Thompson13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI and TU Delft Notebook TREC 2013: Contextual Suggestion,  Federated Web Search, KBA, and Web Tracks

_Alejandro Bellogín, Gebrekirstos G. Gebremeskel, Jiyin He, Alan Said, Thaer Samar, Arjen P. de Vries, Jimmy Lin, Jeroen B. P. Vuurens_

- :fontawesome-solid-user-group: **Participant:** [CWI](./web/participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf](http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf)
- :material-file-search: **Runs:** [cwiwt13cps](./web/runs.md#cwiwt13cps) | [cwiwt13cpe](./web/runs.md#cwiwt13cpe) | [cwiwt13kld](./web/runs.md#cwiwt13kld)

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

#### DLDE at web track: ad-hoc task

_Jie Chen, Zhendong Niu, Yulong Shi, Changmin Zhang, Weiyin Li_

- :fontawesome-solid-user-group: **Participant:** [DLDE](./web/participants.md#dlde)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/DLDE-web.pdf](http://trec.nist.gov/pubs/trec22/papers/DLDE-web.pdf)
- :material-file-search: **Runs:** [dlde](./web/runs.md#dlde)

??? abstract "Abstract"
	
	In this note paper, we report our experiment method at adhoc task of Web Track 2013. The goal of this task is to return a rank of documents order by relevance from a collection of static web pages. Our group used meta search to help query expansion as the first step, and then retrieved with the expansion query to get the search results and rerank them.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenNSZL13.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenNSZL13,
		author = {Jie Chen and Zhendong Niu and Yulong Shi and Changmin Zhang and Weiyin Li},
		editor = {Ellen M. Voorhees},
		title = {{DLDE} at web track: ad-hoc task},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/DLDE-web.pdf},
		timestamp = {Thu, 10 Jun 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ChenNSZL13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2013-Session and Web Track

_Matthias Hagen, Michael Völske, Jakob Gomoll, Marie Bornemann, Lene Ganschow, Florian Kneist, Abdul Hamid Sabri, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [webis](./web/participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/webis-session-web.pdf](http://trec.nist.gov/pubs/trec22/papers/webis-session-web.pdf)
- :material-file-search: **Runs:** [webishybrid](./web/runs.md#webishybrid) | [webiswikibased](./web/runs.md#webiswikibased) | [webisnaive](./web/runs.md#webisnaive) | [webismixed](./web/runs.md#webismixed) | [webiswtbaseline](./web/runs.md#webiswtbaseline) | [webisrandom](./web/runs.md#webisrandom)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2013 Session and Web tracks. All our runs are on the full ClueWeb12 and use the online Indri retrieval system hosted at CMU. As for the session track, our runs implement three main ideas that were slightly improved compared to our participation in 2012: (1) distinguishing low risk sessions where we want to involve session knowledge in the form of a conservative query expansion strategy (only few expansion terms based on keywords from previous queries and seen/clicked documents/titles/snippets) from those where we don't, (2) conservative query expansion based on similar sessions from other users, (3) result list postprocessing to boost clicked documents of other users in similar sessions. As these techniques leave a lot of queries unchanged when not enough session knowledge is available, we do not expect large gains over all the sessions. As for the Web track, our runs exploit different strategies of segmenting the queries (i.e., identifying and highlighting concepts within the query as phrases to be contained in the results). Additionally to algorithmic segmentations based on our WWW 2011 and CIKM 2012 ideas, we had one run where we chose the segmentation according to a majority vote amongst five humans. In a last run, the results are constructed so as to be disjunct from the track's baseline's and our other runs' results. Instead, we populate the result list with documents that different segmentations of the query would return top-ranked or that are deeper in the ranking for segmentations already chosen in previous runs. The underlying idea was to obtain at least some judgments for the top documents that other segmentations would bring up in their rankings. As most of the queries are rather short, we expect only slight improvements or no effect at all from the different segmentation strategies that are tailored to longer and more verbose queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenVGBGKSS13.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenVGBGKSS13,
		author = {Matthias Hagen and Michael V{\"{o}}lske and Jakob Gomoll and Marie Bornemann and Lene Ganschow and Florian Kneist and Abdul Hamid Sabri and Benno Stein},
		editor = {Ellen M. Voorhees},
		title = {Webis at {TREC} 2013-Session and Web Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/webis-session-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenVGBGKSS13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Application of Data Fusion in the Web Track

_Chunlan Huang, Shengli Wu, Jinbo Feng, Yongquan Tao, Yuping Xing_

- :fontawesome-solid-user-group: **Participant:** [UJS](./web/participants.md#ujs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/jiangsu-web.pdf](http://trec.nist.gov/pubs/trec22/papers/jiangsu-web.pdf)
- :material-file-search: **Runs:** [UJS13LCRAd1](./web/runs.md#ujs13lcrad1) | [UJS13LCRAd2](./web/runs.md#ujs13lcrad2) | [UJS13Risk1](./web/runs.md#ujs13risk1) | [UJS13Risk2](./web/runs.md#ujs13risk2)

??? abstract "Abstract"
	
	In this paper, we report on the experiments we conducted whilst participating in the TREC 2013 Web track. We use data fusion to test how to improve the results from different information retrieval systems. Linear combination is used for fusion and multiple linear regression is used to obtain suitable weights for all the component systems involved. In our experiments, the ClueWeb09 dataset is used as training data to obtain weights for the three component systems Indri, MG4J, and Terrier. After running the official evaluation program, we find that all four runs submitted are better than all component results with one exception.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangWFTX13.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangWFTX13,
		author = {Chunlan Huang and Shengli Wu and Jinbo Feng and Yongquan Tao and Yuping Xing},
		editor = {Ellen M. Voorhees},
		title = {Application of Data Fusion in the Web Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/jiangsu-web.pdf},
		timestamp = {Wed, 08 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HuangWFTX13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Crowdsourcing for Robustness in Web Search

_Yubin Kim, Kevyn Collins-Thompson, Jaime Teevan_

- :fontawesome-solid-user-group: **Participant:** [MSR_Redmond](./web/participants.md#msr_redmond)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/MSR-web.pdf](http://trec.nist.gov/pubs/trec22/papers/MSR-web.pdf)
- :material-file-search: **Runs:** [msr_alpha10](./web/runs.md#msr_alpha10) | [msr_alpha5](./web/runs.md#msr_alpha5) | [msr_alpha1](./web/runs.md#msr_alpha1) | [msr_alpha0](./web/runs.md#msr_alpha0) | [msr_alpha0_95_4](./web/runs.md#msr_alpha0_95_4)

??? abstract "Abstract"
	
	Search systems are typically evaluated by averaging an effectiveness measure over a set of queries. However, this method does not capture the the robustness of the retrieval approach, as measured by its variability across queries. Robustness can be a critical retrieval property, especially in settings such as commercial search engines that must build user trust and maintain brand quality. This paper investigates two ways of integrating crowdsourcing into web search in order to increase robustness. First, we use crowd workers in query expansion; votes by crowd workers are used to determine candidate expansion terms that have broad coverage and high relatedness to query terms mitigating the risky nature of query expansion. Second, crowd workers are used to filter the top ranks of a ranked list in order to remove non-relevant documents. We find that these methods increase robustness in search results. In addition, we discover that different evaluation measures lead to different optimal parameter settings when optimizing for robustness; precision-oriented metrics favor safer parameter settings while recall-oriented metrics can handle riskier configurations that improve average performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KimCT13.bib) "
	```
	@inproceedings{DBLP:conf/trec/KimCT13,
		author = {Yubin Kim and Kevyn Collins{-}Thompson and Jaime Teevan},
		editor = {Ellen M. Voorhees},
		title = {Crowdsourcing for Robustness in Web Search},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/MSR-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KimCT13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2013: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Web Tracks

_Richard McCreadie, M-Dyaa Albakour, Stuart Mackie, Nut Limsopatham, Craig Macdonald, Iadh Ounis, Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./web/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf](http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf)
- :material-file-search: **Runs:** [uogTrAIwLmb](./web/runs.md#uogtraiwlmb) | [uogTrBDnLmxw](./web/runs.md#uogtrbdnlmxw) | [uogTrAS2Lb](./web/runs.md#uogtras2lb) | [uogTrBDnLaxw](./web/runs.md#uogtrbdnlaxw) | [uogTrADnLrb](./web/runs.md#uogtradnlrb) | [uogTrAS1Lb](./web/runs.md#uogtras1lb)

??? abstract "Abstract"
	
	In TREC 2013, we focus on tackling the challenges posed by the new Contextual Suggestion and Temporal summarisation tracks, as well as enhancing our existing technologies to tackle the new risk-sensitive aspect of the Web track, building upon our Terrier Information Retrieval Platform. In particular, for the Contextual Suggestion track, we investigate how to exploit location-based social networks, with the aim of better identifying venues within a city that a given user might be interested in visiting. For the Temporal Summarisation track, we propose a new summarisation framework and investigate novel techniques to adaptively alter the summarisation strategy over time. For the TREC Web track, we continue to build upon our learning-to-rank approaches and novel xQuAD / Fat frameworks within Terrier, increasing effectiveness when ranking and examining two new approaches to risk-sensitive retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieAMLMOD13.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieAMLMOD13,
		author = {Richard McCreadie and M{-}Dyaa Albakour and Stuart Mackie and Nut Limsopatham and Craig Macdonald and Iadh Ounis and Bekir Taner Din{\c{c}}er},
		editor = {Ellen M. Voorhees},
		title = {University of Glasgow at {TREC} 2013: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Web Tracks},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieAMLMOD13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Technion at TREC 2013 Web Track: Cluster-based Document Retrieval

_Fiana Raiber, Oren Kurland_

- :fontawesome-solid-user-group: **Participant:** [Technion](./web/participants.md#technion)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/technion-web.pdf](http://trec.nist.gov/pubs/trec22/papers/technion-web.pdf)
- :material-file-search: **Runs:** [clustmrfbf](./web/runs.md#clustmrfbf) | [clustmrfaf](./web/runs.md#clustmrfaf) | [mmrbf](./web/runs.md#mmrbf)

??? abstract "Abstract"
	
	Many cluster-based document retrieval methods have been proposed over the years. In our submissions to the ad hoc task of the TREC 2013 Web Track we experimented with one such highly effective method. Empirical results demonstrate the effectiveness of using our approach; specifically, with respect to other submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RaiberK13.bib) "
	```
	@inproceedings{DBLP:conf/trec/RaiberK13,
		author = {Fiana Raiber and Oren Kurland},
		editor = {Ellen M. Voorhees},
		title = {The Technion at {TREC} 2013 Web Track: Cluster-based Document Retrieval},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/technion-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RaiberK13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Universite de Montreal at TREC 2013: Experiments with Quantum Language  Models in the Web Track

_Alessandro Sordoni, Wei Yuan, Jian-Yun Nie_

- :fontawesome-solid-user-group: **Participant:** [diro_web_13](./web/participants.md#diro_web_13)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/diro-web.pdf](http://trec.nist.gov/pubs/trec22/papers/diro-web.pdf)
- :material-file-search: **Runs:** [udemQlm1l](./web/runs.md#udemqlm1l) | [udemQlm1lFb](./web/runs.md#udemqlm1lfb) | [udemQlm1lFbWiki](./web/runs.md#udemqlm1lfbwiki) | [udemQlml1FbR](./web/runs.md#udemqlml1fbr) | [udemQlml1R](./web/runs.md#udemqlml1r) | [udemFbWikiR](./web/runs.md#udemfbwikir)

??? abstract "Abstract"
	
	In TREC 2013, we focus on addressing the challenges posed by the Web track using our recently proposed Quantum Language Modeling (QLM) approach for IR [1]. QLM can be considered as a dependence model for IR for its capability of representing and integrating compound term dependencies into the scoring function. Among the main properties of the model, two of them make it stand out from the literature of existing dependence models (such as MRF [3]). First, QLM does not combine scores obtained from matching single terms and from matching compound dependencies, which makes it virtually parameterless. This is quite an appealing property for an IR system, especially when a new dataset such as ClueWeb12 is released and no previous training examples can be leveraged to fine-tune important parameters. The second peculiar feature of our model is its ability to automatically fallback onto the baseline bag-of-words score in the case that the required dependence relationship does not hold in the document. This is expected to bring improved robustness w.r.t. the baseline ranking. In the light of these considerations, the Web Track ad-hoc and robustness task seem the perfect testbeds for our model. In what follows we briefly review some of the theoretical background of QLM before delving into the description of the submitted runs and obtained results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SordoniYN13.bib) "
	```
	@inproceedings{DBLP:conf/trec/SordoniYN13,
		author = {Alessandro Sordoni and Wei Yuan and Jian{-}Yun Nie},
		editor = {Ellen M. Voorhees},
		title = {Universite de Montreal at {TREC} 2013: Experiments with Quantum Language Models in the Web Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/diro-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SordoniYN13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2013

_Yuanhai Xue, Feng Guan, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./web/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/ICTNET-web.pdf](http://trec.nist.gov/pubs/trec22/papers/ICTNET-web.pdf)
- :material-file-search: **Runs:** [ICTNET13ADR3](./web/runs.md#ictnet13adr3) | [ICTNET13RSR3](./web/runs.md#ictnet13rsr3) | [ICTNET13RSR2](./web/runs.md#ictnet13rsr2) | [ICTNET13ADR2](./web/runs.md#ictnet13adr2) | [ICTNET13ADR1](./web/runs.md#ictnet13adr1) | [ICTNET13RSR1](./web/runs.md#ictnet13rsr1)

??? abstract "Abstract"
	
	In this paper, we report our TREC experiments with both ad-hoc task and risk-sensitive task of Web Track 2013. The ClueWeb12 dataset and its derived data were used this year. We use BM25 model with term proximity, entity recognition and external resource to rank the final results. We submitted six runs which were not optimized for any particular metric.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XueGYLC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/XueGYLC13,
		author = {Yuanhai Xue and Feng Guan and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees},
		title = {{ICTNET} at Web Track 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/ICTNET-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XueGYLC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluating the Effectiveness of Axiomatic Approaches in Web Track

_Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./web/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/udel_fang-web.pdf](http://trec.nist.gov/pubs/trec22/papers/udel_fang-web.pdf)
- :material-file-search: **Runs:** [UDInfolabWEB1](./web/runs.md#udinfolabweb1) | [UDInfolabWEB1R](./web/runs.md#udinfolabweb1r) | [UDInfolabWEB2](./web/runs.md#udinfolabweb2) | [UDInfolabWEB2R](./web/runs.md#udinfolabweb2r)

??? abstract "Abstract"
	
	In this paper we describe our efforts for TREC 2013 Web track. We focus on evaluating the effectiveness of axiomatic retrieval model on large data collection. Axiomatic approach basically searches for the retrieval functions that satisfy some reasonable retrieval constraints. We also evaluate the semantic term matching method which does the query expansion by choosing the semantically related terms. Experiment results on adhoc task and diversity task demonstrate the effectiveness of the method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangF13a.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangF13a,
		author = {Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees},
		title = {Evaluating the Effectiveness of Axiomatic Approaches in Web Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/udel\_fang-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangF13a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mirex and Taily at TREC 2013

_Robin Aly, Djoerd Hiemstra, Dolf Trieschnigg, Thomas Demeester_

- :fontawesome-solid-user-group: **Participant:** [ut](./web/participants.md#ut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/lowlands-web-federated.pdf](http://trec.nist.gov/pubs/trec22/papers/lowlands-web-federated.pdf)
- :material-file-search: **Runs:** [ut22base](./web/runs.md#ut22base) | [ut22spam](./web/runs.md#ut22spam) | [ut22xact](./web/runs.md#ut22xact)

??? abstract "Abstract"
	
	We describe the participation of the Lowlands at the Web Track and the FedWeb track of TREC 2013. For the Web Track we used the Mirex Map-Reduce library with out-of-the-box approaches and for the FedWeb Track we adapted our shard selection method Taily for resource selection. Here, our results were above median and close to the maximum performance achieved.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlyHTD13.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlyHTD13,
		author = {Robin Aly and Djoerd Hiemstra and Dolf Trieschnigg and Thomas Demeester},
		editor = {Ellen M. Voorhees},
		title = {Mirex and Taily at {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/lowlands-web-federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlyHTD13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Federated Web Search 

#### Overview of the TREC 2013 Federated Web Search Track

_Thomas Demeester, Dolf Trieschnigg, Dong Nguyen, Djoerd Hiemstra_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/FEDERATED.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/FEDERATED.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Federated Web Search track is intended to promote research related to federated search in a realistic web setting, and hereto provides a large data collection gathered from a series of online search engines. This overview paper discusses the results of the first edition of the track, FedWeb 2013. The focus was on basic challenges in federated search: (1) resource selection, and (2) results merging. After an overview of the provided data collection and the relevance judgments for the test topics, the participants' individual approaches and results on both tasks are discussed. Promising research directions and an outlook on the 2014 edition of the track are provided as well.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DemeesterTNH13.bib) "
	```
	@inproceedings{DBLP:conf/trec/DemeesterTNH13,
		author = {Thomas Demeester and Dolf Trieschnigg and Dong Nguyen and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees},
		title = {Overview of the {TREC} 2013 Federated Web Search Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/FEDERATED.OVERVIEW.pdf},
		timestamp = {Tue, 24 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DemeesterTNH13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mirex and Taily at TREC 2013

_Robin Aly, Djoerd Hiemstra, Dolf Trieschnigg, Thomas Demeester_

- :fontawesome-solid-user-group: **Participant:** [ut](./federated/participants.md#ut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/lowlands-web-federated.pdf](http://trec.nist.gov/pubs/trec22/papers/lowlands-web-federated.pdf)
- :material-file-search: **Runs:** [utTailyM400](./federated/runs.md#uttailym400) | [utTailyNormM400](./federated/runs.md#uttailynormm400)

??? abstract "Abstract"
	
	We describe the participation of the Lowlands at the Web Track and the FedWeb track of TREC 2013. For the Web Track we used the Mirex Map-Reduce library with out-of-the-box approaches and for the FedWeb Track we adapted our shard selection method Taily for resource selection. Here, our results were above median and close to the maximum performance achieved.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlyHTD13.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlyHTD13,
		author = {Robin Aly and Djoerd Hiemstra and Dolf Trieschnigg and Thomas Demeester},
		editor = {Ellen M. Voorhees},
		title = {Mirex and Taily at {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/lowlands-web-federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlyHTD13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Collection and Document Language Models for Resource Selection

_Krisztian Balog_

- :fontawesome-solid-user-group: **Participant:** [UiS](./federated/participants.md#uis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/uis-federated.pdf](http://trec.nist.gov/pubs/trec22/papers/uis-federated.pdf)
- :material-file-search: **Runs:** [UiSS](./federated/runs.md#uiss) | [UiSP](./federated/runs.md#uisp) | [UiSSP](./federated/runs.md#uissp)

??? abstract "Abstract"
	
	This paper describes our participation in the resource selection task of the Federated Web Search track at TREC 2013. We employ two general strategies, collection-centric and document-centric, formulated in a language modeling framework. Results show that the document-centric approach delivers solid performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Balog13.bib) "
	```
	@inproceedings{DBLP:conf/trec/Balog13,
		author = {Krisztian Balog},
		editor = {Ellen M. Voorhees},
		title = {Collection and Document Language Models for Resource Selection},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/uis-federated.pdf},
		timestamp = {Tue, 08 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Balog13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Padua at TREC 2013: Federated Web Search Track

_Emanuele Di Buccio, Ivano Masiero, Massimo Melucci_

- :fontawesome-solid-user-group: **Participant:** [UPD](./federated/participants.md#upd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/upd-federated.pdf](http://trec.nist.gov/pubs/trec22/papers/upd-federated.pdf)
- :material-file-search: **Runs:** [UPDFW13sh](./federated/runs.md#updfw13sh) | [UPDFW13mu](./federated/runs.md#updfw13mu) | [UPDFW13rrsh](./federated/runs.md#updfw13rrsh) | [UPDFW13rrmu](./federated/runs.md#updfw13rrmu)

??? abstract "Abstract"
	
	This paper reports on the participation of the University of Padua to the TREC 2013 Federated Web Search track. The objective was the experimental investigation in Federated Web Search setting of TWF·IRF, which is a recursive weighting scheme for resource selection. The experimental results show that the TWF component, that is peculiar of this scheme, is sufficient to obtain an effective search engine ranking in terms of NDCG@20 when compared with the baseline and the runs of other track participants.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuccioMM13.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuccioMM13,
		author = {Emanuele Di Buccio and Ivano Masiero and Massimo Melucci},
		editor = {Ellen M. Voorhees},
		title = {University of Padua at {TREC} 2013: Federated Web Search Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/upd-federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuccioMM13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Federated Web Search Track 2013

_Feng Guan, Yuanhai Xue, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./federated/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/ICTNET-federated.pdf](http://trec.nist.gov/pubs/trec22/papers/ICTNET-federated.pdf)
- :material-file-search: **Runs:** [ICTNETRun1](./federated/runs.md#ictnetrun1) | [ICTNETRun2](./federated/runs.md#ictnetrun2) | [ICTNETRun3](./federated/runs.md#ictnetrun3)

??? abstract "Abstract"
	
	This paper is about work done for result merging task of TREC 2013 Federated Web Track. We introduce three methods for calculating score of documents. These methods are based on linear combination with scores of document fields. The distinction is different weight factors. Score of base line method is the combination with score of basic html fields. Page rank score is added in second method. Documents with lower score are filtered during the third method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GuanXYLC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/GuanXYLC13,
		author = {Feng Guan and Yuanhai Xue and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees},
		title = {{ICTNET} at Federated Web Search Track 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/ICTNET-federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GuanXYLC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NovaSearch at TREC 2013 Federated Web Search Track: Experiments  with rank fusion

_André Mourão, Flávio Martins, João Magalhães_

- :fontawesome-solid-user-group: **Participant:** [NOVASEARCH](./federated/participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/novasearch-federated.pdf](http://trec.nist.gov/pubs/trec22/papers/novasearch-federated.pdf)
- :material-file-search: **Runs:** [nsCondor](./federated/runs.md#nscondor) | [nsISR](./federated/runs.md#nsisr) | [nsRRF](./federated/runs.md#nsrrf)

??? abstract "Abstract"
	
	We propose an unsupervised late-fusion approach for the results merging task, based on combining the ranks from all the search engines. Our idea is based on the known pressure for Web search engines to put the most relevant documents at the very top of their ranks and the intuition that relevance of a document should increase as it appears on more search engines [9]. We performed experiments with state-of-the-art rank fusion algorithms: RRF and Condorcet Fuse and our proposed method: Inverse Square Rank (ISR) fusion algorithm. Rank fusion algorithms have low computational complexity and do not need engines to return document scores nor training data. Inverse Square Rank is a novel fully unsupervised rank fusion algorithm based on quadratic decay and on logarithmic document frequency normalization. The results achieved in the competition were very positive and we were able to improve them further post-TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MouraoMM13.bib) "
	```
	@inproceedings{DBLP:conf/trec/MouraoMM13,
		author = {Andr{\'{e}} Mour{\~{a}}o and Fl{\'{a}}vio Martins and Jo{\~{a}}o Magalh{\~{a}}es},
		editor = {Ellen M. Voorhees},
		title = {NovaSearch at {TREC} 2013 Federated Web Search Track: Experiments with rank fusion},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/novasearch-federated.pdf},
		timestamp = {Thu, 14 May 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MouraoMM13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ISI at the TREC 2013 Federated task

_Dipasree Pal, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [isi_pal](./federated/participants.md#isi_pal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/isipal-federated.pdf](http://trec.nist.gov/pubs/trec22/papers/isipal-federated.pdf)
- :material-file-search: **Runs:** [incgqd](./federated/runs.md#incgqd) | [incgqdv2](./federated/runs.md#incgqdv2) | [mergv1](./federated/runs.md#mergv1)

??? abstract "Abstract"
	
	The resource selection task contains a variety of Search Engines (SEs). There exists many domain specific SEs. These SEs can retrieve domain related query results more efficiently, whereas, they are not good at retrieving out-of-domain query results. Thus, it is difficult to predict the performance of a SE in a given query using the results of other queries. In our approach, each query has been searched in the web by all the SEs ( using Google search API's search site option ). We try to predict the performance of each SE with only top 8 retrieved results. Based on the term frequency of each query term in the retrieved results, our method ranks those SEs for that query. At the time of run submission, we missed a few queries. After that, we rank SEs for all queries using the same method. We observed that the result is better in nDCG@20 than the 'median' result. Also, when measured in ERR@20, the result is better in more queries. Median ERR@20, is substantially higher than our result for one query, this affects the average. In the results merging task, the same concept has been applied. Here also, we did not use the actual retrieved results, as it will take time after retrieval. The score of a SE found in the resource selection task, is used here. The documents retrieved by a SE are assigned a score that is a combination of its rank and the SE's score. This can be computed without retrieving actual results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PalM13.bib) "
	```
	@inproceedings{DBLP:conf/trec/PalM13,
		author = {Dipasree Pal and Mandar Mitra},
		editor = {Ellen M. Voorhees},
		title = {{ISI} at the {TREC} 2013 Federated task},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/isipal-federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PalM13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI and TU Delft Notebook TREC 2013: Contextual Suggestion,  Federated Web Search, KBA, and Web Tracks

_Alejandro Bellogín, Gebrekirstos G. Gebremeskel, Jiyin He, Alan Said, Thaer Samar, Arjen P. de Vries, Jimmy Lin, Jeroen B. P. Vuurens_

- :fontawesome-solid-user-group: **Participant:** [CWI](./federated/participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf](http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf)
- :material-file-search: **Runs:** [cwi13ODPJac](./federated/runs.md#cwi13odpjac) | [cwi13SniTI](./federated/runs.md#cwi13sniti) | [cwi13ODPTI](./federated/runs.md#cwi13odpti) | [CWI13bstTODPJ](./federated/runs.md#cwi13bsttodpj) | [CWI13iaTODPJ](./federated/runs.md#cwi13iatodpj) | [CWI13IndriQL](./federated/runs.md#cwi13indriql)

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

## Microblog 

#### Overview of the TREC-2013 Microblog Track

_Jimmy Lin, Miles Efron_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/MB.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/MB.OVERVIEW.pdf)
??? abstract "Abstract"
	
	This year represents the third iteration of the TREC Microblog track, which began in 2011. There was no substantive change in the task definition, which remains nominally real-time search, best summarized as “At time T , give me the most relevant tweets about topic X.” However, we introduced a radically different evaluation methodology, dubbed “evaluation as a service”, which attempted to address deficiencies in how the document collection was distributed in previous years. This is the first time such an approach has been deployed at TREC. Overall, we believe that the evaluation methodology was successful, drawing participation from twenty groups around the world.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinE13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinE13,
		author = {Jimmy Lin and Miles Efron},
		editor = {Ellen M. Voorhees},
		title = {Overview of the {TREC-2013} Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/MB.OVERVIEW.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinE13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion for Microblog Retrieval: 2013

_Ayan Bandyopadhyay_

- :fontawesome-solid-user-group: **Participant:** [ISIKol](./microblog/participants.md#isikol)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/isikol-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/isikol-microblog.pdf)
- :material-file-search: **Runs:** [GSAT](./microblog/runs.md#gsat) | [GSAS](./microblog/runs.md#gsas) | [GSAA](./microblog/runs.md#gsaa)

??? abstract "Abstract"
	
	Microblogging sites like http://twitter.com have emerged as a popular platform for expressing opinions. Given the increasing amount of information available through such microblogging sites, it would be nice to be able to retrieve useful tweets in response to a given information need. Finding relevant tweets that match a user query is challenging for the following reasons. Tweets are short. They contain a maximum of 140 characters. Tweets are not always written maintaining formal grammar and proper spelling. Spelling variations increase the likelihood of vocabulary mismatch. In this preliminary study, we explore standard query expansion approaches as a way to address this problem.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bandyopadhyay13.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bandyopadhyay13,
		author = {Ayan Bandyopadhyay},
		editor = {Ellen M. Voorhees},
		title = {Query Expansion for Microblog Retrieval: 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/isikol-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bandyopadhyay13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QCRI at TREC 2013 Microblog Track

_Tarek El-Ganainy, Walid Magdy, Wei Gao, Zhongyu Wei_

- :fontawesome-solid-user-group: **Participant:** [QCRI](./microblog/participants.md#qcri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/QCRI-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/QCRI-microblog.pdf)
- :material-file-search: **Runs:** [QCRI2](./microblog/runs.md#qcri2) | [QCRI1](./microblog/runs.md#qcri1) | [QCRI3](./microblog/runs.md#qcri3) | [QCRI4](./microblog/runs.md#qcri4)

??? abstract "Abstract"
	
	We report our work in the real-time ad hoc search task of TREC-2013 Microblog track. Our system focuses on improving retrieval effectiveness of Microblog search through query expansion and reranking of search results. We apply web-based query expansion algorithm for enriching the microblog queries with additional terms from concurrent webpages related to the search topic. Later we apply results reranking through utilizing state-of-the-art learning to rank algorithms to train 12 different ranking models using relevance judgment of Tweets2011-12 queries, for which we conduct feature engineering, validation dataset selection, and the ensemble of these models. Our approach differs from salient approaches in the previous Microblog tracks that are based on document expansion utilizing embedded URLs and that leverage some single ranking model for tweets re-ranking. Our pipeline constructed using the hybrid of these two components showed promising retrieval results on Tweets2013 benchmark dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/El-GanainyMGW13.bib) "
	```
	@inproceedings{DBLP:conf/trec/El-GanainyMGW13,
		author = {Tarek El{-}Ganainy and Walid Magdy and Wei Gao and Zhongyu Wei},
		editor = {Ellen M. Voorhees},
		title = {{QCRI} at {TREC} 2013 Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/QCRI-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/El-GanainyMGW13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Microblog Track in TREC 2013

_Jinhua Gao, Guoxin Cui, Shenghua Liu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./microblog/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/ICTNET-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/ICTNET-microblog.pdf)
- :material-file-search: **Runs:** [ICTNETBASE](./microblog/runs.md#ictnetbase) | [ICTNETBO1EXP](./microblog/runs.md#ictnetbo1exp) | [ICTNETCOCCUR](./microblog/runs.md#ictnetcoccur)

??? abstract "Abstract"
	
	Microblogging services, in which users can publish and share personal status, are now very popular, and attracting more and more industrial and scientific interests. Twitter is one of the most famous microblogging services. On twitter, Users can post personal updates, which are called tweets and limited to 140 characters long. In tweets, users can share interesting messages to their friends by retweeting(RT), push some tweets to specific users using @ mention, and indicate the topics of their tweets using # hashtags. The short-text characteristic and social attributes such as RT, @ mention and # hashtags, make traditional problems, like search, rank, and recommendation etc, quite different in microblogging settings. Microblog track was first introduced in 2011, and ICTNET group have participated in this track three times[2, 7]. In this year's track, only the realtime ad-hoc search task, which was also proposed in 2011 and 2012, was open for submission. This task requires to retrieve all the tweets that are relevant to query Q and before time T. Unlike the past two years, in which participants had to collect the corpus themselves, microblog track was first provided as a service this year, and participants could access the corpus through official APIs, which made it possible for the organizers to increase the size of corpus from 16M tweets to 260M tweets, which were collected via the Twitter streaming API over a two-month period. This report is organized as follows. Section 2 mainly focuses on the data preparation step, which contains the data collecting step and preprocessing step. The methodology and framework are illustrated in section 3, and some experiments and results are presented in section 4
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaoCLLC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaoCLLC13,
		author = {Jinhua Gao and Guoxin Cui and Shenghua Liu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees},
		title = {{ICTNET} at Microblog Track in {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/ICTNET-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaoCLLC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QU at TREC-2013: Expansion Experiments for Microblog Ad hoc Search

_Maram Hasanain, Latifa Al-Marri, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./microblog/participants.md#qu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/qu-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/qu-microblog.pdf)
- :material-file-search: **Runs:** [QUQueryExp](./microblog/runs.md#ququeryexp) | [QUBaseline](./microblog/runs.md#qubaseline) | [QUTemporal](./microblog/runs.md#qutemporal) | [QUDocExp](./microblog/runs.md#qudocexp)

??? abstract "Abstract"
	
	In the first appearance of Qatar University (QU) at Text REtrieval Conference (TREC), our submitted microblog runs explored different ways of expanding the context of both queries and tweets to overcome the sparsity and lack of context problems. Since the task is real-time, we have also considered the temporal aspect, once combined with tweet expansion technique, and another separately as a scoring factor. Our explored ideas were all unsupervised and only used internal resources (i.e., the provided API service with only access to the tweets). For query expansion, we have used pseudo relevance feedback to include terms from the top-ranked retrieved tweets. Based on experiments on previous TREC collections, an aggressive expansion with 30 terms or more provided the best improvement. For tweet expansion, a 2-step relevance modeling approach was leveraged to temporally and lexically expand a tweet. To further explore the effect of considering the time dimension in scoring tweets, we also developed a temporal re-scoring function used to favor tweets that are closer in time to the query over tweets that might be more lexically relevant but are posted further apart in time from the query. We also conducted post-TREC experiments in which we worked on enhancing the query expansion and temporal re-scoring approaches. Resuls released by TREC have shown that the temporal re-scoring run was the most effective run among all of our submitted ones. As for the post-TREC experiments, our results have shown that the enhanced query expansion and temporal re-scoring approaches had notable improvements on retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HasanainAE13.bib) "
	```
	@inproceedings{DBLP:conf/trec/HasanainAE13,
		author = {Maram Hasanain and Latifa Al{-}Marri and Tamer Elsayed},
		editor = {Ellen M. Voorhees},
		title = {{QU} at {TREC-2013:} Expansion Experiments for Microblog Ad hoc Search},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/qu-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HasanainAE13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Microblog Track 2013

_Lamjed Ben Jabeur, Firas Damak, Lynda Tamine, Guillaume Cabanac, Karen Pinel-Sauvagnat, Mohand Boughanem_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./microblog/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/IRIT-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/IRIT-microblog.pdf)
- :material-file-search: **Runs:** [iritfdUrlRoc](./microblog/runs.md#iritfdurlroc) | [iritfdUrl](./microblog/runs.md#iritfdurl) | [BNTSrK](./microblog/runs.md#bntsrk) | [BNTSrKSO](./microblog/runs.md#bntsrkso)

??? abstract "Abstract"
	
	This paper describes the participation of the IRIT lab, University of Toulouse, France, to the Microblog Track of TREC 2013. Two different approaches are experimented by our team for the real-time ad-hoc search task: (i) a Bayesian network retrieval model for tweet search and (ii) a document and query expansion model for microblog search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JabeurDTCPB13.bib) "
	```
	@inproceedings{DBLP:conf/trec/JabeurDTCPB13,
		author = {Lamjed Ben Jabeur and Firas Damak and Lynda Tamine and Guillaume Cabanac and Karen Pinel{-}Sauvagnat and Mohand Boughanem},
		editor = {Ellen M. Voorhees},
		title = {{IRIT} at {TREC} Microblog Track 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/IRIT-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JabeurDTCPB13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCAS at TREC-2013 Microblog Track

_Dongxing Li, Ben He, Xin Zhang, Tiejian Luo_

- :fontawesome-solid-user-group: **Participant:** [UCAS](./microblog/participants.md#ucas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/UCAS-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/UCAS-microblog.pdf)
- :material-file-search: **Runs:** [UCASgem](./microblog/runs.md#ucasgem) | [UCASqe](./microblog/runs.md#ucasqe)

??? abstract "Abstract"
	
	The participation of University of Chinese Academy of Sciences (UCAS) in the real-time adhoc task in Microblog track aims to evaluate the effectiveness of the query-biased learning to rank model, which was proposed in our previous work. To further improve the retrieval effectiveness of learning to rank, we construct the query-biased learning to rank framework by taking the difference between queries into consideration. In particular, a query-biased ranking model is learned by a cluster classification learning algorithm in order to better capture the characteristics of the given queries. This query-biased ranking mode is combined with the general ranking model (BM25 etc.) to produce the final ranked list of tweets in response to the given target query. We were also planning to incorporate a machine learning approach for selecting high-quality training data for improving the effectiveness of learning to rank. However, due to interruption caused by lab move, we only managed to experiment with the query-biased approach using partial features.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiHZL13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiHZL13,
		author = {Dongxing Li and Ben He and Xin Zhang and Tiejian Luo},
		editor = {Ellen M. Voorhees},
		title = {{UCAS} at {TREC-2013} Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/UCAS-microblog.pdf},
		timestamp = {Fri, 27 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiHZL13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A User-in-the-Loop Process for Investigational Search: Foreseer in  TREC 2013 Microblog Track

_Cheng Li, Yue Wang, Qiaozhu Mei_

- :fontawesome-solid-user-group: **Participant:** [Foreseer](./microblog/participants.md#foreseer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/foreseer-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/foreseer-microblog.pdf)
- :material-file-search: **Runs:** [FSsvm](./microblog/runs.md#fssvm) | [Direrank](./microblog/runs.md#direrank) | [Avgrank](./microblog/runs.md#avgrank) | [RvsDir](./microblog/runs.md#rvsdir)

??? abstract "Abstract"
	
	Traditionally, ad hoc retrieval aims at satisfying an information need with a few highly relevant documents. This high-precision approach works well for simple and clear queries. When the information need becomes complex, a few top-ranked documents may not provide satisfactory answer. As a result, the user adapts to reformulate the query to explore more relevant information; the search engine evolves to diversify results to cover the user's real information need. In cases where the user puts emphasis on high recall of the results, the search process becomes increasingly laborious. We propose a retrieval system that interacts with the user to obtain high precision and high recall search results, while minimizing the user effort. It iteratively explores the collection by a series of queries to optimize the recall, and refines an active learning classifier to maintain the precision. We built a prototype of the system for TREC 2013 Microblog Track. Depending on the actual query, the system converges to a stable decision on relevant/non-relevant tweets after asking for a few hundred labels, which was used to retrieve and rank 10,000 tweets (maximum allowance of the TREC API).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiWM13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiWM13,
		author = {Cheng Li and Yue Wang and Qiaozhu Mei},
		editor = {Ellen M. Voorhees},
		title = {A User-in-the-Loop Process for Investigational Search: Foreseer in {TREC} 2013 Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/foreseer-microblog.pdf},
		timestamp = {Thu, 03 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiWM13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NovaSearch at TREC 2013 Microblog Track: Experiments with reranking  using Wikipedia

_Flávio Martins, André Mourão, João Magalhães_

- :fontawesome-solid-user-group: **Participant:** [NOVASEARCH](./microblog/participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/novasearch-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/novasearch-microblog.pdf)
- :material-file-search: **Runs:** [NOVAsearch01](./microblog/runs.md#novasearch01) | [NOVAsearch02](./microblog/runs.md#novasearch02) | [NOVAsearch03](./microblog/runs.md#novasearch03) | [NOVAsearch00](./microblog/runs.md#novasearch00)

??? abstract "Abstract"
	
	Users engaged in microblogging services and social-media apps contribute to multiple real-time text streams which amass large volumes of messages often sparked by events reported in newswire and in other media. We explore the use of external sources to detect topic popularity surges and improve microblog search performance using time- based language models [3]. The major novelty concerns the analysis that explores Wikipedia page view streams to find topic interest spikes. We obtained promising initial results when using evidence from Wikipedia for temporal reranking with the Tweets2013 dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MartinsMM13.bib) "
	```
	@inproceedings{DBLP:conf/trec/MartinsMM13,
		author = {Fl{\'{a}}vio Martins and Andr{\'{e}} Mour{\~{a}}o and Jo{\~{a}}o Magalh{\~{a}}es},
		editor = {Ellen M. Voorhees},
		title = {NovaSearch at {TREC} 2013 Microblog Track: Experiments with reranking using Wikipedia},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/novasearch-microblog.pdf},
		timestamp = {Thu, 14 May 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MartinsMM13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2013 Microblog Track Experiments at Kobe University

_Taiki Miyanishi, Sayaka Kitaguchi, Kazuhiro Seki, Kuniaki Uehara_

- :fontawesome-solid-user-group: **Participant:** [KobeU](./microblog/participants.md#kobeu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/kobe-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/kobe-microblog.pdf)
- :material-file-search: **Runs:** [kobeU](./microblog/runs.md#kobeu) | [kobeRMU](./microblog/runs.md#kobermu) | [kobeTSFRM](./microblog/runs.md#kobetsfrm) | [kobeTSFRMU](./microblog/runs.md#kobetsfrmu)

??? abstract "Abstract"
	
	This paper describes our approach to real-time ad hoc task processing in the TREC 2013 microblog track. The approach uses a concept-based query expansion method based on a temporal relevance model that uses the temporal variation of concepts (e.g. terms or phrases) on microblogs. Our model extends an effective existing word and concept-based relevance models by tracking the concept frequency over time in microblogging services. The experimentally obtained results demonstrate that our concept-based query expansion method improve search performance, especially when using tweet selection feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MiyanishiKSU13.bib) "
	```
	@inproceedings{DBLP:conf/trec/MiyanishiKSU13,
		author = {Taiki Miyanishi and Sayaka Kitaguchi and Kazuhiro Seki and Kuniaki Uehara},
		editor = {Ellen M. Voorhees},
		title = {{TREC} 2013 Microblog Track Experiments at Kobe University},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/kobe-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MiyanishiKSU13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow (UoG_TwTeam) at TREC Microblog 2013

_Jesus A. Rodriguez Perez, Andrew James McMinn, Joemon M. Jose_

- :fontawesome-solid-user-group: **Participant:** [UoG_TwTeam](./microblog/participants.md#uog_twteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/TwTeam-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/TwTeam-microblog.pdf)
- :material-file-search: **Runs:** [ModelSEL922](./microblog/runs.md#modelsel922) | [QEDiscIDF25Good](./microblog/runs.md#qediscidf25good) | [DFRBase](./microblog/runs.md#dfrbase) | [QEClustIDF](./microblog/runs.md#qeclustidf)

??? abstract "Abstract"
	
	TREC 2013, we participated in the ad-hoc search task of the Microblog Track. The Microblog track, which is in its third consecutive year, has remained very similar to the last two. This paper describes the approaches we have implemented for Tweet retrieval, which comprehend query expansion, and baseline model selection. The results for all the runs submitted are well above the median achieved for all the automatic runs submitted to TREC. Furthermore, statistically significant improvements in terms of precision at 30, are reported for our automatic query expansion approach with respect to the baseline we chose. The methods here proposed show great potential for enhancing tweet retrieval performance and should therefore be further studied.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PerezMJ13.bib) "
	```
	@inproceedings{DBLP:conf/trec/PerezMJ13,
		author = {Jesus A. Rodriguez Perez and Andrew James McMinn and Joemon M. Jose},
		editor = {Ellen M. Voorhees},
		title = {University of Glasgow (UoG{\_}TwTeam) at {TREC} Microblog 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/TwTeam-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PerezMJ13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKUICST at TREC 2013 Microblog Track

_Runwei Qiang, Yue Fei, Yihong Hong, Jianwu Yang_

- :fontawesome-solid-user-group: **Participant:** [PKUICST](./microblog/participants.md#pkuicst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/PKUICST-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/PKUICST-microblog.pdf)
- :material-file-search: **Runs:** [PKUICST1](./microblog/runs.md#pkuicst1) | [PKUICST2](./microblog/runs.md#pkuicst2) | [PKUICST3](./microblog/runs.md#pkuicst3) | [PKUICST4](./microblog/runs.md#pkuicst4)

??? abstract "Abstract"
	
	This paper describes PKUICST's entry into the TREC 2013 Microblog track. In this year of microblog track, we designed and conducted a series of experiments based on both our local crawled collection and the official track API. For runs with local crawled dataset, we exploited different retrieval models, such as TFIDF, Okapi BM25 and statistic language model and tuned optimal parameters for all these models with the dataset in TREC 2012. Furthermore, we attempted to combine these models to gain a better performance with the help of learning to rank framework. For runs with the official track API, we employed language model with two-stage pseudo feedback query expansion. In addition, a filtering component was adopted to refine the results retrieved by the expanded query. Experimental results demonstrate that our approach obtains convincing performances.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiangFHY13.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiangFHY13,
		author = {Runwei Qiang and Yue Fei and Yihong Hong and Jianwu Yang},
		editor = {Ellen M. Voorhees},
		title = {{PKUICST} at {TREC} 2013 Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/PKUICST-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiangFHY13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CIRGIRDISCO at TREC 2013 Microblog Track

_Muhammad Atif Qureshi, Colm O'Riordan, Gabriella Pasi_

- :fontawesome-solid-user-group: **Participant:** [CIRG_IRDISCO](./microblog/participants.md#cirg_irdisco)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/NUIG-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/NUIG-microblog.pdf)
- :material-file-search: **Runs:** [CIRGIRDISCO2](./microblog/runs.md#cirgirdisco2) | [CIRGIRDISCO3](./microblog/runs.md#cirgirdisco3) | [CIRGIRDISCO4](./microblog/runs.md#cirgirdisco4)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2013 Microblog real-time search task. We utilized a query expansion approach and submitted three runs: one without using any form of external evidence and the remaining two runs utilize extended abstracts of Wikipedia articles.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QureshiOP13.bib) "
	```
	@inproceedings{DBLP:conf/trec/QureshiOP13,
		author = {Muhammad Atif Qureshi and Colm O'Riordan and Gabriella Pasi},
		editor = {Ellen M. Voorhees},
		title = {{CIRGIRDISCO} at {TREC} 2013 Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/NUIG-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QureshiOP13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Tie-breaker: A New Perspective of Ranking and Evaluation for Microblog  Retrieval

_Yue Wang, Jerry Darko, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./microblog/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/udel_fang-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/udel_fang-microblog.pdf)
- :material-file-search: **Runs:** [UDInfoMB](./microblog/runs.md#udinfomb) | [UDInfoMTB1](./microblog/runs.md#udinfomtb1) | [UDInfoMTB2](./microblog/runs.md#udinfomtb2) | [UDInfoMINT](./microblog/runs.md#udinfomint)

??? abstract "Abstract"
	
	Microblog retrieval is the key tool that enables users to access the relevant information from the enormous tweets posted on social media. Due to the differences of the tweets and traditional documents, existing IR models might not be the optimal choice for this problem. In this paper, we aim to introduce a new idea, i.e., tie-breaking, and discuss its implication in ranking methods and evaluation measures for microblog retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangDF13.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangDF13,
		author = {Yue Wang and Jerry Darko and Hui Fang},
		editor = {Ellen M. Voorhees},
		title = {Tie-breaker: {A} New Perspective of Ranking and Evaluation for Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/udel\_fang-microblog.pdf},
		timestamp = {Thu, 17 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WangDF13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2013 Microblog Track

_Zhen Yang, Guangyuan Zhang, Shuyong Si, Yingxu Lai, Kefeng Fan_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./microblog/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/BJUT-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/BJUT-microblog.pdf)
- :material-file-search: **Runs:** [BJUTFreq](./microblog/runs.md#bjutfreq) | [BJUTEntr](./microblog/runs.md#bjutentr) | [BJUTCnor](./microblog/runs.md#bjutcnor)

??? abstract "Abstract"
	
	This paper describes the first participation of BJUT in the TREC Micro-blog Track 2013. We perform the experiments on the 2013 TREC Microblog data using the standard retrieval model with several different query expansion methods including frequency method, C measure and Entropy differences. Also we introduce the details of our system, which consists of data preprocessing, retrieval structure, and query expansion & results analysis module.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangZSLF13.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangZSLF13,
		author = {Zhen Yang and Guangyuan Zhang and Shuyong Si and Yingxu Lai and Kefeng Fan},
		editor = {Ellen M. Voorhees},
		title = {{BJUT} at {TREC} 2013 Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/BJUT-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangZSLF13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2013 Microblog Track

_Siming Zhu, Zhe Gao, Yajing Yuan, Hui Wang, Guang Chen_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./microblog/participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/PRIS-microblog.pdf](http://trec.nist.gov/pubs/trec22/papers/PRIS-microblog.pdf)
- :material-file-search: **Runs:** [PrisRun1](./microblog/runs.md#prisrun1) | [PrisRun2](./microblog/runs.md#prisrun2) | [PrisRun4](./microblog/runs.md#prisrun4) | [PrisRun3](./microblog/runs.md#prisrun3)

??? abstract "Abstract"
	
	This paper described the real-time search system we built for TREC 2013 microblog track. We focused on query expansion and ranking algorithm and employed different strategies. For query expansion, we implied pseudo-relevance feedback using WAF algorithms and a refined tf*idf formula. For re-ranking part, our system makes use of various tweets' features, such as expansion terms, URL information, and incorporate them in a learning-to-rank framework to improve the final ranking results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuGYWC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuGYWC13,
		author = {Siming Zhu and Zhe Gao and Yajing Yuan and Hui Wang and Guang Chen},
		editor = {Ellen M. Voorhees},
		title = {{PRIS} at {TREC} 2013 Microblog Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/PRIS-microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuGYWC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Temporal Summarization 

#### TREC 2013 Temporal Summarization

_Javed A. Aslam, Matthew Ekstrand-Abueg, Virgil Pavlu, Fernando Diaz, Tetsuya Sakai_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/TS.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/TS.OVERVIEW.pdf)
??? abstract "Abstract"
	
	Unexpected news events such as earthquakes or natural disasters represent a unique information access problem where traditional approaches fail. For example, immediately after an event, the corpus may be sparsely populated with relevant content. Even when, after a few hours, relevant content is available, it is often inaccurate or highly redundant. At the same time, crisis events demonstrate a scenario where users urgently need information, especially if they are directly affected by the event. The goal of this track is to develop systems for efficiently monitoring the information associated with an event over time. Specifically, we are interested in developing systems which (1) can broadcast short, relevant, and reliable sentence-length updates about a developing event and (2) can track the value of important event-related attributes (e.g. number of fatalities). The track has the following goals, to develop algorithms which detect sub-events with low latency, to model information reliability in the presence of a dynamic corpus, to understand and address the sensitivity of text summarization algorithms in an online, sequential setting, and to understand and address the sensitivity of information extraction algorithms in dynamic settings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AslamEPDS13.bib) "
	```
	@inproceedings{DBLP:conf/trec/AslamEPDS13,
		author = {Javed A. Aslam and Matthew Ekstrand{-}Abueg and Virgil Pavlu and Fernando Diaz and Tetsuya Sakai},
		editor = {Ellen M. Voorhees},
		title = {{TREC} 2013 Temporal Summarization},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/TS.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AslamEPDS13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at the TREC 2013 Temporal Summarization Track

_Gaurav Baruah, Rakesh Guttikonda, Adam Roegiest, Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./tempsumm/participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/waterloomds-ts.pdf](http://trec.nist.gov/pubs/trec22/papers/waterloomds-ts.pdf)
- :material-file-search: **Runs:** [CosineEgrep](./tempsumm/runs.md#cosineegrep) | [NormEgrep](./tempsumm/runs.md#normegrep) | [UWMDSqlec2t25](./tempsumm/runs.md#uwmdsqlec2t25) | [UWMDSqlec4t50](./tempsumm/runs.md#uwmdsqlec4t50) | [rg1](./tempsumm/runs.md#rg1) | [rg3](./tempsumm/runs.md#rg3) | [rg2](./tempsumm/runs.md#rg2) | [rg4](./tempsumm/runs.md#rg4)

??? abstract "Abstract"
	
	The University of Waterloo participated in the Temporal Summarization Track at TREC 2013 and submitted 8 runs for the Sequential Update Summarization Task. Methods like query likelihood ranking, pseudo relevance feedback, BM25 and cosine similarity, as well as, algorithms for passage retrieval and term expansion using distributional similarity to a set of seed words, were used for returning relevant sentences from a stream of time-ordered documents. Higher scores relative to the average score for all submitted runs were achieved on the Latency Comprehensiveness Metric (returning as many nuggets as possible), however, submitted runs performed poorly on the Expected Latency Gain Metric (speediness of updates).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BaruahGRV13.bib) "
	```
	@inproceedings{DBLP:conf/trec/BaruahGRV13,
		author = {Gaurav Baruah and Rakesh Guttikonda and Adam Roegiest and Olga Vechtomova},
		editor = {Ellen M. Voorhees},
		title = {University of Waterloo at the {TREC} 2013 Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/waterloomds-ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BaruahGRV13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Temporal Summarization Track TREC 2013

_Qian Liu, Yue Liu, Dayong Wu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./tempsumm/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/ICTNET-ts.pdf](http://trec.nist.gov/pubs/trec22/papers/ICTNET-ts.pdf)
- :material-file-search: **Runs:** [run1](./tempsumm/runs.md#run1) | [run2](./tempsumm/runs.md#run2) | [ValueTask](./tempsumm/runs.md#valuetask)

??? abstract "Abstract"
	
	This paper describes our participation in temporal summarization track of TREC2013. All runs are submitted for both two tasks, namely sequential update summarization task and value tracking task. A real-time framework was proposed based on a trigger model. This model consists of two parts. One is selecting the relevant documents by searching on the document titles. The other is obtaining import sentences to an event. Using the KBA 2013 English-and-unknown-language stream corpus, the experimental results show the effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuLWC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuLWC13,
		author = {Qian Liu and Yue Liu and Dayong Wu and Xueqi Cheng},
		editor = {Ellen M. Voorhees},
		title = {{ICTNET} at Temporal Summarization Track {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/ICTNET-ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuLWC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ZZISTI at TREC2013 Temporal Summarization Track

_Yaoyi Xi, Bicheng Li, Jie Zhou, Yongwang Tang_

- :fontawesome-solid-user-group: **Participant:** [wim_GY_2013](./tempsumm/participants.md#wim_gy_2013)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/wim-ts.pdf](http://trec.nist.gov/pubs/trec22/papers/wim-ts.pdf)
- :material-file-search: **Runs:** [SUS1](./tempsumm/runs.md#sus1) | [VT1](./tempsumm/runs.md#vt1) | [VT2](./tempsumm/runs.md#vt2)

??? abstract "Abstract"
	
	Our team submitted runs for the first running of the TREC Temporal Summarization track. TS Track at TREC2013 contains two tasks, namely Sequential update Summarization and value tracking. Our Systems to each task are described in this paper respectively. In particular, Stanford CoreNLP was applied to extract the event attributes.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XiLZT13.bib) "
	```
	@inproceedings{DBLP:conf/trec/XiLZT13,
		author = {Yaoyi Xi and Bicheng Li and Jie Zhou and Yongwang Tang},
		editor = {Ellen M. Voorhees},
		title = {{ZZISTI} at {TREC2013} Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/wim-ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XiLZT13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HLTCOE at TREC 2013: Temporal Summarization

_Tan Xu, Douglas W. Oard, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [hltcoe](./tempsumm/participants.md#hltcoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/hltcoe-ts.pdf](http://trec.nist.gov/pubs/trec22/papers/hltcoe-ts.pdf)
- :material-file-search: **Runs:** [Baseline](./tempsumm/runs.md#baseline) | [BasePred](./tempsumm/runs.md#basepred) | [EXTERNAL](./tempsumm/runs.md#external) | [TuneExternal2](./tempsumm/runs.md#tuneexternal2) | [TuneBasePred2](./tempsumm/runs.md#tunebasepred2)

??? abstract "Abstract"
	
	Our team submitted runs for the first running of the TREC Temporal Summarization track. We focused on the Sequential Update Summarization task. This task involves simulating processing a temporally ordered stream of over 1 billion documents to identify sentences that are relevant to a specific breaking news stories which contain new and important content. In this paper, we describe our approach and evaluation results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuOM13.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuOM13,
		author = {Tan Xu and Douglas W. Oard and Paul McNamee},
		editor = {Ellen M. Voorhees},
		title = {{HLTCOE} at {TREC} 2013: Temporal Summarization},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/hltcoe-ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuOM13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2013 Temporal Summarization Track

_Zhen Yang, Fei Yao, Huayang Sun, Yun Zhao, Yingxu Lai, Kefeng Fan_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./tempsumm/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/BJUT-ts.pdf](http://trec.nist.gov/pubs/trec22/papers/BJUT-ts.pdf)
- :material-file-search: **Runs:** [Q0](./tempsumm/runs.md#q0) | [Q1](./tempsumm/runs.md#q1) | [Q2](./tempsumm/runs.md#q2)

??? abstract "Abstract"
	
	This paper describes the first participation of BJUT in the TREC Temporal Summarization Track 2013. Since this is the first track which is held on temporal summarization, the traditional text retrieval framework is introduced to solve the newly emerging temporal summarization problem at first, and the conventional approach is found that it doesn't work without any consideration on extra expansion information to lose the retrieval limits. Therefore, the baseline is improved by considering the expansion information over the summarization, which includes the use of query expansion based on time/similarity factors, summarization based on information clusters and so on. We do not intend to identify specific methods for solutions. Rather a list of method is presented in capabilities where it is anticipated the methods are likely to adapt over time. Surprisingly, we find the traditional text retrieval methods with default parameters, such as tf-idf model, BM25 model, perform very well and can be used in many areas. Meanwhile some expansion information methods, such as k-means, show complex performance and their parameters need to be chosen carefully to achieve better performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYSZLF13.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYSZLF13,
		author = {Zhen Yang and Fei Yao and Huayang Sun and Yun Zhao and Yingxu Lai and Kefeng Fan},
		editor = {Ellen M. Voorhees},
		title = {{BJUT} at {TREC} 2013 Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/BJUT-ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangYSZLF13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Information Extraction Systems of PRIS at Temporal Summarization  Track

_Chunyun Zhang, Weiyan Xu, Fanyu Meng, Hongyan Li, Tong Wu, Lixin Xu_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./tempsumm/participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/PRIS-ts.pdf](http://trec.nist.gov/pubs/trec22/papers/PRIS-ts.pdf)
- :material-file-search: **Runs:** [cluster1](./tempsumm/runs.md#cluster1) | [cluster2](./tempsumm/runs.md#cluster2) | [cluster3](./tempsumm/runs.md#cluster3) | [cluster4](./tempsumm/runs.md#cluster4) | [PRISTS1](./tempsumm/runs.md#prists1) | [PRISTS2](./tempsumm/runs.md#prists2) | [cluster5](./tempsumm/runs.md#cluster5) | [PRISTS3](./tempsumm/runs.md#prists3)

??? abstract "Abstract"
	
	This paper describes the information extraction systems of PRIS at Temporal Summarization Track. The Temporal Summarization Track includes two tasks: sequential update summarization and value tracking. For the first task, we focus attention on keywords mining and sentence scoring. The system utilizes hierarchical Latent Dirichlet Allocation (LDA) to do keywords mining and score sentences with keywords shooting method. For the second task, we define the value extracting as a sequence labeling problem and build a discriminative undirected graph model (CRF model) to extract attribute values of all topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangXMLWX13.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangXMLWX13,
		author = {Chunyun Zhang and Weiyan Xu and Fanyu Meng and Hongyan Li and Tong Wu and Lixin Xu},
		editor = {Ellen M. Voorhees},
		title = {The Information Extraction Systems of {PRIS} at Temporal Summarization Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/PRIS-ts.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangXMLWX13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2013: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Web Tracks

_Richard McCreadie, M-Dyaa Albakour, Stuart Mackie, Nut Limsopatham, Craig Macdonald, Iadh Ounis, Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./tempsumm/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf](http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf)
- :material-file-search: **Runs:** [uogTrNMM](./tempsumm/runs.md#uogtrnmm) | [uogTrNSQ1](./tempsumm/runs.md#uogtrnsq1) | [uogTrEMMQ2](./tempsumm/runs.md#uogtremmq2) | [uogTrNMTm1MM3](./tempsumm/runs.md#uogtrnmtm1mm3) | [uogTrNMTm3FMM4](./tempsumm/runs.md#uogtrnmtm3fmm4)

??? abstract "Abstract"
	
	In TREC 2013, we focus on tackling the challenges posed by the new Contextual Suggestion and Temporal summarisation tracks, as well as enhancing our existing technologies to tackle the new risk-sensitive aspect of the Web track, building upon our Terrier Information Retrieval Platform. In particular, for the Contextual Suggestion track, we investigate how to exploit location-based social networks, with the aim of better identifying venues within a city that a given user might be interested in visiting. For the Temporal Summarisation track, we propose a new summarisation framework and investigate novel techniques to adaptively alter the summarisation strategy over time. For the TREC Web track, we continue to build upon our learning-to-rank approaches and novel xQuAD / Fat frameworks within Terrier, increasing effectiveness when ranking and examining two new approaches to risk-sensitive retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieAMLMOD13.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieAMLMOD13,
		author = {Richard McCreadie and M{-}Dyaa Albakour and Stuart Mackie and Nut Limsopatham and Craig Macdonald and Iadh Ounis and Bekir Taner Din{\c{c}}er},
		editor = {Ellen M. Voorhees},
		title = {University of Glasgow at {TREC} 2013: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Web Tracks},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieAMLMOD13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Session 

#### Overview of the TREC 2013 Session Track

_Ben Carterette, Ashraf Bah, Evangelos Kanoulas, Mark M. Hall, Paul D. Clough_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/SESSION.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/SESSION.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Session track ran for the fourth time in 2013. The track has the primary goal of providing test collections and evaluation measures for studying information retrieval over user sessions rather than one-time queries. These test collections are meant to be portable, reusable, statistically powerful, and open to anyone that wishes to work on the problem of retrieval over sessions. The experimental design of the track was similar to that of the previous two years [4, 5]: sessions were real user sessions with a search engine that include queries, retrieved results, clicks, and dwell times; retrieval tasks were designed to study the effect of using session data in retrieval for only the mth query in a session. Changes from last year's track include: 1. a new set of topics; 2. a new corpus (ClueWeb12); 3. a new search system for collecting session data; 4. a small change in the retrieval tasks. This overview is organized as follows: in Section 2 we describe the tasks participants were to perform. In Section 3 we describe the corpus, topics, and sessions that comprise the test collection. Section 4 gives some information about submitted runs. In Section 5 we describe relevance judging and evaluation measures, and Sections 6 present evaluation results and analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarteretteBKHC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarteretteBKHC13,
		author = {Ben Carterette and Ashraf Bah and Evangelos Kanoulas and Mark M. Hall and Paul D. Clough},
		editor = {Ellen M. Voorhees},
		title = {Overview of the {TREC} 2013 Session Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/SESSION.OVERVIEW.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarteretteBKHC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Session Track TREC 2013

_Zhenhong Chen, Long Xia, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./session/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/ICTNET-session.pdf](http://trec.nist.gov/pubs/trec22/papers/ICTNET-session.pdf)
- :material-file-search: **Runs:** [ICTNET13SER1.RL1](./session/runs.md#ictnet13ser1.rl1) | [ICTNET13SER1.RL2](./session/runs.md#ictnet13ser1.rl2) | [ICTNET13SER1.RL3](./session/runs.md#ictnet13ser1.rl3) | [ICTNET13SER2.RL1](./session/runs.md#ictnet13ser2.rl1) | [ICTNET13SER2.RL2](./session/runs.md#ictnet13ser2.rl2) | [ICTNET13SER2.RL3](./session/runs.md#ictnet13ser2.rl3) | [ICTNET13SER3.RL1](./session/runs.md#ictnet13ser3.rl1) | [ICTNET13SER3.RL2](./session/runs.md#ictnet13ser3.rl2) | [ICTNET13SER3.RL3](./session/runs.md#ictnet13ser3.rl3)

??? abstract "Abstract"
	
	In this paper, we describe our solutions to the Session Track at TREC 2013. There are three main differences compared to our last year's submission[2]. Firstly, we use Indri[3] to build our retrieval system. Due to computing resource limited, we only index the Category B collection. Secondly, we try to take advantage of FreeBase[4] to recognize the entities in the given query and then weight each term or phrase accordingly. Lastly, we discard the Google virtual document and page rank features from our last year's learning to rank model. The rest of this paper is organized as follows.We detail our research structure in section 2. Section 3 describes our experiments and evaluation results. Conclusions are made in the last section.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenXYLC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenXYLC13,
		author = {Zhenhong Chen and Long Xia and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees},
		title = {{ICTNET} at Session Track {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/ICTNET-session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenXYLC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pitt at TREC 2013: Different Effects of Click-through and Past Queries  on Whole-session Search Performance

_Jiepu Jiang, Daqing He_

- :fontawesome-solid-user-group: **Participant:** [PITT](./session/participants.md#pitt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/pitt-session.pdf](http://trec.nist.gov/pubs/trec22/papers/pitt-session.pdf)
- :material-file-search: **Runs:** [FixInt28.RL1](./session/runs.md#fixint28.rl1) | [FixInt28.RL2](./session/runs.md#fixint28.rl2) | [FixInt28.RL3](./session/runs.md#fixint28.rl3) | [FixInt28N.RL1](./session/runs.md#fixint28n.rl1) | [FixInt28N.RL2](./session/runs.md#fixint28n.rl2) | [FixInt28N.RL3](./session/runs.md#fixint28n.rl3) | [FixInt58.RL1](./session/runs.md#fixint58.rl1) | [FixInt58.RL2](./session/runs.md#fixint58.rl2) | [FixInt58.RL3](./session/runs.md#fixint58.rl3) | [FixInt58N.RL1](./session/runs.md#fixint58n.rl1) | [FixInt58N.RL2](./session/runs.md#fixint58n.rl2) | [FixInt58N.RL3](./session/runs.md#fixint58n.rl3) | [KM1.RL1](./session/runs.md#km1.rl1) | [KM1.RL2](./session/runs.md#km1.rl2) | [KM1.RL3](./session/runs.md#km1.rl3) | [KM1N.RL1](./session/runs.md#km1n.rl1) | [KM1N.RL2](./session/runs.md#km1n.rl2) | [KM1N.RL3](./session/runs.md#km1n.rl3)

??? abstract "Abstract"
	
	Past search queries and click-through information within a search session have been heavily exploited to improve search performance. However, it remains unclear how do these two data source contribute to whole-session search performance due to the lack of reliable evaluation approaches. For example, as pointed out in our last year's report [2], using past search queries as positive relevance feedback information can make search results of the current query similar to previous queries' results. Such issues cannot be disclosed by evaluation metrics such as nDCG@10. Therefore, in this paper, we focus on analyzing the effects of past queries and click-through information on whole-session search performance. We adopted alternative evaluation approaches other than the TREC official ones. We found that past queries may seemingly enhance nDCG@10 by retrieving previously returned results, which is difficult to result in real improvements of whole-session search performance; in comparison, click-through can enhance search performance without sacrificing search novelty, consequently leading to improved search performance across the whole session. However, after appropriate demotion of repeated results, both past queries and click-through can improve search performance while balancing novelty of results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangH13a.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangH13a,
		author = {Jiepu Jiang and Daqing He},
		editor = {Ellen M. Voorhees},
		title = {Pitt at {TREC} 2013: Different Effects of Click-through and Past Queries on Whole-session Search Performance},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/pitt-session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangH13a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Applying the Query Change Retrieval Model on Session Search-Georgetown  at TREC 2013 Session Track

_Sicong Zhang, Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [GeorgetownYang](./session/participants.md#georgetownyang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/georgetown-session.pdf](http://trec.nist.gov/pubs/trec22/papers/georgetown-session.pdf)
- :material-file-search: **Runs:** [GUrun1.RL1](./session/runs.md#gurun1.rl1) | [GUrun1.RL2](./session/runs.md#gurun1.rl2) | [GUrun1.RL3](./session/runs.md#gurun1.rl3) | [GUrun3.RL1](./session/runs.md#gurun3.rl1) | [GUrun3.RL2](./session/runs.md#gurun3.rl2) | [GUrun3.RL3](./session/runs.md#gurun3.rl3) | [GUrun2.RL1](./session/runs.md#gurun2.rl1) | [GUrun2.RL2](./session/runs.md#gurun2.rl2) | [GUrun2.RL3](./session/runs.md#gurun2.rl3)

??? abstract "Abstract"
	
	In TREC 2013 Session Track, we experiment the Query Change Model (QCM) for session search on the new document collection ClueWeb12 CatB. We use structured query formulation and pseudo-relevance feedback for RL1. The QCM approach is used in RL2 and it studies query change between adjacent queries and models session search as a Markov Decision Process. We further add information from other sessions by a majority vote of cross-session clicked data to the model in RL3. Comparing the retrieval accuracy in RL1 with that in RL2 and RL3, we obtain 46.1% and 46.6% improvements, respectively. We present an analysis and discussion on the dataset difference between ClueWeb12 Cat A and Cat B, the difference between TREC2012 and TREC2013 session, and their impact on the retrieval accuracy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangY13.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangY13,
		author = {Sicong Zhang and Hui Yang},
		editor = {Ellen M. Voorhees},
		title = {Applying the Query Change Retrieval Model on Session Search-Georgetown at {TREC} 2013 Session Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/georgetown-session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangY13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2013-Session and Web Track

_Matthias Hagen, Michael Völske, Jakob Gomoll, Marie Bornemann, Lene Ganschow, Florian Kneist, Abdul Hamid Sabri, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [webis](./session/participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/webis-session-web.pdf](http://trec.nist.gov/pubs/trec22/papers/webis-session-web.pdf)
- :material-file-search: **Runs:** [webisS1.RL1](./session/runs.md#webiss1.rl1) | [webisS1.RL2](./session/runs.md#webiss1.rl2) | [webisS1.RL3](./session/runs.md#webiss1.rl3) | [webisS2.RL1](./session/runs.md#webiss2.rl1) | [webisS2.RL2](./session/runs.md#webiss2.rl2) | [webisS2.RL3](./session/runs.md#webiss2.rl3) | [webisS3.RL1](./session/runs.md#webiss3.rl1) | [webisS3.RL2](./session/runs.md#webiss3.rl2) | [webisS3.RL3](./session/runs.md#webiss3.rl3)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2013 Session and Web tracks. All our runs are on the full ClueWeb12 and use the online Indri retrieval system hosted at CMU. As for the session track, our runs implement three main ideas that were slightly improved compared to our participation in 2012: (1) distinguishing low risk sessions where we want to involve session knowledge in the form of a conservative query expansion strategy (only few expansion terms based on keywords from previous queries and seen/clicked documents/titles/snippets) from those where we don't, (2) conservative query expansion based on similar sessions from other users, (3) result list postprocessing to boost clicked documents of other users in similar sessions. As these techniques leave a lot of queries unchanged when not enough session knowledge is available, we do not expect large gains over all the sessions. As for the Web track, our runs exploit different strategies of segmenting the queries (i.e., identifying and highlighting concepts within the query as phrases to be contained in the results). Additionally to algorithmic segmentations based on our WWW 2011 and CIKM 2012 ideas, we had one run where we chose the segmentation according to a majority vote amongst five humans. In a last run, the results are constructed so as to be disjunct from the track's baseline's and our other runs' results. Instead, we populate the result list with documents that different segmentations of the query would return top-ranked or that are deeper in the ranking for segmentations already chosen in previous runs. The underlying idea was to obtain at least some judgments for the top documents that other segmentations would bring up in their rankings. As most of the queries are rather short, we expect only slight improvements or no effect at all from the different segmentation strategies that are tailored to longer and more verbose queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenVGBGKSS13.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenVGBGKSS13,
		author = {Matthias Hagen and Michael V{\"{o}}lske and Jakob Gomoll and Marie Bornemann and Lene Ganschow and Florian Kneist and Abdul Hamid Sabri and Benno Stein},
		editor = {Ellen M. Voorhees},
		title = {Webis at {TREC} 2013-Session and Web Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/webis-session-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenVGBGKSS13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Crowdsourcing 

#### Overview of the TREC 2013 Crowdsourcing Track

_Mark D. Smucker, Gabriella Kazai, Matthew Lease_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/CROWD.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/CROWD.OVERVIEW.pdf)
??? abstract "Abstract"
	
	n 2013, the Crowdsourcing track partnered with the TREC Web Track and had a single task to crowdsource relevance judgments for a set of Web pages and search topics shared by the Web Track. This track overview describes the track and provides analysis of the track's results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmuckerKRL13.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmuckerKRL13,
		author = {Mark D. Smucker and Gabriella Kazai and Matthew Lease},
		editor = {Ellen M. Voorhees},
		title = {Overview of the {TREC} 2013 Crowdsourcing Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/CROWD.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmuckerKRL13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Northeastern University Runs at the TREC13 Crowdsourcing Track

_Maryam Bashir, Jesse Anderton, Virgil Pavlu, Javed A. Aslam_

- :fontawesome-solid-user-group: **Participant:** [NEUIR](./crowd/participants.md#neuir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/northeastern-crowd.pdf](http://trec.nist.gov/pubs/trec22/papers/northeastern-crowd.pdf)
- :material-file-search: **Runs:** [NEUPivot1](./crowd/runs.md#neupivot1)

??? abstract "Abstract"
	
	The goal of the TREC 2013 Crowdsourcing Track was to evaluate approaches to crowdsourcing high quality relevance judgments for web pages and search topics. This paper describes our submission to Crowdsourcing track. Participants of this track were required to assess documents judged on a six-point scale. Our approach is based on collecting a linear number of preference judgements, and combining these into nominal grades using a modified version of QuickSort algorithm.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BashirAPA13.bib) "
	```
	@inproceedings{DBLP:conf/trec/BashirAPA13,
		author = {Maryam Bashir and Jesse Anderton and Virgil Pavlu and Javed A. Aslam},
		editor = {Ellen M. Voorhees},
		title = {Northeastern University Runs at the {TREC13} Crowdsourcing Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/northeastern-crowd.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BashirAPA13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Hrbust in TREC 2013: Crowdsourcing Track

_Li Peng, Sun Bo-yu, Liu Yang, Zhang Tingting_

- :fontawesome-solid-user-group: **Participant:** [Hrbust](./crowd/participants.md#hrbust)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/Hrbust-crowd.pdf](http://trec.nist.gov/pubs/trec22/papers/Hrbust-crowd.pdf)
- :material-file-search: **Runs:** [Hrbust123](./crowd/runs.md#hrbust123)

??? abstract "Abstract"
	
	In the practical application of crowdsourcing, some unreliable workers have emerged due to profit driven. Their results seriously reduce the quality and bring about the initiator's judgment biases. In this paper, we creatively put forward a crowdsourcing fraud detection method based on psychological behavior analysis to find out the spammer according to the psychological difference between deception and reliable behavior by means of Ebbinghaus forgetting curve. Furthermore, we constructed an online crowdsourcing experiment platform to verify the validity of our method. In addition, we participated in TREC 2013 Crowdsourcing Track and the organizer provided the evaluation results for our run. As a result, APCorr, RMSE and GAP attained 0.480, 0.135 and 0.392 respectively. Evaluation and xperimental results show that our method is effective and feasible.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PengBYT13.bib) "
	```
	@inproceedings{DBLP:conf/trec/PengBYT13,
		author = {Li Peng and Sun Bo{-}yu and Liu Yang and Zhang Tingting},
		editor = {Ellen M. Voorhees},
		title = {Hrbust in {TREC} 2013: Crowdsourcing Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/Hrbust-crowd.pdf},
		timestamp = {Sun, 03 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PengBYT13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

