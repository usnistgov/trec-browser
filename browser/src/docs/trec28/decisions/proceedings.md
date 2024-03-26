# Proceedings - Decision 2019 

#### UWaterlooMDS at the TREC 2019 Decision Track

_Mustafa Abualsaud, Fuat Can Beylunioglu, Mark D. Smucker, P. Robert Duimering_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UWaterlooMDS.D.pdf](https://trec.nist.gov/pubs/trec28/papers/UWaterlooMDS.D.pdf)
- :material-file-search: **Runs:** [UWaterMDS_BM25](./runs.md#uwatermds_bm25) | [UWatMDSBM25_HC1](./runs.md#uwatmdsbm25_hc1) | [UWatMDSBM25_HC2](./runs.md#uwatmdsbm25_hc2) | [UWatMDSBM25_HC3](./runs.md#uwatmdsbm25_hc3) | [UWatMDS_BM25_ZS](./runs.md#uwatmds_bm25_zs) | [UWatMDS_BM25_Z](./runs.md#uwatmds_bm25_z) | [UWatMDS_BMZBS10](./runs.md#uwatmds_bmzbs10) | [UWatMDS_BMF_C90](./runs.md#uwatmds_bmf_c90) | [UWatMDS_BMF_C95](./runs.md#uwatmds_bmf_c95) | [UWatMDS_BMF_S30](./runs.md#uwatmds_bmf_s30)

??? abstract "Abstract"
	
	In this report, we discuss the experiments we conducted for the TREC 2019 Decision Track. This year, our goal was to investigate the effect of document credibility on the quality of automatic runs. To address credibility, we combined scores from a spam classifier and a credibility classifier trained to detect non-trustworthy websites. The results from both classifiers were then used to modify a baseline BM25 ranking. In addition to the automatic runs, we also submitted manual runs using the HiCAL [2] system. Our manual runs modify a baseline BM25 ranking using manually judged documents found using the system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbualsaudBSD19.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbualsaudBSD19,
		author = {Mustafa Abualsaud and Fuat Can Beylunioglu and Mark D. Smucker and P. Robert Duimering},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UWaterlooMDS at the {TREC} 2019 Decision Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UWaterlooMDS.D.pdf},
		timestamp = {Mon, 31 Jul 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbualsaudBSD19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2019: Decision Track

_Alexander Bondarenko, Maik Fröbe, Vaibhav Kasturia, Matthias Hagen, Michael Völske, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/Webis.D.pdf](https://trec.nist.gov/pubs/trec28/papers/Webis.D.pdf)
- :material-file-search: **Runs:** [webisMSame1](./runs.md#webismsame1) | [webisMSame2](./runs.md#webismsame2) | [webisMSame3](./runs.md#webismsame3) | [webisMSame4](./runs.md#webismsame4) | [webisMSame5](./runs.md#webismsame5) | [webisTSame1](./runs.md#webistsame1) | [webisMMajority1](./runs.md#webismmajority1) | [webisTMajority1](./runs.md#webistmajority1) | [webisMAll1](./runs.md#webismall1) | [webisTAll1](./runs.md#webistall1)

??? abstract "Abstract"
	
	This paper gives an overview of the Webis group's participation in the TREC 2019 Decision Track. Our idea is to axiomatically re-rank the top-k results of BM25F for those topics that seem to be argumentative. For the re-ranking, we use five axioms that capture signals of argumentativeness and information credibility.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BondarenkoFKHVS19.bib) "
	```
	@inproceedings{DBLP:conf/trec/BondarenkoFKHVS19,
		author = {Alexander Bondarenko and Maik Fr{\"{o}}be and Vaibhav Kasturia and Matthias Hagen and Michael V{\"{o}}lske and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2019: Decision Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/Webis.D.pdf},
		timestamp = {Fri, 19 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BondarenkoFKHVS19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Trec 2019 Decision Track

_Wanqing Cui, Yan Jiang, Shuchang Tao, Hanzhang Guo_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/ICTNET.D.pdf](https://trec.nist.gov/pubs/trec28/papers/ICTNET.D.pdf)
- :material-file-search: **Runs:** [ICTNETv1BM25](./runs.md#ictnetv1bm25) | [ICTNETv2BM25](./runs.md#ictnetv2bm25)

??? abstract "Abstract"
	
	In this paper we report on our participation in the Trec 2019 Decision Track[1] which aims to provide a venue for research on retrieval methods that promote better decision making with search engines and develop new online and offline evaluation methods to predict the decision making quality induced by search results. We convert this task into a standard information retrieval task and use traditional IR model. Finally we give a summary for the solution of our work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CuiJTG19.bib) "
	```
	@inproceedings{DBLP:conf/trec/CuiJTG19,
		author = {Wanqing Cui and Yan Jiang and Shuchang Tao and Hanzhang Guo},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Trec 2019 Decision Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/ICTNET.D.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CuiJTG19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UQ IElab at TREC 2019 Decision Track

_Jimmy, Guido Zuccon_

- :fontawesome-solid-user-group: **Participant:** [UQ](./participants.md#uq)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec28/papers/UQ.D.pdf](https://trec.nist.gov/pubs/trec28/papers/UQ.D.pdf)
- :material-file-search: **Runs:** [IELAB01_ori_q](./runs.md#ielab01_ori_q) | [IELAB02_ori_d](./runs.md#ielab02_ori_d) | [IELAB03_umls_d](./runs.md#ielab03_umls_d) | [IELAB04_umls_n](./runs.md#ielab04_umls_n) | [IELAB05_xChv_q](./runs.md#ielab05_xchv_q) | [IELAB06_xChv_d](./runs.md#ielab06_xchv_d) | [IELAB07_xWiki_q](./runs.md#ielab07_xwiki_q) | [IELAB08_xWiki_d](./runs.md#ielab08_xwiki_d) | [IELAB09_xCW_q](./runs.md#ielab09_xcw_q) | [IELAB10_xCW_d](./runs.md#ielab10_xcw_d)

??? abstract "Abstract"
	
	We describe our participation to the TREC 2019 Decision Track. The first year of this track challenges participants to devise search technologies that retrieve correct health advice from web resources, with the intent to better support people's health decision making. Our solution addressed this challenge by extending the Entity Query Feature Expansion model (EQFE), a knowledge base (KB) query expansion method. In previous work we showed that Wikipedia and the Consumer Health Vocabulary resource can be effective as basis for consumer health search query expansion, within the EQFE method. To obtain query expansion terms, first, we mapped entity mentions to KB entities by performing exact matching. After mapping, we used the Title of the mapped KB entities as the source for expansion terms. Despite previous evaluation demonstrating the effectiveness of this method, EQFE did not provide the expected gains over not using query expansion, on both relevant-based and credibility-based evaluation measures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JimmyZ19.bib) "
	```
	@inproceedings{DBLP:conf/trec/JimmyZ19,
		author = {Jimmy and Guido Zuccon},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UQ} IElab at {TREC} 2019 Decision Track},
		booktitle = {Proceedings of the Twenty-Eighth Text REtrieval Conference, {TREC} 2019, Gaithersburg, Maryland, USA, November 13-15, 2019},
		series = {{NIST} Special Publication},
		volume = {1250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2019},
		url = {https://trec.nist.gov/pubs/trec28/papers/UQ.D.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JimmyZ19.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

