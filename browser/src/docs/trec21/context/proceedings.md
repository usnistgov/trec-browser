# Proceedings - Contextual Suggestion 2012 

#### Overview of the TREC 2012 Contextual Suggestion Track

_Adriel Dean-Hall, Charles L. A. Clarke, Jaap Kamps, Paul Thomas, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/CONTEXTUAL12.overview.pdf](http://trec.nist.gov/pubs/trec21/papers/CONTEXTUAL12.overview.pdf)
??? abstract "Abstract"
	
	The contextual suggestion track investigates search techniques for complex information needs that are highly dependent on context and user interests. According to a report from the Second Strategic Workshop on Information Retrieval in Lorne [1]: “Future information retrieval systems must anticipate user needs and respond with information appropriate to the current context without the user having to enter an explicit query. . . In a mobile context such a system might take the form of an app that recommends interesting places and activities based on the user's location, personal preferences, past history, and environmental factors such as weather and time. . . In contrast to many traditional recommender systems, these systems must be open domain, ideally able to make suggestion and synthesize information from multiple sources. . . ” For example, imagine a group of information retrieval researchers with a November evening to spend in beautiful Gaithersburg, Maryland. A contextual suggestion system might recommend a beer at the Dogfish Head Alehouse (www.dogfishalehouse.com), dinner at the Flaming Pit (www.flamingpitrestaurant.com), or even a trip into Washington on the metro to see the National Mall (www.nps.gov/nacc). As its primary goal, the contextual suggestion track seeks to develop evaluation methodologies for such systems. TREC 2012 is the first year for the track. For this first year, we introduced a single task to evaluate contextual suggestion from the open Web. As input to the task participants were given a set of example suggestions, a set of user preference profiles, and a set of geotemporal contexts. The task was to take the profiles and contexts and to produce up to 50 ranked suggestions for each combination of profile and context. Participants gathered suggestions from the open Web. Each profile corresponds to a single user, and indicates that user's preference with respect to each sample suggestion. For example, one suggestion might be to have a beer at the Dogfish Head Alehouse, and the profile might include a negative preference with respect to this suggestion. Each suggestion includes a title, description, and an associated URL. Each context corresponds to a particular geotemporal location, including city, day of the week, time of day, and season. For example, the context might be Gaithersburg, Maryland, on a weekday evening in the fall. The geographical contexts are very coarse-grained (i.e., an entire city) to help simplify the task. A total of 14 groups submitting 27 runs participated in this first year of the track, this includes the 2 baseline submissions from CSIRO and 2 baseline submissions from the University of Waterloo. These baselines will be discussed later in this report. Given the newness of the track, participants were given the option of basing their suggestions solely on the user profiles (returning suggstions appropriate to any place and time) or solely on geotemporal context (returning suggestions appropriate to a generic user). Only one group, from the University of Delaware, took advantage of this option, submitting runs based solely on user profile.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Dean-HallCKTV12.bib) "
	```
	@inproceedings{DBLP:conf/trec/Dean-HallCKTV12,
		author = {Adriel Dean{-}Hall and Charles L. A. Clarke and Jaap Kamps and Paul Thomas and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2012 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/CONTEXTUAL12.overview.pdf},
		timestamp = {Fri, 24 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Dean-HallCKTV12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC 2012 Contextual Suggestion Track

_Gilles Hubert, Guillaume Cabanac_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/IRIT.context.final.pdf](http://trec.nist.gov/pubs/trec21/papers/IRIT.context.final.pdf)
- :material-file-search: **Runs:** [iritSplit3CPv1](./runs.md#iritsplit3cpv1) | [iritSplit3CPv2](./runs.md#iritsplit3cpv2)

??? abstract "Abstract"
	
	In this paper we give an overview of the participation of the IRIT lab, University of Toulouse, France, in the TREC 2012 Contextual Suggestion Track. We present our personalized contextual retrieval framework, an approach for context processing, and two approaches for user preference processing. The official evaluations of our two submitted runs are reported and compared to the four baselines defined for the track. Evaluation results show that one of our submitted run was ranked 1st among the 27 runs of the 14 participants for the two official evaluation measures of the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HubertC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/HubertC12,
		author = {Gilles Hubert and Guillaume Cabanac},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRIT} at {TREC} 2012 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/IRIT.context.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HubertC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Contextual Suggestion from Wikitravel: Exploiting Community-Based  Suggestions

_Marijn Koolen, Jaap Kamps, Hugo C. Huurdeman_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UAmsterdam.contextual.final.pdf](http://trec.nist.gov/pubs/trec21/papers/UAmsterdam.contextual.final.pdf)
- :material-file-search: **Runs:** [UAmsCS12wtSUM](./runs.md#uamscs12wtsum) | [UAmsCS12wtSUMb](./runs.md#uamscs12wtsumb)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2012 Contextual Suggestion Track. The goal of the track is to evaluate systems that provide suggestions for activities to users in a specific location, at a specific time, taking into account their personal preferences. As a source for travel suggestions we use Wikitravel, which is a community-based travel guide for destinations all over the world. From pages dedicated to cities in the US we extract suggestions for sightseeing, shopping, eating and drinking. Descriptions from positive examples in the user profiles are used as queries to rank all suggestions in the US. Our baseline approach merges the per-query rankings of all positive examples of all users. Our user-dependent approach merges the per-query rankings of the positive examples of a single user. The rankings suggestions are then filtered based on the location of the user. We ignore the temporal aspects of the context. The user-dependent rankings are more effective for contextual suggestion than user-independent rankings. The two systems show similar perform on the geographical dimension, but the user-dependent system provides more interesting suggestions. Our results show that information on user preferences is valuable for providing appropriate suggestions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoolenKH12.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoolenKH12,
		author = {Marijn Koolen and Jaap Kamps and Hugo C. Huurdeman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Contextual Suggestion from Wikitravel: Exploiting Community-Based Suggestions},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UAmsterdam.contextual.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KoolenKH12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Context Suggestion Track TREC 2012

_Bingyang Liu, Tong Wu, Xianghui Lin, Yanqin Zhong, Qian Liu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/ICTNET.contextual.final.pdf](http://trec.nist.gov/pubs/trec21/papers/ICTNET.contextual.final.pdf)
- :material-file-search: **Runs:** [ICTCONTEXTRUN1](./runs.md#ictcontextrun1) | [ICTCONTEXTRUN2](./runs.md#ictcontextrun2)

??? abstract "Abstract"
	
	Yelp'is used to collect the initial candidate web site list for every context. Then we use a spider to fetch contents of each candidate site. We also classify the candidates and examples into 6 classes and calculate preference of each profile to each class. The classes and preference are used for the ranking of the results. Finally we use several methods to filter and generate descriptions for every web site that is returned in the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuWLZLLC12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuWLZLLC12,
		author = {Bingyang Liu and Tong Wu and Xianghui Lin and Yanqin Zhong and Qian Liu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ICTNET} at Context Suggestion Track {TREC} 2012},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/ICTNET.contextual.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuWLZLLC12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Contextual Suggestion

_Abhishek Mallik, Mandar Mitra, Kripabandhu Ghosh_

- :fontawesome-solid-user-group: **Participant:** [isi_paik](./participants.md#isi_paik)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/isi_paik.contextual.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/isi_paik.contextual.nb.pdf)
- :material-file-search: **Runs:** [watcs12a](./runs.md#watcs12a) | [watcs12b](./runs.md#watcs12b)

??? abstract "Abstract"
	
	The goal of this project is to build a Contextual Suggestion system that will recommend the usel a lanked list of suggestions depending on user's context as well as her preferences. In this context we pr€6ent an algorithm based on the regular expression for extra.ting time and address information from different websites for the places. Then we have suggested a ranking function that can utilize these timing and address information of those places as well as the users' context and preferences to rank the places. Here the page6 are unstructured but the address is structured i.e. template based as we have worked with only the plaaes located at Toronto, Canada.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MallikMG12.bib) "
	```
	@inproceedings{DBLP:conf/trec/MallikMG12,
		author = {Abhishek Mallik and Mandar Mitra and Kripabandhu Ghosh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/isi\_paik.contextual.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MallikMG12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding, Weighting and Describing Venues: CSIRO at the 2012 TREC  Contextual Suggestion Track

_David N. Milne, Paul Thomas, Cécile Paris_

- :fontawesome-solid-user-group: **Participant:** [csiro](./participants.md#csiro)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/csiro.contextual.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/csiro.contextual.nb.pdf)
- :material-file-search: **Runs:** [baselineB](./runs.md#baselineb) | [baselineA](./runs.md#baselinea) | [csiroth](./runs.md#csiroth) | [csiroht](./runs.md#csiroht)

??? abstract "Abstract"
	
	We report on the participation of CSIRO1 in the TREC 2012 contextual suggestion track, for which we submitted four runs. Two submissions were baselines that investigate the performance of a commercial system (namely the Google Places API), and whether the current experimental setup encourages diversity. The remaining two submissions were more complex approaches that explore the importance of time and personal preference. For the former, check-in statistics provided by Foursquare were used to identify which times of day and which days of week venues are more likely or less likely to be frequented. For the latter, textual similarity was used to weight venues with respect to positive and negative examples provided for each profile. Our submissions all fall either slightly above or slightly below the mean, depending on how they are judged. Interestingly, our baselines consistently outperform our more complex submissions, which suggests that a) venue quality (as given by Google review score) is a more important signal than either time or personal preference, at least in the context of this evaluation, and b) that the evaluation is biased to a specific type of venue, namely pubs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MilneTP12.bib) "
	```
	@inproceedings{DBLP:conf/trec/MilneTP12,
		author = {David N. Milne and Paul Thomas and C{\'{e}}cile Paris},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Finding, Weighting and Describing Venues: {CSIRO} at the 2012 {TREC} Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/csiro.contextual.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MilneTP12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2012 Contextual Suggestion Track

_Lin Qiu, JunRui Peng, Qianqian Wang, Yue Liu, Zhihua Zhou, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/PRIS.context.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/PRIS.context.nb.pdf)
- :material-file-search: **Runs:** [PRISabc](./runs.md#prisabc)

??? abstract "Abstract"
	
	The system to Contextual Suggestion Track at TREC2012 includes information crawling and preprocessing, context filtering, user modeling, similarity computing and ranking, description generating. Some third party tool kits are used, such as URLPARSE. TF-IDF (term frequency-inverse document frequency) and cosine similarity is also used for building user models and computed similarities between users and candidate items.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiuPWLZXCG12.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiuPWLZXCG12,
		author = {Lin Qiu and JunRui Peng and Qianqian Wang and Yue Liu and Zhihua Zhou and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2012 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/PRIS.context.nb.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiuPWLZXCG12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TNO and RUN at the TREC 2012 Contextual Suggestion Track: Recommending  Personalized Touristic Sights Using Google Places

_Maya Sappelli, Wessel Kraaij, Suzan Verberne_

- :fontawesome-solid-user-group: **Participant:** [TNO_RadboudUniv](./participants.md#tno_radbouduniv)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/TNO_RadboudUniv.contextual.final.pdf](http://trec.nist.gov/pubs/trec21/papers/TNO_RadboudUniv.contextual.final.pdf)
- :material-file-search: **Runs:** [run01TI](./runs.md#run01ti) | [run02K](./runs.md#run02k)

??? abstract "Abstract"
	
	The purpose of the Contextual Suggestion track is to suggest personalized touristic activities to an individual, given a certain location and time. In our approach, we collected initial recommendations by using the location context as search query in Google Places. We first ranked the recommendations based on their textual similarity to the user profiles. In order to improve the ranking of popular sights, we combined the resulted ranking with a number of other rankings based on Google Search, popularity and categories. Finally, we performed filtering based on the temporal context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SappelliKV12.bib) "
	```
	@inproceedings{DBLP:conf/trec/SappelliKV12,
		author = {Maya Sappelli and Wessel Kraaij and Suzan Verberne},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TNO} and {RUN} at the {TREC} 2012 Contextual Suggestion Track: Recommending Personalized Touristic Sights Using Google Places},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/TNO\_RadboudUniv.contextual.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SappelliKV12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Exploraton of Ranking-Based Strategy for Contextual Suggestion

_Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/udel_fang.contextual.final.pdf](http://trec.nist.gov/pubs/trec21/papers/udel_fang.contextual.final.pdf)
- :material-file-search: **Runs:** [UDInfoCSTc](./runs.md#udinfocstc) | [UDInfoCSTdc](./runs.md#udinfocstdc)

??? abstract "Abstract"
	
	The purpose of the Contextual Suggestion track is to suggest personalized touristic activities to an individual, given a certain location and time. In our approach, we collected initial recommendations by using the location context as search query in Google Places. We first ranked the recommendations based on their textual similarity to the user profiles. In order to improve the ranking of popular sights, we combined the resulted ranking with a number of other rankings based on Google Search, popularity and categories. Finally, we performed filtering based on the temporal context.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangF12,
		author = {Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {An Exploraton of Ranking-Based Strategy for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/udel\_fang.contextual.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### (Not Too) Personalized Learning to Rank for Contextual Suggestion

_Andrew Yates, Dave DeBoer, Hui Yang, Nazli Goharian, Steve Kunath, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [Georgetown](./participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/Georgetown.contextual.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/Georgetown.contextual.nb.pdf)
- :material-file-search: **Runs:** [gufinal](./runs.md#gufinal) | [guinit](./runs.md#guinit)

??? abstract "Abstract"
	
	In this work, we emphasize how to merge and re-rank contextual suggestions from the open Web based on a user‟s personal interests. We retrieve relevant results from the open Web by identifying context-independent queries, combining them with location information, and issuing the combined queries to multiple Web search engines. Our learning to rank model utilizes three types of profiles (a general profile, a city profile, and a personal profile) to re-rank and merge the results retrieved from the Web. We find that the learning model generates better results when the user profiles‟ weights are biased heavily towards major personal interests. The detections of major, minor and negative personal interests are done by statistical analysis across users, examples, and context-independent query types. For user interests detected by query types, we call the interests “macro-level interests”, while for user interest detected by examples, we call them “micro-level interests”. In our experiments, we find that “micro-level interests” effectively avoid favoring too much towards rare query types such as spa and game, and thus yields more balanced rankings. Finally, for the top ranked suggestions for each user and context, we generate result descriptions by learning to rank favorable Yelp comments and using a natural language generation algorithm to generate positive comments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YatesDYGKF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/YatesDYGKF12,
		author = {Andrew Yates and Dave DeBoer and Hui Yang and Nazli Goharian and Steve Kunath and Ophir Frieder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {(Not Too) Personalized Learning to Rank for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/Georgetown.contextual.nb.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YatesDYGKF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

