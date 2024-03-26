# Proceedings 1996 

## Overview of the Fifth Text REtrieval Conference (TREC-5)

_Ellen M. Voorhees, Donna Harman_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/overview.ps.gz](http://trec.nist.gov/pubs/trec5/papers/overview.ps.gz)
??? abstract "Abstract"
	
	The fifth Text REtrieval Conference (TREC-5) was held at the National Institute of Standards and Technology (NIST) on November 20-22, 1996. The conference was co-sponsored by NIST and the Information Technology Office of the Defense Advanced Research Projects Agency (DARPA) as part of the TIPSTER Text Program. TREC-5 is the latest in a series of workshops designed to foster research in text retrieval. For analyses of the results of previous workshops, see Sparck Jones 21, Tague-Sutcliffe and Blustein 23, and Har-man [8]. In addition, the overview paper in each of the previous TREC proceedings summarizes the results of that TREC. The TREC workshop series has the following goals: • to encourage research in text retrieval based on large test collections; • to increase communication among industry, academia, and government by creating an open forum for the exchange of research ideas; • to speed the transfer of technology from research labs into commercial products by demonstrating substantial improvements in retrieval methodologies on real-world problems; and • to increase the availability of appropriate evaluation techniques for use by industry and academia, including development of new evaluation techniques more applicable to current sys-tems. Table 1 lists the groups that participated in TREC-5. Thirty-eight groups including participants from nine different countries and ten companies were represented. The diversity of the participating groups has ensured that TREC represents many different approaches to text retrieval. The emphasis on individual experiments evaluated within a common setting has proven to be a major strength of TREC. This paper serves as an introduction to the research described in detail in the remainder of the volume. The next section defines the common retrieval tasks performed in TREC-5. Sections 3 and 4 provide details regarding the test collections and the evaluation methodology used in TREC. Section 5 provides an overview of the retrieval results. The final section summarizes the main themes learned from the exper-iments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VoorheesH96.bib)"
	```
	@inproceedings{DBLP:conf/trec/VoorheesH96,
		author = {Ellen M. Voorhees and Donna Harman},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of the Fifth Text REtrieval Conference {(TREC-5)}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/overview.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VoorheesH96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Adhoc 

#### INQUERY at TREC-5

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, John Broglio, Jinxi Xu, Hongming Shu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./adhoc/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz](http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz)
- :material-file-search: **Runs:** [INQ301](./adhoc/runs.md#inq301) | [INQ302](./adhoc/runs.md#inq302)

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

- :fontawesome-solid-user-group: **Participant:** [ETH](./adhoc/participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/ETHatTREC5.final.USLetter.ps.gz](http://trec.nist.gov/pubs/trec5/papers/ETHatTREC5.final.USLetter.ps.gz)
- :material-file-search: **Runs:** [ETHas1](./adhoc/runs.md#ethas1) | [ETHal1](./adhoc/runs.md#ethal1) | [ETHme1](./adhoc/runs.md#ethme1)

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

- :fontawesome-solid-user-group: **Participant:** [IRIT](./adhoc/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/irit.ps.gz](http://trec.nist.gov/pubs/trec5/papers/irit.ps.gz)
- :material-file-search: **Runs:** [Mercure-as](./adhoc/runs.md#mercure-as) | [Mercure-al](./adhoc/runs.md#mercure-al)

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

- :fontawesome-solid-user-group: **Participant:** [Cornell](./adhoc/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz](http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz)
- :material-file-search: **Runs:** [Cor5A1se](./adhoc/runs.md#cor5a1se) | [Cor5A2cr](./adhoc/runs.md#cor5a2cr) | [Cor5M1le](./adhoc/runs.md#cor5m1le) | [Cor5M2rf](./adhoc/runs.md#cor5m2rf)

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

#### TREC-5 Ad Hoc Retrieval Using K Nearest-Neighbors Re-Scoring

_Ernest P. Chan, Santiago Garcia, Salim Roukos_

- :fontawesome-solid-user-group: **Participant:** [IBM-S](./adhoc/participants.md#ibm-s)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/ibmt5a.ps.gz](http://trec.nist.gov/pubs/trec5/papers/ibmt5a.ps.gz)
- :material-file-search: **Runs:** [ibms96a](./adhoc/runs.md#ibms96a) | [ibms96b](./adhoc/runs.md#ibms96b)

??? abstract "Abstract"
	
	In our first participation in TREC, we focus on improving on baseline results obtained from another search engine by means of automatic query expansion. We call the specific formula we used for query 'expansion Knn re-scoring' where 'Knn' stands for 'K nearest-neighbors'. The first-pass ranking is done using Okapi system's basic scoring formula|1]. The documents are then rescored using the same formula with the top-ranked K documents as queries, weighted according to their first-pass scores. As we shall see in Sec. 5 below, the formula is motivated by viewing the rescoring process as a Markov process. This approach improves the precision substantially outside the topK retrieved documents. We have tested a variety of other techniques in trying to improving the system. These include word-sense disambiguation, passage retrieval, and document length suppression. Although they do not yield substantial or consistent improvements, some insights into search techniques can nevertheless be extracted. Our experiments are done using the short version of the ad-hoc TREC-5 queries with just the description field retained. The offical entry is submitted as ibms96a. For comparison purposes, performance on TREC-4 data and other smaller corpora are also reported here.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChanGR96.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChanGR96,
		author = {Ernest P. Chan and Santiago Garcia and Salim Roukos},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-5} Ad Hoc Retrieval Using {K} Nearest-Neighbors Re-Scoring},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/ibmt5a.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChanGR96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Substring Retrieval (MultiText Experiments for TREC-5)

_Charles L. A. Clarke, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./adhoc/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/waterloo.ps.gz](http://trec.nist.gov/pubs/trec5/papers/waterloo.ps.gz)
- :material-file-search: **Runs:** [uwgcx0](./adhoc/runs.md#uwgcx0) | [uwgcx1](./adhoc/runs.md#uwgcx1)

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

#### Experiments with TREC using the Open Text Livelink Engine

_Larry Fitzpatrick, Mei Dent, Gary Promhouse_

- :fontawesome-solid-user-group: **Participant:** [OpenText](./adhoc/participants.md#opentext)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/opentext_final_paper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/opentext_final_paper.ps.gz)
- :material-file-search: **Runs:** [colm1](./adhoc/runs.md#colm1) | [colm4](./adhoc/runs.md#colm4)

??? abstract "Abstract"
	
	In TREC-5 we baselined the Open Text Livelink Search Engine 6.1 and tested the use of a new automatic feedback technique against both the baseline and automatic top-document feedback. Baseline queries were created in a manner consistent with real users: small queries average 5 word), created without benefit of query execu-tion, manual feedback or external sources. The interesting results were that other similar queries used as a source of new evidence for automatic query augmentation (feed-forward returned a 38% average precision improvement over the baseline, a 12% average precision improvement over automatic top-document feedback, a 6% improvement in top-document feedback (at the 5 and 10 document levels), and was amenable to thresholding for optimal application of the technique. Automatic top-document feedback yielded nominal improvements and hurt top-document preci-sion, which is consistent with the litera-ture. Attempts to use the embedded document structure to improve search results showed no improvements, despite subjective judgments in other domains that this can be worthwhile.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FitzpatrickDP96.bib) "
	```
	@inproceedings{DBLP:conf/trec/FitzpatrickDP96,
		author = {Larry Fitzpatrick and Mei Dent and Gary Promhouse},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments with {TREC} using the Open Text Livelink Engine},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/opentext\_final\_paper.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FitzpatrickDP96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Corpus Analysis for TREC 5 Query Expansion

_Susan Gauch, Jianying Wang_

- :fontawesome-solid-user-group: **Participant:** [UKans](./adhoc/participants.md#ukans)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/KUSG.ps.gz](http://trec.nist.gov/pubs/trec5/papers/KUSG.ps.gz)
- :material-file-search: **Runs:** [KUSG2](./adhoc/runs.md#kusg2) | [KUSG3](./adhoc/runs.md#kusg3)

??? abstract "Abstract"
	
	Accessing online information remains an inexact science. While valuable information can be found, typically many irrelevant documents are also retrieved and many relevant ones are missed. Terminology mismatches between the user's query and document contents is a main cause of retrieval failures. Expanding a user's query with related words can improve search performance, but the problem of identifying related words remains. This research uses corpus linguistics techniques to automatically discover word similarities directly from the contents of the untagged TREC database and to incorporates that information in the SMART information retrieval system. The similarities are calculated based on the contexts in which a set of target words appear. Using these similarities, user queries are automatically expanded, resulting in conceptual retrieval rather than requiring exact word matches between queries and documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GauchW96.bib) "
	```
	@inproceedings{DBLP:conf/trec/GauchW96,
		author = {Susan Gauch and Jianying Wang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Corpus Analysis for {TREC} 5 Query Expansion},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/KUSG.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GauchW96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Term importance, Boolean conjunct training, negative terms, and foreign  language retrieval: probabilistic algorithms at TREC-5

_Fredric C. Gey, Aitao Chen, Jianzhang He, Liangjie Xu, Jason Meggs_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./adhoc/participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz](http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz)
- :material-file-search: **Runs:** [brkly15](./adhoc/runs.md#brkly15) | [brkly16](./adhoc/runs.md#brkly16) | [brkly17](./adhoc/runs.md#brkly17) | [brkly18](./adhoc/runs.md#brkly18)

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

#### Using Relevance Feedback within the Relational Model for TREC-5

_David A. Grossman, Carol Lundquist, John Reichart, David O. Holmes, Abdur Chowdhury, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [GMU](./adhoc/participants.md#gmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz)
- :material-file-search: **Runs:** [gmu96au2](./adhoc/runs.md#gmu96au2) | [gmu96au1](./adhoc/runs.md#gmu96au1) | [gmu96ma1](./adhoc/runs.md#gmu96ma1) | [gmu96ma2](./adhoc/runs.md#gmu96ma2)

??? abstract "Abstract"
	
	For TREC-5, we enhanced our existing prototype that implements relevance ranking using the AT&T DBC-1012 Model 4 parallel database machine to include relevance feedback. We identified SQL to compute relevance feedback and ran several experiments to identify good cutoffs for the number of documents that should be assumed to be relevant and the number of terms to add to a query. We also tried to find an optimal weighting scheme such that terms added by relevance feedback are weighted differently from those in the original query. We implemented relevance feedback in our special purpose IR prototype. Additionally, we used relevance feedback as a part of our submissions for English, Spanish, Chinese and corrupted data. Finally, we were a participant in the large data track as well. We used a text merging approach whereby a single Pentium processor was able to implement adhoc retrieval on a 4GB text collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanLRHCF96.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanLRHCF96,
		author = {David A. Grossman and Carol Lundquist and John Reichart and David O. Holmes and Abdur Chowdhury and Ophir Frieder},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Relevance Feedback within the Relational Model for {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanLRHCF96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi at TREC-5

_Micheline Hancock-Beaulieu, Mike Gatford, Xiangji Huang, Stephen E. Robertson, Steve Walker, P. W. Williams_

- :fontawesome-solid-user-group: **Participant:** [City](./adhoc/participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz)
- :material-file-search: **Runs:** [city96a1](./adhoc/runs.md#city96a1) | [city96a2](./adhoc/runs.md#city96a2)

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

#### ANU/ACSys TREC-5 Experiments

_David Hawking, Paul B. Thistlewaite, Peter Bailey_

- :fontawesome-solid-user-group: **Participant:** [ANU](./adhoc/participants.md#anu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/anu_t5_paper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/anu_t5_paper.ps.gz)
- :material-file-search: **Runs:** [anu5man4](./adhoc/runs.md#anu5man4) | [anu5man6](./adhoc/runs.md#anu5man6) | [anu5aut1](./adhoc/runs.md#anu5aut1) | [anu5aut2](./adhoc/runs.md#anu5aut2)

??? abstract "Abstract"
	
	A number of experiments conducted within the framework of the TREC-5 conference and using the Parallel Document Retrieval Engine (PADRE) are reported. Several of the experiments involve the use of distance-based relevance scoring (spans). This scoring method is shown to be capable of very good precision-recall performance, provided that good queries can be generated. Semi-automatic methods for refining manually-generated span queries are described and evaluated in the context of the adhoc retrieval task. Span queries are also applied to processing a larger (4.5 gigabyte) collection, to retrieval over OCR-corrupted data and to a database merging task. Lightweight probe queries are shown to be an effective method for identifying promising information servers in the context of the latter task. New techniques for automatically generating more conventional weighted-term queries from short topic descriptions have also been devised and are evaluated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingTB96.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingTB96,
		author = {David Hawking and Paul B. Thistlewaite and Peter Bailey},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ANU/ACSys {TREC-5} Experiments},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/anu\_t5\_paper.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HawkingTB96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Bayesian Networks as Retrieval Engines

_Maria Indrawan, Desra Ghazfan, Bala Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [Monash](./adhoc/participants.md#monash)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/monash.ps.gz](http://trec.nist.gov/pubs/trec5/papers/monash.ps.gz)
- :material-file-search: **Runs:** [MONASH](./adhoc/runs.md#monash)

??? abstract "Abstract"
	
	In this paper we discuss Bayesian network implementation for retrieving documents in a text database. We participate in TREC-5 for ad-hoc task in category B. Several problems and possible solutions in implementing large scale text retrieval system using Bayesian network are discussed The main problems are the existence of loop and large number of parents per-node. The solutions suggested are that of intelligence node and virtual layer. Comparison with other Bayesian approach to text retrieval is also discussed. We shows that our approach gives more correct semantic to the retrieval model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/IndrawanGS96.bib) "
	```
	@inproceedings{DBLP:conf/trec/IndrawanGS96,
		author = {Maria Indrawan and Desra Ghazfan and Bala Srinivasan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Bayesian Networks as Retrieval Engines},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/monash.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/IndrawanGS96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLARIT Compound Queries and Constraint-Controlled Feedback in TREC-5  Ad-Hoc Experiments

_Natasa Milic-Frayling, David A. Evans, Xiang Tong, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [CLARITECH](./adhoc/participants.md#claritech)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec5/t5_proceedings.html](https://trec.nist.gov/pubs/trec5/t5_proceedings.html)
- :material-file-search: **Runs:** [CLTHES](./adhoc/runs.md#clthes) | [CLCLUS](./adhoc/runs.md#clclus)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Milic-FraylingETZ96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Milic-FraylingETZ96,
		author = {Natasa Milic{-}Frayling and David A. Evans and Xiang Tong and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CLARIT} Compound Queries and Constraint-Controlled Feedback in {TREC-5} Ad-Hoc Experiments},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {https://trec.nist.gov/pubs/trec5/t5_proceedings.html},
		timestamp = {Tue, 13 Mar 2018 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Milic-FraylingETZ96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ad Hoc Experiments Using EUREKA

_X. Allan Lu, Maen Ayoub, Jianhua Dong_

- :fontawesome-solid-user-group: **Participant:** [Lexis-Nexis](./adhoc/participants.md#lexis-nexis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/lexis.ps.gz](http://trec.nist.gov/pubs/trec5/papers/lexis.ps.gz)
- :material-file-search: **Runs:** [LNaDesc1](./adhoc/runs.md#lnadesc1) | [LNaDesc2](./adhoc/runs.md#lnadesc2) | [LNmFull1](./adhoc/runs.md#lnmfull1) | [LNmFull2](./adhoc/runs.md#lnmfull2)

??? abstract "Abstract"
	
	Our research for TREC5 focused on search and retrieval of full-text documents with short natural language (NL) queries. It has been our strong belief that the queries submitted to any operational retrieval system, especially those on the Internet, are short or very short, and that an effective approach to processing short NL queries has great application poten-tial. We also looked at data fusion [1] with the assumption that a number of well-devel-oped and specialized retrieval functions would probably outperform a single well-developed but general function. For example, two functions, one specialized in retrieving medium to long documents and another short to medium documents, would deliver better performance if they could be combined properly. Finally, we investigated the problem of selecting documents for relevance feedback. Unhappy with the assumption that all of the top 20 retrieved documents, for example, are relevant and ready for a relevance feedback process, we revisited the cluster hypothesis [2] and experimented with clustering the top 20 documents and automatically selecting a subset for relevance feedback. Our research system named EUREKA (End User Research Enquiry and Knowledge Acquisition) was used for carrying out the experiments. EUREKA consists of a rich set of UNIX tools which can be assembled into various automatic indexing and ranking/filtering mechanisms, either as a new retrieval system or as a simulation of an interesting research system. The tool set design provides a maximum level of flexibility. The remaining document is organized as follows: Section 2 describes a strategy for processing short NL queries and reports experiment results. Section 3 describes a strategy for data fusion and presents related experimental results. Section 4 describes a selective relevance feedback process and discusses related experimental results. Note that every experiment reported in these sections used the TREC4 ad hoc data and queries--our training materials for preparing for TREC5. Section 5 summarizes the training work. And finally, Section 6 comments on our TREC5 results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuAD96.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuAD96,
		author = {X. Allan Lu and Maen Ayoub and Jianhua Dong},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Ad Hoc Experiments Using {EUREKA}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/lexis.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuAD96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-5 Experiments at Dublin City University: Query Space Reduction,  Spanish & Character Shape Encoding

_Fergus Kelledy, Alan F. Smeaton_

- :fontawesome-solid-user-group: **Participant:** [Dublin](./adhoc/participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/dcu_trk5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/dcu_trk5.ps.gz)
- :material-file-search: **Runs:** [DCU961](./adhoc/runs.md#dcu961) | [DCU962](./adhoc/runs.md#dcu962) | [DCU963](./adhoc/runs.md#dcu963) | [DCU964](./adhoc/runs.md#dcu964) | [DCU969](./adhoc/runs.md#dcu969) | [DCU96A](./adhoc/runs.md#dcu96a) | [DCU96B](./adhoc/runs.md#dcu96b) | [DCU96C](./adhoc/runs.md#dcu96c) | [DCU96D](./adhoc/runs.md#dcu96d) | [DCU968](./adhoc/runs.md#dcu968)

??? abstract "Abstract"
	
	In this paper we describe work done as part of the TREC-5 benchmarking exercise by a team from Dublin City University. In TREC-5 we had three activities as follows: Our ad hoc submissions employ Query Space Reduction techniques which attempt to minimise the amount of data processed by an IR search engine during the retrieval process. We submitted four runs for evaluation, two automatic and two manual with one automatic run and one manual run employing our Query Space Reduction techniques. The paper reports our findings in terms of retrieval effectiveness and also in terms of the savings we make in execution time. Our submission to the multi-lingual track (Spanish) in TREC-5 involves evaluating the performance of a new stemming algorithm for Spanish developed by Martin Porter. We submitted three runs for evaluation, two automatic, and one manual, involving a manual expansion from retrieved documents. Character shape coding (CSC) is a technique for representing scanned text using a much reduced alphabet. It has been developed by Larry Spitz of Daimler Benz as an alternative to full-scale OCR for paper documents. Some of our TREC-5 experiments have started evaluating the performance of a CSC representation of scanned documents for information retrieval and this paper outlines our future work in this area
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KelledyS96.bib) "
	```
	@inproceedings{DBLP:conf/trec/KelledyS96,
		author = {Fergus Kelledy and Alan F. Smeaton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-5} Experiments at Dublin City University: Query Space Reduction, Spanish {\&} Character Shape Encoding},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/dcu\_trk5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KelledyS96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-5 English and Chinese Retrieval Experiments using PIRCS

_K. L. Kwok, Laszlo Grunfeld_

- :fontawesome-solid-user-group: **Participant:** [CUNY](./adhoc/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz](http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz)
- :material-file-search: **Runs:** [pircsAAS](./adhoc/runs.md#pircsaas) | [pircsAAL](./adhoc/runs.md#pircsaal) | [pircsAM1](./adhoc/runs.md#pircsam1) | [pircsAM2](./adhoc/runs.md#pircsam2)

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

#### Parallel Techniques For Efficient Searching Over Very Large Text Collections

_Basilis Mamalis, Paul G. Spirakis, Basil Tampakas_

- :fontawesome-solid-user-group: **Participant:** [CTI-GR](./adhoc/participants.md#cti-gr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/Ctifr.ps.gz](http://trec.nist.gov/pubs/trec5/papers/Ctifr.ps.gz)
- :material-file-search: **Runs:** [Ctifr1](./adhoc/runs.md#ctifr1) | [Ctifr2](./adhoc/runs.md#ctifr2)

??? abstract "Abstract"
	
	This paper mainly discusses the efficiency of PFIRE sys-tem, a parallel VSM-based text retrieval system running on the GCel3/512 Parsytec machine, as well as the effectiveness of the corresponding pre-existing serial FIRE system. Concerning PFIRE, the use of suitable data sharing and load balancing techniques in combination with specific pipelining techniques and with the capability of building binary and fat-tree virtual topologies over the 2-D mesh physical interconnection network of the parallel machine, leads to very fast interactive searching over the large scale TREC collections. Analytical and experimental evidence is presented to demonstrate the efficiency of our techniques. The corresponding conventional FIRE system was also used to measure the effectiveness (in terms of recall and precission) of several IR techniques (statistical phrase indexing, automatic statistical global thesaurus construction etc.) used over the TREC WSJ subcollection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MamalisST96.bib) "
	```
	@inproceedings{DBLP:conf/trec/MamalisST96,
		author = {Basilis Mamalis and Paul G. Spirakis and Basil Tampakas},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Parallel Techniques For Efficient Searching Over Very Large Text Collections},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/Ctifr.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MamalisST96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The GURU System in TREC-5

_Yael Ravin_

- :fontawesome-solid-user-group: **Participant:** [IBM-S](./adhoc/participants.md#ibm-s)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/ibm_trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/ibm_trec5.ps.gz)
- :material-file-search: **Runs:** [ibms96a](./adhoc/runs.md#ibms96a) | [ibms96b](./adhoc/runs.md#ibms96b)

??? abstract "Abstract"
	
	In our first participation in TREC, we focus on improving on baseline results obtained from another search engine by means of automatic query expansion. We call the specific formula we used for query 'expansion Knn re-scoring' where 'Knn' stands for 'K nearest-neighbors'. The first-pass ranking is done using Okapi system's basic scoring formula|1]. The documents are then rescored using the same formula with the top-ranked K documents as queries, weighted according to their first-pass scores. As we shall see in Sec. 5 below, the formula is motivated by viewing the rescoring process as a Markov process. This approach improves the precision substantially outside the topK retrieved documents. We have tested a variety of other techniques in trying to improving the system. These include word-sense disambiguation, passage retrieval, and document length suppression. Although they do not yield substantial or consistent improvements, some insights into search techniques can nevertheless be extracted. Our experiments are done using the short version of the ad-hoc TREC-5 queries with just the description field retained. The offical entry is submitted as ibms96a. For comparison purposes, performance on TREC-4 data and other smaller corpora are also reported here.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Ravin96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Ravin96,
		author = {Yael Ravin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {GURU} System in {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/ibm\_trec5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Ravin96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### V-Twin: A Lightweight Engine for Interactive Use

_Daniel E. Rose, Curt Stevens_

- :fontawesome-solid-user-group: **Participant:** [Apple](./adhoc/participants.md#apple)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/apple.ps.gz](http://trec.nist.gov/pubs/trec5/papers/apple.ps.gz)
- :material-file-search: **Runs:** [vtwnA1](./adhoc/runs.md#vtwna1) | [vtwnB1](./adhoc/runs.md#vtwnb1)

??? abstract "Abstract"
	
	This paper describes V-Twin, an information access toolkit designed to provide indexing and search capabilities for a variety of applications. We discuss the phenomenon of very short queries generated by users of interactive search services, and summarize a new technique we are using in V-Twin to handle these queries more effectively. We then present some results based on V-Twin's performance at the TREC-5 ad hoc task. V-Twin achieved a high level of performance despite having much lower index overhead and memory footprint than other systems participating in TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoseS96.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoseS96,
		author = {Daniel E. Rose and Curt Stevens},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {V-Twin: {A} Lightweight Engine for Interactive Use},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/apple.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoseS96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the Glasgow IR group (glair4) submission

_Mark Sanderson, Ian Ruthven_

- :fontawesome-solid-user-group: **Participant:** [Glasgow](./adhoc/participants.md#glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/glasgow.new.ps.gz](http://trec.nist.gov/pubs/trec5/papers/glasgow.new.ps.gz)
- :material-file-search: **Runs:** [glair4](./adhoc/runs.md#glair4)

??? abstract "Abstract"
	
	This year's submission from the Glasgow IR group (glair4) is to the category B automatic ad hoc section. Due to pressures of time and unexpected complications, our intended application of a technique known as generalised imaging [Crestani 95] was not completed in time for the TREC deadline. Therefore, the submission is the output of an IR system running a simplistic retrieval strategy, similar to last year's submission though with some intended improvements. It would appear from comparison with other category B submissions that this strategy is relatively successful. The following sections of this report contain a description of the retrieval strategy used, a analysis of the results, and finally, a discussion of our intentions for TREC 6.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SandersonR96.bib) "
	```
	@inproceedings{DBLP:conf/trec/SandersonR96,
		author = {Mark Sanderson and Ian Ruthven},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Report on the Glasgow {IR} group (glair4) submission},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/glasgow.new.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SandersonR96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC-5 Experiment: Data Fusion and Collection Fusion

_Jacques Savoy, Anne Le Calvé, Dana Vrajitoru_

- :fontawesome-solid-user-group: **Participant:** [Neuchatel](./adhoc/participants.md#neuchatel)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec5/t5_proceedings.html](https://trec.nist.gov/pubs/trec5/t5_proceedings.html)
- :material-file-search: **Runs:** [UniNE8](./adhoc/runs.md#unine8) | [UniNE7](./adhoc/runs.md#unine7)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavoyCV96.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavoyCV96,
		author = {Jacques Savoy and Anne Le Calv{\'{e}} and Dana Vrajitoru},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Report on the {TREC-5} Experiment: Data Fusion and Collection Fusion},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {https://trec.nist.gov/pubs/trec5/t5_proceedings.html},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SavoyCV96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Document Retrieval Using The MPS Information Server (A Report  on the TREC-5 Experiment)

_François Schiettecatte_

- :fontawesome-solid-user-group: **Participant:** [FS Consulting](./adhoc/participants.md#fs consulting)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/fsconsult.ps.gz](http://trec.nist.gov/pubs/trec5/papers/fsconsult.ps.gz)
- :material-file-search: **Runs:** [fsclt3](./adhoc/runs.md#fsclt3) | [fsclt4](./adhoc/runs.md#fsclt4)

??? abstract "Abstract"
	
	This paper summarizes the results of the experiments conducted by FS Consulting, Inc. as part of the Fifth Text Retrieval Experiment Conference (TREC-5). We participated in Category C, ran the ad-hoc experiments and participated in the database merging track, producing three sets of official results (fsclt, fsclt and fsclt3m) as well as some unofficial results (fsclta). Our long-term research interest is in building information retrieval systems that help users find information to solve real-world problems. Our TREC-5 participation centered on two goals: to see if automatic query reformulation (relevance feedback) provides better results than the searcher's query reformulation; and to evaluate the effectiveness of the document scoring algorithms when searching across multiple databases. Our TREC-5 ad-hoc experiments were designed around a model of an experienced end user of information systems, one who might regularly use a system like the MPS Information Server while seeking information in a workplace or library setting
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Schiettecatte96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Schiettecatte96,
		author = {Fran{\c{c}}ois Schiettecatte},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Document Retrieval Using The {MPS} Information Server {(A} Report on the {TREC-5} Experiment)},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/fsconsult.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Schiettecatte96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Natural Language Information Retrieval: TREC-5 Report

_Tomek Strzalkowski, Louise Guthrie, Jussi Karlgren, Jim Leistensnider, Fang Lin, Jose Perez Carballo, Troy Straszheim, Jing Wang, Jon Wilding_

- :fontawesome-solid-user-group: **Participant:** [GE-NYU](./adhoc/participants.md#ge-nyu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/ge.ps.gz](http://trec.nist.gov/pubs/trec5/papers/ge.ps.gz)
- :material-file-search: **Runs:** [genrl1](./adhoc/runs.md#genrl1) | [genrl2](./adhoc/runs.md#genrl2) | [genrl3](./adhoc/runs.md#genrl3) | [genrl4](./adhoc/runs.md#genrl4)

??? abstract "Abstract"
	
	In this paper we report on the joint GE/Lockheed Martin/Rutgers/NYU natural language information retrieval project as related to the 5th Text Retrieval Conference (TREC-5). The main thrust of this project is to use natural language processing techniques to enhance the effectiveness of full-text document retrieval. Since our first TREC entry in 1992 (as NYU team) the basic premise of our research was to demonstrate that robust if relatively shallow NLP can help to derive a better representation of text documents for statistical search. TREC-5 marks a shift in this approach away from text representation issues and towards query development problems. While our TREC-5 system still performs extensive text processing in order to extract phrasal and other indexing terms, our main focus this year was on query construction using words, sentences, and entire passages to expand initial topic specifications in an attempt to cover their various angles, aspects and contexts. Based on our earlier TREC results indicating that NLP is more effective when long, descriptive queries are used, we allowed for liberal expansion with long passages from related documents imported verbatim into the queries. This method appears to have produced a dramatic improvement in the performance of two different statistical search engines that we tested (Cornell's SMART and NIST's Prise) boosting the average precision by at least 40%. The overall architecture of TREC-5 system has also changed in a number of ways from TREC-4. The most notable new feature is the stream architecture in which several independent, parallel indexes are built for a given collection, each index reflecting a different representation strategy for text documents. Stream indexes are built using a mixture of different indexing approaches, term extracting, and weighting strategies. We used both SMART and Prise base indexing engines, and selected optimal term weighting strategies for each stream, based on a training collection of approximately 500 MBytes. The final results are produced by a merging procedure that combines ranked list of documents obtained by searching all stream indexes with appropriately preprocessed queries. This allows for an effective combination of alternative retrieval and filtering methods, creating into a meta-search where the contribution of each stream can be optimized through training.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StrzalkowskiGKLLCSWW96.bib) "
	```
	@inproceedings{DBLP:conf/trec/StrzalkowskiGKLLCSWW96,
		author = {Tomek Strzalkowski and Louise Guthrie and Jussi Karlgren and Jim Leistensnider and Fang Lin and Jose Perez Carballo and Troy Straszheim and Jing Wang and Jon Wilding},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Natural Language Information Retrieval: {TREC-5} Report},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/ge.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StrzalkowskiGKLLCSWW96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Investigation of Relevance Feedback Using Adaptive Linear and Probabilistic  Models

_Robert G. Sumner Jr., William M. Shaw Jr._

- :fontawesome-solid-user-group: **Participant:** [UNC](./adhoc/participants.md#unc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/unc_trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/unc_trec5.ps.gz)
- :material-file-search: **Runs:** [uncis1](./adhoc/runs.md#uncis1) | [uncis2](./adhoc/runs.md#uncis2)

??? abstract "Abstract"
	
	The SMART system (v. 11.0) was used as a front-end to a two-stage retrieval process. In the first stage, (WSJ documents and the description field of (ad hoc) topics were indexed by the stems of single terms; Inc and It weights were computed for word stems in documents and queries, respectively; and documents were ranked according to the cosine similarity of document and query vectors. Related by the initial query vector, the first 5000 documents in the ranked list for each topic constituted a 'condensed' database for that topic. Preliminary experiments with TREC-4 topics and official relevance evaluations suggested each such database would include a high fraction of relevant documents for the associated topic, and the result was confirmed by TREC-S results. In the second stage, initial query vectors were automatically refined by two relevance feedback strategies applied to the condensed databases. One of us employed the adaptive linear model (uncis/), and the other used a variation of the 'classic' probabilistic model (uncis2); relevance judgments were made independently. In uncisi, the query at a given search iteration is expanded by all terms in relevant, retrieved documents and all terms in selected, nonrelevant, retrieved documents, and documents are ranked by the inner product of document and query vectors. In uncis2, the query is expanded by all terms in relevant, retrieved documents, and documents are ranked by the cosine similarity of document and query vectors. For uncisI and uncis2, respectively, average non-interpolated precision values over all relevant documents are 0.25 and 0.20, and average R-precision values are 0.25 and 0.21. Results show that independent relevance judgments made in uncis and uncis are quite different and have a strong effect on retrieval outcomes; our relevance evaluations also differ significantly from official relevance judgments. Retrieval performance improves when official relevance judgments are utilized by both models. For the 31 topics in which there was an official relevant document in the top 34 of the initial ranking, average non-interpolated precision values are 0.60 for the adaptive linear model and 0.59 for the probabilistic model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SumnerS96.bib) "
	```
	@inproceedings{DBLP:conf/trec/SumnerS96,
		author = {Robert G. Sumner Jr. and William M. Shaw Jr.},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {An Investigation of Relevance Feedback Using Adaptive Linear and Probabilistic Models},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/unc\_trec5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SumnerS96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Relevance to Train a Linear Mixture of Experts

_Christopher C. Vogt, Garrison W. Cottrell, Richard K. Belew, Brian T. Bartell_

- :fontawesome-solid-user-group: **Participant:** [UCSD](./adhoc/participants.md#ucsd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/ucsd.ps.gz](http://trec.nist.gov/pubs/trec5/papers/ucsd.ps.gz)
- :material-file-search: **Runs:** [sdmix2](./adhoc/runs.md#sdmix2) | [sdmix1](./adhoc/runs.md#sdmix1)

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

#### The MDS Experiments for TREC5

_Marcin Kaszkiel, Phil Vines, Ross Wilkinson, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [CITRI](./adhoc/participants.md#citri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/rmit.ps.gz](http://trec.nist.gov/pubs/trec5/papers/rmit.ps.gz)
- :material-file-search: **Runs:** [mds001](./adhoc/runs.md#mds001) | [mds002](./adhoc/runs.md#mds002) | [mds003](./adhoc/runs.md#mds003)

??? abstract "Abstract"
	
	The Multimedia Database Systems (MDS) group at RMIT is investigating many aspects of information retrieval of relevance to TREC. Current work includes combination of evidence, Asian-language text retrieval, passage retrieval, collection fusion, and efficient retrieval from large collections. Here we report on results from three of these strands of research.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KaszkielVWZ96.bib) "
	```
	@inproceedings{DBLP:conf/trec/KaszkielVWZ96,
		author = {Marcin Kaszkiel and Phil Vines and Ross Wilkinson and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {MDS} Experiments for {TREC5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/rmit.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KaszkielVWZ96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Database Merging 

#### The TREC-5 Database Merging Track

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/dbmerge_track.ps.gz](http://trec.nist.gov/pubs/trec5/papers/dbmerge_track.ps.gz)
??? abstract "Abstract"
	
	There are many times when users want to search separate text collections as if they were a single collection. For example, computer networks can provide access to a variety of corpora that are owned and maintained by different entities. Instead of issuing search commands to each of the databases in turn and manually collating the individual results, users prefer a mechanism for performing a single, integrated search. In other cases, reliability and efficiency concerns may dictate that databases that are under the same administrative control should be physically separate. Again, users want to issue a single search request that returns an integrated result. The database merging track investigates methods for combining the results of separate searches into a single, cohesive result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees96,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-5} Database Merging Track},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/dbmerge\_track.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ANU/ACSys TREC-5 Experiments

_David Hawking, Paul B. Thistlewaite, Peter Bailey_

- :fontawesome-solid-user-group: **Participant:** [ANU](./dbmerge/participants.md#anu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/anu_t5_paper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/anu_t5_paper.ps.gz)
- :material-file-search: **Runs:** [anu5mrg0](./dbmerge/runs.md#anu5mrg0) | [anu5mrg1](./dbmerge/runs.md#anu5mrg1) | [anu5mrg7](./dbmerge/runs.md#anu5mrg7)

??? abstract "Abstract"
	
	A number of experiments conducted within the framework of the TREC-5 conference and using the Parallel Document Retrieval Engine (PADRE) are reported. Several of the experiments involve the use of distance-based relevance scoring (spans). This scoring method is shown to be capable of very good precision-recall performance, provided that good queries can be generated. Semi-automatic methods for refining manually-generated span queries are described and evaluated in the context of the adhoc retrieval task. Span queries are also applied to processing a larger (4.5 gigabyte) collection, to retrieval over OCR-corrupted data and to a database merging task. Lightweight probe queries are shown to be an effective method for identifying promising information servers in the context of the latter task. New techniques for automatically generating more conventional weighted-term queries from short topic descriptions have also been devised and are evaluated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingTB96.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingTB96,
		author = {David Hawking and Paul B. Thistlewaite and Peter Bailey},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ANU/ACSys {TREC-5} Experiments},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/anu\_t5\_paper.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HawkingTB96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC-5 Experiment: Data Fusion and Collection Fusion

_Jacques Savoy, Anne Le Calvé, Dana Vrajitoru_

- :fontawesome-solid-user-group: **Participant:** [Neuchatel](./dbmerge/participants.md#neuchatel)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec5/t5_proceedings.html](https://trec.nist.gov/pubs/trec5/t5_proceedings.html)
- :material-file-search: **Runs:** [UniNE9](./dbmerge/runs.md#unine9) | [UniNE0](./dbmerge/runs.md#unine0)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavoyCV96.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavoyCV96,
		author = {Jacques Savoy and Anne Le Calv{\'{e}} and Dana Vrajitoru},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Report on the {TREC-5} Experiment: Data Fusion and Collection Fusion},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {https://trec.nist.gov/pubs/trec5/t5_proceedings.html},
		timestamp = {Tue, 07 Apr 2015 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SavoyCV96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Routing 

#### INQUERY at TREC-5

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, John Broglio, Jinxi Xu, Hongming Shu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./routing/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz](http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz)
- :material-file-search: **Runs:** [INQ303](./routing/runs.md#inq303)

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

- :fontawesome-solid-user-group: **Participant:** [ETH](./routing/participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/ETHatTREC5.final.USLetter.ps.gz](http://trec.nist.gov/pubs/trec5/papers/ETHatTREC5.final.USLetter.ps.gz)
- :material-file-search: **Runs:** [ETHru1](./routing/runs.md#ethru1)

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

- :fontawesome-solid-user-group: **Participant:** [IRIT](./routing/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/irit.ps.gz](http://trec.nist.gov/pubs/trec5/papers/irit.ps.gz)
- :material-file-search: **Runs:** [Mercure1](./routing/runs.md#mercure1) | [Mercure2](./routing/runs.md#mercure2)

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

- :fontawesome-solid-user-group: **Participant:** [Cornell](./routing/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz](http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz)
- :material-file-search: **Runs:** [Cor5R1cc](./routing/runs.md#cor5r1cc) | [Cor5R2cr](./routing/runs.md#cor5r2cr)

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

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./routing/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/waterloo.ps.gz](http://trec.nist.gov/pubs/trec5/papers/waterloo.ps.gz)
- :material-file-search: **Runs:** [uwgcr0](./routing/runs.md#uwgcr0)

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

- :fontawesome-solid-user-group: **Participant:** [NMSU-C](./routing/participants.md#nmsu-c)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/nmsu.cowie.ps.gz](http://trec.nist.gov/pubs/trec5/papers/nmsu.cowie.ps.gz)
- :material-file-search: **Runs:** [nmsu-1](./routing/runs.md#nmsu-1)

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

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./routing/participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz](http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz)
- :material-file-search: **Runs:** [brkly13](./routing/runs.md#brkly13) | [brkly14](./routing/runs.md#brkly14)

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

- :fontawesome-solid-user-group: **Participant:** [City](./routing/participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz)
- :material-file-search: **Runs:** [city96r1](./routing/runs.md#city96r1) | [city96r2](./routing/runs.md#city96r2)

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

- :fontawesome-solid-user-group: **Participant:** [Xerox](./routing/participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz](http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz)
- :material-file-search: **Runs:** [xerox.rout1](./routing/runs.md#xerox.rout1) | [xerox.rout2](./routing/runs.md#xerox.rout2) | [xerox.rout3](./routing/runs.md#xerox.rout3)

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

- :fontawesome-solid-user-group: **Participant:** [ITI-SG](./routing/participants.md#iti-sg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/iti.trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/iti.trec5.ps.gz)
- :material-file-search: **Runs:** [itidp1](./routing/runs.md#itidp1) | [itidp2](./routing/runs.md#itidp2)

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

- :fontawesome-solid-user-group: **Participant:** [CUNY](./routing/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz](http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz)
- :material-file-search: **Runs:** [pircsg0](./routing/runs.md#pircsg0) | [pircsg6](./routing/runs.md#pircsg6)

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

- :fontawesome-solid-user-group: **Participant:** [UIUC](./routing/participants.md#uiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/newby-proceedings-final.ps.gz](http://trec.nist.gov/pubs/trec5/papers/newby-proceedings-final.ps.gz)
- :material-file-search: **Runs:** [ispaR](./routing/runs.md#ispar)

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

- :fontawesome-solid-user-group: **Participant:** [RutgersK](./routing/participants.md#rutgersk)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/rutgers.kantor.ps.gz](http://trec.nist.gov/pubs/trec5/papers/rutgers.kantor.ps.gz)
- :material-file-search: **Runs:** [rutAPspt](./routing/runs.md#rutapspt) | [rutAPglob](./routing/runs.md#rutapglob)

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

- :fontawesome-solid-user-group: **Participant:** [UCSD](./routing/participants.md#ucsd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/ucsd.ps.gz](http://trec.nist.gov/pubs/trec5/papers/ucsd.ps.gz)
- :material-file-search: **Runs:** [sdmix3](./routing/runs.md#sdmix3)

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

## Filtering 

#### The TREC-5 Filtering Track

_David D. Lewis_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/filtering.ps.gz](http://trec.nist.gov/pubs/trec5/papers/filtering.ps.gz)
??? abstract "Abstract"
	
	The TREC-5 filtering track, an evaluation of binary text classification systems, was a repeat of the filtering evaluation run in a trial version for TREC-4, with only the data set and participants changing. Seven sites took part, submitting a total of ten runs. We review the nature of the task, the effectiveness measures and evaluation methods used, and briefly discuss the results. Some deficiencies in the evaluation are examined, with an eye toward improving future filtering evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lewis96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lewis96,
		author = {David D. Lewis},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-5} Filtering Track},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/filtering.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lewis96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY at TREC-5

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, John Broglio, Jinxi Xu, Hongming Shu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./filtering/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz](http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz)
- :material-file-search: **Runs:** [INR3-p](./filtering/runs.md#inr3-p) | [INR3-m](./filtering/runs.md#inr3-m) | [INR3-r](./filtering/runs.md#inr3-r)

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

#### Okapi at TREC-5

_Micheline Hancock-Beaulieu, Mike Gatford, Xiangji Huang, Stephen E. Robertson, Steve Walker, P. W. Williams_

- :fontawesome-solid-user-group: **Participant:** [City](./filtering/participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz)
- :material-file-search: **Runs:** [city96f1](./filtering/runs.md#city96f1) | [city96f2](./filtering/runs.md#city96f2) | [city96f3](./filtering/runs.md#city96f3)

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

- :fontawesome-solid-user-group: **Participant:** [Xerox](./filtering/participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz](http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz)
- :material-file-search: **Runs:** [xerox.f1p25](./filtering/runs.md#xerox.f1p25) | [xerox.f1p50](./filtering/runs.md#xerox.f1p50) | [xerox.f1p75](./filtering/runs.md#xerox.f1p75) | [xerox.f2p75](./filtering/runs.md#xerox.f2p75) | [xerox.f2p50](./filtering/runs.md#xerox.f2p50) | [xerox.f2p25](./filtering/runs.md#xerox.f2p25) | [xerox.f3p25](./filtering/runs.md#xerox.f3p25) | [xerox.f3p50](./filtering/runs.md#xerox.f3p50) | [xerox.f3p75](./filtering/runs.md#xerox.f3p75)

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

- :fontawesome-solid-user-group: **Participant:** [ITI-SG](./filtering/participants.md#iti-sg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/iti.trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/iti.trec5.ps.gz)
- :material-file-search: **Runs:** [itift1](./filtering/runs.md#itift1) | [itift2](./filtering/runs.md#itift2) | [itift3](./filtering/runs.md#itift3)

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

#### InTEXT Automatic Query Enhancement in TREC-5

_Richard L. Jones, Mark Burnett, D. Lewis Pape_

- :fontawesome-solid-user-group: **Participant:** [Intext](./filtering/participants.md#intext)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/intext.ps.gz](http://trec.nist.gov/pubs/trec5/papers/intext.ps.gz)
- :material-file-search: **Runs:** [INTXA1](./filtering/runs.md#intxa1) | [INTXA2](./filtering/runs.md#intxa2) | [INTXA3](./filtering/runs.md#intxa3) | [INTXM1](./filtering/runs.md#intxm1) | [INTXM2](./filtering/runs.md#intxm2) | [INTXM3](./filtering/runs.md#intxm3)

??? abstract "Abstract"
	
	InTEXT Systems is a subsidiary of the CP Software Group, whose headquarters are in Folsom, California. InTEXT is a leader in the provision of advanced tools and end-user products that can best be described as doing 'smart things with text'. The InTEXT Research and Development group, based in Canberra Australia, has been in existence for 11 years. We develop leading edge technology in areas including text retrieval, filtering, indexing, summarisation and thematic clustering, using the InTEXT Heuristic Learning Architecture. The InTEXT Systems R and D group has participated in two previous TRECs. We took part in TREC-4 and also in TREC-1, when the team formed the Centre for Electronic Document Research (CEDR), in conjunction with CITRI.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JonesBP96.bib) "
	```
	@inproceedings{DBLP:conf/trec/JonesBP96,
		author = {Richard L. Jones and Mark Burnett and D. Lewis Pape},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {InTEXT Automatic Query Enhancement in {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/intext.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JonesBP96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-5 English and Chinese Retrieval Experiments using PIRCS

_K. L. Kwok, Laszlo Grunfeld_

- :fontawesome-solid-user-group: **Participant:** [CUNY](./filtering/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz](http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz)
- :material-file-search: **Runs:** [pircshp](./filtering/runs.md#pircshp) | [pircsmp](./filtering/runs.md#pircsmp) | [pircslp](./filtering/runs.md#pircslp)

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

- :fontawesome-solid-user-group: **Participant:** [UIUC](./filtering/participants.md#uiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/newby-proceedings-final.ps.gz](http://trec.nist.gov/pubs/trec5/papers/newby-proceedings-final.ps.gz)
- :material-file-search: **Runs:** [ispFA1](./filtering/runs.md#ispfa1) | [ispFB1](./filtering/runs.md#ispfb1) | [ispFC1](./filtering/runs.md#ispfc1)

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

- :fontawesome-solid-user-group: **Participant:** [RutgersK](./filtering/participants.md#rutgersk)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/rutgers.kantor.ps.gz](http://trec.nist.gov/pubs/trec5/papers/rutgers.kantor.ps.gz)

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

## Spanish 

#### Spanish and Chinese Document Retrieval in TREC-5

_Alan F. Smeaton_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/multilingual_track.ps.gz](http://trec.nist.gov/pubs/trec5/papers/multilingual_track.ps.gz)
??? abstract "Abstract"
	
	The TREC-5 conference was the third year in which document retrieval in a language other than English was benchmarked. In TREC-3, 4 groups participated in an ad hoc retrieval task on a collection of 208 Mbytes of Mexican newspaper text in the Spanish language. In TREC-4 there were 10 groups who participated, once again in an ad hoc document retrieval task on the same Mexican newspaper texts but with new topics. In TREC-5 there was a change of document corpus and new topics for the Spanish ad hoc retrieval task and a corpus of documents and topics to support ad hoc retrieval in the Chinese language was introduced for the first time. There were 7 groups who submitted runs for the Spanish track and 10 who submitted results for Chinese. The corpus of texts used in the TREC-5 Spanish language task was approximately the same size as the one used in TREC-3 and TREC-4 but differed in that there was a more consistent use of accented characters and it was European Spanish as opposed to Mexican Spanish. This slightly affected the morphological processing of word forms. In the Chinese language each character represents at least a complete syllable, rather than a letter as in other languages. Many characters are also single syllable words. The total number of characters is therefore quite large and somewhat ill defined. A literate adult would typically recognise at least 5-6,000 characters. The various modern standards define between 10-12,000 characters, although if early and ancient literature is included the number rises to approximately 100,000. Chinese is agglutinating - there is no space between consecutive characters, except perhaps, at the end of a sentence. Thus to perform retrieval in Chinese, the basis has to be characters unless the text is pre-segmented into words.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Smeaton96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Smeaton96,
		author = {Alan F. Smeaton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Spanish and Chinese Document Retrieval in {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/multilingual\_track.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Smeaton96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY at TREC-5

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, John Broglio, Jinxi Xu, Hongming Shu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./Spanish/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz](http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz)
- :material-file-search: **Runs:** [SIN300](./Spanish/runs.md#sin300) | [SIN301](./Spanish/runs.md#sin301)

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

#### Using Query Zoning and Correlation Within SMART: TREC 5

_Chris Buckley, Amit Singhal, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [Cornell](./Spanish/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz](http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz)
- :material-file-search: **Runs:** [Cor5SP1s](./Spanish/runs.md#cor5sp1s) | [Cor5SP2l](./Spanish/runs.md#cor5sp2l)

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

#### New Experiments In Cross-Language Text Retrieval At NMSU's Computing  Research Lab

_Mark W. Davis_

- :fontawesome-solid-user-group: **Participant:** [NMSU-D](./Spanish/participants.md#nmsu-d)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/nmsu.davis.paper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/nmsu.davis.paper.ps.gz)
- :material-file-search: **Runs:** [nmsuc1](./Spanish/runs.md#nmsuc1) | [nmsuc2](./Spanish/runs.md#nmsuc2) | [nmsuc3](./Spanish/runs.md#nmsuc3)

??? abstract "Abstract"
	
	In Cross-Language Text Retrieval, queries in one language retrieve documents in other languages. Query translation is the least expensive approach to the retrieval task when compared to full document translation. The simple combinatorial properties of vector-based text retrieval systems simplify the translation task enormously, reducing most translation to the correct substitution of equivalents from a bilingual lexicon or corpus. New experiments are presented on methods for selecting among potential equivalents from a bilingual lexicon, including one fully-automatic method that achieves 73.5% of the performance of a monolingual system operating on the same retrieval task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Davis96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Davis96,
		author = {Mark W. Davis},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {New Experiments In Cross-Language Text Retrieval At NMSU's Computing Research Lab},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/nmsu.davis.paper.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Davis96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Term importance, Boolean conjunct training, negative terms, and foreign  language retrieval: probabilistic algorithms at TREC-5

_Fredric C. Gey, Aitao Chen, Jianzhang He, Liangjie Xu, Jason Meggs_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./Spanish/participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz](http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz)
- :material-file-search: **Runs:** [BrklySP5](./Spanish/runs.md#brklysp5) | [BrklySP6](./Spanish/runs.md#brklysp6)

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

#### Using Relevance Feedback within the Relational Model for TREC-5

_David A. Grossman, Carol Lundquist, John Reichart, David O. Holmes, Abdur Chowdhury, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [GMU](./Spanish/participants.md#gmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz)
- :material-file-search: **Runs:** [gmu96sp1](./Spanish/runs.md#gmu96sp1) | [gmu96sp2](./Spanish/runs.md#gmu96sp2)

??? abstract "Abstract"
	
	For TREC-5, we enhanced our existing prototype that implements relevance ranking using the AT&T DBC-1012 Model 4 parallel database machine to include relevance feedback. We identified SQL to compute relevance feedback and ran several experiments to identify good cutoffs for the number of documents that should be assumed to be relevant and the number of terms to add to a query. We also tried to find an optimal weighting scheme such that terms added by relevance feedback are weighted differently from those in the original query. We implemented relevance feedback in our special purpose IR prototype. Additionally, we used relevance feedback as a part of our submissions for English, Spanish, Chinese and corrupted data. Finally, we were a participant in the large data track as well. We used a text merging approach whereby a single Pentium processor was able to implement adhoc retrieval on a 4GB text collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanLRHCF96.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanLRHCF96,
		author = {David A. Grossman and Carol Lundquist and John Reichart and David O. Holmes and Abdur Chowdhury and Ophir Frieder},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Relevance Feedback within the Relational Model for {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanLRHCF96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Xerox TREC-5 Site Report: Routing, Filtering, NLP, and Spanish Tracks

_David A. Hull, Gregory Grefenstette, B. Maximilian Schulze, Éric Gaussier, Hinrich Schütze, Jan O. Pedersen_

- :fontawesome-solid-user-group: **Participant:** [Xerox](./Spanish/participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz](http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz)
- :material-file-search: **Runs:** [xerox-spS](./Spanish/runs.md#xerox-sps) | [xerox-spP](./Spanish/runs.md#xerox-spp) | [xerox-spT](./Spanish/runs.md#xerox-spt) | [xerox-spD](./Spanish/runs.md#xerox-spd)

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

#### Alignment of Spanish and English TREC Topic Descriptions

_Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [UMd](./Spanish/participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/umd.ps.gz](http://trec.nist.gov/pubs/trec5/papers/umd.ps.gz)

??? abstract "Abstract"
	
	A technique is described for aligning TREC topic descriptions that is capable of producing a small multilingual test collection which can be used for cross-language ad-hoc and routing evaluations. Methods for measuring the degree of degradation induced by the necessary approximations are described and illustrated using examples from an evaluation of two cross-language routing techniques. Although the experiments were conducted on a relatively small test collection using existing TREC relevance judg-ments, the results suggest that cross-language routing is practical and that the investment required to produce a cross-language test collection for the TREC multilingual track would be justified.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Oard96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Oard96,
		author = {Douglas W. Oard},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Alignment of Spanish and English {TREC} Topic Descriptions},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/umd.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Oard96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-5 Experiments at Dublin City University: Query Space Reduction,  Spanish & Character Shape Encoding

_Fergus Kelledy, Alan F. Smeaton_

- :fontawesome-solid-user-group: **Participant:** [Dublin](./Spanish/participants.md#dublin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/dcu_trk5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/dcu_trk5.ps.gz)
- :material-file-search: **Runs:** [DCU965](./Spanish/runs.md#dcu965) | [DCU966](./Spanish/runs.md#dcu966) | [DCU967](./Spanish/runs.md#dcu967)

??? abstract "Abstract"
	
	In this paper we describe work done as part of the TREC-5 benchmarking exercise by a team from Dublin City University. In TREC-5 we had three activities as follows: Our ad hoc submissions employ Query Space Reduction techniques which attempt to minimise the amount of data processed by an IR search engine during the retrieval process. We submitted four runs for evaluation, two automatic and two manual with one automatic run and one manual run employing our Query Space Reduction techniques. The paper reports our findings in terms of retrieval effectiveness and also in terms of the savings we make in execution time. Our submission to the multi-lingual track (Spanish) in TREC-5 involves evaluating the performance of a new stemming algorithm for Spanish developed by Martin Porter. We submitted three runs for evaluation, two automatic, and one manual, involving a manual expansion from retrieved documents. Character shape coding (CSC) is a technique for representing scanned text using a much reduced alphabet. It has been developed by Larry Spitz of Daimler Benz as an alternative to full-scale OCR for paper documents. Some of our TREC-5 experiments have started evaluating the performance of a CSC representation of scanned documents for information retrieval and this paper outlines our future work in this area
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KelledyS96.bib) "
	```
	@inproceedings{DBLP:conf/trec/KelledyS96,
		author = {Fergus Kelledy and Alan F. Smeaton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-5} Experiments at Dublin City University: Query Space Reduction, Spanish {\&} Character Shape Encoding},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/dcu\_trk5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KelledyS96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Chinese 

#### Spanish and Chinese Document Retrieval in TREC-5

_Alan F. Smeaton_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/multilingual_track.ps.gz](http://trec.nist.gov/pubs/trec5/papers/multilingual_track.ps.gz)
??? abstract "Abstract"
	
	The TREC-5 conference was the third year in which document retrieval in a language other than English was benchmarked. In TREC-3, 4 groups participated in an ad hoc retrieval task on a collection of 208 Mbytes of Mexican newspaper text in the Spanish language. In TREC-4 there were 10 groups who participated, once again in an ad hoc document retrieval task on the same Mexican newspaper texts but with new topics. In TREC-5 there was a change of document corpus and new topics for the Spanish ad hoc retrieval task and a corpus of documents and topics to support ad hoc retrieval in the Chinese language was introduced for the first time. There were 7 groups who submitted runs for the Spanish track and 10 who submitted results for Chinese. The corpus of texts used in the TREC-5 Spanish language task was approximately the same size as the one used in TREC-3 and TREC-4 but differed in that there was a more consistent use of accented characters and it was European Spanish as opposed to Mexican Spanish. This slightly affected the morphological processing of word forms. In the Chinese language each character represents at least a complete syllable, rather than a letter as in other languages. Many characters are also single syllable words. The total number of characters is therefore quite large and somewhat ill defined. A literate adult would typically recognise at least 5-6,000 characters. The various modern standards define between 10-12,000 characters, although if early and ancient literature is included the number rises to approximately 100,000. Chinese is agglutinating - there is no space between consecutive characters, except perhaps, at the end of a sentence. Thus to perform retrieval in Chinese, the basis has to be characters unless the text is pre-segmented into words.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Smeaton96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Smeaton96,
		author = {Alan F. Smeaton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Spanish and Chinese Document Retrieval in {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/multilingual\_track.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Smeaton96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY at TREC-5

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, John Broglio, Jinxi Xu, Hongming Shu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./Chinese/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz](http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz)
- :material-file-search: **Runs:** [HIN300](./Chinese/runs.md#hin300) | [HIN301](./Chinese/runs.md#hin301)

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

#### Using Query Zoning and Correlation Within SMART: TREC 5

_Chris Buckley, Amit Singhal, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [Cornell](./Chinese/participants.md#cornell)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz](http://trec.nist.gov/pubs/trec5/papers/cornell.ps.gz)
- :material-file-search: **Runs:** [Cor5C1vt](./Chinese/runs.md#cor5c1vt) | [Cor5C2ex](./Chinese/runs.md#cor5c2ex)

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

#### Term importance, Boolean conjunct training, negative terms, and foreign  language retrieval: probabilistic algorithms at TREC-5

_Fredric C. Gey, Aitao Chen, Jianzhang He, Liangjie Xu, Jason Meggs_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./Chinese/participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz](http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.main.ps.gz)
- :material-file-search: **Runs:** [BrklyCH1](./Chinese/runs.md#brklych1) | [BrklyCH2](./Chinese/runs.md#brklych2)

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

#### Using Relevance Feedback within the Relational Model for TREC-5

_David A. Grossman, Carol Lundquist, John Reichart, David O. Holmes, Abdur Chowdhury, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [GMU](./Chinese/participants.md#gmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz)
- :material-file-search: **Runs:** [gmu96ca1](./Chinese/runs.md#gmu96ca1) | [gmu96ca2](./Chinese/runs.md#gmu96ca2) | [gmu96cm1](./Chinese/runs.md#gmu96cm1) | [gmu96cm2](./Chinese/runs.md#gmu96cm2)

??? abstract "Abstract"
	
	For TREC-5, we enhanced our existing prototype that implements relevance ranking using the AT&T DBC-1012 Model 4 parallel database machine to include relevance feedback. We identified SQL to compute relevance feedback and ran several experiments to identify good cutoffs for the number of documents that should be assumed to be relevant and the number of terms to add to a query. We also tried to find an optimal weighting scheme such that terms added by relevance feedback are weighted differently from those in the original query. We implemented relevance feedback in our special purpose IR prototype. Additionally, we used relevance feedback as a part of our submissions for English, Spanish, Chinese and corrupted data. Finally, we were a participant in the large data track as well. We used a text merging approach whereby a single Pentium processor was able to implement adhoc retrieval on a 4GB text collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanLRHCF96.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanLRHCF96,
		author = {David A. Grossman and Carol Lundquist and John Reichart and David O. Holmes and Abdur Chowdhury and Ophir Frieder},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Relevance Feedback within the Relational Model for {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanLRHCF96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi at TREC-5

_Micheline Hancock-Beaulieu, Mike Gatford, Xiangji Huang, Stephen E. Robertson, Steve Walker, P. W. Williams_

- :fontawesome-solid-user-group: **Participant:** [City](./Chinese/participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz)
- :material-file-search: **Runs:** [city96c1](./Chinese/runs.md#city96c1) | [city96c2](./Chinese/runs.md#city96c2)

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

#### Berkeley Chinese Information Retrieval at TREC-5: Technical Report

_Jianzhang He, Jack Xu, Aitao Chen, Jason Meggs, Fredric C. Gey_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./Chinese/participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.chinese.ps.gz](http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.chinese.ps.gz)
- :material-file-search: **Runs:** [BrklyCH1](./Chinese/runs.md#brklych1) | [BrklyCH2](./Chinese/runs.md#brklych2)

??? abstract "Abstract"
	
	The Berkeley experiments for TREC-5 extend those of TREC-4 in numerous ways. For routing retrieval we experimented with the idea of term importance in three ways -- training on Boolean con-juncts of the most important terms, filtering with the most important terms, and, finally, logistic regression on presence or absence of those terms. For ad-hoc retrieval we retained the manual reformulations of the topics and experimented with negative query terms. The ad-hoc retrieval formula originally devised for TREC-2 has proven to be robust, and was used for the TREC-5 ad-hoc retrieval and for our Chinese and Spanish retrieval. Chinese retrieval was accomplished through development of a segmentation algorithm which was used to augment a Chinese dictionary. The manual query run BrklyCH2 achieved a spectacular 97.48 percent recall over the 19 queries evaluated before the conference.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeXCMG96.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeXCMG96,
		author = {Jianzhang He and Jack Xu and Aitao Chen and Jason Meggs and Fredric C. Gey},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Berkeley Chinese Information Retrieval at {TREC-5:} Technical Report},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/brkly.trec5.chinese.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeXCMG96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on Chinese Text Indexing – CLARIT TREC-5 Chinese  Track Report

_Xiang Tong, ChengXiang Zhai, Natasa Milic-Frayling, David A. Evans_

- :fontawesome-solid-user-group: **Participant:** [CLARITECH](./Chinese/participants.md#claritech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/CLARIT-Chinese.ps.gz](http://trec.nist.gov/pubs/trec5/papers/CLARIT-Chinese.ps.gz)
- :material-file-search: **Runs:** [CLCHNA](./Chinese/runs.md#clchna) | [CLCHNM](./Chinese/runs.md#clchnm)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TongZME96.bib) "
	```
	@inproceedings{DBLP:conf/trec/TongZME96,
		author = {Xiang Tong and ChengXiang Zhai and Natasa Milic{-}Frayling and David A. Evans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments on Chinese Text Indexing -- {CLARIT} {TREC-5} Chinese Track Report},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/CLARIT-Chinese.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TongZME96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on Routing, Filtering and Chinese Text Retrieval in TREC-5

_Chong-Wah Ngo, Kok F. Lai_

- :fontawesome-solid-user-group: **Participant:** [ITI-SG](./Chinese/participants.md#iti-sg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/iti.trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/iti.trec5.ps.gz)
- :material-file-search: **Runs:** [iticn1](./Chinese/runs.md#iticn1) | [iticn2](./Chinese/runs.md#iticn2)

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

- :fontawesome-solid-user-group: **Participant:** [CUNY](./Chinese/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz](http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz)
- :material-file-search: **Runs:** [pircsCw](./Chinese/runs.md#pircscw) | [pircsCwc](./Chinese/runs.md#pircscwc)

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

## NLP 

#### NLP Track at TREC-5

_Tomek Strzalkowski, Karen Sparck Jones_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/nlp.track.96.ps.gz](http://trec.nist.gov/pubs/trec5/papers/nlp.track.96.ps.gz)
??? abstract "Abstract"
	
	NLP track has been organized for the first time at TREC-5 to provide a more focused look at how NLP techniques can help in achieving better performance in information retrieval. The intent was to see if NLP techniques available today are mature enough to have an impact on IR, specifically if and when they can offer an advantage over purely quantitative methods. This was also a place to try some more expensive and more risky solutions than those used in main TREC evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StrzalkowskiJ96.bib) "
	```
	@inproceedings{DBLP:conf/trec/StrzalkowskiJ96,
		author = {Tomek Strzalkowski and Karen Sparck Jones},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{NLP} Track at {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/nlp.track.96.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StrzalkowskiJ96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Retrieval and Trainable Natural Language Processing

_John D. Burger, John S. Aberdeen, David D. Palmer_

- :fontawesome-solid-user-group: **Participant:** [MITRE](./nlp/participants.md#mitre)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/mitre2.ps.gz](http://trec.nist.gov/pubs/trec5/papers/mitre2.ps.gz)
- :material-file-search: **Runs:** [MTRa961](./nlp/runs.md#mtra961)

??? abstract "Abstract"
	
	Existing work on indexing and retrieving documents from large on-line collections has had great success at treating both documents and queries as simple, unstructured collections of individual words (terms) with dependencies among these terms largely ignored. However, natural language text has a great deal of structure. In particular, at a scale close to that of the individual word, there are interactions and dependencies that many IR systems ignore. Those systems that do attempt to capture some of these dependencies do so in rather indirect ways. MITRE has substantial experience with trainable natural language algorithms, and we believe this powerful approach is complimentary to the standard information retrieval paradigm. Developed over a number of years, our technology has been used to good effect in the context of information extraction tasks, such as the Message Understanding Conferences (MUC) [1]. Because our approach is based on automatically training our NLP components on large data sets, resulting in accurate and very fast text processors, and because we believe that empirical evaluation is highly important, we have been interested in classical information retrieval for some time. Our first foray into TREC was begun to explore the possibility of improving IR systems with this technology.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BurgerAP96.bib) "
	```
	@inproceedings{DBLP:conf/trec/BurgerAP96,
		author = {John D. Burger and John S. Aberdeen and David D. Palmer},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Information Retrieval and Trainable Natural Language Processing},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/mitre2.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BurgerAP96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Xerox TREC-5 Site Report: Routing, Filtering, NLP, and Spanish Tracks

_David A. Hull, Gregory Grefenstette, B. Maximilian Schulze, Éric Gaussier, Hinrich Schütze, Jan O. Pedersen_

- :fontawesome-solid-user-group: **Participant:** [Xerox](./nlp/participants.md#xerox)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz](http://trec.nist.gov/pubs/trec5/papers/real-xerox.ps.gz)
- :material-file-search: **Runs:** [xerox-nlp1](./nlp/runs.md#xerox-nlp1) | [xerox-nlp2](./nlp/runs.md#xerox-nlp2) | [xerox-nlp3](./nlp/runs.md#xerox-nlp3) | [xerox-nlp4](./nlp/runs.md#xerox-nlp4) | [xerox-nlp5](./nlp/runs.md#xerox-nlp5) | [xerox-nlp6](./nlp/runs.md#xerox-nlp6)

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

#### Evaluation of Syntactic Phrase Indexing – CLARIT NLP Track Report

_Xiang Tong, ChengXiang Zhai, Natasa Milic-Frayling, David A. Evans_

- :fontawesome-solid-user-group: **Participant:** [CLARITECH](./nlp/participants.md#claritech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/CLARIT-NLP-corrected.ps.gz](http://trec.nist.gov/pubs/trec5/papers/CLARIT-NLP-corrected.ps.gz)
- :material-file-search: **Runs:** [CLATMC](./nlp/runs.md#clatmc) | [CLATMN](./nlp/runs.md#clatmn) | [CLPHR0](./nlp/runs.md#clphr0) | [CLPHR1](./nlp/runs.md#clphr1) | [CLPHR2](./nlp/runs.md#clphr2)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TongZME96b.bib) "
	```
	@inproceedings{DBLP:conf/trec/TongZME96b,
		author = {Xiang Tong and ChengXiang Zhai and Natasa Milic{-}Frayling and David A. Evans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Evaluation of Syntactic Phrase Indexing -- {CLARIT} {NLP} Track Report},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/CLARIT-NLP-corrected.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TongZME96b.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Confusion 

#### Report on the TREC-5 Confusion Track

_Paul B. Kantor, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/confusion_track.ps.gz](http://trec.nist.gov/pubs/trec5/papers/confusion_track.ps.gz)
??? abstract "Abstract"
	
	For TREC-5, retrieval from corrupted data was studied through retrieval of single target documents from a corpus which was corrupted by producing page images, corrupting the bit maps, and applying OCR techniques to the results. In general, methods which attempted a probabilistic estimation of the original clean text fare better than methods which simply accept corrupted versions of the query text.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KantorV96.bib) "
	```
	@inproceedings{DBLP:conf/trec/KantorV96,
		author = {Paul B. Kantor and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Report on the {TREC-5} Confusion Track},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/confusion\_track.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KantorV96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SPIDER Retrieval System at TREC-5

_Jean Paul Ballerini, Marco Büchel, Ruxandra Domenig, Daniel Knaus, Bojidar Mateev, Elke Mittendorf, Peter Schäuble, Paraic Sheridan, Martin Wechsler_

- :fontawesome-solid-user-group: **Participant:** [ETH](./confusion/participants.md#eth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/ETHatTREC5.final.USLetter.ps.gz](http://trec.nist.gov/pubs/trec5/papers/ETHatTREC5.final.USLetter.ps.gz)
- :material-file-search: **Runs:** [ETHD20N](./confusion/runs.md#ethd20n) | [ETHD20P](./confusion/runs.md#ethd20p) | [ETHD5N](./confusion/runs.md#ethd5n) | [ETHFR94](./confusion/runs.md#ethfr94) | [ETHD5P](./confusion/runs.md#ethd5p)

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

#### Using Relevance Feedback within the Relational Model for TREC-5

_David A. Grossman, Carol Lundquist, John Reichart, David O. Holmes, Abdur Chowdhury, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [GMU](./confusion/participants.md#gmu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz](http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz)
- :material-file-search: **Runs:** [gmu96v01](./confusion/runs.md#gmu96v01) | [gmu96v02](./confusion/runs.md#gmu96v02) | [gmu96v11](./confusion/runs.md#gmu96v11) | [gmu96v12](./confusion/runs.md#gmu96v12) | [gmu96v21](./confusion/runs.md#gmu96v21) | [gmu96v22](./confusion/runs.md#gmu96v22)

??? abstract "Abstract"
	
	For TREC-5, we enhanced our existing prototype that implements relevance ranking using the AT&T DBC-1012 Model 4 parallel database machine to include relevance feedback. We identified SQL to compute relevance feedback and ran several experiments to identify good cutoffs for the number of documents that should be assumed to be relevant and the number of terms to add to a query. We also tried to find an optimal weighting scheme such that terms added by relevance feedback are weighted differently from those in the original query. We implemented relevance feedback in our special purpose IR prototype. Additionally, we used relevance feedback as a part of our submissions for English, Spanish, Chinese and corrupted data. Finally, we were a participant in the large data track as well. We used a text merging approach whereby a single Pentium processor was able to implement adhoc retrieval on a 4GB text collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanLRHCF96.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanLRHCF96,
		author = {David A. Grossman and Carol Lundquist and John Reichart and David O. Holmes and Abdur Chowdhury and Ophir Frieder},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Relevance Feedback within the Relational Model for {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/gmu.trec5.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanLRHCF96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ANU/ACSys TREC-5 Experiments

_David Hawking, Paul B. Thistlewaite, Peter Bailey_

- :fontawesome-solid-user-group: **Participant:** [ANU](./confusion/participants.md#anu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/anu_t5_paper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/anu_t5_paper.ps.gz)
- :material-file-search: **Runs:** [anu5con0](./confusion/runs.md#anu5con0) | [anu5con1](./confusion/runs.md#anu5con1)

??? abstract "Abstract"
	
	A number of experiments conducted within the framework of the TREC-5 conference and using the Parallel Document Retrieval Engine (PADRE) are reported. Several of the experiments involve the use of distance-based relevance scoring (spans). This scoring method is shown to be capable of very good precision-recall performance, provided that good queries can be generated. Semi-automatic methods for refining manually-generated span queries are described and evaluated in the context of the adhoc retrieval task. Span queries are also applied to processing a larger (4.5 gigabyte) collection, to retrieval over OCR-corrupted data and to a database merging task. Lightweight probe queries are shown to be an effective method for identifying promising information servers in the context of the latter task. New techniques for automatically generating more conventional weighted-term queries from short topic descriptions have also been devised and are evaluated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HawkingTB96.bib) "
	```
	@inproceedings{DBLP:conf/trec/HawkingTB96,
		author = {David Hawking and Paul B. Thistlewaite and Peter Bailey},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {ANU/ACSys {TREC-5} Experiments},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/anu\_t5\_paper.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HawkingTB96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### OCR Correction and Query Expansion for Retrieval on OCR Data –  CLARIT TREC-5 Confusion Track Report

_Xiang Tong, ChengXiang Zhai, Natasa Milic-Frayling, David A. Evans_

- :fontawesome-solid-user-group: **Participant:** [CLARITECH](./confusion/participants.md#claritech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/CLARIT-Confusion.ps.gz](http://trec.nist.gov/pubs/trec5/papers/CLARIT-Confusion.ps.gz)
- :material-file-search: **Runs:** [CLCON20](./confusion/runs.md#clcon20) | [CLCON20F](./confusion/runs.md#clcon20f) | [CLCON5](./confusion/runs.md#clcon5) | [CLCON5F](./confusion/runs.md#clcon5f) | [CLCONBASE](./confusion/runs.md#clconbase)

??? abstract "Abstract"
	
	In CLARIT TREC-5 confusion track experiments, we explored two techniques for improving retrieval performance over corrupted data: (1) OCR word error correction to improve OCR text accuracy, and (2) query expansion by adding query term variants found in the corrupted text. The OCR word correction technique is based on statistical word bigram modeling Tong & Evans 1996]. The variants of a query term are terms similar to the query term, as measured by the edit distance [Wagner 1974]. While the official runs were based on the first approach, in our follow-up experiments we tested the second approach as well. In this report we first give a brief description of the OCR correction and query expansion techniques, and then discuss the results of our experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TongZME96a.bib) "
	```
	@inproceedings{DBLP:conf/trec/TongZME96a,
		author = {Xiang Tong and ChengXiang Zhai and Natasa Milic{-}Frayling and David A. Evans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{OCR} Correction and Query Expansion for Retrieval on {OCR} Data -- {CLARIT} {TREC-5} Confusion Track Report},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/CLARIT-Confusion.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TongZME96a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Interactive 

#### TREC-5 Interactive Track Report

_Paul Over_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/trackreport.ps.gz](http://trec.nist.gov/pubs/trec5/papers/trackreport.ps.gz)
??? abstract "Abstract"
	
	This report presents the framework for the TREC-5 interactive track experiments in detail, cites the results but refers the reader to the site reports for their analysis, and discusses unexpected disagreements between relevance and aspectual assessment performed by the NIST assessors.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Over96.bib) "
	```
	@inproceedings{DBLP:conf/trec/Over96,
		author = {Paul Over},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-5} Interactive Track Report},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/trackreport.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Over96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers Interactive Track at TREC-5

_Nicholas J. Belkin, A. Cabezas, Colleen Cool, K. Kim, Kwong Bor Ng, Soyeon Park, R. Pressman, Soo Young Rieh, Pamela A. Savage-Knepshield, Hong (Iris) Xie_

- :fontawesome-solid-user-group: **Participant:** [RutgersB](./interactive/participants.md#rutgersb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/ruint_paper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/ruint_paper.ps.gz)
- :material-file-search: **Runs:** [ruint](./interactive/runs.md#ruint)

??? abstract "Abstract"
	
	The Interactive Track investigation at Rutgers concentrated primarily on three factors: the searchers' uses and understandings of relevance feedback and ranked output, and the utility of relevance feedback for the interactive track task; the searchers' understandings of the interactive track task; and performance differences based on topic characteristics and searcher and order effects. Our official results are for twelve searchers, each of whom did searches on six different topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinCCKNPPRSX96.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinCCKNPPRSX96,
		author = {Nicholas J. Belkin and A. Cabezas and Colleen Cool and K. Kim and Kwong Bor Ng and Soyeon Park and R. Pressman and Soo Young Rieh and Pamela A. Savage{-}Knepshield and Hong (Iris) Xie},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Rutgers Interactive Track at {TREC-5}},
		booktitle = {Proceedings of The Fifth Text REtrieval Conference, {TREC} 1996, Gaithersburg, Maryland, USA, November 20-22, 1996},
		series = {{NIST} Special Publication},
		volume = {500-238},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1996},
		url = {http://trec.nist.gov/pubs/trec5/papers/ruint\_paper.ps.gz},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BelkinCCKNPPRSX96.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

