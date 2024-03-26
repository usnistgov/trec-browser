# Proceedings - Web 2013 

#### TREC 2013 Web Track Overview

_Kevyn Collins-Thompson, Paul N. Bennett, Fernando Diaz, Charlie Clarke, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/WEB.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/WEB.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The goal of the TREC Web track is to explore and evaluate retrieval approaches over large-scale subsets of the Web - currently on the order of one billion pages. For TREC 2013, the fifth year of the Web track, we implemented the following significant updates compared to 2012. First, the Diversity task was replaced with a new Risk-sensitive retrieval task that explores the tradeoffs systems can achieve between effectiveness (overall gains across queries) and robustness (minimizing the probability of significant failure, relative to a provided baseline). Second, we based the 2013 Web track experiments on the new ClueWeb12 collection created by the Language Technologies Institute at Carnegie Mellon University. ClueWeb12 is a successor to the ClueWeb09 dataset, comprising about one billion Web pages crawled between Feb-May 2012.1 The crawling and collection process for ClueWeb12 included a rich set of seed URLs based on commercial search traffic, Twitter and other sources, and multiple measures for flagging undesirable content such as spam, pornography, and malware. The Adhoc task continued as in previous years. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Collins-Thompson13.bib) "
	```
	@inproceedings{DBLP:conf/trec/Collins-Thompson13,
		author = {Kevyn Collins{-}Thompson and Paul N. Bennett and Fernando Diaz and Charlie Clarke and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees},
		title = {{TREC} 2013 Web Track Overview},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/WEB.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Collins-Thompson13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI and TU Delft Notebook TREC 2013: Contextual Suggestion,  Federated Web Search, KBA, and Web Tracks

_Alejandro Bellogín, Gebrekirstos G. Gebremeskel, Jiyin He, Alan Said, Thaer Samar, Arjen P. de Vries, Jimmy Lin, Jeroen B. P. Vuurens_

- :fontawesome-solid-user-group: **Participant:** [CWI](./participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf](http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf)
- :material-file-search: **Runs:** [cwiwt13cps](./runs.md#cwiwt13cps) | [cwiwt13cpe](./runs.md#cwiwt13cpe) | [cwiwt13kld](./runs.md#cwiwt13kld)

??? abstract "Abstract"
	
	This paper provides an overview of the work done at the Centrum Wiskunde & Informatica (CWI) and Delft University of Technology (TU Delft) for different tracks of TREC 2013. We participated in the Contextual Suggestion Track, the Federated Web Search Track, the Knowledge Base Acceleration (KBA) Track, and the Web Ad-hoc Track. In the Contextual Suggestion track, we focused on filtering the entire ClueWeb12 collection to generate recommendations according to the provided user profiles and contexts. For the Federated Web Search track, we exploited both categories from ODP and document relevance to merge result lists. In the KBA track, we focused on the Cumulative Citation Recommendation task where we exploited different features to two classification algorithms. For the Web track, we extended an ad-hoc baseline with a proximity model that promotes documents in which the query terms are positioned closer together.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelloginGHSSVLV13.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelloginGHSSVLV13,
		author = {Alejandro Bellog{\'{\i}}n and Gebrekirstos G. Gebremeskel and Jiyin He and Alan Said and Thaer Samar and Arjen P. de Vries and Jimmy Lin and Jeroen B. P. Vuurens},
		editor = {Ellen M. Voorhees},
		title = {{CWI} and {TU} Delft Notebook {TREC} 2013: Contextual Suggestion, Federated Web Search, KBA, and Web Tracks},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BelloginGHSSVLV13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DLDE at web track: ad-hoc task

_Jie Chen, Zhendong Niu, Yulong Shi, Changmin Zhang, Weiyin Li_

- :fontawesome-solid-user-group: **Participant:** [DLDE](./participants.md#dlde)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/DLDE-web.pdf](http://trec.nist.gov/pubs/trec22/papers/DLDE-web.pdf)
- :material-file-search: **Runs:** [dlde](./runs.md#dlde)

??? abstract "Abstract"
	
	In this note paper, we report our experiment method at adhoc task of Web Track 2013. The goal of this task is to return a rank of documents order by relevance from a collection of static web pages. Our group used meta search to help query expansion as the first step, and then retrieved with the expansion query to get the search results and rerank them.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenNSZL13.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenNSZL13,
		author = {Jie Chen and Zhendong Niu and Yulong Shi and Changmin Zhang and Weiyin Li},
		editor = {Ellen M. Voorhees},
		title = {{DLDE} at web track: ad-hoc task},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/DLDE-web.pdf},
		timestamp = {Thu, 10 Jun 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ChenNSZL13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2013-Session and Web Track

_Matthias Hagen, Michael Völske, Jakob Gomoll, Marie Bornemann, Lene Ganschow, Florian Kneist, Abdul Hamid Sabri, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/webis-session-web.pdf](http://trec.nist.gov/pubs/trec22/papers/webis-session-web.pdf)
- :material-file-search: **Runs:** [webishybrid](./runs.md#webishybrid) | [webiswikibased](./runs.md#webiswikibased) | [webisnaive](./runs.md#webisnaive) | [webismixed](./runs.md#webismixed) | [webiswtbaseline](./runs.md#webiswtbaseline) | [webisrandom](./runs.md#webisrandom)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2013 Session and Web tracks. All our runs are on the full ClueWeb12 and use the online Indri retrieval system hosted at CMU. As for the session track, our runs implement three main ideas that were slightly improved compared to our participation in 2012: (1) distinguishing low risk sessions where we want to involve session knowledge in the form of a conservative query expansion strategy (only few expansion terms based on keywords from previous queries and seen/clicked documents/titles/snippets) from those where we don't, (2) conservative query expansion based on similar sessions from other users, (3) result list postprocessing to boost clicked documents of other users in similar sessions. As these techniques leave a lot of queries unchanged when not enough session knowledge is available, we do not expect large gains over all the sessions. As for the Web track, our runs exploit different strategies of segmenting the queries (i.e., identifying and highlighting concepts within the query as phrases to be contained in the results). Additionally to algorithmic segmentations based on our WWW 2011 and CIKM 2012 ideas, we had one run where we chose the segmentation according to a majority vote amongst five humans. In a last run, the results are constructed so as to be disjunct from the track's baseline's and our other runs' results. Instead, we populate the result list with documents that different segmentations of the query would return top-ranked or that are deeper in the ranking for segmentations already chosen in previous runs. The underlying idea was to obtain at least some judgments for the top documents that other segmentations would bring up in their rankings. As most of the queries are rather short, we expect only slight improvements or no effect at all from the different segmentation strategies that are tailored to longer and more verbose queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenVGBGKSS13.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenVGBGKSS13,
		author = {Matthias Hagen and Michael V{\"{o}}lske and Jakob Gomoll and Marie Bornemann and Lene Ganschow and Florian Kneist and Abdul Hamid Sabri and Benno Stein},
		editor = {Ellen M. Voorhees},
		title = {Webis at {TREC} 2013-Session and Web Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/webis-session-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenVGBGKSS13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Application of Data Fusion in the Web Track

_Chunlan Huang, Shengli Wu, Jinbo Feng, Yongquan Tao, Yuping Xing_

- :fontawesome-solid-user-group: **Participant:** [UJS](./participants.md#ujs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/jiangsu-web.pdf](http://trec.nist.gov/pubs/trec22/papers/jiangsu-web.pdf)
- :material-file-search: **Runs:** [UJS13LCRAd1](./runs.md#ujs13lcrad1) | [UJS13LCRAd2](./runs.md#ujs13lcrad2) | [UJS13Risk1](./runs.md#ujs13risk1) | [UJS13Risk2](./runs.md#ujs13risk2)

??? abstract "Abstract"
	
	In this paper, we report on the experiments we conducted whilst participating in the TREC 2013 Web track. We use data fusion to test how to improve the results from different information retrieval systems. Linear combination is used for fusion and multiple linear regression is used to obtain suitable weights for all the component systems involved. In our experiments, the ClueWeb09 dataset is used as training data to obtain weights for the three component systems Indri, MG4J, and Terrier. After running the official evaluation program, we find that all four runs submitted are better than all component results with one exception.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangWFTX13.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangWFTX13,
		author = {Chunlan Huang and Shengli Wu and Jinbo Feng and Yongquan Tao and Yuping Xing},
		editor = {Ellen M. Voorhees},
		title = {Application of Data Fusion in the Web Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/jiangsu-web.pdf},
		timestamp = {Wed, 08 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HuangWFTX13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Crowdsourcing for Robustness in Web Search

_Yubin Kim, Kevyn Collins-Thompson, Jaime Teevan_

- :fontawesome-solid-user-group: **Participant:** [MSR_Redmond](./participants.md#msr_redmond)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/MSR-web.pdf](http://trec.nist.gov/pubs/trec22/papers/MSR-web.pdf)
- :material-file-search: **Runs:** [msr_alpha10](./runs.md#msr_alpha10) | [msr_alpha5](./runs.md#msr_alpha5) | [msr_alpha1](./runs.md#msr_alpha1) | [msr_alpha0](./runs.md#msr_alpha0) | [msr_alpha0_95_4](./runs.md#msr_alpha0_95_4)

??? abstract "Abstract"
	
	Search systems are typically evaluated by averaging an effectiveness measure over a set of queries. However, this method does not capture the the robustness of the retrieval approach, as measured by its variability across queries. Robustness can be a critical retrieval property, especially in settings such as commercial search engines that must build user trust and maintain brand quality. This paper investigates two ways of integrating crowdsourcing into web search in order to increase robustness. First, we use crowd workers in query expansion; votes by crowd workers are used to determine candidate expansion terms that have broad coverage and high relatedness to query terms mitigating the risky nature of query expansion. Second, crowd workers are used to filter the top ranks of a ranked list in order to remove non-relevant documents. We find that these methods increase robustness in search results. In addition, we discover that different evaluation measures lead to different optimal parameter settings when optimizing for robustness; precision-oriented metrics favor safer parameter settings while recall-oriented metrics can handle riskier configurations that improve average performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KimCT13.bib) "
	```
	@inproceedings{DBLP:conf/trec/KimCT13,
		author = {Yubin Kim and Kevyn Collins{-}Thompson and Jaime Teevan},
		editor = {Ellen M. Voorhees},
		title = {Crowdsourcing for Robustness in Web Search},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/MSR-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KimCT13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2013: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Web Tracks

_Richard McCreadie, M-Dyaa Albakour, Stuart Mackie, Nut Limsopatham, Craig Macdonald, Iadh Ounis, Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf](http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf)
- :material-file-search: **Runs:** [uogTrAIwLmb](./runs.md#uogtraiwlmb) | [uogTrBDnLmxw](./runs.md#uogtrbdnlmxw) | [uogTrAS2Lb](./runs.md#uogtras2lb) | [uogTrBDnLaxw](./runs.md#uogtrbdnlaxw) | [uogTrADnLrb](./runs.md#uogtradnlrb) | [uogTrAS1Lb](./runs.md#uogtras1lb)

??? abstract "Abstract"
	
	In TREC 2013, we focus on tackling the challenges posed by the new Contextual Suggestion and Temporal summarisation tracks, as well as enhancing our existing technologies to tackle the new risk-sensitive aspect of the Web track, building upon our Terrier Information Retrieval Platform. In particular, for the Contextual Suggestion track, we investigate how to exploit location-based social networks, with the aim of better identifying venues within a city that a given user might be interested in visiting. For the Temporal Summarisation track, we propose a new summarisation framework and investigate novel techniques to adaptively alter the summarisation strategy over time. For the TREC Web track, we continue to build upon our learning-to-rank approaches and novel xQuAD / Fat frameworks within Terrier, increasing effectiveness when ranking and examining two new approaches to risk-sensitive retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieAMLMOD13.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieAMLMOD13,
		author = {Richard McCreadie and M{-}Dyaa Albakour and Stuart Mackie and Nut Limsopatham and Craig Macdonald and Iadh Ounis and Bekir Taner Din{\c{c}}er},
		editor = {Ellen M. Voorhees},
		title = {University of Glasgow at {TREC} 2013: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Web Tracks},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieAMLMOD13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Technion at TREC 2013 Web Track: Cluster-based Document Retrieval

_Fiana Raiber, Oren Kurland_

- :fontawesome-solid-user-group: **Participant:** [Technion](./participants.md#technion)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/technion-web.pdf](http://trec.nist.gov/pubs/trec22/papers/technion-web.pdf)
- :material-file-search: **Runs:** [clustmrfbf](./runs.md#clustmrfbf) | [clustmrfaf](./runs.md#clustmrfaf) | [mmrbf](./runs.md#mmrbf)

??? abstract "Abstract"
	
	Many cluster-based document retrieval methods have been proposed over the years. In our submissions to the ad hoc task of the TREC 2013 Web Track we experimented with one such highly effective method. Empirical results demonstrate the effectiveness of using our approach; specifically, with respect to other submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RaiberK13.bib) "
	```
	@inproceedings{DBLP:conf/trec/RaiberK13,
		author = {Fiana Raiber and Oren Kurland},
		editor = {Ellen M. Voorhees},
		title = {The Technion at {TREC} 2013 Web Track: Cluster-based Document Retrieval},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/technion-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RaiberK13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Universite de Montreal at TREC 2013: Experiments with Quantum Language  Models in the Web Track

_Alessandro Sordoni, Wei Yuan, Jian-Yun Nie_

- :fontawesome-solid-user-group: **Participant:** [diro_web_13](./participants.md#diro_web_13)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/diro-web.pdf](http://trec.nist.gov/pubs/trec22/papers/diro-web.pdf)
- :material-file-search: **Runs:** [udemQlm1l](./runs.md#udemqlm1l) | [udemQlm1lFb](./runs.md#udemqlm1lfb) | [udemQlm1lFbWiki](./runs.md#udemqlm1lfbwiki) | [udemQlml1FbR](./runs.md#udemqlml1fbr) | [udemQlml1R](./runs.md#udemqlml1r) | [udemFbWikiR](./runs.md#udemfbwikir)

??? abstract "Abstract"
	
	In TREC 2013, we focus on addressing the challenges posed by the Web track using our recently proposed Quantum Language Modeling (QLM) approach for IR [1]. QLM can be considered as a dependence model for IR for its capability of representing and integrating compound term dependencies into the scoring function. Among the main properties of the model, two of them make it stand out from the literature of existing dependence models (such as MRF [3]). First, QLM does not combine scores obtained from matching single terms and from matching compound dependencies, which makes it virtually parameterless. This is quite an appealing property for an IR system, especially when a new dataset such as ClueWeb12 is released and no previous training examples can be leveraged to fine-tune important parameters. The second peculiar feature of our model is its ability to automatically fallback onto the baseline bag-of-words score in the case that the required dependence relationship does not hold in the document. This is expected to bring improved robustness w.r.t. the baseline ranking. In the light of these considerations, the Web Track ad-hoc and robustness task seem the perfect testbeds for our model. In what follows we briefly review some of the theoretical background of QLM before delving into the description of the submitted runs and obtained results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SordoniYN13.bib) "
	```
	@inproceedings{DBLP:conf/trec/SordoniYN13,
		author = {Alessandro Sordoni and Wei Yuan and Jian{-}Yun Nie},
		editor = {Ellen M. Voorhees},
		title = {Universite de Montreal at {TREC} 2013: Experiments with Quantum Language Models in the Web Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/diro-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SordoniYN13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2013

_Yuanhai Xue, Feng Guan, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/ICTNET-web.pdf](http://trec.nist.gov/pubs/trec22/papers/ICTNET-web.pdf)
- :material-file-search: **Runs:** [ICTNET13ADR3](./runs.md#ictnet13adr3) | [ICTNET13RSR3](./runs.md#ictnet13rsr3) | [ICTNET13RSR2](./runs.md#ictnet13rsr2) | [ICTNET13ADR2](./runs.md#ictnet13adr2) | [ICTNET13ADR1](./runs.md#ictnet13adr1) | [ICTNET13RSR1](./runs.md#ictnet13rsr1)

??? abstract "Abstract"
	
	In this paper, we report our TREC experiments with both ad-hoc task and risk-sensitive task of Web Track 2013. The ClueWeb12 dataset and its derived data were used this year. We use BM25 model with term proximity, entity recognition and external resource to rank the final results. We submitted six runs which were not optimized for any particular metric.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XueGYLC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/XueGYLC13,
		author = {Yuanhai Xue and Feng Guan and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees},
		title = {{ICTNET} at Web Track 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/ICTNET-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XueGYLC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluating the Effectiveness of Axiomatic Approaches in Web Track

_Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/udel_fang-web.pdf](http://trec.nist.gov/pubs/trec22/papers/udel_fang-web.pdf)
- :material-file-search: **Runs:** [UDInfolabWEB1](./runs.md#udinfolabweb1) | [UDInfolabWEB1R](./runs.md#udinfolabweb1r) | [UDInfolabWEB2](./runs.md#udinfolabweb2) | [UDInfolabWEB2R](./runs.md#udinfolabweb2r)

??? abstract "Abstract"
	
	In this paper we describe our efforts for TREC 2013 Web track. We focus on evaluating the effectiveness of axiomatic retrieval model on large data collection. Axiomatic approach basically searches for the retrieval functions that satisfy some reasonable retrieval constraints. We also evaluate the semantic term matching method which does the query expansion by choosing the semantically related terms. Experiment results on adhoc task and diversity task demonstrate the effectiveness of the method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangF13a.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangF13a,
		author = {Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees},
		title = {Evaluating the Effectiveness of Axiomatic Approaches in Web Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/udel\_fang-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangF13a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mirex and Taily at TREC 2013

_Robin Aly, Djoerd Hiemstra, Dolf Trieschnigg, Thomas Demeester_

- :fontawesome-solid-user-group: **Participant:** [ut](./participants.md#ut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/lowlands-web-federated.pdf](http://trec.nist.gov/pubs/trec22/papers/lowlands-web-federated.pdf)
- :material-file-search: **Runs:** [ut22base](./runs.md#ut22base) | [ut22spam](./runs.md#ut22spam) | [ut22xact](./runs.md#ut22xact)

??? abstract "Abstract"
	
	We describe the participation of the Lowlands at the Web Track and the FedWeb track of TREC 2013. For the Web Track we used the Mirex Map-Reduce library with out-of-the-box approaches and for the FedWeb Track we adapted our shard selection method Taily for resource selection. Here, our results were above median and close to the maximum performance achieved.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlyHTD13.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlyHTD13,
		author = {Robin Aly and Djoerd Hiemstra and Dolf Trieschnigg and Thomas Demeester},
		editor = {Ellen M. Voorhees},
		title = {Mirex and Taily at {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/lowlands-web-federated.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlyHTD13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

