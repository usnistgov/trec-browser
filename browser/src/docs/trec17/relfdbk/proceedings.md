# Proceedings - Relevance Feedback 2008 

#### Relevance Feedback Track Overview: TREC 2008

_Chris Buckley, Stephen Robertson_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec17/papers/REL.FDBK.OVERVIEW.pdf](https://trec.nist.gov/pubs/trec17/papers/REL.FDBK.OVERVIEW.pdf)
??? abstract "Abstract"
	
	Relevance Feedback has been one of the successes of information retrieval research for the past 30 years. It has been proven to be worthwhile in a wide variety of settings, both when actual user feedback is available, and when the user feedback is implicit. However, while the applications of relevance feedback and type of user input to relevance feedback have changed over the years, the actual algorithms have not changed much. Most algorithms are either pure statistical word based (for example, Rocchio or Language Modeling), or are domain dependent. We should be able to do better now, but there have been surprisingly few advances in the area. In part, that's because relevance feedback is hard to study, evaluate, and compare. It is difficult to separate out the effects of an initial retrieval run, the decision procedure to determine what documents will be looked at, the user dependent relevance judgment procedure (including interface), and the actual relevance feedback reformulation algorithm. Setting up a framework to look at these separate effects for future research is an important goal for this track. Why now? We have a lot more natural language tools than we had 10 or 20 years ago. We're hopeful we can get people to actually use those tools to suggest what makes a document relevant or non-relevant to a particular topic. The question-answering community has been very successful at categorizing questions and taking different approaches for different categories. The success has not transferred over to the IR task, partly because there simply isn't enough syntactic information in a typical IR topic to offer clues as to what is wanted. But given relevant and non-relevant judgments, it should be much easier to form categories for topics (e.g., this topic requires these two aspects to both be present, while this other topic does not), and take different approaches depending on topic. Relevance feedback is an area that's ripe for major advances, and is being held back because there isn't a common methodology for investigating and comparing relevance feedback algorithms. This track establishes that methodology, and offers groups the ability to evaluate and compare their relevance feedback algorithms.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BuckleyR08.bib) "
	```
	@inproceedings{DBLP:conf/trec/BuckleyR08,
		author = {Chris Buckley and Stephen Robertson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Relevance Feedback Track Overview: {TREC} 2008},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {https://trec.nist.gov/pubs/trec17/papers/REL.FDBK.OVERVIEW.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BuckleyR08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Iowa at TREC 2008 Legal and Relevance FeedbackTracks

_Brian Almquist, Yelena Mejova, Viet Ha-Thuc, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [UIowa-Srinivasan](./participants.md#uiowa-srinivasan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uiowa.legal.rf.pdf](http://trec.nist.gov/pubs/trec17/papers/uiowa.legal.rf.pdf)
- :material-file-search: **Runs:** [IowaSRF08.A1](./runs.md#iowasrf08.a1) | [IowaSRF08.B1](./runs.md#iowasrf08.b1) | [IowaSRF08.C1](./runs.md#iowasrf08.c1) | [IowaSRF08.D1](./runs.md#iowasrf08.d1) | [IowaSRF08.E1](./runs.md#iowasrf08.e1)

??? abstract "Abstract"
	
	The University of Iowa Team, coordinated by Padmini Srinivasan, participated in the legal discovery and relevance feedback tracks of TREC-2008. This is our second year participating in the legal track and the first year in the relevance feedback track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AlmquistMHS08.bib) "
	```
	@inproceedings{DBLP:conf/trec/AlmquistMHS08,
		author = {Brian Almquist and Yelena Mejova and Viet Ha{-}Thuc and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Iowa at {TREC} 2008 Legal and Relevance FeedbackTracks},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uiowa.legal.rf.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AlmquistMHS08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FUB at TREC 2008 Relevance Feedback Track: Extending Rocchio with  Distributional Term Analysis

_Andrea Bernardini, Claudio Carpineto_

- :fontawesome-solid-user-group: **Participant:** [fub](./participants.md#fub)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/fondazione.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/fondazione.rf.rev.pdf)
- :material-file-search: **Runs:** [FubRF08.A1](./runs.md#fubrf08.a1) | [FubRF08.B1](./runs.md#fubrf08.b1) | [FubRF08.D1](./runs.md#fubrf08.d1) | [FubRF08.E1](./runs.md#fubrf08.e1) | [FubRF08.C1](./runs.md#fubrf08.c1) | [FubRF08.A2](./runs.md#fubrf08.a2) | [FubRF08.E2](./runs.md#fubrf08.e2) | [FubRF08.C2](./runs.md#fubrf08.c2) | [FubRF08.D2](./runs.md#fubrf08.d2)

??? abstract "Abstract"
	
	The main goals of our participation in the Relevance feedback track at TREC 2008 were the following. Test the effectiveness of using a combination of Rocchio and distributional term analysis on a relevance feedback task; so far, this approach has usually been used (with good results) in a pseudo-relevance setting.; Test whether and when negative relevance feedback is useful; e.g., is negative relevance feedback most effective when the distribution of terms in the negative documents is different than the distribution in the positive documents?; Study how the performance of relevance feedback varies as the size of the set of feedback documents grows.; Check if /how the performance of relevance feedback is influenced by the size of the expanded query.; Compare relevance feedback to pseudo-relevance feedback; e.g, is relevance feedback not only more effective but also more robust than pseudo-relevance feedback?
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BernardiniC08.bib) "
	```
	@inproceedings{DBLP:conf/trec/BernardiniC08,
		author = {Andrea Bernardini and Claudio Carpineto},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FUB} at {TREC} 2008 Relevance Feedback Track: Extending Rocchio with Distributional Term Analysis},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/fondazione.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BernardiniC08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2008 Blog Track

_Jianmei Chen, Wei Guo, Fengming Pan, Fuyang Chang, Rui Song, Hongfei Lin_

- :fontawesome-solid-user-group: **Participant:** [DUTIR](./participants.md#dutir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/dalianu.rf.pdf](http://trec.nist.gov/pubs/trec17/papers/dalianu.rf.pdf)
- :material-file-search: **Runs:** [DUTIRRF08.A1](./runs.md#dutirrf08.a1) | [DUTIRRF08.B1](./runs.md#dutirrf08.b1) | [DUTIRRF08.C1](./runs.md#dutirrf08.c1) | [DUTIRRF08.D1](./runs.md#dutirrf08.d1) | [DUTIRRF08.E1](./runs.md#dutirrf08.e1)

??? abstract "Abstract"
	
	For opinion finding task our method of the combination of 5 Windows method and Pseudo Relevance Feedback behaves well, achieving an improvement of over 20% on the baseline adhoc results. For the polarity task we develop two different methods. One is a classification method, and the other uses queries to retrieve positive and negative documents respectively. In Blog Distillation task, Pseudo Relevance Feedback method helps improve the result a little, however, since its dependence on the top 10 retrieval result, the method still need to be improved in order to get better result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChenGPCSL08.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChenGPCSL08,
		author = {Jianmei Chen and Wei Guo and Fengming Pan and Fuyang Chang and Rui Song and Hongfei Lin},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2008 Blog Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/dalianu.rf.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChenGPCSL08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2008: Experiments in Blog, Enterprise,  and Relevance Feedback Tracks with Terrier

_Ben He, Craig Macdonald, Iadh Ounis, Jie Peng, Rodrygo L. T. Santos_

- :fontawesome-solid-user-group: **Participant:** [UoGtr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf)
- :material-file-search: **Runs:** [uogRF08.A2](./runs.md#uogrf08.a2) | [uogRF08.B2](./runs.md#uogrf08.b2) | [uogRF08.C2](./runs.md#uogrf08.c2) | [uogRF08.B1](./runs.md#uogrf08.b1) | [uogRF08.C1](./runs.md#uogrf08.c1) | [uogRF08.E2](./runs.md#uogrf08.e2) | [uogRF08.D2](./runs.md#uogrf08.d2) | [uogRF08.D1](./runs.md#uogrf08.d1) | [uogRF08.E1](./runs.md#uogrf08.e1) | [uogRF08.A1](./runs.md#uogrf08.a1)

??? abstract "Abstract"
	
	In TREC 2008, we participate in the Blog, Enterprise, and Relevance Feedback tracks. In all tracks, we continue the research and development of the Terrier platform1 centred around extending state-of-the-art weighting models based on the Divergence From Randomness (DFR) framework [26]. In particular, we investigate two main themes, namely, proximity-based models, and collection and profile enrichment techniques based on several resources. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HeMOPS08.bib) "
	```
	@inproceedings{DBLP:conf/trec/HeMOPS08,
		author = {Ben He and Craig Macdonald and Iadh Ounis and Jie Peng and Rodrygo L. T. Santos},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2008: Experiments in Blog, Enterprise, and Relevance Feedback Tracks with Terrier},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uglasgow.blog.ent.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HeMOPS08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Impact of Positive, Negative and Topical Relevance Feedback

_Rianne Kaptein, Jaap Kamps, Djoerd Hiemstra_

- :fontawesome-solid-user-group: **Participant:** [UAmsterdam](./participants.md#uamsterdam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uamsterdam-kapms.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uamsterdam-kapms.rf.rev.pdf)
- :material-file-search: **Runs:** [UAmsR08PD.A1](./runs.md#uamsr08pd.a1) | [UAmsR08PD.B1](./runs.md#uamsr08pd.b1) | [UAmsR08PD.C1](./runs.md#uamsr08pd.c1) | [UAmsR08PD.D1](./runs.md#uamsr08pd.d1) | [UAmsR08PD.E1](./runs.md#uamsr08pd.e1) | [UAmsR08PD.F1](./runs.md#uamsr08pd.f1) | [UAmsR08CJ.B2](./runs.md#uamsr08cj.b2) | [UAmsR08CJ.C2](./runs.md#uamsr08cj.c2) | [UAmsR08CJ.D2](./runs.md#uamsr08cj.d2) | [UAmsR08CJ.E2](./runs.md#uamsr08cj.e2)

??? abstract "Abstract"
	
	This document contains a description of experiments for the 2008 Relevance Feedback track. We experiment with different amounts of feedback, including negative relevance feedback. Feedback is implemented using massive weighted query expansion. Parsimonious query expansion using only relevant documents and Jelinek-Mercer smoothing performs best on this relevance feedback track dataset. Additional blind feedback gives better results, except when the blind feedback set is of the same size as the explicit feedback set. On a small number of topics topical feedback is applied, which turns out to be mainly beneficial for early precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KapteinKH08.bib) "
	```
	@inproceedings{DBLP:conf/trec/KapteinKH08,
		author = {Rianne Kaptein and Jaap Kamps and Djoerd Hiemstra},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Impact of Positive, Negative and Topical Relevance Feedback},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uamsterdam-kapms.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KapteinKH08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Incorporating Relevance and Pseudo-relevance Feedback in the Markov  Random Field Model

_Matthew Lease_

- :fontawesome-solid-user-group: **Participant:** [Brown_University](./participants.md#brown_university)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/brownu.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/brownu.rf.rev.pdf)
- :material-file-search: **Runs:** [Brown.A1](./runs.md#brown.a1) | [Brown.B1](./runs.md#brown.b1) | [Brown.E1](./runs.md#brown.e1) | [Brown.C1](./runs.md#brown.c1) | [Brown.D1](./runs.md#brown.d1) | [Brown.A2](./runs.md#brown.a2) | [Brown.B2](./runs.md#brown.b2) | [Brown.C2](./runs.md#brown.c2) | [Brown.D2](./runs.md#brown.d2)

??? abstract "Abstract"
	
	We present a new document retrieval approach combining relevance feedback, pseudo-relevance feedback, and Markov random field modeling of term interaction. Overall effectiveness of our combined model and the relative contribution from each component is evaluated on the GOV2 webpage collection. Given 0-5 feedback documents, we find each component contributes unique value to the overall ensemble, achieving significant improvement individually and in combination. Comparative evaluation in the 2008 TREC Relevance Feedback track further shows our complete system typically performs as well or better than peer systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lease08.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lease08,
		author = {Matthew Lease},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Incorporating Relevance and Pseudo-relevance Feedback in the Markov Random Field Model},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/brownu.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lease08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Study of Adaptive Relevance Feedback - UIUC TREC 2008 Relevance  Feedback Experiments

_Yuanhua Lv, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [UIUC](./participants.md#uiuc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uillinois-uc.rf.rec.pdf](http://trec.nist.gov/pubs/trec17/papers/uillinois-uc.rf.rec.pdf)
- :material-file-search: **Runs:** [UIUC.A1](./runs.md#uiuc.a1) | [UIUC.B2](./runs.md#uiuc.b2) | [UIUC.C2](./runs.md#uiuc.c2) | [UIUC.B1](./runs.md#uiuc.b1) | [UIUC.C1](./runs.md#uiuc.c1) | [UIUC.D1](./runs.md#uiuc.d1) | [UIUC.E1](./runs.md#uiuc.e1) | [UIUC.E2](./runs.md#uiuc.e2) | [UIUC.D2](./runs.md#uiuc.d2)

??? abstract "Abstract"
	
	In this paper, we report our experiments in the TREC 2008 Relevance Feedback Track. Our main goal is to study a novel problem in feedback, i.e., optimization of the balance of the query and feedback information. Intuitively, if we over-trust the feedback information, we may be biased to favor a particular subset of relevant documents, but undertrusting it would not take advantage of feedback. In the cur- rent feedback methods, the balance is usually controlled by some parameter, which is often set to a fixed value across all the queries and collections. However, due to the difference in queries and feedback documents, this balance parameter should be optimized for each query and each set of feedback documents. To address this problem, we present a learning approach to adaptively predict the balance coefficient (i.e., feedback coefficient). First, three heuristics are proposed to characterize the relationships between feedback coefficient and other measures, including discrimination of query, discrimination of feedback documents, and divergence between the query and the feedback documents. Then, taking these three heuristics as a road map, we explore a number of features and combine them using a logistic regression model to predict the feedback coefficient. Experiments show that our adaptive relevance feedback is more robust and effective than the regular fixed-coefficient relevance feedback.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LvZ08.bib) "
	```
	@inproceedings{DBLP:conf/trec/LvZ08,
		author = {Yuanhua Lv and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Study of Adaptive Relevance Feedback - {UIUC} {TREC} 2008 Relevance Feedback Experiments},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uillinois-uc.rf.rec.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LvZ08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Incorporating Non-Relevance Information in the Estimation of Query  Models

_Edgar Meij, Wouter Weerkamp, Jiyin He, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UAms_De_Rijke](./participants.md#uams_de_rijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.rf.rev.pdf)
- :material-file-search: **Runs:** [uams08bl.A1](./runs.md#uams08bl.a1) | [uams08m6.B1](./runs.md#uams08m6.b1) | [uams08m6.C1](./runs.md#uams08m6.c1) | [uams08m6.D1](./runs.md#uams08m6.d1) | [uams08m6.E1](./runs.md#uams08m6.e1) | [uams08m9.B2](./runs.md#uams08m9.b2) | [uams08m9.C2](./runs.md#uams08m9.c2) | [uams08m9.D2](./runs.md#uams08m9.d2) | [uams08m9.E2](./runs.md#uams08m9.e2) | [uams08bl.A2](./runs.md#uams08bl.a2)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's ILPS group in the relevance feedback track at TREC 2008. We introduce a new model which incorporates information from relevant and non-relevant documents to improve the estimation of query models. Our main findings are twofold: (i) in terms of statMAP, a larger number of judged non-relevant documents improves retrieval effectiveness and (ii) on the TREC Terabyte topics, we can effectively replace the estimates on the judged non-relevant documents with estimations on the document collection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeijWHR08.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeijWHR08,
		author = {Edgar Meij and Wouter Weerkamp and Jiyin He and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Incorporating Non-Relevance Information in the Estimation of Query Models},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/uamsterdam-derijke.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MeijWHR08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2008: Relevance Feedback Track

_Yohannes Tsegay, Falk Scholer, Simon J. Puglisi_

- :fontawesome-solid-user-group: **Participant:** [rmit](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/rmit.rf.pdf](http://trec.nist.gov/pubs/trec17/papers/rmit.rf.pdf)
- :material-file-search: **Runs:** [RMIT08.A1](./runs.md#rmit08.a1) | [RMIT08.B1](./runs.md#rmit08.b1) | [RMIT08.C1](./runs.md#rmit08.c1) | [RMIT08.C2](./runs.md#rmit08.c2) | [RMIT08.D1](./runs.md#rmit08.d1) | [RMIT08.D2](./runs.md#rmit08.d2) | [RMIT08.E1](./runs.md#rmit08.e1) | [RMIT08.E2](./runs.md#rmit08.e2)

??? abstract "Abstract"
	
	This report outlines TREC-2008 Relevance Feedback Track experiments done at RMIT University. Relevance feedback in text retrieval systems is a process where a user gives explicit feedback on an initial set of retrieval results returned by a search system. For example, the user might mark some of the items as being relevant, or not relevant, to their current information need. This feedback can be used in different ways; one approach is query expansion, where terms from the relevant documents are added to the original query, with the aim of improving retrieval effectiveness. This report describes the the query expansion methods that we explored as part of TREC 2008. Our results demonstrate that high weight terms are not always necessarily useful for query expansion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TsegaySP08.bib) "
	```
	@inproceedings{DBLP:conf/trec/TsegaySP08,
		author = {Yohannes Tsegay and Falk Scholer and Simon J. Puglisi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2008: Relevance Feedback Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/rmit.rf.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TsegaySP08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluating a Novel Kind of Retrieval Models Based on Relevance Decision  Making in a Relevance Feedback Environment

_Ho Chung Wu, Edward K. F. Dang, Robert Wing Pong Luk, G. Ngai, Yinghao Li, James Allan, Kui-Lam Kwok, Kam-Fai Wong_

- :fontawesome-solid-user-group: **Participant:** [HKPU](./participants.md#hkpu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/hong-kong.pu.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/hong-kong.pu.rf.rev.pdf)
- :material-file-search: **Runs:** [HKPU.A1](./runs.md#hkpu.a1) | [HKPU.D1](./runs.md#hkpu.d1) | [HKPU.B1](./runs.md#hkpu.b1) | [HKPU.E1](./runs.md#hkpu.e1) | [HKPU.C1](./runs.md#hkpu.c1) | [HKPU.B2](./runs.md#hkpu.b2) | [HKPU.C2](./runs.md#hkpu.c2)

??? abstract "Abstract"
	
	This paper presents the results of our participation in the relevance feedback track using our novel retrieval models. These models simulate human relevance decision-making. For each document location of a query term, information from its document-context at that location determines the relevance decision outcomes there. The relevance values for all documents locations of all query terms in the same document are combined to form the final relevance value for that document. Two probabilistic models are developed, and one of them is directly related to the TF-IDF term weights. Our initial retrieval is a passage-based retrieval. Passage scores of the same document are combined by the Dombi fuzzy disjunction operator. Later, we found that the Markov random field (MRF) model produces better results than our initial retrieval system (without relevance information). If we apply our novel retrieval models using the initial retrieval list of the MRF model, the retrieval effectiveness of our models will be improved. These informal run results using the MRF model used in conjunction with our novel models are also presented.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuDLNLAKW08.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuDLNLAKW08,
		author = {Ho Chung Wu and Edward K. F. Dang and Robert Wing Pong Luk and G. Ngai and Yinghao Li and James Allan and Kui{-}Lam Kwok and Kam{-}Fai Wong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Evaluating a Novel Kind of Retrieval Models Based on Relevance Decision Making in a Relevance Feedback Environment},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/hong-kong.pu.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuDLNLAKW08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Extending Relevance Model for Relevance Feedback

_Le Zhao, Chenmin Liang, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [CMU-LTI-DIR](./participants.md#cmu-lti-dir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/cmu.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/cmu.rf.rev.pdf)
- :material-file-search: **Runs:** [CMURF08.A1](./runs.md#cmurf08.a1) | [CMURF08.B1](./runs.md#cmurf08.b1) | [CMURF08.C1](./runs.md#cmurf08.c1) | [CMURF08.D1](./runs.md#cmurf08.d1) | [CMURF08.D2](./runs.md#cmurf08.d2) | [CMURF08.C2](./runs.md#cmurf08.c2) | [CMURF08.B2](./runs.md#cmurf08.b2) | [CMURF08.E1](./runs.md#cmurf08.e1)

??? abstract "Abstract"
	
	Relevance feedback is the retrieval task where the system is given not only an information need, but also some relevance judgement information, usually from users' feedback for an initial result list by the system. With different amount of feedback information available, the optimal feedback strategy might be very different. In TREC Relevance Feedback task, the system is given different sets of feedback information from 1 relevant document to over 40 judgements with at least 3 relevant. Thus, in this work, we try to develop a feedback algorithm that works well on all levels of feedback by extending the relevance model for pseudo relevance feedback to include judged relevant documents when scoring feedback terms. Within these different levels of feedback, it is more difficult for the feedback algorithm to perform well when given minimal amount of feedback. Experiments show that our algorithm performs robustly in those difficult cases.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoLC08.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoLC08,
		author = {Le Zhao and Chenmin Liang and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Extending Relevance Model for Relevance Feedback},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/cmu.rf.rev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoLC08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2008: Relevance Feedback Track

_Bo Zhou, Qi Fang, Rongwei Cen, Min Zhang, Yiqun Liu, Shaoping Ma_

- :fontawesome-solid-user-group: **Participant:** [THUIR](./participants.md#thuir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec17/papers/tsinghua.rf.rev.pdf](http://trec.nist.gov/pubs/trec17/papers/tsinghua.rf.rev.pdf)
- :material-file-search: **Runs:** [THUFB.D1](./runs.md#thufb.d1) | [THUFB.E1](./runs.md#thufb.e1) | [THUFB.A1](./runs.md#thufb.a1) | [THUFB.B1](./runs.md#thufb.b1) | [THUFB.C1](./runs.md#thufb.c1) | [THUFB.B2](./runs.md#thufb.b2) | [THUFB.D2](./runs.md#thufb.d2) | [THUFB.E2](./runs.md#thufb.e2) | [THUFB.C2](./runs.md#thufb.c2)

??? abstract "Abstract"
	
	Our group has participated into Relevance Feedback (RF) Track in TREC2008. In our experiments, two kinds of techniques, query expansion and search result re-ranking based on document relevance model, are adopted to improve the retrieval performance. The TMiner search engine, from IR group of Tsinghua University, is used as our text retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouFCZLM08.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouFCZLM08,
		author = {Bo Zhou and Qi Fang and Rongwei Cen and Min Zhang and Yiqun Liu and Shaoping Ma},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2008: Relevance Feedback Track},
		booktitle = {Proceedings of The Seventeenth Text REtrieval Conference, {TREC} 2008, Gaithersburg, Maryland, USA, November 18-21, 2008},
		series = {{NIST} Special Publication},
		volume = {500-277},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2008},
		url = {http://trec.nist.gov/pubs/trec17/papers/tsinghua.rf.rev.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhouFCZLM08.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

