# Proceedings - Contextual Suggestion 2013 

#### Overview of the TREC 2013 Contextual Suggestion Track

_Adriel Dean-Hall, Charles L. A. Clarke, Nicole Simone, Jaap Kamps, Paul Thomas, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/CONTEXT.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec22/papers/CONTEXT.OVERVIEW.pdf)
??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Dean-HallCSKTV13.bib) "
	```
	@inproceedings{DBLP:conf/trec/Dean-HallCSKTV13,
		author = {Adriel Dean{-}Hall and Charles L. A. Clarke and Nicole Simone and Jaap Kamps and Paul Thomas and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees},
		title = {Overview of the {TREC} 2013 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/CONTEXT.OVERVIEW.pdf},
		timestamp = {Fri, 24 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Dean-HallCSKTV13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Nearest Neighbor Approach to Contextual Suggestion

_Sandeep Avula, John O'Connor, Jaime Arguello_

- :fontawesome-solid-user-group: **Participant:** [UNC_SILS](./participants.md#unc_sils)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/unc-context.pdf](http://trec.nist.gov/pubs/trec22/papers/unc-context.pdf)
- :material-file-search: **Runs:** [uncsils_base](./runs.md#uncsils_base) | [uncsils_param](./runs.md#uncsils_param)

??? abstract "Abstract"
	
	The School of Information and Library Science at the University of North Carolina at Chapel Hill (UNCSILS) submit ted two runs to the Contextual Suggestion Track. Given a geographical context, both our runs (UNCSILS BASE and UNCSILS PARAM) scored venues from the same candidate set gathered using the Yelp API. Our baseline run (UNCSILS BASE) followed a nearest neighbor approach. For a given profile/context pair, the candidate venues were scored using the weighted average rating associated with the venues in the profile. The weighting was implemented based on the cosine similarity between the candidate venue and the profile venue using TF.IDF term weighting. The goal of this approach was to score each candidate venue based on the rating associated with the most similar venues in the profile. Our experimental run (UNCSILS PARAM) boosted the contribution from the profile venue with the greatest similarity with the candidate venue and rating. The experimental run (UNCSILS PARAM) outperformed the baseline run (UNCSILS BASE) by a small, but statistically significant margin.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AvulaOA13.bib) "
	```
	@inproceedings{DBLP:conf/trec/AvulaOA13,
		author = {Sandeep Avula and John O'Connor and Jaime Arguello},
		editor = {Ellen M. Voorhees},
		title = {A Nearest Neighbor Approach to Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/unc-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AvulaOA13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTH at TREC 2013 Contextual Suggestion Track

_George Drosatos, Giorgos Stamatelatos, Avi Arampatzis, Pavlos S. Efraimidis_

- :fontawesome-solid-user-group: **Participant:** [DuTH](./participants.md#duth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/DUTH-context.pdf](http://trec.nist.gov/pubs/trec22/papers/DUTH-context.pdf)
- :material-file-search: **Runs:** [DuTH_A](./runs.md#duth_a) | [DuTH_B](./runs.md#duth_b)

??? abstract "Abstract"
	
	In this report we give an overview of our participation in the TREC 2013 Contextual Suggestion Track. We present an approach for context processing that comprises a newly designed and fine-tuned POI (Point Of Interest) data collection technique, a crowdsourcing approach to speed up data collection and two radically different approaches for suggestion processing (a k-NN based and a Rocchio-like). In the context processing, we collect POIs from three popular place search engines, Google Places, Foursquare and Yelp. The collected POIs are enriched by adding snippets from the Google and Bing search engines using crowdsourcing techniques. In the suggestion processing, we propose two methods. The first submits each candidate place as a query to an index of a user's rated examples and scores it based on the top-k results. The second method is based on Rocchio's algorithm and uses the rated examples per user profile to generate a personal query which is then submitted to an index of all candidate places. The track evaluation shows that both approaches are working well; especially the Rocchio-like approach is the most promising since it scores almost firmly above the median system and achieves the best system result in almost half of the judged context-profile pairs. In the final TREC system rankings, we are the 2nd best group in MRR and TBG, and 3rd best group in P@5, out of 15 groups in the category we participated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DrosatosSAE13.bib) "
	```
	@inproceedings{DBLP:conf/trec/DrosatosSAE13,
		author = {George Drosatos and Giorgos Stamatelatos and Avi Arampatzis and Pavlos S. Efraimidis},
		editor = {Ellen M. Voorhees},
		title = {{DUTH} at {TREC} 2013 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/DUTH-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DrosatosSAE13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT, GeoComp, and LIUPPA at the TREC 2013 Contextual Suggestion  Track

_Gilles Hubert, Guillaume Cabanac, Karen Pinel-Sauvagnat, Damien Palacio, Christian Sallaberry_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/IRIT-context.pdf](http://trec.nist.gov/pubs/trec22/papers/IRIT-context.pdf)
- :material-file-search: **Runs:** [IRIT.OpenWeb](./runs.md#irit.openweb) | [IRIT.ClueWeb](./runs.md#irit.clueweb)

??? abstract "Abstract"
	
	In this paper we give an overview of the participation of the IRIT, GeoComp, and LIUPPA labs in the TREC 2013 Contextual Suggestion Track. Our framework combines existing geo-tools or services (e.g., Google Places, Yahoo! BOSS Geo Services, PostGIS, Gisgraphy, GeoNames) and ranks results according to features such as context-place distance, place popularity, and user preferences. We participated in the Open Web and ClueWeb12 sub-tracks with runs IRIT.OpenWeb and IRIT.ClueWeb.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HubertCPTPS13.bib) "
	```
	@inproceedings{DBLP:conf/trec/HubertCPTPS13,
		author = {Gilles Hubert and Guillaume Cabanac and Karen Pinel{-}Sauvagnat and Damien Palacio and Christian Sallaberry},
		editor = {Ellen M. Voorhees},
		title = {IRIT, GeoComp, and {LIUPPA} at the {TREC} 2013 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/IRIT-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HubertCPTPS13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PITT at TREC 2013 Contextual Suggestion Track

_Ming Jiang, Daqing He_

- :fontawesome-solid-user-group: **Participant:** [PITT](./participants.md#pitt)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/pitt-context.pdf](http://trec.nist.gov/pubs/trec22/papers/pitt-context.pdf)
- :material-file-search: **Runs:** [ming_1](./runs.md#ming_1) | [ming_2](./runs.md#ming_2)

??? abstract "Abstract"
	
	This paper reports the IRIS Lab@Pitt's participation to 2013 TREC Contextual Suggestion track, which focuses on technology and issues related to location-based recommender systems (LBRSs). Besides the data provided by the track, our recommendation algorithms also retrieve information from Yelp for creating candidate, example and user profiles. Our algorithms uses linear regression model to combine multiple attributes of candidate profiles into the calculation, and performed 5-fold cross validation for training and testing on 2012 track data. The two runs we submitted this year both obtained reasonable good performance comparing with the median results of all runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangH13.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangH13,
		author = {Ming Jiang and Daqing He},
		editor = {Ellen M. Voorhees},
		title = {{PITT} at {TREC} 2013 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/pitt-context.pdf},
		timestamp = {Mon, 05 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangH13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Amsterdam at the TREC 2013 Contextual Suggestion Track:  Learning User Preferences from Wikitravel Categories

_Marijn Koolen, Hugo C. Huurdeman, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/uvaKamps-context.pdf](http://trec.nist.gov/pubs/trec22/papers/uvaKamps-context.pdf)
- :material-file-search: **Runs:** [UAmsTF30WU](./runs.md#uamstf30wu)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2013 Contextual Suggestion Track. The goal of the track is to evaluate systems that provide suggestions for activities to users in a specific location, taking into account their personal preferences. As a source for travel suggestions we use Wikitravel, which is a community-based travel guide for destinations all over the world. From pages dedicated to cities in the US we extract suggestions for sightseeing, shopping, eating and drinking. Descriptions from positive examples in the user profiles are used as queries to rank all suggestions in the US. Our user-dependent approach merges the per-query rankings of the positive examples of a single user. We automatically classified the rated examples according to the Wikitravel categories—Buy, Do, Drink, Eat and See - and derived a user-specific prior probability per category. With these we re-rank Wikitravel suggestions. The ranked suggestions are then filtered based on the location of the user.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoolenHK13.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoolenHK13,
		author = {Marijn Koolen and Hugo C. Huurdeman and Jaap Kamps},
		editor = {Ellen M. Voorhees},
		title = {University of Amsterdam at the {TREC} 2013 Contextual Suggestion Track: Learning User Preferences from Wikitravel Categories},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/uvaKamps-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KoolenHK13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Context Suggestion Track TREC 2013

_Bingyang Liu, Yanqin Zhong, Yue Liu, Dayong Wu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/ICTNET-context.pdf](http://trec.nist.gov/pubs/trec22/papers/ICTNET-context.pdf)
- :material-file-search: **Runs:** [RUN1](./runs.md#run1) | [RUN2](./runs.md#run2)

??? abstract "Abstract"
	
	This year we did not use any external structured resources like 'Yelp'. An 'Information Retrieval' scheme is implemented. We built index of the ClueWeb12-B-13 using Lucene and use manually and automatically constructed queries to fetch pages from the data subset. Finally we ranked the pages based on user preferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuZLWC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuZLWC13,
		author = {Bingyang Liu and Yanqin Zhong and Yue Liu and Dayong Wu and Xueqi Cheng},
		editor = {Ellen M. Voorhees},
		title = {{ICTNET} at Context Suggestion Track {TREC} 2013},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/ICTNET-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuZLWC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Boosting Venue Page Rankings for Contextual Retrieval-Georgetown at  TREC 2013 Contextual Suggestion Track

_Jiyun Luo, Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [GeorgetownYang](./participants.md#georgetownyang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/georgetown-context.pdf](http://trec.nist.gov/pubs/trec22/papers/georgetown-context.pdf)
- :material-file-search: **Runs:** [BOW_V18](./runs.md#bow_v18) | [BOW_V17](./runs.md#bow_v17)

??? abstract "Abstract"
	
	We participate in the closed collection sub-track of the TREC 2013 Contextual Suggestion. The dataset that we use is an integrated collection of ClueWeb12 Category B, Wikitravel, and the city-specific sub-collection; all are from ClueWeb12. Since the Open Web is not used in our submissions, the task is essentially a retrieval task instead of a result merging task. Our system takes users' ratings of venues in a training city as inputs, and generates titles, document identification numbers, and descriptions for venues that fit users' interests in a new city. Ideal relevant documents for this task should be a list of Web pages each of which is a venue's homepage, which we call a “venue page”. However, off-the-shelf search tools, such as Lemur, fail to retrieve such venue homepages from the collection. They either retrieve non-relevant documents or “yellow-page”-like pages that link to a long list of venue pages where the links are often broken and the destination pages are out of the collection. Therefore, large portions of the retrieved documents are not suitable as answers for contextual suggestion. To address this challenge, we experiment two different approaches, a precision-oriented approach and a recall-oriented approach, to boost the relevant venue pages' ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuoY13.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuoY13,
		author = {Jiyun Luo and Hui Yang},
		editor = {Ellen M. Voorhees},
		title = {Boosting Venue Page Rankings for Contextual Retrieval-Georgetown at {TREC} 2013 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/georgetown-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuoY13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CIRGIRDISCO at TREC 2013 Contextual Suggestion Track: Using the  Wikipedia Graph Structure for Item-to-Item Recommendation

_Muhammad Atif Qureshi, Arjumand Younus, Colm O'Riordan, Gabriella Pasi_

- :fontawesome-solid-user-group: **Participant:** [CIRG_IRDISCO](./participants.md#cirg_irdisco)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/NUIG-context.pdf](http://trec.nist.gov/pubs/trec22/papers/NUIG-context.pdf)
- :material-file-search: **Runs:** [CIRG_IRDISCOA](./runs.md#cirg_irdiscoa) | [CIRG_IRDISCOB](./runs.md#cirg_irdiscob)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2013 contextual suggestion task. We fetch possible locations based on given contexts using Google Places API and WikiTravel. This is followed by a Wikipedia-based item-to-item similarity computation framework which uses the Wikipedia category-article structure to compute similarity between example locations rated by users and the suggested locations. This is then used in an item-based nearest neighbor recommendation framework to recommend the locations based on given user profile ratings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QureshiYOP13.bib) "
	```
	@inproceedings{DBLP:conf/trec/QureshiYOP13,
		author = {Muhammad Atif Qureshi and Arjumand Younus and Colm O'Riordan and Gabriella Pasi},
		editor = {Ellen M. Voorhees},
		title = {{CIRGIRDISCO} at {TREC} 2013 Contextual Suggestion Track: Using the Wikipedia Graph Structure for Item-to-Item Recommendation},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/NUIG-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QureshiYOP13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Lugano at the TREC 2013 Contextual Suggestion Track

_Andrei Rikitianskii, Morgan Harvey, Fabio Crestani_

- :fontawesome-solid-user-group: **Participant:** [ULugano](./participants.md#ulugano)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/lugano-context.pdf](http://trec.nist.gov/pubs/trec22/papers/lugano-context.pdf)
- :material-file-search: **Runs:** [simpleScore](./runs.md#simplescore) | [complexScore](./runs.md#complexscore)

??? abstract "Abstract"
	
	We report on the University of Lugano's participation in the Contextual Suggestion track of TREC 2013 for which we submitted two runs. In particular we present our approach for contextual suggestion which very carefully constructs user profiles in order to provide more accurate and relevant recommendations. The evaluations of our two runs are reported and compared to each other. Based on the track evaluations we demonstrate that our system performs very well in comparison to other runs submitted to the track, managing to achieve the best results in nearly half of all runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RikitianskiiHC13.bib) "
	```
	@inproceedings{DBLP:conf/trec/RikitianskiiHC13,
		author = {Andrei Rikitianskii and Morgan Harvey and Fabio Crestani},
		editor = {Ellen M. Voorhees},
		title = {University of Lugano at the {TREC} 2013 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/lugano-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RikitianskiiHC13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Simple Context Dependent Suggestion System

_Dwaipayan Roy, Ayan Bandyopadhyay, Mandar Mitra_

- :fontawesome-solid-user-group: **Participant:** [ISIatTREC](./participants.md#isiattrec)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/isi-context.pdf](http://trec.nist.gov/pubs/trec22/papers/isi-context.pdf)
- :material-file-search: **Runs:** [isirun](./runs.md#isirun)

??? abstract "Abstract"
	
	The Contextual Suggestion Problem focuses on search techniques for complex information needs that are highly dependent on context and user interest. In this paper, we present our approach to providing user and context dependent suggestions. The official evaluation scores for our submitted run are reported and compared to the overall median scores (across all 34 runs).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoyBM13.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoyBM13,
		author = {Dwaipayan Roy and Ayan Bandyopadhyay and Mandar Mitra},
		editor = {Ellen M. Voorhees},
		title = {A Simple Context Dependent Suggestion System},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/isi-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoyBM13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2013: Contextual Suggestion Track

_Sushma Yalamarti, Mariam Daoud, Jimmy X. Huang_

- :fontawesome-solid-user-group: **Participant:** [YORK](./participants.md#york)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/york-context.pdf](http://trec.nist.gov/pubs/trec22/papers/york-context.pdf)
- :material-file-search: **Runs:** [york13cr1](./runs.md#york13cr1) | [york13cr2](./runs.md#york13cr2)

??? abstract "Abstract"
	
	This paper presents our participation in the Contextual Suggestion Track of TREC 2013. The goal of this track is to investigate search techniques for complex information needs that are highly dependent on context and user interests. To achieve this goal, we propose a semantic user profile modeling for personalized place recommendation. For the semantic user profile model construction, we construct a place ontology based on the Open Directory Project (ODP), a hierarchical ontology scheme for organizing websites. Previously rated attractions by the user are mapped to the place ontology where we represent positive and negative preferences under each place type. For a new user context represented by geographic coordinates, we rerank the top 50 suggestions returned by Google places API using the user profile.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YalamartiDH13.bib) "
	```
	@inproceedings{DBLP:conf/trec/YalamartiDH13,
		author = {Sushma Yalamarti and Mariam Daoud and Jimmy X. Huang},
		editor = {Ellen M. Voorhees},
		title = {York University at {TREC} 2013: Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/york-context.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YalamartiDH13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Opinion-aware Approach to Contextual Suggestion

_Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/udel_fang-context.pdf](http://trec.nist.gov/pubs/trec22/papers/udel_fang-context.pdf)
- :material-file-search: **Runs:** [UDInfoCS1](./runs.md#udinfocs1) | [UDInfoCS2](./runs.md#udinfocs2)

??? abstract "Abstract"
	
	In this paper we describe our efforts for TREC Contextual Suggestion task. Our goal of this year is to evaluate the effectiveness of (1) an opinion-based method to model user profiles and rank candidate suggestions; and (2) a template-based summarization method that leverages the information from multiple resources to generate the description of a candidate suggestion. Existing approaches often uses the description or category information of the suggestions to estimate the user profile. However, one limitation of such approaches is that it may not be generalized well to other suggestions. To overcome this limitation, we propose to estimate the user profile based on the reviews of the candidate suggestions. Our preliminary results show that the proposed new method can improve the performance. Moreover, we explore a new way of generating summaries for the candidate suggestions. The main idea is that we want to leverage the information from multiple sources to generate a more comprehensive summary for a candidate suggestion. In particular, the summary includes the category information of the suggestion, meta-description of the website, reviews of the suggestion and the similar example suggestions that the user liked.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangF13.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangF13,
		author = {Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees},
		title = {An Opinion-aware Approach to Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/udel\_fang-context.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangF13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI and TU Delft Notebook TREC 2013: Contextual Suggestion,  Federated Web Search, KBA, and Web Tracks

_Alejandro Bellogín, Gebrekirstos G. Gebremeskel, Jiyin He, Alan Said, Thaer Samar, Arjen P. de Vries, Jimmy Lin, Jeroen B. P. Vuurens_

- :fontawesome-solid-user-group: **Participant:** [CWI](./participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf](http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf)
- :material-file-search: **Runs:** [IBCosTop1](./runs.md#ibcostop1)

??? abstract "Abstract"
	
	This paper provides an overview of the work done at the Centrum Wiskunde & Informatica (CWI) and Delft University of Technology (TU Delft) for different tracks of TREC 2013. We participated in the Contextual Suggestion Track, the Federated Web Search Track, the Knowledge Base Acceleration (KBA) Track, and the Web Ad-hoc Track. In the Contextual Suggestion track, we focused on filtering the entire ClueWeb12 collection to generate recommendations according to the provided user profiles and contexts. For the Federated Web Search track, we exploited both categories from ODP and document relevance to merge result lists. In the KBA track, we focused on the Cumulative Citation Recommendation task where we exploited different features to two classification algorithms. For the Web track, we extended an ad-hoc baseline with a proximity model that promotes documents in which the query terms are positioned closer together.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BelloginGHSSVLV13.bib) "
	```
	@inproceedings{DBLP:conf/trec/BelloginGHSSVLV13,
		author = {Alejandro Bellog{\'{\i}}n and Gebrekirstos G. Gebremeskel and Jiyin He and Alan Said and Thaer Samar and Arjen P. de Vries and Jimmy Lin and Jeroen B. P. Vuurens},
		editor = {Ellen M. Voorhees},
		title = {{CWI} and {TU} Delft Notebook {TREC} 2013: Contextual Suggestion, Federated Web Search, KBA, and Web Tracks},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/cwi-context-federated-kba-web.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BelloginGHSSVLV13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2013: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Web Tracks

_Richard McCreadie, M-Dyaa Albakour, Stuart Mackie, Nut Limsopatham, Craig Macdonald, Iadh Ounis, Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf](http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf)
- :material-file-search: **Runs:** [uogTrCFP](./runs.md#uogtrcfp) | [uogTrCFX](./runs.md#uogtrcfx)

??? abstract "Abstract"
	
	In TREC 2013, we focus on tackling the challenges posed by the new Contextual Suggestion and Temporal summarisation tracks, as well as enhancing our existing technologies to tackle the new risk-sensitive aspect of the Web track, building upon our Terrier Information Retrieval Platform. In particular, for the Contextual Suggestion track, we investigate how to exploit location-based social networks, with the aim of better identifying venues within a city that a given user might be interested in visiting. For the Temporal Summarisation track, we propose a new summarisation framework and investigate novel techniques to adaptively alter the summarisation strategy over time. For the TREC Web track, we continue to build upon our learning-to-rank approaches and novel xQuAD / Fat frameworks within Terrier, increasing effectiveness when ranking and examining two new approaches to risk-sensitive retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieAMLMOD13.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieAMLMOD13,
		author = {Richard McCreadie and M{-}Dyaa Albakour and Stuart Mackie and Nut Limsopatham and Craig Macdonald and Iadh Ounis and Bekir Taner Din{\c{c}}er},
		editor = {Ellen M. Voorhees},
		title = {University of Glasgow at {TREC} 2013: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Web Tracks},
		booktitle = {Proceedings of The Twenty-Second Text REtrieval Conference, {TREC} 2013, Gaithersburg, Maryland, USA, November 19-22, 2013},
		series = {{NIST} Special Publication},
		volume = {500-302},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2013},
		url = {http://trec.nist.gov/pubs/trec22/papers/terrier-context-ts-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieAMLMOD13.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

