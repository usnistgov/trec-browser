# Proceedings - Web 2001 

#### Combining Text- and Link-based Retrieval Methods for Web IR

_Kiduk Yang_

- :fontawesome-solid-user-group: **Participant:** [uncYang](./participants.md#uncyang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/uncyang.pdf](http://trec.nist.gov/pubs/trec10/papers/uncyang.pdf)
- :material-file-search: **Runs:** [uncvsms](./runs.md#uncvsms) | [uncfsls](./runs.md#uncfsls) | [uncfslm](./runs.md#uncfslm) | [uncvsmm](./runs.md#uncvsmm)

??? abstract "Abstract"
	
	The characteristics of Web search environment, namely the document characteristics and the searcher behavior on the Web, confound the problems of Information Retrieval (IR). The massive, heterogeneous, dynamic, and distributed Web document collection as well as the unpredictable and less than ideal querying behavior of a typical Web searcher exacerbate conventional IR problems and diminish the effectiveness of retrieval approaches proven in the laboratory conditions of traditional IR. At the same time, the Web is rich with various sources of information that go beyond the contents of documents, such as document characteristics, hyperlinks, Web directories (e.g. Yahoo), and user statistics. Fusion IR studies have repeatedly shown that combining multiple sources of evidence can improve retrieval performance. Furthermore, the nature of the Web search environment is such that retrieval approaches based on single sources of evidence suffer from weaknesses that can hurt the retrieval performance in certain situations. For example, content-based IR approaches have difficulty dealing with the diversity in vocabulary and quality of web documents, while link-based approaches can suffer from incomplete or noisy link topology. The inadequacies of singular Web IR approaches coupled with the fusion hypothesis (i.e. 'fusion is good for IR') make a strong argument for combining multiple sources of evidence as a potentially advantageous retrieval strategy for Web IR. Among the various source of evidence on the Web, we focused our TREC-10 efforts on leveraging document text and hyperlinks, and examined the effects of combining result sets as well as those of various evidence source parameters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Yang01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Yang01,
		author = {Kiduk Yang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Combining Text- and Link-based Retrieval Methods for Web {IR}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/uncyang.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Yang01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Machine Learning Approach for Homepage Finding Task

_Wensi Xi, Edward A. Fox_

- :fontawesome-solid-user-group: **Participant:** [VT](./participants.md#vt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/VT-TREC10.pdf](http://trec.nist.gov/pubs/trec10/papers/VT-TREC10.pdf)
- :material-file-search: **Runs:** [VTBASE](./runs.md#vtbase) | [VTEP](./runs.md#vtep)

??? abstract "Abstract"
	
	This paper describes new machine learning approaches to predict the correct homepage in response to a user's homepage finding query. This involves two phases. In the first phase, a decision tree is generated to predict whether a URL is a homepage URL or not. The decision tree then is used to filter out non-homepages from the webpages returned by a standard vector space IR system. In the second phase, a logistic regression analysis is used to combine multiple sources of evidence on the remaining webpages to predict which homepage is most relevant to a user's query. 100 queries are used to train the logistic regression model and another 145 testing queries are used to evaluate the model derived. Our results show that about 84% of the testing queries had the correct homepage returned within the top 10 pages. This shows that our machine learning approaches are effective since without any machine learning approaches, only 59% of the testing queries had their correct answers returned within the top 10 hits.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XiF01.bib) "
	```
	@inproceedings{DBLP:conf/trec/XiF01,
		author = {Wensi Xi and Edward A. Fox},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Machine Learning Approach for Homepage Finding Task},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/VT-TREC10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XiF01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC-10: Filtering, QA, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yikun Guo, Yingju Xia, Zhe Feng_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf](http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf)
- :material-file-search: **Runs:** [fdut10wtc01](./runs.md#fdut10wtc01) | [fdut10wac01](./runs.md#fdut10wac01) | [fdut10wtl01](./runs.md#fdut10wtl01) | [fdut10wal01](./runs.md#fdut10wal01)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC conference for the second time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we participate in the sub-task of adaptive and batch filtering. Vector representation and computation are heavily applied in filtering procedure. Four runs have been submitted, which includes one TIOSU and one TIOF run for adpative filtering, as well as another one TIOSU and one TIOF run for batch filtering. We have tried many natural language processing techniques in our QA system, including statistical sentence breaking, POS tagging, parsing, name entity tagging, chunking and semantic verification. Various sources of world knowledge are also incorporated, such as WordNet and geographic information. For web retrieval, relevant document set is first created by an extended Boolean retrieval engine, and then reordered according to link information. Four runs with different combination of topic coverage and link information are submitted On video track, We take part in both of the sub-tasks. In the task of shot boundary detection, we have submitted two runs with different parameters. In the task of video retrieval, we have submitted the results of 17 topics among all the topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHNGXF01.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHNGXF01,
		author = {Lide Wu and Xuanjing Huang and Junyu Niu and Yikun Guo and Yingju Xia and Zhe Feng},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{FDU} at {TREC-10:} Filtering, QA, Web and Video Tasks},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHNGXF01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieving Web Pages Using Content, Links, URLs and Anchors

_Thijs Westerveld, Wessel Kraaij, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [tno/utwente](./participants.md#tno/utwente)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/TNO-UTwente-trec10-final.pdf](http://trec.nist.gov/pubs/trec10/papers/TNO-UTwente-trec10-final.pdf)
- :material-file-search: **Runs:** [tnout10t2](./runs.md#tnout10t2) | [tnout10t1](./runs.md#tnout10t1) | [tnout10epCU](./runs.md#tnout10epcu) | [tnout10epCAU](./runs.md#tnout10epcau) | [tnout10epC](./runs.md#tnout10epc) | [tnout10epA](./runs.md#tnout10epa)

??? abstract "Abstract"
	
	For this year's web track, we concentrated on the entry page finding task. For the content-only runs, in both the ad-hoc task and the entry page finding task, we used an information retrieval system based on a simple unigram language model. In the Ad hoc task we experimented with alternatieve approaches to smoothing. For the entry page task, we incorporated additional information into the model. The sources of information we used in addition to the document's content are links, URLs and anchors. We found that almost every approach can improve the results of a content only run. In the end, a very basic approach, using the depth of the path of the URL as a prior, yielded by far the largest improvement over the content only results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WesterveldKH01.bib) "
	```
	@inproceedings{DBLP:conf/trec/WesterveldKH01,
		author = {Thijs Westerveld and Wessel Kraaij and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Retrieving Web Pages Using Content, Links, URLs and Anchors},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/TNO-UTwente-trec10-final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WesterveldKH01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-10 Experiments at CAS-ICT: Filtering, Web and QA

_Bin Wang, Hongbo Xu, Zhifeng Yang, Yue Liu, Xueqi Cheng, Dongbo Bu, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [chinese_academy](./participants.md#chinese_academy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf](http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf)
- :material-file-search: **Runs:** [ictweb10n](./runs.md#ictweb10n) | [ictweb10nl](./runs.md#ictweb10nl) | [ictweb10nfl](./runs.md#ictweb10nfl) | [ictweb10nf](./runs.md#ictweb10nf)

??? abstract "Abstract"
	
	CAS-ICT took part in the TREC conference for the first time this year. We have participated in three tracks of TREC-10. For adaptive filtering track, we paid more attention to feature selection and profile adaptation. For web track, we tried to integrate different ranking methods to improve system performance. For QA track, we focused on question type identification, named entity tagging and answer matching. This paper describes our methods in detail.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangXYLCBB01.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangXYLCBB01,
		author = {Bin Wang and Hongbo Xu and Zhifeng Yang and Yue Liu and Xueqi Cheng and Dongbo Bu and Shuo Bai},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-10} Experiments at {CAS-ICT:} Filtering, Web and {QA}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangXYLCBB01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Hummingbird SearchServer at TREC 2001

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/HumTREC2001.pdf](http://trec.nist.gov/pubs/trec10/papers/HumTREC2001.pdf)
- :material-file-search: **Runs:** [hum01tlx](./runs.md#hum01tlx) | [hum01t](./runs.md#hum01t) | [hum01tl](./runs.md#hum01tl) | [hum01tdlx](./runs.md#hum01tdlx)

??? abstract "Abstract"
	
	Hummingbird submitted ranked result sets for the topic relevance task of the TREC 2001 Web Track (10GB of web data) and for the monolingual Arabic task of the TREC 2001 Cross-Language Track (869MB of Arabic news data). SearchServer's Intuitive Searching™ tied or exceeded the median Precision@10 score in 46 of the 50 web queries. For the web queries, enabling SearchServer's document length normalization increased Precision@10 by 65% and average precision by 55%. SearchServer's option to square the importance of inverse document frequency (V2:4 vs. V2:3) increased Precision@10 by 8% and average precision by 12%. SearchServer's stemming increased Precision@10 by 5% and average precision by 13%. For the Arabic queries, a combination of experimental Arabic morphological normalizations, Arabic stop words and pseudo-relevance feedback increased average precision by 53% and Precision@10 by 9%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson01,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Hummingbird SearchServer at {TREC} 2001},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/HumTREC2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC-10 Experiment: Distributed Collections and Entrypage  Searching

_Jacques Savoy, Yves Rasolofo_

- :fontawesome-solid-user-group: **Participant:** [Neuchatel](./participants.md#neuchatel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/UniNE.pdf](http://trec.nist.gov/pubs/trec10/papers/UniNE.pdf)
- :material-file-search: **Runs:** [UniNEn7d](./runs.md#uninen7d) | [UniNEt7dL](./runs.md#uninet7dl) | [UniNEtd](./runs.md#uninetd) | [UniNEtdL](./runs.md#uninetdl) | [UniNEep1](./runs.md#unineep1) | [UniNEep2](./runs.md#unineep2) | [UniNEep4](./runs.md#unineep4) | [UniNEep3](./runs.md#unineep3)

??? abstract "Abstract"
	
	For our participation in TREC-10, we will focus on the searching distributed collections and also on designing and implementing a new search strategy to find homepages. Presented in the first part of this paper is a new merging strategy based on retrieved list lengths, and in the second part a development of our approach to creating retrieval models able to combine both Web page and URL address information when searching online service locations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SavoyR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/SavoyR01,
		author = {Jacques Savoy and Yves Rasolofo},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Report on the {TREC-10} Experiment: Distributed Collections and Entrypage Searching},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/UniNE.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SavoyR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC-10: Filtering and Web Tracks

_Stephen E. Robertson, Steve Walker, Hugo Zaragoza_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/msr_cambridge.pdf](http://trec.nist.gov/pubs/trec10/papers/msr_cambridge.pdf)
- :material-file-search: **Runs:** [ok10wt1](./runs.md#ok10wt1) | [ok10wt3](./runs.md#ok10wt3) | [ok10wtnd0](./runs.md#ok10wtnd0) | [ok10wtnd1](./runs.md#ok10wtnd1) | [ok10whd1](./runs.md#ok10whd1) | [ok10whd0](./runs.md#ok10whd0) | [ok10wahd0](./runs.md#ok10wahd0) | [ok10wahd1](./runs.md#ok10wahd1)

??? abstract "Abstract"
	
	This report is concerned with the Adaptive Filtering and Web tracks. There are separate reports in this volume [1, 2] on the Microsoft Research Redmond participation in QA track and the Microsoft Research Beijing participation in the Web track.. Two runs were submitted for the Adaptive Filtering track, on the adaptive filtering task only (two optimisa-tion measures), and several runs for the Web track, both tasks (adhoc and home page finding). The filtering system is somewhat similar to the one used for TREC-9; the web system is a simple Okapi system without blind feedback, but the document indexing includes anchor text from incoming links.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonWZ01.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonWZ01,
		author = {Stephen E. Robertson and Steve Walker and Hugo Zaragoza},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Microsoft Cambridge at {TREC-10:} Filtering and Web Tracks},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/msr\_cambridge.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonWZ01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Yonsei/ETRI at TREC-10: Utilizing Web Document Properties

_Dong-Yul Ra, Eui-Kyu Park, Joong-Sik Jang_

- :fontawesome-solid-user-group: **Participant:** [Yonsei](./participants.md#yonsei)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/yonsei_etri_trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/yonsei_etri_trec10.pdf)
- :material-file-search: **Runs:** [yeaht01](./runs.md#yeaht01) | [yeahtd01](./runs.md#yeahtd01) | [yehp01](./runs.md#yehp01) | [yeahtb01](./runs.md#yeahtb01) | [yeahdb01](./runs.md#yeahdb01) | [yehpb01](./runs.md#yehpb01)

??? abstract "Abstract"
	
	As our first TREC participation, four runs were submitted for the ad hoc task and two runs for the home page finding task in the web track. For the ad hoc task we experimented on the usefulness of anchor texts. However, no significant gain in retrieval effectiveness was observed. The substring relationship between URL's was found to be effective in the home page finding task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RaPJ01.bib) "
	```
	@inproceedings{DBLP:conf/trec/RaPJ01,
		author = {Dong{-}Yul Ra and Eui{-}Kyu Park and Joong{-}Sik Jang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Yonsei/ETRI at {TREC-10:} Utilizing Web Document Properties},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/yonsei\_etri\_trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RaPJ01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments Using the Lemur Toolkit

_Paul Ogilvie, James P. Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu-lti](./participants.md#cmu-lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/cmu-dir-lemur-trec10-final.pdf](http://trec.nist.gov/pubs/trec10/papers/cmu-dir-lemur-trec10-final.pdf)
- :material-file-search: **Runs:** [Lemur](./runs.md#lemur)

??? abstract "Abstract"
	
	This paper describes experiments using the Lemur toolkit. We participated in the ad-hoc retrieval task of the Web Track. First, we describe Lemur in the System Description section and discuss parsing decisions. In the Experimental Results section, we discuss the official Lemur run and its retrieval parameters and we also discuss several unofficial runs. Finally, we summarize and draw conclusions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OgilvieC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/OgilvieC01,
		author = {Paul Ogilvie and James P. Callan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Experiments Using the Lemur Toolkit},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/cmu-dir-lemur-trec10-final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OgilvieC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Kasetsart University TREC-10 Experiments

_P. Narasetsathaporn, Arnon Rungsawang_

- :fontawesome-solid-user-group: **Participant:** [kasetsart](./participants.md#kasetsart)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/kutrec10.pdf](http://trec.nist.gov/pubs/trec10/papers/kutrec10.pdf)
- :material-file-search: **Runs:** [kuadhoc2001](./runs.md#kuadhoc2001) | [kuhpf2001](./runs.md#kuhpf2001)

??? abstract "Abstract"
	
	We use WORMS, our experimental text retrieval en-gine, in our TREC-10 experiments this year. The Okapi weighting scheme is used to index and test in both web ad hoc and homepage finding tasks. In web ad hoc task, we propose a novel approach to improve the retrieval performance using text categorization. Our approach is based on an assumption that 'Most relevant documents are in the same categories as their query'. This retrieval approach has a great effectiveness in reducing the number of searching documents and the searching time. In addition, it can be used to improve precision of retrieval. In homepage finding task, we use a query expansion based method and the Google search engine to find more useful words to be added to the topics. Before using with homepage finding task, we test the query expansion method with the homepage finding training set to get the best type of expanded query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NorasetsathapornR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/NorasetsathapornR01,
		author = {P. Narasetsathaporn and Arnon Rungsawang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Kasetsart University {TREC-10} Experiments},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/kutrec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NorasetsathapornR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Challenges of Multi-Mode IR Software

_Gregory B. Newby_

- :fontawesome-solid-user-group: **Participant:** [uncNewby](./participants.md#uncnewby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/gbn-trec10notebook.pdf](http://trec.nist.gov/pubs/trec10/papers/gbn-trec10notebook.pdf)
- :material-file-search: **Runs:** [irtLnut](./runs.md#irtlnut) | [irtLnua](./runs.md#irtlnua)

??? abstract "Abstract"
	
	Web track results are presented. A software project, IRTools, is described. IRTools is intended to enable information retrieval (IR) experimentation by incorporating methods for multiple modes of IR operation, such as the vector space model and latent semantic indexing (LSI). Plans for the interactive track are described.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Newby01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Newby01,
		author = {Gregory B. Newby},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Challenges of Multi-Mode {IR} Software},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/gbn-trec10notebook.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Newby01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fujitsu Laboratories TREC2001 Report

_Isao Namba_

- :fontawesome-solid-user-group: **Participant:** [Fujitsu](./participants.md#fujitsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/flab_trec2001.pdf](http://trec.nist.gov/pubs/trec10/papers/flab_trec2001.pdf)
- :material-file-search: **Runs:** [flabxet256](./runs.md#flabxet256) | [flabxe75a](./runs.md#flabxe75a) | [flabxt](./runs.md#flabxt) | [flabxtl](./runs.md#flabxtl) | [flabxeall](./runs.md#flabxeall) | [flabxemerge](./runs.md#flabxemerge) | [flabxtd](./runs.md#flabxtd) | [flabxtdn](./runs.md#flabxtdn)

??? abstract "Abstract"
	
	This year a Fujitsu Laboratory team participated in web tracks. Both for ad hoc task, and entry point search task, we combined the score of normal ranking search and that of page ranking techniques. For ad hoc style task, the effect of page ranking was very limitted. We only got very little improvement for title field search, and the page rank was not effective for description, and narrative field search. For entry point search task, we compared three heuristics. The first heuristics supposed that entry point page contains key word and had high page rank score. The second heuristics supposed that entry point page contains key word in its head part and had high page ran score. The third heuristics supposes that entry point is pointed by the pages whose anchor string contains key word, and has high page rank score. The page rank improved the result of entry point search about 20-30% in rather small VLC10 test set, and the first heuristics got the best result because of its high recall.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Namba01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Namba01,
		author = {Isao Namba},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Fujitsu Laboratories {TREC2001} Report},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/flab\_trec2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Namba01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2001: Experiments in Filtering and in Arabic,  Video, and Web Retrieval

_James Mayfield, Paul McNamee, Cash Costello, Christine D. Piatko, Amit Banerjee_

- :fontawesome-solid-user-group: **Participant:** [apl-jhu](./participants.md#apl-jhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf](http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf)
- :material-file-search: **Runs:** [apl10hb](./runs.md#apl10hb) | [apl10wa](./runs.md#apl10wa) | [apl10wb](./runs.md#apl10wb) | [apl10ha](./runs.md#apl10ha) | [apl10wc](./runs.md#apl10wc) | [apl10wd](./runs.md#apl10wd)

??? abstract "Abstract"
	
	The outsider might wonder whether, in its tenth year, the Text Retrieval Conference would be a moribund workshop encouraging little innovation and undertaking few new challenges, or whether fresh research problems would continue to be addressed. We feel strongly that it is the later that is true; our group at the Johns Hopkins University Applied Physics Laboratory (JHU/APL) participated in four tracks at this year’s conference, three of which presented us with new and interesting problems. For the first time we participated in the filtering track, and we submitted official results for both the batch and routing subtasks. This year, a first attempt was made to hold a content-based video retrieval track at TREC, and we developed a new suite of tools for image analysis and multimedia retrieval. Finally, though not a stranger to cross-language text retrieval, we made a first attempt at Arabic language retrieval while emphasizing a language-neutral approach that has worked well in other languages. Thus, our team found several challenges to face this year, and this paper mainly reports our initial findings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MayfieldMCPB01.bib) "
	```
	@inproceedings{DBLP:conf/trec/MayfieldMCPB01,
		author = {James Mayfield and Paul McNamee and Cash Costello and Christine D. Piatko and Amit Banerjee},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{JHU/APL} at {TREC} 2001: Experiments in Filtering and in Arabic, Video, and Web Retrieval},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MayfieldMCPB01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC2001 Question-Answer, Web and Cross Language Experiments using  PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf](http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf)
- :material-file-search: **Runs:** [pir1Wa](./runs.md#pir1wa) | [pir1Wt1](./runs.md#pir1wt1) | [pir1Wt2](./runs.md#pir1wt2)

??? abstract "Abstract"
	
	We applied our PIRCS system for the Question-Answer, ad-hoc Web retrieval using the 10-GB collection, and the English-Arabic cross language tracks. These are described in Sections 2,3,4 respectively. We also attempted to complete the adaptive filtering experiments with our upgraded programs but found that we did not have sufficient time to do so.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokGDC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokGDC01,
		author = {Kui{-}Lam Kwok and Laszlo Grunfeld and Norbert Dinstl and M. Chan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC2001} Question-Answer, Web and Cross Language Experiments using {PIRCS}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokGDC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Integrating Link Structure and Content Information for Ranking Web  Documents

_Tapas Kanungo, Jason Y. Zien_

- :fontawesome-solid-user-group: **Participant:** [ibm-web](./participants.md#ibm-web)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/ibm_tapas_paper.pdf](http://trec.nist.gov/pubs/trec10/papers/ibm_tapas_paper.pdf)
- :material-file-search: **Runs:** [ARCJ0](./runs.md#arcj0) | [ARCJ5](./runs.md#arcj5) | [IBMHOMENR](./runs.md#ibmhomenr) | [IBMHOMER](./runs.md#ibmhomer)

??? abstract "Abstract"
	
	In this article we describe the results of our experiments on combining the two sources of information: The web link structure and the document content. We developed a new scoring function that combines TE*IDF scoring with the document rank and show that it is particularly effective in the Home Page Finding task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KanungoZ01.bib) "
	```
	@inproceedings{DBLP:conf/trec/KanungoZ01,
		author = {Tapas Kanungo and Jason Y. Zien},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Integrating Link Structure and Content Information for Ranking Web Documents},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/ibm\_tapas\_paper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KanungoZ01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RICOH at TREC-10: Web Track Ad-hoc Task

_Hideo Itoh, Hiroko Mano, Yasushi Ogawa_

- :fontawesome-solid-user-group: **Participant:** [ricoh](./participants.md#ricoh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/ricoh.pdf](http://trec.nist.gov/pubs/trec10/papers/ricoh.pdf)
- :material-file-search: **Runs:** [ricMM](./runs.md#ricmm) | [ricAP](./runs.md#ricap) | [ricMS](./runs.md#ricms) | [ricST](./runs.md#ricst)

??? abstract "Abstract"
	
	This year we participated in the Web track and submitted four title-only runs {ricM™, ricAP, ricMS, ricST} which were automatically produced for ad-hoc task. This is our third participation in TREC. Last year in the TREC-9 main web track, our system achieved the best performance in automatic results. However the following problems could be pointed out at the same time. Our system uses many parameters in term-weighting and document-scoring. The value of each parameter should be tuned to improve retrieval effectiveness using test collections. However we cannot use enough relevance information in most of practical situations. Automatic query expansion using pseudo-relevance feedback occasionally produces a negative effect. For example in TREC-9, the performance for title-only query was hurt by query expansion using pseudo-relevance feedback. In TREC-10, we tackled the above problems in addition to taking account of practical retrieval efficiency.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ItohMO01.bib) "
	```
	@inproceedings{DBLP:conf/trec/ItohMO01,
		author = {Hideo Itoh and Hiroko Mano and Yasushi Ogawa},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{RICOH} at {TREC-10:} Web Track Ad-hoc Task},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/ricoh.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ItohMO01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Link-based Approaches for Text Retrieval

_Julien Gevrey, Stefan M. Rüger_

- :fontawesome-solid-user-group: **Participant:** [imperial](./participants.md#imperial)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/web-gevrey-rueger.pdf](http://trec.nist.gov/pubs/trec10/papers/web-gevrey-rueger.pdf)
- :material-file-search: **Runs:** [icadhoc1](./runs.md#icadhoc1) | [icadhoc2](./runs.md#icadhoc2) | [icadhoc3](./runs.md#icadhoc3) | [ichp2](./runs.md#ichp2) | [ichp1](./runs.md#ichp1)

??? abstract "Abstract"
	
	We assess a family of ranking mechanisms for search engines based on linkage analysis using a carefully engineered subset of the World Wide Web, WT10g (Bailey, Craswell and Hawking 2001), and a set of relevance judgements for 50 different queries from Trec-9 to evaluate the performance of several link-based ranking techniques. Among these link-based algorithms, Kleinberg's HITS and Larry Page and Sergey Brin's PageRank are assessed. Link analysis seems to yield poor results in Trec's Web Ad Hoc Task. We suggest some alternative algorithms which reuse both text-based search similarity measures and linkage analysis. Although these algorithms yield better results, improving text-only search recall-precision curves in the Web Ad Hoc Task remains elusive; only a certain category of queries seems to benefit from linkage analysis. Among these queries, homepage searches may be good candidates.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GevreyR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/GevreyR01,
		author = {Julien Gevrey and Stefan M. R{\"{u}}ger},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Link-based Approaches for Text Retrieval},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/web-gevrey-rueger.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GevreyR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-10 Web Track Experiments at MSRA

_Jianfeng Gao, Guihong Cao, Hongzhao He, Min Zhang, Jian-Yun Nie, Steve Walker, Stephen E. Robertson_

- :fontawesome-solid-user-group: **Participant:** [microsoft-china](./participants.md#microsoft-china)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/msra.trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/msra.trec10.pdf)
- :material-file-search: **Runs:** [msrcn1](./runs.md#msrcn1) | [msrcn2](./runs.md#msrcn2) | [msrcn3](./runs.md#msrcn3) | [msrcn4](./runs.md#msrcn4) | [msrcnp1](./runs.md#msrcnp1) | [msrcnp2](./runs.md#msrcnp2)

??? abstract "Abstract"
	
	In TREC-10, Microsoft Research Asia (MSRA) participated in the Web track (ad hoc retrieval task and homepage finding task). The latest version of the Okapi system (Windows 2000 version) was used. We focused on the developing of content-based retrieval and link-based retrieval, and investigated the suitable combination of the two. For content-based retrieval, we examined the problems of weighting scheme, re-weighting and pseudo-relevance feedback (PRF). Then we developed a method called collection refinement (CE) for QE. We investigated the use of two kinds of link information, link anchor and link structure. We used anchor descriptions instead of content text to build index. Furthermore, different search strategies, such as spreading activation and PageRank, have been tested. Experimental results show: (1) Okapi system is robust and effective for web retrieval. (2) In ad hoc task, content-based retrieval achieved much better performance, and the impact of anchor text can be neglected; while for homepage finding task, both anchor text and content text provide useful information contributing more on precision and recall respectively. (3) Although query expansion does not show any improvement in our web retrieval experiments, we believe that there are still potential for CE.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaoCHZNWR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaoCHZNWR01,
		author = {Jianfeng Gao and Guihong Cao and Hongzhao He and Min Zhang and Jian{-}Yun Nie and Steve Walker and Stephen E. Robertson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-10} Web Track Experiments at {MSRA}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/msra.trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaoCHZNWR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### More Reflections on "Aboutness" TREC-2001 Evaluation Experiments  at Justsystem

_Sumio Fujita_

- :fontawesome-solid-user-group: **Participant:** [Justsystem](./participants.md#justsystem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/jscbtaw.pdf](http://trec.nist.gov/pubs/trec10/papers/jscbtaw.pdf)
- :material-file-search: **Runs:** [jscbtawep1](./runs.md#jscbtawep1) | [jscbtawep2](./runs.md#jscbtawep2) | [jscbtawep3](./runs.md#jscbtawep3) | [jscbtawep4](./runs.md#jscbtawep4) | [jscbtawtl1](./runs.md#jscbtawtl1) | [jscbtawtl3](./runs.md#jscbtawtl3) | [jscbtawtl2](./runs.md#jscbtawtl2) | [jscbtawtl4](./runs.md#jscbtawtl4)

??? abstract "Abstract"
	
	he TREC-2001 Web track evaluation experiments at the Justsystem site are described with a focus on the 'aboutness' based approach in text retrieval. In the web ad hoc task, our TREC-9 approach is adopted again, combining both pseudo-relevance feedback and reference database feedback but the setting is calibrated for an early precision preferred search. For the entry page finding task, we combined techniques such as search against partitioned collection with result fusion, and attribute-value basis re-ranking. As post-submission experiments, distributed retrieval against WT10G is examined and two different database partitioning and three database selection algorithms are combined and evaluated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Fujita01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Fujita01,
		author = {Sumio Fujita},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {More Reflections on "Aboutness" {TREC-2001} Evaluation Experiments at Justsystem},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/jscbtaw.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Fujita01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Padova at TREC-10

_Franco Crivellari, Massimo Melucci_

- :fontawesome-solid-user-group: **Participant:** [padova](./participants.md#padova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/padova.pdf](http://trec.nist.gov/pubs/trec10/papers/padova.pdf)
- :material-file-search: **Runs:** [PDWTAHDR](./runs.md#pdwtahdr) | [PDWTEPDR](./runs.md#pdwtepdr) | [PDWTAHWL](./runs.md#pdwtahwl) | [PDWTAHTL](./runs.md#pdwtahtl) | [PDWTAHPR](./runs.md#pdwtahpr) | [PDWTEPWL](./runs.md#pdwtepwl) | [PDWTEPTL](./runs.md#pdwteptl) | [PDWTEPPR](./runs.md#pdwteppr)

??? abstract "Abstract"
	
	This is the second year that the University of Padova participates to the Text Retrieval Conference (TREC). Last year we participated as well to this program of experimentation in information retrieval with very large document databases. In both years, we participated to the Web track, and specifically to the ad-hoc task, which consists in testing retrieval performance by submitting 50 queries extracted from 50 respective topics. This year we participated to the homepage finding task as well. This year we could devote more time to experiments than last year, yet some problems still arose because we indexed the full-text of documents, while we indexed only a portion of documents only.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CrivellariM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/CrivellariM01,
		author = {Franco Crivellari and Massimo Melucci},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {University of Padova at {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/padova.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CrivellariM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC10 Web and Interactive Tracks at CSIRO

_Nick Craswell, David Hawking, Ross Wilkinson, Mingfang Wu_

- :fontawesome-solid-user-group: **Participant:** [CSIRO](./participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/csiro-trec-2001.pdf](http://trec.nist.gov/pubs/trec10/papers/csiro-trec-2001.pdf)
- :material-file-search: **Runs:** [csiro0awh1](./runs.md#csiro0awh1) | [csiro0awa1](./runs.md#csiro0awa1) | [csiro0awh2](./runs.md#csiro0awh2) | [csiro0mwa1](./runs.md#csiro0mwa1) | [csiro0awa2](./runs.md#csiro0awa2) | [csiro0awa3](./runs.md#csiro0awa3)

??? abstract "Abstract"
	
	For the 2001 round of TREC, the TED group of CSIRO participated and completed runs in two tracks: web and interactive. Our primary goals in the Web track participation were two-fold: A) to confirm our earlier finding [1] that anchor text is useful in a homepage finding task, and B) to provide an interactive search engine style interface to searching the WT10g data. In addition, three title-only runs were submitted, comparing two different implementations of stemming to unstemmed processing of the raw query. None of these runs used pseudo relevance feedback. In the interactive track, our investigation was focused on whether there exists any correlation between delivery (searching/presentation) mechanisms and searching tasks. Our experiment involved three delivery mechanisms and two types of searching tasks. The three delivery mechanisms are: a ranked list interface, a clustering interface, and an integrated interface with ranked list, clustering structure, and Expert Links. The two searching tasks are searching for an individual document and searching for a set of documents. Our experiment result shows that subjects usually used only one delivery mechanism regardless of the searching task. No delivery mechanism was found to be superior for any particular task, the only difference was the time used to complete a search, that favored the ranked list interface.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CraswellHWW01.bib) "
	```
	@inproceedings{DBLP:conf/trec/CraswellHWW01,
		author = {Nick Craswell and David Hawking and Ross Wilkinson and Mingfang Wu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC10} Web and Interactive Tracks at {CSIRO}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/csiro-trec-2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CraswellHWW01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The NexTrieve Search System in TREC 2001

_Gordon Clare, Kim Hendrikse_

- :fontawesome-solid-user-group: **Participant:** [nextrieve](./participants.md#nextrieve)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/nextrieve.pdf](http://trec.nist.gov/pubs/trec10/papers/nextrieve.pdf)
- :material-file-search: **Runs:** [Ntvenx1](./runs.md#ntvenx1) | [Ntvenx2](./runs.md#ntvenx2) | [Ntvfnx3](./runs.md#ntvfnx3) | [Ntvfnx4](./runs.md#ntvfnx4)

??? abstract "Abstract"
	
	The NexTrieve search system is a combination fuzzy and exact search engine. All document words are indexed. The exact (word) index comprises approximate document position information, along with 'type' information indicating if the word is part of specially tagged text (such as a title or heading). At the time of the TREC runs, word presence (including type) at the document level was also recorded, but word frequency within a document was not. The fuzzy index comprises text n-grams including 'type' and originating word information, and their approximate document positions. An 'exact' search uses only the exact-word indexed information (namely word position and type information, and word-presence in document). A 'fuzzy' search uses the fuzzy-indexed information, and is assisted by a simultaneous exact word search. The 'fuzziness' of a fuzzy search arises from the fact that not all query n-grams need be present in a hit for it to generate a good or winning score. A score of a hit during searching was comprised of two parts -- a 'document level' score and a 'proximity' score. The document level score is most important but simply collected word-presence-in-document information and, as such, does not vary on documents that contain the same set of search words with the same types. The proximity level score of a document is the score given to the highest scoring region of the document containing the most search words (with most valuable types) in the smallest area. The position of this highest-scoring area is later used on winning documents to simplify preview generation. Both levels of scoring had small multipliers in effect that increased as more search words were found in a particular document or region. Both levels also made use of the same scores applied to the originating words. These word level scores are generated from inverse frequency values in the database, augmented with word 'type' information (giving an increase or decrease of the basic value). A 'derived' penalty is also present, on words that have been automatically stemmed from an original query word.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClareH01.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClareH01,
		author = {Gordon Clare and Kim Hendrikse},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The NexTrieve Search System in {TREC} 2001},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/nextrieve.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClareH01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Juru at TREC 10 - Experiments with Index Pruning

_David Carmel, Einat Amitay, Michael Herscovici, Yoëlle S. Maarek, Yael Petruschka, Aya Soffer_

- :fontawesome-solid-user-group: **Participant:** [ibm-web](./participants.md#ibm-web)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/JuruAtTrec.pdf](http://trec.nist.gov/pubs/trec10/papers/JuruAtTrec.pdf)
- :material-file-search: **Runs:** [ARCJ0](./runs.md#arcj0) | [ARCJ5](./runs.md#arcj5) | [IBMHOMENR](./runs.md#ibmhomenr) | [IBMHOMER](./runs.md#ibmhomer)

??? abstract "Abstract"
	
	This is the first year that Juru, a Java IR system developed over the past few years at the IBM Research Lab in Haifa, participated in TREC’s Web track. Our experiments focused on the ad-hoc tasks. The main goal of our experiments was to validate a novel pruning method, first presented at [1], that significantly reduces the size of the index with very little influence on the system’s precision. By reducing the index size, it becomes feasible to index large text collections such as the Web track’s data on low-end machines. Furthermore, using our method, Web search engines can significantly decrease the burden of storing or backing up extremely large indices by discarding entries that have almost no influence on search results. In [1] we showed experimentally, using the LA-TIMES collection of TREC, that our pruning algorithm attains a very high degree of pruning with hardly any effect on precision. We showed that we are able to reduce the size of the index by 35% pruning with a slight decrease in average precision (7%), and with almost no effect on the precision of the top 10 results. For 50% pruning, we were still able to maintain the same precision at the top 10 results. Thereby, we obtained a greatly compressed index that gives answers that are essentially as good as those derived from the full index. One important issue that was not addressed in our previous work dealt with the scalability of our pruning methods. In this work, we repeat our previous experiments on the larger domain of the Web Track data. While our previous experiments were conducted on a collection of 132,000 documents (476 MB), for the current experiments we built a core index for the entire Wt10g collection, (1.69M documents, 10GB). We then ran our pruning algorithms on the core index varying the amount of pruning to obtain a sequence of pruned indices. Section 4 describes the reuslts of the runs obtained from this sequence of indices. In order to be able to index such a large collection and retreive high quality results, we had to scale Juru’s basic indexing and retrieval techniques as well as modify them to specifically handle Web data. The rest of the paper is organized as follows: Section 2 describes Juru’s main functionality. Section 3 briefly describes the pruning algorithms used for the experiments conducted in this work. Section 4 describes the experiments and the results we obtained. Section 5 concludes.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarmelAHMPS01.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarmelAHMPS01,
		author = {David Carmel and Einat Amitay and Michael Herscovici and Yo{\"{e}}lle S. Maarek and Yael Petruschka and Aya Soffer},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Juru at {TREC} 10 - Experiments with Index Pruning},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/JuruAtTrec.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarmelAHMPS01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure and MercureFiltre Applied for Web and Filtering Tasks at TREC-10

_Mohand Boughanem, Claude Chrisment, Mohamed Tmar_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/irit.trec2001.pdf](http://trec.nist.gov/pubs/trec10/papers/irit.trec2001.pdf)
- :material-file-search: **Runs:** [Merxtd](./runs.md#merxtd) | [Merxt](./runs.md#merxt)

??? abstract "Abstract"
	
	The tests performed for TREC-10 focus on the Filtering (adaptive, batch and routing) tracks and web tracks. The runs are based on Mercure system for web, routing and batch tracks, and MercureFiltre for adaptive track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemCT01.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemCT01,
		author = {Mohand Boughanem and Claude Chrisment and Mohamed Tmar},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Mercure and MercureFiltre Applied for Web and Filtering Tasks at {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/irit.trec2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemCT01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FUB at TREC-10 Web Track: A Probabilistic Framework for Topic  Relevance Term Weighting

_Gianni Amati, Claudio Carpineto, Giovanni Romano_

- :fontawesome-solid-user-group: **Participant:** [FUB](./participants.md#fub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/fub01.pdf](http://trec.nist.gov/pubs/trec10/papers/fub01.pdf)
- :material-file-search: **Runs:** [fub01ne](./runs.md#fub01ne) | [fub01idf](./runs.md#fub01idf) | [fub01ne2](./runs.md#fub01ne2) | [fub01be2](./runs.md#fub01be2)

??? abstract "Abstract"
	
	The main investigation of our participation in the WEB track of TREC-10 concerns the effectiveness of a novel probabilistic framework [1] for generating term weighting models of topic relevance retrieval. This approach endeavours to determine the weight of a word within a document in a purely theoretic way as a combination of different probability distributions, with the goal of reducing as much as possible the number of parameters which must be learned and tuned from relevance assessments on training test collections. The framework is based on discounting the probability of terms in the whole col-lection, modeled as deviation from randomness, with a notion of information gain related to the probabilty of terms in single documents. The framework is made up of three components: the 'information content' component relative to the entire data collection, the 'information gain normalization factor' component relative to a subset of the data collection (the elite set of the observed term), and the 'term frequency normalization function' component relative to the document length and to other collection statistics. Each component is obtained by computing a suitable probability density function. One advantage of the framework is that we may easily compare and test the behaviour of different basic models of Information Retrieval under the same experimental conditions and normalization factors and functions. At the same time, we may test and compare ditferent term frequency normalization factors and functions. In addition to testing the effectiveness of the term weighting framework, we were interested in evaluating the utility of query expansion on the WT10g collection. We used information theoretic query expansion and focused on careful paremeter selection. In our experiments, we did not use link information, partly because of tight scheduling - the WT10g collection was made available to us as late as late May 2001 - and partly because it has been shown at TREC-9 that it is not beneficial to topic relevance retrieval. In the rest of the paper, we first introduce the term weighting framework. Then we describe how collection indexing was performed, which probability functions were used in the experiments to instantiate the term weighting framework, and which parameters were chosen for query expansion. A discussion of the main results concludes the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmatiCR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmatiCR01,
		author = {Gianni Amati and Claudio Carpineto and Giovanni Romano},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{FUB} at {TREC-10} Web Track: {A} Probabilistic Framework for Topic Relevance Term Weighting},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/fub01.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmatiCR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT at TREC-10

_Mohammed Aljlayl, Steven M. Beitzel, Eric C. Jensen, Abdur Chowdhury, David O. Holmes, M. Lee, David A. Grossman, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [IIT](./participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/IIT-TREC10.pdf](http://trec.nist.gov/pubs/trec10/papers/IIT-TREC10.pdf)
- :material-file-search: **Runs:** [iit01m](./runs.md#iit01m) | [iit01t](./runs.md#iit01t) | [iit01tfc](./runs.md#iit01tfc) | [iit01tde](./runs.md#iit01tde) | [iit01st](./runs.md#iit01st) | [iit01stb](./runs.md#iit01stb)

??? abstract "Abstract"
	
	For TREC-10, we participated in the adhoc and manual web tracks and in both the site-finding and cross-lingual tracks. For the adhoc track, we did extensive calibrations and learned that combining similarity measures yields little improvement. This year, we focused on a single high-performance similarity measure. For site finding, we implemented several algorithms that did well on the data provided for calibration, but poorly on the real dataset. For the cross-lingual track, we calibrated on the monolingual collection, and developed new Arabic stemming algorithms as well as a novel dictionary-based means of cross-lingual retrieval. Our results in this track were quite promising, with seventeen of our queries performing at or above the median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AljlaylBJCHLGF01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AljlaylBJCHLGF01,
		author = {Mohammed Aljlayl and Steven M. Beitzel and Eric C. Jensen and Abdur Chowdhury and David O. Holmes and M. Lee and David A. Grossman and Ophir Frieder},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{IIT} at {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/IIT-TREC10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AljlaylBJCHLGF01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

