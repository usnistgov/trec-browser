# Proceedings - Entity 2009 

#### Overview of the TREC 2009 Entity Track

_Krisztian Balog, Arjen P. de Vries, Pavel Serdyukov, Paul Thomas, Thijs Westerveld_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ENT09.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec18/papers/ENT09.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The goal of the entity track is to perform entity-oriented search tasks on the World Wide Web. Many user information needs would be better answered by specific entities instead of just any type of documents. The track defines entities as “typed search results,” “things,” represented by their homepages on the web. Searching for entities thus corresponds to ranking these homepages. The track thereby investigates a problem quite similar to the QA list task. In this pilot year, we limited the track's scope to searches for instances of the organizations, people, and product entity types.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BalogVSTW09.bib) "
	```
	@inproceedings{DBLP:conf/trec/BalogVSTW09,
		author = {Krisztian Balog and Arjen P. de Vries and Pavel Serdyukov and Paul Thomas and Thijs Westerveld},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2009 Entity Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ENT09.OVERVIEW.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BalogVSTW09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Related Entity Finding Based on Co-Occurance

_Marc Bron, Krisztian Balog, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UAms](./participants.md#uams)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.ENT.pdf)
- :material-file-search: **Runs:** [ilpsEntem](./runs.md#ilpsentem) | [ilpsEntBL](./runs.md#ilpsentbl) | [ilpsEntcr](./runs.md#ilpsentcr) | [ilpsEntcf](./runs.md#ilpsentcf)

??? abstract "Abstract"
	
	We report on experiments for the Related Entity Finding task in which we focus on only using Wikipedia as a target corpus in which to identify (related) entitities. Our approach is based on co-occurrences between the source entity and potential target entities. We observe improvements in performance when a context-independent co-occurrence model is combined with context-dependent co-occurrence models in which we stress the importance of the expected relation between source and target entity. Applying type filtering yields further improvements results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BronBR09.bib) "
	```
	@inproceedings{DBLP:conf/trec/BronBR09,
		author = {Marc Bron and Krisztian Balog and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Related Entity Finding Based on Co-Occurance},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uamsterdam-derijke.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BronBR09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Entity Retrieval with Hierarchical Relevance Model, Exploiting the  Structure of Tables and Learning Homepage Classifiers

_Yi Fang, Luo Si, Zhengtao Yu, Yantuan Xian, Yangbo Xu_

- :fontawesome-solid-user-group: **Participant:** [Purdue_Si](./participants.md#purdue_si)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/purdue.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/purdue.ENT.pdf)
- :material-file-search: **Runs:** [KMR2PU](./runs.md#kmr2pu) | [KMR1PU](./runs.md#kmr1pu) | [KMR3PU](./runs.md#kmr3pu)

??? abstract "Abstract"
	
	This paper gives an overview of our work done for the TREC 2009 Entity track. We propose a hierarchical relevance retrieval model for entity ranking. In this model, three levels of relevance are examined which are document, passage and entity, respectively. The final ranking score is a linear combination of the relevance scores from the three levels. Furthermore, we exploit the structure of tables and lists to identify the target entities from them by making a joint decision on all the entities with the same attribute. To find entity homepages, we train logistic regression models for each type of entities. A set of templates and filtering rules are also used to identify target entities. The key lessons that we learned by participating this year's Entity track include: 1) our special treatment of table and list data is well rewarding; 2) The high accuracy of homepage finding is crucial in this track; 3) Wikipedia can serve as a valuable knowledge resource for different aspects of the related entity finding task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FangSYXX09.bib) "
	```
	@inproceedings{DBLP:conf/trec/FangSYXX09,
		author = {Yi Fang and Luo Si and Zhengtao Yu and Yantuan Xian and Yangbo Xu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Entity Retrieval with Hierarchical Relevance Model, Exploiting the Structure of Tables and Learning Homepage Classifiers},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/purdue.ENT.pdf},
		timestamp = {Tue, 17 May 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FangSYXX09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Result Diversity and Entity Ranking Experiments: Anchors, Links, Text  and Wikipedia

_Rianne Kaptein, Marijn Koolen, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [Amsterdam](./participants.md#amsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uamsterdam-kamps.ENT.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uamsterdam-kamps.ENT.WEB.pdf)
- :material-file-search: **Runs:** [basewikirun](./runs.md#basewikirun) | [UAmsER09Co](./runs.md#uamser09co) | [UAmsER09Ab1](./runs.md#uamser09ab1) | [wikiruncats](./runs.md#wikiruncats)

??? abstract "Abstract"
	
	In this paper, we document our efforts in participating to the TREC 2009 Entity Ranking and Web Tracks. We had multiple aims: For the Web Track's Adhoc task we experiment with document text and anchor text representation, and the use of the link structure. For the Web Track's Diversity task we experiment with using a top down sliding window that, given the top ranked documents, chooses as the next ranked document the one that has the most unique terms or links. We test our sliding window method on a standard document text index and an index of propagated anchor texts. We also experiment with extreme query expansions by taking the top n results of the initial ranking as multi-faceted aspects of the topic to construct n relevance models to obtain n sets of results. A final diverse set of results is obtained by merging the n results lists. For the Entity Ranking Track, we also explore the effectiveness of the anchor text representation, look at the co-citation graph, and experiment with using Wikipedia as a pivot. Our main findings can be summarized as follows: Anchor text is very effective for diversity. It gives high early precision and the results cover more relevant sub-topics than the document text index. Our baseline runs have low diversity, which limits the possible impact of the sliding window approach. New link information seems more effective for diversifying text-based search results than the amount of unique terms added by a document. In the entity ranking task, anchor text finds few primary pages , but it does retrieve a large number of relevant pages. Using Wikipedia as a pivot results in large gains of P10 and NDCG when only primary pages are considered. Although the links between the Wikipedia entities and pages in the Clueweb collection are sparse, the precision of the existing links is very high.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KapteinKK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/KapteinKK09,
		author = {Rianne Kaptein and Marijn Koolen and Jaap Kamps},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Result Diversity and Entity Ranking Experiments: Anchors, Links, Text and Wikipedia},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uamsterdam-kamps.ENT.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KapteinKK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2009: Experiments with Terrier

_Richard McCreadie, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf](http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf)
- :material-file-search: **Runs:** [uogTrEbl](./runs.md#uogtrebl) | [uogTrEc3](./runs.md#uogtrec3) | [uogTrEpr](./runs.md#uogtrepr) | [uogTrEdi](./runs.md#uogtredi)

??? abstract "Abstract"
	
	In TREC 2009, we extend our Voting Model for the faceted blog distillation, top stories identification, and related entity finding tasks. Moreover, we experiment with our novel xQuAD framework for search result diversification. Besides fostering our research in multiple directions, by participating in such a wide portfolio of tracks, we further develop the indexing and retrieval capabilities of our Terrier Information Retrieval platform, to effectively and efficiently cope with a new generation of large-scale test collections.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMOPS09,
		author = {Richard McCreadie and Craig Macdonald and Iadh Ounis and Jie Peng and Rodrygo L. T. Santos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2009: Experiments with Terrier},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uglasgow.BLOG.ENT.MQ.RF.WEB.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMOPS09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Journey in Entity Related Retrieval for TREC 2009

_Jagadish Pamarthi, GuangXu Zhou, Coskun Bayrak_

- :fontawesome-solid-user-group: **Participant:** [UALR_CB](./participants.md#ualr_cb)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uarkansas-lr.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/uarkansas-lr.ENT.pdf)
- :material-file-search: **Runs:** [UALRCB09r4](./runs.md#ualrcb09r4) | [UALRCB09r1](./runs.md#ualrcb09r1) | [UALRCB09r2](./runs.md#ualrcb09r2) | [UALRCB09r3](./runs.md#ualrcb09r3)

??? abstract "Abstract"
	
	The focus of this paper is to present the results obtained as a result of performing entity information retrieval, namely the home pages of products, organizations and persons. The preliminary results, based on the Indri Search Engine, of this study and experimentation were presented at the Entity Track in TREC 2009. Indri Search Engine is an efficient and effective open source tool, which is operated by indri query language in any windows or UNIX based platform. Indri is based on the inference network framework and supports structured queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PamarthiZB09.bib) "
	```
	@inproceedings{DBLP:conf/trec/PamarthiZB09,
		author = {Jagadish Pamarthi and GuangXu Zhou and Coskun Bayrak},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Journey in Entity Related Retrieval for {TREC} 2009},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uarkansas-lr.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PamarthiZB09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Delft University at the TREC 2009 Entity Track: Ranking Wikipedia  Entities

_Pavel Serdyukov, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [tudelft](./participants.md#tudelft)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/delft.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/delft.ENT.pdf)
- :material-file-search: **Runs:** [tudpw](./runs.md#tudpw) | [tudpwkntop](./runs.md#tudpwkntop) | [tudwtop](./runs.md#tudwtop) | [tudwebtop](./runs.md#tudwebtop)

??? abstract "Abstract"
	
	This paper describes the details of our participation in Entity track of the TREC 2009.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SerdyukovV09.bib) "
	```
	@inproceedings{DBLP:conf/trec/SerdyukovV09,
		author = {Pavel Serdyukov and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Delft University at the {TREC} 2009 Entity Track: Ranking Wikipedia Entities},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/delft.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SerdyukovV09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding Related Entities by Retrieving Relations: UIUC at TREC  2009 Entity Track

_V. G. Vinod Vydiswaran, Kavita Ganesan, Yuanhua Lv, Jing He, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [UIUC](./participants.md#uiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/uiuc.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/uiuc.ENT.pdf)
- :material-file-search: **Runs:** [UIqryForm](./runs.md#uiqryform) | [UIqryForm3](./runs.md#uiqryform3) | [UIauto](./runs.md#uiauto)

??? abstract "Abstract"
	
	Our goal in participating in the TREC 2009 Entity Track was to study whether relation extraction techniques can help in improving accuracy of the entity finding task. Finding related entities is informational in nature and we wanted to explore if inducing structure on the queries helps satisfy this information need. The research outlook we took was to study techniques that retrieve relations between two entities from a large corpus, and from those, find the most relevant entities that participate in the given relation with another given entity. Instead of aiming at retrieving pages about specific entities, we tried to address the problem of directly finding the entities from the text. Our experimental results show that we were able to find many related entities using relation-based extraction, and ranking entities based on further evidence from the text helps to a certain extent.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VydiswaranGLHZ09.bib) "
	```
	@inproceedings{DBLP:conf/trec/VydiswaranGLHZ09,
		author = {V. G. Vinod Vydiswaran and Kavita Ganesan and Yuanhua Lv and Jing He and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Finding Related Entities by Retrieving Relations: {UIUC} at {TREC} 2009 Entity Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/uiuc.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VydiswaranGLHZ09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BUPT at TREC 2009: Entity Track

_Zhanyi Wang, Dong-xin Liu, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [buptpris___2009](./participants.md#buptpris___2009)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/bupt.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/bupt.ENT.pdf)
- :material-file-search: **Runs:** [PRIS1](./runs.md#pris1) | [PRIS2](./runs.md#pris2) | [PRIS3](./runs.md#pris3) | [PRIS4](./runs.md#pris4)

??? abstract "Abstract"
	
	This report introduces the work of BUPT (PRIS) in Entity Track in TREC2009. The task and data are both new this year. In our work, an improved two-stage retrieval model is proposed according to the task. The first stage is document retrieval, in order to get the similarity of the query and documents. The second stage is to find the relationship between documents and entities. We also focus on entity extraction in the second stage and the final ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangLXCG09.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangLXCG09,
		author = {Zhanyi Wang and Dong{-}xin Liu and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{BUPT} at {TREC} 2009: Entity Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/bupt.ENT.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangLXCG09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NiCT at TREC 2009: Employing Three Models for Entity Ranking Track

_Youzheng Wu, Hideki Kashioka_

- :fontawesome-solid-user-group: **Participant:** [NiCT](./participants.md#nict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/nict.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/nict.ENT.pdf)
- :material-file-search: **Runs:** [NiCTm2](./runs.md#nictm2) | [NiCTm1](./runs.md#nictm1) | [NiCTm3](./runs.md#nictm3) | [NiCTm4](./runs.md#nictm4)

??? abstract "Abstract"
	
	This paper describes experiments carried out at NiCT for the TREC 2009 Entity Ranking track. Our main study is to develop an effective approach to rank entities via measuring the “similarities” between supporting snippets of entities and input query. Three models are implemented to this end. 1) The DLM regards entity ranking as a task of calculating the probabilities of generating input query given supporting snippets of entities via language model. 2) The RSVM ranks entities via a supervised Ranking SVM. 3) The CSVM, an unsupervised model, ranks entities according to the probabilities of input query belonging to topics represented by entities and their supporting snippets via SVM classifier. The evaluation shows that the DLM is the best on P@10, while the RSVM outperforms the others on nDCG.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuK09.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuK09,
		author = {Youzheng Wu and Hideki Kashioka},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {NiCT at {TREC} 2009: Employing Three Models for Entity Ranking Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/nict.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuK09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on Related Entity Finding Track at TREC 2009

_Qing Yang, Peng Jiang, Chunxia Zhang, Zhendong Niu_

- :fontawesome-solid-user-group: **Participant:** [BIT](./participants.md#bit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/bit.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/bit.ENT.pdf)
- :material-file-search: **Runs:** [BITDLDE09Run](./runs.md#bitdlde09run)

??? abstract "Abstract"
	
	Our goal in participating in the TREC 2009 Entity Track is to study whether QA list technique can help improve accuracy of the entity finding task. Also, we take a looking for homepage finding to identify homepages of an entity by training a maximum entropy classifier and a logistic regression models for three types of entity respectively.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangJZN09.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangJZN09,
		author = {Qing Yang and Peng Jiang and Chunxia Zhang and Zhendong Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments on Related Entity Finding Track at {TREC} 2009},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/bit.ENT.pdf},
		timestamp = {Fri, 04 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangJZN09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Novel Framework for Related Entities Finding: ICTNET at TREC  2009 Entity Track

_Haijun Zhai, Xueqi Cheng, Jiafeng Guo, Hongbo Xu, Yue Liu_

- :fontawesome-solid-user-group: **Participant:** [CAS_ICT_IR](./participants.md#cas_ict_ir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/ictnet.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/ictnet.ENT.pdf)
- :material-file-search: **Runs:** [ICTZHRun1](./runs.md#ictzhrun1)

??? abstract "Abstract"
	
	This paper addresses the problem of related entity finding, which was proposed in trec 2009. The overall aim of related entity finding (REF) is to perform entity-related search on Web data, which address common information needs that are not that well modeled as ad hoc document search. In this paper, a novel framework was proposed based on a probabilistic model for related entity finding in a Web collection. This model consists of two parts. One is the probability indicating the relation between the source entity and the candidate entities. The other is the probability indicating the relevance between the candidate entities and the topic. Using ClueWeb09 dataset, the experimental evaluations show the effectiveness of our REF framework.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaiCGXL09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaiCGXL09,
		author = {Haijun Zhai and Xueqi Cheng and Jiafeng Guo and Hongbo Xu and Yue Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Novel Framework for Related Entities Finding: {ICTNET} at {TREC} 2009 Entity Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/ictnet.ENT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaiCGXL09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UDEL/SMU at TREC 2009 Entity Track

_Wei Zheng, Swapna Gottipati, Jing Jiang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [EceUdel](./participants.md#eceudel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.ENT.pdf](http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.ENT.pdf)
- :material-file-search: **Runs:** [UdSmuTP](./runs.md#udsmutp) | [UdSmuTU](./runs.md#udsmutu) | [UdSmuCM50](./runs.md#udsmucm50) | [UdSmuCM](./runs.md#udsmucm)

??? abstract "Abstract"
	
	We report our methods and experiment results from the collaborative participation of the InfoLab group from University of Delaware and the school of Information Systems from Singapore Management University in the TREC 2009 Entity track. Our general goal is to study how we may apply language modeling approaches and natural language processing techniques to the task. Specifically, we proposed to find supporting information based on segment retrieval, to extract entities using Stanford NER tagger, and to rank entities based on a previously proposed probabilistic framework for expert finding.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengGJF09.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengGJF09,
		author = {Wei Zheng and Swapna Gottipati and Jing Jiang and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UDEL/SMU} at {TREC} 2009 Entity Track},
		booktitle = {Proceedings of The Eighteenth Text REtrieval Conference, {TREC} 2009, Gaithersburg, Maryland, USA, November 17-20, 2009},
		series = {{NIST} Special Publication},
		volume = {500-278},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2009},
		url = {http://trec.nist.gov/pubs/trec18/papers/udelaware-fang.ENT.pdf},
		timestamp = {Tue, 20 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengGJF09.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

