# Proceedings 2000 

## Overview of the Ninth Text REtrieval Conference (TREC-9)

_Ellen M. Voorhees, Donna Harman_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/overview_9.pdf](http://trec.nist.gov/pubs/trec9/papers/overview_9.pdf)
??? abstract "Abstract"
	
	The ninth Text REtrieval Conference (TREC-9) was held at the National Institute of Standards and Technology (NIST) on November 13-16, 2000. The conference was co-sponsored by NIST, the Information Technology Office of the Defense Advanced Research Projects Agency (DARPA/ITO), and the Advanced Research and Development Activity (ARDA) office of the Department of Defense. TREC-9 is the latest in a series of workshops designed to foster research in text retrieval. The workshop series has four goals: to encourage research in text retrieval based on large test collections; to increase communication among industry, academia, and government by creating an open forum for the exchange of research ideas; to speed the transfer of technology from research labs into commercial products by demonstrating substantial improvements in retrieval methodologies on real-world problems; and to increase the availability of appropriate evaluation techniques for use by industry and academia, including development of new evaluation techniques more applicable to current systems. The previous eight TRECs each had an 'ad hoc' main task through which eight large test collections were built [17. In recognition that sufficient infrastructure exists to support researchers interested in this traditional retrieval task, the ad hoc main task was discontinued in TREC-9 so that more TREC resources could be focused on building evaluation infrastructure for other retrieval tasks (called 'tracks'). The seven tracks included in TREC-9 were Cross-Language Retrieval, Filtering, Interactive Retrieval, Query Analysis, Question Answering, Spoken Document Retrieval, and Web Retrieval. Table 1 lists the groups that participated in TREC-9. Sixty-nine groups including participants from 17 different countries were represented. The diversity of the participating groups ensures that TREC represents many different approaches to text retrieval. This paper serves as an introduction to the research described in detail in the remainder of the volume. The next section provides a summary of the retrieval background knowledge that is assumed in the other papers. Section 3 presents a short description of each track— a more complete description of a track can be found in that track's overview paper in the proceedings. The final section looks forward to future TREC conferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VoorheesH00.bib)"
	```
	@inproceedings{DBLP:conf/trec/VoorheesH00,
		author = {Ellen M. Voorhees and Donna Harman},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of the Ninth Text REtrieval Conference {(TREC-9)}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/overview\_9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VoorheesH00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Web 

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

- :fontawesome-solid-user-group: **Participant:** [CWI](./web/participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/trec9cwi.pdf](http://trec.nist.gov/pubs/trec9/papers/trec9cwi.pdf)
- :material-file-search: **Runs:** [CWI0001](./web/runs.md#cwi0001) | [CWI0000](./web/runs.md#cwi0000) | [CWI0002](./web/runs.md#cwi0002) | [CWI0010](./web/runs.md#cwi0010)

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

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./web/participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/humtrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/humtrec9.pdf)
- :material-file-search: **Runs:** [hum9tdn](./web/runs.md#hum9tdn) | [hum9te](./web/runs.md#hum9te) | [hum9tde](./web/runs.md#hum9tde) | [hum9td4](./web/runs.md#hum9td4)

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

- :fontawesome-solid-user-group: **Participant:** [ATT](./web/participants.md#att)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/att-trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/att-trec9.pdf)
- :material-file-search: **Runs:** [att0010gbe](./web/runs.md#att0010gbe) | [att0010gb](./web/runs.md#att0010gb) | [att0010gbt](./web/runs.md#att0010gbt) | [att0010gbl](./web/runs.md#att0010gbl) | [att0010glf](./web/runs.md#att0010glf) | [att0010glv](./web/runs.md#att0010glv)

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

- :fontawesome-solid-user-group: **Participant:** [Neuchatel](./web/participants.md#neuchatel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/unine9.pdf](http://trec.nist.gov/pubs/trec9/papers/unine9.pdf)
- :material-file-search: **Runs:** [NEnmLpas](./web/runs.md#nenmlpas) | [NEnmLsa](./web/runs.md#nenmlsa) | [NEnm](./web/runs.md#nenm) | [NEtm](./web/runs.md#netm) | [NENRtm](./web/runs.md#nenrtm) | [NENRtmLpas](./web/runs.md#nenrtmlpas)

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

- :fontawesome-solid-user-group: **Participant:** [ricoh](./web/participants.md#ricoh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/ricoh9-final.pdf](http://trec.nist.gov/pubs/trec9/papers/ricoh9-final.pdf)
- :material-file-search: **Runs:** [ric9dpx](./web/runs.md#ric9dpx) | [ric9dpn](./web/runs.md#ric9dpn) | [ric9dsx](./web/runs.md#ric9dsx) | [ric9dpxL](./web/runs.md#ric9dpxl) | [ric9tpx](./web/runs.md#ric9tpx)

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

- :fontawesome-solid-user-group: **Participant:** [newby](./web/participants.md#newby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/newby-t9.pdf](http://trec.nist.gov/pubs/trec9/papers/newby-t9.pdf)
- :material-file-search: **Runs:** [iswtd](./web/runs.md#iswtd) | [iswtdn](./web/runs.md#iswtdn) | [iswt](./web/runs.md#iswt) | [isnnwt](./web/runs.md#isnnwt)

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

- :fontawesome-solid-user-group: **Participant:** [Fujitsu](./web/participants.md#fujitsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/flab_trec9_paper_final.pdf](http://trec.nist.gov/pubs/trec9/papers/flab_trec9_paper_final.pdf)
- :material-file-search: **Runs:** [Flab9atN](./web/runs.md#flab9atn) | [Flab9atdN](./web/runs.md#flab9atdn) | [Flab9atdnN](./web/runs.md#flab9atdnn) | [Flab9atd2N](./web/runs.md#flab9atd2n)

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

- :fontawesome-solid-user-group: **Participant:** [apl-jhu](./web/participants.md#apl-jhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/jhuapl.pdf](http://trec.nist.gov/pubs/trec9/papers/jhuapl.pdf)
- :material-file-search: **Runs:** [apl9tdn](./web/runs.md#apl9tdn) | [apl9t](./web/runs.md#apl9t) | [apl9lt](./web/runs.md#apl9lt) | [apl9ltdn](./web/runs.md#apl9ltdn) | [apl9all](./web/runs.md#apl9all) | [apl9td](./web/runs.md#apl9td)

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

- :fontawesome-solid-user-group: **Participant:** [cuny](./web/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf](http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf)
- :material-file-search: **Runs:** [pir0Wttd](./web/runs.md#pir0wttd) | [pir0Watd](./web/runs.md#pir0watd) | [pir0Wtd2](./web/runs.md#pir0wtd2) | [pir0Wt1](./web/runs.md#pir0wt1) | [pir0WTTD](./web/runs.md#pir0wttd)

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

- :fontawesome-solid-user-group: **Participant:** [twenty-one](./web/participants.md#twenty-one)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/tno-ut.pdf](http://trec.nist.gov/pubs/trec9/papers/tno-ut.pdf)
- :material-file-search: **Runs:** [tnout9t2lk50](./web/runs.md#tnout9t2lk50) | [tnout9t2lc50](./web/runs.md#tnout9t2lc50) | [tnout9t2lc10](./web/runs.md#tnout9t2lc10) | [tnout9t2](./web/runs.md#tnout9t2) | [tnout9f1](./web/runs.md#tnout9f1)

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

- :fontawesome-solid-user-group: **Participant:** [ACSys](./web/participants.md#acsys)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/acsys.pdf](http://trec.nist.gov/pubs/trec9/papers/acsys.pdf)
- :material-file-search: **Runs:** [acsys9mw0](./web/runs.md#acsys9mw0)

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

- :fontawesome-solid-user-group: **Participant:** [dublin](./web/participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/dcu_trec9_final.pdf](http://trec.nist.gov/pubs/trec9/papers/dcu_trec9_final.pdf)
- :material-file-search: **Runs:** [dcu00ca](./web/runs.md#dcu00ca) | [dcu00la](./web/runs.md#dcu00la) | [dcu00lc](./web/runs.md#dcu00lc) | [dcu00lb](./web/runs.md#dcu00lb)

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

- :fontawesome-solid-user-group: **Participant:** [justsystems](./web/participants.md#justsystems)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/jscbt9w_paper.pdf](http://trec.nist.gov/pubs/trec9/papers/jscbt9w_paper.pdf)
- :material-file-search: **Runs:** [jscbt9wll1](./web/runs.md#jscbt9wll1) | [jscbt9wls1](./web/runs.md#jscbt9wls1) | [jscbt9wcs1](./web/runs.md#jscbt9wcs1) | [jscbt9wcl1](./web/runs.md#jscbt9wcl1) | [jscbt9wll2](./web/runs.md#jscbt9wll2) | [jscbt9wls2](./web/runs.md#jscbt9wls2)

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

- :fontawesome-solid-user-group: **Participant:** [IIT](./web/participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/iit-trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/iit-trec9.pdf)
- :material-file-search: **Runs:** [iit00m](./web/runs.md#iit00m) | [iit00td](./web/runs.md#iit00td) | [iit00tde](./web/runs.md#iit00tde) | [iit00t](./web/runs.md#iit00t)

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

- :fontawesome-solid-user-group: **Participant:** [RMIT](./web/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/mds.pdf](http://trec.nist.gov/pubs/trec9/papers/mds.pdf)
- :material-file-search: **Runs:** [rmitWFGweb](./web/runs.md#rmitwfgweb) | [rmitNFGweb](./web/runs.md#rmitnfgweb) | [rmitWFLweb](./web/runs.md#rmitwflweb) | [rmitNFLweb](./web/runs.md#rmitnflweb)

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

- :fontawesome-solid-user-group: **Participant:** [padova](./web/participants.md#padova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/padova.pdf](http://trec.nist.gov/pubs/trec9/papers/padova.pdf)
- :material-file-search: **Runs:** [PuShortAuth](./web/runs.md#pushortauth) | [PuShortWAuth](./web/runs.md#pushortwauth) | [PuShortBase](./web/runs.md#pushortbase) | [PuLongAuth](./web/runs.md#pulongauth) | [PuLongWAuth](./web/runs.md#pulongwauth) | [PuLongBase](./web/runs.md#pulongbase)

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

- :fontawesome-solid-user-group: **Participant:** [sabir](./web/participants.md#sabir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/sabir.pdf](http://trec.nist.gov/pubs/trec9/papers/sabir.pdf)
- :material-file-search: **Runs:** [Sab9web1](./web/runs.md#sab9web1) | [Sab9web2](./web/runs.md#sab9web2) | [Sab9web3](./web/runs.md#sab9web3) | [Sab9web4](./web/runs.md#sab9web4) | [Sab9web5](./web/runs.md#sab9web5)

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

- :fontawesome-solid-user-group: **Participant:** [IRIT](./web/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/irit_trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/irit_trec9.pdf)
- :material-file-search: **Runs:** [Mer9Wtnd](./web/runs.md#mer9wtnd) | [Mer9WtdMr](./web/runs.md#mer9wtdmr) | [Mer9Wt0](./web/runs.md#mer9wt0) | [Mer9Wt1](./web/runs.md#mer9wt1)

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

## Spoken Document Retrieval 

#### Spoken Document Retrieval Track Slides

_John S. Garofolo, J. Lard, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/sdrt9_slides/index.htm](http://trec.nist.gov/pubs/trec9/sdrt9_slides/index.htm)
??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarofoloLV00.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarofoloLV00,
		author = {John S. Garofolo and J. Lard and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Spoken Document Retrieval Track Slides},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/sdrt9\_slides/index.htm},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GarofoloLV00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Thisl SDR System at TREC-9

_Steve Renals, Dave Abberley_

- :fontawesome-solid-user-group: **Participant:** [THISL](./sdr/participants.md#thisl)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/sheffield-sdr.pdf](http://trec.nist.gov/pubs/trec9/papers/sheffield-sdr.pdf)
- :material-file-search: **Runs:** [shef-b1tk](./sdr/runs.md#shef-b1tk) | [shef-b1tu](./sdr/runs.md#shef-b1tu) | [shef-crsu-cuhtk1p1u](./sdr/runs.md#shef-crsu-cuhtk1p1u) | [shef-crsu-cuhtk1u](./sdr/runs.md#shef-crsu-cuhtk1u) | [shef-crsu-limsi2u](./sdr/runs.md#shef-crsu-limsi2u) | [shef-crtu-limsi2u](./sdr/runs.md#shef-crtu-limsi2u) | [shef-crtu-limsi1u](./sdr/runs.md#shef-crtu-limsi1u) | [shef-crtu-cuhtk1u](./sdr/runs.md#shef-crtu-cuhtk1u) | [shef-crtu-cuhtk1p1u](./sdr/runs.md#shef-crtu-cuhtk1p1u) | [shef-r1sk](./sdr/runs.md#shef-r1sk) | [shef-r1su](./sdr/runs.md#shef-r1su) | [shef-r1tk](./sdr/runs.md#shef-r1tk) | [shef-r1tu](./sdr/runs.md#shef-r1tu) | [shef-s1sk-shef1u](./sdr/runs.md#shef-s1sk-shef1u) | [shef-s1su-shef1u](./sdr/runs.md#shef-s1su-shef1u) | [shef-s1tk-shef1u](./sdr/runs.md#shef-s1tk-shef1u) | [shef-s1tu-shef1u](./sdr/runs.md#shef-s1tu-shef1u) | [shef-s2tu-shef2u](./sdr/runs.md#shef-s2tu-shef2u) | [shef-s2tk-shef2u](./sdr/runs.md#shef-s2tk-shef2u) | [shef-s2sk-shef2u](./sdr/runs.md#shef-s2sk-shef2u) | [shef-s2su-shef2u](./sdr/runs.md#shef-s2su-shef2u) | [shef-crsu-limsi1u](./sdr/runs.md#shef-crsu-limsi1u) | [shef-b1su](./sdr/runs.md#shef-b1su) | [shef-b1sk](./sdr/runs.md#shef-b1sk)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC-9 Spoken Document Retrieval (SDR) track. The THISL SDR system consists of a realtime version of a hybrid connection-ist/HMM large vocabulary speech recognition system and a probabilistic text retrieval system. This paper describes the configuration of the speech recognition and text retrieval systems, including segmentation and query expansion. We report our results for development tests using the TREC-8 queries, and for the TREC-9 evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RenalsA00.bib) "
	```
	@inproceedings{DBLP:conf/trec/RenalsA00,
		author = {Steve Renals and Dave Abberley},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The Thisl {SDR} System at {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/sheffield-sdr.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RenalsA00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Spoken Document Retrieval for TREC-9 at Cambridge University

_Sue E. Johnson, Pierre Jourlin, Karen Sparck Jones, Philip C. Woodland_

- :fontawesome-solid-user-group: **Participant:** [cambridge](./sdr/participants.md#cambridge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/cuhtk_trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/cuhtk_trec9.pdf)
- :material-file-search: **Runs:** [cuhtk-b1su](./sdr/runs.md#cuhtk-b1su) | [cuhtk-b1sun](./sdr/runs.md#cuhtk-b1sun) | [cuhtk-b1tu](./sdr/runs.md#cuhtk-b1tu) | [cuhtk-b1tun](./sdr/runs.md#cuhtk-b1tun) | [cuhtk-crsu-cuhtk99s1p1u](./sdr/runs.md#cuhtk-crsu-cuhtk99s1p1u) | [cuhtk-crsu-limsi1u](./sdr/runs.md#cuhtk-crsu-limsi1u) | [cuhtk-crsu-limsi2u](./sdr/runs.md#cuhtk-crsu-limsi2u) | [cuhtk-crsu-nist99b1u](./sdr/runs.md#cuhtk-crsu-nist99b1u) | [cuhtk-crsu-shef1u](./sdr/runs.md#cuhtk-crsu-shef1u) | [cuhtk-crsu-shef2u](./sdr/runs.md#cuhtk-crsu-shef2u) | [cuhtk-crtu-cuhtk99s1p1u](./sdr/runs.md#cuhtk-crtu-cuhtk99s1p1u) | [cuhtk-crtu-limsi1u](./sdr/runs.md#cuhtk-crtu-limsi1u) | [cuhtk-crtu-limsi2u](./sdr/runs.md#cuhtk-crtu-limsi2u) | [cuhtk-crtu-nist99b1u](./sdr/runs.md#cuhtk-crtu-nist99b1u) | [cuhtk-crtu-shef1u](./sdr/runs.md#cuhtk-crtu-shef1u) | [cuhtk-crtu-shef2u](./sdr/runs.md#cuhtk-crtu-shef2u) | [cuhtk-r1su](./sdr/runs.md#cuhtk-r1su) | [cuhtk-r1sun](./sdr/runs.md#cuhtk-r1sun) | [cuhtk-r1tu](./sdr/runs.md#cuhtk-r1tu) | [cuhtk-r1tun](./sdr/runs.md#cuhtk-r1tun) | [cuhtk-s1su](./sdr/runs.md#cuhtk-s1su) | [cuhtk-s1sun](./sdr/runs.md#cuhtk-s1sun) | [cuhtk-s1tu](./sdr/runs.md#cuhtk-s1tu) | [cuhtk-s1tun](./sdr/runs.md#cuhtk-s1tun) | [cuhtk-r1tk](./sdr/runs.md#cuhtk-r1tk) | [cuhtk-r1sk](./sdr/runs.md#cuhtk-r1sk) | [cuhtk-s1sk](./sdr/runs.md#cuhtk-s1sk) | [cuhtk-s1tk](./sdr/runs.md#cuhtk-s1tk) | [cuhtk-b1tk](./sdr/runs.md#cuhtk-b1tk) | [cuhtk-b1sk](./sdr/runs.md#cuhtk-b1sk)

??? abstract "Abstract"
	
	This paper presents work done at Cambridge University for the TREC-9 Spoken Document Retrieval (SDR) track. The CU-HTK transcriptions from TREC-8 with Word Error Rate (WER) of 20.5% were used in conjunction with stopping, Porter stem-ming, Okapi-style weighting and query expansion using a contemporaneous corpus of newswire. A windowing/recombination strategy was applied for the case where story boundaries were unknown (SU) obtaining a final result of 38.8% and 43.0% Average Precision for the TREC-9 short and terse queries respec-tively. The corresponding results for the story boundaries known runs (SK) were 49.5% and 51.9%. Document expansion was used in the SK runs and shown to also be beneficial for SU under certain circumstances. Non-lexical information was generated, which although not used within the evaluation, should prove useful to enrich the transcriptions in real-world applications. Fi-nally, cross recogniser experiments again showed there is little performance degradation as WER increases and thus SDR now needs new challenges such as integration with video data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JohnsonJJW00.bib) "
	```
	@inproceedings{DBLP:conf/trec/JohnsonJJW00,
		author = {Sue E. Johnson and Pierre Jourlin and Karen Sparck Jones and Philip C. Woodland},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Spoken Document Retrieval for {TREC-9} at Cambridge University},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/cuhtk\_trec9.pdf},
		timestamp = {Wed, 05 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JohnsonJJW00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The LIMSI SDR System for TREC-9

_Jean-Luc Gauvain, Lori Lamel, Claude Barras, Gilles Adda, Yannick de Kercadio_

- :fontawesome-solid-user-group: **Participant:** [limsi-tlp](./sdr/participants.md#limsi-tlp)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/limsi-sdr00.pdf](http://trec.nist.gov/pubs/trec9/papers/limsi-sdr00.pdf)
- :material-file-search: **Runs:** [limsi-r1sk](./sdr/runs.md#limsi-r1sk) | [limsi-r1su](./sdr/runs.md#limsi-r1su) | [limsi-r1tk](./sdr/runs.md#limsi-r1tk) | [limsi-r1tu](./sdr/runs.md#limsi-r1tu) | [limsi-s1sk-limsi2u](./sdr/runs.md#limsi-s1sk-limsi2u) | [limsi-s1su-limsi2u](./sdr/runs.md#limsi-s1su-limsi2u) | [limsi-s1tk-limsi2u](./sdr/runs.md#limsi-s1tk-limsi2u) | [limsi-s1tu-limsi2u](./sdr/runs.md#limsi-s1tu-limsi2u) | [limsi-b1su.old](./sdr/runs.md#limsi-b1su.old) | [limsi-b1tu.old](./sdr/runs.md#limsi-b1tu.old) | [limsi-b1su](./sdr/runs.md#limsi-b1su) | [limsi-b1tu](./sdr/runs.md#limsi-b1tu)

??? abstract "Abstract"
	
	In this paper we describe the LIMSI Spoken Document Retrieval system used in the TREC-9 evaluation. This system combines an adapted version of the LIMSI 1999 Hub-4E transcription system for speech recognition with text-based IR methods. Compared with the LIMSI TREC-8 system, this year's system is able to index the audio data without knowledge of the story boundaries using a double windowing approach. The query expansion procedure of the information retrieval component has been revised and makes use of contemporaneous text sources. Experimental results are reported in terms of mean average precision for both the TREC SDR'99 and SDR'00 queries using the same 557h data set. The mean average precision of this year's system is 0.5250 for SDR'99 and 0.3706 for SDR'00 for the focus unknown story boundary condition with a 20% word error rate.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GauvainLBAK00.bib) "
	```
	@inproceedings{DBLP:conf/trec/GauvainLBAK00,
		author = {Jean{-}Luc Gauvain and Lori Lamel and Claude Barras and Gilles Adda and Yannick de Kercadio},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {LIMSI} {SDR} System for {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/limsi-sdr00.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GauvainLBAK00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Question Answering 

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

- :fontawesome-solid-user-group: **Participant:** [fudan](./qa/participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf](http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf)
- :material-file-search: **Runs:** [FDUT9QS1](./qa/runs.md#fdut9qs1) | [FDUT9QL1](./qa/runs.md#fdut9ql1) | [FDUT9QL2](./qa/runs.md#fdut9ql2) | [FDUT9QS2](./qa/runs.md#fdut9qs2)

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

- :fontawesome-solid-user-group: **Participant:** [SUN](./qa/participants.md#sun)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/sun-trec9-final.pdf](http://trec.nist.gov/pubs/trec9/papers/sun-trec9-final.pdf)
- :material-file-search: **Runs:** [SunOne](./qa/runs.md#sunone) | [SunToo](./qa/runs.md#suntoo)

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

- :fontawesome-solid-user-group: **Participant:** [ntt-data](./qa/participants.md#ntt-data)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/nttdata9.pdf](http://trec.nist.gov/pubs/trec9/papers/nttdata9.pdf)
- :material-file-search: **Runs:** [NTTD9QAa1S](./qa/runs.md#nttd9qaa1s) | [NTTD9QAa2S](./qa/runs.md#nttd9qaa2s) | [NTTD9QAa1L](./qa/runs.md#nttd9qaa1l) | [NTTD9QAb1L](./qa/runs.md#nttd9qab1l)

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

- :fontawesome-solid-user-group: **Participant:** [sheffield](./qa/participants.md#sheffield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/shef-trec9-qa-final.pdf](http://trec.nist.gov/pubs/trec9/papers/shef-trec9-qa-final.pdf)
- :material-file-search: **Runs:** [shef50ea](./qa/runs.md#shef50ea) | [shef50](./qa/runs.md#shef50) | [shef250](./qa/runs.md#shef250) | [shef250p](./qa/runs.md#shef250p)

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

- :fontawesome-solid-user-group: **Participant:** [ibmQA](./qa/participants.md#ibmqa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/PragerTrec9notebook.pdf](http://trec.nist.gov/pubs/trec9/papers/PragerTrec9notebook.pdf)
- :material-file-search: **Runs:** [IBMKR250](./qa/runs.md#ibmkr250) | [IBMKA250](./qa/runs.md#ibmka250) | [IBMKA50](./qa/runs.md#ibmka50) | [IBMKR50](./qa/runs.md#ibmkr50)

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

- :fontawesome-solid-user-group: **Participant:** [clresearch](./qa/participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/clresearch00.pdf](http://trec.nist.gov/pubs/trec9/papers/clresearch00.pdf)
- :material-file-search: **Runs:** [clr00b1](./qa/runs.md#clr00b1) | [clr00b2](./qa/runs.md#clr00b2) | [clr00s1](./qa/runs.md#clr00s1) | [clr00s2](./qa/runs.md#clr00s2)

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

- :fontawesome-solid-user-group: **Participant:** [NTU](./qa/participants.md#ntu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/ntuintrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/ntuintrec9.pdf)
- :material-file-search: **Runs:** [qntua02](./qa/runs.md#qntua02) | [qntua01](./qa/runs.md#qntua01) | [qntua03](./qa/runs.md#qntua03)

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

- :fontawesome-solid-user-group: **Participant:** [KAIST](./qa/participants.md#kaist)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/kaist-trec9-qa-filtering.pdf](http://trec.nist.gov/pubs/trec9/papers/kaist-trec9-qa-filtering.pdf)
- :material-file-search: **Runs:** [KAIST9qa1](./qa/runs.md#kaist9qa1) | [KAIST9qa2](./qa/runs.md#kaist9qa2)

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

- :fontawesome-solid-user-group: **Participant:** [UMontreal](./qa/participants.md#umontreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/udempaperqafinal10p.pdf](http://trec.nist.gov/pubs/trec9/papers/udempaperqafinal10p.pdf)
- :material-file-search: **Runs:** [UdeMlng1](./qa/runs.md#udemlng1) | [UdeMlng2](./qa/runs.md#udemlng2) | [UdeMshrt](./qa/runs.md#udemshrt) | [UdeMexct](./qa/runs.md#udemexct)

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

- :fontawesome-solid-user-group: **Participant:** [cuny](./qa/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf](http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf)
- :material-file-search: **Runs:** [pir0qas1](./qa/runs.md#pir0qas1) | [pir0qas2](./qa/runs.md#pir0qas2) | [pir0qal1](./qa/runs.md#pir0qal1) | [pir0qal2](./qa/runs.md#pir0qal2)

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

- :fontawesome-solid-user-group: **Participant:** [korea](./qa/participants.md#korea)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/kuqa.pdf](http://trec.nist.gov/pubs/trec9/papers/kuqa.pdf)
- :material-file-search: **Runs:** [KUQA250a](./qa/runs.md#kuqa250a) | [KUQA250b](./qa/runs.md#kuqa250b) | [KUQA50a](./qa/runs.md#kuqa50a) | [KUQA50b](./qa/runs.md#kuqa50b)

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

- :fontawesome-solid-user-group: **Participant:** [ibm-franz](./qa/participants.md#ibm-franz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/ibm_qa.pdf](http://trec.nist.gov/pubs/trec9/papers/ibm_qa.pdf)
- :material-file-search: **Runs:** [ibmhlt0050](./qa/runs.md#ibmhlt0050) | [ibmhlt00250](./qa/runs.md#ibmhlt00250)

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

- :fontawesome-solid-user-group: **Participant:** [ISI-USC](./qa/participants.md#isi-usc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/webclopedia.pdf](http://trec.nist.gov/pubs/trec9/papers/webclopedia.pdf)
- :material-file-search: **Runs:** [ISI0A50](./qa/runs.md#isi0a50)

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

- :fontawesome-solid-user-group: **Participant:** [SMU](./qa/participants.md#smu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/smu.pdf](http://trec.nist.gov/pubs/trec9/papers/smu.pdf)
- :material-file-search: **Runs:** [LCCSMU1](./qa/runs.md#lccsmu1) | [LCCSMU2](./qa/runs.md#lccsmu2)

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

- :fontawesome-solid-user-group: **Participant:** [Alicante](./qa/participants.md#alicante)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/alicante_trec_9_paper.pdf](http://trec.nist.gov/pubs/trec9/papers/alicante_trec_9_paper.pdf)
- :material-file-search: **Runs:** [ALI9A250](./qa/runs.md#ali9a250) | [ALI9A50](./qa/runs.md#ali9a50) | [ALI9C250](./qa/runs.md#ali9c250) | [ALI9C50](./qa/runs.md#ali9c50)

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

- :fontawesome-solid-user-group: **Participant:** [limsi](./qa/participants.md#limsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/qalc-limsilc.pdf](http://trec.nist.gov/pubs/trec9/papers/qalc-limsilc.pdf)
- :material-file-search: **Runs:** [lcat050](./qa/runs.md#lcat050) | [lcat250](./qa/runs.md#lcat250) | [lcix250](./qa/runs.md#lcix250)

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

- :fontawesome-solid-user-group: **Participant:** [microsoft](./qa/participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/msrc-qa.pdf](http://trec.nist.gov/pubs/trec9/papers/msrc-qa.pdf)
- :material-file-search: **Runs:** [msq9L50](./qa/runs.md#msq9l50) | [msq9L250](./qa/runs.md#msq9l250)

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

- :fontawesome-solid-user-group: **Participant:** [Syracuse](./qa/participants.md#syracuse)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/cnlptrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/cnlptrec9.pdf)
- :material-file-search: **Runs:** [SUT9p2c3c050](./qa/runs.md#sut9p2c3c050) | [SUT9p2c3c250](./qa/runs.md#sut9p2c3c250) | [SUT9bn3c050](./qa/runs.md#sut9bn3c050) | [SUT9bn3c250](./qa/runs.md#sut9bn3c250)

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

- :fontawesome-solid-user-group: **Participant:** [imperial](./qa/participants.md#imperial)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/icrjc99a.pdf](http://trec.nist.gov/pubs/trec9/papers/icrjc99a.pdf)
- :material-file-search: **Runs:** [ICrjc99a](./qa/runs.md#icrjc99a) | [ICrjc99b](./qa/runs.md#icrjc99b)

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

- :fontawesome-solid-user-group: **Participant:** [waterloo](./qa/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/mt9.pdf](http://trec.nist.gov/pubs/trec9/papers/mt9.pdf)
- :material-file-search: **Runs:** [uwmt9qas0](./qa/runs.md#uwmt9qas0) | [uwmt9qal0](./qa/runs.md#uwmt9qal0) | [uwmt9qas1](./qa/runs.md#uwmt9qas1) | [uwmt9qal1](./qa/runs.md#uwmt9qal1)

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

- :fontawesome-solid-user-group: **Participant:** [iowa](./qa/participants.md#iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/iowa.pdf](http://trec.nist.gov/pubs/trec9/papers/iowa.pdf)
- :material-file-search: **Runs:** [UIQA002](./qa/runs.md#uiqa002) | [UIQA001](./qa/runs.md#uiqa001)

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

- :fontawesome-solid-user-group: **Participant:** [mitre](./qa/participants.md#mitre)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/mitre.pdf](http://trec.nist.gov/pubs/trec9/papers/mitre.pdf)
- :material-file-search: **Runs:** [MTR00S1](./qa/runs.md#mtr00s1) | [MTR00L1](./qa/runs.md#mtr00l1) | [MTR00X1](./qa/runs.md#mtr00x1) | [MTR00Y1](./qa/runs.md#mtr00y1)

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

- :fontawesome-solid-user-group: **Participant:** [Pisa](./qa/participants.md#pisa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/pisab.pdf](http://trec.nist.gov/pubs/trec9/papers/pisab.pdf)
- :material-file-search: **Runs:** [PISA0](./qa/runs.md#pisa0) | [PISAB](./qa/runs.md#pisab) | [PISAS](./qa/runs.md#pisas)

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

- :fontawesome-solid-user-group: **Participant:** [umass](./qa/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/umass-trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/umass-trec9.pdf)
- :material-file-search: **Runs:** [INQ9WSUM](./qa/runs.md#inq9wsum) | [INQ9AND](./qa/runs.md#inq9and)

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

## Cross-Language 

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

- :fontawesome-solid-user-group: **Participant:** [BBN](./xlingual/participants.md#bbn)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/bbn-trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/bbn-trec9.pdf)
- :material-file-search: **Runs:** [BBN9XLA](./xlingual/runs.md#bbn9xla) | [BBN9XLB](./xlingual/runs.md#bbn9xlb) | [BBN9XLC](./xlingual/runs.md#bbn9xlc) | [BBN9MONO](./xlingual/runs.md#bbn9mono)

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

- :fontawesome-solid-user-group: **Participant:** [fudan](./xlingual/participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf](http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf)
- :material-file-search: **Runs:** [fdut9xl1](./xlingual/runs.md#fdut9xl1) | [fdut9xl2](./xlingual/runs.md#fdut9xl2) | [fdut9xl3](./xlingual/runs.md#fdut9xl3) | [fdut9xl4](./xlingual/runs.md#fdut9xl4)

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

- :fontawesome-solid-user-group: **Participant:** [textwise](./xlingual/participants.md#textwise)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/TextWise-TREC9.pdf](http://trec.nist.gov/pubs/trec9/papers/TextWise-TREC9.pdf)
- :material-file-search: **Runs:** [TWe2c3CItdn](./xlingual/runs.md#twe2c3citdn) | [TWmono3CItdn](./xlingual/runs.md#twmono3citdn)

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

- :fontawesome-solid-user-group: **Participant:** [UMaryland](./xlingual/participants.md#umaryland)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/umd-final.pdf](http://trec.nist.gov/pubs/trec9/papers/umd-final.pdf)
- :material-file-search: **Runs:** [TB](./xlingual/runs.md#tb) | [percent](./xlingual/runs.md#percent) | [mixed](./xlingual/runs.md#mixed)

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

- :fontawesome-solid-user-group: **Participant:** [apl-jhu](./xlingual/participants.md#apl-jhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/jhuapl.pdf](http://trec.nist.gov/pubs/trec9/papers/jhuapl.pdf)
- :material-file-search: **Runs:** [apl9xcmb](./xlingual/runs.md#apl9xcmb) | [apl9xmon](./xlingual/runs.md#apl9xmon) | [apl9xwrd](./xlingual/runs.md#apl9xwrd) | [apl9xtop](./xlingual/runs.md#apl9xtop)

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

- :fontawesome-solid-user-group: **Participant:** [NTU](./xlingual/participants.md#ntu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/ntuintrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/ntuintrec9.pdf)
- :material-file-search: **Runs:** [ecirntuco](./xlingual/runs.md#ecirntuco) | [ecirntua1](./xlingual/runs.md#ecirntua1)

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

- :fontawesome-solid-user-group: **Participant:** [KAIST](./xlingual/participants.md#kaist)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/kaist-trec9-qa-filtering.pdf](http://trec.nist.gov/pubs/trec9/papers/kaist-trec9-qa-filtering.pdf)
- :material-file-search: **Runs:** [KAIST9xlch](./xlingual/runs.md#kaist9xlch) | [KAIST9xlmt](./xlingual/runs.md#kaist9xlmt) | [KAIST9xlqt](./xlingual/runs.md#kaist9xlqt) | [KAIST9xlqm](./xlingual/runs.md#kaist9xlqm)

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

- :fontawesome-solid-user-group: **Participant:** [cuny](./xlingual/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf](http://trec.nist.gov/pubs/trec9/papers/pircst9.pdf)
- :material-file-search: **Runs:** [pir0Xori](./xlingual/runs.md#pir0xori) | [pir0Xdin](./xlingual/runs.md#pir0xdin) | [pir0Xhnd](./xlingual/runs.md#pir0xhnd) | [pir0XHxD](./xlingual/runs.md#pir0xhxd)

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

- :fontawesome-solid-user-group: **Participant:** [CUHK](./xlingual/participants.md#cuhk)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/cuhk_clir_trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/cuhk_clir_trec9.pdf)
- :material-file-search: **Runs:** [CHUHK00XEC1](./xlingual/runs.md#chuhk00xec1) | [CHUHK00CH1](./xlingual/runs.md#chuhk00ch1)

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

- :fontawesome-solid-user-group: **Participant:** [microsoft-china](./xlingual/participants.md#microsoft-china)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/trec-9.pdf](http://trec.nist.gov/pubs/trec9/papers/trec-9.pdf)
- :material-file-search: **Runs:** [msrcn1](./xlingual/runs.md#msrcn1) | [msrcn2](./xlingual/runs.md#msrcn2) | [msrcn3](./xlingual/runs.md#msrcn3)

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

- :fontawesome-solid-user-group: **Participant:** [ibm-franz](./xlingual/participants.md#ibm-franz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/ibm_clir.pdf](http://trec.nist.gov/pubs/trec9/papers/ibm_clir.pdf)
- :material-file-search: **Runs:** [ibmcl9s](./xlingual/runs.md#ibmcl9s) | [ibmcl9a](./xlingual/runs.md#ibmcl9a) | [ibmcl9m](./xlingual/runs.md#ibmcl9m)

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

- :fontawesome-solid-user-group: **Participant:** [RMIT](./xlingual/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/mds.pdf](http://trec.nist.gov/pubs/trec9/papers/mds.pdf)
- :material-file-search: **Runs:** [rmitcl001](./xlingual/runs.md#rmitcl001) | [rmitcl002](./xlingual/runs.md#rmitcl002) | [rmitcl003](./xlingual/runs.md#rmitcl003) | [rmitcl004](./xlingual/runs.md#rmitcl004)

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

- :fontawesome-solid-user-group: **Participant:** [berkeley-clir](./xlingual/participants.md#berkeley-clir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/trec9_berkeley.pdf](http://trec.nist.gov/pubs/trec9/papers/trec9_berkeley.pdf)
- :material-file-search: **Runs:** [BRKECA1](./xlingual/runs.md#brkeca1) | [BRKCCA1](./xlingual/runs.md#brkcca1) | [BRKECA2](./xlingual/runs.md#brkeca2) | [BRKECM1](./xlingual/runs.md#brkecm1)

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

- :fontawesome-solid-user-group: **Participant:** [umass](./xlingual/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/umass-trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/umass-trec9.pdf)
- :material-file-search: **Runs:** [INQ7XL1](./xlingual/runs.md#inq7xl1) | [INQ7XL2](./xlingual/runs.md#inq7xl2) | [INQ7XL3](./xlingual/runs.md#inq7xl3) | [INQ7XL4](./xlingual/runs.md#inq7xl4)

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

## Filtering 

#### The TREC-9 Filtering Track Final Report

_Stephen E. Robertson, David A. Hull_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/filtering_new.pdf](http://trec.nist.gov/pubs/trec9/papers/filtering_new.pdf)
??? abstract "Abstract"
	
	The TREC-9 filtering track measures the ability of systems to build persistent user profiles which successfully separate relevant and non-relevant documents. It consists of three major subtasks: adaptive filtering, batch filtering, and routing. In adaptive filtering, the system begins with only a topic statement and a small number of positive examples, and must learn a better profile from on-line feedback. Batch filtering and routing are more traditional machine learning tasks where the system begins with a large sample of evaluated training documents. This report describes the track, presents some evaluation results, and provides a general commentary on lessons learned from this year's track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonH00.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonH00,
		author = {Stephen E. Robertson and David A. Hull},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-9} Filtering Track Final Report},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/filtering\_new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonH00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### YFilter at TREC-9

_Yi Zhang, James P. Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu-lti](./filtering/participants.md#cmu-lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/cmu-dirtrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/cmu-dirtrec9.pdf)
- :material-file-search: **Runs:** [CMUDIR11](./filtering/runs.md#cmudir11) | [CMUDIR18](./filtering/runs.md#cmudir18) | [CMUDIR12](./filtering/runs.md#cmudir12) | [CMUDIR13](./filtering/runs.md#cmudir13) | [CMUDIR14](./filtering/runs.md#cmudir14) | [CMUDIR15](./filtering/runs.md#cmudir15) | [CMUDIR16](./filtering/runs.md#cmudir16) | [CMUDIR17](./filtering/runs.md#cmudir17)

??? abstract "Abstract"
	
	We built a filtering system YFILTER this year, which we used for experiments on profile updating and thresholds setting. Our focus is using incremental Rocchio for introducing new query terms and term weighting. Although 1, 0.5, 0.25 is a widely used Rocchio ratio for query expansion based on relevance feedback, we found that the optimal setting for information filtering is corpus and profile dependent. In addition to a new Rocchio ratio, we tested a modified idf measure for term weighting (ydf) that is biased towards words with middle range term frequency.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangC00.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangC00,
		author = {Yi Zhang and James P. Callan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {YFilter at {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/cmu-dirtrec9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangC00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC-9: CLIR, Filtering and QA Tasks

_Lide Wu, Xuanjing Huang, Yikun Guo, Bingwei Liu, Yuejie Zhang_

- :fontawesome-solid-user-group: **Participant:** [ICDC](./filtering/participants.md#icdc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf](http://trec.nist.gov/pubs/trec9/papers/FduT9Report.pdf)
- :material-file-search: **Runs:** [S2RNsamp](./filtering/runs.md#s2rnsamp) | [S2RNr1](./filtering/runs.md#s2rnr1) | [S2RNr2](./filtering/runs.md#s2rnr2)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC-9 conference for the first time. We have participated in three tracks of CLIR, Filtering and QA. We have submitted four runs for CLIR track. Bilingual knowledge source and statistical-based search engine are integrated in our CLIR system. We varied our strategy somewhat between runs: long query (both title and description field of the queries involved) with pseudo relevance feedback (FDUT9L1), long query with no feedback (FDUT9XL2), median query (just description field of queries involved) with feedback (FDUT9XL3) and, the last, mono long query with feedback (FDUT9XL4). For filtering, we participate in the sub-task of adaptive filtering and batch filtering. Vector representation and computation are heavily applied in filtering procedure. 11 runs of various combination of topic and evaluation measure have been submitted: 4 OHSU runs, 1 MeSH run and 2 MSH-SAMPLE runs for adaptive filtering, and 2 OHSU runs, 1 MeSH run and 1 MSH-SAMPLE run for batch filtering. Our QA system consists of three components: Question Analyzer, Candidate Window Searcher and Answer Extractor. We submitted two runs in the 50-byte category and two runs in the 250-byte category. The runs of 'FDUT9QL1' and 'FDUTIQSI' are extracted from the top 100 candidate windows. The other two runs of 'FDUT9QL2' and 'FDUTIQS1' are extracted from the top 24 candidate windows.
	

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

#### Training Context-Sensitive Neural Networks with Few Relevant Examples  for the TREC-9 Routing

_Mathieu Stricker, Frantz Vichot, Gérard Dreyfus, Francis Wolinski_

- :fontawesome-solid-user-group: **Participant:** [ICDC](./filtering/participants.md#icdc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/icdc_final.pdf](http://trec.nist.gov/pubs/trec9/papers/icdc_final.pdf)
- :material-file-search: **Runs:** [S2RNsamp](./filtering/runs.md#s2rnsamp) | [S2RNr1](./filtering/runs.md#s2rnr1) | [S2RNr2](./filtering/runs.md#s2rnr2)

??? abstract "Abstract"
	
	The present paper describes our second participation to the routing task; it features improvements over our previous approach [Stricker et al., 2000]. Our former model used a 'bag of words' for text representation with a feature selection, and a neural network without hidden neuron (i.e. a logistic regression), to estimate the probability of relevance of each document. This approach was close to the ones proposed by [Schütze et al., 1995] or [Wiener et al., 1995] but its original feature was the use of very few relevant features for text representation (25 features per topic on the average for the TREC-8 Routing). In this paper, two main improvements are proposed: The feature selection defines target words for which vectors of local contexts are subsequently defined. These vectors help disambiguate the target words and are defined by an analysis of both the relevant and the irrelevant documents of the training set. This new representation requires large neural networks, which are therefore prone to overfitting. A regularization technique is applied during training to favor smoother network mappings, thereby avoiding overfitting. This was achieved by adding a weight decay term to the usual cost function. This approach led to good results on the MeSH Sample topics (S2RNsamp) and on the OHSUMED topics (S2RNrl and S2RNr2).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StrickerVDW00.bib) "
	```
	@inproceedings{DBLP:conf/trec/StrickerVDW00,
		author = {Mathieu Stricker and Frantz Vichot and G{\'{e}}rard Dreyfus and Francis Wolinski},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Training Context-Sensitive Neural Networks with Few Relevant Examples for the {TREC-9} Routing},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/icdc\_final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StrickerVDW00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC-9: Filtering Track

_Stephen E. Robertson, Steve Walker_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./filtering/participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/msrc-fq.pdf](http://trec.nist.gov/pubs/trec9/papers/msrc-fq.pdf)
- :material-file-search: **Runs:** [ok9bf2po](./filtering/runs.md#ok9bf2po) | [ok9bfr2po](./filtering/runs.md#ok9bfr2po) | [ok9rf2po](./filtering/runs.md#ok9rf2po) | [ok9rfr2po](./filtering/runs.md#ok9rfr2po) | [ok9f2pm](./filtering/runs.md#ok9f2pm) | [ok9f1us](./filtering/runs.md#ok9f1us) | [ok9f3us](./filtering/runs.md#ok9f3us) | [ok9rfr2ps](./filtering/runs.md#ok9rfr2ps) | [ok9bfr2ps](./filtering/runs.md#ok9bfr2ps) | [ok9f3uo](./filtering/runs.md#ok9f3uo) | [ok9f1uo](./filtering/runs.md#ok9f1uo) | [ok9f1po](./filtering/runs.md#ok9f1po) | [ok9f2po](./filtering/runs.md#ok9f2po)

??? abstract "Abstract"
	
	Apart from a short description of our Query Track contri-bution, this report is concerned with the Adaptive Filtering track only. There is a separate report in this volume [1] on the Microsoft Research Cambridge participation in QA track. A number of runs were submitted for the Adaptive Filtering track, on all tasks (adaptive filtering, batch filtering and routing; three separate query sets; two evaluation measures). The filtering system is somewhat more advanced than the one used for TREC-8, and includes query modification and a more highly developed scheme for threshold adaptation. A number of diagnostic runs are also reported here.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonW00.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonW00,
		author = {Stephen E. Robertson and Steve Walker},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Microsoft Cambridge at {TREC-9:} Filtering Track},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/msrc-fq.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonW00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-9 Experiments at KAIST: QA, CLIR and Batch Filtering

_Kyung-Soon Lee, Jong-Hoon Oh, Jin-Xia Huang, Jae-Ho Kim, Key-Sun Choi_

- :fontawesome-solid-user-group: **Participant:** [KAIST](./filtering/participants.md#kaist)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/kaist-trec9-qa-filtering.pdf](http://trec.nist.gov/pubs/trec9/papers/kaist-trec9-qa-filtering.pdf)
- :material-file-search: **Runs:** [KAIST9bfms](./filtering/runs.md#kaist9bfms) | [KAIST9bfo1](./filtering/runs.md#kaist9bfo1) | [KAIST9bfo2](./filtering/runs.md#kaist9bfo2)

??? abstract "Abstract"
	
	In TREC-9, we participated in three tasks: question answering task, cross-language retrieval task, and batch filtering task in the filtering task. Our question answering system consists of following basic components - query analyzer, Named entity tagger, Answer Extractor. First, question analyzer analyzes the given question. Question analyzer generates question type and keywords of the given question. Then retrieved documents are analyzed for extracting relevant answer. POS tagger and Named entity tagger are used for the purpose. Finally, Answer Extractor generates relevant answer. There are four runs in our CLIR, two runs follow the dictionary and MI information based translation approach (KAIST9xlqm, KAIST9xlqt), another one using the mixture result of two commercial Machine Translation systems (KAIST9xImt), and the final one is monolingual run (KAIST9xlch). We translated only query and description fields in all four runs. In batching filtering task, we submitted results for OHSU topics and MSH-SMP topics. For OHSU topics, we have been exploring a filtering technique which combines query zone, support vector machine, and Rocchio's algorithm. For MSH-SMP topics, we use support vector machine simply.
	

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

#### Experiments on the TREC-9 Filtering Track

_Keiichiro Hoashi, Kazunori Matsumoto, Naomi Inoue, Kazuo Hashimoto, Takashi Hasegawa, Katsuhiko Shirai_

- :fontawesome-solid-user-group: **Participant:** [KDD](./filtering/participants.md#kdd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/kddtrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/kddtrec9.pdf)
- :material-file-search: **Runs:** [kddaf904](./filtering/runs.md#kddaf904) | [kddaf905](./filtering/runs.md#kddaf905) | [kddaf906](./filtering/runs.md#kddaf906) | [kddaf903](./filtering/runs.md#kddaf903)

??? abstract "Abstract"
	
	KDD R&D Laboratories has been participating in previous TREC conferences with the cooperation of students from Waseda University. This year, KDD R&D Laboratories and Waseda University are officially participating as a joint research team. We have focused our experiments for TREC-9 on the adaptive filtering experiments of the Filtering Track. Our goal was to evaluate the filtering method using a non-relevant information profile. We have also made experiments of a new feedback method to increase the accuracy of pseudo feedback. In this paper, we will describe our filtering methods, and present results of our evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HoashiMIHHS00.bib) "
	```
	@inproceedings{DBLP:conf/trec/HoashiMIHHS00,
		author = {Keiichiro Hoashi and Kazunori Matsumoto and Naomi Inoue and Kazuo Hashimoto and Takashi Hasegawa and Katsuhiko Shirai},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments on the {TREC-9} Filtering Track},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/kddtrec9.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HoashiMIHHS00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filters and Answers: The University of Iowa TREC-9 Results

_Elena Catona, David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [iowa](./filtering/participants.md#iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/iowa.pdf](http://trec.nist.gov/pubs/trec9/papers/iowa.pdf)
- :material-file-search: **Runs:** [IOWAF001](./filtering/runs.md#iowaf001) | [IOWAF002](./filtering/runs.md#iowaf002) | [IOWAF003](./filtering/runs.md#iowaf003)

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

#### The System RELIEFS: A New Approach for Information Filtering

_Christophe Brouard, Jian-Yun Nie_

- :fontawesome-solid-user-group: **Participant:** [UMontreal](./filtering/participants.md#umontreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/brouard.pdf](http://trec.nist.gov/pubs/trec9/papers/brouard.pdf)
- :material-file-search: **Runs:** [reliefs2](./filtering/runs.md#reliefs2) | [reliefs1](./filtering/runs.md#reliefs1)

??? abstract "Abstract"
	
	In this year's filtering track, we implemented a system called RELIEFS that tries to learn about the prediction capability of words or conjunctions of words for the relevance of documents. The novelty of the system resides in two main points. First, the features used in the prediction involve both : the implication D->Q (from document to query), and the reverse implication Q->D. This is different from usual approaches where only the first of the implication is used. Therefore, the relevance estimation of a document combines the probability that a document containing a term is relevant, and the reverse probability - the probability that a term appears in relevant documents. The second novelty is that, in addition to the use of words as prediction elements, we also consider word combinations (conjunctions). However, not all combinations are significant. Therefore, an incremental algorithm is developped to select only the meaningful conjunctions. To limit the number of conjunctions, we do not use a cut on conjunction length. Rather, we eliminate the conjunctions A&B that bear the same information as A or as B. Our first results prove the feasibility of the approach. Other experiments are ongoing in order to fully evaluate this approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrouardN00.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrouardN00,
		author = {Christophe Brouard and Jian{-}Yun Nie},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The System {RELIEFS:} {A} New Approach for Information Filtering},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/brouard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BrouardN00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Logical Analysis of Data in the TREC-9 Filtering Track

_Endre Boros, Paul B. Kantor, David J. Neu_

- :fontawesome-solid-user-group: **Participant:** [rutgers-kantor](./filtering/participants.md#rutgers-kantor)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/rutgers.pdf](http://trec.nist.gov/pubs/trec9/papers/rutgers.pdf)
- :material-file-search: **Runs:** [antadapt001](./filtering/runs.md#antadapt001) | [antadapt002](./filtering/runs.md#antadapt002) | [antrpnohsu00](./filtering/runs.md#antrpnohsu00) | [antrpohsu00](./filtering/runs.md#antrpohsu00) | [antrpnms00](./filtering/runs.md#antrpnms00) | [antrpms00](./filtering/runs.md#antrpms00)

??? abstract "Abstract"
	
	In the TREC-9 adaptive filtering and routing sub-tasks of the filtering track we continued to explore utilizing the Logical Analysis of Data (LAD) machine learning methodology to develop Boolean expressions that can be utilized as 'rules' for characterizing relevant and irrelevant documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BorosKN00.bib) "
	```
	@inproceedings{DBLP:conf/trec/BorosKN00,
		author = {Endre Boros and Paul B. Kantor and David J. Neu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Logical Analysis of Data in the {TREC-9} Filtering Track},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/rutgers.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BorosKN00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at trec9: Web and Filtering tasks

_M. Abchiche, Mohand Boughanem, Taoufiq Dkaki, Josiane Mothe, Chantal Soulé-Dupuy, Mohamed Tmar_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./filtering/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/irit_trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/irit_trec9.pdf)
- :material-file-search: **Runs:** [Mer9r2](./filtering/runs.md#mer9r2) | [mer9b1](./filtering/runs.md#mer9b1) | [mer9b2](./filtering/runs.md#mer9b2) | [mer9r1](./filtering/runs.md#mer9r1)

??? abstract "Abstract"
	
	The tests performed for TREC9 focus on the Web and Filtering (batch and routing) tracks. The submitted runs are based on the Mercure system. For one of the filtering routing runs, we combine Mercure with mining text functionalities from our system Tétralogie. We also performed some experiments taking hyperlinks into account to evaluate their influence on the retrieval effectiveness, but no runs were sent. Web: We submit four runs in this track. Two elements were tested: a modified Mercure term weighting scheme and the notion of the user preference on the retrieved document were tested. Filtering (batch and routing): our main investigation this year concerns the notion of non-relevant profile in a filtering system. The filtering consists on, first filtering the documents using a relevant profile learned from relevant documents, second re-filtering the selected documents using non-relevant profile learned from non-relevant documents so that non-relevant documents accepted by the relevant profile are rejected. This notion of non-relevant profile was introduced by Hoashi [6] in an adaptive system whereas we use this technique for a batch system.
	

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

#### kNN at TREC-9

_Tom Ault, Yiming Yang_

- :fontawesome-solid-user-group: **Participant:** [cmu](./filtering/participants.md#cmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/cmucat.pdf](http://trec.nist.gov/pubs/trec9/papers/cmucat.pdf)
- :material-file-search: **Runs:** [CMUCAT2](./filtering/runs.md#cmucat2) | [CMUCAT3](./filtering/runs.md#cmucat3) | [CMUCAT4](./filtering/runs.md#cmucat4) | [CMUCAT1](./filtering/runs.md#cmucat1) | [CMUCAT5](./filtering/runs.md#cmucat5) | [CMUCAT6](./filtering/runs.md#cmucat6)

??? abstract "Abstract"
	
	We applied a multi-class k-nearest-neighbor based text classification algorithm to the adaptive and batch filtering problems in the TREC-9 filtering track. While our systems performed well in the batch filtering tasks, they did not perform as well in the adaptive filtering tasks, in part because we did not have an adequate mechanism for taking advantage of the relevance feedback information provided by the filtering tasks. Since TREC-9, we have made considerable improvements in our batch filtering results and discovered some serious problems with both the T9P and T9U metrics. In this paper, we discuss these issues and their impact on our filtering results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AultY00.bib) "
	```
	@inproceedings{DBLP:conf/trec/AultY00,
		author = {Tom Ault and Yiming Yang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {kNN at {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/cmucat.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AultY00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Incrementality, Half-life, and Threshold Optimization for Adaptive  Document Filtering

_Avi Arampatzis, Jean Beney, Cornelis H. A. Koster, Theo P. van der Weide_

- :fontawesome-solid-user-group: **Participant:** [nijmegen](./filtering/participants.md#nijmegen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/trec9-kun-final.pdf](http://trec.nist.gov/pubs/trec9/papers/trec9-kun-final.pdf)
- :material-file-search: **Runs:** [KUNr1](./filtering/runs.md#kunr1) | [KUNr2](./filtering/runs.md#kunr2) | [KUNb](./filtering/runs.md#kunb) | [KUNa1T9U](./filtering/runs.md#kuna1t9u) | [KUNa1T9P](./filtering/runs.md#kuna1t9p) | [KUNa2T9U](./filtering/runs.md#kuna2t9u) | [KUNa2T9P](./filtering/runs.md#kuna2t9p) | [KUNbaT9U](./filtering/runs.md#kunbat9u)

??? abstract "Abstract"
	
	This paper describes the participation by researchers from KUN (the Computing Science Department of the Katholieke Universiteit Nijmegen, The Netherlands) in the TREC-9 Filtering Track. As first-time TREC par-ticipants, our group participated in all three subtasks - adaptive, batch, and routing - while concentrating mainly on adaptive tasks. We have made use of two different systems: FILTERIT, for the adaptive and batch-adaptive' tasks: a pure adaptive filtering system developed in the context of our TREC-9 participation. It is based on the Rocchio algorithm. LOS, for the routing and batch filtering tasks: a multi-classification system based on the Winnow al-gorithm. In adaptive filtering, our contribution has been three-fold. Firstly, we have investigated the value of retrieved documents as training examples in relation to their time of retrieval. For this purpose we have introduced the notion of the half-life of a training document. Secondly, we have introduced a novel statistical threshold selection technique for optimizing linear utility functions. The method can be also applied for optimizing other effectiveness measures as well, however, the resulting equation may have to be solved numerically. Thirdly and most importantly for adaptive long-term tasks, we have developed a system that allows incremental adaptivity. We have tried to minimize the computational and memory requirements of our system without sacrificing its accuracy. In the batch and routing tasks, we have experimented with the use of the Winnow algorithm, including a couple of small improvements. From the two topic-sets given, we have experimented only with the 63 OHSUMED queries. We did not submit any runs on the 4904 MeSH topics; these were simply too many to be processed by our present systems in a reasonable time and space. All experiments were done using a keyword-based representation of documents and queries, with traditional stemming and stoplisting, although our long-term intention is to use phrase representations 2, and apply more sophisticated term selection methods [3]. Table 1 summarizes our official TREC-9 runs. Next, we will briefly describe the pre-processing applied to the data. The FILTERIT and LCS systems are described in Sections 3 and 4, respectively. In Section 5 we give an overall view to how our systems performed in relation to other participants.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ArampatzisBKW00.bib) "
	```
	@inproceedings{DBLP:conf/trec/ArampatzisBKW00,
		author = {Avi Arampatzis and Jean Beney and Cornelis H. A. Koster and Theo P. van der Weide},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Incrementality, Half-life, and Threshold Optimization for Adaptive Document Filtering},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/trec9-kun-final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ArampatzisBKW00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Query 

#### The TREC-9 Query Track

_Chris Buckley_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/query_track.pdf](http://trec.nist.gov/pubs/trec9/papers/query_track.pdf)
??? abstract "Abstract"
	
	The Query Track in TREC-9 is unlike the other tracks in TREC. The other tracks attempt to compare systems to determine the best approaches to solve the particular track problem. This comparison is normally done over a given set of topics, with a single query per topic. The Query Track, on the other hand, compares multiple queries on a single topic to determine which queries perform best with which systems. There is no emphasis on system-system comparisons: none of the participating systems were even the most advanced system from that particular participating group. Instead, the goal is to try and understand how the statement (query) of the user's information need (topic) affects retrieval. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Buckley00.bib) "
	```
	@inproceedings{DBLP:conf/trec/Buckley00,
		author = {Chris Buckley},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-9} Query Track},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/query\_track.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Buckley00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Hummingbird's Fulcrum SearchServer at TREC-9

_Stephen Tomlinson, Tom Blackwell_

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./query/participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/humtrec9.pdf](http://trec.nist.gov/pubs/trec9/papers/humtrec9.pdf)
- :material-file-search: **Runs:** [humBUoM1b](./query/runs.md#humbuom1b) | [humBUoM1a](./query/runs.md#humbuom1a) | [humBAPL2a](./query/runs.md#humbapl2a) | [humBSab3a](./query/runs.md#humbsab3a) | [humBSab2a](./query/runs.md#humbsab2a) | [humBSab1a](./query/runs.md#humbsab1a) | [humBacs1a](./query/runs.md#humbacs1a) | [humBINQ2c](./query/runs.md#humbinq2c) | [humBINQ2j](./query/runs.md#humbinq2j) | [humBINQ2e](./query/runs.md#humbinq2e) | [humBINQ2b](./query/runs.md#humbinq2b) | [humBINQ1i](./query/runs.md#humbinq1i) | [humBINQ1j](./query/runs.md#humbinq1j) | [humBINQ2a](./query/runs.md#humbinq2a) | [humBSab1d](./query/runs.md#humbsab1d) | [humBINQ1g](./query/runs.md#humbinq1g) | [humBINQ1h](./query/runs.md#humbinq1h) | [humBSab1c](./query/runs.md#humbsab1c) | [humBINQ1f](./query/runs.md#humbinq1f) | [humBUoM2](./query/runs.md#humbuom2) | [humBINQ3c](./query/runs.md#humbinq3c) | [humBAPL1a](./query/runs.md#humbapl1a) | [humBINQ1e](./query/runs.md#humbinq1e) | [humBSab1b](./query/runs.md#humbsab1b) | [humBINQ3a](./query/runs.md#humbinq3a) | [humBINQ1d](./query/runs.md#humbinq1d) | [humBpir1a](./query/runs.md#humbpir1a) | [humBINQ3b](./query/runs.md#humbinq3b) | [humBINQ2d](./query/runs.md#humbinq2d) | [humBINQ2f](./query/runs.md#humbinq2f) | [humBINQ1a](./query/runs.md#humbinq1a) | [humBINQ1b](./query/runs.md#humbinq1b) | [humBINQ3d](./query/runs.md#humbinq3d) | [humBINQ2g](./query/runs.md#humbinq2g) | [humBINQ1c](./query/runs.md#humbinq1c) | [humBINQ3j](./query/runs.md#humbinq3j) | [humBINQ2h](./query/runs.md#humbinq2h) | [humBINQ3h](./query/runs.md#humbinq3h) | [humBINQ3i](./query/runs.md#humbinq3i) | [humBINQ2i](./query/runs.md#humbinq2i) | [humBINQ3g](./query/runs.md#humbinq3g) | [humBINQ3f](./query/runs.md#humbinq3f) | [humBINQ3e](./query/runs.md#humbinq3e) | [humKUoM2](./query/runs.md#humkuom2) | [humKUoM1b](./query/runs.md#humkuom1b) | [humKINQ2c](./query/runs.md#humkinq2c) | [hum4Sab3a](./query/runs.md#hum4sab3a) | [hum4UoM1a](./query/runs.md#hum4uom1a) | [humKUoM1a](./query/runs.md#humkuom1a) | [humKacs1a](./query/runs.md#humkacs1a) | [hum4INQ2d](./query/runs.md#hum4inq2d) | [hum4Sab1d](./query/runs.md#hum4sab1d) | [humKINQ3f](./query/runs.md#humkinq3f) | [hum4Sab2a](./query/runs.md#hum4sab2a) | [hum4Sab1c](./query/runs.md#hum4sab1c) | [hum4Sab1b](./query/runs.md#hum4sab1b) | [hum4pir1a](./query/runs.md#hum4pir1a) | [hum4Sab1a](./query/runs.md#hum4sab1a) | [hum4INQ3j](./query/runs.md#hum4inq3j) | [hum4INQ3i](./query/runs.md#hum4inq3i) | [hum4INQ3h](./query/runs.md#hum4inq3h) | [hum4INQ3g](./query/runs.md#hum4inq3g) | [hum4INQ3f](./query/runs.md#hum4inq3f) | [hum4INQ3e](./query/runs.md#hum4inq3e) | [hum4INQ3d](./query/runs.md#hum4inq3d) | [hum4acs1a](./query/runs.md#hum4acs1a) | [hum4INQ3b](./query/runs.md#hum4inq3b) | [hum4INQ3c](./query/runs.md#hum4inq3c) | [hum4INQ2h](./query/runs.md#hum4inq2h) | [hum4INQ3a](./query/runs.md#hum4inq3a) | [hum4INQ2j](./query/runs.md#hum4inq2j) | [hum4INQ2i](./query/runs.md#hum4inq2i) | [hum4INQ2g](./query/runs.md#hum4inq2g) | [hum4INQ2f](./query/runs.md#hum4inq2f) | [hum4INQ2c](./query/runs.md#hum4inq2c) | [hum4INQ2e](./query/runs.md#hum4inq2e) | [hum4INQ2a](./query/runs.md#hum4inq2a) | [hum4INQ1j](./query/runs.md#hum4inq1j) | [hum4INQ2b](./query/runs.md#hum4inq2b) | [hum4INQ1h](./query/runs.md#hum4inq1h) | [hum4INQ1i](./query/runs.md#hum4inq1i) | [hum4INQ1f](./query/runs.md#hum4inq1f) | [hum4INQ1g](./query/runs.md#hum4inq1g) | [hum4INQ1b](./query/runs.md#hum4inq1b) | [hum4INQ1d](./query/runs.md#hum4inq1d) | [hum4INQ1e](./query/runs.md#hum4inq1e) | [humKINQ2d](./query/runs.md#humkinq2d) | [hum4INQ1c](./query/runs.md#hum4inq1c) | [hum4INQ1a](./query/runs.md#hum4inq1a) | [humKINQ2e](./query/runs.md#humkinq2e) | [humKSab2a](./query/runs.md#humksab2a) | [hum4APL2a](./query/runs.md#hum4apl2a) | [hum4APL1a](./query/runs.md#hum4apl1a) | [humKAPL1a](./query/runs.md#humkapl1a) | [hum4UoM2](./query/runs.md#hum4uom2) | [humKAPL2a](./query/runs.md#humkapl2a) | [humKINQ1a](./query/runs.md#humkinq1a) | [humKINQ1b](./query/runs.md#humkinq1b) | [humKINQ1c](./query/runs.md#humkinq1c) | [humKINQ1e](./query/runs.md#humkinq1e) | [humKINQ1f](./query/runs.md#humkinq1f) | [humKINQ1g](./query/runs.md#humkinq1g) | [humKINQ1d](./query/runs.md#humkinq1d) | [humKINQ1h](./query/runs.md#humkinq1h) | [humKINQ1i](./query/runs.md#humkinq1i) | [humKINQ1j](./query/runs.md#humkinq1j) | [humKINQ2a](./query/runs.md#humkinq2a) | [humKINQ2b](./query/runs.md#humkinq2b) | [hum4UoM1b](./query/runs.md#hum4uom1b) | [humKSab1d](./query/runs.md#humksab1d) | [humKINQ2f](./query/runs.md#humkinq2f) | [humKSab3a](./query/runs.md#humksab3a) | [humKINQ2h](./query/runs.md#humkinq2h) | [humKINQ2g](./query/runs.md#humkinq2g) | [humKINQ2i](./query/runs.md#humkinq2i) | [humKINQ3a](./query/runs.md#humkinq3a) | [humKINQ2j](./query/runs.md#humkinq2j) | [humKINQ3b](./query/runs.md#humkinq3b) | [humKINQ3d](./query/runs.md#humkinq3d) | [humKINQ3e](./query/runs.md#humkinq3e) | [humKINQ3c](./query/runs.md#humkinq3c) | [humKINQ3h](./query/runs.md#humkinq3h) | [humKINQ3j](./query/runs.md#humkinq3j) | [humKINQ3g](./query/runs.md#humkinq3g) | [humKSab1a](./query/runs.md#humksab1a) | [humKpir1a](./query/runs.md#humkpir1a) | [humKINQ3i](./query/runs.md#humkinq3i) | [humKSab1c](./query/runs.md#humksab1c) | [humKSab1b](./query/runs.md#humksab1b) | [humDUoM2](./query/runs.md#humduom2) | [humDUoM1a](./query/runs.md#humduom1a) | [humDUoM1b](./query/runs.md#humduom1b) | [humDINQ1i](./query/runs.md#humdinq1i) | [humDSab3a](./query/runs.md#humdsab3a) | [humDSab2a](./query/runs.md#humdsab2a) | [humDINQ3d](./query/runs.md#humdinq3d) | [humDINQ3a](./query/runs.md#humdinq3a) | [humVSab1d](./query/runs.md#humvsab1d) | [humVINQ2b](./query/runs.md#humvinq2b) | [humDINQ3f](./query/runs.md#humdinq3f) | [humVSab2a](./query/runs.md#humvsab2a) | [humVINQ2a](./query/runs.md#humvinq2a) | [humVSab3a](./query/runs.md#humvsab3a) | [humVINQ1j](./query/runs.md#humvinq1j) | [humDSab1d](./query/runs.md#humdsab1d) | [humVINQ1i](./query/runs.md#humvinq1i) | [humVSab1c](./query/runs.md#humvsab1c) | [humVINQ1g](./query/runs.md#humvinq1g) | [humVUoM1b](./query/runs.md#humvuom1b) | [humVacs1a](./query/runs.md#humvacs1a) | [humVINQ1e](./query/runs.md#humvinq1e) | [humVINQ1a](./query/runs.md#humvinq1a) | [humVUoM2](./query/runs.md#humvuom2) | [humVINQ1c](./query/runs.md#humvinq1c) | [humDINQ3c](./query/runs.md#humdinq3c) | [humVAPL1a](./query/runs.md#humvapl1a) | [humVAPL2a](./query/runs.md#humvapl2a) | [humVINQ1b](./query/runs.md#humvinq1b) | [humDSab1c](./query/runs.md#humdsab1c) | [humDINQ1b](./query/runs.md#humdinq1b) | [humVINQ2h](./query/runs.md#humvinq2h) | [humDAPL1a](./query/runs.md#humdapl1a) | [humDINQ2c](./query/runs.md#humdinq2c) | [humVINQ1h](./query/runs.md#humvinq1h) | [humDSab1b](./query/runs.md#humdsab1b) | [humDINQ2i](./query/runs.md#humdinq2i) | [humDSab1a](./query/runs.md#humdsab1a) | [humDINQ2f](./query/runs.md#humdinq2f) | [humVINQ1d](./query/runs.md#humvinq1d) | [humDINQ1f](./query/runs.md#humdinq1f) | [humVINQ1f](./query/runs.md#humvinq1f) | [humDINQ3j](./query/runs.md#humdinq3j) | [humDINQ3i](./query/runs.md#humdinq3i) | [humDINQ3g](./query/runs.md#humdinq3g) | [humDacs1a](./query/runs.md#humdacs1a) | [humDINQ3e](./query/runs.md#humdinq3e) | [humVINQ3j](./query/runs.md#humvinq3j) | [humDINQ1c](./query/runs.md#humdinq1c) | [humDINQ3b](./query/runs.md#humdinq3b) | [humDINQ1e](./query/runs.md#humdinq1e) | [humDINQ2h](./query/runs.md#humdinq2h) | [humDINQ2j](./query/runs.md#humdinq2j) | [humDINQ3h](./query/runs.md#humdinq3h) | [humDINQ2g](./query/runs.md#humdinq2g) | [humDINQ2e](./query/runs.md#humdinq2e) | [humDINQ2d](./query/runs.md#humdinq2d) | [humDpir1a](./query/runs.md#humdpir1a) | [humVINQ3i](./query/runs.md#humvinq3i) | [humDINQ1h](./query/runs.md#humdinq1h) | [humDINQ1a](./query/runs.md#humdinq1a) | [humVSab1b](./query/runs.md#humvsab1b) | [humVINQ2j](./query/runs.md#humvinq2j) | [humVSab1a](./query/runs.md#humvsab1a) | [humVUoM1a](./query/runs.md#humvuom1a) | [humVINQ3f](./query/runs.md#humvinq3f) | [humDAPL2a](./query/runs.md#humdapl2a) | [humDINQ1d](./query/runs.md#humdinq1d) | [humVINQ3b](./query/runs.md#humvinq3b) | [humVINQ3e](./query/runs.md#humvinq3e) | [humDINQ1g](./query/runs.md#humdinq1g) | [humVpir1a](./query/runs.md#humvpir1a) | [humVINQ3d](./query/runs.md#humvinq3d) | [humVINQ3g](./query/runs.md#humvinq3g) | [humVINQ3h](./query/runs.md#humvinq3h) | [humVINQ2e](./query/runs.md#humvinq2e) | [humVINQ2f](./query/runs.md#humvinq2f) | [humDINQ2a](./query/runs.md#humdinq2a) | [humDINQ1j](./query/runs.md#humdinq1j) | [humDINQ2b](./query/runs.md#humdinq2b) | [humVINQ3c](./query/runs.md#humvinq3c) | [humVINQ2g](./query/runs.md#humvinq2g) | [humVINQ2d](./query/runs.md#humvinq2d) | [humVINQ3a](./query/runs.md#humvinq3a) | [humVINQ2c](./query/runs.md#humvinq2c) | [humVINQ2i](./query/runs.md#humvinq2i) | [humIINQ2b](./query/runs.md#humiinq2b) | [humIUoM2](./query/runs.md#humiuom2) | [humIINQ1h](./query/runs.md#humiinq1h) | [humIINQ1j](./query/runs.md#humiinq1j) | [humIUoM1b](./query/runs.md#humiuom1b) | [humIINQ2a](./query/runs.md#humiinq2a) | [humIacs1a](./query/runs.md#humiacs1a) | [humIINQ3c](./query/runs.md#humiinq3c) | [humIINQ3d](./query/runs.md#humiinq3d) | [humIINQ3e](./query/runs.md#humiinq3e) | [humIINQ3f](./query/runs.md#humiinq3f) | [humIINQ2h](./query/runs.md#humiinq2h) | [humIAPL1a](./query/runs.md#humiapl1a) | [humIUoM1a](./query/runs.md#humiuom1a) | [humIINQ3h](./query/runs.md#humiinq3h) | [humIAPL2a](./query/runs.md#humiapl2a) | [humIINQ1b](./query/runs.md#humiinq1b) | [humIINQ1a](./query/runs.md#humiinq1a) | [humISab2a](./query/runs.md#humisab2a) | [humIINQ1c](./query/runs.md#humiinq1c) | [humIINQ2c](./query/runs.md#humiinq2c) | [humIINQ3b](./query/runs.md#humiinq3b) | [humIINQ1e](./query/runs.md#humiinq1e) | [humIINQ1d](./query/runs.md#humiinq1d) | [humIINQ1g](./query/runs.md#humiinq1g) | [humIINQ1f](./query/runs.md#humiinq1f) | [humIINQ3a](./query/runs.md#humiinq3a) | [humIINQ2j](./query/runs.md#humiinq2j) | [humISab3a](./query/runs.md#humisab3a) | [humIINQ1i](./query/runs.md#humiinq1i) | [humIINQ3g](./query/runs.md#humiinq3g) | [humISab1c](./query/runs.md#humisab1c) | [humIINQ2e](./query/runs.md#humiinq2e) | [humIpir1a](./query/runs.md#humipir1a) | [humIINQ2d](./query/runs.md#humiinq2d) | [humISab1d](./query/runs.md#humisab1d) | [humIINQ3i](./query/runs.md#humiinq3i) | [humIINQ2i](./query/runs.md#humiinq2i) | [humIINQ2g](./query/runs.md#humiinq2g) | [humISab1a](./query/runs.md#humisab1a) | [humISab1b](./query/runs.md#humisab1b) | [humIINQ3j](./query/runs.md#humiinq3j) | [humIINQ2f](./query/runs.md#humiinq2f) | [humAUoM2](./query/runs.md#humauom2) | [humAacs1a](./query/runs.md#humaacs1a) | [humAUoM1a](./query/runs.md#humauom1a) | [humAUoM1b](./query/runs.md#humauom1b) | [humAINQ2b](./query/runs.md#humainq2b) | [humAINQ1j](./query/runs.md#humainq1j) | [humASab3a](./query/runs.md#humasab3a) | [humAINQ2i](./query/runs.md#humainq2i) | [humAAPL1a](./query/runs.md#humaapl1a) | [humAAPL2a](./query/runs.md#humaapl2a) | [humASab1d](./query/runs.md#humasab1d) | [humASab2a](./query/runs.md#humasab2a) | [humAINQ2h](./query/runs.md#humainq2h) | [humAINQ2f](./query/runs.md#humainq2f) | [humASab1c](./query/runs.md#humasab1c) | [humASab1b](./query/runs.md#humasab1b) | [humAINQ3j](./query/runs.md#humainq3j) | [humApir1a](./query/runs.md#humapir1a) | [humASab1a](./query/runs.md#humasab1a) | [humAINQ3i](./query/runs.md#humainq3i) | [humAINQ3g](./query/runs.md#humainq3g) | [humAINQ3h](./query/runs.md#humainq3h) | [humAINQ3f](./query/runs.md#humainq3f) | [humAINQ2e](./query/runs.md#humainq2e) | [humAINQ3e](./query/runs.md#humainq3e) | [humAINQ3b](./query/runs.md#humainq3b) | [humAINQ3d](./query/runs.md#humainq3d) | [humAINQ3c](./query/runs.md#humainq3c) | [humAINQ3a](./query/runs.md#humainq3a) | [humAINQ2j](./query/runs.md#humainq2j) | [humAINQ2a](./query/runs.md#humainq2a) | [humAINQ1b](./query/runs.md#humainq1b) | [humAINQ2g](./query/runs.md#humainq2g) | [humAINQ1a](./query/runs.md#humainq1a) | [humAINQ1c](./query/runs.md#humainq1c) | [humAINQ2c](./query/runs.md#humainq2c) | [humAINQ2d](./query/runs.md#humainq2d) | [humAINQ1h](./query/runs.md#humainq1h) | [humAINQ1d](./query/runs.md#humainq1d) | [humAINQ1g](./query/runs.md#humainq1g) | [humAINQ1e](./query/runs.md#humainq1e) | [humAINQ1f](./query/runs.md#humainq1f) | [humAINQ1i](./query/runs.md#humainq1i)

??? abstract "Abstract"
	
	Hummingbird submitted ranked result sets for the Main Web Task (10GB of web data) and Large Web Task (100GB) of the TREC-9 Web Track, and for Stage 2 of the TREC-9 Query Track (43 variations of 50 queries). SearchServer's Intuitive Searching produced the highest Precision@5 score (averaged over 50 web queries) of all Title-only runs submitted to the Main Web Task. SearchServer's approximate text searching and linguistic expansion each increased average precision for web queries by 5%. Enabling SearchServer's document length normalization increased average precision for web queries by 10-30% and for long queries by 100%. Squaring the importance of the inverse document frequency (relevance method 'V2:4') increased average precision in the query track by 5%. Blind query expansion decreased average precision of highly relevants for web queries by almost 15%; the same method was neutral when counting all relevants the same.
	

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

#### Melbourne TREC-9 Experiments

_Daryl J. D'Souza, Michael Fuller, James A. Thom, Phil Vines, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./query/participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/mds.pdf](http://trec.nist.gov/pubs/trec9/papers/mds.pdf)
- :material-file-search: **Runs:** [ok9uAPL2a](./query/runs.md#ok9uapl2a) | [ok9uINQ1a](./query/runs.md#ok9uinq1a) | [ok9uINQ1b](./query/runs.md#ok9uinq1b) | [ok9uINQ1c](./query/runs.md#ok9uinq1c) | [ok9uINQ1d](./query/runs.md#ok9uinq1d) | [ok9uINQ1h](./query/runs.md#ok9uinq1h) | [ok9uINQ1i](./query/runs.md#ok9uinq1i) | [ok9uINQ1j](./query/runs.md#ok9uinq1j) | [ok9uINQ2a](./query/runs.md#ok9uinq2a) | [ok9uINQ2b](./query/runs.md#ok9uinq2b) | [ok9uINQ2c](./query/runs.md#ok9uinq2c) | [ok9uINQ2d](./query/runs.md#ok9uinq2d) | [ok9uINQ2e](./query/runs.md#ok9uinq2e) | [ok9uINQ2f](./query/runs.md#ok9uinq2f) | [ok9uINQ2g](./query/runs.md#ok9uinq2g) | [ok9uINQ2h](./query/runs.md#ok9uinq2h) | [ok9uINQ2i](./query/runs.md#ok9uinq2i) | [ok9uINQ2j](./query/runs.md#ok9uinq2j) | [ok9uINQ3a](./query/runs.md#ok9uinq3a) | [ok9uINQ3b](./query/runs.md#ok9uinq3b) | [ok9uINQ3c](./query/runs.md#ok9uinq3c) | [ok9uINQ3d](./query/runs.md#ok9uinq3d) | [ok9uINQ3e](./query/runs.md#ok9uinq3e) | [ok9uINQ3f](./query/runs.md#ok9uinq3f) | [ok9uINQ3g](./query/runs.md#ok9uinq3g) | [ok9uINQ3i](./query/runs.md#ok9uinq3i) | [ok9uINQ3j](./query/runs.md#ok9uinq3j) | [ok9uSab2a](./query/runs.md#ok9usab2a) | [ok9uSab3a](./query/runs.md#ok9usab3a) | [ok9upir1a](./query/runs.md#ok9upir1a) | [ok9uacs1a](./query/runs.md#ok9uacs1a) | [ok9uUoM2](./query/runs.md#ok9uuom2) | [ok9uUoM1b](./query/runs.md#ok9uuom1b) | [ok9uUoM1a](./query/runs.md#ok9uuom1a) | [ok9uSab1d](./query/runs.md#ok9usab1d) | [ok9uSab1c](./query/runs.md#ok9usab1c) | [ok9uSab1b](./query/runs.md#ok9usab1b) | [ok9uSab1a](./query/runs.md#ok9usab1a) | [ok9uINQ3h](./query/runs.md#ok9uinq3h) | [ok9uINQ1g](./query/runs.md#ok9uinq1g) | [ok9uINQ1f](./query/runs.md#ok9uinq1f) | [ok9uINQ1e](./query/runs.md#ok9uinq1e) | [ok9uAPL1a](./query/runs.md#ok9uapl1a)

??? abstract "Abstract"
	
	We report results for experiments conducted in Melbourne-at CSIRO, RMIT, and The University of Melbourne for TREC-9. We present results for the interactive track, cross-lingual track, main web track, and the query track.
	

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

#### SabIR Research at TREC-9

_Chris Buckley, Janet A. Walz_

- :fontawesome-solid-user-group: **Participant:** [sabir](./query/participants.md#sabir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/sabir.pdf](http://trec.nist.gov/pubs/trec9/papers/sabir.pdf)
- :material-file-search: **Runs:** [SabaAPL1a](./query/runs.md#sabaapl1a) | [SabaAPL2a](./query/runs.md#sabaapl2a) | [SabaINQ1d](./query/runs.md#sabainq1d) | [SabaINQ1a](./query/runs.md#sabainq1a) | [SabaINQ1c](./query/runs.md#sabainq1c) | [SabaINQ1b](./query/runs.md#sabainq1b) | [SabaINQ1e](./query/runs.md#sabainq1e) | [SabaINQ1h](./query/runs.md#sabainq1h) | [SabaINQ1g](./query/runs.md#sabainq1g) | [SabaINQ1f](./query/runs.md#sabainq1f) | [SabaINQ1j](./query/runs.md#sabainq1j) | [SabaINQ1i](./query/runs.md#sabainq1i) | [SabaINQ2a](./query/runs.md#sabainq2a) | [SabaINQ2c](./query/runs.md#sabainq2c) | [SabaINQ2b](./query/runs.md#sabainq2b) | [SabaINQ2e](./query/runs.md#sabainq2e) | [SabaINQ2g](./query/runs.md#sabainq2g) | [SabaINQ2d](./query/runs.md#sabainq2d) | [SabaINQ2f](./query/runs.md#sabainq2f) | [SabaINQ2j](./query/runs.md#sabainq2j) | [SabaINQ2i](./query/runs.md#sabainq2i) | [SabaINQ3d](./query/runs.md#sabainq3d) | [SabaINQ3b](./query/runs.md#sabainq3b) | [SabaINQ3c](./query/runs.md#sabainq3c) | [SabaINQ3a](./query/runs.md#sabainq3a) | [SabaINQ3h](./query/runs.md#sabainq3h) | [SabaINQ3f](./query/runs.md#sabainq3f) | [SabaINQ3e](./query/runs.md#sabainq3e) | [SabaINQ3i](./query/runs.md#sabainq3i) | [SabaINQ3g](./query/runs.md#sabainq3g) | [SabaSab1b](./query/runs.md#sabasab1b) | [SabaINQ3j](./query/runs.md#sabainq3j) | [SabaSab1c](./query/runs.md#sabasab1c) | [SabaSab1a](./query/runs.md#sabasab1a) | [Sabaacs1a](./query/runs.md#sabaacs1a) | [SabaUoM2](./query/runs.md#sabauom2) | [Sabapir1a](./query/runs.md#sabapir1a) | [SabaUoM1a](./query/runs.md#sabauom1a) | [SabeAPL2a](./query/runs.md#sabeapl2a) | [SabeINQ1a](./query/runs.md#sabeinq1a) | [SabeAPL1a](./query/runs.md#sabeapl1a) | [SabeINQ1d](./query/runs.md#sabeinq1d) | [SabeINQ1b](./query/runs.md#sabeinq1b) | [SabeINQ1c](./query/runs.md#sabeinq1c) | [SabeINQ1e](./query/runs.md#sabeinq1e) | [SabeINQ1f](./query/runs.md#sabeinq1f) | [SabeINQ1g](./query/runs.md#sabeinq1g) | [SabeINQ2c](./query/runs.md#sabeinq2c) | [SabeINQ1h](./query/runs.md#sabeinq1h) | [SabeINQ1i](./query/runs.md#sabeinq1i) | [SabeINQ2b](./query/runs.md#sabeinq2b) | [SabeINQ2d](./query/runs.md#sabeinq2d) | [SabeINQ2e](./query/runs.md#sabeinq2e) | [SabeINQ1j](./query/runs.md#sabeinq1j) | [SabeINQ2a](./query/runs.md#sabeinq2a) | [SabeINQ2f](./query/runs.md#sabeinq2f) | [SabeINQ2h](./query/runs.md#sabeinq2h) | [SabeINQ2i](./query/runs.md#sabeinq2i) | [SabeINQ2j](./query/runs.md#sabeinq2j) | [SabeINQ3d](./query/runs.md#sabeinq3d) | [SabeINQ2g](./query/runs.md#sabeinq2g) | [SabmINQ2c](./query/runs.md#sabminq2c) | [SabeSab1a](./query/runs.md#sabesab1a) | [SabmINQ1b](./query/runs.md#sabminq1b) | [SabeINQ3a](./query/runs.md#sabeinq3a) | [SabmSab2a](./query/runs.md#sabmsab2a) | [SabmINQ2g](./query/runs.md#sabminq2g) | [SabmAPL2a](./query/runs.md#sabmapl2a) | [SabmINQ2d](./query/runs.md#sabminq2d) | [SabmINQ2h](./query/runs.md#sabminq2h) | [SabaSab1d](./query/runs.md#sabasab1d) | [SabaSab2a](./query/runs.md#sabasab2a) | [SabmINQ2i](./query/runs.md#sabminq2i) | [SabmINQ2j](./query/runs.md#sabminq2j) | [SabmINQ1a](./query/runs.md#sabminq1a) | [SabaUoM1b](./query/runs.md#sabauom1b) | [SabeINQ3b](./query/runs.md#sabeinq3b) | [SabmSab3a](./query/runs.md#sabmsab3a) | [SabmUoM1a](./query/runs.md#sabmuom1a) | [SabaSab3a](./query/runs.md#sabasab3a) | [SabmINQ2b](./query/runs.md#sabminq2b) | [SabeINQ3j](./query/runs.md#sabeinq3j) | [SabeINQ3i](./query/runs.md#sabeinq3i) | [SabmINQ3b](./query/runs.md#sabminq3b) | [SabeINQ3e](./query/runs.md#sabeinq3e) | [SabmINQ2f](./query/runs.md#sabminq2f) | [SabmSab1d](./query/runs.md#sabmsab1d) | [SabeINQ3h](./query/runs.md#sabeinq3h) | [SabeINQ3c](./query/runs.md#sabeinq3c) | [SabmINQ3j](./query/runs.md#sabminq3j) | [SabeINQ3f](./query/runs.md#sabeinq3f) | [SabmINQ1e](./query/runs.md#sabminq1e) | [Sabmacs1a](./query/runs.md#sabmacs1a) | [Sabeacs1a](./query/runs.md#sabeacs1a) | [SabmAPL1a](./query/runs.md#sabmapl1a) | [SabmINQ1j](./query/runs.md#sabminq1j) | [SabmINQ1f](./query/runs.md#sabminq1f) | [SabmINQ1d](./query/runs.md#sabminq1d) | [SabeUoM1b](./query/runs.md#sabeuom1b) | [SabmINQ1h](./query/runs.md#sabminq1h) | [SabaINQ2h](./query/runs.md#sabainq2h) | [SabeSab2a](./query/runs.md#sabesab2a) | [SabeUoM1a](./query/runs.md#sabeuom1a) | [Sabmpir1a](./query/runs.md#sabmpir1a) | [SabmINQ3a](./query/runs.md#sabminq3a) | [SabmINQ3h](./query/runs.md#sabminq3h) | [SabmINQ2e](./query/runs.md#sabminq2e) | [SabmUoM1b](./query/runs.md#sabmuom1b) | [SabmINQ3d](./query/runs.md#sabminq3d) | [SabmINQ1i](./query/runs.md#sabminq1i) | [SabmINQ2a](./query/runs.md#sabminq2a) | [SabmSab1a](./query/runs.md#sabmsab1a) | [SabmSab1b](./query/runs.md#sabmsab1b) | [SabeSab1d](./query/runs.md#sabesab1d) | [SabeSab3a](./query/runs.md#sabesab3a) | [SabmSab1c](./query/runs.md#sabmsab1c) | [SabeUoM2](./query/runs.md#sabeuom2) | [SabeSab1c](./query/runs.md#sabesab1c) | [SabmINQ1g](./query/runs.md#sabminq1g) | [SabmINQ3c](./query/runs.md#sabminq3c) | [Sabepir1a](./query/runs.md#sabepir1a) | [SabmINQ3f](./query/runs.md#sabminq3f) | [SabmINQ3i](./query/runs.md#sabminq3i) | [SabeSab1b](./query/runs.md#sabesab1b) | [SabmINQ3g](./query/runs.md#sabminq3g) | [SabmINQ3e](./query/runs.md#sabminq3e) | [SabmUoM2](./query/runs.md#sabmuom2) | [SabeINQ3g](./query/runs.md#sabeinq3g) | [SabmINQ1c](./query/runs.md#sabminq1c)

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

#### INQUERY and TREC-9

_James Allan, Margaret E. Connell, W. Bruce Croft, Fangfang Feng, David Fisher, Xiaoyan Li_

- :fontawesome-solid-user-group: **Participant:** [umass](./query/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/umass-trec9.pdf](http://trec.nist.gov/pubs/trec9/papers/umass-trec9.pdf)
- :material-file-search: **Runs:** [IN7aAPL1a](./query/runs.md#in7aapl1a) | [IN7aAPL2a](./query/runs.md#in7aapl2a) | [IN7aINQ1a](./query/runs.md#in7ainq1a) | [IN7aINQ1c](./query/runs.md#in7ainq1c) | [IN7aINQ1d](./query/runs.md#in7ainq1d) | [IN7aINQ1e](./query/runs.md#in7ainq1e) | [IN7aINQ1b](./query/runs.md#in7ainq1b) | [IN7aINQ1f](./query/runs.md#in7ainq1f) | [IN7aINQ1g](./query/runs.md#in7ainq1g) | [IN7aINQ2b](./query/runs.md#in7ainq2b) | [IN7aINQ2a](./query/runs.md#in7ainq2a) | [IN7aINQ1i](./query/runs.md#in7ainq1i) | [IN7aINQ1j](./query/runs.md#in7ainq1j) | [IN7aINQ2e](./query/runs.md#in7ainq2e) | [IN7aINQ2h](./query/runs.md#in7ainq2h) | [IN7aINQ2g](./query/runs.md#in7ainq2g) | [IN7aINQ2i](./query/runs.md#in7ainq2i) | [IN7aINQ2f](./query/runs.md#in7ainq2f) | [IN7aINQ2c](./query/runs.md#in7ainq2c) | [IN7aINQ2j](./query/runs.md#in7ainq2j) | [IN7aINQ2d](./query/runs.md#in7ainq2d) | [IN7aINQ3b](./query/runs.md#in7ainq3b) | [IN7aINQ3a](./query/runs.md#in7ainq3a) | [IN7aINQ3c](./query/runs.md#in7ainq3c) | [IN7aINQ3f](./query/runs.md#in7ainq3f) | [IN7aINQ3h](./query/runs.md#in7ainq3h) | [IN7aINQ3i](./query/runs.md#in7ainq3i) | [IN7aINQ1h](./query/runs.md#in7ainq1h) | [IN7aINQ3g](./query/runs.md#in7ainq3g) | [IN7aINQ3e](./query/runs.md#in7ainq3e) | [IN7aINQ3d](./query/runs.md#in7ainq3d) | [IN7aSab1b](./query/runs.md#in7asab1b) | [IN7aSab1a](./query/runs.md#in7asab1a) | [IN7aINQ3j](./query/runs.md#in7ainq3j) | [IN7aSab1d](./query/runs.md#in7asab1d) | [IN7aSab3a](./query/runs.md#in7asab3a) | [IN7aSab2a](./query/runs.md#in7asab2a) | [IN7aUoM1a](./query/runs.md#in7auom1a) | [IN7aUoM1b](./query/runs.md#in7auom1b) | [IN7aUoM2](./query/runs.md#in7auom2) | [IN7eAPL1a](./query/runs.md#in7eapl1a) | [IN7aSab1c](./query/runs.md#in7asab1c) | [IN7apir1a](./query/runs.md#in7apir1a) | [IN7eAPL2a](./query/runs.md#in7eapl2a) | [IN7eINQ1a](./query/runs.md#in7einq1a) | [IN7eINQ1b](./query/runs.md#in7einq1b) | [IN7eINQ1c](./query/runs.md#in7einq1c) | [IN7eINQ1e](./query/runs.md#in7einq1e) | [IN7eINQ1d](./query/runs.md#in7einq1d) | [IN7eINQ1g](./query/runs.md#in7einq1g) | [IN7eINQ1h](./query/runs.md#in7einq1h) | [IN7eINQ1f](./query/runs.md#in7einq1f) | [IN7eINQ1j](./query/runs.md#in7einq1j) | [IN7eINQ2b](./query/runs.md#in7einq2b) | [IN7eINQ2a](./query/runs.md#in7einq2a) | [IN7aacs1a](./query/runs.md#in7aacs1a) | [IN7eINQ2c](./query/runs.md#in7einq2c) | [IN7eINQ2f](./query/runs.md#in7einq2f) | [IN7eINQ2e](./query/runs.md#in7einq2e) | [IN7eINQ2g](./query/runs.md#in7einq2g) | [IN7eINQ1i](./query/runs.md#in7einq1i) | [IN7eINQ2d](./query/runs.md#in7einq2d) | [IN7eINQ3a](./query/runs.md#in7einq3a) | [IN7eINQ2j](./query/runs.md#in7einq2j) | [IN7eINQ2i](./query/runs.md#in7einq2i) | [IN7eINQ2h](./query/runs.md#in7einq2h) | [IN7eINQ3d](./query/runs.md#in7einq3d) | [IN7eINQ3b](./query/runs.md#in7einq3b) | [IN7eINQ3c](./query/runs.md#in7einq3c) | [IN7eINQ3g](./query/runs.md#in7einq3g) | [IN7eINQ3f](./query/runs.md#in7einq3f) | [IN7eINQ3h](./query/runs.md#in7einq3h) | [IN7eINQ3e](./query/runs.md#in7einq3e) | [IN7eINQ3i](./query/runs.md#in7einq3i) | [IN7eSab1a](./query/runs.md#in7esab1a) | [IN7eSab1c](./query/runs.md#in7esab1c) | [IN7eSab1b](./query/runs.md#in7esab1b) | [IN7eINQ3j](./query/runs.md#in7einq3j) | [IN7eUoM1a](./query/runs.md#in7euom1a) | [IN7eSab1d](./query/runs.md#in7esab1d) | [IN7eSab3a](./query/runs.md#in7esab3a) | [IN7eacs1a](./query/runs.md#in7eacs1a) | [IN7eUoM2](./query/runs.md#in7euom2) | [IN7pINQ1a](./query/runs.md#in7pinq1a) | [IN7epir1a](./query/runs.md#in7epir1a) | [IN7eUoM1b](./query/runs.md#in7euom1b) | [IN7pINQ1e](./query/runs.md#in7pinq1e) | [IN7pAPL2a](./query/runs.md#in7papl2a) | [IN7pINQ1c](./query/runs.md#in7pinq1c) | [IN7pINQ1d](./query/runs.md#in7pinq1d) | [IN7pINQ1g](./query/runs.md#in7pinq1g) | [IN7pINQ1i](./query/runs.md#in7pinq1i) | [IN7pINQ1h](./query/runs.md#in7pinq1h) | [IN7pINQ1b](./query/runs.md#in7pinq1b) | [IN7pINQ1j](./query/runs.md#in7pinq1j) | [IN7pINQ1f](./query/runs.md#in7pinq1f) | [IN7pINQ2a](./query/runs.md#in7pinq2a) | [IN7pINQ2b](./query/runs.md#in7pinq2b) | [IN7eSab2a](./query/runs.md#in7esab2a) | [IN7pINQ2e](./query/runs.md#in7pinq2e) | [IN7pINQ2d](./query/runs.md#in7pinq2d) | [IN7pINQ2f](./query/runs.md#in7pinq2f) | [IN7pAPL1a](./query/runs.md#in7papl1a) | [IN7pINQ2i](./query/runs.md#in7pinq2i) | [IN7pINQ2g](./query/runs.md#in7pinq2g) | [IN7pINQ2h](./query/runs.md#in7pinq2h) | [IN7pINQ2c](./query/runs.md#in7pinq2c) | [IN7pINQ3c](./query/runs.md#in7pinq3c) | [IN7pINQ3b](./query/runs.md#in7pinq3b) | [IN7pINQ3f](./query/runs.md#in7pinq3f) | [IN7pINQ3d](./query/runs.md#in7pinq3d) | [IN7pINQ3e](./query/runs.md#in7pinq3e) | [IN7pINQ2j](./query/runs.md#in7pinq2j) | [IN7pINQ3i](./query/runs.md#in7pinq3i) | [IN7pINQ3a](./query/runs.md#in7pinq3a) | [IN7pINQ3h](./query/runs.md#in7pinq3h) | [IN7pSab1b](./query/runs.md#in7psab1b) | [IN7pSab1a](./query/runs.md#in7psab1a) | [IN7pINQ3j](./query/runs.md#in7pinq3j) | [IN7pSab1c](./query/runs.md#in7psab1c) | [IN7pINQ3g](./query/runs.md#in7pinq3g) | [IN7pUoM1a](./query/runs.md#in7puom1a) | [IN7pacs1a](./query/runs.md#in7pacs1a) | [IN7pSab2a](./query/runs.md#in7psab2a) | [IN7pSab1d](./query/runs.md#in7psab1d) | [IN7pUoM2](./query/runs.md#in7puom2) | [IN7pSab3a](./query/runs.md#in7psab3a) | [IN7ppir1a](./query/runs.md#in7ppir1a) | [IN7pUoM1b](./query/runs.md#in7puom1b)

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

## Interactive 

#### The TREC-9 Interactive Track Report

_William R. Hersh, Paul Over_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/t9irep.pdf](http://trec.nist.gov/pubs/trec9/papers/t9irep.pdf)
??? abstract "Abstract"
	
	The TREC Interactive Track has the goal of investigating interactive information retrieval by examining the process as well as the results. In TREC-9 six research groups ran a total of 12 interactive information retrieval (IR) system variants on a shared problem: a fact-finding task, eight questions, and newspaper/newswire documents from the TREC col-lections. This report summarizes the shared experimental framework, which for TREC-9 was designed to support analysis and comparison of system performance only within sites. The report refers the reader to separate discussions of the experiments performed by each participating group - their hypotheses, experimental systems, and results. The papers from each of the participating groups and the raw and evaluated results are available via the TREC home page (trec.nist.gov).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershO00.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershO00,
		author = {William R. Hersh and Paul Over},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-9} Interactive Track Report},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/t9irep.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershO00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Sheffield Interactive Experiment at TREC-9

_Micheline Hancock-Beaulieu, Helene Fowkes, Hideo Joho_

- :fontawesome-solid-user-group: **Participant:** [sheffield](./interactive/participants.md#sheffield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/sheffield.pdf](http://trec.nist.gov/pubs/trec9/papers/sheffield.pdf)
- :material-file-search: **Runs:** [sheffield-i](./interactive/runs.md#sheffield-i)

??? abstract "Abstract"
	
	The paper reports on the experiment conducted by the University of Sheffield in the Interactive Track of TREC-9 based on the Okapi probabilistic ranking system. A failure analysis of results was undertaken to correlate search outcomes with query characteristics. A detailed comparison of Sheffield results with the aggregate for the track reveals that the time element, topic type, and searcher characteristics and behaviour are interdependent success factors. An analysis of the ranking of documents retrieved by the Okapi system and deemed relevant by the assessors also revealed that more than 50% appeared in the top 10 and 80% in the top 30. However the searchers did not necessarily view these and over half of the items deemed relevant by the assessors and examined by the searchers were actually rejected.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Hancock-BeaulieuFJ00.bib) "
	```
	@inproceedings{DBLP:conf/trec/Hancock-BeaulieuFJ00,
		author = {Micheline Hancock{-}Beaulieu and Helene Fowkes and Hideo Joho},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Sheffield Interactive Experiment at {TREC-9}},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/sheffield.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Hancock-BeaulieuFJ00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melbourne TREC-9 Experiments

_Daryl J. D'Souza, Michael Fuller, James A. Thom, Phil Vines, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./interactive/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/mds.pdf](http://trec.nist.gov/pubs/trec9/papers/mds.pdf)
- :material-file-search: **Runs:** [rmit-i](./interactive/runs.md#rmit-i)

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

#### Question Answering, Relevance Feedback and Summarisation: TREC-9  Interactive Track Report

_Neill Alexander, Craig Brown, Joemon M. Jose, Ian Ruthven, Anastasios Tombros_

- :fontawesome-solid-user-group: **Participant:** [glasgow](./interactive/participants.md#glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/glasgow_proceedings.pdf](http://trec.nist.gov/pubs/trec9/papers/glasgow_proceedings.pdf)
- :material-file-search: **Runs:** [glasgow-i](./interactive/runs.md#glasgow-i)

??? abstract "Abstract"
	
	In this paper we report on the effectiveness of query-biased summaries for a question-answering task. Our summarisation system presents searchers with short summaries of documents, composed of a series of highly matching sentences extracted from the documents. These summaries are also used as evidence for a query expansion algorithm to test the use of summaries as evidence for interactive and automatic query expansion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlexanderBJRT00.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlexanderBJRT00,
		author = {Neill Alexander and Craig Brown and Joemon M. Jose and Ian Ruthven and Anastasios Tombros},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Question Answering, Relevance Feedback and Summarisation: {TREC-9} Interactive Track Report},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/glasgow\_proceedings.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlexanderBJRT00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Support for Question-Answering in Interactive Information Retrieval:  Rutgers' TREC-9 Interactive Track Experience

_Nicholas J. Belkin, Amymarie Keller, Diane Kelly, Jose Perez Carballo, C. Sikora, Ying Sun_

- :fontawesome-solid-user-group: **Participant:** [rutgers-belkin](./interactive/participants.md#rutgers-belkin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec9/papers/rutgers-int.pdf](http://trec.nist.gov/pubs/trec9/papers/rutgers-int.pdf)
- :material-file-search: **Runs:** [rutgers-i](./interactive/runs.md#rutgers-i)

??? abstract "Abstract"
	
	We compared two different interfaces to the InQuery IR system with respect to their support for the TREC-9 Interactive Track Question-Answering task. One interface presented search results as a ranked list of document titles (displayed ten at one time), with the text of one document (the first, or any selected one) displayed in a scrollable window. The other presented search results as a ranked series of scrollable windows of the texts of the retrieved documents, displayed six documents at a time, each document display beginning at the system-computed “best passage”. Our hypotheses were that: multiple-text, best passage display would have an overall advantage for question answering; single-text, multiple title display would have an advantage for the list-oriented question types; and that multiple-text, best passage display would have an advantage for the comparison-oriented question types. The two interfaces were compared on effectiveness, usability and preference measures for sixteen subjects. Results were equivocal.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinKKCSS00.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinKKCSS00,
		author = {Nicholas J. Belkin and Amymarie Keller and Diane Kelly and Jose Perez Carballo and C. Sikora and Ying Sun},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Support for Question-Answering in Interactive Information Retrieval: Rutgers' {TREC-9} Interactive Track Experience},
		booktitle = {Proceedings of The Ninth Text REtrieval Conference, {TREC} 2000, Gaithersburg, Maryland, USA, November 13-16, 2000},
		series = {{NIST} Special Publication},
		volume = {500-249},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2000},
		url = {http://trec.nist.gov/pubs/trec9/papers/rutgers-int.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BelkinKKCSS00.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

