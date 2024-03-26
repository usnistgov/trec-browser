# Proceedings - Temporal Summarization 2015 

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

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/IRIT-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/IRIT-TS.pdf)
- :material-file-search: **Runs:** [FS1A](./runs.md#fs1a) | [OS1C](./runs.md#os1c) | [FS2A](./runs.md#fs2a) | [FS3A](./runs.md#fs3a) | [FS4A](./runs.md#fs4a) | [OS2C](./runs.md#os2c) | [FS5A](./runs.md#fs5a) | [OS3C](./runs.md#os3c) | [FS6A](./runs.md#fs6a) | [OS4C](./runs.md#os4c) | [OS1A](./runs.md#os1a) | [OS2A](./runs.md#os2a) | [OS3A](./runs.md#os3a) | [OS5C](./runs.md#os5c) | [OS6C](./runs.md#os6c) | [OS7C](./runs.md#os7c) | [OS8C](./runs.md#os8c) | [FS1B](./runs.md#fs1b) | [FS2B](./runs.md#fs2b) | [FS3B](./runs.md#fs3b) | [FS4B](./runs.md#fs4b)

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

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/udel_fang-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/udel_fang-TS.pdf)
- :material-file-search: **Runs:** [WikiProfMix1](./runs.md#wikiprofmix1) | [WikiProfMixFS1](./runs.md#wikiprofmixfs1) | [WikiOnlyFS2](./runs.md#wikionlyfs2) | [WikiOnly2](./runs.md#wikionly2) | [ProfOnlyFS3](./runs.md#profonlyfs3) | [ProfOnly3](./runs.md#profonly3)

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

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-TS.pdf)
- :material-file-search: **Runs:** [UWCTSRun1](./runs.md#uwctsrun1) | [UWCTSRun2](./runs.md#uwctsrun2) | [UWCTSRun3](./runs.md#uwctsrun3) | [UWCTSRun4](./runs.md#uwctsrun4) | [UWCTSRun5](./runs.md#uwctsrun5) | [UWCTSRun6](./runs.md#uwctsrun6)

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

- :fontawesome-solid-user-group: **Participant:** [CWI](./participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/CWI-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/CWI-TS.pdf)
- :material-file-search: **Runs:** [IGn](./runs.md#ign) | [IGnPrecision](./runs.md#ignprecision) | [docs](./runs.md#docs) | [titles](./runs.md#titles) | [IGnRecall](./runs.md#ignrecall) | [docsRecall](./runs.md#docsrecall)

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

- :fontawesome-solid-user-group: **Participant:** [ISCASIR](./participants.md#iscasir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/ISCASIR-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/ISCASIR-TS.pdf)
- :material-file-search: **Runs:** [runvec1](./runs.md#runvec1) | [runvec2](./runs.md#runvec2)

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

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/BJUT-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/BJUT-TS.pdf)
- :material-file-search: **Runs:** [DMSL1NMF2](./runs.md#dmsl1nmf2) | [DMSL1AP1](./runs.md#dmsl1ap1) | [DMSL1VSH3](./runs.md#dmsl1vsh3) | [DMSL2N2](./runs.md#dmsl2n2) | [DMSL2A1](./runs.md#dmsl2a1) | [DMSL2V3](./runs.md#dmsl2v3)

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

- :fontawesome-solid-user-group: **Participant:** [AIPHES](./participants.md#aiphes)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/AIPHES-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/AIPHES-TS.pdf)
- :material-file-search: **Runs:** [Run1](./runs.md#run1) | [Run2](./runs.md#run2) | [Run4](./runs.md#run4) | [Run3](./runs.md#run3)

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

- :fontawesome-solid-user-group: **Participant:** [USI](./participants.md#usi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/USI-CXTS.pdf](http://trec.nist.gov/pubs/trec24/papers/USI-CXTS.pdf)
- :material-file-search: **Runs:** [InL2DecrQE1ID1](./runs.md#inl2decrqe1id1) | [InL2DecrQE2ID2](./runs.md#inl2decrqe2id2) | [InL2StabQE2ID3](./runs.md#inl2stabqe2id3) | [InL2IncrQE2ID4](./runs.md#inl2incrqe2id4) | [InL2DocsQE2ID5](./runs.md#inl2docsqe2id5) | [InL2StabQE1ID6](./runs.md#inl2stabqe1id6) | [InL2IncrQE1ID7](./runs.md#inl2incrqe1id7)

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

- :fontawesome-solid-user-group: **Participant:** [UvA.ILPS](./participants.md#uva.ilps)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/UvA.ILPS-TS.pdf](http://trec.nist.gov/pubs/trec24/papers/UvA.ILPS-TS.pdf)
- :material-file-search: **Runs:** [TF](./runs.md#tf) | [TFISF](./runs.md#tfisf) | [QL](./runs.md#ql) | [LLR](./runs.md#llr) | [LDA](./runs.md#lda) | [LexRank](./runs.md#lexrank) | [LM](./runs.md#lm) | [TFW2V](./runs.md#tfw2v) | [TFISFW2V](./runs.md#tfisfw2v) | [LDAv2](./runs.md#ldav2) | [QLLP](./runs.md#qllp) | [TFW](./runs.md#tfw) | [TFISFW](./runs.md#tfisfw) | [QLF](./runs.md#qlf) | [COSSIM](./runs.md#cossim) | [COS](./runs.md#cos) | [TFFilter](./runs.md#tffilter)

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

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf](http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf)
- :material-file-search: **Runs:** [uogTrT1MANU](./runs.md#uogtrt1manu) | [uogTrT1X2iSCP](./runs.md#uogtrt1x2iscp) | [uogTrT1X2iTCP](./runs.md#uogtrt1x2itcp) | [uogTrT1X2iNCP](./runs.md#uogtrt1x2incp) | [uogTrT1X2cSCP](./runs.md#uogtrt1x2cscp) | [uogTrT1X2iSC](./runs.md#uogtrt1x2isc) | [uogTrT2EimpP](./runs.md#uogtrt2eimpp) | [uogTrT2EintP](./runs.md#uogtrt2eintp) | [uogTrdEQR1](./runs.md#uogtrdeqr1) | [uogTrdEEQR3](./runs.md#uogtrdeeqr3) | [uogTrhEQR2](./runs.md#uogtrheqr2) | [uogTrhEEQR4](./runs.md#uogtrheeqr4) | [uogTrhSqCR6](./runs.md#uogtrhsqcr6) | [uogTrdSqCR5](./runs.md#uogtrdsqcr5)

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

