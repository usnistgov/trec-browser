# Proceedings - Question Answering 2000 

#### Overview of the TREC-9 Question Answering Track

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/qa_overview.pdf](http://trec.nist.gov/pubs/trec9/papers/qa_overview.pdf)
??? abstract "Abstract"
	
	The TREC question answering track is an effort to bring the benefits of large-scale evaluation to bear on the question answering problem. The track has run twice so far, where the goal both times was to retrieve small snippets of text that contain the actual answer to a question rather than the document lists traditionally returned by text retrieval systems. The best performing system in TREC-9, the Falcon system from Southern Methodist University, was able to answer about 65% of the questions (compared to approximately 42% of the questions for the next best systems) by combining abductive reasoning with various natural language processing techniques. The 65% score is slightly less than the best scores for TREC-8 in absolute terms, but it represents a very significant improvement in question answering systems. The TREC-9 task was considerably harder than the TREC-8 task because the TREC-9 track used actual users' questions rather than questions constructed specifically for the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees00.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees00,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of the {TREC-9} Question Answering Track},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/qa\_overview.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC-9: CLIR, Filtering and QA Tasks

_Lide Wu, Xuanjing Huang, Yikun Guo, Bingwei Liu, Yuejie Zhang_

- :fontawesome-solid-user-group: **Participant:** [fudan](./participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf](http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf)
- :material-file-search: **Runs:** [FDUT9QS1](./runs.md#fdut9qs1) | [FDUT9QL1](./runs.md#fdut9ql1) | [FDUT9QL2](./runs.md#fdut9ql2) | [FDUT9QS2](./runs.md#fdut9qs2)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC-9 conference for the first time. We have participated in three tracks of CLIR, Filtering and QA. We have submitted four runs for CLIR track. Bilingual knowledge source and statistical-based search engine are integrated in our CLIR system. We varied our strategy somewhat between runs: long query (both title and description field of the queries involved) with pseudo relevance feedback (FDUT9XL1), long query with no feedback (FDUT9XL2), median query (just description field of queries involved) with feedback (FDUT9L3) and, the last, mono long query with feedback (FDUT9XL4). For filtering, we participate in the sub-task of adaptive filtering and batch filtering. Vector representation and computation are heavily applied in filtering procedure. 11 runs of various combination of topic and evaluation measure have been submitted: 4 OHSU runs, 1 MeSH run and 2 MSH-SAMPLE runs for adaptive filtering, and 2 OHSU runs, 1 MeSH run and 1 MSH-SAMPLE run for batch filtering. Our QA system consists of three components: Question Analyzer, Candidate Window Searcher and Answer Extractor. We submitted two runs in the 50-byte category and two runs in the 250-byte category. The runs of 'FDUTIQLI' and 'FDUT9QS1' are extracted from the top 100 candidate windows. The other two runs of 'FDUT9QL2' and 'FDUTIQS1' are extracted from the top 24 candidate windows.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHGLZ00.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHGLZ00,
		author = {Lide Wu and Xuanjing Huang and Yikun Guo and Bingwei Liu and Yuejie Zhang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{FDU} at {TREC-9:} CLIR, Filtering and {QA} Tasks},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHGLZ00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Halfway to Question Answering

_William A. Woods, Stephen J. Green, Paul Alan Martin, Ann Houston_

- :fontawesome-solid-user-group: **Participant:** [SUN](./participants.md#sun)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/sun-trec9-final.pdf](http://trec.nist.gov/pubs/trec9/papers/sun-trec9-final.pdf)
- :material-file-search: **Runs:** [SunOne](./runs.md#sunone) | [SunToo](./runs.md#suntoo)

??? abstract "Abstract"
	
	The conceptual indexing and retrieval system at Sun Microsystems Laboratories (Woods et al., 2000) is designed to help people find specific answers to specific questions in unrestricted text. It uses a combination of syntactic, semantic, and morphological knowledge, together with taxonomic subsumption techniques, to address differences in terminology between a user's queries and the material that may answer them. At indexing time, the system builds a conceptual taxonomy of all the words and phrases in the indexed material. This taxonomy is based on the morphological structure of words, the syntactic structure of phrases, and semantic relations between meanings of words that it knows in its lexicon. At query time, the system automatically retrieves any concepts that are subsumed by (i.e., are more specific than) the user's query terms, according to this taxonomy. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WoodsGMH00.bib) "
	```
	@inproceedings{DBLP:conf/trec/WoodsGMH00,
		author = {William A. Woods and Stephen J. Green and Paul Alan Martin and Ann Houston},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Halfway to Question Answering},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/sun-trec9-final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WoodsGMH00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NTT DATA TREC-9 Question Answering Track Report

_Toru Takaki_

- :fontawesome-solid-user-group: **Participant:** [ntt-data](./participants.md#ntt-data)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/nttdata9.pdf](http://trec.nist.gov/pubs/trec9/papers/nttdata9.pdf)
- :material-file-search: **Runs:** [NTTD9QAa1S](./runs.md#nttd9qaa1s) | [NTTD9QAa2S](./runs.md#nttd9qaa2s) | [NTTD9QAa1L](./runs.md#nttd9qaa1l) | [NTTD9QAb1L](./runs.md#nttd9qab1l)

??? abstract "Abstract"
	
	This paper describes the processing details and TREC-9 question answering results for our QA sys-tem. We use a general information retrieval strategy and a simple information extraction method with our QA system. Two types of indices, one for documents and one for passages, were used for our experiment. We submitted four results, two for each category of short and long answers. A score of 0.231 for the short category and 0.391 for the long category was obtained.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Takaki00.bib) "
	```
	@inproceedings{DBLP:conf/trec/Takaki00,
		author = {Toru Takaki},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{NTT} {DATA} {TREC-9} Question Answering Track Report},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/nttdata9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Takaki00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Sheffield TREC-9 Q&A System

_Sam Scott, Robert J. Gaizauskas_

- :fontawesome-solid-user-group: **Participant:** [sheffield](./participants.md#sheffield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/shef-trec9-qa-final.pdf](http://trec.nist.gov/pubs/trec9/papers/shef-trec9-qa-final.pdf)
- :material-file-search: **Runs:** [shef50ea](./runs.md#shef50ea) | [shef50](./runs.md#shef50) | [shef250](./runs.md#shef250) | [shef250p](./runs.md#shef250p)

??? abstract "Abstract"
	
	The system entered by the University of Sheffield in the question answering track of TREC-9 represents a significant development over the Sheffield system entered for TREC-8 [6] and, satisfyingly, achieved significantly better results on a significantly harder test set. Nevertheless, the underlying architecture and many of the lower level components remained the same. The essence of the approach is to pass the question to an information retrieval (IR) system which uses it as a query to do passage retrieval against the test collection. The top ranked passages output from the IR system are then passed to a modified information extraction (IE) system. Syntactic and semantic analysis of these passages, along with the question, is carried out to identify the 'sought entity' from the question and to score potential matches for this sought entity in each of the retrieved passages. The five highest scoring matches become the system's response.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ScottG00.bib) "
	```
	@inproceedings{DBLP:conf/trec/ScottG00,
		author = {Sam Scott and Robert J. Gaizauskas},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {University of Sheffield {TREC-9} Q{\&}A System},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/shef-trec9-qa-final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ScottG00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### One Search Engine or Two for Question-Answering

_John M. Prager, Eric W. Brown, Dragomir R. Radev, Krzysztof Czuba_

- :fontawesome-solid-user-group: **Participant:** [ibmQA](./participants.md#ibmqa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/PragerTrec9notebook.pdf](http://trec.nist.gov/pubs/trec9/papers/PragerTrec9notebook.pdf)
- :material-file-search: **Runs:** [IBMKR250](./runs.md#ibmkr250) | [IBMKA250](./runs.md#ibmka250) | [IBMKA50](./runs.md#ibmka50) | [IBMKR50](./runs.md#ibmkr50)

??? abstract "Abstract"
	
	We present here a preliminary analysis of the results of our runs in the Question Answering track of TREC9. We have developed a complete system, including our own indexer and search engine, GuruQA, which provides document result lists that our Answer Selection module processes to identify answer fragments. Some TREC participants use a standard set of result lists provided by AT&T's running of the SMART search en-gine. We wondered how our results would be affected by using the AT&T result sets. For a variety of reasons we could not replace GuruQA's results with SMART's, but we could use document co-occurrence counts to influence our hit-lists. We submitted two runs to NIST for both the 50- and 250-byte cases, one with and one without consideration of the AT&T document result sets. The AT&T document set was only used for a subset of about a third of the questions. This subset exhibited an increase in Mean Reciprocal Answer Rank score of 13% and 8% for the two tasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PragerBRC00.bib) "
	```
	@inproceedings{DBLP:conf/trec/PragerBRC00,
		author = {John M. Prager and Eric W. Brown and Dragomir R. Radev and Krzysztof Czuba},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {One Search Engine or Two for Question-Answering},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/PragerTrec9notebook.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PragerBRC00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Syntactic Clues and Lexical Resources in Question-Answering

_Kenneth C. Litkowski_

- :fontawesome-solid-user-group: **Participant:** [clresearch](./participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/clresearch00.pdf](http://trec.nist.gov/pubs/trec9/papers/clresearch00.pdf)
- :material-file-search: **Runs:** [clr00b1](./runs.md#clr00b1) | [clr00b2](./runs.md#clr00b2) | [clr00s1](./runs.md#clr00s1) | [clr00s2](./runs.md#clr00s2)

??? abstract "Abstract"
	
	CL Research's question-answering system (DIMAP-QA) for TREC-9 significantly extends its semantic relation triple (logical form) technology in which documents are fully parsed and databases built around discourse entities. This extension further exploits parsing output, most notably appositives and relative clauses, which are quite useful for question-answering. Further, DIMAP-QA integrated machine-readable lexical resources: a full-sized dictionary and a thesaurus with entries linked to specific dictionary definitions. The dictionary's 270,000 definitions were fully parsed and semantic relations extracted to provide a MindNet-like semantic network; the thesaurus was reorganized into a WordNet file structure. DIMAP-QA uses these lexical resources, along with other methods, to support a just-in-time design that eliminates preprocessing for named-entity extraction, statistical subcategorization patterning, anaphora resolution, ontology development, and unguided query expansion. (All of these techniques are implicit in DIMAP-QA.) The best official scores for TREC-9 are 0.296 for sentences and 0.135 for short answers, based on processing 20 of the top 50 documents provided by NIST, 0.054 and 0.083 below the TREC-9 averages. The initial post-hoc analysis suggests a more accurate assessment of DIMAP-QA's performance in identifying answers is 0.485 and 0.196. This analysis also suggests that many failures can be dealt with relatively straightforwardly, as was done in improving performance for TREC-8 answers to 0.803 and 0.597 for sentences and short answers, respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Litkowski00.bib) "
	```
	@inproceedings{DBLP:conf/trec/Litkowski00,
		author = {Kenneth C. Litkowski},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Syntactic Clues and Lexical Resources in Question-Answering},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/clresearch00.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Litkowski00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Description of NTU QA and CLIR Systems in TREC-9

_Chuan-Jie Lin, Wen-Cheng Lin, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [NTU](./participants.md#ntu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/ntuintrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/ntuintrec9.pdf)
- :material-file-search: **Runs:** [qntua02](./runs.md#qntua02) | [qntua01](./runs.md#qntua01) | [qntua03](./runs.md#qntua03)

??? abstract "Abstract"
	
	National Taiwan University (NTU) Natural Language Processing Laboratory (NLPL) took part in QA and CL tracks in TREC9. For the QA Track, we proposed three models, which integrate the information of Named Entity, inflections, synonyms, and co-reference. We plan to evaluate how each factor effects the performance of a QA system. For the Cross-Language Track, we employed two approaches in Chinese-English information retrieval (Bian and Chen, 1998; Chen, Bian, and Lin, 1999) to English-Chinese information retrieval. We plan to explore their usability.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinLC00.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinLC00,
		author = {Chuan{-}Jie Lin and Wen{-}Cheng Lin and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Description of {NTU} {QA} and {CLIR} Systems in {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/ntuintrec9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinLC00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-9 Experiments at KAIST: QA, CLIR and Batch Filtering

_Kyung-Soon Lee, Jong-Hoon Oh, Jin-Xia Huang, Jae-Ho Kim, Key-Sun Choi_

- :fontawesome-solid-user-group: **Participant:** [KAIST](./participants.md#kaist)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/kaist-trec9-qa-filtering.pdf](http://trec.nist.gov/pubs/trec9/papers/kaist-trec9-qa-filtering.pdf)
- :material-file-search: **Runs:** [KAIST9qa1](./runs.md#kaist9qa1) | [KAIST9qa2](./runs.md#kaist9qa2)

??? abstract "Abstract"
	
	In TREC-9, we participated in three tasks: question answering task, cross-language retrieval task, and batch filtering task in the filtering task. Our question answering system consists of following basic components - query analyzer, Named entity tagger, Answer Extractor. First, question analyzer analyzes the given question. Question analyzer generates question type and keywords of the given question. Then retrieved documents are analyzed for extracting relevant answer. POS tagger and Named entity tagger are used for the purpose. Finally, Answer Extractor generates relevant answer. There are four runs in our CLIR, two runs follow the dictionary and MI information based translation approach (KAIST9xqm, KAIST9xlqt), another one using the mixture result of two commercial Machine Translation systems (KAIST9xImt), and the final one is monolingual run (KAIST9xIch). We translated only query and description fields in all four runs. In batching filtering task, we submitted results for OHSU topics and MSH-SMP topics. For OHSU topics, we have been exploring a filtering technique which combines query zone, support vector machine, and Rocchio's algorithm. For MSH-SMP topics, we use support vector machine simply.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeOHKC00.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeOHKC00,
		author = {Kyung{-}Soon Lee and Jong{-}Hoon Oh and Jin{-}Xia Huang and Jae{-}Ho Kim and Key{-}Sun Choi},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-9} Experiments at {KAIST:} QA, {CLIR} and Batch Filtering},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/kaist-trec9-qa-filtering.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeOHKC00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Goal-Driven Answer Extraction

_Michael Laszlo, Leila Kosseim, Guy Lapalme_

- :fontawesome-solid-user-group: **Participant:** [UMontreal](./participants.md#umontreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/udempaperqafinal10p.pdf](http://trec.nist.gov/pubs/trec9/papers/udempaperqafinal10p.pdf)
- :material-file-search: **Runs:** [UdeMlng1](./runs.md#udemlng1) | [UdeMlng2](./runs.md#udemlng2) | [UdeMshrt](./runs.md#udemshrt) | [UdeMexct](./runs.md#udemexct)

??? abstract "Abstract"
	
	We describe the structure and functioning of an answer-extraction system built from the ground up, in only three man-months, using shallow text-processing techniques. Underlying these techniques is the attribution to each question of a goal type serving to characterize the outward form of candidate answers. The goal type is used as a filter during long-answer ex-traction, essentially a small-scale IR process which returns 250-byte windows rather than whole documents. To obtain short answers, strings matching the goal type are extracted from these windows and ranked by heuristics. TREC-9 performance figures show that our system has difficulty dealing with brief, definition-based questions of the kind most likely to be posed by users. We propose that specialized QA strategies be developed to handle such cases.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LaszloKL00.bib) "
	```
	@inproceedings{DBLP:conf/trec/LaszloKL00,
		author = {Michael Laszlo and Leila Kosseim and Guy Lapalme},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Goal-Driven Answer Extraction},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/udempaperqafinal10p.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LaszloKL00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-9 Cross Language, Web and Question-Answering Track Experiments  using PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf](http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf)
- :material-file-search: **Runs:** [pir0qas1](./runs.md#pir0qas1) | [pir0qas2](./runs.md#pir0qas2) | [pir0qal1](./runs.md#pir0qal1) | [pir0qal2](./runs.md#pir0qal2)

??? abstract "Abstract"
	
	In TREC-9, we participated in the English-Chinese Cross Language, 10GB Web data ad-hoc retrieval as well as the Question-Answering tracks, all using automatic procedures. All these tracks were new for us. For Cross Language track, we made use of two techniques of query translation: MT software and bilingual wordlist lookup with disambiguation. The retrieval lists from them were then combined as our submitted results. One submitted run used wordlist translation only. All cross language runs make use of the previous TREC Chinese collection for enrichment. One MT run also employs pre-translation query expansion using TREC English collections. We also submitted a monolingual run without collection enrichment. Evaluation shows that English-Chinese crosslingual retrieval using only wordlist query translation can achieve about 70-75% of monolingual average precision, and combination with MT query translation further brings this effectiveness to 80-85% of monolingual. Results are well-above median. Our PIRCS system was upgraded to handle the 10GB Web track data. Retrieval procedures were similar to those of the previous ad-hoc experiments. Results are well-above median. In the Question-Answering track, we analyzed questions into a few categories (like 'who', 'where', 'when', etc.) and used simple heuristics to weight and rank sentences in retrieved documents that may contain answers to the questions. We used both the NIST-supplied retrieval list and our own. Results are also well-above median. Two runs were also submitted for the Adaptive Filtering track. These were done using old programs without training because we ran out of time. Results were predictably unsatisfactory.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGC00.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGC00,
		author = {Kui{-}Lam Kwok and Laszlo Grunfeld and Norbert Dinstl and M. Chan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-9} Cross Language, Web and Question-Answering Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGC00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering Considering Semantic Categories and Co-Occurrence  Density

_Soo-Min Kim, Dae-Ho Baek, Sang-Beom Kim, Hae-Chang Rim_

- :fontawesome-solid-user-group: **Participant:** [korea](./participants.md#korea)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/kuqa.pdf](http://trec.nist.gov/pubs/trec9/papers/kuqa.pdf)
- :material-file-search: **Runs:** [KUQA250a](./runs.md#kuqa250a) | [KUQA250b](./runs.md#kuqa250b) | [KUQA50a](./runs.md#kuqa50a) | [KUQA50b](./runs.md#kuqa50b)

??? abstract "Abstract"
	
	In this paper, we present a Question Answering system called KUQA (Korea University Question Answering system) developed by using semantic categories and cooccurrence density. Semantic categories are used for computing the semantic similarity between a question and an answer, and co-occurrence density is used for measuring the proximity of the answer to the words of the question. KUQA is developed based on the hypothesis that the words that are semantically similar to the question and locally close to the words appeared in the question are likely to be the answer to the question.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KimBKR00.bib) "
	```
	@inproceedings{DBLP:conf/trec/KimBKR00,
		author = {Soo{-}Min Kim and Dae{-}Ho Baek and Sang{-}Beom Kim and Hae{-}Chang Rim},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Question Answering Considering Semantic Categories and Co-Occurrence Density},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/kuqa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KimBKR00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM's Statistical Question Answering System

_Abraham Ittycheriah, Martin Franz, Wei-Jing Zhu, Adwait Ratnaparkhi, Richard J. Mammone_

- :fontawesome-solid-user-group: **Participant:** [ibm-franz](./participants.md#ibm-franz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/ibm_qa.pdf](http://trec.nist.gov/pubs/trec9/papers/ibm_qa.pdf)
- :material-file-search: **Runs:** [ibmhlt0050](./runs.md#ibmhlt0050) | [ibmhlt00250](./runs.md#ibmhlt00250)

??? abstract "Abstract"
	
	We describe the IBM Statistical Question Answering for TREC-9 system in detail and look at several examples and errors. The system is an application of maximum entropy classification for question/ answer type prediction and named entity marking. We describe our system for information retrieval which in the first step did document retrieval from a local encyclopedia, and in the second step performed an expansion of the query words and finally did passage retrieval from the TREC collection. We will also discuss the answer selection algorithm which determines the best sentence given both the question and the occurrence of a phrase belonging to the answer class desired by the question. Results at the 250 byte and 50 byte levels for the overall system as well as results on each subcomponent are presented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/IttycheriahFZRM00.bib) "
	```
	@inproceedings{DBLP:conf/trec/IttycheriahFZRM00,
		author = {Abraham Ittycheriah and Martin Franz and Wei{-}Jing Zhu and Adwait Ratnaparkhi and Richard J. Mammone},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {IBM's Statistical Question Answering System},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/ibm\_qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/IttycheriahFZRM00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering in Webclopedia

_Eduard H. Hovy, Laurie Gerber, Ulf Hermjakob, Michael Junk, Chin-Yew Lin_

- :fontawesome-solid-user-group: **Participant:** [ISI-USC](./participants.md#isi-usc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/webclopedia.pdf](http://trec.nist.gov/pubs/trec9/papers/webclopedia.pdf)
- :material-file-search: **Runs:** [ISI0A50](./runs.md#isi0a50)

??? abstract "Abstract"
	
	IR techniques have proven quite successful at locating within large collections of documents those relevant to a user's query. Often, however, the user wants not whole documents but brief answers to specific questions: How old is the President? Who was the second person on the moon? When was the storming of the Bastille? Recently, a number of research projects have investigated the computational techniques needed for effective performance at this level of granularity, focusing just on questions that can be answered in a few words taken as a passage directly from a single text (leaving aside, for the moment, the answering of longer, more complex answers, such as stories about events, descriptions of objects, compare &contrast discussions, arguments of opinion, etc.). The systems being built in these projects exhibit a fairly standard structure: all create a query from the user's question, perform IR with the query to locate (segments of) documents likely to contain an answer, and then pinpoint the most likely answer passage within the candidate documents. The most common difference of approach lies in the pinpointing. A 'pure IR' approach would segment each document in the collection into a series of mini-documents, retrieve the segments that best match the query, and return them as answer. The challenge here would be to make segments so small as to be just answer-sized but still large enough to be indexable. A 'pure NLP' approach would be to match the parse and/or semantic interpretation of the question against the parse and/or semantic interpretation of each sentence in the candidate answer-containing documents, and return the best matches). The challenge here would be to perform parsing, interpretation, and matching fast enough to be practical, given the large volumes of text to be handled. Answering short questions thus becomes a problem of finding the best combination of word-level (IR) and syntactic/semantic-level (NLP) techniques, the former to produce as short a set of likely candidate segments as possible and the latter to pinpoint the answers) as accurately as possible. Because language allows paraphrasing and inference, however, working out the details is not entirely straightforward. In this paper we describe the Webclopedia, a system that uses a classification of QA types to facilitate coverage, uses a robust syntactic-semantic parser to perform the analysis, and contains a matcher that combines word- and parse-tree-level information to identify answer passages. Section 2 outlines the Webclopedia approach and architecture; Section 3 describes document retrieval and processing, Section 4 describes the QA Typology, Section 5 the parsing, and Section 6 the matching.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HovyGHJL00.bib) "
	```
	@inproceedings{DBLP:conf/trec/HovyGHJL00,
		author = {Eduard H. Hovy and Laurie Gerber and Ulf Hermjakob and Michael Junk and Chin{-}Yew Lin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Question Answering in Webclopedia},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/webclopedia.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HovyGHJL00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FALCON: Boosting Knowledge for Answer Engines

_Sanda M. Harabagiu, Dan I. Moldovan, Marius Pasca, Rada Mihalcea, Mihai Surdeanu, Razvan C. Bunescu, Roxana Girju, Vasile Rus, Paul Morarescu_

- :fontawesome-solid-user-group: **Participant:** [SMU](./participants.md#smu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/smu.pdf](http://trec.nist.gov/pubs/trec9/papers/smu.pdf)
- :material-file-search: **Runs:** [LCCSMU1](./runs.md#lccsmu1) | [LCCSMU2](./runs.md#lccsmu2)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HarabagiuMPMSBGRM00.bib) "
	```
	@inproceedings{DBLP:conf/trec/HarabagiuMPMSBGRM00,
		author = {Sanda M. Harabagiu and Dan I. Moldovan and Marius Pasca and Rada Mihalcea and Mihai Surdeanu and Razvan C. Bunescu and Roxana Girju and Vasile Rus and Paul Morarescu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{FALCON:} Boosting Knowledge for Answer Engines},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/smu.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HarabagiuMPMSBGRM00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Semantic Approach to Question Answering Systems

_José Luis Vicedo González, Antonio Ferrández Rodríguez_

- :fontawesome-solid-user-group: **Participant:** [Alicante](./participants.md#alicante)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/alicante_trec_9_paper.pdf](http://trec.nist.gov/pubs/trec9/papers/alicante_trec_9_paper.pdf)
- :material-file-search: **Runs:** [ALI9A250](./runs.md#ali9a250) | [ALI9A50](./runs.md#ali9a50) | [ALI9C250](./runs.md#ali9c250) | [ALI9C50](./runs.md#ali9c50)

??? abstract "Abstract"
	
	This paper describes the architecture, operation and results obtained with the Question Answering prototype developed in the Department of Language Processing and Information Systems at the University of Alicante. Our approach accomplishes question representation by combining keywords with a semantic representation of expected answer characteristics. Answer string ranking is performed by computing similarity between this representation and document sentences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GonzalezR00.bib) "
	```
	@inproceedings{DBLP:conf/trec/GonzalezR00,
		author = {Jos{\'{e}} Luis Vicedo Gonz{\'{a}}lez and Antonio Ferr{\'{a}}ndez Rodr{\'{\i}}guez},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {A Semantic Approach to Question Answering Systems},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/alicante\_trec\_9\_paper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GonzalezR00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QALC–The Question-Answering System of LIMSI-CNRS

_Olivier Ferret, Brigitte Grau, Martine Hurault-Plantet, Gabriel Illouz, Christian Jacquemin, Nicolas Masson, Paule Lecuyer_

- :fontawesome-solid-user-group: **Participant:** [limsi](./participants.md#limsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/qalc-limsilc.pdf](http://trec.nist.gov/pubs/trec9/papers/qalc-limsilc.pdf)
- :material-file-search: **Runs:** [lcat050](./runs.md#lcat050) | [lcat250](./runs.md#lcat250) | [lcix250](./runs.md#lcix250)

??? abstract "Abstract"
	
	In this report we describe the QALC system (the Question-Answering program of the Language and Cognition group at LIMSI-CNRS) which has been involved in the QA-track evaluation at TREC9. The purpose of the Question-Answering track is to find the answers to a set of about 700 questions. The answers are text sequences extracted from the 5 volumes of the TREC collection. All the questions have at least one answer in the collection. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FerretGHIJML00.bib) "
	```
	@inproceedings{DBLP:conf/trec/FerretGHIJML00,
		author = {Olivier Ferret and Brigitte Grau and Martine Hurault{-}Plantet and Gabriel Illouz and Christian Jacquemin and Nicolas Masson and Paule Lecuyer},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {QALC--The Question-Answering System of {LIMSI-CNRS}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/qalc-limsilc.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FerretGHIJML00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering Using a Large NLP System

_David Elworthy_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/msrc-qa.pdf](http://trec.nist.gov/pubs/trec9/papers/msrc-qa.pdf)
- :material-file-search: **Runs:** [msq9L50](./runs.md#msq9l50) | [msq9L250](./runs.md#msq9l250)

??? abstract "Abstract"
	
	There is a separate report in this volume on the Microsoft Research Cambridge participation in the Filtering and Query tracks (Robertson and Walker 2001). The Microsoft Research question-answering system for TREC-9 was based on a combination of the Okapi retrieval engine, Microsoft's natural language processing system (NLPWin), and a module for matching logical forms. There is no recent published account of NLPWin, although a description of its predecessor can be found in Jensen et al. (1993). NLPWin accepts sentences and delivers a detailed syntactic analysis, together with a logical form (LF) representing an abstraction of the meaning. The original goal was to construct a framework for complex inferencing between the logical forms for questions and sentences from documents. Many answers can be found with trivial inference schemas. For example, the TREC-8 question What is the brightest star visible from Earth? could be answered from a sentence containing ... Sirius, the brightest star visible from Earth ...by noting that all of the content words from the question are matched, and stand in the same relationships in the question and in the answer, and that the term Sirius is equivalent to the answer's counterpart of the head term in the question, star. The goal of using inferencing over logical forms was to allow for more complex cases, as in Who wrote the play 'Hamlet'? which should not be answered using ... Zeferelli's film of 'Hamlet' since a film is not a play. The idea of using inferencing for question-answering is not new. It can be found in systems from the 1970s for story understanding (Lehnert, 1978) and database querying (Bolc, 1980), and in more recent work for questions over computer system documentation (Aliod, 1998). Time pressure forced this idea to be dropped (work on the system did not start until March 2000), and instead a simpler scheme was adopted, still using LFs from NLPWin. The main observation behind the actual system is that the answer often appears in close proximity to the content terms from the question within the LF, as in the Sirius example above. Consequently, we can try to find answers by identifying candidate nodes in the LF and then using a measure of the proximity. For some kinds of question, such as when questions, there is a clear way of identifying candidate answers; for others, such as what, it is much harder. In the following section, we will look at the architecture of the system, and describe the main question types and how they are handled. The evaluation follows in section 3. The results turned out to be relatively poor. Interestingly, there is a very large difference between the results on the TREC-8 test set and the TREC-9 questions, and we will use a fine grained evaluation to examine why.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Elworthy00.bib) "
	```
	@inproceedings{DBLP:conf/trec/Elworthy00,
		author = {David Elworthy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Question Answering Using a Large {NLP} System},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/msrc-qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Elworthy00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering: CNLP at the TREC-9 Question Answering Track

_Anne Diekema, Xiaoyong Liu, Jiangping Chen, Hudong Wang, Nancy J. McCracken, Özgür Yilmazel, Elizabeth D. Liddy_

- :fontawesome-solid-user-group: **Participant:** [Syracuse](./participants.md#syracuse)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/cnlptrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/cnlptrec9.pdf)
- :material-file-search: **Runs:** [SUT9p2c3c050](./runs.md#sut9p2c3c050) | [SUT9p2c3c250](./runs.md#sut9p2c3c250) | [SUT9bn3c050](./runs.md#sut9bn3c050) | [SUT9bn3c250](./runs.md#sut9bn3c250)

??? abstract "Abstract"
	
	This paper describes a question answering system that automatically finds answers to questions in a large collection of documents. The prototype CNLP question answering system was developed for participation in the TREC-9 question answering track. The system uses a two-stage retrieval approach to answer finding based on keyword and named entity matching. Results indicate that the system ranks correct answers high (mostly rank 1), provided that an answer to the question was found. Performance figures and further analyses are included.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DiekemaLCWMYL00.bib) "
	```
	@inproceedings{DBLP:conf/trec/DiekemaLCWMYL00,
		author = {Anne Diekema and Xiaoyong Liu and Jiangping Chen and Hudong Wang and Nancy J. McCracken and {\"{O}}zg{\"{u}}r Yilmazel and Elizabeth D. Liddy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Question Answering: {CNLP} at the {TREC-9} Question Answering Track},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/cnlptrec9.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DiekemaLCWMYL00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Simple Question Answering System

_Richard J. Cooper, Stefan M. Rüger_

- :fontawesome-solid-user-group: **Participant:** [imperial](./participants.md#imperial)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/icrjc99a.pdf](http://trec.nist.gov/pubs/trec9/papers/icrjc99a.pdf)
- :material-file-search: **Runs:** [ICrjc99a](./runs.md#icrjc99a) | [ICrjc99b](./runs.md#icrjc99b)

??? abstract "Abstract"
	
	We describe our simple question answering system written in perl that uses the CMU Link parser (Sleator and Temperley 1991), Princeton University's WordNet (Miller 1995), the REX system for XML parsing (Cameron 1998) and the Managing Gigabyte search engine (Witten, Moffat and Bell 1999). This work is based on an MSc project (Cooper 2000).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CooperR00.bib) "
	```
	@inproceedings{DBLP:conf/trec/CooperR00,
		author = {Richard J. Cooper and Stefan M. R{\"{u}}ger},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {A Simple Question Answering System},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/icrjc99a.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CooperR00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering by Passage Selection (MultiText Experiments for  TREC-9)

_Charles L. A. Clarke, Gordon V. Cormack, D. I. E. Kisman, Thomas R. Lynam_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/mt9.pdf](http://trec.nist.gov/pubs/trec9/papers/mt9.pdf)
- :material-file-search: **Runs:** [uwmt9qas0](./runs.md#uwmt9qas0) | [uwmt9qal0](./runs.md#uwmt9qal0) | [uwmt9qas1](./runs.md#uwmt9qas1) | [uwmt9qal1](./runs.md#uwmt9qal1)

??? abstract "Abstract"
	
	MultiText has participated in TREC each year since TREC-4 [3, 2, 7, 8, 6]. For TREC-9 we concentrated our efforts on the question answering (QA) track and also submitted runs for the Web track. The MultiText system incorporates a unique technique for arbitrary passage retrieval, which was used in all of our TREC-9 experiments. The technique efficiently locates high-scoring passages, where the score of a passage is based on its length and the weights of the terms occurring within it. Passage boundaries are determined by the query, and can start and end at any term position. If a document ranking is required, the score of a document is computed by combining the scores of the passages it contains. Versions of the technique have been described in our previous TREC papers and elsewhere [4]. Our TREC-8 paper [6] provides a concise overview of the current version. Our TREC-9 QA experiments extended our TREC-8 work. For TREC-8 we simply stripped stopwords from the question, applied the passage retrieval technique, and submitted 250 or 50 bytes centered at each of the top five passages. Considering that no use was made of the structure of the question or the meaning of words within it, relatively good results were achieved. For TREC-9 we applied both question pre-processing, to a generate a query that is more likely to retrieve passages that contain the answer, and passage post-processing, to select the best 250 or 50 byte answer from within a passage. Both the pre-processor and post-processor make use of a question parser, which generates the query to be executed against the target collection and a set of selection rules that are used to drive a set of pattern matching routines in the post-processor. In addition, we participated in all aspects of the Web Track, submitting runs over both the 10GB and 100GB collections, 10GB runs incorporating link information, and 10GB runs using both title only and title-description queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCKL00.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCKL00,
		author = {Charles L. A. Clarke and Gordon V. Cormack and D. I. E. Kisman and Thomas R. Lynam},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Question Answering by Passage Selection (MultiText Experiments for {TREC-9)}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/mt9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCKL00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filters and Answers: The University of Iowa TREC-9 Results

_Elena Catona, David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [iowa](./participants.md#iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/iowa.pdf](http://trec.nist.gov/pubs/trec9/papers/iowa.pdf)
- :material-file-search: **Runs:** [UIQA002](./runs.md#uiqa002) | [UIQA001](./runs.md#uiqa001)

??? abstract "Abstract"
	
	The University of Iowa participated in the adaptive filtering and question answering tracks of TREC9. The filtering system used was an extension of the one used in TREC-7 [1] and TREC-8 [2]. Question answering was done using a rule-based system that employed a combination of public domain technologies and the SMART retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CatonaES00.bib) "
	```
	@inproceedings{DBLP:conf/trec/CatonaES00,
		author = {Elena Catona and David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Filters and Answers: The University of Iowa {TREC-9} Results},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/iowa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CatonaES00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Another Sys Called Qanda

_Eric Breck, John D. Burger, Lisa Ferro, Warren R. Greiff, Marc Light, Inderjeet Mani, Jason Rennie_

- :fontawesome-solid-user-group: **Participant:** [mitre](./participants.md#mitre)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/mitre.pdf](http://trec.nist.gov/pubs/trec9/papers/mitre.pdf)
- :material-file-search: **Runs:** [MTR00S1](./runs.md#mtr00s1) | [MTR00L1](./runs.md#mtr00l1) | [MTR00X1](./runs.md#mtr00x1) | [MTR00Y1](./runs.md#mtr00y1)

??? abstract "Abstract"
	
	This year our primary goal was to improve on the performance of our TREC-8 system. In addition to improving the system directly, we worked on a number of tools to aid our development. We continued our work on a tool for automatic scoring of system responses, a 'judge' program. We designed a tool for doing regression testing of question answering systems. We developed a measure of candidate confusability which measures the effectiveness of a set of features for reducing the choices that a ranking system has to make: a coarse form of perplexity. Finally, we performed preliminary work on a method for generating supervised training data. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BreckBFGLMR00.bib) "
	```
	@inproceedings{DBLP:conf/trec/BreckBFGLMR00,
		author = {Eric Breck and John D. Burger and Lisa Ferro and Warren R. Greiff and Marc Light and Inderjeet Mani and Jason Rennie},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Another Sys Called Qanda},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/mitre.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BreckBFGLMR00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The PISAB Question Answering System

_Giuseppe Attardi, Cristian Burrini_

- :fontawesome-solid-user-group: **Participant:** [Pisa](./participants.md#pisa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/pisab.pdf](http://trec.nist.gov/pubs/trec9/papers/pisab.pdf)
- :material-file-search: **Runs:** [PISA0](./runs.md#pisa0) | [PISAB](./runs.md#pisab) | [PISAS](./runs.md#pisas)

??? abstract "Abstract"
	
	The PISAB Question Answering system is based on a combination of Information Extraction and Information Retrieval techniques. Knowledge extracted from documents is modeled as a set of entities extracted from text and by relations between them. During the learning phase we index documents using the entities they contain. In the answering phase we exploit the index previously built in order to focus the search for the answer to just the most relevant documents. As answers to a question we select from these documents the paragraphs containing entities most similar to those in the question. PISAB has been submitted to the TREC-9 Conference, achieving encouraging results despite it current prototypical development stage.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AttardiB00.bib) "
	```
	@inproceedings{DBLP:conf/trec/AttardiB00,
		author = {Giuseppe Attardi and Cristian Burrini},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {PISAB} Question Answering System},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/pisab.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AttardiB00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-9

_James Allan, Margaret E. Connell, W. Bruce Croft, Fangfang Feng, David Fisher, Xiaoyan Li_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/umass-trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/umass-trec9.pdf)
- :material-file-search: **Runs:** [INQ9WSUM](./runs.md#inq9wsum) | [INQ9AND](./runs.md#inq9and)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in three of the tracks: the cross-language, question answering, and query tracks. We used approaches that were similar to those used in past years. In the next section, we describe some of the basic processing that was applied across most of the tracks. We then describe the details for each of the tracks and in some cases present some modest analysis of the effectiveness of our results. 
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCCFFL00.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCCFFL00,
		author = {James Allan and Margaret E. Connell and W. Bruce Croft and Fangfang Feng and David Fisher and Xiaoyan Li},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} and {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/umass-trec9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanCCFFL00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

