# Proceedings - Legal 2010 

#### Overview of the TREC 2010 Legal Track

_Gordon V. Cormack, Maura R. Grossman, Bruce Hedin, Douglas W. Oard_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec19/papers/LEGAL10.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec19/papers/LEGAL10.OVERVIEW.pdf)
??? abstract "Abstract"
	
	TREC 2010 was the fifth year of the Legal Track, which focuses on evaluation of search technology for discovery of electronically stored information in litigation and regulatory settings. The TREC 2010 Legal Track consisted of two distinct tasks: the Learning task, in which participants were required to estimate the probability of relevance for each document in a large collection, given a seed set of documents, each coded as responsive or non-responsive; and the Interactive task, in which participants were required to identify all relevant documents using a human-in-the-loop process.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackGHO10.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackGHO10,
		author = {Gordon V. Cormack and Maura R. Grossman and Bruce Hedin and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2010 Legal Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {https://trec.nist.gov/pubs/trec19/papers/LEGAL10.OVERVIEW.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackGHO10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Auto-Relevancy Baseline: A Hybrid System Without Human Feedback

_Cody Bennett_

- :fontawesome-solid-user-group: **Participant:** [TCDI](./participants.md#tcdi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/bennett.cody.LEGAL.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/bennett.cody.LEGAL.rev.pdf)
- :material-file-search: **Runs:** [tcd1](./runs.md#tcd1)

??? abstract "Abstract"
	
	On obtaining a Request for Production and automatically emulating a typical eDiscovery workflow1, a simple application of the classical Bayes algorithm upon the pseudo-hybridization of SemanticA and Latent Semantic IndexingBC systems should smooth out historically high yet noisy Recall of some LSI models and their derivatives and produce a tighter linear distribution when assessing relevant documents unsupervised.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bennett10.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bennett10,
		author = {Cody Bennett},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Auto-Relevancy Baseline: {A} Hybrid System Without Human Feedback},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/bennett.cody.LEGAL.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bennett10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IT-Discovery at TREC 2010 Legal

_Aron Culotta, Andy Liu, Mark Cordover, Bennett Borden, Sam Strickland_

- :fontawesome-solid-user-group: **Participant:** [IT.com](./participants.md#it.com)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/it.com.legal.pdf](http://trec.nist.gov/pubs/trec19/papers/it.com.legal.pdf)
- :material-file-search: **Runs:** [ITCOMRUN0](./runs.md#itcomrun0) | [ITD](./runs.md#itd)

??? abstract "Abstract"
	
	IT-Discovery participated in both the Learning Task (Topics 201-207) and the Interactive Task (Topics 301, 303). For the Learning Task, we used an optimized Naive Bayes classifier, which obtained 90-97% cross-validation accuracy on the provided seed sets for each topic. For the Interactive Task, we used the same classifier trained with one round of active learning. The annotator averaged 36.5 hours per topic, resulting in a cross-validation classification accuracy of 90%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CulottaLCBS10.bib) "
	```
	@inproceedings{DBLP:conf/trec/CulottaLCBS10,
		author = {Aron Culotta and Andy Liu and Mark Cordover and Bennett Borden and Sam Strickland},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {IT-Discovery at {TREC} 2010 Legal},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/it.com.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CulottaLCBS10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Applying Latent Semantic Indexing on the TREC 2010 Legal Dataset

_Andy Garron, April Kontostathis_

- :fontawesome-solid-user-group: **Participant:** [ursinus](./participants.md#ursinus)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/ursinus.college.legal.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/ursinus.college.legal.rev.pdf)
- :material-file-search: **Runs:** [URSLSIT](./runs.md#urslsit) | [URSK35T](./runs.md#ursk35t) | [URSK70T](./runs.md#ursk70t)

??? abstract "Abstract"
	
	We applied both Latent Semantic Indexing (LSI) and Essential Dimensions of LSI (EDLSI) to the 2010 TREC Legal Learning task. This year the Enron email collection was used and teams were given a list of relevant and a list of non-relevant documents for each of the eight test queries. In this article we focus on our attempts to incorporate machine learning into the LSI process. We show the EDLSI continues to outperform LSI on large datasets. For 2011 we plan to enhance our system by adding parallel and distributed approaches to LSI and EDLSI. We believe our retrieval performance would be improved if we could process more dimensions. Our current system resources limited us to 70 dimensions this year. Even with 70 dimensions our system performance was greater than or equal to the median for 6 of the 8 queries on the F1 metric.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarronK10.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarronK10,
		author = {Andy Garron and April Kontostathis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Applying Latent Semantic Indexing on the {TREC} 2010 Legal Dataset},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/ursinus.college.legal.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GarronK10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Indian Statistical Institute, Kolkata at TREC 2010: Legal Interactive

_Kripabandhu Ghosh, Swapan K. Parui, Prasenjit Majumder, Ayan Bandyopadhyay, S. John J. Raja Singh_

- :fontawesome-solid-user-group: **Participant:** [IRISICAL](./participants.md#irisical)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/indian-stat-institute.LEGAL.pdf](http://trec.nist.gov/pubs/trec19/papers/indian-stat-institute.LEGAL.pdf)
- :material-file-search: **Runs:** [IRISICAL1](./runs.md#irisical1)

??? abstract "Abstract"
	
	Indian Statistical Institute, Kolkata participated in TREC for the first time this year. We participated in TREC Legal Interactive task in two topics namely, Topic 301 and Topic 302. We reduced the size of the corpus by Boolean retrieval using Lemur 4.111 and followed it by a clustering technique. We chose members from each cluster (which we called seeds) for relevance judgement by the TA and assumed all other members of the cluster whose seeds are assessed as relevant to be relevant.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GhoshPMBS10.bib) "
	```
	@inproceedings{DBLP:conf/trec/GhoshPMBS10,
		author = {Kripabandhu Ghosh and Swapan K. Parui and Prasenjit Majumder and Ayan Bandyopadhyay and S. John J. Raja Singh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Indian Statistical Institute, Kolkata at {TREC} 2010: Legal Interactive},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/indian-stat-institute.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GhoshPMBS10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Bag of Words (BOW) and Standard Deviations to Represent Expected  Structures for Document Retrieval: A Way of Thinking that Leads  to Method Choices

_Harvey S. Hyman, Warren Fridy III_

- :fontawesome-solid-user-group: **Participant:** [USF_ISDS](./participants.md#usf_isds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.south.florida.rev.LEGAL.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.south.florida.rev.LEGAL.pdf)
- :material-file-search: **Runs:** [USFISDS](./runs.md#usfisds)

??? abstract "Abstract"
	
	This paper discusses a theory and proposed design for a retrieval artifact using a bag of words (BOW) approach for terms and a standard deviation method for assigning weights. The paper is organized into three parts. The first part is an historical overview of the development of text mining techniques. It is intended to acquaint the reader with our perspectives and assumptions; it is not intended to be an exhaustive review of the literature. The second part discusses the application of text mining techniques to the legal domain, specifically eDiscovery. The third part describes our approach to the 2010 TREC Legal Track problem set #301. Part Three is sub-divided into three sections. Section one is a discussion of our approach to document retrieval. Section two is a description of our design approach and method specifically chosen for Problem #301. Section three discusses contributions, limitations, generalizability, and conclusions based on our experience with the initial results produced by the competing artifacts in the TREC proceeding. We include a discussion of the initial results as reported at the conference.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HymanF10.bib) "
	```
	@inproceedings{DBLP:conf/trec/HymanF10,
		author = {Harvey S. Hyman and Warren Fridy III},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Bag of Words {(BOW)} and Standard Deviations to Represent Expected Structures for Document Retrieval: {A} Way of Thinking that Leads to Method Choices},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.south.florida.rev.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HymanF10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTH Does Probabilities of Relevance at the Legal Track

_Dim P. Papadopoulos, Vicky S. Kalogeiton, Avi Arampatzis_

- :fontawesome-solid-user-group: **Participant:** [EE.DUTH.GR](./participants.md#ee.duth.gr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/democritus.univ.legal.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/democritus.univ.legal.rev.pdf)
- :material-file-search: **Runs:** [DUTHsdtA](./runs.md#duthsdta) | [DUTHsdeA](./runs.md#duthsdea) | [DUTHlrgA](./runs.md#duthlrga)

??? abstract "Abstract"
	
	We participated in the Learning Task of the TREC 2010 Legal Track, focusing solely on estimating probabilities of relevance. We submitted three automated runs based on the same tf.idf ranking, produced by the topic narratives and positive-only feedback of the training data in equal contributions. The runs differ in the way the probabilities of relevance are estimated: (1) DUTHsdtA employed the Truncated Normal-Exponential model to turn scores to probabilities. (2) DUTHsdeA did not assume any specific component score distributions but estimated those on the scores of training data via Kernel Density Estimation (KDE) methods. (3) DUTHlrgA used Logistic Regression with the co-efficients estimated on the scores of training data. We found that DUTHsdeA and DUTHlrgA are greatly affected by biases in the training set, since they assume that input score data are uniformly sampled. Also, KDE was found to be very sensitive to its parameters, influencing greatly the probability estimates. In these respects, DUTHsdtA was proven to be the most robust method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PapadopoulosKA10.bib) "
	```
	@inproceedings{DBLP:conf/trec/PapadopoulosKA10,
		author = {Dim P. Papadopoulos and Vicky S. Kalogeiton and Avi Arampatzis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTH} Does Probabilities of Relevance at the Legal Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/democritus.univ.legal.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PapadopoulosKA10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at TREC 2010: Legal Interactive

_Mark D. Smucker, Charles L. A. Clarke, Gordon V. Cormack, Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [uwaterlooclarke](./participants.md#uwaterlooclarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.waterloo.LEGAL.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.waterloo.LEGAL.pdf)
- :material-file-search: **Runs:** [watlint10](./runs.md#watlint10)

??? abstract "Abstract"
	
	This year the University of Waterloo (UW) participated in the TREC Legal Interactive track and used the same process as last year except that this year we used three different human operators as opposed to only one as UW did last year. We participated in three topics: 301, 302, and 303. Relative to other participants, we performed well on one of the three topics. For two of the topics, low recall significantly hurt our F1 scores. Overall, we believe a contributing factor in our lower performance this year was with our interaction with the topic authorities, which resulted in our failing to understand the wide range of what constituted relevant material.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmuckerCCV10.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmuckerCCV10,
		author = {Mark D. Smucker and Charles L. A. Clarke and Gordon V. Cormack and Olga Vechtomova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Waterloo at {TREC} 2010: Legal Interactive},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.waterloo.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmuckerCCV10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UB at TREC 2010 Legal Interactive

_Ying Sun_

- :fontawesome-solid-user-group: **Participant:** [UB](./participants.md#ub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/suny.LEGAL.pdf](http://trec.nist.gov/pubs/trec19/papers/suny.LEGAL.pdf)
- :material-file-search: **Runs:** [UBlegal2010](./runs.md#ublegal2010)

??? abstract "Abstract"
	
	For the TREC 2010, the State University of New York at Buffalo participated in the Legal E-Discovery task, working on the interactive search task. We selected to explore RPD task 303. Our focus was on how to approach the problem with the assumption that business communication often wants to maintain secrecy or plausible deniability. Accordingly, it is not in the spirit of the problem to approach formulating queries by limiting ourselves to the mere text of the Complaint and RPD's. We have to envision the actual business context and the actual business practices to determine truly effective queries in the context of litigation. A simple interactive system based on Indri search engine was used to test the queries and examine the results. Post-experiment analysis is underway in alignment with the official evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Sun10.bib) "
	```
	@inproceedings{DBLP:conf/trec/Sun10,
		author = {Ying Sun},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UB} at {TREC} 2010 Legal Interactive},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/suny.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Sun10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Learning Task Experiments in the TREC 2010 Legal Track

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [ot](./participants.md#ot)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/open.txt.corp.legal.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/open.txt.corp.legal.rev.pdf)
- :material-file-search: **Runs:** [otL10rvlT](./runs.md#otl10rvlt) | [otL10FT](./runs.md#otl10ft) | [otL10bT](./runs.md#otl10bt)

??? abstract "Abstract"
	
	The Learning Task of the TREC 2010 Legal Track investigated the effectiveness of e-Discovery search techniques at learning from examples to estimate the probability of relevance of every document in a collection. The task specified 8 test topics, each of which included a one-sentence request for documents to produce and several examples of relevant and non-relevant items from a new target collection of 685,592 e-mail messages and attachments. For our participation, we produced three retrieval sets to compare experimental feedback-based, topic-based and Boolean-based techniques. In this paper, we describe the experimental approaches and report the scores that each achieved on various set-based and rank-based measures. We report not just the mean scores of the experimental approaches but also the scores on each of the 8 individual test topics and the largest per-topic impacts of the techniques for several measures. Of the three experimental approaches compared, the experimental feedback-based approach had the highest score in the rank-based F1@R measure and set-based F1@K measure for a majority of the test topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson10.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson10,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Learning Task Experiments in the {TREC} 2010 Legal Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/open.txt.corp.legal.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Melbourne Team at the TREC 2010 Legal Track

_William Webber, Falk Scholer, Mingfang Wu, Xiuzhen Zhang, Douglas W. Oard, Phil Farrelly, Sandra Potter, Steven Dick, Phill Bertolus_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec19/papers/univ.melbourne.LEGAL.pdf](https://trec.nist.gov/pubs/trec19/papers/univ.melbourne.LEGAL.pdf)
- :material-file-search: **Runs:** [rmitmlfT](./runs.md#rmitmlft) | [rmitmlsT](./runs.md#rmitmlst) | [rmitindA](./runs.md#rmitinda) | [melbit10](./runs.md#melbit10)

??? abstract "Abstract"
	
	The Melbourne team was a collaboration between academic and industry groups. The team participated in both the learning and the interactive tasks of this year's Legal Track. The baseline run for the learning track employed true-relevance feedback, achieving respectable outcomes; the experimental runs added additional features and employed an SVM classifier, with poor results. The techniques developed for the learning task were then deployed in the interactive task. The classifier again achieved poor predictive quality, although final results place our production (non-significantly) first. We describe the learning task efforts in Section 2, and the interactive task in Section 3.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WebberSWZOFPDB10.bib) "
	```
	@inproceedings{DBLP:conf/trec/WebberSWZOFPDB10,
		author = {William Webber and Falk Scholer and Mingfang Wu and Xiuzhen Zhang and Douglas W. Oard and Phil Farrelly and Sandra Potter and Steven Dick and Phill Bertolus},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Melbourne Team at the {TREC} 2010 Legal Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {https://trec.nist.gov/pubs/trec19/papers/univ.melbourne.LEGAL.pdf},
		timestamp = {Sun, 11 Feb 2018 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WebberSWZOFPDB10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

