# Proceedings - Fair Ranking 2022 

#### Overview of the TREC 2022 Fair Ranking Track

_Michael D. Ekstrand, Graham McDonald, Amifa Raj, Isaac Johnson_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/Overview_fair.pdf](https://trec.nist.gov/pubs/trec31/papers/Overview_fair.pdf)
??? abstract "Abstract"
	
	The TREC Fair Ranking Track aims to provide a platform for participants to develop and evaluate novel retrieval algorithms that can provide a fair exposure to a mixture of demographics or attributes, such as ethnicity, that are represented by relevant documents in response to a search query. For example, particular demographics or attributes can be represented by the documents' topical content or authors. The 2022 Fair Ranking Track adopted a resource allocation task. The task focused on supporting Wikipedia editors who are looking to improve the encyclopedia's coverage of topics under the purview of a WikiProject.1 WikiProject coordinators and/or Wikipedia editors search for Wikipedia documents that are in need of editing to improve the quality of the article. The 2022 Fair Ranking track aimed to ensure that documents that are about, or somehow represent, certain protected characteristics receive a fair exposure to the Wikipedia editors, so that the documents have an fair opportunity of being improved and, therefore, be well-represented in Wikipedia. The under-representation of particular protected characteristics in Wikipedia can result in systematic biases that can have a negative human, social, and economic impact, particularly for disadvantaged or protected societal groups [4, 7].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EkstrandMR022.bib) "
	```
	@inproceedings{DBLP:conf/trec/EkstrandMR022,
		author = {Michael D. Ekstrand and Graham McDonald and Amifa Raj and Isaac Johnson},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2022 Fair Ranking Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/Overview\_fair.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/EkstrandMR022.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT CIDDA IR at the TREC 2022 Fair Ranking Track

_Sachin Pathiyan Cherumanal, Marwah Alaofi, Reham Abdullah Altalhi, Elham Naghizade, Falk Scholer, Damiano Spina_

- :fontawesome-solid-user-group: **Participant:** [rmit_cidda_ir](./participants.md#rmit_cidda_ir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/rmit_cidda_ir.F.pdf](https://trec.nist.gov/pubs/trec31/papers/rmit_cidda_ir.F.pdf)
- :material-file-search: **Runs:** [rmit_cidda_ir_1](./runs.md#rmit_cidda_ir_1) | [rmit_cidda_ir_2](./runs.md#rmit_cidda_ir_2) | [rmit_cidda_ir_3](./runs.md#rmit_cidda_ir_3) | [rmit_cidda_ir_4](./runs.md#rmit_cidda_ir_4) | [rmit_cidda_ir_5](./runs.md#rmit_cidda_ir_5) | [rmit_cidda_ir_6](./runs.md#rmit_cidda_ir_6) | [rmit_cidda_ir_7](./runs.md#rmit_cidda_ir_7) | [rmit_cidda_ir_8](./runs.md#rmit_cidda_ir_8)

??? abstract "Abstract"
	
	This report describes the participation of the RMIT CIDDA IR1 group at the TREC 2022 Fair Ranking Track (Task 1). We submitted 8 runs with the aim to explore the role of explicit search result diversification, ranking fusion, and the use of a multi-criteria decision-making method to generate fair rankings considering multiple protected attributes.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CherumanalAANSS22.bib) "
	```
	@inproceedings{DBLP:conf/trec/CherumanalAANSS22,
		author = {Sachin Pathiyan Cherumanal and Marwah Alaofi and Reham Abdullah Altalhi and Elham Naghizade and Falk Scholer and Damiano Spina},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{RMIT} {CIDDA} {IR} at the {TREC} 2022 Fair Ranking Track},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/rmit\_cidda\_ir.F.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CherumanalAANSS22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Exploration of Learning-to-re-rank Using a Two-step Framework for  Fair Ranking

_Fumian Chen, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec31/papers/udel_fang.F.pdf](https://trec.nist.gov/pubs/trec31/papers/udel_fang.F.pdf)
- :material-file-search: **Runs:** [UDInfo_F_bm25](./runs.md#udinfo_f_bm25) | [UDInfo_F_mlp4](./runs.md#udinfo_f_mlp4) | [UDInfo_F_lgbm4](./runs.md#udinfo_f_lgbm4) | [UDInfo_F_mlp2](./runs.md#udinfo_f_mlp2) | [UDInfo_F_lgbm2](./runs.md#udinfo_f_lgbm2)

??? abstract "Abstract"
	
	As fairness has been attracting increasing attention in search engines, producing both fair and relevant rankings has become a major challenge for many information retrieval systems. In 2022, TREC fair ranking track launched an ad-hoc retrieval task for Wikipedia editors, which returns not only relevant documents of each query but also provides fair exposure to each document. The main goal of our participation in this track is to explore a fairness-aware two-step fair ranking framework using supervised learning-based re-rankers. Given a query, we first retrieve relevant documents and then use the re-ranker to re-rank the documents so that the final ranking is fair evaluated by the attention-weighted rank fairness (AWRF). We utilize the simple yet well-performed BM25 retrieval model to obtain relevant documents of each query. We tested a gradient-boosted tree-based (GBDT) LambdaMART model and a neural-based multilayer perceptron model. To better train the supervised learning models, we also extracted contextual-based features to augment our training data. We encoded fairness through a pre-processing method by constructing fairness scores. Our results also show the possibility of leveraging supervised learning-based re-rankers and contextual features.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenF22.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenF22,
		author = {Fumian Chen and Hui Fang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {An Exploration of Learning-to-re-rank Using a Two-step Framework for Fair Ranking},
		booktitle = {Proceedings of the Thirty-First Text REtrieval Conference, {TREC} 2022, online, November 15-19, 2022},
		series = {{NIST} Special Publication},
		volume = {500-338},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2022},
		url = {https://trec.nist.gov/pubs/trec31/papers/udel\_fang.F.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ChenF22.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

