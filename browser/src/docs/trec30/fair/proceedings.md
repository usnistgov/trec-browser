# Proceedings - Fair Ranking 2021 

#### Overview of the TREC 2021 Fair Ranking Track

_Michael D. Ekstrand, Amifa Raj, Graham McDonald, Isaac Johnson_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Overview-F.pdf](https://trec.nist.gov/pubs/trec30/papers/Overview-F.pdf)
??? abstract "Abstract"
	
	The TREC Fair Ranking Track aims to provide a platform for participants to develop and evaluate novel retrieval algorithms that can provide a fair exposure to a mixture of demographics or attributes, such as ethnicity, that are represented by relevant documents in response to a search query. For example, particular demographics or attributes can be represented by the documents' topical content or authors. The 2021 Fair Ranking Track adopted a resource allocation task. The task focused on supporting Wikipedia editors who are looking to improve the encyclopedia's coverage of topics under the purview of a WikiProject.1 WikiProject coordinators and/or Wikipedia editors search for Wikipedia documents that are in need of editing to improve the quality of the article. The 2021 Fair Ranking track aimed to ensure that documents that are about, or somehow represent, certain protected characteristics receive a fair exposure to the Wikipedia editors, so that the documents have an fair opportunity of being improved and, therefore, be well-represented in Wikipedia. The under-representation of particular protected characteristics in Wikipedia can result in systematic biases that can have a negative human, social, and economic impact, particularly for disadvantaged or protected societal groups [3, 5].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EkstrandRM021.bib) "
	```
	@inproceedings{DBLP:conf/trec/EkstrandRM021,
		author = {Michael D. Ekstrand and Amifa Raj and Graham McDonald and Isaac Johnson},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2021 Fair Ranking Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Overview-F.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/EkstrandRM021.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at TREC 2021 Fair Ranking Track

_Sachin Pathiyan Cherumanal, Damiano Spina, Falk Scholer, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [RMIT-IR](./participants.md#rmit-ir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/RMIT-IR-F.pdf](https://trec.nist.gov/pubs/trec30/papers/RMIT-IR-F.pdf)
- :material-file-search: **Runs:** [RMITRetRerank_2](./runs.md#rmitretrerank_2) | [RMITRetRerank_1](./runs.md#rmitretrerank_1) | [RMITRet](./runs.md#rmitret)

??? abstract "Abstract"
	
	This report describes the data, the assumptions, methodology, and our results involved in the participation at the TREC 2021 Fair Ranking Track. While most of the fairness-aware re-ranking techniques require explicitly defining protected attributes, we tried to leverage the implicit features of the Wikimedia articles by using an implicit diversification technique to study the impact of diversification on a fair ranking problem.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CherumanalSSC21.bib) "
	```
	@inproceedings{DBLP:conf/trec/CherumanalSSC21,
		author = {Sachin Pathiyan Cherumanal and Damiano Spina and Falk Scholer and W. Bruce Croft},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{RMIT} at {TREC} 2021 Fair Ranking Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/RMIT-IR-F.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CherumanalSSC21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TKB48 at TREC 2021 Fairness Ranking Track

_Zhuoqi Jin, Hideo Joho, Sumio Fujita_

- :fontawesome-solid-user-group: **Participant:** [TKB48](./participants.md#tkb48)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/TKB48-F.pdf](https://trec.nist.gov/pubs/trec30/papers/TKB48-F.pdf)
- :material-file-search: **Runs:** [RUN1](./runs.md#run1) | [RUN_task2](./runs.md#run_task2)

??? abstract "Abstract"
	
	Fairness ranking has been recently focused on, which aims to make ranking results fair while keeping relevant. The definition of fairness is diverse. TREC Fairness Ranking Track in 2021 took attention- weighted rank fairness (AWRF) [12] to fit the fairness aspect distribution of ranking results to a population estimator ^p reflecting the target distribution. TKB48's approach was a post-processing method. We obtained an initial ranking using the BM25 score. We then set a bucket for each of 7 geographic areas in the dataset, and iterated the initial BM25 ranking to choose documents and put them into the bucket in a round-robin manner. As the track evaluated the top 20 results of the final ranking, the goal for us was to make the distribution of each area be the same as the target distribution in the top 20 results. We defined the individual fairness score so that we could choose whether a document should be put into the bucket by comparing an individual fairness score and BM25 score. The individual fairness score was based on how many documents in a certain area has been put into the final ranking. We chose one document with the highest combined score of fairness and relevance for one iterate turn of initial ranking. And we iterated 1000 times so that we could get a final ranking with 1000 documents. Our results ranked fifth out of 13 submissions on the TREC Fairness Ranking Track. Finally, we compared the results of different methods on the TREC Fairness Ranking Track and analyzed it.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JinJF21.bib) "
	```
	@inproceedings{DBLP:conf/trec/JinJF21,
		author = {Zhuoqi Jin and Hideo Joho and Sumio Fujita},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TKB48} at {TREC} 2021 Fairness Ranking Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/TKB48-F.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JinJF21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at the TREC 2021 Fair Ranking Track

_Ali Vardasbi, Gabriel Bénédict, Shashank Gupta, Maria Heuss, Pooya Khandel, Ming Li, Fatemeh Sarvi_

- :fontawesome-solid-user-group: **Participant:** [IRLab-Amsterdam](./participants.md#irlab-amsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IRLab-Amsterdam-F.pdf](https://trec.nist.gov/pubs/trec30/papers/IRLab-Amsterdam-F.pdf)
- :material-file-search: **Runs:** [pl_control_0.6](./runs.md#pl_control_0.6) | [pl_control_0.8](./runs.md#pl_control_0.8) | [pl_control_0.92](./runs.md#pl_control_0.92) | [2step_pair_list](./runs.md#2step_pair_list) | [1step_pair_list](./runs.md#1step_pair_list) | [2step_pair](./runs.md#2step_pair) | [1step_pair](./runs.md#1step_pair) | [PL_IRLab_05](./runs.md#pl_irlab_05) | [PL_IRLab_07](./runs.md#pl_irlab_07)

??? abstract "Abstract"
	
	TREC 2021 fair ranking track is composed of two tasks, intended to help WikiProject coordinators, with a static ranking of 1000 pages (Task1), as well as WikiPedia editors, with a stochastic ranking of 50 pages (Task2). The rankings should be fair with respect to geographical locations as well as an undisclosed demographic attribute. We have used a lexical matching method to detect two demographic attributes, namely gender and sexuality. For the static ranker of Task1, we tried a method based on swapping the items that result in largest marginal gain for the relevance-fairness compound objective. We have seen that the greedy pairwise swapping method leads to better results compared to other variants. For the probabilistic ranker of Task2, we used two sampling approaches. The first one is based on an existing control-theory inspired algorithm, and it leads to the best overall performance among our submissions. The second approach uses a two-stage Plackett-Luce and achieves very good disparity performance (in terms of EE-D), but overall, its performance is dominated by the first approach due to its low ranking performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VardasbiB0HKLS21.bib) "
	```
	@inproceedings{DBLP:conf/trec/VardasbiB0HKLS21,
		author = {Ali Vardasbi and Gabriel B{\'{e}}n{\'{e}}dict and Shashank Gupta and Maria Heuss and Pooya Khandel and Ming Li and Fatemeh Sarvi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {The University of Amsterdam at the {TREC} 2021 Fair Ranking Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IRLab-Amsterdam-F.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/VardasbiB0HKLS21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

