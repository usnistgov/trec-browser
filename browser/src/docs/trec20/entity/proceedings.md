# Proceedings - Entity 2011 

#### Overview of the TREC 2011 Entity Track

_Krisztian Balog, Pavel Serdyukov, Arjen P. de Vries_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ENTITY.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec20/papers/ENTITY.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Entity track aimed to build test collections to evaluate entity-oriented search on Web data. In 2011, the track worked with two corpora: the ClueWeb 2009 web corpus and the new Sindice-2011 dataset [2]. Motivated by observations from the 2010 Entity track, we made the following changes in the track setup for 2011. In the REF task, we focused on modifications to simplify the evaluation and to improve cross-system comparison: (1) only primary homepages are accepted, i.e., relevance is binary; (2) for each answer, a (single) supporting document is required; (3) target type is not limited anymore; (4) groups that generate results using Web Search Engines are required to submit an obligatory run, using the Lemur ClueWeb Online Query Service. The main change regarding the LOD task is the use of the Sindice-2011 corpus, an improved and larger Semantic Web crawl, replacing the BTC-2009 collection used in 2010: (1) the target corpus is a larger and more representative LOD crawl; (2) examples are not mapped manually to LOD, but given as ClueWeb document identifiers. Finally, we introduced a new pilot task, REF-LOD, to explore the differences between ranking web data and ranking semantic web data, possibly enabling deeper investigations into connecting Semantic Web data with the 'real' web. We basically repeated the REF task, but requested results identified by their LOD URIs instead of their homepages. One of the goals of this task was to gain more insights in entity representation, and specifically investigate how often entities that are not represented on the web with their own homepage are represented as entities in LOD. In the remainder of the paper we first detail the setup of each task. We present the results collected in this year's track participation, and summarize the approaches applied. The paper concludes with a brief discussion of the problems faced by the track, and the way forward.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalogSV11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalogSV11,
		author = {Krisztian Balog and Pavel Serdyukov and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2011 Entity Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ENTITY.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalogSV11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LIA-iSmart at the TREC 2011 Entity Track: Entity List Completion  Using Contextual Unsupervised Scores for Candidate Entities Ranking

_Ludovic Bonnefoy, Patrice Bellot_

- :fontawesome-solid-user-group: **Participant:** [LIA](./participants.md#lia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/LIA.entity.update.pdf](http://trec.nist.gov/pubs/trec20/papers/LIA.entity.update.pdf)
- :material-file-search: **Runs:** [LIAcwb](./runs.md#liacwb) | [LIAwb](./runs.md#liawb) | [LIAwc](./runs.md#liawc) | [LIAwd](./runs.md#liawd)

??? abstract "Abstract"
	
	This paper describes our participation in the Entity List Completion (ELC) task at Entity track 2011. Our approach combined the work done for the Related Entity Finding 2010 task with some new criteria as the proximity or the similarity between a candidate answer with the correct answers given as examples or their cooccurrences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BonnefoyB11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BonnefoyB11,
		author = {Ludovic Bonnefoy and Patrice Bellot},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {LIA-iSmart at the {TREC} 2011 Entity Track: Entity List Completion Using Contextual Unsupervised Scores for Candidate Entities Ranking},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/LIA.entity.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BonnefoyB11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Team COMMIT at TREC 2011

_Marc Bron, Edgar Meij, Maria-Hendrike Peetz, Manos Tsagkias, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [COMMIT](./participants.md#commit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/COMMIT.entity.update.pdf](http://trec.nist.gov/pubs/trec20/papers/COMMIT.entity.update.pdf)
- :material-file-search: **Runs:** [ilpslinkOL](./runs.md#ilpslinkol) | [ilpsTextFilt](./runs.md#ilpstextfilt) | [ilpslinkcand](./runs.md#ilpslinkcand) | [ilpsPMIcMNZ](./runs.md#ilpspmicmnz)

??? abstract "Abstract"
	
	We describe the participation of Team COMMIT in this year's Microblog and Entity track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BronMPTR11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BronMPTR11,
		author = {Marc Bron and Edgar Meij and Maria{-}Hendrike Peetz and Manos Tsagkias and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Team {COMMIT} at {TREC} 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/COMMIT.entity.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BronMPTR11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Entity ELC TREC 2011

_Bingyang Liu, Fan Yang, Lei Cao, Xueqi Cheng, Yue Liu, Hongbo Xu_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ICTNET.entity.pdf](http://trec.nist.gov/pubs/trec20/papers/ICTNET.entity.pdf)
- :material-file-search: **Runs:** [ICTNET11ENR1](./runs.md#ictnet11enr1) | [ICTNET11ENR2](./runs.md#ictnet11enr2)

??? abstract "Abstract"
	
	The overall aim of the Entity track is to evaluate entity-related searches on Web data. Entity List Completion (ELC) addresses essentially the same task as Related Entity Finding (REF) does: finding entities that are engaged in a specific relation with an input entity. There are two main differences to REF: Entities are not represented by their homepages, but by a unique URI (from a specific collection, a sample from the Linked Open Data cloud). A number of entity homepages (i.e., ClueWeb docIDs) are made available as part of the topic definition, as examples of known relevant answers.The ELC task then is defined as follows: Given an information need and a list of known relevant entity homepages, return a list of relevant entity URIs from a specific collection of Linked Open Data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuYCCLX11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuYCCLX11,
		author = {Bingyang Liu and Fan Yang and Lei Cao and Xueqi Cheng and Yue Liu and Hongbo Xu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Entity {ELC} {TREC} 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ICTNET.entity.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuYCCLX11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TongKey at Entity Track TREC 2011: Related Entity Finding

_Zhengcai Pan, Haiguang Chen_

- :fontawesome-solid-user-group: **Participant:** [TongKey](./participants.md#tongkey)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/TongKey.entity.pdf](http://trec.nist.gov/pubs/trec20/papers/TongKey.entity.pdf)
- :material-file-search: **Runs:** [TongKeyEN1](./runs.md#tongkeyen1) | [TongKeyEN2](./runs.md#tongkeyen2)

??? abstract "Abstract"
	
	This paper presents our work done for the TREC 2011 Entity track. A retrieval model was proposed for the task of related entity finding. This model consists of several parts: In order to get more accurate document collection, query analysis method was utilized to format the narrative of each query. Then, our dataset was generated by using ClueWeb09 API2. Moreover, we employed the NER tools and text pattern recognition to extract entities from this processed dataset. In particular, the types of target entities are not so well-defined as last year. Therefore, a specific classifier trained by employing Wikipedia titles and category was utilized to identify the categories of target entities. To find related entity homepages and supporting documents, a set of feature-based methods were applied.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PanC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/PanC11,
		author = {Zhengcai Pan and Haiguang Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {TongKey at Entity Track {TREC} 2011: Related Entity Finding},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/TongKey.entity.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PanC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fasikom UI at TREC 2011 Entity List Completion Task

_Ananda Budi Prasetya, Hapnes Toba, Mirna Adriani, Hisar Maruli Manurung_

- :fontawesome-solid-user-group: **Participant:** [FASILKOMUI](./participants.md#fasilkomui)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/FASILKOM.entity.update.pdf](http://trec.nist.gov/pubs/trec20/papers/FASILKOM.entity.update.pdf)
- :material-file-search: **Runs:** [uiRunAll01](./runs.md#uirunall01) | [uiRunAll02](./runs.md#uirunall02) | [uiRunAll03](./runs.md#uirunall03)

??? abstract "Abstract"
	
	In this paper we describe our submissions to the TREC 2011 Entity Track. We have experimented with several combined approaches to search the entity candidates, i.e.: by resolving the linguistic relation of the given entity, query expansion by example to broader the retrieval results, and ontology approach to identify the named entity from the search result snippets and to retrieved the candidate entity. We rank the entity candidates based on the frequency of each entity in the web search result snippets. At the end of our system architecture we performed phrase-based search mechanism in the Sindice dump collection to retrieve specific URIs for the final entity list.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PrasetyaTAM11.bib) "
	```
	@inproceedings{DBLP:conf/trec/PrasetyaTAM11,
		author = {Ananda Budi Prasetya and Hapnes Toba and Mirna Adriani and Hisar Maruli Manurung},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Fasikom {UI} at {TREC} 2011 Entity List Completion Task},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/FASILKOM.entity.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PrasetyaTAM11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2011 Entity Track: Related Entity Finding and Entity  List Completion

_Zhanyi Wang, Wenlong Lv, Heng Li, Wenyuan Zhou, Li Zhang, Xiao Mo, Liaoming Zhou, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/PRIS.entity.update.pdf](http://trec.nist.gov/pubs/trec20/papers/PRIS.entity.update.pdf)
- :material-file-search: **Runs:** [PRISREF1](./runs.md#prisref1) | [PRISREF2](./runs.md#prisref2) | [PRISREF3](./runs.md#prisref3) | [PRISREF4](./runs.md#prisref4) | [PRISELC1](./runs.md#priselc1) | [PRISELC2](./runs.md#priselc2) | [PRISELC3](./runs.md#priselc3) | [PRISELC4](./runs.md#priselc4)

??? abstract "Abstract"
	
	The group of PRIS focuses on both tasks in Entity Track this year, Related Entity Finding (REF) and Entity List Completion (ELC). This paper reports the approaches to the two tasks. In REF, three points are improved based the method of last two year: building entity lexicons including more information, introducing a distance algorithm between keywords and entities to entity ranking, allocating homepages in a deeper and more reasonable way. The Entity Activation Force (EAF) and Affinity Measure are used in ELC task for completing and reordering the entity list. The evaluation of experimental results shows that the performance is better than previous ones significantly.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangLLZZMZXCG11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangLLZZMZXCG11,
		author = {Zhanyi Wang and Wenlong Lv and Heng Li and Wenyuan Zhou and Li Zhang and Xiao Mo and Liaoming Zhou and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2011 Entity Track: Related Entity Finding and Entity List Completion},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/PRIS.entity.update.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangLLZZMZXCG11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UALR at TREC 2011 Entity Track

_Venkata Swamy Martha, Halil Bisgin, Stephen Wallace, Nitin Agarwal, Xiaowei Xu, Hemant Joshi_

- :fontawesome-solid-user-group: **Participant:** [CARD.UALR](./participants.md#card.ualr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/CARD.UALR.entity.pdf](http://trec.nist.gov/pubs/trec20/papers/CARD.UALR.entity.pdf)
- :material-file-search: **Runs:** [CARDHTMLA](./runs.md#cardhtmla) | [CARDHTMLM](./runs.md#cardhtmlm) | [CARDHTMLB](./runs.md#cardhtmlb) | [CARDHTML](./runs.md#cardhtml)

??? abstract "Abstract"
	
	The primary objective of the track is to accomplish a mechanism to answer entity related searches over web data. The TREC organizers provided a segment of web data i.e. Clue Web09 data collection which is used for this work. An example of the entity related query is 'Countries other than Iceland to which Icelandair flies?'. To answer such queries, it needs two phases of processing, one is offline processing and the other is query time processing. During offline processing, the data is indexed using third party search engine tool. Query time processing involves query reformulation, extracting related documents from the index and document analysis to answer the query. Document analysis is the heart of the research which include entity identification and entity ranking based on a query. Since there is no readily available sophisticated entity identification tool, consensus approach is incorporated for entity identification. The consensus is achieved from Stanford NER tagger [1] Apache sentence detector with sentence parser [7] and DBpedia dataset lookup [9] A novel technique is developed to rank the entities related to a query. In other words, the identified entities from related documents are ranked based on their relevance to the query terms. Variations of query reformulations are: no reformulation, manual (human reformulated) and programmed using entity identification tool, resulted three submissions CARDHTML, CARDHTMLM and CARDHTMLA respectively. In addition to the above variations, we also used external web search engine (Bing) to extract related documents and submitted the run as CARDHTMLB. The submission also involved LOD URI look up which is achieved using organizers provided Sindice dataset [5] and its tool [10].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MarthaBWAXJ11.bib) "
	```
	@inproceedings{DBLP:conf/trec/MarthaBWAXJ11,
		author = {Venkata Swamy Martha and Halil Bisgin and Stephen Wallace and Nitin Agarwal and Xiaowei Xu and Hemant Joshi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UALR} at {TREC} 2011 Entity Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/CARD.UALR.entity.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MarthaBWAXJ11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

