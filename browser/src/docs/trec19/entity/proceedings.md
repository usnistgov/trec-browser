# Proceedings - Entity 2010 

#### Overview of the TREC 2010 Entity Track

_Krisztian Balog, Pavel Serdyukov, Arjen P. de Vries_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/ENTITY.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec19/papers/ENTITY.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The overall goal of the track is to perform entity-oriented search tasks on the World Wide Web. Many user information needs concern entities (people, organizations, locations, products, ...); these are better answered by returning specific objects instead of just any type of documents. Defining entities on the Web is still an unsolved problem. We settled on representing entities by their homepages, under the assumption that any entity of interest would have at least one homepage. The homepage URL is used as unique identifier. In this scenario, entity ranking corresponds to the task of returning the homepages of entities of a given type, that are relevant to the user's information need (represented as natural language text). We have to also consider that many entity queries could have very large answer sets (e.g., “actors playing in hollywood movies”); extra problematic with corpora the size of ClueWeb. In 2009, we decided therefore that finding associations between entities would be a more challenging one (in terms of modeling) and also a more manageable one (from a test collection building perspective) than finding associations between entities and topics, and defined the Related Entity Finding (REF) task (Balog et al., 2010). Related entity finding requests a ranked list of entities (of a specified type) that engage in a given relationship with a given source entity. REF ran as a pilot in 2009 and is the track's main task in this year; the document collection has been enlarged to the English subset of ClueWeb. We intend to repeat the REF task at least one more time in 2011. One observation from the 2009 edition of the track is that many of the proposed approaches build heavily on Wikipedia and use it as a “semantic backbone”: considering Wikipedia a large repository of entity names and types. Our goal is however not to evaluate entity retrieval over Wikipedia (this task has already been looked at in INEX, and a test collection exists), nor to limit ourselves to the (mostly popular) entities that are present in Wikipedia. As of this year, we are therefore not accepting Wikipedia pages as entity homepages. The issue of combining (noisy) textual material (the Web) with semi-structured data (like Wikipedia or slightly more structured data sources like IMDB) is however an interesting line of research. As many data sources, and in particular those being constructed as so-called Linked Open Data (LOD), are naturally organized around entities, it would be reasonable to examine this problem in the context of entity retrieval. To foster research in this direction, we introduced the new Entity List Completion (ELC) pilot task. ELC is motivated by the same user scenario as REF, but with the main difference that entities are represented by their URIs in a Semantic Web crawl (the Billion Triple Collection). In addition, a small number of example entities (defined by their URIs) are made available as part of the topic definition. Our goal is to turn this pilot task to an “official” task in 2011. In the remainder of the paper we discuss the REF and ELC tasks in detail, in Sections 2 and 3, respectively. We summarize our findings and outline future plans in Section 4.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalogSV10.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalogSV10,
		author = {Krisztian Balog and Pavel Serdyukov and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2010 Entity Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/ENTITY.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BalogSV10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LIA-iSmart at TREC 2010: An Unsupervised Web-Based Approach for  Filtering Answers

_Ludovic Bonnefoy, Patrice Bellot, Michel Benoit_

- :fontawesome-solid-user-group: **Participant:** [LIA_UAPV](./participants.md#lia_uapv)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.avignon.entity.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.avignon.entity.rev.pdf)
- :material-file-search: **Runs:** [LearnDPI](./runs.md#learndpi) | [RanksDivComp](./runs.md#ranksdivcomp) | [Comp](./runs.md#comp) | [Div](./runs.md#div)

??? abstract "Abstract"
	
	Searching for named entities has been the subject of many researches in information retrieval. Our goal in participating in TREC 2010 Entity Ranking track is to look for reconizing any named entity in arbitrary categories and use this to rank candidate named entities. We propose to address the issue by means of a web oriented language modeling approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BonnefoyBB10.bib) "
	```
	@inproceedings{DBLP:conf/trec/BonnefoyBB10,
		author = {Ludovic Bonnefoy and Patrice Bellot and Michel Benoit},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {LIA-iSmart at {TREC} 2010: An Unsupervised Web-Based Approach for Filtering Answers},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.avignon.entity.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BonnefoyBB10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at TREC 2010: Session, Entity and Relevance  Feedback

_Marc Bron, Jiyin He, Katja Hofmann, Edgar Meij, Maarten de Rijke, Manos Tsagkias, Wouter Weerkamp_

- :fontawesome-solid-user-group: **Participant:** [UAms](./participants.md#uams)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam.session.ent.RF.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam.session.ent.RF.rev.pdf)
- :material-file-search: **Runs:** [ilpsM50](./runs.md#ilpsm50) | [ilpsA500](./runs.md#ilpsa500) | [ilpsM50var](./runs.md#ilpsm50var) | [ilpsM50agfil](./runs.md#ilpsm50agfil) | [ilpsSetOL](./runs.md#ilpssetol) | [ilpsSetOLnar](./runs.md#ilpssetolnar)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's ILPS group in the ses- sion, entity, and relevance feedback track at TREC 2010. In the Session Track we explore the use of blind relevance feedback to bias a follow-up query towards or against the topics covered in documents returned to the user in response to the original query. In the Entity Track REF task we experiment with a window size parameter to limit the amount of context considered by the entity co-occurrence models and explore the use of Freebase for type filtering, entity normalization and homepage finding. In the ELC task we use an approach that uses the number of links shared between candidate and example entities to rank candidates. In the Relevance Feedback Track we experiment with a novel model that uses Wikipedia to expand the query language model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BronHHMRTW10.bib) "
	```
	@inproceedings{DBLP:conf/trec/BronHHMRTW10,
		author = {Marc Bron and Jiyin He and Katja Hofmann and Edgar Meij and Maarten de Rijke and Manos Tsagkias and Wouter Weerkamp},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at {TREC} 2010: Session, Entity and Relevance Feedback},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam.session.ent.RF.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BronHHMRTW10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Entity Track TREC 2010

_Lei Cao, Lu Bai, Xueqi Cheng, Jiafeng Guo, Hongbo Xu, Yue Liu, Xiaoming Yu_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.ENTITY.new.pdf](http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.ENTITY.new.pdf)
- :material-file-search: **Runs:** [ICTNETRun1](./runs.md#ictnetrun1)

??? abstract "Abstract"
	
	This paper gives an overview of our work for related entity finding which is proposed in TREC 2010 Entity Track. The goal of the Entity Track is to find the entities relevant to a given query from the web corpus. In this paper, we propose a bipartite graph reinforcement model for entity ranking. As is well known, the entities on the web are embedded not only in the natural language text, but also in the tables and lists. Given a query, both the candidate entities and relevant tables/lists are extracted from web documents. Then the candidate entities extracted from unstructured text are ranked based on a probabilistic model. But the result contains a lot of noise. If some candidate entities are in a relevant table/list, they are more relevant to the given query. And Vice versa, if a table/list contains several candidate entities, it is also more relevant to the query. Based on the above intuition, we construct a bipartite graph and then perform a reinforcement algorithm to re-rank the candidate entities.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaoBCGXLY10.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaoBCGXLY10,
		author = {Lei Cao and Lu Bai and Xueqi Cheng and Jiafeng Guo and Hongbo Xu and Yue Liu and Xiaoming Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Entity Track {TREC} 2010},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/cas-ictnet.ENTITY.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CaoBCGXLY10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Entity List Completion Using Set Expansion Techniques

_Bhavana Bharat Dalvi, Jamie Callan, William W. Cohen_

- :fontawesome-solid-user-group: **Participant:** [CMU_LIRA](./participants.md#cmu_lira)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/carnegie.mellon.univ-lira.ent.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/carnegie.mellon.univ-lira.ent.rev.pdf)
- :material-file-search: **Runs:** [LiraSealClwb](./runs.md#lirasealclwb) | [LiraSealgoog](./runs.md#lirasealgoog)

??? abstract "Abstract"
	
	Set expansion refers to expanding a partial set of “seed” objects into a more complete set. In this paper, we focus on relation and list extraction techniques to perform Entity List Completion task through a two stage retrieval process. First stage takes given query entity and target entity examples as seeds and does set expansion. In second stage, only those candidates who have valid URI in Billion Triple dataset are ranked according to type match with given types. First stage of this system focuses on the recall while second stage tries to improve precision of the outputted list. We submitted the results on the Web as well as ClueWeb09 corpus.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DalviCC10.bib) "
	```
	@inproceedings{DBLP:conf/trec/DalviCC10,
		author = {Bhavana Bharat Dalvi and Jamie Callan and William W. Cohen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Entity List Completion Using Set Expansion Techniques},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/carnegie.mellon.univ-lira.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DalviCC10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Purdue at TREC 2010 Entity Track: A Probabilistic Framework for  Matching Types Between Candidate and Target Entities

_Yi Fang, Luo Si, Naveen Somasundaram, Salman Al-Ansari, Zhengtao Yu, Yantuan Xian_

- :fontawesome-solid-user-group: **Participant:** [Purdue_IR](./participants.md#purdue_ir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/purdue.univ.entity.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/purdue.univ.entity.rev.pdf)
- :material-file-search: **Runs:** [KMR1PU](./runs.md#kmr1pu) | [KMR3PU](./runs.md#kmr3pu) | [KMR5PU](./runs.md#kmr5pu)

??? abstract "Abstract"
	
	This paper gives an overview of our work for the TREC 2010 Entity track. The goal of the TREC Entity track is to study entity-related searches on Web data, which has not been sufficiently addressed in prior research. For both the Related Entity Finding (REF) task and the Entity List Completion (ELC) task in this track, we propose a unified probabilistic framework by incorporating the matching between target entity types and candidate entity types. This framework is motivated by the observation that much more specific type information than the given type can be inferred from the query narratives. These fine-grained types can help narrow down candidate entities. Specific probabilistic models can be derived from this general framework. For the REF task, besides the type matching component, we generally follow our previous work on TREC Entity 2009. For the ELC task, we apply the same framework and the resulting model combines structured document retrieval with type matching.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FangSSAYX10.bib) "
	```
	@inproceedings{DBLP:conf/trec/FangSSAYX10,
		author = {Yi Fang and Luo Si and Naveen Somasundaram and Salman Al{-}Ansari and Zhengtao Yu and Yantuan Xian},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Purdue at {TREC} 2010 Entity Track: {A} Probabilistic Framework for Matching Types Between Candidate and Target Entities},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/purdue.univ.entity.rev.pdf},
		timestamp = {Tue, 17 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FangSSAYX10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ECIR - A Lightweight Approach for Entity-Centric Information Retrieval

_Alexander Hold, Michael Leben, Benjamin Emde, Christoph Thiele, Felix Naumann, Wojciech M. Barczynski, Falk Brauer_

- :fontawesome-solid-user-group: **Participant:** [HPI](./participants.md#hpi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/hasso-plattner-inst.rev.ENTITY.pdf](http://trec.nist.gov/pubs/trec19/papers/hasso-plattner-inst.rev.ENTITY.pdf)
- :material-file-search: **Runs:** [G16](./runs.md#g16) | [G64](./runs.md#g64) | [B64](./runs.md#b64) | [Y64](./runs.md#y64)

??? abstract "Abstract"
	
	This paper describes our system developed for the TREC 2010 Entity track. In particular we study the exploitation of advanced features of different Web search engines to achieve high quality answers for the 'related entity finding'-task. Our system preprocesses a user query using part-of-speech tagging and synonym dictionaries, and generates an enriched keyword query employing advanced features of particular Web search engines. After retrieving a corpus of documents, the system constructs rules to extract candidate entities. Potentially related entities are deduplicated and scored for each document with respect to the distance to the source entity that is defined in the query. Finally, these scores are aggregated across the corpus by incorporating the rank position of a document. For homepage retrieval we further employ advanced features of Web search engines, for instance to retrieve candidate URLs by queries such as 'entity in anchor'. Homepages are ranked by a weighted aggregation of feature vectors. The weight for each individual feature was determined in beforehand using a genetic learning algorithm. We employed a commercial information extraction system as a basis and implemented our system for three different search engines. We discuss our experiments for the different web search engines and elaborate on the lessons learned.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HoldLETNBB10.bib) "
	```
	@inproceedings{DBLP:conf/trec/HoldLETNBB10,
		author = {Alexander Hold and Michael Leben and Benjamin Emde and Christoph Thiele and Felix Naumann and Wojciech M. Barczynski and Falk Brauer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ECIR} - {A} Lightweight Approach for Entity-Centric Information Retrieval},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/hasso-plattner-inst.rev.ENTITY.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HoldLETNBB10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Anchor Text, Spam Filtering and Wikipedia for Web Search and  Entity Ranking

_Jaap Kamps, Rianne Kaptein, Marijn Koolen_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam-kamps.web.ent.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam-kamps.web.ent.rev.pdf)
- :material-file-search: **Runs:** [UAbaseanchB](./runs.md#uabaseanchb) | [UAbaselinkA](./runs.md#uabaselinka) | [UAcatslinkA](./runs.md#uacatslinka) | [UAcatscombB](./runs.md#uacatscombb)

??? abstract "Abstract"
	
	In this paper, we document our efforts in participating to the TREC 2010 Entity Ranking and Web Tracks. We had multiple aims: For the Web Track we wanted to compare the effectiveness of anchor text of the category A and B collections and the impact of global document quality measures such as PageRank and spam scores. We find that documents in ClueWeb09 category B have a higher probability of being retrieved than other documents in category A. In ClueWeb09 category B, spam is mainly an issue for full-text retrieval. Anchor text suffers little from spam. Spam scores can be used to filter spam but also to find key resources. Documents that are least likely to be spam tend to be high-quality results. For the Entity Ranking Track, we use Wikipedia as a pivot to find relevant entities on the Web. Using category information to retrieve entities within Wikipedia leads to large improvements. Although we achieve large improvements over our baseline run that does not use category information, our best scores are still weak. Following the external links on Wikipedia pages to find the homepages of the entities in the ClueWeb collection, works better than searching an anchor text index, and combining the external links with searching an anchor text index.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KampsKK10.bib) "
	```
	@inproceedings{DBLP:conf/trec/KampsKK10,
		author = {Jaap Kamps and Rianne Kaptein and Marijn Koolen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Anchor Text, Spam Filtering and Wikipedia for Web Search and Entity Ranking},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.amsterdam-kamps.web.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KampsKK10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Searching for Entities When Retrieval Meets Extraction

_Qi Li, Daqing He_

- :fontawesome-solid-user-group: **Participant:** [PITTSIS](./participants.md#pittsis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.pittsburgh.entity.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.pittsburgh.entity.rev.pdf)
- :material-file-search: **Runs:** [ValueDoc](./runs.md#valuedoc) | [EntityHP](./runs.md#entityhp) | [YahooEnHP](./runs.md#yahooenhp) | [EntityHP1](./runs.md#entityhp1)

??? abstract "Abstract"
	
	Retrieving entities inside documents instead of documents or web pages themselves has become an active topic in both commercial search systems and academic information retrieval research. Our method of entity retrieval is based on a two-layer retrieval and extraction probability model (TREPM) for integrating document retrieval and entity extraction together. The document retrieval layer finds supporting documents from the corpus, and the entity extraction layer extracts the right entities from those supporting documents. We theoretically demonstrate that the entity extraction problem can be represented as TREPM model. The TREPM model can reduce the overall retrieval complexity while keeping high accuracy of locating target entities. The experiment is based on the document retrieval and entity extraction as well as the overall task. The preliminary results are promising and deserve for further exploration.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiH10.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiH10,
		author = {Qi Li and Daqing He},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Searching for Entities When Retrieval Meets Extraction},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.pittsburgh.entity.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiH10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Related Entity Finding: University of Waterloo at TREC 2010 Entity  Track

_Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooEng](./participants.md#uwaterlooeng)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/univ.waterlooeng.ent.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/univ.waterlooeng.ent.rev.pdf)
- :material-file-search: **Runs:** [UWEntTI](./runs.md#uwentti) | [UWAT1](./runs.md#uwat1) | [UWAT2](./runs.md#uwat2)

??? abstract "Abstract"
	
	The University of Waterloo participated in the Related Entity Finding task of the Entity track. Our goal is to investigate whether related entity finding problem can be addressed by unsupervised approaches that rely primarily on statistical methods and common linguistic tools, such as named-entity taggers and syntactic parsers. We approach the related entity finding problem by first retrieving documents in response to the query, and extracting an initial set of candidate entities from the text of the documents. As a separate step, we automatically construct a set of seed entities, which represent hyponyms of the target entity category specified in the narrative, and then rank the candidate entities by their similarity to the seeds. An example of the target entity category name is “authors”, extracted from the narrative “Authors awarded an Anthony Award at Bouchercon in 2007” (2009 topic #14). The system extracts category names from the free-text narrative, finds seed entities belonging to each category, and computes the similarity of candidate entities to the seeds.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Vechtomova10.bib) "
	```
	@inproceedings{DBLP:conf/trec/Vechtomova10,
		author = {Olga Vechtomova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Related Entity Finding: University of Waterloo at {TREC} 2010 Entity Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/univ.waterlooeng.ent.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Vechtomova10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2010: Related Entity Finding Task of Entity Track

_Zhanyi Wang, Chunsong Tang, Xueji Sun, Haoyi Ouyang, Ru Lan, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/beijing.univ.p-t.rev.ENTITY.pdf](http://trec.nist.gov/pubs/trec19/papers/beijing.univ.p-t.rev.ENTITY.pdf)
- :material-file-search: **Runs:** [PRIS1](./runs.md#pris1) | [PRIS2](./runs.md#pris2) | [PRIS3](./runs.md#pris3) | [PRIS4](./runs.md#pris4)

??? abstract "Abstract"
	
	This paper reports the approaches to the task of Entity Track applied by PRIS lab of BUPT in TREC 2010. We used Document-Centered Model (DCM) and Entity-Centered Model (ECM) for the task. BM25 method was introduced into ECM besides indri retrieval model. Another improvement aimed at entity extraction. Special web page, NER tool and entity list generated by some rules were all taken into account. Also, some external resources such as Google and CMU search engine were applied.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangTSOLXCG10.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangTSOLXCG10,
		author = {Zhanyi Wang and Chunsong Tang and Xueji Sun and Haoyi Ouyang and Ru Lan and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2010: Related Entity Finding Task of Entity Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/beijing.univ.p-t.rev.ENTITY.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangTSOLXCG10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Multiple-Stage Framework for Related Entity Finding: FDWIM at  TREC 2010 Entity Track

_Dong Wang, Qing Wu, Haiguang Chen, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [FDWIM2010](./participants.md#fdwim2010)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/fudan.entity.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/fudan.entity.rev.pdf)
- :material-file-search: **Runs:** [FduWimET2](./runs.md#fduwimet2) | [FduWimET1](./runs.md#fduwimet1) | [FduWimET3](./runs.md#fduwimet3) | [FduWimET4](./runs.md#fduwimet4)

??? abstract "Abstract"
	
	This paper describes a multiple-stage retrieval framework for the task of related entity finding on TREC 2010 Entity Track. In the document retrieval stage, search engine is used to improve the retrieval accuracy. In the entity extraction and filtering stage, we extract entity with NER tools, Wikipedia and text pattern recognition. Then stoplist and other rules are employed to filter entity. Deep mining of the authority pages is proved to be effective in this stage. In entity ranking stage, many factors including keywords from narrative, page rank, combined results of corpus-based association rules and search engine are considered. In the final stage, an improved feature-based algorithm is proposed for the entity homepage detection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangWCN10.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangWCN10,
		author = {Dong Wang and Qing Wu and Haiguang Chen and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Multiple-Stage Framework for Related Entity Finding: {FDWIM} at {TREC} 2010 Entity Track},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/fudan.entity.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangWCN10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NiCT at TREC 2010: Related Entity Finding

_Youzheng Wu, Chiori Hori, Hisashi Kawai_

- :fontawesome-solid-user-group: **Participant:** [NiCT](./participants.md#nict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/national.inst.info.comm.tech.rev.ENT.pdf](http://trec.nist.gov/pubs/trec19/papers/national.inst.info.comm.tech.rev.ENT.pdf)
- :material-file-search: **Runs:** [SuppHomeIsA](./runs.md#supphomeisa) | [SuppHome](./runs.md#supphome) | [SuppIsA](./runs.md#suppisa) | [Supp](./runs.md#supp)

??? abstract "Abstract"
	
	This paper describes experiments carried out at NiCT for the TREC 2010 Entity track. Our studies mainly focus on improving the NE Extraction and Ranking Entity modules, both of them play vital roles in Related Entity Finding system. In our last year's system, only a Named Entity Recognition tool is used to extract entities that match coarse-grained types of target entities such as organization, person, etc. In this year, dependency tree-based patterns learnt automatically are employed to filter out entities that do not match fine-grained types of target entities such as university, airline, author, etc. In the Entity Ranking part, we propose a dependency tree-based similarity method and incorporate homepage information to improve ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHK10.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHK10,
		author = {Youzheng Wu and Chiori Hori and Hisashi Kawai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {NiCT at {TREC} 2010: Related Entity Finding},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/national.inst.info.comm.tech.rev.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHK10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Reconstruct Logical Hierarchical Sitemap for Related Entity Finding

_Qing Yang, Peng Jiang, Chunxia Zhang, Zhendong Niu_

- :fontawesome-solid-user-group: **Participant:** [BIT](./participants.md#bit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.entity.rev.pdf](http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.entity.rev.pdf)
- :material-file-search: **Runs:** [bitDSRRun](./runs.md#bitdsrrun) | [bitRFRun](./runs.md#bitrfrun) | [bitDSHPRun](./runs.md#bitdshprun)

??? abstract "Abstract"
	
	This Paper presents the work done for the TREC 2010 entity track. We concentrate on constructing enriched anchor text model by exploiting hierarchical information presented in web pages to retrieve promising pages, and heuristic rules to extract potential candidate entities by zooming in the right section.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangJZN10.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangJZN10,
		author = {Qing Yang and Peng Jiang and Chunxia Zhang and Zhendong Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Reconstruct Logical Hierarchical Sitemap for Related Entity Finding},
		booktitle = {Proceedings of The Nineteenth Text REtrieval Conference, {TREC} 2010, Gaithersburg, Maryland, USA, November 16-19, 2010},
		series = {{NIST} Special Publication},
		volume = {500-294},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2010},
		url = {http://trec.nist.gov/pubs/trec19/papers/beijing.inst.tech.blog.entity.rev.pdf},
		timestamp = {Fri, 04 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangJZN10.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

