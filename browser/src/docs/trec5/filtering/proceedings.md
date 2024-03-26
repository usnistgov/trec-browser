# Proceedings - Filtering 1996 

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

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz](http://trec.nist.gov/pubs/trec5/papers/umass-trec96.ps.gz)
- :material-file-search: **Runs:** [INR3-p](./runs.md#inr3-p) | [INR3-m](./runs.md#inr3-m) | [INR3-r](./runs.md#inr3-r)

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

- :fontawesome-solid-user-group: **Participant:** [City](./participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz](http://trec.nist.gov/pubs/trec5/papers/city.procpaper.ps.gz)
- :material-file-search: **Runs:** [city96f1](./runs.md#city96f1) | [city96f2](./runs.md#city96f2) | [city96f3](./runs.md#city96f3)

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
- :material-file-search: **Runs:** [xerox.f1p25](./runs.md#xerox.f1p25) | [xerox.f1p50](./runs.md#xerox.f1p50) | [xerox.f1p75](./runs.md#xerox.f1p75) | [xerox.f2p75](./runs.md#xerox.f2p75) | [xerox.f2p50](./runs.md#xerox.f2p50) | [xerox.f2p25](./runs.md#xerox.f2p25) | [xerox.f3p25](./runs.md#xerox.f3p25) | [xerox.f3p50](./runs.md#xerox.f3p50) | [xerox.f3p75](./runs.md#xerox.f3p75)

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
- :material-file-search: **Runs:** [itift1](./runs.md#itift1) | [itift2](./runs.md#itift2) | [itift3](./runs.md#itift3)

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

- :fontawesome-solid-user-group: **Participant:** [Intext](./participants.md#intext)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/intext.ps.gz](http://trec.nist.gov/pubs/trec5/papers/intext.ps.gz)
- :material-file-search: **Runs:** [INTXA1](./runs.md#intxa1) | [INTXA2](./runs.md#intxa2) | [INTXA3](./runs.md#intxa3) | [INTXM1](./runs.md#intxm1) | [INTXM2](./runs.md#intxm2) | [INTXM3](./runs.md#intxm3)

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

- :fontawesome-solid-user-group: **Participant:** [CUNY](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz](http://trec.nist.gov/pubs/trec5/papers/queens.ps.gz)
- :material-file-search: **Runs:** [pircshp](./runs.md#pircshp) | [pircsmp](./runs.md#pircsmp) | [pircslp](./runs.md#pircslp)

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
- :material-file-search: **Runs:** [ispFA1](./runs.md#ispfa1) | [ispFB1](./runs.md#ispfb1) | [ispFC1](./runs.md#ispfc1)

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

