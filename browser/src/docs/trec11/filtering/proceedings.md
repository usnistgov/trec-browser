# Proceedings - Filtering 2002 

#### The TREC 2002 Filtering Track Report

_Stephen E. Robertson, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/OVER.FILTERING.pdf](http://trec.nist.gov/pubs/trec11/papers/OVER.FILTERING.pdf)
??? abstract "Abstract"
	
	The TREC-11 filtering track measures the ability of systems to build persistent user profiles which successfully separate relevant and non-relevant documents in an incoming stream. It consists of three major subtasks: adaptive filtering, batch filtering, and routing. In adaptive filtering, the system begins with only a topic statement and a small number of positive examples, and must learn a better profile from on-line feedback. Batch filtering and routing are more traditional machine learning tasks where the system begins with a large sample of evaluated training documents. This report describes the track, presents some evaluation results, and provides a general commentary on lessons learned from this year's track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonS02,
		author = {Stephen E. Robertson and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {TREC} 2002 Filtering Track Report},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/OVER.FILTERING.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 11 Experiments at NII: The Effects of Virtual Relevant Documents  in Batch Filtering

_Kyung-Soon Lee, Kyo Kageura, Akiko N. Aizawa_

- :fontawesome-solid-user-group: **Participant:** [nii](./participants.md#nii)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/nii.lee.pdf](http://trec.nist.gov/pubs/trec11/papers/nii.lee.pdf)
- :material-file-search: **Runs:** [kNII11bf1](./runs.md#knii11bf1) | [kNII11bf2](./runs.md#knii11bf2)

??? abstract "Abstract"
	
	[...] In TREC-11 batch filtering, we have incorporated prior knowledge called virtual relevant documents to training documents by combining each two relevant documents pair and giving distinct weight for cooccurring terms on assumption that they might be related to the topic. Support vector machine (SVM) was used to learn decision boundary for the artificially enlarged training documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeKA02.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeKA02,
		author = {Kyung{-}Soon Lee and Kyo Kageura and Akiko N. Aizawa},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 11 Experiments at {NII:} The Effects of Virtual Relevant Documents in Batch Filtering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/nii.lee.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeKA02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2002 Web, Novelty and Filtering Track Experiments using PIRCS

_Kui-Lam Kwok, Peter Deng, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf](http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf)
- :material-file-search: **Runs:** [pirc2F01](./runs.md#pirc2f01) | [pirc2F02](./runs.md#pirc2f02) | [pirc2F03](./runs.md#pirc2f03) | [pirc2F04](./runs.md#pirc2f04)

??? abstract "Abstract"
	
	In TREC2002, we participated in three tracks: web, novelty and adaptive filtering. The Web track has two tasks: distillation and named-page retrieval. Distillation is a new utility concept for ranking documents, and needs new design on the output document ranked list after an ad-hoc retrieval from the web (.gov) collection. Novelty track is a new task that involves identifying relevant sentences to a question, and to remove duplicate or non- novel entries in the answer list. The third track is adaptive filtering. We revived a filtering program that was functional at TREC-9 with some added capability. Sections 2, 3, 4 describe our participation in these tracks respectively. Section 5 has our conclusion.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KwokDDC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/KwokDDC02,
		author = {Kui{-}Lam Kwok and Peter Deng and Norbert Dinstl and M. Chan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2002 Web, Novelty and Filtering Track Experiments using {PIRCS}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KwokDDC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Incremental Retrieval of Documents Relevant to a Topic

_Caroline Lyon, Bob Dickerson, James A. Malcolm_

- :fontawesome-solid-user-group: **Participant:** [hertfordshire](./participants.md#hertfordshire)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/hertfordshire.lyon.pdf](http://trec.nist.gov/pubs/trec11/papers/hertfordshire.lyon.pdf)
- :material-file-search: **Runs:** [UHcl1](./runs.md#uhcl1) | [UHcl2](./runs.md#uhcl2)

??? abstract "Abstract"
	
	As new participants to TREC, on the Filtering Track, we have started by first investigating two methods of producing document profiles. We begin by looking for 'obvious' profiles that detect closely related documents. This year we have started by looking for: lexically similar cases; semantically similar cases based on a simple combination of keywords.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LyonDM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/LyonDM02,
		author = {Caroline Lyon and Bob Dickerson and James A. Malcolm},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Incremental Retrieval of Documents Relevant to a Topic},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/hertfordshire.lyon.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LyonDM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLARIT Experiments in Batch Filtering: Term Selection and Threshold  Optimization in IR and SVM Filters

_David A. Evans, James G. Shanahan, Norbert Roma, Jeffrey Bennett, Victor Sheftel, Emilia Stoica, Jesse Montgomery, David A. Hull, Waibhav Tembe_

- :fontawesome-solid-user-group: **Participant:** [clairvoyance](./participants.md#clairvoyance)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/clairvoyance.evans.pdf](http://trec.nist.gov/pubs/trec11/papers/clairvoyance.evans.pdf)
- :material-file-search: **Runs:** [CCT11BFC](./runs.md#cct11bfc) | [CCT11BFD](./runs.md#cct11bfd)

??? abstract "Abstract"
	
	The Clairvoyance team participated in the Filtering Track, submitting two runs in the Batch Filtering category. While we have been exploring the question of both topic modeling and ensemble filter construction (as in our previous TREC filtering experiments [5]), we had one distinct objective this year, to explore the viability of monolithic filters in classification-like tasks. This is appropriate to our work, in part, because monolithic filters are a crucial starting point for ensemble filtering, and it is possible for them to contribute substantially in the ensemble approach. Our primary goal in experiments this year, thus, was to explore two issues in monolithic filter construction: (1) term count selection and (2) filter threshold optimization. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EvansSRBSSMHT02.bib) "
	```
	@inproceedings{DBLP:conf/trec/EvansSRBSSMHT02,
		author = {David A. Evans and James G. Shanahan and Norbert Roma and Jeffrey Bennett and Victor Sheftel and Emilia Stoica and Jesse Montgomery and David A. Hull and Waibhav Tembe},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CLARIT} Experiments in Batch Filtering: Term Selection and Threshold Optimization in {IR} and {SVM} Filters},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/clairvoyance.evans.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EvansSRBSSMHT02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Novel Results and Some Answers - The University of Iowa TREC 11  Results

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [uiowa](./participants.md#uiowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uiowa.eichmann.pdf](http://trec.nist.gov/pubs/trec11/papers/uiowa.eichmann.pdf)
- :material-file-search: **Runs:** [UIowa02Filt](./runs.md#uiowa02filt)

??? abstract "Abstract"
	
	The University of Iowa participated in the novelty, adaptive filtering and question answering tracks of TREC-11. The filtering system used was an extension of the one used in TREC-7 [1] and TREC-8 [2]. Question answering was derived from the TREC-10 system. The novelty system was new...
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS02,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Novel Results and Some Answers - The University of Iowa {TREC} 11 Results},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uiowa.eichmann.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Filtering, Novelty Detection, and Named-Page Finding

_Kevyn Collins-Thompson, Paul Ogilvie, Yi Zhang, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu_lti](./participants.md#cmu_lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf](http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf)
- :material-file-search: **Runs:** [CMUDIRUDESC](./runs.md#cmudirudesc) | [CMUDIRFDESC](./runs.md#cmudirfdesc) | [CMUDIRUml](./runs.md#cmudiruml) | [CMUDIRFml](./runs.md#cmudirfml)

??? abstract "Abstract"
	
	In TREC 11, our group participated in the Novelty track, Filtering track, and the Named-Page Finding task of the Web track. This paper describes our approaches, experiments, and results. As the approach for each task is quite different, the paper contains a section for each of the tasks. The following section describes our experiments in adaptive filtering, Section 3 describes named-page finding, and section 4 discusses the Novelty track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Collins-ThompsonOZC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Collins-ThompsonOZC02,
		author = {Kevyn Collins{-}Thompson and Paul Ogilvie and Yi Zhang and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Information Filtering, Novelty Detection, and Named-Page Finding},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Collins-ThompsonOZC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Kernel Methods for Document Filtering

_Nicola Cancedda, Cyril Goutte, Jean-Michel Renders, Nicolò Cesa-Bianchi, Alex Conconi, Yaoyong Li, John Shawe-Taylor, Alexei Vinokourov, Thore Graepel, Claudio Gentile_

- :fontawesome-solid-user-group: **Participant:** [kerMIT](./participants.md#kermit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/kermit.pdf](http://trec.nist.gov/pubs/trec11/papers/kermit.pdf)
- :material-file-search: **Runs:** [KerMITT11af1](./runs.md#kermitt11af1) | [KerMITT11af2](./runs.md#kermitt11af2) | [KerMITT11af3](./runs.md#kermitt11af3) | [KerMITT11af4](./runs.md#kermitt11af4) | [KerMITT11bf2](./runs.md#kermitt11bf2) | [KerMITT11rr2](./runs.md#kermitt11rr2)

??? abstract "Abstract"
	
	This paper describes the algorithms implemented by the KerMIT consortium for its participation in the TREC 2002 Filtering track. The consortium submitted runs for the routing task using a linear SVM, for the batch task using the same SVM in combination with an innovative threshold-selection mechanism, and for the adaptive task using both a second-order perceptron and a combination of SVM and perceptron with uneven margin. Results seem to indicate that these algorithm performed relatively well on the extensive TREC benchmark.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CanceddaGRCCLSVGG02.bib) "
	```
	@inproceedings{DBLP:conf/trec/CanceddaGRCCLSVGG02,
		author = {Nicola Cancedda and Cyril Goutte and Jean{-}Michel Renders and Nicol{\`{o}} Cesa{-}Bianchi and Alex Conconi and Yaoyong Li and John Shawe{-}Taylor and Alexei Vinokourov and Thore Graepel and Claudio Gentile},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Kernel Methods for Document Filtering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/kermit.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CanceddaGRCCLSVGG02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CLIPS at TREC 11: Experiments in Filtering

_Christophe Brouard_

- :fontawesome-solid-user-group: **Participant:** [clips-imag](./participants.md#clips-imag)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/clips.filter.pdf](http://trec.nist.gov/pubs/trec11/papers/clips.filter.pdf)
- :material-file-search: **Runs:** [reliefst11u](./runs.md#reliefst11u)

??? abstract "Abstract"
	
	At the TREC9 conference, we presented a new adaptive filtering system called RELIEFS. This system which is based on the idea of resonance, combines for each term t, the relative frequency of relevance knowing t and the relative frequency of t kwowing relevance. On the basis of other experiments, several changes have been made. We improved our threshold adaption, we slightly changed our relevance evaluation function and we gave up the use of conjunctions and thesaurus. The system is now focusing more exclusively on the combination of both reverse frequencies that we believe to represent the fundamental aspects of relevance estimation. This year we used the system in its new version and we tested it on the Reuters corpus. Focusing on the combination of the two frequencies, we varied their relative importance. The results show globally a good effectiveness especially when both frequencies are balanced.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Brouard02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Brouard02,
		author = {Christophe Brouard},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CLIPS} at {TREC} 11: Experiments in Filtering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/clips.filter.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Brouard02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IRIT at TREC 2002: Filtering Track

_Mohand Boughanem, Hamid Tebri, Mohamed Tmar_

- :fontawesome-solid-user-group: **Participant:** [irit](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/irit.tebri.pdf](http://trec.nist.gov/pubs/trec11/papers/irit.tebri.pdf)
- :material-file-search: **Runs:** [iritsiga1](./runs.md#iritsiga1) | [iritsiga2](./runs.md#iritsiga2) | [iritsigb](./runs.md#iritsigb) | [iritsigr](./runs.md#iritsigr)

??? abstract "Abstract"
	
	The experiments we undertaken this year for TREC2002 Filtering track, are focussed on threshold calibration. We proposed a new approach to calibrate the dissemination threshold in an adaptive information filtering. It consists of optimizing a utility function represented by a linearized form of the probability distributions of the scores of the relevant and the non-relevant documents already filtered. The profiles are learned using the same method used last year. It is based on a reinforcement algorithm. We submitted results on three tasks: adaptive, batch and routing.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BoughanemTT02.bib) "
	```
	@inproceedings{DBLP:conf/trec/BoughanemTT02,
		author = {Mohand Boughanem and Hamid Tebri and Mohamed Tmar},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IRIT} at {TREC} 2002: Filtering Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/irit.tebri.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BoughanemTT02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Incremental Learning for Profile Training in Adaptive Document Filtering

_Liang Ma, Qunxiu Chen, Shaoping Ma, Min Zhang, Lianhong Cai_

- :fontawesome-solid-user-group: **Participant:** [tsinghua](./participants.md#tsinghua)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/tsinghuau.filtering2.pdf](http://trec.nist.gov/pubs/trec11/papers/tsinghuau.filtering2.pdf)
- :material-file-search: **Runs:** [thuT11af1](./runs.md#thut11af1) | [thuT11af2](./runs.md#thut11af2) | [thuT11af3](./runs.md#thut11af3)

??? abstract "Abstract"
	
	In this paper, we describe our ideas and related experiments in TREC-11 Adaptive Filtering Track. In the track we focused much on a robust way for effective profile training. We developed an incremental learning method which selects pseudo positive documents in less bias from a few initial positive training documents. We also did some experiments with newly emerged information retrieval model, language model-based retrieval mechanism, to evaluate its performance when used in adaptive filtering task. Related experiment results show the incremental learning method can be helpful for profile training, while the new language model perform not well.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MaCMZC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MaCMZC02,
		author = {Liang Ma and Qunxiu Chen and Shaoping Ma and Min Zhang and Lianhong Cai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Incremental Learning for Profile Training in Adaptive Document Filtering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/tsinghuau.filtering2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MaCMZC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 11 Experiments at CAS-ICT: Filtering and Web

_Hongbo Xu, Zhifeng Yang, Bin Wang, Bin Liu, Jun Cheng, Yue Liu, Zhe Yang, Xueqi Cheng, Shuo Bai_

- :fontawesome-solid-user-group: **Participant:** [chinese_academy](./participants.md#chinese_academy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cas_final.hongbo.pdf](http://trec.nist.gov/pubs/trec11/papers/cas_final.hongbo.pdf)
- :material-file-search: **Runs:** [ICTBatFT11Ua](./runs.md#ictbatft11ua) | [ICTBatFT11Ub](./runs.md#ictbatft11ub) | [ICTAdaFT11Ud](./runs.md#ictadaft11ud) | [ICTAdaFT11Ua](./runs.md#ictadaft11ua) | [ICTAdaFT11Ub](./runs.md#ictadaft11ub) | [ICTAdaFT11Uc](./runs.md#ictadaft11uc) | [ICTRouFT11Ua](./runs.md#ictrouft11ua) | [ICTRouFT11Ub](./runs.md#ictrouft11ub)

??? abstract "Abstract"
	
	CAS-ICT took part in the TREC conference for the second time this year and we undertook two tracks of TREC-11. For filtering track, we have submitted results of all three subtasks. In adaptive filtering, we paid more attention to undetermined documents processing, profile building and adaptation. In batch filtering and routing, a centroid-based classifier is used with preprocessed samples. For Web track, we have submitted results of both two subtasks. Different factors are considered to improve the overall performance of our Web systems. This paper describes our methods in detail.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XuYWLCLYCB02.bib) "
	```
	@inproceedings{DBLP:conf/trec/XuYWLCLYCB02,
		author = {Hongbo Xu and Zhifeng Yang and Bin Wang and Bin Liu and Jun Cheng and Yue Liu and Zhe Yang and Xueqi Cheng and Shuo Bai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 11 Experiments at {CAS-ICT:} Filtering and Web},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cas\_final.hongbo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XuYWLCLYCB02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC 2002: Filtering, Q&A, Web and Video Tasks

_Lide Wu, Xuanjing Huang, Junyu Niu, Yingju Xia, Zhe Feng, Yaqian Zhou_

- :fontawesome-solid-user-group: **Participant:** [Fudan](./participants.md#fudan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf](http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf)
- :material-file-search: **Runs:** [FDUT11AF1](./runs.md#fdut11af1) | [FDUT11AF2](./runs.md#fdut11af2)

??? abstract "Abstract"
	
	his year Fudan University takes part in the TREC conference for the third time. We have participated in four tracks of Filtering, Q&A, Web and Video. For filtering, we only participate in the sub-task of adaptive filtering. A novel method is presented, in which a winnow classifier from the description and narrative fields is constructed, and then utilized to assist our previous adaptive filtering system. A novel approach to confidence sorting, which is based on Maximum Entropy, is proposed in our Question Answering system. The rank of individual answer is determined by several weighted factors, and the confidence score is the product of the exponent of the weights of every factors. The weight of every factor is assigned during the training of previous questions. To return highly relevant key resources for web retrieval, we modified our original search system to make it return higher precision result than before. First, we proposed a novel search algorithm to get a base set of highly relevant documents. Then special post-processing modules are used to expand and re-sort the base set. This year we tried a fast manifold-based approach to face recognition in the Video Search Task. It can be used when there are only few different images of a specific person and runs fast. Experiment shows that applying this step will make the face recognition 5-fold faster and with almost no decreasing of performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuHNXFZ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuHNXFZ02,
		author = {Lide Wu and Xuanjing Huang and Junyu Niu and Yingju Xia and Zhe Feng and Yaqian Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDU} at {TREC} 2002: Filtering, Q{\&}A, Web and Video Tasks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/fudan.lide.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuHNXFZ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Example Based Text Matching Methodology for Routing Tasks

_Ari Visa, Jarmo Toivonen, Tomi Vesanen, Jarno Mäkinen, Barbro Back, Hannu Vanharanta_

- :fontawesome-solid-user-group: **Participant:** [tampere](./participants.md#tampere)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/tampere.jarmo.pdf](http://trec.nist.gov/pubs/trec11/papers/tampere.jarmo.pdf)
- :material-file-search: **Runs:** [Visa1T11](./runs.md#visa1t11) | [Visa2T11](./runs.md#visa2t11)

??? abstract "Abstract"
	
	We present two variations of a prototype based text matching methodology used in the Routing Sub-Task of TREC 2002 Filtering Track. The methodology examines text on the word level. It is based on word coding and examines the distributions of these codes using document histograms.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VisaTVMBV02.bib) "
	```
	@inproceedings{DBLP:conf/trec/VisaTVMBV02,
		author = {Ari Visa and Jarmo Toivonen and Tomi Vesanen and Jarno M{\"{a}}kinen and Barbro Back and Hannu Vanharanta},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Example Based Text Matching Methodology for Routing Tasks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/tampere.jarmo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VisaTVMBV02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UB at TREC 11: Batch and Adaptive Filtering

_Munirathnam Srikanth, Xiaoyun Wu, Rohini K. Srihari_

- :fontawesome-solid-user-group: **Participant:** [buffalo_cedar](./participants.md#buffalo_cedar)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/unybuffalo.pdf](http://trec.nist.gov/pubs/trec11/papers/unybuffalo.pdf)
- :material-file-search: **Runs:** [cedar02bffb0](./runs.md#cedar02bffb0) | [cedar02afut0](./runs.md#cedar02afut0) | [cedar02affb0](./runs.md#cedar02affb0) | [cedar02bfut0](./runs.md#cedar02bfut0)

??? abstract "Abstract"
	
	This is the first time we participated in TREC filtering track. We submitted four runs: two for adaptive filtering, and two for batching filtering. And these runs come from two separate efforts with very different approaches. One effort treats the filtering problems as standard text categorization problems and solves them using Support Vector Machines (SVM). The second effort is a Language Modeling approach to information filtering. Among other things we wanted to use filtering tasks as large scale test cases for two separate frameworks we have been working on for information retrieval. Significant time was spent on putting the components together and limited time on pre-submission performance evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SrikanthWS02.bib) "
	```
	@inproceedings{DBLP:conf/trec/SrikanthWS02,
		author = {Munirathnam Srikanth and Xiaoyun Wu and Rohini K. Srihari},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UB} at {TREC} 11: Batch and Adaptive Filtering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/unybuffalo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SrikanthWS02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Microsoft Cambridge at TREC 2002: Filtering Track

_Stephen E. Robertson, Steve Walker, Hugo Zaragoza, Ralf Herbrich_

- :fontawesome-solid-user-group: **Participant:** [microsoft_cambridge](./participants.md#microsoft_cambridge)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cambridge.corrected.pdf](http://trec.nist.gov/pubs/trec11/papers/cambridge.corrected.pdf)
- :material-file-search: **Runs:** [ok11aflu](./runs.md#ok11aflu) | [ok11afsu](./runs.md#ok11afsu) | [ok11afsb](./runs.md#ok11afsb) | [ok11aflb](./runs.md#ok11aflb) | [msPUMs](./runs.md#mspums) | [msPUMb](./runs.md#mspumb)

??? abstract "Abstract"
	
	Six runs were submitted for the Adaptive Filtering track, four on the adaptive filtering task (ok11af??), and two on the routing task (msPUM?). The adaptive filtering system has been somewhat modified from the one used for TREC–10, largely for efficiency and flexibility reasons; the basic filtering algorithms remain similar to those used in recent TRECs. For the routing task, a completely new system based on perceptrons with uneven margins was used.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RobertsonWZH02.bib) "
	```
	@inproceedings{DBLP:conf/trec/RobertsonWZH02,
		author = {Stephen E. Robertson and Steve Walker and Hugo Zaragoza and Ralf Herbrich},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Microsoft Cambridge at {TREC} 2002: Filtering Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/cambridge.corrected.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RobertsonWZH02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Classifier Stacking and Voting for Text Filtering

_Rada Mihalcea_

- :fontawesome-solid-user-group: **Participant:** [north_texas](./participants.md#north_texas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/untexas.mihalcea.pdf](http://trec.nist.gov/pubs/trec11/papers/untexas.mihalcea.pdf)
- :material-file-search: **Runs:** [UNTextCatSU](./runs.md#untextcatsu) | [UNTextCatF](./runs.md#untextcatf) | [UNTextCatR](./runs.md#untextcatr) | [UNTextCatR1](./runs.md#untextcatr1)

??? abstract "Abstract"
	
	This paper summarizes the approach and the results of the TextCat system participating in the Filtering track in the Text Retrieval Conference 2002. The system relies primarily on statistical methods, and was designed with the main purpose of having a backbone system in which we can further integrate semantic components, and evaluate their relative performance as compared to traditional statistical approaches. The system is therefore simple, and is based on techniques for keywords extraction, and various classifier combinations including stacking and voting. TextCat participated in the Batch and Routing tasks. In the Batch task, it achieved a score of 39.02% normalized utility, and 26.37% F-measure respectively, averaged over all topics. The averaged uninterpolated precision for our best routing submission was 14.16%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Mihalcea02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Mihalcea02,
		author = {Rada Mihalcea},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Classifier Stacking and Voting for Text Filtering},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/untexas.mihalcea.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Mihalcea02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### JHU/APL at TREC 2002: Experiments in Filtering and Arabic Retrieval

_Paul McNamee, Christine D. Piatko, James Mayfield_

- :fontawesome-solid-user-group: **Participant:** [jhu_apl](./participants.md#jhu_apl)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/jhuapl.mcnamee.pdf](http://trec.nist.gov/pubs/trec11/papers/jhuapl.mcnamee.pdf)
- :material-file-search: **Runs:** [apl11Fah1](./runs.md#apl11fah1) | [apl11Fah2](./runs.md#apl11fah2) | [apl11Faq1](./runs.md#apl11faq1) | [apl11Faq2](./runs.md#apl11faq2) | [apl11FbF](./runs.md#apl11fbf) | [apl11FbSU](./runs.md#apl11fbsu) | [apl11Frm](./runs.md#apl11frm) | [apl11Frsvm](./runs.md#apl11frsvm)

??? abstract "Abstract"
	
	The Johns Hopkins University Applied Physics Laboratory (JHU/APL) participated in two tracks at this year's conference. We participated in the filtering track, again addressing the batch and routing subtasks, as well as the adaptive task for the first time. We also continued experiments in Arabic retrieval, emphasizing language-neutral approaches. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McNameePM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/McNameePM02,
		author = {Paul McNamee and Christine D. Piatko and James Mayfield},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{JHU/APL} at {TREC} 2002: Experiments in Filtering and Arabic Retrieval},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/jhuapl.mcnamee.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McNameePM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Rutgers Filtering Work at TREC 2002: Adaptive and Batch

_Andrei Anghelescu, Endre Boros, David D. Lewis, Vladimir Menkov, David J. Neu, Paul B. Kantor_

- :fontawesome-solid-user-group: **Participant:** [rutgers-kantor](./participants.md#rutgers-kantor)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/rutgers.kantor.pdf](http://trec.nist.gov/pubs/trec11/papers/rutgers.kantor.pdf)
- :material-file-search: **Runs:** [dimacs11a30Q](./runs.md#dimacs11a30q) | [dimacs11aAPQ](./runs.md#dimacs11aapq) | [dimacs11b001](./runs.md#dimacs11b001) | [dimacs11aP1Q](./runs.md#dimacs11ap1q)

??? abstract "Abstract"
	
	This year at TREC 2002 we participated in the adaptive filtering sub-task of the filtering track with some models for training a Rocchio classifier. Results were poorer than average on the utility type measures. Using simple feature selection produced better than average results on an F-type measure. The key to our approach was the use of pseudo-judgments, and an approach to threshold updating. We also participated in the batch filtering sub-task of the filtering track and investigated the use of rank based feature selection techniques in conjunction with a very simple classification rule.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AnghelescuBLMNK02.bib) "
	```
	@inproceedings{DBLP:conf/trec/AnghelescuBLMNK02,
		author = {Andrei Anghelescu and Endre Boros and David D. Lewis and Vladimir Menkov and David J. Neu and Paul B. Kantor},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Rutgers Filtering Work at {TREC} 2002: Adaptive and Batch},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/rutgers.kantor.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AnghelescuBLMNK02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

