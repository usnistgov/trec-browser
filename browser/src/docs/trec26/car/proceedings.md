# Proceedings - Complex Answer Retrieval 2017 

#### TREC Complex Answer Retrieval Overview

_Laura Dietz, Manisha Verma, Filip Radlinski, Nick Craswell_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-CAR.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-CAR.pdf)
??? abstract "Abstract"
	
	The SWIRL 2012 workshop on frontiers, challenges, and opportunities for information retrieval report [1] noted many important challenges. Among them, challenges such as conversational answer retrieval, sub-document retrieval, and answer aggregation share commonalities: We desire answers to complex needs, and wish to find them in a single and well-presented source. Advancing the state of the art in this area is the goal of this TREC track. Consider a user investigating a new and unfamiliar topic. This user would often be best served with a single summary, rather than being required to synthesize his or her own summary from multiple sources. This is especially the case in mobile environments with restricted interaction capabilities. While these have led to extensive work on finding the best short answer, the target in this track is the retrieval of comprehensive answers that are composed of multiple text fragments from multiple sources. Retrieving high-quality longer answers is challenging as it is not sufficient to choose a lower rank-cutoff with the same techniques as for short answers. Instead, we need new approaches for finding relevant information in a complex answer space. Many examples of manually created complex answers exist on the Web. Famous examples are articles from how-stuff-works.com, travel guides, or fanzines. These are collections of articles, that each constitutes a long answer to an information need represented by the title of the article. The fundamental task of collecting references, facts, and opinions into a single coherent summary has traditionally been a manual process. We envision that automated information retrieval systems can relieve users from a large amount of manual work through sub-document retrieval, consolidation and organization. Ultimately, the goal is to retrieve synthesized information rather than documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DietzVRC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/DietzVRC17,
		author = {Laura Dietz and Manisha Verma and Filip Radlinski and Nick Craswell},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} Complex Answer Retrieval Overview},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-CAR.pdf},
		timestamp = {Tue, 21 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DietzVRC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at TREC2017 Complex Answer Retrieval Track

_Rui Cheng, Xiaomin Zhuang, Hao Yan, Yuanhai Xue, Zhihua Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ICTNET-CAR.pdf](https://trec.nist.gov/pubs/trec26/papers/ICTNET-CAR.pdf)
- :material-file-search: **Runs:** [treccarict](./runs.md#treccarict)

??? abstract "Abstract"
	
	Information retrieval (IR) is finding material (usually documents) of an unstructured nature (usually text) that satisfies an information need from within large collections (usually stored on computers) [1]. The most common and popular information retrieval application is web search engine such as Google[2], Baidu[3], Bing[4] and Sogou[5]. These application will return top-N best retrieval result to users. Information Retrieval systems for the Web, i.e., web search engines, are mainly devoted to finding relevant web documents in response to a user's query[6]. Current retrieval systems performance well in phrase-level retrieval tasks which provide simple fact and entity-centric needs. Complex Answer Retrieval Track is a new track in 2017, which requests a more complex and longer retrieval result to answer a query. It focuses on developing systems that are capable of answering complex information needs by collating relevant information from an entire corpus. Given an article stub Q, retrieval for each of its sections Hi, a ranking of relevant entity-passage tuples (E, P). Tow tasks are offered: passage ranking and entity ranking. This paper introduces an algorithm and a system for passage ranking. The retrieval queries are outlines which consist of titles and section titles of articles. The retrieval collection consists of paragraphs which are come from Wikipedia articles. We use the BM25 algorithm and develop a system to retrieval the top-100 most relevant paragraphs
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChengZYXYLC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChengZYXYLC17,
		author = {Rui Cheng and Xiaomin Zhuang and Hao Yan and Yuanhai Xue and Zhihua Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at {TREC2017} Complex Answer Retrieval Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/ICTNET-CAR.pdf},
		timestamp = {Fri, 19 May 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ChengZYXYLC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Contextualized PACRR for Complex Answer Retrieval

_Sean MacAvaney, Andrew Yates, Kai Hui_

- :fontawesome-solid-user-group: **Participant:** [MPIID5](./participants.md#mpiid5)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/MPIID5-CAR.pdf](https://trec.nist.gov/pubs/trec26/papers/MPIID5-CAR.pdf)
- :material-file-search: **Runs:** [mpii-nn6_pos_tprob](./runs.md#mpii-nn6_pos_tprob) | [mpii-nn4_pos_hperc](./runs.md#mpii-nn4_pos_hperc) | [mpii-nn6_pos](./runs.md#mpii-nn6_pos)

??? abstract "Abstract"
	
	In this work, we present our submission to the TREC Complex Answer Retrieval (CAR) task. Our approach uses a variation of the Position-Aware Convolutional Recurrent Relevance Matching (PACRR) [2] deep neural model to re-rank passages. Modifications include an expanded convolutional kernel size, and contextual vectors to capture heading type (e.g. title), heading frequency, and query term occurrence frequency. We submitted three runs for human relevance judgments by TREC varying which contextual vectors are included, and the number of negative samples used when training. Our approach yields a MAP of 0.241, R-Prec of 0.321, and MRR of 0.520 when using the term occurrence frequency run in the lenient evaluation environment.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacAvaneyYH17.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacAvaneyYH17,
		author = {Sean MacAvaney and Andrew Yates and Kai Hui},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Contextualized {PACRR} for Complex Answer Retrieval},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/MPIID5-CAR.pdf},
		timestamp = {Tue, 15 Mar 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacAvaneyYH17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UTD HLTRI at TREC 2017: Complex Answer Retrieval Track

_Ramón Maldonado, Stuart J. Taylor, Sanda M. Harabagiu_

- :fontawesome-solid-user-group: **Participant:** [UTDHLTRI](./participants.md#utdhltri)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UTDHLTRI-CAR.pdf](https://trec.nist.gov/pubs/trec26/papers/UTDHLTRI-CAR.pdf)
- :material-file-search: **Runs:** [UTDHLTRINN20](./runs.md#utdhltrinn20) | [UTDHLTRINN50](./runs.md#utdhltrinn50) | [UTDHLTRIAR](./runs.md#utdhltriar)

??? abstract "Abstract"
	
	This paper presents our Complex Answer PAragraph Retrieval (CAPAR) system designed for our participation in the TREC Complex Answer Retrieval (CAR) track. Because we were provided with a massive training set consisting of complex questions as well as the paragraphs that answered each aspect of the complex question, we cast the paragraph ranking as a learning to rank (L2R) problem, such that we can produce optimal results at testing time. We considered two alternative Learning to Rank (L2R) approaches for obtaining the relevance scores of each paragraph: (1) the Siamese Attention Network (SANet) for Pairwise Ranking and (2) AdaRank. The evaluation results obtained for CAPAR revealed that the Siamese Attention Network (SANet) for Pairwise Ranking outperformed AdaRank as the L2R approach for CAPAR.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaldonadoTH17.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaldonadoTH17,
		author = {Ram{\'{o}}n Maldonado and Stuart J. Taylor and Sanda M. Harabagiu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UTD} {HLTRI} at {TREC} 2017: Complex Answer Retrieval Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UTDHLTRI-CAR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MaldonadoTH17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

