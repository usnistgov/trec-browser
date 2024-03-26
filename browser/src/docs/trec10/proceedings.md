# Proceedings 2001 

## Overview of TREC 2001

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/overview_10.pdf](http://trec.nist.gov/pubs/trec10/papers/overview_10.pdf)
??? abstract "Abstract"
	
	The tenth Text REtrieval Conference, TREC 2001, was held at the National Institute of Standards and Technology (NIST) November 13-16, 2001. The conference was co-sponsored by NIST, the Information Technology Office of the Defense Advanced Research Projects Agency (DARPA/ITO), and the US Department of Defense Advanced Research and Development Activity (ARDA). TREC 2001 is the latest in a series of workshops designed to foster research on technologies for information retrieval. The workshop series has four goals: to encourage retrieval research based on large test collections; to increase communication among industry, academia, and government by creating an open forum for the exchange of research ideas; to speed the transfer of technology from research labs into commercial products by demonstrating substantial improvements in retrieval methodologies on real-world problems; and to increase the availability of appropriate evaluation techniques for use by industry and academia, including development of new evaluation techniques more applicable to current systems. TREC 2001 contained six areas of focus called 'tracks'. These included the Cross-Language Retrieval Track, the Filtering Track, the Interactive Retrieval Track, the Question Answering Track, the Video Retrieval Track, and the Web Retrieval Track. This was the first year for the video track, which was designed to investigate content-based retrieval of digital video. The other tracks were run in previous TRECs, though the particular tasks performed in some of the tracks changed for TREC 2001. Table 1 lists the groups that participated in TREC 2001. Eighty-seven groups submitted retrieval results, an increase of approximately 25 % over the previous year. The participating groups come from twenty-one different countries and include academic, commercial, and government institutions. This paper serves as an introduction to the research described in detail in the remainder of the volume. The next section provides a summary of the retrieval background knowledge that is assumed in the other papers. Section 3 presents a short description of each track— a more complete description of a track can be found in that track's overview paper in the proceedings. The final section looks forward to future TREC conferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees01.bib)"
	```
	@inproceedings{DBLP:conf/trec/Voorhees01,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of {TREC} 2001},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/overview\_10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Web 

#### Combining Text- and Link-based Retrieval Methods for Web IR

_Kiduk Yang_

- :fontawesome-solid-user-group: **Participant:** [uncYang](./web/participants.md#uncyang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/uncyang.pdf](http://trec.nist.gov/pubs/trec10/papers/uncyang.pdf)
- :material-file-search: **Runs:** [uncvsms](./web/runs.md#uncvsms) | [uncfsls](./web/runs.md#uncfsls) | [uncfslm](./web/runs.md#uncfslm) | [uncvsmm](./web/runs.md#uncvsmm)

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

- :fontawesome-solid-user-group: **Participant:** [VT](./web/participants.md#vt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/VT-TREC10.pdf](http://trec.nist.gov/pubs/trec10/papers/VT-TREC10.pdf)
- :material-file-search: **Runs:** [VTBASE](./web/runs.md#vtbase) | [VTEP](./web/runs.md#vtep)

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

- :fontawesome-solid-user-group: **Participant:** [Fudan](./web/participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf](http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf)
- :material-file-search: **Runs:** [fdut10wtc01](./web/runs.md#fdut10wtc01) | [fdut10wac01](./web/runs.md#fdut10wac01) | [fdut10wtl01](./web/runs.md#fdut10wtl01) | [fdut10wal01](./web/runs.md#fdut10wal01)

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

- :fontawesome-solid-user-group: **Participant:** [tno/utwente](./web/participants.md#tno/utwente)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/TNO-UTwente-trec10-final.pdf](http://trec.nist.gov/pubs/trec10/papers/TNO-UTwente-trec10-final.pdf)
- :material-file-search: **Runs:** [tnout10t2](./web/runs.md#tnout10t2) | [tnout10t1](./web/runs.md#tnout10t1) | [tnout10epCU](./web/runs.md#tnout10epcu) | [tnout10epCAU](./web/runs.md#tnout10epcau) | [tnout10epC](./web/runs.md#tnout10epc) | [tnout10epA](./web/runs.md#tnout10epa)

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

- :fontawesome-solid-user-group: **Participant:** [chinese_academy](./web/participants.md#chinese_academy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf](http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf)
- :material-file-search: **Runs:** [ictweb10n](./web/runs.md#ictweb10n) | [ictweb10nl](./web/runs.md#ictweb10nl) | [ictweb10nfl](./web/runs.md#ictweb10nfl) | [ictweb10nf](./web/runs.md#ictweb10nf)

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

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./web/participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/HumTREC2001.pdf](http://trec.nist.gov/pubs/trec10/papers/HumTREC2001.pdf)
- :material-file-search: **Runs:** [hum01tlx](./web/runs.md#hum01tlx) | [hum01t](./web/runs.md#hum01t) | [hum01tl](./web/runs.md#hum01tl) | [hum01tdlx](./web/runs.md#hum01tdlx)

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

- :fontawesome-solid-user-group: **Participant:** [Neuchatel](./web/participants.md#neuchatel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/UniNE.pdf](http://trec.nist.gov/pubs/trec10/papers/UniNE.pdf)
- :material-file-search: **Runs:** [UniNEn7d](./web/runs.md#uninen7d) | [UniNEt7dL](./web/runs.md#uninet7dl) | [UniNEtd](./web/runs.md#uninetd) | [UniNEtdL](./web/runs.md#uninetdl) | [UniNEep1](./web/runs.md#unineep1) | [UniNEep2](./web/runs.md#unineep2) | [UniNEep4](./web/runs.md#unineep4) | [UniNEep3](./web/runs.md#unineep3)

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

- :fontawesome-solid-user-group: **Participant:** [microsoft](./web/participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/msr_cambridge.pdf](http://trec.nist.gov/pubs/trec10/papers/msr_cambridge.pdf)
- :material-file-search: **Runs:** [ok10wt1](./web/runs.md#ok10wt1) | [ok10wt3](./web/runs.md#ok10wt3) | [ok10wtnd0](./web/runs.md#ok10wtnd0) | [ok10wtnd1](./web/runs.md#ok10wtnd1) | [ok10whd1](./web/runs.md#ok10whd1) | [ok10whd0](./web/runs.md#ok10whd0) | [ok10wahd0](./web/runs.md#ok10wahd0) | [ok10wahd1](./web/runs.md#ok10wahd1)

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

- :fontawesome-solid-user-group: **Participant:** [Yonsei](./web/participants.md#yonsei)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/yonsei_etri_trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/yonsei_etri_trec10.pdf)
- :material-file-search: **Runs:** [yeaht01](./web/runs.md#yeaht01) | [yeahtd01](./web/runs.md#yeahtd01) | [yehp01](./web/runs.md#yehp01) | [yeahtb01](./web/runs.md#yeahtb01) | [yeahdb01](./web/runs.md#yeahdb01) | [yehpb01](./web/runs.md#yehpb01)

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

- :fontawesome-solid-user-group: **Participant:** [cmu-lti](./web/participants.md#cmu-lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/cmu-dir-lemur-trec10-final.pdf](http://trec.nist.gov/pubs/trec10/papers/cmu-dir-lemur-trec10-final.pdf)
- :material-file-search: **Runs:** [Lemur](./web/runs.md#lemur)

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

- :fontawesome-solid-user-group: **Participant:** [kasetsart](./web/participants.md#kasetsart)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/kutrec10.pdf](http://trec.nist.gov/pubs/trec10/papers/kutrec10.pdf)
- :material-file-search: **Runs:** [kuadhoc2001](./web/runs.md#kuadhoc2001) | [kuhpf2001](./web/runs.md#kuhpf2001)

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

- :fontawesome-solid-user-group: **Participant:** [uncNewby](./web/participants.md#uncnewby)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/gbn-trec10notebook.pdf](http://trec.nist.gov/pubs/trec10/papers/gbn-trec10notebook.pdf)
- :material-file-search: **Runs:** [irtLnut](./web/runs.md#irtlnut) | [irtLnua](./web/runs.md#irtlnua)

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

- :fontawesome-solid-user-group: **Participant:** [Fujitsu](./web/participants.md#fujitsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/flab_trec2001.pdf](http://trec.nist.gov/pubs/trec10/papers/flab_trec2001.pdf)
- :material-file-search: **Runs:** [flabxet256](./web/runs.md#flabxet256) | [flabxe75a](./web/runs.md#flabxe75a) | [flabxt](./web/runs.md#flabxt) | [flabxtl](./web/runs.md#flabxtl) | [flabxeall](./web/runs.md#flabxeall) | [flabxemerge](./web/runs.md#flabxemerge) | [flabxtd](./web/runs.md#flabxtd) | [flabxtdn](./web/runs.md#flabxtdn)

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

- :fontawesome-solid-user-group: **Participant:** [apl-jhu](./web/participants.md#apl-jhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf](http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf)
- :material-file-search: **Runs:** [apl10hb](./web/runs.md#apl10hb) | [apl10wa](./web/runs.md#apl10wa) | [apl10wb](./web/runs.md#apl10wb) | [apl10ha](./web/runs.md#apl10ha) | [apl10wc](./web/runs.md#apl10wc) | [apl10wd](./web/runs.md#apl10wd)

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

- :fontawesome-solid-user-group: **Participant:** [cuny](./web/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf](http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf)
- :material-file-search: **Runs:** [pir1Wa](./web/runs.md#pir1wa) | [pir1Wt1](./web/runs.md#pir1wt1) | [pir1Wt2](./web/runs.md#pir1wt2)

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

- :fontawesome-solid-user-group: **Participant:** [ibm-web](./web/participants.md#ibm-web)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/ibm_tapas_paper.pdf](http://trec.nist.gov/pubs/trec10/papers/ibm_tapas_paper.pdf)
- :material-file-search: **Runs:** [ARCJ0](./web/runs.md#arcj0) | [ARCJ5](./web/runs.md#arcj5) | [IBMHOMENR](./web/runs.md#ibmhomenr) | [IBMHOMER](./web/runs.md#ibmhomer)

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

- :fontawesome-solid-user-group: **Participant:** [ricoh](./web/participants.md#ricoh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/ricoh.pdf](http://trec.nist.gov/pubs/trec10/papers/ricoh.pdf)
- :material-file-search: **Runs:** [ricMM](./web/runs.md#ricmm) | [ricAP](./web/runs.md#ricap) | [ricMS](./web/runs.md#ricms) | [ricST](./web/runs.md#ricst)

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

- :fontawesome-solid-user-group: **Participant:** [imperial](./web/participants.md#imperial)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/web-gevrey-rueger.pdf](http://trec.nist.gov/pubs/trec10/papers/web-gevrey-rueger.pdf)
- :material-file-search: **Runs:** [icadhoc1](./web/runs.md#icadhoc1) | [icadhoc2](./web/runs.md#icadhoc2) | [icadhoc3](./web/runs.md#icadhoc3) | [ichp2](./web/runs.md#ichp2) | [ichp1](./web/runs.md#ichp1)

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

- :fontawesome-solid-user-group: **Participant:** [microsoft-china](./web/participants.md#microsoft-china)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/msra.trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/msra.trec10.pdf)
- :material-file-search: **Runs:** [msrcn1](./web/runs.md#msrcn1) | [msrcn2](./web/runs.md#msrcn2) | [msrcn3](./web/runs.md#msrcn3) | [msrcn4](./web/runs.md#msrcn4) | [msrcnp1](./web/runs.md#msrcnp1) | [msrcnp2](./web/runs.md#msrcnp2)

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

- :fontawesome-solid-user-group: **Participant:** [Justsystem](./web/participants.md#justsystem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/jscbtaw.pdf](http://trec.nist.gov/pubs/trec10/papers/jscbtaw.pdf)
- :material-file-search: **Runs:** [jscbtawep1](./web/runs.md#jscbtawep1) | [jscbtawep2](./web/runs.md#jscbtawep2) | [jscbtawep3](./web/runs.md#jscbtawep3) | [jscbtawep4](./web/runs.md#jscbtawep4) | [jscbtawtl1](./web/runs.md#jscbtawtl1) | [jscbtawtl3](./web/runs.md#jscbtawtl3) | [jscbtawtl2](./web/runs.md#jscbtawtl2) | [jscbtawtl4](./web/runs.md#jscbtawtl4)

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

- :fontawesome-solid-user-group: **Participant:** [padova](./web/participants.md#padova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/padova.pdf](http://trec.nist.gov/pubs/trec10/papers/padova.pdf)
- :material-file-search: **Runs:** [PDWTAHDR](./web/runs.md#pdwtahdr) | [PDWTEPDR](./web/runs.md#pdwtepdr) | [PDWTAHWL](./web/runs.md#pdwtahwl) | [PDWTAHTL](./web/runs.md#pdwtahtl) | [PDWTAHPR](./web/runs.md#pdwtahpr) | [PDWTEPWL](./web/runs.md#pdwtepwl) | [PDWTEPTL](./web/runs.md#pdwteptl) | [PDWTEPPR](./web/runs.md#pdwteppr)

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

- :fontawesome-solid-user-group: **Participant:** [CSIRO](./web/participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/csiro-trec-2001.pdf](http://trec.nist.gov/pubs/trec10/papers/csiro-trec-2001.pdf)
- :material-file-search: **Runs:** [csiro0awh1](./web/runs.md#csiro0awh1) | [csiro0awa1](./web/runs.md#csiro0awa1) | [csiro0awh2](./web/runs.md#csiro0awh2) | [csiro0mwa1](./web/runs.md#csiro0mwa1) | [csiro0awa2](./web/runs.md#csiro0awa2) | [csiro0awa3](./web/runs.md#csiro0awa3)

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

- :fontawesome-solid-user-group: **Participant:** [nextrieve](./web/participants.md#nextrieve)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/nextrieve.pdf](http://trec.nist.gov/pubs/trec10/papers/nextrieve.pdf)
- :material-file-search: **Runs:** [Ntvenx1](./web/runs.md#ntvenx1) | [Ntvenx2](./web/runs.md#ntvenx2) | [Ntvfnx3](./web/runs.md#ntvfnx3) | [Ntvfnx4](./web/runs.md#ntvfnx4)

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

- :fontawesome-solid-user-group: **Participant:** [ibm-web](./web/participants.md#ibm-web)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/JuruAtTrec.pdf](http://trec.nist.gov/pubs/trec10/papers/JuruAtTrec.pdf)
- :material-file-search: **Runs:** [ARCJ0](./web/runs.md#arcj0) | [ARCJ5](./web/runs.md#arcj5) | [IBMHOMENR](./web/runs.md#ibmhomenr) | [IBMHOMER](./web/runs.md#ibmhomer)

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

- :fontawesome-solid-user-group: **Participant:** [IRIT](./web/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/irit.trec2001.pdf](http://trec.nist.gov/pubs/trec10/papers/irit.trec2001.pdf)
- :material-file-search: **Runs:** [Merxtd](./web/runs.md#merxtd) | [Merxt](./web/runs.md#merxt)

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

- :fontawesome-solid-user-group: **Participant:** [FUB](./web/participants.md#fub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/fub01.pdf](http://trec.nist.gov/pubs/trec10/papers/fub01.pdf)
- :material-file-search: **Runs:** [fub01ne](./web/runs.md#fub01ne) | [fub01idf](./web/runs.md#fub01idf) | [fub01ne2](./web/runs.md#fub01ne2) | [fub01be2](./web/runs.md#fub01be2)

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

- :fontawesome-solid-user-group: **Participant:** [IIT](./web/participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/IIT-TREC10.pdf](http://trec.nist.gov/pubs/trec10/papers/IIT-TREC10.pdf)
- :material-file-search: **Runs:** [iit01m](./web/runs.md#iit01m) | [iit01t](./web/runs.md#iit01t) | [iit01tfc](./web/runs.md#iit01tfc) | [iit01tde](./web/runs.md#iit01tde) | [iit01st](./web/runs.md#iit01st) | [iit01stb](./web/runs.md#iit01stb)

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

## Question Answering 

#### Overview of the TREC 2001 Question Answering Track

_Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/qa10.pdf](http://trec.nist.gov/pubs/trec10/papers/qa10.pdf)
??? abstract "Abstract"
	
	The TREC question answering track is an effort to bring the benefits of large-scale evaluation to bear on the question answering problem. In its third year, the track continued to focus on retrieving small snippets of text that contain an answer to a question. However, several new conditions were added to increase the realism, and the difficulty, of the task. In the main task, questions were no longer guaranteed to have an answer in the collection; systems returned a response of 'NIL' to indicate their belief that no answer was present. In the new list task, systems assembled a set of instances as the response for a question, requiring the ability to distinguish among instances found in multiple documents. Another new task, the context task, required systems to track discourse objects through a series of questions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Voorhees01a.bib) "
	```
	@inproceedings{DBLP:conf/trec/Voorhees01a,
		author = {Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Overview of the {TREC} 2001 Question Answering Track},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/qa10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Voorhees01a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC-10: Filtering, QA, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yikun Guo, Yingju Xia, Zhe Feng_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./qa/participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf](http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf)
- :material-file-search: **Runs:** [FDUT10Q2](./qa/runs.md#fdut10q2)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC conference for the second time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we participate in the sub-task of adaptive and batch filtering. Vector representation and computation are heavily applied in filtering procedure. Four runs have been submitted, which includes one T10SU and one T10F run for adpative filtering, as well as another one T10SU and one T10F run for batch filtering. We have tried many natural language processing techniques in our QA system, including statistical sentence breaking, POS tagging, parsing, name entity tagging, chunking and semantic verification. Various sources of world knowledge are also incorporated, such as WordNet and geographic information. For web retrieval, relevant document set is first created by an extended Boolean retrieval engine, and then reordered according to link information. Four runs with different combination of topic coverage and link information are submitted. On video track, We take part in both of the sub-tasks. In the task of shot boundary detection, we have submitted two runs with different parameters. In the task of video retrieval, we have submitted the results of 17 topics among all the topics.
	

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

#### Aggressive Morphology and Lexical Relations for Query Expansion

_William A. Woods, Stephen J. Green, Paul Alan Martin, Ann Houston_

- :fontawesome-solid-user-group: **Participant:** [SUN](./qa/participants.md#sun)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/sun-trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/sun-trec10.pdf)
- :material-file-search: **Runs:** [mtsuna0](./qa/runs.md#mtsuna0) | [mtsuna1](./qa/runs.md#mtsuna1)

??? abstract "Abstract"
	
	Our submission to TREC this year is based on a combination of systems. The first is the conceptual indexing and retrieval system that was developed at Sun Microsystems Laboratories (Woods et al., 2000a; Woods et al., 2000b). The second is the MultiText system developed at the University of Waterloo (Clarke et al., 2000; Cormack et al., 2000). The conceptual indexing system was designed to help people find specific answers to specific questions in unrestricted text. It uses a combination of syntactic, semantic, and morphological knowledge, together with taxonomic subsumption techniques, to address differences in terminology between a user’s queries and the material that may answer them. At indexing time, the system builds a conceptual taxonomy of all the words and phrases in the indexed material. This taxonomy is based on the morphological structure of words, the syntactic structure of phrases, and semantic relations between meanings of words that it knows in its lexicon. It was not, however, designed as a question answering system. Our results from last year, while encour- aging, showed that we needed more work in the area of question analysis (i.e., “What would constitute an answer to this question?”) and answer determination (i.e., “Does this retrieved passage actually answer the question?”) to support our relaxation ranking passage retrieval algorithm. After conversations with the researchers at the University of Waterloo, we decided to submit a run where we would provide front-end processing consisting of query formulation and query expansion using our automatically derived taxonomy and Waterloo would provide the back-end processing via their MultiText passage retrieval system and their answer selection component. The result is a direct comparison of two question answering systems that differ only in the query formulation component.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WoodsGMH01.bib) "
	```
	@inproceedings{DBLP:conf/trec/WoodsGMH01,
		author = {William A. Woods and Stephen J. Green and Paul Alan Martin and Ann Houston},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Aggressive Morphology and Lexical Relations for Query Expansion},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/sun-trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WoodsGMH01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-10 Experiments at CAS-ICT: Filtering, Web and QA

_Bin Wang, Hongbo Xu, Zhifeng Yang, Yue Liu, Xueqi Cheng, Dongbo Bu, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [chinese_academy](./qa/participants.md#chinese_academy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf](http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf)
- :material-file-search: **Runs:** [ICTQA10a](./qa/runs.md#ictqa10a) | [ICTQA10b](./qa/runs.md#ictqa10b) | [ICTQA10c](./qa/runs.md#ictqa10c)

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

#### University of Alicante at TREC-10

_José Luis Vicedo González, Antonio Ferrández Rodríguez, Fernando Llopis_

- :fontawesome-solid-user-group: **Participant:** [Alicante](./qa/participants.md#alicante)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/Alicante__TREC-10_Paper.pdf](http://trec.nist.gov/pubs/trec10/papers/Alicante__TREC-10_Paper.pdf)
- :material-file-search: **Runs:** [ALIC01M1](./qa/runs.md#alic01m1) | [ALIC01M2](./qa/runs.md#alic01m2)

??? abstract "Abstract"
	
	This paper describes the architecture, operation and results obtained with the Question Answering prototype developed in the Department of Language Processing and Information Systems at the University of Alicante. Our system is based on our TREC-9 approach where different improvements have been introduced. Essentially these modifications are twofold: the introduction of a passage retrieval module at first stage retrieval and the redefinition of our semantic approach for paragraph selection and answer extraction.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VicedoFL01.bib) "
	```
	@inproceedings{DBLP:conf/trec/VicedoFL01,
		author = {Jos{\'{e}} Luis Vicedo Gonz{\'{a}}lez and Antonio Ferr{\'{a}}ndez Rodr{\'{\i}}guez and Fernando Llopis},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {University of Alicante at {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/Alicante\_\_TREC-10\_Paper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VicedoFL01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Patterns of Potential Answer Expressions as Clues to the Right Answers

_Martin M. Soubbotin_

- :fontawesome-solid-user-group: **Participant:** [InsightSoft](./qa/participants.md#insightsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/insight_trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/insight_trec10.pdf)
- :material-file-search: **Runs:** [insight](./qa/runs.md#insight)

??? abstract "Abstract"
	
	The core of our question-answering mechanism is searching for predefined patterns of textual expressions that may be interpreted as answers to certain types of questions. The presence of such patterns in analyzed answer-string candidates may provide evidence of the right answer. The answer-string candidates are created by cutting up relatively-large source documents passages containing the query terms or their synonyms/substitutes. indicative patterns. The specificity of our approach is: placing the use of indicative patterns in the core of the QA approach; aiming at the comprehensive and systematic use of such indicators; defining various structural types of the indicative patterns, including nontrivial and sophisticated ones; developing accessory techniques that ensure effective performance of the approach. We believe that the use of indicative patterns for question answering can be considered as a special case of the more general approach to text information retrieval that contrasts with linguistics-oriented methodology
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Soubbotin01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Soubbotin01,
		author = {Martin M. Soubbotin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Patterns of Potential Answer Expressions as Clues to the Right Answers},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/insight\_trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Soubbotin01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Learning Components for A Question-Answering System

_Dan Roth, Gio Kao Kao, Xin Li, Ramya Nagarajan, Vasin Punyakanok, Nick Rizzolo, Wen-tau Yih, Cecilia Ovesdotter Alm, Liam Gerard Moran_

- :fontawesome-solid-user-group: **Participant:** [UIUC](./qa/participants.md#uiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/uiuc.pdf](http://trec.nist.gov/pubs/trec10/papers/uiuc.pdf)
- :material-file-search: **Runs:** [UIUC](./qa/runs.md#uiuc)

??? abstract "Abstract"
	
	We describe a machine learning approach to the development of several key components in a question answering system and the way they were used in the UIUC QA system. A unified learning approach is used to develop a part-of-speech tagger, a shallow parser, a named entity recognizer and a module for identifying a question's target. These components are used in analyzing questions, as well as in the analysis of selected passages that may contain the sought after answer. The performance of the learned modules seems to be very high, (e.g., mid 90% for identifying noun phrases in sentences), though evaluating those on a large number of passages proved to be time consuming. Other components of the system, a passage retrieval module and an answer selection module, were put together in an ad-hoc fashion and significantly affected the overall performance. We ran the system only over about 60% of questions, answering a third of them correctly.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RothKLNPRYAM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/RothKLNPRYAM01,
		author = {Dan Roth and Gio Kao Kao and Xin Li and Ramya Nagarajan and Vasin Punyakanok and Nick Rizzolo and Wen{-}tau Yih and Cecilia Ovesdotter Alm and Liam Gerard Moran},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Learning Components for {A} Question-Answering System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/uiuc.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RothKLNPRYAM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Word Proximity QA System

_Philip Rennert_

- :fontawesome-solid-user-group: **Participant:** [ecwise](./qa/participants.md#ecwise)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/ec_wise.pdf](http://trec.nist.gov/pubs/trec10/papers/ec_wise.pdf)
- :material-file-search: **Runs:** [ecw1ps](./qa/runs.md#ecw1ps) | [ecw1csx](./qa/runs.md#ecw1csx)

??? abstract "Abstract"
	
	This is a question answering system with very little NLP, based on question-category-dependent selection and weighting of search terms, selecting answer strings centered around words most commonly found near search terms. Its performance was medium, with a 0.2 MR. Certain category strategies may be of interest to other Aers, and are described.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Rennert01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Rennert01,
		author = {Philip Rennert},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Word Proximity {QA} System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/ec\_wise.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Rennert01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Use of WordNet Hypernyms for Answering What-Is Questions

_John M. Prager, Jennifer Chu-Carroll, Krzysztof Czuba_

- :fontawesome-solid-user-group: **Participant:** [ibm-prager](./qa/participants.md#ibm-prager)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/Trec10Prager.pdf](http://trec.nist.gov/pubs/trec10/papers/Trec10Prager.pdf)
- :material-file-search: **Runs:** [IBMKS1M3](./qa/runs.md#ibmks1m3) | [IBMKS1M1](./qa/runs.md#ibmks1m1) | [IBMKS1M2](./qa/runs.md#ibmks1m2)

??? abstract "Abstract"
	
	We present a preliminary analysis of the use of WordNet hypernyms for answering “What-is” questions. We analyse the approximately 130 definitional questions in the TREC10 corpus with respect to our technique of Virtual Annotation (VA), which has previously been shown to be effective on the TREC9 definitional question set and other questions. We discover that VA is effective on a subset of the TREC10 definitional questions, but that some of these questions seem to need a user model to generate correct answers, or at least answers that agree with the NIST judges. Furthermore, there remains a large enough subset of definitional questions that cannot benefit at all from the WordNet isa-hierarchy, prompting the need to investigate alternative external resources.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PragerCC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/PragerCC01,
		author = {John M. Prager and Jennifer Chu{-}Carroll and Krzysztof Czuba},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Use of WordNet Hypernyms for Answering What-Is Questions},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/Trec10Prager.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PragerCC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The QUANTUM Question Answering System

_Luc Plamondon, Guy Lapalme, Leila Kosseim_

- :fontawesome-solid-user-group: **Participant:** [UMontreal](./qa/participants.md#umontreal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/articleUdeM.pdf](http://trec.nist.gov/pubs/trec10/papers/articleUdeM.pdf)
- :material-file-search: **Runs:** [UdeMlistB](./qa/runs.md#udemlistb) | [UdeMlistP](./qa/runs.md#udemlistp) | [UdeMmainOk60](./qa/runs.md#udemmainok60) | [UdeMmainOk80](./qa/runs.md#udemmainok80) | [UdeMmainQt80](./qa/runs.md#udemmainqt80)

??? abstract "Abstract"
	
	We participated to the TREC-X QA main task and list task with a new system named QUANTUM, which analyzes questions with shallow parsing techniques and regular expressions. Instead of using a question classification based on entity types, we classify the questions according to generic mechanisms (which we call extraction func-tions) for the extraction of candidate answers. We take advantage of the Okapi information retrieval system for one-paragraph-long passage retrieval. We make an extensive use of the Alembic named-entity tagger and the Word Net semantic network to extract candidate answers from those passages. We deal with the possibility of no-answer questions (NIL) by looking for a significant score drop between the extracted candidate answers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PlamondonLK01.bib) "
	```
	@inproceedings{DBLP:conf/trec/PlamondonLK01,
		author = {Luc Plamondon and Guy Lapalme and Leila Kosseim},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {QUANTUM} Question Answering System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/articleUdeM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PlamondonLK01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-10 Experiments at KAIST: Batch Filtering and Question Answering

_Jong-Hoon Oh, Kyung-Soon Lee, Du-Seong Chang, Chung Won Seo, Key-Sun Choi_

- :fontawesome-solid-user-group: **Participant:** [KAIST](./qa/participants.md#kaist)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/kaist-trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/kaist-trec10.pdf)
- :material-file-search: **Runs:** [KAISTQAMAIN1](./qa/runs.md#kaistqamain1) | [KAISTQAMAIN2](./qa/runs.md#kaistqamain2) | [KAISTQALIST2](./qa/runs.md#kaistqalist2) | [KAISTQACTX](./qa/runs.md#kaistqactx) | [KAISTQALIST1](./qa/runs.md#kaistqalist1)

??? abstract "Abstract"
	
	In TREC-10, we participated in two tasks: batch filtering task in the filtering task, and question answering task. In question answering task, we participated in three sub-tasks (main task, list task, and context task). In batching filtering task, we experimented a filtering technique, which unifies the results of support vector machines for subtopics subdivided by incremental clustering. For a topic, we generated subtopics by detecting similar documents in training relevant documents, and unified the results of SVM classifier for subtopics by OR set operation. In question answering task, we submitted two runs for main task (KAISTQAMAIN1, KAISTQAMAIN2), two runs for list task (KAISTQALIST1, KAISTQALIST2), and one run for context task (KAISTQACTX).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OhLCSC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/OhLCSC01,
		author = {Jong{-}Hoon Oh and Kyung{-}Soon Lee and Du{-}Seong Chang and Chung Won Seo and Key{-}Sun Choi},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-10} Experiments at {KAIST:} Batch Filtering and Question Answering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/kaist-trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OhLCSC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Tequesta: The University of Amsterdam's Textual Question Answering  System

_Christof Monz, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uva](./qa/participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/trec10-Monz-deRijke.pdf](http://trec.nist.gov/pubs/trec10/papers/trec10-Monz-deRijke.pdf)
- :material-file-search: **Runs:** [UAmsT10qaL1](./qa/runs.md#uamst10qal1) | [UAmsT10qaL2](./qa/runs.md#uamst10qal2) | [UAmsT10qaM1](./qa/runs.md#uamst10qam1) | [UAmsT10qaM3](./qa/runs.md#uamst10qam3) | [UAmsT10qaM2](./qa/runs.md#uamst10qam2)

??? abstract "Abstract"
	
	We describe our participation in the TREC-10 Question Answering track. All our runs used the Tequesta system; we provide a detailed account of the natural language processing and inferencing techniques that are part of Tequesta. We also summarize and discuss our results, which concern both the main task and the list task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MonzR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/MonzR01,
		author = {Christof Monz and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Tequesta: The University of Amsterdam's Textual Question Answering System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/trec10-Monz-deRijke.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MonzR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multilingual Question/Answering: the DIOGENE System

_Bernardo Magnini, Matteo Negri, Roberto Prevete, Hristo Tanev_

- :fontawesome-solid-user-group: **Participant:** [itc-irst](./qa/participants.md#itc-irst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/IrstQA.pdf](http://trec.nist.gov/pubs/trec10/papers/IrstQA.pdf)
- :material-file-search: **Runs:** [irstqa01](./qa/runs.md#irstqa01)

??? abstract "Abstract"
	
	This paper presents the DIOGENE question/answering system developed at ITC- Irst. The system is based on a rather standard architecture which includes three components for question processing, search and answer extraction. Linguistic processing strongly relies on MULTIWORDNET, an extended version of the English WORDNET. The system has been designed to address two promising directions: multilingual question/answering and question/answering on the Web. The results obtained in the TREC-10 main task will be presented and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MagniniNPT01.bib) "
	```
	@inproceedings{DBLP:conf/trec/MagniniNPT01,
		author = {Bernardo Magnini and Matteo Negri and Roberto Prevete and Hristo Tanev},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Multilingual Question/Answering: the {DIOGENE} System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/IrstQA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MagniniNPT01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CL Research Experiments in TREC-10 Question Answering

_Kenneth C. Litkowski_

- :fontawesome-solid-user-group: **Participant:** [clresearch](./qa/participants.md#clresearch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/clresearch-t10.pdf](http://trec.nist.gov/pubs/trec10/papers/clresearch-t10.pdf)
- :material-file-search: **Runs:** [clr01b1](./qa/runs.md#clr01b1) | [clr01c1](./qa/runs.md#clr01c1) | [clr01l1](./qa/runs.md#clr01l1) | [clr01l2](./qa/runs.md#clr01l2) | [clr01b2](./qa/runs.md#clr01b2)

??? abstract "Abstract"
	
	CL Research's question-answering system (DIMAP-QA) for TREC-10 only slightly extends its semantic relation triple (logical form) technology in which documents are fully parsed and databases built around discourse entities. Time constraints did not allow us to make various changes planned from TREC-9. TREC-10 changes made fuller use of the integrated machine-readable lexical resources and extended the question-answering capability to handle list and context questions. Experiments to further exploit the dictionary resources were not fully completed at the time of the TREC-10 submission, affecting planned revisions in other QA components. The official score for the main TREC-10 QA task was 0.120 (compared to 0.135 in TREC-9), based on processing 10 of the top 50 documents provided by NIST, compared to the average of 0.235 for 67 submissions. Post-hoc analysis suggests a more accurate assessment of DIMAP-QA's performance in identifying answers is 0.217. For the list task, the CL Research average accuracy was 0.13 and 0.12 for two runs compared to the average of 0.222. For the context questions, CL Research had mean reciprocal rank score of 0.178, 5th of the 7 submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Litkowski01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Litkowski01,
		author = {Kenneth C. Litkowski},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{CL} Research Experiments in {TREC-10} Question Answering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/clresearch-t10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Litkowski01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Description of NTU System at TREC-10 QA Track

_Chuan-Jie Lin, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [NTU](./qa/participants.md#ntu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/NTU_TREC10.pdf](http://trec.nist.gov/pubs/trec10/papers/NTU_TREC10.pdf)
- :material-file-search: **Runs:** [qntuam1](./qa/runs.md#qntuam1) | [qntuam2](./qa/runs.md#qntuam2) | [qntuac1](./qa/runs.md#qntuac1) | [qntual1](./qa/runs.md#qntual1) | [qntual2](./qa/runs.md#qntual2)

??? abstract "Abstract"
	
	In the past years, we attended the 250-bytes group. Our main strategy was to measure the similarity score (or the informative score) of each candidate sentence to the question sentence. The similarity score was computed by sums of weights of cooccurred question keywords. To meet the requirement of shorter answering texts proposed in this year, we adapt our system, and experiment on a new strategy that is focused on named entities only. The similarity score is now measured in terms of the distances to the question keywords in the same document. The MRR score is 0.145. Section 2 will deal with our work in the main task. We also attended the list task and the context task this year. In the list task, the algorithm is almost the same as the one in the main task except that we have to avoid duplicate answers and find the new answers at the same time. Positions of the candidates in the answering texts should be considered. We will talk about this in Section 3. In the context task, how to keep the context, and what the answers of the previous questions can help are the main issues. In our strategy, the answers of the first question are kept when answering the subsequent questions, but the answers of the other ones (denoted by question i) are kept only if question i has a co-referential relationship to its previous one. Section 4 will describe this strategy in more detail.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinC01,
		author = {Chuan{-}Jie Lin and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Description of {NTU} System at {TREC-10} {QA} Track},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/NTU\_TREC10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SiteQ: Engineering High Performance QA System Using Lexico-Semantic  Pattern Matching and Shallow NLP

_Gary Geunbae Lee, Jungyun Seo, Seungwoo Lee, Hanmin Jung, Bong-Hyun Cho, Changki Lee, Byung-Kwan Kwak, Jeongwon Cha, Dongseok Kim, Joohui An, Harksoo Kim, Kyungsun Kim_

- :fontawesome-solid-user-group: **Participant:** [postech](./qa/participants.md#postech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/SiteQ_trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/SiteQ_trec10.pdf)
- :material-file-search: **Runs:** [posqa10a](./qa/runs.md#posqa10a)

??? abstract "Abstract"
	
	In TREC-10, we participated in the web track (only ad-hoc task) and the QA track (only main task). In the QA track, our QA system (SiteQ) has general architecture with three processing steps: question processing, passage selection and answer processing. The key technique is LSP's (Lexico-Semantic Patterns) that are composed of linguistic entries and semantic types. LSP grammars constructed from various resources are used for answer type determination and answer matching. We also adapt AAD (Abbreviation-Appositive-Definition) processing for the queries that answer type cannot be determined or expected, encyclopedia search for increasing the matching coverage between query terms and passages, and pivot detection for the distance calculation with answer candidates. We used two-level answer types consisted of 18 upper-level types and 47 lower-level types. Semantic category dictionary, WordNet, POS combined with lexicography and a stemmer were all applied to construct the LSP knowledge base. CSMT (Category Sense-code Mapping Table) tried to find answer types using the matching between semantic categories and sense-codes from WordNet. Evaluation shows that MRR for 492 questions is 0.320 (strict), which is considerably higher than the average MRR of other 67 runs. In the Web track, we focused on the effectiveness of both noun phrase extraction and our new PRF (Pseudo Relevance Feedback). We confirmed that our query expansion using PRF with TSV function adapting TF factor contributed to better performance, but noun phrases did not contribute much. It needs more observations for us to make elaborate rules of tag patterns for the construction of better noun phrases.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeSLJCLKCKAKK01.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeSLJCLKCKAKK01,
		author = {Gary Geunbae Lee and Jungyun Seo and Seungwoo Lee and Hanmin Jung and Bong{-}Hyun Cho and Changki Lee and Byung{-}Kwan Kwak and Jeongwon Cha and Dongseok Kim and Joohui An and Harksoo Kim and Kyungsun Kim},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {SiteQ: Engineering High Performance {QA} System Using Lexico-Semantic Pattern Matching and Shallow {NLP}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/SiteQ\_trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeSLJCLKCKAKK01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC2001 Question-Answer, Web and Cross Language Experiments using  PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./qa/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf](http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf)
- :material-file-search: **Runs:** [pir1Qqa3](./qa/runs.md#pir1qqa3) | [pir1Qqa2](./qa/runs.md#pir1qqa2) | [pir1Qqa1](./qa/runs.md#pir1qqa1) | [pir1Qli2](./qa/runs.md#pir1qli2) | [pir1Qli1](./qa/runs.md#pir1qli1) | [pir1Qctx3](./qa/runs.md#pir1qctx3) | [pir1Qctx2](./qa/runs.md#pir1qctx2)

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

#### NTT Question Answering System in TREC 2001

_Hideto Kazawa, Hideki Isozaki, Eisaku Maeda_

- :fontawesome-solid-user-group: **Participant:** [nttcom_kazawa](./qa/participants.md#nttcom_kazawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/nttcs-trec10-proceeding.pdf](http://trec.nist.gov/pubs/trec10/papers/nttcs-trec10-proceeding.pdf)
- :material-file-search: **Runs:** [nttcs10main](./qa/runs.md#nttcs10main)

??? abstract "Abstract"
	
	In this report, we describe our question-answering system SAIQA-e (System for Advanced Interactive Question Answering in English) which ran the main task of TREC-10’s QA-track. Our system has two characteristics (1) named entity recognition based on support vector machines and (2) heuristic apposition detection. The MPR score of the main task is 0.228 and experimental results indicate the effectiveness of the above two steps in terms of answer extraction accuracy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KazawaIM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/KazawaIM01,
		author = {Hideto Kazawa and Hideki Isozaki and Eisaku Maeda},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{NTT} Question Answering System in {TREC} 2001},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/nttcs-trec10-proceeding.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KazawaIM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM's Statistical Question Answering System - TREC-10

_Abraham Ittycheriah, Martin Franz, Salim Roukos_

- :fontawesome-solid-user-group: **Participant:** [ibm-franz](./qa/participants.md#ibm-franz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/trec2001.pdf](http://trec.nist.gov/pubs/trec10/papers/trec2001.pdf)
- :material-file-search: **Runs:** [ibmsqa01b](./qa/runs.md#ibmsqa01b) | [ibmsqa01a](./qa/runs.md#ibmsqa01a) | [ibmsqa01c](./qa/runs.md#ibmsqa01c)

??? abstract "Abstract"
	
	We describe herein the IBM Statistical Question Answering system for TREC-10 in detail. Based on experiences in TREC-9, we have adapted our system to deal with definition type questions and furthermore completed the trainability aspect of our question-answering system. The experiments performed in this evaluation confirmed our hypothesis that post-processing the IR engine results can achieve the same performance as incorporating query expansion terms into the retrieval engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/IttycheriahFR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/IttycheriahFR01,
		author = {Abraham Ittycheriah and Martin Franz and Salim Roukos},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {IBM's Statistical Question Answering System - {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/trec2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/IttycheriahFR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Use of External Knowledge of Factoid QA

_Eduard H. Hovy, Ulf Hermjakob, Chin-Yew Lin_

- :fontawesome-solid-user-group: **Participant:** [ISI-USC](./qa/participants.md#isi-usc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/TREC10-webclopedia.pdf](http://trec.nist.gov/pubs/trec10/papers/TREC10-webclopedia.pdf)
- :material-file-search: **Runs:** [isi1a50](./qa/runs.md#isi1a50) | [ISI1b50](./qa/runs.md#isi1b50) | [isi1l50](./qa/runs.md#isi1l50)

??? abstract "Abstract"
	
	This paper describes recent development in the Webclopedia QA system, focusing on the use of knowledge resources such as WordNet and a QA typology to improve the basic operations of candidate answer retrieval, ranking, and answer matching.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HovyHL01.bib) "
	```
	@inproceedings{DBLP:conf/trec/HovyHL01,
		author = {Eduard H. Hovy and Ulf Hermjakob and Chin{-}Yew Lin},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The Use of External Knowledge of Factoid {QA}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/TREC10-webclopedia.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HovyHL01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Answering Complex, List and Context Questions with LCC's Question-Answering  Server

_Sanda M. Harabagiu, Dan I. Moldovan, Marius Pasca, Mihai Surdeanu, Rada Mihalcea, Roxana Girju, Vasile Rus, V. Finley Lacatusu, Paul Morarescu, Razvan C. Bunescu_

- :fontawesome-solid-user-group: **Participant:** [LCC](./qa/participants.md#lcc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/lcc-trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/lcc-trec10.pdf)
- :material-file-search: **Runs:** [LCC1](./qa/runs.md#lcc1) | [LCC2](./qa/runs.md#lcc2) | [LCC3](./qa/runs.md#lcc3)

??? abstract "Abstract"
	
	This paper presents the architecture of the Question-Answering Server (QAS) developed at the Language Computer Corporation (LCC) and used in the TREC-10 evaluations. LCC's QASTM extracts answers for (a) factual questions of vairable degree of difficulty; (b) questions that expect lists of answers; and (c) questions posed in the context of previous questions and answers. One of the major novelties is the implementation of bridging inference mechanisms that guide the search for answers to complex questions. Additionally, LCC's QASTM encodes an efficient way of modeling context via reference resolution. In TREC-10, this system generated an RAR of 0.58 on the main task and 0.78 on the context task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HarabagiuMPSMGRLMB01.bib) "
	```
	@inproceedings{DBLP:conf/trec/HarabagiuMPSMGRLMB01,
		author = {Sanda M. Harabagiu and Dan I. Moldovan and Marius Pasca and Mihai Surdeanu and Rada Mihalcea and Roxana Girju and Vasile Rus and V. Finley Lacatusu and Paul Morarescu and Razvan C. Bunescu},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Answering Complex, List and Context Questions with LCC's Question-Answering Server},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/lcc-trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HarabagiuMPSMGRLMB01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding An Answer Based on the Recognition of the Question Focus

_Olivier Ferret, Brigitte Grau, Martine Hurault-Plantet, Gabriel Illouz, Laura Monceaux, Isabelle Robba, Anne Vilnat_

- :fontawesome-solid-user-group: **Participant:** [limsi](./qa/participants.md#limsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/qaLIR.pdf](http://trec.nist.gov/pubs/trec10/papers/qaLIR.pdf)
- :material-file-search: **Runs:** [QALIR1](./qa/runs.md#qalir1) | [QALIR2](./qa/runs.md#qalir2) | [QALIR3](./qa/runs.md#qalir3)

??? abstract "Abstract"
	
	In this report we describe how the QALC system (the Question-Answering program of the LIR group at LIMSI-CNRS, already involved in the QA-track evaluation at TREC9), was improved in order to better extract the very answer in selected sentences. The purpose of the main Question-Answering track in TREC10 was to find text sequences no longer than 50 characters or to produce a 'no answer' response in case of a lack of answer in the TREC corpus. As QALC first retrieves relevant sentences within the document corpus, our main question was: how to find the answer in a sentence? This question involves two kinds of answer: a) it is better to know what you look for and b) you have to know the location of what you look for. The first case is solved by applying a question analysis process. This process determines the type of the expected answer in term of named entity. This named entity is searched for in the sentences. However, all answers cannot be expressed in term of a named entity. Definition questions or explanation questions for example demand phrases (noun phrases or verb phrases) as answers. So, after having studied the structure of subpart of sentences that contained answers, we defined criteria to be able to locate the precise answer within a sentence. These criteria consist in defining triplets composed of a question category, the question focus and an associated list of templates allowing the location of the answer according to the focus place in the candidate sentence. In the following sections, we will detail this novel aspect in our system by presenting the question analysis module, the different processes involved in the answer module and the results we obtained. Before, we give a brief overall presentation of QALC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FerretGHIMRV01.bib) "
	```
	@inproceedings{DBLP:conf/trec/FerretGHIMRV01,
		author = {Olivier Ferret and Brigitte Grau and Martine Hurault{-}Plantet and Gabriel Illouz and Laura Monceaux and Isabelle Robba and Anne Vilnat},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Finding An Answer Based on the Recognition of the Question Focus},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/qaLIR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FerretGHIMRV01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Web Reinforced Question Answering (MultiTest Experiments for TREC  2001)

_Charles L. A. Clarke, Gordon V. Cormack, Thomas R. Lynam, C. M. Li, G. L. McLearn_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./qa/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/mtA.pdf](http://trec.nist.gov/pubs/trec10/papers/mtA.pdf)
- :material-file-search: **Runs:** [uwmta0](./qa/runs.md#uwmta0) | [uwmta1](./qa/runs.md#uwmta1) | [uwmta2](./qa/runs.md#uwmta2) | [uwmtal0](./qa/runs.md#uwmtal0) | [uwmtal1](./qa/runs.md#uwmtal1) | [uwmtac0](./qa/runs.md#uwmtac0)

??? abstract "Abstract"
	
	For TREC 2001, the MultiText Project concentrated on the QA track. Over the past year, we made substantial enhancements to our A system in three general areas. First, we explored a number of methods for taking advantage of external resources (including encyclopedias, dictionaries and Web data) as sources for answer validation, improving our ability to identify correct answers in the target corpus. Of the methods explored, the use of Web data to reinforce answer selection proved to be particular value. Second, we made a large number of incremental improvements to the existing system components. For example, in our parsing component, the query generation and answer category identification algorithms were extended and tuned, as were the named entity identification algorithms used in our answer extraction component. Finally, we made a careful analysis of the problem of null questions, those that have no answer in the target corpus, and developed a general approach to the problem. A basic method for handling null questions, based on the analysis, was added to our system. We submitted three runs for the main task of the QA track. The first run (uwmta1) was based on the enhanced system described above, including the full use of Web resources for answer validation. For the second run (uwmta2) the Web resources were not used for validation, but the system was otherwise identical. A comparison between these runs represents a major goal of our TREC experimental work and the major concern of this paper. The final run (uwmta0) tests a last-minute enhancement. For this run a feedback loop was added to the system, in which candidate answer terms were merged back into the query used for passage retrieval. While answer feedback was not an area of significant effort for TREC 2001, and the intial results were disappointing, it represents an area in which future work is planned. Our other TREC 2001 runs are related to the QA track. Along with the QA runs submitted for the main task, we also submitted exploratory runs for the list (uwmtal0 and uwmtal1) and context (umtacO) tasks. These runs were generated through minor modifications to the existing system, and represent preliminary attempts at participation rather than serious attempts at high performance. Our runs for the Web track (uwmtawO, uwmtawl, and uwmtaw2) are related to our QA runs. These runs were generated by our QA system by treating the topic title as a question and using the ranked list of documents containing the best answers as the result. Finally, the runs submitted by Sun Microsystems (tsuna0 and mtsuna1) were generated using our system as the backend and the Sun parser as the frontend. However, the integration between Sun and MultiText was performed in a short period of time, and these runs should also be viewed as preliminary experiments that point toward future work. In the remainder of the paper we focus on our primary runs for the main task of the QA track. In the next section we provide an overview of the QA system used for our TREC 2001 experiments, including a discussion of our technique for Web reinforcement. In section 3 we present our approach to the problem of null questions. Section 4 details our experimental results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCLLM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCLLM01,
		author = {Charles L. A. Clarke and Gordon V. Cormack and Thomas R. Lynam and C. M. Li and G. L. McLearn},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Web Reinforced Question Answering (MultiTest Experiments for {TREC} 2001)},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/mtA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCLLM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Question Answering: CNLP at the TREC-10 Question Answering Track

_Jiangping Chen, Anne Diekema, Mary D. Taffet, Nancy J. McCracken, Necati Ercan Ozgencil, Özgür Yilmazel, Elizabeth D. Liddy_

- :fontawesome-solid-user-group: **Participant:** [Syracuse](./qa/participants.md#syracuse)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/cnlptrec10.pdf](http://trec.nist.gov/pubs/trec10/papers/cnlptrec10.pdf)
- :material-file-search: **Runs:** [SUT10DOCLT](./qa/runs.md#sut10doclt) | [SUT10DOCMT](./qa/runs.md#sut10docmt) | [SUT10PARLT](./qa/runs.md#sut10parlt) | [SUT10PARMT](./qa/runs.md#sut10parmt)

??? abstract "Abstract"
	
	This paper describes the retrieval experiments for the main task and list task of the TREC-10 question-answering track. The question answering system described automatically finds answers to questions in a large document collection. The system uses a two-stage retrieval approach to answer finding based on matching of named entities, linguistic patterns, and keywords. In answering a question, the system carries out a detailed query analysis that produces a logical query representation, an indication of the question focus, and answer clue words.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenDTMOYL01.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenDTMOYL01,
		author = {Jiangping Chen and Anne Diekema and Mary D. Taffet and Nancy J. McCracken and Necati Ercan Ozgencil and {\"{O}}zg{\"{u}}r Yilmazel and Elizabeth D. Liddy},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Question Answering: {CNLP} at the {TREC-10} Question Answering Track},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/cnlptrec10.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenDTMOYL01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Grammatical Relations, Answer Frequencies and the World Wide  Web for TREC Question Answering

_Sabine Buchholz_

- :fontawesome-solid-user-group: **Participant:** [tilburg](./qa/participants.md#tilburg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/TilburgILK.pdf](http://trec.nist.gov/pubs/trec10/papers/TilburgILK.pdf)
- :material-file-search: **Runs:** [TilburgILKs](./qa/runs.md#tilburgilks) | [TilburgILK](./qa/runs.md#tilburgilk)

??? abstract "Abstract"
	
	This year, we participated for the first time in TREC, and entered two runs for the main task of the TREC 2001 question answering track. Both runs use a simple baseline component implemented especially for TREC, and a high-level NLP component (called Shapaga) that uses various NLP tools developed earlier by our group. Shapaga imposes many linguistic constraints on potential answers strings which results in not so many answers being found but those that are found have a reasonably high precision. The difference between the two runs is that the first applies Shapaga to the TREC document collection only, whereas the second one also uses it on the World Wide Web (WWW). Answers found there are then mapped back to the TREC collection. The first run achieved a MRR of 0.122 under the strict evaluation (and 0.128 lenient), the second one 0.210 (0.234). We argue that the better performance is due to the much larger number of documents that Shapaqa-WWW's answers are based on.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Buchholz01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Buchholz01,
		author = {Sabine Buchholz},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Using Grammatical Relations, Answer Frequencies and the World Wide Web for {TREC} Question Answering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/TilburgILK.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Buchholz01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Data-Intensive Question Answering

_Eric Brill, Jimmy Lin, Michele Banko, Susan T. Dumais, Andrew Y. Ng_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./qa/participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/Trec2001Notebook.AskMSRFinal.pdf](http://trec.nist.gov/pubs/trec10/papers/Trec2001Notebook.AskMSRFinal.pdf)
- :material-file-search: **Runs:** [askmsr](./qa/runs.md#askmsr) | [askmsr2](./qa/runs.md#askmsr2)

??? abstract "Abstract"
	
	Microsoft Research Redmond participated for the first time in TREC this year, focusing on the question answering track. There is a separate report in this volume on the Microsoft Research Cambridge submissions for the filtering and Web tracks (Robertson et al., 2002). We have been exploring data-driven techniques for Web question answering, and modified our system somewhat for participation in TREC QA. We submitted two runs for the main QA track (AskMSR and AskMSR2). Data-driven methods have proven to be powerful techniques for natural language processing. It is still unclear to what extent this success can be attributed to specific techniques, versus simply the data itself. For example, Banko and Brill (2001) demonstrated that for confusion set disambiguation, a prototypical disambiguation-in-string-context problem, the amount of data used far dominates the learning method employed in improving labeling accuracy. The more training data that is used, the greater the chance that a new sample being processed can be trivially related to samples appearing in the training data, thereby lessening the need for any complex reasoning that may be beneficial in cases of sparse training data. The idea of allowing the data, instead of the methods, do most of the work is what motivated our particular approach to the TREC Question Answering task. One of the biggest challenges in TREC-style QA is overcoming the surface string mismatch between the question formulation and the string containing its answer. For some Question/Answer pairs, deep reasoning is needed to relate the two. The larger the data set from which we can draw answers, the greater the chance we can find an answer that holds a simple, easily discovered relationship to the query string. Our approach to question answering is to take advantage of the vast amount of text data that is now available online. In contrast to many question answering systems that begin with rich linguistic resources (e.g., parsers, dictionaries, WordNet), we begin with data and use that to drive the design of our system. To do this, we first use simple techniques to look for answers to questions on the Web. Since the Web has orders of magnitude more data than the TREC QA document collection, simple techniques are likely to work here. After we have found suitable answer strings from online text, we project them onto the TREC corpus in search of supporting documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrillLBDN01.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrillLBDN01,
		author = {Eric Brill and Jimmy Lin and Michele Banko and Susan T. Dumais and Andrew Y. Ng},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Data-Intensive Question Answering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/Trec2001Notebook.AskMSRFinal.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BrillLBDN01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PiQASso: Pisa Question Answering System

_Giuseppe Attardi, Antonio Cisternino, Francesco Formica, Maria Simi, Alessandro Tommasi_

- :fontawesome-solid-user-group: **Participant:** [Pisa](./qa/participants.md#pisa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/piqasso.pdf](http://trec.nist.gov/pubs/trec10/papers/piqasso.pdf)
- :material-file-search: **Runs:** [prun001](./qa/runs.md#prun001) | [prun002](./qa/runs.md#prun002) | [prun003](./qa/runs.md#prun003)

??? abstract "Abstract"
	
	PiQASso is a Question Answering system based on a combination of modern IR techniques and a series of semantic filters for selecting paragraphs containing a justifiable answer. Semantic filtering is based on several NLP tools, including a dependency-based parser, a POS tagger, a NE tagger and a lexical database. Semantic analysis of questions is performed in order to extract keywords used in retrieval queries and to detect the expected answer type. Semantic analysis of retrieved paragraphs includes checking the presence of entities of the expected answer type and extracting logical relations between words. A paragraph is considered to justify an answer if similar relations are present in the question. When no answer passes the filters, the process is repeated applying further levels of query expansions in order to increase recall. We discuss results and limitations of the current implementation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AttardiCFST01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AttardiCFST01,
		author = {Giuseppe Attardi and Antonio Cisternino and Francesco Formica and Maria Simi and Alessandro Tommasi},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {PiQASso: Pisa Question Answering System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/piqasso.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AttardiCFST01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Qanda and the Catalyst Architecture

_Pranav Anand, David Anderson, John D. Burger, John Griffith, Marc Light, Scott A. Mardis, Alexander A. Morgan_

- :fontawesome-solid-user-group: **Participant:** [mitre](./qa/participants.md#mitre)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/MITRE-trecX-1.pdf](http://trec.nist.gov/pubs/trec10/papers/MITRE-trecX-1.pdf)
- :material-file-search: **Runs:** [MITRE01A](./qa/runs.md#mitre01a)

??? abstract "Abstract"
	
	Qanda is MITRE’s entry into the question-answering (QA) track of the TREC conference(Voorhees & Harman 2002). This year, Qanda was re-engineered to use a new architecture for human language technology called Catalyst, developed at MITRE for the DARPA TIDES program. The Catalyst architecture was chosen because it was specifically designed for fast processing and for combin- ing the strengths of Information Retrieval (IR) and Natural Language Processing (NLP) into a single framework. These technology fields are critical to the development of QA systems. The current Qanda implementation serves as a prototype for developing QA systems in the Catalyst architecture. This paper serves as an introduction to Catalyst and the Qanda implementation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnandABGLMM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnandABGLMM01,
		author = {Pranav Anand and David Anderson and John D. Burger and John Griffith and Marc Light and Scott A. Mardis and Alexander A. Morgan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Qanda and the Catalyst Architecture},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/MITRE-trecX-1.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnandABGLMM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Oracle at TREC 10: Filtering and Question-Answering

_Shamin Alpha, Paul Dixon, Ciya Liao, Changwen Yang_

- :fontawesome-solid-user-group: **Participant:** [oracle](./qa/participants.md#oracle)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/orcltrec10.pdf](http://trec.nist.gov/pubs/trec10/papers/orcltrec10.pdf)
- :material-file-search: **Runs:** [orcl1](./qa/runs.md#orcl1)

??? abstract "Abstract"
	
	Oracle’s objective in TREC-10 was to study the behavior of Oracle information retrieval in previously unexplored application areas. The software used was Oracle9i Text[1], Oracle’s full-text retrieval engine integrated with the Oracle relational database management system, and the Oracle PL/SQL procedural programming language. Runs were submitted in filtering and Q/A tracks. For the filtering track we submitted three runs, in adaptive filtering, batch filtering and routing. By comparing the TREC results, we found that the concepts (themes) extracted by Oracle Text can be used to aggregate document information content to simplify statistical processing. Oracle's Q/A system integrated information retrieval (IR) and information extraction (IE). The Q/A system relied on a combination of document and sentence ranking in IR, named entity tagging in IE and shallow parsing based classification of questions into pre-defined categories.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlphaDLY01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlphaDLY01,
		author = {Shamin Alpha and Paul Dixon and Ciya Liao and Changwen Yang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Oracle at {TREC} 10: Filtering and Question-Answering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/orcltrec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlphaDLY01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A ProtoType Question Answering System Using Syntactic and Semantic  Information for Answer Retrieval

_Enrique Alfonseca, Marco De Boni, José-Luis Jara-Valencia, Suresh Manandhar_

- :fontawesome-solid-user-group: **Participant:** [York](./qa/participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/yorkQA_paper.pdf](http://trec.nist.gov/pubs/trec10/papers/yorkQA_paper.pdf)
- :material-file-search: **Runs:** [yorkqa01](./qa/runs.md#yorkqa01) | [yorkqa02](./qa/runs.md#yorkqa02)

??? abstract "Abstract"
	
	This was our first entry at TREC and the system we presented was, due to time constraints, an incomplete prototype. Our main aims were to verify the usefulness of syntactic analysis for QA and to experiment with different semantic distance metrics in view of a more complete and fully integrated future system. To this end we made use of a part-of-speech tagger and NP chunker in conjunction with entity recognition and semantic distance metrics. We also envisaged experimenting with a shallow best first parser but time factors meant integration with the rest of the system was not achieved. Unfortunately due to time constraints no testing and no parameter tuning was carried out prior TREC. This in turn meant that a number of small bugs negatively influenced our results. Moreover it was not possible to carry out experiments in parameter tuning, meaning our system did not achieve optimal performance. Nevertheless we obtained reasonable results, the best score being 18.1% of the questions correct (with lenient judgements).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlfonsecaBJM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlfonsecaBJM01,
		author = {Enrique Alfonseca and Marco De Boni and Jos{\'{e}}{-}Luis Jara{-}Valencia and Suresh Manandhar},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {A ProtoType Question Answering System Using Syntactic and Semantic Information for Answer Retrieval},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/yorkQA\_paper.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AlfonsecaBJM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Cross-Language 

#### The TREC-2001 Cross-Language Information Retrieval Track: Searching  Arabic Using English, French or Arabic Queries

_Fredric C. Gey, Douglas W. Oard_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/clirtrack.pdf](http://trec.nist.gov/pubs/trec10/papers/clirtrack.pdf)
??? abstract "Abstract"
	
	Ten groups participated in the TREC-2001 cross-language information retrieval track, which focussed on retrieving Arabic language documents based on 25 queries that were originally prepared in English. French and Arabic translations of the queries were also available. This was the first year in which a large Arabic test collection was available, so a variety of approaches were tried and a rich set of experiments performed using resources such as machine translation, parallel corpora, several approaches to stemming and/or morphology, and both pre-translation and post-translation blind relevance feedback. On average, forty percent of the relevant documents discovered by a participating team were found by no other team, a higher rate than normally observed at TREC. This raises some concern that the relevance judgment pools may be less complete than has historically been the case.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GeyO01.bib) "
	```
	@inproceedings{DBLP:conf/trec/GeyO01,
		author = {Fredric C. Gey and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-2001} Cross-Language Information Retrieval Track: Searching Arabic Using English, French or Arabic Queries},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/clirtrack.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GeyO01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2001 Cross-lingual Retrieval at BBN

_Jinxi Xu, Alexander M. Fraser, Ralph M. Weischedel_

- :fontawesome-solid-user-group: **Participant:** [BBN](./xlingual/participants.md#bbn)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/BBNTREC2001.pdf](http://trec.nist.gov/pubs/trec10/papers/BBNTREC2001.pdf)
- :material-file-search: **Runs:** [BBN10XLA](./xlingual/runs.md#bbn10xla) | [BBN10XLB](./xlingual/runs.md#bbn10xlb) | [BBN10XLC](./xlingual/runs.md#bbn10xlc) | [BBN10XLD](./xlingual/runs.md#bbn10xld) | [BBN10MON](./xlingual/runs.md#bbn10mon)

??? abstract "Abstract"
	
	BBN only participated in the cross-lingual track in TREC 2001. Arabic, the language of the TREC 2001 corpus, presents a number of challenges to both monolingual and cross-lingual IR. First, many inflected Arabic words can correspond to multiple uninflected words, requiring context to disambiguate them. Second, orthographic variations are prevalent; certain glyphs are sometimes written as different, but similar looking glyphs. Third, broken plurals, analogous to irregular nouns in English, are very common. Such nouns cannot be easily reduced to their singular forms using a rule-based approach. Fourth, Arabic words are highly ambiguous due to the tri-literal root system and the omission of short vowels in written Arabic. The focus of this report is to explore the impact of these issues on Arabic monolingual and cross-lingual retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuFW01.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuFW01,
		author = {Jinxi Xu and Alexander M. Fraser and Ralph M. Weischedel},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC} 2001 Cross-lingual Retrieval at {BBN}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/BBNTREC2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuFW01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Hummingbird SearchServer at TREC 2001

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [hummingbird](./xlingual/participants.md#hummingbird)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/HumTREC2001.pdf](http://trec.nist.gov/pubs/trec10/papers/HumTREC2001.pdf)
- :material-file-search: **Runs:** [humAR01t](./xlingual/runs.md#humar01t) | [humAR01tdn](./xlingual/runs.md#humar01tdn) | [humAR01tdm](./xlingual/runs.md#humar01tdm) | [humAR01tdx](./xlingual/runs.md#humar01tdx) | [humAR01td](./xlingual/runs.md#humar01td)

??? abstract "Abstract"
	
	Hummingbird submitted ranked result sets for the topic relevance task of the TREC 2001 Web Track (10GB of web data) and for the monolingual Arabic task of the TREC 2001 Cross-Language Track (869MB of Arabic news data). SearchServer's Intuitive Searching tied or exceeded the median Precision@10 score in 46 of the 50 web queries. For the web queries, enabling SearchServer's document length normalization increased Precision@10 by 65% and average precision by 55%. SearchServer's option to square the importance of inverse document frequency (V2:4 vs. V2:3) increased Precision@10 by 8% and average precision by 12%. SearchServer’s stemming increased Precision@10 by 5% and average precision by 13%. For the Arabic queries, a combination of experimental Arabic morphological normalizations, Arabic stop words and pseudo-relevance feedback increased average precision by 53% and Precision@10 by 9%.
	

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

#### Keep It Simple Sheffield - A KISS Approach to the Arabic Track

_Mark Sanderson, Asaad Alberair_

- :fontawesome-solid-user-group: **Participant:** [sheffield](./xlingual/participants.md#sheffield)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/sheffield_arabic.pdf](http://trec.nist.gov/pubs/trec10/papers/sheffield_arabic.pdf)
- :material-file-search: **Runs:** [shefea](./xlingual/runs.md#shefea) | [shefeaa](./xlingual/runs.md#shefeaa) | [sheffea](./xlingual/runs.md#sheffea) | [sheffeaa](./xlingual/runs.md#sheffeaa) | [shefma](./xlingual/runs.md#shefma)

??? abstract "Abstract"
	
	Sheffield’s participation in the inaugural Arabic cross language track is described here. Our goal was to examine how well one could achieve retrieval of Arabic text with the minimum of resources and adaptation of existing retrieval systems. To this end the public translators used for query translation and the minimal changes to our retrieval system are described. While the effectiveness of our resulting system is not as high as one might desire, it nevertheless provides reasonable performance particularly in the monolingual track: on average, just under four relevant documents were found in the 10 top ranked documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SandersonA01.bib) "
	```
	@inproceedings{DBLP:conf/trec/SandersonA01,
		author = {Mark Sanderson and Asaad Alberair},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Keep It Simple Sheffield - {A} {KISS} Approach to the Arabic Track},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/sheffield\_arabic.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SandersonA01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2001: Experiments in Filtering and in Arabic,  Video, and Web Retrieval

_James Mayfield, Paul McNamee, Cash Costello, Christine D. Piatko, Amit Banerjee_

- :fontawesome-solid-user-group: **Participant:** [apl-jhu](./xlingual/participants.md#apl-jhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf](http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf)
- :material-file-search: **Runs:** [apl10ca1](./xlingual/runs.md#apl10ca1) | [apl10ce1](./xlingual/runs.md#apl10ce1) | [apl10ce2](./xlingual/runs.md#apl10ce2) | [apl10cf1](./xlingual/runs.md#apl10cf1) | [apl10ce3](./xlingual/runs.md#apl10ce3)

??? abstract "Abstract"
	
	The outsider might wonder whether, in its tenth year, the Text Retrieval Conference would be a moribund workshop encouraging little innovation and undertaking few new challenges, or whether fresh research problems would continue to be addressed. We feel strongly that it is the later that is true; our group at the Johns Hopkins University Applied Physics Laboratory (JHU/APL) participated in four tracks at this year’s conference, three of which presented us with new and interesting problems. For the first time we participated in the filtering track, and we submitted official results for both the batch and routing subtasks. This year, a first attempt was made to hold a content-based video retrieval track at TREC, and we developed a new suite of tools for image analysis and multimedia retrieval. Finally, though not a stranger to cross-language text retrieval, we made a first attempt at Arabic language retrieval while emphasizing a language-neutral approach that has worked well in other languages. Thus, our team found several challenges to face this year, and this paper mainly reports our initial findings. [...]
	

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

#### Arabic Information Retrieval at UMass in TREC-10

_Leah S. Larkey, Margaret E. Connell_

- :fontawesome-solid-user-group: **Participant:** [umass](./xlingual/participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/UMass_TREC10_Final.pdf](http://trec.nist.gov/pubs/trec10/papers/UMass_TREC10_Final.pdf)
- :material-file-search: **Runs:** [UMass1](./xlingual/runs.md#umass1) | [UMass2](./xlingual/runs.md#umass2) | [UMass3](./xlingual/runs.md#umass3) | [UMass4](./xlingual/runs.md#umass4)

??? abstract "Abstract"
	
	The University of Massachusetts took on the TREC10 cross-language track with no prior experience with Arabic, and no Arabic speakers among any of our researchers or students. We intended to implement some standard approaches, and to extend a language modeling approach to handle co-occurrences. Given the lack of resources – training data, electronic bilingual dictionaries, and stemmers, and our unfamiliarity with Arabic, we had our hands full carrying out some standard approaches to monolingual and cross-language Arabic retrieval, and did not submit any runs based on novel approaches. We submitted three monolingual runs and one cross-language run. We first describe the models, techniques, and resources we used, then we describe each run in detail. Our official runs performed moderately well, in the second tier (3rd or 4 th place). Since submitting these results, we have improved normalization and stemming, improved dictionary construction, expanded Arabic queries, improved estimation and smoothing in language models, and added combination of evidence, increasing performance by a substantial amount.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LarkeyC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/LarkeyC01,
		author = {Leah S. Larkey and Margaret E. Connell},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Arabic Information Retrieval at UMass in {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/UMass\_TREC10\_Final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LarkeyC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC2001 Question-Answer, Web and Cross Language Experiments using  PIRCS

_Kui-Lam Kwok, Laszlo Grunfeld, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./xlingual/participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf](http://trec.nist.gov/pubs/trec10/papers/queenst2001.pdf)
- :material-file-search: **Runs:** [pir1XEtd](./xlingual/runs.md#pir1xetd) | [pir1XEtdn](./xlingual/runs.md#pir1xetdn) | [pir1XAtdn](./xlingual/runs.md#pir1xatdn) | [pir1XAtd](./xlingual/runs.md#pir1xatd)

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

#### TREC-10 Experiments at University of Maryland CLIR and Video

_Kareem Darwish, David S. Doermann, Ryan C. Jones, Douglas W. Oard, Mika Rautiainen_

- :fontawesome-solid-user-group: **Participant:** [UMaryland](./xlingual/participants.md#umaryland)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/umdTREC2000.pdf](http://trec.nist.gov/pubs/trec10/papers/umdTREC2000.pdf)
- :material-file-search: **Runs:** [UMmanual](./xlingual/runs.md#ummanual) | [UMmonoAuto](./xlingual/runs.md#ummonoauto) | [UMclirAutoXP](./xlingual/runs.md#umclirautoxp) | [UMclirAutoFL](./xlingual/runs.md#umclirautofl) | [UMclirAutoTJ](./xlingual/runs.md#umclirautotj)

??? abstract "Abstract"
	
	The University of Maryland Researchers participated in both the Arabic-English Cross Language Information Retrieval (CLIR) and Video tracks of TREC-10. In the CLIR track, our goal was to explore effective monolingual Arabic IR techniques and effective query translation from English to Arabic for cross language IR. For the monolingual part, the use of the different index terms including words, stems, roots, and character n-grams were explored. For the English-Arabic CLIR, the use of MT, wordlist based translation, and non-dictionary words transliteration was explored. In the video track, we participated in the shot boundary detection, and known item search with the primary goals being to evaluate existing technology for shot detection and a new approach to extending simple visual image queries to video sequences. We present a general overview of the approaches, summarize the results in discuss how the algorithms are being extended.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DarwishDJOR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/DarwishDJOR01,
		author = {Kareem Darwish and David S. Doermann and Ryan C. Jones and Douglas W. Oard and Mika Rautiainen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-10} Experiments at University of Maryland {CLIR} and Video},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/umdTREC2000.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DarwishDJOR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Translation Term Weighting and Combining Translation Resources in  Cross-Language Retrieval

_Aitao Chen, Fredric C. Gey_

- :fontawesome-solid-user-group: **Participant:** [berkeley-clir](./xlingual/participants.md#berkeley-clir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/berkeley_trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/berkeley_trec10.pdf)
- :material-file-search: **Runs:** [BKYAAA1](./xlingual/runs.md#bkyaaa1) | [BKYEAA1](./xlingual/runs.md#bkyeaa1) | [BKYEAA2](./xlingual/runs.md#bkyeaa2) | [BKYEAA3](./xlingual/runs.md#bkyeaa3) | [BKYEAA4](./xlingual/runs.md#bkyeaa4)

??? abstract "Abstract"
	
	In TREC-10 the Berkeley group participated only in the English-Arabic cross-language retrieval (CLIR) track. One Arabic monolingual run and four English-Arabic cross-language runs were submitted. Our approach to the cross-language retrieval was to translate the English topics into Arabic using online English-Arabic bilingual dictionaries and machine translation software. The five official runs are named as BKYAAA1, BKYAA1, BYEA2, BKYAA3, and BKYEAA4. The BKYAAA1 is the Arabic monolingual run, and the rest are English-to-Arabic cross-language runs. The same logistic regression based document ranking algorithm without pseudo relevance feedback was applied in all five runs. We refer the readers to the paper in [1] for details.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenG01.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenG01,
		author = {Aitao Chen and Fredric C. Gey},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Translation Term Weighting and Combining Translation Resources in Cross-Language Retrieval},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/berkeley\_trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenG01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT at TREC-10

_Mohammed Aljlayl, Steven M. Beitzel, Eric C. Jensen, Abdur Chowdhury, David O. Holmes, M. Lee, David A. Grossman, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [IIT](./xlingual/participants.md#iit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/IIT-TREC10.pdf](http://trec.nist.gov/pubs/trec10/papers/IIT-TREC10.pdf)
- :material-file-search: **Runs:** [iit01mlr](./xlingual/runs.md#iit01mlr) | [iit01ml](./xlingual/runs.md#iit01ml) | [iit01md](./xlingual/runs.md#iit01md) | [iit01xma](./xlingual/runs.md#iit01xma) | [iit01xdi](./xlingual/runs.md#iit01xdi)

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

## Filtering 

#### The TREC 2001 Filtering Track Report

_Stephen E. Robertson, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/filtering_track.pdf](http://trec.nist.gov/pubs/trec10/papers/filtering_track.pdf)
??? abstract "Abstract"
	
	The TREC-10 filtering track measures the ability of systems to build persistent user profiles which successfully separate relevant and non-relevant documents. It consists of three major subtasks: adaptive filtering, batch filtering, and routing. In adaptive filtering, the system begins with only a topic statement and a small number of positive examples, and must learn a better profile from on-line feedback. Batch filtering and routing are more traditional machine learning tasks where the system begins with a large sample of evaluated training documents. This report describes the track, presents some evaluation results, and provides a general commentary on lessons learned from this year's track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonS01.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonS01,
		author = {Stephen E. Robertson and Ian Soboroff},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC} 2001 Filtering Track Report},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/filtering\_track.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonS01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Bias Problem and Language Models in Adaptive Filtering

_Yi Zhang, James P. Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu-lti](./filtering/participants.md#cmu-lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/trec10.CMUDIR.filter.pdf](http://trec.nist.gov/pubs/trec10/papers/trec10.CMUDIR.filter.pdf)
- :material-file-search: **Runs:** [CMUDIRURM](./filtering/runs.md#cmudirurm) | [CMUDIRFLM](./filtering/runs.md#cmudirflm) | [CMUDIRULM](./filtering/runs.md#cmudirulm) | [CMUDIRFRM](./filtering/runs.md#cmudirfrm)

??? abstract "Abstract"
	
	We used the YFILTER filtering system for experiments on updating profiles and setting thresholds. We developed a new method of using language models for updating profiles that is more focused on picking informative/discriminative words for query. The new method was compared with the well-known Rocchio algorithm. Dissemination thresholds were set based on maximum likelihood estimation that models and compensates for the sampling bias inherent in adaptive filtering. Our experimental results suggest that using what kind of distribution to model the scores of relevant and non- relevant documents is corpus dependant. The experimental results also show the sampling bias problem of training data while filtering makes the final profile learned biased.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangC01.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangC01,
		author = {Yi Zhang and James P. Callan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The Bias Problem and Language Models in Adaptive Filtering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/trec10.CMUDIR.filter.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangC01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC-10: Filtering, QA, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yikun Guo, Yingju Xia, Zhe Feng_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./filtering/participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf](http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf)
- :material-file-search: **Runs:** [FDUT10AF1](./filtering/runs.md#fdut10af1) | [FDUT10BF2](./filtering/runs.md#fdut10bf2) | [FDUT10BF1](./filtering/runs.md#fdut10bf1) | [FDUT10AF4](./filtering/runs.md#fdut10af4)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC conference for the second time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we participate in the sub-task of adaptive and batch filtering. Vector representation and computation are heavily applied in filtering procedure. Four runs have been submitted, which includes one T10SU and one T10F run for adpative filtering, as well as another one T10SU and one T10F run for batch filtering. We have tried many natural language processing techniques in our QA system, including statistical sentence breaking, POS tagging, parsing, name entity tagging, chunking and semantic verification. Various sources of world knowledge are also incorporated, such as WordNet and geographic information. For web retrieval, relevant document set is first created by an extended Boolean retrieval engine, and then reordered according to link information. Four runs with different combination of topic coverage and link information are submitted. On video track, We take part in both of the sub-tasks. In the task of shot boundary detection, we have submitted two runs with different parameters. In the task of video retrieval, we have submitted the results of 17 topics among all the topics.
	

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

#### TREC-10 Experiments at CAS-ICT: Filtering, Web and QA

_Bin Wang, Hongbo Xu, Zhifeng Yang, Yue Liu, Xueqi Cheng, Dongbo Bu, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [chinese_academy](./filtering/participants.md#chinese_academy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf](http://trec.nist.gov/pubs/trec10/papers/CASICT.pdf)
- :material-file-search: **Runs:** [ICTAdaFT10Ua](./filtering/runs.md#ictadaft10ua) | [ICTAdaFT10Fa](./filtering/runs.md#ictadaft10fa) | [ICTAdaFT10Ub](./filtering/runs.md#ictadaft10ub) | [ICTAdaFT10Uc](./filtering/runs.md#ictadaft10uc)

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

#### Tampere University of Technology at TREC 2001

_Ari Visa, Jarmo Toivonen, Tomi Vesanen, Jarno Mäkinen_

- :fontawesome-solid-user-group: **Participant:** [Tampere](./filtering/participants.md#tampere)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/Visa.pdf](http://trec.nist.gov/pubs/trec10/papers/Visa.pdf)
- :material-file-search: **Runs:** [VisaWordT10](./filtering/runs.md#visawordt10) | [VisaSent1T10](./filtering/runs.md#visasent1t10)

??? abstract "Abstract"
	
	In this paper we present the prototype based text matching methodology used in the Routing Sub-Task of TREC 2001 Filtering Track. The methodology examines texts on word and sentence levels. On the word level the methodology is based on word coding and transforming the codes into histograms by the means of Weibull distribution. On the sentence level the word coding is done in a similar manner as on the word level. But instead of making histograms we use a more simple method. After the word coding, we transform the sentence vectors to sentence feature vectors using Slant transform. The paper includes also description of the TREC runs and some discussion about the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VisaTVM01.bib) "
	```
	@inproceedings{DBLP:conf/trec/VisaTVM01,
		author = {Ari Visa and Jarmo Toivonen and Tomi Vesanen and Jarno M{\"{a}}kinen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Tampere University of Technology at {TREC} 2001},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/Visa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VisaTVM01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SERbrainware at TREC 2001

_Pal Rujan_

- :fontawesome-solid-user-group: **Participant:** [SER](./filtering/participants.md#ser)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/ser_final.pdf](http://trec.nist.gov/pubs/trec10/papers/ser_final.pdf)
- :material-file-search: **Runs:** [serASSAT10ad](./filtering/runs.md#serassat10ad) | [serASSAT10ba](./filtering/runs.md#serassat10ba) | [serASSAT10ro](./filtering/runs.md#serassat10ro) | [serCLST10af](./filtering/runs.md#serclst10af) | [serCLST10ba](./filtering/runs.md#serclst10ba) | [serCLST10ro](./filtering/runs.md#serclst10ro)

??? abstract "Abstract"
	
	SER Technology Deutschland GmbH is the technological arm of SER Systems Inc, Herndon, Virginia. Our company focuses on knowledge-enabled software products, mostly related to document management. At the core of many of our products is a knowledge management engine called SERbrainware, which is being developed by our group in Oldenburg since 1999. This engine contains, among others, a text classifier and an associative access module. Both were used in preparing our entries. This is our first TREC. In order to get acquainted with the usual procedures, evaluation criteria, etc., we decided to participate first in the filtering track. Due to the fact that we had a rather restricted amount of time - two weeks - at our disposition, we used the commercially available engine version 2.40 without any special add-ons.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Rujan01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Rujan01,
		author = {Pal Rujan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {SERbrainware at {TREC} 2001},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/ser\_final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Rujan01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC-10: Filtering and Web Tracks

_Stephen E. Robertson, Steve Walker, Hugo Zaragoza_

- :fontawesome-solid-user-group: **Participant:** [microsoft](./filtering/participants.md#microsoft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/msr_cambridge.pdf](http://trec.nist.gov/pubs/trec10/papers/msr_cambridge.pdf)
- :material-file-search: **Runs:** [ok10f2br](./filtering/runs.md#ok10f2br) | [ok10f2ur](./filtering/runs.md#ok10f2ur)

??? abstract "Abstract"
	
	This report is concerned with the Adaptive Filtering and Web tracks. There are separate reports in this volume [1, 2] on the Microsoft Research Redmond participation in QA track and the Microsoft Research Beijing participation in the Web track. Two runs were submitted for the Adaptive Filtering track, on the adaptive filtering task only (two optimisa-tion measures), and several runs for the Web track, both tasks (adhoc and home page finding). The filtering system is somewhat similar to the one used for TREC-9; the web system is a simple Okapi system without blind feedback, but the document indexing includes anchor text from incoming links.
	

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

#### Applying Support Vector Machines to the TREC-2001 Batch Filtering  and Routing Tasks

_David D. Lewis_

- :fontawesome-solid-user-group: **Participant:** [Lewis](./filtering/participants.md#lewis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/daviddlewis-trec2001-draft4.pdf](http://trec.nist.gov/pubs/trec10/papers/daviddlewis-trec2001-draft4.pdf)
- :material-file-search: **Runs:** [DLewis01bfFa](./filtering/runs.md#dlewis01bffa) | [DLewis01rFa](./filtering/runs.md#dlewis01rfa) | [DLewis01bfUa](./filtering/runs.md#dlewis01bfua) | [DLewis01rUa](./filtering/runs.md#dlewis01rua)

??? abstract "Abstract"
	
	My goal for TREC-2001 was simple: submit some runs (so that I could attend the conference), spend the minimum time necessary (since I’ve been busy this year with a large client project), and get respectable results (marketing!). The TREC batch filtering task was the obvious choice, since this year it was purely and simply a text categorization task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lewis01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lewis01,
		author = {David D. Lewis},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Applying Support Vector Machines to the {TREC-2001} Batch Filtering and Routing Tasks},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/daviddlewis-trec2001-draft4.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lewis01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Topic-Specific Optimization and Structuring

_David A. Evans, James G. Shanahan, Xiang Tong, Norbert Roma, Emilia Stoica, Victor Sheftel, Jesse Montgomery, Jeffrey Bennett, Gregory Grefenstette_

- :fontawesome-solid-user-group: **Participant:** [clairvoyance](./filtering/participants.md#clairvoyance)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/CLARIT_TREC-2001_Filtering_Final.pdf](http://trec.nist.gov/pubs/trec10/papers/CLARIT_TREC-2001_Filtering_Final.pdf)
- :material-file-search: **Runs:** [CL01afa](./filtering/runs.md#cl01afa) | [CL01afb](./filtering/runs.md#cl01afb) | [CL01afc](./filtering/runs.md#cl01afc) | [CL01afd](./filtering/runs.md#cl01afd) | [clT10rta](./filtering/runs.md#clt10rta) | [clT10rtb](./filtering/runs.md#clt10rtb) | [CLT10BFA](./filtering/runs.md#clt10bfa) | [CLT10BFB](./filtering/runs.md#clt10bfb)

??? abstract "Abstract"
	
	The Clairvoyance team participated in the Filtering Track, submitting the maximum number of runs in each of the filtering categories: Adaptive, Batch, and Routing. We had two distinct goals this year: (1) to establish the generalizability of our approach to adaptive filtering and (2) to experiment with relatively more 'radical' approaches to batch filtering using ensembles of filters. Our routing runs served principally to establish an internal basis for comparisons in performance to adaptive and batch efforts and are not discussed in this report.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EvansSTRSSMBG01.bib) "
	```
	@inproceedings{DBLP:conf/trec/EvansSTRSSMBG01,
		author = {David A. Evans and James G. Shanahan and Xiang Tong and Norbert Roma and Emilia Stoica and Victor Sheftel and Jesse Montgomery and Jeffrey Bennett and Gregory Grefenstette},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Topic-Specific Optimization and Structuring},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/CLARIT\_TREC-2001\_Filtering\_Final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EvansSTRSSMBG01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### kNN, Rocchio and Metrics for Information Filtering at TREC-10

_Tom Ault, Yiming Yang_

- :fontawesome-solid-user-group: **Participant:** [cmu-cat](./filtering/participants.md#cmu-cat)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/cmucat-correct.pdf](http://trec.nist.gov/pubs/trec10/papers/cmucat-correct.pdf)
- :material-file-search: **Runs:** [CMUCATsrf5](./filtering/runs.md#cmucatsrf5) | [CMUCATsr10](./filtering/runs.md#cmucatsr10) | [CMUCATmr10](./filtering/runs.md#cmucatmr10) | [CMUCATmrf5](./filtering/runs.md#cmucatmrf5) | [CMUCATa2f5](./filtering/runs.md#cmucata2f5) | [CMUCATa210](./filtering/runs.md#cmucata210)

??? abstract "Abstract"
	
	We compared a multi-class k-nearest neighbor (kNN) approach and a standard Rocchio method in the filtering tasks of TREC-10. Empirically, we found kNN more effective in batch filtering, and Rocchio better in adaptive filtering. For threshold adjustment based on relevance feedback, we developed a new strategy that updates a local regression over time based on a sliding window over positive examples and a sliding window over negative examples in the history. Applying this strategy to Rocchio and comparing its results to those by the same method with a fixed threshold, the recall was improved by 37-39% while the precision was improved by as much as 9%. Motivated by the extremely low performance of all systems on the T10S metric, we also analyzed this metric, and found that it favors more frequently occurring categories over rare ones and is somewhat inconsistent with its most straightforward interpretation. We propose a change to this metric which fixes these problems and brings it closer to the Cirk metric used to evaluate the TDT tracking task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AultY01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AultY01,
		author = {Tom Ault and Yiming Yang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {kNN, Rocchio and Metrics for Information Filtering at {TREC-10}},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/cmucat-correct.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AultY01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Unbiased S-D Threshold Optimization, Initial Query Degradation,  Decay, and Incrementality, for Adaptive Document Filtering

_Avi Arampatzis_

- :fontawesome-solid-user-group: **Participant:** [nijmegen](./filtering/participants.md#nijmegen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/KUN-TREC10.pdf](http://trec.nist.gov/pubs/trec10/papers/KUN-TREC10.pdf)
- :material-file-search: **Runs:** [KUNbU](./filtering/runs.md#kunbu) | [KUNbF](./filtering/runs.md#kunbf) | [KUNr1](./filtering/runs.md#kunr1) | [KUNr2](./filtering/runs.md#kunr2) | [KUNaU](./filtering/runs.md#kunau) | [KUNaF](./filtering/runs.md#kunaf)

??? abstract "Abstract"
	
	We develop further the S-D threshold optimization method. Specifically, we deal with the bias problem introduced by receiving relevance judgements only for documents retrieved. The new approach estimates the parameters of the exponential Gaussian score density model without using any relevance judgements. The standard expectation maximization (EM) method for resolving mixtures of distributions is used. In order to limit the number of documents that need to be buffered, we apply nonuni-form document sampling, emphasizing the right tail (high scores) of the total score distribution. For learning filtering profiles, we present a version of Rocchio's method which is suitable and efficient for adaptive filtering. Its main new features are the initial query degradation and decay, while it is fully incremental in query updates and in calculating document score statistics. Initial query degradation eliminates gradually the contribution of the initial query as the number of relevant training documents increases. Decay considers relevant instances (documents and/or initial query) of the near past more heavily than those of the early past. This is achieved by the use of half-life, i.e. the age that a training instance must be before it is half as influential as a fresh one in training/updating a profile. All these new enhancements are consistent with the initial motivation of Rocchio's formula. We, moreover, use a form of term selection for all tasks (which in adaptive tasks is applied repeatedly), and query zoning for batch filtering and routing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Arampatzis01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Arampatzis01,
		author = {Avi Arampatzis},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Unbiased {S-D} Threshold Optimization, Initial Query Degradation, Decay, and Incrementality, for Adaptive Document Filtering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/KUN-TREC10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Arampatzis01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Mercure and MercureFiltre Applied for Web and Filtering Tasks at TREC-10

_Mohand Boughanem, Claude Chrisment, Mohamed Tmar_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./filtering/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/irit.trec2001.pdf](http://trec.nist.gov/pubs/trec10/papers/irit.trec2001.pdf)
- :material-file-search: **Runs:** [mer10b](./filtering/runs.md#mer10b) | [mer10r1](./filtering/runs.md#mer10r1)

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

#### Oracle at TREC 10: Filtering and Question-Answering

_Shamin Alpha, Paul Dixon, Ciya Liao, Changwen Yang_

- :fontawesome-solid-user-group: **Participant:** [oracle](./filtering/participants.md#oracle)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/orcltrec10.pdf](http://trec.nist.gov/pubs/trec10/papers/orcltrec10.pdf)
- :material-file-search: **Runs:** [oraBU082701](./filtering/runs.md#orabu082701) | [oraRO082801](./filtering/runs.md#oraro082801) | [oraAU082201](./filtering/runs.md#oraau082201)

??? abstract "Abstract"
	
	Oracle’s objective in TREC-10 was to study the behavior of Oracle information retrieval in previously unexplored application areas. The software used was Oracle9i Text[1], Oracle’s full-text retrieval engine integrated with the Oracle relational database management system, and the Oracle PL/SQL procedural programming language. Runs were submitted in filtering and Q/A tracks. For the filtering track we submitted three runs, in adaptive filtering, batch filtering and routing. By comparing the TREC results, we found that the concepts (themes) extracted by Oracle Text can be used to aggregate document information content to simplify statistical processing. Oracle's Q/A system integrated information retrieval (IR) and information extraction (IE). The Q/A system relied on a combination of document and sentence ranking in IR, named entity tagging in IE and shallow parsing based classification of questions into pre-defined categories.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlphaDLY01.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlphaDLY01,
		author = {Shamin Alpha and Paul Dixon and Ciya Liao and Changwen Yang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Oracle at {TREC} 10: Filtering and Question-Answering},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/orcltrec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlphaDLY01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Video 

#### The TREC-2001 Video Track Report

_Alan F. Smeaton, Paul Over, R. Taban_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/TREC10Video_Proc_Report.pdf](http://trec.nist.gov/pubs/trec10/papers/TREC10Video_Proc_Report.pdf)
??? abstract "Abstract"
	
	New in TREC-2001 was the Video Track, the goal of which was to promote progress in content-based retrieval from digital video via open, metrics-based evaluation. The track built on publicly available video provided by the Open Video Project of the University of North Carolina at Chapel Hill under Gary Marchionini (Marchionini, 2001), the NIST Digital Video Library (Over, 2001), and stock shot video provided for TREC-2001 by the British Broadcasting Corporation (Richard Wright et al). The track used very nice work on shot boundary evaluation done as part of the ISIS Coordinated Research Project (AIM, 2001). This paper is an introduction to the track framework — the tasks, data, and measures. For information about results, see the tables associated with the conference proceedings. TREC research has remained true to its late twentieth century origins, concentrating on retrieval of text documents with only occasional excursions into other media: spoken documents and images of doc-uments. Using TREC as an incubator, the Video Track has pushed into true multimedia territory with respect to formulation of search requests, analysis of multimedia material to be searched (video, audio, transcripts, text in video, music, natural sound, etc), combination of search strategies, and in some cases presentation of results to a human searcher The TREC video track had 12 participating groups, 5 from US, 2 from Asia and 5 from Europe. 11 hours of MPEG-1 data was collected and distributed as well as 74 topics or queries. What made these queries particularly interesting and challenging was that they were true multimedia queries as they all had video clips, images, or audio clips as part of the query, in addition to a text description. Participating groups used a variety of techniques to match these multimedia queries against the video dataset, some running fully automated techniques and others involving users in interactive search experiments. As might be expected for the first running of such a track, the framework was a bit unorthodox by the standards of mature TREC tracks. Participating groups contributed significant amounts of work toward the creation of the track infrastructure. Search systems were called upon to handle a very wide variety of topic types. We hoped exploring more of the possible territory, though it decreased the likelihood of definitive outcomes in any one area this year, would still generate some interesting results and more importantly provide a good foundation for a more focused track in TREC-2002. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmeatonOT01.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmeatonOT01,
		author = {Alan F. Smeaton and Paul Over and R. Taban},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC-2001} Video Track Report},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/TREC10Video\_Proc\_Report.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmeatonOT01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Lazy Users and Automatic Video Retrieval Tools in (the) Lowlands

_Jan Baan, Alex van Ballegooij, Jan Mark Geusenbroek, Jurgen den Hartog, Djoerd Hiemstra, Johan List, Thijs Westerveld, Ioannis Patras, Stephan Raaijmakers, Cees Snoek, Leon Todoran, Jeroen Vendrig, Arjen P. de Vries, Marcel Worring_

- :fontawesome-solid-user-group: **Participant:** [lowlands](./video/participants.md#lowlands)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/lowlands01.pdf](http://trec.nist.gov/pubs/trec10/papers/lowlands01.pdf)
- :material-file-search: **Runs:** [MediaMill1](./video/runs.md#mediamill1) | [MediaMill2](./video/runs.md#mediamill2) | [Lowlands_1](./video/runs.md#lowlands_1) | [Lowlands_2](./video/runs.md#lowlands_2) | [Lowlands_3](./video/runs.md#lowlands_3) | [Lowlands_4](./video/runs.md#lowlands_4) | [Lowlands_5](./video/runs.md#lowlands_5)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC Video Retrieval evaluation. Our approach uses two complementary automatic approaches (the first based on visual content, the other on transcripts), to be refined in an interactive setting. The experiments focused on revealing relationships between (1) different modalities, (2) the amount of human processing, and (3) the quality of the results. We submitted five runs, summarized in Table 1. Run 1 is based on the query text and the visual content of the video. The query text is analyzed to choose the best detectors, e.g. for faces, names, specific camera techniques, dialogs, or natural scenes. Query by example based on detector specific features (e.g. number of faces, invariant color histograms) yields the final ranking result. To assess the additional value of speech content, we experimented with a transcript generated using speech recognition (made available by CMU). We queried the transcribed collection with the topic text combined with the transcripts of video examples. Despite of the error-prone recognition process, the transcripts often provide useful information about the video scenes. Run 2 combines the ranked output of the speech transcripts with (visual-only) run 1 in an attempt to improve its results; run 3 is the obligatory transcript-only run. Run 4 models a user working with the output of an automatic visual run, choosing the best answer-set from a number of options, or attempting to improve its quality by helping the system; for example, finding moon-landers by entering knowledge that the sky on the moon is black or locating the Starwars scene by pointing out that the robot has golden skin. Finally, run 5 combines all information available in our system: from detectors, to speech transcript, to the human-in-the-loop. Depending on the evaluation measures used, this leads to slightly better or slightly worse results than using these methods in isolation, caused by laziness expressed in the model for selecting the combination strategy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/X01.bib) "
	```
	@inproceedings{DBLP:conf/trec/X01,
		author = {Jan Baan and Alex van Ballegooij and Jan Mark Geusenbroek and Jurgen den Hartog and Djoerd Hiemstra and Johan List and Thijs Westerveld and Ioannis Patras and Stephan Raaijmakers and Cees Snoek and Leon Todoran and Jeroen Vendrig and Arjen P. de Vries and Marcel Worring},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Lazy Users and Automatic Video Retrieval Tools in (the) Lowlands},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/lowlands01.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/X01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC-10: Filtering, QA, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yikun Guo, Yingju Xia, Zhe Feng_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./video/participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf](http://trec.nist.gov/pubs/trec10/papers/FDUT10NoteBook.pdf)
- :material-file-search: **Runs:** [FundanSys1](./video/runs.md#fundansys1) | [FundanSys2](./video/runs.md#fundansys2) | [FDUSys1](./video/runs.md#fdusys1)

??? abstract "Abstract"
	
	This year Fudan University takes part in the TREC conference for the second time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we participate in the sub-task of adaptive and batch filtering. Vector representation and computation are heavily applied in filtering procedure. Four runs have been submitted, which includes one T10SU and one T10F run for adpative filtering, as well as another one T10SU and one T10F run for batch filtering. We have tried many natural language processing techniques in our QA system, including statistical sentence breaking, POS tagging, parsing, name entity tagging, chunking and semantic verification. Various sources of world knowledge are also incorporated, such as WordNet and geographic information. For web retrieval, relevant document set is first created by an extended Boolean retrieval engine, and then reordered according to link information. Four runs with different combination of topic coverage and link information are submitted. On video track, We take part in both of the sub-tasks. In the task of shot boundary detection, we have submitted two runs with different parameters. In the task of video retrieval, we have submitted the results of 17 topics among all the topics.
	

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

#### Integrating Features, Models, and Semantics for TREC Video Retrieval

_John R. Smith, Savitha Srinivasan, Arnon Amir, Sankar Basu, Giridharan Iyengar, Ching-Yung Lin, Milind R. Naphade, Dulce B. Ponceleon, Belle L. Tseng_

- :fontawesome-solid-user-group: **Participant:** [ibm-video](./video/participants.md#ibm-video)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/IBM-TREC-VIDEO-2001.pdf](http://trec.nist.gov/pubs/trec10/papers/IBM-TREC-VIDEO-2001.pdf)
- :material-file-search: **Runs:** [IBM_Alm1](./video/runs.md#ibm_alm1) | [IBM_Alm2](./video/runs.md#ibm_alm2) | [IBM_I_ASR](./video/runs.md#ibm_i_asr) | [IBM_A_ASR](./video/runs.md#ibm_a_asr) | [IBM_I_C+S](./video/runs.md#ibm_i_c+s) | [IBM_A_C+S](./video/runs.md#ibm_a_c+s) | [IBM_I_CBR](./video/runs.md#ibm_i_cbr) | [IBM_A_CBR](./video/runs.md#ibm_a_cbr)

??? abstract "Abstract"
	
	In this paper, we describe a system for automatic and interactive content-based retrieval of video that integrates features, models, and semantics. The novelty of the approach lies in the (1) semi-automatic construction of models of scenes, events, and objects from feature descriptors, and (2) integration of content-based and model-based querying in the search process. We describe several approaches for integration including iterative filtering, score aggregation, and relevance feedback searching. We describe our effort of applying the content-based retrieval system to the TREC video retrieval benchmark.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmithSABILNPT01.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmithSABILNPT01,
		author = {John R. Smith and Savitha Srinivasan and Arnon Amir and Sankar Basu and Giridharan Iyengar and Ching{-}Yung Lin and Milind R. Naphade and Dulce B. Ponceleon and Belle L. Tseng},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Integrating Features, Models, and Semantics for {TREC} Video Retrieval},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/IBM-TREC-VIDEO-2001.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmithSABILNPT01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNT TRECvid: A Brighton Image Searcher Application

_Mark E. Rorvig, Ki-Tau Jeong, Anup Pachlag, Ramprasad Anusuri, Diane Jenkins, Sara Oyarce_

- :fontawesome-solid-user-group: **Participant:** [north_texas](./video/participants.md#north_texas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/UNT_final.pdf](http://trec.nist.gov/pubs/trec10/papers/UNT_final.pdf)
- :material-file-search: **Runs:** [UNT1](./video/runs.md#unt1)

??? abstract "Abstract"
	
	The results, architecture and processing steps used by the University of North Texas team in the 2001 TRECvid video retrieval trials are described. Only a limited number of questions were selected by the team due to resource limitations described in the paper. However, the average precision of the team results over thirteen questions from the General search category were reasonable at 0.59.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RorvigJPAJO01.bib) "
	```
	@inproceedings{DBLP:conf/trec/RorvigJPAJO01,
		author = {Mark E. Rorvig and Ki{-}Tau Jeong and Anup Pachlag and Ramprasad Anusuri and Diane Jenkins and Sara Oyarce},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{UNT} TRECvid: {A} Brighton Image Searcher Application},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/UNT\_final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RorvigJPAJO01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-10 Shot Boundary Detection Task: CLIPS System Description  and Evaluation

_Georges Quénot_

- :fontawesome-solid-user-group: **Participant:** [clips-imag](./video/participants.md#clips-imag)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/clips-imag-bin.pdf](http://trec.nist.gov/pubs/trec10/papers/clips-imag-bin.pdf)
- :material-file-search: **Runs:** [CLIPS-1](./video/runs.md#clips-1) | [CLIPS-2](./video/runs.md#clips-2)

??? abstract "Abstract"
	
	This paper presents the system used by CLIPS-IMAG to perform the Shot Boundary Detection (SBD) task of the Video track of the TREC-10 conference. Cut detection is performed by computing image difference after motion compensation. Dissolve detection is performed by the comparison of the norm over the whole image of the first and second temporal derivatives. An output filter is added in order to clean the data of both detector and to merge them into a consistent output. This system also has a special module for detecting photographic ashes and filtering them as erroneous 'cuts'. Results obtained for the TREC-10 evaluation are presented. The system app ear to p erform in a very go o d way for cut transitions and within the average for gradual transitions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Quenot01.bib) "
	```
	@inproceedings{DBLP:conf/trec/Quenot01,
		author = {Georges Qu{\'{e}}not},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-10} Shot Boundary Detection Task: {CLIPS} System Description and Evaluation},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/clips-imag-bin.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Quenot01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multi-timescale Video Shot-Change Detection

_Marcus Jerome Pickering, Stefan M. Rüger_

- :fontawesome-solid-user-group: **Participant:** [imperial](./video/participants.md#imperial)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/video-pickering-rueger.pdf](http://trec.nist.gov/pubs/trec10/papers/video-pickering-rueger.pdf)
- :material-file-search: **Runs:** [ICKM1](./video/runs.md#ickm1)

??? abstract "Abstract"
	
	We describe our shot-boundary detection experiments for the TREC-10 video track, using a multi-timescale shot-change detection algorithm.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PickeringR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/PickeringR01,
		author = {Marcus Jerome Pickering and Stefan M. R{\"{u}}ger},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Multi-timescale Video Shot-Change Detection},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/video-pickering-rueger.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PickeringR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2001: Experiments in Filtering and in Arabic,  Video, and Web Retrieval

_James Mayfield, Paul McNamee, Cash Costello, Christine D. Piatko, Amit Banerjee_

- :fontawesome-solid-user-group: **Participant:** [apl-jhu](./video/participants.md#apl-jhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf](http://trec.nist.gov/pubs/trec10/papers/jhuapl01.pdf)
- :material-file-search: **Runs:** [JHUAPL](./video/runs.md#jhuapl) | [JHUAPLg](./video/runs.md#jhuaplg)

??? abstract "Abstract"
	
	The outsider might wonder whether, in its tenth year, the Text Retrieval Conference would be a moribund workshop encouraging little innovation and undertaking few new challenges, or whether fresh research problems would continue to be addressed. We feel strongly that it is the later that is true; our group at the Johns Hopkins University Applied Physics Laboratory (JHU/APL) participated in four tracks at this year’s conference, three of which presented us with new and interesting problems. For the first time we participated in the filtering track, and we submitted official results for both the batch and routing subtasks. This year, a first attempt was made to hold a content-based video retrieval track at TREC, and we developed a new suite of tools for image analysis and multimedia retrieval. Finally, though not a stranger to cross-language text retrieval, we made a first attempt at Arabic language retrieval while emphasizing a language-neutral approach that has worked well in other languages. Thus, our team found several challenges to face this year, and this paper mainly reports our initial findings. [...]
	

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

#### MSR-Asia at TREC-10 Video Track: Shot Boundary Detection Task

_Yufei Ma, Jia Sheng, Yuan Chen, HongJiang Zhang_

- :fontawesome-solid-user-group: **Participant:** [microsoft-china](./video/participants.md#microsoft-china)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/MSR_SBD.pdf](http://trec.nist.gov/pubs/trec10/papers/MSR_SBD.pdf)
- :material-file-search: **Runs:** [MSSD](./video/runs.md#mssd)

??? abstract "Abstract"
	
	The video track is added into TREC-10, composed of two tasks, automatic shot boundary detection and video retrieval. In this year, we (MSR-Asia) participated in the video track, focusing on shot boundary detection task. Our work is to find out all of boundaries the shot changes by a fast algorithm based on uncompressed domain. In our algorithm, all of non-cut transitions are considered as gradual transition, including dissolve, fade-in, fade-out, and all kinds of wipes. Experimental results indicate that the accuracy and processing speed of our algorithm are all very satisfactory.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaSCZ01.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaSCZ01,
		author = {Yufei Ma and Jia Sheng and Yuan Chen and HongJiang Zhang},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {MSR-Asia at {TREC-10} Video Track: Shot Boundary Detection Task},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/MSR\_SBD.pdf},
		timestamp = {Tue, 16 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MaSCZ01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Video Retrieval with the Informedia Digital Video Library System

_Alexander G. Hauptmann, Rong Jin, Norman Papernick, Tobun Dorbin Ng, Yanjun Qi, Ricky Houghton, Sue Thornton_

- :fontawesome-solid-user-group: **Participant:** [cmu-Hauptmann](./video/participants.md#cmu-hauptmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/CMU-VideoTrack.pdf](http://trec.nist.gov/pubs/trec10/papers/CMU-VideoTrack.pdf)
- :material-file-search: **Runs:** [CMU1](./video/runs.md#cmu1) | [CMU2](./video/runs.md#cmu2) | [CMU3](./video/runs.md#cmu3) | [CMU4](./video/runs.md#cmu4)

??? abstract "Abstract"
	
	The Informedia Digital Video Library [1] was the only NSF DLI project focusing specifically on information extraction from video and audio content. Over a terabyte of online data was collected, with automatically generated metadata and indices for retrieving videos from this library. The architecture for the project was based on the premise that real-time constraints on library and associated metadata creation could be relaxed in order to realize increased automation and deeper parsing and indexing for identifying the library contents and breaking it into segments. Library creation was an offline activity, with library exploration by users occurring online and making use of the generated metadata and segmentation. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HauptmannJPNQHT01.bib) "
	```
	@inproceedings{DBLP:conf/trec/HauptmannJPNQHT01,
		author = {Alexander G. Hauptmann and Rong Jin and Norman Papernick and Tobun Dorbin Ng and Yanjun Qi and Ricky Houghton and Sue Thornton},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Video Retrieval with the Informedia Digital Video Library System},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/CMU-VideoTrack.pdf},
		timestamp = {Thu, 16 Dec 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HauptmannJPNQHT01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC-10 Experiments at University of Maryland CLIR and Video

_Kareem Darwish, David S. Doermann, Ryan C. Jones, Douglas W. Oard, Mika Rautiainen_

- :fontawesome-solid-user-group: **Participant:** [umd-allen](./video/participants.md#umd-allen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/umdTREC2000.pdf](http://trec.nist.gov/pubs/trec10/papers/umdTREC2000.pdf)
- :material-file-search: **Runs:** [UMDLAMP](./video/runs.md#umdlamp) | [CMRS_UMD](./video/runs.md#cmrs_umd) | [CMRS_UMD2](./video/runs.md#cmrs_umd2)

??? abstract "Abstract"
	
	The University of Maryland Researchers participated in both the Arabic-English Cross Language Information Retrieval (CLIR) and Video tracks of TREC-10. In the CLIR track, our goal was to explore effective monolingual Arabic IR techniques and effective query translation from English to Arabic for cross language IR. For the monolingual part, the use of the different index terms including words, stems, roots, and character n-grams were explored. For the English-Arabic CLIR, the use of MT, wordlist based translation, and non-dictionary words transliteration was explored. In the video track, we participated in the shot boundary detection, and known item search with the primary goals being to evaluate existing technology for shot detection and a new approach to extending simple visual image queries to video sequences. We present a general overview of the approaches, summarize the results in discuss how the algorithms are being extended.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DarwishDJOR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/DarwishDJOR01,
		author = {Kareem Darwish and David S. Doermann and Ryan C. Jones and Douglas W. Oard and Mika Rautiainen},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {{TREC-10} Experiments at University of Maryland {CLIR} and Video},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/umdTREC2000.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DarwishDJOR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Dublin City University Video Track Experiments for TREC 2001

_Paul Browne, Cathal Gurrin, Hyowon Lee, Kieran McDonald, Sorin Sav, Alan F. Smeaton, Jiamin Ye_

- :fontawesome-solid-user-group: **Participant:** [DCUKI2001](./video/participants.md#dcuki2001)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/dcu_trec01_final.pdf](http://trec.nist.gov/pubs/trec10/papers/dcu_trec01_final.pdf)

??? abstract "Abstract"
	
	Dublin City University participated in the interactive search task and Shot Boundary Detection task* of the TREC Video Track. In the interactive search task experiment thirty people used three different digital video browsers to find video segments matching the given topics. Each user was under a time constraint of six minutes for each topic assigned to them. The purpose of this experiment was to compare video browsers and so a method was developed for combining independent users’ results for a topic into one set of results. Collated results based on thirty users are available herein though individual users’ and browsers’ results are currently unavailable for comparison. Our purpose in participating in this TREC track was to create the ground truth within the TREC framework, which will allow us to do direct browser performance comparisons.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrowneGLMSSY01.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrowneGLMSSY01,
		author = {Paul Browne and Cathal Gurrin and Hyowon Lee and Kieran McDonald and Sorin Sav and Alan F. Smeaton and Jiamin Ye},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Dublin City University Video Track Experiments for {TREC} 2001},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/dcu\_trec01\_final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BrowneGLMSSY01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Interactive 

#### The TREC 2001 Interactive Track Report

_William R. Hersh, Paul Over_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/t10ireport.pdf](http://trec.nist.gov/pubs/trec10/papers/t10ireport.pdf)
??? abstract "Abstract"
	
	In the TREC 2001 Interactive Track six research teams carried out observational studies which increased the realism of the searching by allowing the use of data and search systems/tools publicly accessible via the Internet. To the extent possible, searchers were allowed to choose tasks and systems/tools for accomplishing those tasks. At the same time, the studies for TREC 2001 were designed to maximize the likelihood that groups would find in their observations the germ of a hypothesis they could test for TREC 2002. This suggested that there be restrictions - some across all sites, some only within a given site - to make it more likely that patterns would emerge. The restrictions were formalized in two sorts of guidelines: one set for all sites and another set that applied only within a site.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershO01.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershO01,
		author = {William R. Hersh and Paul Over},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {The {TREC} 2001 Interactive Track Report},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/t10ireport.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershO01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Observations of Searchers: OHSU TREC 2001 Interactive Track

_William R. Hersh, Lynetta Sacherek, Daniel Olson_

- :fontawesome-solid-user-group: **Participant:** [OHSU](./interactive/participants.md#ohsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/Hersh.pdf](http://trec.nist.gov/pubs/trec10/papers/Hersh.pdf)
- :material-file-search: **Runs:** [ohsuI](./interactive/runs.md#ohsui)

??? abstract "Abstract"
	
	The goal of the TREC 2001 Interactive Track was to carry out observational experiments of Web-based searching to develop hypotheses for experiments in subsequent years. Each participating group was asked to undertake exploratory experiments based on a general protocol. For the OHSU Interactive Track experiments this year, we chose to perform a pure observational study of watching searchers carry out tasks on the Web. We found users were able to complete almost all the tasks within the time limits of the protocol. Future experimental studies aiming to discern differences among systems may need to provide more challenging tasks to detect such differences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershSO01.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershSO01,
		author = {William R. Hersh and Lynetta Sacherek and Daniel Olson},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Observations of Searchers: {OHSU} {TREC} 2001 Interactive Track},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/Hersh.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershSO01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC10 Web and Interactive Tracks at CSIRO

_Nick Craswell, David Hawking, Ross Wilkinson, Mingfang Wu_

- :fontawesome-solid-user-group: **Participant:** [CSIRO](./interactive/participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/csiro-trec-2001.pdf](http://trec.nist.gov/pubs/trec10/papers/csiro-trec-2001.pdf)
- :material-file-search: **Runs:** [csiroI](./interactive/runs.md#csiroi)

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

#### Selecting Versus Describing: A Preliminary Analysis of the Efficacy  of Categories in Exploring the Web

_Elaine G. Toms, Richard W. Kopak, Joan C. Bartlett, Luanne Freund_

- :fontawesome-solid-user-group: **Participant:** [toronto](./interactive/participants.md#toronto)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/toms-trec10.pdf](http://trec.nist.gov/pubs/trec10/papers/toms-trec10.pdf)
- :material-file-search: **Runs:** [torontoI](./interactive/runs.md#torontoi)

??? abstract "Abstract"
	
	This paper reports the findings of an exploratory study carried out as part of the Interactive Track at the 10th annual Text Retrieval Conference (TREC). Forty-eight, non-expert participants each completed four Web search tasks from among four specified topic areas: shopping, medicine, travel, and research. Participants were given a choice of initiating the search with a query or with a selection of a category from a pre-defined list. Participants were also asked to phrase a selected number of their search queries in the form of a complete statement or question. Results showed that there was little effect of the task domain on the search outcome. Exceptions to this were the problematic nature of the Shopping tasks, and the preference for query over category when the search task was general, i.e. when the semantics of the task did not map directly onto one of the available categories. Participants also evidenced a reluctance/inability to phrase search queries in the form of a complete statement or question. When keywords were used, they were short, averaging around two terms per query statement.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TomsKBF01.bib) "
	```
	@inproceedings{DBLP:conf/trec/TomsKBF01,
		author = {Elaine G. Toms and Richard W. Kopak and Joan C. Bartlett and Luanne Freund},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Selecting Versus Describing: {A} Preliminary Analysis of the Efficacy of Categories in Exploring the Web},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/toms-trec10.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TomsKBF01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Comparing Explicit and Implicit Feedback Techniques for Web Retrieval:  TREC-10 Interactive Track Report

_Ryen White, Joemon M. Jose, Ian Ruthven_

- :fontawesome-solid-user-group: **Participant:** [glasgow](./interactive/participants.md#glasgow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/glasgow.pdf](http://trec.nist.gov/pubs/trec10/papers/glasgow.pdf)
- :material-file-search: **Runs:** [glasgowI](./interactive/runs.md#glasgowi)

??? abstract "Abstract"
	
	In this paper we examine the extent to which implicit feedback (where the system attempts to estimate what the user may be interested in) can act as a substitute for explicit feedback (where searchers explicitly mark documents relevant). Therefore, we attempt to side-step the problem of getting users to explicitly mark documents relevant by making predictions on relevance through analysing the user’s interaction with the system. Specifically, we hypothesised that implicit and explicit feedback were interchangeable as sources of relevance information for relevance feedback. Through developing a system that utilised each type of feedback we were able to compare the two approaches in terms of search effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WhiteJR01.bib) "
	```
	@inproceedings{DBLP:conf/trec/WhiteJR01,
		author = {Ryen White and Joemon M. Jose and Ian Ruthven},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Comparing Explicit and Implicit Feedback Techniques for Web Retrieval: {TREC-10} Interactive Track Report},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/glasgow.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WhiteJR01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers' TREC 2001 Interactive Track Experience

_Nicholas J. Belkin, Colleen Cool, J. Jeng, Amymarie Keller, Diane Kelly, Ja-Young Kim, Hyuk-Jin Lee, Muh-Chyun (Morris) Tang, Xiaojun Yuan_

- :fontawesome-solid-user-group: **Participant:** [rutgers-belkin](./interactive/participants.md#rutgers-belkin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec10/papers/rutgers-interactive-paper.pdf](http://trec.nist.gov/pubs/trec10/papers/rutgers-interactive-paper.pdf)
- :material-file-search: **Runs:** [rutgersI](./interactive/runs.md#rutgersi)

??? abstract "Abstract"
	
	Our focus this year was to investigate methods for increasing query length in interactive information searching in the Web context, and to see if these methods led to changes in task performance and/or interaction. Thirty-four subjects each searched on four of the Interactive Track topics, in one of two conditions: a “box” query input mode; and a “line” query input mode. One-half of the subjects were instructed to enter their queries as complete sentences or questions; the other half as lists of words or phrases. Results are that: queries entered as questions or statements were significantly longer than those entered as words or phrases (twice as long); that there was no difference in query length between the box and line modes (except for medical topics, where keyword mode led to significantly more unique terms per search); and, that longer queries led to better performance. Other results of note are that satisfaction with the search was negatively correlated with length of time searching and other measures of interaction effort, and that the “buying” topics were significantly more difficult than the other three types.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelkinCJKKKLTY01.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelkinCJKKKLTY01,
		author = {Nicholas J. Belkin and Colleen Cool and J. Jeng and Amymarie Keller and Diane Kelly and Ja{-}Young Kim and Hyuk{-}Jin Lee and Muh{-}Chyun (Morris) Tang and Xiaojun Yuan},
		editor = {Ellen M. Voorhees and Donna K. Harman},
		title = {Rutgers' {TREC} 2001 Interactive Track Experience},
		booktitle = {Proceedings of The Tenth Text REtrieval Conference, {TREC} 2001, Gaithersburg, Maryland, USA, November 13-16, 2001},
		series = {{NIST} Special Publication},
		volume = {500-250},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2001},
		url = {http://trec.nist.gov/pubs/trec10/papers/rutgers-interactive-paper.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BelkinCJKKKLTY01.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

