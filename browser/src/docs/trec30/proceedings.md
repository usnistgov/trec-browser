# Proceedings 2021 

## Overview of TREC 2021

_Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Overview-2021.pdf](https://trec.nist.gov/pubs/trec30/papers/Overview-2021.pdf)
??? abstract "Abstract"
	
	TREC 2021 is the thirtieth edition of the Text REtrieval Conference (TREC). The main goal of TREC is to create the evaluation infrastructure required for large-scale testing of information retrieval (IR) technology. This includes research on best methods for evaluation as well as development of the evaluation materials themselves. “Retrieval technology” is broadly interpreted to include a variety of techniques that enable and/or facilitate access to information that is not specifically structured for machine use. The TREC 2021 meeting was held at the National Institute of Standards and Technology (NIST) November 15-19, 2021. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Soboroff21.bib)"
	```
	@inproceedings{DBLP:conf/trec/Soboroff21,
		author = {Ian Soboroff},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of {TREC} 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Overview-2021.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Soboroff21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Incident Streams 

#### Siena's Incident Stream System SISS

_Ting Liu, Sharon Gower Small, Patrick Baumgardner, Lydia Cartwright, Michael Coppola, Samuil Orlioglu_

- :fontawesome-solid-user-group: **Participant:** [SienaCLTeam](./incident/participants.md#sienaclteam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/SienaCLTeam-IS.pdf](https://trec.nist.gov/pubs/trec30/papers/SienaCLTeam-IS.pdf)
- :material-file-search: **Runs:** [Siena2021A](./incident/runs.md#siena2021a)

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

- :fontawesome-solid-user-group: **Participant:** [L3i_Rochelle](./incident/participants.md#l3i_rochelle)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/L3i_Rochelle-IS.pdf](https://trec.nist.gov/pubs/trec30/papers/L3i_Rochelle-IS.pdf)
- :material-file-search: **Runs:** [RB_2Tx2_TTH_280](./incident/runs.md#rb_2tx2_tth_280) | [RB_2T_TTH_256_LR5](./incident/runs.md#rb_2t_tth_256_lr5) | [RB_2T_TT_280_SVM](./incident/runs.md#rb_2t_tt_280_svm) | [RB_2T_MT_H_280](./incident/runs.md#rb_2t_mt_h_280) | [l3i-ttxth](./incident/runs.md#l3i-ttxth) | [l3i-ttxth.combined](./incident/runs.md#l3i-ttxth.combined)

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

- :fontawesome-solid-user-group: **Participant:** [njit](./incident/participants.md#njit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/njit-IS.pdf](https://trec.nist.gov/pubs/trec30/papers/njit-IS.pdf)
- :material-file-search: **Runs:** [njit_bert](./incident/runs.md#njit_bert) | [njit_roberta](./incident/runs.md#njit_roberta) | [njit.roberta](./incident/runs.md#njit.roberta) | [njit-semi.sup](./incident/runs.md#njit-semi.sup) | [njit-label.prop](./incident/runs.md#njit-label.prop) | [njit-semi_sup_cat2prior](./incident/runs.md#njit-semi_sup_cat2prior) | [njit.label.prop.cat2prior](./incident/runs.md#njit.label.prop.cat2prior) | [njit.augly.v2](./incident/runs.md#njit.augly.v2) | [njit-EDA](./incident/runs.md#njit-eda) | [njit.deberta](./incident/runs.md#njit.deberta) | [njit-debly](./incident/runs.md#njit-debly)

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

- :fontawesome-solid-user-group: **Participant:** [UCD-CS](./incident/participants.md#ucd-cs)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UCD-CS-IS.pdf](https://trec.nist.gov/pubs/trec30/papers/UCD-CS-IS.pdf)
- :material-file-search: **Runs:** [ucdcs-run2](./incident/runs.md#ucdcs-run2) | [ucdcs-run1](./incident/runs.md#ucdcs-run1) | [ucdcs-run3](./incident/runs.md#ucdcs-run3) | [ucdcs-run4](./incident/runs.md#ucdcs-run4) | [ucdcs-mtl.ens](./incident/runs.md#ucdcs-mtl.ens) | [ucdcs-strans.nb](./incident/runs.md#ucdcs-strans.nb) | [ucdcs-mtl.fta](./incident/runs.md#ucdcs-mtl.fta) | [ucdcs-mtl.ens.fta](./incident/runs.md#ucdcs-mtl.ens.fta) | [ucdcs-mtl.ens.new](./incident/runs.md#ucdcs-mtl.ens.new) | [ucdcs-mtl.fta.nla](./incident/runs.md#ucdcs-mtl.fta.nla)

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

- :fontawesome-solid-user-group: **Participant:** [uog_trec_team](./incident/participants.md#uog_trec_team)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/uogTr-IS.pdf](https://trec.nist.gov/pubs/trec30/papers/uogTr-IS.pdf)
- :material-file-search: **Runs:** [uogTr-01-pw](./incident/runs.md#uogtr-01-pw) | [uogTr-02-pwcoocc](./incident/runs.md#uogtr-02-pwcoocc) | [uogTr-04-coocc](./incident/runs.md#uogtr-04-coocc)

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

## News 

#### IRCologne at TREC 2021 News Track Relation-based re-ranking for  background linking

_Björn Engelmann, Philipp Schaer_

- :fontawesome-solid-user-group: **Participant:** [IR-Cologne](./news/participants.md#ir-cologne)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IR-Cologne-N.pdf](https://trec.nist.gov/pubs/trec30/papers/IR-Cologne-N.pdf)
- :material-file-search: **Runs:** [base](./news/runs.md#base) | [rel00_ent07](./news/runs.md#rel00_ent07) | [rel02_ent05](./news/runs.md#rel02_ent05) | [rel05_ent02](./news/runs.md#rel05_ent02) | [rel07_ent00](./news/runs.md#rel07_ent00) | [bm25_sub_0.25](./news/runs.md#bm25_sub_0.25) | [bm25_sub_0.5](./news/runs.md#bm25_sub_0.5) | [bm25_sub_1.0](./news/runs.md#bm25_sub_1.0) | [bm25_sub_2](./news/runs.md#bm25_sub_2) | [bm25_sub_4](./news/runs.md#bm25_sub_4)

??? abstract "Abstract"
	
	This paper presents our approach to the background linking task of the TREC 2021 News Track. The background linking task is to find a set of relevant articles in the Washington Post dataset containing helpful background information for a given news article. Our approach involved a two-stage retrieval process. In the first stage, the 200 most relevant documents were extracted from the entire corpus using BM25. The second stage involved re-ranking using similarity scores based on entities and relations extracted from the query document and the associated 200 relevant documents. For this task, we submitted five runs, each giving different weights to the entities and relations. Our best run received a nDCG@5 of 0.4423, and we were thus able to show that re-ranking with the use of relations leads to a slight improvement over the baseline without re-ranking.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0002S21.bib) "
	```
	@inproceedings{DBLP:conf/trec/0002S21,
		author = {Bj{\"{o}}rn Engelmann and Philipp Schaer},
		editor = {Ian Soboroff and Angela Ellis},
		title = {IRCologne at {TREC} 2021 News Track Relation-based re-ranking for background linking},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IR-Cologne-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0002S21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Elastic Embedded Background Linking for News Articles with Keywords,  Entities and Events

_Luis Adrián Cabrera-Diego, Emanuela Boros, Antoine Doucet_

- :fontawesome-solid-user-group: **Participant:** [L3i_Rochelle](./news/participants.md#l3i_rochelle)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/L3i_Rochelle-N.pdf](https://trec.nist.gov/pubs/trec30/papers/L3i_Rochelle-N.pdf)
- :material-file-search: **Runs:** [300K_ENT_PH](./news/runs.md#300k_ent_ph) | [300K_ENT_PH_DN](./news/runs.md#300k_ent_ph_dn) | [KWVec](./news/runs.md#kwvec) | [KWVec_sub](./news/runs.md#kwvec_sub) | [Lambda](./news/runs.md#lambda) | [Lambda_narr](./news/runs.md#lambda_narr) | [Lambda_sub](./news/runs.md#lambda_sub) | [S300K_PH_DN](./news/runs.md#s300k_ph_dn) | [S300K_ENT_PH_DN](./news/runs.md#s300k_ent_ph_dn) | [S300K_ENT_P_DN2](./news/runs.md#s300k_ent_p_dn2)

??? abstract "Abstract"
	
	In this paper, we present a collection of five flexible background linking models created for the News Track in TREC 2021 that generate ranked lists of articles to provide contextual information. The collection is based on the use of sentence embeddings indexes, created with Sentence BERT and Open Distro for ElasticSearch. For each model, we explore additional tools, from keywords extraction using YAKE, to entity and event detection, while passing through a linear combination. The associated code is available online as open-source software.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Cabrera-DiegoBD21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Cabrera-DiegoBD21,
		author = {Luis Adri{\'{a}}n Cabrera{-}Diego and Emanuela Boros and Antoine Doucet},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Elastic Embedded Background Linking for News Articles with Keywords, Entities and Events},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/L3i\_Rochelle-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Cabrera-DiegoBD21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### bigIR at TREC 2021: Adopting Transfer Learning for News Background  Linking

_Marwa Essam, Tamer Elsayed_

- :fontawesome-solid-user-group: **Participant:** [QU](./news/participants.md#qu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/QU-N.pdf](https://trec.nist.gov/pubs/trec30/papers/QU-N.pdf)
- :material-file-search: **Runs:** [QU_SP_MBERT](./news/runs.md#qu_sp_mbert) | [QU_SP_MSM](./news/runs.md#qu_sp_msm) | [QU_SS_MSM](./news/runs.md#qu_ss_msm) | [QU_LeadPar](./news/runs.md#qu_leadpar) | [QU_YakeTruss](./news/runs.md#qu_yaketruss)

??? abstract "Abstract"
	
	In this paper, we present the participation of the bigIR team at Qatar University in the TREC 2021 news track. We participated in the background linking task. The task mainly aims to retrieve news articles that provide context and background knowledge to the reader of a specific query article. We submitted five runs for this task. In the first two, we adopted an ad-hoc retrieval approach, where the query articles were analyzed to generate search queries that were issued against the news articles collection to retrieve the required links. In the remaining runs, we adopted a transfer learning approach to rerank the articles retrieved given their usefulness to address specific subtopics related to the query articles. These subtopics were given by the track organizers as a new challenge this year. The results show that one of our runs outperformed TREC median submission, while others achieved comparable results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EssamE21.bib) "
	```
	@inproceedings{DBLP:conf/trec/EssamE21,
		author = {Marwa Essam and Tamer Elsayed},
		editor = {Ian Soboroff and Angela Ellis},
		title = {bigIR at {TREC} 2021: Adopting Transfer Learning for News Background Linking},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/QU-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/EssamE21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SU-NLP at TREC NEWS 2021

_Kenan Fayoumi, Reyyan Yeniterzi_

- :fontawesome-solid-user-group: **Participant:** [SU-NLP](./news/participants.md#su-nlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/SU-NLP-N.pdf](https://trec.nist.gov/pubs/trec30/papers/SU-NLP-N.pdf)
- :material-file-search: **Runs:** [SU_BiEnc](./news/runs.md#su_bienc) | [SU_BiEnc_CrsEnc](./news/runs.md#su_bienc_crsenc) | [SU_ES_CrsEnc](./news/runs.md#su_es_crsenc) | [SU_ES](./news/runs.md#su_es) | [SU_ES_CrsEnc_NF](./news/runs.md#su_es_crsenc_nf)

??? abstract "Abstract"
	
	This paper presents our work and submissions for the TREC 2021 News Track Wikification task. We approach the problem as an entity linking task initially and after identifying the mentions and their corresponding Wikipedia entities, we rank the mentions within the news article based on their usefulness. For the entity linking part, transformer-based architectures are explored for both detecting the mentions, generating the possible candidates and re-ranking them. Finally for the mention ranking, we use previous years' best performing approach which uses the position of the mention within the text
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FayoumiY21.bib) "
	```
	@inproceedings{DBLP:conf/trec/FayoumiY21,
		author = {Kenan Fayoumi and Reyyan Yeniterzi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{SU-NLP} at {TREC} {NEWS} 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/SU-NLP-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FayoumiY21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Middlebury at TREC News '21 Exploring Learning to Rank Model Variants

_Culton Koster, John Foley_

- :fontawesome-solid-user-group: **Participant:** [middlebury](./news/participants.md#middlebury)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/middlebury-N.pdf](https://trec.nist.gov/pubs/trec30/papers/middlebury-N.pdf)
- :material-file-search: **Runs:** [midd-rf](./news/runs.md#midd-rf) | [midd-direct](./news/runs.md#midd-direct) | [midd-twostage](./news/runs.md#midd-twostage) | [midd-transfer](./news/runs.md#midd-transfer)

??? abstract "Abstract"
	
	Middlebury College participated in the TREC News Background Linking task in 2021. We constructed a linear learning to rank model trained on the 2018-2020 data and submitted runs that included variants on the standard low resource learning-to-rank models. In this notebook paper we detail the contents of our submissions and our lessons learned from this year's participation. We explored a few variant models including a random forest ranker, linear models trained on that random forest, and two-stage linear models, but found that traditional, direct ranking still appears to be optimal.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KosterF21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KosterF21,
		author = {Culton Koster and John Foley},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Middlebury at {TREC} News '21 Exploring Learning to Rank Model Variants},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/middlebury-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KosterF21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Semantic Search for Background Linking in News Articles

_Udhav Sethi, Anup Anand Deshmukh_

- :fontawesome-solid-user-group: **Participant:** [Waterloo_Cormack](./news/participants.md#waterloo_cormack)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Waterloo_Cormack-N.pdf](https://trec.nist.gov/pubs/trec30/papers/Waterloo_Cormack-N.pdf)
- :material-file-search: **Runs:** [UW_UDHAVSETHI](./news/runs.md#uw_udhavsethi) | [UW_UDHAVSETHI_S](./news/runs.md#uw_udhavsethi_s) | [UW_UDHAV_S100](./news/runs.md#uw_udhav_s100)

??? abstract "Abstract"
	
	The task of background linking aims at recommending news articles to a reader that are most relevant for providing context and background for the query article. For this task, we propose a two-stage approach, IR-BERT, which combines the retrieval power of BM25 with the contextual understanding gained through a BERT-based model. We further propose the use of a diversity measure to evaluate the effectiveness of background linking approaches in retrieving a diverse set of documents. We provide a comparison of IR-BERT with other participating approaches at TREC 2021. We have open sourced our implementation on Github.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SethiD21.bib) "
	```
	@inproceedings{DBLP:conf/trec/SethiD21,
		author = {Udhav Sethi and Anup Anand Deshmukh},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Semantic Search for Background Linking in News Articles},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Waterloo\_Cormack-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SethiD21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Hagen @ TREC2021 News Track

_Stefan Wagenpfeil, Matthias L. Hemmje, Paul Mc Kevitt_

- :fontawesome-solid-user-group: **Participant:** [FUH](./news/participants.md#fuh)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/FUH-N.pdf](https://trec.nist.gov/pubs/trec30/papers/FUH-N.pdf)
- :material-file-search: **Runs:** [FUH_News_BG](./news/runs.md#fuh_news_bg) | [FUH_News_ST](./news/runs.md#fuh_news_st)

??? abstract "Abstract"
	
	This paper discusses University of Hagen's approach for the TREC2021 News Track. The News Track aims at providing relevant background links to documents of the Washington Post article archive. Our submitted run is based on research and development in the field of multimedia information retrieval and employs a modified TFIDF (Text Frequency vs. Inverse Document Frequency) algorithm for topic modeling and matrix based indexing operations founded on Graph Codes for the calculation of similarity, relevance, and recommendations. This run was submitted as FUH (Fernuniversit¨at Hagen) and obtained a nDCG@5 of 0.2655.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WagenpfeilHK21.bib) "
	```
	@inproceedings{DBLP:conf/trec/WagenpfeilHK21,
		author = {Stefan Wagenpfeil and Matthias L. Hemmje and Paul Mc Kevitt},
		editor = {Ian Soboroff and Angela Ellis},
		title = {University of Hagen @ {TREC2021} News Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/FUH-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WagenpfeilHK21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TKB48 at TREC 2021 News Track

_Lirong Zhang, Hideo Joho, Sumio Fujita_

- :fontawesome-solid-user-group: **Participant:** [TKB48](./news/participants.md#tkb48)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/TKB48-N.pdf](https://trec.nist.gov/pubs/trec30/papers/TKB48-N.pdf)
- :material-file-search: **Runs:** [TKB48_Run1_DTQ](./news/runs.md#tkb48_run1_dtq) | [TKB48_Run3_skw](./news/runs.md#tkb48_run3_skw) | [TKB48_Run4_tlkw](./news/runs.md#tkb48_run4_tlkw) | [TKB48_Run2_Tep](./news/runs.md#tkb48_run2_tep) | [TKB48_SRun1_DS](./news/runs.md#tkb48_srun1_ds) | [TKB48_SRun2_Tep](./news/runs.md#tkb48_srun2_tep) | [TKB48_SRun3_DTQ](./news/runs.md#tkb48_srun3_dtq) | [TKB48_SRun4_ST](./news/runs.md#tkb48_srun4_st)

??? abstract "Abstract"
	
	TKB48 incorporated document expansion methods such as docT5query and keyword extraction into indexing to solve the background linking problem. Using a transformer-based model, we calculated the text similarity of queries and documents at a semantic level and combined the semantic similarity and BM25 score for re-ranking background articles. We examined different combinations of re-ranking factors such as semantic similarities between expanded documents and attributes of topics. We found that increasing index fields produced by the docT5query model and keyword extraction model was beneficial. At the same time, the re-ranking performance was influenced by the amount of semantic similarity factors and their weight in the total relevance score. To discover the effectiveness of document expansion and our method using temporal recency, we further generated several unofficial runs incorporating a temporal topic classifier and learning to rank method. However, the lack of temporal topics limits the performance of the model. Our purposed algorithm outperformed the learning to rank method. Our future work will focus on fine-tuning of the docT5query model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangJF21.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangJF21,
		author = {Lirong Zhang and Hideo Joho and Sumio Fujita},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TKB48} at {TREC} 2021 News Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/TKB48-N.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangJF21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Fair Ranking 

#### Overview of the TREC 2021 Fair Ranking Track

_Michael D. Ekstrand, Amifa Raj, Graham McDonald, Isaac Johnson_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Overview-F.pdf](https://trec.nist.gov/pubs/trec30/papers/Overview-F.pdf)
??? abstract "Abstract"
	
	The TREC Fair Ranking Track aims to provide a platform for participants to develop and evaluate novel retrieval algorithms that can provide a fair exposure to a mixture of demographics or attributes, such as ethnicity, that are represented by relevant documents in response to a search query. For example, particular demographics or attributes can be represented by the documents' topical content or authors. The 2021 Fair Ranking Track adopted a resource allocation task. The task focused on supporting Wikipedia editors who are looking to improve the encyclopedia's coverage of topics under the purview of a WikiProject.1 WikiProject coordinators and/or Wikipedia editors search for Wikipedia documents that are in need of editing to improve the quality of the article. The 2021 Fair Ranking track aimed to ensure that documents that are about, or somehow represent, certain protected characteristics receive a fair exposure to the Wikipedia editors, so that the documents have an fair opportunity of being improved and, therefore, be well-represented in Wikipedia. The under-representation of particular protected characteristics in Wikipedia can result in systematic biases that can have a negative human, social, and economic impact, particularly for disadvantaged or protected societal groups [3, 5].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EkstrandRM021.bib) "
	```
	@inproceedings{DBLP:conf/trec/EkstrandRM021,
		author = {Michael D. Ekstrand and Amifa Raj and Graham McDonald and Isaac Johnson},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2021 Fair Ranking Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Overview-F.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/EkstrandRM021.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at TREC 2021 Fair Ranking Track

_Sachin Pathiyan Cherumanal, Damiano Spina, Falk Scholer, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [RMIT-IR](./fair/participants.md#rmit-ir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/RMIT-IR-F.pdf](https://trec.nist.gov/pubs/trec30/papers/RMIT-IR-F.pdf)
- :material-file-search: **Runs:** [RMITRetRerank_2](./fair/runs.md#rmitretrerank_2) | [RMITRetRerank_1](./fair/runs.md#rmitretrerank_1) | [RMITRet](./fair/runs.md#rmitret)

??? abstract "Abstract"
	
	This report describes the data, the assumptions, methodology, and our results involved in the participation at the TREC 2021 Fair Ranking Track. While most of the fairness-aware re-ranking techniques require explicitly defining protected attributes, we tried to leverage the implicit features of the Wikimedia articles by using an implicit diversification technique to study the impact of diversification on a fair ranking problem.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CherumanalSSC21.bib) "
	```
	@inproceedings{DBLP:conf/trec/CherumanalSSC21,
		author = {Sachin Pathiyan Cherumanal and Damiano Spina and Falk Scholer and W. Bruce Croft},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{RMIT} at {TREC} 2021 Fair Ranking Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/RMIT-IR-F.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CherumanalSSC21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TKB48 at TREC 2021 Fairness Ranking Track

_Zhuoqi Jin, Hideo Joho, Sumio Fujita_

- :fontawesome-solid-user-group: **Participant:** [TKB48](./fair/participants.md#tkb48)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/TKB48-F.pdf](https://trec.nist.gov/pubs/trec30/papers/TKB48-F.pdf)
- :material-file-search: **Runs:** [RUN1](./fair/runs.md#run1) | [RUN_task2](./fair/runs.md#run_task2)

??? abstract "Abstract"
	
	Fairness ranking has been recently focused on, which aims to make ranking results fair while keeping relevant. The definition of fairness is diverse. TREC Fairness Ranking Track in 2021 took attention- weighted rank fairness (AWRF) [12] to fit the fairness aspect distribution of ranking results to a population estimator ^p reflecting the target distribution. TKB48's approach was a post-processing method. We obtained an initial ranking using the BM25 score. We then set a bucket for each of 7 geographic areas in the dataset, and iterated the initial BM25 ranking to choose documents and put them into the bucket in a round-robin manner. As the track evaluated the top 20 results of the final ranking, the goal for us was to make the distribution of each area be the same as the target distribution in the top 20 results. We defined the individual fairness score so that we could choose whether a document should be put into the bucket by comparing an individual fairness score and BM25 score. The individual fairness score was based on how many documents in a certain area has been put into the final ranking. We chose one document with the highest combined score of fairness and relevance for one iterate turn of initial ranking. And we iterated 1000 times so that we could get a final ranking with 1000 documents. Our results ranked fifth out of 13 submissions on the TREC Fairness Ranking Track. Finally, we compared the results of different methods on the TREC Fairness Ranking Track and analyzed it.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JinJF21.bib) "
	```
	@inproceedings{DBLP:conf/trec/JinJF21,
		author = {Zhuoqi Jin and Hideo Joho and Sumio Fujita},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TKB48} at {TREC} 2021 Fairness Ranking Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/TKB48-F.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JinJF21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at the TREC 2021 Fair Ranking Track

_Ali Vardasbi, Gabriel Bénédict, Shashank Gupta, Maria Heuss, Pooya Khandel, Ming Li, Fatemeh Sarvi_

- :fontawesome-solid-user-group: **Participant:** [IRLab-Amsterdam](./fair/participants.md#irlab-amsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IRLab-Amsterdam-F.pdf](https://trec.nist.gov/pubs/trec30/papers/IRLab-Amsterdam-F.pdf)
- :material-file-search: **Runs:** [pl_control_0.6](./fair/runs.md#pl_control_0.6) | [pl_control_0.8](./fair/runs.md#pl_control_0.8) | [pl_control_0.92](./fair/runs.md#pl_control_0.92) | [2step_pair_list](./fair/runs.md#2step_pair_list) | [1step_pair_list](./fair/runs.md#1step_pair_list) | [2step_pair](./fair/runs.md#2step_pair) | [1step_pair](./fair/runs.md#1step_pair) | [PL_IRLab_05](./fair/runs.md#pl_irlab_05) | [PL_IRLab_07](./fair/runs.md#pl_irlab_07)

??? abstract "Abstract"
	
	TREC 2021 fair ranking track is composed of two tasks, intended to help WikiProject coordinators, with a static ranking of 1000 pages (Task1), as well as WikiPedia editors, with a stochastic ranking of 50 pages (Task2). The rankings should be fair with respect to geographical locations as well as an undisclosed demographic attribute. We have used a lexical matching method to detect two demographic attributes, namely gender and sexuality. For the static ranker of Task1, we tried a method based on swapping the items that result in largest marginal gain for the relevance-fairness compound objective. We have seen that the greedy pairwise swapping method leads to better results compared to other variants. For the probabilistic ranker of Task2, we used two sampling approaches. The first one is based on an existing control-theory inspired algorithm, and it leads to the best overall performance among our submissions. The second approach uses a two-stage Plackett-Luce and achieves very good disparity performance (in terms of EE-D), but overall, its performance is dominated by the first approach due to its low ranking performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VardasbiB0HKLS21.bib) "
	```
	@inproceedings{DBLP:conf/trec/VardasbiB0HKLS21,
		author = {Ali Vardasbi and Gabriel B{\'{e}}n{\'{e}}dict and Shashank Gupta and Maria Heuss and Pooya Khandel and Ming Li and Fatemeh Sarvi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {The University of Amsterdam at the {TREC} 2021 Fair Ranking Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IRLab-Amsterdam-F.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/VardasbiB0HKLS21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Deep Learning 

#### Overview of the TREC 2021 Deep Learning Track

_Nick Craswell, Bhaskar Mitra, Emine Yilmaz, Daniel Campos, Jimmy Lin_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Overview-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/Overview-DL.pdf)
??? abstract "Abstract"
	
	This is the third year of the TREC Deep Learning track. As in previous years, we leverage the MS MARCO datasets that made hundreds of thousands of human annotated training labels available for both passage and document ranking tasks. In addition, this year we refreshed both the document and the passage collections which also led to a nearly four times increase in the document collection size and nearly 16 times increase in the size of the passage collection. Deep neural ranking models that employ large scale pretraininig continued to outperform traditional retrieval methods this year. We also found that single stage retrieval can achieve good performance on both tasks although they still do not perform at par with multistage retrieval pipelines. Finally, the increase in the collection size and the general data refresh raised some questions about completeness of NIST judgments and the quality of the training labels that were mapped to the new collections from the old ones which we discuss in this report.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Craswell0YCL21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Craswell0YCL21,
		author = {Nick Craswell and Bhaskar Mitra and Emine Yilmaz and Daniel Campos and Jimmy Lin},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2021 Deep Learning Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Overview-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Craswell0YCL21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2021: Deep Learning, Health Misinformation, and Podcasts  Tracks

_Alexander Bondarenko, Maik Fröbe, Sebastian Günther, Matthias Hagen, Marcel Gohsen, Johannes Kiesel, Michael Völske, Benno Stein, Jakob Schwerter, Shahbaz Syed, Martin Potthast_

- :fontawesome-solid-user-group: **Participant:** [Webis](./deep/participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf)
- :material-file-search: **Runs:** [webis-dl-1](./deep/runs.md#webis-dl-1) | [webis-dl-2](./deep/runs.md#webis-dl-2) | [webis-dl-3](./deep/runs.md#webis-dl-3)

??? abstract "Abstract"
	
	We describe the Webis group's participation in the TREC 2021 Deep Learning, Health Misinformation, and Podcasts tracks. Our three LambdaMART-based runs submitted to the Deep Learning track focus on the question whether anchor text is an effective retrieval feature in the MS MARCO scenario. In the Health Misinformation track, we axiomatically re-ranked the top-20 results of BM25 and MonoT5 for argumentative topics. As for the Podcasts track, our submitted six runs focus on supervised classification of podcasts as entertaining, subjective, or containing discussion by using audio and text embeddings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001F0HGKV0SSP21.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001F0HGKV0SSP21,
		author = {Alexander Bondarenko and Maik Fr{\"{o}}be and Sebastian G{\"{u}}nther and Matthias Hagen and Marcel Gohsen and Johannes Kiesel and Michael V{\"{o}}lske and Benno Stein and Jakob Schwerter and Shahbaz Syed and Martin Potthast},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Webis at {TREC} 2021: Deep Learning, Health Misinformation, and Podcasts Tracks},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 17:23:07 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001F0HGKV0SSP21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CIP at TREC 2021 Deep Learning Track

_Xuanang Chen, Ben He, Le Sun, Yingfei Sun_

- :fontawesome-solid-user-group: **Participant:** [CIP](./deep/participants.md#cip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CIP-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/CIP-DL.pdf)
- :material-file-search: **Runs:** [CIP_run1](./deep/runs.md#cip_run1) | [CIP_run2](./deep/runs.md#cip_run2) | [CIP_run3](./deep/runs.md#cip_run3)

??? abstract "Abstract"
	
	This paper describes the CIP participation in the TREC 2021 Deep Learning Track. Akin to our previous participation, we adopt the passage-level BERT re-ranker in the re-ranking subtask of the document ranking task. Besides, we utilize the MS MARCO v1 passage dataset and both the MS MARCO v2 passage and document datasets to generate hopefully sufficient training data, and BERT re-ranker is fine-tuned on these three kinds of training data one by one. Meanwhile, we adopt pairwise hinge loss rather than pointwise cross-entropy loss this year for model training, to boost the ranking effectiveness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenH0S21.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenH0S21,
		author = {Xuanang Chen and Ben He and Le Sun and Yingfei Sun},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{CIP} at {TREC} 2021 Deep Learning Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CIP-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ChenH0S21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TU Wien at TREC DL and Podcast 2021: Simple Compression for  Dense Retrieval

_Sebastian Hofstätter, Mete Sertkan, Allan Hanbury_

- :fontawesome-solid-user-group: **Participant:** [TU_Vienna](./deep/participants.md#tu_vienna)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/TU_Vienna-DL-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/TU_Vienna-DL-Pod.pdf)
- :material-file-search: **Runs:** [TUW_DR_Base](./deep/runs.md#tuw_dr_base) | [TUW_TAS-B_768](./deep/runs.md#tuw_tas-b_768) | [TUW_TAS-B_ANN](./deep/runs.md#tuw_tas-b_ann) | [TUW_IDCM_S4](./deep/runs.md#tuw_idcm_s4) | [TUW_IDCM_ALL](./deep/runs.md#tuw_idcm_all)

??? abstract "Abstract"
	
	The IR group of TU Wien participated in two tracks at TREC 2021: Deep Learning and Podcast segment retrieval. We continued our focus from our previous TREC participations on efficient approaches for retrieval and re-ranking. We propose a simple training process for compressing a dense retrieval model's output. First, we train it with full capacity, and then add a compression, or dimensionality reduction, layer on top and conduct a second full training pass. At TREC 2021 we test this model in a blind evaluation and zero-shot collection transfer for both Deep Learning and Podcast tracks. For our participation at the Podcast segment retrieval track, we also employ hybrid sparse-dense retrieval. Furthermore, we utilize auxiliary information to re-rank the retrieved segments by entertainment and subjectivity signals. Our results show that our simple compression procedure with approximate nearest neighbor search achieves comparable in-domain results (minus 2 points nDCG@10 difference) to a full TAS-Balanced retriever and reasonable effectiveness in a zero-shot domain transfer (Podcast track), where we outperform BM25 by 6 points nDCG@10.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HofstatterSH21.bib) "
	```
	@inproceedings{DBLP:conf/trec/HofstatterSH21,
		author = {Sebastian Hofst{\"{a}}tter and Mete Sertkan and Allan Hanbury},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TU} Wien at {TREC} {DL} and Podcast 2021: Simple Compression for Dense Retrieval},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/TU\_Vienna-DL-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HofstatterSH21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2021: Deep Learning Track

_Yizheng Huang, Jimmy X. Huang_

- :fontawesome-solid-user-group: **Participant:** [yorku](./deep/participants.md#yorku)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/yorku-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/yorku-DL.pdf)
- :material-file-search: **Runs:** [yorku21_a](./deep/runs.md#yorku21_a) | [yorku21_b](./deep/runs.md#yorku21_b) | [yorku21_c](./deep/runs.md#yorku21_c)

??? abstract "Abstract"
	
	This is our first time to participate in TREC Deep Learning track. We submitted three BERT-based runs “YorkU21a”, “YorkU21b” and “YorkU21c”, where YorkU21a has the best performance. Our main goal is to explore the possibility of combining deep learning with traditional BM25 retrieval method. In this paper, we discuss the results of using the summation method to combine the above two approaches and provide some illustrative analyses on the impact of different retrieval strategies on the results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangH21.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangH21,
		author = {Yizheng Huang and Jimmy X. Huang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {York University at {TREC} 2021: Deep Learning Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/yorku-DL.pdf},
		timestamp = {Tue, 17 Oct 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangH21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### M4D-MKLab/ITI-CERTH Participation in TREC Deep Learning Track 2021

_Alexandros-Michail Koufakis, Theodora Tsikrika, Stefanos Vrochidis, Ioannis Kompatsiaris_

- :fontawesome-solid-user-group: **Participant:** [CERTH_ITI_M4D](./deep/participants.md#certh_iti_m4d)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CERTH_ITI_M4D-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/CERTH_ITI_M4D-DL.pdf)
- :material-file-search: **Runs:** [bigrams_cont_qe](./deep/runs.md#bigrams_cont_qe) | [bigram_qe_cedr](./deep/runs.md#bigram_qe_cedr)

??? abstract "Abstract"
	
	Our team's (CERTH ITI M4D) goal in the TREC Deep Learning Track was to study how the Contextualized Embedding Query Expansion (CEQE) [1] method performs in such setting and how our proposed modifications affect the performance. In particular, we examine how CEQE performs with the addition of bigrams as potential expansion terms, and how an IDF weight component affects the performance. The first run we submitted is produced by a query expansion pipeline that uses BM25 for retrieval and CEQE with the IDF modification for query expansion. The second submitted run used a modification of CEQE with the addition of bigrams as candidate expansion terms and a re-ranking step using CEDR. Our runs showed promising results, especially for Average Precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoufakisTVK21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoufakisTVK21,
		author = {Alexandros{-}Michail Koufakis and Theodora Tsikrika and Stefanos Vrochidis and Ioannis Kompatsiaris},
		editor = {Ian Soboroff and Angela Ellis},
		title = {M4D-MKLab/ITI-CERTH Participation in {TREC} Deep Learning Track 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CERTH\_ITI\_M4D-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KoufakisTVK21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Naver Labs Europe (SPLADE) @ TREC Deep Learning 2021

_Carlos Lassance, Arnaud Sors, Stéphane Clinchant, Thibault Formal, Benjamin Piwowarski_

- :fontawesome-solid-user-group: **Participant:** [NLE](./deep/participants.md#nle)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/NLE-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/NLE-DL.pdf)
- :material-file-search: **Runs:** [NLE_P_v1](./deep/runs.md#nle_p_v1) | [NLE_P_V1andV2](./deep/runs.md#nle_p_v1andv2) | [NLE_P_quick](./deep/runs.md#nle_p_quick) | [NLE_D_v1](./deep/runs.md#nle_d_v1) | [NLE_D_V1andV2](./deep/runs.md#nle_d_v1andv2) | [NLE_D_quick](./deep/runs.md#nle_d_quick)

??? abstract "Abstract"
	
	This paper describes our participation to the 2021 TREC Deep Learning challenge. We submitted runs to both passage and document full ranking tasks, with a focus on the passage task, where the goal is to retrieve and rank a set of 100 passages directly from the new MS MARCO v2 collection, containing around 138M entries. We rely on SPLADE for first-stage retrieval. For the second stage, we use an ensemble of BERT re-rankers, trained using hard negatives selected by SPLADE. Three runs were submitted, coming from a diverse set of experiments: i) a fast retriever without re-ranking nor query encoding (SPLADE-doc model), ii) a SPLADE model fully trained on MS MARCO v1, and re-ranked by an en- semble of models, and iii) an ensemble of SPLADE models trained on both new and old MS MARCO, re-ranked by an ensemble of models also trained on both datasets. Much to our surprise, out of the 3 runs, the one trained only on MS MARCO v1 obtained the best results on the TREC competition and is very competitive when compared to the median and best results. More surprising to us is that the results on the dev set of MS MARCO v2 did not correlate with TREC results, contrary to previous years.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LassanceSCFP21.bib) "
	```
	@inproceedings{DBLP:conf/trec/LassanceSCFP21,
		author = {Carlos Lassance and Arnaud Sors and St{\'{e}}phane Clinchant and Thibault Formal and Benjamin Piwowarski},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Naver Labs Europe {(SPLADE)} @ {TREC} Deep Learning 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/NLE-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LassanceSCFP21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### L3S at the TREC 2021 Deep Learning Track

_Jurek Leonhardt, Avishek Anand, Koustav Rudra_

- :fontawesome-solid-user-group: **Participant:** [L3S](./deep/participants.md#l3s)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/L3S-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/L3S-DL.pdf)
- :material-file-search: **Runs:** [Fast_Forward_2](./deep/runs.md#fast_forward_2) | [Fast_Forward_5](./deep/runs.md#fast_forward_5) | [Fast_Forward_7](./deep/runs.md#fast_forward_7) | [Fast_Forward_3](./deep/runs.md#fast_forward_3) | [Fast_ForwardP_2](./deep/runs.md#fast_forwardp_2) | [Fast_ForwardP_5](./deep/runs.md#fast_forwardp_5)

??? abstract "Abstract"
	
	In this paper we describe the approach we used for the passage and document ranking task in the TREC 2021 deep learning track. Our approach aims for efficient retrieval and re-ranking by making use of fast look-up-based forward indexes for dense dual-encoder models. The score of a query-document pair is computed as a linear interpolation of the corresponding lexical (BM25) and semantic (re-ranking) scores. This is akin to performing the re-ranking step “implicitly” together with the retrieval step. We improve efficiency by avoiding forward passes of expensive re-ranking models without compromising performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeonhardtAR21.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeonhardtAR21,
		author = {Jurek Leonhardt and Avishek Anand and Koustav Rudra},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{L3S} at the {TREC} 2021 Deep Learning Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/L3S-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LeonhardtAR21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Quality and Cost Trade-Offs in Passage Re-Ranking Task

_Pavel Podberezko, Vsevolod Mitskevich, Raman Makouski, Pavel Goncharov, Andrei Khobnia, Nikolay Bushkov, Marina Chernyshevich_

- :fontawesome-solid-user-group: **Participant:** [IHSM](./deep/participants.md#ihsm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IHSM-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/IHSM-DL.pdf)
- :material-file-search: **Runs:** [ihsm_colbert64](./deep/runs.md#ihsm_colbert64) | [ihsm_bicolbert](./deep/runs.md#ihsm_bicolbert) | [ihsm_poly8q](./deep/runs.md#ihsm_poly8q)

??? abstract "Abstract"
	
	Deep learning models named transformers achieved state-of-the-art results in a vast majority of NLP tasks at the cost of increased computational complexity and high memory consumption. Using the transformer model in real-time inference becomes a major challenge when implemented in production, because it requires expensive computational resources. The more executions of a transformer are needed the lower the overall throughput is, and switching to the smaller encoders leads to the decrease of accuracy. Our paper is devoted to the problem of how to choose the right architecture for the ranking step of the information retrieval pipeline, so that the number of required calls of transformer encoder is minimal with the maximum achievable quality of ranking. We investigated several late-interaction models such as Colbert and Poly-encoder architectures along with their modifications. Also, we took care of the memory footprint of the search index and tried to apply the learning-to-hash method to binarize the output vectors from the transformer encoders. The results of the evaluation are provided using TREC 2019-2021 and MS Marco dev datasets.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PodberezkoMMGKB21.bib) "
	```
	@inproceedings{DBLP:conf/trec/PodberezkoMMGKB21,
		author = {Pavel Podberezko and Vsevolod Mitskevich and Raman Makouski and Pavel Goncharov and Andrei Khobnia and Nikolay Bushkov and Marina Chernyshevich},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Quality and Cost Trade-Offs in Passage Re-Ranking Task},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IHSM-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PodberezkoMMGKB21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PASH at TREC 2021 Deep Learning Track: Generative Enhanced Model  for Multi-stageRankingtrack: DL

_Yixuan Qiao, Hao Chen, Tuozhen Liu, Xianbin Ye, Jun Wang, Peng Gao, Guotong Xie_

- :fontawesome-solid-user-group: **Participant:** [PASH](./deep/participants.md#pash)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/PASH-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/PASH-DL.pdf)
- :material-file-search: **Runs:** [pash_r1](./deep/runs.md#pash_r1) | [pash_r2](./deep/runs.md#pash_r2) | [pash_r3](./deep/runs.md#pash_r3) | [pash_f1](./deep/runs.md#pash_f1) | [pash_f2](./deep/runs.md#pash_f2) | [pash_f3](./deep/runs.md#pash_f3) | [pash_doc_r1](./deep/runs.md#pash_doc_r1) | [pash_doc_r2](./deep/runs.md#pash_doc_r2) | [pash_doc_f1](./deep/runs.md#pash_doc_f1) | [pash_doc_f4](./deep/runs.md#pash_doc_f4) | [pash_doc_f5](./deep/runs.md#pash_doc_f5) | [pash_doc_r3](./deep/runs.md#pash_doc_r3)

??? abstract "Abstract"
	
	This paper describes the PASH participation in TREC 2021 Deep Learning Track. In the recall stage, we adopt a scheme combining sparse and dense retrieval method. In the multi-stage ranking phase, point-wise and pair-wise ranking strategies are used one after another based on model continual pre-trained on general knowledge and document-level data. Compared to TREC 2020 Deep Learning Track, we have additionally introduced the generative model T5 to further enhance the performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiaoC0GXLYX21.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiaoC0GXLYX21,
		author = {Yixuan Qiao and Hao Chen and Tuozhen Liu and Xianbin Ye and Jun Wang and Peng Gao and Guotong Xie},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{PASH} at {TREC} 2021 Deep Learning Track: Generative Enhanced Model for Multi-stageRankingtrack: {DL}},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/PASH-DL.pdf},
		timestamp = {Fri, 15 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/QiaoC0GXLYX21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Recall Aspects of Transformers for Text Ranking

_David Rau, Jaap Kamps_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./deep/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UAmsterdam-DL.pdf](https://trec.nist.gov/pubs/trec30/papers/UAmsterdam-DL.pdf)
- :material-file-search: **Runs:** [top1000](./deep/runs.md#top1000)

??? abstract "Abstract"
	
	This paper documents the University of Amsterdam's participation in the TREC 2021 Deep Learning Track. In addition to providing labeled training data at scale, the other major contribution of the TREC DL track is to avoid the pool-bias exhibited in all the earlier adhoc search test collections created through the pooling only runs from traditional sparse retrieval systems. However, even in the TREC deep learning track, we have shallow pools, and runs with varying but high fractions of unjudged documents. This prompts a deeper analysis of pool coverage over ranks for both a representative traditional approach (i.e., BM25) and a representative neural approach (i.e., the BERT cross-encoder for the passage retrieval task). Our main conclusions are the following. First, we submitted a neural run that specifically looks beyond those documents easily found by traditional models, highlighting the potential of neural models to address recall aspects in addition to the precision aspects prioritized in the TREC Deep Learning Track up to now. Second, we observe high fractions of unjudged documents after the initial ranks for both the 2020 and 2021 data, which may hinder the evaluation of recall-oriented aspects and reusability of the judgments for runs not contributing to the pooling. Third, we observe a gradual decline of the fraction of relevant over judged documents for 2020, which is a positive sign against pooling bias, but almost no decrease for 2021. Our general conclusion is that coverage below the guaranteed pooling horizon is far from complete and that analysis of recall aspects must be done with care, but that there is great potential to study these in future editions of the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RauK21.bib) "
	```
	@inproceedings{DBLP:conf/trec/RauK21,
		author = {David Rau and Jaap Kamps},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Recall Aspects of Transformers for Text Ranking},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UAmsterdam-DL.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RauK21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Clinical Trials 

#### Alibaba DAMO Academy at TREC Clinical Trials 2021: ExploringEmbedding-based  First-stage Retrieval with TrialMatcher

_Qiao Jin, Chuanqi Tan, Zhengyun Zhao, Zheng Yuan, Songfang Huang_

- :fontawesome-solid-user-group: **Participant:** [ALIBABA](./trials/participants.md#alibaba)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/ALIBABA_CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/ALIBABA_CAsT.pdf)
- :material-file-search: **Runs:** [damohitl](./trials/runs.md#damohitl) | [damohitls](./trials/runs.md#damohitls) | [damoebrtog](./trials/runs.md#damoebrtog) | [damoebrsigir](./trials/runs.md#damoebrsigir) | [damoebr](./trials/runs.md#damoebr)

??? abstract "Abstract"
	
	This paper describes the submissions of Ailbaba DAMO Academy to the TREC 2021 Clinical Trials Track, where the task is to match eligible clinical trials for given patient notes. Our systems follow the standard retrieval-reranking procedure. We propose a novel embedding-based retrieval model, TrialMatcher, as the retriever. TrialMatcher contains a patient note encoder and a clinical trial encoder pre-trained by 370k clinical trial documents. It retrieves relevant clinical trials based on embedding space distances. We then use different re-rankers to reorder the candidates returned by Trial-Matcher. In automatic runs, the re-rankers are trained by a relevant dataset or a synthetic patient-trial relevance dataset. In manual runs, the re-rankers are trained by annotations derived from a human-in-the-loop active learning strategy. Our automatic runs rank the second in all participants on all four metrics. Our manual runs rank the first on one metric, and the second on three other metrics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001TZ0H21.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001TZ0H21,
		author = {Qiao Jin and Chuanqi Tan and Zhengyun Zhao and Zheng Yuan and Songfang Huang},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Alibaba {DAMO} Academy at {TREC} Clinical Trials 2021: ExploringEmbedding-based First-stage Retrieval with TrialMatcher},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/ALIBABA\_CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001TZ0H21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IBM @ TREC Clinical Trials Track 2021

_Laura Biester, Venkata Joopudi, Bharath Dandala_

- :fontawesome-solid-user-group: **Participant:** [IBMResearch](./trials/participants.md#ibmresearch)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IBMResearch-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/IBMResearch-CT.pdf)
- :material-file-search: **Runs:** [IBMLucene](./trials/runs.md#ibmlucene) | [IBMSTS](./trials/runs.md#ibmsts) | [IBMSIGIR](./trials/runs.md#ibmsigir) | [IBMAUTOGT](./trials/runs.md#ibmautogt) | [IBMSIGIRACT](./trials/runs.md#ibmsigiract)

??? abstract "Abstract"
	
	Although clinical trials are crucial to the advancement of medical science, many clinical trials fail because they do not meet recruitment targets. This problem engenders a need for automated systems that can match patients to ongoing trials. The potential benefits of such systems are twofold: first, they would allow for the systematic study of new treatments through completed clinical trials and second, they could improve or even save the lives of patients for whom existing treatments are ineffective. We participate in the TREC Clinical Trials (CT) Track, for which the aim is to match synthetic 5-10 sentence patient descriptions with clinical trials from ClinicalTrials.gov, a clinical trials repository that includes all clinical trials in the United States. Our system uses BM25 and semantic textual similarity (STS) models to retrieve two thousand candidates from hundreds of thousands of clinical trials. We then proceed to rerank those trials using neural reranking models with BERT-based encoders and novel attention mechanisms. In addition to training our models on an existing related corpus [Koopman and Zuccon, 2016], we leverage data from MIMIC-III to generate a larger training corpus. In the end, we found that our BM25-based ranker utilizing a Lucene index outperformed our neural models, likely due to a lack of high-quality training data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BiesterJD21.bib) "
	```
	@inproceedings{DBLP:conf/trec/BiesterJD21,
		author = {Laura Biester and Venkata Joopudi and Bharath Dandala},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{IBM} @ {TREC} Clinical Trials Track 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IBMResearch-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BiesterJD21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SIB Text Mining at TREC Clinical Trials 2021

_Déborah Caucheteur, Emilie Pasche, Luc Mottin, Anaïs Mottaz, Julien Gobeill, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BITEM](./trials/participants.md#bitem)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/BITEM-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/BITEM-CT.pdf)
- :material-file-search: **Runs:** [SIBTMct1](./trials/runs.md#sibtmct1) | [SIBTMct2](./trials/runs.md#sibtmct2) | [SIBTMct3](./trials/runs.md#sibtmct3) | [SIBTMct4](./trials/runs.md#sibtmct4) | [SIBTMct5](./trials/runs.md#sibtmct5)

??? abstract "Abstract"
	
	TREC 2021 Clinical Trials Track aimed to develop algorithms to improve patient recruitment in clinical trials. These recruitment problems represent a real obstacle to medical research, leading to delays in clinical trial schedules and sometimes even to the termination of the trial due to the lack of eligible patients recruited. A set of 75 topics was distributed to participants. Each topic represents a patient's medical record, in other words a patient case description in free text format. In parallel, a set of clinical trials from ClinicalTrials.gov was also provided. The challenge was then to determine for each patient, if during a recruitment phase for a clinical trial from the corpus, the patient would be assessed as eligible, excluded or irrelevant. As an output, for each topic, our system returns a list of clinical trials ranked from the highest (relevant) score to the lowest within the limit of 1,000 results per topic. In total, five strategies were tested corresponding to the five runs submitted and will be described in this paper. The publication of the results at the TREC conference in November 2021 will indicate whether one of the strategies has proved more likely to deliver good results or whether, on the contrary, the work should be redirected towards new ideas.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaucheteurPMMGR21.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaucheteurPMMGR21,
		author = {D{\'{e}}borah Caucheteur and Emilie Pasche and Luc Mottin and Ana{\"{\i}}s Mottaz and Julien Gobeill and Patrick Ruch},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{SIB} Text Mining at {TREC} Clinical Trials 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/BITEM-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/CaucheteurPMMGR21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pozna'n Contribution to TREC Clinical Trials 2021⋆

_Jakub Dutkiewicz, Czeslaw Jedrzejek_

- :fontawesome-solid-user-group: **Participant:** [POZNAN](./trials/participants.md#poznan)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/POZNAN-PM.pdf](https://trec.nist.gov/pubs/trec30/papers/POZNAN-PM.pdf)
- :material-file-search: **Runs:** [pozAbbrMesh](./trials/runs.md#pozabbrmesh) | [pozAddTerms](./trials/runs.md#pozaddterms) | [pozFulltext](./trials/runs.md#pozfulltext) | [pozMeshTerms](./trials/runs.md#pozmeshterms) | [pozTermFds](./trials/runs.md#poztermfds)

??? abstract "Abstract"
	
	In this papaer we go over our approach to TREC Clinical Trials 2021. We discuss the architecture of our retrieval system. Specifically, we describe the used topic processing techniques. We recount the structure of a document and our methods of interpreting and extracting data from the document. This paper also covers the description of experiments we proposed for TREC Clinical Trials 2021. We conclude with a brief discussion of the obtained results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DutkiewiczJ21.bib) "
	```
	@inproceedings{DBLP:conf/trec/DutkiewiczJ21,
		author = {Jakub Dutkiewicz and Czeslaw Jedrzejek},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Pozna'n Contribution to {TREC} Clinical Trials 2021{\(\star\)}},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/POZNAN-PM.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/DutkiewiczJ21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An approach to relevant clinical trials retrieving

_Mariia Fedorova_

- :fontawesome-solid-user-group: **Participant:** [clinical_trials](./trials/participants.md#clinical_trials)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/clinical_trials-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/clinical_trials-CT.pdf)
- :material-file-search: **Runs:** [RUN0](./trials/runs.md#run0) | [RUN1FREQS](./trials/runs.md#run1freqs) | [RUN3SENTS](./trials/runs.md#run3sents)

??? abstract "Abstract"
	
	In this notebook paper an approach to retrieving relevant clinical trials for patients' unstructured descriptions (electronic health records, EHTs) is described.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Fedorova21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Fedorova21,
		author = {Mariia Fedorova},
		editor = {Ian Soboroff and Angela Ellis},
		title = {An approach to relevant clinical trials retrieving},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/clinical\_trials-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Fedorova21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2021⋆ Clinical Trials Retrieval, Duisburg-Essen University  submission

_Sameh Frihat, Norbert Fuhr_

- :fontawesome-solid-user-group: **Participant:** [IRUniDUE](./trials/participants.md#irunidue)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IRUniDUE-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/IRUniDUE-CT.pdf)
- :material-file-search: **Runs:** [first_run](./trials/runs.md#first_run) | [second_run](./trials/runs.md#second_run) | [third_run](./trials/runs.md#third_run) | [fourth_run](./trials/runs.md#fourth_run) | [fifth_run](./trials/runs.md#fifth_run)

??? abstract "Abstract"
	
	Clinical trials are human research studies that aim to evaluate a medical, surgical, or behavioral intervention that is critical to the advancement of medical science. The majority of clinical trials fail because recruitment goals are not met. This issue necessitates the incorporation of automated systems capable of matching patients to ongoing clinical trials. This paper summarizes our participation in the TREC 2021 clinical trials track, which provided all participants with a 5-10 sentence patient description and a clinical trials database from ClinicalTrials.gov for matching. Our submission consists of a variety of retrieval techniques, including BM25, entity recognition, BERT, and others. The results show that a simple BM25 ranking algorithm could outperform neural network-based models, mainly due to the absence of quality training data.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FrihatF21.bib) "
	```
	@inproceedings{DBLP:conf/trec/FrihatF21,
		author = {Sameh Frihat and Norbert Fuhr},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC} 2021{\(\star\)} Clinical Trials Retrieval, Duisburg-Essen University submission},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IRUniDUE-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FrihatF21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Clinical Trial Search Using Lucene and UMLS

_Yanqing Ji, Yun Tian, Hao Ying, John Tran_

- :fontawesome-solid-user-group: **Participant:** [GU_BioMed](./trials/participants.md#gu_biomed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/GU_BioMed-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/GU_BioMed-CT.pdf)
- :material-file-search: **Runs:** [TxtInc](./trials/runs.md#txtinc) | [TxtIncExc](./trials/runs.md#txtincexc) | [CuiInc](./trials/runs.md#cuiinc) | [TxtIncExcExp](./trials/runs.md#txtincexcexp) | [CuiIncExc](./trials/runs.md#cuiincexc)

??? abstract "Abstract"
	
	We approached the clinical trial search task of the 2021 TREC Clinical Trials Track as a query problem. A query (also known as a topic in 2021 TREC) is the free text description of a patient record, while the corpus is a large set of clinical trials descriptions. A commercial search engine, Lucene, was utilized for this clinical trial matching process. Namely, given a query, the system searches in the corpus and returns a subset of clinical trials with specific requirements. In this study, Unified Medical Language System (UMLS) was employed to convert the free text of both topics and clinical trials to more meaningful biomedical concepts, each of which is represented as a Concept Unique Identifier (CUI). An expansion technique based on Medical Subject Headings (MeSH) was used to expand all the condition terms for each clinical trial to their child terms. To assess whether UMLS can improve the search accuracy, we designed two groups of tests: one group uses free text, while the other uses CUIs for both queries and clinical trial corpuses. As the inclusion/exclusion criteria represent the core aspect of each trial description, we also examined whether the exclusion criteria played an important role in the process of selecting a clinical trial. We extracted the inclusion criteria and exclusion criteria for each clinical study and saved them into two separate corpuses. For each group of tests, we searched against the corpus with inclusion criteria only and also against both corpuses. When searching in both corpuses, for each query (i.e. a patient profile), the search results were sorted using the difference of the two Lucene scores that were returned when searching against the two corpuses, respectively. For the free text group, we also tested whether the expansion technique could improve the performance. Our experiment results demonstrated that the CUI-based search clearly outperformed the text-based search, which indicated the effectiveness of UMLS in text preprocessing and biomedical concept extraction. Our methods of using the exclusion criteria information and the MeSH-based term expansion technique were not as effective as we expected.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiTYT21.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiTYT21,
		author = {Yanqing Ji and Yun Tian and Hao Ying and John Tran},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Clinical Trial Search Using Lucene and {UMLS}},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/GU\_BioMed-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JiTYT21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2021 Clinical Trials Submission for Universidad del País  Vasco

_Jordan Koontz, Maite Oronoz, Alicia Pérez_

- :fontawesome-solid-user-group: **Participant:** [uni_pais_vasco](./trials/participants.md#uni_pais_vasco)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/uni_pais_vasco-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/uni_pais_vasco-CT.pdf)
- :material-file-search: **Runs:** [LaBSE](./trials/runs.md#labse) | [specter](./trials/runs.md#specter) | [LaBSE_rerank](./trials/runs.md#labse_rerank) | [spect_rerank](./trials/runs.md#spect_rerank) | [spec_rrk_fqv](./trials/runs.md#spec_rrk_fqv)

??? abstract "Abstract"
	
	This paper describes the University of the Basque Country's submission to the TREC 2021 Clinical Trials Track. We begin by summarizing the documents by extracting medical entities. Next, we utilize multi-lingual and scientific domain sentence embeddings to represent the summarized clinical trials descriptions and the patient topic documents. Lastly, we rank the clinical trial relevance by calculating the cosine similarities between texts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KoontzOP21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KoontzOP21,
		author = {Jordan Koontz and Maite Oronoz and Alicia P{\'{e}}rez},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC} 2021 Clinical Trials Submission for Universidad del Pa{\'{\i}}s Vasco},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/uni\_pais\_vasco-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KoontzOP21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DOSSIER at TREC 2021 Clinical Trials Track

_Wojciech Kusa, Yasin Ghafourian_

- :fontawesome-solid-user-group: **Participant:** [DOSSIER](./trials/participants.md#dossier)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/DOSSIER-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/DOSSIER-CT.pdf)
- :material-file-search: **Runs:** [baseline](./trials/runs.md#baseline) | [postproc](./trials/runs.md#postproc) | [rerank2000](./trials/runs.md#rerank2000)

??? abstract "Abstract"
	
	This paper describes our experimental setup and results for the Clinical Trials Track at TREC 2021. In particular, we study (i) the effectiveness of post-processing with patients' metadata and (ii) the novel re-ranking formula using eligibility criteria. We find that the post-processing improves the model over the baseline run. However, the custom re-ranking negatively impacts average results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KusaG21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KusaG21,
		author = {Wojciech Kusa and Yasin Ghafourian},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{DOSSIER} at {TREC} 2021 Clinical Trials Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/DOSSIER-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KusaG21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNTIIA Lab at TREC 2021 - Clinical Trial

_Huyen Nguyen, Haihua Chen, Bhanu Prasad, Huanhuan Zhao, Junhua Ding, Jiangping Chen, Ana D. Cleveland_

- :fontawesome-solid-user-group: **Participant:** [UNTIIA](./trials/participants.md#untiia)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UNTIIA-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/UNTIIA-CT.pdf)
- :material-file-search: **Runs:** [UNTIIARUN1](./trials/runs.md#untiiarun1) | [UNTIIARUN2](./trials/runs.md#untiiarun2) | [UNTIIARUN3](./trials/runs.md#untiiarun3) | [UNTIIARUN4](./trials/runs.md#untiiarun4) | [UNTIIARUN5](./trials/runs.md#untiiarun5)

??? abstract "Abstract"
	
	This paper reports our participation in 2021 TREC Clinical Trial (CT) track based on the ElasticSearch information retrieval platform. We studied different query extraction and query expansion methods with both manual and automatic strategies for query construction. Our experiments on the 2016 Clinical Decision Support collection proved the effectiveness of the knowledge base mapping method for both query extraction and expansion. We proposed a novel query construction strategy to balance precision and accuracy: we retrieve clinical trials documents with a complete list of query terms first and then decrease the number of query terms used for searching additional documents to improve recall. We also investigated two transformer-based models for reranking: unsupervised and supervised learning. Pairs of query and candidate documents were encoded with the sentence-BERT in the unsupervised reranking model, and then their semantic similarity was compared using a Cross-encoder model. We also took advantage of BERT transformers for the supervised reranking model by finetuning the model on the ground truth of the 2016 Clinical Decision Support collection and then feeding it into the TFR-BERT model for reranking. Our experiment indicates that the unsupervised transformer reranking model outperformed the supervised learning model and achieved the highest performance among teams on a number of topics
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Nguyen0PZDCC21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Nguyen0PZDCC21,
		author = {Huyen Nguyen and Haihua Chen and Bhanu Prasad and Huanhuan Zhao and Junhua Ding and Jiangping Chen and Ana D. Cleveland},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{UNTIIA} Lab at {TREC} 2021 - Clinical Trial},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UNTIIA-CT.pdf},
		timestamp = {Tue, 29 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Nguyen0PZDCC21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Filter, Transform, Expand, and Fuse The IMS Unipd at TREC 2021  Clinical Trials

_Giorgio Maria Di Nunzio, Guglielmo Faggioli, Stefano Marchesin_

- :fontawesome-solid-user-group: **Participant:** [ims_unipd](./trials/participants.md#ims_unipd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/ims_unipd-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/ims_unipd-CT.pdf)
- :material-file-search: **Runs:** [RM3Filtered](./trials/runs.md#rm3filtered) | [BARTRM3Filt](./trials/runs.md#bartrm3filt) | [T5RM3Filt](./trials/runs.md#t5rm3filt) | [imsFused1](./trials/runs.md#imsfused1) | [imsFused2](./trials/runs.md#imsfused2)

??? abstract "Abstract"
	
	We present the methodology and the experimental setting of the participation of the IMS Unipd team in TREC Clinical Trials 2021. The objective of this work is to continue the longitudinal study of the evaluation of query expansion, ranking fusion, and document filtering approach optimized in the previous participation to TREC. In particular, we added to our procedure proposed in 2020, a comparison with a pipeline that use the large transformers. The results obtained provide interesting insights in terms of the different per-topic effectiveness and will be used for further failure analyses.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NunzioF021.bib) "
	```
	@inproceedings{DBLP:conf/trec/NunzioF021,
		author = {Giorgio Maria Di Nunzio and Guglielmo Faggioli and Stefano Marchesin},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Filter, Transform, Expand, and Fuse The {IMS} Unipd at {TREC} 2021 Clinical Trials},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/ims\_unipd-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NunzioF021.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNIMIB at TREC 2021 Clinical Trials Track

_Georgios Peikos, Oscar Espitia, Gabriella Pasi_

- :fontawesome-solid-user-group: **Participant:** [UNIMIB](./trials/participants.md#unimib)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UNIMIB-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/UNIMIB-CT.pdf)
- :material-file-search: **Runs:** [UNM_5](./trials/runs.md#unm_5) | [UNM_4](./trials/runs.md#unm_4) | [IKR3_BSL](./trials/runs.md#ikr3_bsl) | [IKR3_TT_MW_k](./trials/runs.md#ikr3_tt_mw_k) | [IKR3_TT_MW_d](./trials/runs.md#ikr3_tt_mw_d)

??? abstract "Abstract"
	
	This contribution summarizes the participation of the UNIMIB team to the TREC 2021 Clinical Trials Track. We have investigated the effect of different query representations combined with several retrieval models on the retrieval performance. First, we have implemented a neural re-ranking approach to study the effectiveness of dense text representations. Additionally, we have investigated the effectiveness of a novel decision-theoretic model for relevance estimation. Finally, both of the above relevance models have been compared with standard retrieval approaches. In particular, we combined a keyword extraction method with a standard retrieval process based on the BM25 model and a decision-theoretic relevance model that exploits the characteristics of this particular search task. The obtained results show that the proposed keyword extraction method improves 84% of the queries over the TREC's median NDCG@10 measure when combined with either traditional or decision-theoretic relevance models. Moreover, regarding RPEC@10, the employed decision-theoretic model improves 85% of the queries over the reported TREC's median value.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PeikosEP21.bib) "
	```
	@inproceedings{DBLP:conf/trec/PeikosEP21,
		author = {Georgios Peikos and Oscar Espitia and Gabriella Pasi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{UNIMIB} at {TREC} 2021 Clinical Trials Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UNIMIB-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/PeikosEP21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSIROmed Team Report of TREC 2021 Clinical Trials track: Experiments  with BERT Reranking Methods

_Maciej Rybinski, Vincent Nguyen, Sarvnaz Karimi_

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./trials/participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CSIROmed-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/CSIROmed-CT.pdf)
- :material-file-search: **Runs:** [CSIROmed_abs](./trials/runs.md#csiromed_abs) | [CSIROmed_inc](./trials/runs.md#csiromed_inc) | [CSIROmed_DCT](./trials/runs.md#csiromed_dct) | [CSIROmedNIR](./trials/runs.md#csiromednir) | [CSIROmed_brd](./trials/runs.md#csiromed_brd)

??? abstract "Abstract"
	
	A large body of clinical trials fail to attract enough eligible participants. TREC 2021 Clinical Trials track set a task to use patient data in the form of clinical notes as a way to identify patients eligible for clinical trials. We explore a number of reranking methods as well as query rewighting using Bidi- rectional Encoder Representations from Transformers (BERT). Our best method used BERT reranking trained on scientific literature.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RybinskiNK21.bib) "
	```
	@inproceedings{DBLP:conf/trec/RybinskiNK21,
		author = {Maciej Rybinski and Vincent Nguyen and Sarvnaz Karimi},
		editor = {Ian Soboroff and Angela Ellis},
		title = {CSIROmed Team Report of {TREC} 2021 Clinical Trials track: Experiments with {BERT} Reranking Methods},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CSIROmed-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RybinskiNK21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WisPerMed Text at TREC Clinical Trials Track 2021

_Henning Schäfer, Ahmad Idrissi-Yaghir, Wolfgang Galetzka, Marie Bexte, Christoph M. Friedrich_

- :fontawesome-solid-user-group: **Participant:** [wispermedtxt](./trials/participants.md#wispermedtxt)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/wispermedtxt-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/wispermedtxt-CT.pdf)
- :material-file-search: **Runs:** [wpm_biobert](./trials/runs.md#wpm_biobert) | [wpm_CBert](./trials/runs.md#wpm_cbert) | [wpm_KWBM25](./trials/runs.md#wpm_kwbm25) | [wpm_bmre](./trials/runs.md#wpm_bmre) | [wpm_critumls](./trials/runs.md#wpm_critumls)

??? abstract "Abstract"
	
	This paper describes the submissions of the WisPerMed Text group to the TREC Clinical Trials Track 2021. It aims to overcome the problems in patient recruitment that often lead to delays or even discontinuation of clinical trials. The focus here is finding methods to improve the process of matching patient case descriptions to eligible clinical trials. For this purpose, different systems were proposed and tested to rank the trials for each patient topic. These systems utilize methods such as transformer-based models, BM25 and keyword extraction. Additionally, Unified Medical Language System (UMLS) was used in an attempt to find relevancy between patient topics and clinical trials based on biomedical concepts. The results obtained showed that the BM25 model based on keyword extraction performed the best out of all our submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchaferIFGFB21.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchaferIFGFB21,
		author = {Henning Sch{\"{a}}fer and Ahmad Idrissi{-}Yaghir and Wolfgang Galetzka and Marie Bexte and Christoph M. Friedrich},
		editor = {Ian Soboroff and Angela Ellis},
		title = {WisPerMed Text at {TREC} Clinical Trials Track 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/wispermedtxt-CT.pdf},
		timestamp = {Fri, 15 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SchaferIFGFB21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ITTC @ TREC 2021 Clinical Trials Track

_Hung-Thinh Truong, Yulia Otmakhova, Timothy Baldwin, Jey Han Lau, Trevor Cohn, Karin Verspoor, Rahmad Mahendra, Lawrence Cavedon, Damiano Spina_

- :fontawesome-solid-user-group: **Participant:** [ITTC-AIMedTech](./trials/participants.md#ittc-aimedtech)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/ITTC-AIMedTech-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/ITTC-AIMedTech-CT.pdf)
- :material-file-search: **Runs:** [ittc1](./trials/runs.md#ittc1) | [ittc2](./trials/runs.md#ittc2) | [ittc3](./trials/runs.md#ittc3) | [ittc4](./trials/runs.md#ittc4) | [ittc5](./trials/runs.md#ittc5)

??? abstract "Abstract"
	
	This paper describes the submissions of the Natural Language Processing (NLP) team from the Australian Research Council Industrial Transformation Training Centre (ITTC) for Cognitive Computing in Medical Technolo- gies to the TREC 2021 Clinical Trials Track. The task focuses on the problem of matching eligible clinical trials to topics constituting a summary of a patient's admission notes. We explore different ways of representing trials and topics using NLP techniques, and then use a common retrieval model to generate the ranked list of relevant trials for each topic. The results from all our submitted runs are well above the median scores for all topics, but there is still plenty of scope for improvement.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Truong0BLCVMCS21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Truong0BLCVMCS21,
		author = {Hung{-}Thinh Truong and Yulia Otmakhova and Timothy Baldwin and Jey Han Lau and Trevor Cohn and Karin Verspoor and Rahmad Mahendra and Lawrence Cavedon and Damiano Spina},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{ITTC} @ {TREC} 2021 Clinical Trials Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/ITTC-AIMedTech-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Truong0BLCVMCS21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CincyMedIR at TREC 2021 Clinical Trial Track

_Hoang Vu, Danny T. Y. Wu_

- :fontawesome-solid-user-group: **Participant:** [CincyMedIR](./trials/participants.md#cincymedir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CincyMedIR-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/CincyMedIR-CT.pdf)
- :material-file-search: **Runs:** [CincyMedIR_1](./trials/runs.md#cincymedir_1) | [CincyMedIR_2](./trials/runs.md#cincymedir_2) | [CincyMedIR_3](./trials/runs.md#cincymedir_3) | [CincyMedIR_4](./trials/runs.md#cincymedir_4) | [CincyMedIR_5](./trials/runs.md#cincymedir_5)

??? abstract "Abstract"
	
	The CincyMedIR team led by Dr. Danny T.Y. Wu at the University of Cincinnati College of Medicine participated in the Text Retrieval Conference 2021 Clinical Trials Track (TREC-CT). This year, we applied our existing text-retrieval methods from our previous TREC tracks on the new Clinical Trials track while also experimenting with new techniques to process the trial exclusion criteria.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VuW21.bib) "
	```
	@inproceedings{DBLP:conf/trec/VuW21,
		author = {Hoang Vu and Danny T. Y. Wu},
		editor = {Ian Soboroff and Angela Ellis},
		title = {CincyMedIR at {TREC} 2021 Clinical Trial Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CincyMedIR-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/VuW21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Application of Traditional IE as a Non-traditional Method in  an IR Task: TDMINER at 2021 TREC Clinical Trials

_Chengyi Zheng_

- :fontawesome-solid-user-group: **Participant:** [TDMINER](./trials/participants.md#tdminer)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/TDMINER-CT.pdf](https://trec.nist.gov/pubs/trec30/papers/TDMINER-CT.pdf)
- :material-file-search: **Runs:** [tdminerrun1](./trials/runs.md#tdminerrun1) | [tdminerrun2](./trials/runs.md#tdminerrun2) | [tdminerrun3](./trials/runs.md#tdminerrun3) | [tdminerrun4](./trials/runs.md#tdminerrun4)

??? abstract "Abstract"
	
	The 2021 TREC Clinical Trials (CT) task focused on finding appropriate trials based on the health profiles of individual patients. This notebook details our participation in the 2021 TREC CT. In this paper, we presented the findings of our first participation in the TREC task. The TREC Clinical Trials (CT) goal for 2021 was to discover appropriate trials based on the health characteristics of individual patients. This notebook details our participation in the TREC CT in 2021 (team TDMINER). We presented the findings of our initial participation in the TREC task in this publication. Traditional information retrieval approaches, such as Elasticsearch with BM25 or DFR with query expansion, and machine learning-based rerankers, such as BERT, were used in previous efforts. Unlike these methods, we concentrated on developing an IE-based baseline that could be utilized as a starting point for future research. As part of our two-stage IR process, we implemented a basic weight-scaled reranking method. We submitted our results in the manual run category since we manually reranked the IE-identified concepts for each topic. There were 26 teams in total, with 101 automatic runs and 12 manual runs submitted. In terms of NDCG@10, PREC@10, and mean reciprocal rank (MRR), we achieved final ranking scores of 0.715, 0.576, and 0.834, respectively. In manual runs, the averaged median scores for these assessment criteria were 0.621, 0.457, and 0.721; in automatic runs, 0.304, 0.161, and 0.294. Our system ranked first on the NDCG@10 and MRR, second on the PREC@10 among all the submissions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Zheng21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Zheng21,
		author = {Chengyi Zheng},
		editor = {Ian Soboroff and Angela Ellis},
		title = {The Application of Traditional {IE} as a Non-traditional Method in an {IR} Task: {TDMINER} at 2021 {TREC} Clinical Trials},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/TDMINER-CT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Zheng21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Conversational Assistance 

#### TREC CAsT 2021: The Conversational Assistance Track Overview

_Jeffrey Dalton, Chenyan Xiong, Jamie Callan_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Overview-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/Overview-CAsT.pdf)
??? abstract "Abstract"
	
	CAsT 2021 is the third year of the Conversational Assistance Track. The techniques for conversational search continue to evolve as the task becomes more challenging. Proven neural query rewriting and ranking approaches based on pre-trained language models continue to improve with new large-scale datasets. As there is increased dependence on long result history, models that discriminatively select relevant parts of the conversation history are increasingly important. The traditional NLP approaches continue to be used, but generative approaches based on large-scale pre-trained language models are most widely used. One important development this year is the use of dense retrieval approaches. The results show that these models are complementary to traditional search approaches and appear to improve recall, but still usually require a multi-pass neural re-ranking model to be most effective. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001XC21.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001XC21,
		author = {Jeffrey Dalton and Chenyan Xiong and Jamie Callan},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC} CAsT 2021: The Conversational Assistance Track Overview},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Overview-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001XC21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MLIA-LIP6@TREC-CAST2021: Feature augmentation for query recontextualization  and passage ranking

_Nawel Astaouti, Thomas Gerald, Maya Touzari, Laure Soulier, Jian-Yun Nie_

- :fontawesome-solid-user-group: **Participant:** [MLIA-LIP6](./cast/participants.md#mlia-lip6)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/MLIA-LIP6-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/MLIA-LIP6-CAsT.pdf)
- :material-file-search: **Runs:** [t5colbert](./cast/runs.md#t5colbert) | [Rewritt5_monot5](./cast/runs.md#rewritt5_monot5) | [t5_monot5](./cast/runs.md#t5_monot5) | [t5_doc2query](./cast/runs.md#t5_doc2query)

??? abstract "Abstract"
	
	In this work, we investigate approaches for query recontextualization in the context of conversational search. We use a pipeline setting in which we first reformulate the query and then rank passages according to a backbone model. Our main focus is put on the feature inputs of a T5 query reformulation model and we evaluate different evidence sources such as the history (previous questions and answers) as well as semantic proxy through the doc2query model. We also experiment an end-to-end version of the setting which unfortunately has not been much optimized due to time constraints.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AstaoutiGTSN21.bib) "
	```
	@inproceedings{DBLP:conf/trec/AstaoutiGTSN21,
		author = {Nawel Astaouti and Thomas Gerald and Maya Touzari and Laure Soulier and Jian{-}Yun Nie},
		editor = {Ian Soboroff and Angela Ellis},
		title = {MLIA-LIP6@TREC-CAST2021: Feature augmentation for query recontextualization and passage ranking},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/MLIA-LIP6-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AstaoutiGTSN21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IITD-DBAI: Multi-Stage Retrieval with Pseudo-Relevance Feedback  and Query Reformulation

_Shivani Choudhary_

- :fontawesome-solid-user-group: **Participant:** [IITD-DBAI](./cast/participants.md#iitd-dbai)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IITD-DBAI-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/IITD-DBAI-CAsT.pdf)
- :material-file-search: **Runs:** [IITD-RAW_U_T5_1](./cast/runs.md#iitd-raw_u_t5_1) | [IITD-RAW_U_T5_2](./cast/runs.md#iitd-raw_u_t5_2)

??? abstract "Abstract"
	
	Conversational systems have acquired the center stage in NLP research. Compared to the conventional information retrieval task where we have to extract the passage or document from a vast collection of documents, the Conversational system requires extracting related information to respond to a series of questions. The turns in the conversation may follow the previous question. Complexity in this task arises due to the way we form the queries, which often have a reference to previous information using pronouns, co-reference. The presence of pronouns and unresolved co-references induces ambiguity in the query. Resolving the contextual dependency is one of the most challenging tasks in the Conversational system. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Choudhary21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Choudhary21,
		author = {Shivani Choudhary},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{IITD-DBAI:} Multi-Stage Retrieval with Pseudo-Relevance Feedback and Query Reformulation},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IITD-DBAI-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Choudhary21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TKB48 at TREC 2021 Conversational Assistance Track

_Yubo Fang, Hideo Joho, Sumio Fujita_

- :fontawesome-solid-user-group: **Participant:** [TKB48](./cast/participants.md#tkb48)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/TKB48_CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/TKB48_CAsT.pdf)
- :material-file-search: **Runs:** [dense_manual](./cast/runs.md#dense_manual) | [sparse_manual](./cast/runs.md#sparse_manual) | [hybrid_manual](./cast/runs.md#hybrid_manual) | [bm25_automatic](./cast/runs.md#bm25_automatic)

??? abstract "Abstract"
	
	In this paper, we present TKB48's methods and submitted runs for the TREC Conversational Assistance Track of Y3. We incorporated dense retrieval methods into the conversational task. We leveraged a Dual-encoder structure[ 2] to encode the user's utterance together with the conversation context and each document of the corpus into dense vector representation. After embedding we computed their relevance score by the dot product of the dense vectors. Our four submitted runs show an competitive performance compared to a sparse retrieval model. In addition to the submitted runs, we further conducted experiments and created two unofficial runs, which followed ConvDR's [29 ] strategy and trained the conversational dense retrieval model and performed inference on CAsT21 dataset. The results of these two unofficial runs show an effective use of multiple loss functions for conversational search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FangJF21.bib) "
	```
	@inproceedings{DBLP:conf/trec/FangJF21,
		author = {Yubo Fang and Hideo Joho and Sumio Fujita},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TKB48} at {TREC} 2021 Conversational Assistance Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/TKB48\_CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/FangJF21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Query Rewriting with Expansion and Multi-Turn Entity Graphs for Answer  Selection

_Nour Jedidi, Gustavo Gonçalves, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU-LTI](./cast/participants.md#cmu-lti)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CMU-LTI-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/CMU-LTI-CAsT.pdf)
- :material-file-search: **Runs:** [LTI-rewriter-tc](./cast/runs.md#lti-rewriter-tc) | [LTI-rewriter-5q](./cast/runs.md#lti-rewriter-5q) | [LTI-entity-g](./cast/runs.md#lti-entity-g) | [LTI-rewriter-g](./cast/runs.md#lti-rewriter-g)

??? abstract "Abstract"
	
	Conversational search is challenging in part because often the meaning of the current question cannot be fully understood without contextual information from previous questions and/or answers. This paper describes research on using query reformulation and lightweight reranking based on a multi-turn entity graph to represent and make use of contextual information in the CAsT 2021 track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JedidiGC21.bib) "
	```
	@inproceedings{DBLP:conf/trec/JedidiGC21,
		author = {Nour Jedidi and Gustavo Gon{\c{c}}alves and Jamie Callan},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Query Rewriting with Expansion and Multi-Turn Entity Graphs for Answer Selection},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CMU-LTI-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JedidiGC21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Radboud University at TREC CAsT 2021

_Hideaki Joko, Emma J. Gerritse, Faegheh Hasibi, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [RUIR](./cast/participants.md#ruir)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/RUIR-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/RUIR-CAsT.pdf)
- :material-file-search: **Runs:** [RUIR1_TURN-FT](./cast/runs.md#ruir1_turn-ft) | [RUIR2_TURN](./cast/runs.md#ruir2_turn) | [RUIR4_HIST](./cast/runs.md#ruir4_hist)

??? abstract "Abstract"
	
	This paper describes Radboud University's participation in the TREC Conversational Assistance Track (CAsT) 2021 for the manually rewritten utterances. We propose an entity-enriched BERT-based re- trieval model, where entity information is injected into the BERT model, and compare it to the regular BERT-based retrieval model. We annotate the manually resolved user utterances with named entities using an entity linker, and inject both text and entity representations into our entity-enriched BERT-based retrieval model. We present our experimental setup, results, and analysis of helped and hurt queries when using entity information.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JokoGHV21.bib) "
	```
	@inproceedings{DBLP:conf/trec/JokoGHV21,
		author = {Hideaki Joko and Emma J. Gerritse and Faegheh Hasibi and Arjen P. de Vries},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Radboud University at {TREC} CAsT 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/RUIR-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JokoGHV21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Exploration Study of Multi-stage Conversational Passage Retrieval:  Paraphrase Query Expansion and Multi-view Point-wise Ranking

_Jia-Huei Ju, Chih-Ting Yeh, Cheng-Wei Lin, Chia-Ying Tsao, Jun-En Ding, Chuan-Ju Wang, Ming-Feng Tsai_

- :fontawesome-solid-user-group: **Participant:** [CFDA_CLIP](./cast/participants.md#cfda_clip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CFDA_CLIP-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/CFDA_CLIP-CAsT.pdf)
- :material-file-search: **Runs:** [CFDA_CLIP_MRUN1](./cast/runs.md#cfda_clip_mrun1) | [CFDA_CLIP_MRUN2](./cast/runs.md#cfda_clip_mrun2) | [CFDA_CLIP_ARUN1](./cast/runs.md#cfda_clip_arun1) | [CFDA_CLIP_ARUN2](./cast/runs.md#cfda_clip_arun2)

??? abstract "Abstract"
	
	In this paper, we report our methods and experiments for the TREC Conversational Assistance Track (CAsT) 2021. In this work, We aim to improve the conversational information seeking system by reforming the modules in the existing multi-stage conversational search pipeline. In the first-stage document retrieval, we proposed the Paraphrase Query Expansion (PQE), which is adapted to the less-training-data scenario like CAsT. As for the second-stage re-ranking, we adopt the T5 point-wise ranking model with multi-view learning framework (monoT5M) to avoid the underlying overfitting problems. To further elucidate the effectiveness of our proposed methods, we also report the ablation studies of our proposed modules.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JuYLTDWT21.bib) "
	```
	@inproceedings{DBLP:conf/trec/JuYLTDWT21,
		author = {Jia{-}Huei Ju and Chih{-}Ting Yeh and Cheng{-}Wei Lin and Chia{-}Ying Tsao and Jun{-}En Ding and Chuan{-}Ju Wang and Ming{-}Feng Tsai},
		editor = {Ian Soboroff and Angela Ellis},
		title = {An Exploration Study of Multi-stage Conversational Passage Retrieval: Paraphrase Query Expansion and Multi-view Point-wise Ranking},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CFDA\_CLIP-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/JuYLTDWT21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Stavanger (IAI) at the TREC 2021 Conversational  Assistance Track

_Ivica Kostric, Krisztian Balog, Magnus Book, Trond Linjordet, Vinay Setty_

- :fontawesome-solid-user-group: **Participant:** [UiS](./cast/participants.md#uis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UiS-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/UiS-CAsT.pdf)
- :material-file-search: **Runs:** [UiS_raft](./cast/runs.md#uis_raft)

??? abstract "Abstract"
	
	This paper describes the participation of the IAI group at the University of Stavanger in the TREC 2021 Conversational Assistance track. The focus of our submission was to produce a strong baseline on top of which future research can be conducted. We followed the already established two-step passage ranking architecture, i.e., first-pass passage retrieval followed by re-ranking. In the first step, standard BM25 ranking is used. For the second step, we used a T5 model pre-trained on the MS MARCO QA dataset. Initial results suggest that our submission constitutes a reasonable and competitive baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KostricBBLS21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KostricBBLS21,
		author = {Ivica Kostric and Krisztian Balog and Magnus Book and Trond Linjordet and Vinay Setty},
		editor = {Ian Soboroff and Angela Ellis},
		title = {The University of Stavanger {(IAI)} at the {TREC} 2021 Conversational Assistance Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UiS-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KostricBBLS21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRLab-Amsterdam at TREC 2021 Conversational Assistant Track

_Antonios Minas Krasakis, Evangelos Kanoulas_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./cast/participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/IRlab-Amsterdam-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/IRlab-Amsterdam-CAsT.pdf)
- :material-file-search: **Runs:** [astypalaia256](./cast/runs.md#astypalaia256) | [historyonly](./cast/runs.md#historyonly) | [historyonlyKILT](./cast/runs.md#historyonlykilt)

??? abstract "Abstract"
	
	This paper describes our participation (IRLab-Amsterdam) in TREC CAsT 2021. Our approach adapts a pre-trained token-level dense retriever (ColBERT) to perform zero-shot conversational search. Specifically, our query encoder reads the entire conversation history to contextualize the embeddings of the last user utterance/query, while the token-level matching function uses the contextualized embeddings to retrieve directly from the collection. The advantages of our method are two-fold: (a) it does not need any conversational data for training (ie. query resolutions, or conversational relevance judgements) and (b) it avoids complex pipeline systems based on rewriting that can affect performance (response latency) and robustness.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KrasakisK21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KrasakisK21,
		author = {Antonios Minas Krasakis and Evangelos Kanoulas},
		editor = {Ian Soboroff and Angela Ellis},
		title = {IRLab-Amsterdam at {TREC} 2021 Conversational Assistant Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/IRlab-Amsterdam-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KrasakisK21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding Context through Utterance Dependencies in Search Conversations  - Participation of the CNR Team in CAsT 2021

_Ida Mele, Cristina Ioana Muntean, Franco Maria Nardini, Raffaele Perego, Nicola Tonellotto_

- :fontawesome-solid-user-group: **Participant:** [CNR](./cast/participants.md#cnr)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CNR-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/CNR-CAsT.pdf)
- :material-file-search: **Runs:** [CNR-run1](./cast/runs.md#cnr-run1) | [CNR-run2](./cast/runs.md#cnr-run2) | [CNR-run4](./cast/runs.md#cnr-run4) | [CNR-run3](./cast/runs.md#cnr-run3)

??? abstract "Abstract"
	
	To help research on Conversational Information Seeking, TREC has organized a competition on conversational assistant systems, called Conversational Assistant Track (CAsT). It provides test collections for open-domain conversational search systems. For our participation in CAsT 2021, we implemented a three-step architecture consisting of: (i) automatic utterance rewriting, (ii) first-stage retrieval of candidate passages, and (iii) neural re-ranking of candidate passages. Each run is based on a different utterance rewriting technique for enriching the raw utterance with context extracted from the previous utterances and/or replies in the conversation. Two of our approaches use only raw utterances and other two use utterances plus the canonical responses of the automatically rewritten utterances provided by CAsT 2021. Our approaches also rely on utterances manually classified by human assessors using a taxonomy defined ad hoc for this task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeleMN0T21.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeleMN0T21,
		author = {Ida Mele and Cristina Ioana Muntean and Franco Maria Nardini and Raffaele Perego and Nicola Tonellotto},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Finding Context through Utterance Dependencies in Search Conversations - Participation of the {CNR} Team in CAsT 2021},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CNR-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MeleMN0T21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Full-Collection Search with Passage and Document Evidence: Maryland  at the TREC 2021 Conversational Assistance Track

_Xin Qian, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [UMD](./cast/participants.md#umd)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UMD-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/UMD-CAsT.pdf)
- :material-file-search: **Runs:** [umd2021_run1](./cast/runs.md#umd2021_run1) | [umd2021_run2doc](./cast/runs.md#umd2021_run2doc) | [umd2021_run3rrf](./cast/runs.md#umd2021_run3rrf) | [umd2021_run4den](./cast/runs.md#umd2021_run4den)

??? abstract "Abstract"
	
	The University of Maryland (UMD) team submitted four runs to the automatic canonical condition of the track, exploring three ideas: (1) indexing both document-scale and passage-scale features, (2) using sharding to scale dense retrieval to large collections, and (3) combining results from sparse and dense methods using re-ranking and result fusion. Compared with the three-stage baseline pipeline of query rewriting using T5-base, document retrieval using BM25, and passage re-ranking using monoT5, UMD Run #1 modifies the second stage to retrieve passages rather than documents. UMD Run #2 retrieves documents in the second stage, but augments each second-stage document with additional document-scale evidence. UMD Run #3, our best run, fuses the final output of three runs: UMD Run #1, UMD Run #2, and the organizer-provided baseline. UMD Run #4, fuses results from TCT-ColBERT (a distilled ColBERT model) passage retrieval with results from BM25 document retrieval as the second stage. The TCT-ColBERT passage retrieval uses sharding to accommodate the large collection size. In each case, the first stage is the organizer-provided baseline query rewriter, and the third stage is a re-implementation of the baseline's third stage, but using monoBERT-large.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QianO21.bib) "
	```
	@inproceedings{DBLP:conf/trec/QianO21,
		author = {Xin Qian and Douglas W. Oard},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Full-Collection Search with Passage and Document Evidence: Maryland at the {TREC} 2021 Conversational Assistance Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UMD-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/QianO21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke at the TREC 2021 Conversational Assistant Track

_Xinyi Yan, Charles L. A. Clarke, Negar Arabzadeh_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./cast/participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/WaterlooClarke-CAsT.pdf](https://trec.nist.gov/pubs/trec30/papers/WaterlooClarke-CAsT.pdf)
- :material-file-search: **Runs:** [clarke-manual](./cast/runs.md#clarke-manual) | [clarke-cc](./cast/runs.md#clarke-cc) | [clarke-auto](./cast/runs.md#clarke-auto)

??? abstract "Abstract"
	
	For TREC 2021, the WaterlooClarke group submitted three runs to TREC Conversational Assistance Track (CAsT): clarke-auto, clarke-cc, and clarke-manual. The three runs were based on raw utterances, canonical response, and manually rewritten utterances respectively. This report describes the generation and the results of each of these runs. The overall approach consists of three steps: 1) query reformulation, 2) passage retrieval, and 3) passage reranking. We did not apply the query reformulation step for the clarke-manual run as manually rewritten utterances were used. In order to improve our performance, this year we focused our effort on maximizing the total system recall at the first stage by employing both dense and sparse retrievers. Research has shown that sparse retrievers and dense retrievers can retrieve complementary information [3]. We merged the retrieved passages into a single pool, then reranked this pool using a two-stage reranking pipeline with monoT5 and duoT5 [4]. In the next section, we will explain the details of our methodology.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YanCA21.bib) "
	```
	@inproceedings{DBLP:conf/trec/YanCA21,
		author = {Xinyi Yan and Charles L. A. Clarke and Negar Arabzadeh},
		editor = {Ian Soboroff and Angela Ellis},
		title = {WaterlooClarke at the {TREC} 2021 Conversational Assistant Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/WaterlooClarke-CAsT.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YanCA21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Health Misinformation 

#### Overview of the TREC 2021 Health Misinformation Track

_Charles L. A. Clarke, Maria Maistro, Mark D. Smucker_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Overview-HM.pdf](https://trec.nist.gov/pubs/trec30/papers/Overview-HM.pdf)
??? abstract "Abstract"
	
	TREC 2021 was the third year for the Health Misinformation track, which was named the Decision Track in 2019 [1]. In 2021, the track had an ad-hoc retrieval task. In each year, the track has used a crawl for its document collection. In 2019 and 2021, we used web crawls, and in 2020, we used a web crawl restricted to news sites. By focusing on health-related ad-hoc web search, the track brings new challenges to the web retrieval task. The most striking difference is that for health search, documents containing incorrect information are considered to be harmful and not merely non-relevant. As such, retrieval systems need to actively work to avoid including or ranking this incorrect, harmful information highly in the results. For relevant documents that contain correct information, we prefer sources with higher credibility. This year, each topic's description was expressed as a question, for example “Should I apply ice to a burn?”. A topic also has a query, for example “put ice on a burn”, that represents what a user might enter if they do not ask a full question. All topics concern themselves with determining the efficacy of a treatment for a health issue. Based on a credible source of information, we declare a stance for a topic as either helpful or unhelpful. We provide an evidence URL link to the source we used to determine the stance. Each topic is also supplied with a narrative providing additional clarification to the assessors. Automatic runs could only make use of the topic's query or description. If a run used the narrative, stance, or evidence, it had to be considered a manual run. A challenge of health-related search is determining what is correct information, i.e., determining the correct stance for a topic. Based on the assessors' judgments, we establish a preference ordering for documents considered to be helpful as well as for documents considered to be harmful. Helpful documents are supportive of helpful treatments or try to dissuade the reader from using unhelpful treatments. Harmful documents encourage use of unhelpful treatments or dissuade the reader from using helpful treatments. Whether a treatment is considered helpful or unhelpful is based on our provided stance. Submitted runs are evaluated based on their compatibility [4, 5] with both a preference ordering for helpful documents as well as a preference ordering for harmful documents. The best runs have high compatibility with the helpful preference ordering and low compatibility with the harmful ordering. The preference orderings take into consideration the usefulness, correctness, and credibility of the documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ClarkeMS21.bib) "
	```
	@inproceedings{DBLP:conf/trec/ClarkeMS21,
		author = {Charles L. A. Clarke and Maria Maistro and Mark D. Smucker},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Overview of the {TREC} 2021 Health Misinformation Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Overview-HM.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ClarkeMS21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2021: Deep Learning, Health Misinformation, and Podcasts  Tracks

_Alexander Bondarenko, Maik Fröbe, Sebastian Günther, Matthias Hagen, Marcel Gohsen, Johannes Kiesel, Michael Völske, Benno Stein, Jakob Schwerter, Shahbaz Syed, Martin Potthast_

- :fontawesome-solid-user-group: **Participant:** [Webis](./misinfo/participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf)
- :material-file-search: **Runs:** [webis-bm25](./misinfo/runs.md#webis-bm25) | [webis-t5](./misinfo/runs.md#webis-t5) | [webis-bm25-ax1](./misinfo/runs.md#webis-bm25-ax1) | [webis-bm25-ax3](./misinfo/runs.md#webis-bm25-ax3) | [webis-t5-ax1](./misinfo/runs.md#webis-t5-ax1) | [webis-t5-ax3](./misinfo/runs.md#webis-t5-ax3)

??? abstract "Abstract"
	
	We describe the Webis group's participation in the TREC 2021 Deep Learning, Health Misinformation, and Podcasts tracks. Our three LambdaMART-based runs submitted to the Deep Learning track focus on the question whether anchor text is an effective retrieval feature in the MS MARCO scenario. In the Health Misinformation track, we axiomatically re-ranked the top-20 results of BM25 and MonoT5 for argumentative topics. As for the Podcasts track, our submitted six runs focus on supervised classification of podcasts as entertaining, subjective, or containing discussion by using audio and text embeddings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001F0HGKV0SSP21.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001F0HGKV0SSP21,
		author = {Alexander Bondarenko and Maik Fr{\"{o}}be and Sebastian G{\"{u}}nther and Matthias Hagen and Marcel Gohsen and Johannes Kiesel and Michael V{\"{o}}lske and Benno Stein and Jakob Schwerter and Shahbaz Syed and Martin Potthast},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Webis at {TREC} 2021: Deep Learning, Health Misinformation, and Podcasts Tracks},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 17:23:07 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001F0HGKV0SSP21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UWaterlooMDS at the TREC 2021 Health Misinformation Track

_Mustafa Abualsaud, Kamyar Ghajar, Linh Nhi Phan Minh, Dake Zhang, Irene Xiangyi Chen, Mark D. Smucker, Amir Vakili Tahami_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./misinfo/participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UwaterlooMDS-HM.pdf](https://trec.nist.gov/pubs/trec30/papers/UwaterlooMDS-HM.pdf)
- :material-file-search: **Runs:** [WatSAM-BM25](./misinfo/runs.md#watsam-bm25) | [WatSMM-CAL](./misinfo/runs.md#watsmm-cal) | [WatSMC-CAL](./misinfo/runs.md#watsmc-cal) | [WatSMM-CALHC](./misinfo/runs.md#watsmm-calhc) | [WatSMM-CALPR](./misinfo/runs.md#watsmm-calpr) | [WatSMM-Fused](./misinfo/runs.md#watsmm-fused) | [WatSMM-CALQA100](./misinfo/runs.md#watsmm-calqa100) | [WatSMM-CALQAAll](./misinfo/runs.md#watsmm-calqaall) | [WatSMC-CALQA100](./misinfo/runs.md#watsmc-calqa100) | [WatSMC-CALQAAll](./misinfo/runs.md#watsmc-calqaall) | [WatSMC-CALQAHC1](./misinfo/runs.md#watsmc-calqahc1) | [WatSMC-CALQAHC2](./misinfo/runs.md#watsmc-calqahc2) | [WatSMC-Correct](./misinfo/runs.md#watsmc-correct) | [baselineBM25](./misinfo/runs.md#baselinebm25) | [WatSAE-BM25](./misinfo/runs.md#watsae-bm25) | [WatSAE-BM25RM3](./misinfo/runs.md#watsae-bm25rm3) | [WatSAE-BM25-RR](./misinfo/runs.md#watsae-bm25-rr) | [WatSMT-SD-S1](./misinfo/runs.md#watsmt-sd-s1) | [WatSMT-SD-S2](./misinfo/runs.md#watsmt-sd-s2)

??? abstract "Abstract"
	
	In this report, we discuss the experiments we conducted for the TREC 2021 Health Misinformation Track. For our manual runs, we used an improved version of our high-recall retrieval system [ 2] to manually search and judge documents. The system is built to efficiently retrieve the most-likely relevant documents based on a Continuous Active Learning (CAL) model and allows a speedy document assessment phase. Using the judged documents, we built CAL models to score documents that are part of our filtered collections. We also experimented with neural reranking methods based on question answering and stance detection methods to modify our CAL-based runs and a traditional BM25 run. For our automatic runs, we filtered the collection by running PageRank with a seed set of reliable domains and then using a text classifier and further refined the collection by including only medical web pages. We then ran traditional BM25 on this smaller and more reliable collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbualsaudGMZCST21.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbualsaudGMZCST21,
		author = {Mustafa Abualsaud and Kamyar Ghajar and Linh Nhi Phan Minh and Dake Zhang and Irene Xiangyi Chen and Mark D. Smucker and Amir Vakili Tahami},
		editor = {Ian Soboroff and Angela Ellis},
		title = {UWaterlooMDS at the {TREC} 2021 Health Misinformation Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UwaterlooMDS-HM.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbualsaudGMZCST21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CiTIUS at the TREC 2021 Health Misinformation Track

_Marcos Fernández-Pichel, Manuel de Prada Corral, David E. Losada, Juan Carlos Pichel, Pablo Gamallo_

- :fontawesome-solid-user-group: **Participant:** [CiTIUS](./misinfo/participants.md#citius)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CiTIUS-HM.pdf](https://trec.nist.gov/pubs/trec30/papers/CiTIUS-HM.pdf)
- :material-file-search: **Runs:** [citius.r1](./misinfo/runs.md#citius.r1) | [citius.r2](./misinfo/runs.md#citius.r2) | [citius.r3](./misinfo/runs.md#citius.r3) | [citius.r4](./misinfo/runs.md#citius.r4) | [citius.r5](./misinfo/runs.md#citius.r5) | [citius.r6](./misinfo/runs.md#citius.r6) | [citius.r9](./misinfo/runs.md#citius.r9) | [citius.r10](./misinfo/runs.md#citius.r10) | [citius.r7](./misinfo/runs.md#citius.r7) | [citius.r8](./misinfo/runs.md#citius.r8)

??? abstract "Abstract"
	
	The TREC Health Misinformation Track pursues the development of retrieval methods that promote credible and correct information over misinformation for health-related information needs. In this year, only the AdHoc Web Retrieval task was carried out. Its main goal was developing search technologies that promote credible and correct information over incorrect information. In these working notes, we present the CiTIUS team's multistage retrieval system for addressing this task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Fernandez-Pichel21.bib) "
	```
	@inproceedings{DBLP:conf/trec/Fernandez-Pichel21,
		author = {Marcos Fern{\'{a}}ndez{-}Pichel and Manuel de Prada Corral and David E. Losada and Juan Carlos Pichel and Pablo Gamallo},
		editor = {Ian Soboroff and Angela Ellis},
		title = {CiTIUS at the {TREC} 2021 Health Misinformation Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/CiTIUS-HM.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Fernandez-Pichel21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UPV at TREC Health Misinformation Track 2021 Ranking with SBERT  and Quality Estimators

_Ipek Baris Schlicht, Angel Felipe Magnossão de Paula, Paolo Rosso_

- :fontawesome-solid-user-group: **Participant:** [UPV](./misinfo/participants.md#upv)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UPV-HM.pdf](https://trec.nist.gov/pubs/trec30/papers/UPV-HM.pdf)
- :material-file-search: **Runs:** [upv_bm25](./misinfo/runs.md#upv_bm25) | [upv_fuse_2](./misinfo/runs.md#upv_fuse_2) | [upv_fuse_3](./misinfo/runs.md#upv_fuse_3) | [upv_fuse_4](./misinfo/runs.md#upv_fuse_4) | [upv_fuse_5](./misinfo/runs.md#upv_fuse_5) | [upv_fuse_6](./misinfo/runs.md#upv_fuse_6) | [upv_fuse_7](./misinfo/runs.md#upv_fuse_7) | [upv_fuse_8](./misinfo/runs.md#upv_fuse_8) | [upv_fuse_9](./misinfo/runs.md#upv_fuse_9) | [upv_fuse_10](./misinfo/runs.md#upv_fuse_10)

??? abstract "Abstract"
	
	Health misinformation on search engines is a significant problem that could negatively affect individuals or public health. To mitigate the problem, TREC organizes a health misinformation track. This paper presents our sub- missions to this track. We use a BM25 and a domain-specific semantic search engine for retrieving initial documents. Later, we examine a health news schema for quality assessment and apply it to re-rank documents. Finally, we merge the scores from the different components by using reciprocal rank fusion. Finally, we discuss the results and conclude with future works.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchlichtPR21.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchlichtPR21,
		author = {Ipek Baris Schlicht and Angel Felipe Magnoss{\~{a}}o de Paula and Paolo Rosso},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{UPV} at {TREC} Health Misinformation Track 2021 Ranking with {SBERT} and Quality Estimators},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/UPV-HM.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SchlichtPR21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DS4DH at TREC Health Misinformation 2021: Multi-Dimensional Ranking  Models with Transfer Learning and Rank Fusion

_Boya Zhang, Nona Naderi, Fernando Jaume-Santero, Douglas Teodoro_

- :fontawesome-solid-user-group: **Participant:** [DigiLab](./misinfo/participants.md#digilab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/DigiLab-HM.pdf](https://trec.nist.gov/pubs/trec30/papers/DigiLab-HM.pdf)
- :material-file-search: **Runs:** [bow_sup_cred](./misinfo/runs.md#bow_sup_cred) | [mlm_sup_cred](./misinfo/runs.md#mlm_sup_cred) | [lin_use_sup_rf](./misinfo/runs.md#lin_use_sup_rf) | [all_use_sup_cre](./misinfo/runs.md#all_use_sup_cre) | [use_sup_cred](./misinfo/runs.md#use_sup_cred) | [use_rob_cred](./misinfo/runs.md#use_rob_cred) | [bm25_rob_rf](./misinfo/runs.md#bm25_rob_rf)

??? abstract "Abstract"
	
	This paper describes the work of the Data Science for Digital Health (DS4DH) group at the TREC Health Misinformation Track 2021. The TREC Health Misinformation track focused on the development of retrieval methods that provide relevant, correct and credible information for health related searches on the Web. In our methodology, we used a two-step ranking approach that includes i) a standard retrieval phase, based on BM25 model, and ii) a reranking phase, with a pipeline of models focused on the usefulness, supportiveness and credibility dimensions of the retrieved documents. To estimate the usefulness, we classified the initial rank list using pre-trained language models based on the transformers architecture fine-tuned on the MS MARCO corpus. To assess the supportiveness, we utilized BERT-based models fine-tuned on scientific and Wikipedia corpora. Finally, to evaluated the credibility of the documents, we employed a random forest model trained on the Microsoft Credibility dataset combined with a list of credible sites. The resulting ranked lists were then combined using the Reciprocal Rank Fusion algorithm to obtain the final list of useful, supporting and credible documents. Our approach achieved competitive results, being top-2 in the compatibility measurement for the automatic runs. Our findings suggest that integrating automatic ranking models created for each information quality dimension with transfer learning can increase the effectiveness of health-related information retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangNJT21.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangNJT21,
		author = {Boya Zhang and Nona Naderi and Fernando Jaume{-}Santero and Douglas Teodoro},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{DS4DH} at {TREC} Health Misinformation 2021: Multi-Dimensional Ranking Models with Transfer Learning and Rank Fusion},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/DigiLab-HM.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangNJT21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Podcast 

#### TREC 2021 Podcasts Track Overview

_Jussi Karlgren, Rosie Jones, Ben Carterette, Ann Clifton, Edgar Tanaka, Maria Eskevich, Gareth J. F. Jones, Sravana Reddy_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Overview-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/Overview-Pod.pdf)
??? abstract "Abstract"
	
	The TREC Podcasts Track is intended to facilitate research in language technologies applied to podcasts specifically by lowering the barrier-to-entry for data-oriented research for podcasts and for diverse spoken documents in general. This year, 2021, is the second year of the track. A more general overview of some of the challenges is given in last year's Podcasts Track Overview. The track this year consisted of two shared tasks: segment retrieval and summarisation, both based on a dataset of over 100,000 podcast episodes (metadata, audio, and automatic transcripts) which was released concurrently with the track. The tasks were slightly elaborated this year to encourage participants to use audio analysis. This paper gives an overview of the tasks and the results of the participants' experiments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KarlgrenJCCTEJR21.bib) "
	```
	@inproceedings{DBLP:conf/trec/KarlgrenJCCTEJR21,
		author = {Jussi Karlgren and Rosie Jones and Ben Carterette and Ann Clifton and Edgar Tanaka and Maria Eskevich and Gareth J. F. Jones and Sravana Reddy},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TREC} 2021 Podcasts Track Overview},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Overview-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/KarlgrenJCCTEJR21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2021: Deep Learning, Health Misinformation, and Podcasts  Tracks

_Alexander Bondarenko, Maik Fröbe, Sebastian Günther, Matthias Hagen, Marcel Gohsen, Johannes Kiesel, Michael Völske, Benno Stein, Jakob Schwerter, Shahbaz Syed, Martin Potthast_

- :fontawesome-solid-user-group: **Participant:** [Webis](./podcast/participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf)
- :material-file-search: **Runs:** [Webis_pc_bs](./podcast/runs.md#webis_pc_bs) | [Webis_pc_cola](./podcast/runs.md#webis_pc_cola) | [Webis_pc_rob](./podcast/runs.md#webis_pc_rob) | [Webis_pc_co_rob](./podcast/runs.md#webis_pc_co_rob) | [Webis_pc_extr](./podcast/runs.md#webis_pc_extr) | [Webis_pc_abstr](./podcast/runs.md#webis_pc_abstr)

??? abstract "Abstract"
	
	We describe the Webis group's participation in the TREC 2021 Deep Learning, Health Misinformation, and Podcasts tracks. Our three LambdaMART-based runs submitted to the Deep Learning track focus on the question whether anchor text is an effective retrieval feature in the MS MARCO scenario. In the Health Misinformation track, we axiomatically re-ranked the top-20 results of BM25 and MonoT5 for argumentative topics. As for the Podcasts track, our submitted six runs focus on supervised classification of podcasts as entertaining, subjective, or containing discussion by using audio and text embeddings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001F0HGKV0SSP21.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001F0HGKV0SSP21,
		author = {Alexander Bondarenko and Maik Fr{\"{o}}be and Sebastian G{\"{u}}nther and Matthias Hagen and Marcel Gohsen and Johannes Kiesel and Michael V{\"{o}}lske and Benno Stein and Jakob Schwerter and Shahbaz Syed and Martin Potthast},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Webis at {TREC} 2021: Deep Learning, Health Misinformation, and Podcasts Tracks},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 17:23:07 +0200},
		biburl = {https://dblp.org/rec/conf/trec/0001F0HGKV0SSP21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TU Wien at TREC DL and Podcast 2021: Simple Compression for  Dense Retrieval

_Sebastian Hofstätter, Mete Sertkan, Allan Hanbury_

- :fontawesome-solid-user-group: **Participant:** [TU_Vienna](./podcast/participants.md#tu_vienna)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/TU_Vienna-DL-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/TU_Vienna-DL-Pod.pdf)
- :material-file-search: **Runs:** [TUW_hybrid_ws](./podcast/runs.md#tuw_hybrid_ws) | [TUW_hybrid_cat](./podcast/runs.md#tuw_hybrid_cat) | [TUW_tasb_cat](./podcast/runs.md#tuw_tasb_cat) | [TUW_tasb192_ann](./podcast/runs.md#tuw_tasb192_ann)

??? abstract "Abstract"
	
	The IR group of TU Wien participated in two tracks at TREC 2021: Deep Learning and Podcast segment retrieval. We continued our focus from our previous TREC participations on efficient approaches for retrieval and re-ranking. We propose a simple training process for compressing a dense retrieval model's output. First, we train it with full capacity, and then add a compression, or dimensionality reduction, layer on top and conduct a second full training pass. At TREC 2021 we test this model in a blind evaluation and zero-shot collection transfer for both Deep Learning and Podcast tracks. For our participation at the Podcast segment retrieval track, we also employ hybrid sparse-dense retrieval. Furthermore, we utilize auxiliary information to re-rank the retrieved segments by entertainment and subjectivity signals. Our results show that our simple compression procedure with approximate nearest neighbor search achieves comparable in-domain results (minus 2 points nDCG@10 difference) to a full TAS-Balanced retriever and reasonable effectiveness in a zero-shot domain transfer (Podcast track), where we outperform BM25 by 6 points nDCG@10.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HofstatterSH21.bib) "
	```
	@inproceedings{DBLP:conf/trec/HofstatterSH21,
		author = {Sebastian Hofst{\"{a}}tter and Mete Sertkan and Allan Hanbury},
		editor = {Ian Soboroff and Angela Ellis},
		title = {{TU} Wien at {TREC} {DL} and Podcast 2021: Simple Compression for Dense Retrieval},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/TU\_Vienna-DL-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HofstatterSH21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Multilingual Podcast Summarization using Longformers

_Edgar Tanaka, Ann Clifton, Md. Iftekhar Tanveer_

- :fontawesome-solid-user-group: **Participant:** [Unicamp](./podcast/participants.md#unicamp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Unicamp-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/Unicamp-Pod.pdf)
- :material-file-search: **Runs:** [Unicamp1](./podcast/runs.md#unicamp1) | [Unicamp2](./podcast/runs.md#unicamp2)

??? abstract "Abstract"
	
	Most literature on automated summarization, including podcast summarization, has been restricted to the English language. At the same time, podcasts are now an important form of media in many countries and in many languages and therefore, it is crucial that we expand the problem of podcast summarization to a wider range of languages. In this work, we explore the application of multilingual models to the task of summarizing podcasts in English and Portuguese. We compare various training scenarios including adapting a Longformer encoder, cross-lingual and cross-task transfer learning and we demonstrate that a unified model fine-tuned to multilingual data can perform on par with dedicated models that are fine-tuned monolingually. As a result, our models significantly outperform the TREC baseline based on the first minute of each episode.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TanakaCT21.bib) "
	```
	@inproceedings{DBLP:conf/trec/TanakaCT21,
		author = {Edgar Tanaka and Ann Clifton and Md. Iftekhar Tanveer},
		editor = {Ian Soboroff and Angela Ellis},
		title = {Multilingual Podcast Summarization using Longformers},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/Unicamp-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/TanakaCT21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PoliTO at TREC 2021 Podcast Summarization Track

_Lorenzo Vaiani, Moreno La Quatra, Luca Cagliero, Paolo Garza_

- :fontawesome-solid-user-group: **Participant:** [PoliTO](./podcast/participants.md#polito)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/PoliTO-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/PoliTO-Pod.pdf)
- :material-file-search: **Runs:** [PoliTO_50_32-128](./podcast/runs.md#polito_50_32-128) | [PoliTO_25_32-128](./podcast/runs.md#polito_25_32-128) | [PoliTO_100_32-128](./podcast/runs.md#polito_100_32-128) | [PoliTO_50_64-128](./podcast/runs.md#polito_50_64-128)

??? abstract "Abstract"
	
	This paper presents the approach proposed by the PoliTO team to accomplish the TREC 2021 podcast summarization task. The purpose is to extract synchronized text/audio segments that convey the most relevant podcast information. The main challenge is to consider is the multimodal nature of the data source, which comprises both textual and acoustic sequences. PoliTO presents a two-stage pipeline that (i) extracts relevant content from multimodal sources and (ii) leverages the extracted content to generate abstractive summaries by using an attention-based Deep Learning architecture. The extractive stage combines the high-dimensional encodings of both textual and audio sources to build a neural network-based regression model. The key idea is to predict the textual similarity between the selected text snippets and the podcast description by also exploiting the underlying information provided by the acoustic features. While audio summaries are obtained by concatenating selected audio samples, summaries in textual form are generated by exploiting the selected information as input of a sequence-to-sequence generative model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VaianiQCG21.bib) "
	```
	@inproceedings{DBLP:conf/trec/VaianiQCG21,
		author = {Lorenzo Vaiani and Moreno La Quatra and Luca Cagliero and Paolo Garza},
		editor = {Ian Soboroff and Angela Ellis},
		title = {PoliTO at {TREC} 2021 Podcast Summarization Track},
		booktitle = {Proceedings of the Thirtieth Text REtrieval Conference, {TREC} 2021, online, November 15-19, 2021},
		series = {{NIST} Special Publication},
		volume = {500-335},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2021},
		url = {https://trec.nist.gov/pubs/trec30/papers/PoliTO-Pod.pdf},
		timestamp = {Mon, 28 Aug 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/VaianiQCG21.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

