# Proceedings - Crowdsourcing 2011 

#### MSRC at TREC 2011 Crowdsourcing Track

_Paul Bennett, Ece Kamar, Gabriella Kazai_

- :fontawesome-solid-user-group: **Participant:** [MSRC](./participants.md#msrc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/MSRC.crowdsourcing.update.pdf](http://trec.nist.gov/pubs/trec20/papers/MSRC.crowdsourcing.update.pdf)

??? abstract "Abstract"
	
	Crowdsourcing useful data, such as reliable relevance labels for pairs of topics and documents, requires a multidisciplinary approach that spans aspects such as user interface and interaction design, incentives, crowd engagement and management, and spam detection and filtering. Research has shown that the design of a crowdsourcing task can significantly impact the quality of the obtained data, where the geographic location of crowd workers was found to be a main indicator of quality. Following this, for the Assessment task of the TREC crowdsourcing track, we designed HITs to minimize attracting spam workers, and restricted participation to workers in the US. As an incentive, we included the possibility of a bonus pay of $5 for the best performing workers. When crowdsourcing relevance judgments, multiple judgments are typically obtained to provide greater certainty as to the true label. However, combining these judgments by a simple majority vote not only has the flawed underlying assumption that each assessor has comparable accuracy but also ignores the impact of topic specific effects (e.g. the amount of topic-expertise needed to accurately judge). We provide a simple probabilistic framework for predicting true relevance from crowdsourced judgments and explore variations that condition on worker and topic. In particular, we focus on the topic conditional model that was our primary submission for the Consensus task of the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BennettKK11.bib) "
	```
	@inproceedings{DBLP:conf/trec/BennettKK11,
		author = {Paul Bennett and Ece Kamar and Gabriella Kazai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{MSRC} at {TREC} 2011 Crowdsourcing Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/MSRC.crowdsourcing.update.pdf},
		timestamp = {Thu, 28 Apr 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/BennettKK11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Iowa at TREC 2011: Microblogs, Medical Records  and Crowdsourcing

_Sanmitra Bhattacharya, Christopher G. Harris, Yelena Mejova, Chao Yang, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [UIowaS](./participants.md#uiowas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf)

??? abstract "Abstract"
	
	The Text Retrieval and Text Mining group at the University of Iowa participated in three tracks, all new tracks introduced this year: Microblog, Medical Records (Med) and Crowdsourcing. Details of our strategies are provided in this paper. Overall our effort has been fruitful in that we have been able to understand more about the nature of medical records and Twitter messages, and also the merits and challenges of working with games as a framework for gathering relevance judgments.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Bhattacharya0MYS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Bhattacharya0MYS11,
		author = {Sanmitra Bhattacharya and Christopher G. Harris and Yelena Mejova and Chao Yang and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Iowa at {TREC} 2011: Microblogs, Medical Records and Crowdsourcing},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UIowaS.microblog.medical.crowdsourcing.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Bhattacharya0MYS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Hierarchical Bayesian Model of Crowdsourced Relevance Coding

_Bob Carpenter_

- :fontawesome-solid-user-group: **Participant:** [LingPipe](./participants.md#lingpipe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/LingPipe.crowdsourcing.pdf](http://trec.nist.gov/pubs/trec20/papers/LingPipe.crowdsourcing.pdf)
- :material-file-search: **Runs:** [LingPipeSemi](./runs.md#lingpipesemi) | [LingPipeUn](./runs.md#lingpipeun) | [LingPipeSBin](./runs.md#lingpipesbin)

??? abstract "Abstract"
	
	We apply a generative probabilistic model of noisy crowdsourced coding to overlapping relevance judgments for documents in several topics (queries). We demonstrate the model's utility for Task 2 of the 2011 TREC Crowdsourcing Track (Karzai and Lease 2011). Our model extends Dawid and Skene's (1979) approach to inferring gold standards from noisy coding in several ways: we add a hierarchical model of prevalence of relevant documents in multiple topics (queries), semi-supervision using known gold labels, and hierarchically modeled priors for coder sensitivity and specificity. We also replace Dawid and Skene's maximum likelihood point estimates with full Bayesian inference using Gibbs sampling and generalize their full-panel design in which every coder labels every document to a fully ad hoc design in which a coder may label each document zero, one or more times.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Carpenter11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Carpenter11,
		author = {Bob Carpenter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Hierarchical Bayesian Model of Crowdsourced Relevance Coding},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/LingPipe.crowdsourcing.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Carpenter11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### GeAnn at the TREC 2011 Crowdsourcing Track

_Carsten Eickhoff, Christopher G. Harris, Padmini Srinivasan, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [GeAnn](./participants.md#geann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/GeAnn.crowdsourcing.pdf](http://trec.nist.gov/pubs/trec20/papers/GeAnn.crowdsourcing.pdf)
- :material-file-search: **Runs:** [G6T1R1](./runs.md#g6t1r1) | [G6T2R1](./runs.md#g6t2r1) | [G6T2R2](./runs.md#g6t2r2) | [G6T2R3](./runs.md#g6t2r3)

??? abstract "Abstract"
	
	Relevance assessments of information retrieval results are often created by domain experts. This expertise is typically expensive in terms of money or personal effort. The TREC 2011 crowdsourcing track aims to evaluate different strategies of crowdsourcing relevance judgements. This work describes the joint participation of Delft University of Technology and The University of Iowa, using GeAnn, a term association game, we generate relevance judgements in an engaging way that encourages quality submissions, which otherwise would have to be motivated through rigid quality control mechanisms and additional incentives such as higher monetary rewards.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Eickhoff0SV11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Eickhoff0SV11,
		author = {Carsten Eickhoff and Christopher G. Harris and Padmini Srinivasan and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {GeAnn at the {TREC} 2011 Crowdsourcing Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/GeAnn.crowdsourcing.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Eickhoff0SV11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT at the Crowdsourcing Track of TREC 2011

_Matthias Petri, Mark Sanderson, Falk Scholer_

- :fontawesome-solid-user-group: **Participant:** [RMIT](./participants.md#rmit)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/RMIT.crowdsourcing.pdf](http://trec.nist.gov/pubs/trec20/papers/RMIT.crowdsourcing.pdf)
- :material-file-search: **Runs:** [RMITT1](./runs.md#rmitt1)

??? abstract "Abstract"
	
	In this paper we describe our submission to the crowdsourcing track of TREC 2011. We first describe our crowdsourcing environment. Next we evaluate our approach and discuss our results. We conclude with a discussion of problems encountered during our participation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/PetriSS11.bib) "
	```
	@inproceedings{DBLP:conf/trec/PetriSS11,
		author = {Matthias Petri and Mark Sanderson and Falk Scholer},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} at the Crowdsourcing Track of {TREC} 2011},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/RMIT.crowdsourcing.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/PetriSS11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Crowdsourcing with a Crowd of One and Other TREC 2011 Crowdsourcing  and Web Track Experiments

_Mark D. Smucker_

- :fontawesome-solid-user-group: **Participant:** [UWaterlooMDS](./participants.md#uwaterloomds)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/UWaterlooMDS.crowd.update.pdf](http://trec.nist.gov/pubs/trec20/papers/UWaterlooMDS.crowd.update.pdf)
- :material-file-search: **Runs:** [UWatCS1Human](./runs.md#uwatcs1human) | [UWatCS2Semi](./runs.md#uwatcs2semi) | [UWatCS2Unsup](./runs.md#uwatcs2unsup)

??? abstract "Abstract"
	
	Our submissions to the Crowdsourcing and Web tracks emphasized simplicity in either method, construction or both. Based on preliminary results, we found that if the number of relevance assessments is low, researchers may be better off “self-sourcing” the assessments, i.e. performing the relevance assessments themselves, rather than crowdsourcing the work. For the Crowdsourcing consensus task, we found that a simple weighted majority vote with iteratively refined workers' quality as measured by d′ (d-prime) performed slightly above the median on the gold test set. Finally, we submitted easy to construct runs to the Web ad-hoc track which had P@10 scores above the median on a majority of the topics.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Smucker11.bib) "
	```
	@inproceedings{DBLP:conf/trec/Smucker11,
		author = {Mark D. Smucker},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Crowdsourcing with a Crowd of One and Other {TREC} 2011 Crowdsourcing and Web Track Experiments},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/UWaterlooMDS.crowd.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Smucker11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University Carlos III of Madrid at TREC 2011 Crowdsourcing  Track

_Julián Urbano, Mónica Marrero, Diego Martín, Jorge Morato, Karina Robles, Juan Lloréns_

- :fontawesome-solid-user-group: **Participant:** [uc3m](./participants.md#uc3m)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uc3m.crowd.update.pdf](http://trec.nist.gov/pubs/trec20/papers/uc3m.crowd.update.pdf)
- :material-file-search: **Runs:** [uc3m.graded](./runs.md#uc3m.graded) | [uc3m.slider](./runs.md#uc3m.slider) | [uc3m.hterms](./runs.md#uc3m.hterms) | [uc3m.rule](./runs.md#uc3m.rule) | [uc3m.svn](./runs.md#uc3m.svn) | [uc3m.wordnet](./runs.md#uc3m.wordnet)

??? abstract "Abstract"
	
	This paper describes the participation of the uc3m team in both tasks of the TREC 2011 Crowdsourcing Track. For the first task we submitted three runs that used Amazon Mechanical Turk: one where workers made relevance judgments based on a 3-point scale, and two similar runs where workers provided an explicit ranking of documents. All three runs implemented a quality control mechanism at the task level based on a simple reading comprehension test. For the second task we also submitted three runs: one with a stepwise execution of the GetAnotherLabel algorithm and two others with a rule-based and a SVM-based model. According to the NIST gold labels, our runs performed very well in both tasks, ranking at the top for most measures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UrbanoMMMRL11.bib) "
	```
	@inproceedings{DBLP:conf/trec/UrbanoMMMRL11,
		author = {Juli{\'{a}}n Urbano and M{\'{o}}nica Marrero and Diego Mart{\'{\i}}n and Jorge Morato and Karina Robles and Juan Llor{\'{e}}ns},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University Carlos {III} of Madrid at {TREC} 2011 Crowdsourcing Track},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uc3m.crowd.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/UrbanoMMMRL11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Managing the Quality of Large-Scale Crowdsourcing

_Jeroen B. P. Vuurens, Carsten Eickhoff, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [TUD_DMIR](./participants.md#tud_dmir)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/TUD_DMIR.crowdsourcing.4-20update.pdf](http://trec.nist.gov/pubs/trec20/papers/TUD_DMIR.crowdsourcing.4-20update.pdf)
- :material-file-search: **Runs:** [DMIR1](./runs.md#dmir1) | [DMIR2](./runs.md#dmir2) | [DMIR3](./runs.md#dmir3)

??? abstract "Abstract"
	
	Crowdsourcing can be used to obtain relevance judgments needed for the evaluation of information retrieval systems. However, the quality of crowdsourced relevance judgments may be questionable; a substantial amount of workers appear to spam HITs in order to maximize their hourly wages, and workers may know less than expert annotators about the topic being queried. The task for the TREC 2011 Crowdsourcing track was to obtain high-quality relevance judgments. The quality of obtained annotations is improved by removing random judgments and aggregating multiple annotations per query-document pair. We conclude that crowdsourcing can be used as a feasible alternative to expert annotations, based on the estimated proportions of correctly judged query-document pairs in the crowdsourced relevance judgments and previous TREC qrels.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/VuurensEV11.bib) "
	```
	@inproceedings{DBLP:conf/trec/VuurensEV11,
		author = {Jeroen B. P. Vuurens and Carsten Eickhoff and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Managing the Quality of Large-Scale Crowdsourcing},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/TUD\_DMIR.crowdsourcing.4-20update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/VuurensEV11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow (qirdcsuog) at TREC Crowdsourcing 2011: TurkRank-Network-based  Worker Ranking in Crowdsourcing

_Stewart Whiting, Jesus A. Rodriguez Perez, Guido Zuccon, Teerapong Leelanupab, Joemon M. Jose_

- :fontawesome-solid-user-group: **Participant:** [qirdcsuog](./participants.md#qirdcsuog)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/qirdcsuog.crowd.update.pdf](http://trec.nist.gov/pubs/trec20/papers/qirdcsuog.crowd.update.pdf)
- :material-file-search: **Runs:** [beta0](./runs.md#beta0) | [beta04](./runs.md#beta04) | [beta08](./runs.md#beta08)

??? abstract "Abstract"
	
	For TREC Crowdsourcing 2011 (Stage 2) we propose a network-based approach for assigning an indicative measure of worker trustworthiness in crowdsourced labelling tasks. Workers, the gold standard and worker/gold standard agreements are modelled as a network. For the purpose of worker trustworthiness assignment, a variant of the PageRank algorithm, named TurkRank, is used to adaptively combine evidence that suggests worker trustworthiness, i.e., agreement with other trustworthy co-workers and agreement with the gold standard. A single parameter controls the importance of co-worker agreement versus gold standard agreement. The TurkRank score calculated for each worker is incorporated with a worker-weighted mean label aggregation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WhitingPZLJ11.bib) "
	```
	@inproceedings{DBLP:conf/trec/WhitingPZLJ11,
		author = {Stewart Whiting and Jesus A. Rodriguez Perez and Guido Zuccon and Teerapong Leelanupab and Joemon M. Jose},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow (qirdcsuog) at {TREC} Crowdsourcing 2011: TurkRank-Network-based Worker Ranking in Crowdsourcing},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/qirdcsuog.crowd.update.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WhitingPZLJ11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BUPT_WILDCAT at TREC Crowdsourcing Track: Crowdsourcing for Relevance  Evaluation

_Tao Xia, Chuang Zhang, Tai Li, Jingjing Xie_

- :fontawesome-solid-user-group: **Participant:** [BUPT_WILDCAT](./participants.md#bupt_wildcat)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/BUPT_WILDCAT.crowd.new.pdf](http://trec.nist.gov/pubs/trec20/papers/BUPT_WILDCAT.crowd.new.pdf)
- :material-file-search: **Runs:** [BUPTWildCat1](./runs.md#buptwildcat1) | [BUPTWildCat2](./runs.md#buptwildcat2) | [wildcatrun](./runs.md#wildcatrun)

??? abstract "Abstract"
	
	In recent years, crowdsourcing has become an effective method in many fields, such as relecance evaluation. Based on our experiment carried out in Beijing University of Posts and Telecommunications for the TREC 2011 Crowdsourcing track, in this paper we introduce our strategies in recruiting workers, obtaining their relevance and rank juegements and quality control. Then we explain the improved EM algorithm and Gaussian model that we make use of to calculate the consensus of labels. The result shows that our stategies and algorithms are effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/XiaZLX11.bib) "
	```
	@inproceedings{DBLP:conf/trec/XiaZLX11,
		author = {Tao Xia and Chuang Zhang and Tai Li and Jingjing Xie},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BUPT{\_}WILDCAT at {TREC} Crowdsourcing Track: Crowdsourcing for Relevance Evaluation},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/BUPT\_WILDCAT.crowd.new.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/XiaZLX11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2011: Experiments with Terrier in  Crowdsourcing, Microblog, and Web Tracks

_Richard McCreadie, Craig Macdonald, Rodrygo L. T. Santos, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf](http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf)
- :material-file-search: **Runs:** [uogTrP1rg](./runs.md#uogtrp1rg) | [uogTrP2O4wtr](./runs.md#uogtrp2o4wtr) | [uogTrP2O4wte](./runs.md#uogtrp2o4wte) | [uogTrP2O4teh](./runs.md#uogtrp2o4teh)

??? abstract "Abstract"
	
	In TREC 2011, we focus on tackling the new challenges proposed by the pilot Crowdsourcing and Microblog tracks, using our Terrier Information Retrieval Platform. Meanwhile, we continue to build upon our novel xQuAD framework and data-driven ranking approaches within Terrier to achieve effective and efficient ranking for the TREC Web track. In particular, the aim of our Microblog track participation is the development of a learning to rank approach for filtering within a tweet ranking environment, where tweets are ranked in reverse chronological order. In the Crowdsourcing track, we work to achieve a closer integration between the crowdsourcing marketplaces that are used for relevance assessment, and Terrier, which produces the document rankings to be assessed. Moreover, we focus on generating relevance assessments quickly and at a minimal cost. For the Web track, we enhance the data-driven learning support within Terrier by proposing a novel framework for the fast computation of document features for learning to rank.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieMSO11.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieMSO11,
		author = {Richard McCreadie and Craig Macdonald and Rodrygo L. T. Santos and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2011: Experiments with Terrier in Crowdsourcing, Microblog, and Web Tracks},
		booktitle = {Proceedings of The Twentieth Text REtrieval Conference, {TREC} 2011, Gaithersburg, Maryland, USA, November 15-18, 2011},
		series = {{NIST} Special Publication},
		volume = {500-296},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2011},
		url = {http://trec.nist.gov/pubs/trec20/papers/uogTr.crowd.microblog.web.update4-20.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieMSO11.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

