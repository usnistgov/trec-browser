# Proceedings - Routing 1996 

#### INQUERY at TREC-5

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, John Broglio, Jinxi Xu, Hongming Shu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz](http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz)
- :material-file-search: **Runs:** [INQ303](./runs.md#inq303)

??? abstract "Abstract"
	
	The University of Massachusetts participated in five tracks in TREC-5: Ad-hoc, Routing, Fil-tering, Chinese, and Spanish. Our results are generally positive, continuing to indicate that the techniques we have applied perform well in a variety of settings. Significant changes in our approaches include emphasis on identifying key concepts/terms in the query topics, expansion of the query using a variant of automatic feedback called 'Local Context Analysis', and application of these techniques to a non-European language. The results show the broad applicability of Local Context Analysis, demonstrate successful identification and use of key concepts, raise interesting questions about how key concepts affect precision, support the belief that many IR techniques can be applied across languages, present an intriguing lack of tradeoff between recall and precision when filtering, and confirm once again several known results about query formulation and combination. Regrettably, three of our official submissions were marred by errors in the processing (an undetected syntax error in some queries, and an incomplete data set in an another case). The following discussion analyzes corrected runs as well as those (not particularly meaningful) submitted runs. Our experiments were conducted with version 3.1 of the INQUERY information retrieval system. INQUERY is based on the Bayesian inference network retrieval model. It is described elsewhere [5, 4, 12, 11], so this paper focuses on relevant differences to the previously published algorithms.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCCBBHS96.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCCBBHS96,
		author = {James Allan and James P. Callan and W. Bruce Croft and Lisa Ballesteros and John Broglio and Jinxi Xu and Hongming Shu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} at {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AllanCCBBHS96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SPIDER Retrieval System at TREC-5

_Jean Paul Ballerini, Marco Büchel, Ruxandra Domenig, Daniel Knaus, Bojidar Mateev, Elke Mittendorf, Peter Schäuble, Paraic Sheridan, Martin Wechsler_

- :fontawesome-solid-user-group: **Participant:** [ETH](./participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/ETHatTREC5.final.USLetter.ps.gz](http://trec.nist.gov/pubs/trec5/papers/ETHatTREC5.final.USLetter.ps.gz)
- :material-file-search: **Runs:** [ETHru1](./runs.md#ethru1)

??? abstract "Abstract"
	
	The ETH group participated in this year's TREC in the following tracks: automatic adhoc (long and short), the manual adhoc, routing, and confusion. We also did some experiments on the chinese data which were not submitted. While for adhoc we relied mainly on methods which were well evaluated in previous TRECs, we successfully tried completely new techniques for the routing task and the confusion task: for routing we found an optimal feature selection method and included co-occurrence data into the retrieval function; for confusion we applied a robust probabilistic technique for estimating feature frequencies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalleriniBDKMMSSW96.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalleriniBDKMMSSW96,
		author = {Jean Paul Ballerini and Marco B{\"{u}}chel and Ruxandra Domenig and Daniel Knaus and Bojidar Mateev and Elke Mittendorf and Peter Sch{\"{a}}uble and Paraic Sheridan and Martin Wechsler},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SPIDER} Retrieval System at {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/ETHatTREC5.final.USLetter.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalleriniBDKMMSSW96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure02: adhoc and routing tasks

_Mohand Boughanem, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/irit.ps.gz](http://trec.nist.gov/pubs/trec5/papers/irit.ps.gz)
- :material-file-search: **Runs:** [Mercure1](./runs.md#mercure1) | [Mercure2](./runs.md#mercure2)

??? abstract "Abstract"
	
	Mercure02 is an object oriented information retrieval system based on connectionist approach. It allows the query formulation, the query evaluation based on propagation of the neuron activation and the query modification based on backpropagation of the user judgements of the document relevance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemS96.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemS96,
		author = {Mohand Boughanem and Chantal Soul{\'{e}}{-}Dupuy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure02: adhoc and routing tasks},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/irit.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemS96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Query Zoning and Correlation Within SMART: TREC 5

_Chris Buckley, Amit Singhal, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [Cornell](./participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz](http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz)
- :material-file-search: **Runs:** [Cor5R1cc](./runs.md#cor5r1cc) | [Cor5R2cr](./runs.md#cor5r2cr)

??? abstract "Abstract"
	
	The Smart information retrieval project emphasizes completely automatic approaches to the understanding and retrieval of large quantities of text. We continue our work in TREC 5, performing runs in the routing, ad-hoc, and foreign language environments. The major focus this year is on 'zoning' different parts of an initial retrieval ranking, and treating each type of query zone differently as processing continues. We also experiment with dynamic phrasing, seeing which words co-occur with original query words in documents judged relevant. Exactly the same procedure is used for foreign language environments as for English; our tenet is that good information retrieval techniques are more powerful than linguistic knowledge.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleySM96.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleySM96,
		author = {Chris Buckley and Amit Singhal and Mandar Mitra},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Query Zoning and Correlation Within {SMART:} {TREC} 5},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleySM96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Substring Retrieval (MultiText Experiments for TREC-5)

_Charles L. A. Clarke, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/waterloo.ps.gz](http://trec.nist.gov/pubs/trec5/papers/waterloo.ps.gz)
- :material-file-search: **Runs:** [uwgcr0](./runs.md#uwgcr0)

??? abstract "Abstract"
	
	Queries for TREC-5 were formulated in the GCL query language using an interactive system that showed short passages containing relevant terms. Solutions to the queries were ranked by the shortest substring method introduced at TREC-4, resulting in good precision/recall performance in the adhoc and routing tasks. Performance results were found to be insensitive to a document length normalization adjustment. Shortest substring ranking was augmented by the use of a progression of successively weaker queries to improve recall, but this augmentation provided only a slight improvement to overall retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeC96.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeC96,
		author = {Charles L. A. Clarke and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Interactive Substring Retrieval (MultiText Experiments for {TREC-5)}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/waterloo.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeC96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CRL English Routing System for TREC-5

_James R. Cowie, Zhiqiang Guan_

- :fontawesome-solid-user-group: **Participant:** [NMSU-C](./participants.md#nmsu-c)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/nmsu.cowie.ps.gz](http://trec.nist.gov/pubs/trec5/papers/nmsu.cowie.ps.gz)
- :material-file-search: **Runs:** [nmsu-1](./runs.md#nmsu-1)

??? abstract "Abstract"
	
	The routing system described here was initially developed as a final filter to rank documents being produced by multiple queries given to a Boolean retrieval system. This system was still being developed by the time the TREC-5 deadline arrived and it was decided to use the filtering component on its own for the routing task. The router was trained using the relevance judgements from previous evalua-tions. It is based on a theoretical approach for discriminating between two different types of documents developed by Guthrie and Walker [1]. The generalizations made to extend this approach to multiple document types are not, however, particularly well founded. The system is a true router, each document is handled individually and matched against a profile for each topic to decide if it should be rejected or included. The results for the method are poor. The most likely cause for this is that any word in a profile can count multiple times towards success or failure. The method is similar in many ways to a vector based retrieval system, with a vector for each topic being matched against a word vector for the document.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CowieG96.bib) "
	```
	@inproceedings{DBLP:conf/trec/CowieG96,
		author = {James R. Cowie and Zhiqiang Guan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CRL} English Routing System for {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/nmsu.cowie.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CowieG96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Term importance, Boolean conjunct training, negative terms, and foreign  language retrieval: probabilistic algorithms at TREC-5

_Fredric C. Gey, Aitao Chen, Jianzhang He, Liangjie Xu, Jason Meggs_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz](http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz)
- :material-file-search: **Runs:** [brkly13](./runs.md#brkly13) | [brkly14](./runs.md#brkly14)

??? abstract "Abstract"
	
	The Berkeley experiments for TREC-5 extend those of TREC-4 in numerous ways. For routing retrieval we experimented with the idea of term importance in three ways -- training on Boolean con-juncts of the most important terms, filtering with the most important terms, and, finally, logistic regression on presence or absence of those terms. For ad-hoc retrieval we retained the manual reformulations of the topics and experimented with negative query terms. The ad-hoc retrieval formula originally devised for TREC-2 has proven to be robust, and was used for the TREC-5 ad-hoc retrieval and for our Chinese and Spanish retrieval. Chinese retrieval was accomplished through development of a segmentation algorithm which was used to augment a Chinese dictionary. The manual query run BrklyCH2 achieved a spectacular 97.48 percent recall over the 19 queries evaluated before the conference.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyCHXM96.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyCHXM96,
		author = {Fredric C. Gey and Aitao Chen and Jianzhang He and Liangjie Xu and Jason Meggs},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Term importance, Boolean conjunct training, negative terms, and foreign language retrieval: probabilistic algorithms at {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GeyCHXM96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi at TREC-5

_Micheline Hancock-Beaulieu, Mike Gatford, Xiangji Huang, Stephen E. Robertson, Steve Walker, P. W. Williams_

- :fontawesome-solid-user-group: **Participant:** [City](./participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz)
- :material-file-search: **Runs:** [city96r1](./runs.md#city96r1) | [city96r2](./runs.md#city96r2)

??? abstract "Abstract"
	
	City submitted two runs each for the automatic ad hoc, very large collection track, automatic routing and Chinese track; and took part in the interactive and filtering tracks. There were no very significant new developments; the same Okapi-style weighting as in TREC-3 and TREC-4 was used this time round, although there were attempts, in the ad hoc and more notably in the Chinese experiments, to extend the weighting to cover searches containing both words and phrases. All submitted runs except for the Chinese incorporated run-time passage determination and searching. The Okapi back-end search engine has been considerably speeded, and a few new functions incorporated. See Section 3.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Hancock-BeaulieuGHRWW96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Hancock-BeaulieuGHRWW96,
		author = {Micheline Hancock{-}Beaulieu and Mike Gatford and Xiangji Huang and Stephen E. Robertson and Steve Walker and P. W. Williams},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Okapi at {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Hancock-BeaulieuGHRWW96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Xerox TREC-5 Site Report: Routing, Filtering, NLP, and Spanish Tracks

_David A. Hull, Gregory Grefenstette, B. Maximilian Schulze, Éric Gaussier, Hinrich Schütze, Jan O. Pedersen_

- :fontawesome-solid-user-group: **Participant:** [Xerox](./participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz](http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz)
- :material-file-search: **Runs:** [xerox.rout1](./runs.md#xerox.rout1) | [xerox.rout2](./runs.md#xerox.rout2) | [xerox.rout3](./runs.md#xerox.rout3)

??? abstract "Abstract"
	
	Xerox participated in TREC 5 through experiments carried out separately and conjointly at the Rank Xerox Research Centre (RXRC) in Grenoble and the Xerox Palo Alto Research Center The remainder of this report is divided into three sections. The first section describes our work on routing and filtering (Hull, Schütze, and Pedersen), the second section covers the NLP track (Grefenstette, Schulze, and Gaussier), and the final section addresses the Spanish track (Grefenstette, Schulze, and Hull).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HullGSGSP96.bib) "
	```
	@inproceedings{DBLP:conf/trec/HullGSGSP96,
		author = {David A. Hull and Gregory Grefenstette and B. Maximilian Schulze and {\'{E}}ric Gaussier and Hinrich Sch{\"{u}}tze and Jan O. Pedersen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Xerox {TREC-5} Site Report: Routing, Filtering, NLP, and Spanish Tracks},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz},
		timestamp = {Thu, 08 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HullGSGSP96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on Routing, Filtering and Chinese Text Retrieval in TREC-5

_Chong-Wah Ngo, Kok F. Lai_

- :fontawesome-solid-user-group: **Participant:** [ITI-SG](./participants.md#iti-sg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/iti.trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/iti.trec5.ps.gz)
- :material-file-search: **Runs:** [itidp1](./runs.md#itidp1) | [itidp2](./runs.md#itidp2)

??? abstract "Abstract"
	
	We describes our experiments in the routing, filtering and Chinese text retrieval. We based our routing and filtering experiments on our discriminant project algorithm. The algorithm sequentially constructs a series of orthogonal axis from the training documents using the Gram-Schmidt procedure. It then rotates the resulting subspace using principal component analysis so that the axis are ordered by their importance. For Chinese text retrieval, we experimented both with an automatic method and a manual method. For the automatic method, we use all phrases in the description field and compute the aggregate scores using the simple tf.idf formula. We then manually construct boolean phrase queries which are thought to improve the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NgoL96.bib) "
	```
	@inproceedings{DBLP:conf/trec/NgoL96,
		author = {Chong{-}Wah Ngo and Kok F. Lai},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments on Routing, Filtering and Chinese Text Retrieval in {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/iti.trec5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NgoL96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-5 English and Chinese Retrieval Experiments using PIRCS

_K. L. Kwok, Laszlo Grunfeld_

- :fontawesome-solid-user-group: **Participant:** [CUNY](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz](http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz)
- :material-file-search: **Runs:** [pircsg0](./runs.md#pircsg0) | [pircsg6](./runs.md#pircsg6)

??? abstract "Abstract"
	
	Two English automatic ad-hoc runs have been submitted: pircsAAS uses short and pircsAAL employs long topics. Our new avtf*ildf term weighting was used for short queries. 2-stage retrieval were performed. Both automatic runs are much better than the overall automatic average. Two manual runs are based on short topics: pircAM1 employs double weighting for user-selected query terms and pircs AM2 additionally extends these queries with new terms chosen manually. They perform about average compared with the the overall manual runs. Our two Chinese automatic ad-hoc runs are: pircsCw, using short-word segmentation for Chinese texts and piresCwc, which additionally includes single characters. Both runs are much better than average, but pircsCwe has a slight edge over pircsCw. In routing a genetic algorithm is used to select suitable subsets of relevant documents for training queries. Out of an initial random population of 15, the best subset (based on average precision) was employed to train the routing queries for the pircsRGO run. This ith (= 0) population is operated by a probabilistic reproduction and crossover strategy to produce the (i+1)th and evaluated, and this iterates for 6 generations. The best relevant subset of the 6th is used for training our queries for pircsRG6. It performs a few percent better than pircsRGO, and both are well above average. For the filtering experiment, we use thresholding on the retrieval status values; thresholds are trained based on the utility functions. Results are also good.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokG96.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokG96,
		author = {K. L. Kwok and Laszlo Grunfeld},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-5} English and Chinese Retrieval Experiments using {PIRCS}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokG96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Metric Multidimensional Information Space

_Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [UIUC](./participants.md#uiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/newby-proceedings-final.ps.gz](http://trec.nist.gov/pubs/trec5/papers/newby-proceedings-final.ps.gz)
- :material-file-search: **Runs:** [ispaR](./runs.md#ispar)

??? abstract "Abstract"
	
	The rationale and methodology for retrieval based on the relative locations of documents within a geometric information space are introduced. Results from category A routing and filtering experiments in TREC-5 are discussed. The techniques used are related to the vector space model, latent semantic indexing, and other methods that rely on statistical qualities of texts to assess document relatedness. Results show some promise, but additional research is needed to determine the extent to which retrieval may be improved over existing approaches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Newby96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Newby96,
		author = {Gregory B. Newby},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Metric Multidimensional Information Space},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/newby-proceedings-final.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Newby96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Data Fusion of Machine-Learning Methods for the TREC5 Routing Task  (and other work)

_Kwong Bor Ng, David Loewenstern, Chumki Basu, Haym Hirsh, Paul B. Kantor_

- :fontawesome-solid-user-group: **Participant:** [RutgersK](./participants.md#rutgersk)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/rutgers.kantor.ps.gz](http://trec.nist.gov/pubs/trec5/papers/rutgers.kantor.ps.gz)
- :material-file-search: **Runs:** [rutAPspt](./runs.md#rutapspt) | [rutAPglob](./runs.md#rutapglob)

??? abstract "Abstract"
	
	The goal of the document routing task is to extrapolate from documents judged relevant or irrelevant for each of a set of topics accurate procedures for assessing the relevance of future documents for each topic. Rather than viewing different approaches to this problem as 'winner-takes-all' competitors, we view them as potentially complementary methods, each exploiting different sources of information. This paper describes two quite different machine-learning approaches to the document routing task, and two approaches to combining their results to perform relevance assessments on new documents. We also describe an approach to the the confusion task based on n-grams that allow approximate matches.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NgLBHK96.bib) "
	```
	@inproceedings{DBLP:conf/trec/NgLBHK96,
		author = {Kwong Bor Ng and David Loewenstern and Chumki Basu and Haym Hirsh and Paul B. Kantor},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Data Fusion of Machine-Learning Methods for the {TREC5} Routing Task (and other work)},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/rutgers.kantor.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NgLBHK96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Relevance to Train a Linear Mixture of Experts

_Christopher C. Vogt, Garrison W. Cottrell, Richard K. Belew, Brian T. Bartell_

- :fontawesome-solid-user-group: **Participant:** [UCSD](./participants.md#ucsd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/ucsd.ps.gz](http://trec.nist.gov/pubs/trec5/papers/ucsd.ps.gz)
- :material-file-search: **Runs:** [sdmix3](./runs.md#sdmix3)

??? abstract "Abstract"
	
	A linear mixture of experts is used to combine three standard IR systems. The parameters for the mixture are determined automatically through training on document relevance assessments via optimization of a rank-order statistic which is empirically correlated with average precision. The mixture improves performance in some cases and degrades it in others, with the degradations possibly due to training techniques, model strength, and poor performance of the individual experts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VogtCBB96.bib) "
	```
	@inproceedings{DBLP:conf/trec/VogtCBB96,
		author = {Christopher C. Vogt and Garrison W. Cottrell and Richard K. Belew and Brian T. Bartell},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Relevance to Train a Linear Mixture of Experts},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/ucsd.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VogtCBB96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

