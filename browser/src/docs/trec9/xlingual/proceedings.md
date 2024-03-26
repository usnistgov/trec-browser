# Proceedings - Cross-Language 2000 

#### TREC-9 Cross-Language Information Retrieval (English-Chinese) Overview

_Fredric C. Gey, Aitao Chen_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/trec9-clir-overview.pdf](http://trec.nist.gov/pubs/trec9/papers/trec9-clir-overview.pdf)
??? abstract "Abstract"
	
	Sixteen groups participated in the TREC-9 cross-language information retrieval track which focussed on retrieving Chinese language documents in response to 25 English queries. A variety of CLIR approaches were tested and a rich set of experiments performed which measured the utility of various resources such as machine translation and parallel corpora, as well as pre- and post-translation query expansion using pseudo-relevance feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyC00.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyC00,
		author = {Fredric C. Gey and Aitao Chen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-9} Cross-Language Information Retrieval (English-Chinese) Overview},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/trec9-clir-overview.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GeyC00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-9 Cross-lingual Retrieval at BBN

_Jinxi Xu, Ralph M. Weischedel_

- :fontawesome-solid-user-group: **Participant:** [BBN](./participants.md#bbn)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/bbn-trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/bbn-trec9.pdf)
- :material-file-search: **Runs:** [BBN9XLA](./runs.md#bbn9xla) | [BBN9XLB](./runs.md#bbn9xlb) | [BBN9XLC](./runs.md#bbn9xlc) | [BBN9MONO](./runs.md#bbn9mono)

??? abstract "Abstract"
	
	BBN participated only in the cross-language track at TREC-9. We extended the monolingual approach of Miller et al. (1999), which uses hidden Markov models (HMM), by incorporating translation probabilities from Chinese terms to English terms. We will describe our approach in detail in the next section. This report will explore the following issues: 1. Whether our HMM-based retrieval model is a viable approach to cross-lingual IR. This is answered by its retrieval performance relative to monolingual retrieval performance. 2. The relative contribution of bilingual lexicons and parallel corpora. 3. The impact of query expansion on cross-lingual performance. We will use two types of query expansion: using English terms and Chinese terms. 4. The impact of query length on retrieval performance. We will use three versions of queries: short, which consist of only the title fields, medium, which consist of title and description fields and long, which consist of title, description and narrative fields of the TREC topics. 5. Whether indexing English words in Chinese documents helps cross-lingual IR. Even though the documents in the corpus are in Chinese, many of them also contain some English words. English words in the documents can directly match the query words. 6. Dialect issues. The Chinese language has many dialects. Cantonese, which is used by the TREC-9 corpus, is one example. Since we had lexical resources for Mandarin (standard Chinese) and for Cantonese, we could measure the impact of dialects on cross-lingual IR. This report includes official results for our submitted runs and results for experimental runs that are designed to help us explore the issues above.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuW00.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuW00,
		author = {Jinxi Xu and Ralph M. Weischedel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-9} Cross-lingual Retrieval at {BBN}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/bbn-trec9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuW00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC-9: CLIR, Filtering and QA Tasks

_Lide Wu, Xuanjing Huang, Yikun Guo, Bingwei Liu, Yuejie Zhang_

- :fontawesome-solid-user-group: **Participant:** [fudan](./participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf](http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf)
- :material-file-search: **Runs:** [fdut9xl1](./runs.md#fdut9xl1) | [fdut9xl2](./runs.md#fdut9xl2) | [fdut9xl3](./runs.md#fdut9xl3) | [fdut9xl4](./runs.md#fdut9xl4)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC-9 conference for the first time. We have participated in three tracks of CLIR, Filtering and QA. We have submitted four runs for CLIR track. Bilingual knowledge source and statistical-based search engine are integrated in our CLIR system. We varied our strategy somewhat between runs: long query (both title and description field of the queries involved) with pseudo relevance feedback (FDUT9XL1), long query with no feedback (FDUT9L2), median query (just description field of queries involved) with feedback (FDUT9XL3) and, the last, mono long query with feedback (FDUT9XLA). For filtering, we participate in the sub-task of adaptive filtering and batch filtering. Vector representation and computation are heavily applied in filtering procedure. 11 runs of various combination of topic and evaluation measure have been submitted: 4 OHSU runs, 1 MeSH run and 2 MSH-SAMPLE runs for adaptive filtering, and 2 OHSU runs, 1 MeSH run and 1 MSH-SAMPLE run for batch filtering. Our QA system consists of three components: Question Analyzer, Candidate Window Searcher and Answer Extractor. We submitted two runs in the 50-byte category and two runs in the 250-byte category. The runs of 'FDUT9QL1' and 'FDUT9QS1' are extracted from the top 100 candidate windows. The other two runs of 'FDUT9QL2' and 'FDUTIQS1' are extracted from the top 24 candidate windows.
	

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

#### CINDOR TREC-9 English-Chinese Evaluation

_Miguel E. Ruiz, Steve Rowe, Maurice Forrester, Paraic Sheridan_

- :fontawesome-solid-user-group: **Participant:** [textwise](./participants.md#textwise)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/TextWise-TREC9.pdf](http://trec.nist.gov/pubs/trec9/papers/TextWise-TREC9.pdf)
- :material-file-search: **Runs:** [TWe2c3CItdn](./runs.md#twe2c3citdn) | [TWmono3CItdn](./runs.md#twmono3citdn)

??? abstract "Abstract"
	
	MNIS-TextWise Labs participated in the TREC-9 Chinese Cross-Language Information Retrieval track. The focus of our research for this participation has been on rapidly adding Chinese capabilities to CINDOR using tools for automatically generating a Chinese Conceptual Interlingua from existing lexical resources. For the TREC-9 evaluation we also built a version of our system which loosely integrates the CINDOR Conceptual Language Analysis process with the SMART retrieval system. This was motivated by the conclusions of our TREC-8 experiments which pointed to sub-standard retrieval based on the underlying retrieval algorithm. This integrated system has further allowed us to experiment with a range of approaches for cross-language retrieval, some specific to Chinese, which we have used in combination for our official TREC submissions. For evaluation, we submitted a monolingual Chinese run and a cross-language English-Chinese run. Analysis of results to date allow us to conclude that the automatically generated Conceptual Interlingua helps to improve performance in both cross-language and monolingual retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuizRFS00.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuizRFS00,
		author = {Miguel E. Ruiz and Steve Rowe and Maurice Forrester and Paraic Sheridan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CINDOR} {TREC-9} English-Chinese Evaluation},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/TextWise-TREC9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuizRFS00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-9 Experiments at Maryland: Interactive CLIR

_Douglas W. Oard, Gina-Anne Levow, Clara I. Cabezas_

- :fontawesome-solid-user-group: **Participant:** [UMaryland](./participants.md#umaryland)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/umd-final.pdf](http://trec.nist.gov/pubs/trec9/papers/umd-final.pdf)
- :material-file-search: **Runs:** [TB](./runs.md#tb) | [percent](./runs.md#percent) | [mixed](./runs.md#mixed)

??? abstract "Abstract"
	
	The University of Maryland team participated in the TREC-9 Cross-Language Information Retrieval Track, with the goal of exploring evaluation paradigms for interactive cross-language retrieval. Participants were asked to examine gloss translations of highly ranked documents and make relevance judgments, and those judgments were used to produce a new ranked list in which documents assessed as relevant were promoted and those assessed as nonrelevant were demoted. No improvement over fully automatic ranking was found, which suggests that additional work on user interface design and evaluation metrics is required.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardLC00.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardLC00,
		author = {Douglas W. Oard and Gina{-}Anne Levow and Clara I. Cabezas},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-9} Experiments at Maryland: Interactive {CLIR}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/umd-final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OardLC00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The HAIRCUT System at TREC-9

_Paul McNamee, James Mayfield, Christine D. Piatko_

- :fontawesome-solid-user-group: **Participant:** [apl-jhu](./participants.md#apl-jhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/jhuapl.pdf](http://trec.nist.gov/pubs/trec9/papers/jhuapl.pdf)
- :material-file-search: **Runs:** [apl9xcmb](./runs.md#apl9xcmb) | [apl9xmon](./runs.md#apl9xmon) | [apl9xwrd](./runs.md#apl9xwrd) | [apl9xtop](./runs.md#apl9xtop)

??? abstract "Abstract"
	
	The Hopkins Automated Information Retriever for Combing Unstructured Text (HAIRCUT) is a research IR system developed at the Johns Hopkins University Applied Physics Laboratory (JHU/APL). HAIRCUT benefits from a basic design decision to support flexibility throughout the system. One specific example of this is the way we represent documents and queries; words, stemmed words, character n-grams, multiword phrases are all supported as indexing terms. This year we concentrated our efforts on two of the tasks in TREC-9, the main web task and cross-language retrieval in Chinese and English.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McNameeMP00.bib) "
	```
	@inproceedings{DBLP:conf/trec/McNameeMP00,
		author = {Paul McNamee and James Mayfield and Christine D. Piatko},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {HAIRCUT} System at {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/jhuapl.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McNameeMP00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Description of NTU QA and CLIR Systems in TREC-9

_Chuan-Jie Lin, Wen-Cheng Lin, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [NTU](./participants.md#ntu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/ntuintrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/ntuintrec9.pdf)
- :material-file-search: **Runs:** [ecirntuco](./runs.md#ecirntuco) | [ecirntua1](./runs.md#ecirntua1)

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
- :material-file-search: **Runs:** [KAIST9xlch](./runs.md#kaist9xlch) | [KAIST9xlmt](./runs.md#kaist9xlmt) | [KAIST9xlqt](./runs.md#kaist9xlqt) | [KAIST9xlqm](./runs.md#kaist9xlqm)

??? abstract "Abstract"
	
	In TREC-9, we participated in three tasks: question answering task, cross-language retrieval task, and batch filtering task in the filtering task. Our question answering system consists of following basic components - query analyzer, Named entity tagger, Answer Extractor. First, question analyzer analyzes the given question. Question analyzer generates question type and keywords of the given question. Then retrieved documents are analyzed for extracting relevant answer. POS tagger and Named entity tagger are used for the purpose. Finally, Answer Extractor generates relevant answer. There are four runs in our CLIR, two runs follow the dictionary and MI information based translation approach (KAIST9xIqm, KAIST9xlqt), another one using the mixture result of two commercial Machine Translation systems (KAIST9xImt), and the final one is monolingual run (KAIST9xIch). We translated only query and description fields in all four runs. In batching filtering task, we submitted results for OHSU topics and MSH-SMP topics. For OHSU topics, we have been exploring a filtering technique which combines query zone, support vector machine, and Rocchio's algorithm. For MSH-SMP topics, we use support vector machine simply.
	

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

#### TREC-9 Cross Language, Web and Question-Answering Track Experiments  using PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf](http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf)
- :material-file-search: **Runs:** [pir0Xori](./runs.md#pir0xori) | [pir0Xdin](./runs.md#pir0xdin) | [pir0Xhnd](./runs.md#pir0xhnd) | [pir0XHxD](./runs.md#pir0xhxd)

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

#### TREC-9 CLIR at CUHK: Disambiguation by Similarity Values Between  Adjacent Words

_Honglan Jin, Kam-Fai Wong_

- :fontawesome-solid-user-group: **Participant:** [CUHK](./participants.md#cuhk)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/cuhk_clir_trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/cuhk_clir_trec9.pdf)
- :material-file-search: **Runs:** [CHUHK00XEC1](./runs.md#chuhk00xec1) | [CHUHK00CH1](./runs.md#chuhk00ch1)

??? abstract "Abstract"
	
	We investigated the dictionary-based query translation method combining the translation disambiguation process using statistic co-occurrence information trained from the provided corpus. We believe that neighboring words tend to be related in contextual meaning and have higher chance of co-occurrence particularly if adjacent words (two or more) compose a phrase. The correct translation equivalents of co-occurrence pattern in a source language are more likely to co-occur in a target language documents than in conjunction with any incorrect translation equivalents within a certain range of contextual window size. In this work, we tested several methods to calculate the degree of co-occurrence and used them as the basis of disambiguation. Different from most disambiguation methods which usually select one best translation equivalent for a word, we select the best translation equivalent pairs for two adjacent words. The final translated queries are the concatenation of all overlapped adjacent word translation pairs after disambiguation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JinW00.bib) "
	```
	@inproceedings{DBLP:conf/trec/JinW00,
		author = {Honglan Jin and Kam{-}Fai Wong},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-9} {CLIR} at {CUHK:} Disambiguation by Similarity Values Between Adjacent Words},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/cuhk\_clir\_trec9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JinW00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-9 CLIR Experiments at MSRCN

_Jianfeng Gao, Jian-Yun Nie, Jian Zhang, Endong Xun, Yi Su, Ming Zhou, Changning Huang_

- :fontawesome-solid-user-group: **Participant:** [microsoft-china](./participants.md#microsoft-china)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/trec-9.pdf](http://trec.nist.gov/pubs/trec9/papers/trec-9.pdf)
- :material-file-search: **Runs:** [msrcn1](./runs.md#msrcn1) | [msrcn2](./runs.md#msrcn2) | [msrcn3](./runs.md#msrcn3)

??? abstract "Abstract"
	
	In TREC-9, we participated in the English-Chinese Cross-Language Information Retrieval (CLIR) track. Our work involved two aspects: finding good methods for Chinese IR, and finding effective translation means between English and Chinese. On Chinese monolingual retrieval, we investigated the use of different entities as indexes, pseudo-relevance feedback, and length normalization, and examined their impact on Chinese IR. On English-Chinese CLIR, our focus was put on finding effective ways for query translation. Our method incorporates three improvements over the simple lexicon-based translation: (1) word/term disambiguation using co-occurrence, (2) phrase detecting and translation using a statistical language model and (3) translation coverage enhancement using a statistical translation model. This method is shown to be as effective as a good MT system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaoNZXSZH00.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaoNZXSZH00,
		author = {Jianfeng Gao and Jian{-}Yun Nie and Jian Zhang and Endong Xun and Yi Su and Ming Zhou and Changning Huang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-9} {CLIR} Experiments at {MSRCN}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/trec-9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaoNZXSZH00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### English-Chinese Information Retrieval at IBM

_Martin Franz, J. Scott McCarley, Wei-Jing Zhu_

- :fontawesome-solid-user-group: **Participant:** [ibm-franz](./participants.md#ibm-franz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/ibm_clir.pdf](http://trec.nist.gov/pubs/trec9/papers/ibm_clir.pdf)
- :material-file-search: **Runs:** [ibmcl9s](./runs.md#ibmcl9s) | [ibmcl9a](./runs.md#ibmcl9a) | [ibmcl9m](./runs.md#ibmcl9m)

??? abstract "Abstract"
	
	We describe TREC-9 experiments with an IR system that incorporates statistical machine translation trained on sentence-aligned parallel corpora for both query translation (English→Chinese) and document translation (Chinese→English.) These systems are contrasted with monolingual Chinese retrieval and with query translation based on a widely available commercial machine translation package. These systems incorporate both words and characters as features for the retrieval. Comparisons with a baseline from TREC-5/6 enable our experiments to address issues related to the differences between Beijing and Hong Kong dialects.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FranzMZ00.bib) "
	```
	@inproceedings{DBLP:conf/trec/FranzMZ00,
		author = {Martin Franz and J. Scott McCarley and Wei{-}Jing Zhu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {English-Chinese Information Retrieval at {IBM}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/ibm\_clir.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FranzMZ00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melbourne TREC-9 Experiments

_Daryl J. D'Souza, Michael Fuller, James A. Thom, Phil Vines, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/mds.pdf](http://trec.nist.gov/pubs/trec9/papers/mds.pdf)
- :material-file-search: **Runs:** [rmitcl001](./runs.md#rmitcl001) | [rmitcl002](./runs.md#rmitcl002) | [rmitcl003](./runs.md#rmitcl003) | [rmitcl004](./runs.md#rmitcl004)

??? abstract "Abstract"
	
	We report results for experiments conducted in Melbourne at CSIRO, RMIT, and The University of Melbourne for TREC-9. We present results for the interactive track, cross-lingual track, main web track, and the query track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DSouzaFTVZ00.bib) "
	```
	@inproceedings{DBLP:conf/trec/DSouzaFTVZ00,
		author = {Daryl J. D'Souza and Michael Fuller and James A. Thom and Phil Vines and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Melbourne {TREC-9} Experiments},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/mds.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DSouzaFTVZ00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### English-Chinese Cross-Language IR Using Bilingual Dictionaries

_Aitao Chen, Hailing Jiang, Fredric C. Gey_

- :fontawesome-solid-user-group: **Participant:** [berkeley-clir](./participants.md#berkeley-clir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/trec9_berkeley.pdf](http://trec.nist.gov/pubs/trec9/papers/trec9_berkeley.pdf)
- :material-file-search: **Runs:** [BRKECA1](./runs.md#brkeca1) | [BRKCCA1](./runs.md#brkcca1) | [BRKECA2](./runs.md#brkeca2) | [BRKECM1](./runs.md#brkecm1)

??? abstract "Abstract"
	
	This report describes the English-Chinese cross-language retrieval experiments at Berkeley for TREC-9 Cross-Language Information Retrieval track. We present a simple and effective Chinese word segmentation method and compare the cross-language retrieval performance of two bilingual dictionaries for query translation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenJG00.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenJG00,
		author = {Aitao Chen and Hailing Jiang and Fredric C. Gey},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {English-Chinese Cross-Language {IR} Using Bilingual Dictionaries},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/trec9\_berkeley.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenJG00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-9

_James Allan, Margaret E. Connell, W. Bruce Croft, Fangfang Feng, David Fisher, Xiaoyan Li_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/umass-trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/umass-trec9.pdf)
- :material-file-search: **Runs:** [INQ7XL1](./runs.md#inq7xl1) | [INQ7XL2](./runs.md#inq7xl2) | [INQ7XL3](./runs.md#inq7xl3) | [INQ7XL4](./runs.md#inq7xl4)

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

