# Proceedings - Question Answering 2001 

#### Overview of the TREC 2001 Question Answering Track

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/qa10.pdf](http://trec.nist.gov/pubs/trec10/papers/qa10.pdf)
??? abstract "Abstract"
	
	The TREC question answering track is an effort to bring the benefits of large-scale evaluation to bear on the question answering problem. In its third year, the track continued to focus on retrieving small snippets of text that contain an answer to a question. However, several new conditions were added to increase the realism, and the difficulty, of the task. In the main task, questions were no longer guaranteed to have an answer in the collection; systems returned a response of 'NIL' to indicate their belief that no answer was present. In the new list task, systems assembled a set of instances as the response for a question, requiring the ability to distinguish among instances found in multiple documents. Another new task, the context task, required systems to track discourse objects through a series of questions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees01a.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees01a,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of the {TREC} 2001 Question Answering Track},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/qa10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees01a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC-10: Filtering, QA, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yikun Guo, Yingju Xia, Zhe Feng_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf](http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf)
- :material-file-search: **Runs:** [FDUT10Q2](./runs.md#fdut10q2)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC conference for the second time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we participate in the sub-task of adaptive and batch filtering. Vector representation and computation are heavily applied in filtering procedure. Four runs have been submitted, which includes one T10SU and one T10F run for adpative filtering, as well as another one T10SU and one T10F run for batch filtering. We have tried many natural language processing techniques in our QA system, including statistical sentence breaking, POS tagging, parsing, name entity tagging, chunking and semantic verification. Various sources of world knowledge are also incorporated, such as WordNet and geographic information. For web retrieval, relevant document set is first created by an extended Boolean retrieval engine, and then reordered according to link information. Four runs with different combination of topic coverage and link information are submitted. On video track, We take part in both of the sub-tasks. In the task of shot boundary detection, we have submitted two runs with different parameters. In the task of video retrieval, we have submitted the results of 17 topics among all the topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHNGXF01.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHNGXF01,
		author = {Lide Wu and Xuanjing Huang and Junyu Niu and Yikun Guo and Yingju Xia and Zhe Feng},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{FDU} at {TREC-10:} Filtering, QA, Web and Video Tasks},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHNGXF01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Aggressive Morphology and Lexical Relations for Query Expansion

_William A. Woods, Stephen J. Green, Paul Alan Martin, Ann Houston_

- :fontawesome-solid-user-group: **Participant:** [SUN](./participants.md#sun)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/sun-trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/sun-trec10.pdf)
- :material-file-search: **Runs:** [mtsuna0](./runs.md#mtsuna0) | [mtsuna1](./runs.md#mtsuna1)

??? abstract "Abstract"
	
	Our submission to TREC this year is based on a combination of systems. The first is the conceptual indexing and retrieval system that was developed at Sun Microsystems Laboratories (Woods et al., 2000a; Woods et al., 2000b). The second is the MultiText system developed at the University of Waterloo (Clarke et al., 2000; Cormack et al., 2000). The conceptual indexing system was designed to help people find specific answers to specific questions in unrestricted text. It uses a combination of syntactic, semantic, and morphological knowledge, together with taxonomic subsumption techniques, to address differences in terminology between a user’s queries and the material that may answer them. At indexing time, the system builds a conceptual taxonomy of all the words and phrases in the indexed material. This taxonomy is based on the morphological structure of words, the syntactic structure of phrases, and semantic relations between meanings of words that it knows in its lexicon. It was not, however, designed as a question answering system. Our results from last year, while encour- aging, showed that we needed more work in the area of question analysis (i.e., “What would constitute an answer to this question?”) and answer determination (i.e., “Does this retrieved passage actually answer the question?”) to support our relaxation ranking passage retrieval algorithm. After conversations with the researchers at the University of Waterloo, we decided to submit a run where we would provide front-end processing consisting of query formulation and query expansion using our automatically derived taxonomy and Waterloo would provide the back-end processing via their MultiText passage retrieval system and their answer selection component. The result is a direct comparison of two question answering systems that differ only in the query formulation component.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WoodsGMH01.bib) "
	```
	@inproceedings{DBLP:conf/trec/WoodsGMH01,
		author = {William A. Woods and Stephen J. Green and Paul Alan Martin and Ann Houston},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Aggressive Morphology and Lexical Relations for Query Expansion},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/sun-trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WoodsGMH01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-10 Experiments at CAS-ICT: Filtering, Web and QA

_Bin Wang, Hongbo Xu, Zhifeng Yang, Yue Liu, Xueqi Cheng, Dongbo Bu, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [chinese_academy](./participants.md#chinese_academy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf](http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf)
- :material-file-search: **Runs:** [ICTQA10a](./runs.md#ictqa10a) | [ICTQA10b](./runs.md#ictqa10b) | [ICTQA10c](./runs.md#ictqa10c)

??? abstract "Abstract"
	
	CAS-ICT took part in the TREC conference for the first time this year. We have participated in three tracks of TREC-10. For adaptive filtering track, we paid more attention to feature selection and profile adaptation. For web track, we tried to integrate different ranking methods to improve system performance. For QA track, we focused on question type identification, named entity tagging and answer matching. This paper describes our methods in detail.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangXYLCBB01.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangXYLCBB01,
		author = {Bin Wang and Hongbo Xu and Zhifeng Yang and Yue Liu and Xueqi Cheng and Dongbo Bu and Shuo Bai},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-10} Experiments at {CAS-ICT:} Filtering, Web and {QA}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangXYLCBB01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Alicante at TREC-10

_José Luis Vicedo González, Antonio Ferrández Rodríguez, Fernando Llopis_

- :fontawesome-solid-user-group: **Participant:** [Alicante](./participants.md#alicante)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/Alicante__TREC-10_Paper.pdf](http://trec.nist.gov/pubs/trec10/papers/Alicante__TREC-10_Paper.pdf)
- :material-file-search: **Runs:** [ALIC01M1](./runs.md#alic01m1) | [ALIC01M2](./runs.md#alic01m2)

??? abstract "Abstract"
	
	This paper describes the architecture, operation and results obtained with the Question Answering prototype developed in the Department of Language Processing and Information Systems at the University of Alicante. Our system is based on our TREC-9 approach where different improvements have been introduced. Essentially these modifications are twofold: the introduction of a passage retrieval module at first stage retrieval and the redefinition of our semantic approach for paragraph selection and answer extraction.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VicedoFL01.bib) "
	```
	@inproceedings{DBLP:conf/trec/VicedoFL01,
		author = {Jos{\'{e}} Luis Vicedo Gonz{\'{a}}lez and Antonio Ferr{\'{a}}ndez Rodr{\'{\i}}guez and Fernando Llopis},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {University of Alicante at {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/Alicante\_\_TREC-10\_Paper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VicedoFL01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Patterns of Potential Answer Expressions as Clues to the Right Answers

_Martin M. Soubbotin_

- :fontawesome-solid-user-group: **Participant:** [InsightSoft](./participants.md#insightsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/insight_trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/insight_trec10.pdf)
- :material-file-search: **Runs:** [insight](./runs.md#insight)

??? abstract "Abstract"
	
	The core of our question-answering mechanism is searching for predefined patterns of textual expressions that may be interpreted as answers to certain types of questions. The presence of such patterns in analyzed answer-string candidates may provide evidence of the right answer. The answer-string candidates are created by cutting up relatively-large source documents passages containing the query terms or their synonyms/substitutes. indicative patterns. The specificity of our approach is: placing the use of indicative patterns in the core of the QA approach; aiming at the comprehensive and systematic use of such indicators; defining various structural types of the indicative patterns, including nontrivial and sophisticated ones; developing accessory techniques that ensure effective performance of the approach. We believe that the use of indicative patterns for question answering can be considered as a special case of the more general approach to text information retrieval that contrasts with linguistics-oriented methodology
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Soubbotin01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Soubbotin01,
		author = {Martin M. Soubbotin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Patterns of Potential Answer Expressions as Clues to the Right Answers},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/insight\_trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Soubbotin01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Learning Components for A Question-Answering System

_Dan Roth, Gio Kao Kao, Xin Li, Ramya Nagarajan, Vasin Punyakanok, Nick Rizzolo, Wen-tau Yih, Cecilia Ovesdotter Alm, Liam Gerard Moran_

- :fontawesome-solid-user-group: **Participant:** [UIUC](./participants.md#uiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/uiuc.pdf](http://trec.nist.gov/pubs/trec10/papers/uiuc.pdf)
- :material-file-search: **Runs:** [UIUC](./runs.md#uiuc)

??? abstract "Abstract"
	
	We describe a machine learning approach to the development of several key components in a question answering system and the way they were used in the UIUC QA system. A unified learning approach is used to develop a part-of-speech tagger, a shallow parser, a named entity recognizer and a module for identifying a question's target. These components are used in analyzing questions, as well as in the analysis of selected passages that may contain the sought after answer. The performance of the learned modules seems to be very high, (e.g., mid 90% for identifying noun phrases in sentences), though evaluating those on a large number of passages proved to be time consuming. Other components of the system, a passage retrieval module and an answer selection module, were put together in an ad-hoc fashion and significantly affected the overall performance. We ran the system only over about 60% of questions, answering a third of them correctly.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RothKLNPRYAM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/RothKLNPRYAM01,
		author = {Dan Roth and Gio Kao Kao and Xin Li and Ramya Nagarajan and Vasin Punyakanok and Nick Rizzolo and Wen{-}tau Yih and Cecilia Ovesdotter Alm and Liam Gerard Moran},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Learning Components for {A} Question-Answering System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/uiuc.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RothKLNPRYAM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Word Proximity QA System

_Philip Rennert_

- :fontawesome-solid-user-group: **Participant:** [ecwise](./participants.md#ecwise)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/ec_wise.pdf](http://trec.nist.gov/pubs/trec10/papers/ec_wise.pdf)
- :material-file-search: **Runs:** [ecw1ps](./runs.md#ecw1ps) | [ecw1csx](./runs.md#ecw1csx)

??? abstract "Abstract"
	
	This is a question answering system with very little NLP, based on question-category-dependent selection and weighting of search terms, selecting answer strings centered around words most commonly found near search terms. Its performance was medium, with a 0.2 MR. Certain category strategies may be of interest to other Aers, and are described.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Rennert01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Rennert01,
		author = {Philip Rennert},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Word Proximity {QA} System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/ec\_wise.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Rennert01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Use of WordNet Hypernyms for Answering What-Is Questions

_John M. Prager, Jennifer Chu-Carroll, Krzysztof Czuba_

- :fontawesome-solid-user-group: **Participant:** [ibm-prager](./participants.md#ibm-prager)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/Trec10Prager.pdf](http://trec.nist.gov/pubs/trec10/papers/Trec10Prager.pdf)
- :material-file-search: **Runs:** [IBMKS1M3](./runs.md#ibmks1m3) | [IBMKS1M1](./runs.md#ibmks1m1) | [IBMKS1M2](./runs.md#ibmks1m2)

??? abstract "Abstract"
	
	We present a preliminary analysis of the use of WordNet hypernyms for answering “What-is” questions. We analyse the approximately 130 definitional questions in the TREC10 corpus with respect to our technique of Virtual Annotation (VA), which has previously been shown to be effective on the TREC9 definitional question set and other questions. We discover that VA is effective on a subset of the TREC10 definitional questions, but that some of these questions seem to need a user model to generate correct answers, or at least answers that agree with the NIST judges. Furthermore, there remains a large enough subset of definitional questions that cannot benefit at all from the WordNet isa-hierarchy, prompting the need to investigate alternative external resources.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PragerCC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/PragerCC01,
		author = {John M. Prager and Jennifer Chu{-}Carroll and Krzysztof Czuba},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Use of WordNet Hypernyms for Answering What-Is Questions},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/Trec10Prager.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PragerCC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The QUANTUM Question Answering System

_Luc Plamondon, Guy Lapalme, Leila Kosseim_

- :fontawesome-solid-user-group: **Participant:** [UMontreal](./participants.md#umontreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/articleUdeM.pdf](http://trec.nist.gov/pubs/trec10/papers/articleUdeM.pdf)
- :material-file-search: **Runs:** [UdeMlistB](./runs.md#udemlistb) | [UdeMlistP](./runs.md#udemlistp) | [UdeMmainOk60](./runs.md#udemmainok60) | [UdeMmainOk80](./runs.md#udemmainok80) | [UdeMmainQt80](./runs.md#udemmainqt80)

??? abstract "Abstract"
	
	We participated to the TREC-X QA main task and list task with a new system named QUANTUM, which analyzes questions with shallow parsing techniques and regular expressions. Instead of using a question classification based on entity types, we classify the questions according to generic mechanisms (which we call extraction func-tions) for the extraction of candidate answers. We take advantage of the Okapi information retrieval system for one-paragraph-long passage retrieval. We make an extensive use of the Alembic named-entity tagger and the Word Net semantic network to extract candidate answers from those passages. We deal with the possibility of no-answer questions (NIL) by looking for a significant score drop between the extracted candidate answers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PlamondonLK01.bib) "
	```
	@inproceedings{DBLP:conf/trec/PlamondonLK01,
		author = {Luc Plamondon and Guy Lapalme and Leila Kosseim},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {QUANTUM} Question Answering System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/articleUdeM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PlamondonLK01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-10 Experiments at KAIST: Batch Filtering and Question Answering

_Jong-Hoon Oh, Kyung-Soon Lee, Du-Seong Chang, Chung Won Seo, Key-Sun Choi_

- :fontawesome-solid-user-group: **Participant:** [KAIST](./participants.md#kaist)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/kaist-trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/kaist-trec10.pdf)
- :material-file-search: **Runs:** [KAISTQAMAIN1](./runs.md#kaistqamain1) | [KAISTQAMAIN2](./runs.md#kaistqamain2) | [KAISTQALIST2](./runs.md#kaistqalist2) | [KAISTQACTX](./runs.md#kaistqactx) | [KAISTQALIST1](./runs.md#kaistqalist1)

??? abstract "Abstract"
	
	In TREC-10, we participated in two tasks: batch filtering task in the filtering task, and question answering task. In question answering task, we participated in three sub-tasks (main task, list task, and context task). In batching filtering task, we experimented a filtering technique, which unifies the results of support vector machines for subtopics subdivided by incremental clustering. For a topic, we generated subtopics by detecting similar documents in training relevant documents, and unified the results of SVM classifier for subtopics by OR set operation. In question answering task, we submitted two runs for main task (KAISTQAMAIN1, KAISTQAMAIN2), two runs for list task (KAISTQALIST1, KAISTQALIST2), and one run for context task (KAISTQACTX).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OhLCSC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/OhLCSC01,
		author = {Jong{-}Hoon Oh and Kyung{-}Soon Lee and Du{-}Seong Chang and Chung Won Seo and Key{-}Sun Choi},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-10} Experiments at {KAIST:} Batch Filtering and Question Answering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/kaist-trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OhLCSC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Tequesta: The University of Amsterdam's Textual Question Answering  System

_Christof Monz, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uva](./participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/trec10-Monz-deRijke.pdf](http://trec.nist.gov/pubs/trec10/papers/trec10-Monz-deRijke.pdf)
- :material-file-search: **Runs:** [UAmsT10qaL1](./runs.md#uamst10qal1) | [UAmsT10qaL2](./runs.md#uamst10qal2) | [UAmsT10qaM1](./runs.md#uamst10qam1) | [UAmsT10qaM3](./runs.md#uamst10qam3) | [UAmsT10qaM2](./runs.md#uamst10qam2)

??? abstract "Abstract"
	
	We describe our participation in the TREC-10 Question Answering track. All our runs used the Tequesta system; we provide a detailed account of the natural language processing and inferencing techniques that are part of Tequesta. We also summarize and discuss our results, which concern both the main task and the list task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MonzR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/MonzR01,
		author = {Christof Monz and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Tequesta: The University of Amsterdam's Textual Question Answering System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/trec10-Monz-deRijke.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MonzR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multilingual Question/Answering: the DIOGENE System

_Bernardo Magnini, Matteo Negri, Roberto Prevete, Hristo Tanev_

- :fontawesome-solid-user-group: **Participant:** [itc-irst](./participants.md#itc-irst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/IrstQA.pdf](http://trec.nist.gov/pubs/trec10/papers/IrstQA.pdf)
- :material-file-search: **Runs:** [irstqa01](./runs.md#irstqa01)

??? abstract "Abstract"
	
	This paper presents the DIOGENE question/answering system developed at ITC- Irst. The system is based on a rather standard architecture which includes three components for question processing, search and answer extraction. Linguistic processing strongly relies on MULTIWORDNET, an extended version of the English WORDNET. The system has been designed to address two promising directions: multilingual question/answering and question/answering on the Web. The results obtained in the TREC-10 main task will be presented and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MagniniNPT01.bib) "
	```
	@inproceedings{DBLP:conf/trec/MagniniNPT01,
		author = {Bernardo Magnini and Matteo Negri and Roberto Prevete and Hristo Tanev},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Multilingual Question/Answering: the {DIOGENE} System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/IrstQA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MagniniNPT01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CL Research Experiments in TREC-10 Question Answering

_Kenneth C. Litkowski_

- :fontawesome-solid-user-group: **Participant:** [clresearch](./participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/clresearch-t10.pdf](http://trec.nist.gov/pubs/trec10/papers/clresearch-t10.pdf)
- :material-file-search: **Runs:** [clr01b1](./runs.md#clr01b1) | [clr01c1](./runs.md#clr01c1) | [clr01l1](./runs.md#clr01l1) | [clr01l2](./runs.md#clr01l2) | [clr01b2](./runs.md#clr01b2)

??? abstract "Abstract"
	
	CL Research's question-answering system (DIMAP-QA) for TREC-10 only slightly extends its semantic relation triple (logical form) technology in which documents are fully parsed and databases built around discourse entities. Time constraints did not allow us to make various changes planned from TREC-9. TREC-10 changes made fuller use of the integrated machine-readable lexical resources and extended the question-answering capability to handle list and context questions. Experiments to further exploit the dictionary resources were not fully completed at the time of the TREC-10 submission, affecting planned revisions in other QA components. The official score for the main TREC-10 QA task was 0.120 (compared to 0.135 in TREC-9), based on processing 10 of the top 50 documents provided by NIST, compared to the average of 0.235 for 67 submissions. Post-hoc analysis suggests a more accurate assessment of DIMAP-QA's performance in identifying answers is 0.217. For the list task, the CL Research average accuracy was 0.13 and 0.12 for two runs compared to the average of 0.222. For the context questions, CL Research had mean reciprocal rank score of 0.178, 5th of the 7 submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Litkowski01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Litkowski01,
		author = {Kenneth C. Litkowski},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CL} Research Experiments in {TREC-10} Question Answering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/clresearch-t10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Litkowski01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Description of NTU System at TREC-10 QA Track

_Chuan-Jie Lin, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [NTU](./participants.md#ntu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/NTU_TREC10.pdf](http://trec.nist.gov/pubs/trec10/papers/NTU_TREC10.pdf)
- :material-file-search: **Runs:** [qntuam1](./runs.md#qntuam1) | [qntuam2](./runs.md#qntuam2) | [qntuac1](./runs.md#qntuac1) | [qntual1](./runs.md#qntual1) | [qntual2](./runs.md#qntual2)

??? abstract "Abstract"
	
	In the past years, we attended the 250-bytes group. Our main strategy was to measure the similarity score (or the informative score) of each candidate sentence to the question sentence. The similarity score was computed by sums of weights of cooccurred question keywords. To meet the requirement of shorter answering texts proposed in this year, we adapt our system, and experiment on a new strategy that is focused on named entities only. The similarity score is now measured in terms of the distances to the question keywords in the same document. The MRR score is 0.145. Section 2 will deal with our work in the main task. We also attended the list task and the context task this year. In the list task, the algorithm is almost the same as the one in the main task except that we have to avoid duplicate answers and find the new answers at the same time. Positions of the candidates in the answering texts should be considered. We will talk about this in Section 3. In the context task, how to keep the context, and what the answers of the previous questions can help are the main issues. In our strategy, the answers of the first question are kept when answering the subsequent questions, but the answers of the other ones (denoted by question i) are kept only if question i has a co-referential relationship to its previous one. Section 4 will describe this strategy in more detail.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinC01,
		author = {Chuan{-}Jie Lin and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Description of {NTU} System at {TREC-10} {QA} Track},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/NTU\_TREC10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SiteQ: Engineering High Performance QA System Using Lexico-Semantic  Pattern Matching and Shallow NLP

_Gary Geunbae Lee, Jungyun Seo, Seungwoo Lee, Hanmin Jung, Bong-Hyun Cho, Changki Lee, Byung-Kwan Kwak, Jeongwon Cha, Dongseok Kim, Joohui An, Harksoo Kim, Kyungsun Kim_

- :fontawesome-solid-user-group: **Participant:** [postech](./participants.md#postech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/SiteQ_trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/SiteQ_trec10.pdf)
- :material-file-search: **Runs:** [posqa10a](./runs.md#posqa10a)

??? abstract "Abstract"
	
	In TREC-10, we participated in the web track (only ad-hoc task) and the QA track (only main task). In the QA track, our QA system (SiteQ) has general architecture with three processing steps: question processing, passage selection and answer processing. The key technique is LSP's (Lexico-Semantic Patterns) that are composed of linguistic entries and semantic types. LSP grammars constructed from various resources are used for answer type determination and answer matching. We also adapt AAD (Abbreviation-Appositive-Definition) processing for the queries that answer type cannot be determined or expected, encyclopedia search for increasing the matching coverage between query terms and passages, and pivot detection for the distance calculation with answer candidates. We used two-level answer types consisted of 18 upper-level types and 47 lower-level types. Semantic category dictionary, WordNet, POS combined with lexicography and a stemmer were all applied to construct the LSP knowledge base. CSMT (Category Sense-code Mapping Table) tried to find answer types using the matching between semantic categories and sense-codes from WordNet. Evaluation shows that MRR for 492 questions is 0.320 (strict), which is considerably higher than the average MRR of other 67 runs. In the Web track, we focused on the effectiveness of both noun phrase extraction and our new PRF (Pseudo Relevance Feedback). We confirmed that our query expansion using PRF with TSV function adapting TF factor contributed to better performance, but noun phrases did not contribute much. It needs more observations for us to make elaborate rules of tag patterns for the construction of better noun phrases.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeSLJCLKCKAKK01.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeSLJCLKCKAKK01,
		author = {Gary Geunbae Lee and Jungyun Seo and Seungwoo Lee and Hanmin Jung and Bong{-}Hyun Cho and Changki Lee and Byung{-}Kwan Kwak and Jeongwon Cha and Dongseok Kim and Joohui An and Harksoo Kim and Kyungsun Kim},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {SiteQ: Engineering High Performance {QA} System Using Lexico-Semantic Pattern Matching and Shallow {NLP}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/SiteQ\_trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeSLJCLKCKAKK01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC2001 Question-Answer, Web and Cross Language Experiments using  PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf](http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf)
- :material-file-search: **Runs:** [pir1Qqa3](./runs.md#pir1qqa3) | [pir1Qqa2](./runs.md#pir1qqa2) | [pir1Qqa1](./runs.md#pir1qqa1) | [pir1Qli2](./runs.md#pir1qli2) | [pir1Qli1](./runs.md#pir1qli1) | [pir1Qctx3](./runs.md#pir1qctx3) | [pir1Qctx2](./runs.md#pir1qctx2)

??? abstract "Abstract"
	
	We applied our PIRCS system for the Question-Answer, ad-hoc Web retrieval using the 10-GB collection, and the English-Arabic cross language tracks. These are described in Sections 2,3,4 respectively. We also attempted to complete the adaptive filtering experiments with our upgraded programs but found that we did not have sufficient time to do so.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGDC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGDC01,
		author = {Kui{-}Lam Kwok and Laszlo Grunfeld and Norbert Dinstl and M. Chan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC2001} Question-Answer, Web and Cross Language Experiments using {PIRCS}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGDC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NTT Question Answering System in TREC 2001

_Hideto Kazawa, Hideki Isozaki, Eisaku Maeda_

- :fontawesome-solid-user-group: **Participant:** [nttcom_kazawa](./participants.md#nttcom_kazawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/nttcs-trec10-proceeding.pdf](http://trec.nist.gov/pubs/trec10/papers/nttcs-trec10-proceeding.pdf)
- :material-file-search: **Runs:** [nttcs10main](./runs.md#nttcs10main)

??? abstract "Abstract"
	
	In this report, we describe our question-answering system SAIQA-e (System for Advanced Interactive Question Answering in English) which ran the main task of TREC-10’s QA-track. Our system has two characteristics (1) named entity recognition based on support vector machines and (2) heuristic apposition detection. The MPR score of the main task is 0.228 and experimental results indicate the effectiveness of the above two steps in terms of answer extraction accuracy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KazawaIM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/KazawaIM01,
		author = {Hideto Kazawa and Hideki Isozaki and Eisaku Maeda},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{NTT} Question Answering System in {TREC} 2001},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/nttcs-trec10-proceeding.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KazawaIM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM's Statistical Question Answering System - TREC-10

_Abraham Ittycheriah, Martin Franz, Salim Roukos_

- :fontawesome-solid-user-group: **Participant:** [ibm-franz](./participants.md#ibm-franz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/trec2001.pdf](http://trec.nist.gov/pubs/trec10/papers/trec2001.pdf)
- :material-file-search: **Runs:** [ibmsqa01b](./runs.md#ibmsqa01b) | [ibmsqa01a](./runs.md#ibmsqa01a) | [ibmsqa01c](./runs.md#ibmsqa01c)

??? abstract "Abstract"
	
	We describe herein the IBM Statistical Question Answering system for TREC-10 in detail. Based on experiences in TREC-9, we have adapted our system to deal with definition type questions and furthermore completed the trainability aspect of our question-answering system. The experiments performed in this evaluation confirmed our hypothesis that post-processing the IR engine results can achieve the same performance as incorporating query expansion terms into the retrieval engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/IttycheriahFR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/IttycheriahFR01,
		author = {Abraham Ittycheriah and Martin Franz and Salim Roukos},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {IBM's Statistical Question Answering System - {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/trec2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/IttycheriahFR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Use of External Knowledge of Factoid QA

_Eduard H. Hovy, Ulf Hermjakob, Chin-Yew Lin_

- :fontawesome-solid-user-group: **Participant:** [ISI-USC](./participants.md#isi-usc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/TREC10-webclopedia.pdf](http://trec.nist.gov/pubs/trec10/papers/TREC10-webclopedia.pdf)
- :material-file-search: **Runs:** [isi1a50](./runs.md#isi1a50) | [ISI1b50](./runs.md#isi1b50) | [isi1l50](./runs.md#isi1l50)

??? abstract "Abstract"
	
	This paper describes recent development in the Webclopedia QA system, focusing on the use of knowledge resources such as WordNet and a QA typology to improve the basic operations of candidate answer retrieval, ranking, and answer matching.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HovyHL01.bib) "
	```
	@inproceedings{DBLP:conf/trec/HovyHL01,
		author = {Eduard H. Hovy and Ulf Hermjakob and Chin{-}Yew Lin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The Use of External Knowledge of Factoid {QA}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/TREC10-webclopedia.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HovyHL01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Answering Complex, List and Context Questions with LCC's Question-Answering  Server

_Sanda M. Harabagiu, Dan I. Moldovan, Marius Pasca, Mihai Surdeanu, Rada Mihalcea, Roxana Girju, Vasile Rus, V. Finley Lacatusu, Paul Morarescu, Razvan C. Bunescu_

- :fontawesome-solid-user-group: **Participant:** [LCC](./participants.md#lcc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/lcc-trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/lcc-trec10.pdf)
- :material-file-search: **Runs:** [LCC1](./runs.md#lcc1) | [LCC2](./runs.md#lcc2) | [LCC3](./runs.md#lcc3)

??? abstract "Abstract"
	
	This paper presents the architecture of the Question-Answering Server (QAS) developed at the Language Computer Corporation (LCC) and used in the TREC-10 evaluations. LCC's QASTM extracts answers for (a) factual questions of vairable degree of difficulty; (b) questions that expect lists of answers; and (c) questions posed in the context of previous questions and answers. One of the major novelties is the implementation of bridging inference mechanisms that guide the search for answers to complex questions. Additionally, LCC's QASTM encodes an efficient way of modeling context via reference resolution. In TREC-10, this system generated an RAR of 0.58 on the main task and 0.78 on the context task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HarabagiuMPSMGRLMB01.bib) "
	```
	@inproceedings{DBLP:conf/trec/HarabagiuMPSMGRLMB01,
		author = {Sanda M. Harabagiu and Dan I. Moldovan and Marius Pasca and Mihai Surdeanu and Rada Mihalcea and Roxana Girju and Vasile Rus and V. Finley Lacatusu and Paul Morarescu and Razvan C. Bunescu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Answering Complex, List and Context Questions with LCC's Question-Answering Server},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/lcc-trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HarabagiuMPSMGRLMB01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding An Answer Based on the Recognition of the Question Focus

_Olivier Ferret, Brigitte Grau, Martine Hurault-Plantet, Gabriel Illouz, Laura Monceaux, Isabelle Robba, Anne Vilnat_

- :fontawesome-solid-user-group: **Participant:** [limsi](./participants.md#limsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/qaLIR.pdf](http://trec.nist.gov/pubs/trec10/papers/qaLIR.pdf)
- :material-file-search: **Runs:** [QALIR1](./runs.md#qalir1) | [QALIR2](./runs.md#qalir2) | [QALIR3](./runs.md#qalir3)

??? abstract "Abstract"
	
	In this report we describe how the QALC system (the Question-Answering program of the LIR group at LIMSI-CNRS, already involved in the QA-track evaluation at TREC9), was improved in order to better extract the very answer in selected sentences. The purpose of the main Question-Answering track in TREC10 was to find text sequences no longer than 50 characters or to produce a 'no answer' response in case of a lack of answer in the TREC corpus. As QALC first retrieves relevant sentences within the document corpus, our main question was: how to find the answer in a sentence? This question involves two kinds of answer: a) it is better to know what you look for and b) you have to know the location of what you look for. The first case is solved by applying a question analysis process. This process determines the type of the expected answer in term of named entity. This named entity is searched for in the sentences. However, all answers cannot be expressed in term of a named entity. Definition questions or explanation questions for example demand phrases (noun phrases or verb phrases) as answers. So, after having studied the structure of subpart of sentences that contained answers, we defined criteria to be able to locate the precise answer within a sentence. These criteria consist in defining triplets composed of a question category, the question focus and an associated list of templates allowing the location of the answer according to the focus place in the candidate sentence. In the following sections, we will detail this novel aspect in our system by presenting the question analysis module, the different processes involved in the answer module and the results we obtained. Before, we give a brief overall presentation of QALC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FerretGHIMRV01.bib) "
	```
	@inproceedings{DBLP:conf/trec/FerretGHIMRV01,
		author = {Olivier Ferret and Brigitte Grau and Martine Hurault{-}Plantet and Gabriel Illouz and Laura Monceaux and Isabelle Robba and Anne Vilnat},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Finding An Answer Based on the Recognition of the Question Focus},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/qaLIR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FerretGHIMRV01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Web Reinforced Question Answering (MultiTest Experiments for TREC  2001)

_Charles L. A. Clarke, Gordon V. Cormack, Thomas R. Lynam, C. M. Li, G. L. McLearn_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/mtA.pdf](http://trec.nist.gov/pubs/trec10/papers/mtA.pdf)
- :material-file-search: **Runs:** [uwmta0](./runs.md#uwmta0) | [uwmta1](./runs.md#uwmta1) | [uwmta2](./runs.md#uwmta2) | [uwmtal0](./runs.md#uwmtal0) | [uwmtal1](./runs.md#uwmtal1) | [uwmtac0](./runs.md#uwmtac0)

??? abstract "Abstract"
	
	For TREC 2001, the MultiText Project concentrated on the QA track. Over the past year, we made substantial enhancements to our A system in three general areas. First, we explored a number of methods for taking advantage of external resources (including encyclopedias, dictionaries and Web data) as sources for answer validation, improving our ability to identify correct answers in the target corpus. Of the methods explored, the use of Web data to reinforce answer selection proved to be particular value. Second, we made a large number of incremental improvements to the existing system components. For example, in our parsing component, the query generation and answer category identification algorithms were extended and tuned, as were the named entity identification algorithms used in our answer extraction component. Finally, we made a careful analysis of the problem of null questions, those that have no answer in the target corpus, and developed a general approach to the problem. A basic method for handling null questions, based on the analysis, was added to our system. We submitted three runs for the main task of the QA track. The first run (uwmta1) was based on the enhanced system described above, including the full use of Web resources for answer validation. For the second run (uwmta2) the Web resources were not used for validation, but the system was otherwise identical. A comparison between these runs represents a major goal of our TREC experimental work and the major concern of this paper. The final run (uwmta0) tests a last-minute enhancement. For this run a feedback loop was added to the system, in which candidate answer terms were merged back into the query used for passage retrieval. While answer feedback was not an area of significant effort for TREC 2001, and the intial results were disappointing, it represents an area in which future work is planned. Our other TREC 2001 runs are related to the QA track. Along with the QA runs submitted for the main task, we also submitted exploratory runs for the list (uwmtal0 and uwmtal1) and context (umtacO) tasks. These runs were generated through minor modifications to the existing system, and represent preliminary attempts at participation rather than serious attempts at high performance. Our runs for the Web track (uwmtawO, uwmtawl, and uwmtaw2) are related to our QA runs. These runs were generated by our QA system by treating the topic title as a question and using the ranked list of documents containing the best answers as the result. Finally, the runs submitted by Sun Microsystems (tsuna0 and mtsuna1) were generated using our system as the backend and the Sun parser as the frontend. However, the integration between Sun and MultiText was performed in a short period of time, and these runs should also be viewed as preliminary experiments that point toward future work. In the remainder of the paper we focus on our primary runs for the main task of the QA track. In the next section we provide an overview of the QA system used for our TREC 2001 experiments, including a discussion of our technique for Web reinforcement. In section 3 we present our approach to the problem of null questions. Section 4 details our experimental results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCLLM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCLLM01,
		author = {Charles L. A. Clarke and Gordon V. Cormack and Thomas R. Lynam and C. M. Li and G. L. McLearn},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Web Reinforced Question Answering (MultiTest Experiments for {TREC} 2001)},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/mtA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCLLM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering: CNLP at the TREC-10 Question Answering Track

_Jiangping Chen, Anne Diekema, Mary D. Taffet, Nancy J. McCracken, Necati Ercan Ozgencil, Özgür Yilmazel, Elizabeth D. Liddy_

- :fontawesome-solid-user-group: **Participant:** [Syracuse](./participants.md#syracuse)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/cnlptrec10.pdf](http://trec.nist.gov/pubs/trec10/papers/cnlptrec10.pdf)
- :material-file-search: **Runs:** [SUT10DOCLT](./runs.md#sut10doclt) | [SUT10DOCMT](./runs.md#sut10docmt) | [SUT10PARLT](./runs.md#sut10parlt) | [SUT10PARMT](./runs.md#sut10parmt)

??? abstract "Abstract"
	
	This paper describes the retrieval experiments for the main task and list task of the TREC-10 question-answering track. The question answering system described automatically finds answers to questions in a large document collection. The system uses a two-stage retrieval approach to answer finding based on matching of named entities, linguistic patterns, and keywords. In answering a question, the system carries out a detailed query analysis that produces a logical query representation, an indication of the question focus, and answer clue words.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenDTMOYL01.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenDTMOYL01,
		author = {Jiangping Chen and Anne Diekema and Mary D. Taffet and Nancy J. McCracken and Necati Ercan Ozgencil and {\"{O}}zg{\"{u}}r Yilmazel and Elizabeth D. Liddy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Question Answering: {CNLP} at the {TREC-10} Question Answering Track},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/cnlptrec10.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenDTMOYL01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Grammatical Relations, Answer Frequencies and the World Wide  Web for TREC Question Answering

_Sabine Buchholz_

- :fontawesome-solid-user-group: **Participant:** [tilburg](./participants.md#tilburg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/TilburgILK.pdf](http://trec.nist.gov/pubs/trec10/papers/TilburgILK.pdf)
- :material-file-search: **Runs:** [TilburgILKs](./runs.md#tilburgilks) | [TilburgILK](./runs.md#tilburgilk)

??? abstract "Abstract"
	
	This year, we participated for the first time in TREC, and entered two runs for the main task of the TREC 2001 question answering track. Both runs use a simple baseline component implemented especially for TREC, and a high-level NLP component (called Shapaga) that uses various NLP tools developed earlier by our group. Shapaga imposes many linguistic constraints on potential answers strings which results in not so many answers being found but those that are found have a reasonably high precision. The difference between the two runs is that the first applies Shapaga to the TREC document collection only, whereas the second one also uses it on the World Wide Web (WWW). Answers found there are then mapped back to the TREC collection. The first run achieved a MRR of 0.122 under the strict evaluation (and 0.128 lenient), the second one 0.210 (0.234). We argue that the better performance is due to the much larger number of documents that Shapaqa-WWW's answers are based on.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Buchholz01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Buchholz01,
		author = {Sabine Buchholz},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Grammatical Relations, Answer Frequencies and the World Wide Web for {TREC} Question Answering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/TilburgILK.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Buchholz01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Data-Intensive Question Answering

_Eric Brill, Jimmy Lin, Michele Banko, Susan T. Dumais, Andrew Y. Ng_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/Trec2001Notebook.AskMSRFinal.pdf](http://trec.nist.gov/pubs/trec10/papers/Trec2001Notebook.AskMSRFinal.pdf)
- :material-file-search: **Runs:** [askmsr](./runs.md#askmsr) | [askmsr2](./runs.md#askmsr2)

??? abstract "Abstract"
	
	Microsoft Research Redmond participated for the first time in TREC this year, focusing on the question answering track. There is a separate report in this volume on the Microsoft Research Cambridge submissions for the filtering and Web tracks (Robertson et al., 2002). We have been exploring data-driven techniques for Web question answering, and modified our system somewhat for participation in TREC QA. We submitted two runs for the main QA track (AskMSR and AskMSR2). Data-driven methods have proven to be powerful techniques for natural language processing. It is still unclear to what extent this success can be attributed to specific techniques, versus simply the data itself. For example, Banko and Brill (2001) demonstrated that for confusion set disambiguation, a prototypical disambiguation-in-string-context problem, the amount of data used far dominates the learning method employed in improving labeling accuracy. The more training data that is used, the greater the chance that a new sample being processed can be trivially related to samples appearing in the training data, thereby lessening the need for any complex reasoning that may be beneficial in cases of sparse training data. The idea of allowing the data, instead of the methods, do most of the work is what motivated our particular approach to the TREC Question Answering task. One of the biggest challenges in TREC-style QA is overcoming the surface string mismatch between the question formulation and the string containing its answer. For some Question/Answer pairs, deep reasoning is needed to relate the two. The larger the data set from which we can draw answers, the greater the chance we can find an answer that holds a simple, easily discovered relationship to the query string. Our approach to question answering is to take advantage of the vast amount of text data that is now available online. In contrast to many question answering systems that begin with rich linguistic resources (e.g., parsers, dictionaries, WordNet), we begin with data and use that to drive the design of our system. To do this, we first use simple techniques to look for answers to questions on the Web. Since the Web has orders of magnitude more data than the TREC QA document collection, simple techniques are likely to work here. After we have found suitable answer strings from online text, we project them onto the TREC corpus in search of supporting documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrillLBDN01.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrillLBDN01,
		author = {Eric Brill and Jimmy Lin and Michele Banko and Susan T. Dumais and Andrew Y. Ng},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Data-Intensive Question Answering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/Trec2001Notebook.AskMSRFinal.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BrillLBDN01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PiQASso: Pisa Question Answering System

_Giuseppe Attardi, Antonio Cisternino, Francesco Formica, Maria Simi, Alessandro Tommasi_

- :fontawesome-solid-user-group: **Participant:** [Pisa](./participants.md#pisa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/piqasso.pdf](http://trec.nist.gov/pubs/trec10/papers/piqasso.pdf)
- :material-file-search: **Runs:** [prun001](./runs.md#prun001) | [prun002](./runs.md#prun002) | [prun003](./runs.md#prun003)

??? abstract "Abstract"
	
	PiQASso is a Question Answering system based on a combination of modern IR techniques and a series of semantic filters for selecting paragraphs containing a justifiable answer. Semantic filtering is based on several NLP tools, including a dependency-based parser, a POS tagger, a NE tagger and a lexical database. Semantic analysis of questions is performed in order to extract keywords used in retrieval queries and to detect the expected answer type. Semantic analysis of retrieved paragraphs includes checking the presence of entities of the expected answer type and extracting logical relations between words. A paragraph is considered to justify an answer if similar relations are present in the question. When no answer passes the filters, the process is repeated applying further levels of query expansions in order to increase recall. We discuss results and limitations of the current implementation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AttardiCFST01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AttardiCFST01,
		author = {Giuseppe Attardi and Antonio Cisternino and Francesco Formica and Maria Simi and Alessandro Tommasi},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {PiQASso: Pisa Question Answering System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/piqasso.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AttardiCFST01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Qanda and the Catalyst Architecture

_Pranav Anand, David Anderson, John D. Burger, John Griffith, Marc Light, Scott A. Mardis, Alexander A. Morgan_

- :fontawesome-solid-user-group: **Participant:** [mitre](./participants.md#mitre)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/MITRE-trecX-1.pdf](http://trec.nist.gov/pubs/trec10/papers/MITRE-trecX-1.pdf)
- :material-file-search: **Runs:** [MITRE01A](./runs.md#mitre01a)

??? abstract "Abstract"
	
	Qanda is MITRE’s entry into the question-answering (QA) track of the TREC conference(Voorhees & Harman 2002). This year, Qanda was re-engineered to use a new architecture for human language technology called Catalyst, developed at MITRE for the DARPA TIDES program. The Catalyst architecture was chosen because it was specifically designed for fast processing and for combin- ing the strengths of Information Retrieval (IR) and Natural Language Processing (NLP) into a single framework. These technology fields are critical to the development of QA systems. The current Qanda implementation serves as a prototype for developing QA systems in the Catalyst architecture. This paper serves as an introduction to Catalyst and the Qanda implementation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnandABGLMM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnandABGLMM01,
		author = {Pranav Anand and David Anderson and John D. Burger and John Griffith and Marc Light and Scott A. Mardis and Alexander A. Morgan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Qanda and the Catalyst Architecture},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/MITRE-trecX-1.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnandABGLMM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Oracle at TREC 10: Filtering and Question-Answering

_Shamin Alpha, Paul Dixon, Ciya Liao, Changwen Yang_

- :fontawesome-solid-user-group: **Participant:** [oracle](./participants.md#oracle)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/orcltrec10.pdf](http://trec.nist.gov/pubs/trec10/papers/orcltrec10.pdf)
- :material-file-search: **Runs:** [orcl1](./runs.md#orcl1)

??? abstract "Abstract"
	
	Oracle’s objective in TREC-10 was to study the behavior of Oracle information retrieval in previously unexplored application areas. The software used was Oracle9i Text[1], Oracle’s full-text retrieval engine integrated with the Oracle relational database management system, and the Oracle PL/SQL procedural programming language. Runs were submitted in filtering and Q/A tracks. For the filtering track we submitted three runs, in adaptive filtering, batch filtering and routing. By comparing the TREC results, we found that the concepts (themes) extracted by Oracle Text can be used to aggregate document information content to simplify statistical processing. Oracle's Q/A system integrated information retrieval (IR) and information extraction (IE). The Q/A system relied on a combination of document and sentence ranking in IR, named entity tagging in IE and shallow parsing based classification of questions into pre-defined categories.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlphaDLY01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlphaDLY01,
		author = {Shamin Alpha and Paul Dixon and Ciya Liao and Changwen Yang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Oracle at {TREC} 10: Filtering and Question-Answering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/orcltrec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlphaDLY01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A ProtoType Question Answering System Using Syntactic and Semantic  Information for Answer Retrieval

_Enrique Alfonseca, Marco De Boni, José-Luis Jara-Valencia, Suresh Manandhar_

- :fontawesome-solid-user-group: **Participant:** [York](./participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/yorkQA_paper.pdf](http://trec.nist.gov/pubs/trec10/papers/yorkQA_paper.pdf)
- :material-file-search: **Runs:** [yorkqa01](./runs.md#yorkqa01) | [yorkqa02](./runs.md#yorkqa02)

??? abstract "Abstract"
	
	This was our first entry at TREC and the system we presented was, due to time constraints, an incomplete prototype. Our main aims were to verify the usefulness of syntactic analysis for QA and to experiment with different semantic distance metrics in view of a more complete and fully integrated future system. To this end we made use of a part-of-speech tagger and NP chunker in conjunction with entity recognition and semantic distance metrics. We also envisaged experimenting with a shallow best first parser but time factors meant integration with the rest of the system was not achieved. Unfortunately due to time constraints no testing and no parameter tuning was carried out prior TREC. This in turn meant that a number of small bugs negatively influenced our results. Moreover it was not possible to carry out experiments in parameter tuning, meaning our system did not achieve optimal performance. Nevertheless we obtained reasonable results, the best score being 18.1% of the questions correct (with lenient judgements).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlfonsecaBJM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlfonsecaBJM01,
		author = {Enrique Alfonseca and Marco De Boni and Jos{\'{e}}{-}Luis Jara{-}Valencia and Suresh Manandhar},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {A ProtoType Question Answering System Using Syntactic and Semantic Information for Answer Retrieval},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/yorkQA\_paper.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AlfonsecaBJM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

