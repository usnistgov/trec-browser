# Proceedings - Contextual Suggestion 2016 

#### Overview of the TREC 2016 Contextual Suggestion Track

_Seyyed Hadi Hashemi, Jaap Kamps, Julia Kiseleva, Charles L. A. Clarke, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec25/papers/Overview-CS.pdf](https://trec.nist.gov/pubs/trec25/papers/Overview-CS.pdf)
??? abstract "Abstract"
	
	The TREC Contextual Suggestion Track offers a personalized point of interest (POI) recommendation task, in which participants develop systems to give a ranked list of suggestions related to a profile and a context pair available in the tasks' requests provided by the track organizers. Previously, reusability of the contextual suggestion track suffered from using dynamic collections and a shallow pool depth. The main innovations at TREC 2016 are the following. First, the TREC CS web corpus, consisting of a web crawl of the TREC contextual suggestion collection, was made available. The rich textual descriptions of the web pages makes far more information available for each candidate POI in the collection. Second, we released endorsements (end user tags) of the attractions as given by NIST assessors, potentially matching the endorsements of POIs in another city as given by the person issuing the request as part of her profile. Third, a multi-depth pooling approach extending beyond the shallow top 5 pool was used. The multi-depth pooling approach has created a test collection that provides more reliable evaluation results in ranks deeper than the traditional pool cut-off.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HashemiKKCV16.bib) "
	```
	@inproceedings{DBLP:conf/trec/HashemiKKCV16,
		author = {Seyyed Hadi Hashemi and Jaap Kamps and Julia Kiseleva and Charles L. A. Clarke and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2016 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {https://trec.nist.gov/pubs/trec25/papers/Overview-CS.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HashemiKKCV16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Venue Appropriateness Prediction for Contextual Suggestion

_Mohammad Aliannejadi, Ida Mele, Fabio Crestani_

- :fontawesome-solid-user-group: **Participant:** [USI](./participants.md#usi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/USI-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/USI-CX.pdf)
- :material-file-search: **Runs:** [USI1](./runs.md#usi1) | [USI2](./runs.md#usi2) | [USI3](./runs.md#usi3) | [USI4](./runs.md#usi4) | [USI5](./runs.md#usi5)

??? abstract "Abstract"
	
	This technical report presents the work of Universit `a della Svizzera italiana (USI) at TREC 2016 Contextual Suggestion track. The goal of the Contextual Suggestion track is to develop systems that could make suggestions for venues that a user will potentially like. Our proposed method aempts to model the users' behavior and opinion by training a SVM classifier for each user. It then enriches the basic model using additional data sources such as venue categories and taste keywords to model users' interest. For predicting the contextual appropriateness of a venue to a user's context, we modeled the problem as a binary classification one. Furthermore, we built two datasets using crowdsourcing that are used to train a SVM classifier to predict the contextual appropriateness of venues. Finally, we show how to incorporate the multimodal scores in our model to produce the final ranking. The experimental results illustrate that our proposed method performed very well in terms of all the evaluation metrics used in TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AliannejadiMC16.bib) "
	```
	@inproceedings{DBLP:conf/trec/AliannejadiMC16,
		author = {Mohammad Aliannejadi and Ida Mele and Fabio Crestani},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Venue Appropriateness Prediction for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/USI-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AliannejadiMC16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ADAPT_TCD: An Ontology-Based Context Aware Approach for Contextual  Suggestion

_Mostafa Bayomi, Séamus Lawless_

- :fontawesome-solid-user-group: **Participant:** [ADAPT_TCD](./participants.md#adapt_tcd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ADAPT_TCD-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/ADAPT_TCD-CX.pdf)
- :material-file-search: **Runs:** [ADAPT_TCD_r1](./runs.md#adapt_tcd_r1) | [ADAPT_TCD_r2](./runs.md#adapt_tcd_r2) | [ADAPT_TCD_br1](./runs.md#adapt_tcd_br1) | [ADAPT_TCD_br2](./runs.md#adapt_tcd_br2) | [ADAPT_TCD_br3](./runs.md#adapt_tcd_br3)

??? abstract "Abstract"
	
	In this paper we give an overview of the participation of the ADAPT Centre, Trinity College Dublin, Ireland, in both phases of the TREC 2016 Contextual Suggestion Track. We present our ontology-based approach that consists of three models that are based on an ontology that was extracted from the Foursquare category hierarchy. The three models are: User Model, Document Model and Rule Model. In the User Model we build two models, one for each phase of the task, based upon the attractions that were rated in the user's profile. The Document Model enriches documents with extra metadata from Foursquare and categories (concepts) from the ontology are attached to each document. The Rule model is used to tune the score for candidate suggestions based on how the context of the trip aligns with the rules in the model. The results of our submitted runs, in both phases, demonstrate the effectiveness of the proposed methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BayomiL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/BayomiL16,
		author = {Mostafa Bayomi and S{\'{e}}amus Lawless},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {ADAPT{\_}TCD: An Ontology-Based Context Aware Approach for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/ADAPT\_TCD-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BayomiL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Significant Words Language Models for Contextual Suggestion

_Mostafa Dehghani, Jaap Kamps, Hosein Azarbonyad, Maarten Marx_

- :fontawesome-solid-user-group: **Participant:** [ExPoSe](./participants.md#expose)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ExPoSe-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/ExPoSe-CX.pdf)
- :material-file-search: **Runs:** [response_tags](./runs.md#response_tags) | [run_content](./runs.md#run_content) | [run_all](./runs.md#run_all) | [SWLM](./runs.md#swlm)

??? abstract "Abstract"
	
	In this paper, we present the participation of the University of Amsterdam's ExPoSe team in the TREC 2016 Contextual Suggestion Track. The main goal of contextual suggestion track is to evaluate methods for providing suggestions for activities or points of interest to users in a specific location, at a specific time, taking their personal preferences into consideration. One of the key steps of contextual suggestion methods is estimating a proper model for representing different objects in the data like users and attractions. Here, we describe our approach which is employing Significant Words Language Models (SWLM) [2] as an effective method for estimating models representing significant features of sets of attractions as user profiles and sets of users as group profile. We observe that using SWLM, we are able to better estimate a model representing the set of preferences positively rated by users as their profile, compared to the case we use standard language model as the profiling approach. We also find that using negatively rated attractions as negative samples along with positively rated attractions as positive samples, we may loose the performance when we use standard language model as the profiling approach. While, using SWLM, taking negatively rated attractions into consideration may help to improve the quality of suggestions. In addition, we investigate groups of users sharing a property (e.g. of a similar age) and study the effect of taking group-based profiles on the performance of suggestions provided for individual users. We noticed that group-based suggestion helps more when users have a tendency to rate attraction in a neutral way, compared to the case users are more subjective in their rating behavior.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DehghaniKAM16.bib) "
	```
	@inproceedings{DBLP:conf/trec/DehghaniKAM16,
		author = {Mostafa Dehghani and Jaap Kamps and Hosein Azarbonyad and Maarten Marx},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Significant Words Language Models for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/ExPoSe-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DehghaniKAM16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Neural Endorsement Based Contextual Suggestion

_Seyyed Hadi Hashemi, Jaap Kamps, Nawal Ould Amer_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Uamsterdam-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/Uamsterdam-CX.pdf)
- :material-file-search: **Runs:** [UAmsterdam1](./runs.md#uamsterdam1) | [UAmsterdam2](./runs.md#uamsterdam2) | [UAmsterdamCB](./runs.md#uamsterdamcb) | [UAmsterdamDL](./runs.md#uamsterdamdl)

??? abstract "Abstract"
	
	This paper presents the University of Amsterdam's participation in the TREC 2016 Contextual Suggestion Track. In this research, we have studied a personallized neural document language modeling and a neural category preference modeling for contextual suggestion using available endorsements in TREC 2016 contextual suggestion track phase 2 requests. Specifically, our main aim is to answer the questions: How to model users' profiles by using the suggestions' endorsements as an additional data? How effective is using word embeddings to boost terms' weights relevant to the given endorsements? How to model users' attraction-category preferences? How effective is using deep neural networks to learn users' category preferences in contextual suggestion task? Our main findings are the following: First, the neural personalized document based user profiling using word embeddings improves the baseline content-based filtering approach based on all the common IR measures including TREC 2016 Contextual Suggestion official metric (NDCG@5). Second, neural users' category preference modeling beats both baseline content-based filtering and the user profiling model using word-embeddings in terms of all the common IR measures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HashemiKA16.bib) "
	```
	@inproceedings{DBLP:conf/trec/HashemiKA16,
		author = {Seyyed Hadi Hashemi and Jaap Kamps and Nawal Ould Amer},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Neural Endorsement Based Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Uamsterdam-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HashemiKA16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Recommending Points-of-Interest via Weighted kNN, Rated Rocchio, and  Borda Count Fusion

_Georgios Kalamatianos, Avi Arampatzis_

- :fontawesome-solid-user-group: **Participant:** [DUTH](./participants.md#duth)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/DUTH-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/DUTH-CX.pdf)
- :material-file-search: **Runs:** [DUTH_rocchio](./runs.md#duth_rocchio) | [DUTH_knn](./runs.md#duth_knn) | [DUTH_bcf](./runs.md#duth_bcf)

??? abstract "Abstract"
	
	We present the work of the Democritus University of Thrace (DUTH) team in TREC's 2016 Contextual Suggestion Track. The goal of the Contextual Suggestion Track is to build a system capable of proposing venues which a user might be interested to visit, using any available contextual and personal information. First, we enrich the TREC-provided dataset by collecting more information on venues from web-services like Foursquare and Yelp. Then, we address the task with two different content-based methods, namely, a Weighted kNN classifier and a Rated Rocchio personalized query. Last, we also explore the use of a voting system, namely Borda Count, as a means of fusing the results of several suggestion systems. Our runs provided very good results, achieving top or near-top TREC performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KalamatianosA16.bib) "
	```
	@inproceedings{DBLP:conf/trec/KalamatianosA16,
		author = {Georgios Kalamatianos and Avi Arampatzis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Recommending Points-of-Interest via Weighted kNN, Rated Rocchio, and Borda Count Fusion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/DUTH-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KalamatianosA16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Employing open-web for Contextual Suggestion using tag-tag similarity

_Sainyam Kapoor, Manajit Chakraborty, C. Ravindranath Chowdary_

- :fontawesome-solid-user-group: **Participant:** [DPLAB_IITBHU](./participants.md#dplab_iitbhu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/DPLAB_IITBHU-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/DPLAB_IITBHU-CX.pdf)
- :material-file-search: **Runs:** [iitbhu01](./runs.md#iitbhu01) | [iitbhu04](./runs.md#iitbhu04) | [iitbhu05](./runs.md#iitbhu05)

??? abstract "Abstract"
	
	The TREC 2016 Contextual Suggestion task aims at providing recommendations on points of attraction for different kind of users and a varying context. Our group DPLAB IITBHU tries to recommend relevant point-of-interests to a user based on the information provided on the candidate attractions and her past preferences. We employ open-web information in a novel way to capture the best possible setting for a user's tastes and distastes in terms of tag scores. The scores are then ranked using a heuristic to suggest the most pertinent attraction to the user. One of our methods exceed the TREC-CS 2016 median of the standard evaluation scores of all participant runs, which reflects the effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KapoorCC16.bib) "
	```
	@inproceedings{DBLP:conf/trec/KapoorCC16,
		author = {Sainyam Kapoor and Manajit Chakraborty and C. Ravindranath Chowdary},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Employing open-web for Contextual Suggestion using tag-tag similarity},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/DPLAB\_IITBHU-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KapoorCC16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Context Based Recommender System through Collaborative Filtering  and Word Embedding Techniques

_Mahsa Khorasani, Hamid Sadjadi, Faezeh Ramazani, Faezeh Ensan_

- :fontawesome-solid-user-group: **Participant:** [FUM-IRLAB](./participants.md#fum-irlab)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/FUM-IRLAB-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/FUM-IRLAB-CX.pdf)
- :material-file-search: **Runs:** [1](./runs.md#1) | [2](./runs.md#2) | [3](./runs.md#3) | [phase2_1](./runs.md#phase2_1) | [phase2_2](./runs.md#phase2_2)

??? abstract "Abstract"
	
	This report presents a description of the context-based recommender system that was developed by the FUM-IR team from the Ferdowsi University of Mashhad for the Contextual Suggestion track of TREC 2016. This will also include the description of the different runs were submitted to this track. In developing our system, we followed two main approaches for finding suitable attractions for a given user: a content-based approach and a category-based approach. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KhorasaniSRE16.bib) "
	```
	@inproceedings{DBLP:conf/trec/KhorasaniSRE16,
		author = {Mahsa Khorasani and Hamid Sadjadi and Faezeh Ramazani and Faezeh Ensan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Context Based Recommender System through Collaborative Filtering and Word Embedding Techniques},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/FUM-IRLAB-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KhorasaniSRE16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team at TREC 2016: Experiments in  Contextual Suggestions

_Jarana Manotumruksa, Craig MacDonald, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/uogTr-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/uogTr-CX.pdf)
- :material-file-search: **Runs:** [uogTrCs](./runs.md#uogtrcs) | [uogTrCsContext](./runs.md#uogtrcscontext)

??? abstract "Abstract"
	
	For TREC 2016, we focus on tackling the challenges posed by the Contextual Suggestion by investigating the use of user-generated data (e.g. textual content of comments and venue's information) in location-based social networks (LBSNs) to suggest a ranked list of venues to users. In particular, we exploit a word embedding technique to extract user-venue and context-venue preference features to train learning-to-rank models. In addition, we leverage each venue's information (e.g. number of check-in) to extract venue-dependent features. We train learning-to-rank models using these features on the TREC 2015 Contextual Suggestion dataset. We submit two runs (uogTrCs and uogTrCsContext) where uogTrCsContexl is a context-aware approach. The batch experimental results show that uogTrCS is competitive, performing above the TREC median in terms of NDCG@5 and P@5 and outperforms uogTrCsContext.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ManotumruksaMO16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ManotumruksaMO16,
		author = {Jarana Manotumruksa and Craig MacDonald and Iadh Ounis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow Terrier Team at {TREC} 2016: Experiments in Contextual Suggestions},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/uogTr-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ManotumruksaMO16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Word embeddings and Global Preference for Contextual Suggestion

_Jian Mo, Luc Lamontagne, Richard Khoury_

- :fontawesome-solid-user-group: **Participant:** [LavalLakehead](./participants.md#lavallakehead)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/LavalLakehead-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/LavalLakehead-CX.pdf)
- :material-file-search: **Runs:** [Laval_run1](./runs.md#laval_run1) | [Laval_batch_1](./runs.md#laval_batch_1) | [Laval_batch_2](./runs.md#laval_batch_2) | [Laval_batch_3](./runs.md#laval_batch_3)

??? abstract "Abstract"
	
	In this paper we describe our effort on 2016 Contextual Suggestion Track. We present a new ranking model that captures both global trend of interests as well as contextual individual preference. We trained a regressor on common users data thus it can prioritize popular places and categories. In order to model individual user preference, we introduce word embeddings to represent both user profiles and candidate places as vectors in a same Euclidean space.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoLK16.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoLK16,
		author = {Jian Mo and Luc Lamontagne and Richard Khoury},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Word embeddings and Global Preference for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/LavalLakehead-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoLK16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Beijing University of Posts and Telecommunications(BUPT) at TREC  2016: A Rating Model Based on Tags for ABSTRACT Contextual Suggestion

_Danping Yin, Siyuan Gao, Zonghui Peng, Yameng Li, Ruifang Liu_

- :fontawesome-solid-user-group: **Participant:** [bupt_pris_2016](./participants.md#bupt_pris_2016)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/bupt_pris_2016-CX.pdf](http://trec.nist.gov/pubs/trec25/papers/bupt_pris_2016-CX.pdf)
- :material-file-search: **Runs:** [bupt_runA](./runs.md#bupt_runa) | [cs.2_.4_max](./runs.md#cs.2_.4_max) | [cs.4_.2_max](./runs.md#cs.4_.2_max) | [cs.3_.3_avg](./runs.md#cs.3_.3_avg)

??? abstract "Abstract"
	
	In this paper we focus on the effort of Beijing University of Posts and Telecommunications (BUPT) on the TREC 2016's Contextual Suggestion Track. The problem we are supposed to tackle is how to make suggestions for a particular person with the provided context as well as its preferences. Basically we regard tags as the most important factor, and get ratings for different attractions with the ratings of tags. Also we use Collaborative Filtering to fill the missing ratings. A ranked list is generated after calculating users' ratings for candidate attractions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YinGPLL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/YinGPLL16,
		author = {Danping Yin and Siyuan Gao and Zonghui Peng and Yameng Li and Ruifang Liu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Beijing University of Posts and Telecommunications(BUPT) at {TREC} 2016: {A} Rating Model Based on Tags for {ABSTRACT} Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/bupt\_pris\_2016-CX.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YinGPLL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

