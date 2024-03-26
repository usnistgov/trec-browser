# Proceedings - Fair Ranking 2020 

#### MacEwan University at the TREC 2020 Fair Ranking Track

_Brian Almquist_

- :fontawesome-solid-user-group: **Participant:** [MacEwan_Biz](./participants.md#macewan_biz)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/MacEwan_BIZ.FR.pdf](https://trec.nist.gov/pubs/trec29/papers/MacEwan_BIZ.FR.pdf)
- :material-file-search: **Runs:** [MacEwan-base](./runs.md#macewan-base) | [MacEwan-norm](./runs.md#macewan-norm)

??? abstract "Abstract"
	
	The MacEwan University School of Business submitted two runs for the TREC 2020 Fair Ranking Track. For this task, we indexed the document abstracts and the associated metadata from the provided Semantic Scholar dataset into a single Solr1 node using a standard Tokenizer chain. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Almquist20.bib) "
	```
	@inproceedings{DBLP:conf/trec/Almquist20,
		author = {Brian Almquist},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {MacEwan University at the {TREC} 2020 Fair Ranking Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/MacEwan\_BIZ.FR.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Almquist20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Washington at TREC 2020 Fairness Ranking Track

_Yunhe Feng, Daniel Saelid, Ke Li, Chirag Shah, Ruoyuan Gao_

- :fontawesome-solid-user-group: **Participant:** [InfoSeeking](./participants.md#infoseeking)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/InfoSeeking.FR.pdf](https://trec.nist.gov/pubs/trec29/papers/InfoSeeking.FR.pdf)
- :material-file-search: **Runs:** [UW_bm25](./runs.md#uw_bm25) | [UW_Kr_r60g20c20](./runs.md#uw_kr_r60g20c20) | [UW_Kr_r25g25c50](./runs.md#uw_kr_r25g25c50) | [UW_Kr_r0g100c0](./runs.md#uw_kr_r0g100c0) | [UW_Kr_r0g0c100](./runs.md#uw_kr_r0g0c100) | [UW_t_bm25](./runs.md#uw_t_bm25) | [UW_Kt_r0g0c100](./runs.md#uw_kt_r0g0c100) | [UW_Kt_r25g25c50](./runs.md#uw_kt_r25g25c50) | [UW_Kt_r60g20c20](./runs.md#uw_kt_r60g20c20) | [UW_Kt_r80g10c10](./runs.md#uw_kt_r80g10c10)

??? abstract "Abstract"
	
	InfoSeeking Lab's FATE (Fairness Accountability Transparency Ethics) group at University of Washington participated in 2020 TREC Fairness Ranking Track. This report describes that track, assigned data and tasks, our group definitions, and our results. Our approach to bringing fairness in retrieval and re-ranking tasks with Semantic Scholar data was to extract various dimensions of author identity. These dimensions included gender and location. We developed modules for these extractions in a way that allowed us to plug them in for either of the tasks as needed. After trying different combinations of relative weights assigned to relevance, gender, and location information, we chose five runs for retrieval and five runs for re-ranking tasks. The results showed that our runs performed below par for re-ranking task, but above average for retrieval
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FengSLSG20.bib) "
	```
	@inproceedings{DBLP:conf/trec/FengSLSG20,
		author = {Yunhe Feng and Daniel Saelid and Ke Li and Chirag Shah and Ruoyuan Gao},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Washington at {TREC} 2020 Fairness Ranking Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/InfoSeeking.FR.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FengSLSG20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Balancing Exposure and Relevance in Academic Search

_Andres Ferraro, Lorenzo Porcaro, Xavier Serra_

- :fontawesome-solid-user-group: **Participant:** [MTG](./participants.md#mtg)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/MTG.FR.pdf](https://trec.nist.gov/pubs/trec29/papers/MTG.FR.pdf)
- :material-file-search: **Runs:** [LM-relevance](./runs.md#lm-relevance) | [Deltr-gammas](./runs.md#deltr-gammas) | [LM-relev-year](./runs.md#lm-relev-year) | [LM-rel-year-100](./runs.md#lm-rel-year-100) | [LM-rel-groups](./runs.md#lm-rel-groups)

??? abstract "Abstract"
	
	The TREC 2020 Fair Ranking Track focuses on the evaluation of retrieval systems according to how well they fairly rank academic papers. The evaluation metric considered estimates how much the ranked papers are relevant and fairly represent different groups of authors, groups unknown to the track's participants. In this paper, we present the three different solutions proposed by our team to the given problem. The first solution is built on a learning-to-rank model to predict how much the documents are relevant for a given query and modify the ranking based on this relevance and a randomization strategy. The second approach is also based on the relevance predicted by a learning-to-rank model, but it additionally selects the authors using categories defined by analyzing collaborations between authors. The third approach uses the DELTR framework, and it considers different categories of authors based on the corresponding H-class. The results show that the first approach gives the best performance, with the additional advantage that it does not require extra information about the authors.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FerraroPS20.bib) "
	```
	@inproceedings{DBLP:conf/trec/FerraroPS20,
		author = {Andres Ferraro and Lorenzo Porcaro and Xavier Serra},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Balancing Exposure and Relevance in Academic Search},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/MTG.FR.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FerraroPS20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Naver Labs Europe at TREC 2020 Fair Ranking Track

_Till Kletti_

- :fontawesome-solid-user-group: **Participant:** [NLE](./participants.md#nle)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/NLE.FR.pdf](https://trec.nist.gov/pubs/trec29/papers/NLE.FR.pdf)
- :material-file-search: **Runs:** [NLE_TEXT_99_1](./runs.md#nle_text_99_1) | [NLE_META_99_1](./runs.md#nle_meta_99_1) | [NLE_META_9_1](./runs.md#nle_meta_9_1) | [NLE_META_PKL](./runs.md#nle_meta_pkl) | [NLE_TEXT_9_1](./runs.md#nle_text_9_1)

??? abstract "Abstract"
	
	In our participation to the TREC 2020 Fair Ranking Track, as Naver Labs Europe, we focused on the re-ranking task and we investigated the performance of a controller as a way to minimize unfairness over time, with minimal loss of utility. We used a two-step approach, based on (1) a relevance probability estimator, and (2) a controller that aims to bring the actual exposure close to the target exposure. This paper describes the components we designed in more detail. It contains a comparison of the performance of the controller to a baseline, which consists of a Plackett-Luce sampler. It also analyses the effect of the quality of the estimated relevance probabilities (closeness to the true binary relevance values) on the controller performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Kletti20.bib) "
	```
	@inproceedings{DBLP:conf/trec/Kletti20,
		author = {Till Kletti},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Naver Labs Europe at {TREC} 2020 Fair Ranking Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/NLE.FR.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Kletti20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team at the TREC 2020 Fair Ranking  Track

_Graham McDonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/uogTr.FR.pdf](https://trec.nist.gov/pubs/trec29/papers/uogTr.FR.pdf)
- :material-file-search: **Runs:** [UoGTrBComRel](./runs.md#uogtrbcomrel) | [UoGTrBComPro](./runs.md#uogtrbcompro) | [UoGTrBRel](./runs.md#uogtrbrel) | [UoGTrComRel](./runs.md#uogtrcomrel) | [UoGTrBComFu](./runs.md#uogtrbcomfu)

??? abstract "Abstract"
	
	In our participation to the TREC 2020 Fair Ranking Track, the University of Glasgow Terrier Team investigated a new approach for organically uncovering latent communities of authors that we wish to be fair to. Our deployed approach leverages a co-embedding model to jointly model a document's attributes, such as the document's authors, and the citation link graph of the documents in a collection, within a single embedding space. This network co-embedding is then used as input to a community detection approach that automatically updates the identified communities for each instance of a repeated query. Moreover, we experiment with two different ranking strategies to provide a fair exposure to different communities, and the authors within the communities, over time. Our first ranking strategy is inspired by the concepts of coverage and novelty from search results diversification, while our second ranking strategy leverages a data fusion approach for prioritising different communities over time.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McDonaldO20.bib) "
	```
	@inproceedings{DBLP:conf/trec/McDonaldO20,
		author = {Graham McDonald and Iadh Ounis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow Terrier Team at the {TREC} 2020 Fair Ranking Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/uogTr.FR.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/McDonaldO20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Maryland at the TREC 2020 Fair Ranking Track

_Mahmoud F. Sayed, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [UMD_IR](./participants.md#umd_ir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UMD_IR.FR.pdf](https://trec.nist.gov/pubs/trec29/papers/UMD_IR.FR.pdf)
- :material-file-search: **Runs:** [umd_relfair_ltr](./runs.md#umd_relfair_ltr)

??? abstract "Abstract"
	
	In this paper, we describe our submission to the second Fair Ranking Track at TREC 2020. We leverage the flexibility of listwise Learning to Rank (LtR) techniques which directly optimize towards a custom evaluation measure. To do this, we developed an objective function that balances between relevance and fairness
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SayedO20.bib) "
	```
	@inproceedings{DBLP:conf/trec/SayedO20,
		author = {Mahmoud F. Sayed and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Maryland at the {TREC} 2020 Fair Ranking Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/UMD\_IR.FR.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SayedO20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

