# Proceedings - Incident Streams 2021 

#### Siena's Incident Stream System SISS

_Ting Liu, Sharon Gower Small, Patrick Baumgardner, Lydia Cartwright, Michael Coppola, Samuil Orlioglu_

- :fontawesome-solid-user-group: **Participant:** [SienaCLTeam](./participants.md#sienaclteam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/SienaCLTeam-IS.pdf](https://trec.nist.gov/pubs/trec30/papers/SienaCLTeam-IS.pdf)
- :material-file-search: **Runs:** [Siena2021A](./runs.md#siena2021a)

??? abstract "Abstract"
	
	This paper discusses our work and participation in the Text Retrieval Conference (TREC) Incident Streams track (IS) of 2021. The mass adoption of mobile internet-enabled devices paired with wide-spread use of social media platforms for communication and coordination has created new ways for the public on-the-ground to contact response services. With the rise of social media, emergency service operators are now expected to monitor those channels and answer questions from the public. However, they do not have adequate tools or manpower to effectively monitor social media, due to the large volume of information posted on these platforms and the need to categorize, cross-reference and verify that information. The TREC Incident Streams (TREC-IS) track aims to provide a base for research to tackle this technology gap. TREC-IS was designed to bring together academia and industry to research technologies to automatically process social media streams during emergency situations with the aim of categorizing information and aid requests made on social media for emergency service operators. Given a corpus of tweets for a set of emergency events, participants are required to categorize each tweet into its information type, i.e. Request-Search & Rescue, Report-Weather, CallToAction-Volunteer, etc. and its level of criticality. This paper discusses our work and submission to TREC-IS 2021.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0003SBCCO21.bib) "
	```
	@inproceedings{DBLP:conf/trec/0003SBCCO21,
		author = {Ting Liu and Sharon Gower Small and Patrick Baumgardner and Lydia Cartwright and Michael Coppola and Samuil Orlioglu},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Siena's Incident Stream System {SISS}},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/SienaCLTeam-IS.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0003SBCCO21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Transformer-based Methods with #Entities for Detecting Emergency  Events on Social Media

_Emanuela Boros, Nhu Khoa Nguyen, Mickaël Coustaty, Antoine Doucet, Gaël Lejeune_

- :fontawesome-solid-user-group: **Participant:** [L3i_Rochelle](./participants.md#l3i_rochelle)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/L3i_Rochelle-IS.pdf](https://trec.nist.gov/pubs/trec30/papers/L3i_Rochelle-IS.pdf)
- :material-file-search: **Runs:** [RB_2Tx2_TTH_280](./runs.md#rb_2tx2_tth_280) | [RB_2T_TTH_256_LR5](./runs.md#rb_2t_tth_256_lr5) | [RB_2T_TT_280_SVM](./runs.md#rb_2t_tt_280_svm) | [RB_2T_MT_H_280](./runs.md#rb_2t_mt_h_280) | [l3i-ttxth](./runs.md#l3i-ttxth) | [l3i-ttxth.combined](./runs.md#l3i-ttxth.combined)

??? abstract "Abstract"
	
	This paper summarizes the participation of the L3i laboratory of the University of La Rochelle in the TREC Incident Streams 2021. This track aimed at identifying critical information present in social media by categorizing and prioritizing tweets in a disaster situation to assist emergency service operators. For both classifying tweets by information type and ranking tweets by criticality, we proposed a multitask and multilabel learning approach based on representing the tweet text and the event types with pre-trained language models, and by highlighting entities and hashtags. We also experimented with a bag of words representation and classical machine learning methods for the prioritization task. We conclude that, because our multitask approach can take advantage of both tasks, it achieved the best performance in comparison with different proposed ensembles. Our submissions obtained top performance for the prioritization task and surpassed the median performance for the information type classification task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BorosNCDL21.bib) "
	```
	@inproceedings{DBLP:conf/trec/BorosNCDL21,
		author = {Emanuela Boros and Nhu Khoa Nguyen and Micka{\"{e}}l Coustaty and Antoine Doucet and Ga{\"{e}}l Lejeune},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Transformer-based Methods with {\#}Entities for Detecting Emergency Events on Social Media},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/L3i\_Rochelle-IS.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BorosNCDL21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Method Comparison for Crisis Pipelines

_Shivam Sharma, Cody Buntain_

- :fontawesome-solid-user-group: **Participant:** [njit](./participants.md#njit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/njit-IS.pdf](https://trec.nist.gov/pubs/trec30/papers/njit-IS.pdf)
- :material-file-search: **Runs:** [njit_bert](./runs.md#njit_bert) | [njit_roberta](./runs.md#njit_roberta) | [njit.roberta](./runs.md#njit.roberta) | [njit-semi.sup](./runs.md#njit-semi.sup) | [njit-label.prop](./runs.md#njit-label.prop) | [njit-semi_sup_cat2prior](./runs.md#njit-semi_sup_cat2prior) | [njit.label.prop.cat2prior](./runs.md#njit.label.prop.cat2prior) | [njit.augly.v2](./runs.md#njit.augly.v2) | [njit-EDA](./runs.md#njit-eda) | [njit.deberta](./runs.md#njit.deberta) | [njit-debly](./runs.md#njit-debly)

??? abstract "Abstract"
	
	In crisis informatics, data sparsity remains a crucial bottleneck for learning, and while numerous approaches exist to alleviate this issue, little domain-specific guidance exists for choosing or prioritizing these approaches. When developing a crisis informatics pipeline, there are majorly four areas to take into consideration, namely, augmentation, counter data imbalance, class selection for data augmentation, to consider which classes to augment, language model selection, and training methods. When considering these different sections of a crisis informatics pipeline, there is a lack of guidance regarding prioritization of these sections for optimization. For example, using an off-the-shelf, state-of-the-art pre-trained language model may give us some performance boost, but will an older model with better class-balanced dataset show better or similar performance, and if so, then should data augmentation be prioritized over model selection? Will a pipeline with multi-task learning give similar performance on a not so well-balanced dataset, and if so, should using better training methods be prioritized over selecting the best augmentation technique? These are some of the questions we aim to consider through our work. This paper provides this much needed domain-specific guidance by evaluating performance improvements across a series of data augmentations, model improvements, and learning designs. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SharmaB21.bib) "
	```
	@inproceedings{DBLP:conf/trec/SharmaB21,
		author = {Shivam Sharma and Cody Buntain},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Method Comparison for Crisis Pipelines},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/njit-IS.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SharmaB21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCD-CS at TREC 2021 Incident Streams Track

_Congcong Wang, David Lillis_

- :fontawesome-solid-user-group: **Participant:** [UCD-CS](./participants.md#ucd-cs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UCD-CS-IS.pdf](https://trec.nist.gov/pubs/trec30/papers/UCD-CS-IS.pdf)
- :material-file-search: **Runs:** [ucdcs-run2](./runs.md#ucdcs-run2) | [ucdcs-run1](./runs.md#ucdcs-run1) | [ucdcs-run3](./runs.md#ucdcs-run3) | [ucdcs-run4](./runs.md#ucdcs-run4) | [ucdcs-mtl.ens](./runs.md#ucdcs-mtl.ens) | [ucdcs-strans.nb](./runs.md#ucdcs-strans.nb) | [ucdcs-mtl.fta](./runs.md#ucdcs-mtl.fta) | [ucdcs-mtl.ens.fta](./runs.md#ucdcs-mtl.ens.fta) | [ucdcs-mtl.ens.new](./runs.md#ucdcs-mtl.ens.new) | [ucdcs-mtl.fta.nla](./runs.md#ucdcs-mtl.fta.nla)

??? abstract "Abstract"
	
	In recent years, the task of mining important information from social media posts during crises has become a focus of research for the purposes of assisting emergency response (ES). The TREC Incident Streams (IS) track is a research challenge organised for this purpose. The track asks participating systems to both classify a stream of crisis-related tweets into humanitarian aid related information types and estimate their importance regarding criticality. The former refers to a multi-label information type classification task and the latter refers to a priority estimation task. In this paper, we report on the participation of the University College Dublin School of Computer Science (UCD-CS) in TREC-IS 2021. We explored a variety of approaches, including simple machine learning algorithms, multi-task learning techniques, text augmentation, and ensemble approaches. The official evaluation results indicate that our runs achieve the highest scores in many metrics. To aid reproducibility, our code is publicly available.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangL21.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangL21,
		author = {Congcong Wang and David Lillis},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{UCD-CS} at {TREC} 2021 Incident Streams Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UCD-CS-IS.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WangL21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow Terrier Team (uogTr) at the TREC 2021 Incident  Streams Track

_Alexander J. Hepburn, Richard McCreadie_

- :fontawesome-solid-user-group: **Participant:** [uog_trec_team](./participants.md#uog_trec_team)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/uogTr-IS.pdf](https://trec.nist.gov/pubs/trec30/papers/uogTr-IS.pdf)
- :material-file-search: **Runs:** [uogTr-01-pw](./runs.md#uogtr-01-pw) | [uogTr-02-pwcoocc](./runs.md#uogtr-02-pwcoocc) | [uogTr-04-coocc](./runs.md#uogtr-04-coocc)

??? abstract "Abstract"
	
	In this paper, we detail our approach as part of the runs submitted on behalf of the University of Glasgow Terrier Team (uogTr) for the 2021-A/B edition of the Incident Streams track. Our approach employs the use of transfer learning between component labels of the dataset; more specifically, we decompose the traditional multi-label approach and investigate the relationship between each label as a binary classification task. We submit a total of three official runs to the 2021-A/B edition of the track, namely: uogTr-01-pw, uogTr-02-pwcoocc, and uogTr-04-coocc. Our results show that there exists potential for performance increase through transfer learning.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangMMOJMOHM21.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangMMOJMOHM21,
		author = {Alexander J. Hepburn and Richard McCreadie},
		editor = {Ian Soboroff and Angela Ellis},
		title = {University of Glasgow Terrier Team (uogTr) at the {TREC} 2021 Incident Streams Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/uogTr-IS.pdf},
		timestamp = {Thu, 31 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WangMMOJMOHM21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

