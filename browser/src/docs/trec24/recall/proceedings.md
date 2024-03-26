# Proceedings - Total Recall 2015 

#### TREC 2015 Total Recall Track Overview

_Adam Roegiest, Gordon V. Cormack, Charles L. A. Clarke, Maura R. Grossman_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec24/papers/Overview-TR.pdf](https://trec.nist.gov/pubs/trec24/papers/Overview-TR.pdf)
??? abstract "Abstract"
	
	The primary purpose of the Total Recall Track is to evaluate, through controlled simulation, methods designed to achieve very high recall - as close as practicable to 100% - with a human assessor in the loop. Motivating applications include, among others, electronic discovery in legal proceedings [2], systematic review in evidence-based medicine [11], and the creation of fully labeled test collections for information retrieval (“IR”) evaluation [8]. A secondary, but no less important, purpose is to develop a sandboxed virtual test environment within which IR systems may be tested, while preventing the disclosure of sensitive test data to participants. At the same time, the test environment also operates as a “black box,” affording participants confidence that their proprietary systems cannot easily be reverse engineered
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RoegiestCCG15.bib) "
	```
	@inproceedings{DBLP:conf/trec/RoegiestCCG15,
		author = {Adam Roegiest and Gordon V. Cormack and Charles L. A. Clarke and Maura R. Grossman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2015 Total Recall Track Overview},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {https://trec.nist.gov/pubs/trec24/papers/Overview-TR.pdf},
		timestamp = {Wed, 03 Feb 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RoegiestCCG15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Waterloo (Cormack) Participation in the TREC 2015 Total Recall Track

_Gordon V. Cormack, Maura R. Grossman_

- :fontawesome-solid-user-group: **Participant:** [WaterlooCormack](./participants.md#waterloocormack)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WaterlooCormack-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/WaterlooCormack-TR.pdf)
- :material-file-search: **Runs:** [UWGVCknee100](./runs.md#uwgvcknee100) | [UWGVCknee1000](./runs.md#uwgvcknee1000) | [stop3299](./runs.md#stop3299)

??? abstract "Abstract"
	
	In the course of developing tools for the 2015 Total Recall Track, co-coordinators Cormack and Grossman created an autonomous continuous active learning (“CAL”) system, which was provided to participants as the baseline model implementation (“BMI”) [http://plg.uwaterloo.ca/⇠gvcormac/trecvm/]. BMI essentially employs the approach described by Cormack and Grossman [http://arxiv.org/abs/1504.06868]; the only difference is that BMI employs logistic regression implemented by Sofia ML [https://code.google.com/p/sofia-ml/] instead of SVMlight [http://svmlight.joachims.org/]. The Waterloo (Cormack) team submitted runs using BMI for each of the five 2015 Total Recall test collections. The only change that was made to BMI was to add a provision to “call our shot” - that is, to indicate to the assessment server when we believed the run to be reasonably complete. Although the Track provided three milestones - '70recall,' '80recall,' and 'reasonable' - we made no attempt to quantify the recall of our runs, and instead used the three milestones to indicate graduated levels of completeness, which one might interpret as “good,” “better,” and 'best.' [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackG15.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackG15,
		author = {Gordon V. Cormack and Maura R. Grossman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Waterloo (Cormack) Participation in the {TREC} 2015 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/WaterlooCormack-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackG15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Efficient semantic indexing via neural networks with dynamic supervised  feedback

_Vivek Dhand_

- :fontawesome-solid-user-group: **Participant:** [CCRi](./participants.md#ccri)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/CCRi-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/CCRi-TR.pdf)
- :material-file-search: **Runs:** [CCRi-athome](./runs.md#ccri-athome)

??? abstract "Abstract"
	
	We describe a portable system for ecient semantic indexing of documents via neural networks with dynamic supervised feedback. We initially represent each document as a modified TF-IDF sparse vector and then apply a learned mapping to a compact embedding space. This mapping is produced by a shallow neural network which learns a latent representation for the textual graph linking words to nearby contexts. The resulting document embeddings provide significantly better semantic representation, partly because they incorporate information about synonyms. Query topics are uniformly represented in the same manner as documents. For each query, we dynamically train an additional hidden layer which modifies the embedding space in response to relevance judgements. The system was tested using the documents and topics provided in the Total Recall track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Dhand15.bib) "
	```
	@inproceedings{DBLP:conf/trec/Dhand15,
		author = {Vivek Dhand},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Efficient semantic indexing via neural networks with dynamic supervised feedback},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/CCRi-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Dhand15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### e-Discovery Team at TREC 2015 Total Recall Track

_Ralph Losey, Jim Sullivan, Tony Reichenberger_

- :fontawesome-solid-user-group: **Participant:** [eDiscoveryTeam](./participants.md#ediscoveryteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/eDiscoveryTeam-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/eDiscoveryTeam-TR.pdf)
- :material-file-search: **Runs:** [Multimodal](./runs.md#multimodal)

??? abstract "Abstract"
	
	The 2015 TREC Total Recall Track provided instant relevance feedback in thirty prejudged topics searching three different datasets. The e-Discovery Team of three attorneys specializing in legal search participated in all thirty topics using Kroll Ontrack's search and review software, eDiscovery.com Review (EDR). They employed a hybrid approach to continuous active learning that uses both manual and automatic searches. A variety of manual search methods were used to find training documents, including high probability ranked documents and keywords, an ad hoc process the Team calls multimodal. In the one topic (109) requiring legal analysis the Team's approach was significantly more effective than all other participants, including the fully automated approaches that otherwise attained comparable scores. In all topics the Team's hybrid multimodal method consistently attained the highest F1 values at the time of Reasonable Call, equivalent to a stop point. In all topics the Team's multimodal human machine approach also found relevant documents more quickly and with greater precision than the fully automated or other methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LoseySR15.bib) "
	```
	@inproceedings{DBLP:conf/trec/LoseySR15,
		author = {Ralph Losey and Jim Sullivan and Tony Reichenberger},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {e-Discovery Team at {TREC} 2015 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/eDiscoveryTeam-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LoseySR15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TUW at the First Total Recall Track

_Mihai Lupu_

- :fontawesome-solid-user-group: **Participant:** [TUW](./participants.md#tuw)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/TUW-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/TUW-TR.pdf)
- :material-file-search: **Runs:** [1NB](./runs.md#1nb) | [1ST](./runs.md#1st) | [1SB](./runs.md#1sb) | [6SB](./runs.md#6sb) | [6NB](./runs.md#6nb) | [6ST](./runs.md#6st) | [1NB_sandbox](./runs.md#1nb_sandbox) | [1ST_sandbox](./runs.md#1st_sandbox) | [1SB_sandbox](./runs.md#1sb_sandbox) | [6SB_sandbox](./runs.md#6sb_sandbox) | [6NB_sandbox](./runs.md#6nb_sandbox) | [6ST_sandbox](./runs.md#6st_sandbox)

??? abstract "Abstract"
	
	For the first participation in the TREC Total Recall track, we set out to try some basic changes to the baseline provided by the organisers. Namely, the weighting scheme, the use of stopwords, and the number of learners that contribute to the decision of which documents to ask the virtual assessor to review. We observed that the baseline was extremely strong and none of the runs significantly and consistently outperformed it.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Lupu15.bib) "
	```
	@inproceedings{DBLP:conf/trec/Lupu15,
		author = {Mihai Lupu},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TUW} at the First Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/TUW-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Lupu15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Constrained Approach to Manual Total Recall

_Jeremy Pickens, Tom Gricks, Bayu Hardi, Mark Noel_

- :fontawesome-solid-user-group: **Participant:** [catres](./participants.md#catres)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/catres-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/catres-TR.pdf)
- :material-file-search: **Runs:** [attemptone](./runs.md#attemptone)

??? abstract "Abstract"
	
	The Catalyst participation in the manual at home Total Recall Track was both limited and quick, a TREC submission of practicality over research. The group's decision to participate in TREC was made three weeks, and data was not loaded until six days, before the final submission deadline. As a result and to reasonably simulate an expedited document review process, a number of shortcuts were taken in order to accomplish the runs in limited time. Choices about implementation details were due primarily to time constraint and necessity, rather than out of designed scientific hypothesis. We detail these shortcuts, as well as provide a few additional post hoc, non-ocial runs in which we remove some of the shortcuts and constraints. We also explore the e↵ect of di↵erent manual seeding approaches on the recall outcome.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PickensGHN15.bib) "
	```
	@inproceedings{DBLP:conf/trec/PickensGHN15,
		author = {Jeremy Pickens and Tom Gricks and Bayu Hardi and Mark Noel},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {A Constrained Approach to Manual Total Recall},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/catres-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PickensGHN15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WHU at TREC Total Recall Track 2015

_Chuan Wu, Wei Lu, Ruixue Wang_

- :fontawesome-solid-user-group: **Participant:** [WHU_IRGroup](./participants.md#whu_irgroup)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WHU_IRGroup-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/WHU_IRGroup-TR.pdf)
- :material-file-search: **Runs:** [iterative_expansion](./runs.md#iterative_expansion)

??? abstract "Abstract"
	
	This paper describes the WHU IRLAB participation to the Total Recall Track in TREC 2015. We implement an end-to-end system to deal with the total recall task. We propose an iterative query expansion method, which construct queries using iteratively selected terms. We choose to participate the 'Play-at-home' evaluation. Results are presented and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WuLW15.bib) "
	```
	@inproceedings{DBLP:conf/trec/WuLW15,
		author = {Chuan Wu and Wei Lu and Ruixue Wang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{WHU} at {TREC} Total Recall Track 2015},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/WHU\_IRGroup-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WuLW15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WaterlooClarke: TREC 2015 Total Recall Track

_Haotian Zhang, Wu Lin, Yipeng Wang, Charles L. A. Clarke, Mark D. Smucker_

- :fontawesome-solid-user-group: **Participant:** [WaterlooClarke](./participants.md#waterlooclarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-TR.pdf)
- :material-file-search: **Runs:** [UWPAH](./runs.md#uwpah) | [UWPAH_](./runs.md#uwpah_)

??? abstract "Abstract"
	
	The total recall track in TREC 2015 seeks an enhanced model to accelerate the autonomous technology-assisted review process. This paper introduces several noval ideas such as clustering based seed selection method, extended n-grams features and continuous query expansion learned from the relevant documents derived from each iteration. These methods can retrieve more relevant documents from each iteration thereby achieving high recall while requiring less review effort.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangLWCS15.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangLWCS15,
		author = {Haotian Zhang and Wu Lin and Yipeng Wang and Charles L. A. Clarke and Mark D. Smucker},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {WaterlooClarke: {TREC} 2015 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/WaterlooClarke-TR.pdf},
		timestamp = {Sun, 09 Aug 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangLWCS15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam (ILPS) at TREC 2015 Total Recall Track

_David van Dijk, Zhaochun Ren, Evangelos Kanoulas, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [UvA.ILPS](./participants.md#uva.ilps)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/UvA.ILPS-TR.pdf](http://trec.nist.gov/pubs/trec24/papers/UvA.ILPS-TR.pdf)
- :material-file-search: **Runs:** [BASELINE](./runs.md#baseline) | [BASELINE2](./runs.md#baseline2) | [BASELINE_SANDBOX](./runs.md#baseline_sandbox) | [BASELINE2_SANDBOX](./runs.md#baseline2_sandbox)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdams ILPS group in the Total Recall track at TREC 2015. Based on the provided Baseline Model Implemention (”BMI”) we set out to provide two more baselines we can compare to in future work. The two methods are bootstrapped by a synthetic document based on the query, use TF/IDF features, and sample with dynamic batch sizes which depend on the percentage of predicted relevant documents. We sample at least 1 percent of the corpus and stop sampling if a batch contains no relevant documents. The methods differ in the classifier used, i.e. Logistic Regression and Random Forest.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DijkRKR15.bib) "
	```
	@inproceedings{DBLP:conf/trec/DijkRKR15,
		author = {David van Dijk and Zhaochun Ren and Evangelos Kanoulas and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Amsterdam {(ILPS)} at {TREC} 2015 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/UvA.ILPS-TR.pdf},
		timestamp = {Wed, 07 Dec 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DijkRKR15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2015: Tasks and Total Recall Tracks

_Matthias Hagen, Steve Göring, Magdalena Keil, Olaoluwa Anifowose, Amir Othman, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/Webis-TTR.pdf](http://trec.nist.gov/pubs/trec24/papers/Webis-TTR.pdf)
- :material-file-search: **Runs:** [Baseline](./runs.md#baseline) | [Keyphrase](./runs.md#keyphrase) | [SandboxBaseline](./runs.md#sandboxbaseline) | [SandboxKeyphrase](./runs.md#sandboxkeyphrase)

??? abstract "Abstract"
	
	In this paper we give a brief overview of the Webis group's participation in the TREC 2015 Tasks and Total Recall tracks. In the task understanding subtask of the Tasks track, we use dierent data sources (AOL query log, Freebase, etc.) and APIs (Google, Bing, etc.) to retrieve topics related to a given query. All sources are combined in our SQuare system. The task completion subtask is based on combining the results of our ChatNoir 2 for the dierent topics identified in the task understanding subtask. Finally, for the ad-hoc sub-task (similar to the previous years' Web tracks), we use an axiomatic re-ranking approach of the search results obtained from ChatNoir 2. In the Total Recall track, we employ a simple SVM baseline with variable batch sizes equipped with a keyqueries step to identify potentially relevant documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenGKAOS15.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenGKAOS15,
		author = {Matthias Hagen and Steve G{\"{o}}ring and Magdalena Keil and Olaoluwa Anifowose and Amir Othman and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2015: Tasks and Total Recall Tracks},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/Webis-TTR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenGKAOS15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

