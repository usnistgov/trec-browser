# Proceedings - Knowledge Base Acceleration 2014 

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

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-IRIT_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-IRIT_kba.pdf)
- :material-file-search: **Runs:** [IRIT-alpha_10_0.25](./runs.md#irit-alpha_10_0.25) | [IRIT-alpha_10_0.5](./runs.md#irit-alpha_10_0.5) | [IRIT-alpha_10_0.75](./runs.md#irit-alpha_10_0.75) | [IRIT-alpha_50_0.25](./runs.md#irit-alpha_50_0.25) | [IRIT-alpha_50_0.5](./runs.md#irit-alpha_50_0.5) | [IRIT-alpha_50_0.75](./runs.md#irit-alpha_50_0.75) | [IRIT-alpha_100_0.25](./runs.md#irit-alpha_100_0.25) | [IRIT-alpha_100_0.5](./runs.md#irit-alpha_100_0.5) | [IRIT-alpha_100_0.75](./runs.md#irit-alpha_100_0.75) | [IRIT-VLM_10](./runs.md#irit-vlm_10) | [IRIT-VLM_50](./runs.md#irit-vlm_50) | [IRIT-VULMBuzz_10](./runs.md#irit-vulmbuzz_10) | [IRIT-VULMBuzz_50](./runs.md#irit-vulmbuzz_50) | [IRIT-ULM_10](./runs.md#irit-ulm_10) | [IRIT-ULM_50](./runs.md#irit-ulm_50) | [IRIT-alpha_50_0.75T](./runs.md#irit-alpha_50_0.75t) | [IRIT-ULMBuzz_50_0.5T](./runs.md#irit-ulmbuzz_50_0.5t) | [IRIT-ULMBuzz_50_0.7T](./runs.md#irit-ulmbuzz_50_0.7t) | [IRIT-VULMBuz_50_0.7T](./runs.md#irit-vulmbuz_50_0.7t) | [IRIT-VULMBuz_50_0.5T](./runs.md#irit-vulmbuz_50_0.5t)

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

- :fontawesome-solid-user-group: **Participant:** [LSIS](./participants.md#lsis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-LSIS_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-LSIS_kba.pdf)
- :material-file-search: **Runs:** [LSIS-AF_NU_MCE](./runs.md#lsis-af_nu_mce) | [LSIS-AF_NU_SE](./runs.md#lsis-af_nu_se) | [LSIS-AF_NU_TSE](./runs.md#lsis-af_nu_tse) | [LSIS-AF_NU_VOE](./runs.md#lsis-af_nu_voe) | [LSIS-AF_UD_MCE](./runs.md#lsis-af_ud_mce) | [LSIS-AF_UD_SE](./runs.md#lsis-af_ud_se) | [LSIS-AF_UD_TSE](./runs.md#lsis-af_ud_tse) | [LSIS-AF_UD_VOE](./runs.md#lsis-af_ud_voe) | [LSIS-AF_US_MCE](./runs.md#lsis-af_us_mce) | [LSIS-AF_US_SE](./runs.md#lsis-af_us_se) | [LSIS-AF_US_TSE](./runs.md#lsis-af_us_tse) | [LSIS-AF_US_VOE](./runs.md#lsis-af_us_voe)

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

- :fontawesome-solid-user-group: **Participant:** [UW](./participants.md#uw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UW_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UW_kba.pdf)
- :material-file-search: **Runs:** [UW-basic_single](./runs.md#uw-basic_single) | [UW-basic_multitask](./runs.md#uw-basic_multitask) | [UW-embedding_pos](./runs.md#uw-embedding_pos) | [UW-embedding_comb](./runs.md#uw-embedding_comb) | [UW-mean_stat](./runs.md#uw-mean_stat) | [UW-clu_stat_a08](./runs.md#uw-clu_stat_a08) | [UW-mean_dyn_g06](./runs.md#uw-mean_dyn_g06) | [UW-clu_dyn_a08_g04](./runs.md#uw-clu_dyn_a08_g04) | [UW-clu_dyn_nv_e](./runs.md#uw-clu_dyn_nv_e) | [UW-f_basic_single](./runs.md#uw-f_basic_single) | [UW-f_basic_multi](./runs.md#uw-f_basic_multi) | [UW-f_emb_comb](./runs.md#uw-f_emb_comb) | [UW-f_mean_stat](./runs.md#uw-f_mean_stat) | [UW-f_mean_dyn](./runs.md#uw-f_mean_dyn) | [UW-f_clust_stat](./runs.md#uw-f_clust_stat) | [UW-f_clust_dyn](./runs.md#uw-f_clust_dyn) | [UW-f_emb_pos](./runs.md#uw-f_emb_pos)

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

- :fontawesome-solid-user-group: **Participant:** [KobeU](./participants.md#kobeu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-KobeU_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-KobeU_kba.pdf)
- :material-file-search: **Runs:** [KobeU-exact_match](./runs.md#kobeu-exact_match) | [KobeU-ccr_03](./runs.md#kobeu-ccr_03) | [KobeU-ccr_08](./runs.md#kobeu-ccr_08)

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

- :fontawesome-solid-user-group: **Participant:** [SCU](./participants.md#scu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-SCU_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-SCU_kba.pdf)
- :material-file-search: **Runs:** [SCU-ssf_1](./runs.md#scu-ssf_1) | [SCU-ssf_2](./runs.md#scu-ssf_2) | [SCU-ssf_3](./runs.md#scu-ssf_3) | [SCU-ssf_4](./runs.md#scu-ssf_4) | [SCU-ssf_5](./runs.md#scu-ssf_5) | [SCU-ssf_6](./runs.md#scu-ssf_6) | [SCU-ssf_7](./runs.md#scu-ssf_7) | [SCU-ssf_8](./runs.md#scu-ssf_8) | [SCU-ssf_9](./runs.md#scu-ssf_9) | [SCU-ssf_10](./runs.md#scu-ssf_10) | [SCU-ssf_11](./runs.md#scu-ssf_11) | [SCU-ssf_12](./runs.md#scu-ssf_12) | [SCU-ssf_13](./runs.md#scu-ssf_13) | [SCU-ssf_14](./runs.md#scu-ssf_14)

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

- :fontawesome-solid-user-group: **Participant:** [BUPT_PRIS](./participants.md#bupt_pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BUPT_PRIS_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BUPT_PRIS_kba.pdf)
- :material-file-search: **Runs:** [BUPT_PRIS-pris_baseline](./runs.md#bupt_pris-pris_baseline) | [BUPT_PRIS-pris_svm](./runs.md#bupt_pris-pris_svm) | [BUPT_PRIS-pris_NN](./runs.md#bupt_pris-pris_nn) | [BUPT_PRIS-pris_rf](./runs.md#bupt_pris-pris_rf) | [BUPT_PRIS-ssf1](./runs.md#bupt_pris-ssf1) | [BUPT_PRIS-ssf2](./runs.md#bupt_pris-ssf2)

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

- :fontawesome-solid-user-group: **Participant:** [uiucGSLIS](./participants.md#uiucgslis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-uiucGSLIS-federated-kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-uiucGSLIS-federated-kba.pdf)
- :material-file-search: **Runs:** [uiucGSLIS-baseline_sf](./runs.md#uiucgslis-baseline_sf) | [uiucGSLIS-baseline_rm3](./runs.md#uiucgslis-baseline_rm3) | [uiucGSLIS-length_sf](./runs.md#uiucgslis-length_sf) | [uiucGSLIS-length_rm3](./runs.md#uiucgslis-length_rm3) | [uiucGSLIS-prevdocs_sf](./runs.md#uiucgslis-prevdocs_sf) | [uiucGSLIS-prevdocs_rm3](./runs.md#uiucgslis-prevdocs_rm3) | [uiucGSLIS-pdsrc_rm3](./runs.md#uiucgslis-pdsrc_rm3) | [uiucGSLIS-pdsrc_sf](./runs.md#uiucgslis-pdsrc_sf) | [uiucGSLIS-pdverb_sf](./runs.md#uiucgslis-pdverb_sf) | [uiucGSLIS-pdverb_rm3](./runs.md#uiucgslis-pdverb_rm3) | [uiucGSLIS-sourcelen_rm3](./runs.md#uiucgslis-sourcelen_rm3) | [uiucGSLIS-sourcelen_sf](./runs.md#uiucgslis-sourcelen_sf) | [uiucGSLIS-verbsource_rm3](./runs.md#uiucgslis-verbsource_rm3) | [uiucGSLIS-verbsource_sf](./runs.md#uiucgslis-verbsource_sf)

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

- :fontawesome-solid-user-group: **Participant:** [BIT_Purdue](./participants.md#bit_purdue)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BIT-Purdue_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BIT-Purdue_kba.pdf)
- :material-file-search: **Runs:** [BIT_Purdue-baseline](./runs.md#bit_purdue-baseline) | [BIT_Purdue-profile](./runs.md#bit_purdue-profile) | [BIT_Purdue-labeled](./runs.md#bit_purdue-labeled) | [BIT_Purdue-GlobalRank](./runs.md#bit_purdue-globalrank) | [BIT_Purdue-BinaryRank](./runs.md#bit_purdue-binaryrank) | [BIT_Purdue-GlobalClassU](./runs.md#bit_purdue-globalclassu) | [BIT_Purdue-GlobalClassV](./runs.md#bit_purdue-globalclassv) | [BIT_Purdue-GlobalClassV1](./runs.md#bit_purdue-globalclassv1)

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

- :fontawesome-solid-user-group: **Participant:** [WHU_IRGroup](./participants.md#whu_irgroup)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-WHU_IRGroup_kba.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-WHU_IRGroup_kba.pdf)
- :material-file-search: **Runs:** [WHU_IRGroup-baseline](./runs.md#whu_irgroup-baseline) | [WHU_IRGroup-BM_TF](./runs.md#whu_irgroup-bm_tf) | [WHU_IRGroup-BM_TF_3](./runs.md#whu_irgroup-bm_tf_3) | [WHU_IRGroup-CUSTOM_TF_FIXED](./runs.md#whu_irgroup-custom_tf_fixed)

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

