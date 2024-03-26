# Proceedings - Web 2000 

#### Overview of the TREC-9 Web Track

_David Hawking_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/web9.pdf](http://trec.nist.gov/pubs/trec9/papers/web9.pdf)
??? abstract "Abstract"
	
	TREC-9 marked a broadening of the range of of search task types represented in the Web track and a serious attempt to determine whether hyperlinks could be used to improve retrieval effectiveness on a topic-relevance ad hoc retrieval task. The Large Web Task compared the ability of systems to locate online service pages within the 18.5 million page VLC2 collection. In this case the question is not whether the page is relevant to the topic, but whether it provides direct access to the desired service. In contrast, the Main Web Task compared link-based and non-link methods on a task involving topic relevance queries and a 1.69 million page corpus (WT10g) which was carefully engineered to ensure a high density of inter-server links and (relative) ease of processing. The Main Web task topics were in TREC Ad Hoc form but were reverse engineered from query logs. Ternary relevance judgments were obtained and, in addition, assessors were asked to identify 'best' documents for each topic. As in TREC-8, no significant benefit associated with the use of link information in a topic-relevance retrieval task was demonstrated by any of the participating groups, whether or not additional weight was given to highly relevant documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Hawking00.bib) "
	```
	@inproceedings{DBLP:conf/trec/Hawking00,
		author = {David Hawking},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of the {TREC-9} Web Track},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/web9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Hawking00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Mirror DBMS at TREC-9

_Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [CWI](./participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/trec9cwi.pdf](http://trec.nist.gov/pubs/trec9/papers/trec9cwi.pdf)
- :material-file-search: **Runs:** [CWI0001](./runs.md#cwi0001) | [CWI0000](./runs.md#cwi0000) | [CWI0002](./runs.md#cwi0002) | [CWI0010](./runs.md#cwi0010)

??? abstract "Abstract"
	
	The Mirror DBMS is a prototype database system especially designed for multimedia and web retrieval. From a database perspective, this year's purpose has been to check whether we can get sufficient efficiency on the larger data set used in TREC-9. From an IR perspective, the experiments are limited to rather primitive web-retrieval, teaching us that web-retrieval is (un?-) fortunately not just retrieving text from a different data source. We report on some limited (and disappointing) experiments in an attempt to benefit from the manually assigned data in the metatags. We further discuss observations with respect to the effectiveness of title-only topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Vries00.bib) "
	```
	@inproceedings{DBLP:conf/trec/Vries00,
		author = {Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The Mirror {DBMS} at {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/trec9cwi.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Vries00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Hummingbird's Fulcrum SearchServer at TREC-9

_Stephen Tomlinson, Tom Blackwell_

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/humtrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/humtrec9.pdf)
- :material-file-search: **Runs:** [hum9tdn](./runs.md#hum9tdn) | [hum9te](./runs.md#hum9te) | [hum9tde](./runs.md#hum9tde) | [hum9td4](./runs.md#hum9td4)

??? abstract "Abstract"
	
	Hummingbird submitted ranked result sets for the Main Web Task (10GB of web data) and Large Web Task (100GB) of the TREC-9 Web Track, and for Stage 2 of the TREC-9 Query Track (43 variations of 50 queries). SearchServer's Intuitive Searching produced the highest Precision@S score (averaged over 50 web queries) of all Title-only runs submitted to the Main Web Task. SearchServer's approximate text searching and linguistic expansion each increased average precision for web queries by 5%. Enabling SearchServer's document length normalization increased average precision for web queries by 10-30% and for long queries by 100%. Squaring the importance of the inverse document frequency (relevance method 'V2:4') increased average precision in the query track by 5%. Blind query expansion decreased average precision of highly relevants for web queries by almost 15%; the same method was neutral when counting all relevants the same.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TomlinsonB00.bib) "
	```
	@inproceedings{DBLP:conf/trec/TomlinsonB00,
		author = {Stephen Tomlinson and Tom Blackwell},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Hummingbird's Fulcrum SearchServer at {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/humtrec9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TomlinsonB00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AT&T at TREC-9

_Amit Singhal, Marcin Kaszkiel_

- :fontawesome-solid-user-group: **Participant:** [ATT](./participants.md#att)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/att-trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/att-trec9.pdf)
- :material-file-search: **Runs:** [att0010gbe](./runs.md#att0010gbe) | [att0010gb](./runs.md#att0010gb) | [att0010gbt](./runs.md#att0010gbt) | [att0010gbl](./runs.md#att0010gbl) | [att0010glf](./runs.md#att0010glf) | [att0010glv](./runs.md#att0010glv)

??? abstract "Abstract"
	
	This year we come to TREC with a new retrieval system Tira that we have implemented over the last year. Tivra is based on the vector space model, and is mainly designed to do large-scale web search with limited resources. We run Tivra on a cheap Linux box. It currently indexes around 14-15 gigabytes of web data per hour, and allows sub-second web searches for 2-3 word queries on a 700 MHz Pentium box. At the time of submissions Tivra was in its early development stages, and was not fully tested. However, we still submitted runs for both the web tracks - 10 gigabytes and 100 gigabytes. The results look quite reasonable for an untested version of the system. For the 10 gigabytes ad-hoc task, our results are above median for majority of the queries. This is specially notable given that we use only the title portion of the queries whereas the results pool contains results based on both long and short queries. Our results are among the top results in the 100 gigabytes task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinghalK00.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinghalK00,
		author = {Amit Singhal and Marcin Kaszkiel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {AT{\&}T at {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/att-trec9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SinghalK00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC-9 Experiment: Link-based Retrieval and Distributed  Collections

_Jacques Savoy, Yves Rasolofo_

- :fontawesome-solid-user-group: **Participant:** [Neuchatel](./participants.md#neuchatel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/unine9.pdf](http://trec.nist.gov/pubs/trec9/papers/unine9.pdf)
- :material-file-search: **Runs:** [NEnmLpas](./runs.md#nenmlpas) | [NEnmLsa](./runs.md#nenmlsa) | [NEnm](./runs.md#nenm) | [NEtm](./runs.md#netm) | [NENRtm](./runs.md#nenrtm) | [NENRtmLpas](./runs.md#nenrtmlpas)

??? abstract "Abstract"
	
	The web and its search engines have resulted in a new paradigm, generating new challenges for the IR community which are in turn attracting a growing interest from around the world. The decision by NIST to build a new and larger test collection based on web pages represents a very attractive initiative. This motivated us at TREC-9 to support and participate in the creation of this new corpus, to address the underlying problems of managing large text collections and to evaluate the retrieval effectiveness of hyperlinks. In this paper, we will describe the results of our investigations, which demonstrate that simple raw score merging may show interesting retrieval performances while the hyperlinks used in different search strategies were not able to improve retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavoyR00.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavoyR00,
		author = {Jacques Savoy and Yves Rasolofo},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Report on the {TREC-9} Experiment: Link-based Retrieval and Distributed Collections},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/unine9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SavoyR00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Structuring and Expanding Queries in the Probabilistic Model

_Yasushi Ogawa, Hiroko Mano, Masumi Narita, Sakiko Honma_

- :fontawesome-solid-user-group: **Participant:** [ricoh](./participants.md#ricoh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/ricoh9-final.pdf](http://trec.nist.gov/pubs/trec9/papers/ricoh9-final.pdf)
- :material-file-search: **Runs:** [ric9dpx](./runs.md#ric9dpx) | [ric9dpn](./runs.md#ric9dpn) | [ric9dsx](./runs.md#ric9dsx) | [ric9dpxL](./runs.md#ric9dpxl) | [ric9tpx](./runs.md#ric9tpx)

??? abstract "Abstract"
	
	This is our second participation in TREC, following the last year's ad-hoc, and five runs were submitted for the main web track. Our system is based on our Japanese text retrieval system (3], to which English tokenizer/stemmer has been added to process English text. Our indexing system stores term positions, thus providing proximity-based search, in which the user can specify the distance between query terms. What our system does is outlined as follows: 1. Query construction The query constructor accepts each topic, extracts words in each of the appropriate fields and constructs a query to be supplied to the ranking system. 2. Initial retrieval The constucted query is fed into the ranking system, which then assigns term weights to query terms, scores each document and turns up a set of top-ranked documents assumed to be relevant to the topic (pseudo-relevant documents). 3. Query expansion The query expander collects and ranks the words in the pseudo-relevant documents and the words ranked the highest are added to the original query, with the words already in the query re-assigned new term weights. 4. Final retrieval The ranking system performs final retrieval using the modified query. The basic features of the system are mostly the same as those implemented last year for the TREC-8 ad-hoc track (2). In what follows, we explain each of the steps in more detail, both the features retained from last year and new enhancements we added this year for the TREC-9 main web track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OgawaMNH00.bib) "
	```
	@inproceedings{DBLP:conf/trec/OgawaMNH00,
		author = {Yasushi Ogawa and Hiroko Mano and Masumi Narita and Sakiko Honma},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Structuring and Expanding Queries in the Probabilistic Model},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/ricoh9-final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OgawaMNH00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Space Based on HTML Structure

_Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [newby](./participants.md#newby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/newby-t9.pdf](http://trec.nist.gov/pubs/trec9/papers/newby-t9.pdf)
- :material-file-search: **Runs:** [iswtd](./runs.md#iswtd) | [iswtdn](./runs.md#iswtdn) | [iswt](./runs.md#iswt) | [isnnwt](./runs.md#isnnwt)

??? abstract "Abstract"
	
	The main goal for the Information Space system for TREC9 was early precision. To facilitate this, an emphasis was placed on seeking matches from only the TITLE, H1, H2 and H3 tags in the Web (wt10G) and large Web (wt100) document collections. Ranking of documents was based on a combination of Boolean union sets, term weights, and principal components analysis (PCA). Very large sparse cooccurrence matrices were created for term weighting and PCA. The Information Space system is part of a larger general software package called IRTools. 
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Newby00.bib) "
	```
	@inproceedings{DBLP:conf/trec/Newby00,
		author = {Gregory B. Newby},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Information Space Based on {HTML} Structure},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/newby-t9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Newby00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fujitsu Laboratories TREC-9 Report

_Isao Namba_

- :fontawesome-solid-user-group: **Participant:** [Fujitsu](./participants.md#fujitsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/flab_trec9_paper_final.pdf](http://trec.nist.gov/pubs/trec9/papers/flab_trec9_paper_final.pdf)
- :material-file-search: **Runs:** [Flab9atN](./runs.md#flab9atn) | [Flab9atdN](./runs.md#flab9atdn) | [Flab9atdnN](./runs.md#flab9atdnn) | [Flab9atd2N](./runs.md#flab9atd2n)

??? abstract "Abstract"
	
	This year a Fujitsu Laboratory team participated in web tracks. For TREC9 we experimented passage retrieval which is expected to be effective for Web pages which contain more than one topic. To split document into passages, we used NLP based paragrah detecting program, not by fixed (variable) window size. But it did not produce better result for TREC9 Web data. For indexing large web data faster, we developped two techiniques. One is multi-partional selective sorting for inversion which is about 10-30% faster than normal quick sorting in sorting term-number, text-number pair. The other is compressed trie dictionary based stemming.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Namba00.bib) "
	```
	@inproceedings{DBLP:conf/trec/Namba00,
		author = {Isao Namba},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Fujitsu Laboratories {TREC-9} Report},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/flab\_trec9\_paper\_final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Namba00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The HAIRCUT System at TREC-9

_Paul McNamee, James Mayfield, Christine D. Piatko_

- :fontawesome-solid-user-group: **Participant:** [apl-jhu](./participants.md#apl-jhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/jhuapl.pdf](http://trec.nist.gov/pubs/trec9/papers/jhuapl.pdf)
- :material-file-search: **Runs:** [apl9tdn](./runs.md#apl9tdn) | [apl9t](./runs.md#apl9t) | [apl9lt](./runs.md#apl9lt) | [apl9ltdn](./runs.md#apl9ltdn) | [apl9all](./runs.md#apl9all) | [apl9td](./runs.md#apl9td)

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

#### TREC-9 Cross Language, Web and Question-Answering Track Experiments  using PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf](http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf)
- :material-file-search: **Runs:** [pir0Wttd](./runs.md#pir0wttd) | [pir0Watd](./runs.md#pir0watd) | [pir0Wtd2](./runs.md#pir0wtd2) | [pir0Wt1](./runs.md#pir0wt1) | [pir0WTTD](./runs.md#pir0wttd)

??? abstract "Abstract"
	
	In TREC-9, we participated in the English-Chinese Cross Language, 10GB Web data ad-hoc retrieval as well as the Question-Answering tracks, all using automatic procedures. All these tracks were new for us. For Cross Language track, we made use of two techniques of query translation: MT software and bilingual wordlist lookup with disambiguation. The retrieval lists from them were then combined as our submitted results. One submitted run used wordlist translation only. All cross language runs make use of the previous TREC Chinese collection for enrichment. One MT run also employs pre-translation query expansion using TREC English collections. We also submitted a monolingual run without collection enrichment. Evaluation shows that English-Chinese crosslingual retrieval using only wordlist query translation can achieve about 70-75% of monolingual average precision, and combination with MT query translation further brings this effectiveness to 80-85% of monolingual. Results are well-above median. Our PIRCS system was upgraded to handle the 10GB Web track data. Retrieval procedures were similar to those of the previous ad-hoc experiments. Results are well-above median. In the Question-Answering track, we analyzed questions into a few categories (like 'who' ', 'where', 'when', etc.) and used simple heuristics to weight and rank sentences in retrieved documents that may contain answers to the questions. We used both the NIST-supplied retrieval list and our own. Results are also well-above median. Two runs were also submitted for the Adaptive Filtering track. These were done using old programs without training because we ran out of time. Results were predictably unsatisfactory.
	

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

#### TNO-UT at TREC-9: How Different are Web Documents?

_Wessel Kraaij, Thijs Westerveld_

- :fontawesome-solid-user-group: **Participant:** [twenty-one](./participants.md#twenty-one)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/tno-ut.pdf](http://trec.nist.gov/pubs/trec9/papers/tno-ut.pdf)
- :material-file-search: **Runs:** [tnout9t2lk50](./runs.md#tnout9t2lk50) | [tnout9t2lc50](./runs.md#tnout9t2lc50) | [tnout9t2lc10](./runs.md#tnout9t2lc10) | [tnout9t2](./runs.md#tnout9t2) | [tnout9f1](./runs.md#tnout9f1)

??? abstract "Abstract"
	
	Although at first sight, the web track might seem a copy of the ad hoc track, we discovered that some small adjustments had to be made to our systems to run the web evaluation. As we expected, the basic language model based IR model worked effectively on this data. Blind feedback methods however, seem less effective on web data. We also experimented with rescoring the documents based on several algorithms that exploit link information. These methods yielded no positive result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KraaijW00.bib) "
	```
	@inproceedings{DBLP:conf/trec/KraaijW00,
		author = {Wessel Kraaij and Thijs Westerveld},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TNO-UT} at {TREC-9:} How Different are Web Documents?},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/tno-ut.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KraaijW00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ACSys/CSIRO TREC-9 Experiments

_David Hawking_

- :fontawesome-solid-user-group: **Participant:** [ACSys](./participants.md#acsys)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/acsys.pdf](http://trec.nist.gov/pubs/trec9/papers/acsys.pdf)
- :material-file-search: **Runs:** [acsys9mw0](./runs.md#acsys9mw0)

??? abstract "Abstract"
	
	Unfortunately, ACSys was able to commit very few resources to TREC experiments this year and participated only in the Web track. I took the retrieval component (PADRE99) of our standard metadata/content Intranet search engine, modified it to handle TREC-formatted web pages and ran the unexpanded topic titles as queries. I also generated a set of manual (non-interactive) queries from the topic statements. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Hawking00a.bib) "
	```
	@inproceedings{DBLP:conf/trec/Hawking00a,
		author = {David Hawking},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ACSys/CSIRO {TREC-9} Experiments},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/acsys.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Hawking00a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Dublin City University Experiments in Connectivity Analysis for TREC-9

_Cathal Gurrin, Alan F. Smeaton_

- :fontawesome-solid-user-group: **Participant:** [dublin](./participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/dcu_trec9_final.pdf](http://trec.nist.gov/pubs/trec9/papers/dcu_trec9_final.pdf)
- :material-file-search: **Runs:** [dcu00ca](./runs.md#dcu00ca) | [dcu00la](./runs.md#dcu00la) | [dcu00lc](./runs.md#dcu00lc) | [dcu00lb](./runs.md#dcu00lb)

??? abstract "Abstract"
	
	Dublin City University (DCU) took part in the Web Track (small task) in TREC-9. Our experiments were based on evaluating a number of connectivity analysis algorithms that we hoped would produce a marked improvement over a baseline Vector Space model system. Our connectivity experiments are all based on non-iterative post-query algorithms, which rerank a set of documents returned from content-only VSM queries. We feel that in order to implement a real-world system based on connectivity analysis the algorithms must have a low query-time processing overhead, hence our employment of non-iterative algorithms. Our results showed that we were unable to improve over a content-only run with our algorithms. We believe this to be mainly due to the nature of the link structure within the WT10g dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GurrinS00.bib) "
	```
	@inproceedings{DBLP:conf/trec/GurrinS00,
		author = {Cathal Gurrin and Alan F. Smeaton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Dublin City University Experiments in Connectivity Analysis for {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/dcu\_trec9\_final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GurrinS00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Reflections on "Aboutness" TREC-9 Evaluation Experiments at Justsystem

_Sumio Fujita_

- :fontawesome-solid-user-group: **Participant:** [justsystems](./participants.md#justsystems)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/jscbt9w_paper.pdf](http://trec.nist.gov/pubs/trec9/papers/jscbt9w_paper.pdf)
- :material-file-search: **Runs:** [jscbt9wll1](./runs.md#jscbt9wll1) | [jscbt9wls1](./runs.md#jscbt9wls1) | [jscbt9wcs1](./runs.md#jscbt9wcs1) | [jscbt9wcl1](./runs.md#jscbt9wcl1) | [jscbt9wll2](./runs.md#jscbt9wll2) | [jscbt9wls2](./runs.md#jscbt9wls2)

??? abstract "Abstract"
	
	TREC-9 evaluation experiments at the Justsystem site are described with a focus on 'aboutness' based approach in text retrieval. Experiments on the effects of supplemental noun phrase indexing, pseudo-relevance feedback and reference database feedback in view of the effect of various length of queries are reported. The results show that pesudo-relevance feedback is always effective while reference database feedback is effective only with very short queries. We reconfirmed that supplemental phrasal indexing is more effective with longer queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Fujita00.bib) "
	```
	@inproceedings{DBLP:conf/trec/Fujita00,
		author = {Sumio Fujita},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Reflections on "Aboutness" {TREC-9} Evaluation Experiments at Justsystem},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/jscbt9w\_paper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Fujita00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT TREC-9 - Entity Based Feedback with Fusion

_Abdur Chowdhury, Steven M. Beitzel, Eric C. Jensen, M. Sailee, David A. Grossman, Ophir Frieder, M. Catherine McCabe, David O. Holmes_

- :fontawesome-solid-user-group: **Participant:** [IIT](./participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/iit-trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/iit-trec9.pdf)
- :material-file-search: **Runs:** [iit00m](./runs.md#iit00m) | [iit00td](./runs.md#iit00td) | [iit00tde](./runs.md#iit00tde) | [iit00t](./runs.md#iit00t)

??? abstract "Abstract"
	
	For TREC-9, we focused on effectiveness in the web track. The key techniques we employed were information fusion, entity-based relevance feedback, Wordnet-based query parsing and a user interface designed to assist with web-based manual queries. Our initial results are positive. For the manual task, forty of fifty queries are over the median. In the adhoc, title-only task, thirty-four of fifty queries are over the median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChowdhuryBJSGFMH00.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChowdhuryBJSGFMH00,
		author = {Abdur Chowdhury and Steven M. Beitzel and Eric C. Jensen and M. Sailee and David A. Grossman and Ophir Frieder and M. Catherine McCabe and David O. Holmes},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{IIT} {TREC-9} - Entity Based Feedback with Fusion},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/iit-trec9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChowdhuryBJSGFMH00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melbourne TREC-9 Experiments

_Daryl J. D'Souza, Michael Fuller, James A. Thom, Phil Vines, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/mds.pdf](http://trec.nist.gov/pubs/trec9/papers/mds.pdf)
- :material-file-search: **Runs:** [rmitWFGweb](./runs.md#rmitwfgweb) | [rmitNFGweb](./runs.md#rmitnfgweb) | [rmitWFLweb](./runs.md#rmitwflweb) | [rmitNFLweb](./runs.md#rmitnflweb)

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

#### Web Document Retrieval Using Passage Retrieval, Connectivity Information,  and Automatic Link Weighting–TREC-9 Report

_Franco Crivellari, Massimo Melucci_

- :fontawesome-solid-user-group: **Participant:** [padova](./participants.md#padova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/padova.pdf](http://trec.nist.gov/pubs/trec9/papers/padova.pdf)
- :material-file-search: **Runs:** [PuShortAuth](./runs.md#pushortauth) | [PuShortWAuth](./runs.md#pushortwauth) | [PuShortBase](./runs.md#pushortbase) | [PuLongAuth](./runs.md#pulongauth) | [PuLongWAuth](./runs.md#pulongwauth) | [PuLongBase](./runs.md#pulongbase)

??? abstract "Abstract"
	
	This report describes the participation at the Web track of the TREC-9 of the Information Management Systems research group of the Department of Electronics and Computer Science at the University of Padova (Italy). TREC-9 has been our first participation to TREC and, then, to the Web track. In the following, we describe the experimental approach we have chosen, the research hypotheses and questions, the problems we encountered, the results we reached and our conclusions. We consider this experience as the first step towards the participation to the next Web tracks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CrivellariM00.bib) "
	```
	@inproceedings{DBLP:conf/trec/CrivellariM00,
		author = {Franco Crivellari and Massimo Melucci},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Web Document Retrieval Using Passage Retrieval, Connectivity Information, and Automatic Link Weighting--TREC-9 Report},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/padova.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CrivellariM00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SabIR Research at TREC-9

_Chris Buckley, Janet A. Walz_

- :fontawesome-solid-user-group: **Participant:** [sabir](./participants.md#sabir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/sabir.pdf](http://trec.nist.gov/pubs/trec9/papers/sabir.pdf)
- :material-file-search: **Runs:** [Sab9web1](./runs.md#sab9web1) | [Sab9web2](./runs.md#sab9web2) | [Sab9web3](./runs.md#sab9web3) | [Sab9web4](./runs.md#sab9web4) | [Sab9web5](./runs.md#sab9web5)

??? abstract "Abstract"
	
	Sabir Research participated in TREC-9 in a somewhat lower key fashion than normal. We participated only in the Main Web Task, and in the Query Track. Most of our interesting work and analysis was done in the Query Track, and is reported in the TREC-9 Query Track Overview. Here we report very briefly on the Main Web Task; briefly because there really isn't much interesting to say this year! [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleyW00.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleyW00,
		author = {Chris Buckley and Janet A. Walz},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {SabIR Research at {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/sabir.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleyW00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at trec9: Web and Filtering tasks

_M. Abchiche, Mohand Boughanem, Taoufiq Dkaki, Josiane Mothe, Chantal Soulé-Dupuy, Mohamed Tmar_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/irit_trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/irit_trec9.pdf)
- :material-file-search: **Runs:** [Mer9Wtnd](./runs.md#mer9wtnd) | [Mer9WtdMr](./runs.md#mer9wtdmr) | [Mer9Wt0](./runs.md#mer9wt0) | [Mer9Wt1](./runs.md#mer9wt1)

??? abstract "Abstract"
	
	The tests performed for TREC9 focus on the Web and Filtering (batch and routing) tracks. The submitted runs are based on the Mercure system. For one of the filtering routing runs, we combine Mercure with mining text functionalities from our system Tétralogie. We also performed some experiments taking hyperlinks into account to evaluate their influence on the retrieval effectiveness, but no runs were sent. Web: We submit four runs in this track. Two elements were tested: a modified Mercure term weighting scheme and the notion of the user preference on the retrieved document were tested. Filtering (batch and routing): our main investigation this year concerns the notion of non-relevant profile in a filtering system. The filtering consists on, first filtering the documents using a relevant profile learned from relevant documents, second re-filtering the selected documents using non-relevant profile learned from non-relevant documents so that non-relevant documents accepted by the relevant profile are rejected. This notion of non-relevant profile was introduced by Hoashi (6] in an adaptive system whereas we use this technique for a batch system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbchicheBDMST00.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbchicheBDMST00,
		author = {M. Abchiche and Mohand Boughanem and Taoufiq Dkaki and Josiane Mothe and Chantal Soul{\'{e}}{-}Dupuy and Mohamed Tmar},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure at trec9: Web and Filtering tasks},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/irit\_trec9.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbchicheBDMST00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

