# Proceedings - Health Misinformation 2021 

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

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf](https://trec.nist.gov/pubs/trec30/papers/Webis-DL-HM-Pod.pdf)
- :material-file-search: **Runs:** [webis-bm25](./runs.md#webis-bm25) | [webis-t5](./runs.md#webis-t5) | [webis-bm25-ax1](./runs.md#webis-bm25-ax1) | [webis-bm25-ax3](./runs.md#webis-bm25-ax3) | [webis-t5-ax1](./runs.md#webis-t5-ax1) | [webis-t5-ax3](./runs.md#webis-t5-ax3)

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

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UwaterlooMDS-HM.pdf](https://trec.nist.gov/pubs/trec30/papers/UwaterlooMDS-HM.pdf)
- :material-file-search: **Runs:** [WatSAM-BM25](./runs.md#watsam-bm25) | [WatSMM-CAL](./runs.md#watsmm-cal) | [WatSMC-CAL](./runs.md#watsmc-cal) | [WatSMM-CALHC](./runs.md#watsmm-calhc) | [WatSMM-CALPR](./runs.md#watsmm-calpr) | [WatSMM-Fused](./runs.md#watsmm-fused) | [WatSMM-CALQA100](./runs.md#watsmm-calqa100) | [WatSMM-CALQAAll](./runs.md#watsmm-calqaall) | [WatSMC-CALQA100](./runs.md#watsmc-calqa100) | [WatSMC-CALQAAll](./runs.md#watsmc-calqaall) | [WatSMC-CALQAHC1](./runs.md#watsmc-calqahc1) | [WatSMC-CALQAHC2](./runs.md#watsmc-calqahc2) | [WatSMC-Correct](./runs.md#watsmc-correct) | [baselineBM25](./runs.md#baselinebm25) | [WatSAE-BM25](./runs.md#watsae-bm25) | [WatSAE-BM25RM3](./runs.md#watsae-bm25rm3) | [WatSAE-BM25-RR](./runs.md#watsae-bm25-rr) | [WatSMT-SD-S1](./runs.md#watsmt-sd-s1) | [WatSMT-SD-S2](./runs.md#watsmt-sd-s2)

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

- :fontawesome-solid-user-group: **Participant:** [CiTIUS](./participants.md#citius)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/CiTIUS-HM.pdf](https://trec.nist.gov/pubs/trec30/papers/CiTIUS-HM.pdf)
- :material-file-search: **Runs:** [citius.r1](./runs.md#citius.r1) | [citius.r2](./runs.md#citius.r2) | [citius.r3](./runs.md#citius.r3) | [citius.r4](./runs.md#citius.r4) | [citius.r5](./runs.md#citius.r5) | [citius.r6](./runs.md#citius.r6) | [citius.r9](./runs.md#citius.r9) | [citius.r10](./runs.md#citius.r10) | [citius.r7](./runs.md#citius.r7) | [citius.r8](./runs.md#citius.r8)

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

- :fontawesome-solid-user-group: **Participant:** [UPV](./participants.md#upv)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/UPV-HM.pdf](https://trec.nist.gov/pubs/trec30/papers/UPV-HM.pdf)
- :material-file-search: **Runs:** [upv_bm25](./runs.md#upv_bm25) | [upv_fuse_2](./runs.md#upv_fuse_2) | [upv_fuse_3](./runs.md#upv_fuse_3) | [upv_fuse_4](./runs.md#upv_fuse_4) | [upv_fuse_5](./runs.md#upv_fuse_5) | [upv_fuse_6](./runs.md#upv_fuse_6) | [upv_fuse_7](./runs.md#upv_fuse_7) | [upv_fuse_8](./runs.md#upv_fuse_8) | [upv_fuse_9](./runs.md#upv_fuse_9) | [upv_fuse_10](./runs.md#upv_fuse_10)

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

- :fontawesome-solid-user-group: **Participant:** [DigiLab](./participants.md#digilab)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec30/papers/DigiLab-HM.pdf](https://trec.nist.gov/pubs/trec30/papers/DigiLab-HM.pdf)
- :material-file-search: **Runs:** [bow_sup_cred](./runs.md#bow_sup_cred) | [mlm_sup_cred](./runs.md#mlm_sup_cred) | [lin_use_sup_rf](./runs.md#lin_use_sup_rf) | [all_use_sup_cre](./runs.md#all_use_sup_cre) | [use_sup_cred](./runs.md#use_sup_cred) | [use_rob_cred](./runs.md#use_rob_cred) | [bm25_rob_rf](./runs.md#bm25_rob_rf)

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

