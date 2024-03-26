# Proceedings - Filtering 1999 

#### The TREC-8 Filtering Track Final Report

_David A. Hull, Stephen E. Robertson_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/filtering.pdf](http://trec.nist.gov/pubs/trec8/papers/filtering.pdf)
??? abstract "Abstract"
	
	The TREC-8 filtering track measures the ability of systems to build persistent user profiles which successfully separate relevant and non-relevant documents. It consists of three major subtasks: adaptive filtering, batch filtering, and routing. In adaptive filtering, the system begins with only a topic statement and must learn a better profile from on-line feedback. Batch filtering and routing are more traditional machine learning tasks where the system begins with a large sample of evaluated training documents. This report describes the track, presents the evaluation results in graphical format, and provides a general commentary on lessons learned from this year's track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HullR99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HullR99,
		author = {David A. Hull and Stephen E. Robertson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-8} Filtering Track Final Report},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/filtering.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HullR99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Optimization in CLARIT TREC-8 Adaptive Filtering

_ChengXiang Zhai, Peter Jansen, Norbert Roma, Emilia Stoica, David A. Evans_

- :fontawesome-solid-user-group: **Participant:** [claritech](./participants.md#claritech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/CLARIT_Filtering.pdf](http://trec.nist.gov/pubs/trec8/papers/CLARIT_Filtering.pdf)
- :material-file-search: **Runs:** [CL99afL1a](./runs.md#cl99afl1a) | [CL99afL1b](./runs.md#cl99afl1b) | [CL99bfL1](./runs.md#cl99bfl1) | [CL99bfL2](./runs.md#cl99bfl2) | [CL99afL1c](./runs.md#cl99afl1c) | [CL99afL1d](./runs.md#cl99afl1d) | [CL99afL2](./runs.md#cl99afl2) | [CL99afN1](./runs.md#cl99afn1)

??? abstract "Abstract"
	
	In this paper, we describe the system and methods used for the CLARITECH entries in the TREC-8 Filtering Track. Our focus of participation was on the adaptive filtering task, as this comes closest to actual applications. In TREC-7, we proposed, evaluated, and proved effective two algorithms for threshold setting and updating— the delivery ratio mechanism, which is used to obtain a profile threshold when no feedback has been received, and beta-gamma regulation, which is used for threshold updating. This year, we explored two ways of improving filtering performance given these our threshold-setting algorithms as a basis by (1) allowing profile-specific anytime updating and (2) optimizing the other filtering system components, in particular, the retrieval/scoring mechanism and the profile vector learning. Our results show that profile-specific frequent updating indeed improves filtering performance. In addition, they suggest that optimizing the scoring function and the term vector learning component independently leads to even further improvement, providing another indication of the effectiveness and robustness of our threshold updating mechanism.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaiJRSE99.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaiJRSE99,
		author = {ChengXiang Zhai and Peter Jansen and Norbert Roma and Emilia Stoica and David A. Evans},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Optimization in {CLARIT} {TREC-8} Adaptive Filtering},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/CLARIT\_Filtering.pdf},
		timestamp = {Thu, 05 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhaiJRSE99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Two-Step Feature Selection and Neural Network Classification for the  TREC-8 Routing

_Mathieu Stricker, Frantz Vichot, Gérard Dreyfus, Francis Wolinski_

- :fontawesome-solid-user-group: **Participant:** [icdc](./participants.md#icdc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/s2n2.pdf](http://trec.nist.gov/pubs/trec8/papers/s2n2.pdf)
- :material-file-search: **Runs:** [S2N2](./runs.md#s2n2)

??? abstract "Abstract"
	
	At the Caisse des Dépôts et Consignations (CDC), the Agence France-Presse (AFP) news releases are filtered continuously according to the users' interests. Once a user has specified a topic of interest, a filter is customized to fit this user's profile. Until now, these filters would rely on rule-based methods, whose efficiency is proven [Vichot et al., 1999], but which require a large amount of work for each specific filter. This drawback can be avoided by using statistical methods which have the ability to learn from examples of relevant documents. Recently, we have developed a methodology for the AFP corpus. This paper presents its application to the TREC-8 corpus. For the TREC-8 routing, one specific filter is built for each topic. Each filter is a classifier trained to recognize the documents that are relevant to the topic. When presented with a document, each classifier estimates the probability for the document to be relevant to the topic for which it has been trained. Since the procedure for building a filter is topic-independent, the system is fully automatic. Therefore, we describe it for one topic; the procedure is repeated 50 times. By making use of a sample of documents that have previously been evaluated as relevant or not relevant to a particular topic, a term selection is performed, and a neural network is trained. Each document is represented by a vector of frequencies of a list of selected terms. This list depends on the topic to be filtered; it is constructed in two steps. The first step defines the characteristic words used in the relevant documents of the corpus; the second one chooses, among the previous list, the most discriminant ones. The length of the vector is optimized automatically for each topic. At the end of the term selection, a vector of typically 25 words is defined for the topic, so that each document which has to be processed is represented by a vector of term frequencies. This vector is subsequently input to a classifier that is trained from the same sample. After training, the classifier estimates for each document of a test set its probability of being relevant; for submission to TREC, the top 1000 documents are ranked in order of decreasing relevance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/StrickerVDW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/StrickerVDW99,
		author = {Mathieu Stricker and Frantz Vichot and G{\'{e}}rard Dreyfus and Francis Wolinski},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Two-Step Feature Selection and Neural Network Classification for the {TREC-8} Routing},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/s2n2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/StrickerVDW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SCAI TREC-8 Experiments

_Dong-Ho Shin, Yu-Hwan Kim, Sun Kim, Jae-Hong Eom, Hyung-Joo Shin, Byoung-Tak Zhang_

- :fontawesome-solid-user-group: **Participant:** [seoul](./participants.md#seoul)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps](http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps)
- :material-file-search: **Runs:** [Scai8Ft](./runs.md#scai8ft)

??? abstract "Abstract"
	
	This working note reports our experiences with TREC-8 on four tracks: Ad Hoc, Filtering, Web, and QA. The Ad Hoc retrieval engine, SCAIR, has been used for the Web and QA experiments, and the filtering experiments were based on it's own engine. As a second entry to TREC, we focused this year on exploring possibilities of applying machine learning techniques to TREC tasks. The Ad Hoc track employed a cluster-based retrieval method where the scoring function used cluster information extracted from a collection of precompiled documents. Filtering was based on naive Bayes learning supported by an EM algorithm. In the Web track, we compared the performance of using link information to that of not using the information. In the QA track, some passage extraction techniques have been tested using the baseline SCAIR retrieval engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShinKKESZ99.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShinKKESZ99,
		author = {Dong{-}Ho Shin and Yu{-}Hwan Kim and Sun Kim and Jae{-}Hong Eom and Hyung{-}Joo Shin and Byoung{-}Tak Zhang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{SCAI} {TREC-8} Experiments},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/ScaiTrec8.ps},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShinKKESZ99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Okapi/Keenbow at TREC-8

_Stephen E. Robertson, Steve Walker_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/okapi.pdf](http://trec.nist.gov/pubs/trec8/papers/okapi.pdf)
- :material-file-search: **Runs:** [ok8f112](./runs.md#ok8f112) | [ok8f122](./runs.md#ok8f122) | [ok8f311](./runs.md#ok8f311) | [ok8f312](./runs.md#ok8f312) | [ok8f321](./runs.md#ok8f321) | [ok8f222](./runs.md#ok8f222)

??? abstract "Abstract"
	
	Automatic ad hoc and web track: Three ad hoc runs were submitted: long (title, description and narrative), medium (title and description) and short (title only). 'Blind' expansion was used for all runs. The queries from the medium ad hoc run were reused for the small web track submission. Most of the negative expressions were removed from the narrative field of the topic statements, and a new expansion term selection procedure was tried. Adaptive filtering: Methods were similar to those we used in TREC-7. Six runs were submitted. VLC track: Two unexpanded ad hoc runs were submitted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonW99.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonW99,
		author = {Stephen E. Robertson and Steve Walker},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Okapi/Keenbow at {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/okapi.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonW99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Experiments at Maryland: CLIR, QA and Routing

_Douglas W. Oard, Jianqiang Wang, Dekang Lin, Ian Soboroff_

- :fontawesome-solid-user-group: **Participant:** [umd](./participants.md#umd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf](http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf)
- :material-file-search: **Runs:** [umrqz](./runs.md#umrqz) | [umrlsi](./runs.md#umrlsi)

??? abstract "Abstract"
	
	The University of Maryland team participated in four aspects of TREC-8: the ad hoc retrieval task, the main task in the cross-language retrieval (CLIR) track, the question answering track, and the routing task in the filtering track. The CLIR method was based on Pirkola's method for Dictionary-based Query Translation, using freely available dictionaries. Broad-coverage parsing and rule-based matching was used for question answering. Routing was performed using Latent Semantic Indexing in profile space.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OardWLS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/OardWLS99,
		author = {Douglas W. Oard and Jianqiang Wang and Dekang Lin and Ian Soboroff},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Experiments at Maryland: CLIR, {QA} and Routing},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/umdtrec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OardWLS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DSO at TREC-8: A Hybrid Algorithm for the Routing Task

_Hwee Tou Ng, Huey Ting Ang, Wee Meng Soon_

- :fontawesome-solid-user-group: **Participant:** [dso](./participants.md#dso)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/DSO.pdf](http://trec.nist.gov/pubs/trec8/papers/DSO.pdf)
- :material-file-search: **Runs:** [dso99rt1](./runs.md#dso99rt1) | [dso99rt2](./runs.md#dso99rt2)

??? abstract "Abstract"
	
	In this paper, we describe a new hybrid algorithm that we used for the routing task at TREC-8. The algorithm combines the use of Rocchio's formula for term selection, and an improved variant of the perceptron learning algorithm for tuning the term weights. This algorithm is able to give good performance on TREC-8 test data. We also achieved a slight improvement in average uninterpolated precision by using Dynamic Feedback Optimization (DFO) as another weight tuning algorithm and combining the ranked list generated by DFO with that of perceptron.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NgAS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/NgAS99,
		author = {Hwee Tou Ng and Huey Ting Ang and Wee Meng Soon},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{DSO} at {TREC-8:} {A} Hybrid Algorithm for the Routing Task},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/DSO.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NgAS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PLIERS at TREC8

_Andrew MacFarlane, Stephen E. Robertson, Julie A. McCann_

- :fontawesome-solid-user-group: **Participant:** [city-pliers](./participants.md#city-pliers)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/pliers8.pdf](http://trec.nist.gov/pubs/trec8/papers/pliers8.pdf)
- :material-file-search: **Runs:** [plt8f1](./runs.md#plt8f1) | [plt8f2](./runs.md#plt8f2) | [plt8r1](./runs.md#plt8r1) | [plt8r2](./runs.md#plt8r2)

??? abstract "Abstract"
	
	The use of the PLIERS text retrieval system in TREC8 experiments is described. The tracks entered for are: Ad-Hoc, Filtering (Batch and Routing) and the Web Track (Large only). We describe both retrieval efficiency and effectiveness results for all these tracks. We also describe some preliminary experiments with BM_25 tuning constant variation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacFarlaneRM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacFarlaneRM99,
		author = {Andrew MacFarlane and Stephen E. Robertson and Julie A. McCann},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{PLIERS} at {TREC8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/pliers8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacFarlaneRM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-8 Ad-Hoc, Query and Filtering Track Experiments using PIRCS

_K. L. Kwok, Laszlo Grunfeld, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf](http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf)
- :material-file-search: **Runs:** [pir9LF1](./runs.md#pir9lf1) | [pir9LF1a](./runs.md#pir9lf1a) | [pir9LF2](./runs.md#pir9lf2) | [pir9LF2a](./runs.md#pir9lf2a) | [pirc9BF1](./runs.md#pirc9bf1) | [pirc9BF2](./runs.md#pirc9bf2) | [pirc9R1](./runs.md#pirc9r1) | [pirc9R2](./runs.md#pirc9r2)

??? abstract "Abstract"
	
	In TREC-8, we participated in automatic ad-hoc retrieval as well as the query and filtering tracks. The theme of our participation is 'retrieval lists combination', and the technique is applied throughout our experiments to various degree. It is pointed out that our PIRCS system may be considered as a combination of probabilistic retrieval model and a language model approach. For ad-hoc, three types of experiments were done with short, medium and long queries as before. General approach is similar to TREC-7, but combination of retrieval lists from different query types were used to boost effectiveness. For query track, we submitted one short-query set, and performed retrieval for twenty one natural language query vairants. For filtering track, experiments for adaptive, batch filtering, and routing were performed. For adaptive, historical selected document list was used to train profile term weights and dynamically vary retrieval status value (rsv) threshold for deciding document selection during the course of filtering. For batch filtering, Financial Times FT92 data was used to define 6 retrieval profiles whose results were combined based on coefficients trained via a genetic algorithm. Logistic regression transforms rsv's to probabilities. Routing was similarly done with additional training data obtained from non-PT collections and two additional profiles were defined and combined
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGC99.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGC99,
		author = {K. L. Kwok and Laszlo Grunfeld and M. Chan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-8} Ad-Hoc, Query and Filtering Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/queenst8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGC99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Twenty-One at TREC-8: using Language Technology for Information  Retrieval

_Wessel Kraaij, Renée Pohlmann, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [twentyone](./participants.md#twentyone)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf](http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf)
- :material-file-search: **Runs:** [uttno8lf1](./runs.md#uttno8lf1) | [uttno8lf2](./runs.md#uttno8lf2) | [uttno8lf1f](./runs.md#uttno8lf1f) | [uttno8lf2f](./runs.md#uttno8lf2f) | [uttno8lf2p](./runs.md#uttno8lf2p) | [uttno8lf1p](./runs.md#uttno8lf1p)

??? abstract "Abstract"
	
	This paper describes the official runs of the Twenty-One group for TREC-8. The Twenty-One group participated in the Ad-hoc, CLIR, Adaptive Filtering and SDR tracks. The main focus of our experiments is the development and evaluation of retrieval methods that are motivated by natural language processing techniques. The following new techniques are introduced in this paper. In the Ad-Hoc and CLIR tasks we experimented with automatic sense disambiguation followed by query expansion or translation. We used a combination of thesaurial and corpus information for the disambiguation process. We continued research on CLIR techniques which exploit the target corpus for an implicit disambiguation, by importing the translation probabilities into the probabilistic term-weighting framework. In filtering we extended the the use of language models for document ranking with a relevance feedback algorithm for query term reweighting.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KraaijPH99.bib) "
	```
	@inproceedings{DBLP:conf/trec/KraaijPH99,
		author = {Wessel Kraaij and Ren{\'{e}}e Pohlmann and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Twenty-One at {TREC-8:} using Language Technology for Information Retrieval},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/twentyone8final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KraaijPH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on the TREC-8 Filtering Track

_Keiichiro Hoashi, Kazunori Matsumoto, Naomi Inoue, Kazuo Hashimoto_

- :fontawesome-solid-user-group: **Participant:** [kdd](./participants.md#kdd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/kddtrec8.pdf](http://trec.nist.gov/pubs/trec8/papers/kddtrec8.pdf)
- :material-file-search: **Runs:** [kdd8f003](./runs.md#kdd8f003) | [kdd8f002](./runs.md#kdd8f002) | [kdd8f001](./runs.md#kdd8f001)

??? abstract "Abstract"
	
	For this year's TREC, KDD R&D Laboratories focused on the adaptive filtering experiments of the Filtering Track. The main focus of our research was the development and evaluation of the profile updating algorithm. Our profile updating algorithm is based on the query expansion method based on word contribution [1][2]. Given manual feedback, our QE method has achieved high performance in the ad hoc track. Therefore, our hypothesis is that this method should work well in the filtering track. We will describe how we implemented this method to the filtering track, and analyze experiments. Our officially submitted results to TREC were generated from a system with a major bug. The results described in this notebook paper are based on the bug-fixed version of our system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HoashiMIH99.bib) "
	```
	@inproceedings{DBLP:conf/trec/HoashiMIH99,
		author = {Keiichiro Hoashi and Kazunori Matsumoto and Naomi Inoue and Kazuo Hashimoto},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments on the {TREC-8} Filtering Track},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/kddtrec8.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HoashiMIH99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filters, Webs and Answers: The University of Iowa TREC-8 Results

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [iowa](./participants.md#iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf](http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf)
- :material-file-search: **Runs:** [IOWAF993](./runs.md#iowaf993) | [IOWAF991](./runs.md#iowaf991) | [IOWAF992](./runs.md#iowaf992)

??? abstract "Abstract"
	
	The University of lowa attempted three tracks this year: filtering, question answering, and Web, the latter two new for us this year. All work was based upon that done for TREC-7 [2], with our system adapted for the specifics of the QA and Web tracks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS99,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Filters, Webs and Answers: The University of Iowa {TREC-8} Results},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/UIowa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure at trec8: Adhoc, Web, CLIR and Filtering tasks

_Mohand Boughanem, Christine Julien, Josiane Mothe, Chantal Soulé-Dupuy_

- :fontawesome-solid-user-group: **Participant:** [irit](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/irit.pdf](http://trec.nist.gov/pubs/trec8/papers/irit.pdf)
- :material-file-search: **Runs:** [Mer8BaLF1](./runs.md#mer8balf1) | [Mer8BaLF2](./runs.md#mer8balf2) | [Mer8BaNF1](./runs.md#mer8banf1) | [Mer8R1](./runs.md#mer8r1) | [Mer8R2](./runs.md#mer8r2)

??? abstract "Abstract"
	
	The tests performed for TREC8 were focused on automatic Adhoc, Web, Clir and Filtering (batch and routing) tasks. All the submitted runs were based on the Mercure system. Automatic adhoc : Four runs were submitted. All these runs were based on automatic relevance back-propagation used in the previous TREC, with a slight change for one of these runs (Mer8Adtd3). A strategy based on predicting the relevance of documents using the past relevant documents was tested for this run. More precisely, instead of using the same relevance value for all top retrieved documents, some of them are selected and have their relevance value boosted. Web : Four runs were submitted in this track: 1. content based only using Mercure simple search 2. content tilink, according to Mercure architecture, we consider that document nodes are linked each other by weighted links. The top selected documents resulting from the initial search spread their signals towards the other document nodes. The documents were then sorted according to their activations, the top 1000 documents were submitted. 3. (2) + pseudo-relevance back-propagation method. 4. reranking of the 40 top documents using their links between each others. Cross-language : Three runs were submitted for our first participation in this track. All these runs were based on query translation using an online machine translation . Two of these runs are a comparison between query translation from English to other languages and from French to other languages. Filtering - batch and routing: The profiles were learned using three different strategies : Relevance Back-propagation (RB) and Gradient Back-propagation (GB) used in the previous TREC and a new strategy based on Genetic Algorithm (GA). Four runs were submitted, two batch runs based on RB+GB and two routing runs, one based on RB+GB and the other one based on GA.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemJMS99.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemJMS99,
		author = {Mohand Boughanem and Christine Julien and Josiane Mothe and Chantal Soul{\'{e}}{-}Dupuy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure at trec8: Adhoc, Web, {CLIR} and Filtering tasks},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/irit.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemJMS99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY and TREC-8

_James Allan, James P. Callan, Fangfang Feng, Daniella Malin_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf](http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf)
- :material-file-search: **Runs:** [INQ610](./runs.md#inq610) | [INQ611](./runs.md#inq611) | [INQ612](./runs.md#inq612) | [INQ613](./runs.md#inq613)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CI IR) at the University of Massachusetts partic- ipated in seven of the tracks: ad-ho c, ltering, sp oken do cument retrieval, small web, large web, question and answer, and the query tracks. We sp ent signi cant time working on the ltering track, resulting in substantial p erformance improvement over TREC-7. For all of the other tracks, we used essentially the same system as used in previous years. In the next section, we describ e some of the basic pro cessing that was applied across most of the tracks. We then describ e the details for each of the tracks and in some cases present some mo dest analysis of the e ectiveness of our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCFM99.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCFM99,
		author = {James Allan and James P. Callan and Fangfang Feng and Daniella Malin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} and {TREC-8}},
		booktitle = {Proceedings of The Eighth Text REtrieval Conference, {TREC} 1999, Gaithersburg, Maryland, USA, November 17-19, 1999},
		series = {{NIST} Special Publication},
		volume = {500-246},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1999},
		url = {http://trec.nist.gov/pubs/trec8/papers/trec8-umass.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanCFM99.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

