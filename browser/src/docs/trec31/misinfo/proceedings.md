# Proceedings - Health Misinformation 2022 

#### CiTIUS at the TREC 2022 Health Misinformation Track

_Marcos Fernández-Pichel, Manuel de Prada Corral, David E. Losada, Juan Carlos Pichel_

- :fontawesome-solid-user-group: **Participant:** [CiTIUS](./participants.md#citius)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/CiTIUS.H.pdf](https://trec.nist.gov/pubs/trec31/papers/CiTIUS.H.pdf)
- :material-file-search: **Runs:** [citius.base](./runs.md#citius.base) | [citius.r1](./runs.md#citius.r1) | [citius.r2](./runs.md#citius.r2) | [citius.r3](./runs.md#citius.r3) | [citius.r4](./runs.md#citius.r4) | [citius.r5](./runs.md#citius.r5) | [citius.r6](./runs.md#citius.r6) | [citius.gpt-3](./runs.md#citius.gpt-3) | [citius.se](./runs.md#citius.se) | [citius.se_gpt](./runs.md#citius.se_gpt)

??? abstract "Abstract"
	
	The TREC Health Misinformation Track fosters the development of retrieval methods that promote credible and correct information over misinformation for health-related decision tasks. To make the procedure more realistic, an Answer Prediction challenge was added to this year's track. In these working notes, we describe our endeavours to estimate the correct response to each topic using search engine results and Transformer models. On the other hand, our adhoc retrieval solutions are based on new addons to our pipeline and the weighted fusion of signals.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Fernandez-Pichel22.bib) "
	```
	@inproceedings{DBLP:conf/trec/Fernandez-Pichel22,
		author = {Marcos Fern{\'{a}}ndez{-}Pichel and Manuel de Prada Corral and David E. Losada and Juan Carlos Pichel},
		editor = {Ian Soboroff and Angela Ellis},
		title = {CiTIUS at the {TREC} 2022 Health Misinformation Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/CiTIUS.H.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Fernandez-Pichel22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UWaterlooMDS at the TREC 2022 Health Misinformation Track

_Amir Vakili Tahami, Dake Zhang, Mark D. Smucker_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/UWaterlooMDS.H.pdf](https://trec.nist.gov/pubs/trec31/papers/UWaterlooMDS.H.pdf)
- :material-file-search: **Runs:** [WatS-MT5-MT5](./runs.md#wats-mt5-mt5) | [WatS-Bigbird2_75-MT5](./runs.md#wats-bigbird2_75-mt5) | [WatS-Bigbird2_75-MT5-TA2](./runs.md#wats-bigbird2_75-mt5-ta2) | [WatS-BB75-MT5-TA](./runs.md#wats-bb75-mt5-ta) | [WatS-manual-pred](./runs.md#wats-manual-pred) | [WatS-BM25-Query](./runs.md#wats-bm25-query) | [WatS-BM25-Question](./runs.md#wats-bm25-question) | [WatS-Trust](./runs.md#wats-trust) | [WatS-Trust-L1](./runs.md#wats-trust-l1) | [WatS-Trust-MT5](./runs.md#wats-trust-mt5) | [WatS-Trust-MT5-L1](./runs.md#wats-trust-mt5-l1) | [WatS-AP-Baseline](./runs.md#wats-ap-baseline) | [WatS-AP-Baseline-L1](./runs.md#wats-ap-baseline-l1) | [WatS-AP-MT5](./runs.md#wats-ap-mt5) | [WatS-AP-MT5-L1](./runs.md#wats-ap-mt5-l1) | [WatS-Bigbird2_75-MT5-TA1](./runs.md#wats-bigbird2_75-mt5-ta1) | [WatS-Manual](./runs.md#wats-manual) | [WatS-AP-Manual](./runs.md#wats-ap-manual)

??? abstract "Abstract"
	
	In this paper, we report our participation in the TREC 2022 Health Misinformation Track. With the aim to foster research on retrieval algorithms to promote correct information over misinformation for health-related queries, this year's track had two tasks: web retrieval and answer prediction. We reused our previous method with minor modifications to create our baselines. To overcome some limitations of our previous methods, we investigated a document-aware sentence-level passage extraction model based on the BigBird transformer. The upgraded pipeline with this model achieved our best automatic performance on the web retrieval task but failed to beat our baselines on the answer prediction task. Meanwhile, our manual runs still outperformed our automatic runs by great margins on both tasks, showing room for further improvements.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TahamiZS22.bib) "
	```
	@inproceedings{DBLP:conf/trec/TahamiZS22,
		author = {Amir Vakili Tahami and Dake Zhang and Mark D. Smucker},
		editor = {Ian Soboroff and Angela Ellis},
		title = {UWaterlooMDS at the {TREC} 2022 Health Misinformation Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/UWaterlooMDS.H.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/TahamiZS22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2022: Deep Learning and Health Misinformation

_Alexander Bondarenko, Maik Fröbe, Lukas Gienapp, Alexander Pugachev, Jan Heinrich Reimer, Ferdinand Schlatt, Ekaterina Artemova, Martin Potthast, Benno Stein, Pavel Braslavski, Matthias Hagen_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Webis.DH.pdf](https://trec.nist.gov/pubs/trec31/papers/Webis.DH.pdf)
- :material-file-search: **Runs:** [webis-goo-lbert-abs](./runs.md#webis-goo-lbert-abs) | [webis-nlm-lbert-abs](./runs.md#webis-nlm-lbert-abs) | [webis-goo-lbert-title-abs](./runs.md#webis-goo-lbert-title-abs) | [webis-goo-boolq-abs](./runs.md#webis-goo-boolq-abs) | [webis-nlm-boolq-abs](./runs.md#webis-nlm-boolq-abs) | [webis-longck-dis](./runs.md#webis-longck-dis) | [webis-uniqa-dis](./runs.md#webis-uniqa-dis) | [webis-verasent-dis](./runs.md#webis-verasent-dis) | [webis-longck-uniqa-dis](./runs.md#webis-longck-uniqa-dis) | [webis-longck-uniqa-ax-dis](./runs.md#webis-longck-uniqa-ax-dis) | [webis-uniqa-ax-lin](./runs.md#webis-uniqa-ax-lin) | [webis-uniqa-ax-pol](./runs.md#webis-uniqa-ax-pol) | [webis-uniqa-ax-com](./runs.md#webis-uniqa-ax-com) | [webis-longck-ax-lin](./runs.md#webis-longck-ax-lin) | [webis-longck-ax-pol](./runs.md#webis-longck-ax-pol) | [webis-longck-ax-com](./runs.md#webis-longck-ax-com) | [webis-longck-uniqa-ax-pol](./runs.md#webis-longck-uniqa-ax-pol) | [webis-longck-uniqa-ax-com](./runs.md#webis-longck-uniqa-ax-com) | [webis-longck-uniqa-pol](./runs.md#webis-longck-uniqa-pol) | [webis-longck-uniqa-ax-lin](./runs.md#webis-longck-uniqa-ax-lin)

??? abstract "Abstract"
	
	We describe the Webis group's participation in the TREC 2022 Deep Learning and Health Misinformation tracks. Our runs submitted to the Deep Learning track focus on improving the pairwise retrieval model duoT5 by combining a greedy aggregation algorithm with document augmentation. In the Health Misinformation track, our submissions to the Answer Prediction task exploit pre-trained question answering and claim verification models, whose input is extended by evidence information from PubMed abstracts. For the Web Retrieval task, we explore re-ranking based on the closeness of the predicted answers for each web document in the initial ranking to the predicted “true” answer of a topic's question.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001FGPRSAP0BH22.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001FGPRSAP0BH22,
		author = {Alexander Bondarenko and Maik Fr{\"{o}}be and Lukas Gienapp and Alexander Pugachev and Jan Heinrich Reimer and Ferdinand Schlatt and Ekaterina Artemova and Martin Potthast and Benno Stein and Pavel Braslavski and Matthias Hagen},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Webis at {TREC} 2022: Deep Learning and Health Misinformation},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Webis.DH.pdf},
		timestamp = {Tue, 29 Aug 2023 17:20:28 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001FGPRSAP0BH22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

