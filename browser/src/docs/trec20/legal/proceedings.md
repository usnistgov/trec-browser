# Proceedings - Legal 2011 

#### Overview of the TREC 2011 Legal Track

_Maura R. Grossman, Gordon V. Cormack, Bruce Hedin, Douglas W. Oard_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/LEGAL.OVERVIEW.2011.pdf](http://trec.nist.gov/pubs/trec20/papers/LEGAL.OVERVIEW.2011.pdf)
??? abstract "Abstract"
	
	The TREC 2011 Legal Track consisted of a single task: the learning task, which captured elements of both the TREC 2010 learning and interactive tasks. Participants were required to rank the entire corpus of 685,592 documents by their estimate of the probability of responsiveness to each of three topics, and also to provide a quantitative estimate of that probability. Participants were permitted to request up to 1,000 responsiveness determinations from a Topic Authority for each topic. Participants elected either to use only these responsiveness determinations in preparing automatic submissions, or to augment these determinations with their own manual review in preparing technology-assisted submissions. We provide an overview of the task and a summary of the results. More detailed results are available in the Appendix to the TREC 2011 Proceedings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanCHO11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanCHO11,
		author = {Maura R. Grossman and Gordon V. Cormack and Bruce Hedin and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2011 Legal Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/LEGAL.OVERVIEW.2011.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanCHO11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Auto-Relevancy and Responsiveness Baseline II Improving Concept  Search to Establish a Subset with Maximized Recall for Automated First  Pass and Early Assessment Using Latent Semantic Indexing [LSI], Bigrams  and WordNet 3.0 Seeding

_Cody Bennett_

- :fontawesome-solid-user-group: **Participant:** [TCDI](./participants.md#tcdi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/TCDI.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/TCDI.legal.update.pdf)
- :material-file-search: **Runs:** [tcdicskwA1](./runs.md#tcdicskwa1) | [tcdilentA2](./runs.md#tcdilenta2) | [tcdihentA3](./runs.md#tcdihenta3) | [tcdinokaAF](./runs.md#tcdinokaaf)

??? abstract "Abstract"
	
	We experiment with manipulating the features at build time by indexing bigrams created from EDRM data and seeding the LSI index with thesaurus-like WordNet 3.0 strata. From experimentation, this produces fewer false positives and a smaller, more focused relevant set. The method allows concept searching using bigrams and WordNet senses in addition to singular terms increasing polysemous value and precision; steps towards a unification of Semantic and Statistical. Also, because of LSI and WordNet senses, WSD appears enhanced. We then apply an automated method for selecting search criteria, query expansion and concept searching from Reviewer Guidelines and the original Request for Production thereby returning a search result with scores across the Enron corpus for each topic. The result of the normalized cosine distance score for each document in each topic is then shifted based on the foundation of primes, golden standard, and golden ratio. This results in 'best cutoff' using naturally occurring patterns in probability of expected relevancy with limit approaching .5. Submissions A1, A2, A3, and AF include similar combinations of the above. Although we did not submit a mopup run, we analyzed the mopups for post assessment. For each of the three topics, there were documents which TAs selected as relevant in contention with their other personal assessments. The defect percentage and potential impact to a semi/automated system will also be examined. Overall the influence of humans involved (TAs) was very minimal, as their assessments were not allowed to modify any rank or probability of documents. However, the identification of relevant documents by TAs at low LSI thresholds provided a feedback loop to affect the natural cutoff. Cutoffs for A1, A2, A3 were nearly -.04 (Landau) against the Golden and Poisson means and F was nearly +.04 (Apéry). Since more work is required to decrease false positives, it is encouraging to find a natural relevancy cutoff that maximizes probable Recall of Responsiveness across differing topics. Automated concept search using a mechanically generated semantically derived feature set upon indexed bigram and WordNet sense terms in an LSI framework reduces false positives and produces a tighter cluster of potentially responsive documents. Further, since legal Productions are essentially binary (R/NR), work was done to argue for scoring supporting this view. Obtaining Recall =>90% and Precision =>90% with a high degree of success is a two step process1, of which we test and discuss the first (maximization of Recall) for this study. Therefore, our focus will be heavily skewed on the probability of attaining high Recall for the creation of a subset of the corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bennett11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bennett11,
		author = {Cody Bennett},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Auto-Relevancy and Responsiveness Baseline {II} Improving Concept Search to Establish a Subset with Maximized Recall for Automated First Pass and Early Assessment Using Latent Semantic Indexing [LSI], Bigrams and WordNet 3.0 Seeding},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/TCDI.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bennett11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Latent Semantic Indexing with selective Query Expansion

_Andy Garron, April Kontostathis_

- :fontawesome-solid-user-group: **Participant:** [URSINUS](./participants.md#ursinus)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Ursinus.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Ursinus.legal.update.pdf)
- :material-file-search: **Runs:** [URS205A1](./runs.md#urs205a1) | [URS222A2](./runs.md#urs222a2) | [URS403A2](./runs.md#urs403a2) | [URS205A3](./runs.md#urs205a3) | [URS205AM](./runs.md#urs205am)

??? abstract "Abstract"
	
	This article describes our experiments during participation in the Legal Track of the 2011 Text REtrieval Conference. We incorporated machine learning, via selective query expansion, into our existing EDLSI system. We also were able to expand the number of dimensions used within our EDLSI system. Our results show that EDLSI is an effective technique for E-Discovery. We also have shown that selective query expansion can be a useful mechanism for improving retrieval results when a specific initial query is provided. We believe that queries that are stated in general terms, however, may suffer from “expansion in the wrong direction” when certain iterative approaches to incorporating relevance feedback information are incorporated into the search process.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarronK11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarronK11,
		author = {Andy Garron and April Kontostathis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Latent Semantic Indexing with selective Query Expansion},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Ursinus.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GarronK11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cluster-Based Relevance Feedback: Legal Track 2011

_Kripabandhu Ghosh, Swapan K. Parui, Prasenjit Majumder_

- :fontawesome-solid-user-group: **Participant:** [IRISCAL](./participants.md#iriscal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/IRISCAL.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/IRISCAL.legal.update.pdf)

??? abstract "Abstract"
	
	This is our second participation in the TREC Legal Track. The TREC Legal Track 2011 featured only the Learning Task. We participated in Topics 401 and 403. We used Lemur 4.111 for Boolean retrieval and followed it with a clustering technique, where we chose members from each cluster (which we called seeds) for relevance judgement by the TA and assumed all other members of the cluster whose seeds are assessed as relevant to be relevant. Based on the relevance information from seeds and their clusters, we applied Rocchio relevance feedback technique implemented in Terrier 3.02. Then, we used the feedback terms for the expansion of both the text queries and the Boolean queries. Finally, we used Z-fusion[4], a data fusion technique, on two of our runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GhoshPM11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GhoshPM11,
		author = {Kripabandhu Ghosh and Swapan K. Parui and Prasenjit Majumder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Cluster-Based Relevance Feedback: Legal Track 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/IRISCAL.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GhoshPM11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Modeling Concept and Context to Improve Performance in eDiscovery

_Harvey S. Hyman, Warren Fridy III_

- :fontawesome-solid-user-group: **Participant:** [USF_ISDS](./participants.md#usf_isds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/USF-ISDS.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/USF-ISDS.legal.update.pdf)
- :material-file-search: **Runs:** [USFEOLT](./runs.md#usfeolt) | [USFDSET](./runs.md#usfdset) | [USFMOPT](./runs.md#usfmopt)

??? abstract "Abstract"
	
	One condition of eDiscovery making it unique from other, more routine forms of IR is that all documents retrieved are settled by human inspection. Automated IR tools are used to reduce the size of a corpus search space to produce smaller sets of documents to be reviewed. However, a limitation associated with automated tools is they mainly employ statistical use of search terms that can result in poor performance when measured by recall and precision. One reason for this limitation is that relevance -- the quality of matching a document to user criteria - - is dynamic and fluid, whereas a query -- representing the translation of a user's IR goal - is fixed. This paper reports on a design approach to eDiscovey that combines concept and context modeling to enhance search term performance. We apply this approach to the TREC 2011 Legal Track Problem Set #401. Our goal is to improve performance in eDiscovery IR results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HymanF11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HymanF11,
		author = {Harvey S. Hyman and Warren Fridy III},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Modeling Concept and Context to Improve Performance in eDiscovery},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/USF-ISDS.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HymanF11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Heliod at TREC Legal 2011: Learning to Rank from Relevance Feedback  for e-Discovery

_Peter Lubell-Doughtie, Kenneth Hamilton_

- :fontawesome-solid-user-group: **Participant:** [dioileh](./participants.md#dioileh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/dioileh.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/dioileh.legal.update.pdf)
- :material-file-search: **Runs:** [HELqlaA1](./runs.md#helqlaa1) | [HELclrAM](./runs.md#helclram) | [HELq20rAM](./runs.md#helq20ram)

??? abstract "Abstract"
	
	We present the results of applying a learning to rank algorithm to the 2011 TREC Legal dataset. The learning to rank algorithm we use was designed to maximize NDCG, MAP, and AUC scores. We therefore examine our results using the AUC and hypothetical F1 scores. We find query expansion and learning to rank improve scores beyond standard language model retrieval, however learning to rank does not outperform query expansion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lubell-DoughtieH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lubell-DoughtieH11,
		author = {Peter Lubell{-}Doughtie and Kenneth Hamilton},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Heliod at {TREC} Legal 2011: Learning to Rank from Relevance Feedback for e-Discovery},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/dioileh.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lubell-DoughtieH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Learning Task Experiments in the TREC 2011 Legal Track

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [ot](./participants.md#ot)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/OpenText.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/OpenText.legal.update.pdf)
- :material-file-search: **Runs:** [otL11BT1](./runs.md#otl11bt1) | [otL11FT1](./runs.md#otl11ft1) | [otL11FT2](./runs.md#otl11ft2) | [otL11BT2](./runs.md#otl11bt2) | [otL11HT1](./runs.md#otl11ht1) | [otL11HT2](./runs.md#otl11ht2) | [otL11FTM](./runs.md#otl11ftm) | [otL11BTM](./runs.md#otl11btm) | [otL11HTM](./runs.md#otl11htm)

??? abstract "Abstract"
	
	The Learning Task of the TREC 2011 Legal Track investigated the effectiveness of e-Discovery search techniques at selecting training examples and learning from them to estimate the probability of relevance of every document in a collection. The task specified 3 test topics, each of which included a one-sentence request for documents to produce from a target collection of 685,592 e-mail messages and attachments. In this paper, we describe the experimental approaches used and report the scores that each achieved.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson11,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Learning Task Experiments in the {TREC} 2011 Legal Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/OpenText.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at TREC 2011: A Social Networking Approach  to the Legal Learning Track

_Robert Warren_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/waterloo.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/waterloo.legal.update.pdf)
- :material-file-search: **Runs:** [UWABASA1](./runs.md#uwabasa1) | [UWABASA2](./runs.md#uwabasa2) | [UWABASA3](./runs.md#uwabasa3) | [UWABASA4](./runs.md#uwabasa4) | [UWASNAA1](./runs.md#uwasnaa1) | [UWASNAA2](./runs.md#uwasnaa2) | [UWASNAA4](./runs.md#uwasnaa4) | [UWASNAA3](./runs.md#uwasnaa3) | [UWASNAAF](./runs.md#uwasnaaf) | [UWALINAF](./runs.md#uwalinaf) | [UWABASAF](./runs.md#uwabasaf) | [UWALINA2](./runs.md#uwalina2) | [UWALINA4](./runs.md#uwalina4) | [UWALINA3](./runs.md#uwalina3) | [UWABASAM](./runs.md#uwabasam) | [UWASNAAM](./runs.md#uwasnaam) | [UWALINAM](./runs.md#uwalinam)

??? abstract "Abstract"
	
	This paper reports on the University of Waterloo experience with the Legal Learning track where three different methods were used to approach the retrieval task. Two are based on previously used methods and the last is a novel method based on modifying the responsiveness probability using social network analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Warren11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Warren11,
		author = {Robert Warren},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Waterloo at {TREC} 2011: {A} Social Networking Approach to the Legal Learning Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/waterloo.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Warren11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melboune at the TREC 2011 Legal Track

_William Webber, Phil Farrelly_

- :fontawesome-solid-user-group: **Participant:** [unimelb_plus](./participants.md#unimelb_plus)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/unimelb_plus.legal.pdf](http://trec.nist.gov/pubs/trec20/papers/unimelb_plus.legal.pdf)
- :material-file-search: **Runs:** [mlbclsA1](./runs.md#mlbclsa1) | [mlbclsAF](./runs.md#mlbclsaf) | [mlblrnTF](./runs.md#mlblrntf) | [mlblrnTM](./runs.md#mlblrntm)

??? abstract "Abstract"
	
	The Melbourne team was a collaboration of the University of Melbourne, RMIT University, and the Victorian Society for Computers and the Law. The approach taken was to train a support vector machine based upon textual features using active learning. Two sources of relevance annotations were used for different runs: the official annotations, provided by the topic authorities; and annotations provided by a member of the Melbourne team with e-discovery experience (though not legal training). We describe the SVM method used in Section 1.1, the run using official annotations in Section 1.2, and the run using the internal annotations in Section 1.3.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WebberF11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WebberF11,
		author = {William Webber and Phil Farrelly},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Melboune at the {TREC} 2011 Legal Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/unimelb\_plus.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WebberF11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Recommind at TREC 2011 Legal Track

_Peter Zeinoun, Aaron Laliberte, Jan Puzicha, Howard Sklar, Craig Carpenter_

- :fontawesome-solid-user-group: **Participant:** [Recommind](./participants.md#recommind)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Recommind.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Recommind.legal.update.pdf)
- :material-file-search: **Runs:** [recommind03T](./runs.md#recommind03t) | [recommind04T](./runs.md#recommind04t)

??? abstract "Abstract"
	
	The TREC 2011 Legal Track Learning Task (the '2011 Task') evaluated each of approximately 685,000 documents from the Enron data set for responsiveness to one or more requests for production. The 2011 Task included three new requests for production (the 'Topics' and each a 'Topic')). In this paper, we describe the approaches used to conduct the review by the Recommind team and report the scores for each of the three Topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZeinounLPSC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZeinounLPSC11,
		author = {Peter Zeinoun and Aaron Laliberte and Jan Puzicha and Howard Sklar and Craig Carpenter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Recommind at {TREC} 2011 Legal Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Recommind.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZeinounLPSC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2011 Legal Track Discovery Based on Relevant Feedback

_Jiayue Zhang, Wenyi Yang, Xi Wang, Lihua Wu, Yongtian Zhang, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/PRIS.legal.pdf](http://trec.nist.gov/pubs/trec20/papers/PRIS.legal.pdf)
- :material-file-search: **Runs:** [priindA1](./runs.md#priinda1) | [priindA2](./runs.md#priinda2)

??? abstract "Abstract"
	
	In order to finish the task of TREC 2011 Legal Track, this paper puts forward an experiment method, which combines indri and relevant feedback to evaluate the probability of relevance of every document in a collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangYWWZXCG11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangYWWZXCG11,
		author = {Jiayue Zhang and Wenyi Yang and Xi Wang and Lihua Wu and Yongtian Zhang and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2011 Legal Track Discovery Based on Relevant Feedback},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/PRIS.legal.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangYWWZXCG11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

