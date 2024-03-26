# Proceedings 2011 

## Entity 

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

- :fontawesome-solid-user-group: **Participant:** [LIA](./entity/participants.md#lia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/LIA.entity.update.pdf](http://trec.nist.gov/pubs/trec20/papers/LIA.entity.update.pdf)
- :material-file-search: **Runs:** [LIAcwb](./entity/runs.md#liacwb) | [LIAwb](./entity/runs.md#liawb) | [LIAwc](./entity/runs.md#liawc) | [LIAwd](./entity/runs.md#liawd)

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

- :fontawesome-solid-user-group: **Participant:** [COMMIT](./entity/participants.md#commit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/COMMIT.entity.update.pdf](http://trec.nist.gov/pubs/trec20/papers/COMMIT.entity.update.pdf)
- :material-file-search: **Runs:** [ilpslinkOL](./entity/runs.md#ilpslinkol) | [ilpsTextFilt](./entity/runs.md#ilpstextfilt) | [ilpslinkcand](./entity/runs.md#ilpslinkcand) | [ilpsPMIcMNZ](./entity/runs.md#ilpspmicmnz)

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

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./entity/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ICTNET.entity.pdf](http://trec.nist.gov/pubs/trec20/papers/ICTNET.entity.pdf)
- :material-file-search: **Runs:** [ICTNET11ENR1](./entity/runs.md#ictnet11enr1) | [ICTNET11ENR2](./entity/runs.md#ictnet11enr2)

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

- :fontawesome-solid-user-group: **Participant:** [TongKey](./entity/participants.md#tongkey)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/TongKey.entity.pdf](http://trec.nist.gov/pubs/trec20/papers/TongKey.entity.pdf)
- :material-file-search: **Runs:** [TongKeyEN1](./entity/runs.md#tongkeyen1) | [TongKeyEN2](./entity/runs.md#tongkeyen2)

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

- :fontawesome-solid-user-group: **Participant:** [FASILKOMUI](./entity/participants.md#fasilkomui)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/FASILKOM.entity.update.pdf](http://trec.nist.gov/pubs/trec20/papers/FASILKOM.entity.update.pdf)
- :material-file-search: **Runs:** [uiRunAll01](./entity/runs.md#uirunall01) | [uiRunAll02](./entity/runs.md#uirunall02) | [uiRunAll03](./entity/runs.md#uirunall03)

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

- :fontawesome-solid-user-group: **Participant:** [PRIS](./entity/participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/PRIS.entity.update.pdf](http://trec.nist.gov/pubs/trec20/papers/PRIS.entity.update.pdf)
- :material-file-search: **Runs:** [PRISREF1](./entity/runs.md#prisref1) | [PRISREF2](./entity/runs.md#prisref2) | [PRISREF3](./entity/runs.md#prisref3) | [PRISREF4](./entity/runs.md#prisref4) | [PRISELC1](./entity/runs.md#priselc1) | [PRISELC2](./entity/runs.md#priselc2) | [PRISELC3](./entity/runs.md#priselc3) | [PRISELC4](./entity/runs.md#priselc4)

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

- :fontawesome-solid-user-group: **Participant:** [CARD.UALR](./entity/participants.md#card.ualr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/CARD.UALR.entity.pdf](http://trec.nist.gov/pubs/trec20/papers/CARD.UALR.entity.pdf)
- :material-file-search: **Runs:** [CARDHTMLA](./entity/runs.md#cardhtmla) | [CARDHTMLM](./entity/runs.md#cardhtmlm) | [CARDHTMLB](./entity/runs.md#cardhtmlb) | [CARDHTML](./entity/runs.md#cardhtml)

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

## Microblog 

#### Overview of the TREC 2011 Microblog Track

_Iadh Ounis, Craig Macdonald, Jimmy Lin, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec20/papers/MICROBLOG.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec20/papers/MICROBLOG.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Microblog track examines search tasks and evaluation methodologies for information seeking behaviours in microblogging environments such as Twitter. It was first introduced in 2011, addressing a real-time adhoc search task, whereby the user wishes to see the most recent but relevant information to the query. In particular, systems should respond to a query by providing a list of relevant tweets ordered from newest to oldest, starting from the time the query was issued. For TREC 2011, we used the newly-created Tweets2011 corpus. The corpus is comprised of 16M tweets over approximately two weeks, sampled courtesy of Twitter. The corpus is designed to be a reusable, representative sample of the twittersphere. As the reusability of a test collection is paramount in a TREC track, these sampled tweets can be obtained at any point in time (subjected to some caveats, discussed below). To accomplish this, the TREC Microblog track introduced a novel methodology whereby participants sign an agreement for the ids of the tweets in the corpus. Tools are then provided that permit the downloading of the corpus from the Twitter website. The first Microblog track in TREC 2011 has been a remarkable success. A total of 59 groups participated in the track from across the world, with 184 submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OunisMLS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/OunisMLS11,
		author = {Iadh Ounis and Craig Macdonald and Jimmy Lin and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {https://trec.nist.gov/pubs/trec20/papers/MICROBLOG.OVERVIEW.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OunisMLS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LiveTweet: Microblog Retrieval Based on Interestingness and an Adaptation  of the Vector Space Model

_Arifah Che Alhadi, Thomas Gottron, Jérôme Kunegis, Nasir Naveed_

- :fontawesome-solid-user-group: **Participant:** [WeST](./microblog/participants.md#west)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/WeST.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/WeST.microblog.update.pdf)
- :material-file-search: **Runs:** [WESTfilter](./microblog/runs.md#westfilter) | [WESTrelint](./microblog/runs.md#westrelint) | [WESTfilext](./microblog/runs.md#westfilext) | [WESTrlext](./microblog/runs.md#westrlext)

??? abstract "Abstract"
	
	This paper presents the Institute for Web Science and Technology's contribution to the TREC2011 Microblog Track. The goal of the Microblog Track is to address the user's information need in which a user wishes to see not only the most recent but also the most interesting and relevant information to a query in Twitter. In this paper we present the LiveTweet system, submitted by the Institute for Web Science and Technologies (WeST) from the University of Koblenz-Landau. The system addresses two issues of microblog media: sparsity and its effect on document length normalization, as well as the problem of assessing content quality. We provide the following approaches to overcome these issues: ignoring length normalization and using interestingness as a static quality measure to find the most recent and interesting tweets related to a given query topic. The results in similar settings have shown that deliberately ignoring length normalization yields better retrieval results in general and that interestingness improves retrieval for underspecified queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlhadiGKN11.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlhadiGKN11,
		author = {Arifah Che Alhadi and Thomas Gottron and J{\'{e}}r{\^{o}}me Kunegis and Nasir Naveed},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {LiveTweet: Microblog Retrieval Based on Interestingness and an Adaptation of the Vector Space Model},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/WeST.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlhadiGKN11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FUB, IASI-CNR, UNIVAQ at TREC 2011 Microblog Track

_Gianni Amati, Giuseppe Amodeo, Marco Bianchi, Giuseppe Marcone, Fondazione Ugo Bordoni, Carlo Gaibisso, Giorgio Gambosi, Alessandro Celi, Cesidio Di Nicola, Michele Flammini_

- :fontawesome-solid-user-group: **Participant:** [FUB](./microblog/participants.md#fub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/FUB.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/FUB.microblog.update.pdf)
- :material-file-search: **Runs:** [DFReeKLIM](./microblog/runs.md#dfreeklim) | [DFReeKLIM30](./microblog/runs.md#dfreeklim30) | [DFReeKLIMDC](./microblog/runs.md#dfreeklimdc) | [DFReeKLIMRA](./microblog/runs.md#dfreeklimra)

??? abstract "Abstract"
	
	The ad-hoc task of the microblogging track has an important theoretical impact for Information Retrieval. A key problem in Information Retrieval is, in fact, how to compare term frequencies among documents of different length. Apparently, term frequency normalization for microblogging can be simplified because of the short length constraint for the composition of admissible messages. The shortness of messages reduces the number of admissible values for the document length, and thus the length of a message can be regarded as if it were almost small and constant. On the other hand, short messages can carry a small amount of information, so that they are hardly distinguishable from each other for content. To overcome both problems, we propose to use a precise mathematical definition of information as the one given by Shannon [10] to provide an ad hoc IR model for Microblogging search. We show how to use Shannon's information theory and coding theory to weight the query content in Twitter messages and retrieve relevant messages. A second major problem of the microblogging track, as well as of any new collection of TREC, is the unavailability of a set of queries to derive and tune model parameters. Moreover, this is the first evaluation campaign on a new released corpus ever made for the microblogging search task, and in absence of any relevance data, it seems very interesting to define a retrieval methodology which is independent from relevance data, but still highly effective for the ranking of very short messages. Indeed, the proposed information theoretic methodology leads to the construction of a microblogging retrieval model that does not contain parameters to learn, and evaluation has shown the effectiveness of such parameter-free approach. In addition to these two major problems (i.e. how short length affects relevance and how to learn param- eters in absence of any relevance data), message recency is the only criterion applied to re-rank the retrieved messages. Thus, we regard the microblogging task more as a filtering decision task than as a ranking task. The new microblogging search task shares several similarities with some of the previous TREC evaluation campaigns, in particular with the past legal and blog TREC tracks. The legal track is basically a filtering task, that provides a large boolean retrieved set. In the legal track of TREC 2008 [8], for example, participants were asked to improve the quality of a given boolean baseline. This baseline was hard to improve according to the official evaluation measure. The task was to perform a dynamic cut-off value K in the ranking, being all evaluation measures estimated at the depth of this variable value for K, e.g. the precision and recall at depth K, P @K or R@K or other similar official measures used to assess the quality of the retrieved set. Similarly to the recency re-ordering of retrieved messages, in the TREC 2008 blog track [6] participants had to re-rank the documents by relevance according also to an opinion content dimension. An evaluation study however showed that filtering relevant documents by a second dimension or criterion, such as the opinionated content of documents, is often more harmful than performing a mild re-ranking strategy for the official MAP or P@10 measures [3] or even no re-ordering at all. As a consequence of these general remarks we made the following hypotheses and submissions: a) We have submitted a standard TREC baseline (the run named DFReeKLIM with 1000 messages retrieved per query) ordered by relevance only, that is without any time analysis, in order to assess how time re-ranking affects the precision at different depths of the retrieved set. b) Relevance by score distribution follows a mixture of two distributions (e.g. one exponential for the non-relevant documents, and the normal for the relevant ones [7,11]). Therefore, relevant documents have to be found on top of the ranking, and indeed P @K is a decreasing function with respect to K. It has been also observed that the precision at depth K, P @K, increases with collection size [5]. We assumed that relevance is dependent of recency of the messages. However, a pure re-ranking by time of the first K topmost messages, retrieved by relevance, hardly improve the official measure P @30 when K 6 = 30 since relevance scores and relevance ranks do not distribute uniformly but follow a power law. Therefore we submitted an official run retrieving exactly 30 messages per query (the run named DFReeKLIM30). c) We made a preliminary recency analysis. A dynamical cut to the retrieved set was introduced. The aim was to predict the best K documents for each query for which time reordering would have been successful. The mean threshold value for K was 73. The effectiveness of the methodology (run DFReeKLIMDC) must be assessed by the evaluation measures on time re-ranking. d) We explicitly assumed dependence of relevance with respect to time and used the time ranking as recency score to reorder by relevance the first pass retrieval. The effectiveness of the methodology can be thus assessed by the evaluation measures on relevance and not by time re-ranking, as performed by the official TREC measures (run DFReeKLIMRA).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmatiA0MBGGCNF11.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmatiA0MBGGCNF11,
		author = {Gianni Amati and Giuseppe Amodeo and Marco Bianchi and Giuseppe Marcone and Fondazione Ugo Bordoni and Carlo Gaibisso and Giorgio Gambosi and Alessandro Celi and Cesidio Di Nicola and Michele Flammini},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {FUB, IASI-CNR, {UNIVAQ} at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/FUB.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmatiA0MBGGCNF11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NUSIS at TREC 2011 Microblog Track: Refining Query Results with  Hashtags

_Hadi Amiri, Yang Bao, Anindya Datta, Xiaoying Xu, Anqi Cui_

- :fontawesome-solid-user-group: **Participant:** [NUSIS](./microblog/participants.md#nusis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/NUSIS.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/NUSIS.microblog.pdf)
- :material-file-search: **Runs:** [relevanceRun](./microblog/runs.md#relevancerun) | [balanceRun](./microblog/runs.md#balancerun) | [refRelRun](./microblog/runs.md#refrelrun) | [refBalRun](./microblog/runs.md#refbalrun)

??? abstract "Abstract"
	
	In this paper, we describe our submission to the TREC 2011 Microblog track. We first use URLs as a clue to discover and remove the spam tweets. Then we use both Lucene and Indri to generate a ranked list of results for each query, together with their relevance scores. After that, we use the scores to find out useful hashtags relevant to the query, therefore some previously lower-ranked tweets can be discovered and are re-ranked higher. Query reformulation is considered in two of the four runs in our submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmiriBDXC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmiriBDXC11,
		author = {Hadi Amiri and Yang Bao and Anindya Datta and Xiaoying Xu and Anqi Cui},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NUSIS} at {TREC} 2011 Microblog Track: Refining Query Results with Hashtags},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/NUSIS.microblog.pdf},
		timestamp = {Mon, 03 May 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AmiriBDXC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion for Microblog Retrieval

_Ayan Bandyopadhyay, Mandar Mitra, Prasenjit Majumder_

- :fontawesome-solid-user-group: **Participant:** [IRSI](./microblog/participants.md#irsi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/IRSI.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/IRSI.microblog.update.pdf)
- :material-file-search: **Runs:** [IRSIGoogle1G](./microblog/runs.md#irsigoogle1g) | [IRSIGoogle2G](./microblog/runs.md#irsigoogle2g) | [Google1GNO](./microblog/runs.md#google1gno) | [InL2c1](./microblog/runs.md#inl2c1)

??? abstract "Abstract"
	
	Entries in microblogging sites such as Twitter are very short: a “tweet ”can contain at most 140 characters. Given a user query, retrieving relevant tweets is particularly challenging since their extreme brevity exacerbates the well-known vocabulary mismatch problem. In this preliminary study, we explore standard query expansion approaches as a way to address this problem. Since the tweets are short, we use external corpora as a source for query expansion terms. Specifically, we used the Google Search API (GSA) to retrieve pages from the Web, and used the titles to expand queries. Initial results on the TREC 2011 Microblog test data are very promising. Since many of the TREC topics were oriented towards the news genre, we also tried restricting the GSA to a news site (BBC) in the hope that it would be a cleaner, less noisy source for expansion terms. This turned out to be counter-productive. Some analysis of these results is also included.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BandyopadhyayMM11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BandyopadhyayMM11,
		author = {Ayan Bandyopadhyay and Mandar Mitra and Prasenjit Majumder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Query Expansion for Microblog Retrieval},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/IRSI.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BandyopadhyayMM11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ISTI@TREC Microblog Track 2011: Exploring the Use of Hashtag Segmentation  and Text Quality Ranking

_Giacomo Berardi, Andrea Esuli, Diego Marcheggiani, Fabrizio Sebastiani_

- :fontawesome-solid-user-group: **Participant:** [NEMIS_ISTI_CNR](./microblog/participants.md#nemis_isti_cnr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/NEMIS_ISTI_CNR.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/NEMIS_ISTI_CNR.microblog.update.pdf)
- :material-file-search: **Runs:** [runNeMIS](./microblog/runs.md#runnemis) | [runNeMISext](./microblog/runs.md#runnemisext)

??? abstract "Abstract"
	
	In the first year of the TREC Micro Blog track, our participation has focused on building from scratch an IR system based on the Whoosh IR library. Though the design of our system (CipCipPy) is pretty standard it includes three ad-hoc solutions for the track: (i) a dedicated indexing function for hashtags that automatically recognizes the distinct words composing an hashtag, (ii) expansion of tweets based on the title of any referred Web page, and (iii) a tweet ranking function that ranks tweets in results by their content quality, which is compared against a reference corpus of Reuters news. In this preliminary paper we describe all the components of our system, and the efficacy scored by our runs. The CipCipPy system is available under a GPL license.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BerardiEMS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BerardiEMS11,
		author = {Giacomo Berardi and Andrea Esuli and Diego Marcheggiani and Fabrizio Sebastiani},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {ISTI@TREC Microblog Track 2011: Exploring the Use of Hashtag Segmentation and Text Quality Ranking},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/NEMIS\_ISTI\_CNR.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BerardiEMS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Microblog Track TREC 2011

_Peng Cao, Jinhua Gao, Yubao Yu, Shenghua Liu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./microblog/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ICTNET.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/ICTNET.microblog.pdf)
- :material-file-search: **Runs:** [ICTNET11MBR1](./microblog/runs.md#ictnet11mbr1) | [ICTNET11MBR2](./microblog/runs.md#ictnet11mbr2) | [ICTNET11MBR3](./microblog/runs.md#ictnet11mbr3) | [ICTNET11MBR4](./microblog/runs.md#ictnet11mbr4)

??? abstract "Abstract"
	
	The ICTNET group has participated in the Microblog track of TREC 2011. The main task is to search the messy tweets for those about a topic that is represented by a query. There are 50 queries, i.e. topics given for the track totally. Besides the topic description, a query time is also given for each query, indicating the exact time of the query issuance. The search is supposed to be conducted onsite, and those tweets later than the query time should not be returned. Furthermore, the issuers wishes to see the most recent but relevant information to the query. Hence, our system should answer a query by providing a list of relevant tweets ordered from newest to oldest, starting from the time the query was issued. The existing related work about microblog is mainly focused on users [1-2], information flow [3-4], and tweets' content [5-6]. Our work is to query the tweets' content to find relevant, interesting, and fresh tweets. With exploring the features of tweets' content, hashtags, urls, post time etc., we employ SVM ranking model to rank our query results. The model is trained on pair-wise labeled data. Query extension both within tweets and external Wikipedia articles and Google search results are conducted by pseudo relevance feedback method and keywords extracting. In our experiment, 4 running results of 50 queries are collected on more than 5.6 million English tweets. There are 64.6% relevant tweets retrieved in less than 1000 returned results, and 449 relevant tweets are retrieved in top 30 according our ranking scores. The rest of the report is organized as follows. Section 2 introduces the data preprocessing. Section 3 describes our main method to rank the search results namely the learning to rank. Section 4 shows the experiment results, and section 5 concludes the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaoGYLLC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaoGYLLC11,
		author = {Peng Cao and Jinhua Gao and Yubao Yu and Shenghua Liu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Microblog Track {TREC} 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ICTNET.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CaoGYLLC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Simple Rank-Based Filtering for Microblog Retrieval: Implications  for Evaluation and Test Collections

_Ben Carterette, Naveen Kumar, Ashwani Rao, Dongqing Zhu_

- :fontawesome-solid-user-group: **Participant:** [udel](./microblog/participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/udel.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/udel.microblog.pdf)
- :material-file-search: **Runs:** [udelIndri](./microblog/runs.md#udelindri) | [udelLucene](./microblog/runs.md#udellucene)

??? abstract "Abstract"
	
	The IR Lab at the University of Delaware participated in the first year of the TREC Microblog track. We submitted two runs using two different indexers and ranking functions, one of which filtered results by a score threshold. The results inspired some post hoc analysis of the test collection, which is the main focus of this paper. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarteretteKRZ11.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarteretteKRZ11,
		author = {Ben Carterette and Naveen Kumar and Ashwani Rao and Dongqing Zhu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Simple Rank-Based Filtering for Microblog Retrieval: Implications for Evaluation and Test Collections},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/udel.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarteretteKRZ11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Microblog 2011

_Firas Damak, Lamjed Ben Jabeur, Guillaume Cabanac, Karen Pinel-Sauvagnat, Lynda Tamine, Mohand Boughanem_

- :fontawesome-solid-user-group: **Participant:** [IRIT_SIG](./microblog/participants.md#irit_sig)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/IRIT_SIG.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/IRIT_SIG.microblog.update.pdf)
- :material-file-search: **Runs:** [iritfd1](./microblog/runs.md#iritfd1) | [iritfd2](./microblog/runs.md#iritfd2) | [Nestor](./microblog/runs.md#nestor) | [NestorS](./microblog/runs.md#nestors)

??? abstract "Abstract"
	
	This paper describes the participation of the IRIT lab, university of Toulouse, France, to the Microblog Track of TREC 2011. Two different approaches were experimented by our team, which are described in the two main parts of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DamakJCPTB11.bib) "
	```
	@inproceedings{DBLP:conf/trec/DamakJCPTB11,
		author = {Firas Damak and Lamjed Ben Jabeur and Guillaume Cabanac and Karen Pinel{-}Sauvagnat and Lynda Tamine and Mohand Boughanem},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRIT} at {TREC} Microblog 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/IRIT\_SIG.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DamakJCPTB11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting Social #-Tagging Behavior in Twitter for Information  Filtering and Recommendation

_Ernesto Diaz-Aviles, Patrick Siehndel, Kaweh Djafari Naini_

- :fontawesome-solid-user-group: **Participant:** [L3S](./microblog/participants.md#l3s)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/L3S.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/L3S.microblog.update.pdf)
- :material-file-search: **Runs:** [qHtagBaseRun](./microblog/runs.md#qhtagbaserun)

??? abstract "Abstract"
	
	We present a ranking approach for Twitter documents that exploits social hashtagging behavior. We first map topics of user interest, represented by keywords, to a set of twitter hashtags that we use as query terms to retrieve twitter documents (tweets) based on tf-idf scores, with the additional restrictions that the documents retrieved should occur before the query timestamp. We show that this simple method performs significantly better than a disjunctive baseline based on the topic description.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Diaz-AvilesSN11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Diaz-AvilesSN11,
		author = {Ernesto Diaz{-}Aviles and Patrick Siehndel and Kaweh Djafari Naini},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploiting Social {\#}-Tagging Behavior in Twitter for Information Filtering and Recommendation},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/L3S.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Diaz-AvilesSN11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Illinois' Graduate School of Library and Information  Science at TREC 2011

_Miles Efron_

- :fontawesome-solid-user-group: **Participant:** [gslisUIUC](./microblog/participants.md#gslisuiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/gslisUIUC.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/gslisUIUC.microblog.update.pdf)
- :material-file-search: **Runs:** [gus](./microblog/runs.md#gus) | [gust](./microblog/runs.md#gust) | [gustc](./microblog/runs.md#gustc) | [gut](./microblog/runs.md#gut)

??? abstract "Abstract"
	
	The University of Illinois' Graduate School of Library and Information Science (GSLIS) participated in TREC's microblog track this year-the track's first iteration. In keeping with the foundational status of the track, our goals were chosen to emphasize the role of a single factor in microblog IR: time. As such, we adhered to the strictest guidelines of the task description, using only real-time information available in the microblog corpus to inform retrieval. Our innovation involved assessing the extent to which (and the way in which) temporal factors can improve microblog search effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Efron11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Efron11,
		author = {Miles Efron},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Illinois' Graduate School of Library and Information Science at {TREC} 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/gslisUIUC.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Efron11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Online Topic Modeling for Real-Time Twitter Search

_Christan Earl Grant, Clint P. George, Chris Jenneisch, Joseph N. Wilson_

- :fontawesome-solid-user-group: **Participant:** [Morpheus](./microblog/participants.md#morpheus)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Morpheus.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Morpheus.microblog.update.pdf)
- :material-file-search: **Runs:** [MorpheusRun1](./microblog/runs.md#morpheusrun1)

??? abstract "Abstract"
	
	This paper discusses the work done by a team at the University of Florida for the TREC 2011 Microblog Track. To build a real-time microblog search engine we rely on topic modeling for our search. To facilitate our algorithms we bundle similar tweets together in what we call supertweet generation. We perform online inference and offline inference depending on the time frame of the topical query. In this paper we discuss our techniques, challenges, future work, but not the evaluation of our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrantGJW11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrantGJW11,
		author = {Christan Earl Grant and Clint P. George and Chris Jenneisch and Joseph N. Wilson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Online Topic Modeling for Real-Time Twitter Search},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Morpheus.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrantGJW11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melbourne Language Group Microblog Track Report

_Bo Han, Marco Lui, Timothy Baldwin_

- :fontawesome-solid-user-group: **Participant:** [UniMelbLT](./microblog/participants.md#unimelblt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UniMelbLT.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UniMelbLT.microblog.update.pdf)
- :material-file-search: **Runs:** [melblt](./microblog/runs.md#melblt)

??? abstract "Abstract"
	
	This report outlines the TREC 2011 microblog track submission of the Language Technology Group at The University of Melbourne. The microblog track is an ad-hoc retrieval task over Twitter data with temporally-specified queries, and the requirement that all results must predate the query. Our objective is to establish baseline results for the task and study the relative impact of various factors on microblog retrieval. Twitter messages are authored in many different languages (Hong et al., 2011), but the queries were all monolingual English and assessors where instructed to base their judgements on only the English content of tweets. As such, we first conduct language identification to filter out non-English tweets (Baldwin and Lui, 2010). Next, we lexically-normalise tweets, to remove typos and phonetic substitutions, and deabbreviate common abbreviations (Han and Baldwin, 2011). Finally, we index the language-filtered, normalised documents using Indri,1 apply dynamic lexical normalisation to the queries, and temporally filter the results relative to the query timestamp. Descriptions of each module in our system are presented in the following sections. As we use language processing tools and a dictionary as part of the lexical normalisation, our submission is classified as making use of external evidence.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HanLB11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HanLB11,
		author = {Bo Han and Marco Lui and Timothy Baldwin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Melbourne Language Group Microblog Track Report},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UniMelbLT.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HanLB11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Expansion and Message-Passing Algorithms for TREC Microblog  Track

_Dzung Hong, Qifan Wang, Dan Zhang, Luo Si_

- :fontawesome-solid-user-group: **Participant:** [Purdue_IR](./microblog/participants.md#purdue_ir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Purdue_IR.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Purdue_IR.microblog.update.pdf)
- :material-file-search: **Runs:** [myRun](./microblog/runs.md#myrun) | [myrun3](./microblog/runs.md#myrun3) | [myrun2](./microblog/runs.md#myrun2)

??? abstract "Abstract"
	
	This report describes the methods that our Information Retrieval Group at Purdue University used for the TREC Microblog 2011 track. The first method is the pseudo-relevance feedback, a traditional algorithm to reformulate the query by adding expanded terms to the query. The second method is the affinity propagation, a non parametric clustering algorithm that can group the top tweets according to their similarities. The final score of a tweet is based on its relevance score and the relevance score of its representative in the group. We found that query expansion is a very useful technique for microblog retrieval, while affinity propagation could achieve a comparable performance when combining with other techniques.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HongWZS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HongWZS11,
		author = {Dzung Hong and Qifan Wang and Dan Zhang and Luo Si},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Query Expansion and Message-Passing Algorithms for {TREC} Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Purdue\_IR.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HongWZS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Realtime Ad Hoc Search in Twitter: Know-Center at TREC Microblog  Track 2011

_Christopher Horn, Oliver Pimas, Michael Granitzer, Elisabeth Lex_

- :fontawesome-solid-user-group: **Participant:** [knowcenter](./microblog/participants.md#knowcenter)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/knowcenter.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/knowcenter.microblog.update.pdf)
- :material-file-search: **Runs:** [1](./microblog/runs.md#1) | [2](./microblog/runs.md#2) | [3](./microblog/runs.md#3) | [4](./microblog/runs.md#4)

??? abstract "Abstract"
	
	In this paper, we outline our experiments carried out at the TREC Microblog Track 2011. Our system is based on a plain text index extracted from Tweets crawled from twitter.com. This index has been used to retrieve candidate Tweets for the given topics. The resulting Tweets were post-processed and then analyzed using three different approaches: (i) a burst detection approach, (ii) a hashtag analysis, and (iii) a Retweet analysis. Our experiments consisted of four runs: Firstly, a combination of the Lucene ranking with the burst detection, and secondly, a combination of the Lucene ranking, the burst detection, and the hashtag analysis. Thirdly, a combination of the Lucene ranking, the burst detection, the hashtag analysis, and the Retweet analysis, and fourthly, again a combination of the Lucene ranking with the burst detection but in this case with more sophisticated query language and post-processing. We achieved the best MAP values overall in the fourth run.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HornPGL11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HornPGL11,
		author = {Christopher Horn and Oliver Pimas and Michael Granitzer and Elisabeth Lex},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Realtime Ad Hoc Search in Twitter: Know-Center at {TREC} Microblog Track 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/knowcenter.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HornPGL11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lugano at TREC 2011 Microblog Track

_Giacomo Inches_

- :fontawesome-solid-user-group: **Participant:** [ULugano](./microblog/participants.md#ulugano)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ULugano.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/ULugano.microblog.update.pdf)
- :material-file-search: **Runs:** [baselineBM25](./microblog/runs.md#baselinebm25)

??? abstract "Abstract"
	
	In this document we present the participation of University of Lugano in the Microblog track of TREC 2011. We describe our approach based on a time-based filtering algorithm of retrieved documents. We highlight the results and the possible improvement of the described technique.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Inches11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Inches11,
		author = {Giacomo Inches},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Lugano at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ULugano.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Inches11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BEST of KAUST at TREC 2011: Building Effective Search in Twitter

_Jinling Jiang, Lailatul Hidayah, Hany E. Ramadan, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [KAUST](./microblog/participants.md#kaust)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/kaust.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/kaust.microblog.update.pdf)
- :material-file-search: **Runs:** [KAUSTExpRrnk](./microblog/runs.md#kaustexprrnk) | [KAUSTExp](./microblog/runs.md#kaustexp) | [KAUSTRerank](./microblog/runs.md#kaustrerank) | [KAUSTBase](./microblog/runs.md#kaustbase)

??? abstract "Abstract"
	
	In our first-ever appearance at TREC, we explore initial ideas on building an effective search tool over tweet stream as a participation in this year's microblog track. Among those ideas are tweet expansion with short representation of terms that frequently co-occur with hashtags and URLs, and re-ranking based on statistics that estimate user popularity (using replies and mentions), tweet popularity, URL popularity and user topic authority (using simple user profiles). Initial results show that re-ranking improves the effectiveness while expansion sometimes harms it. Overall, the system built for the task is indeed a great resource for further extensions and experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangHREL11.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangHREL11,
		author = {Jinling Jiang and Lailatul Hidayah and Hany E. Ramadan and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BEST} of {KAUST} at {TREC} 2011: Building Effective Search in Twitter},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/kaust.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangHREL11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### QCRI @ TREC 2011: Microblog Track

_Ali El Kahki, Kareem Darwish_

- :fontawesome-solid-user-group: **Participant:** [QCRI](./microblog/participants.md#qcri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/QCRI.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/QCRI.microblog.pdf)
- :material-file-search: **Runs:** [QCRIwTagOrg](./microblog/runs.md#qcriwtagorg) | [QCRIwoTagOrg](./microblog/runs.md#qcriwotagorg) | [nQCRIwTag](./microblog/runs.md#nqcriwtag) | [nQCRIwoTag](./microblog/runs.md#nqcriwotag)

??? abstract "Abstract"
	
	This paper briefly describes the Qatar Computing Research Institute (QCRI) participation in the TREC 2011 Microblog track. The focus of our TREC submissions was on using a generative graphic model to perform query expansion. We trained a model that attempted to predict appropriate hashtags to expand tweets as well as queries. In essence, we used hashtags to represent latent topics in tweets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KahkiD11.bib) "
	```
	@inproceedings{DBLP:conf/trec/KahkiD11,
		author = {Ali El Kahki and Kareem Darwish},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{QCRI} @ {TREC} 2011: Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/QCRI.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KahkiD11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microblog Retrieval Using Topical Features and Query Expansion

_Cher Han Lau, Yuefeng Li, Dian Tjondronegoro_

- :fontawesome-solid-user-group: **Participant:** [QUT1](./microblog/participants.md#qut1)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/QUT1.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/QUT1.microblog.pdf)
- :material-file-search: **Runs:** [run3a](./microblog/runs.md#run3a) | [run4a](./microblog/runs.md#run4a) | [run1a](./microblog/runs.md#run1a) | [run2a](./microblog/runs.md#run2a)

??? abstract "Abstract"
	
	Retrieving information from Twitter is always challenging given its volume, inconsistent writing and noise. Existing systems focus on term-based approach, but important topical features such as person, proper noun and events are often neglected, leading to less satisfactory results while searching information from tweets. This paper propose a novelty feature extraction algorithm which targets the above problems, and present the experiment results using TREC11 dataset. The proposed approach considers both term-based and pattern-based features and distribute weights accordingly. We experiment four different setting to evaluate different combinations and results show that our approach outperformed traditional method of using term-based or pattern only methods and signify the importance of topical features in microblog retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LauLT11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LauLT11,
		author = {Cher Han Lau and Yuefeng Li and Dian Tjondronegoro},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microblog Retrieval Using Topical Features and Query Expansion},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/QUT1.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LauLT11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HIT_LTRC at TREC 2011 Microblog Track

_Yun Li, Xishuang Dong, Yi Guan_

- :fontawesome-solid-user-group: **Participant:** [HIT_LTRC](./microblog/participants.md#hit_ltrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/HIT_LTRC.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/HIT_LTRC.microblog.pdf)
- :material-file-search: **Runs:** [hitWIt](./microblog/runs.md#hitwit) | [hitWId](./microblog/runs.md#hitwid)

??? abstract "Abstract"
	
	This paper describes our entry into the TREC 2011 Microblog track. We submitted two runs in this year's track, both in real-time fashion and without any external resources. The runs were generated through a three-step procedure, including scoring, threshold selection and re-ranking. The evaluation results of our submitted runs significantly outperform the disjunctive baseline run. We conducted additional runs to show our score decay and threshold selection strategies to be exceptionally effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiDG11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiDG11,
		author = {Yun Li and Xishuang Dong and Yi Guan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {HIT{\_}LTRC at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/HIT\_LTRC.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiDG11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DMIR on Microblog Track 2011

_Wen Li, Carsten Eickhoff, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [TUD_DMIR](./microblog/participants.md#tud_dmir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/TUD-DMIR.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/TUD-DMIR.microblog.pdf)
- :material-file-search: **Runs:** [EMAX](./microblog/runs.md#emax) | [RTB](./microblog/runs.md#rtb)

??? abstract "Abstract"
	
	In this paper we present our work on the Microblog Track of TREC 2011. We tried two methods to tackle the problem of tweet retrieval, namely EMAX and RTB. The first method EMAX is mainly based on the intuition that not only should retrieved tweets related to the keywords in given queries but also provide more information. This results in a ranking method based on self-information. Our second method RTB tries to incorporate the importance of recency along with relevance in microblog retrieval tasks. Therefore, we adapt portfolio theory to balance the relevance dimension and recency dimension. However, the evaluation results suggest no significant improvement from both two methods because of the short lengths of documents, the noisy and spam tweets and the re-ordering in recency. Meanwhile, we also present some ideas during the course of participation. By closely examining the judgments, we find that most of relevant documents are those containing a link to external resource and have a length of around 17 words, which is different from the statistics observed in the collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiEV11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiEV11,
		author = {Wen Li and Carsten Eickhoff and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DMIR} on Microblog Track 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/TUD-DMIR.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiEV11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Author Model and Negative Feedback Methods on TREC 2011 Microblog  Track

_Rui Li, Binjie Wei, Kai Lu, Bin Wang_

- :fontawesome-solid-user-group: **Participant:** [ICTIR](./microblog/participants.md#ictir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ICTIR.microblog.new.pdf](http://trec.nist.gov/pubs/trec20/papers/ICTIR.microblog.new.pdf)
- :material-file-search: **Runs:** [baseline](./microblog/runs.md#baseline) | [run1](./microblog/runs.md#run1) | [run1fix](./microblog/runs.md#run1fix) | [run2](./microblog/runs.md#run2)

??? abstract "Abstract"
	
	This paper gives an overview of our work (the ICTIR group) in microblog track of TREC 2011 for tweets retrieval. The basic query likelihood model with smoothing is the fundamental method in our approaches, we also consider other factors: the author information and the negative feedback. Firstly, we classify all queries into three categories, construct refined feedback in different ways to reform them; Secondly, extremely short tweets lead to poor clustering performance, the author topic models are trained for tweets expansion and smoothing. Finally, we train negative feedback model to reduce noise impacts in our microblog search task. Experimental results show that our methods could improve the retrieval performance greatly.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiWLW11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiWLW11,
		author = {Rui Li and Binjie Wei and Kai Lu and Bin Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Author Model and Negative Feedback Methods on {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ICTIR.microblog.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiWLW11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2011 Microblog Track

_Yan Li, Zhenhua Zhang, Wenlong Lv, Qianlong Xie, Yuhang Lin, Rao Xu, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./microblog/participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/PRIS.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/PRIS.microblog.pdf)
- :material-file-search: **Runs:** [PRISrun1](./microblog/runs.md#prisrun1) | [PRISrun2](./microblog/runs.md#prisrun2) | [PRISrun3](./microblog/runs.md#prisrun3) | [PRISrun4](./microblog/runs.md#prisrun4)

??? abstract "Abstract"
	
	Our system to Micro-blog Track at TREC2011 is described in this paper, which includes data obtaining and preprocessing, index building and query expansion. There‟re two methods of query expansion introduced in this report: Word Activation Force algorithm (WAF) and Electric Resistance Network. We also show the evaluation results for our team and the comparison with the best and median evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiZLXLXXCG11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiZLXLXXCG11,
		author = {Yan Li and Zhenhua Zhang and Wenlong Lv and Qianlong Xie and Yuhang Lin and Rao Xu and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/PRIS.microblog.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiZLXLXXCG11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKU_ICST at TREC 2011 Microblog Track

_Feng Liang, Runwei Qiang, Jianwu Yang_

- :fontawesome-solid-user-group: **Participant:** [PKU_ICST](./microblog/participants.md#pku_icst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/PKU_ICST.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/PKU_ICST.microblog.update.pdf)
- :material-file-search: **Runs:** [PKUICST](./microblog/runs.md#pkuicst) | [PKUICST2](./microblog/runs.md#pkuicst2) | [PKUICST3](./microblog/runs.md#pkuicst3) | [PKUICST4](./microblog/runs.md#pkuicst4)

??? abstract "Abstract"
	
	This paper describes the PKU_ICST participation in the TREC 2011 Microblog track. In the first year of Microblog track, we designed a group of experiments to verify whether external resources and future resources would improve the performance of our system. Moreover, given that microblog track is a real-­-‑time adhoc task, we explored an approach making use of the temporal evidence. To obtain a better performance, we employed different strategies to generate final results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiangQY11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiangQY11,
		author = {Feng Liang and Runwei Qiang and Jianwu Yang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {PKU{\_}ICST at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/PKU\_ICST.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiangQY11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Indonesia at TREC 2011 Microblog Task

_Samuel Louvan, Mochamad Ibrahim, Mirna Adriani, Clara Vania, Bayu Distiawan, Metti Zakaria Wanagiri_

- :fontawesome-solid-user-group: **Participant:** [FASILKOMUI](./microblog/participants.md#fasilkomui)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/FASILKOM.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/FASILKOM.microblog.update.pdf)
- :material-file-search: **Runs:** [FASILKOM01](./microblog/runs.md#fasilkom01) | [FASILKOM03](./microblog/runs.md#fasilkom03) | [FASILKOM04](./microblog/runs.md#fasilkom04) | [FASILKOM02](./microblog/runs.md#fasilkom02)

??? abstract "Abstract"
	
	In this paper we describe our submission to the TREC2011 MicroblogTrack. Our run combines different methods namely customized scoring function, query reformulation, and query expansion. We apply query expansion from dataset with different weighting scheme. Furthermore, we do an initial experiment to incorporate timestamp of the tweet document in order to improve search performance. We found the query expansion utilizing external search result combined with re-tweet value in the customized scoring function was the most effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LouvanIAVDW11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LouvanIAVDW11,
		author = {Samuel Louvan and Mochamad Ibrahim and Mirna Adriani and Clara Vania and Bayu Distiawan and Metti Zakaria Wanagiri},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Indonesia at {TREC} 2011 Microblog Task},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/FASILKOM.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LouvanIAVDW11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### USC/ISI at TREC 2011: Microblog Track

_Donald Metzler, Congxing Cai_

- :fontawesome-solid-user-group: **Participant:** [isi](./microblog/participants.md#isi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/isi.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/isi.microblog.update.pdf)
- :material-file-search: **Runs:** [isiFD](./microblog/runs.md#isifd) | [isiFDL](./microblog/runs.md#isifdl) | [isiFDRML](./microblog/runs.md#isifdrml) | [isiFDRM](./microblog/runs.md#isifdrm)

??? abstract "Abstract"
	
	This paper describes the search system we developed for the inaugural TREC 2011 Microblog Track. Our system makes use of best-practice ranking techniques, including term, phrase, and proximity-based text matching via the Markov random field model, pseudo-relevance feedback using Latent Concept Expansion, and a feature-based ranking model that uses a simple, but effective learning-to-rank model. We adapted each of these approaches to the specifics of the microblog search task, giving rise to a highly effective end-to-end search system. The official results from the TREC evaluation suggest that pseudo-relevance feedback and learning-to-rank yield significant improvements in precision at early rank under different evaluation scenarios.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MetzlerC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/MetzlerC11,
		author = {Donald Metzler and Congxing Cai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{USC/ISI} at {TREC} 2011: Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/isi.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MetzlerC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2011 Microblog Track Experiments at Kobe University

_Taiki Miyanishi, Naoto Okamura, Xiaoxi Liu, Kazuhiro Seki, Kuniaki Uehara_

- :fontawesome-solid-user-group: **Participant:** [KobeU](./microblog/participants.md#kobeu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/KobeU.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/KobeU.microblog.update.pdf)
- :material-file-search: **Runs:** [rit](./microblog/runs.md#rit) | [ri](./microblog/runs.md#ri) | [normal](./microblog/runs.md#normal) | [rit3](./microblog/runs.md#rit3)

??? abstract "Abstract"
	
	This paper describes our approach to real-time microblog search that returns tweets for a given query in reverse chronological order. The approach utilizes a learning-to-rank (L2R) algorithm that has been increasingly used for information retrieval (IR). Generally, L2R algorithms require features which represent the associations between a user query and a document (tweet in this case). However, it is more difficult for microblog search to obtain rich features than traditional document search because the contents of microblog are too short: limited to only 140 characters. In addition, there is no standard, publicly available training data for learning to rank microblogs. To solve these problems, we generate new features by clustering large microblog data (the Tweets2011 corpus). The features are de ned for triplets ⟨user query, tweet, cluster⟩ and represent the relevance of the tweet with respect to both the query and its topic (cluster). An L2R model is learned using the generated features as well as other features on labeled training data manually created by our research group. The effectiveness of the proposed approach is demonstrated by comparative experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MiyanishiOLSU11.bib) "
	```
	@inproceedings{DBLP:conf/trec/MiyanishiOLSU11,
		author = {Taiki Miyanishi and Naoto Okamura and Xiaoxi Liu and Kazuhiro Seki and Kuniaki Uehara},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2011 Microblog Track Experiments at Kobe University},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/KobeU.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MiyanishiOLSU11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Yandex at TREC 2011 Microblog Track

_Zlata Obukhovskaya, Konstantin Pervyshev, Andrey Styskin, Pavel Serdyukov_

- :fontawesome-solid-user-group: **Participant:** [yandex](./microblog/participants.md#yandex)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/yandex.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/yandex.microblog.update.pdf)
- :material-file-search: **Runs:** [YNDXTPC2](./microblog/runs.md#yndxtpc2) | [YNDXTPC1](./microblog/runs.md#yndxtpc1) | [ya3](./microblog/runs.md#ya3) | [ya4](./microblog/runs.md#ya4)

??? abstract "Abstract"
	
	Building microblog search is a challenging task in many ways. One of its most exciting aspects is the creation of reliable search engine architecture. However in our work we focused on tweet retrieval, utilizing relevance signals coming from various sources related to a tweet and learning to rank. For ranking-related tasks we decided to rely on the following data sources: Text sources: tweet itself and the title of the linked URL: Crowd activity (retweets) We assumed that the number of retweets should be a good indicator of social interest to the particular document and the retweet prediction would be a useful feature for ranking. Also we encountered a problem with low recall of TF-based retrieval on small-sized twitter documents. This prompted us to use flexible term weighting models and query expansion to avoid missing relevant results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ObukhovskayaPSS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ObukhovskayaPSS11,
		author = {Zlata Obukhovskaya and Konstantin Pervyshev and Andrey Styskin and Pavel Serdyukov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Yandex at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/yandex.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ObukhovskayaPSS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Wolverhampton at the TREC 2011 Microblog Track

_Georgios Paltoglou, Mike Thelwall_

- :fontawesome-solid-user-group: **Participant:** [UoW](./microblog/participants.md#uow)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UoW.microblog.new.pdf](http://trec.nist.gov/pubs/trec20/papers/UoW.microblog.new.pdf)
- :material-file-search: **Runs:** [PL2NoQeSd](./microblog/runs.md#pl2noqesd) | [PL2NoQeSdExt](./microblog/runs.md#pl2noqesdext) | [PL2NoQENoDM](./microblog/runs.md#pl2noqenodm) | [PL2Bo1SDExt](./microblog/runs.md#pl2bo1sdext)

??? abstract "Abstract"
	
	In this report we discuss the experiments we conducted at the University of Wolverhampton for the Microblog Track at TREC-2011. As this was the first time we participated in TREC and the particular task presents some unique challenges we initially focused on properly analyzing and indexing the new Tweets2011 Corpus. We experimented with the effects that some standard IR techniques, such as query expansion and proximity models have in this setting. Initial results indicated that both techniques provide small increases in precision, but more experiments are needed for final conclusions to be reached. Lastly, we experimented with using the page that a tweet links to as part of the tweet. The results were particularly low, indicating a potential error in the indexing process or a natural outcome, due to the increased length of the combined documents. More research into answering the issue is underway.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PaltoglouT11.bib) "
	```
	@inproceedings{DBLP:conf/trec/PaltoglouT11,
		author = {Georgios Paltoglou and Mike Thelwall},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Wolverhampton at the {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UoW.microblog.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PaltoglouT11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at TREC 2011 Microblog Track

_Matthias Petri, J. Shane Culpepper, Falk Scholer_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./microblog/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/RMIT.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/RMIT.microblog.pdf)
- :material-file-search: **Runs:** [RMITM](./microblog/runs.md#rmitm) | [RMITMR](./microblog/runs.md#rmitmr) | [RMITAR](./microblog/runs.md#rmitar) | [RMITMRR](./microblog/runs.md#rmitmrr)

??? abstract "Abstract"
	
	This paper describes our submission to the TREC 2011 microblog task. For the experiments, we use our new self-index search engine, NeWT, to support ranked search in the Twitter document corpus. We use a combination of phrase queries and degrading conjunctive Boolean intersection to improve retrieval effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PetriCS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/PetriCS11,
		author = {Matthias Petri and J. Shane Culpepper and Falk Scholer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/RMIT.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PetriCS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at TREC 2011 Microblog Track

_Adam Roegiest, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./microblog/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/waterloo.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/waterloo.microblog.update.pdf)
- :material-file-search: **Runs:** [waterlooa1](./microblog/runs.md#waterlooa1) | [waterlooa2](./microblog/runs.md#waterlooa2) | [waterlooa3](./microblog/runs.md#waterlooa3) | [waterlooa4](./microblog/runs.md#waterlooa4)

??? abstract "Abstract"
	
	For the first year of the Microblog Track, a real time ad hoc search task was determined to be a suitable first task. The goal of the track is to return the most recent but also relevant tweets for a user's query. Participating runs will be officially scored using precision at 30. Other experimental scoring measures will be evaluated in parallel to the official measure. As this was the first year for the Microblog Track, our primary goal was to create a baseline method and then attempt to improve upon the baseline. Since the only task was to perform a real time ad hoc search for the track, we decided that the task would be best suited by using a traditional search methodology. In doing so we used the Wumpus Search Engine1, which was developed by Stefan B¨uttcher while at the University of Waterloo.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoegiestC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoegiestC11,
		author = {Adam Roegiest and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Waterloo at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/waterloo.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoegiestC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2011 Microblog Track

_Cunhui Shi, Kejiang Ren, Hongfei Lin, Shaowu Zhang_

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./microblog/participants.md#dutir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/DUTIR.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/DUTIR.microblog.pdf)
- :material-file-search: **Runs:** [dutirLmFb](./microblog/runs.md#dutirlmfb) | [dutirMixFb](./microblog/runs.md#dutirmixfb) | [dutirTfidfFb](./microblog/runs.md#dutirtfidffb) | [dutirMixSp](./microblog/runs.md#dutirmixsp)

??? abstract "Abstract"
	
	In TREC 2011 Microblog Track, we explore the use of pseudo relevance feedback to expand original query terms in topics. Hyperlink is used to enhance the performance of the retrieval results. And we set a threshold of entropy to filter retrieval results. Microblog is a Realtime Adhoc Task, so we make use of average querytweettime that comes from pseudo relevance feedback to change retrieval score. We combine two models to improve retrieval results. The results show that our model is effective at realtime relevance retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShiRLZ11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShiRLZ11,
		author = {Cunhui Shi and Kejiang Ren and Hongfei Lin and Shaowu Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/DUTIR.microblog.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ShiRLZ11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### 10 Weeks to TREC: STIRS Siena's Twitter Information Retrieval  System

_Sharon Gower Small, Darren Lim, Karl Appel, Denis Kalic, Matthew Kemmer, David Purcell, Carl Tompkins, Chan Tran_

- :fontawesome-solid-user-group: **Participant:** [SienaCLTeam](./microblog/participants.md#sienaclteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/SienaCLTeam.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/SienaCLTeam.microblog.pdf)
- :material-file-search: **Runs:** [SienaCLbase](./microblog/runs.md#sienaclbase) | [SienaCL342](./microblog/runs.md#sienacl342) | [SienaCL31](./microblog/runs.md#sienacl31) | [SienaCL1B](./microblog/runs.md#sienacl1b)

??? abstract "Abstract"
	
	There has been an increasing interest, both of the research community and federal funding agencies in microblogs as a source of viable information for a variety of tasks. NIST (National Institute of Standards and Technology) has added a microblog retrieval track to TREC (Text REtrieval Conference) for the first time in 2011. NIST has selected Twitter as the source of microblog data. Twitter is a dynamic social website that allows users to post tweets which are short posts to share news with friends and followers across the world. While some tweets provide useful information, this information is very limited by the restriction on length to 140 characters or less. Participating teams were provided with the code necessary to download the Twitter Corpus, consisting of 16,141,812 tweets from a 2-week time period, January 24, 2011 to February 8, 2011, inclusive. Teams were also provided with a training set of 12 example topics, and later the test set of 50 topics. In this paper, we describe three modules designed for this track, built within a system called STIRS, Siena's Twitter Information Retrieval System. After submitting three user-defined runs and a Lucene baseline run, the NIST judging showed our best run to be at 30.83% precision. The reported median from all runs of all 58 participating teams was 25.9%. We also describe our process of developing a new and complete end-to-end system in just 10 weeks time with six undergraduate researchers.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmallLAKKPTT11.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmallLAKKPTT11,
		author = {Sharon Gower Small and Darren Lim and Karl Appel and Denis Kalic and Matthew Kemmer and David Purcell and Carl Tompkins and Chan Tran},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {10 Weeks to {TREC:} {STIRS} Siena's Twitter Information Retrieval System},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/SienaCLTeam.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmallLAKKPTT11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WISTUD at TREC 2011: Microblog Track: Exploiting Background Knowledge  from DBpedia and News Articles for Search on Twitter

_Ke Tao, Fabian Abel, Claudia Hauff_

- :fontawesome-solid-user-group: **Participant:** [wis_tudelft](./microblog/participants.md#wis_tudelft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/wis.tudelft.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/wis.tudelft.microblog.update.pdf)
- :material-file-search: **Runs:** [manualWISTUD](./microblog/runs.md#manualwistud) | [basicWISTUD](./microblog/runs.md#basicwistud) | [dbpWISTUD](./microblog/runs.md#dbpwistud) | [mulnewWISTUD](./microblog/runs.md#mulnewwistud)

??? abstract "Abstract"
	
	These working notes describe the system developed by the WISTUD team for the Microblog track. We evaluated the suitability of semantic technologies for the search task, in particular, query expansion with named entities that are deduced by means of a topic-based profiling process. The results indicate the feasibility of the approach: for half of the topics, at P@30, our top performing automatic method based on semantic profiling yields better results than the median over all submitted runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TaoAH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/TaoAH11,
		author = {Ke Tao and Fabian Abel and Claudia Hauff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WISTUD} at {TREC} 2011: Microblog Track: Exploiting Background Knowledge from DBpedia and News Articles for Search on Twitter},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/wis.tudelft.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TaoAH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microblog Track 2011 of FDU

_Bingqing Wang, Xuanjing Huang_

- :fontawesome-solid-user-group: **Participant:** [FDUMED](./microblog/participants.md#fdumed)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/FDUMED.microblog.pdf](http://trec.nist.gov/pubs/trec20/papers/FDUMED.microblog.pdf)
- :material-file-search: **Runs:** [FDUNLP](./microblog/runs.md#fdunlp) | [FDUNLP2](./microblog/runs.md#fdunlp2)

??? abstract "Abstract"
	
	Twitter provides huge amount of short mes-sages, raises challenge problems to the research community. The Microblog Track of TREC detects the special behavior of the twitter dataset in the 'real-time' retrieval task. This paper reports our participation in the Microblog Track task. Given the query topic-s, each participants are required to conduct a 'real-time' retrieval task, which seeks for the most recent and interesting tweets for each query topic. Our focus in this task includes t-wo aspects: (1)data preprocessing to remove non-English tweets, and (2)feature extraction for clustering the tweets into two categories. Given the huge interest in the microblog, there is lot of work to apply different linguist analysis techniques and data analysis methods to explore the behavior and special features in the Microblog sphere.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangH11,
		author = {Bingqing Wang and Xuanjing Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microblog Track 2011 of {FDU}},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/FDUMED.microblog.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring Tweets Normalization and Query Time Sensitivity for Twitter  Search

_Zhongyu Wei, Wei Gao, Lanjun Zhou, Binyang Li, Kam-Fai Wong_

- :fontawesome-solid-user-group: **Participant:** [SEEM_CUHK](./microblog/participants.md#seem_cuhk)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/SEEM_CUHK.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/SEEM_CUHK.microblog.update.pdf)
- :material-file-search: **Runs:** [WiseFouthRun](./microblog/runs.md#wisefouthrun) | [WiseThirdRun](./microblog/runs.md#wisethirdrun) | [Wise2ndRun](./microblog/runs.md#wise2ndrun) | [WiseFifthRun](./microblog/runs.md#wisefifthrun)

??? abstract "Abstract"
	
	This paper presents our work for the Realtime Adhoc Task of TREC 2011 Microblog Track. Microblog texts like tweets are generally characterized by the inclusion of a large proportion of irregular expressions, such as ill-formed words, which can lead to significant mismatch between query terms and tweets. In addition, Twitter queries are distinguished from Web queries with many unique characteristics, one of which reflects the clearly distinct temporal aspects of Twitter search behavior. In this study, we deal with the first problem by normalizing tweet texts and the second by capturing the temporal characteristics of a topic. We divided topics into two categories: time-sensitive and time-insensitive. For the time-sensitive ones, we introduce a decay factor to adjust the relevance score of results according to the expected date of the topical event to happen, and then re-rank the search results. Experiments demonstrate that our methods are significantly better than baseline and outperform the medium of all runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WeiZLWGWE11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WeiZLWGWE11,
		author = {Zhongyu Wei and Wei Gao and Lanjun Zhou and Binyang Li and Kam{-}Fai Wong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploring Tweets Normalization and Query Time Sensitivity for Twitter Search},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/SEEM\_CUHK.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WeiZLWGWE11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow (UGLA-D) at TREC Microblog 2011: Temporal  Pseudo-Relevance Feedback in Microblog Retrieval

_Stewart Whiting, Iraklis A. Klampanos, Joemon M. Jose_

- :fontawesome-solid-user-group: **Participant:** [UGLA_D](./microblog/participants.md#ugla_d)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UGLA-D.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UGLA-D.microblog.update.pdf)
- :material-file-search: **Runs:** [simfoll](./microblog/runs.md#simfoll) | [simfollTP01](./microblog/runs.md#simfolltp01) | [tfTP01](./microblog/runs.md#tftp01)

??? abstract "Abstract"
	
	This submission represents a first attempt to apply temporal pseudo-relevance feedback for the microblog context. For our submission to the TREC Microblogging 2011 track we perform two approaches, which serve as our initial bases for retrieval. Our first approach uses the retrieval facilities of a standard MySQL server on a heuristically altered tweet collection. Our second approach intends to improve on this initial retrieval through pseudo-relevance feedback, based upon the temporal profiles of n-grams extracted from the top N relevance feedback tweets. A weighted graph is used to model temporal correlation between n-grams, with a PageRank variant employed to combine both pseudo-relevant document term distribution and temporal collection evidence. Preliminary experiments with the TREC Microblogging 2011 Twitter corpus indicate that through parameter optimisation, retrieval effectiveness can be improved.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WhitingKJ11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WhitingKJ11,
		author = {Stewart Whiting and Iraklis A. Klampanos and Joemon M. Jose},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow {(UGLA-D)} at {TREC} Microblog 2011: Temporal Pseudo-Relevance Feedback in Microblog Retrieval},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UGLA-D.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WhitingKJ11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Time-Sensitive Weighting for Microblog Retrieval

_Hao Wu, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [Udel_Fang](./microblog/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Udel_Fang.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Udel_Fang.microblog.update.pdf)
- :material-file-search: **Runs:** [UDMicroIDF](./microblog/runs.md#udmicroidf) | [UDMicroIDFD](./microblog/runs.md#udmicroidfd) | [UDMicroComb1](./microblog/runs.md#udmicrocomb1) | [UDMicroComb2](./microblog/runs.md#udmicrocomb2)

??? abstract "Abstract"
	
	We report our system and experiments for the realtime Adhoc task in the 2011 MicroBlog track. Our goal is to develop effective technique to retrieve relevant tweets that have been posted recently. In particular, we propose a time sensitive term weighting strategy that can favor tweets in hot discussed time and a document length related weighting method that can favor long tweets which are more likely to be interesting. Query expansion technique is also used to further improve the retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuF11a.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuF11a,
		author = {Hao Wu and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Time-Sensitive Weighting for Microblog Retrieval},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Udel\_Fang.microblog.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuF11a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### GUCAS at TREC 2011 Microblog Track

_Xin Zhang, Kai Hui, Ben He, Tiejian Luo_

- :fontawesome-solid-user-group: **Participant:** [GUCAS](./microblog/participants.md#gucas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/GUCAS.microblog.update.pdf](http://trec.nist.gov/pubs/trec20/papers/GUCAS.microblog.update.pdf)
- :material-file-search: **Runs:** [IDEABASIC](./microblog/runs.md#ideabasic) | [IDEABASICQE](./microblog/runs.md#ideabasicqe) | [IDEAACTQE](./microblog/runs.md#ideaactqe) | [IDEABASICACT](./microblog/runs.md#ideabasicact)

??? abstract "Abstract"
	
	The aim of GUCAS's participation in the Microblog track this year is to evaluate the effectiveness of probabilistic retrieval models in combination with various sources of evidence for relevance in the context of the Twitter corpus. In our official runs, we use the PL2F field-based model as the baseline, on top of which query expansion is also applied. In addition, a supplement model combining recency, authority and URL length is developed to retrieve authoritative and timely tweets. Finally, a language filter is used to remove non-English tweets. Our experimental results show that the language filter and URL length filter can benefit the most the retrieval effectiveness. In the following-up experiments, it demonstrates that the results applying the basic models improve siginificantly after removing the retweets in the preliminary results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangHHL11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangHHL11,
		author = {Xin Zhang and Kai Hui and Ben He and Tiejian Luo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{GUCAS} at {TREC} 2011 Microblog Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/GUCAS.microblog.update.pdf},
		timestamp = {Fri, 27 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangHHL11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2011: Experiments with Terrier in  Crowdsourcing, Microblog, and Web Tracks

_Richard McCreadie, Craig Macdonald, Rodrygo L. T. Santos, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./microblog/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf](http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf)
- :material-file-search: **Runs:** [uogTrUB2](./microblog/runs.md#uogtrub2) | [uogTrLqea](./microblog/runs.md#uogtrlqea) | [uogTrLqeabdd](./microblog/runs.md#uogtrlqeabdd) | [uogTrLqeabd](./microblog/runs.md#uogtrlqeabd)

??? abstract "Abstract"
	
	In TREC 2011, we focus on tackling the new challenges proposed by the pilot Crowdsourcing and Microblog tracks, using our Terrier Information Retrieval Platform. Meanwhile, we continue to build upon our novel xQuAD framework and data-driven ranking approaches within Terrier to achieve effective and efficient ranking for the TREC Web track. In particular, the aim of our Microblog track participation is the development of a learning to rank approach for filtering within a tweet ranking environment, where tweets are ranked in reverse chronological order. In the Crowdsourcing track, we work to achieve a closer integration between the crowdsourcing marketplaces that are used for relevance assessment, and Terrier, which produces the document rankings to be assessed. Moreover, we focus on generating relevance assessments quickly and at a minimal cost. For the Web track, we enhance the data-driven learning support within Terrier by proposing a novel framework for the fast computation of document features for learning to rank.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMSO11.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMSO11,
		author = {Richard McCreadie and Craig Macdonald and Rodrygo L. T. Santos and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2011: Experiments with Terrier in Crowdsourcing, Microblog, and Web Tracks},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMSO11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Iowa at TREC 2011: Microblogs, Medical Records  and Crowdsourcing

_Sanmitra Bhattacharya, Christopher G. Harris, Yelena Mejova, Chao Yang, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [UIowaS](./microblog/participants.md#uiowas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf)
- :material-file-search: **Runs:** [UIowaS1](./microblog/runs.md#uiowas1) | [UIowaS2](./microblog/runs.md#uiowas2) | [UIowaS3](./microblog/runs.md#uiowas3) | [UIowaS4](./microblog/runs.md#uiowas4)

??? abstract "Abstract"
	
	The Text Retrieval and Text Mining group at the University of Iowa participated in three tracks, all new tracks introduced this year: Microblog, Medical Records (Med) and Crowdsourcing. Details of our strategies are provided in this paper. Overall our effort has been fruitful in that we have been able to understand more about the nature of medical records and Twitter messages, and also the merits and challenges of working with games as a framework for gathering relevance judgments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bhattacharya0MYS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bhattacharya0MYS11,
		author = {Sanmitra Bhattacharya and Christopher G. Harris and Yelena Mejova and Chao Yang and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Iowa at {TREC} 2011: Microblogs, Medical Records and Crowdsourcing},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bhattacharya0MYS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Web 

#### Overview of the TREC 2011 Web Track

_Charles L. A. Clarke, Nick Craswell, Ian Soboroff, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/WEB.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec20/papers/WEB.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Web Track explores and evaluates Web retrieval technology over large collections of Web data. In its current incarnation, the Web Track has been active since TREC 2009, where it included both a traditional adhoc retrieval task and a new diversity task [4]. The goal of this diversity task is to return a ranked list of pages that together provide complete coverage for a query, while avoiding excessive redundancy in the result list. For TREC 2010 the track introduced a new Web spam task and Web-style, six-level relevance assessment for the adhoc task [5]. For TREC 2011, as recommended by participants at the track planning session held during TREC 2010, we dropped the spam task but continued the other tasks essentially unchanged. As we did for TREC 2009 and TREC 2010, we based our TREC 2011 experiments on the billion-page ClueWeb091 collection created by the Language Technologies Institute at Carnegie Mellon University. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeCSV11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeCSV11,
		author = {Charles L. A. Clarke and Nick Craswell and Ian Soboroff and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2011 Web Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/WEB.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeCSV11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ranking Web Pages Using Collective Knowledge

_Falah Hassan Al-akashi, Diana Inkpen_

- :fontawesome-solid-user-group: **Participant:** [uottawa](./web/participants.md#uottawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uottawa.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/uottawa.web.update.pdf)
- :material-file-search: **Runs:** [DFalah11](./web/runs.md#dfalah11)

??? abstract "Abstract"
	
	Indexing is a crucial technique for dealing with the massive amount of data present on the web. Indexing can be performed based on words or on phrases. Our approach aims to efficiently index web documents by employing a hybrid technique in which web documents are indexed in such a way that knowledge available in the Wikipedia and in meta-content is efficiently used. Our preliminary experiments on the TREC dataset have shown that our indexing scheme is a robust and efficient method for both indexing and for retrieving relevant web pages. We ranked term queries in different ways, depending if they were found in Wikipedia pages or not. This paper presents our preliminary algorithm and experiments for the ad-hoc and diversity tasks of the TREC 2011 Web track. We ran our system on the subset B (50 million web documents) from the ClueWeb09 dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Al-akashiI11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Al-akashiI11,
		author = {Falah Hassan Al{-}akashi and Diana Inkpen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Ranking Web Pages Using Collective Knowledge},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uottawa.web.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Al-akashiI11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Research at TREC 2011 Web Track

_Bodo Billerbeck, Nick Craswell, Dennis Fetterly, Marc Najork_

- :fontawesome-solid-user-group: **Participant:** [msrsv](./web/participants.md#msrsv)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/msrsv.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/msrsv.web.update.pdf)
- :material-file-search: **Runs:** [msrsv2011a1](./web/runs.md#msrsv2011a1) | [msrsv2011a2](./web/runs.md#msrsv2011a2) | [msrsv2011a3](./web/runs.md#msrsv2011a3) | [msrsv2011d1](./web/runs.md#msrsv2011d1) | [msrsv2011d2](./web/runs.md#msrsv2011d2) | [msrsv2011d3](./web/runs.md#msrsv2011d3)

??? abstract "Abstract"
	
	This paper describes our entry into the TREC 2011 Web track. We extracted and ranked results from the ClueWeb09 corpus using a parallel processing pipeline that avoids the generation of an inverted file. We describe the components of the parallel architecture and the pipeline, how we ran the TREC experiments, and we present effectiveness results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BillerbeckCFN11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BillerbeckCFN11,
		author = {Bodo Billerbeck and Nick Craswell and Dennis Fetterly and Marc Najork},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Research at {TREC} 2011 Web Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/msrsv.web.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BillerbeckCFN11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluating Learning-to-Rank Methods in the Web Track Adhoc Task

_Leonid Boytsov, Anna Belova_

- :fontawesome-solid-user-group: **Participant:** [srchvrs](./web/participants.md#srchvrs)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/srchvrs.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/srchvrs.web.update.pdf)
- :material-file-search: **Runs:** [srchvrs11b](./web/runs.md#srchvrs11b) | [srchvrs11o](./web/runs.md#srchvrs11o)

??? abstract "Abstract"
	
	Learning-to-rank methods are becoming ubiquitous in information retrieval. Their advantage lies in the ability to combine a large number of low-impact relevance signals. This requires large training and test data sets. A large test data set is also needed to verify the usefulness of specific relevance signals (using statistical methods). There are several publicly available data collections geared towards evaluation of learning-to-rank methods. These collections are large, but they typically provide a fixed set of precomputed (and often anonymized) relevance signals. In turn, computing new signals may be impossible. This limitation motivated us to experiment with learning-to-rank methods using the TREC Web adhoc collection. Specifically, we compared performance of learning-to-rank methods with performance of a hand-tuned formula (based on the same set of relevance signals). Even though the TREC data set did not have enough queries to draw definitive conclusions, the hand-tuned formula seemed to be at par with learning-to-rank methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoytsovB11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoytsovB11,
		author = {Leonid Boytsov and Anna Belova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Evaluating Learning-to-Rank Methods in the Web Track Adhoc Task},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/srchvrs.web.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoytsovB11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LIA at TREC 2011 Web Track: Experiments on the Combination of  Online Resources

_Romain Deveaud, Eric SanJuan, Patrice Bellot_

- :fontawesome-solid-user-group: **Participant:** [LIA](./web/participants.md#lia)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/LIA.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/LIA.web.update.pdf)
- :material-file-search: **Runs:** [liaQEWikiGoo](./web/runs.md#liaqewikigoo) | [liaQEWikiGoA](./web/runs.md#liaqewikigoa) | [liaQEWikiA](./web/runs.md#liaqewikia) | [liaQEWikiAnA](./web/runs.md#liaqewikiana)

??? abstract "Abstract"
	
	In this paper, we report the experiments we conducted for our participation to the TREC 2011 Web Track. The experiments we conducted this year aim at discovering how the combination of specific external resources in a language modeling fashion can help web search. We use Wikipedia and Google as external resources for different search contexts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DeveaudSB11.bib) "
	```
	@inproceedings{DBLP:conf/trec/DeveaudSB11,
		author = {Romain Deveaud and Eric SanJuan and Patrice Bellot},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{LIA} at {TREC} 2011 Web Track: Experiments on the Combination of Online Resources},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/LIA.web.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DeveaudSB11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI at TREC 2011: Session, Web, and Medical

_Jiyin He, Vera Hollink, Corrado Boscarino, Arjen P. de Vries, Roberto Cornacchia_

- :fontawesome-solid-user-group: **Participant:** [CWI](./web/participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/CWI.session.web.medical.pdf](http://trec.nist.gov/pubs/trec20/papers/CWI.session.web.medical.pdf)
- :material-file-search: **Runs:** [CWIcIAt5b1](./web/runs.md#cwiciat5b1) | [CWIIAt5b5](./web/runs.md#cwiiat5b5) | [CWIcIA2t5b1](./web/runs.md#cwicia2t5b1)

??? abstract "Abstract"
	
	We report on the participation of the Interactive Information Access group of the CWI Amsterdam in the web, session, and medical track at TREC 2011. In the web track we focus on the diversity task. We find that cluster-based subtopic modeling approaches improve diversification performance compared to a non-cluster-based subtopic modeling approach. While gain was observed on previous years' topic sets, diversification with the proposed approaches hurt the performance when compared to a non-diversified baseline run on this year's topic set. In the session track, we examine the effects of differentiating between 'good' and 'bad' users. We find that differentiation is useful as the use of search history appears to be mainly effective when the search is not going well. However, our current strategy is not effective for 'good' users. In addition, we studied the use of random walks on query graphs for formulating session history as search queries, but results are inconclusive. In the medical track, we found that the use of medical background resources for query expansion leads to small improvements in retrieval performance. Such resources appear to be especially useful to promote early precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeHBVC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeHBVC11,
		author = {Jiyin He and Vera Hollink and Corrado Boscarino and Arjen P. de Vries and Roberto Cornacchia},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CWI} at {TREC} 2011: Session, Web, and Medical},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/CWI.session.web.medical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeHBVC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Reducing Redundancy with Anchor Text and Spam Priors

_Marijn Koolen, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./web/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uamsterdam.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/uamsterdam.web.update.pdf)
- :material-file-search: **Runs:** [UAmsAnc05LS](./web/runs.md#uamsanc05ls) | [UAmsM705tiLS](./web/runs.md#uamsm705tils) | [UAmsM7DirExS](./web/runs.md#uamsm7direxs) | [UAmsM705FLS](./web/runs.md#uamsm705fls) | [UAmsT05FLS](./web/runs.md#uamst05fls) | [UAmsM705tFLS](./web/runs.md#uamsm705tfls)

??? abstract "Abstract"
	
	In this paper, we document our efforts in participating to the TREC 2011 Web Tracks. We had multiple aims: This year, tougher topics were selected for the Web Track, for which there is less popularity information available. We look at the relative value of anchor text for these less popular topics, and at impact of spam priors. Full-text retrieval on the ClueWeb09 B collection suffers from text spam, especially in the top 5 ranks. The spam prior largely reduces the impact of spam, leading to a boost in precision. We find that, in contrast to the more common queries of last year, anchor text does improve ad hoc retrieval performance of a full-text baseline for less common queries. However, for diversity, mixing anchor text and full-text leads to an improvement. Closer analysis reveals that mixing anchor text and full-text, fewer relevant nuggets are retrieved which cover more subtopics. Anchor text is an effective way of reducing redundancy and increasing coverage of subtopics at the same time.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoolenK11.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoolenK11,
		author = {Marijn Koolen and Jaap Kamps},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Reducing Redundancy with Anchor Text and Spam Priors},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uamsterdam.web.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KoolenK11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCD SIFT in the TREC 2011 Web Track

_David Leonard, Doychin Doychev, David Lillis, Fergus Toolan, Rem W. Collier, John Dunnion_

- :fontawesome-solid-user-group: **Participant:** [UCDSIFT](./web/participants.md#ucdsift)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/SIFT_UCD.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/SIFT_UCD.web.update.pdf)
- :material-file-search: **Runs:** [2011SiftR1](./web/runs.md#2011siftr1) | [2011SiftR2](./web/runs.md#2011siftr2) | [2011SiftR3](./web/runs.md#2011siftr3)

??? abstract "Abstract"
	
	The SIFT (Segmented Information Fusion Techniques) group in UCD is dedicated to researching Data Fusion in Information Retrieval. This area of research involves the merging of multiple sets of results into a single result set that is presented to the user. As a means of both evaluating the effectiveness of this work and comparing it against other retrieval systems, the group entered Category B of the TREC 2011 Web Track. This involved the use of freely-available Information Retrieval tools to provide inputs to the data fusion process. This paper outlines the strategies of the 3 candidate entries submitted to compete in the ad-hoc task, discusses the methodology employed by them and presents a preliminary analysis of the results issued by TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeonardDLTCD11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeonardDLTCD11,
		author = {David Leonard and Doychin Doychev and David Lillis and Fergus Toolan and Rem W. Collier and John Dunnion},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCD} {SIFT} in the {TREC} 2011 Web Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/SIFT\_UCD.web.update.pdf},
		timestamp = {Thu, 11 Aug 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LeonardDLTCD11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2011 Ad-Hoc Track

_Heyuan Li, Yuanhai Xue, Xu Chen, Xiaoming Yu, Feng Guan, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./web/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ICTNET.web-adhoc.pdf](http://trec.nist.gov/pubs/trec20/papers/ICTNET.web-adhoc.pdf)
- :material-file-search: **Runs:** [ICTNET11ADR2](./web/runs.md#ictnet11adr2) | [ICTNET11DVR1](./web/runs.md#ictnet11dvr1) | [ICTNET11DVR2](./web/runs.md#ictnet11dvr2) | [ICTNET11ADR3](./web/runs.md#ictnet11adr3) | [ICTNET11DVR3](./web/runs.md#ictnet11dvr3) | [ICTNET11ADR4](./web/runs.md#ictnet11adr4)

??? abstract "Abstract"
	
	An ad-hoc task in TREC investigates the performance of systems that search a static set of documents using previously-unseen topics. This year, ClueWeb09 Dataset [1] was used again as document collection. But the topics developed for this year was less common and ambiguous than before. The rest of this paper is organized as follows. In Section 2, we discuss the processing of ClueWeb09, derived data and external resources. In Section 3, the BM25 model with term proximity, searching with anchor text, query expansion and promoting authoritative sites are introduced. We report experimental results in Section 4 and conclude our work in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiXCYGLC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiXCYGLC11,
		author = {Heyuan Li and Yuanhai Xue and Xu Chen and Xiaoming Yu and Feng Guan and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2011 Ad-Hoc Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ICTNET.web-adhoc.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiXCYGLC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2011: Experiments with Terrier in  Crowdsourcing, Microblog, and Web Tracks

_Richard McCreadie, Craig Macdonald, Rodrygo L. T. Santos, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./web/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf](http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf)
- :material-file-search: **Runs:** [uogTrA45Vm](./web/runs.md#uogtra45vm) | [uogTrA45Nm](./web/runs.md#uogtra45nm) | [uogTrB47Vm](./web/runs.md#uogtrb47vm) | [uogTrA45Vmx](./web/runs.md#uogtra45vmx) | [uogTrA45Nmx2](./web/runs.md#uogtra45nmx2) | [uogTrB47Vmx](./web/runs.md#uogtrb47vmx)

??? abstract "Abstract"
	
	In TREC 2011, we focus on tackling the new challenges proposed by the pilot Crowdsourcing and Microblog tracks, using our Terrier Information Retrieval Platform. Meanwhile, we continue to build upon our novel xQuAD framework and data-driven ranking approaches within Terrier to achieve effective and efficient ranking for the TREC Web track. In particular, the aim of our Microblog track participation is the development of a learning to rank approach for filtering within a tweet ranking environment, where tweets are ranked in reverse chronological order. In the Crowdsourcing track, we work to achieve a closer integration between the crowdsourcing marketplaces that are used for relevance assessment, and Terrier, which produces the document rankings to be assessed. Moreover, we focus on generating relevance assessments quickly and at a minimal cost. For the Web track, we enhance the data-driven learning support within Terrier by proposing a novel framework for the fast computation of document features for learning to rank.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMSO11.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMSO11,
		author = {Richard McCreadie and Craig Macdonald and Rodrygo L. T. Santos and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2011: Experiments with Terrier in Crowdsourcing, Microblog, and Web Tracks},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMSO11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Web Track 2011 Diversity Track

_Shengxian Wan, Yuanhai Xue, Xiaoming Yu, Feng Guan, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./web/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ICTNET.web-diversity.pdf](http://trec.nist.gov/pubs/trec20/papers/ICTNET.web-diversity.pdf)
- :material-file-search: **Runs:** [ICTNET11ADR2](./web/runs.md#ictnet11adr2) | [ICTNET11DVR1](./web/runs.md#ictnet11dvr1) | [ICTNET11DVR2](./web/runs.md#ictnet11dvr2) | [ICTNET11ADR3](./web/runs.md#ictnet11adr3) | [ICTNET11DVR3](./web/runs.md#ictnet11dvr3) | [ICTNET11ADR4](./web/runs.md#ictnet11adr4)

??? abstract "Abstract"
	
	Traditional IR systems use document-query relevance as the main measure for ranking and consider the relevance is independent of the other documents. However, the only measure of relevance cannot deal with redundant information and can fail to reflect the broad range of user needs that can underlie a query. IR systems need to consider the diversity and novelty of the result list. Diversity task is trying to solve this problem. The goal of diversity task is to return a ranked list of pages that together provide complete coverage for a query, while avoiding excessive redundancy in the result list. This year, the primary evaluation measure is intent aware expected reciprocal rank (ERR-IA) [1], some other evaluation measures such as α-nDCG [1] have also been evaluated. This paper is organized as follows. Section 2 describes different clustering methods used for text clustering. Section 3 describes our query expansion method. Section 4 describes the diversity model used for re-ranking. Section 5 analyzes the result and in section 6 we conclude our work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WanXYGLC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WanXYGLC11,
		author = {Shengxian Wan and Yuanhai Xue and Xiaoming Yu and Feng Guan and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Web Track 2011 Diversity Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ICTNET.web-diversity.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WanXYGLC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Study of Pattern-Based Suptopic Discovery and Integration in the  Web Track

_Wei Zheng, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [Udel_Fang](./web/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Udel_Fang.web.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Udel_Fang.web.update.pdf)
- :material-file-search: **Runs:** [UDPattern](./web/runs.md#udpattern) | [UDCombine1](./web/runs.md#udcombine1) | [UDCombine2](./web/runs.md#udcombine2)

??? abstract "Abstract"
	
	We report our systems and experiments in the diversity task of TREC 2011 Web track. Our goal is to evaluate the effectiveness of the proposed methods for subtopic extraction and diversification steps on the large data collection. In the subtopic extraction step, we extract subtopics using both structured data, i.e., ODP, which provides high quality information and unstructured data, i.e., original retrieved documents, which contains terms effective in diversifying documents. In the diversification step, we use a coverage-based method to diversify documents based on the extracted subtopics. It has the desired properties of diversification which favors documents covering more subtopics and documents covering novel subtopics that have not been well covered by previously selected documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengF11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengF11,
		author = {Wei Zheng and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Study of Pattern-Based Suptopic Discovery and Integration in the Web Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Udel\_Fang.web.update.pdf},
		timestamp = {Tue, 20 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengF11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Legal 

#### Overview of the TREC 2011 Legal Track

_Maura R. Grossman, Gordon V. Cormack, Bruce Hedin, Douglas W. Oard_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/LEGAL.OVERVIEW.2011.pdf](http://trec.nist.gov/pubs/trec20/papers/LEGAL.OVERVIEW.2011.pdf)
??? abstract "Abstract"
	
	The TREC 2011 Legal Track consisted of a single task: the learning task, which captured elements of both the TREC 2010 learning and interactive tasks. Participants were required to rank the entire corpus of 685,592 documents by their estimate of the probability of responsiveness to each of three topics, and also to provide a quantitative estimate of that probability. Participants were permitted to request up to 1,000 responsiveness determinations from a Topic Authority for each topic. Participants elected either to use only these responsiveness determinations in preparing automatic submissions, or to augment these determinations with their own manual review in preparing technology-assisted submissions. We provide an overview of the task and a summary of the results. More detailed results are available in the Appendix to the TREC 2011 Proceedings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanCHO11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanCHO11,
		author = {Maura R. Grossman and Gordon V. Cormack and Bruce Hedin and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2011 Legal Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/LEGAL.OVERVIEW.2011.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanCHO11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Auto-Relevancy and Responsiveness Baseline II Improving Concept  Search to Establish a Subset with Maximized Recall for Automated First  Pass and Early Assessment Using Latent Semantic Indexing [LSI], Bigrams  and WordNet 3.0 Seeding

_Cody Bennett_

- :fontawesome-solid-user-group: **Participant:** [TCDI](./legal/participants.md#tcdi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/TCDI.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/TCDI.legal.update.pdf)
- :material-file-search: **Runs:** [tcdicskwA1](./legal/runs.md#tcdicskwa1) | [tcdilentA2](./legal/runs.md#tcdilenta2) | [tcdihentA3](./legal/runs.md#tcdihenta3) | [tcdinokaAF](./legal/runs.md#tcdinokaaf)

??? abstract "Abstract"
	
	We experiment with manipulating the features at build time by indexing bigrams created from EDRM data and seeding the LSI index with thesaurus-like WordNet 3.0 strata. From experimentation, this produces fewer false positives and a smaller, more focused relevant set. The method allows concept searching using bigrams and WordNet senses in addition to singular terms increasing polysemous value and precision; steps towards a unification of Semantic and Statistical. Also, because of LSI and WordNet senses, WSD appears enhanced. We then apply an automated method for selecting search criteria, query expansion and concept searching from Reviewer Guidelines and the original Request for Production thereby returning a search result with scores across the Enron corpus for each topic. The result of the normalized cosine distance score for each document in each topic is then shifted based on the foundation of primes, golden standard, and golden ratio. This results in 'best cutoff' using naturally occurring patterns in probability of expected relevancy with limit approaching .5. Submissions A1, A2, A3, and AF include similar combinations of the above. Although we did not submit a mopup run, we analyzed the mopups for post assessment. For each of the three topics, there were documents which TAs selected as relevant in contention with their other personal assessments. The defect percentage and potential impact to a semi/automated system will also be examined. Overall the influence of humans involved (TAs) was very minimal, as their assessments were not allowed to modify any rank or probability of documents. However, the identification of relevant documents by TAs at low LSI thresholds provided a feedback loop to affect the natural cutoff. Cutoffs for A1, A2, A3 were nearly -.04 (Landau) against the Golden and Poisson means and F was nearly +.04 (Apéry). Since more work is required to decrease false positives, it is encouraging to find a natural relevancy cutoff that maximizes probable Recall of Responsiveness across differing topics. Automated concept search using a mechanically generated semantically derived feature set upon indexed bigram and WordNet sense terms in an LSI framework reduces false positives and produces a tighter cluster of potentially responsive documents. Further, since legal Productions are essentially binary (R/NR), work was done to argue for scoring supporting this view. Obtaining Recall =>90% and Precision =>90% with a high degree of success is a two step process1, of which we test and discuss the first (maximization of Recall) for this study. Therefore, our focus will be heavily skewed on the probability of attaining high Recall for the creation of a subset of the corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bennett11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bennett11,
		author = {Cody Bennett},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Auto-Relevancy and Responsiveness Baseline {II} Improving Concept Search to Establish a Subset with Maximized Recall for Automated First Pass and Early Assessment Using Latent Semantic Indexing [LSI], Bigrams and WordNet 3.0 Seeding},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/TCDI.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bennett11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Latent Semantic Indexing with selective Query Expansion

_Andy Garron, April Kontostathis_

- :fontawesome-solid-user-group: **Participant:** [URSINUS](./legal/participants.md#ursinus)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Ursinus.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Ursinus.legal.update.pdf)
- :material-file-search: **Runs:** [URS205A1](./legal/runs.md#urs205a1) | [URS222A2](./legal/runs.md#urs222a2) | [URS403A2](./legal/runs.md#urs403a2) | [URS205A3](./legal/runs.md#urs205a3) | [URS205AM](./legal/runs.md#urs205am)

??? abstract "Abstract"
	
	This article describes our experiments during participation in the Legal Track of the 2011 Text REtrieval Conference. We incorporated machine learning, via selective query expansion, into our existing EDLSI system. We also were able to expand the number of dimensions used within our EDLSI system. Our results show that EDLSI is an effective technique for E-Discovery. We also have shown that selective query expansion can be a useful mechanism for improving retrieval results when a specific initial query is provided. We believe that queries that are stated in general terms, however, may suffer from “expansion in the wrong direction” when certain iterative approaches to incorporating relevance feedback information are incorporated into the search process.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GarronK11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GarronK11,
		author = {Andy Garron and April Kontostathis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Latent Semantic Indexing with selective Query Expansion},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Ursinus.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GarronK11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cluster-Based Relevance Feedback: Legal Track 2011

_Kripabandhu Ghosh, Swapan K. Parui, Prasenjit Majumder_

- :fontawesome-solid-user-group: **Participant:** [IRISCAL](./legal/participants.md#iriscal)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/IRISCAL.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/IRISCAL.legal.update.pdf)

??? abstract "Abstract"
	
	This is our second participation in the TREC Legal Track. The TREC Legal Track 2011 featured only the Learning Task. We participated in Topics 401 and 403. We used Lemur 4.111 for Boolean retrieval and followed it with a clustering technique, where we chose members from each cluster (which we called seeds) for relevance judgement by the TA and assumed all other members of the cluster whose seeds are assessed as relevant to be relevant. Based on the relevance information from seeds and their clusters, we applied Rocchio relevance feedback technique implemented in Terrier 3.02. Then, we used the feedback terms for the expansion of both the text queries and the Boolean queries. Finally, we used Z-fusion[4], a data fusion technique, on two of our runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GhoshPM11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GhoshPM11,
		author = {Kripabandhu Ghosh and Swapan K. Parui and Prasenjit Majumder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Cluster-Based Relevance Feedback: Legal Track 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/IRISCAL.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GhoshPM11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Modeling Concept and Context to Improve Performance in eDiscovery

_Harvey S. Hyman, Warren Fridy III_

- :fontawesome-solid-user-group: **Participant:** [USF_ISDS](./legal/participants.md#usf_isds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/USF-ISDS.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/USF-ISDS.legal.update.pdf)
- :material-file-search: **Runs:** [USFEOLT](./legal/runs.md#usfeolt) | [USFDSET](./legal/runs.md#usfdset) | [USFMOPT](./legal/runs.md#usfmopt)

??? abstract "Abstract"
	
	One condition of eDiscovery making it unique from other, more routine forms of IR is that all documents retrieved are settled by human inspection. Automated IR tools are used to reduce the size of a corpus search space to produce smaller sets of documents to be reviewed. However, a limitation associated with automated tools is they mainly employ statistical use of search terms that can result in poor performance when measured by recall and precision. One reason for this limitation is that relevance -- the quality of matching a document to user criteria - - is dynamic and fluid, whereas a query -- representing the translation of a user's IR goal - is fixed. This paper reports on a design approach to eDiscovey that combines concept and context modeling to enhance search term performance. We apply this approach to the TREC 2011 Legal Track Problem Set #401. Our goal is to improve performance in eDiscovery IR results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HymanF11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HymanF11,
		author = {Harvey S. Hyman and Warren Fridy III},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Modeling Concept and Context to Improve Performance in eDiscovery},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/USF-ISDS.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HymanF11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Heliod at TREC Legal 2011: Learning to Rank from Relevance Feedback  for e-Discovery

_Peter Lubell-Doughtie, Kenneth Hamilton_

- :fontawesome-solid-user-group: **Participant:** [dioileh](./legal/participants.md#dioileh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/dioileh.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/dioileh.legal.update.pdf)
- :material-file-search: **Runs:** [HELqlaA1](./legal/runs.md#helqlaa1) | [HELclrAM](./legal/runs.md#helclram) | [HELq20rAM](./legal/runs.md#helq20ram)

??? abstract "Abstract"
	
	We present the results of applying a learning to rank algorithm to the 2011 TREC Legal dataset. The learning to rank algorithm we use was designed to maximize NDCG, MAP, and AUC scores. We therefore examine our results using the AUC and hypothetical F1 scores. We find query expansion and learning to rank improve scores beyond standard language model retrieval, however learning to rank does not outperform query expansion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lubell-DoughtieH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lubell-DoughtieH11,
		author = {Peter Lubell{-}Doughtie and Kenneth Hamilton},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Heliod at {TREC} Legal 2011: Learning to Rank from Relevance Feedback for e-Discovery},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/dioileh.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lubell-DoughtieH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Learning Task Experiments in the TREC 2011 Legal Track

_Stephen Tomlinson_

- :fontawesome-solid-user-group: **Participant:** [ot](./legal/participants.md#ot)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/OpenText.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/OpenText.legal.update.pdf)
- :material-file-search: **Runs:** [otL11BT1](./legal/runs.md#otl11bt1) | [otL11FT1](./legal/runs.md#otl11ft1) | [otL11FT2](./legal/runs.md#otl11ft2) | [otL11BT2](./legal/runs.md#otl11bt2) | [otL11HT1](./legal/runs.md#otl11ht1) | [otL11HT2](./legal/runs.md#otl11ht2) | [otL11FTM](./legal/runs.md#otl11ftm) | [otL11BTM](./legal/runs.md#otl11btm) | [otL11HTM](./legal/runs.md#otl11htm)

??? abstract "Abstract"
	
	The Learning Task of the TREC 2011 Legal Track investigated the effectiveness of e-Discovery search techniques at selecting training examples and learning from them to estimate the probability of relevance of every document in a collection. The task specified 3 test topics, each of which included a one-sentence request for documents to produce from a target collection of 685,592 e-mail messages and attachments. In this paper, we describe the experimental approaches used and report the scores that each achieved.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tomlinson11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tomlinson11,
		author = {Stephen Tomlinson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Learning Task Experiments in the {TREC} 2011 Legal Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/OpenText.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tomlinson11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at TREC 2011: A Social Networking Approach  to the Legal Learning Track

_Robert Warren_

- :fontawesome-solid-user-group: **Participant:** [waterloo](./legal/participants.md#waterloo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/waterloo.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/waterloo.legal.update.pdf)
- :material-file-search: **Runs:** [UWABASA1](./legal/runs.md#uwabasa1) | [UWABASA2](./legal/runs.md#uwabasa2) | [UWABASA3](./legal/runs.md#uwabasa3) | [UWABASA4](./legal/runs.md#uwabasa4) | [UWASNAA1](./legal/runs.md#uwasnaa1) | [UWASNAA2](./legal/runs.md#uwasnaa2) | [UWASNAA4](./legal/runs.md#uwasnaa4) | [UWASNAA3](./legal/runs.md#uwasnaa3) | [UWASNAAF](./legal/runs.md#uwasnaaf) | [UWALINAF](./legal/runs.md#uwalinaf) | [UWABASAF](./legal/runs.md#uwabasaf) | [UWALINA2](./legal/runs.md#uwalina2) | [UWALINA4](./legal/runs.md#uwalina4) | [UWALINA3](./legal/runs.md#uwalina3) | [UWABASAM](./legal/runs.md#uwabasam) | [UWASNAAM](./legal/runs.md#uwasnaam) | [UWALINAM](./legal/runs.md#uwalinam)

??? abstract "Abstract"
	
	This paper reports on the University of Waterloo experience with the Legal Learning track where three different methods were used to approach the retrieval task. Two are based on previously used methods and the last is a novel method based on modifying the responsiveness probability using social network analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Warren11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Warren11,
		author = {Robert Warren},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Waterloo at {TREC} 2011: {A} Social Networking Approach to the Legal Learning Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/waterloo.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Warren11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Melboune at the TREC 2011 Legal Track

_William Webber, Phil Farrelly_

- :fontawesome-solid-user-group: **Participant:** [unimelb_plus](./legal/participants.md#unimelb_plus)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/unimelb_plus.legal.pdf](http://trec.nist.gov/pubs/trec20/papers/unimelb_plus.legal.pdf)
- :material-file-search: **Runs:** [mlbclsA1](./legal/runs.md#mlbclsa1) | [mlbclsAF](./legal/runs.md#mlbclsaf) | [mlblrnTF](./legal/runs.md#mlblrntf) | [mlblrnTM](./legal/runs.md#mlblrntm)

??? abstract "Abstract"
	
	The Melbourne team was a collaboration of the University of Melbourne, RMIT University, and the Victorian Society for Computers and the Law. The approach taken was to train a support vector machine based upon textual features using active learning. Two sources of relevance annotations were used for different runs: the official annotations, provided by the topic authorities; and annotations provided by a member of the Melbourne team with e-discovery experience (though not legal training). We describe the SVM method used in Section 1.1, the run using official annotations in Section 1.2, and the run using the internal annotations in Section 1.3.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WebberF11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WebberF11,
		author = {William Webber and Phil Farrelly},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Melboune at the {TREC} 2011 Legal Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/unimelb\_plus.legal.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WebberF11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Recommind at TREC 2011 Legal Track

_Peter Zeinoun, Aaron Laliberte, Jan Puzicha, Howard Sklar, Craig Carpenter_

- :fontawesome-solid-user-group: **Participant:** [Recommind](./legal/participants.md#recommind)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Recommind.legal.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Recommind.legal.update.pdf)
- :material-file-search: **Runs:** [recommind03T](./legal/runs.md#recommind03t) | [recommind04T](./legal/runs.md#recommind04t)

??? abstract "Abstract"
	
	The TREC 2011 Legal Track Learning Task (the '2011 Task') evaluated each of approximately 685,000 documents from the Enron data set for responsiveness to one or more requests for production. The 2011 Task included three new requests for production (the 'Topics' and each a 'Topic')). In this paper, we describe the approaches used to conduct the review by the Recommind team and report the scores for each of the three Topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZeinounLPSC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZeinounLPSC11,
		author = {Peter Zeinoun and Aaron Laliberte and Jan Puzicha and Howard Sklar and Craig Carpenter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Recommind at {TREC} 2011 Legal Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Recommind.legal.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZeinounLPSC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2011 Legal Track Discovery Based on Relevant Feedback

_Jiayue Zhang, Wenyi Yang, Xi Wang, Lihua Wu, Yongtian Zhang, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./legal/participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/PRIS.legal.pdf](http://trec.nist.gov/pubs/trec20/papers/PRIS.legal.pdf)
- :material-file-search: **Runs:** [priindA1](./legal/runs.md#priinda1) | [priindA2](./legal/runs.md#priinda2)

??? abstract "Abstract"
	
	In order to finish the task of TREC 2011 Legal Track, this paper puts forward an experiment method, which combines indri and relevant feedback to evaluate the probability of relevance of every document in a collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangYWWZXCG11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangYWWZXCG11,
		author = {Jiayue Zhang and Wenyi Yang and Xi Wang and Lihua Wu and Yongtian Zhang and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2011 Legal Track Discovery Based on Relevant Feedback},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/PRIS.legal.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangYWWZXCG11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Chemical 

#### Overview of the TREC 2011 Chemical IR Track

_Mihai Lupu, Jiashu Zhao, Jimmy X. Huang, Harsha Gurulingappa, Juliane Fluck, Marc Zimmermann, Igor V. Filippov, John Tait_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/CHEM.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec20/papers/CHEM.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The third year of the Chemical IR evaluation track benefitted from the support of many more people interested in the domain, as shown by the number of co-authors of this overview paper. We continued the two tasks we had before, and introduced a new task focused on chemical image recognition. The objective is to gradually move towards systems really useful to the practitioners, and in chemistry, this involves both text and images. The track had a total of 9 groups participating, submitting a total of 36 runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LupuZHGFZFT11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LupuZHGFZFT11,
		author = {Mihai Lupu and Jiashu Zhao and Jimmy X. Huang and Harsha Gurulingappa and Juliane Fluck and Marc Zimmermann and Igor V. Filippov and John Tait},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2011 Chemical {IR} Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/CHEM.OVERVIEW.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LupuZHGFZFT11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Optical Structure Recognition Application Entry in Image2Structure  Task

_Igor V. Filippov, Dmitry Katsubo, Marc C. Nicklaus_

- :fontawesome-solid-user-group: **Participant:** [SAIC_Frederick](./chemical/participants.md#saic_frederick)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/saic-frederick.chem.pdf](http://trec.nist.gov/pubs/trec20/papers/saic-frederick.chem.pdf)
- :material-file-search: **Runs:** [osra_1.3.8_r300](./chemical/runs.md#osra_1.3.8_r300) | [osra_1.3.8_def](./chemical/runs.md#osra_1.3.8_def)

??? abstract "Abstract"
	
	We present Optical Structure Recognition Application (OSRA) as an entry into Image2Structure task of TREC-CHEM. OSRA is an open source utility to convert images of chemical structures to connection tables in an established computerized molecular format. There exists a large body of chemical information which has remained largely inaccessible to machine data mining techniques so far. One of the most common ways of describing a chemical structure in a journal publication or a patent document is by drawing a two-dimensional structure diagram which represents atoms and bonds of the molecule in a human-recognizable form. While easily interpreted by a human expert, such drawings are by themselves unsuitable for use in a computer database for applications such as virtual screening and computer aided drug development. OSRA allows recognition and conversion of such drawings into computer formats widely used by the chemoinformatics community.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FilippovKN11.bib) "
	```
	@inproceedings{DBLP:conf/trec/FilippovKN11,
		author = {Igor V. Filippov and Dmitry Katsubo and Marc C. Nicklaus},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Optical Structure Recognition Application Entry in Image2Structure Task},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/saic-frederick.chem.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FilippovKN11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BiTeM Group Report for TREC Chemical IR Track 2011

_Julien Gobeill, Arnaud Gaudinat, Patrick Ruch, Emilie Pasche, Douglas Teodoro, Dina Vishnyakova_

- :fontawesome-solid-user-group: **Participant:** [BiTeM](./chemical/participants.md#bitem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/BiTeM.chem.pdf](http://trec.nist.gov/pubs/trec20/papers/BiTeM.chem.pdf)
- :material-file-search: **Runs:** [BiTeMtext](./chemical/runs.md#bitemtext) | [BiTeMmesh](./chemical/runs.md#bitemmesh) | [BiTeMboth](./chemical/runs.md#bitemboth) | [BiTeMPAmesh](./chemical/runs.md#bitempamesh) | [BiTeMPAtext](./chemical/runs.md#bitempatext) | [BiTeMPAcomb](./chemical/runs.md#bitempacomb) | [BiTeMPAcitFB](./chemical/runs.md#bitempacitfb)

??? abstract "Abstract"
	
	For the third year, the BiTeM group participated in the TREC Chemical IR Track. For this campaign, we applied strategies that already showed their effectiveness, as the Citations Feedback, which takes benefit from the citations of the retrieved documents in order to re-arrange the ranking. But we also investigated a new inter-lingua model built with chemical annotations with concepts that we automatically mapped into documents. We used the MeSH controlled vocabulary for this purpose. For the Technology Survey task, the fusion of the MeSH and Text models led to a remarkable improvement (+71% for MAP) compared to the Text model alone. The most interesting aspect is that both models are highly complementary as the MeSH model brings 70% of new relevant documents that were not retrieved by the Text model. For the Prior Art task, we showed that there exist patterns of chemical patents that are interconnected (i.e. linked together with direct citations) and that are more likely to be present together in a prior art. Such patterns are efficiently retrieved with our Citations Feedback strategy. On the other hand, we pointed out that the less the prior art of a given topic is interconnected, the less efficient is the Information Retrieval. We hypothesize that such patents have a larger technical focus, maybe represented by a larger set of IPC codes, and then have a lower textual similarity with their prior art documents. These topics should gain to be recognized in order to be treated with complementary techniques.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GobeillGRPTV11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GobeillGRPTV11,
		author = {Julien Gobeill and Arnaud Gaudinat and Patrick Ruch and Emilie Pasche and Douglas Teodoro and Dina Vishnyakova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BiTeM Group Report for {TREC} Chemical {IR} Track 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/BiTeM.chem.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GobeillGRPTV11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Retrieval Framework for Technology Survey in Biomedical  and Chemistry Literature

_Harsha Gurulingappa, Bernd Müller, Martin Hofmann-Apitius, Juliane Fluck_

- :fontawesome-solid-user-group: **Participant:** [fraunhofer.scai](./chemical/participants.md#fraunhofer.scai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Fraunhofer-SCAI.chem.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Fraunhofer-SCAI.chem.update.pdf)
- :material-file-search: **Runs:** [SCAIRUN1](./chemical/runs.md#scairun1) | [SCAIRUN2](./chemical/runs.md#scairun2) | [SCAIRUN3](./chemical/runs.md#scairun3) | [SCAIRUN4](./chemical/runs.md#scairun4)

??? abstract "Abstract"
	
	The Technology survey task deals with the retrieval of information that can best answer a scientific question. This task is more challenging in biomedical and chemistry domains due to diverse conventions applied for naming the entities. In order to address this challenge, the work reported here presents an ad-hoc retrieval task that has been evaluated during the TRECCHEM-2011 for its ability to support retrieval from the biomedical and chemistry literature. The core of the framework contains nearly 1.3 million patents and full-text articles that were indexed with pre-selected biomedical concepts. Altogether, four runs were submitted based on different query formulation strategies and they exhibited competitive results
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GurulingappaMHFGH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GurulingappaMHFGH11,
		author = {Harsha Gurulingappa and Bernd M{\"{u}}ller and Martin Hofmann{-}Apitius and Juliane Fluck},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Information Retrieval Framework for Technology Survey in Biomedical and Chemistry Literature},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Fraunhofer-SCAI.chem.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GurulingappaMHFGH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Image-to-Structure Task by ChemReader

_Jungkap Park, Ye Li, Gus R. Rosania, Kazuhiro Saitou_

- :fontawesome-solid-user-group: **Participant:** [ChemReader](./chemical/participants.md#chemreader)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/chemreader.chem.update.pdf](http://trec.nist.gov/pubs/trec20/papers/chemreader.chem.update.pdf)
- :material-file-search: **Runs:** [ChemReader_Run1](./chemical/runs.md#chemreader_run1) | [ChemReader_Run2](./chemical/runs.md#chemreader_run2)

??? abstract "Abstract"
	
	Chemical structure recognition software aims to extract raster images of 2D chemical structure diagrams and convert them into a standard, machineͲreadable chemical file format. Such software, so called chemical OCR can be used for mining chemical entities appeared in scientific literature. Since traditional textͲbased mining methods haven't attempt to utilize image data in documents yet, chemical OCR software will pave a new way for the development of chemical literature mining [1, 2]. This year, the TREC Chemical IR campaign has launched a new topic called “ImageͲtoͲStructure (I2S) task” where participants are asked to process given images and recognize chemical structures in the images. While the immediate objective of this task would be to evaluate the existing chemical OCR software, it ultimately aims to create a platform to see how information in image data can be incorporated with existing textͲmining approach to facilitate further development of chemical IR techniques. We developed a chemical OCR software, ChemReader which specifically tailored to a chemical database annotation scheme [3, 4]. The recognition algorithms are optimized to achieve high accuracy and robust performance sufficient for fully automated processing of scientific articles. In our previous reports, ChemReader was able to outperform other chemical OCR software on several sets of sample images from diverse sources in terms of the rate of correct outputs and the accuracy on extracting molecular substructure patterns. Since then, other existing tools have been continuously updated, and new chemical OCR tools also have been released. Thus this task is a good opportunity for chemical OCR developers to evaluate their algorithms against common image set, and see strengths and weaknesses of their own comparing them to others. Here we report how we performed the I2S task during MayͲJuly, 2011. We first briefly present the recognition algorithms in ChemReader, followed by the updates during the training. Then, we will show the results of its evaluation on test set and discuss major errors of ChemReader on the test. Most importantly, on the basis of the lessons learned from this task, we will discuss issues and insights in the chemical OCR development.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ParkLRS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ParkLRS11,
		author = {Jungkap Park and Ye Li and Gus R. Rosania and Kazuhiro Saitou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Image-to-Structure Task by ChemReader},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/chemreader.chem.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ParkLRS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Performance of MolRec at TREC 2011 Overview and Analysis of Results

_Noureddin M. Sadawi, Alan P. Sexton, Volker Sorge_

- :fontawesome-solid-user-group: **Participant:** [UoB](./chemical/participants.md#uob)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UoB.chem.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UoB.chem.update.pdf)
- :material-file-search: **Runs:** [Run1](./chemical/runs.md#run1) | [Run2](./chemical/runs.md#run2)

??? abstract "Abstract"
	
	Chemical molecular diagrams are commonly found in documents from the chemical and life science disciplines. We present an overview of the elements of these diagrams and of MolRec, our system for analysing and recognising them. MolRec uses a number of techniques to refine the scanned images and precisely detect line segments and line junctions, structural elements and the atomic formulae that commonly appear in such diagrams. The output of our system is a chemical formula and associated MOL file, a standard representation of molecular structures used in cheminformatics that records precise molecular spatial and connectivity information. When applied to the TREC 2011 test set of 1000 molecular diagrams, MolRec returned in two separate runs 949 and 950 correctly recalled structures, respectively. We discuss these results and present an analysis of MolRec's performance on the test set.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SadawiSS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/SadawiSS11,
		author = {Noureddin M. Sadawi and Alan P. Sexton and Volker Sorge},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Performance of MolRec at {TREC} 2011 Overview and Analysis of Results},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UoB.chem.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SadawiSS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Imago: Open-Source Toolkit for 2D Chemical Structure Image Recognition

_Viktor Smolov, Fedor Zentsev, Mikhail Rybalkin_

- :fontawesome-solid-user-group: **Participant:** [GGA](./chemical/participants.md#gga)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/GGA.chemical.pdf](http://trec.nist.gov/pubs/trec20/papers/GGA.chemical.pdf)
- :material-file-search: **Runs:** [GGA_Imago_2011](./chemical/runs.md#gga_imago_2011) | [GGA_Imago2011a](./chemical/runs.md#gga_imago2011a)

??? abstract "Abstract"
	
	Different chemical databases contain molecule structures with links to articles and patents, where such molecules are presented as images. Keeping such a database in a consistent state is a challenging problem, and, thus, efficient and accurate molecule image recognition algorithms are very important for solving this task. We present an open-source toolkit for 2D chemical structure image recognition, called Imago. The main aim of this paper is to describe the algorithm approach implemented in Imago, and to share our ideas of possible improvements in the algorithm after we have summarized the results from the participation in the Image2Structure task at TREC-CHEM 2011.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SmolovZR11.bib) "
	```
	@inproceedings{DBLP:conf/trec/SmolovZR11,
		author = {Viktor Smolov and Fedor Zentsev and Mikhail Rybalkin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Imago: Open-Source Toolkit for 2D Chemical Structure Image Recognition},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/GGA.chemical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SmolovZR11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2011 Chemistry Track

_Ping Zhang, Hongfei Lin, Jiajin Wu, Yuan Lin_

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./chemical/participants.md#dutir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/DUTIR.chem.update.pdf](http://trec.nist.gov/pubs/trec20/papers/DUTIR.chem.update.pdf)
- :material-file-search: **Runs:** [DUT11TSRun1](./chemical/runs.md#dut11tsrun1) | [DUT11TSRun2](./chemical/runs.md#dut11tsrun2) | [DUT11TSRun3](./chemical/runs.md#dut11tsrun3) | [DUT11TSRun4](./chemical/runs.md#dut11tsrun4) | [DUT11PARun1](./chemical/runs.md#dut11parun1) | [DUT11PARun5](./chemical/runs.md#dut11parun5) | [DUT11PARun2](./chemical/runs.md#dut11parun2) | [DUT11PARun3](./chemical/runs.md#dut11parun3) | [DUT11PARun4](./chemical/runs.md#dut11parun4) | [DUT11PARun6](./chemical/runs.md#dut11parun6) | [DUT11PARun7](./chemical/runs.md#dut11parun7) | [DUT11PARun8](./chemical/runs.md#dut11parun8) | [DUT11PARun9](./chemical/runs.md#dut11parun9)

??? abstract "Abstract"
	
	This paper presents the DUTIR submission to TREC 2011 Chemical IR Track. Several experiments are done mainly with two retrieval models i.e. Language Model for IR and DFR model. In addition, query expansion technology is also applied to enhance retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangLWL11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangLWL11,
		author = {Ping Zhang and Hongfei Lin and Jiajin Wu and Yuan Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2011 Chemistry Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/DUTIR.chem.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangLWL11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### How to Make Manual Conjunctive Normal Form Queries Work in Patents  Search

_Le Zhao, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU.LIRA](./chemical/participants.md#cmu.lira)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/CMU-LIRA.chemistry.pdf](http://trec.nist.gov/pubs/trec20/papers/CMU-LIRA.chemistry.pdf)
- :material-file-search: **Runs:** [CMUTSmans](./chemical/runs.md#cmutsmans) | [CMUTStncs](./chemical/runs.md#cmutstncs) | [CMUTStncws](./chemical/runs.md#cmutstncws)

??? abstract "Abstract"
	
	This year we focused on the Technology Survey (TS) task: Given a natural language description of the topic, look for related patents about that topic. The task is close to an ad hoc retrieval task, except for the additional information of the specific chemicals or chemical reactions that the user cares about. Since there are only 6 topics for the TS task, this notebook paper is more of a case study report, than the ordinary TREC report with significance tests. We found that on average, with the infAP measure, manually created conjunctive normal form queries performed similarly as automatic keyword search with some tuning of term weights. Manual queries do not seem to always help, especially when initial keyword performance is high, but can give large improvements on difficult queries. We also used the same querying strategy in the Patent Olympics 2011 ChemAthlon task, and also include some of the ChemAthlon cases in this report. Since CNF queries are strictly more expressive than keyword queries, we try to identify problems that may have caused the manual CNF queries to be seen sometimes performing worse than the automatic keyword queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoC11,
		author = {Le Zhao and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {How to Make Manual Conjunctive Normal Form Queries Work in Patents Search},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/CMU-LIRA.chemistry.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Chemical Structure Reconstruction with chemoCR

_Marc Zimmermann_

- :fontawesome-solid-user-group: **Participant:** [chemoCR](./chemical/participants.md#chemocr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/chemoCR.chem.update.pdf](http://trec.nist.gov/pubs/trec20/papers/chemoCR.chem.update.pdf)
- :material-file-search: **Runs:** [chemoCR_v93_p10](./chemical/runs.md#chemocr_v93_p10)

??? abstract "Abstract"
	
	chemoCR makes chemical information contained in depictions of chemical structures accessible as connection table for computer programs. In order to solve the problem of recognizing and translating chemical structures in image documents, our chemoCR system combines pattern recognition techniques with supervised machine learning concepts. The method is based on the idea of identifying from structural formulas the most significant semantic entities. Semantic entities are for example chiral bonds, superatoms and reaction arrows. The workflow consists of three phases: image preprocessing, semantic entity recognition, and molecule reconstruction plus validation of the result. All steps of the process make use of chemical knowledge in order to detect and fix errors. The system can be trained and adapted to different sources of input images. The reconstructed connection table can be used by all chemical software.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Zimmermann11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Zimmermann11,
		author = {Marc Zimmermann},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Chemical Structure Reconstruction with chemoCR},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/chemoCR.chem.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Zimmermann11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Medical 

#### Search for Clinical Records: RMIT at Medical TREC

_Iman Amini, Mark Sanderson, David Martínez, Xiaodong Li_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./medical/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/RMIT.medical.update.pdf](http://trec.nist.gov/pubs/trec20/papers/RMIT.medical.update.pdf)
- :material-file-search: **Runs:** [RMIT1](./medical/runs.md#rmit1) | [RMIT2](./medical/runs.md#rmit2) | [RMIT3](./medical/runs.md#rmit3) | [RMITN1](./medical/runs.md#rmitn1) | [RMITN2](./medical/runs.md#rmitn2) | [RMITN3](./medical/runs.md#rmitn3)

??? abstract "Abstract"
	
	We combine several techniques to participate in Medical TREC 2011 and later we decompose our combined methodologies to gain a thorough understanding of the effects of each individual technique. In this paper we focus on Information Extraction and Expansion to find the best setting for an ideal IR system. Results suggest that Information Expansion is a key strategy in finding relevant reports for a medical query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AminiSML11.bib) "
	```
	@inproceedings{DBLP:conf/trec/AminiSML11,
		author = {Iman Amini and Mark Sanderson and David Mart{\'{\i}}nez and Xiaodong Li},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Search for Clinical Records: {RMIT} at Medical {TREC}},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/RMIT.medical.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AminiSML11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Identifying Patients for Clinical Studies from Electronic Health Records:  TREC Medical Records Track at OHSU

_Steven Bedrick, Kyle H. Ambert, Aaron M. Cohen, William R. Hersh_

- :fontawesome-solid-user-group: **Participant:** [OHSU](./medical/participants.md#ohsu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/OHSU.medical.update.pdf](http://trec.nist.gov/pubs/trec20/papers/OHSU.medical.update.pdf)
- :material-file-search: **Runs:** [ohsuManAll](./medical/runs.md#ohsumanall) | [ohsuManLim](./medical/runs.md#ohsumanlim)

??? abstract "Abstract"
	
	The task of the TREC 2011 Medical Records Track consisted of searching electronic health record (EHR) documents in order to identify patients matching a set of clinical criteria, a use case that might be part of the preparation of a quality report or to develop a cohort for a clinical trial. The task's various topics each represented a different case definition, with the topics varying widely in terms of detail and linguistic complexity. This use case is one of a larger group that represent the “secondary use” of data in EHRs [1] that facilitate clinical research, quality improvement, and other aspects of a health care system that can “learn” from its data and outcomes [2]. It is made possible by the large US government investment in EHR adoption that has occurred since 2009 [3]. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BedrickACH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BedrickACH11,
		author = {Steven Bedrick and Kyle H. Ambert and Aaron M. Cohen and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Identifying Patients for Clinical Studies from Electronic Health Records: {TREC} Medical Records Track at {OHSU}},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/OHSU.medical.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BedrickACH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCD IIRG at TREC 2011 Medical Track

_James Cogley, Nicola Stokes, John Dunnion, Joe Carthy_

- :fontawesome-solid-user-group: **Participant:** [UCD_CSI](./medical/participants.md#ucd_csi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UCDSI.med.pdf](http://trec.nist.gov/pubs/trec20/papers/UCDSI.med.pdf)
- :material-file-search: **Runs:** [UCDCSIrunOne](./medical/runs.md#ucdcsirunone) | [UCDCSIrunTwo](./medical/runs.md#ucdcsiruntwo) | [UCDCSIrun3](./medical/runs.md#ucdcsirun3) | [UCDCSIrun4](./medical/runs.md#ucdcsirun4)

??? abstract "Abstract"
	
	In this paper, we present several approaches to the retrieval of medical visits in response to user queries on patient demographics. A visit is comprised of one or more medical reports. Given a data collection of medical reports, TREC Medical Track participants had the opportunity to either preprocess the documents concatenating reports into visits, or to post-process by retrieving reports and developing a method to create a ranking of visits given the retrieved reports. This paper outlines attempts at both approaches in order to determine the influence of the disparity of document lengths in the collection. For both these approaches query expansion and concept re-ranking are applied. Concept reranking identifies the number of unique concepts from an expanded query contained in a document, and boosts the rank of documents which contain more unique concepts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CogleySDC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/CogleySDC11,
		author = {James Cogley and Nicola Stokes and John Dunnion and Joe Carthy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UCD} {IIRG} at {TREC} 2011 Medical Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UCDSI.med.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CogleySDC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MetaMap is a Superior Baseline to a Standard Document Retrieval Engine  for the Task of Finding Patient Cohorts in Clinical Free Text

_K. Bretonnel Cohen, Tom Christiansen, Lawrence E. Hunter_

- :fontawesome-solid-user-group: **Participant:** [UCSOM_BTMG](./medical/participants.md#ucsom_btmg)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UCSOM_BTMG.medical.new.pdf](http://trec.nist.gov/pubs/trec20/papers/UCSOM_BTMG.medical.new.pdf)
- :material-file-search: **Runs:** [unityranked](./medical/runs.md#unityranked)

??? abstract "Abstract"
	
	The goal of this work was to establish a reasonable baseline for research in patient cohort retrieval from clinical free text. Much recent work has used Lucene for this purpose. Our approach was to use MetaMap alone. We found that although many TREC 2011 Electronic Medical Records track participants found it difficult to beat a Lucene baseline, our MetaMap-based baseline did outperform a number of Lucene runs. We propose that MetaMap is a more valid baseline than Lucene, providing essential concept extraction, and that failure to make use of this industry-standard tool results in an unfairly low baseline for evaluation of system outputs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CohenCH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/CohenCH11,
		author = {K. Bretonnel Cohen and Tom Christiansen and Lawrence E. Hunter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {MetaMap is a Superior Baseline to a Standard Document Retrieval Engine for the Task of Finding Patient Cohorts in Clinical Free Text},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UCSOM\_BTMG.medical.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CohenCH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Medical-Miner at TREC 2011 Medical Records Track

_Juan Manuel Córdoba, Manuel J. Maña López, Noa P. Cruz Díaz, Jacinto Mata, Fernando Aparicio, Manuel de Buenaga Rodríguez, Daniel Glez-Peña, Florentino Fdez-Riverola_

- :fontawesome-solid-user-group: **Participant:** [MedicalMiner](./medical/participants.md#medicalminer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Medicalminer.medical.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Medicalminer.medical.update.pdf)
- :material-file-search: **Runs:** [UHU1BL](./medical/runs.md#uhu1bl) | [UHU2MFB](./medical/runs.md#uhu2mfb) | [UHU3BWRTDDD](./medical/runs.md#uhu3bwrtddd) | [UHU4BWRTDDD2](./medical/runs.md#uhu4bwrtddd2)

??? abstract "Abstract"
	
	This paper presents work done at Medical Minner Project on the TREC-2011 Medical Records Track. The paper proposes four models for medical information retrieval based on Lucene index approach. Our retrieval engine used an Lucen Index scheme with traditional stopping and stemming, enhanced with entity recognition software on query terms. Our aim in this first competition is to set a broader project that involves the develop of a configurable Apache Lucene-based framework that allows the rapid development of medical search facilities. Results around the track median have been achieved. In this exploratory track, we think that these results are a good beginning and encourage us for future developments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CordobaLDVARGF11.bib) "
	```
	@inproceedings{DBLP:conf/trec/CordobaLDVARGF11,
		author = {Juan Manuel C{\'{o}}rdoba and Manuel J. Ma{\~{n}}a L{\'{o}}pez and Noa P. Cruz D{\'{\i}}az and Jacinto Mata and Fernando Aparicio and Manuel de Buenaga Rodr{\'{\i}}guez and Daniel Glez{-}Pe{\~{n}}a and Florentino Fdez{-}Riverola},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Medical-Miner at {TREC} 2011 Medical Records Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Medicalminer.medical.update.pdf},
		timestamp = {Fri, 24 Jul 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CordobaLDVARGF11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2011: Medical Records Track

_Mariam Daoud, Dawid Kasperowicz, Jun Miao, Jimmy X. Huang_

- :fontawesome-solid-user-group: **Participant:** [york](./medical/participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/york.medical.pdf](http://trec.nist.gov/pubs/trec20/papers/york.medical.pdf)
- :material-file-search: **Runs:** [york11CQ2](./medical/runs.md#york11cq2) | [york11CB1](./medical/runs.md#york11cb1) | [york11mQeD1](./medical/runs.md#york11mqed1) | [york11mSB1](./medical/runs.md#york11msb1)

??? abstract "Abstract"
	
	n this paper, we present our participation in the Medical Records Track of TREC 2011. The goal of this track is to develop quick search and retrieval tools that are useful for physicians for the purpose to find patients that have similar diseases and/or treatments. To achieve this goal, we propose query expansion and semantic matching models using semantic medical ontologies for medical data retrieval. The query expansion utilizes a medical disease dictionary that presents different possible reformulations given the query disease keywords. For the semantic matching model, we employed BioLabler, a medical annotation tool that allows indexing of queries and documents with UMLS concepts of our choosing. Moreover, the matching model consists of ranking the documents that contain the query concepts according to their scores in the document. We also evaluate a traditional weighting model (BM25), query expansion using relevance feedback under Rocchio's feedback framework and the impact of genre and age filtering, proximity and co-occurrence between disease keywords and procedure/intervention keywords on the retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DaoudKMH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/DaoudKMH11,
		author = {Mariam Daoud and Dawid Kasperowicz and Jun Miao and Jimmy X. Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2011: Medical Records Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/york.medical.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DaoudKMH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Knowledge-Based Approach to Medical Records Retrieval

_Dina Demner-Fushman, Swapna Abhyankar, Antonio Jimeno-Yepes, Russell F. Loane, Bastien Rance, François-Michel Lang, Nicholas C. Ide, Emilia Apostolova, Alan R. Aronson_

- :fontawesome-solid-user-group: **Participant:** [NLM](./medical/participants.md#nlm)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/NLM.medical.pdf](http://trec.nist.gov/pubs/trec20/papers/NLM.medical.pdf)

??? abstract "Abstract"
	
	The NLM LHC team approached the cohort selection task of the 2011 Medical Records Track as a question answering problem. We developed 60 training topics and then manually converted those topics to question frames. We started with the evidence-based medicine well-formed question frame and expanded it to explicitly capture temporal and causal relations. We then implemented a syntactic-semantic method for extracting the question frames from the free text topics. Based on the clinical documentation standards and knowledge of the clinical documentation structure, we split each report type into sections corresponding to different categories of clinical content, with the result that each section contained a specific class of data. We then ranked each document section according to its likelihood of containing answers to specific question frame slots. For example, if a question concerns medications prior to admission, the answers should be found in the Medications on Admission and the Medical History sections. In addition, we split each section into Positive (containing asserted findings, problems, and interventions), Negative (in which findings are negated) and Possible (that includes all uncertain statements). After structuring the questions and the documents, we developed algorithms for expressing question frames in the languages of the two search engines used for retrieval: Essie and Lucene. In addition to the UMLS synonymy-based query expansion built into Essie and implemented externally for Lucene, we expanded the terms in the documents with their ancestors and children from the MeSH hierarchy. We also expanded query terms for recognized drug names using RxNorm and Google searches. In addition to the automatically generated baseline and expanded queries that we ran against the original and the structured documents, we used the Essie user interface for manual query generation. During this process, we determined that a third of the automatically generated question frames, although technically correct, needed significant modifications due to different sub-languages used in the documents and in the queries. The manually created queries were used to search the collection with each search engine. Our manual queries submitted to Essie significantly outperformed all of our other runs (achieving 0.73 P@10, 0.66 bpref, and 0.49 R-prec). Interestingly, the best automatic run for Lucene was the baseline run (P@10 = 0.44, bpref = 0.47, R-prec = 0.33) that used the topics “as is” to search the original documents. The results for this run are not significantly different from the manual Lucene (P@10 = 0.51, bpref = 0.51, R-prec = 0.35) and the automatic Essie (P@10 = 0.49, bpref = 0.48, R-prec = 0.33) runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Demner-FushmanAJLRLIAA11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Demner-FushmanAJLRLIAA11,
		author = {Dina Demner{-}Fushman and Swapna Abhyankar and Antonio Jimeno{-}Yepes and Russell F. Loane and Bastien Rance and Fran{\c{c}}ois{-}Michel Lang and Nicholas C. Ide and Emilia Apostolova and Alan R. Aronson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Knowledge-Based Approach to Medical Records Retrieval},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/NLM.medical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Demner-FushmanAJLRLIAA11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC 2011: Evaluation of Query Expansion Techniques for  Medical Record Retrieval

_Duy Dinh, Lynda Tamine_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./medical/participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/IRIT.medical.update.pdf](http://trec.nist.gov/pubs/trec20/papers/IRIT.medical.update.pdf)
- :material-file-search: **Runs:** [IRITa1](./medical/runs.md#irita1) | [IRITa1QE1](./medical/runs.md#irita1qe1) | [IRITm1](./medical/runs.md#iritm1) | [IRITm1QE1](./medical/runs.md#iritm1qe1)

??? abstract "Abstract"
	
	In TREC 2011, we are motivated to participate in the medical record retrieval task, namely TRECMed. Our research focused on the evaluation of term weighting models and query expansion techniques within the medical record retrieval task. We compared the performance of different state-of-the-art term weighting models for retrieving patient records that might best suit the clinical information need. Afterwards, we evaluate different state-of-the-art query expansion (QE) techniques within an IR framework. We describe the IR system architecture and how we carried out the TREC experiments, and we present effectiveness results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DinhT11.bib) "
	```
	@inproceedings{DBLP:conf/trec/DinhT11,
		author = {Duy Dinh and Lynda Tamine},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRIT} at {TREC} 2011: Evaluation of Query Expansion Techniques for Medical Record Retrieval},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/IRIT.medical.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DinhT11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept-Centric Indexing and Retrieval on Medical Text

_David Eichmann_

- :fontawesome-solid-user-group: **Participant:** [UI_ICTS](./medical/participants.md#ui_icts)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UI_ICTS.medical.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UI_ICTS.medical.update.pdf)
- :material-file-search: **Runs:** [UIICTSmed01](./medical/runs.md#uiictsmed01) | [UIICTSmed02](./medical/runs.md#uiictsmed02) | [UIICTSmed03](./medical/runs.md#uiictsmed03) | [UIICTSmed04](./medical/runs.md#uiictsmed04) | [UIICTSmed05](./medical/runs.md#uiictsmed05) | [UIICTSmed06](./medical/runs.md#uiictsmed06) | [UIICTSmed07](./medical/runs.md#uiictsmed07) | [UIICTSmed08](./medical/runs.md#uiictsmed08)

??? abstract "Abstract"
	
	The NIH Clinical and Translational Science Award (CTSA) program has resulted in the formation of new research interactions for many IR and NLP research groups. Research access to large-­-scale clinical data is proving to be a critical component of the overall goals of the CTSA. While much of the clinical record is tabular and structured, substantial amounts of pertinent information reside in unstructured text attached to those structured records. This is particularly true for research subject cohort identification, where the inclusion and exclusion criteria for a given study (e.g., family history, quality of life assessments, etc.) may not well align with the data captured in a typical clinical encounter. The TREC Medical Record track provides an excellent means to drive innovation in clinical data retrieval, particularly for unstructured elements of the electronic medical record.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Eichmann11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Eichmann11,
		author = {David Eichmann},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concept-Centric Indexing and Retrieval on Medical Text},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UI\_ICTS.medical.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Eichmann11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BiTeM Group Report for TREC Medical Records Track 2011

_Julien Gobeill, Arnaud Gaudinat, Patrick Ruch, Emilie Pasche, Douglas Teodoro, Dina Vishnyakova_

- :fontawesome-solid-user-group: **Participant:** [BiTeM](./medical/participants.md#bitem)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/BiTeM.medical.pdf](http://trec.nist.gov/pubs/trec20/papers/BiTeM.medical.pdf)
- :material-file-search: **Runs:** [BiTeMbase](./medical/runs.md#bitembase) | [BiTeMmEsh](./medical/runs.md#bitemmesh) | [BiTeMsnomed](./medical/runs.md#bitemsnomed) | [BiTeMmhICD](./medical/runs.md#bitemmhicd)

??? abstract "Abstract"
	
	The BiTeM group participated in the first TREC Medical Records Track in 2011 relying on a strong background in medical records processing and medical terminologies. For this campaign, we submitted a baseline run, computed with a simple free-text index in the Terrier platform, which achieved fair results (0.468 for P10). We also performed automatic text categorization on medical records and built additional inter-lingua representations in MeSH and SNOMED-CT concepts. Combined with the text index, these terminological representations led to a slight improvement of the top precision (+5 % for Mean Reciprocal Rank). But the most interesting is analysing the contribution of each representation in the coverage of the correct answer. The text representation and the additional terminological representations bring different, and finally complementary, views of the problem: if 40% of the official relevant visits were retrieved by our text index, an additional 15% part was retrieved only with the terminological representations, leading to 55% (more than half) of the relevant visits retrieved by all representations. Finally, an innovative re-ranking strategy was designed capitalizing on MeSH disorders concepts mapped on queries and their UMLS-equivalent ICD9 codes: visits that shared this ICD9 discharge code were boosted. This strategy led to another 10% improvement for top precision. Unfortunately, any deeper conclusion based on the official results is impossible to draw due the massive use of Lucene and the evaluation methods (pool): in our baseline text run, only 52% of our top 50 retrieved documents were judged, against 77% for another participant's baseline text run who used Lucene. Official metrics focused on precision are thus difficult to interpret.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GobeillGRPTV11a.bib) "
	```
	@inproceedings{DBLP:conf/trec/GobeillGRPTV11a,
		author = {Julien Gobeill and Arnaud Gaudinat and Patrick Ruch and Emilie Pasche and Douglas Teodoro and Dina Vishnyakova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BiTeM Group Report for {TREC} Medical Records Track 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/BiTeM.medical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GobeillGRPTV11a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cohort Shepherd: Discoving Cohort Traits from Hospital Visits

_Travis R. Goodwin, Bryan Rink, Kirk Roberts, Sanda M. Harabagiu_

- :fontawesome-solid-user-group: **Participant:** [UTD_HLT](./medical/participants.md#utd_hlt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UTD_HLT.medical.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UTD_HLT.medical.update.pdf)
- :material-file-search: **Runs:** [UTDHLTMK](./medical/runs.md#utdhltmk) | [UTDHLTSL](./medical/runs.md#utdhltsl) | [UTDHLTCIR](./medical/runs.md#utdhltcir) | [UTDHLTCIRLS](./medical/runs.md#utdhltcirls)

??? abstract "Abstract"
	
	This paper describes the system created by the University of Texas at Dallas for content-based medical record retrieval submitted to the TREC 2011 Medical Records Track. Our system builds a query by extracting keywords from a given topic using a Wikipedia-based approach we use regular expressions to extract age, gender, and negation requirements. Each query is then expanded by relying on UMLS, SNOMED, Wikipedia, and PubMed Co-occurrence data for retrieval. Four runs were submitted: two based on Lucene with varying scoring methods, and two based on a hybrid approach with varying negation detection techniques. Our highest scoring submission achieved a MAP score of 40.8.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoodwinRRH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoodwinRRH11,
		author = {Travis R. Goodwin and Bryan Rink and Kirk Roberts and Sanda M. Harabagiu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Cohort Shepherd: Discoving Cohort Traits from Hospital Visits},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UTD\_HLT.medical.update.pdf},
		timestamp = {Mon, 19 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GoodwinRRH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Semantic Platform for Information Retrieval from E-Health Records

_Harsha Gurulingappa, Bernd Müller, Martin Hofmann-Apitius, Juliane Fluck_

- :fontawesome-solid-user-group: **Participant:** [fraunhofer.scai](./medical/participants.md#fraunhofer.scai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Fraunhofer-SCAI.med.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Fraunhofer-SCAI.med.update.pdf)
- :material-file-search: **Runs:** [SCAIMED1](./medical/runs.md#scaimed1) | [SCAIMED2](./medical/runs.md#scaimed2) | [SCAIMED3](./medical/runs.md#scaimed3) | [SCAIMED4](./medical/runs.md#scaimed4) | [SCAIMED5](./medical/runs.md#scaimed5) | [SCAIMED6](./medical/runs.md#scaimed6) | [SCAIMED7](./medical/runs.md#scaimed7)

??? abstract "Abstract"
	
	Electronic patient health records encompass valuable information about patient's medical problems, diagnoses, and treatments offered including their outcomes. However, a problem for medical professionals is an ability to efficiently access the information that are documented in the form of free-text. Therefore, the work presented here exhibits an information retrieval platform for efficient processing of e-health records. The system offers facilities for keyword searches, semantic searches, and ontological searches. An open evaluation during the TRECMED 2011 demonstrated competitive results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GurulingappaMHFGH11a.bib) "
	```
	@inproceedings{DBLP:conf/trec/GurulingappaMHFGH11a,
		author = {Harsha Gurulingappa and Bernd M{\"{u}}ller and Martin Hofmann{-}Apitius and Juliane Fluck},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Semantic Platform for Information Retrieval from E-Health Records},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Fraunhofer-SCAI.med.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GurulingappaMHFGH11a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Search for Medical Records: NICTA at TREC 2011 Medical Track

_Sarvnaz Karimi, David Martínez, Sumukh Ghodke, Lawrence Cavedon, Hanna Suominen, Lumin Zhang_

- :fontawesome-solid-user-group: **Participant:** [NICTA_BioTALA](./medical/participants.md#nicta_biotala)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/NICTA_BIOTALA.med.update2.pdf](http://trec.nist.gov/pubs/trec20/papers/NICTA_BIOTALA.med.update2.pdf)
- :material-file-search: **Runs:** [NICTA1](./medical/runs.md#nicta1) | [NICTA2](./medical/runs.md#nicta2) | [NICTA3](./medical/runs.md#nicta3) | [NICTA4](./medical/runs.md#nicta4) | [NICTA6](./medical/runs.md#nicta6) | [NICTA5](./medical/runs.md#nicta5) | [NICTA7](./medical/runs.md#nicta7)

??? abstract "Abstract"
	
	NICTA (National ICT Australia) participated in the Medical Records track of TREC 2011 with seven automatic runs. The main techniques used in our submissions involved using Boolean retrieval for filtering, query transformation, and query expansion. Evaluation of our best run ranks our submissions higher than the median of all systems for this track, and stands at rank seven among 109 automatic runs which were submitted by the 29 participating groups.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KarimiMGCSZ11.bib) "
	```
	@inproceedings{DBLP:conf/trec/KarimiMGCSZ11,
		author = {Sarvnaz Karimi and David Mart{\'{\i}}nez and Sumukh Ghodke and Lawrence Cavedon and Hanna Suominen and Lumin Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Search for Medical Records: {NICTA} at {TREC} 2011 Medical Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/NICTA\_BIOTALA.med.update2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KarimiMGCSZ11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Cengage Learning at TREC 2011 Medical Track

_Benjamin King, Lijun Wang, Ivan Provalov, Jerry Zhou_

- :fontawesome-solid-user-group: **Participant:** [Cengage](./medical/participants.md#cengage)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Cengage.medical.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Cengage.medical.update.pdf)
- :material-file-search: **Runs:** [CengageM11R1](./medical/runs.md#cengagem11r1) | [CengageM11R2](./medical/runs.md#cengagem11r2) | [CengageM11R4](./medical/runs.md#cengagem11r4) | [CengageM11R3](./medical/runs.md#cengagem11r3)

??? abstract "Abstract"
	
	This paper details Cengage Learning's submissions for this year's TREC medical track. The techniques we used fall roughly into two categories: information extraction and query expansion. From both the queries and the medical reports, we extracted limiting attributes, such as age, race, and gender, and labeled terms appearing in the Unified Medical Language System (UMLS). We also used three different techniques of query expansion: UMLS related terms, terms from a network built from UMLS, and terms from our medical reference encyclopedias. We submitted four different runs varying only in their methods of query expansion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KingWPZ11.bib) "
	```
	@inproceedings{DBLP:conf/trec/KingWPZ11,
		author = {Benjamin King and Lijun Wang and Ivan Provalov and Jerry Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Cengage Learning at {TREC} 2011 Medical Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Cengage.medical.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KingWPZ11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### AEHRC & QUT at TREC 2011 Medical Track: A Concept-Based  Information Retrieval Approach

_Bevan Koopman, Michael Lawley, Peter Bruza, Laurianne Sitbon_

- :fontawesome-solid-user-group: **Participant:** [AEHRC](./medical/participants.md#aehrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/AEHRC.medical.pdf](http://trec.nist.gov/pubs/trec20/papers/AEHRC.medical.pdf)
- :material-file-search: **Runs:** [AEHRC1](./medical/runs.md#aehrc1) | [AEHRC2](./medical/runs.md#aehrc2)

??? abstract "Abstract"
	
	The Australian e-Health Research Centre and Queensland University of Technology recently participated in the TREC 2011 Medical Records Track. This paper reports on our methods, results and experience using a concept-based information retrieval approach. Our concept-based approach is intended to overcome specific challenges we identify in searching medical records. Queries and documents are transformed from their term-based originals into medical concepts as defined by the SNOMED-CT ontology. Results show our concept-based approach performed above the median in all three performance metrics: bref (+12%), R-prec (+18%) and Prec@10 (+6%).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoopmanLBS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoopmanLBS11,
		author = {Bevan Koopman and Michael Lawley and Peter Bruza and Laurianne Sitbon},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{AEHRC} {\&} {QUT} at {TREC} 2011 Medical Track: {A} Concept-Based Information Retrieval Approach},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/AEHRC.medical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KoopmanLBS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at Medical Records Track: Experiments with Terrier

_Nut Limsopatham, Craig Macdonald, Iadh Ounis, Graham McDonald, Matt-Mouley Bouamrane_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./medical/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uogTr.medical.update.pdf](http://trec.nist.gov/pubs/trec20/papers/uogTr.medical.update.pdf)
- :material-file-search: **Runs:** [uogTrDeNSo](./medical/runs.md#uogtrdenso) | [uogTrDeNsEc](./medical/runs.md#uogtrdensec) | [uogTrDeNIo](./medical/runs.md#uogtrdenio) | [uogTrMDeNFo](./medical/runs.md#uogtrmdenfo) | [uogTrDeNfCE](./medical/runs.md#uogtrdenfce)

??? abstract "Abstract"
	
	In our participation in the TREC 2011 Medical Records track, we investigate (1) novel voting-based approaches for identifying relevant patient visits from an aggregate of relevant medical records, (2) the effective handling of negated language in records and queries, and (3) the adoption of medical-domain ontologies for improving the representation of queries, all within the context of our Terrier information retrieval platform.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LimsopathamMOMB11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LimsopathamMOMB11,
		author = {Nut Limsopatham and Craig Macdonald and Iadh Ounis and Graham McDonald and Matt{-}Mouley Bouamrane},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at Medical Records Track: Experiments with Terrier},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uogTr.medical.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LimsopathamMOMB11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DEMIR at TREC Medical 2011: Power of Term Phrases in Medical Text  Retrieval

_Okan Ozturkmenoglu, Adil Alpkocak_

- :fontawesome-solid-user-group: **Participant:** [DEUCENG](./medical/participants.md#deuceng)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/DEUCENG.medical.update.pdf](http://trec.nist.gov/pubs/trec20/papers/DEUCENG.medical.update.pdf)
- :material-file-search: **Runs:** [DEMIR2TW](./medical/runs.md#demir2tw) | [DEMIR4TWP](./medical/runs.md#demir4twp) | [DEMIR1BASE](./medical/runs.md#demir1base)

??? abstract "Abstract"
	
	This paper present the details of participation of DEMIR (Dokuz Eylul University Multimedia Information Retrieval) research team to TREC 2011 Medical Records track. In this study, our aim is to index and retrieve medical terms and term phrases in medical text archives. We searched medical terms and term phrases with using UMLS which is a metathesaurus about medical. We evaluated the effects of terms and term phrases on retrieval system in TREC 2011 Medical Records track, considering terms and term phrases as medical entities. We improved results by examination of different weighting schemes for retrieved data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/OzturkmenogluA11.bib) "
	```
	@inproceedings{DBLP:conf/trec/OzturkmenogluA11,
		author = {Okan Ozturkmenoglu and Adil Alpkocak},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DEMIR} at {TREC} Medical 2011: Power of Term Phrases in Medical Text Retrieval},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/DEUCENG.medical.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/OzturkmenogluA11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DutchHatTrick: Semantic Query Modeling, ConText, Section Detection,  and Match Score Maximization

_Martijn J. Schuemie, Dolf Trieschnigg, Edgar Meij_

- :fontawesome-solid-user-group: **Participant:** [DutchHatTrick](./medical/participants.md#dutchhattrick)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/DutchHatTrick.med.update.pdf](http://trec.nist.gov/pubs/trec20/papers/DutchHatTrick.med.update.pdf)

??? abstract "Abstract"
	
	This report discusses the collaborative work of the ErasmusMC, University of Twente, and the University of Amsterdam on the TREC 2011 Medical track. Here, the task is to retrieve patient visits from the University of Pittsburgh NLP Repository for 35 topics. The repository consists of 101,711 patient reports, and a patient visit was recorded in one or more reports. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchuemieTM11.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchuemieTM11,
		author = {Martijn J. Schuemie and Dolf Trieschnigg and Edgar Meij},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {DutchHatTrick: Semantic Query Modeling, ConText, Section Detection, and Match Score Maximization},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/DutchHatTrick.med.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchuemieTM11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding Patient Visits in EMR Using LUXID®

_Luca Toldo, Alexander Scheer_

- :fontawesome-solid-user-group: **Participant:** [MERCKKGAA](./medical/participants.md#merckkgaa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/merckkgaa.medical.update.pdf](http://trec.nist.gov/pubs/trec20/papers/merckkgaa.medical.update.pdf)
- :material-file-search: **Runs:** [merckkgaamer](./medical/runs.md#merckkgaamer)

??? abstract "Abstract"
	
	INTRODUCTION : Free text sections of the Electronic Medical Records (EMR) contain information that cannot be appropriately constrained in the structured forms. Several studies have shown the potential utility in mining EMR free texts for identifying adverse events (e.g. EU-PSIP, EU-ALERT), and large public-private research projects (e.g. IMI-EHR4CR, CLOUD4HEALTH) aim at mining them further, e.g. for clinical trial optimisation and pharmacovigilance purposes. AIM : The purpose of this work has been to assess the performance of LUXID R©, an off-the-shelve commercial natural language processing system, using the dictionary- and rule-based Medical Entity Relationships Skill Cartridge R©and KNIME as automation workflow engine for result combination and formatting, on the University of Pittsburgh BLULab NLP Repository benchmark, in the context of the TREC 2011 Medical Records Retrieval Track (TREC-MED2011). RESULTS : The system here described achieved the best score for one of the 34 queries (defined as query 111) and overall classified as top 7th-8th (according to the scoring used) in the manual track of TREC-MED2011. More than 80% of the queries of TREC-MED2011 could be appropriately processed automatically. Performance of manually interpreted queries did not differ substantially from those automatically processed. More than 60% of the queries submitted by our system delivered a performance above or on the median of all participants. Very high precision of the system, delivering in certain cases a very low number of hits, correlated statistically with the overall performance. CONCLUSIONS : Initial results, error analysis are reported and strategies for improvements of the system are outlined; fully supporting the appropriateness in using this technology for identifying patients matching inclusion/exclusion criteria using plain text from unstructured EMR.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ToldoS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ToldoS11,
		author = {Luca Toldo and Alexander Scheer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Finding Patient Visits in {EMR} Using LUXID{\textregistered}},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/merckkgaa.medical.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ToldoS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Exploration of New Ranking Strategies for Medical Record Tracks

_Hao Wu, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [Udel_Fang](./medical/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Udel_Fang.medical.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Udel_Fang.medical.update.pdf)
- :material-file-search: **Runs:** [UDMedProx](./medical/runs.md#udmedprox) | [UDMedExp](./medical/runs.md#udmedexp) | [UDMedComb](./medical/runs.md#udmedcomb) | [UDMedDiv](./medical/runs.md#udmeddiv) | [UDMedBL](./medical/runs.md#udmedbl)

??? abstract "Abstract"
	
	We report our system and experiments at the 2011 Medical Record Track. Our goal is to return most relevant visits according to a query. In particular, we start with an axiomatic retrieval, and combine it with an aspect based term proximity strategy to improve the retrieval performance. We also propose a “disease diversity” strategy based on the assumption that most of documents only contain information related to one main disease. Query expansion using external resources has also been studied.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuF11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuF11,
		author = {Hao Wu and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {An Exploration of New Ranking Strategies for Medical Record Tracks},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Udel\_Fang.medical.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuF11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2011 Medical Record Track

_Jiayue Zhang, Xueneng Lin, Yang Zou, Shuai Zhu, Jing Xiao, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [BUPT_WILDCAT](./medical/participants.md#bupt_wildcat)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/PRIS.medical.pdf](http://trec.nist.gov/pubs/trec20/papers/PRIS.medical.pdf)
- :material-file-search: **Runs:** [buptpris01](./medical/runs.md#buptpris01) | [buptpris02](./medical/runs.md#buptpris02)

??? abstract "Abstract"
	
	Our method to accomplish the Medical Record Track is described in this paper. For ad hoc retrieval, Indri and Xapian are used for indexing, searching, and initial query expansion. The main query expansion is achieved using LSI. The evaluation results show the performance of our system is above the average.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangLZZXXCG11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangLZZXXCG11,
		author = {Jiayue Zhang and Xueneng Lin and Yang Zou and Shuai Zhu and Jing Xiao and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2011 Medical Record Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/PRIS.medical.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangLZZXXCG11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Multiple External Collections for Query Expansion

_Dongqing Zhu, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [udel](./medical/participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/udel.medical.pdf](http://trec.nist.gov/pubs/trec20/papers/udel.medical.pdf)
- :material-file-search: **Runs:** [udelbl](./medical/runs.md#udelbl) | [udelmx](./medical/runs.md#udelmx) | [udelgn](./medical/runs.md#udelgn) | [udelpm](./medical/runs.md#udelpm)

??? abstract "Abstract"
	
	For the 2011 Medical Records Track, we used several external collections for query expansion and mainly explored three research questions: First, we investigated the possibility of using query sessions from PubMed query logs for improving the estimation of a relevance model. In a typical search scenario, a user may submit multiple queries before she actually finds satisfactory search results. These closely related queries form a single query session which represents a single information need. By finding relevant query sessions with regard to a Medical Track topic we can incorporate into our relevance model useful query terms which reflect real information needs that are more or less related to the Medical Track topic. Second, we explored how the size and quality of external collections would impact the effectiveness of query expansion. More specifically, we used TREC 2007 Genomics Track data and ImageCLEF 2009 Medical Retrieval data. The former collection is more genomics-related and is larger while the latter one is more medical-related and is much smaller. Intuitively, it is more likely for a larger external collection to contain more good expansion terms. However, the quality (in terms of the overlapping concepts between the target collection and an external collection) can be an important factor as well. This allowed us to carry out a pilot study on the relationship between collection quality, size, and the effect on query expansion. Third, we used a mixture of external collections for query expansion. In particular, we explored methods that can adaptively combine evidence from multiple collections for different topics. Usually, the weights for a mixture relevance model are determined via training on a test collection, and thus are fixed across all topics. If we could estimate the concept overlapping of a topic with external collections and assign weights for the mixture model accordingly, the system can be adaptive to topics and may achieve a better performance. That is the motivation for this third research direction. We first describe our retrieval models and systems in Sections 2 and 3. Then in Section 4 we show and compare the official TREC evaluation results of our submissions, and further analyze our retrieval system performance based on the test collection. Following that, we discuss the above research questions in Section 5. We conclude in Section 6.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhuC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhuC11,
		author = {Dongqing Zhu and Ben Carterette},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Multiple External Collections for Query Expansion},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/udel.medical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhuC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Empirical Ontologies for Cohort Identification

_Stephen T. Wu, Kavishwar B. Wagholikar, Sunghwan Sohn, Vinod Kaggal, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [MayoClinicNLP](./medical/participants.md#mayoclinicnlp)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Mayo.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Mayo.update.pdf)
- :material-file-search: **Runs:** [mayobaseline](./medical/runs.md#mayobaseline) | [mayoauto](./medical/runs.md#mayoauto) | [mayocooccur](./medical/runs.md#mayocooccur) | [mayolbrst](./medical/runs.md#mayolbrst) | [mayolbra](./medical/runs.md#mayolbra) | [mayoubr](./medical/runs.md#mayoubr) | [mayo2noprop](./medical/runs.md#mayo2noprop)

??? abstract "Abstract"
	
	The growth of patient data stored in Electronic Medical Records (EMR) has greatly expanded the potential for the evidence-based improvement of clinical practice. The proper re-use of this clinical information, however, does not replace basic research techniques — it augments them. The Text REtrieval Conference 2011 Medical Records Track explored how information retrieval may support clinical research by providing an efficient means to identify cohorts for clinical studies. Mayo Clinic NLP's submission to the TREC Medical Records track attempts information retrieval at a semantic level, combining two disparate means of computing clinical semantics. Substantial effort has gone into the development of precise semantic specification of concepts in medical ontologies and terminologies[1, ?]. But human clinicians do not generate clinical text by referring to such resources, and ontology creators do not base their terminology design on clinical text — so the distribution of ontology concepts in actual clinical texts may differ greatly. Therefore, in representing clinical reports for cohort identification, we advocate for a model that makes use of expert knowledge, is empirically validated, and considers context. This is accomplished through a new framework: empirical ontologies. Patient cohort identification is thus a practical use case for the techniques in our recent work on clinical concept frequency comparisons[2, 3]. The rest of this paper describes the TREC 2011 Medical Records task, describes Mayo Clinic's run submissions, and reports evaluation results with subsequent discussion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuWSKL11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuWSKL11,
		author = {Stephen T. Wu and Kavishwar B. Wagholikar and Sunghwan Sohn and Vinod Kaggal and Hongfang Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Empirical Ontologies for Cohort Identification},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Mayo.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuWSKL11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Iowa at TREC 2011: Microblogs, Medical Records  and Crowdsourcing

_Sanmitra Bhattacharya, Christopher G. Harris, Yelena Mejova, Chao Yang, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [UIowaS](./medical/participants.md#uiowas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf)
- :material-file-search: **Runs:** [UIowaSMED1](./medical/runs.md#uiowasmed1) | [UIowaSMED2](./medical/runs.md#uiowasmed2) | [UIowaSMED3](./medical/runs.md#uiowasmed3) | [UIowaSMED4](./medical/runs.md#uiowasmed4)

??? abstract "Abstract"
	
	The Text Retrieval and Text Mining group at the University of Iowa participated in three tracks, all new tracks introduced this year: Microblog, Medical Records (Med) and Crowdsourcing. Details of our strategies are provided in this paper. Overall our effort has been fruitful in that we have been able to understand more about the nature of medical records and Twitter messages, and also the merits and challenges of working with games as a framework for gathering relevance judgments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bhattacharya0MYS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bhattacharya0MYS11,
		author = {Sanmitra Bhattacharya and Christopher G. Harris and Yelena Mejova and Chao Yang and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Iowa at {TREC} 2011: Microblogs, Medical Records and Crowdsourcing},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bhattacharya0MYS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Session 

#### Overview of the TREC 2011 Session Track

_Evangelos Kanoulas, Mark M. Hall, Paul D. Clough, Ben Carterette, Mark Sanderson_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/SESSION.OVERVIEW.2011.pdf](http://trec.nist.gov/pubs/trec20/papers/SESSION.OVERVIEW.2011.pdf)
??? abstract "Abstract"
	
	The TREC Session track ran for the second time in 2011. The track has the primary goal of providing test collections and evaluation measures for studying information retrieval over user sessions rather than one-time queries. These test collections are meant to be portable, reusable, statistically powerful, and open to anyone that wishes to work on the problem of retrieval over sessions. The second year has seen a near-complete overhaul of the track in terms of topic design, session data, and experimental evaluation. The changes are: 1. topics were formed from real user sessions with a search engine, and include queries, retrieved results, clicks, and dwell times; 2. retrieval tasks designed to study the effect of using increasing amounts of user data on retrieval effectiveness for the mth query in a session; 3. subtopic relevance judgments similar to the Web track diversity task. We believe the resulting test collection better models the interaction between system and user, though there is certainly still room for improvement. This overview is organized as follows: in Section 2 we describe the tasks participants were to perform. In Section 3 we describe the corpus, topics, and sessions that comprise the test collection. Section 4 gives some information about submitted runs. In Section 5 we describe relevance judging and evaluation measures, and Sections 6 and 7 present evaluation results and analysis. We conclude in Section 8 with some directions for the 2012 Session track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KanoulasHCCS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/KanoulasHCCS11,
		author = {Evangelos Kanoulas and Mark M. Hall and Paul D. Clough and Ben Carterette and Mark Sanderson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2011 Session Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/SESSION.OVERVIEW.2011.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KanoulasHCCS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RGU-ISTI-Essex at TREC 2011 Session Track

_Ibrahim Adeyanju, Dawei Song, Franco Maria Nardini, M-Dyaa Albakour, Udo Kruschwitz_

- :fontawesome-solid-user-group: **Participant:** [RGU_AutoAdapt](./session/participants.md#rgu_autoadapt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/RGU.session.update.pdf](http://trec.nist.gov/pubs/trec20/papers/RGU.session.update.pdf)
- :material-file-search: **Runs:** [rguPisaSS.RL1](./session/runs.md#rgupisass.rl1) | [rguPisaSS.RL2](./session/runs.md#rgupisass.rl2) | [rguPisaSS.RL3](./session/runs.md#rgupisass.rl3) | [rguPisaSS.RL4](./session/runs.md#rgupisass.rl4) | [rguPisaSST.RL1](./session/runs.md#rgupisasst.rl1) | [rguPisaSST.RL2](./session/runs.md#rgupisasst.rl2) | [rguPisaSST.RL3](./session/runs.md#rgupisasst.rl3) | [rguPisaSST.RL4](./session/runs.md#rgupisasst.rl4) | [rguBase.RL1](./session/runs.md#rgubase.rl1) | [rguBase.RL2](./session/runs.md#rgubase.rl2) | [rguBase.RL3](./session/runs.md#rgubase.rl3) | [rguBase.RL4](./session/runs.md#rgubase.rl4)

??? abstract "Abstract"
	
	Mining query recommendation from query logs has attracted a lot of attention in recent years. We propose to use query recommendations extracted from the logs of a web search engine to solve the session track tasks. The runs are obtained by using the Search Shortcuts recommender system. The Search Shortcuts technique uses an inverted index and the concept of “successful sessions” present in a web search engine's query log to produce effective recommendations for both frequent and rare/unseen queries. We adapt the above technique as a query expansion tool and use it to expand the given queries for Session Track at TREC 2011. The expansion is generated by using a method which aims to consider all past queries in the session. The expansion terms obtained are then used to build a global, uniformly weighted, representation of the user session (RL2). Furthermore, the expansion terms are then combined with a ranked list of results in order to boost terms appearing more frequently in the final results lists (RL3). Finally, we also integrate dwell times and the weighting method obtained taking both result lists and clicks into account for assigning weights to the terms to expand the final query of the session. In addition to that, we submitted a baseline run. It is based on the observation that using the term “wikipedia” to expand the query resulted in a better retrieval performance for the tasks at last year's session track at TREC 2010.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AdeyanjuSNAK11.bib) "
	```
	@inproceedings{DBLP:conf/trec/AdeyanjuSNAK11,
		author = {Ibrahim Adeyanju and Dawei Song and Franco Maria Nardini and M{-}Dyaa Albakour and Udo Kruschwitz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {RGU-ISTI-Essex at {TREC} 2011 Session Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/RGU.session.update.pdf},
		timestamp = {Wed, 03 Feb 2021 08:31:23 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AdeyanjuSNAK11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Essex at the TREC 2011 Session Track

_M-Dyaa Albakour, Udo Kruschwitz, Brendan Neville, Deirdre Lungley, Maria Fasli, Nikolaos Nanas_

- :fontawesome-solid-user-group: **Participant:** [essexuni](./session/participants.md#essexuni)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/essexuni.session.update.pdf](http://trec.nist.gov/pubs/trec20/papers/essexuni.session.update.pdf)
- :material-file-search: **Runs:** [essexAnchor.RL1](./session/runs.md#essexanchor.rl1) | [essexNooPos.RL1](./session/runs.md#essexnoopos.rl1) | [essexNooPos.RL2](./session/runs.md#essexnoopos.rl2) | [essexNooPos.RL3](./session/runs.md#essexnoopos.rl3) | [essexNooPos.RL4](./session/runs.md#essexnoopos.rl4) | [essexNooNeg.RL1](./session/runs.md#essexnooneg.rl1) | [essexNooNeg.RL2](./session/runs.md#essexnooneg.rl2) | [essexNooNeg.RL3](./session/runs.md#essexnooneg.rl3) | [essexNooNeg.RL4](./session/runs.md#essexnooneg.rl4) | [essexAnchor.RL2](./session/runs.md#essexanchor.rl2) | [essexAnchor.RL3](./session/runs.md#essexanchor.rl3) | [essexAnchor.RL4](./session/runs.md#essexanchor.rl4)

??? abstract "Abstract"
	
	This paper provides an overview of the experiments we carried out at the TREC 2011 Session Track. We propose two different approaches to tackle the task introduced this year. The first one relies on a biologically inspired adaptive model for information filtering to build a user profile of multiple topics of interests throughout the session. The learnt profile is then exploited in the retrieval process. The second approach is an extension of our anchor log technique we proposed in the previous year. We use the anchor logs to simulate queries in order to derive query expansions that are relevant to user information needs throughout the session.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlbakourKNLFN11.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlbakourKNLFN11,
		author = {M{-}Dyaa Albakour and Udo Kruschwitz and Brendan Neville and Deirdre Lungley and Maria Fasli and Nikolaos Nanas},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Essex at the {TREC} 2011 Session Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/essexuni.session.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlbakourKNLFN11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Implicit Feedback and Document Filtering for Retrieval Over Query  Sessions

_Ben Carterette, Praveen Chandar_

- :fontawesome-solid-user-group: **Participant:** [udel](./session/participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/udel.session.pdf](http://trec.nist.gov/pubs/trec20/papers/udel.session.pdf)
- :material-file-search: **Runs:** [udelASFe1new.RL1](./session/runs.md#udelasfe1new.rl1) | [udelASFe1new.RL2](./session/runs.md#udelasfe1new.rl2) | [udelASFe1new.RL3](./session/runs.md#udelasfe1new.rl3) | [udelASFe1new.RL4](./session/runs.md#udelasfe1new.rl4) | [udelBe2.RL1](./session/runs.md#udelbe2.rl1) | [udelBe2.RL2](./session/runs.md#udelbe2.rl2) | [udelBe2.RL3](./session/runs.md#udelbe2.rl3) | [udelWPmnz.RL1](./session/runs.md#udelwpmnz.rl1) | [udelWPmnz.RL2](./session/runs.md#udelwpmnz.rl2) | [udelWPmnz.RL3](./session/runs.md#udelwpmnz.rl3) | [udelWPmnz.RL4](./session/runs.md#udelwpmnz.rl4) | [udelBe2.RL4](./session/runs.md#udelbe2.rl4)

??? abstract "Abstract"
	
	The IR Lab at the University of Delaware participated in the 2011 Sessions track. The Sessions track features sequences of queries q 1 , ..., qm , with only q m being the subject for automatic retrieval. There are four separate experimental conditions for q m , each with a greater amount of data about user/system interaction for prior queries: 1. RL1: no interaction information; q m only. 2. RL2: previous queries q 1 , ..., qm−1 known to the system. 3. RL3: previous queries and retrieved results known to the system. 4. RL4: previous queries, retrieved results, and clicks on retrieved results known to the system. We used the different experimental conditions in the track to explore three research questions: 1. the effect of simple implicit feedback on retrieval results; 2. the effect of corpus filters on retrieval results; 3. the effect of duplicate detection and removal on retrieval results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CarteretteC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/CarteretteC11,
		author = {Ben Carterette and Praveen Chandar},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Implicit Feedback and Document Filtering for Retrieval Over Query Sessions},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/udel.session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CarteretteC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at the TREC 2011 Session Track

_Matthias Hagen, Jan Graßegger, Maximilian Michel, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./session/participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/Webis.session.update.pdf](http://trec.nist.gov/pubs/trec20/papers/Webis.session.update.pdf)
- :material-file-search: **Runs:** [webis11cnb.RL1](./session/runs.md#webis11cnb.rl1) | [webis11cnb.RL2](./session/runs.md#webis11cnb.rl2) | [webis11cnb.RL3](./session/runs.md#webis11cnb.rl3) | [webis11ind.RL1](./session/runs.md#webis11ind.rl1) | [webis11cnb.RL4](./session/runs.md#webis11cnb.rl4) | [webis11cnw.RL1](./session/runs.md#webis11cnw.rl1) | [webis11cnw.RL2](./session/runs.md#webis11cnw.rl2) | [webis11cnw.RL3](./session/runs.md#webis11cnw.rl3) | [webis11ind.RL2](./session/runs.md#webis11ind.rl2) | [webis11cnw.RL4](./session/runs.md#webis11cnw.rl4) | [webis11ind.RL3](./session/runs.md#webis11ind.rl3) | [webis11ind.RL4](./session/runs.md#webis11ind.rl4)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2011 Sessions track with an extended version of our last year's approach [HSV10]. The basic idea can be described as a conservative query expansion based on terms used in previous queries or terms contained in clicked snippets. Furthermore, a query's result set is reduced by removing documents shown for previous queries or documents containing important terms from non- clicked snippets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenGMS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenGMS11,
		author = {Matthias Hagen and Jan Gra{\ss}egger and Maximilian Michel and Benno Stein},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Webis at the {TREC} 2011 Session Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/Webis.session.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenGMS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at the TREC 2011 Session Track

_Bouke Huurnink, Richard Berendsen, Katja Hofmann, Edgar Meij, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UvA](./session/participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UvA.session.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UvA.session.update.pdf)
- :material-file-search: **Runs:** [UvAmodeling.RL1](./session/runs.md#uvamodeling.rl1) | [UvAmodeling.RL2](./session/runs.md#uvamodeling.rl2) | [UvAsemantic.RL1](./session/runs.md#uvasemantic.rl1) | [UvAmodeling.RL3](./session/runs.md#uvamodeling.rl3) | [UvAsemantic.RL2](./session/runs.md#uvasemantic.rl2) | [UvAmodeling.RL4](./session/runs.md#uvamodeling.rl4) | [UvAsemantic.RL3](./session/runs.md#uvasemantic.rl3) | [UvAsemantic.RL4](./session/runs.md#uvasemantic.rl4) | [UvAlearning.RL2](./session/runs.md#uvalearning.rl2) | [UvAlearning.RL3](./session/runs.md#uvalearning.rl3) | [UvAlearning.RL4](./session/runs.md#uvalearning.rl4) | [UvAlearning.RL1](./session/runs.md#uvalearning.rl1)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's ILPS group in the Session track at TREC 2011.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuurninkBHMR11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuurninkBHMR11,
		author = {Bouke Huurnink and Richard Berendsen and Katja Hofmann and Edgar Meij and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at the {TREC} 2011 Session Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UvA.session.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HuurninkBHMR11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PITT at TREC 2011 Session Track

_Jiepu Jiang, Shuguang Han, Jia Wu, Daqing He_

- :fontawesome-solid-user-group: **Participant:** [PITTSIS](./session/participants.md#pittsis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/PITTSIS.session.update.pdf](http://trec.nist.gov/pubs/trec20/papers/PITTSIS.session.update.pdf)
- :material-file-search: **Runs:** [PITTSIS.RL1](./session/runs.md#pittsis.rl1) | [PITTSIS.RL2](./session/runs.md#pittsis.rl2) | [PITTSIS.RL3](./session/runs.md#pittsis.rl3) | [PITTSIS.RL4](./session/runs.md#pittsis.rl4)

??? abstract "Abstract"
	
	In this paper, we introduce our approaches for TREC 2011 session track. Our approaches focus on combining different query language models to model information needs in a search session. In RL1 stage, we build ad hoc retrieval system using sequential dependence model (SDM) on current query. In RL2 stage, we build query language models by combining SDM features (e.g. single term, ordered phrase, and unordered phrase) in both current query and previous queries in the session, which can significantly improve search performance. In RL3 and RL4, we combine query model in RL2 with two different pseudo-relevance feedback query models: in RL3, we use top ranked Wikipedia documents from RL2's results as pseudo-relevant documents; in RL4, snippets of the documents clicked by users in a search session are used. Our evaluation results indicate: texts of previous queries in a session are effective resources for estimating query models and improving search performance; mixing query model in RL2 with the query model estimated using click-through data (in RL4) can improve performance in evaluation setting that considers all subtopics, but no improvement is observed in evaluation setting that considers the only subtopic of current query; our methods of mixing query model in RL2 with query model in RL3 did not improve search performance over RL2 in any of the two evaluation settings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangHWH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangHWH11,
		author = {Jiepu Jiang and Shuguang Han and Jia Wu and Daqing He},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PITT} at {TREC} 2011 Session Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/PITTSIS.session.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangHWH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at TREC 2011 Session Track

_Lorena Leal Bando, Sadegh Kharazmi, Jasbir Dhaliwal, Mark Sanderson, Falk Scholer, Sargol Sadeghi, Fahad Alahmari_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./session/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/RMIT.session.update.pdf](http://trec.nist.gov/pubs/trec20/papers/RMIT.session.update.pdf)
- :material-file-search: **Runs:** [RMIT1.RL1](./session/runs.md#rmit1.rl1) | [RMIT2.RL1](./session/runs.md#rmit2.rl1) | [RMIT3.RL1](./session/runs.md#rmit3.rl1) | [RMIT1.RL2](./session/runs.md#rmit1.rl2) | [RMIT2.RL2](./session/runs.md#rmit2.rl2) | [RMIT3.RL2](./session/runs.md#rmit3.rl2) | [RMIT1.RL3](./session/runs.md#rmit1.rl3) | [RMIT2.RL3](./session/runs.md#rmit2.rl3) | [RMIT3.RL3](./session/runs.md#rmit3.rl3) | [RMIT1.RL4](./session/runs.md#rmit1.rl4) | [RMIT2.RL4](./session/runs.md#rmit2.rl4) | [RMIT3.RL4](./session/runs.md#rmit3.rl4)

??? abstract "Abstract"
	
	The 2011 Session track aims to study retrieval system performance by pro- viding different components in a search session. We report on experiments and results based on query expansion techniques when lists of results are provided with or without clicked information. In contrast, a bag-of-words approach is employed as a baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LealKDSSSA11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LealKDSSSA11,
		author = {Lorena Leal Bando and Sadegh Kharazmi and Jasbir Dhaliwal and Mark Sanderson and Falk Scholer and Sargol Sadeghi and Fahad Alahmari},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} at {TREC} 2011 Session Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/RMIT.session.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LealKDSSSA11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at the Session Track in TREC 2011

_Wenfei Liu, Hongfei Lin, Yunlong Ma, Tianshu Chang_

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./session/participants.md#dutir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/DUTIR.session.pdf](http://trec.nist.gov/pubs/trec20/papers/DUTIR.session.pdf)
- :material-file-search: **Runs:** [DUTIR2011A.RL1](./session/runs.md#dutir2011a.rl1) | [DUTIR2011A.RL2](./session/runs.md#dutir2011a.rl2) | [DUTIR2011A.RL3](./session/runs.md#dutir2011a.rl3) | [DUTIR2011A.RL4](./session/runs.md#dutir2011a.rl4)

??? abstract "Abstract"
	
	This paper presents the DUTIR submission to TREC 2011 Session Track, the task is to test whether systems can improve their performance for a given query by using previous queries and user interactions with the retrieval system. We use language model as the basic retrieval model. Query Expansion is applied to reformulate the original query. Some other technologies like Pseudo Relevance Feedback (PRF) are also applied. The results show that our methods are effective, but the results of Query Expansion method using previous queries and user interactions are unanticipated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuLMC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuLMC11,
		author = {Wenfei Liu and Hongfei Lin and Yunlong Ma and Tianshu Chang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at the Session Track in {TREC} 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/DUTIR.session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuLMC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers at the TREC 2011 Session Track

_Chang Liu, Si Sun, Michael J. Cole, Nicholas J. Belkin_

- :fontawesome-solid-user-group: **Participant:** [SCI_TREC_2011](./session/participants.md#sci_trec_2011)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/SCI_TREC_2011.session.pdf](http://trec.nist.gov/pubs/trec20/papers/SCI_TREC_2011.session.pdf)
- :material-file-search: **Runs:** [Rgposneg.RL1](./session/runs.md#rgposneg.rl1) | [Rgposneg.RL2](./session/runs.md#rgposneg.rl2) | [Rgposneg.RL3](./session/runs.md#rgposneg.rl3) | [Rgposneg.RL4](./session/runs.md#rgposneg.rl4) | [Rspos.RL1](./session/runs.md#rspos.rl1) | [Rspos.RL2](./session/runs.md#rspos.rl2) | [Rspos.RL3](./session/runs.md#rspos.rl3) | [Rspos.RL4](./session/runs.md#rspos.rl4) | [Rsposneg.RL1](./session/runs.md#rsposneg.rl1) | [Rsposneg.RL2](./session/runs.md#rsposneg.rl2) | [Rsposneg.RL3](./session/runs.md#rsposneg.rl3) | [Rsposneg.RL4](./session/runs.md#rsposneg.rl4)

??? abstract "Abstract"
	
	At Rutgers, we approached the Session Track task as an issue of personalization, based on both the behaviors exhibited by the searcher during the course of an information-seeking episode, and a classification of the task that led the person to engage in information-seeking behavior. Our general approach is described in detail at the Web site of our project, and in the papers available there (http://comminfo.rutgers.edu/imls/poodle); in this section, we give an overview of our approach and how we applied results from our previous studies to the TREC 2011 Session Track. Subsequent sections give details of how we actually did things, our results, and our conclusions about the results. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuSCB11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuSCB11,
		author = {Chang Liu and Si Sun and Michael J. Cole and Nicholas J. Belkin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Rutgers at the {TREC} 2011 Session Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/SCI\_TREC\_2011.session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuSCB11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BUPT_WILDCAT at TREC 2011 Session Track

_Tang Liu, Chuang Zhang, Yasi Gao, Wenjun Xiao, Hao Huang_

- :fontawesome-solid-user-group: **Participant:** [BUPT_WILDCAT](./session/participants.md#bupt_wildcat)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/BUPT_WILDCAT.session.update.pdf](http://trec.nist.gov/pubs/trec20/papers/BUPT_WILDCAT.session.update.pdf)
- :material-file-search: **Runs:** [wildcat3.RL2](./session/runs.md#wildcat3.rl2) | [wildcat2.RL1](./session/runs.md#wildcat2.rl1) | [wildcat2.RL3](./session/runs.md#wildcat2.rl3) | [wildcat3.RL3](./session/runs.md#wildcat3.rl3) | [wildcat3.RL1](./session/runs.md#wildcat3.rl1) | [wildcat2.RL4](./session/runs.md#wildcat2.rl4) | [wildcat2.RL2](./session/runs.md#wildcat2.rl2) | [wildcat1.RL3](./session/runs.md#wildcat1.rl3) | [wildcat1.RL4](./session/runs.md#wildcat1.rl4) | [wildcat1.RL2](./session/runs.md#wildcat1.rl2) | [wildcat1.RL1](./session/runs.md#wildcat1.rl1) | [wildcat3.RL4](./session/runs.md#wildcat3.rl4)

??? abstract "Abstract"
	
	his paper is an overview of the runs carried out at TREC 2011 Session track, which proposes several approaches to improve the retrieval performance over one session including the search model based on user behavior, VSM_meta similarity model, optimization based on history ranked lists, optimization based on user‟s attention time and anchor log. The evaluation results show that our implementations are effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuZGXH11.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuZGXH11,
		author = {Tang Liu and Chuang Zhang and Yasi Gao and Wenjun Xiao and Hao Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BUPT{\_}WILDCAT at {TREC} 2011 Session Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/BUPT\_WILDCAT.session.update.pdf},
		timestamp = {Wed, 14 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LiuZGXH11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Session Track TREC 2011

_Mingxhuan Wei, Yuanhai Xue, Chen Xu, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./session/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/ICTNET.session.pdf](http://trec.nist.gov/pubs/trec20/papers/ICTNET.session.pdf)
- :material-file-search: **Runs:** [ICTNET11SER1.RL1](./session/runs.md#ictnet11ser1.rl1) | [ICTNET11SER1.RL2](./session/runs.md#ictnet11ser1.rl2) | [ICTNET11SER1.RL3](./session/runs.md#ictnet11ser1.rl3) | [ICTNET11SER1.RL4](./session/runs.md#ictnet11ser1.rl4) | [ICTNET11SER2.RL1](./session/runs.md#ictnet11ser2.rl1) | [ICTNET11SER2.RL2](./session/runs.md#ictnet11ser2.rl2) | [ICTNET11SER2.RL3](./session/runs.md#ictnet11ser2.rl3) | [ICTNET11SER2.RL4](./session/runs.md#ictnet11ser2.rl4) | [ICTNET11SER3.RL1](./session/runs.md#ictnet11ser3.rl1) | [ICTNET11SER3.RL2](./session/runs.md#ictnet11ser3.rl2) | [ICTNET11SER3.RL3](./session/runs.md#ictnet11ser3.rl3) | [ICTNET11SER3.RL4](./session/runs.md#ictnet11ser3.rl4)

??? abstract "Abstract"
	
	Following several methods of some past publications, among these we refined an important idea that related queries could be derived from queries submitted within the same session. As the browsers not just provide the previous queries but more informations,so we could use these informations to build a expert database for a special user, base on the database ,we could analysis some fixed behaviors of the user, so then forecast what information he really wants, rerank the results from search engine and give them to the user finally. The whole process is the session trec works on:Providing the really information to different user, so we can make the search engine more efficient and smarter. The rest of paper is structured as follows. In section 2 we discuss the ideal of session type. In section 3 we descripte the classification we used . In section 4 we explain the experiment and result we submitted ,Finally we make a brief conclusion and a plan for the future work.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WeiXXYLC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WeiXXYLC11,
		author = {Mingxhuan Wei and Yuanhai Xue and Chen Xu and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Session Track {TREC} 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/ICTNET.session.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WeiXXYLC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI at TREC 2011: Session, Web, and Medical

_Jiyin He, Vera Hollink, Corrado Boscarino, Arjen P. de Vries, Roberto Cornacchia_

- :fontawesome-solid-user-group: **Participant:** [CWI](./session/participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/CWI.session.web.medical.pdf](http://trec.nist.gov/pubs/trec20/papers/CWI.session.web.medical.pdf)
- :material-file-search: **Runs:** [CWIpostRW.RL1](./session/runs.md#cwipostrw.rl1) | [CWIpostRW.RL2](./session/runs.md#cwipostrw.rl2) | [CWIpostRW.RL3](./session/runs.md#cwipostrw.rl3) | [CWIpostRW.RL4](./session/runs.md#cwipostrw.rl4) | [CWIrun1.RL1](./session/runs.md#cwirun1.rl1) | [CWIrun1.RL2](./session/runs.md#cwirun1.rl2) | [CWIrun1.RL3](./session/runs.md#cwirun1.rl3) | [CWIrun1.RL4](./session/runs.md#cwirun1.rl4) | [CWIrun2.RL1](./session/runs.md#cwirun2.rl1) | [CWIrun2.RL2](./session/runs.md#cwirun2.rl2) | [CWIrun2.RL3](./session/runs.md#cwirun2.rl3) | [CWIrun2.RL4](./session/runs.md#cwirun2.rl4)

??? abstract "Abstract"
	
	We report on the participation of the Interactive Information Access group of the CWI Amsterdam in the web, session, and medical track at TREC 2011. In the web track we focus on the diversity task. We find that cluster-based subtopic modeling approaches improve diversification performance compared to a non-cluster-based subtopic modeling approach. While gain was observed on previous years' topic sets, diversification with the proposed approaches hurt the performance when compared to a non-diversified baseline run on this year's topic set. In the session track, we examine the effects of differentiating between 'good' and 'bad' users. We find that differentiation is useful as the use of search history appears to be mainly effective when the search is not going well. However, our current strategy is not effective for 'good' users. In addition, we studied the use of random walks on query graphs for formulating session history as search queries, but results are inconclusive. In the medical track, we found that the use of medical background resources for query expansion leads to small improvements in retrieval performance. Such resources appear to be especially useful to promote early precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeHBVC11.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeHBVC11,
		author = {Jiyin He and Vera Hollink and Corrado Boscarino and Arjen P. de Vries and Roberto Cornacchia},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CWI} at {TREC} 2011: Session, Web, and Medical},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/CWI.session.web.medical.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeHBVC11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Crowdsourcing 

#### MSRC at TREC 2011 Crowdsourcing Track

_Paul Bennett, Ece Kamar, Gabriella Kazai_

- :fontawesome-solid-user-group: **Participant:** [MSRC](./crowd/participants.md#msrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/MSRC.crowdsourcing.update.pdf](http://trec.nist.gov/pubs/trec20/papers/MSRC.crowdsourcing.update.pdf)

??? abstract "Abstract"
	
	Crowdsourcing useful data, such as reliable relevance labels for pairs of topics and documents, requires a multidisciplinary approach that spans aspects such as user interface and interaction design, incentives, crowd engagement and management, and spam detection and filtering. Research has shown that the design of a crowdsourcing task can significantly impact the quality of the obtained data, where the geographic location of crowd workers was found to be a main indicator of quality. Following this, for the Assessment task of the TREC crowdsourcing track, we designed HITs to minimize attracting spam workers, and restricted participation to workers in the US. As an incentive, we included the possibility of a bonus pay of $5 for the best performing workers. When crowdsourcing relevance judgments, multiple judgments are typically obtained to provide greater certainty as to the true label. However, combining these judgments by a simple majority vote not only has the flawed underlying assumption that each assessor has comparable accuracy but also ignores the impact of topic specific effects (e.g. the amount of topic-expertise needed to accurately judge). We provide a simple probabilistic framework for predicting true relevance from crowdsourced judgments and explore variations that condition on worker and topic. In particular, we focus on the topic conditional model that was our primary submission for the Consensus task of the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BennettKK11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BennettKK11,
		author = {Paul Bennett and Ece Kamar and Gabriella Kazai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{MSRC} at {TREC} 2011 Crowdsourcing Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/MSRC.crowdsourcing.update.pdf},
		timestamp = {Thu, 28 Apr 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BennettKK11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Iowa at TREC 2011: Microblogs, Medical Records  and Crowdsourcing

_Sanmitra Bhattacharya, Christopher G. Harris, Yelena Mejova, Chao Yang, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [UIowaS](./crowd/participants.md#uiowas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf)

??? abstract "Abstract"
	
	The Text Retrieval and Text Mining group at the University of Iowa participated in three tracks, all new tracks introduced this year: Microblog, Medical Records (Med) and Crowdsourcing. Details of our strategies are provided in this paper. Overall our effort has been fruitful in that we have been able to understand more about the nature of medical records and Twitter messages, and also the merits and challenges of working with games as a framework for gathering relevance judgments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bhattacharya0MYS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bhattacharya0MYS11,
		author = {Sanmitra Bhattacharya and Christopher G. Harris and Yelena Mejova and Chao Yang and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Iowa at {TREC} 2011: Microblogs, Medical Records and Crowdsourcing},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bhattacharya0MYS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Hierarchical Bayesian Model of Crowdsourced Relevance Coding

_Bob Carpenter_

- :fontawesome-solid-user-group: **Participant:** [LingPipe](./crowd/participants.md#lingpipe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/LingPipe.crowdsourcing.pdf](http://trec.nist.gov/pubs/trec20/papers/LingPipe.crowdsourcing.pdf)
- :material-file-search: **Runs:** [LingPipeSemi](./crowd/runs.md#lingpipesemi) | [LingPipeUn](./crowd/runs.md#lingpipeun) | [LingPipeSBin](./crowd/runs.md#lingpipesbin)

??? abstract "Abstract"
	
	We apply a generative probabilistic model of noisy crowdsourced coding to overlapping relevance judgments for documents in several topics (queries). We demonstrate the model's utility for Task 2 of the 2011 TREC Crowdsourcing Track (Karzai and Lease 2011). Our model extends Dawid and Skene's (1979) approach to inferring gold standards from noisy coding in several ways: we add a hierarchical model of prevalence of relevant documents in multiple topics (queries), semi-supervision using known gold labels, and hierarchically modeled priors for coder sensitivity and specificity. We also replace Dawid and Skene's maximum likelihood point estimates with full Bayesian inference using Gibbs sampling and generalize their full-panel design in which every coder labels every document to a fully ad hoc design in which a coder may label each document zero, one or more times.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Carpenter11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Carpenter11,
		author = {Bob Carpenter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Hierarchical Bayesian Model of Crowdsourced Relevance Coding},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/LingPipe.crowdsourcing.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Carpenter11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### GeAnn at the TREC 2011 Crowdsourcing Track

_Carsten Eickhoff, Christopher G. Harris, Padmini Srinivasan, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [GeAnn](./crowd/participants.md#geann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/GeAnn.crowdsourcing.pdf](http://trec.nist.gov/pubs/trec20/papers/GeAnn.crowdsourcing.pdf)
- :material-file-search: **Runs:** [G6T1R1](./crowd/runs.md#g6t1r1) | [G6T2R1](./crowd/runs.md#g6t2r1) | [G6T2R2](./crowd/runs.md#g6t2r2) | [G6T2R3](./crowd/runs.md#g6t2r3)

??? abstract "Abstract"
	
	Relevance assessments of information retrieval results are often created by domain experts. This expertise is typically expensive in terms of money or personal effort. The TREC 2011 crowdsourcing track aims to evaluate different strategies of crowdsourcing relevance judgements. This work describes the joint participation of Delft University of Technology and The University of Iowa, using GeAnn, a term association game, we generate relevance judgements in an engaging way that encourages quality submissions, which otherwise would have to be motivated through rigid quality control mechanisms and additional incentives such as higher monetary rewards.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Eickhoff0SV11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Eickhoff0SV11,
		author = {Carsten Eickhoff and Christopher G. Harris and Padmini Srinivasan and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {GeAnn at the {TREC} 2011 Crowdsourcing Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/GeAnn.crowdsourcing.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Eickhoff0SV11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at the Crowdsourcing Track of TREC 2011

_Matthias Petri, Mark Sanderson, Falk Scholer_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./crowd/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/RMIT.crowdsourcing.pdf](http://trec.nist.gov/pubs/trec20/papers/RMIT.crowdsourcing.pdf)
- :material-file-search: **Runs:** [RMITT1](./crowd/runs.md#rmitt1)

??? abstract "Abstract"
	
	In this paper we describe our submission to the crowdsourcing track of TREC 2011. We first describe our crowdsourcing environment. Next we evaluate our approach and discuss our results. We conclude with a discussion of problems encountered during our participation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PetriSS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/PetriSS11,
		author = {Matthias Petri and Mark Sanderson and Falk Scholer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} at the Crowdsourcing Track of {TREC} 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/RMIT.crowdsourcing.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PetriSS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Crowdsourcing with a Crowd of One and Other TREC 2011 Crowdsourcing  and Web Track Experiments

_Mark D. Smucker_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./crowd/participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UWaterlooMDS.crowd.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UWaterlooMDS.crowd.update.pdf)
- :material-file-search: **Runs:** [UWatCS1Human](./crowd/runs.md#uwatcs1human) | [UWatCS2Semi](./crowd/runs.md#uwatcs2semi) | [UWatCS2Unsup](./crowd/runs.md#uwatcs2unsup)

??? abstract "Abstract"
	
	Our submissions to the Crowdsourcing and Web tracks emphasized simplicity in either method, construction or both. Based on preliminary results, we found that if the number of relevance assessments is low, researchers may be better off “self-sourcing” the assessments, i.e. performing the relevance assessments themselves, rather than crowdsourcing the work. For the Crowdsourcing consensus task, we found that a simple weighted majority vote with iteratively refined workers' quality as measured by d′ (d-prime) performed slightly above the median on the gold test set. Finally, we submitted easy to construct runs to the Web ad-hoc track which had P@10 scores above the median on a majority of the topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Smucker11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Smucker11,
		author = {Mark D. Smucker},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Crowdsourcing with a Crowd of One and Other {TREC} 2011 Crowdsourcing and Web Track Experiments},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UWaterlooMDS.crowd.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Smucker11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University Carlos III of Madrid at TREC 2011 Crowdsourcing  Track

_Julián Urbano, Mónica Marrero, Diego Martín, Jorge Morato, Karina Robles, Juan Lloréns_

- :fontawesome-solid-user-group: **Participant:** [uc3m](./crowd/participants.md#uc3m)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uc3m.crowd.update.pdf](http://trec.nist.gov/pubs/trec20/papers/uc3m.crowd.update.pdf)
- :material-file-search: **Runs:** [uc3m.graded](./crowd/runs.md#uc3m.graded) | [uc3m.slider](./crowd/runs.md#uc3m.slider) | [uc3m.hterms](./crowd/runs.md#uc3m.hterms) | [uc3m.rule](./crowd/runs.md#uc3m.rule) | [uc3m.svn](./crowd/runs.md#uc3m.svn) | [uc3m.wordnet](./crowd/runs.md#uc3m.wordnet)

??? abstract "Abstract"
	
	This paper describes the participation of the uc3m team in both tasks of the TREC 2011 Crowdsourcing Track. For the first task we submitted three runs that used Amazon Mechanical Turk: one where workers made relevance judgments based on a 3-point scale, and two similar runs where workers provided an explicit ranking of documents. All three runs implemented a quality control mechanism at the task level based on a simple reading comprehension test. For the second task we also submitted three runs: one with a stepwise execution of the GetAnotherLabel algorithm and two others with a rule-based and a SVM-based model. According to the NIST gold labels, our runs performed very well in both tasks, ranking at the top for most measures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UrbanoMMMRL11.bib) "
	```
	@inproceedings{DBLP:conf/trec/UrbanoMMMRL11,
		author = {Juli{\'{a}}n Urbano and M{\'{o}}nica Marrero and Diego Mart{\'{\i}}n and Jorge Morato and Karina Robles and Juan Llor{\'{e}}ns},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University Carlos {III} of Madrid at {TREC} 2011 Crowdsourcing Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uc3m.crowd.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/UrbanoMMMRL11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Managing the Quality of Large-Scale Crowdsourcing

_Jeroen B. P. Vuurens, Carsten Eickhoff, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [TUD_DMIR](./crowd/participants.md#tud_dmir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/TUD_DMIR.crowdsourcing.4-20update.pdf](http://trec.nist.gov/pubs/trec20/papers/TUD_DMIR.crowdsourcing.4-20update.pdf)
- :material-file-search: **Runs:** [DMIR1](./crowd/runs.md#dmir1) | [DMIR2](./crowd/runs.md#dmir2) | [DMIR3](./crowd/runs.md#dmir3)

??? abstract "Abstract"
	
	Crowdsourcing can be used to obtain relevance judgments needed for the evaluation of information retrieval systems. However, the quality of crowdsourced relevance judgments may be questionable; a substantial amount of workers appear to spam HITs in order to maximize their hourly wages, and workers may know less than expert annotators about the topic being queried. The task for the TREC 2011 Crowdsourcing track was to obtain high-quality relevance judgments. The quality of obtained annotations is improved by removing random judgments and aggregating multiple annotations per query-document pair. We conclude that crowdsourcing can be used as a feasible alternative to expert annotations, based on the estimated proportions of correctly judged query-document pairs in the crowdsourced relevance judgments and previous TREC qrels.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VuurensEV11.bib) "
	```
	@inproceedings{DBLP:conf/trec/VuurensEV11,
		author = {Jeroen B. P. Vuurens and Carsten Eickhoff and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Managing the Quality of Large-Scale Crowdsourcing},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/TUD\_DMIR.crowdsourcing.4-20update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VuurensEV11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow (qirdcsuog) at TREC Crowdsourcing 2011: TurkRank-Network-based  Worker Ranking in Crowdsourcing

_Stewart Whiting, Jesus A. Rodriguez Perez, Guido Zuccon, Teerapong Leelanupab, Joemon M. Jose_

- :fontawesome-solid-user-group: **Participant:** [qirdcsuog](./crowd/participants.md#qirdcsuog)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/qirdcsuog.crowd.update.pdf](http://trec.nist.gov/pubs/trec20/papers/qirdcsuog.crowd.update.pdf)
- :material-file-search: **Runs:** [beta0](./crowd/runs.md#beta0) | [beta04](./crowd/runs.md#beta04) | [beta08](./crowd/runs.md#beta08)

??? abstract "Abstract"
	
	For TREC Crowdsourcing 2011 (Stage 2) we propose a network-based approach for assigning an indicative measure of worker trustworthiness in crowdsourced labelling tasks. Workers, the gold standard and worker/gold standard agreements are modelled as a network. For the purpose of worker trustworthiness assignment, a variant of the PageRank algorithm, named TurkRank, is used to adaptively combine evidence that suggests worker trustworthiness, i.e., agreement with other trustworthy co-workers and agreement with the gold standard. A single parameter controls the importance of co-worker agreement versus gold standard agreement. The TurkRank score calculated for each worker is incorporated with a worker-weighted mean label aggregation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WhitingPZLJ11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WhitingPZLJ11,
		author = {Stewart Whiting and Jesus A. Rodriguez Perez and Guido Zuccon and Teerapong Leelanupab and Joemon M. Jose},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow (qirdcsuog) at {TREC} Crowdsourcing 2011: TurkRank-Network-based Worker Ranking in Crowdsourcing},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/qirdcsuog.crowd.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WhitingPZLJ11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BUPT_WILDCAT at TREC Crowdsourcing Track: Crowdsourcing for Relevance  Evaluation

_Tao Xia, Chuang Zhang, Tai Li, Jingjing Xie_

- :fontawesome-solid-user-group: **Participant:** [BUPT_WILDCAT](./crowd/participants.md#bupt_wildcat)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/BUPT_WILDCAT.crowd.new.pdf](http://trec.nist.gov/pubs/trec20/papers/BUPT_WILDCAT.crowd.new.pdf)
- :material-file-search: **Runs:** [BUPTWildCat1](./crowd/runs.md#buptwildcat1) | [BUPTWildCat2](./crowd/runs.md#buptwildcat2) | [wildcatrun](./crowd/runs.md#wildcatrun)

??? abstract "Abstract"
	
	In recent years, crowdsourcing has become an effective method in many fields, such as relecance evaluation. Based on our experiment carried out in Beijing University of Posts and Telecommunications for the TREC 2011 Crowdsourcing track, in this paper we introduce our strategies in recruiting workers, obtaining their relevance and rank juegements and quality control. Then we explain the improved EM algorithm and Gaussian model that we make use of to calculate the consensus of labels. The result shows that our stategies and algorithms are effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XiaZLX11.bib) "
	```
	@inproceedings{DBLP:conf/trec/XiaZLX11,
		author = {Tao Xia and Chuang Zhang and Tai Li and Jingjing Xie},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BUPT{\_}WILDCAT at {TREC} Crowdsourcing Track: Crowdsourcing for Relevance Evaluation},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/BUPT\_WILDCAT.crowd.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XiaZLX11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2011: Experiments with Terrier in  Crowdsourcing, Microblog, and Web Tracks

_Richard McCreadie, Craig Macdonald, Rodrygo L. T. Santos, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./crowd/participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf](http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf)
- :material-file-search: **Runs:** [uogTrP1rg](./crowd/runs.md#uogtrp1rg) | [uogTrP2O4wtr](./crowd/runs.md#uogtrp2o4wtr) | [uogTrP2O4wte](./crowd/runs.md#uogtrp2o4wte) | [uogTrP2O4teh](./crowd/runs.md#uogtrp2o4teh)

??? abstract "Abstract"
	
	In TREC 2011, we focus on tackling the new challenges proposed by the pilot Crowdsourcing and Microblog tracks, using our Terrier Information Retrieval Platform. Meanwhile, we continue to build upon our novel xQuAD framework and data-driven ranking approaches within Terrier to achieve effective and efficient ranking for the TREC Web track. In particular, the aim of our Microblog track participation is the development of a learning to rank approach for filtering within a tweet ranking environment, where tweets are ranked in reverse chronological order. In the Crowdsourcing track, we work to achieve a closer integration between the crowdsourcing marketplaces that are used for relevance assessment, and Terrier, which produces the document rankings to be assessed. Moreover, we focus on generating relevance assessments quickly and at a minimal cost. For the Web track, we enhance the data-driven learning support within Terrier by proposing a novel framework for the fast computation of document features for learning to rank.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMSO11.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMSO11,
		author = {Richard McCreadie and Craig Macdonald and Rodrygo L. T. Santos and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2011: Experiments with Terrier in Crowdsourcing, Microblog, and Web Tracks},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMSO11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

