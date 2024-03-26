# Proceedings - Contextual Suggestion 2014 

#### Overview of the TREC 2014 Contextual Suggestion Track

_Adriel Dean-Hall, Charles L. A. Clarke, Jaap Kamps, Paul Thomas, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/overview-context.pdf](http://trec.nist.gov/pubs/trec23/papers/overview-context.pdf)
??? abstract "Abstract"
	
	For participants familiar with the 2013 Contextual Suggestion Track we have provided a list of the main changes to this year's track: Assessors were recruited only from a crowdsourcing service (Mechanical Turk) and not from any student bodies. Only CSV formatted files were available for profiles, contexts, and suggestions. Two seed cities were used instead of one (Chicago, IL and Santa Fe, NM) and the target cities were also changed. The number of ratings provided in profiles was changed from 50 to 70 or 100 (depending on the profile). 31 runs were submitted from 17 groups, 6 of these were ClueWeb12 runs and 25 were open web runs. If you are already familiar with this track you can skip to Section 5 which gives an overview of the approaches participants used and Section 6 which contains the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Dean-HallCKTV14.bib) "
	```
	@inproceedings{DBLP:conf/trec/Dean-HallCKTV14,
		author = {Adriel Dean{-}Hall and Charles L. A. Clarke and Jaap Kamps and Paul Thomas and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2014 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/overview-context.pdf},
		timestamp = {Fri, 24 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Dean-HallCKTV14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A New Approach to Contextual Suggestions Based on Word2Vec

_Yongqiang Chen, Zhenjun Tang, Xiaozhao Zhao, Dawei Song, Peng Zhang_

- :fontawesome-solid-user-group: **Participant:** [TJU_CS_IR](./participants.md#tju_cs_ir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-TJU_CS_IR _cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-TJU_CS_IR _cs.pdf)
- :material-file-search: **Runs:** [runB](./runs.md#runb) | [runA](./runs.md#runa)

??? abstract "Abstract"
	
	We report our participation in the contextual suggestion track of TREC 2014 for which we submitted two runs using a novel approach to complete the competition. The goal of the track is to generate suggestions that users might fond of given the history of users' preference where he or she used to live in when they travel to a new city. We tested our new approach in the dataset of ClueWeb12-CatB which has been pre-indexed by Luence. Our system represents all attractions and user contexts in the continuous vector space learnt by neural network language models, and then we learn the user-dependent profile model to predict the user's ratings for the attraction's websites using Softmax. Finally, we rank all the venues by using the generated model according the users' personal preference.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenTZSZ14.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenTZSZ14,
		author = {Yongqiang Chen and Zhenjun Tang and Xiaozhao Zhao and Dawei Song and Peng Zhang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A New Approach to Contextual Suggestions Based on Word2Vec},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-TJU\_CS\_IR\ \_cs.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenTZSZ14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Applying Learning to Rank Techniques to Contextual Suggestions

_Julia Kiseleva, Alejandro Montes García, Yongming Luo, Mykola Pechenizkiy, Paul De Bra, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [eindhoven](./participants.md#eindhoven)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-eindhoven_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-eindhoven_cs.pdf)
- :material-file-search: **Runs:** [tueRforest](./runs.md#tuerforest) | [tueNet](./runs.md#tuenet)

??? abstract "Abstract"
	
	The Text Retrieval Conference's Contextual Suggestion Track investigates search techniques for complex information needs that are highly dependent on a context and user interests. The goal of the track is to evaluate systems that provide suggestions for activities to users in a specific location, taking into account their historical personal preferences. In this paper, we present our approach for the Contextual Sugges- tion Track 2014. We suggest to treat the problem of Con- textual Suggestion as a Learning to Rank problem. As a source for travel suggestions we use data from four social networks: Yelp, Facebook, Foursquare and Google Places. For our study we train two ranking algorithms: Rank Net and Random Forest. In our experiments, we seek to answer the following research questions: Does the distance between the locations of training and testing contexts impact precision? Which data sources (i.e., Facebook, Foursquare, Yelp, and Google Places) provide more effective training data?
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KiselevaGLPBK14.bib) "
	```
	@inproceedings{DBLP:conf/trec/KiselevaGLPBK14,
		author = {Julia Kiseleva and Alejandro Montes Garc{\'{\i}}a and Yongming Luo and Mykola Pechenizkiy and Paul De Bra and Jaap Kamps},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Applying Learning to Rank Techniques to Contextual Suggestions},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-eindhoven\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KiselevaGLPBK14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### User Modeling for Contextual Suggestion

_Hua Li, Rafael Alonso_

- :fontawesome-solid-user-group: **Participant:** [RAMA](./participants.md#rama)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-RAMA_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-RAMA_cs.pdf)
- :material-file-search: **Runs:** [RUN1](./runs.md#run1) | [RAMARUN2](./runs.md#ramarun2)

??? abstract "Abstract"
	
	This paper describes our work on the Contextual Suggestion Track of the Twenty-Third Text REtrieval Conference (TREC 2014). The key to our approach is user interest modeling. By building explicit models of user interests and information needs, we are able to make suggestions relevant to the user. We extended our Reinforcement and Aging Modeling Algorithm (RAMA) to create user interest models using the rated examples in a user profile as explicit relevance feedback. Two models, one for specific interests and the other for general interests, are built for each user profile. To ensure that the recommendations are contextually appropriate, we have also built a simple model to capture contextual relevance of a recommendation. Candidate suggestions are retrieved from the Yelp®1 website using its application programming interface. For each candidate, we calculate three component scores based on the specific interest model, the general interest model, and the context model, respectively. Final scoring and ranking are computed as a weighted linear combination of the component scores. We hypothesize that the relative weighting of the components may affect the performance of our system. To test the hypothesis, we have submitted two runs with different weighting schemes. In particular, RUN1 has a specific interest priority whereas RAMARUN2 has a general interest priority. TREC evaluation reveals that both runs performed significantly better than the median of all submitted runs (i.e., the Track Median) on three performance metrics. In addition, RAMARUN2 has a slight performance edge over RUN1. The effectiveness of our approach is evidenced by the TREC evaluation result that RAMARUN2 and RUN1 ranked #2 and #6 out of the 31 runs submitted by the 17 participating teams from around the world.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiA14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiA14,
		author = {Hua Li and Rafael Alonso},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {User Modeling for Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-RAMA\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiA14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2014 Contextual Suggestion Track: Hybrid Recommendation  Based on Open-web Information

_Hanchen Li, Zhen Yang, Yingxu Lai, Lijuan Duan, Kefeng Fan_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BJUT_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BJUT_cs.pdf)
- :material-file-search: **Runs:** [BJUTa](./runs.md#bjuta) | [BJUTb](./runs.md#bjutb)

??? abstract "Abstract"
	
	In this paper we describe our efforts for TREC contextual suggestion task. Our goal of this year is to evaluate the effectiveness of: (1) Preference crawling method that as far as possible to obtain more candidate spots' information from open-web to model the users' interest profiles; (2) Automatic summarization method that leverages the information from multiple resources to generate the description for each candidate scenic spots; (3) Hybrid recommendation method that combing a variety of factors to construct a system of hybrid recommendation system. Finally, we conduct extensive experiments to evaluate the proposed framework on TREC 2014 Contextual Suggestion data set, and, as would be expected, the results demonstrate its generality and superior performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiYLDF14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiYLDF14,
		author = {Hanchen Li and Zhen Yang and Yingxu Lai and Lijuan Duan and Kefeng Fan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2014 Contextual Suggestion Track: Hybrid Recommendation Based on Open-web Information},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BJUT\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiYLDF14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at Context Suggestion Track TREC 2014

_Zihao Lu, Zhijie Qiu, Liang Chang, Bingyang Liu, Dayong Wu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET_cs.pdf)
- :material-file-search: **Runs:** [lda](./runs.md#lda) | [cat](./runs.md#cat)

??? abstract "Abstract"
	
	This year we did not use ClueWeb12 or ClueWeb12-B,while we solve this issue based on data we crawled from openweb.Firstly, we use external structured resource -Google Place API[1] to find all of the possible candidate places in the distance of 5 hours' drive. Secondly, we use Yandex[2] to find a description of each place because we get URL of the corresponding place. Then, we classifythe descriptions of all places. Finally, we ranked the pages based on users' preferences.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuQCLWLC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuQCLWLC14,
		author = {Zihao Lu and Zhijie Qiu and Liang Chang and Bingyang Liu and Dayong Wu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at Context Suggestion Track {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-ICTNET\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuQCLWLC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC 2014 Contextual Suggestion Track

_Bilel Moulahi, Lynda Tamine, Sadok Ben Yahia_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-IRIT_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-IRIT_cs.pdf)
- :material-file-search: **Runs:** [choqrun](./runs.md#choqrun)

??? abstract "Abstract"
	
	In this work, we give an overview of our participation in the TREC 2014 Contextual Suggestion Track. To address the retrieval of attraction places, we propose a fuzzy-based document combination approach for preference learning and context processing. We use the open web in our submission and make use of both criteria users preferences and geographical location criteria.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoulahiTMY14.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoulahiTMY14,
		author = {Bilel Moulahi and Lynda Tamine and Sadok Ben Yahia},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IRIT} at {TREC} 2014 Contextual Suggestion Track},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-IRIT\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoulahiTMY14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Better Contextual Suggestions in ClueWeb12 Using Domain Knowledge  Inferred from The Open Web

_Thaer Samar, Arjen P. de Vries, Alejandro Bellogín_

- :fontawesome-solid-user-group: **Participant:** [CWI](./participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-CWI_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-CWI_cs.pdf)
- :material-file-search: **Runs:** [CWI_CW12_Full](./runs.md#cwi_cw12_full) | [CWI_CW12.MapWeb](./runs.md#cwi_cw12.mapweb)

??? abstract "Abstract"
	
	This paper provides an overview of our participation in the Contextual Suggestion Track. The TREC 2014 Contextual Suggestion Track allowed participants to submit personalized rankings using documents either from the Open Web or from an archived, static Web collection (ClueWeb12) collection. One of the main steps in recommending attractions for a particular user in a given context is the selection of the candidate documents. This task is more challenging when relying on ClueWeb12 collection rather than public tourist APIs for finding suggestions. In this paper, we present our approach for selecting candidate suggestions from the entire ClueWeb12 collection using the tourist domain knowledge available in the Open Web. We show that the generated recommendations to the provided user profiles and contexts improve significantly using this inferred domain knowledge.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SamarVB14.bib) "
	```
	@inproceedings{DBLP:conf/trec/SamarVB14,
		author = {Thaer Samar and Arjen P. de Vries and Alejandro Bellog{\'{\i}}n},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Better Contextual Suggestions in ClueWeb12 Using Domain Knowledge Inferred from The Open Web},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-CWI\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SamarVB14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Waterloo at TREC 2014 Contextual Suggestion: Experiments  with suggestion clustering

_Luchen Tan, Adriel Dean-Hall, Pragnya Addala, Charles L. A. Clarke_

- :fontawesome-solid-user-group: **Participant:** [waterloo_clarke](./participants.md#waterloo_clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-waterloo_clarke_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-waterloo_clarke_cs.pdf)
- :material-file-search: **Runs:** [waterlooA](./runs.md#waterlooa) | [waterlooB](./runs.md#waterloob)

??? abstract "Abstract"
	
	In this work we present our group's first attempt at developing a system to solve the problem presented in the contextual suggestion task. As part of TREC 2014 the contextual suggestion track is running for the third time. The goal of this task is to tailor point-of-interest suggestions to users according to this preferences. Here we present how we gathered candidate points-of-interest, grouped them according to similarity using clustering, and picked points-of-interest that each user would find especially appealing. The organizers of this track distributed users' personal profiles in three files: examples2014.csv, profiles2014-70.csv and profiles2014-100.csv. A list of 100 example points-of-interest, which each consist of an ID, a title, a description and a URL were included in examples2014.csv. 299 users indicated their preferences by giving a rating on a 5-point score (0, 1, 2, 3, 4) to the description and website of each example point-of-interest. 116 users, indicated preferences to all the 100 example points of interests, these profiles are distributed in profiles2014-100.csv. The other 183 users, only indicated 70% of all the example points of interest, these profiles are distributed in profiles2014-70.csv. There are 50 contexts which each represent a city in the United States which are listed in contexts2014.txt. Each group is permitted to submit up to 2 runs of suggested point of interests in the 50 contexts. Below we describe in detail our approach for building both of our runs
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TanDAC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/TanDAC14,
		author = {Luchen Tan and Adriel Dean{-}Hall and Pragnya Addala and Charles L. A. Clarke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Waterloo at {TREC} 2014 Contextual Suggestion: Experiments with suggestion clustering},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-waterloo\_clarke\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TanDAC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploration of Opinion-aware Approach to Contextual Suggestion

_Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_fang_cs.pdf)
- :material-file-search: **Runs:** [UDInfoCS2014_1](./runs.md#udinfocs2014_1) | [UDInfoCS2014_2](./runs.md#udinfocs2014_2)

??? abstract "Abstract"
	
	In this paper we describe our effort on TREC Contextual Suggestion Track. Using resources such as description or websites of example suggestions to build user profile has been proven to be effective on last year's TREC. This year we also leverage the power of using user profile. Real world opinions of the suggestions are used in our method to build both user profile and candidate suggestion profile. Two ranking method are investigated to rank the candidate suggestions: linear interpolation and learning to rank. For description generation, we apply the similar method as used in the last year. The structured description combines the category information of the suggestion, meta-description of the website, reviews of the suggestion and the similar example suggestions that the user liked. Official results of our submitted runs show the effectiveness of the proposed method.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangF14.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangF14,
		author = {Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Exploration of Opinion-aware Approach to Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_fang\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangF14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Delaware at TREC 2014

_Ashraf Bah, Karankumar Sabhnani, Mustafa Zengin, Ben Carterette_

- :fontawesome-solid-user-group: **Participant:** [udel](./participants.md#udel)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-udel_cs-federated-microblog-web-sesson.pdf)
- :material-file-search: **Runs:** [run_DwD](./runs.md#run_dwd) | [run_FDwD](./runs.md#run_fdwd)

??? abstract "Abstract"
	
	This paper describes the work of the Information Retrieval Lab at the University of Delaware (team name “udel”) on TREC 2014 tracks. We participated in five different tracks: Contextual Suggestion, Federated Web, Microblog, Session, and Web.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BahSZC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/BahSZC14,
		author = {Ashraf Bah and Karankumar Sabhnani and Mustafa Zengin and Ben Carterette},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Delaware at {TREC} 2014},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-udel\_cs-federated-microblog-web-sesson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BahSZC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Modelling Psychological Needs for User-dependent Contextual Suggestion

_Di Xu, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [Group.Xu](./participants.md#group.xu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-Group.Xu_cs.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-Group.Xu_cs.pdf)
- :material-file-search: **Runs:** [dixlticmu](./runs.md#dixlticmu)

??? abstract "Abstract"
	
	This paper presents our approach for the Contextual Suggestion track of 2014 Text REtrieval Conference (TREC). The task aims to provide recommendations on points of interests (POI) for various kinds of users under different contexts. This becomes challenging due to the limited amount of training data provided by TREC and the demanding constraints for a suggestion to be judged as relevant. Our approach does not deviate from existing Machine Learning based methods in principle, but sticks closely to the defined relevance judgement criteria, by focusing primarily on modelling users' preferences on POI categories, and investigating upon their psychological expectations on the textual descriptions of the POIs. The latter is considered as our novelty in this work. Support Vector Regression was used for suggestion ranking, an ad-hoc web information extractor was used to collect POI descriptions, and a description evaluation mechanism was engaged to select proper POI descriptions subject to the nature of the POIs. Our results suggest that our methods are effective in obtaining satisfying user-specific POI rankings and generating descriptions that meet users' psychological expectations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuC14.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuC14,
		author = {Di Xu and Jamie Callan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Modelling Psychological Needs for User-dependent Contextual Suggestion},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-Group.Xu\_cs.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuC14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2014: Web, Session, and Contextual Suggestion Tracks

_Matthias Hagen, Steve Goering, Maximilian Michel, Georg Müller, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [BUW](./participants.md#buw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-BUW_cs-session-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-BUW_cs-session-web.pdf)
- :material-file-search: **Runs:** [webis_1](./runs.md#webis_1) | [webis_2](./runs.md#webis_2)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2014 Web, Session and Contextual Suggestion tracks. All our runs for the Web and the Session track are on the full ClueWeb12 and use the online Indri retrieval system hosted at CMU. Our runs for the Contextual Suggestion track are based on the open web. As for the Web track, our runs are aimed at one research question: whether using axioms for re-ranking a baseline result list improve the retrieval performance. Therefore, we implement the axioms available in the axiomatic IR literature and combine them with new axioms aimed at term proximity. Trained on the TREC 2013 Web track data, three promising combinations of axioms are identified in a large-scale experiment and used for our three runs. As for the session track, we tackle three research questions in three different runs. First, similar to the Web track, we examine whether an axiom combination helps to improve session retrieval. Second, we examine the effect of presenting relevant documents from previous years when they seem to be related to the current queries of the 2014 data. Our third question is whether the user interactions can be used to train an activation model to predict relevant documents for new queries. As for the contextual suggestion track, our research question is whether explanations based on the user profile and explaining why specific entities are suggested by the system are perceived positively or negatively by the user. Our focus is not explicitly on finding the most relevant suggestions but rather on examining the effect of different descriptions. Thus, the system for finding the suggestions is simply based on techniques shown promising in the previous years. Our first run uses “standard” descriptions while in the second run the standard description is enriched by a profile specific sentence explaining the reasoning underlying the suggestion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenGMMS14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenGMMS14,
		author = {Matthias Hagen and Steve Goering and Maximilian Michel and Georg M{\"{u}}ller and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2014: Web, Session, and Contextual Suggestion Tracks},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-BUW\_cs-session-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenGMMS14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Venue Recommendation and Web Search Based on Anchor Text

_Seyyed Hadi Hashemi, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-UAmsterdam_cs-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-UAmsterdam_cs-web.pdf)
- :material-file-search: **Runs:** [Model1](./runs.md#model1) | [Model0](./runs.md#model0)

??? abstract "Abstract"
	
	This paper presents the University of Amsterdam's participation in TREC 2014. For the Contextual Suggestion Track, we experimented with the use of anchor text representations in the language modeling framework, and base our runs either on full ClueWeb12 or the subset of touristic aggregators (e.g., tripadvisor) provided by the organizers of the track. We also look at the effectiveness of priors (in particular, PageRank) and ways of formulating the query based on the context. Our main finding is that the anchor text representation is effective for retrieving candidate attractions, and performs better than a standard document text index. A linear combination of both anchor and document text leads to further improvement. For the Web Track, we continued our experiment with the fusion of anchor text relative to the text-based baseline run. Our main finding is, again, that the combination of anchor and document text leads to improvement, and we demonstrate how the fusion weight can be used as a handle to tune the amount of risk acceptable for the risk sensitive evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HashemiK14.bib) "
	```
	@inproceedings{DBLP:conf/trec/HashemiK14,
		author = {Seyyed Hadi Hashemi and Jaap Kamps},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Venue Recommendation and Web Search Based on Anchor Text},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-UAmsterdam\_cs-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HashemiK14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2014: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Web Tracks

_Richard McCreadie, Romain Deveaud, M-Dyaa Albakour, Stuart Mackie, Nut Limsopatham, Craig Macdonald, Iadh Ounis, Thibaut Thonet, Bekir Taner Dinçer_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec23/papers/pro-uogTr_cs-ts-web.pdf](http://trec.nist.gov/pubs/trec23/papers/pro-uogTr_cs-ts-web.pdf)
- :material-file-search: **Runs:** [uogTrBunSumF](./runs.md#uogtrbunsumf) | [uogTrCsLtrF](./runs.md#uogtrcsltrf)

??? abstract "Abstract"
	
	In TREC 2014, we focus on tackling the challenges posed by the Contextual Suggestion and Temporal Summarisation tracks, as well as enhancing our existing technologies to tackle risk-sensitivity as part of the Web track, building upon our Terrier Information Retrieval Platform. In particular, for the Contextual Suggestion track, we propose a novel bundled venue retrieval approach and experiment with text-based summarisation for building the venue description. For our participation to the Temporal Summarisation track, we propose a general framework for performing summarisation over time and two new real-time filtering approaches that leverage the semi-structured nature of news articles to enhance summary coverage. For the TREC Web track, we investigated a novel risk-sensitive learning to rank approach that is based on hypothesis testing and examined approaches that selectively apply different retrieval techniques based upon the query, with the aim of minimising risk.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieDAMLMO14.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieDAMLMO14,
		author = {Richard McCreadie and Romain Deveaud and M{-}Dyaa Albakour and Stuart Mackie and Nut Limsopatham and Craig Macdonald and Iadh Ounis and Thibaut Thonet and Bekir Taner Din{\c{c}}er},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow at {TREC} 2014: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Web Tracks},
		booktitle = {Proceedings of The Twenty-Third Text REtrieval Conference, {TREC} 2014, Gaithersburg, Maryland, USA, November 19-21, 2014},
		series = {{NIST} Special Publication},
		volume = {500-308},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2014},
		url = {http://trec.nist.gov/pubs/trec23/papers/pro-uogTr\_cs-ts-web.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieDAMLMO14.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

