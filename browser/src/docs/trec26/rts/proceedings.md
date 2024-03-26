# Proceedings - Real-time Summarization 2017 

#### Overview of the TREC 2017 Real-Time Summarization Track

_Jimmy Lin, Salman Mohammed, Royal Sequiera, Luchen Tan, Nimesh Ghelani, Mustafa Abualsaud, Richard McCreadie, Dmitrijs Milajevs, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-RT.pdf)
??? abstract "Abstract"
	
	The TREC 2017 Real-Time Summarization (RTS) Track is the second iteration of a community effort to explore techniques, algorithms, and systems that automatically monitor streams of social media posts such as tweets on Twier to address users' prospective information needs. These needs are articulated as “interest profiles”, akin to topics in ad hoc retrieval. In real-time summarization, the goal is for a system to deliver interesting and novel content to users in a timely fashion. We refer to these messages generically as “updates”. For example, the user might be concerned about tensions on the Korean Peninsula and wishes to be notified whenever there are new developments. Real-Time Summarization was introduced at TREC 2016 [8] and represented the merger of the Microblog (MB) Track, which ran from 2010 to 2015, and the Temporal Summarization (TS) Track, which ran from 2013 to 2015 [ 2 ]. The creation of RTS was designed to leverage synergies between the two tracks in exploring prospective information needs over document streams. The evaluation design is largely based on the real-time filtering task in the TREC 2015 Microblog Track [7]. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinMSTGAMMV17.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinMSTGAMMV17,
		author = {Jimmy Lin and Salman Mohammed and Royal Sequiera and Luchen Tan and Nimesh Ghelani and Mustafa Abualsaud and Richard McCreadie and Dmitrijs Milajevs and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2017 Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinMSTGAMMV17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC Real-Time Summarization 2017

_Abdelhamid Chellal, Mohand Boughanem_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/IRIT-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/IRIT-RT.pdf)
- :material-file-search: **Runs:** [IRIT-RunB1](./runs.md#irit-runb1) | [IRIT-RunB2](./runs.md#irit-runb2) | [IRIT-RunB3](./runs.md#irit-runb3) | [IRIT-Run1-A](./runs.md#irit-run1-a) | [IRIT-Run2-A](./runs.md#irit-run2-a) | [IRIT-Run3-A](./runs.md#irit-run3-a)

??? abstract "Abstract"
	
	This paper presents the participation of the IRIT laboratory (University of Toulouse) to the Real-Time Summarization track of TREC RTS 2017. This track aims at exploring prospective information needs over document streams containing novel and evolving information and it consists of two scenarios ( A: push notification and B: Email digest). In this year the live mobile assessment was made available in real-time which provides the opportunity to propose an approach based on adaptive learning that leverages relevance feedback. We submitted two runs for scenarios A and three runs for scenarios B. In both scenarios, the identification of relevant tweets is based on a binary classifier that predicts the relevance of an incoming tweet with respect to an interest profile. We examine the impact of the use of the live relevance feedback to re-train the classier each time new relevance assessments are made available. For scenario B, the summary generation is modeled as an optimization problem using Integer Linear Programming.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChellalB17.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChellalB17,
		author = {Abdelhamid Chellal and Mohand Boughanem},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IRIT} at {TREC} Real-Time Summarization 2017},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/IRIT-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChellalB17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fast NLP-based Pattern Matching in Real Time Tweet Recommendation

_Zheng Gao, John Wolohan_

- :fontawesome-solid-user-group: **Participant:** [SOIC](./participants.md#soic)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/SOIC-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/SOIC-RT.pdf)
- :material-file-search: **Runs:** [IUB](./runs.md#iub) | [SOIC-Run1-A](./runs.md#soic-run1-a)

??? abstract "Abstract"
	
	Social media users are willing to obtain information from online social streaming services. Everyday people receive news notifications from mobile devices and figure out information which are new and interesting to them. Therefore, it is necessary to learn a recommendation mechanism to see how to attract users attention most by providing most useful news or information to them. This year, TREC (Text REtrieval Conference) offers a Real Time Summarization track to explore online user reading preference on Twitter, one of the largest social media platform so far, to figure out recommendation patterns best suitable for users.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GaoW17.bib) "
	```
	@inproceedings{DBLP:conf/trec/GaoW17,
		author = {Zheng Gao and John Wolohan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Fast NLP-based Pattern Matching in Real Time Tweet Recommendation},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/SOIC-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GaoW17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NOVASearch at TREC 2017 Real-Time Summarization Track

_Gustavo Gonçalves, Flávio Martins, João Magalhães_

- :fontawesome-solid-user-group: **Participant:** [NOVASearch](./participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/NOVASearch-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/NOVASearch-RT.pdf)
- :material-file-search: **Runs:** [NOVASearchB1](./runs.md#novasearchb1) | [NOVASearchB2](./runs.md#novasearchb2) | [NOVASearchB3](./runs.md#novasearchb3)

??? abstract "Abstract"
	
	The rise of large data streams introduces new challenges regard- ing the delivery of relevant content towards an information need. This information need can be seen as a broad topic of information. One possible strategy to tackle the delivery of the most relevant documents regarding this broader topic is summarization. TREC 2017 Real-Time Summarization (RTS) provides a testbed for the development of stream based real-time summarization systems. Leveraging on the social media network, Twitter, the participants are challenged to deliver the most relevant and diverse information in two main scenarios. The real-time push notifications scenario, or Scenario A, focuses on the identification and delivery of relevant information in near real-time. Whereas the daily-digest scenario, or scenario B, strives for the daily delivery of the most relevant and diverse documents. This paper presents the participation of the NOVASearch group at TREC 2017 Real-Time Summarization (RTS). Our work was developed for tackling the scenario B, after an analysis of the proposed systems for the TREC RTS 2016. In our approach we explore document filtering methods; vocabulary expansions; and the identification of subtopics through the aggregation of documents based on their textual similarity.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoncalvesMM17.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoncalvesMM17,
		author = {Gustavo Gon{\c{c}}alves and Fl{\'{a}}vio Martins and Jo{\~{a}}o Magalh{\~{a}}es},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {NOVASearch at {TREC} 2017 Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/NOVASearch-RT.pdf},
		timestamp = {Thu, 14 May 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/GoncalvesMM17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HLJIT at TREC 2017 Real-Time Summarization

_Zhongyuan Han, Song Li, Leilei Kong, Liuyang Tian, Haoliang Qi_

- :fontawesome-solid-user-group: **Participant:** [HLJIT](./participants.md#hljit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/HLJIT-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/HLJIT-RT.pdf)
- :material-file-search: **Runs:** [qFB_url](./runs.md#qfb_url) | [HLJIT_l2r](./runs.md#hljit_l2r) | [HLJIT_rank_svm](./runs.md#hljit_rank_svm) | [testRun1-A](./runs.md#testrun1-a) | [testRun2-A](./runs.md#testrun2-a) | [testRun3-A](./runs.md#testrun3-a)

??? abstract "Abstract"
	
	This paper describes the approaches used at the TREC 2017 Real-Time Summarization. This task contains two scenarios: push notifications and email digest. For the scenario of push notifications, three filtering models, which are based on the hyperlink-extended retrieval model, the Learning to Rank and the hybrid filtering model, are proposed to filter the relevant tweets for a given topic. A novelty verification method is given for further filter the tweets for push notification. For the scenario of email digest, three ranking models, the hyperlink-extended retrieval model, the retrieval model based on learning to rank, and the personal retrieval model, are presented to rank the relevant tweets. Similarly, a novelty verification is proposed for filtering the redundant tweets. The evaluation results of TREC 2017 Real-Time Summarization show that the performance of our models is competitive.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HanLKTQ17.bib) "
	```
	@inproceedings{DBLP:conf/trec/HanLKTQ17,
		author = {Zhongyuan Han and Song Li and Leilei Kong and Liuyang Tian and Haoliang Qi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{HLJIT} at {TREC} 2017 Real-Time Summarization},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/HLJIT-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HanLKTQ17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Some thoughts from IRIT about the scenario A of the TREC RTS  2016 and 2017 tracks

_Gilles Hubert, José G. Moreno, Karen Pinel-Sauvagnat, Yoann Pitarch_

- :fontawesome-solid-user-group: **Participant:** [IRIT](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/IRIT2-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/IRIT2-RT.pdf)
- :material-file-search: **Runs:** [IRIT-RunB1](./runs.md#irit-runb1) | [IRIT-RunB2](./runs.md#irit-runb2) | [IRIT-RunB3](./runs.md#irit-runb3) | [IRIT-Run1-A](./runs.md#irit-run1-a) | [IRIT-Run2-A](./runs.md#irit-run2-a) | [IRIT-Run3-A](./runs.md#irit-run3-a)

??? abstract "Abstract"
	
	The TREC Real-Time Summarization (RTS) track provides a framework for evaluating systems monitoring the Twitter stream and pushing tweets to users according to given profiles. It includes metrics, files, settings and hypothesis provided by the organizers. In this work, we perform a thorough analysis of each component of the framework used for batch evaluation of scenario A in 2016 and 2017. We found some weaknesses of the metrics and took advantage of these limitations to submit our official run in the 2017 edition. The good evaluation results validate our findings. This paper also gives clear recommendations to fairly reuse the collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HubertMPP17.bib) "
	```
	@inproceedings{DBLP:conf/trec/HubertMPP17,
		author = {Gilles Hubert and Jos{\'{e}} G. Moreno and Karen Pinel{-}Sauvagnat and Yoann Pitarch},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Some thoughts from {IRIT} about the scenario {A} of the {TREC} {RTS} 2016 and 2017 tracks},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/IRIT2-RT.pdf},
		timestamp = {Tue, 06 Sep 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HubertMPP17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Recognizing Tweet Relevance with Profile-specific and Profile-independent  Supervised Models

_Kathy Lee, Ashequl Qadir, Yuan Ling, Joey Liu, Sadid A. Hasan, Vivek V. Datla, Aaditya Prakash, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna](./participants.md#prna)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/prna-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/prna-RT.pdf)
- :material-file-search: **Runs:** [PRNA-B1](./runs.md#prna-b1) | [PRNA-B2](./runs.md#prna-b2) | [PRNA-B3](./runs.md#prna-b3) | [PRNA-A1-A](./runs.md#prna-a1-a) | [PRNA-A2-A](./runs.md#prna-a2-a) | [PRNA-A3-A](./runs.md#prna-a3-a)

??? abstract "Abstract"
	
	In the 2017 TREC (Text Retrieval Conference) Real-Time Summarization (RTS) track, we explored supervised methods for identifying relevant tweets based on a user's interest profile. We primarily focused on two approaches: profile-specific and profile-independent. For profile-specific, we trained a model for each interest profile with features specific to the target profile. In case of profile-independent, a single model was trained with features that were general across all profiles. For training the supervised models, we used labeled data from the previous year's challenge. We additionally introduced a novel method for automatically labeling tweets with relevance scores. The method treated keywords from titles as an essential information and penalized the relevance score for a tweet when the keywords were absent; while treating keywords from description as supporting information, and rewarding the relevance score when these keywords were present. In scenario A (real-time push notification), our best run yielded 9.95% EG-p and 11.11% nDCG-p improvements over the median in batch evaluation. In scenario B (daily digest), our best run achieved 25.43% nDCGp improvement over the median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeQLLHDPF17.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeQLLHDPF17,
		author = {Kathy Lee and Ashequl Qadir and Yuan Ling and Joey Liu and Sadid A. Hasan and Vivek V. Datla and Aaditya Prakash and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Recognizing Tweet Relevance with Profile-specific and Profile-independent Supervised Models},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/prna-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeQLLHDPF17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Silent Day Detection in Real-Time Summarization Track

_Kuang Lu, Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/udel_fang-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/udel_fang-RT.pdf)
- :material-file-search: **Runs:** [UDInfoJac](./runs.md#udinfojac) | [UDInfoW2VPre](./runs.md#udinfow2vpre) | [UDInfoW2VTWT](./runs.md#udinfow2vtwt) | [UDInfoBL-A](./runs.md#udinfobl-a) | [UDInfoEXP-A](./runs.md#udinfoexp-a) | [UDInfoSDWR-A](./runs.md#udinfosdwr-a)

??? abstract "Abstract"
	
	In microblog retrieval, a system's ability to detect silent days and 'shut up' during these days have an huge impact on its performance [1]. Therefore, in this year's Real-Time Summarization Track, we focus on detecting silent days. More specifically, we propose two silent day detectors phrase-based weighted information gain and local query term coherence, both of which focus on using query terms collectively instead of individually. Track results suggest that our methods can effectively detect silent days, which subsequently results in promising performances for both scenarios.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuY017.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuY017,
		author = {Kuang Lu and Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Silent Day Detection in Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/udel\_fang-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuY017.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2017: Real-Time Summarization Track

_Qingwei Meng, Kai Wang, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/BJUT-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/BJUT-RT.pdf)
- :material-file-search: **Runs:** [bjutg](./runs.md#bjutg) | [bjutgs](./runs.md#bjutgs) | [bjut_tmg](./runs.md#bjut_tmg) | [BL1-A](./runs.md#bl1-a) | [BL2-A](./runs.md#bl2-a) | [BL3-A](./runs.md#bl3-a)

??? abstract "Abstract"
	
	This paper describes our effort for the TREC Real-Time Summarization task in 2017, which is pushing notifications to the users mobile phone (Task A) and submitting periodic email digest according to tweets posted on the previous day (Task B). In essence, both of the tasks are about a process of ex- tracting the relevant data from tweets stream with respect to the users' interest profiles. For each task we submitted three runs, in this paper, we presented the system framework and experimental results briefly.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MengWY17.bib) "
	```
	@inproceedings{DBLP:conf/trec/MengWY17,
		author = {Qingwei Meng and Kai Wang and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2017: Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/BJUT-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MengWY17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Summarizing tweet in real-time by filtering quality, relevant and  non redundant tweets

_Bilel Moulahi, Lamjed Ben Jabeur, Rafik Abbes, Lynda Tamine_

- :fontawesome-solid-user-group: **Participant:** [advanse_lirmm](./participants.md#advanse_lirmm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/advanse_lirmm-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/advanse_lirmm-RT.pdf)
- :material-file-search: **Runs:** [adv_lirmm-Run1](./runs.md#adv_lirmm-run1) | [adv_lirmm-Run2](./runs.md#adv_lirmm-run2) | [adv_lirmm-Run3](./runs.md#adv_lirmm-run3) | [advanse_lirmm-Run1-A](./runs.md#advanse_lirmm-run1-a) | [advanse_lirmm-Run2-A](./runs.md#advanse_lirmm-run2-a) | [advanse_lirmm-Run3-A](./runs.md#advanse_lirmm-run3-a)

??? abstract "Abstract"
	
	This paper presents the participation of LIRMM laboratory (University of Montpellier), P3 Group and IRIT laboratory (University of Toulouse) to the Real Time Summarization track of TREC 2017. We extend our previous approach [1] for real-time filtering of tweet stream that aims to identify quality, relevant and non-redundant tweets to be pushed to the user at real-time. We describe in this paper the proposed approach and we discuss official obtained results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MoulahiJAT17.bib) "
	```
	@inproceedings{DBLP:conf/trec/MoulahiJAT17,
		author = {Bilel Moulahi and Lamjed Ben Jabeur and Rafik Abbes and Lynda Tamine},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Summarizing tweet in real-time by filtering quality, relevant and non redundant tweets},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/advanse\_lirmm-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MoulahiJAT17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting Live Feedback for Tweet Real-time Push Notifications

_Reem Suwaileh, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./participants.md#qu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/QU-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/QU-RT.pdf)
- :material-file-search: **Runs:** [QUBaseline-A](./runs.md#qubaseline-a) | [QUExpDyn-A](./runs.md#quexpdyn-a) | [QUExp-A](./runs.md#quexp-a)

??? abstract "Abstract"
	
	Twitter has been developed as an immense information creation and sharing network through which users post diverse information. Although a user would regularly check her Twitter timeline to stay up-to-date on her topics of interest, it is impossible to survive with manual topic tracking techniques while tackling the challenges that emerge from the Twitter timeline nature. Among these challenges are the big volume of posted tweets, noise (e.g., spam), redundant information (e.g., retweets), and the rapid development of topics over time. This necessitates the development of real-time summarization (RTS) systems that automatically track predefined topics of interest and summarize the stream while considering the relevance, novelty, and freshness of the selected tweets. We tackle this problem as part of Qatar University's participation in TREC-2017 Real-Time Summarization (RTS) track. Our RTS system adopts a light-weight and conservative filtering strategy that monitors the continuous stream of tweets over a pipeline of multiple phases including pre-qualification, preprocessing, indexing, relevance filtering, novelty filtering, and tweets nomination. The system also exploits life (explicit) feedback to update profiles and pushing criteria (e.g., relevance threshold). The experimental results show that the runs that exploit the live explicit feedback exhibited a better performance in comparison to the baseline run that has been the best (among our runs) for the last two years. Additionally, all submitted runs have scored above the median provided by the track organizers in the batch evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SuwailehE17.bib) "
	```
	@inproceedings{DBLP:conf/trec/SuwailehE17,
		author = {Reem Suwaileh and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Exploiting Live Feedback for Tweet Real-time Push Notifications},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/QU-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SuwailehE17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKUICST at TREC 2017 Real-Time Summarization Track: Push Notifications  and Email Digest

_Jizhi Tang, Chao Lv, Lili Yao, Dongyan Zhao_

- :fontawesome-solid-user-group: **Participant:** [PKUICST](./participants.md#pkuicst)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/PKUICST-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/PKUICST-RT.pdf)
- :material-file-search: **Runs:** [PKUICSTRunB1](./runs.md#pkuicstrunb1) | [PKUICSTRunB2](./runs.md#pkuicstrunb2) | [PKUICSTRunB3](./runs.md#pkuicstrunb3) | [PKUICSTRunA1-A](./runs.md#pkuicstruna1-a) | [PKUICSTRunA2-A](./runs.md#pkuicstruna2-a) | [PKUICSTRunA3-A](./runs.md#pkuicstruna3-a)

??? abstract "Abstract"
	
	In this paper, we describe our approaches and corresponding results in the Real-Time Summarization(RTS) track at the 2017 Text Retrieval Conference(TREC). The main idea is to build a two-stage filter system for both scenario A and B. In the first stage, tweets are filtered according to its relevance score to a particular topic, while in the second stage, they are filtered according to its novelty score to previous submitted tweets. We tried several approaches to model the text similarity, such as negative KL-divergence and cosine distance, as well as blending models. Especially, in scenario A, the push notification scenario, we designed a decoupled system that can maintain high availability in order to meet the real-time requirements. The experiment results show that our methods reach good performance with respect to several metrics such as EG-p and nDCG-p.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TangLYZ17.bib) "
	```
	@inproceedings{DBLP:conf/trec/TangLYZ17,
		author = {Jizhi Tang and Chao Lv and Lili Yao and Dongyan Zhao},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{PKUICST} at {TREC} 2017 Real-Time Summarization Track: Push Notifications and Email Digest},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/PKUICST-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TangLYZ17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at TREC 2017 Real-Time Summarization Track

_Xiao Wang, Pengcheng Fan, Liang Cheng, Guoliang Xing, Zhihua Yu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ICTNET-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/ICTNET-RT.pdf)
- :material-file-search: **Runs:** [ICTNET-Run1](./runs.md#ictnet-run1) | [ICTNET-Run2](./runs.md#ictnet-run2) | [ICTNET-Run3](./runs.md#ictnet-run3) | [ICTNET-run1-A](./runs.md#ictnet-run1-a) | [ICTNET-run2-A](./runs.md#ictnet-run2-a) | [ICTNET-run3-A](./runs.md#ictnet-run3-a)

??? abstract "Abstract"
	
	Nowadays Twitter represents a successful social application and own billions of users, and there is a growing trend for recommending high quality message to users due to the business need. The Real-Time Summarization (RTS) track explores techniques for constructing real-time update summaries from social media streams in response to users' information needs. Our task then can be reduced to a recommendation system, actually it is a recommendation system based on data stream which has continuous and enormous message data of various types. As indicated by the name of the track, the main goal of this track is to solve the problem of making the recommendation real-time, relative and novel, which is exactly the demands of scenario A. For scenario B, posting the mail digest is like a compromise to scenario A, in this scenario, we only need to post a batch of tweets to users through email at the end of the day, which means there is no real-time limitation of scenario A, and this problem then can be reduced to traditional ad-hoc search problem. In this paper we mainly focus on scenario A and then conduct the solution of scenario B based on scenario A. Substantially, Scenario A can be interpreted as following problem: given user profiles (also known as topics) which is the abstraction of a certain crowd of people's interests, by monitoring the twitter steam data, we need to make real-time (as soon as the tweet is posted), relative and novel tweet recommendation to the corresponding profile once detected. The problem mainly contains the following aspects: text processing (i.e. natural language processing), vectorization (feature selecting and extraction, vector similarity) and data storage (database management), the key part is the vectorization and similarity calculation. We need to combine these parts together to build an effective system. Our approach mainly includes two different models, the word2vec model and TF-IDF model. In word2vec model, we simply train a word2vec language model based on wiki corpus, and then appliy the model to tweet and profile to gain vector, based on the similarity between tweet vector and profile vector we adopt corresponding pushing strategy. The TF-IDF is different in vectorization, it cached tweets a few days ahead, and apply TF-IDF model on the cached tweet corpus as well as profiles to gain the tweet vector and profile vector, details will be explored in the rest of the paper. According to the results of evaluation, our TF-IDF model achieved better performance than the naïve word2vec model, the best run was around 15% above the medium score of all automatic runs this year in Scenario A.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangFCXYC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangFCXYC17,
		author = {Xiao Wang and Pengcheng Fan and Liang Cheng and Guoliang Xing and Zhihua Yu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at {TREC} 2017 Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/ICTNET-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangFCXYC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### at TREC 2017: Real-Time Summarization Track

_Junjie Xiong, Dongdong Xiang, Qian Guo, Haiguang Chen_

- :fontawesome-solid-user-group: **Participant:** [S.T](./participants.md#s.t)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/S.T-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/S.T-RT.pdf)
- :material-file-search: **Runs:** [SHNU_run1](./runs.md#shnu_run1) | [SHNU_run2](./runs.md#shnu_run2) | [SHNU_run3](./runs.md#shnu_run3) | [SHNU_run1-A](./runs.md#shnu_run1-a) | [SHNU_run2-A](./runs.md#shnu_run2-a) | [SHNU_run3-A](./runs.md#shnu_run3-a)

??? abstract "Abstract"
	
	This paper presents the participation of Shanghai Normal University to the TREC 2017 Real-Time Summarization (RTS) Track. We adopted three different composed methods by applying various factors, i.e., count, cosine and distance to measure relevance between a tweet and a given topic. By setting static relevance threshold for each run, we selected the most relevant but non-redundant tweets and then pushed them to user's phone in Scenario A. For Scenario B, we used a similar but much simpler approach. The evaluation results showed that there was still a long way to go in practice. Nonetheless, some progress has been made. We submitted three runs for both scenarios. This paper demonstrates the implementation details and official evaluation results of our system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XiongXGC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/XiongXGC17,
		author = {Junjie Xiong and Dongdong Xiang and Qian Guo and Haiguang Chen},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {at {TREC} 2017: Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/S.T-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XiongXGC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

