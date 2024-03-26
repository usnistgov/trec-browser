# Proceedings - Real-time Summarization 2016 

#### Overview of the TREC 2016 Real-Time Summarization Track

_Jimmy Lin, Adam Roegiest, Luchen Tan, Richard McCreadie, Ellen M. Voorhees, Fernando Diaz_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec25/papers/Overview-RT.pdf](https://trec.nist.gov/pubs/trec25/papers/Overview-RT.pdf)
??? abstract "Abstract"
	
	The TREC 2016 Real-Time Summarization (RTS) Track aims to explore techniques and systems that automatically monitor streams of social media posts such as Twitter to keep users up to date on topics of interest. We might think of these topics as “interest profiles”, specifying the user's prospective information needs. In real-time summarization, the goal is for a system to “push” (i.e., recommend or suggest) interesting and novel content to users in a timely fashion. For example, the user might be interested in poll results for the 2016 U.S. presidential elections and wishes to be notified whenever new results are published. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinRTMV016.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinRTMV016,
		author = {Jimmy Lin and Adam Roegiest and Luchen Tan and Richard McCreadie and Ellen M. Voorhees and Fernando Diaz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2016 Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {https://trec.nist.gov/pubs/trec25/papers/Overview-RT.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinRTMV016.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CCNU at TREC 2016 Real-Time Summarization Track

_Chao Bei, Po Hu_

- :fontawesome-solid-user-group: **Participant:** [CCNU2016NLP](./participants.md#ccnu2016nlp)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/CCNU2016NLP-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/CCNU2016NLP-RT.pdf)
- :material-file-search: **Runs:** [CCNUNLPrun1](./runs.md#ccnunlprun1) | [CCNUNLPrun2](./runs.md#ccnunlprun2) | [CCNUNLPrun1-06](./runs.md#ccnunlprun1-06) | [CCNUNLPrun2-07](./runs.md#ccnunlprun2-07)

??? abstract "Abstract"
	
	This paper describes our approach to real-time summarization track for push notification scenario and email digest scenario in TREC 2016. This track aims at monitoring a stream of twitter posts and pushing the most relevant tweets to the users according to their interest profiles. In the push notification scenario, we adopt a combined method by take into account several critical factors i.e., relevance, salience and redundancy to select some relevant but non-redundant tweets. In the email digest scenario, in addition to considering these factors, we additionally adopted a novel TF-IDF strategy to automatically rank tweets at the end of a day. The experimental results on both scenarios show the effectiveness of our approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BeiH16.bib) "
	```
	@inproceedings{DBLP:conf/trec/BeiH16,
		author = {Chao Bei and Po Hu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CCNU} at {TREC} 2016 Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/CCNU2016NLP-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BeiH16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Assorted Textual Features and Dynamic Push Strategies for Real-time  Tweet Notification

_Kathy Lee, Ashequl Qadir, Vivek V. Datla, Sadid A. Hasan, Joey Liu, Aaditya Prakash, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna](./participants.md#prna)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/prna-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/prna-RT.pdf)
- :material-file-search: **Runs:** [PRNABaseline-34](./runs.md#prnabaseline-34) | [PRNATaskA2-35](./runs.md#prnataska2-35) | [PRNATaskA3-36](./runs.md#prnataska3-36) | [PRNATaskB1](./runs.md#prnataskb1) | [PRNATaskB2](./runs.md#prnataskb2) | [PRNATaskB3](./runs.md#prnataskb3)

??? abstract "Abstract"
	
	In this paper, we describe our systems and corresponding results submitted to the Real-Time Summarization (RTS) track at the 2016 Text Retrieval Conference (TREC). The task involved identifying relevant tweets based on a user's interest profile. In Scenario A of the task, tweets relevant to an interest profile were pushed to a live user in real-time. In Scenario B, a daily digest of relevant tweets was sent to a user. We submitted three automatic runs for each scenario. Our overall method for identifying relevant tweets was based on 1) automatically identifying key textual features from a set of interest profiles provided by the Track organizers, 2) expanding the textual phrases with their paraphrases, and 3) exploiting the features for message filtering and relevance measurement after novelty recognition. We experimented with different push strategies to decide when to deliver a message to a user. The evaluation results (by mobile and NIST assessors) show that our system ranked 3rd for Scenario A and 6th for Scenario B.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeQDHLPF16.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeQDHLPF16,
		author = {Kathy Lee and Ashequl Qadir and Vivek V. Datla and Sadid A. Hasan and Joey Liu and Aaditya Prakash and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Assorted Textual Features and Dynamic Push Strategies for Real-time Tweet Notification},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/prna-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeQDHLPF16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HLJIT at TREC 2016: The Approaches Based on Document Language  Model for Real-Time Summarization Track

_Song Li, Zhenyuan Hao, Zhongyuan Han, Leilei Kong, Haoliang Qi_

- :fontawesome-solid-user-group: **Participant:** [HLJIT](./participants.md#hljit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/HLJIT-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/HLJIT-RT.pdf)
- :material-file-search: **Runs:** [HLJIT_LM-19](./runs.md#hljit_lm-19) | [MyBaseline-17](./runs.md#mybaseline-17) | [MyBaseline-18](./runs.md#mybaseline-18) | [HLJIT_LM_URL](./runs.md#hljit_lm_url) | [HLJIT_LM_TIME](./runs.md#hljit_lm_time) | [HLJIT_LM](./runs.md#hljit_lm)

??? abstract "Abstract"
	
	The paper describes the technology of HLJIT for TREC 2016 Real-Time Summarization Track for microblog. Three summarization approaches under the language model framework, the traditional language model, the temporal document language model and the hyperlink-extended language model, are proposed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiHHKQLK16.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiHHKQLK16,
		author = {Song Li and Zhenyuan Hao and Zhongyuan Han and Leilei Kong and Haoliang Qi},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{HLJIT} at {TREC} 2016: The Approaches Based on Document Language Model for Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/HLJIT-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiHHKQLK16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Performance Prediction and Topic Shift in Microblog Retrieval

_Kuang Lu, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/udel_fang-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/udel_fang-RT.pdf)
- :material-file-search: **Runs:** [UDInfoDFP-47](./runs.md#udinfodfp-47) | [UDInfoSFP-46](./runs.md#udinfosfp-46) | [UDInfoSPP-48](./runs.md#udinfospp-48) | [UDInfo_TN](./runs.md#udinfo_tn) | [UDInfo_TlmN](./runs.md#udinfo_tlmn) | [UDInfo_TlmNlm](./runs.md#udinfo_tlmnlm)

??? abstract "Abstract"
	
	In Microblog retrieval, a system's ability to know when to ”shut up” and how many results to return for a given query can have huge impact on its performance [1]. In addition, since relevant but redundant tweets will be deemed as irrelevant, it is also important to detect whether a tweet contain novel information or not. Therefore, in this year's Real-Time Summarization Track, we focus on estimating result cut-off thresholds and redundancy thresholds. Query performance prediction techniques [2, 3] can be used to predict the performance of a query and therefore would be helpful in deciding both thresholds. Moreover, we define topic shift of a query as the change of subtopics or aspects discussed or mentioned on Twitter over time. We suggests that using it could help us further refine the thresholds since it reflects how much new information emerges on Twitter.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuF16.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuF16,
		author = {Kuang Lu and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Query Performance Prediction and Topic Shift in Microblog Retrieval},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/udel\_fang-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuF16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DAIICT at TREC RTS 2016: Live Push Notification and Email Digest

_Sandip Modha, Krati Agrawal, Deepali Verma, Prasenjit Majumder, Chintak Mandalia_

- :fontawesome-solid-user-group: **Participant:** [IRLAB_DA-IICT](./participants.md#irlab_da-iict)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/IRLAB_DA-IICT-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/IRLAB_DA-IICT-RT.pdf)
- :material-file-search: **Runs:** [runA_daiict_irlab-23](./runs.md#runa_daiict_irlab-23) | [IRLAB2](./runs.md#irlab2) | [IRLAB](./runs.md#irlab)

??? abstract "Abstract"
	
	This paper describes the participation of Information Retrieval Lab(IRLAB) at DA-IICT Gandhinagar,India in Real-Time Summarization track TREC 2016. This year TREC RTS offered two tasks. In the first task, that is scenario A, our system will be monitoring continuous posts from Twitter public stream and push the relevant tweet for each interest profile to RTS evaluation broker. For the same, we have expanded interest profile using Word2vec training model with past 30 days tweets. We have calculated relevance score between tweets and expanded interest profile using Okapi BM25 model. For Scenario B, Email digest, we anticipated summarization problem as a clustering problem. In scenario A, we reported result in terms of Expected Gain EG-1(primary metric)=0.1708 and in scenario B we have achieved primary metric nDCG-1 = 0.1972.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ModhaAVMM16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ModhaAVMM16,
		author = {Sandip Modha and Krati Agrawal and Deepali Verma and Prasenjit Majumder and Chintak Mandalia},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{DAIICT} at {TREC} {RTS} 2016: Live Push Notification and Email Digest},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/IRLAB\_DA-IICT-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ModhaAVMM16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Light-weight, Conservative, yet Effective: Scalable Real-time Tweet  Summarization

_Reem Suwaileh, Maram Hasanain, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./participants.md#qu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/QU-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/QU-RT.pdf)
- :material-file-search: **Runs:** [QUDR8](./runs.md#qudr8) | [QUJM16](./runs.md#qujm16) | [QUJMDR24](./runs.md#qujmdr24) | [QUBaseline-37](./runs.md#qubaseline-37) | [QUExpP-38](./runs.md#quexpp-38) | [QUExpT-39](./runs.md#quexpt-39)

??? abstract "Abstract"
	
	Microblogging platforms and Twitter specifically have become a major resource for exploring diverse topics of interest that vary from the world's breaking news to other topics such as sports, science, religion and even personal daily updates. Nevertheless, one by herself cannot easily follow her topics of interest while tackling the challenges that stem from the Twitter timeline nature. Among those challenges is the huge amount of posted tweets that are either not interesting, noisy, or redundant. Additionally, one cannot survive with manual techniques to summarize tweets related to topics that are discussed on the stream and are developed rapidly. In this paper, we tackle the problem of summarizing a stream of tweets given a pre-defined set of topics in the context of Qatar University's participation in TREC-2016 Real-Time Summarization (RTS) track. We participated in both push notification and e-mail digest scenarios. Given a set of users' interest profiles, our RTS system for push notifications scenario adopts a light-weight and conservative filtering strategy that monitors the continuous stream of tweets over a pipeline of multiple stages, while maintaining a scalable processing of a large number of interest profiles. For the e-mail digest scenario, we adopted a similar but even simpler approach. At the end of each day, a list of potentially relevant tweets is retrieved using a query of topic title terms that is issued against an index of all streamed tweets of that day. Our push-notification runs exhibited the best performance among all submitted automatic runs in the push notification task this year. Moreover, our best-performing email-digest run was the second-best among all submitted automatic runs in the email-digest task this year. However, the evaluation results show that the performance is still away from being adopted in practice.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SuwailehHE16.bib) "
	```
	@inproceedings{DBLP:conf/trec/SuwailehHE16,
		author = {Reem Suwaileh and Maram Hasanain and Tamer Elsayed},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Light-weight, Conservative, yet Effective: Scalable Real-time Tweet Summarization},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/QU-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SuwailehHE16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PolyU at TREC 2016 Real-Time Summarization

_Haihui Tan, Dajun Luo, Wenjie Li_

- :fontawesome-solid-user-group: **Participant:** [COMP2016](./participants.md#comp2016)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/COMP2016-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/COMP2016-RT.pdf)
- :material-file-search: **Runs:** [PolyURunB1](./runs.md#polyurunb1) | [PolyURunB2](./runs.md#polyurunb2) | [PolyURunB3](./runs.md#polyurunb3) | [run1-11](./runs.md#run1-11) | [run2-12](./runs.md#run2-12) | [run3-13](./runs.md#run3-13)

??? abstract "Abstract"
	
	This paper presents the participation of The Hong Kong Polytechnic University (PolyU) to the TREC 2016 Real-Time Summarization track. The two tasks related to Scenario A and Scenario B both focuses on information real-time processing. During the evaluation period, the system monitors the Twitter sample stream with respect to a number of “interest profiles”. We submitted three runs for both scenarios. We describe the system overview and the implementation details in this paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TanLL16.bib) "
	```
	@inproceedings{DBLP:conf/trec/TanLL16,
		author = {Haihui Tan and Dajun Luo and Wenjie Li},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {PolyU at {TREC} 2016 Real-Time Summarization},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/COMP2016-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TanLL16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2016: Real-Time Summarization Track

_Kai Wang, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./participants.md#bjut)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/BJUT-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/BJUT-RT.pdf)
- :material-file-search: **Runs:** [BJUTmydt-04](./runs.md#bjutmydt-04) | [BJUTmydt-05](./runs.md#bjutmydt-05) | [BJUTmyrf-03](./runs.md#bjutmyrf-03) | [bjutrf](./runs.md#bjutrf) | [bjutdt](./runs.md#bjutdt) | [bjutgbdt](./runs.md#bjutgbdt)

??? abstract "Abstract"
	
	This paper describes our approaches to Real-Time Summarization Track in the TREC 2016, including pushing notifications on a mobile phone task (Task A) and periodic email digesting task (Task B). In Task A, we applied the classifiers to categorize all of the input tweets. External information extracted from Google search engine was well incorporated to enhance the understanding of a users interest. In Task B, all the tweets were classified into a specific topic which was ranked by a scoring system. Finally, we used the non-negative matrix factorization clusering to remove redundancy of the classification results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangY16.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangY16,
		author = {Kai Wang and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2016: Real-Time Summarization Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/BJUT-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangY16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PKUICST at TREC 2016 Real-Time Summarization Track: Push Notifications  and Email Digest

_Lili Yao, Chao Lv, Feifan Fan, Jianwu Yang, Dongyan Zhao_

- :fontawesome-solid-user-group: **Participant:** [PKUICST](./participants.md#pkuicst)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/PKUICST-RT.pdf](http://trec.nist.gov/pubs/trec25/papers/PKUICST-RT.pdf)
- :material-file-search: **Runs:** [PKUICSTRunB1](./runs.md#pkuicstrunb1) | [PKUICSTRunB2](./runs.md#pkuicstrunb2) | [PKUICSTRunB3](./runs.md#pkuicstrunb3) | [ru32-33](./runs.md#ru32-33) | [run1-31](./runs.md#run1-31) | [run2-32](./runs.md#run2-32)

??? abstract "Abstract"
	
	This paper describes our approaches for the TREC 2016 Real-Time Summarization track, including push notifications scenario and email digest scenario. In the push notifications scenario, we mainly focus on designing a real-time system, which listens to the Twitter sample stream and makes the push actions for the given topics. Low coupling modules are utilized to obtain the timely, relevant and novel features. In the email digest scenario, we apply the language model combined with the external knowledge base, i.e. Google, for query expansion. Besides, different text similarity algorithms are tried, such as negative KL-divergence and Simhash. Experimental results show that our two-stage filtering methods achieve good performance with respect to EG1 and nCG1 metrics for push notifications scenario. In addition, our systems for email digest scenario also obtain convincing nDCG1 scores.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YaoLFYZ16.bib) "
	```
	@inproceedings{DBLP:conf/trec/YaoLFYZ16,
		author = {Lili Yao and Chao Lv and Feifan Fan and Jianwu Yang and Dongyan Zhao},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{PKUICST} at {TREC} 2016 Real-Time Summarization Track: Push Notifications and Email Digest},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/PKUICST-RT.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YaoLFYZ16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

