# Proceedings - Common Core 2017 

#### TREC 2017 Common Core Track Overview

_James Allan, Donna Harman, Evangelos Kanoulas, Dan Li, Christophe Van Gysel, Ellen M. Voorhees_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-CC.pdf)
??? abstract "Abstract"
	
	The primary goal of the TREC Common Core track is three-fold: (a) bring the information retrieval community back into a traditional ad-hoc search task; (b) attract a diverse set of participating runs and build a new test collections using more recently created documents; (c) establish a (new) test collection construction methodology that avoids the pitfalls of depth-k pooling. A number of side-goals are also set, including studying the shortcomings of test collections constructed in the past; experimenting with new ideas for constructing test collections; expand test collections by new participant tasks (ad-hoc/interactive), new relevance judgments (binary/multilevel), new pooling methods, new assessment resources (NIST/crowd-sourcing) and new retrieval systems contributing documents (manual/neural/strong baselines).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AllanHKLGV17.bib) "
	```
	@inproceedings{DBLP:conf/trec/AllanHKLGV17,
		author = {James Allan and Donna Harman and Evangelos Kanoulas and Dan Li and Christophe Van Gysel and Ellen M. Voorhees},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2017 Common Core Track Overview},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-CC.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AllanHKLGV17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2017 Common Core Track

_Qingyao Ai, Hamed Zamani, Stephen M. Harding, Shahrzad Naseri, James Allan, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [UMass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UMass-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/UMass-CC.pdf)
- :material-file-search: **Runs:** [umass_direlmnvs](./runs.md#umass_direlmnvs) | [umass_direlm](./runs.md#umass_direlm) | [umass_diremart](./runs.md#umass_diremart) | [umass_maxpas50](./runs.md#umass_maxpas50) | [umass_maxpas150](./runs.md#umass_maxpas150) | [umass_letor_lm](./runs.md#umass_letor_lm) | [umass_letor_m](./runs.md#umass_letor_m) | [umass_emb1](./runs.md#umass_emb1) | [umass_erm](./runs.md#umass_erm) | [umass_letor_lmn](./runs.md#umass_letor_lmn)

??? abstract "Abstract"
	
	This is an overview of University of Massachusetts efforts in providing document retrieval run submissions for the TREC Common Core Track with the goal of using newly developed techniques in retrieval and ranking to provide many new documents for relevance judgments. It is hoped these new techniques will reveal new documents not seen via traditional techniques, that will increase the numbers of relevant judged documents for the research collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AiZHNAC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/AiZHNAC17,
		author = {Qingyao Ai and Hamed Zamani and Stephen M. Harding and Shahrzad Naseri and James Allan and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UMass at {TREC} 2017 Common Core Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UMass-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AiZHNAC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at the 2017 TREC CORE Track

_Rodger Benham, Luke Gallagher, Joel M. Mackenzie, Tadele Tedla Damessie, Ruey-Cheng Chen, Falk Scholer, Alistair Moffat, J. Shane Culpepper_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/RMIT-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/RMIT-CC.pdf)
- :material-file-search: **Runs:** [RMITRBCUQVT5M1](./runs.md#rmitrbcuqvt5m1) | [RMITUQVBestM2](./runs.md#rmituqvbestm2) | [RMITFDMQEA1](./runs.md#rmitfdmqea1)

??? abstract "Abstract"
	
	The TREC 2017 CORE Track1 is a re-run of the classic TREC ad hoc search evaluation campaign, with the vision of establishing new methodologies for creating IR test collections. The previous TREC newswire ad hoc task was the 2004 Robust Track, where the emphasis was on improving the effectiveness of poorly performing topics in previous tracks [16]. The TREC CORE 2017 track reuses the Robust 2004 topic set, for the development of relevance judgments over a new New York Times corpus, composed of newswire articles published between 1987 and 2007. In this track, our interest is driven by two related lines of research: efficient multi-stage retrieval [3-7,9,14], where it is believed that improving recall in early stage retrieval can improve end-to-end- effectiveness; and more reliable deep evaluation when using shallow judgments [8,10-13]. By participating in CORE, we aempted to develop a recall-oriented approach that exploits user query variations and rank fusion. We venture that, in an evaluation campaign such as the TREC CORE Track, which typically aracts runs of a high effectiveness caliber from research groups worldwide, the ability to retrieve a large number of relevant documents that other systems fail to find is indicative of a high-recall system. A useful consequence of this approach is the ability to compare query variation phenomena across corpora. The UQV100 test collection contains one hundred single-faceted topics with over five thousand unique query variations [1], but to date has only judgments against the ClueWeb12B collection. The variation- rich collection produced for participation in the CORE track, while smaller in scope than the UQV100 collection, now enables comparisons of query variations to be made across different docu- ment representations and editorial quality. Observing the relative effectiveness across ClueWeb12B and Robust04, one consisting of websites, and the other composed of journalistic content, is of considerable interest, as is the question of the benefit of rank fusion mechanisms based on those variations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BenhamGMDCSMC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/BenhamGMDCSMC17,
		author = {Rodger Benham and Luke Gallagher and Joel M. Mackenzie and Tadele Tedla Damessie and Ruey{-}Cheng Chen and Falk Scholer and Alistair Moffat and J. Shane Culpepper},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{RMIT} at the 2017 {TREC} {CORE} Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/RMIT-CC.pdf},
		timestamp = {Mon, 26 Apr 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BenhamGMDCSMC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at TREC 2017 Common Core Track

_Xu Chang, Liying Jiao, Jinlong Liu, Weijian Zhu, Yuanhai Xue, Li Zha, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ICTNET-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/ICTNET-CC.pdf)
- :material-file-search: **Runs:** [ICT17ZCJL01](./runs.md#ict17zcjl01) | [ICT17ZCJL02](./runs.md#ict17zcjl02) | [ICT17ZCJL03](./runs.md#ict17zcjl03) | [ICT17ZCJL05](./runs.md#ict17zcjl05) | [ICT17ZCJL06](./runs.md#ict17zcjl06) | [ICT17ZCJL07](./runs.md#ict17zcjl07)

??? abstract "Abstract"
	
	The common core track is a new track for TREC 2017. The track will serve as a common task for a wide spectrum of IR researchers, thus attracting a diverse run set that can be used to investigate new methodologies for test collection construction. This track provides the structured NYTimes corpus. Its primary goal is to get the relative documents from the corpus with the given topics, and there are 1855660 news across from 1987 to 2007 on NYTimes in this common core track. Two sets of topics are used for searching relative News, one of which is to be judged by NIST and crowd workers and the other is to be judged by crowd workers only. Participants need choose the first or the both topics according to the requirements. There are three common text information retrieval model: Vector Space Model, Probabilistic Model and Inference Network Model. BM25 is a probabilistic function to rank the list of matched documents according to a given query[4]. Solr uses the BM25 rank function when doing the search work. It is an open source enterprise search platform and can do the full-text search work. Solr runs in the servlet container. User can get the results from the web interface. In our work, we choose Solr as the tool for indexing documents and searching topics. We have an exploration on the topics, which are distributed by the NIST. Most of the topics contain less than three words and some include even one word. Therefore, we need to expand the query words to query more information. We select the apache Solr[5] as our retrieve frame in order to improve the effectiveness on the automatic query expansion. Recently, neural network is widely used in NLP. We use the word-embedding model for automatic query expansion and the TextRank algorithm with the description of the topic to extract the keywords as the expansion words. Next, we build index for the corpus and get the query results with Solr.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChangJLZXZLC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChangJLZXZLC17,
		author = {Xu Chang and Liying Jiao and Jinlong Liu and Weijian Zhu and Yuanhai Xue and Li Zha and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at {TREC} 2017 Common Core Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/ICTNET-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChangJLZXZLC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IMS @ TREC 2017 Core Track

_Nicola Ferro_

- :fontawesome-solid-user-group: **Participant:** [ims-core](./participants.md#ims-core)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ims-core-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/ims-core-CC.pdf)
- :material-file-search: **Runs:** [ims_wcmbsum_ap](./runs.md#ims_wcmbsum_ap) | [ims_cmbsum](./runs.md#ims_cmbsum) | [ims_wcs_ap_uf](./runs.md#ims_wcs_ap_uf) | [ims_wcs_p10](./runs.md#ims_wcs_p10) | [ims_wcs_ndcg](./runs.md#ims_wcs_ndcg) | [ims_wcs_twist](./runs.md#ims_wcs_twist) | [ims_wcs_rbp](./runs.md#ims_wcs_rbp) | [ims_wcs_err](./runs.md#ims_wcs_err) | [ims_wcs_recall](./runs.md#ims_wcs_recall) | [ims_wcs_rprec](./runs.md#ims_wcs_rprec)

??? abstract "Abstract"
	
	We report our participation to the TREC 2017 Core Track. Our objective is to systematically investigate the use of weak baselines, namely off-the-shelf open source IR systems, and understand how they compare with respect to TREC state-of-the-art ones. We are also interested in understanding how IR components - namely stop lists, stemmers/n-grams, and IR models - contribute to the overall performances and, specifically, to the pools.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Ferro17.bib) "
	```
	@inproceedings{DBLP:conf/trec/Ferro17,
		author = {Nicola Ferro},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{IMS} @ {TREC} 2017 Core Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/ims-core-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Ferro17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MRG_UWaterloo and WaterlooCormack Participation in the TREC 2017  Common Core Track

_Maura R. Grossman, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [MRG_UWaterloo](./participants.md#mrg_uwaterloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/MRG_UWaterloo-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/MRG_UWaterloo-CC.pdf)
- :material-file-search: **Runs:** [MRGrankrel](./runs.md#mrgrankrel) | [MRGrandrel](./runs.md#mrgrandrel) | [MRGrankall](./runs.md#mrgrankall)

??? abstract "Abstract"
	
	The MRG_UWaterloo group from the University of Waterloo used a Continuous Active Learning (“CAL”) approach [1] to identify and manually review a substantial fraction of the relevant documents for each of the 250 Common Core topics. Our primary goal was to create, with less effort, a set of relevance assessments (“qrels”) comparable to the official Common Core Track qrels (cf. [12, 2]). To this end, we adapted for live, human-in-the-loop use, the AutoTAR CAL implementation,1 which had demonstrated superior effectiveness as a baseline for the TREC 2015 and 2016 Total Recall Tracks [9, 5]. In total, for 250 topics, the authors spent 64.1 hours assessing 42,587 documents (on average, 15.4 mins/topic; 5.4 secs/doc), judging 30,124 of them to be relevant (70.7%). [...] The WaterlooCormack submission consisted of “automatic routing” runs, as defined in TRECs 1 through 8 [7]. Document rankings were derived using logistic regression on prior relevance assessments for the same topics (but with respect to different corpora), without manual intervention. Feature engineering, learning software, and parameter settings were identical to those used in the TREC 2015 and 2016 Total Recall Tracks [9, 5], and identical to those used by the MRG_UWaterloo group. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanC17,
		author = {Maura R. Grossman and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {MRG{\_}UWaterloo and WaterlooCormack Participation in the {TREC} 2017 Common Core Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/MRG\_UWaterloo-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MRG_UWaterloo and WaterlooCormack Participation in the TREC 2017  Common Core Track

_Maura R. Grossman, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [WaterlooCormack](./participants.md#waterloocormack)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/WaterlooCormack-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/WaterlooCormack-CC.pdf)
- :material-file-search: **Runs:** [WCrobust04](./runs.md#wcrobust04) | [WCrobust0405](./runs.md#wcrobust0405) | [WCrobust04W](./runs.md#wcrobust04w)

??? abstract "Abstract"
	
	The MRG_UWaterloo group from the University of Waterloo used a Continuous Active Learning (“CAL”) approach [1] to identify and manually review a substantial fraction of the relevant documents for each of the 250 Common Core topics. Our primary goal was to create, with less effort, a set of relevance assessments (“qrels”) comparable to the official Common Core Track qrels (cf. [12, 2]). To this end, we adapted for live, human-in-the-loop use, the AutoTAR CAL implementation,1 which had demonstrated superior effectiveness as a baseline for the TREC 2015 and 2016 Total Recall Tracks [9, 5]. In total, for 250 topics, the authors spent 64.1 hours assessing 42,587 documents (on average, 15.4 mins/topic; 5.4 secs/doc), judging 30,124 of them to be relevant (70.7%). [...] The WaterlooCormack submission consisted of “automatic routing” runs, as defined in TRECs 1 through 8 [7]. Document rankings were derived using logistic regression on prior relevance assessments for the same topics (but with respect to different corpora), without manual intervention. Feature engineering, learning software, and parameter settings were identical to those used in the TREC 2015 and 2016 Total Recall Tracks [9, 5], and identical to those used by the MRG_UWaterloo group. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanC17a.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanC17a,
		author = {Maura R. Grossman and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {MRG{\_}UWaterloo and WaterlooCormack Participation in the {TREC} 2017 Common Core Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/WaterlooCormack-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanC17a.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ILPS at TREC 2017 Common Core Track

_Christophe Van Gysel, Dan Li, Evangelos Kanoulas_

- :fontawesome-solid-user-group: **Participant:** [UvA.ILPS](./participants.md#uva.ilps)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ILPS-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/ILPS-CC.pdf)
- :material-file-search: **Runs:** [IlpsUvAQlmNvsm](./runs.md#ilpsuvaqlmnvsm) | [IlpsUvANvsm](./runs.md#ilpsuvanvsm) | [IlpsUvABoir](./runs.md#ilpsuvaboir)

??? abstract "Abstract"
	
	The TREC 2017 Common Core Track aimed at gathering a diverse set of participating runs and building a new test collection using advanced pooling methods. In this paper, we describe the participation of the IlpsUvA team at the TREC 2017 Common Core Track. We submitted runs created using two methods to the track: (1) BOIR uses Bayesian optimization to automatically optimize retrieval model hyperparameters. (2) NVSM is a latent vector space model where representations of documents and query terms are learned from scratch in an unsupervised manner. We find that BOIR is able to optimize hyperparameters as to find a system that performs competitively amongst track participants. NVSM provides rankings that are diverse, as it was amongst the top automated unsupervised runs that provided the most unique relevant documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GyselLK17.bib) "
	```
	@inproceedings{DBLP:conf/trec/GyselLK17,
		author = {Christophe Van Gysel and Dan Li and Evangelos Kanoulas},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ILPS} at {TREC} 2017 Common Core Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/ILPS-CC.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GyselLK17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2017: Open Search and Core Tracks

_Matthias Hagen, Yamen Ajjour, Johannes Kiesel, Payam Adineh, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Webis-O-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/Webis-O-CC.pdf)
- :material-file-search: **Runs:** [webis_baseline](./runs.md#webis_baseline) | [webis_baseline2](./runs.md#webis_baseline2) | [webis_reranked](./runs.md#webis_reranked) | [webis_reranked2](./runs.md#webis_reranked2)

??? abstract "Abstract"
	
	We give a brief overview of the Webis group's participation in the TREC 2017 Open Search and Core tracks. Our submission to the Open Search track is similar to our last year's approach, we axiomatically re-rank a BM25-ordered result list to come up with a final ranking. The axiomatic re-ranking idea is also applied in our Core track contribution but with an emphasis on argumentativeness as a not-yet-covered aspect in retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenAKAS17.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenAKAS17,
		author = {Matthias Hagen and Yamen Ajjour and Johannes Kiesel and Payam Adineh and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2017: Open Search and Core Tracks},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Webis-O-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenAKAS17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Tarragon Consulting at TREC 2017: Common Core Track

_Richard M. Tong_

- :fontawesome-solid-user-group: **Participant:** [tgncorp](./participants.md#tgncorp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/tgncorp-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/tgncorp-CC.pdf)
- :material-file-search: **Runs:** [tgncorpBASE](./runs.md#tgncorpbase) | [tgncorpBOOST](./runs.md#tgncorpboost)

??? abstract "Abstract"
	
	Tarragon Consulting Corporation (henceforth Tarragon) contributed two runs to the new Common Core track. Both were manual runs using the NIST judged topics. Both used Solr as the base search engine with the queries semi-automatically constructed from the Topic descriptions and augmented with information from Wordnet and Wikipedia. Results are generally below the published median scores but for several topics our results are very competitive. And we did contribute a significant number of “unique relevant” documents to the judged pool.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tong17.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tong17,
		author = {Richard M. Tong},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Tarragon Consulting at {TREC} 2017: Common Core Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/tgncorp-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tong17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluating Axiomatic Retrieval Models in the Core Track

_Yue Wang, Peilin Yang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/udel_fang-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/udel_fang-CC.pdf)
- :material-file-search: **Runs:** [UDelInfoLOGext](./runs.md#udelinfologext) | [UDelInfoLOGint](./runs.md#udelinfologint) | [UDelInfoEXPint](./runs.md#udelinfoexpint)

??? abstract "Abstract"
	
	Axiomatic analysis of the existing retrieval models have shown great power on understanding the retrieval models, which further shows a great opportunities on improve the retrieval performances of existing models. In this work, we tested the axiomatic retrieval models with query expansion on the newly provided data collection. The results show that the proposed method could outperform the baseline methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangY017.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangY017,
		author = {Yue Wang and Peilin Yang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Evaluating Axiomatic Retrieval Models in the Core Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/udel\_fang-CC.pdf},
		timestamp = {Thu, 17 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/WangY017.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UWaterlooMDS at the TREC 2017 Common Core Track

_Haotian Zhang, Mustafa Abualsaud, Nimesh Ghelani, Angshuman Ghosh, Mark D. Smucker, Gordon V. Cormack, Maura R. Grossman_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UWaterlooMDS-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/UWaterlooMDS-CC.pdf)
- :material-file-search: **Runs:** [UWatMDS_TARSv1](./runs.md#uwatmds_tarsv1) | [UWatMDS_HT10](./runs.md#uwatmds_ht10) | [UWatMDS_TARSv2](./runs.md#uwatmds_tarsv2) | [UWatMDS_ustudy](./runs.md#uwatmds_ustudy) | [UWatMDS_BUnion](./runs.md#uwatmds_bunion) | [UWatMDS_BFuse](./runs.md#uwatmds_bfuse) | [UWatMDS_AUnion](./runs.md#uwatmds_aunion) | [UWatMDS_AFuse](./runs.md#uwatmds_afuse) | [UWatMDS_AWgtd](./runs.md#uwatmds_awgtd) | [UWatMDS_BWgtd](./runs.md#uwatmds_bwgtd)

??? abstract "Abstract"
	
	In this report, we discuss the experiments we conducted for the TREC 2017 Common Core Track. We implemented a High-Recall retrieval system for assessors to efficiently find relevant documents within a limited period of time. The system consists of an AutoTAR Continuous Active Learning (CAL) system based on paragraph/document level relevance feedback. The system also includes a search engine where users can repeatedly enter their own queries to find relevant documents. For the first round of submissions, we used our system to judge 32,172 documents across 250 topics. The system's trained model of relevance was used to rank all unjudged documents. After each judgment, our system can retrain the machine learning model and rank the whole collection while maintaining interactive performance without any user discernible lag. For the second round of submissions, we crafted a user study to measure the impact of interaction mechanisms on technology assisted review and completed an initial version of the study with 10 users and 50 topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangAGGSCG17.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangAGGSCG17,
		author = {Haotian Zhang and Mustafa Abualsaud and Nimesh Ghelani and Angshuman Ghosh and Mark D. Smucker and Gordon V. Cormack and Maura R. Grossman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UWaterlooMDS at the {TREC} 2017 Common Core Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UWaterlooMDS-CC.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangAGGSCG17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

