# Proceedings - Incident Streams 2020 

#### Incident Streams 2020: TRECIS in the Time of COVID-19

_Cody Buntain, Richard McCreadie, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.IS.pdf](https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.IS.pdf)
??? abstract "Abstract"
	
	Between 2018 and 2019, the Incident Streams track (TREC-IS) has developed standard approaches for classifying the types and criticality of information shared in online social spaces during crises, but the introduction of SARS-CoV-2 has shifted the landscape of online crises substantially. While prior editions of TREC-IS have lacked data on large-scale public-health emergencies as these events are exceedingly rare, COVID-19 has introduced an over-abundance of potential data, and significant open questions remain about how existing approaches to crisis informatics and datasets built on other emergencies adapt to this new context. This paper describes how the 2020 edition of TREC-IS has addressed these dual issues by introducing a new COVID-19-specific task for evaluating generalization of existing COVID-19 annotation and system performance to this new context, applied to 11 regions across the globe. TREC-IS has also continued expanding its set of target crises, adding 29 new events and expanding the collection of event types to include explosions, fires, and general storms, making for a total of 9 event types in addition to the new COVID-19 events. Across these events, TREC-IS has made available 478,110 COVID-related messages and 282,444 crisis-related messages for participant systems to analyze, of which 14,835 COVID-related and 19,784 crisis-related messages have been manually annotated. Analyses of these new datasets and participant systems demonstrate first that both the distributions of information type and priority of information vary between general crises and COVID-19-related discussion. Secondly, despite these differences, results suggest leveraging general crisis data in the COVID-19 context improves performance over baselines. Using these results, we provide guidance on which information types appear most consistent between general crises and COVID-19.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuntainMS20.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuntainMS20,
		author = {Cody Buntain and Richard McCreadie and Ian Soboroff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Incident Streams 2020: {TRECIS} in the Time of {COVID-19}},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.IS.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BuntainMS20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Improving Classification of Crisis-Related Social Media Content via  Text Augmentation and Image Analysis

_Shivam Sharma, Cody Buntain_

- :fontawesome-solid-user-group: **Participant:** [njit](./participants.md#njit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/NJIT.IS.pdf](https://trec.nist.gov/pubs/trec29/papers/NJIT.IS.pdf)
- :material-file-search: **Runs:** [njit-sub01.text.2020A.task1](./runs.md#njit-sub01.text.2020a.task1) | [njit-sub01.text.2020A.task2](./runs.md#njit-sub01.text.2020a.task2) | [njit-sub02.text+aug.2020A.task1](./runs.md#njit-sub02.text+aug.2020a.task1) | [njit-sub02.text+aug.2020A.task2](./runs.md#njit-sub02.text+aug.2020a.task2) | [njit-sub01.text.2020A.task3](./runs.md#njit-sub01.text.2020a.task3) | [njit-sub02.text+aug.2020A.task3](./runs.md#njit-sub02.text+aug.2020a.task3) | [njit.s1.aug](./runs.md#njit.s1.aug) | [njit.s1.aug.t2](./runs.md#njit.s1.aug.t2) | [njit.s1.aug.t3](./runs.md#njit.s1.aug.t3) | [njit.s2.cmmd.t1](./runs.md#njit.s2.cmmd.t1) | [njit.s2.cmmd.t2](./runs.md#njit.s2.cmmd.t2) | [njit.s2.cmmd.t3](./runs.md#njit.s2.cmmd.t3) | [njit.s3.img.t1](./runs.md#njit.s3.img.t1) | [njit.s3.img.t2](./runs.md#njit.s3.img.t2) | [njit.s3.img.t3](./runs.md#njit.s3.img.t3) | [njit.s4.cml.t1](./runs.md#njit.s4.cml.t1) | [njit.s4.cml.t2](./runs.md#njit.s4.cml.t2) | [njit.s4.cml.t3](./runs.md#njit.s4.cml.t3)

??? abstract "Abstract"
	
	Identifying, classifying, and prioritizing crisis-related content in social media is an increasingly important task, as users of online platforms continue to expect emergency-response officials to monitor these channels. Much of the current work in this area, however, focuses on applications of neural language models (NLMs) to the text of these social media messages, leaving many meta-content and multi-modal signals unaddressed. This work challenges this text- and NLM-centric view as it applies to crisis informatics and the Incident Streams track at the annual Text Retrieval Conference (TREC-IS) by first measuring the performance enhancements NLMs provide over classical text-classification pipelines and then by integrating external data sources and non-textual image analysis. Results suggest classical machine learning (ML) models are still competitive to NLMs, especially in identifying high-priority content, but adding a simple text augmentation strategy results in significant gains in NLM performance. Preliminary results are consistent with the community's focus on NLMs as our work suggests augmented NLMs perform best in classification, while integrating image analysis has marginal effects on performance. Augmenting samples with inferences from CrisisMMD, however, also significantly increases prioritization performance, suggesting strategies for integrating other data and signals remain valuable. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SharmaB20.bib) "
	```
	@inproceedings{DBLP:conf/trec/SharmaB20,
		author = {Shivam Sharma and Cody Buntain},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Improving Classification of Crisis-Related Social Media Content via Text Augmentation and Image Analysis},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/NJIT.IS.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SharmaB20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2020 Incident Streams Track

_Hesong Wang, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT2020](./participants.md#bjut2020)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/BJUT.IS.pdf](https://trec.nist.gov/pubs/trec29/papers/BJUT.IS.pdf)
- :material-file-search: **Runs:** [BJUT-run](./runs.md#bjut-run)

??? abstract "Abstract"
	
	In this paper, we will continue to use the new method in the 2019 version to continue the work of the 2020 TREC Incident Streams System task[1]. Social media has become an indispensable part of human life, such as Twitter, Weibo and so on. When natural disasters occur, such as fires, earthquakes, flash floods, tsunamis, mudslides and other natural disasters or shootings, robberies and other emergencies, if only through media reports, the time of the event will be very slow, leading to some preventable loss. People like to post disaster situations or events on social media. The purpose of the task is to filter such natural disasters or emergencies by classifying the text on twitter. Similarly, each tweet is prioritized and the tagged information is reported to the relevant personnel according to different priorities. Let the staff know about the progress of the incident to help. This article will introduce the framework and methods of the classification system, as well as the experimental results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Wang020.bib) "
	```
	@inproceedings{DBLP:conf/trec/Wang020,
		author = {Hesong Wang and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2020 Incident Streams Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/BJUT.IS.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Wang020.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multi-task Transfer Learning for Finding Actionable Information from  Crisis-related Messages on Social Media

_Congcong Wang, David Lillis_

- :fontawesome-solid-user-group: **Participant:** [UCD-CS](./participants.md#ucd-cs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/UCD-CS.IS.pdf](https://trec.nist.gov/pubs/trec29/papers/UCD-CS.IS.pdf)
- :material-file-search: **Runs:** [CD_CS_R1.2020A.task1](./runs.md#cd_cs_r1.2020a.task1) | [CD_CS_R2.2020A.task1](./runs.md#cd_cs_r2.2020a.task1) | [CD_CS_R3.2020A.task1](./runs.md#cd_cs_r3.2020a.task1) | [CD_CS_R4.2020A.task1](./runs.md#cd_cs_r4.2020a.task1) | [CD_CS_T2_R1.2020A.task2](./runs.md#cd_cs_t2_r1.2020a.task2) | [UCD_CS_T3_R1](./runs.md#ucd_cs_t3_r1) | [UCD_CS_T3_R2](./runs.md#ucd_cs_t3_r2) | [UCD_CS_T3_R3](./runs.md#ucd_cs_t3_r3) | [ucd-run1](./runs.md#ucd-run1) | [ucd-run2](./runs.md#ucd-run2) | [ucd-run3](./runs.md#ucd-run3) | [ucd-run4](./runs.md#ucd-run4) | [ucd-run5](./runs.md#ucd-run5)

??? abstract "Abstract"
	
	The Incident streams (IS) track is a research challenge aimed at finding important information from social media during crises for emergency response purposes. More specifically, given a stream of crisis-related tweets, the IS challenge asks a participating system to 1) classify what the types of users' concerns or needs are expressed in each tweet, known as the information type (IT) classification task and 2) estimate how critical each tweet is with regard to emergency response, known as the priority level prediction task. In this paper, we describe our multi-task transfer learning approach for this challenge. Our approach leverages state-of-the-art transformer models including both encoder-based models such as BERT and a sequence-to-sequence based T5 for joint transfer learning on the two tasks. Based on this approach, we submitted several runs to the track. The returned evaluation results show that our runs substantially outperform other participating runs in both IT classification and priority level prediction.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangL20.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangL20,
		author = {Congcong Wang and David Lillis},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Multi-task Transfer Learning for Finding Actionable Information from Crisis-related Messages on Social Media},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/UCD-CS.IS.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WangL20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team (uogTr) at the TREC 2020 Incident  Streams Track

_Alexander J. Hepburn, Richard McCreadie_

- :fontawesome-solid-user-group: **Participant:** [UoGTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec29/papers/uogTr.IS.pdf](https://trec.nist.gov/pubs/trec29/papers/uogTr.IS.pdf)
- :material-file-search: **Runs:** [elmo_all_brf](./runs.md#elmo_all_brf) | [elmo_all_eec](./runs.md#elmo_all_eec) | [elmo_all_tfidf_brf](./runs.md#elmo_all_tfidf_brf) | [elmo_all_tfidf_eec](./runs.md#elmo_all_tfidf_eec) | [elmo_textonly_eec_covid](./runs.md#elmo_textonly_eec_covid)

??? abstract "Abstract"
	
	In this paper, we describe runs submitted on behalf of the University of Glasgow Terrier Team (uogTr) for the TREC 2020 Incident Streams track. We detail our approach to addressing the challenges present in the classification of crisis and disaster management data in unstructured text. In particular, we explore the usage of pre-trained ELMo embeddings alongside descriptive metadata-level and event-level features for classification. We also utilise algorithms incorporating undersampling techniques in order to mitigate the significant class imbalance in the dataset. We submitted a total of three official runs to the 2020A track: ELMO_ALL_BRF, ELMO_ALL_EEC, and ELMO_ALL_TFIDF_BRF with varying features and classifiers used. Our results show that our run, ELMO_ALL_BRF shows competitive performance, performing above the median across a number of track-specific metrics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HepburnM20.bib) "
	```
	@inproceedings{DBLP:conf/trec/HepburnM20,
		author = {Alexander J. Hepburn and Richard McCreadie},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow Terrier Team (uogTr) at the {TREC} 2020 Incident Streams Track},
		booktitle = {Proceedings of the Twenty-Ninth Text REtrieval Conference, {TREC} 2020, Virtual Event [Gaithersburg, Maryland, USA], November 16-20, 2020},
		series = {{NIST} Special Publication},
		volume = {1266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2020},
		url = {https://trec.nist.gov/pubs/trec29/papers/uogTr.IS.pdf},
		timestamp = {Wed, 07 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HepburnM20.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

