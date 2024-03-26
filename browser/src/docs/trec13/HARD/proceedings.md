# Proceedings - HARD 2004 

#### HARD Track Overview in TREC 2004 - High Accuracy Retrieval from  Documents

_James Allan_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/HARD.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec13/papers/HARD.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The HARD track of TREC 2004 aims to improve the accuracy of information retrieval through the use of three techniques: (1) query metadata that better describes the information need, (2) focused and time-limited interaction with the searcher through “clarification forms”, and (3) incorporation of passage-level relevance judgments and retrieval. Participation in all three aspects of the track was excellent this year with about 10 groups trying something in each area. No group was able to achieve huge gains in effectiveness using these techniques, but some improvements were found and enthusiasm for the clarification forms (in particular) remains high. The track will run again in TREC 2005.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Allan04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Allan04,
		author = {James Allan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{HARD} Track Overview in {TREC} 2004 - High Accuracy Retrieval from Documents},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/HARD.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Allan04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers' HARD Track Experiences at TREC 2004

_Nicholas J. Belkin, I. Chaleva, Michael J. Cole, Yuelin Li, Lu Liu, Ying-Hsang Liu, Gheorghe Muresan, Catherine L. Smith, Ying Sun, Xiaojun Yuan, Xiao-Min Zhang_

- :fontawesome-solid-user-group: **Participant:** [rutgers.belkin](./participants.md#rutgers.belkin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/rutgers-belkin.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/rutgers-belkin.hard.pdf)
- :material-file-search: **Runs:** [rutinb](./runs.md#rutinb) | [Rutleb](./runs.md#rutleb) | [Rutlet1](./runs.md#rutlet1) | [Rutlet2](./runs.md#rutlet2)

??? abstract "Abstract"
	
	The goal of our work in the HARD track was to test techniques for using knowledge about various aspects of the information seeker's context to improve IR system performance. We were particularly concerned with such knowledge which could be gained through implicit sources of evidence, rather than explicit questioning of the information seeker. We therefore did not submit any clarification form1, preferring to rely on the categories of supplied metadata concerning the user which we believed could, at least in principle, be inferred from user behavior, either in the past or during the current information seeking episode. The experimental condition of the HARD track was for each site to submit at least one baseline run for the set of 50 topics, using only the title and (optionally) description fields for query construction. The results of the baseline run(s) were compared with the results from one or more experimental runs, which made use of the supplied searcher metadata, and of a clarification form submitted to the searcher, asking for whatever information each site thought would be useful in improving search results. We used only the supplied metadata, for the reasons stated above, and especially because we were interested in how to make initial queries better, rather than in how to conduct a dialogue with a searcher. There were five categories of searcher metadata for each topic (not all topics had values for all five): Genre, Familiarity, Geography, Granularity and Related text(s), which were intended to represent aspects of the searcher's context which might be useful in tailoring retrieval to the individual, and the individual situation. We made the assumption that at least some of these categories would be available to the IR system prior to (or in conjunction with) the specific search session, either through explicit or implicit evidence. Therefore, for us the HARD track experimental condition was designed to test whether knowledge of these contextual characteristics, and our specific ways of using that knowledge, would result in better retrieval performance than a good IR system without such knowledge. We understood that there would be, in general, two ways in which to take account of the metadata. One would be to modify the initial query from the (presumed) searcher, before submitting it for search; the other would be to search with the initial query, and then to modify (i.e. re-rank) the results before showing them to the searcher. We used both, but mainly concentrated on the latter of these techniques in taking account of the different types of metadata.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinCCLLLMSSYZ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinCCLLLMSSYZ04,
		author = {Nicholas J. Belkin and I. Chaleva and Michael J. Cole and Yuelin Li and Lu Liu and Ying{-}Hsang Liu and Gheorghe Muresan and Catherine L. Smith and Ying Sun and Xiaojun Yuan and Xiao{-}Min Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Rutgers' {HARD} Track Experiences at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/rutgers-belkin.hard.pdf},
		timestamp = {Wed, 24 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BelkinCCLLLMSSYZ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2004 HARD Track Experiments in Clustering

_David A. Evans, Jeffrey Bennett, Jesse Montgomery, Victor Sheftel, David A. Hull, James G. Shanahan_

- :fontawesome-solid-user-group: **Participant:** [clairvoyance](./participants.md#clairvoyance)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/clairvoyance.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/clairvoyance.hard.pdf)
- :material-file-search: **Runs:** [CL102TDN](./runs.md#cl102tdn) | [CLAI2](./runs.md#clai2) | [CLAI1](./runs.md#clai1)

??? abstract "Abstract"
	
	The Clairvoyance team participated in the High Accuracy Retrieval from Documents (HARD) Track of TREC 2004, submitting three runs. The principal hypothesis we have been pursuing is that small numbers of documents in clusters can provide a better basis for relevance feedback than ranked lists or, alternatively, than top-N pseudo-relevance feedback (PRF). Clustering of a query response can yield one or more groups of documents in which there are “significant” numbers (greater than 30%) of relevant documents; we expect the best results when such groups are selected for feedback. Following up on work we began in our TREC-2003 HARD-Track experiments [Shanahan et al. 2004], therefore, we continued to explore approaches to clustering query response sets to concentrate relevant documents, with the goal of (a) providing users (assessors) with better sets of documents to judge and (b) making the choices among sets easier to evaluate. Our experiments, thus, focused primarily on exploiting assessor feedback through clarification forms for query expansion and largely ignored other features of the documents or metadata. One of the submitted runs was a baseline automatic ad-hoc retrieval run. It used pseudo-relevance feedback, but no assessor judgments. Two non-baseline runs contrasted alternative strategies for clustering documents in the response set of a topic—one based on simple re-grouping of responding documents (our “standard” approach using quintad pseudo-clusters) and another based on reprocessing of the response set into small sub-documents (passages) and then clustering. In both cases, the grouped documents were presented to assessors in evaluation forms and the groups of documents selected as being on topic were used as the source of query expansion terms. A third version of the response set, based on summaries of sub-document clusters, was also submitted to assessors, but not as an official run. Our standard approach, using simple re-grouping of documents into quintad pseudo-clusters, proved robust and most effective, giving above-median performance. However, our attempt at producing more concentrated clusters of relevant information by using small sub-documents instead of whole documents in clusters proved to be largely unsuccessful. Upon further analysis, this result seems to derive more from the apparent difficulty assessors may have had in judging such sub-document clusters and less from the actual quality of the clusters or our ranking of them. We attribute this failure to our inability to discovery the best methods (parameters) for clustering a response set and to the limitations in representing the results of response-set analysis through the rather rigid forms interface to assessors. In the following sections, we provide the details of our work. Section 2 presents our processing approach and experiments, including examples of the assessor forms we produced. Section 3 gives a brief summary of our results. Section 4 offers an analysis of our work from the point of view of our primary hypotheses. Section 5 gives concluding thoughts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EvansBMSHS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/EvansBMSHS04,
		author = {David A. Evans and Jeffrey Bennett and Jesse Montgomery and Victor Sheftel and David A. Hull and James G. Shanahan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2004 {HARD} Track Experiments in Clustering},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/clairvoyance.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EvansBMSHS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Robert Gordon University's HARD Track Experiments at TREC  2004

_David J. Harper, Gheorghe Muresan, Bicheng Liu, Ivan Koychev, Dietrich Wettschereck, Nirmalie Wiratunga_

- :fontawesome-solid-user-group: **Participant:** [robert.gordon.u](./participants.md#robert.gordon.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/robertgordonu.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/robertgordonu.hard.pdf)
- :material-file-search: **Runs:** [RGU0](./runs.md#rgu0) | [RGUE1](./runs.md#rgue1) | [RGUE5](./runs.md#rgue5) | [RGUE6](./runs.md#rgue6) | [RGUE10](./runs.md#rgue10)

??? abstract "Abstract"
	
	The High Accuracy Retrieval from Documents (HARD) track explores methods of improving the accuracy of document retrieval systems. As part of this track, the participants have investigated how information about a searcher's context can be used to improve retrieval performance [Allan, 2003; Allan, 2004]. Searchers, referred to as assessors in this track, produce TREC-style search topics. Additionally, assessors are asked to specify values from pre-defined categories of metadata, that relate to the context of the search, as opposed to the topic of the search. The categories and values of the metadata used for the HARD track in 2004 are: Desired genre of documents, with values news, opinion-editorial, other, and any. Desired geographic treatment, with values USA, non-USA, and any. (Documents satisfying the USA metadata value may also refer to non-USA geographic areas, and vice versa.) Assessor's familiarity with the topic, with values much and little (or equivalently high and low). One or more documents related to the topic, but not from the collection to be searched. Desired granularity of response, with values passage and document. The work reported in this paper focuses on exploiting the genre, geographic and familiarity metadata. We refer to the combination of metadata category and value, e.g. genre/news, as a meta-pair.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HarperMLKWW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/HarperMLKWW04,
		author = {David J. Harper and Gheorghe Muresan and Bicheng Liu and Ivan Koychev and Dietrich Wettschereck and Nirmalie Wiratunga},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Robert Gordon University's {HARD} Track Experiments at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/robertgordonu.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HarperMLKWW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improving Passage Retrieval Using Interactive Elicition and Statistical  Modeling

_Daqing He, Dina Demner-Fushman, Douglas W. Oard, Damianos G. Karakos, Sanjeev Khudanpur_

- :fontawesome-solid-user-group: **Participant:** [u.md.best.umiacs](./participants.md#u.md.best.umiacs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/umd-jhu.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/umd-jhu.hard.pdf)
- :material-file-search: **Runs:** [UMDBLTFAIDF](./runs.md#umdbltfaidf) | [UMDBLTITDES](./runs.md#umdbltitdes) | [UMDBLITFLOC](./runs.md#umdblitfloc) | [UMDBLBRF](./runs.md#umdblbrf) | [UMAREXPR1](./runs.md#umarexpr1) | [UMAREXPR3](./runs.md#umarexpr3) | [UMAREXPR5](./runs.md#umarexpr5)

??? abstract "Abstract"
	
	The University of Maryland and Johns Hopkins University worked together in the 2004 High Accuracy Retrieval from Documents (HARD) track to explore design options for interactive passage retrieval systems. HARD assessors responded to clarification forms by (1) selecting additional search terms from an automatically constructed list of potentially discriminating terms, (2) selected relevant passages from an automatically constructed list of possibly relevant passages, and (3) entered additional search terms. Query expansion based on these three types of elicited information yielded statistically significant improvements in R-precision over baselines with and without blind relevance feedback. For topics that requested passages as answers, a preliminary analysis shows that statistical models for passage extent trained on HARD 2003 data yielded a significant improvement over a replication of the University of Maryland's HARD-2003 technique for passage extent determination, and the results of the new technique appear to generally be well above the median for HARD 2004 systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeDOKK04.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeDOKK04,
		author = {Daqing He and Dina Demner{-}Fushman and Douglas W. Oard and Damianos G. Karakos and Sanjeev Khudanpur},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Improving Passage Retrieval Using Interactive Elicition and Statistical Modeling},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/umd-jhu.hard.pdf},
		timestamp = {Sun, 22 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeDOKK04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2004: HARD and Genomics Tracks

_Xiangji Huang, Yan Rui Huang, Ming Zhong, Miao Wen_

- :fontawesome-solid-user-group: **Participant:** [york.u](./participants.md#york.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/yorku.hard.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/yorku.hard.geo.pdf)
- :material-file-search: **Runs:** [york04hb1](./runs.md#york04hb1) | [york04ha1](./runs.md#york04ha1) | [york04hm1](./runs.md#york04hm1) | [york04ha2](./runs.md#york04ha2) | [york04hm2](./runs.md#york04hm2)

??? abstract "Abstract"
	
	York University participated in HARD and Genomics tracks this year. For both tracks, we used Okapi BSS (basic search system) as the basis. Our experiments mainly focused on exploiting various methods for combining document and passage scores, new term weighting formulae and feedback methods for query expansion. For HARD track, we built two levels of indexes, and search against both indexes for each topic. Then we combine these two searches into one. For Genomics track, we used a new strategy to automatically expand search terms by using relevance feedback and combined retrieval results from different fields into the final result. We achieved good results on the HARD task and average results on the Genomics task. For the HARD passage level evaluation, the automatic run ‘yorku04ha1' obtained the best result (0.358) in terms of Bpref measure at 12K characters. The evaluation results show that Algorithm 1 is more effective than Algorithm 2 for the passage level retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangHZW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangHZW04,
		author = {Xiangji Huang and Yan Rui Huang and Ming Zhong and Miao Wen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2004: {HARD} and Genomics Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/yorku.hard.geo.pdf},
		timestamp = {Tue, 05 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangHZW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2004: Novelty and HARD

_Nasreen Abdul Jaleel, James Allan, W. Bruce Croft, Fernando Diaz, Leah S. Larkey, Xiaoyan Li, Mark D. Smucker, Courtney Wade_

- :fontawesome-solid-user-group: **Participant:** [u.mass](./participants.md#u.mass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/umass.novelty.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/umass.novelty.hard.pdf)
- :material-file-search: **Runs:** [UMassBaseSVM](./runs.md#umassbasesvm) | [UMassBaseRM3](./runs.md#umassbaserm3) | [UMassBaseQL](./runs.md#umassbaseql) | [UMassVPMM](./runs.md#umassvpmm) | [UMassRGG](./runs.md#umassrgg) | [UMassCVC](./runs.md#umasscvc) | [UMassCFC](./runs.md#umasscfc) | [UMassC2](./runs.md#umassc2) | [UMassCMC](./runs.md#umasscmc) | [UMassCFMC](./runs.md#umasscfmc) | [UMassF](./runs.md#umassf) | [UMassMerge](./runs.md#umassmerge) | [UMassC3](./runs.md#umassc3)

??? abstract "Abstract"
	
	For the TREC 2004 Novelty track, UMass participated in all four tasks. Although finding relevant sentences was harder this year than last, we continue to show marked improvements over the baseline of calling all sentences relevant, with a variant of tfidf being the most successful approach. We achieve 5-9% improvements over the baseline in locating novel sentences, primarily by looking at the similarity of a sentence to earlier sentences and focusing on named entities. For the High Accuracy Retrieval from Documents (HARD) track, we investigated the use of clarification forms, fixed- and variable-length passage retrieval, and the use of metadata. Clarification form results indicate that passage level feedback can provide improvements comparable to user supplied related-text for document evaluation and outperforms related-text for passage evaluation. Document retrieval methods without a query expansion component show the most gains from related-text. We also found that displaying the top passages for feedback outperformed displaying centroid passages. Named entity feedback resulted in mixed performance. Our primary findings for passage retrieval are that document retrieval methods performed better than passage retrieval methods on the passage evaluation metric of binary preference at 12,000 characters, and that clarification forms improved passage retrieval for every retrieval method explored. We found no benefit to using variable-length passages over fixed-length passages for this corpus. Our use of geography and genre metadata resulted in no significant changes in retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JaleelACDLLSW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/JaleelACDLLSW04,
		author = {Nasreen Abdul Jaleel and James Allan and W. Bruce Croft and Fernando Diaz and Leah S. Larkey and Xiaoyan Li and Mark D. Smucker and Courtney Wade},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2004: Novelty and {HARD}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/umass.novelty.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JaleelACDLLSW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIUC in HARD 2004–Passage Retrieval Using HMMs

_Jing Jiang, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [u.illinois.uc](./participants.md#u.illinois.uc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uillinois-uc.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/uillinois-uc.hard.pdf)
- :material-file-search: **Runs:** [uiucHARDb0](./runs.md#uiuchardb0) | [uiucHARDb1](./runs.md#uiuchardb1) | [uiucHARDf0](./runs.md#uiuchardf0) | [uiucHARDf1](./runs.md#uiuchardf1) | [uiucHARDf2](./runs.md#uiuchardf2) | [uiucHARDf3](./runs.md#uiuchardf3)

??? abstract "Abstract"
	
	UIUC participated in the HARD track in TREC 2004 and focused on the evaluation of a new method for identifying variable-length passages using HMMs. Most existing approaches to passage retrieval rely on pre-segmentation of documents, but the optimal boundaries of a relevant passage depends on both the query and the document. Our new method aims at determining or improving the boundaries of a relevant passage based on both the query and topical coherence in the document. In this paper, we describe the method and present analysis of our HARD 2004 evaluation results. The results show that the HMM method can improve the boundaries of pre-segmented passages in terms of overall passage retrieval accuracy and recall, but at the price of precision sometimes. However, due to the non-optimality of the relevance feedback procedure and the poor ranking performance based on passage scoring, the best of our passage runs is still worse than a whole document baseline run. Further experiments and analysis are needed to fully understand why the language modeling approach did not work well on passage scoring.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangZ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangZ04,
		author = {Jing Jiang and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIUC} in {HARD} 2004--Passage Retrieval Using HMMs},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uillinois-uc.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangZ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of North Carolina's HARD Track Experiments at TREC  2004

_Diane Kelly, Vijay Deepak Dollu, Xin Fu_

- :fontawesome-solid-user-group: **Participant:** [u.northcarolina](./participants.md#u.northcarolina)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/unorthcarolina.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/unorthcarolina.hard.pdf)
- :material-file-search: **Runs:** [UNCHARDrun1](./runs.md#unchardrun1) | [UNCHARDq234](./runs.md#unchardq234) | [UNCHARDq2](./runs.md#unchardq2) | [UNCHARDtdn1](./runs.md#unchardtdn1) | [UNCHARDtdn2](./runs.md#unchardtdn2) | [UNCHARDq4](./runs.md#unchardq4) | [UNCHARDq3](./runs.md#unchardq3) | [UNCHARDq3q4](./runs.md#unchardq3q4) | [UNCHARDq2q3](./runs.md#unchardq2q3) | [UNCHARDq2q4](./runs.md#unchardq2q4) | [UNCHARDq2m](./runs.md#unchardq2m) | [UNCHARDq2q3m](./runs.md#unchardq2q3m) | [UNCHARDq234m](./runs.md#unchardq234m) | [UNCHARDq2q4m](./runs.md#unchardq2q4m) | [UNCHARDq3m](./runs.md#unchardq3m) | [UNCHARDq3q4m](./runs.md#unchardq3q4m) | [UNCHARDq4m](./runs.md#unchardq4m)

??? abstract "Abstract"
	
	In the experiment described in this paper, we investigate the effectiveness of a document-independent technique for eliciting additional information from searchers about their information problems. We propose that such a technique can be used to elicit terms for use in query expansion and as a follow-up when ambiguous queries are initially posed by searchers. We use a clarification form to obtain additional information from searchers and create a series of experimental runs based on the information that we obtained from this form. Although we were successful at eliciting more information from searchers, we were unable to demonstrate that this additional information increased performance because of an indexing error that resulted in very poor performance for our baseline and experimental runs. Additionally, we use our clarification form to investigate an alternative measure of topic familiarity and demonstrate how it relates to the length of searchers' topic descriptions and responses to our clarification form.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KellyDF04.bib) "
	```
	@inproceedings{DBLP:conf/trec/KellyDF04,
		author = {Diane Kelly and Vijay Deepak Dollu and Xin Fu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of North Carolina's {HARD} Track Experiments at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/unorthcarolina.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KellyDF04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Chicago at TREC 2004: HARD Track

_Gina-Anne Levow_

- :fontawesome-solid-user-group: **Participant:** [u.chichago](./participants.md#u.chichago)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uchichago.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/uchichago.hard.pdf)

??? abstract "Abstract"
	
	The University of Chicago participated in the Text Retrieval Conference 2004 (TREC 2004) HARD track. HARD track experiments focused on passage retrieval and exploitation of metadata information to increase accuracy under HARD-relevance criteria. Passage retrieval employed query-based repeated merger of 2-3 sentence pseudo-documents to extract tightly focused relevant passages. Lexical cues and statistical language modeling were applied to identify documents consistent with specified metadata criteria. Retrieval lists were reranked based on the quality of metadata match.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Levow04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Levow04,
		author = {Gina{-}Anne Levow},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Chicago at {TREC} 2004: {HARD} Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uchichago.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Levow04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Conceptual Language Models for Context-Aware Text Retrieval

_Henning Rode, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [utwente](./participants.md#utwente)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/utwente.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/utwente.hard.pdf)
- :material-file-search: **Runs:** [utwenteB421](./runs.md#utwenteb421) | [utwenteB21](./runs.md#utwenteb21) | [utwenteB111](./runs.md#utwenteb111) | [utwenteM111](./runs.md#utwentem111)

??? abstract "Abstract"
	
	While participating in the HARD track our first question was, what an IR-application should look like that takes into account preference meta-data from the user, without the need of explicit (manual) meta-data tagging of the collection. Especially, we touch the question how contextual information can be described in an abstract model appropriate for the IR-task, which further allows improving and fine-tuning of the context representations by learning from the user. As a first result, we roughly sketch a system architecture and context representation based on statistical language models that fits well to the task of the HARD track. Furthermore, we discuss issues of ranking and score normalizations on this background.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RodeH04.bib) "
	```
	@inproceedings{DBLP:conf/trec/RodeH04,
		author = {Henning Rode and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Conceptual Language Models for Context-Aware Text Retrieval},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/utwente.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RodeH04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ISCAS at TREC 2004: HARD Track

_Le Sun, Junlin Zhang, Yufang Sun_

- :fontawesome-solid-user-group: **Participant:** [cas.sun](./participants.md#cas.sun)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/cas-sun.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/cas-sun.hard.pdf)
- :material-file-search: **Runs:** [ISCAS](./runs.md#iscas) | [chastdn](./runs.md#chastdn) | [chascfw](./runs.md#chascfw) | [chascfd](./runs.md#chascfd) | [chascfwd](./runs.md#chascfwd) | [chasbsubfam](./runs.md#chasbsubfam) | [chasbcsubfam](./runs.md#chasbcsubfam) | [chascfsubfam](./runs.md#chascfsubfam) | [chasccsubfam](./runs.md#chasccsubfam) | [chasbaserel](./runs.md#chasbaserel) | [chasbasegen](./runs.md#chasbasegen) | [chasbaseger](./runs.md#chasbaseger) | [chascfrel](./runs.md#chascfrel) | [chascfgen](./runs.md#chascfgen) | [chascfger](./runs.md#chascfger) | [chasregenger](./runs.md#chasregenger) | [chasdcfd](./runs.md#chasdcfd) | [chasdcfwd](./runs.md#chasdcfwd) | [chasdcfw](./runs.md#chasdcfw)

??? abstract "Abstract"
	
	Institute of Software, Chinese Academy of Sciences (ISCAS) participated in TREC-2004, submitting 18 runs. We focus on studying the problem of the combination of the user- and query-information from clarification forms and metadata. We provided two kinds of Clarification Form. Our experiment shows the CF2 is more effective than CF1. We use Google as a resource for query expansion base on metadata subject and familiarity together, and the R-prec is increased from 0.2308 (baseline) to 0.2646 (+14.6%). Our approach to exploiting the metadata Genre and Geography yield negative result when used alone, however, surprisedly, when combinate metadata Genre and metadata Geography with CF2 respectively, we get an increase (+1.2%) and (+5.4%) than use CF2 alone. Our combination of CF2 and metadata relt_text is the best results of all the TREC runs (R-prec), and in this run, the R-prec is increased from 0.3303 (CF2 alone) to 0.3766 (+14%), and from 0.2888 (metadata rel-text alone) to 0.3766 (+30.4%). From the results we can see the information from user (CF2) and the information from query (metadata relt-text) may complement each other.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SunZS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SunZS04,
		author = {Le Sun and Junlin Zhang and Yufang Sun},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ISCAS} at {TREC} 2004: {HARD} Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/cas-sun.hard.pdf},
		timestamp = {Fri, 21 Aug 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SunZS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Approaches to High Accuracy Retrieval: Phrase-Based Search Experiments  in the HARD Track

_Olga Vechtomova, Murat Karamuftuoglu_

- :fontawesome-solid-user-group: **Participant:** [u.waterloo.vechtomova](./participants.md#u.waterloo.vechtomova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uwaterloo-bilkent.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/uwaterloo-bilkent.hard.pdf)
- :material-file-search: **Runs:** [UwatBaseTD](./runs.md#uwatbasetd) | [UwatBaseT](./runs.md#uwatbaset) | [UWATexp1](./runs.md#uwatexp1) | [UWATexp2](./runs.md#uwatexp2) | [UWATexp3](./runs.md#uwatexp3) | [UWATexp4](./runs.md#uwatexp4) | [UWATexp5](./runs.md#uwatexp5) | [UWATexp6](./runs.md#uwatexp6)

??? abstract "Abstract"
	
	Our main research focus this year was on the use of phrases (or multi-word units) in query expansion. Multi-word units (MWUs) comprise a number of lexical units, such as named entities (“United Nations”), nominal compounds (“amusement park”) and phrasal verbs (‘check in'). Although MWUs can belong to different parts of speech, our focus was on nominal MWUs. We used a combined syntactico-statistical approach for selecting nominal MWUs. In the first selection pass we obtained valid noun phrases, and in the second pass we used statistical measures to select strongly bound MWUs. We have experimented with using two statistical measures of selecting MWUs from text: the C-value (Frantzi and Ananiadou 1996, Vintar 2004) and the Log-Likelihood ratio (Dunning 1993). Selected MWUs were then suggested to the user for interactive query expansion. Two main research questions were studied in these experiments: Whether nominal MWUs which exhibit strong degree of stability in the corpus are better candidates for interactive query expansion than nominal MWUs selected by the frequency parameters of the individual terms they contain; Whether nominal MWUs are better candidates for interactive query expansion than single terms. In more detail these experiments are presented in section 2.2. The second focus of this work is on studying the effectiveness of noun phrases in document ranking. We have developed a new method of phrase-based document re-ranking, which addresses the problem of weighting overlapping phrases in documents, which in statistical IR models, such as probabilistic leads to the over-inflation of the document score. The method is described in detail in section 2.3.1. In section 3 we present the evaluation results, and in section 4 we discuss the differences in query expansion and retrieval performance between queries formulated by users with low and high familiarity with the topic.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VechtomovaK04.bib) "
	```
	@inproceedings{DBLP:conf/trec/VechtomovaK04,
		author = {Olga Vechtomova and Murat Karamuftuoglu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Approaches to High Accuracy Retrieval: Phrase-Based Search Experiments in the {HARD} Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uwaterloo-bilkent.hard.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VechtomovaK04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2004 Genomics, Hard, Robust and Web Tracks

_Kiduk Yang, Ning Yu, Adam Wead, Gavin La Rowe, Yu-Hsiu Li, Christopher Friend, Yoon Lee_

- :fontawesome-solid-user-group: **Participant:** [indiana.u.yang](./participants.md#indiana.u.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf](http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf)
- :material-file-search: **Runs:** [wdoqlz](./runs.md#wdoqlz) | [wdvqlz](./runs.md#wdvqlz) | [wdvqlz1](./runs.md#wdvqlz1) | [wdoqlz1](./runs.md#wdoqlz1) | [wdvqlzp](./runs.md#wdvqlzp) | [wdvqlzcf1](./runs.md#wdvqlzcf1)

??? abstract "Abstract"
	
	To facilitate understanding of information as well as its discovery, we need to combine the capabilities of the human and the machine as well as multiple methods and sources of evidence. Web Information Discovery Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science houses several projects that aim to apply this idea of multi-level fusion in the areas of information retrieval and knowledge organization. The TREC research group of WIDIT, who engages in examination of information retrieval strategies that can accommodate a variety of data environments and search tasks, participated in the Genomics, HARD, Robust, and Web tracks in TREC-2004. The basic approach of WIDIT was to leverage multiple sources of evidence, combine multiple methods, and integrate the strengths of man and the machine. Our main strategies for the tracks were: the use of gene name thesaurus in the Genomics track; query expansion and relevance feedback in the HARD track; query expansion with keywords from Web search in the Robust track, and the interactive system tuning process called “Dynamic Tuning” in the Web track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYWRLFL04.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYWRLFL04,
		author = {Kiduk Yang and Ning Yu and Adam Wead and Gavin La Rowe and Yu{-}Hsiu Li and Christopher Friend and Yoon Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2004 Genomics, Hard, Robust and Web Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf},
		timestamp = {Tue, 24 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangYWRLFL04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC 13: Web and Hard Tracks

_Hugo Zaragoza, Nick Craswell, Michael J. Taylor, Suchi Saria, Stephen E. Robertson_

- :fontawesome-solid-user-group: **Participant:** [microsoft.robertson](./participants.md#microsoft.robertson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/microsoft-cambridge.web.hard.pdf](http://trec.nist.gov/pubs/trec13/papers/microsoft-cambridge.web.hard.pdf)
- :material-file-search: **Runs:** [MSRCBaseline](./runs.md#msrcbaseline) | [MSRCh4SD](./runs.md#msrch4sd) | [MSRCh4SSnGBD](./runs.md#msrch4ssngbd) | [MSRCh4SSnGB](./runs.md#msrch4ssngb) | [MSRCh4SSnG](./runs.md#msrch4ssng) | [MSRCh4SSnB](./runs.md#msrch4ssnb) | [MSRCh4SSn](./runs.md#msrch4ssn) | [MSRCh4SGB](./runs.md#msrch4sgb) | [MSRCh4SG](./runs.md#msrch4sg)

??? abstract "Abstract"
	
	All our submissions from the Microsoft Research Cambridge (MSRC) team this year continue to explore issues in IR from a perspective very close to that of the original Okapi team, working first at City University of London, and then at MSRC. A summary of the contributions by the team, from TRECs 1 to 7 is presented in [3]. In this work, weighting schemes for ad-hoc retrieval were developed, inspired by a probabilistic interpretation of relevance; this lead, for instance, to the successful BM25 weighting function. These weighting schemes were extended to deal with pseudo relevance feedback (blind feedback). Furthermore, the Okapi team participated in most of the early interactive tracks, and also developed iterative relevance feedback strategies for the routing task. Following up on the routing work, TRECs 7-11 submissions dealt principally with the adaptive filtering task; this work is summarised in [5]. Last year MSRC entered only the HARD track, concentrating on the use of the clarification forms [6]. We hoped to make use of the query expansion methods developed for filtering in the context of feedback on snippets in the clarification forms. However, our methods were not very successful. In this year's TREC we took part in the HARD and WEB tracks. In HARD, we tried some variations on the process of feature selection for query expansion. On the WEB track, we investigated the combination of information from different content fields and from link-based features. Section 3 briefly describes the system we used. Section 4 describes our HARD participation and Section 5 our TREC participation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZaragozaCTSR04.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZaragozaCTSR04,
		author = {Hugo Zaragoza and Nick Craswell and Michael J. Taylor and Suchi Saria and Stephen E. Robertson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Cambridge at {TREC} 13: Web and Hard Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/microsoft-cambridge.web.hard.pdf},
		timestamp = {Tue, 04 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZaragozaCTSR04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

