# Proceedings - Filtering 2001 

#### The TREC 2001 Filtering Track Report

_Stephen E. Robertson, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/filtering_track.pdf](http://trec.nist.gov/pubs/trec10/papers/filtering_track.pdf)
??? abstract "Abstract"
	
	The TREC-10 filtering track measures the ability of systems to build persistent user profiles which successfully separate relevant and non-relevant documents. It consists of three major subtasks: adaptive filtering, batch filtering, and routing. In adaptive filtering, the system begins with only a topic statement and a small number of positive examples, and must learn a better profile from on-line feedback. Batch filtering and routing are more traditional machine learning tasks where the system begins with a large sample of evaluated training documents. This report describes the track, presents some evaluation results, and provides a general commentary on lessons learned from this year's track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonS01.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonS01,
		author = {Stephen E. Robertson and Ian Soboroff},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC} 2001 Filtering Track Report},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/filtering\_track.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonS01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Bias Problem and Language Models in Adaptive Filtering

_Yi Zhang, James P. Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu-lti](./participants.md#cmu-lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/trec10.CMUDIR.filter.pdf](http://trec.nist.gov/pubs/trec10/papers/trec10.CMUDIR.filter.pdf)
- :material-file-search: **Runs:** [CMUDIRURM](./runs.md#cmudirurm) | [CMUDIRFLM](./runs.md#cmudirflm) | [CMUDIRULM](./runs.md#cmudirulm) | [CMUDIRFRM](./runs.md#cmudirfrm)

??? abstract "Abstract"
	
	We used the YFILTER filtering system for experiments on updating profiles and setting thresholds. We developed a new method of using language models for updating profiles that is more focused on picking informative/discriminative words for query. The new method was compared with the well-known Rocchio algorithm. Dissemination thresholds were set based on maximum likelihood estimation that models and compensates for the sampling bias inherent in adaptive filtering. Our experimental results suggest that using what kind of distribution to model the scores of relevant and non- relevant documents is corpus dependant. The experimental results also show the sampling bias problem of training data while filtering makes the final profile learned biased.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangC01,
		author = {Yi Zhang and James P. Callan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The Bias Problem and Language Models in Adaptive Filtering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/trec10.CMUDIR.filter.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC-10: Filtering, QA, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yikun Guo, Yingju Xia, Zhe Feng_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf](http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf)
- :material-file-search: **Runs:** [FDUT10AF1](./runs.md#fdut10af1) | [FDUT10BF2](./runs.md#fdut10bf2) | [FDUT10BF1](./runs.md#fdut10bf1) | [FDUT10AF4](./runs.md#fdut10af4)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC conference for the second time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we participate in the sub-task of adaptive and batch filtering. Vector representation and computation are heavily applied in filtering procedure. Four runs have been submitted, which includes one T10SU and one T10F run for adpative filtering, as well as another one T10SU and one T10F run for batch filtering. We have tried many natural language processing techniques in our QA system, including statistical sentence breaking, POS tagging, parsing, name entity tagging, chunking and semantic verification. Various sources of world knowledge are also incorporated, such as WordNet and geographic information. For web retrieval, relevant document set is first created by an extended Boolean retrieval engine, and then reordered according to link information. Four runs with different combination of topic coverage and link information are submitted. On video track, We take part in both of the sub-tasks. In the task of shot boundary detection, we have submitted two runs with different parameters. In the task of video retrieval, we have submitted the results of 17 topics among all the topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHNGXF01.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHNGXF01,
		author = {Lide Wu and Xuanjing Huang and Junyu Niu and Yikun Guo and Yingju Xia and Zhe Feng},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{FDU} at {TREC-10:} Filtering, QA, Web and Video Tasks},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHNGXF01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-10 Experiments at CAS-ICT: Filtering, Web and QA

_Bin Wang, Hongbo Xu, Zhifeng Yang, Yue Liu, Xueqi Cheng, Dongbo Bu, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [chinese_academy](./participants.md#chinese_academy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf](http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf)
- :material-file-search: **Runs:** [ICTAdaFT10Ua](./runs.md#ictadaft10ua) | [ICTAdaFT10Fa](./runs.md#ictadaft10fa) | [ICTAdaFT10Ub](./runs.md#ictadaft10ub) | [ICTAdaFT10Uc](./runs.md#ictadaft10uc)

??? abstract "Abstract"
	
	CAS-ICT took part in the TREC conference for the first time this year. We have participated in three tracks of TREC-10. For adaptive filtering track, we paid more attention to feature selection and profile adaptation. For web track, we tried to integrate different ranking methods to improve system performance. For QA track, we focused on question type identification, named entity tagging and answer matching. This paper describes our methods in detail.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangXYLCBB01.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangXYLCBB01,
		author = {Bin Wang and Hongbo Xu and Zhifeng Yang and Yue Liu and Xueqi Cheng and Dongbo Bu and Shuo Bai},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-10} Experiments at {CAS-ICT:} Filtering, Web and {QA}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangXYLCBB01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Tampere University of Technology at TREC 2001

_Ari Visa, Jarmo Toivonen, Tomi Vesanen, Jarno Mäkinen_

- :fontawesome-solid-user-group: **Participant:** [Tampere](./participants.md#tampere)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/Visa.pdf](http://trec.nist.gov/pubs/trec10/papers/Visa.pdf)
- :material-file-search: **Runs:** [VisaWordT10](./runs.md#visawordt10) | [VisaSent1T10](./runs.md#visasent1t10)

??? abstract "Abstract"
	
	In this paper we present the prototype based text matching methodology used in the Routing Sub-Task of TREC 2001 Filtering Track. The methodology examines texts on word and sentence levels. On the word level the methodology is based on word coding and transforming the codes into histograms by the means of Weibull distribution. On the sentence level the word coding is done in a similar manner as on the word level. But instead of making histograms we use a more simple method. After the word coding, we transform the sentence vectors to sentence feature vectors using Slant transform. The paper includes also description of the TREC runs and some discussion about the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VisaTVM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/VisaTVM01,
		author = {Ari Visa and Jarmo Toivonen and Tomi Vesanen and Jarno M{\"{a}}kinen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Tampere University of Technology at {TREC} 2001},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/Visa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VisaTVM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SERbrainware at TREC 2001

_Pal Rujan_

- :fontawesome-solid-user-group: **Participant:** [SER](./participants.md#ser)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/ser_final.pdf](http://trec.nist.gov/pubs/trec10/papers/ser_final.pdf)
- :material-file-search: **Runs:** [serASSAT10ad](./runs.md#serassat10ad) | [serASSAT10ba](./runs.md#serassat10ba) | [serASSAT10ro](./runs.md#serassat10ro) | [serCLST10af](./runs.md#serclst10af) | [serCLST10ba](./runs.md#serclst10ba) | [serCLST10ro](./runs.md#serclst10ro)

??? abstract "Abstract"
	
	SER Technology Deutschland GmbH is the technological arm of SER Systems Inc, Herndon, Virginia. Our company focuses on knowledge-enabled software products, mostly related to document management. At the core of many of our products is a knowledge management engine called SERbrainware, which is being developed by our group in Oldenburg since 1999. This engine contains, among others, a text classifier and an associative access module. Both were used in preparing our entries. This is our first TREC. In order to get acquainted with the usual procedures, evaluation criteria, etc., we decided to participate first in the filtering track. Due to the fact that we had a rather restricted amount of time - two weeks - at our disposition, we used the commercially available engine version 2.40 without any special add-ons.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Rujan01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Rujan01,
		author = {Pal Rujan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {SERbrainware at {TREC} 2001},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/ser\_final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Rujan01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC-10: Filtering and Web Tracks

_Stephen E. Robertson, Steve Walker, Hugo Zaragoza_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/msr_cambridge.pdf](http://trec.nist.gov/pubs/trec10/papers/msr_cambridge.pdf)
- :material-file-search: **Runs:** [ok10f2br](./runs.md#ok10f2br) | [ok10f2ur](./runs.md#ok10f2ur)

??? abstract "Abstract"
	
	This report is concerned with the Adaptive Filtering and Web tracks. There are separate reports in this volume [1, 2] on the Microsoft Research Redmond participation in QA track and the Microsoft Research Beijing participation in the Web track. Two runs were submitted for the Adaptive Filtering track, on the adaptive filtering task only (two optimisa-tion measures), and several runs for the Web track, both tasks (adhoc and home page finding). The filtering system is somewhat similar to the one used for TREC-9; the web system is a simple Okapi system without blind feedback, but the document indexing includes anchor text from incoming links.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonWZ01.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonWZ01,
		author = {Stephen E. Robertson and Steve Walker and Hugo Zaragoza},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Microsoft Cambridge at {TREC-10:} Filtering and Web Tracks},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/msr\_cambridge.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonWZ01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Applying Support Vector Machines to the TREC-2001 Batch Filtering  and Routing Tasks

_David D. Lewis_

- :fontawesome-solid-user-group: **Participant:** [Lewis](./participants.md#lewis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/daviddlewis-trec2001-draft4.pdf](http://trec.nist.gov/pubs/trec10/papers/daviddlewis-trec2001-draft4.pdf)
- :material-file-search: **Runs:** [DLewis01bfFa](./runs.md#dlewis01bffa) | [DLewis01rFa](./runs.md#dlewis01rfa) | [DLewis01bfUa](./runs.md#dlewis01bfua) | [DLewis01rUa](./runs.md#dlewis01rua)

??? abstract "Abstract"
	
	My goal for TREC-2001 was simple: submit some runs (so that I could attend the conference), spend the minimum time necessary (since I’ve been busy this year with a large client project), and get respectable results (marketing!). The TREC batch filtering task was the obvious choice, since this year it was purely and simply a text categorization task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lewis01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lewis01,
		author = {David D. Lewis},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Applying Support Vector Machines to the {TREC-2001} Batch Filtering and Routing Tasks},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/daviddlewis-trec2001-draft4.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lewis01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Topic-Specific Optimization and Structuring

_David A. Evans, James G. Shanahan, Xiang Tong, Norbert Roma, Emilia Stoica, Victor Sheftel, Jesse Montgomery, Jeffrey Bennett, Gregory Grefenstette_

- :fontawesome-solid-user-group: **Participant:** [clairvoyance](./participants.md#clairvoyance)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/CLARIT_TREC-2001_Filtering_Final.pdf](http://trec.nist.gov/pubs/trec10/papers/CLARIT_TREC-2001_Filtering_Final.pdf)
- :material-file-search: **Runs:** [CL01afa](./runs.md#cl01afa) | [CL01afb](./runs.md#cl01afb) | [CL01afc](./runs.md#cl01afc) | [CL01afd](./runs.md#cl01afd) | [clT10rta](./runs.md#clt10rta) | [clT10rtb](./runs.md#clt10rtb) | [CLT10BFA](./runs.md#clt10bfa) | [CLT10BFB](./runs.md#clt10bfb)

??? abstract "Abstract"
	
	The Clairvoyance team participated in the Filtering Track, submitting the maximum number of runs in each of the filtering categories: Adaptive, Batch, and Routing. We had two distinct goals this year: (1) to establish the generalizability of our approach to adaptive filtering and (2) to experiment with relatively more 'radical' approaches to batch filtering using ensembles of filters. Our routing runs served principally to establish an internal basis for comparisons in performance to adaptive and batch efforts and are not discussed in this report.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EvansSTRSSMBG01.bib) "
	```
	@inproceedings{DBLP:conf/trec/EvansSTRSSMBG01,
		author = {David A. Evans and James G. Shanahan and Xiang Tong and Norbert Roma and Emilia Stoica and Victor Sheftel and Jesse Montgomery and Jeffrey Bennett and Gregory Grefenstette},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Topic-Specific Optimization and Structuring},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/CLARIT\_TREC-2001\_Filtering\_Final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EvansSTRSSMBG01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### kNN, Rocchio and Metrics for Information Filtering at TREC-10

_Tom Ault, Yiming Yang_

- :fontawesome-solid-user-group: **Participant:** [cmu-cat](./participants.md#cmu-cat)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/cmucat-correct.pdf](http://trec.nist.gov/pubs/trec10/papers/cmucat-correct.pdf)
- :material-file-search: **Runs:** [CMUCATsrf5](./runs.md#cmucatsrf5) | [CMUCATsr10](./runs.md#cmucatsr10) | [CMUCATmr10](./runs.md#cmucatmr10) | [CMUCATmrf5](./runs.md#cmucatmrf5) | [CMUCATa2f5](./runs.md#cmucata2f5) | [CMUCATa210](./runs.md#cmucata210)

??? abstract "Abstract"
	
	We compared a multi-class k-nearest neighbor (kNN) approach and a standard Rocchio method in the filtering tasks of TREC-10. Empirically, we found kNN more effective in batch filtering, and Rocchio better in adaptive filtering. For threshold adjustment based on relevance feedback, we developed a new strategy that updates a local regression over time based on a sliding window over positive examples and a sliding window over negative examples in the history. Applying this strategy to Rocchio and comparing its results to those by the same method with a fixed threshold, the recall was improved by 37-39% while the precision was improved by as much as 9%. Motivated by the extremely low performance of all systems on the T10S metric, we also analyzed this metric, and found that it favors more frequently occurring categories over rare ones and is somewhat inconsistent with its most straightforward interpretation. We propose a change to this metric which fixes these problems and brings it closer to the Cirk metric used to evaluate the TDT tracking task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AultY01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AultY01,
		author = {Tom Ault and Yiming Yang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {kNN, Rocchio and Metrics for Information Filtering at {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/cmucat-correct.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AultY01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Unbiased S-D Threshold Optimization, Initial Query Degradation,  Decay, and Incrementality, for Adaptive Document Filtering

_Avi Arampatzis_

- :fontawesome-solid-user-group: **Participant:** [nijmegen](./participants.md#nijmegen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/KUN-TREC10.pdf](http://trec.nist.gov/pubs/trec10/papers/KUN-TREC10.pdf)
- :material-file-search: **Runs:** [KUNbU](./runs.md#kunbu) | [KUNbF](./runs.md#kunbf) | [KUNr1](./runs.md#kunr1) | [KUNr2](./runs.md#kunr2) | [KUNaU](./runs.md#kunau) | [KUNaF](./runs.md#kunaf)

??? abstract "Abstract"
	
	We develop further the S-D threshold optimization method. Specifically, we deal with the bias problem introduced by receiving relevance judgements only for documents retrieved. The new approach estimates the parameters of the exponential Gaussian score density model without using any relevance judgements. The standard expectation maximization (EM) method for resolving mixtures of distributions is used. In order to limit the number of documents that need to be buffered, we apply nonuni-form document sampling, emphasizing the right tail (high scores) of the total score distribution. For learning filtering profiles, we present a version of Rocchio's method which is suitable and efficient for adaptive filtering. Its main new features are the initial query degradation and decay, while it is fully incremental in query updates and in calculating document score statistics. Initial query degradation eliminates gradually the contribution of the initial query as the number of relevant training documents increases. Decay considers relevant instances (documents and/or initial query) of the near past more heavily than those of the early past. This is achieved by the use of half-life, i.e. the age that a training instance must be before it is half as influential as a fresh one in training/updating a profile. All these new enhancements are consistent with the initial motivation of Rocchio's formula. We, moreover, use a form of term selection for all tasks (which in adaptive tasks is applied repeatedly), and query zoning for batch filtering and routing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Arampatzis01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Arampatzis01,
		author = {Avi Arampatzis},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Unbiased {S-D} Threshold Optimization, Initial Query Degradation, Decay, and Incrementality, for Adaptive Document Filtering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/KUN-TREC10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Arampatzis01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure and MercureFiltre Applied for Web and Filtering Tasks at TREC-10

_Mohand Boughanem, Claude Chrisment, Mohamed Tmar_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/irit.trec2001.pdf](http://trec.nist.gov/pubs/trec10/papers/irit.trec2001.pdf)
- :material-file-search: **Runs:** [mer10b](./runs.md#mer10b) | [mer10r1](./runs.md#mer10r1)

??? abstract "Abstract"
	
	The tests performed for TREC-10 focus on the Filtering (adaptive, batch and routing) tracks and web tracks. The runs are based on Mercure system for web, routing and batch tracks, and MercureFiltre for adaptive track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemCT01.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemCT01,
		author = {Mohand Boughanem and Claude Chrisment and Mohamed Tmar},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure and MercureFiltre Applied for Web and Filtering Tasks at {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/irit.trec2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemCT01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Oracle at TREC 10: Filtering and Question-Answering

_Shamin Alpha, Paul Dixon, Ciya Liao, Changwen Yang_

- :fontawesome-solid-user-group: **Participant:** [oracle](./participants.md#oracle)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/orcltrec10.pdf](http://trec.nist.gov/pubs/trec10/papers/orcltrec10.pdf)
- :material-file-search: **Runs:** [oraBU082701](./runs.md#orabu082701) | [oraRO082801](./runs.md#oraro082801) | [oraAU082201](./runs.md#oraau082201)

??? abstract "Abstract"
	
	Oracle’s objective in TREC-10 was to study the behavior of Oracle information retrieval in previously unexplored application areas. The software used was Oracle9i Text[1], Oracle’s full-text retrieval engine integrated with the Oracle relational database management system, and the Oracle PL/SQL procedural programming language. Runs were submitted in filtering and Q/A tracks. For the filtering track we submitted three runs, in adaptive filtering, batch filtering and routing. By comparing the TREC results, we found that the concepts (themes) extracted by Oracle Text can be used to aggregate document information content to simplify statistical processing. Oracle's Q/A system integrated information retrieval (IR) and information extraction (IE). The Q/A system relied on a combination of document and sentence ranking in IR, named entity tagging in IE and shallow parsing based classification of questions into pre-defined categories.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlphaDLY01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlphaDLY01,
		author = {Shamin Alpha and Paul Dixon and Ciya Liao and Changwen Yang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Oracle at {TREC} 10: Filtering and Question-Answering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/orcltrec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlphaDLY01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

