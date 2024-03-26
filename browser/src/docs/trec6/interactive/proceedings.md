# Proceedings - Interactive 1997 

#### TREC-6 Interactive Report

_Paul Over_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/t6irep.ps.gz](http://trec.nist.gov/pubs/trec6/papers/t6irep.ps.gz)
??? abstract "Abstract"
	
	This report is an introduction to the work of the TREC-6 Interactive Track with its goal of investigating interactive information retrieval by examining the process as well as the results. Twelve interactive information retrieval (IR) systems were run on a shared problem: a question-answering task, 6 statements of information need, and a collection of 210,158 articles from the Financial Times of London 1991-1994. The track specification called for two levels of experimentation: cross-site system comparisons in terms of simple measures of end results and local experiments with their own hypotheses and attention to the search process. This report summarizes the cross-site experiment. It refers the reader to separate discussions of the experiments performed at each participating site - their hypotheses, experimental systems, and results. The cross-site experiment can be seen as a case study in the application of experimental design principles and the use of a shared control IR system in addressing the problems of comparing experimental interactive IR systems across sites: isolating the effects of topics, human searchers, and other site-specific factors within an affordable design. The cross-site results confirm the dominance of the topic effect, show the searcher effect is almost as often absent as present, and indicate that for several sites the 2-factor interactions are negligible. An analysis of variance found the system effect to be significant, but a multiple comparisons test found no significant pairwise differences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Over97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Over97,
		author = {Paul Over},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-6} Interactive Report},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {73--81},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/t6irep.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Over97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Retrieval using IRIS: TREC-6 Experiments

_Robert G. Sumner Jr., Kiduk Yang, Roger Akers, William M. Shaw Jr._

- :fontawesome-solid-user-group: **Participant:** [UNC-S](./participants.md#unc-s)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/unc-sumner.ps.gz](http://trec.nist.gov/pubs/trec6/papers/unc-sumner.ps.gz)
- :material-file-search: **Runs:** [Iunc](./runs.md#iunc)

??? abstract "Abstract"
	
	For the TREC-5, Category B adhoc task, we examined the effectiveness of two relevance feedback models: an adaptive linear model and a probabilistic model (Sumner & Shaw, 1997). The models were shown to be effective, especially when the relevance assessments of the searchers matched those of the official TREC judges. During feedback, the query was expanded by a large number of terms from the retrieved documents. Some queries were expanded by as many as 1000 terms. Building on the basic framework of our TREC-S system, we developed an interactive, Web-based retrieval system called IRIS (Information Retrieval Interactive System ) for TREC-6. Although IRIS inherits both the adaptive linear and the probabilistic model from the TREC-5 system, we made significant modifications to the implementation of both models in order to use a three-valued scale of relevance during feedback. Furthermore, we expanded the scope of human interaction with the system. For example, throughout the search process, the searcher can add and delete query terms as well as change their weights. Moreover, statistically significant, two-word collocations have been added to the term index. IRIS uses collocations not only in formulating the feedback query, but also in presenting to the searcher 'suggested phrases' (i.e., collocations related to the initial query), prior to the first document retrieval pass. Finally, as with our TREC-5 system, during feedback the query is expanded by a large number of terms. However, for reasons of efficiency, the number of terms in the query was limited to 300 in our TREC-6 system. The primary focus of our TREC-6 experiments was on the interactive track and the manual, Category B adhoc task. People were hired to conduct searches for these runs. Here, we are interested not only in the official TREC results but also (perhaps more so) in the reactions of the searchers to the various features of IRIS.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SumnerYAJ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/SumnerYAJ97,
		author = {Robert G. Sumner Jr. and Kiduk Yang and Roger Akers and William M. Shaw Jr.},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Interactive Retrieval using {IRIS:} {TREC-6} Experiments},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {711--733},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/unc-sumner.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SumnerYAJ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM Search UI Prototype Evaluation at the Interactive Track of  TREC-6

_Birgit Schmidt-Wesche, Robert Mack, Christian Lenz Cesar, David VanEsselstyn_

- :fontawesome-solid-user-group: **Participant:** [IBM-Brown](./participants.md#ibm-brown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ibm-interactive.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ibm-interactive.ps.gz)
- :material-file-search: **Runs:** [Iibm](./runs.md#iibm)

??? abstract "Abstract"
	
	Our search application used in the TREC6 Interactive Track was developed as part of a User-Centered Design (UCD) program aimed at prototyping Ul approaches for using different search technologies being investigated at IBM Research. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Schmidt-WescheMCV97.bib) "
	```
	@inproceedings{DBLP:conf/trec/Schmidt-WescheMCV97,
		author = {Birgit Schmidt{-}Wesche and Robert Mack and Christian Lenz Cesar and David VanEsselstyn},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{IBM} Search {UI} Prototype Evaluation at the Interactive Track of {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {517--534},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ibm-interactive.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Schmidt-WescheMCV97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Information Retrieval Using Term Relationship Networks

_Jim McDonald, William C. Ogden, Peter W. Foltz_

- :fontawesome-solid-user-group: **Participant:** [NMSU-C](./participants.md#nmsu-c)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/nmsu-interactive.ps.gz](http://trec.nist.gov/pubs/trec6/papers/nmsu-interactive.ps.gz)
- :material-file-search: **Runs:** [Inmsu](./runs.md#inmsu)

??? abstract "Abstract"
	
	Users have difficulty retrieving information from ad-hoc, textual databases because, by definition, they don't know precisely what's in them. Thus, users submit queries that contain the wrong terms or which don't contain enough information to retrieve all and only those documents relevant to their information needs. Our approach to these problems is to provide users with abstract representations of database con-tent, in the form of Pathfinder networks linking related terms used in the database. This allows users to recognize and select appropriate query terms. The networks displayed to users are derived from textual analyses of documents retrieved from initial queries and, thus, the process can be thought of as a form of relevance feedback. Compared to other relevance feedback methods, however, the network displays can show important relationships between the query terms and terms suggested by the system. In the study to be reported, we compared the performance of two information retrieval systems Zprise, a control system, and InfoView, a system that uses our network displays. Participants used both systems to perform an 'aspectual retrieval' task using the six topics. Preliminary results from this study suggest that when participants used InfoView they took less time to identify topic aspects and were at least as successful as when they used Zprise.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McDonaldOF97.bib) "
	```
	@inproceedings{DBLP:conf/trec/McDonaldOF97,
		author = {Jim McDonald and William C. Ogden and Peter W. Foltz},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Interactive Information Retrieval Using Term Relationship Networks},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {379--384},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/nmsu-interactive.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/McDonaldOF97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cheshire II at TREC 6: Interactive Probabilistic Retrieval

_Ray R. Larson, Jerome McDonough_

- :fontawesome-solid-user-group: **Participant:** [Berkeley](./participants.md#berkeley)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/brkly_interactive.ps.gz](http://trec.nist.gov/pubs/trec6/papers/brkly_interactive.ps.gz)
- :material-file-search: **Runs:** [Iberkeley](./runs.md#iberkeley)

??? abstract "Abstract"
	
	This paper briefly describes the features of the Cheshire II system and how it was used in the TREC 6 Interactive track. The results of the interactive track are discussed and future improvements to the Cheshire II system are considered.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LarsonM97.bib) "
	```
	@inproceedings{DBLP:conf/trec/LarsonM97,
		author = {Ray R. Larson and Jerome McDonough},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Cheshire {II} at {TREC} 6: Interactive Probabilistic Retrieval},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {649--659},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/brkly\_interactive.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LarsonM97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Comparison of Boolean and Natural Language Searching for the TREC-6  Interactive Task

_William R. Hersh, Bikram Day_

- :fontawesome-solid-user-group: **Participant:** [OHSU](./participants.md#ohsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ohsu.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ohsu.ps.gz)
- :material-file-search: **Runs:** [Iohsu](./runs.md#iohsu)

??? abstract "Abstract"
	
	The TREC-6 interactive task used a multi-site experimental protocol, where each participating site compared an 'experimental' system with a common 'control' system used at all sites. For the Oregon Health Sciences University site, the 'experimental' system was a Boolean interface to the MG system, while the control system was, as for all sites, the natural language ZPRISE system. Performance was measured by aspectual recall and precision. OHSU searchers did well overall, achieving the highest overall aspectual precision. These searchers did obtain below-average aspectual recall overall, although they achieved above-average aspectual recall with the control system, indicating that for the TREC-6 interactive task, a natural language searching system was superior to a Boolean one.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershD97.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershD97,
		author = {William R. Hersh and Bikram Day},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {A Comparison of Boolean and Natural Language Searching for the {TREC-6} Interactive Task},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {585--595},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ohsu.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HershD97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MDS TREC6 Report

_Michael Fuller, Marcin Kaszkiel, Chien Leng Ng, Phil Vines, Ross Wilkinson, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [MDS](./participants.md#mds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz](http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz)
- :material-file-search: **Runs:** [Irmit](./runs.md#irmit)

??? abstract "Abstract"
	
	This year the MDS group has participated in the ad hoc task, the Chinese task, the speech track, and the interactive track. It is our first year of participation in the speech and interactive tracks. We found the participation in both of these tracks of great benefit and interest.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FullerKNVWZ97.bib) "
	```
	@inproceedings{DBLP:conf/trec/FullerKNVWZ97,
		author = {Michael Fuller and Marcin Kaszkiel and Chien Leng Ng and Phil Vines and Ross Wilkinson and Justin Zobel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{MDS} {TREC6} Report},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {241--257},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/mds.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FullerKNVWZ97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The GURU System in TREC-6

_Eric W. Brown, Herb A. Chong_

- :fontawesome-solid-user-group: **Participant:** [IBM-Brown](./participants.md#ibm-brown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ibm_brown.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ibm_brown.ps.gz)
- :material-file-search: **Runs:** [Iibm](./runs.md#iibm)

??? abstract "Abstract"
	
	As the on-line world grows and increases its role in our daily lives, the problems of searching, categorizing, and understanding textual information become ever more important. While researchers and practitioners have made much progress in these areas over the last thirty years, anyone who has gone to the World Wide Web seeking information and returned with more frustration than answers can attest that much work remains. Today's important issues cover topics such as scalability, user interfaces, and techniques that exploit the unique hypermedia features of Web environments. To support our research in these areas, the Text Analysis and Advanced Search department at the IBM T. J. Watson Research Center has developed an experimental probabilistic text retrieval system called Guru[4]. Guru was originally built to explore new probabilistic ranking algorithms, and now serves as a test-bed for much of our text analysis, search, and categorization work. Guru may be run as a stand-alone system or in a client/server configuration. The Guru indexer performs minimal case and hyphen normalization, but otherwise indexes all words (including stop words) in their original form. The index includes document, paragraph, sentence, and word-in-sentence positional information for each word occurrence in the document collection. At search time, queries are input to Guru in a free-text format. Stop words are eliminated from the query and morphological variants for each query term are automatically generated and added as synonyms to the query term. Syntax is provided that allows the user to control morphological expansion and stop word elimination. Guru ranks documents using a probabilistic algorithm that considers the frequency statistics of the query terms in individual documents and the collection as a whole. Guru also considers lexical affinities (LAs), which are co-occurrences of two terms within a given distance. These automatically identified 'phrases' are ranked higher than instances of the component words occurring outside of the LA distance. Our purpose in participating in TREC-6 is four-fold. First, we continue to refine the base probabilistic ranking algorithm in Guru and wish to evaluate its performance on a large, standard test set. Second, we are developing a prototype user interface and seek initial feedback and guidance for further development. Third, we are interested in text search scalability as an issue orthogonal to the basic problems of search and categorization and seek feedback on initial attempts to address this issue. Fourth, hypermedia domains, such as the World Wide Web, are an increasingly important arena for application of text analysis and search technology. Such domains, however, pose a challenge for evaluation since both search and navigation must be considered by the evaluation metric. We hope that this issue will be addressed by the TREC community with the ultimate goal of defining appropriate evaluation metrics and building suitable test collections. Toward these ends, we are participating in the Ad-hoc Task, the Interactive Track, and the Very Large Corpus Track of TREC-6.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrownC97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrownC97,
		author = {Eric W. Brown and Herb A. Chong},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {GURU} System in {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {535--540},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ibm\_brown.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BrownC97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers' TREC-6 Interactive Track Experience

_Nicholas J. Belkin, Jose Perez Carballo, Colleen Cool, Shin-jeng Lin, Soyeon Park, Soo Young Rieh, Pamela A. Savage-Knepshield, C. Sikora, Hong (Iris) Xie, James Allan_

- :fontawesome-solid-user-group: **Participant:** [RutgersB](./participants.md#rutgersb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/ruint-paper2.ps.gz](http://trec.nist.gov/pubs/trec6/papers/ruint-paper2.ps.gz)
- :material-file-search: **Runs:** [Irutgers](./runs.md#irutgers)

??? abstract "Abstract"
	
	The goal of the Rutgers TREC-6 Interactive Track study was to compare the performance and usability of a system offering positive relevance feedback with one offering positive and negative relevance feedback. Our hypothesis was that the latter system would better support the aspect identification task than the former. Although aspectual recall was higher for the system supporting both kinds of relevance feedback (0.53 vs. 0.46), the difference was not significant, possibly because of the small number of subjects (four in each condition, each doing three searches). Usability results were also equivocal, perhaps due to the complexity of the system. Compared to ZPRISE, the control system without relevance feedback, both relevance feedback systems were rated more difficult to learn to use, but more effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinCCLPRSSXA97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinCCLPRSSXA97,
		author = {Nicholas J. Belkin and Jose Perez Carballo and Colleen Cool and Shin{-}jeng Lin and Soyeon Park and Soo Young Rieh and Pamela A. Savage{-}Knepshield and C. Sikora and Hong (Iris) Xie and James Allan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Rutgers' {TREC-6} Interactive Track Experience},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {597--610},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/ruint-paper2.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BelkinCCLPRSSXA97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Interactive Okapi at TREC-6

_Micheline Hancock-Beaulieu, Mike Gatford_

- :fontawesome-solid-user-group: **Participant:** [City](./participants.md#city)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/city-interactive.ps.gz](http://trec.nist.gov/pubs/trec6/papers/city-interactive.ps.gz)
- :material-file-search: **Runs:** [Icity](./runs.md#icity)

??? abstract "Abstract"
	
	A full description of the experimental system and conditions is given in Appendices A and B. Searchers filled in three types of questionnaires. The pre-session questionnaire established the user's experience and profile. In the post search questionnaires, searchers were asked questions regarding the topic, the search and the system used after undertaking each individual search. Finally in the post-session questionnaire, subjects were asked to provide an overview of the experiment. In addition to the questionnaires, searchers noted on a worksheet the different aspects of the topics they encountered whilst they undertook each search. A total of eight subjects completed forty eight searches, that is three searches on each of the two systems, Okapi and ZPrise. The sessions were divided into two rounds of four searchers. Of the two groups who carried out the twenty-four searches on Okapi, Group A used the same interface as in TREC-5, but with incremental query expansion modified (Appendix A.3.2), and Group B searched a slightly different version which allowed the searcher to cancel the relevance feedback process or clear the query (Appendix A.4).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BeaulieuG97.bib) "
	```
	@inproceedings{DBLP:conf/trec/BeaulieuG97,
		author = {Micheline Hancock{-}Beaulieu and Mike Gatford},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Interactive Okapi at {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {143--167},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/city-interactive.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BeaulieuG97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### INQUERY Does Battle With TREC-6

_James Allan, James P. Callan, W. Bruce Croft, Lisa Ballesteros, Donald Byrd, Russell C. Swan, Jinxi Xu_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz](http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz)
- :material-file-search: **Runs:** [Iumass](./runs.md#iumass)

??? abstract "Abstract"
	
	This year the Center for Intelligent Information Retrieval (CIIR) at the University of Massachusetts participated in eight of the ten tracks that were part of the TREC-6 workshop. We started with the two required tracks, ad-hoc and routing, but then included VLC, Filtering, Chinese, Cross-language, SDR, and Interactive. We omitted NLP and High Precision for want of time and energy. With so many tracks involved, it is nearly inevitable that something will go wrong. Despite our best efforts at verifying all aspects of each track-before, during, and after the experiments-we once again made mistakes that were minor in scope, but major in consequence. Those mistakes affected our results in Ad-hoc and Routing, as well as the dependent tracks of VLC and Filtering. The details of the mistakes are presented in each track's discussion, along with information comparing the submitted runs to the corrected runs. Unfortunately, those corrected runs are not included in TREC-6 summary information. This remainder of this report covers our approach to each of the tracks as well as some experimental results and analysis. We start with an overview of the major tools that were used across all tracks. The paper is divided into the following sections. The track descriptions are generally broken into approach, results, and analysis sections, though some tracks require a different description.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanCCBBSX97.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanCCBBSX97,
		author = {James Allan and James P. Callan and W. Bruce Croft and Lisa Ballesteros and Donald Byrd and Russell C. Swan and Jinxi Xu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{INQUERY} Does Battle With {TREC-6}},
		booktitle = {Proceedings of The Sixth Text REtrieval Conference, {TREC} 1997, Gaithersburg, Maryland, USA, November 19-21, 1997},
		series = {{NIST} Special Publication},
		volume = {500-240},
		pages = {169--206},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {1997},
		url = {http://trec.nist.gov/pubs/trec6/papers/umass-trec6.ps.gz},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AllanCCBBSX97.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

