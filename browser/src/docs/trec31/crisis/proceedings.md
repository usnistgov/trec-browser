# Proceedings - CrisisFACTs 2022 

#### IRIT-IRIS at TREC 2022: CrisisFACTS Track

_Alexis Dusart, Gilles Hubert, Karen Pinel-Sauvagnat_

- :fontawesome-solid-user-group: **Participant:** [IRIT_IRIS](./participants.md#irit_iris)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/IRIT_IRIS.R.pdf](https://trec.nist.gov/pubs/trec31/papers/IRIT_IRIS.R.pdf)
- :material-file-search: **Runs:** [IRIT_IRIS_tssubert](./runs.md#irit_iris_tssubert) | [IRIT_IRIS_mean_USE_INeeds](./runs.md#irit_iris_mean_use_ineeds) | [IRIT_IRIS_mean_USE](./runs.md#irit_iris_mean_use)

??? abstract "Abstract"
	
	This paper presents the approaches proposed by the IRIS team of the IRIT laboratory for the TREC CrisisFACTS track. The CrisisFACTS track aims to summarize online data sources during crisis events. In our participation, we used neural language models according to three different strategies.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DusartHP22.bib) "
	```
	@inproceedings{DBLP:conf/trec/DusartHP22,
		author = {Alexis Dusart and Gilles Hubert and Karen Pinel{-}Sauvagnat},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{IRIT-IRIS} at {TREC} 2022: CrisisFACTS Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/IRIT\_IRIS.R.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DusartHP22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Neural Reranking and GPT-3 for Social Media Disaster Content  Summarization

_Jayr Alencar Pereira, Robson do Nascimento Fidalgo, Roberto de Alencar Lotufo, Rodrigo Frassetto Nogueira_

- :fontawesome-solid-user-group: **Participant:** [NM.unicamp](./participants.md#nm.unicamp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/NM.unicamp.R.pdf](https://trec.nist.gov/pubs/trec31/papers/NM.unicamp.R.pdf)
- :material-file-search: **Runs:** [NM-1](./runs.md#nm-1) | [NM-2](./runs.md#nm-2)

??? abstract "Abstract"
	
	Managing emergency events, such as natural disasters, necessitates real-time situational awareness for management teams. This paper presents a novel approach to obtaining accurate and comprehensive summaries of these events by utilizing a state-of-the-art open-source search engine and a large language model to retrieve and summarize information from social media and online news sources. The efficacy of this approach was evaluated on the TREC CrisisFACTS challenge dataset, utilizing automatic summarization metrics (e.g. Rouge-2 and BERTScore) and manual evaluation by the challenge organizers. Results indicate that while our approach achieves high comprehensiveness, it also exhibits a high degree of summary redundancy. Importantly, the pipeline components are few-shot, avoiding the need for training data collection and enabling rapid deployment.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PereiraFLN22.bib) "
	```
	@inproceedings{DBLP:conf/trec/PereiraFLN22,
		author = {Jayr Alencar Pereira and Robson do Nascimento Fidalgo and Roberto de Alencar Lotufo and Rodrigo Frassetto Nogueira},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Using Neural Reranking and {GPT-3} for Social Media Disaster Content Summarization},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/NM.unicamp.R.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PereiraFLN22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### L3S at the TREC 2022 CrisisFACTS Track

_Thi Huyen Nguyen, Koustav Rudra_

- :fontawesome-solid-user-group: **Participant:** [eXSum22](./participants.md#exsum22)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/eXSum22.R.pdf](https://trec.nist.gov/pubs/trec31/papers/eXSum22.R.pdf)
- :material-file-search: **Runs:** [eXSum22_submission_01](./runs.md#exsum22_submission_01) | [eXSum22_submission_02](./runs.md#exsum22_submission_02)

??? abstract "Abstract"
	
	This paper describes our proposed approach for the multi-stream summarization of the crisis-related events in the TREC 2022 CrisisFACTS track [2]. We apply a retrieval and ranking-based two-step summarization approach. First, we employ a sparse retrieval framework where content texts from multiple online streams are treated as a document corpus, and a term matching-based retrieval strategy is used to retrieve relevant contents, so-called facts, to the set of queries in a given event day. Next, we use several pre-trained models to measure semantic similarity between query-fact or fact-fact pairs, score and rank the facts for the extraction of daily event summaries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NguyenR22.bib) "
	```
	@inproceedings{DBLP:conf/trec/NguyenR22,
		author = {Thi Huyen Nguyen and Koustav Rudra},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{L3S} at the {TREC} 2022 CrisisFACTS Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/eXSum22.R.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NguyenR22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Deep Neural Reranking and Unsupervised Extraction for Multi-Query  Focused Summarization

_Philipp Seeberger, Korbinian Riedhammer_

- :fontawesome-solid-user-group: **Participant:** [ohm_kiz](./participants.md#ohm_kiz)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/ohm_kiz.R.pdf](https://trec.nist.gov/pubs/trec31/papers/ohm_kiz.R.pdf)
- :material-file-search: **Runs:** [BM25_QAcrisis_ILP](./runs.md#bm25_qacrisis_ilp) | [BM25_QAasnq_ILP](./runs.md#bm25_qaasnq_ilp) | [BM25_Heuristic_ILP](./runs.md#bm25_heuristic_ilp) | [ColBERT_ILP](./runs.md#colbert_ilp)

??? abstract "Abstract"
	
	The CrisisFACTS Track aims to tackle challenges such as multi-stream fact-finding in the domain of event tracking; participants' systems extract important facts from several disasterrelated events while incorporating the temporal order. We propose a combination of retrieval, reranking, and the well-known Integer Linear Programming (ILP) and Maximal Marginal Relevance (MMR) frameworks. In the former two modules, we explore various methods including an entity-based baseline, pre-trained and fine-tuned Question Answering systems, and ColBERT. We then use the latter module as an extractive summarization component by taking diversity and novelty criteria into account. The automatic scoring runs show strong results across the evaluation setups but also reveal shortcomings and challenges.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SeebergerR22.bib) "
	```
	@inproceedings{DBLP:conf/trec/SeebergerR22,
		author = {Philipp Seeberger and Korbinian Riedhammer},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Combining Deep Neural Reranking and Unsupervised Extraction for Multi-Query Focused Summarization},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/ohm\_kiz.R.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SeebergerR22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multi-Faceted Question Fusion in the TREC 2022 CrisisFACTS Track

_Nathaniel W. Rollings, Peter A. Rankel, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [umcp](./participants.md#umcp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/umcp.R.pdf](https://trec.nist.gov/pubs/trec31/papers/umcp.R.pdf)
- :material-file-search: **Runs:** [mrr_all](./runs.md#mrr_all) | [mrr_no_dd](./runs.md#mrr_no_dd) | [rr_now](./runs.md#rr_now) | [mrr_nobrf](./runs.md#mrr_nobrf) | [mrr_main](./runs.md#mrr_main) | [mrr_sum](./runs.md#mrr_sum) | [combsum](./runs.md#combsum)

??? abstract "Abstract"
	
	To address the challenges of multi-faceted questions in rapidly evolving environments, this paper introduces a system with an architecture based on recency-weighted and score-weighted reciprocal rank fusion of per-facet ranked lists. In the absence of existing data for parameter tuning, a small test collection built to support formative evaluation was developed and employed in system refinement. Issues of duplication were addressed through pruning near duplicates and, in one variation, synthesizing rather than simply selecting responses.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RollingsRO22.bib) "
	```
	@inproceedings{DBLP:conf/trec/RollingsRO22,
		author = {Nathaniel W. Rollings and Peter A. Rankel and Douglas W. Oard},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Multi-Faceted Question Fusion in the {TREC} 2022 CrisisFACTS Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/umcp.R.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RollingsRO22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

