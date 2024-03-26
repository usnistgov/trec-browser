# Proceedings - Routing 1995 

#### Shortest Substring Ranking (MultiText Experiments for TREC-4)

_Charles L. A. Clarke, Gordon V. Cormack, Forbes J. Burkowski_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo](./participants.md#uwaterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/uwaterloo.ps.gz](http://trec.nist.gov/pubs/trec4/papers/uwaterloo.ps.gz)
- :material-file-search: **Runs:** [uwgcl1](./runs.md#uwgcl1)

??? abstract "Abstract"
	
	To address the TREC-4 topics, we used a precise query language that yields and combines arbitrary intervals of text rather than pre-defined units like words and documents. Each solution was scored in inverse proportion to the length of the shortest interval containing it. Each document was scored by the sum of the scores of solutions within it. Whenever the above strategy yielded less than 1000 documents, documents satisfying successively weaker queries were added with lower rank. Our results for the ad-hoc topics compare favourably with the median average precision for all groups.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCB95.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCB95,
		author = {Charles L. A. Clarke and Gordon V. Cormack and Forbes J. Burkowski},
		editor = {Donna K. Harman},
		title = {Shortest Substring Ranking (MultiText Experiments for {TREC-4)}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/uwaterloo.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCB95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Recent Experiments with INQUERY

_James Allan, Lisa Ballesteros, James P. Callan, W. Bruce Croft, Zhihong Lu_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz](http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz)
- :material-file-search: **Runs:** [INQ203](./runs.md#inq203) | [INQ204](./runs.md#inq204)

??? abstract "Abstract"
	
	Past TREC experiments by the University of Massachusetts have focused primarily on ad-hoc query creation. Substantial effort was directed towards automatically translating TREC topics into queries, using a set of simple heuristics and query expansion. Less emphasis was placed on the routing task, although results were generally good. The Spanish experiments in TREC-3 concentrated on simple indexing, sophisticated stemming, and simple methods of creating queries. The TREC-4 experiments were a departure from the past. The ad-hoc experiments involved 'fine tuning' existing approaches, and modifications to the INQUERY term weighting algorithm. However, much of the research focus in TREC-4 was on the routing, Spanish, and collection merging experiments. These tracks more closely match our broader research interests in document routing, document filtering, distributed IR, and multilingual retrieval. The University of Massachusetts' experiments were conducted with version 3.0 of the INQUERY information retrieval system. INQUERY is based on the Bayesian inference network retrieval model. It is described elsewhere [7, 5, 12, 11], so this paper focuses on relevant differences to the previously published algorithms.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanBCCL95.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanBCCL95,
		author = {James Allan and Lisa Ballesteros and James P. Callan and W. Bruce Croft and Zhihong Lu},
		editor = {Donna K. Harman},
		title = {Recent Experiments with {INQUERY}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/umass.ps.gz},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AllanBCCL95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### New Retrieval Approaches Using SMART: TREC 4

_Chris Buckley, Amit Singhal, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [cornell](./participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/Cornell_trec4.ps.gz](http://trec.nist.gov/pubs/trec4/papers/Cornell_trec4.ps.gz)
- :material-file-search: **Runs:** [CrnlRE](./runs.md#crnlre) | [CrnlRL](./runs.md#crnlrl)

??? abstract "Abstract"
	
	The Smart information retrieval project emphasizes completely automatic approaches to the understanding and retrieval of large quantities of text. We continue our work in TREC 4, performing runs in the routing, ad-hoc, confused text, interactive, and foreign language environments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleySM95.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleySM95,
		author = {Chris Buckley and Amit Singhal and Mandar Mitra},
		editor = {Donna K. Harman},
		title = {New Retrieval Approaches Using {SMART:} {TREC} 4},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/Cornell\_trec4.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleySM95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Research in Automatic Profile Generation and Passage-Level Routing  with LMDS

_Julian A. Yochum_

- :fontawesome-solid-user-group: **Participant:** [logicon](./participants.md#logicon)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/logicon.ps.gz](http://trec.nist.gov/pubs/trec4/papers/logicon.ps.gz)
- :material-file-search: **Runs:** [losPA2](./runs.md#lospa2) | [losPA3](./runs.md#lospa3)

??? abstract "Abstract"
	
	This paper describes the development of a prototype system to generate routing profiles automatically from sets of relevant documents provided by a user, and to assign relevance scores to the documents selected by these profiles. The prototype was developed with the Logicon Message Dissemination System (LMDS) for participation in the Fourth Text REtrieval Conference (TREC-4). Each generated profile contains two sets of terms: a very small set to select documents, and a much larger set to assign a relevance score to each document selected. The profile generator chooses each term and assigns a weight to it, based on its frequency of occurrence in the set of documents provided by the user, and on its frequency of occurrence in a large representative corpus of documents. The LMDS search engine uses the resulting profiles to select documents, and then passes the documents to the scoring prototype for ranking. The score assigned is a function of the weights of all profile terms found in the entire document, and of those found in fixed-length overlapping passages within the document. Performance figures and TREC-4 results are included. An appendix describes a modification to the TREC-4 algorithm, made since the conference, which has produced significant improvements in both recall and precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yochum95.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yochum95,
		author = {Julian A. Yochum},
		editor = {Donna K. Harman},
		title = {Research in Automatic Profile Generation and Passage-Level Routing with {LMDS}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/logicon.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Yochum95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Natural Language Information Retrieval: TREC-4 Report

_Tomek Strzalkowski, Jose Perez Carballo_

- :fontawesome-solid-user-group: **Participant:** [nyuge](./participants.md#nyuge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/nyuge.ps.gz](http://trec.nist.gov/pubs/trec4/papers/nyuge.ps.gz)
- :material-file-search: **Runs:** [nyuge1](./runs.md#nyuge1) | [nyuge2](./runs.md#nyuge2)

??? abstract "Abstract"
	
	In this paper we report on the joint GE/NYU natural language information retrieval project as related to the 4th Text Retrieval Conference (TREC-4). The main thrust of this project is to use natural language processing techniques to enhance the effectiveness of full-text document retrieval. During the course of the four TREC conferences, we have built a prototype IR system designed around a statistical full-text indexing and search backbone provided by the NIST's Prise engine. The original Prise has been modified to allow handling of multi-word phrases, differential term weighting schemes, automatic query expansion, index partitioning and rank merging, as well as dealing with complex documents. Natural language processing is used to (1) preprocess the documents in order to extract content-carrying terms, (2) discover inter-term dependencies and build a conceptual hierarchy specific to the database domain, and (3) process user's natural language requests into effective search queries. The overall architecture of the system is essentially the same as in TREC-3, as our efforts this year were directed at optimizing the performance of all components. A notable exception is the new massive query expansion module used in routing experiments, which replaces a prototype extension used in the TREC-3 system. On the other hand, it has to be noted that the character and the level of difficulty of TREC queries has changed quite significantly since the last year evaluation. TREC-4 new ad-hoc queries are far shorter, less focused, and they have a flavor of information requests (What is the prognosis of ...) rather than search directives typical for earlier TRECs (The relevant document will contain ...). This makes building of good search queries a more sensitive task than before. We thus decided to introduce only minimum number of changes to our indexing and search processes, and even roll back some of the TREC-3 extensions which dealt with longer and somewhat redundant queries (e.g., locality matching? ). Overall, our system performed quite well as our position with respect to the best systems improved steadily since the beginning of TREC. It should be noted that the most significant gain in performance seems to occur in precision near the top of the ranking, at 5, 10, 15 and 20 documents. Indeed, our unofficial manual runs performed after TREC-4 conference show superior results in these categories, topping by a large margin the best manual scores by any system in the official evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StrzalkowskiC95.bib) "
	```
	@inproceedings{DBLP:conf/trec/StrzalkowskiC95,
		author = {Tomek Strzalkowski and Jose Perez Carballo},
		editor = {Donna K. Harman},
		title = {Natural Language Information Retrieval: {TREC-4} Report},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/nyuge.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StrzalkowskiC95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi at TREC-4

_Stephen E. Robertson, Steve Walker, Micheline Hancock-Beaulieu, Mike Gatford, A. Payne_

- :fontawesome-solid-user-group: **Participant:** [city](./participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/city.ps.gz](http://trec.nist.gov/pubs/trec4/papers/city.ps.gz)
- :material-file-search: **Runs:** [cityr1](./runs.md#cityr1) | [cityr2](./runs.md#cityr2)

??? abstract "Abstract"
	
	City have submitted interactive runs in all the previous TRECs, with fairly undistinguished results. This time the main emphasis has been on the development of an entirely new interactive ad hoc search system (Sections 3 and Appendix). On the non-interactive side routing term selection: there has been further work on methods of selecting routing terms; manual and automatic ad hoc: the automatic ad hoc was done in more or less the same way as for TREC-3, but in view of the very brief topic statements a few runs were also done with manually edited queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonWHGP95.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonWHGP95,
		author = {Stephen E. Robertson and Steve Walker and Micheline Hancock{-}Beaulieu and Mike Gatford and A. Payne},
		editor = {Donna K. Harman},
		title = {Okapi at {TREC-4}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/city.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonWHGP95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Xerox Site Report: Four TREC-4 Tracks

_Marti A. Hearst, Jan O. Pedersen, Peter Pirolli, Hinrich Schütze, Gregory Grefenstette, David A. Hull_

- :fontawesome-solid-user-group: **Participant:** [xerox](./participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/xerox.ps.gz](http://trec.nist.gov/pubs/trec4/papers/xerox.ps.gz)
- :material-file-search: **Runs:** [xerox1](./runs.md#xerox1) | [xerox2](./runs.md#xerox2)

??? abstract "Abstract"
	
	The Xerox research centers participated in four TREC-4 activities: the routing task, the filtering track, the Spanish track, and the interactive track. We addressed the core routing task as a problem in statistical classifica-tion: given a training set of judged documents, build an error-minimizing statistical classifier to assess the relevance of new test documents. This year, we built on the methodology developed in 21] by adding a combination strategy that pooled evidence across a number of separately trained classification schemes. Since many of our classifiers infer probability of relevance, adapting our routing methods to the filtering track consisted of obtaining probability estimates for the remaining classifiers and reporting those documents scoring above the probability thresholds determined by the three set linear utility func-tions. Our contribution to the Spanish track focussed on the effect of principled language analysis on a baseline retrieval system. We employed finite-state morphology [14] and hidden-Markov-model-based part-of-speech tagging 17] to analyze Spanish language text into canonical stemmed forms, and to identify verbs and noun phrases. Various combinations of these were then fed into SMART [1] for ranked retrieval. This year our activity on the ad hoc task focussed on the interactive track, which allows arbitrary user interaction in the process of finding relevant documents. We developed a graphical user interface to two interactive tools, Scatter/Gather [6] and Tilebars [11], and asked a number of subjects to use this tool to 'find as many good documents as you can for a topic, in around 30 minutes, without collecting too much rubbish'. We set up an experimental design to measure the value of each tool, and their combination, averaging out subject effects. That is, we were interested in determining how well the average user might perform with interactive tools rather than measuring the very best performance possible assuming an expert searcher. These efforts are described in more detail in the following sections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HearstPPSGH95.bib) "
	```
	@inproceedings{DBLP:conf/trec/HearstPPSGH95,
		author = {Marti A. Hearst and Jan O. Pedersen and Peter Pirolli and Hinrich Sch{\"{u}}tze and Gregory Grefenstette and David A. Hull},
		editor = {Donna K. Harman},
		title = {Xerox Site Report: Four {TREC-4} Tracks},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/xerox.ps.gz},
		timestamp = {Thu, 08 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HearstPPSGH95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Acquaintance: Language-Independent Document Categorization by N-Grams

_Stephen Huffman_

- :fontawesome-solid-user-group: **Participant:** [nsa](./participants.md#nsa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/nsa.ps.gz](http://trec.nist.gov/pubs/trec4/papers/nsa.ps.gz)
- :material-file-search: **Runs:** [ACQROU](./runs.md#acqrou)

??? abstract "Abstract"
	
	Acquaintance is the name of a novel vector-space n-gram technique for categorizing documents. The technique is completely language-independent, highly garble-resistant, and computationally simple. An unoptimized version of the algorithm was used to process the TREC database in a very short time.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Huffman95.bib) "
	```
	@inproceedings{DBLP:conf/trec/Huffman95,
		author = {Stephen Huffman},
		editor = {Donna K. Harman},
		title = {Acquaintance: Language-Independent Document Categorization by N-Grams},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/nsa.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Huffman95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Logistic Regression at TREC4: Probabilistic Retrieval from Full  Text Document Collections

_Fredric C. Gey, Aitao Chen, Jianzhang He, Jason Meggs_

- :fontawesome-solid-user-group: **Participant:** [berkeley](./participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/berkeley.ps.gz](http://trec.nist.gov/pubs/trec4/papers/berkeley.ps.gz)
- :material-file-search: **Runs:** [Brkly11](./runs.md#brkly11) | [Brkly12](./runs.md#brkly12)

??? abstract "Abstract"
	
	The Berkeley experiments for TREC4 extend those of TREC3 in three ways: for ad-hoc retrieval we retain the manual reformulations of the topics and experiment with limited query expansion based upon the assumption that top documents are relevant (this experiment was an interesting failure); for routing retrieval we introduce a logistic regression which assumes relevance weights to be only one clue among several in predicting probability of relevance. Finally, for Spanish retrieval we retrain the basic logistic regression equations to apply to the statistical distributions of Spanish words. In addition we apply two approaches to Spanish stemming, one which attempts to resolve verb variants into a standardized form, the other of which eschews stemming in favor of a massive stop word list of variants of common words.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyCHM95.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyCHM95,
		author = {Fredric C. Gey and Aitao Chen and Jianzhang He and Jason Meggs},
		editor = {Donna K. Harman},
		title = {Logistic Regression at {TREC4:} Probabilistic Retrieval from Full Text Document Collections},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/berkeley.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GeyCHM95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-4 Ad-Hoc, Routing Retrieval and Filtering Experiments using  PIRCS

_K. L. Kwok, Laszlo Grunfeld_

- :fontawesome-solid-user-group: **Participant:** [queens](./participants.md#queens)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/queenst4.ps.gz](http://trec.nist.gov/pubs/trec4/papers/queenst4.ps.gz)
- :material-file-search: **Runs:** [pircsC](./runs.md#pircsc) | [pircsL](./runs.md#pircsl)

??? abstract "Abstract"
	
	Our ad-hoc submissions are pircsi which is fully automatic, and pircs2 which involves manually weighting some terms and adding some new words to the original topic descriptions. The number of words added are minimal. Both methods involve training and query expansion using the best-ranked subdocuments from an initial retrieval as feedback. For our routing experiments we make use of massive query expansion of 350 terms in pircsL, with emphasis on expansion with low frequency terms. Training is done using short and top-ranked known relevant subdocuments. In pircsC, we define four different 'expert' queries (pircsL being one of them) for each topic by using different subsets of training document, and later combine their retrieval results into one. Filtering experiment is done with the retrieval lists of pircsL. For each query, we use the training collections to define retrieval status values (RSVs) where the utilities are maximum for the three precision types. These RSVs are then used as thresholds for the new collections. Evaluated results show that both ad-hoc and routing retrievals perform substantially better than median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokG95.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokG95,
		author = {K. L. Kwok and Laszlo Grunfeld},
		editor = {Donna K. Harman},
		title = {{TREC-4} Ad-Hoc, Routing Retrieval and Filtering Experiments using {PIRCS}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/queenst4.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokG95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multi-lingual Text Filtering Using Semantic Modeling

_James R. Driscoll, S. Abbott, K. Hu, M. Miller, G. Theis_

- :fontawesome-solid-user-group: **Participant:** [ucf](./participants.md#ucf)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/papers/ucentral-florida.pdf](https://trec.nist.gov/pubs/trec4/papers/ucentral-florida.pdf)
- :material-file-search: **Runs:** [UCF100](./runs.md#ucf100)

??? abstract "Abstract"
	
	Semantic Modeling is used to investigate multilingual text filtering. In our approach, the Entity-Relationship (ER) Model is used as a basis for descriptions of information preferences (profiles) in the information filtering process. A profile is viewed as having both a static aspect and a dynamic aspect. The static aspect of a profile can be represented as an ER schema; and the dynamic aspect of the profile can be represented by synonyms of schema components and domain values for schema attributes. For TREC-4, the routing task and the Spanish adhoc task are accomplished using this technique. For the routing task, a large amount of time was spent in an effort to optimize filter performance using the training data that was available for the routing topics. For the Spanish adhoc task, a large amount of time was spent using external sources to develop good filters; in addition, some time was spent implementing a program to help port our approach to this second language. A multi-lingual (English, French, German, and Spanish) experiment is also reported.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DriscollAHMT95.bib) "
	```
	@inproceedings{DBLP:conf/trec/DriscollAHMT95,
		author = {James R. Driscoll and S. Abbott and K. Hu and M. Miller and G. Theis},
		editor = {Donna K. Harman},
		title = {Multi-lingual Text Filtering Using Semantic Modeling},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/papers/ucentral-florida.pdf},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DriscollAHMT95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLARIT TREC-4 Interactive Experiments

_Natasa Milic-Frayling, Michael P. Mastroianni, David A. Evans, Robert G. Lefferts, ChengXiang Zhai, Xiang Tong_

- :fontawesome-solid-user-group: **Participant:** [clarit](./participants.md#clarit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/t4_proceedings.html](https://trec.nist.gov/pubs/trec4/t4_proceedings.html)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Milic-FraylingMELZT95.bib) "
	```
	@inproceedings{DBLP:conf/trec/Milic-FraylingMELZT95,
		author = {Natasa Milic{-}Frayling and Michael P. Mastroianni and David A. Evans and Robert G. Lefferts and ChengXiang Zhai and Xiang Tong},
		editor = {Donna K. Harman},
		title = {{CLARIT} {TREC-4} Interactive Experiments},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/t4_proceedings.html},
		timestamp = {Fri, 19 Jun 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Milic-FraylingMELZT95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Document Routing by Discriminant Projection: TREC-4

_Kok F. Lai, Vincent A. S. Lee, Jeremy P. Chew_

- :fontawesome-solid-user-group: **Participant:** [iti](./participants.md#iti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec4/papers/iti.ps.gz](http://trec.nist.gov/pubs/trec4/papers/iti.ps.gz)
- :material-file-search: **Runs:** [itidp1](./runs.md#itidp1) | [itidp2](./runs.md#itidp2)

??? abstract "Abstract"
	
	We present document routing as a standard problem in discriminant analysis. The standard solution involves the inversion of a large matrix whose dimension is the number of indexed terms. Typically, the solution does not exist because the number of training documents are much smaller compared to the number of terms. We show that one can project this raw document space into a lower dimensional space where solution is possible. Our projection algorithm exploits the characterisitics of the empty space, using only the training documents for efficient coding of the relevance information. Its complexity is linear with respect to the number of terms, and second order with respect to the number of training documents. We can therefore fully exploit the power of discriminant analysis without imposing severe computational and storage constraints.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LaiLC95.bib) "
	```
	@inproceedings{DBLP:conf/trec/LaiLC95,
		author = {Kok F. Lai and Vincent A. S. Lee and Jeremy P. Chew},
		editor = {Donna K. Harman},
		title = {Document Routing by Discriminant Projection: {TREC-4}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {http://trec.nist.gov/pubs/trec4/papers/iti.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LaiLC95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improvements on Query Term Expansion and Ranking Formula

_Kenji Satoh, Susumu Akamine, Akitoshi Okumura_

- :fontawesome-solid-user-group: **Participant:** [nec](./participants.md#nec)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/t4_proceedings.html](https://trec.nist.gov/pubs/trec4/t4_proceedings.html)
- :material-file-search: **Runs:** [virtu3](./runs.md#virtu3)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SatohAO95.bib) "
	```
	@inproceedings{DBLP:conf/trec/SatohAO95,
		author = {Kenji Satoh and Susumu Akamine and Akitoshi Okumura},
		editor = {Donna K. Harman},
		title = {Improvements on Query Term Expansion and Ranking Formula},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/t4_proceedings.html},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SatohAO95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using CONVECTIS, A Context Vector-Based Indexing System for TREC-4

_Joel Carleton, William R. Caid, R. V. Sasseen_

- :fontawesome-solid-user-group: **Participant:** [hnc](./participants.md#hnc)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec4/t4_proceedings.html](https://trec.nist.gov/pubs/trec4/t4_proceedings.html)
- :material-file-search: **Runs:** [HNC11](./runs.md#hnc11) | [HNC21](./runs.md#hnc21)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarletonCS95.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarletonCS95,
		author = {Joel Carleton and William R. Caid and R. V. Sasseen},
		editor = {Donna K. Harman},
		title = {Using CONVECTIS, {A} Context Vector-Based Indexing System for {TREC-4}},
		booktitle = {Proceedings of The Fourth Text REtrieval Conference, {TREC} 1995, Gaithersburg, Maryland, USA, November 1-3, 1995},
		series = {{NIST} Special Publication},
		volume = {500-236},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1995},
		url = {https://trec.nist.gov/pubs/trec4/t4_proceedings.html},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CarletonCS95.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

