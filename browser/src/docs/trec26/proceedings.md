# Proceedings 2017 

## Common Core 

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

- :fontawesome-solid-user-group: **Participant:** [UMass](./core/participants.md#umass)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UMass-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/UMass-CC.pdf)
- :material-file-search: **Runs:** [umass_direlmnvs](./core/runs.md#umass_direlmnvs) | [umass_direlm](./core/runs.md#umass_direlm) | [umass_diremart](./core/runs.md#umass_diremart) | [umass_maxpas50](./core/runs.md#umass_maxpas50) | [umass_maxpas150](./core/runs.md#umass_maxpas150) | [umass_letor_lm](./core/runs.md#umass_letor_lm) | [umass_letor_m](./core/runs.md#umass_letor_m) | [umass_emb1](./core/runs.md#umass_emb1) | [umass_erm](./core/runs.md#umass_erm) | [umass_letor_lmn](./core/runs.md#umass_letor_lmn)

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

- :fontawesome-solid-user-group: **Participant:** [RMIT](./core/participants.md#rmit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/RMIT-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/RMIT-CC.pdf)
- :material-file-search: **Runs:** [RMITRBCUQVT5M1](./core/runs.md#rmitrbcuqvt5m1) | [RMITUQVBestM2](./core/runs.md#rmituqvbestm2) | [RMITFDMQEA1](./core/runs.md#rmitfdmqea1)

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

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./core/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ICTNET-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/ICTNET-CC.pdf)
- :material-file-search: **Runs:** [ICT17ZCJL01](./core/runs.md#ict17zcjl01) | [ICT17ZCJL02](./core/runs.md#ict17zcjl02) | [ICT17ZCJL03](./core/runs.md#ict17zcjl03) | [ICT17ZCJL05](./core/runs.md#ict17zcjl05) | [ICT17ZCJL06](./core/runs.md#ict17zcjl06) | [ICT17ZCJL07](./core/runs.md#ict17zcjl07)

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

- :fontawesome-solid-user-group: **Participant:** [ims-core](./core/participants.md#ims-core)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ims-core-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/ims-core-CC.pdf)
- :material-file-search: **Runs:** [ims_wcmbsum_ap](./core/runs.md#ims_wcmbsum_ap) | [ims_cmbsum](./core/runs.md#ims_cmbsum) | [ims_wcs_ap_uf](./core/runs.md#ims_wcs_ap_uf) | [ims_wcs_p10](./core/runs.md#ims_wcs_p10) | [ims_wcs_ndcg](./core/runs.md#ims_wcs_ndcg) | [ims_wcs_twist](./core/runs.md#ims_wcs_twist) | [ims_wcs_rbp](./core/runs.md#ims_wcs_rbp) | [ims_wcs_err](./core/runs.md#ims_wcs_err) | [ims_wcs_recall](./core/runs.md#ims_wcs_recall) | [ims_wcs_rprec](./core/runs.md#ims_wcs_rprec)

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

- :fontawesome-solid-user-group: **Participant:** [MRG_UWaterloo](./core/participants.md#mrg_uwaterloo)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/MRG_UWaterloo-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/MRG_UWaterloo-CC.pdf)
- :material-file-search: **Runs:** [MRGrankrel](./core/runs.md#mrgrankrel) | [MRGrandrel](./core/runs.md#mrgrandrel) | [MRGrankall](./core/runs.md#mrgrankall)

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

- :fontawesome-solid-user-group: **Participant:** [WaterlooCormack](./core/participants.md#waterloocormack)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/WaterlooCormack-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/WaterlooCormack-CC.pdf)
- :material-file-search: **Runs:** [WCrobust04](./core/runs.md#wcrobust04) | [WCrobust0405](./core/runs.md#wcrobust0405) | [WCrobust04W](./core/runs.md#wcrobust04w)

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

- :fontawesome-solid-user-group: **Participant:** [UvA.ILPS](./core/participants.md#uva.ilps)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ILPS-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/ILPS-CC.pdf)
- :material-file-search: **Runs:** [IlpsUvAQlmNvsm](./core/runs.md#ilpsuvaqlmnvsm) | [IlpsUvANvsm](./core/runs.md#ilpsuvanvsm) | [IlpsUvABoir](./core/runs.md#ilpsuvaboir)

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

- :fontawesome-solid-user-group: **Participant:** [Webis](./core/participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Webis-O-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/Webis-O-CC.pdf)
- :material-file-search: **Runs:** [webis_baseline](./core/runs.md#webis_baseline) | [webis_baseline2](./core/runs.md#webis_baseline2) | [webis_reranked](./core/runs.md#webis_reranked) | [webis_reranked2](./core/runs.md#webis_reranked2)

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

- :fontawesome-solid-user-group: **Participant:** [tgncorp](./core/participants.md#tgncorp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/tgncorp-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/tgncorp-CC.pdf)
- :material-file-search: **Runs:** [tgncorpBASE](./core/runs.md#tgncorpbase) | [tgncorpBOOST](./core/runs.md#tgncorpboost)

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

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./core/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/udel_fang-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/udel_fang-CC.pdf)
- :material-file-search: **Runs:** [UDelInfoLOGext](./core/runs.md#udelinfologext) | [UDelInfoLOGint](./core/runs.md#udelinfologint) | [UDelInfoEXPint](./core/runs.md#udelinfoexpint)

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

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./core/participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UWaterlooMDS-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/UWaterlooMDS-CC.pdf)
- :material-file-search: **Runs:** [UWatMDS_TARSv1](./core/runs.md#uwatmds_tarsv1) | [UWatMDS_HT10](./core/runs.md#uwatmds_ht10) | [UWatMDS_TARSv2](./core/runs.md#uwatmds_tarsv2) | [UWatMDS_ustudy](./core/runs.md#uwatmds_ustudy) | [UWatMDS_BUnion](./core/runs.md#uwatmds_bunion) | [UWatMDS_BFuse](./core/runs.md#uwatmds_bfuse) | [UWatMDS_AUnion](./core/runs.md#uwatmds_aunion) | [UWatMDS_AFuse](./core/runs.md#uwatmds_afuse) | [UWatMDS_AWgtd](./core/runs.md#uwatmds_awgtd) | [UWatMDS_BWgtd](./core/runs.md#uwatmds_bwgtd)

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

## Precision Medicine 

#### Overview of the TREC 2017 Precision Medicine Track

_Kirk Roberts, Dina Demner-Fushman, Ellen M. Voorhees, William R. Hersh, Steven Bedrick, Alexander J. Lazar, Shubham Pant_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-PM.pdf)
??? abstract "Abstract"
	
	For many complex diseases, there is no “one size fits all” solutions for patients with a particular diagnosis. The proper treatment for a patient depends upon genetic, environmental, and lifestyle choices. The ability to personalize treatment in a scientifically rigorous manner based on these factors is the hallmark of the emerging “precision medicine” paradigm. Nowhere is the potential impact of precision medicine more closely felt than in cancer, where lifesaving treatments for particular patients could prove ineffective or even deadly for other patients based entirely upon the particular genetic mutations in the patient's tumor(s). Significant effort, therefore, has been devoted to deepening the scientific research surrounding precision medicine. This includes a Precision Medicine Initiative (Collins and Varmus, 2015) launched by former President Barack Obama in 2015, now known as the All of Us Research Program. A fundamental difficulty with putting the findings of precision medicine into practice is that-by its very nature-precision medicine creates a huge space of treatment options (Frey et al., 2016). These can easily overwhelm clinicians attempting to stay up-to-date with the latest findings, and can easily inhibit a clinician's attempts to determine the best possible treatment for a particular patient. However, the ability to quickly locate relevant evidence is the hallmark of information retrieval (IR). Further, for three consecutive years the TREC Clinical Decision Support (CDS) track has sought to evaluate IR systems that provide medical evidence to the point-of-care. It was natural, then, to specialize the CDS track to the needs of precision medicine so IR systems can focus on this important issue. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsDVHBLP17.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsDVHBLP17,
		author = {Kirk Roberts and Dina Demner{-}Fushman and Ellen M. Voorhees and William R. Hersh and Steven Bedrick and Alexander J. Lazar and Shubham Pant},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the {TREC} 2017 Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsDVHBLP17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### POZNAN Contribution to TREC PM 2017

_Artur Cieslewicz, Jakub Dutkiewicz, Czeslaw Jedrzejek_

- :fontawesome-solid-user-group: **Participant:** [POZNAN_SEMMED](./pm/participants.md#poznan_semmed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/POZNAN-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/POZNAN-PM.pdf)
- :material-file-search: **Runs:** [LGDprfGOpt](./pm/runs.md#lgdprfgopt) | [LGDnoprfGOpt](./pm/runs.md#lgdnoprfgopt) | [LGDraw](./pm/runs.md#lgdraw) | [LDGprfStrict](./pm/runs.md#ldgprfstrict) | [POZabsBB2GRn](./pm/runs.md#pozabsbb2grn) | [POZabsLGDGRn](./pm/runs.md#pozabslgdgrn) | [POZabsBB2sn](./pm/runs.md#pozabsbb2sn) | [LGDStrict](./pm/runs.md#lgdstrict)

??? abstract "Abstract"
	
	This work describes the medical information retrieval systems designed by the Poznan Consortium for TREC PM, personalized medicine track, which was submitted to the TREC 2017. The baseline is the Terrier DPH Bo1 which recently has been shown to be the most effective Terrier option. We also used Mesh query expansion, word2vec query expansion, and the combination of these two options. In all measures our results are approximately 0,02 above the median.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CieslewiczDJ17.bib) "
	```
	@inproceedings{DBLP:conf/trec/CieslewiczDJ17,
		author = {Artur Cieslewicz and Jakub Dutkiewicz and Czeslaw Jedrzejek},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{POZNAN} Contribution to {TREC} {PM} 2017},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/POZNAN-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CieslewiczDJ17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ETH Zurich at TREC Precision Medicine 2017

_Negar Foroutan Eghlidi, Jannick Griner, Nicolas Mesot, Leandro von Werra, Carsten Eickhoff_

- :fontawesome-solid-user-group: **Participant:** [ETH](./pm/participants.md#eth)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ETH-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/ETH-PM.pdf)
- :material-file-search: **Runs:** [eth_a_ws](./pm/runs.md#eth_a_ws) | [eth_a_luc](./pm/runs.md#eth_a_luc) | [eth_a_nn](./pm/runs.md#eth_a_nn) | [eth_a_ws_q](./pm/runs.md#eth_a_ws_q) | [eth_a_gws](./pm/runs.md#eth_a_gws) | [eth_t_ws](./pm/runs.md#eth_t_ws) | [eth_t_luc](./pm/runs.md#eth_t_luc) | [eth_t_nn](./pm/runs.md#eth_t_nn) | [eth_t_wsb_q](./pm/runs.md#eth_t_wsb_q) | [eth_t_gwsq](./pm/runs.md#eth_t_gwsq)

??? abstract "Abstract"
	
	This paper describes ETH Zurich's submission to the TREC 2017 Precision Medicine (PM) track. We begin by performing literal query term matching, taking into account the likelihood of document relevance in terms of cancer types, genetic variants, and demographics. In a second, subsequent stage, we re-rank the most relevant results based on a range of deep neural gene embeddings that project literal genetic expressions into a semantics-preserving vector space using feed-forward networks trained on PubMed and NCBI information but also relying on generative adversarial methods to determine the likelihood of co-occurrence of various mutations within the same patient/article. Empirical results show that even without existing expert labels, the proposed method can introduce marginal improvements over competitive tf-idf baselines.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EghlidiGMWE17.bib) "
	```
	@inproceedings{DBLP:conf/trec/EghlidiGMWE17,
		author = {Negar Foroutan Eghlidi and Jannick Griner and Nicolas Mesot and Leandro von Werra and Carsten Eickhoff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ETH} Zurich at {TREC} Precision Medicine 2017},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/ETH-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EghlidiGMWE17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UTD HLTRI at TREC 2017: Precision Medicine Track

_Travis R. Goodwin, Michael A. Skinner, Sanda M. Harabagiu_

- :fontawesome-solid-user-group: **Participant:** [UTDHLTRI](./pm/participants.md#utdhltri)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UTDHLTRI-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/UTDHLTRI-PM.pdf)
- :material-file-search: **Runs:** [UTDHLTJQ](./pm/runs.md#utdhltjq) | [UTDHLTJQT](./pm/runs.md#utdhltjqt) | [UTDHLTAFT](./pm/runs.md#utdhltaft) | [UTDHLTSFT](./pm/runs.md#utdhltsft) | [UTDHLTFFT](./pm/runs.md#utdhltfft) | [UTDHLTSQT](./pm/runs.md#utdhltsqt) | [UTDHLTAF](./pm/runs.md#utdhltaf) | [UTDHLTSF](./pm/runs.md#utdhltsf) | [UTDHLTFF](./pm/runs.md#utdhltff) | [UTDHLTSQ](./pm/runs.md#utdhltsq)

??? abstract "Abstract"
	
	In this paper, we describe the system designed for the TREC 2017 Precision Medicine track by the University of Texas at Dallas (UTD) Human Language Technology Research Institute (HLTRI). Our system incorporates an aspect-based retrieval paradigm wherein each of the four structured components of the topic is cast as a separate aspect, along with two “hidden” aspects encoding the need that retrieved documents be within the domain of precision medicine and that retrieved documents have a focus on treatment. To this end, we construct knowledge graph encoding the relationships between drugs, genes, and mutations. Our experiments reveal that the aspect-based approach leads to improved quality of retrieved scientific articles and clinical trials.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoodwinSH17.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoodwinSH17,
		author = {Travis R. Goodwin and Michael A. Skinner and Sanda M. Harabagiu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UTD} {HLTRI} at {TREC} 2017: Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UTDHLTRI-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GoodwinSH17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CBNU at TREC 2017 Precision Medicine Track

_Seung-Hyeon Jo, Kyung-Soon Lee_

- :fontawesome-solid-user-group: **Participant:** [cbnu](./pm/participants.md#cbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/cbnu-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/cbnu-PM.pdf)
- :material-file-search: **Runs:** [cbnuCT1](./pm/runs.md#cbnuct1) | [cbnuCT2](./pm/runs.md#cbnuct2) | [cbnuCT3](./pm/runs.md#cbnuct3) | [cbnuSA1](./pm/runs.md#cbnusa1) | [cbnuSA2](./pm/runs.md#cbnusa2) | [cbnuSA3](./pm/runs.md#cbnusa3)

??? abstract "Abstract"
	
	This paper describes the participation of the CBNU team at the TREC Precision Medicine Track 2017. We have constructed cancer-centered document clusters using cancer-gene relation and clinical causal information. A query has been expanded with disease terms and pseudo-relevance feedback is applied for cancer disease document clusters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoL17.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoL17,
		author = {Seung{-}Hyeon Jo and Kyung{-}Soon Lee},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CBNU} at {TREC} 2017 Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/cbnu-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoL17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Patient selection for clinical trials based on concept-based retrieval  and result filtering and ranking

_Johannes Leveling_

- :fontawesome-solid-user-group: **Participant:** [teckro](./pm/participants.md#teckro)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/teckro-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/teckro-PM.pdf)
- :material-file-search: **Runs:** [teckro1](./pm/runs.md#teckro1) | [teckro2](./pm/runs.md#teckro2) | [teckro3](./pm/runs.md#teckro3) | [teckro4](./pm/runs.md#teckro4) | [teckro5](./pm/runs.md#teckro5)

??? abstract "Abstract"
	
	For our participation at the clinical trials task in the TREC 2017 Precision Medicine track 2017, we investigated retrieving and matching clinical trial documents with patient information based on text and concept annotations of the text, filtering results for demographic information such as gender and age, and re-ranking results based on patient information. Experimental results show a competitive precision at high ranks for our least complex approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Leveling17.bib) "
	```
	@inproceedings{DBLP:conf/trec/Leveling17,
		author = {Johannes Leveling},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Patient selection for clinical trials based on concept-based retrieval and result filtering and ranking},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/teckro-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Leveling17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UCAS at TREC-2017 Precision Medicine Track

_Canjia Li, Ben He, Yingfei Sun, Jungang Xu_

- :fontawesome-solid-user-group: **Participant:** [UCAS](./pm/participants.md#ucas)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UCAS-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/UCAS-PM.pdf)
- :material-file-search: **Runs:** [UCASBASE](./pm/runs.md#ucasbase) | [UCASSEM3](./pm/runs.md#ucassem3) | [UCASSEM2](./pm/runs.md#ucassem2) | [UCASSEMUMLS](./pm/runs.md#ucassemumls) | [UCASSEM1](./pm/runs.md#ucassem1) | [UCASSEM3a](./pm/runs.md#ucassem3a) | [UCASSEM2a](./pm/runs.md#ucassem2a) | [UCASSEMUMLSa](./pm/runs.md#ucassemumlsa) | [UCASSEM1a](./pm/runs.md#ucassem1a) | [UCASBASEa](./pm/runs.md#ucasbasea)

??? abstract "Abstract"
	
	The participation of UCAS at TREC Precision Medicine 2017 aims to evaluate the effectiveness of integrating semantic evidence to enhance medical information retrieval system. Benefited from the success of distributed semantic representation of words and documents in the natural language process (NLP) domain, two methods on generating document vectors are proposed. Based on the hypothesis that pseudo relevant feedback for a given query would be a better representation of the query in the semantic vector space, we propose a framework that integrates the semantic features to the final ranking process. In addition, query expansion using Medical Subject Headings (MeSH) and pseudo relevance feedback (PRF) are used. Experimental results show that our method achieves significant improvement over the PRF baseline for clinical trials, while full text articles might be required for learning local document embeddings that are effective for retrieval from abstracts.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiHSX17.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiHSX17,
		author = {Canjia Li and Ben He and Yingfei Sun and Jungang Xu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UCAS} at {TREC-2017} Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UCAS-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiHSX17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Hybrid Approach to Precision Medicine-related Biomedical Article  Retrieval and Clinical Trial Matching

_Yuan Ling, Sadid A. Hasan, Michele Filannino, Kevin P. Buchan, Kahyun Lee, Joey Liu, William Boag, Di Jin, Özlem Uzuner, Kathy Lee, Vivek V. Datla, Ashequl Qadir, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna-mit-suny](./pm/participants.md#prna-mit-suny)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/prna-mit-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/prna-mit-PM.pdf)
- :material-file-search: **Runs:** [pms_run1](./pm/runs.md#pms_run1) | [pms_run1_tri](./pm/runs.md#pms_run1_tri) | [pms_run2_abs](./pm/runs.md#pms_run2_abs) | [pms_run2_tri](./pm/runs.md#pms_run2_tri) | [pms_run3_abs](./pm/runs.md#pms_run3_abs) | [pms_run3_tri](./pm/runs.md#pms_run3_tri) | [pms_run4_abs](./pm/runs.md#pms_run4_abs) | [pms_run4_tri](./pm/runs.md#pms_run4_tri) | [pms_run5_abs](./pm/runs.md#pms_run5_abs) | [pms_run5_tri](./pm/runs.md#pms_run5_tri)

??? abstract "Abstract"
	
	We describe our systems implemented for the Text Retrieval Conference (TREC 2017) Precision Medicine track. We submitted five runs for biomedical article retrieval and five runs for clinical trial matching. Our approaches combine strict rule matching with an ontology-based solution. Evaluation results demonstrate that our best run obtained the 2nd highest precision (P@5) score for the clinical trial matching task and was consistently ranked within top 5 teams in all evaluation metrics for the biomedical literature retrieval task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LingHFBLLBJULDQ17.bib) "
	```
	@inproceedings{DBLP:conf/trec/LingHFBLLBJULDQ17,
		author = {Yuan Ling and Sadid A. Hasan and Michele Filannino and Kevin P. Buchan and Kahyun Lee and Joey Liu and William Boag and Di Jin and {\"{O}}zlem Uzuner and Kathy Lee and Vivek V. Datla and Ashequl Qadir and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Hybrid Approach to Precision Medicine-related Biomedical Article Retrieval and Clinical Trial Matching},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/prna-mit-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LingHFBLLBJULDQ17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2017 Precision Medicine - Medical University of Graz

_Pablo López-García, Michel Oleynik, Zdenko Kasác, Stefan Schulz_

- :fontawesome-solid-user-group: **Participant:** [imi_mug](./pm/participants.md#imi_mug)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/imi_mug-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/imi_mug-PM.pdf)
- :material-file-search: **Runs:** [mugpubbase](./pm/runs.md#mugpubbase) | [mugctbase](./pm/runs.md#mugctbase) | [mugpubboost](./pm/runs.md#mugpubboost) | [mugpubdiseas](./pm/runs.md#mugpubdiseas) | [mugpubgene](./pm/runs.md#mugpubgene) | [mugpubshould](./pm/runs.md#mugpubshould) | [mugctboost](./pm/runs.md#mugctboost) | [mugctmust](./pm/runs.md#mugctmust) | [mugctdisease](./pm/runs.md#mugctdisease) | [mugctgene](./pm/runs.md#mugctgene)

??? abstract "Abstract"
	
	In this paper we report on our participation in the TREC 2017 Precision Medicine track (team name: imi_mug). We submitted 5 fully automatic runs to both the biomedical articles and clinical trials subtasks, focusing strongly on the former. Our system was based on Elasticsearch, whose queries were generated modularly via our own open source framework. Our results showed that a modern search engine with an advanced query language is a powerful solution for the proposed tasks but it requires deep medical knowledge and careful tuning to get top performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lopez-GarciaOK017.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lopez-GarciaOK017,
		author = {Pablo L{\'{o}}pez{-}Garc{\'{\i}}a and Michel Oleynik and Zdenko Kas{\'{a}}c and Stefan Schulz},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2017 Precision Medicine - Medical University of Graz},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/imi\_mug-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lopez-GarciaOK017.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UD_GU_BioTM at TREC 2017: Precision Medicine Track

_A. S. M. Ashique Mahmood, Gang Li, Shruti Rao, Peter B. McGarvey, Cathy H. Wu, Subha Madhavan, K. Vijay-Shanker_

- :fontawesome-solid-user-group: **Participant:** [UD_GU_BioTM](./pm/participants.md#ud_gu_biotm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UD_GU_BioTM-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/UD_GU_BioTM-PM.pdf)
- :material-file-search: **Runs:** [UD_GU_SA_1](./pm/runs.md#ud_gu_sa_1) | [UD_GU_SA_2](./pm/runs.md#ud_gu_sa_2) | [UD_GU_SA_3](./pm/runs.md#ud_gu_sa_3) | [UD_GU_SA_4](./pm/runs.md#ud_gu_sa_4) | [UD_GU_SA_5](./pm/runs.md#ud_gu_sa_5) | [UD_GU_CT_1](./pm/runs.md#ud_gu_ct_1) | [UD_GU_CT_2](./pm/runs.md#ud_gu_ct_2) | [UD_GU_CT_3](./pm/runs.md#ud_gu_ct_3) | [UD_GU_CT_4](./pm/runs.md#ud_gu_ct_4) | [UD_GU_CT_5](./pm/runs.md#ud_gu_ct_5)

??? abstract "Abstract"
	
	This paper describes the system developed for the TREC 2017 PM track. We employed a two-part system to generate the ranked list of clinical trials and scientific abstracts. The first part pertains to query expansion and document retrieval from document index. The second part pertains to generating the final ranked list by implementing a heuristic scoring method. The scoring for clinical trials involved grouping trials based on different trial fields and extraction of features based on occurrences of gene/disease and other terms in the trial. The scoring for scientific abstracts involved applying a NLP system to extract relations from text, as well as extraction of additional information relevant to precision medicine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MahmoodLRMWMV17.bib) "
	```
	@inproceedings{DBLP:conf/trec/MahmoodLRMWMV17,
		author = {A. S. M. Ashique Mahmood and Gang Li and Shruti Rao and Peter B. McGarvey and Cathy H. Wu and Subha Madhavan and K. Vijay{-}Shanker},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UD{\_}GU{\_}BioTM at {TREC} 2017: Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UD\_GU\_BioTM-PM.pdf},
		timestamp = {Mon, 19 Oct 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/MahmoodLRMWMV17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSIRO at 2017 TREC Precision Medicine Track

_Vincent Nguyen, Sarvnaz Karimi, Sara Falamaki, Diego Mollá Aliod, Cécile Paris, Stephen Wan_

- :fontawesome-solid-user-group: **Participant:** [CSIROmed](./pm/participants.md#csiromed)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/CSIRO-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/CSIRO-PM.pdf)
- :material-file-search: **Runs:** [aCSIROmedAll](./pm/runs.md#acsiromedall) | [cCSIROmedAll](./pm/runs.md#ccsiromedall) | [cCSIROmedNEG](./pm/runs.md#ccsiromedneg) | [cCSIROmedMCM](./pm/runs.md#ccsiromedmcm) | [cCSIROmedHGB](./pm/runs.md#ccsiromedhgb) | [cCSIROmedMCB](./pm/runs.md#ccsiromedmcb) | [aCSIROmedNEG](./pm/runs.md#acsiromedneg) | [aCSIROmedPCB](./pm/runs.md#acsiromedpcb) | [aCSIROmedMGB](./pm/runs.md#acsiromedmgb) | [aCSIROmedMCB](./pm/runs.md#acsiromedmcb)

??? abstract "Abstract"
	
	We report on our participation as the CSIROmed1 team in the TREC 2017 Precision Medicine track. We submitted five runs for the scientific abstracts collection (MEDLINE and Cancer Proceedings), and five runs for the clinical trials collection. We experimented with a number of query expansion and search result re-ranking techniques. We used citation and MeSH-based re-ranking methods, as well as reranking based on a merging algorithm proposed for federated search. Our results show that boosting the gene variant in the query increases the relevance of the retrieved results. One of our five runs for clinical trials task was ranked in top 10 runs out of 133 runs submitted for this task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NguyenKFAPW17.bib) "
	```
	@inproceedings{DBLP:conf/trec/NguyenKFAPW17,
		author = {Vincent Nguyen and Sarvnaz Karimi and Sara Falamaki and Diego Moll{\'{a}} Aliod and C{\'{e}}cile Paris and Stephen Wan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CSIRO} at 2017 {TREC} Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/CSIRO-PM.pdf},
		timestamp = {Thu, 21 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NguyenKFAPW17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Team UKNLP at TREC 2017 Precision Medicine Track: A Knowledge-Based  IR System with Tuned Query-Time Boosting

_Jiho Noh, Ramakanth Kavuluru_

- :fontawesome-solid-user-group: **Participant:** [UKNLP](./pm/participants.md#uknlp)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UKNLP-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/UKNLP-PM.pdf)
- :material-file-search: **Runs:** [UKY_BASE](./pm/runs.md#uky_base) | [UKY_CJT](./pm/runs.md#uky_cjt) | [UKY_AGG](./pm/runs.md#uky_agg) | [UKY_COM](./pm/runs.md#uky_com) | [UKY_MAN](./pm/runs.md#uky_man) | [UKY_TRL](./pm/runs.md#uky_trl) | [UKY_T2](./pm/runs.md#uky_t2) | [UKY_T3](./pm/runs.md#uky_t3) | [UKY_T4](./pm/runs.md#uky_t4)

??? abstract "Abstract"
	
	This paper describes the system architecture of the University of Kentucky Natural Language Processing (UKNLP) team's entry for the TREC 2017 Precision Medicine Track. The goal of the challenge is to retrieve useful precision medicine-related information (abstracts, clinical trials) for the given synthetic cancer patient cases, each of which consists of a neoplastic condition, genetic variants, demographic details, and any additional information (e.g., comorbidities). We explored query expansion techniques using well-known broad knowledge sources such as the Unified Medical Language System (UMLS) and the Medical Subject Headings (MeSH) for each abstract, and additional specialized sources such as the Catalogue Of Somatic Mutations In Cancer (COSMIC) database, which allowed us to construct boosted queries. We conducted several experiments with model averaging techniques and our final system architecture placed 6th (in terms of infNDCG and R-prec) among 29 teams that submitted runs to the scientific abstract retrieval task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NohK17.bib) "
	```
	@inproceedings{DBLP:conf/trec/NohK17,
		author = {Jiho Noh and Ramakanth Kavuluru},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Team {UKNLP} at {TREC} 2017 Precision Medicine Track: {A} Knowledge-Based {IR} System with Tuned Query-Time Boosting},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UKNLP-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NohK17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Customizing a Variant Annotation-Support Tool: an Inquiry into Probability  Ranking Principles for TREC Precision Medicine

_Emilie Pasche, Julien Gobeill, Luc Mottin, Anaïs Mottaz, Douglas Teodoro, Paul Van Rijen, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [BiTeM](./pm/participants.md#bitem)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/BiTeM-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/BiTeM-PM.pdf)
- :material-file-search: **Runs:** [SIBTMlit1](./pm/runs.md#sibtmlit1) | [SIBTMlit2](./pm/runs.md#sibtmlit2) | [SIBTMlit3](./pm/runs.md#sibtmlit3) | [SIBTMlit4](./pm/runs.md#sibtmlit4) | [SIBTMlit5](./pm/runs.md#sibtmlit5) | [SIBTct1](./pm/runs.md#sibtct1) | [SIBTct2](./pm/runs.md#sibtct2) | [SIBTct3](./pm/runs.md#sibtct3) | [SIBTct4](./pm/runs.md#sibtct4) | [SIBTct5](./pm/runs.md#sibtct5)

??? abstract "Abstract"
	
	The TREC 2017 Precision Medicine Track aims at building systems providing meaningful precision medicine-related information to clinicians in the field of oncology. The track includes two tasks: 1) retrieving scientific abstracts addressing treatment effect and prognosis of a disease and 2) retrieving clinical trials for which a patient is eligible. The SIB Text Mining group participated in both tasks. Regarding the retrieval of scientific abstracts, we designed a set of different queries with decreasing levels of specificity. The idea was to start initiating a very specific query, from which less specific queries will be inferred. We may thus consider as relevant abstracts that did not mention all critical aspects of the complete query but could still be of interest. Therefore, the main component of our approach was a large query generation module (e.g. disease + gene + variant; disease + gene; gene + variant) - with each generated query being differentially weighted. To increase the scope of the queries, we applied query expansion strategies. In particular, a single nucleotide variant (SNV) generator was developed to recognize standard nomenclature as described by the Human Genome Variation Society (HGVS) as well as non-standard formats frequently found in the literature. We thus expect to retrieve a maximum of relevant abstracts. We then applied different strategies to favor relevant abstracts by re-ranking them based on more general criteria. First, we assumed that an abstract with a high frequency of drug names is more probably relevant to support our task. Therefore, we pre-annotated all the collection with DrugBank, thus enabling to retrieve the number of occurrences of drug names per abstract. Second, we assumed that the presence of some specific keywords (e.g. “treat”) in the abstract should increase the relevance of the paper, while the presence of some other keywords (e.g. “marker”) should decrease its relevance. Third, we assumed that some publications, such as clinical trials, should receive higher relevance for this task. Regarding the retrieval of clinical trials, we investigated for the competition different combinations of filtering and information retrieval strategies, mostly based on the exploitation of ontologies. Our preliminary analysis of the collection showed that : (1) demographic features (age and gender) are stored in a perfectly-structured form in clinical trials, thus this feature can be easily handled with strict filtering ; (2) the trials contain very few mentions of the requested genes and variants ; (3) diseases are stored in very inconsistent forms, as they are free text entities and can be mentioned in different fields such as condition, keywords, summary, criteria, etc. Thus, we assumed that identifying clinical trials dealing with the correct disease was the most challenging issue for this competition. For such a task, we perform Name Entity Recognition with the NCI thesaurus in order to recognize mentions of diseases in topics and in different fields of the clinical trials. This strategy handles several issues of free text descriptions, such as synonyms (“Cancer” and “Neoplasm” are equivalent) and hierarchies (“Colon carcinoma” is a subtype of “Colorectal carcinoma”). Then, for each topic, we apply different strategies of trials filtering - according to fields where the disease was identified - and hierarchies. Finally, classical information retrieval is performed with genes and variants as queries. The strictest filtering leads to an average of 62 retrieved trials per topic and tends to favor high precision, while the most relaxed filtering leads to an average of 379 retrieved trials per topic and tends to favor high recall. Yet, results show that the Precision values are poorly impacted by these strategies, while runs that favor Recall showed a better general behavior for this task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PascheGMMTRR17.bib) "
	```
	@inproceedings{DBLP:conf/trec/PascheGMMTRR17,
		author = {Emilie Pasche and Julien Gobeill and Luc Mottin and Ana{\"{\i}}s Mottaz and Douglas Teodoro and Paul Van Rijen and Patrick Ruch},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Customizing a Variant Annotation-Support Tool: an Inquiry into Probability Ranking Principles for {TREC} Precision Medicine},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/BiTeM-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PascheGMMTRR17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Identifying Personalised Treatments and Clinical Trials for Precision  Medicine using Semantic Search with Thalia

_Piotr Przybyla, Axel J. Soto, Sophia Ananiadou_

- :fontawesome-solid-user-group: **Participant:** [NaCTeM](./pm/participants.md#nactem)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/NaCTeM-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/NaCTeM-PM.pdf)
- :material-file-search: **Runs:** [Textual](./pm/runs.md#textual) | [Ontological](./pm/runs.md#ontological) | [Broad](./pm/runs.md#broad) | [Semantic](./pm/runs.md#semantic) | [Focused](./pm/runs.md#focused) | [Textualc](./pm/runs.md#textualc) | [Ontologicalc](./pm/runs.md#ontologicalc) | [Broadc](./pm/runs.md#broadc) | [Semanticc](./pm/runs.md#semanticc) | [Focusedc](./pm/runs.md#focusedc)

??? abstract "Abstract"
	
	This paper reports the main methods applied in our submission to TREC 2017 Precision Medicine Track. The goal of this challenge was to retrieve documents containing potential treatments and clinical trials for specific patient characteristics. Our main strategy involved using a semantic search engine called Thalia (Text mining for Highlighting, Aggregating and Linking Information in Articles), which allows the recognition of diseases and genes mentioned in text. The recognition of named entities and its linking to concepts in ontologies facilitates more accurate retrieval than just relying on plain textual search and matching. We also highlight the different strategies applied when querying Thalia in the context of this Precision Medicine challenge, which aimed to support different use cases (i.e. more focused or broader searches).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PrzybylaSA17.bib) "
	```
	@inproceedings{DBLP:conf/trec/PrzybylaSA17,
		author = {Piotr Przybyla and Axel J. Soto and Sophia Ananiadou},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Identifying Personalised Treatments and Clinical Trials for Precision Medicine using Semantic Search with Thalia},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/NaCTeM-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PrzybylaSA17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ranking Clinical Trials Using Elasticsearch

_Ajinkya Yogesh Thorve, Haimonti Dutta_

- :fontawesome-solid-user-group: **Participant:** [TREC_UB](./pm/participants.md#trec_ub)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/TREC_UB-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/TREC_UB-PM.pdf)
- :material-file-search: **Runs:** [1_ec_simple](./pm/runs.md#1_ec_simple) | [2_ec_complex](./pm/runs.md#2_ec_complex)

??? abstract "Abstract"
	
	The clinical trials task of the TREC 2017 Precision Medicine Track was designed to represent the potential for connecting patients with experimental treatments if existing treatments were ineffective. Participants were challenged with the task of retrieving appropriate clinical trials from ClinicalTrials.gov for which a patient is eligible. This paper presents an approach to solving the problem by first preparing an index for the clinical trial descriptions based on specific tags in the XML files and querying them using Elasticsearch. Initial results indicate that our approach performed very well for certain kinds of queries - however, more tuning may be required for ensuring generalizable results from the search.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ThorveD17.bib) "
	```
	@inproceedings{DBLP:conf/trec/ThorveD17,
		author = {Ajinkya Yogesh Thorve and Haimonti Dutta},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Ranking Clinical Trials Using Elasticsearch},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/TREC\_UB-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ThorveD17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UNT Precision Medicine Information Retrieval at TREC 2017

_Lokesh Kumar Viswavarapu, Jiangping Chen, Ana D. Cleveland, Haihua Chen_

- :fontawesome-solid-user-group: **Participant:** [UNTIIA](./pm/participants.md#untiia)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UNTIIA-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/UNTIIA-PM.pdf)
- :material-file-search: **Runs:** [UNTIIADW](./pm/runs.md#untiiadw) | [UNTIIASY](./pm/runs.md#untiiasy) | [UNTIIAIS](./pm/runs.md#untiiais) | [UNTIIAGA](./pm/runs.md#untiiaga) | [UNTIIALQ](./pm/runs.md#untiialq) | [UNTIIACTDW](./pm/runs.md#untiiactdw) | [UNTIIACTSY](./pm/runs.md#untiiactsy) | [UNTIIACTIS](./pm/runs.md#untiiactis) | [UNTIIACTGA](./pm/runs.md#untiiactga) | [UNTIIACTLQ](./pm/runs.md#untiiactlq)

??? abstract "Abstract"
	
	This paper reports our participation in TREC 2017 Precision Medicine (PM) track. Based on our TREC 2016 Clinical Decision Support System, we implemented and tested five different query construction strategies: Query construction with disease weighted terms, with synonyms of disease terms, with Internet search results, with gene alias terms, and with Terrier logical query language. A re-ranking strategy that considered the occurrence of disease names, gene names, and treatment terms were applied to adjust the order of the retrieved documents. A new experimental module called Relevance Judgment User System (RJUS), which is an augmentation to the information retrieval platform Terrier1 v4.2, was designed to facilitate the design of query construction and result re-ranking strategies. We submitted 5 runs applying the five query construction strategies respectively combining with pseudo relevance feedback and the reranking approach. The query construction with Terrier logical query language achieved the best performance among our submitted results. Our future study will investigate the use of topic modeling for query construction and effective approaches for finding relevant clinical trials.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ViswavarapuCCC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/ViswavarapuCCC17,
		author = {Lokesh Kumar Viswavarapu and Jiangping Chen and Ana D. Cleveland and Haihua Chen},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UNT} Precision Medicine Information Retrieval at {TREC} 2017},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UNTIIA-PM.pdf},
		timestamp = {Thu, 23 Dec 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ViswavarapuCCC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Term-based and Concept-based Representation for Clinical  Retrieval

_Yue Wang, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./pm/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/udel_fang-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/udel_fang-PM.pdf)
- :material-file-search: **Runs:** [UDInfoPMCT3](./pm/runs.md#udinfopmct3) | [UDInfoPMCT4](./pm/runs.md#udinfopmct4) | [UDInfoPMCT6](./pm/runs.md#udinfopmct6) | [UDInfoPMCT10](./pm/runs.md#udinfopmct10) | [UDInfoPMSA2](./pm/runs.md#udinfopmsa2) | [UDInfoPMSA3](./pm/runs.md#udinfopmsa3) | [UDInfoPMSA5](./pm/runs.md#udinfopmsa5) | [UDInfoPMSA6](./pm/runs.md#udinfopmsa6) | [UDInfoPMSA7](./pm/runs.md#udinfopmsa7) | [UDInfoPMCT8](./pm/runs.md#udinfopmct8)

??? abstract "Abstract"
	
	Biomedical domain retrieval has been a trending topic that attracts many IR researchers. Different document representation methods, i.e., term based representation and concept based representation, have been proposed to solve this question. However, previous studies have focused the verbose queries. In this year's Precision Medicine track, we evaluated the performance of these two basic document representation methods on short queries. We also explored possible ways to combine these two methods. The results show that these two representations perform differently on the scientific abstract and clinical trail data sets. Simply merge the results list may not leads to optimal performance, while term based filtering on top of the concept based results could significantly improve the performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Wang017.bib) "
	```
	@inproceedings{DBLP:conf/trec/Wang017,
		author = {Yue Wang and Hui Fang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Combining Term-based and Concept-based Representation for Clinical Retrieval},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/udel\_fang-PM.pdf},
		timestamp = {Thu, 17 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/Wang017.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### HokieGo at 2017 PM Task: Genetic Programming based re-ranking method  In Biomedical Information Retrieval

_Junyan Wu, Xiaofu Ma, Weiguo Fan_

- :fontawesome-solid-user-group: **Participant:** [HokieGo](./pm/participants.md#hokiego)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/HokieGo-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/HokieGo-PM.pdf)
- :material-file-search: **Runs:** [GP16Medline](./pm/runs.md#gp16medline) | [GP16Trail](./pm/runs.md#gp16trail) | [GP14Medline](./pm/runs.md#gp14medline) | [GP14Trail](./pm/runs.md#gp14trail)

??? abstract "Abstract"
	
	This paper summarizes our efforts on TREC 2017 Precision Medicine Track. We present a genetic programming based learning-to-rank algorithm. We perform two training experiments on 2014 and 2016 TREC CDS data and apply the pre-trained model as re-ranking method to improve the performance. In addition, two utility functions, CHK and FFP4, have been used for the training optimization.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuMF17.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuMF17,
		author = {Junyan Wu and Xiaofu Ma and Weiguo Fan},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {HokieGo at 2017 {PM} Task: Genetic Programming based re-ranking method In Biomedical Information Retrieval},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/HokieGo-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuMF17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieving documents based on gene name variations: MedIER at TREC  2017 Precision Medicine Track

_Tong Yin, Danny T. Y. Wu, V. G. Vinod Vydiswaran_

- :fontawesome-solid-user-group: **Participant:** [MedIER](./pm/participants.md#medier)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/MedIER-PM.pdf](https://trec.nist.gov/pubs/trec26/papers/MedIER-PM.pdf)
- :material-file-search: **Runs:** [MedIER_sa2](./pm/runs.md#medier_sa2) | [MedIER_sa1](./pm/runs.md#medier_sa1) | [MedIER_sa4](./pm/runs.md#medier_sa4) | [MedIER_sa3](./pm/runs.md#medier_sa3) | [MedIER_ct1](./pm/runs.md#medier_ct1) | [MedIER_ct2](./pm/runs.md#medier_ct2) | [MedIER_ct3](./pm/runs.md#medier_ct3) | [MedIER_ct4](./pm/runs.md#medier_ct4)

??? abstract "Abstract"
	
	The TREC 2017 Precision Medicine Track focused on finding relevant medical documents - scientific abstracts and clinical trials - for cancer patient cases based on specific genetic variation and demographic information. We focused on the genetic variations mentioned in the query and explored ways to modify the search query and the retrieval ranking using this information. Further, we explored filtering retrieved results based on demographic information matching for clinical trials. The results show little improvements of the approaches over baseline runs, and suggest need for additional exploration.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YinWV17.bib) "
	```
	@inproceedings{DBLP:conf/trec/YinWV17,
		author = {Tong Yin and Danny T. Y. Wu and V. G. Vinod Vydiswaran},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Retrieving documents based on gene name variations: MedIER at {TREC} 2017 Precision Medicine Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/MedIER-PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YinWV17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Leveraging both Structured and Unstructured Data for Precision Information  Retrieval

_Yanshan Wang, Ravikumar Komandur Elayavilli, Majid Rastegar-Mojarad, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [MayoNLPTeam](./pm/participants.md#mayonlpteam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/MayoNLPTeam_PM.pdf](https://trec.nist.gov/pubs/trec26/papers/MayoNLPTeam_PM.pdf)
- :material-file-search: **Runs:** [mayonlppm1](./pm/runs.md#mayonlppm1) | [mayonlppm2](./pm/runs.md#mayonlppm2) | [mayonlppm3](./pm/runs.md#mayonlppm3) | [mayonlppm4](./pm/runs.md#mayonlppm4) | [mayonlppm5](./pm/runs.md#mayonlppm5) | [mayonlpct1](./pm/runs.md#mayonlpct1) | [mayonlpct2](./pm/runs.md#mayonlpct2) | [mayonlpct3](./pm/runs.md#mayonlpct3) | [mayonlpct4](./pm/runs.md#mayonlpct4) | [mayonlpct5](./pm/runs.md#mayonlpct5)

??? abstract "Abstract"
	
	This paper describes the participation of the Mayo Clinic NLP team in the Text REtreival Conference (TREC) 2017 Precision Medicine track. The novelty of our systems is four-fold. First, compared to our submissions in the previous year, our systems utilized an enhanced named entity recognition (NER) method to extract genes, variants, proteins, and diseases from PubMed articles. This NER method combined several state-of-the-art NER tools including TaggerOne, beCAS, Reach and tmVAR. The extracted entities were indexed in different fields and treated as structured data for retrieval. Second, we used multi-field querying in a Pseudo Relevance Feedback (PRF) model. We first query the unstructured fields (i.e., the fields of title and abstract) and utilize information in structured fields from top-ranked documents as feedback for query expansion. Third, we explored the use of MeSH on Demand, a web service identifying MeSH terms in free-text and recommending similar PubMed articles which are relevant to the text, to boost the performance of our retrieval systems. The reason we used MeSH on Demand is due to its effectiveness for recommending relevant PubMed articles based on our manual judgments. Fourth, we utilized the demographic information (i.e., age and sex) as structured data to filter out the clinical trials that did not meet the criteria in each topic.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangERL17.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangERL17,
		author = {Yanshan Wang and Ravikumar Komandur Elayavilli and Majid Rastegar{-}Mojarad and Hongfang Liu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Leveraging both Structured and Unstructured Data for Precision Information Retrieval},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/MayoNLPTeam\_PM.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangERL17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## LiveQA 

#### Overview of the Medical Question Answering Task at TREC 2017 LiveQA

_Asma Ben Abacha, Eugene Agichtein, Yuval Pinter, Dina Demner-Fushman_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-QA.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-QA.pdf)
??? abstract "Abstract"
	
	We present an overview of the medical question answering task organized at the TREC 2017 LiveQA track. The task addresses the automatic answering of consumer health questions received by the U.S. National Library of Medicine. We provided both training question-answer pairs, and test questions with reference answers1. All questions were manually annotated with the main entities (foci) and question types. The medical task received eight runs from five participating teams. Different approaches have been applied, including classical answer retrieval based on question analysis and similar question retrieval. In particular, several deep learning approaches were tested, including attentional encoder-decoder networks, long short-term memory networks and convolutional neural networks. The training datasets were both from the open domain and the medical domain. We discuss the obtained results and give some insights for future research in medical question answering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbachaAPD17.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbachaAPD17,
		author = {Asma Ben Abacha and Eugene Agichtein and Yuval Pinter and Dina Demner{-}Fushman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of the Medical Question Answering Task at {TREC} 2017 LiveQA},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-QA.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbachaAPD17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Open domain real-time question answering based on asynchronous multiperspective  context-driven retrieval and neural paraphrasing

_Vivek V. Datla, Tilak Raj Arora, Joey Liu, Viraj Adduru, Sadid A. Hasan, Kathy Lee, Ashequl Qadir, Yuan Ling, Aaditya Prakash, Oladimeji Farri_

- :fontawesome-solid-user-group: **Participant:** [prna](./qa/participants.md#prna)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/prna-QA.pdf](https://trec.nist.gov/pubs/trec26/papers/prna-QA.pdf)
- :material-file-search: **Runs:** [prnar1](./qa/runs.md#prnar1) | [prnarun2](./qa/runs.md#prnarun2) | [prnarun3](./qa/runs.md#prnarun3)

??? abstract "Abstract"
	
	The live-QA task involves real user questions, extracted from the stream of most recent questions submitted to the Yahoo Answers (YA) site that has not yet been answered. There are two tracks in the live-QA task, general domain, and medical domain. In general domain, unanswered questions are taken from six categories of real-time yahoo question answering feed, and for the medical domain, they are taken from the consumer health questions asked in NLM forums. The answers given by the system for both general and medical tasks are evaluated by human experts looking into accuracy, readability, and preciseness. The features of our open-domain question answering include question decomposition, question focus identification, context identification, answer retrieval and summarization. The current system builds an asynchronous system which has a multi-perspective view of the question being asked by decomposing the question into multiple smaller questions and identifying answers to sub-questions and summarizing the answers. Our system performed close to the median in the live-QA task and ranked second in the medical sub-task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DatlaALAHLQLPF17.bib) "
	```
	@inproceedings{DBLP:conf/trec/DatlaALAHLQLPF17,
		author = {Vivek V. Datla and Tilak Raj Arora and Joey Liu and Viraj Adduru and Sadid A. Hasan and Kathy Lee and Ashequl Qadir and Yuan Ling and Aaditya Prakash and Oladimeji Farri},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Open domain real-time question answering based on asynchronous multiperspective context-driven retrieval and neural paraphrasing},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/prna-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DatlaALAHLQLPF17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CMU OAQA at TREC 2017 LiveQA: A Neural Dual Entailment Approach  for Question Paraphrase Identification

_Di Wang, Eric Nyberg_

- :fontawesome-solid-user-group: **Participant:** [CMU-OAQA](./qa/participants.md#cmu-oaqa)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/CMU-OAQA-QA.pdf](https://trec.nist.gov/pubs/trec26/papers/CMU-OAQA-QA.pdf)
- :material-file-search: **Runs:** [CMUOAQA](./qa/runs.md#cmuoaqa)

??? abstract "Abstract"
	
	In this paper, we present CMU's question answering system that was evaluated in the TREC 2017 LiveQA Challenge. Our overall approach this year is similar to the one used in 2015 and 2016. This system answers real-user submitted questions from Yahoo! Answers website and medical questions, which involves retrieving relevant web pages, extracting answer candidate texts, ranking and selecting final answer text. The main improvement this year is the introduction of our new question paraphrase identification module based on a neural dual entailment model. The model uses bidirectional recurrent neural network to encode the premise question into phrase vectors, and then align corresponding phrase vectors from the candidate question with the attention mechanism. The final similarity score is produced based on aggregated phrase-wise comparisons of both entailment directions. In the TREC 2017 LiveQA evaluations, human assessors gave our system an average score of 1.139 on a three-point scale and the median score was 0.777 for all the systems evaluated. Overall, our approach received the highest average scores among automatic systems in main tasks of 2015, 2016 and 2017, and also the highest average score in the new medical subtask of 2017.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WangN17.bib) "
	```
	@inproceedings{DBLP:conf/trec/WangN17,
		author = {Di Wang and Eric Nyberg},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{CMU} {OAQA} at {TREC} 2017 LiveQA: {A} Neural Dual Entailment Approach for Question Paraphrase Identification},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/CMU-OAQA-QA.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WangN17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Real-time Summarization 

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

- :fontawesome-solid-user-group: **Participant:** [IRIT](./rts/participants.md#irit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/IRIT-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/IRIT-RT.pdf)
- :material-file-search: **Runs:** [IRIT-RunB1](./rts/runs.md#irit-runb1) | [IRIT-RunB2](./rts/runs.md#irit-runb2) | [IRIT-RunB3](./rts/runs.md#irit-runb3) | [IRIT-Run1-A](./rts/runs.md#irit-run1-a) | [IRIT-Run2-A](./rts/runs.md#irit-run2-a) | [IRIT-Run3-A](./rts/runs.md#irit-run3-a)

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

- :fontawesome-solid-user-group: **Participant:** [SOIC](./rts/participants.md#soic)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/SOIC-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/SOIC-RT.pdf)
- :material-file-search: **Runs:** [IUB](./rts/runs.md#iub) | [SOIC-Run1-A](./rts/runs.md#soic-run1-a)

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

- :fontawesome-solid-user-group: **Participant:** [NOVASearch](./rts/participants.md#novasearch)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/NOVASearch-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/NOVASearch-RT.pdf)
- :material-file-search: **Runs:** [NOVASearchB1](./rts/runs.md#novasearchb1) | [NOVASearchB2](./rts/runs.md#novasearchb2) | [NOVASearchB3](./rts/runs.md#novasearchb3)

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

- :fontawesome-solid-user-group: **Participant:** [HLJIT](./rts/participants.md#hljit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/HLJIT-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/HLJIT-RT.pdf)
- :material-file-search: **Runs:** [qFB_url](./rts/runs.md#qfb_url) | [HLJIT_l2r](./rts/runs.md#hljit_l2r) | [HLJIT_rank_svm](./rts/runs.md#hljit_rank_svm) | [testRun1-A](./rts/runs.md#testrun1-a) | [testRun2-A](./rts/runs.md#testrun2-a) | [testRun3-A](./rts/runs.md#testrun3-a)

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

- :fontawesome-solid-user-group: **Participant:** [IRIT](./rts/participants.md#irit)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/IRIT2-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/IRIT2-RT.pdf)
- :material-file-search: **Runs:** [IRIT-RunB1](./rts/runs.md#irit-runb1) | [IRIT-RunB2](./rts/runs.md#irit-runb2) | [IRIT-RunB3](./rts/runs.md#irit-runb3) | [IRIT-Run1-A](./rts/runs.md#irit-run1-a) | [IRIT-Run2-A](./rts/runs.md#irit-run2-a) | [IRIT-Run3-A](./rts/runs.md#irit-run3-a)

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

- :fontawesome-solid-user-group: **Participant:** [prna](./rts/participants.md#prna)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/prna-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/prna-RT.pdf)
- :material-file-search: **Runs:** [PRNA-B1](./rts/runs.md#prna-b1) | [PRNA-B2](./rts/runs.md#prna-b2) | [PRNA-B3](./rts/runs.md#prna-b3) | [PRNA-A1-A](./rts/runs.md#prna-a1-a) | [PRNA-A2-A](./rts/runs.md#prna-a2-a) | [PRNA-A3-A](./rts/runs.md#prna-a3-a)

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

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./rts/participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/udel_fang-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/udel_fang-RT.pdf)
- :material-file-search: **Runs:** [UDInfoJac](./rts/runs.md#udinfojac) | [UDInfoW2VPre](./rts/runs.md#udinfow2vpre) | [UDInfoW2VTWT](./rts/runs.md#udinfow2vtwt) | [UDInfoBL-A](./rts/runs.md#udinfobl-a) | [UDInfoEXP-A](./rts/runs.md#udinfoexp-a) | [UDInfoSDWR-A](./rts/runs.md#udinfosdwr-a)

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

- :fontawesome-solid-user-group: **Participant:** [BJUT](./rts/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/BJUT-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/BJUT-RT.pdf)
- :material-file-search: **Runs:** [bjutg](./rts/runs.md#bjutg) | [bjutgs](./rts/runs.md#bjutgs) | [bjut_tmg](./rts/runs.md#bjut_tmg) | [BL1-A](./rts/runs.md#bl1-a) | [BL2-A](./rts/runs.md#bl2-a) | [BL3-A](./rts/runs.md#bl3-a)

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

- :fontawesome-solid-user-group: **Participant:** [advanse_lirmm](./rts/participants.md#advanse_lirmm)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/advanse_lirmm-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/advanse_lirmm-RT.pdf)
- :material-file-search: **Runs:** [adv_lirmm-Run1](./rts/runs.md#adv_lirmm-run1) | [adv_lirmm-Run2](./rts/runs.md#adv_lirmm-run2) | [adv_lirmm-Run3](./rts/runs.md#adv_lirmm-run3) | [advanse_lirmm-Run1-A](./rts/runs.md#advanse_lirmm-run1-a) | [advanse_lirmm-Run2-A](./rts/runs.md#advanse_lirmm-run2-a) | [advanse_lirmm-Run3-A](./rts/runs.md#advanse_lirmm-run3-a)

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

- :fontawesome-solid-user-group: **Participant:** [QU](./rts/participants.md#qu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/QU-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/QU-RT.pdf)
- :material-file-search: **Runs:** [QUBaseline-A](./rts/runs.md#qubaseline-a) | [QUExpDyn-A](./rts/runs.md#quexpdyn-a) | [QUExp-A](./rts/runs.md#quexp-a)

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

- :fontawesome-solid-user-group: **Participant:** [PKUICST](./rts/participants.md#pkuicst)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/PKUICST-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/PKUICST-RT.pdf)
- :material-file-search: **Runs:** [PKUICSTRunB1](./rts/runs.md#pkuicstrunb1) | [PKUICSTRunB2](./rts/runs.md#pkuicstrunb2) | [PKUICSTRunB3](./rts/runs.md#pkuicstrunb3) | [PKUICSTRunA1-A](./rts/runs.md#pkuicstruna1-a) | [PKUICSTRunA2-A](./rts/runs.md#pkuicstruna2-a) | [PKUICSTRunA3-A](./rts/runs.md#pkuicstruna3-a)

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

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./rts/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ICTNET-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/ICTNET-RT.pdf)
- :material-file-search: **Runs:** [ICTNET-Run1](./rts/runs.md#ictnet-run1) | [ICTNET-Run2](./rts/runs.md#ictnet-run2) | [ICTNET-Run3](./rts/runs.md#ictnet-run3) | [ICTNET-run1-A](./rts/runs.md#ictnet-run1-a) | [ICTNET-run2-A](./rts/runs.md#ictnet-run2-a) | [ICTNET-run3-A](./rts/runs.md#ictnet-run3-a)

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

- :fontawesome-solid-user-group: **Participant:** [S.T](./rts/participants.md#s.t)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/S.T-RT.pdf](https://trec.nist.gov/pubs/trec26/papers/S.T-RT.pdf)
- :material-file-search: **Runs:** [SHNU_run1](./rts/runs.md#shnu_run1) | [SHNU_run2](./rts/runs.md#shnu_run2) | [SHNU_run3](./rts/runs.md#shnu_run3) | [SHNU_run1-A](./rts/runs.md#shnu_run1-a) | [SHNU_run2-A](./rts/runs.md#shnu_run2-a) | [SHNU_run3-A](./rts/runs.md#shnu_run3-a)

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

## Complex Answer Retrieval 

#### TREC Complex Answer Retrieval Overview

_Laura Dietz, Manisha Verma, Filip Radlinski, Nick Craswell_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-CAR.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-CAR.pdf)
??? abstract "Abstract"
	
	The SWIRL 2012 workshop on frontiers, challenges, and opportunities for information retrieval report [1] noted many important challenges. Among them, challenges such as conversational answer retrieval, sub-document retrieval, and answer aggregation share commonalities: We desire answers to complex needs, and wish to find them in a single and well-presented source. Advancing the state of the art in this area is the goal of this TREC track. Consider a user investigating a new and unfamiliar topic. This user would often be best served with a single summary, rather than being required to synthesize his or her own summary from multiple sources. This is especially the case in mobile environments with restricted interaction capabilities. While these have led to extensive work on finding the best short answer, the target in this track is the retrieval of comprehensive answers that are composed of multiple text fragments from multiple sources. Retrieving high-quality longer answers is challenging as it is not sufficient to choose a lower rank-cutoff with the same techniques as for short answers. Instead, we need new approaches for finding relevant information in a complex answer space. Many examples of manually created complex answers exist on the Web. Famous examples are articles from how-stuff-works.com, travel guides, or fanzines. These are collections of articles, that each constitutes a long answer to an information need represented by the title of the article. The fundamental task of collecting references, facts, and opinions into a single coherent summary has traditionally been a manual process. We envision that automated information retrieval systems can relieve users from a large amount of manual work through sub-document retrieval, consolidation and organization. Ultimately, the goal is to retrieve synthesized information rather than documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DietzVRC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/DietzVRC17,
		author = {Laura Dietz and Manisha Verma and Filip Radlinski and Nick Craswell},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} Complex Answer Retrieval Overview},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-CAR.pdf},
		timestamp = {Tue, 21 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DietzVRC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at TREC2017 Complex Answer Retrieval Track

_Rui Cheng, Xiaomin Zhuang, Hao Yan, Yuanhai Xue, Zhihua Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./car/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ICTNET-CAR.pdf](https://trec.nist.gov/pubs/trec26/papers/ICTNET-CAR.pdf)
- :material-file-search: **Runs:** [treccarict](./car/runs.md#treccarict)

??? abstract "Abstract"
	
	Information retrieval (IR) is finding material (usually documents) of an unstructured nature (usually text) that satisfies an information need from within large collections (usually stored on computers) [1]. The most common and popular information retrieval application is web search engine such as Google[2], Baidu[3], Bing[4] and Sogou[5]. These application will return top-N best retrieval result to users. Information Retrieval systems for the Web, i.e., web search engines, are mainly devoted to finding relevant web documents in response to a user's query[6]. Current retrieval systems performance well in phrase-level retrieval tasks which provide simple fact and entity-centric needs. Complex Answer Retrieval Track is a new track in 2017, which requests a more complex and longer retrieval result to answer a query. It focuses on developing systems that are capable of answering complex information needs by collating relevant information from an entire corpus. Given an article stub Q, retrieval for each of its sections Hi, a ranking of relevant entity-passage tuples (E, P). Tow tasks are offered: passage ranking and entity ranking. This paper introduces an algorithm and a system for passage ranking. The retrieval queries are outlines which consist of titles and section titles of articles. The retrieval collection consists of paragraphs which are come from Wikipedia articles. We use the BM25 algorithm and develop a system to retrieval the top-100 most relevant paragraphs
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChengZYXYLC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChengZYXYLC17,
		author = {Rui Cheng and Xiaomin Zhuang and Hao Yan and Yuanhai Xue and Zhihua Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at {TREC2017} Complex Answer Retrieval Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/ICTNET-CAR.pdf},
		timestamp = {Fri, 19 May 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ChengZYXYLC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Contextualized PACRR for Complex Answer Retrieval

_Sean MacAvaney, Andrew Yates, Kai Hui_

- :fontawesome-solid-user-group: **Participant:** [MPIID5](./car/participants.md#mpiid5)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/MPIID5-CAR.pdf](https://trec.nist.gov/pubs/trec26/papers/MPIID5-CAR.pdf)
- :material-file-search: **Runs:** [mpii-nn6_pos_tprob](./car/runs.md#mpii-nn6_pos_tprob) | [mpii-nn4_pos_hperc](./car/runs.md#mpii-nn4_pos_hperc) | [mpii-nn6_pos](./car/runs.md#mpii-nn6_pos)

??? abstract "Abstract"
	
	In this work, we present our submission to the TREC Complex Answer Retrieval (CAR) task. Our approach uses a variation of the Position-Aware Convolutional Recurrent Relevance Matching (PACRR) [2] deep neural model to re-rank passages. Modifications include an expanded convolutional kernel size, and contextual vectors to capture heading type (e.g. title), heading frequency, and query term occurrence frequency. We submitted three runs for human relevance judgments by TREC varying which contextual vectors are included, and the number of negative samples used when training. Our approach yields a MAP of 0.241, R-Prec of 0.321, and MRR of 0.520 when using the term occurrence frequency run in the lenient evaluation environment.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacAvaneyYH17.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacAvaneyYH17,
		author = {Sean MacAvaney and Andrew Yates and Kai Hui},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Contextualized {PACRR} for Complex Answer Retrieval},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/MPIID5-CAR.pdf},
		timestamp = {Tue, 15 Mar 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacAvaneyYH17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UTD HLTRI at TREC 2017: Complex Answer Retrieval Track

_Ramón Maldonado, Stuart J. Taylor, Sanda M. Harabagiu_

- :fontawesome-solid-user-group: **Participant:** [UTDHLTRI](./car/participants.md#utdhltri)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/UTDHLTRI-CAR.pdf](https://trec.nist.gov/pubs/trec26/papers/UTDHLTRI-CAR.pdf)
- :material-file-search: **Runs:** [UTDHLTRINN20](./car/runs.md#utdhltrinn20) | [UTDHLTRINN50](./car/runs.md#utdhltrinn50) | [UTDHLTRIAR](./car/runs.md#utdhltriar)

??? abstract "Abstract"
	
	This paper presents our Complex Answer PAragraph Retrieval (CAPAR) system designed for our participation in the TREC Complex Answer Retrieval (CAR) track. Because we were provided with a massive training set consisting of complex questions as well as the paragraphs that answered each aspect of the complex question, we cast the paragraph ranking as a learning to rank (L2R) problem, such that we can produce optimal results at testing time. We considered two alternative Learning to Rank (L2R) approaches for obtaining the relevance scores of each paragraph: (1) the Siamese Attention Network (SANet) for Pairwise Ranking and (2) AdaRank. The evaluation results obtained for CAPAR revealed that the Siamese Attention Network (SANet) for Pairwise Ranking outperformed AdaRank as the L2R approach for CAPAR.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaldonadoTH17.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaldonadoTH17,
		author = {Ram{\'{o}}n Maldonado and Stuart J. Taylor and Sanda M. Harabagiu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{UTD} {HLTRI} at {TREC} 2017: Complex Answer Retrieval Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/UTDHLTRI-CAR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MaldonadoTH17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Tasks 

#### TREC 2017 Tasks Track Overview

_Evangelos Kanoulas, Emine Yilmaz, Rishabh Mehrotra, Ben Carterette, Nick Craswell, Peter Bailey_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-T.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-T.pdf)
??? abstract "Abstract"
	
	Research in Information Retrieval has traditionally focused on serving the best results for a single query, ignoring the reasons (or the task) that might have motivated the user to submit that query. Often times search engines are used to complete complex tasks; achieving these tasks with current search engines requires users to issue multiple queries. For example, booking travel to a location such as London could require the user to submit various queries such as flights to London, hotels in London, points of interest around London, etc. Standard evaluation mechanisms focus on evaluating the quality of a retrieval system in terms of the topical relevance of the results retrieved, completely ignoring the fact that user satisfaction mainly depends on the usefulness of the system in helping the user complete the actual task that led the user issue the query. The TREC Tasks Track is an attempt in devising mechanisms for evaluating quality of retrieval systems in terms of (1) how well they can understand the underlying task that led the user submit a query, and (2) how useful they are for helping users complete their tasks. A number of application areas, beyond task-based retrieval, could benefit from such an evaluation framework and the constructed test collections, including, but not limited to, digital assistants tasks, query suggestions, session-based retrieval, exploratory search, entity-based search. In this paper, we first summarize the three categories of evaluation mechanisms used in the track and briefly describe the corpus, topics, and tasks that comprise the test collection. We then give an overview of the runs submitted to the 2017 Tasks Track and present the evaluation results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KanoulasYMCCB17.bib) "
	```
	@inproceedings{DBLP:conf/trec/KanoulasYMCCB17,
		author = {Evangelos Kanoulas and Emine Yilmaz and Rishabh Mehrotra and Ben Carterette and Nick Craswell and Peter Bailey},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2017 Tasks Track Overview},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-T.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KanoulasYMCCB17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Siena's Tasks Track System

_Emily Barranca, Sharon Gower Small_

- :fontawesome-solid-user-group: **Participant:** [SienaCLTeam](./task/participants.md#sienaclteam)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/SienaCLTeam-T.pdf](https://trec.nist.gov/pubs/trec26/papers/SienaCLTeam-T.pdf)
- :material-file-search: **Runs:** [SienaCLTeamRun1](./task/runs.md#sienaclteamrun1) | [SienaCLTeamRun2](./task/runs.md#sienaclteamrun2)

??? abstract "Abstract"
	
	This paper discusses our development of Siena's Tasks Track System (STTS) and its participation in the Tasks Track of the 2017 Text Retrieval Conference (TREC). The purpose of this track is to try to understand the underlying task a user might be trying to complete when searching a specific query. The Task Understanding portion of this task aimed to find a list of up to 100 keywords and phrases that might be related to a user's task given the example query. In the first year of our work in this track we submitted two fairly simple runs. In the first run, we used the jsoup library to run these queries through Google and processed the first five documents resulting from the search. We automatically extracted keywords and phrases that appeared commonly across the documents. In the second run we utilized Wordnet to generate new words and phrases to augment the query. These two methods, the Wordnet approach and the Google approach were submitted as two separate runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BarrancaS17.bib) "
	```
	@inproceedings{DBLP:conf/trec/BarrancaS17,
		author = {Emily Barranca and Sharon Gower Small},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Siena's Tasks Track System},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/SienaCLTeam-T.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BarrancaS17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BJUT at TREC 2017: Tasks Track

_Lupu Li, Guangyuan Zhang, Zhen Yang_

- :fontawesome-solid-user-group: **Participant:** [BJUT](./task/participants.md#bjut)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/BJUT-T.pdf](https://trec.nist.gov/pubs/trec26/papers/BJUT-T.pdf)
- :material-file-search: **Runs:** [BJUT_1](./task/runs.md#bjut_1) | [BJUT_2](./task/runs.md#bjut_2)

??? abstract "Abstract"
	
	We generally evaluate the quality of task based information retrieval system from two aspects: task understanding and task completion. To evaluate the quality of task understanding, we need a list of sub-tasks that provide a complete coverage of tasks for each query. Finding a way to get a list like that for every query is our target. So, this paper explored the viable approach to achieve it and analyzed experimental results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiZY17.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiZY17,
		author = {Lupu Li and Guangyuan Zhang and Zhen Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{BJUT} at {TREC} 2017: Tasks Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/BJUT-T.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiZY17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## Dynamic Domain 

#### TREC 2017 Dynamic Domain Track Overview

_Grace Hui Yang, Zhiwen Tang, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-DD.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-DD.pdf)
??? abstract "Abstract"
	
	The goal of dynamic domain track is promoting the research of dynamic, exploratory search within complex information domains, where the search process is usually interactive and user's information need is also complex. Dynamic Domain (DD) track has been held in the past three years. This track's name includes two parts. “Dynamic” means the search process may contain multiple runs of iteration, and the participating system is expected to adapt its search algorithm based on the relevance feedback. “Domain” means the search task focuses on special domains, where user's information need consists of multiple aspects, and the participating system is expected to help the user explore the domain through rich interaction. This task has received great attention and this track is inspired by interested groups in government, including DARPA MEMEX program. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangTS17.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangTS17,
		author = {Grace Hui Yang and Zhiwen Tang and Ian Soboroff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2017 Dynamic Domain Track Overview},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangTS17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMD_CLIP: Using Relevance Feedback to Find Diverse Documents for  TREC Dynamic Domain 2017

_Kristine M. Rogers, Douglas W. Oard_

- :fontawesome-solid-user-group: **Participant:** [UMD_CLIP](./domain/participants.md#umd_clip)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/umd_clip-DD.pdf](https://trec.nist.gov/pubs/trec26/papers/umd_clip-DD.pdf)
- :material-file-search: **Runs:** [clip_baseline](./domain/runs.md#clip_baseline) | [clip_addwords](./domain/runs.md#clip_addwords) | [clip_filter](./domain/runs.md#clip_filter)

??? abstract "Abstract"
	
	The University of Maryland's participation in TREC's 2017 Dynamic Domain track focused on two types of experiments: adding new terms from passages judged as being relevant, and exclusion of terms from documents that the track's jig feedback system indicated were not relevant to the topic. The best results for iterative multi-step retrieval were obtained by restricting retrieval to documents that contained all topic terms, and then ranking those documents using terms extracted from known relevant passages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RogersO17.bib) "
	```
	@inproceedings{DBLP:conf/trec/RogersO17,
		author = {Kristine M. Rogers and Douglas W. Oard},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {UMD{\_}CLIP: Using Relevance Feedback to Find Diverse Documents for {TREC} Dynamic Domain 2017},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/umd\_clip-DD.pdf},
		timestamp = {Sun, 14 May 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/RogersO17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Reinforcement Learning Approach for Dynamic Search

_Zhiwen Tang, Grace Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [georgetown](./domain/participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/georgetown-DD.pdf](https://trec.nist.gov/pubs/trec26/papers/georgetown-DD.pdf)
- :material-file-search: **Runs:** [galago_baseline](./domain/runs.md#galago_baseline) | [dqn_5_actions](./domain/runs.md#dqn_5_actions) | [dqn_semantic_state](./domain/runs.md#dqn_semantic_state)

??? abstract "Abstract"
	
	TREC Dynamic Domain (DD) track is intended to support the research in dynamic, exploratory search within complex domains. It simulates an interactive search process where the search system is expected to improve its efficiency and effectiveness based on its interaction with the user. We propose to model the dynamic search as a reinforcement learning problem and use neural network to find the best policy during a search process. We show a great potential of deep reinforcement learning on DD track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TangY17.bib) "
	```
	@inproceedings{DBLP:conf/trec/TangY17,
		author = {Zhiwen Tang and Grace Hui Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Reinforcement Learning Approach for Dynamic Search},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/georgetown-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TangY17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at TREC 2017 Dynamic Domain Track

_Weimin Zhang, Yaokang Hu, Rongqian Jia, Xianfa Wang, Le Zhang, Yue Feng, Sihao Yu, Yuanhai Xue, Xiaoming Yu, Yue Liu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./domain/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ICTNET-DD.pdf](https://trec.nist.gov/pubs/trec26/papers/ICTNET-DD.pdf)
- :material-file-search: **Runs:** [ictnet_div_qe](./domain/runs.md#ictnet_div_qe) | [ictnet_emulti](./domain/runs.md#ictnet_emulti) | [ictnet_fom_itr1](./domain/runs.md#ictnet_fom_itr1) | [ictnet_params1_s](./domain/runs.md#ictnet_params1_s) | [ictnet_params2_ns](./domain/runs.md#ictnet_params2_ns)

??? abstract "Abstract"
	
	This track focuses on interactive search algorithms that adapt to the dynamic information needs of professional users as they explore in complex domains. [1] Unlike the common retrieval, there are two different aspects in TREC Dynamic Domain task, that we need to interact with users and retrieve in a speci c data set. The JIG program acts as users' feedback, then we use the feedback to expand the query, the different subtopics of the user feedback information are also used for the result diversi cation algorithm. In addition, we also tried to integrate a variety of ranking algorithms and deal with some detail issues. Five solutions using the above algorithm were submitted. In those submissions, one combined Suggested Queries and JIG feedback [2], one didn't use stop strategy, the others all based on the same algorithm, but with different argumentstending to improve CT or ACT.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangHJWZFYXYLC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangHJWZFYXYLC17,
		author = {Weimin Zhang and Yaokang Hu and Rongqian Jia and Xianfa Wang and Le Zhang and Yue Feng and Sihao Yu and Yuanhai Xue and Xiaoming Yu and Yue Liu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at {TREC} 2017 Dynamic Domain Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/ICTNET-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangHJWZFYXYLC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

## OpenSearch 

#### Overview of TREC OpenSearch 2017

_Rolf Jagerman, Krisztian Balog, Philipp Schaer, Johann Schaible, Narges Tavakolpoursaleh, Maarten de Rijke_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Overview-O.pdf](https://trec.nist.gov/pubs/trec26/papers/Overview-O.pdf)
??? abstract "Abstract"
	
	In this paper we provide an overview of the TREC 2017 OpenSearch track. The OpenSearch track provides researchers the opportunity to have their retrieval approaches evaluated in a live setting with real users. We focus on the academic search domain with the Social Science Open Access Repository (SSOAR) search engine and report our results.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JagermanBSSTR17.bib) "
	```
	@inproceedings{DBLP:conf/trec/JagermanBSSTR17,
		author = {Rolf Jagerman and Krisztian Balog and Philipp Schaer and Johann Schaible and Narges Tavakolpoursaleh and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Overview of {TREC} OpenSearch 2017},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/Overview-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JagermanBSSTR17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FEUP at TREC 2017 OpenSearch Track Graph-Based Models for Entity-Oriented

_José Luís Devezas, Carla Teixeira Lopes, Sérgio Nunes_

- :fontawesome-solid-user-group: **Participant:** [FEUP](./open/participants.md#feup)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/FEUP-O.pdf](https://trec.nist.gov/pubs/trec26/papers/FEUP-O.pdf)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2017 OpenSearch Track, where we explored graph-based approaches for document representation and retrieval. We tackled the problem as an entity-oriented search task over the SSOAR site (Social Science Open Access Repository), using the title and the abstract as a text block and the remaining metadata as a knowledge block. Our main goal for this edition was to compare the graph-of-word, a text-only representation, with the graph-of-entity, a combined data representation that we are working on. The proposal is that, by combining text and knowledge through a unified representation, we will be able to unlock novel weighting strategies capable of harnessing all available information and ultimately improving retrieval effectiveness. Unfortunately, due to a technical problem with the OpenSearch track infrastructure, we were unable to obtain feedback for the real round during August 2017. As an alternative, we were offered the opportunity to participate in a third extraordinary round, happening during October 2017, as well as available feedback from the period between the two official rounds, at the end of July 2017. We obtained an outcome of 0.375 for the graph-of-word and 0.167 for the graph-of-entity, based on only 29 impressions with clicks, out of a total of 4,683 impressions. According to this small number of clicked impressions, both models performed below the site's native search, with graph-of-entity performing below graph-of-word.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DevezasLN17.bib) "
	```
	@inproceedings{DBLP:conf/trec/DevezasLN17,
		author = {Jos{\'{e}} Lu{\'{\i}}s Devezas and Carla Teixeira Lopes and S{\'{e}}rgio Nunes},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{FEUP} at {TREC} 2017 OpenSearch Track Graph-Based Models for Entity-Oriented},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/FEUP-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DevezasLN17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IR-Cologne at TREC 2017 OpenSearch Track: Rerunning Popularity Ranking  Experiments in a Living Lab

_Narges Tavakolpoursaleh, Mandy Neumann, Philipp Schaer_

- :fontawesome-solid-user-group: **Participant:** [IR-Cologne](./open/participants.md#ir-cologne)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/IR-Cologne-O.pdf](https://trec.nist.gov/pubs/trec26/papers/IR-Cologne-O.pdf)
- :material-file-search: **Runs:** [Gesis](./open/runs.md#gesis)

??? abstract "Abstract"
	
	In this paper, we will present our work on popularity-based relevance ranking within the SSOAR open access repository system where we reused a popularity data-driven ranking approach. We applied the same normalization method as last year, namely the Characteristic Scores and Scale Method (CSS). Our main focus was to test if we could reproduce the results of last year's track. We, therefore, see this work not as a sole engineering task to produce the best possible popularity ranking method for scientific literature but as a test bed for reproducibility experiments in the domain of living labs. The TREC 2016 OpenSearch track was focused on ad-hoc search for scientific literature and three scientific search engines and document repositories were part of this living lab-centered evaluation campaign: (1) CiteSeerX, (2) Microsoft Academic Search, and (3) SSOAR - Social Science Open Access Repository. From these three only SSOAR remained in this year's OpenSearch track. The first author of this paper is responsible for the implementation of the living lab infrastructure and the LL4IR API that is necessary to include an online system into the OpenSearch evaluation campaign. This work is based on her Master's thesis at University of Bonn [8]. Details of the implementation are described in the two overview papers of the OpenSearch track [1,3].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tavakolpoursaleh17.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tavakolpoursaleh17,
		author = {Narges Tavakolpoursaleh and Mandy Neumann and Philipp Schaer},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {IR-Cologne at {TREC} 2017 OpenSearch Track: Rerunning Popularity Ranking Experiments in a Living Lab},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/IR-Cologne-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tavakolpoursaleh17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ICTNET at TREC2017 OpenSearch Track

_Peng Xu, Long Bai, Suiyuan Zhang, Fang Yang, Zhibin Zhang, Xiaoming Yu, Xiaolong Jin, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [ICTNET](./open/participants.md#ictnet)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/ICTNET-O.pdf](https://trec.nist.gov/pubs/trec26/papers/ICTNET-O.pdf)
- :material-file-search: **Runs:** [ICTNET](./open/runs.md#ictnet)

??? abstract "Abstract"
	
	The OpenSearch track explores The 'Living Labs' evaluation paradigm for IR that involves real users of operational search engines. The task in the track will continue/expand upon the ad hoc Academic Search task of TREC 2016. It is difficult to define who is better in the ranking experimentation, because the real users in the natural environments search a key word with their own purpose. The best way to evaluate two ranks is let the real users make use of them. So TREC 2017 Open Search Track provides this platform which is a new form to assess the ranks good or bad. The Open Search provide the training queries, testing queries and candidates documents, but it did not tell us which document is more relevant to a specific query which is necessary to train our model. So first we need to crawl the rank of all the documents on each query from an existing web search engine. Then we try a serial of features in order to find the relevance between the queries and the documents. And we also designed scoring rules to give each document a score. Finally, we used XGBoost to train models for each training query and then found a way to predict testing data based on the models. Feedback data is the key to this track. We find a simple way to integrate the feedback into our model. Unfortunately, there is so little feedback that can hardly improve the result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuBZYZYJC17.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuBZYZYJC17,
		author = {Peng Xu and Long Bai and Suiyuan Zhang and Fang Yang and Zhibin Zhang and Xiaoming Yu and Xiaolong Jin and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{ICTNET} at {TREC2017} OpenSearch Track},
		booktitle = {Proceedings of The Twenty-Sixth Text REtrieval Conference, {TREC} 2017, Gaithersburg, Maryland, USA, November 15-17, 2017},
		series = {{NIST} Special Publication},
		volume = {500-324},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2017},
		url = {https://trec.nist.gov/pubs/trec26/papers/ICTNET-O.pdf},
		timestamp = {Thu, 13 Jan 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuBZYZYJC17.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2017: Open Search and Core Tracks

_Matthias Hagen, Yamen Ajjour, Johannes Kiesel, Payam Adineh, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./open/participants.md#webis)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec26/papers/Webis-O-CC.pdf](https://trec.nist.gov/pubs/trec26/papers/Webis-O-CC.pdf)
- :material-file-search: **Runs:** [Webis](./open/runs.md#webis)

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

