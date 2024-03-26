# Proceedings - Incident Streams 2018 

#### CBNU at TREC 2018 Incident Streams Track

_Won-Gyu Choi, Seung-Hyeon Jo, Kyung-Soon Lee_

- :fontawesome-solid-user-group: **Participant:** [cbnu](./participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/cbnu-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/cbnu-IS.pdf)
- :material-file-search: **Runs:** [cbnuC1](./runs.md#cbnuc1) | [cbnuC2](./runs.md#cbnuc2) | [cbnuS2](./runs.md#cbnus2) | [cbnuS1](./runs.md#cbnus1)

??? abstract "Abstract"
	
	This paper describes the participation of the CBNU team at the TREC Incident Streams Track 2018. For tweet representation, crisis-related terms are represented as conceptual entities. For tweet classification, we have compared support vector machines and our deep learning model which combines class activation mapping with one-shot learning in convolutional neural networks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChoiJL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChoiJL18,
		author = {Won{-}Gyu Choi and Seung{-}Hyeon Jo and Kyung{-}Soon Lee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CBNU} at {TREC} 2018 Incident Streams Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/cbnu-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChoiJL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### EPIC_MR Participation in the TREC 2018 Incidence Stream Track

_Simon W. Y. Chung, K. K. Lo_

- :fontawesome-solid-user-group: **Participant:** [EPIC_MR](./participants.md#epic_mr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/EPIC_MR-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/EPIC_MR-IS.pdf)
- :material-file-search: **Runs:** [myrun-11](./runs.md#myrun-11) | [myrun-10](./runs.md#myrun-10) | [myrun-2](./runs.md#myrun-2) | [myrun-21](./runs.md#myrun-21)

??? abstract "Abstract"
	
	This paper describes our participation of the EPIC_MR group to the TREC 2018 Incident Streams Track. The target of the track is to monitor the social media and classify different type of information to help different response agencies. This paper describes our approach to use the words with Wikipedia articles to build the training vector, and also the result and comments of our runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChungL18.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChungL18,
		author = {Simon W. Y. Chung and K. K. Lo},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {EPIC{\_}MR Participation in the {TREC} 2018 Incidence Stream Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/EPIC\_MR-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChungL18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Neural Networks and Support Vector Machine based Approach for Classifying  Tweets by Information Types at TREC 2018 Incident Streams Task

_Abu Nowshed Chy, Umme Aymun Siddiqua, Masaki Aono_

- :fontawesome-solid-user-group: **Participant:** [KDEIS](./participants.md#kdeis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/KDEIS-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/KDEIS-IS.pdf)
- :material-file-search: **Runs:** [KDEIS2_ACBLSTM](./runs.md#kdeis2_acblstm) | [KDEIS1_CLSTM](./runs.md#kdeis1_clstm) | [KDEIS3_ACSBLSTM](./runs.md#kdeis3_acsblstm) | [KDEIS4_DM](./runs.md#kdeis4_dm)

??? abstract "Abstract"
	
	Microblog, especially twitter, is treated as an important source to serve the situational information needs during a disaster period. Monitoring and producing the curated tweets based on different information types from massive twitter posts provide enormous opportunities to different public safety personnel or used for post-incident analysis. In this paper, we present our approach to addressing the problem defined in the TREC 2018 incident streams (TREC-IS) task. The task is to classify the tweets in each event/incident's stream into different high-level information types within the incident ontology. In our approach, we employ different deep neural network (DNN) classifiers in combination with a multi-class support vector machine (SVM) classifier and a rule-based classifier. We consider a rich set of hand-crafted features to train our multi-class SVM classifier, whereas a pre-trained word2vec model is used for the DNN based classifiers. Moreover, we introduce a set of rules based on the language of tweets, exploiting indicator terms, and WH-orientation of tweets for our rule-based classifier. Experimental results showed that our proposed KDEIS4 DM method obtained the second position among the participants in TREC-IS task and outperforms the participant median by more than 8% and 5% in terms of F1 Score and accuracy, respectively
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChySA18.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChySA18,
		author = {Abu Nowshed Chy and Umme Aymun Siddiqua and Masaki Aono},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Neural Networks and Support Vector Machine based Approach for Classifying Tweets by Information Types at {TREC} 2018 Incident Streams Task},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/KDEIS-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChySA18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SINAI at TREC 2018: Experiments in Incident Streams

_Miguel Ángel García Cumbreras, Manuel Carlos Díaz-Galiano, Manuel García Vega, Salud María Jiménez Zafra_

- :fontawesome-solid-user-group: **Participant:** [SINAI](./participants.md#sinai)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/SINAI-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/SINAI-IS.pdf)
- :material-file-search: **Runs:** [SINAI_run1](./runs.md#sinai_run1) | [SINAI_run2](./runs.md#sinai_run2) | [SINAI_run3](./runs.md#sinai_run3) | [SINAI_run4](./runs.md#sinai_run4)

??? abstract "Abstract"
	
	This paper describes the system architecture of the University of Jaén - SINAI team's for the TREC 2018 Incident Streams Track. The goal of the challenge is to automatically process social media streams during emergency situations with the aim of categorizing information and aid requests made on social media for emergency service operators. We explored four alternatives: baseline experimentation, WordNet synonyms, spelling correction and word embeddings. All of them use Support Vector Machine (SVM) as machine learning method. Our experiments reveal that the last approach leads to improve the baseline result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CumbrerasDVZ18.bib) "
	```
	@inproceedings{DBLP:conf/trec/CumbrerasDVZ18,
		author = {Miguel {\'{A}}ngel Garc{\'{\i}}a Cumbreras and Manuel Carlos D{\'{\i}}az{-}Galiano and Manuel Garc{\'{\i}}a Vega and Salud Mar{\'{\i}}a Jim{\'{e}}nez Zafra},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{SINAI} at {TREC} 2018: Experiments in Incident Streams},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/SINAI-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CumbrerasDVZ18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2018: Incident Streams Track

_Ning Lu, Hesong Wang, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/BJUT-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/BJUT-IS.pdf)
- :material-file-search: **Runs:** [myrun2](./runs.md#myrun2) | [myrun1](./runs.md#myrun1)

??? abstract "Abstract"
	
	In this paper we will introduce our work on the 2018 TREC real-time event flow test task. With the development of social media, more and more people choose to use social media to share their lives. Similarly, when encountering unexpected situations such as fires, earthquakes, flash floods, tsunamis, mudslides and other natural disasters or shootings, robberies and other emergencies, people like to release the progress of the disaster situation or event through social media. This task is to filter the information of such natural disasters or emergencies through text detection, and to classify the information, and finally to report the marked information to relevant staff according to different priorities. Let the staff know about the progress of the incident and the local real-time situation in case of rescue. This article will introduce the framework and methods of the classification system, as well as the experimental results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuW018.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuW018,
		author = {Ning Lu and Hesong Wang and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2018: Incident Streams Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/BJUT-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuW018.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT-BHU In TREC 2018 Incidents Stream Track

_Harshit Mehrotra, Sukomal Pal_

- :fontawesome-solid-user-group: **Participant:** [IIT-BHU](./participants.md#iit-bhu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/IIT-BHU-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/IIT-BHU-IS.pdf)
- :material-file-search: **Runs:** [IITBHU1](./runs.md#iitbhu1) | [IITBHU12](./runs.md#iitbhu12)

??? abstract "Abstract"
	
	This paper presents details of the work done by the team of IIT (BHU) Varanasi for the Incidents Stream track in TREC 2018. The task involved classifying tweets posted during a disaster into a number of categories, which are useful for relief work purposes at such a time. The data given was in the form of tweets from one earthquake, tornado, wildfire, flood, shooting and bombing incident.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MehrotraP18.bib) "
	```
	@inproceedings{DBLP:conf/trec/MehrotraP18,
		author = {Harshit Mehrotra and Sukomal Pal},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IIT-BHU} In {TREC} 2018 Incidents Stream Track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/IIT-BHU-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MehrotraP18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NHK STRL at TREC 2018 Incident Streams track

_Taro Miyazaki, Kiminobu Makino, Yuka Takei, Hiroki Okamoto, Jun Goto_

- :fontawesome-solid-user-group: **Participant:** [NHK](./participants.md#nhk)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/NHK-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/NHK-IS.pdf)
- :material-file-search: **Runs:** [NHK_run2](./runs.md#nhk_run2) | [NHK_run3](./runs.md#nhk_run3) | [NHK_run1](./runs.md#nhk_run1) | [NHK_run4](./runs.md#nhk_run4)

??? abstract "Abstract"
	
	We describe NHK STRL's models for the TREC 2018 Incident Streams track. The goal of this track is classifying incident related Tweets into information types such as InformationWanted and EmergingThreats. The number of provided pieces of training data is about 2,000, which is not enough for current machine learning methods. We propose two models to overcome this small amount of data scenario: a knowledge base-based model and a model that considers meta-information. In addition, we used two bag-of-words baseline models, a multi-layer perceptron-based one and a support vector machine-based one, for comparison. Evaluation results show that our models can classify Tweets with a rather high F1 score.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MiyazakiMTOG18.bib) "
	```
	@inproceedings{DBLP:conf/trec/MiyazakiMTOG18,
		author = {Taro Miyazaki and Kiminobu Makino and Yuka Takei and Hiroki Okamoto and Jun Goto},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{NHK} {STRL} at {TREC} 2018 Incident Streams track},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/NHK-IS.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MiyazakiMTOG18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DICE @ TREC-IS 2018: Combining Knowledge Graphs and Deep Learning  to Identify Crisis-Relevant Tweets

_Hamada M. Zahera, Rricha Jalota, Ricardo Usbeck_

- :fontawesome-solid-user-group: **Participant:** [DICE-UPB](./participants.md#dice-upb)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec27/papers/DICE-UPB-IS.pdf](https://trec.nist.gov/pubs/trec27/papers/DICE-UPB-IS.pdf)
- :material-file-search: **Runs:** [UPB_DICE1](./runs.md#upb_dice1) | [UPB_DICE2](./runs.md#upb_dice2) | [UPB_DICE4](./runs.md#upb_dice4) | [UPB_DICE3](./runs.md#upb_dice3)

??? abstract "Abstract"
	
	In this paper, we describe our submissions to the TREC Incident Stream (TREC-IS) challenge 2018. We investigated different machine learning approaches to classify crisis-related tweets into different information types. We incorporated knowledge graphs as features into this social media analysis, in addition to bag of words, word embeddings, time data, and event-types. Further, we evaluate state-of-the-art classification models on 31 generated features sets. Our TREC-IS results indicate that a model based on combining knowledge graphs (i.e., Babelfy), word embeddings and textual features outperformes classical machine learning models
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZaheraJU18.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZaheraJU18,
		author = {Hamada M. Zahera and Rricha Jalota and Ricardo Usbeck},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DICE} @ {TREC-IS} 2018: Combining Knowledge Graphs and Deep Learning to Identify Crisis-Relevant Tweets},
		booktitle = {Proceedings of the Twenty-Seventh Text REtrieval Conference, {TREC} 2018, Gaithersburg, Maryland, USA, November 14-16, 2018},
		series = {{NIST} Special Publication},
		volume = {500-331},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2018},
		url = {https://trec.nist.gov/pubs/trec27/papers/DICE-UPB-IS.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZaheraJU18.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

