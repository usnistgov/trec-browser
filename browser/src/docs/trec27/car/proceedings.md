# Proceedings - Complex Answer Retrieval 2018 

#### TREC Complex Answer Retrieval Overview

_Laura Dietz, Ben Gamari, Jeff Dalton, Nick Craswell_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/Overview-CAR.pdf](https://trec.nist.gov/pubs/trec27/papers/Overview-CAR.pdf)
??? abstract "Abstract"
	
	This notebook gives an overview of activities, datasets, and results of the second year of TREC Complex Answer Retrieval. We lay out the tasks offered and how provided datasets are automatically derived from Wikipedia and TQA. Manual relevance assessments are created by NIST. We describe the details of the assessment procedures, inter-annotator agreement, and statistics. Nine teams submitted runs exploring interactions of entities and passages, neural as well as traditional retrieval methods. We see that combining traditional methods with learning-to-rank can outperform neural methods, even when many training queries are available.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DietzG0C18.bib) "
	```
	@inproceedings{DBLP:conf/trec/DietzG0C18,
		author = {Laura Dietz and Ben Gamari and Jeff Dalton and Nick Craswell},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} Complex Answer Retrieval Overview},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/Overview-CAR.pdf},
		timestamp = {Tue, 21 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DietzG0C18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CUIS Team at TREC 2018 CAR Track

_Xinshi Lin, Wai Lam_

- :fontawesome-solid-user-group: **Participant:** [CUIS](./participants.md#cuis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/CUIS-CAR.pdf](https://trec.nist.gov/pubs/trec27/papers/CUIS-CAR.pdf)
- :material-file-search: **Runs:** [CUIS-F150](./runs.md#cuis-f150) | [CUIS-MX5](./runs.md#cuis-mx5) | [CUIS-Swift](./runs.md#cuis-swift) | [CUIS-dogeDodge](./runs.md#cuis-dogedodge) | [CUIS-XTS](./runs.md#cuis-xts)

??? abstract "Abstract"
	
	We participated in the Complex Answer Retrieval(CAR) Track at TREC 2018. We propose a Markov random field based framework concerning unigrams, bigrams and concepts from differnt query sections. Besides, we employ a language modelling framework facilitating the Wikipedia article information and query entity mentions. Our best passage run achieves NDCG@5 of 0.3503 and MAP of 0.1715.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinL18,
		author = {Xinshi Lin and Wai Lam},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CUIS} Team at {TREC} 2018 {CAR} Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/CUIS-CAR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Trec-CAR 2018: A Simple Unsupervised Semantic Query Expansion Model

_Robert Litschko, Federico Nanni, Goran Glavas_

- :fontawesome-solid-user-group: **Participant:** [DWS-UMA](./participants.md#dws-uma)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/DWS-UMA-CAR.pdf](https://trec.nist.gov/pubs/trec27/papers/DWS-UMA-CAR.pdf)
- :material-file-search: **Runs:** [DWS-UMA-SemqQueryExp](./runs.md#dws-uma-semqqueryexp) | [DWS-UMA-SemqQueryExp20](./runs.md#dws-uma-semqqueryexp20) | [DWS-UMA-SemqQueryExp30](./runs.md#dws-uma-semqqueryexp30) | [DWS-UMA-EntAspBM25none](./runs.md#dws-uma-entaspbm25none) | [DWS-UMA-EntAspQLrm](./runs.md#dws-uma-entaspqlrm)

??? abstract "Abstract"
	
	In this summary we present a simple and unsupervised Semantic Query Expansion model (SemQueryExp) for Complex Answer Retrieval (CAR). TREC CAR is a large-scale information retrieval shared evaluation task based on Wikipedia content. We have participated in the Passage Ranking Task of TREC CAR. Queries are provided as hierarchical section outlines and the goal is to retrieve the relevant paragraph, i.e., the original Wikipedia paragraphs of the respective section. The queries consist of the page title in which the section appears, the name of the main section and one or more sub-level sections (e.g., Thompson Capper // Early career // South African service). A section in turn contains a number of terms that we want to use in order to expand the query with semantically related terms. Here we rely on 300-dimensional GloVe [1] word embeddings, pre-trained on Wikipedia. For each word in the query we lookup its embedding, search for the k-nearest-neighbors and add the corresponding words to the query. Distances between word embeddings are measured with the cosine similarity. The final query consists now of its original query terms as well as the words added during query expansion. We assume that words appearing in lower sub-section levels, i.e. more specific sections, capture more relevance for the query than words appearing on higher levels such as the page title, which only describe the surrounding theme. This is encoded by assigning each query term a weight according to it's level in the hierarchical outline. If a word is in the title it receives a weight of 1, if it is in the main section it receives a weight of 2, etc. Expanded query terms are assumed to be noisy and scored with a value ranging between 0 and 1, depending on their cosine similarity. The final query consists of the union of all terms appearing in the outline and the expanded query terms, coupled with respective weights. All data is normalized by removing stop words and applying lemmatization. We execute the query on a Lucene index as a BoostedQuery using the BM25 retrieval model. We used no external data and we tuned the value of the parameter k on the benchmarkY1-train portion of the TREC CAR dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LitschkoNG18.bib) "
	```
	@inproceedings{DBLP:conf/trec/LitschkoNG18,
		author = {Robert Litschko and Federico Nanni and Goran Glavas},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Trec-CAR 2018: {A} Simple Unsupervised Semantic Query Expansion Model},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/DWS-UMA-CAR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LitschkoNG18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PACRR Gated Expansion for TREC CAR 2018

_Sean MacAvaney, Nazli Goharian, Ophir Frieder, Andrew Yates_

- :fontawesome-solid-user-group: **Participant:** [GUIR](./participants.md#guir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/GUIR-CAR.pdf](https://trec.nist.gov/pubs/trec27/papers/GUIR-CAR.pdf)
- :material-file-search: **Runs:** [guir](./runs.md#guir) | [guir-exp](./runs.md#guir-exp)

??? abstract "Abstract"
	
	In this work, we present our approach to the 2018 TREC Complex Answer Retrieval (CAR) task. We submitted two passage retrieval runs. The first uses the state-of-the-art technique from TREC CAR 2017: a modified neural ranker modified to incorporate query heading frequency information while performing term matching on each heading independently. The second run incorporates a novel gated technique for incorporating query expansion terms in a neural ranker. Our TREC runs indicate significant performance improvements can be achieved when using the expansion approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacAvaneyGFY18.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacAvaneyGFY18,
		author = {Sean MacAvaney and Nazli Goharian and Ophir Frieder and Andrew Yates},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{PACRR} Gated Expansion for {TREC} {CAR} 2018},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/GUIR-CAR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacAvaneyGFY18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UTD HLTRI at TREC 2018: Complex Answer Retrieval Track

_Ramón Maldonado, Sanda M. Harabagiu_

- :fontawesome-solid-user-group: **Participant:** [UTDHLTRI](./participants.md#utdhltri)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UTDHLTRI-CAR.pdf](https://trec.nist.gov/pubs/trec27/papers/UTDHLTRI-CAR.pdf)
- :material-file-search: **Runs:** [UTDHLTRI2](./runs.md#utdhltri2)

??? abstract "Abstract"
	
	Finding answers to complex questions within a corpus of Wikipedia paragraphs needs to account for (a) the similarity between questions and paragraphs as well as (b) their shared semantics. In our participation in the 2018 TREC CAR track, we focused on developing a novel neural paragraph ranking model in our existing CAPAR system, developed for the 2017 TREC CAR track. The new system TRANS-CAPAR, takes advantage of the recently introduced Transformer architecture to encode information from the question and to semantically decode it in each paragraph. The results obtained during the official evaluations indicate that TRANSCAPAR makes good use of both discourse context and similarity when ranking paragraphs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaldonadoH18.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaldonadoH18,
		author = {Ram{\'{o}}n Maldonado and Sanda M. Harabagiu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UTD} {HLTRI} at {TREC} 2018: Complex Answer Retrieval Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UTDHLTRI-CAR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MaldonadoH18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### New York University at TREC 2018 Complex Answer Retrieval Track

_Rodrigo Frassetto Nogueira, Kyunghyun Cho_

- :fontawesome-solid-user-group: **Participant:** [NYU-DL](./participants.md#nyu-dl)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/NYU-DL-CAR.pdf](https://trec.nist.gov/pubs/trec27/papers/NYU-DL-CAR.pdf)
- :material-file-search: **Runs:** [NYU-L](./runs.md#nyu-l) | [NYU-M](./runs.md#nyu-m) | [NYU-XL](./runs.md#nyu-xl)

??? abstract "Abstract"
	
	In this paper, we describe our submission to the TREC-CAR 2018. We use a method introduced by Nogueira et al. (2018) to efficiently learn diverse strategies in reinforcement learning for query reformulation and focus minimally on the ranking function. In this framework, an agent consists of multiple specialized sub-agents and a meta-agent that learns to aggregate the answers from sub-agents to produce a final answer. Sub-agents are trained on disjoint partitions of the training data, while the meta-agent is trained on the full training set. Our method makes learning faster, because it is highly parallelizable, and has better generalization performance than strong baselines, such as an ensemble of agents trained on the full data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NogueiraC18.bib) "
	```
	@inproceedings{DBLP:conf/trec/NogueiraC18,
		author = {Rodrigo Frassetto Nogueira and Kyunghyun Cho},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {New York University at {TREC} 2018 Complex Answer Retrieval Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/NYU-DL-CAR.pdf},
		timestamp = {Fri, 20 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NogueiraC18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREMA-UNH at TREC 2018: Complex Answer Retrieval and News Track

_Sumanta Kashyapi, Shubham Chatterjee, Jordan Ramsdell, Laura Dietz_

- :fontawesome-solid-user-group: **Participant:** [trema-unh](./participants.md#trema-unh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/TREMA-UNH-CAR-N.pdf](https://trec.nist.gov/pubs/trec27/papers/TREMA-UNH-CAR-N.pdf)
- :material-file-search: **Runs:** [UNH-p-mixed](./runs.md#unh-p-mixed) | [UNH-p-l2r](./runs.md#unh-p-l2r) | [UNH-p-sdm](./runs.md#unh-p-sdm) | [UNH-e-mixed](./runs.md#unh-e-mixed) | [UNH-e-graph](./runs.md#unh-e-graph) | [UNH-e-L2R](./runs.md#unh-e-l2r)

??? abstract "Abstract"
	
	This notebook describes the submission of team TREMA-UNH to the TREC Complex Answer Retrieval track and the TREC News track in 2018. Our methods focus on passage retrieval, entity-aware passage retrieval, and entity retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KashyapiCRD18.bib) "
	```
	@inproceedings{DBLP:conf/trec/KashyapiCRD18,
		author = {Sumanta Kashyapi and Shubham Chatterjee and Jordan Ramsdell and Laura Dietz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREMA-UNH} at {TREC} 2018: Complex Answer Retrieval and News Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/TREMA-UNH-CAR-N.pdf},
		timestamp = {Tue, 21 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KashyapiCRD18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2018: CAR, Common Core and News Tracks

_Shahrzad Naseri, John Foley, James Allan_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf](https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf)
- :material-file-search: **Runs:** [entityEmbedLambdaMart](./runs.md#entityembedlambdamart)

??? abstract "Abstract"
	
	UMass participated in three TREC tasks in 2018: the TREC CAR, TREC Core tasks and TREC News (Background Linking). In this paper we detail the contents of our submissions and our lessons learned from this year's participation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NaseriFA18.bib) "
	```
	@inproceedings{DBLP:conf/trec/NaseriFA18,
		author = {Shahrzad Naseri and John Foley and James Allan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UMass at {TREC} 2018: CAR, Common Core and News Tracks},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/UMass-CAR-CC-N.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NaseriFA18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

