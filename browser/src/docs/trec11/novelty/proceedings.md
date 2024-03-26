# Proceedings - Novelty 2002 

#### Overview of the TREC 2002 Novelty Track

_Donna Harman_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/NOVELTY.OVER.pdf](http://trec.nist.gov/pubs/trec11/papers/NOVELTY.OVER.pdf)
??? abstract "Abstract"
	
	The novelty track was a new track in TREC-11. The basic task was as follows: given a TREC topic and an ordered list of relevant documents (ordered by relevance ranking), find the relevant and 'novel' sentences that should be returned to the user from this set. There were 13 groups that participated in this new task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Harman02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Harman02,
		author = {Donna Harman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2002 Novelty Track},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/NOVELTY.OVER.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Harman02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Machine Learning Approach for QA and Novelty Tracks: NTT System  Description

_Hideto Kazawa, Tsutomu Hirao, Hideki Isozaki, Eisaku Maeda_

- :fontawesome-solid-user-group: **Participant:** [nttcom_kazawa](./participants.md#nttcom_kazawa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/nttcom.pdf](http://trec.nist.gov/pubs/trec11/papers/nttcom.pdf)
- :material-file-search: **Runs:** [nttcslabnvp](./runs.md#nttcslabnvp) | [nttcslabnvr2](./runs.md#nttcslabnvr2)

??? abstract "Abstract"
	
	In one sense, the goals of QA and Novelty tasks are the same: extracting small document parts which are relevant to users' queries. Additionally, the unit of extraction is almost always fixed in both tasks. For QA, an answer is a noun phrase in most cases, and for Novelty, a sentence is recognized as the basic information unit. This observation leads us to the following unified approach to both QA and Novelty tasks: first identify information units in documents, then judge whether each unit is relevant to the query. This two step approach is amenable to machine learning methods because each step can be cast as a classification problem. For example, noun phrase identification can be achieved by classifying each word into the start/middle/end/exterior of a noun phrase; sentence identification by classifying whether each period marks the of a sentence. Additionally, relevance judgment can be regarded as the classification of a pair of query and an information unit into a relevant-pair or non-relevant-pair. In QA and Novelty Tracks at TREC 2002, we studied the feasibility of this two step approach, using Support Vector Machines as the learning algorithm of the classifiers. Since many studies on identifying information units have already been reported, we concentrate on the relevance judgment step in QA and Novelty tasks in this paper
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KazawaHIM02.bib) "
	```
	@inproceedings{DBLP:conf/trec/KazawaHIM02,
		author = {Hideto Kazawa and Tsutomu Hirao and Hideki Isozaki and Eisaku Maeda},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Machine Learning Approach for {QA} and Novelty Tracks: {NTT} System Description},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/nttcom.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KazawaHIM02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2002 Web, Novelty and Filtering Track Experiments using PIRCS

_Kui-Lam Kwok, Peter Deng, Norbert Dinstl, M. Chan_

- :fontawesome-solid-user-group: **Participant:** [cuny](./participants.md#cuny)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf](http://trec.nist.gov/pubs/trec11/papers/queens.kwok.pdf)
- :material-file-search: **Runs:** [pircs2N01](./runs.md#pircs2n01) | [pircs2N02](./runs.md#pircs2n02) | [pircs2N03](./runs.md#pircs2n03) | [pircs2N04](./runs.md#pircs2n04) | [pircs2N05](./runs.md#pircs2n05)

??? abstract "Abstract"
	
	In TREC2002, we participated in three tracks: web, novelty and adaptive filtering. The Web track has two tasks: distillation and named-page retrieval. Distillation is a new utility concept for ranking documents, and needs new design on the output document ranked list after an ad-hoc retrieval from the web (.gov) collection. Novelty track is a new task that involves identifying relevant sentences to a question, and to remove duplicate or non-novel entries in the answer list. The third track is adaptive filtering. We revived a filtering program that was functional at TREC-9 with some added capability. Sections 2, 3, 4 describe our participation in these tracks respectively. Section 5 has our conclusion.
	

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

#### Information Filtering, Novelty Detection, and Named-Page Finding

_Kevyn Collins-Thompson, Paul Ogilvie, Yi Zhang, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [cmu_lti](./participants.md#cmu_lti)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf](http://trec.nist.gov/pubs/trec11/papers/cmu.collins-thompson.pdf)
- :material-file-search: **Runs:** [cmu02t300rCv](./runs.md#cmu02t300rcv) | [cmu02t300rCw](./runs.md#cmu02t300rcw) | [cmu02t300rCb](./runs.md#cmu02t300rcb) | [cmu02t300rBw](./runs.md#cmu02t300rbw) | [cmu02t300rAs](./runs.md#cmu02t300ras)

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

#### Novelty Track at IRIT-SIG

_Taoufiq Dkaki, Josiane Mothe, Jérôme Augé_

- :fontawesome-solid-user-group: **Participant:** [irit](./participants.md#irit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/irit.novelty.pdf](http://trec.nist.gov/pubs/trec11/papers/irit.novelty.pdf)
- :material-file-search: **Runs:** [dumbrun](./runs.md#dumbrun)

??? abstract "Abstract"
	
	IRIT developed a new strategy in order to detect the relevant sentences that we did not try in a more general context of document retrieval but did try previously and partially in document categorization. In our approach a sentence is considered as relevant if it matches the topic with a certain level of coverage. This level of coverage depends on the category of the terms used in the texts. Three types of terms have been defined: highly relevant, lowly relevant and no relevant. With regard to the novelty part, a sentence is considered as novel when its levels of coverage with the previously processed sentences and with the best-matching sentences do not exceed certain thresholds.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DkakiMA02.bib) "
	```
	@inproceedings{DBLP:conf/trec/DkakiMA02,
		author = {Taoufiq Dkaki and Josiane Mothe and J{\'{e}}r{\^{o}}me Aug{\'{e}}},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Novelty Track at {IRIT-SIG}},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/irit.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DkakiMA02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THU TREC 2002: Novelty Track Experiments

_Min Zhang, Ruihua Song, Chuan Lin, Shaoping Ma, Zhe Jiang, Yijiang Jin, Yiqun Liu, Le Zhao_

- :fontawesome-solid-user-group: **Participant:** [tsinghua](./participants.md#tsinghua)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/tsinghuau.novelty2.pdf](http://trec.nist.gov/pubs/trec11/papers/tsinghuau.novelty2.pdf)
- :material-file-search: **Runs:** [thunv1](./runs.md#thunv1) | [thunv2](./runs.md#thunv2) | [thunv3](./runs.md#thunv3) | [thunv4](./runs.md#thunv4) | [thunv5](./runs.md#thunv5)

??? abstract "Abstract"
	
	This is the first time that Tsinghua University took part in TREC. In this year's novelty track, our basic idea is to find the key factor that help people find relevant and new information on a set of documents with noise. We paid attention to three points: 1. how to get full information from a short sentence; 2. how to complement hidden well-known knowledge to the sentences; 3. how to make the determination of duplication. Accordingly, expansion-based technologies are the key points. Studies of expansion technologies have been performed on three levels: efficient query expansion based on thesaurus and statistics, replacement-based document expansion, and term-expansion-related duplication elimination strategy based on overlapping measurement. Besides, two issues have been studied: finding key information in topics, and dynamic result selection. A new IR system has been developed for the task. In the system, four weighting strategies have been implemented: ltn.lnu [1], BM2500[2], FUB1 [3], FUB2 [3]. It provides both similarity and overlapping measurements, based on term expansion. Comparisons can be made on sentence-to-sentence or sentence-to-pool level.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangSLMJJLZ02.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangSLMJJLZ02,
		author = {Min Zhang and Ruihua Song and Chuan Lin and Shaoping Ma and Zhe Jiang and Yijiang Jin and Yiqun Liu and Le Zhao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THU} {TREC} 2002: Novelty Track Experiments},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/tsinghuau.novelty2.pdf},
		timestamp = {Wed, 16 Sep 2020 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhangSLMJJLZ02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Some Similarity Computation Methods in Novelty Detection

_Ming-Feng Tsai, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [NTU](./participants.md#ntu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/ntu.feng.final2.pdf](http://trec.nist.gov/pubs/trec11/papers/ntu.feng.final2.pdf)
- :material-file-search: **Runs:** [ntu1](./runs.md#ntu1) | [ntu2](./runs.md#ntu2) | [ntu3](./runs.md#ntu3)

??? abstract "Abstract"
	
	In the novelty task, the amount of information of a sentence that can be used in similarity computation is the major challenging issue. Some sort of information expansion methods was introduced to tackle this problem. Our approach to relevance identification was to expand the information of a sentence with the context of this sentence using a sliding window method. The similarity was measured by the number of words of a topic description that match the sentences within a window. Besides, WordNet was employed to relax word match operation to inexact match. In the novelty detection part, we first applied a coherent text segmentation algorithm to partition the sentences extracted from the relevance identification part into several coherent segments denoting sub-topics. Then we compute the similarity of each sentence with each segment. A sentence was in terms of a sentence-segment similarity vector. Two sentences are regarded as similar if they are related to the same sub-topics. In this way, the redundant sentences were filtered out.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TsaiC02.bib) "
	```
	@inproceedings{DBLP:conf/trec/TsaiC02,
		author = {Ming{-}Feng Tsai and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Some Similarity Computation Methods in Novelty Detection},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/ntu.feng.final2.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TsaiC02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Novelty Detection at Columbia University

_Barry Schiffman_

- :fontawesome-solid-user-group: **Participant:** [columbia_novelty](./participants.md#columbia_novelty)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/columbia.schiffman.pdf](http://trec.nist.gov/pubs/trec11/papers/columbia.schiffman.pdf)
- :material-file-search: **Runs:** [novcolcl35](./runs.md#novcolcl35) | [novcolclfx](./runs.md#novcolclfx) | [novcolmerg](./runs.md#novcolmerg) | [novcolsent](./runs.md#novcolsent) | [novcolcl85](./runs.md#novcolcl85)

??? abstract "Abstract"
	
	This paper describes the method we used for the Novelty Track for the 2002 Text Retrieval Conference (TREC). We tried to adapt tools we are developing for a task closely related to the novelty part of the this track. The system we are building will scan a stream of documents and present to the user only the new information it finds. For the 'relevance' part of the TREC, we decided to test the applicability of some of these tools. Since information retrieval is not a focus of our research, we thought it would be more interesting to use something new rather than try to hurriedly catch up. The results were far from satisfactory, but it is clear from the overall results that novelty detection remains a difficult and unsolved problem.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Schiffman02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Schiffman02,
		author = {Barry Schiffman},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Novelty Detection at Columbia University},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/columbia.schiffman.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Schiffman02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Michigan at TREC 2002: Question Answering and  Novelty Tracks

_Hong Qi, Jahna Otterbacher, Adam Winkel, Dragomir R. Radev_

- :fontawesome-solid-user-group: **Participant:** [umich](./participants.md#umich)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umichigan.radev.pdf](http://trec.nist.gov/pubs/trec11/papers/umichigan.radev.pdf)
- :material-file-search: **Runs:** [umich1](./runs.md#umich1) | [UMICH4](./runs.md#umich4) | [UMich3](./runs.md#umich3) | [UMich5](./runs.md#umich5) | [UMIch2](./runs.md#umich2)

??? abstract "Abstract"
	
	The University of Michigan participated in two evaluations this year. In the Question Answering Track, we entered three different versions of our system, NSIR, previously described in (1. For the Novelty Track, we modified our multi-document summarizer, MEAD (www.summarization.com/mead) and submitted five runs with different input parameters.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/QiOWR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/QiOWR02,
		author = {Hong Qi and Jahna Otterbacher and Adam Winkel and Dragomir R. Radev},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Michigan at {TREC} 2002: Question Answering and Novelty Tracks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umichigan.radev.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/QiOWR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Crude Cut at Query Expansion

_Philip Rennert_

- :fontawesome-solid-user-group: **Participant:** [streamsage](./participants.md#streamsage)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/streamsage.rennert.pdf](http://trec.nist.gov/pubs/trec11/papers/streamsage.rennert.pdf)
- :material-file-search: **Runs:** [ss1](./runs.md#ss1)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Rennert02.bib) "
	```
	@inproceedings{DBLP:conf/trec/Rennert02,
		author = {Philip Rennert},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Crude Cut at Query Expansion},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/streamsage.rennert.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Rennert02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at TREC 2002

_Christof Monz, Jaap Kamps, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uva](./participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf](http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf)
- :material-file-search: **Runs:** [UAmsT11ntste](./runs.md#uamst11ntste) | [UAmsT11ntlem](./runs.md#uamst11ntlem) | [UAmsT11ntcom](./runs.md#uamst11ntcom)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2002 Novelty, Question answering, and Web tracks. We provide a detailed account of the ideas underlying our approaches to these tasks. All our runs used the FlexIR information retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MonzKR02.bib) "
	```
	@inproceedings{DBLP:conf/trec/MonzKR02,
		author = {Christof Monz and Jaap Kamps and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at {TREC} 2002},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/uamsterdam.derijke.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MonzKR02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2002: Cross Language and Novelty Tracks

_Leah S. Larkey, James Allan, Margaret E. Connell, Alvaro Bolivar, Courtney Wade_

- :fontawesome-solid-user-group: **Participant:** [umass](./participants.md#umass)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec11/papers/umass.wade.pdf](http://trec.nist.gov/pubs/trec11/papers/umass.wade.pdf)
- :material-file-search: **Runs:** [CIIR02tfkl](./runs.md#ciir02tfkl) | [CIIR02tfnew](./runs.md#ciir02tfnew)

??? abstract "Abstract"
	
	The University of Massachusetts participated in the cross-language and novelty tracks this year. The cross-language submission was characterized by combination of evidence to merge results from two different retrieval engines and a variety of different resources - stemmers, dictionaries, machine translation, and an acronym database. We found that proper names were extremely important in this year's queries. For the novelty track, we applied variants of techniques that have been employed for other problems. In addition, we created additional training data by manually annotating 48 additional topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LarkeyACBW02.bib) "
	```
	@inproceedings{DBLP:conf/trec/LarkeyACBW02,
		author = {Leah S. Larkey and James Allan and Margaret E. Connell and Alvaro Bolivar and Courtney Wade},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2002: Cross Language and Novelty Tracks},
		booktitle = {Proceedings of The Eleventh Text REtrieval Conference, {TREC} 2002, Gaithersburg, Maryland, USA, November 19-22, 2002},
		series = {{NIST} Special Publication},
		volume = {500-251},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2002},
		url = {http://trec.nist.gov/pubs/trec11/papers/umass.wade.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LarkeyACBW02.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

