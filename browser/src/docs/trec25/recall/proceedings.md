# Proceedings - Total Recall 2016 

#### TREC 2016 Total Recall Track Overview

_Maura R. Grossman, Gordon V. Cormack, Adam Roegiest_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Overview-TR.pdf](http://trec.nist.gov/pubs/trec25/papers/Overview-TR.pdf)
??? abstract "Abstract"
	
	The primary purpose of the Total Recall Track is to evaluate, through controlled simulation, methods designed to achieve very high recall - as close as practicable to 100% - with a human assessor in the loop. Motivating applications include, among others, electronic discovery in legal proceedings [3], systematic review in evidence-based medicine [6], and the creation of fully labeled test collections for information retrieval (“IR”) evaluation [5]. A secondary, but no less important, purpose is to develop a sandboxed virtual test environment within which IR systems may be tested, while preventing the disclosure of sensitive test data to participants. At the same time, the test environment also operates as a “black box,” affording participants confidence that their proprietary systems cannot easily be reverse engineered. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossmanCR16.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossmanCR16,
		author = {Maura R. Grossman and Gordon V. Cormack and Adam Roegiest},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2016 Total Recall Track Overview},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Overview-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossmanCR16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### "When to Stop" Waterloo (Cormack) Participation in the TREC 2016  Total Recall Track

_Gordon V. Cormack, Maura R. Grossman_

- :fontawesome-solid-user-group: **Participant:** [WaterlooCormack](./participants.md#waterloocormack)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/WaterlooCormack-TR.pdf](http://trec.nist.gov/pubs/trec25/papers/WaterlooCormack-TR.pdf)
- :material-file-search: **Runs:** [UWathome4Knee](./runs.md#uwathome4knee) | [UWathome4descKnee](./runs.md#uwathome4descknee) | [UWathome4Target](./runs.md#uwathome4target) | [UWathome4descTarget](./runs.md#uwathome4desctarget) | [UWathome4descBaseline](./runs.md#uwathome4descbaseline) | [UWathome4Baseline](./runs.md#uwathome4baseline) | [uwsandboxknee](./runs.md#uwsandboxknee) | [uwsandboxtarget](./runs.md#uwsandboxtarget)

??? abstract "Abstract"
	
	In the course of developing tools for the 2015 Total Recal Track, Track Co-Coordinators Gordon V. Cormack and Maura R. Grossman created an autonomous continuous active learning (“CAL”) system, which was provided to participants as the baseline model implementation (“BMI”) [http://plg.uwaterloo.ca/∼gvcormac/trecvm/]. BMI employs the technology-assisted review (“TAR”) approach described by Cormack and Grossman [2]; the only difference is that BMI employs logistic regression implemented by Sofia ML [https://code.google.com/p/sofia-ml/], instead of SVMlight [http://svmlight.joachims.org/]. BMI was reprised, unchanged from TREC 2015, except for the addition of a default “call-your-shot” stopping rule indicating the system's estimate of the point at which a reasonable compromise between recall and effort had been achieved. [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CormackG16.bib) "
	```
	@inproceedings{DBLP:conf/trec/CormackG16,
		author = {Gordon V. Cormack and Maura R. Grossman},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {"When to Stop" Waterloo (Cormack) Participation in the {TREC} 2016 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/WaterlooCormack-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CormackG16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2016 Total Recall Track

_Ralph Losey, Jackson Lewis P. C., Jim Sullivan, Tony Reichenberger, Levi Kuehn, Jani Grant_

- :fontawesome-solid-user-group: **Participant:** [e-discoveryteam](./participants.md#e-discoveryteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/e-Discoveryteam-TR.pdf](http://trec.nist.gov/pubs/trec25/papers/e-Discoveryteam-TR.pdf)
- :material-file-search: **Runs:** [Run1](./runs.md#run1)

??? abstract "Abstract"
	
	The e-Discovery Team participated in the 2016 TREC Total Recall Track, Athome division, where thirty-four prejudged topics were considered using 290,099 emails of former Florida Governor Jeb Bush. The Team participated in TREC 2016 primarily to test the effectiveness of the standard search methodology it uses commercially to search for relevant evidence in legal proceedings: Predictive Coding 4.0 Hybrid Multimodal IST. The Team's method uses a hybrid approach to continuous active learning with both manual searches and active machine learning based document ranking searches. This is a systematic process involving implementation of a variety of search functions by skilled searchers. The Team calls this type of search multimodal because all types of search methods are used. A single expert reviewer was used in each topic along with Kroll Ontrack's search and review software, eDiscovery.com Review (EDR). The Team classified 9,863,366 documents as either relevant or irrelevant in all 34 review projects. A total of 34,723 documents were correctly classified as Relevant, as per the Team's judgment and corrected standard. The 34,723 relevant documents were found by manual review of 6,957 documents, taking a total of 234.25 man-hours. This represent an average project time of 6.89 hours per topic. The Team thus reviewed and classified documents at an average speed of 42,106 files per hour. The Team's attained an average 88% Recall score across all 34 topics using the corrected standard. The Team also attained F1 scores of greater than 90% in twelve topics, including two perfect scores of 100% F1.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LoseyCSRKG16.bib) "
	```
	@inproceedings{DBLP:conf/trec/LoseyCSRKG16,
		author = {Ralph Losey and Jackson Lewis P. C. and Jim Sullivan and Tony Reichenberger and Levi Kuehn and Jani Grant},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2016 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/e-Discoveryteam-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LoseyCSRKG16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Padua (IMS) at TREC 2016 Total Recall Track

_Giorgio Maria Di Nunzio, Maria Maistro, Daniel Zilio_

- :fontawesome-solid-user-group: **Participant:** [ims_unipd](./participants.md#ims_unipd)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/ims_unipd-TR.pdf](http://trec.nist.gov/pubs/trec25/papers/ims_unipd-TR.pdf)
- :material-file-search: **Runs:** [baseline_bm25](./runs.md#baseline_bm25) | [baseline_bm25_smoothing](./runs.md#baseline_bm25_smoothing) | [auto_shift_rotation](./runs.md#auto_shift_rotation) | [auto_shift_rotation_exp](./runs.md#auto_shift_rotation_exp)

??? abstract "Abstract"
	
	The participation of the Information Management System (IMS) Group of the University of Padua in the Total Recall track at TREC 2016 consisted in a set of fully automated experiments based on the two-dimensional probabilistic model. We trained the model in two ways that tried to mimic a real user, and we compared it to two versions of the BM25 model with different parameter settings. This initial set of experiments lays the ground for a wider study that will explore a gamification approach in the context of high recall situations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NunzioMZ16.bib) "
	```
	@inproceedings{DBLP:conf/trec/NunzioMZ16,
		author = {Giorgio Maria Di Nunzio and Maria Maistro and Daniel Zilio},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {The University of Padua {(IMS)} at {TREC} 2016 Total Recall Track},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/ims\_unipd-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NunzioMZ16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### An Exploration of Total Recall with Multiple Manual Seedings

_Jeremy Pickens, Tom Gricks, Bayu Hardi, Mark Noel, John Tredennick_

- :fontawesome-solid-user-group: **Participant:** [catres](./participants.md#catres)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/catres-TR.pdf](http://trec.nist.gov/pubs/trec25/papers/catres-TR.pdf)
- :material-file-search: **Runs:** [manual_seed](./runs.md#manual_seed)

??? abstract "Abstract"
	
	The Catalyst participation in the manual at home Total Recall Track had one fundamental question at the core of its run: What effect various kinds of limited human effort have on a total recall process. Our two primary modes were one-shot (single query) and interactive (multiple queries).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PickensGHNT16.bib) "
	```
	@inproceedings{DBLP:conf/trec/PickensGHNT16,
		author = {Jeremy Pickens and Tom Gricks and Bayu Hardi and Mark Noel and John Tredennick},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {An Exploration of Total Recall with Multiple Manual Seedings},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/catres-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PickensGHNT16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Webis at TREC 2016: Tasks, Total Recall, and Open Search Tracks

_Matthias Hagen, Johannes Kiesel, Payam Adineh, Masoud Alahyari, Ehsan Fatehifar, Arefeh Bahrami, Pia Fichtl, Benno Stein_

- :fontawesome-solid-user-group: **Participant:** [Webis](./participants.md#webis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf](http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf)

??? abstract "Abstract"
	
	We give a brief overview of the Webis group's participation in the TREC 2016 Tasks, Total Recall, and Open Search tracks. Our submissions to the Tasks track are similar to our last year's system. In the task understanding subtask of the Tasks track, we use different data sources (ClueWeb12 anchor texts, AOL query log, Wikidata, etc.) and APIs (Google, Bing, etc.) to retrieve suggestions related to a given query. For the task completion and ad-hoc subtask, we combine the results of the Indri search engine for the different related queries identified in the task understanding subtask. Our system for the the Total Recall track also is similar to our last year's idea with some slight changes in the details; we employ a simple SVM baseline with variable batch sizes equipped with a keyqueries step to identify potentially relevant documents. In the Open Search track, we axiomatically re-rank a BM25-ordered result list to come up with a final document ranking
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HagenKAAFBFS16.bib) "
	```
	@inproceedings{DBLP:conf/trec/HagenKAAFBFS16,
		author = {Matthias Hagen and Johannes Kiesel and Payam Adineh and Masoud Alahyari and Ehsan Fatehifar and Arefeh Bahrami and Pia Fichtl and Benno Stein},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Webis at {TREC} 2016: Tasks, Total Recall, and Open Search Tracks},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/Webis-T-TR-O.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HagenKAAFBFS16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### San Francisco State University (SFSU) at Total Recall Track of TREC  2016

_Mon-Shih Chuang, Anagha Kulkarni_

- :fontawesome-solid-user-group: **Participant:** [IR.SFSU.2016](./participants.md#ir.sfsu.2016)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec25/papers/IR.SFSU.2016-TR.pdf](http://trec.nist.gov/pubs/trec25/papers/IR.SFSU.2016-TR.pdf)
- :material-file-search: **Runs:** [ah4_run1](./runs.md#ah4_run1) | [ah4_run2_seed_expansion](./runs.md#ah4_run2_seed_expansion) | [ah4_descsubset](./runs.md#ah4_descsubset) | [sandbox_run](./runs.md#sandbox_run)

??? abstract "Abstract"
	
	This paper describes the participation of San Francisco State University group in Text Retrieval Conference (TREC) 2016 Total Recall Track from National Institute of Standard and Technology (NIST). The TREC series provide large test collections and judgements for participant to design Information Retrieval (IR) systems for different proposes. The purpose of Total Recall Track is seeking text search system which achieves high recall with minimum number of return documents. This year, our team participates all automatic tasks, including 34 topics in athome task and 2 datasets in sandbox task. Our system is built based on the autonomous technology-assisted review (Auto TAR) model[1], which is also the baseline of Total Recall Track. In this paper, we will introduce several approaches which have improved the evaluation metrics compare to the baseline model. Our enhanced model combines seed expansion and feature engineering including adding n-gram, eliminating stop words, and preserving words contain digits.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ChuangK16.bib) "
	```
	@inproceedings{DBLP:conf/trec/ChuangK16,
		author = {Mon{-}Shih Chuang and Anagha Kulkarni},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {San Francisco State University {(SFSU)} at Total Recall Track of {TREC} 2016},
		booktitle = {Proceedings of The Twenty-Fifth Text REtrieval Conference, {TREC} 2016, Gaithersburg, Maryland, USA, November 15-18, 2016},
		series = {{NIST} Special Publication},
		volume = {500-321},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2016},
		url = {http://trec.nist.gov/pubs/trec25/papers/IR.SFSU.2016-TR.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ChuangK16.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

