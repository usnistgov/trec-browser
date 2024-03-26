# Proceedings - Legal 2009 

#### Overview of the TREC 2009 Legal Track

_Bruce Hedin, Stephen Tomlinson, Jason R. Baron, Douglas W. Oard_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/LEGAL09.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec18/papers/LEGAL09.OVERVIEW.pdf)
??? abstract "Abstract"
	
	TREC 2009 was the fourth year of the Legal Track, which focuses on evaluation of search technology for “discovery” (i.e., responsive review) of electronically stored information in litigation and regulatory settings. The track included two tasks: an Interactive task (in which real users could iteratively refine their queries and/or engage in multi-pass relevance feedback) and a Batch task (two-pass search in a controlled setting with some relevant and nonrelevant documents manually marked after the first pass). This paper describes the design of the two tasks and presents the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HedinTBO09.bib) "
	```
	@inproceedings{DBLP:conf/trec/HedinTBO09,
		author = {Bruce Hedin and Stephen Tomlinson and Jason R. Baron and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2009 Legal Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/LEGAL09.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HedinTBO09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Machine Learning for Information Retrieval: TREC 2009 Web, Relevance  Feedback and Legal Tracks

_Gordon V. Cormack, Mona Mojdeh_

- :fontawesome-solid-user-group: **Participant:** [Waterloo](./participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf)
- :material-file-search: **Runs:** [watrrf](./runs.md#watrrf) | [watstack](./runs.md#watstack) | [watlogistic](./runs.md#watlogistic) | [watlint](./runs.md#watlint)

??? abstract "Abstract"
	
	For the TREC 2009, we exhaustively classified every document in each corpus, using machine learning methods that had previously been shown to work well for email spam [9, 3]. We treated each document as a sequence of bytes, with no tokenization or parsing of tags or meta-information. This approach was used exclusively for the adhoc web, diversity and relevance feedback tasks, as well as to the batch legal task: the ClueWeb09 and Tobacco collections were processed end-to-end and never indexed. We did the interactive legal task in two phases: first, we used interactive search and judging to find a large and diverse set of training examples; then we used active learning process, similar to what we used for the other tasks, to find find more relevant documents. Finally, we fitted a censored (i.e. truncated) mixed normal distribution to estimate recall and the cutoff to optimize F1, the principal effectiveness measure.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackM09.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackM09,
		author = {Gordon V. Cormack and Mona Mojdeh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Machine Learning for Information Retrieval: {TREC} 2009 Web, Relevance Feedback and Legal Tracks},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uwaterloo-cormack.WEB.RF.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackM09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Backstop LLP and Cleary Gottlied Steen & Hamilton LLP at TREC  Legal Track 2009

_Bruce Ellis Fein, Brian Merrell, F. Eli Nelson_

- :fontawesome-solid-user-group: **Participant:** [Cleary_Backstop](./participants.md#cleary_backstop)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/backstop.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/backstop.LEGAL.pdf)
- :material-file-search: **Runs:** [CGSHBCK2](./runs.md#cgshbck2) | [CGSHBCK](./runs.md#cgshbck) | [CGSHBCK1](./runs.md#cgshbck1)

??? abstract "Abstract"
	
	This paper presents the results of the collaborative entry of Backstop LLP and Cleary Gottlieb Steen & Hamilton LLP in the Legal Track of the 2009 Text Retrieval Conference (TREC) sponsored by the National Institute for Standards and Technology (NIST). The Legal Track served as a truncated replication of a document review of almost one million documents. Backstop software, assisted by attorney document review of less than one-tenth of one percent of the overall document set, classified the documents and achieved a combined accuracy rate (“F1 score”) of approximately 80%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FeinMN09.bib) "
	```
	@inproceedings{DBLP:conf/trec/FeinMN09,
		author = {Bruce Ellis Fein and Brian Merrell and F. Eli Nelson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Backstop {LLP} and Cleary Gottlied Steen {\&} Hamilton {LLP} at {TREC} Legal Track 2009},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/backstop.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FeinMN09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Sparse Matrix Factorization: Applications to Latent Semantic Indexing

_Erin Moulding, Raymond J. Spiteri, April Kontostathis_

- :fontawesome-solid-user-group: **Participant:** [URSINUS](./participants.md#ursinus)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ursinus.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/ursinus.LEGAL.pdf)
- :material-file-search: **Runs:** [ucedlsi](./runs.md#ucedlsi) | [uclsi](./runs.md#uclsi) | [ucscra](./runs.md#ucscra)

??? abstract "Abstract"
	
	This article describes the use of Latent Semantic Indexing (LSI) and some of its variants for the TREC Legal batch task. Both folding-in and Essential Dimensions of LSI (EDLSI) ap- peared as if they might be successful for recall-focused retrieval on a collection of this size. Furthermore, we developed a new LSI technique, one which replaces the Singular Value Decomposition (SVD) with another technique for matrix factorization, the sparse column-row approximation (SCRA). We were able to conclude that all three LSI techniques have similar performance. Although our 2009 results showed significant improvement when compared to our 2008 results, the use of a better method for selection of the parameter K, which is the ranking that results in the best balance between precision and recall, appears to have provided the most benefit.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MouldingSK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/MouldingSK09,
		author = {Erin Moulding and Raymond J. Spiteri and April Kontostathis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Sparse Matrix Factorization: Applications to Latent Semantic Indexing},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ursinus.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MouldingSK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Clearwell Systems at TREC 2009 Legal Interactive

_Venkat Rangan, Maojin Jiang_

- :fontawesome-solid-user-group: **Participant:** [Clearwell09](./participants.md#clearwell09)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/clearwell09.legal.pdf](http://trec.nist.gov/pubs/trec18/papers/clearwell09.legal.pdf)
- :material-file-search: **Runs:** [Clearwell09i](./runs.md#clearwell09i) | [clearwell01](./runs.md#clearwell01)

??? abstract "Abstract"
	
	The TREC Legal Track 2009 features an Interactive Task that is designed to replicate real-world challenges in producing a collection of responsive documents from a large collection of documents. The task required us to produce responsive documents from any of the seven topics, which are production requests. Clearwell Systems incorporated novel methods for producing a responsive collection using a combination of automated sampling, evaluation of the samples, and using the samples as input into a blind relevance feedback engine. The algorithms applied use an automatic correlation covariance matrix for automatic evaluation of the samples and, using the correlation coefficient, determine whether the process of blind feedback converges to a highly correlated set of responsive documents. The number of iterations of sampling, the K-value for blind feedback, along with the final convergence threshold are monitored. The F-measure results of this are compared across the three different Interactive Topics that Clearwell participated in, for discussions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RanganJ09.bib) "
	```
	@inproceedings{DBLP:conf/trec/RanganJ09,
		author = {Venkat Rangan and Maojin Jiang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Clearwell Systems at {TREC} 2009 Legal Interactive},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/clearwell09.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RanganJ09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### EQUIVIO at TREC 2009 Legal Interactive

_Tal Sterenzy_

- :fontawesome-solid-user-group: **Participant:** [Equivio](./participants.md#equivio)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/equivio.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/equivio.LEGAL.pdf)
- :material-file-search: **Runs:** [Equivio207R1](./runs.md#equivio207r1) | [Equivio205R1](./runs.md#equivio205r1)

??? abstract "Abstract"
	
	Equivio participated in two runs under the legal interactive track: topics 205 and 207. The runs utilized the Equivio>Relevance product. Equivio>Relevance is an expert-guided system which enables automated prioritization of documents and keywords. Based on initial input from a lead attorney, Equivio>Relevance uses statistical and self-learning techniques to calculate graduated relevance scores for each document in the data collection. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Sterenzy09.bib) "
	```
	@inproceedings{DBLP:conf/trec/Sterenzy09,
		author = {Tal Sterenzy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{EQUIVIO} at {TREC} 2009 Legal Interactive},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/equivio.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Sterenzy09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments with the Negotiated Boolean Queries of the TREC 2009  Legal Track

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [ot](./participants.md#ot)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/open-text.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/open-text.LEGAL.pdf)
- :material-file-search: **Runs:** [otL09rvl](./runs.md#otl09rvl) | [otL09F](./runs.md#otl09f) | [otL09frwF](./runs.md#otl09frwf)

??? abstract "Abstract"
	
	For our participation in the Batch Task of the TREC 2009 Legal Track, we produced several retrieval sets to compare experimental Boolean, vector, fusion and relevance feedback techniques for e-Discovery requests. In this paper, we have reported not just the mean scores of the experimental approaches but also the largest per-topic impacts of the techniques for several measures. The experimental automatic relevance feedback technique was found to attain a statistically significant gain over the reference Boolean result in both the mean Precision@B and F1@K measures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson09.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson09,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments with the Negotiated Boolean Queries of the {TREC} 2009 Legal Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/open-text.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ZL Technologies at TREC 2009 Legal Interactive: Comparing Exclusionary  and Investigative Approaches for Electronic Discovery Using the TREC  Enron Corpus

_John Wang, Cameron Coles, Rob Elliot, Sofia Andrianakou_

- :fontawesome-solid-user-group: **Participant:** [ZLTech](./participants.md#zltech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/zlti.legal.pdf](http://trec.nist.gov/pubs/trec18/papers/zlti.legal.pdf)
- :material-file-search: **Runs:** [CompCustIT09](./runs.md#compcustit09) | [CompEntrIT09](./runs.md#compentrit09)

??? abstract "Abstract"
	
	Organizations responding to requests to produce electronically stored information (ESI) for litigation today often conduct information retrieval with a limited amount of data that has first been culled by custodian mailboxes, date ranges, or other factors chosen semi-arbitrarily based on legal negotiations or other exogenous factors. The culling process does not necessarily take into account the composition of the data set; and may, in fact, impede the expediency and cost-effectiveness of the eDiscovery process as ESI not initially identified may need to be collected later in the eDiscovery process. This exclusionary eDiscovery approach has been recommended by search and information retrieval technology providers in the past, in part, based on the state of technology available at the time; however, the technology now exists to perform an inclusive, content-based, investigative eDiscovery across a large document collection without the introduction of semi- arbitrary exclusion factors. In this paper, we investigate whether limited document retrieval based on custodian email mailboxes results in lower recall and produces fewer responsive documents than a broader, inclusive search process that covers all potential custodians. In order to compare the two approaches, we designed an experiment with two independent teams conducting electronic discovery using the different approaches. We found that searching across the entire data set resulted in finding significantly more responsive documents and more initial custodians than implementing an approach that relies on custodian-based culling. Specifically, investigative eDiscovery found 516% more relevant documents and 1825% more initial custodians in our study. Based on these results, we believe organizations that employ an exclusionary, culling-based methodology may require subsequent collections, risk under production and sanctions during litigation, and will ultimately expend more resources in responding to eDiscovery production requests with a less comprehensive result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangCEA09.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangCEA09,
		author = {John Wang and Cameron Coles and Rob Elliot and Sofia Andrianakou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ZL} Technologies at {TREC} 2009 Legal Interactive: Comparing Exclusionary and Investigative Approaches for Electronic Discovery Using the {TREC} Enron Corpus},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/zlti.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangCEA09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2009 at the University of Buffalo: Interactive Legal E-Discovery  With Enron Emails

_Jianqiang Wang, Ying Sun, Paul Thompson_

- :fontawesome-solid-user-group: **Participant:** [SUNY_Buffalo](./participants.md#suny_buffalo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ubuffalo.LEGAL.pdf](http://trec.nist.gov/pubs/trec18/papers/ubuffalo.LEGAL.pdf)
- :material-file-search: **Runs:** [buffalo](./runs.md#buffalo)

??? abstract "Abstract"
	
	For the TREC 2009, the team from University at Buffalo, the State University of New York participated in the Legal E-Discovery track, working on the interactive search task. We explored indexing and searching at both the record level and the document level with the Enron email collection. We studied the usefulness of fielded search and document presentation features such as clustering documents based on email threads. For query formulation for the selected search topic, we combined a precision-oriented Specific Query method that a recall-oriented Generic Query method. Future evaluation of the effectiveness of these query techniques is still needed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangST09.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangST09,
		author = {Jianqiang Wang and Ying Sun and Paul Thompson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2009 at the University of Buffalo: Interactive Legal E-Discovery With Enron Emails},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ubuffalo.LEGAL.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangST09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Model for Understanding Collaborative Information Behavior in E-Discovery

_Zhen Yue, Daqing He_

- :fontawesome-solid-user-group: **Participant:** [pitt_sis](./participants.md#pitt_sis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/pitt_sis.legal.pdf](http://trec.nist.gov/pubs/trec18/papers/pitt_sis.legal.pdf)
- :material-file-search: **Runs:** [pittsis09](./runs.md#pittsis09)

??? abstract "Abstract"
	
	The University of Pittsburgh team participated in the interactive task of Legal Track in TREC 2009. We designed an experiment to investigate into the collaborative information behavior (CIB) of the group of people working on e-discovery tasks provided by Legal Track in TREC 2009. Through the studies, we proposed a model for understanding CIB in e-discovery.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YueH09.bib) "
	```
	@inproceedings{DBLP:conf/trec/YueH09,
		author = {Zhen Yue and Daqing He},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Model for Understanding Collaborative Information Behavior in E-Discovery},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/pitt\_sis.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YueH09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

